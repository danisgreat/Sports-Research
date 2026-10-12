# Czech top-flight ice hockey 1975-76 to 2025-26: provenance, schema and known defects

**Status (2026-10-12):** the yearly files `<YEAR>/<YEAR>_games.csv` for 1975 to 2025 were rebuilt from observed source fields only, under [framework change 2026-10-12-1](../../../research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md) (audit items R01, R04, R05, R06, R26, R27). Before this, published main held header-only placeholders for these years. An unpublished local build of 2026-10-12 02:14 AEDT invented dates (15 September / "Friday" for 16,242 rows), start times (17:30), attendances (5,420 / 4,800), referee text and balanced period scores. That build is **quarantined outside the repository** and was never published. No row below comes from it.

These rows are research reference data. They are not evidence of forecasting skill, and they are a retrospective compilation: a row's date says when the game was played, not when the result became available (see "Point-in-time use").

## 1. Source

| Item | Value |
|---|---|
| Publisher | Hockey Archives (Marc Branchu), `https://www.hockeyarchives.info/` |
| Pages | `Tchecoslovaquie1976.htm` … `Tchecoslovaquie1993.htm` (seasons 1975-76 to 1992-93), `Tcheque1994.htm` … `Tcheque2026.htm` (1993-94 to 2025-26) |
| Capture | One HTML file per season, captured 2026-10-12 about 02:05 AEDT by an earlier local session. Not re-fetched for this rebuild; each page's SHA-256 is in §6 |
| Language | French narrative with game lines in a fixed format |
| Other publishers | **None were read.** Hokej.cz, the Czech federation and Wikipedia were not used to build any field. The quarantined build's claim that they were is withdrawn |

The top division is read from named page sections only:
- **1975-76 to 1992-93:** anchors `L1`, `L1f` (final pool), `L1m`/`L1maintien` (relegation pool), `L1po` (play-offs) and `L1prom` (promotion/relegation).
- **1993-94 onward:** anchors `Extraliga`/`Extraligar` (regular season), `Extraligamaintien`, `Extraligapo`, and `Extraligaprom`/`Extraligapromrel`.

Standings sections (suffix `c`) and the commentary section `Extraligacom` hold no games. The anchors `Dresde` (2019-20) and `Shcherbak` (2022-23) are commentary anchors inside the regular season; they do not end it. From 1993-94, a section stops at a "1re ligue" or "I. liga" heading, so second-division games cannot enter. Before 1993, "I. liga" **is** the top division.

## 2. How each field was filled

Classes: **OBSERVED**, copied as printed; **DERIVED**, computed deterministically from observed fields only; **CONFLICT**, observed but internally inconsistent, kept as printed and flagged; **NOT_IN_SOURCE**, always blank.

| Field | Class | Rule |
|---|---|---|
| Season, Season Year | DERIVED | From the page's season |
| League / Competition Name | DERIVED | "Czechoslovak First League (1. liga)" before 1993-94, "Czech Extraliga" after |
| Source Section, Game Type | OBSERVED / DERIVED | Anchor name, mapped by the table in §1 |
| Round / Stage | OBSERVED | "Round N" from the `Ne journée` header. In play-off and relegation sections, the stage named in the heading (quarter-finals, semi-finals, final, third place, barrage) |
| Date, Day of Week | OBSERVED | From the round header `(weekday d month yyyy)`, overridden by a per-game `[weekday d month]`, `(weekday d month)`, `(le d month)` or bare `d month yyyy`. The year is inferred for July to December as the season's first year, otherwise the second. The weekday is computed from the date |
| Date Basis | DERIVED | `ROUND_HEADER`, `GAME_BRACKET`, `GAME_NOTE` or `NOT_IN_SOURCE` |
| Source Date Note | OBSERVED | Play-off rounds print a list of dates for a whole round ("15, 16, 19 … mars 2024"). The list is kept verbatim. **No individual play-off date is assigned from it**: 1,843 play-off and relegation games have a blank Date |
| Start Time (Local), City, Region, Attendance, Referees, Notable Players | NOT_IN_SOURCE | Always blank |
| Venue, Venue Basis | OBSERVED where printed | Filled only when the source prints a relocated venue (`[à Nitra]`, `[… à Dresde, ALL]`, `[en plein air …]`): 34 games. Otherwise blank with `NOT_IN_SOURCE`. The home club's usual arena is **not** inferred |
| Home, Away, Team A, Team B | OBSERVED | Names exactly as printed. Spelling varies by era (Plzen/Plzeň, Ceské Budejovice/České Budějovice) |
| Home Key, Away Key | DERIVED | Accent-stripped, lower-case slug of the printed name. **Club lineage is not resolved**: renamed clubs get different keys (VZKG Ostrava → Vítkovice Ostrava in 1976-77; Gottwaldov → Zlín) |
| Home Score, Away Score, Game Score | OBSERVED | As printed. In the modern format, the printed score includes the deciding shootout goal ("2-1 t.a.b."). In the 1980s format, the score excludes the shootout and the tally is printed separately ("4-4 a.p. … / 3-1 aux tirs au but") |
| Score Marker (as printed) | OBSERVED | `*` or `K` after the score. `K` is the Czech kontumace (forfeit) mark. In 2002-03 both `*` games were annulled and replayed, but `*` is not defined generally: read the row's flags |
| Official Result Note (as printed) | OBSERVED | Awarded results ("0-5 sur tapis vert"), "par forfait", "[arrêté à 38'49"]" |
| Result, Winning Team, Losing Team | DERIVED | An awarded result overrides the played score. A forfeit is labelled "(Forfeit)". Otherwise the result comes from the shootout tally or the printed score and marker. Draws are kept: ties, including after overtime, were legal in several eras |
| Total Goals, Winning Margin | DERIVED | From the printed score |
| Overtime, Shootout | OBSERVED / DERIVED | `a.p.`, `t.a.b.` or a shootout tally. 4 games print extra-period pairs without a marker: Overtime = Yes, flagged `OT_MARKER_MISSING_IN_SOURCE` |
| Period Scores (as printed) | OBSERVED | Verbatim, including malformed text |
| Home/Away P1–P3, OT, SO | DERIVED | Split from the printed pairs. Multiple overtime pairs are summed into OT. In the `t.a.b.` format the last pair is the shootout. **Nothing is balanced**: a printed sum that differs from the score is flagged `PERIOD_SUM_MISMATCH` (55 rows), never adjusted |
| A Succint one line game comment… | DERIVED | Generated from the result only, with no narrative and no venue |
| Source Line (verbatim) | OBSERVED | The exact game line, which is the per-row receipt |
| QA Flags, Unavailable Fields | DERIVED | See §4 |
| Primary Data Source, Source Retrieved | OBSERVED | Page URL and capture time |
| Game Number | DERIVED | Order within the season file. It is **not** an identity |
| Game ID | DERIVED | `CZE1-<season year>-<SECTION>-<home key>-<away key>-<yyyymmdd>` when dated. Otherwise the same stem plus `-N<k>`, the k-th listing of that ordered pairing in that section. Adding a missing game elsewhere does not change other IDs |

## 3. Schema migration

The previous published file was a 13-column header-only placeholder: `Game Number, Game Type (…), Team A, Team B, Home, Away, Venue, Date, Game Score, Total Goals, Winning Margin, Notable Players, A Succint one line game comment…`. All 13 names are kept with the same meaning. 43 columns are added (56 in total; the quarantined build had 44). The placeholder had no rows, so no consumer depended on row positions. Read columns by name.

Full header, in order: Game Number, Game ID, Season, Season Year, League / Competition Name, Source Section, Game Type, Round / Stage, Date, Day of Week, Date Basis, Source Date Note, Start Time (Local), Team A, Team B, Home, Away, Home Key, Away Key, Home Score, Away Score, Game Score, Score Marker (as printed), Official Result Note (as printed), Total Goals, Winning Margin, Winning Team, Losing Team, Result, Overtime, Shootout, Shootout Score (as printed), Period Scores (as printed), Home P1, Away P1, Home P2, Away P2, Home P3, Away P3, Home OT, Away OT, Home SO, Away SO, Venue, Venue Basis, City, Region, Attendance, Referees, Notable Players, A Succint one line game comment to summarise that game, Source Line (verbatim), QA Flags, Unavailable Fields, Primary Data Source, Source Retrieved.

**Canonical path (R06):** `Previous Sports Results/Ice Hockey/Czech Extraliga/<YEAR>/<YEAR>_games.csv` is the only copy. The two duplicate trees of the quarantined build (`Czechia Extraliga/` and the root folder `Czechia_Extraliga_Ice_Hockey_CSVs/`) are not in the repository. Do not recreate them.

## 4. Checks run and known source defects

**Checks run (2026-10-12):**
- Every file parsed.
- 18,752 games; 0 duplicate Game IDs; 0 unmatched game-like lines inside top-division sections.
- 0 date/weekday disagreements between Date and Day of Week. The weekday is computed, and the **printed** weekday is compared separately (10 conflicts below).
- 16,909 games dated, of which 74 genuinely on 15 September.
- Regular-season games per team and per ordered pairing were checked in every season.

**Independent check, a sample only:** 8 of 8 games in the 2023-24 play-offs agree with the Czech Wikipedia season article (`cs.wikipedia.org/wiki/Česká_hokejová_extraliga_2023/2024`, read 2026-10-12) on score, period scores and overtime marker:
- the quarter-final Pardubice–Hradec Králové 5-4 a.p. (0-2, 3-1, 1-1, 1-0) of 15 March 2024
- the semi-finals Pardubice–Litvínov 2-1, 3-0, 2-3, 5-6
- the semi-finals Sparta–Třinec 3-0, 3-2 a.p., 2-3 a.p.

A sample of 8 out of 18,752 does not certify the archive.

| Flag / pattern | Rows | Meaning and what to do |
|---|---:|---|
| `PERIOD_SUM_MISMATCH` | 55 | Printed periods do not add to the printed score (source typo). Use the final score; drop this row from period-level analysis |
| `SO_DECIDING_GOAL_NOT_PRINTED_AS_PAIR` | 32 | `t.a.b.` with only one extra pair; the printed score includes the shootout goal. Consistent, informational |
| `POSSIBLE_DUPLICATE_LISTING_OF_GAME_NUMBER_n` | 21 | Same section, teams, score and periods as an earlier row. Usually a source repeat. Exclude before counting games. Verify before treating it as a real second game |
| `MARKER_ASTERISK` / `MARKER_K_KONTUMACE` | 15 / 1 | Official decision marker; read with the Official Result Note |
| `SOURCE_WEEKDAY_CONFLICT` | 10 | The printed weekday does not match the printed date. The date is kept. The true day is unknown within the source |
| `PERIODS_NOT_IN_SOURCE` | 7 | No period breakdown printed |
| `AWARDED_RESULT` / `FORFEIT_NOT_PLAYED` / `ABANDONED` | 5 / 3 / 1 | **Exclude from scoring-rate statistics.** The result fields follow the official award |
| `OT_MARKER_MISSING_IN_SOURCE` | 4 | Extra-period pairs printed without `a.p.` |
| Typos read explicitly (`novemre`, `jeufi`) | 2 | Flagged `SOURCE_TYPO_READ_AS` |
| Other malformed text | 6 | Flagged, values left blank where unparseable |

**Season-level source defects:**
- **2000-01:** one regular-season round reprints round 1's seven results (the rows flagged `POSSIBLE_DUPLICATE_LISTING_OF_GAME_NUMBER_1` to `_7`, dated 2000-10-08). That round's real results are missing: seven ordered pairings appear once instead of twice. **Exclude the seven flagged rows.**
- **1999-00:** Vsetín–Slavia 4-3 is listed twice.
- **2002-03:** two `*` games (Sparta–Slavia 2-2*, Havířov–Třinec 4-2*) were replayed, and both versions are listed.
- **2004-05:** one game is missing (Litvínov–Zlín).
- **2019-20:** one game is missing (Hradec Králové–Mladá Boleslav).
- **2006-07 and 2007-08:** home and away appear swapped for one pairing.
- **1976-77:** VZKG Ostrava changes name to Vítkovice Ostrava mid-season.
- **1985-86 to 1992-93 and 1995-96:** uneven home/away counts follow those seasons' formats.
- **2019-20:** the play-offs were cancelled after 4 games.
- **2025-26:** complete as captured.

## 5. Use rules

- **Point-in-time:** a row may feed a card only if its date is before the card's cutoff, and the card must say the archive is a retrospective compilation captured 2026-10-12 (R28). Undated play-off rows cannot be placed in a last-N window. Use `Source Date Note` to bound them, or leave them out.
- **Form windows (L5/L10/L15/L20):**
  - Use dated rows only.
  - Exclude rows flagged `POSSIBLE_DUPLICATE…`, `AWARDED_RESULT`, `FORFEIT_NOT_PLAYED` and `ABANDONED`.
  - A team's window crosses a renamed key only when the card says so.
- **Period or overtime features:** drop rows with any period flag.
- This file is not an official record. Settle a live card from the official field owner ([SOURCES.md](../../../SOURCES.md) §3.31).

## 6. Per-season counts and source fingerprints

"Pools" means championship and relegation pools; "Prom./rel." means promotion/relegation series against the second tier. "Flagged rows" counts rows with any QA flag, informational ones included. The SHA-256 is that of the captured HTML page (first 16 hex characters; the full hashes are in the change folder's DATA_REBUILD_RECEIPT).

| Season | Rows | Regular | Pools | Playoffs | Prom./rel. | Dated | Periods numeric | Flagged rows | Source file | Source SHA-256 (first 16) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1975-76 | 192 | 132 | 60 | 0 | 0 | 192 | 192 | 0 | `Tchecoslovaquie1976.htm` | `360420cd6c2d1c39` |
| 1976-77 | 264 | 264 | 0 | 0 | 0 | 264 | 264 | 0 | `Tchecoslovaquie1977.htm` | `df0ae6b3920fa6d2` |
| 1977-78 | 264 | 264 | 0 | 0 | 0 | 264 | 264 | 0 | `Tchecoslovaquie1978.htm` | `623badca2a3bfc3c` |
| 1978-79 | 264 | 264 | 0 | 0 | 0 | 264 | 264 | 0 | `Tchecoslovaquie1979.htm` | `78902e17e6b883a9` |
| 1979-80 | 264 | 264 | 0 | 0 | 0 | 264 | 264 | 0 | `Tchecoslovaquie1980.htm` | `a4773191b1e165ae` |
| 1980-81 | 264 | 264 | 0 | 0 | 0 | 264 | 264 | 1 | `Tchecoslovaquie1981.htm` | `9ce1186f303dfd4e` |
| 1981-82 | 264 | 264 | 0 | 0 | 0 | 264 | 264 | 0 | `Tchecoslovaquie1982.htm` | `dcda6f989a7d0331` |
| 1982-83 | 264 | 264 | 0 | 0 | 0 | 264 | 264 | 1 | `Tchecoslovaquie1983.htm` | `0ea7cef098114655` |
| 1983-84 | 270 | 264 | 0 | 0 | 6 | 264 | 270 | 0 | `Tchecoslovaquie1984.htm` | `9adf46a6b5fbc02f` |
| 1984-85 | 270 | 264 | 0 | 0 | 6 | 264 | 270 | 0 | `Tchecoslovaquie1985.htm` | `97d948f437de7c51` |
| 1985-86 | 265 | 204 | 24 | 37 | 0 | 228 | 265 | 0 | `Tchecoslovaquie1986.htm` | `2bddedb8eeb2f75c` |
| 1986-87 | 259 | 204 | 24 | 31 | 0 | 229 | 259 | 0 | `Tchecoslovaquie1987.htm` | `c99c391793cb86e5` |
| 1987-88 | 273 | 204 | 24 | 45 | 0 | 228 | 273 | 0 | `Tchecoslovaquie1988.htm` | `adbbeda19866449c` |
| 1988-89 | 294 | 204 | 16 | 44 | 30 | 252 | 294 | 0 | `Tchecoslovaquie1989.htm` | `a32e93ec5db2bec4` |
| 1989-90 | 326 | 258 | 0 | 38 | 30 | 288 | 326 | 1 | `Tchecoslovaquie1990.htm` | `1bc9bfda5de97e4d` |
| 1990-91 | 377 | 364 | 0 | 13 | 0 | 364 | 377 | 1 | `Tchecoslovaquie1991.htm` | `a6cadb7a3f30672a` |
| 1991-92 | 322 | 266 | 0 | 56 | 0 | 266 | 322 | 1 | `Tchecoslovaquie1992.htm` | `68e6ed054a1a33ca` |
| 1992-93 | 328 | 280 | 0 | 48 | 0 | 280 | 326 | 3 | `Tchecoslovaquie1993.htm` | `95b40c90145eb887` |
| 1993-94 | 313 | 264 | 8 | 29 | 12 | 276 | 313 | 1 | `Tcheque1994.htm` | `3f9059c845bf42f7` |
| 1994-95 | 304 | 264 | 0 | 28 | 12 | 276 | 304 | 2 | `Tcheque1995.htm` | `7a4141ae18c6a23c` |
| 1995-96 | 352 | 280 | 0 | 48 | 24 | 304 | 352 | 4 | `Tcheque1996.htm` | `c3c27d4cc65443cc` |
| 1996-97 | 403 | 364 | 0 | 27 | 12 | 364 | 403 | 1 | `Tcheque1997.htm` | `0421458bab4c7971` |
| 1997-98 | 402 | 364 | 0 | 31 | 7 | 364 | 402 | 2 | `Tcheque1998.htm` | `22cdb3515f3200bf` |
| 1998-99 | 399 | 364 | 0 | 28 | 7 | 364 | 399 | 1 | `Tcheque1999.htm` | `9565126c4e88e0eb` |
| 1999-00 | 392 | 365 | 0 | 23 | 4 | 365 | 392 | 4 | `Tcheque2000.htm` | `266aa037821e00de` |
| 2000-01 | 407 | 364 | 0 | 37 | 6 | 364 | 407 | 11 | `Tcheque2001.htm` | `2d9032fa8b547ed2` |
| 2001-02 | 405 | 364 | 0 | 36 | 5 | 364 | 403 | 8 | `Tcheque2002.htm` | `9558094f42b1b3fd` |
| 2002-03 | 411 | 366 | 0 | 39 | 6 | 366 | 407 | 12 | `Tcheque2003.htm` | `1790b47cd43e508e` |
| 2003-04 | 412 | 364 | 0 | 44 | 4 | 364 | 412 | 4 | `Tcheque2004.htm` | `2d8a0bce5a175f33` |
| 2004-05 | 409 | 363 | 0 | 41 | 5 | 363 | 409 | 6 | `Tcheque2005.htm` | `397824f9e9978b21` |
| 2005-06 | 407 | 364 | 0 | 37 | 6 | 364 | 407 | 6 | `Tcheque2006.htm` | `ea2f4f08a37da7f2` |
| 2006-07 | 411 | 364 | 0 | 47 | 0 | 364 | 411 | 5 | `Tcheque2007.htm` | `a698b462dba58562` |
| 2007-08 | 440 | 364 | 24 | 47 | 5 | 388 | 440 | 12 | `Tcheque2008.htm` | `75004f9a397d5b9f` |
| 2008-09 | 440 | 364 | 24 | 48 | 4 | 388 | 440 | 16 | `Tcheque2009.htm` | `20b62c0cb6390fec` |
| 2009-10 | 440 | 364 | 24 | 47 | 5 | 388 | 440 | 7 | `Tcheque2010.htm` | `683552343bc92b19` |
| 2010-11 | 444 | 364 | 24 | 49 | 7 | 388 | 443 | 5 | `Tcheque2011.htm` | `996c5ac37dd130b6` |
| 2011-12 | 445 | 364 | 24 | 50 | 7 | 388 | 445 | 5 | `Tcheque2012.htm` | `c4f93edcfeeb910b` |
| 2012-13 | 454 | 364 | 12 | 54 | 24 | 401 | 454 | 0 | `Tcheque2013.htm` | `3ad0a11b30123319` |
| 2013-14 | 448 | 364 | 12 | 48 | 24 | 400 | 448 | 2 | `Tcheque2014.htm` | `0a4ae527e0162f85` |
| 2014-15 | 447 | 364 | 12 | 47 | 24 | 400 | 447 | 4 | `Tcheque2015.htm` | `42cc00a325ad5cfd` |
| 2015-16 | 445 | 364 | 12 | 45 | 24 | 400 | 445 | 5 | `Tcheque2016.htm` | `cd33fa66473433c5` |
| 2016-17 | 447 | 364 | 12 | 47 | 24 | 400 | 447 | 1 | `Tcheque2017.htm` | `3f7cedd85b3e2348` |
| 2017-18 | 446 | 364 | 12 | 46 | 24 | 400 | 446 | 3 | `Tcheque2018.htm` | `93a0e924e2c94faa` |
| 2018-19 | 448 | 364 | 12 | 48 | 24 | 400 | 448 | 1 | `Tcheque2019.htm` | `b5636a822ae4281e` |
| 2019-20 | 367 | 363 | 0 | 4 | 0 | 363 | 367 | 2 | `Tcheque2020.htm` | `bdd344b68f02bb16` |
| 2020-21 | 414 | 364 | 0 | 50 | 0 | 364 | 414 | 1 | `Tcheque2021.htm` | `000954e83eecf552` |
| 2021-22 | 477 | 420 | 0 | 52 | 5 | 420 | 477 | 1 | `Tcheque2022.htm` | `6354948bfe1fef73` |
| 2022-23 | 425 | 364 | 0 | 57 | 4 | 364 | 425 | 1 | `Tcheque2023.htm` | `0ee8341f4ff29fc4` |
| 2023-24 | 422 | 364 | 0 | 54 | 4 | 364 | 422 | 2 | `Tcheque2024.htm` | `f4d8714d14926636` |
| 2024-25 | 427 | 364 | 0 | 59 | 4 | 364 | 427 | 1 | `Tcheque2025.htm` | `c28c1e3bd067f5c6` |
| 2025-26 | 425 | 364 | 0 | 56 | 5 | 364 | 425 | 1 | `Tcheque2026.htm` | `002f71badd834e5d` |
| **Total** | **18,752** | | | | | **16,909** | **18,743** | **145** | | |
