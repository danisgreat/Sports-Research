# B.League (Japan) top division 2016-17 to 2026-27: provenance, schema and known defects

**Status (2026-10-14):** the yearly files `<YEAR>/<YEAR>_games.csv` for 2016 to 2026 were rebuilt from observed source fields only, under [framework change 2026-10-14-1](../../../research/verification/framework_change_2026-10-14-1/IMPLEMENTATION.md) (audit items R01–R07, R26, R27). Before this, main held header-only placeholders. Commit `e73c9c24e` (2026-10-14) briefly published a build with a generic referee label ("JBL/JBA/B.League Official Crew") on 98.8% of rows, a fixed attendance of 4,200, hand-typed pre-2016 tables with no source receipts, B2 (second-division) and All-Star games mixed in, and a duplicate root export folder. That build is **quarantined outside the repository**; no row below comes from it.

**Seasons before 2016-17 (JBL, bj-league, NBL Japan) are not rebuilt.** The quarantined build had them only as hand-typed tables, which fail the R03 test (no per-row source). Those years keep their header-only placeholder.

These rows are research reference data, not evidence of forecasting skill, and a retrospective compilation (a row's date is when the game was played).

## 1. Source

| Item | Value |
|---|---|
| Publisher | B.LEAGUE official site, `https://www.bleague.jp/` (field owner) |
| Route | `schedule/?data_format=json&year=<YYYY>&tab=1&event=<E>&mon=all&index=<N>` (pages of 20 game cards). Tab 1 is the top division |
| Capture | Captured fresh on 2026-10-14 by this rebuild (about 13:30–15:30 AEDT); one gzip file per page with SHA-256 in [CAPTURE_MANIFEST.csv](../../../research/verification/framework_change_2026-10-14-1/CAPTURE_MANIFEST.csv) |
| Other publishers | **None were used to build a field.** Twelve game-detail pages on bleague.jp and Japanese Wikipedia's 2024-25 post-season article were read as checks only (§4) |

**The `event` parameter does not filter.** `event=2` returns every top-division game of the season (regular season, championship and All-Star). Games are therefore classified from the stage label printed on each card. `event=3` repeats the championship games (duplicates dropped by ScheduleKey); `event=4` (B1 relegation playoff, 16 games) and `event=11` (B1/B2 promotion-relegation, 2 games) add the series games.

**Scope.** Excluded and counted in the change receipt: All-Star and exhibition squads (B.BLACK, B.WHITE, Rising Stars, Asia All-Stars, U18 teams, B2 Selected, Kyushu United: 19 games), one exhibition against KBL club Anyang KGC printed with a round label (a team with fewer than 5 regular-season games in a season is not a member), cards without a final score, and duplicate listings.

## 2. How each field was filled

| Field | Class | Rule |
|---|---|---|
| Game ID | DERIVED | `BLEAGUE-B1-` + ScheduleKey. Stable |
| Native Game ID | OBSERVED | `ScheduleKey <n>` (the card's list-item id) |
| Season, Season Year | DERIVED | From the `year` parameter (season start year) |
| League / Competition Name | DERIVED | "B.League B1" to 2025-26; "B.League top division (schedule tab 1…)" for 2026-27, the first season of the restructured league |
| Competition Phase, Game Type | DERIVED from the printed stage | 第N節 → Regular Season; クォーターファイナル / セミファイナル → Playoffs; ファイナル → Finals; event 4 and 11 → Not applicable. 2026-27 cards print no stage yet: Regular Season, flagged `ROUND_NOT_PRINTED_AT_CAPTURE` |
| Round / Stage | OBSERVED | The printed stage label |
| Date | OBSERVED | The list prints a date header (`2016.09.22(木)`) above each day's games. A game card without its own header takes the header above it (flag `DATE_FROM_PRECEDING_DATE_HEADER`, the page's layout, not a guess). Rescheduled games and series games print their own `MM/DD (weekday)`; that date is used, with the year from the season (flag `DATE_FROM_CARD_MMDD_YEAR_FROM_SEASON`). Every printed weekday agrees with the date |
| Day of Week | DERIVED | From Date |
| Start Time (Local) | OBSERVED | The printed tip-off time (JST) |
| Home, Away, Team A, Team B | OBSERVED | The league's short team names as printed (A東京, 琉球, …) |
| Scores and derived result fields | OBSERVED / DERIVED | As printed; home-away |
| Venue | OBSERVED | Printed `prefecture \| short arena name` |
| Overtime, quarter scores, City, Attendance, Referees, Notable Players, Start Time (UTC) | NOT_IN_SOURCE | The schedule list does not carry them. They exist on per-game pages, which were not captured for this rebuild |

## 3. Schema migration

Same 46-column header as the other basketball folders rebuilt on 2026-10-14 (see the KBL folder's DATA_PROVENANCE §3 for the full list). All 13 placeholder names are kept with the same meaning. Years before 2016 keep their 13-column placeholder.

**Canonical path (R06):** `Previous Sports Results/Basketball/B League/<YEAR>/<YEAR>_games.csv` is the only copy. Do not recreate the quarantined root folder `B_League_Basketball_CSVs/`.

## 4. Checks run and known defects

**Checks run (2026-10-14):** 6,350 games; 0 duplicate Game IDs; 0 weekday disagreements; exactly 60 regular-season games for every team in 2016-17, 2017-18, 2018-19, 2023-24 and 2025-26 (18, 18, 18, 24 and 26 teams). 2019-20 stopped at 40–41 games by COVID-19. In 2020-21 (54–60), 2021-22 (45–59), 2022-23 (59–60) and 2024-25 (59–60) some teams have fewer than 60 listed games; this matches games not played (cancellations) but was **not** checked game by game, so treat those seasons' counts as as-printed.

**Checks of the carried dates and the scores (samples only):**
- 12 of 12 randomly chosen header-dated games (seed 20261014) show the same date on their own bleague.jp game page.
- The 2024-25 final (宇都宮 v 琉球: 81-68, 75-87, 73-71 on 24, 25 and 27 May 2025) agrees with Japanese Wikipedia's `Bリーグポストシーズン 2024-25` bracket.

Flags carried in `QA Flags` (a row can carry several):

| Flag | Rows |
|---|---:|
| `DATE_FROM_PRECEDING_DATE_HEADER` | 5,373 |
| `DATE_FROM_CARD_MMDD_YEAR_FROM_SEASON` | 163 |
| `ROUND_NOT_PRINTED_AT_CAPTURE` | 85 |

## 5. Use rules

- Point-in-time and form windows as in ARCHIVE_USE_GUIDE §3 and §9; the archive was captured 2026-10-14.
- No quarter, overtime or attendance features can be built from this folder.
- Settle a live card from the B.LEAGUE field owner ([SOURCES.md](../../../SOURCES.md) §3.33), not from this file.

## 6. Per-season counts

| Season | Rows | Regular season | Play-off / final types | Other (`Not applicable`) | Quarters filled | Start time filled | Attendance filled | Referees filled | Venue filled | Rows with any QA flag |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2016-17 | 562 | 540 | 15 | 7 | 0 | 562 | 0 | 0 | 562 | 461 |
| 2017-18 | 563 | 540 | 15 | 8 | 0 | 563 | 0 | 0 | 563 | 463 |
| 2018-19 | 558 | 540 | 15 | 3 | 0 | 558 | 0 | 0 | 558 | 475 |
| 2019-20 | 367 | 367 | 0 | 0 | 0 | 367 | 0 | 0 | 367 | 307 |
| 2020-21 | 591 | 574 | 17 | 0 | 0 | 591 | 0 | 0 | 591 | 509 |
| 2021-22 | 619 | 604 | 15 | 0 | 0 | 619 | 0 | 0 | 619 | 542 |
| 2022-23 | 734 | 718 | 16 | 0 | 0 | 734 | 0 | 0 | 734 | 658 |
| 2023-24 | 739 | 720 | 19 | 0 | 0 | 739 | 0 | 0 | 739 | 664 |
| 2024-25 | 736 | 719 | 17 | 0 | 0 | 736 | 0 | 0 | 736 | 660 |
| 2025-26 | 796 | 780 | 16 | 0 | 0 | 796 | 0 | 0 | 796 | 727 |
| 2026-27 | 85 | 85 | 0 | 0 | 0 | 85 | 0 | 0 | 85 | 85 |
| **Total** | **6,350** | **6,187** | **145** | **18** | **0** | **6,350** | **0** | **0** | **6,350** | **5,551** |
