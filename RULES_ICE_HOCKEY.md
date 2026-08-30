# Ice hockey analysis rules

Status: **ACTIVE**
Effective: **2026-08-30**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Numerical training specification: **NTS-2026.08.25-v0.2 — design only; no ice-hockey model is fit**

This module covers NHL and other ice-hockey competitions only after their rules, data and scoring populations are separated. It does not authorise an NHL probability model.

## 1. Identity and contract

Resolve competition, season/rules era, venue, home/away/neutral status, scheduled start, regulation versus overtime/shootout endpoint, tie/draw availability, puck-line/total/team/player/period target, goalie/action terms and provider statistic.

The following are distinct contracts and targets:

- regulation three-way result;
- moneyline including OT/SO;
- regulation score/total;
- full-match score as defined by the operator, including any shootout accounting convention;
- period target;
- team/player shots, points, saves and other provider events.

A completed period or settled player-action condition at issue is handled under the general SETTLED_AT_ISSUE rule.

## 2. High-value inputs

### Participants and exposure

- Confirm projected and, when available, official line combinations, defence pairs, power-play/penalty-kill units and scratches.
- Treat starting goalie as a regime variable. Model start probability, recent workload/rest, injury/return state, replacement quality and pull risk.
- Estimate skater ice time, line/unit role, shift distribution and special-teams exposure. Active does not guarantee normal minutes or role.
- Record back-to-back/rest, travel, altitude, venue and roster/coach/system changes.

### Shot and goal process

Use opponent- and manpower-adjusted:

- shot attempts, unblocked attempts and shots on goal under the named definition;
- shot location/angle/type, pre-shot movement/rebound context and expected-goal quality where provider-defined;
- finishing talent with shrinkage;
- goaltending/save quality and shot mix;
- offensive-zone/transition/forecheck process where available;
- power-play and penalty-kill opportunities/efficiency;
- penalties, score state, pulled-goalie and empty-net behavior.

Raw recent goals, save percentage, head-to-head and one hot/cold streak are outcomes, not stable rates without mechanism and opponent adjustment.

## 3. Model

Exposure units are regulation minutes, shifts, ice time, shot attempts/chances, shots on goal and manpower-state possessions. Estimate shot/chance intensity and quality first, then finishing/goaltending, special teams and empty-net branches.

Use a joint regulation goal distribution. Link it to a separate rules-correct OT/SO result process for full-match moneylines. Derive regulation winner, totals, team totals and puck lines only from the target object matching their endpoint. Player shots/points/saves use their own participation × ice-time/opportunity × event-rate distributions linked to team/score/manpower state.

Numerical candidates begin with empirical and independent-Poisson diagnostics, then hierarchical bivariate/count distributions. The A2 candidate simulates shifts/shots, manpower state, goalies, score effects, penalties, pulled goalie, empty net, OT and shootout. Boosted/ordered score grids are challengers only after support, dispersion, covariance, tail, OOD and calibration checks. Every candidate is unfit and unvalidated.

## 4. Structural controls

1. **Goalie uncertainty is a scenario mixture.** Do not use a reported expectation as confirmed fact.
2. **Shots and goals are linked but not interchangeable.** Shot quality, finishing and goalie state mediate conversion.
3. **Blocked shots are definition-sensitive.** A dataset that omits them cannot control all-attempt metrics without reconciliation.
4. **Special teams change both exposure and rate.** Use current units and penalty environment; season percentage alone is incomplete.
5. **Score state changes pace and shot mix.** Trailing teams may create more attempts while allowing transition/empty-net risk.
6. **Empty-net goals are an explicit tail.** They affect totals and margins differently from five-on-five central play.
7. **Regulation and moneyline are different targets.** A regulation draw can proceed to OT/SO; never infer one contract mechanically from the other without the linked process.
8. **Back-to-back is mechanistic.** Connect rest to goalie choice, line workload, forecheck/transition and late-game quality.
9. **Player props require role and ice time.** Recent shots/points do not substitute for line, unit and matchup exposure.
10. **External xG/forecast models are challengers.** Cite their provider/method/version and never present them as internal probabilities.
11. **Shot volume is exposure, not a goal total.** A high SOG forecast or realised shot edge cannot by itself support an Over. The total rationale must separately represent shot quality, finishing shrinkage, confirmed/probable goalie mixtures, special teams and empty-net exposure.
12. **Sparse competitions retain a conversion cap.** When current goalie identity, shot quality or manpower context is unavailable, recent high-scoring results and raw SOG may describe the ceiling but cannot remove the low-conversion branch or justify false confidence.
13. **OT result geometry and operator settlement remain separate.** In sparse competitions, a verified overtime final can settle the research event path, but it does not establish whether a supplied moneyline, puck line or total included OT/SO or how shootout goals are counted. Preserve the regulation-draw/one-goal-OT branch and use `UNKNOWN_DEFINITION` until the named operator/action terms are available.

## 5. Live state

Store score, period/clock, current manpower/penalties, goalie in net, shots/attempts and xG under named definitions, line/unit changes, injuries/ejections, timeouts, pull state and venue conditions. Rebuild remaining regulation exposure, goalie/pull/empty-net branches and any later OT/SO process; do not extrapolate elapsed goals per minute.

## 6. Sources and settlement

- NHL/competition official rules, match centres, roster/lineup/goalie reporting, statistics and finals control official facts.
- The [NHL hockey glossary](https://www.nhl.com/info/hockey-glossary) controls NHL official-stat definitions where applicable.
- [NHL projected lineups/goalies](https://www.nhl.com/news/topic/game-previews/nhl-projected-lineup-projections) is an official reporting lane but remains projected until confirmed.
- [MoneyPuck downloads](https://www.moneypuck.com/data.htm) and methodology may support specialist research only within current use/attribution terms. Its documented downloadable shot data omits blocked shots; do not silently treat it as all shot attempts.
- Other shot/xG/line providers control only their defined metrics after coverage, method, licence and correction checks.

Settle from the official final and named statistic provider, preserving regulation/OT/SO and shootout-score conventions. Retry official stat corrections for player props before UNSETTLEABLE.

## 7. Upcoming-game research sequence

1. Freeze competition/rules, regulation/full-match endpoint, goalie/action/stat-provider terms and complete candidate slate.
2. Retrieve official event/roster/injury state, projected goalie/lines and current specialist shot/process data; refresh confirmed goalie, scratches, lines/units and state immediately before puck drop.
3. Estimate regulation minutes/shifts, shots/chances by manpower and score state, shot quality, finishing, goalie/save distribution, penalties/special teams and pulled-goalie/empty-net branches.
4. Audit whether the total direction survives a high-shot/low-conversion branch and each unresolved starting-goalie branch.
5. Produce one regulation joint goal object and, where required, a linked OT/SO result object. Player props retain their own ice-time/opportunity target.
6. Derive and rank only contracts whose exact endpoints and definitions are resolved. Missing goalie confirmation widens scenarios; it does not authorise an invented starter or probability.
