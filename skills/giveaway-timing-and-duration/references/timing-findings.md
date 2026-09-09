# Timing findings

Extracted from the ordinary segment of the export (crypto, ambiguous and purchase-only campaigns removed). All campaigns reached at least 1,000 contestants. Duration is end date minus start date in days as recorded, so a campaign extended after launch shows its final length.

<!-- generated:timing -->
Duration: median 16 days, IQR 8 to 31, 90th percentile 43 (n=37,180). By campaign size: 1k-2.5k 15 days, 2.5k-10k 18 days, 10k+ 20 days.

| Duration (days) | Share of campaigns | Entries per contestant, median |
|---|---|---|
| 1-3 | 12% | 2.94 |
| 4-7 | 13% | 4.19 |
| 8-14 | 20% | 4.4 |
| 15-30 | 30% | 4.62 |
| 31-60 | 19% | 5.07 |
| 61-180 | 5% | 3.59 |
| 181+ | 1% | 3.6 |

| Start month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Share of campaigns | 6.6% | 7.6% | 8.9% | 7.8% | 8.4% | 8.5% | 7.7% | 8.3% | 7.6% | 8.3% | 8.6% | 11.8% |

| Start weekday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|---|---|---|---|---|---|---|---|
| Share of campaigns | 18.7% | 16.4% | 17.0% | 16.0% | 16.7% | 6.4% | 8.9% |
<!-- /generated -->

## Reading the tables

- Two to four weeks is the most common choice at every size, and half of all campaigns run between 8 and 31 days. Campaigns above 10,000 contestants run a little longer (median 20 days) than those under 2,500 (median 15 days).
- Entries per contestant rise with duration up to about two months, then fall. Repeatable daily actions accumulate over time, and campaigns past two months are mostly evergreen or recurring formats with different mechanics. This describes the campaigns organizers ran at each length. It cannot say that shortening or lengthening a campaign would change its entries, and it says nothing about reach or results.
- December holds about 12% of starts, half again the share of a typical month. March, May, June and November are the next busiest. January is the quietest.
- Five in six campaigns start on a weekday. Monday is the most common start day and Saturday the rarest.

## Experience (extracted)

Organizers on their eleventh or later campaign had a median 2,194 contestants and 44% conversion in the clean subset (n=6,031), against 1,844 and 33% on a first campaign (n=1,655). Second campaigns sat at 1,877 and 34%, third to fifth at 1,943 and 34%, sixth to tenth at 2,075 and 35%. The export holds only campaigns that passed 1,000 contestants, so organizers who stopped after a weak first run are missing, and the curve mostly shows who kept going. Read it with the recency finding: running again, soon, is the pattern that comes with better numbers.

## Limits

- Duration and start date co-vary with organizer type, budget and season. The data cannot separate a duration effect from those.
- A campaign that runs for years (the maximum is over 13,000 days) is an always-on widget, and its figures describe a different product.
- Start dates are in UTC. Local-time patterns for a specific audience will shift by a day at the edges.

## Duration, weekday and recency against contestants and conversion (extracted)

Impressions in the export are unique per day, so a visitor who returns counts again each day. Repeatable actions (daily bonus, loyalty, timed bonus) and long runs raise impressions per contestant and lower contestants per impression without any change in who entered. The clean subset removes campaigns with a repeatable action and any run over 14 days. Medians, ordinary segment, descriptive only.

<!-- generated:cmp_repeatable -->
| Repeatable actions | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| no repeatable actions | 23,857 | 2,155 | 3.73 | 31% | 3.2 | 6 |
| has repeatable actions | 13,266 | 2,298 (+7%) | 5.84 (+56%) | 22% (-28%) | 4.5 | 10 |
<!-- /generated -->

<!-- generated:cmp_duration -->
| Duration, no repeatable actions | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| 1 to 7 days | 6,806 | 2,024 | 3.22 | 45% | 2.2 | 5 |
| 8 to 14 | 4,830 | 2,144 (+6%) | 3.97 (+23%) | 31% (-31%) | 3.2 | 6 |
| 15 to 30 | 7,030 | 2,233 (+10%) | 3.98 (+24%) | 28% (-38%) | 3.6 | 6 |
| 31 to 60 | 3,751 | 2,201 (+9%) | 3.86 (+20%) | 24% (-46%) | 4.1 | 6 |
| 61 or more | 1,440 | 2,392 (+18%) | 2.94 (-9%) | 23% (-49%) | 4.4 | 5 |
<!-- /generated -->

Longer runs collect about a tenth more contestants and roughly double the impressions per contestant, so contestants per impression halves with no change in who entered. Compare conversion only across campaigns of similar length.

<!-- generated:cmp_weekday -->
| Start weekday | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| Monday | 6,943 | 2,210 | 4.29 | 27% | 3.7 | 7 |
| Tuesday | 6,080 | 2,148 (-3%) | 4.34 (+1%) | 28% (+2%) | 3.6 | 7 |
| Wednesday | 6,297 | 2,239 (+1%) | 4.18 (-3%) | 29% (+6%) | 3.5 | 7 |
| Thursday | 5,944 | 2,186 (-1%) | 4.41 (+3%) | 27% (-1%) | 3.7 | 7 |
| Friday | 6,195 | 2,235 (+1%) | 4.53 (+6%) | 28% (+2%) | 3.6 | 7 |
| Saturday | 2,366 | 2,290 (+4%) | 4.17 (-3%) | 29% (+6%) | 3.5 | 7 |
| Sunday | 3,298 | 2,132 (-4%) | 4.40 (+3%) | 29% (+5%) | 3.5 | 7 |
<!-- /generated -->

Start weekday shows no difference on any measure. Organizers favour weekdays, and the data gives no reason to prefer one day over another.

<!-- generated:cmp_recency -->
| Gap since previous campaign, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| first campaign | 1,650 | 1,844 | 3.58 | 33% | 3.0 | 6 |
| previous within 30 days | 6,776 | 2,136 (+16%) | 3.57 (-0%) | 44% (+32%) | 2.3 | 5 |
| previous 31 to 90 days | 1,674 | 2,091 (+13%) | 3.78 (+6%) | 33% (+1%) | 3.0 | 6 |
| previous 91 to 365 days | 1,248 | 2,085 (+13%) | 3.57 (-0%) | 32% (-2%) | 3.1 | 6 |
| previous over a year | 288 | 1,820 (-1%) | 3.18 (-11%) | 33% (-1%) | 3.1 | 5 |
<!-- /generated -->

<!-- generated:cmp_recency_vertical -->
| Vertical (regex proxy) | First campaigns | Within 30 days | Contestants | Contestants per impression |
|---|---|---|---|---|
| unclassified | 950 | 4,752 | +13% | +35% |
| gaming_streaming | 345 | 962 | +27% | +25% |
| travel_events | 55 | 137 | +16% | +5% |
| tech_phones_gadgets | 79 | 366 | +73% | +26% |
| food_drink | 44 | 89 | +0% | +18% |
| home_garden | 41 | 144 | +24% | +69% |
| fitness_outdoor | 33 | 38 | +35% | +29% |
<!-- /generated -->

A campaign that starts within 30 days of the organizer's previous one draws more contestants and converts a third better than an organizer's first campaign, with fewer impressions per contestant. Past 30 days the conversion gain is gone while the contestant gain stays, which reads as a warm audience returning. It holds in every vertical with enough campaigns. Momentum is the one timing finding with a consistent direction, and it describes organizers who ran campaigns close together, so it cannot say that scheduling alone caused the lift.
