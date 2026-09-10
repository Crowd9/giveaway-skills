# Campaign setup in Gleam

Read from the official documentation on 9 September 2026 (pages marked "Updated on July 27, 2026" unless stated). Link the page beside any setting you quote. Where a page says a feature depends on plan without naming figures, say so and stop there.

Start: [Competitions overview](https://gleam.io/docs/competitions/setup/overview). A competition belongs to a site, drafts autosave, and a previous competition can be copied with most settings and actions so only the Prize and terms need updating.

## Setup tab

[Setup Tab](https://gleam.io/docs/competitions/setup/setup)

- **Name** appears in the Entrant email and sets the default landing page URL.
- **Start and end dates** can be changed at any point during the contest, with hours and minutes available.
- **Timezone** is set per competition, independent of the account default.
- **Hide X ways to enter** and **Hide total entry count** are checkboxes.
- **Event Mode** is for shared devices at a live event only. It drops cookies, logs users out on refresh and relaxes the fraud filter. The page warns against using it on a normal campaign.
- **Fraud Filter** invalidates suspicious entries automatically from 20 or more attributes. Invalid entries show as Invalid on the Actions tab for review before drawing, do not appear in reporting, and Entrants are never told. **CAPTCHA** can be Automatic, Always or Never. **Fraud Level** has five settings:

| Fraud Level | What it does |
|---|---|
| Off | Accepts same-network and same-device entries with no CAPTCHA |
| Low | Adds CAPTCHA and login verification |
| Medium | Low plus VPN and data-centre protection |
| High | The default |
| Very High | Adds more aggressive Cloudflare challenges |

Gleam may adjust a campaign's level if it blocks legitimate Entrants or lets too many suspicious ones through.
- **Terms and Conditions** are generated automatically from the campaign setup with editable fields: sponsor name and address, governing law country, privacy policy link, selection method (Random Draw by default, or Judges Panel, Popular Vote, Most Entries, other), contact window (7 days by default), claim window (7 days by default), additional terms. **Custom terms** written from scratch are available on Hobby and above. A "read the terms" checkbox can be added to the User Details form.
- **Allowed Locations** restricts by country (not city) using MaxMind. Restricted visitors see a message.
- **Age Restriction** works through the Minimum Age field in User Details, set required, with a DD/MM/YYYY format.
- **Languages**: 27 supported, applied to the widget and emails. Text typed into actions is not translated. **Widget Text Overrides** replace any widget string in YAML form.

## User Details tab

[User Details tab](https://gleam.io/docs/competitions/setup/user-details) (updated 5 August 2026)

- The details form pops up after the first action. Social logins prefill what the network provides (Facebook gives email, Twitter does not).
- **Minimum Age** takes a date of birth in UK or US format, or a checkbox declaration.
- **Login With**: default shows actions first and asks for login after the first one. **Require login before actions** hides the actions until the user logs in, which the page notes can reduce fraud, for example by forcing Facebook or Instagram login. With it on, **Automatic Entry** awards an entry for logging in through a bonus action added on save. Email-only login shows the details form first. Single or multiple social login types can be offered.
- **Build Competition Subscriber List** (Pre-Entry tab) adds a checkbox so Entrants can opt in to future campaign emails. Promotion emails skip people who already entered and carry unsubscribe links. **Capture Subscribers After Competition Ends** shows a name and email form on the ended campaign.
- **Email Verification** sends a 4-digit code before entry. **Phone Number Verification** does the same by SMS through a Twilio integration under Site Settings. Turning either on mid-campaign leaves earlier unverified entries valid.
- **Custom User Details fields** are on Business and above, and sync to email providers and webhooks. Connect the email provider integration before launch and test it with an admin entry (admin entries made before the start are invalidated automatically, see the reporting reference), so the Entrant emails in giveaway-promotion-plan trigger during the run.
- The subscribe checkbox is marketing consent and covers nothing else. Entering the giveaway is its own consent, so an Entrant who leaves the box unticked still gets the entry confirmation and the Winner announcement and no marketing. Where the Entrant's country requires confirmed opt-in, configure double opt-in in the email provider, since the checkbox on its own is a single opt-in.

## How to Enter tab

[How to Enter Tab](https://gleam.io/docs/competitions/setup/how-to-enter)

- Actions are added from the supported list and reordered by drag and drop. The page lists the current actions. Quote from it, not from memory.
- **Mandatory actions** must be completed before non-mandatory ones unlock. With more than one mandatory action, completing any one of them unlocks the rest. A single mandatory action with an expandable state auto-expands.
- **Actions required** locks an action until a set number of others are done. Available on Bonus, Custom, Promote a Campaign, Question, Choose Image, Single and Multiple Choice Question, Secret Code, Subscribe to an Email List, Visit a Page and Viral Share.
- **Daily actions** reset at midnight in the competition's timezone. Follows cannot repeat. **Entry interval** (Single, Hourly, Daily, Unlimited) exists on some actions such as photo submissions and secret codes, and also governs automatic imports.
- **Actions that require payment**: tick "A purchase or donation is required" on Eventbrite, Twitch Subscriber Bonus and Custom Actions to offer a free entry alternative. It appears in the terms for users in the listed countries only, awards the same entries as the paid route, and the page suggests asking a Winner for proof of residence.

## Prize tab

[Prize Tab](https://gleam.io/docs/competitions/setup/prizes)

- **Prize Area** holds the public title, description (basic HTML) and layout. **Prize Details** lists each Prize with its number of Winners and an optional retail value, used for drawing and not shown in the widget, so the description must also list the Prizes. Total Winners is the sum across Prizes. Prize and Winner counts and image layouts depend on plan, and the page names no figures.

## Post Entry tab

[Post Entry Tab](https://gleam.io/docs/competitions/setup/post-entry)

- **Post entry email** goes to every Entrant by default, in the campaign language, and can be disabled. **Custom post-entry emails** with tokens (campaign name, landing page URL, Contestant first and full name, current and prospective entries, viral share URL, unsubscribe) are on Business.
- **Post Entry Redirect** sends the user to a URL once all actions are complete. It ignores Viral Share, so do not make Viral Share the last action when using it.
- **Pixel Tracking**: Adroll, Facebook Pixel and Conversions API (on load, conversion, or both, deduplicated by event id), Google Ads, Tune, Twitter.
- **Post-Entry Webhook** sends entry data to your endpoint, Premium plans only.
