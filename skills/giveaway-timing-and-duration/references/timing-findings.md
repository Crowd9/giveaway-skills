# Timing findings

Built from the campaigns behind these numbers: crypto, ambiguous and purchase-only campaigns removed, and every one reached at least 100 Entrants. Duration is the end date minus the start date in days as recorded, so a campaign extended after launch shows its final length. The typical range given below covers the middle half of campaigns, from the lower quarter to the upper quarter. Where a figure says nine campaigns in ten sit below it, that's the top-tenth mark.

<!-- generated:timing -->
Duration: median 14 days, IQR 7 to 29, 90th percentile 35 (n=115,754). By campaign size: 100-250 12 days, 250-500 14 days, 500-1k 14 days, 1k-2.5k 15 days, 2.5k-10k 18 days, 10k+ 18 days.

| Duration (days) | Share of campaigns | Entries per contestant, median |
|---|---|---|
| 1-3 | 13% | 3.52 |
| 4-7 | 16% | 3.99 |
| 8-14 | 22% | 4.41 |
| 15-30 | 28% | 4.83 |
| 31-60 | 16% | 5.14 |
| 61-180 | 3% | 3.84 |
| 181+ | 0% | 3.86 |

The two tables below are shares of every campaign carrying a start date. They hold no campaign count of their own, so never borrow one from another table on this page: measured answers attached both 116,499 and 115,754 to these rows and neither is theirs.

| Start month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Share of campaigns | 6.7% | 8.0% | 9.1% | 8.3% | 8.6% | 8.5% | 7.9% | 7.9% | 7.4% | 8.3% | 9.0% | 10.4% |

| Start weekday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|---|---|---|---|---|---|---|---|
| Share of campaigns | 19.2% | 16.0% | 16.5% | 15.9% | 15.6% | 7.2% | 9.6% |
<!-- /generated -->

## Reading the tables

- Two to four weeks is the most common choice at every size, and bigger campaigns run a little longer. [Half of all campaigns run 7 to 29 days, 18 days typical above 10,000 Entrants against 12 in the 100 to 250 band.]
- Entries per Entrant rise with duration up to about two months, then fall. Repeatable daily actions accumulate over time, and campaigns past two months are mostly evergreen or recurring formats with different mechanics. This describes the campaigns businesses ran at each length. It cannot say that shortening or lengthening a campaign would change Entries per Entrant, and it says nothing about reach or results.
- December holds about 10% of starts, a quarter again the share of a typical month. March, May, June and November are the next busiest. January is the quietest.
- Five in six campaigns start on a weekday. Monday is the most common start day and Saturday the rarest.

## Experience (extracted)

Experience tracks a slightly better Conversion Rate: businesses on their eleventh campaign or later get 27% of viewers to enter, against 26% on a first campaign, and they draw 515 Entrants against 382. These are all runs at their actual length, so a repeatable action or a long run pulls a row's Conversion Rate down the same way it does anywhere else on this page.

<!-- generated:tm_experience -->
| Campaign number | Entrants | Conversion Rate |
|---|---|---|
| 11th+ | 515 | 27% |
| 1st | 382 | 26% |
| 2nd | 434 | 26% |
| 3rd-5th | 504 | 27% |
| 6th-10th | 545 | 27% |
<!-- /generated -->

These are campaigns that already reached 100 Entrants, so a business that stopped after a weak first run is missing, and the curve mostly shows who kept going. Read it with the momentum finding below: running again, soon, is the pattern that comes with better numbers.

A shorter first campaign is part of that pattern too: businesses that went on to run a second campaign ran a shorter first one than businesses that did not, at every starting size. [13 days against 15 for a first campaign under 250 Entrants, 21 against 30 at 10,000 or more, rounded to whole days from `analysis/output/organizer_history.json`, `first_campaign_by_survival_matched_on_band`.] For advice on a new business's first-campaign duration, mention this and see giveaway-results-review for the full table by campaign size.

## Cadence and persistence (extracted)

Gap since the business's previous campaign, all the campaigns behind these numbers:

<!-- generated:tm_cadence -->
| Campaign number | Campaigns | Entrants | Entries per Entrant | Conversion Rate |
|---|---|---|---|---|
| 1st | 17,247 | 382 | 3.67 | 26% |
| 2nd | 8,445 | 434 | 3.85 | 26% |
| 3rd-5th | 14,228 | 504 | 4.04 | 27% |
| 6th-10th | 12,804 | 545 | 4.18 | 27% |
| 11th+ | 63,775 | 515 | 4.90 | 27% |
<!-- /generated -->

<!-- generated:tm3_persistence -->
Campaign size repeats: after a campaign of 5,000 or more Entrants, about 51 in 100 of the next ones reach 5,000 too, against 3 in 100 when the previous one was smaller, across 97,370 consecutive pairs from 8,455 businesses.

| Prior campaign size | Next reaches same size | Otherwise |
|---|---|---|
| 5,000+ Entrants | 51% | 3% |
| 10,000+ Entrants | 50% | 1% |

One campaign's size and the next one's size move together closely, a correlation of 0.66 out of 1 on a log scale.
<!-- /generated -->

Repeat audiences, lists and promotion habits are possible explanations to check in campaign records. This comparison does not measure their contribution.

Source: `analysis/output/context_checks.json` (`persistence`).

## Overlapping campaigns and close day (extracted)

Overlapping campaigns had similar Entrant counts within the fair-comparison subset. In that subset, a campaign that started before the business's previous one closed got 36% of viewers to enter against 34% without overlap [453 Entrants against 451, 13,741 campaigns against 25,721]. Overlapping campaigns are more often December starts, the advent-calendar pattern, which accounts for part of a gap that is under two points to begin with [15% of starts against 12%]. Across all runs, overlapping campaigns drew 471 Entrants against 511 without overlap, about 8% fewer, while Conversion Rate stayed within one percentage point.

Close day of the week, all the campaigns behind these numbers:

<!-- generated:tm_close_day -->
| Close day | Campaigns | Entrants | Conversion Rate |
|---|---|---|---|
| Monday | 20,127 | 498 | 27% |
| Friday | 17,754 | 504 | 27% |
| Thursday | 16,043 | 509 | 27% |
| Sunday | 15,909 | 457 | 27% |
| Tuesday | 15,800 | 497 | 26% |
| Wednesday | 15,606 | 506 | 27% |
| Saturday | 15,044 | 475 | 27% |
<!-- /generated -->

Flat, like the start day. Close hour in UTC shows no usable pattern either, and the campaign timezone is not in the dataset, so pick the close time for your audience and your own working hours.

Comparing within the 1-7-day and 8-14-day run-length bands, close-day type makes little difference: a weekend and a weekday close sit within about a point of each other at both lengths, and a public-holiday close sits under three points below them in 1-7 day runs and within a point at 8-14. A raw comparison mixes short flash campaigns that close mid-week with long advent-style runs that close disproportionately in the holiday period. Comparing within run-length bands reduces that mix, though durations still vary inside each band. A public holiday is read from the business's own country against the Nager.Date calendar.

<!-- generated:tm2_close_type -->
| Duration | Close type | Campaigns | Businesses | Conversion Rate (campaigns with no repeatable action) | Entries per Entrant |
|---|---|---|---|---|---|
| 1-7 days | Weekday | 23,821 | 4,450 | 41.3% (16,519) | 3.76 |
| 1-7 days | Weekend | 8,295 | 2,484 | 41.4% (5,483) | 3.87 |
| 1-7 days | Public holiday | 1,392 | 730 | 38.6% (976) | 3.83 |
| 8-14 days | Weekday | 18,248 | 5,247 | 28.2% (11,629) | 4.41 |
| 8-14 days | Weekend | 6,103 | 2,734 | 29.3% (4,097) | 4.42 |
| 8-14 days | Public holiday | 1,218 | 737 | 28.7% (758) | 4.39 |
<!-- /generated -->

Entries per Entrant sit within about a tenth of an Entry across the three close types at both lengths, so no secondary pattern survives either.

Source: `analysis/output/text_and_context.json` (`overlap_clean`, `overlap_all`) for the overlap figures, `analysis/output/calendar.json` (`by_close_day_type`) for the close day.

## Limits

- Duration and start date move together with the type of business running it, the budget and the season. The data cannot pull apart a pure duration effect from those.
- The benchmark duration summary tops out at 365 days (`analysis/output/benchmarks.json`, `ordinary_benchmark.duration_days.max`). Runs outside its duration scope are not represented in that summary.
- Start dates are in UTC. Local-time patterns for a specific audience will shift by a day at the edges.

## Duration, weekday and momentum against Entrants and Conversion Rate (extracted)

Impressions in the data are counted once per day, so a visitor who returns counts again each day. Repeatable actions (daily bonus, loyalty, timed bonus) and long runs raise Impressions per Entrant and lower the Conversion Rate, without any change in who actually entered. The campaigns we can compare fairly are the ones with no repeatable action and any run over 14 days removed. Figures below are typical values from the campaigns behind these numbers, description only.

<!-- generated:cmp_repeatable -->
| Repeatable actions | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| no repeatable actions | 74,826 | 494 | 3.82 | 29% | 3.4 | 6 |
| has repeatable actions | 41,457 | 490 (-1%) | 5.66 (+48%) | 23% (-22%) | 4.4 | 9 |
<!-- /generated -->

<!-- generated:cmp_duration -->
| Duration, no repeatable actions | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| 1 to 7 days | 22,978 | 440 | 3.53 | 41% | 2.4 | 5 |
| 8 to 14 | 16,484 | 468 (+6%) | 3.92 (+11%) | 28% (-31%) | 3.5 | 6 |
| 15 to 30 | 20,497 | 538 (+22%) | 4.07 (+15%) | 26% (-37%) | 3.9 | 6 |
| 31 to 60 | 11,419 | 545 (+24%) | 4.19 (+19%) | 23% (-45%) | 4.4 | 7 |
| 61 or more | 2,929 | 733 (+67%) | 3.21 (-9%) | 21% (-48%) | 4.7 | 5 |
<!-- /generated -->

Longer runs collect two thirds more Entrants by 61 days and roughly double the Impressions per Entrant, so the Conversion Rate halves with no change in who actually entered. Compare the Conversion Rate only across campaigns of similar length.

The day-to-day view sharpens this. Each row is a different campaign's whole run, grouped by how long that run was, so the curve compares a 1-day campaign with a 14-day one and never tracks a single campaign day by day. The bend below is a two-segment straight-line fit tried at every possible split of the curve, and the split reported is the one that beats a single straight line by the most. Measured answers read it as a within-run drop and scheduled pushes against it, which this cut cannot support.

<!-- generated:tm3_bend -->
| Day | Conversion Rate |
|---|---|
| 1 | 58% |
| 4 | 38% |
| 5 | 35% |
| 7 | 32% |
| 14 | 26% |
| 30 | 26% |

The typical Conversion Rate bends between a 4-day and a 5-day run across 65,576 campaigns with no repeatable action that ran 1 to 35 days. The two-segment fit reduces squared fitting error by 83% compared with a single straight line.

The same search repeated inside each campaign size, plan tier and industry:

| Segment | Bend point | Squared fitting error reduction versus one line | Campaigns | Businesses |
|---|---|---|---|---|
| 100-250 Entrants | day 5-6 | 78% | 18,510 | 853 |
| 250-500 Entrants | day 3-4 | 79% | 15,057 | 598 |
| 500-1,000 Entrants | day 5-6 | 78% | 12,592 | 495 |
| 1,000-2,500 Entrants | day 6-7 | 73% | 11,102 | 405 |
| 2,500-10,000 Entrants | day 7-8 | 80% | 6,686 | 286 |
| 10,000+ Entrants | day 14-15 | 31% | 1,392 | 64 |
| Pro accounts | day 3-4 | 87% | 35,630 | 1,113 |
| Business accounts | day 5-6 | 81% | 16,482 | 365 |
| Free accounts | day 3-4 | 60% | 6,632 | 370 |
| Hobby accounts | day 3-4 | 32% | 5,826 | 277 |
| Premium accounts | day 15-29 | 74% | 390 | 17 |
| Gaming and esports | day 3-4 | 75% | 14,651 | 618 |
| Media and entertainment | day 7-8 | 33% | 12,188 | 224 |
| Electronics and tech | day 6-7 | 68% | 9,135 | 253 |
| Other industries | day 17-28 | 65% | 2,446 | 120 |
| Toys, hobbies, collectibles | day 3-4 | 29% | 2,348 | 76 |
| Food and drink | day 4-5 | 55% | 2,325 | 93 |
| Apparel and fashion | day 12-13 | 64% | 2,219 | 83 |
| Sports and outdoors | day 5-6 | 83% | 2,092 | 98 |

For campaigns of 10,000 or more Entrants the bend moves to day 14-15 and gets weaker: the two-segment fit reduces squared fitting error by 31% compared with a single straight line, against 73% to 80% in the two sizes below (1,392 campaigns, 64 businesses). Industries spread from day 3-4 in gaming and esports to day 12-13 in apparel and fashion.
<!-- /generated -->

Across every size band under 10,000 Entrants and the two largest plan tiers the bend lands within the first week or so of campaign duration. This compares whole runs of different lengths. Read the 10,000-plus bend as suggestive only, since it rests on a thinner slice of data, and treat any row that reduces squared fitting error by under half compared with a single straight line the same way. Bend locations vary across segments, and none of these rows is a rule to plan a run length around.

Source: `analysis/output/thresholds.json` (`duration_days`).

## Daily pace falls as a campaign runs longer (extracted)

Entrants per day of the run, not just per campaign, fall well past the launch window as duration increases, in every industry checked. This cannot separate a business choosing a longer run from also choosing a smaller Prize or a slower-moving category, since industry is the only thing held constant here.

<!-- generated:tm2_daily_pace -->
| Industry | 1-3 days | 4-7 days | 8-14 days | 15-30 days | 31 days or more |
|---|---|---|---|---|---|
| Gaming and esports | 233.4 | 63.3 | 37.9 | 20.1 | 11.9 |
| Electronics and tech | 586.5 | 124.1 | 83.8 | 49.8 | 26.9 |

Entrants per day, typical. A gaming campaign of one to three days drew about six times the daily pace of one running eight to fourteen, and electronics about seven times.

[Gaming and esports: 2,926 campaigns from 724 businesses at 1-3 days, 4,904/1,445 at 4-7, 6,002/1,899 at 8-14, 6,269/2,058 at 15-30, 4,031/1,393 at 31 or more. Electronics and tech: 2,710 campaigns from 248 businesses at 1-3 days, 2,152/548 at 4-7, 3,263/833 at 8-14, 4,595/1,078 at 15-30, 2,775/741 at 31 or more.]
<!-- /generated -->

The fall continues past two weeks in both.

Source: `analysis/output/calendar.json` (`per_day_by_length_industry`).

## Higher launch-day Impressions than closing-day Impressions (extracted)

Closing-day Impressions are lower than launch-day Impressions and close to the quietest days of the run. These are daily page views, which can include repeat visits. They do not establish when new Entrants first arrive or what share enter during the launch window.

In a 7-day campaign, Impressions run highest on the launch day and the close sits among the quietest days:

<!-- generated:tm2_launch_curve -->
| Day of a 7-day run | Share of Impressions | Campaigns | Businesses |
|---|---|---|---|
| Launch (day 1) | 15.9% | 19,677 | 5,052 |
| Day 2 | 12.6% | 23,098 | 5,598 |
| Day 3 | 10.8% | 25,385 | 5,959 |
| Day 4 | 9.3% | 25,794 | 6,046 |
| Day 5 | 8.3% | 25,838 | 6,052 |
| Day 6 | 8.8% | 25,894 | 6,064 |
| Close (day 7) | 8.6% | 25,892 | 6,066 |

A 14-day campaign shows the same shape: close 5.8% (17,492 campaigns, 5,195 businesses) against 9.1% on the launch day (13,160 campaigns, 4,090 businesses), with the days between running 4.4% to 7.3%. Both curves are anchored to the close date, so a run a day longer or shorter than the label shifts every row by a day.
<!-- /generated -->

The daily Impressions comparison does not establish a benefit from closing early. Common practice, our data doesn't cover this. Use the closing days for deadline reminders and preparation for the draw and Winner messages. See `giveaway-winner-communications` for those messages.

<!-- generated:cmp_weekday -->
| Start weekday | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| Monday | 22,313 | 479 | 4.39 | 26% | 3.8 | 7 |
| Tuesday | 18,584 | 500 (+4%) | 4.26 (-3%) | 26% (+2%) | 3.8 | 7 |
| Wednesday | 19,181 | 504 (+5%) | 4.23 (-4%) | 28% (+6%) | 3.6 | 7 |
| Thursday | 18,502 | 513 (+7%) | 4.43 (+1%) | 27% (+3%) | 3.7 | 7 |
| Friday | 18,162 | 521 (+9%) | 4.52 (+3%) | 27% (+3%) | 3.7 | 7 |
| Saturday | 8,346 | 438 (-9%) | 4.44 (+1%) | 28% (+9%) | 3.5 | 7 |
| Sunday | 11,195 | 454 (-5%) | 4.50 (+3%) | 27% (+4%) | 3.7 | 7 |
<!-- /generated -->

The outcome table records fewer Entrants for weekend starts, with smaller differences in Conversion Rate and Entries per Entrant. Its row counts describe the observed outcomes. The start-share table near the top describes organizer choices and has no reported sample count. Missing start-date coverage is not reported separately. Neither table establishes what choosing a different day would change, so plan around audience availability and team coverage.

<!-- generated:cmp_recency -->
| Gap since previous campaign, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| first campaign | 4,967 | 332 | 3.18 | 31% | 3.2 | 5 |
| previous within 30 days | 25,695 | 470 (+42%) | 3.94 (+24%) | 38% (+22%) | 2.7 | 6 |
| previous 31 to 90 days | 4,820 | 499 (+50%) | 3.51 (+10%) | 33% (+6%) | 3.1 | 5 |
| previous 91 to 365 days | 3,296 | 439 (+32%) | 3.35 (+5%) | 31% (+1%) | 3.2 | 5 |
| previous over a year | 684 | 382 (+15%) | 3.12 (-2%) | 32% (+3%) | 3.2 | 5 |
<!-- /generated -->

<!-- generated:cmp_recency_vertical -->
| Vertical | First campaigns | Within 30 days | Contestants | Contestants per impression |
|---|---|---|---|---|
| music_media | 696 | 5,148 | +49% | +19% |
| gaming | 1,461 | 5,928 | +41% | +15% |
| unclassified | 793 | 4,825 | +68% | +16% |
| technology | 512 | 4,001 | +71% | +48% |
| fitness_outdoor | 344 | 1,048 | -32% | +6% |
| kids_family_pets | 235 | 1,191 | -2% | -9% |
| fashion_beauty | 326 | 1,559 | +106% | +35% |
| food_drink | 191 | 582 | +63% | +21% |
| travel_events | 138 | 484 | +40% | +36% |
| home | 135 | 646 | +23% | +24% |
| software | 136 | 283 | +69% | +44% |
<!-- /generated -->

A campaign that starts within 30 days of the business's previous one draws more Entrants and gets about a fifth more of them to enter than a business's first campaign, with fewer Impressions needed per Entrant. Past 30 days the entry-rate gain is gone while the Entrant gain stays. Returning audiences are one hypothesis, but this comparison does not track returning people. It holds in nine of the eleven verticals, with fitness and outdoor and kids, family and pets the exceptions. Momentum is the one timing finding with a consistent direction, and it describes businesses that ran campaigns close together, so it cannot say that scheduling alone caused the lift.

Source: `analysis/output/calendar.json` (`last_days_impression_curve_by_duration`) for the launch curve.

## Build lead time (extracted)

All the campaigns behind these numbers (116,499 campaigns, 17,633 businesses): the recorded create date sits after the campaign's start date in 22% of them. That is not a business building after launch. The field also updates on a later edit, so for about a fifth of these campaigns it reads as last-modified, not build lead time. Treat every number below with that in mind.

Among the campaigns where the create date sits before the start date, the typical lead time is 1 day, the upper quarter 5 days, the top tenth 14 days. Most businesses with a usable lead figure built the campaign the day before launch or closer.

| Build lead | Campaigns | Businesses | Conversion Rate | Entries per Entrant | Methods |
|---|---|---|---|---|---|
| Same day | 42,030 | 9,219 | 27% | 4.65 | 7 |
| 1 to 2 days | 17,018 | 5,010 | 26% | 4.36 | 7 |
| 3 to 7 days | 15,604 | 4,572 | 27% | 4.11 | 7 |
| 8 or more days | 16,509 | 4,173 | 26% | 3.90 | 7 |

Same-day builds get as many Entrants to enter as campaigns built a week or more ahead. A longer lead buys time for assets and partner briefs, not a better Conversion Rate on its own.

Source: analysis/output/field_cuts.json (build_lead_days, by_build_lead).

## Duration by plan tier and hosting mix (extracted)

Premium accounts run the longest campaigns with the most methods, Hobby accounts run the shortest and Free accounts use the fewest. [116,499 campaigns, 17,633 businesses total.]

| Plan tier | Campaigns | Businesses | Typical duration | Methods |
|---|---|---|---|---|
| Premium | 1,993 | 202 | 22 days | 10 |
| Business | 29,645 | 3,553 | 15 days | 8 |
| Pro | 62,061 | 10,160 | 14 days | 8 |
| Free | 11,993 | 4,183 | 12 days | 4 |
| Hobby | 10,802 | 2,555 | 11 days | 6 |

By growth stage, mid-market businesses and startups run the shortest campaigns and individuals the longest, with enterprises at the same typical length as small businesses:

<!-- generated:tm2_stage -->
| Growth stage | Campaigns | Businesses | Typical duration | Methods |
|---|---|---|---|---|
| Mid market | 17,126 | 1,384 | 8 days | 6 |
| Startup | 23,190 | 5,227 | 10 days | 8 |
| Small business | 60,935 | 7,897 | 14 days | 7 |
| Enterprise | 6,675 | 507 | 14 days | 6 |
| Public body | 1,109 | 294 | 14 days | 7 |
| Individual | 10,371 | 1,808 | 16 days | 9 |

The growth-stage cut is 121,842 campaigns, 2,436 of them with no stage read, wider than the campaigns behind the rest of this page, so its counts do not add to the plan-tier table above.
<!-- /generated -->

Hosting mix tracks the same pattern. Campaigns that keep most of their Impressions on the Gleam-hosted page run a shorter typical length than campaigns that lean on the embed.

| Share of Impressions on the hosted page | Campaigns | Businesses | Typical days |
|---|---|---|---|
| 90% or more hosted | 70,080 | 13,712 | 12 |
| 50 to 90% hosted | 7,912 | 2,161 | 16 |
| 10 to 50% hosted | 17,319 | 2,923 | 21 |
| Mostly embedded | 20,872 | 3,212 | 16 |

An embed sits inside a page the business already controls, so there is less pressure to close it down on a fixed date.

More methods and a longer run go together in both of these breakdowns, which is the account tier and the hosting choice describing each other as much as describing duration on its own.

Source: analysis/output/field_cuts.json (by_tier, by_hosted_share), analysis/output/industries.json (by_org_stage).

## Region (extracted)

A short, high-entry-rate format fills the South American rows, and more specifically the Portuguese-language and Brazilian YouTube-hosted ones, running well below the typical campaign length at double the typical Conversion Rate or more. Impressions count once per visitor per day, so repeat visits across days can affect the denominator. This table does not establish how much that explains the regional differences.

<!-- generated:tm2_region -->
| Group | Campaigns | Businesses | Typical duration | Methods | Conversion Rate |
|---|---|---|---|---|---|
| South America | 5,333 | 588 | 1 day | 8 | 57% |
| Portuguese-language | 2,331 | 116 | 1 day | 19 | 65% |
| Brazilian YouTube-hosted | 2,199 | 86 | 1 day | 19 | 67% |

The Brazilian YouTube-hosted row is read from the industries cut, which runs wider than the campaigns behind the rest of this page. It is 2,199 campaigns from 86 businesses, so it describes those accounts, never a market.
<!-- /generated -->

These rows describe short runs and high Conversion Rates among the sampled businesses. An audience ready for a fast giveaway is a hypothesis to check against their promotion and audience records. The table does not establish what shortening another campaign would change.

Source: analysis/output/field_cuts.json (by_continent, by_language), analysis/output/industries.json (by_youtube_country).

## Response and draw windows (extracted)

Almost every campaign keeps the platform's 7-day default for both the draw window and the response window, so this mostly shows businesses keeping the default, not choosing seven days on purpose. [94.3% of campaigns use the 7-day draw window and 93.4% the 7-day response window, out of the 115,361 campaigns whose terms record these settings, from `analysis/output/winner_terms.json` (`terms_timetable`). The earlier pair of 96% figures carried a campaign count that traces to no run of the source, so both are read off the recorded denominator now.]

Source for the response-window bands below: `analysis/output/field_cuts.json` (`by_response_days`). The band labels are `8_14_days` and `15_plus_days`.

Conversion Rate is higher across the response-window bands up to 14 days. The 15-plus-day band has the lowest Conversion Rate and the longest campaign duration. The table does not establish why Conversion Rates differ, and the configured response window does not measure how quickly Winners responded.

<!-- generated:tm_response_days -->
| Response window | Campaigns | Businesses | Conversion Rate | Days |
|---|---|---|---|---|
| 1-3 days | 5,109 | 1,047 | 25% | 12 |
| 4-7 days (default) | 108,256 | 16,671 | 27% | 14 |
| 8-14 days | 990 | 273 | 30% | 13 |
| 15+ days | 935 | 229 | 19% | 29 |
<!-- /generated -->

Source: analysis/output/field_cuts.json (terms, by_response_days).

## Start weekday and month, a second check (extracted)

A separate check, using all runs at their actual length, for a second read on the weekday and month findings above.

<!-- generated:tm_weekday -->
| Start weekday | Campaigns | Businesses | Entrants | Conversion Rate |
|---|---|---|---|---|
| Monday | 22,360 | 6,566 | 479 | 26% |
| Tuesday | 18,606 | 5,960 | 500 | 26% |
| Wednesday | 19,213 | 5,986 | 505 | 28% |
| Thursday | 18,524 | 6,035 | 513 | 27% |
| Friday | 18,193 | 5,705 | 520 | 27% |
| Saturday | 8,372 | 3,483 | 438 | 28% |
| Sunday | 11,231 | 4,192 | 454 | 27% |
<!-- /generated -->

This outcome table also records fewer Entrants for weekend starts and a narrow range of Conversion Rates. Use its own campaign and business counts when quoting a row. It describes recorded results alongside start days, without establishing the effect of choosing a day.

Month moves once, in December, and nowhere else:

<!-- generated:tm_month -->
| Start month | Conversion Rate | Entrants | Days |
|---|---|---|---|
| December (12,068 campaigns, 3,958 businesses) | 30.9% | 560 | 10 |
| November (10,433 campaigns, 3,944 businesses) | 26.9% | 490 | 15 |
| January (7,751 campaigns, 3,368 businesses) | 26.7% | 479 | 15 |
| March (10,641 campaigns, 4,073 businesses) | 26.6% | 485 | 14 |
| May (10,049 campaigns, 3,965 businesses) | 26.6% | 477 | 15 |
| February (9,286 campaigns, 3,839 businesses) | 26.6% | 474 | 14 |
| April (9,675 campaigns, 3,888 businesses) | 26.5% | 471 | 14 |
| July (9,173 campaigns, 3,840 businesses) | 26.5% | 498 | 15 |
| October (9,671 campaigns, 3,867 businesses) | 26.4% | 474 | 15 |
| June (9,856 campaigns, 3,839 businesses) | 26.3% | 502 | 15 |
| August (9,221 campaigns, 3,780 businesses) | 26.2% | 508 | 15 |
| September (8,675 campaigns, 3,640 businesses) | 25.6% | 494 | 15 |
<!-- /generated -->

Every month outside December sits inside a 1.5-point range on Conversion Rate. December clears the nearest of them by 4.0 points and the furthest by 5.3, on a run about two thirds the length of the rest of the year.

December also has higher Conversion Rates within most industries in this comparison:

<!-- generated:tm_december_best -->
| Industry | December | Next-best month | Gap |
|---|---|---|---|
| Electronics and tech | 38.5% (2,114 campaigns, 557 businesses) | June, 30.3% | 8.2 pts |
| Home and garden | 35.2% (420 campaigns, 135 businesses) | February, 31.0% | 4.2 pts |
| Toys, hobbies, collectibles | 33.0% (418 campaigns, 126 businesses) | November, 29.3% | 3.7 pts |
| Travel and events | 32.2% (337 campaigns, 119 businesses) | January, 29.8% | 2.4 pts |
| Sports and outdoors | 31.5% (462 campaigns, 209 businesses) | November, 25.2% | 6.3 pts |
| Other | 31.5% (385 campaigns, 242 businesses) | April, 29.8% | 1.7 pts |
| Food and drink | 30.6% (408 campaigns, 163 businesses) | January, 28.6% | 2.0 pts |
| Gaming and esports | 28.8% (2,591 campaigns, 1,109 businesses) | July, 27.8% | 1.0 pts |
| Health, wellness and fitness | 26.9% (305 campaigns, 110 businesses) | November, 24.1% | 2.8 pts |
| Media and entertainment | 25.9% (2,149 campaigns, 451 businesses) | March, 24.5% | 1.4 pts |
<!-- /generated -->

December is not the best month in two of the twelve industries measured. Apparel and fashion peaks in May, a few points above its December rate, and creator or influencer campaigns peak in March, well above it.

<!-- generated:tm_december_not_best -->
| Industry | Peak month | Peak Conversion Rate | December Conversion Rate |
|---|---|---|---|
| Creator or influencer | March | 46.3% | 37.3% (329 campaigns, 179 businesses) |
| Apparel and fashion | May | 34.2% | 31.7% (386 campaigns, 147 businesses) |
<!-- /generated -->

Source: `analysis/output/prize_timing_cuts.json` (`by_start_weekday`, `by_start_month`, `by_start_month_and_industry`).

## Launch and pre-release wording (extracted)

Campaigns whose name, incentive name or description carries launch or pre-release wording, against campaigns with none:

<!-- generated:tm_launch_wording -->
| Wording | Campaigns | Businesses | Conversion Rate | Referrals % of Entrants | Share offered | Email offered | Days |
|---|---|---|---|---|---|---|---|
| No launch wording | 110,374 | 16,703 | 27.0% | 11 | 37% | 32% | 14 |
| Launch or release | 3,604 | 1,600 | 25.7% | 15 | 39% | 41% | 13 |
| Coming soon or waitlist | 1,014 | 588 | 25.5% | 16 | 40% | 31% | 11 |
| Crowdfunding | 699 | 203 | 23.0% | 10 | 84% | 64% | 15 |
| Pre-order | 444 | 188 | 24.0% | 14 | 42% | 41% | 18 |
| Wishlist or pre-save | 364 | 148 | 27.3% | 15 | 28% | 16% | 8 |
<!-- /generated -->

Launch wording gets a little fewer viewers to enter than the no-wording baseline and brings in more referrals. Crowdfunding wording leans hardest on sharing and email and converts worst, wishlist or pre-save wording converts best on the shortest run, and pre-order campaigns run the longest.

By industry, gaming and esports leads on most launch wording, with media and entertainment ahead on pre-order wording.

<!-- generated:tm_launch_industry -->
| Wording | Leading industry (campaigns) | Next industry (campaigns) |
|---|---|---|
| Launch or release | Gaming and esports (994) | Electronics and tech (563) |
| Coming soon or waitlist | Gaming and esports (366) | Electronics and tech (137) |
| Crowdfunding | Gaming and esports (308) | Toys, hobbies, collectibles (224) |
| Pre-order | Media and entertainment (189) | Gaming and esports (110) |
| Wishlist or pre-save | Gaming and esports (222) | Media and entertainment (30) |
<!-- /generated -->

Two Prize types carry a release date, and both are advice only given the small counts. Spotify pre-saves lead further out the earlier the campaign starts:

<!-- generated:tm_release_spotify -->
| Start timing | Campaigns | Businesses | Typical lead | Conversion Rate |
|---|---|---|---|---|
| 30+ days before release | 34 | 8 | 56 days before | 17% |
| Under 30 days before release | 50 | 24 | 10 days before | 20% |
<!-- /generated -->

Steam game campaigns convert best starting just before release, and worst starting well ahead of it:

<!-- generated:tm_release_steam -->
| Start timing | Campaigns | Businesses | Typical lead | Conversion Rate |
|---|---|---|---|---|
| 30+ days before release | 111 | 52 | 164 days before | 18% |
| Under 30 days before release | 67 | 35 | 10 days before | 25% |
| Within 30 days after release | 107 | 64 | 4 days after | 24% |
| Over 30 days after release | 460 | 135 | 561 days after | 22% |
<!-- /generated -->

Most Steam campaigns in this group start long after their release date, as the last row shows.

Source: `analysis/output/prize_timing_cuts.json` (`by_launch_wording`, `launch_wording_by_industry`, `campaign_start_against_release_date`).

## Run length by country (extracted)

Run length varies by the business's country. Rows that would reveal small residual groups are withheld from this comparison.

<!-- generated:tm_country_duration -->
| Country | Typical days | Lower quarter | Typical days, crypto and SaaS removed | Campaigns | Businesses |
|---|---|---|---|---|---|
| United States | 14 | 7 | 14 | 57,061 | 8,646 |
| United Kingdom | 21 | 10 | 22 | 15,125 | 1,688 |
| Canada | 12 | 7 | 12 | 6,940 | 1,056 |
| Australia | 15 | 8 | 15 | 6,045 | 1,328 |
| India | 9 | 6 | 16 | 4,024 | 678 |
| Vietnam | 9 | 5 | 20 | 2,450 | 519 |
| Hong Kong | 8 | 5 | 10 | 1,973 | 428 |
| Spain | 13 | 7 | 14 | 1,865 | 491 |
| Türkiye | 8 | 5 | 8 | 1,393 | 360 |
<!-- /generated -->

The third column removes crypto and SaaS businesses from each available country comparison.

By industry across all countries, finance and crypto businesses run the shortest typical length, with food and drink and beauty and personal care the longest. A country with a large crypto share reads shorter in the raw figure until that share is set aside.

<!-- generated:tm_industry_duration -->
| Industry | Typical days | Campaigns | Businesses |
|---|---|---|---|
| Finance and crypto | 7 | 24,555 | 4,297 |
| Apparel and fashion | 8 | 4,660 | 824 |
| Creator or influencer | 8 | 3,408 | 1,053 |
| Retail marketplace | 8 | 2,870 | 388 |
| Education | 8 | 1,894 | 369 |
| Other | 10 | 4,625 | 1,558 |
| Local services | 11 | 921 | 177 |
| Gaming and esports | 12 | 25,595 | 4,903 |
| Software and SaaS | 12 | 2,490 | 612 |
| Nonprofit and community | 13 | 546 | 203 |
| Electronics and tech | 14 | 15,634 | 2,072 |
| Automotive | 14 | 2,288 | 382 |
| Toys, hobbies, collectibles | 15 | 4,641 | 759 |
| Travel and events | 15 | 4,032 | 654 |
| Home and garden | 15 | 3,726 | 596 |
| Art and crafts | 15 | 1,646 | 418 |
| Marketing agency | 15 | 1,264 | 165 |
| Pets | 15 | 980 | 214 |
| Sports and outdoors | 16 | 4,640 | 1,016 |
| Health, wellness and fitness | 16 | 3,064 | 503 |
| Jewelry and watches | 17 | 459 | 166 |
| Media and entertainment | 18 | 21,675 | 2,082 |
| Baby and kids | 18 | 1,187 | 137 |
| Food and drink | 19 | 4,734 | 900 |
| Beauty and personal care | 19 | 1,416 | 352 |
<!-- /generated -->

Source: `analysis/output/indicators.json` (`duration_by_country`, `duration_by_industry`, `mechanics_by_country_excluding_crypto`).

## Start hour and weekend starts by country (extracted)

Local start hour is estimated with one UTC offset per country and no daylight saving, so read it as a rough window, not a precise hour. Countries spanning several time zones (the US, Canada, Brazil, Australia) carry up to three hours of error on top of that.

<!-- generated:tm_start_hour -->
| Country | Typical local start hour | Weekend starts | Campaigns | Businesses |
|---|---|---|---|---|
| United States | 08:00 | 19% | 57,289 | 8,720 |
| United Kingdom | 12:00 | 16% | 15,188 | 1,710 |
| Canada | 03:00 | 19% | 7,004 | 1,066 |
| Australia | 10:00 | 20% | 6,066 | 1,334 |
| Brazil | Midnight | 19% | 5,299 | 497 |
| Japan | 12:00 | 11% | 4,797 | 235 |
| India | Midnight | 22% | 4,062 | 691 |
| Singapore | 12:00 | 11% | 3,491 | 271 |
| Germany | 13:00 | 22% | 3,322 | 419 |
| South Korea | Midnight | 14% | 2,675 | 392 |
| Vietnam | 12:00 | 21% | 2,501 | 547 |
| France | 13:00 | 22% | 2,174 | 356 |
| Poland | 13:00 | 16% | 2,157 | 188 |
| Philippines | 15:00 | 18% | 2,053 | 289 |
| Hong Kong | 11:00 | 15% | 1,973 | 428 |
| Taiwan | 15:00 | 11% | 1,920 | 157 |
| Spain | 13:00 | 20% | 1,884 | 496 |
| China | 15:00 | 13% | 1,541 | 136 |
| Malaysia | 08:00 | 10% | 1,501 | 103 |
| Türkiye | 03:00 | 21% | 1,406 | 367 |
<!-- /generated -->

The share of campaigns starting on a local Saturday or Sunday varies less by country, from about 10% to about 22%, as the weekend column shows. The same single-offset caveat applies.

Source: `analysis/output/indicators.json` (`start_hour_local_by_country`, `weekend_start_by_country`).

## Run length by starting point (extracted)

Duration barely varies by where the build started from.

<!-- generated:tm_template_source -->
| Build source | Typical duration | Campaigns | Businesses |
|---|---|---|---|
| Own earlier campaign copied | 14 days | 67,690 | 5,640 |
| Blank build | 15 days | 26,892 | 10,759 |
| Copied from a campaign outside this dataset | 14 days | 11,961 | 4,211 |
| Library template | 15 days | 9,955 | 6,467 |
<!-- /generated -->

A few library templates run notably longer than the rest:

<!-- generated:tm_template_longest -->
| Library template | Typical duration | Campaigns | Businesses |
|---|---|---|---|
| Every Entry Type | 26 days | 49 | 47 |
| Build Pre-Launch Awareness | 23 days | 76 | 75 |
| Grow Twitch Stream | 22.5 days | 127 | 112 |
| Mr Beast's Giveaway | 22 days | 77 | 74 |
| Photo Contest | 21 days | 157 | 138 |
<!-- /generated -->

Source: `analysis/output/templates.json` (`source_mix`, `by_template`).

## Repeat business concentration by country (extracted)

Average campaigns per business varies sharply by country, Japan highest and Spain lowest among the countries measured here. In Japan four campaigns in five come from a business on its eleventh campaign or later, against fewer than one in three in Spain, the same gap in a second measure. A country's campaign count partly reflects a small number of businesses who run often, more so in Japan than in most other countries measured here.

<!-- generated:tm_repeat_country -->
| Country | Campaigns per business | Eleventh campaign or later | Campaigns | Businesses |
|---|---|---|---|---|
| Japan | 20 | 81% | 4,797 | 235 |
| Malaysia | 15 | 77% | 1,501 | 103 |
| Singapore | 13 | 73% | 3,491 | 271 |
| Taiwan | 12 | 70% | 1,920 | 157 |
| Poland | 11 | 70% | 2,157 | 188 |
| China | 11 | 67% | 1,541 | 136 |
| Brazil | 11 | 73% | 5,299 | 497 |
| United Kingdom | 9 | 65% | 15,188 | 1,710 |
| Germany | 8 | 59% | 3,322 | 419 |
| Philippines | 7 | 56% | 2,053 | 289 |
| South Korea | 7 | 52% | 2,675 | 392 |
| Canada | 7 | 53% | 7,004 | 1,066 |
| United States | 7 | 53% | 57,289 | 8,720 |
| France | 6 | 51% | 2,174 | 356 |
| India | 6 | 57% | 4,062 | 691 |
| Hong Kong | 5 | 35% | 1,973 | 428 |
| Vietnam | 5 | 41% | 2,501 | 547 |
| Australia | 5 | 37% | 6,066 | 1,334 |
| Türkiye | 4 | 35% | 1,406 | 367 |
| Spain | 4 | 29% | 1,884 | 496 |
<!-- /generated -->

Source: `analysis/output/indicators.json` (`repeat_organizer_by_country`).
