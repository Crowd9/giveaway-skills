# Drawing winners in Gleam

Read from the official documentation on 8 and 9 September 2026. Re-verify before quoting plan limits.

- **Winners tab.** Choose how many winners to draw and optionally restrict entries by date ([Drawing Random Winners](https://gleam.io/docs/competitions/post-campaign/random-winners)). With several prizes, drawing All Prizes assigns the first winner drawn to the first prize listed and so on, or draw per prize. The docs say random draws use Random.org.
- **Allow Repeat Winners** lets more than one entry from the same contestant win ([Allow Repeat Winners](https://gleam.io/docs/competitions/post-campaign/repeat-winners)). Leave it off for one prize per person.
- **Daily or weekly winners.** Winners can be drawn at any time during the campaign from the Winners tab ([Daily / Weekly Winners](https://gleam.io/docs/competitions/post-campaign/daily-weekly-winners)). Date-range restriction is described as a Business-plan-and-above control. Archiving entries after each draw starts the pool fresh while keeping the data on the Actions tab.
- **Manual winners** for judged contests, which the docs say Gleam audits ([Selecting Manual Winners](https://gleam.io/docs/competitions/post-campaign/manual-winners)).
- **Contacting winners.** The docs state Gleam does not contact winners automatically. Draws must follow Gleam's Terms of Service.
- **Quick Draws** for lists outside a campaign: [Random Name Picker](https://gleam.io/docs/competitions/quick-draws/random-name-picker) (one name per line, weighted with "Name, 5", name limits by plan as listed on the page), [Instagram Comment Picker](https://gleam.io/docs/competitions/quick-draws/instagram-comment-picker), [Competitions Live Draw](https://gleam.io/docs/competitions/quick-draws/competitions-live-draw), [Multiple Campaign Draw](https://gleam.io/docs/competitions/quick-draws/multiple-campaign-draw).

For a draw the organizer can prove outside the app, export valid entries and use the giveaway-random-draw skill. The audit note in that skill applies to Gleam draws too: record the date, the count drawn and the announcement.
