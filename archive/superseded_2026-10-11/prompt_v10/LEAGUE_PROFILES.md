# League profiles: scoring levels and shapes measured from the archive

**Version LP-2026.10.09-v1 (Markdown only).** These are the numbers a distribution starts from: the average score for each side, the spread of the margin and the total, how the two scores move together, and the shares of games that go to overtime, extra innings, a shootout or a one-run finish. They were measured on 2026-10-09 from the yearly CSVs in [Previous Sports Results](Previous%20Sports%20Results/README.md) (regular-season games only; the files used are listed under each table) and replace `runtime/config/leagues/*.json` and `runtime/config/sports/*.json`, removed that day (last copies at commit `37203fc2b`).

## How to use a profile

1. **Prior, not forecast.** A profile is the starting centre and spread for the league. The card then adjusts for the teams, lineups, venue, weather and rest, and lists each adjustment (CARD_AND_LOG_TEMPLATES, adjustments table).
2. **Name the row.** The card's `Archive check` and appendix A4 say which profile row supplied which number.
3. **Check the seasons.** Each row lists the seasons it covers. If the event is more than one season after the last season listed, recompute the row from the CSVs by hand (ARCHIVE_USE_GUIDE recipe R1) and say so.
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

| Sport | Scoring units | Largest score supported | Draw possible | Notes |
|---|---|---:|---|---|
| AFL / AFLW | points (goals, behinds) | 180 | yes | 6 points per goal, 1 per behind |
| Baseball | runs | 25 | no | 9 nominal innings; Statcast regimes pre-2008, 2008-2014, 2015+ |
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

- **KBO** extras: extra-innings share 0.1%; home win share 51.5%; margin excess kurtosis 0.630; one-run share 23.8%; park/environment sigma 0.044; team-run dispersion phi 0.290; tie share 2.1%.
  Built from: `Previous Sports Results/Baseball/KBO/2023/2023_games.csv`, `Previous Sports Results/Baseball/KBO/2024/2024_games.csv`, `Previous Sports Results/Baseball/KBO/2025/2025_games.csv`; stage regular.
- **MLB** extras: extra-innings share 8.7%; home win share 53.1%; margin excess kurtosis 0.932; one-run share 28.2%; park/environment sigma 0.073; team-run dispersion phi 0.288; tie share 0.0%.
  Built from: `Previous Sports Results/Baseball/MLB/2024/2024_games.csv`, `Previous Sports Results/Baseball/MLB/2025/2025_games.csv`, `Previous Sports Results/Baseball/MLB/2026/2026_games.csv`; stage regular.
  Extra-inning frame runs: 0 runs 43.0%, 1 29.4%, 2 13.0%, 3 7.3%, 4 3.6%, 5+ 3.7% (888 frames).
- **NPB** extras: extra-innings share 0.0%; home win share 54.2%; margin excess kurtosis 1.096; one-run share 33.7%; park/environment sigma 0.100; team-run dispersion phi 0.337; tie share 2.8%.
  Built from: `Previous Sports Results/Baseball/NPB/2023/2023_games.csv`, `Previous Sports Results/Baseball/NPB/2024/2024_games.csv`, `Previous Sports Results/Baseball/NPB/2025/2025_games.csv`; stage regular.

### Basketball

| League | Games | Seasons | Mean home | Mean away | Mean total | Margin SD | Total SD | Score corr. |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| EuroLeague | 992 | 2023-2025 | 85.84 | 82.35 | 168.19 | 12.47 | 17.94 | 0.349 |
| Greek Basket League | 420 | 2023-2025 | 83.33 | 79.57 | 162.90 | 15.91 | 18.25 | 0.136 |
| NBA | 3692 | 2023-2025 | 115.46 | 113.62 | 229.08 | 15.98 | 20.04 | 0.223 |
| NBL | 425 | 2022-2024 | 91.41 | 89.72 | 181.13 | 15.28 | 19.53 | 0.241 |
| WNBA | 769 | 2023-2025 | 82.83 | 81.15 | 163.99 | 14.13 | 17.29 | 0.199 |

- **EuroLeague** extras: margin excess kurtosis 0.504; regulation minutes 40.000.
  Built from: `Previous Sports Results/Basketball/EuroLeague/2023/2023_games.csv`, `Previous Sports Results/Basketball/EuroLeague/2024/2024_games.csv`, `Previous Sports Results/Basketball/EuroLeague/2025/2025_games.csv`; stage regular.
- **Greek Basket League** extras: margin excess kurtosis 0.111; regulation minutes 40.000.
  Built from: `Previous Sports Results/Basketball/Greek Basket League/2023/2023_games.csv`, `Previous Sports Results/Basketball/Greek Basket League/2024/2024_games.csv`, `Previous Sports Results/Basketball/Greek Basket League/2025/2025_games.csv`; stage regular.
- **NBA** extras: margin excess kurtosis 0.245; overtime share 4.7%; regulation minutes 48.000.
  Built from: `Previous Sports Results/Basketball/NBA/2023/2023_games.csv`, `Previous Sports Results/Basketball/NBA/2024/2024_games.csv`, `Previous Sports Results/Basketball/NBA/2025/2025_games.csv`; stage regular.
- **NBL** extras: margin excess kurtosis 0.308; overtime share 4.7%; regulation minutes 40.000.
  Built from: `Previous Sports Results/Basketball/NBL/2022/2022_games.csv`, `Previous Sports Results/Basketball/NBL/2023/2023_games.csv`, `Previous Sports Results/Basketball/NBL/2024/2024_games.csv`; stage regular.
- **WNBA** extras: margin excess kurtosis 0.132; overtime share 3.0%; regulation minutes 40.000.
  Built from: `Previous Sports Results/Basketball/WNBA/2023/2023_games.csv`, `Previous Sports Results/Basketball/WNBA/2024/2024_games.csv`, `Previous Sports Results/Basketball/WNBA/2025/2025_games.csv`; stage regular.

Excluded as implausible (do not use): Austria Basketball Bundesliga (home_advantage 9.210 outside plausible [-1.0, 5.0]; total_sd 8.412 outside plausible [10.0, 30.0]); BSL (home_advantage 9.210 outside plausible [-1.0, 5.0]; total_sd 8.412 outside plausible [10.0, 30.0]).

### Ice hockey

| League | Games | Seasons | Mean home | Mean away | Mean total | Margin SD | Total SD | Score corr. |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| NHL | 3936 | 2023-2025 | 3.21 | 2.98 | 6.19 | 2.61 | 2.31 | -0.123 |

- **NHL** extras: margin excess kurtosis -0.570; P(margin>=2) 60.1%; P(margin>=3) 40.3%; OT decided before shootout 68.0%; overtime share 22.1%; shootout home win share 52.2%; shootout share 7.1%.
  Built from: `Previous Sports Results/Ice Hockey/NHL/2023/2023_games.csv`, `Previous Sports Results/Ice Hockey/NHL/2024/2024_games.csv`, `Previous Sports Results/Ice Hockey/NHL/2025/2025_games.csv`; stage regular.

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
