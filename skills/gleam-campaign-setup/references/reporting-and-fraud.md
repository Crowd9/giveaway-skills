# Reporting and fraud in Gleam

Read from the official documentation on 9 September 2026.

## Reporting terms

[Common Reporting Terms](https://gleam.io/docs/competitions/data/common-reporting-terms)

- **Impressions**: individual views of the campaign, counted once per user per 24 hours.
- **Actions**: entry methods completed.
- **Entries**: actions completed multiplied by entry worth.
- **Users**: unique people who entered.
- **Conversion Rate**: users who entered after viewing. Across the 116,285 campaigns in `analysis/output/percentiles.json` (`scope.campaigns`), the typical figure is 26.9% (`bench.platform_average_conversion`).
- **Events**: optional metrics outside the incentivised actions, such as Facebook likes.

[Reporting Tab](https://gleam.io/docs/competitions/data/reporting-tab) shows the campaign over time with a date-range filter. The Actions report under Data & Reporting ranks completed actions by volume.

## Actions tab

[Actions Tab](https://gleam.io/docs/competitions/data/actions-tab)

Real-time list of every action with Who, Action, Details (form answers, tweet URL, handle, photos, custom fields), Where, When (in your user-settings time zone), Worth and Status. Status is Valid, Invalid or Winner. In exports each Details line becomes its own CSV column.

## Fraud filter

[Setup Tab](https://gleam.io/docs/competitions/setup/setup), Fraud Filter section

The filter analyses 20 or more attributes and marks suspicious entries Invalid for review before the draw. Invalid entries are hidden from reporting and Entrants are not told. Levels: Off, Low, Medium, High (default), Very High. CAPTCHA: Automatic, Always, Never. Gleam monitors campaigns and may adjust the level. Extra controls on other pages: Require login before actions and email or phone verification live on the User Details tab, Allowed Locations on the Setup tab.

**What an invalid share normally looks like (extracted).** The level a campaign ran on is not in the data, so
nothing here says what any level produced. What it does give a reader is the yardstick for their own number:

| Invalid entries as a share of all entries | Share |
|---|---|
| Lower quarter of campaigns | 1.1% |
| Typical | 4.2% |
| Upper quarter | 10.4% |
| Top tenth | 17.7% |
| Top hundredth | 38.4% |

So roughly one entry in twenty is marked Invalid in a typical campaign, and a campaign above about 18% is in the
noisiest tenth. That position cannot establish whether the filter is effective or which level to use. Campaigns
with a share action recorded 4.6% typical against 3.9% without one. Next, review your own Invalid entries
and any reports of legitimate Entrants being blocked before deciding whether a setting needs to change.

Scope: 107,109 campaigns from 16,490 businesses, with 100 or more Entrants that recorded at least one entry, on the ordinary population, so crypto, ambiguous and purchase-only campaigns are out. The filter level a campaign ran on is not in the data, so this is what the Invalid share looked like, never what any level produced. Source: `analysis/output/invalid_share.json`.

The documentation describes what the filter does to entries as they arrive. It does not say what happens to entries already collected when the level is changed part way through a campaign, so do not tell a user that raising the level will or will not re-screen what is already in. Say the docs do not cover it, and that the Actions tab is where the entries already collected get reviewed before the draw.

The same holds for what an Entrant sees. The documentation says a flagged entry is marked Invalid, hidden from
reporting, and that the Entrant is not told. It says nothing about whether the entry form lets them finish, what
they see on screen, or whether a CAPTCHA appears at that moment. An answer that describes the Entrant's
experience is inventing it. Describe what the business sees on the Actions tab and stop there.

## When suspicious Entries get through

Give the reader these next steps even when the first recommendation is to keep High. These are review practices, with controls verified against the [Pre-Entry tab](https://gleam.io/docs/competitions/setup/user-details) and [Actions tab](https://gleam.io/docs/competitions/data/actions-tab) on 10 October 2026.

- Review the Actions tab and save an export before changes. Compare suspicious Entries with the terms, the promotion schedule and legitimate Entrants reporting problems. A burst or shared location alone does not prove fraud. Record the reason for any exclusion before the draw.
- Check Allowed Locations against the countries already eligible in the terms. Consider Pre-Entry Login or email verification. Phone verification needs the documented Twilio integration. Test that eligible Entrants can still enter.
- If suspicious Entries continue, review the Fraud Level with support. Change one control at a time, note when, then compare subsequent suspicious Entries and reports of legitimate people blocked. A change in Invalid share alone cannot establish improvement.
- Review Entries already collected before drawing and check a selected Winner against the terms before announcing. Turning on verification mid-run leaves earlier unverified Entries valid. Do not promise a Fraud Level change rechecks old Entries.

Keep any benchmark sample sizes in one short source line, outside these steps. Include the missing filter-level note when using the Invalid-share comparison.

## Admin and test entries

[Admin / Test Entries](https://gleam.io/docs/competitions/post-campaign/test-entries)

An admin's own entries made before the competition starts are invalidated automatically, so entry methods can be tested. Testing an email provider integration needs those entries made valid by hand.

## Importing entries

The tips library notes that entries can be imported from a CSV so Winners can be drawn in Gleam for an audience managed elsewhere ([Advanced Tips](https://gleam.io/docs/competitions/tips/library), "Import External Entries With CSV").
