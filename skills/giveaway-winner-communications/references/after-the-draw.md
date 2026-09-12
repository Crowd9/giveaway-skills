# After the draw

Advice from practice, except the subscription-Action usage table below. The campaign emails that run while entries are open belong to giveaway-promotion-plan, and the opt-in wording on the entry form belongs to giveaway-entry-method-planner. This page picks up at the moment the Winner is announced and the rest of the list is still sitting there.

## Most campaigns ran no email Action (extracted)

Everything on this page runs on email, and the majority of campaigns never ran an email Action, so they collected no address through the campaign. Marketing permission is a separate switch, the subscriber checkbox the setup skill describes, and this cut does not measure it. The share of campaigns
offering an email or newsletter Action rises with size and stays a minority at every size:

<!-- generated:wc_email_band -->
| Campaign size | Offered an email Action | Campaigns | Businesses |
|---|---|---|---|
| 100 to 250 Entrants | 25% | 33,074 | 9,533 |
| 250 to 500 | 31% | 25,681 | 6,496 |
| 500 to 1,000 | 38% | 21,838 | 5,509 |
| 1,000 to 2,500 | 44% | 20,021 | 5,077 |
| 2,500 to 10,000 | 46% | 12,714 | 2,991 |
| 10,000 or more | 41% | 3,171 | 748 |
<!-- /generated -->

So in three campaigns out of four at the small end, and in more than half at every size, the campaign ran no
email Action, so it collected no address through one and has no list for the series on this page to go to.
The table measures which Actions campaigns offered, never how many addresses exist or who ticked a box.
Where there is no email Action there is no welcome series and no sunset rule to run, and the public announcement
is the only message that reaches the people who did not win. Check three things before choosing the message channel:

- **Address availability.** Inspect the campaign's contact records. An address can be collected through the User Details form even when no subscription Action is offered. If there is no usable email address, use the available contact channel for the Winner and the public announcement for the audience.
- **Marketing consent.** Check each person's recorded opt-in and its scope. An Email Subscription Action gets consent through a checkbox on the User Details form. Newsletter signup also collects explicit consent. Having an address alone grants no marketing permission. Keep Winner administration separate from promotional messages.
- **Subscription-Action usage.** The table describes which Actions campaigns offered. Offering an Action establishes neither a particular person's consent nor the absence of addresses in campaigns without that Action.

Plan the promotional welcome series only for people with recorded marketing consent. When addresses exist without that consent, keep them out of the promotional series and core marketing list. When no contact address exists, use another available channel for permitted campaign administration.

Source: `analysis/output/benchmarks.json` (`ordinary_benchmark.entry_methods.by_band.share_with_family`).

## The welcome series that starts with the non-Winner message

The series starts at entry. Message one is the welcome and referral email the promotion plan sends within a day of the sync landing, while the giveaway still runs. The three below follow the draw. Send them only to people whose recorded marketing consent covers the series, from the giveaway stream, on a fixed schedule, and stop.

| Message | When | What it does |
|---|---|---|
| 0. Welcome and referral | Within a day of entry, during the run | Confirms the entry, names the brand, carries the referral link. Written in giveaway-promotion-plan. |
| 1. Result and thank-you | With the public announcement, within a week of the draw | Names the Winner as the terms allow, thanks everyone, carries the one offer promised at entry. This is the non-Winner message in `references/message-templates.md`. |
| 2. What the brand is for | A few days after message one | One product or one story, chosen because the Prize pointed at it. A person who entered for a coffee machine came for coffee. |
| 3. One reason to come back | About a week after message two | A single next step: a code with an expiry, a guide, a restock alert, an invitation to the community. |

After message three the subscriber either joins the core list or drops out under the hygiene rule below. Three messages is the practice, chosen so the sequence finishes before entry interest fades. Adjust the count to what the business has to say.

## The code for everyone who did not win

Every Entrant browsed the store to enter, so the result email is the store's best-timed offer of the year. Mechanics, from practice:

- **One code per person.** Generate unique single-use codes in the store (Shopify Discounts supports single-use codes, and the email tool merges them per address, Klaviyo and Mailchimp both do this). A shared code lands on coupon sites within a day and the discount goes to people who never entered.
- **Expiry of 7 to 14 days.** Long enough to open the email, short enough to act on. Say the date in the subject.
- **Minimum spend or a collection limit** so the code does not turn the cheapest item free. Exclude sale items and gift cards.
- **A tier for referrers.** Entrants who referred a friend get a larger code. The referral entries are in the dataset, so the segment is a filter on the Entrant list.
- **Winners get no code.** They got the Prize. The welcome series still goes to them.
- **Track it.** The redemption count is the campaign's revenue line in giveaway-results-review, and the code name carries the campaign name so the store's reports show it. Without the code, revenue attribution is a join of Entrant email to orders.
- **Codes during a sale.** A 15% code sent the day the store goes 30% off is dead on arrival. Before Black Friday or a seasonal sale, make the non-Winner offer early access to the sale, or a code that stacks on one item, and say which it is in the email.
- **Wording that keeps the terms honest.** The code is a thank-you after the draw, never promised on the entry form as a reward for entering, which would make it a purchase condition under most sweepstakes readings.

## Keep the giveaway list on its own stream

Send the Winners email and the whole welcome series from a separate stream, segment or subaccount, kept apart from the list the business mails every week.

A giveaway list opens and clicks less than a list built from purchases. Mailbox providers read engagement per sending domain and stream, so a large low-engagement send lands the core list in the promotions tab or the spam folder alongside it. The separation costs one segment in the email tool and protects the asset the giveaway was meant to grow.

Keep the separation until the address has done something: opened, clicked, or bought. Then move it across.

## Watch the send

Read these in the email provider within a day or two of the Winners email, for the giveaway segment on its own.

- Unsubscribe rate on that send.
- Spam complaint rate on that send.
- Bounce rate, hard bounces especially, which say how many addresses were typed to win and never to be read.
- Open share in the first 48 hours.

A complaint rate that jumps on the Winners email usually means the entry form did not make the marketing opt-in obvious, so people who only wanted a Prize are receiving marketing. Fix the form before the next campaign. Set the numbers down beside the campaign report so the next giveaway has something to compare with.

## Hygiene before the core list

Addresses that never open in their first weeks are the ones that cost sender reputation later.

- Sunset rule (external practice, no dataset support here): an address that has opened nothing in its first 30 to 60 days gets suppressed. Suppress it outright, or send one plain re-permission email and suppress everyone who ignores that. It never joins the core list.
- Re-permission copy, plain text, one link: "You entered the [campaign name] giveaway and have not opened anything since. Tap here if you want to keep hearing from [Brand]. If not, this is the last one." Subject: "Should we stop emailing you?"
- Hard bounces come off immediately.
- Role addresses (info@, sales@, contact@) and obvious throwaway domains rarely become customers. The disposable-domain review lines from giveaway-random-draw flag the same addresses at draw time.
- Only what survives this joins the core list.

## Record entry consent and marketing consent separately

Entry consent and marketing consent are separate permissions. Record each separately, even when both appear on the same form.

| Consent | Where it is given | What it allows |
|---|---|---|
| Entry consent | The entry form, by entering | Running the promotion: contacting a Winner, verifying eligibility, delivering the Prize, publishing the result as the terms describe |
| Marketing consent | A ticked opt-in box on the entry form, or an opt-in on the thank-you page | Sending the promotional messages covered by the recorded opt-in |

Entering does not subscribe anyone. Anyone without recorded marketing consent stays out of promotional messages. Winner notification, verification and delivery messages follow the campaign terms and use the contact details available. The terms script in giveaway-winner-structure writes this as a marketing-consent clause under its --marketing-consent flag.

Where the region requires confirmed opt-in, send the confirmation email before message one, and hold the address out of the series until it is confirmed. Germany and Austria are the usual examples. Confirm the requirement for every country the Entrants live in before launch, since this is not legal advice.

## One question to Entrants

Ask one question with the result email or on the thank-you page. One question, one screen, no login.

Useful shapes:

- Which of these would you rather win next time? (three options taken from the Prize shortlist)
- Where did you hear about the giveaway? (fills the gap left by referrers that arrive as direct traffic)
- Had you bought from us before entering? (yes or no, and the answer sizes how much of the list is new)

Send the answers to whoever plans the next campaign. A Prize question answered by a few hundred Entrants is the cheapest Prize research available, and it feeds giveaway-prize-picker directly.
