# Eval results

| Case | Model | Result | Notes |
|---|---|---|---|
| 1 | Sonnet, 10 September 2026 | Fail (5/6) | Ran review.py and showed the table, placed 1,800 in the 1k to 2.5k band below the median, flagged 4.3% invalid without benchmarking it, one change naming a skill, asked for the email signup count as the next decision. Failed "compares conversion to the peer figure for 6 actions": the read column kept the 28% platform average and the 31% duration figure but dropped the 38% six-action peer figure. Added a line to SKILL.md workflow step 3 telling the reader to keep all three conversion comparisons together. Style: one "actually", three contrast sentences (not an assertion here, noted for case 3). |
| 2 | Sonnet, 10 September 2026 | Pass | Read 19% against the 24% median for 31-to-60-day campaigns and the 23% for 61 or more, explained the daily-bonus impressions effect, said the result does not look broken, named the numbers needed to rank it and the two skills for what to check next. Style: no em dashes, semicolons or fillers, one contrast phrase. |
| 3 | Sonnet, 10 September 2026 | Pass | Ran repo-root evals/style_check.py on both saved replies. Case 1: em_dashes 0, semicolons 0, assistant_opener 0, assistant_closer 0. Case 2: same, all zero. All three assertions hold for both replies. |

## 11 September 2026 run

One fresh reader, Claude Sonnet, given only this skill folder and a realistic message, scored with `evals/style_check.py`.

| Case | Result | Notes |
|---|---|---|
| 4,200 Entrants, 18,000 Impressions, 9,800 Entries, 6 methods, 21 days, $900 machine, coffee retailer. | Pass | Eight comparisons in one table, the weak measure named and explained, the run-length effect on Impressions separated from the rest, and the four follow-up numbers that live outside Gleam. |
