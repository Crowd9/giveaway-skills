# Prize taxonomy

Categories were built from prize names, campaign names and descriptions in the export, then refined against what the records contained. Classification is by regular expressions on the prize name, with campaign context for the segment decision. These labels are our inference. The organizer never chose them. Figures are for the ordinary segment (37,180 campaigns, 60,282 prize records, 6,817 organizers) after excluding crypto, ambiguous and purchase-opportunity campaigns. "Value stated" is the share of records with a non-null, non-zero value. USD medians use stated USD values only.

<!-- generated:taxonomy -->
| Category | What it covers | Prize records | Campaigns | Organizers | Value stated | Stated USD median (n) |
|---|---|---|---|---|---|---|
| Tech hardware | PCs, GPUs, consoles, phones, peripherals, monitors, audio, smart devices | 16,692 | 11,669 | 2,545 | 37% | 448 (6,100) |
| Gift card or cash | Store gift cards, vouchers, cash, store credit, shopping sprees | 6,852 | 5,062 | 1,766 | 53% | 150 (3,650) |
| Game items or skins | Game keys and copies, in-game currency, cosmetic skins, editions | 6,554 | 3,113 | 915 | 36% | 59 (2,369) |
| Bundle or box | Packs, kits, setups, boxes, partner bundles, mystery boxes | 5,374 | 4,226 | 1,623 | 42% | 350 (2,243) |
| Merch, apparel, collectibles | Signed items, jerseys, hoodies, sneakers, bags, replicas, comics | 2,809 | 2,129 | 787 | 28% | 125 (791) |
| Experience, travel, tickets | Trips, stays, cruises, event tickets, concerts, guided experiences | 2,592 | 2,154 | 798 | 33% | 710 (855) |
| Home, garden, appliance | Grills, kitchen appliances, furniture, decor, power stations, wellness devices | 2,460 | 1,857 | 594 | 50% | 282 (1,220) |
| Regulated goods (firearms) | Firearms, ammunition, parts and optics, from specialist retailers | 1,622 | 1,401 | 206 | 64% | 1,306 (1,038) |
| Sports and outdoor gear | Fitness, bikes, fishing, hunting gear, camping, archery, EDC knives | 1,206 | 915 | 435 | 52% | 380 (630) |
| Music gear | Guitars, pianos, pedals, recording equipment | 980 | 681 | 151 | 64% | 300 (625) |
| Toys and collectibles | LEGO, figures, statues, plush, board games | 912 | 732 | 220 | 16% | 100 (140) |
| Food, drink, consumables | Food, drink, supplements, a year's supply of consumables | 858 | 732 | 326 | 39% | 206 (331) |
| Tools, craft, DIY | Power tools, 3D printers and filament, crafting machines, epoxy | 834 | 557 | 163 | 42% | 300 (353) |
| Subscription or membership | Annual plans, lifetime memberships, a year of a product, courses | 790 | 539 | 321 | 47% | 150 (373) |
| Discount or coupon | Discount codes, coupons, cashback. Requires a purchase, so a weak prize | 647 | 492 | 160 | 44% | 100 (282) |
| Vehicle | Cars, trucks, motorcycles, e-bikes, outboard motors | 483 | 425 | 207 | 66% | 1,099 (319) |
| Beauty and wellness | Skincare, grooming, wellness products | 365 | 300 | 147 | 52% | 250 (188) |
| Exclusive access | Beta keys, playtests, creator interaction, community roles | 186 | 169 | 133 | 17% | 422 (32) |
| Pet products | Pet supplies | 114 | 97 | 31 | 41% | 149 (47) |
| Baby and kids | Cribs, strollers, baby products | 101 | 61 | 37 | 35% | 329 (35) |
| Services | Car washes, courses, insurance, consultations | 101 | 76 | 59 | 45% | 600 (45) |
| Bullion | Silver and gold bars, rounds, coins | 90 | 77 | 15 | 74% | 400 (67) |
| Art and custom | Artwork, prints, commissions | 84 | 67 | 53 | 32% | 209 (27) |
| Placeholder name | "1st Prize", "Winner", a campaign title reused: the record does not say what the prize was | 4,199 | 2,729 | 903 | 34% | 300 (1,422) |
| Unclassified | Neither rules nor the label pass could place them (opaque brand codes, ambiguous short names) | 3,377 | 2,690 | 1,310 | 35% | 230 (1,183) |

Categories were assigned in two passes: name-pattern rules (50,402 records) and, only where rules failed, a private LLM-assisted label pass over the leftover names (9,880 records). Small categories are listed for completeness and are too thin to benchmark.
<!-- /generated -->

## Cross-cutting flags

- **Own product** (inferred): a prize name sharing a distinctive word with the organizer's name. 18.1% of ordinary prize records carry this weak signal. It under-counts (a bakery giving away "a cake" does not match) and over-counts (a channel named after a phone brand), so treat it as directional only.
- **Complementary or partner product**: undetectable from names alone, but visible in descriptions as "teamed up with", "courtesy of", "sponsored by". Common in bundles and streamer campaigns.
- **Digital rewards**: game items, subscriptions and gift codes overlap. Digital delivery removes shipping cost and adds region-lock and account questions.

## Segments kept out of the ordinary benchmark

The crypto rule needs two or more strong signals among: wallet-address entry method, a crypto currency code on a prize, crypto terms in the prize or campaign name (airdrop, NFT, whitelist, IDO, token sale, exchange and chain names, stablecoin symbols), "$N in NAME" wording, amount plus a known ticker, or dense crypto terms in the description. One strong signal alone, weak signals only, or a label-pass flag put a campaign in the ambiguous bucket. Purchase opportunity covers sneaker raffles whose prize is the right to buy (by wording, or prize records that are shoe sizes).

<!-- generated:segments -->
| Segment | Campaigns | Handling |
|---|---|---|
| Ordinary | 37,180 (60,282 prize records, 6,817 organizers) | Basis for every default figure |
| Crypto | 16,150 | Excluded. Described only when a user asks for crypto advice. 40% used a wallet-address entry method |
| Ambiguous | 1,251 | Excluded and reported separately |
| Purchase opportunity | 94 | Excluded. The prize is the right to buy something |

Excluded campaigns are similar in size to ordinary ones (crypto median 3,339 contestants versus 2,201 ordinary), so exclusion changes who is in the benchmark and leaves the size distribution alone.
<!-- /generated -->

Any claim that crypto campaigns inflate a benchmark remains a hypothesis.

## Using the taxonomy

Pick the category that matches the objective first, then choose the item:

- Leads or sales in a niche: own product, store credit, category bundle, membership.
- Discount codes and coupons appear as prizes in 492 campaigns. They require a purchase, so treat them as a promotion with an entry form, and use them as a consolation tier under a real prize if at all.
- Hobby and home audiences: category gear (sports, music, tools, home) selects for the audience in a way generic electronics cannot.
- Reach or launch awareness: hardware or gift card tied to the brand, or the launched product itself.
- Community and UGC: merch, signed items, exclusive access, experiences with the team.
- Retention: subscription extensions, credit, early access.

Regulated goods (firearms, alcohol, tobacco, gambling-adjacent items) are recorded in the data but are not used as examples. If a user sells them, the accessibility and legal criteria dominate and local counsel is required.
