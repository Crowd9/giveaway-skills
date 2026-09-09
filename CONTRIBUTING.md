# Contributing

Contributions are welcome: a fix to an existing skill, a new reference, a new eval case, or a new skill. The bar is the same for all of them: platform-neutral advice, evidence with its sample size, and prose that reads as a person wrote it.

## Adding or Changing a Skill

Keep it small and self-contained:

- `skills/<skill-name>/SKILL.md` with `name`, `description` and `metadata.version` frontmatter. The description quotes the phrases users say and names what is out of scope. The body stays under 200 lines: workflow, questions to ask, output shape, guardrails.
- `skills/<skill-name>/references/` for material the skill loads only when relevant (taxonomies, criteria, examples, limitations). Name the file for what it contains.
- `skills/<skill-name>/evals/evals.json` (prompt, expected output, assertions) plus `cases.md` with the last run's results. Run `python3 scripts/validate.py` and the evals before merging, and bump the version in `VERSIONS.md`.
- If a skill derives numbers from data, put the reproducible script in `analysis/` and commit only aggregates. Raw exports, customer names, emails, account ids and record-level outputs stay out of git (see `.gitignore`).
- Generic advice stays platform-neutral. Platform-specific help lives in a separate reference loaded only when the user asks for that platform.
- Write every file, and every answer a skill produces, the way a practitioner would. No em dashes, no semicolons, straight quotes. No "X, not Y" contrast sentences, no question or slogan headings, no assistant openers or closers, no filler vocabulary (leverage, robust, comprehensive, streamline, furthermore). Lead with the answer, ground claims in numbers or examples, vary sentence length, and stop when the content stops. The style section in `skills/giveaway-prize-picker/SKILL.md` is the reference wording; copy it into new skills.

Candidates for later that need no data: a full terms-and-rules skill (the winner-structure skill ships a draft generator), platform compliance checks, giveaway page copy, fraud and verification, post-mortem, partner brief. A referral-loop skill is justified by the share data and would be strongest with per-campaign viral share clicks, successful sharers and viral conversion rate from the platform's Viral Share report. From fields the export has and the current skills do not use: campaign descriptions (a copy skill for the giveaway page), custom terms (a terms-and-eligibility checklist skill, with legal review), and impressions against contestants (a promotion and reach skill).


## Before Opening a Pull Request

```bash
python3 scripts/validate.py
```

The validator checks frontmatter, name rules, file size, reference links, prose style (no em dashes, semicolons or curly quotes) and the shape of `evals/evals.json`. Run the skill's eval cases with an assistant that has loaded only the skill folder, and record the results in `evals/cases.md`. Bump the skill's `metadata.version` and add a line to `VERSIONS.md`.

## What Never Goes In

Customer data of any kind: names, emails, account ids, campaign links, raw exports, record-level analysis. Only aggregates with sample sizes. The `.gitignore` blocks the usual paths, and the validator will not catch a pasted name, so look before you commit.

## Licence

MIT. By contributing you agree your contribution is licensed the same way.
