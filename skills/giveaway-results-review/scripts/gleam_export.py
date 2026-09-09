#!/usr/bin/env python3
"""Read a Gleam Actions export (one row per completed action) into the numbers the review needs. No dependencies.

  python3 gleam_export.py export.csv                 # summary, then the review.py command to run
  python3 gleam_export.py export.csv --actions-csv actions.csv --entrants-csv entrants.csv
  python3 gleam_export.py --self-test

Columns read: Email (the person), Status (Valid, Invalid, Winner), Action, Entries (worth), Country, When, Referring URL.
Contestants are unique emails with at least one valid row. Actions completed are valid rows. Entries are the sum of the
Entries column on valid rows. Impressions are not in this export: pass them from the Reporting tab. Nothing leaves the
machine and no row is printed: the summary is aggregates only.

The review.py command printed at the end passes --invalid as invalid entries worth, the Entries column summed over rows
whose Status is Invalid. The row count is printed separately as "invalid rows".
"""
import argparse, collections, csv, datetime as dt, sys

FOLLOW_KEYS = [("x_follows", ("follow", ("x", "twitter", "@"))), ("instagram_follows", ("follow", ("instagram",))), ("tiktok_follows", ("follow", ("tiktok",))),
               ("twitch_follows", ("follow", ("twitch",))), ("youtube_subscribes", ("subscribe", ("youtube",))), ("discord_joins", ("join", ("discord",)))]

def kind(action):
    a = action.lower()
    if "refer" in a: return "referrals"
    if ("subscribe" in a or "sign up" in a or "signup" in a or "newsletter" in a or "email" in a) and "youtube" not in a: return "emails"
    for key, (verb, nets) in FOLLOW_KEYS:
        if verb in a and any(n in a for n in nets):
            if key == "x_follows" and ("instagram" in a or "tiktok" in a or "twitch" in a): continue
            return key
    return None

GENERIC = [("Viral Shares", ("refer",)), ("Secret Code", ("secret code",)), ("Loyalty Bonuses", ("loyalty",)), ("Bonus", ("bonus", "entry confirmed")),
           ("Email Subscriptions", ("subscribe", "newsletter", "sign up", "signup")), ("Instagram Comments", ("comment", "instagram")), ("X Reposts", ("repost", "retweet")),
           ("X Posts", ("post on x", "tweet")), ("Instagram Follows", ("follow", "instagram")), ("TikTok Follows", ("follow", "tiktok")), ("Twitch Follows", ("follow", "twitch")),
           ("X Follows", ("follow", "x")), ("Facebook visits", ("facebook",)), ("YouTube Channel Visits", ("youtube",)), ("Chat Members", ("discord",)), ("Answer a Question", ("question", "answer")),
           ("Visit a Page", ("visit", "read", "check out", "view", "watch"))]

def generic_name(action):
    """Best guess at the Gleam action type behind an organizer's custom title, for the per-action benchmark."""
    a = action.lower()
    for name, words in GENERIC:
        if all(w in a for w in words) if len(words) == 2 and name.endswith(("Follows", "Comments")) else any(w in a for w in words): return name
    return ""

def parse_when(s):
    for fmt in ("%Y-%m-%d %H:%M:%S %z", "%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M", "%Y-%m-%dT%H:%M:%S%z"):
        try: return dt.datetime.strptime(s.strip(), fmt)
        except ValueError: continue
    return None

def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f: rows = list(csv.DictReader(f))
    if not rows or "Action" not in rows[0]: sys.exit("not a Gleam Actions export: no Action column")
    who = "Email" if "Email" in rows[0] else "Name"
    valid = [r for r in rows if (r.get("Status") or "Valid").strip().lower() in ("valid", "winner")]
    bad = [r for r in rows if (r.get("Status") or "Valid").strip().lower() not in ("valid", "winner")]
    people = {r[who].strip().lower() for r in valid if r.get(who)}
    per_action = collections.Counter(r["Action"].strip() for r in valid)
    entries = sum(float(r.get("Entries") or 0) for r in valid)
    assets = collections.Counter()
    for r in valid:
        k = kind(r["Action"])
        if k: assets[k] += 1
    whens = [w for w in (parse_when(r.get("When") or "") for r in valid) if w]
    days = collections.Counter(w.date().isoformat() for w in whens); hours = collections.Counter(w.hour for w in whens)
    countries = collections.Counter((r.get("Country") or "").strip() for r in valid if r.get("Country"))
    refs = collections.Counter()
    for r in valid:
        u = (r.get("Referring URL") or "").strip()
        refs[u.split("/")[2] if u.startswith("http") and u.count("/") >= 2 else (u or "direct or unknown")] += 1
    span = (max(whens).date() - min(whens).date()).days + 1 if whens else None
    return {"rows": len(rows), "valid_rows": len(valid), "invalid_rows": len(bad), "invalid_entries": int(sum(float(r.get("Entries") or 0) for r in bad)),
            "contestants": len(people), "entries": int(entries),
            "actions_completed": len(valid), "per_action": dict(per_action.most_common()), "assets": dict(assets), "days_covered": span,
            "by_day": dict(sorted(days.items())), "by_hour_local": dict(sorted(hours.items())), "countries": dict(countries.most_common(10)),
            "country_share_top": countries.most_common(1)[0][1] / len(valid) if countries and valid else None, "referrers": dict(refs.most_common(8)), "person_column": who}

def review_command(s, args):
    cmd = f"python3 review.py --contestants {s['contestants']} --entries {s['entries']} --invalid {s['invalid_entries']} --actions-completed {s['actions_completed']}"
    if s["days_covered"]: cmd += f" --days {s['days_covered']}"
    cmd += f" --methods {len(s['per_action'])}"
    for k in ("emails", "referrals", "x_follows", "instagram_follows", "tiktok_follows", "twitch_follows", "youtube_subscribes", "discord_joins"):
        if s["assets"].get(k): cmd += f" --{k.replace('_', '-')} {s['assets'][k]}"
    if args.actions_csv: cmd += f" --actions {args.actions_csv}"
    return cmd + " --impressions N   # impressions from the Reporting tab"

def self_test():
    import os, tempfile
    d = tempfile.mkdtemp(); p = os.path.join(d, "e.csv")
    with open(p, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["ID", "Email", "Status", "Action", "Entries", "Country", "When", "Referring URL"])
        w.writerow([1, "a@example.com", "Valid", "Subscribe to Our List", 1, "Australia", "2026-05-01 10:00:00 +1000", "https://x.com/p"])
        w.writerow([2, "a@example.com", "Valid", "Follow @brand on X", 2, "Australia", "2026-05-02 11:00:00 +1000", ""])
        w.writerow([3, "b@example.com", "Invalid", "Subscribe to Our List", 4, "Canada", "2026-05-02 12:00:00 +1000", ""])
        w.writerow([4, "c@example.com", "Winner", "Refer 3 Friends", 5, "Canada", "2026-05-03 09:00:00 +1000", ""])
    s = load(p)
    assert s["contestants"] == 2 and s["entries"] == 8 and s["invalid_rows"] == 1 and s["invalid_entries"] == 4 and s["assets"] == {"emails": 1, "x_follows": 1, "referrals": 1} and s["days_covered"] == 3, s
    class A: actions_csv = None
    assert "--invalid 4" in review_command(s, A), review_command(s, A)
    assert generic_name("Follow @Gleamapp on Instagram:") == "Instagram Follows" and generic_name("Read Our Ideas:") == "Visit a Page" and generic_name("Subscribe to Our Giveaway List") == "Email Subscriptions", "generic"
    assert kind("Follow @Gleamapp on Instagram:") == "instagram_follows" and kind("Follow Gleamapp on X") == "x_follows" and kind("Subscribe to Our Giveaway List") == "emails"
    print("self-test passed"); return 0

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export", nargs="?"); ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--actions-csv", help="write action,completions for review.py --actions")
    ap.add_argument("--entrants-csv", help="write email,entries for valid people, for the draw script")
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    if not a.export: ap.error("export path required")
    s = load(a.export)
    print(f"rows {s['rows']:,}  valid {s['valid_rows']:,}  invalid rows {s['invalid_rows']:,}  invalid entries {s['invalid_entries']:,}  contestants {s['contestants']:,}  entries {s['entries']:,}  actions completed {s['actions_completed']:,}  days {s['days_covered']}")
    print("assets", {k: f"{v:,}" for k, v in s["assets"].items()})
    print("per action"); [print(f"  {n:>7,}  {name}") for name, n in s["per_action"].items()]
    print("top countries", {k: f"{v / s['valid_rows']:.0%}" for k, v in list(s["countries"].items())[:6]})
    print("referrers", {k: v for k, v in s["referrers"].items()})
    if s["by_day"]:
        top = sorted(s["by_day"].items(), key=lambda kv: -kv[1])[:3]; print("busiest days", top, "  first", next(iter(s["by_day"])), "last", list(s["by_day"])[-1])
    if a.actions_csv:
        with open(a.actions_csv, "w", newline="") as f:
            w = csv.writer(f); w.writerow(["action", "completions", "generic"]); [w.writerow([k, v, generic_name(k)]) for k, v in s["per_action"].items()]
    if a.entrants_csv:
        with open(a.export, newline="", encoding="utf-8-sig") as f, open(a.entrants_csv, "w", newline="") as g:
            w = csv.writer(g); w.writerow(["email", "entries"]); who = s["person_column"]
            for r in csv.DictReader(f):
                if (r.get("Status") or "Valid").strip().lower() in ("valid", "winner") and r.get(who): w.writerow([r[who].strip().lower(), r.get("Entries") or 1])
        print("entrants written for the draw script, one row per valid action, weights add up per person")
    print("\nrun:", review_command(s, a)); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
