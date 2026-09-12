# Benchmarks

The script ranks a campaign against every fifth percentile of twelve figures in `percentiles.json` (Entrants, Impressions (views of the campaign page), Conversion Rate, actions and entries per Entrant, entries, Entrants per day, action count, duration, stated Prize value per Entrant, email signups, share who signed up for email, referral entries per Entrant, follows by network), plus completions per Entrant for 51 Gleam actions, for all campaigns, the campaigns we can compare fairly, campaigns your size, and your vertical. The tables below give the typical figure and the reading guide.

Every figure is drawn from the campaigns behind these numbers (116,499 campaigns that reached 100 unique Entrants, crypto and purchase-only campaigns removed). Typical figures unless stated. The campaigns we can compare fairly have no repeatable action and a run of 14 days or less, because Impressions are unique per person per day.

## Campaign size

<!-- generated:bm_size -->
| Metric | Lower quarter | Typical | Upper quarter | Top tenth | Campaigns |
|---|---|---|---|---|---|
| Entrants | 225 | 492 | 1,290 | 3,334 | 116,499 |
| Entries | 882 | 2,322 | 6,715 | 17,903 | 116,283 |
| Entries per Entrant | 2.74 | 4.38 | 7.06 | 11.87 | 116,283 |
| Entries per 100 Entrants | 274 | 438 | 706 | 1,187 | 116,283 |
| Impressions | 865 | 2,033 | 5,590 | 16,363 | 116,119 |
| Duration in days | 7 | 14 | 29 | 35 | 115,754 |
<!-- /generated -->

Half of all campaigns sat between 225 and 1,290 Entrants, and the script compares a campaign against others in its own band.

| Comparison band | Campaigns | Businesses |
|---|---|---|
| 100 to 250 Entrants | 33,074 | 9,533 |
| 250 to 500 | 25,681 | 6,496 |
| 500 to 1,000 | 21,838 | 5,509 |
| 1,000 to 2,500 | 20,021 | 5,077 |
| 2,500 to 10,000 | 12,714 | 2,991 |
| 10,000 or more | 3,171 | 748 |

State entries as entries per 100 Entrants, not the raw decimal, using the row above. Give the reader's own figure the same way (entries divided by Entrants, times 100), and state the gap against the typical figure as a percentage or a plain multiple ("about half the typical rate"), never as two decimals side by side.

## Conversion Rate, by number of actions (the campaigns we can compare fairly)

| Actions | Campaigns | Conversion Rate |
|---|---|---|
| 1 to 3 | 10,838 | 44% |
| 4 to 6 | 12,430 | 35% |
| 7 to 10 | 9,744 | 29% |
| 11 or more | 6,795 | 31% |

## Conversion Rate, by duration (no repeatable actions)

| Duration | Campaigns | Conversion Rate |
|---|---|---|
| 1 to 7 days | 21,429 | 40% |
| 8 to 14 | 16,613 | 29% |
| 15 to 30 | 20,578 | 26% |
| 31 to 60 | 11,468 | 23% |
| 61 or more | 3,532 | 22% |

## How many did each kind of action (completions per Entrant, all campaigns)

| Family | Campaigns offering | Typical | Typical range |
|---|---|---|---|
| Visit a page or profile | 94,591 | 0.80 | 0.61 to 0.94 |
| Follow or subscribe (free) | 78,061 | 0.51 | 0.35 to 0.69 |
| Share, repost or refer | 61,298 | 0.26 | 0.10 to 0.47 |
| Email or newsletter signup | 40,733 | 0.84 | 0.70 to 1.01 |
| Post or create content | 21,785 | 0.31 | 0.15 to 0.44 |

A share entry is a referred person multiplied by entry worth, so the share row is not a click rate. Full family tables sit in the entry-method-planner skill.

## What campaigns produced (extracted)

Completions of the acquire and amplify actions, summed per campaign, across the 116,499 campaigns behind these numbers that offered each. This is the closest the dataset comes to an outcome: an email signup completed is an address on the list, a follow completed is a follower at that moment. Unsubscribes, unfollows and list quality are not visible. Stated USD per completion divides the stated Prize pool by completions, for campaigns with every Prize valued in USD, and the stated value is what the organizer wrote.

Reading it: cost per completion varies widely by asset, from about $0.40 for an email signup to about $16 for a content submission (exact figures and sample sizes in the table below). Follows sit in between, roughly $0.6 to $1.2 on most networks, with Snapchat at $2.30 and LinkedIn at $4.63 above that.

A subscribe asset's Share of Entrants column can read over 100: a campaign can offer more than one subscribe action, such as a newsletter and an SMS list, and every completion counts.

| Asset | Campaigns | Lower quarter | Typical | Upper quarter | Top tenth | Share of Entrants | Stated USD per completion (Campaigns) |
|---|---|---|---|---|---|---|---|
| X follows | 66,279 | 134 | 309 | 841 | 2,382 | 61 (0.61) | 0.64 (24,490) |
| Referral entries (Viral Share) | 42,900 | 26 | 88 | 277 | 728 | 12 (0.12) | 2.89 (20,168) |
| Email signups | 39,532 | 306 | 712 | 1,648 | 4,009 | 99 (0.99) | 0.40 (19,518) |
| Twitch follows | 22,521 | 141 | 335 | 925 | 2,394 | 77 (0.77) | 0.57 (7,287) |
| Discord joins | 19,190 | 117 | 268 | 650 | 1,498 | 48 (0.48) | 1.15 (6,503) |
| TikTok follows | 14,329 | 103 | 230 | 638 | 1,519 | 38 (0.38) | 1.22 (5,631) |
| Instagram follows | 8,234 | 143 | 372 | 985 | 2,479 | 61 (0.61) | 0.81 (3,625) |
| Telegram joins | 4,153 | 226 | 640 | 1,740 | 3,724 | 88 (0.88) | 0.77 (1,165) |
| Facebook likes | 3,971 | 102 | 243 | 515 | 1,166 | 41 (0.41) | 0.83 (1,875) |
| YouTube subscribes | 3,506 | 160 | 374 | 920 | 2,022 | 83 (0.83) | 0.70 (1,080) |
| App downloads | 3,495 | 141 | 339 | 846 | 2,060 | 41 (0.41) | 1.31 (1,493) |
| Content submissions | 3,308 | 21 | 112 | 368 | 970 | 18 (0.18) | 15.89 (1,285) |
| Bluesky follows | 1,913 | 53 | 90 | 191 | 487 | 30 (0.30) | 1.00 (627) |
| LinkedIn follows | 1,737 | 92 | 229 | 571 | 1,410 | 28 (0.28) | 4.63 (657) |
| Pinterest follows | 1,608 | 112 | 240 | 430 | 669 | 40 (0.40) | 0.64 (971) |
| Threads follows | 1,219 | 57 | 148 | 279 | 577 | 24 (0.24) | 0.56 (684) |
| Snapchat follows | 983 | 55 | 154 | 591 | 2,065 | 21 (0.21) | 2.30 (548) |

Email signups and referral entries both scale with campaign size:

| Campaign size | Email signups (range) | Email signups typical | Referral entries (range) | Referral entries typical |
|---|---|---|---|---|
| 100 to 250 | 118 to 211 | 157 | 5 to 44 | 17 |
| 250 to 500 | 274 to 481 | 353 | 11 to 88 | 35 |
| 500 to 1,000 | 516 to 827 | 645 | 34 to 189 | 84 |
| 1,000 to 2,500 | 1,046 to 1,790 | 1,346 | 97 to 522 | 218 |
| 2,500 to 10,000 | 2,782 to 5,433 | 3,713 | 230 to 1,254 | 515 |
| 10,000 or more | 11,686 to 28,933 | 16,566 | 707 to 3,705 | 1,698 |

Stated USD per email signup by Prize category, campaigns with an email action:

| Prize category | Campaigns | Typical USD per signup |
|---|---|---|
| Other or unclassified | 5,142 | 0.59 |
| Gift card or cash | 4,398 | 0.16 |
| Tech hardware | 3,000 | 0.42 |
| Bundle or box | 2,666 | 0.60 |
| Game items or skins | 1,465 | 0.42 |
| Experience, travel, tickets | 930 | 1.16 |
| Merch, apparel, collectibles | 828 | 0.49 |
| Regulated goods (firearms) | 606 | 0.39 |
| Home, garden, appliance | 604 | 0.49 |
| Placeholder Prize name | 496 | 0.56 |

## By start year

<!-- generated:bm_year -->
| Year | Campaigns | Entrants | Conversion Rate |
|---|---|---|---|
| 2021 | 27,806 | 501 | 28% |
| 2022 | 25,956 | 475 | 29% |
| 2023 | 20,237 | 489 | 26% |
| 2024 | 16,725 | 472 | 24% |
| 2025 | 16,359 | 512 | 25% |
| 2026 | 7,992 | 528 | 27% |
| 2020 | 1,156 | 611 | 26% |
<!-- /generated -->

The typical campaign has held between 472 and 528 Entrants since 2021 while the Conversion Rate held steady. A campaign run this year sits a little above the typical figures across the whole export, at the same quality. The 2020 row rests on 1,156 campaigns against several thousand in every later year, so treat it as a rough marker.

## By template

Where a campaign was copied from, scoped to 100 or more Entrants, finance_crypto organizers excluded, so a review can compare a campaign against others built from the same template or the same source kind (across 117,346 campaigns, the four source kinds).

| Source | Share | Campaigns | Businesses | Conversion Rate |
|---|---|---|---|---|
| Own earlier campaign, copied | 58% | 68,068 | 5,673 | 0.265 |
| Blank, no copying | 23% | 27,188 | 10,864 | 0.285 |
| A campaign outside the dataset | 10% | 12,019 | 4,238 | 0.254 |
| Gleam library template | 9% | 10,071 | 6,523 | 0.263 |

Typical figures for the library templates with the most campaigns at this size:

<!-- generated:bm_template -->
| Template | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Days | Methods | Email offered | Share offered |
|---|---|---|---|---|---|---|---|---|---|
| Gleam Sweepstakes | 3,097 | 2,310 | 748 | 24% | 4.23 | 15 | 7 | 58% | 60% |
| Instant Entry | 1,717 | 924 | 248 | 47% | 1.00 | 8 | 1 | 7% | 6% |
| YouTube Contest | 603 | 493 | 437 | 27% | 3.72 | 18 | 6 | 9% | 38% |
| Email Signup | 420 | 343 | 742 | 30% | 1.92 | 15 | 4 | 92% | 61% |
| Refer A Friend | 286 | 251 | 606 | 23% | 2.44 | 19 | 4 | 35% | 92% |
| E-Commerce Giveaway | 273 | 248 | 618 | 23% | 4.45 | 17 | 9 | 79% | 80% |
| Instagram Contest | 244 | 219 | 500 | 23% | 3.49 | 14 | 6 | 29% | 58% |
| Contest Entry Form | 181 | 155 | 765 | 24% | 1.94 | 17 | 3 | 37% | 17% |
| Social Media Giveaway | 171 | 159 | 285 | 26% | 4.50 | 14 | 7 | 16% | 22% |
| Twitter / X Contest | 159 | 131 | 282 | 22% | 4.43 | 10 | 6 | 8% | 31% |
| Photo Contest | 157 | 138 | 345 | 10% | 2.26 | 21 | 3 | 24% | 22% |
| Email Signup Referrals | 149 | 113 | 666 | 27% | 1.91 | 16 | 3 | 97% | 94% |
<!-- /generated -->

Source: `analysis/output/templates.json` (`source_mix`, `by_template`).

## Benchmarks by plan tier

A Free or Hobby organizer runs on a plan with no email or share action, so ranking that campaign against the Premium typical figure compares two different tools. Read a campaign against its own tier first, then against campaigns your size. Figures come from `field_cuts.json`, which runs on the same 116,499 campaigns as the numbers above, so a tier row and the campaign-size table split one population two ways. Conversion Rate here is Entrants over Impressions on every run in the tier, not the campaigns we can compare fairly, so a tier with more long or repeatable campaigns reads lower for that reason alone.

<!-- generated:bm_tier -->
| Tier | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Days | Methods | Email offered | Share offered |
|---|---|---|---|---|---|---|---|---|---|
| Pro | 62,061 | 10,160 | 526 | 26% | 4.83 | 14 | 8 | 38% | 48% |
| Business | 29,645 | 3,553 | 709 | 24% | 4.34 | 15 | 8 | 45% | 43% |
| Free | 11,993 | 4,183 | 238 | 34% | 3.29 | 12 | 4 | 0% | 0% |
| Hobby | 10,802 | 2,555 | 307 | 31% | 3.77 | 11 | 6 | 0% | 2% |
| Premium | 1,993 | 202 | 1,221 | 23% | 5.34 | 22 | 10 | 61% | 39% |
<!-- /generated -->

Free campaigns carry no email or share action at all and Hobby campaigns carry almost none, so their Conversion Rate sits above Pro and Business on a smaller ask, not a stronger landing page. Premium campaigns run the most methods over the longest window and the lowest Conversion Rate follows from the duration and repeatable-action caveat, not from a weaker campaign.

## Benchmarks by organizer stage, scale and business type

For picking a comparison group closer than campaigns your size: how established the business is, how big the organization is, what kind of business it runs, and its industry. Figures come from `industries.json`, whose scope is campaigns with 100 or more Entrants and a labelled organizer site, wider than the 116,499 campaigns behind the numbers above (it keeps crypto, which is the largest single industry, and applies no purchase-only exclusion). Conversion Rate is Entrants over Impressions on every run, same caveat as the tier table above.

By organizer stage (`by_org_stage`), read from the homepage:

<!-- generated:bm_stage -->
| Stage | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Days | Email offered |
|---|---|---|---|---|---|---|---|
| Small business | 60,935 | 7,897 | 540 | 26% | 4.44 | 14 | 45% |
| Startup | 23,190 | 5,227 | 635 | 26% | 5.34 | 10 | 15% |
| Mid market | 17,126 | 1,384 | 616 | 28% | 4.29 | 8 | 22% |
| Individual | 10,371 | 1,808 | 309 | 26% | 5.49 | 16 | 10% |
| Enterprise | 6,675 | 507 | 716 | 32% | 3.68 | 14 | 25% |
| Unknown | 2,436 | 755 | 325 | 26% | 4.25 | 13 | 22% |
| Public body | 1,109 | 294 | 445 | 27% | 3.35 | 14 | 44% |
<!-- /generated -->

By organization scale (`by_org_scale`, from revenue, employee and traffic-rank signals):

<!-- generated:bm_scale -->
| Scale | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Days |
|---|---|---|---|---|---|---|
| Small | 40,576 | 3,663 | 495 | 25% | 5.03 | 14 |
| Micro | 33,465 | 11,488 | 401 | 27% | 4.70 | 14 |
| Mid | 26,886 | 1,770 | 756 | 27% | 4.29 | 13 |
| Shared host | 21,907 | 4,076 | 382 | 34% | 4.42 | 9 |
| Large | 16,918 | 658 | 627 | 30% | 4.31 | 7 |
| Enterprise | 4,105 | 387 | 648 | 30% | 4.69 | 10 |
<!-- /generated -->

By business type (`by_business_type`, from what the organizer's homepage sells):

<!-- generated:bm_btype -->
| Type | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Days | Email offered |
|---|---|---|---|---|---|---|---|
| Brand | 31,193 | 5,708 | 587 | 26% | 4.29 | 14 | 41% |
| Software | 30,426 | 5,133 | 633 | 28% | 5.18 | 8 | 12% |
| Retailer | 21,733 | 2,266 | 651 | 28% | 4.36 | 14 | 44% |
| Media or publisher | 21,108 | 1,645 | 418 | 24% | 4.94 | 17 | 42% |
| Creator | 18,168 | 4,187 | 348 | 34% | 4.28 | 12 | 5% |
| Other | 7,846 | 2,149 | 388 | 29% | 4.60 | 10 | 18% |
| Community | 4,999 | 1,128 | 343 | 30% | 5.45 | 9 | 8% |
| Service business | 4,092 | 803 | 365 | 25% | 3.43 | 12 | 32% |
| Agency | 3,324 | 368 | 484 | 26% | 4.52 | 12 | 22% |
| Nonprofit | 968 | 280 | 390 | 26% | 3.33 | 16 | 33% |
<!-- /generated -->

By industry (`by_industry_excluding_crypto`), finance_crypto (43,194 campaigns) held out on the same crypto exclusion as the rest of this page:

<!-- generated:bm_industry -->
| Industry | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Days | Email offered |
|---|---|---|---|---|---|---|---|
| Gaming and esports | 25,711 | 4,943 | 404 | 27% | 5.06 | 12 | 16% |
| Media and entertainment | 21,745 | 2,111 | 400 | 24% | 4.98 | 18 | 43% |
| Electronics and tech | 15,683 | 2,091 | 897 | 30% | 4.60 | 14 | 23% |
| Food and drink | 4,763 | 909 | 622 | 27% | 3.60 | 19 | 54% |
| Toys, hobbies, collectibles | 4,730 | 763 | 416 | 26% | 4.24 | 15 | 39% |
| Other | 4,694 | 1,589 | 319 | 28% | 4.47 | 10 | 11% |
| Apparel and fashion | 4,670 | 828 | 613 | 31% | 2.57 | 8 | 51% |
| Sports and outdoors | 4,655 | 1,022 | 966 | 24% | 3.78 | 16 | 52% |
| Travel and events | 4,049 | 661 | 488 | 27% | 3.28 | 15 | 43% |
| Home and garden | 3,739 | 602 | 916 | 29% | 3.58 | 15 | 58% |
| Creator influencer | 3,429 | 1,067 | 315 | 37% | 4.84 | 8 | 4% |
| Health wellness fitness | 3,209 | 509 | 474 | 22% | 4.26 | 16 | 32% |
| Retail marketplace | 2,880 | 389 | 488 | 29% | 5.10 | 8 | 28% |
| Software and SaaS | 2,513 | 615 | 647 | 28% | 5.08 | 12 | 26% |
| Automotive | 2,331 | 387 | 949 | 26% | 4.06 | 14 | 56% |
<!-- /generated -->

This industry cut reads the organizer's own homepage, and so do `percentiles.json`'s groups since the  rebuild: the ten vertical names `review.py` accepts (gaming, technology, fashion_beauty and the rest) fold the homepage labels together (fashion_beauty is apparel, beauty and jewellery, kids_family_pets is baby, pets and toys), and every label with five organizers also has its own `industry:` group. Conversion Rate by vertical sits in a narrow band (table below, 116,499 campaigns). Say which cut a rank came from.

| Vertical | Conversion Rate |
|---|---|
| Gaming | 27% |
| Technology | 29% |
| Fashion and beauty | 31% |
| Home | 31% |
| Fitness and outdoor | 24% |
| Software | 26% |

Gaming reads differently across sources because each draws on a different scope, so use the cut that matches the comparison you're making. `prize_timing_cuts.json`'s `by_industry_ordinary` scopes the homepage labels to the campaigns behind these numbers, tighter than the `by_industry` table further up the page. The Prize picker's ROI benchmarks describe the earlier dataset's campaigns we can compare fairly, no repeatable action and a run of 14 days or less.

| Source | Conversion Rate | Campaigns | Organizers |
|---|---|---|---|
| `by_industry_ordinary` (tighter scope) | 27% | 6,328 | 1,414 |
| `by_industry` (table above) | 28% | 7,808 | 1,840 |
| Prize picker ROI benchmarks (earlier dataset) | 36% | — | — |

Source: `analysis/output/prize_timing_cuts.json` (`by_industry_ordinary`), `analysis/output/industries.json` (`vertical_mapping`).

### Comparing against a similar-sized company

Source: `analysis/output/industries.json` (`by_employee_band`, `by_founded_band`, `enrichment_coverage`).

`industries.json`'s `by_employee_band` and `by_founded_band` add a company headcount and company age cut, matched against company records, where the other industry cuts read the homepage. That match covers 3,609 businesses [`analysis/output/industries.json`, `enrichment_coverage`, `by_employee_band`, `by_founded_band`]. How many carry an industry label is not a figure the outputs hold, so read both cuts for direction and never as coverage of the whole set. The match skews toward companies with a public web presence, and the match skews toward companies with a public web presence, so read this as a lean on the larger and more established end, not a full comparison across every business.

| Employee count | Campaigns | Businesses | Conversion Rate | Email offered |
|---|---|---|---|---|
| 1 to 9 | 28,827 | 1,798 | 25.5% | 30% |
| 10 to 49 | 27,400 | 1,215 | 25.2% | 44% |
| 50 to 199 | 12,043 | 552 | 29.2% | 32% |
| 200 to 999 | 9,352 | 285 | 29.8% | 25% |
| 1,000 or more | 12,262 | 524 | 34.2% | 17% |

Businesses with 200 or more staff see a higher Conversion Rate than businesses under 50 staff, 29.8% and 34.2% against 25.5% and 25.2%, while offering an email action about half as often, 25% and 17% against 30% and 44% (table above).

`by_founded_band` shows a related split by company age: the newest companies offer email far less often than older ones, while running the highest entries per Entrant and the highest referral rate of the five groups (table below, 11,919 to 18,308 campaigns and 660 to 947 organizers per band).

| Founded | Campaigns | Businesses | Email offered | Entries per Entrant | Referrals per 100 Entrants |
|---|---|---|---|---|---|
| 2020 or later | 11,919 | 824 | 14.9% | 5.56 | 60 |
| 2015 to 2019 | 17,931 | 947 | 24.2% | 4.80 | 30 |
| 2010 to 2014 | 12,553 | 660 | 41.5% | 4.83 | 14 |
| 2000 to 2009 | 18,308 | 688 | 44.8% | 4.99 | 9 |
| Before 2000 | 14,533 | 862 | 38.5% | 3.57 | 12 |

Company size, company age, plan tier and organizer scale move together, so read this as another angle on the pattern in the tables above, not a separate driver.


## Campaign sequence and organizer activity

Where the organizer sits in their own run of campaigns, from `field_cuts.json`'s `by_campaign_sequence` and `by_organizer_active`:

<!-- generated:bm_sequence -->
| Sequence | Campaigns | Businesses | Entrants | Conversion Rate | Days |
|---|---|---|---|---|---|
| 11th plus | 63,192 | 1,877 | 516 | 27% | 14 |
| 4th to 10th | 21,244 | 4,622 | 535 | 27% | 14 |
| 1st campaign | 17,633 | 17,633 | 382 | 26% | 16 |
| 2nd to 3rd | 14,430 | 8,546 | 453 | 27% | 15 |
<!-- /generated -->

<!-- generated:bm_activity -->
| Activity | Campaigns | Businesses | Entrants | Conversion Rate | Days |
|---|---|---|---|---|---|
| Ran another campaign in the last 12 months | 61,616 | 3,563 | 538 | 27% | 14 |
| Has not | 54,883 | 14,070 | 441 | 27% | 14 |
<!-- /generated -->

Later campaigns see a higher Conversion Rate over a shorter run than a 1st campaign. Read this as which organizers kept going before reading it as improvement: an organizer whose first campaign did poorly is less likely to be in the file with a 2nd, so the 11th-plus row describes organizers who kept going, not the same organizer's own campaign 1 through campaign 11.

Figures that compare like with like sit behind that caveat, from `organizer_history.json`. This source uses a wider 100+ Entrant scope (120,561 campaigns, 18,324 organizers), a broader size range than the 1,000+ scope the rest of this page uses, so the counts below cover smaller campaigns too.

- Organizers who start bigger are much more likely to keep going: about 2.5x the reach rate to an 11th campaign (table below). This is why every cut below matches organizers on their first-campaign size before comparing them.

- Matched on first campaigns of 1,000 to 2,499 Entrants, Entrants and entries per Entrant move in opposite directions across the sequence (table below): Entrants fall once you allow for starting size, while entries per Entrant looks like it rises.

- That rise in entries per Entrant is survivorship, not improvement. Paired within-organizer transitions, each organizer against its own immediate next campaign with no gap, show close to zero typical change in entries per Entrant at every step. Organizers who started higher are the ones who keep going to later positions, not individual campaigns improving.

- Entrants typically decline from one campaign to the next too, though the decline narrows the further into the sequence you go. Well under half of "next" campaigns actually outdraw the one before (44% to 49%) [8,583 to 62,640 paired transitions].

| First campaign size | Reach an 11th campaign | Organizers |
|---|---|---|
| 10,000+ Entrants | 16.3% | 1,144 |
| Under 250 Entrants | 6.4% | 8,957 |

<!-- generated:bm_seq_band -->
| Position in sequence (1,000 to 2,499 Entrants) | Entrants | Entries per Entrant | Organizers |
|---|---|---|---|
| 1st | 1,483 | 3.94 | 2,689 |
| 2nd | 986 | 3.90 | 1,535 |
| 3rd-5th | 923 | 4.10 | 1,117 |
| 6th-10th | 896 | 4.29 | 652 |
| 11th+ | 678 | 6.18 | 373 |
<!-- /generated -->

| Transition | Typical change in Entrants |
|---|---|
| 1st to 2nd | -4.0% |
| 11th-plus | -0.4% |

None of this says a second or third campaign will not grow, so it gives no reason to stop after one. What it rules out is treating the campaign count itself as the lever: running more of them, on its own, carries no guaranteed lift. The line below on continuers shows where the real lever sits, in what the organizer sets up before the next campaign even launches, Prize, entry mix, timing and promotion, the design choices this skill and `giveaway-entry-method-planner`, `giveaway-timing-and-duration` and `giveaway-promotion-plan` cover.

Neither a steady schedule nor a fast one shows a performance edge once organizers are matched on total campaign count, and frequent repetition carries no fatigue signature, both worth publishing as clean negative results (tables below, same source and 100+ Entrant scope as above). Irregular spacing is the norm: the typical coefficient of variation of gaps runs about 1.0 [6,431 qualifying sites]. A faster cadence does not show a growing penalty over a slower one, which rules out a simple audience-fatigue story.

| Spacing (organizers with 21+ campaigns) | Typical Entrants change |
|---|---|
| Sporadic | -0.37% |
| Regular | -0.44% |

Sample: 52,246 sporadic against 17,095 regular paired transitions.

| Cadence | Change at 1st transition |
|---|---|
| Monthly or faster | -2.3% |
| Over a month between campaigns | -5.1% to -5.4% |

Both cadences ease toward zero by the 11th-plus transition.

Organizers who go on to run a second campaign already look different on their first one, matched within every first-campaign size: higher entries per Entrant and a shorter run than organizers who never continued, in the same direction across all 7 size bands tested (table below, organizer counts range 110 to 4,192 per cell).

| First-campaign size | Entries/Entrant, continuers | Entries/Entrant, non-continuers | Duration, continuers | Duration, non-continuers |
|---|---|---|---|---|
| Under 250 | 3.82 | 3.41 | 13 days | 16 days |
| 1,000-2,499 | 4.13 | 3.63 | 16 days | 22 days |
| 10,000+ | 3.81 | 3.19 | 22 days | 31 days | See `giveaway-timing-and-duration` for the duration angle.

Source: `analysis/output/organizer_history.json` (`reach_rate_by_first_band`, `sequence_curve_by_first_band`, `within_organizer_transition_by_seq`, `cadence_regularity`, `transition_by_cadence_regularity_and_campaign_count`, `transition_by_gap_length_and_seq`, `first_campaign_by_survival_matched_on_band`).

## Organizer site age

`field_cuts.json`'s `by_organizer_tenure` groups campaigns by how old the organizer's site was when the campaign launched.

| Site age | Campaigns | Businesses | Conversion Rate | Email offered |
|---|---|---|---|---|
| 3 years or more | 56,242 | 4,077 | 26% | 35% |
| 1 to 3 years | 26,629 | 4,594 | 28% | 31% |
| 6 to 12 months | 9,286 | 3,217 | 28% | 31% |
| 1 to 6 months | 12,430 | 4,951 | 27% | 32% |
| 1 to 4 weeks | 4,959 | 3,704 | 27% | 35% |
| Under 1 week | 5,483 | 5,102 | 26% | 28% |

Conversion Rate barely moves across site age, and neither does how often an email action is offered (table above). Both hold inside a few points across every group, so site age is a weak comparison to lean on.

Source: `analysis/output/field_cuts.json` (`by_organizer_tenure`).

## Country benchmarks

`country_cuts.json`'s `by_country` scopes every campaign with 100 or more Entrants, organizer country read from IP, with a floor of five organizers per row. The twelve countries with the most campaigns:

| Country | Campaigns | Businesses | Entrants | Conversion Rate | Entries/Entrant | Days | Methods | Impressions/Entrant | Business tier or above |
|---|---|---|---|---|---|---|---|---|---|
| United States | 58,843 | 9,105 | 491 | 25% | 4.52 | 14 | 7 | 3.96 | 29% |
| United Kingdom | 15,716 | 1,847 | 500 | 31% | 4.32 | 21 | 7 | 3.28 | 30% |
| Canada | 7,276 | 1,156 | 568 | 25% | 3.85 | 12 | 6 | 4.06 | 26% |
| Japan | 6,505 | 291 | 352 | 30% | 5.56 | 6 | 7 | 3.36 | 61% |
| Australia | 6,433 | 1,406 | 548 | 29% | 3.32 | 15 | 6 | 3.47 | 35% |
| India | 6,010 | 873 | 1,065 | 34% | 5.36 | 9 | 8 | 2.98 | 11% |
| Brazil | 5,860 | 563 | 478 | 59% | 6.98 | 1 | 10 | 1.69 | 9% |
| Singapore | 4,743 | 351 | 656 | 32% | 4.71 | 7 | 6 | 3.16 | 49% |
| South Korea | 4,521 | 537 | 534 | 30% | 5.78 | 7 | 7 | 3.32 | 38% |
| Vietnam | 3,762 | 773 | 865 | 32% | 5.78 | 9 | 8 | 3.18 | 30% |
| Germany | 3,530 | 472 | 658 | 28% | 4.84 | 11 | 7.5 | 3.64 | 25% |
| Hong Kong | 3,113 | 573 | 718 | 30% | 4.84 | 7 | 7 | 3.37 | 24% |

Japan runs the highest plan-tier mix of the twelve, 61% of campaigns on Business or above, against 9% for Brazil. Brazil's one-day typical duration and its 59% Conversion Rate are two readings of the same thing. Impressions count once per visitor per day, so a one-day campaign has one day of Impressions to divide into and converts higher by construction. Both figures rest on campaigns that are 90% repeats from a small set of accounts, so treat the row as a description of automated draws.

### City benchmarks

`field_cuts.json`'s `by_organizer_city` adds a city cut of the same shape, scoped like the rest of this page to 100 or more Entrants. Every row already carries five or more organizers. The eight cities with the most campaigns, for a finer comparison when one fits:

<!-- generated:bm_city -->
| City | Campaigns | Businesses | Entrants | Conversion Rate | Entries/Entrant | Days | Methods |
|---|---|---|---|---|---|---|---|
| Los Angeles, United States | 3,020 | 370 | 636 | 24% | 4.80 | 12 | 7 |
| Plano, United States | 2,440 | 11 | 336 | 15% | 12.36 | 31 | 11 |
| Sydney, Australia | 1,863 | 375 | 573 | 28% | 3.05 | 18 | 5 |
| Melbourne, Australia | 1,515 | 333 | 671 | 29% | 3.19 | 15 | 6 |
| London, United Kingdom | 1,465 | 44 | 589 | 43% | 1.68 | 19 | 2 |
| Chicago, United States | 1,306 | 143 | 570 | 26% | 7.68 | 15 | 12 |
| Seattle, United States | 918 | 106 | 1,642 | 35% | 3.14 | 10 | 5 |
| Singapore | 915 | 115 | 487 | 22% | 4.65 | 14 | 7 |
<!-- /generated -->

Source: `analysis/output/country_cuts.json` (`by_country`), `analysis/output/indicators.json` (`impressions_per_contestant_by_country`, `plan_tier_by_country`), `analysis/output/field_cuts.json` (`by_organizer_city`).

## Every size band

`field_cuts.json`'s `by_band_all` covers every campaign with a contestant count, so each band has its own benchmark row. Counts are exact: the contestant dump covers the 100 to 1,000 range, so nothing here is modelled.

Read the campaign counts in this table on their own terms. `by_band_all` is the whole platform at the floor, before the crypto, ambiguous and purchase-only campaigns are set aside, so its rows add up to far more than the ordinary population every other table in this file describes. Use it to place a campaign in its band, and take the benchmark a campaign is judged against from the tables above.

| Size | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Days | Methods | Email offered | Share offered |
|---|---|---|---|---|---|---|---|---|---|
| 100 to 250 | 47,150 | 13,254 | 160 | 27% | 4.46 | 9 | 6 | 17% | 30% |
| 250 to 500 | 35,627 | 9,067 | 350 | 28% | 4.92 | 11 | 7 | 22% | 42% |
| 500 to 1,000 | 29,505 | 7,649 | 690 | 28% | 4.98 | 11 | 7 | 28% | 46% |
| 1,000 to 2,500 | 27,891 | 7,404 | 1,496 | 29% | 4.72 | 13 | 7 | 32% | 50% |
| 2,500 to 10,000 | 20,532 | 5,375 | 4,124 | 30% | 4.95 | 14 | 8 | 30% | 56% |
| 10,000 or more | 6,363 | 1,989 | 16,706 | 34% | 5.28 | 14 | 8 | 23% | 61% |

Entries per Entrant barely moves across the whole range, from 4.46 in the smallest band to 5.28 in the largest. The Entrants a small campaign does reach are working about as hard as the ones in a campaign a hundred times the size, so a low Entrant count is a reach problem, with engagement holding up.

Conversion Rate climbs gently with size, from 27% to 34%. A share action is offered far less often in small campaigns, 30% against 61% in the largest band, and email peaks in the middle bands at 32% against 17% in the smallest. Those are the two gaps a small campaign can close on its own, and the target is the next band's own figure.

State entries the same way here: entries per 100 Entrants, not the raw decimal (table below). Read a campaign's own figure against the matching row and state the gap as a percentage or a plain multiple ("about half", "roughly double"), never as two decimals set side by side.

| Size | Entries per 100 Entrants |
|---|---|
| 100 to 250 | 446 |
| 250 to 500 | 492 |
| 500 to 1,000 | 498 |
| 1,000 to 2,500 | 472 |
| 2,500 to 10,000 | 495 |
| 10,000 or more | 528 |

Source: `analysis/output/field_cuts.json` (`by_tier`, `by_campaign_sequence`, `by_organizer_active`, `by_band_all`) and `analysis/output/industries.json` (`by_org_stage`, `by_org_scale`, `by_business_type`, `by_industry`).

## Other reference points

- Top fifth against bottom fifth by Entrants pulls apart on Impressions and Prize pool, not on Conversion Rate or organizer experience (table below). Previous campaigns from the organizer no longer separate the two groups, unlike the earlier dataset where the top fifth had noticeably more.

- After a campaign of 5,000 or more Entrants, the next one reached 5,000 again 61% of the time, against 12% after a smaller one.

- Two more comparisons among the campaigns we can compare fairly: a campaign launched within 30 days of the organizer's previous one converts noticeably better than a first campaign and draws 42% more Entrants, and a campaign without a share action converts better than one with while drawing about a quarter fewer Entrants (table below).

<!-- generated:bm_quintile -->
| Top fifth vs bottom fifth (by Entrants) | Top fifth | Bottom fifth |
|---|---|---|
| Entrants | 3,338 | 140 |
| Impressions | 14,070 | 552 |
| Conversion Rate | 27.6% | 25.4% |
| Stated Prize pool (USD) | 1,200 | 120 |
| Previous campaigns from the business | 12 | 7 |

Reach is what separates the two, 25 times the Impressions for a Conversion Rate two points apart. [Extracted from `analysis/output/context_checks.json`, `top_vs_bottom_quintile`, 23,256 campaigns each side.]
<!-- /generated -->

<!-- generated:bm_splits -->
| Split (campaigns we can compare fairly) | Entrants | Conversion Rate |
|---|---|---|
| Within 30 days of previous campaign | 470 | 38% |
| First campaign | 332 | 31% |
| Share action offered | 543 | 29% |
| No share action | 408 | 37% |
<!-- /generated -->

The share-action line and the top-fifth line answer different questions and cannot be read as one finding. The share-action line splits campaigns by a setting the organizer chose before launch. The top-fifth line splits the same campaigns by the result they got afterwards. Neither says that adding or removing a share action moves a campaign between the fifths.

- December: 10.4% of starts, a quarter again an even month, and December campaigns drew more Entrants at a higher Conversion Rate, 560 at 30.8% against 471 to 508 at 25.6% to 26.9% across the other eleven months. [Extracted from `analysis/output/prize_timing_cuts.json`, `by_start_month`.]

## Campaign weighted against business weighted

[Extracted from `analysis/output/organizer_history.json`, `sequence_curve_all`, `reach_rate_by_first_band`, `ordinary_n` and `ordinary_organizers`. The shares below are worked from those counts and are not stored figures.]

Every benchmark on this page counts campaigns, and campaigns are not spread evenly across businesses. 63,775 of the 116,499, which is 55%, come from the 1,965 businesses on their eleventh campaign or later, 11% of the 17,633. The median business ran one or two campaigns in total. So a typical figure here describes the businesses that run giveaways constantly, and a reader on their first campaign is being measured against people who have run dozens.

The first row below is one campaign per business, which is the business-weighted view of the same data.

<!-- generated:bm_seqcurve -->
| The campaign is the business's | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant |
|---|---|---|---|---|---|
| 1st | 17,247 | 17,247 | 382 | 25.5% | 3.67 |
| 2nd | 8,445 | 8,445 | 434 | 26.4% | 3.85 |
| 3rd to 5th | 14,228 | 5,979 | 504 | 26.8% | 4.04 |
| 6th to 10th | 12,804 | 3,300 | 545 | 26.9% | 4.18 |
| 11th or later | 63,775 | 1,965 | 515 | 27.5% | 4.90 |
| All campaigns | 116,499 | 17,633 | 492 | 26.9% | 4.38 |
<!-- /generated -->

A first campaign drew 382 Entrants where the all-campaign figure is 492, so the headline benchmark sits about 29% above what a first-timer's peers actually did. Quote 382 to a reader running their first campaign and 492 only when they have run several. Entries per Entrant moves the same way, 3.67 against 4.38, because a business on its eleventh campaign runs more actions.

None of this says that running more campaigns produces bigger ones. The businesses still running an eleventh campaign are the ones whose earlier campaigns went well enough to justify another, which is survivorship, never a result.

How far businesses get, one row per business, by the size of their first campaign:

| First campaign | Businesses | Median campaigns run | Ran a 2nd | Reached a 5th | Reached an 11th |
|---|---|---|---|---|---|
| Under 250 Entrants | 8,957 | 1 | 39% | 15% | 6% |
| 250 to 499 | 4,659 | 1 | 48% | 19% | 9% |
| 500 to 999 | 3,717 | 2 | 53% | 24% | 12% |
| 1,000 to 2,499 | 3,885 | 2 | 54% | 25% | 12% |
| 2,500 to 4,999 | 1,943 | 2 | 58% | 27% | 14% |
| 5,000 to 9,999 | 1,178 | 2 | 58% | 28% | 14% |
| 10,000 or more | 1,143 | 2 | 62% | 31% | 16% |

Most businesses run one campaign. A bigger first campaign goes with a better chance of a second, and even at 10,000 or more Entrants fewer than two in three came back. Read that as a reason to treat the first campaign as the start of a list the business keeps, since the second one is not guaranteed.
