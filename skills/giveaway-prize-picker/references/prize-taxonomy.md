# Prize taxonomy

Categories were built from Prize names, campaign names and descriptions in the dataset, then refined against what the listings contained. Classification is by pattern matching on the Prize name, with campaign context for the segment decision. These labels are our inference. The business never chose them. Figures are for the campaigns behind these numbers (117,348 campaigns, 172,645 Prize listings, 17,777 businesses) after excluding crypto, ambiguous and purchase-opportunity campaigns. "Value stated" is the share of listings with a non-null, non-zero value. USD figures are typical values, using stated USD values only.

<!-- generated:taxonomy -->
| Category | What it covers | Prize records | Campaigns | Organizers | Value stated | Stated USD median (n) |
|---|---|---|---|---|---|---|
| Tech hardware | PCs, GPUs, consoles, phones, peripherals, monitors, audio, smart devices | 30,188 | 22,137 | 4,938 | 34% | 299 (10,082) |
| Gift card or cash | Store gift cards, vouchers, cash, store credit, shopping sprees | 22,963 | 17,927 | 4,514 | 56% | 50 (12,845) |
| Game items or skins | Game keys and copies, in-game currency, cosmetic skins, editions | 17,194 | 11,228 | 2,730 | 37% | 56 (6,310) |
| Bundle or box | Packs, kits, setups, boxes, partner bundles, mystery boxes | 16,071 | 13,410 | 3,944 | 40% | 175 (6,333) |
| Experience, travel, tickets | Trips, stays, cruises, event tickets, concerts, guided experiences | 7,165 | 6,321 | 1,925 | 29% | 400 (2,101) |
| Merch, apparel, collectibles | Signed items, jerseys, hoodies, sneakers, bags, replicas, comics | 6,728 | 5,548 | 1,838 | 30% | 50 (2,011) |
| Home, garden, appliance | Grills, kitchen appliances, furniture, decor, power stations, wellness devices | 2,830 | 2,452 | 913 | 45% | 200 (1,283) |
| Toys and collectibles | LEGO, figures, statues, plush, board games | 2,524 | 2,297 | 474 | 17% | 58 (416) |
| Subscription or membership | Annual plans, lifetime memberships, a year of a product, courses | 2,157 | 1,637 | 882 | 47% | 150 (1,020) |
| Regulated goods (firearms) | Firearms, ammunition, parts and optics, from specialist retailers | 1,770 | 1,579 | 329 | 63% | 1,118 (1,116) |
| Food, drink, consumables | Food, drink, supplements, a year's supply of consumables | 1,591 | 1,468 | 608 | 37% | 190 (588) |
| Sports and outdoor gear | Fitness, bikes, fishing, hunting gear, camping, archery, EDC knives | 1,562 | 1,366 | 654 | 52% | 299 (804) |
| Discount or coupon | Discount codes, coupons, cashback. Requires a purchase, so a weak prize | 1,352 | 1,054 | 348 | 34% | 100 (465) |
| Beauty and wellness | Skincare, grooming, wellness products | 895 | 815 | 310 | 45% | 150 (403) |
| Vehicle | Cars, trucks, motorcycles, e-bikes, outboard motors | 803 | 733 | 369 | 58% | 699 (468) |
| Tools, craft, DIY | Power tools, 3D printers and filament, crafting machines, epoxy | 790 | 581 | 203 | 45% | 209 (353) |
| Exclusive access | Beta keys, playtests, creator interaction, community roles | 587 | 535 | 332 | 20% | 200 (119) |
| Music gear | Guitars, pianos, pedals, recording equipment | 573 | 452 | 175 | 45% | 399 (256) |
| Art and custom | Artwork, prints, commissions | 217 | 185 | 112 | 32% | 73 (70) |
| Bullion | Silver and gold bars, rounds, coins | 26 | 25 | 13 | 38% | 750 (9) |
| Placeholder name | "1st Prize", "Winner", a campaign title reused: the record does not say what the prize was | 7,859 | 5,696 | 1,292 | 26% | 200 (2,023) |
| Unclassified | Neither rules nor the label pass could place them (opaque brand codes, ambiguous short names) | 46,800 | 34,953 | 8,748 | 34% | 120 (15,943) |

Categories were assigned in two passes: name-pattern rules (172,645 records) and, only where rules failed, a private LLM-assisted label pass over the leftover names (0 records). Small categories are listed for completeness and are too thin to benchmark.
<!-- /generated -->

## Category performance

A campaign-level cut on the same campaigns behind these numbers, one row per campaign. The counts below sit a little under the listing-level counts in the table above. Every category here clears 30 campaigns and 10 businesses. Conversion Rate (the share of people who saw it and entered) is one of the columns.

<!-- generated:px_category -->
| Category | Campaigns | Businesses | Typical Entrants | Conversion Rate | Actions per Entrant | Methods | Email offered |
|---|---|---|---|---|---|---|---|
| Unclassified | 31,365 | 7,678 | 403 | 28% | 4.2 | 6 | 30% |
| Tech hardware | 20,271 | 4,514 | 926 | 28% | 5.0 | 8 | 24% |
| Gift card or cash | 15,812 | 3,747 | 420 | 24% | 4.7 | 8 | 36% |
| Bundle or box | 11,756 | 3,317 | 476 | 27% | 4.4 | 7 | 41% |
| Game items or skins | 10,168 | 2,427 | 341 | 25% | 5.1 | 8 | 24% |
| Experience, travel, tickets | 5,934 | 1,736 | 392 | 25% | 3.2 | 6 | 45% |
| Placeholder name | 5,199 | 1,158 | 544 | 34% | 4.3 | 6 | 20% |
| Merch, apparel, collectibles | 4,282 | 1,232 | 466 | 27% | 3.6 | 6 | 45% |
| Toys and collectibles | 2,120 | 391 | 406 | 26% | 4.0 | 7 | 37% |
| Home, garden, appliance | 2,038 | 696 | 895 | 31% | 4.0 | 7 | 46% |
| Regulated goods (firearms) | 1,473 | 276 | 2,177 | 19% | 8.2 | 11 | 60% |
| Food, drink, consumables | 1,269 | 503 | 655 | 30% | 3.6 | 6 | 58% |
| Subscription or membership | 1,176 | 616 | 370 | 24% | 3.8 | 6 | 38% |
| Sports and outdoor gear | 1,072 | 498 | 764 | 27% | 4.0 | 6 | 50% |
| Beauty and wellness | 748 | 257 | 472 | 28% | 4.3 | 8 | 44% |
| Vehicle | 652 | 327 | 854 | 22% | 4.2 | 6 | 45% |
| Discount or coupon | 539 | 141 | 489 | 40% | 4.5 | 7 | 11% |
| Exclusive access | 463 | 277 | 346 | 28% | 3.9 | 5 | 18% |
| Tools, craft, DIY | 449 | 155 | 793 | 28% | 3.9 | 7 | 39% |
| Music gear | 402 | 155 | 1,277 | 27% | 3.6 | 6 | 61% |
| Art and custom | 141 | 80 | 355 | 32% | 3.1 | 5 | 42% |
<!-- /generated -->

Home, garden, appliance and food, drink, consumables lead the categories with real size on Conversion Rate. Music gear and food, drink, consumables offer email most often. Regulated goods ties for the most Entry Methods but has the lowest Conversion Rate (17%), consistent with the eligibility friction that category carries. Discount or coupon has the highest Conversion Rate of all (50%), on a typical two-day run that fits a promotion with a form more than a Prize people wait for.

The two or three Prize categories businesses reach for most, by industry:

| Industry | Most common categories (share of the industry's campaigns) |
|---|---|
| Electronics and tech | Tech hardware (61%, 4,399 campaigns), Other or unclassified (20%, 1,426 campaigns), Bundle or box (5%, 379 campaigns) |
| Gaming and esports | Tech hardware (35%, 2,208 campaigns), Game items or skins (23%, 1,458 campaigns), Other or unclassified (19%, 1,194 campaigns) |
| Media and entertainment | Tech hardware (31%, 1,513 campaigns), Other or unclassified (22%, 1,091 campaigns), Bundle or box (16%, 771 campaigns) |
| Sports and outdoors | Other or unclassified (27%, 606 campaigns), Regulated goods (firearms) (21%, 460 campaigns), Bundle or box (13%, 296 campaigns) |
| Food and drink | Other or unclassified (19%, 318 campaigns), Bundle or box (17%, 280 campaigns), Gift card or cash (14%, 239 campaigns) |
| Home and garden | Other or unclassified (30%, 494 campaigns), Home, garden, appliance (25%, 417 campaigns), Bundle or box (13%, 222 campaigns) |
| Apparel and fashion | Merch, apparel, collectibles (39%, 629 campaigns), Gift card or cash (23%, 377 campaigns), Other or unclassified (18%, 288 campaigns) |
| Travel and events | Experience, travel, tickets (55%, 687 campaigns), Other or unclassified (18%, 220 campaigns), Gift card or cash (14%, 176 campaigns) |
| Automotive | Regulated goods (firearms) (37%, 392 campaigns), Other or unclassified (24%, 259 campaigns), Gift card or cash (13%, 140 campaigns) |
| Toys, hobbies and collectibles | Toys and collectibles (38%, 322 campaigns), Other or unclassified (25%, 207 campaigns), Bundle or box (14%, 115 campaigns) |

Gaming and esports splits its Prizes three ways (hardware, game items, other) where electronics and tech and travel and events each concentrate on one category. Automotive's regulated-goods share (37%, 392 campaigns) sits on only 12 businesses, at the floor for a figure this skill quotes, and reads as a handful of firearms retailers labelled automotive, not a general pattern for cars.

Source: `analysis/output/prize_timing_cuts.json` (by_prize_category, prize_category_by_industry).

## Ticket Prizes

Experience, travel, tickets is one category in the table above, but the ticket types inside it price and draw viewers differently enough to choose between. A listing-level cut on Prizes classified as a specific ticket kind. Every row below clears 30 campaigns and 10 businesses.

| Ticket kind | Campaigns | Businesses | Typical USD per Winner | Conversion Rate | Multi-Winner share | Actions per Entrant |
|---|---|---|---|---|---|---|
| Concert tickets | 222 | 105 | 774 | 28% | 16% | 4.33 |
| Festival tickets | 115 | 59 | 950 | 24.6% | 24% | 4.27 |
| Sports tickets | 179 | 122 | 329 | 25% | 26% | 3.93 |
| Event passes | 95 | 22 | 1,500 | 24% | 12% | 3.11 |
| Flights or hotel | 695 | 313 | 1,810 | 29% | 7% | 2.97 |

Flights or hotel packages are the priciest ticket Prize (1,810 USD per Winner) and the least likely to go to more than one Winner. Sports tickets sit at the other end on price and are the most likely of the five to go multi-Winner. Concert and flights or hotel Prizes have the highest Conversion Rate of the group, festival and event passes the lowest. Actions per Entrant falls as the Prize gets more expensive and travel-shaped, highest for concert tickets and lowest for flights or hotel, in line with the low actions-per-Entrant pattern for the wider experience, travel, tickets category.

Source: `analysis/output/prize_timing_cuts.json` (winners_by_ticket_kind).

## Cross-cutting flags

- **Own product** (inferred): a Prize name sharing a distinctive word with the business's name. 18.5% of Prize listings across the campaigns behind these numbers carry this weak signal. It under-counts (a bakery giving away "a cake" does not match) and over-counts (a channel named after a phone brand), so treat it as directional only.
- **Complementary or partner product**: undetectable from names alone, but visible in descriptions as "teamed up with", "courtesy of", "sponsored by". Common in bundles and streamer campaigns.
- **Digital rewards**: game items, subscriptions and gift codes overlap. Digital delivery removes shipping cost and adds region-lock and account questions.

## Segments kept out of the benchmark

The crypto rule needs two or more strong signals among: wallet-address Entry Method, a crypto currency code on a Prize, crypto terms in the Prize or campaign name (airdrop, NFT, whitelist, IDO, token sale, exchange and chain names, stablecoin symbols), "$N in NAME" wording, amount plus a known ticker, or dense crypto terms in the description. One strong signal alone, weak signals only, or a label-pass flag put a campaign in the ambiguous bucket. Purchase opportunity covers sneaker raffles whose Prize is the right to buy (by wording, or Prize listings that are shoe sizes).

<!-- generated:segments -->
| Segment | Campaigns | Handling |
|---|---|---|
| Ordinary | 117,348 (172,645 prize records, 17,777 organizers) | Basis for every default figure |
| Crypto | 6,288 | Excluded. Described only when a user asks for crypto advice. 38% used a wallet-address entry method |
| Purchase opportunity | 262 | Excluded. The prize is the right to buy something |

Excluded campaigns are similar in size to ordinary ones (crypto median 732 contestants versus 492 ordinary), so exclusion changes who is in the benchmark and leaves the size distribution alone.
<!-- /generated -->

Any claim that crypto campaigns inflate a benchmark remains a hypothesis.

## Using the taxonomy

Pick the category that matches the objective first, then choose the item:

- Leads or sales in a niche: own product, store credit, category bundle, membership.
- Discount codes and coupons appear as Prizes in 438 campaigns. They require a purchase, so treat them as a promotion with an entry form, and use them as a consolation tier under a real Prize if at all.
- Hobby and home audiences: category gear (sports, music, tools, home) selects for the audience in a way generic electronics cannot.
- Reach or launch awareness: hardware or gift card tied to the brand, or the launched product itself.
- Community and UGC: merch, signed items, exclusive access, experiences with the team.
- Retention: subscription extensions, credit, early access.

Regulated goods (firearms, alcohol, tobacco, gambling-adjacent items) are recorded in the data but are not used as examples. If a user sells them, the accessibility and legal criteria dominate and local counsel is required.
