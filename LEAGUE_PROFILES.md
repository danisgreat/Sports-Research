# League profiles: scoring levels and shapes measured from the archive

**v10 freshness/baseline control (2026-10-11).** Existing numeric rows below are retained, not recomputed in this release. A profile older than one season is STALE_PROFILE; inspect actual current coverage before replacing it. If sufficient verified data is unavailable, retain explicit stale-prior sensitivity or qualitative research. No universal shift is inferred from a few forecast residuals. Baseline recipes follow [SELECTION_RULES §9](SELECTION_RULES.md#9-frozen-league-only-baseline-ret-02); mean/SD alone may not support discrete, phase or extras probabilities. Draw/innings/OT conditions must be verified for the actual competition/season; generic sport rows below never override them. The NBL refresh and the KBO/NPB extras audit were carried out on 2026-10-11 (version below).

**Version LP-2026.10.12-v3 (2026-10-12, framework change 2026-10-12-1, audit R13/R32).** Additive only; no existing numeric row changed.
1. The **Czech Extraliga** row was added from the rebuilt archive (see Ice hockey). Read its DATA_PROVENANCE first.
2. A **freshness table** (below) gives every row an as-of date, window, source, coverage and permitted endpoints, plus a status:
   - `CURRENT`: the window includes the latest completed season.
   - `LAG_1`: one completed season is missing. Usable as a disclosed prior; check current coverage.
   - `STALE_PROFILE`: two or more seasons are missing. Prompt-1 sensitivity is required.
3. The sport-constants table now labels per-team score limits as computational support limits, and draws as competition-specific (R13).

A refreshed or added row is a data update, not demonstrated predictive improvement.

### Freshness table (2026-10-12)

"Latest completed season" is judged on 2026-10-12. The permitted endpoints are those the row's own measurements support. Anything else (period, extras, corners) needs its own supported source or stays `NOT_ESTIMABLE`.

| League | Window (n) | As-of version | Source | Latest completed season | Status | Permitted endpoints | Notes |
|---|---|---|---|---|---|---|---|
| KBO | 2023–2025 (2,182) | LP-2026.10.09-v1 | archive yearly files | 2026 | LAG_1 | full-game runs, totals, margins, winner, tie share | Window extras share still NOT_ESTIMABLE (2023–2024 not recovered). 2025 alone, owner-checked: extras 8.2% (59/720), ties 3.1%. See ARCHIVE_USE_GUIDE §8 (R31) and the note under Baseball |
| MLB | 2024–2026 (7,288) | LP-2026.10.09-v1 | archive | 2026 | CURRENT | full-game, extras share | — |
| NPB | 2023–2025 (2,576) | LP-2026.10.09-v1 | archive | 2026 | LAG_1 | as KBO | Window extras share NOT_ESTIMABLE. 2025 alone, owner-checked: extras 11.8% (101/858), ties 2.7% (ARCHIVE_USE_GUIDE §8, R31) |
| EuroLeague | 2023–2025 (992) | LP-2026.10.09-v1 | archive | 2025-26 | CURRENT | full-game | — |
| Greek Basket League | 2023–2025 (420) | LP-2026.10.09-v1 | archive | 2025-26 | CURRENT | full-game | Archive start times SUSPECTED_DEFAULT (ARCHIVE_USE_GUIDE §8); scores not implicated |
| NBA | 2023–2025 (3,692) | LP-2026.10.09-v1 | archive | 2025-26 | CURRENT | full-game, OT share | Attendance zero-as-missing; not used here |
| NBL | 2023–2025 (450) | LP-2026.10.11-v2 | archive (2025 dates and stages repaired 2026-10-12; the row's scores are unchanged) | 2025-26 | CURRENT | full-game, OT share, home win | Prior row LP-2026.10.09-v1 retained |
| WNBA | 2023–2025 (769) | LP-2026.10.09-v1 | archive | 2026 | LAG_1 | full-game, OT share | BASE_RATES_REGISTER notes WNBA 2026 scoring +10.7 over 2024–25: use the regime note |
| NHL | 2023–2025 (3,936) | LP-2026.10.09-v1 | archive | 2025-26 | CURRENT | full-game incl. OT/SO, margins | — |
| **Czech Extraliga** | 2023–2025 (1,092) | **LP-2026.10.12-v3** | rebuilt archive (single compiler) | 2025-26 | CURRENT | full-game incl. OT/SO, margins | New row; see Ice hockey |
| AFL | 2023–2025 (621) | LP-2026.10.09-v1 | archive | 2026 | LAG_1 | full-game | — |
| AFLW | 2022, 2025 (270) | LP-2026.10.09-v1 | archive (files 2022 and 2025 only) | 2025 (2026 in progress) | CURRENT with gap | full-game | Window omits 2023–2024; coverage disclosed |
| NRL | 2023–2025 (612) | LP-2026.10.09-v1 | archive | 2026 | LAG_1 | full-game | — |
| NFL | 2023–2025 (816) | LP-2026.10.09-v1 | archive | 2025 | CURRENT | full-game, key margins | — |
| EPL | 2023–2025 (1,140) | LP-2026.10.09-v1 | `research/data/processed/league_csv/epl_results.csv` | 2025-26 | CURRENT | full-game goals; corners and first-half from BASE_RATES §7.3 (2025-26) | Rebuilt archive (2026-10-12) now holds HT from 1995-96 and corners from 2000-01: a candidate refresh source for a future version |

**Version LP-2026.10.11-v2 (2026-10-11, run 2 of the October 11 framework change).** Two changes since LP-2026.10.09-v1; every other row is unchanged and was not re-audited.
1. **NBL row refreshed** to the 2023–2025 window (n = 450). The previous row (2022–2024, n = 425) is retained below as the frozen comparator `LP-2026.10.09-v1`. A card issued before this version keeps the row it cited. The window comparison, the 2025-26 schedule reconciliation, the 2026-27 year-to-date check and the data defects found are in [NBL_PROFILE_AUDIT.md](research/verification/framework_change_2026-10-11-2/NBL_PROFILE_AUDIT.md).
2. **KBO and NPB "extra-innings share" withdrawn** (was 0.1% and 0.0%). Those figures came from `Extra Innings` and `Innings Played` columns that hold placeholder defaults, not measurements; the share is `NOT_ESTIMABLE` from the yearly files. Evidence: [KBO_NPB_EXTRAS_AUDIT.md](research/verification/framework_change_2026-10-11-2/KBO_NPB_EXTRAS_AUDIT.md).

A refreshed profile is a data update, not demonstrated predictive improvement; the paired prospective comparison (FC10-PROFILE-v1) has not started.

**Version LP-2026.10.09-v1 (Markdown only).** These are the numbers a distribution starts from: the average score for each side, the spread of the margin and the total, how the two scores move together, and the shares of games that go to overtime, extra innings, a shootout or a one-run finish. They were measured on 2026-10-09 from the yearly CSVs in [Previous Sports Results](Previous%20Sports%20Results/README.md) (regular-season games only; the files used are listed under each table) and replace `runtime/config/leagues/*.json` and `runtime/config/sports/*.json`, removed that day (last copies at commit `37203fc2b`).

## How to use a profile

1. **Prior, not forecast.** A profile is the starting centre and spread for the league. The card then adjusts for the teams, lineups, venue, weather and rest, and lists each adjustment (CARD_AND_LOG_TEMPLATES, adjustments table).
2. **Name the row.** The card's `Archive check` and appendix A4 say which profile row supplied which number.
3. **Check the seasons.** If a profile is more than one season stale, inspect vetted new-season rows and propose a documented refresh under prompt 7. Print the old and supported current level or DATA_PENDING; never invent a current profile when the archive is incomplete. A later refresh cannot alter an earlier card's baseline.
4. **Leagues not listed** have no profile. Use the archive recipes in [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md) and state that the numbers are your own.
5. **Do not use an excluded league's numbers.** The rows listed as implausible failed the plausibility check (home advantage or total SD outside a sensible range), usually because the archive for that league is incomplete or wrongly scraped.

## Reading the columns

- **Mean home / Mean away:** average score per team-game in the sport's own units (runs, goals, points).
- **Margin SD / Total SD:** standard deviation of (home minus away) and of (home plus away).
- **Score corr.:** correlation between the two teams' scores in a game. Negative means a points-trading game is rarer than a one-sided one (AFL, NRL, NHL). Positive means both teams score more or less together (basketball, EuroLeague).
- **Dispersion phi:** negative-binomial overdispersion. The variance of a team's count is mean + phi × mean².
- **Park/environment sigma:** the standard deviation (log scale) of a game-level environment factor shared by both teams. It is what makes both baseball teams score high or low together.
- **Margin excess kurtosis:** tail weight of the margin compared with a normal curve. Above 0 means fatter tails.

## Sport constants

**Read these two columns carefully (R13, 2026-10-12).**
- **Computational support limit** is the largest per-team score a hand grid or table is expected to carry. It is not a physical limit. Any mass beyond it must be assigned explicitly (a tail bucket, or renormalisation stated on the card).
- **Draw possible** is the sport's general case. The exact competition, season and stage decide, and the frozen contract decides how a tie settles (moneyline void/push, three-way, or loss). A generic row never overrides them.

| Sport | Scoring units | Computational support limit (per team) | Draw possible | Notes |
|---|---|---:|---|---|
| AFL / AFLW | points (goals, behinds) | 180 | yes | 6 points per goal, 1 per behind |
| Baseball | runs | 25 | competition-specific: MLB no (extras to a result); KBO, NPB and CPBL regular-season games can end tied after the innings cap | 9 nominal innings; Statcast regimes pre-2008, 2008-2014, 2015+ |
| Basketball | points | 180 | no | about 100 possessions and 1.14 points per possession nominal |
| Cricket | runs | 700 | yes | phases powerplay, middle, death; formats Test, ODI, T20 |
| American football | points | 65 | yes | about 11 drives per team; key margins 3, 6, 7, 10, 14, 17, 20, 21 |
| Ice hockey (NHL) | goals | 14 | regulation only | empty-net rate 22% in one-goal games; puck line 1.5 |
| Rugby league (NRL) | points (tries, conversions, penalty_goals, field_goals) | 70 | yes | try 4, conversion 2, penalty goal 2, field goal 1; key margins 2, 4, 6, 8, 10, 12, 14, 16 |
| Soccer | goals | 12 | yes | derivatives: corners, cards, half-time, both teams to score |
| Tennis | games | 75 | no | formats best-of-3 and best-of-5; surfaces hard, clay, grass, carpet |

## Profiles by sport

### Baseball

| League | Games | Seasons | Mean home | Mean away | Mean total | Margin SD | Total SD | Score corr. |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| KBO | 2182 | 2023-2025 | 4.88 | 4.89 | 9.77 | 4.79 | 4.93 | 0.028 |
| MLB | 7288 | 2024-2026 | 4.46 | 4.42 | 8.88 | 4.52 | 4.47 | -0.011 |
| NPB | 2576 | 2023-2025 | 3.41 | 3.29 | 6.71 | 3.76 | 3.80 | 0.011 |

- **KBO** extras: extra-innings share NOT_ESTIMABLE (the 0.1% in LP-2026.10.09-v1 was a placeholder artefact; see the correction note below); home win share 51.5%; margin excess kurtosis 0.630; one-run share 23.8%; park/environment sigma 0.044; team-run dispersion phi 0.290; tie share 2.1%.
  Built from: `Previous Sports Results/Baseball/KBO/2023/2023_games.csv`, `Previous Sports Results/Baseball/KBO/2024/2024_games.csv`, `Previous Sports Results/Baseball/KBO/2025/2025_games.csv`; stage regular.
- **MLB** extras: extra-innings share 8.7%; home win share 53.1%; margin excess kurtosis 0.932; one-run share 28.2%; park/environment sigma 0.073; team-run dispersion phi 0.288; tie share 0.0%.
  Built from: `Previous Sports Results/Baseball/MLB/2024/2024_games.csv`, `Previous Sports Results/Baseball/MLB/2025/2025_games.csv`, `Previous Sports Results/Baseball/MLB/2026/2026_games.csv`; stage regular.
  Extra-inning frame runs: 0 runs 43.0%, 1 29.4%, 2 13.0%, 3 7.3%, 4 3.6%, 5+ 3.7% (888 frames).
- **NPB** extras: extra-innings share NOT_ESTIMABLE (the 0.0% in LP-2026.10.09-v1 was a placeholder artefact; see the correction note below); home win share 54.2%; margin excess kurtosis 1.096; one-run share 33.7%; park/environment sigma 0.100; team-run dispersion phi 0.337; tie share 2.8%.
  Built from: `Previous Sports Results/Baseball/NPB/2023/2023_games.csv`, `Previous Sports Results/Baseball/NPB/2024/2024_games.csv`, `Previous Sports Results/Baseball/NPB/2025/2025_games.csv`; stage regular.

**Correction note, KBO and NPB extras (2026-10-11).** Both rows reproduce exactly from the files (KBO n 2,182, NPB n 2,576, every mean, SD, correlation and tie count), so the means, spreads, ties, one-run and home-win figures stand. The extra-innings share does not. In the yearly files no NPB final of 2023–2025 has `Innings Played` above 9 or `Extra Innings` marked yes (0 of 2,637; every 2025 row reads 9 and "No", including its 28 cancelled games), and only 3 of 2,370 KBO finals do (`Innings Played` is 9 on 778 of 779 KBO 2025 finals). Yet 46 KBO and 72 NPB regular-season games ended tied (2.1% and 2.8%), and a game tied after nine innings goes to extras. The line-score columns that would settle it are blank (NPB 0 rows; KBO 22 to 75 rows per season). So:
- Do not use 0.1% or 0.0%. Do not use the MLB 8.7% for KBO or NPB either.
- A card that needs an extras or tie-after-extras mass states it as its own estimate with the basis, or flags `NOT_ESTIMABLE`. The tie share above is measured (equal final scores) and may be cited as such.
- A baseline that depends on extras (a three-way KBO/NPB winner, a full-game total with extras) stays `BASELINE_UNAVAILABLE` until innings are recovered from an official box-score source under prompt 7.

**Recovery note, 2025 seasons (2026-10-12, audit R31).** The 2025 KBO and NPB files now hold owner-checked innings for every completed game: KBO's scoreboard service and each game's npb.jp box score (ARCHIVE_USE_GUIDE §8). This adds measurements; the numeric rows above are not recomputed and keep their versions.
- **Measured 2025 regular season, single season:** KBO extras 8.2% (59 of 720) and ties 3.1% (22). NPB extras 11.8% (101 of 858) and ties 2.7% (23).
- **Ties by how they ended:** KBO 19 after extras and 3 called at 9 innings. NPB 21 at the 12-inning cap and 2 called short.
- **Citing these:** a card may cite them as a one-season 2025 measurement with n. They are not a 2023–2025 window value. The window extras share stays `NOT_ESTIMABLE` until 2023–2024 are recovered the same way.
- **Stage labels were repaired in 2025:** KBO gains 5 regular-season games (opening day, typed Exhibition) and NPB loses 2 (Climax Series First Stage games typed Regular Season). So the frozen rows above (KBO n 2,182, NPB n 2,576) no longer reproduce exactly from the repaired files. They remain the cited LP-2026.10.09-v1 values; a refresh is a new version.

### Basketball

| League | Games | Seasons | Mean home | Mean away | Mean total | Margin SD | Total SD | Score corr. |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| EuroLeague | 992 | 2023-2025 | 85.84 | 82.35 | 168.19 | 12.47 | 17.94 | 0.349 |
| Greek Basket League | 420 | 2023-2025 | 83.33 | 79.57 | 162.90 | 15.91 | 18.25 | 0.136 |
| NBA | 3692 | 2023-2025 | 115.46 | 113.62 | 229.08 | 15.98 | 20.04 | 0.223 |
| NBL | 450 | 2023-2025 | 92.35 | 90.79 | 183.14 | 16.34 | 19.26 | 0.163 |
| WNBA | 769 | 2023-2025 | 82.83 | 81.15 | 163.99 | 14.13 | 17.29 | 0.199 |

- **EuroLeague** extras: margin excess kurtosis 0.504; regulation minutes 40.000.
  Built from: `Previous Sports Results/Basketball/EuroLeague/2023/2023_games.csv`, `Previous Sports Results/Basketball/EuroLeague/2024/2024_games.csv`, `Previous Sports Results/Basketball/EuroLeague/2025/2025_games.csv`; stage regular.
- **Greek Basket League** extras: margin excess kurtosis 0.111; regulation minutes 40.000.
  Built from: `Previous Sports Results/Basketball/Greek Basket League/2023/2023_games.csv`, `Previous Sports Results/Basketball/Greek Basket League/2024/2024_games.csv`, `Previous Sports Results/Basketball/Greek Basket League/2025/2025_games.csv`; stage regular.
- **NBA** extras: margin excess kurtosis 0.245; overtime share 4.7%; regulation minutes 48.000.
  Built from: `Previous Sports Results/Basketball/NBA/2023/2023_games.csv`, `Previous Sports Results/Basketball/NBA/2024/2024_games.csv`, `Previous Sports Results/Basketball/NBA/2025/2025_games.csv`; stage regular.
- **NBL** (LP-2026.10.11-v2, effective for cards issued from 2026-10-11) extras: margin excess kurtosis 0.156; overtime share 4.0%; home win share 54.7%; regulation minutes 40.000.
  Built from: `Previous Sports Results/Basketball/NBL/2023/2023_games.csv`, `Previous Sports Results/Basketball/NBL/2024/2024_games.csv`, `Previous Sports Results/Basketball/NBL/2025/2025_games.csv`; stage regular, defined as `Game Type` = Regular Season **and** `Round / Stage` = "Round 1" to "Round 22" in the 2025 file (165 games = 33 per team, reconciled; 14 post-season rows typed "Regular Season" are excluded).
  **Retained prior, `LP-2026.10.09-v1`** (use only as the stated comparator or by a card that cited it): 2022-2024 (files 2022–2024), n 425, mean home 91.41, away 89.72, total 181.13, margin SD 15.28, total SD 19.53, corr 0.241, kurtosis 0.308, overtime 4.7%, home win 55.8%.
  **Window comparison** (same definition and method; the method reproduces the retained row exactly):

  | Window | Games | Mean home | Mean away | Mean total | Margin SD | Total SD | Corr | Kurt | OT | Home win |
  |---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
  | 2022-23 | 140 | 88.59 | 87.70 | 176.29 | 15.35 | 18.96 | 0.212 | 0.224 | 7.9% | 52.9% |
  | 2023-24 | 140 | 92.01 | 89.21 | 181.23 | 14.61 | 17.68 | 0.189 | 1.039 | 3.6% | 59.3% |
  | 2024-25 | 145 | 93.54 | 92.16 | 185.70 | 15.88 | 20.74 | 0.261 | -0.089 | 2.8% | 55.2% |
  | 2025-26 | 165 | 91.58 | 90.92 | 182.50 | 18.06 | 19.06 | 0.054 | -0.183 | 5.5% | 50.3% |
  | **2023-25 (active row)** | 450 | 92.35 | 90.79 | 183.14 | 16.34 | 19.26 | 0.163 | 0.156 | 4.0% | 54.7% |
  | 2022-24 (retained prior) | 425 | 91.41 | 89.72 | 181.13 | 15.28 | 19.53 | 0.241 | 0.308 | 4.7% | 55.8% |
  | 2026-27 to 11 Oct (in progress, **not pooled**) | 29 | 95.07 | 92.31 | 187.38 | 13.23 | 20.38 | 0.411 | -0.789 | 3.4% | 62.1% |

  Season means of the total differ by up to 9.4 points (2022-23 against 2024-25, about 4 standard errors), so the pooled spreads contain between-season variation; dropping 2022-23 removes the lowest-scoring season. The 2025-26 margin SD (18.06) is the highest of the four seasons and agrees with BASE_RATES_REGISTER §7.1 (raw 18.1). The 2026-27 games are early-season (rounds 1 to 4; every team has played 4 to 7), come from a different source (ESPN site API, evidence B) and are shown for comparison only: their mean total is +4.2 over the active row (standard error 3.8, z 1.1) and +6.3 over the retained prior (z 1.7), so no 2026-27 shift is established. The 3-game excess on the retrospective's NBL cards (+16.8) does not generalise: the four NBL games on cards P-560, P-565, P-566 and P-575 averaged 207.8 and the other 25 games averaged 184.1.
- **WNBA** extras: margin excess kurtosis 0.132; overtime share 3.0%; regulation minutes 40.000.
  Built from: `Previous Sports Results/Basketball/WNBA/2023/2023_games.csv`, `Previous Sports Results/Basketball/WNBA/2024/2024_games.csv`, `Previous Sports Results/Basketball/WNBA/2025/2025_games.csv`; stage regular.

Excluded as implausible (do not use): Austria Basketball Bundesliga (home_advantage 9.210 outside plausible [-1.0, 5.0]; total_sd 8.412 outside plausible [10.0, 30.0]); BSL (home_advantage 9.210 outside plausible [-1.0, 5.0]; total_sd 8.412 outside plausible [10.0, 30.0]).

### Ice hockey

| League | Games | Seasons | Mean home | Mean away | Mean total | Margin SD | Total SD | Score corr. |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| NHL | 3936 | 2023-2025 | 3.21 | 2.98 | 6.19 | 2.61 | 2.31 | -0.123 |
| Czech Extraliga | 1092 | 2023-2025 | 2.95 | 2.48 | 5.43 | 2.46 | 2.19 | -0.118 |

- **NHL** extras: margin excess kurtosis -0.570; P(margin>=2) 60.1%; P(margin>=3) 40.3%; OT decided before shootout 68.0%; overtime share 22.1%; shootout home win share 52.2%; shootout share 7.1%.
  Built from: `Previous Sports Results/Ice Hockey/NHL/2023/2023_games.csv`, `Previous Sports Results/Ice Hockey/NHL/2024/2024_games.csv`, `Previous Sports Results/Ice Hockey/NHL/2025/2025_games.csv`; stage regular.

- **Czech Extraliga** (LP-2026.10.12-v3, effective for cards issued from 2026-10-12):
  - Extras: overtime share 22.3%; shootout share 9.2%; home win share 57.8%; P(margin ≥ 2) 55.9%; P(margin ≥ 3) 34.4%; 0 draws (overtime and shootouts decide every regular-season game in these seasons).
  - Final scores are as printed, with the deciding shootout goal included (DATA_PROVENANCE §2). SDs and correlation are sample statistics (n − 1).
  - Built from: `Previous Sports Results/Ice Hockey/Czech Extraliga/2023/2023_games.csv`, `…/2024/2024_games.csv`, `…/2025/2025_games.csv`; regular season only (364 games per season). Excluded: rows flagged POSSIBLE_DUPLICATE, AWARDED_RESULT, FORFEIT_NOT_PLAYED or ABANDONED (0 in this window).
  - Single compiler (hockeyarchives.info); the 2023-24 sample check agreed 8/8. [Provenance](Previous%20Sports%20Results/Ice%20Hockey/Czech%20Extraliga/DATA_PROVENANCE.md).

Excluded as implausible (do not use): Metal Ligaen (home_advantage 1.229 outside plausible [-0.3, 0.6]).

### Australian rules

| League | Games | Seasons | Mean home | Mean away | Mean total | Margin SD | Total SD | Score corr. |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| AFL | 621 | 2023-2025 | 87.73 | 80.50 | 168.23 | 41.08 | 29.30 | -0.328 |
| AFLW | 270 | 2022-2025 | 37.13 | 35.07 | 72.20 | 32.89 | 23.61 | -0.320 |

- **AFL** extras: goal conversion 53.2%; margin excess kurtosis 0.377; scoring-shot dispersion phi 0.019; scoring shots per team 22.982.
  Built from: `Previous Sports Results/AFL/AFL/2023/2023_games.csv`, `Previous Sports Results/AFL/AFL/2024/2024_games.csv`, `Previous Sports Results/AFL/AFL/2025/2025_games.csv`; stage regular.
- **AFLW** extras: goal conversion 46.0%; margin excess kurtosis 0.224; scoring-shot dispersion phi 0.152; scoring shots per team 10.941.
  Built from: `Previous Sports Results/AFL/AFLW/2022/2022_games.csv`, `Previous Sports Results/AFL/AFLW/2025/2025_games.csv`; stage regular.

### Rugby league

| League | Games | Seasons | Mean home | Mean away | Mean total | Margin SD | Total SD | Score corr. |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| NRL | 612 | 2023-2025 | 24.56 | 21.68 | 46.24 | 19.06 | 13.63 | -0.323 |

- **NRL** extras: conversion rate 86.2%; first-half points share 49.2%; margin excess kurtosis 0.481; tries per team 4.025.
  Built from: `Previous Sports Results/Rugby League/NRL/2023/2023_games.csv`, `Previous Sports Results/Rugby League/NRL/2024/2024_games.csv`, `Previous Sports Results/Rugby League/NRL/2025/2025_games.csv`; stage regular.

### American football

| League | Games | Seasons | Mean home | Mean away | Mean total | Margin SD | Total SD | Score corr. |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| NFL | 816 | 2023-2025 | 23.67 | 21.46 | 45.13 | 14.34 | 13.57 | -0.055 |

- **NFL** extras: margin excess kurtosis 0.112.
  Built from: `Previous Sports Results/American Football/NFL/2023/2023_games.csv`, `Previous Sports Results/American Football/NFL/2024/2024_games.csv`, `Previous Sports Results/American Football/NFL/2025/2025_games.csv`; stage regular.

### Soccer

| League | Games | Seasons | Mean home | Mean away | Mean total | Margin SD | Total SD | Score corr. |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| EPL | 1140 | 2023-2025 | 1.61 | 1.37 | 2.99 | 1.86 | 1.63 | -0.132 |

- **EPL** extras: corners per match 10.000; corners SD 3.270; corners per team 5.000; team corners SD 2.770; draw share 24.5%; first-half goal share 43.3%; first-half goals per match 1.190; margin excess kurtosis 0.596; P(first-half goal) 71.6%.
  Built from: `research/data/processed/league_csv/epl_results.csv`; reference extras from BASE_RATES_REGISTER.md section 7.3 (EPL 2025-26, n = 380, scoreboard plus match summaries); stage regular.

### NFL absolute-margin distribution (2015-2025, 2,895 games)

| Margin | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 20 | 21 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| P(abs margin) | 0.3% | 4.6% | 4.6% | 14.6% | 4.7% | 4.4% | 6.9% | 8.7% | 4.3% | 1.7% | 4.9% | 2.1% | 1.8% | 2.0% | 5.1% | 1.7% | 2.3% | 3.5% | 2.2% | 2.0% | 2.2% |

A margin of exactly 3 carries 14.6% of games and exactly 7 carries 8.7%, together 23.3%. Use these masses, not a smoothed normal, near key numbers.

## Sources and limits

The soccer row reuses the 2025-26 reference extras in BASE_RATES_REGISTER §7.3; the corner figures are from match summaries, not from the yearly files (which are header-only for soccer). Profiles describe regular-season games. Knockout and finals games run lower-scoring (see the regime table in [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md)). A profile never replaces the confirmed lineups, starters, goalies and weather for the event itself.
