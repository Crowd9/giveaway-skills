# Eval results

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## The 40-Prompt Evaluation, 11 September 2026

Four of the forty prompts in `.omc/skill-loop/evalset.json` were run against this skill on 11 September 2026. Scoring was by an independent grader against `.omc/skill-loop/rubric.md`. Types are S straightforward, U underspecified, H hard realistic, T trap.

These forty prompts are additional to the cases in `evals.json`, which are a different set and were not re-scored in this round. The last recorded run of those cases was 10 September 2026, before this round of corrections landed, so their results are no longer reported here.

| Prompt | Type | Baseline | Latest | Latest graded run |
|---|---|---|---|---|
| setup-1 | S | 37 | 88 | iteration 2 |
| setup-2 | H | 52 | 86 | iteration 2 |
| setup-3 | T | 75 | 76 | iteration 2 |
| setup-4 | U | 55 | 82 | iteration 2 |

### setup-1 (S)

```
First time using Gleam Competitions. Walk me through setting up a 14-day giveaway where people enter by joining our email list and following us on Instagram.
```

The baseline gave a fully specified prompt no setup content at all. The latest answer walks the tabs in the order the app presents them, with every setting name and doc URL checkable in the reference and the two decisive settings argued from figures, and it files Build Competition Subscriber List under two different tabs in one bullet.

An iteration 5 answer sits at `.omc/skill-loop/iter5/setup-1.md` and carries no entry in `.omc/skill-loop/iter5/grades.json`, so iteration 2 is the latest graded run.

### setup-2 (H)

```
Gleam campaign is live and we're seeing what looks like fraud, lots of entries from similar-looking emails within minutes. Which settings do I change mid-campaign, what do I do about the entries already in, and what do I check in the Actions tab?
```

The baseline invented how the Fraud Filter treats Entries already collected, on the one sub-question the references do not answer. The latest answer says outright that the docs do not cover it and routes the reader to a manual Actions tab pass, and it borrows throwaway-account completion figures to size two settings the reference says are not in the dataset.

### setup-3 (T)

```
Can I make the email signup mandatory and skip the free entry alternative? It's our competition and we want the emails. Also can I set the fraud filter to maximum so we get zero fake entries?
```

The baseline endorsed the Very High fraud level without naming its cost, against the skill's own evidence file. The latest answer corrects the premise at the right level, that the free entry alternative is a checkbox tied to paid actions, and it credits the data with a best-performing verdict that the reference files under advice.

Deduction standing in the latest grade, causal claim: "email as your first and only mandatory action is what the data says works best for collecting an asset like this"

### setup-4 (U)

```
how do i set up a giveaway in gleam
```

The baseline handed back nothing, so a reader who answered the questions still had no idea what the setup involves. The latest answer delivers the whole five-tab shape with the settings that bite and then asks its three questions, and it hand-waves on how many actions where the sibling skill carries a number.
