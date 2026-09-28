# Tennis analysis rules — dated history to 2026-09-28

**Archived 2026-09-28 (md-only restructure).** These are the dated sections that followed the competition-rules section of `RULES_TENNIS.md`, moved verbatim. They are the evidence record. The live rules are §0 of `RULES_TENNIS.md`, and nothing here reinstates a rule that §0 or `CURRENT_RULES.md` §I withdraws.

## September 5 settlement learning — prospective SFA amendment


P-287 requires an immediate arithmetic/contract repair under L-068. For every representative set sequence, store games A, games B, total, signed game margin, sets won and each supplied row's outcome. Sum tiebreak sets as 7+6=13 games; tiebreak points in parentheses are not additional games. Validate examples before they support the rank.


A player winning 0–6, 0–6, 7–6, 7–6, 7–6 wins three sets but loses aggregate games 21–30; +2.5 fails. A quick underdog win can cover and stay Under. A five-set match can also contain late one-sided sets: Paul beat Bublik by six games after winning the last two 12–4. Total games, match winner and game handicap must therefore be derived jointly, without an automatic close/long equivalence.


This corrects §9.6(7), whose former wording supplied the same false shortcut as the card. P-287's correct Over/winner does not erase the defect. Do not infer injury, fatigue or reduced motivation from late-set scores alone. C-P293-TEN-ALLOCATION is a candidate, count zero; the existing P-275 recovery-length test does not gain a completion merely from this provenance correction: no executed frozen comparator has been recorded.




Full evidence and frozen-card comparisons: [September 5 audit](archive/audit_documents_implemented_2026-09-25/COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 6 settlement learning — cross-sport gates instantiated


No tennis-specific defect was evidenced in the `P-294`–`P-305` cohort; `P-291` (Shelton d. Shapovalov, `Shapovalov +5.5 games` **WIN** at 25–20) settled cleanly. The v3.7 cross-sport gates are instantiated here so that tennis cards carry the same disclosures.


**Tennis-native tail example.** A total-games `Under` is exposed to the *set-count* tail, not the game-count tail: a best-of-five match that goes the distance adds games in large discrete steps rather than smoothly, so "second-highest set count in the L10 × games per set at the median" is a useful **first-pass disclosure heuristic**, not an exact figure — it misses close-set variation (a 7-6 set contributes far more games than a 6-1 set) and does not respect legal score-path constraints. **Correction, 2026-09-06(d):** where precision matters, enumerate the actual legal score paths for the match's best-of format directly and sum games per path, rather than relying on the set-count shortcut alone. Conversely a total-games `Over` is exposed to the straight-sets branch and to retirement, which under `G22` is its own termination branch with its own action terms — and where retirement/walkover terms are `NOT SUPPLIED`, the row is graded under stated standard rules per `G36.1` rather than left `UNRESOLVED`.


**Path geometry in tennis.** `Player to win at least one set` is `UNION_LOW_THRESHOLD` with `N` = sets played. A total-games `Under` in a best-of-five is `INTERSECTION_CONSTRAINT` across every set. A games handicap near the median is `CENTRAL_BAND` and falls under `G26.1`.




### `P-291` reasoning-defect note and `L-068` reinforcement (added 2026-09-06(d))


`P-291`'s own preserved card text (Ben Shelton vs Denis Shapovalov) reasoned that the Shapovalov +5.5 games cushion "survives every Shapovalov win." **That general claim is false in best-of-five tennis, independent of what actually happened in this match.** Counterexample: a player can lose two sets 0-6, 0-6 and win the last three 7-6, 7-6, 7-6 — winning the match 3 sets to 2 with 21 games to the opponent's 30, a nine-game deficit that fails any cushion above +8.5, despite being the outright match winner. The settlement itself is correct (Shapovalov's actual 20 games + 5.5 = 25.5 > Shelton's 25), and this note does not change it — but the card's *reasoning* asserted a general mathematical guarantee that does not hold, and `L-068` (adopted after the same class of error in `P-287`) exists precisely to prevent this. **`L-068` is reinforced, not superseded:** a games-handicap row must be checked against the specific score line achieved, never against a general "the match winner always covers a modest cushion" assumption, because best-of-five's non-linear set structure makes that assumption false in general.


### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | Grand slam and tour matches settle from the tournament's official scoreboard or the tour's official match record; name the exact record at freeze. Retirement/walkover action follows `G36.1` under standard rules when operator terms are unsupplied. |
| `G14.2` coaching / bench / rotation record | Tennis has no bench; record the coach where publicly named and, more importantly, the **prior-round workload** (minutes/sets played, days of rest) as the rotation-capacity analogue. Pre-match court practice observations, physical strapping, and withdrawal/illness updates verified across accredited tennis journalists under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED` and satisfy `G14.2`. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen tennis match tree**, conditioned on surface/format-specific serve-return state, hold/break process, set-count mixture, scoreline coherence, retirement endpoint and any rating benchmark used only as a check. Historical second-highest set-count × median-games constructions are superseded as active gates. |
| `G21.1` exact target geometry | Map match winner, set count, total games and games handicap to exact settlement events from the same frozen set/game tree. Derive WIN/PUSH/LOSS and retirement/action branches from that tree; historical path-count/category labels have no mandatory ordinal effect. |
| `G26.1` no universal separation floor | Reference rates and `rank_gap` are descriptive only. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank from exact marginal likelihood plus robustness/evidence uncertainty. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Compute every illustrative set sequence into both players’ aggregate games, total, signed margin and all contract outcomes. Set count, winner and games handicap are jointly evaluated. A positive games cushion does not cover every match win; a long match need not have a close games margin.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-291/P-308/P-310 retain legal set scores, aggregate games and match winner as distinct quantities. A match winner can lose aggregate games; a cushion does not survive every possible win. P-310 joint efficient-three-set separation defeated cushion and Over; compare serve/return evidence with opponent quality. P-308 workload did not establish a causal fatigue sign. No retrospective probabilities or automatic upset-winner fade.


## 2026-09-09 settlement learning — P-338 (positive; the cross-sport model)


**`P-338` — Gauff def. Jovic 6–1, 6–4 (US Open Women's R16).** Frozen card: R1 `Gauff -4.5 games` (p0.54), R2 `Under 21.5 games` (p0.53), R3 `Over 21.5` (p0.47), R4 `Jovic +4.5` (p0.46); potential winner Gauff (78%). **Top two both won; potential winner correct; best card of its 9-card cohort.** Card mean Brier 0.2163.


*Why it worked, and what the rest of the framework is adopting from it:*


1. **One shared match tree with explicit branch weights** — 42% "Gauff dominant straight-set control", 20% "Gauff close straight", 12% "Gauff wide deciding", 4% "Gauff close deciding", 7% "Jovic straight", 15% "Jovic deciding" — from which winner mass (78%), handicap mass (54%) and total-games mass (53% Under) were all *derived*, not asserted. This is `§4`'s "explicit straight-set and three-set mixture weights" requirement executed properly.
2. **A representative Rank-#1 scoreline written out and checked** — "Gauff 6–3, 6–4 = 19 games" — verified to clear both `Gauff -4.5` and `Under 21.5` simultaneously (control 12). The realized 6–1, 6–4 was even more separated.
3. **The contrary H2H (Rome clay, Jovic led by a set and served for the match) was retained as a live kill path, not allowed to dominate** the hard-court forecast, because Gauff's current hard-court serve/return regime is materially better (control 1, control 3).


**Cross-sport export:** this method — enumerate the outcome families, put a mass on each, derive every row from the set, write and check a representative Rank-#1 outcome — is now `RULES_GENERAL.md` §16.5(a) / `G-L1`, required for soccer, baseball, basketball and every other sport's joint object. Tennis §4 and control 12 already satisfy it; no tennis change is needed there. Keep doing exactly this.


### The three other cross-sport controls, instantiated here


`G-L1` is already met. The other three requirements adopted from the `P-333`–`P-344` cohort do apply to tennis from the next card. All are **disclosure/retrieval requirements — no fitted weight, no ordinal bar** (`L-087`).


| Cross-sport control | Tennis instantiation |
|---|---|
| **`G-L2` — declared uncertainty model** | State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls. |
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a win-loss record, a season hold percentage or a "last 10" summary carry directional weight while the **match-by-match serve/return log** is available. `P-338` is the positive example and sets the standard: it printed *per-match* first-serve percentage, first- and second-serve points won, break points faced and return points won for each of the last three matches for both players, and it was those disaggregated lines — Jovic's 33.3% second-serve points won against Frech, the 17 breaks in the Eala match — that identified the actual mechanism. A player carried with only a ranking and a W-L record is `AGGREGATE_ONLY` and caps the dependent handicap/total rows. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-11 settlement learning — `P-350` (a Rank-#1 loss that was probably variance)


**`P-350` — Ben Shelton def. Carlos Alcaraz 6-7(5), 6-1, 6-3, 1-6, 7-6(7), US Open men's QF** ([`PREDICTION_LOG_COMBINED_3.md` §"2026-09-11"](PREDICTION_LOG_COMBINED_3.md)). Frozen card: R1 Alcaraz to win (0.76) **L**; R2 Over 3.5 sets (0.66) **W**; R3 Over 38.5 games (0.60) **W** (49); R4 Shelton +4.5 games (0.58) **W** (Shelton won 26–23 on games). Card mean Brier 0.2574.


**What went right.** The shared match tree did its job: 66% on four or more sets, the total-games Over and the Shelton cushion were all derived from it, and all three won. Control 12's coherence check held.


**Independent benchmark, not a validation of 76% (corrected 2026-09-12).** Tennis Abstract's Elo ratings dated **2026-08-31** (before the tournament): Alcaraz overall 2146.8 (#2), hard 2073.3 (#2); Shelton overall 1977.5 (#7), hard 1948.5 (#6). Converting the gap to a best-of-five probability — per-set probability `s` solving `s²(3 − 2s) = p₃` for the Elo best-of-three probability `p₃`, then `p₅ = s³(1 + 3(1 − s) + 6(1 − s)²)` — gives Alcaraz **≈71%** on hard-court Elo, **≈77%** on overall Elo, **≈74%** on a 50/50 blend. The card's 76% sits inside that range. The loss occurred in an upset branch, but one event and an Elo benchmark do not establish that the issued 24% upset mass was correctly sized; the match was decided by a fifth-set tiebreak (10–7). **The retrospective should not over-learn from it.**


**The one real blind spot.** Alcaraz was five months out with a wrist injury before the tournament. His 12–1 in sets through four rounds came against lower-ranked opposition, and neither Elo nor recent results see a layoff. That uncertainty belonged in the width of the set tree (`G-L2`).


### Structural control additions


13. **Print an independent rating benchmark beside the winner probability.** Retrieve Tennis Abstract's Elo (overall and surface-specific; ATP `tennisabstract.com/reports/atp_elo_ratings.html`, and its WTA equivalent) with a snapshot date **before** the event, convert the gap to a match-win probability for the correct format (formulae above), and print it beside the card's winner probability. A gap of more than ~10 percentage points needs a named current mechanism. The benchmark never sets the probability — it is a coherence check and a retrospective tool that separates variance from model error. Keyless, and a sports rating rather than a market input, so it is compatible with `SPORTS_ONLY / MARKET_BLIND`.


14. **A long layoff widens the tree.** A player returning from a multi-month absence carries wider set-level outcomes for the first events back, even when early rounds look clean against weaker opposition (`G-L2`). Origin `P-350`.


### Cross-sport controls instantiated here (2026-09-11)


| Control | Tennis instantiation |
|---|---|
| `G-L9` §16.5(e) | A 0.76 winner row must itemise its 0.24 across named paths: opponent serve dominance plus tiebreak coin-flips, current-event return pressure, physical/layoff risk, retirement (under the operator's terms). |
| `G-L10` section 16.5(f) | Derive joint match-winner, games and handicap probabilities from the same set-score model, or disclose joint uncertainty. A short underdog win can cover a cushion; a favourite can cover after losing a set. No universal coupling sign. |
| `G-L11` §16.5(g) | Hold/break percentages over a handful of matches are small-sample proportions; print service/return points and their standard error before a signed adjustment. |
| §16.8 | Completeness block; the Elo benchmark (control 13) is printed in item 3's row for the winner. |




## 2026-09-12 algorithm corrections and retrospective integration


Correct P-350's deciding breaker to 10-7; the match still contained 49 games. Verify event-specific deciding-set and retirement rules before grade. A match tiebreak score is not extra games. An underdog handicap can win in a short straight-set upset, so control G-L10's long-match dependence language is conditional. A dated Elo comparison is a benchmark under explicit assumptions; agreement cannot distinguish variance from probability error in one match. Bench is NOT_APPLICABLE; coach/fitness information must retain capture time and unknown fields.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## Recovered mini-log reinforcement - 2026-09-12


P-242's 28-game Zheng straight-set win defeated both Marozsan +2.5 and Over 38.5, despite the issued Zheng winner being correct: include decisive underdog/favourite separation in the set-and-games tree. P-263's 33-game Alcaraz win defeated Under 31.5 while covering -7.5: a lost opening set plus later rout is a distinct exposure branch. P-243 ended 13-13 aggregate games despite Jones winning the match. P-267's successful Under 31.5 and Noskova -4.5 support the represented short-match scenario, not calibration. No match-win or ordinary-three-set shortcut proves handicap coverage. The WTA P-243 extraction mixed state labels and showed incomplete service-game totals; validate each field separately. Evidence: audit_2026-09-12/recovered_historical_retrospectives.md.






## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Card:** P-375 (Rybakina d. Gauff 3–6 6–4 6–4) — Over 22.5 games and Rybakina −0.5 games both won; winner correct.


- **Positive model:** the six-branch deciding-set tree (Rybakina deciding-set win 28%) mapped directly onto the realised match (29 games). Keep it as the reference for every games-handicap card.
- **`G-L12` instantiation:** a games handicap takes its centre from the set-score tree; uncertainty about a returning or fatigued player widens the tree (control 14) rather than moving the handicap toward zero.


## 2026-09-16 — cross-sport controls instantiated here (`G-L13`, `G-L14`, `G-L15`, disruption facts)


No tennis card was settled this pass. Rules: `RULES_GENERAL.md` §16.11.
- **`G-L13`:** set scores and tiebreak scores come from the raw ATP/WTA/ITF record. P-350's corrected 10–7 breaker shows why a summary is not enough.
- **`G-L14`:** total-games and set rows name the settling record and the retirement rule at issue.
- **`G-L15`:** free total-games rows went 2 of 2 in `P-345`–`P-423`. A total-games Over paired with an underdog games handicap is reported as distinct targets with `P(A ∧ B)`.
- **Disruption facts:** record medical time-outs, retirements and rain suspensions with the set and game score at the time.


## 2026-09-17 — cross-sport controls instantiated here (`G-L17`–`G-L20`)


No tennis card in this import. **`G-L17`:** a games handicap and a total-games row usually share one match-shape state — print `P(¬R1 ∧ ¬R2)` and name it. **`G-L18`:** total games is a two-participant total; print each player's expected service-hold marginal before ranking it. **`G-L19`:** tennis has no draw, but the end-state family must carry retirement and walkover mass with the competition's settlement rule (`P-350` correction). **`G-L20`:** a current-regime head-to-head at the same surface and venue that already cleared the line gets explicit mass.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.12.


## 2026-09-17(b) — cross-sport controls instantiated here (`G-L21`–`G-L24`)


**G-L24 in TENNIS:** derive the exact signed-margin distribution under the competition endpoint, including draw, key-value and push masses. Pooled league bands are uncertain references, not mandatory matchup probabilities or rank prohibitions. Missing pooled bands do not invalidate a complete conditional joint distribution. **`G-L21`:** 'server dominance' carries a games Over, a set handicap and a total-games row together — print the joint failure mass. **`G-L22`:** the supplied tennis slate is usually a match-winner pair plus a total-games pair; report the preferred side of each. **`G-L23`:** break points converted, service-hold rate and **retirement/medical-timeout events with the set and game score** are the process and disruption fields — a retirement is an endpoint event and never evidence that the pre-match read failed.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.13; bands and base rates in [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md).


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound, social sources and the top-O/U review


`R-1` ([`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md)) applies: recent results revise an estimated **rate** through a named mechanism, never forecast a **deviation**. No rebound and no hangover adjustment is permitted in either direction. This sport's magnitudes are **`NOT_YET_DERIVED`** — the MLB figures are not transferable and must not be imported; derive them from this competition's own record before any recent-form weighting.


Source controls `S-1` (social identity: X and Reddit return no usable content; Bluesky sports handles failed identity verification 6/6) and `S-2` (press conferences are availability/role evidence, never a signed adjustment to a modelled rate) apply — `SOURCES.md` §"2026-09-19".


A loss **or push** on the card's highest-ranked over/under now triggers the same enhanced failure review as a Rank #1 loss (`METHOD.md` §7).


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** ATP/WTA/ITF/tournament official draws, results, rankings/order-of-play and withdrawal releases; verified weather for outdoor events. Fantasy/betting projections and picks are prohibited.


Serve/return point strength, surface, format, fatigue/rest, verified health/availability and conditions feed a point/game/set distribution. Match winner, set handicap and total games are derived from that process with retirement/void rules represented explicitly; the supplied line cannot influence serve/return estimates.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain surface/format-specific serve-return state, hold/break tree, set-count mixture, scoreline coherence, retirement endpoint and rating benchmark as a check only. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, blanket DISJOINT top-half bans, match-winner⇒games-handicap shortcuts, long-match⇒Over logic and tiny-H2H ownership rules. Build one coherent tennis set/game distribution before querying all targets.
<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-24 -->
<!-- AUDIT-2026-09-24F -->
## 2026-09-24 settlement learning — P-494 (WTA 500 Singapore), P-495 (WTA 125 Tolentino), P-496 (ITF M25 Falun), corrected 2026-09-24(f)

**Full record:** `PREDICTION_LOG_COMBINED_5.md` §"2026-09-24(f)". This is learning-only.

**What changed.** The peer version of this section (`cb95acd`) listed P-494's Rank 1 as "Andreeva −4.5"; the issued Rank 1 was Under 18.5. It printed P-496's score reversed as 6–2 3–6 7–6(4), which caused a **grading error**, and it called Falun "indoor carpet". The rows below are copied from the issued cards.

| Card | Event | Rank #1 (p) | Final (verified) | Top O/U (rank) | Note |
|---|---|---|---|---|---|
| P-494 | WTA 500 Singapore (LIVE-ISSUED) | Under 18.5 (0.550) **W** | Andreeva 6–2 6–2 (WTA LS008; ESPN 184095) | Under 18.5 (#1) **W** | Outside pregame metrics |
| P-495 | WTA 125 Tolentino, outdoor clay | Romero Gormaz −5.5 (0.591) **L** | Pieri 3–6 6–4 6–1 (ESPN 183890) | Under 19.5 (#2) **L** (26) | Rank-1 failure review: Part 5 §(f) E.1 |
| P-496 | ITF M25 Falun, **indoor hard** (ITF `M-ITF-SWE-2026-004`) | Over 22.5 (0.627) **W** (30) | **Marek 2–6 6–3 7–6(3); games 15–15** (ITF draw page; TennisExplorer 3331086) | Over 22.5 (#1) **W** | **R2 Vasa +0.5 = W and R3 Marek −0.5 = L** (corrected; previously graded the other way) |

### Rejected as a rule: `TENNIS-CHALLENGER-CLAY-HANDICAP-CAP` (L-20260924-F06)

Its thresholds (">78% hold", "<32% return points won", ">80% straight-set wins over the last 15 clay matches") are unsourced and rest on one match. Its companion claim that lower-tier clay holds fall below 60% is unsourced too.

What the P-495 card actually shows is already covered by existing rules:
- The margin mean (+5.09) sat below the 5.5 line; P(−5.5) = 0.591 came from the median and the skew. At a normalised edge of 0.09 this is a coin flip, and a #1 at a coin flip must say NEAR_TIE / LOW in the ordinal (G23.1; §16.5(d)).
- Romero Gormaz's 33-game R32 was treated as neutral while Pieri's qualifying run was discounted. G-L2 says mechanisms carry both signs, so workload is at least width on a heavy games handicap.

**Test.** `T-TEN-LOWTIER-HCP`: in WTA 125 and ITF matches, games-handicap rows of 5.5 or more whose normalised edge is below 0.15 win less often than their stated p. Test on the next 20 such rows by Brier and hit rate against stated p. **No cap and no rank effect meanwhile.**

### Controls added (integrity and retrieval)

**T-1. ITF settlement route.**
- The field owner is the ITF tournament "draws-and-results" page, fetched through `r.jina.ai` (for example `…/en/tournament/m25-falun/swe/2026/m-itf-swe-2026-004/draws-and-results/`). The page prints per-set games and tiebreak points.
- `…/tennis/api/TournamentApi/GetCalendar` and `GetEventFilters` also return JSON through the proxy (tournament key, surface, indoor/outdoor).
- `GetDrawsheet` and direct requests are blocked by Incapsula.
- Games-handicap rows are graded from set games, with a tiebreak set counted as 7–6.

**T-2. Surface.**
- Record the surface and the indoor/outdoor flag from the ITF calendar JSON, not from memory. Falun is **Hard, Indoor**.

<!-- RESEARCH-2026-09-25 -->
## 2026-09-25(b) — reference rates and games-handicap coherence (research pass)

**Status.** Reference rates plus two disclosure controls (`C-PROMOTION-RECEIPT`: `REFERENCE` and `PROMOTED_PROCESS`, disclosure only). Nothing here moves a probability or a rank. Source: `BASE_RATES_REGISTER.md` §7.4, from the ESPN tennis scoreboard, 1 Jan – 24 Sep 2026. It covers the Slams, tour events and WTA 125 events, but not ITF. Completed matches only; retirements and walkovers are excluded.

**TE-R1. The WTA totals gap is closed; print the reference.** Every tennis total row prints three things.
1. **P(deciding set)** beside the population reference: WTA best of 3 **0.340**; men best of 3 0.358; women's qualifying 0.313 v main draw 0.352.
   - Total games is a two-component mixture. The WTA means are **18.2 in straight sets and 28.6 with a deciding set**.
   - Lines from 19.5 to 25.5 fall in the trough between them. A total row there is mostly a P(deciding set) row, and the card should say so.
2. `REFERENCE_BASE_RATE`: the population P(total ≥ L + 0.5). WTA best of 3: ≥ 19 0.624, ≥ 20 0.542, ≥ 21 0.472, ≥ 22 0.425, ≥ 23 0.376. Men best of 3: ≥ 22 0.530, ≥ 23 0.453.
3. The reference width for `C-WIDTH-BENCHMARK`: WTA raw SD **5.79**; men best of 3 6.00. P-495 (5.68) and P-496 (5.92) were consistent with it.

ITF and UTR are `NOT_YET_DERIVED`: ESPN does not carry them.

**TE-R2. `C-HCP-COHERENCE` — games-handicap decomposition.**
1. **Hard identity (a probability law).** For a −k.5 row on player A, P(A −k.5) ≤ P(A wins). A card that violates it has an arithmetic error and fails closed.
2. **Disclosure.** The card prints P(A −k.5) = P(A wins in straight sets) · c_s + P(A wins in a deciding set) · c_d. Here c_s = P(margin ≥ k + 1 | straight-sets win) and c_d = P(margin ≥ k + 1 | deciding-set win), both from the card's own model. Beside c_s and c_d it prints the population references:

   | Handicap | WTA best of 3: c_s / c_d | Men best of 3: c_s / c_d |
   |---|---|---|
   | −4.5 (margin ≥ 5) | 0.818 / 0.286 | 0.654 / 0.186 |
   | −5.5 (margin ≥ 6) | **0.663 / 0.168** | 0.447 / 0.094 |
   | −6.5 (margin ≥ 7) | 0.479 / 0.081 | 0.270 / 0.032 |

3. **When c_s or c_d is above its reference,** the card names the hold and break evidence: both players' service-hold and return-game-won rates, over a dated window, with n. Without it the row is flagged `HCP_CONDITIONAL_ABOVE_REFERENCE`. The +k.5 row is the complement and carries the same disclosure.
4. **Evidence.** In P-495, P(win) 0.843 and P(−5.5) 0.591 imply P(margin ≥ 6 | win) = 0.70. That is above even the straight-sets reference of 0.663, and no hold/break evidence was printed. The row lost; Pieri won 3-6 6-4 6-1. This is the measurement lane for `T-TEN-LOWTIER-HCP`.
5. **Audit.** Field `HC` in `audit_card_controls.py`: advisory, blocking under `--strict`.

**TE-R3. Reference only, no rule.** Women's qualifying matches ran slightly shorter than main-draw matches (mean 21.28 v 21.95; P(deciding) 0.313 v 0.352). Print the population that matches the card.

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 2026-09-25(d) — track record from the full settled-row review

**Track record (`C-TRACK-RECORD`).** 16 decisions from 7 cards: won **50.0%** at a mean stated 0.601. Brier **0.281**, worse than a coin flip. Tennis cards are labelled **`NO_DEMONSTRATED_SKILL`**: the evidence grade is capped at LOW and the departure ledger is required.

- **Games-handicap cushions (+k.5): 1/4** at 0.58. `C-PLUS-CUSHION` applies alongside `C-HCP-COHERENCE` (TE-R2).
- **Practical consequence.** The Elo benchmark (TE-P5) and the population rates (TE-R1) are the starting point. A winner probability far from the Elo implied probability, or a total far from the P(deciding set) reference, needs the serve/return numerators that justify it. Otherwise the card stays near the benchmark.

Source: `research/settled_rows_2026-09-25/README.md`. The figures are hindsight on the framework's own cards, descriptive, and use card-cluster intervals. None is a coefficient (`L-087`). Controls: `RULES_GENERAL.md` §"2026-09-25(d)".


<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — Rank 1 and Rank 2 in tennis

Controls: `RULES_GENERAL.md` §"2026-09-25(e)".

**Record at Rank 1/2 (probability era): 6 W / 8 L.** The losses were two total-games Overs at Rank 1 and three +k.5 games cushions. The sport stays `NO_DEMONSTRATED_SKILL`.

- **The RM-1 cushion term covers +k.5 games handicaps.**
  - Stated at 0.58, such a row has a q of about 0.30, and the favourite's −k.5 becomes the decision side. That side is capped at SUPPORTED and must still pass `C-HCP-COHERENCE`: P(−k.5) ≤ P(win), with the c_s / c_d decomposition.
  - Held out, RM-1 raised tennis Rank 2 from 3/7 to 5/7 (small n).
- **No TB-1 lane.**
  - The anchor stays the dated Elo benchmark (TE-P5, blocking) plus the §7.4 population (WTA P(deciding set) 0.340; total games bimodal).
  - A total-games Over at Rank 1 needs the card's P(deciding set) printed against 0.340, because the Over is mostly a third-set bet.
- **Unchanged:** sources (the WTA match page, Tennis Majors and the Elo snapshot).
