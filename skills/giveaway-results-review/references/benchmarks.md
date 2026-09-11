# Benchmarks

The script ranks a campaign against every fifth percentile of twelve figures in `percentiles.json` (Entrants, Impressions (views of the campaign page), Conversion Rate, actions and entries per Entrant, entries, Entrants per day, action count, duration, stated Prize value per Entrant, email signups, share who signed up for email, referral entries per Entrant, follows by network), plus completions per Entrant for 51 Gleam actions, for all campaigns, the campaigns we can compare fairly, campaigns your size, and your vertical. The tables below give the typical figure and the reading guide.

Every figure is drawn from the campaigns behind these numbers (117,348 campaigns that reached 100 unique Entrants, crypto and purchase-only campaigns removed). Typical figures unless stated. The campaigns we can compare fairly have no repeatable action and a run of 14 days or less, because Impressions are unique per person per day.

## Campaign size

| Metric | Lower quarter | Typical | Upper quarter | Top tenth | Campaigns |
|---|---|---|---|---|---|
| Entrants | 225 | 492 | 1,293 | 3,349 | 117,130 |
| Entries | 883 | 2,320 | 6,719 | 17,968 | 117,130 |
| Entries per Entrant | 2.74 | 4.39 | 7.05 | 11.84 | 117,130 |
| Entries per 100 Entrants | 274 | 439 | 705 | 1,184 | 117,130 |
| Impressions | 862 | 2,033 | 5,608 | 16,452 | 117,041 |
| Duration in days | 7 | 14 | 29 | 36 | 117,130 |

Half of all campaigns sat between 225 and 1,293 Entrants, and the script compares a campaign against others in its own band.

| Comparison band | Campaigns | Businesses |
|---|---|---|
| 100 to 250 Entrants | 33,338 | 9,607 |
| 250 to 500 | 25,892 | 6,554 |
| 500 to 1,000 | 21,935 | 5,550 |
| 1,000 to 2,500 | 20,137 | 5,123 |
| 2,500 to 10,000 | 12,828 | 3,035 |
| 10,000 or more | 3,218 | 762 |

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

Completions of the acquire and amplify actions, summed per campaign, across the 117,348 campaigns behind these numbers that offered each. This is the closest the dataset comes to an outcome: an email signup completed is an address on the list, a follow completed is a follower at that moment. Unsubscribes, unfollows and list quality are not visible. Stated USD per completion divides the stated Prize pool by completions, for campaigns with every Prize valued in USD, and the stated value is what the organizer wrote.

Reading it: cost per completion varies widely by asset, from under $0.50 for an email signup to about $17 for a content submission (exact figures and sample sizes in the table below). Follows sit in between, roughly $0.4 to $0.9 depending on the network.

A subscribe asset's Share of Entrants column can read over 100: a campaign can offer more than one subscribe action, such as a newsletter and an SMS list, and every completion counts.

| Asset | Campaigns | Lower quarter | Typical | Upper quarter | Top tenth | Share of Entrants | Stated USD per completion (Campaigns) |
|---|---|---|---|---|---|---|---|
| X follows | 19,433 | 752 | 1,405 | 3,035 | 7,846 | 57 (0.57) | 0.51 (7,954) |
| Referral entries (Viral Share) | 16,018 | 168 | 337 | 718 | 1,334 | 12 (0.12) | 2.14 (8,013) |
| Email signups | 15,799 | 1,269 | 2,053 | 3,960 | 8,294 | 98 (0.98) | 0.31 (8,082) |
| Twitch follows | 5,998 | 973 | 1,738 | 3,557 | 9,187 | 68 (0.68) | 0.43 (2,327) |
| Discord joins | 5,734 | 552 | 955 | 1,796 | 3,842 | 41 (0.41) | 0.65 (2,379) |
| TikTok follows | 5,276 | 477 | 862 | 1,613 | 3,187 | 37 (0.37) | 0.92 (2,221) |
| Instagram follows | 2,750 | 800 | 1,456 | 2,828 | 6,354 | 61 (0.61) | 0.62 (1,309) |
| Telegram joins | 1,622 | 976 | 1,697 | 3,057 | 4,857 | 84 (0.84) | 0.68 (372) |
| App downloads | 1,501 | 550 | 943 | 1,860 | 3,950 | 36 (0.36) | 0.90 (645) |
| Facebook likes | 1,281 | 482 | 746 | 1,334 | 2,499 | 39 (0.39) | 0.79 (680) |
| YouTube subscribes | 1,111 | 915 | 1,494 | 2,365 | 3,994 | 80 (0.80) | 0.47 (312) |
| Comments | 1,060 | 347 | 547 | 1,063 | 2,557 | 32 (0.32) | 0.74 (526) |
| Content submissions | 1,024 | 40 | 202 | 810 | 1,935 | 6 (0.06) | 16.67 (432) |
| Spotify follows | 899 | 523 | 896 | 1,533 | 2,758 | 31 (0.31) | 0.80 (349) |
| Podcast subscribes | 865 | 458 | 873 | 1,833 | 3,713 | 35 (0.35) | 0.94 (313) |
| LinkedIn follows | 767 | 393 | 641 | 1,229 | 2,326 | 26 (0.26) | 2.07 (323) |
| Pinterest follows | 506 | 410 | 557 | 748 | 1,266 | 38 (0.38) | 0.50 (369) |
| Snapchat follows | 430 | 408 | 728 | 1,948 | 3,511 | 25 (0.25) | 1.56 (272) |
| Bluesky follows | 340 | 347 | 534 | 899 | 1,470 | 25 (0.25) | 0.85 (144) |
| Threads follows | 315 | 307 | 502 | 725 | 1,132 | 27 (0.27) | 0.61 (197) |

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
| Tech hardware | 2,658 | 0.37 |
| Gift card or cash | 1,644 | 0.35 |
| Game items or skins | 1,455 | 0.96 |
| Bundle or box | 1,416 | 0.42 |
| Home, garden, appliance | 721 | 0.40 |
| Regulated goods (firearms) | 685 | 0.36 |
| Placeholder Prize name | 673 | 0.38 |
| Other or unclassified | 572 | 0.50 |
| Experience, travel, tickets | 565 | 0.78 |
| Music gear | 528 | 0.14 |

## By start year

| Year | Campaigns | Entrants | Conversion Rate |
|---|---|---|---|
| 2020 | 454 | 2,685 | 27% |
| 2021 | 8,749 | 2,438 | 30% |
| 2022 | 7,602 | 2,201 | 30% |
| 2023 | 6,177 | 2,164 | 27% |
| 2024 | 5,088 | 2,117 | 24% |
| 2025 | 5,031 | 2,058 | 26% |
| 2026 | 2,531 | 2,060 | 27% |

The typical campaign has drifted smaller since 2021 while the Conversion Rate held steady. A campaign run this year sits a little under the typical figures across the whole export, at the same quality. The 2020 row rests on 454 campaigns against several thousand in every later year, so treat it as a rough marker.

## By template

Where a campaign was copied from, scoped to 100 or more Entrants, finance_crypto organizers excluded, so a review can compare a campaign against others built from the same template or the same source kind (across 117,346 campaigns, the four source kinds).

| Source | Share | Campaigns | Businesses | Conversion Rate |
|---|---|---|---|---|
| Own earlier campaign, copied | 62% | 21,973 | 2,710 | 0.270 |
| Blank, no copying | 23% | 8,167 | 3,432 | 0.307 |
| Gleam library template | 9% | 3,059 | 2,219 | 0.264 |
| A campaign outside the dataset | 7% | 2,458 | 1,268 | 0.273 |

Typical figures for the library templates with the most campaigns at this size:

| Template | Campaigns | Businesses | Entrants | Conversion Rate | Entries/Entrant | Days | Methods | Email offered | Share offered |
|---|---|---|---|---|---|---|---|---|---|
| Gleam Sweepstakes | 1,268 | 960 | 2,185.5 | 24.7% | 4.27 | 19 | 8 | 68% | 67% |
| Instant Entry | 271 | 217 | 2,079 | 37.7% | 2.15 | 15 | 3 | 15% | 13% |
| Email Signup | 173 | 143 | 2,125 | 30.8% | 2.09 | 18 | 4 | 93% | 63% |
| YouTube Contest | 170 | 137 | 2,190 | 29.6% | 4.19 | 21 | 7 | 19% | 54% |
| E-Commerce Giveaway | 114 | 106 | 2,412.5 | 25.2% | 4.38 | 22.5 | 8 | 90% | 91% |
| Refer A Friend | 102 | 92 | 1,808 | 26.3% | 2.52 | 24 | 4 | 41% | 92% |
| Contest Entry Form | 73 | 62 | 2,501 | 27.9% | 2.23 | 23 | 3 | 41% | 27% |
| Instagram Contest | 63 | 57 | 1,929 | 26.0% | 3.93 | 15 | 6 | 29% | 71% |
| Email Signup Referrals | 53 | 44 | 1,815 | 29.0% | 2.09 | 16 | 4 | 96% | 96% |
| eSports Streaming Giveaway | 36 | 34 | 2,303.5 | 30.2% | 4.61 | 19.5 | 7 | 17% | 39% |
| Promote Shopify Store | 33 | 31 | 1,764 | 21.4% | 4.10 | 20 | 8 | 79% | 85% |
| Photo Contest | 31 | 27 | 2,412 | 19.4% | 2.66 | 15 | 5 | 36% | 29% |

Source: `analysis/output/templates.json` (`source_mix_1k`, `by_template_1k`).

## Benchmarks by plan tier

A Free or Hobby organizer runs on a plan with no email or share action, so ranking that campaign against the Premium typical figure compares two different tools. Read a campaign against its own tier first, then against campaigns your size. Figures come from `field_cuts.json`'s own scope (100 or more Entrants, plausible start dates, no crypto or purchase-only exclusion), which is wider than the 117,348 campaigns behind the numbers above, so treat these as tier comparisons, not a restatement of the campaign-size table. Conversion Rate here is Entrants over Impressions on every run in the tier, not the campaigns we can compare fairly, so a tier with more long or repeatable campaigns reads lower for that reason alone.

| Tier | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Days | Methods | Email offered | Share offered |
|---|---|---|---|---|---|---|---|---|---|
| Free | 1,936 | 804 | 2,085 | 45% | 2.83 | 11 | 4 | 0% | 0% |
| Hobby | 2,501 | 841 | 1,833 | 37% | 3.80 | 13 | 5 | 0% | 2% |
| Pro | 29,173 | 6,947 | 2,272 | 30% | 4.98 | 13 | 8 | 30% | 60% |
| Business | 19,383 | 3,590 | 2,883 | 28% | 4.94 | 14 | 8 | 35% | 55% |
| Premium | 1,788 | 418 | 4,137 | 23% | 7.88 | 22 | 13 | 50% | 60% |

Free and Hobby campaigns carry no email or share action at all, so their Conversion Rate sits above Pro and Business on a smaller ask, not a stronger landing page. Premium campaigns run the most methods over the longest window and the lowest Conversion Rate follows from the duration and repeatable-action caveat, not from a weaker campaign.

## Benchmarks by organizer stage, scale and business type

For picking a comparison group closer than campaigns your size: how established the business is, how big the organization is, what kind of business it runs, and its industry. Figures come from `industries.json`, whose scope is campaigns with 100 or more Entrants and a labelled organizer site, also wider than the 117,348 campaigns behind the numbers above (it keeps crypto, which is the largest single industry, and applies no purchase-only exclusion). Conversion Rate is Entrants over Impressions on every run, same caveat as the tier table above.

By organizer stage (`by_org_stage`), read from the homepage:

| Stage | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Email offered |
|---|---|---|---|---|---|---|
| Small business | 20,470 | 3,580 | 2,178 | 28% | 4.38 | 51% |
| Startup | 14,661 | 4,088 | 2,980 | 30% | 5.86 | 14% |
| Mid market | 6,813 | 815 | 2,447 | 28% | 4.06 | 30% |
| Enterprise | 2,902 | 280 | 2,521 | 31% | 4.51 | 31% |
| Individual | 1,792 | 426 | 1,766 | 32% | 5.58 | 16% |
| Public body | 323 | 100 | 2,070 | 31% | 2.86 | 46% |

By organization scale (`by_org_scale`, from revenue, employee and traffic-rank signals):

| Scale | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Days |
|---|---|---|---|---|---|---|
| Micro | 12,415 | 5,377 | 2,366 | 30% | 5.27 | 15 |
| Small | 14,598 | 2,343 | 2,320 | 28% | 5.14 | 15 |
| Mid | 11,789 | 1,201 | 2,555 | 27% | 4.47 | 14 |
| Large | 6,941 | 405 | 2,451 | 34% | 4.17 | 8 |
| Enterprise | 1,914 | 186 | 2,789 | 32% | 5.15 | 14 |
| Shared platform page (YouTube, Twitch, X and the like) | 6,672 | 1,131 | 2,593 | 36% | 4.82 | 11 |

By business type (`by_business_type`, from what the organizer's homepage sells):

| Type | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Days | Email offered |
|---|---|---|---|---|---|---|---|
| Software | 18,311 | 4,205 | 2,960 | 31% | 5.59 | 9 | 12% |
| Brand | 11,380 | 2,578 | 2,145 | 26% | 4.54 | 16 | 50% |
| Retailer | 7,952 | 996 | 2,428 | 29% | 4.23 | 14 | 50% |
| Media or publisher | 5,556 | 703 | 2,054 | 29% | 4.26 | 19 | 49% |
| Creator | 4,175 | 1,026 | 2,313 | 38% | 4.19 | 13 | 8% |
| Community | 1,923 | 490 | 2,633 | 33% | 5.61 | 9 | 5% |
| Agency | 1,374 | 171 | 2,711 | 32% | 5.20 | 15 | 23% |
| Service business | 1,157 | 255 | 2,239 | 28% | 3.23 | 16 | 39% |
| Nonprofit | 265 | 94 | 2,077 | 28% | 3.04 | 28 | 40% |

By industry (`by_industry`), finance_crypto (15,796 campaigns) held out on the same crypto exclusion as the rest of this page:

| Industry | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Days | Email offered |
|---|---|---|---|---|---|---|---|
| Gaming and esports | 7,808 | 1,840 | 2,324 | 28% | 5.35 | 14 | 18% |
| Electronics and tech | 7,347 | 1,051 | 2,258 | 30% | 4.93 | 15 | 24% |
| Media and entertainment | 5,115 | 637 | 2,066 | 26% | 4.53 | 21 | 65% |
| Sports and outdoors | 2,300 | 546 | 2,470 | 24% | 4.40 | 22 | 56% |
| Apparel and fashion | 1,815 | 331 | 2,676 | 30% | 2.74 | 8 | 74% |
| Food and drink | 1,803 | 425 | 2,399 | 29% | 3.54 | 18 | 63% |
| Home and garden | 1,784 | 334 | 2,240 | 31% | 3.82 | 16 | 59% |
| Travel and events | 1,384 | 275 | 2,745 | 29% | 3.02 | 23 | 55% |
| Software and SaaS | 1,281 | 270 | 2,442 | 34% | 5.25 | 11 | 25% |
| Automotive | 1,133 | 144 | 2,741 | 23% | 6.38 | 18 | 68% |
| Toys, hobbies and collectibles | 1,000 | 208 | 1,838 | 26% | 3.55 | 20 | 42% |
| Health, wellness and fitness | 926 | 214 | 1,786 | 27% | 4.11 | 21 | 38% |
| Retail and marketplace | 857 | 134 | 2,288 | 28% | 2.37 | 8 | 25% |
| Marketing agency | 559 | 82 | 2,995 | 33% | 4.90 | 16 | 25% |
| Art and crafts | 489 | 118 | 1,932 | 25% | 5.08 | 17 | 42% |
| Education | 453 | 124 | 1,913 | 26% | 4.14 | 14 | 37% |
| Pets | 391 | 89 | 1,756 | 27% | 3.67 | 17 | 79% |
| Beauty and personal care | 342 | 115 | 1,689 | 33% | 3.18 | 19 | 54% |
| Local services | 319 | 56 | 2,197 | 27% | 4.14 | 14 | 14% |
| Baby and kids | 311 | 71 | 1,992 | 30% | 3.18 | 15 | 53% |
| Creator or influencer | 216 | 81 | 3,361 | 28% | 4.51 | 10 | 26% |
| Jewelry and watches | 137 | 65 | 2,225 | 26% | 3.51 | 22 | 71% |
| Nonprofit or community | 134 | 57 | 2,069 | 32% | 2.57 | 16 | 42% |

This industry cut reads the organizer's own homepage, and so do `percentiles.json`'s groups since the  rebuild: the ten vertical names `review.py` accepts (gaming, technology, fashion_beauty and the rest) fold the homepage labels together (fashion_beauty is apparel, beauty and jewellery, kids_family_pets is baby, pets and toys), and every label with five organizers also has its own `industry:` group. Conversion Rate by vertical sits in a narrow band (table below, 117,348 campaigns). Say which cut a rank came from.

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

`industries.json`'s `by_employee_band` and `by_founded_band` add a company headcount and company age cut, matched against Apollo's own organization data, not read from the homepage. Same 1,000-or-more scope as the tables above. Apollo matched 3,609 of the organizers here, about a third of the 11,225 organizers with an industry label, and the match skews toward companies with a public web presence, so read this as a lean on the larger and more established end, not a full comparison across every business.

| Employee count | Campaigns | Businesses | Conversion Rate | Email offered |
|---|---|---|---|---|
| 1 to 9 | 9,894 | 1,260 | 27.3% | 38% |
| 10 to 49 | 9,336 | 916 | 26.5% | 50% |
| 50 to 199 | 4,859 | 430 | 30.7% | 40% |
| 200 to 999 | 4,325 | 218 | 33.7% | 24% |
| 1,000 or more | 4,412 | 295 | 33.8% | 25% |

Organizers with 200 or more staff see a higher Conversion Rate than organizers under 50 staff, while running an email action about half as often (table above). The smaller organizer gets the useful half of that trade: a lower Conversion Rate on this one run, but an email list built on close to twice the share of campaigns, the asset that keeps paying out after the giveaway itself has closed.

`by_founded_band` shows a related split by company age: the newest companies offer email far less often than older ones, while running the highest entries per Entrant and referral rate of the five groups (table below, 3,936 campaigns, 513 organizers).

| Founded | Email offered | Entries per Entrant | Referral rate |
|---|---|---|---|
| 2020 or later | 21.5% | 5.76 | 84% of Entrants |
| Before 2015 (four earlier bands) | 35% to 46% | — | — |

Company size, company age, plan tier and organizer scale move together, so read this as another angle on the pattern in the tables above, not a separate driver.

Source: `analysis/output/industries.json` (`by_employee_band`, `by_founded_band`, `enrichment_coverage`).

## Campaign sequence and organizer activity

Where the organizer sits in their own run of campaigns, from `field_cuts.json`'s `by_campaign_sequence` and `by_organizer_active`:

| Sequence | Campaigns | Businesses | Entrants | Conversion Rate | Days |
|---|---|---|---|---|---|
| 1st campaign | 25,482 | 25,482 | 433 | 26% | 15 |
| 2nd to 3rd | 20,660 | 12,314 | 484 | 27% | 14 |
| 4th to 10th | 29,232 | 6,452 | 539 | 28% | 12 |
| 11th plus | 91,694 | 2,531 | 520 | 30% | 9 |

| Organizer activity | Campaigns | Businesses | Entrants | Conversion Rate | Days |
|---|---|---|---|---|---|
| Ran another campaign in the last 12 months | 24,708 | 1,986 | 2,324 | 29% | 15 |
| Has not, in this export | 30,078 | 8,728 | 2,559 | 30% | 12 |

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

| Position in sequence (1,000 to 2,499 Entrants) | Entrants | Entries per Entrant | Organizers |
|---|---|---|---|
| 1st | 1,483 | 3.94 | 2,658 |
| 3rd to 10th | ~900 | — | — |
| 11th or more | 662 | 6.10 | 377 |

| Transition | Typical change in Entrants |
|---|---|
| 1st to 2nd | -4.0% |
| 11th-plus | -0.4% |

None of this says a second or third campaign will not grow, and it is not a reason to stop after one. What it rules out is treating the campaign count itself as the lever: running more of them, on its own, carries no guaranteed lift. The line below on continuers shows where the real lever sits, in what the organizer sets up before the next campaign even launches, Prize, entry mix, timing and promotion, the design choices this skill and `giveaway-entry-method-planner`, `giveaway-timing-and-duration` and `giveaway-promotion-plan` cover.

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
| 3 years or more | 19,034 | 2,013 | 28% | 41% |
| 1 to 3 years | 12,992 | 2,499 | 32% | 29% |
| 6 to 12 months | 6,437 | 1,939 | 31% | 21% |
| 1 to 6 months | 9,011 | 3,475 | 31% | 20% |
| 1 to 4 weeks | 3,287 | 2,487 | 30% | 24% |
| Under 1 week | 3,273 | 3,032 | 29% | 21% |

Conversion Rate barely moves across site age (table above). Email offered moves the most: an established site (three years or more) carries an email action about twice as often as a site under a year old.

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

Japan runs the highest plan-tier mix of the twelve, 61% of campaigns on Business or above, against 9% for Brazil. Brazil's one-day typical duration lines up with its 59% Conversion Rate, both marks of a short flash-style campaign.

### City benchmarks

`field_cuts.json`'s `by_organizer_city` adds a city cut of the same shape, scoped like the rest of this page to 100 or more Entrants. Every row already carries five or more organizers. The eight cities with the most campaigns, for a finer comparison when one fits:

| City | Campaigns | Businesses | Entrants | Conversion Rate | Entries/Entrant | Days | Methods |
|---|---|---|---|---|---|---|---|
| Singapore | 1,614 | 145 | 2,682 | 37% | 4.58 | 6 | 6 |
| Los Angeles, United States | 1,216 | 240 | 1,997 | 26% | 4.79 | 14 | 8 |
| Hanoi, Vietnam | 786 | 219 | 6,500 | 34% | 6.46 | 9 | 9 |
| Taipei, Taiwan | 750 | 37 | 3,089 | 35% | 6.53 | 7 | 9 |
| Ho Chi Minh City, Vietnam | 723 | 201 | 4,002 | 32% | 5.88 | 12 | 8 |
| Sydney, Australia | 710 | 204 | 2,212 | 29% | 3.54 | 22 | 6 |
| Tokyo, Japan | 702 | 79 | 2,126 | 27% | 6.00 | 8 | 8 |
| Melbourne, Australia | 700 | 171 | 2,072 | 28% | 3.41 | 19 | 7 |

Source: `analysis/output/country_cuts.json` (`by_country`), `analysis/output/indicators.json` (`impressions_per_contestant_by_country`, `plan_tier_by_country`), `analysis/output/field_cuts.json` (`by_organizer_city`).

## Every size band

`field_cuts.json`'s `by_band_all` covers every campaign with a contestant count, so each band has its own benchmark row. Counts are exact: the contestant dump covers the 100 to 1,000 range, so nothing here is modelled.

| Size | Campaigns | Businesses | Entrants | Conversion Rate | Entries per Entrant | Days | Methods | Email offered | Share offered |
|---|---|---|---|---|---|---|---|---|---|
| 100 to 250 | 47,150 | 13,254 | 160 | 27% | 4.46 | 9 | 6 | 17% | 30% |
| 250 to 500 | 35,627 | 9,067 | 350 | 28% | 4.92 | 11 | 7 | 22% | 42% |
| 500 to 1,000 | 29,505 | 7,649 | 690 | 28% | 4.98 | 11 | 7 | 28% | 46% |
| 1,000 to 2,500 | 27,891 | 7,404 | 1,496 | 29% | 4.72 | 13 | 7 | 32% | 50% |
| 2,500 to 10,000 | 20,532 | 5,375 | 4,124 | 30% | 4.95 | 14 | 8 | 30% | 56% |
| 10,000 or more | 6,363 | 1,989 | 16,706 | 34% | 5.28 | 14 | 8 | 23% | 61% |

Entries per Entrant barely moves across the whole range, from 4.46 in the smallest band to 5.28 in the largest. The Entrants a small campaign does reach are working about as hard as the ones in a campaign a hundred times the size, so a low Entrant count is a reach problem and not an engagement problem.

Conversion Rate climbs gently with size, from 27% to 34%. Email and a share action are both offered far less often in small campaigns, 17% against 23% for email and 30% against 61% for sharing. Those are the two gaps a small campaign can close on its own, and the target is the next band's own figure.

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

- Two more comparisons among the campaigns we can compare fairly: a campaign launched within 30 days of the organizer's previous one converts noticeably better than a first campaign despite drawing about the same number of Entrants, and a campaign without a share action converts better than one with, while also drawing more Entrants (table below).

| Top fifth vs bottom fifth (by Entrants) | Top fifth | Bottom fifth |
|---|---|---|
| Impressions | 35,505 | 4,047 |
| Conversion Rate | 28% | 28% |
| Stated Prize pool (USD) | 2,016 | 400 |
| Previous campaigns from organizer | 13 | 13 |

| Split (campaigns we can compare fairly) | Entrants | Conversion Rate |
|---|---|---|
| Within 30 days of previous campaign | 2,109 | 41% |
| First campaign | 2,025 | 32% |
| Share action offered | 1,871 | 31% |
| No share action | 2,236 | 41% |

The share-action line and the top-fifth line answer different questions and cannot be read as one finding. The share-action line splits campaigns by a setting the organizer chose before launch. The top-fifth line splits the same campaigns by the result they got afterwards. Neither says that adding or removing a share action moves a campaign between the fifths.

- December: about 12% of starts, and December campaigns drew more Entrants and had a higher Conversion Rate.
