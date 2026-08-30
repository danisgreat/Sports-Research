# American football analysis rules

Status: **ACTIVE**
Effective: **2026-08-30**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Numerical training specification: **NTS-2026.08.25-v0.2 — design only; no football model is fit**

## 1. Identity and contract

Resolve NFL preseason/regular/postseason, NCAA level/conference/bowl/playoff, UFL, high school, CFL, or another code. These are different rules and data environments. Record regulation/OT/tie terms, spread/total/team/player phase, stat provider, and listed-player/action terms.

Verify the current governing rulebook. Relevant 2026 regime checks include NFL kickoff/onside/overtime rules, NCAA timing/overtime and conference availability systems, and UFL four-point field goal, 1/2/3-point try, punt, catch, and shootout-style overtime rules. Never transfer NFL key numbers or possession rules to NCAA/UFL/CFL.

## 2. High-value inputs

### Quarterback and expected snaps

- Confirm starting quarterback, backup branch, health/mobility, expected snaps, and scheme.
- For side, total, passing, rushing, or pressure-sensitive markets, map the material offensive-line combination and replacements. Do not require irrelevant roster detail for an unrelated contract.
- Estimate expected snaps/routes/carries/targets for material skill players and replacement roles.
- Record defensive front, coverage, and sub-package absences that affect the matchup; confirm kicker/punter/long snapper when the contract depends on them.
- Preseason requires quarterback/unit rotation and expected reps, not regular-season power ratings.

### Drive process

Use opponent- and quarterback-regime-adjusted:

- expected drives and neutral pace;
- starting field position;
- early-down EPA/success;
- pass/run rate and play action;
- pressure, sack, scramble and explosive rates;
- coverage and protection matchup;
- third/fourth-down and red-zone process;
- turnovers with shrinkage;
- special-teams field position and scoring.

Raw points, one-score record, turnover margin, and defensive touchdowns are outcomes, not stable abilities by default.

### Context

Record rest/bye/short week, travel/time zones, surface/roof, venue-local weather, altitude, opponent quality, and verified roster/coach changes. College homecoming, exams, rivalry, bowl, portal or opt-out context matters only when verified and connected to participation or tactics.

## 3. Model

Exposure units are drives, plays within drives, starting field position, and expected snaps. Map drive outcomes to touchdown, field goal, no score, safety, and non-offensive score, then add dependent tries/kicks.

Use quarterback-regime dynamic strength, trench and coverage interactions, and explicit explosive/turnover/non-offensive-score tails. Points cluster around football scoring values and are not a homogeneous Poisson process. Derive side, total, team, phase and player contracts from one joint score distribution.

For numerical training, retain empirical and simple drive-rate baselines, then challenge them with a drive/possession A2 simulator. It samples remaining drives, start field position, plays, TD/FG/safety/no-score/turnover outcomes, dependent tries, non-offensive-score tails, clock/game script and competition-specific overtime. Tree or distributional models estimate state components or a coherent score grid; they do not fit one independent classifier per spread/total. Exact football key values and push mass come from the discrete joint score distribution. All candidates remain unfit and unvalidated.

## 4. Structural controls

1. **Quarterback identity is a regime change.** Rebuild pace, pass/run, pressure, scramble and receiver distribution.
2. **Line continuity is combinatorial.** One returning tackle does not repair every pressure path.
3. **Game script creates dependence.** A leading favourite may drain clock; a trailing team can add yards, sacks, turnovers and garbage-time points.
4. **Turnovers and one-score records shrink.** Require pressure, decision, ball-security or coaching mechanisms.
5. **Weather is matchup-specific.** Wind, cold/heat, snow, footing and roof affect passing/kicking/tempo differently; rain is not an automatic Under.
6. **Key numbers and pushes are discrete.** Model score combinations and exact integer boundaries.
7. **Overtime matches the competition/contract.** NFL regular/postseason, NCAA and UFL rules differ.
8. **Special teams are field-position mechanisms.** Use current kickoff and return rules.
9. **Preseason is a separate phase model.** Starter quality matters only for expected reps.
10. **College availability is asymmetric.** Absence of an NFL-style report does not mean healthy.
11. **Preseason is a quarter-by-quarter unit mixture.** Freeze expected quarterback, offensive-line, skill-unit and defensive-rotation reps by phase. If rep plans are missing, widen the side and total distributions and cap unit-dependent claims; never project a starter or one reserve sample through four quarters.
12. **Reserve-sample shrinkage and explosive tails.** Pool tiny backup/deep-reserve quarterback samples toward the relevant role/competition prior. Retain coverage busts, return/non-offensive scores, short fields, long conversion drives and fourth-down/red-zone variance even when the central reserve efficiency is low.
13. **Low total does not imply close spread.** Preserve low-underdog-score and shutout branches before ranking a positive underdog cushion over the favourite.
14. **CFL possession-to-points chain is code-specific.** For Canadian football, model expected rushing workload, second-down conversion, protection/explosives, red-zone touchdown conversion and possession share under CFL downs, field and timing rules. A supported underdog-control branch can defeat both favourite and Under and must be reconciled with their ranks.
15. **Aligned current-regime uncertainty caps a favourite.** In openers and transitions, separately branch new quarterback/coordinator, protection, availability, neutral-site, weather and opponent-upgrade states. When several current uncertainties all support the favourite's ordinary kill path, a prior-season power rating, reputation or broad market direction cannot leave the favourite spread `SUPPORTED`; lower evidence or rank the robust opposing spread/total branch unless current matchup evidence resolves the conflict.

## 5. Live state

Store score, quarter/clock, possession, ball spot, down/distance, timeouts, drive origin/count, opening/second-half possession, penalties, turnovers/short fields, fourth-down decisions, QB/line status, injuries/ejections, snap/route/carry distribution, roof/weather, and scoring type.

Recalculate remaining drives from clock, pace, timeouts, game script, field position, fourth-down aggression, onside/kneel-down branches, and competition rules.

## 6. Sources and settlement

- [NFL rules and operations](https://operations.nfl.com/rules-officiating/), NFL official injury reports, match centres and gamebooks control NFL.
- [NCAA football playing rules](https://www.ncaa.org/championships/playing-rules/football-playing-rules), official conference/school availability, schedules and gamebooks control college.
- Official UFL rules, match centres, transactions and team releases control UFL.
- NFHS/state associations control high school; CFL official sources control Canadian football.
- Government weather services and venue/airport observations control conditions.

Settle from the official final/gamebook and named stat provider. Reconcile kneel-downs, sacks, laterals, returns, defensive scores and stat corrections under the competition's conventions.

## 7. Upcoming-game research sequence

1. Freeze code/competition, current rules, regulation/OT/tie terms, phase, listed-player/action rules and candidate slate.
2. Retrieve official QB, injury/availability, roster/inactive and weather/roof facts before historical trends; refresh after the applicable inactive/availability release and just before issue.
3. Model QB/regime and line/skill exposure, expected drives/plays/field position, drive outcome probabilities, red-zone/fourth-down process, special teams and turnover/explosive tails. In preseason, do this by expected unit and quarter; in CFL, include rushing possession, second-down and red-zone conversion explicitly.
4. Preserve football's discrete scoring combinations and exact key-value/push mass. Competition-specific OT and try rules are part of the target, not a display adjustment.
5. Derive winner, total, margin and team scores from one joint score object. Props use snaps/routes/carries/targets/kicking opportunities and their own provider labels.

nflverse/nflfastR-style data is a candidate NFL play-by-play lane, not the official owner of current availability or rules and not approved for H0 until the source card passes.
