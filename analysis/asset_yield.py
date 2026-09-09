#!/usr/bin/env python3
"""What campaigns produced, from action completions: email signups, follows by network, community joins, app installs,
referrals and content submissions per campaign, by size band, and stated USD per completion where the prize pool is
valued. Writes analysis/output/asset_yield.json.

  python3 analysis/asset_yield.py export.json --classification private/classification.jsonl
"""
import argparse, collections, json, os, statistics as st

ASSET = {"Email Subscriptions": "email", "Gleam Subscriber": "email", "X Follows": "follow_x", "Instagram Follows": "follow_instagram",
         "TikTok Follows": "follow_tiktok", "Twitch Follows": "follow_twitch", "Facebook Likes": "follow_facebook", "YouTube Entries": "subscribe_youtube",
         "Chat Members": "discord_join", "Telegram Channel Members": "telegram_join", "App Downloads": "app_download", "Viral Shares": "referrals",
         "Pinterest Entries": "follow_pinterest", "Bluesky Follows": "follow_bluesky", "Threads Follows": "follow_threads", "LinkedIn Follow": "follow_linkedin",
         "Spotify follows": "follow_spotify", "Podcast Subscriptions": "subscribe_podcast", "Snapchat": "follow_snapchat", "Media Submits": "ugc",
         "File Uploads": "ugc", "Instagram Comments": "comments", "Blog Comment": "comments"}

def med(xs): return st.median(xs) if xs else None
def q(xs, p): xs = sorted(xs); return xs[int(p * (len(xs) - 1))] if xs else None
def band(n): return "10k+" if n >= 10000 else "2.5k-10k" if n >= 2500 else "1k-2.5k"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("export"); ap.add_argument("--classification", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "output", "asset_yield.json"))
    a = ap.parse_args()
    cl = {}
    for l in open(a.classification):
        j = json.loads(l); cl[j["campaign_id"]] = j
    d = json.load(open(a.export)); o = []
    for c in d:
        j = cl.get(c["campaign_id"])
        if not j or j["segment"] != "ordinary" or not c.get("valid_contestants") or not c.get("valid_entries"): continue
        usd = [(p.get("value") or 0) * (p.get("quantity") or 1) for p in c["prizes"] if (p.get("currency") or "").upper() == "USD" and p.get("value")]
        c["_val"] = sum(usd) if usd and all((p.get("currency") or "").upper() == "USD" and p.get("value") for p in c["prizes"]) else None
        c["_cats"] = set(j.get("prize_cats") or []); o.append(c)
    yl = collections.defaultdict(list); yb = collections.defaultdict(list); cost = collections.defaultdict(list); share = collections.defaultdict(list); cc = collections.defaultdict(list)
    for c in o:
        got = collections.Counter()
        for e in c["entry_methods"]:
            k = ASSET.get(e.get("entry_method_generic_name"))
            if k and e.get("entry_count") is not None: got[k] += e["entry_count"]
        for k, n in got.items():
            yl[k].append(n); yb[k + "|" + band(c["valid_contestants"])].append(n); share[k].append(n / c["valid_contestants"])
            if c["_val"] and 0 < c["_val"] < 10 ** 7 and n > 0:
                cost[k].append(c["_val"] / n)
                if k == "email":
                    for cat in c["_cats"]: cc[cat].append(c["_val"] / n)
    out = {"definitions": {"yield": "completions of the asset action summed per campaign, campaigns offering it", "usd_per_completion": "stated USD prize pool divided by completions, campaigns with every prize valued in USD",
                           "share": "completions divided by unique contestants"}, "ordinary_n": len(o),
           "yield_by_asset": {k: {"campaigns": len(v), "p25": q(v, .25), "median": med(v), "p75": q(v, .75), "p90": q(v, .9), "per_contestant": med(share[k]),
                                  "usd_per_completion": med(cost[k]), "valued_campaigns": len(cost[k])} for k, v in sorted(yl.items(), key=lambda kv: -len(kv[1]))},
           "yield_by_asset_and_band": {k: {"campaigns": len(v), "p25": q(v, .25), "median": med(v), "p75": q(v, .75)} for k, v in sorted(yb.items())},
           "usd_per_email_by_prize_category": {k: {"campaigns": len(v), "median": med(v)} for k, v in sorted(cc.items(), key=lambda kv: -len(kv[1])) if len(v) >= 100}}
    json.dump(out, open(a.out, "w"), indent=1); print("wrote", a.out)

if __name__ == "__main__":
    main()
