> **Authority.** [CORE](CORE.md) and [CURRENT_RULES](RULES_REFERENCE.md#part-a-current_rules) govern new work; this page holds this sport's rules, and earlier statements below keep their historical scope.

**Executable forecast cycle (CYCLE-v1).** Defined in [FORECAST_CYCLE_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol); summarised in [CORE](CORE.md) §7.

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](WORKFLOW.md#part-b-mini_log_identity_protocol); summarised in [CORE](CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_PROTOCOL.md#part-b-research_exhaustiveness_protocol); summarised in [CORE](CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

# Soccer analysis rules

**Live rules for Soccer. Markdown-only operation, 2026-09-28.** Read §0 in full for every card: it governs this file.
- §1 onward is the reference algorithm and the competition rules; it is consulted by citation.
- The dated history (settlement learnings and the evidence behind every numbered control) was moved verbatim to `archive/superseded_2026-09-28/sport_history/RULES_SOCCER_history_to_2026-09-28.md`, which is no longer in the Markdown tree. A maintainer can recover it from the pinned commit ([Git 3fbf0c981b40](https://github.com/danisgreat/Sports-Research/blob/3fbf0c981b40a1d0e3ffff9725dcc8e383ff05fa/archive/superseded_2026-09-28/sport_history/RULES_SOCCER_history_to_2026-09-28.md); [index](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) when a control's full text or evidence is needed. The model works from §0 and the sections below.
- Arithmetic: `PROBABILITY_TOOLKIT.md`. Sources: `SOURCES.md` §3.4. Card and self-audit: `CARD_AND_LOG_TEMPLATES.md`. The cross-sport rules are in `RULES_REFERENCE.md`, which outranks this file.
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
- *[Non-operative since v10: rank by p_card, SELECTION_RULES §2.]* Rank by RM-1 q; soccer's order is almost unchanged by it (1 of 35 held-out cards re-ordered).
- **Track record:** the strongest resolution of any sport. 143 decisions from 37 cards won 74.8% at 0.700 (Brier 0.170, resolution 0.036). The card-cluster calibration interval spans 0, so this is the strongest evidence rather than proof of skill. Rank 1/2 went 55 W / 17 L. Phase against full-game totals on the same cards: 30/36 against 27/41 (`C-PHASE-VS-FULL-TOTAL`, still TESTING). First-half Over 0.5 at Rank 1/2 lost four times.

### 0.5 Settlement (controls 34, 36, 41)
- Settle from a structured feed that carries shots, cards and minutes, never a narrative report. Copy red cards, penalties, keeper changes and weather stoppages with the minute and score, and say whether each target was already decided (controls 34, 41).
- Regulation versus extra time is exact (G-L16). Media corner counts are cross-checks only; both observed media conflicts were wrong by one (control 30).
- ESPN slugs: AFC Champions League Two is `soccer/afc.cup`; the AFC feed has no `Halftime` event, so reconstruct half-time from goal minutes (control 41).

### 0.6 Reference numbers (EPL 2025-26, `PARAMETERS.md` §7.3)
Goals mean 2.75; Over 1.5/2.5/3.5 0.789/0.550/0.284; draw 0.274; BTTS 0.561. First half: mean 1.19 (second half 1.56); P(≥1)/P(≥2)/P(≥3) 0.716/0.334/0.111. Corners mean 10.0 (SD 3.27); P(≥10) 0.563, P(≥11) 0.437. EPL only.

### 0.7 Withdrawn in soccer — never apply
The blanket corners Rank-1 cap (L-073, replaced by the coverage test L-081/G10.2); the automatic knockout Under sign; pseudo-tails; path-count categories; 40–60% bands; normalised-edge ordering; one-result response rules; any implication that a cushion determines the winner.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The soccer model (A1) is Poisson attack/defence ratings with linked halves. On 2022-23 to 2025-26 it beat the league baseline on results and margins in all five top leagues, and TB-1 on EPL results. It did **not** beat the baseline on totals in the EPL, Serie A or Ligue 1, nor on BTTS or first-half totals outside La Liga. Dixon–Coles added nothing. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability and cards (2026-09-26(e)).** EPL three-way favourites reach 0.70 in only 6% of games (result Brier 0.222 against 0.243), so soccer's STRONG Rank-1 rows come from phase, team-total and double-chance markets (the cards' own record), not from three-way results. On 4 EPL card contracts: card 0.178, A1 0.151. The 80 soccer cards spread across more than 30 competitions, most without a validated model (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `PARAMETERS.md` §7.8).

### 0.8 Control index (full text in §4 and the dated sections)
1 regulation winner ≠ advance · 2 rotation changes strength · 3 draw-band discipline (draw/upset mass) · 4 corners are not dominance proxies · 5 leading-state branch · 6 red cards asymmetric · 7 friendlies phased · 8 set-piece/keeper extremes shrink · 9 weather is mechanism-specific · 10 niche-stat settleability · 11 derivative completeness · 12 two-leg early-goal regime · 13 sparse-participant side cap · 14 corner share ≠ corner total · 15 current competition v inherited class · 16 friendly participant phase · 17 placeholder conflict is not a final · 18 winner endpoint literal · 19 schedule conflict · 20 early-goal reconciliation with both sides' first-half rates · 21 late events don't backfill first half · 22 bench minutes · 23 early-season shrinkage · 24 volume/allocation/result · 25 transition pressure · 26 contract matches mechanism · 27 territory/chance/scoreboard separate · 28 exact knockout population · 29 prior leg is context · 30 UEFA matchstats route · 31 cross-competition translation · 32 EPL data API route · 33 team-corner generators · 34 disruption facts · 35 league corner route table · 36 period scope on knockout derivatives · 37 single-team rows > 0.80 without XI · 38 AFC routes · 39 cross-league defensive translation · 40 sibling phase lines from one distribution · 41 settle from a structured feed. References: S-R1 EPL rates · S-R2 disclosure thresholds · S-R3 recency and width.

### 0.9 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1)
Numerical-engine design notes (the engine code was removed on 2026-10-09; compute by hand with PROBABILITY_TOOLKIT.md and the sport block of research/prompts/1_GAME_CARD.md; this list is a design record, not a rule):
1. **Event-First Modeling**: Bivariate goal process derived from expected goals (xG) and shot quality:
   $$\text{Shots} \times \text{xG/Shot} \longrightarrow \text{Poisson/Negative Binomial Goal Matrix } P(G_{\text{home}}=g_1, G_{\text{away}}=g_2)$$
2. **Derivative Independence**: Corners and cards are modeled via distinct point processes, not as proxies for goal dominance; all contract lines (1X2, Over/Under, BTTS, Asian handicap) are integrated directly from the joint score PMF.
3. **Regime Conditioning**: Red cards, key starter rotation (especially starting goalkeeper and primary goalscorer), and match state (leading/trailing dynamics) condition transition intensities.
4. **Independent Training**: Fit exclusively on `H0-SOCCER-v1` via StatsBomb / Football-Data.co.uk; D0 is strictly reserved for qualitative error diagnostics.

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

Added 2026-09-04. The IFAB Laws of the Game, the shared competition variables that decide settlement (extra time, penalties, substitution regimes, VAR, points and tiebreak systems, promotion/relegation, playoff/liguilla/split formats, foreign-player limits, points deductions), and a dedicated section for every soccer competition in the prediction logs — Premier League, Carabao Cup, Bundesliga, 2. Bundesliga, LaLiga, Serie A, Coppa Italia, Eredivisie, Jupiler Pro League, Danish Superliga, DBU Pokalen, Championnat National, Brasileirão Série A, Argentine Liga Profesional (and Primera C / reserve fixtures), Roshn Saudi League, Chinese Super League, Chinese FA Cup, Egyptian Premier League, Israeli competitions, Kazakhstan Premier League, Armenian Premier League and Cup, Uzbekistan Pro League, MOL Cup, the Sikkim S-League, NWSL, MLS NEXT Pro, Liga MX and Liga MX Femenil, Leagues Cup, the UEFA club competitions (Conference League, Women's Champions League, Women's Europa Cup), CONMEBOL Libertadores, the FIFA Intercontinental Cup, and the club friendlies (KCC Pre-Season Cup, Coupang Play Series, ASEAN club competition) — all in **[RULES_SOCCER.md (LEAGUE_RULES_SOCCER)](#merged-league_rules_soccer)**.

That file is the reference for `§1` identity (competition, leg/tie state, regulation vs extra time/penalties, advance vs win) and `§6` settlement. It does not change `SFA-SOCCER`. Its **maintenance note** carries the season-boundary rules-currency check and the new-competition onboarding requirement (RULES_GENERAL (archived) §3, `G2`): the August restart of the European leagues, and any new season / edition elsewhere, triggers a re-verification of the IFAB Laws in force plus the competition's format, substitution/VAR/foreign-player rules and any points deductions before the first card; a new soccer competition must be fully documented there before it is forecast.

---

# Merged: LEAGUE_RULES_SOCCER

*Merged 2026-11-07 (CR-2026.11.07-R2, FORMAT), verbatim. Formerly `LEAGUE_RULES_SOCCER.md` (original title: Soccer — sport and competition rules reference). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/LEAGUE_RULES_SOCCER.md](archive/consolidation_2026-11-07/merged_sources/LEAGUE_RULES_SOCCER.md).*

> **Current authority (October 5):** [CORE.md (METHOD)](CORE.md#merged-method) and [RULES_REFERENCE.md (CURRENT_RULES)](RULES_REFERENCE.md#part-a-current_rules) govern new work. Requested qualitative or explicitly uncalibrated research receives canonical Part 6 IDs regardless of calibration; numerical performance certification is separate. Read current IDs/freeze from the [status register](GAME_LOG_STATUS_CURRENT.md), unresolved items from the [carryover](archive/verification_2026-10/closure_2026-10-05/carryover.md), and [current implementation evidence](archive/verification_2026-10/implementation_2026-10-05/REPORT.md). Earlier method, queue, freeze and eligibility statements below retain their historical scope.

> **Authority.** [CORE](CORE.md) and [CURRENT_RULES](RULES_REFERENCE.md#part-a-current_rules) govern new work; this page holds this sport's rules, and earlier statements below keep their historical scope.


> **Status (md-only, 2026-09-28):** reference material for identity, format and settlement. No scope is prospectively validated; every card is LEARNING_ONLY. Live rules: `RULES_REFERENCE.md` and the sport file's §0.

Status: **ACTIVE — reference**
Created: **2026-09-04**
Companion to: **[RULES_SOCCER.md](RULES_SOCCER.md) §9**. Reference only; it does not change `SFA-SOCCER` or any gate. It documents the IFAB Laws of the Game, the competition variables that decide settlement, and the specific rules of every soccer competition in the prediction logs.

Rules-era caveat: formats below are those in force for the **2025–2026 / 2026 / 2026-27** seasons the current log covers. Domestic formats (split systems, playoff qualifier counts, foreign-player quotas, relegation on/off) change frequently — **verify the season** for any event, especially for the Belgian, Danish, Egyptian, Argentine, Mexican, Chinese and Kazakh competitions, which have all changed format recently.

**Maintenance (RULES_GENERAL (archived) §3, `G2`).** Last reviewed **2026-09-04**. Before the first card of a new season / new edition of any competition here — or the first appearance of a competition after a break of ~6 weeks or more (most European leagues run Aug–May, so the August restart is a hard checkpoint; Brazil, China, Argentina, the Nordic and MLS-adjacent competitions run on other calendars) — re-verify against the field owner: the IFAB Laws currently in force (a new edition applies from 1 July each year), the competition's format (team count, split-system adoption, playoff/liguilla qualifier count, promotion/relegation on or off, points/tiebreak order), substitution and VAR adoption, foreign-player quotas, and any points deductions — then update the section below **before** issuing the card. The first time a new soccer competition is forecast, document its full rules here first. Recent examples of why this matters: the away-goals rule was abolished (2021); the 5-substitutions and goalkeeper-8-second rules were added; the UEFA competitions moved to the 36/18-team "league phase"; Liga MX abolished its play-in round from Apertura 2026; the Belgian, Danish and Egyptian leagues changed their split formats; China revised its foreign-player rule for 2026.

---

## 1. The IFAB Laws of the Game (universal)

**Objective.** Two teams of **11** (including a goalkeeper). Score by putting the whole ball over the opponent's goal line between the posts and under the bar. Most goals wins; many competitions allow a draw, others force a winner (§2).

**Duration.** Two **45-minute** halves + **"additional time"** (stoppage time) added by the referee for stoppages. Since 2022–2026 referees add time far more generously (often 5–10+ minutes) — this materially raises late-goal and total exposure versus pre-2022 data. Half-time ≤15 minutes. A "cooling break" (~3 min) may be taken mid-half in hot conditions.

**Restarts.** Kick-off (start of each half and after a goal), throw-in (ball out on the touchline), goal kick, corner kick, free kick (direct — can score directly; or indirect), penalty kick (a foul by the defending team inside its own penalty area, or a deliberate handball there), drop ball.

**Offside.** An attacker is offside if, when a team-mate plays the ball, they are nearer the opponents' goal line than both the ball and the second-last opponent, **and** become involved in active play. Not offside direct from a throw-in, corner or goal kick.

**Fouls and misconduct.** Direct free kick / penalty for kicking, tripping, pushing, holding, handball, dangerous play, etc. **Yellow card** (caution) for reckless fouls, dissent, time-wasting, persistent infringement; **two yellows = red**. Straight **red card** (dismissal) for serious foul play, violent conduct, denying an obvious goal-scoring opportunity (DOGSO), spitting, offensive language. A sent-off player is **not replaced** — the team plays a man short for the rest of the match. A red card carries a suspension into subsequent matches (length varies by competition).

**Substitutions.** Since 2022 the Laws permit up to **5 substitutions** per team (made in a maximum of **3 stoppages**, plus half-time), where the competition adopts it — almost all professional competitions now do. **Concussion substitutes** (an additional 1 or 2, permanent, not counting against the 5) are used in many competitions. Friendlies and some youth competitions allow more.

**VAR (Video Assistant Referee).** Where adopted, on-field review of four categories only: **goals** (and build-up infringements), **penalty decisions**, **direct red cards**, **mistaken identity**. "Clear and obvious error" / "serious missed incident" threshold. **Semi-automated offside** (SAOT) is now used in the top UEFA competitions and several leagues. Many lower divisions, reserve leagues, youth leagues and some cup rounds have **no VAR** — this raises officiating variance and is an identity fact worth recording.

**Goalkeeper 8-second rule (Law 12, from 1 July 2025).** A goalkeeper controlling the ball with the hands must release it within **8 seconds** (the referee shows a visible 5-second countdown). Penalty for a breach: a **corner kick** to the opponents (replacing the old, almost-never-called indirect free kick for 6 seconds). This modestly increases corner counts and reduces goalkeeper time-wasting.

**"Captain only" (from 1 July 2025).** When the referee signals it, only the **captain** may approach to query a decision; other players who surround the referee are cautioned.

**Coin toss.** Decides which team kicks off and which way each team attacks in the first half; teams switch ends at half-time.

---

## 2. Shared competition variables (these decide settlement)

Resolve **all** of these per competition and per fixture before setting any market (RULES_SOCCER.md §1, controls 1, 18):

### 2.1 Regulation vs extra time vs penalties

- **League matches:** end after 90' + stoppage. A **draw is a live result**. No extra time.
- **Single-leg knockouts:** if level after 90', normally **two 15-minute halves of extra time** (played in full — a goal does not end them), then a **penalty shoot-out** if still level. Some cups (notably the **Carabao Cup** before the semis, **Leagues Cup**, **Chinese FA Cup** before round 5) **skip extra time and go straight to penalties**.
- **Two-leg ties:** the team with the higher **aggregate** score over both legs advances. If aggregate is level after the second leg's 90', **extra time then penalties** in the second leg. The **away-goals rule was abolished by UEFA in 2021** and by CONMEBOL earlier; some competitions (Liga MX Liguilla) instead advance the **higher-seeded/better-placed team** when aggregate is level, with no extra time except in the final. **Always check the tie-break rule for the specific competition.**
- **A "regulation winner" bet, an "advance/qualify" bet, and an "eventual match winner" bet are three different propositions** (RULES_SOCCER.md control 18). The standard 90-minute market **excludes** extra time and penalties unless the operator says "including ET/pens." A shoot-out win is never a regulation win.

### 2.2 Penalty shoot-out

Five kicks each, alternating, then **sudden death** if level. Only players on the pitch at the end of extra time may take kicks. Since 2017 the standard order is ABAB; the "ABBA" order was trialled and dropped. In the log's terms, a shoot-out result settles "advance/win the tie" markets and any explicit "including penalties" market — nothing else.

### 2.3 Points, tiebreakers and league tables

- **Points:** win **3**, draw **1**, loss **0** — universal in the modern era.
- **Ordering when level on points** varies and matters for relegation/title/European-place markets:
  - **Goal difference first**, then goals scored, then head-to-head: England (Premier League), Germany (Bundesliga), Netherlands, Brazil (with a different chain — see §6.1), most leagues.
  - **Head-to-head first**, then goal difference: **Spain (LaLiga)**, **Italy (Serie A)**, Argentina and several others.
  - **A playoff match ("spareggio"/"desempate")** if two teams are level for the title, a Champions-League place or relegation: **Serie A**, and historically Spain.
- **Points deductions** for insolvency, financial-fair-play or licensing breaches are applied by several federations mid-season — check the current table, not a pre-season projection.

### 2.4 Season structure types

- **Balanced double round-robin** (everyone plays everyone home and away): Premier League, LaLiga, Serie A, Bundesliga, Ligue 1, Eredivisie, Brasileirão, Roshn Saudi League, Chinese Super League, Championnat National.
- **Split system** (a full or partial round-robin, then the table splits into a championship group and a relegation group, with points carried): **Scotland, Belgium, Denmark, Israel, Egypt (2025-26)** and others. In a split league, the fixture list and even the number of remaining games differ by group — never assume a full home-and-away season.
- **Apertura / Clausura** (two separate short championships per calendar year, each with its own champion, plus an annual/aggregate table for continental qualification and relegation): **Argentina, Mexico** and much of Latin America. Frequently followed by a knockout **playoff / "Liguilla" / "fase final"** among the top teams of the short tournament.
- **Group + knockout** (a tournament, not a league): the cups, Leagues Cup, and the continental competitions.

### 2.5 Promotion, relegation and playoffs

The number of clubs relegated, whether the process includes a **relegation/promotion playoff**, and whether **relegation is currently suspended** (Mexico; Egypt for 2025-26) are all competition- and season-specific and are given per competition below. In some countries relegation is decided by a **multi-season average** ("promedios" in Argentina, "coeficiente" in Mexico) rather than the current season alone.

### 2.6 Squad and foreign-player rules

Registered-squad size (often 25 with homegrown-player quotas in Europe), and **foreign / non-domestic player limits** — how many may be **registered** and how many may be **on the pitch at once** — vary widely (see Saudi Arabia, China, Argentina below). A change of one or two available imports is a large effective-strength swing in leagues with tight quotas.

### 2.7 Populations that must not be pooled

Friendlies, youth, reserve/second-team, and senior competitive matches are **different populations** (RULES_SOCCER.md §1). Within senior football, a two-leg European tie is a different population from the same clubs' league matches (controls 12, 15, 28). Knockout stakes suppress the pregame scoring baseline before any goal (control 28).

---

## 3. Continental and international club competitions

### 3.1 UEFA Europa Conference League ("UEFA Conference League")

UEFA's third-tier club competition. In the log: **2026-27 qualifying, second qualifying round, 2nd leg** (July–August 2026).

- **Qualifying (July–August):** two-legged ties (Champions Path and Main Path), aggregate score, **extra time + penalties** in the second leg if level (no away goals). Winners of the play-off round reach the league phase.
- **League phase (since 2024-25):** **36 clubs in one table** ("Swiss model"); each club plays **6 matches** against 6 different opponents (3 home, 3 away). Win 3 / draw 1 / loss 0. **Top 8 → round of 16 directly; 9th–24th → a two-legged knockout play-off; 25th–36th eliminated** (no drop to another competition).
- **Knockout (R16 onward):** two legs, aggregate, ET + penalties, **no away goals**. **Final:** single match at a neutral venue, ET + penalties.
- Settlement: qualifying and knockout ties need the "regulation / 90'" vs "advance" endpoint frozen. League-phase matches are ordinary 90-minute fixtures where a draw is live.

### 3.2 UEFA Women's Champions League (new format, 2025-26)

- **League phase:** **18 clubs in one table**; each plays **6 matches** vs 6 different opponents (3 home, 3 away). Nine clubs enter directly; nine via the third qualifying round.
- **Knockout:** **top 4 get a bye to the quarter-finals; 5th–12th play a two-legged knockout play-off**; then QF and SF two legs (aggregate, ET + penalties, no away goals); **Final** single match at a neutral venue.
- Qualifying rounds (in the log: **third qualifying round, league path, first/second leg**) are two-legged ties, aggregate, ET + penalties in the second leg.

### 3.3 UEFA Women's Europa Cup (new for 2025-26)

UEFA's **second women's club competition**, launched 2025-26 to sit below the Women's Champions League. Two-legged qualifying rounds → a group/league stage → two-legged knockouts → final. Aggregate scoring, ET + penalties, no away goals. Because it is brand-new, there is **no competition history** — treat as a sparse population and shrink hard (RULES_SOCCER.md control 13).

### 3.4 CONMEBOL Copa Libertadores

South America's premier club competition. In the log: **Round of 16, second leg** (2026).

- **Group stage:** 8 groups of 4, double round-robin, top 2 advance (3rd drops to the Copa Sudamericana).
- **Knockout (R16 → QF → SF):** **two legs, aggregate, NO away goals** (removed in 2005), **penalties directly if aggregate is level after the second leg's 90'** — CONMEBOL knockouts before the final go **straight to penalties, with no extra time** (a key difference from UEFA). Confirm per edition, as CONMEBOL has toggled this.
- **Final:** a **single match at a pre-selected neutral venue** (since 2019), with extra time + penalties.
- Settlement: the "advance" market for a R16/QF/SF tie can be decided by a shoot-out with no extra time — freeze the endpoint.

### 3.5 FIFA Intercontinental Cup

A FIFA competition launched in 2024, contested annually by the reigning continental club champions. A **single-match knockout ladder**: the AFC/CAF/CONCACAF/OFC champions play off (the "playoff" and "FIFA Challenger Cup" stages), the survivor plays the CONMEBOL champion (the "Derby of the Americas"), and that winner plays the **UEFA Champions League holder** in the **final** (the FIFA Intercontinental Cup itself). All ties are single matches with **extra time + penalties**. It is distinct from the expanded 32-team **FIFA Club World Cup** (played in 2025, next in 2029).

---

## 4. Domestic leagues — Europe

### 4.1 England — Premier League

20 clubs, **38-match** balanced season (Aug–May). Win 3 / draw 1 / loss 0. **Tiebreak: goal difference, then goals scored, then head-to-head; a playoff match only if the title, relegation or a European place is otherwise unresolved.** **Bottom 3 relegated** to the Championship (which sends up 2 automatically + 1 playoff winner). **5 substitutions** (3 stoppages) + concussion subs. Full **VAR + semi-automated offside**. 25-player squad with **homegrown** quotas; no in-season transfer of the mid-season break rule beyond a short winter pause. No promotion/relegation playoffs at the top level. European qualification: top 5 (currently) to the Champions League + Europa/Conference places, plus domestic cup winners.

### 4.2 England — Carabao Cup (EFL Cup)

Single-elimination knockout of all 92 Premier League + EFL clubs (Premier League clubs in European competition enter in round 3). **No replays.** **No extra time until the semi-finals** — a drawn match in rounds 1–4 and the quarter-finals goes **straight to a penalty shoot-out**. **Semi-finals are two legs** (aggregate, ET + penalties if level after the second leg, **no away goals**). **Final:** single match at Wembley, ET + penalties. Winner qualifies for the Europa/Conference League. Heavy rotation is normal in the early rounds — treat as a partial-strength population.

### 4.3 Germany — Bundesliga

18 clubs, **34-match** balanced season with a **winter break** (~mid-Dec to mid-Jan). Win 3 / draw 1 / loss 0. **Tiebreak: goal difference, then goals scored, then head-to-head.** **16th place plays a two-legged relegation/promotion playoff** against the 3rd-placed club of the 2. Bundesliga; **17th–18th relegated automatically**. **5 subs.** VAR. The **"50+1" ownership rule** shapes the league's economics but not match rules.

### 4.4 Germany — 2. Bundesliga

18 clubs, 34 matches, same points/tiebreak/subs/VAR as the Bundesliga. **Top 2 promoted; 3rd plays the Bundesliga's 16th** in a two-legged playoff. **Bottom 2 relegated to the 3. Liga; 16th plays the 3. Liga's 3rd** in a playoff. In the log: **2026-27, Matchday 3**.

### 4.5 Spain — LaLiga (LaLiga EA Sports)

20 clubs, **38-match** balanced season. Win 3 / draw 1 / loss 0. **Tiebreak: head-to-head first (points, then goal difference between the tied clubs), then overall goal difference, then goals scored, then Fair Play.** **Bottom 3 relegated.** **5 subs.** VAR + SAOT. Non-EU player registration limits apply (typically 3 in the squad). Note the head-to-head-first tiebreak makes late-season "who finishes above whom" markets behave differently from England/Germany.

### 4.6 Italy — Serie A

20 clubs, **38-match** balanced season. Win 3 / draw 1 / loss 0. **Tiebreak: head-to-head (points, then GD in those matches), then overall goal difference, then goals scored; a single playoff match ("spareggio") if two clubs finish level and the position decides the title, a Champions League place, or relegation.** **Bottom 3 relegated** (Serie B promotes 2 + a playoff winner). **5 subs.** VAR. Winter break. In the log: **2026-27, Matchday 2**.

### 4.7 Italy — Coppa Italia

Single-elimination knockout, **seeded** so that Serie A clubs (especially the top 8) enter in later rounds and **host** lower-seeded opponents (home advantage by ranking, not draw). **Extra time + penalties** if level (all rounds). **Semi-finals are two legs** (the only two-legged round; aggregate, ET + penalties, no away goals). **Final:** single match in Rome, ET + penalties. Winner qualifies for the Europa League. In the log: **2026-27, Round of 32**.

### 4.8 Netherlands — Eredivisie

18 clubs, **34-match** balanced season. Win 3 / draw 1 / loss 0. **Tiebreak: goal difference, then goals scored.** The champion and cup winner take European places; a **European play-off** among clubs finishing roughly 5th–8th decides a Conference League qualifying spot. **Bottom club relegated automatically; 16th–17th enter the "Nacompetitie"** — a multi-club playoff with second-tier (Eerste Divisie) clubs for the remaining top-flight places. **5 subs.** VAR.

### 4.9 Belgium — Jupiler Pro League (Belgian Pro League)

**2025-26: 16 clubs** (expanding to 18 in 2026-27). **Regular season:** full double round-robin (30 matches). **Then the table splits:**
- **Champions' play-offs (top 6):** a further double round-robin; **regular-season points are halved** (and rounded) before it starts. Decides the title and top European places.
- **Europe play-offs (7th–12th):** a mini-tournament for the last European ticket; **points halved**.
- **Relegation play-offs (13th–16th):** a further round-robin; **regular-season points carried in full**. **No automatic relegation in 2025-26** — the bottom club after the relegation play-offs meets the Challenger Pro League promotion-playoff winner in a promotion/relegation playoff.
- Settlement: the point-halving means mid-table "points" markets and title/relegation projections must use the **post-split** points, not the regular-season table.

### 4.10 Denmark — Superliga (3F Superliga)

**12 clubs.** **Regular season:** double round-robin (**22 matches**). **Then the table splits, with all points carried in full:**
- **Championship play-off (top 6):** a double round-robin (**10 more matches**) for the title and European places.
- **Qualification/relegation play-off (bottom 6):** a double round-robin; a further **European play-off** for a Conference League qualifying spot; **the bottom 2 are relegated** to the 1st Division.
- Win 3 / draw 1 / loss 0; GD-based tiebreak. In the log: **2026-27, Round 6** (regular season).

### 4.11 Denmark — DBU Pokalen (Danish Cup, "Betano Pokalen")

Single-elimination knockout across all tiers. Early rounds single-leg (lower-ranked club hosts); **quarter-finals and semi-finals are two legs** (aggregate, ET + penalties, no away goals); **final** single match. Extra time + penalties whenever a single match or an aggregate is level. Winner qualifies for the Europa League. In the log: **2026-27, Round 2 (1/32-final)**.

### 4.12 France — Championnat National (National 1)

France's **third tier** (below Ligue 1 and Ligue 2), 18 clubs, **34-match** balanced season, a mix of professional and semi-professional clubs. Win 3 / draw 1 / loss 0; GD tiebreak. **Top 2 (sometimes 3) promoted to Ligue 2; bottom 4 relegated to National 2.** **No end-of-season playoffs. No VAR.** Reserve teams of Ligue 1 clubs may compete but cannot be promoted. Lower budgets, higher variance, thin public data — a sparse population (RULES_SOCCER.md controls 13, 21). In the log: **Round 4** (referred to as "Ligue 3 / National").

---

## 5. Domestic leagues and cups — rest of the world

### 5.1 Brazil — Campeonato Brasileiro Série A

20 clubs, **38-match** balanced season (roughly April–December — a **calendar-year** season, unlike Europe). Win 3 / draw 1 / loss 0. **Tiebreak chain: most wins, then goal difference, then goals scored, then head-to-head, then fewest red cards, then fewest yellow cards, then a draw.** **Bottom 4 relegated** to Série B. Top clubs qualify for the Copa Libertadores and Copa Sudamericana. **5 subs** (6 in some domestic competitions), VAR. Heavy fixture congestion (state championships, two national cups, continental play) means rotation is constant. In the log: **Round 25**.

### 5.2 Argentina — Liga Profesional de Fútbol (Torneo Apertura / Torneo Clausura)

**2026 format:** two tournaments per year (**Apertura**, first half; **Clausura**, second half). **2 zones of ~15 clubs**; each club plays its zone home-and-away plus **1 interzonal "clásico"** (≈15–16 matches). **Top 8 of each zone** enter a **single-match knockout** (Octavos → Cuartos → Semifinales → Final; higher seed hosts; extra time + penalties if level). Each tournament has its own champion.
- **Annual table ("Tabla anual"):** regular-phase points from both tournaments combined — decides most **Copa Libertadores / Sudamericana** berths and **one relegation**.
- **Relegation by "promedios":** a **three-season points-per-match average**; the club(s) with the worst average go down (plus the annual-table bottom club). This means a club can be safe on current form but doomed on its average, or vice versa — check the promedios table, not just the current standings.
- VAR in the top flight. In the log: **Torneo Clausura 2026** (and earlier "Fecha 7, Zona A").

### 5.3 Argentina — Primera C and reserve-league fixtures

The log also contains **Argentine reserve-team fixtures** (labelled variously "Argentina Reserve League", "Primera C Metropolitana Reserves", "Campeonato de Reserva"). These are **reserve (second-string) matches** that mirror the senior club fixture list, usually played at training grounds or small stadia, **with no VAR, minimal public data, heavy squad rotation, and frequent trialists/youth players**. **Primera C** itself is a lower senior division (4th–5th tier of the AFA pyramid) with its own promotion playoffs. Treat both as sparse, low-information populations and cap participant-dependent rows hard (RULES_SOCCER.md control 13).

### 5.4 Saudi Arabia — Roshn Saudi League (Saudi Pro League)

**18 clubs**, **34-match** balanced season (Aug–May). Win 3 / draw 1 / loss 0; GD tiebreak. **Bottom 3 relegated** to the First Division League. **Squad limited to 25**, of which **up to 10 may be foreign**, with **a maximum of 8 foreign players on the pitch at once** (quota expanded in recent seasons). VAR. Top clubs qualify for the AFC Champions League Elite. The heavy foreign allowance means the league's effective quality is highly roster-dependent and top-heavy.

### 5.5 China — Chinese Super League (CFA Super League)

**16 clubs**, **30-match** balanced season (a **calendar-year** season, roughly March–November). Win 3 / draw 1 / loss 0; GD tiebreak. **Bottom 2 relegated** to China League One (which promotes 2). **2026 foreign-player rule ("6655"):** roughly **5 foreign players registered per match and 4 on the pitch simultaneously**, with salary controls — confirm the exact numbers for the season. VAR. In the log: **Round 25**.

### 5.6 China — Chinese FA Cup

Single-elimination knockout, ~80 clubs across all tiers, **8 rounds** (March–December). Lower-division clubs enter first and host. **From the fifth round onward, a level match goes to 30 minutes of extra time then penalties**; in the earlier rounds a level match goes **straight to penalties**. **Quarter-finals and semi-finals** are (in recent editions) single matches; confirm per year. Winner qualifies for the AFC Champions League Two. In the log: **quarter-final** ties (2026).

### 5.7 Egypt — Egyptian Premier League

**2025-26: 21 clubs**, new **split format** — a single round-robin first half, then the table splits into **Group A (top 7)** contesting the title and continental places and **Group B (bottom 14)** contesting survival, with **4 relegated** (relegation had been cancelled the previous season). Win 3 / draw 1 / loss 0. VAR at major venues only. A long, hot-weather, congested calendar (clubs also play CAF competitions and the Egypt Cup). In the log: **Round 3**.

### 5.8 Israel — Israeli Premier League and State Cup

- **Israeli Premier League (Ligat ha'Al):** **14 clubs**, a double round-robin (**26 matches**), then a **split** into a **top playoff (1st–6th)** for the title/Europe and a **bottom playoff (7th–14th)** with **relegation** (bottom 2, sometimes + a playoff). Points carried. Win 3 / draw 1 / loss 0.
- **Israel State Cup (Gvia ha'Medina):** single-elimination knockout of all tiers; **extra time + penalties** if level; final at a national stadium; winner qualifies for the Europa/Conference League. In the log: **2026/27, Round 1**.
- **Israel U19 "Elite" (Noar Premier) division:** the **under-19 youth league** — a development competition. No VAR, volatile lineups, results driven by individual age-group talent; a sparse, low-information population.

### 5.9 Kazakhstan — Premier League (Qazaqstan Prem'er Ligasy)

**2026: expanded to 16 clubs** (from 14). Calendar-year season (March–November). Win 3 / draw 1 / loss 0. **2 clubs relegated** to the First League (which promotes 3). The champion enters the UEFA Champions League qualifying path. VAR at selected matches. In the log: a **postponed Round 21 fixture**.

### 5.10 Armenia — Premier League and Cup

- **Armenian Premier League:** a small league (**10–11 clubs**) playing a **quadruple round-robin** (~36 matches) to fill a full season. Win 3 / draw 1 / loss 0. Bottom club relegated (sometimes + a playoff) with the First League. Champion to the UEFA Champions League qualifying path. Thin squads, small crowds, wide performance variance.
- **Armenian Cup:** knockout; **quarter-finals and semi-finals two legs** (aggregate, ET + penalties, no away goals), **final** a single match; winner to the Europa/Conference League. In the log: a **preliminary / Round of 16** listing.

### 5.11 Uzbekistan — Pro League (second tier)

The **Uzbekistan Pro League is the second tier** of Uzbek football (the top flight is the **Uzbekistan Super League**, 16 clubs). The Pro League runs a calendar-year season (April–November); **top 2 promoted** to the Super League, bottom club(s) relegated to the First League. No VAR; minimal public data. In the log: **Round 17**. Do not confuse it with the Super League.

### 5.12 India — SFA A Division S-League (Sikkim)

A **state-level competition in Sikkim** run under the local sports-federation structure ("SFA" = Sports For All / Sikkim Football Association A Division). Effectively a **regional semi-amateur league** — small squads, part-time players, single grounds, no VAR, near-zero reliable public data, and frequent schedule uncertainty (the log carries an *unresolved* fixture, P-126, precisely because the field-owner schedule could not be confirmed). Standard 90-minute league matches, draws live, points 3-1-0. This is the sparsest population in the entire soccer register — participant/identity uncertainty caps essentially every market (RULES_SOCCER.md control 13, and the general evidence ceiling).

---

## 6. North and Central America

### 6.1 United States — NWSL (National Women's Soccer League)

**2026: 16 clubs** (Boston Legacy and Denver Summit added). **30-match** balanced regular season, single table. Win 3 / draw 1 / loss 0; **draws are live** in the regular season. **No promotion/relegation** (closed league); a **salary cap and roster limits** (~26 senior roster, allocation/international slots). VAR (added 2024). The regular-season leader wins the **NWSL Shield**.
- **Playoffs:** **8 clubs**, single-elimination, seeded by regular-season points. If level after 90', **two full 15-minute extra-time periods** (played out completely), then a **penalty shoot-out**. The final is the **NWSL Championship**.

### 6.2 United States — MLS NEXT Pro

MLS's **third-division development league** (mostly MLS reserve teams + a few independents). **No draws:** a match level after 90' goes **straight to a penalty shoot-out** — **both teams get 1 point for the 90-minute draw, and the shoot-out winner gets a 2nd point** (so a "regulation winner" is a real, distinct outcome from a "match/shoot-out winner"). **3 points for a 90-minute win.** Rosters ~20 for a matchday; up to 5 subs. Heavy developmental rotation — effective team strength swings match to match. **Playoffs:** conference-based single-elimination. In the log: **Colorado Rapids 2 vs Ventura County FC** — the card's "potential winner" is explicitly the **regulation winner**, not the shoot-out winner.

### 6.3 Mexico — Liga MX

**18 clubs.** Two tournaments per year (**Apertura**, Jul–Dec; **Clausura**, Jan–May), each a **17-match** single round-robin, each with its own champion.
- **Liguilla (playoff):** **from Apertura 2026 the "Play-In"/reclasificación round is abolished — the top 8 of the Tabla General go straight to two-legged quarter-finals**, then two-legged semi-finals, then a two-legged final. Higher aggregate advances; **if aggregate is level in the QF or SF, the higher-seeded team advances (no extra time); the final has extra time + penalties.**
- **Tiebreakers:** points, GD, goals scored, head-to-head, away goals, relegation coefficient, Fair Play.
- **Relegation is suspended** — the club with the worst multi-season **coefficient** pays a fine instead of going down. Continental berths (CONCACAF Champions Cup) go to tournament champions and the top of the aggregate table.
- **5 subs**, VAR. In the log: cards reference **Apertura 2026** and earlier **Apertura 2026** fixtures.

### 6.4 Mexico — Liga MX Femenil

The women's competition, **same Apertura/Clausura + Liguilla structure** as the men's Liga MX (17-match tournaments, top-8 two-legged playoff, higher seed advances on level aggregate outside the final). No relegation. In the log: **Apertura 2026**.

### 6.5 CONCACAF — Leagues Cup

An annual **MLS vs Liga MX** tournament (co-sanctioned). **2026: 36 clubs — all 18 Liga MX + 18 qualified MLS clubs.**
- **Phase One (group stage):** clubs split into an **Eastern** and **Western** region of 18, each seeded into 3 tiers; each club plays **3 or 4 cross-league matches** in a mini-round-robin. **"No draws" format — a group match level after 90' goes straight to a penalty shoot-out** (3 points for a 90-minute win, and points for a shoot-out result).
- **Knockout:** the **top 4 clubs from each league** enter a fixed **MLS-vs-Liga-MX bracket** — quarter-finals, semi-finals, third-place match, final — all **single matches, straight to penalties if level (no extra time except, in most editions, the final)**.
- The **finalists and the third-place-match winner qualify for the 2027 CONCACAF Champions Cup.**
- Settlement: the "no draws / straight to penalties" rule means a "regulation (90') result" market and a "match winner (incl. penalties)" market diverge frequently — freeze which one the card uses. In the log: **2026 Quarterfinal** cards.

---

## 7. Friendlies and exhibition tournaments

In the log: **Coupang Play Series** (a promoter-run friendly series in South Korea, e.g. Manchester City vs Atlético Madrid), **KCC Pre-Season Cup** (a club pre-season tournament in Cambodia — *not* the Cambodian Premier League), and various senior "pre-season friendly" / "Telekom Cup" matches.

- **Friendly rules are loose:** often **6+ substitutions** (sometimes unlimited or "rolling"), sometimes **shorter halves**, and a drawn match in a friendly *tournament* frequently goes **straight to a penalty shoot-out** for the bracket / trophy (no extra time).
- **The starting XI cannot be projected for 90 minutes** (RULES_SOCCER.md controls 7, 16): teams make wholesale changes at half-time or on the hour. Separate the **starting-XI phase** from the **mass-substitution phase**; if the substitution plan is unknown, widen second-half scoring and side tails and cap any participant-dependent thesis.
- Motivation is low and asymmetric (fitness work vs a team treating it as a trophy). Treat every friendly as its own one-off population — no transfer to or from competitive form.

### 7.1 ASEAN Club Championship ("ASEAN Hyundai Cup")

Unlike the above, the **ASEAN Club Championship** is a **competitive regional club competition** (Southeast Asian federation), with a group stage and a **two-legged final** (aggregate, ET + penalties). In the log: **senior men's final, second leg**. Treat it as competitive, not a friendly, but with a sparse-competition evidence ceiling.

---

## 8. Cross-competition settlement quick reference

| Competition | Type | Draw in regulation? | Level knockout → | 5 subs / VAR |
|---|---|---|---|---|
| Premier League | balanced league | yes | n/a | yes / yes |
| Carabao Cup | knockout | — | **straight to pens** (ET+pens in 2-leg SF and final) | yes / yes |
| Bundesliga / 2. Bundesliga | balanced league (+ relegation playoff) | yes | n/a | yes / yes |
| LaLiga | balanced league (H2H tiebreak) | yes | n/a | yes / yes |
| Serie A | balanced league (H2H tiebreak; spareggio) | yes | n/a | yes / yes |
| Coppa Italia | seeded knockout | — | ET + pens (2-leg SF) | yes / yes |
| Eredivisie | balanced league (+ Nacompetitie) | yes | n/a | yes / yes |
| Jupiler Pro League | split (points halved in title/Europe playoffs) | yes | n/a | yes / yes |
| Danish Superliga | split (points carried) | yes | n/a | yes / yes |
| DBU Pokalen | knockout | — | ET + pens | yes / partial |
| Championnat National (FRA 3) | balanced league | yes | n/a | yes / **no VAR** |
| Brasileirão Série A | balanced league (calendar year) | yes | n/a | yes / yes |
| Argentine Liga Profesional | Apertura/Clausura + zonal top-8 knockout | yes (league) | ET + pens (final phase) | yes / yes |
| Argentine reserve / Primera C | reserve / lower senior | yes | varies | no / **no VAR** |
| Roshn Saudi League | balanced league (10 foreign / 8 on pitch) | yes | n/a | yes / yes |
| Chinese Super League | balanced league (calendar year; "6655") | yes | n/a | yes / yes |
| Chinese FA Cup | knockout | — | pens (early), ET + pens (R5+) | yes / partial |
| Egyptian Premier League | split (21 clubs, 2025-26) | yes | n/a | yes / partial |
| Israeli Premier League | split | yes | n/a | yes / partial |
| Israel State Cup | knockout | — | ET + pens | yes / partial |
| Israel U19 Elite | youth league | yes | n/a | — / no |
| Kazakhstan Premier League | balanced league (16 clubs, 2026) | yes | n/a | yes / partial |
| Armenian Premier League | quadruple round-robin | yes | n/a | yes / partial |
| Armenian Cup | knockout (2-leg QF/SF) | — | ET + pens | yes / partial |
| Uzbekistan Pro League | 2nd-tier league | yes | n/a | yes / no |
| Sikkim SFA A Division S-League | regional semi-amateur league | yes | n/a | — / no |
| NWSL | balanced league + 8-team playoff | yes (league) | **full ET + pens** | yes / yes |
| MLS NEXT Pro | 3rd-tier league, **no draws** | **no** — 90' draw → shoot-out for bonus point | shoot-out | ~5 / no |
| Liga MX / Femenil | Apertura/Clausura + top-8 Liguilla | yes (league) | higher seed advances (QF/SF); ET+pens (final) | yes / yes |
| Leagues Cup | group + knockout, **no draws** | **no** — 90' draw → shoot-out | shoot-out (ET+pens usually in final only) | yes / yes |
| UEFA Conference League | qualifying/league phase/knockout | yes (league phase) | ET + pens; no away goals | yes / yes |
| UEFA Women's Champions League | qualifying + 18-team league phase + knockout | yes (league phase) | ET + pens; no away goals | yes / yes |
| UEFA Women's Europa Cup | qualifying + group + knockout (new) | yes (group) | ET + pens; no away goals | yes / partial |
| CONMEBOL Libertadores | group + knockout | yes (group) | **pens directly** (R16–SF); ET+pens (final) | yes / yes |
| FIFA Intercontinental Cup | single-match knockout ladder | — | ET + pens | yes / yes |
| Club friendlies / pre-season cups | exhibition | yes (or shoot-out for a trophy) | usually straight to pens | 6+ / usually no |
| ASEAN Club Championship | group + 2-leg final | yes (group) | ET + pens | — / partial |

## 9. Identity checklist (soccer)

Resolve before any rate or contract work, per RULES_SOCCER.md §1:

1. **Exact competition and season**, and therefore the **format type** (balanced league / split / Apertura-Clausura / group-knockout / cup) and the **rule package** in force (subs, VAR, foreign-player quota, points deductions).
2. **Population:** senior competitive vs friendly vs reserve/second-team vs youth — never pooled.
3. **Fixture type:** league match (draw live), single-leg knockout, two-leg tie (which leg, aggregate state), or a "no-draws" competition (MLS NEXT Pro, Leagues Cup, Libertadores knockouts before the final).
4. **Winner-decision rule** for this exact fixture: does it have **extra time**? does a level knockout go **straight to penalties**? if a two-leg aggregate is level, does the **higher seed advance** (Liga MX) or is there ET + penalties (UEFA)? **No away goals** anywhere current.
5. **Market endpoint:** is the contract "regulation / 90'+ stoppage" (the default), "advance/qualify", or "eventual winner incl. ET/penalties"? A shoot-out win is never a regulation win; an ET winner is never a regulation-winner call (RULES_SOCCER.md control 18).
6. **Table stakes** if the card touches a title/relegation/European place: the **tiebreak order** (GD-first vs head-to-head-first), whether a **playoff match** can occur, whether **relegation is suspended**, and whether it is decided by a **multi-season average**.
7. **Data environment:** VAR present or not; public data depth; sparse-competition evidence ceiling (RULES_SOCCER.md control 13) for the lower and exotic competitions above.

## Verified competition-metadata corrections - 2026-09-12

P-176/P-178/P-179 are Ligue 3 2026-27 round-four fixtures. P-179 was a 1-1 league draw, not a National 2 cup tie decided by shootout; in-play penalty goals must not become shootout settlement. P-233/P-234/P-235 were Chinese FA Cup quarterfinals on 1 September, not R16. These corrections are backed by exact L'Equipe and Xinhua/Titan records in audit_2026-09-12/historical_queue_evidence.md. They do not establish any corner total or require a general cup scoring coefficient. P-265's separate Leagues Cup semifinal ended Toluca 2-0 Leon, with first goal at 41 minutes, verified from club/competition reports; its later corner adjudication remains a documentary gap.

## 2026-09-15 — competition sections found missing by `P-374` and `P-377`

Reference only; changes no algorithm. Each fact below was read on an opened page on 2026-09-15; anything not confirmed is marked.

### UEFA Champions League (men's), 2026-27 — league phase and knockouts

- **League phase:** 36 clubs; each plays **eight matches, four home and four away, against eight different opponents** — two from each of four coefficient pots, one home and one away — in a single 36-team table. Win 3 / draw 1 / loss 0.
- **Progression:** places **1–8** go straight to the round of 16; **9–24** play two-legged knockout phase play-offs (9–16 seeded); **25–36** are eliminated from European competition.
- **Tiebreak order when level on points:** goal difference; goals scored; away goals scored; wins; away wins; higher points collected by league-phase opponents; superior goal difference of opponents; higher goals scored by opponents; lower disciplinary points; UEFA club coefficient. *(Source: Wikipedia "2026–27 UEFA Champions League league phase", which summarises the UEFA regulations; open the regulations before settling anything that turns on a tiebreak.)*
- **Calendar:** Matchday 1 8–10 September 2026 to Matchday 8 27 January 2027; play-offs February 2027; round of 16 March; quarter-finals April; semi-finals late April–early May; **final Saturday 5 June 2027, Estadio Metropolitano, Madrid** (UEFA.com).
- **Not confirmed on an opened page this pass:** knockout-tie procedure (aggregate, extra time, penalties, away goals). Verify against the UEFA regulations before any advance/qualify contract; 90-minute contracts are unaffected.
- **Settlement lane:** UEFA `matchstats` FAME feed (field owner for corners, attempts and possession — `SOURCES.md` §"2026-09-11"); ESPN `soccer/uefa.champions` corroborates.

### Guatemala — Liga Nacional (Liga Bantrab), Apertura 2026

- **Final phase (new for Apertura 2026):** **six** clubs qualify, down from eight, so the quarter-finals are removed. **1st and 2nd go straight to the semi-finals**; **3rd v 6th** and **4th v 5th** play the preliminary round (Prensa Libre; ClaroSports).
- **Level series:** in every series **except the final**, the tiebreak favours the club that finished higher in the regular phase (ClaroSports, quoted: "en todas las series, excepto en la final, el criterio de desempate favorecerá al club que haya terminado en mejor posición"). The final's procedure was not stated in the opened articles.
- **Calendar:** season opened on the weekend of 25–26 July 2026; regular phase ends 23 November; second leg of the final scheduled 20 December (could move to 27 December if a Guatemalan club reaches the Copa Centroamericana final).
- **Clubs:** San Pedro and Deportivo Suchitepéquez were promoted (Prensa Libre). **Club count and number of regular-phase rounds are not confirmed:** Prensa Libre gives 22 rounds; a second summary gave 10 clubs / 17 rounds, which is inconsistent. Confirm from the league's own table (`ligagt.com`) before using either number.
- **Settlement lane:** Liga Bantrab official feed owns the score; ESPN `soccer/gua.1` carries scores but **no match statistics**, so no corner or shot contract can be settled there (`P-377-C02`).

<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — source firewall precedence

All league-specific source instructions are subordinate to `SOURCES.md` PF-1/PF-2. Official competition/federation/club sources outrank derivative score sites. Sportsbook/betting/fantasy/DFS material and market-derived projections are never predictive evidence; if an older league note suggests otherwise, this section controls.
