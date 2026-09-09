# Reading results

Advice from practice plus the reporting definitions Gleam publishes. Other platforms define the same words differently, so confirm before comparing.

## Reading an export from another platform

Most contest platforms export one row per entry or per action with an email, an action name, a date and often a status and points. The report script matches those columns by name (Email Address, Entry Type, Points, Date, Verified and so on) and says on its first line which column it used for each role and which roles it could not find. When a role is wrong, pass `--map role=Column`. Exports with one row per person and one column per entry method are read as wide exports, with a non-empty cell counting as a completion. Sections whose columns are missing (referrers, cities, connected accounts) are omitted, never estimated. Benchmarks still apply: they describe campaigns of 1,000 or more entrants whatever the platform, and the vertical rank is a name guess.

## Reading a Gleam Actions export

One row per completed action. The person is the Email column, Status is Valid, Invalid or Winner, Entries is the worth of that action, When carries the campaign's timezone offset, Country comes from the entrant's IP, and Referring URL says where the visit came from. Contestants are unique valid emails. Actions completed are valid rows. Entries are the sum of the Entries column on valid rows. The export has no impressions, so conversion needs the Reporting tab. An auto-entry bonus (a row like "Entry Confirmed") counts as an action for nearly everyone and says nothing about engagement. Landing page URLs tell you where the widget was: gleam.io/KEY/slug is the hosted page, gleam.io/giveaways/KEY is the listing on the Gleam giveaways directory, and any other host is an embed on the organizer's site. A first touch that landed on the listing with gleam.io as the referrer means the campaign was found by browsing the directory (featured traffic). The listing link also gets shared by aggregators and in email, so the report shows both the browsing count and everyone who landed on the listing. Contest aggregators (contestgirl, loquax, giveawaybase, ozbargain and the like) are grouped as competition directories. Referrers show the promotion channels that worked and the giveaway-listing sites (contest aggregators) that found the campaign, which explain a low email uptake as much as the form does.

## The metrics

| Metric | Definition (Gleam) | What it tells you |
|---|---|---|
| Impressions | One view per user per 24 hours | Reach of the entry page, inflated by return visits on long or daily campaigns |
| Users, contestants | Unique people who entered | The real audience size |
| Actions | Entry methods completed | Engagement depth |
| Entries | Actions completed multiplied by entry worth | A weighting artefact. Never compare entries between campaigns with different worths |
| Conversion rate | Users divided by impressions | Landing page fit, with the impressions caveat below. Platform average about 34% |

## The impressions caveat

A visitor who returns every day for a daily bonus counts as a new impression each day and as one contestant once. A 30-day campaign with a daily action can show a conversion rate half that of a 7-day campaign with the same audience. In the export, the clean subset (the campaigns with no repeatable action and a run of 14 days or less, which is the group the script names clean campaigns) converted at a median 42%. Campaigns of 31 to 60 days sat at 24% and 61 days or more at 23%. Before calling conversion low, check run length and repeatable actions.

## Tone

The reader ran the campaign and is deciding whether to run another. Lead with what worked and its rank. Every gap becomes a target with a route: the benchmark it can reach, the previous campaign that reached it, and the single change that closes it. The percentile file holds the top quarter for every metric, so "the top quarter of campaigns this size reach X" is always available as the target. A campaign in the export already beat the 1,000-entrant floor, which most giveaways never reach, and the review can say so.

## Judgement words

A rank says where a figure sits. It does not say the figure is bad. Most metrics here have a narrow spread, so a campaign can be "better than 15% of campaigns" on email uptake while four in five of its entrants still subscribed. Write the figure, the median and the rank. Use weak or strong only for the bottom or top tenth, or a gap of a third or more from the median, and say so in the same sentence. Absolute reads matter too: 68% of entrants subscribing is most of them.

## Common misreads

- **Low conversion with a long run or daily action.** Usually the caveat above. Compare against the duration row, not the overall median.
- **High entries, ordinary contestants.** Entry worth on share or bonus actions. Look at contestants and actions instead.
- **One action at 90%, the rest under 20%.** Normal. Visits and email signups sit near 0.75 to 0.89 completions per contestant, follows near 0.47, shares near 0.22, content near 0.24. Rank against the family median, not against the top action.
- **A fifth or more of entries invalid.** Check for a validated-answer question first (wrong answers count as invalid), then referral and Discord actions. Invalid entries are otherwise left out of the benchmarks.
- **Fewer contestants than last time.** Check the gap since the previous campaign, the prize category, the month, and the number of actions before blaming promotion.

## Recommendation map

| Figure that is off | Likely change | Skill |
|---|---|---|
| Contestants low for the band, conversion fine | Reach. The top fifth of campaigns had nine times the impressions of the bottom fifth at the same conversion. Promotion channels, partners, timing | giveaway-promotion-plan, giveaway-timing-and-duration |
| Conversion low on a clean campaign | Landing fit: prize appeal, too many actions, a mandatory action on the wrong network | giveaway-prize-picker, giveaway-entry-method-planner |
| Actions per entrant low | Entry mix and ordering, entry worth | giveaway-entry-method-planner |
| The asset action (email, follow) underperformed | Make it the single mandatory action, cut the rest | giveaway-entry-method-planner |
| Share action near zero | Expected. Drop it or give it a reason to exist | giveaway-entry-method-planner |
| Winner drama | Structure, terms, communications | giveaway-winner-structure, giveaway-winner-communications |
| Unsubscribes or spam complaints on the winners email above what the core list runs at | A visible marketing opt-in on the entry form and a separate sending stream for the giveaway segment. Target: the core list's own rate on the same send type | giveaway-winner-communications, giveaway-entry-method-planner |
| Open share of the new subscribers in their first 30 days under the core list's | The welcome series after the non-winner message, then the sunset rule before these addresses join the core list. Target: the core list's 30-day open share | giveaway-winner-communications |
| Customers and revenue at 30, 60 and 90 days under what the core list produces over the same window | Prize relevance to what the business sells, and the offer carried in the result email. Target: the store's own 90-day rate for a new subscriber | giveaway-prize-picker, giveaway-winner-communications |

The last three come from the email provider and the store. Ask for them, or read them from the outcomes checklist the report prints.

## Using the entrant list afterwards

Two things the list can do once the winner is announced. Both are practice, with no dataset figure behind them.

**A retargeting or lookalike audience.** Ad platforms take a customer list as hashed email addresses and match it against their own users. Upload the entrants who gave marketing consent, exclude anyone who is already a customer, and use the matched audience two ways: retarget the entrants who never bought, and seed a lookalike audience for cold prospecting. Entrants self-selected on the prize, so a lookalike built from them resembles people who want that prize. Where the prize was close to what the business sells, that is the audience worth copying. Where the prize was a generic gift card, the lookalike will be people who like gift cards, and the campaign report's country and city split usually shows it first.

**Revenue attributed by joining email to orders.** Take the entrant addresses, take the store's order export, and match on email over a fixed window from the close date. Thirty, sixty and ninety days gives a curve. Count the entrants who ordered, sum the order value, and set it beside what the same window produces for a new subscriber from any other source. That comparison is the only honest revenue read available, since the campaign export carries no order data and the report says so where the ROI figures print.

Both joins run on the organizer's own machine, in a spreadsheet or the store's admin. The entrant export never leaves it. Uploading a customer list to an ad platform is a separate decision with its own consent question, so check the marketing consent and the privacy policy cover it before the file goes anywhere.

For a store that sent a non-winner code, the redemption count and revenue on that code in the store's discount report is the attribution figure, with no join needed. Read it at 14 days (the usual expiry) and again at 90.

A campaign that ran in November or December compares against its week as well as the year. The timing skill's every-week table gives contestants and conversion for weeks 46 to 52 (weeks 48 to 51 convert at 40% to 53% against 38% for the year, week 47 at 33%), so a December result that matches the all-year median sits below its week, and a week 47 result that matches the median sits above it.
