# EuroCup (ULEB Cup 2002-08, Eurocup 2008-) 2002-03 to 2026-27: provenance, schema and known defects

**Status (2026-10-14):** the yearly files `<YEAR>/<YEAR>_games.csv` for 2002 to 2026 were rebuilt from observed source fields only, under [framework change 2026-10-14-1](../../../research/verification/framework_change_2026-10-14-1/IMPLEMENTATION.md) (audit items R01–R07, R26, R27). Before this, main held header-only placeholders. Commit `e73c9c24e` (2026-10-14) briefly published a build whose 1975–2001 rows were parsed from Wikipedia with **invented dates** (15 and 22 October, 15 and 22 January, 15 March of each season) and invented stage labels, whose start time was the value `1` on 81% of rows, and whose missing venues read "European Indoor Arena". It also carried a duplicate root export folder. That build is **quarantined outside the repository**; no row below comes from it.

**1975–2001 (Cup Winners' Cup, Korać-era tier-two cups, Saporta Cup) is not rebuilt.** Those competitions are not the same competition as the ULEB Cup/EuroCup, and the only rows that existed had invented dates. Those years keep their header-only placeholder.

These rows are research reference data, not evidence of forecasting skill, and a retrospective compilation.

## 1. Source

| Item | Value |
|---|---|
| Publisher | Euroleague Basketball official API, `https://api-live.euroleague.net/` (field owner; competition code `U`) |
| Route | `v2/competitions/U/seasons/U<YYYY>/games` (one JSON per season) |
| Capture | Captured fresh on 2026-10-14 (about 13:30 AEDT); one gzip file per season with SHA-256 in [CAPTURE_MANIFEST.csv](../../../research/verification/framework_change_2026-10-14-1/CAPTURE_MANIFEST.csv) |
| Other publishers | **None were used to build a field.** English Wikipedia's 2024-25 EuroCup article was read as a spot check only (§4) |

**Scope.** Games with `played = true` and status `Confirmed` or `Walkover`. Excluded and counted in the change receipt: 199 unplayed confirmed fixtures, 6 cancelled games and 1 game still `Planned` at capture.

## 2. How each field was filled

| Field | Class | Rule |
|---|---|---|
| Game ID | DERIVED | `EUROCUP-` + the API `identifier` (for example `EUROCUP-U2016_186`). Stable |
| Native Game ID | OBSERVED | `identifier` |
| Season, Season Year, League / Competition Name | OBSERVED | `season.alias`, `season.year`, `season.name` (for example "EuroCup 2016-17") |
| Competition Phase (as printed) | OBSERVED | `phaseType.name` and `group.rawName` |
| Game Type | DERIVED | RS → Regular Season; TS and Last 16 groups → Top 16; Last 32 groups → Not applicable; eliminatory, eighth-, quarter- and semi-final rounds → Quarter-Finals / Playoffs; the Finals phase → Final Four (single-venue semi-finals), Third Place Game, or Championship Game from the group's raw name |
| Round / Stage | OBSERVED | `roundName` |
| Date, Start Time (Local) | OBSERVED | `localDate`. The time is kept only when `confirmedHour` is true. 173 games print 00:00, a placeholder rather than a tip-off: blanked (flag `START_TIME_00_00_SUSPECTED_DEFAULT_BLANKED`) |
| Start Time (UTC) | OBSERVED | `utcDate`, kept under the same conditions |
| Home, Away, Team A, Team B | OBSERVED | `local.club.name`, `road.club.name` as printed that season |
| Scores and derived result fields | OBSERVED / DERIVED | `score`; home-away. 8 ties are printed: in two-legged rounds a single leg can end level (`TIE_AS_PRINTED`) |
| Home/Away Q1–Q4, OT, Overtime Periods | OBSERVED / DERIVED | `partials1`–`partials4`; OT is the sum of `extraPeriods` and Overtime Periods its count. All-zero partials are treated as missing (1 row, `QUARTERS_NOT_IN_SOURCE`). Nothing is balanced |
| Venue | OBSERVED | `venue.name` |
| Attendance | OBSERVED | `audience`. Kept with flag `ATTENDANCE_NOT_CONFIRMED_BY_SOURCE` where `audienceConfirmed` is false (1,408 rows, mostly 2009-10 to 2015-16). A zero is kept only inside 1 Feb 2020 to 30 Jun 2022 (closed-door COVID games); 85 zeros outside it are blanked as suspected defaults. Round figures such as 2,000 (175 rows, spread over many seasons) look like publisher estimates and are kept |
| Referees | OBSERVED | `referee1`–`referee4` names |
| City, Notable Players | NOT_IN_SOURCE | The API gives only a free-text venue address, which is not parsed |

## 3. Schema migration

Same 46-column header as the other basketball folders rebuilt on 2026-10-14 (full list in the KBL folder's DATA_PROVENANCE §3), with this folder's own `Game Type (Regular Season, Top 16, Quarter-Finals / Playoffs, Final Four, Third Place Game, Championship Game, Not applicable)` header kept. Years before 2002 keep their placeholder.

**Canonical path (R06):** `Previous Sports Results/Basketball/EuroCup/<YEAR>/<YEAR>_games.csv` is the only copy. Do not recreate the quarantined root folder `EuroCup_Basketball_CSVs/`.

## 4. Checks run and known defects

**Checks run (2026-10-14):** 4,851 games; 0 duplicate Game IDs; 0 weekday disagreements; every team in a season has the same number of `Regular Season` games (6, 8, 10 or 18 by format), except 2021-22 (12–18, consistent with the suspension of Russian clubs in February 2022) and 2024-25 (17–18). Neither shortfall was checked game by game. 2026-27 holds the 37 games completed by the capture.

**Independent check, a sample only:** the 2024-25 final (Hapoel Shlomo Tel Aviv 74-65 Dreamland Gran Canaria on 8 April 2025, Gran Canaria 94-103 Tel Aviv on 11 April) agrees with English Wikipedia's 2024-25 EuroCup article on dates and scores.

Flags carried in `QA Flags` (a row can carry several):

| Flag | Rows |
|---|---:|
| `ATTENDANCE_NOT_CONFIRMED_BY_SOURCE` | 1,408 |
| `START_TIME_00_00_SUSPECTED_DEFAULT_BLANKED` | 173 |
| `ATTENDANCE_ZERO_CONFIRMED_COVID_PERIOD` | 154 |
| `ATTENDANCE_ZERO_OUTSIDE_COVID_PERIOD_SUSPECTED_DEFAULT_BLANKED` | 85 |
| `TIE_AS_PRINTED` | 8 |
| `WALKOVER_AWARDED` | 1 |
| `QUARTERS_NOT_IN_SOURCE` | 1 |
| `START_TIME_NOT_CONFIRMED_BY_SOURCE` | 1 |

## 5. Use rules

- Point-in-time and form windows as in ARCHIVE_USE_GUIDE §3 and §9; the archive was captured 2026-10-14.
- Exclude the walkover from scoring statistics.
- Treat `ATTENDANCE_NOT_CONFIRMED_BY_SOURCE` values as estimates.
- Settle a live card from the Euroleague Basketball field owner ([SOURCES.md](../../../SOURCES.md) §3.33).

## 6. Per-season counts

| Season | Rows | Regular season | Play-off / final types | Other (`Not applicable`) | Quarters filled | Start time filled | Attendance filled | Referees filled | Venue filled | Rows with any QA flag |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2002-03 | 150 | 120 | 30 | 0 | 150 | 0 | 150 | 150 | 150 | 150 |
| 2003-04 | 209 | 180 | 29 | 0 | 209 | 191 | 209 | 209 | 209 | 18 |
| 2004-05 | 239 | 210 | 29 | 0 | 239 | 239 | 239 | 239 | 239 | 1 |
| 2005-06 | 149 | 120 | 29 | 0 | 149 | 149 | 147 | 149 | 149 | 2 |
| 2006-07 | 149 | 120 | 29 | 0 | 149 | 144 | 147 | 149 | 149 | 7 |
| 2007-08 | 326 | 270 | 56 | 0 | 326 | 326 | 276 | 326 | 326 | 53 |
| 2008-09 | 151 | 96 | 55 | 0 | 150 | 151 | 143 | 151 | 151 | 8 |
| 2009-10 | 156 | 96 | 60 | 0 | 156 | 156 | 151 | 156 | 156 | 17 |
| 2010-11 | 156 | 96 | 60 | 0 | 156 | 156 | 154 | 156 | 156 | 154 |
| 2011-12 | 156 | 96 | 60 | 0 | 156 | 156 | 154 | 156 | 156 | 101 |
| 2012-13 | 157 | 96 | 61 | 0 | 157 | 157 | 156 | 157 | 157 | 156 |
| 2013-14 | 366 | 240 | 30 | 96 | 366 | 366 | 364 | 366 | 366 | 363 |
| 2014-15 | 306 | 180 | 30 | 96 | 306 | 306 | 304 | 306 | 306 | 304 |
| 2015-16 | 306 | 180 | 30 | 96 | 306 | 306 | 299 | 306 | 306 | 299 |
| 2016-17 | 146 | 80 | 66 | 0 | 146 | 146 | 146 | 146 | 146 | 3 |
| 2017-18 | 184 | 120 | 64 | 0 | 184 | 184 | 182 | 184 | 184 | 3 |
| 2018-19 | 186 | 120 | 66 | 0 | 186 | 186 | 186 | 186 | 186 | 1 |
| 2019-20 | 168 | 120 | 48 | 0 | 168 | 168 | 168 | 168 | 168 | 3 |
| 2020-21 | 185 | 120 | 65 | 0 | 185 | 185 | 181 | 185 | 185 | 136 |
| 2021-22 | 189 | 174 | 15 | 0 | 189 | 189 | 187 | 189 | 189 | 26 |
| 2022-23 | 195 | 180 | 15 | 0 | 195 | 194 | 195 | 195 | 195 | 1 |
| 2023-24 | 195 | 180 | 15 | 0 | 195 | 195 | 187 | 195 | 195 | 8 |
| 2024-25 | 195 | 179 | 16 | 0 | 195 | 195 | 191 | 195 | 195 | 4 |
| 2025-26 | 195 | 180 | 15 | 0 | 195 | 195 | 192 | 195 | 195 | 3 |
| 2026-27 | 37 | 37 | 0 | 0 | 37 | 37 | 34 | 37 | 37 | 4 |
| **Total** | **4,851** | **3,590** | **973** | **288** | **4,850** | **4,677** | **4,742** | **4,851** | **4,851** | **1,825** |
