# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## The 40-Prompt Evaluation, 11 September 2026

Four of the forty prompts in `.omc/skill-loop/evalset.json` were run against this skill on 11 September 2026. Scoring was by an independent grader against `.omc/skill-loop/rubric.md`. Types are S straightforward, U underspecified, H hard realistic, T trap.

These forty prompts are additional to the cases in `evals.json`, which are a different set and were not re-scored in this round. The last recorded run of those cases was 10 September 2026, before this round of corrections landed, so their results are no longer reported here.

| Prompt | Type | Baseline | Latest | Latest graded run |
|---|---|---|---|---|
| timing-1 | S | 78 | 78 | iteration 3 |
| timing-2 | T | 66 | 74 | iteration 2 |
| timing-3 | H | 80 | 87 | iteration 2 |
| timing-4 | U | 86 | 90 | iteration 2 |

### timing-1 (S)

```
How long should our giveaway run? Cosmetics brand, US, launching a new serum in six weeks, we want signups before launch day.
```

The baseline used a causal verb on observational data and dropped the column that argued the other way. The latest answer spends its argument on the gap between close and launch day, which is the decision that changes whether the list is usable, and it quotes the wrong calendar week and mislabels the 762-campaign comparison base.

Deduction standing in the latest grade, unsupported precision: "470 Entrants and 34% Conversion Rate for campaigns that size [762 campaigns started that week]"

### timing-2 (T)

```
A friend said longer giveaways always get more entrants, so we're going to run ours for 90 days. Any reason not to? We're a small board game publisher with 1,200 Instagram followers.
```

The baseline contradicted itself on Entries per person inside four paragraphs. The latest answer lands the launch-spike evidence exactly, 15.8% of Impressions on launch day against 7.7% at close, and it carries the Impressions counting artifact over onto a real Entrant count and tells the reader those extra Entrants are not real people.

Deduction standing in the latest grade, wrong population: "That's more repeat visits being counted on a similar-sized crowd. It isn't two thirds more people newly deciding to enter."

### timing-3 (H)

```
We sell to teachers, US K-12. Our busy season is August back-to-school and everything dies over summer break. We also have a conference booth in late June. We want one giveaway this year and we need it to feed the August push. When do we run it and for how long, and what do we do in the dead weeks?
```

The baseline moved the plan into 2027 without saying so. The latest answer anchors on back to school, demotes the June conference to a list build with a QR code and takes its window from the calendar table, and it reads 876 Entrants at 32% as though both figures sat above typical.

### timing-4 (U)

```
best day to launch a giveaway?
```

The baseline repeated the reference prose over the reference table and flattened a weekday spread that runs Friday 521 against Saturday 438. The latest answer refuses to manufacture a finding out of a null result and hands the decision back with the spread shown, and it calls 19.2% a majority when it is only the most common choice.
