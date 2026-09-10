# Action families

Extracted from the campaigns we can compare fairly (crypto, ambiguous and purchase-only campaigns removed). Platform-specific action types were mapped by hand to generic families so the advice works on any platform. [Completion is entries recorded on a method divided by the campaign's valid Entrants, capped at 5, then the typical value across campaigns that offered the family, converted here to a count per 100 Entrants with the raw figure alongside for tracing. Entries are actions completed times the entry worth the business set, and entry worth is unknown in the dataset, so a figure near 100 per 100 means most Entrants did it only where the worth was 1, repeatable actions and referrals can pass 100. The bracketed range in the table below is the middle half of campaigns, between the lower and upper quarter, and its top marks the level nine campaigns in ten sit below.]

<!-- generated:entry_families -->
| Action family | Campaigns using it | Share of campaigns | Uptake median (IQR) | n with uptake |
|---|---|---|---|---|
| Visit a page or profile | 94,591 | 81% | 0.80 (0.61 to 0.94) | 376,120 |
| Follow or subscribe (free) | 78,061 | 66% | 0.51 (0.35 to 0.69) | 173,303 |
| Share, repost or refer | 61,298 | 52% | 0.26 (0.10 to 0.47) | 81,916 |
| Bonus, loyalty or code | 45,912 | 39% | 0.87 (0.33 to 1.22) | 64,921 |
| Email or newsletter signup | 40,733 | 35% | 0.84 (0.70 to 1.01) | 49,688 |
| Join a community | 23,242 | 20% | 0.49 (0.32 to 0.72) | 32,383 |
| Custom action (other) | 23,057 | 20% | 0.51 (0.26 to 0.81) | 52,841 |
| Post or create content | 21,785 | 19% | 0.31 (0.15 to 0.44) | 26,338 |
| Engage with a post | 19,841 | 17% | 0.54 (0.29 to 0.80) | 36,525 |
| Answer a question or poll | 19,474 | 17% | 0.76 (0.49 to 1.00) | 31,477 |
| Connect an account to enter | 15,382 | 13% | 0.55 (0.39 to 0.74) | 24,194 |
| Paid subscription | 7,529 | 6% | 0.11 (0.03 to 0.36) | 8,413 |
| Download or play | 4,082 | 4% | 0.37 (0.23 to 0.58) | 4,392 |
| Imported or offline entries | 1,190 | 1% | 0.08 (0.01 to 0.64) | 1,390 |

Methods per campaign: median 7, IQR 4 to 11, 90th percentile 16 (n=117,348). uptake = entries recorded on the method divided by the campaign's valid contestants, capped at 5 (repeatable methods can exceed 1). Family names are generic, and platform types were mapped to them by hand.
<!-- /generated -->

## Reading the table

- Visiting a page or profile is in four out of five campaigns and most Entrants do it. It is cheap for the Entrant and teaches little about them.
- Email signup, when offered, is completed by almost everyone who enters. It is the highest-completing asset-producing action in the data.
- Free follows are the most common social action and are completed by about half of Entrants. Community joins and content posting see lower completion.
- Sharing and referring is offered in more than half of campaigns and records about 20 entries for every 100 Entrants, where each entry is a referred person times the entry worth. In the top tenth of campaigns the figure reaches 65 per 100. That is the only action whose entries are new people, so weight it and name the reward.
- Paid subscriptions and imported entries have very low completion. Paid actions only work when the audience already intended to pay.

## Completions by action, required versus optional

A completions cut of the dataset: `entry_count` is the number of Entrants who completed the action, not a worth-weighted total, so this needs no division by worth. Scope: campaigns with 100 or more Entrants, every group at least five businesses. Source: `analysis/output/field_cuts.json`, actions_completions. Wallet-address actions are excluded, they run mostly in crypto campaigns, which this skill's figures leave out.

<!-- table -->
| Action | Campaigns | Businesses | Share who completed it | When required | When optional | How often required |
|---|---|---|---|---|---|---|
| Custom Actions | 138,883 | 8,753 | 82 | 101 | 72 | 23% |
| X Follows | 61,231 | 7,475 | 69 | 103 | 56 | 36% |
| Instagram Profile Visits | 30,371 | 4,785 | 79 | 94 | 77 | 11% |
| Viral Shares | 29,316 | 6,538 | 31 | 100 | 22 | 17% |
| X Reposts | 27,707 | 5,276 | 69 | 100 | 49 | 40% |
| YouTube Channel Visits | 21,661 | 4,205 | 83 | 98 | 81 | 14% |
| Facebook visits | 21,503 | 3,793 | 77 | 92 | 75 | 8% |
| Telegram Channel Members | 20,971 | 2,843 | 118 | 124 | 113 | 55% |
| Email Subscriptions | 18,113 | 3,430 | 90 | 102 | 76 | 41% |
| Chat Members | 17,658 | 3,670 | 53 | 89 | 43 | 36% |
| Twitch Follows | 9,172 | 1,237 | 55 | 75 | 52 | 12% |
| X Posts | 7,117 | 1,820 | 42 | 100 | 35 | 23% |
| TikTok Follows | 7,059 | 1,503 | 34 | 58 | 33 | 8% |
| Secret Code | 6,647 | 1,246 | 26 | 94 | 25 | 4% |
| Instagram Follows | 4,747 | 1,077 | 49 | 77 | 47 | 11% |
| TikTok Video Views | 3,233 | 1,039 | 48 | 67 | 47 | 6% |
| App Downloads | 3,023 | 724 | 55 | 115 | 43 | 24% |
| Twitch Subscribers | 2,604 | 342 | 5 | 99 | 5 | 1% |
| Facebook Entries | 2,349 | 680 | 49 | 72 | 47 | 12% |
| Instagram Post Views | 2,308 | 753 | 63 | 87 | 60 | 8% |
| Pinterest Visits | 2,148 | 467 | 63 | 68 | 62 | 2% |
| X Hashtag Posts | 1,880 | 920 | 71 | 95 | 56 | 34% |
| Reddit Visits | 1,702 | 467 | 74 | 95 | 72 | 10% |
| Facebook Likes | 1,597 | 546 | 37 | 55 | 36 | 6% |
| Media Submits | 1,359 | 531 | 7 | 51 | 5 | 16% |
| Podcast Subscriptions | 1,297 | 229 | 29 | 94 | 29 | 3% |
| LinkedIn Follow | 1,275 | 380 | 30 | 51 | 29 | 6% |
| YouTube Entries | 1,265 | 276 | 73 | 100 | 62 | 11% |
| Facebook Post Views | 1,244 | 480 | 63 | 82 | 60 | 10% |
| Submit URL | 1,253 | 463 | 32 | 78 | 23 | 30% |
| Spotify follows | 1,183 | 271 | 28 | 90 | 27 | 6% |
| Instagram Entries | 1,065 | 414 | 47 | 61 | 45 | 10% |
<!-- /table -->

Email Subscriptions is completed by almost everyone who enters, more so when required.

| Context | Completion |
|---|---|
| Overall | 90 per 100 Entrants |
| Required | 102 per 100 |
| Optional | 76 per 100 |

Businesses make it required about 41 times in 100 that they offer it.

Visiting a profile still beats following it on the same network: Instagram Profile Visits completes at about 79 per 100 Entrants against about 49 for Instagram Follows, roughly 60% higher, the same gap the family table above shows between visiting and following in general. [Each figure rests on well over 1,000 campaigns and 1,000 businesses.]

A follow required completes far more often than the same follow left optional, across every network tested.

| Action | Required | Optional |
|---|---|---|
| TikTok Follows | 58 per 100 | 33 per 100 |
| X Follows | 103 per 100 | 56 per 100 |
| Instagram Follows | 77 per 100 | 47 per 100 |

TikTok Follows is made required for about 8 of every 100 campaigns that offer it.

## Entry worth

Worth changes what an Entrant is credited, not whether they complete the action, and its effect differs by action. Worth is a lever for sharing, not for the other families: the campaign's entries per Entrant rise with it, while Email Subscriptions, follows and Custom Actions are flat or fall as worth rises. Worth stays advice, never a mandated value.

| Worth | Viral Share completion |
|---|---|
| 1 | 16 per 100 Entrants |
| 2-4 | 18 per 100 |
| 5-9 | 21 per 100 |
| 10+ | 34 per 100 |

| Action | Worth 1 | Worth 10+ |
|---|---|---|
| Email Subscriptions | 77 per 100 | 77 per 100, flat |
| Custom Actions | 82 per 100 | 62 per 100 |

Typical settings: share worth typically sits at 5, with the top quarter of campaigns setting it at 10 or higher, email typically at 1, follows typically at 2. [Viral Share bands: 6,901 to 9,184 campaigns depending on the band. From `worth_bands_by_action` and `worth_distribution_by_action`.]

## Action settings from the config

Share who completed it by settings read from the action config, campaigns with 100 or more Entrants, every group covers at least 30 campaigns and 10 businesses. Source: `analysis/output/field_cuts.json`, config_cuts.

**Share text.** Medium-length copy completes about twice as often as long copy.

| Share text trait | Completion |
|---|---|
| 60-140 characters | 26 per 100 (53,617 campaigns, 9,335 businesses) |
| Over 140 characters | 14 per 100 (14,664 campaigns, 2,731 businesses) |
| Plain, no link or hashtag | 22 per 100 (66,155 campaigns, 11,243 businesses) |
| With hashtag | 22 per 100 (665 campaigns, 175 businesses) |
| With link | 44 per 100 (4,753 campaigns, 552 businesses) |

Share text carrying a link completes twice as often as plain text, and a hashtag makes no difference either way. Read the link row with care: 40% of those actions were mandatory against 15% of the plain ones, so the gap is partly who was made to complete them and not the link itself.

**Actions required.** Completion holds steady through a few steps, then falls hard from eight steps on.

| Steps required | Completion |
|---|---|
| 1 | 84 per 100 (372,987 actions, 19,088 businesses) |
| 2-4 | 99-109 per 100 (2,709 to 4,517 actions, 871 to 1,391 businesses each) |
| 5-7 | 66-81 per 100 (3,726 to 5,900 actions, 1,398 to 1,938 businesses each) |
| 8 | 31 per 100 (2,429 actions, 738 businesses) |
| 11 | 23 per 100 (682 actions, 270 businesses) |

**Paid actions.** A paid step moves completion in different directions depending on the action.

| Action | Free | Paid |
|---|---|---|
| Twitch Subscribers | 4 per 100 (2,226 campaigns, 250 businesses) | 11 per 100 (378 campaigns, 118 businesses) |
| Custom Actions | 82 per 100 (137,494 campaigns, 8,713 businesses) | 44 per 100 (1,389 campaigns, 541 businesses) |

## SMS and messaging opt-in (advice, no dataset support)

A phone number or a messaging opt-in (SMS, WhatsApp, Messenger, a Telegram or Discord bot subscription used to message Entrants directly) is an owned channel in the same family as an email signup: the Entrant hands over a way to reach them that no platform can take away. The dataset carries no SMS action type and no bot-subscription action type, so there is no benchmark on this page for how many Entrants would complete a messaging opt-in, cost per number or anything else. That gap is specific to the messaging opt-in itself. Joining a Telegram channel or a Discord server is a different action and is measured, in the family table above and in the table below. Say plainly that a messaging opt-in has no benchmark when recommending one, and never borrow the email row or the channel-join row as a stand-in.

What practice suggests, with no numbers attached:

- Treat it as a second asset alongside email. A number costs more to message and carries a harder consent regime.
- Ask for it only where the business already sends messages and has a sender identity registered where the region requires one.
- Keep it optional unless the messaging channel is the objective. It asks more of an Entrant than an email field does.
- Collect the marketing consent at the same moment and in its own wording. A number given to enter a giveaway is not a number given for promotional messages.
- Where the region requires double opt-in, the confirmation message goes out at capture, and only confirmed numbers reach the list.

## Use by campaign size

Share of campaigns of each size that offered at least one action from the family.

<!-- generated:entry_by_band -->
| Action family | 100-250 | 250-500 | 500-1k | 1k-2.5k | 2.5k-10k | 10k+ |
|---|---|---|---|---|---|---|
| Visit a page or profile | 79% | 82% | 81% | 80% | 83% | 82% |
| Follow or subscribe (free) | 68% | 68% | 67% | 64% | 64% | 66% |
| Share, repost or refer | 45% | 53% | 56% | 57% | 57% | 52% |
| Email or newsletter signup | 25% | 31% | 38% | 43% | 46% | 40% |
| Bonus, loyalty or code | 40% | 37% | 38% | 39% | 42% | 44% |
| Join a community | 18% | 19% | 22% | 21% | 20% | 17% |
| Answer a question or poll | 17% | 17% | 17% | 16% | 16% | 16% |
| Post or create content | 21% | 20% | 18% | 16% | 15% | 18% |
| Connect an account to enter | 15% | 13% | 13% | 12% | 10% | 7% |
| Download or play | 3% | 3% | 4% | 4% | 5% | 5% |
| Methods per campaign (median) | 6 | 7 | 7 | 7 | 7 | 7 |
<!-- /generated -->

The mix barely changes with size. Seven methods is typical at every size. Bigger campaigns are slightly less likely to ask for shares and slightly more likely to ask for follows and page visits.

## How much the business's own community or channel size mattered

The business's own server, channel, page or app against how much its join, follow, visit or download action was completed. Completion here is entries on the action divided by Entrants, the same measure as the family table above, not worth-normalised. Every group listed has at least five businesses, the dataset's own floor. A note flags any group under 30 campaigns or 10 businesses, this skill's own floor for calling a figure more than advice. Source: `analysis/output/industries.json`.

Discord, the business's own server (by_discord_server_size, action is a Discord server join):

| Server size | Campaigns | Businesses | Share who completed it | Email offered |
|---|---|---|---|---|
| 1k to 10k members | 105 | 52 | 67 | 11% |
| 10k to 100k members | 145 | 38 | 64 | 9% |

Telegram, the business's own channel (by_telegram_size, action is a channel join plus a channel post view):

| Channel size | Campaigns | Businesses | Share who completed it | Email offered |
|---|---|---|---|---|
| Under 1k | 4,206 | 1,198 | 129 | 4% |
| 1k to 10k | 5,788 | 1,041 | 119 | 6% |
| 10k to 100k | 6,626 | 470 | 119 | 1% |
| 100k+ | 2,006 | 95 | 103 | 0% |

Steam groups (by_steam_group_size): no group size cleared the five-business floor for reporting. No figure to report.

Patreon, the business's own page (by_patreon_size, action is a Patreon page visit):

| Patron count | Campaigns | Businesses | Share who completed it | Email offered |
|---|---|---|---|---|
| 100 to 999 | 43 | 21 | 65 | 14% |
| 1k+ | 37 | 21 | 63 | 32% |

Bluesky, the business's own account (by_bluesky_followers, action is a Bluesky follow):

| Follower count | Campaigns | Businesses | Share who completed it | Email offered |
|---|---|---|---|---|
| Under 1k | 93 | 58 | 18 | 29% |
| 1k to 10k | 206 | 71 | 25 | 34% |
| 10k to 100k | 50 | 15 | 30 | 24% |

Kick, the business's own channel (by_kick_followers, action is a Kick follow):

| Follower count | Campaigns | Businesses | Share who completed it | Email offered |
|---|---|---|---|---|
| 1k to 10k | 123 | 20 | 38 | 15% |
| 10k to 100k | 101 | 13 | 51 | 20% |

App downloads by install count (by_app_installs, action is an app download):

| Installs | Campaigns | Businesses | Share who completed it | Email offered |
|---|---|---|---|---|
| Under 100k | 468 | 179 | 41 | 61% |
| 100k to 1m | 411 | 110 | 42 | 50% |
| 1m to 10m | 440 | 69 | 40 | 21% |
| 10m+ | 499 | 32 | 77 | 1% |

App downloads by genre (by_app_genre):

| Genre | Campaigns | Businesses | Share who completed it | Email offered |
|---|---|---|---|---|
| Finance | 554 | 79 | 79 | 3% |
| Shopping | 542 | 69 | 36 | 48% |
| Entertainment | 129 | 31 | 47 | 65% |
| Sports | 75 | 27 | 39 | 56% |
| Tools | 73 | 17 | 103 | 10% |
| Health and fitness | 49 | 17 | 66 | 16% |
| Travel and local | 50 | 16 | 24 | 58% |
| Role playing | 33 | 15 | 73 | 3% |
| Social | 30 | 17 | 79 | 27% |
| News and magazines | 38 | 7 | 53 | 92% |
| Action | 36 | 5 | 77 | 14% |

News and magazines runs 7 businesses and Action runs 5. Both advice only.

Apps under 10m installs offer email in half or more of campaigns. Above 10m installs, offered email drops to 1% and completion on the download action itself is highest, about 77 of every 100, likely large apps that no longer need the asset a smaller app would chase.

YouTube channel size (by_youtube_subscribers), methods and referrals:

| Subscribers | Campaigns | Businesses | Methods | Referral entries % of Entrants | Email completed % of Entrants |
|---|---|---|---|---|---|
| Under 1k | 180 | 23 | 6 | 38 | no email offered |
| 1k to 10k | 90 | 36 | 3 | 85 | 60 |
| 10k to 100k | 247 | 91 | 6 | 17 | 77 |
| 100k to 1m | 1,173 | 187 | 4 | 7 | 87 |
| 1m+ | 643 | 80 | 4 | 8 | 51 |

Small channels lean on referrals: channels with 1,000 to 10,000 subscribers record the most referral entries of any group and run the fewest methods, per the table above. YouTube gaming channels (by_youtube_gaming) show the same shape against other YouTube channels:

| Channel type | Methods | Referral entries per 100 Entrants |
|---|---|---|
| Gaming | 5 (964 campaigns, 220 businesses) | 6 |
| Other | 4 (1,307 campaigns, 184 businesses) | 20 |

### Does a bigger channel mean a bigger campaign? (extracted)

Every figure in this subsection comes from businesses whose action config named a public channel URL, a self-selected minority of the dataset. Don't generalize it to businesses without a channel-join or channel-follow action.

Channel size barely predicts campaign size, in either direction. A big channel does not guarantee a big campaign, and on this same evidence a small channel does not cap one either. If the business's channel is small, that is not the constraint to plan around.

| Channel type | Correlation with campaign Entrants |
|---|---|
| YouTube subscribers | 15.6% (9,267 campaigns, 1,518 businesses) |
| Telegram channel size | 1.9% (24,612 campaigns, 4,249 businesses) |
| Discord server size | 0.1% (728 campaigns, 196 businesses) |

[Extracted from `analysis/output/industries.json`, `channel_size_predicts_campaign_size`.]

The raw YouTube conversion gap by subscriber count disappears once you compare like-for-like within an industry, and it reverses inside gaming and esports specifically: campaigns there convert at 40.9% with a 100,000-to-1m subscriber channel against 33.6% with a 1m+ channel. [376 and 122 campaigns.] Don't cite the version of this gap that doesn't compare like with like. [Extracted from `analysis/output/industries.json`, `channel_size_within_industry`.]

Telegram's size gap holds up better. It survives a like-for-like check inside finance and crypto specifically, one of the few industries with enough channel-size volume to test. [Conversion runs 32.3% under 1,000 channel members up to 39.1% at 100,000+, 2,008 campaigns/967 businesses under 1,000, 797/64 at 100,000+.] This is the finance_crypto industry label, an exception to this skill's usual crypto exclusion made here only because the question is channel size, not entry mechanics. It also holds within two of the three Entrant-size groups tested: campaigns of 1,000-2,500 and 2,500-10,000 Entrants rise with channel size at every step, campaigns of 10,000 or more do not. [Extracted from `analysis/output/industries.json`, `channel_size_within_industry` and `channel_size_within_contestant_band`.]

Channel age separates channels of the same size. Among YouTube channels with 100,000 to 1m subscribers, ones created before 2017 convert notably higher than ones created 2017 or later. [48.8% against 34.6%, 980 campaigns/124 businesses pre-2017, 167/56 later.] The pattern reverses for the smallest channels, where the newer ones convert higher. [Extracted from `analysis/output/industries.json`, `youtube_subscribers_vs_channel_age`.]

Bigger channels pull less direct traffic to the campaign. A bigger audience relies more on the platform surfacing the campaign and less on people going straight to it.

| Channel | Smaller size | Larger size |
|---|---|---|
| YouTube (10k-100k vs 1m+ subscribers) | 26.7% direct (247 campaigns) | 13.4% direct (643 campaigns) |
| Telegram (1k-10k vs 100k+ members) | 69.2% direct (3,229 campaigns) | 52.0% direct (1,221 campaigns) |

[Extracted from `analysis/output/industries.json`, `channel_size_vs_direct_traffic`.]

## Limits

- The completion figures count completions the platform recorded. They cannot show whether a follow stayed or an email address was real.
- Families group actions across platforms whose rules differ. A follow on one network is verifiable, on another it is on trust.
- Every campaign passed the 100-Entrant floor, so the table describes campaigns that reached an audience and nothing about what a mix does for a campaign that has not.

## Method count, sharing and email against Entrants and conversion

Impressions in the dataset are unique per day, so a visitor who returns counts again each day. Repeatable actions (daily bonus, loyalty, timed bonus) and long runs raise Impressions per Entrant and lower Entrants per Impression without any change in who entered. The campaigns we can compare fairly here remove any campaign with a repeatable action and any run over 14 days. Typical values, the campaigns we can compare fairly, descriptive only. A vertical is a regex proxy on business, campaign and Prize names.

<!-- generated:cmp_methods -->
| Entry methods, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| 1 to 3 | 10,841 | 443 | 1.29 | 44% | 2.3 | 2 |
| 4 to 6 | 12,430 | 401 (-9%) | 3.43 (+166%) | 35% (-21%) | 2.9 | 5 |
| 7 to 10 | 9,744 | 463 (+5%) | 5.26 (+307%) | 29% (-35%) | 3.5 | 8 |
| 11 or more | 6,795 | 519 (+17%) | 9.26 (+617%) | 31% (-29%) | 3.2 | 14 |
<!-- /generated -->

Entrants per 100 Impressions falls with every extra group of methods and Entrants fall about a quarter at 11 or more, in the campaigns we can compare fairly and in every vertical with enough campaigns. Actions per Entrant rise because there are more things to do. More methods means more Actions per Entrant and fewer people.

<!-- generated:cmp_share -->
| Share action, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| no share action | 28,415 | 406 | 3.36 | 37% | 2.7 | 5 |
| offers a share action | 11,395 | 544 (+34%) | 4.90 (+46%) | 29% (-23%) | 3.5 | 8 |
<!-- /generated -->

<!-- generated:cmp_email -->
| Email signup, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| no email signup | 28,961 | 423 | 3.71 | 37% | 2.7 | 5 |
| offers email signup | 10,849 | 546 (+29%) | 3.65 (-2%) | 30% (-17%) | 3.3 | 6 |
<!-- /generated -->

Entries on the share action are referral entries: the platform's reporting terms define entries as actions completed times entry worth, and the Viral Share report counts a successful share as a user who entered as a direct result of it. Share completion therefore measures referred Entrants times the entry worth the business set, and the entry worth is unknown in the dataset. Campaigns offering a share action had fewer Entrants and lower conversion in the campaigns we can compare fairly, which describes the businesses who chose it. It cannot show whether the referrals added people who would otherwise have stayed away. An email signup cost about a fifth of conversion for a small gain in Entrants. Both are prices worth paying only when the asset is the objective.

A click on that share link converts differently than the click itself suggests: a shared link converts at about two-thirds the rate of any other visit, excluding crypto businesses [14.9% against 22.5%].

| Cut | Share-click conversion |
|---|---|
| Excluding finance and crypto | 14.9% (against 22.5% for ordinary Impressions on the same campaigns, 47,097 campaigns, 7,603 businesses) |
| Pooled with crypto (referral farms included) | 20.0% (71,191 campaigns, 11,563 businesses) |
| Worth 1-9, pooled | 16.7%-18.1% |
| Worth 10+, pooled | 26.2% (27,991 campaigns, 4,196 businesses), with more clicks per Entrant too (1.61 against 1.27 at worth 1) |

[Source: analysis/output/field_cuts.json (viral_click_conversion, viral_click_conversion_excluding_crypto, viral_click_conversion_by_worth).]
</content>
