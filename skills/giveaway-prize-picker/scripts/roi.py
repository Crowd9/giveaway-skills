#!/usr/bin/env python3
"""Giveaway ROI, before or after the campaign. No dependencies.

Before the campaign, pricing a plan: we will spend 1,400 USD all in on a food and drink campaign we expect to draw 2,000 Entrants, and an email address is worth 4 USD to us.
  python3 roi.py --prize-cost 900 --stated-value 1500 --promotion 300 --admin 200 --contestants 2000 --vertical food_drink --value-per-email 4
After the campaign, pricing what actually happened: the same spend drew 1,800 Entrants, 1,500 addresses, 900 follows and 200 referral Entries.
  python3 roi.py --prize-cost 900 --stated-value 1500 --promotion 300 --contestants 1800 --emails 1500 --follows 900 --referrals 200 --value-per-email 4

Costs are what you pay. --stated-value is the retail figure you advertise, which is what the benchmarks below use, because the
export records what organizers stated, never what they paid. Benchmarks are medians from the ordinary segment of the campaign
export (116,283 campaigns that reached 100 Entrants). Value per email or follow is yours to supply: expected revenue per
subscriber over the period you care about, or what you would pay a channel for the same list. The script reports the breakeven
value if you give none. Nothing here predicts Entrants. Give the number you expect and the script prices it.

These benchmarks do not split by single-prize versus split-prize campaigns. Cost per Entrant runs meaningfully higher for a
split-prize campaign than a single Prize of matched value and vertical, see giveaway-winner-structure for the numbers.
"""
import argparse, json, math, sys
from pathlib import Path

# Source: analysis/output/roi_benchmarks.json, ordinary scope.
BENCH = {
 "all": {
  "usd_per_contestant": 0.42,
  "usd_per_email": 0.4,
  "usd_per_follow": 0.47,
  "usd_per_referral_entry": 2.9,
  "emails_per_campaign": 714,
  "stated_pool_usd": 299.0
 },
 "by_band": {
  "100-250": {
   "usd_per_contestant": 0.77,
   "usd_per_email": 1.03,
   "usd_per_follow": 0.74,
   "usd_per_referral_entry": 8.57,
   "emails_per_campaign": 157,
   "stated_pool_usd": 120.0,
   "n": 33021
  },
  "250-500": {
   "usd_per_contestant": 0.39,
   "usd_per_email": 0.34,
   "usd_per_follow": 0.36,
   "usd_per_referral_entry": 3.12,
   "emails_per_campaign": 354.0,
   "stated_pool_usd": 148.0,
   "n": 25625
  },
  "500-1k": {
   "usd_per_contestant": 0.37,
   "usd_per_email": 0.42,
   "usd_per_follow": 0.43,
   "usd_per_referral_entry": 2.51,
   "emails_per_campaign": 646,
   "stated_pool_usd": 260.0,
   "n": 21789
  },
  "1k-2.5k": {
   "usd_per_contestant": 0.36,
   "usd_per_email": 0.39,
   "usd_per_follow": 0.46,
   "usd_per_referral_entry": 2.21,
   "emails_per_campaign": 1346.0,
   "stated_pool_usd": 533.0,
   "n": 19974
  },
  "2.5k-10k": {
   "usd_per_contestant": 0.29,
   "usd_per_email": 0.29,
   "usd_per_follow": 0.38,
   "usd_per_referral_entry": 2.18,
   "emails_per_campaign": 3711,
   "stated_pool_usd": 1299.0,
   "n": 12703
  },
  "10k+": {
   "usd_per_contestant": 0.14,
   "usd_per_email": 0.16,
   "usd_per_follow": 0.19,
   "usd_per_referral_entry": 1.46,
   "emails_per_campaign": 16633.0,
   "stated_pool_usd": 3000.0,
   "n": 3171
  }
 },
 "by_vertical": {
  "music_media": {
   "usd_per_contestant": 0.17,
   "usd_per_email": 0.09,
   "usd_per_follow": 0.23,
   "usd_per_referral_entry": 2.0,
   "emails_per_campaign": 828.0,
   "stated_pool_usd": 70.0,
   "n": 24929
  },
  "gaming": {
   "usd_per_contestant": 0.42,
   "usd_per_email": 0.59,
   "usd_per_follow": 0.37,
   "usd_per_referral_entry": 2.11,
   "emails_per_campaign": 490,
   "stated_pool_usd": 200.0,
   "n": 24229
  },
  "unclassified": {
   "usd_per_contestant": 0.55,
   "usd_per_email": 0.55,
   "usd_per_follow": 0.72,
   "usd_per_referral_entry": 3.88,
   "emails_per_campaign": 580,
   "stated_pool_usd": 379.0,
   "n": 16477
  },
  "technology": {
   "usd_per_contestant": 0.6,
   "usd_per_email": 0.65,
   "usd_per_follow": 0.52,
   "usd_per_referral_entry": 2.54,
   "emails_per_campaign": 764.5,
   "stated_pool_usd": 545.0,
   "n": 15543
  },
  "fitness_outdoor": {
   "usd_per_contestant": 0.69,
   "usd_per_email": 0.66,
   "usd_per_follow": 1.13,
   "usd_per_referral_entry": 3.57,
   "emails_per_campaign": 849.5,
   "stated_pool_usd": 540.0,
   "n": 7795
  },
  "kids_family_pets": {
   "usd_per_contestant": 0.52,
   "usd_per_email": 0.57,
   "usd_per_follow": 0.76,
   "usd_per_referral_entry": 5.1,
   "emails_per_campaign": 488,
   "stated_pool_usd": 249.0,
   "n": 6831
  },
  "fashion_beauty": {
   "usd_per_contestant": 0.44,
   "usd_per_email": 0.41,
   "usd_per_follow": 0.52,
   "usd_per_referral_entry": 2.99,
   "emails_per_campaign": 880,
   "stated_pool_usd": 368.0,
   "n": 6457
  },
  "food_drink": {
   "usd_per_contestant": 0.5,
   "usd_per_email": 0.52,
   "usd_per_follow": 0.87,
   "usd_per_referral_entry": 2.78,
   "emails_per_campaign": 712,
   "stated_pool_usd": 427.5,
   "n": 4681
  },
  "travel_events": {
   "usd_per_contestant": 0.86,
   "usd_per_email": 0.84,
   "usd_per_follow": 2.72,
   "usd_per_referral_entry": 7.91,
   "emails_per_campaign": 650.0,
   "stated_pool_usd": 599.0,
   "n": 3969
  },
  "home": {
   "usd_per_contestant": 0.48,
   "usd_per_email": 0.54,
   "usd_per_follow": 0.91,
   "usd_per_referral_entry": 3.32,
   "emails_per_campaign": 867.5,
   "stated_pool_usd": 510.0,
   "n": 3710
  },
  "software": {
   "usd_per_contestant": 1.13,
   "usd_per_email": 1.19,
   "usd_per_follow": 1.28,
   "usd_per_referral_entry": 4.39,
   "emails_per_campaign": 979.0,
   "stated_pool_usd": 1000.0,
   "n": 1662
  }
 }
}
UPTAKE = {"email": 0.85, "follow": 0.53, "referral": 0.11}   # median completions per Entrant when the action is offered

def band(n): return "10k+" if n >= 10000 else "2.5k-10k" if n >= 2500 else "1k-2.5k" if n >= 1000 else "500-1k" if n >= 500 else "250-500" if n >= 250 else "100-250"

def money(x): return "-" if x is None else f"{x:,.2f}"

def run(a):
    if a.contestants is None or a.contestants <= 0:
        raise ValueError("contestants must be positive")
    for field in ("prize_cost", "stated_value", "promotion", "admin", "shipping", "emails", "follows", "referrals", "value_per_email", "value_per_follow", "value_per_referral"):
        value = getattr(a, field)
        if value is not None and (not math.isfinite(value) or value < 0):
            raise ValueError(field.replace("_", " ") + " must be finite and nonnegative")
    cost = (a.prize_cost or 0) + (a.promotion or 0) + (a.admin or 0) + (a.shipping or 0)
    stated = a.stated_value
    actual = any(count is not None for count in (a.emails, a.follows, a.referrals))
    est = any(count is None and action for count, action in ((a.emails, a.email_action), (a.follows, a.follow_action), (a.referrals, a.share_action)))
    emails = a.emails if a.emails is not None else (round(a.contestants * UPTAKE["email"]) if a.email_action else 0)
    follows = a.follows if a.follows is not None else (round(a.contestants * UPTAKE["follow"]) if a.follow_action else 0)
    refs = a.referrals if a.referrals is not None else (round(a.contestants * UPTAKE["referral"]) if a.share_action else 0)
    bench = BENCH["by_vertical"].get(a.vertical) or BENCH["by_band"][band(a.contestants)]
    label = a.vertical if a.vertical in BENCH["by_vertical"] else f"band {band(a.contestants)}"
    rows = [("Total cost (what you pay)", money(cost), "", ""),
            ("Cost per Entrant", money(cost / a.contestants), "", "")]
    if stated is not None:
        rows.append(("Stated value per Entrant", money(stated / a.contestants), money(bench["usd_per_contestant"]), label))
    for count, asset, key in ((emails, "email signup", "usd_per_email"),
                              (follows, "follow", "usd_per_follow"),
                              (refs, "referral entry", "usd_per_referral_entry")):
        if count:
            rows.append(("Cost per " + asset, money(cost / count), "", ""))
            if stated is not None:
                rows.append(("Stated value per " + asset, money(stated / count), money(bench[key]), label))
    value = (a.value_per_email or 0) * emails + (a.value_per_follow or 0) * follows + (a.value_per_referral or 0) * refs
    if value:
        rows += [("Value of what was produced", money(value), "", "your per-unit values"), ("Return per dollar", f"{value / cost:.2f}" if cost else "-", "", "")]
    elif emails and cost:
        rows += [("Breakeven value per email", money(cost / emails), "", "what each address must be worth for the campaign to pay for itself, with follows and referrals valued at zero")]
    note = "estimated from how often the actions you named are completed, given your expected Contestants" if est else "from the counts you gave"
    if est and actual:
        note = "from the counts you gave, with missing action counts estimated from expected Contestants"
    elif not est and not actual:
        note = "not supplied and no action estimates requested"
    return rows, note

def print_table(rows, header):
    widths = [max(len(str(x)) for x in col) for col in zip(header, *rows)]
    for line in [header] + rows: print("  ".join(str(x).ljust(w) for x, w in zip(line, widths)))

def benchmark_self_test():
    # Installed skills carry the reference, while the private aggregate source is optional.
    reference = Path(__file__).resolve().parents[1] / "references" / "roi-benchmarks.md"
    vertical_names = ("Music and media", "Gaming", "Unclassified", "Technology",
                      "Fitness and outdoor", "Kids, family, pets", "Fashion and beauty",
                      "Food and drink", "Travel and events", "Home", "Software")
    band_names = ("100 to 250", "250 to 500", "500 to 1,000", "1,000 to 2,500",
                  "2,500 to 10,000", "10,000 or more")
    lines = reference.read_text().splitlines()
    for section, names, columns in (
        ("by_vertical", vertical_names, {1: "n", 3: "stated_pool_usd", 5: "usd_per_email",
                                        6: "usd_per_follow", 7: "usd_per_referral_entry", 8: "emails_per_campaign"}),
        ("by_band", band_names, {1: "n", 2: "stated_pool_usd", 4: "usd_per_email",
                                5: "usd_per_follow", 6: "emails_per_campaign"}),
    ):
        for key, name in zip(BENCH[section], names):
            cells = next(line for line in lines if line.startswith("| " + name + " |"))
            cells = [cell.strip() for cell in cells.strip("|").split("|")]
            for column, metric in columns.items():
                value = BENCH[section][key][metric]
                expected = f"{value:.2f}" if metric.startswith("usd_per_") else f"{value:,.0f}"
                assert cells[column] == expected, (section, key, metric, cells[column], expected)
    source_path = Path(__file__).resolve().parents[3] / "analysis" / "output" / "roi_benchmarks.json"
    if source_path.is_file():
        source = json.loads(source_path.read_text())
        for section in BENCH:
            rows = {"all": BENCH[section]} if section == "all" else BENCH[section]
            for key, row in rows.items():
                source_row = source[section] if section == "all" else source[section][key]
                for metric, value in row.items():
                    expected = round(source_row[metric], 2) if metric.startswith("usd_per_") else source_row[metric]
                    assert value == expected, (section, key, metric, value, expected)


def self_test():
    class A: prize_cost = 900; stated_value = 1500; promotion = 300; admin = 200; shipping = 0; contestants = 2000; vertical = "food_drink"
    class A(A): emails = None; follows = None; referrals = None; email_action = True; follow_action = True; share_action = True; value_per_email = 4; value_per_follow = 0; value_per_referral = 0
    rows, note = run(A); d = {r[0]: r for r in rows}
    assert d["Total cost (what you pay)"][1] == "1,400.00" and d["Cost per email signup"][1] == "0.82" and d["Return per dollar"][1] == "4.86", rows
    A.value_per_email = 0; rows, _ = run(A); assert any(r[0] == "Breakeven value per email" for r in rows)
    A.stated_value = None
    rows, _ = run(A)
    assert not any(r[0].startswith("Stated value") or r[2] for r in rows), rows
    assert sum(r[0].startswith("Cost per") for r in rows) == 4, rows
    A.stated_value = 1500
    rows, _ = run(A); d = {r[0]: r for r in rows}
    assert d["Cost per Entrant"][1] == "0.70" and d["Stated value per Entrant"][1] == "0.75", rows
    A.stated_value = 0
    rows, _ = run(A)
    assert dict((r[0], r[1]) for r in rows)["Stated value per Entrant"] == "0.00"
    assert sum(r[0].startswith("Stated value") and r[1] == "0.00" for r in rows) == 4, rows
    A.emails = A.follows = A.referrals = 0
    _, note = run(A)
    assert note == "from the counts you gave", note
    A.follows = None
    _, note = run(A)
    assert "estimated" in note and "counts you gave" in note, note
    for field, bad in [("contestants", 0), ("contestants", -1), ("prize_cost", -1), ("shipping", float("nan")), ("value_per_email", float("inf")), ("emails", -1)]:
        previous = getattr(A, field); setattr(A, field, bad)
        try:
            run(A)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid ROI input accepted: " + field)
        setattr(A, field, previous)
    benchmark_self_test()
    print("self-test passed"); return 0

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--prize-cost", type=float, help="what the Prizes cost you"); ap.add_argument("--stated-value", type=float, help="retail value you advertise")
    ap.add_argument("--promotion", type=float, default=0); ap.add_argument("--admin", type=float, default=0); ap.add_argument("--shipping", type=float, default=0)
    ap.add_argument("--contestants", type=int, help="expected or actual unique Entrants"); ap.add_argument("--vertical", help="one of: " + ", ".join(BENCH["by_vertical"]))
    ap.add_argument("--emails", type=int); ap.add_argument("--follows", type=int); ap.add_argument("--referrals", type=int)
    ap.add_argument("--email-action", action="store_true", help="estimate emails from Contestants"); ap.add_argument("--follow-action", action="store_true"); ap.add_argument("--share-action", action="store_true")
    ap.add_argument("--value-per-email", type=float); ap.add_argument("--value-per-follow", type=float); ap.add_argument("--value-per-referral", type=float)
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    if not a.contestants or a.prize_cost is None: ap.error("--prize-cost and --contestants are required")
    try:
        rows, note = run(a)
    except ValueError as exc:
        ap.error(str(exc))
    print_table(rows, ("Metric", "This campaign", "Benchmark median", "Note")); print(); print("Counts", note + ".")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
