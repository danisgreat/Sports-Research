# Australian rules football analysis rules

Status: **ACTIVE**
Effective: **2026-08-30**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Numerical training specification: **NTS-2026.08.25-v0.2 — design only; no AFL model is fit**

## 1. Identity and contract

Resolve AFL, AFLW, VFL, SANFL, WAFL, or another competition; season/rules era; round/finals state; venue; home/away/neutral; named teams and late changes; regulation/draw/overtime terms; and whether the contract is margin, total, quarter/half, team, player, or statistic.

AFL and AFLW are separate modelling populations. Do not transfer scoring levels or volatility without an explicit hierarchical adjustment.

## 2. High-value inputs

### Participants and roles

- Confirm the named team, interchange, substitute/activation rules for the current competition, late outs, and replacement.
- Estimate time on ground, position, centre-bounce attendance, ruck share, forward/defensive role, and expected matchup.
- Translate each absence into the territory/scoring chain; do not count a name without role consequence.

### Territory and shot creation

Use opponent-adjusted:

- centre and stoppage clearances;
- contested possession and pressure;
- turnovers/intercepts and rebound;
- inside-50s and repeat entries;
- marks inside 50;
- scoring shots, shot location/pressure quality, and expected score where available;
- conversion, separated from shot creation.

A ruck or clearance edge is not points until it survives the chain from hitout/contest → clearance → inside-50 → mark/shot → conversion.

### Context

Record venue dimensions/roof, surface, match-window weather, rest, travel, ladder incentives, and coaching/tactical changes. Weather can suppress clean handling or create territory/short-field repeat entries; no automatic Under is allowed.

## 3. Model

Exposure units are time on ground, centre/stoppage possessions, inside-50s, marks inside 50, and scoring shots. Estimate territory and shot creation first, then shot quality/conversion. Use a joint score and margin distribution with overdispersion and both late-separation and tempo-control branches.

Derive winner, handicap, total, phase, and player/stat contracts from that same distribution.

For numerical training, compare empirical and simple scoring-shot baselines with a territory → inside-50 → mark/shot → goal/behind A2 simulator. The simulator preserves both teams' tempo/territory dependence, shot quality, conversion, late separation and phase transitions. Direct joint-score, distributional boosting and hierarchical conversion candidates must pass AFL/AFLW population, support, covariance, overdispersion and calibration checks. Elo is an upstream strength feature/baseline, not a replacement for the scoring chain. Every line integrates the same joint score distribution. All candidates remain unfit and unvalidated.

## 4. Structural controls

1. **Decompose the current shot chain.** Model territory → inside-50 → mark/shot → shot quality/conversion separately. Raw recent totals and old H2H are diagnostic only; any numerical relative weight must be learned from prediction-time-safe data.
2. **Estimate conversion persistence separately.** Do not assume unusually accurate or inaccurate kicking persists or regresses at a fixed rate without current shot-quality and comparable-population evidence.
3. **Winner and handicap are different thresholds.** Model the whole margin distribution; do not align them mechanically.
4. **Positive handicaps for both teams can overlap.** Map every interval.
5. **Live Under requires observed suppression.** Remaining allowance must be supported by current inside-50/scoring-shot/tempo evidence.
6. **Large Q4 cushion requires remaining-possession analysis.** A tied or close state plus favourite clearance/territory control can create fast separation.
7. **Venue and competition matter.** Marvel/MCG/Optus and AFL/AFLW baselines are not interchangeable.
8. **Hitouts are opportunity, not territory.** Use clearance and post-clearance outcomes.
9. **High total needs a high-shot branch.** For 180+ men's totals, store both teams' current inside-50, marks-I50, scoring-shot, ruck/clearance and venue distributions.
10. **Motivation remains conditional.** Ladder urgency changes weight only through selection, roles, pressure, tempo, or tactics.
11. **Availability-to-conversion handshake.** Returning or absent forwards, midfield creators and goal kickers must be translated through role/time on ground, centre-bounce or inside-50 involvement, shot location/pressure, scoring-shot volume and goal/behind conversion. Do not apply a name-only scoring bump.
12. **Conversion sensitivity near the line.** When current personnel or shot-quality evidence makes conversion materially uncertain, report the total/margin ordering under at least a lower, central and upper conversion branch. Recent raw points or accuracy cannot fix the branch weight by themselves.
13. **Scoring volume and margin allocation are separate.** A low aggregate scoring-shot or conversion state can still create decisive separation when one side suppresses the opponent. Query the total and margin independently from the joint score tree; a broad Under is not evidence that an underdog cushion is safe.

## 5. Live state

Store score, quarter/clock, scoring shots and accuracy, inside-50s, marks inside 50, centre/stoppage clearances, current-quarter territory, rotations, injuries/substitute, weather/roof, and tactical state. Recompute remaining scoring shots and margin branches rather than extending points per minute.

## 6. Sources and settlement

- AFL/AFLW official match centres, team sheets, injury reports, tribunal/late-change notices, and official statistics control.
- The [AFL statistics glossary](https://www.afl.com.au/news/144837/stats-glossary-every-stat-explained) controls definitions.
- BOM and official venue sources control weather/roof.
- Reputable tracking providers may supply expected score or role detail after definitions and coverage are checked.

Settle from the official final/stat provider, preserving draw/overtime and phase terms.

## 7. Upcoming-game research sequence

1. Freeze competition/rules era, venue, phase, draw/overtime terms and candidate slate; AFL and AFLW remain distinct populations.
2. Retrieve official selected teams, injuries, substitute/interchange rules and late changes first. Refresh after the current official final-team/late-change window and just before the bounce.
3. Model role/time-on-ground/CBA/ruck exposure, territory and clearance chain, inside-50s/marks-I50, scoring-shot volume/quality, goal/behind conversion, venue dimensions, roof/weather and tempo/separation tails. Translate returning/absent scoring personnel through that chain and run conversion sensitivity when it can cross the supplied line.
4. Treat conversion separately from shot creation and hitouts separately from clearances/territory. External ratings/consensus are baselines or challengers, not the scoring engine.
5. Derive joint scores, winner, total and margin/handicaps from the same score object; player/stat targets retain their own role/exposure labels.

Official AFL/AFLW sources own current teams, state and definitions. AFL Tables/Squiggle-style sources are candidate historical or external-model lanes only, with access/coverage limits recorded in DATA_SOURCE_REGISTER.md.
