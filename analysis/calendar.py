#!/usr/bin/env python3
"""The calendar against results, for every campaign whatever its theme: by ISO week of the start (launch volume,
contestants, clean conversion, entries per entrant), by start day of the month, and campaigns whose run spanned a holiday
against campaigns of the same length that did not. Writes analysis/output/calendar.json.

  python3 analysis/calendar.py export.json --classification private/classification.jsonl
"""
import argparse, collections, datetime as dt, json, os, statistics as st, importlib.util, sys

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("hol", os.path.join(here, "holidays.py")); hol = importlib.util.module_from_spec(spec); spec.loader.exec_module(hol)
REPEAT = {"loyalty", "timed_bonus"}
DATED = [(n, fn) for n, _, fn in hol.HOLIDAYS if fn and n != "Summer"] + [("Prime Day (mid July, varies)", lambda y: dt.date(y, 7, 12)), ("Cyber Monday", lambda y: hol.last_weekday(y, 11, 4) + dt.timedelta(days=3)),
                                                                       ("Singles Day", lambda y: dt.date(y, 11, 11)), ("Independence Day (US)", lambda y: dt.date(y, 7, 4)), ("Super Bowl (US)", lambda y: hol.nth_weekday(y, 2, 6, 2))]
def med(xs): xs = [x for x in xs if x is not None]; return st.median(xs) if xs else None
def prof(g):
    clean = [c for c in g if c["_clean"]]
    return {"n": len(g), "contestants": med([c["valid_contestants"] for c in g]), "conv_clean": med([c["_conv"] for c in clean]), "clean_n": len(clean), "entries_per_entrant": med([c["_epc"] for c in g]),
            "duration": med([c["duration_in_days"] for c in g]), "email_uptake": med([c["_email_up"] for c in g])}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("export"); ap.add_argument("--classification", required=True)
    ap.add_argument("--out", default=os.path.join(here, "output", "calendar.json"))
    a = ap.parse_args()
    seg = {}
    for l in open(a.classification):
        j = json.loads(l); seg[j["campaign_id"]] = j["segment"]
    d = json.load(open(a.export)); o = []
    for c in d:
        if seg.get(c["campaign_id"]) != "ordinary" or not c.get("valid_contestants") or not c.get("valid_entries") or not c.get("starts_at") or not c.get("ends_at"): continue
        ems = c["entry_methods"]
        c["_rep"] = any(e.get("entry_method_type") in REPEAT or (e.get("entry_method_type") == "custom_action" and e.get("entry_method_template") == "bonus") for e in ems)
        c["_clean"] = not c["_rep"] and c["duration_in_days"] <= 14
        c["_conv"] = c["valid_contestants"] / c["impressions"] if c.get("impressions") else None; c["_epc"] = c["valid_entries"] / c["valid_contestants"]
        em = [e for e in ems if e.get("entry_method_generic_name") in ("Email Subscriptions", "Gleam Subscriber") and e.get("entry_count") is not None]
        c["_email_up"] = sum(e["entry_count"] for e in em) / c["valid_contestants"] if em else None
        c["_start"] = dt.date.fromisoformat(c["starts_at"][:10]); c["_end"] = dt.date.fromisoformat(c["ends_at"][:10]); o.append(c)
    n_all = len(o); base = prof(o)
    # by ISO week of start
    byw = collections.defaultdict(list)
    for c in o: byw[c["_start"].isocalendar()[1]].append(c)
    weeks = {}
    for w in range(1, 54):
        g = byw.get(w, [])
        if len(g) >= 100: weeks[w] = dict(prof(g), share_of_starts=len(g) / n_all)
    # holidays that fall in each week (typical year 2026)
    week_holidays = collections.defaultdict(list)
    for name, fn in DATED:
        try: dd = fn(2026)
        except Exception: continue
        week_holidays[dd.isocalendar()[1]].append(name)
    # by start day of month
    bydom = collections.defaultdict(list)
    for c in o: bydom["1-7" if c["_start"].day <= 7 else "8-14" if c["_start"].day <= 14 else "15-21" if c["_start"].day <= 21 else "22-31"].append(c)
    # live over the holiday, matched on duration bucket
    def dbucket(x): return "1-7" if x <= 7 else "8-14" if x <= 14 else "15-30" if x <= 30 else "31+"
    spans = {}
    for name, fn in DATED:
        over, notover = [], []
        for c in o:
            hit = False
            for y in (c["_start"].year, c["_end"].year):
                try: h = fn(y)
                except Exception: continue
                if c["_start"] <= h <= c["_end"]: hit = True; break
            (over if hit else notover).append(c)
        if len(over) < 100: continue
        # weight the comparison group to the same duration mix
        mix = collections.Counter(dbucket(c["duration_in_days"]) for c in over)
        comp = []
        for b, k in mix.items():
            pool = [c for c in notover if dbucket(c["duration_in_days"]) == b]
            comp.extend(pool[: max(k, 0) * 5] if len(pool) > k * 5 else pool)
        po, pc = prof(over), prof(comp)
        spans[name] = {"over": po, "same_length_not_over": pc, "contestants_ratio": po["contestants"] / pc["contestants"] if pc["contestants"] else None,
                       "conv_ratio": (po["conv_clean"] / pc["conv_clean"]) if po["conv_clean"] and pc["conv_clean"] else None, "closed_on_holiday_share": None}
        # closing on the holiday itself, within the over group
        close_on = [c for c in over if any(c["_end"] == fn(y) for y in (c["_end"].year,) if True)]
        spans[name]["closed_on_holiday_n"] = len(close_on)
        spans[name]["closed_on_holiday_contestants"] = med([c["valid_contestants"] for c in close_on])
    out = {"ordinary_n": n_all, "all": base, "definitions": {"week": "ISO week of the start date, UTC", "conv_clean": "contestants per impression on campaigns with no repeatable action and 14 days or less",
                                                             "live_over": "start on or before the holiday date and end on or after it; the comparison group is drawn from campaigns not spanning it with the same duration mix",
                                                             "holiday dates": "2026 dates used to place holidays in weeks; live-over uses each campaign's own year"},
           "by_start_week": {str(w): dict(v, holidays=week_holidays.get(w, [])) for w, v in weeks.items()}, "by_start_day_of_month": {k: prof(v) for k, v in sorted(bydom.items())}, "live_over_holiday": spans}
    json.dump(out, open(a.out, "w"), indent=1); print("wrote", a.out)

if __name__ == "__main__":
    main()
