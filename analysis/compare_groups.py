#!/usr/bin/env python3
"""Descriptive group comparisons for the skill references. Writes analysis/output/comparisons.json.

  python3 analysis/compare_groups.py export.json --classification private/classification.jsonl

Impressions in the export are unique per day, so a returning visitor counts once per day. Repeatable actions
(daily bonus, loyalty, timed bonus) and long runs inflate impressions and depress contestants per impression.
Conversion comparisons therefore use a CLEAN subset: campaigns with no repeatable action and a run of 14 days
or less. Every figure is a median and describes what organizers chose. Every campaign passed the export floor.
Verticals are a regex proxy on organizer, campaign and prize names, so treat them as rough.
"""
import argparse, collections, datetime as dt, json, os, re, statistics as st

REPEAT = {"loyalty", "timed_bonus"}
VERTICALS = [("gaming_streaming", r"\b(twitch|stream|gaming|gamer|esport|steam|playstation|xbox|nintendo|rtx|gpu|pc build|gaming pc|game|games|skins?|discord)\b"),
    ("tech_phones_gadgets", r"\b(phone|smartphone|iphone|galaxy|xiaomi|redmi|oneplus|oppo|realme|laptop|tablet|earbuds|headphones|smartwatch|tech|gadget|android)\b"),
    ("beauty_fashion", r"\b(beauty|skincare|makeup|cosmetic|fashion|apparel|clothing|sneaker|jewel|hair|fragrance|dress|boutique)\b"),
    ("food_drink", r"\b(coffee|food|snack|restaurant|bakery|cafe|brew|beer|wine|whisky|tea|kitchen|recipe|chocolate|grill|bbq)\b"),
    ("home_garden", r"\b(home|garden|furniture|decor|mattress|appliance|vacuum|cleaning|candle|bedding)\b"),
    ("fitness_outdoor", r"\b(fitness|gym|workout|bike|cycling|fishing|hunting|camping|outdoor|golf|running|yoga|supplement)\b"),
    ("travel_events", r"\b(travel|trip|vacation|holiday|hotel|resort|cruise|flight|tickets?|concert|festival|tour)\b"),
    ("kids_family_pets", r"\b(baby|kids|toys?|lego|family|parent|pet|dog|cat)\b"),
    ("software_apps", r"\b(app|software|saas|subscription|plan|premium account|vpn|course|membership)\b"),
    ("auto_moto", r"\b(car|truck|motorcycle|auto|vehicle|ev\b|tyre|tire)\b"),
    ("music_media", r"\b(music|album|vinyl|guitar|podcast|book|novel|comic|film|movie|magazine)\b")]

def med(xs):
    xs = [x for x in xs if x is not None]; return st.median(xs) if xs else None

def stats(g):
    return {"n": len(g), "contestants": med([c["valid_contestants"] for c in g]), "entries_per_entrant": med([c["_epc"] for c in g]),
            "contestants_per_impression": med([c["_conv"] for c in g]), "impressions_per_contestant": med([c["_ipc"] for c in g]),
            "methods": med([c["_nm"] for c in g]), "share_with_repeatable": round(sum(c["_rep"] for c in g) / len(g), 3) if g else None}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("export"); ap.add_argument("--classification", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "output", "comparisons.json"))
    a = ap.parse_args()
    d = json.load(open(a.export)); seg = {}
    for l in open(a.classification):
        j = json.loads(l); seg[j["campaign_id"]] = j["segment"]
    allc = sorted([c for c in d if c.get("starts_at")], key=lambda c: c["starts_at"]); last = {}
    for c in allc:
        t = dt.datetime.fromisoformat(c["starts_at"].replace("Z", "+00:00")).timestamp()
        c["_gap"] = (t - last[c["site_id"]]) / 86400 if c["site_id"] in last else None; last[c["site_id"]] = t
    o = []
    for c in d:
        if seg.get(c["campaign_id"]) != "ordinary" or not c.get("valid_contestants") or not c.get("valid_entries"): continue
        ems = c.get("entry_methods") or []
        c["_rep"] = any(e.get("entry_method_type") in REPEAT or (e.get("entry_method_type") == "custom_action" and e.get("entry_method_template") == "bonus") for e in ems) or bool(re.search(r"\bdaily\b", c.get("name") or "", re.I))
        c["_nm"] = len(ems); c["_epc"] = c["valid_entries"] / c["valid_contestants"]
        c["_conv"] = c["valid_contestants"] / c["impressions"] if c.get("impressions") else None
        c["_ipc"] = c["impressions"] / c["valid_contestants"] if c.get("impressions") else None
        c["_types"] = {e.get("entry_method_type") for e in ems}
        txt = " ".join([c.get("site_name") or "", c.get("name") or "", c.get("incentive_name") or ""] + [p.get("name") or "" for p in c["prizes"]]).lower()
        c["_vert"] = next((v for v, pat in VERTICALS if re.search(pat, txt)), "unclassified")
        o.append(c)
    clean = [c for c in o if not c["_rep"] and c["duration_in_days"] <= 14]
    gapb = lambda c: "first campaign" if c["_gap"] is None else "previous within 30 days" if c["_gap"] <= 30 else "previous 31 to 90 days" if c["_gap"] <= 90 else "previous 91 to 365 days" if c["_gap"] <= 365 else "previous over a year"
    nmb = lambda c: "1 to 3" if c["_nm"] <= 3 else "4 to 6" if c["_nm"] <= 6 else "7 to 10" if c["_nm"] <= 10 else "11 or more"
    durb = lambda c: "1 to 7 days" if c["duration_in_days"] <= 7 else "8 to 14" if c["duration_in_days"] <= 14 else "15 to 30" if c["duration_in_days"] <= 30 else "31 to 60" if c["duration_in_days"] <= 60 else "61 or more"
    def grouped(pop, keyf, order):
        return {k: stats([c for c in pop if keyf(c) == k]) for k in order if any(keyf(c) == k for c in pop)}
    out = {"definitions": __doc__.strip(), "ordinary_n": len(o), "clean_n": len(clean), "share_with_repeatable_actions": round(sum(c["_rep"] for c in o) / len(o), 3),
        "repeatable_actions_all": grouped(o, lambda c: "has repeatable actions" if c["_rep"] else "no repeatable actions", ["no repeatable actions", "has repeatable actions"]),
        "duration_no_repeatable": grouped([c for c in o if not c["_rep"]], durb, ["1 to 7 days", "8 to 14", "15 to 30", "31 to 60", "61 or more"]),
        "method_count_clean": grouped(clean, nmb, ["1 to 3", "4 to 6", "7 to 10", "11 or more"]),
        "share_action_clean": grouped(clean, lambda c: "offers a share action" if "share_action" in c["_types"] else "no share action", ["no share action", "offers a share action"]),
        "email_clean": grouped(clean, lambda c: "offers email signup" if "email_subscribe" in c["_types"] else "no email signup", ["no email signup", "offers email signup"]),
        "recency_clean": grouped(clean, gapb, ["first campaign", "previous within 30 days", "previous 31 to 90 days", "previous 91 to 365 days", "previous over a year"]),
        "recency_all": grouped(o, gapb, ["first campaign", "previous within 30 days", "previous 31 to 90 days", "previous 91 to 365 days", "previous over a year"]),
        "weekday_all": grouped(o, lambda c: dt.datetime.fromisoformat(c["starts_at"].replace("Z", "+00:00")).strftime("%A"), ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]),
        "vertical_clean": grouped(clean, lambda c: c["_vert"], [v for v, _ in collections.Counter(c["_vert"] for c in o).most_common()]),
        "vertical_all": grouped(o, lambda c: c["_vert"], [v for v, _ in collections.Counter(c["_vert"] for c in o).most_common()])}
    rec = {}
    for v in out["vertical_clean"]:
        a_ = [c for c in clean if c["_vert"] == v and c["_gap"] is None]; b_ = [c for c in clean if c["_vert"] == v and c["_gap"] is not None and c["_gap"] <= 30]
        if len(a_) >= 30 and len(b_) >= 30: rec[v] = {"first_n": len(a_), "within30_n": len(b_), "contestants_rel": round(med([c["valid_contestants"] for c in b_]) / med([c["valid_contestants"] for c in a_]) - 1, 3), "conversion_rel": round(med([c["_conv"] for c in b_]) / med([c["_conv"] for c in a_]) - 1, 3)}
    out["recency_by_vertical_clean"] = rec
    os.makedirs(os.path.dirname(a.out), exist_ok=True); json.dump(out, open(a.out, "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k in ("ordinary_n", "clean_n", "share_with_repeatable_actions")}))

if __name__ == "__main__": main()
