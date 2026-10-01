# MLB game-by-game files, 2000-2026

One file per season, `MLB_<YEAR>.csv` (UTF-8 with BOM, opens in Excel). 27 files, **77,829 games**. Each season holds every game played that year: spring training, exhibitions, the regular season, the All-Star Game and the postseason, each labelled. Copies also sit in `Previous Sports Results/Baseball/MLB/<YEAR>/<YEAR>_games.csv` for 2000-2025 (the header-only templates you already had, now filled and byte-identical). Nothing was committed or pushed to git.

**Retrieved 2026-10-01.** 2026 is in progress: the regular season is complete (2,429 games played), but only the 4 Wild Card games already played are included. The rest of the 2026 postseason is not in the file. Re-run before relying on it.

## What is in each season

| Season | Pre-Season | Exhibition | Regular | Postseason | All-Star | Total |
|---|---|---|---|---|---|---|
| 2000 | 407 | 55 | 2429 | 31 | 1 | 2923 |
| 2001 | 481 | 5 | 2429 | 35 | 1 | 2951 |
| 2002 | 480 | 3 | 2426 | 34 | 1 | 2944 |
| 2003 | 461 | 1 | 2430 | 38 | 1 | 2931 |
| 2004 | 405 | 68 | 2428 | 34 | 1 | 2936 |
| 2005 | 473 | 7 | 2431 | 30 | 1 | 2942 |
| 2006 | 483 | 0 | 2429 | 30 | 1 | 2943 |
| 2007 | 488 | 1 | 2431 | 28 | 1 | 2949 |
| 2008 | 478 | 6 | 2428 | 32 | 1 | 2945 |
| 2009 | 570 | 0 | 2430 | 30 | 1 | 3031 |
| 2010 | 477 | 0 | 2430 | 32 | 1 | 2940 |
| 2011 | 504 | 0 | 2429 | 38 | 1 | 2972 |
| 2012 | 493 | 15 | 2430 | 37 | 1 | 2976 |
| 2013 | 539 | 0 | 2431 | 38 | 1 | 3009 |
| 2014 | 457 | 8 | 2430 | 32 | 1 | 2928 |
| 2015 | 498 | 0 | 2429 | 36 | 1 | 2964 |
| 2016 | 485 | 0 | 2428 | 35 | 1 | 2949 |
| 2017 | 549 | 0 | 2430 | 38 | 1 | 3018 |
| 2018 | 499 | 0 | 2431 | 33 | 1 | 2964 |
| 2019 | 477 | 7 | 2429 | 37 | 1 | 2951 |
| 2020 | 328 | 0 | 898 | 53 | 0 | 1279 |
| 2021 | 415 | 0 | 2429 | 37 | 1 | 2882 |
| 2022 | 268 | 0 | 2430 | 40 | 1 | 2739 |
| 2023 | 483 | 0 | 2430 | 41 | 1 | 2955 |
| 2024 | 460 | 7 | 2429 | 43 | 1 | 2940 |
| 2025 | 463 | 7 | 2430 | 47 | 1 | 2948 |
| 2026 | 486 | 0 | 2429 | 4 | 1 | 2920 |

Years differ, as expected:

- **2020:** 60-game season (898 played of 900 scheduled), no All-Star Game, spring training cut off by the shutdown on 12 March, a 16-team postseason with best-of-three Wild Card Series, and neutral-site bubble venues (Petco Park, Dodger Stadium, Globe Life Field, Minute Maid Park). Regular-season attendance reads 0 in both sources.
- **2022:** short spring training after the lockout (268 games).
- **Wild Card:** none before 2012; a single Wild Card **Game** 2012-2019 and 2021; best-of-three Wild Card **Series** in 2020 and from 2022. Postseason rows are labelled by round.
- **Tiebreaker games** (one-game playoffs to decide a division or Wild Card spot: 2007, 2008, 2009, 2013 and two in 2018) are counted in the regular season and are labelled `Regular Season (Tiebreaker Game)`.
- **Expos / Nationals, Devil Rays / Rays, Marlins, Angels, Indians / Guardians, Athletics:** team names are the ones used in that season. Abbreviations and league/division are that season's.
- **Not in the files:** postponed or cancelled games that were never played, World Baseball Classic games (a separate competition), the Futures Game and minor-league games. A postponed game that was made up appears once, on the day it was played, with the original date in `Rescheduled From`.

## Columns

Blank means the source did not publish the value. It never means zero.

**Identity and type**
`Game Number` (1..N in chronological order within the year, by first-pitch time in UTC) - `Game ID (MLB gamePk)` (`ESPN-<id>` for the 2,864 games only ESPN has) - `Season` - `Season Phase` (Pre-Season, Exhibition, Regular Season, Postseason, All-Star Game) - `Game Type` (Spring Training, Exhibition, Regular Season, Regular Season (Tiebreaker Game), Wild Card Game, Wild Card Series, Division Series, League Championship Series, World Series, All-Star Game) - `Series / Round` (ALDS, NLCS, ...) - `Series Game No.` - `Series Length (Games)` - `Series Status After Game` (e.g. "LAD wins 4-1", or "Series tied 2-2" for a regular-season series) - `Date` (local date; a suspended game keeps its start date) - `Day of Week` - `Start Time (UTC)` - `Day/Night` - `Doubleheader` (N, Y traditional, S split) - `Doubleheader Game No.`

**Teams and place**
`Away Team`, `Away Abbr`, `Away League`, `Away Division`, the same four for Home, `Interleague` - `Venue`, `City`, `State/Province`, `Country` - `Neutral or Alternate Site` (Y when the game was not at the designated home team's own ballpark: Tokyo, San Juan, Sydney, Monterrey, London, Williamsport, Field of Dreams, hurricane and weather moves, the 2020 bubble; "Neutral" for All-Star host parks) - `Site / Event Note` (special-event label from MLB such as "Jackie Robinson Day", and suspension details).

**Result**
`Away Score`, `Home Score`, `Total Runs`, `Winning Margin`, `Winning Team`, `Losing Team`, `Result` (Away Win, Home Win, Tie), `Game Score` (text) - `Innings Played`, `Scheduled Innings` (7 for 2020-21 doubleheaders), `Extra Innings`, `Walk-Off Win` (home team won in its last at-bat while tied or behind), `Completed Early / Shortened` (rain-shortened, mercy-rule and called tie games), `Suspended and Resumed`, `Resumed On`, `Rescheduled From` - `Away / Home Line Score (runs by inning)` (X = did not bat).

**Team totals**
`Away/Home Hits, Errors, LOB, At-Bats, Doubles, Triples, HR, RBI, Walks, Strikeouts, Stolen Bases, Hit By Pitch, GIDP, Pitchers Used, Earned Runs`.

**People**
`Winning Pitcher`, `Losing Pitcher`, `Save Pitcher` - `Away/Home Starting Pitcher` (the actual starter, not the probable) - `Away/Home Manager` - `Umpire - Home Plate / First / Second / Third Base / Left Field / Right Field` (LF and RF are used in the postseason and the All-Star Game).

**Conditions and flags**
`Attendance` - `Game Duration (min)` - `Delay (min)` - `Temperature (F)`, `Sky Condition`, `Wind` - `No-Hitter`, `Perfect Game` - `Game Summary` (built from the fields above, not written by a person).

**Provenance and checking**
`Primary Data Source` - `Team Stats Source` - `Independent Check (Retrosheet or ESPN)` - `Check Details`.

## How the data was collected and checked

1. **Primary:** MLB Stats API (the league's own record) for every game in every type.
2. **Independent second source for 2000-2025 regular season, postseason and All-Star Game:** Retrosheet game logs. Team totals, starters and managers come from Retrosheet for those games. Every game was matched to Retrosheet by date and team pair and compared on score, hits, errors, attendance, duration, home-plate umpire, winning pitcher and the walk-off flag.
3. **Independent second source for pre-season and exhibition games:** ESPN scoreboards, every date from 10 February to 31 May of each year. ESPN also supplied the 2,864 games the MLB API does not carry (all of 2000-2005 spring training, plus college and national-team games in other years).
4. **2026 and the 12,367 games Retrosheet does not cover** use the API boxscore for team totals and starters.

| Result of the check | Games |
|---|---|
| Match (no differences) | 70,985 |
| Match with minor differences noted in `Check Details` (errors, attendance, duration, umpire, name variants) | 1,354 |
| Conflict with ESPN by a run on a spring game (API value kept, ESPN score written in the note) | 11 |
| Single source: ESPN only | 2,864 |
| Single source: MLB API only, not found on ESPN (mostly college and international exhibitions) | 181 |
| 2026, no Retrosheet file exists yet | 2,434 |

Full list of the 1,365 games with a note: `MLB_verification_exceptions.csv`.

**Completeness proof.** For every team in every season 2000-2026 (810 team-seasons), the win-loss record computed from these rows equals the league's own running record in the API. Zero mismatches, so no regular-season game is missing or duplicated. Known records agree (2001 Mariners 116-46, 2003 Tigers 43-119, 2016 Cubs 103-58 with one tie, 2022 Dodgers 111-51, 2024 Dodgers 98-64). Total runs, margins, results and winners were re-derived from the scores for all 77,829 rows with no errors; every line score adds up to the score except the 2025 All-Star Game (below).

**Disagreements that were settled**

| Game | Sources | Decision |
|---|---|---|
| 2022-08-13 Pirates at Giants, 2023-10-04 Rangers at Rays, 2024-10-17 Yankees at Guardians | Retrosheet is one hit different | MLB linescore, boxscore team total and the sum of individual batters all agree with each other, so the API value stands |
| 2025 All-Star Game | API NL 7, AL 6; Retrosheet 6-6 | Tied after nine and decided by a home-run swing-off. The API figure is kept (it counts the swing-off as one run) and explained in the note; `Total Runs` includes it |
| 953 games | API errors one lower than Retrosheet | Retrosheet used (official scoresheet; the 2024 World Series Game 5 is 3, the API says 2) |
| 44 games moved to the opponent's park (2010 G20 Blue Jays/Phillies, 2015 Orioles/Rays, 2017 Marlins/Brewers, 2020 makeup doubleheaders and others) | Retrosheet lists the ballpark owner as home | MLB's designated home team (the side that batted last, confirmed from the line scores) is kept and the difference is noted |

## Known limits

- **Managers** exist only for games Retrosheet covers: blank for 2026 and for all pre-season and exhibition games.
- **ESPN-only rows** (2,864) carry date, teams, score, venue, attendance and innings only. They have no hits, errors, line score, umpires, pitchers or totals because ESPN does not publish them for these games. Their venue is blank where ESPN gave none (college games), and college opponent names are ESPN's.
- **Spring-training and exhibition scores** have no second lineage other than ESPN. They agree with ESPN in 9,741 of the 9,752 games both sources carry (99.9%), but they are the least reliable rows in the set.
- **Attendance:** 0 for the first game of a single-admission doubleheader is left blank; real zeros (2020, the closed 2015 Baltimore game) stay 0. Retrosheet and the API differ by small amounts in some years (different counting conventions); only differences above 3% are noted.
- **Home-plate umpire** differs from Retrosheet in 9 games (the API value is kept and the difference is in `Check Details`).
- **2026** has no second-source check for regular-season or postseason games.
- `Game Duration`, `Delay`, `Temperature`, `Sky Condition` and `Wind` are as published by MLB and are blank where MLB has nothing.

Sources and the traps found are recorded in `SOURCES.md` section 3.14.
