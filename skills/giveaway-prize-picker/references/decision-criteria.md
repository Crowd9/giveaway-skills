# Decision criteria

Everything here is general advice unless a sentence is marked as a dataset finding.

Four USD tables sit in this repository and each answers a different question. In answers, translate "crowd for the money" and "crowd per Prize dollar" into Entrants compared with campaigns offering Prizes of similar stated value. Use the one that matches what is being asked.

| Table | Where | The question it answers |
|---|---|---|
| Stated Prize cost per email signup by Prize category | below, in this file | For the kind of Prize we are considering, what did businesses declare per address captured? |
| Stated Prize value % of Entrants, per email, per follow and per referral entry by industry | `references/roi-benchmarks.md` | For our industry, what did a result typically cost? |
| Stated USD Prize values by category and campaign size | `references/prize-values-by-category-and-size.json` | For a campaign of our expected size in our category, what did businesses declare? |
| Crowd per Prize dollar by Prize category and by number of Prize units | `references/evidence-and-limitations.md` | Once the money is held constant, which categories and structures drew more people than their price tag suggests? |

The first three price a result. The fourth ranks categories after the budget is stripped out, so it is the table to reach for when the question is one Prize against another at the same spend.

## Six criteria

Rate each candidate Prize on all six. A Prize that fails accessibility or fulfillment is out regardless of desirability.

| Criterion | Question | Common failure |
|---|---|---|
| Audience relevance | Would the people you want to reach want this more than a random person would? | Generic electronics that attract sweepstakes hobbyists instead of customers |
| Desirability | Is it wanted enough to justify the entry effort you ask for? | A discount code or low-value merch positioned as a "grand Prize" |
| Connection to the business | Does winning (or seeing) the Prize teach Entrants what you sell? | Prize that never mentions or uses the product |
| Accessibility | Can the Entrants you target legally and practically receive it? | Alcohol, firearms, age-gated goods, region-locked services, travel needing visas |
| Fulfillment practicality | Can you ship, book or deliver it within the promised window? | Bulky or perishable goods across borders; experiences with blackout dates |
| Total cost | Retail value plus shipping, duties, taxes on the Winner, staff time, partner obligations, and a substitute if the item is unavailable | Budgeting the sticker price only |

## Broad versus specialized appeal

Broad appeal (cash, gift cards, phones, consoles) is appropriate when the objective genuinely is reach: awareness for a mass-market product, a launch where the product itself is the broad Prize, or list-building where you accept churn and will qualify later. Specialized appeal (own product, category-specific gear, expert experiences, access) fits lead generation for a defined niche, retention, community growth and UGC, where the value of an Entrant depends on who they are. For own product specifically, weigh that fit against a measured quality cost on Conversion Rate (the share of people who saw it and entered), cost % of Entrants and crowd per Prize dollar, not just headline Entrant count, see the own-product finding below.

A Prize that matches the business's own category draws no more crowd for the money than one that plainly does not. Both sit a little above a generic Prize, and the gap between them is within noise.

<!-- generated:ev_audience_fit -->
| Prize fit | Campaigns | Businesses | Entrants | Crowd per Prize dollar |
|---|---|---|---|---|
| A definite category that does not match | 27,625 | 6,464 | 547 | 1.09 |
| Matches the business's own category | 21,264 | 4,305 | 673 | 1.08 |
| Generic (cash, gift card, bundle, subscription, discount) | 36,845 | 8,215 | 463 | 1.00 |
<!-- /generated -->

Campaigns with several Prize records drew about a quarter less crowd per Prize dollar than single-record campaigns. Use several records when the reason is fulfilment or fairness, not when the reason is reach.

Expect a broad Prize to bring Entrants who never buy. That is acceptable when the objective needs reach and the follow-up handles the mismatch. It becomes a problem when the leads go straight to a sales team.

For a foot-traffic or local objective, name the reason directly: cash, electronics or a gift card to somewhere else can be won and used without the Winner ever visiting, so these Prizes do not require the store visit your objective needs. Own product or in-store credit fixes this because redemption in person is the filter.

Before allowing for size, own product shows up in 17% of campaigns, and those campaigns drew more Entrants and fewer Entries per Entrant on a lower Conversion Rate than bought-in ones. That comparison does not hold campaign size or industry constant, and it describes what businesses saw with no comparison group of failed campaigns.

| | Own product | Bought-in |
|---|---|---|
| Share of campaigns | 17% [19,602 campaigns, 5,124 businesses] | 83% [96,681 campaigns, 14,836 businesses] |
| Typical Entrant count | 696 | 464 |
| Entries per Entrant | 4.0 | 4.5 |
| Conversion Rate | 26% | 27% |

Compared within the source's stated groups, own-product Prizes appear more often among campaigns with the most Entrants and the strongest crowd per Prize dollar, and less often among the top performers on Conversion Rate, cost per Entrant and engagement. Entrant and value-adjusted cohorts compare within industry. The other cohorts compare within campaign size and industry. A ratio below 1.00 means the own-product flag is less common in the top fifth than in the rest. These are feature-prevalence ratios, not changes in performance caused by the Prize. Email signups also show a small positive association after matching.

| Measure (top performers) | Ratio, compared like with like | Ratio, before allowing for size | Campaigns | Businesses |
|---|---|---|---|---|
| Raw Entrant count | 1.23 | 1.48 | 23,256 | 4,467 |
| Conversion Rate | 0.76 | 0.72 | 7,839 | 1,092 |
| Crowd per Prize dollar | 1.03 | 1.09 | 8,590 | 2,098 |
| Cost per Entrant | 0.54 | 0.38 | 8,580 | 2,071 |
| Engagement | 0.81 | 0.68 | 23,250 | 3,371 |
| Email signups | 1.047 | 0.621 | 7,863 | 1,648 |

What own product buys back is fit: the Entrant who wanted it is closer to a buyer than an Entrant chasing a generic Prize, and the cost to you is wholesale, not the retail figure stated to Entrants. That trade is the right call when the objective is a qualified list or a repeat customer, not the largest crowd at any quality, and the size of the association varies by industry and campaign size, covered next.

Own product trails bought-in Prizes on crowd per Prize dollar overall and in each of the four industries below. The gap is smallest in electronics and tech. Counts describe the full group, while the index uses only its valued campaigns.

| Industry | Own product | Bought-in |
|---|---|---|
| Overall | 0.93 [19,602 campaigns, 5,124 businesses, 7,510 valued campaigns] | 1.01 [96,681 campaigns, 14,836 businesses, 35,443 valued campaigns] |
| Media and entertainment | 0.94 [1,389 campaigns, 378 businesses, 388 valued campaigns] | 1.20 [20,151 campaigns, 1,865 businesses, 8,530 valued campaigns] |
| Gaming and esports | 0.78 [2,666 campaigns, 717 businesses, 863 valued campaigns] | 0.82 [21,563 campaigns, 4,357 businesses, 6,610 valued campaigns] |
| Electronics and tech | 1.17 [4,296 campaigns, 674 businesses, 1,443 valued campaigns] | 1.20 [11,247 campaigns, 1,751 businesses, 3,584 valued campaigns] |
| Sports and outdoors | 1.17 [1,095 campaigns, 421 businesses, 574 valued campaigns] | 1.26 [3,540 campaigns, 782 businesses, 1,743 valued campaigns] |

By campaign size, crowd per Prize dollar does not reverse the same way: own product trails bought-in Prizes at every size tested. Conversion Rate tells a different story by campaign size: own product converts worse than bought-in at the smallest size but better at the two larger ones, on the same campaigns as the crowd-per-Prize-dollar figures above, so a larger campaign chasing buyers over browsers is where the trade pays off most cleanly on this measure.

| Campaign size (Entrants) | Crowd/$, own product | Crowd/$, bought-in | Conversion Rate, own product | Conversion Rate, bought-in |
|---|---|---|---|---|
| 1,000 to 2,500 | 1.64 [4,257 campaigns, 1,645 businesses, 1,698 valued campaigns] | 2.03 [15,717 campaigns, 4,029 businesses, 6,078 valued campaigns] | 26.9% | 28.5% |
| 2,500 to 10,000 | 3.38 [2,926 campaigns, 1,041 businesses, 1,205 valued campaigns] | 3.87 [9,777 campaigns, 2,373 businesses, 3,915 valued campaigns] | 27.8% | 27.0% |
| 10,000 and up | 10.81 [715 campaigns, 262 businesses, 224 valued campaigns] | 12.06 [2,456 campaigns, 581 businesses, 908 valued campaigns] | 30.2% | 28.2% |

### Prize hierarchy (advice, from Gleam's campaign team)

This ordering is one operator's working practice, written down by the team that runs campaigns on the platform. Nothing in the dataset tests it. Treat it as a starting shortlist a practitioner would defend, and drop any rung the business has a reason to drop.

A default order to consider, adapted to the business: an audience-specific hero Prize, then your own product plus the aspirational thing your customer wants next (coffee plus an espresso machine, supplements plus a sports watch, skincare plus a beauty device), then own product or own-brand credit, then an exclusive or limited item, then category-specific equipment, then a relevant collaboration bundle, then generic technology, then cash, then a generic gift card. The question that finds the adjacent Prize: what does the customer's ideal day contain right before or after using this product?

Audience-specific Prizes show mixed associations across the four industries tested. They draw more crowd for the money than generic Prizes in electronics and tech and sports and outdoors, and less in media and entertainment and gaming and esports. The table lists the full group and its valued subset. A third bucket, Prizes matching neither the audience nor the generic list, is not reported here.

| Industry | Audience-specific | Generic |
|---|---|---|
| Electronics and tech | 1.61 [7,826 campaigns, 1,334 businesses, 2,363 valued campaigns] | 0.94 [2,501 campaigns, 649 businesses, 1,072 valued campaigns] |
| Media and entertainment | 0.87 [1,288 campaigns, 287 businesses, 375 valued campaigns] | 1.29 [8,375 campaigns, 920 businesses, 4,277 valued campaigns] |
| Gaming and esports | 0.75 [5,881 campaigns, 1,573 businesses, 1,673 valued campaigns] | 0.80 [6,095 campaigns, 1,679 businesses, 2,502 valued campaigns] |
| Sports and outdoors | 1.24 [335 campaigns, 145 businesses, 169 valued campaigns] | 1.12 [1,335 campaigns, 497 businesses, 726 valued campaigns] |

Collaborations should pass one practical test: same customer, different product. The title-signal cut now reports less crowd for the money than typical, but a slightly larger share reaching the top fifth [2,967 valued campaigns, 1,112 businesses].

| | Collaboration-titled | Rest |
|---|---|---|
| Crowd per Prize dollar | 0.94, about 6% below typical | 1.00, typical |
| Reached the best fifth of campaigns | 23% of the time | 20% of the time |

Crowd per Prize dollar means a campaign's Entrants divided by the typical Entrants for other campaigns at the same stated Prize cost, so 1.00 is typical for the money.

The collaboration cut in `analysis/output/prize_economics.json` gives the same pooled direction: collaborations sit at 0.94 against 1.00 for everything else. The substantial positive gap is in media and entertainment, where collaborations reach 2.59 against 1.18 for the rest of that industry. Elsewhere the gap is small or negative. Use the industry row when a partner is the question. Counts in brackets are campaigns with a stated Prize value, the only ones a value index can be computed on.

| Industry | Wider collaboration | Rest |
|---|---|---|
| Pooled (all industries) | 0.94 [2,967 valued campaigns] | 1.00 [39,986 valued campaigns] |
| Media and entertainment | 2.59 [338 valued campaigns] | 1.18 [8,580 valued campaigns] |
| Electronics and tech | 1.20 [501 valued campaigns] | 1.19 [4,526 valued campaigns] |
| Gaming and esports | 0.82 [909 valued campaigns] | 0.81 [6,564 valued campaigns] |
| Sports and outdoors | 1.11 [117 valued campaigns] | 1.25 [2,200 valued campaigns] |

## Structure tradeoffs

Default for an acquisition giveaway: one Prize worth wanting. One-unit campaigns drew about 15% more crowd for the money than typical (1.15 on crowd per Prize dollar) against 36% less for six to twenty units (0.64), in the crowd-per-Prize-dollar-by-number-of-Prize-units table in `references/evidence-and-limitations.md`. Split the budget only when the units are the point: sampling, digital Prizes, community rewards, or tiers that make the campaign read better. Before finalizing Prize count against a fixed budget, check `giveaway-winner-structure`'s structure findings: splitting that budget across several Prizes was associated with fewer Entrants than one Prize of the same value, with the full breakdown by Prize value there.

| Structure | Strengths | Costs and risks |
|---|---|---|
| One major Prize | Simple story, strongest headline, easiest fulfillment | Perceived odds are worst; one unhappy Winner is the whole outcome |
| Several equal Winners | Better perceived odds, more social proof, more product in more hands | Headline value is split; fulfillment multiplies |
| Tiered (1st, 2nd, 3rd) | Headline plus odds; natural for partner bundles | More admin; lower tiers must still be worth wanting |
| Bundle around your product | Raises headline value cheaply with partners; teaches your category | Partner obligations; substitutes needed if items go out of stock |
| Recurring (daily, weekly) | Keeps a long campaign alive; good for content series | Requires repeated draws and announcements |

Looking at the campaigns behind these numbers: 83% listed one Prize, and 32% listed a quantity above one for at least one Prize [24,591 of 116,499 campaigns listed five or more Prize units].

Typical Entrant counts for single-unit and five-plus-unit structures were almost identical [492 against 513], which says nothing about effect because every campaign passed the dataset's 100-Entrant floor. Those raw counts use a broader population and different unit groups from the value-adjusted comparison. The paired raw and adjusted columns in the crowd-per-Prize-dollar table in `references/evidence-and-limitations.md` use 26,919 one-unit campaigns, 10,192 with two to five units, 4,276 with six to twenty and 1,566 with twenty one or more. Their typical Entrant counts are 509, 463, 565 and 1,065 respectively. Use that paired table when explaining the adjustment for stated Prize value. Its population omits campaigns without usable value information, so the difference from the broader raw comparison cannot be attributed to adjustment alone. These associations do not predict what splitting this reader's budget will cause.

## Stated Prize cost per email signup (extracted)

For campaigns with an email action and every Prize valued in USD, the stated pool divided by email signups. Of the categories with the most campaigns, cash and gift cards sit lowest at 0.20 and experiences highest at 1.20. Use it to sanity-check a budget against the list it is meant to build, and remember the stated value is what the organizer wrote.

| Prize category | Campaigns | Typical USD per signup |
|---|---|---|
| Other or unclassified | 4,747 | 0.59 |
| Gift card or cash | 5,103 | 0.20 |
| Tech hardware | 2,987 | 0.42 |
| Bundle or box | 2,541 | 0.58 |
| Game items or skins | 1,437 | 0.45 |
| Experience, travel, tickets | 861 | 1.20 |
| Merch, apparel, collectibles | 795 | 0.50 |
| Regulated goods (firearms) | 603 | 0.39 |
| Home, garden, appliance | 601 | 0.49 |
| Placeholder Prize name | 478 | 0.54 |

## What another dollar of Prize money is worth (extracted)

Split the campaigns that put a USD value on every Prize into ten equal groups by Prize pool and the crowd rises
with the money, slowly:

| Prize pool tenth | Campaigns | Typical pool USD | Typical Entrants |
|---|---|---|---|
| lowest | 4,301 | 20 | 272 |
| third | 4,301 | 90 | 306 |
| fifth | 4,300 | 227 | 520 |
| seventh | 4,300 | 550 | 816 |
| ninth | 4,300 | 1,850 | 1,516 |
| highest | 4,300 | 4,600 | 2,022 |

230 times the Prize money goes with 7.4 times the Entrants. Put another way, doubling the Prize budget goes with
about 29% more Entrants. That is the weaker of the two levers this data can separate: doubling the traffic put in
front of the page goes with about 40% more, which is the figure in the promotion reference. Neither is a promise,
and the two are in different units. What the data supports is the ordering. Where a business is deciding
between a bigger Prize and a bigger push, the Prize is the slower of the two.

Three limits, all of which matter here. Only 37% of campaigns valued every Prize, so this describes the
businesses organised enough to fill the field. A bigger Prize goes with a bigger business and a bigger audience,
so the Prize money is not what bought the crowd. And the bottom tenth sits at a 20 USD pool. That is a different kind of campaign, and reading the range as one
smooth curve overstates it.

Source: `analysis/output/prize_elasticity.json`.

## Budget template

Label every figure an estimate. Verify current prices when a tool is available and the number matters.

```
Prize retail value            (per unit x units)
Your actual cost              (wholesale, own product at cost, partner-supplied at 0)
Shipping / delivery           (quoted parcels, destination-dependent)
Duties, import tax, sales tax (who pays, and disclose it)
Winner-side taxes             (some jurisdictions tax prizes, so disclose it)
Substitution reserve          (if the item may be unavailable)
Admin time                    (drawing, contacting, verifying, chasing)
Promotion                     (separate from the prize, and easy to starve)
Contingency                   (5 to 10%)
```

In `scripts/budget.py`, shipping defaults to a charge for each physical Prize unit. Use `--shipping-total` with the complete delivery quote when several items share a parcel or one Winner needs several parcels. The override replaces shipping only. Duties and taxes remain separate. Winner count does not determine parcel count.

For mixed-cost Prizes, set `--cost-ratio` to total actual Prize cost divided by total retail value, then use `--substitute-reserve-amount` for the actual replacement cost being reserved. For example, an own product worth $100 that costs $30 plus a bought $500 device has $600 retail value and $530 actual cost. A ratio of `0.8833333333333333` and `--substitute-reserve-amount 500` reserve the device's full replacement cost. Use either that amount or `--substitute-reserve`, which prices reserve units using the global ratio.

Typical Prize values across the campaigns behind these numbers, and by campaign size, are shown below [stated USD values only, 64,579 of 170,599 Prize listings, 62% of listings have no stated value, fully valued campaign totals from 42,892 campaigns]. Bigger campaigns declared bigger Prizes, and bigger businesses run bigger campaigns, so read that as who runs what, with no price of admission implied.

| Measure | Typical | Middle half | Note |
|---|---|---|---|
| Per-listing stated value | 125 | 50 to 425 | nine in ten declared less than 1,199 |
| Fully valued campaign total | 299 | 90 to 1,000 | - |
| Campaign total, 1,000-2,500 Entrants | 530 | - | - |
| Campaign total, 2,500-10,000 Entrants | 1,299 | - | - |
| Campaign total, 10,000+ Entrants | 3,000 | - | - |

Entrants rise with the stated pool up to about 5,000 USD and fall back above it [42,953 campaigns with a full value stated, from 9,089 businesses].

| Stated Prize pool | Typical Entrants |
|---|---|
| Under 50 USD | 266 |
| 50,000 USD and up | 1,128 |

Prize value and Entrant count move together only loosely: ten times the stated pool comes with about 2.2 times the Entrants, and value accounts for about 23% of the spread in Entrant counts, so most of what separates a big campaign from a small one is something other than the money. All of it describes what businesses chose and who they were. A bigger Prize comes with a bigger business, so none of it says a bigger Prize would lift a given campaign.

Across the four bands from 250 to 4,999 USD, a 1% larger stated pool is associated with about 0.46% to 0.63% more Entrants. Higher bands alternate between small increases and declines, so the pooled curve supplies no reliable return for another dollar.

| Spend level (USD) | Extra Entrants per 1% bigger Prize | Campaigns | Businesses |
|---|---|---|---|
| 250 to 4,999 (four bands) | 0.46 to 0.63 | - | - |
| 5,000 and up (four bands) | 0.03, -0.41, 0.24, -0.70 | 1,099, 553, 130, 146 | 631, 359, 103, 101 |

The larger-pool association varies by tier and industry. Gaming and esports still rises at 5,000 to 9,999 USD but falls in the next band. Sports and outdoors rises across those two bands. These differences rule out a universal budget ceiling.

| Cut, at 5,000-9,999 USD (unless noted) | Extra Entrants per 1% bigger Prize | Campaigns | Businesses |
|---|---|---|---|
| Pro tier | 0.09 | 441 | 307 |
| Business tier | -0.25 | 521 | 313 |
| Electronics and tech | -0.04 | 191 | 104 |
| Media and entertainment | -1.11 | 82 | 47 |
| Gaming and esports | 0.17, then -0.46 at 10,000-24,999 | 134 | 74 |
| Sports and outdoors | 0.23, then 0.06 at 10,000-24,999 | 97 | 69 |

The share beating the typical crowd for its stated value and the share falling short are close at the low end. The 250 to 499 USD band has slightly more misses than beats, and the highest band is even. This gives no clear cheap-Prize advantage. These are selected campaigns that already reached 100 Entrants, with no comparison group of smaller or failed campaigns.

| Spend level (USD) | Beat by 50%+ (crowd/$ 1.5+) | Missed by 50%+ (crowd/$ below 0.667) | Campaigns |
|---|---|---|---|
| Under 50 | 29% | 28% | 6,063 |
| 250 to 499 | 37% | 39% | 6,146 |
| 50,000 and up | 42% | 42% | 146 |

## Prizes for a store

- **Own product at cost.** The stated value is retail, your cost is wholesale, and the Prize filters for interest in the product. The own-product comparisons above show lower Conversion Rate and low-cost performance, but more frequent top-fifth Entrant and crowd-per-dollar results after the source's matching. Own product trails bought-in on the typical crowd-per-dollar figure in all four industry rows. Conversion Rate turns in its favor above 2,500 Entrants. Use fit and actual cost to decide, since none of these figures measures lead quality.
- **Win your cart up to a cap.** The Prize is whatever the Winner put in the cart, capped at a stated number. The cap is the budget, and the title carries it. Cart and wishlist campaigns sit at 1.42 on crowd per Prize dollar, about 42% above typical for the money and the second highest figure of any campaign type, on 450 valued campaigns of 902. They also draw 724 Entrants against a typical 492. Price them as a wishlist and browsing play that also reaches. [`analysis/output/campaign_types.json`, `types`.]
- **Gift card to your own store.** Budget the goods or service cost of full redemption plus delivery and other fulfilment costs, separately from the card's face value. For example, a fully redeemed $100 card at 70% gross margin costs $30 in goods before fulfilment. Add delivery explicitly, without assuming an unspent balance or additional purchases. Gift card campaigns post 1.18 on crowd per Prize dollar, about 18% above typical for the money, on 6,787 valued campaigns of 11,095, while drawing fewer Entrants than typical at 432. A gift card to someone else's store buys reach and sends the Winner elsewhere. [`analysis/output/campaign_types.json`, `types`.]
- **Discount codes as the headline Prize.** 1,046 campaigns, 0.73 on crowd per Prize dollar (about 27% below typical for the money), and a purchase condition dressed as a Prize. Use codes for everyone who did not win, under a real Prize, and read giveaway-winner-communications for the mechanics. [`analysis/output/prize_economics.json`, `by_prize_category`.]
- **Ship the Prize as an order.** Create the Winner's Prize as a zero-value order in the store so it goes out through the normal pick, pack and tracking flow, and the Winner sees it in their account.
- **Fourth quarter.** Reserve the Prize stock before the sale sells it out. Close a December draw at least a week before the carrier's cutoff, and where that is not possible make the Prize a gift card so the Winner still has it by the day.
- **Budget line for the codes.** A store campaign has two costs: the Prize, and the discount taken up by non-Winners. Budget the discount cost as expected redemptions times average discount. Afterwards, report redemption count, total discount cost and redeemed-order revenue separately. Obtain the monetary totals from order records, including discounts and refunds. The same redemption count can represent different revenue totals, and redeemed-order revenue alone does not establish incremental revenue from the campaign.

## Fulfillment checklist

- Eligibility: countries, states, age, employees excluded, one entry per person rules.
- Delivery: who ships, insured or not, address verification, replacement policy for damage.
- Insurance on a high-value physical Prize: insure it for the replacement cost while it is in transit, use a tracked and signature-required service, and budget the premium as a line in the Prize cost. A lost console is a refund. A lost 3,000 USD hero Prize is a public failure with a named Winner waiting.
- Timing: draw date, response deadline for Winners, redraw policy, delivery window.
- Substitution: "Prize of equal or greater value" clause when stock is uncertain.
- Experiences: dates, blackout periods, travel included or not, companion allowed, transferable or not.
- Digital Prizes: region locks, platform accounts, expiry.
- Disclosure: retail value, taxes, sponsor, and terms. Sweepstakes and lottery law differs by jurisdiction, so recommend the user confirm local rules. This skill does not give legal advice.

## Common mistakes

- Choosing the Prize before the objective. A Prize picked for its headline pulls whoever wants that item. Decide what the Entrants are for, then pick.
- Budgeting the sticker price. Shipping, duties, Winner-side tax, a substitute unit and staff time routinely add 20 to 40 percent to a physical Prize.
- Inflating "retail value". Entrants and regulators can check. State the price a buyer would pay today, and treat "lifetime" or "a year of" values as retail, with your cost kept separate.
- No eligibility terms. Countries, age, employees, one entry per person, and what happens if a Winner does not respond. Missing terms are where disputes start.
- Promising Entrant numbers. Volume comes from promotion, audience size and entry friction. No Prize guarantees it, and this dataset cannot show that any Prize caused participation.
- Regional or regulated Prizes offered globally. Alcohol, firearms, gift cards locked to one country, or travel that needs visas. Check the accessibility criterion before the headline.
- One Prize, many objectives. A single PS5 cannot both build a niche email list and drive mass awareness. Pick one objective per giveaway.
- Copying a big campaign's Prize. A local business does not need the typical figures from campaigns of 10,000 Entrants and up. Half of all campaigns in this skill's data ran at a fraction of that size and Prize spend (see the budget template above). The cheap Prizes that drew crowds cut in giveaway-idea-generator lists 109 campaigns under 250 USD that passed 5,000 Entrants, and the campaigns that beat their Prize money cut sits next to it. Both point the same way: the audience in front of the Prize did the work, and most of those businesses had run campaigns before [four in five].

## When the Prize is unrelated to the business

Ask what the objective is. If it is reach and the follow-up can qualify the audience, an unrelated popular Prize can work, ideally tied to the brand (branded edition, bundled with own product, framed around a use the brand serves). If the objective is leads or sales, prefer a Prize that filters for interest: own product, a category-specific item, or store credit. Say plainly that the dataset cannot show which choice performs better.
