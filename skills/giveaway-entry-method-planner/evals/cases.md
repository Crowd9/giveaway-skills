# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

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

## Contact and consent regression, 12 September 2026

Added the no-subscription-Action prompt in `evals.json`. The documentation review checked the workflow and reference for separate address, consent and Action-usage decisions. No model response was generated or scored for this new case.
