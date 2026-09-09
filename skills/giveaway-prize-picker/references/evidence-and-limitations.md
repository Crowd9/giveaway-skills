# Evidence and limitations

## The source

A private export of 54,675 campaigns from one giveaway platform, each with at least 1,000 valid (unique) contestants. Half sit between 1,000 and 2,500 contestants, 38% between 2,500 and 10,000, and 12% above 10,000. Fields: contestant, entry and impression counts, dates and duration, nested prize records (name, value, currency, quantity, position), the campaign's public title and description, entry methods with counts, plan tier, and organizer contact details. Organizer details, ids, links and raw text are never reproduced in this repository.

Verified counts: 54,675 campaigns, 85,326 prize records, 10,703 organizers, and prize value missing in 61.3% of prize records (51,461 null, 801 zero). Currencies on stated values: USD 33,818, then EUR 17, GBP 9, CAD 8, AUD 7 and a handful of others, so only USD supports any distribution. Campaign start years run 2013 to 2026, with 69% between 2021 and 2023. Sixty-nine campaigns have a null entry count and 5,157 have no description. A few stated values are data-entry errors (one negative, one of 50 million).

## Segmenting before any benchmark

<!-- generated:segments -->
| Segment | Campaigns | Handling |
|---|---|---|
| Ordinary | 37,180 (60,282 prize records, 6,817 organizers) | Basis for every default figure |
| Crypto | 16,150 | Excluded. Described only when a user asks for crypto advice. 40% used a wallet-address entry method |
| Ambiguous | 1,251 | Excluded and reported separately |
| Purchase opportunity | 94 | Excluded. The prize is the right to buy something |

Excluded campaigns are similar in size to ordinary ones (crypto median 3,339 contestants versus 2,201 ordinary), so exclusion changes who is in the benchmark and leaves the size distribution alone.
<!-- /generated -->

The crypto rule combines prize names, campaign names, descriptions and entry-method types. A single weak keyword never decides. Excluding crypto changes who is in the benchmark and leaves campaign size where it was: crypto median 17,305 contestants versus 16,175 ordinary. Any claim that crypto inflated participation figures is a hypothesis.

## What the ordinary segment shows (extracted)

<!-- generated:benchmark -->
| Measure | Value | n or note |
|---|---|---|
| Valid contestants | median 2,201, IQR 1,415 to 4,152, 90th pct 9,006 | 37,180. Floor is 1,001 by selection |
| Valid entries | median 10,445 | 37,123. Entries count actions, and one person makes many |
| Entries per contestant | median 4.34, IQR 2.68 to 7.07 | 37,123 |
| Impressions | median 9,072 | 37,148 with a non-zero value. Zeros treated as unknown |
| Duration | median 16 days, IQR 8 to 31 | 37,180. Maximum 13,200 days (evergreen campaigns) |
| One prize record | 79.2% of campaigns | quantity may still exceed 1 |
| Any quantity above 1 | 31.5% of campaigns | |
| Prize value stated | 40.5% of prize records | 59.5% unknown |
| Stated USD values | median 299, IQR 100 to 864, 90th pct 2,042 | 24,365 records. Max 10,000,000 |
| Stated EUR values | median 41, IQR 41 to 1,000, 90th pct 3,748 | 15 records. Too few to use. Max 9,100 |
| Stated CAD values | median 2,340, IQR 840 to 4,500, 90th pct 35,000 | 8 records. Too few to use. Max 35,000 |
| Stated GBP values | median 450, IQR 420 to 940, 90th pct 1,200 | 8 records. Too few to use. Max 1,200 |
| Stated AUD values | median 899, IQR 750 to 4,000, 90th pct 4,500 | 7 records. Too few to use. Max 4,500 |
| Stated TRY values | median 52,500, IQR 20,000 to 85,000, 90th pct 85,000 | 2 records. Too few to use. Max 85,000 |
| Stated NZD values | median 1,000, IQR 1,000 to 1,000, 90th pct 1,000 | 1 records. Too few to use. Max 1,000 |
| Stated COIN values | median 500, IQR 500 to 500, 90th pct 500 | 1 records. Too few to use. Max 500 |
| Fully valued campaign totals (USD) | median 900, IQR 329 to 2,000 | 14,538 campaigns. Max 50,000,000 |
| Repeat organizers | 1,424 organizers with 5+ campaigns account for 77.0% of campaigns | patterns can reflect prolific accounts |
| Plan tier | Business 12,976, Pro 19,303, Hobby 2,220, Free 1,533, Premium 1,144, Not Available 4 | tier at export time |
<!-- /generated -->

## By campaign size (extracted, descriptive only)

Every band is still a selected sample with a floor, and bigger campaigns come from bigger organizers with bigger budgets, so differences between bands describe who runs what. They do not show that a prize made a campaign larger.

<!-- generated:bands -->
| Band (valid contestants) | Campaigns | Organizers | Value stated | Stated USD median (n) | Campaign total USD median (n) | One prize record | Entries per contestant | Duration median |
|---|---|---|---|---|---|---|---|---|
| 1k-2.5k | 20,887 | 5,310 | 40% | 200 (12,715) | 525 (8,093) | 80% | 4.31 | 15 days |
| 2.5k-10k | 13,083 | 3,142 | 42% | 376 (9,458) | 1,297 (5,267) | 78% | 4.38 | 18 days |
| 10k+ | 3,210 | 781 | 38% | 799 (2,192) | 3,000 (1,178) | 80% | 4.405 | 20 days |

Primary prize category (first prize record) by band, share of campaigns:

| Category | 1k-2.5k | 2.5k-10k | 10k+ |
|---|---|---|---|
| Tech hardware | 26.4% | 32.6% | 39.3% |
| Gift card or cash | 12.1% | 10.5% | 8.9% |
| Bundle or box | 10.2% | 9.0% | 5.6% |
| Experience, travel, tickets | 4.8% | 6.1% | 6.5% |
| Game items or skins | 7.9% | 6.2% | 5.6% |
| Merch, apparel, collectibles | 4.0% | 4.1% | 5.0% |
| Home, garden, appliance | 4.5% | 4.9% | 1.7% |
| Regulated goods (firearms) | 2.5% | 3.8% | 10.2% |
| Sports and outdoor gear | 2.2% | 1.8% | 1.1% |
| Food, drink, consumables | 1.9% | 1.3% | 0.5% |
| Subscription or membership | 1.0% | 0.6% | 0.4% |
| Discount or coupon | 0.8% | 0.4% | 0.1% |
<!-- /generated -->

## Inferred prize values from text

To reduce the 61% gap we parsed explicit amounts from prize names ("$4,000 RTX PC"), from "worth / valued at / MSRP" phrases in descriptions, and from campaign titles of single-prize campaigns.

- Records with a parsed value: 10,487 (7,661 from prize names, 903 from campaign titles, 1,923 from description phrases).
- Records that had no stated value but gained a parsed one: 4,955. Coverage rises from 40.5% to 48.7%.
- Validation: 5,018 records had both a stated USD value and a parsed "$" value, and 79% agreed within ±20%. Disagreements are mostly totals across several prizes, marketing round numbers, or a cash component inside a larger bundle.
- The "$" symbol is recorded as "USD?" because it is ambiguous (USD, CAD, AUD and others). Parsed-only "$" values: n=3,519, median 400, IQR 100 to 1,000. The maximum (2.4 million) is a campaign-wide total that an organizer typed into one prize record.
- Parsed values are what organizers wrote, never what they paid. They are kept separate from stated values and never used in a record-level claim.

Category medians of stated values are given in the taxonomy as reference ranges. We do not fill missing records with them.

## What the data cannot support

- **Causation or effect size.** Every campaign reached at least 1,000 contestants, and there is no set of smaller or failed campaigns to compare against. The size bands compare selected samples with each other, which shows who ran what and nothing about what a prize did. Nothing here shows that a prize type produced participation.
- **Entrant volume promises.** No prize "guarantees" a number of entrants. Volume depends on promotion, audience size, entry friction and timing, none of which the prize controls.
- **Business outcomes.** Sales, lead quality, retention and profitability are absent from the export.
- **Cost.** Values are stated retail values entered by organizers, often rounded, sometimes totals, occasionally wrong by orders of magnitude. Organizer cost is unknown.
- **Winners.** Quantity is the number of units listed and may differ from the number of winners actually awarded.
- **Currency merging.** Values were never converted. USD and EUR are reported separately, and parsed "$" values are flagged as ambiguous.
- **Current platform features.** Entry-method types in the export are history. Current capability lives in each platform's own documentation.

## Classification limits

- Prize categories come from name-pattern rules (50,402 records) plus a private LLM-assisted label pass on the 10,611 unique names the rules missed (9,880 records after dropping low-confidence labels). 5.6% remain unclassified and 7.0% are placeholders ("1st Prize", or a campaign title reused as the prize name). Label-pass categories are a language model's inference over organizer-typed text in many languages. Spot checks looked sound, and no systematic accuracy measurement was done. Without the private label files, rules alone leave about 21% unclassified.
- The own-product flag is a word-overlap heuristic with both false positives and false negatives.
- Crypto detection is conservative on purpose. The 1,251 ambiguous campaigns probably include some ordinary giveaways and some crypto ones. The label pass caught token names the rules had missed, but non-English crypto campaigns (an Arabic-language token airdrop, an NFT platform's mystery box) were seen in the ordinary segment during spot checks, so a small residual remains.

## Text safety

Descriptions contained URLs in 5,069 campaigns, HTML in 17, and phrases addressed to an AI in 14. All were treated as data. Nothing was fetched, executed or followed, and no example reproduces a link.

## Impressions and conversion

Verified from the platform's reporting terms page on 9 September 2026: impressions count one view per user per 24 hours, an action is one entry method completed, entries are actions completed times entry worth, users are unique entrants, and the platform quotes an average conversion rate of about 34%. The export's valid contestants are users, valid entries are entries, and entry worth is absent, so entries per entrant mixes how many actions people did with how much each was worth.

Impressions in the export are unique per day, so a visitor who returns counts again each day. Repeatable actions (daily bonus, loyalty, timed bonus) and long runs raise impressions per contestant and lower contestants per impression without any change in who entered. The clean subset removes campaigns with a repeatable action and any run over 14 days. Medians, ordinary segment, descriptive only. The comparisons that depend on conversion live in the entry-method planner and timing references, all computed on the clean subset by `analysis/compare_groups.py`.

<!-- generated:cmp_vertical -->
| Vertical, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| unclassified | 7,638 | 1,983 | 3.49 | 39% | 2.6 | 5 |
| gaming_streaming | 1,941 | 2,291 (+16%) | 4.69 (+34%) | 36% (-6%) | 2.8 | 7 |
| travel_events | 306 | 2,521 (+27%) | 2.84 (-19%) | 31% (-18%) | 3.2 | 5 |
| tech_phones_gadgets | 591 | 2,807 (+42%) | 3.59 (+3%) | 33% (-14%) | 3.0 | 5 |
| music_media | 95 | 1,558 (-21%) | 2.85 (-19%) | 34% (-12%) | 3.0 | 5 |
| food_drink | 213 | 1,993 (+1%) | 2.89 (-17%) | 37% (-3%) | 2.7 | 5 |
| home_garden | 250 | 2,230 (+12%) | 3.22 (-8%) | 41% (+7%) | 2.4 | 5 |
| fitness_outdoor | 143 | 2,021 (+2%) | 2.79 (-20%) | 34% (-11%) | 2.9 | 5 |
| kids_family_pets | 190 | 2,134 (+8%) | 2.83 (-19%) | 35% (-9%) | 2.8 | 4 |
| beauty_fashion | 119 | 1,667 (-16%) | 1.90 (-46%) | 39% (+2%) | 2.6 | 2 |
| software_apps | 123 | 1,821 (-8%) | 3.77 (+8%) | 36% (-5%) | 2.7 | 6 |
| auto_moto | 27 | 1,866 (-6%) | 3.13 (-10%) | 36% (-6%) | 2.8 | 5 |
<!-- /generated -->

Verticals are a regex on names and leave 41% of campaigns unclassified. Gaming, tech and travel campaigns draw more contestants, beauty campaigns see the fewest actions per entrant, and home and garden campaigns convert best. Use them as context for a customer's expectations, never as targets.
