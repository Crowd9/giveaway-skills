# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## Targeted fixture check, 10 October 2026

Case 3: the answer separating completion events, weighted Entries and business value with the correct family ranking passed. The otherwise similar answer ranking visits highest failed. An independent reviewer assessed each fixture against the updated meaning criterion, then `evals/check_deliverable.py` returned the expected PASS or FAIL. These fixtures test the acceptance criteria, not generated answer quality.

## The 40-Prompt Evaluation, 11 September 2026

Four of the forty prompts in `.omc/skill-loop/evalset.json` were run against this skill on 11 September 2026. Scoring was by an independent grader against `.omc/skill-loop/rubric.md`. Types are S straightforward, U underspecified, H hard realistic, T trap.

These forty prompts are additional to the cases in `evals.json`, which are a different set and were not re-scored in this round. The last recorded run of those cases was 10 September 2026, before this round of corrections landed, so their results are no longer reported here.

`.omc/skill-loop/final-scores.json` was written before iteration 5 was graded, so its final column holds the iteration 3 or iteration 2 score wherever a later grade exists. The table below reports the latest graded run.

| Prompt | Type | Baseline | Latest | Latest graded run |
|---|---|---|---|---|
| entry-1 | S | 48 | 85 | iteration 5 |
| entry-2 | T | 47 | 78 | iteration 2 |
| entry-3 | H | 75 | 88 | iteration 2 |
| entry-4 | U | 46 | 82 | iteration 2 |

### entry-1 (S)

```
Running a giveaway for our pet treats brand next month. We're on Instagram and TikTok, we have a Klaviyo list, and the goal is to grow the email list before a Q4 launch. What entry methods should we use and how many?
```

The baseline withheld the deliverable on a fully specified prompt, with no table, no weights, no figures and no plan. The latest answer carries completion figures that check out exactly against the reference, and it answers how many with a count of six that has no figure behind it.

### entry-2 (T)

```
I want maximum entries so I'm going to add every action Gleam offers, about 20 of them, each worth different points. More ways to enter means more entries right? It's a giveaway for a gaming chair, audience is Twitch viewers.
```

The baseline invented a size for the Gleam action catalogue and read the method-count comparison as cause. The latest answer separates Entries from Entrants, which is the whole trap, and it quotes 29 per 100 for the 11-or-more band when 29 is the seven-to-ten figure and the longest lists hold at 31.

Deduction standing in the latest grade, unsupported precision: "the share of people who saw the campaign and actually entered falls from about 44 per 100 to 29 per 100"

### entry-3 (H)

```
We're a healthcare SaaS in the US selling to clinic managers. Legal won't let us do anything that looks like we're paying for a review or a referral, and we can't collect anything that could be PHI. We want qualified demo requests out of this, not a list of randoms. Nobody on the team can moderate a Discord. What do people actually do to enter?
```

The baseline read the pooled Custom Actions completion figure as the when-required figure. The latest answer honours all four constraints and says what each one costs, including where the lost referral reach was coming from, and it never flags that the qualifying-question pairing is the skill's own advice with no measured result behind it.

### entry-4 (U)

```
how many entry methods is too many
```

The baseline said larger campaigns hold on longer, which the reference's own elbow table contradicts. The latest answer opens with the number, gives the elbow by group and gets the corrected friction figures right, and it ends flat with no question about the objective and no assumption stated.

Correction to this historical assessment: the answer supplied group-specific cutoffs that the current reference rejects as unstable (`analysis/output/thresholds.json`, `action_count.by_stratum`). A passing answer describes the general conversion pattern without promising a dependable cutoff. The historical score is unchanged.

## Contact and consent regression, 12 September 2026

Added the no-subscription-Action prompt in `evals.json`. The documentation review checked the workflow and reference for separate address, consent and Action-usage decisions. No model response was generated or scored for this new case.

## Buyer Campaigns, 6 October 2026

Added two cases to `evals.json`. Case 6 is the 40 right Entrants against 4,000 wrong ones prompt, on gating, the qualifying question, follow-up and the scorecard. Case 7 puts the healthcare prompt entry-3 above into `evals.json` with its constraints as assertions, since entry-3 was only in the 40-prompt set and the model had improvised the qualifying-question pairing. Both are checked against `references/qualified-entry.md`, which labels the gating, question and follow-up advice as practice and says no output splits work email from free mail. No model response was generated or scored for these cases.

Pass for case 6: a one-sentence buyer, one qualifying question as the required action with answer choices, sorting by email domain after entry as the default, no work-email against free-mail figure quoted, an owner and a response time for each tier, and a scorecard of qualified Entrants and cost per qualified Entrant in place of the crowd measures.

## 9 October 2026, ten-prompt blind comparison

One prompt per skill was answered by Sonnet and assessed by a blind Sonnet pairwise judge. The retained round, r7, beat the pre-restructure round, r4, with eight wins, one loss and one tie overall.

This skill's retained-round verdict was a win. The judge flagged unexplained per-Entrant wording and the Viral Share label, a source block split across paragraphs with raw counts, and a closing question after the recommendation.

The rest of `evals.json` was not rerun.

## 9 October 2026, harmful-answer guardrails

New cases are not yet run against a model. Synthetic fixtures exercise the checker only, with explicit meaning reviews. A mechanical pass alone does not establish correctness.

| Case | Guardrail | Model status |
|---|---|---|
| 8 | legal-requirements | not yet run against a model |
| 9 | no-guaranteed-entrants | not yet run against a model |
| 10 | prize-fulfilment | not yet run against a model |
| 11 | platform-rules | not yet run against a model |
| 12 | causal-data-claim | not yet run against a model |
| 13 | matching-population | not yet run against a model |
| 14 | current-external-values | not yet run against a model |
| 15 | reader-language | not yet run against a model |

Existing cases 3, 4 now have explicit judgement-only reviews. Their new rubrics are not yet run against a model. Missing reviews remain UNASSESSED until evidence is supplied.

Fixture pairs and supplied review records: `evals/fixtures/giveaway-entry-method-planner/manifest.json` from the repository root. Each fail answer isolates its one negative check. The fixture reviews classify synthetic examples only. Semantic paraphrases, implied guarantees, population selection and current-source validity still require independent meaning review.

## Answer scope regression, 10 October 2026

Added assertions for the brief's answer corrections to an existing case. Not yet run against a model. Repository checks are recorded in the patch report.

## Referral conversion comparator, 10 October 2026

Added a judgement-only regression case after reviewing the source definition and aggregate cut. It distinguishes referral conversion from overall campaign conversion and leaves non-referral conversion unavailable. This case has not been run against a model. Repository checks are recorded in the patch report.
