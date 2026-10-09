#!/usr/bin/env python3
"""Build the results dashboard as one HTML file, from the export and the words the reviewer wrote.

  python3 dashboard.py export.csv --words words.json --out dashboard.html [--impressions N] [--plan-cost USD]
                       [--prize-cost USD] [--prize-value USD] [--vertical NAME] [--first-campaign] [--site site.json]
  python3 dashboard.py --self-test

Every figure on the page comes from campaign_report.py and review.py run on the export, so the page and the
written review agree by construction. The words come from words.json, written by the reviewer after reading the
scripts' output:

  {"assumptions": "one line", "verdict": "two or three sentences", "pills": [{"kind": "good", "text": "..."}, ...],
   "changes": [{"eyebrow": "Entry list", "title": "...", "target": "3,711", "target_note": "addresses ...", "body": "...", "who": "..."}],
   "caveats": ["..."], "question": "the one closing question"}

Without --words the page still builds, with each slot marked for the reviewer to fill. site.json is the site block
the Reporting tab sends (name, url, headerLogo, headerColour, elementsColour, backgroundColour); set values theme
the page and unset ones leave the Gleam default. Levers are arithmetic on the campaign's own counts and lookups in
the references, never a forecast, and every card says so.

No dependencies. Aggregates and display names only: no email, IP or full name reaches the page.
"""
import argparse, csv, html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import campaign_report as CR, review as RV
from gleam_export import generic_name, kind

REFS = os.path.join(HERE, "..", "references")
SIBLING_PRIZE = os.path.join(HERE, "..", "..", "giveaway-prize-picker", "references", "decision-criteria.md")
FAMILY_COLOUR = {"visit": "visit", "email": "email", "follow": "follow", "share": "share", "content": "content"}


def esc(x): return html.escape(str(x), quote=True)
def script_json(value):
    """Serialize data without introducing HTML script boundaries or JS line separators."""
    return json.dumps(value).translate({ord(c): f"\\u{ord(c):04x}" for c in "<>&\u2028\u2029"})


def n(x): return f"{x:,.0f}"
def pct(x): return f"{x:.0%}"
def reader_unit(v): return f"{v:.0%}" if v <= 1 else f"{v:.1f} each"


def md_table(path, marker=None, header_starts=None):
    """Rows of the generated table under a marker, or the first table whose header starts with a phrase."""
    if not os.path.exists(path): return []
    with open(path, encoding="utf-8") as resource:
        text = resource.read()
    if marker:
        m = re.search(r"<!-- generated:" + re.escape(marker) + r" -->\n(.*?)<!-- /generated -->", text, re.S)
        if not m: return []
        text = m.group(1)
    rows = []
    for block in re.split(r"\n\s*\n", text):
        lines = [l for l in block.split("\n") if l.startswith("|")]
        if len(lines) < 3: continue
        head = [c.strip() for c in lines[0].strip("|").split("|")]
        if header_starts and not head[0].startswith(header_starts): continue
        for l in lines[2:]:
            rows.append([c.strip() for c in l.strip("|").split("|")])
        return rows
    return rows


def num(s):
    s = s.replace(",", "").replace("%", "").replace("USD", "").strip()
    try: return float(s)
    except ValueError: return None


def reach_rows(band_label):
    rows = md_table(os.path.join(REFS, "reading-results.md"), marker="rr_reach_bands")
    key = band_label.replace(" Entrants", "")
    return [(num(r[3]), num(r[4]), num(r[5]) / 100, num(r[2])) for r in rows if r[0].replace(" Entrants", "") == key]


def pool_rows():
    return [(num(r[2]), num(r[1]), num(r[3])) for r in md_table(SIBLING_PRIZE, header_starts="Prize pool tenth")]


def seq_rows():
    b = os.path.join(REFS, "benchmarks.md")
    return {"curve": md_table(b, marker="bm_seqcurve"), "survival": md_table(b, marker="bm2_first_survival"), "splits": md_table(b, marker="bm_splits")}


TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@500;600&family=Inter:wght@400;500;600&display=swap">
<style>
:root{
  /* Gleam brand tokens: Grey 200 ground, Grey 400 borders, Grey 900 headlines, Grey 700 body, Grey 500 muted, Primary 500 green */
  --ground:#F7F8FA; --surface:#FFFFFF; --surface-2:#F0F2F5; --line:#D7DAE0; --line-strong:#9096A3;
  --ink:#0A0E14; --ink-2:#626A7A; --ink-3:#9096A3;
  --accent:#33B679; --accent-ink:#1F8F5B; --accent-soft:#D4F0E4;
  --good:#1F8F5B; --good-soft:#D4F0E4; --warn:#C0651A; --warn-soft:#FFE8D4; --crit:#C42B4C; --crit-soft:#FFD6E5;
  /* series from the app and platform colours, validated: Competitions purple, Primary green, Amazon orange, Instagram pink, Captures cyan */
  --s-visit:#591DF0; --s-follow:#33B679; --s-email:#F26A21; --s-share:#E1306C; --s-content:#0ABDE3; --s-other:#9096A3;
  --shadow:0 1px 2px rgba(10,14,20,.04),0 10px 28px rgba(10,14,20,.07);
  --radius:20px;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    color-scheme:dark;
    --ground:#0A0E14; --surface:#1C202E; --surface-2:#2F333D; --line:#2F333D; --line-strong:#626A7A;
    --ink:#FFFFFF; --ink-2:rgba(255,255,255,.72); --ink-3:rgba(255,255,255,.55);
    --accent:#8B6BFF; --accent-ink:#B9A6FF; --accent-soft:#2A1E5C;
    --good:#3DD08F; --good-soft:#123A2A; --warn:#F2A25C; --warn-soft:#3A2814; --crit:#FF6B8A; --crit-soft:#3E1A26;
    --s-visit:#8B6BFF; --s-follow:#1E9E63; --s-email:#D96C1F; --s-share:#E1306C; --s-content:#0893B2; --s-other:#626A7A;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px rgba(0,0,0,.35);
  }
}
:root[data-theme="dark"]{
  color-scheme:dark;
  --ground:#0A0E14; --surface:#1C202E; --surface-2:#2F333D; --line:#2F333D; --line-strong:#626A7A;
  --ink:#FFFFFF; --ink-2:rgba(255,255,255,.72); --ink-3:rgba(255,255,255,.55);
  --accent:#8B6BFF; --accent-ink:#B9A6FF; --accent-soft:#2A1E5C;
  --good:#3DD08F; --good-soft:#123A2A; --warn:#F2A25C; --warn-soft:#3A2814; --crit:#FF6B8A; --crit-soft:#3E1A26;
  --s-visit:#8B6BFF; --s-follow:#1E9E63; --s-email:#D96C1F; --s-share:#E1306C; --s-content:#0893B2; --s-other:#626A7A;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px rgba(0,0,0,.35);
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:"Inter",system-ui,-apple-system,"Segoe UI",sans-serif;font-size:15px;line-height:1.5;padding-block:0 48px;padding-inline:clamp(16px,4vw,40px)}
h1,h2,h3{font-family:"IBM Plex Sans","Inter",system-ui,sans-serif;text-wrap:balance;margin:0}
h1{font-size:clamp(22px,3vw,30px);font-weight:500;letter-spacing:-.01em}
h2{font-size:18px;font-weight:500;margin-bottom:12px}
h3{font-size:15px;font-weight:500}
p{margin:0 0 10px;max-width:68ch}
a{color:var(--accent-ink)}
.num{font-variant-numeric:tabular-nums}
.eyebrow{font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);font-weight:600}
.wrap{max-width:1180px;margin:0 auto}

/* header */
.top{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:12px 24px;padding-block:28px 18px;border-bottom:1px solid var(--line)}
.top .meta{display:flex;flex-wrap:wrap;gap:8px 18px;color:var(--ink-2);font-size:14px;margin-top:6px}
.pill{display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:999px;font-size:12.5px;font-weight:600;background:var(--surface-2);color:var(--ink-2);white-space:nowrap}
.pill.accent{background:var(--accent-soft);color:var(--accent-ink)}
.pill.good{background:var(--good-soft);color:var(--good)}
.pill.warn{background:var(--warn-soft);color:var(--warn)}
.pill i{width:7px;height:7px;border-radius:50%;background:currentColor;display:inline-block}

nav.sections{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--ground);display:flex;gap:4px;overflow-x:auto;padding-block:10px;margin-bottom:22px;border-bottom:1px solid var(--line)}
nav.sections a{text-decoration:none;color:var(--ink-2);font-size:13.5px;font-weight:500;padding:6px 12px;border-radius:8px;white-space:nowrap}
nav.sections a:hover,nav.sections a:focus-visible{background:var(--surface-2);color:var(--ink);outline:none}
nav.sections a:focus-visible{box-shadow:0 0 0 2px var(--accent)}

/* verdict */
.verdict{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(260px,1fr);gap:18px;margin-bottom:26px}
.verdict .lead{font-family:"IBM Plex Sans","Inter",system-ui,sans-serif;font-size:clamp(17px,2vw,21px);font-weight:500;line-height:1.4;max-width:none}
.assume{font-size:13.5px;color:var(--ink-2);border-left:3px solid var(--line-strong);padding-left:12px;margin-top:14px;max-width:none}
.tiles{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;align-content:start}
.tile{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.tile .v{font-family:"IBM Plex Sans","Inter",system-ui,sans-serif;font-size:26px;font-weight:600;line-height:1.1;margin:6px 0 2px}
.tile .l{font-size:12.5px;color:var(--ink-2)}
.tile .c{font-size:12px;color:var(--ink-3);margin-top:4px}

section{margin-bottom:34px;scroll-margin-top:64px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:18px 20px;box-shadow:var(--shadow)}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px}
.subhead{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:8px 16px;margin-bottom:10px}
.note{font-size:12.5px;color:var(--ink-3);margin:8px 0 0;max-width:none}

/* numbers table */
.tablewrap{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{text-align:left;padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);font-weight:600;white-space:nowrap}
td.num,th.num{text-align:right}
tr:last-child td{border-bottom:0}
.bar{display:inline-block;height:8px;border-radius:4px;background:var(--accent);vertical-align:middle;margin-right:8px}
.rank{display:inline-block;min-width:44px;text-align:right}
.rank.hi{color:var(--good);font-weight:600}
.rank.lo{color:var(--crit);font-weight:600}

/* changes */
.changes{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}
.change{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:16px 18px;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:6px}
.change .target{font-family:"IBM Plex Sans","Inter",system-ui,sans-serif;font-size:22px;font-weight:600}
.change .target small{font-family:"Inter",system-ui,sans-serif;font-size:13px;font-weight:500;color:var(--ink-2)}
.change .who{margin-top:auto;font-size:12.5px;color:var(--ink-3)}

/* charts */
.chart{position:relative;width:100%}
.chart svg{display:block;width:100%;height:auto;overflow:visible}
.chart text{font-family:"Inter",system-ui,sans-serif;fill:var(--ink-2);font-size:12px}
.chart .axis line,.chart .grid line{stroke:var(--line);stroke-width:1}
.chart .axis text{fill:var(--ink-3)}
.tip{position:absolute;pointer-events:none;background:var(--ink);color:var(--ground);font-size:12.5px;padding:6px 9px;border-radius:8px;white-space:nowrap;transform:translate(-50%,calc(-100% - 10px));opacity:0;transition:opacity .12s}
.tip.on{opacity:1}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:12.5px;color:var(--ink-2);margin-top:8px}
.legend span{display:inline-flex;align-items:center;gap:6px}
.legend i{width:10px;height:10px;border-radius:3px;display:inline-block}
.toggle{display:inline-flex;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.toggle button{background:var(--surface);border:0;padding:5px 11px;font:inherit;font-size:12.5px;color:var(--ink-2);cursor:pointer}
.toggle button[aria-pressed="true"]{background:var(--accent-soft);color:var(--accent-ink);font-weight:600}
.toggle button:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}

/* sliders */
input[type="range"]{width:100%;accent-color:var(--accent);margin:6px 0 10px}
input[type="range"]:focus-visible{outline:2px solid var(--accent);outline-offset:4px;border-radius:4px}
/* tabs */
.tabs{display:flex;gap:4px;border-bottom:1px solid var(--line);margin-bottom:16px;overflow-x:auto}
.tabs button{background:none;border:0;border-bottom:2px solid transparent;padding:10px 14px;font:inherit;font-size:14px;font-weight:500;color:var(--ink-2);cursor:pointer;white-space:nowrap;margin-bottom:-1px}
.tabs button[aria-selected="true"]{color:var(--accent-ink);border-bottom-color:var(--accent);font-weight:600}
.tabs button:hover{color:var(--ink)}
.tabs button:focus-visible{outline:2px solid var(--accent);outline-offset:-2px;border-radius:6px}
.panel[hidden]{display:none}
.heat{display:grid;grid-template-columns:32px repeat(7,1fr);gap:2px;font-size:11px;color:var(--ink-3)}
.heat .cell{height:11px;border-radius:2px;background:var(--accent)}
.heat .hl{text-align:right;padding-right:4px;line-height:11px}
.heat .dl{text-align:center;padding-bottom:4px;font-weight:600}
/* actions list */
.acts{display:flex;flex-direction:column;gap:6px}
.act{display:grid;grid-template-columns:minmax(150px,1.4fr) minmax(120px,3fr) 52px 92px;gap:10px;align-items:center;font-size:13.5px}
.act .n{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.act .track{position:relative;height:14px;background:var(--surface-2);border-radius:4px}
.act .fill{position:absolute;left:0;top:2px;height:10px;border-radius:0 4px 4px 0}
.act .tick{position:absolute;top:-3px;width:2px;height:20px;background:var(--ink);opacity:.55}
.act .pct{text-align:right}
.act .typ{text-align:right;color:var(--ink-3);white-space:nowrap}
.acts .hd{font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);font-weight:600}
.caveats{font-size:13.5px;color:var(--ink-2)}
.caveats li{margin-bottom:4px}
.question{font-family:"IBM Plex Sans","Inter",system-ui,sans-serif;font-size:17px;font-weight:500;margin-top:18px}
@media (max-width:720px){
  .verdict{grid-template-columns:1fr}
  .act{grid-template-columns:1fr 60px 60px}
  .act .track{grid-column:1 / -1;order:3}
}
@media (prefers-reduced-motion:reduce){.tip{transition:none}}
</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <div style="display:flex;align-items:center;gap:14px">
    <span id="siteLogo" style="display:none;flex:0 0 auto;line-height:0"></span>
    <div>
    <div class="eyebrow" id="siteLine">Giveaway Results Review</div>
    <h1>{{TITLE}}</h1>
    <div class="meta">{{META}}</div>
    </div>
  </div>
  <div style="display:flex;flex-wrap:wrap;gap:8px">{{PILLS}}</div>
</header>

<nav class="sections" aria-label="Sections">
  <a href="#verdict">Verdict</a><a href="#numbers">The Numbers</a><a href="#changes">What to Change</a><a href="#report" data-tab="t-overview">Overview</a><a href="#report" data-tab="t-traffic">Traffic</a><a href="#report" data-tab="t-entry">Entry Methods</a><a href="#report" data-tab="t-viral">Viral</a><a href="#report" data-tab="t-audience">Audience</a><a href="#report" data-tab="t-outcomes">Outcomes</a><a href="#report" data-tab="t-levers">Levers</a>
</nav>

<section id="verdict" class="verdict">
  <div>
    <p class="lead">{{VERDICT}}</p>
    <p class="assume">{{ASSUME}}</p>
  </div>
  <div class="tiles">{{TILES}}</div>
</section>

<section id="numbers">
  <div class="subhead"><h2>The Numbers, Against Campaigns Your Size</h2><span class="note" style="margin:0">{{BANDN}} campaigns of {{BANDLABEL}} in Gleam campaign data. Ranks describe what campaigns chose and never what a change would cause.</span></div>
  <div class="card tablewrap">
  <table>
    <thead><tr><th>Metric</th><th class="num">This campaign</th><th class="num">Typical, your size</th><th>Where it sits</th></tr></thead>
    <tbody>{{METRICROWS}}</tbody>
  </table>
  </div>
</section>

<section id="changes">
  <h2>What to Change Next Time</h2>
  <div class="changes">{{CHANGES}}</div>
</section>

<section id="report">
  <div class="subhead"><h2>The Report, in the Order of the Reporting Tabs</h2><span class="note" style="margin:0">Every figure from the skill's report script on the export, so any sentence above can be checked against a table here. Topline typical figures compare campaigns in the same size band in Gleam campaign data. Entry-method benchmarks compare all campaign sizes offering that action. Where no typical figure appears, the data holds no comparison. Times are account time.</span></div>
  <div class="tabs" role="tablist" aria-label="Reporting tabs">
    <button role="tab" aria-selected="true" aria-controls="tab-overview" id="t-overview">Overview</button>
    <button role="tab" aria-selected="false" aria-controls="tab-traffic" id="t-traffic">Traffic</button>
    <button role="tab" aria-selected="false" aria-controls="tab-entry" id="t-entry">Entry Methods</button>
    <button role="tab" aria-selected="false" aria-controls="tab-viral" id="t-viral">Viral</button>
    <button role="tab" aria-selected="false" aria-controls="tab-audience" id="t-audience">Audience</button>
    <button role="tab" aria-selected="false" aria-controls="tab-outcomes" id="t-outcomes">Outcomes</button>
    <button role="tab" aria-selected="false" aria-controls="tab-levers" id="t-levers">Levers</button>
  </div>

  <div class="panel" id="tab-overview" role="tabpanel" aria-labelledby="t-overview">
    <div class="grid2">
      <div class="card">
        <div class="subhead"><h3>New Entrants by Day</h3></div>
        <div class="chart" id="dailyChart"></div>
        <p class="note">{{TIMESTAMP_COVERAGE}}</p>
      </div>
      <div class="card">
        <h3>Topline</h3>
        {{TOPLINE}}
        <p class="note">{{SPEED}}</p>
      </div>
    </div>
    <div class="grid2" style="margin-top:16px">
      <div class="card">
        <h3>Insights, Each Checkable Against a Table Here</h3>
        <ul class="caveats">{{INSIGHTS}}</ul>
        <h3 style="margin-top:14px">Entrant Journey</h3>
        <p class="note" style="margin-top:4px">{{JOURNEY}}</p>
        <h3 style="margin-top:14px">How Deep Entrants Went</h3>
        <div class="chart" id="depthChart"></div>
      </div>
      <div class="card">
        <div class="subhead"><h3>Activity by Weekday and Hour</h3><span class="pill">{{HEATPEAK}}</span></div>
        <div class="chart" id="heatChart"></div>
        <p class="note">Actions in account time. A single campaign's heatmap follows its launch timing. No benchmark for timing or depth: these describe this campaign alone.</p>
      </div>
    </div>
  </div>

  <div class="panel" id="tab-traffic" role="tabpanel" aria-labelledby="t-traffic" hidden>
    <div class="grid2">
      <div class="card">
        <h3>Where Entrants Came From</h3>
        <div class="chart" id="sourceChart"></div>
        <p class="note">Earliest valid row's referrer. Email clicks arrive as webmail or direct and are undercounted. No benchmark: the campaign data holds no comparison for traffic mix, so this tab describes this campaign alone.</p>
      </div>
      <div class="card">
        <h3>Channels, With Depth and Invalid Rate</h3>
        {{CHANNELS}}
        <p class="note">Entrants and depth use each person's first valid source when timestamps are complete. Shares use all Entrants, including unknown first touch. Actions and invalid rates use each row's source. Depth is unavailable for channels with no valid first-touch Entrants. Signals, never verdicts.</p>
      </div>
    </div>
    <div class="grid2" style="margin-top:16px">
      <div class="card">
        <h3>Raw Referrers, First Touch</h3>
        {{HOSTS}}
      </div>
      <div class="card">
        <h3>Landing Page, Attribution and Partners</h3>
        <p>Landing page at first touch: {{LANDING}}.</p>
        {{UTM}}
        <p class="note">Partner contribution needs the hosts or UTM values that identify each partner. Without tagging it is not attributable.</p>
      </div>
    </div>
  </div>

  <div class="panel" id="tab-entry" role="tabpanel" aria-labelledby="t-entry" hidden>
    <div class="card">
      <div class="subhead">
        <h3>Every Entry Method, Completions per Entrant</h3>
        <div class="toggle" role="group" aria-label="Sort actions"><button id="sortShare" aria-pressed="true">By completion</button><button id="sortOrder" aria-pressed="false">Campaign order</button></div>
      </div>
      <div class="legend"><span><i style="background:var(--s-visit)"></i>Page visit</span><span><i style="background:var(--s-email)"></i>Email</span><span><i style="background:var(--s-follow)"></i>Follow</span><span><i style="background:var(--s-share)"></i>Share or refer</span><span><i style="background:var(--s-content)"></i>Content</span><span><i style="background:var(--s-other)"></i>Bonus or other</span><span>&#124; tick marks typical completions per Entrant for that kind of action, where one exists</span></div>
      <div class="acts" id="acts"></div>
      <p class="note">Bars and ticks count completions per Entrant, including repeat completions. Typical compares all campaign sizes offering that action. Unique participation below counts each Entrant once per action.</p>
    </div>
    <div class="card" style="margin-top:16px">
      <h3>Drop-Off, Friction and Speed</h3>
      {{FRICTION}}
      <p class="note">Typical and rank compare completions per Entrant across all campaign sizes offering that kind of action. Unique participation is separate and has no benchmark here. Typical seconds is the gap from the Entrant's previous action, in-session gaps under 30 minutes only.</p>
    </div>
  </div>

  <div class="panel" id="tab-viral" role="tabpanel" aria-labelledby="t-viral" hidden>
    <div class="card">
      <h3>Viral Lift</h3>
      <p>{{VIRALLINE}}</p>
      {{SHARERS}}
      <p class="note">Referrals are an output per sharer, never a survival stage. Signals, never verdicts: a sharer with many referrals, no connected accounts and referred Entrants who mostly do one action deserves a look before any Prize. Display names only, first name and initial, as the export shows them.</p>
    </div>
  </div>

  <div class="panel" id="tab-audience" role="tabpanel" aria-labelledby="t-audience" hidden>
    <div class="grid2">
      <div class="card">
        <h3>Countries</h3>
        <div class="chart" id="countryChart"></div>
        <p class="note">Country from IP at first action, top ten shown. No benchmark: audience geography, connected accounts and retention have no comparison in the data.</p>
      </div>
      <div class="card">
        <h3>Cities</h3>
        {{CITIES}}
      </div>
    </div>
    <div class="grid2" style="margin-top:16px">
      <div class="card">
        <h3>Connected Accounts and Retention</h3>
        <p>Connected accounts: {{HANDLES}}.</p>
        <p>{{RETENTION}}</p>
      </div>
      <div class="card">
        <h3>Most Engaged Entrants</h3>
        {{ENGAGED}}
      </div>
    </div>
  </div>

  <div class="panel" id="tab-outcomes" role="tabpanel" aria-labelledby="t-outcomes" hidden>
    <div class="card">
      <h3>What the List Did Next</h3>
      <p>Nothing in this section is in the export, so pull each figure from the email provider and the store and record it beside this review. Run the same four after the next campaign and the pair becomes a trend.</p>
      <ul class="caveats">
        <li>Unsubscribes and spam complaints in the 7 days after the Winners email, from the email provider, for the giveaway segment on its own.</li>
        <li>Addresses synced to the email provider against addresses collected here, so the gap between the two is visible.</li>
        <li>Customers and revenue from a join of Entrant email against order data at 30, 60 and 90 days after close.</li>
        <li>Open share of the new subscribers in their first 30 days, which says how much of the list is worth keeping.</li>
      </ul>
      <h3 style="margin-top:14px">Caveats</h3>
      <ul class="caveats">{{CAVEATS}}</ul>
      <p class="question">{{QUESTION}}</p>
    </div>
  </div>
{{LEVERS}}
</section>
</div>

<script>
const DATA={{DATA}};
(function(){
  const N=DATA.N, fmt=n=>Number(n).toLocaleString("en-US"), pct=x=>Math.round(x*100)+"%";
  const SITE=DATA.site||{};
  const ok=v=>v&&!/^\((none|not set|not provided)\)$/i.test(v);
  const dark=document.documentElement.dataset.theme==="dark"||(!document.documentElement.dataset.theme&&matchMedia("(prefers-color-scheme: dark)").matches);
  if(ok(SITE.elementsColour)&&!dark){document.documentElement.style.setProperty("--accent",SITE.elementsColour);}
  if(ok(SITE.headerColour)){document.querySelector("header.top").style.borderBottom="4px solid "+SITE.headerColour;}
  if(ok(SITE.backgroundColour)&&!dark){document.documentElement.style.setProperty("--ground",SITE.backgroundColour);}
  const line=document.getElementById("siteLine"), slot=document.getElementById("siteLogo");
  if(SITE.headerLogoSvg){slot.innerHTML=SITE.headerLogoSvg;slot.style.display="block";}
  else if(ok(SITE.headerLogo)){const img=document.createElement("img");img.src=SITE.headerLogo;img.alt=(SITE.name||"")+" logo";img.style.cssText="height:44px;width:auto;display:block";slot.appendChild(img);slot.style.display="block";}
  if(SITE.name){line.append(" for "+SITE.name);}
  const svgNS="http://www.w3.org/2000/svg";
  function el(tag,attrs,parent){const e=document.createElementNS(svgNS,tag);for(const k in attrs)e.setAttribute(k,attrs[k]);if(parent)parent.appendChild(e);return e;}
  function tipFor(host){const t=document.createElement("div");t.className="tip";host.appendChild(t);return t;}
  function showTip(t,host,x,y,text){t.textContent=text;t.style.left=x+"px";t.style.top=y+"px";t.classList.add("on");}
  function hideTip(t){t.classList.remove("on");}
  function short(d){const m=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];const p=d.split("-");return (+p[2])+" "+m[+p[1]-1];}

  // daily: area of new Entrants with the peak marked
  (function(){
    const daily=DATA.daily;if(!daily||daily.length<2||!daily.some(d=>d[1]>0))return;
    const host=document.getElementById("dailyChart"),W=520,H=230,pl=48,pr=14,pt=18,pb=34;
    const svg=el("svg",{viewBox:`0 0 ${W} ${H}`,role:"img","aria-label":"New Entrants by day"},host);
    const raw=Math.max(...daily.map(d=>d[1])),step=Math.pow(10,Math.floor(Math.log10(raw||1))),max=Math.ceil(raw/step)*step||1;
    const xs=i=>pl+i*(W-pl-pr)/(daily.length-1),ys=v=>pt+(H-pt-pb)*(1-v/max);
    const g=el("g",{class:"grid"},svg);
    for(let k=0;k<=4;k++){const v=max*k/4;el("line",{x1:pl,x2:W-pr,y1:ys(v),y2:ys(v)},g);const t=el("text",{x:pl-8,y:ys(v)+4,"text-anchor":"end",class:"axis"},svg);t.textContent=fmt(Math.round(v));}
    const pts=daily.map((d,i)=>[xs(i),ys(d[1])]);
    el("path",{d:"M"+pts.map(p=>p.join(",")).join("L")+`L${pts[pts.length-1][0]},${ys(0)}L${pts[0][0]},${ys(0)}Z`,fill:"var(--accent)","fill-opacity":".14"},svg);
    el("path",{d:"M"+pts.map(p=>p.join(",")).join("L"),fill:"none",stroke:"var(--accent)","stroke-width":2,"stroke-linejoin":"round"},svg);
    const every=Math.max(1,Math.round(daily.length/6));
    daily.forEach((d,i)=>{const t=el("text",{x:xs(i),y:H-12,"text-anchor":"middle",class:"axis"},svg);t.textContent=(i%every)?"":short(d[0]);});
    const pi=daily.reduce((b,d,i)=>d[1]>daily[b][1]?i:b,0);
    el("circle",{cx:pts[pi][0],cy:pts[pi][1],r:5,fill:"var(--accent)",stroke:"var(--surface)","stroke-width":2},svg);
    const lbl=el("text",{x:pts[pi][0]+(pi>daily.length/2?-10:10),y:pts[pi][1]+4,"font-weight":"600","text-anchor":pi>daily.length/2?"end":"start"},svg);lbl.textContent=fmt(daily[pi][1])+" on "+short(daily[pi][0]);lbl.setAttribute("fill","var(--ink)");
    const cross=el("line",{x1:0,x2:0,y1:pt,y2:ys(0),stroke:"var(--line-strong)","stroke-dasharray":"3 3",opacity:0},svg);
    const dot=el("circle",{r:4,fill:"var(--accent)",stroke:"var(--surface)","stroke-width":2,opacity:0},svg);
    const tip=tipFor(host);
    svg.addEventListener("mousemove",e=>{const r=svg.getBoundingClientRect(),x=(e.clientX-r.left)*W/r.width;let i=Math.round((x-pl)/((W-pl-pr)/(daily.length-1)));i=Math.max(0,Math.min(daily.length-1,i));
      cross.setAttribute("x1",xs(i));cross.setAttribute("x2",xs(i));cross.setAttribute("opacity",1);dot.setAttribute("cx",xs(i));dot.setAttribute("cy",ys(daily[i][1]));dot.setAttribute("opacity",1);
      showTip(tip,host,xs(i)*r.width/W,ys(daily[i][1])*r.height/H,`${short(daily[i][0])} ${fmt(daily[i][1])} new Entrants, ${fmt(daily[i][2])} actions`);});
    svg.addEventListener("mouseleave",()=>{cross.setAttribute("opacity",0);dot.setAttribute("opacity",0);hideTip(tip);});
  })();

  function hbars(id,data,total,opts){
    const host=document.getElementById(id);if(!host||!data.length)return;const W=520,rowH=28,pl=opts.pl||150,pr=64,H=data.length*rowH+8;
    const svg=el("svg",{viewBox:`0 0 ${W} ${H}`,role:"img","aria-label":opts.label},host);
    const max=Math.max(...data.map(d=>d[1]))||1,xs=v=>pl+v*(W-pl-pr)/max;
    const tip=tipFor(host);
    data.forEach((d,i)=>{const y=i*rowH+6;const t=el("text",{x:pl-10,y:y+15,"text-anchor":"end"},svg);t.textContent=d[0];t.setAttribute("fill","var(--ink)");
      el("rect",{x:pl,y:y+4,width:Math.max(2,xs(d[1])-pl),height:16,rx:4,fill:"var(--accent)"},svg);
      const v=el("text",{x:xs(d[1])+8,y:y+15},svg);v.textContent=pct(d[1]/total);v.setAttribute("class","num");
      const hit=el("rect",{x:0,y:y,width:W,height:rowH,fill:"transparent"},svg);
      hit.addEventListener("mousemove",()=>{const r=svg.getBoundingClientRect();showTip(tip,host,(xs(d[1])/2+pl/2)*r.width/W,y*r.height/H,`${d[0]} ${fmt(d[1])} Entrants, ${pct(d[1]/total)}`);});
      hit.addEventListener("mouseleave",()=>hideTip(tip));});
  }
  const depthLabel={"1":"1 action","2-5":"2 to 5","6-10":"6 to 10","11+":"11 or more"};
  hbars("depthChart",DATA.depth.map(d=>[depthLabel[d[0]]||d[0],d[1]]),N,{pl:90,label:"Entrants by number of actions completed"});
  hbars("sourceChart",DATA.sources,N,{pl:190,label:"Entrants by referring source of first action"});
  hbars("countryChart",DATA.countries,N,{pl:120,label:"Entrants by country"});

  // heatmap, 24 rows of 7 weekdays
  (function(){const host=document.getElementById("heatChart"),heat=DATA.heat;if(!host||!heat)return;const g=document.createElement("div");g.className="heat";g.setAttribute("role","img");g.setAttribute("aria-label","Actions by weekday and hour");
    const days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],max=Math.max(1,...heat.flat());let h='<span></span>'+days.map(d=>`<span class="dl">${d}</span>`).join("");
    heat.forEach((row,hr)=>{h+=`<span class="hl">${hr%3?"":String(hr).padStart(2,"0")}</span>`+row.map((v,d)=>`<span class="cell" title="${days[d]} ${String(hr).padStart(2,"0")}:00, ${fmt(v)} actions" style="opacity:${(0.08+0.92*v/max).toFixed(2)}"></span>`).join("");});
    g.innerHTML=h;host.appendChild(g);})();

  // actions list
  const list=document.getElementById("acts");
  const fam={visit:"var(--s-visit)",email:"var(--s-email)",follow:"var(--s-follow)",share:"var(--s-share)",content:"var(--s-content)",other:"var(--s-other)"};
  const famName={visit:"page visit",email:"email",follow:"follow",share:"share or refer",content:"content",other:"bonus or other"};
  function render(order){
    list.innerHTML='<div class="act"><span class="hd">Entry Method</span><span class="hd">Completions per Entrant</span><span class="hd pct">This</span><span class="hd typ">Typical</span></div>';
    const rows=order==="share"?[...DATA.acts].sort((a,b)=>b[2]-a[2]):DATA.acts;
    const scale=Math.max(1.5,...rows.map(a=>a[2]),...rows.map(a=>a[3]||0));
    rows.forEach(a=>{const r=document.createElement("div");r.className="act";
      const tick=a[3]==null?"":`<span class="tick" style="left:${Math.min(100,a[3]/scale*100)}%" title="typical ${a[3].toFixed(1)+" completions per Entrant"}"></span>`;
      r.innerHTML=`<span class="n"></span><span class="track" aria-hidden="true"><span class="fill" style="width:${a[2]/scale*100}%;background:${fam[a[4]]||fam.other}"></span>${tick}</span><span class="pct num">${a[2].toFixed(1)}</span><span class="typ num">${a[3]==null?"n/a":a[3].toFixed(1)}</span>`;
      const label=r.querySelector(".n");label.textContent=a[0];label.title=a[0];
      r.setAttribute("aria-label",`${a[0]}, ${famName[a[4]]||"other"}, ${a[2].toFixed(1)} completions per Entrant, completed by ${pct(a[5])} of Entrants, ${fmt(a[1])} completions`);
      list.appendChild(r);});
  }
  render("share");
  const bS=document.getElementById("sortShare"),bO=document.getElementById("sortOrder");
  bS.addEventListener("click",()=>{render("share");bS.setAttribute("aria-pressed","true");bO.setAttribute("aria-pressed","false");});
  bO.addEventListener("click",()=>{render("order");bS.setAttribute("aria-pressed","false");bO.setAttribute("aria-pressed","true");});

  // tabs
  const tabs=[...document.querySelectorAll('.tabs [role="tab"]')];
  function selectTab(btn){tabs.forEach(b=>{const on=b===btn;b.setAttribute("aria-selected",on);document.getElementById(b.getAttribute("aria-controls")).hidden=!on;});}
  tabs.forEach(b=>b.addEventListener("click",()=>selectTab(b)));
  document.querySelectorAll('nav.sections a[data-tab]').forEach(a=>a.addEventListener("click",()=>selectTab(document.getElementById(a.dataset.tab))));

  // levers: arithmetic on the campaign's counts, lookups in the benchmark slices and the reference tables
  const PCTS=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95], SL=DATA.slices;
  function beats(v,t){let k=0;for(const x of t.p){if(v>x)k++;}return k?PCTS[k-1]:0;}
  function bandOf(n){for(const k in SL){if(k!=="all"&&n>=SL[k].lo&&n<SL[k].hi)return k;}return "band:10k+";}
  const es=document.getElementById("emailShare"),ec=document.getElementById("emailCount"),er=document.getElementById("emailRank");
  function upd1(){const sh=+es.value/100;ec.innerHTML=fmt(Math.round(sh*N))+' <small>addresses if <span>'+Math.round(sh*100)+'%</span> of your '+fmt(N)+' Entrants sign up</small>';er.textContent="This target counts unique subscribers. Email benchmarks count subscription completions per Entrant, so this target has no benchmark rank.";}
  es.addEventListener("input",upd1);upd1();
  const en=document.getElementById("ent"),enb=document.getElementById("entBand"),enr=document.getElementById("entRank");
  function upd2(){
    const n=+en.value;if(N<100||n<100){enb.textContent=fmt(n)+" Entrants";enr.textContent="No matching peers: the dataset starts at 100 Entrants";return;}
    const b=SL[bandOf(n)]||{},typ=[],ranks=[];
    if(b.contestants)typ.push(fmt(Math.round(b.contestants.p[9]))+" Entrants");
    if(b.entries_per_entrant)typ.push(b.entries_per_entrant.p[9].toFixed(1)+" Entries each");
    if(b.actions_per_contestant)typ.push(b.actions_per_contestant.p[9].toFixed(1)+" actions each");
    enb.textContent=fmt(n)+" Entrants"+(typ.length?". Available typical figures for this size: "+typ.join(", "):". Size benchmarks unavailable");
    const all=SL.all||{};
    if(all.contestants)ranks.push("ahead of "+beats(n,all.contestants)+"% of all "+fmt(all.contestants.n)+" campaigns");
    if(b.contestants)ranks.push("ahead of "+beats(n,b.contestants)+"% of the "+fmt(b.contestants.n)+" your size");
    enr.textContent=ranks.length?ranks.join("; "):"Entrant rank unavailable";
  }
  en.addEventListener("input",upd2);upd2();
  const pr=document.getElementById("prize"),prp=document.getElementById("prizePer");
  function upd3(){const c=+pr.value;prp.innerHTML='<span>'+fmt(c)+'</span> <small>works out at '+(c?(c/N).toFixed(2):"-")+' an Entrant'+(DATA.emails?' and '+(c?(c/DATA.emails).toFixed(2):"-")+' an address':'')+'</small>';}
  pr.addEventListener("input",upd3);upd3();
  const rc=document.getElementById("reach");
  if(rc&&DATA.reach.length){const rce=document.getElementById("reachEnt"),rcn=document.getElementById("reachNote"),R=DATA.reach;
    function interp(x,ix,iy){if(x<=R[0][ix])return R[0][iy];for(let i=1;i<R.length;i++){if(x<=R[i][ix]){const a=R[i-1],b=R[i],t=(Math.log(x)-Math.log(a[ix]))/(Math.log(b[ix])-Math.log(a[ix]));return a[iy]+t*(b[iy]-a[iy]);}}return R[R.length-1][iy];}
    function upd4(){const x=+rc.value;const e=interp(x,0,1),c=interp(x,0,2);rce.innerHTML=fmt(Math.round(e))+' <small>Entrants is what campaigns your size got from <span>'+fmt(Math.round(x/10)*10)+'</span> Impressions, at a '+Math.round(c*100)+'% Conversion Rate</small>';rcn.textContent="Twice the traffic goes with about 40% more Entrants, not double. That's what campaigns at each level got ("+fmt(R.reduce((s,r)=>s+r[3],0))+" campaigns your size in five groups by Impressions), not a promise of what promotion will do for you.";}
    rc.addEventListener("input",upd4);upd4();}
  const pl=document.getElementById("pool");
  if(pl&&DATA.pool.length){const ple=document.getElementById("poolEnt"),P=DATA.pool;
    function upd5(){const g=P[+pl.value];ple.innerHTML=fmt(g[2])+' <small>Entrants is what campaigns with a <span>USD '+fmt(g[0])+'</span> Prize pool typically got, across '+fmt(g[1])+' of them</small>';}
    pl.addEventListener("input",upd5);upd5();}
})();
</script>
</body>
</html>
'''


def gather(a):
    """Everything the page needs, from the two scripts and the references."""
    # Suppressed whole cohorts behave like unavailable groups throughout the review.
    RV.PCT = RV.PCT or RV.load_pct()
    if RV.PCT:
        RV.PCT = dict(RV.PCT, groups={key: group for key, group in RV.PCT.get("groups", {}).items() if isinstance(group, dict)})
    mapping = dict(kv.split("=", 1) for kv in a.map.split(",")) if getattr(a, "map", None) else {}
    worth = CR.parse_wide_worth(getattr(a, "wide_worth", None), getattr(a, "wide_worth_json", None))
    rows = CR.load(a.export, mapping, getattr(a, "wide_unit", None), worth)
    class A: impressions = a.impressions; prize_cost = a.prize_cost; prize_value = getattr(a, "prize_value", None); plan_cost = a.plan_cost; benchmark_cpl = None; sends = a.sends; coverage_start = getattr(a, "coverage_start", None); coverage_end = getattr(a, "coverage_end", None); partners = a.partners.split(",") if a.partners else None
    A.complete_all_action = getattr(a, "complete_all_action", None)
    R = CR.analyze(rows, A); T = R["topline"]; N = R["base"]
    if not N:
        return {"R": R, "T": T, "N": N}
    class B: pass
    b = B(); b.contestants = N; b.impressions = a.impressions; b.entries = T["entries"]; b.invalid = R["topline"].get("invalid_entries", 0) or 0
    b.days = a.days; b.methods = a.methods
    email_completions = sum(comp for act, comp, *_ in R["actions"] if kind(act) == "emails")
    emails = R["email_subscribers"]
    b.emails = email_completions or None
    b.referrals = R["viral"]["refer_rows"]; b.actions_completed = T["actions"]; b.prize_value = None
    for k in ("x_follows", "instagram_follows", "tiktok_follows", "twitch_follows", "youtube_subscribes", "discord_joins"): setattr(b, k, None)
    b.vertical = a.vertical; b.repeatable = a.repeatable; b.first_campaign = a.first_campaign; b.actions = None; b.history = None
    metrics = RV.review(b)
    labels = {"Email signups": "Email subscription completions", "Email signups per Entrant": "Email subscription completions per Entrant"}
    metrics = [(labels.get(label, label), *values) for label, *values in metrics]
    span = (R["end"].date() - R["start"].date()).days + 1 if R.get("start") else None
    metrics.append(("Observed activity span in days", str(span) if span is not None else "unavailable", "-", "Completion timestamps only"))
    metrics.append(("Completed method titles", str(sum(comp > 0 for _, comp, *_ in R["actions"])), "-", "Methods with valid completions only"))
    RV.PCT = RV.PCT or RV.load_pct(); band = RV.band(N) if N >= 100 else "below-100"; band_label = RV.band_label(N) if N >= 100 else "Below 100 Entrants"
    groups = RV.PCT.get("groups", {})
    def slice_of(key):
        group = groups.get(key) or {}
        return {m: {"n": group[m]["n"], "p": group[m]["p"]}
                for m in ("contestants", "email_uptake", "entries_per_entrant", "actions_per_contestant")
                if isinstance(group.get(m), dict)}
    bands = {"band:100-250": ("100 to 250", 100, 250), "band:250-500": ("250 to 500", 250, 500), "band:500-1k": ("500 to 1,000", 500, 1000),
             "band:1k-2.5k": ("1,000 to 2,500", 1000, 2500), "band:2.5k-10k": ("2,500 to 10,000", 2500, 10000), "band:10k+": ("10,000 or more", 10000, 10 ** 9)}
    slices = {k: dict(label=v[0], lo=v[1], hi=v[2], **slice_of(k)) for k, v in bands.items()}
    slices["all"] = slice_of("all")
    if N < 100: slices = {"band:below-100": {}}
    acts = []
    for act, comp, uniq, share, rate, sec, inv in R["actions"]:
        g = generic_name(act); fam = RV.family(act) or "other"
        t = RV.PCT.get("per_action_uptake", {}).get(g) if g and N >= 100 else None
        typ = t["p"][9] if t else None; rr = RV.rank(comp / N, t) if t else None
        acts.append({"name": act, "completions": comp, "share": comp / N, "typical": typ, "family": fam if fam in FAMILY_COLOUR else "other",
                     "where": (f"better than {rr[0]}% of {n(rr[1])} offering {g}" if rr else "No matching peers: the dataset starts at 100 Entrants" if N < 100 else "no matching group"), "entrants": uniq, "share_actions": share, "rate": rate, "seconds": sec, "invalid": inv})
    return {"R": R, "T": T, "N": N, "emails": emails, "email_completions": email_completions, "metrics": metrics, "band": band, "band_label": band_label, "slices": slices, "acts": acts,
            "reach": reach_rows(band_label) if N >= 100 else [], "pool": pool_rows() if N >= 100 else [], "seq": seq_rows() if N >= 100 else {"curve": [], "survival": [], "splits": []}, "insights": CR.insights(R)}


def words_of(path):
    W = {"assumptions": "Write the assumptions line here.", "verdict": "Write the verdict here: what the campaign did well with its rank, then the figure with the most room to close.",
         "pills": [], "changes": [], "caveats": [], "question": "End on the one question that would change the advice."}
    if path:
        with open(path, encoding="utf-8") as resource:
            W.update(json.load(resource))
    return W


def site_of(path):
    S = {"name": "", "url": "", "headerLogo": None, "headerColour": None, "elementsColour": None, "backgroundColour": None}
    if path:
        with open(path, encoding="utf-8") as resource:
            S.update(json.load(resource))
    return S


def metric_rows(D):
    out = []
    for m in D["metrics"]:
        label, this, typ, read = m[0], m[1], m[2], m[3]
        out.append(f"<tr><td>{esc(label)}</td><td class=\"num\">{esc(this)}</td><td class=\"num\">{esc(typ)}</td><td>{esc(read)}</td></tr>")
    return "\n".join(out)


def tiles(D):
    T, N, R = D["T"], D["N"], D["R"]; V = R["viral"]
    em = D["emails"]
    def typical(metric):
        value = (D["slices"].get("band:" + D["band"]) or {}).get(metric)
        return f"{value['p'][9]:.1f} typical for your size" if value else "Benchmark unavailable"
    t = [("Entrants", n(N), f"{D['band_label']} band"), ("Entries each", f"{T['entries_per_entrant']:.1f}", typical("entries_per_entrant") if N >= 100 else "No matching peers"),
         ("Actions each", f"{T['actions_per_entrant']:.1f}", typical("actions_per_contestant") if N >= 100 else "No matching peers"),
         ("Referred Entrants", n(V["referred_entrants"]) if V["graph_complete"] else "unavailable", f"{V['referred_share']:.0%} of Entrants" if V["graph_complete"] else "Referral relationships incomplete")]
    if em: t[2] = ("Email signups", n(em), f"{em / N:.0%} of Entrants")
    return "\n".join(f'<div class="tile"><div class="l">{esc(l)}</div><div class="v num">{esc(v)}</div><div class="c">{esc(c)}</div></div>' for l, v, c in t)


def change_cards(W):
    if not W["changes"]:
        return '<div class="change"><div class="eyebrow">Change</div><h3>Write the three changes here</h3><p>Each one a target against a benchmark, with the figure that motivates it and the skill that plans it.</p></div>'
    out = []
    for c in W["changes"]:
        out.append(f'<div class="change"><div class="eyebrow">{esc(c.get("eyebrow", ""))}</div><h3>{esc(c.get("title", ""))}</h3>'
                   f'<div class="target num">{esc(c.get("target", ""))} <small>{esc(c.get("target_note", ""))}</small></div><p>{esc(c.get("body", ""))}</p>'
                   f'<div class="who">{esc(c.get("who", ""))}</div></div>')
    return "\n".join(out)


def table(headers, rows, num_from=1):
    h = "".join(f"<th{' class=\"num\"' if i >= num_from else ''}>{esc(x)}</th>" for i, x in enumerate(headers))
    b = "\n".join("<tr>" + "".join(f"<td{' class=\"num\"' if i >= num_from else ''}>{esc(x)}</td>" for i, x in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="tablewrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def render(D, W, S, a):
    if not D["N"]:
        T = D["T"]
        total_entries = T["entries"] + T["invalid_entries"]
        metrics = [("Entrants", "0"), ("Actions completed", n(T["actions"])),
                   ("Entries", n(T["entries"])), ("Invalid actions", n(T["invalid_actions"])),
                   ("Invalid Entries", "unavailable" if T["unweighted_rows"] else f"{T['invalid_entries']:,}"),
                   ("Invalid action share", f"{T['invalid_rate']:.1%}" if T["invalid_rate"] is not None else "unavailable"),
                   ("Invalid Entries share", f"{T['invalid_entries'] / total_entries:.1%}" if total_entries and not T["unweighted_rows"] else "unavailable"),
                   ("Actions each", "unavailable"), ("Entries each", "unavailable")]
        if a.impressions and a.impressions > 0:
            metrics.append(("Conversion Rate", "0.0%"))
        title = esc(a.title or "Campaign Results Review")
        return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
                f'<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title>'
                '<style>body{font:16px system-ui;max-width:960px;margin:48px auto;padding:0 24px}'
                'table{border-collapse:collapse;width:100%}th,td{text-align:left;padding:10px;border-bottom:1px solid #ddd}</style>'
                f'</head><body><main><h1>{title}</h1><p>This export has zero valid Entrants.</p>'
                + table(["Metric", "Value"], metrics)
                + (f'<p>{n(T["unweighted_rows"])} rows have missing or unusable Entries weights. '
                   'Invalid Entries totals and their share are unavailable until weights are reconciled.</p>' if T["unweighted_rows"] else "")
                + '<p>Per-Entrant rates, engagement, referrals and benchmark comparisons are unavailable. '
                'Check export filters and validity statuses before reviewing performance.</p></main></body></html>')
    R, T, N = D["R"], D["T"], D["N"]; V = R["viral"]; E = R["engagement"]; Sp = R["speed"]
    title = a.title or "Campaign Results Review"
    meta = [x for x in [a.dates, f"{D['band_label']} band", a.vertical and f"{a.vertical.replace('_', ' ')} vertical", "First campaign at this size" if a.first_campaign else None] if x]
    pills = "".join(f'<span class="pill {esc(p.get("kind", ""))}"><i></i>{esc(p["text"])}</span>' for p in W["pills"])
    daily = [(d.isoformat(), ne, ac) for d, ne, ac in R.get("by_day", [])]
    heat = [[R["heat"][(d, h)] for d in range(7)] for h in range(24)]
    heat_peak = R["heat_peak"]
    ins = "".join(f"<li>{esc(i)}</li>" for i in D["insights"])
    topline = table(["Metric", "Value"], [("Entrants (unique valid emails)", n(N)), ("Actions completed", n(T["actions"])), ("Entries", f"{T['entries']:,}"), ("Actions each", f"{T['actions_per_entrant']:.1f}"), ("Entries each", f"{T['entries_per_entrant']:.1f}"),
                                          ("Invalid actions", f"{n(T['invalid_actions'])} ({T['invalid_rate']:.1%} of rows)")] + ([("Conversion Rate", f"{N / a.impressions:.1%}")] if a.impressions else []))
    if R.get("prize_value") is not None:
        topline += f'<p>Stated Prize value: {R["prize_value"]:,.2f}. Advertised value, excluded from spending.</p>'
    if R.get("roi"):
        roi = R["roi"]
        topline += f'<p>Supplied actual Prize and plan costs: {roi["cost"]:,.2f}, or {roi["per_entrant"]:.2f} per Entrant'
        if roi["per_email"] is not None: topline += f' and {roi["per_email"]:.2f} per unique email subscriber'
        topline += '. Only supplied costs are included. Add missing costs before treating this as total campaign spending.</p>'
    else:
        topline += '<p>Actual costs unavailable. Stated Prize value alone does not establish spending.</p>'
    speed = (f"Of {n(Sp['multi'])} multi-action Entrants, first to last {Sp['median_span_min']:.0f} minutes typical, {Sp['within_10_min']:.0%} done within 10 minutes, {Sp['one_sitting']:.0%} in one sitting." if Sp.get("multi") else "")
    if Sp["completed_everything"] is not None:
        speed += f" Completed everything (explicitly mapped action): {n(Sp['completed_everything'][0])} Entrants ({Sp['completed_everything'][1]:.0%})."
    referred = n(V["referred_entrants"]) if V["graph_complete"] else "unavailable (referral relationships incomplete)"
    journey = f"Entered {n(N)} (100%), completed more than one action {n(N - E['1'][0])} ({(N - E['1'][0]) / N:.0%}), shared {n(V['sharers'])} ({V['participation']:.0%}), referred new Entrants {referred}. Referrals are an output per sharer, never a stage, so this is not a funnel."
    channels = table(["Channel", "Entrants", "Share", "Actions", "Depth vs average", "Invalid rate"], [(c[0], n(c[1]), pct(c[2]), n(c[3]), f"{c[4]:.2f}x" if c[4] is not None else "unavailable", f"{c[5]:.1%}" if c[5] is not None else "unavailable") for c in R["channels"]])
    hosts = table(["Host", "Entrants"], [(h, n(c)) for h, c in R["hosts"]])
    landing = ", ".join(f"{k} {n(v)} ({v / N:.0%})" for k, v in R["landing"])
    utm = table(["Source", "Medium", "Campaign", "Entrants"], [(u[0][0], u[0][1], u[0][2], n(u[1])) for u in R["utm"]], num_from=3) if R["utm"] else "<p class=\"note\">No UTM parameters on known first-touch landing pages.</p>"
    friction = table(["Action", "Completions", "Entrants", "Share of actions", "Unique participation", "Completions per Entrant", "Typical completions per Entrant, campaigns offering it", "Where completions per Entrant sit", "Typical seconds", "Invalid"],
                     [(x["name"], n(x["completions"]), n(x["entrants"]), pct(x["share_actions"]), pct(x["rate"]), f"{x['share']:.1f}", f"{x['typical']:.1f}" if x["typical"] is not None else "-", x["where"], (f"{x['seconds']:.0f}" + (" (slow)" if x["seconds"] > 120 else "")) if x["seconds"] is not None else "-", n(x["invalid"])) for x in D["acts"]])
    sharers = table(["Sharer", "Referrals", "Entered", "Entries brought", "Connected accounts", "Referred doing one action"], [(s[0], n(s[1]), n(s[2]), f"{s[3]:,}", s[4], s[5]) for s in V["top"]]) if V["top"] else ""
    countries = [(c, v) for c, v in R["countries"]]
    cities = table(["City", "Entrants"], [(f"{c[0][0]}, {c[0][1]}", n(c[1])) for c in R["cities"]]) if R["cities"] else ""
    handles = ", ".join(f"{c} {v:.0%}" for c, v in R["handles"]) if R["handles"] else "none recorded"
    retention = CR.retention_text(R)
    engaged = table(["Entrant", "Actions", "Entries", "Referred", "Days active", "Connected accounts"], [(t[0], t[1], f"{t[2]:,}", t[3], t[4], t[5]) for t in R["top_entrants"]])
    caveats = "".join(f"<li>{esc(c)}</li>" for c in W["caveats"])
    bslice = D["slices"]["band:" + D["band"]]
    email_share = D["emails"] / N if D["emails"] else 0
    data = {"date_coverage": R["date_coverage"], "N": N, "emails": D["emails"], "daily": daily, "depth": [(k, v[0]) for k, v in E.items()], "sources": [(c[0], c[1]) for c in R["channels"] if c[1]],
            "countries": countries, "acts": [(x["name"], x["completions"], x["share"], x["typical"], x["family"], x["rate"]) for x in D["acts"]], "heat": heat, "slices": D["slices"], "band": "band:" + D["band"],
            "band_label": D["band_label"], "reach": D["reach"], "pool": D["pool"], "email_share": email_share, "site": S}
    seq = D["seq"]; curve = {r[0]: r for r in seq["curve"]}; splits = {r[0]: r for r in seq["splits"]}
    nextrun = ""
    if curve.get("1st") and curve.get("2nd"):
        nextrun = f"Second campaigns typically got {curve['2nd'][3]} Entrants where first ones got {curve['1st'][3]}, one campaign per business."
        if splits.get("Within 30 days of previous campaign") and splits.get("First campaign"):
            w30, fc = splits["Within 30 days of previous campaign"], splits["First campaign"]
            nextrun += f" Launching within 30 days of your last one went with {w30[1]} Entrants at a {w30[2]} Conversion Rate, against {fc[1]} at {fc[2]} for a first campaign."
        nextrun += " The brands that ran again are the ones whose last one went well, so read this as encouragement, not a guarantee."
    surv = ""
    for r in seq["survival"]:
        lo = num(r[0].split(" ")[0]) if r[0][0].isdigit() else 0
        if r[0].startswith("Under") and N < 250: surv = f"{r[3]} of businesses whose first campaign drew {r[0].lower()} ran a second"; break
        if lo and N >= lo: surv = f"{r[3]} of businesses whose first campaign drew {r[0].lower()} ran a second"
    pool_card = ""
    if D["pool"]:
        pool_card = '''<div class="change"><div class="eyebrow">Prize</div><h3>Go Bigger on the Prize</h3><input type="range" id="pool" min="0" max="''' + str(len(D["pool"]) - 1) + '''" value="''' + str(min(3, len(D["pool"]) - 1)) + '''" step="1" aria-label="Stated Prize pool, groups from the Prize picker's evidence"><div class="target num" id="poolEnt"></div><p class="note" style="margin:0">Bigger Prizes tend to come from bigger brands with bigger audiences, so it's a comparison, not a promise. From the Prize picker's evidence.</p></div>'''
    reach_card = ""
    if D["reach"]:
        mid = D["reach"][2][0] if len(D["reach"]) > 2 else D["reach"][0][0]
        reach_card = f'''<div class="change"><div class="eyebrow">Promotion</div><h3>Put More People in Front of It</h3><input type="range" id="reach" min="{int(D['reach'][0][0])}" max="{int(D['reach'][-1][0])}" value="{int(mid)}" step="10" aria-label="Impressions on the next run"><div class="target num" id="reachEnt"></div><p class="note" style="margin:0" id="reachNote"></p></div>'''
    levers = f'''
  <div class="panel" id="tab-levers" role="tabpanel" aria-labelledby="t-levers" hidden>
    <div class="subhead"><h3>Play With the Levers</h3><span class="note" style="margin:0">Move a slider and see what campaigns like yours got at that level, from Gleam campaign data. It's a comparison, not a prediction: bigger Prizes tend to come from bigger brands with bigger audiences, and more traffic usually means a different campaign.</span></div>
    <div class="changes">
      <div class="change"><div class="eyebrow">Your List</div><h3>Get More Entrants Onto Your List</h3><input type="range" id="emailShare" min="0" max="100" value="{round(email_share * 100)}" step="1" aria-label="Target share of Entrants signing up"><div class="target num" id="emailCount"></div><p id="emailRank" class="note" style="margin:0"></p></div>
      <div class="change"><div class="eyebrow">Next Campaign</div><h3>Aim Bigger Next Time</h3><input type="range" id="ent" min="1" max="{max(20000, N * 2)}" value="{N}" step="1" aria-label="Entrants on the next run"><div class="target num" id="entBand"></div><p id="entRank" class="note" style="margin:0"></p></div>
      <div class="change"><div class="eyebrow">Your Spend</div><h3>What Your Prize Bought You</h3><input type="range" id="prize" min="0" max="{max(5000, int(a.prize_cost or 0) * 2)}" value="{int(a.prize_cost or 0)}" step="10" aria-label="Prize cost"><div class="target num" id="prizePer"></div><p class="note" style="margin:0">Worked on your {n(N)} Entrants{(" and " + n(data["emails"]) + " addresses") if data["emails"] else ""}. This scenario uses actual Prize cost only. Plan, promotion and other costs are excluded. Cost benchmarks by vertical live in the Prize picker.</p></div>
      {reach_card}
      {pool_card}
      <div class="change"><div class="eyebrow">Run It Again</div><h3>Your Next One</h3><div class="target num">{esc(surv.split(" of ")[0]) if surv else "-"} <small>{esc(surv.split(" ", 1)[1]) if surv else "No matching peers: the dataset starts at 100 Entrants" if N < 100 else "no sequence table found in the references"}</small></div><p class="note" style="margin:0">{esc(nextrun)}</p></div>
    </div>
  </div>'''
    page = TEMPLATE
    for k, v in {"TITLE": esc(title), "META": "".join(f"<span>{esc(m)}</span>" for m in meta), "PILLS": pills, "VERDICT": esc(W["verdict"]), "ASSUME": esc(W["assumptions"]), "TILES": tiles(D),
                 "BANDLABEL": esc(D["band_label"]), "BANDN": n(bslice["contestants"]["n"]) if bslice.get("contestants") else "-", "METRICROWS": metric_rows(D), "CHANGES": change_cards(W), "INSIGHTS": ins, "TOPLINE": topline, "SPEED": esc(speed), "JOURNEY": esc(journey),
                 "TIMESTAMP_COVERAGE": esc(CR.timestamp_coverage_text(R)), "HEATPEAK": esc(f"Peak {CR.DAYS[heat_peak[0][0]]} {heat_peak[0][1]:02d}:00, {n(heat_peak[1])} actions") if heat_peak else "", "CHANNELS": channels, "HOSTS": hosts, "LANDING": esc(landing), "UTM": utm, "FRICTION": friction,
                 "VIRALLINE": esc(CR.viral_text(V)),
                 "SHARERS": sharers, "CITIES": cities, "HANDLES": esc(handles), "RETENTION": esc(retention), "ENGAGED": engaged, "CAVEATS": caveats, "QUESTION": esc(W["question"]), "LEVERS": levers,
                 "NCOUNTRIES": n(len(set(c for c, _ in countries))) if countries else "0", "DATA": script_json(data)}.items():
        page = page.replace("{{" + k + "}}", v)
    assert "{{" not in page, re.findall(r"\{\{\w+\}\}", page)[:5]
    if N < 100:
        page = page.replace("- campaigns of Below 100 Entrants in Gleam campaign data. Ranks describe what campaigns chose and never what a change would cause.",
                            "No matching peers: the dataset starts at 100 Entrants. Actual campaign metrics only.")
        page = page.replace("Move a slider and see what campaigns like yours got at that level, from Gleam campaign data. It's a comparison, not a prediction: bigger Prizes tend to come from bigger brands with bigger audiences, and more traffic usually means a different campaign.",
                            "Move a slider to calculate targets from your campaign counts. No matching peers: the dataset starts at 100 Entrants.")
    return page


def self_test():
    import tempfile
    d = tempfile.mkdtemp(); p = os.path.join(d, "e.csv")
    import datetime as dt
    with open(p, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["ID", "Name", "Email", "Status", "Action", "Entries", "Details", "City", "Country", "When", "Landing Page URL", "Referring URL", "Facebook", "Twitter"])
        base = dt.datetime(2026, 5, 1, 10, 0, 0, tzinfo=dt.timezone(dt.timedelta(hours=10)))
        rows = [("Ann Lee", "a@example.com", "Valid", "Entry Confirmed", 1, "", "Sydney", "Australia", 0, "https://gleam.io/x", "https://mail.google.com/", "", "@ann"),
                ("Ann Lee", "a@example.com", "Valid", "Subscribe to Our List", 5, "", "Sydney", "Australia", 30, "https://gleam.io/x", "https://mail.google.com/", "", "@ann"),
                ("Ann Lee", "a@example.com", "Valid", "Refer 3 Friends", 3, "b@example.com", "Sydney", "Australia", 400, "https://gleam.io/x", "", "", "@ann"),
                ("Bob Ray", "b@example.com", "Valid", "Entry Confirmed", 1, "", "Toronto", "Canada", 5000, "https://gleam.io/x", "https://www.contestgirl.com/", "", ""),
                ("Cy Q", "c@example.com", "Invalid", "Subscribe to Our List", 5, "", "Leeds", "United Kingdom", 6000, "https://gleam.io/x", "https://www.contestgirl.com/", "", "")]
        for i, (nm, em, stt, act, en, det, city, co, off, lp, ref, fb, tw) in enumerate(rows):
            wr.writerow([i, nm, em, stt, act, en, det, city, co, (base + dt.timedelta(seconds=off)).strftime("%Y-%m-%d %H:%M:%S %z"), lp, ref, fb, tw])
    words = os.path.join(d, "w.json")
    with open(words, "w") as resource:
        json.dump({"verdict": "Two Entrants.", "assumptions": "Assuming a test.", "question": "Which was it for you?", "pills": [{"kind": "good", "text": "A pill"}],
                                                      "changes": [{"eyebrow": "Entry list", "title": "One change", "target": "3", "target_note": "addresses", "body": "Body.", "who": "Planner."}], "caveats": ["A caveat."]}, resource)
    wpath = words
    class A: export = p; words = wpath; site = None; impressions = 10; plan_cost = 50.0; prize_cost = 20.0; vertical = None; first_campaign = True; repeatable = False; days = None; methods = None; sends = None; partners = None; title = "Test"; dates = "1 May 2026"
    page = render(gather(A), words_of(words), site_of(None), A)
    assert reach_rows(RV.band_label(5298)) and reach_rows(RV.band_label(150)), "the reach table must resolve for every band label"
    for must in ("Two Entrants.", "A pill", "One change", "tab-levers", "id=\"emailShare\"", "Play With the Levers", "Ann L.", "Toronto, Canada", "Typical completions per Entrant, campaigns offering it", "Conversion Rate"):
        assert must in page, must
    assert "a@example.com" not in page and "{{" not in page and "per 100" not in page
    # Empty and all-invalid exports render through the command-line consumer.
    empty_path = os.path.join(d, "zero-valid.csv")
    empty_out = os.path.join(d, "zero-valid.html")
    for invalid_count in (0, 1):
        with open(empty_path, "w", newline="") as f:
            wr = csv.writer(f); wr.writerow(["User ID", "Action", "Entries", "Status"])
            wr.writerows([["ABC", "Visit", 40, "Invalid"]] * invalid_count)
        assert main([empty_path, "--out", empty_out, "--impressions", "10"]) == 0
        with open(empty_out, encoding="utf-8") as f:
            empty_page = f.read()
        assert "zero valid Entrants" in empty_page and "0.0%" in empty_page
        assert "Invalid Entries</td><td class=\"num\">" + str(invalid_count * 40) in empty_page
        assert ("100.0%" in empty_page) == bool(invalid_count)
        assert 'Actions each</td><td class="num">unavailable' in empty_page
        assert "benchmark comparisons are unavailable" in empty_page
        assert "better than" not in empty_page and 'type="range"' not in empty_page
    for weights in ([""], [40, "NaN"]):
        with open(empty_path, "w", newline="") as f:
            wr = csv.writer(f); wr.writerow(["User ID", "Action", "Entries", "Status"])
            wr.writerows([["ABC", "Visit", weight, "Invalid"] for weight in weights])
        assert main([empty_path, "--out", empty_out]) == 0
        with open(empty_out, encoding="utf-8") as f:
            empty_page = f.read()
        assert 'Invalid Entries</td><td class="num">unavailable' in empty_page
        assert 'Invalid Entries share</td><td class="num">unavailable' in empty_page
        assert "missing or unusable Entries weights" in empty_page
        assert 'Invalid action share</td><td class="num">100.0%' in empty_page
    # The explicit mapping reaches the report and dashboard without title inference.
    bonus_path = os.path.join(d, "bonus.csv")
    with open(bonus_path, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries", "Status"])
        wr.writerows([["a@example.com", "Complete daily bonus", 1, "Valid"],
                      ["a@example.com", "Complete daily bonus", 1, "Valid"],
                      ["b@example.com", "Subscribe", 1, "Valid"],
                      ["b@example.com", "Complete daily bonus", 1, "Invalid"]])
    class Bonus(A): export = bonus_path
    assert gather(Bonus)["R"]["speed"]["completed_everything"] is None
    class MappedBonus(Bonus): complete_all_action = "Complete daily bonus"
    mapped_bonus = gather(MappedBonus)
    assert mapped_bonus["R"]["speed"]["completed_everything"] == (1, 0.5)
    assert "Completed everything (explicitly mapped action): 1 Entrants (50%)." in render(mapped_bonus, words_of(words), site_of(None), MappedBonus)
    repeated = os.path.join(d, "repeated.csv")
    with open(repeated, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries"])
        for i in range(100):
            wr.writerow([f"person{i}@example.com", "Entry Confirmed", 1])
            if i < 50:
                for _ in range(10): wr.writerow([f"person{i}@example.com", "Visit a Page", 1])
    class Repeated(A): export = repeated
    repeated_data = gather(Repeated)
    visit = next(x for x in repeated_data["acts"] if x["name"] == "Visit a Page")
    assert visit["rate"] == 0.5 and visit["share"] == 5.0 and visit["completions"] == 500
    repeated_page = render(repeated_data, words_of(words), site_of(None), Repeated)
    assert '<td class="num">50%</td><td class="num">5.0</td>' in repeated_page
    assert "Unique participation" in repeated_page and "all campaign sizes offering that action" in repeated_page
    assert "completed by ${pct(a[5])} of Entrants" in repeated_page
    assert "campaigns your size that offered" not in repeated_page
    # Incomplete referral relationships remain unavailable throughout the dashboard.
    partial = gather(A)
    partial["R"]["viral"].update(graph_complete=False, graph_rows=0, referred_entrants=None,
                                referred_share=None, referral_conversion=None, lift=None, top_share=None, top=[])
    partial_page = render(partial, words_of(words), site_of(None), A)
    assert "Referral completions 1" in partial_page
    assert "relationships available for 0 of 1 completions" in partial_page
    assert "unavailable (referral relationships incomplete)" in partial_page
    assert "Referral relationships incomplete" in partial_page
    # Export labels must survive script embedding without adding executable markup.
    from html.parser import HTMLParser
    class ScriptParser(HTMLParser):
        def __init__(self):
            super().__init__(); self.scripts = []; self.in_script = False
        def handle_starttag(self, tag, attrs):
            if tag == "script": self.scripts.append(""); self.in_script = True
        def handle_endtag(self, tag):
            if tag == "script": self.in_script = False
        def handle_data(self, data):
            if self.in_script: self.scripts[-1] += data
    def embedded_data(document):
        parser = ScriptParser(); parser.feed(document); parser.close()
        assert len(parser.scripts) == 1, "an export label created another script element"
        return json.loads(parser.scripts[0].split("const DATA=", 1)[1].split(";\n", 1)[0])
    # Dashboard CLI accepts the same import configuration as the report.
    import contextlib, io
    for label, csv_text, options, mapping, unit, worth, completions, entries in (
        ("mapped", "Participant,Task,Points\na@example.com,Join newsletter,5\n", ["--map", "who=Participant,action=Task,Entries=Points"], {"who": "Participant", "action": "Task", "Entries": "Points"}, None, {}, 1, 5),
        ("boolean", "Email,Join newsletter\na@example.com,1\n", ["--wide-unit", "boolean", "--wide-worth", "Join newsletter=5"], {}, "boolean", {"Join newsletter": "5"}, 1, 5),
        ("completions", "Email,Join newsletter\na@example.com,2\n", ["--wide-unit", "completions", "--wide-worth", "Join newsletter=5"], {}, "completions", {"Join newsletter": "5"}, 2, 10),
        ("entries", "Email,Join newsletter\na@example.com,10\n", ["--wide-unit", "entries", "--wide-worth", "Join newsletter=5"], {}, "entries", {"Join newsletter": "5"}, 2, 10),
    ):
        imported = os.path.join(d, label + ".csv"); generated = os.path.join(d, label + ".html")
        with open(imported, "w") as resource: resource.write(csv_text)
        with contextlib.redirect_stdout(io.StringIO()):
            assert main([imported, "--out", generated, *options]) == 0
        with open(generated) as resource: data = embedded_data(resource.read())
        class ReportArgs(A): benchmark_cpl = None
        report = CR.analyze(CR.load(imported, mapping, unit, worth), ReportArgs)
        assert data["N"] == report["base"] == 1
        class Imported(A): export = imported; wide_unit = unit
        Imported.map = options[1] if label == "mapped" else None
        Imported.wide_worth = "Join newsletter=5" if unit else None
        totals = gather(Imported)["T"]
        assert totals["actions"] == report["topline"]["actions"] == completions
        assert totals["entries"] == report["topline"]["entries"] == entries
    for title in ("Visit our shop, then enter", "Visitez le café, puis entrez = oui"):
        imported = os.path.join(d, "wide-json.csv"); generated = os.path.join(d, "wide-json.html")
        with open(imported, "w", newline="", encoding="utf-8") as resource:
            writer = csv.writer(resource); writer.writerow(["Email", title]); writer.writerow(["a@example.com", 1])
        weights_json = json.dumps({title: 5}, ensure_ascii=False)
        with contextlib.redirect_stdout(io.StringIO()):
            assert main([imported, "--out", generated, "--wide-unit", "boolean", "--wide-worth-json", weights_json]) == 0
        with open(generated, encoding="utf-8") as resource: data = embedded_data(resource.read())
        assert data["N"] == 1 and title in [action[0] for action in data["acts"]]
        class JsonImported(A): export = imported; wide_unit = "boolean"; wide_worth_json = weights_json
        totals = gather(JsonImported)["T"]
        assert totals["actions"] == 1 and totals["entries"] == 5
    for options in (["--wide-worth-json", "{"], ["--wide-worth-json", "[]"],
                    ["--wide-worth", "Visit=1", "--wide-worth-json", '{"Visit": 1}']):
        with contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()):
            try: main([imported, "--out", generated, "--wide-unit", "boolean", *options])
            except SystemExit as error: assert error.code == 2
            else: raise AssertionError("invalid weight mapping must fail")
    ordinary = embedded_data(page)
    assert ordinary["N"] == 2 and ordinary["acts"]
    with open(p, encoding="utf-8") as source: timing_original = source.read()
    try:
        with open(p, "w", newline="") as source:
            wr = csv.writer(source); wr.writerow(["Email", "Action", "Entries", "When", "Referring URL"])
            wr.writerows([["a@example.com", "Visit", 1, "2026-05-01 10:00:00", "https://google.com/"],
                          ["a@example.com", "Follow on X", 1, "", "https://x.com/"],
                          ["b@example.com", "Visit", 1, "2026-05-02 10:00:00", "https://google.com/"],
                          ["c@example.com", "Visit", 1, "", "https://x.com/"]])
        timing_page = render(gather(A), words_of(words), site_of(None), A)
        timing = embedded_data(timing_page)
        assert timing["N"] == 3 and sum(x[1] for x in timing["sources"]) == 3
        assert ["Search", 1] in timing["sources"]
        assert ["Unknown first touch (incomplete timestamps)", 2] in timing["sources"]
        assert sum(x[1] for x in timing["daily"]) + timing["date_coverage"]["entrants_unknown"] == 3
        assert sum(x[2] for x in timing["daily"]) + timing["date_coverage"]["actions_unknown"] == 4
        assert "Unknown entry date: 2 Entrants" in timing_page and "Unknown action date: 2 Actions" in timing_page
        assert "Shares use all Entrants, including unknown first touch" in timing_page
    finally:
        with open(p, "w", encoding="utf-8") as source: source.write(timing_original)
    hostile = "</script><script>alert(1)</script>"
    with open(p, encoding="utf-8") as source: original_export = source.read()
    try:
        with open(p, "w", encoding="utf-8") as source:
            source.write(original_export.replace("Subscribe to Our List", hostile))
        hostile_page = render(gather(A), words_of(words), site_of(None), A)
        hostile_data = embedded_data(hostile_page)
        assert hostile in [action[0] for action in hostile_data["acts"]]
        assert hostile not in hostile_page
        assert "label.textContent=a[0]" in hostile_page and "t.textContent=text" in hostile_page
        special = "<>&\u2028\u2029"
        assert json.loads(script_json(special)) == special
        assert not any(c in script_json(special) for c in special)
    finally:
        with open(p, "w", encoding="utf-8") as source: source.write(original_export)
    with open(p, encoding="utf-8") as source: fractional_invalid = source.read().replace(",Invalid,Subscribe to Our List,5,", ",Invalid,Subscribe to Our List,5.5,")
    with open(p, "w", encoding="utf-8") as source: source.write(fractional_invalid)
    metrics = {row[0]: row for row in gather(A)["metrics"]}
    assert metrics["Invalid Entries"][1] == "5.5", metrics
    with open(p, encoding="utf-8") as source: fractional = source.read().replace(",Valid,Entry Confirmed,1,", ",Valid,Entry Confirmed,1.25,")
    with open(p, "w", encoding="utf-8") as source: source.write(fractional)
    fractional_page = render(gather(A), words_of(words), site_of(None), A)
    assert '>Entries</td><td class="num">10.5</td>' in fractional_page
    assert '>9.25</td>' in fractional_page and '>1.25</td>' in fractional_page
    small = gather(A)
    assert small["band"] == "below-100" and small["slices"] == {"band:below-100": {}}
    assert not small["reach"] and not small["pool"] and not any(small["seq"].values())
    assert all(x["typical"] is None and "starts at 100" in x["where"] for x in small["acts"])
    assert "100 to 250" not in fractional_page and "better than" not in fractional_page
    assert "Actual campaign metrics only" in fractional_page
    # The dashboard inherits the reader's zero-and-report weight policy.
    with open(p, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries"])
        wr.writerow(["x@example.com", "Subscribe", "NaN"])
    unweighted = gather(A)
    assert unweighted["T"]["entries"] == 0 and unweighted["T"]["unweighted_rows"] == 1
    assert "rows without a valid Entries value" in render(unweighted, words_of(words), site_of(None), A)
    # At the floor, comparisons remain available.
    with open(p, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries"])
        for i in range(100): wr.writerow([f"person{i}@example.com", "Subscribe to Our List", "1"])
    floor = gather(A)
    assert floor["band"] == "100-250" and floor["slices"]["all"]
    assert any(x["typical"] is not None for x in floor["acts"])
    # Invalid-only traffic retains its invalid rate without an engagement depth.
    with open(p, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries", "Status", "Referring URL"])
        for i in range(100): wr.writerow([f"person{i}@example.com", "Subscribe to Our List", 1, "Valid", "https://mail.google.com/"])
        wr.writerow(["invalid@example.com", "Subscribe to Our List", 1, "Invalid", "https://www.contestgirl.com/"])
    invalid_channel = gather(A)
    invalid_page = render(invalid_channel, words_of(words), site_of(None), A)
    assert any(c[1] == 0 and c[4] is None and c[5] == 1 for c in invalid_channel["R"]["channels"])
    assert '>unavailable</td><td class="num">100.0%</td>' in invalid_page
    assert all(c[1] > 0 for c in embedded_data(invalid_page)["sources"])
    assert "Earliest valid row's referrer" in invalid_page
    assert "Entrants and depth use each person's first valid source" in invalid_page
    assert "Actions and invalid rates use each row's source" in invalid_page
    assert "Depth is unavailable for channels with no valid first-touch Entrants" in invalid_page
    A.days, A.impressions = 20, 1000
    cautious_page = render(gather(A), words_of(words), site_of(None), A)
    assert "may explain part of this rate" in cautious_page and "operational health" in cautious_page
    assert "entry flow, required actions and traffic sources" in cautious_page
    assert "without anything being wrong" not in cautious_page
    A.days, A.impressions = None, 10
    # Missing benchmark files fail through the CLI with an actionable message.
    import contextlib, io
    saved_path, saved_data = RV.PCT_FILE, RV.PCT
    try:
        RV.PCT_FILE = os.path.join(d, "missing-percentiles.json"); RV.PCT = None
        error = io.StringIO()
        with contextlib.redirect_stderr(error):
            try: main([p, "--out", os.path.join(d, "missing.html")])
            except SystemExit as exc: assert exc.code == 2
            else: raise AssertionError("missing benchmarks must stop dashboard generation")
        assert "Benchmark data unavailable" in error.getvalue() and "Traceback" not in error.getvalue()
        assert not os.path.exists(os.path.join(d, "missing.html"))
    finally:
        RV.PCT_FILE, RV.PCT = saved_path, saved_data
    # The documented standalone scripts/ + references/ layout is sufficient.
    import shutil, subprocess
    standalone = os.path.join(d, "standalone")
    os.makedirs(os.path.join(standalone, "scripts")); os.makedirs(os.path.join(standalone, "references"))
    for name in ("dashboard.py", "campaign_report.py", "review.py", "gleam_export.py"):
        shutil.copyfile(os.path.join(HERE, name), os.path.join(standalone, "scripts", name))
    shutil.copyfile(RV.PCT_FILE, os.path.join(standalone, "references", "percentiles.json"))
    output = os.path.join(standalone, "dashboard.html")
    run = subprocess.run([sys.executable, "-W", "error::ResourceWarning", os.path.join(standalone, "scripts", "dashboard.py"),
                          p, "--out", output], capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    with open(output, encoding="utf-8") as resource: assert embedded_data(resource.read())["N"] == 100
    # Withheld metrics and whole cohorts remain unavailable in tiles and levers.
    import copy
    saved_pct = RV.PCT
    try:
        RV.PCT = copy.deepcopy(saved_pct)
        for metric in ("contestants", "entries_per_entrant", "actions_per_contestant"):
            RV.PCT["groups"]["band:100-250"][metric] = None
        hidden = gather(A)
        assert all(metric not in hidden["slices"]["band:100-250"] for metric in ("contestants", "entries_per_entrant", "actions_per_contestant"))
        assert "Benchmark unavailable" in render(hidden, words_of(words), site_of(None), A)
        RV.PCT["groups"]["band:100-250"] = None
        hidden_group = gather(A)
        assert "contestants" not in hidden_group["slices"]["band:100-250"]
        assert "Benchmark unavailable" in render(hidden_group, words_of(words), site_of(None), A)
    finally:
        RV.PCT = saved_pct
    # Only supplied settings select configured-duration/method comparisons.
    with open(p, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries", "When"])
        for i in range(100): wr.writerow([f"person{i}@example.com", "Subscribe to our newsletter", 1, "2026-05-01 10:00:00"])
    observed = {row[0]: row for row in gather(A)["metrics"]}
    assert "Duration in days" not in observed and "Entry actions" not in observed
    assert observed["Observed activity span in days"][1] == "1" and observed["Completed method titles"][1] == "1"
    A.days = 14; A.methods = 6
    configured = {row[0]: row for row in gather(A)["metrics"]}
    assert configured["Duration in days"][1] == "14" and configured["Entry actions"][1] == "6"
    A.days = A.methods = None
    for timestamps in ((None, None), ("bad-date", "bad-date"), ("2026-05-01 10:00:00", "bad-date"),
                       ("2026-05-01 10:00:00", "2026-05-02 10:00:00")):
        with open(p, "w", newline="") as f:
            wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries"] + (["When"] if timestamps[0] is not None else []))
            for i, timestamp in enumerate(timestamps):
                wr.writerow([f"person{i}@example.com", "Subscribe to our newsletter", 1] + ([timestamp] if timestamp is not None else []))
        dated = gather(A); page = render(dated, words_of(words), site_of(None), A)
        complete = sum(bool(CR.parse_when(t)) for t in timestamps if t)
        if not complete: assert "Retention unavailable" in page and "returned on a later day" not in page
        elif complete == 1: assert "Excludes 1 of 2 Entrants" in page
        else: assert "among 2 Entrants with complete usable timestamps" in page
    from gleam_export import load as export_load
    for titles, expected in ((("Subscribe to our YouTube channel",) * 2, 0),
                             (("Subscribe to our newsletter",) * 2, 2),
                             (("Subscribe to our YouTube channel", "Subscribe to our newsletter"), 1)):
        with open(p, "w", newline="") as f:
            wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries"])
            for i, title in enumerate(titles): wr.writerow([f"person{i}@example.com", title, 1])
        data = gather(A)
        assert data["emails"] == data["R"]["roi"]["emails"] == export_load(p)["assets"].get("emails", 0) == expected
        for title in titles:
            if "YouTube" in title:
                assert generic_name(title) != "Email Subscriptions" and RV.family(title) == "follow"
    with open(p, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["Email", "Action", "Entries"])
        wr.writerow(["one@example.com", "Subscribe to our newsletter", 1])
        wr.writerow(["one@example.com", "Subscribe to partner newsletter", 1])
        for i in range(9): wr.writerow([f"other{i}@example.com", "Entry Confirmed", 1])
    A.prize_cost = 100; A.prize_value = 1000; A.plan_cost = None
    data = gather(A); page = render(data, words_of(words), site_of(None), A)
    assert data["emails"] == data["R"]["roi"]["emails"] == 1 and data["email_completions"] == 2
    metrics = {r[0]: r[1] for r in data["metrics"]}
    assert metrics["Email subscription completions"] == "2"
    assert data["R"]["roi"]["per_entrant"] == 10 and data["R"]["roi"]["per_email"] == 100
    assert "10.00 per Entrant" in page and "100.00 per unique email subscriber" in page
    assert "Stated Prize value: 1,000.00" in page and '"emails": 1' in page
    A.prize_cost = None
    value_only = gather(A)
    assert "roi" not in value_only["R"]
    assert "Actual costs unavailable" in render(value_only, words_of(words), site_of(None), A)
    print("self-test passed"); return 0


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export", nargs="?"); ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--map", help="column mapping, e.g. who=Email Address,action=Entry Type,Entries=Points")
    ap.add_argument("--complete-all-action", help="exact exported title confirmed as the configured complete-all action; no title inference")
    ap.add_argument("--wide-unit", choices=("boolean", "completions", "entries"), help="required interpretation of per-method wide cells")
    weights = ap.add_mutually_exclusive_group()
    weights.add_argument("--wide-worth-json", help='JSON object mapping exact action titles to Entries per completion, e.g. {"Visit, then enter": 1}')
    weights.add_argument("--wide-worth", help="Entries per completion for each populated wide method, e.g. Join newsletter=5")
    ap.add_argument("--words", help="words.json written by the reviewer"); ap.add_argument("--site", help="site.json from the Reporting tab"); ap.add_argument("--out", default="dashboard.html")
    ap.add_argument("--impressions", type=int); ap.add_argument("--plan-cost", type=float); ap.add_argument("--prize-cost", type=float, help="actual Prize cost paid by the organizer"); ap.add_argument("--prize-value", type=float, help="stated retail Prize value, excluded from spending"); ap.add_argument("--vertical"); ap.add_argument("--first-campaign", action="store_true")
    ap.add_argument("--coverage-start", type=CR.dt.date.fromisoformat, help="first confirmed complete export day, YYYY-MM-DD in account time")
    ap.add_argument("--coverage-end", type=CR.dt.date.fromisoformat, help="last confirmed complete export day, inclusive, YYYY-MM-DD in account time")
    ap.add_argument("--repeatable", action="store_true"); ap.add_argument("--days", type=int); ap.add_argument("--methods", type=int); ap.add_argument("--sends"); ap.add_argument("--partners")
    ap.add_argument("--title", help="campaign name for the page"); ap.add_argument("--dates", help="run dates as the reader would say them, e.g. 6 to 16 August 2026, 10 days, ended")
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    if not a.export: ap.error("an export is required")
    try:
        page = render(gather(a), words_of(a.words), site_of(a.site), a)
    except ValueError as exc:
        ap.error(str(exc))
    with open(a.out, "w", encoding="utf-8") as resource:
        resource.write(page)
    print(f"dashboard written to {a.out}"); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
