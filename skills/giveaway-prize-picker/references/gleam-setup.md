# Applying a Prize recommendation in Gleam

Load this only when the user says they use Gleam or asks about it. Everything below was checked against the official documentation on 8 September 2026 (pages marked "Updated on July 27, 2026"). Re-verify before quoting plan limits, and never state a feature or limit that is missing from the linked page.

Start here: [Competitions documentation](https://gleam.io/docs/competitions).

## Where the Prize goes

[Prize Tab](https://gleam.io/docs/competitions/setup/prizes)

- **Prize Area** holds the public competition title, the description and the layout. The description is where the Prize is sold to Entrants, and it supports basic HTML. Put the adapted Prize description from the recommendation here, including value, eligibility and what is and is not included.
- **Prize Details** lists each Prize, the number of Winners for it, and an optional approximate retail value. Add one entry per distinct Prize via "Add Prize". The docs note this list is used for drawing Winners and is not displayed in the widget, so the description must also list the Prizes.
- Total Winners is the sum of Winners across Prize entries. Limits on Prize count and Winners depend on the plan. The page says so without listing figures, so check it for the user's plan.
- Layouts with images, image sliders and video depend on plan (the docs name Hobby and Business thresholds). Confirm on the page before advising.

## Mapping structures

| Recommended structure | In Gleam |
|---|---|
| One major Prize | One Prize entry, 1 Winner |
| Several equal Winners | One Prize entry with Winners set to N |
| Tiered Prizes | One Prize entry per tier, in order; when drawing "All Prizes" the first Winner drawn gets the first Prize listed, and so on ([Drawing Random Winners](https://gleam.io/docs/competitions/post-campaign/random-winners)) |
| Recurring Winners | Draw at any time during the campaign from the Winners tab; date-range restriction on draws is described as a Business-plan-and-above control ([Daily / Weekly Winners](https://gleam.io/docs/competitions/post-campaign/daily-weekly-winners)) |
| Skill-based judging | [Selecting Manual Winners](https://gleam.io/docs/competitions/post-campaign/manual-winners); the docs note Gleam audits manual draws |

## Fulfillment notes from the docs

- Gleam does not contact Winners automatically. The organizer announces and contacts them.
- Random draws use Random.org according to the docs.
- Winners must be drawn in line with Gleam's Terms of Service.

## Claims to avoid

- Do not quote plan prices, Prize-count limits or Winner limits from memory.
- Do not claim integrations, Entry Methods or features beyond the linked pages. The dataset used to build this skill shows historical Entry Methods. Current capability lives in the docs.
- If the user is on another platform, translate the same structure into that platform's terms and do not suggest switching.

For the full settings walk-through in tab order, use the `gleam-campaign-setup` skill.
