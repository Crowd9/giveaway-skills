# Reading a Campaign That Is Still Running

The live mode of the review. A finished campaign is ranked against finished campaigns. For a running campaign, say "These are your totals so far, and they can still grow before the close." Any rank describes where those totals stand today, without judging the final result. What a live read can do is diagnose: reach, conversion or something broken, and what to do first.

## What the Data Holds and What It Does Not

- **Extracted, Impressions and share clicks only.** How a run's Impressions arrive day by day, by run length, how its share clicks arrive, and where Impressions come from. These are visits and clicks. They are never Entrants, so none of this says what an Entrant pace should be on day 4.
- **Extracted, finished campaigns.** Conversion Rate by run length and by Impressions group, and the Entrant count by size band, in `references/benchmarks.md` and `references/reading-results.md`.
- **No cut tracks Entrants, Entries or Conversion Rate day by day.** Nothing here can say how many Entrants a campaign should have on day 4. It cannot say how far a day sits from normal, or what days added to a run bring in. The curves hold a typical figure and no spread.
- **Everything else on this page is advice, common practice with nothing in the data behind it.** Say that in the answer, in the reader's words. There is no base rate here for how often a quiet or odd-looking campaign is broken, and an answer that offers one has made it up.

## Before Reading Anything (Advice)

1. Say it is live in the first line, with days run of days planned, as `references/gleam-reporting.md` says. Use the days run for every rate and the planned days for nothing.
2. Collect Impressions for each day from the Reporting tab, since the export does not carry them. Take Entrants for each day and the time of the last Entry from the export's When column. Ask what changed and when, which pushes have gone out and on what dates, and what the campaign is for.
3. Run `campaign_report.py` on the export and `review.py` with the days elapsed. Describe Entrants, Entries and follows as totals so far. Any rank is where they stand today, and a live total cannot yet be judged "below typical".

## Is the Pace Normal for This Day (Extracted)

Count days from the start date. The start date itself is day 0 and the closing day is left out of the table, because a campaign rarely begins or ends on a midnight and both are partial days. Divide the campaign's Impressions on day N by its Impressions on day 1 and read the answer against the last column. Use the row for the run length nearest to the planned one, and say which row it was. A run of ten or twenty days sits between rows.

The curve falls on purpose. A typical run front-loads its Impressions, so a fall from day one is the shape of the campaigns measured and carries no fault. What the table can show is a campaign sitting well under the typical multiple, which reads as reach, or sitting level because one source is carrying all of it. A campaign with a daily action counts a returning visitor again each day, so its own line runs higher. Read `references/reading-results.md` on the Impressions caveat before judging either.

<!-- generated:rr_live_pace -->
| Run length | Day since start | Typical share of the run's Impressions | Day as a multiple of day one | Campaigns | Businesses |
|---|---|---|---|---|---|
| 7 days | 1 | 20.6% | 1.00x | 23,879 | 5,739 |
| 7 days | 2 | 15.0% | 0.73x | 25,519 | 6,004 |
| 7 days | 3 | 11.3% | 0.55x | 25,703 | 6,026 |
| 7 days | 4 | 9.3% | 0.45x | 25,802 | 6,043 |
| 7 days | 5 | 8.3% | 0.40x | 25,829 | 6,052 |
| 7 days | 6 | 7.8% | 0.38x | 23,755 | 5,724 |
| 14 days | 1 | 10.7% | 1.00x | 15,997 | 4,817 |
| 14 days | 2 | 9.0% | 0.84x | 16,818 | 5,031 |
| 14 days | 3 | 6.7% | 0.63x | 16,935 | 5,045 |
| 14 days | 4 | 5.6% | 0.52x | 17,055 | 5,083 |
| 14 days | 5 | 5.0% | 0.47x | 17,161 | 5,107 |
| 14 days | 6 | 4.7% | 0.44x | 17,246 | 5,134 |
| 14 days | 7 | 4.6% | 0.43x | 17,330 | 5,148 |
| 14 days | 8 | 4.6% | 0.43x | 17,419 | 5,172 |
| 14 days | 9 | 4.5% | 0.42x | 17,448 | 5,178 |
| 14 days | 10 | 4.4% | 0.41x | 17,443 | 5,176 |
| 14 days | 11 | 4.5% | 0.43x | 17,459 | 5,179 |
| 14 days | 12 | 4.7% | 0.44x | 17,468 | 5,185 |
| 14 days | 13 | 5.1% | 0.48x | 15,919 | 4,785 |
| 30 days | 1 | 4.0% | 1.00x | 20,348 | 5,030 |
| 30 days | 2 | 4.9% | 1.22x | 21,783 | 5,270 |
| 30 days | 3 | 3.9% | 0.96x | 22,156 | 5,271 |
| 30 days | 4 | 3.3% | 0.83x | 22,440 | 5,292 |
| 30 days | 5 | 3.0% | 0.75x | 22,666 | 5,334 |
| 30 days | 6 | 2.8% | 0.70x | 22,783 | 5,349 |
| 30 days | 7 | 2.7% | 0.67x | 22,932 | 5,397 |
| 30 days | 8 | 2.6% | 0.65x | 23,043 | 5,421 |
| 30 days | 9 | 2.5% | 0.63x | 23,044 | 5,411 |
| 30 days | 10 | 2.4% | 0.60x | 23,066 | 5,422 |
| 30 days | 11 | 2.4% | 0.59x | 23,058 | 5,400 |
| 30 days | 12 | 2.3% | 0.58x | 23,133 | 5,442 |
| 30 days | 13 | 2.3% | 0.57x | 23,114 | 5,413 |
| 30 days | 14 | 2.3% | 0.57x | 23,158 | 5,422 |
| 30 days | 15 | 2.3% | 0.58x | 23,206 | 5,433 |
| 30 days | 16 | 2.3% | 0.56x | 23,235 | 5,449 |
| 30 days | 17 | 2.2% | 0.56x | 23,265 | 5,459 |
| 30 days | 18 | 2.2% | 0.55x | 23,255 | 5,458 |
| 30 days | 19 | 2.2% | 0.55x | 23,250 | 5,444 |
| 30 days | 20 | 2.2% | 0.55x | 23,262 | 5,451 |
| 30 days | 21 | 2.2% | 0.56x | 23,334 | 5,474 |
| 30 days | 22 | 2.3% | 0.58x | 23,360 | 5,464 |
| 30 days | 23 | 2.3% | 0.58x | 23,345 | 5,466 |
| 30 days | 24 | 2.4% | 0.59x | 23,343 | 5,466 |
| 30 days | 25 | 2.5% | 0.61x | 23,355 | 5,469 |
| 30 days | 26 | 2.6% | 0.64x | 23,373 | 5,464 |
| 30 days | 27 | 2.6% | 0.66x | 22,605 | 5,308 |
| 30 days | 28 | 2.8% | 0.69x | 21,562 | 5,085 |
| 30 days | 29 | 3.0% | 0.74x | 19,596 | 4,704 |
<!-- /generated -->

Source: `analysis/output/prize_timing_cuts.json` (`impression_curve_by_duration`).

### Share Clicks, When a Share Action Is On

Only campaigns that offered a share action have share clicks, so the sample is smaller and different. The Reporting tab's viral view, with clicks by day, is the figure to read against it. The shape is tighter, with the biggest days at the start.

<!-- generated:rr_live_share -->
| Run length | Day since start | Typical share of the run's share clicks | Day as a multiple of day one | Campaigns | Businesses |
|---|---|---|---|---|---|
| 7 days | 1 | 22.3% | 1.00x | 6,807 | 1,774 |
| 7 days | 2 | 17.1% | 0.77x | 7,739 | 1,967 |
| 7 days | 3 | 12.6% | 0.57x | 7,882 | 2,017 |
| 7 days | 4 | 10.2% | 0.46x | 7,912 | 2,027 |
| 7 days | 5 | 9.3% | 0.42x | 7,908 | 2,027 |
| 7 days | 6 | 8.7% | 0.39x | 7,304 | 1,896 |
| 14 days | 1 | 12.0% | 1.00x | 5,676 | 1,621 |
| 14 days | 2 | 10.6% | 0.89x | 6,713 | 1,868 |
| 14 days | 3 | 7.8% | 0.65x | 6,908 | 1,902 |
| 14 days | 4 | 6.5% | 0.54x | 7,049 | 1,939 |
| 14 days | 5 | 5.8% | 0.48x | 7,103 | 1,978 |
| 14 days | 6 | 5.2% | 0.44x | 7,149 | 1,996 |
| 14 days | 7 | 5.1% | 0.43x | 7,208 | 2,023 |
| 14 days | 8 | 4.9% | 0.41x | 7,267 | 2,023 |
| 14 days | 9 | 4.7% | 0.40x | 7,316 | 2,046 |
| 14 days | 10 | 4.6% | 0.39x | 7,284 | 2,040 |
| 14 days | 11 | 4.7% | 0.40x | 7,289 | 2,050 |
| 14 days | 12 | 4.8% | 0.40x | 7,355 | 2,047 |
| 14 days | 13 | 5.1% | 0.43x | 6,723 | 1,879 |
| 30 days | 1 | 6.4% | 1.00x | 6,702 | 1,552 |
| 30 days | 2 | 6.5% | 1.00x | 8,419 | 1,872 |
| 30 days | 3 | 4.9% | 0.76x | 8,868 | 1,948 |
| 30 days | 4 | 4.0% | 0.62x | 9,172 | 1,993 |
| 30 days | 5 | 3.5% | 0.55x | 9,324 | 2,039 |
| 30 days | 6 | 3.2% | 0.49x | 9,442 | 2,061 |
| 30 days | 7 | 2.9% | 0.46x | 9,473 | 2,079 |
| 30 days | 8 | 2.8% | 0.44x | 9,597 | 2,130 |
| 30 days | 9 | 2.7% | 0.42x | 9,685 | 2,148 |
| 30 days | 10 | 2.6% | 0.40x | 9,630 | 2,139 |
| 30 days | 11 | 2.5% | 0.39x | 9,687 | 2,154 |
| 30 days | 12 | 2.5% | 0.38x | 9,741 | 2,158 |
| 30 days | 13 | 2.4% | 0.37x | 9,708 | 2,180 |
| 30 days | 14 | 2.3% | 0.36x | 9,760 | 2,199 |
| 30 days | 15 | 2.4% | 0.36x | 9,828 | 2,205 |
| 30 days | 16 | 2.3% | 0.35x | 9,810 | 2,192 |
| 30 days | 17 | 2.2% | 0.34x | 9,801 | 2,181 |
| 30 days | 18 | 2.2% | 0.34x | 9,844 | 2,207 |
| 30 days | 19 | 2.2% | 0.34x | 9,854 | 2,208 |
| 30 days | 20 | 2.2% | 0.34x | 9,861 | 2,212 |
| 30 days | 21 | 2.3% | 0.35x | 9,896 | 2,216 |
| 30 days | 22 | 2.2% | 0.35x | 9,888 | 2,219 |
| 30 days | 23 | 2.3% | 0.36x | 9,940 | 2,228 |
| 30 days | 24 | 2.3% | 0.36x | 9,974 | 2,240 |
| 30 days | 25 | 2.4% | 0.38x | 9,989 | 2,230 |
| 30 days | 26 | 2.5% | 0.39x | 10,028 | 2,250 |
| 30 days | 27 | 2.6% | 0.41x | 9,736 | 2,191 |
| 30 days | 28 | 2.7% | 0.42x | 9,331 | 2,070 |
| 30 days | 29 | 2.8% | 0.44x | 8,543 | 1,928 |
<!-- /generated -->

Source: `analysis/output/field_cuts.json` (`share_click_curve_by_duration`).

### The Closing Days

Read from the close, so a run a day longer or shorter than its label shifts every row by a day. Use this table for the question of what the last days normally hold, and the first table for what day N normally holds.

<!-- generated:rr_live_close -->
| Run length | Close day | 1 day before | 2 days before | 3 days before | 4 days before | 5 days before | Campaigns (close day) | Businesses |
|---|---|---|---|---|---|---|---|---|
| 7 days | 8.6% | 8.8% | 8.3% | 9.3% | 10.8% | 12.6% | 25,892 | 6,066 |
| 14 days | 5.8% | 5.8% | 4.8% | 4.5% | 4.4% | 4.4% | 17,492 | 5,195 |
| 30 days | 3.6% | 3.5% | 2.9% | 2.6% | 2.5% | 2.4% | 23,476 | 5,527 |
<!-- /generated -->

Source: `analysis/output/calendar.json` (`last_days_impression_curve_by_duration`).

### Where a Typical Campaign's Impressions Came From

A share of Impressions across the campaigns measured. It names which source to check first when Impressions fall. It is no ranking of channels, and it cannot be set beside the export's referrers, which describe the visits behind completed actions. Set it beside the Reporting tab's traffic view and nothing else.

<!-- generated:rr_live_traffic -->
| Traffic source | Share of Impressions |
|---|---|
| Direct | 48% |
| Organizer sites | 9.6% |
| Meta | 9.0% |
| YouTube | 6.1% |
| Giveaway directories | 4.8% |
| Search | 3.9% |
| X | 3.7% |
| Gaming communities | 3.1% |
| Gleam pages | 3.1% |
<!-- /generated -->

Source: `analysis/output/field_cuts.json` (`referrer_channel_share`).

## Reach, Conversion or Broken (Advice)

Decide in this order and say which one the numbers support, with the figure that decides it.

| What you see | It reads as | Check first |
|---|---|---|
| Impressions under the typical multiple for the day, Entrants moving with them | Reach | Which source carried day one and whether it has stopped. Which pushes are still unsent, from the promotion plan |
| Impressions on the pattern, Conversion Rate so far well under the row below for the run length so far | Conversion | What the page asks: the mandatory action, verification, a login wall, the eligibility line, the Prize. The report's entry methods section shows which action loses people |
| Impressions arriving, Entrants flat for hours or stopped at one clock time | Something broken | The entry link in every place it was posted, the embed, the verification step, the email provider sync, and any change made at that time. Enter once yourself, signed out, on a phone |
| Entrants jump in a short window from one source, one country or similar-looking addresses | Entries that look fake | The section below |
| Everything on the pattern | Not a fault yet | The objective, then the last section |

Conversion Rate so far is Entrants so far divided by Impressions so far. Read it against the row for the run length so far, in the table below. That is a rough yardstick and nothing in the data tracks a campaign's rate by day, so say it is rough.

<!-- generated:bm2_conv_duration -->
| Duration | Campaigns | Conversion Rate |
|---|---|---|
| 1 to 7 days | 21,210 | 40% |
| 8 to 14 | 16,484 | 28% |
| 15 to 30 | 20,497 | 26% |
| 31 to 60 | 11,419 | 23% |
| 61 or more | 2,929 | 21% |
<!-- /generated -->

Source: `analysis/output/percentiles.json` (`bench`, `conv_by_duration`). Campaigns with no repeatable action. The source does not specify completion-status filtering.

Read the Impressions count before calling a Conversion Rate low. Inside every size band the campaigns with the fewest Impressions converted highest and those with the most converted lowest, in the table under "What extra reach is worth" in `references/reading-results.md`. A high Conversion Rate beside low Impressions is therefore a reach problem that looks like a good rate.

## Entries That Look Fake (Advice)

Read the export. Gleam's documentation says Invalid entries do not appear in reporting, so the Reporting tab can hide what you are looking for, and the export's Status column holds them.

1. Rule out the harmless causes first. A validated-answer question marks wrong answers Invalid. A referral chain shows in the referral graph as a few sharers behind many Entrants. A post, partner, listing or email at that hour can explain a burst alone.
2. Find the source in the report: first-touch channel and invalid rate for each, countries and cities, and the daily pattern.
3. Read the invalid share beside its own industry in `references/reading-results.md` under "Invalid share by industry and country". It is a figure and never a score, and a fifth or more of entries is the point where the review mentions it at all.
4. Report what you found as signs to investigate. A shared referrer, a country the audience is not in, one Entry Method and nothing else, a pattern in the addresses, a clock time. None proves anything alone.
5. Leave the removal to the draw, with a rule written down first. The steps, and what each Gleam setting is documented to do, are in the promotion plan's live rescue reference. Never say what raising the Fraud Level does to entries already in. The Gleam docs do not cover it.

## Extend, Push or Accept (Advice)

The review's part is the arithmetic and the question. Give the days left, where the typical curve sits for those days, the pushes still unsent and the objective, then say which of the three the numbers support and what would change the call.

- **Push** when Impressions sit under the typical multiple and scheduled pushes are unsent.
- **Fix the page** when Impressions are on the pattern and the Conversion Rate so far is well under the row for the run length so far.
- **Accept** when the objective is met, or the pushes are spent and the curve is at its quiet level.
- **Extend** only with a dated new push at the start of the extension. Nothing in the data measures what bare added days bring in. Any change of date goes through the terms check in the promotion plan's live rescue reference.

When most Entrants came in the first week and the campaign has run quietly for months, keep its published closing date. Consider a fresh push or accept the quiet period. Before recommending an earlier close, establish that the change is permitted through the terms check in the promotion plan's live rescue reference. Draw only after the permitted entry window ends. See `references/gleam-reporting.md` for the live reporting workflow.

## What to Hand Back

1. A one-line verdict: live, day N of M, which of reach, conversion, broken, odd-looking or on pattern, and the figure that decides it.
2. The reader's day N beside the typical multiple for that day, with the row named.
3. The checks for that cause, cheapest first.
4. The one change that helps this run, with the terms check beside it when it changes dates, the Prize, an Entry Method or eligibility.
5. The call on extend, push or accept.
6. One closing question, addressed to "you", for the one fact only they can give.
