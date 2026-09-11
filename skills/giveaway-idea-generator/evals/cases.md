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
