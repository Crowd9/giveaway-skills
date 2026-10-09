# Mix by objective

Advice unless marked as extracted. Completion throughout this file means recorded completed events (`entry_count`) divided by the campaign's Entrants, without multiplying by Entry worth: about 75 per 100 is three completions for every four Entrants, not three distinct people. Source definition: `analysis/output/field_cuts.json`, `definitions.completions_per_contestant`. This definition is for you. Tell the reader what it changes in their list, such as "Required follows were completed more often, so making them optional trades some follows for a shorter route to entry." Keep ratios out of action descriptions unless their size decides the choice. If quoting one, name the action counted and explain that repeats count too.

## Patterns

| Objective | Required action | Supporting actions | Reach action | Leave out |
|---|---|---|---|---|
| Email list | Entry form with an email address for giveaway contact | Optional email marketing opt-in, visit a key page, follow the main channel | Refer a friend, weighted high | Content tasks, account connections |
| Phone or messaging list | Entry form with a giveaway contact route (advice, no dataset support) | Optional SMS or messaging marketing opt-in, visit a key page | Refer a friend | A second messaging channel in the same campaign |
| Followers on one channel | Follow on that channel | Engage with a pinned post, visit profile | Share the giveaway | Follows on channels the business ignores |
| Community members | Join the community | Answer a question that seeds a first post, follow main channel | Refer a friend | Anything that needs an app install |
| Content (UGC) | Submit a photo, video or review | Follow, visit a product page | Share | More than one content task |
| App installs | Download or play | Entry form as fallback, optional email marketing opt-in, follow | Share | Actions on channels with no mobile path |
| Reach or launch awareness | Visit the launch page | Follow, engage with the launch post | Share, weighted highest | Long questions, content tasks |
| Local foot traffic | In-store code or visit | Follow, tag a local friend | Share to story | Email if the business cannot send to it |
| Qualified leads or demo requests (B2B) | A short qualifying question only a real buyer can answer, paired with an email address for giveaway contact (advice, no dataset support for the pairing) | Optional email marketing opt-in, visit the pricing or product page, follow the company channel | Refer a colleague | Anything that reads as payment for a review or a referral, content tasks, community joins nobody can moderate |

The B2B row is advice, and `qualified-entry.md` holds the full version: who to name as the buyer, gating, the qualifying question, what to require, the follow-up and the scorecard. What the data does hold is 12,728 B2B campaigns from 1,779 businesses, and what those businesses chose: the same typical 7 Entry Methods as B2C, 44 referral entries per 100 Entrants where B2C saw 16, and email offered in 19% of campaigns where B2C offered it in 34% (extracted, the mix by the kind of business running it section below). None of that says whether a lead was qualified, because the dataset ends at the entry and carries no outcome after it. So treat a B2B giveaway as list building whose qualification happens in the question and in the follow-up, and tell the reader that is what they are buying. The usual scorecard of Entrants and Conversion Rate rewards a big crowd, so a buyer campaign needs its own, and `qualified-entry.md` gives one.

A buyer's employer may have rules about being paid for a review, a referral or a public endorsement, and a regulated buyer may have more. Where the user raises that, drop the referral and review actions and put the reach into the question and the page visit, and say why.

## Mixes in campaigns copied from Gleam library templates (extracted)

Campaigns copied from each Gleam library template used different mixes of methods, email and sharing. These aggregates include businesses' subsequent configuration choices. Campaigns copied from Refer A Friend offered sharing most often. Campaigns copied from E-Commerce Giveaway carried the most methods. [Scope: 100 or more Entrants, finance and crypto businesses excluded.]

| Template | Methods | Email offered | Share offered |
|---|---|---|---|
| Email Signup | 4 | 92% | 61% |
| Refer A Friend | 4 | 35% | 92% |
| E-Commerce Giveaway | 9 | 79% | 80% |
| Gleam Sweepstakes | 7 | 58% | 60% |
| Instant Entry | 1 | 7% | 6% |
| YouTube Contest | 6 | 9% | 38% |

Use the observed mixes as context, and weight and add actions against the objective table above.

Source: `analysis/output/templates.json` (`by_template`).

### Every action has a job (advice, from Gleam's campaign team)

Five optional jobs help plan the mix. In the answer, replace these labels with a plain reason tied to the reader's objective, such as collect email signups, grow Instagram followers or bring in referrals. Keep actions only when that reason earns their place. Acquire: email signup, SMS or messaging opt-in, account creation, app install, community join, the actions that create an owned relationship. Grow social: a follow on the one or two networks where the audience already is. Learn: a single-choice or open question that collects something the business can use, such as which flavour, which feature, which destination, never trivia. Engage: a visit, a video, a secret code, a bonus, exposure to the product. Amplify: Viral Share or refer a friend, low completion by nature and the only action that brings new people. Choose only the jobs that support the requested asset and audience. A campaign can use just the acquisition action, with supporting actions added when each earns its place. Judge an amplify action by referrals, never by completion rate.

## Weighting

- As a practical starting point, give the asset-producing action 3 to 5 entries and sharing 5 to 9 entries per referral. Choose the weight according to how much extra draw weight referrals should receive. The observed share click rate (viral share clicks over Impressions) was highest in that band and matched the weight-1 rate at 10 or more. This comparison does not predict what changing the weight would do to a campaign.

| Weight offered | Share click rate |
|---|---|
| 1 | 19 per 100 Impressions |
| 2 to 4 | 21 per 100 |
| 5 to 9 | 23 per 100 |
| 10 or more | 19 per 100 |

[Campaigns/businesses: 13,579/2,729 (weight 1), 8,616/1,866 (2-4), 7,181/1,895 (5-9), 13,755/2,184 (10+). Extracted from `analysis/output/field_cuts.json`, share_clicks.by_share_worth.] This shows businesses who weight sharing in the middle bands see a higher click rate, not that raising the weight on one campaign would raise its clicks, since the businesses who choose a high weight may also run a more shareable campaign.
- One entry for visits and views. Two for follows and joins.
- Daily repeatable actions keep a long campaign alive and inflate the entries recorded per Entrant. Extracted: a typical campaign records 430 entries for every 100 Entrants, and campaigns with more repeatable bonus actions sit well above that.
- If the platform allows, require the chosen entry action before other actions unlock. For email, SMS or messaging lists, use the entry form as that action and keep marketing permission optional and separate. Declining marketing permission leaves the entry and other actions available. Take a proposed subscription condition to the counsel question under Consent and rules before configuring it.
- Campaigns with boosted referral worth recorded more completions in the comparisons below. Follow and join results varied. Businesses chose their own weights, so these comparisons do not show whether raising worth would bring more people or improve completion. As practice, keep Telegram, YouTube and UGC worth at default and review whether the action fits the audience before changing its reward.

| Action | Observed completion comparison with boosted worth |
|---|---|
| Referral share, 1,000-10,000 Entrants | +34-35% completions, 19-21% cheaper per completion |
| Referral share, 10,000+ Entrants | +11% completions |
| Follow (X, Twitch, TikTok) | within 17% either way, no consistent direction |
| Telegram Channel Members | 0.57x-0.74x completions |
| YouTube Entries | 0.53x-0.85x completions |
| UGC submissions | 0.20x-0.57x completions |

[Extracted from `analysis/output/asset_yield.json`, `yield_by_asset_and_worth_tier`.]

## Actions that came with more people (extracted)

Among campaigns with no repeatable action and a run of 14 days or less, Telegram joins came with more Entrants and a higher Conversion Rate. Secret Code came with more Entrants and about the same Conversion Rate. App downloads came with more Entrants and a lower Conversion Rate. Follow actions differed: X Follows came with fewer Entrants and a lower Conversion Rate, while Twitch Follows came with fewer Entrants and a higher Conversion Rate. Read the counts and both measures in each row. These associations describe the campaigns businesses ran and do not show what adding an Action would change. Missing-data coverage is not reported separately for these rows.

<!-- generated:em_actions_baseline -->
| Action | Entrants vs the campaigns without it | Conversion Rate vs the same | Campaigns | Businesses |
|---|---|---|---|---|
| Telegram Channel Members | +47% | +38% | 1,789 | 370 |
| App Downloads | +45% | -28% | 1,184 | 257 |
| Secret Code | +28% | about level | 1,594 | 563 |
| Discord Members | +6% | about level | 7,176 | 1,443 |
| Instagram Follows | +3% | -7% | 2,238 | 876 |
| Facebook Likes | about level | -18% | 771 | 366 |
| YouTube Entries | about level | about level | 14,242 | 3,287 |
| X Follows | -9% | -6% | 21,879 | 4,119 |
| X Reposts | -14% | -4% | 8,938 | 2,294 |
| Twitch Follows | -17% | +24% | 8,981 | 1,873 |
<!-- /generated -->

As practice, require an app download only when using the app is the campaign objective and the hardware Prize is relevant to its users. Otherwise keep the download optional or omit it. The hardware comparison below does not establish that requiring an install improves conversion. These counts are small, the smallest cell resting on 56 businesses, so state the count every time and do not extend the pattern beyond these three cells.

<!-- generated:em_app_download -->
| Context | Observed conversion association (against what the action and Prize predict separately) |
|---|---|
| Prize is tech hardware | 1.9x (294 campaigns, 61 businesses) |
| Prize is a gift card or cash | 0.751x (219 campaigns, 83 businesses) |
| Gaming and esports vertical | 0.735x (265 campaigns, 56 businesses) |
<!-- /generated -->

[Extracted from `analysis/output/success_profiles.json`, `interactions.entry_method_by_prize_type` and `.entry_method_by_industry`.]

## What it looks like when many Entrants were referred (extracted)

Campaigns offering a share action had more Entrants and lower conversion typically [`cmp_share` in action-families.md: 544 Entrants against 406, and conversion 23% lower]. The dataset does not count the new people brought by that action, so these comparisons cannot establish a referral gain.

As practice, offer optional sharing when reaching new people is an objective. For a focused signup campaign, leave sharing out or place it after the signup. Choose based on the campaign's purpose, without promising a gain in reach or a loss of completion elsewhere. Lower completion on other actions was observed at the sizes below, with Telegram varying by size. [1,000-2,500, 2,500-10,000, 10,000+ Entrants.]

Observed differences:

| Metric | Comparison with campaigns offering a share action |
|---|---|
| Impressions per Entrant | +33-52% (1.33x-1.52x) |
| Entries per Entrant | +20-24% |
| Visits to the business's own site | +19-71% |

Completion on other actions running beside it (lower at every size tested except Telegram, which varies by size):

| Action | Completion multiplier |
|---|---|
| X Follows | 0.43x-0.71x |
| Twitch Follows | 0.20x-0.66x |
| Chat Members | 0.77x-0.82x |
| Telegram Channel Members | 0.60x-1.61x |
| YouTube Entries | 0.68x-0.74x |
| App Downloads | 0.74x-0.96x |
| UGC submissions | 0.21x-0.34x |

The email comparison with sharing varies by campaign size (cheaper and lower-yield at the smallest size, roughly flat to worse at 2,500-10,000 and 10,000+ Entrants), so don't claim sharing makes email cheaper or higher-yield as a general rule. [30 to 10,864 campaigns per group, 14 to 2,858 businesses. Extracted from `analysis/output/asset_yield.json`, `yield_by_asset_and_sharing`.] For planning referral promotion, see giveaway-promotion-plan.

**A few action pairs cluster well above chance, and they're the effort-heavy ones.** As with the family table above, this describes what businesses choose to run together, not what pairing two actions would do to either one's completion.

| Action pair | Co-occurrence lift |
|---|---|
| Content + account-connection | 1.41x (3,998 campaigns, 915 businesses) |
| Content + engagement | 1.97x (7,210 campaigns, 1,164 businesses) |
| Email + follow | 0.96x (25,855 campaigns, 3,645 businesses) |

[Extracted from `analysis/output/method_mix.json`, `family_pair_lift`.]

## What separated the top fifth, by goal (extracted)

Pick the goal and read down its column. Each column takes the campaigns that did best on that goal, the top fifth, and compares how often they made each choice with the other four fifths of campaigns of the same size and the same vertical. A cell shows how much more or less often the top fifth made the choice, then both shares. "About level" means the ratio sits between 0.85x and 1.15x. These are the choices businesses made, and nothing here says what any choice caused. Bigger and more experienced businesses choose differently, and matching on size and vertical removes some of that and never all of it.

<!-- generated:em3_goal_cohorts -->
| Goal | Campaigns the top fifth is drawn from | Campaigns in the top fifth | Businesses | Size and vertical groups |
|---|---|---|---|---|
| An email list | Email signups per Entrant, among campaigns running an email Action | 7,863 | 1,648 | 65 |
| Referrals | Referral entries per Entrant, among campaigns running a Referral share | 8,490 | 2,685 | 63 |
| Follows and joins | Follow, join or subscribe completions per Entrant, among campaigns running at least one | 16,769 | 3,547 | 64 |
| A bigger crowd | Entrants, compared inside each vertical only | 23,256 | 4,467 | 11 |
| More Entries per Entrant | Entries per Entrant, among all campaigns | 23,250 | 3,371 | 65 |
<!-- /generated -->

The population is campaigns of 100 or more Entrants with crypto and ambiguous campaigns removed (116,283 campaigns from 17,603 businesses). Each goal uses only the campaigns that can report it, so the email column covers campaigns that ran an email Action. The bigger-crowd column is matched on vertical alone, because matching on size would make it circular.

<!-- generated:em3_goal_features -->
| Choice | An email list (7,863 campaigns, 1,648 businesses) | Referrals (8,490 campaigns, 2,685 businesses) | Follows and joins (16,769 campaigns, 3,547 businesses) | A bigger crowd (23,256 campaigns, 4,467 businesses) | More Entries per Entrant (23,250 campaigns, 3,371 businesses) |
|---|---|---|---|---|---|
| Prize is the business's own product | about level (23% against 22%) | about level (19% against 19%) | about level (15% against 16%) | 1.2x (20% against 16%) | 0.8x (14% against 18%) |
| Collaboration wording in the title | about level (18% against 16%) | 1.2x (16% against 13%) | 1.5x (20% against 14%) | 1.3x (18% against 13%) | about level (14% against 14%) |
| Business has run 5 or more campaigns | about level (87% against 83%) | about level (76% against 85%) | about level (83% against 82%) | about level (86% against 80%) | about level (90% against 79%) |
| Secret Code offered | 0.6x (6% against 11%) | about level (11% against 11%) | 1.7x (14% against 8%) | 1.6x (11% against 7%) | 2.2x (14% against 6%) |
| Email signup offered | all, by construction | 0.8x (49% against 59%) | 0.6x (20% against 34%) | 1.5x (45% against 31%) | 1.3x (41% against 32%) |
| Referral share offered | about level (66% against 62%) | all, by construction | 0.8x (33% against 40%) | 1.2x (44% against 35%) | 1.7x (55% against 33%) |
| A follow, join or subscribe offered | about level (60% against 69%) | about level (76% against 74%) | all, by construction | about level (68% against 73%) | 1.3x (90% against 68%) |
| A question offered | 0.4x (5% against 11%) | 0.8x (10% against 13%) | 0.7x (9% against 12%) | about level (11% against 12%) | 1.2x (13% against 12%) |
| A required Action | 1.4x (60% against 43%) | about level (44% against 42%) | about level (41% against 39%) | about level (46% against 41%) | 0.8x (34% against 44%) |
| One Prize unit in total | about level (67% against 62%) | about level (56% against 63%) | about level (62% against 59%) | about level (60% against 60%) | 1.2x (67% against 59%) |
| Stated Prize pool under 250 USD | 1.3x (26% against 19%) | about level (20% against 21%) | 0.7x (14% against 19%) | 0.3x (5% against 20%) | 1.4x (22% against 16%) |
| 11 or more Actions | about level (30% against 34%) | about level (38% against 44%) | 2.0x (56% against 29%) | 1.2x (30% against 26%) | 5.0x (73% against 15%) |
| A repeatable Action | 0.7x (27% against 37%) | about level (41% against 44%) | about level (34% against 39%) | about level (37% against 35%) | 1.9x (56% against 30%) |
| Started in December | 1.3x (11% against 9%) | about level (9% against 10%) | about level (10% against 11%) | 1.2x (12% against 10%) | about level (9% against 11%) |
| An Action worth 5 or more Entries | 0.8x (48% against 59%) | about level (74% against 69%) | 1.2x (64% against 54%) | about level (51% against 49%) | 1.7x (72% against 43%) |
<!-- /generated -->

"All, by construction" marks the choice that defines the column. A stated Prize pool under 250 USD counts campaigns with a stated value only, so a campaign with no value stated counts as not under. A top fifth is a share of campaigns, and a business with many campaigns fills it many times, so read each ratio as describing campaigns.

- **An email list.** The top fifth by email signups per Entrant ran a required Action more often (1.4x, 60% against 43%) and a stated pool under 250 USD more often (1.3x, 26% against 19%). They ran a question less often (0.4x, 5% against 11%) and Secret Code less often (0.6x, 6% against 11%). Referral share sat level (66% against 62%).
- **Referrals.** Almost nothing in the table separated the top fifth by referral entries per Entrant. Collaboration wording was the one choice above level (1.2x, 16% against 13%), with email signup (0.8x) and a question (0.8x) below it. The 15 choices here do not explain referral yield.
- **Follows and joins.** The top fifth carried long lists of 11 or more Actions (2.0x, 56% against 29%), Secret Code (1.7x, 14% against 8%) and collaboration wording (1.5x, 20% against 14%) more often. They offered email signup less often (0.6x, 20% against 34%).
- **A bigger crowd.** The top fifth offered email signup (1.5x, 45% against 31%), Secret Code (1.6x, 11% against 7%) and collaboration wording (1.3x, 18% against 13%) more often. A stated pool under 250 USD marked 5% of the top fifth against 20% of the rest, the widest gap in the column.
- **More Entries per Entrant.** This column partly describes how the measure is built, because Entries rise with every Action and with every extra Entry an Action is worth. The top fifth ran 11 or more Actions far more often (5.0x, 73% against 15%), and a repeatable Action (1.9x, 56% against 30%), Secret Code (2.2x, 14% against 6%) and a referral share (1.7x, 55% against 33%) more often too.

To check a plan against this, take the goal's column and ask which of its choices the plan makes. If the goal is an email list and the plan has a question Action, the campaigns that did best on email signups per Entrant ran one less often than their peers.

[Extracted from `analysis/output/success_profiles.json`, `success_cohorts.email_yield_per_contestant`, `.referral_yield_per_contestant`, `.social_yield_per_contestant`, `.entrants` and `.engagement`, the stratified comparison. The unmatched comparison sits beside it in the source, and a choice that is large unmatched and level matched is explained by size and vertical.]

## Actions more common in top campaigns, by vertical (extracted)

Within each vertical, defined by grouping the business's industry label, campaigns split into fifths by Entrants. The ratio is how much more often an Action appears in the top fifth than the bottom fifth. The frame includes 116,283 ordinary campaigns with positive valid Entries. Business counts below cover the whole vertical, and distinct-business counts for each fifth are not published, so their privacy floor remains unverified. These comparisons describe the groups and do not show that an Action produced a larger audience.

Source: `analysis/output/context_checks.json` (`method_prevalence_top_vs_bottom_by_vertical`, `ordinary_n`).

| Vertical | Campaigns | Businesses | Campaigns per fifth | Actions over-represented in the top fifth |
|---|---|---|---|---|
| Gaming | 24,229 | 4,657 | 4,845 | Email Subscriptions 2.4x, Viral Shares 2.0x, TikTok Follows 1.6x, Chat Members 1.3x, Custom Actions 1.3x |
| Technology | 15,543 | 2,063 | 3,108 | TikTok Follows 1.7x, Custom Actions 1.6x, Secret Code 1.6x, Viral Shares 1.5x, Instagram Follows 1.4x, Chat Members 1.3x |
| Home | 3,710 | 594 | 742 | Pinterest Visits 2.5x, X Follows 2.2x, YouTube Channel Visits 2.0x, Viral Shares 1.7x, Instagram Profile Visits 1.6x, Facebook visits 1.4x, Bonus 1.4x, Email Subscriptions 1.3x |
| Fitness and outdoor | 7,795 | 1,508 | 1,559 | Viral Shares 2.1x, Bonus 1.7x, Email Subscriptions 1.5x, X Follows 1.4x, Instagram Profile Visits 1.2x |
| Travel | 3,969 | 638 | 793 | Viral Shares 1.9x, Email Subscriptions 1.6x, Custom Actions 1.6x, YouTube Channel Visits 1.5x |
| Software | 1,662 | 545 | 332 | Email Subscriptions 2.8x, Viral Shares 1.4x, Custom Actions 1.4x, YouTube Channel Visits 1.2x |
| Fashion and beauty | 6,457 | 1,305 | 1,291 | Custom Actions 3.7x, Email Subscriptions 2.9x, Facebook visits 1.9x, Viral Shares 1.8x, X Follows 1.3x |

The top fifth ran a typical 7 Actions against 6 in the bottom fifth, each covering 23,256 campaigns, from 4,543 and 7,763 businesses respectively (`analysis/output/context_checks.json`, `top_vs_bottom_quintile`). The comparison is within the same positive-valid-Entries frame. The finding from the campaigns we can compare fairly is that eleven or more actions came with 17% more Entrants than one to three, alongside lower conversion and far more Entries per Entrant [`cmp_methods` in action-families.md]. Keep the list purposeful and tied to the assets you can use.

**The exact combination businesses reach for differs by vertical, beyond what the per-family table above shows.** In electronics and tech and gaming and esports, the single most common exact action set skips email entirely and anchors on follow plus visit. In food and drink, sports and outdoors and media and entertainment, the most common sets are all built around email, visit and share together, with an extra action or two layered on. This is consistent with, not independent of, the per-family email-offered shares already in the sections above. [Campaigns, all clearing the size floor comfortably (334 to 1,840 businesses overall): electronics and tech 7,289, gaming and esports 6,328, food and drink 1,787, sports and outdoors 2,268, media and entertainment 5,019. Extracted from `analysis/output/method_mix.json`, `top_combinations_by_industry`.]

## Actions by industry, offered and completed (extracted)

The source covers 23 qualifying industries, from 116,283 campaigns of 100 or more Entrants and 17,603 businesses. Rows that could expose small groups by subtraction are withheld here. The offered columns list the Actions an industry's businesses offered at least 1.5x as often as the all-industry rate, or at most 0.67x as often, strongest first and up to three each. The completed columns list Actions where the typical completion among campaigns offering them ran at least 1.25x or at most 0.75x of the all-industry completion, up to two each. A dash means no Action cleared the cut. Each figure carries the campaigns and businesses that offered the Action. Completion is recorded completion events divided by Entrants, taking the median across campaigns offering the Action. A high ratio in an industry describes the Entrants that industry's businesses reached, and says nothing about what the Action would do for another business there.

<!-- generated:em3_industry_actions -->
| Industry | Campaigns | Businesses | Offered most often against all industries | Offered least often | Completed more often once offered | Completed less often once offered |
|---|---|---|---|---|---|---|
| Gaming and esports | 24,229 | 4,657 | Discord join 2.3x (9,008 campaigns, 1,802 businesses). Twitch follow 2.2x (10,358 campaigns, 2,536 businesses). X repost 1.7x (9,784 campaigns, 2,526 businesses) | Email signup 0.5x (3,935 campaigns, 493 businesses) | - | - |
| Media and entertainment | 21,540 | 2,074 | - | Secret code 0.5x (835 campaigns, 228 businesses). Twitch follow 0.6x (2,593 campaigns, 477 businesses). TikTok follow 0.6x (1,679 campaigns, 325 businesses) | - | Telegram join 0.4x (464 campaigns, 73 businesses). Referral share 0.7x (8,102 campaigns, 672 businesses) |
| Electronics and tech | 15,543 | 2,063 | Telegram join 1.8x (965 campaigns, 76 businesses). TikTok follow 1.6x (3,000 campaigns, 418 businesses) | - | Secret code 2.0x (1,616 campaigns, 290 businesses). Referral share 1.7x (4,564 campaigns, 756 businesses) | - |
| Apparel and fashion | 4,628 | 812 | Email signup 1.6x (2,376 campaigns, 435 businesses) | Discord join 0.2x (128 campaigns, 53 businesses). Telegram join 0.2x (33 campaigns, 16 businesses). Twitch follow 0.3x (268 campaigns, 97 businesses) | - | Telegram join 0.3x (33 campaigns, 16 businesses). Secret code 0.5x (189 campaigns, 75 businesses) |
| Travel and events | 3,969 | 638 | - | Twitch follow 0.1x (70 campaigns, 29 businesses). Discord join 0.1x (66 campaigns, 37 businesses). Telegram join 0.3x (37 campaigns, 20 businesses) | - | Twitch follow 0.2x (70 campaigns, 29 businesses). X follow 0.4x (1,419 campaigns, 220 businesses) |
| Home and garden | 3,710 | 594 | Email signup 1.8x (2,148 campaigns, 341 businesses). Referral share 1.5x (2,099 campaigns, 338 businesses) | Discord join 0.1x (44 campaigns, 16 businesses). Twitch follow 0.1x (74 campaigns, 15 businesses). X repost 0.4x (359 campaigns, 77 businesses) | - | Secret code 0.6x (271 campaigns, 84 businesses). Discord join 0.6x (44 campaigns, 16 businesses) |
| Health, wellness and fitness | 3,160 | 498 | - | Discord join 0.2x (94 campaigns, 21 businesses). Twitch follow 0.2x (139 campaigns, 10 businesses) | - | Secret code 0.5x (180 campaigns, 71 businesses). Discord join 0.6x (94 campaigns, 21 businesses) |
| Retail marketplace | 2,860 | 382 | - | YouTube channel visit 0.5x (512 campaigns, 142 businesses). Telegram join 0.5x (51 campaigns, 29 businesses). Discord join 0.6x (272 campaigns, 40 businesses) | Discord join 2.4x (272 campaigns, 40 businesses). Secret code 1.9x (162 campaigns, 54 businesses) | Referral share 0.6x (1,306 campaigns, 162 businesses) |
| Automotive | 2,310 | 379 | Email signup 1.7x (1,295 campaigns, 145 businesses). Referral share 1.5x (1,293 campaigns, 175 businesses) | Discord join 0.1x (41 campaigns, 30 businesses). X repost 0.3x (177 campaigns, 65 businesses). TikTok follow 0.4x (127 campaigns, 60 businesses) | Secret code 1.5x (242 campaigns, 50 businesses) | Twitch follow 0.2x (276 campaigns, 50 businesses). X follow 0.7x (1,179 campaigns, 155 businesses) |
| Education | 1,868 | 357 | - | Twitch follow 0.3x (109 campaigns, 29 businesses). Discord join 0.3x (93 campaigns, 36 businesses). X repost 0.3x (138 campaigns, 67 businesses) | - | Discord join 0.6x (93 campaigns, 36 businesses). Referral share 0.7x (534 campaigns, 200 businesses) |
| Software and SaaS | 1,662 | 545 | Telegram join 2.2x (125 campaigns, 71 businesses) | Facebook visit 0.7x (445 campaigns, 191 businesses) | Referral share 1.9x (702 campaigns, 264 businesses). Telegram join 1.6x (125 campaigns, 71 businesses) | Twitch follow 0.7x (218 campaigns, 64 businesses) |
| Art and crafts | 1,590 | 401 | - | Twitch follow 0.4x (110 campaigns, 72 businesses). Discord join 0.4x (108 campaigns, 53 businesses). X follow 0.5x (485 campaigns, 177 businesses) | Telegram join 1.5x (41 campaigns, 24 businesses) | TikTok follow 0.7x (154 campaigns, 62 businesses) |
| Beauty and personal care | 1,411 | 351 | Instagram follow 4.3x (429 campaigns, 47 businesses). Secret code 3.1x (337 campaigns, 43 businesses). TikTok follow 2.9x (495 campaigns, 64 businesses) | Discord join 0.1x (31 campaigns, 17 businesses). Twitch follow 0.2x (48 campaigns, 28 businesses). YouTube channel visit 0.6x (321 campaigns, 113 businesses) | Secret code 1.3x (337 campaigns, 43 businesses) | X repost 0.6x (419 campaigns, 42 businesses). X follow 0.6x (641 campaigns, 117 businesses) |
| Marketing agency | 1,201 | 157 | TikTok follow 2.0x (297 campaigns, 33 businesses). Secret code 1.5x (139 campaigns, 27 businesses) | Twitch follow 0.6x (134 campaigns, 20 businesses) | Referral share 1.3x (366 campaigns, 65 businesses) | Secret code 0.7x (139 campaigns, 27 businesses). Instagram follow 0.7x (120 campaigns, 26 businesses) |
| Baby and kids | 1,184 | 138 | Email signup 1.6x (626 campaigns, 91 businesses). Referral share 1.5x (661 campaigns, 78 businesses) | YouTube channel visit 0.3x (136 campaigns, 25 businesses). X repost 0.6x (170 campaigns, 10 businesses) | - | YouTube channel visit 0.6x (136 campaigns, 25 businesses). Referral share 0.7x (661 campaigns, 78 businesses) |
| Local services | 917 | 181 | Secret code 1.6x (114 campaigns, 34 businesses) | YouTube channel visit 0.3x (123 campaigns, 61 businesses). X repost 0.5x (102 campaigns, 19 businesses). Email signup 0.5x (144 campaigns, 49 businesses) | - | X repost 0.3x (102 campaigns, 19 businesses). Secret code 0.4x (114 campaigns, 34 businesses) |
<!-- /generated -->

**Gaming and esports campaigns offer Discord, Twitch and X reposts more often, and email less often, than the all-industry rate.** Email is offered in 16.2% of gaming campaigns against 33.0% across all industries, and where it is offered it completes at 0.83x its all-industry completion rate, the lowest relative index of the 13 Actions in the table below. Each index compares an Action with its own baseline, so it cannot rank different Actions by absolute completion or value to the requested asset. Keep email as the primary acquisition action when the objective is an email list. Consider Discord, Twitch or X only when the audience and objective support them.

<!-- generated:em3_gaming_actions -->
| Action | Offered, gaming and esports | Offered, all industries | Ratio | Completion against all industries | Campaigns offering it | Businesses |
|---|---|---|---|---|---|---|
| Discord join | 37.2% | 16.2% | 2.3x | 1.01x | 9,008 | 1,802 |
| Twitch follow | 42.8% | 19.3% | 2.2x | 1.00x | 10,358 | 2,536 |
| X repost | 40.4% | 23.6% | 1.7x | 1.08x | 9,784 | 2,526 |
| Telegram join | 5.6% | 3.4% | 1.7x | 1.06x | 1,367 | 276 |
| X follow | 78.3% | 56.5% | 1.4x | 1.18x | 18,968 | 3,827 |
| YouTube channel visit | 50.2% | 38.4% | 1.3x | 1.04x | 12,157 | 3,032 |
| Secret code | 9.0% | 7.7% | 1.2x | 1.10x | 2,173 | 631 |
| TikTok follow | 13.9% | 12.3% | 1.1x | 1.14x | 3,368 | 822 |
| Instagram profile visit | 48.2% | 50.8% | 1.0x | 1.03x | 11,689 | 2,368 |
| Instagram follow | 6.2% | 7.1% | 0.9x | 0.99x | 1,499 | 577 |
| Facebook visit | 33.6% | 40.1% | 0.8x | 1.05x | 8,135 | 1,471 |
| Referral share | 26.7% | 37.1% | 0.7x | 1.24x | 6,456 | 1,045 |
| Email signup | 16.2% | 33.0% | 0.5x | 0.83x | 3,935 | 493 |
<!-- /generated -->

[24,229 gaming and esports campaigns, 4,657 businesses, with each Action's own counts in the table. Extracted from `analysis/output/vertical_profiles.json`, `by_industry` and `action_index_by_industry`.]

## Mix by the kind of business running it (extracted)

From `analysis/output/industries.json`. Every group listed clears 30 campaigns and 10 businesses. This cut runs wider than the 116,499 campaigns behind the rest of this file, so read its campaign counts as that wider set.

By audience (by_audience), typical values:

<!-- generated:em_audience -->
| Audience | Campaigns | Businesses | Methods | Referral entries % of Entrants | Email offered |
|---|---|---|---|---|---|
| B2C | 105,282 | 15,582 | 7 | 16 | 34% |
| B2B | 12,728 | 1,779 | 7 | 44 | 19% |
| Both | 3,832 | 511 | 7 | 46 | 19% |
<!-- /generated -->

B2B and mixed-audience businesses lean far more on referrals than B2C, close to three times as many referral entries per 100 Entrants, and offer email about half as often. All three run the same typical 7 methods.

By stage (by_org_stage), typical values:

<!-- generated:em_stage -->
| Stage | Campaigns | Businesses | Methods | Referral entries % of Entrants | Email offered |
|---|---|---|---|---|---|
| Small business | 60,935 | 7,897 | 7 | 12 | 45% |
| Startup | 23,190 | 5,227 | 8 | 58 | 15% |
| Mid market | 17,126 | 1,384 | 6 | 36 | 22% |
| Individual | 10,371 | 1,808 | 9 | 12 | 10% |
| Enterprise | 6,675 | 507 | 6 | 24 | 25% |
| Public body | 1,109 | 294 | 7 | 8 | 44% |
<!-- /generated -->

Startups run the most referral-heavy mix of any stage and offer email least often next to individuals. Small businesses sit at the other end, email offered in 45% of campaigns and referrals a fifth of a startup's.

By business type (by_business_type), email offered, lowest to highest:

<!-- generated:em_btype -->
| Business type | Campaigns | Businesses | Email offered | Referral entries % of Entrants |
|---|---|---|---|---|
| Creator | 18,168 | 4,187 | 5% | 7 |
| Community | 4,999 | 1,128 | 8% | 44 |
| Software | 30,426 | 5,133 | 12% | 62 |
| Other | 7,846 | 2,149 | 18% | 20 |
| Agency | 3,324 | 368 | 22% | 22 |
| Service business | 4,092 | 803 | 32% | 9 |
| Nonprofit | 968 | 280 | 33% | 9 |
| Brand | 31,193 | 5,708 | 41% | 14 |
| Media or publisher | 21,108 | 1,645 | 42% | 10 |
| Retailer | 21,733 | 2,266 | 44% | 11 |
<!-- /generated -->

Creator businesses offer email least, community next. Software and community are the two most referral-heavy business types in the data, at 62 and 44 referral entries per 100 Entrants, ahead of agency in third place at 22.

## Mix by country (extracted)

Action shares among campaigns with 100 or more Entrants, by the business's country. Source: `analysis/output/country_cuts.json`, by_country.

<!-- generated:em_country -->
| Country | Campaigns | Businesses | Days | Methods | Email | Share or refer | X Follows | Instagram visits | Facebook | Telegram | Wallet address |
|---|---|---|---|---|---|---|---|---|---|---|---|
| United States | 57,289 | 8,720 | 14 | 7 | 39% | 44% | 54% | 51% | 50% | 2% | 1% |
| United Kingdom | 15,188 | 1,710 | 21 | 7 | 30% | 23% | 66% | 43% | 48% | 4% | 1% |
| Canada | 7,004 | 1,066 | 12 | 6 | 40% | 38% | 59% | 52% | 47% | 2% | 1% |
| Australia | 6,066 | 1,334 | 15 | 6 | 48% | 43% | 39% | 56% | 55% | 1% | 0% |
| Brazil | 5,299 | 497 | 1 | 9 | 1% | 35% | 75% | 69% | 25% | 27% | 1% |
| Japan | 4,797 | 235 | 6 | 7 | 6% | 60% | 88% | 11% | 21% | 48% | 5% |
| India | 4,062 | 691 | 9 | 7 | 6% | 57% | 81% | 29% | 19% | 54% | 41% |
| Singapore | 3,491 | 271 | 7 | 6 | 5% | 45% | 81% | 16% | 16% | 35% | 11% |
| Germany | 3,322 | 419 | 11 | 7 | 18% | 32% | 65% | 50% | 45% | 8% | 2% |
| South Korea | 2,675 | 392 | 8 | 7 | 2% | 60% | 88% | 10% | 5% | 56% | 21% |
| Vietnam | 2,501 | 547 | 9 | 7 | 2% | 62% | 80% | 4% | 19% | 43% | 18% |
| France | 2,174 | 356 | 14 | 7 | 12% | 22% | 80% | 54% | 32% | 6% | 4% |
| Poland | 2,157 | 188 | 13 | 8 | 38% | 43% | 72% | 49% | 50% | 10% | 2% |
| Philippines | 2,053 | 289 | 17 | 7 | 44% | 57% | 50% | 25% | 39% | 12% | 4% |
| Hong Kong | 1,973 | 428 | 8 | 7 | 12% | 49% | 75% | 18% | 26% | 28% | 17% |
| Taiwan | 1,920 | 157 | 8 | 7 | 5% | 45% | 71% | 35% | 35% | 33% | 6% |
| Spain | 1,884 | 496 | 13 | 7 | 9% | 22% | 79% | 49% | 23% | 12% | 2% |
| China | 1,541 | 136 | 8 | 7 | 14% | 56% | 75% | 18% | 44% | 27% | 3% |
| Malaysia | 1,501 | 103 | 6 | 7 | 11% | 55% | 72% | 16% | 21% | 49% | 8% |
| Türkiye | 1,406 | 367 | 8 | 5 | 2% | 26% | 55% | 35% | 10% | 29% | 21% |
| Sweden | 1,311 | 137 | 9 | 5 | 7% | 11% | 32% | 50% | 33% | 1% | 2% |
| The Netherlands | 1,232 | 253 | 14 | 7 | 28% | 35% | 71% | 53% | 40% | 18% | 3% |
| United Arab Emirates | 742 | 153 | 8 | 7 | 5% | 41% | 87% | 24% | 19% | 30% | 14% |
| Egypt | 716 | 37 | 8 | 13 | - | 4% | 6% | 4% | 4% | 1% | - |
| Thailand | 652 | 170 | 8 | 8 | 12% | 47% | 74% | 8% | 47% | 18% | 6% |
| Mexico | 652 | 183 | 8 | 5 | 10% | 16% | 44% | 51% | 57% | 7% | 1% |
| South Africa | 633 | 155 | 15 | 6 | 22% | 21% | 61% | 50% | 44% | 6% | 1% |
| Portugal | 521 | 146 | 9 | 6 | 8% | 37% | 53% | 46% | 31% | 20% | 5% |
| Indonesia | 517 | 138 | 7 | 9 | 3% | 53% | 90% | 10% | 14% | 65% | 50% |
| Italy | 512 | 105 | 22 | 7 | 50% | 30% | 81% | 50% | 50% | 12% | 4% |
<!-- /generated -->

Japan and India both lean on Telegram, offered in about half their campaigns. India adds a wallet-address action, the crypto marker this skill's default figures exclude elsewhere, in two fifths of its campaigns, and Indonesia in half. Brazil's campaigns run a typical one day and carry 9 Entry Methods, behind only Egypt's 13 on 716 campaigns. Both figures come from automated recurring draws: its 25th percentile duration is also 1 day, 91% of its campaigns are repeats and 93% start on the hour. Read the row as what those accounts do. An X Follow is the most common action in most of the table, the United States included at 54%. Email is offered most often in Italy, Australia and the Philippines, all above two fifths of their campaigns.

**How often actions are required.** Malaysia requires at least one action in 91% of its campaigns and India follows at 79%. China, South Korea and Vietnam ask for the most once they ask for any, a typical 6. Germany requires an action least often at 29%.

<!-- generated:em_mandatory_country -->
| Country | Campaigns | Businesses | Campaigns with 1+ required action | Typical required actions (where 1+) |
|---|---|---|---|---|
| Malaysia | 1,501 | 103 | 91% | 5 |
| India | 4,062 | 691 | 79% | 5 |
| Japan | 4,797 | 235 | 76% | 5 |
| Philippines | 2,053 | 289 | 73% | 1 |
| China | 1,541 | 136 | 73% | 6 |
| Singapore | 3,491 | 271 | 71% | 5 |
| South Korea | 2,675 | 392 | 66% | 6 |
| Vietnam | 2,501 | 547 | 62% | 6 |
| Türkiye | 1,406 | 367 | 59% | 3 |
| Hong Kong | 1,973 | 428 | 59% | 4 |
| Australia | 6,066 | 1,334 | 57% | 1 |
| Spain | 1,884 | 496 | 56% | 2 |
| France | 2,174 | 356 | 47% | 2 |
| Poland | 2,157 | 188 | 38% | 3 |
| United Kingdom | 15,188 | 1,710 | 36% | 1 |
| Brazil | 5,299 | 497 | 36% | 3 |
| Canada | 7,004 | 1,066 | 35% | 1 |
| Germany | 3,322 | 419 | 29% | 2 |
<!-- /generated -->

[Source: `analysis/output/indicators.json`, mandatory_actions_by_country.]

**Question actions.** A question action is closer to routine in East and Southeast Asia than elsewhere, with Vietnam, Singapore, Malaysia and South Korea all near or above half their campaigns. Among the published validation shares, Taiwan is highest at 16% and the other countries are at or below a tenth. Withheld shares cannot support a comparison.

<!-- generated:em_question_country -->
| Country | Campaigns | Businesses | Campaigns with a question action | Validation on, of those |
|---|---|---|---|---|
| Vietnam | 2,501 | 547 | 59% | 9% |
| Singapore | 3,491 | 271 | 53% | 6% |
| Malaysia | 1,501 | 103 | 49% | 1% |
| South Korea | 2,675 | 392 | 49% | 3% |
| China | 1,541 | 136 | 46% | - |
| Taiwan | 1,920 | 157 | 38% | 16% |
| Poland | 2,157 | 188 | 36% | 1% |
| Hong Kong | 1,973 | 428 | 32% | 6% |
| Japan | 4,797 | 235 | 29% | 1% |
| India | 4,062 | 691 | 20% | 2% |
| Australia | 6,066 | 1,334 | 18% | 8% |
| Türkiye | 1,406 | 367 | 16% | 3% |
| United Kingdom | 15,188 | 1,710 | 13% | 4% |
| United States | 57,289 | 8,720 | 12% | 10% |
| Philippines | 2,053 | 289 | 11% | 4% |
| Germany | 3,322 | 419 | 11% | 9% |
| Brazil | 5,299 | 497 | 9% | - |
| Spain | 1,884 | 496 | 8% | - |
| France | 2,174 | 356 | 8% | 3% |
| Canada | 7,004 | 1,066 | 7% | 7% |
<!-- /generated -->

[Source: `analysis/output/indicators.json`, question_action_by_country.]

**Worth settings, crypto and SaaS businesses removed.** Poland's typical top worth on a campaign runs well above the other countries measured here.

<!-- generated:em_worth_country -->
| Country | Campaigns | Businesses | Typical top worth |
|---|---|---|---|
| Poland | 1,911 | 140 | 25 |
| Türkiye | 957 | 206 | 10 |
| China | 814 | 79 | 7 |
| Malaysia | 466 | 60 | 7 |
| United States | 53,955 | 7,886 | 5 |
| Germany | 2,945 | 325 | 5 |
| France | 1,920 | 264 | 5 |
| Spain | 1,612 | 403 | 5 |
| Taiwan | 1,162 | 89 | 5 |
| South Korea | 776 | 132 | 5 |
| Singapore | 1,148 | 139 | 4 |
| United Kingdom | 13,899 | 1,470 | 3 |
| Canada | 6,445 | 932 | 3 |
| Australia | 5,765 | 1,231 | 3 |
| Brazil | 4,790 | 392 | 3 |
| Japan | 1,019 | 125 | 3 |
| Philippines | 1,632 | 215 | 2 |
| India | 1,558 | 441 | 2 |
| Hong Kong | 891 | 205 | 2 |
| Vietnam | 676 | 191 | 1 |
<!-- /generated -->

[Source: `analysis/output/indicators.json`, mechanics_by_country_excluding_crypto.]

These describe businesses' choices in each country, never a country's effect on a campaign.

## What each action produced per campaign (extracted)

Typical completions per campaign among campaigns that offered the action, completions % of Entrants, and stated USD of Prize per completion where the pool was valued. A completion is a signup, follow or join at that moment. Full table with quarter-by-quarter detail and campaigns by size in the results-review skill. Source: `analysis/output/asset_yield.json`, `yield_by_asset`.

| Asset | Campaigns | Typical per campaign | Share of Entrants | Stated USD per completion |
|---|---|---|---|---|
| Email Subscriptions | 39,339 | 714 | 99 | 0.40 |
| X Follows | 65,714 | 308 | 61 | 0.64 |
| Instagram Follows | 8,208 | 370 | 61 | 0.81 |
| TikTok Follows | 14,295 | 230 | 38 | 1.22 |
| Twitch Follows | 22,490 | 335 | 77 | 0.57 |
| YouTube Entries | 3,495 | 373 | 83 | 0.70 |
| Chat Members | 18,890 | 264 | 48 | 1.15 |
| Telegram Channel Members | 3,916 | 638 | 87 | 0.77 |
| App Downloads | 3,463 | 335 | 41 | 1.31 |
| Referral entries (Viral Shares) | 42,536 | 88 | 11 | 2.90 |
| Content submissions | 3,271 | 110 | 17 | 16.00 |

Stated Prize value per email signup and per follow by vertical sits in the Prize picker's `roi-benchmarks.md`. An Email Subscriptions action in a typical campaign produced about 700 email signups. The same campaign's Viral Share produced about 90 referral entries, and a content action about 110 submissions. Those are recorded completions among campaigns offering the action, never a count of available contact addresses or of individual marketing consent, and each row covers its own campaigns, so the medians do not describe one campaign's combined results. Source: `analysis/output/asset_yield.json`, `yield_by_asset` (rounded completion medians).

## Wording and destinations (extracted)

Completion events per Entrant, summarized across offered Actions within each family and position.

Completions % of Entrants by position in the action list, from `analysis/output/field_cuts.json` `uptake_by_family_and_position`. The sharing comparison uses `share|1st.completions_per_contestant` and `share|5th+.completions_per_contestant`. Sample counts are Actions offered, not campaigns:

| Family | 1st | 2nd to 4th | 5th or later |
|---|---|---|---|
| Email signup | 101 (20,986 Actions) | 78 (10,182 Actions) | 73 (16,859 Actions) |
| Visit a page | 98 (14,449 Actions) | 86 (84,512 Actions) | 75 (132,797 Actions) |
| Follow or subscribe | 82 (20,468 Actions) | 56 (75,063 Actions) | 42 (116,619 Actions) |
| Content upload | 81 (2,573 Actions) | 27 (4,657 Actions) | 13 (6,599 Actions) |
| Share or refer | 16 (993 Actions) | 12 (11,344 Actions) | 11 (30,470 Actions) |

Every family falls down the list, and a follow loses about half its completions between first place and fifth. Put the action that captures the asset at the top. Sharing sits at 16% of Entrants in first and 12% in the next three, then 11% fifth or later: it completes lowest of any family wherever it sits, and it gives up 5 points between first place and fifth, the smallest drop in the table, so the bottom slot is the cheapest place to put it. That drop is the difference between the cited completion ratios, multiplied by a hundred and rounded to whole percentage points (`analysis/output/field_cuts.json`, `uptake_by_family_and_position`).

The position advantage extends past email and follow, and holds by campaign size. The ratio below is the asset's completions per Entrant in the first list position over the same asset later in the list, split into three groups by campaign size. [Scope: 1,000+ Entrant campaigns. Extracted from `analysis/output/asset_yield.json`, `yield_by_asset_and_position`.]

| Asset | 1,000-2,500 | 2,500-10,000 | 10,000+ |
|---|---|---|---|
| Email Subscriptions | 1.42x | 1.45x | 1.27x |
| X Follows | 1.44x | 1.59x | 1.62x |
| Instagram Follows | 1.40x | 1.76x | too few campaigns to report |
| Twitch Follows | 1.68x | 1.77x | 1.98x |
| Chat Members | 1.60x | 1.91x | too few campaigns to report |
| YouTube Entries | 2.09x | 2.23x | too few campaigns to report |
| Visit the business's own site | 1.36x | 1.50x | 1.50x |

Every asset with enough volume to test held its position advantage at every size. Instagram Follows, Chat Members and YouTube Entries don't clear enough campaigns at 10,000+ Entrants to report. [Campaign counts behind the ratios above range from 38 (Twitch Follows, first position, 10,000+ Entrants, 21 businesses) to 26,161 (visits to the business's own site, later position, 1,000-2,500 Entrants, 2,581 businesses).]

**Which asset goes first, when the objective is reach.** The advice above is to put the asset action first, and that has a direction when the asset is sharing. In campaigns offering both an email action and a share action, listing share before email records more share completions on lists of 1 to 6 methods and on lists of 11 or more, and fewer on lists of 7 to 10. The larger share-first association appears at 11 or more methods, where those campaigns record about two thirds again the share completions. Treat the short-list difference as too small to act on. These comparisons hold list length within a band, but do not isolate what changing order would do. Common practice, our data doesn't cover this. Choose an order to test against the objective and weigh both email and share completion. Method-count associations are discussed separately further down this file.

| Method count | Share completion, share-first | Share completion, email-first |
|---|---|---|
| 1-6 methods | 14 per 100 | 12 per 100 |
| 7-10 methods | 10 per 100 | 13 per 100 |
| 11+ methods | 34 per 100 | 20 per 100 |

Email does not consistently pay for it: it completes about 82 to 104 per 100 Entrants when it follows a share action, against roughly 89 to 101 when it leads, lower on short lists and level or a little higher on longer ones. [Share-first campaigns/businesses: 672/256 (1-6), 1,821/421 (7-10), 4,554/521 (11+). Email-first: 5,863/1,666 (1-6), 6,945/1,889 (7-10), 7,463/1,234 (11+). Extracted from `analysis/output/method_mix.json`, `share_position_relative_to_email` and `top_combinations`.]

A cross-check on exact combinations shows the same direction on share: follow, visit and share with no email completes about 45 per 100 Entrants on share [3,790 campaigns, 1,359 businesses]. Add email to a share-carrying shape and share completion runs about 8 to 36 per 100 across the five combinations carrying both, under the matching shape without email in every pair.

**What leads the list and overall conversion.** Campaigns led by different action families show different conversion, pooled across every method count, not split by list length. This is an association across the whole dataset, not a comparison within a fixed list length, and businesses who lead with a quick connect-account step or a single question may already be running a leaner campaign in every other respect. Treat it as a pattern to weigh, not a rule to follow.

<!-- generated:em_lead_family -->
| Lead action family | Conversion Rate | Campaigns | Businesses |
|---|---|---|---|
| Question | 30.9% | 7,315 | 1,244 |
| Account connection | 30.6% | 4,780 | 1,326 |
| Follow | 28.2% | 16,266 | 4,493 |
| Join | 27.1% | 2,576 | 826 |
| Visit | 26.7% | 31,064 | 6,181 |
| Email | 26.7% | 21,047 | 3,825 |
| Bonus | 26.1% | 19,036 | 3,776 |
| Share | 23.7% | 2,692 | 916 |
| Engage | 22.3% | 2,866 | 444 |
| Download | 20.9% | 649 | 255 |
| Content | 14.3% | 1,756 | 649 |
<!-- /generated -->

A question or an account connection at the head of the list sits about four points above a visit, an email or a bonus, and content sits twelve points below them. The five families from follow down to bonus sit within about two points of each other, so what leads matters far less than whether the first thing asked is a piece of work. These are campaigns grouped by what they happened to lead with, never a test of moving an action to the front.

[Source: `analysis/output/method_mix.json`, `lead_action_family`.]

Question actions by what they ask (regex on the question text):

<!-- generated:em2_question_types -->
| Question type | Actions | Businesses | Completed it, per 100 Entrants (typical) |
|---|---|---|---|
| feedback or open | 839 | 374 | 86 |
| other | 6,937 | 1,509 | 75 |
| preference | 3,475 | 898 | 70 |
| detail capture | 6,755 | 851 | 68 |
| trivia | 1,640 | 325 | 62 |

A feedback or open question is completed most, by about 86 of every 100 Entrants, and trivia least at 62. Detail capture, the type that asks for a name, an order id or an account, sits fourth at 68.
<!-- /generated -->

Trivia is the only type with a right answer, which is the plain reading of why it sits last. [Source: `analysis/output/text_and_context.json`, `question_types`.]

Share copy on Viral Share and X Posts actions (59,012 actions with custom text, from `analysis/output/text_and_context.json` `share_copy`): a hashtag, first person and an emoji all complete higher. Length does not run one way, with short copy highest and the 60 to 140 character band lowest. Most of the hashtag gap is the action type, since X Posts actions carry hashtags and record more completions than Viral Share (about 34 against 11 per 100 Entrants), first person and an emoji still sit higher within the same copy length. Nearly every campaign wrote custom share text, so the default cannot be compared.

| Copy trait | Completion (per 100 Entrants) |
|---|---|
| Short, under 60 characters | 24 (1,123 actions) |
| Medium, 60-140 characters | 16 (39,435 actions) |
| Long, over 140 characters | 20 (18,454 actions) |
| No hashtag | 13 (46,415 actions) |
| With hashtag | 35 (12,597 actions) |
| Not first person | 15 (48,969 actions) |
| First person | 29 (10,043 actions) |
| No emoji | 16 (56,264 actions) |
| With emoji | 32 (2,748 actions) |

Visit actions by where they send people:

<!-- generated:em_visit_destinations -->
| Destination | Actions | Businesses | Share who completed it (typical) |
|---|---|---|---|
| another site | 121,345 | 6,668 | 77 |
| YouTube | 49,326 | 7,552 | 85 |
| the business's own site | 10,195 | 2,564 | 97 |
| another Gleam campaign | 583 | 271 | 85 |
| Steam | 303 | 30 | 79 |
| Instagram | 194 | 39 | 95 |
| Facebook | 109 | 33 | 57 |
| Amazon | 100 | 29 | 69 |
<!-- /generated -->

A visit to the business's own site records 97 completions per 100 Entrants, a YouTube channel by 85 and any other site by 77. Two thirds of visit actions land in that last row, which is every destination the rules do not name, so it carries no one kind of page. [Source: `analysis/output/text_and_context.json`, `visit_destinations`.]

Email Subscriptions by the description under the action, from `analysis/output/text_and_context.json` `newsletter_wording`:

<!-- generated:em_newsletter_wording -->
| Newsletter description | Actions | Businesses | Share who completed it (typical) |
|---|---|---|---|
| no description | 20,856 | 3,554 | 95 |
| description without those | 18,701 | 2,478 | 81 |
| mentions frequency or unsubscribe | 7,301 | 863 | 81 |
<!-- /generated -->

No description at all ran highest, at 95 per 100 Entrants. A description completed at 81 whether or not it mentioned frequency and unsubscribe wording. More words under the checkbox give people more to think about. Write the frequency line anyway where the law asks for it, and keep it to one line.

## Friction

Longer lists went with a lower share of Impressions converting, though their Entrant counts held up. Extracted: a typical campaign offers 7 methods and the top tenth offers 16 or more. Nothing in the data shows the effect of adding a method, so keep the count tied to the number of assets you can use. Three assets, five to eight methods.

Actions that cost the most: account connections (sign in with a social account), app installs, anything that leaves the entry page, and content creation. Keep those optional unless they are the objective.

**A single well-chosen action beats most combinations.** Among campaigns running exactly one action family, a bonus-only campaign has the highest Conversion Rate among the combinations listed, followed by question-only and email-only campaigns. This ranks the leanest campaigns against each other and does not repeat the method-count table below, it says which single action to reach for when the campaign only needs one.

| Single-family campaign | Conversion Rate |
|---|---|
| Question-only | 45.6% (2,464 campaigns, 403 businesses) |
| Bonus-only | 52.2% (2,428 campaigns, 639 businesses) |
| Email-only | 44.5% (2,502 campaigns, 471 businesses) |
| Visit-only | 39.6% (3,810 campaigns, 1,052 businesses) |
| Any 2+ family combination | below 40% |

[Extracted from `analysis/output/method_mix.json`, `top_combinations`.]

Source for the required-action comparisons: `analysis/output/method_mix.json`, `mandatory_count_vs_optional_completion`. Entrant differences use `contestants` for one required action divided by the comparison group in each method band, minus one, expressed as a percentage and rounded.

**More required actions costs completion on the optional ones, not overall conversion.** Holding total method count fixed, adding required actions lowers completion on whatever stays optional, while the campaign's conversion barely moves. Whether this is fatigue or businesses routing their lower-appeal actions into optional slots when they require more elsewhere can't be told apart in this data.

| Methods | Required actions | Optional-action completion | Conversion Rate |
|---|---|---|---|
| 7-10 | 0 | 70 per 100 | 24.5% |
| 7-10 | 1 | 54 per 100 | 24.0% |
| 7-10 | 2 | 52 per 100 | 23.7% |
| 7-10 | 3+ | 38 per 100 | 26.0% |
| 11+ | 0 | 61 per 100 | 22.4% |
| 11+ | 3+ | 39 per 100 | 20.5% |

**Exactly one required action goes with the biggest crowd, in every method band.** The Entrant count peaks at one
and drops on either side, and the shape repeats three times:

| Methods | 0 required | 1 required | 2 required | 3 or more |
|---|---|---|---|---|
| 1 to 6 | 436 | 544 | 412 | 390 |
| 7 to 10 | 484 | 644 | 386 | 408 |
| 11 or more | 560 | 747 | 408 | 546 |

One required action goes with 25% to 33% more Entrants than requiring none, and 32% to 83% more than requiring two (ratios of the table's Entrant medians, `analysis/output/method_mix.json`, `mandatory_count_vs_optional_completion`). Three separate bands landing on the same shape is worth more than any one of them, and the groups are large:
the smallest cell holds 1,908 campaigns from 436 businesses.

Read it as the signature of a campaign built around one asset. A business that requires exactly one action has
usually decided what the campaign is for and put a push behind it, where requiring none leaves the entry free and
requiring three makes the reader work before they are in. Nothing here shows that switching an action to required
would add Entrants to this campaign.

[7-10 methods: 2,095 to 18,990 campaigns, 799 to 4,297 businesses per group. 11+ methods: 1,908 to 19,534 campaigns, 436 to 2,562 businesses per group. Extracted from `analysis/output/method_mix.json`, `mandatory_count_vs_optional_completion`.]

**Conversion generally falls as action count rises, and there is no reliable point where the decline stops.** The curve halves between one action and thirteen, and quoting a single turning point to a reader overstates what the data holds.

| Actions | Campaigns | Conversion Rate |
|---|---|---|
| 1 | 4,886 | 49.7% |
| 4 | 4,288 | 35.4% |
| 7 | 3,287 | 31.3% |
| 10 | 1,628 | 27.2% |
| 13 | 990 | 26.0% |
| 16 | 288 | 25.3% |
| 20 | 524 | 68.8% |

A two-segment fit over the pooled 38,463 campaigns [`analysis/output/thresholds.json`, `action_count`] puts its breakpoint at 15 to 16 actions, and that is the fitter finding where the curve turns back up, never where the decline eases. The same search repeated inside each industry, size band and plan tier lands anywhere from 3 to 17 across eighteen groups, with the 10,000-plus band at 3 and the 500 to 1,000 band at 17. The source calls that stratification noise, and it is: no ordering by size, tier or industry survives it. So never quote a reader an elbow for their own group, and never promise them a count where the cost stops.

What the curve does support is the shape. Conversion Rate generally falls from the first action to about the thirteenth, with some increases between adjacent counts. Past sixteen it climbs back up on a few hundred campaigns per point, likely a handful of unusually well-optimized businesses still clearing 100 Entrants at that length, and that climb is no evidence that more actions help. [Ratios against what action count and size predict separately ran 91%-110% for conversion and 92%-111% for engagement, across all 12 groups. Extracted from `analysis/output/thresholds.json`, `action_count`, and `analysis/output/success_profiles.json`, `interactions.action_count_by_conversion_and_band` and `.action_count_by_engagement_and_band`.]

**Campaigns running more actions convert lower, and that holds inside most industries and not only pooled across all of them.** [`analysis/output/vertical_profiles.json`, `top_quartile_vs_rest_by_industry`.] In at least 13 of the 21 industries tested, the top quarter by conversion runs fewer actions and far less social or referral friction than the rest of that same industry, a like-for-like version of the pattern above.

<!-- generated:em_quartile_features -->
| Metric | Top quarter vs rest of industry | Industries showing this direction |
|---|---|---|
| Actions run | 0.67x | 17 of 21 |
| Referral share offered | 0.47x | 14 of 21 |
| Secret code offered | 0.46x | 14 of 21 |
| Platform follow offered | 0.71x | 13 of 21 |
<!-- /generated -->

Two examples:

<!-- generated:em_quartile_examples -->
| Industry | Top quarter | Rest of industry | Top quarter actions | Rest actions | Top quarter referral offered | Rest referral offered |
|---|---|---|---|---|---|---|
| Electronics and tech | 1,428 campaigns, 115 businesses | 4,281 campaigns, 851 businesses | 4 | 6 | 0.3% | 26.1% |
| Apparel and fashion | 499 campaigns, 48 businesses | 1,494 campaigns, 333 businesses | 1 | 4 | 3.6% | 25.4% |
<!-- /generated -->

This prices the fourth and fifth action, it is not an instruction to cut down to one. A campaign that needs three assets cannot run a one-action campaign, and nothing here says it should. What each added action, especially a referral or a secret code, costs on this specific completion measure is the number to weigh against what that action collects, so add it when the campaign needs that asset and budget for this rate to move. Conversion here is Entrants over Impressions, and a lean single-action entry form structurally has less friction between an Impression and a completed entry, so part of the pattern may describe how the metric is built as much as business choice. It does not mean a heavier campaign performs worse on total entries or reach, only on this completion rate. The top quarter itself is defined by conversion, one objective among several (an email list, followers, UGC and reach are the others), so an industry's top quarter by conversion is not automatically the shape to copy when the campaign's objective is one of those. Cite this finding with both caveats every time. Email offered and completion did not survive this same check (offered lower in 11 of the 21 industries and higher in 3, completion flat at a typical ratio of 1.00 across industries) and neither did community-join actions or question actions, so none of those are a vertical-strength signal here. [Extracted from `analysis/output/vertical_profiles.json`, `top_quartile_vs_rest_by_industry` and `threshold_check_top_vs_bottom_decile_pooled`.]

### Cheap actions against costly ones (extracted)

Two kinds of action sit on a list. The cheap kind is a visit, a follow or an engagement, quick to do and teaching the business little about the Entrant. The costly kind is a question, a content upload, an account connection, a download or a join, which asks more of the Entrant. Each campaign is placed by the share of its action types that are cheap. The count is of types, so a campaign with six follows and one question carries one cheap type and one costly type.

<!-- generated:em3_reach_deep -->
| Share of action types that are cheap | Campaigns | Businesses | Typical Entrants | Conversion Rate | Entries per Entrant | Typical Entry Methods | Email offered | Share offered |
|---|---|---|---|---|---|---|---|---|
| Under 25% cheap | 6,089 | 1,494 | 521 | 35% | 1.1 | 2 | 16% | 18% |
| 25% to under 50% cheap | 5,060 | 1,398 | 407 | 22% | 5.1 | 9 | 30% | 60% |
| 50% to under 75% cheap | 43,110 | 8,143 | 508 | 25% | 5.4 | 9 | 32% | 61% |
| 75% to 100% cheap | 54,694 | 10,418 | 482 | 27% | 4.2 | 6 | 38% | 53% |
<!-- /generated -->

Read it with three limits. Conversion Rate here is the typical value across every campaign in the group, never the fair-comparison subset used elsewhere in this file, so run length and repeatable Actions are mixed in. The share of cheap types travels with the length of the list: the mostly costly group ran a typical 2 Entry Methods, the two mixed groups ran 9 and the all-cheap group ran 6, so the table cannot separate the mix from the count. The mostly costly group is a short list, which fits its highest Conversion Rate and its 1.1 Entries each.

What it answers about piling on easy actions: the campaigns whose lists were 75% to 100% cheap types converted at 27% on a typical 6 Entry Methods, against 22% and 25% for the two mixed groups on 9. Mostly cheap lists did not convert lower than lists that mixed in costly types, and the data holds no separate limit for cheap Actions. The action-count curve above is the guide on length, since Conversion Rate generally fell from the first Action to about the thirteenth. Entries per Entrant rises with every Action an Entrant completes, so read the 4.2 against 5.1 and 5.4 as partly the list length.

[Population: campaigns of 100 or more Entrants carrying at least one cheap or costly action type, 1,398 to 10,418 businesses per group. Extracted from `analysis/output/method_mix.json`, `reach_vs_deep`.]

## Invalid entries (extracted)

Invalid share is invalid Entries divided by all Entries, calculated per campaign. The overall typical share is 4.2%, from 107,109 campaigns and 16,490 businesses with recorded invalid-entry values (`analysis/output/invalid_share.json`, `distribution.typical`). Campaigns with missing invalid-entry values are excluded from that distribution.

The wider Action comparison counts missing invalid-entry values as zero. Its population is 116,499 ordinary campaigns (`analysis/output/extra_cuts.json`, `ordinary_n`). Each rate is the typical campaign's invalid share, not a prediction of what adding an Action would cause.

Source: `analysis/output/extra_cuts.json` (`invalid_by_method_presence_all`, `ordinary_n`). Without-Action campaign counts are `ordinary_n` minus `n_with`. Distinct-business counts without each Action are not published and their privacy floor remains unverified.

| Action offered | With Action | Without Action | Campaigns with | Businesses with | Campaigns without |
|---|---|---|---|---|---|
| Share or referral | 4.3% | 3.1% | 43,173 | 6,959 | 73,326 |
| Chat Members | 4.5% | 3.4% | 18,909 | 3,254 | 97,590 |
| X Reposts | 4.0% | 3.4% | 27,474 | 5,658 | 89,025 |
| Email Subscriptions | 3.9% | 3.3% | 38,418 | 5,715 | 78,081 |
| Twitch Follows | 2.5% | 3.7% | 22,515 | 4,326 | 93,984 |

For campaigns without repeatable Actions and lasting at most 14 days, the typical invalid share was 3.5% both with and without a validated question. The groups contain 509 campaigns from 77 businesses and 38,993 campaigns from 7,104 businesses, respectively (`analysis/output/extra_cuts.json`, `invalid_validated_question_clean`). Missing invalid values are counted as zero in this comparison too.

Across the wider 116,499-campaign population, 42% had at least 5% invalid Entries and 7% had at least 20% (`analysis/output/extra_cuts.json`, `invalid_share_campaigns_5pct_plus`, `invalid_share_campaigns_20pct_plus`, `ordinary_n`). The source does not publish distinct-business counts for these threshold groups.

## Consent and rules

Keep entry consent and marketing consent separate, and collect the permission needed for each use. Entry consent is agreement to the terms of the giveaway, and it is collected on the entry form and recorded in the terms the Entrant accepts. Marketing consent is agreement to receive specified promotional messages. An Email Subscription Action collects it through a checkbox on the User Details form, and Newsletter signup also collects explicit consent. Check the recorded choice and wording for each person. Contact details can exist without either subscription Action. One does not imply the other, and an Entrant who declines the second is still a valid Entrant.

- Ask counsel what consent wording and records fit the campaign's countries, audience and email or SMS channel, and whether a proposed subscription condition is permissible or needs a different entry route. Draft wording that says what the Entrant will receive and how to leave, then check it against that advice and the chosen provider's documented setup.
- Ask counsel whether double opt-in is appropriate or required for this email or SMS flow in the relevant countries. If the agreed flow uses it, send confirmation at capture and add only confirmed contacts to the marketing list. Plan for a share of Entrants never confirming.
- Retention is a legal question this skill cannot answer. How long entry data, contact details and Winner records may be held, and what has to be deleted at the end, goes to the business's privacy counsel before the campaign opens.
- Follow-to-enter, tag-a-friend and share-to-enter are governed by each network's promotion rules, which change. Read the current rules for each network you name.
- For discount-code or purchase-linked entries, ask counsel whether the proposed access to the code creates a purchase condition in the relevant jurisdictions, whether the mechanic can run, and whether a free route or other changes are needed. Describe how people obtain the code and configure the entry flow according to that advice before launch.
- Age and region limits belong in the terms and on the entry form.

This skill does not give legal advice.

Extracted: of the Email Subscriptions actions in the ordinary campaigns with the opt-in checkbox set on or off, 24.9% had it on (9,764 actions against 29,510 off, with a further 7,584 set to automatic), a setting the campaign recorded and never a count of who ticked it or who declined. With the checkbox on, the typical action recorded 85 entries per 100 Entrants against 92 with it off [1,618 and 4,506 businesses, `analysis/output/field_cuts.json`, `config_cuts.email_opt_in_checkbox`]. The setting says nothing about whether an address was collected elsewhere, so check the live consent records before adding anyone to a mailing list.

## Store campaigns

The actions a store wants send the Entrant into the catalogue and bring something back.

- **Visit a product or collection page.** The Visit a Page action is in four out of five campaigns at a typical 78 completions % of Entrants (63,172 campaigns). Point it at the page the campaign is about, not the home page.
- **Answer a question with the product.** "Which item would you pick" or "paste the link to your cart or wishlist" as the required action. Question templates ran a typical 81 completions % of Entrants (4,875 campaigns, 976 businesses). The answers are the wishlist data a cart campaign exists to collect.
- **Pick your Prize.** A choice action with the three Prize options, so the preference is recorded on entry.
- **Subscribe with the store tag.** The Email Subscriptions action synced to the store's customer list with the campaign name as the tag, so the non-Winner code and the welcome series go to the right segment.
- **Refer a friend.** Where the platform can cap referrals per person, leave the cap off unless the Prize is small enough that referral farming pays. The friend lands on the store, and the referrer earns entries when the friend enters. A second reward when the friend buys is a mechanic the store can run through its own code, with no figure in the dataset.
- **Review purchase-linked entries before launch.** For order-number entries or bonus entries for buying, ask counsel whether the proposed mechanic can run in the relevant jurisdictions and whether a free entry route, particular weighting or other changes are needed. Configure the mechanic and terms according to that advice.

## Follows that lapse after the campaign (advice)

Common practice, nothing in the data covers it. This is about every Entrant who followed to enter, and almost
all of them lose. A Winner is one person among hundreds and their follow is a rounding error either way. What
the campaign data cannot see is whether the other several hundred are still following a month later, because it
records the Action completed at the moment of entry and never looks again.

Start by telling the reader that some of them leaving is normal. A follow given to enter a draw is a low price
someone paid for a ticket, and a share of those people were always going to go. A drop after the campaign is not
by itself a sign anything went wrong, and a reader bracing for zero churn is measuring against a number nobody
hits. What decides how big the drop is comes down to two things, and both are chosen before the campaign opens.

**Was there a reason to stay.** The feed goes quiet after the Winner is announced and the account stops being
why they are there. The welcome series, the Winner announcement and the non-Winner offer are the three reasons
to appear while the campaign still explains your presence, so plan them as part of the campaign.

**Was the Prize anything to do with you.** A Prize that only connects to the business through its price tag
pulls people who wanted the price tag. Choose a Prize your intended audience has a reason to want.
The data does not measure who stays after the campaign, so check follower retention with your own audience.

Then give them this.

- Measure it yourself, because it is the only way anyone finds out. Write down the follower count on the day the
  campaign opens, the day it closes and 30 days after, on each network you asked people to follow. Two campaigns
  in and the reader has a number for their own audience, which beats any benchmark.
- Ask for the follow on the network where the business actually posts. A follow on an account that goes quiet
  for six weeks is the one that lapses.
- Where the objective is a list, weight the email Action above the follow. An address is yours and a follow sits
  on somebody else's platform, which is worth saying to a reader whose whole plan rests on a follower count.
- Treat the follower count on the close day as the top of the range. The business keeps some share of those
  Entrants and nothing here says what share.
- Judge the campaign on the Entrants it drew and the addresses it captured, both of which are countable. A
  follower number read a month later mixes the campaign with everything else the account did since.

## Using what you built (advice)

The list is the point of the campaign, and it decays from the day the Winner is announced. The first 30 days decide whether it becomes an audience. All of this is practice, with nothing in the dataset to support it.

- **Welcome series.** Four messages: a welcome with the referral link within a day of entry, sent by the email provider when the sync lands, then the result and two brand messages over the fortnight after the draw. The first names the giveaway so nobody wonders who is writing. The rest do the job the giveaway could not: what the business sells, why anyone buys it, one reason to come back.
- **A separate segment.** Tag the giveaway group and keep it apart from customers and organic signups for at least 90 days. Its open and complaint rates run differently and will distort the reporting on the rest of the list if they are mixed.
- **A sunset rule.** Set it before the campaign opens. No opens in 60 or 90 days, one re-permission message, then out of the sending list. A giveaway list that is never pruned quietly damages deliverability for every other campaign.
- **Consent noted at capture.** Store what the Entrant agreed to, in what wording, on what date, alongside the address. That record is what answers a complaint or an audit later, and it cannot be reconstructed after the fact.
- **Followers and community members get the same treatment.** A first post that welcomes the new arrivals and says what the channel is for, then the normal cadence. A community with nothing happening in it loses the people a giveaway just brought.

The messages themselves, including the Winner announcement and the consolation offer to everyone who did not win, belong to giveaway-winner-communications.
</content>
