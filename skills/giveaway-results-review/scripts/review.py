#!/usr/bin/env python3
"""Derived metrics and benchmark position for one finished giveaway. No dependencies.

  python3 review.py --contestants 1800 --impressions 6000 --entries 9000 --invalid 400 --days 14 --methods 6 [--actions actions.csv]
  python3 review.py --self-test

Benchmarks are medians from the ordinary segment of the campaign export (37,180 campaigns that reached 1,000 unique
entrants), as published in references/benchmarks.md. Update both together. Impressions count one view per user per day,
so long runs and daily actions depress conversion without anything being wrong. The script says so when it applies.
"""
import argparse, csv, json, os, sys

BENCH = {
    "contestants": {"p25": 1415, "median": 2201, "p75": 4152, "p90": 9006},
    "entries_per_contestant": {"p25": 2.68, "median": 4.34, "p75": 7.07, "p90": 12.06},
    "impressions": {"p25": 4751, "median": 9073, "p75": 19661, "p90": 45590},
    "duration_days": {"p25": 8, "median": 16, "p75": 31, "p90": 43},
    "invalid_share": {"median": 0.038, "share_5pct_plus": 0.43, "share_20pct_plus": 0.07},
    "conv_by_methods": [(3, 0.50), (6, 0.37), (10, 0.33), (10 ** 9, 0.31)],       # clean subset
    "conv_by_duration": [(7, 0.45), (14, 0.31), (30, 0.28), (60, 0.24), (10 ** 9, 0.23)],  # no repeatable actions
    "platform_average_conversion": 0.34,
    "family_uptake": {"visit": 0.75, "follow": 0.47, "share": 0.22, "email": 0.89, "content": 0.24},
    "yield_median": {"email": {"1k-2.5k": 1346, "2.5k-10k": 3703, "10k+": 16344}, "share": {"1k-2.5k": 224, "2.5k-10k": 520, "10k+": 1643}},
}
FAMILY_WORDS = {"email": ("email", "newsletter", "subscribe to", "signup", "sign up"), "share": ("share", "refer", "retweet", "repost", "viral"),
                "content": ("upload", "submit", "photo", "video", "post a", "write", "comment"), "follow": ("follow", "subscribe", "join", "like"),
                "visit": ("visit", "view", "watch", "check out", "page")}

PCT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "percentiles.json")

def load_pct():
    try: return json.load(open(PCT_FILE))
    except (OSError, ValueError): return None

def rank(value, table, lower_is_better=False):
    """Share of campaigns in the group that this value beats, from the every-fifth-percentile table."""
    if not table or value is None: return None
    ps, vals = table_pcts, table["p"]
    beaten = sum(1 for v in vals if value > v) if not lower_is_better else sum(1 for v in vals if value < v)
    pct = ps[beaten - 1] if beaten else 0
    return pct, table["n"]

table_pcts = list(range(5, 100, 5))

def rank_line(metric, value, groups, lower_is_better=False):
    parts = []
    for label, key in groups:
        t = (PCT or {}).get("groups", {}).get(key, {}).get(metric)
        r = rank(value, t, lower_is_better)
        if r: parts.append(f"{'better' if not lower_is_better else 'lower'} than {r[0]}% of {label} (n={r[1]:,})")
    return "; ".join(parts) if False else ", ".join(parts)

PCT = None

def position(value, dist):
    if value < dist["p25"]: return "bottom quarter"
    if value < dist["median"]: return "below the median"
    if value < dist["p75"]: return "above the median"
    if value < dist["p90"]: return "top quarter"
    return "top tenth"

def band(c): return "10k+" if c >= 10000 else "2.5k-10k" if c >= 2500 else "1k-2.5k" if c >= 1000 else "under 1k (no peer group in the benchmarks)"

def lookup(table, x):
    for limit, v in table:
        if x <= limit: return v
    return table[-1][1]

def family(name):
    n = name.lower()
    for fam, words in FAMILY_WORDS.items():
        if any(w in n for w in words): return fam
    return None

def review(a):
    global PCT
    PCT = PCT or load_pct()
    groups = [("all campaigns", "all"), (f"the {band(a.contestants)} band", "band:" + band(a.contestants))]
    if getattr(a, "vertical", None): groups.append((a.vertical.replace("_", " ") + " campaigns", "vertical:" + a.vertical))
    conv_groups = [("all campaigns", "all"), ("clean campaigns", "clean")] + groups[2:]
    rows = []
    rows.append(("Unique contestants", f"{a.contestants:,}", f"{BENCH['contestants']['median']:,}", f"{position(a.contestants, BENCH['contestants'])}, band {band(a.contestants)}. " + rank_line("contestants", a.contestants, [g for g in groups if not g[1].startswith("band")])))
    if a.entries:
        epc = a.entries / a.contestants
        rows.append(("Entries per contestant", f"{epc:.2f}", f"{BENCH['entries_per_contestant']['median']}", position(epc, BENCH["entries_per_contestant"]) + ". Depends on entry worth, compare with care. " + rank_line("entries_per_entrant", epc, groups)))
    if a.impressions:
        conv = a.contestants / a.impressions
        rows.append(("Impressions", f"{a.impressions:,}", f"{BENCH['impressions']['median']:,}", position(a.impressions, BENCH["impressions"])))
        peer_m = lookup(BENCH["conv_by_methods"], a.methods) if a.methods else None
        peer_d = lookup(BENCH["conv_by_duration"], a.days) if a.days else None
        note = f"platform average {BENCH['platform_average_conversion']:.0%}"
        if peer_m: note += f", clean campaigns with {a.methods} actions {peer_m:.0%}"
        if peer_d: note += f", campaigns of {a.days} days {peer_d:.0%}"
        if a.repeatable or (a.days and a.days > 14): note += ". Impressions count once per user per day, so a long run or a daily action lowers this without anything being wrong"
        note += ". " + rank_line("conversion", conv, conv_groups)
        rows.append(("Contestants per impression", f"{conv:.1%}", f"{BENCH['platform_average_conversion']:.0%}", note))
    if a.invalid is not None and a.entries:
        inv = a.invalid / (a.entries + a.invalid)
        read = "below the median" if inv < BENCH["invalid_share"]["median"] else "above the median"
        if inv >= 0.2: read += f", in the top {BENCH['invalid_share']['share_20pct_plus']:.0%} of campaigns. Check for a validated-answer question, then referral and Discord actions"
        elif inv >= 0.05: read += f", like {BENCH['invalid_share']['share_5pct_plus']:.0%} of campaigns"
        read += ". " + rank_line("invalid_share", inv, groups, lower_is_better=True)
        rows.append(("Invalid share of entries", f"{inv:.1%}", f"{BENCH['invalid_share']['median']:.1%}", read))
    if getattr(a, "emails", None):
        up = a.emails / a.contestants
        rows.append(("Email signups", f"{a.emails:,}", f"{BENCH['yield_median']['email'][band(a.contestants)]:,}", rank_line("email_signups", a.emails, groups)))
        rows.append(("Email signups per contestant", f"{up:.2f}", f"{BENCH['family_uptake']['email']:.2f}", rank_line("email_uptake", up, groups)))
    if getattr(a, "referrals", None):
        rp = a.referrals / a.contestants
        rows.append(("Referral entries per contestant", f"{rp:.2f}", "0.13", rank_line("referrals_per_contestant", rp, groups)))
    if a.days:
        rows.append(("Duration in days", f"{a.days}", f"{BENCH['duration_days']['median']}", position(a.days, BENCH["duration_days"])))
    if a.methods:
        rows.append(("Entry actions", f"{a.methods}", "5", "11 or more lost a fifth of contestants in the clean subset" if a.methods >= 11 else "within the usual range"))
    return rows

def read_actions(path, contestants):
    out = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        rd = csv.reader(f); header = next(rd)
        for r in rd:
            if len(r) < 2: continue
            try: n = float(r[1].replace(",", ""))
            except ValueError: continue
            fam = family(r[0]); up = n / contestants
            bench = BENCH["family_uptake"].get(fam)
            read = (("at or above" if bench and up >= bench else "below") + " its family median") if bench else "no family benchmark"
            ym = BENCH["yield_median"].get(fam, {}).get(band(contestants))
            if ym: read += f", median campaign in this band collected {ym:,}"
            out.append((r[0], f"{up:.2f}", f"{bench:.2f}" if bench else "n/a", fam or "unclassified", read))
    return sorted(out, key=lambda x: -float(x[1]))

def print_table(rows, header):
    widths = [max(len(str(x)) for x in col) for col in zip(header, *rows)]
    for line in [header] + rows: print("  ".join(str(x).ljust(w) for x, w in zip(line, widths)))

def self_test():
    class A: contestants = 1800; impressions = 6000; entries = 9000; invalid = 400; days = 14; methods = 6; repeatable = False; vertical = "food_drink"; emails = 1500; referrals = 200
    rows = review(A); d = {r[0]: r for r in rows}
    assert "better than" in d["Unique contestants"][3] and "food drink campaigns" in d["Unique contestants"][3], rows
    assert "Email signups" in d and "better than" in d["Email signups"][3], rows
    assert "1k-2.5k" in d["Unique contestants"][3] and d["Entries per contestant"][1] == "5.00" and d["Contestants per impression"][1] == "30.0%", rows
    assert d["Invalid share of entries"][1] == "4.3%" and "above the median" in d["Invalid share of entries"][3]
    assert family("Subscribe to our newsletter") == "email" and family("Share on Facebook") == "share" and family("Visit our store") == "visit"
    print("self-test passed"); return 0

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true"); ap.add_argument("--contestants", type=int); ap.add_argument("--impressions", type=int)
    ap.add_argument("--entries", type=int); ap.add_argument("--invalid", type=int); ap.add_argument("--days", type=int); ap.add_argument("--methods", type=int)
    ap.add_argument("--repeatable", action="store_true", help="the campaign had a daily, loyalty or timed bonus action")
    ap.add_argument("--actions", help="CSV with action name and completions per row, header row first")
    ap.add_argument("--vertical", help="rank against one vertical too: gaming, technology, fashion_beauty, food_drink, home, fitness_outdoor, travel_events, kids_family_pets, software, music_media")
    ap.add_argument("--emails", type=int, help="email signups collected"); ap.add_argument("--referrals", type=int, help="referral entries recorded")
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    if not a.contestants: ap.error("--contestants is required")
    print_table(review(a), ("Metric", "This campaign", "Benchmark median", "Read"))
    if a.actions:
        print(); print_table(read_actions(a.actions, a.contestants), ("Action", "Per contestant", "Family median", "Family", "Read"))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
