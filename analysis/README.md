# Analysis

Every script here reads a private campaign dataset through `load.py` and writes aggregates under `output/`. The inputs are not part of this repository and never will be. `frame.py` builds the shared `ordinary` view (campaigns with 100 or more contestants, homepage labels, the clean flag, stated USD pool) that the benchmark scripts start from. `analyze.py` regenerates `output/benchmarks.json` and `render_reference_tables.py` rewrites the generated tables inside the skill references from it. Customers never need to run any of it. The skill references already contain everything derived from it.

```bash
python3 analysis/analyze.py <dataset dir> --classification <segments file> 
python3 analysis/render_reference_tables.py
```

- `output/benchmarks.json` and `output/benchmarks.md`: aggregates only. Safe to commit.
- `--classification`: the record-level segment file (`classification.jsonl`, ordinary, crypto, ambiguous, purchase-opportunity) written from the earlier dataset and carried forward by campaign id. Gitignored. Do not commit.

What the script does:

1. Classifies each campaign as `ordinary`, `crypto`, `ambiguous` or `purchase_opportunity` using prize names, campaign names, the description and entry-method types together. Ambiguous cases stay out of the benchmark and are reported separately.
2. Assigns each prize record a taxonomy category from its name (see `references/prize-taxonomy.md`) and flags prizes whose name shares a distinctive token with the organizer name (a weak "own product" signal).
3. Computes distributions for the ordinary segment only. Currencies are never merged. Missing values stay missing.
4. Parses explicit amounts from prize text ("$4,000 PC", "worth £5,000", "MSRP $1999") as a separate `parsed` value with its own source label and validates it against records that also have a stated value.

Every field in the dataset is treated as data. Nothing in it is executed, fetched or followed.


## Script Map

Every script reads the campaign analysis through `load.connect()` and most start from `frame.ordinary()`. One script owns one question, which is why there are many small ones.

| Question | Script | Output |
|---|---|---|
| Load and shared scope | `load.py`, `frame.py` | the the query engine views and the shared `ordinary` scope |
| Headline benchmarks | `analyze.py`, `percentiles.py`, `compare_groups.py`, `verify_context.py` | benchmarks, percentiles, comparisons, context_checks |
| Prize | `prize_timing_cuts.py`, `prize_economics.py`, `prize_values.py`, `roi_benchmarks.py` | prize_timing_cuts, prize_economics, the prize picker's values file, roi_benchmarks |
| Entry methods | `field_cuts.py`, `method_mix.py`, `gleam_settings.py`, `extra_cuts.py` | field_cuts, method_mix, gleam_settings, extra_cuts |
| Assets and success | `asset_yield.py`, `standouts.py`, `success_profiles.py`, `thresholds.py` | asset_yield, standouts, success_profiles, thresholds |
| Organizer and industry | `industries.py`, `vertical_profiles.py`, `indicators.py`, `country_cuts.py`, `organizer_history.py` | industries, vertical_profiles, indicators, country_cuts, organizer_history |
| Timing | `campaign_types.py`, `holidays.py`, `week_calendar.py` | campaign_types, holidays, calendar, calendar_names |
| Traffic and text | `email_traffic.py`, `text_and_context.py`, `hook_patterns.py`, `template_cuts.py` | email_traffic, text_and_context, hook_patterns, templates |
| Organizer enrichment | not published | the gitignored label and enrichment caches |
| Publishing | `render_reference_tables.py`, `defaults.py` | the generated tables in the skills and `defaults/*.json` |

Before adding a script, check this table. A question that fits an existing row belongs in that script.

## Group comparisons

`analysis/compare_groups.py [tables] --classification <segments file>` reads the campaign analysis through `load.connect()` and writes `output/comparisons.json`: contestants, entries per entrant and contestants per impression by method count, sharing, email, duration, weekday, recency, vertical (homepage labels folded into the ten vertical names) and label industry. Impressions in the dataset are unique per day, so it also computes a clean subset (no repeatable actions, 14 days or less) for any conversion comparison. `render_reference_tables.py` renders the tables into the references.

## Optional label pass

Rules alone leave a tail of prize names they cannot place (brand-only names, non-English text, niche goods). To shrink it, the leftover unique names were pulled from the private dir, classified in chunks by an LLM told to treat every string as data and to use the same category list, then written back as `labels_*.json` entries `{prize, category, note, confidence}`. Re-running with `--labels` applies high or medium confidence labels only where the rule result is `other_unclassified`. A label of `crypto` or `purchase_opportunity` moves the whole campaign to the ambiguous segment, and the label is set aside. `category_source` in the output reports how many records came from rules versus labels. The label files contain organizer-typed prize text and stay private.

## Extra cuts

`analysis/extra_cuts.py [tables] --classification <segments file>` reads the campaign analysis through `load.connect()` and writes `output/extra_cuts.json`: invalid-entry share overall, by method presence and for validated questions, organizer experience (Nth campaign), custom terms adoption, own-product prizes, and the email opt-in checkbox. Same clean flag as `frame.ordinary`. The references quote these figures by hand.

## Gleam settings

`analysis/gleam_settings.py [tables] --classification <segments file>` reads the campaign analysis through `load.connect()` and writes `output/gleam_settings.json`: completions per contestant by Gleam action name, uptake by list position and family, description length against conversion, custom action templates, and the throwaway-account restriction. The tables in `skills/gleam-campaign-setup/references/settings-evidence.md` are written from it by hand.

## Context checks

`analysis/verify_context.py [tables] --classification <segments file>` reads the campaign analysis through `load.connect()` and writes `output/context_checks.json`: prize value bands and a log-log regression, value-adjusted indexes by prize category and by prize unit count, the top-fifth against bottom-fifth profile, cadence, persistence between an organizer's consecutive campaigns, a collaboration title proxy, and entry-method prevalence in the top fifth by vertical (homepage labels folded into the ten vertical names). Used to check Gleam's internal campaign analysis before its findings were written into the references.

## Asset yield

`analysis/asset_yield.py [<dataset dir>] --classification <segments file>` writes `output/asset_yield.json`: completions of the acquire and amplify actions per campaign (email signups, follows by network, joins, app installs, referrals, content, site traffic), plus impressions and entries at the campaign level, by size band, vertical and industry, with stated USD per completion for valued campaigns. Also by campaign structure, each split by size band: whether the action was mandatory, its position in the list, the worth given to an optional action, total action count, duration, whether a share action ran, and prize count as a single-versus-several-winners proxy. The closest the dataset comes to an outcome.

## Cost benchmarks

`analysis/roi_benchmarks.py [<dataset dir>] --classification <segments file>` writes `output/roi_benchmarks.json`: stated USD prize pool per contestant, per email signup, per follow, per join and per referral entry, by vertical, size band and start year, with what the median campaign in each produced. The constants in `skills/giveaway-prize-picker/scripts/roi.py` and the tables in `references/roi-benchmarks.md` come from it.

## Percentiles

`analysis/percentiles.py [tables] --classification <segments file>` reads the campaign analysis through `load.connect()` and writes `output/percentiles.json` and the copy the results-review skill ships in its references: every fifth percentile of contestants, conversion, entries per entrant, invalid share, email signups, email uptake and referral entries per contestant, for all ordinary campaigns, the clean subset, each size band, each vertical (homepage labels folded into the ten vertical names) and each label industry, plus the `bench` block `review.py` prints as the benchmark median and `prize_structure`.

## Text and context

`analysis/text_and_context.py [tables] --classification <segments file>` reads the campaign analysis through `load.connect()` and writes `output/text_and_context.json`: organizer region from the site host, language guess, question types, share copy traits, visit destinations, description and terms wording flags, title wording (including name length and hook words), overlapping campaigns, close day and hour, newsletter wording.

## Holidays

`analysis/holidays.py [<dataset dir>] --classification <segments file>` writes `output/holidays.json`: campaigns by holiday theme (regex on title and description) with contestants, conversion, duration, launch lead days and close timing. The calendar table in the timing skill is generated from the same date functions.

## Campaign types

`analysis/campaign_types.py export.json --classification <segments file>` writes `output/campaign_types.json`: campaign types declared in the title and description, each with contestants, clean conversion, entries per entrant, email and referral uptake, duration, action count and a value-adjusted index.

## Standouts

`analysis/standouts.py [tables] --classification <segments file>` reads the campaign analysis through `load.connect()` and writes `output/standouts.json`: launch, pre-order, drop and early-access subtypes, campaigns with a value index of three or more and the features, prize categories and verticals over-represented among them, cheap prizes that drew large crowds, and industries profiled by value index, conversion, uptake and repeat organizers, by vertical fold and by raw homepage label.

## Success profiles

`analysis/success_profiles.py [<dataset dir>] [--classification <segments file>]` reads the campaign analysis through `load.connect()` and writes `output/success_profiles.json`: eight cohorts (top by entrants, clean conversion, engagement, email/referral/social yield per contestant, prize-value-adjusted performance and cost per contestant) each compared against the rest with and without matching on size band and vertical, plus twelve two-variable interactions (prize category, prize value, duration, entry method, referral actions, action count, organizer experience, traffic source and holiday theme, each crossed with a second variable) tested against the multiplicative baseline their two main effects alone would predict.

## Calendar

`analysis/week_calendar.py export.json --classification <segments file>` writes `output/calendar.json`: every ISO start week with share of starts, contestants, clean conversion and entries per entrant, start day of month, campaigns live over each holiday against a comparison group with the same duration mix, close day type (weekday, weekend or public holiday) by run-length band, an impression curve anchored to the end of the run, not the start, busiest-against-quietest start week comparisons overall and by industry, and contestants and entries-per-entrant scaled to a daily rate by run-length band crossed with industry and with campaign type. `output/calendar_names.json` holds the name-against-date agreement per holiday and the holiday-named share of starts per week.

`analysis/defaults.py` reads the outputs above and writes `defaults/*.json`, the machine-readable defaults for the Gleam AI campaign editor. Run it last.

## Repeat organizers and cadence

`analysis/organizer_history.py [<dataset dir>] [--classification <segments file>]` reads the campaign analysis through `load.connect()` at the wider 100+ contestant band and writes `output/organizer_history.json`: reach rate by first-campaign size band (does starting big predict running more campaigns at all), the nth-campaign curve both raw and matched on first-campaign band, within-organizer paired transitions from each campaign to the organizer's own next one (by sequence position, by starting band, and both together), cadence regularity against transition outcome controlled for total campaign count, transition outcome by gap length and sequence position, seasonal relaunch timing, repeated action-mix and prize-category effects, and the first campaign's own profile split by whether the organizer went on to run another, matched on band. Every within-organizer block pairs an organizer's own consecutive campaigns so it is not a cross-sectional cut.

## Structure thresholds

`analysis/thresholds.py [<dataset dir>] [--classification <segments file>]` reads the campaign analysis through `load.connect()` and `frame.ordinary` and writes `output/thresholds.json`: single-unit curves and a two-segment breakpoint fit for action count, duration, prize count, prize units (a winner-count proxy, since `wins` is never used), description word count and share-action worth, each repeated by industry, size band and plan tier so a breakpoint that moves under stratification can be told apart from one that holds. Also a ten-decile cut of the ordinary population by contestant count, to check whether campaign size on its own predicts action count or engagement.

## Running These Scripts

The inputs are private and are not distributed. Every script takes the converted dataset directory as its first argument and a segment file through `--classification`, both gitignored. Customers never need to run any of this: the skill references already contain everything derived from it.

## Organizer Labels and Enrichment

Every organizer host carries an industry, business type, niche, stage and audience. Company facts (organization scale, domain age, store platform, social channel size) come from public sources keyed on the host's own public homepage and public profile pages. The scripts that fetch and build these labels are not published, and every cache they write is gitignored.

`industries.json` reports medians by industry, business type, store platform, niche, organizer stage, audience, organizer scale, plan tier, widget language, domain age, marketing stack, social channel size band, country and topic. Every row needs at least five distinct organizers, so no row describes one company.
