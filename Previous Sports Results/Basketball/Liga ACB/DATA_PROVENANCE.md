# Spanish top-flight basketball (Liga Nacional 1975-83, Liga ACB 1983-) 1975-76 to 2026-27: provenance, schema and known defects

**Status (2026-10-14):** the yearly files `<YEAR>/<YEAR>_games.csv` for 1975 to 2026 were rebuilt from observed source fields only, under [framework change 2026-10-14-1](../../../research/verification/framework_change_2026-10-14-1/IMPLEMENTATION.md) (audit items R01–R07, R26, R27). Before this, main held header-only placeholders. Commit `e73c9c24e` (2026-10-14) briefly published a build that labelled UTC kick-off times as local time, put each home club's usual arena (from a hand-typed table, defaulting to "Pabellón Polideportivo") in Venue, wrote "No" overtime for every game, guessed play-off and relegation labels, mixed Copa del Rey and Supercopa games into the league and carried a duplicate root export folder. That build is **quarantined outside the repository**; no row below comes from it.

These rows are research reference data, not evidence of forecasting skill, and a retrospective compilation.

## 1. Source

| Item | Value |
|---|---|
| Publisher | ACB (Asociación de Clubes de Baloncesto), `https://acb.com/` (field owner; the site also carries the pre-ACB Liga Nacional seasons) |
| Route | `es/liga/calendario?temporada=<edition>` with edition = season start year − 1935 (checked: every file's dates fall in its own season). The page embeds the season's rounds, matches and teams in its Next.js data |
| Capture | Captured fresh on 2026-10-14 (about 13:30–14:40 AEDT); one gzip file per page with SHA-256 in [CAPTURE_MANIFEST.csv](../../../research/verification/framework_change_2026-10-14-1/CAPTURE_MANIFEST.csv). The Copa del Rey and Supercopa pages were captured too but **not used** (separate competitions) |
| Other publishers | **None were used to build a field.** English Wikipedia's 2025 ACB Playoffs article was read as a spot check only (§4) |

**Scope.** League games with status `FINALIZED` and both scores. Excluded and counted in the change receipt: 271 `NOT_STARTED` and 9 `UNSCHEDULED` listings (2026-27 fixtures), all Copa del Rey and Supercopa games.

## 2. How each field was filled

| Field | Class | Rule |
|---|---|---|
| Game ID | DERIVED | `ACB-LIGA-` + the native match id. Stable |
| Native Game ID | OBSERVED | Match `id` |
| Season, Season Year | DERIVED | From the edition (season start year) |
| League / Competition Name | DERIVED | "Liga Nacional" to 1982-83, "Liga ACB" from 1983-84 (the ACB's founding) |
| Competition Phase, Game Type | DERIVED, checked | A round with no subphase → Regular Season, **unless** its round number is after the season's last full round (the last round with as many games as round 1): those 429 games are post-season games stored without a subphase and are `Not applicable`, flagged `ROUND_AFTER_LAST_FULL_ROUND_NO_SUBPHASE`. The source gives play-off subphases only as numbers. A subphase is named only when a structural check holds in that season: 291 has exactly 2 teams (final series → Championship Game), 292 has 4 (semi-finals), 293 has 8 (quarter-finals), 294 has 16 (round of 16) → Quarter-Finals / Playoffs. Otherwise the row is `Not applicable`, flagged `SUBPHASE_NOT_NAMED_IN_SOURCE`, and the phase text keeps the raw subphase number (for example 271/272 group phases in the 1970s–80s, 280 in 1990-91, 221 in the 2019-20 Valencia bubble) |
| Round / Stage | OBSERVED | `Round <roundNumber>` |
| Start Time (UTC) | OBSERVED | From `startDateTime`, which is UTC (`…Z`) |
| Date, Start Time (Local) | DERIVED | UTC converted to Europe/Madrid, or Atlantic/Canary when the home team's printed name contains Canarias/Gran Canaria/Tenerife/Lanzarote/Fuerteventura (flag `LOCAL_TIME_ATLANTIC_CANARY`) |
| Placeholder seasons | Blanked | In 1975-76 to 1989-90 at least half of each season's games carry the same UTC time (12:00Z), a placeholder rather than a tip-off. Their times are blank (flag `SEASON_TIMES_PLACEHOLDER_12:00Z_BLANKED`) and the date is the UTC calendar date. This is the R26 diagnostic applied per season; the raw value stays in the capture |
| Home, Away, Team A, Team B | OBSERVED | `fullName` as printed for that edition (sponsor names change by season). Club lineage is not resolved |
| Scores and derived result fields | OBSERVED / DERIVED | As printed; home-away. Ties are kept as printed (`TIE_AS_PRINTED`): 33 rows, all in 1975-76 to 1982-83 |
| Overtime, quarter scores, Venue, City, Attendance, Referees, Notable Players | NOT_IN_SOURCE | The calendar data has no such fields (its `currentQuarter` is 1 for finished games and is not used) |

## 3. Schema migration

Same 46-column header as the other basketball folders rebuilt on 2026-10-14 (full list in the KBL folder's DATA_PROVENANCE §3), with this folder's own `Game Type (Regular Season, Top 16, Quarter-Finals / Playoffs, Final Four, Third Place Game, Championship Game, Not applicable)` header kept. All 13 placeholder names keep their meaning. Years before 1975 keep their placeholder.

**Canonical path (R06):** `Previous Sports Results/Basketball/Liga ACB/<YEAR>/<YEAR>_games.csv` is the only copy. Do not recreate the quarantined root folder `Liga_ACB_Basketball_CSVs/`.

## 4. Checks run and known defects

**Checks run (2026-10-14):** 15,881 games; 0 duplicate Game IDs; 0 weekday disagreements; every season's dates lie in that season. Every team has the same number of `Regular Season` games within each completed season (for example 22 in 1976-77 to 1979-80, 38 in 1994-95 and 1995-96, 34 from 1996-97, 32 in the 17-team 2008-09 and 2016-17 and 36 in the 19-team 2020-21), except 2019-20 (22–23, stopped by COVID-19). In the group-phase seasons of the 1980s and early 1990s the `Regular Season` rows are the first phase only; the later phases are `Not applicable` with their raw subphase number. 2026-27 holds the 26 games completed by the capture.

**Independent check, a sample only:** the 2024-25 final (Real Madrid 89-75 and 102-96 at home on 20 and 22 June 2025, then 81-70 at Valencia on 25 June) agrees with English Wikipedia's `2025 ACB Playoffs` article. That article marks game 2 as an overtime game, which this folder cannot show (no overtime field in the source).

**Not checked:** whether the 1975-83 ties were genuine results; the subphase numbers left unnamed.

Flags carried in `QA Flags` (a row can carry several):

| Flag | Rows |
|---|---:|
| `SEASON_TIMES_PLACEHOLDER_12:00Z_BLANKED` | 3,547 |
| `SUBPHASE_NOT_NAMED_IN_SOURCE` | 925 |
| `LOCAL_TIME_ATLANTIC_CANARY` | 874 |
| `ROUND_AFTER_LAST_FULL_ROUND_NO_SUBPHASE` | 429 |
| `TIE_AS_PRINTED` | 33 |

## 5. Use rules

- Point-in-time and form windows as in ARCHIVE_USE_GUIDE §3 and §9; the archive was captured 2026-10-14.
- Do not use start times from 1975-76 to 1989-90 (blank by design). Rest-day features may use dates.
- No quarter, overtime, venue or attendance features can be built from this folder.
- Settle a live card from the ACB field owner ([SOURCES.md](../../../SOURCES.md) §3.33).

## 6. Per-season counts

| Season | Rows | Regular season | Play-off / final types | Other (`Not applicable`) | Quarters filled | Start time filled | Attendance filled | Referees filled | Venue filled | Rows with any QA flag |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1975-76 | 192 | 120 | 0 | 72 | 0 | 0 | 0 | 0 | 0 | 192 |
| 1976-77 | 132 | 132 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 132 |
| 1977-78 | 132 | 132 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 132 |
| 1978-79 | 132 | 132 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 132 |
| 1979-80 | 132 | 132 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 132 |
| 1980-81 | 182 | 182 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 182 |
| 1981-82 | 182 | 182 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 182 |
| 1982-83 | 183 | 182 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 183 |
| 1983-84 | 260 | 144 | 7 | 109 | 0 | 0 | 0 | 0 | 0 | 260 |
| 1984-85 | 258 | 224 | 6 | 28 | 0 | 0 | 0 | 0 | 0 | 258 |
| 1985-86 | 257 | 192 | 2 | 63 | 0 | 0 | 0 | 0 | 0 | 257 |
| 1986-87 | 262 | 128 | 4 | 130 | 0 | 0 | 0 | 0 | 0 | 262 |
| 1987-88 | 264 | 192 | 13 | 59 | 0 | 0 | 0 | 0 | 0 | 264 |
| 1988-89 | 492 | 240 | 0 | 252 | 0 | 0 | 0 | 0 | 0 | 492 |
| 1989-90 | 487 | 456 | 0 | 31 | 0 | 0 | 0 | 0 | 0 | 487 |
| 1990-91 | 494 | 312 | 2 | 180 | 0 | 494 | 0 | 0 | 0 | 193 |
| 1991-92 | 498 | 408 | 0 | 90 | 0 | 498 | 0 | 0 | 0 | 107 |
| 1992-93 | 394 | 275 | 15 | 104 | 0 | 394 | 0 | 0 | 0 | 104 |
| 1993-94 | 336 | 280 | 18 | 38 | 0 | 336 | 0 | 0 | 0 | 38 |
| 1994-95 | 412 | 380 | 11 | 21 | 0 | 412 | 0 | 0 | 0 | 21 |
| 1995-96 | 411 | 380 | 3 | 28 | 0 | 411 | 0 | 0 | 0 | 47 |
| 1996-97 | 341 | 306 | 12 | 23 | 0 | 341 | 0 | 0 | 0 | 40 |
| 1997-98 | 341 | 306 | 12 | 23 | 0 | 341 | 0 | 0 | 0 | 40 |
| 1998-99 | 331 | 306 | 10 | 15 | 0 | 331 | 0 | 0 | 0 | 32 |
| 1999-00 | 335 | 306 | 29 | 0 | 0 | 335 | 0 | 0 | 0 | 18 |
| 2000-01 | 331 | 306 | 11 | 14 | 0 | 331 | 0 | 0 | 0 | 31 |
| 2001-02 | 332 | 306 | 10 | 16 | 0 | 332 | 0 | 0 | 0 | 33 |
| 2002-03 | 332 | 306 | 12 | 14 | 0 | 332 | 0 | 0 | 0 | 31 |
| 2003-04 | 335 | 306 | 29 | 0 | 0 | 335 | 0 | 0 | 0 | 36 |
| 2004-05 | 336 | 306 | 29 | 1 | 0 | 336 | 0 | 0 | 0 | 37 |
| 2005-06 | 331 | 306 | 23 | 2 | 0 | 331 | 0 | 0 | 0 | 20 |
| 2006-07 | 336 | 306 | 30 | 0 | 0 | 336 | 0 | 0 | 0 | 19 |
| 2007-08 | 323 | 306 | 15 | 2 | 0 | 323 | 0 | 0 | 0 | 19 |
| 2008-09 | 292 | 272 | 20 | 0 | 0 | 292 | 0 | 0 | 0 | 17 |
| 2009-10 | 326 | 306 | 20 | 0 | 0 | 326 | 0 | 0 | 0 | 18 |
| 2010-11 | 324 | 306 | 18 | 0 | 0 | 324 | 0 | 0 | 0 | 18 |
| 2011-12 | 329 | 306 | 14 | 9 | 0 | 329 | 0 | 0 | 0 | 26 |
| 2012-13 | 328 | 306 | 22 | 0 | 0 | 328 | 0 | 0 | 0 | 36 |
| 2013-14 | 329 | 306 | 23 | 0 | 0 | 329 | 0 | 0 | 0 | 35 |
| 2014-15 | 328 | 306 | 22 | 0 | 0 | 328 | 0 | 0 | 0 | 35 |
| 2015-16 | 328 | 306 | 22 | 0 | 0 | 328 | 0 | 0 | 0 | 35 |
| 2016-17 | 295 | 272 | 23 | 0 | 0 | 295 | 0 | 0 | 0 | 34 |
| 2017-18 | 327 | 306 | 21 | 0 | 0 | 327 | 0 | 0 | 0 | 37 |
| 2018-19 | 325 | 306 | 19 | 0 | 0 | 325 | 0 | 0 | 0 | 34 |
| 2019-20 | 238 | 205 | 3 | 30 | 0 | 238 | 0 | 0 | 0 | 53 |
| 2020-21 | 360 | 342 | 18 | 0 | 0 | 360 | 0 | 0 | 0 | 39 |
| 2021-22 | 327 | 306 | 21 | 0 | 0 | 327 | 0 | 0 | 0 | 36 |
| 2022-23 | 325 | 306 | 19 | 0 | 0 | 325 | 0 | 0 | 0 | 36 |
| 2023-24 | 326 | 306 | 20 | 0 | 0 | 326 | 0 | 0 | 0 | 36 |
| 2024-25 | 325 | 306 | 19 | 0 | 0 | 325 | 0 | 0 | 0 | 37 |
| 2025-26 | 327 | 306 | 21 | 0 | 0 | 327 | 0 | 0 | 0 | 36 |
| 2026-27 | 26 | 26 | 0 | 0 | 0 | 26 | 0 | 0 | 0 | 1 |
| **Total** | **15,881** | **13,878** | **649** | **1,354** | **0** | **12,334** | **0** | **0** | **0** | **5,012** |
