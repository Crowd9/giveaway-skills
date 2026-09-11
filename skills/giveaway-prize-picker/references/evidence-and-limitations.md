# Evidence and limitations

## The source

A private dataset of 167,068 campaigns from one giveaway platform, each with at least 100 valid (unique) Entrants. Fields: Entrant, entry and Impressions (views of the campaign page) counts, dates and duration, nested Prize records (name, value, currency, quantity, position), the campaign's public title and description, Entry Methods with counts, plan tier, and organizer contact details. Organizer details, ids, links and raw text are never reproduced in this repository.

The benchmarks below describe the 117,348 of those campaigns left after removing crypto, purchase-only and finance_crypto organizers.

| Entrant count | Share of the 117,348 campaigns |
|---|---|
| 100 to 250 | 28% |
| 250 to 500 | 22% |
| 500 to 1,000 | 19% |
| 1,000 to 2,500 | 17% |
| 2,500 to 10,000 | 11% |
| Above 10,000 | 3% |

Where the repository summary says the skills rest on about 966,000 entry actions, that total is not a field in the dataset and no analysis file carries it. It is the sum of the per-family action counts in the action families table in giveaway-entry-method-planner, the column headed with how many Entrants took the action. Each one is an entry action offered in one of the campaigns behind these numbers, for which the dataset recorded how many Entrants took it.

| Action family | Entrants who took it |
|---|---|
| Visits | 376,120 |
| Follows | 173,303 |
| Shares | 81,916 |
| Bonus or code | 64,921 |
| Custom actions | 52,841 |
| Email signups | 49,688 |
| Post engagements | 36,525 |
| Community joins | 32,383 |
| Questions | 31,477 |
| Content posts | 26,338 |
| Account connections | 24,194 |
| Paid subscriptions | 8,413 |
| Downloads | 4,392 |
| Imported entries | 1,390 |

That sums to 966,269, rounded to 966,000.

The dataset's core counts are verified directly. Only USD has enough stated values to support any distribution, the rest are too thin to use. A few stated values are data-entry errors and are treated as such, never corrected.

| Field | Value |
|---|---|
| Campaigns | 167,068 |
| Prize records | 243,835 |
| Businesses | 25,482 |
| Prize value missing | 62.0% of Prize records (149,102 null, 2,099 zero) |
| Stated-value currencies | USD 94,611, GBP 38, EUR 38, AUD 22, CAD 21, plus a handful of others |
| Campaign start years | 2013 to 2026, 68% between 2021 and 2023 |
| Missing fields | 259 campaigns with no entry count, 16,432 with no description |
| Data-entry errors | negative values, and a stated value of 250 million |

## Segmenting before any benchmark

<!-- generated:segments -->
| Segment | Campaigns | Handling |
|---|---|---|
| Ordinary | 117,348 (172,645 prize records, 17,777 organizers) | Basis for every default figure |
| Crypto | 6,288 | Excluded. Described only when a user asks for crypto advice. 38% used a wallet-address entry method |
| Purchase opportunity | 262 | Excluded. The prize is the right to buy something |

Excluded campaigns are similar in size to ordinary ones (crypto median 732 contestants versus 492 ordinary), so exclusion changes who is in the benchmark and leaves the size distribution alone.
<!-- /generated -->

The crypto rule combines Prize names, campaign names, descriptions and Entry Method types. A single weak keyword never decides. Excluding crypto changes who is in the benchmark and leaves campaign size where it was: crypto typical 732 Entrants versus 492 for the rest. Any claim that crypto inflated participation figures is a hypothesis.

A homepage-label industry cut on the campaign analysis confirms the exclusion is not a small correction: finance and crypto is the largest single industry by campaign count, ahead of gaming and esports. See `references/roi-benchmarks.md` for the table this cut produced.

## What the campaigns behind these numbers show

Two shorthands run through the tables below. The middle half is the middle half of campaigns, running from the lower quarter to the upper quarter. The top-tenth mark is the level nine campaigns in ten sit below, so it marks the top tenth without naming an extreme.

<!-- generated:benchmark -->
| Measure | Value | n or note |
|---|---|---|
| Valid contestants | median 492, IQR 225 to 1,292, 90th pct 3,345 | 117,348. Floor is 101 by selection |
| Valid entries | median 2,320 | 117,128. Entries count actions, and one person makes many |
| Entries per contestant | median 4.39, IQR 2.74 to 7.05 | 117,128 |
| Impressions | median 2,029 | 117,258 with a non-zero value. Zeros treated as unknown |
| Duration | median 14 days, IQR 7 to 29 | 116,491. Maximum 365 days (evergreen campaigns) |
| One prize record | 82.4% of campaigns | quantity may still exceed 1 |
| Any quantity above 1 | 31.8% of campaigns | units listed, which may differ from Winners |
| Prize value stated | 37.7% of prize records | 62.3% unknown |
| Stated USD values | median 125, IQR 50 to 424, 90th pct 1,199 | 65,018 records. Max 1,000,000 |
| Stated EUR values | median 75, IQR 39 to 332, 90th pct 2,200 | 35 records. Max 9,100 |
| Stated GBP values | median 62, IQR 25 to 400, 90th pct 450 | 34 records. Max 1,200 |
| Stated CAD values | median 545, IQR 200 to 2,180, 90th pct 4,500 | 21 records. Too few to use. Max 35,000 |
| Stated AUD values | median 600, IQR 129 to 3,600, 90th pct 6,000 | 18 records. Too few to use. Max 60,000 |
| Fully valued campaign totals (USD) | median 299, IQR 90 to 1,000 | 43,109 campaigns. Max 10,000,000 |
| Repeat organizers | 3,818 organizers with 5+ campaigns account for 81.5% of campaigns | patterns can reflect prolific accounts |
| Plan tier | Business 29,966, Pro 62,493, Hobby 10,838, Free 12,039, Premium 2,007, Not Available 5 | tier at export time |
<!-- /generated -->

## By campaign size

Every size group is still a selected sample with a floor, and bigger campaigns come from bigger businesses with bigger budgets, so differences between size groups describe who runs what. They do not show that a Prize made a campaign larger.

<!-- generated:bands -->
| Band (valid contestants) | Campaigns | Organizers | Value stated | Stated USD median (n) | Campaign total USD median (n) | One prize record | Entries per contestant | Duration median |
|---|---|---|---|---|---|---|---|---|
| 100-250 | 33,338 | 9,607 | 36% | 69 (16,411) | 120 (11,715) | 85% | 4.09 | 12 days |
| 250-500 | 25,892 | 6,554 | 37% | 80 (13,293) | 149 (9,455) | 84% | 4.61 | 14 days |
| 500-1k | 21,935 | 5,550 | 36% | 120 (11,515) | 260 (7,838) | 82% | 4.68 | 14 days |
| 1k-2.5k | 20,137 | 5,123 | 40% | 210 (12,345) | 530 (7,794) | 79% | 4.32 | 15 days |
| 2.5k-10k | 12,828 | 3,035 | 42% | 375 (9,313) | 1,299 (5,152) | 78% | 4.39 | 18 days |
| 10k+ | 3,218 | 762 | 37% | 779 (2,141) | 3,000 (1,155) | 80% | 4.39 | 18 days |

Primary prize category (first prize record) by band, share of campaigns:

| Category | 100-250 | 250-500 | 500-1k | 1k-2.5k | 2.5k-10k | 10k+ |
|---|---|---|---|---|---|---|
| Tech hardware | 10.8% | 12.5% | 16.8% | 23.5% | 29.8% | 36.9% |
| Gift card or cash | 13.0% | 18.4% | 13.7% | 11.0% | 9.8% | 8.1% |
| Bundle or box | 9.7% | 10.9% | 11.1% | 9.9% | 8.7% | 4.9% |
| Experience, travel, tickets | 6.4% | 4.6% | 4.0% | 4.4% | 5.4% | 5.4% |
| Game items or skins | 11.9% | 8.9% | 7.9% | 6.5% | 5.3% | 5.0% |
| Merch, apparel, collectibles | 3.8% | 3.6% | 3.8% | 3.1% | 3.7% | 4.6% |
| Home, garden, appliance | 1.1% | 1.3% | 1.7% | 2.7% | 2.9% | 1.4% |
| Regulated goods (firearms) | 0.3% | 0.5% | 0.8% | 2.0% | 2.9% | 9.1% |
| Sports and outdoor gear | 0.6% | 0.8% | 1.0% | 1.3% | 1.3% | 0.6% |
| Food, drink, consumables | 0.8% | 1.0% | 1.2% | 1.5% | 1.1% | 0.4% |
| Subscription or membership | 1.3% | 1.0% | 1.0% | 0.9% | 0.6% | 0.3% |
| Discount or coupon | 0.6% | 0.3% | 0.5% | 0.6% | 0.3% | 0.1% |
<!-- /generated -->

## Plan tier, extended

The plan tier row above comes from the campaigns at large. A cut on the same field, restricted to campaigns with a labelled site, breaks format and Conversion Rate out by tier. Free and Hobby convert best and neither offers an email action. Premium runs longest and offers the most Entry Methods, and converts worst. Business and Pro sit in the middle on every measure.

| Tier | Conversion Rate | Campaigns | Businesses | Days | Entry Methods | Email offered |
|---|---|---|---|---|---|---|
| Free | 34% | 14,233 | 5,360 | 11 | 4 | 0% |
| Hobby | 32% | 12,725 | 3,133 | 10 | 6 | 0% |
| Pro | 28% | 88,816 | 14,971 | 11 | 8 | 28% |
| Business | 26% | 46,822 | 5,852 | 11 | 7 | 31% |
| Premium | 24% | 3,076 | 547 | 18 | 9 | 42% |

## Business scale

Homepage labels also split businesses into listed and private companies. Private businesses run shorter campaigns with a higher referral rate, listed businesses run longer campaigns with a lower one. Revenue cuts inside this data, matched against Fortune-500-like companies, sit below the ten-business floor for anything but advice [7 to 20 businesses per group].

| Business type | Duration | Referrals % of Entrants | Campaigns | Businesses |
|---|---|---|---|---|
| Private | 14 days | 20.3 | 30,975 | 2,975 |
| Listed | 20 days | 12.3 | 1,831 | 128 |

## Repeat businesses

Campaign sequence tracks how many campaigns a business had already run. Conversion Rate rises and duration shrinks the more campaigns a business has already run. Recency does not explain it: businesses active in the last 12 months convert about the same as inactive ones (28% against 27%). The likelier explanation is who kept going: businesses whose early campaigns worked well enough are the ones who keep running them.

| Campaign sequence | Conversion Rate | Duration | Campaigns | Businesses |
|---|---|---|---|---|
| First campaign | 26% | 15 days | 25,482 | 25,482 |
| Eleventh or later | 30% | 9 days | 91,694 | 2,531 |

## Inferred Prize values from text

To reduce the 61% gap we parsed explicit amounts from Prize names ("$4,000 RTX PC"), from "worth / valued at / MSRP" phrases in descriptions, and from campaign titles of single-Prize campaigns. Validation against listings that carried both a stated and a parsed value agreed within ±20% most of the time. Disagreements are mostly totals across several Prizes, marketing round numbers, or a cash component inside a larger bundle. The "$" symbol is recorded as "USD?" because it is ambiguous between USD, CAD, AUD and others, so parsed-only "$" values are kept separate from stated values and never used in a listing-level claim.

Coverage rises from 40.5% to 48.5% of listings.

| Parsing measure | Value |
|---|---|
| Listings with a parsed value | 9,847 (7,127 from Prize names, 823 from campaign titles, 1,897 from description phrases) |
| Listings gaining a value with none stated | 4,634 |
| Listings with both a stated and a parsed value | 4,824, agreeing within ±20% for 81% |
| Parsed-only "$" values | 3,342 listings, typical 399, middle half 100 to 1,000, max 2.4 million (a campaign-wide total an organizer typed into one Prize listing) |

Parsed values are what organizers wrote, never what they paid.

Category typical figures for stated values are given in the taxonomy as reference ranges. We do not fill missing listings with them.

## Prize value, adjusted

A  field cut confirms the coverage gap holds at scale: 38.8% of Prize listings carry a stated value, and 99.9% of those are USD. Every typical figure below rests on that self-selected minority.

Campaigns whose every Prize carried a stated USD value: 43,173, from 9,180 businesses. Prize cost per Entrant is the stated pool divided by Entrants, and stated value is what the organizer wrote, which need not be what they paid.

<!-- generated:ev_value_bands -->
| Stated pool, USD | Campaigns | Entrants | Actions per Entrant | Stated USD per Entrant |
|---|---|---|---|---|
| under 50 | 6,066 | 266 | 6.05 | 0.07 |
| 50-99 | 5,224 | 320 | 5.89 | 0.19 |
| 100-249 | 8,628 | 403 | 4.42 | 0.37 |
| 250-499 | 6,166 | 618 | 4.39 | 0.55 |
| 500-999 | 5,888 | 850 | 4.39 | 0.77 |
| 1000-2499 | 6,468 | 1,303 | 4.39 | 1.10 |
| 2500-4999 | 2,777 | 2,133 | 4.96 | 1.57 |
| 5000-9999 | 1,109 | 2,132 | 4.35 | 2.92 |
| 10000-24999 | 559 | 1,545 | 4.49 | 9.23 |
| 25000-49999 | 131 | 1,858 | 3.68 | 17.48 |
| 50000+ | 157 | 1,095 | 4.25 | 108.93 |
<!-- /generated -->

Prize value and Entrant count move together only loosely: ten times the Prize value comes with about 2.2 times the Entrants, and value accounts for about 23% of the variation in Entrant counts [the `value_regression` cut in `context_checks.json`, 43,173 campaigns from 9,180 businesses]. The table above rises through the middle bands and falls back at the largest pools.

Most campaigns spend little: 74% of these campaigns used a pool of 1,000 USD or less, and 46% under 250 USD.

### Prize pool by industry, business type, tier and category

Stated USD Prize pool for campaigns with a full value, cut four ways across the campaigns behind these numbers. Share is that cut's campaign count against the same group's total campaign count, so it is the share of campaigns in the group that stated a value, not a share of Prize listings. State it beside every typical figure here, coverage runs from 9% to 69% and a thin-coverage figure describes a self-selected subset.

By industry:

| Industry | Campaigns | Share with value | Typical pool USD | Middle half | USD % of Entrants |
|---|---|---|---|---|---|
| Electronics and tech | 2,422 | 33% | 1,000 | 440 to 2,400 | 40 |
| Gaming and esports | 2,082 | 33% | 800 | 300 to 2,000 | 26 |
| Media and entertainment | 2,114 | 42% | 500 | 200 to 1,500 | 17 |
| Sports and outdoors | 1,210 | 53% | 1,000 | 491 to 2,250 | 38 |
| Food and drink | 888 | 50% | 750 | 318 to 2,000 | 27 |
| Home and garden | 1,043 | 59% | 829 | 345 to 1,992 | 33 |
| Apparel and fashion | 675 | 39% | 1,000 | 499 to 1,980 | 31 |
| Travel and events | 462 | 34% | 1,199 | 519 to 2,682 | 47 |
| Automotive | 724 | 64% | 1,725 | 754 to 3,892 | 32 |
| Toys, hobbies and collectibles | 245 | 25% | 500 | 250 to 1,620 | 24 |

By business type:

| Business type | Campaigns | Share with value | Typical pool USD | Middle half | USD % of Entrants |
|---|---|---|---|---|---|
| Brand | 5,282 | 49% | 1,000 | 400 to 2,244 | 38 |
| Retailer | 2,802 | 36% | 822 | 300 to 2,400 | 25 |
| Media publisher | 1,845 | 37% | 553 | 229 to 1,499 | 23 |
| Software | 1,769 | 46% | 1,000 | 400 to 2,490 | 25 |
| Creator | 1,100 | 28% | 698 | 300 to 1,500 | 25 |
| Other | 571 | 37% | 600 | 200 to 1,798 | 25 |
| Service business | 344 | 33% | 1,000 | 470 to 2,500 | 47 |
| Agency | 307 | 36% | 1,250 | 650 to 2,875 | 39 |
| Community | 176 | 38% | 490 | 300 to 1,000 | 27 |
| Nonprofit | 114 | 44% | 1,000 | 508 to 2,498 | 47 |

By plan tier:

| Tier | Campaigns | Share with value | Typical pool USD | Middle half | USD % of Entrants |
|---|---|---|---|---|---|
| Pro | 8,010 | 43% | 699 | 300 to 1,646 | 29 |
| Business | 4,959 | 41% | 1,495 | 500 to 2,848 | 36 |
| Hobby | 574 | 27% | 400 | 148 to 988 | 21 |
| Premium | 548 | 50% | 1,825 | 456 to 4,544 | 16 |
| Free | 246 | 16% | 219 | 100 to 800 | 13 |

By Prize category:

| Category | Campaigns | Share with value | Typical pool USD | Middle half | USD % of Entrants |
|---|---|---|---|---|---|
| Tech hardware | 3,811 | 39% | 900 | 380 to 2,099 | 27 |
| Other or unclassified | 2,923 | 38% | 799 | 316 to 1,999 | 33 |
| Gift card or cash | 1,975 | 53% | 500 | 200 to 1,400 | 20 |
| Bundle or box | 1,456 | 45% | 781 | 300 to 1,856 | 30 |
| Game items or skins | 705 | 33% | 1,125 | 300 to 2,035 | 30 |
| Regulated goods (firearms) | 694 | 66% | 1,836 | 876 to 3,870 | 32 |
| Experience, travel, tickets | 577 | 33% | 1,600 | 575 to 4,000 | 57 |
| Placeholder name | 439 | 30% | 1,200 | 330 to 3,344 | 33 |
| Home, garden, appliance | 387 | 40% | 600 | 350 to 1,449 | 26 |
| Merch, apparel, collectibles | 271 | 23% | 800 | 314 to 1,980 | 30 |
| Sports and outdoor gear | 255 | 58% | 1,050 | 470 to 2,000 | 42 |
| Vehicle | 194 | 69% | 1,999 | 999 to 3,988 | 89 |
| Food, drink, consumables | 176 | 38% | 540 | 200 to 1,189 | 22 |
| Subscription or membership | 127 | 48% | 906 | 458 to 1,980 | 40 |
| Music gear | 113 | 49% | 1,100 | 500 to 1,999 | 33 |
| Tools, craft, DIY | 79 | 40% | 879 | 300 to 2,358 | 24 |
| Beauty and wellness | 73 | 51% | 365 | 250 to 992 | 26 |
| Toys and collectibles | 44 | 9% | 232 | 109 to 1,000 | 14 |

Regulated goods and vehicle Prizes state a value most often (66% and 69%), consistent with retailers who already price these items for sale, and vehicle carries the highest USD % of Entrants of any cut here.

Toys and collectibles states a value least often, so its typical pool describes a small, self-selected group [9% of 493 campaigns, 44 listings].

Premium-tier campaigns post the highest typical pool on a below-typical USD % of Entrants. Free campaigns post the lowest of both together, a floor at both ends.

Source: `analysis/output/prize_timing_cuts.json` (prize_pool_by_industry, prize_pool_by_business_type, prize_pool_by_tier, prize_pool_by_category).

### Crowd per Prize dollar, by Prize category

Each campaign's Entrants divided by the typical Entrants for other campaigns at the same stated Prize cost, then the typical of that ratio per category. That ratio is crowd per Prize dollar: how much crowd a category draws once you strip out how much was spent. 1.00 means typical for the money, above 1.00 means the category draws more crowd than its price tag suggests, and below 1.00 means less. Categories with at least 100 valued campaigns.

<!-- generated:ev_crowd_category -->
| Category | Campaigns | Entrants | Crowd per Prize dollar | For the money |
|---|---|---|---|---|
| Regulated goods (firearms) | 1,579 | 2,107 | 2.03 | 103% above typical |
| Music gear | 452 | 1,306 | 1.90 | 90% above typical |
| Tech hardware | 22,076 | 900 | 1.43 | 43% above typical |
| Home, garden, appliance | 2,452 | 913 | 1.35 | 35% above typical |
| Tools, craft, DIY | 581 | 941 | 1.16 | 16% above typical |
| Food, drink, consumables | 1,467 | 694 | 1.14 | 14% above typical |
| Beauty and wellness | 815 | 472 | 1.11 | 11% above typical |
| Gift card or cash | 17,880 | 436 | 1.10 | 10% above typical |
| Sports and outdoor gear | 1,366 | 776 | 1.04 | 4% above typical |
| Vehicle | 733 | 805 | 1.04 | 4% above typical |
| Art and custom | 185 | 397 | 1.02 | typical |
| Placeholder name | 5,629 | 547 | 0.95 | 5% below typical |
| Bundle or box | 13,409 | 499 | 0.89 | 11% below typical |
| Toys and collectibles | 2,297 | 420 | 0.86 | 14% below typical |
| Unclassified | 34,888 | 423 | 0.82 | 18% below typical |
| Merch, apparel, collectibles | 5,548 | 497 | 0.79 | 21% below typical |
| Game items or skins | 11,220 | 363 | 0.74 | 26% below typical |
| Discount or coupon | 1,054 | 726 | 0.73 | 27% below typical |
| Exclusive access | 535 | 380 | 0.61 | 39% below typical |
| Experience, travel, tickets | 6,319 | 404 | 0.61 | 39% below typical |
| Subscription or membership | 1,636 | 426 | 0.52 | 48% below typical |
<!-- /generated -->

Gaming PCs and GPUs draw far more crowd than their price tag suggests, consoles draw more too, phones and peripherals draw about what their price tag suggests. Cash and gift cards draw a little more than their price tag suggests at 1.10, broadly wanted and close to what the money buys. This agrees with Gleam's internal analysis of the same export, which found the same ordering with a wider spread.

### Crowd per Prize dollar, by number of Prize units

| Prize units | Campaigns | Businesses | Crowd per Prize dollar | For the money | Entrants |
|---|---|---|---|---|---|
| 1 | 26,976 | 5,681 | 1.15 | 15% above typical | 509 |
| 2-5 | 10,243 | 3,601 | 0.82 | 18% below typical | 463 |
| 6-20 | 4,349 | 1,908 | 0.64 | 36% below typical | 562 |
| 21+ | 1,605 | 695 | 0.78 | 22% below typical | 1,065 |

One unit draws more crowd than its price tag suggests, and six or more draw less. For a fixed budget, one Prize worth wanting came with more Entrants than the same money split across several. Many units still fit sampling, digital Prizes and community goals, where the unit count is the point.

The raw Entrants column runs the other way, and the difference matters. Raw crowd rises with unit count, from 509 at one unit to 1,065 at twenty one or more, so campaigns giving away many things drew more people. Hold the money constant and the order reverses, because those campaigns also spent more. Quote the raw Entrant counts when the question is what campaigns looked like, and crowd per Prize dollar when the question is what a fixed budget bought. [Extracted from `analysis/output/context_checks.json`, `winner_count_index_value_adjusted`.] The crowd-per-Prize-dollar column is those same campaigns with the money held constant. Quote the raw Entrant counts when the question is what campaigns looked like, and crowd per Prize dollar when the question is where to put a fixed budget.

### Top fifth against bottom fifth

Campaigns behind these numbers split into fifths by Entrant count. Typical figures for the top and bottom fifth:

| | Top fifth | Bottom fifth |
|---|---|---|
| Entrants | 3,349 | 140 |
| Impressions | 14,063 | 550 |
| Conversion Rate | 27.7% | 25.5% |
| Stated Prize pool, USD | 1,200 | 120 |
| Winners | 1 | 1 |
| Entry Methods | 7 | 6 |
| Business's previous campaigns | 12 | 7 |
| Campaigns | 23,425 | 23,425 |
| Businesses | 4,602 | 7,829 |

Twenty five times the Impressions at a Conversion Rate two points apart. Reach separates the top from the bottom far more than anything else in the table. Two things that used to read as level no longer do: the top fifth's businesses have run 12 previous campaigns against 7, and its stated Prize pool is ten times the bottom's at 1,200 USD against 120. The bottom fifth is also spread across more businesses, 7,829 against 4,602, which is the concentration effect showing up again: the top is fewer accounts running more campaigns. None of this says a bigger Prize or more experience produced the Entrants. [Extracted from `analysis/output/context_checks.json`, `top_vs_bottom_quintile`, 23,425 campaigns each side.]

## Region and language

Region is the top-level domain of the business's site, so a .com business in Manchester reads as global. Language is a word-pattern count on the description and title. Figures are typical values on the campaigns we can compare fairly, the 10,719 campaigns with no repeatable action and a run of 14 days or less, which is the cut that makes Impressions comparable between campaigns. A row below the five-business floor goes unpublished, which is why the Nordic advent-calendar rows seen in earlier cuts of this export no longer appear here.

<!-- generated:ev_region -->
| Business domain | Campaigns | Entrants | Conversion Rate | Actions per Entrant |
|---|---|---|---|---|
| global domain (.com, .io, .net and so on) | 99,919 | 488 | 26% | 4.45 |
| United Kingdom | 4,572 | 468 | 36% | 3.82 |
| other or none | 4,222 | 412 | 26% | 4.75 |
| Australia | 3,030 | 566 | 32% | 3.24 |
| Brazil | 1,231 | 1,076 | 54% | 4.70 |
| Germany | 789 | 773 | 31% | 4.86 |
| Sweden | 677 | 663 | 75% | 3.87 |
| Canada | 612 | 612 | 23% | 3.26 |
| South Africa | 301 | 432 | 22% | 4.47 |
| Finland | 232 | 9,018 | 77% | 1.00 |
| Belgium | 222 | 296 | 35% | 5.65 |
| France | 207 | 224 | 20% | 3.98 |
| Netherlands | 196 | 374 | 31% | 4.05 |
| Spain | 165 | 381 | 24% | 5.02 |
| Japan | 143 | 280 | 29% | 3.73 |
<!-- /generated -->

Brazil has twice the Conversion Rate of the global-domain rate, 54% against 26%.

<!-- generated:ev_language -->
| Language guess | Campaigns | Entrants | Conversion Rate | Actions per Entrant |
|---|---|---|---|---|
| English or unknown | 108,830 | 490 | 27% | 4.4 |
| Indonesian | 2,480 | 556 | 24% | 4.9 |
| Spanish | 1,890 | 465 | 29% | 4.9 |
| Portuguese | 1,820 | 1,000 | 51% | 4.8 |
| French | 1,113 | 301 | 27% | 4.1 |
| German | 521 | 339 | 25% | 4.3 |
| Dutch | 185 | 267 | 34% | 6.1 |
| Turkish | 185 | 581 | 32% | 2.9 |
| Italian | 104 | 450 | 15% | 4.5 |
<!-- /generated -->

### Prize currency by country

Among Prize listings that state a currency, how often that currency is the business's own against USD. This cut uses the same 100-Entrant floor as the benchmarks above.

| Country | Campaigns | Businesses | Home-currency share | USD share |
|---|---|---|---|---|
| United States | 29,990 | 5,917 | 100% | 100% |
| United Kingdom | 4,458 | 792 | 1% | 99% |
| Japan | 3,169 | 152 | 0% | 100% |
| India | 1,640 | 402 | 0% | 100% |
| Australia | 2,095 | 684 | 1% | 99% |
| Brazil | 839 | 128 | 0% | 100% |
| South Korea | 799 | 208 | 0% | 100% |
| Germany | 797 | 231 | 0% | 100% |

Outside the United States, the business's own currency appears on under 1% of stated Prize values in every country in this cut, and USD covers over 99% of stated values everywhere outside the US. A stated value from a Japanese or Brazilian business is a USD figure the business typed, not a local price converted to dollars. Price a Prize in the business's own currency when quoting it to Entrants, and treat every stated USD value in this dataset as USD-shaped regardless of where the campaign ran.

Source: `analysis/output/indicators.json` (prize_currency_localisation_by_country).

### Description wording

Flags found by text pattern in the Prize description, in the campaigns we can compare fairly. Descriptions that state the value go with a lower Conversion Rate, and descriptions that state the Winner count go with fewer Entrants. A no-purchase line goes with more Entrants, and the table carries no Conversion Rate for either of those two flags. Nothing here says the wording moved a number.

| Flag | Share of descriptions | Present (Conversion Rate / Entrants / campaigns) | Absent (Conversion Rate / Entrants / campaigns) |
|---|---|---|---|
| States the value | 26% | 33% / 2,101 / 2,130 | 39% / 2,121 / 8,589 |
| States the Winner count | 5% | — / 1,864 / 429 | — / 2,127 / 10,290 |
| No-purchase line | 6% | — / 2,405 / 287 | — / 2,109 / 10,432 |
| Worldwide mentioned | 4% | - | - |
| US only mentioned | 2% | - | - |
| Age line included | 2% | - | - |

## What the data cannot support

- **Cause and effect.** Every campaign reached at least 100 Entrants, and there is no set of smaller or failed campaigns to compare against. The campaign-size groups compare selected samples with each other, which shows who ran what and nothing about what a Prize did. Nothing here shows that a Prize type produced participation.
- **Entrant volume promises.** No Prize "guarantees" a number of Entrants. Volume depends on promotion, audience size, entry friction and timing, none of which the Prize controls.
- **Business outcomes.** Sales, lead quality, retention and profitability are absent from the dataset.
- **Cost.** Values are stated retail values entered by businesses, often rounded, sometimes totals, occasionally wrong by orders of magnitude. What the business actually paid is unknown.
- **Winners.** Quantity is the number of units listed and may differ from the number of Winners actually awarded.
- **Currency merging.** Values were never converted. USD and EUR are reported separately, and parsed "$" values are flagged as ambiguous.
- **Current platform features.** Entry-method types in the dataset are history. Current capability lives in each platform's own documentation.

## Classification limits

- Prize categories come from name-pattern rules plus a private AI-assisted label pass on the names the rules missed. 6.7% remain unclassified and 6.0% are placeholders ("1st Prize", or a campaign title reused as the Prize name). Label-pass categories are an AI model's inference over business-typed text in many languages, spot-checked but not systematically measured for accuracy.
- The own-product flag is a word-overlap heuristic with both false positives and false negatives.
- Crypto detection is conservative on purpose. The ambiguous campaigns probably include some regular giveaways and some crypto ones [1,251 of them]. The label pass caught token names the rules had missed, but non-English crypto campaigns (an Arabic-language token airdrop, an NFT platform's mystery box) were seen among the campaigns behind these numbers during spot checks, so a small residual remains.

Categorization draws on 49,511 listings from name-pattern rules plus 8,553 more from the label pass after dropping low-confidence labels. Rules alone would leave about 21% unclassified.

## Company profile data (thin)

Apollo organization matches cover about a seventh of the businesses in the source count [3,609 of 25,482].

Industry and country cuts on this match (`by_apollo_industry`, `by_apollo_country`) carry many thin cells. Quote nothing from either cut without its campaign count and business count next to it.

| Cut | Cells under 10 businesses |
|---|---|
| Industry (`by_apollo_industry`) | 13 of 51 |
| Country (`by_apollo_country`) | 2 of 31 |

## Text safety

Descriptions contained URLs in 5,069 campaigns, HTML in 17, and phrases addressed to an AI in 14. All were treated as data. Nothing was fetched, executed or followed, and no example reproduces a link.

## Impressions and Conversion Rate

Conversion Rate means Entrants per Impression: the share of unique daily Impressions of the entry page that became a unique Entrant.

Verified from the platform's reporting terms page on 9 September 2026: Impressions count one view per user per 24 hours, an Action is one Entry Method completed, Entries are Actions completed times Entry Worth, Users are unique Entrants, and the platform quotes an average Conversion Rate of about 34%. The dataset's valid Entrants are Users, valid entries are Entries, and Entry Worth is absent, so Actions per Entrant mixes how many Actions people did with how much each was worth.

Impressions in the dataset are unique per day, so a visitor who returns counts again each day. Repeatable actions (daily bonus, loyalty, timed bonus) and long runs raise Impressions per Entrant and lower Conversion Rate, without any change in who entered. The campaigns we can compare fairly excludes campaigns with a repeatable action and any run over 14 days. Typical figures, across the campaigns behind these numbers, descriptive only. The comparisons that depend on this rate live in the entry-method planner and timing references, all computed on the campaigns we can compare fairly by the analysis behind it.

<!-- generated:cmp_vertical -->
| Vertical, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| music_media | 7,047 | 365 | 4.01 | 36% | 2.8 | 6 |
| gaming | 10,161 | 383 (+5%) | 4.17 (+4%) | 35% (-4%) | 2.9 | 6 |
| unclassified | 6,861 | 406 (+11%) | 3.88 (-3%) | 33% (-8%) | 3.0 | 6 |
| technology | 5,742 | 816 (+124%) | 4.16 (+4%) | 40% (+11%) | 2.5 | 6 |
| fitness_outdoor | 2,010 | 429 (+18%) | 3.05 (-24%) | 31% (-15%) | 3.3 | 5 |
| kids_family_pets | 1,909 | 366 (+0%) | 3.15 (-21%) | 29% (-19%) | 3.4 | 4 |
| fashion_beauty | 2,443 | 832 (+128%) | 2.44 (-39%) | 34% (-6%) | 2.9 | 4 |
| food_drink | 1,178 | 686 (+88%) | 2.95 (-27%) | 35% (-4%) | 2.9 | 5 |
| travel_events | 803 | 452 (+24%) | 3.00 (-25%) | 34% (-6%) | 2.9 | 6 |
| home | 1,078 | 744 (+104%) | 3.22 (-20%) | 35% (-4%) | 2.9 | 5 |
| software | 578 | 424 (+16%) | 4.30 (+7%) | 31% (-15%) | 3.3 | 6 |
<!-- /generated -->

Industries here fold each business's homepage-label category into the ten names this skill uses throughout. Gaming is gaming_esports, technology is electronics_tech, and so on, see `references/roi-benchmarks.md` for the full mapping. Fashion and beauty campaigns draw the most Entrants in this cut and run the lowest Actions per Entrant at 2.44, and technology has the highest Conversion Rate. Use them as context for a customer's expectations, never as targets.
