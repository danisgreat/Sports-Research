# Using the Previous Sports Results archive

**v10 usage control (2026-10-11).** Inspect present files; the dated coverage counts below are historical snapshots. Count logical CSV records, retain zeros separately from missing values, verify season/stage/endpoint and expose sampled-versus-complete checks. A same-day result is usable only with evidence it was final and available before cutoff; a date alone is insufficient. Baselines use the frozen league-only recipe in SELECTION_RULES §9; historical TB-1/team-form recipes are distinct diagnostics. No data was refreshed by this document revision.

**Version ARC-2026.10.09-v1 (Markdown and CSV only).** Every card, settlement and retrospective consults the archive **whenever it holds rows that bear on the event**, and says what it found. This page tells you where the rows are, which columns to trust, how to avoid leakage, how to turn rows into the numbers a card needs, and what to write when nothing is available. It replaces the archive builders and the canonical export scripts that were removed on 2026-10-09 (last copies at commit `37203fc2b`).

The archive is a research aid. A row proves what was recorded about a past game. It does not prove forecasting skill, and an empty or header-only file is **missing data, not a finding**.

## 1. Where the rows are

```text
Previous Sports Results/<Sport>/<Competition>/<Year>/<Year>_games.csv
```

Examples: `Previous Sports Results/Baseball/MLB/2025/2025_games.csv`, `.../Basketball/NBA/2025/2025_games.csv`, `.../Ice Hockey/NHL/2025/2025_games.csv`, `.../AFL/AFL/2025/2025_games.csv`, `.../Rugby League/NRL/2025/2025_games.csv`, `.../American Football/NFL/2025/2025_games.csv`. The year is the season label used by that competition (a 2025-26 winter season sits under 2025). Players, coaches, officials and venue notes sit beside the CSVs in `COACHES.md`, `OFFICIATING.md`, `HISTORICAL_PLAYERS_AND_ROSTERS.md` and `VENUES_AND_LOCATIONS.md`; they vary in sourcing and are **not** pregame evidence unless you can show what was known at the time.

**Populated and header-only (checked 2026-10-09).** Files with data are concentrated in Basketball (383 files), American Football (239), Ice Hockey (153), AFL (152), State Level AFL (140), College Football (126), Baseball (105), Cricket one-day (102), Rugby League (51), Cricket Tests (51) and Cricket T20 (51). **Added 2026-10-12:** `Ice Hockey/Czech Extraliga` and `Soccer/Premier League`, 51 seasons each (1975-76 to 2025-26), rebuilt from observed source fields only. Read each folder's `DATA_PROVENANCE.md` before use, and see §8. **Tennis, Rugby Union, Field Hockey, Canadian Football and the other Soccer leagues' yearly files are header-only**; for those the archive gives you nothing, so use:

| Need | Where |
|---|---|
| English Premier League results | The yearly files `Previous Sports Results/Soccer/Premier League/<year>/<year>_games.csv` (1975-76 to 2025-26; half-time from 1995-96, corners/shots/referee from 2000-01; [provenance](Previous%20Sports%20Results/Soccer/Premier%20League/DATA_PROVENANCE.md)). Also `research/data/processed/league_csv/epl_results.csv`, and fixtures and results as text in `research/data/raw/openfootball/<season>.txt` (2020-21 to 2026-27). The 2026-27 season is **not** in the yearly files: add it from SOURCES §3.4 |
| NBL results | The yearly files `Previous Sports Results/Basketball/NBL/<year>/<year>_games.csv` (see §8: the 2025 file lacks dates on its regular-season rows and mistypes post-season games; the **2026 file is a partial snapshot** of 2026-27 to 2026-10-11 and must be refreshed before use). Dated results for 2021-22 to 2025-26 are also in `research/data/processed/league_csv/nbl_results.csv`; `research/data/nbl_results_wide.csv` and team box scores are in `research/data/nbl_box_team.csv` |
| The literal historical rank log (learning only) | `GAME_PREDICTION_RANK_LOG.csv` and `research/data/processed/legacy_learning/cards.csv`, `contracts.csv` |
| Tennis, soccer and rugby union rates | [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md) §6 and §7, then the source routes in [SOURCES.md](SOURCES.md) |

Before you trust any season, read the two coverage documents in the archive folder:

- [Coverage, blank years and why](Previous%20Sports%20Results/COVERAGE_AND_BLANK_YEARS.md): which years had no competition, which fields cannot be recovered for which eras, and the season-year convention.
- [Data source implementation guide](Previous%20Sports%20Results/DATA_SOURCES_IMPLEMENTATION.md): where each competition's games, players and officials come from.
- [Archive README](Previous%20Sports%20Results/README.md): the folder architecture and the 16 sport categories.

The large exports `Previous Sports Results/_canonical/events.csv`, `narratives.csv`, `provenance.csv` and `seasons.csv` hold one row per event with identity, scores, `quality_status`, `training_eligible` and `exclusion_reasons`. They are too large for GitHub and exist only on the maintainer's machine; the [canonical README](Previous%20Sports%20Results/_canonical/README.md) explains them. When you can open them, use only rows with `training_eligible = true` for base rates.

## 2. Columns that matter (read the header first)

Headers differ by sport. Always print the header row of the file you open and use the names exactly.

| Sport | Key columns |
|---|---|
| Baseball (MLB) | `Date`, `Start Time (UTC)`, `Season Phase`, `Game Type`, `Away Team`, `Home Team`, `Away Score`, `Home Score`, `Total Runs`, `Winning Margin`, `Innings Played`, `Extra Innings`, `Away/Home Line Score (runs by inning)`, `Away/Home Starting Pitcher`, `Doubleheader`, `Venue` |
| Baseball (KBO) | `Date`, `Start Time (KST)`, `Away Team`, `Home Team`, `Away Score`, `Home Score`, `Total Runs`, `Innings Played`, `Extra Innings`, `Game Status`, `Away/Home Line Score`, `Away/Home Starting Pitcher` |
| Basketball (NBA, WNBA, NBL, EuroLeague and others) | `Date`, `Home`, `Away`, `Home Score`, `Away Score`, `Total Points`, `Winning Margin`, `Overtime`, quarter or half scores where present, `Game Type (...)` |
| Ice hockey (NHL) | `Date`, `Home`, `Away`, `Home Score`, `Away Score`, `Total Goals`, `Decision Type`, `Overtime`, `Shootout`, `Game State` |
| AFL, AFLW | `Date`, `Home`, `Away`, `Game Score` (goals.behinds (points) text), `Total Points`, `Winning Margin`, `Venue` |
| Rugby league (NRL) | `Date`, `Home`, `Away`, `Home Score`, `Away Score`, halftime scores, tries, goals, field goals, `Extra Time / Golden Point` |
| American football (NFL) | `Date`, `Home`, `Away`, `Game Score` (text), `Total Points`, `Winning Margin`, `Game Type` |

**Never use as pregame evidence:** `Notable Players`, `A Succint one line game comment to summarise that game`, `Game Summary`, `Walk-Off Win` and any other prose or postgame field. They describe the result.

## 3. The point-in-time rule (no leakage)

1. Use only results known final and available before the card's explicit input cutoff. Exclude the forecast event and future games. For same-day rows require actual availability evidence; date-only records cannot establish this. If timestamps are absent, restrict to safely earlier dates and disclose the limitation.
2. A current-season file is a snapshot. Open it and read the **last `Date`**. If the last date is older than the games you need, say so and use [SOURCES.md](SOURCES.md) for the missing recent games.
3. Season-level profiles in [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md) were built from whole seasons. They are fine as priors for an upcoming event. Do not use them to "forecast" a game inside the same seasons after the fact.
4. A rule or environment change makes old rows unreliable. Compare season means before pooling years (BASE_RATES_REGISTER names examples: WNBA 2026 scored 10.7 points per game above 2024 and 2025; NRL six-again from 2020). Say which seasons you pooled and why.

## 4. Recipes: from rows to the numbers a card needs

Do these by reading the file and calculating by hand with [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md). Write the inputs and the result into the card's appendix (A3 and A4).

| Recipe | Steps | Used for |
|---|---|---|
| **R1 League level** | Take the league's row in [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md): mean home and away score, total SD, margin SD, score correlation, home-win share, extras (one-run share, overtime share, first-half share). If the league is missing or the profile is more than one season old, average `Home Score` and `Away Score` over the last three regular seasons in the files. | Centre and spread of the distribution |
| **R2 Team form: four windows, one rate** (PR-01, 2026-10-12) | See the steps below the table | Form-window table (template §3b), team rating, expected score |
| **R3 Season-to-date rating** | Build the standings from the file and apply the team-baseline arithmetic in PROBABILITY_TOOLKIT §4 (TB-1-MD). It is a comparator and a sanity check, not the distribution. | Baseline probability |
| **R4 Head-to-head** | Count the last meetings in the same competition and era with comparable personnel. Treat as light supporting evidence only; never the centre. | Matchup colour |
| **R5 Line frequency** | For the exact line you will price, count the share of the league's games that finished over or under it in the last three seasons. | Sanity check on a total or margin row |
| **R6 Rest and schedule** | From `Date` gaps: days since each team's last game, back-to-backs, travel. | Rest adjustments (list them as adjustments) |
| **R7 Venue and home edge** | Home-win share and mean margin at the venue and in the league. | Home advantage term |
| **R8 Extras and tails** | Overtime, shootout, extra-innings, one-run and big-margin shares from the profile. | Endpoint resolution inside the grid |

Small samples and noisy recent games: prior learning notes L-20260919-01/02 questioned last-game and bounce-back heuristics within their historical samples. Do not promote that into a universal impossibility claim, and do not invent a one-game adjustment without a supported model and sensitivity.

**Recipe R2 in full (form windows).**

1. **Rows.**
   - For each side, list its dated competitive games before the cutoff, newest first. Use the archive file or a SOURCES route: the ESPN team schedule `site.api.espn.com/apis/site/v2/sports/<sport>/<league>/teams/<id>/schedule`, MLB statsapi, StatMuse for US leagues, Tennis Abstract for players.
   - Exclude rows the archive flags as duplicate listings, awarded results, forfeits or abandonments, and say so.
   - An undated row cannot enter a window.
2. **Windows.** L5, L10, L15 and L20 (true n if fewer), season to date, and the league level from LEAGUE_PROFILES. For each, give scored, conceded and margin per game, plus the home/away split for L10 and L20. Print the table in template §3b.
3. **Season boundary.**
   - Previous-season games fill a window only when the current season has fewer games than the window. They are flagged.
   - Exclude them, and print the shorter n, when the side changed head coach, or when more than about 30% of its regular minutes or starts changed. Say which, with the source.
4. **Primary rate (equal weight, longer window).**
   - r = the L20 per-game mean, or season to date if longer and in the same regime.
   - Shrink it toward the league level: rate = (n × r + k × LM) ÷ (n + k). The constant k comes from PROBABILITY_TOOLKIT §4.3; use k = 2 where the league has none, and say so.
   - Do this separately for scored and conceded.
   - This is the rate that may enter the centre, as a listed adjustment.
   - Why equal weight over the longer window. This repository's historical out-of-sample checks ([RECENCY_AND_REBOUND.md](archive/historical_restored/RECENCY_AND_REBOUND.md) §4 and §7.2, one season each) found these RMSE changes for next-game team points against the league constant:

     | Window | NBA | WNBA | NBL | NHL | EPL |
     |---|---|---|---|---|---|
     | Last 1 | +35.7% | +28.2% | +18.0% | +39.9% | +37.6% |
     | Last 5 | +6.5% | +0.9% | −8.1% | +8.2% | +7.7% |
     | Last 10 | +1.9% | −1.7% | −10.4% | +3.4% | +2.2% |
     | Season to date | −1.1% | −4.2% | −7.7% | 0.0% | 0.0% |

     - Shorter windows were worse, monotonically, in the NBA, NHL and EPL, and the one-game window was the worst everywhere.
     - The NBL was the exception: last 10 beat season to date, consistent with scoring rising through its season.
     - In the NHL and EPL a half-way shrink to the league mean was the best simple predictor, so use a large k there.
     - For MLB starters' next-start earned runs: last 1 2.77, last 3 2.24, last 5 2.13, season 2.02, league 1.98 (L-20260919-04).
     - These are historical, single-season results. The comparison in step 5 tests them prospectively.
5. **Recency blend (printed as a comparison, not used for the pick).**
   - B = (L5 + L10 + L15 + L20) ÷ 4. This is a recency-weighted mean of the last 20 games, with weights per game of 0.1042 (games 1–5), 0.0542 (6–10), 0.0292 (11–15) and 0.0125 (16–20); its effective n is about 13.5.
   - Shrink it with the same k, using n = 13.5.
   - Print it beside the primary rate. Experiment FC11-FORM-v1 compares the two on settled games.
6. **Opponent context** (optional, recommended for basketball, where opponent defence improved RMSE by 7–11%):
   - For each game in the window, adjusted scored = scored − (opponent's conceded per game before that game − LM). Use the analogous formula for conceded.
   - Print the adjusted L20 mean beside the raw one.
   - If it is used, it is a listed adjustment, and the unadjusted pair is shown.
7. **Reading the windows.**
   - The windows overlap: they are one piece of evidence, counted once.
   - A gap between L5 and L20 is described, not traded on, unless a named, current mechanism explains it: an injury or return, a role or lineup change, a coach change, schedule density. There is no bounce-back or streak lean.
   - Disclose a short-window outlier as width, not as a centre shift.

## 5. The Archive check line

Every card has an `Archive check` bullet in its metadata. Allowed forms:

- `Previous Sports Results/Baseball/KBO/2025/2025_games.csv · 873 rows · last date 2025-10-01 · R1 league level, R2 form windows (L5/L10/L15/L20 each side, k = 20), R5 line frequency at 10.5 · KBO totals averaged 9.77 runs, 41% of games over 10.5`
- `ARCHIVE_PARTIAL: <file> holds games to <last date>; the missing weeks came from <SOURCES route>`
- `ARCHIVE_UNAVAILABLE: Soccer yearly files are header-only; used research/data/processed/league_csv/epl_results.csv instead` or `ARCHIVE_UNAVAILABLE: <exact reason>`

The line names the files opened, the number of rows read, the date range, the recipes used and the finding. Appendix A3 shows the numbers. A card whose Rank 1 depends on an archive-derived input (a league level, a form figure, a line frequency) must show that input.

## 6. Settlement and retrospective

- **Settlement.** If the season file already holds the game, compare its score with the official source. Agreement is a corroboration (say so in Basis). Disagreement is a source flag (R9): report both values, settle on the official source, and do not edit the archive.
- **Retrospective.** Compare each sport's realised rates in the cohort with its archive rates (home-win share, overtime share, one-run share, total SD). A cohort rate far from the archive rate is a finding about the cohort, not the archive.

## 7. Extending or repairing the archive

Use prompt 7 in [PROMPTS.md](PROMPTS.md). Keep each source's identity and date, never fill an unknown name or time, keep awards and narratives separate from game features, and say in the coverage document which seasons are inactive, future or unexplained. A header-only folder is never "complete".

## 8. Known data-quality notes (audit of 2026-10-11)

Found while carrying out the NBL profile refresh and the KBO/NPB extras audit ([run 2 folder](research/verification/framework_change_2026-10-11-2/IMPLEMENTATION.md)). No existing archive cell was changed. Each note says what to do instead.

| File(s) | Defect | Effect | What to do |
|---|---|---|---|
| `Basketball/NBL/2025/2025_games.csv` | `Date`, `Day of Week` and `Start Time (Local)` are blank on all 179 rows typed "Regular Season" | The recipe R2 (last 10 games before a date), R6 (rest) and the point-in-time rule cannot be applied to 2025-26 regular-season games from this file | **Repaired 2026-10-12 (R30):** all 179 rows now have `Date` and `Day of Week`. The 165 regular-season rows come from the run-2 sidecar (scheduled UTC start converted to the home club's local date); the 14 post-season rows come from ESPN event dates (evidence B; [evidence](research/verification/framework_change_2026-10-12-1/NBL_2025_26_POSTSEASON_DATE_EVIDENCE.csv)). `Start Time (Local)` stays blank: scheduled is not actual. Cell-level log: [NBL_2025_REPAIR_LOG.csv](research/verification/framework_change_2026-10-12-1/NBL_2025_REPAIR_LOG.csv). Venue is assumed to be the home club's city for the time-zone conversion |
| same file | 14 of the 179 "Regular Season" rows are post-season games (Round names CHAMPIONSHIP, ELIMINATION, IGNITE CUP FINAL, PLAYOFF 1, PLAYOFF 2, QUALIFIER, SEEDING, "SYD 2-1 ADL", "SYD WIN 3-2", "TIED 2-2") | A profile or base rate filtered on `Game Type` alone is contaminated by about 8% | **Repaired 2026-10-12 (R30):** `Game Type` set from the printed round label: SEEDING, QUALIFIER and ELIMINATION → Play-In (3); PLAYOFF 1/2 → Playoffs (5); CHAMPIONSHIP and the series rows → Finals (5); IGNITE CUP FINAL → Not applicable (1). `Game Type = Regular Season` now gives exactly 165 games, 33 per team. Round labels unchanged |
| `Basketball/NBL` yearly files | The quarter columns do not sum to the final score on some rows: 2025 has 3 of the 165 regular rows (game numbers 101, 186, 187; two are exactly double the final) and 3 of the 14 post-season rows; 2024 has 8 of 145; 2022 has 1 of 140; 2023 has none. The final scores themselves reconcile (2025: 165 of 165 against the processed file) | Quarter-level and half-level features from those rows are wrong; totals, margins and profiles are unaffected | Check that the quarters sum to the final before using them, and drop the row's quarter data if not |
| `Basketball/NBA/<2023, 2024, 2025>` and `Basketball/WNBA/<2023, 2024, 2025>` | One in-season cup final per file ("NBA In-Season Tournament Championship", "WNBA Commissioner's Cup Championship") is typed "Regular Season" | 3 of the NBA profile's 3,692 games and 3 of the WNBA profile's 769 are cup finals; the effect on means is negligible | Exclude them when a count must equal the schedule. Not corrected |
| `Baseball/KBO` and `Baseball/NPB` yearly files | `Innings Played` and `Extra Innings` hold placeholder defaults (9 / No); line scores are blank (NPB 0 rows, KBO 22 to 75 per season) | An extras or tie-after-extras share cannot be measured; LEAGUE_PROFILES withdrew its KBO 0.1% and NPB 0.0% | Treat extras as `NOT_ESTIMABLE` from the 2000–2024 files. Tie shares (equal final scores) are measured and usable. See [the audit](research/verification/framework_change_2026-10-11-2/KBO_NPB_EXTRAS_AUDIT.md). **2025 seasons repaired 2026-10-12 (R31).** See the next two rows |
| `Baseball/KBO/2025/2025_games.csv` | **Repaired 2026-10-12 (R31).** `Innings Played` and `Extra Innings` checked on all 779 completed games against KBO's own scoreboard service (evidence A): 777 agree and 0 final scores differ. Two values from a first MyKBO pass were wrong (10 innings for two 9-inning games) and are reverted. Stage labels also repaired: the five 22 March games (opening day) were typed Exhibition, and the Wild Card and Semi-Playoff labels were swapped | Regular season is now complete: 720 games, 144 per team. 2025 extras 59/720 (8.2%); ties 22 (3.1%), of which 19 came after extras and 3 were called ties at 9 innings | Use 2025 innings and extras. Line scores are still blank. Logs: [MyKBO pass](research/verification/framework_change_2026-10-12-1/KBO_2025_INNINGS_REPAIR_LOG.csv) then [owner correction](research/verification/framework_change_2026-10-12-1/KBO_2025_OWNER_CORRECTION_LOG.csv); [owner check, all games](research/verification/framework_change_2026-10-12-1/KBO_2025_OWNER_INNINGS_CHECK.csv). The postponed 2025-10-10 row's stage is derived from its series, not read |
| `Baseball/NPB/2025/2025_games.csv` | **Repaired 2026-10-12 (R31).** All 878 completed games read from each row's own npb.jp box score (evidence A). 109 innings values were wrong (all were 9 / No). Final scores agree 878/878. Two 11 October games typed Regular Season are Climax Series First Stage game 1 (npb.jp prints a new series counter) and are relabelled | Regular season is now 858 games, 143 per team. 2025 extras 101/858 (11.8%); ties 23 (2.7%), of which 21 came at the 12-inning cap and 2 were called short | Use 2025 innings and extras. Line scores are still blank in the file; the observed line scores are in the [owner check](research/verification/framework_change_2026-10-12-1/NPB_2025_OWNER_INNINGS_CHECK.csv). [Cell log](research/verification/framework_change_2026-10-12-1/NPB_2025_INNINGS_REPAIR_LOG.csv) |
| `Basketball/NBL/2026/2026_games.csv` (new) | A snapshot of 29 completed 2026-27 regular-season games to 2026-10-11, from the ESPN site API (evidence B); `Round / Stage`, venue, city, attendance, notable players and comment are blank because the source lacks them (blank = unknown) | Stale from the day after it was written | Read the last `Date`; add later games from [SOURCES.md](SOURCES.md) (§3.2) and say so in `Archive check`. A card may cite it only with `ARCHIVE_PARTIAL` and its last date. **Denominator checked 2026-10-12 (R30):** ESPN lists exactly 165 regular-season 2026-27 fixtures (10 teams × 33 ÷ 2); the 29 completed on 2026-10-12 equal this file's 29 rows, IDs and scores ([schedule](research/verification/framework_change_2026-10-12-1/NBL_2026_27_SCHEDULE_DENOMINATOR_ESPN.csv), evidence B). An NBL-owned score for the 19 single-source games is still DATA_PENDING: nbl.com.au loads scores client-side |
| `Ice Hockey/Czech Extraliga/<1975…2025>` (rebuilt 2026-10-12) | Single compiler (hockeyarchives.info); 1,843 play-off/relegation games undated (the source prints only a round's date list); 145 rows flagged, including a 2000-01 round that reprints round 1 (7 rows), awarded/forfeit games and 55 period-sum typos; club renames are separate keys | Form windows, rest and period features need the flags | Read [DATA_PROVENANCE.md](Previous%20Sports%20Results/Ice%20Hockey/Czech%20Extraliga/DATA_PROVENANCE.md) §4–5 before use; exclude the listed flags |
| `Soccer/Premier League/<1975…2025>` (rebuilt 2026-10-12) | 1975-76 to 1992-93 single-source (england.csv); 2022-23 and 2025-26 not cross-checked; HT score absent before 1995-96, statistics and referee before 2000-01; 2026-27 not included | Period and corner features exist only for the stated seasons | Read [DATA_PROVENANCE.md](Previous%20Sports%20Results/Soccer/Premier%20League/DATA_PROVENANCE.md); add the current season from SOURCES §3.4 |
| Four duplicate folder pairs (scan of 2026-10-12): `Basketball/BSL` = `Basketball/Austria Basketball Bundesliga`; `Ice Hockey/Metal Ligaen` = `Ice Hockey/Danish Metal Ligaen`; `Cricket One-Day Format/Men's ODI International` = `…/ODI International`; `American Football/College Football` = `College Football/NCAA Division I FBS` | Byte-identical across every season | Aggregating both counts each game twice | Use the canonical member (the second of each pair; [ACTIVE_FILE_INDEX](ACTIVE_FILE_INDEX.md)); each alias folder carries `ALIAS_OF_CANONICAL.md`. Rows not deleted (owner decision) |
| `Basketball/Austria Basketball Bundesliga` (and alias), `Basketball/Greek Basket League`, `Ice Hockey/Danish Metal Ligaen` (and alias) | One start time fills 63–68% of rows (17:30, 19:30, 15:00): the pattern of the fabricated builds quarantined on 2026-10-12; no builder survives in git to prove or clear it | Start-time and rest features may be defaults | `SUSPECTED_DEFAULT`: do not use `Start Time` from these folders until a prompt-7 check classifies it. Scores and dates are not implicated by this scan |
| `Basketball/NBA`, `Basketball/WNBA` | `Attendance` = 0 on 51% and 57% of rows | 0 likely means unknown (R26) | Treat `Attendance` 0 as missing unless a source confirms an empty venue (for example, the 2020 bubble games) |
| `Baseball/KBO`, `Baseball/NPB`; `College Football` (both folders) | KBO 18:30 (59%), NPB 18:00 (75%); 39% of college rows dated 1 January | Plausibly genuine (weekday night starts; New Year's bowls) | `SUSPECTED_DEFAULT` until checked; low risk |

## 9. Integrity rules for archive data (2026-10-12, audit R06, R26, R27, R28)

1. **One canonical path per competition.** A competition's yearly files live in exactly one `Previous Sports Results/<Sport>/<Competition>/` folder. Alias folders and root-level export folders holding copies are not allowed. Where two folder names exist for the same competition, one must say in its README that it is an alias, and must not carry rows. Aggregations count each event once, by its stable ID.
2. **Stable identities.** A game ID uses the native ID where one exists. Otherwise it uses a documented surrogate built from competition, date and teams (with a numbered suffix only where the source gives no date), never a row number. Inserting a missing older game must not change any existing ID.
3. **Observed, derived, missing, conflicting.** Every populated archive folder gets a `DATA_PROVENANCE.md` that classifies every column. A missing value is blank with its reason in the provenance file. It is never a default (no fixed start times, attendances, referee labels, mid-season dates, "half of the final score" or approximate rounds). A derived value is computed only from observed fields of the same row or season.
4. **Constant or default-looking values are a diagnostic, not a verdict.** Mark them `SUSPECTED_DEFAULT` until the field, the source and the season rules have been checked. A genuine measured zero (for example 0 red cards) or a legitimately constant field stays. A value proven to be a builder default (by reading the builder or the source) is removed. Keep the raw value in the quarantine record, and the interpretation separately.
5. **Endpoint-specific reconciliation.** State, per league and era, which equation should hold. For example: periods sum to the printed final, with the shootout goal included in the modern Czech format and excluded in the 1980s format. A row that breaks its equation is flagged and kept as printed. **Never repair a total by inventing a balancing field.** A row can stay usable for final-score work while being unusable for period work.
6. **Known-at versus event date.** The archive is a retrospective compilation; a row's date is when the game was played, not when the row became available. For a pregame card, use rows dated before the cutoff and say the archive capture date. For a replay or backtest, a corrected or late-published field (a re-dated postponement, a revised statistic) counts only from its correction date if that is known. Otherwise disclose the limit as `KNOWN_AT_UNVERIFIED`.
7. **Claims.** "Verified" in an archive or SOURCES text must name the fields, the coverage (full or sample, with n) and the checking source. Agreement between copies of the same file is replication, not corroboration.
