# Structure findings

These figures come from the campaigns we can compare fairly (crypto, unclear listings and purchase-only campaigns removed). A Prize record is one line in the business's Prize list. Units are the quantities on those lines added up. Tiered means the Prize list has more than one position (a first Prize and a second Prize, for example).

<!-- generated:structure_detail -->
| Prize records per campaign | Share |
|---|---|
| 1 | 82.6% |
| 2 | 6.2% |
| 3 | 6.0% |
| 4 | 1.8% |
| 5 | 1.3% |
| 6+ | 2.2% |

Total prize units per campaign: median 1, 75th percentile 3, 90th percentile 10 (n=116,499). 40% of campaigns list more than one unit and 17% list tiered prizes (more than one position).

| Band | Single unit | Tiered prizes | Ten or more units |
|---|---|---|---|
| 100-250 | 60% | 15% | 11% |
| 250-500 | 61% | 15% | 12% |
| 500-1k | 61% | 18% | 11% |
| 1k-2.5k | 60% | 21% | 13% |
| 2.5k-10k | 60% | 22% | 15% |
| 10k+ | 61% | 20% | 19% |
<!-- /generated -->

The 100 to 250 Entrant band contains 33,074 campaigns from 9,533 businesses, with 15% listing tiered Prizes. Source: `analysis/output/benchmarks.json`, `ordinary_benchmark.structure_detail.by_band["100-250"]`. These are listed Prizes, not completed awards, and campaigns below 100 Entrants are absent.

## Reading the tables

- Four in five campaigns list a single Prize record, and three in five give away exactly one unit. One Winner is the default choice at every size.
- Two in five campaigns give away more than one unit, and one in five list tiered Prizes. Ten or more units appears in about one campaign in seven, rising slightly with campaign size.
- The typical number of Entrants for single-unit and multi-unit campaigns is almost identical in the Prize-picker findings, which describes the structure people chose and nothing about what it did.

## Entrants and Conversion Rate by Prize count (extracted)

This compares campaigns with one Prize record against campaigns with several, showing the Entrants, the Conversion Rate (the share of people who saw it and entered) and the Entries per Entrant, for each count. Every group below is at least 30 campaigns from 10 businesses.

<!-- generated:st_prize_count -->
| Prize records | Campaigns | Businesses | Typical Entrants | Conversion Rate | Entries per Entrant | Days | Methods |
|---|---|---|---|---|---|---|---|
| 1 | 96,177 | 14,183 | 471 | 28% | 4.3 | 14 | 7 |
| 10+ | 988 | 472 | 1,340 | 19% | 5.6 | 18 | 10 |
| 2-3 | 14,184 | 5,139 | 584 | 24% | 4.6 | 14 | 8 |
| 4-9 | 5,150 | 2,134 | 688 | 23% | 5.1 | 15 | 9 |
<!-- /generated -->

Conversion Rate falls steadily from 28% at one Prize record to 19% at ten or more. Entrants rise at every step, from 471 at one record to 1,340 at ten or more, alongside more Entry Methods and a longer run at that top end. That describes campaigns that already chose to run many Prizes, run longer and offer more ways to enter, not what adding Prize records would do to one campaign.

Campaigns classified as bundles had fewer Entrants relative to the median in their stated Prize value band than the remaining campaigns. The bundle group includes campaigns with multiple Prize records or a bundle/box category. This comparison accounts for stated Prize value band. It does not establish what splitting one campaign's Prize would change.

Comparing within stated Prize value bands leaves campaigns outside the bundle group ahead in six of the seven ranges shown. The reversal is at 25,000 to 49,999 USD, where bundles sit slightly ahead on a small sample. Combined counts below describe each full group. The index uses 35,165 valued campaigns outside the bundle group and 7,788 valued bundle campaigns.

| Cut (matched to stated Prize value) | Crowd-per-dollar score | Campaigns | Businesses |
|---|---|---|---|
| Outside the bundle group, by price range | 1.00 to 1.21 | - | - |
| Bundle group, by price range | 0.70 to 1.04 | - | - |
| Outside the bundle group, all price ranges combined | 1.04 | 96,008 | 14,156 |
| Bundle group, all price ranges combined | 0.79 | 20,275 | 6,516 |
| Bundle group at 25,000-49,999 USD, reverses | 1.04 | 50 | 46 |
| Ranges shown | 7, from 250-499 USD to 25,000-49,999 USD | - | - |

Single-unit campaigns are more common in the top fifth on the three measures below. Conversion Rate and cost per Entrant compare within size and industry. Crowd per dollar compares within industry after accounting for value. The ratios compare the prevalence of single-unit campaigns in the top fifth against the rest. They measure feature prevalence. Counts are the matched top-fifth cohorts.

| Metric (single Prize vs split) | Advantage | Campaigns | Businesses |
|---|---|---|---|
| Conversion Rate | 1.293x | 7,839 | 1,092 |
| Crowd per dollar spent | 1.170x | 8,590 | 2,098 |
| Cost per Entrant | 1.434x | 8,580 | 2,071 |

The asset-yield comparison associates more Prize records with more Impressions and referral completions per 100 Entrants, going from one Prize record to five or more, consistent across three campaign sizes, though not more follows or joins, which stay close to flat for the two smaller sizes and fall for the largest (table below).

| Effect of 1 Prize record to 5+ | Lift per 100 Entrants |
|---|---|
| Reach | 28% to 55% |
| Referrals | 8% to 25% |

Common practice, our data doesn't cover this. Choose the structure from the value of each unit, fulfillment cost and campaign objective. A single Prize can preserve headline appeal, while several can support product trial or community rewards. Use the associations above as context for a test, without promising lower cost or more Entrants.

A separate look at Entries per Entrant against Prize unit count finds different bend points by campaign size and plan tier. The two larger campaign-size groups bend around 14 to 15 units, while Pro and Business bend later. Treat these as descriptive fits, not a settled stopping point.

| Group | Flattening point (Prize units) |
|---|---|
| 1,000-2,500 and 2,500-10,000 Entrants | 14 to 15 |
| Pro and Business plans | 21 to 24 |
| Other reported size and tier groups | 5 to 21 |

Each of those two size groups and two tiers has more than 11,000 campaigns and 1,800 businesses. The two-line fit improves on one line by 9% to 47% across them. This is fit improvement, not correlation.

None of this establishes what splitting a business's next Prize would do. Single-unit campaigns appear more often among strong Conversion Rate and low-cost results after matching by size and industry, while the value-range comparison has one reversal among the seven ranges shown.

Source: `analysis/output/success_profiles.json` (success_cohorts.clean_conversion, .prize_value_adjusted_performance, .cost_per_contestant), `analysis/output/prize_economics.json` (bundles, bundles_by_value_band), `analysis/output/asset_yield.json` (yield_by_asset_and_prize_structure), `analysis/output/thresholds.json` (winner_units, moderate confidence).

The same campaigns cut by stated Prize pool, not by Prize count:

<!-- generated:st_pool_band -->
| Prize pool, USD | Campaigns | Businesses | Typical Entrants | Conversion Rate | Entries per Entrant | Days | Methods |
|---|---|---|---|---|---|---|---|
| under 250 | 20,236 | 4,208 | 327 | 24% | 5.14 | 16 | 8 |
| 250 to 1k | 12,324 | 4,051 | 721 | 24% | 4.38 | 15 | 7 |
| 1k to 5k | 9,399 | 3,119 | 1,472 | 23% | 4.55 | 18 | 8 |
| 5k and up | 1,998 | 1,051 | 1,823 | 20% | 4.29 | 22 | 7 |
<!-- /generated -->

Bigger pools bring more Entrants and a longer run. Conversion Rate holds near 24% through the first three pool sizes and drops to 20% at 5k and up. A bigger pool and more Prize records tend to travel together with a bigger business and a longer campaign, so read both tables as who ran what, not as what a structure change would do to a given campaign.

Source: `analysis/output/prize_timing_cuts.json` (by_prize_count, by_pool_band).

## Winners by Prize category (extracted)

This looks at each Prize row: the typical number of Winners on a category's rows, how often a row names more than one Winner, and the stated USD value per Winner among rows that state one. Every category below has at least 30 campaigns from 10 businesses.

<!-- generated:st_winners_category -->
| Category | Campaigns | Businesses | Typical Winners | Multi-Winner share | USD per Winner (typical) | Conversion Rate |
|---|---|---|---|---|---|---|
| Unclassified | 31,413 | 8,165 | 1 | 32% | 129 | 27% |
| Gift card or cash | 22,648 | 5,278 | 1 | 29% | 60 | 24% |
| Tech hardware | 22,080 | 4,926 | 1 | 22% | 299 | 26% |
| Bundle or box | 12,783 | 3,789 | 1 | 25% | 170 | 26% |
| Game items or skins | 11,226 | 2,743 | 1 | 38% | 56 | 21% |
| Experience, travel, tickets | 6,050 | 1,861 | 1 | 27% | 399 | 25% |
| Merch, apparel, collectibles | 5,257 | 1,806 | 1 | 36% | 50 | 26% |
| Placeholder name | 5,087 | 1,254 | 1 | 32% | 200 | 32% |
| Home, garden, appliance | 2,534 | 895 | 1 | 16% | 199 | 30% |
| Toys and collectibles | 2,267 | 470 | 1 | 35% | 54 | 25% |
| Subscription or membership | 1,560 | 848 | 1 | 42% | 149 | 23% |
| Regulated goods (firearms) | 1,510 | 323 | 1 | 6% | 1,178 | 19% |
| Food, drink, consumables | 1,359 | 568 | 1 | 17% | 180 | 29% |
| Sports and outdoor gear | 1,303 | 630 | 1 | 21% | 300 | 26% |
| Discount or coupon | 1,046 | 344 | 3 | 61% | 100 | 26% |
| Beauty and wellness | 727 | 286 | 1 | 22% | 111 | 28% |
| Vehicle | 662 | 342 | 1 | 20% | 649 | 23% |
| Tools, craft, DIY | 613 | 227 | 1 | 29% | 180 | 28% |
| Exclusive access | 520 | 321 | 1 | 48% | 200 | 27% |
| Music gear | 447 | 173 | 1 | 8% | 399 | 26% |
| Art and custom | 178 | 106 | 1 | 21% | 99 | 27% |
<!-- /generated -->

The typical Prize row names one Winner in every category except discount or coupon (table above). Discount or coupon rows have a typical count of three Winners and a 61% multi-Winner share across 1,046 campaigns and 344 businesses. Use the relevant category row when considering Winner count. USD per Winner tracks what the category costs per unit, not how often a row goes multi-Winner: the highest-value category pays the most per Winner on the lowest multi-Winner share, and the cheapest categories sit in the middle of the multi-Winner range. That highest-value category, firearms, also carries the lowest Conversion Rate at 19%, in line with the extra eligibility steps it carries elsewhere in this repository.

Within experience, travel, tickets, flights or hotel packages alone return 1,000 USD per Winner, well above the category's 399 USD typical figure, because the category mixes cheap tickets with priced-out travel.

Source: `analysis/output/prize_timing_cuts.json` (winners_by_prize_category, winners_by_ticket_kind).

## Winner count against Prize value (extracted, campaigns that stated a value)

Single-Winner campaigns had a higher ratio of observed to predicted Entrants than campaigns listing many Winners in the comparison below, after accounting for stated Prize value (table below). The gap varies by price range and is not largest at the highest range. The combined column uses the value-adjusted index, while the range column also accounts for the winner-count group's typical crowd.

| Winner count | Ratio to predicted crowd, by price range | Ratio, all price ranges combined | Campaigns (combined) | Businesses (combined) |
|---|---|---|---|---|
| Single Winner | 1.26 to 1.95x | 1.15x | 26,919 | 5,664 |
| 21 or more Winners | 0.29 to 0.45x | 0.77x | 1,566 | 670 |

| Winner count | First price tier | Last price tier | Campaigns per tier | Businesses per tier |
|---|---|---|---|---|
| Single Winner | 500-999 USD | 10,000-24,999 USD | 166 to 3,221 | 119 to 1,344 |
| Pool (21+) | 500-999 USD | 25,000-49,999 USD | 54 to 506 | 45 to 202 |

The single-Winner group had the higher score on this measure. That association does not establish a cost from splitting one campaign's budget. Apply the practical choice above: keep the Prize whole when its unit value matters, or divide it when rewarding more people serves the objective and each unit remains worth winning. Account for fulfillment before choosing the count.

The displayed comparison covers 500 to 49,999 USD. The source also reports qualifying cells outside that range.

Source: `analysis/output/success_profiles.json` (interactions.prize_value_by_winner_count), `analysis/output/context_checks.json` (winner_count_index_value_adjusted).

## Winners by Prize position (extracted)

A record-level look at position within a campaign's Prize list: first Prize, second or third, and fourth or later. Every position below has at least 30 campaigns from 10 businesses.

<!-- generated:st_winners_position -->
| Position | Campaigns | Businesses | Multi-Winner share | USD per Winner (typical) | Conversion Rate |
|---|---|---|---|---|---|
| Second or third | 94,954 | 15,834 | 27% | 150 | 26% |
| First Prize | 40,691 | 9,761 | 34% | 100 | 27% |
| Fourth plus | 4,810 | 1,819 | 32% | 69 | 20% |
<!-- /generated -->

First and fourth-plus Prizes go multi-Winner more often than second or third place (table above). USD per Winner runs highest at second or third, above first Prize, which reads as product tiers: a second or third Prize often repeats the same product line at a smaller size, lifting its per-Winner value above the headline Prize. Fourth-plus Prizes settle at the lowest per-Winner value at 69 USD, in line with a consolation tier, on the lowest Conversion Rate of the three at 20%.

Source: `analysis/output/prize_timing_cuts.json` (winners_by_position).

## Prize structure by country (extracted, business's country, 100+ Entrants)

This groups campaigns with at least 100 Entrants by the business's country, including crypto businesses. It is a separate population from the ordinary-campaign benchmarks. Every country below clears its 30-campaign, 10-business floor by a wide margin.

| Country | Campaigns | Businesses | Prize units (typical) | Single-unit share | Pool USD (typical) | Pool stated share |
|---|---|---|---|---|---|---|
| Japan | 4,797 | 235 | 20 | 18% | 1,625 | 55% |
| Singapore | 3,491 | 271 | 10 | 21% | 580 | 29% |
| South Korea | 2,675 | 392 | 7 | 38% | 1,000 | 17% |
| Vietnam | 2,501 | 547 | 5 | 45% | 500 | 35% |
| Malaysia | 1,501 | 103 | 5 | 43% | 1,000 | 27% |
| United States | 57,289 | 8,720 | 1 | 62% | 299 | 51% |
| United Kingdom | 15,188 | 1,710 | 1 | 68% | 180 | 27% |
| Australia | 6,066 | 1,334 | 1 | 63% | 769 | 32% |
| Brazil | 5,299 | 497 | 1 | 73% | 40 | 6% |

Japan and Singapore list the most Prize units, the US, UK, Brazil and Australia the fewest, and single-unit Prizes are rare in the first pair and common in the second group (table above). South Korea, Vietnam and Malaysia sit between the two groups. Typical pool USD follows no simple pattern against unit counts, and it rests on a much thinner slice of campaigns in some countries than others: Pool stated share ranges widely by country (table above), so read a country's typical pool figure alongside its stated share, not on its own.

Source: `analysis/output/indicators.json` (prize_structure_by_country), `analysis/output/country_cuts.json` (by_country).

## What the terms actually say (extracted)

Two settings decide the Winner timetable, and almost nobody changes either.

<!-- generated:st_terms -->
Every share below is out of the 115,361 campaigns whose terms record these settings.

| Setting | Value | Campaigns | Share |
|---|---|---|---|
| Days after close before the draw | 7 (Gleam's default) | 108,813 | 94.3% |
| Days a Winner has to reply | 7 (Gleam's default) | 107,694 | 93.4% |
| Selection method | Random Draw | 114,444 | 99.2% |
<!-- /generated -->

Seven days is Gleam's default for both, so this describes what campaigns end up with and never what businesses
weighed up. Never write that 93% of businesses chose seven days: 93% of them left the setting alone, and the two
readings point a reader in opposite directions. The count is also the share, and the population is the line printed above the table. Answers have reached for the
116,499-campaign figure from elsewhere on this page, which reconciles with no share here. Six measured answers
across two rounds got this pair wrong, so read the line above the table before quoting a share from it. The next most common reply window is two days on 2,390 campaigns, then one day on 1,365. A 72-hour
deadline, which trade advice often recommends, is written into 1.2% of these campaigns (1,354 of 115,361, `analysis/output/winner_terms.json`, `terms_timetable.reply_days.values.3`).

Source for selection shares: `analysis/output/winner_terms.json` (`selection_method`).

Judging is close to non-existent. 99.2% name a random draw, and every other method together covers the
remaining 0.8%.

Source for the default windows: `analysis/output/winner_terms.json` (`terms_timetable`), with seven days stored as the `values.7` key for both windows.

The practical reading: 7 days is what a reader's Entrants will expect because it is what almost every Gleam
campaign says, and a shorter deadline is a deliberate choice to defend in the terms. Pick a shorter one when the
Prize expires (an event ticket, a seasonal item), and leave the default otherwise.

Source: `analysis/output/winner_terms.json`.

## Limits

- Quantity is what the business typed. A record with quantity 100 may be 100 Winners, or 100 codes for one Winner. That applies to the country group's typical Prize-unit figures too.

- Recurring draws (daily or weekly Winners) appear as high quantities on one record and cannot be separated from a single bulk draw.

- Every campaign in the tables above passed the 100-Entrant floor. Nothing here shows a structure changed participation. The country group uses a lower, 100-Entrant floor and does not exclude crypto businesses, so its figures are not directly comparable to the tables above.
