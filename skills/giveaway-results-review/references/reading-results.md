# Reading results

Advice from practice plus the reporting definitions Gleam publishes. Other platforms define the same words differently, so confirm before comparing.

## Reading an export from another platform

Most contest platforms export one row per entry or per action with an email, an action name, a date and often a status and points. The report script matches those columns by name (Email Address, Entry Type, Points, Date, Verified and so on) and says on its first line which column it used for each role and which roles it could not find. When a role is wrong, pass `--map role=Column`. Exports with one row per person and one column per entry method require `--wide-unit boolean`, `--wide-unit completions` or `--wide-unit entries`. Declare the configured Entries per completion for every populated method with `--wide-worth "Daily visit=1,Join newsletter=5"`. Boolean cells accept yes, true or 1. Completion counts retain repeated Actions. Earned Entries are divided by the declared worth and must resolve to whole completions. Blank, zero, no and false cells mean no completions. The script requires both units and configured worth before calculating Actions and Entries. Summary dates do not establish individual action timestamps, so wide reports leave speed, retention and action timing unavailable. Referral relationships also require individual action rows. Missing cities and connected accounts are omitted. Missing referrers appear as direct or unknown, so check the reported column mapping before interpreting that traffic. Benchmarks still apply: they describe campaigns of 100 or more Entrants whatever the platform, and the vertical rank is a name guess.

Complete-all participation requires the campaign configuration to identify an action that awards completion of all required actions. Pass its exact exported title as `--complete-all-action "Configured action title"` to the report and dashboard. Confirm that the title uniquely identifies that action, since exports can merge actions sharing a title. A custom daily bonus or survey title establishes only participation in that named action. Without a confirmed mapping, leave complete-all participation unavailable. The mapped count uses distinct valid Entrants, excludes invalid completions and counts repeated completions once. It does not require timestamps.

## Reading a Gleam Actions export

One row per completed action. The person is the Email column, Status is Valid, Invalid or Winner, Entries is the worth of that action, When carries the campaign's timezone offset, Country comes from the Entrant's IP, and Referring URL says where the visit came from. Entrants are unique valid emails. Actions completed are valid rows. Entries are the sum of the Entries column on valid rows. The dataset has no Impressions, so the Conversion Rate needs the Reporting tab. An auto-entry bonus (a row like "Entry Confirmed") counts as an action for nearly everyone and says nothing about engagement. Landing page URLs tell you where the widget was: gleam.io/KEY/slug is the hosted page, gleam.io/giveaways/KEY is the listing on the Gleam giveaways directory, and any other host is an embed on the organizer's site. A first touch that landed on the listing with gleam.io as the referrer means the campaign was found by browsing the directory (featured traffic). The listing link also gets shared by aggregators and in email, so the report shows both the browsing count and everyone who landed on the listing. Contest aggregators (contestgirl, loquax, giveawaybase, ozbargain and the like) are grouped as competition directories. Referrers show the promotion channels that worked and the giveaway-listing sites (contest aggregators) that found the campaign, which explain why few Entrants signed up for email as much as the form does. Where the landing URL carries an email UTM tag, the review can name the organizer's own mass mail as a source. A send with no tag on the link leaves no trace in the dataset, so a low referred share does not mean the list was not mailed.

A wider read comes from the referring host. A click out of a mail client or a webmail page is countable whether or not the link was tagged, and most campaigns show at least one [114,965 campaigns, 18,733 organizers]. Conversion Rate holds fairly steady regardless of how much of a campaign's Impressions came from mail clients (table below). Campaigns with no mail-client click at all read differently, but that's because they are the smallest campaigns in the data, not because of mailing.

<!-- generated:rr_mail_share -->
| Mail-client share of Impressions | Campaigns | Conversion Rate | Entrants |
|---|---|---|---|
| None | 31,679 | 35% | 240 |
| Under 2% | 98,367 | 26% | 765 |
| 2 to 10% | 14,594 | 25% | 744 |
| 10 to 25% | 1,565 | 25% | 516 |
| 25% or more | 313 | 27% | 438 |
<!-- /generated -->

Source: `analysis/output/email_traffic.json` `outcomes_by_email_share`.

Source: analysis/output/field_cuts.json (email_traffic_by_provider, outcomes_when_email_over_10pct).

## The metrics

| Metric | Definition (Gleam) | What it tells you |
|---|---|---|
| Impressions (views of the campaign page) | One view per person per 24 hours | Reach of the entry page, inflated by return visits on long or daily campaigns |
| Users, Entrants | Unique people who entered | The real audience size |
| Actions | Entry methods completed | Engagement depth |
| Entries | Actions completed multiplied by entry worth | A weighting artefact. Never compare entries between campaigns with different worths |
| Conversion Rate | Users divided by Impressions | Landing page fit, with the Impressions caveat below. The dataset median is 26.9% across 115,906 campaigns with Conversion Rate data in `percentiles.json` (`groups.all.conversion`), from the 116,285-campaign population that reached 100 Entrants, excluding crypto, ambiguous and purchase-only campaigns. Missing or unusable Conversion Rate fields are excluded |

## The Impressions caveat

A visitor who returns every day for a daily bonus counts as a new Impression each day and as one Entrant once. A 30-day campaign with a daily action can show a Conversion Rate half that of a 7-day campaign with the same audience. Conversion Rate falls as duration grows (table below). Before calling the Conversion Rate low, check run length and repeatable actions. A benchmark from campaigns without repeatable actions is context for a daily-entry campaign, never a forecast. The rate alone establishes neither a fault nor a healthy campaign, and aggregate thresholds cannot establish that the campaign worked. A passed check rules out only the fault tested. It cannot prove that return visits caused the rate or that the whole campaign is healthy. Next, check its daily Impressions, new Entrants and action completions for a specific drop to investigate.

| Duration | Conversion Rate |
|---|---|
| The campaigns we can compare fairly (no repeatable action, 14 days or less) | 35% |
| 31 to 60 days | 23% |
| 61 days or more | 21% |

Source: `analysis/output/calendar.json` (`all.conv_clean`, 39,462 campaigns) and `analysis/output/comparisons.json` (`duration_no_repeatable`, 11,419 and 2,929 campaigns for the longer runs). Only campaigns with the required duration, action and Impression fields enter these comparisons. The five-row duration table in `references/benchmarks.md` supplies the finer comparison.

## What extra reach is worth (extracted)

Split the campaigns in one size band into five equal groups by Impressions and both the reach and the Conversion
Rate move a long way, while the Entrant count barely does. In the 1,000 to 2,500 band:

| Impressions group | Campaigns | Impressions | Entrants | Conversion Rate |
|---|---|---|---|---|
| lowest fifth | 3,988 | 2,504 | 1,232 | 54% |
| second | 3,988 | 3,875 | 1,377 | 36% |
| middle | 3,988 | 5,416 | 1,516 | 28% |
| fourth | 3,988 | 7,874 | 1,669 | 21% |
| highest fifth | 3,988 | 14,836 | 1,788 | 11% |

Nearly six times the Impressions goes with about 45% more Entrants. The same shape holds in every band, from 5.5
to 10.7 times the reach for 1.22 to 3.17 times the crowd, and the Conversion Rate falls from 48% to 58% in the lowest fifth to
10% to 15% in the highest fifth across the six bands. The 10,000-plus band is the one with no ceiling on its Entrant counts, and there 10.7 times the
Impressions goes with 3.17 times the Entrants, which is close to the square root of the reach multiple.

Use the measured comparison within the reader's size band. These groups describe campaigns at each reach level,
with no universal traffic multiplier or forecast for adding a channel to this campaign. Nothing here holds the
audience or the Prize constant.

Every band, so a reader's own row is here:

<!-- generated:rr_reach_bands -->
| Size band | Impressions group | Campaigns | Impressions | Entrants | Conversion Rate |
|---|---|---|---|---|---|
| 100 to 250 Entrants | lowest fifth | 6,601 | 274 | 132 | 53% |
| 100 to 250 Entrants | second | 6,601 | 441 | 148 | 34% |
| 100 to 250 Entrants | middle | 6,601 | 632 | 164 | 26% |
| 100 to 250 Entrants | fourth | 6,601 | 928 | 176 | 19% |
| 100 to 250 Entrants | highest fifth | 6,601 | 1,764 | 187 | 10% |
| 250 to 500 | lowest fifth | 5,122 | 593 | 315 | 58% |
| 250 to 500 | second | 5,122 | 949 | 340 | 36% |
| 250 to 500 | middle | 5,122 | 1,341 | 354 | 26% |
| 250 to 500 | fourth | 5,122 | 1,922 | 370 | 19% |
| 250 to 500 | highest fifth | 5,121 | 3,322 | 385 | 11% |
| 500 to 1,000 | lowest fifth | 4,358 | 1,153 | 611 | 57% |
| 500 to 1,000 | second | 4,358 | 1,820 | 662 | 37% |
| 500 to 1,000 | middle | 4,358 | 2,509 | 698 | 28% |
| 500 to 1,000 | fourth | 4,358 | 3,529 | 738 | 21% |
| 500 to 1,000 | highest fifth | 4,357 | 6,292 | 765 | 12% |
| 1,000 to 2,500 | lowest fifth | 3,988 | 2,504 | 1,232 | 54% |
| 1,000 to 2,500 | second | 3,988 | 3,875 | 1,377 | 36% |
| 1,000 to 2,500 | middle | 3,988 | 5,416 | 1,516 | 28% |
| 1,000 to 2,500 | fourth | 3,988 | 7,874 | 1,669 | 21% |
| 1,000 to 2,500 | highest fifth | 3,988 | 14,836 | 1,788 | 11% |
| 2,500 to 10,000 | lowest fifth | 2,533 | 6,905 | 3,030 | 48% |
| 2,500 to 10,000 | second | 2,533 | 11,147 | 3,611 | 33% |
| 2,500 to 10,000 | middle | 2,533 | 15,922 | 4,201 | 27% |
| 2,500 to 10,000 | fourth | 2,532 | 24,126 | 4,931 | 20% |
| 2,500 to 10,000 | highest fifth | 2,532 | 46,236 | 5,560 | 11% |
| 10,000 or more | lowest fifth | 623 | 23,160 | 12,158 | 58% |
| 10,000 or more | second | 623 | 41,399 | 13,834 | 34% |
| 10,000 or more | middle | 623 | 62,315 | 15,778 | 25% |
| 10,000 or more | fourth | 622 | 109,844 | 21,530 | 20% |
| 10,000 or more | highest fifth | 622 | 246,976 | 38,600 | 15% |
<!-- /generated -->

A band bounds how far its Entrant counts can spread, so the middle bands understate the relationship. The
direction and the steepness of the Conversion Rate fall are what carry.

Source: `analysis/output/reach_returns.json`.

## Why this skill compares campaigns by size, not a size trend

Splitting the campaigns behind these numbers into ten equal-count tenths by Entrant count, from `thresholds.json`'s `size_deciles`, shows no tenth where action count, entries per Entrant or Conversion Rate meaningfully bends: all three stay in a narrow band across every tenth tested (table below) [11,649 to 11,650 campaigns per tenth, 2,504 to 4,977 organizers]. Campaign size on its own carries no independent trend. The size splits used throughout this skill's benchmarks exist because where a threshold sits moves by size, not because a bigger campaign performs better on its own. Read a size-specific benchmark as the figure for campaigns of that size, not as a rung on a ladder where bigger always wins.

| Metric | Range across the ten tenths |
|---|---|
| Action count | 6 to 7 |
| Entries per Entrant | 3.99 to 4.74 |
| Conversion Rate | 25.3% to 28.3% |
| Entrants (typical in the tenth) | 119 to 6,101 |

## Tone

The reader ran the campaign and is deciding whether to run another. Lead with what worked and its rank. Every gap becomes a target with a route: the benchmark it can reach, the previous campaign that reached it, and the single change that closes it. The percentile file holds the top quarter for every metric, so "the top quarter of campaigns this size reach X" is always available as the target. The comparison includes campaigns with at least 100 Entrants. It cannot establish how many giveaways fall below that floor or whether clearing it beats most giveaways.

## Judgement words

A rank says where a figure sits. It does not say the figure is bad. Most metrics here have a narrow spread, so a campaign can be "better than 15% of campaigns" on email signups while four in five of its Entrants still subscribed. Choose the typical figure or rank that answers the question. This grading rule is for you: use weak or strong only for the bottom or top tenth, or a gap of a third or more from the typical figure in a relevant group. Tell the reader the actual comparison, without explaining which words a threshold allows. A group with different repeatable actions or run length cannot decide whether their result is low, so say that once and omit relative-gap arithmetic against it. Absolute reads matter too: 68% of Entrants subscribing is most of them.

## Entries and completions

Entrants count people. Completed Actions count valid action completions. Entries add up the worth credited for those completions, so weighted Entries can exceed the completion count. For example, ten valid completed Actions worth five Entries each produce ten completions and fifty Entries, regardless of how many people completed them.

## Common misreads

- **A low Conversion Rate with a long run or daily action.** Return visits are a possible explanation. Check for entry faults and changes in daily Impressions, new Entrants and action completions before drawing a conclusion. Use the duration row as context with its repeatable-action caveat.
- **A low Conversion Rate at a normal run length.** Usually reach. Campaigns in the top fifth of their size band by Impressions convert at about 11% where the bottom fifth convert at about 55%, and they drew more Entrants doing it. Check the Impression count before calling the page or the Prize weak.
- **High entries, ordinary Entrant count.** Entry worth on share or bonus actions. Look at Entrants and actions.
- **One action at 90%, the rest under 20%.** Normal: each action family completes at a different typical rate (table below), so a high top action and much lower others do not mean the others are broken. Rank against the typical figure for that family, not against the top action.
- **A fifth or more of entries invalid** is a suggested point to start checking, with no measured boundary between healthy and broken campaigns. Check for a question that only accepts the correct answer first (wrong answers count as invalid), then referral and Discord actions. Investigate reported entry problems at any share. Invalid entries are otherwise left out of the benchmarks.
- **Fewer Entrants than last time.** Check the gap since the previous campaign, the Prize category, the month, and the number of actions before blaming promotion.

| Family | Completions per 100 Entrants (typical) |
|---|---|
| Visits and email signups | 78 to 85 |
| Follows | 53 |
| Shares | 11 |
| Content | 12 |

Source: `analysis/output/percentiles.json` (`bench.family_uptake`).

## Organizer experience at a large campaign size

From `success_profiles.json`'s organizer-experience-by-size interaction, the campaigns we can compare fairly, matched on Entrant size. The ratios compare each cell's Conversion Rate with the value expected from both its size and organizer-experience group. Across all cells they range from 0.832 to 1.076. These are descriptive differences, with no uncertainty interval in the output.

| Cells compared (at 10,000+ Entrants) | Ratio, actual to expected Conversion Rate |
|---|---|
| 1st campaign | 0.83 |
| 21st-or-later campaign | 1.08 |

Sample across all cells: 81 to 4,472 campaigns per cell, 56 to 2,042 organizers. Only campaigns with the fields needed for the clean Conversion Rate and experience comparison are included.

First-time and early organizers running an unusually large campaign show the largest downward departures from the expected rate:

| Organizer experience (at 10,000+ Entrants) | Ratio, actual to expected Conversion Rate | Campaigns | Organizers |
|---|---|---|---|
| First-time | 0.832 | 81 | 81 |
| 2nd to 5th campaign | 0.838 | 142 | 107 |

The gaps are about 17% and 16%. Check a large campaign from a newer organizer against its own comparison group. These ratios do not establish that experience caused the difference.

Source: `analysis/output/success_profiles.json` (`interactions.organizer_experience_by_performance_and_band`).

## Why a peer campaign in the same vertical outperforms

From `vertical_profiles.json`'s best-quarter-versus-rest cut, by industry, on 21 tested industries. In 17 of the 21, the campaigns with the best quarter of Conversion Rate are run by organizers deeper into their own platform history than the rest of that industry (nth-campaign ratio of at least 1.15). Four industries reverse the pattern. Only industries with enough businesses for publication appear, and the source carries no uncertainty intervals.

| Industry | Ratio (nth campaign, best quarter over rest) | Campaigns, best quarter / rest | Businesses, best quarter / rest |
|---|---|---|---|
| Software and SaaS | 3.5x | 135 / 396 | 46 / 175 |
| Travel and events | 6.4x | 194 / 576 | 57 / 200 |
| Apparel and fashion | 8.9x | 499 / 1,494 | 48 / 333 |
| Home and garden | 5.0x | 271 / 804 | 49 / 192 |
| Electronics and tech | 3.9x | 1,428 / 4,281 | 115 / 851 |
| Gaming and esports | 3.0x | 2,487 / 7,461 | 490 / 2,022 |
| Media and entertainment | 1.9x | 1,342 / 4,026 | 223 / 752 |
| Retail and marketplace | 5.1x | 360 / 1,074 | 16 / 139 |

The reversals are toys, health and fitness, education and marketing agencies. Name those exceptions when citing the experience pattern.

| Industry | Ratio | Campaigns, best quarter / rest | Businesses, best quarter / rest |
|---|---|---|---|
| Toys, hobbies and collectibles | 0.46x | 332 / 993 | 104 / 195 |
| Health, wellness and fitness | 0.64x | 201 / 597 | 61 / 139 |
| Education | 0.06x | 247 / 738 | 58 / 87 |
| Marketing agency | 0.55x | 101 / 294 | 29 / 50 |

Campaign size also differs. In 13 of the 21 industries the best-quarter campaigns are at least 15% larger, and the median size ratio across all industries is 1.27. Read size and organizer history together. This comparison does not isolate either as the cause of a higher Conversion Rate.

Source: `analysis/output/vertical_profiles.json` (`top_quartile_vs_rest_by_industry`).

## Invalid share by industry and country

Invalid share is reported as a figure only, never scored. It varies sharply by industry, from crypto at the high end to media at the low end (table below). Read a campaign's invalid share against its own industry before anything else.

| Industry | Typical invalid share | Campaigns | Organizers |
|---|---|---|---|
| Crypto | 21.7% | 23,974 | 4,195 |
| Media | 2.8% | 19,800 | 1,927 |

Most of the country gap in invalid share is industry mix. The table reads each country's typical invalid share for all industries and again with crypto and SaaS organizers set aside.

| Country | All industries | Crypto and SaaS excluded |
|---|---|---|
| India | 26.0% (3,867 campaigns, 646 organizers) | 3.6% (1,386 campaigns, 401 organizers) |
| Singapore | 18.5% (3,401 campaigns, 256 organizers) | 7.1% (1,088 campaigns, 127 organizers) |
| Vietnam | 24.1% (2,337 campaigns, 525 organizers) | 18.4% (541 campaigns, 178 organizers) |
| Turkiye | 13.4% (1,313 campaigns, 352 organizers) | 10.3% (881 campaigns, 194 organizers) |

Vietnam and Turkiye keep most of their gap once crypto and SaaS are excluded. India, Japan and Singapore do not. Six percent of campaigns carry no invalid count and are left out of every figure on this page.

Source: `analysis/output/indicators.json` (`invalid_entry_share_by_industry`, `invalid_entry_share_by_country`, `invalid_entry_share_by_country_excluding_crypto`).

## Recommendation map

| Figure that is off | Likely change | Skill |
|---|---|---|
| Entrants low for campaigns your size, Conversion Rate fine | Reach. The top fifth of campaigns had 25 times the Impressions of the bottom fifth, with Conversion Rates of 28% and 25% (`analysis/output/context_checks.json`, `top_vs_bottom_quintile`). Promotion channels, partners, timing | giveaway-promotion-plan, giveaway-timing-and-duration |
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
| 47 | 33% |
| Year typical | 35% |

Source for the week table: `analysis/output/calendar.json` (`by_start_week.47` to `by_start_week.51`, `all.conv_clean`). Clean Conversion Rate samples are 845 to 1,562 campaigns per week and 39,462 for the year. Campaigns without the required timing and Impression fields are excluded.
