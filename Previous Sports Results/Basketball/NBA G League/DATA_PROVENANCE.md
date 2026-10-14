# NBA G League (NBA Development League to 2017) 2004-05 to 2025-26: provenance, schema and known defects

**Status (2026-10-14):** the yearly files `<YEAR>/<YEAR>_games.csv` for 2004 to 2025 were rebuilt from observed source fields only, under [framework change 2026-10-14-1](../../../research/verification/framework_change_2026-10-14-1/IMPLEMENTATION.md) (audit items R01–R07, R26, R27). Before this, main held header-only placeholders. Commit `e73c9c24e` (2026-10-14) briefly published a build with the R01/R02 fingerprint (start time 19:00 on 49.8% and attendance 2,500 on 52.6% of rows, including all 418 games of 2010), quarter scores on every row back to 2001, a duplicate folder `Basketball/G League/` and a root export folder. The framework change of 2026-10-12 had already found that build and left it unpublished. It is **quarantined outside the repository**; no row below comes from it.

**Not rebuilt:** 2001-02 to 2003-04 (NBDL) and 2026-27. The league's statistics API returns no games for the NBDL seasons, and no 2026-27 game had been played at capture. Those years keep their header-only placeholder. The folder `Basketball/G League/` is not used (R06).

These rows are research reference data, not evidence of forecasting skill, and a retrospective compilation.

## 1. Sources

| Item | Value |
|---|---|
| Owner record (every row) | NBA G League statistics API, `https://stats.gleague.nba.com/stats/leaguegamelog?LeagueID=20&Season=<YYYY-YY>&SeasonType=<type>&PlayerOrTeam=T`, season types `Regular Season`, `Playoffs` and `Showcase` (the Tip-Off Tournament / Showcase Cup games, which the regular-season log omits from 2021-22). Two team rows per game |
| Enrichment (where joinable) | ESPN site API, `https://site.api.espn.com/apis/site/v2/sports/basketball/nba-development/scoreboard?dates=<YYYYMM>&limit=1000` (evidence B; covers 2018 onward) |
| Capture | Both captured fresh on 2026-10-14 (about 13:30–15:20 AEDT); one gzip file per request with SHA-256 in [CAPTURE_MANIFEST.csv](../../../research/verification/framework_change_2026-10-14-1/CAPTURE_MANIFEST.csv) |
| Other publishers | **None were used to build a field.** English Wikipedia's 2024-25 season article was read as a spot check only (§4) |

**The ESPN join is strict.** An ESPN game is used only when (a) it is the only completed ESPN game within one day of the owner's date with the same home and away scores, and (b) both ESPN team ids map to the owner's team ids. The id map is built by majority vote over all unique score-and-date matches (an id must agree at least 90% of the time), because ESPN prints today's franchise names on old games (Maine Red Claws appear as "Maine Celtics", Fort Wayne Mad Ants as "Noblesville Boom"), so names cannot be compared. 4,809 games are enriched; 339 matched on score and date but failed the id check and 41 were ambiguous, so neither is used.

## 2. How each field was filled

| Field | Class | Rule |
|---|---|---|
| Game ID | DERIVED | `GLEAGUE-` + the owner `GAME_ID`. Stable |
| Native Game ID | OBSERVED | `GAME_ID` |
| Season, Season Year | OBSERVED / DERIVED | The API season (for example 2023-24) and its first year |
| Competition Phase, Game Type | DERIVED | Season type: Regular Season → Regular Season; Playoffs → Playoffs; Showcase → Not applicable (phase text names the Showcase / Tip-Off Tournament). Finals are not distinguished from earlier play-off rounds |
| Date | OBSERVED | `GAME_DATE` (US local date) |
| Home, Away, Team A, Team B | OBSERVED | `TEAM_NAME` of the row whose `MATCHUP` reads `vs.` (home) and `@` (away). Neutral-site games still follow the owner's designation; ESPN's neutral flag is copied where joined |
| Scores and derived result fields | OBSERVED / DERIVED | `PTS` of each team row; home-away. One owner row pair prints a tie (Albuquerque 102-102 Tulsa, 1 January 2005), kept as printed (`TIE_AS_PRINTED`): a basketball game cannot end level, so treat it as a source defect |
| Home/Away Q1–Q4, OT, Overtime Periods | OBSERVED (ESPN) | ESPN `linescores` where joined; overtime is any period after the fourth. Blank otherwise |
| Venue, City | OBSERVED (ESPN) | ESPN venue name, city and state where joined |
| Attendance | OBSERVED (ESPN) | Where joined. Zero is kept only inside 1 Feb 2020 to 30 Jun 2022 (the 2020-21 bubble and closed-door games); 310 zeros outside it are blanked as suspected defaults |
| Start Time (UTC) | OBSERVED (ESPN) | ESPN event time (UTC) where joined |
| Start Time (Local), Referees, Round / Stage, Notable Players | NOT_IN_SOURCE | Blank |

## 3. Schema migration

Same 46-column header as the other basketball folders rebuilt on 2026-10-14 (full list in the KBL folder's DATA_PROVENANCE §3). All 13 placeholder names keep their meaning.

**Canonical path (R06):** `Previous Sports Results/Basketball/NBA G League/<YEAR>/<YEAR>_games.csv` is the only copy. Do not recreate `Basketball/G League/` or the root folder `NBA_G_League_Basketball_CSVs/`.

## 4. Checks run and known defects

**Checks run (2026-10-14):** 10,947 games; 0 duplicate Game IDs; 0 weekday disagreements; every team has the same number of regular-season games (48 in 2004-05 and 2005-06, 50 from 2006-07 to 2018-19 with one-game exceptions in 2008-09 and 2014-15, 15 in the 2020-21 bubble, 32–36 from 2022-23), except 2019-20 (41–44, stopped by COVID-19) and 2021-22 (31–35). Those exceptions were not checked game by game.

**Independent check, a sample only:** the 2024-25 final (Osceola Magic 129-118 Stockton Kings on 8 April 2025, Stockton 144-126 Osceola on 11 April, Osceola 110-118 Stockton on 14 April) agrees with English Wikipedia's 2024-25 NBA G League season article on dates, home team and scores.

Flags carried in `QA Flags` (a row can carry several):

| Flag | Rows |
|---|---:|
| `ENRICHED_FROM_ESPN_EVENT_<id>` | 4,809 |
| `ESPN_JOIN_TEAM_ID_DISAGREES_NOT_USED` | 339 |
| `ATTENDANCE_ZERO_OUTSIDE_COVID_PERIOD_SUSPECTED_DEFAULT_BLANKED` | 310 |
| `ATTENDANCE_ZERO_COVID_PERIOD` | 277 |
| `NEUTRAL_SITE_PER_ESPN` | 206 |
| `ESPN_JOIN_AMBIGUOUS_NOT_USED` | 41 |
| `TIE_AS_PRINTED` | 1 |

## 5. Use rules

- Point-in-time and form windows as in ARCHIVE_USE_GUIDE §3 and §9; the archive was captured 2026-10-14.
- Quarter, venue and attendance features exist only on rows flagged `ENRICHED_FROM_ESPN_EVENT_<id>` (2018 onward), and they are evidence B.
- Exclude the 2005 tie from scoring statistics.
- Settle a live card from the league's own record ([SOURCES.md](../../../SOURCES.md) §3.33).

## 6. Per-season counts

| Season | Rows | Regular season | Play-off / final types | Other (`Not applicable`) | Quarters filled | Start time filled | Attendance filled | Referees filled | Venue filled | Rows with any QA flag |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2004-05 | 144 | 144 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2005-06 | 194 | 192 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2006-07 | 305 | 300 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2007-08 | 357 | 350 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2008-09 | 407 | 399 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2009-10 | 420 | 400 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2010-11 | 418 | 400 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2011-12 | 418 | 400 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2012-13 | 415 | 400 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2013-14 | 442 | 425 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2014-15 | 468 | 451 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2015-16 | 493 | 475 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2016-17 | 569 | 550 | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2017-18 | 662 | 650 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2018-19 | 688 | 675 | 13 | 0 | 628 | 628 | 570 | 0 | 628 | 681 |
| 2019-20 | 597 | 597 | 0 | 0 | 546 | 546 | 505 | 0 | 546 | 591 |
| 2020-21 | 142 | 135 | 7 | 0 | 141 | 141 | 141 | 0 | 141 | 141 |
| 2021-22 | 676 | 458 | 12 | 206 | 608 | 608 | 608 | 0 | 608 | 660 |
| 2022-23 | 763 | 480 | 12 | 271 | 704 | 704 | 646 | 0 | 704 | 759 |
| 2023-24 | 789 | 527 | 13 | 249 | 728 | 728 | 666 | 0 | 728 | 783 |
| 2024-25 | 789 | 527 | 13 | 249 | 724 | 724 | 676 | 0 | 724 | 787 |
| 2025-26 | 791 | 558 | 16 | 217 | 730 | 730 | 687 | 0 | 730 | 787 |
| **Total** | **10,947** | **9,493** | **262** | **1,192** | **4,809** | **4,809** | **4,499** | **0** | **4,809** | **5,190** |
