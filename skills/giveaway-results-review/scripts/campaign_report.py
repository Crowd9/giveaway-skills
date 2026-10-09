#!/usr/bin/env python3
"""Full report from a campaign data, in the order of Gleam's reporting tabs. Reads a Gleam Actions export (one row per
completed action) as is, and exports from other platforms through --map or the built-in column synonyms, including wide
exports with one column per entry method. No dependencies. Aggregates only: no email, name, IP or row ever prints. Top Entrants show a display name (first
name and last initial) only.

  python3 campaign_report.py export.csv [--impressions N] [--prize-cost USD] [--prize-value USD] [--plan-cost USD] [--benchmark-cpl USD]
                                        [--sends "2026-04-20=Launch email,2026-05-01=Last call"] [--partners host1,host2]
                                        [--markdown report.md]
  python3 campaign_report.py --self-test

Parsing rules. ID is per row: Entrants are keyed by lower-cased Email, with Name as the fallback. When is in the account's
timezone, so every time figure is account time. Status Invalid rows are counted and excluded from engagement metrics.
Details on a refer action holds the referred person's email: that is the referral graph. Actions and Entries are outputs,
never funnel stages. The only funnel is Impressions to Entrants, and Impressions are not in the dataset.
"""
import argparse, collections, csv, datetime as dt, math, os, statistics as st, sys, urllib.parse

# The benchmark columns come from review.py and the action families from gleam_export.py, both beside this file.
# Keep gleam_export.py beside this script so all action counts use the same classifier.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gleam_export import generic_name as _gname, kind as _kind, classify_action
try:
    import review as _bench
except ImportError:
    _bench = None


def reader_unit(v):
    return f"{v:.0%}" if v <= 1 else f"{v:.1f} each"


def bench(metric, value, n, fmt=lambda v: f"{v:,.2f}", key=None, group=None):
    """Two cells: the typical figure for campaigns this size (or the named group) and where this one sits."""
    if n < 100: return "-", "No matching peers: the dataset starts at 100 Entrants"
    if not _bench or value is None: return "-", "no benchmark loaded"
    _bench.PCT = _bench.PCT or _bench.load_pct()
    if not _bench.PCT: return "-", "no benchmark loaded"
    if group is None:
        key = key or "band:" + _bench.band(n); t = _bench.PCT.get("groups", {}).get(key, {}).get(metric); label = f"campaigns of {_bench.band_label(n)}"
    else:
        t = _bench.PCT.get("per_action_uptake", {}).get(group); label = f"campaigns offering {group}"
    if not t: return "-", "no benchmark for this"
    rr = _bench.rank(value, t)
    return fmt(t["p"][9]), f"better than {rr[0]}% of {rr[1]:,} {label}"

# Maintenance: DIRECTORIES, SOCIAL, WEBMAIL and SEARCH are hand-kept host lists used only to label a referrer.
# Add a host when a report shows it under "Other referrers" with a meaningful entrant count. An unknown host is labelled, never dropped.
DIRECTORIES = ("contestgirl", "giveawaybase", "ozbargain", "loquax", "latestdeals", "jeu-concours", "freestuffspot", "aussiecomps", "competitiondatabase",
               "giveawaylisting", "sweepstakes", "sweepsadvantage", "contestcanada", "hotukdeals", "prizefinder", "myoffers", "competitions")
SOCIAL = ("facebook.com", "t.co", "twitter.com", "x.com", "reddit.com", "instagram.com", "tiktok.com", "youtube.com", "youtu.be", "pinterest.com", "discord.com", "discord.gg", "linkedin.com", "threads.net", "threads.com", "bsky.app")
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

# Identity, location and account fields are metadata even when a synonym was not selected.
METADATA_COLUMNS = {name.casefold() for names in SYNONYMS.values() for name in names} | {
    name.casefold() for name in HANDLE_COLS
} | {"id", "user id", "entrant id", "first name", "last name", "full name", "ip", "ip address",
     "address", "postal code", "postcode", "zip", "zip code", "phone", "phone number", "birthday", "age", "gender"}

def resolve_columns(header, mapping):
    """Pick the column for each role from a user mapping (role=Column) or the synonym list. Missing roles are reported, never guessed."""
    mapping = {k.lower(): v for k, v in mapping.items()}
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
    if any(host.lower().rstrip(".") == s or host.lower().rstrip(".").endswith("." + s) for s in SOCIAL): return "Social"
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
def entry_number(value): return int(value) if value == int(value) else value
def pct(a, b): return f"{a / b:.0%}" if b else "-"

def load(path, mapping=None, wide_unit=None, wide_worth=None):
    with open(path, newline="", encoding="utf-8-sig") as f: raw = list(csv.DictReader(f))
    if not raw: sys.exit("empty file")
    cols = resolve_columns(list(raw[0].keys()), mapping or {})
    if "who" not in cols: sys.exit("no column names the Entrant. Pass --map who=<column>")
    rows = []
    if "action" not in cols:
        # Wide cells carry declared units; weights alone never imply one completion.
        if wide_unit not in ("boolean", "completions", "entries"):
            raise ValueError("wide export requires --wide-unit boolean, completions or entries")
        meta = METADATA_COLUMNS | {h.casefold() for h in cols.values()}
        empty = ("", "0", "no", "false")
        acts = [h for h in raw[0] if h.casefold() not in meta and any((r.get(h) or "").strip().casefold() not in empty for r in raw)]
        if not acts: sys.exit("no action column and no per-method columns found. Pass --map action=<column>")
        from decimal import Decimal, InvalidOperation
        worths = {}
        for h in acts:
            try: worth = Decimal(str((wide_worth or {}).get(h, "")))
            except InvalidOperation: raise ValueError(f"supply --wide-worth '{h}=EntriesPerCompletion' from the campaign configuration") from None
            if not worth.is_finite() or worth <= 0 or not math.isfinite(float(worth)) or float(worth) <= 0:
                raise ValueError("wide Entries worth must be finite and positive")
            worths[h] = worth
        for r in raw:
            for h in acts:
                v = (r.get(h) or "").strip().casefold()
                if v in empty: continue
                if wide_unit == "boolean":
                    if v not in ("1", "yes", "true"):
                        raise ValueError("boolean wide cells must be 0, 1, yes, no, true, false or blank")
                    count = Decimal(1)
                else:
                    try: count = Decimal(v)
                    except InvalidOperation: raise ValueError("numeric wide cells must contain finite nonnegative numbers") from None
                    if not count.is_finite() or count < 0:
                        raise ValueError("numeric wide cells must contain finite nonnegative numbers")
                    if wide_unit == "entries": count /= worths[h]
                    if count != count.to_integral_value():
                        raise ValueError("wide values must resolve to a whole number of completions using the declared Entries worth")
                for _ in range(int(count)):
                    rows.append(dict(r, **{"Action": h, "Entries": str(worths[h])}))
        cols["action"] = "Action"; cols["entries"] = "Entries"; wide = True
    else: rows = raw; wide = False
    for r in rows:
        r["Action"] = (r.get(cols["action"]) or "").strip() or "unnamed action"
        r["_who"] = (r.get(cols["who"]) or "").strip().lower()
        sv = str(r.get(cols["status"]) or "").strip().lower() if "status" in cols else ""
        r["_valid"] = sv in ("", "valid", "winner", "approved", "verified", "true", "yes", "1")
        r["_when"] = parse_when(r.get(cols["when"])) if "when" in cols and not wide else None
        try: r["_entries"] = float(r.get(cols.get("entries")) or "")
        except (TypeError, ValueError): r["_entries"] = float("nan")
        r["_unweighted"] = not math.isfinite(r["_entries"]) or r["_entries"] <= 0
        if r["_unweighted"]: r["_entries"] = 0.0
        r["_host"] = host_of(r.get(cols["referrer"])) if "referrer" in cols else ""
        r["_landing"] = landing_kind(r.get(cols["landing"])) if "landing" in cols else "unknown"; r["_channel"] = channel(r["_host"], r["_landing"])
        asset, _, family = classify_action(r["Action"])
        r["_refer"] = asset == "referrals" or family == "share" and "share" in r["Action"].lower() and "@" in (r.get(cols.get("details", ""), "") or "")
        if wide and "details" in cols: r[cols["details"]] = ""
        for role, key in (("country", "Country"), ("city", "City"), ("details", "Details"), ("landing", "Landing Page URL")):
            if role in cols and cols[role] != key: r[key] = r.get(cols[role])
    rows = [r for r in rows if r["_who"]]
    try: math.fsum(r["_entries"] for r in rows)
    except OverflowError: raise ValueError("Entries total exceeds the finite range; reconcile earned weights before export") from None
    load.last = {"columns": cols, "wide": wide, "wide_unit": wide_unit, "missing": [k for k in ("status", "when", "entries", "country", "city", "referrer", "landing", "details") if k not in cols]}
    return rows

def analyze(rows, a):
    valid = [r for r in rows if r["_valid"]]; invalid = [r for r in rows if not r["_valid"]]
    people = collections.defaultdict(list)
    for r in valid: people[r["_who"]].append(r)
    for rs in people.values(): rs.sort(key=lambda r: r["_when"].timestamp() if r["_when"] else 0)
    n = len(people); R = {"base": n, "notes": []}
    if not n: sys.exit("no valid Entrants in export")
    entries = sum(r["_entries"] for r in valid)
    R["topline"] = {"entrants": n, "actions": len(valid), "entries": entry_number(entries), "actions_per_entrant": len(valid) / n, "entries_per_entrant": entries / n,
                    "unweighted_rows": sum(bool(r.get("_unweighted")) for r in rows), "invalid_actions": len(invalid), "invalid_entries": sum(r["_entries"] for r in invalid), "invalid_rate": len(invalid) / len(rows) if rows else 0}
    # engagement distribution
    b = collections.Counter()
    for rs in people.values():
        k = len(rs); b["1"] += k == 1; b["2-5"] += 2 <= k <= 5; b["6-10"] += 6 <= k <= 10; b["11+"] += k > 10
    R["engagement"] = {k: (b[k], b[k] / n) for k in ("1", "2-5", "6-10", "11+")}
    ten_plus = sum(1 for rs in people.values() if len(rs) >= 10)
    # speed
    spans = []; ten = 0; sitting = 0; multi = 0; eligible = 0
    for rs in people.values():
        if len(rs) < 2: continue
        eligible += 1
        if any(r["_when"] is None for r in rs): continue
        ts = [r["_when"] for r in rs]
        multi += 1; span = (max(ts) - min(ts)).total_seconds(); spans.append(span); ten += span <= 600; sitting += span <= 7200
    bonus_all = [r for r in valid if "complet" in r["Action"].lower() and ("bonus" in r["Action"].lower() or "everything" in r["Action"].lower())]
    R["speed"] = {"multi": multi, "eligible": eligible, "missing": eligible - multi, "median_span_min": (med(spans) or 0) / 60, "within_10_min": ten / multi if multi else None, "one_sitting": sitting / multi if multi else None,
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
    referred_by = {}; sharer = collections.defaultdict(set)
    referral_actions = [r for r in valid if r["_refer"]]
    refer_rows = len(referral_actions); referral_people = {r["_who"] for r in referral_actions}; graph_rows = 0
    for r in valid:
        if r["_refer"] and "@" in (r.get("Details") or ""):
            graph_rows += 1; ref = r["Details"].strip().lower(); sharer[r["_who"]].add(ref); referred_by.setdefault(ref, r["_who"])
    referred_entrants = {e for e in referred_by if e in people}
    handles_of = lambda who: [c for c in HANDLE_COLS if any(r.get(c) for r in people.get(who, []))]
    top_sharers = []
    for who, refs in sorted(sharer.items(), key=lambda kv: -len(kv[1]))[:10]:
        joined = [e for e in refs if e in people]; brought = sum(sum(r["_entries"] for r in people[e]) for e in joined)
        one_action = sum(1 for e in joined if len(people[e]) == 1)
        top_sharers.append((display(people[who][0].get("Name")), len(refs), len(joined), entry_number(brought), len(handles_of(who)), one_action))
    R["viral"] = {"refer_rows": refer_rows, "sharers": len(referral_people), "referred_entrants": len(referred_entrants), "referred_share": len(referred_entrants) / n,
                  "referrals_per_sharer": (refer_rows / len(referral_people)) if referral_people else None, "top": top_sharers,
                  "participation": len(referral_people) / n, "referral_conversion": len(referred_entrants) / refer_rows if refer_rows else None,
                  "lift": len(referred_entrants) / (n - len(referred_entrants)) if n > len(referred_entrants) else None,
                  "top_share": (top_sharers[0][1] / refer_rows) if top_sharers and refer_rows else None}
    R["viral"]["graph_rows"] = graph_rows
    R["viral"]["graph_complete"] = graph_rows == refer_rows
    if graph_rows != refer_rows:
        for key in ("referred_entrants", "referred_share", "referral_conversion", "lift", "top_share"):
            R["viral"][key] = None
        R["viral"]["top"] = []
    # geo
    first = {who: rs[0] for who, rs in people.items()}
    R["countries"] = collections.Counter(first[w].get("Country") or "unknown" for w in first).most_common(10)
    cities = collections.Counter((first[w].get("City"), first[w].get("Country")) for w in first if first[w].get("City"))
    R["cities"] = cities.most_common(10)
    # Only complete timestamp histories can support the one-day/returning comparison.
    days_active = collections.Counter(); complete = 0
    for rs in people.values():
        if any(r["_when"] is None for r in rs): continue
        complete += 1
        k = len({r["_when"].date() for r in rs})
        days_active["1" if k == 1 else "2" if k == 2 else "3" if k == 3 else "4+"] += 1
    R["retention_coverage"] = {"complete": complete, "missing": n - complete, "total": n}
    R["retention"] = {k: (days_active[k], days_active[k] / complete) for k in ("1", "2", "3", "4+")} if complete else None
    # heatmap
    heat = collections.Counter((r["_when"].weekday(), r["_when"].hour) for r in valid if r["_when"])
    R["heat"] = heat; R["heat_peak"] = heat.most_common(1)[0] if heat else None
    whens = [r["_when"] for r in valid if r["_when"]]
    if whens:
        start = min(whens); R["first48"] = sum(1 for w in whens if (w - start).total_seconds() <= 172800) / len(whens); R["start"] = start; R["end"] = max(whens)
    # by day: the day each Entrant first acted, and actions that day. The curve the Reporting tab draws, here as a table.
    new_by_day = collections.Counter(rs[0]["_when"].date() for rs in people.values() if rs and rs[0]["_when"])
    act_by_day = collections.Counter(r["_when"].date() for r in valid if r["_when"])
    R["by_day"] = [(d, new_by_day[d], act_by_day[d]) for d in sorted(act_by_day)]
    # traffic: first touch channels, hosts, hosted vs embedded, utm
    ft = collections.Counter(first[w]["_channel"] for w in first); fh = collections.Counter(first[w]["_host"] or "direct or unknown" for w in first)
    ch_actions = collections.Counter(r["_channel"] for r in valid); ch_invalid = collections.Counter(r["_channel"] for r in invalid); ch_all = collections.Counter(r["_channel"] for r in rows)
    avg_apc = len(valid) / n
    ch_apc = {}
    for c in ch_all:
        ppl = [w for w in first if first[w]["_channel"] == c]; ch_apc[c] = (sum(len(people[w]) for w in ppl) / len(ppl)) / avg_apc if ppl else None
    R["channels"] = [(c, ft[c], ft[c] / n, ch_actions[c], ch_apc[c], ch_invalid[c] / ch_all[c] if ch_all[c] else 0) for c in sorted(ch_all, key=lambda c: -ft[c])]
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
    R["top_entrants"] = [(display(rs[0].get("Name")), len(rs), entry_number(sum(r["_entries"] for r in rs)), len(sharer.get(who, ())) if R["viral"]["graph_complete"] else "unavailable", len({r["_when"].date() for r in rs}) if all(r["_when"] for r in rs) else "unavailable", len(handles_of(who))) for who, rs in top]
    # promotions
    R["sends"] = []
    coverage_start = getattr(a, "coverage_start", None)
    coverage_end = getattr(a, "coverage_end", None)
    if isinstance(coverage_start, str): coverage_start = dt.date.fromisoformat(coverage_start)
    if isinstance(coverage_end, str): coverage_end = dt.date.fromisoformat(coverage_end)
    if bool(coverage_start) != bool(coverage_end): raise ValueError("supply both --coverage-start and --coverage-end")
    if coverage_start and coverage_start > coverage_end: raise ValueError("coverage start must be on or before coverage end")
    if a.sends:
        byday = collections.Counter(w.date() for w in whens); newby = collections.Counter(first[w]["_when"].date() for w in first if first[w]["_when"])
        for item in a.sends.split(","):
            d, _, label = item.partition("="); day = dt.date.fromisoformat(d.strip())
            covered = (coverage_start is not None and coverage_start <= day - dt.timedelta(days=7)
                       and coverage_end >= day + dt.timedelta(days=1) and len(whens) == len(valid))
            after = sum(byday[day + dt.timedelta(days=i)] for i in range(2)) if covered else None
            newa = sum(newby[day + dt.timedelta(days=i)] for i in range(2)) if covered else None
            base = sum(byday[day - dt.timedelta(days=i)] for i in range(1, 8)) / 7 if covered else None
            R["sends"].append((label.strip() or d, day.isoformat(), after, newa, (after / 2) / base if base else None))
    # People are deduplicated across subscription Actions. Benchmarks still use completions.
    emails = sum(1 for rs in people.values() if any(_kind(r["Action"]) == "emails" for r in rs))
    R["email_subscribers"] = emails
    R["prize_value"] = getattr(a, "prize_value", None)
    # Stated retail value is never substituted for the organizer's actual cost.
    prize_cost = getattr(a, "prize_cost", None)
    if prize_cost is not None or a.plan_cost is not None:
        cost = (prize_cost or 0) + (a.plan_cost or 0)
        R["roi"] = {"cost": cost, "per_entrant": cost / n, "per_entry": cost / entries if entries else None, "per_email": cost / emails if emails else None, "emails": emails,
                    "lead_value": (a.benchmark_cpl * emails) if a.benchmark_cpl and emails else None}
    R["ten_plus"] = ten_plus
    return R

def retention_text(R):
    coverage = R["retention_coverage"]; ret = R["retention"]
    if ret is None:
        return f"Retention unavailable: {coverage['missing']:,} Entrants lack complete usable timestamps."
    text = "Retention by distinct active days: " + ", ".join(f"{k}: {v[0]:,} ({v[1]:.0%})" for k, v in ret.items())
    text += f". {1 - ret['1'][1]:.0%} returned on a later day among {coverage['complete']:,} Entrants with complete usable timestamps."
    if coverage["missing"]:
        text += f" Excludes {coverage['missing']:,} of {coverage['total']:,} Entrants with missing or unusable timestamps; this subset may not represent all Entrants."
    return text


def viral_text(V):
    text = f"Referral completions {V['refer_rows']:,}, sharers {V['sharers']:,} ({V['participation']:.0%} of entrants)"
    if V["referrals_per_sharer"] is not None: text += f", referrals per sharer {V['referrals_per_sharer']:.1f}"
    text += f". Referral relationships available for {V['graph_rows']:,} of {V['refer_rows']:,} completions."
    if not V["graph_complete"]:
        return text + " Referred Entrants, referral conversion, viral lift and top-sharer graph measures are unavailable because referral relationships are incomplete."
    text += f" referred entrants who entered {V['referred_entrants']:,} ({V['referred_share']:.0%} of entrants)"
    if V["referral_conversion"] is not None: text += f", share of referrals who joined {V['referral_conversion']:.0%} (referred entrants divided by referral completions, no click data)"
    if V["lift"] is not None: text += f", viral lift +{V['lift']:.0%} (referred divided by non-referred entrants)"
    return text + "."


def insights(R):
    """The deterministic findings, each checkable against a table in the report."""
    T = R["topline"]; n = R["base"]
    ins = []
    if T["unweighted_rows"]: ins.append(f"{T['unweighted_rows']:,} rows without a valid Entries value, counted at zero. Reconcile earned weights before a draw.")
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
    return ins


def render(R, a):
    L = []; w = L.append; T = R["topline"]; n = R["base"]
    info = getattr(load, "last", None)
    if info:
        w("Columns read: " + ", ".join(f"{k} = {v}" for k, v in info["columns"].items()) + (", wide export with one column per entry method" if info["wide"] else "") + (". Not in this file: " + ", ".join(info["missing"]) + ", so those sections are thin or omitted." if info["missing"] else "."))
    if info and info["wide"]:
        w(f"Wide cell unit: {info['wide_unit']}. Entries use declared worth per completion. Summary dates cannot establish action times, so timing and speed are unavailable. Referral relationships require individual action rows.")
    w(f"# Campaign report\n\nBase: {n:,} export entrants (unique valid emails). Times are the account timezone. Impressions are not in the dataset" + (f", {a.impressions:,} supplied from the Reporting tab." if a.impressions else ", so there is no Impressions-to-entrants funnel here."))
    w("\n## Overview\n")
    def row(label, shown, metric=None, value=None, fmt=lambda v: f"{v:,.2f}"):
        typ, where = bench(metric, value, n, fmt) if metric else ("-", "no benchmark for this")
        return f"| {label} | {shown} | {typ} | {where} |"
    w("| Metric | Value | Typical, campaigns your size | Where this campaign sits |\n|---|---|---|---|\n"
      + "\n".join([row("Users", f"{n:,}", "contestants", n, lambda v: f"{v:,.0f}"), row("Actions completed", f"{T['actions']:,}"), row("Entries", f"{T['entries']:,}", "entries", T["entries"], lambda v: f"{v:,.0f}"),
                   row("Actions each", f"{T['actions_per_entrant']:.1f}", "actions_per_contestant", T["actions_per_entrant"], lambda v: f"{v:.1f}"),
                   row("Entries each", f"{T['entries_per_entrant']:.1f}", "entries_per_entrant", T["entries_per_entrant"], lambda v: f"{v:.1f}"),
                   row("Invalid actions", f"{T['invalid_actions']:,} ({T['invalid_rate']:.1%} of rows)")]
                  + ([row("Conversion Rate", f"{n / a.impressions:.1%}", "conversion", n / a.impressions, lambda v: f"{v:.0%}")] if a.impressions else [])))
    w("\nTypical is the median of campaigns in the same size band in Gleam campaign data, and the rank is the share of that band this campaign beats. Engagement depth, speed, timing, traffic mix, audience and retention have no benchmark in the data, so those sections describe this campaign alone.")
    E = R["engagement"]; w("\nEngagement by actions per Entrant: " + ", ".join(f"{k}: {v[0]:,} ({v[1]:.0%})" for k, v in E.items()) + ".")
    S = R["speed"]
    if S["multi"]:
        w(f"Speed: among {S['multi']:,} of {S['eligible']:,} multi-action Entrants with complete usable timestamps, typical first-to-last span {S['median_span_min']:.0f} minutes, {S['within_10_min']:.0%} done within 10 minutes, {S['one_sitting']:.0%} in one sitting (under 2 hours)." + (f" Completed everything: {S['completed_everything'][0]:,} entrants ({S['completed_everything'][1]:.0%})." if S["completed_everything"] else ""))
    elif S["eligible"]:
        w("Speed unavailable: no multi-action Entrants have complete usable timestamps.")
    if S["missing"]:
        w(f"Speed excludes {S['missing']:,} of {S['eligible']:,} multi-action Entrants with missing or unusable timestamps; the covered subset may not represent all Entrants.")
    ins = insights(R); V = R["viral"]
    w("\nInsights:\n" + "\n".join(f"- {i}" for i in ins))
    referred = f"{V['referred_entrants']:,}" if V["graph_complete"] else "unavailable (referral relationships incomplete)"
    w(f"\nEntrant journey: entered {n:,} (100%), completed more than one action {n - E['1'][0]:,} ({(n - E['1'][0]) / n:.0%}), shared {V['sharers']:,} ({V['participation']:.0%}), referred new entrants (an output per sharer, never a stage): {referred} referred entrants.")
    if R.get("by_day"):
        peak = max(R["by_day"], key=lambda t: t[1])
        w(f"\nBy day (account time), new Entrants and actions. Peak day for new Entrants {peak[0].isoformat()} with {peak[1]:,}.")
        w("\nDay | New Entrants | Actions\n---|---|---")
        for d, ne, ac in R["by_day"]: w(f"{d.isoformat()} | {ne:,} | {ac:,}")
    if R["heat_peak"]:
        (dw, hr), cnt = R["heat_peak"]; w(f"\nActivity peak: {DAYS[dw]} {hr:02d}:00 account time with {cnt:,} actions. A single campaign's heatmap follows its launch timing.")
        w("\nHour | " + " | ".join(DAYS) + "\n---|" + "---|" * 7)
        for h in range(24): w(f"{h:02d} | " + " | ".join(f"{R['heat'][(d, h)]:,}" if R["heat"][(d, h)] else "" for d in range(7)))
    if R["sends"]:
        w("\nPromotional sends (send date and following account-time day against the preceding 7-day daily baseline, never a causal claim). Both windows require confirmed complete export coverage via --coverage-start and --coverage-end, inclusive full dates. Observed activity does not establish coverage.\n\n| Send | Date | Actions in 2 days | New Entrants in 2 days | Lift |\n|---|---|---|---|---|")
        for label, day, actions, entrants, lift in R["sends"]:
            activity = f"{actions:,} | {entrants:,}" if actions is not None else "unavailable | unavailable"
            comparison = f"{lift:.1f}x" if lift is not None else "unavailable (incomplete coverage)" if actions is None else "unavailable (zero baseline)"
            w(f"| {label} | {day} | {activity} | {comparison} |")
    w(f"\nUnique email subscribers: {R['email_subscribers']:,} (people with a valid subscription Action).")
    if R.get("prize_value") is not None:
        w(f"\nStated Prize value: {R['prize_value']:,.2f}. This is the advertised value, not actual spending.")
    if R.get("roi"):
        r = R["roi"]; per_entry = format(r["per_entry"], ".4f") if r["per_entry"] is not None else "unavailable"
        w(f"\nCost per result on the supplied actual costs (Prize and plan inputs total {r['cost']:,.0f}): {r['per_entrant']:.2f} per entrant, {per_entry} per entry" + (f", {r['per_email']:.2f} per email subscriber ({r['emails']:,} subscribers)" if r["per_email"] else "") + (f". Lead-value proxy at the benchmark cost per lead of {a.benchmark_cpl:.2f} that the user supplied: {r['lead_value']:,.0f}. That is what the same subscribers would cost through another channel, an assumption priced at the user's own figure." if r["lead_value"] else "."))
        w("A real revenue figure comes from joining Entrant email against store orders over a fixed window and summing order value. The dataset carries no order data, so nothing here is revenue.")
        w("Only supplied costs are included. Add any missing Prize, plan, promotion and other costs before treating this as total campaign spending.")
    else: w("\nCost per result needs actual Prize cost or plan cost (--prize-cost, --plan-cost, optional --benchmark-cpl). Stated Prize value alone does not establish spending.")
    w("\n## Traffic\n\nFirst-touch channel per valid Entrant (earliest valid row's referrer). Actions and invalid rates use each row's own source, including sources with no valid Entrants. Depth is unavailable without valid first-touch Entrants. Email clicks arrive as webmail or direct and are undercounted.\n\n| Channel | Entrants | Share | Actions | Depth vs average | Invalid rate |\n|---|---|---|---|---|---|")
    for c in R["channels"]:
        depth = f"{c[4]:.2f}x" if c[4] is not None else "unavailable"
        w(f"| {c[0]} | {c[1]:,} | {c[2]:.0%} | {c[3]:,} | {depth} | {c[5]:.1%}{' (2x campaign rate or more)' if c[5] >= 2 * R['invalid_rate_all'] and c[5] > 0 else ''} |")
    w("\nRaw referrers (first touch):\n\n| Host | Entrants |\n|---|---|" + "".join(f"\n| {h} | {k:,} |" for h, k in R["hosts"]))
    w("\nLanding page at first touch: " + ", ".join(f"{k} {v:,} ({v / n:.0%})" for k, v in R["landing"]) + ". gleam.io/KEY/slug is the hosted page, gleam.io/giveaways/KEY is the directory listing, any other host is an embed.")
    if R.get("featured"):
        F = R["featured"]; w(f"\nFeatured on gleam.io/giveaways: {F['entrants']:,} entrants ({F['share']:.0%}) came from browsing the directory (landed on the listing with gleam.io as the referrer)" + (f", at {F['depth']:.2f}x the average actions per entrant" if F["depth"] else "") + f". {F['landed']:,} entrants ({F['landed_share']:.0%}) landed on the listing URL from any source, at {F['landed_depth']:.2f}x, since the listing link also gets shared by aggregators, email and social. Listing traffic is people browsing giveaways, so read its depth and email signups apart from your own channels.")
    if R["utm"]: w("\nUTM rollup (first touch):\n\n| Source | Medium | Campaign | Entrants |\n|---|---|---|---|" + "".join(f"\n| {s} | {m} | {c} | {k:,} |" for (s, m, c), k in R["utm"]))
    if R.get("partners"): w("\nPartners (by referrer host): " + ", ".join(f"{p} {k:,} entrants ({sh:.1%})" for p, k, sh in R["partners"]) + ". Host substring matches can overlap, so do not sum partner rows. Read tagged email traffic in the separate UTM rollup.")
    else: w("\nPartner contribution needs --partners with referrer-host substrings. For tagged email traffic, read the separate UTM rollup. Overlapping host matches may count the same Entrant in multiple partner rows, so do not sum them.")
    w("\n## Entry methods\n\n| Action | Completions | Entrants | Share of actions | Completion rate | Typical, campaigns offering it | Where it sits | Typical seconds | Invalid |\n|---|---|---|---|---|---|---|---|---|")
    for act, comp, uniq, share, rate, sec, inv in R["actions"]:
        flag = " (slow)" if sec and sec > 120 else ""
        g = _gname(act) if _gname else None
        typ, where = bench(None, comp / n, n, reader_unit, group=g) if g else ("-", "no matching group")
        w(f"| {act} | {comp:,} | {uniq:,} | {share:.0%} | {rate:.0%} | {typ} | {where} | {f'{sec:.0f}{flag}' if sec is not None else '-'} | {inv:,} |")
    w("\nTypical seconds is the gap from the Entrant's previous action, in-session gaps under 30 minutes only. Visits usually run a few seconds, referrals minutes.")
    w("\n## Viral\n\n" + viral_text(V))
    rtyp, rwhere = bench("referrals_per_contestant", V["refer_rows"] / n, n, lambda v: f"{v:.2f}")
    w(f"\nReferral completions per Entrant: {V['refer_rows'] / n:.2f} here, {rtyp} typical for campaigns your size, {rwhere}.")
    if V["top"]:
        w("\n| Sharer | Referral completions | Referred who entered | Entries brought | Connected accounts | Referred doing one action |\n|---|---|---|---|---|---|")
        for s in V["top"]:
            tell = " (signal: no connected accounts, outsized referrals)" if s[4] == 0 and s[1] >= 10 else ""
            w(f"| {s[0]}{tell} | {s[1]:,} | {s[2]:,} | {s[3]:,} | {s[4]} | {s[5]:,} |")
        w("\nSignals, never verdicts: a sharer with many referrals, no connected accounts and referred Entrants who mostly do one action deserves a look before any Prize.")
    w("\n## Audience\n\n| Country | Entrants | Share |\n|---|---|---|" + "".join(f"\n| {c} | {k:,} | {k / n:.0%} |" for c, k in R["countries"]))
    if R["cities"]: w("\n| City | Entrants |\n|---|---|" + "".join(f"\n| {c}, {co} | {k:,} |" for (c, co), k in R["cities"]))
    if R["handles"]: w("\nConnected accounts: " + ", ".join(f"{c} {v:.0%}" for c, v in R["handles"]) + ".")
    w("\n" + retention_text(R))
    w("\nMost engaged Entrants:\n\n| Entrant | Actions | Entries | Referred | Days active | Connected accounts |\n|---|---|---|---|---|---|" + "".join(f"\n| {t[0]} | {t[1]} | {t[2]:,} | {t[3]} | {t[4]} | {t[5]} |" for t in R["top_entrants"]))
    w("""
## Outcomes

Nothing in this section is in the dataset. Pull each figure from the email provider and the store, then record it beside this report.

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
    class A: impressions = None; prize_cost = 100.0; prize_value = 1000.0; plan_cost = 50.0; benchmark_cpl = 2.0; sends = "2026-05-01=Launch"; partners = ["contestgirl"]
    R = analyze(load(p), A)
    assert R["topline"]["entrants"] == 2 and R["topline"]["invalid_actions"] == 1 and R["viral"]["referred_entrants"] == 1 and R["viral"]["sharers"] == 1, R["topline"]
    assert landing_kind("https://gleam.io/giveaways/UQW3q") == "Gleam giveaways directory" and landing_kind("https://gleam.io/UQW3q/apple-airpods") == "hosted page on gleam.io" and landing_kind("https://shop.example.com/win") == "embedded on shop.example.com"
    assert R["channels"][0][0] in ("Email (webmail)", "Competition directories") and R["utm"][0][1] == 1 and R["roi"]["emails"] == 1 and R["partners"][0][1] == 1, (R["channels"], R["utm"], R["roi"])
    out = render(R, A); assert "## Viral" in out and "Ann L." in out and "a@example.com" not in out and "Toronto, Canada" in out, out[:300]
    assert "| Users | 2 |" in out and "Typical, campaigns your size" in out and "starts at 100 Entrants" in out and "better than" not in out, out[:900]
    assert "Impressions are not in the dataset" in out and "so there is no Impressions-to-entrants funnel here" in out, out[:400]
    class C: impressions = 10; prize_value = None; plan_cost = None; benchmark_cpl = None; sends = None; partners = None
    out2 = render(analyze(load(p), C), C)
    assert "| Conversion Rate | 20.0% |" in out2 and "supplied from the Reporting tab" in out2 and "Views" not in out2 and "share who entered" not in out2.lower(), out2[:400]
    q = os.path.join(d, "wide.csv")
    with open(q, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email Address", "Date", "Country", "Follow on Instagram", "Join newsletter", "Share with friends"])
        wr.writerow(["x@example.com", "2026-05-01 09:00:00", "Ireland", "1", "1", "0"]); wr.writerow(["y@example.com", "2026-05-01 09:30:00", "Ireland", "1", "0", "0"])
    class B: impressions = None; prize_value = None; plan_cost = None; benchmark_cpl = None; sends = None; partners = None
    R2 = analyze(load(q, {}, "boolean", {"Follow on Instagram": 1, "Join newsletter": 1}), B); assert R2["topline"]["entrants"] == 2 and R2["topline"]["actions"] == 3 and load.last["wide"], R2["topline"]
    assert "referrer" in load.last["missing"] and "Follow on Instagram" in render(R2, B)
    fractional = load(p)
    for r in fractional: r["_entries"] = 1.25
    fractional[3]["_entries"] = 1.5
    fr = analyze(fractional, B)
    assert fr["topline"]["entries"] == 5.25 and fr["top_entrants"][0][2] == 3.75, fr["top_entrants"]
    assert fr["viral"]["top"][0][3] == 1.5, fr["viral"]["top"]
    assert fr["topline"]["invalid_entries"] == 1.25, fr["topline"]
    fractional[2]["Details"] = "absent@example.com"
    assert analyze(fractional, B)["viral"]["top"][0][3] == 0
    for empty in ([], [r for r in fractional if not r["_valid"]]):
        try: analyze(empty, B)
        except SystemExit as exc: assert str(exc) == "no valid Entrants in export", exc
        else: raise AssertionError("empty campaign must explain why it cannot be reported")
    assert resolve_columns(["Email", "Action", "Custom Worth"], {"Entries": "Custom Worth"})["entries"] == "Custom Worth"
    # Small exports never acquire a ranking, including action-family comparisons.
    for count in (1, 30, 99):
        assert bench("contestants", count, count)[0] == "-"
        assert "starts at 100" in bench(None, 1, count, group="Email")[1]
    assert "better than" in bench("contestants", 100, 100)[1]
    # Metadata must not become actions in wide exports.
    with open(q, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Name", "First Name", "ID", "IP Address", "Twitter", "Subscribe to newsletter"])
        wr.writerow(["x@example.com", "Example Person", "Example", "123", "unknown", "@example", "yes"])
    wide_rows = load(q, wide_unit="boolean", wide_worth={"Subscribe to newsletter": 1})
    assert len(wide_rows) == 1 and wide_rows[0]["Action"] == "Subscribe to newsletter"
    assert wide_rows[0]["_entries"] == 1
    # Invalid or missing weights retain actions at zero Entries, like gleam_export.py.
    for value in ("", "0", "-1", "NaN", "inf", "bad", "1.25"):
        with open(q, "w", newline="") as f:
            wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries"])
            wr.writerow(["x@example.com", "Subscribe", value])
        weighted = load(q); report = analyze(weighted, B)
        assert report["topline"]["entries"] == (1.25 if value == "1.25" else 0)
        assert report["topline"]["unweighted_rows"] == (0 if value == "1.25" else 1)
    with open(q, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action"]); wr.writerow(["x@example.com", "Subscribe"])
    assert analyze(load(q), B)["topline"]["unweighted_rows"] == 1
    assert "unavailable per entry" in render(analyze(load(q), A), A)
    with open(q, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries"])
        wr.writerows([["x@example.com", "Subscribe", "1e308"], ["y@example.com", "Subscribe", "1e308"]])
    try: load(q)
    except ValueError as exc: assert "finite range" in str(exc)
    else: raise AssertionError("overflowing Entry weights accepted")
    repeated = load(p)
    repeated.append(dict(repeated[2]))
    repeated.append(dict(repeated[2], Details="absent@example.com"))
    referral_report = render(analyze(repeated, B), B)
    assert "Referral completions per Entrant: 1.50" in referral_report
    assert "referred entrants who entered 1 (50% of entrants)" in referral_report
    assert "Referred Entrants as a share of all Entrants" not in referral_report
    # Missing histories never become confirmed one-day participants.
    for timestamps in ((None, None), ("bad-date", "bad-date"), ("2026-05-01 10:00:00", "bad-date"),
                       ("2026-05-01 10:00:00", "2026-05-02 10:00:00")):
        with open(q, "w", newline="") as f:
            wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries"] + (["When"] if timestamps[0] is not None else []))
            for i, timestamp in enumerate(timestamps):
                wr.writerow([f"person{i}@example.com", "Subscribe to our newsletter", 1] + ([timestamp] if timestamp is not None else []))
        dated = analyze(load(q), B); rendered = render(dated, B)
        count = sum(bool(parse_when(t)) for t in timestamps if t)
        assert dated["retention_coverage"]["complete"] == count
        if not count: assert "Retention unavailable" in rendered and "returned on a later day" not in rendered
        elif count == 1: assert "Excludes 1 of 2 Entrants" in rendered and dated["retention"]["1"] == (1, 1.0)
        else: assert dated["retention"]["1"] == (2, 1.0)
    complete_history = load(p)
    complete_history[1]["_when"] += dt.timedelta(days=1)
    returned = analyze(complete_history, B)
    assert returned["retention"]["2"] == (1, 0.5) and "50% returned on a later day" in render(returned, B)
    # One undated action makes its participant's otherwise dated history incomplete.
    history = load(p); history[0]["_when"] = None
    assert analyze(history, B)["retention_coverage"] == {"complete": 1, "missing": 1, "total": 2}
    for titles, expected in ((("Subscribe to our YouTube channel",) * 2, 0),
                             (("Subscribe to our newsletter",) * 2, 2),
                             (("Subscribe to our YouTube channel", "Subscribe to our newsletter"), 1)):
        with open(q, "w", newline="") as f:
            wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries"])
            for i, title in enumerate(titles): wr.writerow([f"person{i}@example.com", title, 1])
        report = analyze(load(q), A)
        assert report["roi"]["emails"] == expected
        assert report["roi"]["per_email"] == (150 / expected if expected else None)
    # Multiple subscription Actions count one person for acquisition costs.
    with open(q, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries"])
        wr.writerow(["one@example.com", "Subscribe to our newsletter", 1])
        wr.writerow(["one@example.com", "Subscribe to partner newsletter", 1])
        for i in range(9): wr.writerow([f"other{i}@example.com", "Entry Confirmed", 1])
    class Costs(A): prize_cost = 100; prize_value = 1000; plan_cost = None
    report = analyze(load(q), Costs)
    assert report["email_subscribers"] == report["roi"]["emails"] == 1
    assert sum(comp for act, comp, *_ in report["actions"] if _kind(act) == "emails") == 2
    assert report["roi"]["per_entrant"] == 10 and report["roi"]["per_email"] == 100
    rendered = render(report, Costs)
    assert "Stated Prize value: 1,000.00" in rendered and "10.00 per entrant" in rendered
    # Legacy --prize-value remains accepted but never becomes spending.
    class ValueOnly(B): prize_value = 1000
    legacy = analyze(load(q), ValueOnly)
    assert "roi" not in legacy and "Stated Prize value alone does not establish spending" in render(legacy, ValueOnly)
    # Invalid-only sources stay visible without gaining valid people or depth.
    with open(q, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries", "Status", "Referring URL", "Landing Page URL"])
        wr.writerows([["valid@example.com", "Visit", 1, "Valid", "", "https://example.org/?utm_source=partnera"],
                      ["invalid@example.com", "Visit", 1, "Invalid", "https://facebook.com/", ""],
                      ["host@example.com", "Visit", 1, "Valid", "https://partner.example.org/", ""]])
    class Partners(B): partners = ["partnera", "partner.example.org", "example.org"]
    traffic = analyze(load(q), Partners)
    social = next(c for c in traffic["channels"] if c[0] == "Social")
    assert social[1:] == (0, 0, 0, None, 1.0), traffic["channels"]
    assert traffic["base"] == 2 and sum(c[1] for c in traffic["channels"]) == 2
    text = render(traffic, Partners)
    assert "| Social | 0 | 0% | 0 | unavailable | 100.0%" in text
    assert not any("Social" in line for line in insights(traffic))
    assert traffic["partners"] == [("partnera", 0, 0), ("partner.example.org", 1, 0.5), ("example.org", 1, 0.5)]
    assert traffic["utm"] == [(("partnera", "-", "-"), 1)]
    assert "do not sum partner rows" in text and "separate UTM rollup" in text
    import contextlib, io
    help_output = io.StringIO()
    with contextlib.redirect_stdout(help_output):
        try: main(["--help"])
        except SystemExit as exc: assert exc.code == 0
    assert "referrer-host substrings" in help_output.getvalue() and "referrer hosts or UTM values" not in help_output.getvalue()
    # Host suffixes cannot turn merchant domains into social traffic.
    for host in ("walmart.com", "best.com", "notfacebook.com", "facebook.com.example.org"):
        assert channel(host) == "Other referrers", host
    for host in ("t.co", "m.facebook.com", "www.reddit.com", "X.COM", "www.instagram.com"):
        assert channel(host) == "Social", host
    # Referral completions survive missing, blank and partial graph data.
    for details in (None, ("", ""), ("b@example.com", "")):
        with open(q, "w", newline="") as f:
            wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries"] + (["Details"] if details is not None else []))
            for i in range(2): wr.writerow([f"person{i}@example.com", "Refer Friends", 1] + ([details[i]] if details is not None else []))
        partial = analyze(load(q), B); viral = partial["viral"]
        assert viral["refer_rows"] == 2 and viral["sharers"] == 2 and viral["referrals_per_sharer"] == 1
        assert viral["graph_rows"] == (1 if details and details[0] else 0)
        assert viral["referred_entrants"] is None and viral["lift"] is None and viral["top"] == []
        assert "relationships are incomplete" in render(partial, B)
        assert all(row[3] == "unavailable" for row in partial["top_entrants"])
    # Constant activity produces no lift only when both full windows are confirmed.
    with open(q, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries", "When"])
        for day in range(1, 10):
            for i in range(8): wr.writerow([f"person{i}@example.com", "Visit", 1, f"2026-05-{day:02d} 12:00:00"])
    class Covered(B): sends = "2026-05-08=Reminder"; coverage_start = "2026-05-01"; coverage_end = "2026-05-09"
    constant = load(q)
    assert analyze(constant, Covered)["sends"][0][4] == 1.0
    class Early(Covered): sends = "2026-05-02=Early reminder"
    class ShortPost(Covered): coverage_end = "2026-05-08"
    class Unconfirmed(B): sends = Covered.sends
    for args in (Early, ShortPost, Unconfirmed):
        report = analyze(constant, args)
        assert report["sends"][0][2:] == (None, None, None)
        assert "unavailable (incomplete coverage)" in render(report, args)
    constant[0]["_when"] = None
    assert analyze(constant, Covered)["sends"][0][4] is None
    # Shared referral classification keeps program visits out of the graph.
    for title, expected in (("Join the Referral Program:", 0), ("Refer Friends", 1), ("Share with friends", 1)):
        with open(q, "w", newline="") as f:
            wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries", "Details"])
            wr.writerow(["a@example.com", title, 1, "b@example.com"])
        assert analyze(load(q), B)["viral"]["refer_rows"] == expected
    # A missing third timestamp invalidates an otherwise one-minute span.
    with open(q, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries", "When"])
        for timestamp in ("2026-05-01 10:00:00", "2026-05-01 10:01:00", ""):
            wr.writerow(["a@example.com", "Visit", 1, timestamp])
    partial_rows = load(q); partial_speed = analyze(partial_rows, B)
    assert partial_speed["speed"]["multi"] == 0 and partial_speed["speed"]["missing"] == 1
    assert "Speed unavailable" in render(partial_speed, B)
    assert "done within 10 minutes" not in render(partial_speed, B)
    full_speed = analyze(partial_rows[:2], B)
    assert full_speed["speed"]["within_10_min"] == 1 and full_speed["speed"]["median_span_min"] == 1
    assert "1 of 1 multi-action Entrants with complete usable timestamps" in render(full_speed, B)
    mixed = partial_rows + [dict(r, _who="b@example.com") for r in partial_rows[:2]]
    assert "Speed excludes 1 of 2" in render(analyze(mixed, B), B)
    # Declared wide units retain repeats, weights and unique participants.
    for unit, values, worth, actions, entries in (
        ("boolean", ("true", "yes"), 5, 2, 10),
        ("completions", ("10", "2"), 3, 12, 36),
        ("entries", ("10", "2.5"), 2.5, 5, 12.5)):
        with open(q, "w", newline="") as f:
            wr = csv.writer(f); wr.writerow(["Email", "Daily visit", "Unused", "When"])
            for i, value in enumerate(values): wr.writerow([f"p{i}@example.com", value, "false", "2026-05-01 10:00:00"])
            for i, zero in enumerate(("0", "no", "false", "")): wr.writerow([f"zero{i}@example.com", zero, "0", ""])
        wide_rows = load(q, wide_unit=unit, wide_worth={"Daily visit": worth})
        report = analyze(wide_rows, B)
        assert report["topline"]["entrants"] == 2 and report["topline"]["actions"] == actions
        assert report["topline"]["entries"] == entries and report["actions"][0][1:3] == (actions, 2)
        assert report["speed"]["multi"] == 0 and not report["by_day"]
        if unit == "completions": assert report["engagement"]["6-10"] == (1, 0.5)
    for unit, worth in ((None, {}), ("entries", {}), ("entries", {"Daily visit": 3}), ("boolean", {"Daily visit": 1})):
        try: load(q, wide_unit=unit, wide_worth=worth)
        except ValueError: pass
        else: raise AssertionError("ambiguous wide units or invalid counts accepted")
    saved_pct, saved_load = _bench.PCT, _bench.load_pct
    try:
        _bench.PCT = None; _bench.load_pct = lambda: None
        assert bench("contestants", 100, 100) == ("-", "no benchmark loaded")
    finally: _bench.PCT, _bench.load_pct = saved_pct, saved_load
    print("self-test passed"); return 0

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export", nargs="?"); ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--impressions", type=int); ap.add_argument("--prize-cost", type=float, help="actual Prize cost paid by the organizer"); ap.add_argument("--prize-value", type=float, help="stated retail Prize value, excluded from spending"); ap.add_argument("--plan-cost", type=float); ap.add_argument("--benchmark-cpl", type=float)
    ap.add_argument("--sends", help='comma list of date=label, e.g. "2026-04-20=Launch email,2026-05-01=Last call"'); ap.add_argument("--partners", help="comma list of referrer-host substrings identifying partners (matches may overlap). For tagged email traffic, read the separate UTM rollup")
    ap.add_argument("--coverage-start", type=dt.date.fromisoformat, help="first confirmed complete export day, YYYY-MM-DD in account time")
    ap.add_argument("--coverage-end", type=dt.date.fromisoformat, help="last confirmed complete export day, inclusive, YYYY-MM-DD in account time")
    ap.add_argument("--markdown", help="write the report here as well as printing it")
    ap.add_argument("--map", help="column mapping for exports from other platforms, e.g. \"who=Email Address,action=Entry Type,Entries=Points,when=Date,status=Verified,referrer=Source\"")
    ap.add_argument("--wide-unit", choices=("boolean", "completions", "entries"), help="required interpretation of per-method wide cells")
    ap.add_argument("--wide-worth", help="required Entries per completion for each populated wide method, e.g. 'Daily visit=1,Join newsletter=5'")
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    if not a.export: ap.error("export path required")
    a.partners = [p.strip() for p in a.partners.split(",")] if a.partners else None
    mapping = dict(kv.split("=", 1) for kv in a.map.split(",")) if a.map else {}
    try:
        worth = dict(kv.split("=", 1) for kv in a.wide_worth.split(",")) if a.wide_worth else {}
        out = render(analyze(load(a.export, mapping, a.wide_unit, worth), a), a)
    except ValueError as exc:
        ap.error(str(exc))
    print(out)
    if a.markdown:
        with open(a.markdown, "w") as resource:
            resource.write(out + "\n")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
