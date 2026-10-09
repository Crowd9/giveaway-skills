# Prizes That Filter for a Buyer

Advice unless marked as extracted. This file is for the campaign where 40 right Entrants are worth more than 4,000 wrong ones, most often a B2B giveaway. The Prize is the whole game there. Cash, a gift card or a console suits reach, and `decision-criteria.md` expects a broad Prize to bring Entrants who never buy. A Prize that only a buyer values is the first filter, ahead of any form.

## What the Data Holds (extracted)

From `analysis/output/prize_timing_cuts.json`, `by_prize_category`, campaigns of 100 or more Entrants. The category is our reading of the Prize name, so it is an inference and never a label the business chose. Every row clears five distinct businesses.

<!-- generated:bp_categories -->
| Category | Campaigns | Businesses | Typical Entrants | Conversion Rate |
|---|---|---|---|---|
| Tech hardware | 20,219 | 4,504 | 923 | 28% |
| Gift card or cash | 20,137 | 4,485 | 433 | 25% |
| Bundle or box | 11,188 | 3,177 | 470 | 27% |
| Experience, travel, tickets | 5,676 | 1,675 | 380 | 25% |
| Subscription or membership | 1,123 | 586 | 372 | 24% |
| Exclusive access | 450 | 268 | 333 | 28% |
<!-- /generated -->

[Typical values per campaign. Conversion Rate is the share of people who saw the campaign and entered. Source: `analysis/output/prize_timing_cuts.json`, `by_prize_category`.]

Campaigns that gave away a subscription or membership drew a typical 372 Entrants, against 433 for gift cards and cash and 923 for tech hardware.

Source: `analysis/output/prize_economics.json`, `by_prize_category`, `subscription_membership`.

Crowd per Prize dollar for subscriptions was 0.51 across 1,559 campaigns (`prize-taxonomy.md`).

Source: `analysis/output/vertical_profiles.json`, `prize_category_index_by_industry`, `software_saas.subscription_membership`.

Inside software and SaaS the category sat at 0.24 across 60 campaigns from 29 businesses, where the all-industry figure for it is 0.47. Those are crowd measures, and a buyer campaign should set them aside. Nothing in the data says whether the smaller crowds held a larger share of buyers.

Source for the category-fit comparison below: `analysis/output/prize_economics.json`, `audience_fit`, `audience_specific` and `generic`.

Four limits on what that shows.

- The data ends at the entry, so no row says who the Entrants were, whether they bought or whether a Prize was ever collected by a buyer.
- The taxonomy has no row for a service Prize such as an audit, a migration or a consultation. Nothing here describes how those campaigns went.
- A Prize in the business's own category came with a typical 673 Entrants against 463 for a generic Prize (21,264 and 36,845 campaigns, `decision-criteria.md`). A Prize that fits the business has not shown up as a small crowd. A Prize only a buyer values is narrower than a category match, and the data cannot tell the two apart.
- A bigger Prize pool went with a bigger crowd (`decision-criteria.md`, with the limits that file lists). A buyer campaign is not buying crowd, so size the Prize to the work it costs you and stop there.

The rest of this file is practice, common practice with nothing in the data behind it. Say so when you pass it on.

## What a Buyer Wants That a Hunter Does Not (advice)

The test is one question, and it is whether someone with no use for the product would still want this. A yes means the Prize recruits them as readily as it recruits buyers, and the campaign will fill with people who never needed what you sell. `decision-criteria.md` makes the same point for any lead campaign, and a gift card or a console fails it.

| Prize | Why a buyer values it | Catch |
|---|---|---|
| The product at the tier a buyer would buy: an annual plan, a set of seats, a module | It is the answer to the problem | A Winner who is not a fit still uses it, so verify before the draw. State retail value honestly and keep your own cost separate. |
| A done-for-you service: an audit, a migration, an implementation sprint, a workshop for their team | It saves them time they cannot get another way | Staff time is the cost. Cap it, put a date on it and say what it covers. |
| Time with someone senior: an advisory session, a seat at a closed roundtable | Access they cannot buy | The cost is that person's calendar. Fix the dates before launch. |
| A seat at a conference or a certification course | It matters to one profession | Travel, expenses and employer rules. Ask whether the buyer may accept it. |
| A report or benchmark cut for their segment | Information they would otherwise pay for | Cheap to send to everyone, which makes it the best consolation |
| A bundle of the above | Product, service and access in one | Price each part, and keep the bundle to what one Winner can use in a quarter |

A Prize anyone would take belongs to a different campaign. Cash, gift cards, phones and consoles suit reach. `decision-criteria.md` says a broad Prize brings Entrants who never buy, and that becomes a problem when the leads go straight to a sales team.

## The Prize Test (advice)

Put each candidate through four questions.

1. **Would a person with no use for the product still want it?** If yes, rework it.
2. **May the Winner's employer let them accept it?** Gift and ethics rules differ by employer, and nothing here says what any employer allows. Ask, or give the Prize to the company, as account credit or a service delivered to the business.
3. **Can you deliver it to a buyer in the time promised and the region they are in?** Use the fulfillment checklist in `decision-criteria.md`.
4. **Does winning teach them what you sell?** A Prize that uses the product does this for free.

Then price it to the work. Where a Prize carries a stated USD value, campaigns in the software industry stated a typical 1,000 USD pool (1,752 campaigns, 571 businesses, `roi-benchmarks.md`). That is a stated value and never what the business paid, and a buyer campaign has no reason to chase it.

## Making the Prize Hard to Use If You Are Not a Buyer (advice)

- **Name the Prize in the buyer's terms.** "A warehouse stock audit by our solutions team" says who it is for. "Win a Prize worth 5,000 dollars" does not.
- **Say who may win in the terms.** An eligibility line for people acting for a business, a non-transferable Prize and whether a cash alternative is offered. Wording for these is a question for counsel in each country, and giveaway-winner-structure holds the terms checklist.
- **Verify the Winner before announcing.** Ask for a work address and role at the claim step, say so in the terms, and redraw per the terms if the Winner does not fit.
- **Deliver it to the company.** Account credit and delivered services are used by a business. A physical item goes to a person.
- **Keep to one Prize.** The default in `SKILL.md` for acquisition holds here, and one Winner is easy to verify.

## Everyone Else Gets Something (advice)

One Winner means nearly every qualified Entrant leaves with nothing, and those Entrants are the pipeline. Put a consolation behind the main Prize that costs little to send and is useful to a buyer: the report, a shortened audit, a call with the team, a trial extension. `prize-taxonomy.md` treats a discount code as a consolation tier for a store. A buyer campaign needs one that moves a conversation forward. Budget the consolation as a line, with the cost times the expected number of qualified Entrants. giveaway-winner-communications writes the message, and giveaway-winner-structure covers tiers.

## Pricing a Buyer Campaign (advice)

- **Budget lines.** The Prize, the staff time to deliver it, the consolation and promotion where the buyers are. Run `scripts/budget.py` for the lines and count staff time as a cost.
- **Judge it per qualified Entrant.** Divide everything spent by the number of Entrants who match the buyer definition, and set the result against what the business pays for a lead elsewhere. That second number is the reader's, so ask for it and never invent one.
- **Find the break-even.** Divide the total cost by what one qualified lead is worth to the business, using the business's own figure. The answer is how many qualified Entrants the campaign needs.
- **Leave out the per-email benchmarks.** `scripts/roi.py` and `roi-benchmarks.md` price an email address across every Entrant, and a qualified Entrant is a smaller and different count. The entry-method side of the scorecard is in `qualified-entry.md` of giveaway-entry-method-planner.

## Evaluating a Prize Already Chosen (advice)

Run the four questions on it, then give a verdict of keep, adjust or replace. A console or a laptop offered to a B2B software audience fails the first question, since nearly anyone wants it. Say that plainly, then offer the replacement in the buyer's terms: a year of the product plus an onboarding session, an audit, or a team workshop. If the business insists on the consumer Prize, the adjustment is a business-only eligibility line, the qualifying question from the entry planner and verification before the draw. Say that the consumer Prize leaves the first filter off, and that the data cannot show what that costs.
