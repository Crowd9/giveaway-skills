# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## Last run

10 September 2026, Claude Sonnet reading only the skill folder.

| Case | Result | Notes |
|---|---|---|
| 1 Coffee subscription, two weeks, one partner post | Pass 6/6 | Dated schedule table by channel, copy leading with prize and deadline, roaster brief, a six-email sequence covering the launch, mid and last-call assertion, no entrant-number promise, no platform pitch. |
| 2 Nobody entering | Pass 4/4 | Same-day relaunch across every channel, entry page and link checked before sending, boost capped at one extra winner, states plainly that the data cannot say how many entries this pulls in. |
| 3 Comments, DMs and an impersonator on launch day | Pass 5/5 after fix, was 4/5 | Pinned comment covers entry, eligibility and close time, eligibility never widened, fake account screenshotted and reported. The impersonation warning read "we contact winners only from this account", which names nothing once the line is screenshotted or forwarded past the post it started on, the reader's failure traced back to the same wording in channel-playbook.md's impersonation row. Fixed: that row's reply now requires the official handle by name, "We contact winners only from @[official handle] and [official email]", with a note explaining why "this account" fails. |
| 4 Style | Pass | Zero em dashes, semicolons, curly quotes, assistant openers or closers across all three saved replies, checked with `evals/style_check.py`. |

## 11 September 2026 run

One fresh reader, Claude Sonnet, given only this skill folder and a realistic message, scored with `evals/style_check.py`.

| Case | Result | Notes |
|---|---|---|
| $600 prize, two-week run starting Monday, 3,000 email and 5,000 Instagram, no TikTok. | Pass | Dated schedule for three pushes, the actual post and email copy, the pinned comment for "is this real", an impersonation response, and what to measure from Instagram's own insights. |
