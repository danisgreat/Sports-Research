# Current operating rules

Authority: **MDS-2026.10.01-v7.0 / CR-2026.10.01-I1**. Applies to new work. Issued historical forecast values remain frozen. The user's October overhaul authorizes code/data/process improvements; it does not authorize manufacturing future evidence.

## A. Evidence, identity and the source firewall

1. Keep **SPORTS_ONLY / MARKET_BLIND**. No odds, movement, tips, betting previews, prediction markets or fantasy data enter model fitting, manual adjustments, confidence or ranking. A user-supplied line is contract metadata. An after-event market benchmark is separately quarantined and informational.
2. Declare the complete fixture universe before a live cohort. Record league, season, durable event ID, exact teams, scheduled start, endpoint, period and void rule. Unknown official IDs remain unknown. A provider-derived surrogate is permitted only for clearly labelled model research.
3. Fetch approved sources through `sources.py`. Retain the unmodified body, source URL, retrieval timestamp, content hash, parser version and registry hash. Verify retained bytes before parsing. Review the exact field and event, rather than trusting a page title.
4. Independent collection requires a supported lineage audit. Three websites sharing a provider count once. UNKNOWN independence never satisfies a live quorum. Official status establishes field ownership; it does not prove independent collection.
5. Live issue and terminal admission require the source quorum implemented in `eligibility.py`, exact event/endpoint agreement and at least one official source. Conflict, missingness, unavailable sources and schema drift produce a documented no-forecast or unresolved settlement.
6. Pregame admission proves fresh pregame state and a scheduled start still in the future. Actual start is verified separately after the event. A schedule time or first-play timestamp cannot silently substitute for actual start.

## B. Probability models and families

Use registered executable models and complete dependency receipts. Verify code, processed inputs, runtime dependencies and distributions. The model must use only information available at its cutoff. `point_in_time.py` excludes postgame awards, future lineups and undefined temporal roles. Historical date-only availability assumptions belong in labelled development experiments.

EPL candidate `epl-coherent-ensemble-0.2.0` uses one score matrix: 0.75 Dixon-Coles plus 0.25 TB1-MD. Its operational research scope is regulation 1X2. Totals and BTTS can be coherent diagnostics, but have not passed qualification against every required baseline. NBL candidate `nbl-oof-width-0.2.0` uses the joint score-model margin mean and a width estimated from strictly earlier out-of-fold residuals. Its scope is regular-season moneyline including overtime. All candidates are **SHADOW_ONLY**.

The previous EPL/NBL versions remain reproducible comparison models. Passing their historical holdout does not qualify a different version or family. Other leagues remain `NO_MODEL` for numerical issuance until they have their own reconciled data, frozen test and registration. More source access or archived years alone does not qualify a model.

All probabilities for a score-model card derive from one distribution. Record win, push and loss mass; conditional win is win/(1-push). Never treat q as an event probability. Future ranked card rows use `p_card`; coherent paired contracts and joint top-two failure mass are reported. Preserve historical q rankings literally for learning.

A new manual adjustment requires an approved versioned method, pre-cutoff source artifacts, a named mechanism and frozen parameters. Recompute the whole distribution; record `p_model`, `p_card` and `p_baseline` separately. Unsupported adjustments are omitted. Default `NONE` leaves the model distribution unchanged. An arbitrary confidence factor or subjective percentage is insufficient.

## C. Daily workflow

1. Run the dated daily job. It retains current EPL/openfootball and official NBL observations, final-score snapshots and every fixture disposition. Current single-publisher scores are explicitly provisional for model-only research.
2. Fit verified model builds at the recorded cutoff and freeze shadows before scheduled start. Each includes version, input/body/build hashes, probability vector, family, endpoint and missing lineup/adjustment status.
3. Keep all fixtures in coverage: frozen shadow, no forecast, state conflict, source failure or outside the declared time window. Count coverage and failures, not just successful predictions.
4. Append diagnostic grades when exact official finals appear. They remain performance-ineligible until actual-start and independent terminal evidence pass the separate gate. Source/result truth is distinct from a passing code test.
5. Live preparation uses the complete evidence bundle, frozen universe and current admission/source registries. The issuer renders a reviewable draft without assigning a permanent ID. Live commit revalidates under a lock, checks sufficient time before start, freezes the bundle, journals preparation, appends Part 6 and journals commitment. Interrupted transactions block the next ID until exact recovery.
6. Freeze every core before the event. Append settlements and corrections; never edit core probabilities, contracts, ranks, cutoff or baseline literals after issuance.

## D. Learning, scoring and model releases

Historical rank logs and reconstructed ledger views are **LEARNING_ONLY**. Blank cutoffs, baselines and grades are not zero. Multiple contracts under one card/rank, disputed results and unresolved pointers are flagged. A source-linked literal is not an independently audited result.

Use paired chronological comparisons against population and stronger team-sensitive baselines on identical events. Report family-specific log loss, half-scaled multiclass Brier, binary Brier, calibration/reliability with uncertainty, effective sample and week-block bootstrap intervals. Evaluate failures and successes symmetrically. Separate model miss, source/identity error, endpoint/contract error, timing leakage, adjustment miss and missing-field censoring.

October development results use already opened data. They are selection and robustness evidence. Preserve untouched future testing and prospective shadows for release decisions. Do not relabel them as new untouched holdouts.

Live qualification requires an exact model/family/endpoint review, applicable passed holdout, current adapter/issuer evidence and at least 50 unique audited shadows spanning at least 28 days under the coded gate. Do not set LIVE_QUALIFIED from a row flag. All current sources retain UNKNOWN independent collection pending real audits, and all current model registrations remain SHADOW_ONLY.

An adjustment pilot starts only after the exact fixed scoring families qualify, a source-backed sample/power plan exists and the fixture universe is frozen. It uses the first chronological adjusted issues, an immutable lock, at least four week blocks, one persistent interim and a terminal futility decision. A pending earlier settlement cannot be dropped to favour later events. No such live pilot has been started.

## E. Archive and custody

Use canonical archive events plus provenance and season-status tables. Exclude duplicates, mirror copies, subsets and unresolved scores from learning joins. Keep postgame narratives separate. Do not inject whole-season awards into individual game features. Keep source retrieval separate from historical availability. A header-only year is missing, inactive, future or unexplained according to evidence; it is never automatically complete.

Parts 1-5 and the original 141,740-byte P-518-P-522 block in Part 6 remain unchanged. P-518/P-522 have dated learning-only settlement appends; their reserved identity and performance exclusions remain. P-519/P-520/P-521 retain unresolved reconciliation work. P-523 is the next new ID; empty mini-log headers consume none. New issued cards go exclusively to Part 6.

Run tests, source/archive validation, original-byte checks and the active manifest verification before recording completion. Preserve unrelated pre-existing dirty work. Stage and publish only if separately instructed.

Baseline provenance is mandatory for certified admission: exact lane/league/endpoint/families/version, a pinned approved definition and code artifacts, approval strictly before cutoff, and matching distribution/holdout/shadow/pilot comparator. Hash joins verify retained bytes and declared metadata; they do not independently prove every declared input availability time or recompute every distribution. Review the original source field and baseline construction. The point-in-time feature filter likewise labels declared metadata and cannot confer live admission by itself.

## October 1 settlement readback

The dated all-log audit in Part 6 and `research/verification/settlement_2026-10-01/REPORT.md` controls the current diagnostic queue. P-518–P-522 have known ranked-row sporting outcomes but remain reserved and uncertified; issue-time, baseline, actual-start and source-independence work is still unresolved. The intake mini-log contains a manual claim for P-523 and an earlier contradictory empty-header/next-P-524 assertion. Its four goal rows are diagnostic W/W/L/L; its unknown corner line remains unissued. No canonical issue transaction exists, and P-523 remains unconsumed. The archive of original headers/forecasts is preserved. This changes no model qualification or future ranking rule.
