# Framework retrospective and improvement plan, 2026-10-09

**Status:** `IMPLEMENTED 2026-10-09` (see §5.8). Sections 0–5.7 and 6–7 are the review as written, including its acceptance tests and the wording "not implemented"; they are kept unchanged so the findings can be re-read against what was found at the time. §5.8 records, for every recommendation ID, what was implemented, what could not be verified offline, and what only prospective cards can show. The only changes made with the review itself were the user-directed final settlement (`research/verification/final_settlement_2026-10-09/`) and the three October 9 rules (T2, R1, P4).

**Update 2026-10-09 (Markdown-only).** After this review was implemented, the framework was reduced to Markdown, CSV and text (commits `a64675cf7` to `a93352c30`). The findings, the failure-class baseline and the acceptance tests below stand. Every recommendation that §5.8 marks as implemented in code, tools, CI or the runtime (fitted engines, calibration, stacking, candidate pricing, validators, the importer, scoreboard generation, source adapters, evidence snapshots, cross-card experiments) is now **`SUSPENDED_MD_ONLY`**: the code is gone and the rule it carried now lives in a document ([SELECTION_RULES.md](SELECTION_RULES.md), [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md), [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md), [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md), the prompts). The three rules (T2, R1, P4), the Rank-1 gate, the one-distribution card and the regime and contract-definition fields are kept as documented rules. Paths and commands named in this document refer to the tree at commit `37203fc2b`.

**Authority at review:** MDS-2026.10.09-v8.1 / CR-2026.10.09-R1 / SCV-2026.10.09-v4.

---

## 0. Evidence base and method

Every finding below was reproduced in this session from the repository at commit `bc4a1e847` plus the October 9 settlement. Nothing is taken on trust from earlier reports.

| Evidence | How it was obtained |
|---|---|
| Final-settlement cohort: 72 records, 71 forecast cards | `research/verification/final_settlement_2026-10-09/settlement_table.json` and `build/build_settlement.py` |
| Full rank history: 2,004 rows, 522 card IDs, 630 rows with a stated p | `GAME_PREDICTION_RANK_LOG.csv` (literal grades, `LEARNING_ONLY`) |
| Runtime code review | All of `runtime/src` (about 3,900 lines) read line by line; defects confirmed by executing the code |
| Test and verifier baseline | `pytest research/tests research/operations runtime/tests`, then `log_card verify`, `control_freeze --verify`, `verify_all_logs`, `verify_rollover`, `verify_carryover_review` |
| Tennis distribution check | `final_settlement_2026-10-09/build/tennis_overdispersion_check.py`, which reproduces the P-551 and P-555 card numbers exactly |
| Source and data inventory | `research/sources_registry.json`, `DATA_SOURCE_REGISTER.md`, `H0_DATASET_CARD.md`, `Previous Sports Results/` (22,071 CSVs), `research/data/processed/` |
| Trained-model evidence | `research/runs/epl_2025-26_holdout.json` and `research/runs/nbl_2025-26_holdout.json` |

Historical figures are literal-grade diagnostics. They describe what the log says happened; they are not certified prospective skill.

---

## 1. Executive summary

### 1.1 What the results say

1. **Rank 1 carries real but modest signal; Rank 2 carries almost none.** Across 522 historical cards, Rank 1 won **61.9%** (304/491; 95% Wilson CI 57.5–66.1%). Rank 2 won **54.3%** (251/462; CI 49.8–58.8%), statistically indistinguishable from ranks 3–4 (54.3%, 491/905). Under the new top-two rule, Rank 2 is the weakest link: half of every card's counted result rests on a slot that has not beaten the informational alternates.
2. **Stated probabilities have weak skill and are over-extreme.** On the 630 rows with a stated p: Brier 0.2332 against climatology 0.2456, a **Brier skill score of 0.050**, and a calibration slope of **0.865** (probabilities about 13% too extreme). The 350 rows stated at 0.40–0.60 won 51.7% (181/350, rows-weighted): coin flips.
3. **The final-settlement cohort repeats the pattern.** 79 counted wins from 134 live top-two rows (59.0%). Rank 1 was 40 W / 28 L / 3 VOID (58.8% of live). Both picks were lost on 15 of 68 live cards.
4. **The 28 Rank-1 failures cluster into six fixable classes, not randomness** (§3.3). These are first-half-goal over-selection, the +1.5 run-line ceiling, basketball totals without a pace model, tennis i.i.d. under-dispersion and handicap over-reach, ranking by q instead of p, and dependent top-two pairs. At least 15 of the 28 were knowable at cutoff from information printed on the card itself.

### 1.2 What the code and data say

5. **The numerical ML runtime does not import.** `runtime/src/common/evaluation.py:132` uses `Optional` without importing it, so every runtime test module (11 of them) fails at collection. CI on `windows-latest` runs `runtime/tests`, so the CI regression job cannot be green.
6. **Machine-learning components contain correctness defects.** The isotonic calibrator is wrong: it returns 0.382 where PAVA gives 0.333, with deviations up to 0.46 over random fits. The NHL, baseball and NRL engines silently replace a score of 0 with a default ("falsy zero"); a toy fit gave a hockey league average of 2.2 against a true 0.75. Several optimisers fall back silently to flat parameters on failure.
7. **The distributions used on cards are not produced by the engines.** All 19 recent cards (P-538–P-556) label their probabilities `UNCALIBRATED_ANALYST_SCENARIO` or `UNCALIBRATED_QUALITATIVE`, and P-550 states `EVENT_SPECIFIC_REGISTERED_NHL_MODEL_OUTPUT_USED: NO`. Card probabilities come from analyst-chosen Poisson/normal/i.i.d.-point parameters that are typed in, not fitted. Only EPL and NBL have trained, held-out models (EPL log loss 1.033 against a 1.085 population baseline; NBL 0.606 against 0.696). Most cards are for other leagues.
8. **Source collection is mostly manual and unregistered.** The source registry holds 15 sources, all with independence `UNKNOWN`. Automated fetchers exist only for MLB, ESPN and NBL finals. Most forecast leagues (KBO, NPB, B.LEAGUE, KBL, ATP, NHL, China League One, Ligue 3 and others) have no registered adapter, so evidence is gathered ad hoc per card, and settlement fields (corners, half-time, serve stats) are often unobtainable later.
9. **A large historical archive is unused by the models.** `Previous Sports Results/` holds 22,071 CSVs across eight sports. Schemas are inconsistent: KBO and NHL rows are rich, while B.LEAGUE, ATP and Premier League rows hold only score strings and narrative. Nothing joins the archive into an H0 training table, base rates or the engines.
10. **Governance overhead is high and partly self-defeating.** There are 13 superseded or current control manifests, about 0.84 MB in total, with a 14th added today. Snapshot-bound verifiers fail on every legitimate state change: `verify_rollover` requires `event_count == 65`. Line-ending-sensitive hashes fail on a non-Windows checkout. Errors still pass through, for example settlement-refresh R1 blocks for P-539–P-545 copy P-538's ranking text verbatim, and the rank index encodes blank-contract corner rows as `P` (push).

### 1.3 Ten highest-value recommendations

| # | ID | Recommendation | Why first |
|---:|---|---|---|
| 1 | ENG-01 | Fix the `Optional` import and make CI green; add an import smoke test | Nothing in the ML runtime can run or be tested until this is fixed |
| 2 | ML-01 | Replace the isotonic calibrator with a correct, tested PAVA | A calibrator that mis-calibrates is worse than none |
| 3 | DST-01 | Fix falsy-zero score coercion in the NHL, baseball and NRL engines | Shutouts corrupt every fitted mean |
| 4 | PRD-01 | Enforce rank order = p_card order in a card validator; reject q-ordering | Three Rank-1 failures came from q-ordering alone |
| 5 | PRD-02 | Rank-2 selection by diversification: pick the best row whose joint failure with Rank 1 is lowest | Rank 2 currently adds no information over ranks 3–4 |
| 6 | DST-04 | Tennis: add a match-level serve random effect calibrated to the archive's deciding-set rate | Reproduced: it flips Over 22.5 from 0.61 to 0.47 |
| 7 | DST-02 | Resolve OT/extra-innings mass in the hockey, basketball and baseball engines | Moneylines and full-game totals are currently incoherent |
| 8 | SRC-01 | Build registered adapters for every league actually forecast, with target fields retained at settlement time | Removes most of the C/E/X evidence grades in the settlement |
| 9 | SRC-05 / ML-03 | Turn `Previous Sports Results` into a standard-schema H0 table and fit per-league engines on it | Converts hand-typed λ into fitted, testable parameters |
| 10 | EVL-01 | A rolling prospective scoreboard for counted top-two wins, Rank-1/2 rates, calibration and failure classes | Turns Rule T2/R1 into a measurable feedback loop |

---

## 2. Scope of the October 9 changes (implemented, by instruction)

| Change | Where |
|---|---|
| 72 pending records settled: 1 consolidated block (50 records: P-126–P-522 plus P-538–P-549, whose rollover verifier pins twelve addenda) plus 22 ledger addenda (P-523–P-537, P-550–P-556); no ID consumed, next ID P-557 | `prediction logs/PREDICTION_LOG_COMBINED_7.md`; `research/canonical_ledger.jsonl` (+44 records); `research/issued_research/` |
| 28 deep Rank-1 retrospections | Same addenda; source `final_settlement_2026-10-09/build/rank1_retrospectives.py` |
| Rules T2, R1 and P4 | CURRENT_RULES.md, CARD_AND_LOG_TEMPLATES.md, SCORING_AND_VALIDATION.md (SCV-2026.10.09-v4), PROMPTS.md |
| New control revision and freeze | METHOD.md → CR-2026.10.09-R1, `CONTROL_MANIFEST_2026-10-09-1.md` |

Temporary IDs: every `TMP-`/`LOCAL-` alias in the repository already maps to a canonical P-ID, so none needed a new ID. `P-557` remains next.

---

## 3. Performance retrospective

### 3.1 Final-settlement cohort under the top-two rule (71 forecast cards)

| Measure | Value |
|---|---|
| Counted wins / live top-two rows | **79 / 134 (59.0%)** |
| Rank 1 | 40 W / 28 L / 3 VOID (58.8% of live) |
| Rank 2 | 39 W / 27 L / 5 VOID (59.1% of live) |
| Card class | 27 all live top-two won · 26 split · 15 all lost · 3 void |
| Hit@2 | 53 / 68 |
| Winner calls | 37 correct / 11 incorrect / 23 not recoverable |
| Evidence grades over 313 settled rows | A 168 · B 107 · OP 16 · C 13 · X 7 · E 2 |

By sport, Rank 1: ice hockey 5/6, soccer 20/29 live, baseball 8/14, basketball 5/11, tennis 2/5 live, and AFLW, cricket and NRL 0/1 each. Basketball and tennis Rank-1 rows were at or below a coin flip in this cohort.

### 3.2 Full history (literal grades, 522 cards)

| Slot | W–L | Win rate | 95% CI |
|---|---|---:|---|
| Rank 1 | 304–187 | 61.9% | 57.5–66.1% |
| Rank 2 | 251–211 | 54.3% | 49.8–58.8% |
| Ranks 3–4 | 491–414 | 54.3% | 51.0–57.5% |

Card classes on live top-two rows: 181 all won, 213 split, 102 all lost.

Calibration of stated p (n = 630):

| Stated p bin | n | Mean p | Win rate |
|---|---:|---:|---:|
| 0.3–0.4 | 62 | 0.362 | 0.403 |
| 0.4–0.5 | 158 | 0.444 | 0.506 |
| 0.5–0.6 | 192 | 0.552 | 0.526 |
| 0.6–0.7 | 118 | 0.639 | 0.619 |
| 0.7–0.8 | 62 | 0.739 | 0.758 |
| 0.8–0.9 | 29 | 0.845 | 0.828 |

The 0.7–0.9 bins are well calibrated. The mid-range (0.4–0.6) has no resolution. **Practical reading:** Rank 1 should come from rows the distribution places at 0.65 or above, with a demonstrated separation from Rank 2. Rows in the 0.5–0.6 band behave like coin flips and should not be picks.

### 3.3 Rank-1 failure classes (28 failures in the final settlement)

| Class | Records | Knowable at cutoff? | Mechanism |
|---|---|---|---|
| First-half-goal over-selection | P-148, P-234, P-250, P-342, P-377 | Yes (4/5 named the 0-0 half as a kill path) | A 0.61–0.68 proposition placed at Rank 1 with no half-split model. In the final-settlement cohort, 1H Over 0.5 at Rank 1 went 9 W / 5 L, exactly what p≈0.65 predicts. This is a selection error, not a calibration error. |
| Baseball +1.5 cushion ceiling | P-274, P-524, P-544, P-547 | Yes | An underdog's +1.5 ≈ P(win) + P(lose by 1) is capped near 0.60–0.63. The stated p sat at that ceiling, so there was no edge. |
| Basketball totals without a pace model | P-527, P-548, P-553 | Partly | Hand-centred totals; an unfitted analyst shift (P-553) or an unmodelled rule-change regime (P-548). |
| Tennis score-tree under-dispersion or dependence | P-541, P-551, P-555 | Yes | I.i.d. points put deciding-set mass at 0.48–0.50 against the 0.358 reference. Overdispersed Over 22.5 is 0.46–0.47, not 0.59–0.61. Top two shared the long-match driver. |
| Rank by q instead of p | P-519, P-521, P-522 | Yes (printed on the card) | P-521's Rank 1 had p = 0.408 while its complement had p = 0.592. |
| Dependent top two sharing one driver | P-176, P-492, P-541, P-549, P-555 | Yes | One thesis (starter, favourite dominance, away λ) decided both picks. |
| Other | P-200 (−2.5 hockey tail), P-217 (phase incoherence and reduced overs), P-369 (corners by one, no provider), P-430 (85% team-to-score), P-520 (weak slate), P-531 (late, unquantified), P-534 (finals compression) | Mostly yes | See each addendum. |

### 3.4 What worked (reviewed under the same standard as failures)

- **Hockey sides and totals** (5/6 at Rank 1). Low-variance regulation-plus-OT structure with clear goalie information.
- **Soccer team totals and double chance for clearly stronger sides** (P-233, P-235, P-407, P-409, P-410, P-419). High-mass rows with direct mechanisms: a favourite's team total over 0.5 or 1.5, and 1X/X2.
- **Well-separated basketball spreads** (P-535, P-536). Large-gap mismatches ranked on margin, not total.
- **High-p rows are honest.** Stated 0.7–0.9 probabilities historically matched realised rates.
- **Process controls held.** Market blindness, immutable originals, append-only logs and named kill paths. Many failures were *predicted in the card's own failure routes*; what was missing was weighting, not foresight.

---

## 4. Findings by component

Each finding has an ID that the recommendation register (§5) references. Severity: **Critical** (results are wrong or the system cannot run), **High** (materially degrades forecasts or evaluation), **Medium**, **Low**.

### 4.1 Source collection and data (SRC)

| ID | Severity | Finding | Evidence |
|---|---|---|---|
| F-SRC-1 | High | The registry covers 15 sources; most forecast leagues have no registered adapter. | `research/sources_registry.json`: NBL, MLB, ESPN EPL/NBL, openfootball, PL official, AFLW, two college sites, NFL gamebooks, Perth Wildcats, NBL news, football-data, fixture-download, plus an excluded fantasy entry. No KBO, NPB, KBL, B.LEAGUE, ATP/WTA, NHL, Chinese, French or Korean soccer adapters. |
| F-SRC-2 | High | Settlement target fields are not captured at the time they are available. Corners, half-time scores and period splits were lost to later 403s and redirects. | 7 rows settled VOID for no data; 13 at best-available C; 2 estimated E. P-126, P-250, P-341 and P-418 had no provider at all. |
| F-SRC-3 | Medium | All 15 sources have `independence_status: UNKNOWN` and no lineage audit was ever run, so the documented three-collector quorum can never be met. | Registry fields; CURRENT_RULES §A.4 |
| F-SRC-4 | Medium | `DATA_SOURCE_REGISTER.md` describes `runtime/data/raw/<sport>/<provider>/<date>/` snapshots and R bridges (fitzRoy, nrlR). That directory does not exist and no ingestion job writes it. | `ls runtime/data` returns "No such file or directory" |
| F-SRC-5 | High | The archive (22,071 CSVs) is heterogeneous. KBO and NHL rows have IDs, scores, OT/SO flags and start times; B.LEAGUE, ATP and Premier League rows have only a score string, "Notable Players" and a one-line narrative. There are no half-time, corner or serve-stat fields. | Sampled `2025_games.csv` headers per sport |
| F-SRC-6 | Medium | Card-time evidence (lineups, goalie confirmations, injury lists) is gathered by browsing and cited by URL. Bodies are not retained, so point-in-time availability cannot be proven afterwards. | Card section I/J literals: "actual warm-up … not certified", "source page may change" |
| F-SRC-7 | Low | A fantasy source sits in the registry (as `EXCLUDED_FANTASY`). It is correctly excluded, but its presence in the main registry invites error. | Registry entry `fantasy_premierleague` |
| F-SRC-8 | Medium | Egress is blocked for some reference sources from cloud sessions (rsssf.org returned `EGRESS_BLOCKED` here), and Sofascore/AiScore return 403. Card research depends on whichever sources the current session can reach. | This session's WebFetch; earlier reviews |

### 4.2 Prediction workflow and ranking (PRD)

| ID | Severity | Finding | Evidence |
|---|---|---|---|
| F-PRD-1 | High | Rank order is not validated against probability. q-ordered cards inverted p (P-519, P-521, P-522). | P518_P522_RECONCILIATION.md rows |
| F-PRD-2 | High | Rank 2 has no information over ranks 3–4 historically (54.3% against 54.3%). It is usually a correlated restatement of Rank 1, or a near-coin-flip complement. | §3.2; P-176, P-492, P-541, P-549, P-555 |
| F-PRD-3 | High | Supplied contracts set the candidate set. Several Rank-1 rows were the "least bad" supplied row rather than the best proposition the distribution supported (P-534 Roosters −4.5 against Knights +12.5; P-200 −2.5 against +2.5). Rule P4 now addresses this procedurally. | Final-settlement counterfactuals |
| F-PRD-4 | High | No numeric gate stops coin-flip rows reaching Rank 1 (P-234 at 0.50; P-520 at 0.577 with a 0.52 Rank 2). | Cards |
| F-PRD-5 | Medium | Unfitted analyst adjustments decide ranks (P-553's −2.75-point judgment shift made the Under the top row). | P-553 card section F |
| F-PRD-6 | Medium | Late and live research keeps stale ranks after material news (P-274 starter change; P-531 starter change). There is no re-forecast trigger. | Cards and reviews |
| F-PRD-7 | Medium | Regime flags are missing: finals compression (P-534), league rule changes (P-548 KBL foreign-player rule) and early-season small samples (P-176) are mentioned in prose but never shift the distribution. | Cards |
| F-PRD-8 | Low | Card bodies are very long (3–10 KB of caveat boilerplate). The decision-relevant content (distribution, four candidates, failure mass) is hard to audit. | Part 7 card bodies |

### 4.3 Distribution modelling (DST)

| ID | Severity | Finding | Evidence |
|---|---|---|---|
| F-DST-1 | Critical | Falsy-zero coercion: `float(m.get("home_goals") or m.get("home_score", 3.0))` turns a 0 into the fallback. On a toy set the NHL league average was fitted as 2.2 (true 0.75) and MLB as 3.75 (true 1.5). | `nhl/engine.py:36`, `baseball/engine.py:37`, `nrl/engine.py:38` |
| F-DST-2 | High | Endpoint incoherence. The NHL grid keeps regulation draws (16.9% mass in a 3.0/2.8 example) with no OT/SO resolution. Basketball and baseball grids keep ties, about 3.5% in the basketball example. So "full-game" moneylines and spreads computed from the grid are wrong. | `nhl/engine.py`; `basketball/engine.py`; `baseball/engine.py:129` |
| F-DST-3 | High | Basketball support is fixed at 60–160 points per team. For low-scoring leagues (B.LEAGUE, KBL, NBL1, women's) truncation biases means: inputs of 72/68 gave grid means of 75.1/72.4. | `basketball/engine.py:100–101` |
| F-DST-4 | High | Tennis uses an i.i.d. point model with no match-level variance. Reproduced: P(3 sets) = 0.499 against the 0.358 reference; P(Over 22.5) moves from 0.609 to 0.474 once a calibrated form shock is added. | `tennis/engine.py`; `tennis_overdispersion_check.py` |
| F-DST-5 | Medium | The hockey "empty-net" transfer applies a fixed 22% to every 1–2-goal lead regardless of game state or time, and shifts mass without re-fitting λ. | `nhl/engine.py:93–111` |
| F-DST-6 | Medium | Team strength is `0.8 × (raw mean/league mean) + 0.2`, a fixed shrinkage independent of games played and not opponent-adjusted (basketball, baseball, NHL, AFL). | `*/engine.py` fit methods |
| F-DST-7 | Medium | Silent defaults: an unknown soccer team gets xG 1.55/1.20 (`soccer/engine.py:63–64`); Dixon-Coles' unknown team gets 1.45/1.20 (`dixon_coles.py:154`); basketball defaults to an NBA mean of 112 for any league. | Code |
| F-DST-8 | Medium | Baseball team runs are independent negative binomials (no covariance), with a fixed starter innings default (5.2/5.5) and no bottom-of-ninth truncation for a leading home team. | `baseball/engine.py` |
| F-DST-9 | Medium | Cricket chase success puts all mass exactly at target, though a final boundary can overshoot by up to 5. Home is assumed to bat first, and reduced-overs/DLS branches are absent (P-217). | `cricket/engine.py` |
| F-DST-10 | Low | NFL drives are i.i.d. with only 0/2/3/7 outcomes (no 6 or 8), so key-number mass at 6, 10 and 14 is approximated. | `nfl/engine.py:66–96` |
| F-DST-11 | Medium | There is no corner/cards count engine, although corners appear in about a quarter of soccer cards. No negative-binomial count model with score-state adjustment is wired in. | The runtime has `NegativeBinomialCountRegressor` but no soccer corner engine |
| F-DST-12 | Low | The quantile reconstructor returns exactly 1−τ₀ below the lowest quantile (no tail extrapolation). | `distributional.py:161` |

### 4.4 Machine learning and calibration (ML)

| ID | Severity | Finding | Evidence |
|---|---|---|---|
| F-ML-1 | Critical | `IsotonicCalibrator` PAVA is incorrect: pooled weights are double-counted and the routine rescans from 0. It outputs 0.382 for y=[1,0,0] where PAVA gives 0.333, with a maximum deviation of 0.46 over 200 random fits. | `calibration.py:48–80` |
| F-ML-2 | High | Silent optimiser fallbacks: Dixon-Coles sets all attacks and defences to 0 on failure (`dixon_coles.py:135`); Bradley-Terry, NB regression, Platt and temperature scaling keep defaults. A failed fit looks like a valid flat model. | Code |
| F-ML-3 | High | Dixon-Coles likelihood loops over matches in Python inside L-BFGS-B with numerical gradients over 2T+2 parameters, roughly O(T·N) Python operations per gradient. It is impractical for multi-season league fits. No analytic gradient, vectorisation or decay tuning (ξ fixed at 0.002). | `dixon_coles.py` |
| F-ML-4 | High | No engine is trained on archive data, and no recent card uses engine output (all 19 cards P-538–P-556 are uncalibrated analyst scenarios or qualitative). The model register lists 12 model families (CatBoost, NGBoost, hierarchical Bayes, BigQuery) that are specification only. | `runtime/config/models/models.json`; card literals |
| F-ML-5 | Medium | The BigQuery layer is a SQL string generator with a hard-coded project `sports-analytics-prod`. It centres ARIMA_PLUS/AI.FORECAST time-series forecasting, the wrong model class for match-outcome distributions. | `bigquery_ml.py:15` |
| F-ML-6 | Medium | Artifacts are saved with `pickle`, which is unsafe to load and version-fragile. There are no model cards or reproducible training receipts for runtime engines. | `base.py:102–107` |
| F-ML-7 | Medium | Elo has no margin-of-victory term, season regression or rating uncertainty, and K is fixed. | `ratings.py` |
| F-ML-8 | Low | Stacking is a linear pool only, with no logit/beta pooling and no per-family weights. | `stacking.py` |

### 4.5 Evaluation and scoring (EVL)

| ID | Severity | Finding | Evidence |
|---|---|---|---|
| F-EVL-1 | High | The promotion gate uses fixed point thresholds (ΔBrier ≤ −0.010, slope 0.90–1.10, |intercept| ≤ 0.05) at n ≥ 50, with no uncertainty. At n = 50 the slope's standard error is far wider than ±0.10, so the gate is mostly noise. | `evaluation.py:264, 302` |
| F-EVL-2 | High | The prospective harness bootstraps i.i.d. rows, contradicting the scoring standard's week-block bootstrap; it understates uncertainty for same-day correlated events. | `prospective.py:101` against SCORING_AND_VALIDATION.md |
| F-EVL-3 | Medium | Before October 9 there was no metric aligned with the user's objective (counted top-two wins); NDCG@2 and Wins@2 were descriptive only. SCV-v4 now defines them, but there is no rolling dashboard. | SCORING_AND_VALIDATION.md |
| F-EVL-4 | Medium | There is no rolling calibration monitor by sport and family, though the history shows a 0.865 slope and an uninformative 0.5–0.6 band. | §3.2 |
| F-EVL-5 | Medium | The 15 registered experiments are per-card hypotheses, none run. There is no cross-card experiment on the recurring failure classes. | `research/experiment_measures.json` |

### 4.6 Settlement, logging and governance (GOV)

| ID | Severity | Finding | Evidence |
|---|---|---|---|
| F-GOV-1 | High | Snapshot-coupled verifiers break on legitimate progress (`verify_rollover` requires `event_count == 65` and exactly 12 ledger addenda for P-538–P-549; `verify_carryover_review` requires the selected register to equal its own snapshot). The October 9 settlement therefore could not switch `current_settlement_register.json`, and had to record P-538–P-549 in the consolidated block rather than as ledger addenda, to avoid code changes. | `verify_rollover.py:52–55`; `verify_carryover_review.py:54` |
| F-GOV-2 | High | Line-ending-sensitive custody: Parts 1–5 and the rank CSV are hashed as Windows CRLF bytes, so `verify_all_logs`, `verify_rollover`, `verify_carryover_review` and `control_freeze` fail on a Linux checkout although the content is identical. | Confirmed: the CRLF transform of the LF checkout reproduces every recorded hash |
| F-GOV-3 | Medium | Copy-paste defects slipped through review: the Part 6 settlement-refresh "R1" blocks for P-539–P-545 repeat P-538's ranking text, and P-519's original settlement asserted a fabricated 50–22 final. | Part 6 lines 12262–12584; P518_P522_RECONCILIATION.md |
| F-GOV-4 | Medium | The rank index encodes blank-contract rows as `P` (push). Five corner rows (P-407 R1, P-409 R2, P-410 R5, P-419 R5, P-430 R5) were therefore pushes in the index though actually WIN/LOSS. | `GAME_PREDICTION_RANK_LOG.csv` against the original settlement tables |
| F-GOV-5 | Medium | Governance volume: 13 control manifests before today (about 0.84 MB), 15 dated verification folders and long status registers. Current state is hard to read: README line 44 still says Part 6 is the sole destination and the next ID is P-538. | Root listing; README.md |
| F-GOV-6 | Low | Clutter: seven zero-byte Python files at the root (`apply_preseason_all.py`, `audit_preseason_results.py`, `build_and_apply_preseason.py`, `fetch_all_preseason.py`, `test_afl_matches.py`, `test_aflw_matches.py`, `test_parser.py`) plus stray `subagent_parser.js` and `validate_austria_bundesliga.py`. | `ls -la` |
| F-GOV-7 | Medium | Settlement-ready contract definitions are not captured at issue (operator retirement, OT and listed-pitcher rules), so 16 rows needed the OP default and 8 tennis rows were voided by convention. | Settlement evidence counts |

### 4.7 Engineering and CI (ENG)

| ID | Severity | Finding | Evidence |
|---|---|---|---|
| F-ENG-1 | Critical | Runtime import failure (`Optional`), so 11 runtime test modules error at collection and the CI job cannot pass. | `evaluation.py:132`; pytest output |
| F-ENG-2 | Medium | The frozen model-build check pins Python 3.14 exactly, so on 3.13 two pipeline tests fail. This is reasonable for custody, but there is no documented container image. | `research/src/model_custody.py:21` |
| F-ENG-3 | Medium | No type checking or linting in CI (the `Optional` error would have been caught by any static check). | `.github/workflows/research.yml` |

---

## 5. Recommendation register (as written; implementation status in §5.8)

Columns: **ID** · **Priority** (P0 = correctness/blocking, P1 = high value, P2 = valuable, P3 = hygiene) · **Addresses** · **Recommendation** · **Acceptance test** · **Effort** (S < 1 day, M 1–3 days, L > 3 days).

### 5.1 Engineering and correctness (do first)

| ID | P | Addresses | Recommendation | Acceptance test | Effort |
|---|---|---|---|---|---|
| ENG-01 | P0 | F-ENG-1 | Add `Optional` to the `typing` import in `runtime/src/common/evaluation.py`. Add `tests/test_import_smoke.py`, which imports every runtime module. | `pytest runtime/tests` collects all 11 modules; CI regression job green | S |
| ENG-02 | P0 | F-ENG-3 | Add `ruff` (pyflakes rules) and `mypy --ignore-missing-imports` on `runtime/src` and `research/src` to CI. | CI fails on an undefined name | S |
| ENG-03 | P1 | F-ENG-2 | Publish a pinned dev container or `uv` lock for Python 3.14.6, matching the frozen build receipt. | Fresh clone runs the full suite with no version skips | S |
| DST-01 | P0 | F-DST-1 | Replace `a or b` score coercion with explicit `None` checks in the NHL, baseball and NRL `fit()`. Raise on missing scores; never default to a league-typical number. | Unit test: fitting on all-shutout games gives a league mean of 0.75 exactly | S |
| ML-01 | P0 | F-ML-1 | Replace `IsotonicCalibrator` with a block-PAVA (stack-based, weighted) or `sklearn.isotonic.IsotonicRegression`; handle ties in x. | Property test: matches reference PAVA to 1e-12 on 1,000 random fits; monotone output | S |
| ML-02 | P0 | F-ML-2 | Every optimiser failure raises `FitFailed` (or returns a result object with `converged=False`). Callers must refuse to predict from an unconverged model. | Test: a forced failure cannot produce a ScoreDistribution | S |
| DST-02 | P0 | F-DST-2 | Add an explicit endpoint layer: `regulation` returns the grid with draws; `full_game` resolves draw mass through a sport-specific OT/SO/extra-innings model (hockey: OT goal-rate race plus shootout ≈ 0.5±skill, +1 goal; basketball: 5-minute OT convolution, repeatable; MLB: extra-innings runner model; KBO/NPB: tie allowed after 12). | `p_home_win + p_away_win == 1` for full-game in NHL, NBA and MLB; regulation contracts unchanged | M |
| DST-03 | P1 | F-DST-3 | Make basketball support data-driven (μ ± 6σ, floor 0), with league-specific priors (NBA, WNBA, EuroLeague, NBL, B.LEAGUE, KBL, CBA) from the archive. | Grid mean equals input mean within 0.1 point for μ ∈ [55, 125] | S |

### 5.2 Source collection (SRC)

| ID | P | Addresses | Recommendation | Acceptance test | Effort |
|---|---|---|---|---|---|
| SRC-01 | P1 | F-SRC-1 | Build registered adapters, in order of card frequency, for the leagues actually forecast: KBO (koreabaseball.com scoreboard/box), NPB (npb.jp), NHL (api-web.nhle.com), ATP/WTA (tournament results plus Sackmann-format stats), B.LEAGUE (bleague.jp game keys), KBL (kbl.or.kr), NBL (already partial), EuroLeague/ACB/BBL/GBL (official feeds), and soccer via one structured provider with corners and half-time fields. Each adapter: allowed URL prefixes, parser ID, endpoint taxonomy (regulation/full/HT/corners), body retention, hash. | Each adapter has a recorded-body unit test and a probe; `fetch_source` returns a hashed receipt | L |
| SRC-02 | P1 | F-SRC-2, F-GOV-7 | Settlement-field capture at issue: when a card includes a corners, half-time, period or player row, register the exact provider field and schedule an automatic post-game capture within 24 hours (before routes rot). | Zero "no provider" VOIDs on new cards over a 4-week window | M |
| SRC-03 | P1 | F-SRC-6 | Pregame evidence snapshots: retain the bodies (or a hashed text extract) of lineup, goalie and injury pages used on a card, with retrieval time. | Every new card's evidence list resolves to retained hashes | M |
| SRC-04 | P2 | F-SRC-3 | Run actual lineage audits for the top 10 sources (who collects, who syndicates). Mark `INDEPENDENT`, `SHARED_FEED` or `UNKNOWN` with evidence, so the quorum rule becomes satisfiable. | ≥ 3 independent terminal collectors registered for MLB, NBL and EPL | M |
| SRC-05 | P1 | F-SRC-5 | Standardise the archive to one event schema per sport: event_id, date and UTC start, home/away, scores by period (half/quarter/inning/set), endpoint flags (OT/SO/ET/pens/retirement), venue, stage, source receipt. Back-fill from the richer sources first (NHL and KBO already conform). | `research.src.archive build` emits per-sport standard tables; coverage report by season | L |
| SRC-06 | P2 | F-SRC-4 | Either implement the documented `runtime/data/raw` snapshot layout and R bridges (fitzRoy, nrlR), or delete those sections from DATA_SOURCE_REGISTER.md. | Register matches the filesystem | S–M |
| SRC-07 | P2 | F-SRC-8 | Keep a reachability matrix per environment (local Windows against cloud), with fallback sources per field. Cards record which fallback was used. | Matrix in SOURCES.md, refreshed weekly | S |
| SRC-08 | P3 | F-SRC-7 | Move excluded sources (fantasy, odds) to a separate `excluded_sources.json`, so the main registry holds only admissible sources. | Registry lint passes | S |

### 5.3 Prediction workflow and ranking (PRD)

| ID | P | Addresses | Recommendation | Acceptance test | Effort |
|---|---|---|---|---|---|
| PRD-01 | P0 | F-PRD-1 | Card validator (run inside `log_card commit`): ranks must be non-increasing in p_card. Every p must come from one declared distribution object; p and q columns cannot coexist on new cards. | Historical replay flags P-519, P-521 and P-522; new card with an inversion is rejected | S |
| PRD-02 | P1 | F-PRD-2 | Rank-2 selection rule: from the remaining candidates with p ≥ 0.58, choose the one that minimises P(Rank 1 and Rank 2 both lose), computed from the same distribution. Break ties by p. Print the joint failure mass. | On a replay of the final-settlement cohort, simulated joint failure ≤ 0.30 on ≥ 80% of cards | M |
| PRD-03 | P1 | F-PRD-4 | Rank-1 gates: p_card ≥ 0.62 and ≥ 0.04 above the best non-complementary alternative; otherwise label `RANK1_UNSTABLE` and score it in a separate cohort. Calibrate the thresholds on history (the 0.6–0.7 bin is the first with resolution). | Prospective Rank-1 win rate in gated cards exceeds ungated by ≥ 5 pts over 8+ weeks | S |
| PRD-04 | P1 | F-PRD-3 | Implement Rule P4 as tooling: a `candidates` helper that, given a distribution, enumerates the standard line ladder for winner/double chance/handicap/total/team total/period, prices every row and proposes the top four (supplied rows included and tagged), excluding p > 0.90. | Card JSON includes the ladder table and the four chosen rows with tags | M |
| PRD-05 | P1 | F-PRD-5 | Analyst adjustments become named parameters with a prior size and sign, logged in the card; any rank that flips because of an adjustment larger than 0.25 SD is flagged `ADJUSTMENT_DEPENDENT`. | Flag present on replay of P-553 | S |
| PRD-06 | P2 | F-PRD-6 | Re-forecast trigger: a confirmed starter, goalie or QB change, or a lineup change above a threshold after cutoff, produces a dated re-forecast addendum. The original stays immutable. | Addendum created in simulation for P-274/P-531-type changes | M |
| PRD-07 | P2 | F-PRD-7 | Regime flags with quantitative effects estimated from the archive: finals/knockout compression (NRL, AFL, NBA playoffs), early-season shrinkage (games < 5), rule-change regimes (KBL 2026-27, NRL six-again), cup rotation. | Each flag has a fitted multiplier and CI, stored in BASE_RATES_REGISTER | M |
| PRD-08 | P2 | F-PRD-8 | A short-form card: a ≤ 1-page decision block (distribution summary, ladder, four candidates, joint failure, kill paths), with full evidence in an appendix. | Median decision-block length ≤ 2.5 KB | S |
| PRD-09 | P2 | §3.3 | Family-specific selection rules learned from history: 1H Over 0.5 not Rank 1 unless p ≥ 0.72 from a half-split model; baseball +1.5 not Rank 1 unless p ≥ 0.65; tennis games rows only from the overdispersed tree; corners only with a provider and an NB model. | Rules encoded in the validator; replay shows the failure classes removed | S |

### 5.4 Distribution modelling (DST)

| ID | P | Addresses | Recommendation | Acceptance test | Effort |
|---|---|---|---|---|---|
| DST-04 | P1 | F-DST-4 | Tennis: add a match-level random effect on serve-point probabilities (form shock δ ~ N(0, σ²), applied +δ/−δ). Fit σ by maximum likelihood on archive set and game counts per surface and tour. Target: deciding-set rate and game-margin distribution match the ATP/WTA archive. Keep the exact enumeration (already implemented in `tennis_overdispersion_check.py`). | Deciding-set rate within ±2 pts of archive by surface; PIT histogram of total games is flat | M |
| DST-05 | P1 | F-DST-6 | Replace the ad hoc `0.8·ratio + 0.2` strengths with opponent-adjusted ratings: Poisson/NB GLM or hierarchical attack–defence, with shrinkage ∝ n/(n+k) and k fitted per league. | Out-of-sample log loss beats current engine on 2 seasons per sport | M |
| DST-06 | P1 | F-DST-11 | Soccer corners/cards engine: NB2 regression per team for corners for and against, with a score-state adjustment (trailing teams win more corners) and a match-level covariance, priced to totals, team totals and handicaps. | Calibration of P(corners > L) within ±3 pts per decile on an archive season | M |
| DST-07 | P1 | §3.3 | Soccer half-time model: separate first- and second-half λ (≈ 0.45/0.55 split, fitted per league) with Dixon-Coles low-score correction per half. Feeds 1H rows and the "0-0 at half" kill path. | P(HT 0-0) calibrated per league within ±3 pts | M |
| DST-08 | P1 | F-DST-8 | Baseball: a bivariate run model with a shared game-environment factor (park, weather, umpire) for covariance, a starter-leash distribution (not a fixed 5.2 IP), and home-team bottom-of-ninth truncation. One-run share then emerges by environment (fixes the P-547 issue). | Predicted one-run-game share by expected-total decile matches the KBO/MLB archive ±2 pts | M |
| DST-09 | P1 | F-DST-3, §3.3 | Basketball: possessions × points-per-possession bivariate model with team pace/efficiency ratings, Student-t margin, league-specific totals priors, early-season shrinkage, and an explicit regime prior after rule changes. | Totals PIT flat per league; Under/Over calibration ±3 pts | M |
| DST-10 | P2 | F-DST-5 | Hockey: replace the fixed empty-net transfer with a late-game state model (goalie-pull hazard by deficit and time; EN goal rate), fitted on NHL play-by-play. Add regulation-plus-OT/SO full-game resolution (DST-02). | Two-goal-margin share and EN share match archive ±2 pts | M |
| DST-11 | P2 | F-DST-9 | Cricket: ball/over resource simulation with wickets, phase-specific run rates, toss/bat-first branch, reduced-overs/DLS branch, and boundary overshoot at chase completion. Powerplay and death phase rows must come from the same simulation. | Phase/total joint calibration on Cricsheet T20 archive | L |
| DST-12 | P2 | §3.3 (P-534) | NRL/AFL: score-event models (tries/goals; scoring shots/conversion) with finals compression from the archive, plus period splits for half-time and quarter rows. | Grand-final margin dispersion reproduced | M |
| DST-13 | P2 | F-DST-7 | Remove silent defaults. An unknown team triggers an explicit promoted/new-team prior with logged uncertainty, or refuses to predict. | No literal 1.55/1.20/112 defaults remain in engines | S |
| DST-14 | P3 | F-DST-10 | NFL: drive model with 6/8 outcomes and score-state pace; key-number mass checked against archive. | Margin key-number frequencies ±1 pt | M |
| DST-15 | P3 | F-DST-12 | Quantile reconstructor: parametric tail extrapolation (exponential/GPD) beyond the outer quantiles. | Tail probabilities monotone and continuous | S |

### 5.5 Machine learning and calibration (ML)

| ID | P | Addresses | Recommendation | Acceptance test | Effort |
|---|---|---|---|---|---|
| ML-03 | P1 | F-ML-4 | Build H0 per sport from the standardised archive (SRC-05): point-in-time features (rolling ratings, rest, travel, schedule density, home/away, stage, regime flags) with `known_at` derived from event end times. Fit every runtime engine on H0 with rolling-origin splits; publish model cards. | Each engine has a fitted build receipt and holdout metrics against the population baseline | L |
| ML-04 | P1 | F-ML-3 | Vectorise Dixon-Coles (numpy arrays of team indices, analytic gradients) and tune ξ by rolling-origin log loss. Add xG-informed variants where xG exists. | Fit of one EPL season ≤ 2 s; ξ chosen by CV | M |
| ML-05 | P1 | F-EVL-4, §3.2 | Post-hoc calibration layer per sport × family (Platt or beta calibration, or the fixed isotonic) fitted on rolling CAL folds, applied to engine probabilities before ranking. Recalibrate monthly; monitor slope and intercept. | Calibration slope in [0.9, 1.1] with CI on rolling 8-week windows | M |
| ML-06 | P2 | F-ML-4 | First ML challenger as registered: gradient boosting (CatBoost/LightGBM) on H0 features to predict distribution parameters (λ, μ, σ) rather than binary outcomes, so contracts stay coherent. Then NGBoost for heteroscedastic width. | Beats the engine baseline on log loss and CRPS in ≥ 2 sports under the fixed-cohort evaluator | L |
| ML-07 | P2 | F-ML-7 | Ratings: Elo with margin-of-victory multiplier, season carry-over regression and Glicko-style uncertainty; surface-specific tennis Elo (already referenced in RULES_TENNIS) wired into the tennis engine prior. | Rating-only baseline log loss improves on archive | M |
| ML-08 | P2 | F-ML-6 | Replace pickle with JSON/NPZ parameter files plus a model card (data hash, code hash, metrics, date range). | Load does not execute code; receipts verify | S |
| ML-09 | P2 | F-ML-5 | Re-scope BigQuery: either remove it from the active register, or use it only as a feature warehouse (point-in-time joins) and BOOSTED_TREE challengers on H0, never ARIMA for match outcomes. Make project/dataset configuration-driven. | Register states the reduced scope; no hard-coded project ID | S |
| ML-10 | P3 | F-ML-8 | Stacking: add logit (geometric) pooling and per-family weights; fit on CAL only. | Stacked model beats best single model on TEST or is not used | M |

### 5.6 Evaluation and scoring (EVL)

| ID | P | Addresses | Recommendation | Acceptance test | Effort |
|---|---|---|---|---|---|
| EVL-01 | P1 | F-EVL-3 | A rolling top-two scoreboard (SCV-v4): counted wins over live top-two, Rank-1/2 rates with Wilson CIs, card classes, failure-class tallies, and evidence-grade counts, by sport, family and month. Generated from settlement tables; published on each settlement. | Report regenerates deterministically from the ledger | M |
| EVL-02 | P1 | F-EVL-1 | Promotion gate with uncertainty: require the week-block-bootstrap 95% CI of ΔBrier and Δlog-loss to sit below 0 (not a fixed −0.010), and calibration slope CI to contain 1. Report power for the observed n. | Gate decision unchanged by resampling seed; documented power | S |
| EVL-03 | P1 | F-EVL-2 | Switch `ProspectiveEvaluationHarness` to week-block (or match-day) bootstrap as the scoring standard requires. | Test: block structure honoured; CI wider than i.i.d. on correlated synthetic data | S |
| EVL-04 | P2 | F-EVL-5 | Replace per-card experiments with cross-card experiments on the six failure classes (e.g. "half-split model vs current for 1H rows"), each with a frozen cohort and acceptance criterion. | Six registered experiments with power plans | M |
| EVL-05 | P2 | §3.2 | Separate "informational" cohort scoring for ranks 3–4 (calibration only) and a `RANK1_UNSTABLE` cohort (PRD-03), so the counted cohort measures only the picks. | Scoreboard shows the cohorts separately | S |

### 5.7 Settlement, logging and governance (GOV)

| ID | P | Addresses | Recommendation | Acceptance test | Effort |
|---|---|---|---|---|---|
| GOV-01 | P1 | F-GOV-1 | Refactor dated verifiers to verify their **own pinned snapshot by hash**, not to require it to be the current selection. Then point `research/current_settlement_register.json` at `final_settlement_2026-10-09/register.json`. | All verifiers pass after a legitimate settlement update | S–M |
| GOV-02 | P1 | F-GOV-2 | Hash text artefacts after newline normalisation everywhere (as `control_freeze` already does for `.md`), or add `-text` attributes to all custody-hashed files so bytes are platform-identical. | Verifiers pass on Linux and Windows checkouts of the same commit | S |
| GOV-03 | P1 | F-GOV-3, F-GOV-4 | Settlement lint: each addendum's R1/original-ranking block must match the card's own rank table (string-equality on propositions). The rank index must never encode a blank contract as `P`; blank means `UNKNOWN_CONTRACT`. | Replay flags P-539–P-545 R1 blocks and the five `P` corner rows | S |
| GOV-04 | P2 | F-GOV-7 | Contract-definition capture at issue: endpoint (regulation/full/incl. OT), retirement/walkover rule, listed-pitcher rule and abandonment/DLS rule for every row, from the framework default when no operator is named. Settlement then never needs OP inference. | New cards carry all four fields | S |
| GOV-05 | P2 | F-GOV-5 | Consolidate governance: one current-state page (generated), archive superseded manifests into `archive/controls/`, regenerate README's queue paragraph from the ledger, and cap status-register history at a pointer. | README/CURRENT_RULES contain no stale next-ID or destination statements | M |
| GOV-06 | P3 | F-GOV-6 | Remove zero-byte root scripts and move one-off scripts (`validate_austria_bundesliga.py`, `subagent_parser.js`) into `research/src/` or `archive/`. | Root contains only docs, configs and the canonical CSV | S |
| GOV-07 | P2 | F-SRC-2 | A settlement SLA: every card is settled within 72 h of its final with the evidence hierarchy (A/B/C/E/OP/X), so carryover cannot accumulate to 72 records again. | Open carryover ≤ 5 at any time | S |

### 5.8 Implementation status (2026-10-09)

Status values: **IMPLEMENTED** (mechanism built and tested; the stated acceptance test was run and passes, or is a property of the code); **PARTLY** (part done, the remainder named); **PENDING DATA** (mechanism built and tested, but the acceptance test needs prospective cards or elapsed time); **NOT MET OFFLINE** (needs web access, restricted local files or data the build environment did not have). No row is marked implemented on the strength of a test that was not run. All paths are in this repository.

| ID | Status | What exists, and what it did not show |
|---|---|---|
| ENG-01 | IMPLEMENTED | `runtime/tests/test_import_smoke.py` imports every runtime module, so a broken import fails collection. |
| ENG-02 | IMPLEMENTED | CI and `dev_check` run ruff (undefined names on `research/src`; the full rule set on `runtime` and `research/operations`) and mypy. |
| ENG-03 | IMPLEMENTED | `.python-version` (3.14.6), `requirements-lint.txt`, `dev_check` mirroring CI step for step (a parity test fails on drift); a wrong interpreter exits 2 instead of skipping tests. |
| DST-01 | IMPLEMENTED | A zero score is a score. Fits reject missing scores; tests in every engine module. |
| ML-01 | IMPLEMENTED | PAVA calibrator with a reference implementation test and monotone output; temperature, Platt and beta calibrators. |
| ML-02 | IMPLEMENTED | `FitFailed`, `InsufficientData`, `MissingInputs`, `NotFitted`; no silent default in Dixon–Coles, distributional regression, stacking, ratings or strengths (`test_fit_failures.py`). |
| DST-02 | IMPLEMENTED | `common/endpoints.py`: NHL, NBA and MLB full-game contracts resolve OT/SO/extras inside the grid, so P(home) + P(away) = 1; regulation contracts unchanged. |
| DST-03 | IMPLEMENTED | Grid mean equals the input mean across league scoring levels; league profiles are built from the archive (`runtime/config/leagues/`), with no NBA default for another league. |
| SRC-01 | PARTLY | `research/src/adapters.py` and `research/sources_registry_adapters.json`. Recorded-body tests: KBO, NPB and the MLB live feed (plus parsers for the already-registered MLB schedule and NBL routes). Synthetic-fixture only: NHL, ESPN soccer, Sackmann ATP, because no live body could be fetched (no internet in the build environment; the cloud container's proxy refuses most sports hosts). Planned, no adapter: B.League, KBL, EuroLeague, ACB, BBL/GBL. `adapters.fetch` returns a hashed receipt (tested with an injected opener). The acceptance test is met for 3 of the 11 new adapters. |
| SRC-02 | PENDING DATA | `Settlement fields` and `Capture due` are validated on every v3 card; `capture_schedule` lists captures due and overdue; `evidence_snapshot store --kind capture` retains the page. "Zero no-provider VOIDs over 4 weeks" needs four weeks of cards. |
| SRC-03 | PENDING DATA | `evidence_snapshot` stores hashed bodies or extracts and prints the `sha256@time` token; `verify-card` resolves every token on a card to a stored receipt retrieved before the research time. "Every new card resolves" needs new cards. |
| SRC-04 | NOT MET OFFLINE | `lineage_audit` (schema, validator, quorum function requiring distinct terminal collectors including an official one) and `registry_lint` exist. **No audit was performed**: reading publishers' own documentation needs web access. Every collector stays UNKNOWN and no league has an independent quorum. |
| SRC-05 | IMPLEMENTED | `research.src.archive_std` (`coverage`, `build`): one standard event schema over the raw archive with a recorded reason for every unmapped row. The module name differs from the register's `archive build`; the pinned `archive.py` is unchanged. |
| SRC-06 | IMPLEMENTED | `runtime/src/common/snapshots.py` writes hashed snapshots in the documented layout; the R bridges register their output; `DATA_SOURCE_REGISTER.md` was regenerated to match the filesystem. |
| SRC-07 | PARTLY | `reachability` probes each registered source per environment and renders the matrix with same-league, different-lineage fallbacks into `SOURCES.md`. Probed from the cloud container (1 of 14 sources reachable: openfootball; 2 manual-only). The local Windows machine has not been probed; the weekly refresh is an operator action. |
| SRC-08 | IMPLEMENTED | `fantasy_premierleague` moved to `research/excluded_sources.json`; `registry_lint` fails if an excluded source returns to the executable registry. |
| PRD-01 | IMPLEMENTED | `card_validator` rejects rank inversions, `q` ranking and p-and-q columns; the historical replay flags exactly P-519, P-521 and P-522 in the P-518–P-522 range. |
| PRD-02 | PARTLY | Rank 2 is the row minimising P(both lose) from the joint grid (`common/selection.py`), with a conservative bound across outcome spaces. Replaying the final-settlement cohort was impossible: those cards do not retain their distributions. The ≤ 0.30 criterion is tested on synthetic distributions and left to the prospective experiments. |
| PRD-03 | PENDING DATA | Gate (p ≥ 62%, margin ≥ 4 points) in `selection_rules.json`, validated on every card and routed to its own scoreboard cohort. The values stay provisional until experiment SEL-1 (8 or more weeks) completes. |
| PRD-04 | IMPLEMENTED | `candidates` returns the ladder, the four chosen rows with tags, joint failure, the gate and the distribution object (id with a content hash). |
| PRD-05 | IMPLEMENTED | Adjustments table, `ADJUSTMENT_DEPENDENT` label and the unadjusted top two, checked in both directions. P-553 was not replayed: the old card has no adjustments table. |
| PRD-06 | IMPLEMENTED | `reforecast check` and `addendum`; tested on goalie, starter and quarterback changes of the P-274 and P-531 kind. |
| PRD-07 | IMPLEMENTED | `regimes build`: 15 league/flag multipliers with season-block bootstrap intervals in `runtime/config/regimes.json` and `BASE_RATES_REGISTER.md`; the recommended multiplier is 1.0 where the interval contains 1. CUP_ROTATION and the KBL foreign-player rule are NOT_ESTIMABLE (reasons recorded). |
| PRD-08 | IMPLEMENTED | Decision block capped at 4096 bytes (target 2560) with the appendix below; the golden examples measure 1.7–1.8 KB. A median over real cards is not yet measurable. |
| PRD-09 | IMPLEMENTED | Family rules from `selection_rules.json` are enforced by the validator. |
| DST-04 | PARTLY | Exact point-to-match tree with serve order and a match-level form effect, tested (the P-551/P-555 deciding-set inflation is removed). The archive has results only, so the form σ and the by-surface deciding-set check could not be fitted: the tennis engine is NOT_FITTED. |
| DST-05 | IMPLEMENTED | Opponent-adjusted, shrunk strengths with a cross-validated ridge, recovered on synthetic data. The register's "beats the current engine on 2 seasons per sport" comparison was not run; rolling-origin receipts (ML-03) compare engines with the population baseline instead. |
| DST-06 | PARTLY | Negative-binomial corners with score-state effects, validated against the register's EPL mean and on synthetic provider data. The archive has no corners provider, so the per-decile calibration on an archive season was not run. |
| DST-07 | IMPLEMENTED | Half-split Dixon–Coles validated against the register's EPL first-half rates. |
| DST-08 | PARTLY | Starter-leash mixture, matchup shock, conditional bottom of the ninth; one-run share falls with the expected total. League-average shape matches the archive within 3 points (observed gap about 2 points); the ±2-point by-decile criterion was not demonstrated. |
| DST-09 | PARTLY | Pace × efficiency with a Student-t joint. Moment matching is tested; a per-league PIT histogram was not produced. |
| DST-10 | PARTLY | Empty-net late-game state with a stepwise DP that converges to the closed form. Rates are `ILLUSTRATIVE`, not fitted to the archive, so the ±2-point archive match is not demonstrated. |
| DST-11 | PARTLY | Exact innings dynamic program checked against brute force and a ball-by-ball simulation; chase stopping rule with boundary overshoot; toss branch; reduced-overs ratio. No ball-by-ball archive was available to calibrate it, so the cricket engine is NOT_FITTED. |
| DST-12 | IMPLEMENTED | NRL (Conway–Maxwell–Poisson tries, negative home share, kicking, half-time) and AFL (shots × conversion) reproduce league spread and correlation in archive round-trip tests. |
| DST-13 | IMPLEMENTED | No literal 1.55 / 1.20 / 112 defaults remain in `runtime/src` (grep-checked); engines require a league profile. |
| DST-14 | IMPLEMENTED | NFL margin weights; key-number mass (3, 6, 7, 10, 14) within 1 point on 2023–2025 games, weights learned on 2015–2025. |
| DST-15 | IMPLEMENTED | Quantile reconstruction is monotone and non-crossing (`common/distributional.py`). |
| ML-03 | PARTLY | Rolling-origin receipts with monthly refits for NHL, NBA, MLB, NFL, NRL, AFL and EPL under `research/model_builds/runtime_h0/`. Cricket and tennis have no receipt (no data). Home-win interval below zero: AFL, EPL. Margin cover: AFL, EPL, MLB. Totals: none. See `NUMERICAL_MODEL_REGISTER.md` §6. |
| ML-04 | IMPLEMENTED | Dixon–Coles with a time-decay ξ chosen by cross-validation and a vectorised fit (timing tested). |
| ML-05 | IMPLEMENTED | Rolling calibration layer reporting slope and intercept with intervals. |
| ML-06 | NOT MET | Dependency-free histogram gradient boosting for Poisson rates, Gaussian means and log variance (`common/boosting.py`) and a rolling-origin comparison in NHL, NBA, EPL and MLB. The acceptance test (beats the baseline on log loss and CRPS in at least two sports, interval below zero) was **not met in any sport**; the challenger is not used. |
| ML-07 | IMPLEMENTED | Elo, Glicko (published worked example reproduced) and a rating baseline. |
| ML-08 | IMPLEMENTED | JSON artifacts with hashes; loading executes no code. |
| ML-09 | IMPLEMENTED | BigQuery module reduced to point-in-time feature joins and BOOSTED_TREE challengers; no project hard-coded; the register states the scope. |
| ML-10 | IMPLEMENTED | Chronological linear and logit stacking, used only if it beats the best single model on TEST. |
| EVL-01 | IMPLEMENTED | `scoreboard publish/verify`: deterministic, byte-comparable, built only from retained settlement tables, the ledger and the legacy rank log. |
| EVL-02 | IMPLEMENTED | Promotion gate with week-block bootstrap intervals, calibration-slope interval, seed stability and power (`FixedCohortEvaluator`). |
| EVL-03 | IMPLEMENTED | Block structure required; interval wider than i.i.d. on correlated synthetic data (tested). |
| EVL-04 | PARTLY | Six pre-registered experiments (XCARD-1..6, SEL-1) in `research/experiments/cross_card_v1.json` with power calculations. XCARD-3..6 are infeasible within 26 weeks at current card volume; XCARD-6 is blocked pending a machine-readable ladder. |
| EVL-05 | IMPLEMENTED | The scoreboard reports COUNTED, RANK1_UNSTABLE and informational cohorts separately; the headline counts only the first. |
| GOV-01 | IMPLEMENTED | Settlement register is a pointer with pinned history (kinds `carryover` and `settled`); verifiers read the pointer instead of hard-coded counts. |
| GOV-02 | IMPLEMENTED | `custody_text` hashes CRLF-normalised bytes; tests cover LF and CRLF checkouts. The full custody verifiers still cannot pass on a clean checkout: 52 local-only source bodies are gitignored by design. |
| GOV-03 | IMPLEMENTED | `settlement_lint` flags the R1 blocks of P-539–P-545 and any new blank-contract `P` row; the five historical rows (P-407 R1, P-409 R2, P-410 R5, P-419 R5, P-430 R5) are reported as `UNKNOWN_CONTRACT`. |
| GOV-04 | IMPLEMENTED | Retirement, listed-pitcher and abandonment rule fields are required on v3 cards. |
| GOV-05 | IMPLEMENTED | `CURRENT_STATE.md` is generated and verified; living documents no longer state a next ID or destination (a test fails if they do); superseded manifests moved unchanged to `archive/controls/`; removed paragraphs kept in `archive/status_notes/`. |
| GOV-06 | IMPLEMENTED | Seven zero-byte root scripts deleted; the two unused files moved to `archive/legacy_root/`; `validate_austria_bundesliga.py` moved to `research/src/`. |
| GOV-07 | IMPLEMENTED | `settlement_sla` (72 h after the final plus a per-sport allowance; open carryover at most 5). No carryover is open now (the final settlement closed all 72 records). |

**Counts.** 57 recommendation IDs: 41 implemented, 11 partly implemented (SRC-01, SRC-07, PRD-02, DST-04, DST-06, DST-08, DST-09, DST-10, DST-11, ML-03, EVL-04), 3 pending prospective data (SRC-02, SRC-03, PRD-03), 1 not met offline (SRC-04) and 1 built but not met (ML-06: the challenger did not beat the baseline). On CPython 3.14.6 the full suite (`research/tests`, `research/operations`, `research/experiments`, `runtime/tests`) passes with 634 tests and no skips; ruff and mypy are clean. `verify_custody` and `verify_all_logs` cannot pass on a checkout that lacks the 52 gitignored local-only source bodies.

**What this does not establish.** Nothing here changes an issued forecast, certifies a model, or shows that the new rules raise the win rate: PRD-03, SRC-02 and SRC-03 need prospective cards, SRC-04 needs web access, and the engines' rolling-origin evidence is development evidence on opened data. The thresholds in `selection_rules.json` remain provisional.

---

## 6. Sequenced roadmap

| Phase | Window | Items | Outcome |
|---|---|---|---|
| 0: Make it run and be right | Week 1 | ENG-01, ENG-02, ML-01, ML-02, DST-01, PRD-01, GOV-03 | Runtime imports, CI green, calibrator correct, no silent fallbacks, no q-ordering |
| 1: Coherent distributions | Weeks 1–3 | DST-02, DST-03, DST-04, DST-13, GOV-02, GOV-01 | Full-game endpoints coherent; tennis overdispersion; platform-independent custody |
| 2: Data foundation | Weeks 2–6 | SRC-05, SRC-01 (top 5 leagues), SRC-02, SRC-03, GOV-04, GOV-07 | Standard archive schema; adapters for the most-forecast leagues; settlement fields captured on time |
| 3: Fitted models on cards | Weeks 4–10 | ML-03, ML-04, DST-05–DST-09, ML-05, PRD-04 | Cards use fitted engine distributions plus calibration; candidate ladder tooling implements Rule P4 |
| 4: Selection and feedback | Weeks 6–12 | PRD-02, PRD-03, PRD-05, PRD-09, EVL-01–EVL-05 | Rank-2 diversification and Rank-1 gates, measured on a live scoreboard |
| 5: Challengers and breadth | Quarter 2 | ML-06, ML-07, DST-10–DST-12, DST-14, SRC-04, SRC-06–SRC-08, ML-08–ML-10, PRD-06–PRD-08, GOV-05, GOV-06 | Boosted distributional challengers, remaining sports, governance simplification |

**How to tell it is working:** over a 12-week prospective window, track Rank-1 win rate, Rank-2 win rate (target: clearly above the ranks 3–4 rate) and calibration slope (target: CI containing 1). Also track the share of settled rows at evidence grade A/B (target ≥ 95%) and the recurrence of the six failure classes (target: near zero for the classes with a validator rule).

---

## 7. Notes on accuracy and limits

- Historical win rates use literal grades from the rank index, which includes provisional and later-corrected rows. They are learning diagnostics, not certified performance.
- The tennis overdispersion figures come from the reproduction script with a chosen σ = 0.05; the correct σ must be fitted (DST-04). The direction of the effect is robust: any positive σ lowers deciding-set mass and the 22.5 Over probability for near-equal players.
- Some threshold values (PRD-02's 0.58, PRD-03's 0.62/0.04, PRD-09's family gates) are starting points derived from §3.2. They must be confirmed prospectively before becoming binding.
- Nothing in this document changes an issued forecast or a model weight. The implementation that followed (§5.8) changed controls, tooling and engines only, by explicit instruction.

## Subsequent prediction repair (v8.4 / R4)

The earlier implementation status above is a dated record. The later [repair report](research/verification/prediction_repairs_2026-10-09/REPORT.md) supersedes its runtime receipt interpretation: v1 profiles leaked test-season information, winner scoring excluded draws inconsistently, and fitted artifacts/calibration were not loaded by the card generator. Corrected evidence is versioned in `runtime_h0_v2`; archived v1 receipts are not silently replaced. Gated scoreboard wins require a recorded PASS, while historical unknown-gate results remain separate diagnostics. Neither these repairs nor a passing test suite demonstrates prospective predictive improvement.
