# Hooks and themes

## Hooks in campaign titles (extracted)

Regex matches on the titles of 37,180 ordinary campaigns with 1,000 or more contestants. One title can match several hooks. Peak month is the month where the hook's share of that month's starts is highest.

| Hook | Campaigns | Share of titles | Peak month | Share of that month's starts |
|---|---|---|---|---|
| Collaboration or partner ("X x Y", "with", "ft.") | 3,979 | 10.7% | September | 11.6% |
| Milestone or anniversary (birthday, 100k, celebration) | 2,089 | 5.6% | September | 6.8% |
| Holiday season (Christmas, advent, New Year) | 1,752 | 4.7% | December | 22.4% |
| Seasonal (summer, spring, back to school) | 1,730 | 4.7% | July | 9.1% |
| Daily or weekly series (day 3, week 2, advent calendar) | 1,510 | 4.1% | December | 13.1% |
| Launch or new product | 1,251 | 3.4% | January | 8.0% |
| Gaming release tie-in | 1,137 | 3.1% | March | 3.8% |
| Event or livestream tie-in | 953 | 2.6% | July | 4.5% |
| Black Friday or sales event | 465 | 1.3% | November | 8.6% |
| Valentine's, Mother's and Father's Day | 430 | 1.2% | February | 4.0% |
| Halloween | 201 | 0.5% | October | 4.8% |
| Charity or cause | 49 | 0.1% | February | 0.3% |

Most titles carry no hook at all, which is the plainest finding: "[Brand] giveaway" with a prize name is the default, and a hook is what separates a campaign from the default.

The timing skill's `holiday-benchmarks.md` holds contestants, conversion, duration and launch lead days for each holiday theme, with a dated calendar. Christmas and advent is the only theme above the all-campaign medians on both counts. Load it when the hook is a date.

## Campaign types (extracted)

A type is declared by words in the title, incentive name or the start of the description, so a campaign can carry several and the rows overlap. Value index is the campaign's contestants against the median of its stated-USD value band, 1.00 being typical for the money. Conversion is the clean subset. All ordinary campaigns: 2,203 contestants, 38% conversion, 4.3 entries per entrant, 0.13 referral entries per contestant, index 1.00. Reproduce with `analysis/campaign_types.py`.

| Type | n | Contestants | Conversion (clean n) | Entries per entrant | Referrals per contestant | Value index (n) | Duration | Actions |
|---|---|---|---|---|---|---|---|---|
| Advent or daily calendar | 1,061 | 3,277 | 50% (635) | 3.5 | 0.09 | 1.04 (294) | 5 | 5 |
| Free or no purchase | 1,755 | 3,097 | 38% (261) | 8.4 | 0.10 | 1.57 (1,152) | 31 | 13 |
| Charity or fundraiser | 242 | 2,976 | 34% (203) | 1.0 | 0.11 | 0.69 (23) | 0 | 1 |
| Sweepstakes wording (US) | 1,804 | 2,946 | 29% (379) | 4.5 | 0.10 | 1.22 (1,088) | 22 | 7 |
| Sorteo (Spanish) | 557 | 2,848 | 38% (220) | 4.8 | 0.11 | 1.01 (103) | 16 | 7 |
| Concours (French) | 360 | 2,672 | 36% (199) | 3.1 | 0.07 | 1.44 (79) | 11 | 5 |
| Milestone | 2,004 | 2,663 | 32% (539) | 4.8 | 0.17 | 0.94 (804) | 19 | 8 |
| Gewinnspiel (German) | 298 | 2,600 | 37% (194) | 4.3 | 0.05 | 0.63 (16) | 1 | 6 |
| Collaboration or partner | 6,449 | 2,380 | 32% (2,282) | 4.8 | 0.13 | 1.02 (2,427) | 15 | 8 |
| Bundle, mega or ultimate | 5,835 | 2,341 | 33% (1,403) | 4.6 | 0.12 | 0.96 (2,679) | 19 | 8 |
| Creator or streamer | 1,391 | 2,308 | 40% (440) | 5.4 | 0.16 | 0.98 (537) | 18 | 8 |
| Anniversary or birthday | 854 | 2,274 | 32% (276) | 4.2 | 0.13 | 0.97 (368) | 14 | 7 |
| Voting contest | 99 | 2,169 | 32% (47) | 2.9 | 0.15 | 0.73 (29) | 14 | 5 |
| Holiday themed | 3,771 | 2,133 | 35% (1,207) | 4.3 | 0.12 | 0.96 (1,802) | 15 | 7 |
| Scavenger hunt or secret code | 181 | 2,126 | 38% (69) | 4.6 | 0.14 | 0.91 (63) | 14 | 8 |
| Product launch | 1,271 | 2,020 | 29% (343) | 5.1 | 0.20 | 0.89 (558) | 16 | 8 |
| Cash prize | 1,442 | 1,976 | 42% (336) | 6.2 | 0.18 | 1.00 (718) | 21 | 10 |
| Community or Discord | 1,585 | 1,965 | 33% (623) | 4.8 | 0.33 | 0.92 (537) | 13 | 7 |
| Gift card or voucher | 2,811 | 1,953 | 35% (666) | 4.0 | 0.14 | 0.98 (1,559) | 21 | 7 |
| Cart, wishlist or spree | 382 | 1,920 | 27% (84) | 3.8 | 0.11 | 0.93 (213) | 28 | 7 |
| Competition wording (UK) | 1,733 | 1,788 | 46% (628) | 3.3 | 0.11 | 0.84 (584) | 15 | 6 |
| Weekly or monthly series | 1,022 | 1,697 | 36% (247) | 4.6 | 0.17 | 0.88 (487) | 17 | 8 |
| Flash (24 to 72 hours) | 104 | 1,693 | 40% (29) | 5.2 | 0.18 | 0.75 (51) | 12 | 8 |
| Quiz or trivia | 134 | 1,676 | 33% (82) | 4.2 | 0.42 | 0.72 (34) | 8 | 7 |

Reading it:

- **Advent or daily calendars** lead on contestants (3,277) and conversion (50%) on 1,061 campaigns: five days, five actions, and a reason to come back. The shape wins, and it is a December shape.
- **Campaigns that say free entry or no purchase** run long, with 13 actions and repeatable bonuses, and post the highest value index (1.57 on 1,152 valued campaigns). Those are the professional sweepstakes operators. Copy the discipline, not the action count.
- **Sweepstakes wording** carries the largest US campaigns (2,946 contestants, index 1.22) at the lowest conversion (29%), which is the long-run, daily-entry pattern.
- **Collaborations** are 17% of campaigns and sit a little above the median on contestants with a value index of 1.02. The title proxy for a partner does not by itself mark a strong campaign. The prize-picker reference shows the index rises to 1.13 when the collaboration is signalled in the title alone.
- **Creator and streamer** campaigns convert at 40% with the most actions per entrant (5.4). An existing audience does that.
- **Cash** converts well (42%) at a small size, with 10 actions and long runs. **Gift cards** sit below the median on everything except email uptake.
- **Community and Discord** campaigns record the most referral entries per contestant (0.33). **Quiz and trivia** campaigns record 0.42, on 134 campaigns.
- **Product launches** sit below the median (2,020 contestants, 29% conversion, index 0.89). A launch has no audience yet, which is the point of running one, so plan the promotion first.
- **Weekly or monthly series**, **flash** campaigns and **cart or wishlist** campaigns are the smallest. A series spreads one audience across many draws. A flash campaign has no time to be found.
- **UK competition wording** is small, short and converts at 46%, the UK pattern seen in the region table.

Nothing here says the type caused the number. Organizers who run advent calendars have December audiences, and organizers who write "no purchase necessary" have run many campaigns before.

## Theme starters by business (advice)

| Business | Moment-based | Manufactured |
|---|---|---|
| Food and drink | New menu, anniversary, local festival | "Tell us your order" question, a year-of-product series, staff-pick bundles |
| Fashion and beauty | Season drop, collaboration | Style-it UGC, advent or 12-days series, wardrobe or routine makeover with a partner |
| Home and garden | Spring, moving season, Black Friday | Before-and-after UGC, room makeover bundle with two partners |
| Fitness and outdoors | New year, event (a race, a season opener) | 30-day challenge with weekly draws, gear-up bundle with a coach session |
| Software and apps | Launch, milestone users, conference | Beta or early access, a year free plus a setup session, "show us your workspace" UGC |
| Creators and streamers | Subscriber milestone, subathon, a sponsor's launch | Daily draws during a stream series, signed items, a game with the creator |
| Local services | Opening, anniversary, local event | A year of the service, neighbourhood partner bundle, referral-weighted draw |
| B2B | Webinar, report launch, trade show | Consultation or audit as the prize, a peer-nomination mechanic |

### Two prize formulas that travel (advice, from Gleam's campaign team)

Own product plus the aspirational thing the customer wants next: coffee plus an espresso machine, snacks plus a stand mixer, supplements plus a sports watch, skincare plus a beauty device, camera accessory plus a camera. Ask what the customer's ideal day contains right before or after using the product. And the collaboration rule: same customer, different product. A partner should be non-competing, complementary, similar in positioning, and able to bring reach as well as a prize. Extracted: campaigns whose title signals a collaboration reached the top fifth 29% of the time against 19% for the rest (title proxy, n=1,195).

## Title wording (extracted, clean subset)

| Word in the title | n | Contestants | Contestants per impression | Entries per entrant | December starts |
|---|---|---|---|---|---|
| giveaway | 5,254 | 2,022 | 34% | 3.84 | 11% |
| none of the usual words | 4,965 | 2,143 | 44% | 3.51 | 25% |
| competition | 350 | 1,547 | 62% | 1.88 | 10% |
| sweepstakes | 312 | 2,633 | 29% | 4.06 | 11% |
| gewinnspiel | 179 | 2,193 | 38% | 4.30 | 48% |
| sorteo | 177 | 2,604 | 39% | 4.59 | 5% |
| raffle | 158 | 2,420 | 60% | 1.00 | 9% |
| concours | 148 | 2,042 | 36% | 1.00 | 16% |
| contest | 104 | 1,628 | 25% | 3.04 | 6% |

"Competition" and "raffle" are UK words and carry the UK pattern: small, one or two actions, high conversion. "Sweepstakes" is the US word and carries the largest campaigns. Titles with none of the usual words are a quarter December starts, which is the advent calendar pattern. Titles that start with "Win" drew 1,926 contestants against 2,077 (n=529), a value in the title 1,694 against 2,095 (n=630), and an emoji 1,656 against 2,092 (n=349). Titles over 60 characters converted best at 41% (n=922). The title reflects the organizer's market and habits more than it moves anyone.

## Mechanics (advice)

- Single draw: one prize, one push, the default for a small budget.
- Series: daily or weekly winners keep a long run alive and suit advent calendars and challenges. Needs a prize per draw and fresh content each week.
- Question or poll entry: cheap research and higher completion when it is one tap. Ask something that segments the list.
- UGC: photo or video entry with a review or a use of the product. Fewer entrants, better content, needs clear rights wording.
- Referral-weighted: extra entries per verified friend. The only mechanic that reaches new people. Say the reward in every post.
- Nomination: entrants nominate someone who deserves the prize. Suits services, B2B and cause-linked campaigns.
- Instant win or scratch: high-frequency small prizes for foot traffic or app installs. Regulated as a game of chance in some places.

## Formats to avoid, or to run with care

- Anything that requires a purchase to enter, including "buy to unlock entries" and discount codes as the prize. Lottery rules in many jurisdictions.
- Tag-a-friend and share-to-enter on platforms whose promotion rules forbid it. Check the current rules for each platform.
- Prizes unrelated to the business unless the objective is pure reach and there is a plan to qualify the list.
- Regulated goods as prizes (alcohol, firearms, tobacco, gambling credit) outside a tightly eligible audience with legal review.
- Manufactured scarcity or fake countdowns. Trust loss outlasts the campaign.
- "Guaranteed" anything. No prize guarantees entrants and the data cannot say otherwise.
