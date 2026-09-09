# Decision criteria

Everything here is general advice unless a sentence is marked as a dataset finding.

Four USD tables sit in this repository and each answers a different question. Use the one that matches what is being asked.

| Table | Where | The question it answers |
|---|---|---|
| Stated prize cost per email signup by prize category | below, in this file | For the kind of prize we are considering, what did organizers declare per address captured? |
| Stated prize value per contestant, per email, per follow and per referral entry by vertical | `references/roi-benchmarks.md` | For our industry, what did a result cost at the median? |
| Stated USD prize values by category and campaign size band | `references/prize-values-by-category-and-size.json` | For a campaign of our expected size in our category, what did organizers declare? |
| Value index by prize category and by number of prize units | `references/evidence-and-limitations.md` | Once the money is held constant, which categories and structures drew more people than their price tag suggests? |

The first three price a result. The fourth ranks categories after the budget is stripped out, so it is the table to reach for when the question is one prize against another at the same spend.

## Six criteria

Rate each candidate prize on all six. A prize that fails accessibility or fulfillment is out regardless of desirability.

| Criterion | Question | Common failure |
|---|---|---|
| Audience relevance | Would the people you want to reach want this more than a random person would? | Generic electronics that attract sweepstakes hobbyists instead of customers |
| Desirability | Is it wanted enough to justify the entry effort you ask for? | A discount code or low-value merch positioned as a "grand prize" |
| Connection to the business | Does winning (or seeing) the prize teach entrants what you sell? | Prize that never mentions or uses the product |
| Accessibility | Can the entrants you target legally and practically receive it? | Alcohol, firearms, age-gated goods, region-locked services, travel needing visas |
| Fulfillment practicality | Can you ship, book or deliver it within the promised window? | Bulky or perishable goods across borders; experiences with blackout dates |
| Total cost | Retail value plus shipping, duties, taxes on the winner, staff time, partner obligations, and a substitute if the item is unavailable | Budgeting the sticker price only |

## Broad versus specialized appeal

Broad appeal (cash, gift cards, phones, consoles) is appropriate when the objective genuinely is reach: awareness for a mass-market product, a launch where the product itself is the broad prize, or list-building where you accept churn and will qualify later. Specialized appeal (own product, category-specific gear, expert experiences, access) fits lead generation for a defined niche, retention, community growth and UGC, where the value of an entrant depends on who they are.

Expect a broad prize to bring entrants who never buy. That is acceptable when the objective needs reach and the follow-up handles the mismatch. It becomes a problem when the leads go straight to a sales team.

Extracted: 21% of clean-subset campaigns showed an own-product signal in the prize name (n=2,429). Their median contestants were 2,020 against 2,082 for bought-in prizes, with 4.1 entries per entrant against 3.4 and conversion of 34% against 39%. Giving away your own product came with about the same number of entrants as buying a prize in, and those entrants completed more actions. That describes what organizers saw, with no comparison group of failed campaigns. The taxonomy reference reports the same flag at 18.1%, counted over prize records across all ordinary campaigns, while the 21% here counts campaigns in the clean subset, so the two figures measure the same weak signal on different bases and neither supersedes the other.

### Prize hierarchy (advice, from Gleam's campaign team)

This ordering is one operator's working practice, written down by the team that runs campaigns on the platform. Nothing in the export tests it. Treat it as a starting shortlist a practitioner would defend, and drop any rung the business has a reason to drop.

A default order to consider, adapted to the business: an audience-specific hero prize, then your own product plus the aspirational thing your customer wants next (coffee plus an espresso machine, supplements plus a sports watch, skincare plus a beauty device), then own product or own-brand credit, then an exclusive or limited item, then category-specific equipment, then a relevant collaboration bundle, then generic technology, then cash, then a generic gift card. The question that finds the adjacent prize: what does the customer's ideal day contain right before or after using this product?

Collaborations work when they pass one test: same customer, different product. Extracted: campaigns whose title signals a collaboration ("x", "collab", "partner") had a value index of 1.13 against 0.99 for the rest, and reached the top fifth 29% of the time against 19% (n=1,195, a title proxy). Value index means a campaign's contestants divided by the median contestants of its stated-value band, so 1.00 is typical for the money.

## Structure tradeoffs

Default for an acquisition giveaway: one prize worth wanting. Extracted, on the value index: one-unit campaigns index 1.07 against 0.85 for six to twenty units, in the value index by number of prize units table in `references/evidence-and-limitations.md`. Split the budget only when the units are the point: sampling, digital prizes, community rewards, or tiers that make the campaign read better.

| Structure | Strengths | Costs and risks |
|---|---|---|
| One major prize | Simple story, strongest headline, easiest fulfillment | Perceived odds are worst; one unhappy winner is the whole outcome |
| Several equal winners | Better perceived odds, more social proof, more product in more hands | Headline value is split; fulfillment multiplies |
| Tiered (1st, 2nd, 3rd) | Headline plus odds; natural for partner bundles | More admin; lower tiers must still be worth wanting |
| Bundle around your product | Raises headline value cheaply with partners; teaches your category | Partner obligations; substitutes needed if items go out of stock |
| Recurring (daily, weekly) | Keeps a long campaign alive; good for content series | Requires repeated draws and announcements |

Dataset observation (extracted, ordinary segment): 79% of campaigns listed one prize record, 32% listed a quantity above one for at least one prize, and 8,761 of 37,180 campaigns listed five or more prize units. Contestant medians for single-winner and multi-unit structures were almost identical (2,228 vs 2,270), which says nothing about effect because every campaign passed the export floor. Those raw medians and the value index by number of prize units are the same campaigns seen two ways: raw, one unit and many units drew the same crowd, and once the money is held constant, one unit sits above par and six or more below. The value index table in `references/evidence-and-limitations.md` carries the second view, and it is the one to quote when a budget is fixed.

## Stated prize cost per email signup (extracted)

For campaigns with an email action and every prize valued in USD, the stated pool divided by email signups. Music gear and cash sit lowest, experiences and game items highest. Use it to sanity-check a budget against the list it is meant to build, and remember the stated value is what the organizer wrote.

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

Dataset reference ranges (extracted, ordinary segment, stated USD values only, n=24,365 of 60,282 prize records, and 60% of records have no stated value): median 299, interquartile range (IQR, the middle half of records between the 25th and 75th percentile) 100 to 864, 90th percentile 2,042, meaning nine records in ten declared less than that. Fully valued campaign totals (n=14,538): median 900, IQR 329 to 2,000. By campaign size the total-value medians are 525 (1k to 2.5k contestants), 1,297 (2.5k to 10k) and 3,000 (10k+). Bigger campaigns declared bigger prizes, and bigger organizers run bigger campaigns, so read that as who runs what, never as a price of admission.

What the export shows about value and category (extracted, clean subset of 11,636 campaigns with no repeatable actions and runs of 14 days or less, medians against the subset median): a first prize stated under 100 USD ran 23% fewer contestants, 500 to 1,999 USD ran 9% more, and 2,000 USD or more ran 86% more with conversion about 20% lower. Merch and apparel campaigns ran 32% more contestants, tech hardware and experiences 11% more, home and garden converted 16% better. Campaigns started in December ran 15% more contestants and converted 23% better despite the crowded month. All of it describes what organizers chose and who they were. A bigger prize comes with a bigger organizer, so none of it says a bigger prize would lift a given campaign.

## Prizes for a store

- **Own product at cost.** The stated value is retail, the cost is wholesale, and the entrant who wanted it is a customer. The own-product finding above (21% of clean-subset campaigns, contestants close to bought-in prizes, more entries per entrant) is the case for it.
- **Win your cart up to a cap.** The prize is whatever the winner put in the cart, capped at a stated number. The cap is the budget, and the title carries it. Cart and wishlist campaigns sit at a value index of 0.93 on 213 valued campaigns, so price them as a wishlist and browsing play, not a reach play.
- **Gift card to your own store.** Costs the margin on what the winner spends, and the winner comes back to spend it. Gift card campaigns post an index of 0.98 on 1,559 valued campaigns. A gift card to someone else's store buys reach and sends the winner elsewhere.
- **Discount codes as the headline prize.** 492 campaigns, index 0.78, and a purchase condition dressed as a prize. Use codes for everyone who did not win, under a real prize, and read giveaway-winner-communications for the mechanics.
- **Ship the prize as an order.** Create the winner's prize as a zero-value order in the store so it goes out through the normal pick, pack and tracking flow, and the winner sees it in their account.
- **Fourth quarter.** Reserve the prize stock before the sale sells it out. Close a December draw at least a week before the carrier's cutoff, and where that is not possible make the prize a gift card so the winner still has it by the day.
- **Budget line for the codes.** A store campaign has two costs: the prize, and the discount taken up by non-winners. Put the second in the budget as redemptions expected times average discount, and read the redemption count as the campaign's revenue line afterwards.

## Fulfillment checklist

- Eligibility: countries, states, age, employees excluded, one entry per person rules.
- Delivery: who ships, insured or not, address verification, replacement policy for damage.
- Insurance on a high-value physical prize: insure it for the replacement cost while it is in transit, use a tracked and signature-required service, and budget the premium as a line in the prize cost. A lost console is a refund. A lost 3,000 USD hero prize is a public failure with a named winner waiting.
- Timing: draw date, response deadline for winners, redraw policy, delivery window.
- Substitution: "prize of equal or greater value" clause when stock is uncertain.
- Experiences: dates, blackout periods, travel included or not, companion allowed, transferable or not.
- Digital prizes: region locks, platform accounts, expiry.
- Disclosure: retail value, taxes, sponsor, and terms. Sweepstakes and lottery law differs by jurisdiction, so recommend the user confirm local rules. This skill does not give legal advice.

## Common mistakes

- Choosing the prize before the objective. A prize picked for its headline pulls whoever wants that item. Decide what the entrants are for, then pick.
- Budgeting the sticker price. Shipping, duties, winner-side tax, a substitute unit and staff time routinely add 20 to 40 percent to a physical prize.
- Inflating "retail value". Entrants and regulators can check. State the price a buyer would pay today, and treat "lifetime" or "a year of" values as retail, with your cost kept separate.
- No eligibility terms. Countries, age, employees, one entry per person, and what happens if a winner does not respond. Missing terms are where disputes start.
- Promising entrant numbers. Volume comes from promotion, audience size and entry friction. No prize guarantees it, and this dataset cannot show that any prize caused participation.
- Regional or regulated prizes offered globally. Alcohol, firearms, gift cards locked to one country, or travel that needs visas. Check the accessibility criterion before the headline.
- One prize, many objectives. A single PS5 cannot both build a niche email list and drive mass awareness. Pick one objective per giveaway.
- Copying a big campaign's prize. Half the campaigns in this skill's data had between 1,000 and 2,500 entrants and a median declared total of about 525 USD. A local business does not need the 3,000 USD medians of the 10,000-plus band. The cheap prizes that drew crowds cut in giveaway-idea-generator lists 129 campaigns under 250 USD that passed 5,000 contestants, and the campaigns that beat their prize money cut sits next to it. Both point the same way: the audience in front of the prize did the work, and four in five of those organizers had run campaigns before.

## When the prize is unrelated to the business

Ask what the objective is. If it is reach and the follow-up can qualify the audience, an unrelated popular prize can work, ideally tied to the brand (branded edition, bundled with own product, framed around a use the brand serves). If the objective is leads or sales, prefer a prize that filters for interest: own product, a category-specific item, or store credit. Say plainly that the dataset cannot show which choice performs better.
