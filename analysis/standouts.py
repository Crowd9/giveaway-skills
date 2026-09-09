#!/usr/bin/env python3
"""Launch, pre-order and limited-drop subtypes; campaigns that outperformed their prize money (value index) and what
they had in common; and industries by how well giveaways work for them (value index, conversion, email and referral
uptake, repeat organizers). Writes analysis/output/standouts.json. Aggregates only.

  python3 analysis/standouts.py export.json --classification private/classification.jsonl
"""
import argparse, collections, json, os, re, statistics as st

REPEAT = {"loyalty", "timed_bonus"}
VERTICALS = [("gaming", r"\b(twitch|stream|gaming|gamer|esport|steam|playstation|xbox|nintendo|rtx|gpu|pc build|gaming pc|game|games|skins?|discord)\b"),
    ("technology", r"\b(phone|smartphone|iphone|galaxy|xiaomi|redmi|oneplus|oppo|realme|laptop|tablet|earbuds|headphones|smartwatch|tech|gadget|android)\b"),
    ("fashion_beauty", r"\b(beauty|skincare|makeup|cosmetic|fashion|apparel|clothing|sneaker|jewel|hair|fragrance|dress|boutique)\b"),
    ("food_drink", r"\b(coffee|food|snack|restaurant|bakery|cafe|brew|beer|wine|whisky|tea|kitchen|recipe|chocolate|grill|bbq)\b"),
    ("home", r"\b(home|garden|furniture|decor|mattress|appliance|vacuum|cleaning|candle|bedding)\b"),
    ("fitness_outdoor", r"\b(fitness|gym|workout|bike|cycling|fishing|hunting|camping|outdoor|golf|running|yoga|supplement)\b"),
    ("travel_events", r"\b(travel|trip|vacation|holiday|hotel|resort|cruise|flight|tickets?|concert|festival|tour)\b"),
    ("kids_family_pets", r"\b(baby|kids|toys?|lego|family|parent|pet|dog|cat)\b"),
    ("software", r"\b(app|software|saas|subscription|plan|premium account|vpn|course|membership)\b"),
    ("music_media", r"\b(music|album|vinyl|guitar|podcast|book|novel|comic|film|movie|magazine)\b"),
    ("auto", r"\b(car|truck|motorcycle|auto|vehicle|ev\b|tyre|tire)\b"), ("finance_crypto_adjacent", r"\b(bank|trading|invest|broker|finance|loan)\b")]
LAUNCH = [("Pre-order or crowdfunding", r"\b(pre-?order|kickstarter|indiegogo|crowdfund|backer)\b"), ("Limited edition or drop", r"\b(limited edition|limited run|drop\b|exclusive release|only \d+ made|numbered)\b"),
          ("Early access, beta or waitlist", r"\b(early access|beta|waitlist|wait list|founders?)\b"), ("Launch or new release", r"\b(launch|now available|new release|just dropped|introducing|new collection|new product)\b"),
          ("Restock or back in stock", r"\b(restock|back in stock)\b")]
VB = [(50, "under 50"), (100, "50-99"), (250, "100-249"), (500, "250-499"), (1000, "500-999"), (2500, "1000-2499"), (5000, "2500-4999"), (10000, "5000-9999"), (25000, "10000-24999"), (50000, "25000-49999"), (10 ** 12, "50000+")]
def vband(v): return next(n for l, n in VB if v < l)
def med(xs): xs = [x for x in xs if x is not None]; return st.median(xs) if xs else None

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("export"); ap.add_argument("--classification", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "output", "standouts.json"))
    a = ap.parse_args()
    cl = {}
    for l in open(a.classification):
        j = json.loads(l); cl[j["campaign_id"]] = j
    d = json.load(open(a.export)); o = []; site_counts = collections.Counter()
    for c in d:
        j = cl.get(c["campaign_id"])
        if not j or j["segment"] != "ordinary" or not c.get("valid_contestants") or not c.get("valid_entries"): continue
        site_counts[c["site_id"]] += 1
        ems = c["entry_methods"]
        c["_rep"] = any(e.get("entry_method_type") in REPEAT or (e.get("entry_method_type") == "custom_action" and e.get("entry_method_template") == "bonus") for e in ems)
        c["_clean"] = not c["_rep"] and c["duration_in_days"] <= 14
        c["_conv"] = c["valid_contestants"] / c["impressions"] if c.get("impressions") else None; c["_epc"] = c["valid_entries"] / c["valid_contestants"]
        em = [e for e in ems if e.get("entry_method_generic_name") in ("Email Subscriptions", "Gleam Subscriber") and e.get("entry_count") is not None]
        c["_email_up"] = sum(e["entry_count"] for e in em) / c["valid_contestants"] if em else None
        vs = [e for e in ems if e.get("entry_method_generic_name") == "Viral Shares" and e.get("entry_count") is not None]
        c["_ref_up"] = sum(e["entry_count"] for e in vs) / c["valid_contestants"] if vs else None
        usd = [(p.get("value") or 0) * (p.get("quantity") or 1) for p in c["prizes"] if (p.get("currency") or "").upper() == "USD" and p.get("value")]
        val = sum(usd) if usd and all((p.get("currency") or "").upper() == "USD" and p.get("value") for p in c["prizes"]) else None
        c["_val"] = val if val and 0 < val < 10 ** 7 else None; c["_cats"] = set(j.get("prize_cats") or []); c["_own"] = any(j.get("own_signal") or [])
        c["_txt"] = ((c.get("name") or "") + " " + (c.get("incentive_name") or "") + " " + re.sub("<[^>]+>", " ", c.get("incentive_desc") or "")[:600]).lower()
        c["_vert"] = next((v for v, pat in VERTICALS if re.search(pat, c["_txt"] + " " + (c.get("site_name") or "").lower())), "unclassified")
        c["_types"] = {e.get("entry_method_generic_name") for e in ems}
        o.append(c)
    for c in o: c["_repeat"] = site_counts[c["site_id"]] >= 5
    valued = [c for c in o if c["_val"]]; bm = collections.defaultdict(list)
    for c in valued: bm[vband(c["_val"])].append(c["valid_contestants"])
    bm = {k: st.median(v) for k, v in bm.items()}
    for c in valued: c["_idx"] = c["valid_contestants"] / bm[vband(c["_val"])]
    def prof(g):
        clean = [c for c in g if c["_clean"]]; v = [c for c in g if c["_val"]]
        return {"n": len(g), "contestants": med([c["valid_contestants"] for c in g]), "conv_clean": med([c["_conv"] for c in clean]), "clean_n": len(clean), "entries_per_entrant": med([c["_epc"] for c in g]),
                "email_uptake": med([c["_email_up"] for c in g]), "referral_uptake": med([c["_ref_up"] for c in g]), "value_index": med([c["_idx"] for c in v]), "valued_n": len(v),
                "stated_pool_usd": med([c["_val"] for c in v]), "usd_per_contestant": med([c["_val"] / c["valid_contestants"] for c in v]), "repeat_organizer_share": sum(c["_repeat"] for c in g) / len(g) if g else None,
                "own_product_share": sum(c["_own"] for c in g) / len(g) if g else None, "duration": med([c["duration_in_days"] for c in g]), "actions": med([len(c["entry_methods"]) for c in g])}
    out = {"all": prof(o), "definitions": {"value_index": "contestants divided by the median contestants of the campaign's stated-USD value band", "repeat_organizer": "organizer with five or more ordinary campaigns in the export",
                                            "standout": "value index of 3 or more, the top 6% of valued campaigns", "vertical": "regex on names"}}
    # 1. launch subtypes
    out["launch_subtypes"] = {}
    for name, pat in LAUNCH:
        g = [c for c in o if re.search(pat, c["_txt"])]
        if len(g) >= 40: out["launch_subtypes"][name] = prof(g)
    # 2. standouts: index >= 3
    thr = 3.0; stand = [c for c in valued if c["_idx"] >= thr]; rest = [c for c in valued if c["_idx"] < thr]
    def share(g, f): return sum(1 for c in g if f(c)) / len(g) if g else None
    feats = {"own product prize": lambda c: c["_own"], "collaboration in title": lambda c: bool(re.search(r"(\bx\b|×|collab|partner)", c["_txt"])), "repeat organizer": lambda c: c["_repeat"],
             "stated pool under 250 USD": lambda c: c["_val"] < 250, "secret code action": lambda c: "Secret Code" in c["_types"], "email action": lambda c: bool(c["_email_up"]),
             "viral share action": lambda c: "Viral Shares" in c["_types"], "single prize unit": lambda c: sum((p.get("quantity") or 1) for p in c["prizes"]) == 1, "december start": lambda c: c["starts_at"][5:7] == "12",
             "14 days or less": lambda c: c["duration_in_days"] <= 14, "repeatable action": lambda c: c["_rep"], "11 or more actions": lambda c: len(c["entry_methods"]) >= 11, "youtube visit": lambda c: "YouTube Channel Visits" in c["_types"],
             "twitch follow": lambda c: "Twitch Follows" in c["_types"], "discord join": lambda c: "Chat Members" in c["_types"], "question action": lambda c: bool(c["_types"] & {"Answer a Question", "Single Choice List", "Multiple Choice Checkboxes"})}
    out["standouts"] = {"n": len(stand), "share_of_valued": len(stand) / len(valued), "contestants": med([c["valid_contestants"] for c in stand]), "stated_pool_usd": med([c["_val"] for c in stand]),
                        "usd_per_contestant": med([c["_val"] / c["valid_contestants"] for c in stand]), "features": {k: {"standouts": share(stand, f), "rest": share(rest, f)} for k, f in feats.items()},
                        "prize_categories": {}, "verticals": {}, "email_uptake": med([c["_email_up"] for c in stand]), "referral_uptake": med([c["_ref_up"] for c in stand]), "conv_clean": med([c["_conv"] for c in stand if c["_clean"]])}
    catc = collections.Counter(k for c in stand for k in c["_cats"]); catr = collections.Counter(k for c in rest for k in c["_cats"])
    out["standouts"]["prize_categories"] = {k: {"standouts": catc[k] / len(stand), "rest": catr[k] / len(rest), "ratio": (catc[k] / len(stand)) / (catr[k] / len(rest)) if catr[k] else None} for k, _ in catc.most_common(12)}
    vc = collections.Counter(c["_vert"] for c in stand); vr = collections.Counter(c["_vert"] for c in rest)
    out["standouts"]["verticals"] = {k: {"standouts": vc[k] / len(stand), "rest": vr[k] / len(rest), "ratio": (vc[k] / len(stand)) / (vr[k] / len(rest)) if vr[k] else None} for k, _ in vc.most_common(10)}
    # cheap prizes, big crowds
    cheap = [c for c in valued if c["_val"] < 250 and c["valid_contestants"] >= 5000]
    out["cheap_and_big"] = {"n": len(cheap), "prize_categories": dict(collections.Counter(k for c in cheap for k in c["_cats"]).most_common(6)), "verticals": dict(collections.Counter(c["_vert"] for c in cheap).most_common(6)),
                            "repeat_organizer_share": share(cheap, lambda c: c["_repeat"]), "own_product_share": share(cheap, lambda c: c["_own"]), "december_share": share(cheap, lambda c: c["starts_at"][5:7] == "12"),
                            "median_actions": med([len(c["entry_methods"]) for c in cheap]), "median_duration": med([c["duration_in_days"] for c in cheap])}
    # 3. industries
    byv = collections.defaultdict(list)
    for c in o: byv[c["_vert"]].append(c)
    out["industries"] = {k: prof(v) for k, v in sorted(byv.items(), key=lambda kv: -len(kv[1])) if len(v) >= 100}
    json.dump(out, open(a.out, "w"), indent=1); print("wrote", a.out)

if __name__ == "__main__":
    main()
