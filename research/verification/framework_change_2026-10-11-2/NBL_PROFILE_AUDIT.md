# NBL profile audit (RET-01), 2026-10-11

Prompt 7 procedure, carried out inside the October 11 framework change (run 2). Base revision `abb3e98d7ab2dfc3bd33bcdf42b4a3bf3a11a7d4` (local `main`; published `origin/main` was `2d6d86350`). Read-only on every pre-existing archive file; the only archive change is one **new** file, `Previous Sports Results/Basketball/NBL/2026/2026_games.csv`.

**Method.** The yearly CSVs were copied to a scratch folder outside the repository, carriage returns removed, and counted with `awk` (means, sample standard deviations, correlation, excess kurtosis from central moments). The same code reproduces the published `LP-2026.10.09-v1` NBL row exactly (n 425; 91.41 / 89.72 / 181.13; margin SD 15.28; total SD 19.53; corr 0.241; kurtosis 0.308; overtime 4.7%), which is the check that the method matches the original builder. The 2026-27 downloads were parsed with a short Python script run in isolated mode on the scratch copies; no script or JSON was added to the repository.

## 1. Coverage inventory

| File | Logical records | Header | Fields per row | Line ending | Note |
|---|---:|---|---|---|---|
| `NBL/2020` | 179 | same | 39 | CRLF | not used |
| `NBL/2021` | 168 | same | 39 | CRLF | not used |
| `NBL/2022` | 178 | same | 39 | CRLF | 140 regular-season games |
| `NBL/2023` | 181 | same | 39 | CRLF | 140 |
| `NBL/2024` | 183 | same | 39 (one pre-season row has a quoted venue) | CRLF | 145 |
| `NBL/2025` | 206 | same | 39 on all 206 | LF | 165 regular-season games + 14 mistyped post-season + 27 pre-season |
| `NBL/2026` | none before this run | | | | **new**: 29 games to 2026-10-11 |

Logical records equal physical lines minus the header because no data row of the 2025 file contains a quote, an embedded comma or a newline (`awk` field count 39 on 206 of 206 rows).

## 2. The 2025 file (season 2025-26)

**What the 206 rows are.** 27 pre-season rows (`Pre-Season`, `Pre-Season / NBL Blitz`) and 179 rows typed `Regular Season`. Of the 179, **165 have `Round / Stage` = "Round 1" to "Round 22"** and 14 have names that are not rounds: CHAMPIONSHIP (2), ELIMINATION, IGNITE CUP FINAL, PLAYOFF 1 (3), PLAYOFF 2 (2), QUALIFIER, SEEDING, "SYD 2-1 ADL", "SYD WIN 3-2", "TIED 2-2". The 14 are post-season (and Ignite Cup) games, several named after a series score.

**Schedule reconciliation.** The 165 round-numbered games are 33 for each of the 10 clubs (10 × 33 ÷ 2 = 165), with no duplicate Game ID and no duplicate (home, away, score) key. They match the official 33-game season. `research/data/processed/league_csv/nbl_results.csv` (season `NBL26`) holds the same 165 games, 33 per club, dated 2025-09-18 to 2026-02-20; the multiset of (home, away, home score, away score) is identical, and for all 165 rows the archive `Game ID` (`NBL_2025_2026_<uuid>`) carries the same native UUID as the processed file's `event_key`. The two files may share an upstream (the NBL schedule feed), so this is a consistency check, not an independent collection. BASE_RATES_REGISTER §7.1 reports the same population independently (n 165, total 182.5, SD 19.1, overtime 0.055, home win 0.503), matching the 2025-26 row below.

**Arithmetic checks on the 2022–2025 regular-season rows.** `Total Points` = home + away and `Winning Margin` = |home − away| on every row (0 failures in 2022, 2023, 2024 and 2025).

**Defects found** (none repaired; the guide now warns about each, [ARCHIVE_USE_GUIDE §8](../../../ARCHIVE_USE_GUIDE.md)):
1. `Date`, `Day of Week` and `Start Time (Local)` are blank on all 179 rows typed `Regular Season`. Dates for the 165 genuine games are available from the processed file: [NBL_2025_26_DATE_EVIDENCE.csv](NBL_2025_26_DATE_EVIDENCE.csv) (scheduled UTC starts; 165 of 165 native IDs match; these are scheduled, not actual, starts).
2. The 14 post-season rows are typed `Regular Season`. A profile built on `Game Type` alone would have taken them (7.8% of the file).
3. The quarter columns do not sum to the final on 3 of the 165 regular rows (game numbers 101, 186 and 187; the last two are exactly double the final) and on 3 of the 14 post-season rows (also doubled). The 2024 file has 8 such rows in 145 and the 2022 file 1 in 140. Final scores are not affected.

## 3. Profile windows and the decision

| Window | Games | Mean home | Mean away | Mean total | Margin SD | Total SD | Corr | Kurt | OT | Home win |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2022-23 | 140 | 88.59 | 87.70 | 176.29 | 15.35 | 18.96 | 0.212 | 0.224 | 7.9% | 52.9% |
| 2023-24 | 140 | 92.01 | 89.21 | 181.23 | 14.61 | 17.68 | 0.189 | 1.039 | 3.6% | 59.3% |
| 2024-25 | 145 | 93.54 | 92.16 | 185.70 | 15.88 | 20.74 | 0.261 | -0.089 | 2.8% | 55.2% |
| 2025-26 | 165 | 91.58 | 90.92 | 182.50 | 18.06 | 19.06 | 0.054 | -0.183 | 5.5% | 50.3% |
| **2023-25 (new active row)** | 450 | 92.35 | 90.79 | 183.14 | 16.34 | 19.26 | 0.163 | 0.156 | 4.0% | 54.7% |
| 2022-24 (retained prior) | 425 | 91.41 | 89.72 | 181.13 | 15.28 | 19.53 | 0.241 | 0.308 | 4.7% | 55.8% |
| 2026-27 to 2026-10-11 (not pooled) | 29 | 95.07 | 92.31 | 187.38 | 13.23 | 20.38 | 0.411 | -0.789 | 3.4% | 62.1% |

**Why this window.** ARCHIVE_USE_GUIDE recipe R1 uses the last three regular seasons, and every other league row is a three-season window ending in 2025. The 2022-24 row was one season stale (it omits 2025-26) and included the lowest-scoring season, 2022-23: its mean total sits 9.4 points below 2024-25, a difference of 4.0 standard errors (SE 2.35), so the seasons are not one population. The later three seasons differ by at most 4.5 points (largest z about 1.9). The windows were compared before pooling, as prompt 7 §4 requires, and the 2026-27 games were not pooled (early season, partial, a different source).

**What changes for a card.** Mean total +2.0, margin SD +1.1, total SD −0.3, correlation −0.08. The change is a data update. It is not evidence of better forecasts: the paired prospective comparison is FC10-PROFILE-v1 and has not started.

## 4. The 2026-27 snapshot (new file)

**Scope declared before collection.** NBL, 2026-27 regular season only (ESPN `season.slug` = `regular-season`), completed games as retrieved late on 2026-10-11 (before 23:40 AEDT), event grain = one row per game, venue-local calendar date. The 14 pre-season games ESPN lists are excluded.

**Source and field provenance.** ESPN site API `basketball/nbl/scoreboard?dates=YYYYMMDD`, one request per day from 2026-09-01 to 2026-10-11 (41 requests, all HTTP 200; 14 returned no event). Per game: ESPN event id, UTC start, home and away team, final score, linescore per period. Evidence class B (structured provider, collector lineage unknown). Mapped to the existing 39-column schema; the header is byte-identical to the 2025 file's. Written: `Game ID` = `NBL_ESPN_<event id>`; `Season` 2026-2027; `Season Year` 2026; local `Date`, `Day of Week` and `Start Time (Local)` derived from the UTC start and the home club's time zone (Perth +8; Brisbane and Cairns +10; Melbourne, SEM, Sydney, Illawarra and Tasmania +10 then +11 from 2026-10-03 16:00Z; Adelaide +9:30 then +10:30 from 2026-10-03 16:30Z; New Zealand +12 then +13 from 2026-09-26 14:00Z); `Team A` = home as in the 2025 file; `Result` winner-first; `Game Score` home-away; the four quarter pairs and one overtime pair. **Left blank because the source does not supply them** (blank means unknown): `Round / Stage`, `Venue`, `City / State`, `Attendance`, `Notable Players`, the comment column.

**Checks run on the written file** (separate `awk` code from the generator): header identical to the 2025 header; 39 fields on 29 of 29 rows; total = home + away; margin = |home − away|; winner, loser, `Result` text and `Game Score` consistent with the scores; quarters (+ overtime) sum to the final for home and away; `Overtime` flag agrees with the overtime columns (1 game); no duplicate `Game ID` or (date, home, away); `Game Number` 1 to 29 in order; day of week matches the date; round trip to the parsed ESPN table identical (event id, home score, away score). **0 failures on all 29 rows.** Local start times agree with the scheduled starts on the cards: P-560 19:30, P-565 19:30, P-566 18:30 Perth (21:30 AEDT), P-575 17:00.

**Independent confirmation of results** (predeclared spread: early, middle and late season, an overtime game, the lowest and the highest total). 10 of 29 games were matched, to the point, against a source other than ESPN; none disagreed.

| # | Local date and start | Home | Away | Final | ESPN event | Independent confirmation |
|---:|---|---|---|---|---|---|
| 1 | 2026-09-19 19:30 | Melbourne United | Adelaide 36ers | 95-97  | 401875251 | single source (ESPN) |
| 2 | 2026-09-19 19:30 | Perth Wildcats | South East Melbourne Phoenix | 79-100  | 401875243 | single source (ESPN) |
| 3 | 2026-09-20 17:00 | New Zealand Breakers | Illawarra Hawks | 95-81  | 401875263 | single source (ESPN) |
| 4 | 2026-09-20 17:00 | Sydney Kings | Cairns Taipans | 111-90  | 401875242 | single source (ESPN) |
| 5 | 2026-09-21 19:30 | Tasmania JackJumpers | South East Melbourne Phoenix | 96-91  | 401875253 | single source (ESPN) |
| 6 | 2026-09-22 19:30 | Brisbane Bullets | New Zealand Breakers | 88-85  | 401875244 | single source (ESPN) |
| 7 | 2026-09-23 19:30 | Cairns Taipans | Tasmania JackJumpers | 93-87  | 401875241 | single source (ESPN) |
| 8 | 2026-09-24 19:30 | South East Melbourne Phoenix | Melbourne United | 61-86  | 401875267 | basketball.com.au report (quarters) |
| 9 | 2026-09-24 19:30 | Perth Wildcats | Adelaide 36ers | 98-97  | 401875245 | single source (ESPN) |
| 10 | 2026-09-25 19:30 | Brisbane Bullets | Illawarra Hawks | 103-95  | 401875252 | single source (ESPN) |
| 11 | 2026-09-26 19:30 | Perth Wildcats | New Zealand Breakers | 97-93  | 401875254 | single source (ESPN) |
| 12 | 2026-09-27 15:30 | Adelaide 36ers | Cairns Taipans | 83-69  | 401875257 | single source (ESPN) |
| 13 | 2026-09-27 18:00 | Sydney Kings | Illawarra Hawks | 121-100  | 401875277 | basketball.com.au report (quarters) |
| 14 | 2026-09-30 20:30 | New Zealand Breakers | Cairns Taipans | 98-75  | 401875246 | single source (ESPN) |
| 15 | 2026-09-30 19:30 | Sydney Kings | Brisbane Bullets | 93-78  | 401875279 | single source (ESPN) |
| 16 | 2026-10-01 19:30 | Tasmania JackJumpers | Melbourne United | 84-82  | 401875255 | P-532 settlement (log) |
| 17 | 2026-10-02 19:30 | Illawarra Hawks | Adelaide 36ers | 114-92  | 401875256 | single source (ESPN) |
| 18 | 2026-10-02 19:30 | Perth Wildcats | South East Melbourne Phoenix | 92-88  | 401875287 | single source (ESPN) |
| 19 | 2026-10-03 17:30 | Brisbane Bullets | Tasmania JackJumpers | 99-109 OT | 401875250 | basketball.com.au report (OT 18-8) |
| 20 | 2026-10-03 19:30 | Melbourne United | Cairns Taipans | 95-107  | 401875260 | single source (ESPN) |
| 21 | 2026-10-04 15:00 | South East Melbourne Phoenix | Illawarra Hawks | 113-96  | 401875262 | single source (ESPN) |
| 22 | 2026-10-04 16:30 | Adelaide 36ers | New Zealand Breakers | 72-88  | 401875248 | single source (ESPN) |
| 23 | 2026-10-07 19:00 | Adelaide 36ers | Melbourne United | 91-96  | 401875259 | P-542 settlement (log) |
| 24 | 2026-10-08 18:30 | Cairns Taipans | Brisbane Bullets | 97-91  | 401875265 | P-552 settlement (log) |
| 25 | 2026-10-09 19:30 | Illawarra Hawks | Tasmania JackJumpers | 112-122  | 401875247 | P-560 settlement (Austadiums) |
| 26 | 2026-10-10 19:30 | South East Melbourne Phoenix | Melbourne United | 99-104  | 401875266 | P-565 settlement (RealGM quarters, club) |
| 27 | 2026-10-10 18:30 | Perth Wildcats | New Zealand Breakers | 100-84  | 401875268 | P-566 settlement (NBL.com.au story) |
| 28 | 2026-10-11 15:00 | Sydney Kings | Adelaide 36ers | 78-84  | 401875249 | single source (ESPN) |
| 29 | 2026-10-11 17:00 | Illawarra Hawks | Cairns Taipans | 100-110  | 401875258 | P-575 settlement (RealGM quarters) |

The ten confirmations are: seven finals already settled in Combined Log 7 from NBL, RealGM, Austadiums or club sources (P-532, P-542, P-552, P-560, P-565, P-566, P-575; P-565 and P-575 also match the RealGM quarter scores exactly) and three match reports on basketball.com.au read on 2026-10-11 (Brisbane–Tasmania 99–109 in overtime with 91–91 after regulation and 8–18 in overtime; Melbourne United 86–61 over SEM with the Phoenix on 4 points in the fourth quarter, consistent with the ESPN box score of 24-for-88 from the field and 111 recorded fourth-quarter plays; Sydney 121–100 over Illawarra with exact quarter scores). Two further facts fit. The SEM coach said the club played Perth on the Saturday, Hobart on the Monday and Melbourne three days later (19, 21 and 24 September in the table). The Illawarra club preview quoted on P-575 says the club was 1–5 (1–1 at home) and scoring 99.7 points a game; the table lists exactly six Illawarra games before 11 October, one win, one home win and one home loss, totalling 598 points = 99.7 a game. Publishers can share an upstream, so "independent" means a different publisher, lineage unknown (SOURCES §1.1).

**What is not verified.** 19 games rest on ESPN alone, including the newest (Sydney 78–84 Adelaide on 11 October, for which a same-evening search found no second report). The official schedule denominator for 2026-27 could not be read (the NBL ladder and schedule pages render client-side), so completeness is argued, not proven. For the evidence available: club game counts of 4 to 7 add to 58 = 2 × 29; the Illawarra record and scoring average and the Phoenix coach's sequence above match the lists for those two clubs. That shows those clubs' lists are complete, not that every club's is. ESPN returned no event on 28 and 29 September or 5 and 6 October; no source was found that says whether the league played on those days. A postponed or rescheduled game would not appear. Do not treat the file as a complete season or as a replacement for a card's own source check.

**Use.** A card may cite the file only as `ARCHIVE_PARTIAL` with its last `Date` (2026-10-11) and must add later games from SOURCES. The file is a development snapshot, not a result of the pre-registered comparison.

## 5. Reading the retrospective's NBL finding again

The October 11 retrospective found NBL totals above the cards' expected totals on 3 of 3 cards (mean +16.8 points, interval −2.0 to +35.6) and recorded an NBL profile two seasons old. With 29 games the picture is smaller. The 2026-27 mean total is 187.4 (SD 20.4). That is +4.2 over the new active row (standard error 3.8, z 1.1), +6.3 over the retained prior (z 1.7), and +10.0 over the first 23 games of 2025-26 (rounds 1 to 4: 177.4; SE 5.2, z 1.9). None of the three reaches 2 standard errors, and the 25 games other than the four on the retrospective cohort's NBL cards averaged 184.1 against 207.8 for those four (P-560 234, P-565 203, P-566 184, P-575 210). The +16.8 should not be used as an offset (the v10 rule already says so). What the refreshed row does give is a documented, reproducible 2023-25 level (183.1) and a visible, unpooled 2026-27 level (187.4) to read beside it. Whether either predicts better is the FC10-PROFILE-v1 question.

## 6. Pending after this run

- **Not repaired:** the 2025 file's blank dates, its 14 mistyped post-season rows and its quarter errors (the sidecar and the guide record them; a repair needs the old value, new value and evidence per row under prompt 7 §2 and an owner decision on editing a published historical file).
- **Not done:** a 2026-27 schedule denominator; an NBL-owner source for the 19 single-source games; refreshes of other basketball rows (EuroLeague, Greek Basket League, NBA, WNBA windows were not recomputed).
- **Blocked by design inputs:** predictive acceptance of the refreshed profile (HYPOTHESIS_REGISTER, FC10-PROFILE-v1: no effect size, tolerance or sample plan yet).
