#!/usr/bin/env python3
"""Read a Gleam Actions export (one row per completed action) into the numbers the review needs. No dependencies.

  python3 gleam_export.py export.csv                 # summary, then the review.py command to run
  python3 gleam_export.py export.csv --actions-csv actions.csv --entrants-csv entrants.csv
  python3 gleam_export.py --self-test

Columns read: Email (the person, or a confirmed stable ID via --person-column), Status (Valid, Invalid, Winner), Action, Entries (worth), Country, When, Referring URL.
Entrants are unique person identifiers with at least one valid row. Actions completed are valid rows. Entries are the sum of the
Entries column on valid rows. Impressions are not in this export: pass them from the Reporting tab. Nothing leaves the
machine and no row is printed: the summary is aggregates only.
Missing identifiers are rejected before aggregation or output. Display names are never inferred as identifiers.
Use --person-column "User ID" only after confirming that the column identifies people, not actions.
Email identifiers are lowercased; opaque IDs retain case and are exported under entrant_id.
A row whose Entries is missing, nonnumeric, nonpositive or non-finite counts at zero in the summary and is
reported; the draw export refuses the file until those rows are reconciled against the campaign records, since a
chance the export invented is worse than a review one row short. Valid fractional weights are preserved in both.

The review.py command printed at the end passes --invalid as invalid Entries worth, the Entries column summed over rows
whose Status is Invalid. The row count is printed separately as "invalid rows".
"""
import argparse, collections, csv, datetime as dt, math, shlex, sys
from pathlib import Path

# A custom title is evidence of an action, not proof of the underlying configuration.
# Keep ambiguous subscriptions unknown. Explicit platform names take precedence over email cues.
def classify_action(action):
    """Return (asset key, benchmark name, family) from one shared title classifier."""
    import re
    a = action.lower()
    if a.strip() == "watch a video": return None, "Watch a Video", "visit"
    if "youtube" in a and "visit" in a:
        return None, "YouTube Channel Visits", "visit"
    if any(w in a for w in ("check ", "read ", "learn", "see how", "program", "watch", "view ", "visit ")):
        return None, "Visit a Page", "visit"
    platforms = (("youtube", "youtube_subscribes", "", "subscribe"),
                 ("instagram", "instagram_follows", "Instagram Follows", "follow"),
                 ("tiktok", "tiktok_follows", "TikTok Follows", "follow"),
                 ("twitch", "twitch_follows", "Twitch Follows", "follow"),
                 ("discord", "discord_joins", "Chat Members", "join"))
    for platform, asset, benchmark, verb in platforms:
        if platform in a:
            if verb in a: return asset, benchmark, "follow"
            if "subscribe" in a: return None, "Twitch Subscribers" if platform == "twitch" else "", "follow"
            if "comment" in a and platform == "instagram": return None, "Instagram Comments", "content"
            if "visit" in a: return None, "YouTube Channel Visits" if platform == "youtube" else "Visit a Page", "visit"
            return None, "", None
    if "follow" in a and re.search(r"\bx\b|twitter", a):
        return "x_follows", "X Follows", "follow"
    if re.search(r"\b(?:refer|refers|referred|referring|referral|referrals)\b", a): return "referrals", "Viral Shares", "share"
    if a.strip(" :") == "newsletter" or (any(w in a for w in ("newsletter", "email", "mailing list", "our list", "giveaway list")) and any(w in a for w in ("subscri", "sign up", "signup", "join", "opt in", "opt-in"))):
        return "emails", "Email Subscriptions", "email"
    if "share" in a: return None, "", "share"
    for name, words, family in (
        ("Secret Code", ("secret code",), None), ("Loyalty Bonuses", ("loyalty",), None),
        ("Bonus", ("bonus", "entry confirmed"), None), ("X Reposts", ("repost", "retweet"), "share"),
        ("X Posts", ("post on x", "tweet"), "content"), ("Facebook visits", ("facebook",), "visit"),
        ("Answer a Question", ("question", "answer"), "content"), ("Visit a Page", ("visit",), "visit")):
        if any(w in a for w in words): return None, name, family
    if any(w in a for w in ("share", "viral")): return None, "", "share"
    if any(w in a for w in ("upload", "submit", "photo", "video", "post a", "write", "comment")): return None, "", "content"
    if any(w in a for w in ("follow", "join", "like")): return None, "", "follow"
    return None, "", None


def kind(action):
    return classify_action(action)[0]


def generic_name(action):
    return classify_action(action)[1]

def parse_when(s):
    """Read export timestamps without changing the account-local time or UTC offset."""
    value = (s or "").strip()
    for separator in (" ", "T"):
        for seconds in ("%S", "%S.%f"):
            for zone in (" %z", "%z", ""):
                try: return dt.datetime.strptime(value, f"%Y-%m-%d{separator}%H:%M:{seconds}{zone}")
                except ValueError: continue
    try: return dt.datetime.strptime(value, "%d/%m/%Y %H:%M")
    except ValueError: return None

def read_rows(path, strict=False):
    """Rows with their Entries parsed. A row whose Entries is blank, zero, negative or not a number counts as
    unweighted: the summary keeps it at zero and reports it, the draw export refuses it, because a chance the
    export invented is worse than a review that is one row short."""
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    for number, row in enumerate(rows, 2):
        try:
            weight = float(row.get("Entries") or "")
        except (TypeError, ValueError):
            weight = float("nan")
        if not math.isfinite(weight) or weight <= 0:
            if strict:
                raise ValueError(f"row {number}: Entries must be a positive finite number; reconcile earned weights before export")
            weight = 0.0; row["_unweighted"] = True
        row["Entries"] = weight
    return rows


def weight_total(rows):
    try:
        total = math.fsum(r["Entries"] for r in rows)
    except OverflowError:
        raise ValueError("Entries total exceeds the finite range; reconcile earned weights before export") from None
    return total


def person_identifiers(rows, who=None):
    """Validate one confirmed identity column for every source row before counting or writing."""
    who = who or "Email"
    if not rows or who not in rows[0]:
        raise ValueError("no person identifier column available; pass --person-column with a confirmed stable person ID column")
    if who.strip().lower() in ("name", "entrant", "user", "display name", "display_name"):
        raise ValueError("display names cannot identify people safely; supply Email or a confirmed stable person ID column")
    missing = [str(number) for number, row in enumerate(rows, 2) if not (row.get(who) or "").strip()]
    if missing:
        raise ValueError(f"missing person identifiers at source CSV rows {', '.join(missing)}; "
                         "reconcile identities or pass --person-column with a complete confirmed stable person ID column")
    email = who.strip().lower().replace("_", "").replace("-", "").replace(" ", "") in (
        "email", "emailaddress", "entrantemail", "useremail", "contactemail", "contactemailaddress")
    for row in rows:
        value = row[who].strip()
        row["_person"] = value.lower() if email else value
    return who, "email" if email else "entrant_id"


def write_entrants(path, destination, who=None):
    rows = read_rows(path, strict=True)
    _, identifier_header = person_identifiers(rows, who)
    weight_total(rows)
    with open(destination, "w", newline="", encoding="utf-8") as g:
        writer = csv.writer(g)
        writer.writerow([identifier_header, "entries"])
        for row in rows:
            if (row.get("Status") or "Valid").strip().lower() in ("valid", "winner"):
                writer.writerow([row["_person"], row["Entries"]])


def load(path, who=None):
    rows = read_rows(path)
    if not rows or "Action" not in rows[0]: sys.exit("not a Gleam Actions export: no Action column")
    who, _ = person_identifiers(rows, who)
    valid = [r for r in rows if (r.get("Status") or "Valid").strip().lower() in ("valid", "winner")]
    bad = [r for r in rows if (r.get("Status") or "Valid").strip().lower() not in ("valid", "winner")]
    people = {r["_person"] for r in valid}
    per_action = collections.Counter(r["Action"].strip() for r in valid)
    entries = weight_total(valid)
    assets = collections.Counter()
    for r in valid:
        k = kind(r["Action"])
        if k: assets[k] += 1
    whens = [w for w in (parse_when(r.get("When") or "") for r in valid) if w]
    days = collections.Counter(w.date().isoformat() for w in whens); hours = collections.Counter(w.hour for w in whens)
    # Match the full report: each valid Entrant contributes their earliest dated row,
    # with undated rows last and file order breaking ties. Missing countries remain unknown.
    first = {}
    for r in sorted(valid, key=lambda row: (parse_when(row.get("When") or "").timestamp()
                                          if parse_when(row.get("When") or "") else float("inf"))):
        first.setdefault(r["_person"], r)
    countries = collections.Counter(r.get("Country") or "unknown" for r in first.values())
    refs = collections.Counter()
    for r in valid:
        u = (r.get("Referring URL") or "").strip()
        refs[u.split("/")[2] if u.startswith("http") and u.count("/") >= 2 else (u or "direct or unknown")] += 1
    span = (max(whens).date() - min(whens).date()).days + 1 if whens else None
    return {"rows": len(rows), "valid_rows": len(valid), "invalid_rows": len(bad), "invalid_entries": weight_total(bad),
            "unweighted_rows": sum(1 for r in rows if r.get("_unweighted")),
            "contestants": len(people), "entries": entries,
            "actions_completed": len(valid), "per_action": dict(per_action.most_common()), "assets": dict(assets), "days_covered": span,
            "by_day": dict(sorted(days.items())), "by_hour_local": dict(sorted(hours.items())), "countries": dict(countries.most_common(10)),
            "country_share_top": countries.most_common(1)[0][1] / len(people) if countries and people else None, "referrers": dict(refs.most_common(8)), "person_column": who}

def review_command(s, args):
    script = shlex.quote(str(Path(__file__).resolve().with_name("review.py")))
    cmd = f"python3 {script} --contestants {s['contestants']} --entries {s['entries']} --invalid {s['invalid_entries']} --actions-completed {s['actions_completed']}"
    if getattr(args, "days", None) is not None: cmd += f" --days {args.days}"
    if getattr(args, "methods", None) is not None: cmd += f" --methods {args.methods}"
    for k in ("emails", "referrals", "x_follows", "instagram_follows", "tiktok_follows", "twitch_follows", "youtube_subscribes", "discord_joins"):
        if s["assets"].get(k): cmd += f" --{k.replace('_', '-')} {s['assets'][k]}"
    if args.actions_csv: cmd += f" --actions {shlex.quote(str(Path(args.actions_csv).resolve()))}"
    return cmd + " --impressions N   # Impressions from the Reporting tab"

def self_test():
    # The shared parser preserves fractional precision and explicit offsets.
    for zone, offset in (("Z", dt.timedelta()), ("+10:00", dt.timedelta(hours=10)), ("-04:30", -dt.timedelta(hours=4, minutes=30)), ("", None)):
        for separator in ("T", " "):
            parsed = parse_when(f"2026-05-01{separator}00:15:00.123456{zone}")
            assert parsed.microsecond == 123456 and parsed.utcoffset() == offset
            assert parsed.date() == dt.date(2026, 5, 1) and parsed.hour == 0
    for malformed in (None, "", "bad-date", "2026-05-01", "2026-05-01T00:15:00.nopeZ", "2026-13-01T00:15:00.123Z"):
        assert parse_when(malformed) is None, malformed
    assert parse_when("01/05/2026 10:30") == dt.datetime(2026, 5, 1, 10, 30)
    assert parse_when("2026-05-01 10:30:00.5 +1000").utcoffset() == dt.timedelta(hours=10)
    for title in ("What is your preferred flavour?", "Tell us your preferences", "Answer a question: which do you prefer?"):
        assert classify_action(title)[0] is None and classify_action(title)[2] != "share"
    assert generic_name("Answer a question: which do you prefer?") == "Answer a Question"
    for title in ("Refer a friend", "Referral bonus", "Friends referred", "Referrals"):
        assert classify_action(title) == ("referrals", "Viral Shares", "share")
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
    assert s["countries"] == {"Australia": 1, "Canada": 1} and s["country_share_top"] == 0.5
    # Activity volume does not weight audience geography; choose the earliest valid row.
    geo_path = os.path.join(d, "geo.csv")
    with open(geo_path, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["Email", "Status", "Action", "Entries", "Country", "When"])
        w.writerows([["a@example.com", "Valid", "Visit", 1, "Australia", "2026-05-02 10:00:00"]] * 9)
        w.writerow(["a@example.com", "Valid", "Visit", 1, "Canada", "2026-05-01 10:00:00"])
        w.writerow(["b@example.com", "Winner", "Visit", 1, "Australia", ""])
        w.writerow(["c@example.com", "Invalid", "Visit", 1, "France", "2026-04-01 10:00:00"])
    geo = load(geo_path)
    assert geo["countries"] == {"Canada": 1, "Australia": 1} and geo["country_share_top"] == 0.5
    import campaign_report
    class GeoArgs: impressions = None; prize_cost = None; prize_value = None; plan_cost = None; benchmark_cpl = None; sends = None; partners = None
    report = campaign_report.analyze(campaign_report.load(geo_path), GeoArgs)
    assert geo["countries"] == dict(report["countries"])
    import contextlib, io
    printed = io.StringIO()
    with contextlib.redirect_stdout(printed):
        assert main([geo_path]) == 0
    assert "top countries (share of valid Entrants)" in printed.getvalue()
    assert "'Canada': '50%'" in printed.getvalue() and "'Australia': '50%'" in printed.getvalue()
    class A: actions_csv = None
    assert "--invalid 4" in review_command(s, A), review_command(s, A)
    assert "# Impressions from the Reporting tab" in review_command(s, A) and "views" not in review_command(s, A).lower(), review_command(s, A)
    assert generic_name("Follow @Gleamapp on Instagram:") == "Instagram Follows" and generic_name("Read Our Ideas:") == "Visit a Page" and generic_name("Subscribe to Our Giveaway List") == "Email Subscriptions", "generic"
    assert kind("Follow @Gleamapp on Instagram:") == "instagram_follows" and kind("Follow Gleamapp on X") == "x_follows" and kind("Subscribe to Our Giveaway List") == "emails"
    import contextlib, io
    output = os.path.join(d, "entrants.csv")
    with contextlib.redirect_stdout(io.StringIO()):
        assert main([p, "--entrants-csv", output]) == 0
    with open(output, newline="") as exported:
        exported_rows = list(csv.DictReader(exported))
    assert [float(r["entries"]) for r in exported_rows] == [1, 2, 5]
    # Confirmed stable IDs separate shared names, survive blank emails, and retain case.
    identity_path = Path(d) / "identities.csv"
    with identity_path.open("w", newline="") as source:
        writer = csv.writer(source)
        writer.writerow(["User ID", "Name", "Email", "Status", "Action", "Entries"])
        writer.writerows([["U1", "Alex Smith", "", "Valid", "Visit", 1.25],
                          ["U2", "Alex Smith", "", "Valid", "Visit", 2],
                          ["u1", "Alex Smith", "", "Winner", "Visit", 3],
                          ["U1", "Alex Smith", "", "Valid", "Visit", 2.5]])
    identified = load(identity_path, "User ID")
    assert identified["contestants"] == 3 and identified["entries"] == 8.75
    identity_output = Path(d) / "identity-entrants.csv"
    with contextlib.redirect_stdout(io.StringIO()):
        assert main([str(identity_path), "--person-column", "User ID", "--entrants-csv", str(identity_output)]) == 0
    with identity_output.open(newline="") as exported:
        identity_rows = list(csv.DictReader(exported))
    assert list(identity_rows[0]) == ["entrant_id", "entries"]
    totals = collections.Counter()
    for row in identity_rows: totals[row["entrant_id"]] += float(row["entries"])
    assert totals == {"U1": 3.75, "U2": 2, "u1": 3}
    # Neither an unresolved identity nor a missing ID can destroy existing outputs.
    before = identity_output.read_bytes()
    for chosen in (None, "Name", "Missing column"):
        for operation in (lambda: load(identity_path, chosen),
                          lambda: write_entrants(identity_path, identity_output, chosen)):
            try: operation()
            except ValueError: pass
            else: raise AssertionError("unresolved identity accepted")
            assert identity_output.read_bytes() == before
    for status in ("Valid", "Invalid"):
        with identity_path.open("w", newline="") as source:
            writer = csv.writer(source)
            writer.writerow(["User ID", "Email", "Status", "Action", "Entries"])
            writer.writerows([["U1", "a@example.com", "Valid", "Visit", 1],
                              [" ", "b@example.com", status, "Visit", 2]])
        for operation in (lambda: load(identity_path, "User ID"),
                          lambda: write_entrants(identity_path, identity_output, "User ID")):
            try: operation()
            except ValueError as exc: assert "source CSV rows 3" in str(exc)
            else: raise AssertionError("partially missing identity accepted")
            assert identity_output.read_bytes() == before
        # CLI validates identities before opening either output destination.
        with contextlib.redirect_stderr(io.StringIO()):
            try:
                main([str(identity_path), "--person-column", "User ID", "--actions-csv", str(identity_output),
                      "--entrants-csv", str(identity_output)])
            except SystemExit as exc: assert exc.code == 2
            else: raise AssertionError("CLI accepted missing identity")
        assert identity_output.read_bytes() == before
    # Email normalization still joins repeated actions for the same address.
    with identity_path.open("w", newline="") as source:
        writer = csv.writer(source); writer.writerow(["Email", "Action", "Entries"])
        writer.writerows([["A@example.com", "Visit", 1], [" a@example.com ", "Visit", 2]])
    assert load(identity_path)["contestants"] == 1
    # Both public paths reject unreconciled weights before creating or replacing an export.
    for invalid in ("", "unknown", "0", "-1", "NaN", "Infinity", "-Infinity"):
        with open(p, "w", newline="") as source:
            writer = csv.writer(source)
            writer.writerow(["Email", "Action", "Entries"])
            writer.writerow(["a@example.com", "Subscribe", invalid])
        assert load(p)["unweighted_rows"] == 1 and load(p)["entries"] == 0, load(p)
        with contextlib.redirect_stderr(io.StringIO()):
            try: main([p, "--actions-csv", output, "--entrants-csv", str(identity_output)])
            except SystemExit as exc: assert exc.code == 2
            else: raise AssertionError("CLI accepted unreconciled weight")
        with open(output, newline="") as exported:
            assert list(csv.DictReader(exported)) == exported_rows
        assert identity_output.read_bytes() == before
        try:
            write_entrants(p, output, "Email")
        except ValueError:
            pass
        else:
            raise AssertionError("invalid weight accepted by the draw export")
        with open(output, newline="") as exported:
            assert list(csv.DictReader(exported)) == exported_rows
    for columns, values in ((["Email", "Action"], ["a@example.com", "Subscribe"]),
                            (["Email", "Action", "Entries"], ["a@example.com", "Subscribe"])):
        with open(p, "w", newline="") as source:
            writer = csv.writer(source); writer.writerow(columns); writer.writerow(values)
        assert load(p)["unweighted_rows"] == 1, load(p)
        try:
            write_entrants(p, output, "Email")
        except ValueError:
            pass
        else:
            raise AssertionError("missing weight accepted by the draw export")
    with open(p, "w", newline="") as source:
        writer = csv.writer(source); writer.writerow(["Email", "Action", "Entries"])
        writer.writerows([["a@example.com", "Subscribe", "1.25"], ["a@example.com", "Visit", "2.5"]])
    assert load(p)["entries"] == 3.75
    write_entrants(p, output, "Email")
    assert kind("Refer Friends For Extra Entries") == "referrals" and kind("Join the Referral Program:") is None
    assert generic_name("Join the Referral Program:") == "Visit a Page" and generic_name("Refer Friends For Extra Entries") == "Viral Shares"
    import shlex
    A.actions_csv = "action results.csv"
    command = shlex.split(review_command(s, A))
    assert command[command.index("--actions") + 1] == str(Path(A.actions_csv).resolve()), command
    assert "--days" not in review_command(s, A) and "--methods" not in review_command(s, A)
    A.days = 14; A.methods = 6
    assert "--days 14 --methods 6" in review_command(s, A)
    # Printed commands work outside the install, including paths with spaces.
    import shutil, subprocess
    installation = Path(d) / "installed skill with spaces"
    (installation / "scripts").mkdir(parents=True)
    (installation / "references").mkdir()
    source = Path(__file__).resolve().parent
    for filename in ("gleam_export.py", "review.py"):
        shutil.copyfile(source / filename, installation / "scripts" / filename)
    shutil.copyfile(source.parent / "references" / "percentiles.json", installation / "references" / "percentiles.json")
    elsewhere = Path(d) / "another directory"; elsewhere.mkdir()
    for cwd in (installation, elsewhere):
        converted = subprocess.run([sys.executable, str(installation / "scripts" / "gleam_export.py"), p], cwd=cwd, capture_output=True, text=True)
        assert converted.returncode == 0, converted.stderr
        printed = next(line.removeprefix("run: ") for line in converted.stdout.splitlines() if line.startswith("run: "))
        args = shlex.split(printed, comments=True)
        args[args.index("--impressions") + 1] = "10"
        assert args[1] == str((installation / "scripts" / "review.py").resolve())
        checked = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
        assert checked.returncode == 0, checked.stderr

    assert classify_action("Subscribe to our YouTube channel") == ("youtube_subscribes", "", "follow")
    assert classify_action("Subscribe to our newsletter") == ("emails", "Email Subscriptions", "email")
    for title in ("Subscribe", "Subscribe to Brand", "Sign up", "Email a friend", "Enter your email", "Follow @brand"):
        assert kind(title) is None, title
    assert classify_action("Visit our newsletter page") == (None, "Visit a Page", "visit")
    assert classify_action("Visit our YouTube channel") == (None, "YouTube Channel Visits", "visit")
    assert classify_action("Watch a Video") == (None, "Watch a Video", "visit")
    assert classify_action("Join our referral program") == (None, "Visit a Page", "visit")
    assert classify_action("Refer a friend") == ("referrals", "Viral Shares", "share")
    assert classify_action("Follow on Instagram") == ("instagram_follows", "Instagram Follows", "follow")
    assert classify_action("Subscribe on Twitch") == (None, "Twitch Subscribers", "follow")
    assert classify_action("Watch our subscription program overview") == (None, "Visit a Page", "visit")
    for title in ("Subscribe", "Subscribe to Brand", "Sign up"):
        assert classify_action(title) == (None, "", None), title
    print("self-test passed"); return 0

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export", nargs="?"); ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--days", type=int, help="configured campaign duration in days, not the activity span")
    ap.add_argument("--methods", type=int, help="configured available method count, including unused methods")
    ap.add_argument("--actions-csv", help="write action,completions for review.py --actions")
    ap.add_argument("--entrants-csv", help="write email or entrant_id,entries for valid people, for the draw script")
    ap.add_argument("--person-column", help="confirmed stable person identifier column (defaults to Email, never a display name or action ID)")
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    if not a.export: ap.error("export path required")
    try:
        s = load(a.export, a.person_column)
        if a.entrants_csv:
            # Validate draw weights before opening either requested output.
            checked_rows = read_rows(a.export, strict=True)
            person_identifiers(checked_rows, s["person_column"])
            weight_total(checked_rows)
    except ValueError as exc:
        ap.error(str(exc))
    print(f"rows {s['rows']:,}  valid {s['valid_rows']:,}  invalid rows {s['invalid_rows']:,}  invalid entries {s['invalid_entries']:,}  entrants {s['contestants']:,}  entries {s['entries']:,}  actions completed {s['actions_completed']:,}  observed activity span in days {s['days_covered']}  completed method titles {len(s['per_action'])}")
    if s["unweighted_rows"]: print(f"rows without a valid Entries value {s['unweighted_rows']:,} (counted at zero here; the draw export refuses them until reconciled)")
    print("assets", {k: f"{v:,}" for k, v in s["assets"].items()})
    print("per action"); [print(f"  {n:>7,}  {name}") for name, n in s["per_action"].items()]
    print("top countries (share of valid Entrants)", {k: f"{v / s['contestants']:.0%}" for k, v in list(s["countries"].items())[:6]})
    print("referrers", {k: v for k, v in s["referrers"].items()})
    if s["by_day"]:
        top = sorted(s["by_day"].items(), key=lambda kv: -kv[1])[:3]; print("busiest days", top, "  first", next(iter(s["by_day"])), "last", list(s["by_day"])[-1])
    if a.actions_csv:
        with open(a.actions_csv, "w", newline="") as f:
            w = csv.writer(f); w.writerow(["action", "completions", "generic"]); [w.writerow([k, v, generic_name(k)]) for k, v in s["per_action"].items()]
    if a.entrants_csv:
        try:
            write_entrants(a.export, a.entrants_csv, s["person_column"])
        except ValueError as exc:
            ap.error(str(exc))
        print("entrants written for the draw script, one row per valid action, weights add up per person")
    print("\nrun:", review_command(s, a)); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
