# Soccer analysis rules

**Live rules for Soccer. Markdown-only operation, 2026-09-28.** Read §0 in full for every card: it governs this file.
- §1 onward is the reference algorithm and the competition rules; it is consulted by citation.
- The dated history (settlement learnings and the evidence behind every numbered control) was moved verbatim to `archive/superseded_2026-09-28/sport_history/RULES_SOCCER_history_to_2026-09-28.md`, which is no longer in the Markdown tree. A maintainer can recover it from the pinned commit ([Git 3fbf0c981b40](https://github.com/danisgreat/Sports-Research/blob/3fbf0c981b40a1d0e3ffff9725dcc8e383ff05fa/archive/superseded_2026-09-28/sport_history/RULES_SOCCER_history_to_2026-09-28.md); [index](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) when a control's full text or evidence is needed. The model works from §0 and the sections below.
- Arithmetic: `PROBABILITY_TOOLKIT.md`. Sources: `SOURCES.md` §3.4. Card and self-audit: `CARD_AND_LOG_TEMPLATES.md`. The cross-sport rules are in `CURRENT_RULES.md`, which outranks this file.
- No sport, competition or target is prospectively validated. Every card is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

<!-- LIVE-RULES-PAGE-2026-09-26 -->
## 0. Live rules — one page (consolidated 2026-09-26)

**Status (md-only, 2026-09-28).** This page is the live rule set for this sport and governs the rest of the file. It was consolidated on 2026-09-26 from the numbered controls, the SFA algorithm and the dated sections through 2026-09-25(e). Those dated sections are now archived (see the header). Where a control below is one line, that line is the operative rule, and the archived history is its evidence.

### 0.1 Blocking preconditions (§8.1)
| Gate | Requirement | If it fails |
|---|---|---|
| SO-P1 endpoint | Competition, leg/tie state, regulation / extra time / penalties / advance, and which endpoint each row settles on | Stop. Regulation winner, eventual winner and advance are different contracts (controls 1, 18) |
| SO-P2 participants | Confirmed XI, keeper, formation, **bench**, set-piece and penalty takers for both sides (ESPN `rosters[]` or the official club/league source), refreshed at freeze | Side, double-chance and handicap rows capped. `BENCH_NOT_RETRIEVED` ⇒ no full-match total or handicap at Rank 1 (September 6 override 2). `PROJECTED_BEAT_VERIFIED` needs the S-1 Rev 2 receipt |
| SO-P3 derivative provider | Exact provider and definition for corners, cards, shots | `UNKNOWN_DEFINITION`; the row cannot reach LEAN/SUPPORTED |
| SO-P4 schedule identity | Start confirmed by the competition or association when aggregators conflict | Identity quarantined |

**Settlement route at issue (controls 30, 32, 35, 36, 38, G-L14).** A corner or shot row names its route before it is ranked: EPL → the Premier League data API (pulselive, control 32); UEFA club competitions → UEFA matchstats (control 30); otherwise pre-register ESPN `wonCorners` (Opta lineage) or do not issue the row. On a knockout fixture, name the interval and settle from a record that exposes it (control 36).

### 0.2 Building the goal distribution
1. **Anchor.** `TEAM_BASELINE_P` is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4, Poisson form, k 2).
   - **Results** anchor on it in the **EPL, La Liga, the Bundesliga, Serie A and Ligue 1**. P6 (2026-09-28, preregistered) found it beat the population in every one of five held-out seasons in each league, by 0.043–0.057 three-way Brier.
   - **Totals (Over/Under 2.5)** anchor on it only in **La Liga and the Bundesliga**. The EPL, Serie A and Ligue 1 totals anchor on the population; EPL totals were *worse* with TB-1.
   - The EPL also has its §7.3 reference (S-R1).
   - Other competitions: `BASELINE_P` where derived, else `NOT_YET_DERIVED`, with TB-1-MD printed only as `UNVALIDATED:<league>`. **Never transfer EPL rates to cups, lower tiers or other leagues (M12).**
2. **Four layers per side:** chance creation, shot quality, finishing, goalkeeping (SO-S2, control 27). Print shots, shots on target and xG beside goals per match (G-L7). A season rate predicts no better than the league constant, and the last game is 38% worse: form needs a named mechanism (S-R3, R-1).
3. **Cross-competition translation.** Print the source-league rate, the adjustment and the result for every cross-league or cross-division fixture (control 31). A clean-sheet run against weaker opposition widens the favourite-separation tail; it does not shift the centre (control 39). Early-season droughts shrink hard (control 23).
4. **Phases.** First and second halves are separate states, not a fixed fraction (SO-S3). Before any 1H Over 0.5 outranks its Under, print both teams' current first-half rates and 0–0-HT frequency and derive P(no 1H goal) ≈ e^(−λ) from both sides (control 20). Sibling phase lines come from **one printed phase distribution**. A phase Under at 0.80+ on U1.5 or lower states the modal count and P(phase = 2) (control 40).
5. **Bench and state.** The bench has expected-minute value (control 22). Early goals switch to leading/trailing-state branches that propagate into later goals and corners (controls 5, 12, 25). Red cards rebuild both sides (control 6).
6. **Knockouts.** Compare the exact competition/round/leg/aggregate population; there is no automatic knockout Under sign (control 28, L-064).
7. **Width.** The EPL total residual SD is 1.61. A goals-total width below about 1.37 names what the card knows (S-R3, C-WIDTH-BENCHMARK).
8. **One regulation score grid plus linked corner and player objects → every row** (SO-S7). Use `PROBABILITY_TOOLKIT.md` §1–§3 for margins.

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

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The soccer model (A1) is Poisson attack/defence ratings with linked halves. On 2022-23 to 2025-26 it beat the league baseline on results and margins in all five top leagues, and TB-1 on EPL results. It did **not** beat the baseline on totals in the EPL, Serie A or Ligue 1, nor on BTTS or first-half totals outside La Liga. Dixon–Coles added nothing. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability and cards (2026-09-26(e)).** EPL three-way favourites reach 0.70 in only 6% of games (result Brier 0.222 against 0.243), so soccer's STRONG Rank-1 rows come from phase, team-total and double-chance markets (the cards' own record), not from three-way results. On 4 EPL card contracts: card 0.178, A1 0.151. The 80 soccer cards spread across more than 30 competitions, most without a validated model (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `BASE_RATES_REGISTER.md` §7.8).

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
29. **A prior leg or a recent head-to-head result is context, not a cause.** Per RULES_GENERAL (archived) §11.3E (G17.1), a team's result in the first leg of the same tie, or in its immediately preceding match, may support a "response"/"bounce back" lean only with a named, currently active mechanism (a specific tactical change, a returning player, a disclosed rotation consequence); otherwise it carries no directional weight. Record the series/aggregate-state block from RULES_GENERAL (archived) §5 for every two-leg tie.


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


Algorithm ID: `SFA-SOCCER`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL (archived) §11) with soccer content. Process composition only; no fitted weight, scenario weight or published probability is introduced. Senior, reserve, youth, women's, friendly and inaugural-competition populations are separate, and goals, corners, cards and player events are separate processes throughout.


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
| A prior leg or recent result used as a "response" cause with no named current mechanism | A bounce-back/reversal lean lacking G17.1 support | §4 control 29, RULES_GENERAL (archived) §11.3E (G17.1) |


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


Implements `GFA-2` step G13.1 (RULES_GENERAL (archived) §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


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


Implements `GFA-2` step G15.1 (RULES_GENERAL (archived) §11.3C). Venue classification for this sport is normally **OUTDOOR unless the venue has a closed roof**.


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


That file is the reference for `§1` identity (competition, leg/tie state, regulation vs extra time/penalties, advance vs win) and `§6` settlement. It does not change `SFA-SOCCER`. Its **maintenance note** carries the season-boundary rules-currency check and the new-competition onboarding requirement (RULES_GENERAL (archived) §3, `G2`): the August restart of the European leagues, and any new season / edition elsewhere, triggers a re-verification of the IFAB Laws in force plus the competition's format, substitution/VAR/foreign-player rules and any points deductions before the first card; a new soccer competition must be fully documented there before it is forecast.
