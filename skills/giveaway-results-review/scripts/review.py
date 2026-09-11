#!/usr/bin/env python3
"""Derived metrics and benchmark position for one finished giveaway. No dependencies.

  python3 review.py --contestants 1800 --impressions 6000 --entries 9000 --invalid 400 --days 14 --methods 6 [--actions actions.csv]
  python3 review.py --self-test

Benchmarks are typical figures from the campaigns behind these numbers (116,499 campaigns that reached 100 unique
Entrants), as published in references/benchmarks.md. Update both together. Impressions count one look per person per day,
so long runs and daily actions pull down the Conversion Rate without anything being wrong. The script says so when it applies.

--invalid takes invalid Entries worth, the Entries column summed over rows whose status is Invalid, which is the unit
gleam_export.py writes into the command it prints. The invalid share is derived as invalid / (Entries + invalid).

Every campaign is ranked inside its own size band. The six bands run 100 to 250, 250 to 500, 500 to 1,000,
1,000 to 2,500, 2,500 to 10,000 and 10,000 or more Entrants, so a campaign is only ever compared with a group
it belongs to.
"""
import argparse, csv, json, os, sys

BENCH = {
    "contestants": {"p25": 225, "median": 492, "p75": 1293, "p90": 3349},
    "entries_per_contestant": {"p25": 2.74, "median": 4.39, "p75": 7.05, "p90": 11.84},
    "impressions": {"p25": 862, "median": 2033, "p75": 5608, "p90": 16452},
    "duration_days": {"p25": 7, "median": 14, "p75": 29, "p90": 36},
    "conv_by_methods": [(3, 0.44), (6, 0.35), (10, 0.29), (10 ** 9, 0.31)],       # the campaigns we can compare fairly
    "conv_by_duration": [(7, 0.40), (14, 0.29), (30, 0.26), (60, 0.23), (10 ** 9, 0.22)],  # no repeatable actions
    "platform_average_conversion": 0.27,
    # one campaign per business, 17,383 businesses, from organizer_history.json sequence_curve_all.
    # The all-campaign figures are campaign weighted, and 55% of campaigns come from 11% of businesses,
    # so a first campaign held against 492 is held against people who have run dozens.
    "first_campaign": {"contestants": 382, "conversion": 0.256, "entries_per_contestant": 3.68, "n": 17383},
    "family_uptake": {"visit": 0.78, "follow": 0.53, "share": 0.11, "email": 0.85, "content": 0.13},
    "yield_median": {"email": {"100-250": 157, "250-500": 353, "500-1k": 645, "1k-2.5k": 1346, "2.5k-10k": 3713, "10k+": 16566},
                     "share": {"100-250": 17, "250-500": 35, "500-1k": 84, "1k-2.5k": 218, "2.5k-10k": 515, "10k+": 1698}},
}
FAMILY_WORDS = {"email": ("email", "newsletter", "subscribe to", "signup", "sign up"), "share": ("share", "refer", "retweet", "repost", "viral"),
                "content": ("upload", "submit", "photo", "video", "post a", "write", "comment"), "follow": ("follow", "subscribe", "join", "like"),
                "visit": ("visit", "view", "watch", "check out", "page")}

PCT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "percentiles.json")

def load_pct():
    try: d = json.load(open(PCT_FILE))
    except (OSError, ValueError): return None
    if d.get("bench"):
        BENCH.update({k: v for k, v in d["bench"].items() if v is not None})
        for k in ("conv_by_methods", "conv_by_duration"): BENCH[k] = [(x[0], x[1]) for x in BENCH[k] if x[1] is not None]
    return d

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
        if r:
            word = "better" if not lower_is_better else "lower"
            parts.append(f"in the bottom 5% of {label} (across {r[1]:,} campaigns)" if r[0] == 0
                         else f"{word} than {r[0]}% of {label} (across {r[1]:,} campaigns)")
        if t and key.startswith("band") and not lower_is_better and value < t["p"][14]: target = (label, t["p"][14])
    line = ", ".join(parts)
    if target: line += f". The best quarter of {target[0]} reach " + fmt.format(target[1])
    return line

PCT = None

def median_of(metric, key="all"):
    t = (PCT or {}).get("groups", {}).get(key, {}).get(metric)
    return t["p"][9] if t else None

def typical(metric, contestants):
    """The column is headed 'Typical for campaigns your size', so it takes the size band's own median.
    It used to take the all-campaign median, which called a 3,400-Entrant campaign a top-tenth result
    against every campaign in the data and then printed its band's name beside the claim."""
    return median_of(metric, "band:" + band(contestants)) or median_of(metric)

def band_rank(metric, value, contestants, lower_is_better=False):
    """Where this sits inside its own band, in words, with the band's campaign count."""
    t = (PCT or {}).get("groups", {}).get("band:" + band(contestants), {}).get(metric)
    r = rank(value, t, lower_is_better)
    if not r:
        return None
    word = "lower" if lower_is_better else "better"
    return (f"in the bottom 5% of campaigns of {band_label(contestants)}" if r[0] == 0
            else f"{word} than {r[0]}% of campaigns of {band_label(contestants)}") + f" (across {r[1]:,} campaigns)"

def position(value, dist):
    # Ranked against every campaign, where the sentence beside it in the same cell ranks against the size band.
    # An answer read "top quarter" as the band's top quarter and printed a figure the band could not hold, so the
    # phrase now says which distribution it came from.
    if value < dist["p25"]: return "bottom quarter of all campaigns"
    if value < dist["median"]: return "below typical for all campaigns"
    if value == dist["median"]: return "typical for all campaigns"
    if value < dist["p75"]: return "above typical for all campaigns"
    if value < dist["p90"]: return "top quarter of all campaigns"
    return "top tenth of all campaigns"

def band(c): return "10k+" if c >= 10000 else "2.5k-10k" if c >= 2500 else "1k-2.5k" if c >= 1000 else "500-1k" if c >= 500 else "250-500" if c >= 250 else "100-250"

BAND_NAMES = {"10k+": "10,000 or more Entrants", "2.5k-10k": "2,500 to 10,000 Entrants", "1k-2.5k": "1,000 to 2,500 Entrants",
              "500-1k": "500 to 1,000 Entrants", "250-500": "250 to 500 Entrants", "100-250": "100 to 250 Entrants"}
def band_label(c): return BAND_NAMES.get(band(c), band(c))

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
    groups = [("all campaigns", "all"), (f"campaigns of {band_label(a.contestants)}", "band:" + band(a.contestants))]
    if getattr(a, "vertical", None): groups.append((a.vertical.replace("_", " ") + " campaigns", "vertical:" + a.vertical))
    conv_groups = [("all campaigns", "all"), ("the campaigns we can compare fairly", "clean")] + groups[2:]
    rows = []
    if getattr(a, "first_campaign", False):
        fc = BENCH["first_campaign"]
        rows.append(("Users", f"{a.contestants:,}", f"{fc['contestants']:,}",
                     f"against first campaigns, where the typical one drew {fc['contestants']:,} "
                     f"(one campaign each from {fc['n']:,} businesses). The all-campaign figure of "
                     f"{BENCH['contestants']['median']:,} counts every campaign, and most of those come from "
                     f"businesses on their eleventh or later. " + rank_line("contestants", a.contestants, groups)))
    else:
        rows.append(("Users", f"{a.contestants:,}", f"{typical('contestants', a.contestants):,.0f}", (band_rank("contestants", a.contestants, a.contestants) or position(a.contestants, BENCH["contestants"])) + ". " + rank_line("contestants", a.contestants, [g for g in groups if not g[1].startswith("band")])))
    if a.entries:
        rows.append(("Entries", f"{a.entries:,}", f"{typical('entries', a.contestants) or 0:,.0f}", "depends on entry worth. " + rank_line("entries", a.entries, groups)))
        epc = a.entries / a.contestants
        rows.append(("Entries per Entrant", f"{epc:.2f}", f"{typical('entries_per_entrant', a.contestants) or 0:,.2f}", position(epc, BENCH["entries_per_contestant"]) + ". Depends on entry worth, compare with care. " + rank_line("entries_per_entrant", epc, groups)))
    if a.impressions:
        conv = a.contestants / a.impressions
        rows.append(("Impressions", f"{a.impressions:,}", f"{typical('impressions', a.contestants) or 0:,.0f}", position(a.impressions, BENCH["impressions"]) + ". " + rank_line("impressions", a.impressions, groups)))
        peer_m = lookup(BENCH["conv_by_methods"], a.methods) if a.methods else None
        peer_d = lookup(BENCH["conv_by_duration"], a.days) if a.days else None
        note = f"platform average {BENCH['platform_average_conversion']:.0%}"
        if peer_m: note += f", the campaigns we can compare fairly with {a.methods} actions {peer_m:.0%}"
        if peer_d: note += f", campaigns of {a.days} days {peer_d:.0%}"
        if a.repeatable or (a.days and a.days > 14): note += ". Impressions count once per person per day, so a long run or a daily action lowers this without anything being wrong"
        note += ". " + rank_line("conversion", conv, conv_groups, fmt="{:.0%}")
        rows.append(("Conversion Rate", f"{conv:.1%}", f"{BENCH['platform_average_conversion']:.0%}", note))
    if a.invalid is not None and a.entries:
        inv = a.invalid / (a.entries + a.invalid)
        if inv >= 0.2: rows.append(("Invalid Entries", f"{a.invalid:,}", "", "a fifth or more of Entries failed verification. Check for a validated-answer question first, then referral and Discord actions"))
    if getattr(a, "actions_completed", None):
        apc = a.actions_completed / a.contestants
        rows.append(("Actions completed per Entrant", f"{apc:.2f}", f"{typical('actions_per_contestant', a.contestants) or 0:.2f}", "entry worth removed. " + rank_line("actions_per_contestant", apc, groups)))
    if a.days:
        pace = a.contestants / a.days
        rows.append(("Entrants per day", f"{pace:,.0f}", f"{typical('contestants_per_day', a.contestants) or 0:,.0f}", rank_line("contestants_per_day", pace, groups)))
    if getattr(a, "prize_value", None):
        pv = a.prize_value / a.contestants
        rows.append(("Stated Prize value per Entrant", f"{pv:.2f}", f"{typical('stated_usd_per_contestant', a.contestants) or 0:.2f}", "USD, stated value. " + rank_line("stated_usd_per_contestant", pv, groups).replace("better than", "higher than")))
    for flag, key, label in [("x_follows", "x_follows", "X follows"), ("instagram_follows", "instagram_follows", "Instagram follows"), ("tiktok_follows", "tiktok_follows", "TikTok follows"), ("twitch_follows", "twitch_follows", "Twitch follows"), ("youtube_subscribes", "youtube_subscribes", "YouTube subscribes"), ("discord_joins", "discord_joins", "Discord joins")]:
        val = getattr(a, flag, None)
        if val: rows.append((label, f"{val:,}", f"{typical(key, a.contestants) or 0:,.0f}", rank_line(key, val, groups)))
    if getattr(a, "emails", None):
        up = a.emails / a.contestants
        rows.append(("Email signups", f"{a.emails:,}", f"{BENCH['yield_median']['email'][band(a.contestants)]:,}", rank_line("email_signups", a.emails, groups)))
        rows.append(("Email signups per Entrant", f"{up:.2f}", f"{BENCH['family_uptake']['email']:.2f}", rank_line("email_uptake", up, groups)))
    if getattr(a, "referrals", None):
        rp = a.referrals / a.contestants
        rows.append(("Referral Entries per Entrant", f"{rp:.2f}", "0.13", rank_line("referrals_per_contestant", rp, groups)))
    if a.days:
        rows.append(("Duration in days", f"{a.days}", f"{typical('duration_days', a.contestants) or 0:,.0f}", position(a.days, BENCH["duration_days"]) + ". " + rank_line("duration_days", a.days, groups).replace("better than", "longer than")))
    if a.methods:
        rows.append(("Entry actions", f"{a.methods}", "5", ("11 or more is more than most campaigns carry, and the campaigns that did drew a lower share of viewers through. Read the entry-method planner's friction section before adding another" if a.methods >= 11 else "within the usual range") + ". " + rank_line("methods", a.methods, groups).replace("better than", "more than")))
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
            read = (("at or above" if bench and up >= bench else "below") + " what's typical for that kind of action") if bench else "no matching group to compare against"
            gname = r[2].strip() if len(r) > 2 and r[2].strip() else r[0]
            t = (PCT or {}).get("per_action_uptake", {}).get(gname)
            rr = rank(up, t)
            if rr: read = f"better than {rr[0]}% of the {rr[1]:,} campaigns offering {gname}"
            ym = BENCH["yield_median"].get(fam, {}).get(band(contestants))
            if ym: read += f", a typical campaign of {band_label(contestants)} collected {ym:,}"
            out.append((r[0], f"{up:.2f}", f"{bench:.2f}" if bench else "n/a", fam or "unclassified", read))
    return sorted(out, key=lambda x: -float(x[1]))

HIST_COLS = ("campaign", "contestants", "impressions", "entries", "invalid", "days", "methods", "emails")

def read_history(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rd = csv.DictReader(f); rows = []
        for r in rd:
            # Gleam writes its headers with capitals, a hand-made file usually does not, so read either
            r = {(k or "").strip().lower(): v for k, v in r.items()}
            row = {"campaign": r.get("campaign") or r.get("name") or f"campaign {len(rows) + 1}"}
            for k in HIST_COLS[1:]:
                try: row[k] = float(str(r.get(k, "")).replace(",", "")) if r.get(k, "") not in ("", None) else None
                except ValueError: row[k] = None
            rows.append(row)
    return rows

def history_table(a, hist):
    """This campaign beside the organizer's previous ones and their own typical figure."""
    def metrics(c, i, e, inv, d):
        return {"contestants": c, "conversion": c / i if i else None, "entries_per_entrant": e / c if e and c else None,
                "invalid_share": inv / (e + inv) if e is not None and inv is not None and (e + inv) else None, "contestants_per_day": c / d if d else None}
    prev = [dict(h, **metrics(h["contestants"], h["impressions"], h["entries"], h["invalid"], h["days"])) for h in hist if h.get("contestants")]
    for h in prev: h["emails_val"] = h.get("emails")
    now = metrics(a.contestants, a.impressions, a.entries, a.invalid, a.days); now["emails"] = getattr(a, "emails", None)
    out = []
    for m, label, fmt in [("contestants", "Users", "{:,.0f}"), ("conversion", "Conversion Rate", "{:.1%}"), ("entries_per_entrant", "Entries per Entrant", "{:.2f}"),
                          ("contestants_per_day", "Entrants per day", "{:,.0f}"), ("emails", "Email signups", "{:,.0f}")]:
        vals = [p.get(m) for p in prev if p.get(m) is not None]
        if now.get(m) is None or not vals: continue
        last = vals[-1]; med = sorted(vals)[len(vals) // 2]
        delta = (now[m] - last) / last if last else None
        out.append((label, fmt.format(now[m]), fmt.format(last), fmt.format(med), f"{delta:+.0%} against the previous" if delta is not None else "", f"{sum(1 for v in vals if now[m] > v)} of {len(vals)} previous beaten"))
    notes = []
    if prev and prev[-1]["contestants"] >= 5000: notes.append("After a campaign of 5,000 or more, the next one reached 5,000 in 57% of cases in the dataset")
    elif prev: notes.append("After a campaign under 5,000, the next one reached 5,000 in 11% of cases in the dataset, so a jump past it is unusual")
    return out, notes

def print_table(rows, header):
    widths = [max(len(str(x)) for x in col) for col in zip(header, *rows)]
    for line in [header] + rows: print("  ".join(str(x).ljust(w) for x, w in zip(line, widths)))

def plain_reading(rows):
    """Entries per Entrant is a count, never a share, because one person can hold many Entries. So the plain reading
    says how many each person took, and how that sits against a typical campaign of this size. A share of Entrants is
    written as a percentage elsewhere. Turning a count into a percentage produces nonsense like 250 per 100."""
    row = next((r for r in rows if r[0] == "Entries per Entrant"), None)
    if not row: return ""
    try:
        this_v, bench_v = float(row[1]), float(row[2])
    except ValueError:
        return ""
    diff = f", about {abs(this_v - bench_v) / bench_v:.0%} {'above' if this_v > bench_v else 'below'} typical" if bench_v else ""
    return f"\nEach person took about {this_v:.1f} Entries, against about {bench_v:.1f} for campaigns this size{diff}."

def self_test():
    class A: contestants = 1800; impressions = 6000; entries = 9000; invalid = 400; days = 14; methods = 6; repeatable = False; vertical = "food_drink"; emails = 1500; referrals = 200; actions_completed = 5400; prize_value = 1500; x_follows = 900
    rows = review(A); d = {r[0]: r for r in rows}
    assert "better than" in d["Users"][3] and "food drink campaigns" in d["Users"][3], rows
    assert "Email signups" in d and "better than" in d["Email signups"][3], rows
    assert d["Actions completed per Entrant"][1] == "3.00" and "Entrants per day" in d and "Impressions" in d and "better than" in d["Impressions"][3], rows
    assert "X follows" in d and "better than" in d["X follows"][3] and "higher than" in d["Stated Prize value per Entrant"][3], rows
    assert d["Conversion Rate"][2] == "27%", rows
    hist = [{"campaign": "spring", "contestants": 1200, "impressions": 5000, "entries": 5000, "invalid": 100, "days": 10, "methods": 5, "emails": 900},
            {"campaign": "summer", "contestants": 1500, "impressions": 5500, "entries": 7000, "invalid": 200, "days": 14, "methods": 6, "emails": 1200}]
    ht, notes = history_table(A, hist); hd = {r[0]: r for r in ht}
    assert hd["Users"][4] == "+20% against the previous" and hd["Users"][5] == "2 of 2 previous beaten" and notes, ht
    assert "1,000 to 2,500 Entrants" in d["Users"][3] and d["Entries per Entrant"][1] == "5.00" and d["Conversion Rate"][1] == "30.0%", rows
    assert "Invalid share of Entries" not in d and "Entries" in d and "better than" in d["Entries"][3]
    import tempfile, os
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, newline="") as fh:
        fh.write("campaign,Contestants,Impressions,Entries,invalid,days,methods,emails\nspring,1200,5000,5000,100,10,5,900\n")
    assert read_history(fh.name)[0]["contestants"] == 1200, "the help text's capitalised headers must parse"
    os.unlink(fh.name)
    assert family("Subscribe to our newsletter") == "email" and family("Share on Facebook") == "share" and family("Visit our store") == "visit"
    class Small: contestants = 300; impressions = 1000; entries = 1200; invalid = None; days = 9; methods = 6; repeatable = False; vertical = None
    srows = review(Small); sd = {r[0]: r for r in srows}
    assert sd["Users"][1] == "300" and "250 to 500 Entrants" in sd["Users"][3], srows
    assert "Conversion Rate" in sd and "better than" in sd["Conversion Rate"][3], srows
    assert plain_reading(rows) == "\nEach person took about 5.0 Entries, against about 4.3 for campaigns this size, about 16% above typical.", plain_reading(rows)
    assert plain_reading(srows) == "\nEach person took about 4.0 Entries, against about 4.6 for campaigns this size, about 13% below typical.", plain_reading(srows)
    # the column says "for campaigns your size", so the two sizes must not be handed the same figure
    assert d["Entries per Entrant"][2] != sd["Entries per Entrant"][2], "a band typical that does not move with the band is the all-campaign median wearing the band's name"
    assert d["Users"][2] == "1,484" and sd["Users"][2] == "352", (d["Users"][2], sd["Users"][2])
    assert "campaigns of 1,000 to 2,500 Entrants" in d["Users"][3] and "campaigns of 250 to 500 Entrants" in sd["Users"][3], "the rank must be taken inside the band it names"
    # a first campaign must be held against first campaigns, never against the campaign-weighted figure
    class First: contestants = 400; impressions = 1400; entries = 1500; invalid = None; days = 12
    First.methods = 5; First.repeatable = False; First.vertical = None; First.first_campaign = True
    fd = {r[0]: r for r in review(First)}
    assert fd["Users"][2] == "382", fd["Users"]
    assert "first campaigns" in fd["Users"][3], fd["Users"]
    First.first_campaign = False
    assert {r[0]: r for r in review(First)}["Users"][2] != "382", "the flag must change the comparison"
    print("self-test passed"); return 0

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true"); ap.add_argument("--contestants", type=int); ap.add_argument("--impressions", type=int)
    ap.add_argument("--entries", type=int); ap.add_argument("--invalid", type=int, help="invalid Entries worth (the Entries column summed over invalid rows), never a count of rows"); ap.add_argument("--days", type=int); ap.add_argument("--methods", type=int)
    ap.add_argument("--repeatable", action="store_true", help="the campaign had a daily, loyalty or timed bonus action")
    ap.add_argument("--actions", help="CSV with action name and completions per row, header row first; an optional third column names the Gleam action type (gleam_export.py writes it)")
    ap.add_argument("--vertical", help="rank against one vertical too: gaming, technology, fashion_beauty, food_drink, home, fitness_outdoor, travel_events, kids_family_pets, software, music_media")
    ap.add_argument("--emails", type=int, help="email signups collected"); ap.add_argument("--referrals", type=int, help="referral Entries recorded")
    ap.add_argument("--actions-completed", type=int, help="total actions completed across all entry methods (sum of the actions report)")
    ap.add_argument("--prize-value", type=float, help="stated Prize pool in USD, to rank value per Entrant")
    for flag, help_ in [("x-follows", "X follows gained"), ("instagram-follows", "Instagram follows gained"), ("tiktok-follows", "TikTok follows gained"), ("twitch-follows", "Twitch follows gained"), ("youtube-subscribes", "YouTube subscribes gained"), ("discord-joins", "Discord joins gained")]:
        ap.add_argument("--" + flag, type=int, help=help_)
    ap.add_argument("--first-campaign", action="store_true",
                    help="this is the business's first campaign, so compare it with first campaigns (382 Entrants) "
                         "and not the campaign-weighted 492, which is mostly businesses on their eleventh or later")
    ap.add_argument("--history", help="CSV of the organizer's previous campaigns, oldest first: campaign,Contestants,Impressions,Entries,invalid,days,methods,emails (missing cells allowed)")
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    if not a.contestants: ap.error("--contestants is required")
    rows = review(a)
    print_table(rows, ("Metric", "This campaign", "Typical for campaigns your size", "Read"))
    print(plain_reading(rows))
    if a.actions:
        acts = read_actions(a.actions, a.contestants); print(); print_table(acts, ("Action", "Per Entrant", "Typical for that action", "Family", "Read"))
    if a.history:
        rows, notes = history_table(a, read_history(a.history)); print()
        print_table(rows, ("Metric", "This campaign", "Previous", "Your typical", "Change", "Record")); [print(n) for n in notes]
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
