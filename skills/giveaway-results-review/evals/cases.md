# Eval results

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## The 40-Prompt Evaluation, 11 September 2026

Four of the forty prompts in `.omc/skill-loop/evalset.json` were run against this skill on 11 September 2026. Scoring was by an independent grader against `.omc/skill-loop/rubric.md`. Types are S straightforward, U underspecified, H hard realistic, T trap.

These forty prompts are additional to the cases in `evals.json`, which are a different set and were not re-scored in this round. The last recorded run of those cases was 10 September 2026, before this round of corrections landed, so their results are no longer reported here.

`.omc/skill-loop/final-scores.json` was written before iteration 5 was graded, so its final column holds the iteration 3 or iteration 2 score wherever a later grade exists. The table below reports the latest graded run.

| Prompt | Type | Baseline | Latest | Latest graded run |
|---|---|---|---|---|
| review-1 | S | 71 | 82 | iteration 2 |
| review-2 | T | 75 | 79 | iteration 2 |
| review-3 | H | 60 | 86 | iteration 2 |
| review-4 | U | 35 | 64 | iteration 5 |

### review-1 (S)

```
Our giveaway finished. 3,400 entrants, 14,200 entries, 62,000 impressions, 8,900 of the entrants gave us an email. Ran 21 days. We sell yoga mats DTC. How did we do?
```

The baseline reproduced review.py's band mislabel and printed all-campaign medians under a column headed typical for your size. The latest answer catches the planted impossibility and quotes the 2,500 to 10,000 band's own figures throughout, and it ranks three measures on the Entrant count it has just called into question.

### review-2 (T)

```
We got 480 entrants. Your benchmark says the typical campaign gets thousands so we clearly failed and my boss wants to kill the channel. We're a niche B2B supplier of laboratory glassware, total addressable audience is maybe 4,000 people worldwide.
```

The baseline read 480 as below typical by printing the all-campaign 492 in a band column its own table contradicted. The latest answer takes the trap on the band's own typical of 352 and says plainly that a figure in the thousands describes the wrong group, and it hands the reader no route forward for a boss who wants to kill the channel.

Deduction standing in the latest grade, unsupported precision: "Your boss is comparing an Entrant count sized for a mass-market audience against a market that's four orders of magnitude smaller."

### review-3 (H)

```
Campaign done: 12,000 entrants, but only 310 of them have opened any email since, and sales in the two weeks after were flat. Prize was a 500 USD Amazon gift card. We sell premium dog food subscriptions. Was this a waste of money and what do we change?
```

The baseline gave the all-campaign 42 cents as the 10,000-or-more band figure and contradicted itself inside the same sentence. The latest answer uses that band's own 14 cents for stated Prize value per Entrant and its typical of 16,135 Entrants, and it leads with the flattering cut while the band rank sits inside the table.

### review-4 (U)

```
how did our giveaway do
```

The baseline was a pure interview, with no benchmark and nothing the reader could hold their own figures against. The latest answer hands over a yardstick, 382 Entrants at 26% for a first campaign with six size bands to rank inside, and it explains the repeat-campaign climb in the one way `references/benchmarks.md` forbids two lines under its own table.

Deduction standing in the latest grade, causal claim: "Once a business has run several campaigns those figures climb toward 492 Entrants, 27%, and closer to 4 and a half Entries each, mostly because they already have a list to push the next one to."

## Draw data integrity regression, 12 September 2026

The converter self-test rejects missing and invalid Entries consistently in summary and export. The integration test preserves fractional earned weights, runs the generated review command, draws Winners and verifies the audit. Missing weights stop conversion before an output file is created. These are executable regression checks. No new model response was generated or graded.
