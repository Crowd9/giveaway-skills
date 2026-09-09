#!/usr/bin/env python3
"""Cuts from the text and context fields of the export: organizer region from the site domain, question wording, share
copy, visit destinations, description and terms wording, campaign title wording, overlapping campaigns, close day and
hour, and newsletter wording. Writes analysis/output/text_context.json. Medians, ordinary segment, clean subset where
conversion is compared. No customer fields.

  python3 analysis/text_and_context.py export.json --classification private/classification.jsonl
"""
import argparse, collections, datetime as dt, json, os, re, statistics as st

REPEAT = {"loyalty", "timed_bonus"}
TLD = {"uk": "United Kingdom", "au": "Australia", "ca": "Canada", "de": "Germany", "fr": "France", "nz": "New Zealand", "in": "India", "es": "Spain", "it": "Italy", "nl": "Netherlands",
       "br": "Brazil", "mx": "Mexico", "pl": "Poland", "se": "Sweden", "dk": "Denmark", "no": "Norway", "fi": "Finland", "ie": "Ireland", "ch": "Switzerland", "at": "Austria", "be": "Belgium",
       "pt": "Portugal", "za": "South Africa", "sg": "Singapore", "my": "Malaysia", "ph": "Philippines", "id": "Indonesia", "jp": "Japan", "kr": "South Korea", "ru": "Russia", "tr": "Turkey", "ae": "UAE", "us": "United States"}
STOP = {"German": r"\b(und|der|die|das|nicht|mit|für|gewinnspiel|teilnahme)\b", "French": r"\b(et|les|des|pour|vous|concours|gagner|jeu)\b", "Spanish": r"\b(y|los|las|para|sorteo|ganar|participa)\b",
        "Portuguese": r"\b(e|para|você|sorteio|ganhar|participe)\b", "Italian": r"\b(e|per|gli|della|concorso|vincere)\b", "Dutch": r"\b(en|het|voor|winactie|winnen)\b", "Turkish": r"\b(ve|için|çekiliş|kazan)\b", "Indonesian": r"\b(dan|untuk|giveaway|menang|hadiah)\b"}

def med(xs): xs = [x for x in xs if x is not None]; return st.median(xs) if xs else None
def prof(g):
    return {"n": len(g), "contestants": med([c["valid_contestants"] for c in g]), "contestants_per_impression": med([c["_conv"] for c in g]), "entries_per_entrant": med([c["_epc"] for c in g]),
            "stated_usd_per_contestant": med([c["_val"] / c["valid_contestants"] for c in g if c["_val"]]), "usd_per_email": med([c["_val"] / c["_email"] for c in g if c["_val"] and c["_email"]]),
            "december_share": sum(c["starts_at"][5:7] == "12" for c in g) / len(g) if g else None}
def grouped(g, key, minn=50):
    b = collections.defaultdict(list)
    for c in g: b[key(c)].append(c)
    return {str(k): prof(v) for k, v in sorted(b.items(), key=lambda kv: -len(kv[1])) if len(v) >= minn}
def uptake_by(rows, key, minn=100):
    b = collections.defaultdict(list)
    for u, k in rows: b[k].append(u)
    return {str(k): {"n": len(v), "median_uptake": med(v)} for k, v in sorted(b.items(), key=lambda kv: -len(kv[1])) if len(v) >= minn}

def region(site_url):
    h = (site_url or "").lower().split("/")[2] if (site_url or "").startswith("http") else (site_url or "").lower()
    parts = h.split("."); tld = parts[-1] if parts else ""
    if tld in TLD: return TLD[tld]
    if len(parts) >= 2 and parts[-2] in ("co", "com", "org", "net") and tld in TLD: return TLD[tld]
    return "global domain (.com, .io, .net and so on)" if tld in ("com", "io", "net", "org", "gg", "tv", "app", "co", "shop", "store", "me", "xyz") else "other or none"

def qtype(q):
    q = (q or "").lower()
    if not q.strip(): return None
    if re.search(r"\b(which|favou?rite|prefer|would you|do you like|what would you|pick|choose)\b", q): return "preference"
    if re.search(r"\b(what year|how many|who (is|was|are)|name the|capital|which year|true or false|what is the)\b", q): return "trivia"
    if re.search(r"\b(why|feedback|improve|suggest|what do you think|tell us|opinion|idea)\b", q): return "feedback or open"
    if re.search(r"\b(email|phone|name|address|order|id|code|account|username)\b", q): return "detail capture"
    return "other"

def share_traits(t):
    t = t or ""
    return {"length": "short (under 60)" if len(t) < 60 else "medium (60 to 140)" if len(t) <= 140 else "long (over 140)", "hashtag": "#" in t, "mentions_win": bool(re.search(r"\b(win|giveaway|chance)\b", t, re.I)),
            "first_person": bool(re.search(r"\b(I|I'm|I've|my)\b", t)), "emoji": bool(re.search(r"[\U0001F300-\U0001FAFF☀-➿]", t))}

def dest(cfg, site_host):
    u = cfg.get("config_url") or cfg.get("config_page_url") or ""
    if not u and cfg.get("config_open_graph_data"):
        m = re.search(r'"source_url":\s*"([^"]+)"', str(cfg["config_open_graph_data"])); u = m.group(1) if m else ""
    h = u.lower().split("/")[2] if u.startswith("http") and u.count("/") >= 2 else ""
    if not h: return None
    if site_host and (h == site_host or h.endswith("." + site_host) or site_host.endswith("." + h)): return "organizer's own site"
    for k, lab in (("youtube", "YouTube"), ("youtu.be", "YouTube"), ("instagram", "Instagram"), ("facebook", "Facebook"), ("tiktok", "TikTok"), ("twitter", "X"), ("x.com", "X"), ("amazon", "Amazon"), ("shopify", "Shopify store"), ("gleam.io", "another Gleam campaign"), ("discord", "Discord"), ("twitch", "Twitch"), ("kickstarter", "Kickstarter"), ("apps.apple", "App Store"), ("play.google", "Google Play"), ("steam", "Steam")):
        if k in h: return lab
    return "another site"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("export"); ap.add_argument("--classification", required=True)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "output", "text_context.json"))
    a = ap.parse_args()
    seg = {}
    for l in open(a.classification):
        j = json.loads(l); seg[j["campaign_id"]] = j["segment"]
    d = json.load(open(a.export)); o = []
    bysite = collections.defaultdict(list)
    for c in d:
        if c.get("starts_at") and c.get("ends_at"): bysite[c["site_id"]].append(c)
    for cs in bysite.values():
        cs.sort(key=lambda c: c["starts_at"])
        for i, c in enumerate(cs): c["_overlap"] = i > 0 and c["starts_at"] < cs[i - 1]["ends_at"]
    for c in d:
        if seg.get(c["campaign_id"]) != "ordinary" or not c.get("valid_contestants") or not c.get("valid_entries"): continue
        ems = c["entry_methods"]
        c["_rep"] = any(e.get("entry_method_type") in REPEAT or (e.get("entry_method_type") == "custom_action" and e.get("entry_method_template") == "bonus") for e in ems)
        c["_conv"] = c["valid_contestants"] / c["impressions"] if c.get("impressions") else None; c["_epc"] = c["valid_entries"] / c["valid_contestants"]
        usd = [(p.get("value") or 0) * (p.get("quantity") or 1) for p in c["prizes"] if (p.get("currency") or "").upper() == "USD" and p.get("value")]
        val = sum(usd) if usd and all((p.get("currency") or "").upper() == "USD" and p.get("value") for p in c["prizes"]) else None
        c["_val"] = val if val and 0 < val < 10 ** 7 else None
        c["_email"] = sum(e["entry_count"] for e in ems if e.get("entry_method_generic_name") in ("Email Subscriptions", "Gleam Subscriber") and e.get("entry_count")) or None
        c["_region"] = region(c.get("site_url")); c["_host"] = (c.get("site_url") or "").lower().split("/")[2] if (c.get("site_url") or "").startswith("http") else ""
        desc = re.sub("<[^>]+>", " ", c.get("incentive_desc") or ""); tos = re.sub("<[^>]+>", " ", c.get("custom_tos") or ""); name = c.get("name") or ""
        c["_desc"] = desc; c["_tos"] = tos; c["_name"] = name
        low = (desc + " " + name).lower()
        c["_lang"] = next((L for L, pat in STOP.items() if len(re.findall(pat, low)) >= 4), "English or unknown")
        o.append(c)
    clean = [c for c in o if not c["_rep"] and c["duration_in_days"] <= 14]
    out = {"ordinary_n": len(o), "clean_n": len(clean), "definitions": {"region": "TLD of the organizer's site URL, a proxy", "clean": "no repeatable action and 14 days or less", "uptake": "completions per contestant of that action"}}
    out["region_all"] = grouped(o, lambda c: c["_region"], 100); out["region_clean"] = grouped(clean, lambda c: c["_region"], 50)
    out["language_guess_all"] = grouped(o, lambda c: c["_lang"], 50)
    # questions
    qrows = []; qtext = collections.Counter()
    for c in o:
        for e in c["entry_methods"]:
            cfg = e.get("entry_method_config") or {}
            if cfg.get("config_question") and e.get("entry_count") is not None:
                t = qtype(cfg["config_question"]); qrows.append((e["entry_count"] / c["valid_contestants"], t)); qtext[t] += 1
    out["question_types"] = uptake_by(qrows, lambda k: k)
    # share copy
    srows = []
    for c in o:
        for e in c["entry_methods"]:
            cfg = e.get("entry_method_config") or {}
            t = cfg.get("config_tweet_text") or cfg.get("config_share_body") or cfg.get("config_default_share_text")
            if t and e.get("entry_count") is not None and (e.get("entry_method_type") in ("share_action", "viral_share", "twitter_tweet") or "Viral" in (e.get("entry_method_generic_name") or "") or "Post" in (e.get("entry_method_generic_name") or "")):
                tr = share_traits(t); srows.append((e["entry_count"] / c["valid_contestants"], tr, e.get("entry_method_generic_name")))
    out["share_copy"] = {"by_length": uptake_by([(u, tr["length"]) for u, tr, g in srows], lambda k: k), "hashtag": uptake_by([(u, "with hashtag" if tr["hashtag"] else "no hashtag") for u, tr, g in srows], lambda k: k),
                         "mentions_win": uptake_by([(u, "says win, giveaway or chance" if tr["mentions_win"] else "does not") for u, tr, g in srows], lambda k: k),
                         "first_person": uptake_by([(u, "first person" if tr["first_person"] else "not first person") for u, tr, g in srows], lambda k: k),
                         "emoji": uptake_by([(u, "with emoji" if tr["emoji"] else "no emoji") for u, tr, g in srows], lambda k: k), "actions": len(srows),
                         "by_action": uptake_by([(u, g) for u, tr, g in srows], lambda k: k)}
    # visit destinations
    vrows = []
    for c in o:
        for e in c["entry_methods"]:
            if "Visit" not in (e.get("entry_method_generic_name") or "") or e.get("entry_count") is None: continue
            dd = dest(e.get("entry_method_config") or {}, c["_host"])
            if dd: vrows.append((e["entry_count"] / c["valid_contestants"], dd))
    out["visit_destinations"] = uptake_by(vrows, lambda k: k)
    # description and terms flags
    def flags(txt):
        t = txt.lower()
        return {"worldwide": bool(re.search(r"\b(worldwide|international|open globally|all countries|any country)\b", t)), "us_only": bool(re.search(r"\b(us only|usa only|united states only|u\.s\. only|us residents)\b", t)),
                "age_18": bool(re.search(r"\b(18\+|18 or older|over 18|aged 18|18 years)\b", t)), "no_purchase": bool(re.search(r"no purchase", t)), "winners_stated": bool(re.search(r"\b\d+ winners?\b", t)),
                "value_stated": bool(re.search(r"(\$|usd|£|€)\s?\d|\bworth\b|\bvalued? at\b", t))}
    out["description_flags_clean"] = {}
    for k in ("worldwide", "us_only", "age_18", "no_purchase", "winners_stated", "value_stated"):
        out["description_flags_clean"][k] = grouped(clean, lambda c, k=k: "present" if flags(c["_desc"])[k] else "absent", 50)
    out["description_flag_share_all"] = {k: sum(flags(c["_desc"])[k] for c in o) / len(o) for k in ("worldwide", "us_only", "age_18", "no_purchase", "winners_stated", "value_stated")}
    tos = [c for c in o if c["_tos"].strip()]
    out["terms_flag_share_of_custom_terms"] = {"n": len(tos), **{k: sum(flags(c["_tos"])[k] for c in tos) / len(tos) for k in ("worldwide", "us_only", "age_18", "no_purchase")},
                                              "median_words": med([len(c["_tos"].split()) for c in tos])}
    # title wording
    def term(nm):
        n = nm.lower()
        for w in ("giveaway", "sweepstakes", "contest", "competition", "raffle", "sorteo", "concours", "gewinnspiel", "prize draw", "airdrop"):
            if w in n: return w
        return "none of the usual words"
    out["title_term_clean"] = grouped(clean, lambda c: term(c["_name"]), 50); out["title_term_all"] = grouped(o, lambda c: term(c["_name"]), 100)
    out["title_traits_clean"] = {"win_a": grouped(clean, lambda c: "starts with win" if re.match(r"\s*win\b", c["_name"].lower()) else "other", 50),
                                 "value_in_title": grouped(clean, lambda c: "value in title" if re.search(r"(\$|£|€)\s?\d|\d+\s?(usd|eur|gbp)", c["_name"].lower()) else "no value", 50),
                                 "emoji_in_title": grouped(clean, lambda c: "emoji" if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", c["_name"]) else "no emoji", 50),
                                 "title_length": grouped(clean, lambda c: "under 30 characters" if len(c["_name"]) < 30 else "30 to 60" if len(c["_name"]) <= 60 else "over 60", 50)}
    # overlap
    out["overlap_all"] = grouped(o, lambda c: "overlaps the previous campaign" if c.get("_overlap") else "no overlap", 100)
    out["overlap_clean"] = grouped(clean, lambda c: "overlaps the previous campaign" if c.get("_overlap") else "no overlap", 50)
    # close day and hour (UTC)
    def endt(c): return dt.datetime.fromisoformat(c["ends_at"].replace("Z", "+00:00"))
    out["close_weekday_all"] = grouped([c for c in o if c.get("ends_at")], lambda c: endt(c).strftime("%A"), 100)
    out["close_hour_utc_all"] = grouped([c for c in o if c.get("ends_at")], lambda c: f"{endt(c).hour:02d}", 100)
    # newsletter wording
    nrows = []
    for c in o:
        for e in c["entry_methods"]:
            if e.get("entry_method_type") != "email_subscribe" or e.get("entry_count") is None: continue
            t = (e.get("entry_method_config") or {}).get("config_newsletter_description") or ""
            k = "no description" if not t.strip() else "mentions frequency or unsubscribe" if re.search(r"\b(weekly|monthly|daily|unsubscribe|any time|anytime|privacy)\b", t.lower()) else "description without those"
            nrows.append((e["entry_count"] / c["valid_contestants"], k))
    out["newsletter_wording"] = uptake_by(nrows, lambda k: k)
    json.dump(out, open(a.out, "w"), indent=1); print("wrote", a.out)

if __name__ == "__main__":
    main()
