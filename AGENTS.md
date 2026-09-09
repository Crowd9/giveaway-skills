# AGENTS.md

Guidance for AI agents working in this repository.

## What This Is

A library of Agent Skills for running giveaways, following the [Agent Skills specification](https://agentskills.io/specification.md). Skills live in `skills/<name>/SKILL.md` with optional `references/`, `evals/` and `scripts/`. The repo also serves as a Claude Code plugin marketplace through `.claude-plugin/marketplace.json`. Supported by Gleam, platform-neutral in its advice.

## Rules

- `name` in frontmatter matches the directory, lowercase letters, digits and hyphens, 1 to 64 characters. `description` is 1 to 1024 characters and quotes the phrases users say. `metadata.version` is present and bumped on every shipped change, mirrored in `VERSIONS.md`.
- `SKILL.md` stays under 200 lines. Detail goes in `references/` and is loaded only when the skill says so.
- Every skill has `evals/evals.json` (prompt, expected output, assertions) and a `cases.md` with the last run's results.
- Prose follows the style section in `skills/giveaway-prize-picker/SKILL.md`: no em dashes, no semicolons, straight quotes, no "X, not Y" contrast sentences, no assistant openers or closers, specifics over adjectives.
- Dataset-derived numbers carry a sample size and a missing-data note. No causal claims from the export, which contains only large campaigns.
- Never commit the campaign export, organizer names, emails, ids, links, or record-level analysis. Aggregates only. See `.gitignore`.
- Gleam appears only in Gleam-named reference files (`gleam-setup.md`, `gleam-drawing.md`, `gleam-draws.md`), loaded on explicit request. Verify Gleam features against https://gleam.io/docs before stating them.
- If `.agents/product-marketing.md` exists in the user's project (the context file from the marketingskills library), skills read it before asking about business, audience or positioning.

## Checks

```bash
python3 scripts/validate.py                                  # frontmatter, size, links, style, evals
python3 skills/giveaway-prize-picker/evals/style_check.py reply.txt   # score a saved reply
python3 analysis/analyze_export.py <export> --private-dir <dir>       # regenerate aggregates (private input)
```
