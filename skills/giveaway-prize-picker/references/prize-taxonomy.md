# Prize taxonomy

Categories were built from Prize names, campaign names and descriptions in the dataset, then refined against what the listings contained. Classification is by pattern matching on the Prize name, with campaign context for the segment decision. These labels are our inference. The business never chose them. Figures are for the campaigns behind these numbers (116,499 campaigns, 170,599 Prize listings, 17,633 businesses) after excluding crypto, ambiguous and purchase-opportunity campaigns. "Value stated" is the share of listings with a non-null, non-zero value. USD figures are typical values, using stated USD values only.

<!-- generated:taxonomy -->
| Category | What it covers | Prize records | Campaigns | Organizers | Value stated | Stated USD median (n) |
|---|---|---|---|---|---|---|
| Tech hardware | PCs, GPUs, consoles, phones, peripherals, monitors, audio, smart devices | 30,098 | 22,080 | 4,926 | 33% | 299 (10,032) |
| Gift card or cash | Store gift cards, vouchers, cash, store credit, shopping sprees | 28,897 | 22,648 | 5,278 | 52% | 60 (14,906) |
| Game items or skins | Game keys and copies, in-game currency, cosmetic skins, editions | 17,038 | 11,226 | 2,743 | 36% | 57 (6,208) |
| Bundle or box | Packs, kits, setups, boxes, partner bundles, mystery boxes | 15,311 | 12,783 | 3,789 | 40% | 170 (6,046) |
| Experience, travel, tickets | Trips, stays, cruises, event tickets, concerts, guided experiences | 6,853 | 6,050 | 1,861 | 29% | 399 (1,964) |
| Merch, apparel, collectibles | Signed items, jerseys, hoodies, sneakers, bags, replicas, comics | 6,412 | 5,257 | 1,806 | 30% | 50 (1,952) |
| Home, garden, appliance | Grills, kitchen appliances, furniture, decor, power stations, wellness devices | 2,922 | 2,534 | 895 | 44% | 200 (1,286) |
| Toys and collectibles | LEGO, figures, statues, plush, board games | 2,495 | 2,267 | 470 | 16% | 55 (400) |
| Subscription or membership | Annual plans, lifetime memberships, a year of a product, courses | 2,057 | 1,560 | 848 | 47% | 149 (967) |
| Regulated goods (firearms) | Firearms, ammunition, parts and optics, from specialist retailers | 1,690 | 1,510 | 323 | 62% | 1,178 (1,051) |
| Sports and outdoor gear | Fitness, bikes, fishing, hunting gear, camping, archery, EDC knives | 1,498 | 1,303 | 630 | 51% | 300 (765) |
| Food, drink, consumables | Food, drink, supplements, a year's supply of consumables | 1,475 | 1,359 | 568 | 37% | 180 (550) |
| Discount or coupon | Discount codes, coupons, cashback. Requires a purchase, so a weak prize | 1,344 | 1,046 | 344 | 34% | 100 (464) |
| Tools, craft, DIY | Power tools, 3D printers and filament, crafting machines, epoxy | 814 | 613 | 227 | 44% | 180 (359) |
| Beauty and wellness | Skincare, grooming, wellness products | 804 | 727 | 286 | 49% | 111 (395) |
| Vehicle | Cars, trucks, motorcycles, e-bikes, outboard motors | 725 | 662 | 342 | 59% | 649 (429) |
| Exclusive access | Beta keys, playtests, creator interaction, community roles | 572 | 520 | 321 | 20% | 200 (116) |
| Music gear | Guitars, pianos, pedals, recording equipment | 568 | 447 | 173 | 45% | 399 (255) |
| Art and custom | Artwork, prints, commissions | 208 | 178 | 106 | 32% | 99 (67) |
| Bullion | Silver and gold bars, rounds, coins | 24 | 23 | 12 | 38% | 1,041 (8) |
| Placeholder name | "1st Prize", "Winner", a campaign title reused: the record does not say what the prize was | 7,463 | 5,087 | 1,254 | 26% | 200 (1,950) |
| Unclassified | Neither rules nor the label pass could place them (opaque brand codes, ambiguous short names) | 41,331 | 31,413 | 8,165 | 35% | 129 (14,409) |

Categories were assigned in two passes: name-pattern rules (170,599 records) and, only where rules failed, a private LLM-assisted label pass over the leftover names (0 records). Small categories are listed for completeness and are too thin to benchmark.
<!-- /generated -->

## Category performance

A campaign-level cut on the same campaigns behind these numbers, one row per campaign. The counts below sit a little under the listing-level counts in the table above. Every category here clears 30 campaigns and 10 businesses. Conversion Rate (the share of people who saw it and entered) is one of the columns.

<!-- generated:px_category -->
| Category | Campaigns | Businesses | Typical Entrants | Conversion Rate | Entries per Entrant | Methods | Email offered |
|---|---|---|---|---|---|---|---|
| Unclassified | 28,097 | 7,132 | 413 | 28% | 4.2 | 6 | 30% |
| Tech hardware | 20,219 | 4,504 | 923 | 28% | 5.0 | 8 | 24% |
| Gift card or cash | 20,137 | 4,485 | 433 | 25% | 4.7 | 8 | 37% |
| Bundle or box | 11,188 | 3,177 | 470 | 27% | 4.4 | 7 | 41% |
| Game items or skins | 10,173 | 2,437 | 342 | 25% | 5.1 | 8 | 24% |
| Experience, travel, tickets | 5,676 | 1,675 | 380 | 25% | 3.2 | 6 | 44% |
| Placeholder name | 4,838 | 1,120 | 474 | 38% | 3.8 | 5 | 21% |
| Merch, apparel, collectibles | 4,011 | 1,207 | 446 | 28% | 3.4 | 5 | 42% |
| Home, garden, appliance | 2,109 | 676 | 804 | 32% | 4.2 | 7 | 49% |
| Toys and collectibles | 2,089 | 385 | 406 | 26% | 4.0 | 7 | 37% |
| Regulated goods (firearms) | 1,403 | 270 | 2,214 | 18% | 7.9 | 11 | 62% |
| Food, drink, consumables | 1,172 | 469 | 615 | 30% | 3.6 | 6 | 58% |
| Subscription or membership | 1,123 | 586 | 372 | 24% | 3.8 | 6 | 38% |
| Sports and outdoor gear | 1,021 | 480 | 771 | 27% | 4.0 | 6 | 48% |
| Beauty and wellness | 655 | 232 | 482 | 29% | 4.2 | 8 | 46% |
| Vehicle | 585 | 301 | 839 | 22% | 4.2 | 6 | 46% |
| Discount or coupon | 536 | 139 | 490 | 40% | 4.5 | 7 | 11% |
| Tools, craft, DIY | 463 | 168 | 745 | 29% | 3.9 | 6 | 39% |
| Exclusive access | 450 | 268 | 333 | 28% | 3.8 | 5 | 18% |
| Music gear | 399 | 155 | 1,243 | 26% | 3.6 | 6 | 61% |
| Art and custom | 136 | 76 | 358 | 33% | 3.2 | 6 | 40% |
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
