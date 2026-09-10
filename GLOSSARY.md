# Glossary

The terms the skills and their references use, in one place. Each skill defines the ones it needs on first use, and this page is the long form.

## Gleam's Own Words

These are the terms the Gleam dashboard uses. The skills write them exactly as the app writes them, with capitals, so a reader can match the advice to what is on their screen.

- **Impressions.** Individual views of the campaign, counted once per person per 24 hours.
- **Actions.** Entry Methods completed.
- **Entries.** Actions completed multiplied by entry worth. A Viral Shares action worth 3 gives 3 Entries for 1 Action.
- **Users.** Unique people who entered. These pages usually say entrants, and say Users when pointing at the dashboard figure.
- **Conversion Rate.** Users who entered after viewing.
- **Events.** Optional metrics outside the incentivised Actions.
- **Entry Method.** One thing an entrant is asked to do. The app names each one, from Email Subscriptions to Viral Shares, and the skills use those names unchanged.

Everything the app does not name is written plainly: entrants, businesses, campaigns, and every rate as a count per 100 entrants.

## Campaign Counts

- **The dataset.** Every figure in these skills is extracted from Gleam's own campaign records. The campaign analysis, pulled on 10 September 2026, covers 167,072 campaigns from 25,483 organizers with 100 or more entrants, and carries per action worth and mandatory flags, plan tier, language, country rules, terms settings, organizer location, daily impressions and referrers. It replaced a earlier dataset of campaigns with 1,000 or more entrants. Where a table still comes from the earlier dataset it says so.
- **Ordinary segment.** The 117,348 campaigns the benchmarks describe: every campaign in the campaign analysis that reached 100 unique valid entrants, after removing organizers whose homepage label is finance_crypto, token airdrops, buy-to-enter raffles and campaigns whose purpose could not be classified. Tables built with `analysis/frame.py` show n between 117,041 and 117,348 depending on which fields a cut needs.
- **Clean subset.** The 10,719 ordinary campaigns with no repeatable action (daily bonus, loyalty, timed bonus) and a run of 14 days or less. Impressions count once per visitor per day, so long runs and daily actions inflate impressions and depress conversion. Every comparison that depends on conversion uses this subset.
- **n.** The number of campaigns, prize records or actions behind a figure. A figure with a small n is reported as thin.

## Entrants and Entries

- **Contestant.** One unique person with at least one valid entry. Also called an entrant.
- **Entry.** One completed action multiplied by its entry worth. A follow worth 3 entries is 3 entries from 1 action.
- **Entries per contestant.** Total entries divided by contestants. Rises with more actions and with repeatable actions, so it measures how much each person did, never how many people came.
- **Action.** One thing an entrant is asked to do: follow, subscribe, share, answer, visit, join. Gleam calls these entry methods.
- **Completion.** One action done by one entrant. A signup, follow or join at that moment. The dataset counts completions per action, not entries, so a completion figure is never divided by worth.
- **Entry worth.** The number of entries an organizer assigns to one completion of an action. The default is 1. Worth changes the entry total and the odds, never the completion count, and only Viral Share completions rise as worth rises.
- **Uptake.** Completions of an action divided by contestants, in the campaigns that offered it. Above 1.0 means the campaign offered more than one action of that kind.
- **Invalid entry.** An entry the platform rejected after a check: an undone follow, a duplicate account, a wrong answer, a referral that never entered. Reported, never benchmarked.
- **Referral entry.** An entry credited to a sharer when the person they referred enters.

## Reach

- **Impression.** A unique visitor to the campaign page, counted once per visitor per day.
- **Conversion.** Contestants divided by impressions. The references also write this as contestants per impression. The two are the same number.
- **Hosted page.** The campaign at gleam.io/KEY/slug. **Embed** is the same campaign inside the organizer's site. **Directory listing** is the gleam.io/giveaways entry, and traffic from it counts as featured only when the referrer is gleam.io.

## Prizes

- **Stated value.** The USD value the organizer typed for the prize. About 60% of prize records have none, so value figures come from the ones that do.
- **Value band.** Stated campaign prize totals grouped on a roughly doubling scale: under 50, 50 to 99, 100 to 249, 250 to 499, 500 to 999, 1,000 to 2,499, 2,500 to 4,999, 5,000 to 9,999, 10,000 to 24,999, 25,000 to 49,999 and 50,000 USD and over.
- **Value index.** A campaign's contestants divided by the median contestants of its value band. 1.00 is typical for the money spent. 1.50 drew half again more than campaigns with the same budget.
- **Cost per asset.** Stated prize value divided by completions of an asset action (emails, follows, referrals). The giveaway's acquisition cost for that asset.

## Statistics

- **Median.** The middle value. Half of campaigns sit above it.
- **IQR.** Interquartile range, the span from the 25th to the 75th percentile. Half of campaigns sit inside it.
- **90th percentile.** The value one campaign in ten reaches or beats.
- **Top fifth, top tenth.** Campaigns above the 80th or 90th percentile of the metric named.

## Evidence Labels

- **Extracted.** Computed from the dataset by a script under `analysis/`.
- **Inferred.** Read from the dataset with a proxy, such as a regex on a title for a holiday or a vertical. Rough by construction.
- **Advice.** Practice with no dataset support, stated as practice.
