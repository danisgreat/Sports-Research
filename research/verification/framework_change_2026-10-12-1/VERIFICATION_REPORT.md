# Verification report — framework change 2026-10-12-1

Format: `Check | PASS/FAIL/NOT_VERIFIED/N/A | evidence | limitation` (VERIFICATION_PROTOCOL). The checks were run by this session with plain git/file commands and CSV-aware reading in a scratch area outside the repository. **A green check proves only what it checks**. None of these is a predictive or live-sports validation.

## Phase A (R01–R07), checked 2026-10-12 about 13:40 AEDT before commit

| Check | Result | Evidence | Limitation |
|---|---|---|---|
| Pre-change inventory recorded | PASS | Quarantine `git_status_before.txt` (107 M, 12 ??), base `eb1acf58b` = fetched `origin/main` | — |
| Unpublished work preserved before any change | PASS | 107 byte copies + 23.5 MB patch + 320 moved files; quarantine README | Outside git; the user owns its retention |
| Rebuilt CSVs: logical rows, CSV-aware | PASS | Hockey 18,752 / football 20,740 via a CSV parser, not physical line counts | — |
| Duplicate IDs | PASS | 0 / 0 | — |
| Quarantined defaults absent | PASS | 0 non-blank start time, attendance or referee (hockey); 0 Shield rows, 0 odds-named columns, half-time blank where the source lacks it (football) | — |
| Date ↔ weekday | PASS | 0 disagreements in both | Printed-weekday conflicts in the hockey source are flagged separately (10) |
| League-size / games-per-team | PASS | Football all 51 seasons. Hockey all except 5 documented source defects | — |
| Cross-compiler agreement (football) | PASS | 11,943 / 11,944; 1 date-only difference explained | Upstream independence not audited |
| External samples | PASS | Hockey 8/8 (cs.wikipedia 2023-24 play-offs); football 9/9 (ESPN API) | Sample only |
| No code/JSON/HTML staged | PASS | Staged list checked by extension before commit (see commit) | — |
| `git diff --check` on touched paths | PASS | No whitespace errors | — |
| Line endings | PASS | Edited docs not mixed (`file`, `git ls-files --eol`); new CSVs LF like the placeholders they replace | — |
| Relative links in new docs | PASS | 38 checked, 0 problems once this report exists. 42 pre-existing broken links in CHANGELOG (38), SOURCES (3) and the archive README (1) are the audit's R36 and are handled in phase C | Anchors checked with GitHub-style slugs |
| Archived originals = base | PASS | `cmp` against `git show HEAD:<path>` for SOURCES, ARCHIVE_USE_GUIDE, CONTRIBUTING, the archive README and CHANGELOG | — |
| Issued logs, cards, dated reports, P-IDs unchanged | PASS | No path under `prediction logs/`, `research/issued_research/`, dated retrospectives or earlier change folders is in the diff | — |

Later phases append their own sections below.
