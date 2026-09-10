# What the data says about Gleam settings

Extracted from the campaigns we could compare fairly in the export: campaigns that reached 1,000 or more unique Entrants, crypto and purchase-only campaigns removed. (35,668 campaigns.)

Every figure below is the share of a campaign's Entrants who completed a given action, worked out as completions of that action divided by Entrants, then taken as the typical value across every campaign that offered it, shown as a count % of Entrants with the decimal it came from in brackets. A figure of 51 per 100 means about half the Entrants did it. A figure above 100 per 100 means the action was completed more than once per Entrant on average, which happens on daily and repeatable actions.

Action names are the export's generic names, which are history. Check the current name on the [How to Enter page](https://gleam.io/docs/competitions/setup/how-to-enter) before quoting one. Every figure describes what businesses chose and what their Entrants did. No comparison group of failed campaigns exists, so none of it shows cause. (Reproduce with `analysis/gleam_settings.py`.)

## Starting point (extracted)

From the analysis's campaign-history match, covering campaigns with 100 or more Entrants, finance and crypto organizers excluded, an organizer's first campaign in the export more often starts blank than from a template.

| Starting point (organizer's first campaign) | Share |
|---|---|
| Gleam library template | 31% |
| Blank | 53% |
| Copied from outside the export | remainder |

(17,959 first campaigns, holding out 365 tagged as a copy of the organizer's own earlier campaign, a data anomaly.)

Templates in use are 68% Pro-tier across every tier measured. (7,143 campaigns, 5,069 businesses.)

Template use has fallen since 2020 while own-copy use has risen sharply, over the same years:

| Year | Template use | Own-copy use | Template campaigns | Template businesses |
|---|---|---|---|---|
| 2020 | 15% | 22% | 1,198 | 723 |
| 2026 | 6% | 66% | 8,061 | 2,250 |

By organizer tenure, a sixth-or-later campaign built from a template converts better than a sixth-or-later own copy:

| Sixth-or-later campaign, source | Conversion Rate | Campaigns | Businesses |
|---|---|---|---|
| Built from a template | 32.5% | 2,287 | 650 |
| Own copy | 26.8% | 57,605 | 2,790 |

Source: `analysis/output/templates.json` (`source_mix_first_campaign`, `template_tier_mix`, `template_share_by_year`, `template_by_organizer_tenure`).

## What share of Entrants completed each Gleam action

Actions offered by at least 300 campaigns, in order of how many campaigns offered them.

| Action | Campaigns | Typical share who did it, % of Entrants | Typical range, % of Entrants |
|---|---|---|---|
| X Follows | 19,433 | 50 (0.50) | 36 to 66 (0.36 to 0.66) |
| Visit a Page | 19,348 | 71 (0.71) | 48 to 99 (0.48 to 0.99) |
| Instagram Profile Visits | 18,044 | 79 (0.79) | 63 to 90 (0.63 to 0.90) |
| Viral Shares | 16,018 | 12 (0.12) | 7 to 23 (0.07 to 0.23) |
| Email Subscriptions | 15,463 | 90 (0.90) | 71 to 102 (0.71 to 1.02) |
| Facebook visits | 14,640 | 76 (0.76) | 60 to 88 (0.60 to 0.88) |
| YouTube Channel Visits | 14,099 | 83 (0.83) | 66 to 95 (0.66 to 0.95) |
| Bonus | 12,328 | 101 (1.01) | 41 to 195 (0.41 to 1.95) |
| X Reposts | 7,182 | 39 (0.39) | 27 to 53 (0.27 to 0.53) |
| Custom Actions | 6,695 | 47 (0.47) | 22 to 81 (0.22 to 0.81) |
| Twitch Follows | 5,998 | 55 (0.55) | 41 to 73 (0.41 to 0.73) |
| Chat Members | 5,734 | 36 (0.36) | 25 to 50 (0.25 to 0.50) |
| TikTok Follows | 5,276 | 34 (0.34) | 25 to 46 (0.25 to 0.46) |
| Secret Code | 3,803 | 25 (0.25) | 8 to 54 (0.08 to 0.54) |
| Answer a Question | 3,695 | 81 (0.81) | 47 to 101 (0.47 to 1.01) |
| X Posts | 3,655 | 29 (0.29) | 19 to 39 (0.19 to 0.39) |
| Instagram Follows | 2,750 | 48 (0.48) | 39 to 62 (0.39 to 0.62) |
| TikTok Video Views | 2,353 | 48 (0.48) | 35 to 63 (0.35 to 0.63) |
| Pinterest Visits | 1,972 | 63 (0.63) | 49 to 72 (0.49 to 0.72) |
| Twitch Subscribers | 1,884 | 5 (0.05) | 2 to 15 (0.02 to 0.15) |
| Facebook Entries | 1,842 | 49 (0.49) | 37 to 64 (0.37 to 0.64) |
| Loyalty Bonuses | 1,780 | 47 (0.47) | 29 to 66 (0.29 to 0.66) |
| Single Choice List | 1,659 | 93 (0.93) | 67 to 103 (0.67 to 1.03) |
| Telegram Channel Members | 1,622 | 83 (0.83) | 55 to 89 (0.55 to 0.89) |
| Instagram Post Views | 1,545 | 62 (0.62) | 40 to 79 (0.40 to 0.79) |
| App Downloads | 1,501 | 35 (0.35) | 26 to 49 (0.26 to 0.49) |
| Facebook Likes | 1,281 | 37 (0.37) | 29 to 44 (0.29 to 0.44) |
| YouTube Entries | 1,111 | 77 (0.77) | 47 to 102 (0.47 to 1.02) |
| Reddit Visits | 1,061 | 71 (0.71) | 51 to 83 (0.51 to 0.83) |
| Facebook Post Views | 947 | 62 (0.62) | 38 to 79 (0.38 to 0.79) |
| Instagram Entries | 925 | 47 (0.47) | 32 to 59 (0.32 to 0.59) |
| Spotify follows | 899 | 29 (0.29) | 18 to 42 (0.18 to 0.42) |
| Podcast Subscriptions | 865 | 29 (0.29) | 24 to 36 (0.24 to 0.36) |
| LinkedIn Follow | 767 | 25 (0.25) | 19 to 31 (0.19 to 0.31) |
| Media Submits | 683 | 4 (0.04) | 1 to 16 (0.01 to 0.16) |
| Group Members | 682 | 41 (0.41) | 28 to 58 (0.28 to 0.58) |
| Multiple Choice Checkboxes | 657 | 90 (0.90) | 64 to 102 (0.64 to 1.02) |
| Blog Comment | 592 | 24 (0.24) | 16 to 37 (0.16 to 0.37) |
| X Hashtag Posts | 508 | 34 (0.34) | 21 to 51 (0.21 to 0.51) |
| Pinterest Entries | 506 | 38 (0.38) | 18 to 44 (0.18 to 0.44) |
| csv_import | 495 | 5 (0.05) | 0 to 71 (0.00 to 0.71) |
| Instagram Comments | 484 | 33 (0.33) | 23 to 44 (0.23 to 0.44) |
| X Entries | 456 | 40 (0.40) | 28 to 59 (0.28 to 0.59) |
| Snapchat | 430 | 26 (0.26) | 16 to 38 (0.16 to 0.38) |
| Gleam Subscriber | 423 | 61 (0.61) | 52 to 68 (0.52 to 0.68) |
| X Post Views | 392 | 59 (0.59) | 49 to 71 (0.49 to 0.71) |
| File Uploads | 383 | 9 (0.09) | 2 to 33 (0.02 to 0.33) |
| Submit URL | 373 | 14 (0.14) | 5 to 38 (0.05 to 0.38) |
| Spotify listen | 370 | 70 (0.70) | 31 to 133 (0.31 to 1.33) |
| Bluesky Follows | 340 | 24 (0.24) | 17 to 33 (0.17 to 0.33) |
| Threads Follows | 315 | 27 (0.27) | 21 to 32 (0.21 to 0.32) |
| Patreon Visits | 304 | 59 (0.59) | 24 to 75 (0.24 to 0.75) |

Reading it: visits and email signups are completed by most Entrants (see table above). Follows sit near half. Viral Shares are the exception, a small share of Entrants refer someone, and a Viral Share entry is a referred person multiplied by entry worth, so the share of Entrants who actually shared is lower still. Twitch Subscribers, a paid action, and Media Submits sit lowest of all the actions measured. Bonus and Answer a Question run highest, because they are quick and often gated at the top.

## Position in the action list

Typical share of Entrants who completed an action, by the action's list position, split by family, analysis. Businesses put the action they care about first, and Gleam shows actions in list order, so this mixes ordering with choice.

| Family | 1st, % of Entrants | 2nd to 4th, % of Entrants | 5th and later, % of Entrants |
|---|---|---|---|
| Email signup | 101 (1.01, 9,521 campaigns) | 75 (0.75, 4,595 campaigns) | 67 (0.67, 4,470 campaigns) |
| Visit or view | 98 (0.98, 4,447 campaigns) | 84 (0.84, 27,832 campaigns) | 71 (0.71, 53,229 campaigns) |
| Follow, subscribe, join | 100 (1.00, 15,548 campaigns) | 78 (0.78, 49,352 campaigns) | 48 (0.48, 66,981 campaigns) |
| Viral Share, refer | 19 (0.19, 492 campaigns) | 14 (0.14, 6,050 campaigns) | 47 (0.47, 22,774 campaigns) |
| Content upload | 82 (0.82, 378 campaigns) | 29 (0.29, 1,050 campaigns) | 16 (0.16, 2,897 campaigns) |

Every family sees fewer Entrants complete it the further down the list it sits, except Viral Share, which is low in the top four and higher fifth or later, where long action lists with a mandatory share sit. An email signup or a follow in first position was completed by close to every Entrant, an email fifth or later by about two thirds of Entrants and a follow by about half. Source: `analysis/output/field_cuts.json` `uptake_by_family_and_position`.

## Description length

Words in the campaign description, analysis, among the campaigns we can compare fairly: no repeatable action, 14 days or less.

| Words | Campaigns | Businesses | Entrants | Conversion Rate | Actions per Entrant |
|---|---|---|---|---|---|
| none | 2,015 | 436 | 2,333 | 41% | 2.97 |
| 1-25 words | 2,643 | 856 | 2,123 | 40% | 3.88 |
| 26-75 words | 8,451 | 2,263 | 2,399 | 36% | 4.56 |
| 76-150 words | 6,924 | 1,721 | 2,638 | 37% | 5.36 |
| 151+ words | 2,705 | 829 | 2,585 | 34% | 5.28 |

No description and short descriptions sit with the simplest campaigns, which also see the highest share of viewers enter, so the 41% says as much about the campaign as the copy. Longer descriptions run with more actions and more actions per Entrant. Source: `analysis/output/field_cuts.json` `by_description_length`.

## Custom Actions templates

| Template | Actions | Typical share who did it, % of Entrants |
|---|---|---|
| visit | 58,747 | 71 (0.71) |
| none | 15,106 | 47 (0.47) |
| bonus | 13,999 | 101 (1.01) |
| question | 4,875 | 81 (0.81) |
| choose_option | 2,348 | 93 (0.93) |
| multiple_choice | 826 | 90 (0.90) |
| choose_image | 296 | 98 (0.98) |

Custom Actions with no template (a free-form instruction) were completed by under half of Entrants, the lowest of any template. Visit and question templates sit in the middle, and the choice templates highest (see table above).

## Throwaway account restriction

The throwaway account restriction lowers completion:

| Throwaway account restriction | Actions | Typical completion, % of Entrants |
|---|---|---|
| On | 3,286 | 36% (0.36) |
| Off | 41,289 | 46% (0.46) |

That is consistent with the setting rejecting some accounts, and nothing here shows which of the rejected ones were real people.

## Visit action options

Visit actions can complete on click, after a delay, or after a question about the page. Completing on click gets the most Entrants through. A post-visit question costs the most.

| Completion option | Typical completion, % of Entrants | Actions |
|---|---|---|
| Complete on click | 80% (0.80) | 57,868 |
| After a delay | 75% (0.75) | 4,016 |
| After a question | 65% (0.65) | 5,794 |
| Option unset | 71% (0.71) | 60,599 |

Visit a Page link options work the same way. A plain link outperforms embedding the page as HTML inside the widget. An Open Graph preview does best of all.

| Link option | Typical completion, % of Entrants | Actions |
|---|---|---|
| Plain link | 74% (0.74) | 47,702 |
| Page content as HTML in the widget | 50% (0.50) | 9,818 |
| Open Graph preview | 85% (0.85) | 1,227 |

Nearly every Viral Share action carried custom share text, not the default, so the export cannot compare the two. (16,640 with custom text against 182 with the default.)

## More settings that move how many Entrants complete an action

Read from the action's own configuration, counted per campaign. Each setting shows the same pattern: fewer choices or shorter waits keep completion higher, and X throwaway account restriction (per campaign) matches the direction of the per-action figure in Throwaway account restriction above.

| Setting | Option | Completion, % of Entrants (decimal) | Campaigns | Businesses |
|---|---|---|---|---|
| Email opt-in checkbox | Off | 93% (0.93) | 13,076 | 2,710 |
| Email opt-in checkbox | On | 86% (0.86) | 3,872 | 922 |
| Email opt-in checkbox | Auto | 72% (0.72) | 1,165 | 198 |
| Newsletter description | None | 95% (0.95) | 10,092 | 2,191 |
| Newsletter description | Long | 86% (0.86) | 6,881 | 1,514 |
| Newsletter description | Short | 76% (0.76) | 1,140 | 313 |
| Instagram visit delay | 5 seconds or less | 80% (0.80) | 72,067 | 6,355 |
| Instagram visit delay | 6 to 15 seconds | 71% (0.71) | 849 | 221 |
| Instagram visit delay | 16 seconds or more | 58% (0.58) | 417 | 74 |
| X throwaway account restriction (per campaign) | Open | 68% (0.68) | 87,436 | 7,382 |
| X throwaway account restriction (per campaign) | Restricted | 64% (0.64) | 8,619 | 1,246 |
| Share text length | 60 to 140 characters | 41% (0.41) | 23,207 | 5,345 |
| Share text length | Over 140 characters | 13% (0.13) | 4,934 | 1,401 |
| Share text length | Default text | 28% (0.28) | 1,006 | 464 |
| Secret Code length | 3 characters | 68% (0.68) | 176 | 72 |
| Secret Code length | 4 to 13 characters (open-ended) | 19–35% | – | – |
| Secret Code length | 8 characters, fixed-length pattern | 8% (0.08) | 209 | 51 |
| Actions required | 1 to 7 (range) | 73–102% | – | – |
| Actions required | 7 (exact) | 73% (0.73) | 1,464 | 637 |
| Actions required | 8 | 42% (0.42) | 857 | 344 |

Actions required is the exception worth flagging on its own: completion holds fairly steady through 7 required actions, then drops by roughly half at 8.

Email opt-in checkbox on or set to auto, by organizer country. Poland leads by a wide margin. Malaysia barely uses it.

| Organizer country | Opt-in checkbox on or set to auto | Campaigns | Businesses |
|---|---|---|---|
| Poland | 70% | 850 | 41 |
| United States | 34% | 22,662 | 3,324 |
| Australia | 16% | 2,997 | 733 |
| Malaysia | 3% | 175 | 20 |

Source: `analysis/output/field_cuts.json` key `config_cuts`, `analysis/output/indicators.json` key `email_optin_checkbox_by_country`.

## Terms by country

Custom terms text share by country: campaigns whose organizer wrote their own terms wording. English-speaking markets write their own far more often than India or Brazil.

| Organizer country | Wrote custom terms | Campaigns | Businesses |
|---|---|---|---|
| Australia | 52% | 6,433 | 1,406 |
| United Kingdom | 44% | 15,716 | 1,847 |
| United States | 38% | 58,843 | 9,105 |
| India | 5% | 6,010 | 873 |
| Brazil | 4% | 5,860 | 563 |

Wording families inside that text turn up at different rates by country. Void where prohibited and no purchase necessary are classic US sweepstakes phrases. Platform disclaimer wording is an Australian habit, and permit-or-licence wording is almost entirely Australian, with Malaysia the only real exception. Age wording differs by phrasing more than by presence: Canada is the one country in the table where "age of majority" outruns a stated "18+", the reverse of the United States, United Kingdom and Australia, where "18+" is the more common phrase.

| Wording family | Country | Share |
|---|---|---|
| Void where prohibited | United States | 28% |
| No purchase necessary | United States | 34% |
| Platform disclaimer | Australia | 37% |
| Permit or licence | Australia | 5.6% |
| Permit or licence | Malaysia | 4.3% |
| Skill or judged | Australia | 8% |
| "Age of majority" phrasing | Canada | 26% |
| "18+" phrasing | Canada | 23% |

Governing law named in the generated terms points to a country other than the organizer's own far more in some markets than others. Organizer country here comes from IP, so a genuinely foreign-registered entity reads as a mismatch too.

| Organizer country | Governing law names a different country | Campaigns | Businesses |
|---|---|---|---|
| China | 94% | 2,608 | 165 |
| Japan | 76% | 6,469 | 290 |
| Singapore | 74% | 4,720 | 350 |
| United States | 9% | 58,128 | 8,998 |

The generated terms set the draw window and the Winner response window at 7 days on the typical campaign in every country in the table.

Source: `analysis/output/country_cuts.json` key `terms_by_country`, `analysis/output/indicators.json` keys `governing_law_mismatch_by_country` and `age_wording_in_custom_terms_by_country`.

## Australian games of skill

Australian campaigns that carry a skill or judged signal in their name, Prize copy or terms run fewer entry methods, ask for fewer actions, get less to enter, run longer, and carry a bigger stated Prize pool than Australia's other campaigns.

| | Skill/judged signal | No skill/judged signal |
|---|---|---|
| Campaigns | 631 | 5,802 |
| Businesses | 126 | 1,349 |
| Entry methods (typical) | 2 | 6 |
| Actions per Entrant | 1.8 | 3.4 |
| Entry rate | 18% | 30% |
| Duration (typical) | 18 days | 15 days |
| Prize pool (typical) | $2,135 | $699 |

By industry, media and entertainment publishers account for about half of the skill or judged campaigns, ahead of electronics and tech, gaming, and nonprofit and community.

| Industry | Campaigns (of the 631 skill/judged) |
|---|---|
| Media and entertainment | 320 |
| Electronics and tech | 51 |
| Gaming | 48 |
| Nonprofit and community | 33 |

Most of these 631 still carry a plain generated-terms selection method reading "random draw," with no judging step named: 82%. Only 17% name a judged, best-answer or vote method in that field, and a further share describe a two-stage draw, finalists chosen at random and then judged, a method Gleam's generated terms support directly.

Source: `analysis/output/country_cuts.json` keys `skill_against_other` and `australia_skill_industries`. The selection-method share is computed from the same base view as `skill_against_other` (name, incentive text, custom terms and the generated selection-method field), not itself a stored key.

## Settings the analysis added

The September 2026 export carries entry worth, the mandatory flag, actions required, the paid flag, loyalty tiers, integrations, language, allowed and excluded countries, the generated terms settings and the organizer's country. Aggregates live in `analysis/output/field_cuts.json`. Headlines on campaigns with 1,000 or more Entrants:

- Entry worth: `entry_count` is the number of completions of the action, not a worth-weighted total, so no division by worth is needed. Making an action mandatory raises how many Entrants complete it, and typically lowers the cost per completion too, scoped to campaigns with every Prize valued (about a third of the export). Email was mandatory on 41% of the campaigns offering it.

  | Email action | Completion, % of Entrants (decimal) | Actions |
  |---|---|---|
  | Typical campaign (any) | 90% (0.901) | 18,113 |
  | Mandatory | 102% (1.023) | – |
  | Optional | 76% (0.759) | – |

  | Action | Campaign size (Entrants) | Cost optional | Cost mandatory | Save | Campaigns (optional / mandatory) | Businesses (optional / mandatory) |
  |---|---|---|---|---|---|---|
  | Email | 1,000–2,500 | $0.44 | $0.39 | 11% | 5,903 / 3,650 | 1,447 / 1,104 |
  | Email | 2,500–10,000 | $0.51 | $0.25 | 52% | 3,698 / 2,830 | 829 / 800 |
  | X Follow | 1,000–2,500 | $0.63 | $0.65 | close, no save | – | – |
  | X Follow | 2,500–10,000 | $0.64 | $0.59 | – | 10,101 / 1,056 | 1,374 / 268 |
  | X Follow | 10,000+ | $0.44 | $0.26 | – | 2,812 / 394 | 351 / 71 |
  | Discord_join | 1,000–2,500 | $0.72 | $0.94 | optional cheaper | – | – |
  | Discord_join | 2,500–10,000 | $0.61 | $0.77 | mandatory cheaper | – | – |

  Follow_x follows the email pattern from 2,500 Entrants up, not below it. Discord_join is not a rule either way, its mandatory cost is cheaper at one size and pricier at the other. (Figures from `asset_yield.json`'s `yield_by_asset_and_mandatory` cut.)
- Email provider: connecting a provider does not raise completions, so connect for the workflow, not the number.

  | Email provider | Completion, % of Entrants (decimal) | Campaigns |
  |---|---|---|
  | No integration | 92% (0.915) | 11,039 |
  | MailChimp | 86% (0.858) | 2,545 |
  | Klaviyo | 96% (0.96) | 1,917 |
  | MailerLite | 100% (0.998) | 243 |
  | ConstantContact | 86% (0.858) | 186 |
- Marketing stack: businesses running Klaviyo offer email far more often, and are far more often on Shopify too.

  | | Runs Klaviyo | Doesn't run Klaviyo |
  |---|---|---|
  | Campaigns | 1,659 | 30,397 |
  | Businesses | 444 | 5,054 |
  | Offers email | 63% | 46% |
  | On Shopify | 29% | 4% |
- Country rules: 24% of campaigns restrict entry by country. Restricted campaigns offer email far more often, and restricting costs little on the share who enter.

  | | Restricted by country | Open |
  |---|---|---|
  | Campaigns | 12,990 | 41,796 |
  | Businesses | 2,736 | 8,862 |
  | Offers email | 52% | 23% |
  | Entry rate | 29% | 30% |
- Paid actions: campaigns that carry a paid action run more methods and more actions per Entrant than campaigns without one, with a lower share of viewers entering.

  | | Has a paid action | No paid action |
  |---|---|---|
  | Campaigns | 1,637 | 53,149 |
  | Businesses | 664 | – |
  | Methods (typical) | 10 | 8 |
  | Actions per Entrant | 5.31 | 4.86 |
  | Entry rate | 26% | 30% |
- Language: English dominates the export and runs the longest campaigns with the most email asks. Portuguese and German campaigns are both one-day runs, but German offers email far more often. Spanish and French sit in between on both duration and email.

  | Language | Share of campaigns | Campaigns | Businesses | Duration (typical) | Email offered |
  |---|---|---|---|---|---|
  | English | 96% | 52,259 | – | 14 days | 31% |
  | Portuguese | – | 563 | 68 | 1 day | under 1% |
  | German | – | 390 | 55 | 1 day | 19% |
  | Spanish | – | 457 | 119 | 10 days | 16% |
  | French | – | 425 | 100 | 11 days | 27% |
- Terms: the generated terms set the draw and the Winner response window at 7 days on most campaigns. 37% of organizers wrote fully custom terms. Governing law runs US, GB and IN as the top three, then AU and CA.

  | Governing law | Campaigns |
  |---|---|
  | US | 19,658 |
  | GB | 4,240 |
  | IN | 3,163 |
- Build lead: 24% of campaigns show a creation time after the start date, so the field reads as a modified-at time on those rows, not a true build lead. (12,927 campaigns, 3,776 businesses.) Among the rest, lead time barely moves the share who enter.

  | Build lead | Entry rate |
  |---|---|
  | Same day | 30% |
  | 1 to 2 days | 29% |
  | 3 to 7 days | 28% |
  | 8 days or more | 28% |
- Viral Share clicks: campaigns with a Viral Share action see share clicks equal to 47% of Impressions, and the typical campaign sees about 174 share clicks per 100 Entrants (1.743 per Entrant).
- Landing: most Impressions land on the hosted gleam.io page, not on an embed or the directory listing. Traffic source is dominated by direct, ahead of organizer sites, Meta, and Gleam's own pages. Of the Impressions carrying a UTM tag, about a third trace to email newsletters and a fifth to Meta.

  | Landing page type | Share of Impressions |
  |---|---|
  | Hosted gleam.io page | 63% |
  | Embed | 36% |
  | Directory listing | 0.4% |

  | Traffic source | Share of Impressions |
  |---|---|
  | Direct | 52% |
  | Organizer sites | 7.8% |
  | Meta | 7.6% |
  | Gleam pages | 7.5% |
  | YouTube | 4.7% |
  | X | 4.7% |
  | Giveaway directories | 3.3% |
  | Search | 2.6% |

  (11% of Impressions carry a UTM tag. Of those, 35% trace to email newsletters and 20% to Meta.)
- Hosted share: campaigns landing almost entirely on the hosted page get the most to enter, over the shortest run, with the least email offered. Campaigns that lean on an embed run longer, offer email far more, and get less to enter. This is the largest split in the export, with no comparison group to show what caused it.

  | Landing mix | Campaigns | Businesses | Entry rate | Duration | Email offered |
  |---|---|---|---|---|---|
  | 90% or more hosted | 36,817 | 8,400 | 34% | 10 days | 16% |
  | Embed-mostly / 10–50% hosted | 7,444 + 7,125 | 1,568 + 1,660 | 21–24% | 18–27 days | 57–67% |

Still not in the export: fraud level and CAPTCHA mode, require login and the login types, email and phone verification, age restriction, daily and interval settings, feature images and video, post-entry emails, redirects, pixels and webhooks. The docs describe what they do.

## Actions that top campaigns used, by vertical

The entry-method-planner skill holds the table of actions over-represented in the top fifth of campaigns by vertical, in Gleam action names (Twitch Subscribers and Secret Code in gaming, single choice questions in technology, YouTube Channel Visits and Pinterest Visits in home, and so on). Load `mix-by-objective.md` from that skill when the user asks which Gleam actions fit their industry. As a default mix in Gleam terms: one acquire action (Subscribe to an Email List, or Custom for account creation), one follow on the network the audience uses, one Single Choice Question or Answer a Question that collects something useful, one Visit a Page or secret code for exposure, and Viral Share for reach.

## Wording that showed up in the data

The entry-method-planner skill holds the share of Entrants who completed it by question type, by share copy traits, by visit destination and by the newsletter description under the email action (see table). The idea generator holds title wording. Load them when the user is writing the action titles and the description.

| Measure | Category | Completion, % of Entrants |
|---|---|---|
| Question type | Detail capture | 97 |
| Question type | Trivia | 84 |
| Question type | Preference | 75 |
| Visit destination | Own site | 96 |
| Visit destination | YouTube | 81 |
| Visit destination | Other sites | 70 |
| Newsletter description (email action) | None | 95 |
| Newsletter description (email action) | Any description | 84 |

## Settings the other skills already measured

- Email opt-in checkbox on: 89% of Entrants complete the email action against 101 of every 100 off. About one in ten Entrants skips a visible checkbox (giveaway-entry-method-planner). That gap is wider than the 93% against 86% in the table above because it compares like with like on campaign size and industry, where the table above pools every campaign. Quote whichever base the answer is about and say which one it is.
- Validated-answer question: a typical 17% of entries come back invalid, because wrong answers count as invalid (giveaway-entry-method-planner).
- Custom terms: written by 49% of campaigns (giveaway-winner-structure).
- Eleven or more actions: a quarter fewer Entrants, 32% of viewers enter against 48% for one to three (giveaway-entry-method-planner).
- Invalid entries: a typical 3.8% of entries, higher with Viral Share, Discord and retweet actions (giveaway-winner-structure).

## What this suggests for the setup, as advice

- Put the action that produces the asset first and make it the single mandatory action. Position matters a lot: an email action or a follow completed by nearly every Entrant in first position drops off sharply by fifth position or later (see the position table above). See giveaway-entry-method-planner's `references/mix-by-objective.md` for the fuller asset list and the ratios by campaign size.
- Making that action mandatory is worth it beyond the completion count: it also tends to lower the cost per completion (see the entry-worth table above). Email saves the most as campaign size grows. Follow_x follows the same pattern from 2,500 Entrants up. Discord_join's mandatory cost is not a rule, it moves in opposite directions across the two sizes tested.
- Keep the list short. Everything after the fourth action is completed by a minority, and eleven or more actions came with fewer Entrants.
- Set Viral Share expectations at one referred entry per eight Entrants, and weight it accordingly. Its position does not matter. Viral Share can be capped at a maximum number of referred users and is unlimited by default. Leave it off unless the Prize is small enough that referral farming pays, then cap it and check the referral graph before the draw.
- Use a question or choice template when you want an answer. Free-form custom actions lose half the Entrants.
- Let visit actions complete on click, or after a delay of five to ten seconds. A post-visit question costs about a fifth of completions, and showing the page as HTML inside the widget costs a third against a plain link.
- Keep the description under 150 words and lead with eligibility and Winner count, which the Gleam tips library also recommends.
- Leave the fraud level on High, the default, and review Invalid entries on the Actions tab before drawing. Expect a few percent to fall away.
- Turn on the opt-in checkbox when the list will be mailed. Expect about one in ten to skip it, and treat the rest as the mailable list.
