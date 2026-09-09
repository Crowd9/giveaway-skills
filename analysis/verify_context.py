#!/usr/bin/env python3
"""Checks of the value-adjusted claims used in the skills against the export: prize value bands, value-adjusted prize
category and winner-count indexes, top versus bottom quintile profile, cadence, persistence between an organizer's
consecutive campaigns, collaboration signal, and entry-method prevalence in top versus bottom quintile by vertical.
Writes analysis/output/context_checks.json.

  python3 analysis/verify_context.py export.json --classification private/classification.jsonl
"""
import argparse, collections, datetime as dt, json, math, os, re, statistics as st

VERTICALS = [("gaming", r"\b(twitch|stream|gaming|gamer|esport|steam|playstation|xbox|nintendo|rtx|gpu|pc build|gaming pc|game|games|skins?|discord)\b"),
    ("technology", r"\b(phone|smartphone|iphone|galaxy|xiaomi|redmi|oneplus|oppo|realme|laptop|tablet|earbuds|headphones|smartwatch|tech|gadget|android)\b"),
    ("fashion_beauty", r"\b(beauty|skincare|makeup|cosmetic|fashion|apparel|clothing|sneaker|jewel|hair|fragrance|dress|boutique)\b"),
    ("food_drink", r"\b(coffee|food|snack|restaurant|bakery|cafe|brew|beer|wine|whisky|tea|kitchen|recipe|chocolate|grill|bbq)\b"),
    ("home", r"\b(home|garden|furniture|decor|mattress|appliance|vacuum|cleaning|candle|bedding)\b"),
    ("fitness_outdoor", r"\b(fitness|gym|workout|bike|cycling|fishing|hunting|camping|outdoor|golf|running|yoga|supplement)\b"),
    ("travel", r"\b(travel|trip|vacation|holiday|hotel|resort|cruise|flight|tickets?|concert|festival|tour)\b"),
    ("software", r"\b(app|software|saas|subscription|plan|premium account|vpn|course|membership)\b")]
COLLAB = re.compile(r"(\bx\b|×|collab|partner(ed|ship)?\b|in partnership|teamed up|together with)", re.I)
VBANDS = [(50, "under 50"), (100, "50-99"), (250, "100-249"), (500, "250-499"), (1000, "500-999"), (2500, "1000-2499"), (5000, "2500-4999"), (10000, "5000-9999"), (25000, "10000-24999"), (50000, "25000-49999"), (10 ** 12, "50000+")]

def med(xs):
    xs = [x for x in xs if x is not None]; return st.median(xs) if xs else None

def vband(v):
    for lim, name in VBANDS:
        if v < lim: return name

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("export"); ap.add_argument("--classification", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "output", "context_checks.json"))
    a = ap.parse_args()
    cl = {}
    for l in open(a.classification):
        j = json.loads(l); cl[j["campaign_id"]] = j
    d = json.load(open(a.export))
    bysite = collections.defaultdict(list)
    for c in d:
        if c.get("starts_at"): bysite[c["site_id"]].append(c)
    for s, cs in bysite.items():
        cs.sort(key=lambda c: c["starts_at"])
        for i, c in enumerate(cs):
            c["_prev_n"] = i
            c["_gap"] = (dt.datetime.fromisoformat(c["starts_at"].replace("Z", "+00:00")) - dt.datetime.fromisoformat(cs[i - 1]["starts_at"].replace("Z", "+00:00"))).days if i else None
            c["_next"] = cs[i + 1] if i + 1 < len(cs) else None
    o = []
    for c in d:
        j = cl.get(c["campaign_id"])
        if not j or j["segment"] != "ordinary" or not c.get("valid_contestants") or not c.get("valid_entries"): continue
        c["_conv"] = c["valid_contestants"] / c["impressions"] if c.get("impressions") else None
        c["_epc"] = c["valid_entries"] / c["valid_contestants"]; c["_nm"] = len(c["entry_methods"])
        c["_winners"] = sum((p.get("quantity") or 1) for p in c["prizes"]) or 1
        usd = [(p.get("value") or 0) * (p.get("quantity") or 1) for p in c["prizes"] if (p.get("currency") or "").upper() == "USD" and p.get("value")]
        c["_val"] = sum(usd) if usd and all((p.get("currency") or "").upper() == "USD" and p.get("value") for p in c["prizes"]) else None
        c["_cats"] = j.get("prize_cats") or []
        txt = " ".join([c.get("site_name") or "", c.get("name") or "", c.get("incentive_name") or ""] + [p.get("name") or "" for p in c["prizes"]]).lower()
        c["_vert"] = next((v for v, pat in VERTICALS if re.search(pat, txt)), "other")
        c["_collab"] = bool(COLLAB.search((c.get("name") or "") + " " + (c.get("incentive_name") or "")))
        c["_types"] = {e.get("entry_method_generic_name") or e.get("entry_method_type") for e in c["entry_methods"]}
        o.append(c)
    valued = [c for c in o if c["_val"] and 0 < c["_val"] < 10 ** 7]
    out = {"ordinary_n": len(o), "valued_n": len(valued)}
    # 1. value bands
    b = collections.defaultdict(list)
    for c in valued: b[vband(c["_val"])].append(c)
    out["value_bands"] = {k: {"n": len(v), "contestants": med([c["valid_contestants"] for c in v]), "entries_per_entrant": med([c["_epc"] for c in v]),
                             "prize_cost_per_contestant": med([c["_val"] / c["valid_contestants"] for c in v])} for k, v in b.items()}
    xs = [math.log10(c["_val"]) for c in valued]; ys = [math.log10(c["valid_contestants"]) for c in valued]
    mx, my = st.mean(xs), st.mean(ys); sxx = sum((x - mx) ** 2 for x in xs); sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys)); syy = sum((y - my) ** 2 for y in ys)
    slope = sxy / sxx; r2 = sxy ** 2 / (sxx * syy)
    out["value_regression"] = {"log_log_slope": slope, "contestants_multiplier_per_10x_value": 10 ** slope, "r_squared": r2, "n": len(valued),
                               "share_under_1000_usd": sum(c["_val"] <= 1000 for c in valued) / len(valued), "share_under_250_usd": sum(c["_val"] < 250 for c in valued) / len(valued)}
    # 2. value-adjusted index: campaign contestants / median contestants of its value band
    bandmed = {k: v["contestants"] for k, v in out["value_bands"].items()}
    for c in valued: c["_idx"] = c["valid_contestants"] / bandmed[vband(c["_val"])]
    cat = collections.defaultdict(list)
    for c in valued:
        for k in set(c["_cats"]): cat[k].append(c)
    out["prize_category_index_value_adjusted"] = {k: {"n": len(v), "contestants": med([c["valid_contestants"] for c in v]), "index": med([c["_idx"] for c in v]), "entries_per_entrant": med([c["_epc"] for c in v])}
                                                  for k, v in sorted(cat.items(), key=lambda kv: -len(kv[1])) if len(v) >= 100}
    wb = lambda w: "1" if w == 1 else "2-5" if w <= 5 else "6-20" if w <= 20 else "21+"
    w = collections.defaultdict(list)
    for c in valued: w[wb(c["_winners"])].append(c)
    out["winner_count_index_value_adjusted"] = {k: {"n": len(v), "index": med([c["_idx"] for c in v]), "contestants": med([c["valid_contestants"] for c in v])} for k, v in w.items()}
    # 3. top vs bottom quintile by contestants (all ordinary)
    srt = sorted(o, key=lambda c: c["valid_contestants"]); q = len(srt) // 5; bot, top = srt[:q], srt[-q:]
    prof = lambda g: {"n": len(g), "impressions": med([c.get("impressions") for c in g if c.get("impressions")]), "conversion": med([c["_conv"] for c in g]),
                      "prize_value_usd": med([c["_val"] for c in g if c["_val"]]), "winners": med([c["_winners"] for c in g]), "methods": med([c["_nm"] for c in g]),
                      "previous_campaigns": med([c["_prev_n"] for c in g]), "contestants": med([c["valid_contestants"] for c in g])}
    out["top_vs_bottom_quintile"] = {"top": prof(top), "bottom": prof(bot)}
    # 4. cadence
    cb = lambda g: "first" if g is None else "monthly or faster" if g <= 31 else "31-60" if g <= 60 else "61-120" if g <= 120 else "121-365" if g <= 365 else "over a year"
    cad = collections.defaultdict(list)
    for c in o: cad[cb(c["_gap"])].append(c)
    out["cadence"] = {k: {"n": len(v), "contestants": med([c["valid_contestants"] for c in v]), "entries_per_entrant": med([c["_epc"] for c in v]), "conversion": med([c["_conv"] for c in v])} for k, v in cad.items()}
    # 5. persistence
    pairs = [(c, c["_next"]) for c in o if c["_next"] and cl.get(c["_next"]["campaign_id"], {}).get("segment") == "ordinary" and c["_next"].get("valid_contestants")]
    def rate(th, above):
        s = [p for p in pairs if (p[0]["valid_contestants"] >= th) == above]; return {"n": len(s), "next_reaches": sum(p[1]["valid_contestants"] >= th for p in s) / len(s) if s else None}
    lx = [math.log10(p[0]["valid_contestants"]) for p in pairs]; ly = [math.log10(p[1]["valid_contestants"]) for p in pairs]
    mx, my = st.mean(lx), st.mean(ly); r = sum((x - mx) * (y - my) for x, y in zip(lx, ly)) / math.sqrt(sum((x - mx) ** 2 for x in lx) * sum((y - my) ** 2 for y in ly))
    out["persistence"] = {"pairs": len(pairs), "prev_5k_next_5k": rate(5000, True), "prev_under_5k_next_5k": rate(5000, False), "prev_10k_next_10k": rate(10000, True), "prev_under_10k_next_10k": rate(10000, False), "log_correlation": r}
    # 6. collaboration signal
    co = [c for c in valued if c["_collab"]]; nc = [c for c in valued if not c["_collab"]]
    topq = sorted(valued, key=lambda c: -c["_idx"])[:len(valued) // 5]; topset = {c["campaign_id"] for c in topq}
    out["collaboration_signal"] = {"collab_n": len(co), "index_collab": med([c["_idx"] for c in co]), "index_other": med([c["_idx"] for c in nc]),
                                   "top_quintile_rate_collab": sum(c["campaign_id"] in topset for c in co) / len(co), "top_quintile_rate_other": sum(c["campaign_id"] in topset for c in nc) / len(nc),
                                   "note": "collaboration detected by 'x', '×', collab or partner in the campaign name, a rough proxy"}
    # 7. entry method prevalence top vs bottom quintile within vertical
    prev = {}
    for v in {c["_vert"] for c in o}:
        g = sorted([c for c in o if c["_vert"] == v], key=lambda c: c["valid_contestants"]); k = len(g) // 5
        if k < 50: continue
        bot, top = g[:k], g[-k:]; cnt = collections.Counter()
        for c in g:
            for t in c["_types"]: cnt[t] += 1
        rows = {}
        for t, n in cnt.items():
            if n < 0.1 * len(g): continue
            pb = sum(t in c["_types"] for c in bot) / k; pt = sum(t in c["_types"] for c in top) / k
            if pb > 0: rows[t] = {"top": pt, "bottom": pb, "ratio": pt / pb}
        prev[v] = {"n": len(g), "quintile": k, "methods": dict(sorted(rows.items(), key=lambda kv: -kv[1]["ratio"])[:8])}
    out["method_prevalence_top_vs_bottom_by_vertical"] = prev
    json.dump(out, open(a.out, "w"), indent=1); print("wrote", a.out)

if __name__ == "__main__":
    main()
