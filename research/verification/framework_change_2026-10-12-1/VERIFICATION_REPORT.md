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

## Phases B and C (R08–R23, R26–R27, R33–R38, PR-01–PR-10, NEW-01), checked 2026-10-12 about 15:10 AEDT before commit

| Check | Result | Evidence | Limitation |
|---|---|---|---|
| Archived originals = base | PASS | 42 files compared byte-for-byte with `git show eb1acf58b:<path>`: 0 mismatches. The earlier same-day subfolders `prompt1_per_sport/` and `prompts_github_readonly/` were left untouched | — |
| Relative links and anchors, live set | PASS | 542 links in 60+ live documents (operating files, prompts 1–8, examples, sport files, change folder): 0 problems. New CHANGELOG entries: 8 links, 0 problems | Dated CHANGELOG entries and the status register's dated sections keep their historical links. All are mapped in HISTORICAL_LINK_INDEX's 2026-10-12 recovery map, and every Git recovery was checked |
| Version strings consistent | PASS | MDS-2026.10.12-v11.0 in README, CURRENT_STATE, METHOD, CURRENT_RULES, the template and the example; P-2026.10.12-v11.0 in PROMPTS, the prompt index, prompt 1, CURRENT_STATE and README; no live control still names v10 as current | Historical mentions (dated sections, archive) intentionally keep v10 |
| Example pair | PASS | Active (11,052 bytes) is an exact prefix of settled (16,534 bytes): `cmp -n` | Synthetic only |
| Prompt-1 edit counts | PASS | Scripted replacements asserted the expected occurrences (10 per shared sentence, 1 per sport-specific line) before writing | — |
| Line endings of edited files | PASS with note | Uniform files stayed uniform. GAME_LOG_STATUS_CURRENT (`-text`, mixed) was edited at byte level: 80 → 88 CRLF lines, only the 1 changed line and the 8 inserted lines differ | A first editor attempt converted the whole file and was caught and repaired before staging (fixture F18) |
| `git diff --check` | PASS with documented exception | No whitespace errors except GAME_LOG_STATUS_CURRENT lines 4 and 69–76, where git reports the CR of a CRLF ending as trailing whitespace. Those lines deliberately match the CRLF style of the surrounding current-queue section in a byte-exact file | — |
| No code/JSON/HTML added | PASS | Staged list checked by extension at commit | — |
| Issued logs, cards, dated reports, P-IDs unchanged | PASS | No path under `prediction logs/`, `research/issued_research/` or earlier dated folders in the diff | — |
| Unrelated work preserved | PASS | `MODEL_PROBABILITY_ML_RECOMMENDATIONS_2026-10-12.md` (untracked, created 13:45 by another writer) and the root `AUDIT_RECOMMENDATIONS_2026-10-12.txt` are not staged | — |
| Fixtures | PASS (manual) | F01–F32 walked by hand; F09, F11 and F27 recomputed | Manual walkthroughs, not an executed test suite |
