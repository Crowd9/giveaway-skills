# Draw procedure

Advice from practice. Sweepstakes and lottery law differs by jurisdiction. This is not legal advice.

## Before the draw

- Close entries at the time and time zone in the terms. Export the list once and keep that file. Record its hash (the script prints it). The verify step hashes the file it is given and compares that to the hash in the audit record, so it needs the same export, byte for byte. A copy with the emails hashed, trimmed or reordered will not match, and there is no mode that verifies against one. A sponsor who must not see addresses gets the audit record and the published commitment, and checks those.
- Decide the deduplication rule before looking at names. Common choices: one chance per email, or entries add up when the terms promised bonus entries.
- List exclusions in a separate file: staff and their households, previous Winners if the terms bar them, Entrants from ineligible regions, entries flagged as automated.
- Decide tiers and backups. Two backups per tier covers most no-reply cases without a second draw.
- Pick the seed and, if the terms or a partner require it, publish it before drawing.

- Expect some entries to fail verification. Across ordinary campaigns in the dataset the typical campaign had 4.2% of entries marked invalid, across 107,886 campaigns and 16,633 businesses, and referral-heavy mixes ran higher. Draw from valid entries only, and treat a drawn name as a Winner only after the entry checks out.

`commit` also prints review lines for disposable email domains, one domain holding a fifth or more of the list, and runs of handles that differ only by a trailing number. They are prompts to look, never verdicts. Decide what to exclude, update the exclusion file, then commit again.

## Why commit first

A draw is provable when three things hold: the Entrant list and rules were fixed before the seed was known, the seed came from somewhere the organizer could not steer, and the selection from seed to Winners is a fixed calculation anyone can redo. The script does all three. `commit` hashes the frozen file and the rules into one value to publish. The seed comes from a public randomness beacon whose round was named in advance. The selection is a hash ranking, so the audit record plus the file reproduces the Winners in any language.

## Seed sources

| Source | How | Fits when |
|---|---|---|
| drand beacon (League of Entropy) | `commit --draw-at` prints the round number due at that time. Publish it. After that time, `draw --seed-drand ROUND` fetches the round's randomness from api.drand.sh and records the signature. Rounds are every 30 seconds and anyone can refetch a round forever. | Default choice. Free, no account, publicly verifiable. |
| NIST Randomness Beacon | Announce a future minute. `draw --seed-nist UNIXTIME` fetches that pulse's output value. Pulses are every 60 seconds and signed by NIST. | Audiences that prefer a government source. |
| A value published by a third party | A partner or witness emails a phrase before the draw, or a closing index value on a named date. `draw --seed "the value"`. | Co-sponsored giveaways with no internet at the draw. Keep the email. |
| RANDOM.ORG | Third-Party Draw Service runs the draw and publishes a record for at least five years without exposing Entrants. The Signed API can also pre-commit with tickets and returns results signed with RANDOM.ORG's key. Paid, needs an account. | Organizers who want a named independent party rather than their own script. |

Do not let the script or the organizer generate the seed. A generated seed can be regenerated until the result pleases.

## Running it

Write the rules once into a small JSON file so the commit and the draw cannot disagree.

```json
{
  "tiers": "Grand Prize:1,Runner-up:5",
  "backups": 2,
  "id-column": "email",
  "weight-column": "entries",
  "exclude": "staff.txt"
}
```

```bash
# 1. Freeze the list, then commit and announce the drand round for the draw time
python3 scripts/draw.py commit entries.csv --rules rules.json --draw-at "2026-09-12T09:00:00+10:00"

# 2. After that time, draw once
python3 scripts/draw.py draw entries.csv --rules rules.json \
  --seed-drand 6452000 --audit draw-2026-09-12.json --winners-csv winners.csv --mask

# 3. Anyone with the same files can check
python3 scripts/draw.py verify draw-2026-09-12.json --exclude staff.txt
```

Every option still works as a flag, and a flag on the command line overrides the file. Publish `rules.json` beside the commitment so anyone checking the draw can see what was fixed in advance.

One draw. If the tool errors (too few eligible Entrants, wrong column), fix the input, commit again, and keep only the final run.

**Read the counts back before you call it done.** Both commands print, and the audit records, `rows_read`,
`unique_eligible`, `duplicates_merged`, `excluded` and `rows_with_invalid_weight`. The last one is the quiet
failure: an Entrant whose weight is blank, zero or negative is dropped from the draw, so a misnamed weight column
or a sparse entries field can take most of the list out while the draw still succeeds and prints Winners. A file
of five rows where three have no weight draws from two people and says so in one line that is easy to skip.

Check `unique_eligible` against what the business expects before announcing anything. When the gap is more than a
rounding difference, say the number out loud to the user and name the cause. Where the weight column is the
problem, the fix is usually to drop `--weight-column` and run an unweighted draw, which keeps everyone in.

**Weighting concentrates the odds, so decide it before the draw and say which you did.** The key is
`u ^ (1 / weight)`, so an Entrant holding twenty entries is twenty times more likely to take any given place than
one holding a single entry. That is the point of bonus entries, and it is also what a losing Entrant will ask
about. Weight when the campaign rewarded effort and the terms said so. Draw unweighted when the Prize is large
enough that the optics matter more than the reward, and put the choice in the audit note either way.

## Checking it without the script

Each Entrant gets a sortable key from a hash of the seed and their id. Sort by key, highest first, ties broken by id, and the first Entrants fill the tiers in order, then the backups. Ten lines in Python, JavaScript or Go reproduce it, and the audit record lists every Winner's key for comparison.

```
u = first 8 bytes of SHA-256(seed + "|" + lowercase trimmed id), read as an unsigned integer
u = (u + 0.5) / 2^64
key = u ^ (1 / weight)   # weight = 1 when unweighted
```

Anyone can run one line and check the audit record holds the same key for the same person. Worked example with seed `seed-2026` and Entrant id `ann`:

```
printf '%s' 'seed-2026|ann' | shasum -a 256
→ 2c7bf4025594c526ab0099a90d19078a9be42ced94b2583e3d1b781f6d20cacd
first 8 bytes 2c7bf4025594c526 → 3205423850667164966
u = (3205423850667164966 + 0.5) / 2^64 = 0.1737663751
```

Unweighted, that is the Entrant's key.

Deduplication is per identifier column. The script merges rows that match on the one column named by `--id-column`, so somebody who entered by email on one action and by handle on another counts twice unless the dataset links the two into one row. Pick the column that is unique per person in your file, and where the dataset carries both, merge them before you commit.

## After the draw

- Verify each drawn Entrant against the terms before calling them a Winner: required action completed, eligible region, age, one account.
- Contact by the channel the Entrant gave. Two attempts, the second sent halfway to the reply deadline from the terms, then forfeiture and the next backup. On a seven-day deadline that puts the attempts about 72 hours apart.
- If backups run out, hold a second draw with a new seed, recorded as draw 2, from the same frozen list minus everyone already drawn.
- Announce first names and city, or handles, with consent. Never publish the Entrant list.
- Keep the input file, the exclusions file, the audit JSON and the announcement together for as long as the terms or local law require.

## Comment-based draws

Exports from social comments carry duplicates, replies and the organizer's own comments. Deduplicate on handle, drop the organizer's account, and decide whether multiple comments count once or add up before drawing. Tag-a-friend entries count once per commenter unless the terms say otherwise.

## Disputes

Answer with the record: the input hash, the seed and where it came from, the method, and the audit file. A dispute about eligibility is settled by the terms and the verification step. A dispute about the draw itself is settled by rerunning the script with the same file and seed in front of the person asking.

## Audit note template

"Draw for [campaign] held on [date, time, time zone]. Entries closed at [time]. Input file [name], SHA-256 [hash], [N] rows, [M] unique eligible Entrants after merging [D] duplicates and excluding [E] entries under [rule]. Method: seeded random draw ([tool and version]), seed [value] taken from [source]. Winners: [tier, identifier]. Backups: [list]. Drawn by [name], witnessed by [name]."
