# New-system QA — 2026-07-16

## Verdict

The v3 documents materially correct the worst v2 design errors: they retire the top/bottom penalty economy, reject “lock” language, separate settlement from forecasts, require point-in-time data and chronological testing, make Poisson optional, and quarantine the legacy ledger. Those are real improvements.

They are **not yet an operational or statistically validated forecasting system**. They are governance drafts labelled canonical, with no active model cards, source registry v3, machine-readable schema, prediction/settlement stores, or executable acceptance suite. No quantitative sport/market model should be user-facing until the S0 items below are patched and passed. The user’s request for “no mistakes” cannot honestly be guaranteed; the defensible commitment is an auditable process with measured error and abstention.

## S0 — must fix before any quantitative forecast

### 1. Canonical authority conflicts with the actual workspace

- `combined_sports_doc_v3.md:7` says pre-audit files exist under the archive “only,” but active-looking copies remain at workspace root. In particular, `POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:5` still says `Status: ACTIVE modelling standard`, and `PREDICTION_RESULTS_LOG_v3.md:3` still instructs future research to review and update it.
- `combined_sports_doc_v3.md:240` refers to `SPORTS_SOURCE_REGISTRY_v3.md`, which does not exist. Only the stale v2 registry exists.
- No `MODEL_REGISTRY/`, model card, prediction store, settlement store, execution store, generated calibration report, or hypotheses register exists.

**Patch:** add one authority manifest naming the sole operative documents and explicit precedence; mark every legacy root file `ARCHIVED / NON-OPERATIVE` or move it; create the referenced v3 source registry. Change the v3 headers to distinguish `CANONICAL SPECIFICATION` from `OPERATIONAL STATUS: SUSPENDED — NO ACTIVE MODELS`. A document becoming canonical must not imply that any sport is validated.

### 2. Activation and promotion gates are too weak and partly contradictory

- The audit requires an untouched **prospective** period before reactivation (`methodology_audit.md:506,510-520`). The framework merely “recommends” a shadow window (`SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md:43`) and later uses the vague condition “shadow results are consistent” (`:177`).
- Promotion currently needs a point-estimate improvement while the interval merely excludes a “material deterioration” (`:171-179`). That can promote a chance improvement with inadequate power. “Material,” “protected segments,” “consistent,” and minimum effective sample size are undefined.
- The manual permits beating “at least one” baseline (`combined_sports_doc_v3.md:75-80`), allowing a deliberately weak comparator. The audit requires a declared naive baseline and, in price-enabled mode, a no-vig market comparison.

**Patch:** make prospective shadow validation mandatory. Each model card must preregister the test-event roster or time boundary, one primary metric, naive and applicable market baselines, the minimum practically relevant improvement, effective-N/precision requirement, interval or posterior decision rule, protected segments and guardrails, and a rule that a viewed test is spent. Any failed/inspected test requires a new later untouched period. Activation must be a machine-checkable status, not prose approval.

### 3. Candidate-selection bias cannot be audited with the proposed schema

- The audit requires `selection_mode`, a predeclared candidate universe or every inspected candidate, and a separate primary user question (`methodology_audit.md:120-126,380-390,512-515`). None appears in Stage A (`combined_sports_doc_v3.md:32-42`) or the prediction schema.
- The candidate table records only outcome alternatives attached to an already selected prediction (`SPORTS_DATA_DICTIONARY_v3.md:71-86`). It cannot reconstruct markets inspected and rejected, the selection algorithm, eligibility, or the primary requested output. Therefore the framework’s promise to evaluate the “complete selection pipeline” (`SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md:163`) is not implementable.

**Patch:** add `request_id`, `primary_question_id`, `selection_mode = USER_SUPPLIED | FIXED_UNIVERSE | MODEL_SELECTED`, `candidate_universe_version`, selection-policy version, and one immutable row for every inspected candidate including rejected/pass candidates. Store eligibility and rejection reason before settlement. Report the primary requested forecast separately from secondary claims.

### 4. Research/price mode and forecast state are conflated

- `combined_sports_doc_v3.md:38` treats `research-only`, `price/edge evaluation`, and `live update` as alternatives, but live/pregame state is orthogonal to whether prices are authorized.
- The dictionary stores only `PREGAME | LIVE` (`SPORTS_DATA_DICTIONARY_v3.md:35`) and loses the audit-required distinction between projected-lineup pregame and confirmed-lineup pregame. It has no controlled research-only/price-enabled mode.

**Patch:** store two independent fields: `analysis_mode = RESEARCH_ONLY | PRICE_ENABLED` and `forecast_state = PREGAME_PROJECTED | PREGAME_CONFIRMED | LIVE`, plus exact horizon/state bucket. Calibrate and report each state separately. `RESEARCH_ONLY` must hard-block edge, value, staking, yield and CLV fields.

### 5. PASS and `MODEL UNAVAILABLE` cannot be represented honestly

- The framework says no model card means `MODEL UNAVAILABLE` and a qualitative range or PASS (`SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md:20`). The dictionary nevertheless requires model/data/feature versions, raw and “calibrated” probabilities, a baseline and uncertainty for **every** prediction record, including PASS/WATCH (`SPORTS_DATA_DICTIONARY_v3.md:46-67`). The minimum output has the same problem (`combined_sports_doc_v3.md:212-227`).
- This pressures an implementation to invent dummy versions or probabilities and prevents complete abstention-rate measurement if PASS requests are simply omitted. A “qualitative research range” is also unsafe if it looks like an unvalidated numeric forecast; the audit calls for a non-probabilistic summary.

**Patch:** define a request/decision record that always exists. For `PASS`/`MODEL_UNAVAILABLE`, require `pass_reason` and missing prerequisites while making forecast/model fields null and prohibiting numeric probability language. Only a quantitative forecast record from an ACTIVE, in-scope model may contain probabilities. Define whether WATCH is a published probability, a data-refresh state, or a pass variant; currently it is ambiguous.

### 6. Snapshot identity and entity relationships are internally inconsistent

- The entity diagram has a separate `snapshot` entity (`SPORTS_DATA_DICTIONARY_v3.md:8-16`), but no snapshot schema exists.
- Live updates increment `snapshot_version` under a prediction (`:24-25,69`), while the audit says later updates create a new prediction ID (`methodology_audit.md:394-396`). `parent_prediction_id` cannot identify a parent composite key and may point ambiguously to itself. The manual calls both prediction ID and snapshot version immutable (`combined_sports_doc_v3.md:107`).

**Patch:** use an immutable `snapshot_id`/`prediction_id` per publication, a separate stable `forecast_series_id`, and `parent_snapshot_id` for lineage. Define event, market, source packet and snapshot entities, foreign keys, uniqueness and hash boundaries. Settlement must reference one immutable published snapshot, never an ambiguous series ID.

### 7. Price, no-vig and EV rules are not reproducible and are wrong for push markets

- `EV = p_model * d - 1` (`combined_sports_doc_v3.md:188-196`; `SPORTS_DATA_DICTIONARY_v3.md:59`) is valid only when the complement is a loss and there is no push/void mass. For a push-capable market, expected return is `p_win*(d-1) - p_loss` before commission; push/void returns zero profit.
- The dictionary stores one price but not the complete contemporaneous outcome-price set needed for de-vigging, nor bookmaker/exchange, quote ID, de-vig method, overround, commission, limits, expiry/staleness rule, break-even probability, or EV interval. Its single `edge` field may mean either model-minus-baseline or model-minus-market (`SPORTS_DATA_DICTIONARY_v3.md:58`), re-blending forecasting skill with betting value.
- The manual/framework allow yield and CLV with “complete prices” (`combined_sports_doc_v3.md:99,208`; framework `:164`), but the audit permits CLV/P&L only from an actual execution record. No execution entity exists.

**Patch:** add immutable market-snapshot/outcome-price tables and a separate execution table. Split `baseline_skill_delta`, `market_edge`, and `expected_return`. Store win/loss/push/void probabilities, break-even probability, de-vig method, commission and conservative EV interval. Hard-block stake, yield, P&L and CLV without a qualifying execution and closing snapshot. Put any staking policy in a separately authorized risk standard.

### 8. “Calibrated” and uncertainty claims can overstate validity

- `model_probability_calibrated` is mandatory while `calibration_method_version` is required only when it differs from raw (`SPORTS_DATA_DICTIONARY_v3.md:51-55`). An unchanged heuristic/raw number can therefore be labelled calibrated with no validation evidence.
- Bounds are optional and have no stored level, estimand or method. A predictive outcome interval, a confidence/credible interval for a probability, scenario ranges, and model disagreement are different objects but are collapsed into two fields and a note.
- The framework lists uncertainty sources (`SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md:108-123`) and says simulation artifacts are stored (`:135-141`), but the dictionary defines no uncertainty-component or simulation-run entity. The audit’s requirement to show parameter, input/scenario, model and Monte Carlo uncertainty is therefore untestable.

**Patch:** rename the operative field `decision_probability`; add `calibration_status`, calibration artifact/hash, calibration test period and out-of-sample diagnostics. Do not use “calibrated” unless the registered test supports it. For ISSUE, require typed uncertainty components with method, level, target and interval, plus scenario weights/sensitivity. Add a simulation-run schema for seed, generator/PRNG, draws, dependence, parameters, MCSE and convergence test.

### 9. An ISSUE is not required to join to an active, in-scope model

Canonical validation rule 6 requires only model/data/feature versions and a hash for ISSUE (`SPORTS_DATA_DICTIONARY_v3.md:147`). It does not require that the model card is ACTIVE, approved, within sport/competition/market/settlement/state/horizon scope, past its test/shadow gates, and using the matching artifacts. Data-quality grade B can also be read as permission to issue outside a confirmed-input model’s scope (`combined_sports_doc_v3.md:131-138`).

**Patch:** add a foreign-key/activation check covering exact scope and artifact hashes. Data-quality grade can only restrict an otherwise valid model; it can never override activation or scope. Model cards also need the production ISSUE/WATCH/PASS decision policy and selection threshold—not just the model-promotion threshold—to prevent analyst discretion from recreating cherry-picking.

## S1 — required to make evaluation and controls executable

### 10. Temporal leakage checks are described but not enforced relationally

The canonical rules do not require every source observation and feature `known_at <= data_cutoff_utc`, a production fetch before publication, source-packet membership, or a hash recomputation. LIVE state is free-form JSON and the only rule is “official live state at or before prediction” (`SPORTS_DATA_DICTIONARY_v3.md:142-150`), weaker than the audit’s exact clock/exposure hard gate.

**Patch:** implement relational tests over every feature/source join; distinguish real-time production acquisition from historical as-of reconstruction; validate published/known/fetched ordering and allowed access states; reject unresolved conflicts/stale decisive inputs. Give LIVE state a sport-specific typed schema with required clock/exposure and official observation ID.

### 11. Outcome reconciliation and proper-score conventions are underspecified

- `push_or_void_probability` is attached to each candidate (`SPORTS_DATA_DICTIONARY_v3.md:83`), so a binary over/under market can duplicate the same push mass. Use one row per mutually exclusive branch (`OVER`, `UNDER`, `PUSH`, `VOID`) instead.
- The probability-sum tolerance is merely “documented” (`:86`), and `[0,1]` permits unjustified exact 0/1 forecasts that make log loss infinite (`:145`).
- No canonical scoring specification defines Brier normalization for multiclass outcomes, probability clipping policy, push/void/ungradable treatment, event versus market weighting, or whether many markets from one event receive disproportionate weight. “Event/card” clustering in the manual (`combined_sports_doc_v3.md:90`) is also ambiguous; a card may cross events and the same event may appear on several cards.

**Patch:** publish a versioned scoring specification with fixed reconciliation tolerance, branch semantics, inclusion rules and fixtures with known expected scores. Preserve raw probabilities; disallow non-structural exact 0/1 or define a preregistered scoring safeguard. Cluster first by event and add time/team blocks where the model card shows residual dependence; never substitute card ID for event ID.

### 12. Stop rules and document rules have no executable acceptance tests

“Useful minimum sample,” “material calibration drift,” “non-critical,” “protected subgroup,” “current,” and “consistent” are not defined. No rule has the audit-requested stable rule ID, owner, superseded ID and executable test (`methodology_audit.md:302-307`). No regression/parser/schema test suite exists despite those tests being activation and stop conditions.

**Patch:** move repeated technical rules out of the manual into one authoritative ruleset and reference stable IDs from the other documents. Every hard gate needs machine-testable input, pass/fail output, severity, owner, effective/superseded dates and remediation. Model cards must instantiate drift windows, alert thresholds, minimum N, rollback and restart/shadow criteria.

### 13. Settlement alone cannot produce the promised audit outputs

The settlement schema records the result and grade but not a versioned evaluation/scoring run, error taxonomy, interval inclusion or selection-pipeline eligibility (`SPORTS_DATA_DICTIONARY_v3.md:88-107`). The audit calls for those outputs and for generated calibration reports, not hand-maintained claims (`methodology_audit.md:455-476,478-490`).

**Patch:** keep settlement factual and append-only, then create a reproducible evaluation table/report keyed by prediction snapshot, settlement version and scoring-code version. It must calculate proper scores, baseline deltas, interval coverage, candidate-selection coverage, and clustered uncertainty. Legacy rows must fail an explicit `eligible_for_v3_evaluation` test.

### 14. All-sport coverage is a scope map, not validation evidence

The sport tables correctly call their models candidates and tell unsupported sports to pass (`combined_sports_doc_v3.md:140-158`), but there are no validated annexes/cards or current source maps for any sport. The research basis is mostly general forecasting literature plus one soccer model; it does not establish production validity for the many named sports.

**Patch:** add a coverage registry with one row per sport/competition/market/state showing `UNSUPPORTED | DEVELOPMENT | SHADOW | ACTIVE`, model card, source map, test report, approval and expiry. Until evidence exists, every row should be UNSUPPORTED/DEVELOPMENT and the user-facing system must say so plainly.

## Minimum go-live acceptance suite

At minimum, automate tests that prove:

1. only the authority-manifest documents can be operative and every referenced dependency exists;
2. every request—including PASS—has a frozen record, while probabilities require an ACTIVE in-scope model;
3. every feature/source was knowable by cutoff and every published snapshot/hash is immutable;
4. candidate universe, selection mode, primary question and all inspected/rejected candidates are frozen before outcome;
5. pregame-projected, pregame-confirmed and comparable live-state forecasts are never pooled;
6. train/tune/calibrate/test/shadow periods and event IDs do not overlap, and a viewed test cannot be reused;
7. promotion meets the preregistered baseline, effect, uncertainty, effective-N, calibration/tail and subgroup gates;
8. outcome branches reconcile and known scoring fixtures reproduce Brier/log-loss/coverage exactly;
9. no-vig and EV recompute from the complete price snapshot, including push/void/commission, and execution claims fail closed without an execution;
10. uncertainty components, simulation convergence, settlement versioning, legacy exclusion, drift suspension and rollback all fail closed under seeded negative tests.

Until this suite exists and passes for a specific model card, the honest output is `MODEL UNAVAILABLE / PASS`, not a probability, confidence label, edge, or stake suggestion.
