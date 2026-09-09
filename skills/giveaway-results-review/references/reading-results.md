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

A visitor who returns every day for a daily bonus counts as a new impression each day and as one contestant once. A 30-day campaign with a daily action can show a conversion rate half that of a 7-day campaign with the same audience. In the export, clean campaigns (no repeatable action, 14 days or less) converted at a median 42%. Campaigns of 31 to 60 days sat at 24% and 61 days or more at 23%. Before calling conversion low, check run length and repeatable actions.

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
