# Basketball analysis rules

Status: **ACTIVE**
Effective: **2026-08-29**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Numerical training specification: **NTS-2026.08.25-v0.2 — design only; no basketball model is fit**

## 1. Identity and contract

Resolve league, season/rules era, regulation/OT treatment, venue, scheduled start, quarter/half/full-game phase, team/player statistic, line, and operator terms. NBA, WNBA, NCAA, FIBA, domestic leagues, summer league, and preseason have different clocks, foul rules, rotations, and overtime environments.

A phase already completed at issue is SETTLED_AT_ISSUE and unranked.

## 2. High-value inputs

### Participants and minutes

- Use the newest official injury/availability report and confirmed starting five.
- Separate active status from expected minutes, role, usage, and closing-lineup probability.
- Model replacement minutes and lineup combinations; uncertain minutes widen the distribution rather than making all player projections worthless.
- Record rest, back-to-back, travel, altitude, and recent overtime.

### Possession process

Use opponent-adjusted:

- possessions/pace and transition share;
- half-court efficiency and shot quality;
- rim, three-point, and midrange mix;
- free-throw rate;
- turnover and offensive-rebound rates;
- lineup-specific offence/defence;
- foul/bonus and late-game behaviour.

Raw points per game and recent shooting percentage do not substitute for possessions and shot profile.

## 3. Model

Exposure units are minutes, possessions, lineup stints, usage, and shot/rebound/turnover opportunities. Estimate possessions and per-possession efficiency jointly, with lineup branches and overdispersed shooting outcomes.

Model Q1, Q2, first half, second half, and full game as related but distinct segments. Derive all totals, spreads, winners, and props from one coherent joint game distribution.

For numerical training, benchmark a conditional empirical/joint score distribution and simple regularized possession × efficiency model before a possession/lineup state simulator. Candidate nonlinear models estimate possession, efficiency, shot/rebound/turnover or distribution parameters—not unrelated classifiers for each total/spread. The A2 candidate samples remaining possessions, lineup stints, shot/FT/turnover/rebound outcomes, foul/bonus, late fouling, blowout and overtime, then produces one joint team-score distribution. Direct bivariate Normal/Student-t or distributional boosting forms are challengers only with discrete/support, tail, covariance and held-out calibration checks. None is currently fit or validated.

## 4. Structural controls

1. **Nested rows are dependent.** One Q1/H1/full-game pace thesis gets one PRIMARY_FORMAL row unless another phase has independent evidence.
2. **Q1 pace does not determine Q2.** Use rotation, matchup, fouls, possessions, and shot quality for the next segment.
3. **Small H2H phase samples are weak.** A two-game Q2 acceleration pattern cannot control a current H1 direction.
4. **Minutes uncertainty is a distribution.** Do not use active/inactive as a full-workload binary.
5. **Blowout and garbage time are two-sided.** They change starters' minutes, bench pace, defence, and late scoring differently by contract.
6. **Late fouling and overtime are explicit tails.** Match the operator's inclusion rule.
7. **Rest is mechanistic.** Connect fatigue to pace, transition defence, shot quality, or minutes; no automatic Under/Over.
8. **Player props need role coherence.** Usage, minutes, teammates, defensive matchup, and stat opportunity must point in the same direction.
9. **Extreme spread size is not automatic safety.** For large mismatches, model opening separation, maximum-lead and closing-margin distributions separately. Rest/back-to-back, depth, bench quality, rotation intent, mercy/clock rules where applicable and garbage-time compression can move the final margin in opposite directions.
10. **Friendly halves can be different games.** Preparation matches require starter, bench and closing-lineup mixtures. A strong first half does not validate the full-game side when creators, minutes and late-game roles are deliberately rotated.
11. **Mismatch total and margin share a state tree.** Favourite offensive dominance can lift both margin and total, while underdog suppression can lift margin and lower the total. Derive both branches from the same possession/lineup simulation instead of treating an extreme handicap and an Under as independent safety plays.
12. **Current roster regime must be reconciled explicitly.** A missing rim protector, rebound anchor, primary creator or closer changes minutes, paint deterrence, rebounding, turnover pressure and closing-lineup quality. Old H2H and cover counts remain priors and cannot retain a high evidence grade unless the card explains why the present replacements preserve the old mechanism.
13. **Regulation and overtime attribution is exact.** Settle under the operator's endpoint, then report whether the threshold was already crossed in regulation. Do not describe an Over/Under miss as overtime-caused when regulation alone settled it.
14. **Rest is segmented, not a full-game scalar.** When a back-to-back/travel/fatigue branch is material, estimate its first-half versus second-half effect on transition defence, turnovers, defensive rebounding, shot quality, foul/bonus exposure and closing-lineup probability. If the card names a supported late-fatigue failure path, reconcile it with the side rank before issue.
15. **Low total can coexist with favourite blowout.** In depleted-roster or depth mismatches, model the underdog scoring floor and favourite defensive suppression separately from pace. An Under centre does not make the extreme underdog spread safe.

## 5. Live state

Store score, quarter/clock, possession estimate, lineups on court, fouls/bonus, timeouts, rotations/minutes, shot profile, turnovers, offensive rebounds, injuries, and current pace. Rebuild remaining possessions and each later segment independently.

## 6. Sources and settlement

- Official league match centres and play-by-play control state/final.
- Official injury reports and team releases control availability.
- The [NBA statistics glossary](https://www.nba.com/stats/help/glossary) controls NBA definitions; use the equivalent official competition source elsewhere.
- Reputable play-by-play/tracking sources may support lineup and shot-quality features after coverage checks.

Settle from the official final and named statistic provider, preserving regulation/OT and phase boundaries.

## 7. Upcoming-game research sequence

1. Verify league/rules, regulation/OT terms, phase and statistic provider; freeze the complete candidate slate.
2. Retrieve official injury/availability status and likely starters before process history. Recheck the official release and confirmed lineup near tip.
3. Estimate active/start probabilities, minutes/lineup stints and replacement tree, then possessions, per-possession shot/FT/turnover/rebound outcomes and matchup effects.
4. Generate lower, central, shooting-variance, foul/late-foul, blowout and OT branches. Phase targets use their own remaining rotations and possessions. Material rest/travel effects are segmented by half and mechanism rather than applied as one full-game scalar.
5. When current roster evidence conflicts with old H2H/cover history, show the baseline/current-regime mixture and make the spread ranking explain why the named separation branch is or is not subordinate.
6. Derive team scores, winner, total and margin from the joint game object. Player props use a linked `participation × minutes × usage/opportunity × rate` target, not team score alone.

Official league/team sources control current facts; official metric glossaries and audited play-by-play/tracking sources control their defined fields. Query/reference sites may cross-check trends but never override injuries, starters, rules or the operator's price.
