# Qualified Entry for Buyer Campaigns

Advice unless marked as extracted. This file is for the campaign where 40 right Entrants are worth more than 4,000 wrong ones: a B2B giveaway, a high-ticket service, a product only one kind of business can use. The rest of this library scores a campaign by the crowd it drew. This file does not, and the last section says what to measure in place of it.

## What the Data Holds (extracted)

From `analysis/output/industries.json`, `by_audience`. The audience label is an assistant's reading of each organizer's homepage text, so it is an inference and never a choice the business made. This cut runs wider than the 116,499 campaigns behind most of this library, so read its campaign counts as that wider set. Every row clears five distinct businesses.

<!-- generated:qe_audience -->
| Audience | Campaigns | Businesses | Entrants (typical) | Conversion Rate | Days | Methods | Referral entries % of Entrants | Email offered | Email signups % of Entrants, where offered |
|---|---|---|---|---|---|---|---|---|---|
| B2B | 12,728 | 1,779 | 606 | 29.5% | 11 | 7 | 44 | 19% | 92 |
| B2C | 105,282 | 15,582 | 526 | 26.4% | 14 | 7 | 16 | 34% | 100 |
| Both | 3,832 | 511 | 668 | 28.1% | 10 | 7 | 46 | 19% | 82 |
<!-- /generated -->

[Typical values per campaign. Conversion Rate is Entrants over Impressions across all runs, so long and repeatable campaigns sit lower. Email signups are counted only in campaigns that offered the action. Source: `analysis/output/industries.json`, `by_audience`.]

Four limits, stated before anything is built on that table.

- It describes what B2B businesses chose. The data ends at the entry, so it holds nothing on whether an Entrant was a buyer, took a sales call, booked a meeting or became a customer. No figure in this library says a B2B campaign produced a qualified lead.
- Every campaign in it drew at least 100 Entrants, and the typical B2B campaign drew the figure in the table. A campaign aimed at a few dozen sits below anything measured, so no figure here describes it and none can be held against it.
- Campaigns are not spread evenly across businesses, and the audience label is separate from the business type in `mix-by-objective.md`, so a software business can sit in both rows. Many campaigns come from a few businesses, so read each figure as a typical campaign.
- No output in this repository splits Entrants by work email against free mail. The only email-domain data is inbound traffic from mail clients (`analysis/output/email_traffic.json`), which says where a visitor clicked from and nothing about the address an Entrant typed. How many Entrants use a company address, and whether a company address goes with a buyer, is not something this library measures. Nobody should quote a split for it.

Everything below this line is practice, common practice with nothing in the data behind it. Say so when you pass it on.

## Say Who the Campaign Is For (advice)

Write the buyer in one sentence before anything else, naming a role, a kind of company and a problem. "Operations leads at warehouses with 50 to 500 staff who still count stock by hand" is a buyer. "Business owners" is a crowd.

Put that sentence in the campaign title, the first line of the description, the Prize name and the eligibility line in the terms. Say who is out of scope in the same place ("Open only to people buying for a business"). A campaign that names its buyer will draw fewer Entrants, and that is the intent. The people who skip it were never the target.

Where the campaign is promoted decides who sees the sentence, and that belongs to giveaway-promotion-plan. LinkedIn bans giveaways in its own policy, so do not run entries through its posts or comments (`platform-promotion-rules.md`).

A giveaway builds a pool of the right people. It is a poor tool for reaching a short list of named accounts, since direct outreach can be pointed at those and a giveaway cannot.

## Keeping the Wrong People Out, or Telling Them Apart (advice)

A gate stops someone entering. A sort lets everyone enter and tells you which Entrants are buyers. A gate costs real buyers too, so use the lightest one that works and sort for the rest.

| Tool | What it does | What it costs | Use it when |
|---|---|---|---|
| Eligibility line in the terms | Sets who may win, enforces nothing alone | Nothing at entry | Always. It is the line you point to when you disqualify a Winner. |
| Verify before the draw | Checks the company and role of each Entrant who would win | Staff time after the close | Always for a Prize of real value. Name the check in the terms, and ask counsel how to word it. |
| Work-email requirement | The form rejects free-mail addresses | Turns away real buyers who enter from a personal address, such as a sole trader or a freelancer. A domain check says nothing about whether the person works there. | Sales cannot handle a mixed list and you would sooner lose some buyers than call hunters. Check that your platform supports domain rules. |
| Company name field, required | Asks who the Entrant works for | One more required field | Sales will look the company up in the first week |
| Role or size field, as a choice list | Sorts by seniority or company size | One more field | The answer changes who calls |
| Qualifying question | Sorts by need | See the next section | Nearly always |
| Fraud and duplicate filter | Flags repeat and automated Entries | A filter can flag a real Entrant, so read the flagged list before the draw | Always on |

The default is to sort. Let any address enter, then tag each Entrant in the CRM by whether the domain looks like a company or a free-mail provider, and by the answer to the question. The tag costs the Entrant nothing, and it keeps the buyers a gate would have lost. Gate on work email only when you have decided that losing some buyers is the price of a cleaner list, and tell the sales team that was the decision.

## The Qualifying Question (advice)

One question, about the business and never about the person. It should be easy for someone with the problem and slow for someone inventing an answer. Never ask for health, financial or other regulated personal data in it. A healthcare buyer's question is about the clinic's workflow and leaves patients out.

- **Use a choice list of three to five bands plus "something else".** "How do you count stock today? A spreadsheet, a barcode scanner, an inventory system, we do not count it." A buyer picks without thinking and the answer sorts them.
- **Avoid the question everyone answers the same way.** "Do you want to grow your business?" sorts nobody.
- **Leave out a right answer.** Nobody should lose on the answer. Use it to tier, and never to reject. Trivia, the one question type with a right answer, was completed by the fewest Entrants of any type, about 62% (1,640 actions from 325 businesses, `mix-by-objective.md`).
- **Make it the one required action.** Take the email address from the entry form and keep marketing permission as a separate tick (see the consent section of `mix-by-objective.md`).

For the cost to entries, `mix-by-objective.md` has the question-type figures. An open or feedback question was completed by a typical 86% of Entrants (839 actions, 374 businesses), a preference question by 70% (3,475 actions, 898 businesses) and a detail-capture question by 68% (6,755 actions, 851 businesses). Two more figures sit in that file. Question-only campaigns recorded a typical Conversion Rate of 45.6% (2,464 campaigns, 403 businesses), below bonus-only campaigns at 52.2% (2,428 campaigns, 639 businesses). These are single-family campaigns in the source table, with no measurement of buyer quality. The top fifth by email signups per Entrant offered a question less often than the rest, 5% against 11%. All of it describes what businesses chose, and none of it says what your question would do.

## What to Require and What to Leave Optional (advice)

| Item | Required or optional | Reason |
|---|---|---|
| The qualifying question | Required | It is the sort. Ask one. |
| Email address | Collected by the entry form | It is how you reach them. Marketing permission is a separate tick. |
| Company name | Required if sales will look the company up before calling, otherwise optional | Every required field is one more place to stop |
| Role | Optional, or build it into the question's choices | The question can carry it |
| Phone | Optional | Require it only when a person will ring within the week |
| Company size | Optional, or look it up from the domain after entry | Asking costs a field the lookup may already answer |
| Visit the pricing or a case study page | Optional, one entry | It shows intent and costs the Entrant a click |
| Refer a colleague | Optional, low weight | The colleague enters through the same form and answers the same question |
| Follows, reposts, tag a friend | Leave out | They add Entrants who followed to enter, and no list you will use |
| Daily, repeatable or secret-code actions | Leave out | They reward effort, and effort does not show who needs the product |
| Bonus entries for effort | Keep optional actions at low weight | Extra completions still add tickets and increase draw chances |

Where the buyer's employer may have rules about gifts, reviews or referrals, drop the referral action and the review ask, and say why. That is the same advice as the B2B row in `mix-by-objective.md`, and a regulated buyer may have more rules again. If you sell to public bodies, ask them first. Nothing here says what any employer allows, so put the question to the buyer's employer or to counsel.

The Action-count table in `mix-by-objective.md` covers 38,463 campaigns. Conversion generally fell as Action count rose, with increases between some adjacent counts and a rise at the upper end. It does not measure the effect of adding a required form field. As practical buyer-selection advice, ask only for fields that change qualification or follow-up. A qualifying question helps sort buyers, without a measured promise about conversion.

## What Happens to the Entrants Afterwards (advice)

Settle this before launch. Name a person for each tier and a deadline for the first message.

| Tier | Who | Who contacts them | How fast |
|---|---|---|---|
| A | A company-looking address or a role you sell to, and an answer that shows the need | A named salesperson, with a message that names the giveaway and asks one question | Set a number of hours before launch. The same working day is a sound start. |
| B | Fits on one count and misses the other | Marketing's nurture series. Sales picks up on a reply. | Within a few working days |
| C | A free-mail address and an answer that does not fit | The newsletter, only if they ticked marketing permission | None |

The hours and days in that table are judgement, with nothing in the data behind them. What matters is that a number exists, that a named person holds it and that someone checks it.

- **Tag every Entrant in the CRM** with the campaign name and the tier. Without that tag nobody can count outcomes later, and the scorecard below cannot be run.
- **Keep the Prize and the sales call apart.** The Winner gets the Prize process. The sales message comes separately, so that nobody reads the Prize as bait.
- **Give every qualified non-Winner a reason to talk.** One Winner means almost every qualified Entrant leaves with nothing. A useful offer for them, such as a short audit or a trial extension, is where most of the pipeline comes from, and giveaway-winner-communications writes it.
- **Check the consent before the first sales message.** Rules on contacting a business address differ by country and by whether the person ticked marketing permission. Put one question to counsel: may a salesperson contact an Entrant who gave an address to enter and did not tick the marketing box, in each country the campaign is open to?
- **Run the first 30 days** from the using-what-you-built section of `mix-by-objective.md`, with the segment, the sunset rule and the consent record.

## What to Measure in Place of Crowd Size (advice)

Entrants, Conversion Rate, Entries per Entrant, the percentile ranks in the results review and crowd per Prize dollar all rise with a bigger and cheaper crowd. None of them measures a buyer campaign, so set them aside. The data starts at 100 Entrants, and a reader whose whole addressable audience is small is not underperforming by reaching a small share of it.

Measure these, all practice, and fix the definitions before the first Entry arrives.

| Measure | How to count it | Set before launch |
|---|---|---|
| Qualified Entrants | Entrants who match the one-sentence buyer definition | The definition itself, written down. One changed after the results is a scorecard fitted to them. |
| Qualified share | Qualified Entrants over all Entrants | Nothing. Watch it, since a low share says the promotion reached the wrong people. |
| Cost per qualified Entrant | Everything spent (Prize, promotion, staff time) over qualified Entrants | The cost per lead the business pays elsewhere. That number is the reader's, so ask for it and never invent one. |
| Time to first contact | Hours from entry to the first message, by tier | The number in the tier table |
| Replies and meetings | Qualified Entrants who replied, and who booked, inside a window | The window |
| Pipeline | Opportunities opened and their value, by campaign tag | Reading dates, such as 30, 60 and 90 days after the draw |

For the break-even, divide the total cost by what one qualified lead is worth to the business, using the business's own figure. The result is how many qualified Entrants the campaign needs. The cost-per-email benchmarks in the Prize picker are per email across every Entrant, so do not set a cost per qualified Entrant against them.

A campaign that draws 4,000 Entrants of whom 3% qualify has 120 qualified Entrants. Report the 120 as the result and the 4,000 as a footnote. The reverse order is how a buyer campaign gets judged by a crowd measure it was built to ignore.

## An Example Entry List (illustrative)

Built by hand to show the shape, and not taken from any campaign in the data. The buyer is a warehouse operations lead. This example leaves out social follows because they do not help qualify or follow up with the buyer. The job column states the purpose in plain words.

| Action | Job | Required or optional | Entry weight | What it produces |
|---|---|---|---|---|
| Answer the stock-counting question | Identify the buyer | Required | 1 | A sorted Entrant |
| Entry form with company email and company name | Collect a contact | Collected on the entry form | none | A contact to tag by tier |
| Visit the pricing page | Show the product and pricing | Optional | 1 | An intent signal |
| Refer a colleague | Bring in referrals | Optional | 1 | A second Entrant who answers the same question |

This example uses an entry-weighted draw. One completed action earns one ticket and three earn three tickets, so optional actions increase the chance of winning. If equal chances are the goal, state one ticket per distinct eligible person in the terms and do not award draw tickets for optional actions.

The Prize that makes this list worth entering is the job of giveaway-prize-picker, and a Prize anyone would take undoes the sort.
