# Getting your entrant list

The draw needs one file that names every eligible person once per entry. This page covers where that file comes from and what to check before committing to it. Advice from practice, checked September 2026. Export tools change, so confirm the field names in your own file.

## What the script accepts

- CSV or TSV with a header row. Say which column names the person with `--id-column` if it is not obvious.
- One name, handle or email per line, no header.
- JSON from a comment or entrant export. The script finds the list inside the file and picks the person field by looking for, in order: `email`, `username`, `user_name`, `handle`, `authorChannelId.value`, `authorDisplayName`, `author_name`, `author`, `commenter`, `owner`, `user`, `entrant`, `name`, then `id`. Nested objects are flattened with dots, so `from.username` and `snippet.topLevelComment.snippet.authorChannelId.value` both resolve. If the guess is wrong, pass `--id-column` with the dotted path.

Run `commit` first. It prints the column it chose, so a wrong guess shows up before the seed exists.

## Spreadsheets

Google Sheets: File, then Download, then Comma Separated Values. Excel and Numbers: Save As or Export to CSV. Export the one sheet that holds entrants, with a header row, and keep that downloaded file as the frozen input. A live sheet keeps changing and its hash will not match later.

If bonus entries live in a column, name it with `--weight-column`. If the sheet has a column of formulas, the export holds the values, which is what you want.

## Your giveaway platform

Every hosted giveaway tool has an entrant or users export, usually CSV, with an email column and an entries column. Export once after close, name the email column with `--id-column` if the header is unusual, and use the entries column as the weight. Platform-specific notes belong in your platform's own help pages.

## Comment giveaways

Comment exports are the messy case. There is no built-in "download comments" button on the major networks for ordinary accounts, so the file comes from an API call or a third-party picker tool. Whatever the source, the rules are the same: export once after close, keep the file, and deduplicate by account, since one person can comment many times.

| Network | Where the file comes from | Field that names the person |
|---|---|---|
| Instagram | Instagram Graph API comments edge on the media object, for Business or Creator accounts connected to a Facebook Page. Third-party comment picker tools export CSV or JSON from the same source. | `username`, or `from.username` on newer API versions |
| Facebook | Graph API comments edge on the Page post. Third-party tools again. | `from.name` and `from.id` |
| YouTube | YouTube Data API `commentThreads.list` with the video id. Google Takeout only holds your own comments. | `authorChannelId.value` (unique) or `authorDisplayName` |
| TikTok | No comment export for creators. Third-party tools scrape the public comment list and export CSV or JSON. | Usually `username` or `unique_id` |
| X | API v2 recent search filtered by `conversation_id`, on a paid tier. Third-party tools. | `author_id` or `username` |
| Discord | Giveaway bots hold the entrant list. Export it with the bot's command, or copy the reaction user list. | Discord user id |

Prefer a unique id over a display name where both exist. Display names repeat and change, ids do not.

## Checks before committing

- Open the file and read ten rows. Confirm the person column, the count, and that the last comments before close are present.
- Remove entries after the close time. If the export has a timestamp column, filter on it before the draw and say so in the audit note.
- Decide the duplicate rule. The script merges exact matches after trimming and lower-casing. It flags plus-addressed emails but does not merge them.
- Put staff, partners and previous winners in the exclusion file, one id per line, using the same identifier as the entrant file.
- Save the file with a dated name and never edit it after `commit`. Any fix means a new commit before the seed exists.
