# Baseball analysis rules

Status: **ACTIVE**
Effective: **2026-08-30**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Numerical training specification: **NTS-2026.08.25-v0.2 — design only; no baseball model is fit**

## 1. Identity and contract

Resolve league and level: MLB, NPB, KBO, LMB, WBSC, minor league, college, or another competition. Record season/rules era, venue, home batting entitlement, designated-hitter rule, scheduled innings, doubleheader format, extra-innings rule, probable/confirmed starters, and operator action/listed-pitcher terms.

For MLB, use the current official rule and technology environment. The 2026 ABS challenge system weakens transfer from old home-plate zone tendencies; do not use an umpire effect without current-system evidence.

## 2. High-value inputs

### Participants and exposure

- Complete the final starter-identity handshake for both sides against the official event page or official team/league release. Store event ID, team, role, participant ID/name and `CONFIRMED_OFFICIAL`/`PROBABLE_OFFICIAL`/unresolved status; never translate a same-day secondary preview into a confirmed starter.
- Confirm both posted batting orders, bench, catcher, defence, starters, and material absences. If official starters or orders are not released, model explicit participant mixtures and apply the general evidence cap rather than choosing one preview lineup.
- Estimate plate appearances by lineup slot.
- For each starter, model batters faced, pitches, innings, and hook point separately from runs allowed.
- For every relevant reliever, estimate availability probability and likely role. Build opener → bulk → bridge → leverage → low-leverage alternatives; workload informs availability, not performance.

### Starter and lineup process

Use the current arsenal against the current lineup:

- pitch mix, velocity, movement and location;
- K-BB%, whiff/chase, ground/fly-ball shape, HR, barrel/hard-hit and expected contact measures where valid;
- handedness and platoon shape;
- catcher, defence, park, and opponent quality;
- injury/return, pitch cap, rest, and recent mechanics.

ERA and WHIP are context, not a complete distribution. FIP/xFIP/xERA or league equivalents are supporting estimates with their definitions and limitations. Direct starter history receives weight only when current-lineup overlap and arsenal/role continuity are meaningful; never promote one prior start as ownership.

### Environment and context

Record park factors with year/rolling window, dimensions, roof, venue-local game-window weather, altitude, rest/travel, series state, and home last-bat. Hot air, humidity, rain, or wind has no automatic total direction. Officials, motivation, and press comments are conditional only.

## 3. Model

Exposure units are plate appearances, pitcher batters faced, pitches, innings, and live base-out state. Use a joint team-run distribution with overdispersion and explicit sequencing/HR tails rather than a naive homogeneous Poisson.

Build:

1. starter run-rate and exit distributions;
2. the named relief-chain distribution;
3. lineup PA and matchup rates;
4. park/weather/defence adjustments;
5. home-ninth, extra-innings, and score-state branches.

Derive winner, run line, team total, game total, and player contracts from that same distribution.

For numerical training, compare empirical and Poisson/negative-binomial team-run baselines with a plate-appearance/base-out A2 simulator. The structural candidate samples starter batters faced/hook state, the named relief chain, PA outcomes, base/out transitions, sequencing and HR clusters, home-ninth entitlement and extra innings. A bivariate/direct score model or boosted distribution is a challenger only after covariance, overdispersion, support, era and tail checks. All totals, run lines and winners integrate the same joint run distribution; line-specific binary classifiers cannot become the primary engine. All candidates remain unfit and unvalidated.

## 4. Structural controls

1. **Short start is exposure, not an automatic Over.** More bullpen innings raise uncertainty; direction depends on the likely arms and lineup.
2. **Recent run suppression does not erase the HR/contact tail.** Record central and short-start/two-homer branches.
3. **Pitch limit and innings are separate.** Efficiency, baserunners, plate-appearance length, and quick outs determine how far a pitch cap travels.
4. **Cushion decomposition.** For every +1.5 line record win, exactly-one-run loss, and 2+-run loss branches.
5. **Low total does not imply close margin.** One dominant starter and clustered damage can produce a multi-run Under.
6. **Bullpen freshness is not quality.** Name the likely chain and manager alternatives.
7. **Post-trade or role-change regime.** Rebuild catcher, arsenal, velocity/location, mechanics, role, and current-lineup fit.
8. **Trend mechanism.** Classify recent totals by starters, lineups, contact/HR, errors, relief chain, park and weather before using an Under/Over run.
9. **Gapped/overlapping lines.** Map every interval; opposite-team positive run lines can both win, and alternate totals can overlap.
10. **Home batting exposure is state-dependent.** Derive ninth-inning entitlement from the score distribution; do not apply a fixed innings fraction.
11. **Small-sample starters require a mixture.** A debut, return, young starter, opener, or one-start sample is pooled toward the league/role prior with explicit good-start, ordinary, early-hook and contact/HR tails. One good outing cannot collapse that uncertainty.
12. **Starter identity precedes starter quality.** No ERA, arsenal, platoon or hook analysis is decision-driving until the starter is linked to the exact official event/team role at the final volatile refresh.
13. **Season prior versus current starter regime.** When recent arsenal/velocity/location, role, opponent quality or contact indicators conflict with season ERA/reputation, retain a shrunk season/league prior and an explicit current-regime branch. State why each branch is weighted; do not let either a famous season line or a short hot/cold run win silently.
14. **Defence and unearned-run tails stay in the score tree.** Team fielding quality may adjust the baseline, but one game's error cluster is a realised tail unless a current personnel/positioning mechanism made it forecastable. Do not backfit a generic error penalty from a single final.
15. **Joint hook-tail reconciliation.** When either starter is debut/small-sample/returning or both starters have wide exit distributions, construct the joint early-hook branch: batters faced, inherited runners, first available relief arms, bullpen innings, contact/HR cluster and home-ninth exposure. Before an Under can outrank its Over, state why that joint upper tail remains subordinate; otherwise lower evidence or change the order.
16. **Strong opponent starter does not erase debut variance.** A favourable opposing-starter matchup may shift the centre, but it cannot collapse a rookie/first-starter's ordinary and early-hook branches. Both teams' exposure mixtures survive into the total and margin distribution.
17. **Low-total separation remains explicit.** For each underdog +1.5 or favourite -1.5 row in a low-total game, retain shutout and 2–0/3–0/4–1-style one-sided branches. Low expected runs do not mechanically create a close margin.
18. **Weather termination has an event order.** Under the competition's official-game and operator-action rules, separate runs-before-stop, stop-before-runs, restart/relief-transition and void/no-action branches. Rain or a shortened final is not mechanically an Under once a clustered inning has already crossed the line.
19. **Stable starter centres do not remove cluster risk.** Even when both starters have established central projections, retain walks/errors, sequencing, multi-run homer, inherited-runner and first-relief-transition branches. The upper tail is a joint inning/relief state, not only an “early hook” label.

## 5. Live state

Store inning/half, score, outs, base state, current pitcher/pitch count, bullpen behind him, lineup slot due, challenges/reviews, weather/roof, and home batting entitlement. Recalculate remaining PA and named pitcher/reliever branches.

## 6. Sources and settlement

- MLB official StatsAPI and MLB match centres control schedule, lineups, live state, box score, transactions, and final.
- [MLB Statcast glossary](https://www.mlb.com/glossary/statcast) controls Statcast definitions; Baseball Savant supplies park and batted-ball data.
- NPB.jp/BIS, KBO, CPBL official/advanced game pages, LMB.com.mx, WBSC, and official league/team sources control their competitions. Each league remains a separate source/definition population.
- Government weather services and official roof reports control game-window conditions.

Settle from the official final and named statistic provider. Preserve extra-innings and listed-player rules. Recheck documented official stat corrections for props.

## 7. Upcoming-game research sequence

1. Freeze league/rules era, scheduled innings, home-last-bat/extra-inning terms, listed-pitcher/action rules and full candidate slate.
2. Retrieve official probable/confirmed starters, posted orders, catcher/defence, transactions/injuries, roof and park-local weather; refresh lineups, starters, roof and weather before issue.
3. Model lineup PA, starter batters faced/pitch/inning/hook distribution, current arsenal versus lineup, the named bullpen chain, base-out transitions, sequencing/HR clusters, park/defence and home-ninth/extras. If either starter is debut/small-sample or both exit distributions are wide, stress their joint early-hook/relief/cluster branch before ordering the total.
4. Maintain MLB, NPB and KBO as separate priors/rules/data cards; MLB Statcast-era measurements cannot be silently transferred to another league or earlier tracking regime.
5. Derive winner, total, team totals and run lines from the joint run object. Pitcher/batter props use action probability and their own PA/batters-faced/event-rate targets.

Official league/team sources control lineups, starters, rules and finals. Statcast/Savant controls only its defined MLB tracking metrics; projections are external challengers, not labels or ground truth.
