# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root. The script's own check is `python3 scripts/draw.py --self-test`.

## Draw integrity regression, 12 September 2026

`python3 skills/giveaway-random-draw/scripts/draw.py --self-test` passed after the correction. The new regression checks that the commitment preview reports rows read, eligible people, merged duplicates, exclusions and invalid weights from a weighted synthetic input, including a byte-order-mark exclusion file. Further regressions reject nonfinite weights into the invalid-weight count and stop on overflow when combining duplicate weights. Existing ranking and weight tests also passed.

Cases 7 and 8 in `evals.json` cover broken weights after a known seed and unresolved published rules. They have been added as evaluation specifications and have not been run through a model grader. The historical scores below predate this correction.

## The 40-Prompt Evaluation, 11 September 2026

Four of the forty prompts in `.omc/skill-loop/evalset.json` were run against this skill on 11 September 2026. Scoring was by an independent grader against `.omc/skill-loop/rubric.md`. Types are S straightforward, U underspecified, H hard realistic, T trap.

These forty prompts are additional to the cases in `evals.json`, which are a different set and were not re-scored in this round. The last recorded run of those cases was 10 September 2026, before this round of corrections landed, so their results are no longer reported here.

`.omc/skill-loop/final-scores.json` was written before iteration 5 was graded, so its final column holds the iteration 3 or iteration 2 score wherever a later grade exists. The table below reports the latest graded run.

| Prompt | Type | Baseline | Latest | Latest graded run |
|---|---|---|---|---|
| draw-1 | S | 84 | 88 | iteration 2 |
| draw-2 | H | 85 | 89 | iteration 2 |
| draw-3 | T | 88 | 90 | iteration 2 |
| draw-4 | U | 58 | 86 | iteration 5 |

### draw-1 (S)

```
I need to pick 3 winners from a CSV of entrants. Some people entered more than once and should get more chances. How do I do this so people trust it?
```

The baseline described the whole procedure in prose, so a reader with a CSV still had to work out what to type. The latest answer ships a pasteable rules.json and four runnable commands with the commit-before-the-seed step explained, and it prints a drand round number in the draw command that only exists once commit has run.

### draw-2 (H)

```
We already closed entries yesterday and I've got the list. Someone in the comments is accusing us of rigging the last one. I need to draw 5 winners plus 5 backups, exclude our own staff and anyone with a disposable email, and be able to prove afterwards that I didn't pick them. Entrant list is 18,000 rows.
```

The baseline gave an 18,000-row job no copyable commands and never checked its one-entry-per-person assumption. The latest answer uses the flagged-out pass exactly as it was built to be used and re-commits on the approved exclusions before any seed exists, and it never states how duplicates are treated, which is the rule that most needs publishing with an accuser watching.

### draw-3 (T)

```
I'll just use random.org, screenshot it, and post the screenshot. That proves it's fair doesn't it?
```

The baseline closed on a question where the skill's own style rule asks for a decision verb. The latest answer explains what the screenshot fails to show and names the three properties that would fix each gap in turn, and it leaves the free route in prose when the skill ships a script that does the job.

### draw-4 (U)

```
pick a winner for me
```

The baseline stated its four defaults and left the reader no route they could take on their own. The latest answer refuses the impossible ask and names the export route for each network, every one of them checkable in `references/getting-your-entrant-list.md`, and it still leaves nothing the reader can run today.

## Draw data integrity regression, 12 September 2026

Executable self-tests now cover empty, truncated, reordered and reassigned audit results, plus single-column CSV headers and explicit identifier columns. The export integration also performs a weighted draw and verifies its audit. These are executable regression checks. No new model response was generated or graded.
