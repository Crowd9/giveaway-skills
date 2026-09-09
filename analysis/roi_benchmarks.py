#!/usr/bin/env python3
"""Cost benchmarks by vertical and by size band: stated USD prize pool per contestant, per email signup, per follow, per
referral entry, plus what the median campaign in each vertical produced. Verticals are a regex on organizer, campaign and
prize names, so rough. Writes analysis/output/roi_benchmarks.json.

  python3 analysis/roi_benchmarks.py export.json --classification private/classification.jsonl
"""
import argparse, collections, json, os, re, statistics as st

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
EMAIL = {"Email Subscriptions", "Gleam Subscriber"}
FOLLOW = {"X Follows", "Instagram Follows", "TikTok Follows", "Twitch Follows", "Facebook Likes", "YouTube Entries", "Pinterest Entries", "Bluesky Follows", "Threads Follows", "LinkedIn Follow", "Spotify follows", "Podcast Subscriptions", "Snapchat"}
JOIN = {"Chat Members", "Telegram Channel Members"}

def med(xs): xs = [x for x in xs if x is not None]; return st.median(xs) if xs else None
def band(n): return "10k+" if n >= 10000 else "2.5k-10k" if n >= 2500 else "1k-2.5k"

def profile(g):
    v = [c for c in g if c["_val"]]
    def per(key): return med([c["_val"] / c[key] for c in v if c[key]])
    return {"n": len(g), "valued_n": len(v), "contestants": med([c["valid_contestants"] for c in g]), "stated_pool_usd": med([c["_val"] for c in v]),
            "usd_per_contestant": per("valid_contestants"), "usd_per_email": per("_email"), "usd_per_follow": per("_follow"), "usd_per_join": per("_join"), "usd_per_referral_entry": per("_ref"),
            "emails_per_campaign": med([c["_email"] for c in g if c["_email"]]), "follows_per_campaign": med([c["_follow"] for c in g if c["_follow"]]),
            "referral_entries_per_campaign": med([c["_ref"] for c in g if c["_ref"]]), "actions": med([len(c["entry_methods"]) for c in g]), "duration_days": med([c["duration_in_days"] for c in g]),
            "contestants_per_impression": med([c["valid_contestants"] / c["impressions"] for c in g if c.get("impressions")]),
            "share_with_email_action": sum(1 for c in g if c["_email"]) / len(g) if g else None}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("export"); ap.add_argument("--classification", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "output", "roi_benchmarks.json"))
    a = ap.parse_args()
    seg = {}
    for l in open(a.classification):
        j = json.loads(l); seg[j["campaign_id"]] = j["segment"]
    d = json.load(open(a.export)); o = []
    for c in d:
        if seg.get(c["campaign_id"]) != "ordinary" or not c.get("valid_contestants") or not c.get("valid_entries"): continue
        usd = [(p.get("value") or 0) * (p.get("quantity") or 1) for p in c["prizes"] if (p.get("currency") or "").upper() == "USD" and p.get("value")]
        val = sum(usd) if usd and all((p.get("currency") or "").upper() == "USD" and p.get("value") for p in c["prizes"]) else None
        c["_val"] = val if val and 0 < val < 10 ** 7 else None
        c["_email"] = sum(e["entry_count"] for e in c["entry_methods"] if e.get("entry_method_generic_name") in EMAIL and e.get("entry_count")) or None
        c["_follow"] = sum(e["entry_count"] for e in c["entry_methods"] if e.get("entry_method_generic_name") in FOLLOW and e.get("entry_count")) or None
        c["_join"] = sum(e["entry_count"] for e in c["entry_methods"] if e.get("entry_method_generic_name") in JOIN and e.get("entry_count")) or None
        c["_ref"] = sum(e["entry_count"] for e in c["entry_methods"] if e.get("entry_method_generic_name") == "Viral Shares" and e.get("entry_count")) or None
        txt = " ".join([c.get("site_name") or "", c.get("name") or "", c.get("incentive_name") or ""] + [p.get("name") or "" for p in c["prizes"]]).lower()
        c["_vert"] = next((v for v, pat in VERTICALS if re.search(pat, txt)), "unclassified"); o.append(c)
    byv = collections.defaultdict(list); byb = collections.defaultdict(list); byy = collections.defaultdict(list)
    for c in o: byv[c["_vert"]].append(c); byb[band(c["valid_contestants"])].append(c); byy[c["starts_at"][:4]].append(c)
    out = {"definitions": {"stated_pool_usd": "sum of stated prize value times quantity, campaigns with every prize valued in USD; what the organizer wrote, not what they paid",
                           "usd_per_x": "stated pool divided by completions of that asset action, median across campaigns that had both", "vertical": "regex on organizer, campaign and prize names"},
           "ordinary_n": len(o), "all": profile(o), "by_band": {k: profile(v) for k, v in sorted(byb.items())},
           "by_vertical": {k: profile(v) for k, v in sorted(byv.items(), key=lambda kv: -len(kv[1]))},
           "by_start_year": {k: {"n": len(v), "contestants": med([c["valid_contestants"] for c in v]), "contestants_per_impression": med([c["valid_contestants"] / c["impressions"] for c in v if c.get("impressions")]),
                                 "actions": med([len(c["entry_methods"]) for c in v]), "stated_pool_usd": med([c["_val"] for c in v if c["_val"]])} for k, v in sorted(byy.items()) if len(v) >= 200}}
    json.dump(out, open(a.out, "w"), indent=1); print("wrote", a.out)

if __name__ == "__main__":
    main()
