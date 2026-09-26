# Probability scoring and validation


> **CR-2026.09.21-3 audit reconciliation:** scoring/evaluation findings marked superseded or rejected in `archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md` are non-operative. CR-3 additionally removes surviving live gate references to pseudo-tail/path-count/separation-floor shortcuts. Frozen historical probabilities remain unchanged.




Version: **SCV-2026.09.19-v2**. Operational authority for scoring, conditioning and evaluation. Historical cards retain their issued probabilities and method versions. All existing combined logs remain **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
## Universal verification prerequisite — CR-2026.09.19-4


Do not score, settle or retrospectively evaluate an event until its identity, date/time and terminal state pass the universal verification gate: **at least three independent reliable source lineages**, timezone-aware venue-local → `Australia/Melbourne` conversion, and three-source explicit terminal-state confirmation for settlement.


A score without a final marker is not enough. A credible current `LIVE/IN PROGRESS` source or material source conflict leaves the record unresolved. Search snippets/generated summaries do not count as settlement evidence. Historical cards remain attached to the method/control version under which they were issued.


## 1. Define the event before its probability


Record event cluster, target ID, competition, period, endpoint, activation, operator action/void rules, cutoff, issue time, information-availability time, method and control-set hash. Research outcome and operator settlement are separate fields. Evaluate activation first; NO ACTION, VOID, censored and unresolved records are not silently converted to losses or decisive trials.


For an active integer total L, derive u=P(T<L), j=P(T=L), o=P(T>L) from one distribution; u+j+o=1. Over has W/P/L=(o,j,u); Under has (u,j,o). Half-lines have j=0 on integer support. If these masses are conditional on action, label that conditioning; separately record action probability when estimated. Unknown action probability stays unknown. Quarter-lines retain their full settlement categories or equal-stake child contracts; never flatten a half-win into WIN.


Rank by the frozen objective, normally unconditional probability of winning the active contract. A push is not a win, so lower ranking due to push mass can be correct. Do not replace this objective with non-push direction without saying so.


## 2. Proper scores


| Target / diagnostic | Definition | Denominator |
|---|---|---|
| Complete W/P/L Brier, primary for push-capable contracts | 0.5 × sum over W,P,L of (p_category − one_hot_outcome)^2; range 0–1 | All action-settled W/P/L outcomes, including pushes |
| Complete categorical log loss | −log(probability assigned to the realised category); zero probability gives infinity | Same complete outcomes |
| Decisive-direction binary Brier | q=P(W)/(1−P(P)); score (q−I(W))^2 | WIN/LOSS only; undefined if P(P)=1 |
| Win versus non-win diagnostic | (P(W)−I(W))^2 | Include pushes as non-wins; this does not call a push a ticket loss |
| Ordinary binary Brier | (p−I(event))^2 | Exactly two exhaustive outcomes with identical action terms |
| Integer-distribution RPS / CRPS | Sum over integer k of (F(k)−I(y≤k))^2, in target units | One distribution per game and endpoint |


Never compare scores with different category scaling, conditioning, action filters or populations. Legacy WIN/LOSS Brier using unconditional win probabilities is retained only as LEGACY_MIXED_DIAGNOSTIC; it is not the corrected decisive score. Do not invent missing push masses to repair old rows. Recompute new diagnostics only where the entire frozen vector survives, with a separate scoring-version record.


P-443 Over 8: frozen W/P/L=(0.45,0.13,0.42), hence decisive q=0.45/0.87=0.5172413793. The eight recent MLB preferred totals have legacy Brier 0.2591, decisive Brier 0.245720512 and half-scaled categorical Brier 0.259225. These are different measurements of unchanged forecasts, not model improvement.


## 3. One target decision, one event cluster


Keep every row for settlement and coherence. Exact complementary binary rows have identical Brier errors: count the frozen preferred side once in a decision score. An integer pair is one three-category target, including pushes. Label FORCED_PAIR and FREE separately; select highest-ranked scoring total using issue-time ranks before looking at outcomes. Record every analyst-considered line and the fixed selection rule, including rejected lines.


**Top over/under review trigger (user directive, 2026-09-19).** Identify, from issue-time ranks alone and before any outcome is known, the card's **highest-ranked over/under target** and its frozen preferred side. If that side does not win — including when it pushes — the card receives the enhanced failure review defined in `METHOD.md` §7, on the same terms as a Rank #1 loss. Record the trigger as `TOP_OU_REVIEW` beside the Rank-#1 flag so the two are separately countable. This is a retrospective-scrutiny rule and changes no probability, rank or selection rule; in particular it must not be satisfied by hedging a pair, by declining to rank a total, or by shading a stated probability.


**Covering pairs (`G-L22(c)`, added 2026-09-24(f); implemented here 2026-09-25).** Two ranked rows whose union covers every settlement outcome are labelled `COVERING_PAIR`. Examples are opposite +1.5 run lines in MLB, where ties are impossible, and an ML plus the opponent's +1.5. Such a pair records at least one win by construction, and both rows win exactly in the overlap state (a one-run game: 27.6% of 2026 MLB finals, n = 2,374; `BASE_RATES_REGISTER.md` §5). For the card concerned, Hit@2 and "at least one of the top two won" are excluded from top-two reliability summaries. Report which member was preferred, whether it won, and P(overlap). A covering pair may still be the honest ranked output of a supplied slate. What is forbidden is counting it as skill, or seeking it to guarantee a win.

Report row, distinct-target decision and event counts separately. Give each event equal weight after averaging its prespecified target scores. Preserve pregame/live and endpoint distinctions and cluster resamples by event, with schedule-block sensitivity when relevant. Do not add family-specific retrospective tallies that used different selection rules.


## 4. Baselines, development and prospective evidence


Use a competition/endpoint/horizon-specific empirical baseline trained only on earlier games, scored on exactly the same events and thresholds. A binary p=0.5 reference is an optional diagnostic, not the main comparator. Match target difficulty using the frozen baseline probability or quantile, sport, endpoint and line band; stated-p bands and absolute normalised distance alone are insufficient.


Freeze event universe, exclusion reasons, TRAIN/TUNE/CAL/TEST dates, candidate settings, features, thresholds, metrics, uncertainty method and decision rule before evaluation. Fit preprocessing and recency weights within training folds. Group all views of one event. Calibration is optional if unsupported, but any fitted calibrator requires its own later disjoint CAL block and a coherent final distribution. Open an untouched TEST once and retain unsuccessful results; changes require a new test population.


Report paired event-level score differences, uncertainty, count calibration, interval coverage and width, endpoint support and important slices. Lower Brier alone does not prove improved calibration. The 25/50-card and 150-game milestones schedule reviews, not automatic promotion. Retain the simpler candidate when evidence is inconclusive. No recalibration from the current mixed log.


A prospective trial requires a frozen manifest timestamp, forecast timestamp before the event, outcome-availability timestamp after forecast, and matching method/control version. Import date cannot substitute. C-OU-GEOMETRY currently has **zero verified prospective cards**: P-425/P-426/P-427/P-429 were issued on 15 September before its 16 September manifest; the rest lack the complete verified manifest-time join. Keep all existing cohorts as historical development observations. A locally generated hash is content evidence, not independent timestamp proof.


## 5. Distribution construction and uncertainty


One joint event distribution supplies team totals, combined totals, margins, winner, phase relationships and joint success/failure queries. Scenario states must be exhaustive and disjoint; otherwise provide joint bounds with JOINT_UNQUANTIFIED. A modal or representative score illustrates a state but is not the full distribution.


Derive exact CDF/PMF probabilities at each line. Cross-family absolute centre-to-line distance does not order probabilities. Specify mean versus median and width definition/coverage. Integrate uncertainty through stated priors or weighted scenarios; hierarchical shrinkage and asymmetric mixtures may change both mean and variance. No unexplained signed lean, zero-centre shrinkage, universal variance floor, or row-level numerical cap after deriving a distribution. Evidence-grade caps such as LOW remain separate from probabilities. If a different subjective distribution replaces a fitted calculation, label it and regenerate every dependent row.


L5/L10/L15/L20 and H2H windows remain required descriptive retrievals where available; record missingness and continuity. They overlap and are not independent replications. Monotonic windows and dispersion of their averages do not establish a trend or noise. Any inferred recency effect requires opponent/regime context and a declared estimation method tested in time order.


Review realised tails on both successful and unsuccessful cards. One named failure does not prove its mass was too low. C-RUN-CENTRE-BIAS stays development-only: separate leagues, actual means, medians and informal corridor midpoints before estimating residual bias. No generic Over/Under tilt, automatic phase preference or fixed shrink factor is promoted.


## 6. Period bounds and model admission


For a whole-game count C and regulation count R, 0≤R≤C alone cannot prove R exceeds an Over threshold. A bounded grade requires a documented lower/upper bound that gives the same settlement for every admissible split. P-255/P-256 regulation corners are UNRESOLVED_PERIOD until a valid split or bound is recovered. Keep their original predictions and append the correction.


Source admission is per field, target and cutoff. A source's general CANDIDATE label does not prove point-in-time feature fitness. Historical current feeds can supply revised labels for a development backtest but cannot prove what a past forecaster knew. No source access claim, fitted build, test result, calibrator or prospective observation exists merely because its design is written down.


Publication requires source/data integrity, held-out comparison, calibrated or explicitly assessed probability reliability, support/coherence and critical-slice checks, followed by qualifying prospective shadow evidence. M0/M1 market-feature models remain RETIRED. The authorized numerical implementation and its exact status live in NUMERICAL_PROGRAM.md and H0_DATASET_CARD.md.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 7. Deep-research validation standard for totals and lines


Future numerical builds are judged on the **underlying predictive distribution**, not on whether one chosen side happened to win.


Primary scorecard by exact target scope:


- full distribution: CRPS/RPS and log score/negative log likelihood where mathematically valid;
- point summaries: RMSE **and** MAE for expected total/margin/team score;
- push-capable contracts: complete W/P/L Brier and categorical log loss;
- uncertainty: central prediction-interval coverage and width, plus PIT/reliability diagnostics where appropriate;
- probability reliability: calibration intercept/slope and reliability curves with sample uncertainty;
- ranking/hit rate: NDCG/Hit@k/directional accuracy only as secondary diagnostics.


Validation is chronological and event-grouped. Report paired event-level differences between candidates and baselines with block/event bootstrap uncertainty; do not treat multiple lines from one game as independent trials. Publish results by sport, competition, endpoint, line/quantile difficulty and data-quality/source regime.


A flexible model is promoted only if it improves the frozen proper-score objective against the simpler baseline on the untouched chronological TEST **without material calibration/support failure in important slices**. If uncertainty overlaps no-change or critical slices deteriorate, retain the simpler champion and accrue evidence.


No change in this document constitutes an accuracy gain. Improvement must be demonstrated on data not used to design the change and then survive prospective shadow operation.


<!-- ALL-SPORTS-AUDIT-RECONCILIATION-2026-09-21-CR2 -->
## 10. Superseded audit scoring shortcuts


For current evaluation, do **not** revive any of the following historical shortcuts: custom top/bottom penalty records; “one side of the O/U won” as a success metric; treating complementary rows as independent trials; absolute normalized-edge distance as a universal probability ordering across different distributions; hard probability ceilings/floors derived from pooled bands; or post-hoc deletion of process-defective losses/wins to improve a record.


Use the exact target distribution with push/void/censoring mass, one preferred decision per complementary target family, event-clustered denominators, proper scores where validated probabilities exist, and the enhanced Rank-1/top-O/U retrospective trigger. Current logs remain **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** until a separate controlling policy changes that state.




<!-- SCORING-DISTRIBUTION-QUERY-CONSISTENCY-2026-09-21-CR3 -->
## 11. CR-3 distribution-query consistency


For current forecasts, tail checks, target geometry, winner, margin/cushion and phase totals must be queried from the **same frozen event distribution or coherent branch mixture**. Do not convert historical order-statistic stress sums, path-count labels, 40–60% bands or `DISJOINT` labels into probability caps/bonuses or rank bars.


Where no validated numerical distribution exists, retain an explicit qualitative branch set and uncertainty state; do not publish pseudo-precision. This does not alter historical score vectors or resurrect any closed candidate design.


<!-- AUDIT-CLOSURE-2026-09-25 -->
## 12. Settlement-integrity labels (2026-09-24(f) controls; implemented 2026-09-25)

These labels change no forecast probability. They decide what a settled record may be used for.

| Label | Meaning | Consequence for scoring and learning |
|---|---|---|
| `PROCESS_RECORD_UNVERIFIED` | A settlement block whose causal narrative relies on process facts not read from a named record (`C-PROCESS-RECORD-PROVENANCE`) | Grades may stand if the final is verified. The block supports **no** rule, weight, base rate, calibration input or learning-register disposition until the process record is re-read |
| `LINEUP_CLAIM_FALSE` | A player the card named as a driver of the Rank-1 row did not play (`C-LINEUP-DIFF`) | A process defect whatever the result. The card's Rank-1 outcome is reported with the flag and excluded from any "the method worked" summary |
| `COVERING_PAIR` | Two ranked rows jointly cover every outcome (§3) | Hit@2 is excluded from top-two reliability summaries |
| `FIELD_OWNER_VERIFIED_LT3` | The final was verified from the field owner, plus a second lineage where available, but a third independent lineage could not be re-opened at audit time | The grade stands (no conflicting source exists); the record states the lineage count rather than claiming CR-4 completion |

Descriptive reports list how many cards carry each label beside every Rank-1, Hit@2 and top-O/U figure.

<!-- REPO-HYGIENE-CI-2026-09-25C -->
## 13. Naive population baseline (`C-BASELINE-SKILL`, added 2026-09-25(c))

A Brier score is reported beside a **baseline on the same decisions**. From 2026-09-25(c) the primary descriptive baseline is the **naive population baseline** recorded as `BASELINE_P` on each card, not the coin flip (0.25).

- **What it knows.** The competition's outcome distribution from games completed before the event, and which side is at home. For tennis it knows no side information.
- **Report.** Card Brier, baseline Brier, their paired difference (card − baseline), and a bootstrap interval that resamples whole cards (rows within a card are dependent). `tools/skill_baseline.py` computes all of this from `SKILL_BASELINE_LEDGER.md`.
- **Counting.** Forced pairs are counted once and pushes are excluded, as elsewhere in this specification.
- **Status.** Descriptive and LEARNING_ONLY. Beating the naive baseline is a *minimum* condition for any later claim that the research process adds information. It is not sufficient for performance eligibility (`PERFORMANCE_ELIGIBILITY_POLICY.md`). Never fit a shrink or weight from it (`L-087`).
- **Seed result (hindsight, 2026-09-24 cohort).** Card 0.2461 against baseline 0.2360, n = 29 decisions from 9 cards, interval [−0.059, +0.089]: no demonstrated difference.

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 14. Calibration review standard (added 2026-09-25(d))

Every 25-card pattern review, and every audit of a cohort's probabilities, reports the following from `python tools/calibration_report.py`, run on the rebuilt settled-row dataset (`research/settled_rows_2026-09-25/extract_settled_rows.py`):

1. **Reliability table** by stated band, with Wilson intervals and the number of distinct cards per band.
2. **Murphy decomposition**, Brier = reliability − resolution + uncertainty, plus skill against climatology. Resolution is the only component that shows information. A low Brier on a lopsided population can come from uncertainty alone.
3. **Logistic calibration slope and intercept** of the outcome on logit(p), with their SE. A slope below 1 means the probabilities are too extreme; above 1, too timid.
4. **Slices** (family, sport, direction, rank) on **decisions** (p ≥ 0.5, so forced complements count once). Each gives win rate − mean p with a **card-cluster** bootstrap interval, because rows within a card are dependent.
5. **The baseline difference** (§13), whenever `BASELINE_P` exists.

**Reporting rules.**
- **Rank-slot records below #1 are not reported as evidence of ordering.** In the full record, #2–#4 are indistinguishable (54–56%).
- **A cohort Brier trend is read against its sport mix** before any method-improvement statement.
- **Nothing in this section may be applied back to a forecast as a shrink, weight or cap** (`L-087`). Its outputs feed disclosures (`C-TRACK-RECORD`, `C-LOW-RESOLUTION-BAND`) and prospective tests only.

**First full review (2026-09-25(d)):**

| Measure | Value |
|---|---|
| Rows with p | 598 rows, 149 cards |
| Brier | 0.2249 |
| Reliability / resolution / uncertainty | 0.0020 / 0.0188 / 0.2436 |
| Skill against climatology | +7.7% |
| Logistic slope | 1.06 (SE 0.16) |

Details are in `research/settled_rows_2026-09-25/README.md`.


<!-- RANK-MODEL-2026-09-25E -->
## 15. The ranking probability q (RM-1) and the team baseline (added 2026-09-25(e))

1. **Two probabilities per row.** Each ranked row carries the card's stated p (UNVALIDATED_SUBJECTIVE, from its own distribution) and RM-1's q (`tools/rank_model.py`).
   - q is a **calibrated ranking probability**. It is not a PUBLISHED numerical probability (`NUMERICAL_PROGRAM.md`).
   - Ranks follow q (`C-RANK-MODEL`).
   - Settlement scores **both** (Brier and log loss). Settlement tables add a `q` column: `| Rank | Contract | Family | p | q | BASELINE_P | TEAM_BASELINE_P | Result | Brier(p) | Brier(q) |`.
2. **§14 exception.** §14's rule that "nothing in this section may be applied back to a forecast" continues for everything **except RM-1**. RM-1 is the user-authorised calibration of 2026-09-25(e) (`RULES_GENERAL.md` §"2026-09-25(e)"(h)).
   - It is refitted only at the 25-card review, after `extract_settled_rows.py` and `validate_rank_model.py`.
   - A new term enters only if it beats RM-1 on log loss in every forward split.
3. **Prospective check (`T-RM1-PROSPECTIVE`).** After 25 cards, q's Brier is compared with p's on the same rows. If q is worse, `C-RANK-MODEL` reverts to disclosure-only.
4. **Top-two reporting.** For every review, report:
   - the Rank-1 and Rank-2 win rates;
   - the both-win and both-lose rates;
   - the same four under the p order (counterfactual) and the q order (issued);
   - the Rank-1 record by q tier.

   Covering pairs stay excluded from Hit@2.
5. **`TEAM_BASELINE_P`** joins `BASELINE_P` in the baseline difference (§13) wherever it is printed. For a covered league, "card beats baseline" means it beats TB-1.

**RM-1 as fitted 2026-09-25(e)** (409 decision rows, 154 cards):

| Term | Value |
|---|---:|
| a | −0.187 |
| b | 1.543 |
| c (cushion outside baseball, hockey and soccer) | −1.127 |

| Measure | Stated p | RM-1 |
|---|---:|---:|
| Grouped-CV log loss | 0.6112 | 0.6032 |
| Forward log loss from P-450 | 0.6154 | 0.5861 |


<!-- REVIEW-IMPLEMENTATION-2026-09-26 -->
## 16. The measurement ladder and its reports (added 2026-09-26)

Three yardsticks now sit beside every settled decision, from weakest to strongest. Each is scored as a paired Brier difference with a card-cluster bootstrap. Forced pairs count once, pushes are excluded, and **no difference below is a performance, value or ROI claim**.

| Yardstick | Knows | Ledger / tool | Checkpoint |
|---|---|---|---|
| `BASELINE_P` (§13) | League outcome rates and home side, games before the event | `SKILL_BASELINE_LEDGER.md` · `tools/skill_baseline.py` | 100 prospective decisions / 30 cards |
| `TEAM_BASELINE_P` (§15.5) | Season-to-date team scoring (covered leagues) | printed on the card; scored at settlement | as §15 |
| Closing market (`C-MARKET-BENCHMARK`) | Everything public at the close | `MARKET_BENCHMARK_LEDGER.md` · `tools/market_benchmark.py` | 100 decisions / 30 cards |

1. **Seed rows never count.** `tools/skill_baseline.py` reports the "Prospective rows" and "Seed rows" sections separately; only the prospective section counts toward §13's checkpoint (fixed 2026-09-26: the tool had pooled them).
2. **The closing line is entered after settlement only**, as a no-vig probability with its de-vig method (`multiplicative`, `power` or `shin`). Rows entered before settlement are excluded. See `RULES_GENERAL.md` §"2026-09-26"(d).
3. **Universe split.** Cards in a declared universe (`C-EVENT-UNIVERSE`) and `OUT_OF_UNIVERSE` cards are reported separately in every review; the universe group is the one that describes the competition.
4. **Shadow models.** `tools/mlb_model.py score` (MLB, `C-MLB-SHADOW`) and `tools/sport_models.py score` (every other sport, `C-SPORT-SHADOW`, per league) report A1 against A0 on frozen shadow rows. Their historical rolling-origin validation is in `research/sport_models_2026-09-26/README.md`. It is compared with the cards only at its 150-game review.
5. **One table first.** Every 25-card review opens with `python tools/evidence_status.py`.
