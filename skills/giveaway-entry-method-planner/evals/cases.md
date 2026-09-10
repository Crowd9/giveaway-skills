# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## Last run

10 September 2026, Claude Sonnet reading only the skill folder, one fresh sub-agent per case.

| Case | Result | Notes |
|---|---|---|
| 1 Skincare email list | 5/6, then 6/6 after assertion fix | Email required at weight 5 with opt-in wording, Instagram follow, a segmentation question, page visit, referral for reach. Installs and account connections excluded. Uptake figures cited with n and labelled extracted. No platform pitch. Failed "weighted highest" because the referral action came in at weight 8 to 10, above email's 5. That is what `mix-by-objective.md`'s Weighting section now tells a reader to do (weight sharing at the high end of what the platform allows, since email is mandatory and does not need a high weight to be completed), a change from an older version of that section that capped both at 3 to 5. The assertion was written against the old text. Updated the assertion and expected_output in evals.json to require a stated weight rather than the highest weight, matching current skill guidance. |
| 2 Ten required actions | 4/5, then 5/5 after skill fix, reverified | Flagged all ten required and five stacked grow-social actions, moved app install to optional unless it is the objective, checked tag-a-friend rules by platform, cut to one required action and roughly six to eight methods. First run cited the 11-or-more friction figure as a near-fact reason to cut methods without stating the data cannot show what trimming this specific list would do. Added a sentence to SKILL.md workflow step 6 and a rule in Evidence rules requiring the caveat whenever a method-count or friction figure is cited against a specific list. Reran twice: the strengthened Evidence rules line got it right, the reader stated plainly the figure "does not prove trimming this list would raise entries." |
| 3 Most entries | 3/3 | Named the repeatable bonus family for raw volume, then separated completions counted once (Telegram, email, question, visit) from that, all with n and extracted labels, said none of it shows causation, and redirected to the objective before answering. The dataset's actual highest-uptake families are email and the question family, not page visits as the case's expected_output text names, since page visits sit at a middling 0.75 median in the family table while email runs 0.89 and the question family 0.86. No assertion in evals.json names page visits, so nothing failed, but the expected_output prose is dated. Left it, since fixing prose that isn't scored is out of scope for this run. |
| 4 Style | 3/3 | Ran `evals/style_check.py` on the three saved replies above. em_dashes, semicolons, assistant_opener and assistant_closer all zero across all three. The script's own stricter PASS/FAIL flag (curly quotes, question headings, sentence-length spread) failed reply 3 only on shortest_sentence being 7 words against its 6-word bar, which is not one of this case's four assertions, so it does not affect the score. Case 1's reply also tripped the script's contrast-sentence counter six times ("that's normal for this job, judge it by referrals, not by that completion number" and similar), a violation of the skill's own "never rather than or instead of" style rule that this case's assertions do not test either. Worth a tighter pass if a future case starts scoring contrast sentences, not touched here. |

## Skill changes made this run

- `SKILL.md` workflow step 6: added a sentence stating the 11-or-more friction figure describes organizer choice, not the effect of removing a method from the reader's own list.
- `SKILL.md` Evidence rules: added a standing rule to state that caveat whenever a method-count or friction figure is cited against a specific list, not only in step 6's own sentence.
- `evals/evals.json` case 1: updated the expected_output and one assertion from "email weighted highest" to "email required with a stated weight," since the Weighting section's current, data-backed guidance can put a referral action's weight above the mandatory action's.

## 11 September 2026 run

One fresh reader, Claude Sonnet, given only this skill folder and a realistic message, scored with `evals/style_check.py`.

| Case | Result | Notes |
|---|---|---|
| Skincare brand, $500 bundle, two weeks, wants email signups and some spread. | Pass | Five actions in a table with job, required or optional, weight and asset. The share-position tradeoff is given as a percentage change in both directions, so the reader sees what leading with share costs the email list. |
