# Prediction Mini Running Log — P-474 Onward — audit layer, Part B

> **2026-09-21 settlement / retrospective / audit layer for `PREDICTION_MINI_RUNNING_LOG_P474_ONWARD`.**
>
> The original P-474 to P-481 prediction cards and their 2026-09-20 settlements are preserved **unchanged** in the existing Google Doc `PREDICTION_MINI_RUNNING_LOG_P474_ONWARD.md` in this same folder. They were deliberately **not** re-uploaded, so that no preserved issued forecast could be altered in transit (`METHOD.md` §6).
>
> This audit layer is in two parts:
> - **Part A** — front matter, §1 Incomplete / Unsettled Logs, §2 Temporary-ID / Canonical-ID Conflict Logs, and the eight per-event `2026-09-21 independent re-audit` blocks that belong inside §3 Fully Settled Logs, one per card.
> - **Part B** — §4 General Learnings, Rule Changes, Observations and New Sources; §5 Document Update Mapping; §6 Settlement Lists; §7 Running Integrity Notes.
>
> The complete merged single-file version — original cards plus this audit layer, in the required order — is `PREDICTION_MINI_RUNNING_LOG_P474_ONWARD.md` at the Sports Research folder root.

## 4. General Learnings, Rule Changes, Observations, and New Sources

All figures below are **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** descriptive diagnostics on eight events across five sports. Eight events is not a sample from which calibration, edge or model quality can be inferred, and nothing here is a prospective validation. Every probability referenced is `UNVALIDATED_SUBJECTIVE`.

### 4.0 What the eight events actually show

#### Ranking metrics, by slate

| ID | Slate | Rank-1 | Hit@2 | Wins@2 | NDCG@2 | Rows | Winner call |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|
| P-474 | supplied (only ranked slate) | W | YES | 2/2 | 1.000 | 2 W / 2 L | **W** |
| P-475 | model-selected | W | YES | 2/2 | 1.000 | 4 W / 0 L | **W** |
| P-475 | supplied | W | YES | 1/2 | 0.613 | 2 W / 2 L | — |
| P-476 | model-selected | W | YES | 2/2 | 1.000 | 2 W / 2 L | **W** |
| P-476 | supplied | W | YES | 2/2 | 1.000 | 3 W / 1 L | — |
| P-477 | model-selected | W | YES | 2/2 | 1.000 | 2 W / 2 L | **W** |
| P-477 | supplied | W | YES | 1/2 | 0.613 | 2 W / 2 L | — |
| P-478 | model-selected | W | YES | 1/2 | 0.613 | 3 W / 2 L | **L** |
| P-478 | supplied | W | YES | 2/2 | 1.000 | 2 W / 2 L | — |
| P-479 | model-selected | W | YES | 2/2 | 1.000 | 4 W / 0 L | **W** |
| P-479 | supplied | W | YES | 1/2 | 0.613 | 2 W / 2 L | — |
| P-480 | model-selected | **L** | YES | 1/2 | **0.387** | 2 W / 3 L | **L** |
| P-480 | supplied | W | YES | 1/2 | 0.613 | 2 W / 2 L | — |
| P-481 | model-selected | W | YES | 2/2 | 1.000 | 5 W / 0 L | **W** |
| P-481 | supplied | W | YES | 2/2 | 1.000 | 2 W / 2 L | — |

**Model-selected slates (the free, information-bearing slates), 7 cards:** Rank-1 **6 / 7**; Hit@2 **7 / 7**; both-of-top-two **5 / 7**; rows **22 W / 9 L** across 31 rows; mean binary Brier **0.1965**.

**Winner calls, 8 cards:** **6 W / 2 L**; mean Brier **0.1684**. Both losses were soccer: P-478 Djurgården (p ≈ 0.602) and P-480 FC Nordsjælland (p ≈ 0.411 — a call the card itself did not rate above even money).

**NDCG@2 definition used here.** Binary relevance; DCG@2 = rel₁ + rel₂ / log₂3; IDCG@2 is drawn from the whole ranked slate's realised relevances (1.6309 when the slate contains two or more winners, 1.0 when it contains exactly one, undefined when it contains none). No slate in this mini log was a total blank, so NDCG@2 is defined everywhere.

#### The supplied-slate "record" is almost entirely mechanical — treat it accordingly

This is the most important measurement finding of the pass, and it applies to every future card that ranks a user-supplied four-contract slate.

Across the eight cards, the supplied slates contain **32 rows**. Of those:

- **28 rows form 14 strict complementary pairs** (Over/Under on a half-line, or spread/counter-spread). Exactly one row of each pair wins by construction. These pairs generated **14 guaranteed wins** regardless of forecast quality.
- **4 rows are genuinely informative** — the two moneyline/run-line pairs at P-474 (Guardians ML, Athletics +1.5) and P-476 (Angels ML, Twins +1.5), which are *not* complements because both can win when the favourite wins by exactly one run. These produced **3 W / 1 L**.

Total: 17 W / 15 L — of which **14 wins were arithmetic**. The honest decision-level reading is:

| Supplied-slate view | Result | Brier |
|---|---|---|
| Forced-pair preferred sides, counted once each (13 half-line/spread decisions) | 9 W / 4 L | 0.2007 |
| Non-complementary rows (4) | 3 W / 1 L | 0.1794 |
| P-476 Over 7.0 (push-capable, scored separately) | WIN | complete W/P/L 0.2255; decisive q = 0.5541 → 0.1988 |

`SCORING_AND_VALIDATION.md` §3 already requires the preferred side of a forced pair to be counted once in a decision score. The practical consequence for reporting is blunt: **never state a supplied-slate row record as if it were a performance figure.** A card that ranks four supplied contracts made of two complementary pairs will report "2 W / 2 L" whatever it forecasts. This mini log's honest supplied-slate signal is 13 near-coin-flip decisions at a 0.2007 Brier, which is worse than the free-slate 0.1965 — as expected, because the supplied lines sat close to the model's own centres on almost every card.

#### Where the forecasts were strong, and where they were not

**Strong, repeatedly and for stated reasons:**

- **Winner/side direction** — 6 of 8, including both cricket and NBL underdocumented competitions.
- **"Team X scores at least once" / team-total floors** — Rank #1 on three soccer cards, won on all three (P-478, P-481; P-480's equivalent row was Rank #2 and won).
- **Corners, modelled independently of goals** — 3 for 3 (P-478 11 v 7.5; P-480 9 v 7.5; P-481 Villarreal 7 v 4.5), and two of those three landed on cards where the goal-side view was wrong. Independence of the corner model from the goal model is doing real work and must be preserved.
- **Phase-to-innings separation in T20** — P-479's powerplay centre (~45 v realised 41) and innings corridor (145–175 v realised 150) were both right simultaneously.
- **Dependence reasoning on the top two** — P-476 named the exact one-run overlap state in advance and it occurred.

**Weak, repeatedly:**

- **Full-game and phase Unders.** Losses at P-475 (U176.5), P-476 (U8.5), P-477 (U191.5), P-480 (1H U1.5 and FT U3.5). Every one of these lost because the card's own documented upper-tail mechanism fired — late relief and extras, favourite bench offence, favourite perimeter burst, home first-half conversion. **Not one of these was an unforeseeable event.** In each case the mechanism was written down in prose and given no weight in the threshold calculation.
- **Central totals under-estimated the realised total on 6 of 8 cards** (P-474 8.34 v 18; P-475 175.9 v 187; P-476 7.35 v 11; P-477 186.7 v 201; P-480 2.68 v 5; P-481 2.98 v 4). Only P-478 (2.81 v 3) and P-479 (~160 v 150) were close or high. **This is a signal worth logging and is explicitly not yet a rule** — see §4.8. Eight events cannot establish a centre bias, `C-RUN-CENTRE-BIAS` is already development-only under `SCORING_AND_VALIDATION.md` §5, and a generic Over tilt is exactly what that section prohibits. But six of eight in the same direction, with a consistent stated mechanism (documented upper tails not carried into the threshold arithmetic), is a hypothesis with a mechanism attached rather than a bare streak.

### 4.1 Cross-sport learnings

1. **A documented tail that is not given weight is not modelled.** This is the single recurring cause of loss in this mini log. P-474's two-starter collapse, P-475's favourite bench ceiling, P-476's extras tail, P-477's perimeter burst and P-480's home first-half conversion were all *named in the card* and none was carried into the threshold arithmetic. The fix is mechanical: any mechanism named in the failure-mode prose must appear as a weighted branch in the frozen distribution, or be explicitly declared as excluded with a reason. This is recurring-mistake **M15** (control listed, not executed) and it appears on five of eight cards.
2. **Prefer the shorter failure path when two rows have similar probability.** P-480 ranked 1H Under 1.5 (needs the entire half to avoid a second goal) above rows that needed one event. P-475 ranked a full-game Under (needs both teams' totals to stay jointly low) above a favourite team-total Over already priced at 77%. Where stated probabilities are close, path geometry should break the tie toward the row with fewer ways to lose.
3. **An unavailability claim from a non-official aggregator is a hypothesis.** P-480 removed a player from the XI who started; P-476 correctly restored a player an obsolete flag had removed; P-481 treated a same-day third-party page as a team sheet. All three are the same failure class in different directions: availability source class was not carried through to the row.
4. **Team-level targets are robust to lineup error; player-level targets are not.** P-481 went 5 W / 0 L on a materially wrong XI because every row was team-level. That is a reason to be **more** disciplined about player props, not a reason to relax lineup verification.
5. **Independence between derivative models and the main outcome model is valuable and should be protected.** The corner models won twice on cards whose goal models were wrong. Deriving corners from possession/xG dominance would have destroyed that independence.
6. **Do not rank both ends of a narrow corridor as two of the "best" targets.** P-477 held Over 179.5 and Under 191.5 simultaneously around a 186.7 centre. They share one driver, cannot both win outside a ~12-point band, and are not two independent trials.
7. **Start-crossing handling held up.** Four of the eight cards (P-474, P-475, P-478, and P-479 in substance) were issued at or after the scheduled start. In every case the card failed preflight on `PF-EVENT-STATE`, labelled itself a late-issued research forecast, and admitted no live-state information. No settled row shows contamination. The exception process is working and should not be used as an argument for weakening the normal pregame gate — but note that the one card that issued cleanly pregame (P-476) was also the only card with both confirmed lineups. **Late issuance and thin participant evidence travel together.**

### 4.2 Sport-specific learnings

**Baseball (MLB).**

- When both starters carry a documented contact/HR tail, the joint two-starter-failure state needs explicit mass before any total or team-total Under is ranked (P-474). `RULES_BASEBALL` BB-B2/BB-B3/BB-B5 already require it.
- Any alternate Under must be tested against `P(tie after nine) + P(late relief-transition crossing)`, not just the distance from the central total (P-476). BB-B5/BB-B7 already require it.
- Integer totals were handled correctly at P-476: three-state W/P/L, no forced complement, push explicitly not counted as a win. Preserve this.
- The MLB Stats API (`schedule`, `game/{pk}/linescore`, `game/{pk}/boxscore`) settles every MLB field used in this mini log with no narrative interpretation. It should be the first settlement route.

**Basketball (WNBA / NBL).**

- A depleted underdog does not make the full game Under. Twice in this mini log the *favourite's* ceiling consumed the total budget (P-475 Atlanta 106; P-477 Sydney 111). The favourite's team-total Over and the full-game Under must be reconciled in the same joint states before the Under is ranked.
- Blowout states do not reliably suppress scoring: reduced defensive intensity plus productive bench minutes can raise the total while widening the margin (P-475 Borlase 18 in 19 minutes; P-477 six Kings in double figures).
- High-volume low-efficiency perimeter shooting by the losing side sustains pace while losing the game (P-477 Cairns 13-of-44). Margin and total can both go up together; this is a joint state, not two separate ones.
- Round-one / post-off-season / high-roster-turnover games deserve wider dispersion, not a narrower corridor (P-477). Candidate test only — see §4.8.

**Soccer.**

- Corners: keep them independent of the goal model. Build from corner-exposure rates plus score-state width. 3 for 3 here.
- Phase (first-half) totals built on small goal-timing samples are the weakest construct in the set (P-480). Shrink hard toward the competition/home-away phase base rate.
- Away-win branches for competent visiting sides are being compressed too far (P-478: 17.9% for a 34-point side away at a strong home team). Floor against the competition away-win base rate unless a named suppression mechanism justifies going below it.
- Substitution-driven defensive transition decided P-478 and contributed to P-480's fifth goal. A bench is not optional context in soccer; it is an input to the second-half distribution.
- Team-total "over 0.5" rows on the stronger side were the most reliable soccer row type in this mini log (3 for 3 at 0.75–0.84).

**Cricket (T20).**

- Powerplay and full-innings must be modelled as linked but distinct quantities. Modelling the innings as a multiple of the powerplay would have failed at P-479; modelling them separately got both right.
- A subdued powerplay followed by recovery is a real and common state, and a recent same-fixture example of it (36/2 → 190/4) is a width argument, not a centre shift. The card got this right.
- **New:** when every supplied contract is conditioned on a named team batting first, the toss is an activation gate. P-479 issued four toss-conditional rows without the toss and was one coin-flip from a `CONDITION NOT MET` outcome like P-445.

### 4.3 Potential rule changes

Ordered by strength of evidence. Nothing here is asserted as validated; each is a proposal with its evidence and its status.

| # | Proposal | Evidence in this mini log | Status | Target document |
|---|---|---|---|---|
| R-A | **Named-mechanism closure.** Any mechanism named in a card's failure-mode prose must appear as a weighted branch in the frozen distribution or be explicitly declared excluded with a reason. | 5 of 8 cards (P-474, P-475, P-476, P-477, P-480) | **Strong — execution rule, adds no coefficient.** Recommend adoption. | `METHOD.md` §4 field 3; `CONTROLS.md` |
| R-B | **Availability source-class tagging.** Every availability row carries `source_class` and `field_owner`; a non-official aggregator absence is tagged `UNVERIFIED_ABSENCE` and may not remove a player from a modelled XI on its own. | P-480 (Anyembe started while listed unavailable); P-476 (correct removal of a stale flag); P-481 | **Strong — enforces an existing `METHOD.md` §1.1 requirement that was not carried through.** Recommend adoption. | `METHOD.md` §1.1; `RULES_GENERAL.md` §16; `DATA_SOURCE_REGISTER.md` |
| R-C | **Lineup-projection hierarchy.** The club's own official report of its most recent match, cross-checked against a current independent feed, outranks a same-day third-party lineup page. Recency is not confirmation. | P-478 22/22 exact by the first method; P-481 3-of-4 attackers wrong by the second | **Strong, but n = 2.** Recommend adoption as a source-hierarchy rule; record as a standing test. | `RULES_SOCCER.md`; `SOURCES.md`; `DATA_SOURCE_REGISTER.md` |
| R-D | **Toss as an activation gate in cricket** when the supplied slate is conditioned on a named team batting first: recover it, or rank explicitly conditional on activation and state the activation probability. | P-479; precedent P-445 (`CONDITION NOT MET`, all four rows NO ACTION) | **Strong — closes a known failure mode already realised once.** Recommend adoption. | `RULES_CRICKET.md`; `LEAGUE_RULES_CRICKET.md` |
| R-E | **Phase-total shrinkage floor.** A phase total supported only by a goal-timing streak of fewer than ~10 events may not depart from the competition/home-away phase base rate by more than a stated shrinkage allowance, and the allowance must be printed. | P-480 (75% on five goals and two matches) | **Moderate — mechanism clear, magnitude not derived.** Adopt the *disclosure* requirement now; the magnitude stays `NOT_YET_DERIVED`. | `RULES_SOCCER.md`; `RECENCY_AND_REBOUND.md` (`R-1` family) |
| R-F | **Corridor rows count once.** An upper Under and a lower Over drawn from the same frozen centre are one corridor decision, not two targets. | P-477 | **Moderate.** Consistent with `SCORING_AND_VALIDATION.md` §3. | `SCORING_AND_VALIDATION.md` §3; `METHOD.md` §4 field 4 |
| R-G | **Forced-pair reporting discipline.** A supplied-slate row record may not be presented as a performance figure; the preferred side of each complementary pair is counted once and the mechanical component is stated. | All 8 cards; 14 of 17 supplied wins were arithmetic | **Strong — a reporting-honesty rule, no forecasting effect.** Recommend adoption. | `SCORING_AND_VALIDATION.md` §3; `EXTERNAL_LOGGING_WORKFLOW.md` |
| R-H | **Away-win base-rate floor** in soccer for a competent visiting side, absent a named suppression mechanism. | P-478 (17.9%) | **Weak — n = 1.** Log as a candidate test; do not adopt. | `RULES_SOCCER.md` (candidate) |

**Explicitly rejected as rule candidates:**

- **Any generic Over tilt or fixed centre adjustment.** Six of eight centres were low, but `SCORING_AND_VALIDATION.md` §5 prohibits an unexplained signed lean, and one mini log cannot establish a centre bias. The mechanism (unweighted tails) is addressed by R-A, which is a process fix, not a coefficient.
- **Any rule designed to make one side of every total win.** The user's own brief prohibits it and it would be unjustifiable: the Under losses here were caused by specific, identifiable, fixable mechanism omissions, not by the Under side being structurally wrong.
- **Down-ranking Rank-#1 candidates generally after P-480.** One Rank-1 loss in eight events, with an identified cause, is not evidence that the ranking objective is wrong.

### 4.4 Algorithm improvements

1. **Threshold-crossing budget as a required output for every ranked total.** Instead of "centre 7.35, line 7.0, gap +0.35", print the mass of each named state that crosses the threshold: `P(tie after nine) = 0.1425`, `P(late relief transition adds ≥2) = …`, and so on. The centre-and-gap display (already mandated by the 19 Sep display directive) tells you where the distribution sits; it does not tell you which states move it across the line. The four Under losses in this mini log are all threshold-crossing failures, not centre failures.
2. **Joint budget reconciliation before ranking a mismatch total.** `P(favourite TT ≥ x)` against `P(underdog TT ≤ total − x)` in the same frozen states, printed. P-475 would have shown the contradiction immediately.
3. **Path-geometry tiebreak.** Where two ranked rows are within a stated tolerance of each other, rank the one with fewer failure paths first, and record that the tiebreak was applied.
4. **Bench/substitution branch with explicit weight** in soccer winner and team-total distributions whenever the favourite is expected to chase or protect a lead.
5. **Keep derivative models structurally independent** of the primary outcome model. Corners earned their place here precisely because they were not derived from the goal model.

### 4.5 Source improvements

**Newly demonstrated in this pass, with what each is good for.**

| Source / route | Best used for | Evidence from this pass |
|---|---|---|
| `site.api.espn.com/apis/site/v2/sports/soccer/{league}/summary?event={id}` | **Confirmed starting XIs, full benches, substitutions with minutes, goal times and assists, and `wonCorners`** — the complete settlement and lineup-audit package for an ESPN-covered soccer competition, in one keyless call | Settled P-478, P-480 and P-481 finals, halftimes, goal minutes, corner counts (4-7, 4-5, 7-1) and both team sheets for each |
| `site.api.espn.com/.../soccer/{league}/scoreboard?dates=YYYYMMDD` | Terminal-state confirmation (`Full Time`) with explicit status, not just a score | Confirmed all three soccer finals |
| `statsapi.mlb.com/api/v1/game/{pk}/linescore` and `/boxscore` | Innings played, per-inning runs, team totals, margins, individual pitcher lines — settles MLB totals, run lines and pitcher props without narrative | Settled P-474 and P-476 including the 11-inning endpoint and both `5 K` lines |
| `site.api.espn.com/.../basketball/wnba/summary?event={id}` | **Per-player `starter` boolean and `didNotPlay` flag**, plus full team shooting splits | Resolved Natasha Cloud DNP and confirmed Atlanta's exact starting five at P-475 |
| ESPNcricinfo full scorecard via `r.jina.ai` | **Explicit `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)` match note**, toss, fall of wickets, did-not-bat list | Settled P-479's 41/1 powerplay and confirmed Chapman/Miller absent from the XI |
| Austadiums exact-event records | Independent third lineage for Australian fixtures where ESPN has no coverage | Corroborated P-477 111-90 with venue, date and start time |

**Sources demoted or flagged by this pass.**

- **CricketWorld** — supplied P-479's powerplay field on 2026-09-20; on 2026-09-21 it returns a bot-verification wall through both the direct route and the text proxy. Reclassify as *intermittently available*; do not rely on it as a required lineage for a phase field when ESPNcricinfo carries the same match note.
- **WinDrawWin / BetStudy / TotalCorner** — used to settle the P-478 corner row. They gave the right number, but a registered structured source publishes the same field and was not used. Keep them as a last-resort research-only fallback, explicitly below the ESPN `wonCorners` route, and never as predictive evidence.
- **AS same-day lineup page (`as.com/.../alineaciones/`)** — must remain `PROJECTED` unless it exposes an explicit confirmation marker. It was materially wrong at P-481.
- **Third-party availability feeds (generic)** — wrong on Anyembe at P-480. Demote to corroboration; official club matchday squad announcements own the field.
- **NBL public schedule shell** — displays `LIVE NOW` on fixtures that have not started. Confirmed again this pass. Never an event-state authority.
- **Syndicated recaps** — the BBC-via-Yahoo P-479 summary misnamed Devon Conway as "Paul Conway". Recaps do not own player-level fields; scorecards do.
- **The structured soccer event feed used at issue time** — still returned `Scheduled` after kick-off had passed at P-478. Adequate as one lineage; not sufficient alone for event state.

### 4.6 Data-quality observations

1. **Confirmed lineups were obtained for both sides on exactly one of eight cards** (P-476). That is the headline data-quality number of this mini log. On P-478 the projection happened to be exact; on P-481 it was materially wrong; on the remaining five it was uncapturable or capped.
2. **A bench was obtained on zero of the five cards where a bench mattered.** Benches decided or contributed to the outcome at P-478 (both Elfsborg's and Djurgården's), P-480 (Kleis-Kristoffersen's 81' goal after a 70' introduction), P-475 (Borlase 18 from the bench), P-481 (Mikautadze's 86' goal after a 67' introduction) and P-477 (six Kings in double figures).
3. **Intra-provider cache inconsistency is normal, not exceptional.** MLB's all-club lineup index had full orders while its own team pages showed TBD (P-476); a club's official preview promised a squad one hour before kick-off and never refreshed through the accessible route (P-478); the structured soccer feed showed `Scheduled` after kick-off (P-478). Each was correctly logged rather than hidden. This is a retrieval-latency pattern that should be expected and planned around, not treated as an anomaly each time.
4. **Every settlement in this mini log now rests on at least four distinct lineages**, and every derivative field (corners, powerplay) is settled from a source that publishes the field directly rather than from an inference.
5. **Coaching/manager information was obtained on zero of eight cards.** On most it was genuinely immaterial. On P-481 it was not: the card identified a short-rest rotation risk and then published a single non-rotated XI.

### 4.7 Recurring blind spots

Mapped to the existing recurring-mistake registry so repeat offences are countable rather than re-described.

| Registry item | Where it appears in this mini log | Repeat? |
|---|---|---|
| **M14** — total probability not derived from the card's own centre/width | P-475 (Under ranked against the card's own 77% favourite TT Over), P-476 (U8.5 against the card's own tie mass) | Yes — previously logged 2026-09-09 |
| **M15** — control listed but not executed | P-474, P-475, P-476, P-477, P-480, and the P-478 source-selection variant | **Yes, and dominant — 6 of 8 cards.** This is the highest-frequency defect in the set |
| **M17** — small-sample rate used as direction | P-480 (five goals, two matches → 75%) | Yes |
| **M19** — published lineup not retrieved / projected treated as confirmed | P-481 squarely; P-480's availability variant; P-474/P-475/P-477/P-478/P-479 as known missingness correctly labelled | Yes |
| **M11** — unit-performance uncertainty converted into an Over lean | Not observed. Uncertainty was represented as width on every card | No — this control is holding |
| **M10** — kill path stated as prose rather than a weighted branch | This is the mechanism behind M15 here; the kill paths were written and not weighted | Yes |

**New blind spot not previously in the registry — candidate M20: "complementary-pair record reported as performance."** A supplied slate built from complementary pairs produces a fixed row record independent of forecast quality, and reporting it alongside free-slate results invites a false read. Proposed as an addition to the registry with the R-G reporting rule.

### 4.8 Items requiring more evidence before becoming formal rules

1. **Central-total under-estimation.** Six of eight centres sat below the realised total. Mechanism (unweighted documented tails) is plausible and is addressed by R-A as a *process* fix. **Do not convert into a coefficient.** Required before any promotion: per-sport separation, actual means versus medians, a chronological out-of-sample block, and a comparison against the frozen empirical baseline per `SCORING_AND_VALIDATION.md` §4. Status: **development observation, continues `C-RUN-CENTRE-BIAS`.**
2. **Round-one / post-off-season variance widening (basketball).** n = 1 (P-477). Needs a systematic sample of opening-round games across NBL/NBA/WNBA seasons with a pre-specified dispersion metric. Status: **candidate test.**
3. **Away-win base-rate floor (soccer).** n = 1 (P-478). Needs the actual competition away-win base rates and a check of how often recent cards have gone below them. Status: **candidate test (R-H).**
4. **Lineup-projection hierarchy (R-C).** n = 2, but with a clear mechanism and an unusually clean contrast (22/22 versus 3-of-4 wrong). Recommend adopting as a source-hierarchy rule now — it costs nothing and removes a known failure — while continuing to record hit rates for both methods.
5. **Whether team-level target selection should be formalised as a hedge against lineup uncertainty.** P-481 suggests it, but "choose robust targets" can degenerate into choosing uninformative ones. Needs a definition that distinguishes robustness from triviality before it can be a rule. Status: **not ready.**

### 4.9 Open handles outside this mini log — 2026-09-21 re-probe

Recorded here because Phase 8 requires checking whether other entries still require settlement. **None of these belongs to this mini log, and none blocks it.**

The 23 primary handles (Part-2 custody 9, Part-3 custody 13, Part-4 custody 1) plus the documentary/period audits remain open. The Part-3 soccer corner handles are **not open because the value is unknown** — ESPN values are already recorded against them (P-399 17, P-401 17 / IFK 8, P-407 Brugge 9, P-409 Troyes 5, P-410 Leipzig 8, P-419 2+2, P-430 Al Ain 2). They are open because each card **pre-registered a specific field owner** (Lega Serie A, Allsvenskan/SEF, Pro League, LFP, DFL, AFC) and §16.10(j) forbids booking at a provider that was not pre-registered. Refusing to book them is the correct, outcome-independent application of the rule — at P-430 the unbooked evidence points to a *loss*, which is the clearest possible demonstration that the rule is not being applied opportunistically.

Re-probe results, 2026-09-21:

| Pre-registered field owner | Route attempted | Result |
|---|---|---|
| Allsvenskan (P-401, P-419) | `allsvenskan.se/match/6529990` | **HTTP 404** — still unreachable |
| SEF / Everysport API (P-401, P-419) | `api.everysport.com/v1/events/{id}` | **HTTP 401** — requires an API key |
| DFL / Bundesliga (P-410) | `bundesliga.com` match facts | **HTTP 403** — still unreachable |
| Pro League (P-407) | `proleague.be` | Site reachable, no exact-event corner field exposed on the accessible route |

**Structural observation worth escalating.** Pre-registering a settlement provider that does not publish the target field creates a permanently unsettleable row. Seven derivative rows have now been open for a week or more with the correct value already in hand from a registered structured source, purely because the pre-registration named the wrong owner. The rule protects against outcome-driven provider shopping and should be kept. But the pre-registration step should require a check that the named provider actually publishes the field — otherwise the control converts a solvable settlement into a permanent gap. Proposed as a `RULES_GENERAL.md` §16.10 clarification: **a settlement provider may only be pre-registered for a derivative field if that provider is known to publish that field**; where it does not, pre-register the structured route that does (for soccer corners, ESPN `wonCorners`).

### 4.10 Audits reviewed and archived in this pass

Reviewed against their own closure statements and against the current authority chain (`METHOD.md` MDS-2026.09.19-v4.3 / CR-2026.09.19-4, `AUDIT_IMPLEMENTATION_2026-09-19.md`). Archived where closed, superseded or redundant **and** not cited by a currently governing operational document. Files cited only by `LEARNING_REGISTER.md` were treated as archivable, because that register is itself an evidence archive and `METHOD.md` §9 classifies dated retrospectives and audit snapshots as evidence, not active instructions.

| Document | Disposition | Reason |
|---|---|---|
| `PREDICTION_MINI_RUNNING_LOG_P452_ONWARD.md` (folder) | **ARCHIVED** | All 22 entries settled with retrospectives complete; superseded by this mini log; next ID P-474 confirmed contiguous |
| `AUDIT_CHANGELOG_2026-09-06.md` | **ARCHIVED** | Its one outstanding item (retro-tagging ~86 pre-`L-095` lessons) was formally closed as not-to-be-done in `AUDIT_IMPLEMENTATION_2026-09-19.md` §4 |
| `AUDIT_CHANGELOG_2026-09-06_OVERHAUL.md` | **ARCHIVED** | Historical record of a pass implemented in full the same day; no active citation |
| `AUDIT_CHANGELOG_2026-09-07.md` | **ARCHIVED** | Closed settlement/ledger pass; cited only by the learning register |
| `AUDIT_CHANGELOG_2026-09-09.md` | **ARCHIVED** | Closed; no active citation |
| `AUDIT_CHANGELOG_2026-09-11.md` | **ARCHIVED** | Its one outstanding item (`statsapi battingOrder` lineup route "not yet demonstrated pre-game") was closed as demonstrated in `AUDIT_IMPLEMENTATION_2026-09-19.md` §3 |
| `AUDIT_CHANGELOG_2026-09-12.md` | **ARCHIVED** | Closed; no active citation |
| `COMPREHENSIVE_RETROSPECTIVE_2026-08-22.md` | **ARCHIVED** | P-001–P-060 retrospective under MDS-2026.08.22-v1.1; superseded twice over |
| `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-02.md` | **ARCHIVED** | Superseded by the 2026-09-05 and 2026-09-12 audits |
| `GAME_LOG_LEDGER_2026-09-06.md` | **ARCHIVED** | Superseded by `GAME_LOG_STATUS_CURRENT.md`; no active citation |

**Retained in place despite being historical**, because a currently governing document links to them and moving them would break an active reference: `AUDIT_CHANGELOG_2026-09-05.md` (cited by `AGENT_ROLE_AND_TASK.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`), `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md` (`RULES_GENERAL.md`, `DATA_SOURCE_REGISTER.md`), `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-12.md` (`GAME_LOG_STATUS_CURRENT.md`, `SOURCES.md`, `PERFORMANCE_ELIGIBILITY_POLICY.md`), `FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md`, `GAME_LOG_BLINDSPOT_REVIEW_2026-09-06.md`, `GAME_LOG_STATUS_INDEX_2026-09-05.md`, `IMPROVEMENT_PLAN_2026-09-06.md`, `PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md`.

**Retained as current authority, not archivable:** `METHOD.md`, `SCORING_AND_VALIDATION.md`, `CONTROLS.md`, `CONTROL_MANIFEST_2026-09-19.md`, `FORECAST_PREFLIGHT_MANIFEST.md`, `MODEL_REVIEW_2026-09-17.md` (linked from `METHOD.md` and `README.md`), `AUDIT_IMPLEMENTATION_2026-09-17.md` (linked from `METHOD.md` §10), `AUDIT_IMPLEMENTATION_2026-09-19.md` (the current control revision ledger), `GAME_LOG_STATUS_CURRENT.md`, all `RULES_*.md`.

**Findings judged outdated or redundant during this review:**

- `AUDIT_CHANGELOG_2026-09-11.md`'s claim that the `statsapi battingOrder` lineup route was "proposed, not yet demonstrated pre-game" is **outdated** — it was demonstrated on 2026-09-19. Ironically, P-474 still fell back to a CBS/STATS secondary rather than using it, which is why this is listed under §4.5 as an execution gap.
- The `L-095` / `L-096` backlog item ("retro-tag ~86 pre-`L-095` lessons") is **closed as not-to-be-done** and should not be reopened; the correct unit was active controls, which are now classified in `CONTROLS.md`.
- `GAME_LOG_STATUS_INDEX_2026-09-05.md`'s "6/25 top-two and 13/13 main-line O/U" summaries are **superseded** by explicitly enumerated denominators, and — in light of §4.0 — any such headline O/U rate computed over complementary pairs should be treated as structurally inflated regardless of which audit produced it.
- `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md`'s settlement-only performance-eligibility framing is **superseded** by the 2026-09-12 LEARNING_ONLY directive and by `PERFORMANCE_ELIGIBILITY_POLICY.md`.

## 5. Document Update Mapping

Where each learning should eventually be incorporated. **No governing document was modified by this pass.** The mini log is the only file rewritten; archiving moved closed audit files without editing their contents.

| # | Learning / change | Target document | Section | Type |
|---|---|---|---|---|
| 1 | R-A named-mechanism closure — a named failure mechanism must be a weighted branch or an explicit exclusion | `METHOD.md` | §4 compact object, field 3 (Joint distribution) | Execution rule |
| 2 | R-A operational check | `CONTROLS.md` | per-card gate list | New gate |
| 3 | R-B availability source-class tagging; `UNVERIFIED_ABSENCE` label | `METHOD.md` §1.1; `RULES_GENERAL.md` §16 | provenance fields / participant freeze | Enforcement of existing requirement |
| 4 | R-B register entry for third-party availability feeds | `DATA_SOURCE_REGISTER.md` | availability field ownership | Source demotion |
| 5 | R-C lineup-projection hierarchy (club's own last official XI > same-day third-party page) | `RULES_SOCCER.md`; `SOURCES.md`; `DATA_SOURCE_REGISTER.md` | lineup retrieval | Source hierarchy |
| 6 | R-D toss as activation gate for batting-first-conditional slates | `RULES_CRICKET.md`; `LEAGUE_RULES_CRICKET.md` | activation / contract identity | New blocking gate |
| 7 | R-E phase-total shrinkage disclosure (magnitude `NOT_YET_DERIVED`) | `RULES_SOCCER.md`; `RECENCY_AND_REBOUND.md` | phase totals / `R-1` family | Disclosure requirement |
| 8 | R-F corridor rows count once | `SCORING_AND_VALIDATION.md` §3; `METHOD.md` §4 field 4 | decision counting | Scoring clarification |
| 9 | R-G forced-pair reporting discipline; no supplied-slate row record presented as performance | `SCORING_AND_VALIDATION.md` §3; `EXTERNAL_LOGGING_WORKFLOW.md` | decision metrics / log presentation | Reporting-honesty rule |
| 10 | Candidate **M20** "complementary-pair record reported as performance" | `LEARNING_REGISTER.md` recurring-mistake registry | M-series | New registry entry |
| 11 | M15 repeat count (6 of 8 cards) | `LEARNING_REGISTER.md` | M15 evidence rows | Evidence update |
| 12 | Threshold-crossing budget as required output for every ranked total | `METHOD.md` §4 field 4; `RULES_BASEBALL.md`; `RULES_BASKETBALL.md`; `RULES_SOCCER.md` | totals presentation | Algorithm/output change |
| 13 | Joint budget reconciliation (favourite TT Over vs full-game Under) | `RULES_BASKETBALL.md` controls 11/17/18 | mismatch totals | Execution reinforcement |
| 14 | Path-geometry tiebreak between close-probability rows | `METHOD.md` §4 field 4 | ranking | Ranking clarification |
| 15 | Bench/substitution branch carries explicit weight in soccer winner and team-total distributions | `RULES_SOCCER.md` | score-state transitions | Execution reinforcement |
| 16 | Preserve independence of the corner model from the goal model | `RULES_SOCCER.md` | corner process | Preserve-as-is note |
| 17 | MLB two-starter joint-collapse branch | `RULES_BASEBALL.md` BB-B2/BB-B3/BB-B5 | starter states | Execution reinforcement |
| 18 | MLB alternate-Under tie/extras crossing mass | `RULES_BASEBALL.md` BB-B5/BB-B7 | relief transition, extras | Execution reinforcement |
| 19 | ESPN soccer `summary?event=` as primary settlement + lineup route (`wonCorners`, XIs, benches, subs, goal times) | `DATA_SOURCE_REGISTER.md`; `SOURCES.md`; `RULES_SOCCER.md` | settlement routes | New/promoted source |
| 20 | MLB Stats API `linescore`/`boxscore` as first MLB settlement route | `DATA_SOURCE_REGISTER.md`; `RULES_BASEBALL.md` | settlement routes | New/promoted source |
| 21 | ESPN WNBA `summary?event=` `starter`/`didNotPlay` for participation settlement and pre-tip availability testing | `DATA_SOURCE_REGISTER.md`; `RULES_BASKETBALL.md` | availability/settlement | New/promoted source |
| 22 | ESPNcricinfo `Powerplay 1` match note as registered T20 phase-field route; CricketWorld reclassified intermittent | `DATA_SOURCE_REGISTER.md`; `RULES_CRICKET.md` | phase settlement | Source promotion + demotion |
| 23 | Austadiums as independent third lineage for Australian fixtures; NBL schedule shell is never an event-state authority | `DATA_SOURCE_REGISTER.md`; `RULES_BASKETBALL.md` | event state | New source + source warning |
| 24 | WinDrawWin / BetStudy / TotalCorner demoted below the ESPN `wonCorners` route; research-only fallback, never predictive | `DATA_SOURCE_REGISTER.md`; `SOURCES.md` | corner fields | Source demotion |
| 25 | Pre-registered settlement provider must be known to publish the target field | `RULES_GENERAL.md` §16.10 | derivative settlement | Rule clarification — unblocks 7 stalled rows |
| 26 | P-452–P-481 canonical import and register extension; the `next ID P-438` line in the status register is stale | `PREDICTION_LOG_COMBINED_4.md`; `GAME_LOG_STATUS_CURRENT.md` | queue / canonical index | Ledger integrity — **do this before issuing P-482** |
| 27 | Late issuance and thin participant evidence co-occur; keep the start-crossing exception but do not weaken the pregame gate | `EXTERNAL_LOGGING_WORKFLOW.md`; `METHOD.md` §3 | issuance | Process observation |
| 28 | Candidate tests: round-one variance widening; away-win base-rate floor; central-total under-estimation | `LEARNING_REGISTER.md` | prospective-test archive | Candidate tests, not rules |

**Proposed new document — not created.** `TOTALS_THRESHOLD_BUDGET.md`. Purpose: a single cross-sport specification for the threshold-crossing budget (item 12) — which states must be enumerated per sport, how their mass is printed, and how the budget is reconciled against team-total rows before a total is ranked. Justification: items 12, 13, 17 and 18 are the same requirement re-expressed in four sport files, and the four Under losses in this mini log are all instances of it. A single specification referenced from each `RULES_<SPORT>.md` would stop it being restated inconsistently. **This is a proposal only; no document was created.**

## 6. Settlement Lists

### Settled logs — first to most recent

1. **P-474** — Athletics @ Cleveland Guardians, MLB — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Cleveland 12-6; total 18. Supplied slate 2 W / 2 L; Rank-1 WIN; winner WIN.
2. **P-475** — Chicago Sky @ Atlanta Dream, WNBA — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Atlanta 106-81; total 187. Model slate 4 W / 0 L; supplied 2 W / 2 L; Rank-1 WIN both slates; `TOP_OU_REVIEW` fired on supplied Under 176.5; winner WIN.
3. **P-476** — Minnesota Twins @ Los Angeles Angels, MLB — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Angels 6-5 in 11 innings; total 11. Supplied 3 W / 1 L; model slate 2 W / 2 L; Rank-1 WIN both slates; winner WIN.
4. **P-477** — Sydney Kings vs Cairns Taipans, NBL — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Sydney 111-90; total 201. Model slate 2 W / 2 L; supplied 2 W / 2 L; Rank-1 WIN both slates; winner WIN.
5. **P-478** — Djurgårdens IF vs IF Elfsborg, Allsvenskan — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Elfsborg 2-1; HT 0-1; corners 4-7 (11). Model slate 3 W / 2 L; supplied 2 W / 2 L; Rank-1 WIN; winner LOSS.
6. **P-479** — Edinburgh Castle Rockers vs Belfast Wolves, ETPL Final — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Belfast 150/5 (PP 41/1); Edinburgh 151/3 in 18.4, won by 7 wickets. Model slate 4 W / 0 L; supplied 2 W / 2 L; Rank-1 WIN both slates; winner WIN.
7. **P-480** — Viborg FF vs FC Nordsjælland, Superligaen — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Viborg 4-1; HT 3-1; corners 4-5 (9). Model slate 2 W / 3 L; supplied 2 W / 2 L; **Rank-1 LOSS — enhanced Rank-1 + `TOP_OU_REVIEW` completed**; winner LOSS.
8. **P-481** — Villarreal vs Levante, La Liga — **SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21.** Villarreal 3-1; HT 1-1; corners 7-1. Model slate 5 W / 0 L; supplied 2 W / 2 L; Rank-1 WIN both slates; winner WIN. Records a confirmed pre-game lineup defect despite the clean result.

### Logs still awaiting settlement — first to most recent

**None.** No entry in this mini log is unsettled, unresolved, live, delayed, suspended, postponed, abandoned or cancelled.

For completeness, the open items that exist **elsewhere** in the ledger and are not part of this mini log are listed in §4.9: 23 primary handles (Part-2 custody 9, Part-3 custody 13, Part-4 custody 1 — `P-430-C05`) plus the documentary/period audits, including `P-255-C05` and `P-256-C05` as `UNRESOLVED_PERIOD` and `P-418` as `RESULT_NOT_RECOVERED`. Re-probed 2026-09-21; all pre-registered field owners remain unreachable; no handle changed state.

## 7. Running Integrity Notes

- Governing methodology remains **MDS-2026.09.19-v4.3 / CR-2026.09.19-4**. Historical cards keep the method/control version under which they were issued; nothing was retrofitted.
- The dataset remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. Settlement does not confer performance eligibility (`METHOD.md` §7). No EV, ROI, edge or calibration claim follows from anything in this document.
- **No issued forecast, probability, rank, selection, reasoning or canonical ID was altered by the 2026-09-21 pass.** Every original pre-game card is preserved verbatim. All additions are dated, appended settlement and audit material, per `METHOD.md` §6.
- **No settled row changed.** The re-audit confirmed all eight finals and every graded row.
- **Three new findings were added** that the 2026-09-20 pass did not have: the P-480 Anyembe pre-game availability error; the P-478 lineup-projection result (22 of 22 names correct) and the source-hierarchy conclusion that follows from contrasting it with P-481; and the P-478 corner-evidence downgrade, where betting-branded pages were used to settle a field that a registered structured source publishes.
- **Two settlement-evidence upgrades were applied** without changing any outcome: soccer corner fields now rest on ESPN `wonCorners`, and the P-479 powerplay field now rests on the ESPNcricinfo match note (CricketWorld has since gone behind a bot wall and is no longer reproducible).
- **One pre-game uncertainty was resolved:** Natasha Cloud (P-475) did not play.
- Market odds, line movement, betting tips, tipsters and fantasy/DFS material were **not** admitted as predictive evidence on any card. Betting-branded pages appear only as historical settlement cross-checks at P-478, and this pass replaces them with a structured non-market route.
- **No governing methodology file, rules file, canonical prediction log or register was edited.** Nine closed or superseded audit documents and the fully settled P-452 mini-log folder were moved to the Drive archive with their contents unchanged; every proposed rule change is recorded in §5 as a mapping, not applied.
- **Ledger action required before the next issue:** import P-452–P-481 into `PREDICTION_LOG_COMBINED_4.md`, extend `GAME_LOG_STATUS_CURRENT.md` past P-451, and remove the stale "next ID `P-438`" line. Under `METHOD.md` §3 step 7 an overdue unregistered external log blocks the next forecast.
- Next intended prediction ID: **P-482**, subject to that reconciliation.
