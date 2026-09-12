# Evidence and limitations

## The source

A private dataset of 144,878 campaigns from one giveaway platform, each with at least 100 valid (unique) Entrants. Fields: Entrant, entry and Impressions (views of the campaign page) counts, dates and duration, nested Prize records (name, value, currency, quantity, position), the campaign's public title and description, Entry Methods with counts, plan tier, and organizer contact details. Organizer details, ids, links and raw text are never reproduced in this repository.

The benchmarks below describe the 116,499 of those campaigns left after removing crypto, purchase-only and finance_crypto organizers.

<!-- generated:ev2_size_share -->
| Entrant count | Share of the 116,499 campaigns |
|---|---|
| 100 to 250 | 28% |
| 250 to 500 | 22% |
| 500 to 1,000 | 19% |
| 1,000 to 2,500 | 17% |
| 2,500 to 10,000 | 11% |
| Above 10,000 | 3% |
<!-- /generated -->

The repository summary quotes a count of entry actions. That total is not a field in the dataset and no analysis file carries it. It is the sum of the per-family action counts in the action families table in giveaway-entry-method-planner, the column headed n with uptake. Each one is an entry action offered in one of the campaigns behind these numbers, for which the dataset recorded how many Entrants took it.

<!-- generated:ev2_action_families -->
| Action family | Actions with an uptake figure |
|---|---|
| Visit a page or profile | 374,795 |
| Follow or subscribe (free) | 172,265 |
| Share, repost or refer | 80,835 |
| Bonus, loyalty or code | 64,343 |
| Custom action (other) | 52,187 |
| Email or newsletter signup | 49,466 |
| Engage with a post | 36,381 |
| Join a community | 31,662 |
| Answer a question or poll | 31,180 |
| Post or create content | 26,035 |
| Connect an account to enter | 24,076 |
| Paid subscription | 8,404 |
| Download or play | 4,347 |
| Imported or offline entries | 1,387 |

That sums to 957,363, rounded to 957,000.
<!-- /generated -->

The dataset's core counts are verified directly. Only USD has enough stated values to support any distribution, the rest are too thin to use. A few stated values are data-entry errors and are treated as such, never corrected.

The table below counts every campaign that cleared the 100-Entrant floor, before the crypto, ambiguous and purchase-opportunity segments are set aside. It is therefore larger than the 116,499 campaigns and 170,599 Prize records every benchmark on this page describes. Quote a row here only to say what the raw data holds. Within the benchmark population the share of Prize records carrying a stated value is 37.9%.

<!-- generated:ev_dataset -->
| Field | Value |
|---|---|
| Campaigns | 144,878 |
| Prize records | 211,916 |
| Businesses | 22,273 |
| Prize value missing | 60.6% of Prize records (126,889 null, 1,620 zero) |
| Stated-value currencies | USD 84,990, GBP 38, EUR 38, AUD 22, CAD 21, plus a handful of others |
| Campaign start years | 2015 to 2026, 66% between 2021 and 2023 |
| Missing fields | 245 campaigns with no entry count, 15,702 with no description |
| Data-entry errors | negative values, and a stated value of 250 million |
<!-- /generated -->

## Segmenting before any benchmark

<!-- generated:segments -->
| Segment | Campaigns | Handling |
|---|---|---|
| Ordinary | 116,499 (170,599 prize records, 17,633 organizers) | Basis for every default figure |
| Crypto | 3,467 | Excluded. Described only when a user asks for crypto advice. 40% used a wallet-address entry method |
| Purchase opportunity | 259 | Excluded. The prize is the right to buy something |

Excluded campaigns are similar in size to ordinary ones (crypto median 580 contestants versus 492 ordinary), so exclusion changes who is in the benchmark and leaves the size distribution alone.
<!-- /generated -->

The crypto rule combines Prize names, campaign names, descriptions and Entry Method types. A single weak keyword never decides. Excluding crypto changes who is in the benchmark and leaves campaign size where it was: crypto typical 732 Entrants versus 492 for the rest. Any claim that crypto inflated participation figures is a hypothesis.

A homepage-label industry cut on the campaign analysis confirms the exclusion is not a small correction: finance and crypto is the largest single industry by campaign count, ahead of gaming and esports. See `references/roi-benchmarks.md` for the table this cut produced.

## What the campaigns behind these numbers show

Two shorthands run through the tables below. The middle half is the middle half of campaigns, running from the lower quarter to the upper quarter. The top-tenth mark is the level nine campaigns in ten sit below, so it marks the top tenth without naming an extreme.

<!-- generated:benchmark -->
| Measure | Value | n or note |
|---|---|---|
| Valid contestants | median 492, IQR 225 to 1,290, 90th pct 3,334 | 116,499. Floor is 101 by selection |
| Valid entries | median 2,322 | 116,283. Entries count actions, and one person makes many |
| Entries per contestant | median 4.38, IQR 2.74 to 7.06 | 116,283 |
| Impressions | median 2,033 | 116,119 with a non-zero value. Zeros treated as unknown |
| Duration | median 14 days, IQR 7 to 29 | 115,754. Maximum 365 days (evergreen campaigns) |
| One prize record | 82.6% of campaigns | quantity may still exceed 1 |
| Any quantity above 1 | 31.5% of campaigns | units listed, which may differ from Winners |
| Prize value stated | 37.9% of prize records | 62.1% unknown |
| Stated USD values | median 125, IQR 50 to 425, 90th pct 1,199 | 64,579 records. Max 1,000,000 |
| Stated EUR values | median 75, IQR 39 to 332, 90th pct 2,200 | 35 records. Max 9,100 |
| Stated GBP values | median 62, IQR 25 to 400, 90th pct 450 | 34 records. Max 1,200 |
| Stated CAD values | median 545, IQR 200 to 2,180, 90th pct 4,500 | 21 records. Too few to use. Max 35,000 |
| Stated AUD values | median 600, IQR 129 to 3,600, 90th pct 6,000 | 18 records. Too few to use. Max 60,000 |
| Fully valued campaign totals (USD) | median 299, IQR 90 to 1,000 | 42,892 campaigns. Max 10,000,000 |
| Repeat organizers | 3,795 organizers with 5+ campaigns account for 81.5% of campaigns | patterns can reflect prolific accounts |
| Plan tier | Business 29,645, Pro 62,061, Not Available 5, Premium 1,993, Hobby 10,802, Free 11,993 | tier at export time |
<!-- /generated -->

## By campaign size

Every size group is still a selected sample with a floor, and bigger campaigns come from bigger businesses with bigger budgets, so differences between size groups describe who runs what. They do not show that a Prize made a campaign larger.

<!-- generated:bands -->
| Band (valid contestants) | Campaigns | Organizers | Value stated | Stated USD median (n) | Campaign total USD median (n) | One prize record | Entries per contestant | Duration median |
|---|---|---|---|---|---|---|---|---|
| 100-250 | 33,074 | 9,533 | 36% | 69 (16,280) | 120 (11,662) | 85% | 4.09 | 12 days |
| 250-500 | 25,681 | 6,496 | 38% | 80 (13,221) | 147 (9,416) | 85% | 4.6 | 14 days |
| 500-1k | 21,838 | 5,509 | 37% | 120 (11,474) | 259 (7,812) | 82% | 4.68 | 14 days |
| 1k-2.5k | 20,021 | 5,077 | 40% | 210 (12,278) | 530 (7,761) | 79% | 4.32 | 15 days |
| 2.5k-10k | 12,714 | 2,991 | 42% | 379 (9,229) | 1,299 (5,111) | 78% | 4.38 | 18 days |
| 10k+ | 3,171 | 748 | 37% | 799 (2,097) | 3,000 (1,130) | 80% | 4.37 | 18 days |

Primary prize category (first prize record) by band, share of campaigns:

| Category | 100-250 | 250-500 | 500-1k | 1k-2.5k | 2.5k-10k | 10k+ |
|---|---|---|---|---|---|---|
| Tech hardware | 10.9% | 12.6% | 16.9% | 23.6% | 29.9% | 36.8% |
| Gift card or cash | 16.5% | 22.4% | 18.1% | 14.6% | 13.1% | 11.3% |
| Bundle or box | 9.4% | 10.5% | 10.7% | 9.4% | 8.1% | 4.6% |
| Experience, travel, tickets | 6.3% | 4.5% | 3.8% | 4.1% | 5.1% | 5.0% |
| Game items or skins | 12.1% | 8.8% | 8.2% | 6.5% | 5.3% | 5.0% |
| Merch, apparel, collectibles | 3.7% | 3.5% | 3.3% | 2.8% | 3.6% | 4.4% |
| Home, garden, appliance | 1.1% | 1.4% | 2.0% | 2.6% | 2.9% | 1.3% |
| Regulated goods (firearms) | 0.3% | 0.5% | 0.8% | 1.7% | 2.8% | 9.1% |
| Sports and outdoor gear | 0.6% | 0.7% | 0.9% | 1.3% | 1.3% | 0.6% |
| Food, drink, consumables | 0.8% | 1.0% | 1.1% | 1.4% | 1.0% | 0.3% |
| Subscription or membership | 1.2% | 1.0% | 1.0% | 0.9% | 0.6% | 0.3% |
| Discount or coupon | 0.6% | 0.3% | 0.4% | 0.6% | 0.3% | 0.1% |
<!-- /generated -->

## Plan tier, extended

The plan tier row above comes from the campaigns at large. A cut on the same field, restricted to campaigns with a labelled site, breaks format and Conversion Rate out by tier. It counts more campaigns than the 116,499 the benchmarks describe, because it runs before the segment exclusions. Free and Hobby convert best and neither offers an email action. Premium runs longest and offers the most Entry Methods, and converts worst. Business and Pro sit in the middle on every measure.

<!-- generated:ev2_tier_extended -->
| Tier | Conversion Rate | Campaigns | Businesses | Days | Entry Methods | Email offered |
|---|---|---|---|---|---|---|
| Free | 34% | 13,210 | 4,829 | 12 | 4 | 0% |
| Hobby | 32% | 11,949 | 2,909 | 11 | 6 | 0% |
| Pro | 27% | 76,448 | 12,916 | 13 | 8 | 32% |
| Business | 26% | 39,724 | 4,878 | 12 | 7 | 35% |
| Premium | 24% | 2,521 | 393 | 20 | 9 | 50% |
<!-- /generated -->

## Business scale

Homepage labels also split businesses into listed and private companies. Private businesses run shorter campaigns with a higher referral rate, listed businesses run longer campaigns with a lower one. Revenue cuts inside this data, matched against Fortune-500-like companies, are too thin for anything but advice [6 to 48 businesses per group, two of the four groups at ten or fewer].

<!-- generated:ev2_public_company -->
| Business type | Duration | Referrals % of Entrants | Campaigns | Businesses |
|---|---|---|---|---|
| Private | 12 days | 15.6 | 76,732 | 3,963 |
| Listed | 14 days | 14.0 | 4,191 | 160 |
<!-- /generated -->

## Repeat businesses

Campaign sequence tracks how many campaigns a business had already run. Conversion Rate rises and duration shrinks the more campaigns a business has already run. Recency does not explain it, since businesses active in the last 12 months convert about the same as inactive ones (28% against 27%). The likelier explanation is who kept going: businesses whose early campaigns worked well enough are the ones who keep running them.

<!-- generated:ev_sequence -->
| Campaign sequence | Conversion Rate | Duration | Campaigns | Businesses |
|---|---|---|---|---|
| First campaign | 26% | 16 days | 17,633 | 17,633 |
| Eleventh or later | 27% | 14 days | 63,192 | 1,877 |
<!-- /generated -->

## Inferred Prize values from text

To reduce the 61% gap we parsed explicit amounts from Prize names ("$4,000 RTX PC"), from "worth / valued at / MSRP" phrases in descriptions, and from campaign titles of single-Prize campaigns. Validation against listings that carried both a stated and a parsed value agreed within ±20% most of the time. Disagreements are mostly totals across several Prizes, marketing round numbers, or a cash component inside a larger bundle. The "$" symbol is recorded as "USD?" because it is ambiguous between USD, CAD, AUD and others, so parsed-only "$" values are kept separate from stated values and never used in a listing-level claim.

Coverage rises from 40.5% to 48.5% of listings.

<!-- generated:ev_parsing -->
| Parsing measure | Value |
|---|---|
| Listings with a parsed value | 30,590 (23,695 from Prize names, 2,743 from campaign titles, 4,152 from description phrases) |
| Listings gaining a value with none stated | 15,033 |
| Listings with both a stated and a parsed value | 14,112, agreeing within ±20% for 80% |
| Parsed-only "$" values | 9,624 listings, typical 120, middle half 50 to 500, max 2.4 million (a campaign-wide total an organizer typed into one Prize listing) |
<!-- /generated -->

Parsed values are what organizers wrote, never what they paid.

Category typical figures for stated values are given in the taxonomy as reference ranges. We do not fill missing listings with them.

## Prize value, adjusted

A  field cut confirms the coverage gap holds at scale: 38.8% of Prize listings carry a stated value, and 99.9% of those are USD. Every typical figure below rests on that self-selected minority.

Campaigns whose every Prize carried a stated USD value: 42,953, from 9,089 businesses. Prize cost per Entrant is the stated pool divided by Entrants, and stated value is what the organizer wrote, which need not be what they paid.

<!-- generated:ev_value_bands -->
| Stated pool, USD | Campaigns | Entrants | Entries per Entrant | Stated USD per Entrant |
|---|---|---|---|---|
| under 50 | 6,063 | 266 | 6.05 | 0.07 |
| 50-99 | 5,213 | 320 | 5.89 | 0.19 |
| 100-249 | 8,573 | 403 | 4.42 | 0.37 |
| 250-499 | 6,146 | 618 | 4.38 | 0.55 |
| 500-999 | 5,839 | 849 | 4.38 | 0.77 |
| 1000-2499 | 6,428 | 1,307 | 4.39 | 1.10 |
| 2500-4999 | 2,763 | 2,107 | 4.95 | 1.58 |
| 5000-9999 | 1,099 | 2,152 | 4.32 | 2.90 |
| 10000-24999 | 553 | 1,521 | 4.49 | 9.36 |
| 25000-49999 | 130 | 1,830 | 3.63 | 17.76 |
| 50000+ | 146 | 1,128 | 4.27 | 114.55 |
<!-- /generated -->

Prize value and Entrant count move together only loosely: ten times the Prize value comes with about 2.2 times the Entrants, and value accounts for about 23% of the variation in Entrant counts [the `value_regression` cut in `context_checks.json`, 42,953 campaigns from 9,089 businesses]. The table above rises through the middle bands and falls back at the largest pools.

Most campaigns spend little: 77% of these campaigns used a pool of 1,000 USD or less, and 46% under 250 USD.

### Prize pool by industry, business type, tier and category

Stated USD Prize pool for campaigns with a full value, cut four ways across the campaigns behind these numbers. Share is that cut's campaign count against the same group's total campaign count, so it is the share of campaigns in the group that stated a value, not a share of Prize listings. State it beside every typical figure here, coverage runs from 14% to 64% and a thin-coverage figure describes a self-selected subset. Stated USD per Entrant is the stated pool divided by Entrants, as in the table above.

By industry:

<!-- generated:ev2_pool_industry -->
| Industry | Campaigns with a value | Share with value | Typical pool USD | Middle half | Stated USD per Entrant |
|---|---|---|---|---|---|
| Media and entertainment | 9,030 | 42% | 70 | 25 to 300 | 0.16 |
| Gaming and esports | 7,732 | 32% | 200 | 70 to 740 | 0.42 |
| Electronics and tech | 5,167 | 33% | 549 | 199 to 1,599 | 0.61 |
| Sports and outdoors | 2,366 | 51% | 641 | 300 to 1,798 | 0.66 |
| Food and drink | 2,042 | 44% | 438 | 175 to 1,222 | 0.50 |
| Home and garden | 1,989 | 54% | 500 | 200 to 1,450 | 0.48 |
| Apparel and fashion | 1,556 | 34% | 531 | 200 to 1,531 | 0.54 |
| Toys, hobbies, collectibles | 1,441 | 31% | 200 | 99 to 500 | 0.49 |
| Travel and events | 1,282 | 32% | 600 | 254 to 1,500 | 0.87 |
| Automotive | 1,276 | 55% | 999 | 361 to 2,500 | 0.51 |
<!-- /generated -->

By business type:

<!-- generated:ev2_pool_btype -->
| Business type | Campaigns with a value | Share with value | Typical pool USD | Middle half | Stated USD per Entrant |
|---|---|---|---|---|---|
| Brand | 12,407 | 41% | 500 | 200 to 1,487 | 0.63 |
| Media or publisher | 8,517 | 43% | 70 | 25 to 320 | 0.18 |
| Retailer | 8,050 | 37% | 300 | 120 to 1,000 | 0.42 |
| Creator | 5,359 | 30% | 120 | 50 to 499 | 0.33 |
| Software | 3,896 | 40% | 500 | 200 to 1,700 | 0.50 |
| Other | 2,286 | 37% | 250 | 100 to 800 | 0.56 |
| Service business | 1,205 | 32% | 500 | 200 to 1,396 | 1.06 |
| Agency | 868 | 30% | 568 | 180 to 1,688 | 0.73 |
| Community | 753 | 28% | 300 | 100 to 627 | 0.54 |
| Nonprofit | 382 | 40% | 600 | 309 to 1,944 | 1.14 |
<!-- /generated -->

By plan tier:

<!-- generated:ev2_pool_tier -->
| Tier | Campaigns with a value | Share with value | Typical pool USD | Middle half | Stated USD per Entrant |
|---|---|---|---|---|---|
| Pro | 24,491 | 40% | 299 | 100 to 819 | 0.42 |
| Business | 11,227 | 38% | 700 | 175 to 2,000 | 0.56 |
| Free | 3,936 | 33% | 60 | 25 to 168 | 0.25 |
| Hobby | 3,527 | 33% | 149 | 70 to 399 | 0.41 |
| Premium | 771 | 39% | 1,499 | 244 to 4,000 | 0.21 |
<!-- /generated -->

By Prize category:

<!-- generated:ev2_pool_category -->
| Category | Campaigns with a value | Share with value | Typical pool USD | Middle half | Stated USD per Entrant |
|---|---|---|---|---|---|
| Gift card or cash | 10,573 | 52% | 100 | 45 to 500 | 0.25 |
| Unclassified | 9,563 | 34% | 299 | 99 to 916 | 0.47 |
| Tech hardware | 7,294 | 36% | 500 | 200 to 1,500 | 0.43 |
| Bundle or box | 4,459 | 40% | 300 | 100 to 869 | 0.50 |
| Game items or skins | 3,486 | 34% | 150 | 60 to 500 | 0.38 |
| Experience, travel, tickets | 1,578 | 28% | 800 | 300 to 2,400 | 1.24 |
| Merch, apparel, collectibles | 1,198 | 30% | 150 | 50 to 571 | 0.36 |
| Placeholder name | 1,010 | 21% | 570 | 170 to 2,100 | 0.58 |
| Regulated goods (firearms) | 891 | 64% | 1,460 | 649 to 3,200 | 0.45 |
| Home, garden, appliance | 861 | 41% | 365 | 143 to 873 | 0.36 |
| Sports and outdoor gear | 554 | 54% | 552 | 230 to 1,599 | 0.65 |
| Subscription or membership | 509 | 45% | 575 | 160 to 1,500 | 1.09 |
| Food, drink, consumables | 431 | 37% | 300 | 100 to 800 | 0.42 |
| Vehicle | 350 | 60% | 1,141 | 479 to 2,596 | 1.11 |
| Beauty and wellness | 312 | 48% | 200 | 70 to 500 | 0.34 |
| Toys and collectibles | 298 | 14% | 100 | 41 to 200 | 0.26 |
| Tools, craft, DIY | 204 | 44% | 350 | 150 to 1,199 | 0.43 |
| Music gear | 168 | 42% | 808 | 341 to 1,624 | 0.47 |
| Exclusive access | 93 | 21% | 377 | 150 to 1,750 | 0.91 |
| Discount or coupon | 85 | 16% | 300 | 50 to 750 | 0.84 |
<!-- /generated -->

Regulated goods and vehicle Prizes state a value most often (64% and 60%), consistent with retailers who already price these items for sale. Experience, travel and tickets carries the highest stated USD per Entrant of any cut here, 1.24 USD.

Toys and collectibles states a value least often, so its typical pool describes a small, self-selected group [14% of the category, 298 valued campaigns from 159 businesses].

Premium-tier campaigns post the highest typical pool and the lowest stated USD per Entrant of any tier, because their crowds are the largest. Free campaigns post the lowest typical pool.

Source: `analysis/output/prize_timing_cuts.json` (prize_pool_by_industry, prize_pool_by_business_type, prize_pool_by_tier, prize_pool_by_category).

### Crowd per Prize dollar, by Prize category

Each campaign's Entrants divided by the typical Entrants for other campaigns at the same stated Prize cost, then the typical of that ratio per category. That ratio is crowd per Prize dollar: how much crowd a category draws once you strip out how much was spent. 1.00 means typical for the money, above 1.00 means the category draws more crowd than its price tag suggests, and below 1.00 means less. Categories with at least 100 valued campaigns.

<!-- generated:ev_crowd_category -->
| Category | Campaigns | Entrants | Crowd per Prize dollar | For the money |
|---|---|---|---|---|
| Regulated goods (firearms) | 1,510 | 2,133 | 2.07 | 107% above typical |
| Music gear | 447 | 1,290 | 1.93 | 93% above typical |
| Tech hardware | 22,019 | 898 | 1.42 | 42% above typical |
| Home, garden, appliance | 2,534 | 828 | 1.34 | 34% above typical |
| Tools, craft, DIY | 613 | 910 | 1.15 | 15% above typical |
| Beauty and wellness | 727 | 483 | 1.14 | 14% above typical |
| Food, drink, consumables | 1,358 | 657 | 1.10 | 10% above typical |
| Gift card or cash | 22,598 | 450 | 1.07 | 7% above typical |
| Sports and outdoor gear | 1,303 | 784 | 1.05 | 5% above typical |
| Placeholder name | 5,021 | 484 | 0.98 | typical |
| Vehicle | 662 | 798 | 0.98 | typical |
| Art and custom | 178 | 404 | 0.95 | 5% below typical |
| Bundle or box | 12,782 | 496 | 0.89 | 11% below typical |
| Toys and collectibles | 2,267 | 420 | 0.86 | 14% below typical |
| Unclassified | 31,353 | 434 | 0.83 | 17% below typical |
| Merch, apparel, collectibles | 5,257 | 479 | 0.78 | 22% below typical |
| Game items or skins | 11,218 | 365 | 0.73 | 27% below typical |
| Discount or coupon | 1,046 | 732 | 0.73 | 27% below typical |
| Exclusive access | 520 | 376 | 0.61 | 39% below typical |
| Experience, travel, tickets | 6,049 | 390 | 0.60 | 40% below typical |
| Subscription or membership | 1,559 | 423 | 0.51 | 49% below typical |
<!-- /generated -->

Gaming PCs and GPUs draw far more crowd than their price tag suggests, consoles draw more too, phones and peripherals draw about what their price tag suggests. Cash and gift cards draw a little more than their price tag suggests at 1.07, broadly wanted and close to what the money buys. This agrees with Gleam's internal analysis of the same export, which found the same ordering with a wider spread.

### Crowd per Prize dollar, by number of Prize units

<!-- generated:ev2_units -->
| Prize units | Campaigns | Businesses | Crowd per Prize dollar | For the money | Entrants |
|---|---|---|---|---|---|
| 1 | 26,919 | 5,664 | 1.15 | 15% above typical | 509 |
| 2-5 | 10,192 | 3,568 | 0.82 | 18% below typical | 463 |
| 6-20 | 4,276 | 1,866 | 0.64 | 36% below typical | 565 |
| 21+ | 1,566 | 670 | 0.77 | 23% below typical | 1,065 |
<!-- /generated -->

One unit draws more crowd than its price tag suggests, and six or more draw less. For a fixed budget, one Prize worth wanting came with more Entrants than the same money split across several. Many units still fit sampling, digital Prizes and community goals, where the unit count is the point.

The raw Entrants column runs the other way, and the difference matters. Raw crowd rises with unit count, from 509 at one unit to 1,065 at twenty one or more, so campaigns giving away many things drew more people. Hold the money constant and the order reverses, because those campaigns also spent more. Quote the raw Entrant counts when the question is what campaigns looked like, and crowd per Prize dollar when the question is what a fixed budget bought. [Extracted from `analysis/output/context_checks.json`, `winner_count_index_value_adjusted`.] The crowd-per-Prize-dollar column is those same campaigns with the money held constant. Quote the raw Entrant counts when the question is what campaigns looked like, and crowd per Prize dollar when the question is where to put a fixed budget.

### Top fifth against bottom fifth

Campaigns behind these numbers split into fifths by Entrant count. Typical figures for the top and bottom fifth:

<!-- generated:ev_quintile -->
|  | Top fifth | Bottom fifth |
|---|---|---|
| Entrants | 3,338 | 140 |
| Impressions | 14,070 | 552 |
| Conversion Rate | 27.6% | 25.4% |
| Stated Prize pool, USD | 1,200 | 120 |
| Winners | 1 | 1 |
| Entry Methods | 7 | 6 |
| Business's previous campaigns | 12 | 7 |
| Campaigns | 23,256 | 23,256 |
| Businesses | 4,543 | 7,763 |

Twenty five times the Impressions at a Conversion Rate two points apart. Reach separates the top from the bottom far more than anything else in the table. Two things that used to read as level no longer do: the top fifth's businesses have run 12 previous campaigns against 7, and its stated Prize pool is ten times the bottom's at 1,200 USD against 120. The bottom fifth is also spread across more businesses, 7,763 against 4,543, which is the concentration effect showing up again: the top is fewer accounts running more campaigns. None of this says a bigger Prize or more experience produced the Entrants. [Extracted from `analysis/output/context_checks.json`, `top_vs_bottom_quintile`, 23,256 campaigns each side.]
<!-- /generated -->

## Region and language

Region is the top-level domain of the business's site, so a .com business in Manchester reads as global. Language is a word-pattern count on the description and title. Figures are typical values on the campaigns we can compare fairly, the 39,462 campaigns with no repeatable action and a run of 14 days or less, which is the cut that makes Impressions comparable between campaigns. A row below the five-business floor goes unpublished, which is why the Nordic advent-calendar rows seen in earlier cuts of this export no longer appear here.

<!-- generated:ev_region -->
| Business domain | Campaigns | Entrants | Conversion Rate | Entries per Entrant |
|---|---|---|---|---|
| global domain (.com, .io, .net and so on) | 33,656 | 441 | 34% | 3.71 |
| other or none | 1,593 | 438 | 32% | 3.89 |
| United Kingdom | 991 | 397 | 39% | 2.66 |
| Australia | 908 | 550 | 33% | 2.77 |
| Brazil | 680 | 1,289 | 57% | 4.58 |
| Germany | 385 | 803 | 37% | 4.33 |
| Sweden | 345 | 836 | 75% | 3.54 |
| Finland | 184 | 9,799 | 82% | 1.00 |
| Belgium | 173 | 292 | 38% | 6.23 |
| Canada | 117 | 326 | 32% | 1.87 |
| South Africa | 66 | 240 | 35% | 4.59 |
| France | 65 | 162 | 30% | 3.92 |
| Poland | 50 | 462 | 44% | 5.52 |
<!-- /generated -->

Brazil has twice the Conversion Rate of the global-domain rate, 54% against 26%.

<!-- generated:ev_language -->
| Language guess | Campaigns | Entrants | Conversion Rate | Entries per Entrant |
|---|---|---|---|---|
| English or unknown | 108,016 | 491 | 27% | 4.4 |
| Indonesian | 2,455 | 555 | 23% | 4.9 |
| Spanish | 1,889 | 465 | 29% | 4.9 |
| Portuguese | 1,818 | 1,002 | 51% | 4.8 |
| French | 1,113 | 301 | 27% | 4.1 |
| German | 521 | 339 | 25% | 4.3 |
| Turkish | 185 | 581 | 32% | 2.9 |
| Dutch | 184 | 266 | 34% | 6.1 |
| Italian | 102 | 428 | 15% | 4.5 |
<!-- /generated -->

### Prize currency by country

Among Prize listings that state a currency, how often that currency is the business's own against USD. This cut uses the same 100-Entrant floor as the benchmarks above.

<!-- generated:ev2_currency_country -->
| Country | Campaigns | Businesses | Home-currency share | USD share |
|---|---|---|---|---|
| United States | 29,461 | 5,705 | 100% | 100% |
| United Kingdom | 4,285 | 708 | 1% | 99% |
| Japan | 2,652 | 110 | 0% | 100% |
| Australia | 1,965 | 641 | 1% | 99% |
| India | 1,256 | 291 | 0% | 100% |
| Brazil | 772 | 100 | 0% | 100% |
| Germany | 718 | 205 | 0% | 100% |
| South Korea | 480 | 150 | 0% | 100% |
<!-- /generated -->

Outside the United States, the business's own currency appears on under 1% of stated Prize values in every country in this cut, and USD covers at least 99% of stated values, to the nearest point, in every one of them. A stated value from a Japanese or Brazilian business is a USD figure the business typed, not a local price converted to dollars. Price a Prize in the business's own currency when quoting it to Entrants, and treat every stated USD value in this dataset as USD-shaped regardless of where the campaign ran.

Source: `analysis/output/indicators.json` (prize_currency_localisation_by_country).

### Description wording

Flags found by text pattern in the Prize description, in the campaigns we can compare fairly. Share of descriptions counts every campaign, the other columns count the campaigns we can compare fairly. Descriptions that state the value go with a lower Conversion Rate, and descriptions that state the Winner count go with fewer Entrants. A no-purchase line goes with more Entrants. Every flag goes with a lower Conversion Rate than its absence. Nothing here says the wording moved a number.

<!-- generated:ev2_wording -->
| Flag | Share of descriptions | Present (Conversion Rate / Entrants / campaigns) | Absent (Conversion Rate / Entrants / campaigns) |
|---|---|---|---|
| States the value | 23% | 32% / 522 / 6,913 | 35% / 438 / 32,549 |
| States the Winner count | 5% | 27% / 437 / 2,076 | 35% / 453 / 37,386 |
| No-purchase line | 3% | 31% / 547 / 964 | 35% / 450 / 38,498 |
| Worldwide mentioned | 4% | 29% / 462 / 1,044 | 35% / 452 / 38,418 |
| US only mentioned | 1% | 32% / 439 / 562 | 35% / 453 / 38,900 |
| Age line included | 1% | 25% / 583 / 555 | 35% / 450 / 38,907 |
<!-- /generated -->

## What the data cannot support

- **Cause and effect.** Every campaign reached at least 100 Entrants, and there is no set of smaller or failed campaigns to compare against. The campaign-size groups compare selected samples with each other, which shows who ran what and nothing about what a Prize did. Nothing here shows that a Prize type produced participation.
- **Entrant volume promises.** No Prize "guarantees" a number of Entrants. Volume depends on promotion, audience size, entry friction and timing, none of which the Prize controls.
- **Business outcomes.** Sales, lead quality, retention and profitability are absent from the dataset.
- **Cost.** Values are stated retail values entered by businesses, often rounded, sometimes totals, occasionally wrong by orders of magnitude. What the business actually paid is unknown.
- **Winners.** Quantity is the number of units listed and may differ from the number of Winners actually awarded.
- **Currency merging.** Values were never converted. USD and EUR are reported separately, and parsed "$" values are flagged as ambiguous.
- **Current platform features.** Entry-method types in the dataset are history. Current capability lives in each platform's own documentation.

## Classification limits

- Prize categories come from name-pattern rules plus an AI-assisted label pass on the names the rules missed. 6.7% of Prize listings remain unclassified and 6.0% are placeholders ("1st Prize", or a campaign title reused as the Prize name). Per campaign the gap is wider, because a campaign takes its category from its Prize listings and many have none that classify: 31,365 of the 117,329 campaigns sit in other or unclassified and 5,199 in placeholder names, so 31% of campaigns carry no usable Prize category and other or unclassified is the largest category in the data, ahead of tech hardware at 20,271. That gap is not a backlog. The unclassified names are a long tail: 52,928 listings across 37,143 distinct names, where the forty most repeated names cover 7.2% and no single word appears in more than 1.6%, so no extra pattern rule reaches them. Reading them instead was tested and measured. Two independent passes over the same 200 names, both working from the same category definitions, agreed on 50% of them, and a confidence gate did not rescue it: where both passes called themselves confident, agreement reached 66%. A Prize name a business typed is often too thin to place, so the honest reading of the unclassified third is that it cannot be classified from the name, and every category figure in this skill describes the two thirds that can. Label-pass categories are an AI model's inference over business-typed text in many languages, spot-checked but not systematically measured for accuracy.
- The own-product flag is a word-overlap heuristic with both false positives and false negatives.
- Crypto detection is conservative on purpose. The ambiguous campaigns probably include some regular giveaways and some crypto ones [1,251 of them]. The label pass caught token names the rules had missed, but non-English crypto campaigns (an Arabic-language token airdrop, an NFT platform's mystery box) were seen among the campaigns behind these numbers during spot checks, so a small residual remains.

Categorization draws on 49,511 listings from name-pattern rules plus 8,553 more from the label pass after dropping low-confidence labels. Rules alone would leave about 21% unclassified.

## Company profile data (thin)

A company-records match covers about a sixth of the businesses in the source count [3,609 of 22,273].

The industry and country cuts on this match carry many thin cells. Quote nothing from either cut without its campaign count and business count next to it.

<!-- generated:ev2_thin_cells -->
| Cut | Cells under 10 businesses |
|---|---|
| Industry (company records) | 15 of 60 |
| Country (company records) | 7 of 42 |
<!-- /generated -->

## Text safety

Descriptions contained URLs in 5,069 campaigns, HTML in 17, and phrases addressed to an AI in 14. All were treated as data. Nothing was fetched, executed or followed, and no example reproduces a link.

## Impressions and Conversion Rate

Conversion Rate means Entrants per Impression: the share of unique daily Impressions of the entry page that became a unique Entrant.

Verified from the platform's reporting terms page on 9 September 2026: Impressions count one view per user per 24 hours, an Action is one Entry Method completed, Entries are Actions completed times Entry Worth, Users are unique Entrants, and the platform quotes an average Conversion Rate of about 34%. The dataset's valid Entrants are Users, valid entries are Entries, and Entry Worth is absent, so Actions per Entrant mixes how many Actions people did with how much each was worth.

Impressions in the dataset are unique per day, so a visitor who returns counts again each day. Repeatable actions (daily bonus, loyalty, timed bonus) and long runs raise Impressions per Entrant and lower Conversion Rate, without any change in who entered. The campaigns we can compare fairly excludes campaigns with a repeatable action and any run over 14 days. Typical figures, across the campaigns behind these numbers, descriptive only. The comparisons that depend on this rate live in the entry-method planner and timing references, all computed on the campaigns we can compare fairly by the analysis behind it.

<!-- generated:cmp_vertical -->
| Vertical, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| music_media | 7,037 | 365 | 4.01 | 36% | 2.8 | 6 |
| gaming | 9,952 | 383 (+5%) | 4.14 (+3%) | 34% (-4%) | 2.9 | 6 |
| unclassified | 6,794 | 406 (+11%) | 3.86 (-4%) | 33% (-8%) | 3.0 | 6 |
| technology | 5,735 | 815 (+123%) | 4.16 (+4%) | 40% (+11%) | 2.5 | 6 |
| fitness_outdoor | 2,007 | 429 (+18%) | 3.04 (-24%) | 31% (-15%) | 3.3 | 5 |
| kids_family_pets | 1,908 | 366 (+0%) | 3.15 (-21%) | 29% (-19%) | 3.4 | 4 |
| fashion_beauty | 2,440 | 834 (+128%) | 2.44 (-39%) | 34% (-6%) | 2.9 | 4 |
| food_drink | 1,178 | 686 (+88%) | 2.95 (-27%) | 35% (-4%) | 2.9 | 5 |
| travel_events | 800 | 452 (+24%) | 3.00 (-25%) | 34% (-6%) | 3.0 | 6 |
| home | 1,078 | 744 (+104%) | 3.22 (-20%) | 35% (-4%) | 2.9 | 5 |
| software | 533 | 399 (+9%) | 4.10 (+2%) | 31% (-15%) | 3.3 | 6 |
<!-- /generated -->

Industries here fold each business's homepage-label category into the ten names this skill uses throughout. Gaming is gaming_esports, technology is electronics_tech, and so on, see `references/roi-benchmarks.md` for the full mapping. Fashion and beauty campaigns draw the most Entrants in this cut and run the lowest Actions per Entrant at 2.44, and technology has the highest Conversion Rate. Use them as context for a customer's expectations, never as targets.
