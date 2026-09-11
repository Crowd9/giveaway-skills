# Mix by objective

Advice unless marked as extracted. Completion throughout this file means entries recorded on an action divided by the campaign's Entrants, shown here as a count % of Entrants: about 75 per 100 is three completions for every four Entrants.

## Patterns

| Objective | Required action | Supporting actions | Reach action | Leave out |
|---|---|---|---|---|
| Email list | Email signup with clear opt-in | Visit a key page, follow the main channel | Refer a friend, weighted high | Content tasks, account connections |
| Phone or messaging list | SMS or messaging opt-in with its own marketing consent (advice, no dataset support) | Email signup, visit a key page | Refer a friend | A second messaging channel in the same campaign |
| Followers on one channel | Follow on that channel | Engage with a pinned post, visit profile | Share the giveaway | Follows on channels the business ignores |
| Community members | Join the community | Answer a question that seeds a first post, follow main channel | Refer a friend | Anything that needs an app install |
| Content (UGC) | Submit a photo, video or review | Follow, visit a product page | Share | More than one content task |
| App installs | Download or play | Email signup as fallback, follow | Share | Actions on channels with no mobile path |
| Reach or launch awareness | Visit the launch page | Follow, engage with the launch post | Share, weighted highest | Long questions, content tasks |
| Local foot traffic | In-store code or visit | Follow, tag a local friend | Share to story | Email if the business cannot send to it |
| Qualified leads or demo requests (B2B) | A short qualifying question only a real buyer can answer, paired with email signup (advice, no dataset support for the pairing) | Visit the pricing or product page, follow the company channel | Refer a colleague | Anything that reads as payment for a review or a referral, content tasks, community joins nobody can moderate |

The B2B row is advice. What the data does hold is 6,138 B2B campaigns from 1,023 businesses, and what those businesses chose: 9 Entry Methods where B2C took 7, 87 referral entries per 100 Entrants where B2C saw 21, and email offered in 17% of campaigns where B2C offered it in 37% (extracted, the mix by the kind of business running it section below). None of that says whether a lead was qualified, because the dataset ends at the entry and carries no outcome after it. So treat a B2B giveaway as list building whose qualification happens in the question and in the follow-up, and tell the reader that is what they are buying.

A buyer's employer may have rules about being paid for a review, a referral or a public endorsement, and a regulated buyer may have more. Where the user raises that, drop the referral and review actions and put the reach into the question and the page visit, and say why.

## What the Gleam library templates ship (extracted)

Each Gleam library template ships a different default mix of methods, email and sharing. Refer A Friend leans hardest into sharing, the platform's own referral shape. E-Commerce Giveaway carries the most methods. [Scope: 100 or more Entrants, finance and crypto businesses excluded.]

| Template | Methods | Email offered | Share offered |
|---|---|---|---|
| Email Signup | 4 | 92% | 61% |
| Refer A Friend | 5 | 33% | 92% |
| E-Commerce Giveaway | 9 | 78% | 80% |
| Gleam Sweepstakes | 7 | 57% | 60% |
| Instant Entry | 1 | 6% | 7% |
| YouTube Contest | 7 | 8% | 46% |

Each template's default mix is a starting point, not a fixed one, so weight and add actions against the objective table above.

Source: `analysis/output/templates.json` (`by_template`).

### Every action has a job (advice, from Gleam's campaign team)

Five jobs, and every action in a recommended list carries exactly one of these labels. Acquire: email signup, SMS or messaging opt-in, account creation, app install, community join, the actions that create an owned relationship. Grow social: a follow on the one or two networks where the audience already is. Learn: a single-choice or open question that collects something the business can use, such as which flavour, which feature, which destination, never trivia. Engage: a visit, a video, a secret code, a bonus, exposure to the product. Amplify: Viral Share or refer a friend, low completion by nature and the only action that brings new people. A normal campaign has one of each, with a second social channel only when the audience is really there. Judge an amplify action by referrals, never by completion rate.

## Weighting

- Give the asset-producing action 3 to 5 entries. For sharing, weight it at the high end of what the platform allows unless the Prize is small enough that a high weight invites abuse: the share click rate (viral share clicks over Impressions) rises with the entries offered per referral.

| Weight offered | Share click rate |
|---|---|
| 1 | 38 per 100 Impressions |
| 2 to 4 | 39 per 100 |
| 5 to 9 | 48 per 100 |
| 10 or more | 60 per 100 |

[Campaigns/businesses: 7,655/2,274 (weight 1), 4,933/1,566 (2-4), 4,715/1,655 (5-9), 11,904/2,553 (10+). Extracted from `analysis/output/field_cuts.json`, share_clicks.by_share_worth.] This shows businesses who weight sharing higher see a higher click rate, not that raising the weight on one campaign would raise its clicks, since the businesses who choose a high weight may also run a more shareable campaign.
- One entry for visits and views. Two for follows and joins.
- Daily repeatable actions keep a long campaign alive and inflate the entries recorded per Entrant. Extracted: a typical campaign records 430 entries for every 100 Entrants, and campaigns with more repeatable bonus actions sit well above that.
- If the platform allows, make the asset action required before other actions unlock.
- Boosting worth pays off on the referral share action and mostly does nothing for follow or join actions, so put the worth budget where it pays. This is correlation, not causation, in both directions: businesses likely reach for worth-boosting on actions that are already underperforming, so the Telegram, YouTube and UGC numbers below may just reflect a response to that weakness, not an effect of the setting itself, and the same question applies to the referral result, since businesses who most want shares may both boost worth and write better share copy. Leave Telegram, YouTube and UGC worth at default: boosting it is not a fix for low completion there.

| Action | Effect of boosted worth |
|---|---|
| Referral share, 1,000-10,000 Entrants | +34-36% entries, 19-36% cheaper per completion |
| Referral share, 10,000+ Entrants | +7% entries |
| Follow (X, Twitch, TikTok) | within 15% either way, no consistent direction |
| Telegram Channel Members | 0.55x-0.70x completions |
| YouTube Entries | 0.53x-0.94x completions |
| UGC submissions | 0.20x-0.62x completions |

[Extracted from `analysis/output/asset_yield.json`, `yield_by_asset_and_worth_tier`.]

## Actions that came with more people (extracted)

Among the campaigns we can compare fairly (no repeatable action, a run of 14 days or less, which is what makes Impressions comparable), Secret Code (a code shown on a stream, in a newsletter or in store) is the standout: it comes with more Entrants at no conversion cost, the only action with that shape. Actions that pull a single-channel audience convert far better on arrival, with fewer Entrants overall. These describe businesses' choices and audiences, never an action's effect.

| Action | Entrants vs baseline | Conversion vs baseline |
|---|---|---|
| Secret Code | +16% | no cost |
| App Downloads | +21% (likely large, established apps) | - |
| Telegram Channel Members | fewer | +46% |
| YouTube Entries | fewer | +76% |
| Twitch Follows | fewer | +13% |
| Other social follows, X Reposts, Chat Members, Facebook Likes | fewer | lower |

An app-download action's payoff depends heavily on the Prize. Match the action to a Prize the Entrant already wants the app for, and expect it to cost you against a cash or gift-card Prize or in gaming and esports specifically. These counts are small, down to 33 businesses, near this skill's floor for a cut this fine, so state the count every time and don't extend the pattern beyond these three cells.

| Context | Effect on conversion (against what the action and Prize predict separately) |
|---|---|
| Prize is tech hardware | 1.54x, earns its place (203 campaigns, 33 businesses) |
| Prize is a gift card or cash | 0.585x, costs conversion (64 campaigns, 36 businesses) |
| Gaming and esports vertical | 0.588x, costs conversion (89 campaigns, 27 businesses) |

[Extracted from `analysis/output/success_profiles.json`, `interactions.entry_method_by_prize_type` and `.entry_method_by_industry`.]

## What it looks like when many Entrants were referred (extracted)

A share action's value is the people it brings, which the dataset does not count. Campaigns offering one had more Entrants and lower conversion typically [`cmp_share` in action-families.md: 544 Entrants against 406, and conversion 23% lower], so treat it as an amplify action with a job, weight it for referrals, and expect low completion.

Among 16,745 campaigns offering a share action, the typical campaign records 13 referral entries for every 100 Entrants, and the top tenth 65 or more (each referral entry is a referred Entrant times an entry worth the dataset does not carry). The top tenth is a Twitter-centred gaming and hardware audience [tech hardware Prizes in a third, Twitter follow offered in three quarters, retweet in 40%, email signup in only a third], with a slightly cheaper first Prize, fewer Entrants than the typical campaign and lower conversion. A high share of referred Entrants in this data marks an audience that refers for entries. It does not show that referrals grew the audience, because the dataset lacks referral clicks, successful sharers and viral conversion rate, which the platform's own Viral Share report holds.

**A share action is a design tradeoff, not a free addition.** When reach or new people is the objective, its reach and referral gain is worth the completion it costs elsewhere, and it's the case where a share action clearly earns its place. When the objective is a tight, high-completion list, that same cost is the reason to leave sharing out or push it to the bottom of the list. Consistent at every campaign size tested. [1,000-2,500, 2,500-10,000, 10,000+ Entrants.]

What it buys:

| Metric | Change with a share action |
|---|---|
| Impressions per Entrant | +30-60% (1.34x-1.57x) |
| Entries per Entrant | +20-26% |
| Visits to the business's own site | +19-75% |
| Referral entries from people the campaign didn't already reach | 13 per 100 Entrants typical, 65+ in the top tenth (see above) |

What it costs (completion on other actions running beside it, all directionally consistent at every size tested):

| Action | Completion multiplier |
|---|---|
| X Follows | 0.42x-0.71x |
| Twitch Follows | 0.20x-0.66x |
| Chat Members | 0.66x-0.83x |
| Telegram Channel Members | 0.50x-0.70x |
| YouTube Entries | 0.68x-0.75x |
| App Downloads | 0.74x-0.96x |
| UGC submissions | 0.20x-0.27x |

Sharing's effect on email specifically depends on campaign size and is unsettled (cheaper and lower-yield at the smallest size, roughly flat to worse at 2,500-10,000 and 10,000+ Entrants), so don't claim sharing makes email cheaper or higher-yield as a general rule. [1,202 to 10,779 campaigns per group, 376 to 2,845 businesses. Extracted from `analysis/output/asset_yield.json`, `yield_by_asset_and_sharing`.] For the reach-side framing (what a share action brings in, weighed against what it costs elsewhere), see giveaway-promotion-plan.

**A few action pairs cluster well above chance, and they're the effort-heavy ones.** As with the family table above, this describes what businesses choose to run together, not what pairing two actions would do to either one's completion.

| Action pair | Co-occurrence lift |
|---|---|
| Content + account-connection | 1.87x (1,151 campaigns, 284 businesses) |
| Content + engagement | 1.67x (1,040 campaigns, 398 businesses) |
| Email + follow, the most common pair in the data | 0.95x, the only common pair below 1.0 (9,603 campaigns, 1,838 businesses) |

[Extracted from `analysis/output/method_mix.json`, `family_pair_lift`.]

## Actions more common in top campaigns, by vertical (extracted)

Within each vertical (a regex on business, campaign and Prize names, so rough), campaigns split into fifths by Entrants. The ratio is how much more often an action appears in the top fifth than the bottom fifth. Association only: bigger businesses choose differently.

| Vertical | Campaigns | Actions over-represented in the top fifth |
|---|---|---|
| Gaming | 6,503 | Twitch Subscribers 1.7x, Custom Actions 1.7x, Secret Code 1.5x, Twitch Follows 1.3x, Bonus 1.2x |
| Technology | 1,717 | Single Choice List 7.2x, Facebook visits 1.4x, YouTube Channel Visits 1.3x, Instagram Profile Visits 1.3x |
| Home | 883 | YouTube Channel Visits 2.3x, Custom Actions 1.7x, X Posts 1.6x, Pinterest Visits 1.4x, Viral Shares 1.3x |
| Food and drink | 989 | YouTube Channel Visits 2.2x, Facebook visits 1.4x, Instagram Profile Visits 1.2x |
| Fitness and outdoor | 878 | Answer a Question 1.6x, Bonus 1.2x |
| Travel | 1,758 | Secret Code 1.5x, Answer a Question 1.4x, Instagram Profile Visits 1.2x |
| Software | 363 | X Reposts 1.7x, Bonus 1.4x, YouTube Channel Visits 1.3x, Viral Shares 1.3x |
| Fashion and beauty | 359 | YouTube Channel Visits 1.8x, Instagram Profile Visits 1.3x, Bonus 1.3x |

Gleam's internal analysis of the same export, with its own industry labels, found the same shape: questions and single-choice actions over-represented in technology and food, Twitch and custom actions in gaming, Pinterest and YouTube in home. Two readings of one dataset agreeing is still one dataset.

On action count: the top fifth and bottom fifth both ran a typical 7 actions, so count alone does not separate them. The finding from the campaigns we can compare fairly points the same way: eleven or more actions came with 17% more Entrants than one to three, alongside lower conversion and far more Entries per Entrant [`cmp_methods` in action-families.md]. Keep the list purposeful and tied to the assets you can use.

**The exact combination businesses reach for differs by vertical, beyond what the per-family table above shows.** In electronics and tech and gaming and esports, the single most common exact action set skips email entirely and anchors on follow plus visit. In food and drink, sports and outdoors and media and entertainment, the most common sets are all built around email, visit and share together, with an extra action or two layered on. This is consistent with, not independent of, the per-family email-offered shares already in the sections above. [Campaigns, all clearing the size floor comfortably (334 to 1,840 businesses overall): electronics and tech 7,289, gaming and esports 6,328, food and drink 1,787, sports and outdoors 2,268, media and entertainment 5,019. Extracted from `analysis/output/method_mix.json`, `top_combinations_by_industry`.]

**Gaming and esports campaigns lean on Discord, Twitch and Telegram over the baseline, and underuse email.** Email is the weak spot in this vertical: offered less often than the baseline, and where it is offered it completes at 0.77x the baseline, the worst of the three actions in the table below that carry a completion figure. Don't lean on email as the primary acquisition action for a gaming campaign.

| Action | Gaming and esports | All-industry baseline | Ratio |
|---|---|---|---|
| Chat Members offered | 38.0% | 16.1% | 2.4x |
| Twitch Follows offered | 38.6% | 16.8% | 2.3x |
| Telegram Channel Members offered | 7.9% | 4.5% | 1.7x (completion 1.20x baseline) |
| Referral share offered | 31.6% | 45.1% | completion 1.16x baseline |
| Email offered | 20.8% | 43.5% | completion 0.77x baseline |

[6,327 gaming and esports campaigns, 1,413 businesses. Extracted from `analysis/output/vertical_profiles.json`, `action_index_by_industry`.]

## Mix by the kind of business running it (extracted)

From `analysis/output/industries.json`. Every group listed clears 30 campaigns and 10 businesses.

By audience (by_audience), typical values:

| Audience | Campaigns | Businesses | Methods | Referral entries % of Entrants | Email offered |
|---|---|---|---|---|---|
| B2C | 39,320 | 8,130 | 7 | 21 | 37% |
| B2B | 6,138 | 1,023 | 9 | 87 | 17% |
| Both | 2,170 | 330 | 8 | 89 | 20% |

B2B and mixed-audience businesses run more methods than B2C and lean far more on referrals, with email offered less often.

By stage (by_org_stage), typical values:

| Stage | Campaigns | Businesses | Methods | Referral entries % of Entrants | Email offered |
|---|---|---|---|---|---|
| Startup | 14,661 | 4,088 | 9 | 91 | 14% |
| Small business | 20,470 | 3,580 | 7 | 14 | 51% |
| Mid market | 6,813 | 815 | 6 | 20 | 30% |
| Enterprise | 2,902 | 280 | 7 | 24 | 31% |
| Individual | 1,792 | 426 | 8 | 17 | 16% |

Startups run the most referral-heavy mix of any stage and offer email least often next to individuals. Small businesses sit at the other end, email offered in half of campaigns and referrals a small fraction of a startup's.

By business type (by_business_type), email offered, lowest to highest:

| Business type | Campaigns | Businesses | Email offered | Referral entries % of Entrants |
|---|---|---|---|---|
| Community | 1,923 | 490 | 5% | 103 |
| Creator | 4,175 | 1,026 | 8% | 16 |
| Software | 18,311 | 4,205 | 12% | 95 |
| Agency | 1,374 | 171 | 23% | 63 |
| Other | 2,236 | 551 | 24% | 25 |
| Service business | 1,157 | 255 | 39% | 10 |
| Nonprofit | 265 | 94 | 40% | 11 |
| Media or publisher | 5,556 | 703 | 49% | 14 |
| Retailer | 7,952 | 996 | 50% | 11 |
| Brand | 11,380 | 2,578 | 50% | 15 |

Community businesses offer email least, creators next. Community and software are the two most referral-heavy business types in the data, both above 90 referral entries % of Entrants, well ahead of agency in third place at 63.

## Mix by country (extracted)

Action shares among campaigns with 100 or more Entrants, by the business's country. Source: `analysis/output/country_cuts.json`, by_country.

| Country | Campaigns | Businesses | Notable action shares |
|---|---|---|---|
| Japan | 6,505 | 291 | Telegram Channel Members 51%, Email Subscriptions 5% |
| India | 6,010 | 873 | Wallet address 48%, Telegram Channel Members 61% |
| Brazil | 5,860 | 563 | Instagram Profile Visits 70%, typical run 1 day, typically 10 methods |
| Australia | 6,433 | 1,406 | Email Subscriptions 47%, Facebook 54% |
| United Kingdom | 15,716 | 1,847 | Share or refer 24% |
| United States | 58,843 | 9,105 | Instagram Profile Visits 50%, Facebook 49% |

Japan and India both lean on Telegram. India adds a wallet-address action, the crypto marker this skill's default figures exclude elsewhere, in close to half its campaigns. Brazil's campaigns run a typical one day and carry 10 Entry Methods, the most of any country in this table and second across the whole cut to Egypt's 13 on 736 campaigns. Both figures come from automated recurring draws: its 25th percentile duration is also 1 day, 90% of its campaigns are repeats and 94% start on the hour. Read the row as what those accounts do. Australia and the US split their most common single action between email or Instagram and Facebook. The UK's most common reach action is sharing or referring.

**How often actions are required.** Malaysia requires at least one action in the large majority of its campaigns, India follows, and also asks for the most required actions once it asks for any. Germany and the US sit at the other end.

| Country | Campaigns with 1+ required action | Typical required actions (where 1+) |
|---|---|---|
| Malaysia | 90% (2,345 campaigns, 160 businesses) | - |
| India | 79% (6,010 campaigns, 873 businesses) | 6 |
| Germany | 31% (3,530 campaigns, 472 businesses) | - |
| United States | - | 1 (58,839 campaigns, 9,104 businesses) |

[Source: `analysis/output/indicators.json`, mandatory_actions_by_country.]

**Question actions.** A question action is closer to routine in East and Southeast Asia than elsewhere. Answer validation stays rarely on wherever the question action runs, under a tenth of question actions in every country in this table.

| Country | Share of campaigns with a question action |
|---|---|
| China | 61% (2,613 campaigns, 166 businesses) |
| Vietnam | 56% (3,762 campaigns, 773 businesses) |
| United States | 13% (58,843 campaigns, 9,105 businesses) |
| Canada | 8% (7,276 campaigns, 1,156 businesses) |

[Source: `analysis/output/indicators.json`, question_action_by_country.]

**Worth settings, crypto and SaaS businesses removed.** Poland's typical top worth on a campaign runs well above the other countries measured here.

| Country | Typical top worth |
|---|---|
| Poland | 25 (1,956 campaigns, 145 businesses) |
| United States | 5 (54,208 campaigns, 7,941 businesses) |
| United Kingdom | 3 (13,988 campaigns, 1,481 businesses) |
| Australia | 3 (5,943 campaigns, 1,247 businesses) |

[Source: `analysis/output/indicators.json`, mechanics_by_country_excluding_crypto.]

These describe businesses' choices in each country, never a country's effect on a campaign.

## What each action produced per campaign (extracted)

Typical completions per campaign among campaigns that offered the action, completions % of Entrants, and stated USD of Prize per completion where the pool was valued. A completion is a signup, follow or join at that moment. Full table with quarter-by-quarter detail and campaigns by size in the results-review skill.

| Asset | Campaigns | Typical per campaign | Share of Entrants | Stated USD per completion |
|---|---|---|---|---|
| Email Subscriptions | 39,532 | 712 | 99 | 0.40 |
| X Follows | 66,279 | 309 | 61 | 0.64 |
| Instagram Follows | 8,234 | 372 | 61 | 0.81 |
| TikTok Follows | 14,329 | 230 | 38 | 1.22 |
| Twitch Follows | 22,521 | 335 | 77 | 0.57 |
| YouTube Entries | 3,506 | 374 | 83 | 0.70 |
| Chat Members | 19,190 | 268 | 48 | 1.15 |
| Telegram Channel Members | 4,153 | 640 | 88 | 0.77 |
| App Downloads | 3,495 | 339 | 41 | 1.31 |
| Referral entries (Viral Shares) | 42,900 | 88 | 12 | 2.89 |
| Content submissions | 3,308 | 112 | 18 | 15.89 |

Stated Prize value per email signup and per follow by vertical sits in the Prize picker's `roi-benchmarks.md`. An Email Subscriptions action in a typical campaign produced about 700 addresses. The same campaign's Viral Share produced about 90 referral entries, and a content action about 110 submissions.

## Wording and destinations (extracted)

Completions % of Entrants for the action, typical value across campaigns offering it.

Completions % of Entrants by position in the action list, from `analysis/output/field_cuts.json` `uptake_by_family_and_position`:

| Family | 1st | 2nd to 4th | 5th or later |
|---|---|---|---|
| Email signup | 101 (21,831 campaigns) | 78 (10,654 campaigns) | 74 (17,983 campaigns) |
| Visit a page | 98 (15,926 campaigns) | 87 (90,592 campaigns) | 76 (150,937 campaigns) |
| Follow or subscribe | 100 (48,793 campaigns) | 79 (144,024 campaigns) | 52 (171,892 campaigns) |
| Content upload | 86 (2,858 campaigns) | 33 (5,917 campaigns) | 17 (9,707 campaigns) |
| Share or refer | 21 (1,351 campaigns) | 16 (14,581 campaigns) | 27 (55,641 campaigns) |

Everything except sharing falls down the list, and a follow loses half its completions between first place and fifth. Put the action that captures the asset at the top. Sharing sits at 21% of Entrants in first and 16% in the next three, then 27% fifth or later, where long action lists with a required share sit, so its position is free and it can take the bottom slot.

The position advantage extends past email and follow, and holds by campaign size. The ratio below is the asset's completions per Entrant in the first list position over the same asset later in the list, split into three groups by campaign size. [Scope: 1,000+ Entrant campaigns. Extracted from `analysis/output/asset_yield.json`, `yield_by_asset_and_position`.]

| Asset | 1,000-2,500 | 2,500-10,000 | 10,000+ |
|---|---|---|---|
| Email Subscriptions | 1.42x | 1.45x | 1.28x |
| X Follows | 1.43x | 1.57x | 1.60x |
| Instagram Follows | 1.40x | 1.76x | 1.99x |
| Twitch Follows | 1.68x | 1.76x | 1.98x |
| Chat Members | 1.61x | 1.90x | too few campaigns to report |
| YouTube Entries | 2.09x | 2.23x | too few campaigns to report |
| Visit the business's own site | 1.36x | 1.51x | 1.51x |

Every asset with enough volume to test held its position advantage at every size. Chat Members and YouTube Entries don't clear enough campaigns at 10,000+ Entrants to report. [Campaign counts behind the ratios above range from 31 (Instagram Follows, first position, 10,000+ Entrants, 15 businesses) to 26,147 (visits to the business's own site, later position, 1,000-2,500 Entrants, 2,564 businesses).]

**Which asset goes first, when the objective is reach.** The advice above is to put the asset action first, and that has a direction when the asset is sharing. In campaigns offering both an email action and a share action, listing share before email records more share completions on lists of 1 to 6 methods and on lists of 11 or more, and fewer on lists of 7 to 10. The gain is worth planning around only at 11 or more methods, where share-first campaigns record about two thirds again the share completions. Treat the short-list difference as too small to act on. This is about order within a fixed list. List length is the separate friction effect further down this file.

| Method count | Share completion, share-first | Share completion, email-first |
|---|---|---|
| 1-6 methods | 14 per 100 | 12 per 100 |
| 7-10 methods | 10 per 100 | 13 per 100 |
| 11+ methods | 34 per 100 | 20 per 100 |

Email does not consistently pay for it: it completes about 83 to 104 per 100 Entrants when it follows a share action, against roughly 89 to 101 when it leads, lower on short lists and level or a little higher on longer ones. [Share-first campaigns/businesses: 676/257 (1-6), 1,827/424 (7-10), 4,567/528 (11+). Email-first: 5,877/1,669 (1-6), 6,965/1,893 (7-10), 7,511/1,240 (11+). Extracted from `analysis/output/method_mix.json`, `share_position_relative_to_email` and `top_combinations`.]

A cross-check on exact combinations shows the same direction on share: follow, visit and share with no email completes about 45 per 100 Entrants on share [3,802 campaigns, 1,367 businesses]. Add email to a share-carrying shape and share completion runs about 8 to 36 per 100 across the five combinations carrying both, under the matching shape without email in every pair.

**What leads the list and overall conversion.** Campaigns led by different action families show different conversion, pooled across every method count, not split by list length. This is an association across the whole dataset, not a comparison within a fixed list length, and businesses who lead with a quick connect-account step or a single question may already be running a leaner campaign in every other respect. Treat it as a pattern to weigh, not a rule to follow.

| Lead action family | Conversion Rate | Campaigns | Businesses |
|---|---|---|---|
| Question | 30.9% | 7,338 | 1,257 |
| Account connection | 30.5% | 4,816 | 1,343 |
| Follow | 28.2% | 16,473 | 4,565 |
| Join | 27.1% | 2,638 | 858 |
| Visit | 26.7% | 31,153 | 6,209 |
| Email | 26.7% | 21,169 | 3,832 |
| Bonus | 26.2% | 19,139 | 3,807 |
| Share | 23.9% | 2,753 | 927 |
| Engage | 22.3% | 2,869 | 445 |
| Download | 20.9% | 656 | 259 |
| Content | 14.7% | 1,765 | 654 |

A question or an account connection at the head of the list sits about four points above a visit, an email or a bonus, and content sits twelve points below them. The spread across the seven middle families is under two points, so what leads matters far less than whether the first thing asked is a piece of work. These are campaigns grouped by what they happened to lead with, never a test of moving an action to the front.

[Source: `analysis/output/method_mix.json`, `lead_action_family`.]

Question actions by what they ask (regex on the question text):

| Question type | Actions | Businesses | Completed it, per 100 Entrants (typical) |
|---|---|---|---|
| feedback or open | 844 | 375 | 85 |
| detail capture | 5,224 | 708 | 77 |
| other | 8,685 | 1,666 | 71 |
| preference | 3,485 | 901 | 70 |
| trivia | 1,647 | 330 | 62 |

An open or feedback question is completed most, by about 85 of every 100 Entrants, and trivia least at 62. Trivia is the only type with a right answer, which is the plain reading of why it sits last. Detail capture, the type that asks for a name, an order id or an account, sits second at 77. [Source: `analysis/output/text_and_context.json`, `question_types`.]

Share copy on Viral Share and X Posts actions (59,548 actions with custom text, from `analysis/output/text_and_context.json` `share_copy`): a hashtag, first person and an emoji all complete higher. Length does not run one way, with short copy highest and the 60 to 140 character band lowest. Most of the hashtag gap is the action type, since X Posts actions carry hashtags and record more completions than Viral Share (about 34 against 11 per 100 Entrants), first person and an emoji still sit higher within the same copy length. Nearly every campaign wrote custom share text, so the default cannot be compared.

| Copy trait | Completion (per 100 Entrants) |
|---|---|
| Short, under 60 characters | 24 (1,139 actions) |
| Medium, 60-140 characters | 16 (39,841 actions) |
| Long, over 140 characters | 20 (18,568 actions) |
| No hashtag | 13 (46,841 actions) |
| With hashtag | 35 (12,707 actions) |
| Not first person | 15 (49,458 actions) |
| First person | 29 (10,090 actions) |
| No emoji | 16 (56,701 actions) |
| With emoji | 33 (2,847 actions) |

Visit actions by where they send people:

| Destination | Actions | Share who completed it (typical) |
|---|---|---|
| another site | 121,815 | 77 |
| YouTube | 49,522 | 85 |
| the business's own site | 10,333 | 97 |
| another Gleam campaign | 583 | 85 |
| Steam | 303 | 79 |
| Instagram | 194 | 95 |
| Facebook | 117 | 58 |
| Amazon | 101 | 69 |

A visit to the business's own site is completed by almost everyone at 97 per 100 Entrants, a YouTube channel by 85 and any other site by 77. Two thirds of visit actions land in that last row, which is every destination the rules do not name, so it carries no one kind of page. [Source: `analysis/output/text_and_context.json`, `visit_destinations`.]

Email Subscriptions by the description under the action:

| Newsletter description | Actions | Share who completed it (typical) |
|---|---|---|
| no description | 9,429 | 95 |
| description without those | 5,476 | 84 |
| mentions frequency or unsubscribe | 2,169 | 85 |

No description at all ran highest. A description, with or without frequency and unsubscribe wording, went with about a tenth fewer completions. More words under the checkbox give people more to think about. Write the frequency line anyway where the law asks for it, and keep it to one line.

## Friction

Longer lists went with a lower share of Impressions converting, though their Entrant counts held up. Extracted: a typical campaign offers 7 methods and the top tenth offers 16 or more. Nothing in the data shows the effect of adding a method, so keep the count tied to the number of assets you can use. Three assets, five to eight methods.

Actions that cost the most: account connections (sign in with a social account), app installs, anything that leaves the entry page, and content creation. Keep those optional unless they are the objective.

**A single well-chosen action beats most combinations.** Among campaigns running exactly one action family, a question-only campaign gets more Entrants through than any other single-family or multi-family combination tested. This ranks the leanest campaigns against each other and does not repeat the method-count table below, it says which single action to reach for when the campaign only needs one.

| Single-family campaign | Conversion Rate |
|---|---|
| Question-only | 54.9% (862 campaigns, 135 businesses) |
| Bonus-only | 44.2% (437 campaigns, 184 businesses) |
| Email-only | 44.2% (1,017 campaigns, 223 businesses) |
| Visit-only | 42.6% (1,160 campaigns, 286 businesses) |
| Any 2+ family combination | below 40% |

[Extracted from `analysis/output/method_mix.json`, `top_combinations`.]

**More required actions costs completion on the optional ones, not overall conversion.** Holding total method count fixed, adding required actions lowers completion on whatever stays optional, while the campaign's conversion barely moves. Whether this is fatigue or businesses routing their lower-appeal actions into optional slots when they require more elsewhere can't be told apart in this data.

| Methods | Required actions | Optional-action completion | Conversion Rate |
|---|---|---|---|
| 7-10 | 0 | 67 per 100 | 25.1%-27.4% |
| 7-10 | 1 | 50 per 100 | 25.1%-27.4% |
| 7-10 | 2 | 49 per 100 | 25.1%-27.4% |
| 7-10 | 3+ | 43 per 100 | 25.1%-27.4% |
| 11+ | 0 | 58 per 100 | 18.6%-21.1% |
| 11+ | 3+ | 36 per 100 | 18.6%-21.1% |

**Exactly one required action goes with the biggest crowd, in every method band.** The Entrant count peaks at one
and drops on either side, and the shape repeats three times:

| Methods | 0 required | 1 required | 2 required | 3 or more |
|---|---|---|---|---|
| 1 to 6 | 436 | 544 | 412 | 390 |
| 7 to 10 | 484 | 644 | 386 | 408 |
| 11 or more | 560 | 747 | 408 | 546 |

One required action goes with 25% to 33% more Entrants than requiring none, and 32% to 83% more than requiring
two. Three separate bands landing on the same shape is worth more than any one of them, and the groups are large:
the smallest cell holds 1,908 campaigns from 436 businesses.

Read it as the signature of a campaign built around one asset. A business that requires exactly one action has
usually decided what the campaign is for and put a push behind it, where requiring none leaves the entry free and
requiring three makes the reader work before they are in. Nothing here shows that switching an action to required
would add Entrants to this campaign.

[7-10 methods: 553 to 5,493 campaigns, 275 to 1,660 businesses per group. 11+ methods: 503 to 6,107 campaigns, 174 to 1,226 businesses per group. Extracted from `analysis/output/method_mix.json`, `mandatory_count_vs_optional_completion`.]

**Conversion falls steadily with every action added, and there is no reliable point where it stops.** The curve halves between one action and thirteen, and quoting a single turning point to a reader overstates what the data holds.

| Actions | Campaigns | Conversion Rate |
|---|---|---|
| 1 | 4,887 | 49.9% |
| 4 | 4,312 | 35.4% |
| 7 | 3,327 | 31.3% |
| 10 | 1,649 | 27.3% |
| 13 | 997 | 26.0% |
| 16 | 289 | 25.3% |
| 20 | 524 | 68.8% |

A two-segment fit over the pooled 38,810 campaigns [`analysis/output/thresholds.json`, `action_count`] puts its breakpoint at 15 to 16 actions, and that is the fitter finding where the curve turns back up, never where the decline eases. The same search repeated inside each industry, size band and plan tier lands anywhere from 3 to 17 across eighteen groups, with the 10,000-plus band at 3 and the 500 to 1,000 band at 17. The source calls that stratification noise, and it is: no ordering by size, tier or industry survives it. So never quote a reader an elbow for their own group, and never promise them a count where the cost stops.

What the curve does support is the shape. Each action from the first to about the thirteenth costs Conversion Rate, steeply at first and more slowly later. Past sixteen it climbs back up on a few hundred campaigns per point, likely a handful of unusually well-optimized businesses still clearing 100 Entrants at that length, and that climb is no evidence that more actions help. [Ratios against what action count and size predict separately ran 91%-110% for conversion and 92%-111% for engagement, across all 12 groups. Extracted from `analysis/output/thresholds.json`, `action_count`, and `analysis/output/success_profiles.json`, `interactions.action_count_by_conversion_and_band` and `.action_count_by_engagement_and_band`.]

**Campaigns running more actions convert lower, and that holds inside most industries and not only pooled across all of them.** [`analysis/output/vertical_profiles.json`, `top_quartile_vs_rest_by_industry`.] In at least 15 of the 21 industries tested, the top quarter by conversion runs fewer actions and far less social or referral friction than the rest of that same industry, a like-for-like version of the pattern above.

| Metric | Top quarter vs rest of industry | Industries showing this direction |
|---|---|---|
| Actions run | 0.67x | 18 of 21 |
| Referral share offered | 0.50x | 18 of 21 |
| Secret code offered | 0.57x | 15 of 21 |
| Platform follow offered | 0.71x | 16 of 21 |

Two examples:

| Industry | Top quarter actions | Rest actions | Top quarter referral offered | Rest referral offered |
|---|---|---|---|---|
| Electronics and tech | 4 | 6 | 0.3% | 26% |
| Apparel and fashion | 1 | 4 | 3.6% | 25% |

[Electronics and tech: 1,434 campaigns/119 businesses top quarter, 4,299/852 rest. Apparel and fashion: 503/50 top quarter, 1,500/335 rest.]

A tenth-level check strengthens toward the extremes, it does not flatten out, consistent with a real relationship, not an artifact of one cutoff:

| Metric | Top tenth vs bottom tenth | Ratio | Quarter-level ratio (above) |
|---|---|---|---|
| Referral offered | 11.9% against 39.2% | 0.30 | 0.45 |
| Secret code offered | - | 0.27 | 0.44 |
| Platform follow offered | - | 0.50 | 0.61 |

This prices the fourth and fifth action, it is not an instruction to cut down to one. A campaign that needs three assets cannot run a one-action campaign, and nothing here says it should. What each added action, especially a referral or a secret code, costs on this specific completion measure is the number to weigh against what that action collects, so add it when the campaign needs that asset and budget for this rate to move. Conversion here is Entrants over Impressions, and a lean single-action entry form structurally has less friction between an Impression and a completed entry, so part of the pattern may describe how the metric is built as much as business choice. It does not mean a heavier campaign performs worse on total entries or reach, only on this completion rate. The top quarter itself is defined by conversion, one objective among several (an email list, followers, UGC and reach are the others), so an industry's top quarter by conversion is not automatically the shape to copy when the campaign's objective is one of those. Cite this finding with both caveats every time. Email offered and completion did not survive this same check (mixed direction, completion flat at a typical ratio of 0.995 across industries) and neither did community-join actions or question actions, so none of those are a vertical-strength signal here. [Extracted from `analysis/output/vertical_profiles.json`, `top_quartile_vs_rest_by_industry` and `threshold_check_top_vs_bottom_decile_pooled`.]

## Invalid entries (extracted)

Gleam marks an entry invalid when its check fails: a follow that was undone, a duplicate account, a rejected answer, a referral that did not verify. Plan for a few percent of entries to fall away at verification, more when the mix leans on referrals, and say so in the terms. These are typical values of what businesses saw, and invalid entries were already excluded from every other figure in these references.

| Context | Invalid entry rate |
|---|---|
| Typical campaign | 4.2% |
| With a share or referral action | 4.5% |
| Without one | 3.2% |
| Chat Members offered | 4.5% (3.7% without) |
| X Reposts offered | 4.2% (3.7% without) |
| Email Subscriptions offered | 4.3% (3.4% without) |
| Twitch Follows offered | 2.6% (3.9% without) |
| Question action validated the answer | 3.2% |
| Question action did not validate | 3.2%, the same |

[Across 116,499 ordinary campaigns: 42% had 5% or more invalid, 7% had 20% or more. Question-validation comparison: 516 campaigns validated, 39,334 did not.]

## Consent and rules

Entry consent and marketing consent are two separate things, and a campaign needs both collected in the right place. Entry consent is agreement to the terms of the giveaway, and it is collected on the entry form and recorded in the terms the Entrant accepts. Marketing consent is agreement to be contacted afterwards, and it is collected at the email or messaging action itself, in its own wording, with its own checkbox. One does not imply the other, and an Entrant who declines the second is still a valid Entrant.

- Email entries need opt-in wording that says what the Entrant will receive and how to leave. Many jurisdictions require it and most email tools enforce it.
- Where the region requires double opt-in (Germany and much of the EU for email, and most regimes for SMS), the confirmation goes out at the moment of capture and only confirmed contacts join the list. Plan for a share of Entrants never confirming.
- Retention is a legal question this skill cannot answer. How long entry data, contact details and Winner records may be held, and what has to be deleted at the end, goes to the business's privacy counsel before the campaign opens.
- Follow-to-enter, tag-a-friend and share-to-enter are governed by each network's promotion rules, which change. Read the current rules for each network you name.
- Do not require a purchase to enter where sweepstakes law forbids it. Discount codes as entries count as a purchase condition in most readings.
- Age and region limits belong in the terms and on the entry form.

This skill does not give legal advice.

Extracted: 28% of Email Subscriptions actions in the ordinary campaigns showed an explicit opt-in checkbox. Expect roughly one in ten Entrants to skip a visible checkbox, those who tick it are the list you can mail. [Where the checkbox was on, the typical Email Subscriptions action recorded 89 entries per 100 Entrants against 101 where it was off, the campaigns we can compare fairly, 812 campaigns/227 businesses with the checkbox on, 2,612/758 without.]

## Store campaigns

The actions a store wants send the Entrant into the catalogue and bring something back.

- **Visit a product or collection page.** The Visit a Page action is in four out of five campaigns at a typical 78 completions % of Entrants (63,172 campaigns). Point it at the page the campaign is about, not the home page.
- **Answer a question with the product.** "Which item would you pick" or "paste the link to your cart or wishlist" as the required action. Question templates ran a typical 81 completions % of Entrants (4,875 campaigns, 976 businesses). The answers are the wishlist data a cart campaign exists to collect.
- **Pick your Prize.** A choice action with the three Prize options, so the preference is recorded on entry.
- **Subscribe with the store tag.** The Email Subscriptions action synced to the store's customer list with the campaign name as the tag, so the non-Winner code and the welcome series go to the right segment.
- **Refer a friend.** Where the platform can cap referrals per person, leave the cap off unless the Prize is small enough that referral farming pays. The friend lands on the store, and the referrer earns entries when the friend enters. A second reward when the friend buys is a mechanic the store can run through its own code, with no figure in the dataset.
- **Keep purchase out of the entry.** An order number as an entry, or bonus entries for buying, is a purchase condition. Where it runs at all it needs a free entry route of equal weight and a lawyer's read of the terms.

## Keeping a follow after the campaign (advice)

Common practice, nothing in the data covers it. This is about every Entrant who followed to enter, and almost
all of them lose. A Winner is one person among hundreds and their follow is a rounding error either way. What
the campaign data cannot see is whether the other several hundred are still following a month later, because it
records the Action completed at the moment of entry and never looks again. Say that plainly when a reader asks,
then give them this.

- Measure it yourself, because it is the only way anyone finds out. Write down the follower count on the day the
  campaign opens, the day it closes and 30 days after, on each network you asked people to follow. Two campaigns
  in and the reader has a number for their own audience, which beats any benchmark.
- Ask for the follow on the network where the business actually posts. A follow on an account that goes quiet
  for six weeks is the one that lapses.
- Give the new follower something within the first week. The welcome series, the Winner announcement and the
  non-Winner offer are all reasons to appear in a feed while the campaign is still why they are there.
- Where the objective is a list, weight the email Action above the follow. An address is
  yours and a follow sits on somebody else's platform.
- Treat the follower count on the close day as the top of the range. The business keeps some share of those
  Entrants and nothing here says what share.

## Using what you built (advice)

The list is the point of the campaign, and it decays from the day the Winner is announced. The first 30 days decide whether it becomes an audience. All of this is practice, with nothing in the dataset to support it.

- **Welcome series.** Four messages: a welcome with the referral link within a day of entry, sent by the email provider when the sync lands, then the result and two brand messages over the fortnight after the draw. The first names the giveaway so nobody wonders who is writing. The rest do the job the giveaway could not: what the business sells, why anyone buys it, one reason to come back.
- **A separate segment.** Tag the giveaway group and keep it apart from customers and organic signups for at least 90 days. Its open and complaint rates run differently and will distort the reporting on the rest of the list if they are mixed.
- **A sunset rule.** Set it before the campaign opens. No opens in 60 or 90 days, one re-permission message, then out of the sending list. A giveaway list that is never pruned quietly damages deliverability for every other campaign.
- **Consent noted at capture.** Store what the Entrant agreed to, in what wording, on what date, alongside the address. That record is what answers a complaint or an audit later, and it cannot be reconstructed after the fact.
- **Followers and community members get the same treatment.** A first post that welcomes the new arrivals and says what the channel is for, then the normal cadence. A community with nothing happening in it loses the people a giveaway just brought.

The messages themselves, including the Winner announcement and the consolation offer to everyone who did not win, belong to giveaway-winner-communications.
</content>
