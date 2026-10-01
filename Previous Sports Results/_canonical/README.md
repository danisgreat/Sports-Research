# Canonical historical results

This directory contains the conservative archive interface used for historical
result labels. Raw yearly CSVs remain the input layer, with 230 corrected rows and
two appended completed MLB results recorded under `../_custody/corrections.jsonl`.
The exact original bytes are retained separately. Corrections include 222
Brisbane Bears identities from 1987-1996, two transposed AFL dates in 1905,
three AFLW team aliases, both copies of the 2025 Dublin college-football score,
and the NFL Brazil game's neutral venue. All require retained field-owner evidence.

| Output | Meaning |
|---|---|
| `events.csv` | One canonical result identity, separate numeric designated-home/away scores, stage, endpoint, date/time precision, source receipt, quality and training admission |
| `narratives.csv` | Original prose and notable people, always excluded from pregame features |
| `provenance.csv` | Every input row mapped to canonical identity, admission and duplicate/mirror/subset exclusion |
| `seasons.csv` | Measured row coverage, lifecycle evidence basis, independently matched source scope, missing source events and incomplete seasons |
| `manifest.json` | All raw inputs, outputs, parser and transformation hashes, snapshot identity, all 1,615 source receipt hashes and their 1,614 retained-body hashes, measured counts and source-record errors |

Run `python -B -m research.src.archive build` from the repository root to rebuild.
The four bulky event/narrative/provenance/season exports are ignored build products;
the manifest counts, raw inputs and retained source custody make the
same local snapshot reconstructible. Source endpoints can change later: retain
the exact bodies to reproduce a historical snapshot.

`research.src.archive.read_events()` validates the committed export hash and
returns admitted labels by default. `eligible_only=False` exposes quarantined
records for review. Validation checks every raw input, implementation,
transformation input, original backup and all retained source bodies, including
unused ones. One legacy NFL receipt explicitly has no retained body and cannot
verify results. Publication is staged and the manifest acts as the last commit
marker; interruption produces a detectable mismatch, never silently accepted
partial data.

Training admission applies only to verified full-game result labels for regular
seasons and finals. It does not certify complete season populations, predictive
skill or permission to use every column as a feature. Early college-football
curated subsets, exhibitions, pre-founding records, missing numeric scores,
source mismatches, duplicate/mirrored/subset rows and unresolved arithmetic are
excluded. There is no inference that an empty file proves the competition was
not held.

`available_at_utc` is unknown for historical source publication. `retrieved_at_utc`
is custody time and never pregame availability. Date-only labels may be used
under the explicit contract that rolling features use strictly earlier event
dates and never another event on the forecast date. Scheduled/actual timestamps,
venue sponsorship names, actual starting pitchers, same-game statistics,
comments, awards and participation are not historical pregame snapshots.

Final scores include overtime or extra innings as indicated by the endpoint.
Special exhibition tiebreakers are excluded from the regular/finals contract.
`neutral_venue` stays missing when evidence does not establish it. A designated
home team does not establish home-field advantage. Team source IDs are used
where retained field-owner evidence supplies them; otherwise exact normalized
aliases provide stable competition-scoped IDs without merging distinct clubs.
`parser_version` and `source_parser_version` identify both transformations.

`complete_verified_result_scope` means every completed regular/finals result in
the registered retained source population matched. It does not cover exhibitions
or all metadata. Live 2026 MLB stays a snapshot rather than a completed season.
Most competitions have no complete source population registered and remain
partial or unavailable. The archive's old league/season narrative documents are
research material pending field-level sourcing and timing checks.
