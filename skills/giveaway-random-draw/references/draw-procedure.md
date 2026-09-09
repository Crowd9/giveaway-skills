# Draw procedure

Advice from practice. Sweepstakes and lottery law differs by jurisdiction. This is not legal advice.

## Before the draw

- Close entries at the time and time zone in the terms. Export the list once and keep that file. Record its hash (the script prints it).
- Decide the deduplication rule before looking at names. Common choices: one chance per email, or entries add up when the terms promised bonus entries.
- List exclusions in a separate file: staff and their households, previous winners if the terms bar them, entrants from ineligible regions, entries flagged as automated.
- Decide tiers and backups. Two backups per tier covers most no-reply cases without a second draw.
- Pick the seed and, if the terms or a partner require it, publish it before drawing.

- Expect some entries to fail verification. Across ordinary campaigns in the export the median campaign had 3.8% of entries marked invalid, and referral-heavy mixes ran higher. Draw from valid entries only, and treat a drawn name as a winner only after the entry checks out.

`commit` also prints review lines for disposable email domains, one domain holding a fifth or more of the list, and runs of handles that differ only by a trailing number. They are prompts to look, never verdicts. Decide what to exclude, update the exclusion file, then commit again.

## Why commit first

A draw is provable when three things hold: the entrant list and rules were fixed before the seed was known, the seed came from somewhere the organizer could not steer, and the selection from seed to winners is a fixed calculation anyone can redo. The script does all three. `commit` hashes the frozen file and the rules into one value to publish. The seed comes from a public randomness beacon whose round was named in advance. The selection is a hash ranking, so the audit record plus the file reproduces the winners in any language.

## Seed sources

| Source | How | Fits when |
|---|---|---|
| drand beacon (League of Entropy) | `commit --draw-at` prints the round number due at that time. Publish it. After that time, `draw --seed-drand ROUND` fetches the round's randomness from api.drand.sh and records the signature. Rounds are every 30 seconds and anyone can refetch a round forever. | Default choice. Free, no account, publicly verifiable. |
| NIST Randomness Beacon | Announce a future minute. `draw --seed-nist UNIXTIME` fetches that pulse's output value. Pulses are every 60 seconds and signed by NIST. | Audiences that prefer a government source. |
| A value published by a third party | A partner or witness emails a phrase before the draw, or a closing index value on a named date. `draw --seed "the value"`. | Co-sponsored giveaways with no internet at the draw. Keep the email. |
| RANDOM.ORG | Third-Party Draw Service runs the draw and publishes a record for at least five years without exposing entrants. The Signed API can also pre-commit with tickets and returns results signed with RANDOM.ORG's key. Paid, needs an account. | Organizers who want a named independent party rather than their own script. |

Do not let the script or the organizer generate the seed. A generated seed can be regenerated until the result pleases.

## Running it

```bash
# 1. Freeze the list, then commit and announce the drand round for the draw time
python3 scripts/draw.py commit entries.csv --tiers "Grand prize:1,Runner-up:5" --backups 2 \
  --id-column email --weight-column entries --exclude staff.txt --draw-at "2026-09-12T09:00:00+10:00"

# 2. After that time, draw once
python3 scripts/draw.py draw entries.csv --tiers "Grand prize:1,Runner-up:5" --backups 2 \
  --id-column email --weight-column entries --exclude staff.txt \
  --seed-drand 6452000 --audit draw-2026-09-12.json --winners-csv winners.csv --mask

# 3. Anyone with the same files can check
python3 scripts/draw.py verify draw-2026-09-12.json --exclude staff.txt
```

One draw. If the tool errors (too few eligible entrants, wrong column), fix the input, commit again, and keep only the final run.

## Checking it without the script

For each eligible entrant: u = the first 8 bytes of SHA-256(seed + "|" + lowercase trimmed id), read as an unsigned integer, plus 0.5, divided by 2^64. Key = u raised to the power 1/weight (weight 1 when unweighted). Sort by key, highest first, ties broken by id. The first entrants fill the tiers in order, then the backups. Ten lines in Python, JavaScript or Go reproduce it, and the audit record lists every winner's key for comparison.

## After the draw

- Verify each drawn entrant against the terms before calling them a winner: required action completed, eligible region, age, one account.
- Contact by the channel the entrant gave. Two attempts, a reply deadline from the terms (72 hours is common), then forfeiture and the next backup.
- If backups run out, hold a second draw with a new seed, recorded as draw 2, from the same frozen list minus everyone already drawn.
- Announce first names and city, or handles, with consent. Never publish the entrant list.
- Keep the input file, the exclusions file, the audit JSON and the announcement together for as long as the terms or local law require.

## Comment-based draws

Exports from social comments carry duplicates, replies and the organizer's own comments. Deduplicate on handle, drop the organizer's account, and decide whether multiple comments count once or add up before drawing. Tag-a-friend entries count once per commenter unless the terms say otherwise.

## Disputes

Answer with the record: the input hash, the seed and where it came from, the method, and the audit file. A dispute about eligibility is settled by the terms and the verification step. A dispute about the draw itself is settled by rerunning the script with the same file and seed in front of the person asking.

## Audit note template

"Draw for [campaign] held on [date, time, time zone]. Entries closed at [time]. Input file [name], SHA-256 [hash], [N] rows, [M] unique eligible entrants after merging [D] duplicates and excluding [E] entries under [rule]. Method: seeded random draw ([tool and version]), seed [value] taken from [source]. Winners: [tier, identifier]. Backups: [list]. Drawn by [name], witnessed by [name]."
