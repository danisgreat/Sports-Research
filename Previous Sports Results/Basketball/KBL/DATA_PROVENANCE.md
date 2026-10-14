# KBL (Korean Basketball League) 1997 to 2026-27: provenance, schema and known defects

**Status (2026-10-14):** the yearly files `<YEAR>/<YEAR>_games.csv` for 1996 to 2026 were rebuilt from observed source fields only, under [framework change 2026-10-14-1](../../../research/verification/framework_change_2026-10-14-1/IMPLEMENTATION.md) (audit items R01, R04, R05, R06, R07, R26, R27). Before this, main held header-only placeholders for these years. Commit `e73c9c24e` (2026-10-14) briefly published a build that guessed start times from the weekday (14:00 at weekends, 19:00 otherwise), mixed D-League and summer/winter-league games into the top flight and carried a duplicate root export folder. That build is **quarantined outside the repository** and no row below comes from it.

These rows are research reference data. They are not evidence of forecasting skill, and they are a retrospective compilation: a row's date says when the game was played, not when the result became available.

## 1. Source

| Item | Value |
|---|---|
| Publisher | Korean Basketball League, official data API `https://api.kbl.or.kr/` (field owner) |
| Routes | `match/list?fromDate=…&toDate=…&tcodeList=all` (one list per season window), `match/{gmkey}` (one game record per game: attendance, referees, quarter scores), `season/list` |
| Capture | 2026-10-13 about 15:15 AEDT (match lists) and 15:23 AEDT (game records), by an earlier local session. Not re-fetched for this rebuild. The match lists were re-serialised by the capturing script, so they are API content but not byte-identical HTTP bodies. File SHA-256 values are in the change folder's [CAPTURE_MANIFEST.csv](../../../research/verification/framework_change_2026-10-14-1/CAPTURE_MANIFEST.csv) |
| Language | Korean names as printed; the venue's English name is appended where the API gives one |
| Other publishers | **None were used to build a field.** Korean Wikipedia's championship table was read as a spot check only (§4) |

**Scope.** First-team KBL games only (`seasonGrade = 1`) of the categories regular season (`R`), playoffs (`PO`) and championship final (`CP`). Excluded and counted in the change receipt: D-League and the KBL summer/winter leagues (`seasonGrade = 2`, 895 games), KBL Cup (`CU`, 70), the older cup (`EG`, 34), All-Star (`AS`, 30), EASL (`EA`, 25), Open Match Day (`OM`, 20) and 252 listed games without a final score (not yet played at capture).

## 2. How each field was filled

Classes: **OBSERVED**, copied as given; **DERIVED**, computed only from observed fields; **NOT_IN_SOURCE**, always blank.

| Field | Class | Rule |
|---|---|---|
| Game ID | DERIVED | `KBL-` + the native `gmkey` (for example `KBL-S47G01N176`). Stable: no row number |
| Native Game ID | OBSERVED | `gmkey` |
| Season, Season Year | OBSERVED / DERIVED | `seasonName1` as printed. Season Year is its first year, except the inaugural season "1997" (February to April 1997), which is filed under **1996** as the 1996-97 winter (flag `INAUGURAL_1997_SEASON_FILED_UNDER_1996`), so it does not share a file with 1997-98 |
| Competition Phase (as printed) | OBSERVED | `seasonCategoryName` (정규시즌 regular season, 플레이오프 playoffs, 챔피언결정전 championship final) |
| Game Type | DERIVED | R → Regular Season, PO → Playoffs, CP → Finals |
| Round / Stage | DERIVED | Category name plus the API's game number |
| Date | OBSERVED | `gameDate` |
| Day of Week | DERIVED | Computed from Date and compared with the printed `weekDay` (0 conflicts) |
| Start Time (Local) | OBSERVED | `gameStart` (KST) as printed, including odd minutes such as 19:01. Never inferred |
| Start Time (UTC) | NOT_IN_SOURCE | Blank |
| Home, Away, Team A, Team B | OBSERVED | Full team names as printed for that season (`tnameFH`/`tnameFA`). Club lineage is not resolved: renamed clubs appear under each name |
| Home Score, Away Score | OBSERVED | `scoreH`, `scoreA` |
| Game Score, Total Points, Winning Margin, Winning/Losing Team, Result | DERIVED | From the scores. Game Score is home-away |
| Home/Away Q1–Q4, OT, Overtime Periods | OBSERVED / DERIVED | Quarters from the game record's `scoreq1`–`scoreq4`; OT is the sum of the `scoreeq` list and Overtime Periods its length. **Nothing is balanced**: a sum that differs from the final is flagged `PERIOD_SUM_MISMATCH` |
| Venue | OBSERVED | `stadiumnameF`, with `stadiumnameEn` in brackets when it is Latin script and different |
| Attendance | OBSERVED | `crowds`. A zero inside 1 Feb 2020 to 30 Jun 2022 (closed-door COVID games) is kept and flagged. One zero outside that window is blanked as a suspected default (R26) |
| Referees | OBSERVED | Main referee then the two subs, as printed |
| City, Notable Players | NOT_IN_SOURCE | Blank |
| A Succint one line game comment… | DERIVED | Generated from the result only |
| QA Flags, Unavailable Fields | DERIVED | See §4 |
| Primary Data Source, Source Retrieved | OBSERVED | Routes and capture times |
| Game Number | DERIVED | Order within the file (date, time, gmkey). It is **not** an identity |

## 3. Schema migration

The previous file was the 13-column header-only placeholder (`Game Number, Game Type (…), Team A, Team B, Home, Away, Venue, Date, Game Score, Total Points, Winning Margin, Notable Players, A Succint one line game comment…`). All 13 names are kept with the same meaning; 33 columns are added (46 in total). The placeholder had no rows, so no consumer depended on positions. Read columns by name. Years before 1996 keep their header-only placeholder: the KBL did not exist.

Full header, in order: Game Number, Game ID, Native Game ID, Season, Season Year, League / Competition Name, Competition Phase (as printed), Game Type (Pre-Season, Regular Season, Play-In, Playoffs, Conference Finals, Finals, Not applicable), Round / Stage, Date, Day of Week, Start Time (Local), Start Time (UTC), Team A, Team B, Home, Away, Home Score, Away Score, Game Score, Total Points, Winning Margin, Winning Team, Losing Team, Result, Overtime Periods, Home Q1, Away Q1, Home Q2, Away Q2, Home Q3, Away Q3, Home Q4, Away Q4, Home OT, Away OT, Venue, City, Attendance, Referees, Notable Players, A Succint one line game comment to summarise that game, QA Flags, Unavailable Fields, Primary Data Source, Source Retrieved.

**Canonical path (R06):** `Previous Sports Results/Basketball/KBL/<YEAR>/<YEAR>_games.csv` is the only copy. The root export folder `KBL_Basketball_CSVs/` of the quarantined build is not in the repository. Do not recreate it.

## 4. Checks run and known defects

**Checks run (2026-10-14), CSV-aware:** 8,285 games; 0 duplicate Game IDs; 0 weekday disagreements; every regular season complete (8 teams × 21 games in 1997; 10 × 45 from 1997-98 to 2000-01; 10 × 54 from 2001-02; 2019-20 stopped at 42–43 games per team by COVID-19); 2026-27 holds the 18 games completed by the capture.

**Independent check, a sample only:** the 2024-25 final (7 games, LG won 4–3 in the order W-W-W-L-L-L-W) and the 2025-26 final (5 games, KCC won 4–1, W-W-W-L-W) agree with the result sequence in Korean Wikipedia's `KBL 챔피언결정전` table (read 2026-10-14). English Wikipedia's 2024-25 season article says the play-offs ended on 15 May 2025; the owner's record and the Korean table both have a seventh game on 17 May 2025. Twelve games do not certify the archive.

Flags carried in `QA Flags` (a row can carry several):

| Flag | Rows |
|---|---:|
| `ATTENDANCE_ZERO_COVID_PERIOD` | 117 |
| `INAUGURAL_1997_SEASON_FILED_UNDER_1996` | 111 |
| `PERIOD_SUM_MISMATCH` | 1 |
| `ATTENDANCE_ZERO_OUTSIDE_COVID_PERIOD_SUSPECTED_DEFAULT_BLANKED` | 1 |

## 5. Use rules

- **Point-in-time:** a row may feed a card only if its date is before the card's cutoff, and the card must say the archive is a retrospective compilation captured 2026-10-13 (R28).
- **Form windows:** all rows are dated. Count regular season and playoffs together only when the card says so.
- **Quarter features:** drop the one `PERIOD_SUM_MISMATCH` row.
- This file is not an official record. Settle a live card from the KBL field owner ([SOURCES.md](../../../SOURCES.md) §3.33).

## 6. Per-season counts

| Season | Rows | Regular season | Play-off / final types | Other (`Not applicable`) | Quarters filled | Start time filled | Attendance filled | Referees filled | Venue filled | Rows with any QA flag |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1997 | 111 | 84 | 27 | 0 | 111 | 111 | 111 | 111 | 111 | 111 |
| 1997-1998 | 248 | 225 | 23 | 0 | 248 | 248 | 248 | 248 | 248 | 0 |
| 1998-1999 | 244 | 225 | 19 | 0 | 244 | 244 | 244 | 244 | 244 | 0 |
| 1999-2000 | 245 | 225 | 20 | 0 | 245 | 245 | 245 | 245 | 245 | 0 |
| 2000-2001 | 244 | 225 | 19 | 0 | 244 | 244 | 244 | 244 | 244 | 0 |
| 2001-2002 | 291 | 270 | 21 | 0 | 291 | 291 | 291 | 291 | 291 | 0 |
| 2002-2003 | 288 | 270 | 18 | 0 | 288 | 288 | 288 | 288 | 288 | 0 |
| 2003-2004 | 289 | 270 | 19 | 0 | 289 | 289 | 289 | 289 | 289 | 0 |
| 2004-2005 | 287 | 270 | 17 | 0 | 287 | 287 | 287 | 287 | 287 | 0 |
| 2005-2006 | 286 | 270 | 16 | 0 | 286 | 286 | 286 | 286 | 286 | 0 |
| 2006-2007 | 289 | 270 | 19 | 0 | 289 | 289 | 289 | 289 | 289 | 0 |
| 2007-2008 | 286 | 270 | 16 | 0 | 286 | 286 | 286 | 286 | 286 | 0 |
| 2008-2009 | 295 | 270 | 25 | 0 | 295 | 295 | 295 | 295 | 295 | 1 |
| 2009-2010 | 291 | 270 | 21 | 0 | 291 | 291 | 291 | 291 | 291 | 0 |
| 2010-2011 | 290 | 270 | 20 | 0 | 290 | 290 | 290 | 290 | 290 | 0 |
| 2011-2012 | 292 | 270 | 22 | 0 | 292 | 292 | 292 | 292 | 292 | 0 |
| 2012-2013 | 289 | 270 | 19 | 0 | 289 | 289 | 289 | 289 | 289 | 0 |
| 2013-2014 | 292 | 270 | 22 | 0 | 292 | 292 | 292 | 292 | 292 | 0 |
| 2014-2015 | 292 | 270 | 22 | 0 | 292 | 292 | 292 | 292 | 292 | 0 |
| 2015-2016 | 290 | 270 | 20 | 0 | 290 | 290 | 290 | 290 | 290 | 0 |
| 2016-2017 | 292 | 270 | 22 | 0 | 292 | 292 | 292 | 292 | 292 | 0 |
| 2017-2018 | 292 | 270 | 22 | 0 | 292 | 292 | 292 | 292 | 292 | 0 |
| 2018-2019 | 291 | 270 | 21 | 0 | 291 | 291 | 291 | 291 | 291 | 0 |
| 2019-2020 | 213 | 213 | 0 | 0 | 213 | 213 | 213 | 213 | 213 | 8 |
| 2020-2021 | 289 | 270 | 19 | 0 | 289 | 289 | 289 | 289 | 289 | 95 |
| 2021-2022 | 288 | 270 | 18 | 0 | 288 | 288 | 288 | 288 | 288 | 14 |
| 2022-2023 | 292 | 270 | 22 | 0 | 292 | 292 | 292 | 292 | 292 | 0 |
| 2023-2024 | 291 | 270 | 21 | 0 | 291 | 291 | 290 | 291 | 291 | 1 |
| 2024-2025 | 292 | 270 | 22 | 0 | 292 | 292 | 292 | 292 | 292 | 0 |
| 2025-2026 | 288 | 270 | 18 | 0 | 288 | 288 | 288 | 288 | 288 | 0 |
| 2026-2027 | 18 | 18 | 0 | 0 | 18 | 18 | 18 | 18 | 18 | 0 |
| **Total** | **8,285** | **7,695** | **590** | **0** | **8,285** | **8,285** | **8,284** | **8,285** | **8,285** | **230** |
