# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## Last run

10 September 2026, Claude Sonnet reading only the skill folder, one fresh sub-agent per case.

| Case | Result | Notes |
|---|---|---|
| 1 Espresso machine winner set | Pass (6/6) | Six messages in send order with channel and timing, deadline with time zone, no-payment line, address privacy and deletion line, announcement with consent, non-winner message, contact log. First run used em dashes as header separators ("1. Winner notification — send today...") instead of the parentheses `references/message-templates.md` already uses, which broke the style check in case 4. Fixed by telling the Output section to label messages the way the reference does, parentheses, never a dash. Re-run confirmed zero em dashes with the same content passing. |
| 2 Angry DM | Pass (4/4) | Dispute template citing date, method, entrant count and record location, no redraw, one more reply at most then stop, logged. The reply reached this on its own, but the dispute row in the edge-case table did not say to log it or to stop after one more reply, the only row missing that instruction. Added "Log the exchange" and the one-more-reply-then-stop line to the table so the next reader is not relying on inference. |
| 3 After the draw and the list | Pass (8/8) | Non-winner message framed as email one of the three-message series, each with a when and a job, separate stream with the sender-reputation reason, unsubscribe and complaint rates named to read after the send, sunset rule before the core list, entry consent against marketing consent with where each is collected, one feedback question, no invented figures. |
| 4 Style | Pass (3/3) | Ran `evals/style_check.py` on the three saved replies (case 1's post-fix version, case 2, case 3). Zero em dashes, zero semicolons, no assistant opener or closer. Failed on the first case 1 run (10 em dashes) before the SKILL.md fix above. |

21 assertions total, 21 passed after the fix and re-run. No stale assertions found.

## 11 September 2026 run

One fresh reader, Claude Sonnet, given only this skill folder and a realistic message, scored with `evals/style_check.py`.

| Case | Result | Notes |
|---|---|---|
| $1,200 camera bundle Winner has not replied, and what to send everyone else. | Pass | Second attempt with the deadline, the forfeit message, the non-Winner message, single-use codes, and a separate sending stream. Exposed a gap: every edge case assumed a reserve Winner already existed, now fixed. |
