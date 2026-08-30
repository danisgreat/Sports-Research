# Soccer analysis rules

Status: **ACTIVE**
Effective: **2026-08-30**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Numerical training specification: **NTS-2026.08.25-v0.2 — design only; no soccer model is fit**

## 1. Identity and contract

Resolve competition, season/rules era, leg/tie state, venue, regulation versus extra time/penalties, winner versus qualify/advance, draw-no-bet/double-chance terms, team/game total, corners/cards, and player statistic. Friendlies, youth, reserve, senior competitive matches, and two-leg ties are different populations.

## 2. High-value inputs

### Participants and minutes

- Confirm starting XI, goalkeeper, bench, formation, material absences, expected minutes, rotation, set-piece and penalty takers.
- Model the replacement and substitution phase. In friendlies, separate starting-XI and mass-substitution regimes.
- Use current role/system fit rather than club reputation.
- In sparse local, youth, reserve, inaugural, or otherwise low-information competitions, unresolved official XIs/goalkeepers plus weak role continuity cap side, double-chance and handicap rows at `FORCED RANK`/`MEDIUM-LOW`. Historical team records do not remove participant uncertainty.

### Goal process

Use opponent-adjusted:

- dynamic attack and defence strength;
- shots and xG for/against;
- shot location/quality and set-piece xG;
- post-shot/goalkeeper quality with shrinkage;
- field tilt/territory and pressing where defined;
- expected possession and score-state tactics.

Recent goals, finishing streaks, and clean sheets are outcomes. Separate creation, finishing, goalkeeping, and opponent quality.

### Corner process

Corners require their own model:

- team corners for/conceded;
- crosses and blocked crosses;
- end-line entries and defensive clearances;
- set plays and shot-block locations;
- current score/leading/trailing state;
- substitutions and width.

Shots, possession, xG, box touches, or class do not directly imply corners.

Before a corner contract can receive `LEAN` or `SUPPORTED`, the card must contain the available target-event chain: expected corner exposure, team for/opponent-conceded rates, direct width/cross/block/end-line/clearance/set-play evidence, score-state branches, and the exact settlement provider/definition. If a decisive layer is missing, record its missingness and cap the row at `FORCED RANK` with LOW or MEDIUM-LOW evidence.

### Player shot-on-target process

For player SOT contracts, decompose the event rate into:

`expected minutes × opponent-adjusted shots per minute × role/box-shot share × on-target conversion`.

Adjust for starting/substitution probability, teammate shot competition, formation and set-piece role, opponent shot suppression and likely score state. A recent SOT streak is diagnostic only. Freeze whether blocked shots, woodwork and deflections count under the named provider; provider definitions are not interchangeable.

### Context

Record rest/travel, congestion, table/tie incentives, venue and home effect estimated in the relevant league/era, match-window weather, referee only when relevant, and verified tactical changes. Old H2H is descriptive unless lineup/coach/system continuity is meaningful.

## 3. Model

Exposure units are expected minutes, possession/attacking sequences, shots/xG events, set pieces, and corner-causing events. Use dynamic hierarchical attack/defence strengths and a score-dependence model such as a validated Dixon–Coles/bivariate framework rather than unadjusted recent-goal Poisson.

Maintain linked goal, shot/player-event, corner, and discipline processes through shared possession, lineup, and score state. Derive winner, handicap, total, BTTS, and team total from the goal process; derive shots, assists, cards, corners, and other player/event contracts from their corresponding process while preserving cross-process dependence.

For two-leg ties, use an explicit pregame mixture over at least: no early goal, early goal by the aggregate-trailing team, early goal by the aggregate-leading team, and material dismissal/injury branches. Each branch updates qualification pressure, attacking exposure, counterattack space and the remaining goal/corner distributions; a static aggregate adjustment is insufficient.

For numerical training, goal candidates begin with empirical and independent-Poisson baselines, then challenge them with Dixon–Coles/bivariate/dynamic hierarchical and state-simulation forms. Corners retain separate Poisson, negative-binomial and compound/cluster-aware candidates; player SOT retains minutes × shot-rate × on-target components. Boosted or quantile methods estimate these underlying event distributions, never one unrelated classifier per bookmaker line. Shared possession/score state may link processes, but goals cannot substitute for corner or SOT labels. All candidates remain unfit and unvalidated.

## 4. Structural controls

1. **Regulation winner and advance are distinct.**
2. **Rotation changes effective strength.** Class gap is a prior, not protection.
3. **Draw-band discipline.** A non-loss contract can be strong while the outright winner remains weak.
4. **Corners are not dominance proxies.** Require direct corner-causing evidence and, live, the remaining required rate.
5. **Leading-state branch.** A team converting early may reduce later attack/corner demand; a trailing side may increase it.
6. **Red cards are asymmetric.** Rebuild both teams' possession, shot, and score-state distributions.
7. **Friendlies are phased.** Starting XI quality cannot be projected through mass substitutions.
8. **Set-piece and keeper extremes shrink.** Do not assume recent conversion or shot-stopping persists unchanged.
9. **Weather is mechanism-specific.** Wind/rain can alter passing, crossing, shooting, surface speed and set pieces in different directions.
10. **Niche-stat settleability is post-final.** Predeclare likely source; retry official/data-partner sources after final before UNSETTLEABLE.
11. **Derivative completeness gate.** Missing target-event exposure/rate/opponent/context or provider definition prevents a LEAN/SUPPORTED label.
12. **Early aggregate-goal regime switch.** In a two-leg tie, an early goal by the trailing side makes the tie materially more live; rebuild both teams' scoring and transition exposure instead of retaining the original low-tempo corridor.
13. **Sparse-participant side cap.** Weak competition coverage plus unverified XIs/keepers is a side-confidence limit, especially when both teams show wide defensive/error tails.
14. **Corner share and corner total differ.** A chasing side can win the corner race through width and territory while the match remains below a total-corner line; derive both from the corner process rather than transferring one direction to the other.
15. **Current competition and lineup outrank inherited class only after reconciliation.** Domestic scoring strength, reputation and old H2H are priors. Current European/international role, confirmed attackers/keepers, tactical shape and competition incentives form a separate regime branch under the general audit.
16. **Friendly participant phase must be observable.** For friendlies or preseason matches, record the official XI and any credible substitution/minutes plan. If the plan is unavailable, widen second-half scoring/side tails and cap any participant-dependent side or total thesis rather than projecting the starting XI for 90 minutes.
17. **Official placeholder conflict is not a final.** A zero-filled or frozen official match-centre shell that contradicts current reports cannot settle score, corners or other fields. Preserve the conflict, seek an official correction/report and apply the general two-source provisional fallback field by field.
18. **Winner endpoint must be frozen and settled literally.** Regulation winner, eventual match winner and advance/qualify are different. An extra-time winner cannot be counted as a correct regulation-winner call, and a descriptive “potential winner” must name its endpoint before issue.
19. **Schedule conflict survives until field-owner resolution.** A current aggregator consensus can support a provisional queue time, but it cannot erase a conflicting earlier date. Keep the event identity/schedule quarantined, refresh the competition/association source, and withhold prospective-performance eligibility until the actual start/final chronology is resolved.
20. **Early-goal rank reconciliation is mandatory.** Before 1H Over 0.5 outranks its Under, reconcile recent early goals and win streaks against opponent 0–0-HT frequency, current chance-creation mechanism, rest/congestion, weather/surface, venue, confirmed XI/keeper and substitution uncertainty. A streak or market direction without a persistent exposure/rate mechanism cannot control the order.
21. **Late scoring and corners do not backfill first-half evidence.** A late penalty, long-range outlier or chasing corner sequence belongs to its phase/state branch. It cannot justify an earlier first-half Over or team-corner rank after the fact.
22. **The bench has expected-minute value.** A starting-XI asymmetry is not a 90-minute asymmetry. Assign material substitutes entry probabilities, expected minutes, role and likely score-state use; carry the resulting attacking/defensive change into the regulation score tree before ranking a side.
23. **Early-season droughts require aggressive shrinkage.** Through the first two or three matches, zero goals, perfect clean sheets and 0%/100% conversion are unstable outcomes. Separate chance creation, shot quality, finishing and goalkeeping; pool toward current roster/manager and competition priors, widen the tail and cap a team-total or side that relies mainly on the tiny streak.
24. **Volume, allocation and result are different questions.** When global event suppression is stronger than the evidence for which team converts the limited chances, compare the full total and BTTS/team-total rows directly with the side. A low total can make a protected side fragile to one conversion rather than safer.
25. **Transition pressure can create goals and corners without possession.** Model counterattacks, width/end-line entries, blocked actions, set plays and trailing-state attacks directly. Low possession is not low attacking-event exposure, and an early goal must propagate into later shot, goal and corner states rather than remain isolated in a first-half branch.

## 5. Live state

Store score, clock/stoppage, red/yellow cards, substitutions, formation/tactical state, shots/xG when available, set pieces/corners, and who is chasing. Recompute remaining goal and corner events; do not extrapolate the first-half rate.

## 6. Sources and settlement

- Official competition match centres, lineups, disciplinary records, gamebooks and finals control.
- Club official sources support availability and planned rotation.
- Reputable Opta-derived or defined xG providers may support process features after coverage/definition checks.
- Government weather services and official venues control conditions.

Settle regulation, extra-time, advance, corners, cards, and player statistics under the exact contract and named official provider.

When an official result is not recoverable, two independent high-quality current sources may support a provisional field under RULES_GENERAL. Aggregator agreement does not make niche statistics settleable when their provider/definition was not frozen.

Method references:

- [Dixon and Coles, Modelling Association Football Scores (1997)](https://doi.org/10.1111/1467-9876.00065).
- [Stats Perform/Opta event definitions](https://www.statsperform.com/opta-event-definitions/) for shots, blocked shots and shots-on-target semantics.
- [Forecasting corner kicks with a compound Poisson distribution](https://arxiv.org/abs/2112.13001) as evidence that corner counts may be overdispersed and clustered; Poisson, negative-binomial and cluster-aware forms remain numerical challengers, not active defaults.
- [Player-level shot-output forecasting](https://escholarship.org/uc/item/21j688ph) as supporting research for separating expected minutes from per-90 shot rate; it does not establish an active coefficient or probability model here.

## 7. Upcoming-game research sequence

1. Freeze competition, tie/leg state, regulation/extra-time/penalty/advance terms, provider metric and full candidate slate.
2. Retrieve official squad/availability/rotation evidence, then confirmed XI, goalkeeper, formation, bench and set-piece/penalty roles; refresh immediately after lineups and just before kickoff.
3. Build the regulation goal process from dynamic attack/defence, shot/xG/set-piece/keeper and score-state mechanisms. For early-goal rows, explicitly reconcile the current opponent/rest/weather/XI evidence against any streak. Keep extra-time/advance as linked but separate endpoints.
4. Build corners, cards and player SOT from their own exposure/rate/provider definitions. Goals, possession, shots or class may be context, but never substitute for the settled target.
5. Derive 1X2, draw-no-bet, double chance, totals, BTTS and handicaps from the regulation goal grid when their terms match. Player/niche outputs retain separate target distributions and dependence links.

Official competition/club sources own current facts. StatsBomb Open Data is a selective historical candidate; Opta or another provider owns only its own event definitions. Never merge xG or event labels across providers without a versioned reconciliation.
