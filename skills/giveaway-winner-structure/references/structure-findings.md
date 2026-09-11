# Structure findings

These figures come from the campaigns we can compare fairly (crypto, unclear listings and purchase-only campaigns removed). A Prize record is one line in the business's Prize list. Units are the quantities on those lines added up. Tiered means the Prize list has more than one position (a first Prize and a second Prize, for example).

<!-- generated:structure_detail -->
| Prize records per campaign | Share |
|---|---|
| 1 | 82.4% |
| 2 | 6.2% |
| 3 | 6.0% |
| 4 | 1.8% |
| 5 | 1.3% |
| 6+ | 2.2% |

Total prize units per campaign: median 1, 75th percentile 3, 90th percentile 10, maximum 1,133 (n=117,348). 40% of campaigns list more than one unit and 18% list tiered prizes (more than one position).

| Band | Single unit | Tiered prizes | Ten or more units |
|---|---|---|---|
| 100-250 | 59% | 15% | 11% |
| 250-500 | 61% | 16% | 12% |
| 500-1k | 61% | 18% | 11% |
| 1k-2.5k | 59% | 21% | 13% |
| 2.5k-10k | 60% | 22% | 16% |
| 10k+ | 62% | 20% | 19% |
<!-- /generated -->

## Reading the tables

- Four in five campaigns list a single Prize record, and three in five give away exactly one unit. One Winner is the default choice at every size.
- Two in five campaigns give away more than one unit, and one in five list tiered Prizes. Ten or more units appears in about one campaign in seven, rising slightly with campaign size.
- The typical number of Entrants for single-unit and multi-unit campaigns is almost identical in the Prize-picker findings, which describes the structure people chose and nothing about what it did.

## Entrants and Conversion Rate by Prize count (extracted)

This compares campaigns with one Prize record against campaigns with several, showing the Entrants, the Conversion Rate (the share of people who saw it and entered) and the Actions per Entrant, for each count. Every group below is at least 30 campaigns from 10 businesses.

<!-- generated:st_prize_count -->
| Prize records | Campaigns | Businesses | Typical Entrants | Conversion Rate | Actions per Entrant | Days | Methods |
|---|---|---|---|---|---|---|---|
| 1 | 96,743 | 14,283 | 471 | 28% | 4.3 | 14 | 7 |
| 10+ | 1,033 | 477 | 1,157 | 19% | 5.5 | 17 | 10 |
| 2-3 | 14,326 | 5,207 | 582 | 24% | 4.6 | 14 | 8 |
| 4-9 | 5,246 | 2,162 | 675 | 23% | 5.1 | 14 | 9 |
<!-- /generated -->

Conversion Rate falls steadily from 28% at one Prize record to 19% at ten or more. Entrants rise at every step, from 471 at one record to 1,157 at ten or more, alongside more Entry Methods and a longer run at that top end. That describes campaigns that already chose to run many Prizes, run longer and offer more ways to enter, not what adding Prize records would do to one campaign.

In plain terms, splitting a Prize into several draws a smaller crowd for the same money, even once you allow for campaign size and industry. What you get instead is more reach and more referrals, so the trade only pays off when reach is what you need.

Four newer cuts allow for other differences that could explain the pattern on their own, and all four show the same shape. Even matched to the same stated Prize value, a single Prize still beats a split Prize on crowd-per-dollar, across every price range tested (table below). Only the smallest bundle range reverses this, and it rests on a thin sample.

| Cut (matched to stated Prize value) | Crowd-per-dollar score | Campaigns | Businesses |
|---|---|---|---|
| Single Prize, by price range | 1.01 to 1.18 | — | — |
| Split Prize (2+), by price range | 0.81 to 0.99 | — | — |
| Single Prize, all price ranges combined | 1.03 | 28,141 | 5,000 |
| Split Prize, all price ranges combined | 0.87 | 7,463 | 2,555 |
| Smallest bundle range (100-249 USD), reverses | — | 150 | 90 |
| Ranges tested | 7, from 250-499 USD to 25,000-49,999 USD | — | — |

Once we allow for campaign size and industry together, so neither one explains the gap on its own, a single Prize unit still beats a split Prize on three separate measures, among the campaigns we can compare fairly, at close to the same ratios as before that adjustment (table below).

| Metric (single Prize vs split) | Advantage | Campaigns | Businesses |
|---|---|---|---|
| Conversion Rate | 1.245x | 2,113 | 326 |
| Crowd per dollar spent | 1.117x | 2,795 | 749 |
| Cost % of Entrants | 1.379x | 2,781 | 831 |

That is what splitting one Prize into several costs. What it buys: more Prize records lift reach and referrals per 100 Entrants, going from one Prize record to five or more, consistent across three campaign sizes, though not more follows or joins, which stay close to flat for the two smaller sizes and fall for the largest (table below).

| Effect of 1 Prize record to 5+ | Lift per 100 Entrants |
|---|---|
| Reach | 30% to 57% |
| Referrals | 8% to 28% |

A campaign built to turn a fixed audience into Entrants at the lowest cost per person wants the single Prize. A campaign built to reach new people or push referrals gets that lift, for the Conversion Rate and crowd-per-dollar cost above.

A separate look at Actions per Entrant against Prize unit count shows a possible flattening point in the four largest groups (table below), but the two metrics only loosely track each other there, and smaller groups scatter the flattening point far more widely, so treat that last point as worth testing again with a cleaner measure, not a settled number.

| Group | Flattening point (Prize units) |
|---|---|
| Four largest groups (1,000-2,500 and 2,500-10,000 Entrants; Pro and Business plans) | about 14 to 15 |
| Smaller groups | 3 to 15 (wide scatter) |

Each of the four largest groups has more than 11,000 campaigns and 1,100 businesses. Correlation between unit count and Actions per Entrant there: 28%.

None of this is a causal claim about what splitting one business's next campaign would do. It is that the gap between a single Prize and a split Prize, in Conversion Rate, the crowd-per-dollar score and the cost per Entrant, holds up once we remove the most obvious other explanations: value range, campaign size and industry, which the raw table above could not do by itself.

Source: `analysis/output/success_profiles.json` (success_cohorts.clean_conversion, .prize_value_adjusted_performance, .cost_per_contestant), `analysis/output/prize_economics.json` (bundles, bundles_by_value_band), `analysis/output/asset_yield.json` (yield_by_asset_and_prize_structure), `analysis/output/thresholds.json` (winner_units, moderate confidence).

The same campaigns cut by stated Prize pool, not by Prize count:

<!-- generated:st_pool_band -->
| Prize pool, USD | Campaigns | Businesses | Typical Entrants | Conversion Rate | Actions per Entrant | Days | Methods |
|---|---|---|---|---|---|---|---|
| under 250 | 20,307 | 4,246 | 328 | 24% | 5.13 | 16 | 8 |
| 250 to 1k | 12,396 | 4,082 | 722 | 24% | 4.39 | 15 | 7 |
| 1k to 5k | 9,459 | 3,158 | 1,470 | 23% | 4.55 | 18 | 8 |
| 5k and up | 2,034 | 1,069 | 1,802 | 20% | 4.31 | 22 | 7 |
<!-- /generated -->

Bigger pools bring more Entrants and a longer run. Conversion Rate holds near 24% through the first three pool sizes and drops to 20% at 5k and up. A bigger pool and more Prize records tend to travel together with a bigger business and a longer campaign, so read both tables as who ran what, not as what a structure change would do to a given campaign.

Source: `analysis/output/prize_timing_cuts.json` (by_prize_count, by_pool_band).

## Winners by Prize category (extracted)

This looks at each Prize row: the typical number of Winners on a category's rows, how often a row names more than one Winner, and the stated USD value per Winner among rows that state one. Every category below has at least 30 campaigns from 10 businesses.

<!-- generated:st_winners_category -->
| Category | Campaigns | Businesses | Typical Winners | Multi-Winner share | USD per Winner (typical) | Conversion Rate |
|---|---|---|---|---|---|---|
| Unclassified | 34,953 | 8,748 | 1 | 34% | 120 | 27% |
| Tech hardware | 22,137 | 4,938 | 1 | 22% | 299 | 26% |
| Gift card or cash | 17,927 | 4,514 | 1 | 27% | 50 | 23% |
| Bundle or box | 13,410 | 3,944 | 1 | 25% | 175 | 26% |
| Game items or skins | 11,228 | 2,730 | 1 | 38% | 56 | 21% |
| Experience, travel, tickets | 6,321 | 1,925 | 1 | 26% | 400 | 25% |
| Placeholder name | 5,696 | 1,292 | 1 | 34% | 200 | 28% |
| Merch, apparel, collectibles | 5,548 | 1,838 | 1 | 35% | 50 | 26% |
| Home, garden, appliance | 2,452 | 913 | 1 | 17% | 200 | 29% |
| Toys and collectibles | 2,297 | 474 | 1 | 35% | 55 | 25% |
| Subscription or membership | 1,637 | 882 | 1 | 42% | 150 | 23% |
| Regulated goods (firearms) | 1,579 | 329 | 1 | 6% | 1,118 | 20% |
| Food, drink, consumables | 1,468 | 608 | 1 | 17% | 190 | 29% |
| Sports and outdoor gear | 1,366 | 654 | 1 | 20% | 299 | 26% |
| Discount or coupon | 1,054 | 348 | 3 | 62% | 100 | 26% |
| Beauty and wellness | 815 | 310 | 1 | 20% | 150 | 28% |
| Vehicle | 733 | 369 | 1 | 20% | 699 | 23% |
| Tools, craft, DIY | 581 | 203 | 1 | 28% | 209 | 28% |
| Exclusive access | 535 | 332 | 1 | 48% | 200 | 27% |
| Music gear | 452 | 175 | 1 | 9% | 399 | 26% |
| Art and custom | 185 | 112 | 1 | 22% | 73 | 27% |
<!-- /generated -->

One Winner per Prize row is standard across every category (table above): the typical row names one Winner everywhere, so a row naming more than one Winner is the exception. USD per Winner tracks what the category costs per unit, not how often a row goes multi-Winner: the highest-value category pays the most per Winner on the lowest multi-Winner share, and the cheapest categories sit in the middle of the multi-Winner range. That highest-value category, firearms, also carries the lowest Conversion Rate at 20%, in line with the extra eligibility steps it carries elsewhere in this repository.

Within experience, travel, tickets, flights or hotel packages alone return 1,810 USD per Winner, well above the category's 400 USD typical figure, because the category mixes cheap tickets with priced-out travel.

Source: `analysis/output/prize_timing_cuts.json` (winners_by_prize_category, winners_by_ticket_kind).

## Winner count against Prize value (extracted, campaigns that stated a value)

One Winner pulls a bigger crowd for the same stated Prize value than a large pool of Winners does, and the gap widens as the pool grows, even after allowing for the plain "bigger Prize, more Entrants" effect on its own (table below). The gap is widest at the top of the price range tested.

| Winner count | Ratio to predicted crowd, by price range | Ratio, all price ranges combined | Campaigns (combined) | Businesses (combined) |
|---|---|---|---|---|
| Single Winner | 1.09 to 1.53x | 1.07x | 8,640 | 2,149 |
| 21 or more Winners | 0.53 to 0.68x | 0.84x | 769 | 343 |

| Winner count | First price tier | Last price tier | Campaigns per tier | Businesses per tier |
|---|---|---|---|---|
| Single Winner | 500-999 USD | 10,000-24,999 USD | 112 to 2,013 | 78 to 761 |
| Pool (21+) | 500-999 USD | 25,000-49,999 USD | 36 to 263 | 29 to 93 |

That is a cost on this one crowd-per-dollar measure. It does not weigh what a large pool buys: many Winners who each felt something good happened, many small wins worth posting about, and a Prize spread further across a community than one big Winner reaches. A campaign built to get the most Entrants for its stated Prize value wants the single Winner. A campaign built to spread a goodwill moment across a community, reward loyalty broadly, or run a low-stakes recurring series wants the large pool, and pays this crowd-per-dollar cost for it.

Do not use this below 500 USD or above 49,999 USD, where it was not tested.

Source: `analysis/output/success_profiles.json` (interactions.prize_value_by_winner_count), `analysis/output/context_checks.json` (winner_count_index_value_adjusted).

## Winners by Prize position (extracted)

A record-level look at position within a campaign's Prize list: first Prize, second or third, and fourth or later. Every position below has at least 30 campaigns from 10 businesses.

<!-- generated:st_winners_position -->
| Position | Campaigns | Businesses | Multi-Winner share | USD per Winner (typical) | Conversion Rate |
|---|---|---|---|---|---|
| Second or third | 95,702 | 15,970 | 27% | 150 | 26% |
| First Prize | 41,061 | 9,857 | 34% | 100 | 27% |
| Fourth plus | 4,932 | 1,841 | 33% | 69 | 20% |
<!-- /generated -->

First and fourth-plus Prizes go multi-Winner more often than second or third place (table above). USD per Winner runs highest at second or third, above first Prize, which reads as product tiers: a second or third Prize often repeats the same product line at a smaller size, lifting its per-Winner value above the headline Prize. Fourth-plus Prizes settle at the lowest per-Winner value at 69 USD, in line with a consolation tier, on the lowest Conversion Rate of the three at 20%.

Source: `analysis/output/prize_timing_cuts.json` (winners_by_position).

## Prize structure by country (extracted, business's country, 100+ Entrants)

This group is not the same as the campaigns behind the numbers above. It groups every campaign with 100 or more Entrants by the business's country, all industries and crypto businesses included. Read it beside the tables above as a separate check on country patterns. Every country below clears its 30-campaign, 10-business floor by a wide margin.

| Country | Campaigns | Businesses | Prize units (typical) | Single-unit share | Pool USD (typical) | Pool stated share |
|---|---|---|---|---|---|---|
| Japan | 6,505 | 291 | 15 | 16% | 1,250 | 46% |
| Singapore | 4,743 | 351 | 15 | 17% | 500 | 29% |
| South Korea | 4,521 | 537 | 10 | 31% | 1,000 | 17% |
| Vietnam | 3,762 | 773 | 10 | 39% | 500 | 34% |
| Malaysia | 2,345 | 160 | 10 | 35% | 700 | 33% |
| United States | 58,843 | 9,105 | 1 | 61% | 300 | 50% |
| United Kingdom | 15,716 | 1,847 | 1 | 66% | 200 | 27% |
| Australia | 6,433 | 1,406 | 1 | 62% | 769 | 32% |
| Brazil | 5,860 | 563 | 1 | 73% | 90 | 7% |

Japan and Singapore list the most Prize units, the US, UK, Brazil and Australia the fewest, and single-unit Prizes are rare in the first pair and common in the second group (table above). South Korea, Vietnam and Malaysia sit between the two groups. Typical pool USD follows no simple pattern against unit counts, and it rests on a much thinner slice of campaigns in some countries than others: Pool stated share ranges widely by country (table above), so read a country's typical pool figure alongside its stated share, not on its own.

Source: `analysis/output/indicators.json` (prize_structure_by_country), `analysis/output/country_cuts.json` (by_country).

## Limits

- Quantity is what the business typed. A record with quantity 100 may be 100 Winners, or 100 codes for one Winner. That applies to the country group's typical Prize-unit figures too.

- Recurring draws (daily or weekly Winners) appear as high quantities on one record and cannot be separated from a single bulk draw.

- Every campaign in the tables above passed the 100-Entrant floor. Nothing here shows a structure changed participation. The country group uses a lower, 100-Entrant floor and does not exclude crypto businesses, so its figures are not directly comparable to the tables above.
