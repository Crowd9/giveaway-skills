# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## Last run

9 September 2026, Claude Sonnet reading only the skill folder.

| Case | Result | Notes |
|---|---|---|
| 1 Espresso machine winner set | Pass | Six messages in send order with channel and timing, deadline with time zone, no-payment line, address privacy and deletion line, announcement with consent, non-winner message, contact log. An automated content check flagged this run on the anti-scam wording in the notification template, which is the intended text. |
| 2 Angry DM | Pass | Dispute template citing date, method, entrant count and record location, no redraw, one more reply at most then stop, logged, screenshots if abusive. |
| 3 After the draw and the list | Not yet run | Added with `references/after-the-draw.md`. Checks the three-message welcome series, the separate sending stream, the unsubscribe and complaint read, the sunset rule, the entry against marketing consent split, and the one feedback question. |
| 4 Style | Pass on tells | Zero em dashes and semicolons. |
