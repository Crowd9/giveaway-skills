# Contributing

Contributions are welcome: a fix to an existing skill, a new reference, a new eval case, or a new skill. The bar is the same for all of them: platform-neutral advice, evidence with its sample size, and prose that reads as a person wrote it.

## Adding or Changing a Skill

Keep it small and self-contained:

- `skills/<skill-name>/SKILL.md` with `name`, `description` and `metadata.version` frontmatter. The description quotes the phrases users say and names what is out of scope. The body stays under 200 lines: workflow, questions to ask, output shape, guardrails.
- `skills/<skill-name>/references/` for material the skill loads only when relevant (taxonomies, criteria, examples, limitations). Name the file for what it contains.
- `skills/<skill-name>/evals/evals.json` (prompt, expected output, assertions) plus `cases.md` with the last run's results. Run `python3 scripts/validate.py` and `python3 scripts/style_lint.py` and the evals before merging, and bump the version in `VERSIONS.md`.
- If a skill quotes a figure, cite the file under `analysis/output/` it came from. Only aggregates belong here, and no published group describes fewer than five businesses (see `.gitignore`).
- Generic advice stays platform-neutral. Platform-specific help lives in a separate reference loaded only when the user asks for that platform.
- Write every file, and every answer a skill produces, the way a practitioner would. No em dashes, no semicolons, straight quotes. No "X, not Y" contrast sentences, no question or slogan headings, no assistant openers or closers, no filler vocabulary (leverage, robust, comprehensive, streamline, furthermore). Lead with the answer, ground claims in numbers or examples, vary sentence length, and stop when the content stops. A new skill gets those sections by adding the three marker pairs and running `python3 scripts/render_shared.py`. Never copy the wording in by hand, which is how ten skills ended up with ten versions of the same rules.

Candidates for later that need no data: a full terms-and-rules skill (the winner-structure skill ships a draft generator), platform compliance checks, giveaway page copy, fraud and verification, post-mortem, partner brief. A referral-loop skill is justified by the share data and would be strongest with per-campaign viral share clicks, successful sharers and viral conversion rate from the platform's Viral Share report. From fields the dataset has and the current skills do not use: campaign descriptions (a copy skill for the giveaway page), custom terms (a terms-and-eligibility checklist skill, with legal review), and impressions against contestants (a promotion and reach skill).


## Adding a Platform Loader

Both scripts read a Gleam Actions export without configuration and match other platforms' exports by column name. Adding a platform means teaching them its header row.

- `skills/giveaway-results-review/scripts/campaign_report.py` holds `SYNONYMS`, a dict of role to the column names that fill it: `who`, `action`, `entries`, `status`, `when`, `country`, `city`, `referrer`, `landing`, `details`. Add the new platform's header spellings to the roles they fill and leave the roles it has no column for alone, because `resolve_columns` reports a missing role and never guesses one. A wide export with one column per entry method needs no new synonyms, only a `who` column the resolver can find.
- `skills/giveaway-random-draw/scripts/draw.py` holds `ID_KEYS`, the ordered list of field names that name a person in a CSV header or a JSON export. Put the new name where its specificity belongs, since the first match wins and `email` should stay ahead of `name`.
- Add a case to that script's `self_test()` covering the new header, run `python3 <script> --self-test`, and paste four or five anonymised header-only rows into the skill's reference so the next contributor can see the shape. Never commit a real export.

## Contributing Benchmarks

New numbers are welcome as aggregates. Record-level rows stay out of the repository whatever they describe.

- Submit a table in a `references/` file with a column or a caption carrying `n`, the cut the rows were selected by (size floor, exclusions, date range), the date the data was pulled, and the name of the script that produced it.
- Put that script in `analysis/` so anyone can rerun it against their own export. It reads a private path and writes aggregates only.
- One row per group, never per campaign, per organizer or per entrant. No names, emails, account ids, campaign links or titles.
- State what the number describes and what it cannot show. Nothing derived from a single export can carry a causal claim.

## Repository Layout

```
README.md
CONTRIBUTING.md         how to add or change a skill
AGENTS.md               rules for agents editing this repo
VERSIONS.md             changelog and per-skill versions
LICENSE                 MIT
.claude-plugin/         plugin and marketplace manifests
scripts/validate.py     frontmatter, size, links, style and evals checks
scripts/answer-style.md the one copy of the answer style every skill carries
scripts/asking.md       when to answer and when to ask, shared
scripts/evidence-scope.md  what the data covers and what it cannot say, shared
scripts/render_shared.py   writes those copies into every skill, --check guards them
scripts/check_claims.py    prose that contradicts the table it reads
skills/
  giveaway-prize-picker/
    SKILL.md
    references/
    evals/              evals.json, cases.md
    scripts/            style_check.py, generated from evals/style_check.py so a skill can lint its own draft
  giveaway-entry-method-planner/
  giveaway-timing-and-duration/
  giveaway-winner-structure/
  giveaway-random-draw/     includes scripts/draw.py and examples/sample-entrants.csv
  giveaway-idea-generator/
  giveaway-promotion-plan/
  giveaway-winner-communications/
  giveaway-results-review/  includes scripts/review.py and examples/sample-actions-export.csv
  gleam-campaign-setup/
analysis/
  output/               the aggregate findings the skills quote
```

## Before Opening a Pull Request

```bash
python3 scripts/validate.py
```

The validator checks frontmatter, name rules, file size, reference links, prose style (no em dashes, semicolons or curly quotes) and the shape of `evals/evals.json`. `scripts/check_claims.py` checks a comparative sentence against the table it reads and a skill-body figure against the reference that line cites, and fails on either. Cite the file when you put a figure in a SKILL.md body. Run the skill's eval cases with an assistant that has loaded only the skill folder, and record the results in `evals/cases.md`. Bump the skill's `metadata.version` and add a line to `VERSIONS.md`.

Three sections are generated into every skill from one copy each under `scripts/`: `## How to write the answer` from `answer-style.md`, the opening of `## What to ask first` from `asking.md`, and the top of `## Evidence rules` from `evidence-scope.md`. `evals/style_check.py` is generated in whole into every skill at `scripts/style_check.py`, so a skill folder installed on its own can still lint a draft. To change any of them edit the source and run `python3 scripts/render_shared.py`, which rewrites all ten skills and bumps nothing, so bump the versions yourself. A rule only one skill needs goes after that section's `<!-- /generated -->` marker, where it survives a re-render. CI runs `--check` and fails when a skill's copy has drifted from the source.

## What Never Goes In

Personal data of any kind, and anything at record level. Only aggregates with their sample sizes belong here, and no published group describes fewer than five businesses, so no row describes one company.

CI fails on an email address, an IP address, a committed link or a file type that does not belong here.

## Licence

MIT. By contributing you agree your contribution is licensed the same way.

## Sample Data

Two synthetic files let you run the scripts before you have an export of your own. No real people are in either.

`skills/giveaway-random-draw/examples/sample-entrants.csv` is 40 rows of email, name and entries, with duplicates and one disposable domain so the pre-draw scan has something to report:

```bash
python3 skills/giveaway-random-draw/scripts/draw.py commit skills/giveaway-random-draw/examples/sample-entrants.csv --winners 3 --weight-column entries
```

`skills/giveaway-results-review/examples/sample-actions-export.csv` is 118 rows in the shape of a Gleam Actions export, 30 entrants over five days with invalid rows, referrals and both hosted and embedded landing pages:

```bash
python3 skills/giveaway-results-review/scripts/gleam_export.py skills/giveaway-results-review/examples/sample-actions-export.csv
python3 skills/giveaway-results-review/scripts/campaign_report.py skills/giveaway-results-review/examples/sample-actions-export.csv --impressions 4200
```
