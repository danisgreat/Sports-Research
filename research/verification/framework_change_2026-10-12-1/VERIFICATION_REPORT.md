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

## Phase D (R24–R25, R28–R32) and the CR-R2 rules edit, checked 2026-10-12 about 22:40 AEDT before commit

| Check | Result | Evidence | Limitation |
|---|---|---|---|
| R24, R25, R28 already shipped | PASS | Wording and rules found in CURRENT_STATE, HYPOTHESIS_REGISTER v3, CURRENT_RULES §5 and prompt 1 at `93b4b52e6`; the implementation map rows were stale and are corrected | — |
| NBL 2025 cell trace | PASS | 372 changed cells against `git show HEAD:`; each matches a log line (old and new value); 0 unlogged, 0 logged-but-absent | — |
| NBL 2025 shape | PASS | 0 blank dates, 0 weekday mismatches; `Game Type = Regular Season` gives 165 games, 33 per team | Start times blank by design |
| NBL post-season dates | PASS | 14/14 dates (home-club local) and scores re-read from the ESPN summary endpoint at this check | ESPN is evidence B; the NBL owner page loads scores client-side |
| KBO 2025 innings against the owner | PASS after correction | KBO scoreboard service read for all 779 completed games: final scores 779/779; innings 777/779 before correction. The 2 differences were MyKBO-derived values (10 innings for two 9-inning games), now reverted | Line-score columns not filled |
| KBO 2025 stage labels | PASS | Owner series codes (srId 0/4/3) and the 2025 KBO season article agree: regular season from 22 March (5 rows relabelled), NC is the Wild Card loser and SSG the Semi-playoff loser (7 rows swapped back; the postponed 2025-10-10 row by series membership) | 2000–2024 stage labels not checked |
| KBO 2025 cell trace | PASS | 148 changed cells, each traced from main's value to the final value through the MyKBO log, then the owner correction log | The CHECK_TIE_NOT_AT_CAP and UNMATCHED lines in the MyKBO log are notes, not cell changes. The owner confirms all four ties: three at 9 innings, one at 10 |
| NPB 2025 innings against the owner | PASS | npb.jp box score at each row's own URL: 878/878 parsed, scores 878/878 agree; the inning-cell count agrees with the printed "( N innings )" note in all 109 non-9 games; 109 rows repaired (214 cells) | Line scores kept in the evidence file only |
| NPB 2025 stage labels | PASS | Two 11 October games print a new series counter ("Game 1"), while regular-season pages print the season head-to-head count. They are relabelled Climax Series, giving 858 regular-season games at 143 per team (8 cells) | — |
| Only intended rows changed | PASS | `git diff --numstat`: NBL 179, KBO 78, NPB 111 lines. These equal the rows with changed cells; the index stays LF | — |
| Czech Extraliga profile row | PASS | Recomputed from the three yearly files: every printed figure matches | Single compiler |
| CURRENT_RULES user edit | RECORDED | The LATE_START band paragraph and the T−5 freeze limit were removed by the user; two mechanical fixes only (blank lines; ". Update"). Classed PROCEDURE → CR-2026.10.12-R2; R1 archived byte-identical | Prompt 1 sport sections, the card template's "Scheduled lead / band" field and SCORING still name the T−5 / LATE_START terms (see CHANGELOG) |
| Status register byte custody | PASS | GAME_LOG_STATUS_CURRENT (`-text`): 2 lines changed, 1 inserted; CRLF 88 → 89; no other byte changed | — |
| Unrelated work preserved | PASS | NBA G League build, its SOURCES §3.33, `research/src/`, the user's prompt-1 edit and `MODEL_PROBABILITY_ML_RECOMMENDATIONS_2026-10-12.md` left unstaged | — |
| Helpers | DISCLOSED | Read-only checks and the cell-level apply steps ran from Python helpers in the session scratch area, outside the repository (CONTRIBUTING). Their rules are as follows: change only `Innings Played` and `Extra Innings`, and only where the owner differs and the final score agrees; keep the file's line ending; log every cell | — |
