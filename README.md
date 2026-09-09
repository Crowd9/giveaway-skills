# Giveaway Skills

Plan, run and draw a giveaway your audience will trust, with an AI assistant that has read 37,180 real campaigns. Ten skills cover the whole job: the idea, the prize, the entry actions, the dates, the winners and terms, the promotion calendar, a draw anyone can verify, every message afterwards, a review of the results, and the Gleam settings when you run there.

No code to write. Install once, then ask in plain English. Works with Claude Code, OpenAI Codex, Cursor and any assistant that reads `SKILL.md` files under the [Agent Skills specification](https://agentskills.io).

Supported by [Gleam](https://gleam.io). The advice fits any giveaway platform, and the skills only bring up Gleam when you ask. Built to sit beside the [marketingskills library](https://github.com/coreyhaines31/marketingskills).

## Skills

Someone asks for a giveaway by Friday. The last one pulled 400 addresses that never opened an email, a follower called the draw rigged, and nobody could say what the prize should have been. These ten skills turn that into a plan you can defend, with every recommendation grounded in what 37,180 real campaigns did. Run them in order for a whole campaign, or call one when you are stuck. Each hands off to the next.

| Skill | Ask it | You get |
|---|---|---|
| [Idea Generator](#idea-generator) | "Giveaway ideas for our 10k milestone" | Three concepts with hook, mechanic and prize direction, and the one to run |
| [Prize Picker](#prize-picker) | "Is a PS5 a good prize for us?" | A prize that attracts buyers, two alternatives, and a budget with shipping and duties |
| [Entry Method Planner](#entry-method-planner) | "How should people enter?" | A weighted entry list that builds the asset you want and stops before entrants drop off |
| [Timing and Duration](#timing-and-duration) | "How long should it run?" | A run length, a start date and a dated timeline from terms to delivery |
| [Winner Structure](#winner-structure) | "One winner or ten?" | Winner count, tiers, redraw rules and a terms draft for your country |
| [Promotion Plan](#promotion-plan) | "How do I promote it with no ad budget?" | A channel schedule with the posts, four emails and a partner brief written |
| [Random Draw](#random-draw) | "Pick 3 winners from this CSV" | Winners from a public randomness beacon with an audit record anyone can check |
| [Winner Communications](#winner-communications) | "The winner hasn't replied" | Every message after the draw, from notification to the reply that ends a dispute |
| [Results Review](#results-review) | "How did our giveaway do?" | Where your campaign ranks against 37,000 others and your industry, the actions that pulled their weight, and three changes for next time |
| [Gleam Campaign Setup](#gleam-campaign-setup) | "Walk me through the settings in Gleam" | A checklist in tab order with the documentation page beside every setting |

### Idea Generator

Three giveaway concepts that fit your business, your date and your goal, then the one to run.

- Hooks for the moment you have (launch, milestone, season, holiday, collaboration, daily series) and for moments you can manufacture
- Each concept in five lines: title, hook, mechanic, prize direction, and the asset it builds
- Campaign types measured: advent calendars, launches, pre-orders and drops, collaborations, series, flash, cash, cart and wishlist, creator, community, charity and more, with contestants, conversion and a value-adjusted index for each
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
- Prize values by category and campaign size from 60,282 real prizes, with sample sizes shown
- A prize description you can paste, and Gleam setup help only when you ask for it

> "Is a PS5 a good prize for our accounting software?"

[giveaway-prize-picker](skills/giveaway-prize-picker/SKILL.md)

### Entry Method Planner

The actions entrants take, weighted so the giveaway builds the list, following or community you will use.

- One required action that captures the asset, supporting actions on channels you already run, and where to stop
- Entry weights with a one-line reason for each, and what to leave out and why
- Uptake by action family from 325,000 real entry actions, and the friction finding that every extra action costs entrants
- Promotion rules for 17 networks, read from the source pages, including which allow tag-a-friend and which ban giveaways
- Email opt-in wording, age and region notes, and a review of an entry list you already have

> "We want email subscribers, we have Instagram and Klaviyo."

[giveaway-entry-method-planner](skills/giveaway-entry-method-planner/SKILL.md)

### Timing and Duration

A run length and a start date that fit the launch, the promotion plan and the shipping window.

- Recommended duration and start date with the reason
- A dated timeline: terms and assets, launch day, mid-campaign pushes, final 48 hours, draw, announce, fulfil
- Holiday benchmarks: contestants, conversion and launch lead time for Christmas, Black Friday, the family days, Easter, Halloween, back to school and more, with a dated calendar of launch windows
- Seasonal calendar by region, with December's peak and carrier cut-offs flagged
- The recency finding: a campaign within 30 days of your last one drew 16% more entrants and converted a third better
- Risks named in advance: the quiet middle, holiday gaps, the wrong time zone on the close

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
- Four emails: launch, mid-campaign, last call, winners
- Partner and creator briefs, a paid recommendation with a cap, and what to reuse afterwards
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
- Replies for the winner who stalls, the winner who disputes, and the entrant who says the draw was rigged
- A contact log format so you can show what was sent and when

> "Winner hasn't replied in five days."

[giveaway-winner-communications](skills/giveaway-winner-communications/SKILL.md)

### Results Review

Your finished campaign read against 37,180 others of the same size, and what to change next time.

- A script that ranks contestants, impressions, conversion, actions and entries per entrant, pace per day, duration, prize value per contestant, email signups, referrals and follows by network against all campaigns, your size band and your industry ("better than 70% of food and drink campaigns")
- Your own history: this campaign beside your previous ones, the change, and how many it beat
- What the campaign produced (addresses, follows, joins, referrals) against the yield for its size, and what each one cost
- Conversion read against the peer figure for your number of actions and your run length, with the impressions caveat applied
- Each entry action ranked against every campaign that offered the same action, so you see which one carried the campaign
- Three changes at most, each tied to a figure and to the skill that plans it
- A full report from your export in the order of the reporting tabs: overview with insights and a heatmap, traffic by first-touch channel with UTM rollup, entry methods with completion rate and seconds per action, the referral graph with top sharers, audience by country and city, retention, and ROI on the costs you supply
- Reads a Gleam Actions export as is, and other platforms' exports through column matching or a mapping, including one-column-per-method exports

> "1,800 entrants, 6,000 views, 9,000 entries, ran 14 days with 6 actions. How did we do?"

[giveaway-results-review](skills/giveaway-results-review/SKILL.md)

### Gleam Campaign Setup

For teams on Gleam: the plan from the other skills turned into settings, with the documentation cited for every one.

- The Setup, User Details, How to Enter, Prize and Post Entry tabs, read from the official pages in September 2026
- Mandatory and daily actions, actions required, entry intervals, free entry alternatives for paid actions
- Fraud filter levels, CAPTCHA modes, email and phone verification, allowed locations, age restriction, generated and custom terms
- Reporting definitions, the Actions tab, drawing winners, repeat winners, Quick Draws
- What entrants did with every Gleam action across 37,123 campaigns, the drop-off down the action list, description length, and the config switches that showed up in the data
- Gleam's own tips library, attributed, beside that evidence

> "We use Gleam. Email mandatory, Instagram follow optional, US and Canada, 18+, one grand prize and five runner-ups. Walk me through the settings."

[gleam-campaign-setup](skills/gleam-campaign-setup/SKILL.md)

### Try It

Paste one of these into an assistant with the skills loaded:

```text
We sell running shoes online and want email subscribers who will buy. Budget $2,000. One big prize or ten small ones?
```

```text
Which entry actions should a skincare brand with 12k Instagram followers use to grow a Klaviyo list?
```

```text
Our giveaway closes Friday. Walk me through a draw our sponsor can verify.
```

Ask for a plan or ask it to check yours. Every answer states its assumptions, labels what came from the data, and ends with the next decision. You never need the dataset: the skills ship with the findings and paraphrased examples, and the private export is not part of this repository.

## Installing

Two commands and you are done. Pick the one that matches your assistant.

Claude Code, as a plugin:

```bash
/plugin marketplace add Crowd9/giveaway-skills
```

```bash
/plugin install giveaway-skills
```

OpenAI Codex, Cursor and other agents that read `.agents/skills`, with the skills CLI (checked 9 September 2026: it lists all ten skills and installs them into `.agents/skills`, and Codex loads them from there):

```bash
npx skills add Crowd9/giveaway-skills
```

Or copy a skill folder into the place your assistant loads skills from: `.claude/skills/` for Claude Code, `.agents/skills/` for Codex and the cross-agent standard. In Codex, run `/skills` or type `$` to pick one ([Codex skills docs](https://developers.openai.com/codex/skills)). 

These skills follow the conventions of the [marketingskills library](https://github.com/coreyhaines31/marketingskills) by Corey Haines and sit beside it. If you already keep its product context file at `.agents/product-marketing.md`, every skill reads it first and skips the questions it answers.

## Evidence Behind the Advice

Most giveaway advice is somebody's opinion. These skills are built on 37,180 real giveaways from 6,817 organizers, every one of which reached at least 1,000 entrants, with 60,282 prizes and 325,000 entry actions. Token airdrops and buy-to-enter raffles were set aside so the benchmarks describe ordinary businesses giving away ordinary things.

That data is what lets the skills say things like:

- A campaign that starts within 30 days of the organizer's previous one draws 16% more entrants and converts a third better, in every industry we could separate.
- Every extra entry action costs people. Campaigns with 11 or more actions convert at 31% against 50% for one to three, and lose a fifth of their entrants.
- Half of all campaigns had between 1,000 and 2,500 entrants and declared a prize pool of about 525 USD. The 10,000-plus campaigns declared 3,000 USD. Small businesses do not need big-brand budgets.
- Start weekday makes no difference at all. December is the busiest month and its campaigns still drew more entrants and converted better.
- A secret code is the only action that came with more entrants at no cost to conversion. Sharing actions, in this data, fed entries and left audiences where they were.

Every figure carries its sample size, and every finding describes what organizers chose, never what caused participation, because the export holds no failed campaigns to compare against. The full findings, the exclusions and the limits are in [evidence-and-limitations.md](skills/giveaway-prize-picker/references/evidence-and-limitations.md), and the analysis scripts that produced them are in `analysis/`.

## Issues and Support

Found a wrong number, a broken script or a platform rule that has changed? Open an issue on this repository. The skills are maintained here in the open and supported by the community and the maintainers, and they are separate from Gleam's product support.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the conventions: one folder per skill, quoted trigger phrases in the description, references loaded on demand, an eval file per skill, the style rules, and the rule that no customer data ever enters the repository.

## Repository Layout

```
README.md
CONTRIBUTING.md         how to add or change a skill
AGENTS.md               rules for agents editing this repo
VERSIONS.md             changelog and per-skill versions
LICENSE                 MIT
.claude-plugin/         plugin and marketplace manifests
scripts/validate.py     frontmatter, size, links, style and evals checks
skills/
  giveaway-prize-picker/
    SKILL.md
    references/
    evals/              evals.json, cases.md, style_check.py
  giveaway-entry-method-planner/
  giveaway-timing-and-duration/
  giveaway-winner-structure/
  giveaway-random-draw/     includes scripts/draw.py
  giveaway-idea-generator/
  giveaway-promotion-plan/
  giveaway-winner-communications/
  giveaway-results-review/  includes scripts/review.py
  gleam-campaign-setup/
analysis/
  analyze_export.py     regenerates analysis/output from a private export
  render_reference_tables.py  rewrites generated tables in every skill's references
  output/               committed aggregates (no customer data)
```
