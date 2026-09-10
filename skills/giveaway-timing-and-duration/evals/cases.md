# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## Last run

10 September 2026, Claude Sonnet reading only the skill folder.

| Case | Result | Notes |
|---|---|---|
| 1 Launch anchor | Pass 6/6 | Three-week run, 21 Sep to 12 Oct, closing two days before the 14 Oct launch, Monday start, dated timeline, draw plus announce with a reply deadline, duration figure cited with n, no platform pitch. Reasoning called the 15-30 day band "the highest" entries-per-contestant band, but the table's own 31-60 day row (5.06) is higher, an agent misread of the table rather than an ambiguity in it. |
| 2 Three-month giveaway | Pass 4/4 | Named the quiet-middle problem in its own words, offered a shorter run or a monthly recurring draw, cited the duration distribution with n, said the data cannot say which length converts best. No causal slip this time. Four contrast-pattern sentences ("not as", "not because", "instead of", "rather than") the skill's own style section asks the writer to catch, noted but not scored against any case assertion. |
| 3 Best weekday | Pass 3/3 | Monday at 18.8% cited as extracted with n, said flat across weekdays and shows organizer choice not outcomes, tied the pick to audience and team availability. |
| 4 Black Friday | Pass 4/4 | Quoted the Black Friday row (n=352, 8 days, lead 8 with IQR 3 to 16) correctly. The eval's expected_output said 364 campaigns, stale against the current table (352), corrected in evals.json. Gave 19 Nov launch and 25 Nov close (trimmed from 8 to 6 days to close before Thanksgiving), dated timeline, seasonal week note. |
| 5 Style check | Pass 3/3 | Ran style_check.py on all four replies: em_dashes, semicolons, assistant_opener and assistant_closer all 0 across the board. The eval's expected_output pointed at a prize-picker evals/style_check.py that has never existed, the script lives only at the repo root, corrected in evals.json. The script's own stricter PASS/FAIL label (which also checks sentence-length floor and contrast sentences) flagged case 2 and case 4, not part of this case's graded assertions. |

20 of 20 assertions passed. Two stale figures in evals.json corrected: the Black Friday n was 364, now 352 to match holiday-benchmarks.md, and the style-check script path was pointed at a file that does not exist, now points to the repo root. No SKILL.md or reference changes were needed this run.

## 11 September 2026 run

One fresh reader, Claude Sonnet, given only this skill folder and a realistic message, scored with `evals/style_check.py`.

| Case | Result | Notes |
|---|---|---|
| UK garden centre, wants to run before spring planting season. | Pass | Three weeks, 8 February to 1 March 2027, with the voucher out before Mothering Sunday on 7 March. Every weekday in the plan checks out against the calendar. |
