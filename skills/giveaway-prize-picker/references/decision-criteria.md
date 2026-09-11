# Decision criteria

Everything here is general advice unless a sentence is marked as a dataset finding.

Four USD tables sit in this repository and each answers a different question. Use the one that matches what is being asked.

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
| A definite category that does not match | 29,190 | 6,585 | 554 | 1.10 |
| Matches the business's own category | 21,436 | 4,384 | 684 | 1.09 |
| Generic (cash, gift card, bundle, subscription, discount) | 32,900 | 7,767 | 458 | 1.01 |
<!-- /generated -->

Splitting the same budget across records buys about a fifth less crowd per Prize dollar. Use several records when the reason is fulfilment or fairness, not when the reason is reach.

Expect a broad Prize to bring Entrants who never buy. That is acceptable when the objective needs reach and the follow-up handles the mismatch. It becomes a problem when the leads go straight to a sales team.

For a foot-traffic or local objective, name the reason directly: cash, electronics or a gift card to somewhere else can be won and used without the Winner ever visiting, so a broad Prize buys reach, not the visit the objective needs. Own product or in-store credit fixes this because redemption in person is the filter.

Before allowing for size, own product shows up in 17% of campaigns, and those campaigns drew more Entrants and more Actions per Entrant on a lower Conversion Rate than bought-in ones. That comparison does not hold campaign size or industry constant, and it describes what businesses saw with no comparison group of failed campaigns.

| | Own product | Bought-in |
|---|---|---|
| Share of campaigns | 17% [19,671 campaigns, 5,168 businesses] | 83% [97,457 campaigns, 14,966 businesses] |
| Typical Entrant count | 695 | 464 |
| Actions per Entrant | 4.1 | 3.3 |
| Conversion Rate | 34% | 39% |

Once compared like with like by size and industry, using your own product as the Prize costs quality, not turnout: raw Entrant count is statistically the same either way (even odds), but own-product campaigns land among the top performers less often on Conversion Rate, on crowd per Prize dollar, and on keeping cost % of Entrants low, and less often on engagement too. A ratio below 1.00 means own product shows up less often among the top performers on that measure than a bought-in Prize does, once campaigns are compared like with like. It does not cost email signups, where the ratio actually rises once compared like with like, so own product is not shown to hurt that action.

| Measure (top performers) | Ratio, compared like with like | Ratio, before allowing for size | Campaigns | Businesses |
|---|---|---|---|---|
| Raw Entrant count | 1.00 | - | - | - |
| Conversion Rate | 0.77 | 0.83 | 2,113 | 326 |
| Crowd per Prize dollar | 0.93 | 1.01 | 19,671 | 5,168 |
| Cost % of Entrants | 0.73 | 0.61 | 2,781 | 831 |
| Engagement | 0.88 | 0.78 | 7,113 | 1,425 |
| Email signups | 1.002 | 0.799 | - | - |

What own product buys back is fit: the Entrant who wanted it is closer to a buyer than an Entrant chasing a generic Prize, and the cost to you is wholesale, not the retail figure stated to Entrants. That trade is the right call when the objective is a qualified list or a repeat customer, not the largest crowd at any quality, and it reverses by industry and flattens by campaign size, covered next.

That quality cost is not even across industries or campaign sizes. By industry, own product trails bought-in Prizes on crowd per Prize dollar overall and in media and entertainment and gaming and esports, but the gap reverses in electronics and tech and goes flat in sports and outdoors, so a store selling into either category is not paying the pooled cost.

| Industry | Own product | Bought-in |
|---|---|---|
| Overall | 0.96, about 4% below typical [7,845 campaigns, 2,266 businesses] | 1.02, about 2% above [27,652 campaigns, 5,106 businesses] |
| Media and entertainment | 1.01, about 1% above typical [382 campaigns, 136 businesses] | 1.26, about 26% above [4,616 campaigns, 512 businesses] |
| Gaming and esports | 1.01, about 1% above typical [864 campaigns, 273 businesses] | 1.07, about 7% above [5,442 campaigns, 1,287 businesses] |
| Electronics and tech (reversed) | 0.94, about 6% below typical [2,356 campaigns, 408 businesses] | 0.90, about 10% below [4,916 campaigns, 820 businesses] |
| Sports and outdoors (flat) | 0.97, close to typical [512 campaigns, 232 businesses] | 0.98, close to typical [1,753 campaigns, 412 businesses] |

By campaign size, crowd per Prize dollar does not reverse the same way: own product trails bought-in Prizes at every size tested. Conversion Rate tells a different story by campaign size: own product converts worse than bought-in at the smallest size but better at the two larger ones, on the same campaigns as the crowd-per-Prize-dollar figures above, so a larger campaign chasing buyers over browsers is where the trade pays off most cleanly on this measure.

| Campaign size (Entrants) | Crowd/$, own product | Crowd/$, bought-in | Conversion Rate, own product | Conversion Rate, bought-in |
|---|---|---|---|---|
| 1,000 to 2,500 | 0.69, 31% below typical [4,244 campaigns, 1,627 businesses] | 0.75, 25% below typical [15,558 campaigns, 3,970 businesses] | 27.0% | 28.4% |
| 2,500 to 10,000 | 1.51, 51% above typical [2,891 campaigns, 1,017 businesses] | 1.66, 66% above typical [9,684 campaigns, 2,334 businesses] | 28.0% | 27.0% |
| 10,000 and up | 5.29, far above typical [710 campaigns, 258 businesses] | 5.69, far above typical [2,410 campaigns, 562 businesses] | 30.9% | 27.9% |

### Prize hierarchy (advice, from Gleam's campaign team)

This ordering is one operator's working practice, written down by the team that runs campaigns on the platform. Nothing in the dataset tests it. Treat it as a starting shortlist a practitioner would defend, and drop any rung the business has a reason to drop.

A default order to consider, adapted to the business: an audience-specific hero Prize, then your own product plus the aspirational thing your customer wants next (coffee plus an espresso machine, supplements plus a sports watch, skincare plus a beauty device), then own product or own-brand credit, then an exclusive or limited item, then category-specific equipment, then a relevant collaboration bundle, then generic technology, then cash, then a generic gift card. The question that finds the adjacent Prize: what does the customer's ideal day contain right before or after using this product?

Audience-specific Prizes (moderate confidence, holds in 3 of 4 industries tested): a Prize matched to the site's audience (a gaming item on a gaming site, tech hardware on an electronics site) buys more crowd for the money than a generic Prize (cash, gift card, subscription, bundle) in electronics and tech, media and entertainment and gaming and esports, margin small in the latter two. It reverses in sports and outdoors, both close to typical. A third bucket, Prizes matching neither the audience nor the generic list, is not directionally stable across industries and is not reported here.

| Industry | Audience-specific | Generic |
|---|---|---|
| Electronics and tech | 0.97, about 3% below typical [4,832 campaigns, 783 businesses] | 0.76, about 24% below [1,155 campaigns, 340 businesses] |
| Media and entertainment | 1.07, about 7% above typical [613 campaigns, 109 businesses] | 1.05, about 5% above [1,434 campaigns, 276 businesses] |
| Gaming and esports | 1.08, about 8% above typical [1,840 campaigns, 504 businesses] | 1.05, about 5% above [1,317 campaigns, 485 businesses] |
| Sports and outdoors (reversed) | 0.88, about 12% below typical [326 campaigns, 135 businesses] | 0.90, about 10% below [612 campaigns, 257 businesses] |

Collaborations work when they pass one test: same customer, different product. Campaigns whose title signals a collaboration ("x", "collab", "partner") drew noticeably more crowd for the money than typical, and reached the best fifth of campaigns far more often than the rest [1,138 campaigns, a title proxy].

| | Collaboration-titled | Rest |
|---|---|---|
| Crowd per Prize dollar | 1.15, about 15% above typical | 0.99, about 1% below typical |
| Reached the best fifth of campaigns | 30% of the time | 19% of the time |

Crowd per Prize dollar means a campaign's Entrants divided by the typical Entrants for other campaigns at the same stated Prize cost, so 1.00 is typical for the money.

A wider definition of collaboration, matching the campaign or Prize name and not the title alone, puts the figure on a much larger base, and on that base the lift disappears: collaborations sit at 0.94 against 1.00 for everything else. The one industry where it survives is media and entertainment, where collaborations reach 2.57 against 1.18 for the rest of that industry. Elsewhere a collaboration lands level with its own industry or a little below. Read the pooled row, not the title-only figure above it, when a partner is the question. Counts in brackets are campaigns with a stated Prize value, the only ones a value index can be computed on.

| Industry | Wider collaboration | Rest |
|---|---|---|
| Pooled (all industries) | 0.94 [2,985 valued campaigns] | 1.00 [40,188] |
| Media and entertainment | 2.57, about 157% above typical [338] | 1.18, about 18% above typical [8,589] |
| Electronics and tech | 1.20, about 20% above typical [501] | 1.20, about 20% above typical [4,555] |
| Gaming and esports | 0.82, about 18% below typical [920] | 0.81, about 19% below typical [6,644] |
| Sports and outdoors | 1.11, about 11% above typical [117] | 1.25, about 25% above typical [2,201] |

## Structure tradeoffs

Default for an acquisition giveaway: one Prize worth wanting. One-unit campaigns drew about 15% more crowd for the money than typical (1.15 on crowd per Prize dollar) against 36% less for six to twenty units (0.64), in the crowd-per-Prize-dollar-by-number-of-Prize-units table in `references/evidence-and-limitations.md`. Split the budget only when the units are the point: sampling, digital Prizes, community rewards, or tiers that make the campaign read better. Before finalizing Prize count against a fixed budget, check `giveaway-winner-structure`'s structure findings: splitting that budget across several Prizes costs turnout against one Prize of the same value, with the full breakdown by Prize value there.

| Structure | Strengths | Costs and risks |
|---|---|---|
| One major Prize | Simple story, strongest headline, easiest fulfillment | Perceived odds are worst; one unhappy Winner is the whole outcome |
| Several equal Winners | Better perceived odds, more social proof, more product in more hands | Headline value is split; fulfillment multiplies |
| Tiered (1st, 2nd, 3rd) | Headline plus odds; natural for partner bundles | More admin; lower tiers must still be worth wanting |
| Bundle around your product | Raises headline value cheaply with partners; teaches your category | Partner obligations; substitutes needed if items go out of stock |
| Recurring (daily, weekly) | Keeps a long campaign alive; good for content series | Requires repeated draws and announcements |

Looking at the campaigns behind these numbers: 82% listed one Prize, and 32% listed a quantity above one for at least one Prize [25,054 of 117,348 campaigns listed five or more Prize units].

Typical Entrant counts for single-Winner and multi-unit structures were almost identical [492 against 510], which says nothing about effect because every campaign passed the dataset's 100-Entrant floor. Those raw Entrant counts and the crowd-per-Prize-dollar figures by number of Prize units are the same campaigns seen two ways: raw, one unit and many units drew the same crowd, and once the money is held constant, one unit sits above typical and six or more below. The crowd-per-Prize-dollar table in `references/evidence-and-limitations.md` carries the second view, and it is the one to quote when a budget is fixed.

## Stated Prize cost per email signup (extracted)

For campaigns with an email action and every Prize valued in USD, the stated pool divided by email signups. Of the categories with the most campaigns, cash and gift cards sit lowest at 0.16 and experiences highest at 1.16. Use it to sanity-check a budget against the list it is meant to build, and remember the stated value is what the organizer wrote.

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

## What another dollar of Prize money is worth (extracted)

Split the campaigns that put a USD value on every Prize into ten equal groups by Prize pool and the crowd rises
with the money, slowly:

| Prize pool tenth | Campaigns | Typical pool USD | Typical Entrants |
|---|---|---|---|
| lowest | 4,301 | 20 | 272 |
| third | 4,301 | 90 | 313 |
| fifth | 4,300 | 227 | 522 |
| seventh | 4,300 | 550 | 809 |
| ninth | 4,300 | 1,850 | 1,518 |
| highest | 4,300 | 4,600 | 2,020 |

230 times the Prize money goes with 7.4 times the Entrants. Put another way, doubling the Prize budget goes with
about 29% more Entrants. That is the weaker of the two levers this data can separate: doubling the traffic put in
front of the page goes with about 40% more, which is the figure in the promotion reference. Neither is a promise,
and the two are in different units. What the data supports is the ordering. Where a business is deciding
between a bigger Prize and a bigger push, the Prize is the slower of the two.

Three limits, all of which matter here. Only 38% of campaigns valued every Prize, so this describes the
businesses organised enough to fill the field. A bigger Prize goes with a bigger business and a bigger audience,
so the Prize money is not what bought the crowd. And the bottom tenth sits at a 20 USD pool. That is a different kind of campaign, and reading the range as one
smooth curve overstates it.

Source: `analysis/output/prize_elasticity.json`.

## Budget template

Label every figure an estimate. Verify current prices when a tool is available and the number matters.

```
Prize retail value            (per unit x units)
Your actual cost              (wholesale, own product at cost, partner-supplied at 0)
Shipping / delivery           (per winner, destination-dependent)
Duties, import tax, sales tax (who pays, and disclose it)
Winner-side taxes             (some jurisdictions tax prizes, so disclose it)
Substitution reserve          (if the item may be unavailable)
Admin time                    (drawing, contacting, verifying, chasing)
Promotion                     (separate from the prize, and easy to starve)
Contingency                   (5 to 10%)
```

Typical Prize values across the campaigns behind these numbers, and by campaign size, are shown below [stated USD values only, 65,018 of 172,645 Prize listings, 62% of listings have no stated value, fully valued campaign totals from 43,109 campaigns]. Bigger campaigns declared bigger Prizes, and bigger businesses run bigger campaigns, so read that as who runs what, never as a price of admission.

| Measure | Typical | Middle half | Note |
|---|---|---|---|
| Per-listing stated value | 125 | 50 to 424 | nine in ten declared less than 1,199 |
| Fully valued campaign total | 299 | 90 to 1,000 | - |
| Campaign total, 1,000-2,500 Entrants | 530 | - | - |
| Campaign total, 2,500-10,000 Entrants | 1,299 | - | - |
| Campaign total, 10,000+ Entrants | 3,000 | - | - |

Entrants rise with the stated pool up to about 5,000 USD and fall back above it [43,173 campaigns with a full value stated, from 9,180 businesses].

| Stated Prize pool | Typical Entrants |
|---|---|
| Under 50 USD | 266 |
| 50,000 USD and up | 1,095 |

Prize value and Entrant count move together only loosely: ten times the stated pool comes with about 2.2 times the Entrants, and value accounts for about 23% of the spread in Entrant counts, so most of what separates a big campaign from a small one is something other than the money. All of it describes what businesses chose and who they were. A bigger Prize comes with a bigger business, so none of it says a bigger Prize would lift a given campaign.

Below 5,000 USD, a 1% bigger Prize buys a quarter to a half of a percent more Entrants. Past that point, extra Prize spend still buys more Entrants in most industries, just far less per dollar. Name both exception industries whenever this ceiling is cited, and do not treat it as a rule for every industry.

| Spend level (USD) | Extra Entrants per 1% bigger Prize | Campaigns | Businesses |
|---|---|---|---|
| 250 to 4,999 (four bands) | 0.24 to 0.53 | - | - |
| 5,000 and up (four bands) | 0.06, 0.08, 0.02, 0.11 | 710 down to 72 | 378 down to 49 |

The same flattening shows up within plan tier and within some industries, at the 5,000-9,999 USD spend level. It does not hold in gaming and esports or sports and outdoors, where value kept predicting more Entrants through this dataset's biggest campaigns, so a campaign in either industry is not up against this ceiling.

| Cut, at 5,000-9,999 USD (unless noted) | Extra Entrants per 1% bigger Prize | Campaigns | Businesses |
|---|---|---|---|
| Pro tier | -0.00 | 284 | 181 |
| Business tier | -0.08 | 329 | 207 |
| Electronics and tech | -0.31 | 139 | 71 |
| Media and entertainment | -0.42 | 47 | 30 |
| Gaming and esports (exception, still rising) | 0.55, and 0.13 at 10,000-24,999 | 83 | 42 |
| Sports and outdoors (exception, still rising) | 0.19, then 0.26 at 10,000-24,999 | - | - |

A cheap Prize is not a mark against a campaign on this measure: at the cheaper spend levels, campaigns beat their own typical Entrant count for the money by 50% or more more often than they miss it by as much. That margin is what a small budget buys here, a real chance of outperforming its own price tag, and it is the right call when the audience in front of the campaign already wants what's on offer and the objective does not need the largest possible crowd. It reverses at the top, so the same margin does not carry into the largest budgets. This describes campaigns that already cleared this reference's 100-Entrant floor, two things happening together and not a test of what a cheap Prize would do in front of a smaller audience.

| Spend level (USD) | Beat by 50%+ (crowd/$ 1.5+) | Missed by 50%+ (crowd/$ below 0.667) | Campaigns |
|---|---|---|---|
| Under 50 | 29% | 20% | 246 |
| 250 to 499 | 27% | 17% | 2,132 |
| 50,000 and up (reversed) | 40% | 44% | 72 |

## Prizes for a store

- **Own product at cost.** The stated value is retail, your cost is wholesale, and the Entrant who wanted it is already a customer. That is the trade: margin spent, not list price, for a Winner who fits your audience by definition. Once campaign size and industry are held constant, the mechanic costs quality: it stands lower than a bought-in Prize on Conversion Rate, on crowd per Prize dollar and on cost % of Entrants (see the own-product finding above), though raw Entrant count and email signups hold up. That cost reverses in electronics and tech, is flat in sports and outdoors, and on Conversion Rate alone it turns in own product's favor above 2,500 Entrants. It fits best when the objective is a buyer, not the largest crowd at any cost, and least when the objective is pure reach and margin can't absorb a discount.
- **Win your cart up to a cap.** The Prize is whatever the Winner put in the cart, capped at a stated number. The cap is the budget, and the title carries it. Cart and wishlist campaigns sit at 1.43 on crowd per Prize dollar, about 43% above typical for the money and the second highest figure of any campaign type, on 451 valued campaigns of 903. They also draw 725 Entrants against a typical 492. Price them as a wishlist and browsing play that also reaches. [`analysis/output/campaign_types.json`, `types`.]
- **Gift card to your own store.** Costs the margin on what the Winner spends, and the Winner comes back to spend it. Gift card campaigns post 1.17 on crowd per Prize dollar, about 17% above typical for the money, on 6,791 valued campaigns of 11,100, while drawing fewer Entrants than typical at 432. A gift card to someone else's store buys reach and sends the Winner elsewhere. [`analysis/output/campaign_types.json`, `types`.]
- **Discount codes as the headline Prize.** 1,054 campaigns, 0.73 on crowd per Prize dollar (about 27% below typical for the money), and a purchase condition dressed as a Prize. Use codes for everyone who did not win, under a real Prize, and read giveaway-winner-communications for the mechanics. [`analysis/output/prize_economics.json`, `by_prize_category`.]
- **Ship the Prize as an order.** Create the Winner's Prize as a zero-value order in the store so it goes out through the normal pick, pack and tracking flow, and the Winner sees it in their account.
- **Fourth quarter.** Reserve the Prize stock before the sale sells it out. Close a December draw at least a week before the carrier's cutoff, and where that is not possible make the Prize a gift card so the Winner still has it by the day.
- **Budget line for the codes.** A store campaign has two costs: the Prize, and the discount taken up by non-Winners. Put the second in the budget as redemptions expected times average discount, and read the redemption count as the campaign's revenue line afterwards.

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
- Copying a big campaign's Prize. A local business does not need the typical figures from campaigns of 10,000 Entrants and up. Half of all campaigns in this skill's data ran at a fraction of that size and Prize spend (see the budget template above). The cheap Prizes that drew crowds cut in giveaway-idea-generator lists 114 campaigns under 250 USD that passed 5,000 Entrants, and the campaigns that beat their Prize money cut sits next to it. Both point the same way: the audience in front of the Prize did the work, and most of those businesses had run campaigns before [four in five].

## When the Prize is unrelated to the business

Ask what the objective is. If it is reach and the follow-up can qualify the audience, an unrelated popular Prize can work, ideally tied to the brand (branded edition, bundled with own product, framed around a use the brand serves). If the objective is leads or sales, prefer a Prize that filters for interest: own product, a category-specific item, or store credit. Say plainly that the dataset cannot show which choice performs better.
