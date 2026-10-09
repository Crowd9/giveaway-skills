# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## Targeted fixture check, 10 October 2026

Case 3: the attributed weekday answer with an explicitly unavailable campaign count passed, and practical scheduling advice omitting the statistic passed. The answer borrowing the full-dataset count failed. An independent reviewer assessed each fixture against the updated meaning criterion, then `evals/check_deliverable.py` returned the expected PASS or FAIL. These fixtures test the acceptance criteria, not generated answer quality.

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

## 9 October 2026, ten-prompt blind comparison

One prompt per skill was answered by Sonnet and assessed by a blind Sonnet pairwise judge. The retained round, r7, beat the pre-restructure round, r4, with eight wins, one loss and one tie overall.

This skill's retained-round verdict was a win. The judge flagged parenthetical campaign counts that cluttered the prose, unexpected gaps between campaigns, and methodology-heavy wording about comparing Conversion Rate across durations.

The rest of `evals.json` was not rerun.

## 9 October 2026, guardrail fixture checks

These added cases are **not yet run against a model**. Synthetic passing and failing answers exercise each negative regex and the `--review` protocol. Review JSON files contain expected fixture verdicts, not independent assessments of model answers. Meaning review is still required for paraphrases and implied claims.

| Case | Guardrail | Model status |
|---|---|---|
| 6 | legal-requirement | not yet run against a model |
| 7 | entrant-promise | not yet run against a model |
| 8 | fulfilment-claim | not yet run against a model |
| 9 | platform-compliance | not yet run against a model |
| 10 | causal-evidence | not yet run against a model |
| 11 | external-value | not yet run against a model |
| 12 | internal-language | not yet run against a model |
| 13 | matched-population | not yet run against a model |

Fixtures and replay manifest: `evals/fixtures/giveaway-timing-and-duration/` at the repository root. Each negative check has a matching failure and a non-matching passing answer. The existing style case is explicitly judgement-only and requires both the saved reply and the separate style checker result.
