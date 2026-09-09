# Versions

Repo version lives in `.claude-plugin/plugin.json` and `marketplace.json`. Bump the middle number for a new skill, the last number for changes to an existing skill, the first for restructures. Each skill carries its own `metadata.version` in its frontmatter and must be bumped on any shipped change, since that is what installed users compare against.

| Skill | Version | Last change |
|---|---|---|
| giveaway-prize-picker | 1.0.0 | 2026-09-09. Two modes, six criteria, taxonomy from 60,282 prize records, value bands by campaign size, budget calculator, evidence rules, Gleam reference. |
| giveaway-entry-method-planner | 1.0.0 | 2026-09-09. Action families with uptake, mixes by objective, method-count and referral findings, promotion rules from seventeen networks. |
| giveaway-timing-and-duration | 1.0.0 | 2026-09-09. Duration, month, weekday and recency findings, timeline template, calendar by region. |
| giveaway-winner-structure | 1.0.0 | 2026-09-09. Structure findings, draw and contact rules, terms draft generator, Gleam drawing reference. |
| giveaway-promotion-plan | 1.0.0 | 2026-09-09. Channel playbook, email sequence, partner brief, paid rules. |
| giveaway-random-draw | 1.0.0 | 2026-09-09. Provably fair draw: commit, public beacon seeds, hash-ranked selection, verify, audit record. |
| giveaway-winner-communications | 1.0.0 | 2026-09-09. Message set from notification to non-winner, edge cases, contact log. |
| giveaway-idea-generator | 1.0.0 | 2026-09-09. Hook shares from 37,180 campaign titles, theme starters, mechanics, formats to avoid. |

## 1.0.0 (2026-09-09)

First public release. Eight skills built on an export of 54,675 giveaway campaigns with 1,000 or more contestants (37,180 ordinary after excluding crypto, ambiguous and purchase-only campaigns), committed as aggregates only, with the analysis scripts, a validator, evals with a style checker, plugin manifests and an MIT licence.
