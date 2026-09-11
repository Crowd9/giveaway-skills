# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## The 40-Prompt Evaluation, 11 September 2026

Four of the forty prompts in `.omc/skill-loop/evalset.json` were run against this skill on 11 September 2026. Scoring was by an independent grader against `.omc/skill-loop/rubric.md`. Types are S straightforward, U underspecified, H hard realistic, T trap.

These forty prompts are additional to the cases in `evals.json`, which are a different set and were not re-scored in this round. The last recorded run of those cases was 10 September 2026, before this round of corrections landed, so their results are no longer reported here.

`.omc/skill-loop/final-scores.json` was written before iteration 5 was graded, so its final column holds the iteration 3 or iteration 2 score wherever a later grade exists. The table below reports the latest graded run.

| Prompt | Type | Baseline | Latest | Latest graded run |
|---|---|---|---|---|
| promo-1 | S | 80 | 84 | iteration 3 |
| promo-2 | H | 64 | 84 | iteration 2 |
| promo-3 | T | 58 | 84 | iteration 5 |
| promo-4 | U | 76 | 86 | iteration 2 |

### promo-1 (S)

```
Our giveaway goes live Monday. Zero ad budget. We have 4k on Instagram, 900 on TikTok, and a 3k email list. How do we promote it?
```

The baseline turned the output checklist into the form-fill template the skill bans and left the reader one figure. The latest answer leads a zero-budget reader with three named directories and their real reach figures, and it names days 4 to 13 as the quiet stretch and then staffs nothing across a week of it.

### promo-2 (H)

```
Giveaway has been live 6 days and we have 47 entrants. Target was 2,000. We sell mountain bike components, audience is on YouTube and a couple of forums, Instagram is dead for us. We have 11 days left and about 600 USD we could spend. What do we actually do today?
```

The baseline cited deals forums at 47% and never named one. The latest answer names four directories with their own reach figures, all verified against `references/channel-playbook.md`, and tells the reader to post today, and it settles on a single diagnosis without checking a broken entry link before 600 USD goes out.

### promo-3 (T)

```
Just tell me the best channel for giveaway promotion according to your data and we'll put everything there. We're a local gym with two locations.
```

The baseline invented a comparative targeting capability for Meta against YouTube and TikTok. The latest answer corrects the premise in its first sentence and turns it into two things a two-location gym can do this week, and it quotes six channel shares while dropping the 52% direct share that carries the argument.

### promo-4 (U)

```
nobody is entering our giveaway
```

The baseline asked three questions and offered no default plan for a reader who wants something to do before they answer. The latest answer states its assumptions in one line and then ships the schedule, the copy, the email branches and the named directories, and it buries the broken entry link in a risks list at the bottom.
