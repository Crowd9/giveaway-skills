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

A hook and a campaign type are two different things. The hook is the occasion the title claims (Black Friday, a 10k milestone, a collaboration). The campaign type is the shape the campaign declares and runs (an advent calendar, a bundle, a cash draw, a voting contest). One campaign carries both, and the tables below are separate for that reason.

The timing skill's `holiday-benchmarks.md` holds contestants, conversion, duration and launch lead days for each holiday theme, with a dated calendar. Christmas and advent is the only theme above the all-campaign medians on both counts, and the smaller dates section lists the national and world days organizers used (National Coffee Day, World Photography Day, National Sticker Day) and the holidays nobody in the data has taken. Load it when the hook is a date.

## Campaign types (extracted)

A type is declared by words in the title, incentive name or the start of the description, so a campaign can carry several and the rows overlap. Value index is the campaign's contestants against the median of its stated-USD value band, 1.00 being typical for the money. Uptake, where it appears below, is entries recorded on an action divided by the campaign's contestants. Conversion is the clean subset, the campaigns with no repeatable action and a run of 14 days or less, which is what makes impressions comparable between them. All ordinary campaigns: 2,203 contestants, 38% conversion, 4.3 entries per entrant, 0.13 referral entries per contestant, index 1.00. Reproduce with `analysis/campaign_types.py`.

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

### Launches, pre-orders and drops (extracted)

| Subtype | n | Contestants | Conversion (clean n) | Email uptake | Referrals per contestant | Value index (n) | Own product prize | Repeat organizer |
|---|---|---|---|---|---|---|---|---|
| Pre-order or crowdfunding | 178 | 1,504 | 35% (32) | 0.88 | 0.19 | 0.86 (105) | 22% | 51% |
| Limited edition or drop | 654 | 2,076 | 32% (204) | 0.98 | 0.16 | 0.91 (260) | 26% | 77% |
| Early access, beta or waitlist | 211 | 2,260 | 31% (84) | 1.01 | 0.21 | 1.09 (80) | 21% | 59% |
| Launch or new release | 1,194 | 2,029 | 29% (349) | 0.90 | 0.20 | 0.89 (511) | 32% | 64% |

Launch campaigns run below the all-campaign medians on contestants and conversion, and above them on referrals per contestant (0.16 to 0.21 against 0.13). A launch has no audience yet, and its entrants share more. Early access, beta and waitlist campaigns are the exception, at a value index of 1.09 with the highest referral rate: a promise of first access is a reason to bring a friend. Pre-order and crowdfunding campaigns are the smallest (1,504 contestants) and half come from first-time or occasional organizers. For a launch, plan the promotion and the referral action first, keep the prize the product itself (a third do), and treat the campaign as the start of the list.

### Campaigns that beat their prize money (extracted)

1,615 valued campaigns (11%) drew at least three times the median contestants for their stated prize band. Median 13,397 contestants on a 1,658 USD pool, 0.11 USD per contestant. What they had more often than the rest:

| Feature | Standouts | The rest |
|---|---|---|
| twitch follow | 34% | 14% |
| repeat organizer | 88% | 72% |
| 11 or more actions | 48% | 34% |
| secret code action | 26% | 12% |
| repeatable action | 55% | 46% |
| single prize unit | 67% | 60% |
| discord join | 23% | 16% |
| collaboration in title | 20% | 15% |
| youtube visit | 47% | 42% |
| 14 days or less | 40% | 37% |
| email action | 59% | 56% |
| december start | 9% | 9% |
| own product prize | 19% | 22% |
| question action | 10% | 14% |
| stated pool under 250 USD | 9% | 19% |
| viral share action | 49% | 59% |

Prize categories over-represented among them:

| Category | Standouts | The rest | Ratio |
|---|---|---|---|
| Tech hardware | 38% | 30% | 1.26 |
| Regulated goods (firearms) | 16% | 5% | 3.30 |
| Gift card or cash | 13% | 18% | 0.72 |
| Bundle or box | 8% | 13% | 0.61 |
| Placeholder prize name | 8% | 5% | 1.62 |
| Game items or skins | 7% | 6% | 1.11 |
| Merch, apparel, collectibles | 4% | 4% | 1.02 |
| Home, garden, appliance | 3% | 6% | 0.59 |
| Experience, travel, tickets | 3% | 5% | 0.61 |
| Unclassified | 2% | 7% | 0.30 |
| Tools, craft, DIY | 1% | 2% | 0.90 |
| Music gear | 1% | 3% | 0.50 |

The pattern is an organizer who has run many campaigns (88%), a secret code from a stream or video (26% against 12%), Twitch and Discord actions, a single hero prize, and a long list of actions with a daily bonus. Gaming is 29% of standouts against 21% of the rest. Firearms retailers with specialist audiences are the extreme case at three times their share. Cash, gift cards and bundles are under-represented. Standouts converted at 32%, under the median, because their reach came from audiences, streams and directories, and the landing page had less to do with it.

## Store campaigns

For a store, the giveaway is a shopping session with a prize at the end. The data has one line on the shape: cart, wishlist and spree campaigns (382, matched on words like "win your cart" and "wishlist") drew a median 1,920 contestants at 27% clean conversion, ran 28 days at the median, and posted a value index of 0.93. Below the all-campaign medians on size, long by design, and the export cannot see what they were for: every entrant browsed the catalogue and told the store what they wanted. Gift card and voucher campaigns (2,811) sit at 1,953 contestants, 35% conversion and an index of 0.98.

Formats to pick from, each with the store job it does:

- **Win your cart.** Entrants build a cart, submit the cart link or a screenshot, and one cart is paid for up to a cap. Job: browsing depth and a wishlist per entrant. Cap the prize at a number in the title ("up to 500 USD") so the cost is fixed.
- **Win your wishlist.** Same shape on the wishlist app, lighter on the entrant. Job: a wishlist per entrant the store can email against when items restock or drop in price.
- **Pick your prize.** Three products from the range as the prize options, entrant chooses one on the form. Job: a preference vote across the range, and the entrant reads three product pages to choose.
- **Bundle builder.** The prize is the bundle the entrant designs from a set of options. Job: tells the store which combinations sell, and the bundle becomes the post-campaign offer.
- **Restock or drop.** A giveaway of the item that sells out, drawn on restock day. Job: the waitlist. Launch and early-access campaigns sit at a value index of 1.09 in the launch table above.
- **Own product plus the next thing.** The prize hierarchy in giveaway-prize-picker: the store's product with the aspirational adjacent item.
- **Shopping spree with a partner.** Two stores, one cart across both, one entry page. Job: audience swap with a product that fits.
- **Gift card tiers.** One large gift card and several small ones, so the store has many winners who all come back to spend. Job: winners who become customers, and codes with expiry dates that pull a visit.
- **Mystery box.** A box from the range at a stated value. Job: reach at fixed cost and content for the reveal.

Season formats for a store, with the timing skill's holiday table behind them:

- **Pre-sale early access.** A giveaway in the two weeks before Black Friday, closing the day before the sale, with early access to the sale as the offer to everyone who did not win. Black Friday campaigns in the data run 8 days.
- **Gift guide giveaway.** The hero item from the gift guide as the prize, entry by picking the gift for someone on the entrant's list. The December shape, launched around 6 December.
- **Advent or 12 days.** A product a day, one draw a day, a reason to return. Advent calendars lead every type on contestants and conversion.
- **Win your order back.** Everyone who buys in the sale window can also enter free, and one order is refunded. Keep the free entry route equal, and have the terms read by a lawyer, since it sits close to a purchase condition.
- **January restart.** The product that pairs with December's purchases, launched in the last ten days of December. Campaigns live over New Year converted 7% to 8% above matched campaigns.

Every entrant who did not win is a shopper who just browsed the store, so the non-winner code in giveaway-winner-communications is the second half of a store campaign. Keep purchase out of the entry conditions: a purchase-to-enter reads as a lottery in most places, and the free entry route has to stay open.

Cheap prizes that drew crowds: 129 campaigns with a stated pool under 250 USD reached 5,000 contestants or more. 79% came from repeat organizers, only 10% gave away their own product, 7 actions and 22 days at the median, and the prizes were tech hardware, game items and small gift cards in gaming and unclassified verticals. A small prize in front of an audience that already exists beats a large prize in front of nobody. Both cuts on this page describe campaigns that outran their budget, so read them against the spending benchmarks in giveaway-prize-picker before setting a prize budget from them.

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

### Prize direction for a concept (advice, from Gleam's campaign team)

The own-product-plus-adjacent-item formula and its worked pairs live in one place: the prize hierarchy in giveaway-prize-picker. Point there once the concept is chosen.

What belongs to the concept is the collaboration test: same customer, different product. A partner should be non-competing, complementary, similar in positioning, and able to bring reach as well as a prize. Extracted: campaigns whose title signals a collaboration reached the top fifth 29% of the time against 19% for the rest (title proxy, n=1,195).

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
- UGC: photo or video entry with a review or a use of the product. Fewer entrants, better content, needs clear rights wording. Ask for alt text with every image and captions on every video, in the brief and in the entry form, so entrants who use a screen reader can judge the submissions and the content is usable when the brand reposts it.
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
