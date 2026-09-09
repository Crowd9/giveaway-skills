# Applying a prize recommendation in Gleam

Load this only when the user says they use Gleam or asks about it. Everything below was checked against the official documentation on 8 September 2026 (pages marked "Updated on July 27, 2026"). Re-verify before quoting plan limits, and never state a feature or limit that is missing from the linked page.

Start here: [Competitions documentation](https://gleam.io/docs/competitions).

## Where the prize goes

[Prize Tab](https://gleam.io/docs/competitions/setup/prizes)

- **Prize Area** holds the public competition title, the description and the layout. The description is where the prize is sold to entrants, and it supports basic HTML. Put the adapted prize description from the recommendation here, including value, eligibility and what is and is not included.
- **Prize Details** lists each prize, the number of winners for it, and an optional approximate retail value. Add one entry per distinct prize via "Add Prize". The docs note this list is used for drawing winners and is not displayed in the widget, so the description must also list the prizes.
- Total winners is the sum of winners across prize entries. Limits on prize count and winners depend on the plan. The page says so without listing figures, so check it for the user's plan.
- Layouts with images, image sliders and video depend on plan (the docs name Hobby and Business thresholds). Confirm on the page before advising.

## Mapping structures

| Recommended structure | In Gleam |
|---|---|
| One major prize | One prize entry, 1 winner |
| Several equal winners | One prize entry with winners set to N |
| Tiered prizes | One prize entry per tier, in order; when drawing "All Prizes" the first winner drawn gets the first prize listed, and so on ([Drawing Random Winners](https://gleam.io/docs/competitions/post-campaign/random-winners)) |
| Recurring winners | Draw at any time during the campaign from the Winners tab; date-range restriction on draws is described as a Business-plan-and-above control ([Daily / Weekly Winners](https://gleam.io/docs/competitions/post-campaign/daily-weekly-winners)) |
| Skill-based judging | [Selecting Manual Winners](https://gleam.io/docs/competitions/post-campaign/manual-winners); the docs note Gleam audits manual draws |

## Fulfillment notes from the docs

- Gleam does not contact winners automatically. The organizer announces and contacts them.
- Random draws use Random.org according to the docs.
- Winners must be drawn in line with Gleam's Terms of Service.

## Claims to avoid

- Do not quote plan prices, prize-count limits or winner limits from memory.
- Do not claim integrations, entry methods or features beyond the linked pages. The export used to build this skill shows historical entry methods. Current capability lives in the docs.
- If the user is on another platform, translate the same structure into that platform's terms and do not suggest switching.

For the full settings walk-through in tab order, use the `gleam-campaign-setup` skill.
