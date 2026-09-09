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

def rank_line(metric, value, groups, lower_is_better=False, fmt="{:,.2f}"):
    parts = []; target = None
    for label, key in groups:
        t = (PCT or {}).get("groups", {}).get(key, {}).get(metric)
        r = rank(value, t, lower_is_better)
        if r: parts.append(f"{'better' if not lower_is_better else 'lower'} than {r[0]}% of {label} (n={r[1]:,})")
        if t and key.startswith("band") and not lower_is_better and value < t["p"][14]: target = (label, t["p"][14])
    line = ", ".join(parts)
    if target: line += f". Top quarter of {target[0]} reach " + fmt.format(target[1])
    return line

PCT = None

def median_of(metric, key="all"):
    t = (PCT or {}).get("groups", {}).get(key, {}).get(metric)
    return t["p"][9] if t else None

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
        rows.append(("Entries", f"{a.entries:,}", f"{median_of('entries') or 0:,.0f}", "depends on entry worth. " + rank_line("entries", a.entries, groups)))
        epc = a.entries / a.contestants
        rows.append(("Entries per contestant", f"{epc:.2f}", f"{BENCH['entries_per_contestant']['median']}", position(epc, BENCH["entries_per_contestant"]) + ". Depends on entry worth, compare with care. " + rank_line("entries_per_entrant", epc, groups)))
    if a.impressions:
        conv = a.contestants / a.impressions
        rows.append(("Impressions", f"{a.impressions:,}", f"{BENCH['impressions']['median']:,}", position(a.impressions, BENCH["impressions"]) + ". " + rank_line("impressions", a.impressions, groups)))
        peer_m = lookup(BENCH["conv_by_methods"], a.methods) if a.methods else None
        peer_d = lookup(BENCH["conv_by_duration"], a.days) if a.days else None
        note = f"platform average {BENCH['platform_average_conversion']:.0%}"
        if peer_m: note += f", clean campaigns with {a.methods} actions {peer_m:.0%}"
        if peer_d: note += f", campaigns of {a.days} days {peer_d:.0%}"
        if a.repeatable or (a.days and a.days > 14): note += ". Impressions count once per user per day, so a long run or a daily action lowers this without anything being wrong"
        note += ". " + rank_line("conversion", conv, conv_groups, fmt="{:.0%}")
        rows.append(("Contestants per impression", f"{conv:.1%}", f"{BENCH['platform_average_conversion']:.0%}", note))
    if a.invalid is not None and a.entries:
        inv = a.invalid / (a.entries + a.invalid)
        if inv >= 0.2: rows.append(("Invalid entries", f"{a.invalid:,}", "", "a fifth or more of entries failed verification. Check for a validated-answer question first, then referral and Discord actions"))
    if getattr(a, "actions_completed", None):
        apc = a.actions_completed / a.contestants
        rows.append(("Actions completed per contestant", f"{apc:.2f}", f"{median_of('actions_per_contestant') or 0:.2f}", "entry worth removed. " + rank_line("actions_per_contestant", apc, groups)))
    if a.days:
        pace = a.contestants / a.days
        rows.append(("Contestants per day", f"{pace:,.0f}", f"{median_of('contestants_per_day') or 0:,.0f}", rank_line("contestants_per_day", pace, groups)))
    if getattr(a, "prize_value", None):
        pv = a.prize_value / a.contestants
        rows.append(("Stated prize value per contestant", f"{pv:.2f}", f"{median_of('stated_usd_per_contestant') or 0:.2f}", "USD, stated value. " + rank_line("stated_usd_per_contestant", pv, groups).replace("better than", "higher than")))
    for flag, key, label in [("x_follows", "x_follows", "X follows"), ("instagram_follows", "instagram_follows", "Instagram follows"), ("tiktok_follows", "tiktok_follows", "TikTok follows"), ("twitch_follows", "twitch_follows", "Twitch follows"), ("youtube_subscribes", "youtube_subscribes", "YouTube subscribes"), ("discord_joins", "discord_joins", "Discord joins")]:
        val = getattr(a, flag, None)
        if val: rows.append((label, f"{val:,}", f"{median_of(key) or 0:,.0f}", rank_line(key, val, groups)))
    if getattr(a, "emails", None):
        up = a.emails / a.contestants
        rows.append(("Email signups", f"{a.emails:,}", f"{BENCH['yield_median']['email'][band(a.contestants)]:,}", rank_line("email_signups", a.emails, groups)))
        rows.append(("Email signups per contestant", f"{up:.2f}", f"{BENCH['family_uptake']['email']:.2f}", rank_line("email_uptake", up, groups)))
    if getattr(a, "referrals", None):
        rp = a.referrals / a.contestants
        rows.append(("Referral entries per contestant", f"{rp:.2f}", "0.13", rank_line("referrals_per_contestant", rp, groups)))
    if a.days:
        rows.append(("Duration in days", f"{a.days}", f"{BENCH['duration_days']['median']}", position(a.days, BENCH["duration_days"]) + ". " + rank_line("duration_days", a.days, groups).replace("better than", "longer than")))
    if a.methods:
        rows.append(("Entry actions", f"{a.methods}", "5", ("11 or more lost a fifth of contestants in the clean subset" if a.methods >= 11 else "within the usual range") + ". " + rank_line("methods", a.methods, groups).replace("better than", "more than")))
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
            gname = r[2].strip() if len(r) > 2 and r[2].strip() else r[0]
            t = (PCT or {}).get("per_action_uptake", {}).get(gname)
            rr = rank(up, t)
            if rr: read = f"better than {rr[0]}% of the {rr[1]:,} campaigns offering {gname}"
            ym = BENCH["yield_median"].get(fam, {}).get(band(contestants))
            if ym: read += f", median campaign in this band collected {ym:,}"
            out.append((r[0], f"{up:.2f}", f"{bench:.2f}" if bench else "n/a", fam or "unclassified", read))
    return sorted(out, key=lambda x: -float(x[1]))

HIST_COLS = ("campaign", "contestants", "impressions", "entries", "invalid", "days", "methods", "emails")

def read_history(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rd = csv.DictReader(f); rows = []
        for r in rd:
            row = {"campaign": r.get("campaign") or r.get("name") or f"campaign {len(rows) + 1}"}
            for k in HIST_COLS[1:]:
                try: row[k] = float(str(r.get(k, "")).replace(",", "")) if r.get(k, "") not in ("", None) else None
                except ValueError: row[k] = None
            rows.append(row)
    return rows

def history_table(a, hist):
    """This campaign beside the organizer's previous ones and their own median."""
    def metrics(c, i, e, inv, d):
        return {"contestants": c, "conversion": c / i if i else None, "entries_per_entrant": e / c if e and c else None,
                "invalid_share": inv / (e + inv) if e is not None and inv is not None and (e + inv) else None, "contestants_per_day": c / d if d else None}
    prev = [dict(h, **metrics(h["contestants"], h["impressions"], h["entries"], h["invalid"], h["days"])) for h in hist if h.get("contestants")]
    for h in prev: h["emails_val"] = h.get("emails")
    now = metrics(a.contestants, a.impressions, a.entries, a.invalid, a.days); now["emails"] = getattr(a, "emails", None)
    out = []
    for m, label, fmt in [("contestants", "Contestants", "{:,.0f}"), ("conversion", "Contestants per impression", "{:.1%}"), ("entries_per_entrant", "Entries per contestant", "{:.2f}"),
                          ("contestants_per_day", "Contestants per day", "{:,.0f}"), ("emails", "Email signups", "{:,.0f}")]:
        vals = [p.get(m) for p in prev if p.get(m) is not None]
        if now.get(m) is None or not vals: continue
        last = vals[-1]; med = sorted(vals)[len(vals) // 2]
        delta = (now[m] - last) / last if last else None
        out.append((label, fmt.format(now[m]), fmt.format(last), fmt.format(med), f"{delta:+.0%} against the previous" if delta is not None else "", f"{sum(1 for v in vals if now[m] > v)} of {len(vals)} previous beaten"))
    notes = []
    if prev and prev[-1]["contestants"] >= 5000: notes.append("After a campaign of 5,000 or more, the next one reached 5,000 in 57% of cases in the export")
    elif prev: notes.append("After a campaign under 5,000, the next one reached 5,000 in 11% of cases in the export, so a jump past it is unusual")
    return out, notes

def print_table(rows, header):
    widths = [max(len(str(x)) for x in col) for col in zip(header, *rows)]
    for line in [header] + rows: print("  ".join(str(x).ljust(w) for x, w in zip(line, widths)))

def self_test():
    class A: contestants = 1800; impressions = 6000; entries = 9000; invalid = 400; days = 14; methods = 6; repeatable = False; vertical = "food_drink"; emails = 1500; referrals = 200; actions_completed = 5400; prize_value = 1500; x_follows = 900
    rows = review(A); d = {r[0]: r for r in rows}
    assert "better than" in d["Unique contestants"][3] and "food drink campaigns" in d["Unique contestants"][3], rows
    assert "Email signups" in d and "better than" in d["Email signups"][3], rows
    assert d["Actions completed per contestant"][1] == "3.00" and "Contestants per day" in d and "Impressions" in d and "better than" in d["Impressions"][3], rows
    assert "X follows" in d and "better than" in d["X follows"][3] and "higher than" in d["Stated prize value per contestant"][3], rows
    hist = [{"campaign": "spring", "contestants": 1200, "impressions": 5000, "entries": 5000, "invalid": 100, "days": 10, "methods": 5, "emails": 900},
            {"campaign": "summer", "contestants": 1500, "impressions": 5500, "entries": 7000, "invalid": 200, "days": 14, "methods": 6, "emails": 1200}]
    ht, notes = history_table(A, hist); hd = {r[0]: r for r in ht}
    assert hd["Contestants"][4] == "+20% against the previous" and hd["Contestants"][5] == "2 of 2 previous beaten" and notes, ht
    assert "1k-2.5k" in d["Unique contestants"][3] and d["Entries per contestant"][1] == "5.00" and d["Contestants per impression"][1] == "30.0%", rows
    assert "Invalid share of entries" not in d and "Entries" in d and "better than" in d["Entries"][3]
    assert family("Subscribe to our newsletter") == "email" and family("Share on Facebook") == "share" and family("Visit our store") == "visit"
    print("self-test passed"); return 0

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true"); ap.add_argument("--contestants", type=int); ap.add_argument("--impressions", type=int)
    ap.add_argument("--entries", type=int); ap.add_argument("--invalid", type=int); ap.add_argument("--days", type=int); ap.add_argument("--methods", type=int)
    ap.add_argument("--repeatable", action="store_true", help="the campaign had a daily, loyalty or timed bonus action")
    ap.add_argument("--actions", help="CSV with action name and completions per row, header row first; an optional third column names the Gleam action type (gleam_export.py writes it)")
    ap.add_argument("--vertical", help="rank against one vertical too: gaming, technology, fashion_beauty, food_drink, home, fitness_outdoor, travel_events, kids_family_pets, software, music_media")
    ap.add_argument("--emails", type=int, help="email signups collected"); ap.add_argument("--referrals", type=int, help="referral entries recorded")
    ap.add_argument("--actions-completed", type=int, help="total actions completed across all entry methods (sum of the actions report)")
    ap.add_argument("--prize-value", type=float, help="stated prize pool in USD, to rank value per contestant")
    for flag, help_ in [("x-follows", "X follows gained"), ("instagram-follows", "Instagram follows gained"), ("tiktok-follows", "TikTok follows gained"), ("twitch-follows", "Twitch follows gained"), ("youtube-subscribes", "YouTube subscribes gained"), ("discord-joins", "Discord joins gained")]:
        ap.add_argument("--" + flag, type=int, help=help_)
    ap.add_argument("--history", help="CSV of the organizer's previous campaigns, oldest first: campaign,contestants,impressions,entries,invalid,days,methods,emails (missing cells allowed)")
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    if not a.contestants: ap.error("--contestants is required")
    print_table(review(a), ("Metric", "This campaign", "Benchmark median", "Read"))
    if a.actions:
        acts = read_actions(a.actions, a.contestants); print(); print_table(acts, ("Action", "Per contestant", "Family median", "Family", "Read"))
    if a.history:
        rows, notes = history_table(a, read_history(a.history)); print()
        print_table(rows, ("Metric", "This campaign", "Previous", "Your median", "Change", "Record")); [print(n) for n in notes]
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
