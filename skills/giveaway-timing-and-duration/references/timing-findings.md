# Timing findings

Built from the campaigns behind these numbers: crypto, ambiguous and purchase-only campaigns removed, and every one reached at least 1,000 Entrants. Duration is the end date minus the start date in days as recorded, so a campaign extended after launch shows its final length. The typical range given below covers the middle half of campaigns, from the lower quarter to the upper quarter. Where a figure says nine campaigns in ten sit below it, that's the top-tenth mark.

<!-- generated:timing -->
Duration: median 14 days, IQR 7 to 29, 90th percentile 35 (n=116,491). By campaign size: 100-250 12 days, 250-500 14 days, 500-1k 14 days, 1k-2.5k 15 days, 2.5k-10k 18 days, 10k+ 18 days.

| Duration (days) | Share of campaigns | Entries per contestant, median |
|---|---|---|
| 1-3 | 13% | 3.53 |
| 4-7 | 16% | 4.01 |
| 8-14 | 22% | 4.42 |
| 15-30 | 28% | 4.84 |
| 31-60 | 16% | 5.14 |
| 61-180 | 3% | 3.89 |
| 181+ | 1% | 3.86 |

| Start month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Share of campaigns | 6.7% | 8.0% | 9.1% | 8.3% | 8.6% | 8.4% | 7.9% | 7.9% | 7.4% | 8.3% | 9.0% | 10.4% |

| Start weekday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|---|---|---|---|---|---|---|---|
| Share of campaigns | 19.2% | 16.0% | 16.5% | 15.9% | 15.6% | 7.2% | 9.7% |
<!-- /generated -->

## Reading the tables

- Two to four weeks is the most common choice at every size, and bigger campaigns run a little longer. [Half of all campaigns run 8 to 31 days, 20 days typical above 10,000 Entrants against 15 under 2,500.]
- Actions per Entrant rise with duration up to about two months, then fall. Repeatable daily actions accumulate over time, and campaigns past two months are mostly evergreen or recurring formats with different mechanics. This describes the campaigns businesses ran at each length. It cannot say that shortening or lengthening a campaign would change how many actions Entrants do, and it says nothing about reach or results.
- December holds about 12% of starts, half again the share of a typical month. March, May, June and November are the next busiest. January is the quietest.
- Five in six campaigns start on a weekday. Monday is the most common start day and Saturday the rarest.

## Experience (extracted)

Experience tracks a better Conversion Rate: businesses on their eleventh campaign or later get 41% of viewers to enter, against 32% on a first campaign, looking only at the campaigns we can compare fairly (no repeatable action, a run of 14 days or less).

<!-- generated:tm_experience -->
| Campaign number | Entrants | Conversion Rate |
|---|---|---|
| 11th+ | 514 | 27% |
| 1st | 381 | 26% |
| 2nd | 436 | 26% |
| 3rd-5th | 500 | 27% |
| 6th-10th | 546 | 27% |
<!-- /generated -->

These are campaigns that already reached 100 Entrants, so a business that stopped after a weak first run is missing, and the curve mostly shows who kept going. Read it with the momentum finding below: running again, soon, is the pattern that comes with better numbers.

A shorter first campaign is part of that pattern too: businesses that went on to run a second campaign ran a shorter first one than businesses that did not, at every starting size. [13 days against 16 for a first campaign under 250 Entrants, 22 against 31 at 10,000 or more.] For advice on a new business's first-campaign duration, mention this and see giveaway-results-review for the full table by campaign size.

## Cadence and persistence (extracted)

Gap since the business's previous campaign, all the campaigns behind these numbers:

<!-- generated:tm_cadence -->
| Campaign number | Campaigns | Entrants | Actions per Entrant | Conversion Rate |
|---|---|---|---|---|
| 1st | 17,384 | 381 | 3.68 | 26% |
| 2nd | 8,509 | 436 | 3.86 | 26% |
| 3rd-5th | 14,333 | 500 | 4.04 | 27% |
| 6th-10th | 12,887 | 546 | 4.18 | 27% |
| 11th+ | 64,235 | 514 | 4.91 | 27% |
<!-- /generated -->

Campaign size repeats: after a big campaign, the next one tends to be big too, across 21,284 consecutive pairs from the same business.

| Prior campaign size | Next reaches same size | Otherwise |
|---|---|---|
| 5,000+ Entrants | 61% | 12% |
| 10,000+ Entrants | 57% | 5% |

One campaign's size and the next one's size move together closely, a correlation of 0.63 out of 1. Results repeat because audiences, lists and promotion habits repeat. Gleam's own check of the same data found the same figures within a point.

## Overlapping campaigns and close day (extracted)

Running two campaigns at once did not hurt the typical case, and the momentum finding still holds. Among the campaigns we can compare fairly, a campaign that started before the business's previous one closed got 42% of viewers to enter against 36% without overlap [2,117 Entrants against 2,113.5, 3,421 campaigns against 7,298]. Overlapping campaigns are more often December starts, the advent-calendar pattern, which carries much of that gap [25% against 15%]. Across all the campaigns behind these numbers the two groups sit within 5% of each other.

Close day of the week, all the campaigns behind these numbers:

<!-- generated:tm_close_day -->
| Close day | Campaigns | Entrants | Conversion Rate |
|---|---|---|---|
| Monday | 20,244 | 498 | 27% |
| Friday | 17,857 | 504 | 27% |
| Thursday | 16,144 | 509 | 27% |
| Sunday | 16,085 | 454 | 27% |
| Tuesday | 15,886 | 497 | 26% |
| Wednesday | 15,685 | 505 | 27% |
| Saturday | 15,227 | 475 | 26% |
<!-- /generated -->

Flat, like the start day. Close hour in UTC shows no usable pattern either, and the campaign timezone is not in the dataset, so pick the close time for your audience and your own working hours.

Holding run length fixed, close-day type makes no real difference: every gap sits under two points with no consistent direction. Without holding the run length fixed, a raw comparison would mix short flash campaigns that close mid-week against long advent-style runs that close disproportionately in the holiday period, and holding it fixed removes that mix-up.

| Duration | Close type | Conversion Rate | Actions per Entrant |
|---|---|---|---|
| 1-7 days | Weekend | 43.8% | 4.30 |
| 1-7 days | Weekday | 43.6% | 3.90 |
| 1-7 days | Public holiday | 42.0% | n/a |
| 8-14 days | Weekend | 32.3% | 4.51 |
| 8-14 days | Weekday | 32.1% | 4.63 |
| 8-14 days | Public holiday | 31.8% | n/a |

[Campaigns/businesses: 2,406/712 (weekend, 1-7d), 6,936/1,477 (weekday, 1-7d), 433/239 (holiday, 1-7d, checked against the Nager.Date calendar), 1,796/972 (weekend, 8-14d), 5,977/2,117 (weekday, 8-14d), 387/287 (holiday, 8-14d).]

One secondary pattern does not repeat across sizes: a weekend close brings about 10% more Actions per Entrant than a weekday close in 1-7 day campaigns, a gap not present at 8-14 days.

## Limits

- Duration and start date move together with the type of business running it, the budget and the season. The data cannot pull apart a pure duration effect from those.
- A campaign that runs for years (the maximum is over 13,000 days) is an always-on widget, and its figures describe a different product.
- Start dates are in UTC. Local-time patterns for a specific audience will shift by a day at the edges.

## Duration, weekday and momentum against Entrants and Conversion Rate (extracted)

Impressions in the data are counted once per day, so a visitor who returns counts again each day. Repeatable actions (daily bonus, loyalty, timed bonus) and long runs raise Impressions per Entrant and lower the Conversion Rate, without any change in who actually entered. The campaigns we can compare fairly are the ones with no repeatable action and any run over 14 days removed. Figures below are typical values from the campaigns behind these numbers, description only.

<!-- generated:cmp_repeatable -->
| Repeatable actions | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| no repeatable actions | 75,386 | 493 | 3.83 | 29% | 3.4 | 6 |
| has repeatable actions | 41,742 | 490 (-1%) | 5.66 (+48%) | 23% (-23%) | 4.4 | 9 |
<!-- /generated -->

<!-- generated:cmp_duration -->
| Duration, no repeatable actions | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| 1 to 7 days | 23,197 | 439 | 3.54 | 41% | 2.4 | 5 |
| 8 to 14 | 16,613 | 468 (+7%) | 3.92 (+11%) | 29% (-31%) | 3.5 | 6 |
| 15 to 30 | 20,578 | 538 (+23%) | 4.07 (+15%) | 26% (-37%) | 3.9 | 6 |
| 31 to 60 | 11,468 | 544 (+24%) | 4.19 (+18%) | 23% (-45%) | 4.4 | 7 |
| 61 or more | 2,941 | 733 (+67%) | 3.22 (-9%) | 22% (-48%) | 4.6 | 5 |
<!-- /generated -->

Longer runs collect about a tenth more Entrants and roughly double the Impressions per Entrant, so the Conversion Rate halves with no change in who actually entered. Compare the Conversion Rate only across campaigns of similar length.

The day-to-day view sharpens this. The typical Conversion Rate bends sharply between day 6 and day 7 of a campaign, the point that best explains the shape of the curve (accounting for 81% of it), stronger than any other day tested, in the same fairly-compared set (no repeatable action, durations 1 to 35 days).

| Day | Conversion Rate |
|---|---|
| 1 | 56% |
| 6 | 38% |
| 7 | 34% |
| 14 | 28% |
| 30 | 29% |

The same bend lands within a day or two across campaign sizes and account tiers:

| Segment | Bend point |
|---|---|
| 1,000-2,500 Entrants | day 6-7 |
| 2,500-10,000 Entrants | day 7-8 |
| Pro accounts | day 5-6 |
| Business accounts | day 4-5 |
| Free accounts | day 6-7 |
| Electronics and tech | day 8-9 |

[Campaigns/businesses: 19,146/3,866 overall, 11,026/402 (1,000-2,500 Entrants), 6,549/275 (2,500-10,000 Entrants), 10,459/376 (Pro), 6,068/165 (Business), 620/47 (Free), 4,362/115 (electronics and tech).]

For campaigns of 10,000 or more Entrants the bend moves later and gets weaker, and the day 6-7 drop-off established above doesn't hold at this size. [Moves to day 11-12, explaining 44% of the curve shape against 72-77% in the two smaller sizes above, 1,319 campaigns, 63 businesses.] Read that later bend as suggestive, not a rule for large campaigns, since it rests on a thinner slice of data. Two smaller categories move later still [home and garden to day 14-15, sports and outdoors to day 16-28], but both sit under 40 businesses and read as noise, not a pattern to plan around.

## Daily pace falls as a campaign runs longer (extracted)

Entrants per day of the run, not just per campaign, fall well past the launch window as duration increases, in every industry checked. This cannot separate a business choosing a longer run from also choosing a smaller Prize or a slower-moving category, since industry is the only thing held constant here.

| Industry | 1-3 days | 8-14 days |
|---|---|---|
| Gaming and esports | 1,426 Entrants/day | 234 Entrants/day |
| Electronics and tech | 1,540 Entrants/day | 201 Entrants/day |

[Gaming and esports: 858 campaigns/213 businesses at 1-3 days, 1,986/788 at 8-14 days. Electronics and tech: 1,098/87 at 1-3 days, 1,488/419 at 8-14 days.]

## Duration by what the campaign is optimizing for (extracted)

Pick the run length by what the campaign needs to produce, not by a single "longer is better" rule. Reach, engagement, referrals and traffic per Entrant are all higher in 15-plus day campaigns than in campaigns of 7 days or fewer, at every campaign size checked, for example reach for campaigns of 2,500 to 10,000 Entrants: 4.43 Actions per Entrant against 2.40 [7,432 campaigns/2,144 businesses at 15+ days against 2,745/637 at 7 days or fewer]. Discord and Telegram joins go the other way, and bring in more per Entrant in the shorter campaigns:

| Method | Campaign size | 7 days or fewer | 15+ days |
|---|---|---|---|
| Discord join | 1,000-2,500 | 52 per 100 (941 campaigns, 244 businesses) | 38 per 100 (1,641 campaigns, 575 businesses) |
| Discord join | 2,500-10,000 | 46 per 100 (285 campaigns, 125 businesses) | 36 per 100 (1,265 campaigns, 370 businesses) |
| Discord join | 10,000+ | 67 per 100 (55 campaigns, 23 businesses) | 33 per 100 (312 campaigns, 97 businesses) |
| Telegram join | 1,000-2,500 | 89 per 100 (560 campaigns, 58 businesses) | 49 per 100 (335 campaigns, 107 businesses) |
| Telegram join | 2,500-10,000 | 83 per 100 (201 campaigns, 23 businesses) | 77 per 100 (264 campaigns, 60 businesses) |

A community you want people to join before they leave the page favours a short run: Discord and Telegram joins land noticeably higher in shorter campaigns at every size above, roughly a quarter to double the rate. A campaign chasing reach, engagement, referrals or traffic favours a long one instead. Both directions hold across all three campaign sizes with enough data, so this is a genuine split by objective, not a slope in one direction. A campaign that wants both, a community built fast and the widest reach, has to pick which one the run length serves, since a shorter run and a longer one cannot both be the answer on the same clock.

## No late rush, only a launch spike (extracted)

The closing day of a run carries no more traffic than the data's quietest days, and often less. Entrants who have not acted by the final day mostly do not arrive late, the volume advantage sits with the launch and the day or two after it, not the close.

In a 7-day campaign, Impressions run highest on the launch day and lowest on the close:

| Day | Share of Impressions |
|---|---|
| Launch (day 1) | 15.8% |
| Day 2 | 12.5% |
| Day 3 | 10.8% |
| Day 4 | 9.1% |
| Day 5 | 8.2% |
| Day 6 | 8.5% |
| Close (day 7) | 7.7% |

A 14-day campaign shows the same shape: close 4.9% against 9.0% on the launch day. [Days between running 4.4% to 7.4%. 7-day campaign: 7,735 campaigns/2,156 businesses on close-day share, 6,036/1,837 on launch-day share. 14-day campaign: 5,657/2,143 on close, 4,270/1,721 on launch.]

This is a finding about where volume sits, not a reason to close early. The people who were going to show up mostly showed up by the launch window, but the closing days still carry their own work: the deadline reminder, the last-call push and the draw itself shape whether the Entrants already signed up finish, respond to the Winner email and stay on the list afterward, the Entrant relationship `giveaway-winner-communications` covers. Cutting a run short trades that closing work away for a volume gain this data does not show happening.

<!-- generated:cmp_weekday -->
| Start weekday | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| Monday | 22,450 | 480 | 4.40 | 26% | 3.8 | 7 |
| Tuesday | 18,732 | 499 (+4%) | 4.26 (-3%) | 26% (+2%) | 3.8 | 7 |
| Wednesday | 19,315 | 504 (+5%) | 4.23 (-4%) | 28% (+6%) | 3.6 | 7 |
| Thursday | 18,614 | 513 (+7%) | 4.43 (+1%) | 27% (+3%) | 3.7 | 7 |
| Friday | 18,244 | 521 (+9%) | 4.53 (+3%) | 27% (+3%) | 3.7 | 7 |
| Saturday | 8,399 | 438 (-9%) | 4.44 (+1%) | 28% (+9%) | 3.5 | 7 |
| Sunday | 11,374 | 449 (-6%) | 4.52 (+3%) | 27% (+4%) | 3.7 | 7 |
<!-- /generated -->

Start weekday shows no difference on any measure. Businesses favour weekdays, and the data gives no reason to prefer one day over another.

<!-- generated:cmp_recency -->
| Gap since previous campaign, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| first campaign | 5,017 | 333 | 3.19 | 31% | 3.2 | 5 |
| previous within 30 days | 25,947 | 470 (+41%) | 3.96 (+24%) | 38% (+22%) | 2.7 | 6 |
| previous 31 to 90 days | 4,855 | 496 (+49%) | 3.51 (+10%) | 33% (+6%) | 3.1 | 5 |
| previous 91 to 365 days | 3,307 | 434 (+30%) | 3.36 (+5%) | 31% (+0%) | 3.2 | 5 |
| previous over a year | 684 | 382 (+15%) | 3.12 (-2%) | 32% (+3%) | 3.2 | 5 |
<!-- /generated -->

<!-- generated:cmp_recency_vertical -->
| Vertical (regex proxy) | First campaigns | Within 30 days | Contestants | Contestants per impression |
|---|---|---|---|---|
| music_media | 700 | 5,157 | +46% | +19% |
| gaming | 1,481 | 6,084 | +35% | +15% |
| unclassified | 809 | 4,865 | +68% | +17% |
| technology | 515 | 4,008 | +72% | +47% |
| fitness_outdoor | 346 | 1,047 | -32% | +6% |
| kids_family_pets | 235 | 1,191 | +1% | -9% |
| fashion_beauty | 327 | 1,561 | +105% | +35% |
| food_drink | 190 | 585 | +66% | +22% |
| travel_events | 139 | 484 | +37% | +37% |
| home | 134 | 647 | +26% | +25% |
| software | 141 | 318 | +69% | +42% |
<!-- /generated -->

A campaign that starts within 30 days of the business's previous one draws more Entrants and gets about a third more of them to enter than a business's first campaign, with fewer Impressions needed per Entrant. Past 30 days the entry-rate gain is gone while the Entrant gain stays, which reads as a warm audience returning. It holds in every industry with enough campaigns. Momentum is the one timing finding with a consistent direction, and it describes businesses that ran campaigns close together, so it cannot say that scheduling alone caused the lift.

## Build lead time (extracted)

A wider set than the campaigns behind the numbers above (167,068 campaigns, 25,482 businesses, crypto and token formats included): the recorded create date sits after the campaign's start date in 27% of them. That is not a business building after launch. The field also updates on a later edit, so for about a quarter of these campaigns it reads as last-modified, not build lead time. Treat every number below with that in mind.

Among the campaigns where the create date sits before the start date, the typical lead time is 1 day, the upper quarter 4 days, the top tenth 12 days. Most businesses with a usable lead figure built the campaign the day before launch or closer.

| Build lead | Campaigns | Businesses | Conversion Rate | Actions per Entrant | Methods |
|---|---|---|---|---|---|
| Same day | 17,907 | 5,031 | 30% | 5.08 | 8 |
| 1 to 2 days | 8,762 | 3,280 | 29% | 4.97 | 8 |
| 3 to 7 days | 7,437 | 2,892 | 28% | 4.67 | 7 |
| 8 or more days | 7,753 | 2,704 | 28% | 4.21 | 7 |

Same-day builds get as many Entrants to enter as campaigns built a week or more ahead. A longer lead buys time for assets and partner briefs, not a better Conversion Rate on its own.

Source: analysis/output/field_cuts.json (build_lead_days, by_build_lead).

## Duration by plan tier and hosting mix (extracted)

Premium accounts run the longest campaigns with the most methods, Hobby accounts run the shortest and Free accounts use the fewest. [167,068 campaigns, 25,482 businesses total.]

| Plan tier | Campaigns | Businesses | Typical duration | Methods |
|---|---|---|---|---|
| Premium | 3,068 | 550 | 19 days | 9 |
| Free | 14,364 | 5,423 | 12 days | 4 |
| Pro | 89,858 | 15,115 | 11 days | 8 |
| Business | 46,880 | 5,877 | 11 days | 7 |
| Hobby | 12,892 | 3,164 | 10 days | 6 |

By growth stage, startups run short and enterprises run long:

| Growth stage | Campaigns | Businesses | Typical duration | Methods |
|---|---|---|---|---|
| Startups | 14,661 | 4,088 | 11 days | 9 |
| Enterprises | 2,902 | 280 | 17 days | 7 |

Hosting mix tracks the same pattern. Campaigns that keep most of their Impressions on the Gleam-hosted page run a much shorter typical length than campaigns that lean on the embed.

| Share of Impressions on the hosted page | Campaigns | Businesses | Typical days |
|---|---|---|---|
| 90% or more hosted | 36,817 | 8,400 | 10 |
| 50 to 90% hosted | 3,274 | 1,271 | 25 |
| 10 to 50% hosted | 7,125 | 1,660 | 27 |
| Mostly embedded | 7,444 | 1,568 | 18 |

An embed sits inside a page the business already controls, so there is less pressure to close it down on a fixed date.

More methods and a longer run go together in both of these breakdowns, which is the account tier and the hosting choice describing each other as much as describing duration on its own.

Source: analysis/output/field_cuts.json (by_tier, by_hosted_share), analysis/output/industries.json (by_org_stage).

## Region (extracted)

A short, high-entry-rate format shows up strongly in South America and, more specifically, in Portuguese-language and Brazilian YouTube-hosted campaigns, running well below the typical 16-day campaign length at close to double the typical Conversion Rate.

| Group | Campaigns | Businesses | Typical duration | Conversion Rate |
|---|---|---|---|---|
| South America | 1,885 | 269 | 4 days | 53% |
| Portuguese-language | 563 | 68 | 1 day | 60% |
| Brazilian YouTube-hosted | 225 | 28 | 2 days (8 methods) | 56% |

This is a short, high-entry-rate format run by a specific, well-established group of businesses, not a timing technique that travels. A short run works well here because the businesses running it already have an audience primed for a fast giveaway, not because cutting a run to a few days raises the Conversion Rate by itself.

Source: analysis/output/field_cuts.json (by_continent, by_language), analysis/output/industries.json (by_youtube_country).

## Response and draw windows (extracted)

Almost every campaign keeps the platform's 7-day default for both the draw window and the response window, so this mostly shows businesses keeping the default, not choosing seven days on purpose. [96% of campaigns use the 7-day draw window, 96% the 7-day response window, 54,298 campaigns, 10,602 businesses.]

Response window length tracks only a small difference in Conversion Rate, and a longer window pairs with a longer campaign, not a slower-responding Entrant.

| Response window | Campaigns | Businesses | Conversion Rate |
|---|---|---|---|
| 1-3 days | 1,353 | 389 | 31% |
| 4-7 days (default) | 51,881 | 10,205 | 30% |
| 8-14 days | 622 | 190 | 30% |
| 15+ days | 404 | 190 | 26% (20-day campaign typical) |

Source: analysis/output/field_cuts.json (terms, by_response_days).

## Start weekday and month, a second check (extracted)

A separate check, using all runs at their actual length, for a second read on the weekday and month findings above.

<!-- generated:tm_weekday -->
| Start weekday | Campaigns | Businesses | Entrants | Conversion Rate |
|---|---|---|---|---|
| Monday | 22,498 | 6,624 | 479 | 26% |
| Tuesday | 18,754 | 6,011 | 499 | 26% |
| Wednesday | 19,348 | 6,043 | 504 | 28% |
| Thursday | 18,636 | 6,082 | 512 | 27% |
| Friday | 18,276 | 5,744 | 521 | 27% |
| Saturday | 8,425 | 3,516 | 438 | 28% |
| Sunday | 11,411 | 4,226 | 449 | 27% |
<!-- /generated -->

Entrants run from 2,116 to 2,287 and the Conversion Rate from 27.0% to 29.1% across the week, the same flat read as the duration-matched weekday table above. Weekday still shows no usable difference.

Month moves once, in December, and nowhere else:

| Start month | Conversion Rate | Entrants | Days |
|---|---|---|---|
| December (4,253 campaigns, 1,469 businesses) | 33.2% | 2,342 | 10 |
| Every other month (2,312 to 3,151 campaigns per month, 1,195 to 1,506 businesses) | 26.5% to 28.0% | 2,066 to 2,256 | 15 to 20 |

Every month outside December sits inside a 1.5-point range on Conversion Rate. December clears the nearest of them by 5.2 points and the furthest by 6.7, on a run half to two-thirds the length of the rest of the year.

The December lift holds inside most industries too, not just because certain industries happen to start more campaigns in December:

| Industry | December | Next-best month | Gap |
|---|---|---|---|
| Electronics and tech | 44.3% (1,065 campaigns, 289 businesses) | January, 30.5% | 13.8 pts |
| Home and garden | 41.7% (229 campaigns, 73 businesses) | August, 36.4% | 5.3 pts |
| Media and entertainment | 34.0% (709 campaigns, 136 businesses) | March, 27.0% | 7.0 pts |
| Toys, hobbies and collectibles | 33.1% (73 campaigns, 42 businesses) | July, 29.9% | 3.2 pts |
| Travel and events | 32.7% (130 campaigns, 51 businesses) | August, 31.2% | 1.5 pts |
| Health, wellness and fitness | 31.9% (76 campaigns, 41 businesses) | March, 30.9% | 1.0 pts |
| Gaming and esports | 29.7% (801 campaigns, 361 businesses) | July, 29.1% | 0.6 pts |

December is not the best month in five industries, though four of them sit within a point and a half of December's rate. Apparel and fashion is the clear exception, peaking 9.1 points above its December rate.

| Industry | Peak month | Peak Conversion Rate | December Conversion Rate |
|---|---|---|---|
| Retail and marketplace | May | 35.1% | 34.4% |
| Food and drink | January | 34.1% | 33.1% |
| Automotive | July | 27.6% | 27.0% |
| Sports and outdoors | November | 26.6% | 25.8% |
| Apparel and fashion | May | 35.5% | 26.4% |

[Campaigns/businesses: 86/29 (retail and marketplace), 159/73 (food and drink), 133/35 (automotive), 182/111 (sports and outdoors), 149/67 (apparel and fashion).]

Source: `analysis/output/prize_timing_cuts.json` (`by_start_weekday`, `by_start_month`, `by_start_month_and_industry`).

## Launch and pre-release wording (extracted)

Campaigns whose name, incentive name or description carries launch or pre-release wording, against campaigns with none:

| Wording | Campaigns | Businesses | Conversion Rate | Referrals % of Entrants | Share offered | Email offered | Days |
|---|---|---|---|---|---|---|---|
| No launch wording | 33,788 | 6,070 | 28% | 12 | 45% | 43% | 16 |
| Launch or release | 1,281 | 599 | 26.7% | 17 | 45% | 47% | 15 |
| Coming soon or waitlist | 256 | 186 | 24% | 22 | 55% | 37% | 16 |
| Crowdfunding | 117 | 77 | 22.8% | 18 | 77% | 60% | 18 |
| Wishlist or pre-save | 115 | 53 | 17.9% | 14 | 53% | 24% | 14 |
| Pre-order | 101 | 62 | 27.1% | 18 | 49% | 39% | 25 |

Launch wording gets a little fewer viewers to enter than the no-wording baseline and brings in more referrals. Crowdfunding wording leans hardest on sharing and email (the table above), wishlist or pre-save wording converts worst, and pre-order campaigns run the longest.

By industry, electronics and tech leads on launch/release and crowdfunding wording, while media and entertainment leads on pre-order wording. Every count below 30 campaigns is advice only.

| Wording | Leading industry (campaigns) | Next industry (campaigns) |
|---|---|---|
| Launch or release | Electronics and tech (320) | Gaming and esports (269) |
| Crowdfunding | Electronics and tech (31) | Toys, hobbies and collectibles (29), gaming and esports (23) |
| Pre-order | Media and entertainment (36) | Gaming and esports (27) |

Two Prize types carry a release date, and both are advice only given the small counts. Spotify pre-saves lead further out the earlier the campaign starts:

| Start timing | Typical lead |
|---|---|
| 30+ days before release | 66 days |
| Under 30 days before release | 10 days |

Steam game campaigns convert best starting just before release, and worst starting well ahead of it:

| Start timing | Conversion Rate |
|---|---|
| 30+ days before release | 18% |
| Under 30 days before release | 26% |
| Within 30 days after release | 25% |

Most Steam campaigns in this group start long after their release date, a typical 646 days after. [Spotify: 30/5 campaigns/businesses 30+ days before, 26/14 under 30 days before. Steam: 24/18 (30+ days before), 25/18 (under 30 days before), 36/29 (within 30 days after), 148/54 (typical-lag group).]

Source: `analysis/output/prize_timing_cuts.json` (`by_launch_wording`, `launch_wording_by_industry`, `campaign_start_against_release_date`).

## Run length by country (extracted)

Typical run length varies widely by the business's country, from 1 day in Brazil to 21 in the UK.

| Country | Typical duration | Campaigns | Businesses |
|---|---|---|---|
| Brazil | 1 day | 5,860 | 563 |
| Japan | 6 days | 6,505 | 291 |
| United States | 14 days | 58,843 | 9,105 |
| United Kingdom | 21 days | 15,716 | 1,847 |

Japan's raw figure carries a large share of crypto and SaaS businesses, with those removed, Japan's typical run rises to 12 days [1,144 campaigns, 138 businesses]. Doing the same for Brazil, the UK and the US leaves them close to their raw figures, at 1, 22 and 14 days.

By industry across all countries, finance and crypto businesses run the shortest typical length and food and drink the longest. [Finance and crypto: 7 days, 43,170 campaigns, 7,138 businesses. Food and drink: 19 days, 4,774 campaigns, 914 businesses.] A country with a large crypto share reads shorter in the raw figure until that share is set aside, which is what the Japan figures above show directly.

Source: `analysis/output/indicators.json` (`duration_by_country`, `duration_by_industry`, `mechanics_by_country_excluding_crypto`).

## Start hour and weekend starts by country (extracted)

Local start hour is estimated with one UTC offset per country and no daylight saving, so read it as a rough window, not a precise hour. Countries spanning several time zones (the US, Canada, Brazil, Australia) carry up to three hours of error on top of that.

| Country | Typical local start hour | Campaigns | Businesses |
|---|---|---|---|
| India | Midnight | 6,010 | 873 |
| Brazil | Midnight | 5,860 | 563 |
| South Korea | Midnight | 4,521 | 537 |
| Japan | 11:00 | 6,505 | 291 |
| Germany | 13:00 | 3,530 | 472 |

The share of campaigns starting on a local Saturday or Sunday varies less by country, from about 10% (Japan, Singapore) up to about 22% (India, Germany), with most other countries measured between 15% and 20%. The same single-offset caveat applies. [Japan 10.5%, Singapore 10.9%, India 22.2%, Germany 21.5%.]

Source: `analysis/output/indicators.json` (`start_hour_local_by_country`, `weekend_start_by_country`).

## Run length by starting point (extracted)

Duration barely varies by where the build started from, except for two specific templates that run notably longer.

| Build source | Typical duration | Campaigns | Businesses |
|---|---|---|---|
| Library template | 15 days | 10,477 | 6,709 |
| Own earlier campaign copied | 14 days | 69,476 | 5,830 |
| Blank build | 15 days | 28,223 | 11,226 |
| Purchase Product template | 29 days | 31 | 30 |
| Every Entry Type template | 26.5 days | 50 | 48 |

Source: `analysis/output/templates.json` (`source_mix`, `by_template`).

## Repeat business concentration by country (extracted)

Average campaigns per business varies sharply by country: Japan runs highest, Spain lowest among countries with at least ten businesses in this group. [Japan 22 campaigns/business, 6,505 campaigns, 291 businesses. Spain 4 campaigns/business, 2,142 campaigns, 562 businesses.] In Japan, 83% of campaigns come from a business on its eleventh campaign or later, against 29% in Spain, the same gap in a second measure. A country's campaign count partly reflects a small number of businesses who run often, more so in Japan than in most other countries measured here.

Source: `analysis/output/indicators.json` (`repeat_organizer_by_country`).
