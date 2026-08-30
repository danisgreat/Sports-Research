# Rugby league / NRL analysis rules

Status: **ACTIVE**
Effective: **2026-08-30**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Numerical training specification: **NTS-2026.08.25-v0.2 — design only; no rugby-league model is fit**

This file covers rugby league. Rugby union and rugby sevens are different codes and are governed by `RULES_RUGBY_UNION.md`; their data and scoring populations must not be pooled with rugby league.

## 1. Identity and contract

Resolve NRL, NRLW, Super League, reserve-grade, international, or another league competition; current laws/interchange rules; venue; regulation/golden-point/draw terms; team/player/phase statistic; and exact settlement provider. Do not call a Super League fixture NRL.

## 2. High-value inputs

### Participants and roles

- Confirm the official team list, final match-day reduction/release, starting 13, bench, late changes, and current competition interchange/activation rules.
- Identify the spine: fullback, five-eighth, halfback, hooker; primary goal kicker; playmakers and replacement tree.
- Estimate minutes, interchange, carries, tackles, kicking role, goal-kicking share, and position changes.
- Translate absences into set organisation, field position, ruck speed, edge defence, and conversion.

### Possession and field position

Use opponent-adjusted:

- possessions/sets and set starts;
- completion and error rates;
- metres/set and post-contact metres;
- play-the-ball/ruck speed where defined;
- line breaks, tackle breaks, offloads and kick returns;
- repeat sets, penalties, six-again, field position and goal-line entries;
- tries, try location, goal conversion, and defensive conversion;
- tackle load and interchange fatigue.

Raw points and cover history do not substitute for possession and field position.

### Context

Record rest, travel, turnaround, venue, match-window weather, surface, ladder/finals incentives, referee only with current relevant data, and verified tactical changes. Wet conditions can reduce handling but also create short fields and fatigue; no automatic Under.

## 3. Model

Exposure units are possessions/sets, set starts, field position, carries/tackles, line-break opportunities, tries, and conversions. Estimate territory and try opportunities first, then finishing and goal-kicking. Use a joint score/margin distribution with sin-bin, intercept/short-field, fatigue, and golden-point tails.

Derive winner, handicap, total, phase, and player contracts from the same distribution.

For numerical training, compare empirical/simple set-and-try baselines with a sets → field position → goal-line entry → try → conversion A2 simulator. It samples completion/errors, repeat sets, penalties/six-again, ruck/fatigue, line breaks, sin-bin/send-off, kicker and golden-point states while preserving both teams' possession dependence. Direct score or boosted-distribution models are challengers only after discrete-support, scoring-combination, population and calibration checks. Elo is contextual strength, not the scoring engine. Every contract integrates the same joint score distribution. All candidates remain unfit and unvalidated.

## 4. Structural controls

1. **Spine is a regime variable.** Rebuild set organisation, kicking, and edge attack for a changed spine.
2. **Possession imbalance drives dependence.** It can raise favourite margin while suppressing the underdog contribution; total direction remains scenario-specific.
3. **Recent cover rates are diagnostic.** Current participants, set distance, line breaks, and field position control.
4. **Wet weather is bidirectional.** Trace handling errors, kicking, short fields, ruck speed, and goal-kicking.
5. **Goal-kicker state matters.** Tries and conversions are dependent; record the current kicker and replacement.
6. **Sin-bin/send-off is an explicit tail.** Rebuild remaining possessions when it occurs live.
7. **Winner and handicap differ.** Model separation, narrow result, and golden-point branches.
8. **League and union cannot be pooled.** Laws, scoring, possession and settlement differ.
9. **Motivation is conditional.** Tie it to selections, interchange, tempo or risk.
10. **No current calibration claim.** P-039 is one NRL event and cannot establish model performance.
11. **Current defensive regime and spine return require a mixture.** When a recent conceded-points/line-break/field-position collapse or a key spine return conflicts with season averages and old H2H, freeze baseline and current-regime branches with named mechanisms. Weather and historical close scores cannot silently suppress a credible separation tail.
12. **Blowout branch is possession-native.** Stress repeated short fields, missed-tackle/line-break clusters, spine-led set control and conversion quality before ranking a broad Under or underdog cushion. One realised blowout creates a candidate, not an automatic coefficient.
13. **A total can clear through one team.** For every broad Under, test a favourite-only scoring branch in which the underdog remains suppressed but errors, short fields, repeat sets, line breaks and conversions let the favourite carry the total over the line.
14. **Low total does not imply close margin.** A territorial/completion/defensive-control state can produce a multi-score favourite cover while the match stays Under. Margin and total must be queried separately from the joint score tree.
15. **Halftime does not freeze full-time separation.** Carry score, possession/set starts, field position, completion/error state, spine function, bench/interchange usage, defensive workload and conditions into the second-half branch. A competitive first half can become a favourite cover through opponent suppression and fatigue without creating a high total.

## 5. Live state

Store score, clock/half, possession/set and tackle, field position, repeat-set/six-again, penalties/errors, line breaks, sin bins/send-offs, injuries, interchanges, kicker, and current ruck/territory. Recompute remaining sets and field-position distribution.

## 6. Sources and settlement

- NRL official team lists, late mail, match centres, judiciary and [game/statistics resources](https://www.nrl.com/operations/the-game/) control NRL.
- Official competition sources control Super League, NRLW, internationals, and other leagues.
- Government weather services and venue reports control conditions.

Settle from the official final and named provider, preserving regulation/golden-point and exact player-stat definitions.

## 7. Upcoming-game research sequence

1. Freeze rugby-league competition/laws, regulation/golden-point/draw terms, player/stat provider and candidate slate.
2. Retrieve official team lists, injury/casualty status, reductions/late mail, starting 13, bench, spine and goal kicker. Refresh at the current competition's final-update deadline and immediately before kickoff.
3. Model player minutes/interchange, sets and set starts, field position/tackle state, completion/errors, ruck/fatigue, goal-line entry, try location, conversion, penalties/six-again, sin-bin and golden-point tails.
4. Possession dominance can increase margin while reducing the opponent contribution; total direction must be scenario-derived.
5. Before ranking an Under or underdog cushion, calculate one explicit favourite-only blowout path and one low-total separation path; record which mechanisms and score families make each credible.
6. Derive joint score, winner, total and handicap from the same score object. Player props use position, minutes, carries/tackles/kicks or goal-kicking exposure and exact provider definitions.

Official competition sources own current teams/state/rules. Historical archives are cross-check/research lanes and cannot override late mail or enter H0 before field-level approval.
