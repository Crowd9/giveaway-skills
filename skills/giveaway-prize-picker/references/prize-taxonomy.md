# Prize taxonomy

Categories were built from Prize names, campaign names and descriptions in the dataset, then refined against what the listings contained. Classification is by pattern matching on the Prize name, with campaign context for the segment decision. These labels are our inference. The business never chose them. Figures are for the campaigns behind these numbers (116,499 campaigns, 170,599 Prize listings, 17,633 businesses) after excluding crypto, ambiguous and purchase-opportunity campaigns. "Value stated" is the share of listings with a non-null, non-zero value. USD figures are typical values, using stated USD values only.

<!-- generated:taxonomy -->
| Category | What it covers | Prize records | Campaigns | Organizers | Value stated | Stated USD median (n) |
|---|---|---|---|---|---|---|
| Tech hardware | PCs, GPUs, consoles, phones, peripherals, monitors, audio, smart devices | 30,102 | 22,080 | 4,926 | 33% | 299 (10,032) |
| Gift card or cash | Store gift cards, vouchers, cash, store credit, shopping sprees | 22,806 | 17,846 | 4,491 | 56% | 50 (12,769) |
| Game items or skins | Game keys and copies, in-game currency, cosmetic skins, editions | 17,168 | 11,203 | 2,722 | 37% | 56 (6,303) |
| Bundle or box | Packs, kits, setups, boxes, partner bundles, mystery boxes | 16,026 | 13,370 | 3,929 | 40% | 175 (6,320) |
| Experience, travel, tickets | Trips, stays, cruises, event tickets, concerts, guided experiences | 7,151 | 6,310 | 1,920 | 29% | 400 (2,096) |
| Merch, apparel, collectibles | Signed items, jerseys, hoodies, sneakers, bags, replicas, comics | 6,714 | 5,538 | 1,831 | 30% | 50 (2,008) |
| Home, garden, appliance | Grills, kitchen appliances, furniture, decor, power stations, wellness devices | 2,830 | 2,452 | 913 | 45% | 200 (1,283) |
| Toys and collectibles | LEGO, figures, statues, plush, board games | 2,523 | 2,296 | 474 | 17% | 58 (416) |
| Subscription or membership | Annual plans, lifetime memberships, a year of a product, courses | 2,150 | 1,631 | 877 | 48% | 150 (1,019) |
| Regulated goods (firearms) | Firearms, ammunition, parts and optics, from specialist retailers | 1,768 | 1,577 | 327 | 63% | 1,118 (1,115) |
| Food, drink, consumables | Food, drink, supplements, a year's supply of consumables | 1,591 | 1,468 | 608 | 37% | 190 (588) |
| Sports and outdoor gear | Fitness, bikes, fishing, hunting gear, camping, archery, EDC knives | 1,558 | 1,363 | 652 | 52% | 299 (803) |
| Discount or coupon | Discount codes, coupons, cashback. Requires a purchase, so a weak prize | 1,344 | 1,046 | 344 | 34% | 100 (464) |
| Beauty and wellness | Skincare, grooming, wellness products | 895 | 815 | 310 | 45% | 150 (403) |
| Vehicle | Cars, trucks, motorcycles, e-bikes, outboard motors | 798 | 728 | 368 | 59% | 699 (468) |
| Tools, craft, DIY | Power tools, 3D printers and filament, crafting machines, epoxy | 790 | 581 | 203 | 45% | 209 (353) |
| Exclusive access | Beta keys, playtests, creator interaction, community roles | 576 | 524 | 325 | 20% | 200 (118) |
| Music gear | Guitars, pianos, pedals, recording equipment | 573 | 452 | 175 | 45% | 399 (256) |
| Art and custom | Artwork, prints, commissions | 214 | 184 | 111 | 33% | 73 (70) |
| Bullion | Silver and gold bars, rounds, coins | 24 | 23 | 12 | 38% | 1,041 (8) |
| Placeholder name | "1st Prize", "Winner", a campaign title reused: the record does not say what the prize was | 7,781 | 5,623 | 1,277 | 26% | 200 (2,016) |
| Unclassified | Neither rules nor the label pass could place them (opaque brand codes, ambiguous short names) | 45,217 | 34,308 | 8,592 | 35% | 124 (15,671) |

Categories were assigned in two passes: name-pattern rules (170,599 records) and, only where rules failed, a private LLM-assisted label pass over the leftover names (0 records). Small categories are listed for completeness and are too thin to benchmark.
<!-- /generated -->

## Category performance

A campaign-level cut on the same campaigns behind these numbers, one row per campaign. The counts below sit a little under the listing-level counts in the table above. Every category here clears 30 campaigns and 10 businesses. Conversion Rate (the share of people who saw it and entered) is one of the columns.

<!-- generated:px_category -->
| Category | Campaigns | Businesses | Typical Entrants | Conversion Rate | Actions per Entrant | Methods | Email offered |
|---|---|---|---|---|---|---|---|
| Unclassified | 30,774 | 7,537 | 404 | 28% | 4.1 | 6 | 31% |
| Tech hardware | 20,220 | 4,504 | 923 | 28% | 5.0 | 8 | 24% |
| Gift card or cash | 15,754 | 3,730 | 420 | 24% | 4.7 | 8 | 36% |
| Bundle or box | 11,732 | 3,308 | 476 | 27% | 4.4 | 7 | 42% |
| Game items or skins | 10,147 | 2,421 | 340 | 25% | 5.0 | 8 | 24% |
| Experience, travel, tickets | 5,926 | 1,733 | 391 | 25% | 3.2 | 6 | 45% |
| Placeholder name | 5,130 | 1,145 | 544 | 34% | 4.3 | 6 | 20% |
| Merch, apparel, collectibles | 4,279 | 1,229 | 466 | 27% | 3.6 | 6 | 45% |
| Toys and collectibles | 2,120 | 391 | 406 | 26% | 4.0 | 7 | 37% |
| Home, garden, appliance | 2,038 | 696 | 895 | 31% | 4.0 | 7 | 46% |
| Regulated goods (firearms) | 1,471 | 274 | 2,177 | 19% | 8.2 | 12 | 60% |
| Food, drink, consumables | 1,269 | 503 | 655 | 30% | 3.6 | 6 | 58% |
| Subscription or membership | 1,173 | 613 | 368 | 24% | 3.8 | 6 | 38% |
| Sports and outdoor gear | 1,070 | 496 | 764 | 27% | 4.0 | 6 | 50% |
| Beauty and wellness | 748 | 257 | 472 | 28% | 4.3 | 8 | 44% |
| Vehicle | 647 | 326 | 854 | 22% | 4.2 | 6 | 46% |
| Discount or coupon | 536 | 139 | 490 | 40% | 4.5 | 7 | 11% |
| Exclusive access | 454 | 272 | 336 | 28% | 3.9 | 5 | 18% |
| Tools, craft, DIY | 449 | 155 | 793 | 28% | 3.9 | 7 | 39% |
| Music gear | 402 | 155 | 1,277 | 27% | 3.6 | 6 | 61% |
| Art and custom | 141 | 80 | 355 | 32% | 3.1 | 5 | 42% |
<!-- /generated -->

Among the categories with real size, home, garden, appliance and food, drink, consumables convert at 31% and 30%, behind placeholder Prize names at 34%. Music gear and regulated goods offer email most often, at 61% and 60%. Regulated goods runs the most Entry Methods at 11, three clear of the next highest, and has the lowest Conversion Rate at 19%, consistent with the eligibility friction that category carries. Discount or coupon has the highest Conversion Rate of all at 40%, on a typical seven-day run that fits a promotion with a form more than a Prize people wait for.

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

## Crowd per Prize dollar, by category

How much crowd a category draws for the money, against the typical campaign at the same stated value. 1.00 is typical for the money, so a category above it draws more crowd per dollar spent and one below it draws less.

<!-- generated:ev_crowd_category -->
| Category | Campaigns | Entrants | Crowd per Prize dollar | For the money |
|---|---|---|---|---|
| Regulated goods (firearms) | 1,577 | 2,107 | 2.04 | 104% above typical |
| Music gear | 452 | 1,306 | 1.91 | 91% above typical |
| Tech hardware | 22,019 | 898 | 1.42 | 42% above typical |
| Home, garden, appliance | 2,452 | 913 | 1.35 | 35% above typical |
| Tools, craft, DIY | 581 | 941 | 1.16 | 16% above typical |
| Food, drink, consumables | 1,467 | 694 | 1.14 | 14% above typical |
| Beauty and wellness | 815 | 472 | 1.11 | 11% above typical |
| Gift card or cash | 17,799 | 436 | 1.10 | 10% above typical |
| Sports and outdoor gear | 1,363 | 777 | 1.04 | 4% above typical |
| Vehicle | 728 | 802 | 1.04 | 4% above typical |
| Art and custom | 184 | 399 | 1.02 | typical |
| Placeholder name | 5,557 | 548 | 0.95 | 5% below typical |
| Bundle or box | 13,369 | 499 | 0.89 | 11% below typical |
| Toys and collectibles | 2,296 | 420 | 0.86 | 14% below typical |
| Unclassified | 34,246 | 424 | 0.82 | 18% below typical |
| Merch, apparel, collectibles | 5,538 | 497 | 0.79 | 21% below typical |
| Game items or skins | 11,195 | 362 | 0.75 | 25% below typical |
| Discount or coupon | 1,046 | 732 | 0.73 | 27% below typical |
| Exclusive access | 524 | 378 | 0.61 | 39% below typical |
| Experience, travel, tickets | 6,308 | 404 | 0.60 | 40% below typical |
| Subscription or membership | 1,630 | 422 | 0.53 | 47% below typical |
<!-- /generated -->

Any claim that crypto campaigns inflate a benchmark remains a hypothesis.

## Using the taxonomy

Pick the category that matches the objective first, then choose the item:

- Leads or sales in a niche: own product, store credit, category bundle, membership.
- Discount codes and coupons appear as Prizes in 1,054 campaigns. They require a purchase, so treat them as a promotion with an entry form, and use them as a consolation tier under a real Prize if at all.
- Hobby and home audiences: category gear (sports, music, tools, home) selects for the audience in a way generic electronics cannot.
- Reach or launch awareness: hardware or gift card tied to the brand, or the launched product itself.
- Community and UGC: merch, signed items, exclusive access, experiences with the team.
- Retention: subscription extensions, credit, early access.

Regulated goods (firearms, alcohol, tobacco, gambling-adjacent items) are recorded in the data but are not used as examples. If a user sells them, the accessibility and legal criteria dominate and local counsel is required.
