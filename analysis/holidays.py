#!/usr/bin/env python3
"""Holiday-themed campaigns: which holiday the title or description names, how many, contestants and conversion, and
when they launched relative to the holiday (lead days, median) and closed. Writes analysis/output/holidays.json.

  python3 analysis/holidays.py export.json --classification private/classification.jsonl
"""
import argparse, collections, datetime as dt, json, os, re, statistics as st

REPEAT = {"loyalty", "timed_bonus"}
def easter(y):
    a = y % 19; b = y // 100; c = y % 100; d = b // 4; e = b % 4; f = (b + 8) // 25; g = (b - f + 1) // 3; h = (19 * a + b - d - g + 15) % 30
    i = c // 4; k = c % 4; l = (32 + 2 * e + 2 * i - h - k) % 7; m = (a + 11 * h + 22 * l) // 451; mo = (h + l - 7 * m + 114) // 31; da = (h + l - 7 * m + 114) % 31 + 1
    return dt.date(y, mo, da)
def nth_weekday(y, m, weekday, n): d = dt.date(y, m, 1); d += dt.timedelta(days=(weekday - d.weekday()) % 7); return d + dt.timedelta(weeks=n - 1)
def last_weekday(y, m, weekday): d = dt.date(y + (m == 12), (m % 12) + 1, 1) - dt.timedelta(days=1); return d - dt.timedelta(days=(d.weekday() - weekday) % 7)
DIWALI = {2020: (11, 14), 2021: (11, 4), 2022: (10, 24), 2023: (11, 12), 2024: (11, 1), 2025: (10, 20), 2026: (11, 8)}
LNY = {2020: (1, 25), 2021: (2, 12), 2022: (2, 1), 2023: (1, 22), 2024: (2, 10), 2025: (1, 29), 2026: (2, 17)}
HOLIDAYS = [
    ("Christmas and advent", r"\b(christmas|xmas|advent|adventskalender|julkalender|joulukalenteri|noel|navidad|natal|12 days|holiday season|festive)\b", lambda y: dt.date(y, 12, 25)),
    ("New Year", r"\b(new year|nye|new years|año nuevo|silvester)\b", lambda y: dt.date(y + 1, 1, 1)),
    ("Black Friday and Cyber Monday", r"\b(black friday|cyber monday|bfcm)\b", lambda y: last_weekday(y, 11, 4)),
    ("Thanksgiving", r"\bthanksgiving\b", lambda y: nth_weekday(y, 11, 3, 4)),
    ("Halloween", r"\b(halloween|spooky|trick or treat)\b", lambda y: dt.date(y, 10, 31)),
    ("Valentine's Day", r"\b(valentine|valentines|san valent[ií]n)\b", lambda y: dt.date(y, 2, 14)),
    ("Mother's Day", r"\b(mother'?s day|mothers day|mum'?s day|mom'?s day|d[ií]a de la madre|muttertag|fête des mères)\b", lambda y: nth_weekday(y, 5, 6, 2)),
    ("Father's Day", r"\b(father'?s day|fathers day|dad'?s day|d[ií]a del padre|vatertag)\b", lambda y: nth_weekday(y, 6, 6, 3)),
    ("Easter", r"\b(easter|pascua|ostern|pâques)\b", easter),
    ("Back to school", r"\b(back to school|back-to-school|school year)\b", lambda y: dt.date(y, 8, 25)),
    ("Summer", r"\b(summer|verano|sommer|été)\b", lambda y: dt.date(y, 7, 1)),
    ("Diwali", r"\b(diwali|deepavali|dhanteras)\b", lambda y: dt.date(y, *DIWALI.get(y, (11, 1)))),
    ("Lunar New Year", r"\b(lunar new year|chinese new year|tet\b|seollal|year of the)\b", lambda y: dt.date(y, *LNY.get(y, (2, 1)))),
    ("Ramadan and Eid", r"\b(ramadan|eid|iftar)\b", None),
    ("Prime Day and Singles Day", r"\b(prime day|singles'? day|11\.11|double 11)\b", None),
    ("Anniversary or birthday", r"\b(anniversary|birthday|bday|turns \d+|years old)\b", None),
    ("Milestone", r"\b(\d+k|\d{2,3},000|million|milestone|subscribers|followers) (giveaway|celebration|special)\b|\b(hit|reached|celebrat\w+) \d", None)]

def med(xs): xs = [x for x in xs if x is not None]; return st.median(xs) if xs else None
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("export"); ap.add_argument("--classification", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "output", "holidays.json"))
    a = ap.parse_args()
    seg = {}
    for l in open(a.classification):
        j = json.loads(l); seg[j["campaign_id"]] = j["segment"]
    d = json.load(open(a.export)); o = []
    for c in d:
        if seg.get(c["campaign_id"]) != "ordinary" or not c.get("valid_contestants") or not c.get("valid_entries") or not c.get("starts_at"): continue
        ems = c["entry_methods"]
        c["_rep"] = any(e.get("entry_method_type") in REPEAT or (e.get("entry_method_type") == "custom_action" and e.get("entry_method_template") == "bonus") for e in ems)
        c["_conv"] = c["valid_contestants"] / c["impressions"] if c.get("impressions") else None; c["_epc"] = c["valid_entries"] / c["valid_contestants"]
        c["_txt"] = ((c.get("name") or "") + " " + (c.get("incentive_name") or "") + " " + re.sub("<[^>]+>", " ", c.get("incentive_desc") or "")[:400]).lower()
        c["_start"] = dt.date.fromisoformat(c["starts_at"][:10]); c["_end"] = dt.date.fromisoformat(c["ends_at"][:10]) if c.get("ends_at") else None
        o.append(c)
    allp = {"n": len(o), "contestants": med([c["valid_contestants"] for c in o]), "conv_clean": med([c["_conv"] for c in o if not c["_rep"] and c["duration_in_days"] <= 14]), "epc": med([c["_epc"] for c in o]), "duration": med([c["duration_in_days"] for c in o])}
    out = {"all_ordinary": allp, "holidays": {}, "definitions": {"match": "regex on title, incentive name and the first 400 characters of the description", "lead_days": "holiday date minus start date, median, for campaigns starting within 120 days before the holiday",
                                                             "clean": "conversion on campaigns with no repeatable action and 14 days or less"}}
    for name, pat, date_fn in HOLIDAYS:
        g = [c for c in o if re.search(pat, c["_txt"])]
        if len(g) < 30: continue
        clean = [c for c in g if not c["_rep"] and c["duration_in_days"] <= 14]
        row = {"n": len(g), "share_of_campaigns": len(g) / len(o), "contestants": med([c["valid_contestants"] for c in g]), "conv_clean": med([c["_conv"] for c in clean]), "clean_n": len(clean),
               "epc": med([c["_epc"] for c in g]), "duration": med([c["duration_in_days"] for c in g]), "repeatable_share": sum(c["_rep"] for c in g) / len(g),
               "start_months": dict(collections.Counter(c["_start"].strftime("%b") for c in g).most_common(4))}
        if date_fn:
            leads = []; closes = []
            for c in g:
                for y in (c["_start"].year, c["_start"].year + 1):
                    try: h = date_fn(y)
                    except Exception: continue
                    lead = (h - c["_start"]).days
                    if 0 <= lead <= 120: leads.append(lead); closes.append((c["_end"] - h).days if c["_end"] else None); break
            row["lead_days_median"] = med(leads); row["lead_days_p25"] = sorted(leads)[len(leads) // 4] if leads else None; row["lead_days_p75"] = sorted(leads)[3 * len(leads) // 4] if leads else None
            row["lead_n"] = len(leads); row["close_before_holiday_share"] = sum(1 for x in closes if x is not None and x <= 0) / len([x for x in closes if x is not None]) if any(x is not None for x in closes) else None
        out["holidays"][name] = row
    json.dump(out, open(a.out, "w"), indent=1); print("wrote", a.out)

if __name__ == "__main__":
    main()
