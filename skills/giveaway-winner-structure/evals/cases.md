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
