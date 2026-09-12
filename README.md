# Giveaway Skills

[![Checks](https://github.com/Crowd9/giveaway-skills/actions/workflows/checks.yml/badge.svg)](https://github.com/Crowd9/giveaway-skills/actions/workflows/checks.yml)
[![Licence MIT](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)

Plan, run and draw a giveaway your audience will trust, with an AI assistant that has read 167,072 real campaigns. Ten skills cover the whole job, from the idea to the draw to the review afterwards. No code to write. Install once, then ask in plain English.

Works with Claude Code, OpenAI Codex, Cursor and any assistant that reads `SKILL.md` files under the [Agent Skills specification](https://agentskills.io). Maintained by [Gleam](https://gleam.io), and the advice fits any giveaway platform.

Benchmarks come from 116,499 campaigns run by 17,633 businesses, in six size bands from 100 Entrants up. Every figure carries its sample size, and every finding describes what businesses chose, never what caused participation. The detail is in [Evidence Behind the Advice](#evidence-behind-the-advice).

## Install

Claude Code, as a plugin:

```bash
/plugin marketplace add Crowd9/giveaway-skills
```

```bash
/plugin install giveaway-skills
```

OpenAI Codex, Cursor and anything else that reads `.agents/skills`, with the skills CLI:

```bash
npx skills add Crowd9/giveaway-skills
```

Or copy a skill folder into the place your assistant loads skills from: `.claude/skills/` for Claude Code, `.agents/skills/` for Codex ([Codex skills docs](https://developers.openai.com/codex/skills)). Then ask: How long should my giveaway run?

If you keep the [marketingskills](https://github.com/coreyhaines31/marketingskills) product context file at `.agents/product-marketing.md`, every skill reads it first and skips the questions it answers.

## Skills

Run them in order for a whole campaign, or call one when you are stuck. Each hands off to the next.

| Skill | Ask it | You get |
|---|---|---|
| [Idea Generator](#idea-generator) | "Giveaway ideas for our 10k milestone" | Three concepts with hook, mechanic and prize direction, and the one to run |
| [Prize Picker](#prize-picker) | "Is a PS5 a good prize for us?" | A prize that attracts buyers, two alternatives, and a budget with shipping and duties |
| [Entry Method Planner](#entry-method-planner) | "How should people enter?" | A weighted entry list that builds the asset you want and stops before entrants drop off |
| [Timing and Duration](#timing-and-duration) | "How long should it run?" | A run length, a start date and a dated timeline from terms to delivery |
| [Winner Structure](#winner-structure) | "One winner or ten?" | Winner count, tiers, redraw rules and a terms draft for your country |
| [Promotion Plan](#promotion-plan) | "How do I promote it with no ad budget?" | A channel schedule with the posts and emails written, plus partner briefs and retargeting audiences |
| [Random Draw](#random-draw) | "Pick 3 winners from this CSV" | Winners from a public randomness beacon with an audit record anyone can check |
| [Winner Communications](#winner-communications) | "The winner hasn't replied" | Every message after the draw, from notification through the welcome series |
| [Results Review](#results-review) | "How did our giveaway do?" | Where your campaign ranks against campaigns its own size, and three changes for next time |
| [Gleam Campaign Setup](#gleam-campaign-setup) | "Walk me through the settings in Gleam" | A checklist in tab order with the documentation page beside every setting |

### Idea Generator

Three giveaway concepts that fit your business, your date and your goal, then the one to run.

- Hooks for the moment you have (launch, milestone, season, holiday, collaboration, daily series) and for moments you can manufacture
- Each concept in five lines: title, hook, mechanic, prize direction, and the asset it builds
- Campaign types measured (advent calendars, launches, drops, collaborations, series, cash, creator, charity and more) with Entrants, Conversion Rate and a value index for each
- Store campaigns for Shopify and similar: win your cart, win your wishlist, bundle builder, restock drop, gift card tiers
- What the campaigns that beat their prize money had in common, and the cheap prizes that drew crowds

> "We're a candle brand about to hit 10k followers, budget $300, ideas?"

[giveaway-idea-generator](skills/giveaway-idea-generator/SKILL.md)

### Prize Picker

A prize that pulls the people you want, and the budget worked out before you commit.

- Recommend mode when you have nothing yet, evaluate mode when you want a prize checked or improved
- Preferred option, two alternatives from different categories, and the tradeoffs between them
- Budget calculator with cost ratio, shipping, duties, tax, a substitute reserve and contingency
- ROI script: cost per Entrant, per email signup and per follow beside the benchmark for your industry, and the breakeven value per address
- Prize values by category and campaign size from 170,599 real Prize records, with sample sizes shown

> "Is a PS5 a good prize for our accounting software?"

[giveaway-prize-picker](skills/giveaway-prize-picker/SKILL.md)

### Entry Method Planner

The actions entrants take, weighted so the giveaway builds the list, following or community you will use.

- One required action that captures the asset, supporting actions on channels you already run, and where to stop
- Entry weights with a one-line reason for each, and what to leave out and why
- Completion rates by action family from 966,269 real entry actions, and the friction finding that every extra action costs Entrants
- Promotion rules for 17 networks, read from the source pages, including which allow tag-a-friend and which ban giveaways
- Email opt-in wording, age and region notes, and a review of an entry list you already have

> "We want email subscribers, we have Instagram and Klaviyo."

[giveaway-entry-method-planner](skills/giveaway-entry-method-planner/SKILL.md)

### Timing and Duration

A run length and a start date that fit the launch, the promotion plan and the shipping window.

- Recommended duration and start date with the reason
- A dated timeline: terms and assets, launch day, mid-campaign pushes, final 48 hours, draw, announce, fulfil
- Holiday benchmarks with a dated calendar of launch windows: Christmas, Black Friday, Easter, Halloween, back to school and more
- Every week of the year benchmarked, and whether being live over each holiday helped or hurt
- The recency finding: a campaign within 30 days of your last one converted at 41% against 32% for a first campaign

> "Shoe launches 14 October, want hype and emails."

[giveaway-timing-and-duration](skills/giveaway-timing-and-duration/SKILL.md)

### Winner Structure

How many winners, what tiers, and a process that holds up when a winner disappears or disputes the result.

- Winner counts and tiers sized to the budget after shipping
- Draw, contact, redraw, announcement and delivery rules
- Winner verification: the account signals that mark a fake, and what to do when a drawn entry fails
- A terms draft from a short questionnaire, 13 clauses with notes for Australia, the UK, the US, the EU and Canada
- Daily and series structures, skill-based judging, and what the data shows about how businesses split prizes

> "Budget $1,500 of our own $60 meal-prep sets, we want reviews."

[giveaway-winner-structure](skills/giveaway-winner-structure/SKILL.md)

### Promotion Plan

A schedule that fills the whole run, with the copy written.

- Schedule table by date, push, channel, format, owner and asset needed
- Post and story copy for every push in your brand voice
- Two email branches, list and entrants, each with subject, preview text and send time
- Profile prep, a fourteen-day calendar, and the replies for comments and DMs including the impersonation warning
- Partner and creator briefs, a paid recommendation with a cap, and what to reuse afterwards
- Retargeting and lookalike audiences built from the entrant list once the campaign closes, with winners and existing customers excluded

> "Runs 1 to 14 October, one partner post, no paid budget."

[giveaway-promotion-plan](skills/giveaway-promotion-plan/SKILL.md)

### Random Draw

Winners nobody can dispute, from a script that needs no account and no dependencies.

- Commits to your entrant list and rules before the random seed exists, so the draw cannot be steered
- Seed from a public randomness beacon (drand or NIST) or a value you publish, and a formula anyone can rerun
- Reads CSV, spreadsheet exports, one-per-line lists and comment exports from Instagram, TikTok and YouTube
- Deduplication, exclusions, entry weights, tiers, backups, and review lines for suspicious entry clusters
- Audit record with the input hash, seed, round and timestamp, and a verify command that refetches the beacon

> "Pick 3 winners from this CSV, weight by entries, exclude staff."

[giveaway-random-draw](skills/giveaway-random-draw/SKILL.md)

### Winner Communications

Every message after the draw, in send order, in your voice.

- Winner notification with a deadline, and the line that says you will never ask for payment or a login
- Verification request that asks only what the terms allow, and address collection with a privacy note
- Shipping and delivery updates, the public announcement, and the thank-you to everyone who did not win
- The welcome series for entrants who opted in, and the list hygiene pass that retires addresses that never engage
- Replies for the winner who stalls, the winner who disputes, and the entrant who says the draw was rigged

- For a store, the non-winner code: one single-use code per person, 7 to 14 day expiry, a larger code for referrers, tracked as the campaign's revenue line

> "Winner hasn't replied in five days."

[giveaway-winner-communications](skills/giveaway-winner-communications/SKILL.md)

### Results Review

Your finished campaign read against 116,499 others in its own size band, from 100 Entrants up, and what to change next time.

- A script that ranks twelve figures against all campaigns, your size band and your industry ("better than 70% of food and drink campaigns")
- What the campaign produced (addresses, follows, joins, referrals) against the yield for its size, and what each one cost
- Conversion read against the peer figure for your number of actions and your run length, with the impressions caveat applied
- Each entry action ranked against every campaign that offered the same action, so you see which one carried the campaign
- Three changes at most, each tied to a figure and to the skill that plans it
- A full report from your export in reporting-tab order: overview, traffic by channel, entry methods, the referral graph, audience, retention and ROI
- Reads a Gleam Actions export as is, and other platforms' exports through column matching or a mapping, including one-column-per-method exports

- For a store, the redemption count on the non-winner code as the revenue line, read at 14 and 90 days

> "1,800 entrants, 6,000 views, 9,000 entries, ran 14 days with 6 actions. How did we do?"

[giveaway-results-review](skills/giveaway-results-review/SKILL.md)

### Gleam Campaign Setup

For teams on Gleam: the plan from the other skills turned into settings, with the documentation cited for every one.

- The Setup, User Details, How to Enter, Prize and Post Entry tabs, read from the official pages in September 2026
- Mandatory and daily actions, actions required, entry intervals, free entry alternatives for paid actions
- Fraud filter levels, CAPTCHA modes, email and phone verification, allowed locations, age restriction, generated and custom terms
- Reporting definitions, the Actions tab, drawing winners, repeat winners, Quick Draws
- The Shopify app: page creation, Open Graph tags, syncing entrants to the customer list with a campaign tag, and the test before launch
- What Entrants did with every Gleam action across 116,499 campaigns, the drop-off down the action list, description length, and the config switches that showed up in the data
- Gleam's own tips library, attributed, beside that evidence

> "We use Gleam. Email mandatory, Instagram follow optional, US and Canada, 18+, one grand prize and five runner-ups. Walk me through the settings."

[gleam-campaign-setup](skills/gleam-campaign-setup/SKILL.md)

### Try It

Paste one of these into an assistant with the skills loaded:

```text
How long should my giveaway run? We sell running shoes, first campaign, launching in October.
```

An abbreviated version of what comes back:

> Two weeks, opening on a Monday and closing on a weekday evening in your customers' time zone.
>
> Half of all campaigns run between 7 and 29 days and the median is 14. Campaigns that finished under 250 Entrants ran 12 days, the ones over 10,000 ran 18. As a first campaign with no list to warm, plan for the shorter end.
>
> Entries per Entrant sit at 3.92 for an 8 to 14 day run and 4.07 for 15 to 30, so the second week buys repeat entries and little after that. Past two months the figure falls.
>
> Start day makes no measurable difference. Monday is the most common choice at 19% and Saturday the rarest at 7%, worth copying only because your own week is easier that way.
>
> One timing decision does move the numbers, and it is the next one. A campaign that starts within 30 days of your previous one drew 41% more Entrants than a first campaign, and 38% of viewers entered against 31%. Book the second before you launch this one.
>
> Next decision: the exact close date and time zone, which the promotion pushes hang off.

```text
Which entry actions should a skincare brand with 12k Instagram followers use to grow a Klaviyo list?
```

```text
Our giveaway closes Friday. Walk me through a draw our sponsor can verify.
```

Ask for a plan or ask it to check yours. Every answer states its assumptions, labels what came from the data, and ends with the next decision. The skills ship with the findings, so you never need the dataset, which is not part of this repository.

## Evidence Behind the Advice

Most giveaway advice is somebody's opinion. These skills are built on 116,499 real giveaways from 17,633 businesses, every one of which reached at least 100 Entrants, with 170,599 Prize records and 966,269 entry actions. Token airdrops and buy-to-enter raffles were set aside, so the benchmarks describe ordinary businesses giving away ordinary things.

Some of what that shows:

- **A first campaign drew 382 Entrants, and 25.5% of the people who saw it entered.** That is 17,247 businesses running their first. The all-campaign figure of 492 is set by the businesses that run giveaways constantly, so plan against 381.
- **Most campaigns are small and cheap.** 28% drew 100 to 250 Entrants on a stated Prize pool of about 120 USD, which is the biggest group in the data and the row a first campaign should budget against.
- **An email address cost about 0.39 USD of stated Prize value** in a campaign of 1,000 to 2,500 Entrants, and 0.16 USD in campaigns over 10,000.
- **Your industry sets that price.** Music and media captured an address for 0.09 USD of stated Prize value. Software paid 1.19.
- **Spending more on the Prize buys less than you would think.** Ten times the Prize value came with about 2.2 times the Entrants, and Prize value explains about 23% of the difference in Entrant counts.
- **What you give away matters more than what you spend on it.** For the same money, tech hardware drew 42% more crowd than typical and a subscription drew 49% less.
- **A small campaign works its audience as hard as a big one.** Entries per Entrant runs 4.46 in the smallest size band and 5.28 in the largest, so a low Entrant count is a reach problem.
- **Reach separates a big campaign from a small one.** The top fifth of campaigns had 25 times the Impressions of the bottom fifth, for a Conversion Rate about two points apart.
- **A long Action list costs you Conversion Rate.** Campaigns carrying 11 or more entry Actions converted 31% of viewers against 44% for a short list. They drew 17% more Entrants anyway.
- **Run the next one within 30 days.** Businesses that did drew 42% more Entrants than a first campaign, and converted better with it, 38% of viewers against 31%.
- **December is the busiest month, and it converts best.** Its campaigns converted 30.8% of viewers against 26.9% across the year, and the two weeks before Christmas get more people entering than any other week at 41%.
- **A Secret Code is the one Action that costs nothing.** Shown on a stream, in a newsletter or in store, it drew about 16% more Entrants at no cost to Conversion Rate.
- **A guitar outdraws a gift card by nearly three to one.** Music gear campaigns drew a typical 1,290 Entrants against 450 for a gift card or cash, and 93% more crowd than their Prize price predicts. Regulated goods draw the most of all at 2,133.
- **The Prizes that feel most generous sit at the bottom of the table.** A trip, a stay or a pair of tickets drew 40% less crowd than its price band predicts, and a subscription 49% less, the two lowest rows for crowd per Prize dollar.
- **The campaigns that beat their Prize money got an Entrant for 0.13 USD** of stated Prize value, against 0.42 across the data. 6,617 campaigns from 1,668 businesses drew at least three times the typical crowd for what they spent.
- **Four in five campaigns list a single Prize, and three in five give away exactly one unit of it.** More Winners is the lever most businesses never pull, and the campaigns that beat their Prize money pull it less, not more: 71% of them listed a single Prize unit against 61% of the rest.

Every finding describes what businesses chose, never what caused participation, because the dataset holds no failed campaigns to compare against. Cost figures use the stated Prize pool, which is what a business wrote down and the only cost the data holds, so real cost is often lower and promotion spend is invisible. Individual figures sit on slightly smaller bases where a campaign is missing the field being measured, and every one carries its own count in the references. The terms the figures use (contestant, entry, conversion, clean subset, value index, uptake) are defined in [GLOSSARY.md](GLOSSARY.md). The full findings, the exclusions and the limits are in [evidence-and-limitations.md](skills/giveaway-prize-picker/references/evidence-and-limitations.md). `analysis/output/` holds the aggregate files every figure is drawn from, and the scripts that produced them are not published.

## What These Skills Will Not Do

- Give legal advice. The winner-structure skill drafts terms from your answers, and a lawyer in your jurisdiction has to review that draft before you publish it.
- Run anything on your behalf. Nothing here posts, emails, schedules or changes a setting in any platform. You get the copy, the settings list and the commands, and you run them.
- Send your data anywhere. The draw and review scripts read your export on your own machine, have no dependencies and make no network calls except the public randomness beacon you choose for a seed.
- Promise results. The benchmarks describe what other campaigns did at the same size, and no skill will forecast your entrant count or your revenue.

## Issues and Support

Found a wrong number, a broken script or a platform rule that has changed? Open an issue. Used these for a giveaway? Open a discussion and tell us what happened. Support here is separate from Gleam's product support.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the conventions, including the rule that no customer data ever enters the repository.
