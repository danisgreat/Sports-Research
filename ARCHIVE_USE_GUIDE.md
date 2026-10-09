# Using the Previous Sports Results archive

**Version ARC-2026.10.09-v1 (Markdown and CSV only).** Every card, settlement and retrospective consults the archive **whenever it holds rows that bear on the event**, and says what it found. This page tells you where the rows are, which columns to trust, how to avoid leakage, how to turn rows into the numbers a card needs, and what to write when nothing is available. It replaces the archive builders and the canonical export scripts that were removed on 2026-10-09 (last copies at commit `37203fc2b`).

The archive is a research aid. A row proves what was recorded about a past game. It does not prove forecasting skill, and an empty or header-only file is **missing data, not a finding**.

## 1. Where the rows are

```text
Previous Sports Results/<Sport>/<Competition>/<Year>/<Year>_games.csv
```

Examples: `Previous Sports Results/Baseball/MLB/2025/2025_games.csv`, `.../Basketball/NBA/2025/2025_games.csv`, `.../Ice Hockey/NHL/2025/2025_games.csv`, `.../AFL/AFL/2025/2025_games.csv`, `.../Rugby League/NRL/2025/2025_games.csv`, `.../American Football/NFL/2025/2025_games.csv`. The year is the season label used by that competition (a 2025-26 winter season sits under 2025). Players, coaches, officials and venue notes sit beside the CSVs in `COACHES.md`, `OFFICIATING.md`, `HISTORICAL_PLAYERS_AND_ROSTERS.md` and `VENUES_AND_LOCATIONS.md`; they vary in sourcing and are **not** pregame evidence unless you can show what was known at the time.

**Populated and header-only (checked 2026-10-09).** Files with data are concentrated in Basketball (383 files), American Football (239), Ice Hockey (153), AFL (152), State Level AFL (140), College Football (126), Baseball (105), Cricket one-day (102), Rugby League (51), Cricket Tests (51) and Cricket T20 (51). **Soccer, Tennis, Rugby Union, Field Hockey and Canadian Football yearly files are header-only**; for those sports the archive gives you nothing, so use:

| Need | Where |
|---|---|
| English Premier League results | `research/data/processed/league_csv/epl_results.csv`; fixtures and results as text in `research/data/raw/openfootball/<season>.txt` (2020-21 to 2026-27) |
| NBL results | `research/data/processed/league_csv/nbl_results.csv`, `research/data/nbl_results_wide.csv` and team box scores in `research/data/nbl_box_team.csv` |
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

1. Use only rows with `Date` **strictly before** the research completion time of the card. Never use the event being forecast or anything after it.
2. A current-season file is a snapshot. Open it and read the **last `Date`**. If the last date is older than the games you need, say so and use [SOURCES.md](SOURCES.md) for the missing recent games.
3. Season-level profiles in [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md) were built from whole seasons. They are fine as priors for an upcoming event. Do not use them to "forecast" a game inside the same seasons after the fact.
4. A rule or environment change makes old rows unreliable. Compare season means before pooling years (BASE_RATES_REGISTER names examples: WNBA 2026 scored 10.7 points per game above 2024 and 2025; NRL six-again from 2020). Say which seasons you pooled and why.

## 4. Recipes: from rows to the numbers a card needs

Do these by reading the file and calculating by hand with [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md). Write the inputs and the result into the card's appendix (A3 and A4).

| Recipe | Steps | Used for |
|---|---|---|
| **R1 League level** | Take the league's row in [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md): mean home and away score, total SD, margin SD, score correlation, home-win share, extras (one-run share, overtime share, first-half share). If the league is missing or the profile is more than one season old, average `Home Score` and `Away Score` over the last three regular seasons in the files. | Centre and spread of the distribution |
| **R2 Team form** | List each team's last 10 regular-season games before the event date. Compute wins and losses, mean points for and against, and the home or away split. Shrink toward the league mean with the league's constant k in PROBABILITY_TOOLKIT §4.3: rating = (points + k × league mean) ÷ (games + k). Use k = 2 for a league not in that table and say so. | Team rating, expected score |
| **R3 Season-to-date rating** | Build the standings from the file and apply the team-baseline arithmetic in PROBABILITY_TOOLKIT §4 (TB-1-MD). It is a comparator and a sanity check, not the distribution. | Baseline probability |
| **R4 Head-to-head** | Count the last meetings in the same competition and era with comparable personnel. Treat as light supporting evidence only; never the centre. | Matchup colour |
| **R5 Line frequency** | For the exact line you will price, count the share of the league's games that finished over or under it in the last three seasons. | Sanity check on a total or margin row |
| **R6 Rest and schedule** | From `Date` gaps: days since each team's last game, back-to-backs, travel. | Rest adjustments (list them as adjustments) |
| **R7 Venue and home edge** | Home-win share and mean margin at the venue and in the league. | Home advantage term |
| **R8 Extras and tails** | Overtime, shootout, extra-innings, one-run and big-margin shares from the profile. | Endpoint resolution inside the grid |

Small samples and noisy recent games: the last game is the worst predictor, and no bounce-back effect exists in MLB (L-20260919-01 and L-20260919-02 in [LEARNING_REGISTER.md](LEARNING_REGISTER.md)). Do not move a rating on one game.

## 5. The Archive check line

Every card has an `Archive check` bullet in its metadata. Allowed forms:

- `Previous Sports Results/Baseball/KBO/2025/2025_games.csv · 873 rows · last date 2025-10-01 · R1 league level, R2 form (last 10 each), R5 line frequency at 10.5 · KBO totals averaged 9.77 runs, 41% of games over 10.5`
- `ARCHIVE_PARTIAL: <file> holds games to <last date>; the missing weeks came from <SOURCES route>`
- `ARCHIVE_UNAVAILABLE: Soccer yearly files are header-only; used research/data/processed/league_csv/epl_results.csv instead` or `ARCHIVE_UNAVAILABLE: <exact reason>`

The line names the files opened, the number of rows read, the date range, the recipes used and the finding. Appendix A3 shows the numbers. A card whose Rank 1 depends on an archive-derived input (a league level, a form figure, a line frequency) must show that input.

## 6. Settlement and retrospective

- **Settlement.** If the season file already holds the game, compare its score with the official source. Agreement is a corroboration (say so in Basis). Disagreement is a source flag (R9): report both values, settle on the official source, and do not edit the archive.
- **Retrospective.** Compare each sport's realised rates in the cohort with its archive rates (home-win share, overtime share, one-run share, total SD). A cohort rate far from the archive rate is a finding about the cohort, not the archive.

## 7. Extending or repairing the archive

Use prompt 7 in [PROMPTS.md](PROMPTS.md). Keep each source's identity and date, never fill an unknown name or time, keep awards and narratives separate from game features, and say in the coverage document which seasons are inactive, future or unexplained. A header-only folder is never "complete".
