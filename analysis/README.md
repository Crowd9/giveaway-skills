# Analysis

The JSON files under `output/` are the aggregate findings the skills quote. Every skill reference cites the file and the block a figure came from, so any number in the skills can be traced to the table behind it.

Each file holds counts, medians and percentile tables for one topic: benchmarks, percentiles, entry-method mix, prize economics, timing and the calendar, industries and verticals, organizer history, thresholds, templates and campaign types. `benchmarks.md` is a readable summary of `benchmarks.json`.

Two rules hold across all of them:

- **Aggregates only.** No row describes fewer than five distinct businesses, so no row describes one company. Groups below that floor are counted and not described.
- **Description, not cause.** Every figure says what campaigns did, never what caused a result. The skills state that alongside the numbers.

Sample sizes sit next to every figure. Where a field is missing on some campaigns the count for that figure is lower, and the file carries its own `n`.


## Complementary suppression

A null cell with `suppressed_below_floor` is withheld, including a larger cell
whose publication would reveal a smaller group by subtraction. Preserve these
markers and skip null rows when rendering reference tables. Do not replace a
withheld value with zero or restore it from an older export.

`scripts/privacy_floor.py` checks documented parent/subset conventions within and
across the committed files. It checks individual campaign and business count
differences and campaign sums for declared disjoint partitions. Business counts
are never summed across campaign groups because the same business can recur.
A business count difference is a disclosure warning, not the number of businesses
behind all residual campaigns. Action-level asset refinements use only business
support when compared with campaign totals.

Every generator that writes these files needs the same complementary suppression before export, and the reference renderer must omit withheld cells and the prose quoting them.
Check the outputs together after regeneration. A generator passing its own
row floor is insufficient when another file publishes an overlapping total.

The gate cannot certify arbitrary intersections of non-nested groups, business
unions, missing distinct-business support, or equations involving rounded shares
and overlapping totals. Enrichment tables and older cohort snapshots also use
different dates, labels and exclusions, so similar labels and nearby counts do
not prove a subset relationship. These patterns still require a private,
membership-aware disclosure review before further exports. The gate does not
certify historical releases or information published outside this tree.
