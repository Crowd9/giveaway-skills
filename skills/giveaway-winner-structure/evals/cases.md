# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## The 40-Prompt Evaluation, 11 September 2026

Four of the forty prompts in `.omc/skill-loop/evalset.json` were run against this skill on 11 September 2026. Scoring was by an independent grader against `.omc/skill-loop/rubric.md`. Types are S straightforward, U underspecified, H hard realistic, T trap.

These forty prompts are additional to the cases in `evals.json`, which are a different set and were not re-scored in this round. The last recorded run of those cases was 10 September 2026, before this round of corrections landed, so their results are no longer reported here.

| Prompt | Type | Baseline | Latest | Latest graded run |
|---|---|---|---|---|
| winner-1 | S | 58 | 73 | iteration 2 |
| winner-2 | H | 82 | 86 | iteration 2 |
| winner-3 | T | 55 | 79 | iteration 2 |
| winner-4 | U | 30 | 86 | iteration 2 |

### winner-1 (S)

```
We have a 1,000 USD budget for prizes. Is it better to do one 1,000 prize or ten 100 prizes? Direct-to-consumer sock brand, US only.
```

The baseline wrote the comparison as a prediction about this campaign, which the reference says the data cannot support. The latest answer makes the sock-specific case, that 100 USD of socks is still above a normal order, and it inherits a stale crowd-per-dollar pair from this skill's own reference while the corrected file reads 1.15 and 0.64.

Deduction standing in the latest grade, causal claim: "Campaigns that move from one Prize to five or more see Reach lift 30% to 57% per 100 Entrants and referrals lift 8% to 28%."

### winner-2 (H)

```
Running a giveaway across UK, Germany and Japan for our camera accessories brand. Main prize is a 900 GBP lens. What do we do about terms, tax and the fact that our German distributor says we need something different there? Also what happens if the winner doesn't reply.
```

The baseline talked to the reader about the skill's own tooling and printed a terms clause that contradicted its own redraw rule. The latest answer names its own gaps inside the terms and refuses to invent the German requirement while saying what to get in writing, and it fills the draft with a promoter name, a street address and entry dates the reader never supplied.

### winner-3 (T)

```
I'll just pick whoever left the nicest comment as the winner, it's our giveaway and our rules. 3k followers, we're a small candle business in Canada. That's fine right?
```

The baseline stated the scope of the Quebec contest regime as fact, on one reference line that says no such thing. The latest answer catches the line in the published terms that has to change before a judged pick, and it softens the skill's own rule by allowing the criterion to be published once Entries are already in.

### winner-4 (U)

```
how many winners should i have
```

The baseline delivered nothing while the reference carried a one-line default the reader could have acted on. The latest answer gives that default, the four conditions that override it and a worked sizing comparison on six words of prompt, and it supports a crowd-per-dollar claim with Conversion Rate figures, which are a different measure.

## 9 October 2026, ten-prompt blind comparison

One prompt per skill was answered by Sonnet and assessed by a blind Sonnet pairwise judge. The retained round, r7, beat the pre-restructure round, r4, with eight wins, one loss and one tie overall.

This skill's retained-round verdict was a win. The judge flagged an assumed response window stated before its assumption and advice to move to a backup based on account signals before the deadline.

The rest of `evals.json` was not rerun.

## 9 October 2026, guardrail fixture checks

These added cases are **not yet run against a model**. Synthetic passing and failing answers exercise each negative regex and the `--review` protocol. Review JSON files contain expected fixture verdicts, not independent assessments of model answers. Meaning review is still required for paraphrases and implied claims.

| Case | Guardrail | Model status |
|---|---|---|
| 5 | legal-requirement | not yet run against a model |
| 6 | entrant-promise | not yet run against a model |
| 7 | fulfilment-claim | not yet run against a model |
| 8 | platform-compliance | not yet run against a model |
| 9 | causal-evidence | not yet run against a model |
| 10 | external-value | not yet run against a model |
| 11 | internal-language | not yet run against a model |
| 12 | matched-population | not yet run against a model |
| 13 | published-draw-rules | not yet run against a model |

Fixtures and replay manifest: `evals/fixtures/giveaway-winner-structure/` at the repository root. Each negative check has a matching failure and a non-matching passing answer. The existing style case is explicitly judgement-only and requires both the saved reply and the separate style checker result.

## Published action retention regression, 10 October 2026

Added paired judgement-only regression cases 14 and 15. The source instructions were checked against both branches. These cases have not been run against a model.
