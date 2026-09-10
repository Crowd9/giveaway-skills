# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## Last run

10 September 2026, Claude Sonnet reading only the skill folder.

| Case | Result | Notes |
|---|---|---|
| 1 Candle brand at 10k followers | Pass (6/6) | Three distinct concepts (simple draw, vote, partner bundle). Milestone hook cited with current figures (1,262 of 35,658, 3.5%, September peak). Collaboration hook also cited. Recommendation with reasoning, hand-off to prize picker and entry-method planner, no platform pitch, no entrant-number promise. |
| 2 Christmas SaaS | Pass (4/4) | Series/advent concept (12 Days of Workflow Wins), partner concept and a simple year-free concept. Cited the December start share (about 12%, one and a half times a typical month) and both the daily-series and holiday-season hook rows. Warned about competing for attention in December and about carrier cut-offs. Hand-off to four downstream skills. |
| 3 Keyboard launch | Pass (4/4) | Three concepts (early access, daily teaser series, partner bundle), each with hook, mechanic and prize direction. Quoted the launch subtype data with n (launches overall 0.20 referrals, early access 0.16 against the 0.12 median, n=191; product launches generally 2,000 contestants, 29% conversion on 325 clean, index 0.88 on 546 valued). Product itself is the prize in concept 1. Recommended promotion and referral before the prize. Found and fixed a stale figure while checking this case: `references/hooks-and-themes.md`'s store-campaigns section said early access carries a value index of "1.09 in the launch table above", but the table itself says 1.08 (79 valued campaigns), confirmed against `analysis/output/standouts.json` (value_index 1.0778). Fixed the reference doc to 1.08 and updated the case's expected_output in evals.json to match, since the table is the source of truth and the prose had drifted from it. |
| 4 Style check | Pass (3/3 replies clean) | Ran `evals/style_check.py` on the three saved replies above. em_dashes 0/0/0, semicolons 0/0/0, assistant_opener 0/0/0, assistant_closer 0/0/0 across all three. Not scored by the JSON assertions but worth noting: the script also flags contrast constructions ("not X, but Y", "rather than", "instead of"), which SKILL.md's own style section asks writers to avoid: case 1 had 6, case 2 had 1, case 3 had 2 (including "not instead of it" and "not after"). No assertion covers this so it is not a fail, but it is a recurring tell worth another look if a future run adds a contrast assertion. |

## 11 September 2026 run

One fresh reader, Claude Sonnet, given only this skill folder and a realistic message, scored with `evals/style_check.py`.

| Case | Result | Notes |
|---|---|---|
| Indie board game publisher, co-op game launching in six weeks, 8,000 email and 12,000 Instagram. | Pass | Three concepts on the sheet the skill asks for, a pick with its reason, hook shares with the 35,658-campaign base in brackets, and both skip lines grounded in platform rules and lottery law. First run failed on our word "extracted" reaching the reader, which is now out of the skill's instructions. |
