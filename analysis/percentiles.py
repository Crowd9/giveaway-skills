#!/usr/bin/env python3
"""Percentile tables for the results-review skill: every fifth percentile of contestants, contestants per impression,
entries per entrant, invalid share, email signups, email uptake and referral entries per contestant, for all ordinary
campaigns, the clean subset, each size band and each vertical. Writes analysis/output/percentiles.json and a copy the
skill ships in skills/giveaway-results-review/references/percentiles.json. No customer fields.

  python3 analysis/percentiles.py export.json --classification private/classification.jsonl
"""
import argparse, json, os, re

VERTICALS = [("gaming", r"\b(twitch|stream|gaming|gamer|esport|steam|playstation|xbox|nintendo|rtx|gpu|pc build|gaming pc|game|games|skins?|discord)\b"),
    ("technology", r"\b(phone|smartphone|iphone|galaxy|xiaomi|redmi|oneplus|oppo|realme|laptop|tablet|earbuds|headphones|smartwatch|tech|gadget|android)\b"),
    ("fashion_beauty", r"\b(beauty|skincare|makeup|cosmetic|fashion|apparel|clothing|sneaker|jewel|hair|fragrance|dress|boutique)\b"),
    ("food_drink", r"\b(coffee|food|snack|restaurant|bakery|cafe|brew|beer|wine|whisky|tea|kitchen|recipe|chocolate|grill|bbq)\b"),
    ("home", r"\b(home|garden|furniture|decor|mattress|appliance|vacuum|cleaning|candle|bedding)\b"),
    ("fitness_outdoor", r"\b(fitness|gym|workout|bike|cycling|fishing|hunting|camping|outdoor|golf|running|yoga|supplement)\b"),
    ("travel_events", r"\b(travel|trip|vacation|holiday|hotel|resort|cruise|flight|tickets?|concert|festival|tour)\b"),
    ("kids_family_pets", r"\b(baby|kids|toys?|lego|family|parent|pet|dog|cat)\b"),
    ("software", r"\b(app|software|saas|subscription|plan|premium account|vpn|course|membership)\b"),
    ("music_media", r"\b(music|album|vinyl|guitar|podcast|book|novel|comic|film|movie|magazine)\b")]
REPEAT = {"loyalty", "timed_bonus"}; EMAIL = {"Email Subscriptions", "Gleam Subscriber"}
PCTS = list(range(5, 100, 5))

def pct(xs):
    xs = sorted(x for x in xs if x is not None)
    if len(xs) < 50: return None
    return {"n": len(xs), "p": [round(xs[int(p / 100 * (len(xs) - 1))], 4) for p in PCTS]}

def band(n): return "10k+" if n >= 10000 else "2.5k-10k" if n >= 2500 else "1k-2.5k"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("export"); ap.add_argument("--classification", required=True)
    a = ap.parse_args()
    seg = {}
    for l in open(a.classification):
        j = json.loads(l); seg[j["campaign_id"]] = j["segment"]
    d = json.load(open(a.export)); o = []
    for c in d:
        if seg.get(c["campaign_id"]) != "ordinary" or not c.get("valid_contestants") or not c.get("valid_entries"): continue
        ems = c["entry_methods"]; inv = c.get("invalid_entries") or 0
        em = sum(e["entry_count"] for e in ems if e.get("entry_method_generic_name") in EMAIL and e.get("entry_count"))
        rf = sum(e["entry_count"] for e in ems if e.get("entry_method_generic_name") == "Viral Shares" and e.get("entry_count"))
        txt = " ".join([c.get("site_name") or "", c.get("name") or "", c.get("incentive_name") or ""] + [p.get("name") or "" for p in c["prizes"]]).lower()
        o.append({"contestants": c["valid_contestants"], "conversion": c["valid_contestants"] / c["impressions"] if c.get("impressions") else None,
                  "entries_per_entrant": c["valid_entries"] / c["valid_contestants"], "invalid_share": inv / (c["valid_entries"] + inv),
                  "email_signups": em or None, "email_uptake": em / c["valid_contestants"] if em else None, "referrals_per_contestant": rf / c["valid_contestants"] if rf else None,
                  "clean": not any(e.get("entry_method_type") in REPEAT or (e.get("entry_method_type") == "custom_action" and e.get("entry_method_template") == "bonus") for e in ems) and c["duration_in_days"] <= 14,
                  "band": band(c["valid_contestants"]), "vertical": next((v for v, pat in VERTICALS if re.search(pat, txt)), "unclassified")})
    METRICS = ["contestants", "conversion", "entries_per_entrant", "invalid_share", "email_signups", "email_uptake", "referrals_per_contestant"]
    def table(g): return {m: pct([c[m] for c in g]) for m in METRICS}
    out = {"percentiles": PCTS, "definitions": {"conversion": "contestants per impression, all campaigns; the clean group has no repeatable action and 14 days or less",
                                                "email_signups": "campaigns with an email action", "vertical": "regex on organizer, campaign and prize names"},
           "groups": {"all": table(o), "clean": table([c for c in o if c["clean"]])}}
    for b in ["1k-2.5k", "2.5k-10k", "10k+"]: out["groups"]["band:" + b] = table([c for c in o if c["band"] == b])
    for v, _ in VERTICALS: out["groups"]["vertical:" + v] = table([c for c in o if c["vertical"] == v])
    out["groups"] = {k: {m: t for m, t in v.items() if t} for k, v in out["groups"].items()}
    here = os.path.dirname(__file__)
    for p in [os.path.join(here, "output", "percentiles.json"), os.path.join(here, "..", "skills", "giveaway-results-review", "references", "percentiles.json")]:
        json.dump(out, open(p, "w"), separators=(",", ":")); print("wrote", p)

if __name__ == "__main__":
    main()
