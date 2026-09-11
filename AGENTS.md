# AGENTS.md

Guidance for AI agents working in this repository.

## What This Is

A library of Agent Skills for running giveaways, following the [Agent Skills specification](https://agentskills.io/specification.md). Skills live in `skills/<name>/SKILL.md` with optional `references/`, `evals/` and `scripts/`. The repo also serves as a Claude Code plugin marketplace through `.claude-plugin/marketplace.json`. Supported by Gleam, platform-neutral in its advice.

## Rules

- `name` in frontmatter matches the directory, lowercase letters, digits and hyphens, 1 to 64 characters. `description` is 1 to 1024 characters and quotes the phrases users say. `metadata.version` is present and bumped on every shipped change, mirrored in `VERSIONS.md`.
- `SKILL.md` stays under 200 lines. Detail goes in `references/` and is loaded only when the skill says so.
- Every skill has `evals/evals.json` (prompt, expected output, assertions) and a `cases.md` with the last run's results.
- The blocks every skill shares live one copy each under `scripts/`: `answer-style.md`, `asking.md` and `evidence-scope.md`. `render_shared.py` writes them into each SKILL.md between `<!-- generated:NAME -->` markers and `--check` fails the build on a drifted copy. Edit the source, never a skill's copy. A rule one skill needs alone goes after the closing marker.
- Prose follows `scripts/answer-style.md`, which is split by who enforces it. The mechanical rules (em dashes, semicolons, straight quotes, contrast sentences, assistant openers and closers, filler vocabulary and the rest) are enforced by `evals/style_check.py`, generated into every skill at `scripts/style_check.py` so a skill answering a user can run it on its own draft. The judgement rules (how to shape a number, what a caveat is, when to ask) stay as prose, because no checker does those. Measured across forty answers, rules read by eye left about ten faults for every thousand words and the command took the retested answers to zero.
- A figure in a SKILL.md body names the `references/...md` or `analysis/output/...json` it came from, so `check_claims.py` can check it. The body is loaded on every run and was the last surface with no guard over it.
- Benchmarks count campaigns, and 55% of them come from 11% of the businesses. A reader on their first campaign is compared with first campaigns (382 Entrants), never the campaign-weighted 492. The table is in `giveaway-results-review/references/benchmarks.md`.
- Dataset-derived numbers carry a sample size and a missing-data note. No causal claims from the dataset, which has no comparison group of smaller or failed campaigns. It covers campaigns from 100 Entrants up, in six size bands. The shared scope block in `scripts/evidence-scope.md` is the one statement of what it holds, and every skill carries it.
- Never commit the campaign data, organizer names, emails, ids, links, or record-level analysis. Aggregates only. See `.gitignore`. The sample files under `skills/*/examples/` are the one exception: they are synthetic, use example.com and example.org addresses, and describe nobody.
- Gleam appears only in Gleam-named reference files (`gleam-setup.md`, `gleam-drawing.md`, `gleam-draws.md`), loaded on explicit request. Verify Gleam features against https://gleam.io/docs before stating them.
- If `.agents/product-marketing.md` exists in the user's project (the context file from the marketingskills library), skills read it before asking about business, audience or positioning.

## Checks

```bash
python3 scripts/validate.py                                  # frontmatter, size, links, style, evals
python3 scripts/check_data.py                                # empty blocks, blank cells, generated tables
python3 scripts/render_shared.py --check                     # the shared blocks have not drifted
python3 scripts/check_claims.py                              # prose contradicting its table, and skill-body figures against the reference they cite
python3 evals/style_check.py reply.txt                       # score a saved reply, the same script each skill ships
```

## Only Aggregates Are Committed

This repository carries aggregate findings and the skills that use them, and nothing else. No personal data of any kind belongs here: no names, email addresses, IP addresses or anything derived from them, no billing or contact details, no identifiers for a customer or a campaign, and no record-level row.

Every committed figure is an aggregate with its sample size, and no published group describes fewer than five distinct businesses, so no row describes one company. That floor counts businesses and says nothing about concentration: 55% of the campaigns come from the 1,984 businesses on their eleventh campaign or later, so a cut can clear the floor and still describe a handful of accounts. Read a median as the typical campaign and never as the typical business. CI fails on an email address, an IP address, an identity field name, a committed symlink or a data file.
