# Versions

Repo version lives in `.claude-plugin/plugin.json` and `marketplace.json`. Bump the middle number for a new skill, the last number for changes to an existing skill, the first for restructures. Each skill carries its own `metadata.version` in its frontmatter and must be bumped on any shipped change, since that is what installed users compare against.

| Skill | Version | Last change |
|---|---|---|
| giveaway-prize-picker | 1.2.3 | 2026-09-09. Two modes, six criteria, taxonomy from 60,282 prize records, value bands by campaign size, budget calculator, evidence rules, Gleam reference. 2026-09-09, 1.0.1: own-product prize finding. 2026-09-09, 1.1.0: value-adjusted prize category and unit-count indexes, value regression, top-fifth profile, prize hierarchy and collaboration rule. 2026-09-09, 1.1.1: stated prize cost per email signup by category. 2026-09-09, 1.2.0: ROI script and cost benchmarks by vertical, band and year. 2026-09-09, 1.2.1: region and language proxies, description wording flags. 2026-09-09, 1.2.2: industries by value index, conversion, uptake and repeat organizers. 1.2.3: price-it step with industries and the ROI script, ROI eval. |
| giveaway-entry-method-planner | 1.1.4 | 2026-09-09. Action families with uptake, mixes by objective, method-count and referral findings, promotion rules from seventeen networks. 2026-09-09, 1.0.1: invalid-entry rates by method and opt-in checkbox uptake. 2026-09-09, 1.1.0: five jobs for actions, actions over-represented in top campaigns by vertical, action-count reconciliation. 2026-09-09, 1.1.1: yield per action and stated USD per completion. 2026-09-09, 1.1.2: pointer to cost per follow by vertical. 2026-09-09, 1.1.3: question types, share copy traits, visit destinations, newsletter wording. 1.1.4: write-the-actions step with wording, destinations and position. |
| giveaway-timing-and-duration | 1.2.3 | 2026-09-09. Duration, month, weekday and recency findings, timeline template, calendar by region. 2026-09-09, 1.0.1: organizer experience curve. 2026-09-09, 1.1.0: cadence table and persistence between consecutive campaigns. 2026-09-09, 1.1.1: overlapping campaigns, close day and hour. 2026-09-09, 1.2.0: holiday benchmarks by theme with lead days and a dated launch calendar. 1.2.1: Black Friday eval. 1.2.2: every start week benchmarked, live-over-holiday comparison, names checked against dates, calendar annotated. 1.2.3: smaller and obscure dates, named days, the holidays missing from the data. |
| giveaway-winner-structure | 1.2.1 | 2026-09-09. Structure findings, draw and contact rules, terms draft generator, Gleam drawing reference. 2026-09-09, 1.0.1: invalid entries before naming winners, custom terms adoption. 2026-09-09, 1.1.0: winner-verification reference (entry checks, account fraud signals, proof scaled to prize, failure handling). 2026-09-09, 1.2.0: one-prize default with the value-adjusted unit index. 2026-09-09, 1.2.1: what custom terms contain. |
| giveaway-promotion-plan | 1.0.1 | 2026-09-09. Channel playbook, email sequence, partner brief, paid rules. 2026-09-09, 1.0.1: top-fifth reach finding. |
| giveaway-random-draw | 1.2.0 | 2026-09-09. Provably fair draw: commit, public beacon seeds, hash-ranked selection, verify, audit record. 2026-09-09, 1.1.0: entrant-list reference (spreadsheets, platforms, comment exports), loader resolves nested JSON and prefers person fields over comment ids, script 2.2.0. 2026-09-09, 1.1.1: invalid-entry expectation in the pre-draw checklist. 2026-09-09, 1.2.0: pre-commit list scan for disposable domains, domain concentration and numbered handle runs, script 2.3.0. |
| giveaway-winner-communications | 1.0.1 | 2026-09-09. Message set from notification to non-winner, edge cases, contact log. 2026-09-09, 1.0.1: verification rule points at the proof ladder. |
| giveaway-idea-generator | 1.1.3 | 2026-09-09. Hook shares from 37,180 campaign titles, theme starters, mechanics, formats to avoid. 2026-09-09, 1.0.1: own product plus adjacent prize formula, collaboration rule. 2026-09-09, 1.0.2: title wording table. 2026-09-09, 1.0.3: pointer to the holiday benchmarks. 1.1.0: campaign types table from titles and descriptions with contestants, conversion, referrals and a value index. 2026-09-09, 1.1.1: launch subtypes, standout campaigns and their features, cheap prizes that drew crowds. 1.1.2: workflow quotes the types, launch and standout data, launch eval. 1.1.3: pointer to the smaller dates. |
| giveaway-results-review | 1.4.4 | 2026-09-09. Benchmarks by band, review script, reading guide with the impressions caveat and recommendation map. 2026-09-09, 1.0.1: what campaigns produced (yield per asset, by band, USD per completion), script reads asset totals against the band. 2026-09-09, 1.0.2: pricing step with the ROI script, start-year drift table. 2026-09-09, 1.1.0: percentile rank against all campaigns, the band, clean campaigns and the vertical, plus email and referral inputs. 1.1.1: impressions, actions per contestant, pace, action count and duration ranks, and a history file for comparison with the organizer's own campaigns. 1.2.0: invalid share removed from benchmarking, ranks added for entries, stated value per contestant, follows by network and per-action uptake by Gleam action name. 1.3.0: reads a Gleam Actions export directly (contestants, follows by network, emails, referrals, per-action counts mapped to Gleam action types, country and referrer splits, entrants file for the draw). 1.4.0: full campaign report in reporting-tab order from any export (Gleam as is, other platforms by column mapping, wide exports), with traffic channels, UTM, friction, referral graph, audience, retention, promotion lift and ROI on supplied inputs. 1.4.1: landing pages read as hosted, Gleam giveaways directory listing or embed, featured-listing traffic reported, aggregators grouped. 1.4.2: judgement-word rule, figures and ranks reported without verdicts unless the gap is large. 1.4.3: strengths first, every gap framed as a target with a route against the benchmark or the organizer's previous campaign. 1.4.4: eval 2 recorded, Gleam setup cross-link. |
| gleam-campaign-setup | 1.0.2 | 2026-09-09. Setup, User Details, How to Enter, Prize and Post Entry tabs, reporting and fraud, drawing winners, Gleam tips, all cited from the docs read 9 September 2026, plus settings evidence from the export (uptake by action, position effect, description length, templates, throwaway restriction). 2026-09-09, 1.0.1: pointer to the wording findings. 1.0.2: eval 2 recorded, tab placement of login controls stated. |

## 1.3.0 (2026-09-09)

The data pass. Every finding is reproducible from a script in `analysis/` and quoted in the skills as extracted, with sample sizes.

New benchmarks

- Holidays: contestants, conversion, duration and launch lead time for Christmas, Black Friday, the family days, Easter, Halloween, back to school and more, with a dated calendar of launch windows.
- Every week of the year: share of launches, contestants and conversion, with holiday-named campaigns checked against their dates, campaigns live over each holiday against the same-length campaigns that were not, and the smaller dates organizers used (St Patrick's, Earth Day, Prime Day, the national and world days) with the holidays nobody has taken.
- Campaign types from titles and descriptions: advent calendars, launches, collaborations, series, flash, cash, cart and wishlist, creator, community, charity, each with a value-adjusted index.
- Launches, pre-orders, drops and early access as their own rows.
- The campaigns that beat their prize money three times over, what they had in common, and the cheap prizes that drew crowds.
- Industries by value index, conversion, uptake, cost per result and repeat organizers.
- Region and language proxies, question types, share copy, visit destinations, description and terms wording, title wording, overlapping campaigns, close day, newsletter wording.
- What campaigns produced: email signups, follows by network, joins and referrals per campaign, and what each cost.

Results review

- Reads a Gleam Actions export, or another platform's export through column matching, into a full report in the order of the reporting tabs.
- Landing pages read as hosted page, Gleam giveaways directory listing or embed, with featured-listing traffic reported.
- Percentile ranks for a dozen metrics against all campaigns, the size band and the vertical, and per-action ranks by Gleam action type.
- Comparison against the organizer's own previous campaigns.
- Strengths first, and every gap framed as a target with a route.

Housekeeping

- Workflow steps now quote the new tables.
- CI runs the validator, every script self-test and a style lint on each push.
- Five new eval cases recorded.

## 1.2.0 (2026-09-09)

The results review reads exports.

Reports

- A full report from a Gleam Actions export or another platform's export, in the order of the reporting tabs: overview with insights, journey and heatmap, traffic by first-touch channel with UTM rollup and invalid rate per channel, entry methods with completion rate and seconds per action, the referral graph with top sharers, audience by country and city, retention, and ROI on supplied inputs.
- Other platforms read through column matching or a mapping, including one-column-per-method exports.

Benchmarks

- Percentile ranks for a dozen metrics against all campaigns, the size band and the vertical, and per-action ranks by Gleam action type.
- Comparison against the organizer's own previous campaigns.
- ROI script with cost per contestant, per email and per follow beside the benchmark for the industry, and cost benchmarks by vertical, band and year.
- What campaigns produced per asset (emails, follows, joins, referrals) and what each cost.

Housekeeping

- CI runs the validator, every script self-test and a repo-wide style lint on each push.
- Codex and Cursor install paths checked with the skills CLI.

## 1.1.0 (2026-09-09)

Two new skills and a data pass over the rest.

New skills

- giveaway-results-review: a finished campaign read against benchmarks for its size band, with a script that applies the impressions caveat and ranks each action against its family.
- gleam-campaign-setup: a plan turned into Gleam settings cited from the documentation (Setup, User Details, How to Enter, Prize and Post Entry tabs, reporting definitions, fraud filter, drawing winners), with what entrants did with each Gleam action in the export.

New findings in the existing skills

- Invalid-entry rates by action, organizer experience, custom terms adoption, opt-in checkbox uptake, own-product prizes.
- Value-adjusted prize category and unit-count indexes, the reach gap between the top and bottom fifth, cadence, persistence between consecutive campaigns, collaborations, and actions over-represented in top campaigns by vertical, all checked against Gleam's internal analysis before use.
- One prize worth wanting is now the default for acquisition.

Draw and verification

- A winner-verification reference: entry checks, account fraud signals, proof scaled to the prize, what to do when a drawn entry fails.
- The draw script scans the list before commit for disposable domains, domain concentration and runs of numbered handles.
- A guide to getting the entrant list out of spreadsheets, platforms and comment threads, and a loader that reads nested JSON exports.

## 1.0.0 (2026-09-09)

First public release. Eight platform-neutral skills for running giveaways, supported by Gleam.

The skills

- giveaway-idea-generator: three concepts with a hook, mechanic and prize direction, and the one to run.
- giveaway-prize-picker: recommend or evaluate a prize against six criteria, with a budget calculator and prize values by category and campaign size.
- giveaway-entry-method-planner: the actions entrants take, weighted, with promotion rules for seventeen networks read from the source pages.
- giveaway-timing-and-duration: run length, start date and a dated timeline, with a calendar by region.
- giveaway-winner-structure: winner counts, tiers, draw and redraw rules, and a terms draft with notes for AU, UK, US, EU and CA.
- giveaway-promotion-plan: a channel schedule with the posts, four emails and a partner brief written.
- giveaway-random-draw: a provably fair draw that commits to the list before the seed exists, seeds from a public beacon, and writes an audit record anyone can verify.
- giveaway-winner-communications: every message after the draw, from notification to the reply that ends a dispute.

The evidence

- An export of 54,675 giveaway campaigns with 1,000 or more contestants, 37,180 ordinary after excluding crypto, ambiguous and purchase-only campaigns.
- Committed as aggregates only. Every figure carries a sample size and none claims that a choice caused participation.
- Findings baked in: recency within 30 days, the cost of every extra action, the secret code, prize value bands, December, and the weekday that makes no difference.

The repository

- Analysis scripts that regenerate every table from a private export.
- A validator, evals with a style checker, plugin manifests for Claude Code, and an MIT licence.
- Install with the Claude Code plugin marketplace, the skills CLI, or by copying a skill folder.
