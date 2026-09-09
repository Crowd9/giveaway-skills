#!/usr/bin/env python3
"""Provably fair random draw with an audit record. Python 3.8+, no dependencies.

Input: CSV or TSV with a header, one id per line, or a JSON export of comments or entrants (a list, or an object holding one,
with the person named by a field such as username, author, handle, email or owner.username). Pass --id-column to override.

  python3 draw.py commit  entries.csv --tiers "Grand prize:1,Runner-up:5" [--backups 2] [--id-column email]
                          [--weight-column entries] [--exclude staff.txt] [--draw-at "2026-09-12T09:00:00+10:00"]
  python3 draw.py draw    entries.csv --tiers ... [same options] (--seed TEXT | --seed-drand ROUND | --seed-nist UNIXTIME)
                          [--audit draw.json] [--winners-csv winners.csv] [--mask]
  python3 draw.py verify  draw.json [--input entries.csv]
  python3 draw.py --self-test

How the draw works (documented so anyone can recheck it in any language):
  1. Entrants are read, ids trimmed and lower-cased, duplicates merged (weights add up when a weight column is given),
     exclusions removed, invalid or zero weights dropped.
  2. The seed is a public string: text you published in advance, or the randomness of a drand round or NIST beacon
     pulse chosen in advance and fetched after it existed.
  3. Each entrant gets key = u ** (1 / weight), where u = SHA-256(seed + "|" + id) read as a number in (0, 1).
     This is Efraimidis-Spirakis weighted sampling without replacement. With no weights it is a uniform draw.
  4. Entrants are sorted by key, highest first. Tiers and backups are filled in that order.
  The audit record holds the SHA-256 of the input, the rules, the seed and its source, and every winner's key,
  so `verify` (or a few lines in any language) reproduces the result exactly.

commit prints a commitment (hash of the input plus the rules) to publish before the seed exists. With --draw-at it
also prints the drand round that will be produced at that time, so the seed source can be announced in advance.
"""
import argparse, csv, hashlib, io, json, math, sys, datetime, urllib.request

VERSION = "2.1.0"
DRAND = {"url": "https://api.drand.sh", "genesis_time": 1595431050, "period": 30, "chain_hash": "8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce"}
NIST = "https://beacon.nist.gov/beacon/2.0/pulse"

def sha(b): return hashlib.sha256(b).hexdigest()
def norm(s): return (s or "").strip().lower()

ID_KEYS = ("email", "Email", "id", "ID", "entrant", "username", "user_name", "handle", "author", "name", "Name", "owner", "user", "from")

def _flatten_json(obj):
    """Best-effort: find the list of comment or entrant objects inside a JSON export and the field that names the person."""
    if isinstance(obj, dict):
        for k in ("comments", "data", "entries", "items", "results", "comments_media_comments", "rows"):
            if isinstance(obj.get(k), list): obj = obj[k]; break
        else:
            lists = [v for v in obj.values() if isinstance(v, list)]
            obj = lists[0] if lists else [obj]
    rows = []
    for it in obj:
        if isinstance(it, str): rows.append({"entrant": it}); continue
        if not isinstance(it, dict): continue
        flat = {}
        for k, v in it.items():
            if isinstance(v, dict):
                for k2, v2 in v.items():
                    if isinstance(v2, (str, int, float)): flat[f"{k}.{k2}"] = v2
            elif isinstance(v, (str, int, float)): flat[k] = v
        rows.append(flat)
    return rows

def pick_id_column(rows, id_column):
    if id_column:
        if id_column not in rows[0]: sys.exit(f"column '{id_column}' not found; columns are {list(rows[0].keys())}")
        return id_column
    keys = list(rows[0].keys())
    for cand in ID_KEYS:
        for k in keys:
            if k == cand or k.endswith("." + cand): return k
    return keys[0]

def load_entries(path, id_column):
    raw = open(path, "rb").read(); text = raw.decode("utf-8-sig")
    stripped = text.lstrip()
    if stripped.startswith("[") or stripped.startswith("{"):
        rows = _flatten_json(json.loads(text))
        if not rows: sys.exit("no entries found in the JSON export")
        return rows, pick_id_column(rows, id_column), sha(raw)
    lines = [l for l in text.splitlines() if l.strip()]
    if not lines: sys.exit("no entries in input")
    if "," in lines[0] or "\t" in lines[0]:
        dialect = csv.excel_tab if "\t" in lines[0] and "," not in lines[0] else csv.excel
        rows = list(csv.DictReader(io.StringIO(text), dialect=dialect))
        return rows, pick_id_column(rows, id_column), sha(raw)
    return [{"entrant": l.strip()} for l in lines], "entrant", sha(raw)

def prepare(rows, id_column, weight_column, exclude):
    seen, entrants, dupes, excluded, bad = {}, [], 0, 0, 0
    for r in rows:
        key = norm(r.get(id_column))
        if not key: continue
        if key in exclude: excluded += 1; continue
        w = 1.0
        if weight_column:
            try: w = float(r.get(weight_column) or 0)
            except ValueError: w = 0.0
            if w <= 0: bad += 1; continue
        if key in seen:
            dupes += 1
            if weight_column: seen[key]["weight"] += w
            continue
        seen[key] = {"id": key, "shown": r.get(id_column).strip(), "weight": w}; entrants.append(seen[key])
    plus = {}
    for e in entrants:
        if "@" in e["id"]:
            local, _, dom = e["id"].partition("@"); plus.setdefault(local.split("+")[0] + "@" + dom, []).append(e["id"])
    clusters = {k: v for k, v in plus.items() if len(v) > 1}
    return entrants, dupes, excluded, bad, clusters

def rank(entrants, seed):
    for e in entrants:
        h = hashlib.sha256((seed + "|" + e["id"]).encode()).digest()
        u = (int.from_bytes(h[:8], "big") + 0.5) / 2 ** 64          # uniform in (0, 1), never exactly 0 or 1
        e["u"] = u; e["key"] = u ** (1.0 / e["weight"])
    return sorted(entrants, key=lambda e: (-e["key"], e["id"]))

def parse_tiers(spec, winners):
    if not spec: return [["Winner", winners]]
    out = []
    for part in spec.split(","):
        name, _, count = part.rpartition(":"); out.append([name.strip() or "Prize", int(count)])
    return out

def rules_of(a, id_column, tiers):
    return {"id_column": id_column, "weight_column": a.weight_column, "exclude_file_sha256": sha(open(a.exclude, "rb").read()) if a.exclude else None,
            "tiers": tiers, "backups": a.backups, "method": "sha256(seed|id) -> u in (0,1); key = u^(1/weight); highest keys win; ties by id", "tool_version": VERSION}

def commitment(digest, rules): return sha((digest + "\n" + json.dumps(rules, sort_keys=True, separators=(",", ":"))).encode())

def drand_round_at(ts): return int((ts - DRAND["genesis_time"]) // DRAND["period"]) + 1
def drand_round_time(r): return DRAND["genesis_time"] + (r - 1) * DRAND["period"]

def fetch_json(url):
    with urllib.request.urlopen(url, timeout=20) as r: return json.load(r)

def seed_from(a):
    if a.seed is not None: return a.seed, {"type": "published text", "value": a.seed}
    if a.seed_drand:
        r = int(a.seed_drand); now = datetime.datetime.now(datetime.timezone.utc).timestamp()
        if r < 1 or drand_round_time(r) > now: sys.exit(f"drand round {r} has not happened yet (the current round is about {drand_round_at(now)})")
        j = fetch_json(f"{DRAND['url']}/public/{r}")
        return j["randomness"], {"type": "drand", "chain_hash": DRAND["chain_hash"], "round": j["round"], "randomness": j["randomness"], "signature": j.get("signature"), "fetched_from": f"{DRAND['url']}/public/{r}", "round_time_utc": datetime.datetime.fromtimestamp(drand_round_time(r), datetime.timezone.utc).isoformat()}
    if a.seed_nist:
        j = fetch_json(f"{NIST}/time/{int(a.seed_nist) * 1000}")["pulse"]
        return j["outputValue"], {"type": "nist-beacon", "timeStamp": j["timeStamp"], "outputValue": j["outputValue"], "fetched_from": f"{NIST}/time/{int(a.seed_nist) * 1000}"}
    sys.exit("give --seed TEXT, --seed-drand ROUND or --seed-nist UNIXTIME (run `commit` first to announce one)")

def cmd_commit(a):
    rows, id_column, digest = load_entries(a.input, a.id_column); tiers = parse_tiers(a.tiers, a.winners)
    rules = rules_of(a, id_column, tiers); c = commitment(digest, rules)
    print(f"input sha256   {digest}\nrules          {json.dumps(rules, sort_keys=True)}\ncommitment     {c}")
    print("\nPublish the commitment now, before the seed exists. Keep the input file unchanged.")
    if a.draw_at:
        ts = datetime.datetime.fromisoformat(a.draw_at).timestamp(); r = drand_round_at(ts)
        print(f"drand round at {a.draw_at}: {r} (produced {datetime.datetime.fromtimestamp(drand_round_time(r), datetime.timezone.utc).isoformat()} UTC). Announce: 'seed = randomness of drand round {r}', then run draw with --seed-drand {r} after that time.")
    return 0

def cmd_draw(a):
    rows, id_column, digest = load_entries(a.input, a.id_column)
    exclude = {norm(l) for l in open(a.exclude, encoding="utf-8-sig") if l.strip()} if a.exclude else set()
    entrants, dupes, excluded, bad, clusters = prepare(rows, id_column, a.weight_column, exclude)
    tiers = parse_tiers(a.tiers, a.winners); need = sum(c for _, c in tiers) + a.backups
    if len(entrants) < need: sys.exit(f"only {len(entrants)} unique eligible entrants for {need} places")
    rules = rules_of(a, id_column, tiers); seed, source = seed_from(a)
    ranked = rank(entrants, seed); result, i = [], 0
    for name, count in tiers:
        for _ in range(count): e = ranked[i]; result.append({"tier": name, "id": e["shown"], "weight": e["weight"], "key": e["key"]}); i += 1
    for k in range(a.backups): e = ranked[i]; result.append({"tier": f"Backup {k + 1}", "id": e["shown"], "weight": e["weight"], "key": e["key"]}); i += 1
    audit = {"tool": "giveaway-random-draw/draw.py", "version": VERSION, "drawn_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
             "input_file": a.input, "input_sha256": digest, "rules": rules, "commitment": commitment(digest, rules),
             "rows_read": len(rows), "unique_eligible": len(entrants), "duplicates_merged": dupes, "excluded": excluded, "rows_with_invalid_weight": bad,
             "plus_address_clusters": len(clusters), "seed": seed, "seed_source": source, "results": result}
    def show(x): return mask(x) if a.mask else x
    for r in result: print(f"{r['tier']}: {show(r['id'])}" + (f" (weight {r['weight']:g})" if a.weight_column else ""))
    print(f"\nunique eligible {len(entrants)}, duplicates merged {dupes}, excluded {excluded}, invalid weights {bad}, seed source {source['type']}, commitment {audit['commitment'][:16]}...")
    if clusters: print(f"warning: {len(clusters)} groups of addresses share a local part with plus-tags (possible duplicate people). Review before announcing.")
    if a.audit: json.dump(audit, open(a.audit, "w"), indent=2); print(f"audit written to {a.audit}")
    if a.winners_csv:
        with open(a.winners_csv, "w", newline="") as f:
            w = csv.writer(f); w.writerow(["tier", "id", "weight"]); [w.writerow([r["tier"], r["id"], r["weight"]]) for r in result]
    return 0

def mask(x):
    if "@" in x: l, _, d = x.partition("@"); return l[:2] + "***@" + d
    return x[:3] + "***" if len(x) > 4 else "***"

def cmd_verify(a):
    audit = json.load(open(a.audit_file)); path = a.input or audit["input_file"]; ok = True
    rows, id_column, digest = load_entries(path, audit["rules"]["id_column"])
    if digest != audit["input_sha256"]: print("FAIL input file hash differs from the audit record"); ok = False
    if commitment(digest, audit["rules"]) != audit["commitment"]: print("FAIL commitment does not match input and rules"); ok = False
    exclude = set()
    if audit["rules"].get("exclude_file_sha256"):
        if not a.exclude: sys.exit("this draw used an exclusion file; pass it with --exclude to verify")
        raw = open(a.exclude, "rb").read()
        if sha(raw) != audit["rules"]["exclude_file_sha256"]: print("FAIL exclusion file hash differs"); ok = False
        exclude = {norm(l) for l in raw.decode("utf-8-sig").splitlines() if l.strip()}
    src = audit["seed_source"]
    if src["type"] == "drand":
        try:
            j = fetch_json(f"{DRAND['url']}/public/{src['round']}")
            if j["randomness"] != audit["seed"]: print("FAIL drand randomness for that round differs"); ok = False
            else: print(f"ok   drand round {src['round']} randomness matches the public beacon")
        except Exception as ex: print(f"warn could not refetch drand round ({ex}); checked the recorded value only")
    entrants, dupes, excluded, bad, _ = prepare(rows, id_column, audit["rules"]["weight_column"], exclude)
    if (len(entrants), dupes, excluded) != (audit["unique_eligible"], audit["duplicates_merged"], audit["excluded"]): print("FAIL entrant counts differ from the audit record"); ok = False
    got = [e["id"] for e in rank(entrants, audit["seed"])[:len(audit["results"])]]
    if got == [norm(r["id"]) for r in audit["results"]]: print(f"ok   recomputed the top {len(got)} entrants and they match the audit record")
    else: print("FAIL recomputed ranking differs from the audit record"); ok = False
    print("PASS" if ok else "FAIL"); return 0 if ok else 1

def self_test():
    import tempfile, os
    d = tempfile.mkdtemp(); p = os.path.join(d, "e.csv")
    open(p, "w").write("email,entries\nA@x.com,1\nb@x.com,3\na@x.com,2\nc@x.com,0\nd@x.com,1\nb+promo@x.com,1\n")
    rows, col, _ = load_entries(p, None); assert col == "email"
    ents, dupes, exc, bad, clusters = prepare(rows, col, "entries", {"d@x.com"})
    assert [e["id"] for e in ents] == ["a@x.com", "b@x.com", "b+promo@x.com"] and dupes == 1 and exc == 1 and bad == 1 and len(clusters) == 1, (ents, dupes, exc, bad, clusters)
    assert ents[0]["weight"] == 3.0
    r1 = [e["id"] for e in rank(list(ents), "seed-1")]; r2 = [e["id"] for e in rank(list(ents), "seed-1")]; assert r1 == r2
    heavy = [{"id": "h", "weight": 3.0}, {"id": "l", "weight": 1.0}]; wins = sum(1 for i in range(4000) if rank(list(heavy), str(i))[0]["id"] == "h")
    assert 0.70 < wins / 4000 < 0.80, wins       # weight 3 vs 1 should win about 75%
    assert drand_round_at(drand_round_time(1000)) == 1000 and drand_round_at(DRAND["genesis_time"]) == 1
    assert parse_tiers("Grand prize:1,Runner-up:5", 9) == [["Grand prize", 1], ["Runner-up", 5]]
    assert mask("someone@example.com") == "so***@example.com"
    pj = os.path.join(d, "c.json"); open(pj, "w").write(json.dumps({"comments": [{"owner": {"username": "ann"}, "text": "hi"}, {"owner": {"username": "Ann"}, "text": "again"}, {"owner": {"username": "bob"}, "text": "x"}]}))
    rows, col, _ = load_entries(pj, None); assert col == "owner.username" and len(rows) == 3, (col, rows)
    ents, dupes, *_ = prepare(rows, col, None, set()); assert [e["id"] for e in ents] == ["ann", "bob"] and dupes == 1
    print("self-test passed"); return 0

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    def common(p):
        p.add_argument("input"); p.add_argument("--winners", type=int, default=1); p.add_argument("--tiers"); p.add_argument("--backups", type=int, default=0)
        p.add_argument("--id-column"); p.add_argument("--weight-column"); p.add_argument("--exclude")
    c = sub.add_parser("commit", help="hash the input and rules; optionally name the drand round for a draw time"); common(c); c.add_argument("--draw-at", help="ISO time with offset, e.g. 2026-09-12T09:00:00+10:00")
    d = sub.add_parser("draw", help="run the draw once"); common(d)
    d.add_argument("--seed"); d.add_argument("--seed-drand", help="drand round number announced in advance"); d.add_argument("--seed-nist", help="unix time of a NIST beacon pulse announced in advance")
    d.add_argument("--audit"); d.add_argument("--winners-csv"); d.add_argument("--mask", action="store_true", help="print masked ids for announcements")
    v = sub.add_parser("verify", help="recompute a draw from its audit record"); v.add_argument("audit_file"); v.add_argument("--input"); v.add_argument("--exclude")
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    return {"commit": cmd_commit, "draw": cmd_draw, "verify": cmd_verify}.get(a.cmd, lambda a: ap.print_help() or 2)(a)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
