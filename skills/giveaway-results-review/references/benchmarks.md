# Benchmarks

Every figure is extracted from the ordinary segment of the export (37,180 campaigns that reached 1,000 unique entrants, crypto and purchase-only campaigns removed). Medians unless stated. The clean subset has no repeatable action and a run of 14 days or less, because impressions are unique per user per day.

## Campaign size

| Metric | p25 | Median | p75 | p90 | n |
|---|---|---|---|---|---|
| Unique contestants | 1,415 | 2,201 | 4,152 | 9,006 | 37,180 |
| Entries | 5,388 | 10,445 | 22,866 | 56,554 | 37,123 |
| Entries per contestant | 2.68 | 4.34 | 7.07 | 12.06 | 37,123 |
| Impressions | 4,751 | 9,073 | 19,661 | 45,590 | 37,148 |
| Duration in days | 8 | 16 | 31 | 43 | 37,180 |

Half of all campaigns sat between 1,000 and 2,500 contestants. Bands used by the script: 1k to 2.5k, 2.5k to 10k, 10k and over.

## Conversion by number of actions (clean subset)

| Actions | n | Contestants | Contestants per impression |
|---|---|---|---|
| 1 to 3 | 3,526 | 2,213 | 50% |
| 4 to 6 | 3,404 | 2,153 | 37% |
| 7 to 10 | 2,887 | 2,070 | 33% |
| 11 or more | 1,819 | 1,759 | 31% |

## Conversion by duration (no repeatable actions)

| Duration | n | Contestants | Contestants per impression |
|---|---|---|---|
| 1 to 7 days | 6,806 | 2,024 | 45% |
| 8 to 14 | 4,830 | 2,144 | 31% |
| 15 to 30 | 7,030 | 2,233 | 28% |
| 31 to 60 | 3,751 | 2,201 | 24% |
| 61 or more | 1,440 | 2,392 | 23% |

## Invalid entries (all ordinary)

| Invalid share | Share of campaigns |
|---|---|
| Under 1% | 25% |
| 1% to 5% | 32% |
| 5% to 20% | 35% |
| 20% or more | 7% |

Median 3.8%. Referral, Discord join, retweet and email actions ran higher. Validated-answer questions ran a median 17%.

## Action family uptake (completions per contestant, all ordinary)

| Family | Campaigns offering | Median | IQR |
|---|---|---|---|
| Visit a page or profile | 30,088 | 0.75 | 0.55 to 0.92 |
| Follow or subscribe (free) | 23,721 | 0.47 | 0.32 to 0.64 |
| Share, repost or refer | 21,093 | 0.22 | 0.10 to 0.42 |
| Email or newsletter signup | 16,077 | 0.89 | 0.69 to 1.02 |
| Post or create content | 5,756 | 0.24 | 0.08 to 0.38 |

A share entry is a referred person multiplied by entry worth, so the share row is not a click rate. Full family tables sit in the entry-method-planner skill.

## What campaigns produced (extracted)

Completions of the acquire and amplify actions, summed per campaign, across the 37,123 ordinary campaigns that offered each. This is the closest the export comes to an outcome: an email signup completed is an address on the list, a follow completed is a follower at that moment. Unsubscribes, unfollows and list quality are not visible. Stated USD per completion divides the stated prize pool by completions, for campaigns with every prize valued in USD, and the stated value is what the organizer wrote.

| Asset | Campaigns | p25 | Median | p75 | p90 | Per contestant | Stated USD per completion (n) |
|---|---|---|---|---|---|---|---|
| X follows | 20,440 | 768 | 1,448 | 3,157 | 8,163 | 0.59 | 0.51 (8,323) |
| Referral entries (Viral Share) | 16,708 | 171 | 349 | 764 | 1,463 | 0.13 | 2.10 (8,316) |
| Email signups | 16,015 | 1,272 | 2,054 | 3,967 | 8,305 | 0.98 | 0.31 (8,174) |
| Discord joins | 6,145 | 574 | 999 | 1,950 | 4,279 | 0.43 | 0.67 (2,483) |
| Twitch follows | 6,084 | 966 | 1,733 | 3,548 | 9,164 | 0.68 | 0.43 (2,338) |
| TikTok follows | 5,300 | 482 | 868 | 1,612 | 3,187 | 0.37 | 0.92 (2,199) |
| Instagram follows | 2,750 | 809 | 1,472 | 2,862 | 6,419 | 0.61 | 0.62 (1,272) |
| Telegram joins | 2,041 | 1,087 | 1,963 | 3,506 | 6,350 | 0.87 | 0.51 (497) |
| App downloads | 1,592 | 574 | 1,009 | 2,021 | 4,187 | 0.36 | 0.90 (710) |
| Facebook likes | 1,287 | 489 | 766 | 1,350 | 2,557 | 0.39 | 0.78 (662) |
| YouTube subscribes | 1,173 | 846 | 1,445 | 2,319 | 3,868 | 0.74 | 0.54 (366) |
| Content submissions | 1,109 | 34 | 186 | 781 | 1,903 | 0.06 | 20.00 (485) |
| Comments | 1,068 | 348 | 557 | 1,104 | 2,621 | 0.33 | 0.74 (517) |
| Spotify follows | 914 | 507 | 893 | 1,506 | 2,690 | 0.30 | 0.82 (354) |
| Podcast subscribes | 867 | 458 | 873 | 1,833 | 3,713 | 0.35 | 0.94 (314) |
| LinkedIn follows | 833 | 398 | 677 | 1,340 | 2,279 | 0.26 | 1.77 (360) |
| Pinterest follows | 556 | 412 | 554 | 745 | 1,232 | 0.36 | 0.59 (417) |
| Snapchat follows | 430 | 408 | 734 | 1,950 | 3,540 | 0.25 | 1.56 (270) |
| Bluesky follows | 337 | 360 | 543 | 900 | 1,487 | 0.25 | 0.83 (141) |
| Threads follows | 313 | 311 | 515 | 736 | 1,132 | 0.27 | 0.60 (192) |

By campaign size, email signups ran 1,047 to 1,787, median 1,346 | 2,773 to 5,397, median 3,703 | 11,650 to 28,765, median 16,344. Referral entries ran 119 to 446, median 224 | 300 to 980, median 520 | 898 to 3,241, median 1,643.

Reading it: the median campaign with an email action put about 2,000 addresses on the list for a stated prize cost near 0.31 USD each. Follows cost about 0.4 to 0.9 USD each depending on the network. A referral entry cost about 2 USD. A content submission cost about 20 USD and the median campaign collected 186.

Stated USD per email signup by prize category, campaigns with an email action:

| Prize category | Campaigns | Median USD per signup |
|---|---|---|
| Tech hardware | 2,113 | 0.29 |
| Gift card or cash | 1,229 | 0.28 |
| Bundle or box | 1,150 | 0.37 |
| Regulated goods (firearms) | 607 | 0.32 |
| Home, garden, appliance | 482 | 0.34 |
| Game items or skins | 460 | 0.60 |
| Experience, travel, tickets | 457 | 0.68 |
| Merch, apparel, collectibles | 371 | 0.37 |
| Music gear | 355 | 0.15 |
| Sports and outdoor gear | 323 | 0.43 |

## By start year

| Year | n | Contestants | Contestants per impression |
|---|---|---|---|
| 2020 | 461 | 2,685 | 27% |
| 2021 | 9,127 | 2,438 | 30% |
| 2022 | 8,161 | 2,201 | 30% |
| 2023 | 6,356 | 2,164 | 27% |
| 2024 | 5,262 | 2,117 | 24% |
| 2025 | 5,202 | 2,058 | 26% |
| 2026 | 2,516 | 2,060 | 27% |

The median campaign has drifted smaller since 2021 at a steady conversion. A campaign run this year sits a little under the whole-export medians at the same quality.

## Other reference points

- Top fifth against bottom fifth by contestants: 35,098 against 4,028 impressions at the same conversion (28% and 28%), stated prize pool 2,000 against 409 USD, previous campaigns 10 against 5.
- After a campaign of 5,000 or more contestants the next one reached 5,000 57% of the time. After a smaller one, 11%.

- Campaign within 30 days of the organizer's previous one: contestants 16% higher, conversion a third higher (clean subset).
- Share action offered: contestants 1,869 against 2,189 without, conversion 31% against 42% (clean subset).
- December: about 12% of starts, and December campaigns drew more entrants and converted better.
