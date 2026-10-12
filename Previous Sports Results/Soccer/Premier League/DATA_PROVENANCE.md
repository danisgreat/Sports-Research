# English top flight 1975-76 to 2025-26: provenance, schema and known defects

**Status (2026-10-12):** the yearly files `<YEAR>/<YEAR>_games.csv` for 1975 to 2025 were rebuilt from observed source fields only, under [framework change 2026-10-12-1](../../../research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md) (audit items R02, R03, R04, R05, R06). Before this, published main held header-only placeholders.

An unpublished local build of 2026-10-12 02:31 AEDT made up a range of fields:
- half-time scores (half of the full-time score)
- kick-off times (15:00)
- attendances (38,500 / 28,400 / 25,000)
- generic referee labels and approximate matchweeks
- a hand-typed Community Shield table whose 2025 row (Manchester City 2-1 Arsenal) is false: the official Liverpool FC record gives Crystal Palace 2-2 Liverpool, Palace winning 3-2 on penalties

That build is **quarantined outside the repository** and was never published. No row below comes from it. The Community Shield is not a league match and is **not included**. It may be added later only with a per-row official receipt.

The folder is named "Premier League" for continuity. Seasons 1975-76 to 1991-92 are the **Football League First Division**, which the `League / Competition Name` column says on every row. These rows are research reference data and a retrospective compilation (see "Point-in-time use").

## 1. Sources

| Seasons | Primary source | Fields it supplies |
|---|---|---|
| 1975-76 to 1992-93 | `england.csv`, tier 1 (engsoccerdata, James Curley; captured 2026-10-12 about 02:24 AEDT) | Date, home, away, full-time goals |
| 1986-87, 1987-88 | `englandplayoffs.csv` (same compiler), rows involving a tier-1 club | Date, teams, score, round/leg, venue where given, attendance, aet/pens |
| 1993-94 to 2025-26 | football-data.co.uk `mmz4281/<code>/E0.csv` (captured 2026-10-12 about 02:24 AEDT) | Date, home, away, full-time goals and result; half-time goals from 1995-96; referee, shots, shots on target, corners, fouls, yellow and red cards from 2000-01; attendance in 2000-01 and 2001-02; kick-off time from 2019-20 |

The football-data files also carry bookmaker odds columns. **These are never read into the archive** (SPORTS_ONLY / MARKET_BLIND). The cached source files stay outside the repository for the same reason; their SHA-256 values are in the change folder's DATA_REBUILD_RECEIPT. The Premier League's PulseLive API, the FA and RSSSF were **not** used for any field. The quarantined build's claim that they were is withdrawn.

## 2. How each field was filled

Classes: **OBSERVED** (copied), **DERIVED** (computed deterministically from observed fields), **CHECKED** (agrees with a second compiler) and **NOT_IN_SOURCE** (blank).

| Field | Class | Rule |
|---|---|---|
| Season, Season Year, League / Competition Name, Match Type | DERIVED | First Division before 1992-93; FA Premier League 1992-93 to 2006-07; Premier League from 2007-08. Play-off rows are labelled separately |
| Round / Matchweek | NOT_IN_SOURCE for league rows | The quarantined build's approximation (match count ÷ 10) is not reproduced. Play-off rows carry the source's round and leg |
| Date, Day of Week | OBSERVED / DERIVED | football-data's dd/mm/yy (19xx for yy ≥ 70) or england.csv's ISO date. Weekday computed |
| Kickoff Time (Local) | OBSERVED 2019-20 onward | Otherwise blank |
| Home, Away, Team A, Team B | OBSERVED | As printed by that season's source. football-data uses short names ("Man United"), england.csv long names |
| Home Club Key, Away Club Key | DERIVED | A slug of the england.csv club name. football-data names map to england.csv names through 51 aliases, each learnt only from games matched unambiguously on date and score. Every alias had 100% agreement (for example "Man United" → Manchester United, 927 of 927). The key is stable across the 1992/1993 source change |
| Full-time goals, Match Score | OBSERVED, CHECKED 1993-94 to 2024-25 | See §4 |
| Half-time goals, Half Time Score | OBSERVED 1995-96 onward | Blank before. **Never estimated** |
| Total Goals, Winning Margin, Winning Team, Losing Team, Result | DERIVED | From full-time goals. football-data's own FTR result column agreed on every row |
| Points Home / Away | DERIVED | 2 for a win before 1981-82, 3 from 1981-82; 1 for a draw. Blank for play-offs |
| Extra Time / Penalties (as printed) | OBSERVED | Play-offs only |
| Shots, Shots on Target, Corners, Fouls, Yellow / Red Cards | OBSERVED 2000-01 onward | football-data match statistics. Treat as evidence B for corner contracts. Settle a live card from the official field owner ([SOURCES.md](../../../SOURCES.md) §3.4) |
| Venue | OBSERVED for one play-off row only | The home club's ground is **not** inferred |
| City, Region, Notable Players | NOT_IN_SOURCE | Blank |
| Attendance | OBSERVED 2000-01 and 2001-02 (759 rows) and some play-offs | Otherwise blank |
| Referee | OBSERVED 2000-01 onward | Otherwise blank. Never a generic label |
| A Succint one line match comment… | DERIVED | From the result only |
| Cross-check (england.csv) | CHECKED | `AGREE`, `AGREE_SCORE_DATE_DIFFERS (…)`, `NO_MATCHING_ROW`, `NOT_COVERED (england.csv lacks this season)`, or `SOURCE_IS_…` where england.csv is itself the source |
| QA Flags, Unavailable Fields | DERIVED | Per row |
| Primary Data Source, Source Retrieved | OBSERVED | Source file and capture time |
| Match Number | DERIVED | Order in the file, by date. It is **not** an identity |
| Match ID | DERIVED | `ENG1-<yyyymmdd>-<home club key>-<away club key>`, plus `-N<k>` only for a same-day repeat (none occur). Stable: no row number is used |

## 3. Schema migration

The previous published file was a 13-column header-only placeholder: `Match Number, Match Type (…), Team A, Team B, Home, Away, Venue, Date, Match Score, Total Goals, Winning Margin, Notable Players, A Succint one line match comment…`. Those names keep their meaning, except that the long `Match Type (…)` header is now `Match Type`. There are 54 columns in total. The quarantined build had 36, which its own SOURCES text miscounted as 38. The placeholder had no rows, so no consumer depended on positions. Read by name.

**Canonical path (R06):** `Previous Sports Results/Soccer/Premier League/<YEAR>/<YEAR>_games.csv` is the only copy. The quarantined build's duplicates (`Soccer/English Premier League/` and the root folder `English_Premier_League_Soccer_CSVs/`, all byte-identical) are not in the repository. Do not recreate them. The older research file `research/data/processed/league_csv/epl_results.csv` remains a separate, independently compiled reference.

## 4. Checks run and known defects

- **Coverage:** 20,740 rows: 20,732 league games and 8 play-off games.
- **League sizes:** every season has the right number of clubs and an equal number of games per club: 22 clubs/42 games, 21/40 in 1987-88, 20/38.
- **Integrity:** 0 duplicate Match IDs, 0 date/weekday disagreements, 0 Community Shield rows, 0 odds columns.
- **Two-compiler agreement:** 11,943 of the 11,944 football-data games from 1993-94 to 2024-25 match england.csv on date and score. The one other game agrees on score but not date. Manchester United 3-1 AFC Bournemouth was postponed from 15 May 2016 and played on 17 May 2016. football-data gives 17 May; england.csv gives 16 May. The two compilers are separate projects, but agreement does not prove that their upstream origins are independent.
- **Not cross-checked:**
  - 2022-23 and 2025-26 (760 games), because england.csv lacks those seasons
  - 1975-76 to 1992-93, which have a single source
- **Independent check, a sample only:** 9 of 9 games agree with the ESPN site API scoreboard (`site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard?dates=…`, read 2026-10-12): Liverpool 4-2 Bournemouth on 2025-08-15, Manchester United 3-1 Bournemouth on 2016-05-17, and all seven games of 2010-10-16.

## 5. Use rules

- **Point-in-time:** these are retrospective compilations captured 2026-10-12. A row may feed a card only if its date is before the card's cutoff, and the card must say so (R28).
- **Form windows (L5/L10/L15/L20):** use `Home Club Key` / `Away Club Key`, which are stable across eras, and league rows only.
- **Half-time and period work:** use 1995-96 onward only. Shots and corners: 2000-01 onward only.
- This file is not an official record. Settle from the official field owner.

## 6. Per-season counts

| Season | League | Rows | Clubs | HT score | Kick-off | Referee | Stats | Attendance | Cross-check | Primary source |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1975-76 | Football League First Division | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1976-77 | Football League First Division | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1977-78 | Football League First Division | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1978-79 | Football League First Division | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1979-80 | Football League First Division | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1980-81 | Football League First Division | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1981-82 | Football League First Division | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1982-83 | Football League First Division | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1983-84 | Football League First Division | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1984-85 | Football League First Division | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1985-86 | Football League First Division | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1986-87 | Football League First Division | 462 + 4 play-off | 22 | 0 | 0 | 0 | 0 | 4 | SOURCE_IS_ENGLANDPLAYOFFS_CSV 4, SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1987-88 | Football League First Division | 420 + 4 play-off | 21 | 0 | 0 | 0 | 0 | 4 | SOURCE_IS_ENGLANDPLAYOFFS_CSV 4, SOURCE_IS_ENGLAND_CSV 420 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1988-89 | Football League First Division | 380 | 20 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 380 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1989-90 | Football League First Division | 380 | 20 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 380 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1990-91 | Football League First Division | 380 | 20 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 380 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1991-92 | Football League First Division | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1992-93 | FA Premier League | 462 | 22 | 0 | 0 | 0 | 0 | 0 | SOURCE_IS_ENGLAND_CSV 462 | england.csv (engsoccerdata, J. Curley), tier 1 |
| 1993-94 | FA Premier League | 462 | 22 | 0 | 0 | 0 | 0 | 0 | AGREE 462 | football-data.co.uk mmz4281/9394/E0.csv |
| 1994-95 | FA Premier League | 462 | 22 | 0 | 0 | 0 | 0 | 0 | AGREE 462 | football-data.co.uk mmz4281/9495/E0.csv |
| 1995-96 | FA Premier League | 380 | 20 | 380 | 0 | 0 | 0 | 0 | AGREE 380 | football-data.co.uk mmz4281/9596/E0.csv |
| 1996-97 | FA Premier League | 380 | 20 | 380 | 0 | 0 | 0 | 0 | AGREE 380 | football-data.co.uk mmz4281/9697/E0.csv |
| 1997-98 | FA Premier League | 380 | 20 | 380 | 0 | 0 | 0 | 0 | AGREE 380 | football-data.co.uk mmz4281/9798/E0.csv |
| 1998-99 | FA Premier League | 380 | 20 | 380 | 0 | 0 | 0 | 0 | AGREE 380 | football-data.co.uk mmz4281/9899/E0.csv |
| 1999-00 | FA Premier League | 380 | 20 | 380 | 0 | 0 | 0 | 0 | AGREE 380 | football-data.co.uk mmz4281/9900/E0.csv |
| 2000-01 | FA Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 380 | AGREE 380 | football-data.co.uk mmz4281/0001/E0.csv |
| 2001-02 | FA Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 379 | AGREE 380 | football-data.co.uk mmz4281/0102/E0.csv |
| 2002-03 | FA Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/0203/E0.csv |
| 2003-04 | FA Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/0304/E0.csv |
| 2004-05 | FA Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/0405/E0.csv |
| 2005-06 | FA Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/0506/E0.csv |
| 2006-07 | FA Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/0607/E0.csv |
| 2007-08 | Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/0708/E0.csv |
| 2008-09 | Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/0809/E0.csv |
| 2009-10 | Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/0910/E0.csv |
| 2010-11 | Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/1011/E0.csv |
| 2011-12 | Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/1112/E0.csv |
| 2012-13 | Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/1213/E0.csv |
| 2013-14 | Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/1314/E0.csv |
| 2014-15 | Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/1415/E0.csv |
| 2015-16 | Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 379, AGREE_SCORE_DATE_DIFFERS 1 | football-data.co.uk mmz4281/1516/E0.csv |
| 2016-17 | Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/1617/E0.csv |
| 2017-18 | Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/1718/E0.csv |
| 2018-19 | Premier League | 380 | 20 | 380 | 0 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/1819/E0.csv |
| 2019-20 | Premier League | 380 | 20 | 380 | 380 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/1920/E0.csv |
| 2020-21 | Premier League | 380 | 20 | 380 | 380 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/2021/E0.csv |
| 2021-22 | Premier League | 380 | 20 | 380 | 380 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/2122/E0.csv |
| 2022-23 | Premier League | 380 | 20 | 380 | 380 | 380 | 380 | 0 | NOT_COVERED 380 | football-data.co.uk mmz4281/2223/E0.csv |
| 2023-24 | Premier League | 380 | 20 | 380 | 380 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/2324/E0.csv |
| 2024-25 | Premier League | 380 | 20 | 380 | 380 | 380 | 380 | 0 | AGREE 380 | football-data.co.uk mmz4281/2425/E0.csv |
| 2025-26 | Premier League | 380 | 20 | 380 | 380 | 380 | 380 | 0 | NOT_COVERED 380 | football-data.co.uk mmz4281/2526/E0.csv |
| **Total** | | **20,740** | | | | | | | **AGREE 11,943 · date differs 1 · not covered 760 · single-source 8,036** | |
