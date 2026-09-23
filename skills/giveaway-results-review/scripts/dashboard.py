#!/usr/bin/env python3
"""Build the results dashboard as one HTML file, from the export and the words the reviewer wrote.

  python3 dashboard.py export.csv --words words.json --out dashboard.html [--impressions N] [--plan-cost USD]
                       [--prize-cost USD] [--vertical NAME] [--first-campaign] [--site site.json]
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
def n(x): return f"{x:,.0f}"
def pct(x): return f"{x:.0%}"
def reader_unit(v): return f"{v:.0%}" if v <= 1 else f"{v:.1f} each"


def md_table(path, marker=None, header_starts=None):
    """Rows of the generated table under a marker, or the first table whose header starts with a phrase."""
    if not os.path.exists(path): return []
    text = open(path, encoding="utf-8").read()
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
  <div class="subhead"><h2>The Report, in the Order of the Reporting Tabs</h2><span class="note" style="margin:0">Every figure from the skill's report script on the export, so any sentence above can be checked against a table here. Where a typical figure sits beside a number it comes from campaigns the same size in Gleam campaign data; where none does, the data holds no comparison. Times are account time.</span></div>
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
        <p class="note">First day each Entrant acted, from the export.</p>
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
        <p class="note">Earliest row's referrer. Email clicks arrive as webmail or direct and are undercounted. No benchmark: the campaign data holds no comparison for traffic mix, so this tab describes this campaign alone.</p>
      </div>
      <div class="card">
        <h3>Channels, With Depth and Invalid Rate</h3>
        {{CHANNELS}}
        <p class="note">Signals, never verdicts.</p>
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
        <h3>Every Entry Method, Share of Entrants Who Completed It</h3>
        <div class="toggle" role="group" aria-label="Sort actions"><button id="sortShare" aria-pressed="true">By completion</button><button id="sortOrder" aria-pressed="false">Campaign order</button></div>
      </div>
      <div class="legend"><span><i style="background:var(--s-visit)"></i>Page visit</span><span><i style="background:var(--s-email)"></i>Email</span><span><i style="background:var(--s-follow)"></i>Follow</span><span><i style="background:var(--s-share)"></i>Share or refer</span><span><i style="background:var(--s-content)"></i>Content</span><span><i style="background:var(--s-other)"></i>Bonus or other</span><span>&#124; tick marks the typical share for that kind of action, where one exists</span></div>
      <div class="acts" id="acts"></div>
      <p class="note">Typical is the share of Entrants completing that kind of action across campaigns your size that offered it, and it reads as "each" where people complete it more than once.</p>
    </div>
    <div class="card" style="margin-top:16px">
      <h3>Drop-Off, Friction and Speed</h3>
      {{FRICTION}}
      <p class="note">Typical is the completion rate of campaigns your size that offered that kind of action, and the rank is the share of them this campaign beats. Typical seconds is the gap from the Entrant's previous action, in-session gaps under 30 minutes only.</p>
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
        <p>Retention by distinct active days: {{RETENTION}}. One-day dominance is normal for a giveaway.</p>
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
  function showTip(t,host,x,y,html){t.innerHTML=html;t.style.left=x+"px";t.style.top=y+"px";t.classList.add("on");}
  function hideTip(t){t.classList.remove("on");}
  function short(d){const m=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];const p=d.split("-");return (+p[2])+" "+m[+p[1]-1];}

  // daily: area of new Entrants with the peak marked
  (function(){
    const daily=DATA.daily;if(!daily||daily.length<2)return;
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
      showTip(tip,host,xs(i)*r.width/W,ys(daily[i][1])*r.height/H,`<b>${short(daily[i][0])}</b> ${fmt(daily[i][1])} new Entrants, ${fmt(daily[i][2])} actions`);});
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
      hit.addEventListener("mousemove",()=>{const r=svg.getBoundingClientRect();showTip(tip,host,(xs(d[1])/2+pl/2)*r.width/W,y*r.height/H,`<b>${d[0]}</b> ${fmt(d[1])} Entrants, ${pct(d[1]/total)}`);});
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
    list.innerHTML='<div class="act"><span class="hd">Entry Method</span><span class="hd">Share of Entrants</span><span class="hd pct">This</span><span class="hd typ">Typical</span></div>';
    const rows=order==="share"?[...DATA.acts].sort((a,b)=>b[2]-a[2]):DATA.acts;
    const scale=Math.max(1.5,...rows.map(a=>a[2]),...rows.map(a=>a[3]||0));
    rows.forEach(a=>{const r=document.createElement("div");r.className="act";
      const tick=a[3]==null?"":`<span class="tick" style="left:${Math.min(100,a[3]/scale*100)}%" title="typical ${a[3]<=1?Math.round(a[3]*100)+"%":a[3].toFixed(1)+" each"}"></span>`;
      r.innerHTML=`<span class="n" title="${a[0]}">${a[0]}</span><span class="track" aria-hidden="true"><span class="fill" style="width:${a[2]/scale*100}%;background:${fam[a[4]]||fam.other}"></span>${tick}</span><span class="pct num">${pct(a[2])}</span><span class="typ num">${a[3]==null?"n/a":a[3]<=1?Math.round(a[3]*100)+"%":a[3].toFixed(1)+" each"}</span>`;
      r.setAttribute("aria-label",`${a[0]}, ${famName[a[4]]||"other"}, completed by ${pct(a[2])} of Entrants, ${fmt(a[1])} completions`);
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
  function upd1(){const sh=+es.value/100;ec.innerHTML=fmt(Math.round(sh*N))+' <small>addresses if <span>'+Math.round(sh*100)+'%</span> of your '+fmt(N)+' Entrants sign up</small>';const t=SL[DATA.band].email;if(!t){er.textContent="";return;}er.textContent="Campaigns your size that ran an email action typically got a signup from "+(t.p[9]>=0.95?"almost every Entrant":Math.round(t.p[9]*100)+"% of Entrants")+". At "+Math.round(sh*100)+"% you'd be ahead of "+beats(sh,t)+"% of them, across "+fmt(t.n)+" campaigns.";}
  es.addEventListener("input",upd1);upd1();
  const en=document.getElementById("ent"),enb=document.getElementById("entBand"),enr=document.getElementById("entRank");
  function upd2(){const n=+en.value;const k=bandOf(n),b=SL[k];enb.innerHTML='<span>'+fmt(n)+'</span> <small>Entrants puts you with campaigns of '+b.label+', where the typical one gets '+fmt(Math.round(b.contestants.p[9]))+', with '+b.entries_per_entrant.p[9].toFixed(1)+' Entries and '+b.actions_per_contestant.p[9].toFixed(1)+' actions each</small>';enr.textContent="That beats "+beats(n,SL.all.contestants)+"% of all "+fmt(SL.all.contestants.n)+" campaigns and "+beats(n,b.contestants)+"% of the "+fmt(b.contestants.n)+" your size. Getting there is what the promotion plan is for.";}
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
    rows = CR.load(a.export)
    class A: impressions = a.impressions; prize_value = a.prize_cost; plan_cost = a.plan_cost; benchmark_cpl = None; sends = a.sends; partners = a.partners.split(",") if a.partners else None
    R = CR.analyze(rows, A); T = R["topline"]; N = R["base"]
    class B: pass
    b = B(); b.contestants = N; b.impressions = a.impressions; b.entries = T["entries"]; b.invalid = int(R["topline"].get("invalid_entries", 0) or 0)
    b.days = a.days or ((R["end"] - R["start"]).days + 1 if R.get("start") else None); b.methods = a.methods or len(R["actions"])
    emails = sum(comp for act, comp, *_ in R["actions"] if kind(act) == "emails")
    b.emails = emails or None
    b.referrals = R["viral"]["refer_rows"]; b.actions_completed = T["actions"]; b.prize_value = None
    for k in ("x_follows", "instagram_follows", "tiktok_follows", "twitch_follows", "youtube_subscribes", "discord_joins"): setattr(b, k, None)
    b.vertical = a.vertical; b.repeatable = a.repeatable; b.first_campaign = a.first_campaign; b.actions = None; b.history = None
    metrics = RV.review(b)
    RV.PCT = RV.PCT or RV.load_pct(); band = RV.band(N); band_label = RV.band_label(N)
    groups = RV.PCT.get("groups", {})
    def slice_of(key): return {m: {"n": groups[key][m]["n"], "p": groups[key][m]["p"]} for m in ("contestants", "email_uptake", "entries_per_entrant", "actions_per_contestant") if m in groups.get(key, {})}
    bands = {"band:100-250": ("100 to 250", 100, 250), "band:250-500": ("250 to 500", 250, 500), "band:500-1k": ("500 to 1,000", 500, 1000),
             "band:1k-2.5k": ("1,000 to 2,500", 1000, 2500), "band:2.5k-10k": ("2,500 to 10,000", 2500, 10000), "band:10k+": ("10,000 or more", 10000, 10 ** 9)}
    slices = {k: dict(label=v[0], lo=v[1], hi=v[2], **slice_of(k)) for k, v in bands.items()}
    slices["all"] = slice_of("all")
    acts = []
    for act, comp, uniq, share, rate, sec, inv in R["actions"]:
        g = generic_name(act); fam = RV.family(act) or "other"
        t = RV.PCT.get("per_action_uptake", {}).get(g) if g else None
        typ = t["p"][9] if t else None; rr = RV.rank(comp / N, t) if t else None
        acts.append({"name": act, "completions": comp, "share": comp / N, "typical": typ, "family": fam if fam in FAMILY_COLOUR else "other",
                     "where": (f"better than {rr[0]}% of {n(rr[1])} offering {g}" if rr else "no matching group"), "entrants": uniq, "share_actions": share, "rate": rate, "seconds": sec, "invalid": inv})
    return {"R": R, "T": T, "N": N, "emails": emails, "metrics": metrics, "band": band, "band_label": band_label, "slices": slices, "acts": acts,
            "reach": reach_rows(band_label), "pool": pool_rows(), "seq": seq_rows(), "insights": CR.insights(R)}


def words_of(path):
    W = {"assumptions": "Write the assumptions line here.", "verdict": "Write the verdict here: what the campaign did well with its rank, then the figure with the most room to close.",
         "pills": [], "changes": [], "caveats": [], "question": "End on the one question that would change the advice."}
    if path: W.update(json.load(open(path, encoding="utf-8")))
    return W


def site_of(path):
    S = {"name": "", "url": "", "headerLogo": None, "headerColour": None, "elementsColour": None, "backgroundColour": None}
    if path: S.update(json.load(open(path, encoding="utf-8")))
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
    t = [("Entrants", n(N), f"{D['band_label']} band"), ("Entries each", f"{T['entries_per_entrant']:.1f}", f"{D['slices'][('band:' + D['band'])]['entries_per_entrant']['p'][9]:.1f} typical for your size"),
         ("Actions each", f"{T['actions_per_entrant']:.1f}", f"{D['slices'][('band:' + D['band'])]['actions_per_contestant']['p'][9]:.1f} typical for your size"),
         ("Referred Entrants", n(V["referred_entrants"]), f"{V['referred_share']:.0%} of Entrants")]
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
    R, T, N = D["R"], D["T"], D["N"]; V = R["viral"]; E = R["engagement"]; Sp = R["speed"]
    title = a.title or "Campaign Results Review"
    meta = [x for x in [a.dates, f"{D['band_label']} band", a.vertical and f"{a.vertical.replace('_', ' ')} vertical", "First campaign at this size" if a.first_campaign else None] if x]
    pills = "".join(f'<span class="pill {esc(p.get("kind", ""))}"><i></i>{esc(p["text"])}</span>' for p in W["pills"])
    daily = [(d.isoformat(), ne, ac) for d, ne, ac in R.get("by_day", [])]
    heat = [[R["heat"][(d, h)] for d in range(7)] for h in range(24)]
    heat_peak = R["heat_peak"]
    ins = "".join(f"<li>{esc(i)}</li>" for i in D["insights"])
    topline = table(["Metric", "Value"], [("Entrants (unique valid emails)", n(N)), ("Actions completed", n(T["actions"])), ("Entries", n(T["entries"])), ("Actions each", f"{T['actions_per_entrant']:.1f}"), ("Entries each", f"{T['entries_per_entrant']:.1f}"),
                                          ("Invalid actions", f"{n(T['invalid_actions'])} ({T['invalid_rate']:.1%} of rows)")] + ([("Conversion Rate", f"{N / a.impressions:.1%}")] if a.impressions else []))
    speed = (f"Of {n(Sp['multi'])} multi-action Entrants, first to last {Sp['median_span_min']:.0f} minutes typical, {Sp['within_10_min']:.0%} done within 10 minutes, {Sp['one_sitting']:.0%} in one sitting." if Sp.get("multi") else "")
    journey = f"Entered {n(N)} (100%), completed more than one action {n(N - E['1'][0])} ({(N - E['1'][0]) / N:.0%}), shared {n(V['sharers'])} ({V['participation']:.0%}), referred new Entrants {n(V['referred_entrants'])}. Referrals are an output per sharer, never a stage, so this is not a funnel."
    channels = table(["Channel", "Entrants", "Share", "Actions", "Depth vs average", "Invalid rate"], [(c[0], n(c[1]), pct(c[2]), n(c[3]), f"{c[4]:.2f}x", f"{c[5]:.1%}") for c in R["channels"]])
    hosts = table(["Host", "Entrants"], [(h, n(c)) for h, c in R["hosts"]])
    landing = ", ".join(f"{k} {n(v)} ({v / N:.0%})" for k, v in R["landing"])
    utm = table(["Source", "Medium", "Campaign", "Entrants"], [(u[0][0], u[0][1], u[0][2], n(u[1])) for u in R["utm"]], num_from=3) if R["utm"] else "<p class=\"note\">No UTM parameters on any landing page.</p>"
    friction = table(["Action", "Completions", "Entrants", "Share of actions", "Completion rate", "Typical, campaigns offering it", "Where it sits", "Typical seconds", "Invalid"],
                     [(x["name"], n(x["completions"]), n(x["entrants"]), pct(x["share_actions"]), pct(x["rate"]), reader_unit(x["typical"]) if x["typical"] else "-", x["where"], (f"{x['seconds']:.0f}" + (" (slow)" if x["seconds"] > 120 else "")) if x["seconds"] is not None else "-", n(x["invalid"])) for x in D["acts"]])
    sharers = table(["Sharer", "Referrals", "Entered", "Entries brought", "Connected accounts", "Referred doing one action"], [(s[0], n(s[1]), n(s[2]), n(s[3]), s[4], s[5]) for s in V["top"]]) if V["top"] else ""
    countries = [(c, v) for c, v in R["countries"]]
    cities = table(["City", "Entrants"], [(f"{c[0][0]}, {c[0][1]}", n(c[1])) for c in R["cities"]]) if R["cities"] else ""
    handles = ", ".join(f"{c} {v:.0%}" for c, v in R["handles"]) if R["handles"] else "none recorded"
    ret = R["retention"]; retention = ", ".join(f"{k} day{'s' if k != '1' else ''} {n(v[0])} ({v[1]:.0%})" for k, v in ret.items())
    engaged = table(["Entrant", "Actions", "Entries", "Referred", "Days active", "Connected accounts"], [(t[0], t[1], n(t[2]), t[3], t[4], t[5]) for t in R["top_entrants"]])
    caveats = "".join(f"<li>{esc(c)}</li>" for c in W["caveats"])
    bslice = D["slices"]["band:" + D["band"]]
    email_share = D["emails"] / N if D["emails"] else 0
    data = {"N": N, "emails": D["emails"], "daily": daily, "depth": [(k, v[0]) for k, v in E.items()], "sources": [(c[0], c[1]) for c in R["channels"]],
            "countries": countries, "acts": [(x["name"], x["completions"], x["share"], x["typical"], x["family"]) for x in D["acts"]], "heat": heat, "slices": D["slices"], "band": "band:" + D["band"],
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
      <div class="change"><div class="eyebrow">Next Campaign</div><h3>Aim Bigger Next Time</h3><input type="range" id="ent" min="100" max="{max(20000, N * 2)}" value="{N}" step="1" aria-label="Entrants on the next run"><div class="target num" id="entBand"></div><p id="entRank" class="note" style="margin:0"></p></div>
      <div class="change"><div class="eyebrow">Your Spend</div><h3>What Your Prize Bought You</h3><input type="range" id="prize" min="0" max="{max(5000, int(a.prize_cost or 0) * 2)}" value="{int(a.prize_cost or 0)}" step="10" aria-label="Prize cost"><div class="target num" id="prizePer"></div><p class="note" style="margin:0">Worked on your {n(N)} Entrants{(" and " + n(data["emails"]) + " addresses") if data["emails"] else ""}. Cost benchmarks by vertical live in the Prize picker.</p></div>
      {reach_card}
      {pool_card}
      <div class="change"><div class="eyebrow">Run It Again</div><h3>Your Next One</h3><div class="target num">{esc(surv.split(" of ")[0]) if surv else "-"} <small>{esc(surv.split(" ", 1)[1]) if surv else "no sequence table found in the references"}</small></div><p class="note" style="margin:0">{esc(nextrun)}</p></div>
    </div>
  </div>'''
    page = TEMPLATE
    for k, v in {"TITLE": esc(title), "META": "".join(f"<span>{esc(m)}</span>" for m in meta), "PILLS": pills, "VERDICT": esc(W["verdict"]), "ASSUME": esc(W["assumptions"]), "TILES": tiles(D),
                 "BANDLABEL": esc(D["band_label"]), "BANDN": n(bslice["contestants"]["n"]) if bslice.get("contestants") else "-", "METRICROWS": metric_rows(D), "CHANGES": change_cards(W), "INSIGHTS": ins, "TOPLINE": topline, "SPEED": esc(speed), "JOURNEY": esc(journey),
                 "HEATPEAK": esc(f"Peak {CR.DAYS[heat_peak[0][0]]} {heat_peak[0][1]:02d}:00, {n(heat_peak[1])} actions") if heat_peak else "", "CHANNELS": channels, "HOSTS": hosts, "LANDING": esc(landing), "UTM": utm, "FRICTION": friction,
                 "VIRALLINE": esc(f"Referral completions {n(V['refer_rows'])}, sharers {n(V['sharers'])} ({V['participation']:.0%} of Entrants), referred Entrants who entered {n(V['referred_entrants'])} ({V['referred_share']:.0%}), {V['referrals_per_sharer']:.1f} per sharer." if V["sharers"] else "No referral action ran."),
                 "SHARERS": sharers, "CITIES": cities, "HANDLES": esc(handles), "RETENTION": esc(retention), "ENGAGED": engaged, "CAVEATS": caveats, "QUESTION": esc(W["question"]), "LEVERS": levers,
                 "NCOUNTRIES": n(len(set(c for c, _ in countries))) if countries else "0", "DATA": json.dumps(data)}.items():
        page = page.replace("{{" + k + "}}", v)
    assert "{{" not in page, re.findall(r"\{\{\w+\}\}", page)[:5]
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
    words = os.path.join(d, "w.json"); json.dump({"verdict": "Two Entrants.", "assumptions": "Assuming a test.", "question": "Which was it for you?", "pills": [{"kind": "good", "text": "A pill"}],
                                                  "changes": [{"eyebrow": "Entry list", "title": "One change", "target": "3", "target_note": "addresses", "body": "Body.", "who": "Planner."}], "caveats": ["A caveat."]}, open(words, "w"))
    wpath = words
    class A: export = p; words = wpath; site = None; impressions = 10; plan_cost = 50.0; prize_cost = 20.0; vertical = None; first_campaign = True; repeatable = False; days = None; methods = None; sends = None; partners = None; title = "Test"; dates = "1 May 2026"
    page = render(gather(A), words_of(words), site_of(None), A)
    assert reach_rows(RV.band_label(5298)) and reach_rows(RV.band_label(150)), "the reach table must resolve for every band label"
    for must in ("Two Entrants.", "A pill", "One change", "tab-levers", "id=\"emailShare\"", "Play With the Levers", "Ann L.", "Toronto, Canada", "Typical, campaigns offering it", "Conversion Rate"):
        assert must in page, must
    assert "a@example.com" not in page and "{{" not in page and "per 100" not in page
    print("self-test passed"); return 0


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export", nargs="?"); ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--words", help="words.json written by the reviewer"); ap.add_argument("--site", help="site.json from the Reporting tab"); ap.add_argument("--out", default="dashboard.html")
    ap.add_argument("--impressions", type=int); ap.add_argument("--plan-cost", type=float); ap.add_argument("--prize-cost", type=float); ap.add_argument("--vertical"); ap.add_argument("--first-campaign", action="store_true")
    ap.add_argument("--repeatable", action="store_true"); ap.add_argument("--days", type=int); ap.add_argument("--methods", type=int); ap.add_argument("--sends"); ap.add_argument("--partners")
    ap.add_argument("--title", help="campaign name for the page"); ap.add_argument("--dates", help="run dates as the reader would say them, e.g. 6 to 16 August 2026, 10 days, ended")
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    if not a.export: ap.error("an export is required")
    page = render(gather(a), words_of(a.words), site_of(a.site), a)
    open(a.out, "w", encoding="utf-8").write(page); print(f"dashboard written to {a.out}"); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
