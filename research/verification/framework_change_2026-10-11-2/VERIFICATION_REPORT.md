# Verification record: run 2 (NBL profile refresh and data audits), 2026-10-11

Base `abb3e98d7ab2dfc3bd33bcdf42b4a3bf3a11a7d4` (local, unpushed v10) on `2d6d86350ce4d6bd9f4ae0f34a42351e71ff0e4b` (published). Worktree clean at start. Checks below were run after the last edit to the files they concern; results are as printed.

## 1. Scope and protected bytes (VERIFICATION_PROTOCOL §6.1)

| Check | Result |
|---|---|
| Changed tracked files | `ARCHIVE_USE_GUIDE.md`, `CHANGELOG.md`, `CURRENT_STATE.md`, `HYPOTHESIS_REGISTER.md`, `LEAGUE_PROFILES.md`, `SOURCES.md` (numstat added/removed: 14/1, 14/0, 1/1, 11/1, 31/6, 16/14; every removed line is one deliberately replaced) |
| New paths | `Previous Sports Results/Basketball/NBL/2026/2026_games.csv`; `archive/superseded_2026-10-11/profile_refresh/` (7 files incl. note); `research/verification/framework_change_2026-10-11-2/` (6 files: proposal, implementation, two audits, the date-evidence sidecar, this report) |
| Protected paths changed | None: no change under `prediction logs/`, `research/issued_research/`, the retrospective, the v10 or earlier verification folders, or any pre-existing file in `Previous Sports Results/` |
| Archived originals | The six archived copies are byte-identical (SHA-256) to the committed blobs at `abb3e98d7` |
| Code, JSON, notebooks, scripts | None tracked or untracked (`.py`, `.json`, `.jsonl`, `.ipynb`, `.js`, `.sh`); the parsing and generating scripts ran from a scratch folder outside the repository and were not added |
| New log entries / P-IDs | None; next canonical ID still P-580 |

## 2. Format and text checks

| Check | Result |
|---|---|
| `git diff --check` on tracked changes | no findings |
| Trailing whitespace in new Markdown | 0 lines in every new file |
| Links in changed and new documents | All resolve, except pre-existing historical references in SOURCES to removed files (`research/sources_registry.json`, `research/src/sources.py`, a removed observations file) and in older CHANGELOG entries; the links added by this run resolve (re-checked after this report was written) |
| Version strings | `LP-2026.10.11-v2` is the only new version string; it appears consistently in LEAGUE_PROFILES, HYPOTHESIS_REGISTER, CURRENT_STATE and CHANGELOG. MDS-2026.10.11-v10.0, CR-2026.10.11-R1, SCV-2026.10.11-v6 and SEL-2026.10.11-v2 are untouched |
| Contradiction search of the live set | No live document still quotes the withdrawn extras shares or presents the 2022-24 NBL row as current (the retained-prior line, the window table and the dated register entry are the only places, each labelled). The v10 table cell that said `DATA_PENDING` now carries a pointer to the dated update |

## 3. Data checks

| Check | Result |
|---|---|
| Method validity | The `awk` method reproduces the published NBL, KBO and NPB rows exactly, including kurtosis, overtime, tie, home-win and one-run shares |
| 2025-26 reconciliation | 165 games, 33 per club, no duplicate ID or key; 165 of 165 scores and 165 of 165 native UUIDs match the processed NBL file |
| New 2026 CSV, full set | 29 of 29 rows checked (the whole file, not a sample): header identical to the 2025 header; 39 fields; total, margin, winner, loser, result text, game score, quarter sums, overtime flag, team A/B, row sequence, duplicates, day of week: 0 failures; round trip to the parsed source identical |
| Independent checks of results | 10 of 29 games confirmed against other publishers (7 earlier settlements, 3 match reports), spanning early, middle and late season, the overtime game, the lowest total (147) and the highest (234); 0 disagreements. 19 of 29 single-source. No tie, zero score or doubleheader exists in this file |
| Recomputed at random after the final edit | Five claims drawn by `shuf` from eight and recomputed from the repository files: 2023-25 NBL n 450 and mean total 183.14; 33 games per club in 2025; NPB regular-season finals 2,576 and 72 ties; 165 of 165 native-ID matches in the sidecar; cohort NBL games 207.75 against 184.12 for the other 25. All five agree |
| Reachability pass | 12 sources fetched once; 4 expected content, 7 home page or shell, 1 host-root 404; 2 manual-only not fetched; every status cell records what was seen and the date |

## 4. Manual scenario walkthroughs (reasoned, not executed by any importer or validator)

| Case | Documentary result |
|---|---|
| NBL card issued after this version | Cites `LP-2026.10.11-v2` (183.14, margin SD 16.34, total SD 19.26); may print the retained 181.13 beside it; the FC10-PROFILE-v1 trigger fires on the first such card |
| NBL card still in progress that cited the 2022-24 row | Keeps its row; its baseline is not recomputed (LEAGUE_PROFILES rule 3) |
| NBL card wants current-season form | Reads the 2026 CSV as `ARCHIVE_PARTIAL` with last date 2026-10-11 and adds later games from SOURCES; cannot get 2025-26 dates from the 2025 file, must use the processed file or the sidecar |
| Someone rebuilds an NBL 2025-26 profile on `Game Type` alone | ARCHIVE_USE_GUIDE §8 warns: 14 post-season rows are typed regular season; filter on `Round 1` to `Round 22` |
| KBO or NPB card wants an extras or tie-after-extras share | Must give its own estimate with basis or `NOT_ESTIMABLE`; the profile no longer offers 0.1% or 0.0%; an extras-dependent baseline is `BASELINE_UNAVAILABLE` |
| KBO card cites the profile's tie share | Allowed: measured from equal final scores (2.1% KBO, 2.8% NPB) |

## 5. Limits

- Arithmetic was done by scratch code on copies of the files; every printed figure is reproducible with the commands in the audit documents.
- The checks show internal consistency, agreement with other publishers on 10 games and agreement with a second NBL file; they do not prove the ESPN rows are complete or independently collected.
- Nothing here tests any prediction. The refreshed row is a data update; FC10-PROFILE-v1 has 0 events.

## 6. Publication

The release is one commit on local `main` above the unpushed v10 commit. The delivery message states whether it was pushed and the remote SHA after a fetch; this file cannot contain its own commit hash.
