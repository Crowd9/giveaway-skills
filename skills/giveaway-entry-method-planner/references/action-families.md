# Action families

Extracted from the ordinary segment of the export (crypto, ambiguous and purchase-only campaigns removed). Platform-specific action types were mapped by hand to generic families so the advice works on any platform. Uptake is entries recorded on a method divided by the campaign's valid contestants, capped at 5, then the median across campaigns that offered the family. Entries are actions completed times the entry worth the organizer set, and entry worth is unknown in the export, so a value near 1 means most entrants did it only where the worth was 1. Repeatable actions (daily bonuses) and referrals (one entry per referred entrant, times worth) can exceed 1. IQR is the interquartile range, the middle half of campaigns between the 25th and 75th percentile. The 90th percentile is the level nine campaigns in ten sit below.

<!-- generated:entry_families -->
| Action family | Campaigns using it | Share of campaigns | Uptake median (IQR) | n with uptake |
|---|---|---|---|---|
| Visit a page or profile | 30,088 | 81% | 0.75 (0.55 to 0.92) | 134,195 |
| Follow or subscribe (free) | 23,721 | 64% | 0.47 (0.32 to 0.64) | 58,527 |
| Share, repost or refer | 21,093 | 57% | 0.22 (0.10 to 0.42) | 28,609 |
| Email or newsletter signup | 16,077 | 43% | 0.89 (0.69 to 1.02) | 17,875 |
| Bonus, loyalty or code | 14,905 | 40% | 0.66 (0.24 to 1.11) | 22,336 |
| Join a community | 7,742 | 21% | 0.43 (0.28 to 0.70) | 11,179 |
| Custom action (other) | 7,018 | 19% | 0.47 (0.22 to 0.82) | 15,641 |
| Answer a question or poll | 6,442 | 17% | 0.88 (0.59 to 1.02) | 9,450 |
| Post or create content | 5,756 | 16% | 0.24 (0.08 to 0.38) | 6,954 |
| Connect an account to enter | 4,144 | 11% | 0.46 (0.32 to 0.65) | 6,485 |
| Engage with a post | 4,101 | 11% | 0.48 (0.28 to 0.75) | 7,670 |
| Paid subscription | 1,904 | 5% | 0.05 (0.02 to 0.15) | 2,575 |
| Download or play | 1,766 | 5% | 0.35 (0.24 to 0.53) | 1,938 |
| Imported or offline entries | 717 | 2% | 0.05 (0.01 to 0.41) | 858 |

Methods per campaign: median 7, IQR 4 to 11, 90th percentile 17 (n=37,180). uptake = entries recorded on the method divided by the campaign's valid contestants, capped at 5 (repeatable methods can exceed 1). Family names are generic, and platform types were mapped to them by hand.
<!-- /generated -->

## Reading the table

- Visiting a page or profile is in four out of five campaigns and most entrants do it. It is cheap for the entrant and teaches little about them.
- Email signup, when offered, is completed by almost everyone who enters. It is the highest-uptake asset-producing action in the data.
- Free follows are the most common social action and are completed by about half of entrants. Community joins and content posting see lower uptake.
- Sharing and referring is offered in more than half of campaigns and records about a fifth of an entry per contestant, where each entry is a referred person times the entry worth. In the top tenth of campaigns the figure reaches 0.65. That is the only action whose entries are new people, so weight it and name the reward.
- Paid subscriptions and imported entries have very low uptake. Paid actions only work when the audience already intended to pay.

## SMS and messaging opt-in (advice, no dataset support)

A phone number or a messaging opt-in (SMS, WhatsApp, Messenger, a Telegram or Discord bot subscription) is an owned channel in the same family as an email signup: the entrant hands over a way to reach them that no platform can take away. The export carries no SMS action type, so there is no benchmark on this page for uptake, cost per number or anything else. Say that plainly when recommending it, and never borrow the email row as a stand-in.

What practice suggests, with no numbers attached:

- Treat it as a second asset alongside email. A number costs more to message and carries a harder consent regime.
- Ask for it only where the business already sends messages and has a sender identity registered where the region requires one.
- Keep it optional unless the messaging channel is the objective. It asks more of an entrant than an email field does.
- Collect the marketing consent at the same moment and in its own wording. A number given to enter a giveaway is not a number given for promotional messages.
- Where the region requires double opt-in, the confirmation message goes out at capture, and only confirmed numbers reach the list.

## Use by campaign size

Share of campaigns in each size band that offered at least one action from the family.

<!-- generated:entry_by_band -->
| Action family | 1k-2.5k | 2.5k-10k | 10k+ |
|---|---|---|---|
| Visit a page or profile | 80% | 82% | 82% |
| Follow or subscribe (free) | 64% | 64% | 66% |
| Share, repost or refer | 57% | 57% | 52% |
| Email or newsletter signup | 42% | 45% | 41% |
| Bonus, loyalty or code | 38% | 42% | 44% |
| Join a community | 22% | 20% | 17% |
| Answer a question or poll | 18% | 17% | 16% |
| Post or create content | 16% | 15% | 17% |
| Connect an account to enter | 12% | 10% | 7% |
| Download or play | 4% | 5% | 5% |
| Methods per campaign (median) | 7 | 7 | 7 |
<!-- /generated -->

The mix barely changes with size. Seven methods is the median at every size. Bigger campaigns are slightly less likely to ask for shares and slightly more likely to ask for follows and page visits.

## Limits

- Uptake counts completions the platform recorded. It cannot show whether a follow stayed or an email address was real.
- Families group actions across platforms whose rules differ. A follow on one network is verifiable, on another it is on trust.
- Every campaign passed the 1,000-contestant floor, so the table describes campaigns that reached an audience and nothing about what a mix does for a campaign that has not.

## Method count, sharing and email against contestants and conversion (extracted)

Impressions in the export are unique per day, so a visitor who returns counts again each day. Repeatable actions (daily bonus, loyalty, timed bonus) and long runs raise impressions per contestant and lower contestants per impression without any change in who entered. The clean subset removes campaigns with a repeatable action and any run over 14 days. Medians, ordinary segment, descriptive only. A vertical is a regex proxy on organizer, campaign and prize names.

<!-- generated:cmp_methods -->
| Entry methods, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| 1 to 3 | 3,526 | 2,213 | 1.11 | 50% | 2.0 | 2 |
| 4 to 6 | 3,404 | 2,153 (-3%) | 3.40 (+207%) | 37% (-25%) | 2.7 | 5 |
| 7 to 10 | 2,887 | 2,070 (-6%) | 5.09 (+359%) | 33% (-35%) | 3.1 | 8 |
| 11 or more | 1,819 | 1,759 (-21%) | 9.13 (+723%) | 31% (-38%) | 3.2 | 14 |
<!-- /generated -->

Contestants per impression falls with every band of methods and contestants fall about a fifth at 11 or more, in the clean subset and in every vertical with enough campaigns. Entries per entrant rise because there are more things to do. More methods means more actions per person and fewer people.

<!-- generated:cmp_share -->
| Share action, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| no share action | 8,075 | 2,189 | 3.28 | 42% | 2.4 | 5 |
| offers a share action | 3,561 | 1,869 (-15%) | 4.25 (+29%) | 31% (-27%) | 3.2 | 7 |
<!-- /generated -->

<!-- generated:cmp_email -->
| Email signup, clean subset | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |
|---|---|---|---|---|---|---|
| no email signup | 8,073 | 2,039 | 3.76 | 40% | 2.5 | 5 |
| offers email signup | 3,563 | 2,171 (+6%) | 3.34 (-11%) | 33% (-19%) | 3.1 | 6 |
<!-- /generated -->

Entries on the share action are referral entries: the platform's reporting terms define entries as actions completed times entry worth, and the Viral Share report counts a successful share as a user who entered as a direct result of it. Share uptake therefore measures referred entrants times the entry worth the organizer set, and the entry worth is unknown in the export. Campaigns offering a share action had fewer contestants and lower conversion in the clean subset, which describes the organizers who chose it. It cannot show whether the referrals added people who would otherwise have stayed away. An email signup cost about a fifth of conversion for a small gain in contestants. Both are prices worth paying only when the asset is the objective.
