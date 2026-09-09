#!/usr/bin/env python3
"""Campaign types declared in the title and description (advent calendar, photo contest, launch, collaboration, flash,
series, scavenger hunt, cart or wishlist, charity, creator, community and so on) with contestants, clean conversion,
entries per entrant, email uptake, referral uptake and a value-adjusted index. Writes analysis/output/campaign_types.json.

  python3 analysis/campaign_types.py export.json --classification private/classification.jsonl
"""
import argparse, collections, json, os, re, statistics as st

REPEAT = {"loyalty", "timed_bonus"}
TYPES = [
    ("Advent or daily calendar", r"\b(advent|adventskalender|julkalender|joulukalenteri|12 days|24 days|daily prize|daily giveaway|prize a day|every day)\b"),
    ("Photo or video contest (UGC)", r"\b(photo contest|video contest|photo competition|share a photo|submit (a |your )?(photo|video|pic)|best photo|upload (a |your )?(photo|video))\b"),
    ("Voting contest", r"\b(vote for|voting|most votes|cast your vote|fan vote)\b"),
    ("Scavenger hunt or secret code", r"\b(scavenger|treasure hunt|secret code|hidden code|find the code|easter egg hunt)\b"),
    ("Product launch", r"\b(launch|now available|new release|just dropped|introducing|pre-?order|kickstarter|indiegogo)\b"),
    ("Collaboration or partner", r"(\bx\b|×|\bcollab|partner(ed|ship)?\b|teamed up|together with|in partnership)"),
    ("Bundle, mega or ultimate", r"\b(bundle|mega|ultimate|epic|massive|huge|giant|jackpot|grand prize)\b"),
    ("Cash prize", r"\b(cash|paypal|\$\d[\d,]*\s?(cash|usd)?\b(?! gift))"),
    ("Gift card or voucher", r"\b(gift card|giftcard|voucher|store credit|e-?gift)\b"),
    ("Cart, wishlist or spree", r"\b(win your cart|win your wishlist|wishlist|shopping spree|win your order|cart)\b"),
    ("Flash (24 to 72 hours)", r"\b(flash|24[- ]hour|48[- ]hour|72[- ]hour|one day only|ends tonight|weekend giveaway)\b"),
    ("Weekly or monthly series", r"\b(weekly|monthly|every week|every month|week \d|round \d|episode \d|#\d+\b)"),
    ("Charity or fundraiser", r"\b(charity|fundrais|donat|raffle for|in support of)\b"),
    ("Quiz or trivia", r"\b(quiz|trivia|guess the|predict|prediction|bracket)\b"),
    ("Creator or streamer", r"\b(streamer|stream|twitch|youtuber|creator|influencer|subscribers|subs\b)\b"),
    ("Community or Discord", r"\b(discord|community|members|server)\b"),
    ("Milestone", r"\b(\d+k|\d{2,3},000|million|milestone)\b"),
    ("Anniversary or birthday", r"\b(anniversary|birthday|bday|turns \d+|years old|year anniversary)\b"),
    ("Holiday themed", r"\b(christmas|xmas|halloween|valentine|easter|mother'?s day|father'?s day|black friday|thanksgiving|new year|diwali|summer)\b"),
    ("Free or no purchase", r"\b(free entry|no purchase|free to enter|it's free|free giveaway)\b"),
    ("Sweepstakes wording (US)", r"\bsweepstakes\b"), ("Competition wording (UK)", r"\bcompetition\b"), ("Sorteo (Spanish)", r"\bsorteo\b"), ("Gewinnspiel (German)", r"\bgewinnspiel\b"), ("Concours (French)", r"\bconcours\b")]
VB = [(50, "under 50"), (100, "50-99"), (250, "100-249"), (500, "250-499"), (1000, "500-999"), (2500, "1000-2499"), (5000, "2500-4999"), (10000, "5000-9999"), (25000, "10000-24999"), (50000, "25000-49999"), (10 ** 12, "50000+")]
def vband(v): return next(n for l, n in VB if v < l)
def med(xs): xs = [x for x in xs if x is not None]; return st.median(xs) if xs else None

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("export"); ap.add_argument("--classification", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "output", "campaign_types.json"))
    a = ap.parse_args()
    seg = {}
    for l in open(a.classification):
        j = json.loads(l); seg[j["campaign_id"]] = j["segment"]
    d = json.load(open(a.export)); o = []
    for c in d:
        if seg.get(c["campaign_id"]) != "ordinary" or not c.get("valid_contestants") or not c.get("valid_entries"): continue
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
        c["_val"] = val if val and 0 < val < 10 ** 7 else None
        c["_txt"] = ((c.get("name") or "") + " " + (c.get("incentive_name") or "") + " " + re.sub("<[^>]+>", " ", c.get("incentive_desc") or "")[:600]).lower()
        o.append(c)
    valued = [c for c in o if c["_val"]]; bandmed = collections.defaultdict(list)
    for c in valued: bandmed[vband(c["_val"])].append(c["valid_contestants"])
    bandmed = {k: st.median(v) for k, v in bandmed.items()}
    for c in valued: c["_idx"] = c["valid_contestants"] / bandmed[vband(c["_val"])]
    def prof(g):
        clean = [c for c in g if c["_clean"]]; v = [c for c in g if c["_val"]]
        return {"n": len(g), "share": len(g) / len(o), "contestants": med([c["valid_contestants"] for c in g]), "conv_clean": med([c["_conv"] for c in clean]), "clean_n": len(clean),
                "entries_per_entrant": med([c["_epc"] for c in g]), "email_uptake": med([c["_email_up"] for c in g]), "email_n": sum(1 for c in g if c["_email_up"] is not None),
                "referral_uptake": med([c["_ref_up"] for c in g]), "referral_n": sum(1 for c in g if c["_ref_up"] is not None), "duration": med([c["duration_in_days"] for c in g]),
                "actions": med([len(c["entry_methods"]) for c in g]), "repeatable_share": sum(c["_rep"] for c in g) / len(g), "value_index": med([c["_idx"] for c in v]), "valued_n": len(v),
                "stated_pool_usd": med([c["_val"] for c in v])}
    out = {"all": prof(o), "types": {}, "definitions": {"match": "regex on title, incentive name and first 600 characters of the description; a campaign can carry several types",
                                                       "value_index": "campaign contestants divided by the median contestants of its stated-USD value band, median per type", "clean": "no repeatable action and 14 days or less"}}
    for name, pat in TYPES:
        g = [c for c in o if re.search(pat, c["_txt"])]
        if len(g) >= 50: out["types"][name] = prof(g)
    json.dump(out, open(a.out, "w"), indent=1); print("wrote", a.out)

if __name__ == "__main__":
    main()
