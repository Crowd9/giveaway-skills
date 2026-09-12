# Action families

Extracted from the campaigns we can compare fairly (crypto, ambiguous and purchase-only campaigns removed). Platform-specific action types were mapped by hand to generic families so the advice works on any platform. [Completion is entries recorded on a method divided by the campaign's valid Entrants, capped at 5, then the typical value across campaigns that offered the family, converted here to a count per 100 Entrants with the raw figure alongside for tracing. Entries are actions completed times the entry worth the business set, and entry worth is unknown in the dataset, so a figure near 100 per 100 means most Entrants did it only where the worth was 1, repeatable actions and referrals can pass 100. The bracketed range in the table below is the middle half of campaigns, between the lower and upper quarter, so its top marks the level three campaigns in four sit below.]

<!-- generated:entry_families -->
| Action family | Campaigns using it | Share of campaigns | Uptake median (IQR) | n with uptake |
|---|---|---|---|---|
| Visit a page or profile | 94,082 | 81% | 0.80 (0.61 to 0.94) | 374,795 |
| Follow or subscribe (free) | 77,459 | 66% | 0.51 (0.35 to 0.69) | 172,265 |
| Share, repost or refer | 60,707 | 52% | 0.26 (0.10 to 0.46) | 80,835 |
| Bonus, loyalty or code | 45,593 | 39% | 0.88 (0.33 to 1.23) | 64,343 |
| Email or newsletter signup | 40,537 | 35% | 0.84 (0.70 to 1.01) | 49,466 |
| Custom action (other) | 22,828 | 20% | 0.50 (0.26 to 0.80) | 52,187 |
| Join a community | 22,804 | 20% | 0.49 (0.32 to 0.71) | 31,662 |
| Post or create content | 21,573 | 18% | 0.31 (0.14 to 0.44) | 26,035 |
| Engage with a post | 19,750 | 17% | 0.54 (0.29 to 0.80) | 36,381 |
| Answer a question or poll | 19,254 | 16% | 0.76 (0.49 to 1.00) | 31,180 |
| Connect an account to enter | 15,306 | 13% | 0.55 (0.39 to 0.74) | 24,076 |
| Paid subscription | 7,517 | 6% | 0.11 (0.03 to 0.36) | 8,404 |
| Download or play | 4,048 | 4% | 0.37 (0.23 to 0.58) | 4,347 |
| Imported or offline entries | 1,186 | 1% | 0.08 (0.01 to 0.64) | 1,387 |

Methods per campaign: median 7, IQR 4 to 11, 90th percentile 16 (n=116,499). uptake = entries recorded on the method divided by the campaign's valid contestants, capped at 5 (repeatable methods can exceed 1). Family names are generic, and platform types were mapped to them by hand.
<!-- /generated -->

## Reading the table

- Visiting a page or profile is in four out of five campaigns and most Entrants do it. It is cheap for the Entrant and teaches little about them.
- Email signup, when offered, is completed by almost everyone who enters. It is the highest-completing asset-producing action in the data.
- Free follows are the most common social action and are completed by about half of Entrants. Community joins and content posting see lower completion.
- Sharing and referring is offered in more than half of campaigns and records about 26 entries for every 100 Entrants, where each entry is a referred person times the entry worth. In the top tenth of campaigns the figure reaches 66 per 100. [`analysis/output/benchmarks.json`, `ordinary_benchmark` entry_methods families.] That is the only action whose entries are new people, so weight it and name the reward.
- Paid subscriptions and imported entries have very low completion. Paid actions only work when the audience already intended to pay.

## Completions by action, required versus optional

A completions cut of the dataset: `entry_count` is the number of Entrants who completed the action, not a worth-weighted total, so this needs no division by worth. Scope: the ordinary population, the same 116,499 campaigns as every other cut in this file, which is campaigns of 100 or more Entrants once crypto, ambiguous and purchase-only campaigns are removed, every group at least five businesses. This is the same cut as the family table above, so the two tables can be read together. Source: `analysis/output/field_cuts.json`, actions_completions. Wallet-address actions are excluded, they run mostly in crypto campaigns, which this skill's figures leave out.

<!-- table -->
| Action | Campaigns | Businesses | Share who completed it | When required | When optional | How often required |
|---|---|---|---|---|---|---|
| Custom Actions | 285,843 | 13,428 | 77 | 99 | 73 | 13% |
| X Follows | 92,096 | 10,037 | 54 | 79 | 51 | 12% |
| Instagram Profile Visits | 81,803 | 9,807 | 82 | 95 | 80 | 9% |
| Facebook visits | 59,301 | 7,415 | 82 | 93 | 81 | 7% |
| YouTube Channel Visits | 53,783 | 8,874 | 86 | 99 | 84 | 13% |
| Email Subscriptions | 46,858 | 5,708 | 85 | 102 | 78 | 33% |
| Viral Shares | 42,807 | 6,922 | 11 | 20 | 11 | 6% |
| X Reposts | 33,715 | 5,647 | 44 | 71 | 41 | 13% |
| Twitch Follows | 29,618 | 4,323 | 68 | 92 | 62 | 20% |
| Chat Members | 22,329 | 3,249 | 44 | 80 | 42 | 11% |
| TikTok Follows | 17,149 | 2,991 | 35 | 56 | 34 | 7% |
| X Posts | 16,028 | 2,089 | 34 | 43 | 33 | 9% |
| Secret Code | 13,648 | 2,351 | 27 | 84 | 27 | 4% |
| Instagram Follows | 11,970 | 2,596 | 52 | 80 | 50 | 11% |
| Instagram Post Views | 9,092 | 1,870 | 74 | 89 | 73 | 8% |
| Twitch Subscribers | 8,404 | 1,175 | 11 | 22 | 11 | 2% |
| Pinterest Visits | 8,365 | 929 | 66 | 71 | 66 | 4% |
| Facebook Entries | 8,186 | 1,629 | 54 | 77 | 51 | 14% |
| TikTok Visits | 8,112 | 1,846 | 53 | 64 | 52 | 7% |
| Telegram Channel Members | 4,874 | 835 | 85 | 93 | 77 | 35% |
| Facebook Post Views | 4,687 | 1,117 | 71 | 89 | 70 | 7% |
| Facebook Likes | 4,631 | 1,253 | 39 | 54 | 38 | 6% |
| Podcast Subscriptions | 4,234 | 479 | 34 | 59 | 34 | 1% |
| Instagram Entries | 3,928 | 1,198 | 53 | 72 | 51 | 10% |
| App Downloads | 3,607 | 764 | 41 | 81 | 38 | 10% |
| YouTube Entries | 3,584 | 944 | 81 | 99 | 74 | 17% |
| Spotify follows | 2,949 | 554 | 32 | 99 | 31 | 7% |
| Reddit Visits | 2,884 | 461 | 77 | 94 | 76 | 5% |
| Media Submits | 2,758 | 901 | 10 | 100 | 7 | 17% |
| Submit URL | 2,017 | 605 | 19 | 66 | 17 | 14% |
| LinkedIn Follow | 1,782 | 382 | 28 | 51 | 28 | 4% |
| X Hashtag Posts | 1,518 | 535 | 36 | 77 | 34 | 9% |
<!-- /table -->

Email Subscriptions is completed by almost everyone who enters, more so when required.

| Context | Completion |
|---|---|
| Overall | 85 per 100 Entrants |
| Required | 102 per 100 |
| Optional | 78 per 100 |

Businesses make it required about 33 times in 100 that they offer it.

Visiting a profile still beats following it on the same network: Instagram Profile Visits completes at about 82 per 100 Entrants against about 52 for Instagram Follows, roughly 60% higher, the same gap the family table above shows between visiting and following in general. [Each figure rests on well over 1,000 campaigns and 1,000 businesses.]

A follow required completes far more often than the same follow left optional, across every network tested.

| Action | Required | Optional |
|---|---|---|
| TikTok Follows | 56 per 100 | 34 per 100 |
| X Follows | 79 per 100 | 51 per 100 |
| Instagram Follows | 80 per 100 | 50 per 100 |

TikTok Follows is made required for about 7 of every 100 campaigns that offer it.

## Entry worth

Worth changes what an Entrant is credited, not whether they complete the action, and its effect differs by action. Worth is a lever for sharing, not for the other families: Viral Share completion climbs with worth and then flattens above 5, the campaign's entries per Entrant rise with it, while Email Subscriptions, follows and Custom Actions are flat or fall as worth rises. Worth stays advice, never a mandated value.

| Worth | Viral Share completion |
|---|---|
| 1 | 9 per 100 Entrants |
| 2 | 11 per 100 |
| 3-4 | 12 per 100 |
| 5-9 | 13 per 100 |
| 10+ | 13 per 100 |

| Action | Worth 1 | Worth 10+ |
|---|---|---|
| Email Subscriptions | 78 per 100 | 79 per 100, flat |
| Custom Actions | 82 per 100 | 63 per 100 |

Typical settings: share worth typically sits at 4, with the top quarter of campaigns setting it at 10 or higher, email typically at 1, follows typically at 1. [Viral Share bands: 3,607 to 12,774 campaigns depending on the band. From `worth_bands_by_action` and `worth_distribution_by_action`.]

## Action settings from the config

Share who completed it by settings read from the action config, the ordinary population, the same 116,499 campaigns as the tables above, every group covering at least 30 campaigns and 10 businesses. Source: `analysis/output/field_cuts.json`, config_cuts.

**Share text.** Medium-length copy completes about a third more often than long copy.

| Share text trait | Completion |
|---|---|
| 60-140 characters | 12 per 100 (30,789 campaigns, 5,447 businesses) |
| Over 140 characters | 9 per 100 (10,075 campaigns, 1,867 businesses) |
| Plain, no link or hashtag | 11 per 100 (40,545 campaigns, 6,729 businesses) |
| With hashtag | 10 per 100 (385 campaigns, 81 businesses) |
| With link | 11 per 100 (1,877 campaigns, 336 businesses) |

Neither a link nor a hashtag in the share text changes completion on this population. The link row runs at 11 per 100 against 11 for plain text, and 9% of link actions were mandatory against 6% of plain ones, too close together to read anything into.

**Steps inside one Action.** Completion holds through the first few steps, slips through five to seven, then falls hard from eight steps on. This cut counts the steps configured inside a single Entry Method, and its denominator is Actions, not campaigns. It says nothing about how many Entry Methods a campaign should carry, which is the `cmp_methods` table further up this file. A measured answer quoted this row to judge a ten-method entry list and built its whole recommendation on a figure about something else.

| Steps required | Completion |
|---|---|
| 1 | 77 per 100 (277,080 actions, 12,860 businesses) |
| 2-4 | 67-102 per 100 (1,377 to 2,020 actions, 501 to 817 businesses each) |
| 5-7 | 44-63 per 100 (1,900 to 3,278 actions, 709 to 1,170 businesses each) |
| 8 | 27 per 100 (1,691 actions, 440 businesses) |
| 11 | 17 per 100 (485 actions, 182 businesses) |

**Paid actions.** A paid step costs a Custom Action most of its completion and leaves a Twitch subscription where it was.

| Action | Free | Paid |
|---|---|---|
| Twitch Subscribers | 11 per 100 (6,700 campaigns, 847 businesses) | 11 per 100 (1,704 campaigns, 487 businesses) |
| Custom Actions | 77 per 100 (283,662 campaigns, 13,368 businesses) | 19 per 100 (2,181 campaigns, 633 businesses) |

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
| Follow or subscribe (free) | 68% | 68% | 67% | 64% | 64% | 65% |
| Share, repost or refer | 44% | 53% | 56% | 56% | 57% | 52% |
| Email or newsletter signup | 25% | 31% | 38% | 44% | 46% | 41% |
| Bonus, loyalty or code | 40% | 37% | 38% | 39% | 42% | 43% |
| Join a community | 18% | 19% | 21% | 21% | 20% | 17% |
| Answer a question or poll | 17% | 17% | 17% | 16% | 16% | 16% |
| Post or create content | 21% | 20% | 18% | 16% | 14% | 17% |
| Connect an account to enter | 15% | 13% | 13% | 12% | 10% | 7% |
| Download or play | 3% | 3% | 4% | 4% | 5% | 5% |
| Methods per campaign (median) | 6 | 7 | 7 | 7 | 7 | 7 |
<!-- /generated -->

Most families barely change with size. Seven methods is typical everywhere except the 100 to 250 band, which runs six. Email is the exception, offered in a quarter of the smallest campaigns and in around four in ten from 1,000 Entrants up. Bigger campaigns are also a little more likely to ask for shares and page visits, and a little less likely to ask for a follow or an account connection.

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

Apps under 1m installs offer email in half or more of campaigns, and the 1m to 10m band drops to a fifth. Above 10m installs, offered email drops to 1% and completion on the download action itself is highest, about 77 of every 100, likely large apps that no longer need the asset a smaller app would chase.

YouTube channel size (by_youtube_subscribers), methods and referrals:

| Subscribers | Campaigns | Businesses | Methods | Referral entries % of Entrants | Email completed % of Entrants |
|---|---|---|---|---|---|
| Under 1k | 180 | 23 | 6 | 38 | no email offered |
| 1k to 10k | 90 | 36 | 3 | 85 | 60 |
| 10k to 100k | 247 | 91 | 6 | 17 | 77 |
| 100k to 1m | 1,173 | 187 | 4 | 7 | 87 |
| 1m+ | 643 | 80 | 4 | 8 | 51 |

Small channels lean on referrals: channels with 1,000 to 10,000 subscribers record the most referral entries of any group and run the fewest methods, per the table above. YouTube gaming channels (by_youtube_gaming) run the opposite shape against other YouTube channels, more methods and far fewer referral entries:

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
| 1 to 3 | 10,802 | 443 | 1.27 | 44% | 2.3 | 2 |
| 4 to 6 | 12,295 | 403 (-9%) | 3.42 (+169%) | 35% (-21%) | 2.9 | 5 |
| 7 to 10 | 9,603 | 460 (+4%) | 5.25 (+312%) | 29% (-35%) | 3.5 | 8 |
| 11 or more | 6,762 | 518 (+17%) | 9.27 (+628%) | 31% (-29%) | 3.2 | 14 |
<!-- /generated -->

Entrants per 100 Impressions falls from 44 at one to three methods to 29 at seven to ten, then holds at 31 for the longest lists. Entrant counts do not follow it down, and they do not rise in a line either. The count dips before it climbs: 443 at one to three methods, 403 at four to six, 460 at seven to ten, 518 at eleven or more. Only the longest lists beat the shortest, by 17%, and a campaign moving from three methods to five sat 9% below where it started. Quote the row the reader is actually in. Actions per Entrant rise with the list, because there are more things to do. So the longest lists in this data converted a smaller share of the Impressions they drew, and still recorded more Entrants and far more Actions. That describes the campaigns businesses chose to run, and says nothing about what adding a method to this campaign would do.

<!-- generated:cmp_share -->
| Share action, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| no share action | 28,200 | 408 | 3.35 | 37% | 2.7 | 5 |
| offers a share action | 11,262 | 543 (+33%) | 4.89 (+46%) | 29% (-23%) | 3.5 | 8 |
<!-- /generated -->

<!-- generated:cmp_email -->
| Email signup, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| no email signup | 28,621 | 423 | 3.68 | 37% | 2.7 | 5 |
| offers email signup | 10,841 | 546 (+29%) | 3.65 (-1%) | 30% (-17%) | 3.3 | 6 |
<!-- /generated -->

Entries on the share action are referral entries: the platform's reporting terms define entries as actions completed times entry worth, and the Viral Share report counts a successful share as a user who entered as a direct result of it. Share completion therefore measures referred Entrants times the entry worth the business set, and the entry worth is unknown in the dataset. Campaigns offering a share action had 33% more Entrants and 23% lower conversion in the campaigns we can compare fairly, which describes the businesses who chose it. It cannot show whether the referrals added people who would otherwise have stayed away. An email signup came with 29% more Entrants and about a sixth less conversion. What both cost in this data is the share of Impressions that converted, and neither came with a smaller crowd, so weigh the conversion price against the asset the action collects.

A click on that share link converts differently than the click itself suggests: a shared link converts at about two-thirds the rate of any other visit [13.9% against 21.8%].

| Cut | Share-click conversion |
|---|---|
| The ordinary population | 13.9% (against 21.8% for ordinary Impressions on the same campaigns, 42,512 campaigns, 6,919 businesses) |
| Worth 1 to 9 | 11.9%-15.1% |
| Worth 10 or more | 15.1% (13,665 campaigns, 2,183 businesses), with more clicks per Entrant too (0.98 against 0.86 at worth 1) |

There is no longer a crypto-pooled figure to set against the excluded one. `viral_click_conversion` and `viral_click_conversion_excluding_crypto` now report the same campaigns, because the ordinary population already drops crypto. Worth 10 or more sits at the top of the worth 1 to 9 range, so worth no longer separates share-click conversion the way it did on the wider population.

[Source: analysis/output/field_cuts.json (viral_click_conversion, viral_click_conversion_excluding_crypto, viral_click_conversion_by_worth).]
</content>
