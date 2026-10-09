#!/usr/bin/env python3
"""Reproducible random draw with an audit record. Python 3.8+, no dependencies.

Input: CSV or TSV with a header, one id per line, or a JSON export of comments or Entrants (a list, or an object holding one,
with the person named by a field such as username, author, handle, email or owner.username). Pass --id-column to override.

  python3 draw.py commit  entries.csv --tiers "Grand Prize:1,Runner-up:5" [--backups 2] [--id-column email]
                          [--weight-column Entries] [--exclude staff.txt] [--draw-at "2026-09-12T09:00:00+10:00"]
  python3 draw.py draw    entries.csv --tiers ... [same options] (--seed TEXT | --seed-drand ROUND | --seed-nist UNIXTIME)
                          [--audit draw.json] [--winners-csv winners.csv] [--mask]
  python3 draw.py verify  draw.json [--input entries.csv]
  python3 draw.py --self-test

--rules rules.json keeps the flags in one file so commit and draw cannot drift apart. Keys, all optional:
tiers, backups, winners, id-column, weight-column, exclude. A flag given on the command line wins over the file.

  {"tiers": "Grand Prize:1,Runner-up:5", "backups": 2, "id-column": "email", "weight-column": "entries", "exclude": "staff.txt"}

How the draw works (documented so anyone can recheck it in any language):
  1. Entrants are read, ids trimmed and lower-cased, duplicates merged (weights add up when a weight column is given),
     exclusions removed, invalid or zero weights dropped.
  2. Supplied seed text permits reproduction. Fairness requires a preannounced future source beyond the
     organizer's control, such as a drand round or NIST beacon pulse fetched after it exists.
  3. Each Entrant gets key = u ** (1 / weight), where u = SHA-256(seed + "|" + id) read as a number in (0, 1).
     This is Efraimidis-Spirakis weighted sampling without replacement. With no weights it is a uniform draw.
  4. Entrants are sorted by log(u) / weight, highest first, avoiding key underflow.
     This preserves the mathematical key order. Tiers and backups are filled in that order.
  The audit record holds the SHA-256 of the input, the rules, the seed and its source, and every Winner's key,
  so `verify` (or a few lines in any language) reproduces the result exactly.

commit prints a commitment (hash of the input plus the rules) to publish before the seed exists. With --draw-at it
also prints the first drand round produced at or after that time, so the seed source can be announced in advance.
verify returns 0 on success, 1 on a mismatch, or 2 when ranking checks pass but the beacon source is unverified.
"""
import argparse, csv, hashlib, io, json, math, sys, datetime, urllib.request

VERSION = "2.4.3"
DRAND = {"url": "https://api.drand.sh", "genesis_time": 1595431050, "period": 30, "chain_hash": "8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce"}
NIST = "https://beacon.nist.gov/beacon/2.0/pulse"

def sha(b): return hashlib.sha256(b).hexdigest()
def norm(s): return str(s or "").strip().lower()

ACCOUNT_ID_KEYS = ("authorChannelId.value", "authorChannelId", "from.id", "from.id_str",
                   "author_id", "author.id", "author.id_str", "user_id", "user.id", "user.id_str",
                   "owner_id", "owner.id", "account_id", "account.id", "commenter_id", "commenter.id",
                   "entrant_id", "entrant.id", "participant_id", "participant.id")
PERSON_KEYS = ("email", "Email") + ACCOUNT_ID_KEYS + ("username", "user_name", "handle", "authorDisplayName",
               "author_name", "author", "commenter", "owner", "user", "entrant", "name", "Name")
# Generic object IDs remain recognized headers, but need an explicit person-ID choice.
ID_KEYS = PERSON_KEYS + ("id", "ID", "comment_id", "post_id")

def _flatten_json(obj):
    """Best-effort: find the list of comment or Entrant objects inside a JSON export and the field that names the person."""
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
        def walk(prefix, d):
            for k, v in d.items():
                if isinstance(v, dict): walk(f"{prefix}{k}.", v)
                elif isinstance(v, (str, int, float)): flat[f"{prefix}{k}"] = v
        walk("", it)
        rows.append(flat)
    return rows

def person_columns(rows):
    keys = list(dict.fromkeys(k for row in rows for k in row))
    return list(dict.fromkeys(k for cand in PERSON_KEYS for k in keys
                              if k == cand or k.endswith("." + cand)))

def pick_id_column(rows, id_column):
    keys = list(dict.fromkeys(k for row in rows for k in row))
    if id_column:
        if id_column not in keys: sys.exit(f"column '{id_column}' not found; columns are {keys}")
        return id_column
    candidates = person_columns(rows)
    if candidates: return candidates[0]
    sys.exit("cannot identify a person/account column safely; pass --id-column with the person identifier "
             f"(comment/post IDs must not stand in for people); columns are {keys}")

def load_entries(path, id_column):
    with open(path, "rb") as source:
        raw = source.read()
    text = raw.decode("utf-8-sig")
    stripped = text.lstrip()
    if stripped.startswith("[") or stripped.startswith("{"):
        rows = _flatten_json(json.loads(text))
        if not rows: sys.exit("no Entries found in the JSON export")
        return rows, pick_id_column(rows, id_column), sha(raw)
    lines = [l for l in text.splitlines() if l.strip()]
    if not lines: sys.exit("no Entries in input")
    # A one-column CSV has no delimiter. Its extension, header, or requested
    # column still identifies it as a table, so the header cannot become an entrant.
    suffix = str(path).lower().rsplit(".", 1)[-1]
    first_field = next(csv.reader([lines[0]]))[0]
    headered = (suffix in ("csv", "tsv") or "," in lines[0] or "\t" in lines[0]
                or (suffix != "txt" and first_field in ID_KEYS)
                or (id_column is not None and id_column != "entrant"))
    if headered and "," not in lines[0] and "\t" not in lines[0] and id_column is None and first_field not in ID_KEYS:
        sys.exit(f"one-column {suffix} file whose first line '{first_field}' is not a recognised header: "
                 f"pass --id-column '{first_field}' if it is a header, or save a plain list as .txt")
    if headered:
        dialect = csv.excel_tab if suffix == "tsv" or ("\t" in lines[0] and "," not in lines[0]) else csv.excel
        rows = list(csv.DictReader(io.StringIO(text.lstrip()), dialect=dialect))
        if not rows: sys.exit("no Entries below the input header")
        return rows, pick_id_column(rows, id_column), sha(raw)
    return [{"entrant": l.strip()} for l in lines], "entrant", sha(raw)

def prepare(rows, id_column, weight_column, exclude):
    missing = sum(not norm(row.get(id_column)) for row in rows)
    if missing:
        alternatives = [column for column in person_columns(rows) if column != id_column
                        and all(norm(row.get(column)) for row in rows)]
        guidance = (f"complete person identifier columns: {alternatives}; confirm one and pass --id-column"
                    if alternatives else "no complete recognized person identifier column is available")
        sys.exit(f"{missing} of {len(rows)} records lack the chosen identifier '{id_column}'; "
                 f"{guidance}. Reconcile identifiers before drawing; no records were prepared.")
    seen, entrants, dupes, excluded, bad = {}, [], 0, 0, 0
    for r in rows:
        key = norm(r.get(id_column))
        if key in exclude: excluded += 1; continue
        w = 1.0
        if weight_column:
            try: w = float(r.get(weight_column) or 0)
            except ValueError: w = 0.0
            if not math.isfinite(w) or w <= 0: bad += 1; continue
        if key in seen:
            dupes += 1
            if weight_column:
                total_weight = seen[key]["weight"] + w
                if not math.isfinite(total_weight):
                    raise ValueError("combined entry weights exceed the finite range; reconcile weights before drawing")
                seen[key]["weight"] = total_weight
            continue
        seen[key] = {"id": key, "shown": str(r.get(id_column)).strip(), "weight": w}; entrants.append(seen[key])
    plus = {}
    for e in entrants:
        if "@" in e["id"]:
            local, _, dom = e["id"].partition("@"); plus.setdefault(local.split("+")[0] + "@" + dom, []).append(e["id"])
    clusters = {k: v for k, v in plus.items() if len(v) > 1}
    return entrants, dupes, excluded, bad, clusters

# Maintenance: a hand-kept sample of throwaway-mail domains, never a full list. Add a domain when a real export shows it.
# A miss here costs a review line, so keep it short and do not chase completeness.
DISPOSABLE = {"mailinator.com", "guerrillamail.com", "10minutemail.com", "tempmail.com", "temp-mail.org", "yopmail.com", "trashmail.com",
              "getnada.com", "dispostable.com", "sharklasers.com", "maildrop.cc", "fakeinbox.com", "mohmal.com", "throwawaymail.com", "emailondeck.com"}

def scan(entrants):
    """Signals worth a look before committing: disposable domains, one domain holding a large share, and runs of handles
    that differ only by a trailing number. Each is a prompt to review, never a verdict."""
    import re as _re
    notes = []; doms = {}; stems = {}
    for e in entrants:
        i = e["id"]
        if "@" in i:
            dom = i.rpartition("@")[2]; doms[dom] = doms.get(dom, 0) + 1
            if dom in DISPOSABLE: notes.append(f"disposable email domain: {i}")
        m = _re.match(r"^(.*?[a-z_.])(\d{2,})(@.*)?$", i)
        if m: stems.setdefault(m.group(1), []).append(i)
    n = len(entrants)
    for dom, k in sorted(doms.items(), key=lambda kv: -kv[1]):
        if n >= 50 and k >= 10 and k / n >= 0.2 and dom not in ("gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com", "aol.com", "live.com", "protonmail.com", "proton.me", "googlemail.com", "hotmail.co.uk", "yahoo.co.uk", "me.com", "msn.com", "gmx.com", "gmx.de", "web.de", "mail.ru", "yandex.ru", "qq.com", "163.com"):
            notes.append(f"{k} of {n} entrants share the domain {dom}")
    runs = [v for v in stems.values() if len(v) >= 5]
    for v in sorted(runs, key=len, reverse=True)[:5]:
        notes.append(f"{len(v)} handles differ only by a trailing number, e.g. {v[0]}, {v[1]}, {v[2]}")
    return notes

def rank(entrants, seed):
    for e in entrants:
        h = hashlib.sha256((seed + "|" + e["id"]).encode()).digest()
        u = (int.from_bytes(h[:8], "big") + 0.5) / 2 ** 64          # uniform in (0, 1), never exactly 0 or 1
        e["u"] = u; e["key"] = u ** (1.0 / e["weight"])
    return sorted(entrants, key=lambda e: (-math.log(e["u"]) / e["weight"], e["id"]))

def parse_tiers(spec, winners):
    if not spec:
        if type(winners) is not int or winners < 0: sys.exit("winners must be a nonnegative integer")
        return [["Winner", winners]]
    out = []
    for part in spec.split(","):
        name, _, count = part.rpartition(":"); out.append([name.strip() or "Prize", int(count)])
    if any(count < 0 for _, count in out): sys.exit("tier counts must be nonnegative integers")
    return out

def rules_of(a, id_column, tiers):
    exclude_digest = None
    if a.exclude:
        with open(a.exclude, "rb") as source:
            exclude_digest = sha(source.read())
    return {"id_column": id_column, "weight_column": a.weight_column, "exclude_file_sha256": exclude_digest,
            "tiers": tiers, "backups": a.backups, "method": "sha256(seed|id) -> u in (0,1); key = u^(1/weight); rank by log(u)/weight descending; ties by id", "tool_version": VERSION}

def apply_rules(a):
    """Fill any option the command line left unset from --rules FILE. Command-line flags win."""
    if getattr(a, "rules", None):
        with open(a.rules) as resource:
            for k, v in json.load(resource).items():
                attr = k.replace("-", "_")
                if hasattr(a, attr) and getattr(a, attr) is None: setattr(a, attr, v)
    if getattr(a, "backups", None) is None: a.backups = 0
    if getattr(a, "winners", None) is None: a.winners = 1
    for attr in ("winners", "backups"):
        if type(getattr(a, attr)) is not int or getattr(a, attr) < 0:
            sys.exit(f"{attr} must be a nonnegative integer")
    return a

def commitment(digest, rules): return sha((digest + "\n" + json.dumps(rules, sort_keys=True, separators=(",", ":"))).encode())

def drand_round_at(ts): return int((ts - DRAND["genesis_time"]) // DRAND["period"]) + 1
def drand_round_at_or_after(ts): return math.ceil((ts - DRAND["genesis_time"]) / DRAND["period"]) + 1
def drand_round_time(r): return DRAND["genesis_time"] + (r - 1) * DRAND["period"]

def fetch_json(url):
    with urllib.request.urlopen(url, timeout=20) as r: return json.load(r)

def seed_from(a):
    if sum(getattr(a, key, None) is not None for key in ("seed", "seed_drand", "seed_nist")) != 1:
        sys.exit("give exactly one seed source: --seed TEXT, --seed-drand ROUND or --seed-nist UNIXTIME "
                 "(run `commit` first to announce one)")
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

def load_exclusions(path):
    if not path:
        return set()
    with open(path, encoding="utf-8-sig") as source:
        return {norm(line) for line in source if line.strip()}

def warn_plus_clusters(clusters):
    if clusters:
        print(f"warning: {len(clusters)} groups of addresses share a local part with plus-tags (possible duplicate people). "
              "Review before publishing the commitment or announcing Winners. "
              "Addresses remain eligible unless an exclusion is confirmed under the terms.")

def cmd_commit(a):
    rows, id_column, digest = load_entries(a.input, a.id_column); tiers = parse_tiers(a.tiers, a.winners)
    ents, dupes, excluded, bad, clusters = prepare(rows, id_column, a.weight_column, load_exclusions(a.exclude))
    rules = rules_of(a, id_column, tiers); c = commitment(digest, rules)
    print(f"input sha256   {digest}\nrules          {json.dumps(rules, sort_keys=True)}\ncommitment     {c}")
    print(f"rows_read {len(rows)}, unique_eligible {len(ents)}, duplicates_merged {dupes}, "
          f"excluded {excluded}, rows_with_invalid_weight {bad}")
    warn_plus_clusters(clusters)
    notes = scan(ents)
    shown = notes if not getattr(a, "flagged_out", None) else notes[:20]
    for note in shown: print(f"review: {note}")
    if getattr(a, "flagged_out", None):
        # 20,000 review lines in a terminal is not a review. Write the ids out, let a person read them, feed the
        # kept ones back through --exclude. Nothing is dropped here: excluding a real Entrant costs them the Prize.
        ids = [n.split(": ", 1)[1] for n in notes if ": " in n and not n.startswith("one domain")]
        with open(a.flagged_out, "w") as fh:
            fh.write("\n".join(dict.fromkeys(ids)) + ("\n" if ids else ""))
        more = f" ({len(notes) - len(shown)} more not printed)" if len(notes) > len(shown) else ""
        print(f"\n{len(set(ids))} flagged ids written to {a.flagged_out}{more}. Read that file, delete anyone who "
              f"should stay in, then rerun commit with --exclude {a.flagged_out} and the final rules. "
              "Publish the new commitment before the seed exists, then draw with the same input, exclusions and rules. "
              "Flagging is a prompt to look, never a verdict.")
    print("\nReconcile eligibility and earned weights with the published rules before publishing this commitment. "
          "Publish before the seed exists, then keep the input file unchanged.")
    if a.draw_at:
        ts = datetime.datetime.fromisoformat(a.draw_at).timestamp(); r = drand_round_at_or_after(ts)
        print(f"drand round at or after {a.draw_at}: {r} (produced {datetime.datetime.fromtimestamp(drand_round_time(r), datetime.timezone.utc).isoformat()} UTC). Announce: 'seed = randomness of drand round {r}', then run draw with --seed-drand {r} after that time.")
    return 0

def cmd_draw(a):
    rows, id_column, digest = load_entries(a.input, a.id_column)
    exclude = load_exclusions(a.exclude)
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
    print(f"\nrows_read {len(rows)}, unique_eligible {len(entrants)}, duplicates_merged {dupes}, excluded {excluded}, rows_with_invalid_weight {bad}, seed source {source['type']}, commitment {audit['commitment'][:16]}...")
    warn_plus_clusters(clusters)
    for note in scan(entrants): print(f"review: {note}")
    if a.audit:
        with open(a.audit, "w") as resource:
            json.dump(audit, resource, indent=2)
        print(f"audit written to {a.audit}")
    if a.winners_csv:
        with open(a.winners_csv, "w", newline="") as f:
            w = csv.writer(f); w.writerow(["tier", "id", "weight"]); [w.writerow([r["tier"], r["id"], r["weight"]]) for r in result]
    return 0

def mask(x):
    if "@" in x: l, _, d = x.partition("@"); return l[:2] + "***@" + d
    return x[:3] + "***" if len(x) > 4 else "***"

def cmd_verify(a):
    with open(a.audit_file) as resource:
        audit = json.load(resource)
    path = a.input or audit["input_file"]; ok = True; source_unverified = False
    rows, id_column, digest = load_entries(path, audit["rules"]["id_column"])
    if digest != audit["input_sha256"]: print("FAIL input file hash differs from the audit record"); ok = False
    if commitment(digest, audit["rules"]) != audit["commitment"]: print("FAIL commitment does not match input and rules"); ok = False
    exclude = set()
    if audit["rules"].get("exclude_file_sha256"):
        if not a.exclude: sys.exit("this draw used an exclusion file; pass it with --exclude to verify")
        with open(a.exclude, "rb") as resource:
            raw = resource.read()
        if sha(raw) != audit["rules"]["exclude_file_sha256"]: print("FAIL exclusion file hash differs"); ok = False
        exclude = {norm(l) for l in raw.decode("utf-8-sig").splitlines() if l.strip()}
    src = audit.get("seed_source")
    if not isinstance(src, dict) or src.get("type") not in ("drand", "nist-beacon", "published text"):
        print("FAIL unsupported or missing seed source type"); print("FAIL"); return 1
    if src["type"] == "published text":
        if not isinstance(src.get("value"), str) or src["value"] != audit["seed"]:
            print("FAIL published text value does not match the seed"); ok = False
        else:
            print("ok   recorded published text matches the seed; publication must be checked separately")
    elif src["type"] == "drand":
        try:
            j = fetch_json(f"{DRAND['url']}/public/{src['round']}")
            if j["randomness"] != audit["seed"]: print("FAIL drand randomness for that round differs"); ok = False
            else: print(f"ok   drand round {src['round']} randomness matches the public beacon")
        except Exception as ex:
            print(f"warn could not refetch drand round ({ex}); seed source unverified")
            source_unverified = True
    elif src["type"] == "nist-beacon":
        # Fetch only the fixed NIST endpoint, never an arbitrary URL supplied in an audit.
        url = src.get("fetched_from", "")
        prefix = NIST + "/time/"
        valid_url = (isinstance(url, str) and url.startswith(prefix)
                     and url[len(prefix):].isascii() and url[len(prefix):].isdigit())
        stamp = src.get("timeStamp")
        try:
            timestamp = datetime.datetime.fromisoformat(stamp.replace("Z", "+00:00"))
            valid_stamp = timestamp.utcoffset() is not None
        except (AttributeError, TypeError, ValueError):
            valid_stamp = False
        if (not valid_url or not valid_stamp or not isinstance(src.get("outputValue"), str)
                or not src["outputValue"] or src["outputValue"] != audit["seed"]):
            print("FAIL NIST pulse metadata or recorded output does not match the seed"); ok = False
        else:
            try:
                pulse = fetch_json(url)["pulse"]
                if pulse["timeStamp"] != stamp or pulse["outputValue"] != audit["seed"]:
                    print("FAIL NIST pulse timestamp or randomness differs"); ok = False
                else:
                    print("ok   NIST pulse timestamp and randomness match the public beacon")
            except Exception as ex:
                print(f"warn could not refetch NIST pulse ({ex}); seed source unverified")
                source_unverified = True
    entrants, dupes, excluded, bad, _ = prepare(rows, id_column, audit["rules"]["weight_column"], exclude)
    if (len(entrants), dupes, excluded) != (audit["unique_eligible"], audit["duplicates_merged"], audit["excluded"]): print("FAIL Entrant counts differ from the audit record"); ok = False
    tiers = audit["rules"].get("tiers"); backups = audit["rules"].get("backups")
    if (not isinstance(tiers, list) or not tiers or
            any(not isinstance(t, list) or len(t) != 2 or not isinstance(t[0], str) or
                type(t[1]) is not int or t[1] < 0 for t in tiers) or
            type(backups) is not int or backups < 0):
        print("FAIL committed tiers or backup count are invalid"); return 1
    need = sum(count for _, count in tiers) + backups
    results = audit.get("results")
    if not isinstance(results, list) or len(results) != need:
        print(f"FAIL result count differs from the {need} committed places"); ok = False
    if len(entrants) < need:
        print(f"FAIL only {len(entrants)} eligible entrants for {need} committed places"); ok = False
    elif isinstance(results, list) and len(results) == need:
        labels = [name for name, count in tiers for _ in range(count)]
        labels.extend(f"Backup {k + 1}" for k in range(backups))
        expected = [(e["shown"], label) for e, label in zip(rank(entrants, audit["seed"]), labels)]
        recorded = [(r.get("id"), r.get("tier")) if isinstance(r, dict) else None for r in results]
        if expected == recorded:
            print(f"ok   recomputed all {need} committed places, including order and tier assignments")
        else:
            version = audit.get("version")
            try:
                parts = tuple(int(part) for part in version.split("."))
                older = len(parts) == 3 and (0, 0, 0) < parts < (2, 4, 3)
            except (AttributeError, TypeError, ValueError):
                older = False
            legacy = sorted(entrants, key=lambda e: (-e["key"], e["id"]))
            legacy_expected = [(e["shown"], label) for e, label in zip(legacy, labels)]
            if older and legacy_expected == recorded:
                print(f"ok   verified all {need} committed places under the legacy ranking (audit version {version})")
            else:
                print("FAIL recomputed result order, IDs or tier assignments differ from the audit record"); ok = False
    if not ok: print("FAIL"); return 1
    if source_unverified:
        print("PARTIAL: ranking recomputation verified; seed source unverified"); return 2
    print("PASS"); return 0

def verifier_self_test():
    import contextlib, copy, os, tempfile
    with tempfile.TemporaryDirectory() as directory:
        entries = os.path.join(directory, "entries.csv")
        audit_path = os.path.join(directory, "audit.json")
        with open(entries, "w") as handle:
            handle.write("id,entries\nalpha,1\nbeta,2\ngamma,3\ndelta,4\nepsilon,5\nzeta,6\n")
        with contextlib.redirect_stdout(io.StringIO()):
            assert main(["draw", entries, "--id-column", "id", "--weight-column", "entries",
                         "--tiers", "Grand:1,Runner-up:2", "--backups", "2", "--seed", "regression-seed",
                         "--audit", audit_path]) == 0
        with open(audit_path) as handle: original = json.load(handle)
        def check(audit, expected_code):
            with open(audit_path, "w") as handle: json.dump(audit, handle)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = main(["verify", audit_path, "--input", entries])
            assert code == expected_code, output.getvalue()
            ending = {0: "PASS", 1: "FAIL", 2: "PARTIAL: ranking recomputation verified; seed source unverified"}
            assert output.getvalue().splitlines()[-1] == ending[expected_code], output.getvalue()
        assert [(r["tier"], r["id"], r["key"]) for r in original["results"]] == [
            ("Grand", "delta", 0.974794625452104),
            ("Runner-up", "zeta", 0.9522387005466458),
            ("Runner-up", "epsilon", 0.9454234991052942),
            ("Backup 1", "gamma", 0.7696785881239763),
            ("Backup 2", "beta", 0.4605470121165112)], original["results"]
        check(original, 0)
        historical = copy.deepcopy(original)
        historical["version"] = historical["rules"]["tool_version"] = "2.4.2"
        historical["rules"]["method"] = "sha256(seed|id) -> u in (0,1); key = u^(1/weight); highest keys win; ties by id"
        historical["commitment"] = commitment(historical["input_sha256"], historical["rules"])
        check(historical, 0)
        for source in ({"type": "unrecognized-beacon"}, {}, None, [],
                       {"type": "published text"}, {"type": "published text", "value": 123},
                       {"type": "published text", "value": "different-seed"}):
            changed = copy.deepcopy(original); changed["seed_source"] = source
            check(changed, 1)
        # Fabricated metadata must never gain PASS merely by recomputing matching Winners.
        from unittest.mock import patch
        nist = copy.deepcopy(original)
        nist["seed_source"] = {"type": "nist-beacon", "timeStamp": "2026-09-12T00:00:00.000Z",
                               "outputValue": nist["seed"], "fetched_from": NIST + "/time/1789171200000"}
        pulse = {"pulse": {"timeStamp": nist["seed_source"]["timeStamp"], "outputValue": nist["seed"]}}
        fetched = []
        def fetch_pulse(url):
            fetched.append(url)
            return copy.deepcopy(pulse)
        with patch.dict(globals(), fetch_json=fetch_pulse):
            check(nist, 0)
            assert fetched == [nist["seed_source"]["fetched_from"]], fetched
            for field, value in (("outputValue", "fabricated"), ("timeStamp", "2026-09-12T00:01:00.000Z"),
                                 ("timeStamp", "invalid"), ("fetched_from", "https://example.com/pulse")):
                changed = copy.deepcopy(nist); changed["seed_source"][field] = value
                check(changed, 1)
            mismatch = copy.deepcopy(pulse); mismatch["pulse"]["outputValue"] = "actual-beacon-value"
            with patch.dict(globals(), fetch_json=lambda url: mismatch): check(nist, 1)
        drand = copy.deepcopy(original); drand["seed_source"] = {"type": "drand", "round": 1000}
        with patch.dict(globals(), fetch_json=lambda url: {"randomness": original["seed"]}):
            check(drand, 0)
        with patch.dict(globals(), fetch_json=lambda url: {"randomness": "different-seed"}):
            check(drand, 1)
        def unavailable(url): raise OSError("offline test")
        with patch.dict(globals(), fetch_json=unavailable):
            check(nist, 2)
            drand = copy.deepcopy(original); drand["seed_source"] = {"type": "drand", "round": 1000}
            check(drand, 2)
            changed = copy.deepcopy(nist); changed["results"][0]["id"] = "absent-entrant"
            check(changed, 1)
        for length in (0, 1, 3, 4):
            changed = copy.deepcopy(original); changed["results"] = changed["results"][:length]
            check(changed, 1)
        changed = copy.deepcopy(original); changed["results"].append(changed["results"][-1].copy())
        check(changed, 1)
        for index, tier in ((0, "Runner-up"), (1, "Grand"), (3, "Backup 2")):
            changed = copy.deepcopy(original); changed["results"][index]["tier"] = tier
            check(changed, 1)
        changed = copy.deepcopy(original)
        changed["results"][1], changed["results"][2] = changed["results"][2], changed["results"][1]
        check(changed, 1)
        changed = copy.deepcopy(original); changed["results"][0]["id"] = "absent-entrant"
        check(changed, 1)
        changed = copy.deepcopy(original); del changed["results"][0]["tier"]
        check(changed, 1)

def self_test_input_formats():
    import os, tempfile
    with tempfile.TemporaryDirectory() as directory:
        def read_file(name, content, column=None):
            path = os.path.join(directory, name)
            with open(path, "w") as output: output.write(content)
            return load_entries(path, column)
        for name in ("entrants.csv", "entrants.tsv", "entrants"):
            for column in (None, "email"):
                rows, chosen, _ = read_file(name, "email\nalpha\nbeta\n", column)
                pool, _, _, _, _ = prepare(rows, chosen, None, set())
                assert [entrant["id"] for entrant in pool] == ["alpha", "beta"], (name, column, pool)
        rows, chosen, _ = read_file("custom.csv", '"account"\n"alpha"\n"beta"\n', "account")
        assert chosen == "account" and len(rows) == 2, rows
        rows, chosen, _ = read_file("custom.txt", "account\nalpha\nbeta\n", "account")
        assert chosen == "account" and len(rows) == 2, rows
        for column in (None, "entrant"):
            rows, chosen, _ = read_file("plain.txt", "email\nalpha\nbeta\n", column)
            assert chosen == "entrant" and len(rows) == 3, rows
        for name, content, column in (("wrong.csv", "email\nalpha\nbeta\n", "account"),
                                      ("bare.csv", "alpha@example.com\nbeta@example.com\n", None),
                                      ("wrong.txt", "alpha\nbeta\n", "email"),
                                      ("empty.csv", "email\n", None)):
            try: read_file(name, content, column)
            except SystemExit: pass
            else: raise AssertionError("missing header or data must fail, never eat the first entrant: " + name)

def self_test_account_ids():
    import contextlib, os, tempfile
    examples = [
        ([{"id": "c1", "from": {"id": "person-a", "name": "Alex"}},
          {"id": "c2", "from": {"id": "person-b", "name": "Alex"}},
          {"id": "c3", "from": {"id": "person-a", "name": "Renamed"}}], "from.id"),
        ([{"id": "post1", "author_id": "person-a"}, {"id": "post2", "author_id": "person-a"},
          {"id": "post3", "author_id": "person-b"}], "author_id"),
        ([{"id": "c1", "user": {"id": "person-a", "username": "same"}},
          {"id": "c2", "user": {"id": "person-a", "username": "new"}},
          {"id": "c3", "user": {"id": "person-b", "username": "same"}}], "user.id"),
    ]
    for objects, expected in examples:
        rows = _flatten_json(objects)
        column = pick_id_column(rows, None)
        pool, duplicates, *_ = prepare(rows, column, None, set())
        assert column == expected and {e["id"] for e in pool} == {"person-a", "person-b"}
        assert duplicates == 1
    for key in ACCOUNT_ID_KEYS:
        assert pick_id_column([{"id": "comment", "name": "Display", "nested." + key: "person"}], None) == "nested." + key
    with tempfile.TemporaryDirectory() as directory:
        for filename, content in (("comments.json", json.dumps({"comments": [{"id": "c1", "text": "hello"}]})),
                                  ("posts.csv", "id,text\npost1,hello\n"),
                                  ("comments.csv", "comment_id,text\nc1,hello\n")):
            path = os.path.join(directory, filename)
            with open(path, "w") as output: output.write(content)
            try: load_entries(path, None)
            except SystemExit as error: assert "--id-column" in str(error), str(error)
            else: raise AssertionError("ambiguous object IDs must require explicit selection")
            chosen = "comment_id" if filename == "comments.csv" else "id"
            assert load_entries(path, chosen)[1] == chosen
        # Audits record the original column: verification must not auto-select the new default.
        path = os.path.join(directory, "legacy.json")
        audit = os.path.join(directory, "audit.json")
        with open(path, "w") as output: json.dump(examples[0][0], output)
        for old_column in ("from.name", "id"):
            with contextlib.redirect_stdout(io.StringIO()):
                assert main(["draw", path, "--id-column", old_column, "--seed", "legacy-seed", "--audit", audit]) == 0
                assert main(["verify", audit, "--input", path]) == 0


def self_test_invalid_counts():
    for options in ({"winners": -1}, {"backups": -1}, {"tiers": "Grand:2,Runner-up:-1"}):
        a = argparse.Namespace(rules=None, winners=1, backups=0, tiers=None)
        for key, value in options.items(): setattr(a, key, value)
        try:
            apply_rules(a)
            parse_tiers(a.tiers, a.winners)
        except SystemExit as error:
            assert "nonnegative integer" in str(error), str(error)
        else:
            raise AssertionError("negative place counts must fail: " + str(options))

def self_test_numeric_ids():
    import os, tempfile
    with tempfile.TemporaryDirectory() as directory:
        path = os.path.join(directory, "numeric.json")
        with open(path, "w") as output:
            json.dump([{"id": 42}, {"id": "42"}], output)
        rows, column, _ = load_entries(path, "id")
        pool, duplicates, _, _, _ = prepare(rows, column, None, set())
        assert [(e["id"], e["shown"]) for e in pool] == [("42", "42")]
        assert duplicates == 1
        # Values previously silently omitted now require reconciliation before drawing.
        try: prepare([{"id": value} for value in (0, False, None, "alpha")], "id", None, set())
        except SystemExit as error: assert "3 of 4 records" in str(error), str(error)
        else: raise AssertionError("empty normalized identifiers must stop the draw")

def self_test_missing_ids():
    import contextlib, pathlib, tempfile
    from unittest.mock import patch
    with tempfile.TemporaryDirectory() as directory:
        directory = pathlib.Path(directory)
        fixtures = [
            ("sparse.csv", "email,user_id,id\nalpha,person-a,row-a\n,person-b,row-b\n,person-c,row-c\n"),
            ("sparse.json", json.dumps([{"user_id": "person-a", "id": "row-a"},
                                        {"email": "alpha", "user_id": "person-b", "id": "row-b"},
                                        {"email": None, "user_id": "person-c", "id": "row-c"}])),
        ]
        for filename, content in fixtures:
            path = directory / filename
            path.write_text(content)
            rows, column, _ = load_entries(path, None)
            assert column == "email", column
            assert load_entries(path, "email")[1] == "email"
            for command in ("commit", "draw"):
                audit_path = directory / "audit.json"
                args = [command, str(path)]
                if command == "draw": args += ["--seed", "regression-seed", "--audit", str(audit_path)]
                with contextlib.redirect_stdout(io.StringIO()) as output, patch.dict(
                        globals(), seed_from=lambda a: (_ for _ in ()).throw(AssertionError("seed requested before reconciliation"))):
                    try: main(args)
                    except SystemExit as error:
                        message = str(error)
                        assert "2 of 3 records" in message and "'email'" in message, message
                        assert "complete person identifier columns: ['user_id']" in message, message
                        assert "--id-column" in message, message
                    else: raise AssertionError("missing identifiers must block commit and draw")
                assert not output.getvalue() and not audit_path.exists()
            pool, duplicates, excluded, bad, _ = prepare(rows, "user_id", None, set())
            assert [e["id"] for e in pool] == ["person-a", "person-b", "person-c"]
            assert (duplicates, excluded, bad) == (0, 0, 0)
        for rows in ([{"email": "alpha", "id": "row-a"}, {"id": "row-b"}],
                     [{}, {"email": "alpha"}],
                     [{"email": "alpha", "user_id": "person-a"}, {"email": " ", "user_id": ""}]):
            try: prepare(rows, pick_id_column(rows, None), None, set())
            except SystemExit as error:
                assert "1 of 2 records" in str(error), str(error)
                assert "no complete recognized person identifier column" in str(error), str(error)
            else: raise AssertionError("incomplete identifiers cannot fall back per row or use generic row IDs")

def self_test_plus_preview():
    import contextlib, pathlib, tempfile
    with tempfile.TemporaryDirectory() as directory:
        entries = pathlib.Path(directory) / "aliases.csv"
        audit_path = pathlib.Path(directory) / "audit.json"
        aliases = ["a@example.com", "a+one@example.com", "a+two@example.com"]
        entries.write_text("email,entries\n" + "".join(f"{alias},{weight}\n" for alias, weight in zip(aliases, (1, 2, 3))))
        rows, column, _ = load_entries(entries, None)
        pool, duplicates, excluded, bad, clusters = prepare(rows, column, "entries", set())
        assert [e["id"] for e in pool] == aliases and [e["weight"] for e in pool] == [1, 2, 3]
        assert (duplicates, excluded, bad, len(clusters)) == (0, 0, 0, 1)
        expected = [e["shown"] for e in rank(pool, "plus-preview-regression")]
        common = [str(entries), "--weight-column", "entries", "--winners", "3"]
        warnings = []
        for command in ("commit", "draw"):
            extra = ["--seed", "plus-preview-regression", "--audit", str(audit_path)] if command == "draw" else []
            with contextlib.redirect_stdout(io.StringIO()) as output:
                assert main([command] + common + extra) == 0
            text = output.getvalue()
            warnings.append(next(line for line in text.splitlines() if line.startswith("warning:")))
            assert "unique_eligible 3, duplicates_merged 0, excluded 0, rows_with_invalid_weight 0" in text
            if command == "commit": assert "Winner:" not in text and not audit_path.exists()
        assert warnings[0] == warnings[1] and "1 groups" in warnings[0] and "remain eligible" in warnings[0]
        audit = json.loads(audit_path.read_text())
        assert [e["id"] for e in audit["results"]] == expected
        assert audit["unique_eligible"] == 3 and audit["plus_address_clusters"] == 1
        assert prepare(rows, column, "entries", set())[0] == [
            {"id": alias, "shown": alias, "weight": weight} for alias, weight in zip(aliases, (1, 2, 3))]

def self_test_recommit():
    import contextlib, pathlib, tempfile
    with tempfile.TemporaryDirectory() as directory:
        entries = pathlib.Path(directory) / "entries.csv"
        exclusions = pathlib.Path(directory) / "approved.txt"
        audit_path = pathlib.Path(directory) / "audit.json"
        entries.write_text("email,entries\nalpha,2\nbeta,3\ngamma,1\n")
        common = [str(entries), "--weight-column", "entries", "--tiers", "Grand:1", "--backups", "1"]
        with contextlib.redirect_stdout(io.StringIO()) as output:
            assert main(["commit"] + common + ["--flagged-out", str(exclusions)]) == 0
        preview = output.getvalue()
        assert f"rerun commit with --exclude {exclusions} and the final rules" in preview, preview
        assert "Publish the new commitment before the seed exists, then draw with the same input, exclusions and rules" in preview, preview
        for args in (["commit", "--help"],):
            with contextlib.redirect_stdout(io.StringIO()) as output:
                try: main(args)
                except SystemExit as error: assert error.code == 0
            help_text = " ".join(output.getvalue().split())
            assert "rerun commit with the approved file as --exclude and final rules" in help_text, help_text
            assert "Publish the new commitment before the seed exists" in help_text, help_text
        exclusions.write_text("gamma\n")
        final_rules = common + ["--exclude", str(exclusions)]
        with contextlib.redirect_stdout(io.StringIO()) as output:
            assert main(["commit"] + final_rules) == 0
        final_commitment = next(line.split()[-1] for line in output.getvalue().splitlines() if line.startswith("commitment"))
        preview_commitment = next(line.split()[-1] for line in preview.splitlines() if line.startswith("commitment"))
        assert final_commitment != preview_commitment
        with contextlib.redirect_stdout(io.StringIO()):
            assert main(["draw"] + final_rules + ["--seed", "recommit-regression", "--audit", str(audit_path)]) == 0
            assert main(["verify", str(audit_path), "--exclude", str(exclusions)]) == 0
        audit = json.loads(audit_path.read_text())
        assert audit["commitment"] == final_commitment
        assert audit["excluded"] == 1 and all(row["id"] != "gamma" for row in audit["results"])

def self_test_rank_underflow():
    import contextlib, copy, pathlib, tempfile
    seed = "regression-seed"
    ids = ("alpha", "beta", "gamma", "delta")
    def ranked(weights):
        return rank([{"id": key, "weight": weight} for key, weight in zip(ids, weights)], seed)
    ordinary = ranked([1] * 4)
    tiny = ranked([0.0001] * 4)
    assert [e["id"] for e in tiny] == [e["id"] for e in ordinary] == ["delta", "gamma", "alpha", "beta"]
    assert all(e["key"] == 0.0 for e in tiny)
    unequal = ranked([0.00001, 0.00002, 0.00003, 0.00004])
    assert [e["id"] for e in unequal] == [e["id"] for e in ranked([1, 2, 3, 4])]
    assert [e["id"] for e in unequal] == ["delta", "gamma", "beta", "alpha"]
    assert all(e["key"] == 0.0 for e in unequal)
    with tempfile.TemporaryDirectory() as directory:
        entries = pathlib.Path(directory) / "entries.csv"
        audit_path = pathlib.Path(directory) / "audit.json"
        entries.write_text("id,entries\n" + "".join(f"{key},0.0001\n" for key in ids))
        with contextlib.redirect_stdout(io.StringIO()):
            assert main(["draw", str(entries), "--id-column", "id", "--weight-column", "entries",
                         "--winners", "4", "--seed", seed, "--audit", str(audit_path)]) == 0
        audit = json.loads(audit_path.read_text())
        audit["results"].sort(key=lambda row: row["id"])
        for version, expected_code in (("2.4.2", 0), (VERSION, 1), ("9.0.0", 1), (None, 1)):
            historical = copy.deepcopy(audit)
            historical["version"] = historical["rules"]["tool_version"] = version
            historical["rules"]["method"] = "sha256(seed|id) -> u in (0,1); key = u^(1/weight); highest keys win; ties by id"
            historical["commitment"] = commitment(historical["input_sha256"], historical["rules"])
            audit_path.write_text(json.dumps(historical))
            with contextlib.redirect_stdout(io.StringIO()) as output:
                assert main(["verify", str(audit_path)]) == expected_code
            if expected_code == 0:
                assert "legacy ranking (audit version 2.4.2)" in output.getvalue(), output.getvalue()


def self_test_seed_sources():
    import contextlib, itertools, pathlib, tempfile
    from unittest.mock import patch
    sources = (("seed", "regression-seed"), ("seed_drand", "1"), ("seed_nist", "1"))
    with tempfile.TemporaryDirectory() as directory:
        entries = pathlib.Path(directory) / "entries.csv"
        audit_path = pathlib.Path(directory) / "audit.json"
        entries.write_text("id\nalpha\nbeta\ngamma\ndelta\n")
        for count in (0, 2, 3):
            for chosen in itertools.combinations(sources, count):
                namespace = argparse.Namespace(seed=None, seed_drand=None, seed_nist=None)
                flags = []
                for key, value in chosen:
                    setattr(namespace, key, value)
                    flags += ["--" + key.replace("_", "-"), value]
                with patch.dict(globals(), fetch_json=lambda url: (_ for _ in ()).throw(
                        AssertionError("invalid seed sources must fail before fetching"))):
                    try: seed_from(namespace)
                    except SystemExit as error: assert "exactly one seed source" in str(error), str(error)
                    else: raise AssertionError("invalid seed sources accepted by seed_from")
                    with contextlib.redirect_stderr(io.StringIO()) as errors:
                        try: main(["draw", str(entries), "--id-column", "id", "--audit", str(audit_path)] + flags)
                        except SystemExit as error: assert error.code == 2, error.code
                        else: raise AssertionError("invalid seed sources accepted by CLI")
                    assert ("not allowed with argument" if count else "required") in errors.getvalue()
                assert not audit_path.exists()
        responses = [{"round": 1, "randomness": "regression-seed", "signature": "fixture"},
                     {"pulse": {"outputValue": "regression-seed", "timeStamp": "fixture"}}]
        for (key, value), source_type in zip(sources, ("published text", "drand", "nist-beacon")):
            with patch.dict(globals(), fetch_json=lambda url: responses[0 if "/public/" in url else 1]), \
                    contextlib.redirect_stdout(io.StringIO()):
                assert main(["draw", str(entries), "--id-column", "id", "--winners", "4",
                             "--audit", str(audit_path), "--" + key.replace("_", "-"), value]) == 0
            audit = json.loads(audit_path.read_text())
            assert audit["seed"] == "regression-seed"
            assert audit["seed_source"]["type"] == source_type
            assert [row["id"] for row in audit["results"]] == ["delta", "gamma", "alpha", "beta"]
        assert seed_from(argparse.Namespace(seed="", seed_drand=None, seed_nist=None)) == (
            "", {"type": "published text", "value": ""})


def self_test():
    self_test_seed_sources()
    self_test_plus_preview()
    self_test_missing_ids()
    self_test_rank_underflow()
    self_test_recommit()
    self_test_numeric_ids()
    self_test_account_ids()
    self_test_invalid_counts()
    self_test_input_formats()
    import contextlib, io
    for args in (["--help"], ["draw", "--help"]):
        help_output = io.StringIO()
        with contextlib.redirect_stdout(help_output):
            try: main(args)
            except SystemExit as error: assert error.code == 0
        help_text = " ".join(help_output.getvalue().split())
        assert "reproduction" in help_text and "preannounced future source beyond" in help_text, help_text
        assert "text you published in advance" not in help_text, help_text
        if args[0] == "draw": assert "required for ambiguous id fields" in help_text, help_text
    import tempfile, os
    d = tempfile.mkdtemp(); p = os.path.join(d, "e.csv")
    with open(p, "w") as resource:
        resource.write("email,entries\nA@x.com,1\nb@x.com,3\na@x.com,2\nc@x.com,0\nd@x.com,1\nb+promo@x.com,1\n")
    rows, col, _ = load_entries(p, None); assert col == "email"
    ents, dupes, exc, bad, clusters = prepare(rows, col, "entries", {"d@x.com"})
    assert [e["id"] for e in ents] == ["a@x.com", "b@x.com", "b+promo@x.com"] and dupes == 1 and exc == 1 and bad == 1 and len(clusters) == 1, (ents, dupes, exc, bad, clusters)
    assert ents[0]["weight"] == 3.0
    finite_rows = [{"id": key, "entries": weight} for key, weight in [("alpha", "NaN"), ("beta", "Infinity"), ("gamma", "-Infinity"), ("delta", "2")]]
    finite_ents, _, _, invalid, _ = prepare(finite_rows, "id", "entries", set())
    assert [e["id"] for e in finite_ents] == ["delta"] and invalid == 3
    try:
        prepare([{"id": "alpha", "entries": "1e308"}] * 2, "id", "entries", set())
    except ValueError as error:
        assert "combined entry weights" in str(error)
    else:
        raise AssertionError("overflowing combined weights must stop the draw")
    r1 = [e["id"] for e in rank(list(ents), "seed-1")]; r2 = [e["id"] for e in rank(list(ents), "seed-1")]; assert r1 == r2
    heavy = [{"id": "h", "weight": 3.0}, {"id": "l", "weight": 1.0}]; wins = sum(1 for i in range(4000) if rank(list(heavy), str(i))[0]["id"] == "h")
    assert 0.70 < wins / 4000 < 0.80, wins       # weight 3 vs 1 should win about 75%
    assert drand_round_at(drand_round_time(1000)) == 1000 and drand_round_at(DRAND["genesis_time"]) == 1
    assert parse_tiers("Grand Prize:1,Runner-up:5", 9) == [["Grand Prize", 1], ["Runner-up", 5]]
    assert mask("someone@example.com") == "so***@example.com"
    pj = os.path.join(d, "c.json")
    with open(pj, "w") as resource:
        resource.write(json.dumps({"comments": [{"owner": {"username": "ann"}, "text": "hi"}, {"owner": {"username": "Ann"}, "text": "again"}, {"owner": {"username": "bob"}, "text": "x"}]}))
    rows, col, _ = load_entries(pj, None); assert col == "owner.username" and len(rows) == 3, (col, rows)
    ents, dupes, *_ = prepare(rows, col, None, set()); assert [e["id"] for e in ents] == ["ann", "bob"] and dupes == 1
    yj = os.path.join(d, "y.json")
    with open(yj, "w") as resource:
        resource.write(json.dumps({"kind": "youtube#commentThreadListResponse", "items": [{"id": "Ugx1", "snippet": {"topLevelComment": {"snippet": {"authorDisplayName": "Ann", "authorChannelId": {"value": "UCa"}, "textDisplay": "hi"}}}}, {"id": "Ugx2", "snippet": {"topLevelComment": {"snippet": {"authorDisplayName": "Bob", "authorChannelId": {"value": "UCb"}, "textDisplay": "yo"}}}}]}))
    rows, col, _ = load_entries(yj, None); assert col.endswith("authorChannelId.value") and len(rows) == 2 and rows[0][col] == "UCa", (col, rows)
    gj = os.path.join(d, "g.json")
    with open(gj, "w") as resource:
        resource.write(json.dumps({"data": [{"id": "1", "text": "hi", "from": {"id": "9", "username": "ann"}}, {"id": "2", "text": "x", "from": {"id": "8", "username": "bob"}}]}))
    rows, col, _ = load_entries(gj, None); assert col == "from.id", (col, rows)
    sc = scan([{"id": f"ava_k_{2290+i}@example.com"} for i in range(6)] + [{"id": "x@mailinator.com"}])
    assert any("trailing number" in n for n in sc) and any("disposable" in n for n in sc), sc
    rp = os.path.join(d, "rules.json")
    with open(rp, "w") as resource:
        resource.write(json.dumps({"tiers": "Grand Prize:1,Runner-up:5", "backups": 2, "id-column": "email", "weight-column": "entries", "exclude": "staff.txt"}))
    class R: rules = rp; tiers = None; backups = None; winners = None; id_column = None; weight_column = None; exclude = None
    apply_rules(R)
    assert (R.tiers, R.backups, R.winners, R.id_column, R.weight_column, R.exclude) == ("Grand Prize:1,Runner-up:5", 2, 1, "email", "entries", "staff.txt"), vars(R)
    class O: rules = rp; tiers = "Only:1"; backups = 0; winners = None; id_column = None; weight_column = None; exclude = None
    apply_rules(O); assert O.tiers == "Only:1" and O.backups == 0 and O.id_column == "email", vars(O)
    class N: rules = None; tiers = None; backups = None; winners = None
    apply_rules(N); assert (N.backups, N.winners) == (0, 1), vars(N)
    # a flagged list must be writable and must feed --exclude, which is the only route at export scale
    import tempfile as _tf, csv as _csv, os as _os
    with _tf.NamedTemporaryFile("w", suffix=".csv", delete=False, newline="") as fh:
        w = _csv.writer(fh); w.writerow(["email"])
        for i in range(50): w.writerow([f"p{i}@" + ("mailinator.com" if i % 5 == 0 else "example.com")])
    out = fh.name + ".flagged"
    class _A: pass
    _a = _A(); _a.input = fh.name; _a.id_column = "email"; _a.weight_column = None; _a.exclude = None
    _a.tiers = "Grand:1"; _a.winners = None; _a.backups = None; _a.rules = None; _a.draw_at = None; _a.flagged_out = out
    cmd_commit(_a)
    with open(out) as resource:
        flagged = [l.strip() for l in resource if l.strip()]
    assert len(flagged) == 10, f"every disposable id must be written out, got {len(flagged)}"
    assert all(f.endswith("@mailinator.com") for f in flagged), flagged
    _os.unlink(fh.name); _os.unlink(out)
    # The commitment preview must expose missing weights before a seed is fetched or a draw is run.
    import contextlib, io
    preview_file = os.path.join(d, "preview.csv")
    with open(preview_file, "w") as resource:
        resource.write("id,entries\nalpha,2\nalpha,3\nbeta,1\ngamma,\ndelta,0\nepsilon,4\n")
    exclusion_file = os.path.join(d, "exclude.txt")
    with open(exclusion_file, "w", encoding="utf-8-sig") as resource:
        resource.write("epsilon\n")
    _a.input = preview_file; _a.id_column = "id"; _a.weight_column = "entries"
    _a.exclude = exclusion_file; _a.flagged_out = None
    output = io.StringIO()
    with contextlib.redirect_stdout(output): cmd_commit(_a)
    assert "rows_read 6, unique_eligible 2, duplicates_merged 1, excluded 1, rows_with_invalid_weight 2" in output.getvalue(), output.getvalue()
    # Keep the worked example tied to the actual commitment output, not a copied round.
    import pathlib, re
    procedure = (pathlib.Path(__file__).resolve().parents[1] / "references" / "draw-procedure.md").read_text()
    documented_time = re.search(r'commit entries\.csv[^\n]*--draw-at "([^"]+)"', procedure)
    documented_round = re.search(r'--seed-drand (\d+) --audit draw-2026-09-12\.json', procedure)
    assert documented_time and documented_round, "documented commit and draw commands must be present"
    _a.draw_at = documented_time.group(1)
    example_round = int(documented_round.group(1))
    output = io.StringIO()
    with contextlib.redirect_stdout(output): cmd_commit(_a)
    assert f"drand round at or after {_a.draw_at}: {example_round} " in output.getvalue(), output.getvalue()
    assert example_round == 6457886
    assert drand_round_time(example_round) == datetime.datetime.fromisoformat(_a.draw_at).timestamp()
    # Scheduling must round up, while current-round lookup must still round down.
    boundary = drand_round_time(6553045)
    for offset, expected_round in ((0, 6553045), (1, 6553046), (29, 6553046)):
        requested = boundary + offset
        _a.draw_at = datetime.datetime.fromtimestamp(requested, datetime.timezone.utc).isoformat()
        output = io.StringIO()
        with contextlib.redirect_stdout(output): cmd_commit(_a)
        assert f"drand round at or after {_a.draw_at}: {expected_round} " in output.getvalue(), output.getvalue()
        assert drand_round_at_or_after(requested) == expected_round
        assert drand_round_time(expected_round) >= requested
        assert drand_round_time(expected_round - 1) < requested
        assert drand_round_at(requested) == 6553045
    verifier_self_test()
    print("self-test passed"); return 0

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    def common(p):
        p.add_argument("input"); p.add_argument("--winners", type=int); p.add_argument("--tiers"); p.add_argument("--backups", type=int)
        p.add_argument("--id-column", help="person/account column or dotted JSON path; required for ambiguous id fields or unrecognized headers"); p.add_argument("--weight-column"); p.add_argument("--exclude")
        p.add_argument("--rules", help="JSON file holding tiers, backups, winners, id-column, weight-column and exclude, so commit and draw read the same rules")
    c = sub.add_parser("commit", help="hash the input and rules; optionally name the drand round for a draw time"); common(c); c.add_argument("--draw-at", help="ISO time with offset, e.g. 2026-09-12T09:00:00+10:00")
    c.add_argument("--flagged-out", help="write flagged ids for review, then rerun commit with the approved file as --exclude and final rules. Publish the new commitment before the seed exists, then draw with the same input, exclusions and rules")
    d = sub.add_parser("draw", help="run the draw once"); common(d)
    seeds = d.add_mutually_exclusive_group(required=True)
    seeds.add_argument("--seed", help="text for reproduction; fairness requires a preannounced future source beyond organizer control")
    seeds.add_argument("--seed-drand", help="drand round number announced in advance"); seeds.add_argument("--seed-nist", help="unix time of a NIST beacon pulse announced in advance")
    d.add_argument("--audit"); d.add_argument("--winners-csv"); d.add_argument("--mask", action="store_true", help="print masked ids for announcements")
    v = sub.add_parser("verify", help="recompute a draw from its audit record"); v.add_argument("audit_file"); v.add_argument("--input"); v.add_argument("--exclude")
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    if a.cmd in ("commit", "draw"): apply_rules(a)
    return {"commit": cmd_commit, "draw": cmd_draw, "verify": cmd_verify}.get(a.cmd, lambda a: ap.print_help() or 2)(a)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
