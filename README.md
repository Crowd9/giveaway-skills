# Giveaway Skills

[![Checks](https://github.com/Crowd9/giveaway-skills/actions/workflows/checks.yml/badge.svg)](https://github.com/Crowd9/giveaway-skills/actions/workflows/checks.yml)
[![Licence MIT](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)

Plan, run and draw a giveaway your audience will trust, with an AI assistant that has read 35,668 real campaigns. Ten skills cover the whole job: the idea, the prize, the entry actions, the dates, the winners and terms, the promotion calendar, a draw anyone can verify, every message afterwards, a review of the results, and the Gleam settings when you run there. No code to write. Install once, then ask in plain English. Works with Claude Code, OpenAI Codex, Cursor and any assistant that reads `SKILL.md` files under the [Agent Skills specification](https://agentskills.io). Maintained by Crowd9 Pty Ltd, the company behind [Gleam](https://gleam.io), and the advice fits any giveaway platform, with Gleam raised only when you ask.

Behind the advice sit 6,402 organizers, 58,000 prizes and 314,000 entry actions, from campaigns that all reached at least 1,000 entrants.
Every figure carries its sample size, and every finding describes what organizers chose, never what caused participation. The detail is in [Evidence Behind the Advice](#evidence-behind-the-advice).

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

Someone asks for a giveaway by Friday. The last one pulled 400 addresses that never opened an email, a follower called the draw rigged, and nobody could say what the prize should have been. These ten skills turn that into a plan you can defend, with every recommendation grounded in what real campaigns did. Run them in order for a whole campaign, or call one when you are stuck. Each hands off to the next.

| Skill | Ask it | You get |
|---|---|---|
| [Idea Generator](#idea-generator) | "Giveaway ideas for our 10k milestone" | Three concepts with hook, mechanic and prize direction, and the one to run |
| [Prize Picker](#prize-picker) | "Is a PS5 a good prize for us?" | A prize that attracts buyers, two alternatives, and a budget with shipping and duties |
| [Entry Method Planner](#entry-method-planner) | "How should people enter?" | A weighted entry list that builds the asset you want and stops before entrants drop off |
| [Timing and Duration](#timing-and-duration) | "How long should it run?" | A run length, a start date and a dated timeline from terms to delivery |
| [Winner Structure](#winner-structure) | "One winner or ten?" | Winner count, tiers, redraw rules and a terms draft for your country |
| [Promotion Plan](#promotion-plan) | "How do I promote it with no ad budget?" | A channel schedule with the posts, the emails for people who entered and people who have not, the replies for comments and DMs, a partner brief, and the retargeting audiences to build once it closes |
| [Random Draw](#random-draw) | "Pick 3 winners from this CSV" | Winners from a public randomness beacon with an audit record anyone can check |
| [Winner Communications](#winner-communications) | "The winner hasn't replied" | Every message after the draw, from notification through the welcome series and list hygiene for everyone who did not win |
| [Results Review](#results-review) | "How did our giveaway do?" | Where your campaign ranks against 35,000 others and your industry, the actions that pulled their weight, and three changes for next time |
| [Gleam Campaign Setup](#gleam-campaign-setup) | "Walk me through the settings in Gleam" | A checklist in tab order with the documentation page beside every setting |

### Idea Generator

Three giveaway concepts that fit your business, your date and your goal, then the one to run.

- Hooks for the moment you have (launch, milestone, season, holiday, collaboration, daily series) and for moments you can manufacture
- Each concept in five lines: title, hook, mechanic, prize direction, and the asset it builds
- Campaign types measured: advent calendars, launches, pre-orders and drops, collaborations, series, flash, cash, cart and wishlist, creator, community, charity and more, with contestants, conversion and a value index for each
- Store campaigns for Shopify and similar: win your cart up to a cap, win your wishlist, pick your prize, bundle builder, restock drop, gift card tiers, with the cart and wishlist figures from the data
- What the campaigns that beat their prize money had in common, and the cheap prizes that drew crowds
- Formats to avoid for your business, from the list of tired and risky ones
- Which hooks organizers use most, from campaign titles across the dataset, with December's crowding called out

> "We're a candle brand about to hit 10k followers, budget $300, ideas?"

[giveaway-idea-generator](skills/giveaway-idea-generator/SKILL.md)

### Prize Picker

A prize that pulls the people you want, and the budget worked out before you commit.

- Recommend mode when you have nothing yet, evaluate mode when you want a prize checked or improved
- Preferred option, two alternatives from different categories, and the tradeoffs between them
- Budget calculator with cost ratio, shipping, duties, tax, a substitute reserve and contingency
- ROI script: cost per contestant, per email signup and per follow beside the benchmark for your industry, and the breakeven value per address
- Prize values by category and campaign size from 58,000 real prizes, with sample sizes shown
- A prize description you can paste, and Gleam setup help only when you ask for it

> "Is a PS5 a good prize for our accounting software?"

[giveaway-prize-picker](skills/giveaway-prize-picker/SKILL.md)

### Entry Method Planner

The actions entrants take, weighted so the giveaway builds the list, following or community you will use.

- One required action that captures the asset, supporting actions on channels you already run, and where to stop
- Entry weights with a one-line reason for each, and what to leave out and why
- Uptake by action family from 314,000 real entry actions, and the friction finding that every extra action costs entrants
- Promotion rules for 17 networks, read from the source pages, including which allow tag-a-friend and which ban giveaways
- Email opt-in wording, age and region notes, and a review of an entry list you already have

> "We want email subscribers, we have Instagram and Klaviyo."

[giveaway-entry-method-planner](skills/giveaway-entry-method-planner/SKILL.md)

### Timing and Duration

A run length and a start date that fit the launch, the promotion plan and the shipping window.

- Recommended duration and start date with the reason
- A dated timeline: terms and assets, launch day, mid-campaign pushes, final 48 hours, draw, announce, fulfil
- Holiday benchmarks: contestants, conversion and launch lead time for Christmas, Black Friday, the family days, Easter, Halloween, back to school and more, with a dated calendar of launch windows
- Every week of the year benchmarked: share of launches, contestants and conversion, and whether being live over each holiday helped or hurt
- Seasonal calendar by region, with December's peak and carrier cut-offs flagged
- The recency finding: a campaign within 30 days of your last one converted at 41% against 32% for a first campaign
- Risks named in advance: the quiet middle, holiday gaps, the wrong time zone on the close
- The season plan for a store: list build before Black Friday, the gift guide campaign in early December, the New Year restart, with the weeks that convert best behind each

> "Shoe launches 14 October, want hype and emails."

[giveaway-timing-and-duration](skills/giveaway-timing-and-duration/SKILL.md)

### Winner Structure

How many winners, what tiers, and a process that holds up when a winner disappears or disputes the result.

- Winner counts and tiers sized to the budget after shipping
- Draw, contact, redraw, announcement and delivery rules
- Winner verification: entry checks, the account signals that mark a fake, proof scaled to the prize, and what to do when a drawn entry fails
- A terms draft from a short questionnaire, 13 clauses with notes for Australia, the UK, the US, the EU and Canada
- Daily and series structures, skill-based judging, and what the data shows about how organizers split prizes
- Review of a structure you already have, with gaps and fixes

> "Budget $1,500 of our own $60 meal-prep sets, we want reviews."

[giveaway-winner-structure](skills/giveaway-winner-structure/SKILL.md)

### Promotion Plan

A schedule that fills the whole run, with the copy written.

- Schedule table by date, push, channel, format, owner and asset needed
- Post and story copy for every push in your brand voice
- Two email branches: launch, mid and last call for the list, a welcome with the referral link for entrants the day they enter, and the winners email to everyone opted in, each with subject, preview text and send time
- Profile prep, a fourteen-day calendar that keeps the rest of the feed running, and the replies for the comments and DMs that land, including the impersonation warning
- Partner and creator briefs, a paid recommendation with a cap, and what to reuse afterwards
- Retargeting and lookalike audiences built from the entrant list once the campaign closes, with winners and existing customers excluded
- A fix for "nobody is entering" mid-campaign

> "Runs 1 to 14 October, one partner post, no paid budget."

[giveaway-promotion-plan](skills/giveaway-promotion-plan/SKILL.md)

### Random Draw

Winners nobody can dispute, from a script that needs no account and no dependencies.

- Commits to your entrant list and rules before the random seed exists, so the draw cannot be steered
- Seed from a public randomness beacon (drand or NIST) or a value you publish, and a formula anyone can rerun
- Reads CSV, spreadsheet exports, one-per-line lists and comment exports from Instagram, TikTok and YouTube
- Deduplication, exclusions, entry weights, tiers, backups, and review lines for plus-address clusters, disposable domains and runs of numbered handles
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
- A contact log format so you can show what was sent and when

- For a store, the non-winner code: one single-use code per person, 7 to 14 day expiry, a larger code for referrers, tracked as the campaign's revenue line

> "Winner hasn't replied in five days."

[giveaway-winner-communications](skills/giveaway-winner-communications/SKILL.md)

### Results Review

Your finished campaign read against 35,668 others of the same size, and what to change next time.

- A script that ranks contestants, impressions, conversion, actions and entries per entrant, pace per day, duration, prize value per contestant, email signups, referrals and follows by network against all campaigns, your size band and your industry ("better than 70% of food and drink campaigns")
- Your own history: this campaign beside your previous ones, the change, and how many it beat
- What the campaign produced (addresses, follows, joins, referrals) against the yield for its size, and what each one cost
- Conversion read against the peer figure for your number of actions and your run length, with the impressions caveat applied
- Each entry action ranked against every campaign that offered the same action, so you see which one carried the campaign
- Three changes at most, each tied to a figure and to the skill that plans it
- A full report from your export in the order of the reporting tabs: overview with insights and a heatmap, traffic by first-touch channel with UTM rollup, entry methods with completion rate and seconds per action, the referral graph with top sharers, audience by country and city, retention, and ROI on the costs you supply
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
- What entrants did with every Gleam action across 35,668 campaigns, the drop-off down the action list, description length, and the config switches that showed up in the data
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
> Half of all campaigns run between 8 and 31 days and the median is 16. The ones that finished under 2,500 entrants ran 15 days, the ones over 10,000 ran 20. As a first campaign with no list to warm, plan for the shorter end of that.
>
> The 8 to 14 day band holds 20% of campaigns and the 15 to 30 band 30%. Entries per contestant sit at 4.4 and 4.62 across those two bands, so the second week buys you repeat entries and very little after that. Past two months the figure falls.
>
> Start day makes no measurable difference on any measure. Monday is the most common choice at 18.7% of campaigns and Saturday the rarest at 6.4%, which is a habit worth copying only because your own week is easier that way. Close day is flat too, so set the close for the hours you can answer questions in.
>
> One timing decision does move the numbers, and it is the next one. A campaign that starts within 30 days of your previous one converted at 41% against 32% for a first campaign. Book the second one before you launch this one.
>
> Next decision: the exact close date and time zone, which the promotion pushes hang off.

```text
Which entry actions should a skincare brand with 12k Instagram followers use to grow a Klaviyo list?
```

```text
Our giveaway closes Friday. Walk me through a draw our sponsor can verify.
```

Ask for a plan or ask it to check yours. Every answer states its assumptions, labels what came from the data, and ends with the next decision. You never need the dataset: the skills ship with the findings and paraphrased examples, and the private export is not part of this repository.

## Evidence Behind the Advice

Most giveaway advice is somebody's opinion. These skills are built on 35,668 real giveaways from 6,402 organizers, every one of which reached at least 1,000 entrants, with 58,000 prizes and 314,000 entry actions. Token airdrops and buy-to-enter raffles were set aside so the benchmarks describe ordinary businesses giving away ordinary things.

That data is what lets the skills say things like:

- A campaign that starts within 30 days of the organizer's previous one converts at 41% against 32% for a first campaign, on the clean subset (n=7,007 and 1,103).
- Every extra entry action costs people. Campaigns with 11 or more actions convert at 32% against 48% for one to three, and draw a quarter fewer entrants (1,760 against 2,305).
- More than half of all campaigns had between 1,000 and 2,500 entrants and declared a prize pool of about 520 USD. The 10,000-plus campaigns declared 3,000 USD. Small businesses do not need big-brand budgets.
- Start weekday makes no difference at all. December is the busiest month (n=4,253) and its campaigns still drew more entrants and converted better, 2,342 at 33% against 2,211 at 28% overall. The week before Christmas converts best of any week in the year at 54%, being live over Christmas or New Year came with 6% to 7% better conversion than matched campaigns, and Black Friday week came with 16% worse.
- A secret code is the only action that came with more entrants at no cost to conversion (2,380 against 2,102, both at 38%, n=588). Sharing actions, in this data, fed entries and left audiences where they were.
- The top fifth of campaigns had nine times the impressions of the bottom fifth at the same conversion (35,505 against 4,047, both 28%). Reach separates them. History compounds too: after a campaign over 5,000 entrants, 61% of an organizer's next campaigns reached 5,000 again, against 12% after a smaller one.
- Advent calendars lead every campaign type on both size and conversion. Launches sit below the median and refer more. The campaigns that beat their prize money three times over were run by repeat organizers with a secret code, a Twitch or Discord audience and one hero prize, and 129 of them did it with a prize under 250 USD.
- Music and media organizers declared the least prize money per entrant and per address captured, gaming the least per referred entry, and software the most on every count. Brazil and Sweden convert highest of the large organizer countries, the UK sits at 31%.

Every figure carries its sample size, and every finding describes what organizers chose, never what caused participation, because the export holds no failed campaigns to compare against. The terms the figures use (contestant, entry, conversion, clean subset, value index, uptake) are defined in [GLOSSARY.md](GLOSSARY.md). The full findings, the exclusions and the limits are in [evidence-and-limitations.md](skills/giveaway-prize-picker/references/evidence-and-limitations.md), and the analysis scripts that produced them are in `analysis/`.

## Defaults for the Gleam Editor

The same analysis also writes `defaults/`, machine-readable defaults for the Gleam AI campaign editor keyed to its campaign fields, with sample sizes on every value. See [defaults/README.md](defaults/README.md).

## What These Skills Will Not Do

- Give legal advice. The winner-structure skill drafts terms from your answers, and a lawyer in your jurisdiction has to review that draft before you publish it.
- Run anything on your behalf. Nothing here posts, emails, schedules or changes a setting in any platform. You get the copy, the settings list and the commands, and you run them.
- Send your data anywhere. The draw and review scripts read your export on your own machine, have no dependencies and make no network calls except the public randomness beacon you choose for a seed.
- Promise results. The benchmarks describe what other campaigns did at the same size, and no skill will forecast your entrant count or your revenue.

## Issues and Support

Found a wrong number, a broken script or a platform rule that has changed? Open an issue on this repository. Used these for a giveaway? Open a discussion and tell us what happened. The skills are maintained here in the open and supported by the community and the maintainers, and they are separate from Gleam's product support.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the conventions: one folder per skill, quoted trigger phrases in the description, references loaded on demand, an eval file per skill, the style rules, the repository layout, and the rule that no customer data ever enters the repository.
