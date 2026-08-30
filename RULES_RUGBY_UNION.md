# Rugby union and rugby sevens analysis rules

Status: **ACTIVE — QUALITATIVE MODULE**
Effective: **2026-08-29**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, and ALGORITHM_PORTFOLIO_AND_EVALUATION.md.
Numerical status: **NO RUGBY-UNION OR RUGBY-SEVENS TARGET/SOURCE CARD, DATASET OR MODEL IS APPROVED OR FIT**

This module covers 15-a-side rugby union and rugby sevens. They share laws ancestry but have different duration, space, possession, rest, squad and scoring distributions. Neither population may be pooled with rugby league or with the other union format without an explicit population/era model.

## 1. Identity and contract

Resolve competition, season and law-trial era, 15s versus sevens, pool/knockout/tie state, venue, home/away/neutral status, match duration, extra-time/sudden-death/draw rules, bonus/qualification incentives, team/player/phase target, line, provider and operator settlement terms. Freeze whether the contract includes extra time.

## 2. Fifteen-a-side participants and exposure

- Confirm the official starting XV, bench, late changes, captain, halfback/fly-half pairing, primary and replacement goal kickers, front-row/set-piece roles and expected substitution/minutes plan.
- Translate absences and returns into set-piece stability, breakdown/ruck speed, territory kicking, gainline success, defensive alignment, goal-kicking and late bench state.
- Record rest, travel, short turnaround, venue, surface and match-window weather through a named mechanism.

## 3. Fifteen-a-side scoring process

Use opponent- and competition-adjusted:

- possession sequences, territory and opposition-22 entries;
- carries, metres/gainline success, clean breaks, defenders beaten and offloads;
- ruck speed/retention, turnovers won/conceded and handling errors;
- lineout and scrum retention/penalties, maul quality and restart outcomes;
- kicks in play, kick-return field position and tactical kicking;
- penalties by location, card/man-down exposure and referee effects only where current data support them;
- try creation and opposition-22 conversion;
- conversion, penalty-goal and drop-goal attempt/accuracy with current kicker identity;
- score-state decisions between goal, touch/lineout/maul and quick tap.

Raw points, broad competition averages and recent Over/Under hit counts describe outcomes. They cannot control a total unless the current lineup, territory/entry, set-piece/breakdown, discipline, try-conversion and goal-kicking pathways support the same scoring state.

## 4. Rugby sevens process

Freeze tournament stage, daily schedule, match duration, squad, rotation and recovery between games. Model:

- possession time and possessions;
- restart retention/regains;
- turnover-to-open-space conversion;
- passes/rucks per possession and retention;
- line breaks, missed-tackle/open-field exposure and tries per possession;
- conversion success and restart location;
- penalties, yellow cards/man-down minutes and sudden separation;
- score-state chasing and qualification incentives.

Sevens totals and margins are cluster-prone: one restart, turnover, breakaway or card can create several linked scores. Winner, handicap and total still come from one joint score tree, but a winner lean never implies a multi-score cover.

## 5. Joint model

For 15s, estimate possession/territory and scoring opportunities first, then split points into tries, conversions, penalty goals and drop goals. Use a joint team-score distribution with lineup, set-piece, discipline, weather, card, late-bench and extra-time branches.

For sevens, use a possession/restart/turnover/line-break state process with try/conversion, card, fatigue and stage-incentive branches. Keep 15s and sevens candidates and baselines separate.

All numerical forms are design ideas only. Suitable future baselines include empirical/shrunk joint scores and component count models; challengers may simulate possessions, territory/entries, set pieces, penalties/cards, tries and kicks. No form may publish a probability until its own target/source/H0/model cards and chronological gates pass.

## 6. Structural controls

1. **Union is not league.** No tackle-set, six-again, interchange or golden-point mechanism transfers from rugby league.
2. **Fifteens and sevens are separate populations.** Do not transfer scoring averages, margins or rest effects between them.
3. **Broad totals need mechanism support.** League average and recent Over counts cannot outrank thin matchup-native scoring evidence.
4. **Territory is not points.** Opposition-22 entry, lineout/maul, breakdown and finishing/goal-kicking determine conversion.
5. **Points composition matters.** The same total can arise from tries/conversions or repeated penalty goals; weather, discipline and score-state decisions affect them differently.
6. **Goal kicker is a regime variable.** Record attempt choice, range and replacement; tries and final points are not independent.
7. **Set piece and breakdown are exposure engines.** Scrum/lineout/maul and ruck/turnover states change possession quality and field position.
8. **Cards create asymmetric tails.** Rebuild remaining possession, width, try and margin exposure for the exact man-down duration.
9. **Low total does not imply close margin.** One side can suppress entries and create a controlled separation while the total remains low.
10. **Sevens clusters require restart/card branches.** A short match and small sample require wide tails, not false confidence.
11. **Sparse lineups cap evidence.** If official teams/kickers and matchup-native process data are missing, rank as required but cap participant-sensitive totals/sides at `FORCED RANK` or `MEDIUM-LOW` evidence.

## 7. Live state

For 15s store score, clock/half, cards and remaining duration, current players/substitutions, kicker, territory, opposition-22 entries, set pieces, penalties, turnovers, line breaks, tries/kicks and weather/surface. Rebuild remaining possessions and scoring composition.

For sevens also store possession/restart state, elapsed/remaining match time, daily match load and qualification context. Do not extrapolate an early breakaway rate across the remaining short match.

## 8. Sources and settlement

- World Rugby laws and competition regulations control laws, variations and scoring rules.
- Official competition/union/tournament match centres, team sheets, disciplinary releases and finals control current facts.
- New Zealand Rugby/provincial unions are preferred current lanes for NPC identity, team and match facts where exposed.
- Ligue Nationale de Rugby's official SuperSevens hub controls its schedule, stage, tournament reports and official results where exposed.
- Reputable specialist rugby providers may fill defined process fields after provider/coverage checks; they do not override official team, law or final corrections.

Settle score, phase, extra time, cards and player/team statistics under the exact provider and endpoint. If the official final is inaccessible, use two independent high-quality current sources and mark the affected field provisional.

Method references:

- [World Rugby Laws of the Game](https://passport.world.rugby/laws-of-the-game/).
- [Performance Analysis in Rugby Union: a Critical Systematic Review](https://doi.org/10.1186/s40798-019-0232-x), supporting context-specific use of territory, line breaks, metres, kicking, tackles, turnovers and penalties rather than a universal outcome statistic.
- [Performance Indicators Related to Points Scoring and Winning in International Rugby Sevens](https://pmc.ncbi.nlm.nih.gov/articles/PMC3990890/), supporting possession, restarts, set piece, phase play, turnovers, cards and scoring-rate decomposition; it does not establish an active coefficient.

## 9. Upcoming-game research sequence

1. Freeze code/format, competition/law era, stage, duration, extra-time/draw/qualification and contract/provider terms.
2. Retrieve the official fixture and teams/squad, bench/rotation, kickers and current availability; refresh immediately before start.
3. For 15s, build possession/territory/entry, set-piece/breakdown, discipline/card, try-conversion and goal-kicking branches.
4. For sevens, build possession/restart/turnover/open-space, try/conversion, card, recovery and qualification branches.
5. Stress lower, central, high-conversion, penalty-goal, card and controlled-separation states. Explain why broad scoring averages remain relevant after current matchup adjustment.
6. Derive winner, handicap and total from one format-correct joint score tree and log all missing participant/provider fields.
