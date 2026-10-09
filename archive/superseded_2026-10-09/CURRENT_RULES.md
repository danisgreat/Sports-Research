# Current operating rules

**Current state** (method, control revision, active freeze, next canonical ID, active Combined Log) is generated in [CURRENT_STATE.md](CURRENT_STATE.md); this page states rules, not state. Earlier dated status notes are kept verbatim in [archive/status_notes/](archive/status_notes/SUPERSEDED_STATUS_PARAGRAPHS_2026-10-09.md). The recommendations of the October 9 [framework retrospective](FRAMEWORK_RETROSPECTIVE_2026-10-09.md) were implemented on 2026-10-09; its §5.8 records what is implemented, what awaits prospective data and what could not be met offline.

## October 9 local-mini lifecycle (CR-2026.10.09-R4)

Cards from P-557 onward move through six operator prompts in [research/prompts/](research/prompts/README.md). The format is [`mini-log-3`](CARD_AND_LOG_TEMPLATES.md#local-mini-format-mini-log-3) (a superset of `mini-log-2`, which stays valid for minis already in progress).

1. **Start a mini (prompt 2, external chat agent, GitHub read-only).** The first working ID is the larger of the repository's next canonical ID and the previous mini's highest working ID + 1. Only `PENDING_EVENT` cards from the previous settlement carry forward. Creating a mini consumes no ID.
2. **Write cards (prompt 1).** One event = one working ID, issued in order and never changed. Each card names one distribution object, prices four candidates from it under Rule P4 (probabilities mandatory, p_card ≤ 90%, ranked by p_card, no q column), and prints the joint top-two failure probability, computed from the joint grid; it replaces a correlated Rank 2 when that exceeds 35%. The **Rank-1 gate** (provisional, `runtime/config/selection_rules.json`) requires p_card ≥ 62% and a lead of at least 4 points over the best non-complementary alternative; a card that fails it is labelled `RANK1_UNSTABLE`, which routes it to its own scoreboard cohort. A card also carries a decision block (≤ 4096 bytes) with the evidence in an appendix, an adjustments table (an adjustment above 0.25 SD that changes the top two makes the card `ADJUSTMENT_DEPENDENT`), regime flags, the contract-definition fields, the settlement fields with a capture time, and retained evidence snapshots. Corrections and late news are dated `ADDENDUM` blocks under the existing ID.
3. **Settle (prompt 3), within 72 hours of each final, with open carryover at or below 5.** Freeze the mini byte-exactly, then append the settlement section. Every terminal event is settled on the A/B/C/E/OP/X evidence hierarchy (X = VOID), applying the card's own retirement, listed-pitcher and abandonment rules; only non-terminal events stay `PENDING_EVENT`. R1 copies the card's own ranking (`settlement_lint`). Counting follows Rule T2, every settlement carries R1–R12, and every Rank-1 loss has the Rule R1 deep retrospection with a failure class from the taxonomy.
4. **Import (prompt 4, Claude Code).** `import_mini plan`, then `apply`, commits each card's exact bytes through `log_card` under its working ID. It then appends addenda and settlements under the same ID, stops before any write on an identity conflict or ID collision, and is idempotent.
5. **Roll over (prompt 5)** when the active Combined Log should close. `rollover apply` consumes no ID, then a new control manifest is issued.
6. **Retrospective (prompt 6)** once enough new cards are settled. `cohort_review` reports Rule T2 metrics, slot comparison, calibration, joint failure and failure classes. Recommendations stay `PROPOSED_NOT_TESTED`.

The validators enforce structure, not judgement. A card that passes `mini_log verify` still needs honest research, a reproducible distribution and sound ranking.

## October 9 rules: top-two counting, Rank-1 retrospection and analyst-derived picks (CR-2026.10.09-R1)

The user added these three rules on 2026-10-09. They apply to every card from **P-557** onward and to every settlement or re-scoring performed from 2026-10-09. They never rewrite an original forecast, probability, rank or contract. Where an older paragraph below conflicts with them, these rules control.

**Rule T2: only the top two ranked picks can count as a win.**
1. A card ranks four candidates. **Rank 1 and Rank 2 are the card's picks; ranks 3 and 4 are informational alternates.**
2. Ranks 3–4 are still graded exactly and kept for calibration and learning. They never count as wins in card summaries, cohort summaries, win rates, hit rates or any performance statement. A rank-3/4 win never offsets a rank-1/2 loss.
3. Classify each settled card by its live top-two rows: `TOP2_ALL_WON`, `TOP2_SPLIT`, `TOP2_ALL_LOST`, or `VOID` (no live top-two row). Report counted wins over live top-two rows, Rank-1 W/L/VOID, Rank-2 W/L/VOID and Hit@2. VOID and PUSH rows leave the denominators; they are never losses.
4. The two picks share one event. They are not independent trials, and every numerical card reports their joint failure probability.

**Rule R1: a Rank-1 failure requires a deep and thorough retrospection.**
A Rank-1 LOSS must carry a dated deep retrospection in the same settlement record. A settlement with a failed Rank 1 and no deep retrospection is incomplete. Required parts:
(a) **Claim:** the exact proposition, p_card, the evidence it was ranked on, and its gap to Rank 2.
(b) **What happened:** the endpoint and the mechanism that decided the row.
(c) **Distribution check:** where possible, recompute the card's distribution, locate the outcome in it (tail mass or z-score) and stress the decisive assumption.
(d) **Knowability:** what was available at cutoff, as against post-event only.
(e) **Verdict:** one or more of variance, ranking/selection, model/distribution, data/source, contract/endpoint, timing, adjustment.
(f) **Own-top-two counterfactual:** what Rule P4 would have ranked first and second using cutoff information only.
(g) **Failure class:** a tag from the failure taxonomy, linked to earlier cards with the same class.
(h) **Proposed correction:** testable, with an acceptance criterion. It stays `PROPOSED_NOT_TESTED` until evaluated chronologically; no model weight changes on one event.
A Rank-1 VOID or PUSH needs no deep retrospection, but the reason is recorded.

**Rule P4: supplied contracts and lines are reference only; the analyst derives its own top two out of four.**
1. Contracts and lines supplied with an individual game log or request are reference metadata. They do not fix the candidate set or the ranking.
2. Build the event distribution first. Use the framework's sport method and probability toolkit: a score matrix, PMF or simulation from the sport engine, plus a registered ML model where one exists. Otherwise use an explicit, reproducible `UNCALIBRATED_ANALYST_SCENARIO`. All candidate probabilities come from that one distribution.
3. Form exactly four candidates from (i) the supplied contracts at their supplied lines and (ii) analyst-derived sporting propositions priced from the same distribution. The derived kinds are winner/double chance, handicap/spread, match total, team total and period total, on the sport's standard line ladder. Each candidate states its exact proposition, line, period, endpoint and tag (`SUPPLIED` or `ANALYST_DERIVED`, the latter naming the supplied row it replaces). Degenerate propositions with p_card above 0.90 are excluded so the picks stay informative.
4. Rank by p_card from that distribution: the probability the proposition wins on its sporting endpoint. Never rank by q, edge or narrative. A supplied contract is used only when it is the best suited or the most likely to win once the top two are ranked. Being supplied gives it no priority.
5. SPORTS_ONLY / MARKET_BLIND still holds. Analyst-derived lines come from the distribution and the standard ladder, never from odds pages. A user-supplied line remains contract metadata.

Authority: **MDS-2026.10.09-v8.4 / CR-2026.10.09-R4** (with numerical runtime extension **CR-2026.10.06-NUMERICAL-1**); scoring **SCV-2026.10.09-v5**. The October 9 rules above (T2, R1, P4) control ranking, counting and retrospection, and the local-mini lifecycle controls how cards are written, settled and imported. The user's instruction authorizes research regardless of calibration, canonical import, and the full implementation of the numerical ML runtime architecture ([NUMERICAL_MODEL_REGISTER.md](NUMERICAL_MODEL_REGISTER.md), [H0_DATASET_CARD.md](H0_DATASET_CARD.md), [DATA_SOURCE_REGISTER.md](DATA_SOURCE_REGISTER.md), [RULES_NHL.md](RULES_NHL.md)). Issued historical values remain unchanged.

## Requested research — controlling default

Research every requested sport and event. Missing registered models, approved baselines, calibrated probabilities, fixed fixture universes, source-independence audits or pre-start buffers do **not** block analysis, ranked picks or canonical IDs. Provide the best supported assessment with uncertainty and missingness. Use qualitative ranks when reliable numerical estimates are unavailable. Explicit analyst scenarios are allowed with reproducible calculations, named assumptions and an uncalibrated label; never call them validated probabilities.

Use late news and continue beyond scheduled start when requested. Record actual research/log times, observed state and the source's own update time. A stale 0–0 or initialized inning cannot prove pregame status. Label late, live or start-unverified analysis honestly. No preset 5–15-minute buffer, 30-second deadline or mandatory early freeze applies to requested research. Retain each delivered version for audit, and date later changes without backdating.

All requested game cards, including uncalibrated, qualitative, live/late and historical imports, go directly to the configured active combined log through `research.operations.log_card`. A P-ID identifies the retained card independently of calibration or performance certification. The workflow retains original bytes, allocates under the common ledger lock, journals preparation, appends the complete card, verifies its exact bytes and journals commitment. `RESEARCH_LOG_PREPARED`/`RESEARCH_LOG_COMMITTED` are distinct from the frozen certified issuer's `ISSUE_*` records. Recover any pending append before assigning another ID. Duplicate event/source/body returns its existing ID; changed content requires a dated addendum against that ID.

Use `py -3.14 -m research.operations.log_card next-id`, `commit card.json`, then `verify`. Mini logs are fallback storage only if the active combined log cannot be written. Imported minis become reference copies with canonical pointers. Report imported IDs and the actual next ID. Preserve original forecast evidence and all reserved IDs. Sources, honesty and SPORTS_ONLY / MARKET_BLIND remain required. Weather is environmental evidence, not an independent sporting-event lineage.

Provide four ranked candidates when requested, of which Rank 1 and Rank 2 are the picks (Rules T2 and P4), plus the potential winner, exact sporting propositions, reasons and failure routes. `UNCALIBRATED_QUALITATIVE` uses `NOT_ESTIMATED` percentages and baseline. Close ranks are uncertain. A missing bookmaker/operator definition affects later operator settlement, not analysis of explicitly defined sporting propositions. Explain complementary totals, covering run lines, ties and extra innings; do not count correlated picks as independent games. No retrospective or settlement until requested.

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

