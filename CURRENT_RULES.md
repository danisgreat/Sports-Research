# Current operating rules

**October 8 carryover review:** 65 existing records receive 780 supplied retrospective sections in active Part 7, with no new grades, cards or ledger writes. P-518-P-522 remain reserved. The excluded local P-550 card is preserved only in source custody; canonical next remains P-550, while its local working successor is P-551. [Review, source limits and corrections](research/verification/carryover_review_2026-10-08/REPORT.md).

**October 8 settlement and rollover:** P-538–P-549 were imported without renumbering into Part 6, with original text and dated sporting retrospectives. Part 7 is now active; P-550 remains next and no ID was consumed by its creation. The selected carryover has 65 exact records, including four P-540 retirement rows with UNKNOWN_DEFINITION. See [the complete settlement/rollover review](research/verification/mini_rollover_2026-10-08/REPORT.md).

**Local authority, numerical ML runtime and all-log reconciliation (October 6):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

Authority: **MDS-2026.10.01-v8.0 / CR-2026.10.08-R3** (with numerical runtime extension **CR-2026.10.06-NUMERICAL-1**). The user's instruction authorizes research regardless of calibration, canonical import, and the full implementation of the numerical ML runtime architecture ([NUMERICAL_MODEL_REGISTER.md](NUMERICAL_MODEL_REGISTER.md), [H0_DATASET_CARD.md](H0_DATASET_CARD.md), [DATA_SOURCE_REGISTER.md](DATA_SOURCE_REGISTER.md), [RULES_NHL.md](RULES_NHL.md)). Issued historical values remain unchanged.

## Requested research — controlling default

Research every requested sport and event. Missing registered models, approved baselines, calibrated probabilities, fixed fixture universes, source-independence audits or pre-start buffers do **not** block analysis, ranked picks or canonical IDs. Provide the best supported assessment with uncertainty and missingness. Use qualitative ranks when reliable numerical estimates are unavailable. Explicit analyst scenarios are allowed with reproducible calculations, named assumptions and an uncalibrated label; never call them validated probabilities.

Use late news and continue beyond scheduled start when requested. Record actual research/log times, observed state and the source's own update time. A stale 0–0 or initialized inning cannot prove pregame status. Label late, live or start-unverified analysis honestly. No preset 5–15-minute buffer, 30-second deadline or mandatory early freeze applies to requested research. Retain each delivered version for audit, and date later changes without backdating.

All requested game cards, including uncalibrated, qualitative, live/late and historical imports, go directly to the configured active combined log through `research.operations.log_card`. A P-ID identifies the retained card independently of calibration or performance certification. The workflow retains original bytes, allocates under the common ledger lock, journals preparation, appends the complete card, verifies its exact bytes and journals commitment. `RESEARCH_LOG_PREPARED`/`RESEARCH_LOG_COMMITTED` are distinct from the frozen certified issuer's `ISSUE_*` records. Recover any pending append before assigning another ID. Duplicate event/source/body returns its existing ID; changed content requires a dated addendum against that ID.

Use `py -3.14 -m research.operations.log_card next-id`, `commit card.json`, then `verify`. Mini logs are fallback storage only if the active combined log cannot be written. Imported minis become reference copies with canonical pointers. Report imported IDs and the actual next ID. Preserve original forecast evidence and all reserved IDs. Sources, honesty and SPORTS_ONLY / MARKET_BLIND remain required. Weather is environmental evidence, not an independent sporting-event lineage.

Provide four ranked picks when requested, the potential winner, exact sporting propositions, reasons and failure routes. `UNCALIBRATED_QUALITATIVE` uses `NOT_ESTIMATED` percentages and baseline. Close ranks are uncertain. A missing bookmaker/operator definition affects later operator settlement, not analysis of explicitly defined sporting propositions. Explain complementary totals, covering run lines, ties and extra innings; do not count correlated picks as independent games. No retrospective or settlement until requested.

The sections below retain the separately defined certified performance protocol and archive safeguards. Its source quorum, universe, strict pregame timing, approved-model and prospective-shadow requirements govern **certification only**, never availability of requested research or canonical research IDs. Earlier local documents, Drive copies and frozen issuer code cannot override this default.

## A. Evidence, identity and the source firewall

1. Keep **SPORTS_ONLY / MARKET_BLIND**. No odds, movement, tips, betting previews, prediction markets or fantasy data enter model fitting, manual adjustments, confidence or ranking. A user-supplied line is contract metadata. An after-event market benchmark is separately quarantined and informational.
2. Declare the complete fixture universe before a live cohort. Record league, season, durable event ID, exact teams, scheduled start, endpoint, period and void rule. Unknown official IDs remain unknown. A provider-derived surrogate is permitted only for clearly labelled model research.
3. Fetch approved sources through `sources.py`. Retain the unmodified body, source URL, retrieval timestamp, content hash, parser version and registry hash. Verify retained bytes before parsing. Review the exact field and event, rather than trusting a page title.
4. Independent collection requires a supported lineage audit. Three websites sharing a provider count once. UNKNOWN independence never satisfies a live quorum. Official status establishes field ownership; it does not prove independent collection.
5. Certified live issue and terminal admission use the quorum in `eligibility.py`. Requested research reports conflicts, missingness and source failures and still supplies supported analysis; unresolved settlement remains unresolved.
6. Pregame admission proves fresh pregame state and a scheduled start still in the future. Actual start is verified separately after the event. A schedule time or first-play timestamp cannot silently substitute for actual start.

## B. Probability models and families

Use registered executable models and complete dependency receipts. Verify code, processed inputs, runtime dependencies and distributions. The model must use only information available at its cutoff. `point_in_time.py` excludes postgame awards, future lineups and undefined temporal roles. Historical date-only availability assumptions belong in labelled development experiments.

EPL candidate `epl-coherent-ensemble-0.2.0` uses one score matrix: 0.75 Dixon-Coles plus 0.25 TB1-MD. Its operational research scope is regulation 1X2. Totals and BTTS can be coherent diagnostics, but have not passed qualification against every required baseline. NBL candidate `nbl-oof-width-0.2.0` uses the joint score-model margin mean and a width estimated from strictly earlier out-of-fold residuals. Its scope is regular-season moneyline including overtime. All candidates are **SHADOW_ONLY**.

The previous EPL/NBL versions remain reproducible comparison models. Passing their historical holdout does not qualify a different version or family. Other leagues may receive qualitative analysis or explicit uncalibrated analyst scenarios immediately. Missing trained models do not imply NO_FORECAST or prevent canonical logging. More archived years alone do not establish calibration.

All probabilities for a score-model card derive from one distribution. Record win, push and loss mass; conditional win is win/(1-push). Never treat q as an event probability. Future ranked card rows use `p_card`; coherent paired contracts and joint top-two failure mass are reported. Preserve historical q rankings literally for learning.

A certified-model adjustment uses its versioned approved method. Requested analyst scenarios disclose their source-backed mechanisms and assumptions without a qualification prerequisite; numerical cards recompute coherent distributions. Unsupported certainty or arbitrary confidence percentages are omitted. `NONE` leaves model mass unchanged.

## C. Daily workflow

1. Run the dated daily job. It retains current EPL/openfootball and official NBL observations, final-score snapshots and every fixture disposition. Current single-publisher scores are explicitly provisional for model-only research.
2. Fit verified model builds at the recorded cutoff and freeze shadows before scheduled start. Each includes version, input/body/build hashes, probability vector, family, endpoint and missing lineup/adjustment status.
3. Keep all fixtures in coverage: frozen shadow, no forecast, state conflict, source failure or outside the declared time window. Count coverage and failures, not just successful predictions.
4. Append diagnostic grades when exact official finals appear. They remain performance-ineligible until actual-start and independent terminal evidence pass the separate gate. Source/result truth is distinct from a passing code test.
5. Live preparation uses the complete evidence bundle, frozen universe and current admission/source registries. The issuer renders a reviewable draft without assigning a permanent ID. Live commit revalidates under a lock, checks sufficient time before start, freezes the bundle, journals preparation, appends the active combined log and journals commitment. Interrupted transactions block the next ID until exact recovery.
6. Retain each delivered core at its actual delivery time. Requested research may continue after scheduled start. Append later updates and corrections; never backdate or silently rewrite original probabilities, contracts, ranks or baseline literals.

## D. Learning, scoring and model releases

Historical rank logs and reconstructed ledger views are **LEARNING_ONLY**. Blank cutoffs, baselines and grades are not zero. Multiple contracts under one card/rank, disputed results and unresolved pointers are flagged. A source-linked literal is not an independently audited result.

Use paired chronological comparisons against population and stronger team-sensitive baselines on identical events. Report family-specific log loss, half-scaled multiclass Brier, binary Brier, calibration/reliability with uncertainty, effective sample and week-block bootstrap intervals. Evaluate failures and successes symmetrically. Separate model miss, source/identity error, endpoint/contract error, timing leakage, adjustment miss and missing-field censoring.

October development results use already opened data. They are selection and robustness evidence. Preserve untouched future testing and prospective shadows for release decisions. Do not relabel them as new untouched holdouts.

Live qualification requires an exact model/family/endpoint review, applicable passed holdout, current adapter/issuer evidence and at least 50 unique audited shadows spanning at least 28 days under the coded gate. Do not set LIVE_QUALIFIED from a row flag. All current sources retain UNKNOWN independent collection pending real audits, and all current model registrations remain SHADOW_ONLY.

An adjustment pilot starts only after the exact fixed scoring families qualify, a source-backed sample/power plan exists and the fixture universe is frozen. It uses the first chronological adjusted issues, an immutable lock, at least four week blocks, one persistent interim and a terminal futility decision. A pending earlier settlement cannot be dropped to favour later events. No such live pilot has been started.

## E. Archive and custody

Use canonical archive events plus provenance and season-status tables. Exclude duplicates, mirror copies, subsets and unresolved scores from learning joins. Keep postgame narratives separate. Do not inject whole-season awards into individual game features. Keep source retrieval separate from historical availability. A header-only year is missing, inactive, future or unexplained according to evidence; it is never automatically complete.

Parts 1-5 and the original 141,740-byte P-518-P-522 block in Part 6 remain unchanged. P-518–P-522 stay reserved. The October 1 logging repair imports Oriente–The Strongest, KT–Kia and Chunichi–Hiroshima, then logs Hanwha–Samsung. Read current IDs and next-ID state from the canonical ledger workflow and status register; historical snapshots below do not override subsequent appends. Every requested card goes directly to the configured active combined log.

Run tests, source/archive validation, original-byte checks and the active manifest verification before recording completion. Preserve unrelated pre-existing dirty work. Stage and publish only if separately instructed.

Baseline provenance is mandatory for certified admission: exact lane/league/endpoint/families/version, a pinned approved definition and code artifacts, approval strictly before cutoff, and matching distribution/holdout/shadow/pilot comparator. Hash joins verify retained bytes and declared metadata; they do not independently prove every declared input availability time or recompute every distribution. Review the original source field and baseline construction. The point-in-time feature filter likewise labels declared metadata and cannot confer live admission by itself.

## October 5 reconciliation and closure — current guidance

P-523–P-537 are already canonical. Do not reimport or reissue them. Four overlapping versions are dated addenda. The eleven P-527–P-537 sporting reviews are diagnostic, with 132 retained retrospective sections; they do not certify operator settlements or prospective skill. All 15 records retain separate carryover requirements, including P-537 first-half/corners conflicts. [Carryover](research/verification/closure_2026-10-05/carryover.md) and [implementation evidence](research/verification/implementation_2026-10-05/REPORT.md) bind the exact records.

Before removing a redundant mini, verify its complete archived original against the retained length/hash and map all entries/addenda to the existing canonical IDs. Remove only the redundant working pointer/copy; keep original archive bodies, source receipts, issued cores and historical audit snapshots. Do not allocate an ID for closure.

Missing or damaged source bodies fail full custody verification, including quarantined bodies omitted from Git. Local mechanics PASS is distinct from clean-checkout evidence completeness and sporting/operator certification. Run all required checks even if another check fails. A new administrative receipt records reviewed changes only after failures and evidence limits are retained.

## Earlier October 1 settlement readback — historical snapshot

The dated all-log audit in Part 6 and `research/verification/settlement_2026-10-01/REPORT.md` controls the current diagnostic queue. P-518–P-522 have known ranked-row sporting outcomes but remain reserved and uncertified; issue-time, baseline, actual-start and source-independence work is still unresolved. The intake mini-log contains a manual claim for P-523 and an earlier contradictory empty-header/next-P-524 assertion. Its four goal rows are diagnostic W/W/L/L; its unknown corner line remains unissued. No canonical issue transaction exists, and P-523 remains unconsumed. The archive of original headers/forecasts is preserved. This changes no model qualification or future ranking rule.

## Fifteen experiments — measures implemented, results pending

Use [the experiment measures and next steps](research/experiments/NEXT_STEPS.md) for all fifteen registered hypotheses. Freeze exact candidate/comparator artifacts, targets, future cohort, separate-pilot sample plan, declared dependence/adapter audits and justified acceptance tolerances before collecting the experimental forecasts. Capture real timestamps through `research.experiments.runner`; preserve all pending, void and abstention dispositions. Numerical measurement requirements govern experiment evaluation, never access to requested research or canonical logging. A statistical candidate-for-review result does not qualify or deploy a model. Existing qualification and source admission controls remain in force.

## F. Numerical ML runtime & predictive modeling standards

1. **Event-First Principle**: Models estimate the discrete probability mass function of the sporting event $P(Y = y \mid X)$. Bookmaker contract probabilities (Over/Under, spread, moneyline, 1X2) are derived directly from that distribution. Monotonicity across thresholds is mathematically guaranteed: $P(\text{Over } K_2) \le P(\text{Over } K_1)$ for $K_2 > K_1$.
2. **Pregame vs. Live Engine Separation**: Pregame models and live models are separate pipelines with distinct model identifiers. Live models condition on $P(Y_{\text{future}} \mid Y_{\text{observed}}, \text{state}_t)$ rather than naively extrapolating pregame rates.
3. **Point-in-Time Feature Store**: Training features must satisfy $known\_at \le cutoff\_at$. If availability before cutoff cannot be proven, the feature is marked `MISSING`.
4. **Market Snapshot Semantics**: If market price evaluation is conducted, the market quote must be timestamped at or before forecast cutoff. Post-event or closing odds are strictly quarantined for retrospective benchmarking and cannot retroactively claim predictive edge.
5. **Rolling-Origin Splitting**: All evaluation adheres to strict chronological `TRAIN` $\to$ `TUNE` $\to$ `CAL` $\to$ `TEST` partitioning. Calibrators are fitted strictly on the out-of-fold calibration set.
6. **Staking & Kelly Protection**: Fractional Kelly staking is disabled until models achieve validated calibration and edge persistence across untouched out-of-sample data.

