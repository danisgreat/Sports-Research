# Tennis analysis rules

Status: **ACTIVE — QUALITATIVE MODULE**
Effective: **2026-08-29**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, and ALGORITHM_PORTFOLIO_AND_EVALUATION.md.
Numerical status: **NO TENNIS TARGET/SOURCE CARD, DATASET OR MODEL IS APPROVED OR FIT**

## 1. Identity and contract

Resolve tour/competition and level, event, round, surface and indoor/outdoor state, best-of format, final-set tiebreak rules, ball/altitude where verified, and whether the match is singles or doubles. Freeze each contract's retirement/walkover, completed-set, super-tiebreak, dead-heat and void rules from the named operator. A match winner, set handicap and total games contract can settle differently after retirement and are not interchangeable.

## 2. Participants, exposure and current regime

- Confirm the exact players, handedness, current entry/ranking status, draw/round and scheduled start from the official event/tour source.
- Record current surface, the player's recent surface-specific schedule, match duration, rest, travel, qualifying workload, medical timeout/retirement history and credible current injury reporting.
- Separate career/season prior from the current surface-and-role regime. Ranking and reputation are priors, not current form measurements.
- Use opponent-adjusted serve and return points won, first-serve-in rate, first/second-serve points won, break-point creation/saving, hold/break rates, ace/double-fault shape and tiebreak exposure where definitions and sample are reliable.
- Shrink tiny current samples toward an appropriate tour/level/surface prior. Do not let one tournament or one match become the baseline.

## 3. Matchup and continuity

Trace handedness, serve direction/return position, backhand/forehand tolerance, rally length, movement, height/bounce, net use and pressure-point performance through the current surface. Head-to-head is decision-driving only when surface, format, competitive level, fitness and technical/role continuity are material; an old indoor-hard meeting cannot control a current clay match.

When ranking, older H2H, rankings and broad season aggregates must be explicitly reconciled against current surface form and serve-return stability under RULES_GENERAL's regime-dominance audit. If they conflict and the current sample is weak, widen the match distribution and lower evidence quality instead of choosing whichever history supports the preferred side.

## 4. Joint match model

Exposure units are service points, return points, games, sets and match-completion state. Build one coherent qualitative or future numerical match process:

1. participation and completion/retirement branches;
2. surface- and opponent-adjusted point-on-serve distributions for both players;
3. game/hold and break distributions with score-state and pressure uncertainty;
4. set score and tiebreak branches;
5. match winner, set handicap and total-games queries derived from the same simulated or qualitative score tree.

Best-of-three totals require explicit straight-set and three-set mixture weights. A player can be the better winner while a broad opponent +1.5-set cushion is more likely; that relationship must come from the shared match tree, not from independent narratives. Total games depend on set count and within-set closeness, so a three-set branch can rescue both player set cushions and the Over without making those rows independent.

The tree is two-sided. For each player, represent at least: ordinary straight-set control, close straight sets/tiebreaks, and a deciding-set win where supported. A perceived underdog may win quickly; never couple all underdog-win probability to a long or three-set match. First-set contracts use an explicit opening-set state derived from early hold/break/return pressure and current start patterns; they do not inherit the full-match winner ranking.

## 5. Structural controls

1. **Surface is a regime variable.** Overall ranking and all-surface records never override a material surface-specific serve/return change without reconciliation.
2. **Current stability is decomposed.** Distinguish first-serve entry, first/second-serve conversion, return pressure and break-point opportunity; one win/loss streak is not a mechanism.
3. **H2H needs continuity.** Downweight old meetings across surface, level, format, fitness or technical changes.
4. **Set count and game total are linked.** Store straight-set and deciding-set branches and tag dependence.
5. **Set cushions are not free safety.** Price-free likelihood can favour +1.5 sets, but the row still needs a credible set-winning or match-length pathway.
6. **Qualifying and workload change exposure/variance.** Fatigue is not automatically negative; model fitness, acclimatisation and accumulated match load separately.
7. **Retirement terms are a hard gate.** Unknown operator treatment means `UNKNOWN_DEFINITION` and `NO VALUE DETERMINABLE`.
8. **No ranking-only confidence.** ATP/WTA/ITF/UTR rankings and seeding are context, not sufficient evidence for LEAN/SUPPORTED.
9. **Opponent and level comparability must be demonstrated.** Raw ATP, Challenger, qualifying, ITF and other level/surface rates are not exchangeable. State the opponent-strength/level adjustment and shrinkage, or lower the evidence grade.
10. **Win-conditioned cover counts are descriptive only.** A player covering a game handicap in six of seven recent wins does not independently estimate the chance of winning or covering the next match.
11. **Kill paths include opponent control.** For a favourite handicap, “favourite wins narrowly” is incomplete whenever a credible opponent win—especially straight-set control—also defeats the contract.

## 6. Live state

Store set/game/point score, server, tiebreak state, elapsed time, verified injury/medical state and current serve-return point counts. Recalculate only the remaining point/game/set tree. Do not extrapolate a short hot serving spell as a permanent rate change, and do not use a stale scoreboard when participant orientation or server is uncertain.

## 7. Sources and settlement

- Official ATP, WTA, ITF, event and governing competition pages control identity, draw, format, score and official result where exposed.
- Official event/tour statistics control only their defined serve/return fields.
- Reputable specialist score/stat pages may cross-check current results and fill research fields, but they do not override an official correction and require provider/definition continuity.
- Player/social reporting can evidence a statement or injury report only when account identity and publication time are verified; official event status controls withdrawals and walkovers.

Settle from the official final and exact operator retirement rules. If an official stat field is unavailable, use two independent high-quality sources and mark the field provisional; do not infer total games or set scores from the winner alone.

## 8. Upcoming-game research sequence

1. Freeze competition/round, surface, format/tiebreak and operator retirement terms.
2. Verify draw identity, schedule, current withdrawal/fitness state, rest/travel and qualifying workload.
3. Build surface- and opponent-adjusted serve/return priors; separate broad baseline from current regime and shrink sparse samples.
4. Audit H2H continuity and the strongest contrary matchup path.
5. Build straight-set control, close-set/tiebreak and deciding-set branches for **both** players; derive winner, set handicap and total games from the same tree.
6. For first-set rows, freeze a separate opening-set sub-tree and show why it differs from or agrees with the full-match state.
7. Refresh official participant/status fields immediately before issue and log unresolved definitions or missing statistics.
