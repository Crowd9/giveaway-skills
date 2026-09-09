#!/usr/bin/env python3
"""Extra descriptive cuts used in the references: invalid entries, organizer experience, custom terms, opt-in checkbox,
own-product prizes. Writes analysis/output/extra_cuts.json. Same clean-subset rule as compare_groups.py.

  python3 analysis/extra_cuts.py export.json --classification private/classification.jsonl
"""
import argparse, collections, json, os, statistics as st

REPEAT = {"loyalty", "timed_bonus"}
TYPES = ["share_action", "email_subscribe", "tiktok_follow", "instagram_visit_profile", "twitter_follow", "twitter_retweet",
         "secret_code", "discord_join_server", "twitchtv_follow", "youtube_visit_channel", "facebook_visit", "custom_action"]

def med(xs):
    xs = [x for x in xs if x is not None]; return st.median(xs) if xs else None

def stats(g):
    return {"n": len(g), "contestants": med([c["valid_contestants"] for c in g]), "entries_per_entrant": med([c["_epc"] for c in g]),
            "contestants_per_impression": med([c["_conv"] for c in g]), "invalid_share": med([c["_inv"] for c in g])}

def grouped(g, key):
    b = collections.defaultdict(list)
    for c in g: b[key(c)].append(c)
    return {str(k): stats(v) for k, v in sorted(b.items(), key=lambda kv: str(kv[0]))}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("export"); ap.add_argument("--classification", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "output", "extra_cuts.json"))
    a = ap.parse_args()
    cl = {}
    for l in open(a.classification):
        j = json.loads(l); cl[j["campaign_id"]] = j
    d = json.load(open(a.export))
    nth = collections.Counter()
    for c in sorted([c for c in d if c.get("starts_at")], key=lambda c: c["starts_at"]):
        nth[c["site_id"]] += 1; c["_nth"] = nth[c["site_id"]]
    o = []
    for c in d:
        j = cl.get(c["campaign_id"])
        if not j or j["segment"] != "ordinary" or not c.get("valid_contestants") or not c.get("valid_entries"): continue
        ems = c.get("entry_methods") or []
        c["_rep"] = any(e.get("entry_method_type") in REPEAT or (e.get("entry_method_type") == "custom_action" and e.get("entry_method_template") == "bonus") for e in ems)
        c["_epc"] = c["valid_entries"] / c["valid_contestants"]
        c["_conv"] = c["valid_contestants"] / c["impressions"] if c.get("impressions") else None
        inv = c.get("invalid_entries") or 0; c["_inv"] = inv / (c["valid_entries"] + inv)
        c["_types"] = {e.get("entry_method_type") for e in ems}
        c["_own"] = any(j.get("own_signal") or [])
        c["_optin"] = [(e.get("entry_method_config") or {}).get("config_opt_in_checkbox") for e in ems if e.get("entry_method_type") == "email_subscribe"]
        em = [e for e in ems if e.get("entry_method_type") == "email_subscribe"]
        c["_email_uptake"] = (em[0].get("entry_count") or 0) / c["valid_contestants"] if em else None
        c["_validated_q"] = any(str((e.get("entry_method_config") or {}).get("config_validate_answer")).lower() in ("true", "1") for e in ems)
        o.append(c)
    clean = [c for c in o if not c["_rep"] and c["duration_in_days"] <= 14]
    nthb = lambda c: "1st" if c["_nth"] == 1 else "2nd" if c["_nth"] == 2 else "3rd-5th" if c["_nth"] <= 5 else "6th-10th" if c["_nth"] <= 10 else "11th+"
    invb = lambda c: "0" if c["_inv"] == 0 else "<1%" if c["_inv"] < 0.01 else "1-5%" if c["_inv"] < 0.05 else "5-20%" if c["_inv"] < 0.2 else "20%+"
    email = [c for c in clean if c["_optin"]]
    out = {
        "definitions": {"invalid_share": "invalid_entries / (valid_entries + invalid_entries) per campaign, median across campaigns",
                        "clean": "no repeatable action and duration <= 14 days", "own_signal": "word overlap between organizer name and prize name (classification file)"},
        "ordinary_n": len(o), "clean_n": len(clean),
        "invalid_buckets_all": grouped(o, invb),
        "invalid_share_campaigns_5pct_plus": round(sum(c["_inv"] >= 0.05 for c in o) / len(o), 3),
        "invalid_share_campaigns_20pct_plus": round(sum(c["_inv"] >= 0.2 for c in o) / len(o), 3),
        "invalid_by_method_presence_all": {t: {"with": med([c["_inv"] for c in o if t in c["_types"]]), "without": med([c["_inv"] for c in o if t not in c["_types"]]),
                                               "n_with": sum(t in c["_types"] for c in o)} for t in TYPES},
        "invalid_validated_question_clean": grouped(clean, lambda c: "validated question" if c["_validated_q"] else "no validated question"),
        "nth_campaign_clean": grouped(clean, nthb), "nth_campaign_all": grouped(o, nthb),
        "custom_terms_clean": grouped(clean, lambda c: bool(c.get("custom_tos"))),
        "custom_terms_share_all": round(sum(bool(c.get("custom_tos")) for c in o) / len(o), 3),
        "own_product_clean": grouped(clean, lambda c: c["_own"]),
        "optin_checkbox_clean_email_campaigns": grouped(email, lambda c: c["_optin"][0] or "unset"),
        "optin_email_uptake_clean": {str(k): {"n": len(v), "email_entries_per_contestant": med(v)} for k, v in
                                     collections.defaultdict(list, {k: [c["_email_uptake"] for c in email if (c["_optin"][0] or "unset") == k] for k in {c["_optin"][0] or "unset" for c in email}}).items()},
        "optin_checkbox_on_or_auto_share_all": round(sum(1 for c in o for v in c["_optin"] if v in ("On", "Auto")) / max(1, sum(len(c["_optin"]) for c in o)), 3),
    }
    json.dump(out, open(a.out, "w"), indent=1); print("wrote", a.out)

if __name__ == "__main__":
    main()
