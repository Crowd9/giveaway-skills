# Drawing and fulfillment

Advice unless marked as extracted.

## Structure tradeoffs

Common practice, our data doesn't cover this. Choose one Winner when keeping the Prize whole preserves its appeal and keeps fulfillment manageable. Choose several when the units serve product sampling, digital Prizes, community rewards or daily draws. Set the count from the objective, unit value and delivery cost.

| Units | Campaigns | Crowd per Prize dollar | Entrants |
|---|---|---|---|
| One | 26,919 | 1.15 | 509 |
| Two to five | 10,192 | 0.82 | 463 |
| Six to twenty | 4,276 | 0.64 | 565 |
| Twenty-one or more | 1,566 | 0.77 | 1,065 |

[Extracted from `analysis/output/context_checks.json`, `winner_count_index_value_adjusted`.] The raw Entrants column runs the other way, highest in the largest unit-count group, where campaigns also stated larger Prize budgets. Both columns describe observed campaigns. Neither predicts what splitting one campaign's fixed budget would change.

| Shape | Choose it when | Cost |
|---|---|---|
| One Winner | The headline value matters and the Prize cannot be split | Worst perceived odds, one unhappy Winner is the whole outcome |
| Several equal Winners | Product trial, social proof, a consumable or digital Prize | Headline is split, fulfillment multiplies |
| Tiers | A partner supplies a hero item and the business supplies runner-up product | More admin, each lower tier must still be worth wanting |
| Recurring draws | A campaign longer than three weeks, or a content series | Repeated draws and announcements, Entrants may wait for later draws |
| Guaranteed small reward for all | Lead generation where the list matters more than the Prize | Cost scales with Entrants, the reward must be cheap and instant |

Extracted: three in five campaigns give away one unit, one in five use tiers, one in seven give away ten or more units.

## Sizing the count

Budget minus fulfillment (shipping, duties, substitutes, admin time) gives the Prize pool. For a cash budget and one Prize type, the count is the whole number below (budget minus contingency) divided by (unit cost plus per-recipient fulfillment), and the contingency covers one replacement and one redraw's postage. Work it before the terms name a number of Winners, since the terms fix it. Divide until each Prize is still something the audience would enter for. Three Prizes worth 100 each beat ten worth 30 when the audience shops at 100. Digital Prizes and own product at cost let the count rise without the budget rising.

## Draw rules

- Random draws: use a method you can show (a platform draw, a published random-number source, a recorded screen). State the date and time with a time zone.
- Judged entries: publish the criteria before launch, name the judges or their roles, and keep a scoring record.
- Verification before release: check the winning entry completed the required action, the Entrant is eligible, and one person did not enter under several names. Apply the settled eligibility and reserve procedure where it fails.
- Duplicates and fraud: say in the terms that entries from automation, duplicate accounts or ineligible regions are void.

A drawn name has a real chance of failing verification. The typical campaign has 4.2% of entries marked invalid, and campaigns with a referral action run higher. Draw from valid entries only, verify the drawn entry against the terms before naming anyone, and keep backups for the ones that fail.

[Extracted from 107,109 campaigns and 16,490 businesses. 45% of campaigns had 5% or more invalid. Count source: `analysis/output/invalid_share.json`.]

## Contact and redraw

When a Winner has already gone quiet, start with the deadline in the published terms and the notice they received. A seven-day example belongs in the assumption line only while their deadline is unknown. If no deadline was given, agree the next step before sending a new dated notice. Do not apply a new deadline retroactively.

- Contact by the channel the Entrant gave. Two attempts, the second sent halfway to the reply deadline. The
  schedule is written out here so nobody has to work it out mid-answer:

| Reply deadline in the terms | First message | Second message | Forfeit at |
|---|---|---|---|
| 7 days (the platform default) | day 0 | day 3 or day 4 | end of day 7 |
| 72 hours | hour 0 | hour 36 | hour 72 |
| 48 hours | hour 0 | hour 24 | hour 48 |

  Halfway means halfway. On a seven-day deadline the second message goes on day 3 or 4, never on day 5.
- Terms that name no reply deadline. Propose one to the reader before the first message goes out, and propose seven days: it is the platform default, and 93.4% of the 115,361 campaigns whose terms record the setting kept it (`analysis/output/winner_terms.json`, `terms_timetable`). State it in the first message with a date and time zone, since a deadline the Winner never saw is not one you can hold them to.
- Reply deadline in the terms. When it passes, the Prize is forfeited and passes to the first backup drawn under the same audit record, as `winner-verification.md` sets out. A fresh draw after the fact breaks the commitment made before the first one, so it is the last resort, for when no backups were drawn.
- Keep a written log of draws, contacts and responses. Disputes are settled by the log.
- Never publish a Winner's full details without consent. First name and city, or a handle, with permission.

## Announcement

- Announce on the channels used to promote after verification and acceptance, naming the Winner only with publication consent. If they decline, announce confirmation without their name. Follow the published terms for timing. If confirmation takes more than a week, send a pending-confirmation update under those terms: "The draw is complete and Winner confirmation is still in progress. We will share the result once confirmation is complete." Allow any reserve their full response window before announcing a confirmed Winner.
- Thank Entrants and, when the objective was leads, give everyone something small (a code, a guide) so the list stays warm.
- Ask Winners for a photo or a line of feedback, and only use it with permission. The photo and review request in giveaway-winner-communications is the wording for it, sent about a week after delivery, and it is the step that turns one Winner into a repeat customer and a piece of proof for the next campaign.

## Fulfillment

- Delivery window in the terms. Ship tracked and insured for anything valuable.
- Substitution clause: "a Prize of equal or greater value if the stated Prize is unavailable."
- Say who pays duties, import tax and any tax on the Prize. Some jurisdictions tax Prizes as income.
- Experiences: dates, blackout periods, travel included or excluded, transferability.
- Digital Prizes: region locks, platform accounts, expiry.

## How many businesses write their own terms (extracted)

About two in five ordinary campaigns write their own terms in place of the platform default. Custom-terms campaigns run larger and convert lower than campaigns on the platform default, among the campaigns we can compare fairly. That describes who writes terms, not what terms do. Larger and more careful businesses write their own. It says nothing about the terms causing either figure.

| | Custom terms | Platform default |
|---|---|---|
| Typical Entrants | 591 | 401 |
| Campaigns | 13,562 | 25,940 |
| Businesses | 2,094 | 5,792 |
| Conversion Rate | 30.9% | 36.9% |

Campaigns with custom terms drew about 47% more Entrants and got a smaller share of their viewers through. Both figures describe the businesses that wrote their own terms, which are the larger and more practised ones, so neither says that writing terms changes a result. [Extracted from `analysis/output/extra_cuts.json`, `custom_terms_clean`, among the campaigns we can compare fairly.]

Custom terms run long, and the generated draft below is far shorter, which is the point.

| Custom terms (45,528 campaigns) | - |
|---|---|
| Typical length | 1,249 words |
| Carry a no-purchase line | 62% |
| Carry an age line | 29% |
| Say worldwide or international | 29% |
| Say US only | 3% |

## Terms snippet to adapt

Fill the reply period, duplicate policy and reserve procedure from the settled terms. Preserve multiple chances legitimately earned under those terms. Use the first eligible pre-drawn reserve in the recorded order before considering a fresh draw under the agreed procedure. If any of these rules is unsettled, mark it for agreement before publishing.

"Winners are selected at random from valid entries on [date, time, time zone] using [method]. Winners are notified by [channel] within [N] days and must respond within [agreed reply period, with the deadline and time zone stated in the notice]. If a Winner does not reply or fails verification, [agreed reserve procedure]. Entries are checked under [agreed eligibility, duplicate-account and automation rules]. Multiple chances legitimately earned under the entry rules remain valid. Prizes are as stated, with no cash alternative, and the promoter may substitute a Prize of equal or greater value if the stated Prize becomes unavailable. Prizes are delivered within [N] days of confirmation. Any tax, duty or charge arising from receipt of the Prize is the Winner's responsibility unless stated otherwise. Winners' first names and [city or handle] may be published with their consent."

Sweepstakes and lottery law differs by jurisdiction. This is not legal advice. Have the terms checked where the giveaway runs.
