# Reading results

Advice from practice plus the reporting definitions Gleam publishes. Other platforms define the same words differently, so confirm before comparing.

## Reading an export from another platform

Most contest platforms export one row per entry or per action with an email, an action name, a date and often a status and points. The report script matches those columns by name (Email Address, Entry Type, Points, Date, Verified and so on) and says on its first line which column it used for each role and which roles it could not find. When a role is wrong, pass `--map role=Column`. Exports with one row per person and one column per entry method are read as wide exports, with a non-empty cell counting as a completion. Sections whose columns are missing (referrers, cities, connected accounts) are omitted, never estimated. Benchmarks still apply: they describe campaigns of 100 or more Entrants whatever the platform, and the vertical rank is a name guess.

## Reading a Gleam Actions export

One row per completed action. The person is the Email column, Status is Valid, Invalid or Winner, Entries is the worth of that action, When carries the campaign's timezone offset, Country comes from the Entrant's IP, and Referring URL says where the visit came from. Entrants are unique valid emails. Actions completed are valid rows. Entries are the sum of the Entries column on valid rows. The dataset has no Impressions, so the Conversion Rate needs the Reporting tab. An auto-entry bonus (a row like "Entry Confirmed") counts as an action for nearly everyone and says nothing about engagement. Landing page URLs tell you where the widget was: gleam.io/KEY/slug is the hosted page, gleam.io/giveaways/KEY is the listing on the Gleam giveaways directory, and any other host is an embed on the organizer's site. A first touch that landed on the listing with gleam.io as the referrer means the campaign was found by browsing the directory (featured traffic). The listing link also gets shared by aggregators and in email, so the report shows both the browsing count and everyone who landed on the listing. Contest aggregators (contestgirl, loquax, giveawaybase, ozbargain and the like) are grouped as competition directories. Referrers show the promotion channels that worked and the giveaway-listing sites (contest aggregators) that found the campaign, which explain why few Entrants signed up for email as much as the form does. Where the landing URL carries an email UTM tag, the review can name the organizer's own mass mail as a source. A send with no tag on the link leaves no trace in the dataset, so a low referred share does not mean the list was not mailed.

A wider read comes from the referring host. A click out of a mail client or a webmail page is countable whether or not the link was tagged, and most campaigns show at least one [114,965 campaigns, 18,733 organizers]. Conversion Rate holds fairly steady regardless of how much of a campaign's Impressions came from mail clients (table below). Campaigns with no mail-client click at all read differently, but that's because they are the smallest campaigns in the data, not because of mailing.

| Mail-client share of Impressions | Campaigns | Conversion Rate | Entrants |
|---|---|---|---|
| None | — | 35% | 238 |
| Under 2% | 98,447 | 26% | 766 |
| 2 to 10% | 14,632 | 25% | — |
| 10 to 25% | 1,570 | 25% | — |
| 25% or more | 316 | 28% | — |

Source: `analysis/output/email_traffic.json` `outcomes_by_email_share`.

Source: analysis/output/field_cuts.json (email_traffic_by_provider, outcomes_when_email_over_10pct).

## The metrics

| Metric | Definition (Gleam) | What it tells you |
|---|---|---|
| Impressions (views of the campaign page) | One view per person per 24 hours | Reach of the entry page, inflated by return visits on long or daily campaigns |
| Users, Entrants | Unique people who entered | The real audience size |
| Actions | Entry methods completed | Engagement depth |
| Entries | Actions completed multiplied by entry worth | A weighting artefact. Never compare entries between campaigns with different worths |
| Conversion Rate | Users divided by Impressions | Landing page fit, with the Impressions caveat below. The platform quotes an average of about 34% |

## The Impressions caveat

A visitor who returns every day for a daily bonus counts as a new Impression each day and as one Entrant once. A 30-day campaign with a daily action can show a Conversion Rate half that of a 7-day campaign with the same audience. Conversion Rate falls as duration grows (table below). Before calling the Conversion Rate low, check run length and repeatable actions.

| Duration | Conversion Rate |
|---|---|
| The campaigns we can compare fairly (no repeatable action, 14 days or less) | 38% |
| 31 to 60 days | 24% |
| 61 days or more | 23% |

Those three rows are a summary of the shape. Quote the five-row table in `references/benchmarks.md` when you put
a duration figure in front of a reader, because it is cut differently, carries its campaign counts, and reads a
point lower at the long end. Two tables on the same subject disagree by a point here for that reason, so name the
one you used.

## What extra reach is worth (extracted)

Split the campaigns in one size band into five equal groups by Impressions and both the reach and the Conversion
Rate move a long way, while the Entrant count barely does. In the 1,000 to 2,500 band:

| Impressions group | Campaigns | Impressions | Entrants | Conversion Rate |
|---|---|---|---|---|
| lowest fifth | 3,988 | 2,504 | 1,232 | 54% |
| second | 3,988 | 3,875 | 1,376 | 36% |
| middle | 3,988 | 5,416 | 1,516 | 28% |
| fourth | 3,988 | 7,874 | 1,669 | 21% |
| highest fifth | 3,988 | 14,836 | 1,788 | 11% |

Nearly six times the Impressions goes with about 45% more Entrants. The same shape holds in every band, from 5.5
to 10.7 times the reach for 1.22 to 3.17 times the crowd, and the Conversion Rate falls from about 55% to about
11% in all six. The 10,000-plus band is the one with no ceiling on its Entrant counts, and there 10.7 times the
Impressions goes with 3.17 times the Entrants, which is close to the square root of the reach multiple.

The working rule that falls out: doubling the traffic you put in front of a page goes with roughly 40% more
Entrants, not twice as many. Read it as a description of campaigns at each reach level and never as what adding a
channel would do for this campaign, because nothing here holds the audience or the Prize constant.

A band bounds how far its Entrant counts can spread, so the middle bands understate the relationship. The
direction and the steepness of the Conversion Rate fall are what carry.

Source: `analysis/output/reach_returns.json`.

## Why this skill compares campaigns by size, not a size trend

Splitting the campaigns behind these numbers into ten equal-count tenths by Entrant count, from `thresholds.json`'s `size_deciles`, shows no tenth where action count, entries per Entrant or Conversion Rate meaningfully bends: all three stay in a narrow band across every tenth tested (table below) [11,734 to 11,735 campaigns per tenth, 2,539 to 5,022 organizers]. Campaign size on its own carries no independent trend. The size splits used throughout this skill's benchmarks exist because where a threshold sits moves by size, not because a bigger campaign performs better on its own. Read a size-specific benchmark as the figure for campaigns of that size, not as a rung on a ladder where bigger always wins.

| Metric | Range across the ten tenths |
|---|---|
| Action count | 6 to 7 |
| Entries per Entrant | 4.00 to 4.74 |
| Conversion Rate | 25.3% to 28.3% |
| Entrants (typical in the tenth) | 119 to 6,149 |

## Tone

The reader ran the campaign and is deciding whether to run another. Lead with what worked and its rank. Every gap becomes a target with a route: the benchmark it can reach, the previous campaign that reached it, and the single change that closes it. The percentile file holds the top quarter for every metric, so "the top quarter of campaigns this size reach X" is always available as the target. A campaign in the dataset already beat the 100-Entrant floor, which most giveaways never reach, and the review can say so.

## Judgement words

A rank says where a figure sits. It does not say the figure is bad. Most metrics here have a narrow spread, so a campaign can be "better than 15% of campaigns" on email signups while four in five of its Entrants still subscribed. Write the figure, the typical figure and the rank. Use weak or strong only for the bottom or top tenth, or a gap of a third or more from the typical figure, and say so in the same sentence. Absolute reads matter too: 68% of Entrants subscribing is most of them.

## Entries and completions

Entries and completions are the same count, worth only changes the credit.

## Common misreads

- **A low Conversion Rate with a long run or daily action.** Usually the caveat above. Compare against the duration row, not the overall typical figure.
- **A low Conversion Rate at a normal run length.** Usually reach. Campaigns in the top fifth of their size band by Impressions convert at about 11% where the bottom fifth convert at about 55%, and they drew more Entrants doing it. Check the Impression count before calling the page or the Prize weak.
- **High entries, ordinary Entrant count.** Entry worth on share or bonus actions. Look at Entrants and actions instead.
- **One action at 90%, the rest under 20%.** Normal: each action family completes at a different typical rate (table below), so a high top action and much lower others do not mean the others are broken. Rank against the typical figure for that family, not against the top action.
- **A fifth or more of entries invalid.** Check for a validated-answer question first (wrong answers count as invalid), then referral and Discord actions. Invalid entries are otherwise left out of the benchmarks.
- **Fewer Entrants than last time.** Check the gap since the previous campaign, the Prize category, the month, and the number of actions before blaming promotion.

| Family | Completions per 100 Entrants (typical) |
|---|---|
| Visits and email signups | 75 to 89 |
| Follows | 46 |
| Shares | 20 |
| Content | 23 |

## Organizer experience at a large campaign size

From `success_profiles.json`'s organizer-experience-by-size interaction, all campaigns, matched on Entrant size. Once we allow for Entrant size, a highly experienced organizer is not reliably more efficient than a first-timer: the ratio of actual to size-predicted Conversion Rate stays close to 1 across every cell tested (table below). No reliable overall experience effect once size is held fixed.

| Cells compared | Ratio, actual to size-predicted Conversion Rate |
|---|---|
| 1st campaign | 0.87 |
| 21st-or-later campaign | 1.04 |

Sample: 71 to 2,984 campaigns per cell, 53 to 860 organizers.

The one pattern that survives: first-time and early organizers running an unusually large campaign see a Conversion Rate below what size alone would predict, a real if modest inexperience penalty (table below). These two findings are not in conflict, they describe different sizes: no reliable effect at ordinary sizes, a real penalty only at the largest sizes for the newest organizers. Cite them together, useful when reviewing results for a large campaign run by a newer organizer.

| Organizer experience (at 10,000+ Entrants) | Ratio, actual to predicted Conversion Rate | Campaigns | Organizers |
|---|---|---|---|
| First-time | 0.867 | 71 | 71 |
| 2nd to 5th campaign | 0.864 | 133 | 99 |

The penalty runs about 13%.

Source: `analysis/output/success_profiles.json` (`interactions.organizer_experience_by_performance_and_band`).

## Why a peer campaign in the same vertical outperforms

From `vertical_profiles.json`'s best-quarter-versus-rest cut, by industry, on 13 tested industries. In 9 of the 13, the campaigns with the best quarter of Conversion Rate are run by organizers meaningfully deeper into their own platform history than the rest of that same industry (nth-campaign ratio, best quarter over rest, 1.15 or higher):

| Industry | Ratio (nth campaign, best quarter over rest) | Campaigns, best quarter / rest | Businesses, best quarter / rest |
|---|---|---|---|
| Software and SaaS | 9.8x | 31 / 93 | 13 / 44 |
| Travel and events | 6.6x | 57 / 171 | 14 / 52 |
| Apparel and fashion | 5.9x | 230 / 681 | 18 / 125 |
| Home and garden | 4.7x | 119 / 348 | 14 / 91 |
| Electronics and tech | 4.0x | 632 / 1,896 | 47 / 400 |
| Gaming and esports | 3.5x | 591 / 1,773 | 126 / 622 |
| Media and entertainment | 2.0x | 278 / 831 | 36 / 179 |
| Retail and marketplace | 1.5x | 105 / 315 | 10 / 46 |

Two industries reverse the pattern, both small cells, and two more are flat, following it neither way (table below). That is strong but not universal, one industry short of this skill's own 70% robustness bar, so read it as a pattern worth checking in a peer's own history, not a settled rule, and name the two reversals whenever it is cited.

| Industry | Ratio | Campaigns | Organizers |
|---|---|---|---|
| Toys, hobbies and collectibles (reverses) | 0.14x | 51 | 27 |
| Sports and outdoors (reverses) | 0.8x | 92 | 49 |
| Food and drink (flat) | ~1.1x | — | — |
| Marketing agency (flat) | ~1.1x | — | — |

Campaign size does not explain it. Only 6 of the same 13 industries show the best-quarter campaigns even modestly larger than the rest of their industry, typical ratio 1.10, essentially flat. A peer's bigger campaign is not why it sees a higher Conversion Rate, its organizer's own history is the more consistent lead.

Source: `analysis/output/vertical_profiles.json` (`top_quartile_vs_rest_by_industry`).

## Invalid share by industry and country

Invalid share is reported as a figure only, never scored. It varies sharply by industry, from crypto at the high end to media at the low end (table below). Read a campaign's invalid share against its own industry before anything else.

| Industry | Typical invalid share | Campaigns | Organizers |
|---|---|---|---|
| Crypto | 22.3% | 42,004 | 6,961 |
| Media | 2.9% | 19,991 | 1,955 |

Most of the country gap in invalid share is industry mix. The table reads each country's typical invalid share for all industries and again with crypto and SaaS organizers set aside.

| Country | All industries | Crypto and SaaS excluded |
|---|---|---|
| India | 30.5% (5,802 campaigns, 825 organizers) | 4.2% (1,476 campaigns, 420 organizers) |
| Japan | 22.6% (6,307 campaigns, 288 organizers) | 9.9% (1,027 campaigns, 137 organizers) |
| Singapore | 19.8% (4,622 campaigns, 332 organizers) | 7.4% (1,142 campaigns, 141 organizers) |
| Vietnam | 26.2% (3,578 campaigns, 746 organizers) | 19.1% (672 campaigns, 201 organizers) |
| Turkiye | 15.8% (2,009 campaigns, 489 organizers) | 10.9% (926 campaigns, 204 organizers) |

Vietnam and Turkiye keep most of their gap once crypto and SaaS are excluded. India, Japan and Singapore do not. Six percent of campaigns carry no invalid count and are left out of every figure on this page.

Source: `analysis/output/indicators.json` (`invalid_entry_share_by_industry`, `invalid_entry_share_by_country`, `invalid_entry_share_by_country_excluding_crypto`).

## Recommendation map

| Figure that is off | Likely change | Skill |
|---|---|---|
| Entrants low for campaigns your size, Conversion Rate fine | Reach. The top fifth of campaigns had 25 times the Impressions of the bottom fifth at the same Conversion Rate. Promotion channels, partners, timing | giveaway-promotion-plan, giveaway-timing-and-duration |
| Conversion Rate low on a campaign we can compare fairly | Landing fit: Prize appeal, too many actions, a mandatory action on the wrong network | giveaway-prize-picker, giveaway-entry-method-planner |
| Actions per Entrant low | Entry mix and ordering, entry worth | giveaway-entry-method-planner |
| The asset action (email, follow) underperformed | Make it the single mandatory action, cut the rest | giveaway-entry-method-planner |
| Share action near zero | Expected. Drop it or give it a reason to exist | giveaway-entry-method-planner |
| Winner drama | Structure, terms, communications | giveaway-winner-structure, giveaway-winner-communications |
| Unsubscribes or spam complaints on the Winners email above what the core list runs at | A visible marketing opt-in on the entry form and a separate sending stream for the giveaway segment. Target: the core list's own rate on the same send type | giveaway-winner-communications, giveaway-entry-method-planner |
| Open share of the new subscribers in their first 30 days under the core list's | The welcome series after the non-Winner message, then the sunset rule before these addresses join the core list. Target: the core list's 30-day open share | giveaway-winner-communications |
| Customers and revenue at 30, 60 and 90 days under what the core list produces over the same window | Prize relevance to what the business sells, and the offer carried in the result email. Target: the store's own 90-day rate for a new subscriber | giveaway-prize-picker, giveaway-winner-communications |

The last three come from the email provider and the store. Ask for them, or read them from the outcomes checklist the report prints.

## Using the Entrant list afterwards

Two things the list can do once the Winner is announced. Both are practice, with no dataset figure behind them.

**A retargeting or lookalike audience.** Ad platforms take a customer list as hashed email addresses and match it against their own users. Upload the Entrants who gave marketing consent, exclude anyone who is already a customer, and use the matched audience two ways: retarget the Entrants who never bought, and seed a lookalike audience for cold prospecting. Entrants self-selected on the Prize, so a lookalike built from them resembles people who want that Prize. Where the Prize was close to what the business sells, that is the audience worth copying. Where the Prize was a generic gift card, the lookalike will be people who like gift cards, and the campaign report's country and city split usually shows it first.

**Revenue attributed by joining email to orders.** Take the Entrant addresses, take the store's order export, and match on email over a fixed window from the close date. Thirty, sixty and ninety days gives a curve. Count the Entrants who ordered, sum the order value, and set it beside what the same window produces for a new subscriber from any other source. That comparison is the only honest revenue read available, since the campaign data carries no order data and the report says so where the ROI figures print.

Both joins run on the organizer's own machine, in a spreadsheet or the store's admin. The Entrant export never leaves it. Uploading a customer list to an ad platform is a separate decision with its own consent question, so check the marketing consent and the privacy policy cover it before the file goes anywhere.

For a store that sent a non-Winner code, the redemption count and revenue on that code in the store's discount report is the attribution figure, with no join needed. Read it at 14 days (the usual expiry) and again at 90.

A campaign that ran in November or December compares against its week as well as the year. The timing skill's every-week table gives Entrants and Conversion Rate for weeks 46 to 52, and Conversion Rate runs above the year typical in the December weeks and below it in week 47 (table below), so a December result that matches the typical figure across the year sits below its week, and a week 47 result that matches that typical figure sits above it.

| Week | Conversion Rate |
|---|---|
| 48 to 51 | 35% to 41% |
| 47 | 32% |
| Year typical | 35% |
