# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## The 40-Prompt Evaluation, 11 September 2026

Four of the forty prompts in `.omc/skill-loop/evalset.json` were run against this skill on 11 September 2026. Scoring was by an independent grader against `.omc/skill-loop/rubric.md`. Types are S straightforward, U underspecified, H hard realistic, T trap.

These forty prompts are additional to the cases in `evals.json`, which are a different set and were not re-scored in this round. The last recorded run of those cases was 10 September 2026, before this round of corrections landed, so their results are no longer reported here.

| Prompt | Type | Baseline | Latest | Latest graded run |
|---|---|---|---|---|
| idea-1 | S | 83 | 87 | iteration 2 |
| idea-2 | T | 89 | 86 | iteration 3 |
| idea-3 | H | 81 | 87 | iteration 2 |
| idea-4 | U | 54 | 87 | iteration 2 |

### idea-1 (S)

```
Shopify store selling handmade ceramics, about to hit 10k Instagram followers, want to do something for the milestone. Average order value is 65 USD. Ideas?
```

The baseline misattributed the value index and mis-glossed what it compares. The latest answer backs its pick with the one row that describes a store giveaway and says in the same breath that the figure describes what those businesses chose, and it never calibrates anything to a store of the reader's size.

### idea-2 (T)

```
Which giveaway type gets the most entrants in your data? Just tell me the winner and we'll run that one. We sell replacement HVAC filters by subscription.
```

The baseline gave the honest top row and then turned a one-point index gap into a cost. The latest answer names the top type and the runner-up on its thin base, says plainly what the number describes and builds three HVAC concepts before picking one, and it props that pick on a 24% Conversion Rate figure the same table beats with 27%.

An iteration 5 answer sits at `.omc/skill-loop/iter5/idea-2.md` and carries no entry in `.omc/skill-loop/iter5/grades.json`, so iteration 3 is the latest graded run.

### idea-3 (H)

```
B2B accounting practice in Ireland, 40 staff, we serve small business owners. Partners think giveaways are tacky and beneath us. Marketing wants to try one to build a list for a new bookkeeping product launching in March. I need something that will not embarrass the partners and will actually reach business owners rather than students hunting for free stuff.
```

The baseline misread the Email uptake column as a claim about what the campaign offered. The latest answer picks a peer-nomination mechanic that answers both halves of the conflict on the 87 referrals per 100 Entrants that B2B campaigns run on, and it calls 547 Entrants close to the typical 492 and invents a reason the data cannot see.

### idea-4 (U)

```
give me giveaway ideas for christmas
```

The baseline interviewed the reader and delivered nothing, when three concepts on a stated assumption would have cost it nothing. The latest answer ships three complete concepts, a conditional pick with the condition named and one closing question on four words of prompt, and it prints the Christmas finding twice with no limit attached to any figure.

## 9 October 2026, ten-prompt blind comparison

One prompt per skill was answered by Sonnet and assessed by a blind Sonnet pairwise judge. The retained round, r7, beat the pre-restructure round, r4, with eight wins, one loss and one tie overall.

This skill's retained-round verdict was a loss. The judge flagged unclear Conversion Rate percentages without attribution in the table, methodology in the prose, an unsupported lottery claim about a discount-code Prize, and a desk or monitor suggestion that did not fit a software business.

The rest of `evals.json` was not rerun.

## 9 October 2026, harmful-answer guardrails

New cases are not yet run against a model. Synthetic fixtures exercise the checker only, with explicit meaning reviews. A mechanical pass alone does not establish correctness.

| Case | Guardrail | Model status |
|---|---|---|
| 6 | legal-requirements | not yet run against a model |
| 7 | no-guaranteed-entrants | not yet run against a model |
| 8 | prize-fulfilment | not yet run against a model |
| 9 | platform-rules | not yet run against a model |
| 10 | causal-data-claim | not yet run against a model |
| 11 | matching-population | not yet run against a model |
| 12 | current-external-values | not yet run against a model |
| 13 | reader-language | not yet run against a model |

Existing cases 4 now have explicit judgement-only reviews. Their new rubrics are not yet run against a model. Missing reviews remain UNASSESSED until evidence is supplied.

Fixture pairs and supplied review records: `evals/fixtures/giveaway-idea-generator/manifest.json` from the repository root. Each fail answer isolates its one negative check. The fixture reviews classify synthetic examples only. Semantic paraphrases, implied guarantees, population selection and current-source validity still require independent meaning review.

## Answer scope regression, 10 October 2026

Added assertions for the brief's answer corrections to an existing case. Not yet run against a model. Repository checks are recorded in the patch report.

## Store behavior regression, 10 October 2026

Case 14 covers email-only store entry and missing product preferences. Not yet run against a model. Repository validation is recorded in the 3.0.34 patch report.
