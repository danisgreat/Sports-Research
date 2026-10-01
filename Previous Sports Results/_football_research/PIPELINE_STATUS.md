# Archive implementation status

Updated 2026-10-01 (Australia/Sydney).

The former zero-byte helpers were never completed implementations. Their exact
original bytes and the retired AFL/AFLW award-enrichment builders are preserved
under `../_custody/originals/`, indexed by original SHA-256 and path.

The helper filenames remain compatibility entry points. `audit_*`, `master_audit`
and `test_marquee` invoke the canonical validator. Other former `generate_*`,
`update_*` and `standardize_headers` helpers invoke the canonical builder. They do
not claim to collect full rosters, appoint officials or rewrite all seasons.

The implemented workflow is in `../../research/src/archive.py` and
`../../research/src/archive_sources.py`. From the repository root:

```powershell
python -B -m research.src.archive repair
python -B -m research.src.archive build
python -B -m research.src.archive validate
python -B -m research.src.archive_sources profiles
python -B -m unittest discover -s research/tests -p test_archive.py -v
```

`repair` changes only exact matches covered by retained field-owner evidence and
records original and corrected hashes in an append-only correction journal.
`build` verifies source bodies, creates numeric result tables, separates all
prose/people/awards and excludes unsupported, duplicate, mirrored and subset
records from training. Exports are staged before publication and a hashed
manifest is written last. Readers fail closed when exports differ from it.

`collect.py` remains the earlier football evidence collector. Every cache read now
requires its exact URL/body receipt and SHA-256. Its HTML collection modes still
require the documented optional `requests` and `beautifulsoup4` dependencies.
The canonical builder, source verifier, official MLB schedule collector and
supported fixed official correction collectors use Python's standard library.

`refresh-supported` appends only missing completed MLB regular/finals results
from the retained official schedule. It leaves boxscore, people and condition
metadata blank. `inventory` independently measures the yearly input files.

Broad college-football postseason collection, match-level coaching and official
appointments, historical injury/lineup snapshots and most competition result
collections remain incomplete. The college collector now explicitly fetches the
supported official Dublin boxscore rather than generating fictional seasons.
