# Shadow lane for every other sport (`C-SPORT-SHADOW`, opened 2026-09-26)

**Status: CODE IMPLEMENTED AND TESTED; VALIDATED ONLY WHERE PUBLIC RESULTS COULD BE REACHED; NEVER A CARD INPUT.**

This folder holds the prospective shadow record for `tools/sport_models.py`. That file carries the numerical A0/A1 models for soccer, ice hockey, basketball, American football, AFL, rugby league, rugby union, baseball outside MLB, tennis and cricket. MLB keeps its own lane (`research/mlb_shadow/`), because its build adds probable starters.

The rules are the same as the MLB lane's. A model probability is never printed on a card, never used to rank rows and never cited as evidence for a pick.

## What each sport's model is

| Sport (league keys) | A0 — the baseline a card must beat | A1 — the interpretable challenger | Validated here? |
|---|---|---|---|
| Soccer (`epl`, `laliga`, `bundesliga`, `seriea`, `ligue1`, `championship`, `eredivisie`, `primeira`, `spl`, `aleague`, `mls`, `jleague`, `ucl`, `uel`) | League home and away goal rates; the league's first-half share | Time-decayed Poisson attack and defence ratings with a home factor. First half and second half are linked Poisson periods, so one distribution prices 1X2, handicaps, totals, team totals, BTTS and first-half lines | Yes: the five top leagues, 2022-23 to 2025-26 |
| Ice hockey (`nhl`) | League regulation goal rates; league overtime and shootout rates | Regulation Poisson ratings. Overtime is won in proportion to the two scoring rates at the league's decided-in-overtime rate; a shootout is a coin flip. Winners get +1, as the NHL scores it | No (no reachable results) |
| Basketball (`nba`, `wnba`, `nbl`) | League margin and total, with their SDs | Ridge offence/defence ratings. Normal margin and total, with no tie. Widths come from earlier out-of-sample residuals | NBA only, on 2013–2015 seasons (the only public NBA results reachable) |
| American football (`nfl`, `ncaaf`) | As basketball | As basketball, plus key-number weights (3, 7, 10, …) learned from the league's own margins | NFL, 2021–2025 |
| AFL (`afl`) | As basketball | As basketball; draws allowed | Yes, 2021–2024 |
| Rugby league (`nrl`) and rugby union (`union`, any ESPN path or CSV) | As basketball | As American football | No |
| Baseball outside MLB (`npb`, `kbo`, `cpbl`; CSV results) | The season's empirical total and margin frequencies | The MLB shared-environment joint (team, park and home), keeping the competition's tie rate | Tie handling on synthetic data only; the team-only core on MLB (Retrosheet 2022–2024) |
| Tennis (`atp`, `wta`) | Overall Elo for the winner; empirical total-games distribution by best-of | Surface-blended Elo mapped to serve-point probabilities, then the exact point → game → set → match chain | ATP, 2023 to January 2026 |
| Cricket (`t20`, `odi`; cricsheet JSON) | 0.5 for the result; the format's first-innings mean and SD | Elo for the result; ridge batting, bowling and venue model for uncensored first innings | No |

What the validation found, sport by sport, is in [`research/sport_models_2026-09-26/README.md`](../sport_models_2026-09-26/README.md).

## Files written here

| File | Written by | Rule |
|---|---|---|
| `shadow_log.csv` | `python tools/sport_models.py shadow …` | One row per event and line pair. It is frozen after the card and before the start, read from the ESPN scoreboard state. Append-only: the tool refuses to replace a row or to freeze a started event |
| `shadow_results.csv` | `python tools/sport_models.py settle` | Finals read from the same ESPN scoreboard, with source URL and time; never typed. Append-only |

Tennis and cricket are `predict` and `validate` only. Their results sources (TML-Database, cricsheet) lag by days, and neither is an admitted settlement feed.

## Order of operations for a card

1. Build and freeze the card as normal. The card never sees this model.
2. Before the start, run `python tools/sport_models.py shadow --league <key> --event <ESPN id> --date <YYYY-MM-DD> --card P-### --total <line> --line <home handicap>`.
3. After the final, run `python tools/sport_models.py settle`, then `python tools/sport_models.py score`.
4. `python tools/evidence_status.py` prints the per-league counts (`C-SPORT-SHADOW`).

## Preregistered review (150 settled rows per league; a review point, not proof)

A proposal to use a league's model as an anchor needs all three:

1. A1 − A0 Brier below 0, with the week-block interval also below 0.
2. A1 better than the cards' own p on the shared rows.
3. An explicit user instruction, because `C-RULE-FREEZE` treats any new anchor as a `MODEL_CHANGE`.

If a league fails the review, its lane continues or is retired, and the result is recorded either way.
