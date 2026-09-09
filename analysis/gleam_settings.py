#!/usr/bin/env python3
"""Gleam-specific cuts for the gleam-campaign-setup skill: completions per contestant by Gleam action name, uptake by
position in the action list, description length against conversion, custom action templates, and the throwaway-account
restriction. Writes analysis/output/gleam_settings.json. Same clean-subset rule as compare_groups.py.

  python3 analysis/gleam_settings.py export.json --classification private/classification.jsonl
"""
import argparse, collections, json, os, re, statistics as st

REPEAT = {"loyalty", "timed_bonus"}

def med(xs):
    xs = [x for x in xs if x is not None]; return st.median(xs) if xs else None

def fam(e):
    t = e.get("entry_method_type") or ""; g = (e.get("entry_method_generic_name") or "").lower()
    if "email" in t or "newsletter" in g: return "email"
    if t in ("share_action", "viral_share") or "viral" in g or "refer" in g: return "share"
    if "follow" in t or "subscribe" in t or "join" in t or "follow" in g: return "follow"
    if "visit" in t or "view" in t or "visit" in g or "view" in g: return "visit"
    return "other"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("export"); ap.add_argument("--classification", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "output", "gleam_settings.json"))
    a = ap.parse_args()
    seg = {}
    for l in open(a.classification):
        j = json.loads(l); seg[j["campaign_id"]] = j["segment"]
    d = json.load(open(a.export)); o = []
    for c in d:
        if seg.get(c["campaign_id"]) != "ordinary" or not c.get("valid_contestants") or not c.get("valid_entries"): continue
        ems = c["entry_methods"]
        c["_rep"] = any(e.get("entry_method_type") in REPEAT or (e.get("entry_method_type") == "custom_action" and e.get("entry_method_template") == "bonus") for e in ems)
        c["_conv"] = c["valid_contestants"] / c["impressions"] if c.get("impressions") else None
        c["_epc"] = c["valid_entries"] / c["valid_contestants"]; o.append(c)
    clean = [c for c in o if not c["_rep"] and c["duration_in_days"] <= 14]
    up = collections.defaultdict(list); camps = collections.Counter()
    for c in o:
        seen = set()
        for e in c["entry_methods"]:
            g = e.get("entry_method_generic_name") or e.get("entry_method_type"); n = e.get("entry_count")
            if n is None: continue
            up[g].append(n / c["valid_contestants"])
            if g not in seen: camps[g] += 1; seen.add(g)
    by_action = {g: {"campaigns": cnt, "median": med(up[g]), "p25": st.quantiles(up[g], n=4)[0], "p75": st.quantiles(up[g], n=4)[2]}
                 for g, cnt in camps.most_common() if cnt >= 300}
    pos = collections.defaultdict(list)
    for c in o:
        ems = [e for e in c["entry_methods"] if e.get("entry_count") is not None]
        if len(ems) < 4: continue
        for i, e in enumerate(ems):
            pos[fam(e) + "|" + ("1st" if i == 0 else "2nd" if i == 1 else "3rd-4th" if i < 4 else "5th+")].append(e["entry_count"] / c["valid_contestants"])
    by_position = {k: {"n": len(v), "median": med(v)} for k, v in sorted(pos.items())}
    dl = collections.defaultdict(list)
    for c in clean:
        w = len(re.sub("<[^>]+>", " ", c.get("incentive_desc") or "").split())
        dl["0-25" if w <= 25 else "26-75" if w <= 75 else "76-150" if w <= 150 else "151-300" if w <= 300 else "301+"].append(c)
    desc = {k: {"n": len(g), "contestants": med([c["valid_contestants"] for c in g]), "contestants_per_impression": med([c["_conv"] for c in g]),
                "entries_per_entrant": med([c["_epc"] for c in g])} for k, g in dl.items()}
    tp = collections.Counter(); tu = collections.defaultdict(list); tw = collections.defaultdict(list)
    for c in o:
        for e in c["entry_methods"]:
            if e.get("entry_count") is None: continue
            u = e["entry_count"] / c["valid_contestants"]; cfg = e.get("entry_method_config") or {}
            if e.get("entry_method_type") == "custom_action":
                t = e.get("entry_method_template") or "none"; tp[t] += 1; tu[t].append(u)
            if "config_throwaway_account_restriction" in cfg: tw[str(cfg["config_throwaway_account_restriction"])].append(u)
    pv = collections.defaultdict(list); lo = collections.defaultdict(list)
    for c in o:
        for e in c["entry_methods"]:
            if e.get("entry_count") is None or "Visit" not in (e.get("entry_method_generic_name") or ""): continue
            cfg = e.get("entry_method_config") or {}; u = e["entry_count"] / c["valid_contestants"]
            pv[str(cfg.get("config_post_visit") or "unset")].append(u)
            if e.get("entry_method_generic_name") == "Visit a Page" and cfg.get("config_link_options"): lo[str(cfg["config_link_options"])].append(u)
    out = {"visit_post_visit_mode": {k: {"actions": len(v), "median_uptake": med(v)} for k, v in pv.items()},
           "visit_a_page_link_option": {k: {"actions": len(v), "median_uptake": med(v)} for k, v in lo.items()},
           "definitions": {"uptake": "entry_count / valid_contestants per action, median across actions offered", "clean": "no repeatable action and duration <= 14 days",
                           "position": "index of the action in the campaign's action list, campaigns with 4 or more actions"},
           "ordinary_n": len(o), "clean_n": len(clean), "uptake_by_gleam_action": by_action, "uptake_by_family_and_position": by_position,
           "description_length_clean": desc, "custom_action_templates": {t: {"actions": n, "median_uptake": med(tu[t])} for t, n in tp.most_common()},
           "throwaway_restriction_per_action": {k: {"actions": len(v), "median_uptake": med(v)} for k, v in tw.items()}}
    json.dump(out, open(a.out, "w"), indent=1); print("wrote", a.out)

if __name__ == "__main__":
    main()
