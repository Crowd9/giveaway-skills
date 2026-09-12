# Getting your Entrant list

The draw needs one file that names every eligible person once per entry. This page covers where that file comes from and what to check before committing to it. Advice from practice, checked September 2026. Export tools change, so confirm the field names in your own file.

## What the script accepts

- CSV or TSV with a header row, including files with just one column. Keep the `.csv` or `.tsv` extension so the script treats the first row as a header. Say which column names the person with `--id-column` if it is not obvious. A requested column missing from the header stops the script.
- One name, handle or email per line, no header. Save this as `.txt` and omit `--id-column`. The internal column for a plain list is `entrant`. For files without a `.txt` extension, a recognized field name such as `email` on the first line is treated as a header. Use `.csv` or `.tsv` for headered files to avoid ambiguity.
- JSON from a comment or Entrant export. The script finds the list inside the file and picks the person field by looking for, in order: `email`, `username`, `user_name`, `handle`, `authorChannelId.value`, `authorDisplayName`, `author_name`, `author`, `commenter`, `owner`, `user`, `entrant`, `name`, then `id`. Nested objects are flattened with dots, so `from.username` and `snippet.topLevelComment.snippet.authorChannelId.value` both resolve. If the guess is wrong, pass `--id-column` with the dotted path.

Run `commit` first. It prints the column it chose, so a wrong guess shows up before the seed exists.

## Spreadsheets

Google Sheets: File, then Download, then Comma Separated Values. Excel and Numbers: Save As or Export to CSV. Export the one sheet that holds Entrants, with a header row, and keep that downloaded file as the frozen input. A live sheet keeps changing and its hash will not match later.

If bonus entries live in a column, name it with `--weight-column`. If the sheet has a column of formulas, the dataset holds the values, which is what you want.

## Your giveaway platform

A Gleam Actions export has one row per completed action with an Entries column for its worth and a Status column. The results-review skill's `gleam_export.py --entrants-csv entrants.csv` writes the valid rows as email and entries, and the draw script adds the entries up per person with `--weight-column entries`, so bonus entries carry their weight and invalid rows never enter the draw. Its summary counts a row whose Entries is missing, blank, nonnumeric, nonpositive or non-finite at zero and reports how many there were. Its draw export refuses the file until those rows are corrected from the campaign records. Valid fractional weights are preserved in both.

Every hosted giveaway tool has an Entrant or users export, usually CSV, with an email column and an entries column. Export once after close, name the email column with `--id-column` if the header is unusual, and use the entries column as the weight. Platform-specific notes belong in your platform's own help pages.

## Comment giveaways

Comment exports are the messy case. There is no built-in "download comments" button on the major networks for ordinary accounts, so the file comes from an API call or a third-party picker tool. Whatever the source, the rules are the same: export once after close, keep the file, and deduplicate by account, since one person can comment many times.

| Network | Where the file comes from | Field that names the person |
|---|---|---|
| Instagram | Instagram Graph API comments edge on the media object, for Business or Creator accounts connected to a Facebook Page. Third-party comment picker tools export CSV or JSON from the same source. | `username`, or `from.username` on newer API versions |
| Facebook | Graph API comments edge on the Page post. Third-party tools again. | `from.name` and `from.id` |
| YouTube | YouTube Data API `commentThreads.list` with the video id. Google Takeout only holds your own comments. | `authorChannelId.value` (unique) or `authorDisplayName` |
| TikTok | No comment export for creators. Third-party tools scrape the public comment list and export CSV or JSON. | Usually `username` or `unique_id` |
| X | API v2 recent search filtered by `conversation_id`, on a paid tier. Third-party tools. | `author_id` or `username` |
| Discord | Giveaway bots hold the Entrant list. Export it with the bot's command, or copy the reaction user list. | Discord user id |

Prefer a unique id over a display name where both exist. Display names repeat and change, ids do not.

## A worked example on plain handles

Eleven handles from a comment thread, one of them the organizer's own account, drawn for one Winner with two backups. Two files, three commands, and the output as the script printed it. The drand round here is a past one chosen so the example reproduces; a real draw commits to a round in the future, as `draw-procedure.md` sets out.

`handles.txt`:

```
@maya_reads
@tomcooks
@lena.k
@dev_arjun
@sunny_side_up
@kofi_b
@the_real_priya
@marcus.v
@jo_runs
@ella_makes
@brand_official
```

`organizer.txt`:

```
@brand_official
```

```
$ python3 draw.py commit handles.txt --exclude organizer.txt --winners 1 --backups 2
input sha256   c8bacebf4c4bd5df5d49c5b7acd558182fe5bdbfe295925e4f7ee3a491f37721
rules          {"backups": 2, "exclude_file_sha256": "40f1c59455ac72c02922e18b088214802877d75a88d1d2667b111788f40a50d0", "id_column": "entrant", "method": "sha256(seed|id) -> u in (0,1); key = u^(1/weight); highest keys win; ties by id", "tiers": [["Winner", 1]], "tool_version": "2.4.2", "weight_column": null}
commitment     a8adf63be0a5872e2d03c57f35910be387629330b0dd66d258f170f8589d4471
rows_read 11, unique_eligible 10, duplicates_merged 0, excluded 1, rows_with_invalid_weight 0

Reconcile eligibility and earned weights with the published rules before publishing this commitment. Publish before the seed exists, then keep the input file unchanged.

$ python3 draw.py draw handles.txt --exclude organizer.txt --winners 1 --backups 2 --seed-drand 6458188 --audit audit.json
Winner: @ella_makes
Backup 1: @lena.k
Backup 2: @tomcooks

rows_read 11, unique_eligible 10, duplicates_merged 0, excluded 1, rows_with_invalid_weight 0, seed source drand, commitment a8adf63be0a5872e...
audit written to audit.json

$ python3 draw.py verify audit.json --exclude organizer.txt
ok   drand round 6458188 randomness matches the public beacon
ok   recomputed all 3 committed places, including order and tier assignments
PASS
```

Read the counts back: 11 rows read, 1 excluded (the organizer), 10 unique eligible, 3 committed places, and verify recomputes all three from the committed rules and the public beacon. The commitment printed by `commit` is what you publish before the round exists, and the same value appears in the draw output, which is how a reader ties the two together.

## Checks before committing

- Open the file and read ten rows. Confirm the person column, the count, and that the last comments before close are present.
- Remove entries after the close time. If the dataset has a timestamp column, filter on it before the draw and say so in the audit note.
- Decide the duplicate rule. The script merges exact matches after trimming and lower-casing. It flags plus-addressed emails but does not merge them.
- For a comment or social draw, drop the organizer's own account from the list before committing. A handle matching the brand's account is not an Entrant, whether or not the user named it as an exclusion.
- Put staff, partners and previous Winners in the exclusion file, one id per line, using the same identifier as the Entrant file.
- Save the file with a dated name and never edit it after `commit`. Any fix means a new commit before the seed exists.
