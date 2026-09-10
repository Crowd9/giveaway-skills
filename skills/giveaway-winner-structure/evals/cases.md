# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## Last run

10 September 2026, Claude Sonnet reading only the skill folder.

| Case | Result | Notes |
|---|---|---|
| 1 Meal-prep containers | Pass 6/6 | 20 equal winners sized after a $15/parcel shipping estimate, own-cost note, draw and verification rules, 72-hour contact and redraw, terms snippet, contestant-index figure cited as extracted with n=13,977, next decision on real shipping cost. |
| 2 Winner not replying | Pass 4/4 | Second attempt and a written 72-hour deadline, terms-first check with a fallback when none exists, forfeit and redraw from backup, written log, next decision on notifying the original winner. |
| 3 Gleam tiers | Fail 4/5 then Pass 5/5 | Two prize entries (1 and 5), All Prizes draw order, Random.org and no auto-contact from the docs, no invented plan limits. First run named the Prize tab, Winners tab and Random Winners controls but never gave their URLs, failing "links the official pages" even though the reference carries them. Fixed by adding one line to SKILL.md's Platform behaviour section telling the writer to include the doc links, not just cite their content. Re-run after the fix cited all three page links (prizes, random-winners, repeat-winners). |
| 4 Style | Pass 3/3 | Ran `evals/style_check.py` on the saved case 1 to 3 replies. em_dashes, semicolons, assistant_opener and assistant_closer all 0 in every reply, so all three graded fields pass. The script's own PASS/FAIL verdict flags the six-word shortest-sentence floor on two replies (case 1 at 4, case 3 at 7), which is not one of the three graded assertions and was left alone. |

## 11 September 2026 run

One fresh reader, Claude Sonnet, given only this skill folder and a realistic message, scored with `evals/style_check.py`.

| Case | Result | Notes |
|---|---|---|
| $3,000 anniversary prize budget, one big Winner or several smaller. | Pass | Single Prize as the default with the crowd cost of splitting given as a percentage, then what splitting buys back on reach and referrals, and a closing question that decides it. Figures match structure-findings.md exactly. |
