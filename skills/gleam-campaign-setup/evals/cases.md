# Eval results

| Case | Model | Result | Notes |
|---|---|---|---|
| 1 | Sonnet, 9 September 2026 | Pass | Checklist in tab order with the page linked per tab, email action mandatory, Allowed Locations US and CA, minimum age 18 required through User Details, two prize entries with 1 and 5 winners and both written into the description, redirect and Viral Share note, plan limits listed as "not in the docs". Style: two contrast sentences, one "actually". |
| 2 | Sonnet, 9 September 2026 | Pass | Five levels as documented, High as default, CAPTCHA modes, invalid entries reviewable on the Actions tab, Setup page linked, invalid median 3.8% quoted as extracted. One slip: placed Require login before actions on the Setup tab (it is under User Details). |
| 1 | Sonnet, 10 September 2026 | Fail then Pass | First run: tab order, email mandatory, Allowed Locations US and CA, minimum age under User Details, two prize entries with 1 and 5 winners, no invented plan limits, all passed, but the checklist joined each page link with an em dash (13 hits), failing the style check (case 3). Cause: the Output section said "link" with no format, so the model defaulted to an em dash even though the prose section already banned them. Fixed SKILL.md Output bullet and the "Plain punctuation" line to require the link in parentheses and to say the rule holds inside checklist lines. Reran with a fresh reader: same six assertions passed and em_dashes, semicolons, assistant_opener, assistant_closer all came back 0. |
| 2 | Sonnet, 10 September 2026 | Pass | Five levels as documented, High as default, CAPTCHA table matches the page, invalid entries reviewable on the Actions tab, Setup page linked at the end, no invented behaviour beyond Event Mode as described on the page. No change needed. |
| 3 | Sonnet, 10 September 2026 | Fail then Pass | Ran `evals/style_check.py` (repo root, not under a skill) against the saved case 1 and case 2 replies. Case 2 passed em_dashes, semicolons, assistant_opener and assistant_closer on the first run. Case 1 failed em_dashes (13) on the first run for the reason above. After the SKILL.md fix, the reran case 1 reply passed all four counts. |

## 11 September 2026 run

One fresh reader, Claude Sonnet, given only this skill folder and a realistic message, scored with `evals/style_check.py`.

| Case | Result | Notes |
|---|---|---|
| First-time Gleam user, two-week $400 coffee machine giveaway, wants a mailable list afterwards. | Pass | Checklist in tab order with one doc link per tab, the three settings that build the list named in the opening line, plan-gated features flagged, closes by asking which email provider. First run repeated the same URL on seven lines and said "extracted". |
