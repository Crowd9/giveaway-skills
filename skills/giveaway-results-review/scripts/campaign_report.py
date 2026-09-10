#!/usr/bin/env python3
"""Full report from a campaign export, in the order of Gleam's reporting tabs. Reads a Gleam Actions export (one row per
completed action) as is, and exports from other platforms through --map or the built-in column synonyms, including wide
exports with one column per entry method. No dependencies. Aggregates only: no email, name, IP or row ever prints. Top Entrants show a display name (first
name and last initial) only.

  python3 campaign_report.py export.csv [--impressions N] [--prize-value USD] [--plan-cost USD] [--benchmark-cpl USD]
                                        [--sends "2026-04-20=Launch email,2026-05-01=Last call"] [--partners host1,host2]
                                        [--markdown report.md]
  python3 campaign_report.py --self-test

Parsing rules. ID is per row: Entrants are keyed by lower-cased Email, with Name as the fallback. When is in the account's
timezone, so every time figure is account time. Status Invalid rows are counted and excluded from engagement metrics.
Details on a refer action holds the referred person's email: that is the referral graph. Actions and Entries are outputs,
never funnel stages. The only funnel is Impressions to Entrants, and Impressions are not in the export.
"""
import argparse, collections, csv, datetime as dt, statistics as st, sys, urllib.parse

# Maintenance: DIRECTORIES, SOCIAL, WEBMAIL and SEARCH are hand-kept host lists used only to label a referrer.
# Add a host when a report shows it under "Other referrers" with a meaningful entrant count. An unknown host is labelled, never dropped.
DIRECTORIES = ("contestgirl", "giveawaybase", "ozbargain", "loquax", "latestdeals", "jeu-concours", "freestuffspot", "aussiecomps", "competitiondatabase",
               "giveawaylisting", "sweepstakes", "sweepsadvantage", "contestcanada", "hotukdeals", "prizefinder", "myoffers", "competitions")
SOCIAL = ("facebook", "t.co", "twitter", "x.com", "reddit", "instagram", "tiktok", "youtube", "pinterest", "discord", "linkedin", "threads", "bsky")
WEBMAIL = ("mail.google", "outlook.live", "mail.yahoo", "com.google.android.gm", "mail.", "webmail", "protonmail")
SEARCH = ("google.", "bing.", "duckduckgo", "yahoo.com/search", "search.")
HANDLE_COLS = ("Facebook", "Instagram", "Reddit", "Tiktok", "TikTok", "Twitter", "Youtube", "YouTube", "Discord", "Pinterest", "Twitch")
DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
SYNONYMS = {"who": ("Email", "Email Address", "E-mail", "Entrant Email", "User Email", "email", "Name", "Entrant", "User"),
            "action": ("Action", "Entry Method", "Entry Type", "Entry", "Method", "Task", "Action Name"),
            "entries": ("Entries", "Points", "Entry Count", "Worth", "Entries Earned", "Value"),
            "status": ("Status", "State", "Valid", "Verified"), "when": ("When", "Date", "Timestamp", "Created At", "Entered At", "Time", "Date Entered"),
            "country": ("Country",), "city": ("City",), "referrer": ("Referring URL", "Referrer", "Referer", "Referral URL", "Source", "Traffic Source"),
            "landing": ("Landing Page URL", "Landing Page", "Landing URL", "Page URL", "URL"), "details": ("Details", "Referred Email", "Referral", "Referred", "Answer")}

def resolve_columns(header, mapping):
    """Pick the column for each role from a user mapping (role=Column) or the synonym list. Missing roles are reported, never guessed."""
    cols = {}; low = {h.lower(): h for h in header}
    for role, names in SYNONYMS.items():
        if mapping.get(role): cols[role] = mapping[role]; continue
        for n in names:
            if n.lower() in low: cols[role] = low[n.lower()]; break
    if "who" in cols and cols["who"].lower() in ("name", "entrant", "user"):
        for n in ("Email", "Email Address", "E-mail"):
            if n.lower() in low: cols["who"] = low[n.lower()]; break
    return cols

def host_of(url):
    u = (url or "").strip()
    if not u: return ""
    if u.startswith("http"): return u.split("/")[2].lower() if u.count("/") >= 2 else u.lower()
    return u.lower()

def landing_kind(url):
    """gleam.io/giveaways/KEY is the Gleam giveaways directory listing (the campaign was featured). gleam.io/KEY/slug is the
    hosted campaign page. Anything else is the organizer's own page with the widget embedded."""
    u = (url or "").strip(); h = host_of(u)
    if not h: return "unknown"
    if "gleam.io" in h:
        path = u.split(h, 1)[1] if h in u else ""
        return "Gleam giveaways directory" if path.startswith("/giveaways") else "hosted page on gleam.io"
    return "embedded on " + h

def channel(host, landing=None):
    if "gleam.io" in (host or "") and landing == "Gleam giveaways directory": return "Gleam giveaways directory (featured)"
    if not host: return "Direct or unknown"
    if "gleam.io" in host: return "Gleam network (other campaigns and pages)"
    if any(d in host for d in DIRECTORIES): return "Competition directories"
    if any(s in host for s in SOCIAL): return "Social"
    if any(w in host for w in WEBMAIL): return "Email (webmail)"
    if any(s in host for s in SEARCH): return "Search"
    return "Other referrers"

def parse_when(s):
    for fmt in ("%Y-%m-%d %H:%M:%S %z", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S%z", "%d/%m/%Y %H:%M"):
        try: return dt.datetime.strptime((s or "").strip(), fmt)
        except ValueError: continue
    return None

def display(name):
    parts = (name or "").split()
    return (parts[0] + (" " + parts[-1][0] + "." if len(parts) > 1 else "")) if parts else "entrant"

def med(xs): return st.median(xs) if xs else None
def pct(a, b): return f"{a / b:.0%}" if b else "-"

def load(path, mapping=None):
    with open(path, newline="", encoding="utf-8-sig") as f: raw = list(csv.DictReader(f))
    if not raw: sys.exit("empty file")
    cols = resolve_columns(list(raw[0].keys()), mapping or {})
    if "who" not in cols: sys.exit("no column names the Entrant. Pass --map who=<column>")
    rows = []
    if "action" not in cols:
        # wide export: one row per person, one column per entry method holding a count or a yes
        meta = set(cols.values()); acts = [h for h in raw[0] if h not in meta and any((r.get(h) or "").strip() not in ("", "0", "no", "false", "No", "False") for r in raw)]
        if not acts: sys.exit("no action column and no per-method columns found. Pass --map action=<column>")
        for r in raw:
            for h in acts:
                v = (r.get(h) or "").strip()
                if v in ("", "0", "no", "false", "No", "False"): continue
                try: en = float(v)
                except ValueError: en = 1.0
                rows.append(dict(r, **{"Action": h, "Entries": en}))
        cols["action"] = "Action"; cols["entries"] = "Entries"; wide = True
    else: rows = raw; wide = False
    for r in rows:
        r["Action"] = (r.get(cols["action"]) or "").strip() or "unnamed action"
        r["_who"] = (r.get(cols["who"]) or "").strip().lower()
        sv = str(r.get(cols["status"]) or "").strip().lower() if "status" in cols else ""
        r["_valid"] = sv in ("", "valid", "winner", "approved", "verified", "true", "yes", "1")
        r["_when"] = parse_when(r.get(cols["when"])) if "when" in cols else None
        try: r["_entries"] = float(r.get(cols["entries"]) or 0) if "entries" in cols else 1.0
        except ValueError: r["_entries"] = 1.0
        r["_host"] = host_of(r.get(cols["referrer"])) if "referrer" in cols else ""
        r["_landing"] = landing_kind(r.get(cols["landing"])) if "landing" in cols else "unknown"; r["_channel"] = channel(r["_host"], r["_landing"])
        r["_refer"] = "refer" in r["Action"].lower() or "share" in r["Action"].lower() and "@" in (r.get(cols.get("details", ""), "") or "")
        for role, key in (("country", "Country"), ("city", "City"), ("details", "Details"), ("landing", "Landing Page URL")):
            if role in cols and cols[role] != key: r[key] = r.get(cols[role])
    rows = [r for r in rows if r["_who"]]
    load.last = {"columns": cols, "wide": wide, "missing": [k for k in ("status", "when", "entries", "country", "city", "referrer", "landing", "details") if k not in cols]}
    return rows

def analyze(rows, a):
    valid = [r for r in rows if r["_valid"]]; invalid = [r for r in rows if not r["_valid"]]
    people = collections.defaultdict(list)
    for r in valid: people[r["_who"]].append(r)
    for rs in people.values(): rs.sort(key=lambda r: r["_when"].timestamp() if r["_when"] else 0)
    n = len(people); R = {"base": n, "notes": []}
    entries = sum(r["_entries"] for r in valid)
    R["topline"] = {"entrants": n, "actions": len(valid), "entries": int(entries), "actions_per_entrant": len(valid) / n, "entries_per_entrant": entries / n,
                    "invalid_actions": len(invalid), "invalid_rate": len(invalid) / len(rows) if rows else 0}
    # engagement distribution
    b = collections.Counter()
    for rs in people.values():
        k = len(rs); b["1"] += k == 1; b["2-5"] += 2 <= k <= 5; b["6-10"] += 6 <= k <= 10; b["11+"] += k > 10
    R["engagement"] = {k: (b[k], b[k] / n) for k in ("1", "2-5", "6-10", "11+")}
    ten_plus = sum(1 for rs in people.values() if len(rs) >= 10)
    # speed
    spans = []; ten = 0; sitting = 0; multi = 0
    for rs in people.values():
        ts = [r["_when"] for r in rs if r["_when"]]
        if len(ts) < 2: continue
        multi += 1; span = (max(ts) - min(ts)).total_seconds(); spans.append(span); ten += span <= 600; sitting += span <= 7200
    bonus_all = [r for r in valid if "complet" in r["Action"].lower() and ("bonus" in r["Action"].lower() or "everything" in r["Action"].lower())]
    R["speed"] = {"multi": multi, "median_span_min": (med(spans) or 0) / 60, "within_10_min": ten / multi if multi else None, "one_sitting": sitting / multi if multi else None,
                  "completed_everything": (len({r["_who"] for r in bonus_all}), len({r["_who"] for r in bonus_all}) / n) if bonus_all else None}
    # actions: completions, unique, share, completion rate, median seconds
    per = collections.OrderedDict(); gaps = collections.defaultdict(list)
    for r in valid:
        d = per.setdefault(r["Action"], {"completions": 0, "who": set(), "invalid": 0}); d["completions"] += 1; d["who"].add(r["_who"])
    for r in invalid: per.setdefault(r["Action"], {"completions": 0, "who": set(), "invalid": 0})["invalid"] += 1
    for rs in people.values():
        for prev, cur in zip(rs, rs[1:]):
            if prev["_when"] and cur["_when"]:
                g = (cur["_when"] - prev["_when"]).total_seconds()
                if 0 <= g <= 1800: gaps[cur["Action"]].append(g)
    R["actions"] = [(act, d["completions"], len(d["who"]), d["completions"] / len(valid), len(d["who"]) / n, med(gaps[act]), d["invalid"]) for act, d in sorted(per.items(), key=lambda kv: -kv[1]["completions"])]
    # referral graph
    referred_by = {}; sharer = collections.defaultdict(set); refer_rows = 0
    for r in valid:
        if r["_refer"] and "@" in (r.get("Details") or ""):
            refer_rows += 1; ref = r["Details"].strip().lower(); sharer[r["_who"]].add(ref); referred_by.setdefault(ref, r["_who"])
    referred_entrants = {e for e in referred_by if e in people}
    handles_of = lambda who: [c for c in HANDLE_COLS if any(r.get(c) for r in people.get(who, []))]
    top_sharers = []
    for who, refs in sorted(sharer.items(), key=lambda kv: -len(kv[1]))[:10]:
        joined = [e for e in refs if e in people]; brought = sum(sum(r["_entries"] for r in people[e]) for e in joined)
        one_action = sum(1 for e in joined if len(people[e]) == 1)
        top_sharers.append((display(people[who][0].get("Name")), len(refs), len(joined), int(brought), len(handles_of(who)), one_action))
    R["viral"] = {"refer_rows": refer_rows, "sharers": len(sharer), "referred_entrants": len(referred_entrants), "referred_share": len(referred_entrants) / n,
                  "referrals_per_sharer": (refer_rows / len(sharer)) if sharer else None, "top": top_sharers,
                  "participation": len(sharer) / n, "referral_conversion": len(referred_entrants) / refer_rows if refer_rows else None,
                  "lift": len(referred_entrants) / (n - len(referred_entrants)) if n > len(referred_entrants) else None,
                  "top_share": (top_sharers[0][1] / refer_rows) if top_sharers and refer_rows else None}
    # geo
    first = {who: rs[0] for who, rs in people.items()}
    R["countries"] = collections.Counter(first[w].get("Country") or "unknown" for w in first).most_common(10)
    cities = collections.Counter((first[w].get("City"), first[w].get("Country")) for w in first if first[w].get("City"))
    R["cities"] = cities.most_common(10)
    # retention
    days_active = collections.Counter()
    for rs in people.values():
        k = len({r["_when"].date() for r in rs if r["_when"]}); days_active["1" if k <= 1 else "2" if k == 2 else "3" if k == 3 else "4+"] += 1
    R["retention"] = {k: (days_active[k], days_active[k] / n) for k in ("1", "2", "3", "4+")}
    # heatmap
    heat = collections.Counter((r["_when"].weekday(), r["_when"].hour) for r in valid if r["_when"])
    R["heat"] = heat; R["heat_peak"] = heat.most_common(1)[0] if heat else None
    whens = [r["_when"] for r in valid if r["_when"]]
    if whens:
        start = min(whens); R["first48"] = sum(1 for w in whens if (w - start).total_seconds() <= 172800) / len(whens); R["start"] = start; R["end"] = max(whens)
    # traffic: first touch channels, hosts, hosted vs embedded, utm
    ft = collections.Counter(first[w]["_channel"] for w in first); fh = collections.Counter(first[w]["_host"] or "direct or unknown" for w in first)
    ch_actions = collections.Counter(r["_channel"] for r in valid); ch_invalid = collections.Counter(r["_channel"] for r in invalid); ch_all = collections.Counter(r["_channel"] for r in rows)
    avg_apc = len(valid) / n
    ch_apc = {}
    for c in ft:
        ppl = [w for w in first if first[w]["_channel"] == c]; ch_apc[c] = (sum(len(people[w]) for w in ppl) / len(ppl)) / avg_apc if ppl else None
    R["channels"] = [(c, ft[c], ft[c] / n, ch_actions[c], ch_apc[c], ch_invalid[c] / ch_all[c] if ch_all[c] else 0) for c, _ in ft.most_common()]
    R["hosts"] = fh.most_common(12); R["invalid_rate_all"] = R["topline"]["invalid_rate"]
    lp = collections.Counter(first[w]["_landing"] for w in first); R["landing"] = lp.most_common(6)
    feat = [w for w in first if first[w]["_channel"] == "Gleam giveaways directory (featured)"]
    landed = [w for w in first if first[w]["_landing"] == "Gleam giveaways directory"]
    R["featured"] = {"entrants": len(feat), "share": len(feat) / n, "depth": (sum(len(people[w]) for w in feat) / len(feat)) / avg_apc if feat else None,
                     "landed": len(landed), "landed_share": len(landed) / n, "landed_depth": (sum(len(people[w]) for w in landed) / len(landed)) / avg_apc if landed else None} if landed else None
    utm = collections.Counter()
    for w in first:
        q = urllib.parse.parse_qs(urllib.parse.urlparse(first[w].get("Landing Page URL") or "").query)
        if any(k.startswith("utm_") for k in q): utm[(q.get("utm_source", ["-"])[0], q.get("utm_medium", ["-"])[0], q.get("utm_campaign", ["-"])[0])] += 1
    R["utm"] = utm.most_common(10)
    # partners
    if a.partners:
        R["partners"] = [(p, sum(1 for w in first if p in (first[w]["_host"] or "")), sum(1 for w in first if p in (first[w]["_host"] or "")) / n) for p in a.partners]
    # audience handles
    R["handles"] = [(c, sum(1 for w in people if any(r.get(c) for r in people[w])) / n) for c in HANDLE_COLS if c in rows[0] and any(r.get(c) for r in rows)]
    top = sorted(people.items(), key=lambda kv: -len(kv[1]))[:10]
    R["top_entrants"] = [(display(rs[0].get("Name")), len(rs), int(sum(r["_entries"] for r in rs)), len(sharer.get(who, ())), len({r["_when"].date() for r in rs if r["_when"]}), len(handles_of(who))) for who, rs in top]
    # promotions
    R["sends"] = []
    if a.sends and whens:
        byday = collections.Counter(w.date() for w in whens); newby = collections.Counter(first[w]["_when"].date() for w in first if first[w]["_when"])
        for item in a.sends.split(","):
            d, _, label = item.partition("="); day = dt.date.fromisoformat(d.strip())
            after = sum(byday[day + dt.timedelta(days=i)] for i in range(2)); newa = sum(newby[day + dt.timedelta(days=i)] for i in range(2))
            base_days = [day - dt.timedelta(days=i) for i in range(1, 8)]; base = sum(byday[x] for x in base_days) / 7
            R["sends"].append((label.strip() or d, day.isoformat(), after, newa, (after / 2) / base if base else None))
    # ROI
    if a.prize_value is not None or a.plan_cost is not None:
        cost = (a.prize_value or 0) + (a.plan_cost or 0); emails = sum(1 for rs in people.values() if any(("subscribe" in r["Action"].lower() or "newsletter" in r["Action"].lower()) for r in rs))
        R["roi"] = {"cost": cost, "per_entrant": cost / n, "per_entry": cost / entries if entries else None, "per_email": cost / emails if emails else None, "emails": emails,
                    "lead_value": (a.benchmark_cpl * emails) if a.benchmark_cpl and emails else None}
    R["ten_plus"] = ten_plus
    return R

def render(R, a):
    L = []; w = L.append; T = R["topline"]; n = R["base"]
    info = getattr(load, "last", None)
    if info:
        w("Columns read: " + ", ".join(f"{k} = {v}" for k, v in info["columns"].items()) + (", wide export with one column per entry method" if info["wide"] else "") + (". Not in this file: " + ", ".join(info["missing"]) + ", so those sections are thin or omitted." if info["missing"] else "."))
    w(f"# Campaign report\n\nBase: {n:,} export entrants (unique valid emails). Times are the account timezone. Impressions are not in the export" + (f", {a.impressions:,} supplied from the Reporting tab." if a.impressions else ", so there is no Impressions-to-entrants funnel here."))
    w("\n## Overview\n")
    w(f"| Metric | Value |\n|---|---|\n| Users | {n:,} |\n| Actions completed | {T['actions']:,} |\n| Entries | {T['entries']:,} |\n| Actions per entrant | {T['actions_per_entrant']:.2f} |\n| Entries per entrant | {T['entries_per_entrant']:.2f} |\n| Invalid actions | {T['invalid_actions']:,} ({T['invalid_rate']:.1%} of rows) |"
      + (f"\n| Conversion Rate | {n / a.impressions:.1%} |" if a.impressions else ""))
    E = R["engagement"]; w("\nEngagement by actions per Entrant: " + ", ".join(f"{k}: {v[0]:,} ({v[1]:.0%})" for k, v in E.items()) + ".")
    S = R["speed"]
    if S["multi"]:
        w(f"Speed: of {S['multi']:,} multi-action entrants, typical first-to-last span {S['median_span_min']:.0f} minutes, {S['within_10_min']:.0%} done within 10 minutes, {S['one_sitting']:.0%} in one sitting (under 2 hours)." + (f" Completed everything: {S['completed_everything'][0]:,} entrants ({S['completed_everything'][1]:.0%})." if S["completed_everything"] else ""))
    # insights
    ins = []
    ch = [c for c in R["channels"] if c[1] >= 30 and c[4]]
    if ch:
        best = max(ch, key=lambda c: c[4]); worst = min(ch, key=lambda c: c[4])
        ins.append(f"Source whose entrants went deepest: {best[0]} at {best[4]:.2f}x the average actions per entrant ({best[1]:,} entrants). Least deep: {worst[0]} at {worst[4]:.2f}x ({worst[1]:,}).")
    if R.get("first48") is not None: ins.append(f"{R['first48']:.0%} of all actions happened in the first 48 hours.")
    V = R["viral"]
    if V["top_share"] is not None: ins.append(f"Top sharer accounts for {V['top_share']:.0%} of referral completions" + (" (over 40%, review before crediting)." if V["top_share"] > 0.4 else "."))
    ins.append(f"Average depth {T['actions_per_entrant']:.1f} actions, {R['ten_plus'] / n:.0%} of entrants completed 10 or more.")
    if R["cities"]: c0 = R["cities"][0]; ins.append(f"Biggest city concentration: {c0[0][0]}, {c0[0][1]} with {c0[1]:,} entrants ({c0[1] / n:.0%}).")
    if R["countries"] and R["cities"] and R["countries"][0][0] != R["cities"][0][0][1]: ins.append(f"City and country leaders diverge: {R['countries'][0][0]} leads by country, {R['cities'][0][0][0]} leads by city.")
    if R["engagement"]["1"][1] > 0.1: ins.append(f"{R['engagement']['1'][0]:,} entrants ({R['engagement']['1'][1]:.0%}) completed one action only.")
    w("\nInsights:\n" + "\n".join(f"- {i}" for i in ins))
    w(f"\nEntrant journey: entered {n:,} (100%), completed more than one action {n - E['1'][0]:,} ({(n - E['1'][0]) / n:.0%}), shared {V['sharers']:,} ({V['participation']:.0%}), referred new entrants (an output per sharer, never a stage): {V['referred_entrants']:,} referred entrants.")
    if R["heat_peak"]:
        (dw, hr), cnt = R["heat_peak"]; w(f"\nActivity peak: {DAYS[dw]} {hr:02d}:00 account time with {cnt:,} actions. A single campaign's heatmap follows its launch timing.")
        w("\nHour | " + " | ".join(DAYS) + "\n---|" + "---|" * 7)
        for h in range(24): w(f"{h:02d} | " + " | ".join(f"{R['heat'][(d, h)]:,}" if R["heat"][(d, h)] else "" for d in range(7)))
    if R["sends"]:
        w("\nPromotional sends (activity in the 48 hours after each send against the 7-day daily baseline before it, never a causal claim):\n\n| Send | Date | Actions in 48h | New Entrants in 48h | Lift |\n|---|---|---|---|---|")
        for s in R["sends"]: w(f"| {s[0]} | {s[1]} | {s[2]:,} | {s[3]:,} | {s[4]:.1f}x |" if s[4] else f"| {s[0]} | {s[1]} | {s[2]:,} | {s[3]:,} | no baseline |")
    if R.get("roi"):
        r = R["roi"]; w(f"\nCost per result on the inputs given (prize plus plan cost {r['cost']:,.0f}): {r['per_entrant']:.2f} per entrant, {r['per_entry']:.4f} per entry" + (f", {r['per_email']:.2f} per email subscriber ({r['emails']:,} subscribers)" if r["per_email"] else "") + (f". Lead-value proxy at the benchmark cost per lead of {a.benchmark_cpl:.2f} that the user supplied: {r['lead_value']:,.0f}. That is what the same subscribers would cost through another channel, an assumption priced at the user's own figure." if r["lead_value"] else "."))
        w("A real revenue figure comes from joining Entrant email against store orders over a fixed window and summing order value. The export carries no order data, so nothing here is revenue.")
    else: w("\nROI needs Prize value and plan cost (--prize-value, --plan-cost, optional --benchmark-cpl).")
    w("\n## Traffic\n\nFirst-touch channel per Entrant (earliest row's referrer). Email clicks arrive as webmail or direct and are undercounted.\n\n| Channel | Entrants | Share | Actions | Depth vs average | Invalid rate |\n|---|---|---|---|---|---|")
    for c in R["channels"]: w(f"| {c[0]} | {c[1]:,} | {c[2]:.0%} | {c[3]:,} | {c[4]:.2f}x | {c[5]:.1%}{' (2x campaign rate or more)' if c[5] >= 2 * R['invalid_rate_all'] and c[5] > 0 else ''} |")
    w("\nRaw referrers (first touch):\n\n| Host | Entrants |\n|---|---|" + "".join(f"\n| {h} | {k:,} |" for h, k in R["hosts"]))
    w("\nLanding page at first touch: " + ", ".join(f"{k} {v:,} ({v / n:.0%})" for k, v in R["landing"]) + ". gleam.io/KEY/slug is the hosted page, gleam.io/giveaways/KEY is the directory listing, any other host is an embed.")
    if R.get("featured"):
        F = R["featured"]; w(f"\nFeatured on gleam.io/giveaways: {F['entrants']:,} entrants ({F['share']:.0%}) came from browsing the directory (landed on the listing with gleam.io as the referrer)" + (f", at {F['depth']:.2f}x the average actions per entrant" if F["depth"] else "") + f". {F['landed']:,} entrants ({F['landed_share']:.0%}) landed on the listing URL from any source, at {F['landed_depth']:.2f}x, since the listing link also gets shared by aggregators, email and social. Listing traffic is people browsing giveaways, so read its depth and email signups apart from your own channels.")
    if R["utm"]: w("\nUTM rollup (first touch):\n\n| Source | Medium | Campaign | Entrants |\n|---|---|---|---|" + "".join(f"\n| {s} | {m} | {c} | {k:,} |" for (s, m, c), k in R["utm"]))
    if R.get("partners"): w("\nPartners (by referrer host): " + ", ".join(f"{p} {k:,} entrants ({sh:.1%})" for p, k, sh in R["partners"]) + ".")
    else: w("\nPartner contribution needs --partners with the hosts or UTM values that identify them. Without tagging it is not attributable.")
    w("\n## Entry methods\n\n| Action | Completions | Entrants | Share of actions | Completion rate | Typical seconds | Invalid |\n|---|---|---|---|---|---|---|")
    for act, comp, uniq, share, rate, sec, inv in R["actions"]:
        flag = " (slow)" if sec and sec > 120 else ""
        w(f"| {act} | {comp:,} | {uniq:,} | {share:.0%} | {rate:.0%} | {f'{sec:.0f}{flag}' if sec is not None else '-'} | {inv:,} |")
    w("\nTypical seconds is the gap from the Entrant's previous action, in-session gaps under 30 minutes only. Visits usually run a few seconds, referrals minutes.")
    w(f"\n## Viral\n\nReferral completions {V['refer_rows']:,}, sharers {V['sharers']:,} ({V['participation']:.0%} of entrants), referred entrants who entered {V['referred_entrants']:,} ({V['referred_share']:.0%} of entrants)" + (f", referrals per sharer {V['referrals_per_sharer']:.1f}" if V["referrals_per_sharer"] else "") + (f", share of referrals who joined {V['referral_conversion']:.0%} (referred entrants divided by referral completions, no click data)" if V["referral_conversion"] is not None else "") + (f", viral lift +{V['lift']:.0%} (referred divided by non-referred entrants)." if V["lift"] is not None else "."))
    if V["top"]:
        w("\n| Sharer | Referral completions | Referred who entered | Entries brought | Connected accounts | Referred doing one action |\n|---|---|---|---|---|---|")
        for s in V["top"]:
            tell = " (signal: no connected accounts, outsized referrals)" if s[4] == 0 and s[1] >= 10 else ""
            w(f"| {s[0]}{tell} | {s[1]:,} | {s[2]:,} | {s[3]:,} | {s[4]} | {s[5]:,} |")
        w("\nSignals, never verdicts: a sharer with many referrals, no connected accounts and referred Entrants who mostly do one action deserves a look before any Prize.")
    w("\n## Audience\n\n| Country | Entrants | Share |\n|---|---|---|" + "".join(f"\n| {c} | {k:,} | {k / n:.0%} |" for c, k in R["countries"]))
    if R["cities"]: w("\n| City | Entrants |\n|---|---|" + "".join(f"\n| {c}, {co} | {k:,} |" for (c, co), k in R["cities"]))
    if R["handles"]: w("\nConnected accounts: " + ", ".join(f"{c} {v:.0%}" for c, v in R["handles"]) + ".")
    Rt = R["retention"]; w("\nRetention by distinct active days: " + ", ".join(f"{k}: {v[0]:,} ({v[1]:.0%})" for k, v in Rt.items()) + f". {1 - Rt['1'][1]:.0%} returned on a later day. One-day dominance is normal for a giveaway.")
    w("\nMost engaged Entrants:\n\n| Entrant | Actions | Entries | Referred | Days active | Connected accounts |\n|---|---|---|---|---|---|" + "".join(f"\n| {t[0]} | {t[1]} | {t[2]:,} | {t[3]} | {t[4]} | {t[5]} |" for t in R["top_entrants"]))
    w("""
## Outcomes

Nothing in this section is in the export. Pull each figure from the email provider and the store, then record it beside this report.

- Unsubscribes and spam complaints in the 7 days after the Winners email, from the email provider, for the giveaway segment on its own.
- Addresses synced to the email provider against addresses collected here, so the gap between the two is visible.
- Customers and revenue from a join of Entrant email against order data at 30, 60 and 90 days after close.
- Open share of the new subscribers in their first 30 days, which says how much of the list is worth keeping.

Run the same four again after the next campaign and the pair becomes a trend.""")
    return "\n".join(L)

def self_test():
    import os, tempfile
    d = tempfile.mkdtemp(); p = os.path.join(d, "e.csv")
    with open(p, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["ID", "Name", "Email", "Status", "Action", "Entries", "Details", "City", "Country", "When", "Landing Page URL", "Referring URL", "Facebook", "Twitter"])
        base = dt.datetime(2026, 5, 1, 10, 0, 0, tzinfo=dt.timezone(dt.timedelta(hours=10)))
        rows = [("Ann Lee", "a@example.com", "Valid", "Entry Confirmed", 1, "", "Sydney", "Australia", 0, "https://gleam.io/x?utm_source=news&utm_medium=email", "https://mail.google.com/", "", "@ann"),
                ("Ann Lee", "a@example.com", "Valid", "Subscribe to Our List", 5, "", "Sydney", "Australia", 30, "https://gleam.io/x", "https://mail.google.com/", "", "@ann"),
                ("Ann Lee", "a@example.com", "Valid", "Refer 3 Friends", 3, "b@example.com", "Sydney", "Australia", 400, "https://gleam.io/x", "", "", "@ann"),
                ("Bob Ray", "b@example.com", "Valid", "Entry Confirmed", 1, "", "Toronto", "Canada", 5000, "https://gleam.io/x", "https://www.contestgirl.com/", "", ""),
                ("Cy Q", "c@example.com", "Invalid", "Subscribe to Our List", 5, "", "Leeds", "United Kingdom", 6000, "https://gleam.io/x", "https://www.contestgirl.com/", "", "")]
        for i, (nm, em, stt, act, en, det, city, co, off, lp, ref, fb, tw) in enumerate(rows):
            wr.writerow([i, nm, em, stt, act, en, det, city, co, (base + dt.timedelta(seconds=off)).strftime("%Y-%m-%d %H:%M:%S %z"), lp, ref, fb, tw])
    class A: impressions = None; prize_value = 100.0; plan_cost = 50.0; benchmark_cpl = 2.0; sends = "2026-05-01=Launch"; partners = ["contestgirl"]
    R = analyze(load(p), A)
    assert R["topline"]["entrants"] == 2 and R["topline"]["invalid_actions"] == 1 and R["viral"]["referred_entrants"] == 1 and R["viral"]["sharers"] == 1, R["topline"]
    assert landing_kind("https://gleam.io/giveaways/UQW3q") == "Gleam giveaways directory" and landing_kind("https://gleam.io/UQW3q/apple-airpods") == "hosted page on gleam.io" and landing_kind("https://shop.example.com/win") == "embedded on shop.example.com"
    assert R["channels"][0][0] in ("Email (webmail)", "Competition directories") and R["utm"][0][1] == 1 and R["roi"]["emails"] == 1 and R["partners"][0][1] == 1, (R["channels"], R["utm"], R["roi"])
    out = render(R, A); assert "## Viral" in out and "Ann L." in out and "a@example.com" not in out and "Toronto, Canada" in out, out[:300]
    assert "| Users | 2 |" in out and "Impressions are not in the export" in out and "so there is no Impressions-to-entrants funnel here" in out, out[:400]
    class C: impressions = 10; prize_value = None; plan_cost = None; benchmark_cpl = None; sends = None; partners = None
    out2 = render(analyze(load(p), C), C)
    assert "| Conversion Rate | 20.0% |" in out2 and "supplied from the Reporting tab" in out2 and "Views" not in out2 and "share who entered" not in out2.lower(), out2[:400]
    q = os.path.join(d, "wide.csv")
    with open(q, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email Address", "Date", "Country", "Follow on Instagram", "Join newsletter", "Share with friends"])
        wr.writerow(["x@example.com", "2026-05-01 09:00:00", "Ireland", "1", "1", "0"]); wr.writerow(["y@example.com", "2026-05-01 09:30:00", "Ireland", "1", "0", "0"])
    class B: impressions = None; prize_value = None; plan_cost = None; benchmark_cpl = None; sends = None; partners = None
    R2 = analyze(load(q, {}), B); assert R2["topline"]["entrants"] == 2 and R2["topline"]["actions"] == 3 and load.last["wide"], R2["topline"]
    assert "referrer" in load.last["missing"] and "Follow on Instagram" in render(R2, B)
    print("self-test passed"); return 0

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export", nargs="?"); ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--impressions", type=int); ap.add_argument("--prize-value", type=float); ap.add_argument("--plan-cost", type=float); ap.add_argument("--benchmark-cpl", type=float)
    ap.add_argument("--sends", help='comma list of date=label, e.g. "2026-04-20=Launch email,2026-05-01=Last call"'); ap.add_argument("--partners", help="comma list of referrer hosts or UTM values that identify partners")
    ap.add_argument("--markdown", help="write the report here as well as printing it")
    ap.add_argument("--map", help="column mapping for exports from other platforms, e.g. \"who=Email Address,action=Entry Type,Entries=Points,when=Date,status=Verified,referrer=Source\"")
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    if not a.export: ap.error("export path required")
    a.partners = [p.strip() for p in a.partners.split(",")] if a.partners else None
    mapping = dict(kv.split("=", 1) for kv in a.map.split(",")) if a.map else {}
    out = render(analyze(load(a.export, mapping), a), a); print(out)
    if a.markdown: open(a.markdown, "w").write(out + "\n")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
