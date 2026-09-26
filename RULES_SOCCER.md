# Soccer analysis rules


> **2026-09-12 operational correction:** The dated section at the end of this file and RULES_GENERAL section 16.9 control over conflicting older probability, coupling and source claims.


> **`METHOD.md` is now the primary mandatory read (v4.0 comprehensive overhaul, 2026-09-06).** This file remains the full sport-specific reference: its `SFA-<SPORT>` algorithm and competition-rules section (`§9`/`§10`/`§11`) are consulted in full when forecasting this sport; `METHOD.md` states the cross-sport process once.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
> **Current cross-sport authority — MDS-2026.09.19-v4.3 / CR-2026.09.21-3:** this sport module inherits the reconciled all-sports controls, including three independent reliable event lineages, timezone-aware venue-local → `Australia/Melbourne` verification, terminal-state confirmation, market/fantasy source quarantine, and the current distribution-first ranking rules. Historical issued cards retain their own revision.


Status: **ACTIVE**
Effective: **2026-09-06 (v4.0 comprehensive overhaul — see METHOD.md and archive/audit_documents_implemented_2026-09-25/FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md)**
Method version: **MDS-2026.09.06-v4.0**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Executable algorithm: **SFA-SOCCER (§8) — instantiates GFA-2 in RULES_GENERAL.md §11**
Numerical training specification: **NTS-2026.09.02-v0.3 — design only; no soccer model is fit**
Sport and competition rules reference: **§9 → [LEAGUE_RULES_SOCCER.md](LEAGUE_RULES_SOCCER.md)** (added 2026-09-04) — the IFAB Laws of the Game, the shared competition variables (extra time, penalties, substitutions, VAR, points and tiebreak systems, promotion/relegation and playoffs), and a per-competition section for every one of the ~35 soccer competitions in the prediction logs. Broken out to its own file because a full treatment would be several times the length of this document.


<!-- LIVE-RULES-PAGE-2026-09-26 -->
## 0. Live rules — one page (consolidated 2026-09-26)

**Status.** This page consolidates everything in this file that is live on 2026-09-26: the numbered controls, SFA-SOCCER and the dated sections through 2026-09-25(e). It is a derived index. If it disagrees with the section it cites, the cited section governs and this page is corrected in the same pass. **Reading gate (C-READING-GATE, 2026-09-26):** read this page in full for every soccer card, then open each cited section the card relies on (and `LEAGUE_RULES_SOCCER.md` for the competition). Everything below §0 is the full reference and its history.

### 0.1 Blocking preconditions (§8.1)
| Gate | Requirement | If it fails |
|---|---|---|
| SO-P1 endpoint | Competition, leg/tie state, regulation / extra time / penalties / advance, and which endpoint each row settles on | Stop. Regulation winner, eventual winner and advance are different contracts (controls 1, 18) |
| SO-P2 participants | Confirmed XI, keeper, formation, **bench**, set-piece and penalty takers for both sides (ESPN `rosters[]` or the official club/league source), refreshed at freeze | Side, double-chance and handicap rows capped. `BENCH_NOT_RETRIEVED` ⇒ no full-match total or handicap at Rank 1 (September 6 override 2). `PROJECTED_BEAT_VERIFIED` needs the S-1 Rev 2 receipt |
| SO-P3 derivative provider | Exact provider and definition for corners, cards, shots | `UNKNOWN_DEFINITION`; the row cannot reach LEAN/SUPPORTED |
| SO-P4 schedule identity | Start confirmed by the competition or association when aggregators conflict | Identity quarantined |

**Settlement route at issue (controls 30, 32, 35, 36, 38, G-L14).** A corner or shot row names its route before it is ranked: EPL → the Premier League data API (pulselive, control 32); UEFA club competitions → UEFA matchstats (control 30); otherwise pre-register ESPN `wonCorners` (Opta lineage) or do not issue the row. On a knockout fixture, name the interval and settle from a record that exposes it (control 36).

### 0.2 Building the goal distribution
1. **Anchor.** EPL: the §7.3 reference (S-R1) and, for results only, `TEAM_BASELINE_P` (TB-1 has resolution for EPL results, **not totals**). Other competitions: `BASELINE_P` where derived, else `NOT_YET_DERIVED`. **Never transfer EPL rates to cups, lower tiers or other leagues (M12).**
2. **Four layers per side:** chance creation, shot quality, finishing, goalkeeping (SO-S2, control 27). Print shots, shots on target and xG beside goals per match (G-L7). A season rate predicts no better than the league constant, and the last game is 38% worse: form needs a named mechanism (S-R3, R-1).
3. **Cross-competition translation.** Print the source-league rate, the adjustment and the result for every cross-league or cross-division fixture (control 31). A clean-sheet run against weaker opposition widens the favourite-separation tail; it does not shift the centre (control 39). Early-season droughts shrink hard (control 23).
4. **Phases.** First and second halves are separate states, not a fixed fraction (SO-S3). Before any 1H Over 0.5 outranks its Under, print both teams' current first-half rates and 0–0-HT frequency and derive P(no 1H goal) ≈ e^(−λ) from both sides (control 20). Sibling phase lines come from **one printed phase distribution**. A phase Under at 0.80+ on U1.5 or lower states the modal count and P(phase = 2) (control 40).
5. **Bench and state.** The bench has expected-minute value (control 22). Early goals switch to leading/trailing-state branches that propagate into later goals and corners (controls 5, 12, 25). Red cards rebuild both sides (control 6).
6. **Knockouts.** Compare the exact competition/round/leg/aggregate population; there is no automatic knockout Under sign (control 28, L-064).
7. **Width.** The EPL total residual SD is 1.61. A goals-total width below about 1.37 names what the card knows (S-R3, C-WIDTH-BENCHMARK).
8. **One regulation score grid plus linked corner and player objects → every row** (SO-S7). Use `tools/card_math.py … --dist skellam` for margins.

### 0.3 Row rules
- **Where soccer's skill lives:** phase rows, low-threshold team totals, wide alternate totals, corners with their own chain, and protected sides. Main-line full-match totals are close to coin flips (the preferred side won 1 of 6 in one cohort): rank them honestly and never prefer them by default.
- **Disclosure thresholds (S-R2):** a first-half Under 1.5 above about 0.75, or a full-match Over/Under 2.5 above about 0.70, names its reason. These are not caps.
- **Single-team scoring rows above 0.80 without a confirmed XI** print the opponent-suppression and finishing-failure branches with mass (control 37).
- **Corners:** their own exposure → rate → opponent → score-state → provider chain, or they are capped (controls 4, 11, 14). A team-corner row missing its crossers recomputes the centre and gives the leading-state branch mass (control 33). A 3-game corner sample is width.
- **Winner labels:** print the draw mass beside any label under 50%, and the upset mass at or below 60% (control 3). A draw is a third terminal state (G-L19).
- **Cushions and double chances.** +k.5 rows print P(underdog wins) + P(draw) + P(loses by ≤ k) from a Skellam margin beside the EPL band. Underdog cushions went 8/13 at a stated 0.77. A "+0.5 / 1X" row is a **double chance**: 2/5 at about 0.73, so none is stated above 0.70 without the draw mass printed. Soccer +k.5 rows carry no RM-1 cushion penalty.
- **Contract must match mechanism.** One-sided creation supports a team target, not a full-match Over (control 26). Volume, allocation and result are different questions (control 24).

### 0.4 Ranking and track record
- Rank by RM-1 q; soccer's order is almost unchanged by it (1 of 35 held-out cards re-ordered).
- **Track record:** the strongest resolution of any sport. 143 decisions from 37 cards won 74.8% at 0.700 (Brier 0.170, resolution 0.036). The card-cluster calibration interval spans 0, so this is the strongest evidence rather than proof of skill. Rank 1/2 went 55 W / 17 L. Phase against full-game totals on the same cards: 30/36 against 27/41 (`C-PHASE-VS-FULL-TOTAL`, still TESTING). First-half Over 0.5 at Rank 1/2 lost four times.

### 0.5 Settlement (controls 34, 36, 41)
- Settle from a structured feed that carries shots, cards and minutes, never a narrative report. Copy red cards, penalties, keeper changes and weather stoppages with the minute and score, and say whether each target was already decided (controls 34, 41).
- Regulation versus extra time is exact (G-L16). Media corner counts are cross-checks only; both observed media conflicts were wrong by one (control 30).
- ESPN slugs: AFC Champions League Two is `soccer/afc.cup`; the AFC feed has no `Halftime` event, so reconstruct half-time from goal minutes (control 41).

### 0.6 Reference numbers (EPL 2025-26, `BASE_RATES_REGISTER.md` §7.3)
Goals mean 2.75; Over 1.5/2.5/3.5 0.789/0.550/0.284; draw 0.274; BTTS 0.561. First half: mean 1.19 (second half 1.56); P(≥1)/P(≥2)/P(≥3) 0.716/0.334/0.111. Corners mean 10.0 (SD 3.27); P(≥10) 0.563, P(≥11) 0.437. EPL only.

### 0.7 Withdrawn in soccer — never apply
The blanket corners Rank-1 cap (L-073, replaced by the coverage test L-081/G10.2); the automatic knockout Under sign; pseudo-tails; path-count categories; 40–60% bands; normalised-edge ordering; one-result response rules; any implication that a cushion determines the winner.

### Numerical shadow model (2026-09-26(c); never a card input)

`python tools/sport_models.py shadow --league <epl|laliga|bundesliga|seriea|ligue1|…> …` (`C-SPORT-SHADOW`). A1 is Poisson attack/defence ratings with linked halves. On 2022-23 to 2025-26 it beat the league baseline on results and margins in all five top leagues, and TB-1 on EPL results. It did **not** beat the baseline on totals in the EPL, Serie A or Ligue 1, nor on BTTS or first-half totals outside La Liga. Dixon–Coles added nothing. Record it after the freeze and before the start; it is never printed, ranked or cited on a card, and a promotion needs its 150-row review and your instruction (`RULES_GENERAL.md` §"2026-09-26" (e), (k); `research/sport_models_2026-09-26/README.md`).

### 0.8 Control index (full text in §4 and the dated sections)
1 regulation winner ≠ advance · 2 rotation changes strength · 3 draw-band discipline (draw/upset mass) · 4 corners are not dominance proxies · 5 leading-state branch · 6 red cards asymmetric · 7 friendlies phased · 8 set-piece/keeper extremes shrink · 9 weather is mechanism-specific · 10 niche-stat settleability · 11 derivative completeness · 12 two-leg early-goal regime · 13 sparse-participant side cap · 14 corner share ≠ corner total · 15 current competition v inherited class · 16 friendly participant phase · 17 placeholder conflict is not a final · 18 winner endpoint literal · 19 schedule conflict · 20 early-goal reconciliation with both sides' first-half rates · 21 late events don't backfill first half · 22 bench minutes · 23 early-season shrinkage · 24 volume/allocation/result · 25 transition pressure · 26 contract matches mechanism · 27 territory/chance/scoreboard separate · 28 exact knockout population · 29 prior leg is context · 30 UEFA matchstats route · 31 cross-competition translation · 32 EPL data API route · 33 team-corner generators · 34 disruption facts · 35 league corner route table · 36 period scope on knockout derivatives · 37 single-team rows > 0.80 without XI · 38 AFC routes · 39 cross-league defensive translation · 40 sibling phase lines from one distribution · 41 settle from a structured feed. References: S-R1 EPL rates · S-R2 disclosure thresholds · S-R3 recency and width.


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
26. **Contract choice must match the mechanism.** Distinguish high combined scoring, one-team attacking dominance and high chance creation. A full-match Over requires enough conversion and opponent/team contribution under its exact line; if the evidence is mainly one-sided, prefer a supplied, research-complete team target or lower the full-total evidence rather than transferring the mechanism.
27. **Territory, chance quality and scoreboard dominance are separate states.** Possession, shots and corners diagnose different processes. Before a side or total is promoted, explain how territory becomes shot quality and conversion while retaining keeper and transition-counter branches.
28. **Condition on the exact knockout population; do not assume a universal negative scoring sign.** Retrieve competition/round/leg/aggregate-state history and compare its scoring and opportunity environment with relevant league evidence. Use a direction only when those data and current mechanisms support it; missing or sparse knockout evidence is uncertainty, not an automatic Under or downward centre shift. Keep the pregame regime separate from control 12’s post-goal change and from card/injury transitions. L-064 is narrowed to this process requirement; any signed adjustment remains a prospective candidate.
29. **A prior leg or a recent head-to-head result is context, not a cause.** Per RULES_GENERAL.md §11.3E (G17.1), a team's result in the first leg of the same tie, or in its immediately preceding match, may support a "response"/"bounce back" lean only with a named, currently active mechanism (a specific tactical change, a returning player, a disclosed rotation consequence); otherwise it carries no directional weight. Record the series/aggregate-state block from RULES_GENERAL.md §5 for every two-leg tie.


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


## 8. SFA-SOCCER — sport forecast algorithm


Algorithm ID: `SFA-SOCCER`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL.md §11) with soccer content. Process composition only; no fitted weight, scenario weight or published probability is introduced. Senior, reserve, youth, women's, friendly and inaugural-competition populations are separate, and goals, corners, cards and player events are separate processes throughout.


### 8.1 Blocking preconditions


| Precondition | Requirement | Failure output |
|---|---|---|
| `SO-P1` competition and endpoint | Competition, leg/tie state, regulation, extra-time, penalties, advance/qualify terms, and which endpoint each supplied row settles on | `GATE-TARGET` failure. Regulation winner, eventual winner and advance are different contracts |
| `SO-P2` participants | Confirmed starting XI, goalkeeper, formation, bench, set-piece and penalty takers for both sides, re-handshaken at G31 | Unresolved XI or keeper caps side, double-chance and handicap rows at `FORCED RANK` / `MEDIUM-LOW` |
| `SO-P3` derivative provider | For corners, cards, shots or shots-on-target: the exact provider and definition, including blocked-shot, woodwork and deflection treatment | `UNKNOWN_DEFINITION`; the row cannot reach `LEAN` or `SUPPORTED` |
| `SO-P4` schedule identity | Verified start date/time from the competition or association when an aggregator conflicts | Event identity stays quarantined; prospective eligibility withheld |


### 8.2 Exposure chain


Goals, corners and player events each run their own chain. They share possession, lineup and score state but never share a rate.


| Step | Output |
|---|---|
| `SO-S1` | Expected minutes by player, including substitution phase, entry probability, role and likely score-state use |
| `SO-S2` | Dynamic opponent-adjusted attack and defence strength, decomposed into chance creation, shot quality, finishing and goalkeeping as four separate layers |
| `SO-S3` | Regulation goal process by phase: first half, second half, and stoppage, with score-state tactics |
| `SO-S4` | Corner-causing event process: width, crosses and blocked crosses, end-line entries, defensive clearances, set plays, shot-block locations, and score-state exposure |
| `SO-S5` | Player event process: `expected minutes x opponent-adjusted event rate x role share x conversion`, with teammate competition |
| `SO-S6` | Discipline and dismissal process, with the asymmetric rebuild that follows a red card |
| `SO-S7` | One regulation score grid plus linked corner, card and player objects, with cross-process dependence preserved |


### 8.3 Mandatory branch set


| Branch | Content |
|---|---|
| `SO-B1` | Central creation with central finishing for both sides |
| `SO-B2` | Creation-strong, finishing-weak state: territory and chances without conversion — the one-nil dominance family |
| `SO-B3` | Early-goal state, by each side separately, with the tactical rebuild that follows |
| `SO-B4` | Trailing-state chase: the conceding side's raised shot, cross, corner and set-play exposure |
| `SO-B5` | Leading-state control: the leading side's reduced attacking demand |
| `SO-B6` | Substitution-phase state: bench entries changing attacking and defensive quality after roughly the hour |
| `SO-B7` | Dismissal or injury asymmetry state |
| `SO-B8` | Two-leg regime switch where applicable: no early goal, early goal by the aggregate-trailing side, early goal by the aggregate-leading side |


### 8.4 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Full total and BTTS | Regulation score grid, both teams | Enough conversion **and** opponent contribution under the exact line; one-sided creation does not supply this |
| Team total | Team marginal | Own creation and conversion against the confirmed opposing keeper and defence |
| 1X2, double chance, draw-no-bet, handicap | Score grid with matching endpoint | Which side receives limited scoring mass, not merely that the total is low |
| First-half or phase total | The phase's own state from `SO-S3` | Opponent scoreless-at-half base rate, rest, weather, confirmed XI and keeper — reconciled explicitly against any streak |
| Total corners and team corners | `SO-S4` only | Corner share and corner total are different questions; a chasing side can win the race inside a low total |
| Player shots or shots on target | `SO-S5` only | Start probability, teammate competition and the frozen provider definition |


### 8.5 Kill-path library


| Kill path | Defeats | Evidence origin |
|---|---|---|
| Heavy one-team chance creation converting once against a passive opponent | A full-match Over built on dominance | C-PL9-SOC-MECHANISM-CONTRACT, §4 control 26 |
| A trailing side's sustained chase producing width and corners | A home or team corner Under built on expected control | C-PL8-SOC-TRANSITION-EVENTS, §4 controls 5 and 25 |
| Transition and counterattack scoring without possession | A total or side built on possession share | §4 control 25, C-PL8-SOC-TRANSITION-EVENTS |
| A two- or three-match scoreless or clean-sheet run treated as a regime | A low-total or team-total row through the opening rounds | C-PL8-SOC-EARLY-SHRINK, §4 control 23 |
| An opponent with a strong scoreless-at-half base, on short rest, in rain, with no official XI | A first-half Over ranked on a scoring streak | C-PL7-SOC-EARLY-RANK-RECON, §4 control 20 |
| Bench entries changing effective strength after the hour | A side ranked on a starting-XI asymmetry | §4 control 22; local lesson `M4-L03` in PREDICTION_MINI_LOG_4.md §E |
| Global suppression that is correct while the allocation is wrong | A protected side inside a low total, where one conversion decides the match | C-PL8-SOC-VOLUME-ALLOC, §4 control 24 |
| An early goal by the aggregate-trailing side reopening a tie | A static aggregate-adjusted low-tempo corridor | §4 control 12, C-PL4-SOC-AGG-EARLY-GOAL |
| A goal mechanism reused as corner evidence | A corner row lacking its own direct chain | L-007, L-023, §4 controls 4 and 11 |
| Knockout-stakes risk-aversion suppressing tempo below the teams' open-league goal rate | An early-goal or total-Over row anchored to league/H2H scoring frequency in a cup/playoff/two-leg fixture | §4 control 28, CL-P267-01 |
| A prior leg or recent result used as a "response" cause with no named current mechanism | A bounce-back/reversal lean lacking G17.1 support | §4 control 29, RULES_GENERAL.md §11.3E (G17.1) |


### 8.6 Sport ordering overrides


1. A corner, card or player row lacking any layer of its own chain, or lacking a frozen provider definition, may not exceed `FORCED RANK` and may not occupy a top slot above an opposing full-target contract.
2. `align` is `PROXY` for any row justified by possession, territory, shots or class rather than by the settled event. `PROXY` rows sort below `PARTIAL` rows at G24 key 1.
3. Early-goal and first-half rows require the full G17 reconciliation before they can outrank their complement.
4. Late scoring, a late penalty or a chasing corner sequence belongs to its own phase branch and may never be used to backfill an earlier phase row.
5. Recent goal counts, clean-sheet runs, finishing streaks and old head-to-head are `E — diagnostic only`.


### 8.7 Pre-issue checklist


1. `SO-P1`–`SO-P4` status printed, with XI and keeper release status.
2. Competition and matchup goal baseline stated before any line.
3. Creation, finishing, goalkeeping and opponent quality separated in writing.
4. All eight `SO-B*` branches represented; component budget solved at every aggregate line.
5. Corner rows carry their own exposure, rate, opponent, score-state and provider layers, or are capped.
6. Kill-path rows selected from §8.5 and reconciled against the issued order.
7. Winner endpoint named literally for the potential winner and every side row.
8. XI, keeper, weather and state refreshed at G31 before the view is appended.
9. Recency block complete per §8.8: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
10. Environment block complete per §8.9: Match-window wind, rain and surface state recorded; score-state splits retrieved for the corner and shot rows.
11. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §8.10 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
12. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
13. Separation budget (G20.1) solved for every margin, handicap and cushion row by half, with the post-sixtieth-minute substitution and trailing-state window held separately.
14. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
15. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: a late goal from a chasing or a game-managing state.
16. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.
17. Streak persistence-versus-reversion audit (G17.1) recorded for every Under/Over or scoreless run and for any prior-leg/series "response" lean; for a knockout/cup/two-leg fixture, control 28's exact-regime comparison and supported-direction audit completed before any early-goal row is ranked.


### 8.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL.md §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Chance creation | Shots and expected goals for and against, opponent-adjusted, split home and away |
| Finishing and goalkeeping | Goals against expected goals, for and against, held separately from creation |
| Phase output | First-half goals for and against, and how often the first half finished scoreless |
| Corner process | Corners won and conceded, with crosses and end-line entries where the provider defines them |
| Decision-driving players | Each player's own last 5/10/15/20 appearances: minutes, shots, shots on target and role |


**Head-to-head continuity.** Continuity means the same managers, a comparable XI and the same competition tier. A head-to-head record spanning a managerial change or promotion fails continuity.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 8.9 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL.md §11.3C). Venue classification for this sport is normally **OUTDOOR unless the venue has a closed roof**.


| Field | Use in this sport |
|---|---|
| Wind speed, gusts and direction | Crossing, set-piece delivery and long passing; resolved against stadium orientation |
| Hourly precipitation | Surface speed, handling and set-piece behaviour; no automatic total direction |
| Temperature | Congestion and substitution timing in heat |
| Surface and pitch state | Official venue source, including hybrid or artificial surfaces |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 8.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor the first-half Over 0.5 line on the competition frequency of a scoreless first half, and full totals on the competition goal environment. A first-half goal line and a team-total Under are far apart before any analysis and must not be ranked as if they started level.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Set-piece and penalty takers | Named for the confirmed XI, with the replacement if that player is substituted |
| Referee assignment | Cards and penalties only, conditional and only with current data |
| Rest days and travel since the last fixture | Entered through minutes and rotation, not as a label |
| Score-state splits | Shot and corner rates when level, leading and trailing, which is what `SO-B4` and `SO-B5` actually need |


## 9. Sport and competition rules reference


Added 2026-09-04. The IFAB Laws of the Game, the shared competition variables that decide settlement (extra time, penalties, substitution regimes, VAR, points and tiebreak systems, promotion/relegation, playoff/liguilla/split formats, foreign-player limits, points deductions), and a dedicated section for every soccer competition in the prediction logs — Premier League, Carabao Cup, Bundesliga, 2. Bundesliga, LaLiga, Serie A, Coppa Italia, Eredivisie, Jupiler Pro League, Danish Superliga, DBU Pokalen, Championnat National, Brasileirão Série A, Argentine Liga Profesional (and Primera C / reserve fixtures), Roshn Saudi League, Chinese Super League, Chinese FA Cup, Egyptian Premier League, Israeli competitions, Kazakhstan Premier League, Armenian Premier League and Cup, Uzbekistan Pro League, MOL Cup, the Sikkim S-League, NWSL, MLS NEXT Pro, Liga MX and Liga MX Femenil, Leagues Cup, the UEFA club competitions (Conference League, Women's Champions League, Women's Europa Cup), CONMEBOL Libertadores, the FIFA Intercontinental Cup, and the club friendlies (KCC Pre-Season Cup, Coupang Play Series, ASEAN club competition) — all in **[LEAGUE_RULES_SOCCER.md](LEAGUE_RULES_SOCCER.md)**.


That file is the reference for `§1` identity (competition, leg/tie state, regulation vs extra time/penalties, advance vs win) and `§6` settlement. It does not change `SFA-SOCCER`. Its **maintenance note** carries the season-boundary rules-currency check and the new-competition onboarding requirement (RULES_GENERAL.md §3, `G2`): the August restart of the European leagues, and any new season / edition elsewhere, triggers a re-verification of the IFAB Laws in force plus the competition's format, substitution/VAR/foreign-player rules and any points deductions before the first card; a new soccer competition must be fully documented there before it is forecast.


## September 5 settlement learning — prospective SFA amendment


P-233–P-235 demonstrate field-specific settlement: original independent reports can corroborate goals/halves without controlling corners. Keep corner count, provider definition and operator action separate; do not transfer authority from goals to corners. A final/half score cannot resolve P-126's event/rescheduling conflict or P-178's missing trusted corner endpoint.


P-234's 0–0 first half occurred after an early goalkeeper dismissal; the later winning goal was a penalty, and both sides eventually had a dismissal. These are score-state/participant transitions, not clean evidence that every knockout starts slowly. Control 28 is narrowed to competition/round/aggregate conditioning with a sourced direction; the prior automatic negative sign is retired. Red cards are bidirectional total mechanisms: record which side loses which role, the score, time, replacement and opponent response, without a universal Over/Under rule.


P-233's second and third goals were late, so a 3–1 final is not proof of uniformly dominant scoring. P-235's Port scoring success did not establish Shandong BTTS. Retain separate team contribution and phase budgets (L-037/L-039/L-043). Goal-row upgrades do not count as new events or numerical test completions.




Full evidence and frozen-card comparisons: [September 5 audit](archive/audit_documents_implemented_2026-09-25/COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 5(b) settlement learning — P-294–P-305 second continuation


**`P-302` (Newcastle United vs Bournemouth) — L-073, corners Rank-#1 cap promoted.** The card ranked `Bournemouth Over 2.5 team corners` at #1 (already `FORCED RANK`/`MEDIUM-LOW` evidence). Post-match, no independently reproducible full-match corner count could be found despite extensive searching — the tenth consecutive corners row in this log's history to end unresolved or provisional (after P-148, P-149, P-151, P-176, P-178, P-179, P-233, P-234, P-235). This is no longer treated as case-by-case bad luck: **a corners contract may not be ranked Rank #1 whenever a goal-based total (full-match or half) contract is available in the same supplied slate**, because corners settlement has never once resolved cleanly from an independently reproducible field owner across this framework's full history. The card's own `1st Half Over 0.5 Goals` row (ranked #2) settled cleanly and won — three goals (including an own goal) landed before the 38th minute, in a match that finished 2-2. This continues to validate first-half goal markets as the more resiliently-sourced early-scoring contract type relative to both full-match totals and corners, a pattern already visible in this card's own kill-path library.


**Kill-path library addition (§8.5):**


| Kill path | Defeats | Evidence origin |
|---|---|---|
| Structural corners-market sourcing failure (no field owner has ever independently reproduced a full-match corner count in this log) | A corners contract ranked Rank #1 ahead of an available goal-based total in the same slate | `P-302`; L-073; tenth consecutive case since `P-148` |


**Sport ordering override addition (§8.6):** when a supplied decision set contains both a corners contract and a goal-based total/half-total contract, the corners contract is capped below Rank #1 by default; only rank it #1 if a specific, current-session, independently-reproducible corner-count source has already been confirmed for the exact operator/provider definition in use (a bar no card in this log's history has yet cleared).


Full evidence: [PREDICTION_LOG_COMBINED_2.md, 2026-09-05(b) section](PREDICTION_LOG_COMBINED_2.md#component-import--p-294p-305-second-continuation--2026-09-05b).


## September 6 settlement learning — corners are settleable; `L-073` narrowed; the substitute-goal blindspot


**`L-073`'s empirical premise was false and the blanket corners cap is withdrawn.** The September 5(b) section above imposed a structural rule that a corners contract may never be ranked #1 whenever a goal-based total is available in the same slate, on the stated ground that *"no corners market in this framework's entire recorded history has settled cleanly from a single independently-reproducible field owner."* On 2026-09-06 three corners rows were settled from a single keyless structured endpoint, one request each:


| Card | Competition | ESPN event | Corners | Settlement |
|---|---|---|---|---|
| `P-302` | EPL | `eng.1` / `401879286` | Newcastle 4, **Bournemouth 3** | `Bournemouth Over 2.5` → **WIN** |
| `P-273` | Coppa Italia | `ita.coppa_italia` / `401911809` | **Palermo 3**, Mantova 2 | `Palermo Over 4.5` → **LOSS** (confirms the prior provisional grade) |
| `P-151` | Argentina Primera | `arg.1` / `401841527` | **Boca 11**, Lanús 3 | `Boca Over 4.5` → **WIN** (confirms the prior specialist-only 11–3) |


The endpoint is `https://site.api.espn.com/apis/site/v2/sports/soccer/<league>/summary?event=<id>`, field `boxscore.teams[].statistics.wonCorners`, Opta lineage, definition "corners won". Registered as `SRC-ESPN-SITE-API-SOCCER`, `CANDIDATE / RESEARCH ONLY`. The same call also returns **confirmed starting XI, full bench, formation and referee**, which is why it also serves `G14.2`.


**The cap is replaced by a coverage test, not removed.** The real variable was never the market type — it was whether any structured provider carries the *competition*. Verified non-coverage as at 2026-09-06 (HTTP 400 on the league slug): **Liga MX Femenil, MLS NEXT Pro, French third tier (Championnat National), China FA Cup.** Those are precisely the competitions behind `P-148`, `P-149`, `P-176`, `P-178`, `P-179`, `P-233`, `P-234` and `P-235` — eight of the ten cases that produced `L-073`. The rule that follows is `G10.2`:


- **Before** a corners (or cards, or any derivative) row enters the ranked slate, name the endpoint that will settle it and confirm in-session that it returns the field for **this competition**.
- Confirmed ⇒ the row is ranked on its own merits with no market-type penalty.
- Not confirmed ⇒ `SETTLEMENT_UNSOURCED`, `LOW` evidence, capped below Rank #1.


`L-073` is marked `NARROWED — SUPERSEDED BY L-081` in `LEARNING_REGISTER.md`. The lesson underneath it is preserved and generalised: **a promoted control whose justification is "this has never worked" must state the search that was run and the endpoints that were tried**, so it can be falsified the way this one was.


### Corner-generation profile (§8.10 addition)


`P-302` is a clean worked example that corner volume is not a possession proxy. Bournemouth registered 3 corners from **17 shots, 7 of them blocked, on 42.7% possession**; Newcastle registered 4 from 8 shots on 57.3%. The generating mechanism for the away side was blocked-shot deflection in a low-possession, high-volume shooting profile. When ranking a team-corners row, budget the two mechanisms separately — sustained territorial pressure, and blocked/deflected shot volume — and say which one the evidence supports. A possession-only justification is `align = PROXY` under `G23`.


### The substitute-goal blindspot — kill-path library addition (§8.5)


`P-304` (Slavia Praha 4-0 Zbrojovka Brno) was decided in its back half by players who were not on the team sheet the card would have frozen. **Two of the four goals came from substitutes**: Ayaosi (76'), introduced in the **26th minute as a forced injury replacement**, and Jurásek (88'), introduced on 63'. Two Slavia starters were lost to injury inside the first half hour. Nothing in this file previously required a card to record who was on the bench.


| Kill path | Defeats | Evidence origin |
|---|---|---|
| **Bench-driven late scoring surge** — a deep bench converts a controlled 1-0 or 2-0 into a 4-0 after the hour, moving both the total and the margin without any change in the starting XI's quality | A full-match `Under` or a favourite `-handicap` row budgeted from starting-XI exposure only | `P-304`: goals at 76' and 88' from substitutes, one a forced 26th-minute change (`L-082`) |
| **Forced early substitution against a weaker opponent produces no measurable degradation** | A flat personnel-loss markdown applied without an opponent-quality term | `P-304`: two starters lost by 26', still 4-0 — third instance of `L-077` |


### Sport ordering override additions (§8.6)


1. Item 1 of §8.6 is amended: a corner/card/player row lacking a layer of its own chain is still capped, **but the blanket "may not occupy a top slot above an opposing full-target contract" clause now applies only when `G10.2` returns `SETTLEMENT_UNSOURCED` for that competition.** Where the settling endpoint is confirmed, rank the row on its merits.
2. `BENCH_NOT_RETRIEVED` for either side ⇒ no full-match total row and no handicap row may be Rank #1. Where official structured feeds lag, an official club release or accredited beat consensus verified under Control `S-1 Rev 2` qualifies as `PROJECTED_BEAT_VERIFIED`, satisfies `G14.2` personnel modeling, and does not block Rank #1. First-half and other pre-substitution-window phase rows are unaffected, which is a further structural reason those rows have been the more reliable top slot in this log (`P-302`, `P-304`).




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | Name the ESPN league slug and event ID, or the official competition match-centre record, for every supplied row. Verified non-coverage: Liga MX Femenil, MLS NEXT Pro, French tier 3, China FA Cup. |
| `G14.2` coaching / bench / rotation record | `rosters[]` from the same ESPN summary call returns confirmed XI, full bench and formation. When ESPN feeds lag, official club media team sheets (typically released ~60 min pre-kickoff) or accredited journalist reporting verified under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED` and satisfy `G14.2`. Coaches are **not** in that feed (`coach` is `null`) — take them from the club/league official source. |
| `G20.2` distributional tail audit | Derive goal/phase tail mass from the **same frozen soccer joint distribution** used for ranking, including lineup/bench/coaching state, shot/xG process, set pieces, red-card and post-goal regimes, regulation/extra-time endpoint and any competition-specific corner process. Historical second-highest/median order-statistic sums are superseded and cannot rank a row. |
| `G21.1` exact target geometry | Map every supplied total/phase-total to its exact settlement event and derive WIN/PUSH/LOSS (plus void/censoring where applicable) from the same frozen sport-native PMF/CDF or coherent branch mixture. Genuine unions may be described as unions, but historical `TRUE_UNION` / `LOW_BAR_CUMULATIVE` / `CENTRAL_BAND` path-count labels have **no mandatory ordinal effect** and are not a substitute for the distribution. |
| `G26.1` no universal separation floor | Print any relevant reference base rate and `rank_gap` descriptively. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank by the row's exact marginal likelihood from the frozen joint distribution plus robustness/evidence uncertainty; precise probabilities require the validated-model gate. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Retain competition/round/leg/aggregate-specific baselines, opposing win paths and field-defined corner processes. Remove the automatic knockout suppression sign. Keep red-card/post-goal regimes separate from the pre-game baseline and admit only adequately sourced target fields to settlement.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-304/P-306/P-290 distinguish possession, goals, corner share and corner volume. Use exact team-labelled final corner fields; a winning team or goal from a corner cannot supply the total. P-290 most-corners is a research directional target, not an invented operator handicap. Preserve draws as losses for issued 90-minute team-winner calls. Eight older corner rows remain provisional/unresolved; P-126 needs event identity. No blanket corner rank cap is restored.


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-09 settlement learning — P-336, P-337, P-340, P-341, P-342 cohort


Five soccer cards settled ([`PREDICTION_LOG_COMBINED_3.md` §"2026-09-09"](PREDICTION_LOG_COMBINED_3.md)). Rank #1: **4 W / 1 L** (`P-342` lost). **Preferred full-match goals total: 1 W / 4 L** (`P-336` won; `P-337` R2, `P-340` R3, `P-341` R2, `P-342` R2 lost). Winner calls 4/5 (`P-337` a 0–0 draw). The misses concentrate in the FT-total corridor and in the top-of-card coherence between the first-half row and the FT-total direction. **No fitted weight or ordinal bar promoted** (`L-087`); the changes below are disclosure/branch-completeness reinforcements and one candidate-watch item.


### What went right (keep it)


- **`P-336` / `P-337` Rank #1 `Under 2.5` both won on *persistent* multi-window low-output** (Carabobo home, Barracas home — L5/L10/L15/L20 all low, not a single streak). Clean pass of `G17`/`G17.1` and §8.8's "use the longest defensible window". This is the reliable way to rank a goals `Under`.
- **`P-336` corner Rank #2 won on a genuine high-event attacking mechanism** (Estudiantes ≈27 shots / 9 corners), not a possession proxy — the `P-302` `wonCorners` worked example applied correctly.
- **`P-340` top two (`1H Over 0.5`, `Under 10.5 corners`) both won**; the `1H Over` reconciliation under control 20 was clean (both venue 1H splits + current-Clausura H2H each carried a first-half goal).
- **`P-341` pre-registered corner-settlement gate did its job** — "if the exact provider cannot be verified, `UNSETTLEABLE`, not inferred" — no W/L manufactured from a secondary 12-corner display.


### What went wrong, and the fix


1. **Named score-state kill paths were prose, not mass (`P-340` "2–1", `P-342` "1–0/2–0", both realized).** → **`RULES_GENERAL.md` §16.5(a) / `G-L1`:** the joint goal object must now enumerate the score families (0–0, 1–0, 1–1, 2–0, 2–1, 3+ …) with explicit mass, and every current-evidence kill path from the §8.5 audit must be one of those weighted branches. Write a representative Rank-#1 final score and check it against the handicap, FT-total and 1H lines before freezing the order. Add to **§8.7 pre-issue checklist** as item 18.


2. **First-half `Over 0.5` ranked high on historical frequency without a current early-chance mechanism (`P-337`: 1H Over p0.60 at Rank #2, inside a card whose Rank #1 was `Under 2.5` — the two theses were never reconciled; the game finished 0–0 with 14 total shots. `P-342`: 1H Over p0.68 at Rank #1 against a heavily rotated favourite — 0–0 at half). `P-337` is the second instance after `P-323` of a high 1H-Over sitting unreconciled on top of a low-event card.** → **Control 20 is reinforced (not replaced):** before `1H Over 0.5` outranks its complement, require a **named current early-chance-creation mechanism** that survives creator absences and opponent compression — historical first-half-goal frequency is not sufficient. When the same card's Rank #1 is a goals `Under` or its FT centre is at/below the line, the 1H-Over and FT-Under mechanisms must be shown to be *compatible* (one early goal then a controlled low-event game), not left contradictory. For a rotated cup favourite (see point 3), the early-conversion probability is *lower* than the class gap suggests.


3. **Tier gap translated into scoring direction with the wrong shape (`P-341` promoted side → 4–1 blowout; `P-342` third-tier vs rotated top-flight → late 2–0).** → **Controls 2, 23 and 28 reinforced + new candidate-watch item `G-L3`:** do not pool the weaker side's lower-tier defensive rates or an older opponent home regime into the FT-goal centre. Build a **tier-translation branch**: (a) the stronger side's blowout tail is fatter than its own-division scoring rate once it breaks through; (b) a *heavily rotated* favourite specifically produces **territorial dominance + late conversion**, not early goals or a 3+ total — so `1H Over` and `FT Over` must be *shrunk*, not raised, for a rotated cup favourite. Needs 3+ recurrences in a 25-card window before any ordinal treatment.


4. **`Under` won on an outcome-driven mechanism (`P-336` 1–0 with the loser at 27 shots).** → **Control 27 reinforced:** decompose creation → shot quality → finishing → goalkeeping and place current shots/xG/SOT beside the outcome rates *before* treating a clean-sheet run as a low-event mechanism. A winning `Under` does not validate the low-event thesis.


### Measured precision of this framework's full-match goal centres — and what it means for ranking totals


The five soccer cards in this cohort each stated an explicit goal centre and width. Measured against the actual results:


| Card | Centre | Actual | Signed error | Line | Normalised edge `\|centre − line\|/width` | Probability assigned | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| `P-336` | 2.39 | 1 | −1.39 | 2.5 | **0.07** | Under 0.60 | **W** |
| `P-337` | 2.00 | 0 | −2.00 | 2.5 | **0.50** | Under 0.65 | **W** |
| `P-340` | 2.41 | 3 | +0.59 | 2.5 | **0.05** | Under 0.55 | **L** |
| `P-341` | 2.35 | 5 | +2.65 | 2.5 | ~0.08 (width not quantified — a §16.5 defect) | Under 0.58 | **L** |
| `P-342` | 2.83 | 2 | −0.83 | 2.5 | **0.17** | Over 0.56 | **L** |


**Mean signed error −0.20 goals; mean absolute error 1.49 goals**, against stated widths of ±1.55–1.8. The centres are therefore **approximately unbiased but imprecise, and the stated widths were roughly honest.** The consequence is decisive for ranking: the supplied line sat only **0.05–0.50 goals** from the centre in every case. A 0.05-goal edge on a ±1.5-goal error distribution is a coin flip, and **no amount of additional research will make a near-the-line full-match total a high-confidence row.** The two highest normalised edges on the cohort (`P-337` 0.50, `P-342` 0.17) were also the only two where the assigned probability was defensible under §16.5(d); `P-336` had the *smallest* edge (0.07) and nearly the *highest* probability (0.60).


**The ranking consequence, from the cohort's own record:** the full-match goals total went **2 / 2 when it was Rank #1** (`P-336`, `P-337` — both persistent multi-window low-output `Under`s, and the two largest normalised edges) and **0 / 3 when it was Rank #2 or #3** (`P-340`, `P-341`, `P-342`). Rank a full-match total highly only when it has **both** (a) a persistent multi-window mechanism — not a single-regime, single-streak or class-gap one — and (b) a normalised edge that justifies its probability. Otherwise it belongs below the phase row and any research-complete team-total row. This is an evidence-grade and disclosure requirement, **not** an ordinal bar (`L-087`, `G23.1`): if a near-tied total genuinely has the highest marginal likelihood on the slate, it still ranks first — it just may not carry a 0.58–0.60 probability while doing so.


### The phase total has been the more reliable O/U family — three cohorts


| Family | `P-318`–`P-332` | `P-333`–`P-344` | Combined |
|---|---|---|---|
| `1H Over/Under 0.5` | 5 W / 2 L | 3 W / 2 L | **8 W / 4 L (67%)** |
| Full-match goals total | 6 W / 3 L | 2 W / 3 L | **8 W / 6 L (57%)** |


This is the **third** cohort consistent with the observation already recorded in §"September 5(b)" above — first-half goal markets have been the more resiliently-sourced and more reliably-ranked early-scoring contract type relative to both full-match totals and corners. Under the framework's own 3-recurrence threshold this is registrable as a **`CANDIDATE`** with a prospective test manifest (`LEARNING_REGISTER.md`), **not** an ordinal bar and **not** a licence to promote a 1H row above a better-evidenced full-match row. Samples are small, mixed-competition and within-card dependent. Note the two 1H losses this cohort (`P-337`, `P-342`) are both explained by the two mechanisms in "What went wrong" above, not by the family.


### Kill-path library additions (§8.5)


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A heavily rotated cup/knockout favourite dominating territory but not converting until late (0–0 at half, 1–0/2–0 final, large corner count) | A `1H Over 0.5` or `FT Over 2.5` row ranked on the class gap | `P-342`; controls 2, 28; `G-L3` |
| A newly promoted side conceding freely in its first top-flight matches while the class-superior side runs up the score once it breaks through | An `FT Under 2.5` built by pooling the promoted side's lower-tier form or the favourite's older low-event home regime | `P-341`; controls 2, 23; `G-L3` |
| A named score-state (e.g. "2–1") written in the kill-path list but carrying no probability mass in the joint object | Any total/side row whose ranking depends on that state being improbable | `P-340`, `P-342`; `RULES_GENERAL.md` §16.5(a) / `G-L1` |
| A first-half `Over` mechanism that contradicts the same card's Rank-#1 FT-`Under` mechanism | `1H Over 0.5` ranked above its complement inside a card whose Rank #1 is a goals `Under` | `P-337` (2nd after `P-323`); control 20 |


### The other two cross-sport controls, instantiated here (`G-L7`, `G-L8`)


`G-L1` and `G-L2` are covered in "What went wrong" above. The two requirements added on the second pass (`RULES_GENERAL.md` §§16.5(c)–(d)) apply to soccer as follows. Both are **retrieval/disclosure requirements — no fitted weight, no ordinal bar** (`L-087`).


| Cross-sport control | Soccer instantiation |
|---|---|
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a **goals-per-game figure, a clean-sheet rate, an Over/Under percentage or a "last N" summary** carry directional weight while the **per-match record** is available. §8.8 already requires the L5/L10/L15/L20 windows; `16.5(c)` adds that the *underlying match rows* must be opened where a decisive claim rests on them — print **shots, shots on target and xG per match** beside the goals per match, and state whether a run of low or high scores is front-loaded, back-loaded or uniform. `P-336` is the worked example: the Under leaned on Carabobo's home clean-sheet aggregate, and the opponent it kept out registered **~27 shots and ~8 on target** — the per-match creation record was the disaggregation that would have exposed the thesis as outcome-driven rather than low-event (control 27). On participants, quantify **every likely starter's minutes and goal involvement** rather than naming them; a decision-driving attacker carried as a bare name is `AGGREGATE_ONLY` and caps the dependent total/side rows — the direct analogue of the third-scorer failure that decided `P-344`. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


### Sport ordering override addition (§8.6)


6. When the card's own FT-goal centre is at or below the `Under` line, `1H Over 0.5` may not be Rank #1 or Rank #2 unless a named current early-chance-creation mechanism (not historical frequency) is stated and shown to be compatible with the FT-Under thesis. Otherwise cap it at `FORCED RANK` and rank it below the FT-total and any research-complete team-total row.


### Pre-issue checklist addition (§8.7)


18. Score-state family enumeration printed with explicit mass (`RULES_GENERAL.md` §16.5(a)); every §8.5 kill path with current specific evidence appears as a weighted branch; one representative Rank-#1 final score written and checked against the handicap, FT-total and 1H lines. For any tier-gap or rotated-favourite fixture, the tier-translation branch (`G-L3`) is shown and the 1H/FT Over rows are shrunk accordingly.


## 2026-09-11 settlement learning — `P-345`, `P-346`, `P-355`, `P-368`, `P-369`


Five soccer cards ([`PREDICTION_LOG_COMBINED_3.md` §"2026-09-11"](PREDICTION_LOG_COMBINED_3.md)). Rank #1 **3 W / 1 L + 1 provisional L** (`P-345` lost; `P-369`'s corner Rank #1 is a provisional loss). **Three frozen-owner corner rows settled this pass, all WIN** (`P-345-C03` UEFA 4, `P-346-C05` UEFA 10, `P-355-C05` FotMob 9 — two of them by half a corner). Favoured 1st-half rows **4 / 5**; supplied main-line full-match totals **1 / 5** (including two supplied but unranked lines); far-from-centre alternate totals **3 / 3**. Three-way winner labels **1 / 5** (two draws, two upsets). Learning-only; no fitted weight or ordinal bar (`L-087`).


### Measured precision of the full-match goal centres — ten cards


| Card | Centre | Actual | Error |
|---|---:|---:|---:|
| `P-336` | 2.39 | 1 | −1.39 |
| `P-337` | 2.00 | 0 | −2.00 |
| `P-340` | 2.41 | 3 | +0.59 |
| `P-341` | 2.35 | 5 | +2.65 |
| `P-342` | 2.83 | 2 | −0.83 |
| `P-345` | 2.50 | 5 | +2.50 |
| `P-346` | 3.03 | 1 | −2.03 |
| `P-355` | 2.40 | 2 | −0.40 |
| `P-368` | ~2.7 (corridor midpoint) | 2 | −0.70 |
| `P-369` | ~3.1 (corridor midpoint) | 2 | −1.10 |


**Mean −0.27 goals; mean absolute 1.42.** The finding of 2026-09-09 stands on double the sample: the centres are roughly unbiased but imprecise, and a line 0.05–0.5 goals from the centre is a coin flip. The phase row (1st half) and far-from-centre alternate lines are where soccer totals have held.


### What went right (keep it)


- **`P-346`: all five rows won** (mean Brier 0.0816 — the best card of the import). UEFA-confirmed XIs; the set-piece / early-goal branch; a large-edge alternate line (Under 4.5 on a 3.0 centre); a protected side.
- **`P-355`: an explicit goal-family table** (0–1 goals 30%, exactly 2 27%, 3 22%, 4+ 21%) produced three large-edge total rows that all won, and the corner process (width, H2H 16 and 19 corners) settled at its frozen provider. The side row was correctly capped `FORCED RANK` while the XI was unresolved, and a secondary lineup feed listing an ineligible player was quarantined.
- **`P-368`: the 1st-half Over won** on a real early-chance reading.


### What went wrong, linked to earlier lessons


1. **An early-season drought signed negative (`P-345`).** Villa's three-match run of 1 shot on target from 26 shots became a −0.20 attacking adjustment straight after a rebuild; Villa produced 21 attempts, 8 on target and ~3.00 xG. **Control 23 already requires width here** — an application failure.
2. **No cross-league translation (`P-345`, `P-346`).** Belgian domestic volume was projected onto the Europa League holders; Austrian league/cup scoring lifted the supplied Over 2.5 to 0.58 (one goal). → **control 31**.
3. **Control 20's third instance (`P-369`, after `P-323` and `P-337`).** A 64% 1st-half Over against the card's own finding that Shabab had scored one first-half goal in four league games and United's only home match was 0–0 at half-time. → control 20 reinforced below.
4. **Full-match Over despite a stated finishing regression (`P-369`: "United's 30% conversion is unsustainable", then Over at 0.61).** → `G-L2` / `G-L11`.
5. **Corner Under at 0.68 on an 8.0 centre with no width (`P-369`; 11 corners).** → `G-L8`, §16.8 item 3.
6. **Winner labels:** 1 / 5 three-way this import, 5 / 10 across `P-333`+. → control 3 reinforced: print the draw mass beside any plurality winner under 50%.


### Structural control additions and reinforcements


30. **UEFA club-competition derivatives settle from UEFA's own match-statistics feed — pre-register it.** For UEFA Champions League, Europa League and Conference League fixtures, name `matchstats.uefa.com/v1/team-statistics/{matchId}` (UEFA; FAME provider; keyless JSON with both teams' corners, attempts, attempts on target and possession) as the settlement source for corner and shot rows. Media match-stat displays are cross-checks only: in the two conflicts observed so far, **both** secondaries were wrong by one corner (VI on `P-345`, the Guardian on `P-346`). Parse the raw JSON — the WebFetch summariser returns only one team.


31. **Record the cross-competition strength translation explicitly.** When a club's current attacking or defensive rates come from a different domestic league than its opponent's — every UEFA league-phase fixture and most cup ties across divisions — print the translation applied (source-league rate, the adjustment, the resulting rate) before those rates enter the goal centre, and treat recent head-to-heads in the **same competition** with overlapping core squads as current-regime evidence rather than "descriptive". Origin `P-345` (the 2024/25 R16, Villa 3–1 / 3–0, demoted), `P-346`. A disclosure that generalises the `G-L3` candidate-watch to UEFA fixtures; no coefficient.


**Control 20 reinforcement (third recorded instance).** Before any 1st-half Over 0.5 outranks its complement, print **both** teams' current first-half goals for and against per match and their 0–0-at-half-time frequency, and derive the probability from both sides' first-half rates — as a transparent approximation, `P(no first-half goal) ≈ e^(−λ)` with `λ` the opponent-adjusted sum of the two sides' current first-half scoring rates — not from one team's event hit-rate. Now three instances (`P-323`, `P-337`, `P-369`); recorded as recurrence evidence in `LEARNING_REGISTER.md` §"2026-09-11". Control 20 already mandates the reconciliation; this specifies its arithmetic.


**Control 3 reinforcement.** Print the draw mass beside any regulation winner label below 50%, and the upset mass beside any label at or below 60%.


**Control 5 reinforcement (`P-368`).** An early goal that wins the 1st-half row switches the game into a leading-state branch; propagate that slowdown into the full-match distribution rather than reading the early goal as confirmation of a high-event match.


### Kill-path library additions (§8.5)


| Kill path | Defeats | Origin |
|---|---|---|
| A rebuilt attack breaking a two-to-three-match domestic drought | A non-loss or an Under built on the drought | `P-345`; control 23 |
| An opponent whose current first-half scoring is at or below ~0.25 goals a match | A 1st-half Over built on the other side's event hit-rate | `P-369`; control 20 |
| A leading-state slowdown after an early goal | A full-match Over on a card whose 1st-half Over has already won | `P-368`; control 5 |
| A corner count within ±1 of the line taken from a media secondary | Settling a corner row from anything but the field owner | `P-345`, `P-346`; control 30 |


### Pre-issue checklist additions (§8.7)


19. Both teams' current first-half rates and 0–0-HT frequency printed before any 1st-half row (control 20).
20. The cross-competition translation line for any cross-league or cross-division fixture (control 31).
21. Corner/shot settlement source pre-registered — UEFA FAME for UEFA fixtures (control 30); FotMob/Opta only where pre-registered.
22. Draw mass printed beside the regulation winner label (control 3).




## 2026-09-12 algorithm corrections and retrospective integration


Separate goals, corners and period-specific fields, and compute integer thresholds with push mass explicit. A 0-0 first half and late cup goals can support final superiority without an early-goal thesis. A final score does not establish corners or the official provider. Verify exact event/round/date/team order after opening links; translated sites and multiple domains do not prove independence. P-341/P-342/P-368/P-369 retain pending corner fields; provider selection is not backfilled after seeing the count. A league match that draws is not a shootout unless its competition rules and event report establish one. Recent finishing droughts warrant opponent/shot-quality context and sensitivity, not automatic no-direction or two-SE gates.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## Recovered mini-log and identity reinforcement - 2026-09-12


P-250/P-251/P-255/P-256/P-265 have inherited settled labels but missing later corner adjudications; keep their TMP-AUDIT handles until the decision can be reproduced. A complete score retrospective cannot certify its missing corner component. P-179 was a league draw with penalty goals, not a shootout; P-233-P-235 were quarterfinals. P-265's 41-minute opener supports its first-half Over, while the 2-0 final defeated the full Over; a corner-origin goal proves neither total corners nor an inevitable third goal. Reinforce exact competition/phase and separate goal/corner process controls; no generic knockout suppression coefficient follows. Evidence: audit_2026-09-12/historical_queue_evidence.md and recovered_historical_retrospectives.md.






## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Cards:** P-374, P-377, P-387 (log A); P-398, P-399, P-401, P-402 (log B); P-407–P-410, P-418, P-419 (log C). Finals re-verified at ESPN; P-402 and P-408 corners at the **Premier League official data record**.


### What went right (keep it)
- **Large-edge goal-based rows:** log C's team-goal, double-chance, first-half and Under-3.5/Over-2.5 rows went 19 W / 1 L (mean stated ≈ 0.74), built on current xG and shots on target — the P-346 pattern (control 31).
- Derivative discipline: corner rows were not booked on secondary counts; P-387 settled only when J.League published `CK = 7`.
- P-409's direct corner process for the underdog (Troyes 5 corners) and P-410's xG suppression of HSV.


### What went wrong, linked to earlier lessons
1. **P-408 Rank #1 (Brighton team corners O3.5, 75%) lost at 3.** The card had noted that Brighton were missing Mitoma and Minteh (their width) and that an early lead cuts later territory, but only trimmed the centre from 6.3 to 5.4 on a 3-game sample. Brighton led from 35' with 69% possession and 22 shots and took 3 corners. → control 33.
2. **Corners are not goals** (again): P-402 0–0 with 11 corners, P-399 1–1 with 17 (controls 4, 21, 27).
3. **Participant provenance:** P-374's near-kickoff XIs were wrong although several secondary feeds agreed (log A CAND-MINI-A → `L-20260912-07`).
4. **Pressure is not conversion / bench comebacks:** P-377 0–0 killed a 68% 1H Over; P-387 Kyoto led 2–0 and lost 2–3 to substitutes (controls 20, 27; `G14.2`).
5. **Fixture identity:** P-418 was issued on disagreeing aggregator listings; the national broadcaster's round report shows no Drukpa–RTC match (`RULES_GENERAL.md` §16.10(i)).
6. **Self-generated alternates:** P-419's corners O7.5 (69%) is provisional at ESPN 4 — generated without a per-team corner table (control 23).


### Structural control additions
32. **EPL derivative settlement source.** Pre-register the Premier League official data record for EPL corners, shots and XIs: `footballapi.pulselive.com/football/fixtures?comps=1&compSeasons=<id>&statuses=C` → `/football/stats/match/<fixtureId>` (`won_corners`, `total_scoring_att`), requested with `Origin`/`Referer: https://www.premierleague.com`. 2026/27 `compSeason` = 841. Other leagues: name the league's own record or record `UNKNOWN_DEFINITION`.
33. **Team-corner rows need their corner generators.** When a side is missing the players who produce its crosses and blocked shots, recompute the corner centre from the remaining personnel, and give the leading-state branch (the favourite scores first) its own mass. A 3-game corner sample is width, not a hit rate. Origin P-408.


### Kill-path additions
| Kill path | Defeats | Origin |
|---|---|---|
| Favourite leads early and plays through the middle | Favourite team-corner Over | P-408 |
| Exactly four goals | Under 3.5 ranked above Over 2.5 | P-407 |


## 2026-09-16 settlement learning — queue retry and external variant C′ (`P-399`, `P-401`, `P-407`–`P-410`, `P-418`, `P-419`)


Learning-only; disclosure and process changes only — no coefficient or ordinal bar (`L-087`). Cross-sport rules: `RULES_GENERAL.md` §16.11 (`G-L13` raw-record verification, `G-L14` settlement-route execution, `G-L15` O/U geometry, disruption facts). Evidence: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-16"](PREDICTION_LOG_COMBINED_3.md).


### What went right (keep it)
- **Low-threshold team-goal rows.** Free soccer team-goal totals (team Over 0.5 / opponent Under 1.5) went **10 of 10** at a mean stated 0.78 across `P-345`–`P-423`, and free first-half rows went 7 of 9. Both were built on current chance creation and home process (control 31). These are the O/U rows that have held.
- **Derivative discipline.** No corner row was booked on a secondary count, and a model summary claiming official Bundesliga corners was caught before it retired a handle.
- **C′ was right on P-418.** RSSSF lists the 14 September Drukpa – RTC fixture. The canonical "identity conflict" rested on a misdated July report (`RULES_GENERAL.md` §16.11(p)).


### What went wrong, linked to earlier lessons
1. **Main-line full-match totals.** The preferred side of supplied Over/Under pairs won **1 of 6** (`P-345`–`P-423`). This matches §"2026-09-09": centres are unbiased but imprecise, and the line sits a small fraction of a width away. Rank honestly; never prefer by default.
2. **Unsettleable corner rows.** Seven corner rows on `P-399`, `P-401` (two), `P-407`, `P-409`, `P-410` and `P-419` remain provisional. No keyless official record exists for Serie A, Allsvenskan, the Pro League, Ligue 1 or the Bundesliga, and none of the cards pre-registered ESPN. `G10.2` was listed, not executed (→ control 35, `G-L14`).
3. **Disruption facts missing from settlement.** `P-408` (Awoniyi red card at 53', Brighton already 2–0 up) and `P-419` (three red cards: GAIS 59' at 1–0, Djurgården 86', GAIS 90+10') were settled without them (→ control 34).
4. **Provider split on one count.** Leipzig corners were 8 at ESPN but 7 at Guardian/StatMuse/SoccerNews (`P-410`). Both clear 4.5, but a 7.5 line would settle differently by provider — name the provider.
5. **Self-generated alternates in leagues with no route.** `P-418` corners Over 4.5 and `P-419` corners Over 7.5 are both unbookable (control 23 reinforced).


### Structural control additions
34. **Disruption facts at settlement.** Copy red cards, penalties awarded or missed, goalkeeper changes and weather stoppages from ESPN `keyEvents` (or the league record), with the minute and the score at that minute. State whether each derivative or total target was already decided before the event. These are aleatory (`L-117`): record them for the population, never as a pregame "should have known". Origin: P-408, P-419.
35. **League corner settlement-route table (verified 2026-09-16).** A corner row names one of these routes at issue. Where the official record is not keyless-reachable, pre-register ESPN `wonCorners` (Opta lineage) as the settling provider on the card, or do not issue the row.


| Competition | Official record, keyless | Route to pre-register | Evidence |
|---|---|---|---|
| Premier League | Yes — Premier League data API | `SRC-PL-DATA-API` (control 32) | P-402, P-408 |
| UEFA club competitions | Yes — UEFA matchstats | `SRC-UEFA-MATCHSTATS` | P-345, P-346 |
| J1 League | Yes — club result tables (`CK`) | `SRC-JLEAGUE-CLUB-RESULTS` | P-387 |
| Bundesliga | No — bundesliga.com stats JS-only (raw zeros; direct 403) | ESPN `ger.1` | P-410 |
| Ligue 1 | No — plus.ligue1.com JS-only | ESPN `fra.1` | P-409 |
| Belgian Pro League | Not found (2026-27 match slug 404) | ESPN `bel.1` | P-407 |
| Allsvenskan | No — allsvenskan.se JS / cookie wall | ESPN `swe.1` | P-401, P-419 |
| Serie A | Not found (Sky Sport Italia tabellino is secondary) | ESPN `ita.1` | P-399 |
| LaLiga | Club-embedded LALIGA event feed (candidate) | ESPN `esp.1` or that feed | P-398 |
| Guatemala Liga Nacional | No; ESPN `gua.1` has no statistics | none — do not issue | P-377 |
| UAE Pro League | No; no ESPN route | none — do not issue | P-368, P-369 |
| Uganda Premier League | ESPN `uga.1` stale | none — do not issue | P-341 |
| Slovak cup | No ESPN route | none — do not issue | P-342 |
| Bhutan Premier League | No route | none — do not issue derivatives | P-418 |


### Kill-path additions
| Kill path | Defeats | Origin |
|---|---|---|
| Red card after the favourite leads → game management | Favourite team-corner Over; late full-match Over | P-408 (53', 0–2) |
| Dismissal-disrupted match without a corner chase | Total corners Over | P-419 (three reds; 2+2 corners) |


## 2026-09-16(b) — period scope on knockout derivatives (control 36)


36. **Name the interval, and settle it from a record that exposes that interval.** A cup tie can run to extra time, and most match-statistics feeds — including UEFA's own `team-statistics` — report whole-match totals. For any corner, card or shot row on a knockout fixture:
    - state on the card whether the contract is **90 minutes**, **regulation** or **whole match**;
    - name a record that exposes that interval (`G-L14`);
    - at settlement, check `played_time` or the period fields before grading, and if the feed is wider than the contract, grade PERIOD_SCOPE_BOUNDED only if a sourced bound excludes every settlement-changing split; otherwise retain UNRESOLVED_PERIOD (`RULES_GENERAL.md` §16.11(q)).


    Origin: `P-255` (UEFA 24 corners over 137 played minutes) and `P-256` (15 over 115), both 90-minute contracts on ties that went to extra time. The earlier bounded-win grades are withdrawn: neither feed excludes a losing regulation split. Both are UNRESOLVED_PERIOD, not proven wins.


## 2026-09-17 settlement learning — `P-425`, `P-426`, `P-430`, `P-436`, `P-437` (AFC Champions League Elite MD1)


Learning-only; disclosure and process changes only (`L-087`). Cross-sport rules: `RULES_GENERAL.md` §16.12 (`G-L17` joint failure mass, `G-L18` allocation marginals, `G-L19` end-state ontology, `G-L20` direct comparables). Evidence: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md). Every final and every corner count below was independently verified at ESPN `soccer/afc.champions` on 2026-09-17.


### What went right (keep it)
- **Wide totals and protected sides carried both winning cards.** `P-436` (all five rows) and `P-437` (all five rows) ranked **Match Under 4.5 against a 2.4–2.5 centre** and a `+1.5` handicap ahead of the plurality winner. In both, the winner label was wrong or irrelevant while every ranked row won. `P-436` is the cleanest case: the match finished on three goals, so the wide Under won and the supplied narrow Under 2.5 lost by one goal.
- **Overlapping totals are not contradictory.** `P-437` ranked Over 1.5 and Under 4.5 together and both won at three goals. State the overlap interval in advance, as that card did.
- **Weather as width, not sign** (`P-437`, `P-430` heat) — `G-L2` applied correctly.
- **Low-threshold team totals beat match totals** when one side drives the thesis (`P-425` R1 won while R2 and R4 lost).


### What went wrong, linked to earlier lessons
1. **`P-430` Rank #1 (Al Nassr team total Over 0.5, 0.85) LOST.** Al Nassr had 15 shots and 10 corners and did not score. The probability was too extreme for `MEDIUM` evidence with no confirmed XI or bench. → control 37.
2. **One-sided allocation** (`P-425`, `P-430`): the match-total rows needed the *other* side to contribute. Kyoto managed one shot all match. → `G-L18`.
3. **Cross-league defensive translation** (`P-426`): CAHN's four straight clean sheets came against materially weaker domestic and preliminary opposition, and Gamba scored three times after half-time. → control 39.
4. **Corners are not a dominance or goal proxy — again.** Gamba scored **four goals with one corner** (`P-426` R4 lost); Al Ain scored four with two corners. Confirms controls 4, 21, 33 and 34; no change.
5. **Derivative settlement route** (`P-430-C05`): the AFC official report publishes the score but **no corner field**, so the row stays open. → control 38.


### Structural control additions
37. **Single-team scoring rows above 0.80 without a confirmed XI.** When a row depends on one specific team scoring (team total Over 0.5, team Over 1.5) and the official XI and bench are not retrieved, print (a) the opponent-suppression branch and (b) the finishing-failure branch — chances created but not converted — each with explicit mass, and reconcile them against the stated probability. `G14.2` already caps the *rank* of participant-sensitive rows; this constrains the *probability extremity*. No numeric cap is imposed: across this batch rows at p ≥ 0.70 went 22 of 27, so a blanket cap is unsupported. Origin `P-430`.
38. **AFC / ACLE settlement routes** (extends the control 35 table):


| Competition | Score | Corners and derivatives | Notes |
|---|---|---|---|
| AFC Champions League Elite | AFC official match report — **verified** | **AFC report has no corner field** | Pre-register a corner route explicitly or do not issue the row |
| ACLE fixtures involving J.LEAGUE clubs | AFC report or J.LEAGUE | **J.LEAGUE ACLE match-data route / club records (`CK`)** — verified on `P-425`, `P-426`, `P-436` | Check this before any aggregator |
| ACLE generally | ESPN `soccer/afc.champions` — **verified 2026-09-17** for finals, `wonCorners`, goal minutes, possession and shots | Same | Data partner: it settles a row only if the card **pre-registers** it (§16.10(j)) |


39. **Cross-league defensive translation.** When an underdog's clean-sheet or low-concession sample comes mostly from a materially weaker league or qualifying pool, widen the favourite-separation tail rather than shifting the centre, and print the separation mass at +2 and +3 goals (`G-L12`). A clean-sheet streak against weaker opposition is not evidence of a suppression mechanism against a stronger one. Origin `P-426` (Gamba 4–1 after a 0–0-shaped first half).


### Kill-path additions
| Kill path | Defeats | Origin |
|---|---|---|
| Dominant side creates volume but does not convert; opponent contributes nothing | Match total Over ranked above a team total | `P-425`, `P-430` |
| Favourite's class separates after a contained first half | Underdog handicap + full-match Under sharing one low-event thesis | `P-426` |


## 2026-09-17(b) settlement learning — `P-438`, `P-439` (AFC Champions League Two MD1), `P-440`, `P-441` (UEFA Europa League MD1)


Learning-only; disclosure, derivation and retrieval changes only (`L-087`). Cross-sport rules: `RULES_GENERAL.md` §16.13 (`G-L21` card-level failure mass, `G-L23` result-versus-process). Evidence: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md). **All four finals, both half-time states, every goal minute, the disciplinary record and the shot/corner/possession fields were independently verified this pass** at ESPN `soccer/afc.cup` (= AFC Champions League Two — new lane) and `soccer/uefa.europa`.


Four cards, 20 `FREE` ranked rows, 15 W / 5 L, mean Brier **0.1783**. Rank #1: 3 W / 1 L. Three of the four cards won every row or all but one; the fourth (`P-438`) is the worst card in Part 4 to date.


### Round reference — the 17 matchday-1 fixtures of 16 Sep 2026


Reconstructed this pass from ESPN goal minutes across all eight ACL2 and all nine UEL matchday-1 games. Small (n = 17, SE ≈ 12 points) and recorded as **evidence, not a prior**.


| First-half goals | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Matches | 8 | 3 | 4 | 1 | 1 |


**P(1H ≥ 2) = 35.3%** → a first-half Under 1.5 wins 64.7% of that round. **P(1H ≥ 3) = 11.8%** → a first-half Under 2.5 wins 88.2%. Full match: P(FT ≥ 3) = 35.3%, P(FT ≥ 5) = 17.6%.


The three cards that took **1H Under 2.5** priced it at 87%, 89% and 92% — on the round's own number, and 3 W / 0 L. The one card that took **1H Under 1.5** priced it at 84%, roughly 19 points above the round's number, and lost.


### What went right (keep it)


- **`P-441` is the model card.** It printed a full first-half goal-count distribution (0/1/2/3+ = 46/36/10/8) **and** a full-match distribution (10/24/30/19/8/9), read all five rows off them, and printed Fréchet bounds for `P(R1 ∩ R2)` (83%–91%). Every row won; card Brier **0.0112**, the best in Part 4. Its 0.90+ rows are the only ones in the batch that are reconstructable from the card itself. **This is what `G-L8` execution looks like — copy the format.**
- **The shot-process model was right in both directions.** Celta took 19 shots and 12 corners in `P-441` and did not score; Kuwait took **two shots in ninety minutes** in `P-438`. Both confirm the low-conversion reads the cards made. The result diverged from the process only in `P-438`, and only through conversion variance and a red card.
- **Protected side over plurality winner**, again: `P-439` (0–0 draw, handicap survived, winner label lost) and `P-441` (1–0 against the projected winner, handicap survived). Both won every ranked row while the winner label lost.
- **Evidence hygiene** (`P-441`): three third-party "player X is out" claims were rejected because the players appeared in Celta's own published travelling squad, while Iago Aspas' club-confirmed absence was carried. Official squad list beats secondary absence reporting.
- **Phase protection worked where it was correctly sized** (`P-440`): the first-half Under won on exactly two goals while the same card's full-match Under 4.5 lost on the fifth — a clean single-match demonstration of `C-PHASE-VS-FULL-TOTAL`.


### What went wrong, linked to earlier lessons


1. **`P-438` Rank #1 (1H Under 1.5 at 0.84) LOST, and so did three of the other four rows.** The card printed **no first-half goal-count distribution**, so 0.84 was asserted rather than derived — a `G-L8` requirement listed and not executed (`M15`). Its three sibling cards that round put 0.87–0.92 on a **U2.5**; one goal of line cannot be worth only 3–8 points when the modal first-half count is 0–1. `P-441`'s own printed distribution implies a **10-point** gap between U1.5 and U2.5. → **control 40**.
2. **Four of `P-438`'s five rows needed one state.** Under independence P(all four fail) ≈ 0.0018; under the card's own marginals the upper bound is 0.16. Nothing was printed. `P-439` had the same slate shape and won everything, which is why this is a disclosure and not a prohibition. → `G-L21`.
3. **The settlement missed the mechanism.** `P-438`'s external retrospective diagnosed an early-goal-mass modelling failure and proposed raising early-goal mass. The structured feed says the opposite: Kuwait scored **two goals from two shots**, Al-Wahda had **41 shots / 16 on target / 64.5% possession / 11 corners**, and **Kuwait's Marhoon was sent off in the 60th minute** — after which Al-Wahda scored at 87' and 90+7'. The red card appears nowhere in the settlement, although §16.11(o) requires disruption facts with minute and score. → **control 41** and `G-L23`.
4. **Full-match upper tail under a large shot advantage** (`P-440`). Sparta had 23 shots to 13 and 13 corners to 2; three of the five goals came between 53' and 71'. The phase Under held and the 90-minute Under 4.5 died. Control 39 covers cross-league *separation*; this adds the **timing** dimension — a side with a large shot advantage generates its separation disproportionately after the interval.
5. **Winner labels lost on 2 of 4** (`P-439` draw, `P-441` home upset) while 19 of 20 ranked rows in those two cards won. Both cards had explicitly listed the branch that beat them. → `G-L21`(3).


### Structural control additions


40. **Sibling phase lines come from one printed distribution and must be mutually consistent.** Any first-half, first-30-minute or other phase total must be read off a **printed phase goal-count distribution** (`G-L8`, §16.5(d)) that appears on the card. When more than one line on the same phase is available — U0.5, U1.5, U2.5 — the probabilities assigned must be **derivable from that single distribution**, and the card prints the implied probability for each adjacent line so the spacing is visible. A phase Under at 0.80+ on a **tight** line (U1.5 or lower) additionally requires the modal phase count and `P(phase = 2)` to be stated explicitly, because that single cell is the whole difference between a U1.5 and a U2.5. Origin `P-438` (0.84 on a U1.5 with no distribution) against `P-441` (0.92 on a U2.5 with a full distribution, all rows won).


41. **Settle soccer from a feed that carries shots, cards and minutes — never from a narrative report.** A competition's official match report is authoritative for the score and the scorers, and the AFC report is verified for both; it does **not** publish shots, corners or disciplinary events. At settlement, open a structured feed for the same fixture and copy, at minimum: shots and shots on target per side, corners, possession, and **every red card, penalty and injury stoppage with its minute and the score at that minute** (§16.11(o)). These fields decide whether a control may be amended (`G-L23`) — the `P-438` retrospective reached the opposite conclusion from the correct one because it had the score and not the shot counts. Verified routes:


| Competition | ESPN site-API slug | Verified fields |
|---|---|---|
| **AFC Champions League Two** | **`soccer/afc.cup`** — counter-intuitive slug, **new 2026-09-17(b)** | final, goal minutes, **red cards**, `wonCorners`, `totalShots`, `shotsOnTarget`, `possessionPct` |
| AFC Champions League Elite | `soccer/afc.champions` | same (verified 2026-09-17) |
| UEFA Europa League | `soccer/uefa.europa` | same, plus a `Halftime` key event carrying the explicit HT score |


As a data partner this is corroboration, not a settlement route, unless the card **pre-registers** it (§16.10(j), control 32). Note that the AFC feed does not emit a `Halftime` key event — reconstruct the half-time state from goal minutes there.


### Kill-path additions


| Kill path | Defeats | Origin |
|---|---|---|
| A side with near-zero shot volume converts its only two chances early | A tight phase Under (U1.5), and every same-thesis Under behind it | `P-438` |
| Red card converts a contained match into a one-sided late siege | Full-match Unders that survived the first 60 minutes | `P-438` (60'), Al-Wahda scored 87' and 90+7' |
| A large shot advantage discharges after the interval | A 90-minute Under sitting behind a winning phase Under on the same card | `P-440` |


### `G-L24` — the handicap identity in soccer (added 2026-09-17(b))


Soccer signed-goal margin queries include the draw state explicitly. For D=home−away, evaluate each Asian handicap with exact W/P/L masses from the joint regulation goal grid; quarter-lines retain child settlement categories. A pooled one-goal frequency is context, not the conditional band for a specified favourite. A missing pooled season band does not bar Rank #1 when a coherent conditional distribution is disclosed. See corrected G-L24 and MODEL_IMPLEMENTATION_RECIPES.


Two cards in this cohort already depended on it: `P-438`'s Kuwait `+1.5` (0.75) and `P-440`'s Sparta `+1.5` (0.86) were both assigned rather than derived. Both won, which is not evidence that they were right — the band was never printed, so neither number is reconstructable.


### `G-L22` in soccer (added 2026-09-17(b))


Soccer cards in this log typically receive **forced pairs as supplied markets** (1H Over/Under 0.5, FT Over/Under 2.5) while ranking **`FREE` alternates** of their own — wide full-match Unders, phase Unders, low-threshold team totals. Both appear on the same card and they must be scored differently: the supplied pair is **one decision** (which side, and how far from 0.5), while each free alternate is an independent result.


This distinction explains a number that would otherwise mislead. In the `P-438`–`P-451` cohort the four soccer cards scored **0.1783** over 20 free rows against the eight MLB cards' **0.2293** over 32 forced-pair rows. That gap is **contract geometry, not superior soccer analysis**: the soccer cards had wide alternate lines available and chose them; the MLB cards were handed two near-centre pairs and had no alternate to choose. Any comparison across sports that does not separate `FREE` rows from `FORCED_PAIR` decisions is comparing the supplied lines.


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound evidence, debutant gate and the top-O/U review


Cross-sport: [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md) control `R-1`; source controls `S-1` (social identity) and `S-2` (press conferences) in `SOURCES.md` §"2026-09-19"; enhanced-failure trigger in `METHOD.md` §7.


**`R-1` applies qualitatively; soccer magnitudes are `NOT_YET_DERIVED`.** Goals are a low-count target and finishing variance is large relative to the mean, so a one- or two-match scoring run is weak evidence about the underlying rate. This cohort supplies both directions: `P-441`'s Celta had scored twice in five league matches, then produced 19 shots, 12 corners and 4 big chances — and still lost 0–1; `P-456`'s Betis produced 22 shots and 4 big chances for a single goal. In both the **process** read was right and the scoreline was conversion noise. A recent goal drought widens the distribution; it does not move the centre without a named mechanism (personnel change, role change, injury to the primary creator).


**Debutant/new-signing gate.** Where a starting XI contains a player with no minutes in the competition this season, record `NO_COMPETITION_SAMPLE` and widen rather than assume. Club official squad lists (verified superior to third-party absence claims in `P-441`) are the field owner for who is available.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** competition/federation official match centres, official club lineups/injury releases and governing rules; Hudl/StatsBomb open data may support covered historical research after source-card admission. Betting previews/picks and fantasy lineup/projection products are prohibited.


Goals, first-half goals, margins and winner should come from a coherent home/away goal process with lineup/availability, team attack/defence, venue, rest/travel, weather and verified tactical state. Corners are a separate event process. Do not use the market total or handicap to set expected goals, pace or variance.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


This section is the current prospective override for audit-derived ranking logic in this sport. Earlier dated examples remain historical evidence, but any incompatible active instruction is superseded.


- **Retained sport package:** regulation/extra-time endpoint; lineup, bench and coaching; shot/xG/process and set-piece/corner state; red-card/post-goal regimes; competition-specific field-owner corner settlement.
- **Withdrawn here:** second-highest/median or second-lowest/median pseudo-tail construction; path-count/category shortcuts as ranking rules; universal 40–60% top-slot bands; normalized-distance ordering; any one-result rebound/hangover/“due” rule; and any implication that a cushion determines the outright winner.
- **Current construction:** build one coherent sport-native joint outcome distribution/branch mixture, freeze it before supplied lines are queried, then derive exact target marginals and dependencies from that object. When a fitted/calibrated numerical distribution does not exist, a probability may be printed only as an `UNVALIDATED_SUBJECTIVE` output of the card's own complete, reproducible, declared distribution (METHOD §5). A number that cannot be reproduced from the printed distribution is invented precision and is not permitted. No subjective number carries a performance, calibration or value claim. *(Wording corrected 2026-09-25: the earlier "keep probabilities unquantified" contradicted METHOD §5; 2026-09-23 read-only audit item 5.)*

<!-- RESEARCH-2026-09-25 -->
## 2026-09-25(b) — EPL reference rates and recency (research pass)

**Status.** Reference rates (`C-PROMOTION-RECEIPT`: `REFERENCE`). No coefficient. Source: `BASE_RATES_REGISTER.md` §7.3. That is the ESPN scoreboard plus match summaries for all 380 EPL 2025-26 matches: goal minutes from `keyEvents` and `wonCorners`. `RECENCY_AND_REBOUND.md` §7 covers recency.

**S-R1. EPL references (field BR).**

| Quantity | EPL 2025-26 |
|---|---|
| Total goals: mean | 2.75 |
| Over 1.5 / 2.5 / 3.5 | 0.789 / **0.550** / 0.284 |
| Draw; both teams score | 0.274; 0.561 |
| First half: mean goals (second half) | **1.19** (1.56) |
| First half: P(≥ 1) / P(≥ 2) / P(≥ 3) | 0.716 / **0.334** / 0.111 |
| Corners: mean / SD | 10.0 / 3.27 |
| Corners: P(≥ 10) / P(≥ 11) | 0.563 / 0.437 |

- These are EPL-only.
- Cups, lower tiers and other leagues are `NOT_YET_DERIVED`. Do not transfer the EPL rates to them (M12).
- EPL corner **settlement** stays with the pulselive field owner. The ESPN `wonCorners` figures are base rates only.

**S-R2. Disclosure thresholds that follow from the references.**
- A first-half Under 1.5 above about 0.75 names its reason. The population rate is 0.666; the §4 ACL2/UEL round was 0.647.
- A full-match Over or Under 2.5 above about 0.70 names its reason. The population is 0.550 / 0.450.
- Neither threshold is a cap. It is the point at which the card's departure from the population must be written down (field BR).

**S-R3. Recency and width.**
- A team's season scoring rate predicts its next game no better than the league constant (RMSE 1.135 v 1.135). The last game is **38% worse**; half-shrinking to the league mean is best.
- A team-form narrative therefore needs a named mechanism: lineup, tactical change or xG process. Otherwise it is width.
- Width: the total residual SD is **1.61** (no better than the raw 1.57); the margin residual SD is 1.51.
- A goals-total width below about 1.37 (0.85 × 1.61) names what the card knows (`C-WIDTH-BENCHMARK`).

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 2026-09-25(d) — track record from the full settled-row review

**Track record (`C-TRACK-RECORD`).** 143 decisions from 37 cards: won **74.8%** at a mean stated 0.700. Brier **0.170**, resolution 0.036. **This is the framework's clearest demonstrated skill.**

- Overs won 38/51 at 0.674; Unders 30/40 at 0.735.
- **Phase against full-game totals in the same card:** 30/36 against 27/41 (this is evidence for `C-PHASE-VS-FULL-TOTAL`).
- **Exception: underdog cushions (+k.5) won 8/13 at a stated 0.766**, a gap of −0.15. `C-PLUS-CUSHION` applies. A +k.5 soccer row prints P(underdog wins) + P(draw) + P(loses by ≤ k) from a Skellam or bivariate-Poisson margin (`python tools/card_math.py cover --dist skellam --mu … --mu-opp … --line +k`), beside the EPL margin band (`BASE_RATES_REGISTER.md` §7.3), or `NOT_YET_DERIVED` for other competitions.

Source: `research/settled_rows_2026-09-25/README.md`. The figures are hindsight on the framework's own cards, descriptive, and use card-cluster intervals. None is a coefficient (`L-087`). Controls: `RULES_GENERAL.md` §"2026-09-25(d)".


<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — Rank 1 and Rank 2 in soccer: keep what works

Controls: `RULES_GENERAL.md` §"2026-09-25(e)".

**Record at Rank 1/2 (probability era): 55 W / 17 L,** the best of any sport. RM-1 re-ordered 1 of 35 held-out cards, so soccer's order is essentially unchanged.

- **Where soccer's STRONG rows come from.** Phase rows, team totals, double chances and corners, plus +1.5 cushions (7/8 won at about 0.82). These remain the preferred Rank-1/Rank-2 material. `SLATE_ADVISORY` points at them when a supplied slate is main-line only.
- **Classification.**
  - A "+0.5 / 1X" row is a **double chance**, not a cushion. Such rows won 2/5 at a stated ~0.73, so none is stated above 0.70 without the Skellam draw mass printed.
  - Soccer +k.5 rows carry no RM-1 cushion penalty.
- **TB-1 (EPL only).**
  - Results have resolution: P(home win) Brier 0.231 v 0.247.
  - **Totals do not:** TB-1 is worse than the league rate (0.258 v 0.250), so EPL goal totals stay anchored on the §7.3 reference and the XI.
  - Other leagues: `TEAM_BASELINE_P: NOT_COVERED`.
- **First-half Over 0.5 at Rank 1/2** lost 4 times in the probability era. It stays under the §7.3 reference and M12 (no EPL-to-cup transfer).
- **Unchanged:** corner settlement lanes and the confirmed XI.
