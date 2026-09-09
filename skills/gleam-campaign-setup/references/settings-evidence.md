# What the data says about Gleam settings

Extracted from the ordinary segment of the campaign export: 37,123 Gleam campaigns that reached 1,000 unique entrants, crypto and purchase-only campaigns removed. Uptake is the share of a campaign's unique contestants who completed a given action, worked out as completions of that action divided by unique contestants, then taken as the median across every campaign that offered it. An uptake of 0.51 means about half the entrants did it. A figure above 1 means the action was completed more than once per entrant on average, which happens on daily and repeatable actions. Action names are the export's generic names, which are history. Check the current name on the [How to Enter page](https://gleam.io/docs/competitions/setup/how-to-enter) before quoting one. Every figure describes what organizers chose and what their entrants did. No comparison group of failed campaigns exists, so none of it shows cause. Reproduce with `analysis/gleam_settings.py`.

## Completions per contestant by Gleam action

Actions offered by at least 300 campaigns, in order of how many campaigns offered them.

| Action | Campaigns | Median uptake | IQR |
|---|---|---|---|
| X Follows | 20,440 | 0.51 | 0.36 to 0.68 |
| Visit a Page | 20,205 | 0.72 | 0.48 to 1.00 |
| Instagram Profile Visits | 18,334 | 0.79 | 0.63 to 0.90 |
| Viral Shares | 16,708 | 0.13 | 0.08 to 0.25 |
| Email Subscriptions | 15,667 | 0.90 | 0.71 to 1.02 |
| Facebook visits | 14,889 | 0.76 | 0.60 to 0.88 |
| YouTube Channel Visits | 14,361 | 0.83 | 0.66 to 0.95 |
| Bonus | 12,594 | 1.01 | 0.41 to 1.96 |
| X Reposts | 7,899 | 0.40 | 0.28 to 0.56 |
| Custom Actions | 6,978 | 0.47 | 0.22 to 0.82 |
| Chat Members | 6,145 | 0.37 | 0.26 to 0.52 |
| Twitch Follows | 6,084 | 0.55 | 0.40 to 0.73 |
| TikTok Follows | 5,300 | 0.34 | 0.25 to 0.46 |
| Answer a Question | 4,326 | 0.86 | 0.52 to 1.01 |
| Secret Code | 3,854 | 0.25 | 0.08 to 0.54 |
| X Posts | 3,754 | 0.29 | 0.19 to 0.39 |
| Instagram Follows | 2,750 | 0.48 | 0.39 to 0.63 |
| TikTok Video Views | 2,431 | 0.47 | 0.34 to 0.63 |
| Telegram Channel Members | 2,041 | 0.85 | 0.64 to 0.96 |
| Pinterest Visits | 1,988 | 0.63 | 0.48 to 0.72 |
| Facebook Entries | 1,909 | 0.48 | 0.36 to 0.63 |
| Twitch Subscribers | 1,898 | 0.05 | 0.02 to 0.15 |
| Loyalty Bonuses | 1,846 | 0.47 | 0.29 to 0.65 |
| Single Choice List | 1,801 | 0.93 | 0.69 to 1.02 |
| App Downloads | 1,592 | 0.36 | 0.26 to 0.54 |
| Instagram Post Views | 1,568 | 0.62 | 0.40 to 0.79 |
| Facebook Likes | 1,287 | 0.37 | 0.28 to 0.44 |
| YouTube Entries | 1,173 | 0.72 | 0.45 to 1.01 |
| Reddit Visits | 1,125 | 0.72 | 0.52 to 0.84 |
| Instagram Entries | 968 | 0.46 | 0.32 to 0.58 |
| Facebook Post Views | 959 | 0.62 | 0.38 to 0.79 |
| Spotify follows | 914 | 0.28 | 0.18 to 0.42 |
| Podcast Subscriptions | 867 | 0.29 | 0.24 to 0.36 |
| LinkedIn Follow | 833 | 0.26 | 0.19 to 0.34 |
| Media Submits | 751 | 0.04 | 0.01 to 0.16 |
| Group Members | 689 | 0.41 | 0.28 to 0.58 |
| Multiple Choice Checkboxes | 673 | 0.90 | 0.64 to 1.02 |
| Blog Comment | 594 | 0.24 | 0.16 to 0.38 |
| Pinterest Entries | 556 | 0.36 | 0.19 to 0.44 |
| X Hashtag Posts | 551 | 0.36 | 0.23 to 0.55 |
| csv_import | 506 | 0.05 | 0.00 to 0.73 |
| X Entries | 498 | 0.42 | 0.29 to 0.66 |
| Instagram Comments | 489 | 0.33 | 0.23 to 0.43 |
| Gleam Subscriber | 434 | 0.61 | 0.53 to 0.69 |
| Snapchat | 430 | 0.26 | 0.16 to 0.38 |
| X Post Views | 406 | 0.60 | 0.49 to 0.73 |
| File Uploads | 402 | 0.10 | 0.02 to 0.34 |
| Submit URL | 400 | 0.15 | 0.06 to 0.43 |
| Spotify listen | 376 | 0.62 | 0.26 to 1.30 |
| Bluesky Follows | 337 | 0.24 | 0.17 to 0.33 |
| Threads Follows | 313 | 0.27 | 0.21 to 0.32 |
| Patreon Visits | 306 | 0.59 | 0.24 to 0.76 |

Reading it: visits and email signups are completed by most entrants. Follows sit near half. Viral Shares record 0.13 referred entries per contestant at the median, and a Viral Share entry is a referred person multiplied by entry worth, so the share of entrants who shared is lower still. Twitch Subscribers (a paid action) and Media Submits sit near 0.05. Bonus and Answer a Question run near one because they are quick and often gated at the top.

## Position in the action list

Campaigns with four or more actions. Median uptake by the action's position, split by family. Organizers put the action they care about first, and Gleam shows actions in list order, so this mixes ordering with choice.

| Family | 1st | 2nd | 3rd to 4th | 5th and later |
|---|---|---|---|---|
| Email signup | 1.00 (n=7,537) | 0.76 (n=2,105) | 0.70 (n=1,928) | 0.66 (n=3,644) |
| Visit or view | 0.97 (n=7,311) | 0.88 (n=12,772) | 0.80 (n=28,118) | 0.68 (n=86,044) |
| Follow, subscribe, join | 0.74 (n=4,436) | 0.62 (n=7,006) | 0.52 (n=15,131) | 0.39 (n=43,308) |
| Viral Share, refer | 0.16 (n=365) | 0.12 (n=1,836) | 0.12 (n=2,364) | 0.13 (n=11,191) |
| Everything else | 1.00 (n=10,424) | 0.53 (n=6,354) | 0.45 (n=12,605) | 0.36 (n=47,238) |

Every family loses completions down the list except Viral Share, which is flat and low wherever it sits. An email signup in first position was completed by the median entrant once. The same action fifth or later was completed by two thirds.

## Description length (clean subset)

Words in the prize description after stripping HTML. Clean subset: no repeatable action, 14 days or less.

| Words | n | Contestants | Contestants per impression | Entries per entrant |
|---|---|---|---|---|
| 0-25 | 3,706 | 2,163 | 41% | 3.04 |
| 26-75 | 4,230 | 2,024 | 35% | 3.82 |
| 76-150 | 2,800 | 2,052 | 38% | 4.16 |
| 151-300 | 862 | 1,988 | 38% | 3.61 |
| 301+ | 54 | 1,774 | 30% | 5.49 |

Short descriptions sit with the simplest campaigns, which also convert best, so the 41% for the shortest bucket says as much about the campaign as the copy. Over 300 words is rare and sits lowest on both counts.

## Custom action templates

| Template | Actions | Median uptake |
|---|---|---|
| visit | 60,610 | 0.72 |
| none | 15,641 | 0.47 |
| bonus | 14,304 | 1.01 |
| question | 5,639 | 0.86 |
| choose_option | 2,559 | 0.93 |
| multiple_choice | 849 | 0.90 |
| choose_image | 299 | 0.98 |

Custom actions with no template (a free-form instruction) were completed by under half of entrants. A visit template ran at 0.72 and the question and choice templates near 0.9.

## Throwaway account restriction

The restriction was on for 3,852 social actions and off for 43,810. Actions with it on recorded a median 0.37 completions per contestant against 0.47 with it off. That is consistent with the setting rejecting some accounts, and nothing here shows which of the rejected ones were real people.

## Visit action options

Visit actions can complete on click, after a delay, or after a question about the page. Median completions per contestant: complete on click 0.81 (41,291 actions), after a delay 0.75 (2,910), after a question 0.65 (4,742), option unset 0.72 (62,344). Delays of 5 to 10 seconds sat near 0.78, and 20 seconds at 0.54 on 170 actions. Visit a Page link options: a plain link 0.75 (49,435), page content shown as HTML inside the widget 0.50 (9,905), Open Graph preview 0.85 (1,270).

Nearly every Viral Share action carried custom share text (16,640 against 182 with the default), so the export cannot compare the two.

## Settings the export cannot see

Fraud level and CAPTCHA mode, require login before actions and the login types offered, email and phone verification, allowed locations, age restriction, language, entry worth, the mandatory flag, actions required, daily and interval settings, feature images and video, post-entry emails, redirects, pixels, webhooks and integrations are not in the export. Nothing in this reference speaks to them. The docs describe what they do, and the neutral skills' findings on invalid entries and opt-in apply where they overlap.

## Actions that top campaigns used, by vertical

The entry-method-planner skill holds the table of actions over-represented in the top fifth of campaigns by vertical, in Gleam action names (Twitch Subscribers and secret codes in gaming, single choice questions in technology, YouTube channel visits and Pinterest visits in home, and so on). Load `mix-by-objective.md` from that skill when the user asks which Gleam actions fit their industry. As a default mix in Gleam terms: one acquire action (Subscribe to an Email List, or Custom for account creation), one follow on the network the audience uses, one Single Choice Question or Answer a Question that collects something useful, one Visit a Page or secret code for exposure, and Viral Share for reach.

## Wording that showed up in the data

The entry-method-planner skill holds uptake by question type (detail capture 0.97, trivia 0.84, preference 0.75), by share copy traits, by visit destination (own site 0.96, YouTube 0.81, other sites 0.70) and by the newsletter description under the email action (none 0.95, any description 0.84). The idea generator holds title wording. Load them when the user is writing the action titles and the description.

## Settings the other skills already measured

- Email opt-in checkbox on: 0.89 email entries per contestant against 1.01 off. About one in ten entrants skips a visible checkbox (giveaway-entry-method-planner).
- Validated-answer question: median invalid share 17%, because wrong answers count as invalid (giveaway-entry-method-planner).
- Custom terms: written by 49% of campaigns (giveaway-winner-structure).
- Eleven or more actions: a fifth fewer contestants, conversion 31% against 50% for one to three (giveaway-entry-method-planner).
- Invalid entries: median 3.8% of entries, higher with Viral Share, Discord and retweet actions (giveaway-winner-structure).

## What this suggests for the setup, as advice

- Put the action that produces the asset first and make it the single mandatory action. First position was completed by the median entrant, fifth position by two thirds.
- Keep the list short. Everything after the fourth action is completed by a minority, and eleven or more actions came with fewer contestants.
- Set Viral Share expectations at one referred entry per eight entrants, and weight it accordingly. Its position does not matter.
- Use a question or choice template when you want an answer. Free-form custom actions lose half the entrants.
- Let visit actions complete on click, or after a delay of five to ten seconds. A post-visit question costs about a fifth of completions, and showing the page as HTML inside the widget costs a third against a plain link.
- Keep the description under 150 words and lead with eligibility and winner count, which the Gleam tips library also recommends.
- Leave the fraud level on High, the default, and review Invalid entries on the Actions tab before drawing. Expect a few percent to fall away.
- Turn on the opt-in checkbox when the list will be mailed. Expect about one in ten to skip it, and treat the rest as the mailable list.
