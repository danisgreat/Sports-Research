# NBA evidence release verification

Final audit documentation time: 2026-10-17T02:50:07.111966+00:00. This is an evidence publication with open gaps, not ingestion, fitting or qualification.

- 27,832 source/game rows, 9,600 reconciled groups, 1,199,155 long team/stat observations.
- 25 whole-dataset mechanical/quality checks PASS; raw bytes/hashes for 12,032 external captures agree. Corrupted nonfinal, backdated-known-at and altered-capture negative checks reject their in-memory examples.
- All seven completed regular-season fixture populations agree with the independent team-log denominator: 8,289 finals. Candidate feature mask: 8,235; no training admission is claimed.
- Independent original-capture spot checks: 4,292 fields / 90 selected event keys / 252 opened captures, all PASS. The exact inspected remainder and method are explicit; this sample is not labelled exhaustive source-truth validation.
- 62,008 paired period checks include 4 observed disagreements. 3 upstream box arithmetic issues remain preserved. Source values are never repaired to balance equations; quality gates exclude affected derived candidates.
- One final-score conflict remains quarantined: Toronto–Houston Orlando scrimmage NBA0011900111, ESPN 93–84 versus NBA archive 94–83. 75 events retain component/period/sentinel issues. No majority-vote grade or forced result is adopted.
- 5,318 current field requirements remain OPEN. These include absent IDs, non-final/stale sources, incomplete independent final corroboration and single-source regulation/quarter fields. Publication does not declare those facts complete.
- All 2,195 pre-existing tracked working files are byte-identical to the opening inventory, including shared learning/model stores, canonical logs and the unrelated dirty Prompt 1 edit. Only this new evidence folder and the new collection/training framework are intended for publication.
- The external audit notebook executed top-to-bottom, passes nbformat validation and its saved output contains the same measured totals. Helpers/raw/cache/notebook are external; Git contains sporting facts, provenance, quality records and the framework only.

FILE_HASHES.csv records complete raw output identities except itself, including the other-league framework. The verified-history tree has text unset (-text); staged and remote blobs are checked against those raw identities at publication. Publication commit and fresh remote readback are reported only after they actually occur. No executable repository code changed, so model tests or fitting were not invoked for this data-only release.
