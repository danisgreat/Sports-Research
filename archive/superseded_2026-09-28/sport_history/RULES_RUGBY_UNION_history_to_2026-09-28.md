# -- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 --> — dated history to 2026-09-28

**Archived 2026-09-28 (md-only restructure).** These are the dated sections that followed the competition-rules section of `RULES_RUGBY_UNION.md`, moved verbatim. They are the evidence record. The live rules are §0 of `RULES_RUGBY_UNION.md`, and nothing here reinstates a rule that §0 or `CURRENT_RULES.md` §I withdraws.

## September 5 cross-sport process inheritance


L-068–L-071 in RULES_GENERAL §12 apply to this SFA through phase score budgets, actual role/minute exposure, cards and kicking allocation. Validate arithmetic, propagate failed evidence caps, make both sides’ material winning states evaluable and keep source identity/field definitions explicit. No new completed game in this sport was available in the current cohort; no sport-specific empirical improvement or parameter change is claimed.


## September 6 settlement learning — cross-sport gates instantiated


No rugby-union or sevens card was settled in the `P-294`–`P-305` cohort. This file remains qualitative-only; the v3.7 gates are instantiated here as disclosures, consistent with that status.


**Sport-native tail example.** A rugby-union total is exposed to two compounding tails that a points-only budget hides: **the bonus-point chase**, where a side on three tries plays materially more expansively for the fourth, and **the penalty-count tail**, where a high-penalty referee appointment converts territory into three-point increments at a much higher rate than open play. Hold each side's second-highest L10 try count `T` at its own L10 conversion rate `c` and convert to points as **separate scoring components**: `points = 5×T + 2×(T×c) + 3×penalty_goals + 3×drop_goals + 7×penalty_tries` (using the competition's actual try/conversion/penalty-goal/drop-goal/penalty-try values from the reference section — some competitions vary these). **Correction, 2026-09-06(d):** the earlier wording here mirrored the NRL shorthand ("try count × conversion rate") and likewise omitted the try points themselves and the separate goal-scoring terms; the explicit component sum above is the actual required arithmetic. Add the penalty-goal term separately, derived from the fixture's own recent penalty counts, and print the implied total. Where the appointed referee is known and their penalty count is publicly recorded, that is a named exposure pathway under `G15`; where it is not, record `REFEREE_NOT_ANNOUNCED` and do not infer one.


**Sevens** carries a much shorter interval and a much higher per-minute scoring rate, so the same arithmetic is run per seven-minute half rather than per 40. A sevens `Under` is an unusually tight `INTERSECTION_CONSTRAINT`. **Correction, 2026-09-06(d):** the earlier claim that it "should very rarely be Rank #1" was an undisclosed ordinal rule derived from a general geometric observation, not a tested one — one actual sevens result in this log (`P-132`, Vannes 17–10 Lyon, `Under 35.5` **WIN**) is a direct counterexample to treating tight-constraint Unders as structurally unrankable. The path-geometry field remains disclosure only, per `RULES_GENERAL.md` §15; it creates no automatic demotion.


**Bench capacity is unusually load-bearing in this sport.** A rugby-union bench is eight players including a full front row, and the "finishers" model means a large share of late scoring comes from replacements as a matter of design rather than accident. `G14.2` is therefore not optional here: a card with `BENCH_NOT_RETRIEVED` cannot honestly rank a margin or full-game total row first.




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | Test and club rugby settle from the union's or competition's official match record; name the exact record at freeze. Sevens tournaments settle from the World Rugby event record. |
| `G14.2` coaching / bench / rotation record | Record the head coach, the full eight-player bench with its front-row cover, the substitution/HIA provisions from §11, and any confirmed rotation for a congested block. Official union/club 48h team sheets or warm-up scratch notices verified across accredited rugby journalists under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED`, satisfy `G14.2`, and do not block Rank #1. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen rugby-union/sevens joint score distribution**, conditioning on format-specific possession/territory, set piece, discipline/cards, replacements, goal-kicking, and extra-time/tiebreak rules. Sparse evidence widens uncertainty; historical order-statistic stress sums are superseded as active gates. |
| `G21.1` exact target geometry | Map every supplied target to its exact settlement event and derive WIN/PUSH/LOSS from the same frozen sport-native PMF/CDF or coherent branch mixture. Historical path-count/category labels have no mandatory ordinal effect. |
| `G26.1` no universal separation floor | Reference rates and `rank_gap` are descriptive only. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank from exact marginal likelihood plus robustness/evidence uncertainty. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Apply the shared native-score arithmetic, final-role/exposure gate, both-side score/separation budgets and source-field checks to possession, territory, kicking and discipline. This audit supplies no new rugby-union-specific coefficient evidence.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-09 — cross-sport controls instantiated here (`G-L1`, `G-L2`, `G-L7`, `G-L8`)


No rugby-union card was issued in the `P-333`–`P-344` cohort. The four cross-sport requirements adopted from it (`RULES_GENERAL.md` §§16.5(a)–(d), full evidence in `PREDICTION_LOG_COMBINED_3.md` §"2026-09-09") apply to this sport from the next card. All four are **disclosure/retrieval requirements — no fitted weight, no ordinal bar** (`L-087`), and none authorises a numerical model here: rugby union remains qualitative-only.


| Cross-sport control | Rugby-union instantiation |
|---|---|
| **`G-L1` §16.5(a)** — enumerate outcome-state families with explicit mass | Enumerate the **margin families** (favourite by 22+ / 13–21 / 8–12 / 1–7 / draw / underdog win — with the bonus-point thresholds named where the competition uses them) and the **total families** in points, each with an explicit mass summing to 1. Scoring is quantised in 5s, 7s and 3s, so state families as **try-count × conversion × penalty-count** combinations rather than a smooth corridor. Every current-evidence §8.5 kill path — a **yellow/red card**, a **penalty-try**, a shift to kicking for territory, a rolling-maul scoring pattern — appears as a weighted branch. Print a representative Rank-#1 final score as a try/penalty breakdown and check it against the handicap, the total and any bonus-point-dependent row. |
| **`G-L2` — declared uncertainty model** | State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls. |
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a season points-per-game figure or a "last N" summary carry directional weight while the **round-by-round log** is available. Print the per-match record for the decision-relevant window — points for/against, tries, penalties attempted/converted, and the **goal-kicker's per-match success rate** rather than a season percentage. For a returning player, print the **bench-minutes progression** across recent matchday squads, the analogue of the rehab pitch-count ladder that decided `P-335`. Quantify **the primary goal-kicker and every top-three try-scorer on both sides**; a bare name in a "leaders include…" phrase is `AGGREGATE_ONLY` and caps the dependent margin/total rows. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


## 2026-09-11 — cross-sport controls instantiated here (`G-L9`, `G-L10`, `G-L11`, §16.8)


No rugby-union card in the `P-345`–`P-371` import. From the next card ([`RULES_GENERAL.md` §§16.5(e)–(g), §16.8](RULES_GENERAL.md)):


| Control | Rugby-union instantiation |
|---|---|
| `G-L9` §16.5(e) | Itemise the complement across the named paths — a yellow-card swing, goal-kicking accuracy, a bonus-point chase, set-piece dominance in the wet. |
| `G-L10` §16.5(f) | A late bonus-point chase can raise the total while changing the margin in either direction; print the coupling of any handicap + total pair. |
| `G-L11` §16.5(g) | Line-out success, goal-kicking percentage and tries-per-match over a few rounds are small samples; print their standard error before a signed adjustment. |
| §16.8 | Matchday 23s are named before kick-off; `NOT_RETRIEVED` after naming is a `RETRIEVAL_MISS`. |




## 2026-09-12 algorithm corrections and retrospective integration


Apply section 16.9 to possession/territory, tries, conversion/penalty attempts, cards and replacements. A low-scoring close match and a low-scoring shutout have different handicap outcomes. Record both XVs, full replacements, kickers and coaches with publication times. Conversion proportions and points per possession require different uncertainty treatment. No new union result was settled in this pass; no union-specific weight or claimed lift is adopted.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


No rugby-union card in this import. **`G-L12` instantiation:** print the favourite's 8+ and 15+ margin families beside any handicap, with the late-try branch (bonus-point chasing and yellow cards) as mass; sparse team lists (control 11) widen the margin distribution rather than centring it on a close game.


## 2026-09-16 — cross-sport controls instantiated here (`G-L13`, `G-L14`, `G-L15`, disruption facts)


No rugby-union card was settled this pass. Rules: `RULES_GENERAL.md` §16.11.
- **`G-L13`:** XVs, replacements and kickers come from the raw union or competition team announcement, with its publication time.
- **`G-L14`:** try-count and half rows name their settling record at issue.
- **`G-L15`:** label total rows forced-pair or free.
- **Disruption facts:** record yellow cards, red cards (including 20-minute reds where the competition uses them) and HIA replacements with the minute and score.


## 2026-09-17 — cross-sport controls instantiated here (`G-L17`–`G-L20`)


No rugby-union card in this import. **`G-L17`:** a handicap and a total resting on one territory/tempo thesis need their joint failure mass printed. **`G-L18`:** print each side's points marginal before a match total. **`G-L19`:** draws are possible in league fixtures; knockout fixtures add extra time and, where the regulations allow, kicking competitions — enumerate them before a winner label. **`G-L20`:** a current-regime comparable that cleared the line gets explicit mass.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.12.


## 2026-09-17(b) — cross-sport controls instantiated here (`G-L21`–`G-L24`)


**G-L24 in RUGBY UNION:** derive the exact signed-margin distribution under the competition endpoint, including draw, key-value and push masses. Pooled league bands are uncertain references, not mandatory matchup probabilities or rank prohibitions. Missing pooled bands do not invalidate a complete conditional joint distribution. **`G-L21`:** 'forward-pack dominance, territory, low-error game' is one thesis that commonly carries a handicap, an Under and a team total. **`G-L22`:** handicap and total are forced pairs; derive push mass at whole-number lines. **`G-L23`:** possession, territory, set-piece completion and **cards with minute and score** are the process and disruption fields — a red card in union changes the remaining-time scoring rate more sharply than in most codes.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.13; bands and base rates in [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md).


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound, social sources and the top-O/U review


`R-1` ([`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md)) applies: recent results revise an estimated **rate** through a named mechanism, never forecast a **deviation**. No rebound and no hangover adjustment is permitted in either direction. This sport's magnitudes are **`NOT_YET_DERIVED`** — the MLB figures are not transferable and must not be imported; derive them from this competition's own record before any recent-form weighting.


Source controls `S-1` (social identity: X and Reddit return no usable content; Bluesky sports handles failed identity verification 6/6) and `S-2` (press conferences are availability/role evidence, never a signed adjustment to a modelled rate) apply — `SOURCES.md` §"2026-09-19".


A loss **or push** on the card's highest-ranked over/under now triggers the same enhanced failure review as a Rank #1 loss (`METHOD.md` §7).


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** World Rugby, union/competition official match centres/team sheets/rules, club releases and government weather. Betting/fantasy material is prohibited.


Build score/margin distributions from team strength, lineup/bench/kicker availability, set-piece/territory/discipline process, venue/weather, rest/travel and format-specific end states. Sevens and XVs remain separate populations. The supplied line is a final query, never a predictor.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain format-specific possession/territory, set-piece, discipline/cards, replacements, goal-kicking and extra-time/tiebreak rules, with sparse-evidence uncertainty widening. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, imported rugby-league rates, and one-result response rules. Build one coherent rugby-union/sevens joint outcome distribution before querying targets.

<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — Rank 1 and Rank 2 in rugby union

Controls: `RULES_GENERAL.md` §"2026-09-25(e)".

- **No union population or TB-1 lane has been derived yet.** Cards print `TEAM_BASELINE_P: NOT_COVERED` and `REFERENCE_BASE_RATE: NOT_YET_DERIVED`. The ESPN rugby union scoreboards are the candidate lane for the next research pass.
- **RM-1's cushion term applies to union +k.5 rows.** The rugby rows in the record (P-127, P-128, P-132, P-363) include large cushions that won. So a large cushion (k ≥ 10) stated at 0.60–0.65 is still scored by RM-1; when the card writes the reconciliation line, it names the population margin band (`C-PLUS-CUSHION`).
- **The ranking rules are general:** rank by RM-1 q, print `TOP2_QUALITY`, and settle from the feed.
