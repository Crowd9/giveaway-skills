# Reporting and fraud in Gleam

Read from the official documentation on 9 September 2026.

## Reporting terms

[Common Reporting Terms](https://gleam.io/docs/competitions/data/common-reporting-terms)

- **Impressions**: individual views of the campaign, counted once per user per 24 hours.
- **Actions**: entry methods completed.
- **Entries**: actions completed multiplied by entry worth.
- **Users**: unique people who entered.
- **Conversion Rate**: users who entered after viewing. Across the campaigns behind these skills, the typical figure is about 28%.
- **Events**: optional metrics outside the incentivised actions, such as Facebook likes.

[Reporting Tab](https://gleam.io/docs/competitions/data/reporting-tab) shows the campaign over time with a date-range filter. The Actions report under Data & Reporting ranks completed actions by volume.

## Actions tab

[Actions Tab](https://gleam.io/docs/competitions/data/actions-tab)

Real-time list of every action with Who, Action, Details (form answers, tweet URL, handle, photos, custom fields), Where, When (in your user-settings time zone), Worth and Status. Status is Valid, Invalid or Winner. In exports each Details line becomes its own CSV column.

## Fraud filter

[Setup Tab](https://gleam.io/docs/competitions/setup/setup), Fraud Filter section

The filter analyses 20 or more attributes and marks suspicious entries Invalid for review before the draw. Invalid entries are hidden from reporting and Entrants are not told. Levels: Off, Low, Medium, High (default), Very High. CAPTCHA: Automatic, Always, Never. Gleam monitors campaigns and may adjust the level. Extra controls on other pages: Require login before actions and email or phone verification live on the User Details tab, Allowed Locations on the Setup tab.

The documentation describes what the filter does to entries as they arrive. It does not say what happens to entries already collected when the level is changed part way through a campaign, so do not tell a user that raising the level will or will not re-screen what is already in. Say the docs do not cover it, and that the Actions tab is where the entries already collected get reviewed before the draw.

## Admin and test entries

[Admin / Test Entries](https://gleam.io/docs/competitions/post-campaign/test-entries)

An admin's own entries made before the competition starts are invalidated automatically, so entry methods can be tested. Testing an email provider integration needs those entries made valid by hand.

## Importing entries

The tips library notes that entries can be imported from a CSV so Winners can be drawn in Gleam for an audience managed elsewhere ([Advanced Tips](https://gleam.io/docs/competitions/tips/library), "Import External Entries With CSV").
