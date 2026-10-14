# Data rebuild receipt: framework change 2026-10-14-1

[Implementation](IMPLEMENTATION.md) · [Verification](VERIFICATION_REPORT.md) · [Capture manifest](CAPTURE_MANIFEST.csv)

## 1. Quarantine

**Destination:** `C:\Users\danie\Desktop\Sports Research LOCAL_QUARANTINE_2026-10-14\`, a sibling of the repository folder. Contents:

| Path there | What it is |
|---|---|
| `git_status_before.txt`, `head_before.txt` | Working-tree status and HEAD/origin before any change (`e73c9c24e`) |
| `commit_e73c9c24e.patch`, `commit_e73c9c24e_files.txt` | The full binary patch of the commit (53.4 MB) and its 447 paths |
| `working_tree_copy/` | Byte copies of the five basketball folders, `Basketball/G League/` and SOURCES.md as published in `e73c9c24e` |
| `moved_local_only/` | `research/src/` (63 .py and `__pycache__`), `research/data/{acb,bleague,eurocup,kbl}/` (4 .db, 32 .json), `research/sample_game_501311.html`, the five research reports, and the root duplicate `AUDIT_RECOMMENDATIONS_2026-10-12.txt` (identical to the copy in the 2026-10-12 change folder) |
| `captures/` | The raw responses captured for this rebuild (gzip), one `MANIFEST.tsv` per source |

All 2,089 copied files were compared with `cmp` against the repository before anything was removed: 0 mismatches. The quarantine folder is the only copy of the KBL source captures and the `e73c9c24e` working state outside Git history. **Do not delete it** until the owner decides.

## 2. Captures

| League | Source | Requests | Captured | Used |
|---|---|---:|---|---|
| KBL | api.kbl.or.kr match lists and per-game records | 33 files | 2026-10-13 15:15–15:23 AEDT (earlier session) | all |
| B League | bleague.jp schedule JSON, tab 1, events 2/3/4/11 | 402 pages | 2026-10-14 | all |
| Liga ACB | acb.com calendario pages, `liga`, editions 40–91 | 52 pages | 2026-10-14 | all |
| (ACB cups) | `copa-del-rey`, `supercopa` pages | 104 pages | 2026-10-14 | **not used** |
| EuroCup | api-live.euroleague.net v2 games, U2002–U2026 | 25 | 2026-10-14 | all |
| NBA G League | stats.gleague.nba.com leaguegamelog, 2001-02 to 2026-27 × 3 season types | 78 | 2026-10-14 | all (2001-04 and 2026-27 empty) |
| NBA G League | ESPN nba-development scoreboard, monthly 2001-01 to 2026-10 | 310 | 2026-10-14 | joined rows only |

Every request returned HTTP 200. SHA-256 of every raw body (KBL: of every file) is in [CAPTURE_MANIFEST.csv](CAPTURE_MANIFEST.csv).

## 3. Rows kept and excluded

| League | Rows written | Excluded (counted) |
|---|---:|---|
| KBL | 8,285 (1996–2026 files) | D-League and summer/winter leagues 895; KBL Cup 70; older cup 34; All-Star 30; EASL 25; Open Match Day 20; no final score 252 |
| B League | 6,350 (2016–2026) | All-Star/exhibition squads 19; non-member exhibition 1; duplicate listings 145; unplayed or preview cards 964 |
| Liga ACB | 15,881 (1975–2026) | Not started 271; unscheduled 9; all Copa del Rey and Supercopa games |
| EuroCup | 4,851 (2002–2026) | Unplayed 199; cancelled 6; still planned 1 |
| NBA G League | 10,947 (2004–2025) | none (every owner game had two team rows) |
| **Total** | **46,314** | |

## 4. Values blanked as placeholders (R26)

| League | Pattern | Rows | Evidence |
|---|---|---:|---|
| Liga ACB | 12:00Z on at least half of a season's games, 1975-76 to 1989-90 | 3,547 | Per-season time distribution; later seasons vary |
| EuroCup | Start time 00:00 local | 173 | No basketball tip-offs at midnight; values kept in the capture |
| EuroCup, KBL, NBA G League | Attendance 0 outside 1 Feb 2020 to 30 Jun 2022 | 85, 1, 310 | Zeros inside the COVID closed-door window are kept (154, 117, 277) |

## 5. Previous state

On `65f780cef` the five folders were 13-column header-only placeholders (for example `Basketball/KBL/2020/2020_games.csv`, 1 line). No consumer depended on their rows.
