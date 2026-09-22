# Next-time sports model development and operating playbook v1

Status: **working playbook; non-authorizing**  
Current operating state: **SUSPENDED — NO ACTIVE MODELS**

## 1. Purpose

This is the practical sequence for the next research request and the next model-development cycle. It is designed to prevent temporal leakage, retrospective selection, false calibration claims, incoherent markets, understated uncertainty, and accidental activation.

The objective is not to cover every sport quickly. The objective is to produce one narrow, reproducible forecast scope whose evidence is strong enough to survive an untouched chronological test and a later prospective shadow. Until that happens, the runtime should preserve the request and return a non-probabilistic PASS or WATCH.

## 2. Non-negotiable operating rules

1. **No ACTIVE row, no quantitative ISSUE.** A model architecture, source list, historical record, or plausible simulation is not a substitute.
2. **Resolve the target before research.** Event, competition, ruleset, market, line, settlement, state, horizon, and selection mode are part of the prediction target.
3. **Use only information knowable by the cutoff.** `known_at`, ingestion latency, parser state, and raw snapshot membership control eligibility.
4. **Freeze the whole opportunity set.** Preserve every candidate considered and every rejection reason before seeing outcomes.
5. **Keep evidence phases disjoint.** Train, tune, calibrate, untouched test, and prospective shadow are chronological and event-disjoint.
6. **Compare against a real baseline.** The challenger and baseline use the same eligible events, weights, target, and settlement rules.
7. **Evaluate distributions, not slogans.** Use proper scores, explicit calibration notions, sharpness, uncertainty, and coherent joint outcomes.
8. **Abstention has a denominator.** Report risk against coverage; do not advertise only the accuracy of a tiny selected subset.
9. **Every look spends evidence.** Register hypothesis families and mark a test manifest SPENT when first viewed.
10. **Price claims are a separate capability.** A research forecast does not imply value, profitability, a bet, or an executable opportunity.
11. **Failures are append-only facts.** Do not repair a bad snapshot in place. Add a correction, new version, or new cohort.
12. **Activation expires.** Monitoring, suspension, rollback, owner, reviewer, and expiry are approved with the model.

## 3. State vocabulary

### 3.1 Model lifecycle

| State | Meaning | Quantitative user output |
|---|---|---|
| `UNSUPPORTED` | No approved development path or required source/data capability | Never |
| `DEVELOPMENT` | Architecture or fitted candidate under construction; evidence incomplete | Never |
| `SHADOW` | Frozen model runs prospectively but is not user-facing | Never |
| `ACTIVE` | Exact scope has current approved evidence and an unexpired allowlist row | Only if every request-time gate passes |
| `SUSPENDED` | Previously usable version failed or expired | Never |

### 3.2 Request decision

| Decision | Meaning | Probability allowed? |
|---|---|---|
| `PASS` | A terminal hard gate failed; record the primary reason and missing prerequisites | No |
| `WATCH` | A time-bounded refresh may resolve an otherwise eligible request | No |
| `ISSUE` | Exact ACTIVE scope and all packet gates pass | Yes, with complete distribution and typed evidence |

`PASS` is a valid output, not a failed research session. It prevents an unsupported number from becoming future “evidence.”

## 4. Roles and separation of duties

One person may fill more than one role in a small project, but the artifact must still name the role and conflicts must be disclosed.

| Role | Primary responsibility | Must not silently do |
|---|---|---|
| Request owner | Defines the decision need and cost of abstention/error | Change the target after seeing results |
| Contract owner | Registers rules, market, state, and settlement definitions | Generalize one competition's rules to another |
| Data steward | Datasheet, source rights, timestamps, corrections, manifests | Backfill unavailable-at-cutoff values as if known |
| Model developer | Baseline, features, candidate model, reproducible fit | Inspect untouched outcomes while tuning |
| Evaluator | Runs frozen test and reports all registered outcomes | Remove inconvenient events post hoc |
| Operational owner | Runtime, monitoring, incident response, rollback | Override a failed gate manually |
| Approver/reviewer | Checks scope, evidence, limitations, expiry | Approve a version they cannot reproduce |

An untouched test or shadow intended as promotion evidence should have an evaluator who was not making post-view model choices on that cohort.

## 5. Artifact map

Every release should be traceable through exact identifiers and hashes.

| Artifact | Minimum purpose |
|---|---|
| Competition registry | Stable competition ID, jurisdiction, season/rules effective dates, status |
| Contract registry | Event/market/rules/settlement/state/horizon definition and effective dates |
| Registered source catalog | Fact-specific official/researched source starting points |
| Approved source map | Model-specific source IDs, parsers, fallbacks, latency, conflicts, required fact classes |
| Dataset datasheet | Provenance, target construction, known-time policy, coverage, missingness, corrections, license |
| Event manifest | Exact immutable event IDs and partition assignment |
| Feature specification | Definition, source lineage, unit, transformation, latency, missingness policy |
| Development plan | Hypothesis, baseline, model, periods, metrics, guardrails, multiplicity, stop rule |
| Experiment ledger | Test status, hypothesis family, preregistration, manifest and result hashes |
| Model card | Intended/excluded use, exact scope, artifacts, evidence, limitations, owner, expiry |
| Calibration artifact | Mapping or identity justification, fit/evaluation periods, diagnostics and uncertainty |
| Test report | Frozen primary result and every preregistered guardrail/segment |
| Shadow report | Prospective operational reproduction and incident log |
| Coverage row | Final exact operational allowlist |
| Decision packet | Immutable request, sources, universe, distribution, uncertainty, decision and gates |
| Journal record | Chained decision, settlement, evaluation, and corrections |
| Release bundle | Inputs, outputs, hashes, commands, tool versions, warnings, test results, reviewer |

Datasheets follow the accountability intent of [Datasheets for Datasets](https://doi.org/10.1145/3458723); model cards follow [Model Cards for Model Reporting](https://doi.org/10.1145/3287560.3287596). Neither is a box-ticking summary: each links to machine-verifiable evidence.

## 6. End-to-end development sequence

### Phase 0 — choose one narrow claim

Start with one competition, one market family, one forecast state, one horizon family, and one settlement convention. Prefer a target with:

- an authoritative event and settlement source;
- stable historical definitions;
- sufficient chronological sample size and event diversity;
- a transparent baseline;
- a feasible point-in-time data reconstruction;
- a clear operational cutoff;
- manageable dependence and source latency.

Do not begin with “all soccer,” “all player props,” or “all live markets.” A suitable first scope might be one league's pregame match result under one exact overtime/extra-time convention. The choice still requires a feasibility audit; this playbook does not recommend or activate that example.

**Phase 0 exit checklist**

- [ ] `hypothesis_family_id` created.
- [ ] Scope names one competition, market family, state, horizon, and settlement convention.
- [ ] Intended decision and cost of false ISSUE versus PASS documented.
- [ ] Target outcome is observable and can be settled authoritatively.
- [ ] Known high-risk transfers and excluded uses listed.
- [ ] Data/source feasibility assessed before model construction.

### Phase 1 — freeze the forecast contract

Register the contract before feature research. At minimum bind:

- event and competition identifiers;
- season and applicable ruleset version;
- event start and forecast cutoff rules;
- market and outcome state space;
- selection, line, unit, and rounding convention;
- regulation/overtime/extra-time/tiebreak treatment;
- abandonment, postponement, retirement, substitution, dead heat, push, and void behavior;
- pregame-projected, pregame-confirmed, or exact live state;
- live state schema, state bucket, and horizon bucket if applicable;
- candidate selection mode and policy version;
- settlement authority and correction process;
- contract effective and expiry times.

Use a truth table of edge cases. Run it against known historical fixtures without looking at model performance. A contract is RESOLVED only when the same raw official result deterministically produces the same target and settlement grade.

**Stop condition:** ambiguous or conflicting settlement rules produce `CONTRACT_UNRESOLVED`; no modeling begins for that target.

### Phase 2 — build the fact-specific source map

The registered source catalog is discovery and authority metadata. An approved source map must be specific to the model and bind each required fact class to an exact implementation.

For every source route or document, record:

- source ID, publisher, exact URL/route/document issue and authority tier;
- competition, season, fact classes, units, definitions, and coverage exclusions;
- access method, authentication, license/terms, caching and retention policy;
- parser name/version/code hash and schema fingerprint;
- `published_at`, `known_at`, `fetched_at`, applicable time, and latency allowance;
- raw payload/content hash and durable snapshot location;
- missingness, correction/revision, cancellation, and duplication behavior;
- freshness test, parser regression fixtures, and next retest date;
- ordered fallback IDs, authority downgrade, and conflict rule;
- owner and incident contact.

Test the source at the cadence and times it will be used. A parser that works on a final score page after the event is not evidence that pregame or live state was available at the forecast cutoff.

**Source-map acceptance checklist**

- [ ] Every required fact class has a primary source or an explicit unavailable state.
- [ ] Exact rules and settlement documents are effective for the target event.
- [ ] Parser fixtures include normal, missing, delayed, corrected, and schema-change cases.
- [ ] Timestamps distinguish publication, discovery/knowledge, fetch, and applicability.
- [ ] Raw payloads and parser outputs are both hashed.
- [ ] Fallback use is visible in the decision packet.
- [ ] Conflicting sources cannot be silently averaged or overwritten.
- [ ] Source staleness forces WATCH or PASS at the registered threshold.

### Phase 3 — create the dataset datasheet and immutable event manifest

The dataset is a versioned product, not an ad hoc table. The datasheet must state:

- who collected and maintains it;
- source-map version and collection interval;
- event population, inclusion/exclusion rules, and unit of analysis;
- target construction and settlement contract;
- feature definitions, units, transformations, and lineage;
- `known_at` construction, ingestion-latency assumptions, and cutoff simulation;
- coverage by time, competition, state, market, provider, venue, and key segments;
- missingness and correction patterns over time;
- duplicates, reschedules, multi-market rows, and event-cluster IDs;
- rule, roster, schedule, provider, and schema regime changes;
- legal/licensing and participant-integrity restrictions;
- quality tests, known limitations, retention, deprecation, and correction policy;
- immutable manifest hash and row/file hashes.

Each event has one stable `event_cluster_id`. All rows derived from the same event—including complementary outcomes and related markets—stay in the same partition and resampling cluster.

**Known-time invariant**

For every feature value used in snapshot `s`:

`observation.known_at_utc <= snapshot.data_cutoff_utc < event_start_utc`

For live models, replace the right-hand condition with the registered live-state timing rule and also validate clock, exposure, possession/serve/innings, and horizon. Backfilled official corrections may be used for target settlement but cannot be inserted into the historical feature snapshot as if known earlier.

### Phase 4 — preregister evidence partitions and decision rules

Create the development plan and experiment-ledger row before the untouched outcomes are viewed.

Use chronological, event-disjoint, half-open intervals:

1. **Train:** fit parameters and learned representations.
2. **Tune:** select architecture, features, regularization, decay, hyperparameters, and numerical settings.
3. **Calibrate:** fit the probability mapping or document an identity mapping using later data.
4. **Untouched test:** one frozen comparison against the preregistered baseline and guardrails.
5. **Prospective shadow:** later operational evidence collected by the frozen runtime.

Rolling-origin folds inside train/tune are encouraged for stability and regime analysis. Tashman's rolling-origin evaluation is the core time-series design reference ([Tashman, 2000](https://doi.org/10.1016/S0169-2070(00)00065-0)). Time-aware validation is necessary under drift ([Cerqueira et al., 2020](https://doi.org/10.1007/s10994-020-05910-7)); random event shuffling is not the default. If a cross-validation argument is used, state and test the dependence assumptions discussed by [Bergmeir, Hyndman & Koo](https://doi.org/10.1016/j.csda.2017.11.003).

Preregister:

- model, baseline, feature, source-map, contract, code, and configuration hashes;
- exact event manifest and period boundaries;
- primary estimand, metric, direction, practical-effect threshold, and comparison rule;
- equal-row or equal-event weighting and event clustering;
- calibration notions and diagnostics;
- coverage/risk policy and cost of abstention;
- tail, subgroup, source, latency, and operational guardrails;
- uncertainty method, resample count, seed/PRNG, and confidence level;
- hypothesis family and multiplicity method;
- robustness and sensitivity set;
- pass, fail, suspend, and inconclusive outcomes;
- independent evaluator and first-view procedure.

Do not make “significant at 0.05” the sole promotion rule. Require a useful effect size and uncertainty bound as well as nonfailure of safety and calibration guardrails.

### Phase 5 — establish baselines before challengers

Every target needs at least one transparent baseline that could be run at the same cutoff:

- climatology or season/competition rate with appropriate shrinkage;
- simple recency-adjusted rating;
- market consensus only when a point-in-time, executable, de-vigged market snapshot is legally and operationally available;
- a sport-native simple count/state model;
- persistence or official seeding/ranking when appropriate.

The baseline has the same contract, state space, source cutoff, missingness rule, and evaluation population as the candidate. Store the full baseline distribution in every eligible decision packet.

If a complex model cannot beat a simple transparent baseline on later untouched data, it does not promote because it “looks sophisticated.”

### Phase 6 — fit the sport-native model reproducibly

For every fit, preserve:

- code repository state and code hash;
- environment/runtime and library lock information;
- data, event-manifest, source-map, feature-spec, and contract hashes;
- model configuration and seed/PRNG;
- optimizer/sampler settings, convergence diagnostics, and numerical tolerances;
- fitted parameters/artifact hash;
- training logs, warnings, failed attempts, and resource limits;
- feature missingness and fallback behavior;
- developer identity, start/end time, and change ticket.

Fit only on registered train/tune data. If an untouched outcome is exposed accidentally, mark that manifest SPENT and create a later test period; do not rely on human memory to “ignore” it.

### Phase 7 — calibrate and assess sharpness

Probability claims require an explicit calibration object. Fit calibration only on the registered later calibration interval. Possible methods include logistic/Platt, beta, hierarchical, or adequately supported isotonic calibration. An identity mapping is allowed only with a documented out-of-sample justification; `raw_probability == decision_probability` is not itself evidence.

Report:

- raw and decision Brier/log loss on the untouched test;
- calibration-in-the-large/intercept and slope where applicable;
- reliability/CORP-style diagnostics with counts and uncertainty;
- calibration by preregistered competition/state/horizon/protected segments;
- distribution and entropy/concentration of forecast probabilities as sharpness evidence;
- discrimination only as a complement to calibration;
- comparison to baseline and simple recalibration alternatives;
- calibrator fit period, model hash, code hash, method/version, and artifact hash.

Proper scoring rules are the governing framework ([Gneiting & Raftery, 2007](https://doi.org/10.1198/016214506000001437)). Calibration must name its target and notion ([Vaicenavicius et al., 2019](https://proceedings.mlr.press/v89/vaicenavicius19a.html)), and binned reliability diagnostics have an unavoidable confidence-versus-resolution tradeoff ([Arrieta-Ibarra et al., 2022](https://www.jmlr.org/papers/v23/22-0658.html)). Prefer sharper forecasts only after adequate calibration ([Gneiting, Balabdaoui & Raftery, 2007](https://doi.org/10.1111/j.1467-9868.2007.00587.x)).

Do not print probability precision finer than the evidence supports. Simulation draw count does not determine display precision.

### Phase 8 — validate uncertainty and joint coherence

#### Uncertainty record

For each relevant component, store:

| Component | Typical method | Required evidence |
|---|---|---|
| Outcome/aleatoric | Predictive distribution | Full state space and outcome definition |
| Parameter | Posterior, bootstrap, asymptotic or ensemble | Method, assumptions, interval/quantiles, artifact |
| Input/availability | Scenario or measurement-error propagation | Scenario definitions, weights, cutoff-safe source |
| Structural | Registered model ensemble/sensitivity | Candidate set and weighting chosen before test |
| Calibration | Calibrator resampling/posterior/sensitivity | Calibration period and mapping versions |
| Regime/scenario | Preregistered stress cases | Trigger, probability/weight treatment, result |
| Monte Carlo | MCSE/effective sample/convergence | PRNG, seed, draws, autocorrelation if applicable |
| Source/definition | Downgrade, interval, or abstention rule | Source state, conflict and contract evidence |

Never add interval widths from these rows as if independent. A “total 95% interval” requires a registered joint propagation method and a clearly named target.

#### Joint coherence record

Coherence is an accuracy-relevant requirement under proper scoring, not merely presentational tidiness ([Predd et al., 2009](https://doi.org/10.1109/TIT.2009.2027573)). Markets that share primitive events reference one `joint_distribution_id`. Validate registered invariants such as:

- mutually exclusive and exhaustive outcome probabilities sum to one;
- `P(over x) + P(under x) + P(push at x) = 1` under the exact line convention;
- match winner and regulation result are connected through explicit overtime/extra-time branches;
- phase/period totals aggregate consistently to full-event totals under the simulated state process;
- team scores sum to the event total for every joint draw;
- handicap outcomes are deterministic functions of the joint score and line;
- player/count outcomes respect exposure, minutes/balls/possessions, roster, and team aggregates;
- conditional live distributions begin from the frozen official live state rather than a pregame restart.

Reject an unknown constraint name or an empty state space. Do not “repair” incoherence by normalizing only the displayed chosen side.

For multivariate distribution evaluation, use appropriate proper scores and declare their sensitivity. A variogram score can add dependence sensitivity ([Scheuerer & Hamill, 2015](https://doi.org/10.1175/MWR-D-14-00269.1)).

### Phase 9 — freeze the selection policy and risk/coverage rule

A selection policy maps a complete candidate universe to ISSUE/WATCH/PASS. It must be executable, versioned, and frozen before the untouched test.

The candidate-universe record contains:

- request and snapshot IDs;
- external universe-enumeration manifest and count;
- every candidate ID, target, line, contract, state, and availability status;
- model and baseline distributions where eligible;
- uncertainty, source, and price eligibility flags;
- selected/not-selected status and one controlled reason;
- primary candidate invariant;
- selection-policy version/hash and freeze time.

Evaluate the fixed policy with:

- `coverage = issued opportunities / all eligible opportunities`;
- risk/loss among issued opportunities at each threshold;
- area under the right-continuous risk-coverage curve;
- risk at preregistered coverage points and coverage at preregistered risk targets;
- PASS/WATCH reason frequencies;
- source and subgroup coverage disparity;
- complete-pipeline performance, not an oracle re-ranking after outcomes.

Selective prediction methodology is grounded in [El-Yaniv & Wiener](https://jmlr.org/papers/v11/el-yaniv10a.html) and [Geifman & El-Yaniv](https://papers.nips.cc/paper_files/paper/2017/hash/4a8423d5e91fda00bb7e46540e2b0cf1-Abstract.html). A finite-sample risk guarantee needs a matching procedure and assumptions, such as [conformal risk control](https://research.google/pubs/conformal-risk-control/); ordinary threshold tuning cannot borrow that guarantee.

### Phase 10 — run the untouched test once

Before access, verify that the manifest is `PLANNED_UNTOUCHED`, the preregistration timestamp precedes first view, and all artifact hashes match. Then atomically:

1. lock the exact code/environment and inputs;
2. mark the manifest SPENT at first access;
3. generate all predictions and gate decisions;
4. settle from the registered authority without changing predictions;
5. calculate the primary metric and every registered guardrail;
6. preserve warnings, exclusions, parse failures, and missing events;
7. generate a no-clobber report and hash it;
8. record the result in the experiment ledger.

Binary probability reports include Brier and log loss. Ordered/count/continuous targets add the preregistered proper distribution score and interval/tail metrics. Comparisons use paired model-minus-baseline loss on identical eligible rows, with event-clustered uncertainty and the preregistered row/event weighting.

Multiplicity must match the registered family. Holm controls strong family-wise error ([Holm, 1979](https://www.jstor.org/stable/4615733)); Benjamini-Hochberg is an option for a declared FDR objective ([Benjamini & Hochberg, 1995](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x)); strategy searches may require a data-snooping procedure such as White's reality check under its assumptions ([White, 2000](https://doi.org/10.1111/1468-0262.00152)). Sequential looks require a registered alpha-spending or always-valid design ([Lan & DeMets, 1983](https://doi.org/10.1093/biomet/70.3.659); [Howard et al., 2021](https://doi.org/10.1214/20-AOS1991)).

Possible outcomes are PASS, FAIL, or INCONCLUSIVE under the preregistered rule. An inconclusive result does not become a pass because the point estimate has the desired sign.

### Phase 11 — run a later prospective shadow

Freeze a new later event manifest and operate the actual request-time path prospectively:

- resolve requests before event cutoff;
- fetch and hash sources on the production schedule;
- freeze the entire candidate universe;
- run the exact model/calibrator/policy artifacts;
- create decision packets and record all PASS/WATCH outcomes;
- preserve latency, outage, correction, and operator-intervention incidents;
- settle and evaluate only later;
- prohibit tuning on shadow outcomes until the cohort is closed and marked SPENT.

Shadow promotion requires both empirical and operational success. A model that scores well but regularly uses stale lineups, misses candidates, violates latency, or cannot reproduce hashes does not promote.

### Phase 12 — activation review and release

Activation is one reviewed change containing the model card, exact coverage row, manifest/release status, approval, expiry, monitoring plan, and rollback procedure.

**Activation checklist**

- [ ] Contract, source map, dataset, features, model, calibrator, policy, code, and environment hashes reconcile.
- [ ] Model and coverage scope match competition, market, settlement, state, horizon, and analysis mode exactly.
- [ ] Untouched test and later prospective shadow satisfy preregistered primary and guardrail rules.
- [ ] Test manifests are SPENT and cannot be reused.
- [ ] Calibration notion and uncertainty are supported without over-precision.
- [ ] Joint-market constraints and negative fixtures pass.
- [ ] Candidate-universe completeness and risk/coverage are acceptable.
- [ ] No unresolved incident or data-license/definition issue exists.
- [ ] Price mode remains disabled unless its separate evidence is complete.
- [ ] Owner, independent reviewer, approver, effective time, expiry, alert/suspend thresholds, and rollback version are recorded.
- [ ] Release bundle is no-clobber, complete, hashed, and reproducible.
- [ ] Suspension-mode validation passes before the change; activation-candidate validation passes with the proposed row; post-change validation passes again.

Do not activate a broader scope than the test. `ALL`, `OTHER`, or a sport-family wildcard is not justified by one competition.

## 7. Request-time runbook

### 7.1 Before doing any sport research

1. Preserve the user's raw request verbatim.
2. Assign request, primary-question, forecast-series, event, and snapshot identifiers.
3. Resolve competition, event start, market, line, ruleset, settlement, analysis mode, forecast state, state/horizon, and selection mode.
4. Check the exact contract and coverage rows before searching for form, lineups, news, or prices.
5. If the contract is unresolved, freeze PASS with `GATE-CONTRACT-001` and the missing fields.
6. If no exact unexpired ACTIVE model/coverage pair exists, freeze PASS with `GATE-MODEL-001`.

This ordering prevents research effort from creating pressure to issue an unsupported forecast.

### 7.2 When no ACTIVE model exists

Use the decision-packet workflow to record the refusal. Never fill probability fields with zero, 0.5, a historical percentage, or a placeholder.

An operator can copy the request template to a uniquely named input file, replace all placeholders, and run:

```powershell
node scripts/sportsctl.mjs new-request --input <filled-request.json> --output <unique-decision-packet.json>
node scripts/sportsctl.mjs validate-packet --input <unique-decision-packet.json>
node scripts/sportsctl.mjs record --input <unique-decision-packet.json>
node scripts/sportsctl.mjs verify-store
```

Do not edit the shared template in place and do not overwrite a previous packet. If validation fails, preserve the error output in the run bundle and correct the input as a new file.

### 7.3 When an exact ACTIVE scope eventually exists

The initial request packet should remain WATCH until the complete point-in-time source packet, candidate universe, model distribution, calibration artifact, uncertainty, coherence, and policy outputs are frozen. ISSUE is allowed only if the packet validator passes every applicable hard gate.

**ISSUE packet checklist**

- [ ] Request and decision IDs/foreign keys agree.
- [ ] Request, cutoff, freeze, source, live-state, and event times obey the exact mode rules.
- [ ] Contract, model, coverage, source-map, test, shadow, and approval records are ACTIVE/unexpired and hash-matched.
- [ ] Candidate universe is externally enumerated, complete, frozen before selection, and linked to the snapshot.
- [ ] Source observations are registered, timely, hashed, parsed, conflict-resolved, and packet members.
- [ ] Model, data, feature, code, calibrator, baseline, policy, and joint-distribution identifiers/hashes are present.
- [ ] Full raw, decision, and baseline outcome branches are unique, controlled, finite, in `[0,1]`, and sum to one.
- [ ] Selected candidate and primary question agree; nonselected candidates have controlled reasons.
- [ ] Calibration evidence applies to the exact target/scope and is not expired.
- [ ] Typed uncertainty is complete and the robustness rule supports issuance.
- [ ] Every registered joint constraint is evaluated on a nonempty state space.
- [ ] Research-only mode contains no price, value, edge, execution, or staking claim.
- [ ] Price-enabled mode passes its separate price gate; otherwise price fields stay null and the request fails closed for price use.
- [ ] Snapshot hash is recomputed after all fields are final.
- [ ] Journal and independent head/checkpoint state verify before and after append.

### 7.4 WATCH behavior

WATCH must have a specific reason, expected source/change, expiry, and maximum refresh count. Examples include waiting for an official lineup or a brief source outage where the exact ACTIVE model permits confirmed-input operation. On expiry, freeze a new PASS snapshot; do not leave the request indefinitely pending.

## 8. Settlement and evaluation runbook

Settlement is factual and separate from evaluation.

### Settlement

- reference an existing prior prediction/snapshot;
- use a unique settlement ID with monotonically increasing versions for corrections;
- retain the exact contract and outcome state IDs;
- record official event status, result values/units, source ID/route, published/fetched times, raw hash, and correction reason;
- require FINAL outcomes to have a nonpending grade and authoritative evidence;
- use `UNDER_REVIEW`, `PENDING`, or a terminal void/ungradable state consistently;
- never change the prediction, target, or contract during a settlement correction.

### Evaluation

- reference the exact prediction, settlement version, scoring-spec version, and scoring-code hash;
- derive scores from the stored full distribution and selected outcome;
- exclude VOID/UNGRADABLE according to the registered scoring rule; do not count them as correct;
- preserve eligibility, exclusion reason, baseline loss, paired delta, interval inclusion, selection coverage, and event cluster;
- enforce one natural-key evaluation per prediction/settlement/scoring version;
- generate aggregates from the journal; never hand-edit KPI totals.

The evaluation report must separate research-only forecast quality from price/execution performance. Hit rate without odds is not profitability; ROI without actual eligible stakes and fills is not realized performance.

## 9. Monitoring and suspension runbook

Monitoring implements the lifecycle approach in the [NIST AI Risk Management Framework](https://doi.org/10.6028/NIST.AI.100-1) and [NIST AI 800-4](https://doi.org/10.6028/NIST.AI.800-4).

### Per request/event

- contract and scope match;
- source freshness, conflicts, parser/schema fingerprint, and missingness;
- feature bounds and cutoff timing;
- distribution sum/range and joint constraints;
- latency and runtime version/hash;
- decision, pass reason, and candidate coverage;
- journal/head verification.

### Rolling operational window

- volume and ISSUE/WATCH/PASS rates;
- reason-specific abstention and source failure;
- proper score and paired baseline loss;
- calibration and sharpness with N/cluster count;
- risk/coverage at frozen thresholds;
- segment, state/horizon, tail, and missingness guardrails;
- drift metrics and feature/source regime changes;
- settlement corrections and unresolved-event age;
- price/execution/CLV/P&L only where separately active.

### Longer evidence window

- full model-card scope and protected segments;
- uncertainty coverage and sensitivity stability;
- concentration by team/player/venue/provider/event cluster;
- model/baseline degradation and policy coverage changes;
- rules, schedule, roster, provider, and competition regime review;
- expiry and revalidation decision.

Ordinary rolling confidence intervals are not safe for unlimited repeated peeking. If monitoring makes sequential statistical guarantees, use a preregistered confidence-sequence/e-process or alpha-spending design ([Howard et al., 2021](https://doi.org/10.1214/20-AOS1991); [Lan & DeMets, 1983](https://doi.org/10.1093/biomet/70.3.659)). Otherwise label the display diagnostic and apply fixed operational thresholds without overstating inference.

### Immediate suspension triggers

- temporal leakage or post-cutoff feature use;
- wrong event, competition, market, line, rules, state, horizon, or settlement contract;
- model/data/feature/code/calibrator/source-map hash mismatch;
- unknown or stale decisive source, silent fallback, parser/schema failure, or invalid live state;
- probability range/sum failure or cross-market incoherence;
- incomplete candidate universe or changed selection policy;
- reproducibility/regression test failure;
- unresolved settlement/correction that can alter evaluation integrity;
- breached preregistered critical drift, calibration, risk, tail, or protected-segment threshold;
- expired approval, data rights, source route, test report, or coverage row;
- incident indicating operator override or journal/head inconsistency.

Suspension is fail-closed and immediate. Resume only with a new version/change ticket, repaired artifacts, later untouched evidence, later shadow, approval, new expiry, and an append-only incident/correction trail.

## 10. Sport-specific development and source strategy

The following table is a research plan, not evidence that a model exists. Each row must be narrowed to an exact competition and market before development.

| Sport family | Primitive model direction | Critical point-in-time sources/state | Main transfer and integrity risks |
|---|---|---|---|
| Soccer | Hierarchical attack/defence joint score; low-score dependence; separate corners/cards/shots exposure models | Exact competition rules, official event/lineup/result; licensed definition-stable xG/shot/event feed; venue/weather | Regulation vs ET/penalties, tournament state, provider xG definitions, projected lineups, cross-league pooling |
| Baseball | Plate-appearance/run-state or hierarchical team score; starter/bullpen/park/weather states | Official schedule/game report, confirmed starter/lineup, roster/transactions, park and weather | MLB/NPB/KBO rules and data definitions, pitcher changes, F5 vs full game, extras/runline settlement |
| Basketball | Possession distribution with lineup/minutes/usage and late-foul/OT branches | Official schedule/gamebook, confirmed availability/lineup, rules, tracking/box definition source | NBA/WNBA/FIBA/Summer League pace/rules, late scratch, garbage time, quarter/half linkage |
| Cricket | Ball/over/innings state with wickets, resources, batting order and weather/venue regimes | Exact ICC/league playing conditions, official scorecard/toss/XI, weather and interruptions | Format transfer, DLS/interruptions, innings/phase contracts, lineup/toss timing, youth/women's pooling |
| Australian football | Joint scoring-shot opportunity and goal/behind conversion with venue/wind | Official fixture/team/result, exact laws/competition rules, venue dimensions/weather | AFL/AFLW transfer, roof/wind, late teams, blowout pace, margin/line/total coherence |
| Ice hockey | Regulation joint goals from 5v5 chances, special teams and goalie state; explicit OT/SO branch | Official Game Centre, confirmed goalie/lines, roster, rules, event report | Regulation vs winner, goalie uncertainty, empty-net tail, NHL/IIHF rules and rink/event differences |
| American football | Drive/play scoring-state model with possession, field position and clock | Official schedule/gamebook, active/inactive lists, weather, exact rulebook | NFL/college transfer, overtime rules, kneel/garbage states, quarter/half/full coherence |
| Rugby league | Possession/set/field-position score process or hierarchical team score | Official draw/team lists/match centre, competition rules, venue/weather | NRL/NRLW transfer, announced vs actual 17, sin-bin/send-off state, Golden Point settlement |
| Rugby union | Territory/possession/set-piece scoring process with card state | World Rugby plus exact competition regulations, official teams/match sheet, weather | Competition law variations, cards, penalty/try mix, extra-time/knockout rules |
| Tennis | Point-on-serve Markov/hierarchical player-surface model with retirement branch | Exact ATP/WTA/tournament rules, official draw/order/result, entry/withdrawal and surface | Retirement/walkover settlement, best-of format, surface/ball/altitude, doubles vs singles |
| Volleyball | Rally/side-out Markov model with rotation and best-of format | FIVB/exact event rules, official competition/result/roster and live set state | Indoor/beach transfer, event variations, rotation/roster data, set/point/full-match coherence |
| Golf | Hole-level score distribution with course, player, tee-wave weather and cut/withdrawal states | Official field/tee time/leaderboard, tournament rules, course and government weather | Cut/dead heat/withdrawal contracts, wave/weather, course transfer, placement dependence |
| Motorsport | Survival/reliability plus pace/rank joint race model | Exact FIA/championship regulations and entry, official event classifications, grid/penalty/weather state | Series/rule transfer, retirements, grid penalties, safety car/red flag, correlated team reliability |
| Combat | Competing-risk hazard for finish method/time plus decision/judging branch | Event commission rules/result, official participant/card data, weigh-in and bout changes | Jurisdiction/rules, late opponent change, small N, judging variance, method/duration conditioning |

Use the machine registered-source catalog as the initial route inventory. For volleyball, motorsport, and combat, current official starting points include FIVB competition/rules documents, FIA regulations/event-entry documents, and commission/UFC result material. Those sources still need exact source maps, parser/latency tests, cutoff-safe archives, and licensing review.

## 11. Price-enabled capability is a separate project

Do not derive a betting recommendation from a research-only probability. Before `PRICE_ENABLED` can activate, implement and validate:

- operator/book/exchange identity and jurisdiction;
- exact market/selection/line and settlement equivalence to the model target;
- quote timestamp, source, raw hash, odds format, currency, limit and availability;
- overround/vig removal method and complete market sides;
- price staleness/latency and line-movement policy;
- expected-value calculation with probability uncertainty and fees/commission;
- stake policy, bankroll version, caps, responsible-use constraints, and correlation limits;
- order, acceptance/rejection, fill, partial fill, cancellation, and actual average price;
- closing-price observation and comparable-market definition;
- realized settlement, void/correction, P&L, exposure, CLV, and audit reconciliation;
- separate untouched/shadow validation of the price and execution path.

Until this exists, price fields stay null and the system makes no value, edge, stake, ROI, yield, CLV, or profitability claim.

## 12. Multiplicity and evidence-ledger checklist

Before any test result is inspected:

- [ ] Unique nonblank `experiment_id` and `hypothesis_family_id`.
- [ ] Exact model/version/config, data, code, event-manifest, source-map, contract, policy, and preregistration hashes.
- [ ] `preregistered_at_utc` precedes access to outcomes.
- [ ] Status is `PLANNED_UNTOUCHED` with no result fields.
- [ ] Family enumerates all variants, markets, leagues, features, thresholds, and metrics that could win selection.
- [ ] Multiplicity objective and method are named, including alpha/FDR and any sequential looks.
- [ ] Primary metric and practical-effect threshold are fixed.
- [ ] First view atomically changes status to `SPENT` and records evaluator/time.
- [ ] SPENT rows contain result/report hashes and cannot be cloned as untouched.
- [ ] Invalidated rows retain reason and lineage; deletion is prohibited.

Reusable holdout techniques can reduce some adaptive-analysis risk, but they do not justify unlimited informal reuse of a test set; if used, implement the actual privacy/stability mechanism and its budget rather than borrowing the label ([Dwork et al., 2015](https://doi.org/10.1126/science.aaa9375)).

## 13. Test and release discipline

### 13.1 Minimum negative-test families

Each gate needs a known-valid fixture and one-field mutations that prove failure for:

- missing, extra, mistyped, nonfinite, duplicate, malformed timestamp, and placeholder fields;
- request/snapshot/contract/universe/source/model foreign-key mismatch;
- source or feature `known_at` after cutoff and fetch after freeze;
- wrong competition, market, state, horizon, settlement, analysis mode, model version, or artifact hash;
- expired/revoked model, coverage, source map, test, shadow, approval, or contract;
- duplicate/missing outcome branches and sums outside tolerance;
- unknown/failed/empty joint constraints;
- missing uncertainty type/evidence or unsupported robustness result;
- incomplete universe, selection-policy mismatch, or primary/selected inconsistency;
- missing preregistration, reused SPENT manifest, overlap across time partitions, or cross-event leakage;
- stale price, incomplete market, target mismatch, absent quote hash, or no executable status;
- settlement correction that changes prediction/target, illegal status/grade combinations, duplicate versions, or unknown source;
- scoring a VOID/UNGRADABLE outcome, wrong scoring code/spec, or duplicate natural-key evaluation;
- journal chain, anchor, sequence, hash, duplicate ID, crash-window, and concurrency failures.

The traceability report maps every acceptance rule and negative test to its test name, implementation location, last result, runtime version, and release artifact. “All tests” is prohibited unless that matrix is complete.

### 13.2 Audit-script regression fixtures

Include fixtures for the prior retrospective defects:

- exact probability-bin boundaries represented with decimal-safe rules;
- nonoverlapping, exhaustive calibration intervals;
- duplicate/complement classification separated from logical contradiction;
- empty outputs that still contain schemas/headers;
- malformed and mixed-schema Markdown tables surfaced as errors;
- CSV/workbook population differences named and reconciled;
- every input named by relative identifier and SHA-256, never only a local absolute path;
- unique no-clobber output directory and run ID;
- complete output manifest, tool/runtime versions, command line, warnings, and parser failures.

### 13.3 Final verification sequence

Run these only after the implementation is frozen:

```powershell
npm test
npm run validate
npm run verify-store
```

Capture stdout, stderr, exit codes, Node and PowerShell versions, current-time assumptions, every operative artifact hash, journal head/count, and any network/source checks in a dated no-clobber release bundle. This playbook does not assert the result of those commands; the release evidence must.

## 14. Post-event retrospective loop

After a cohort closes:

1. Verify journal/head and settle from the registered authority.
2. Append corrections; never rewrite original predictions or settlements.
3. Generate evaluation from stored distributions and the exact scoring code.
4. Report the full request population, coverage, proper scores, baseline deltas, calibration, sharpness, uncertainty behavior, source failures, and operational incidents.
5. Cluster by event and disclose cluster count/concentration.
6. Separate preregistered primary/guardrail results from exploratory diagnostics.
7. Mark every viewed manifest SPENT.
8. Record root-cause categories: contract, source, cutoff, data, model, calibration, coherence, uncertainty, selection, price, settlement, runtime, or governance.
9. Turn exploratory findings into a future hypothesis family and later data; never patch them into the just-evaluated cohort.
10. Decide continue, narrow, refit as a new version, suspend, or retire.

Retrospection should answer “what decision process failed?” rather than inventing one narrative lesson for each loss. A well-calibrated 80% forecast sometimes loses; an individual loss is not proof of bad probability. Repeated proper-score, calibration, coverage, or operational failure is evidence.

## 15. Error-prevention checklist for every next-time session

Before issuing any answer, ask:

- [ ] Am I about to infer a current probability from a historical hit rate?
- [ ] Is the target contract exact, including settlement and state?
- [ ] Does an exact ACTIVE/unexpired coverage row exist right now?
- [ ] Are all decisive observations proven known by the cutoff?
- [ ] Did I freeze all candidates before selecting one?
- [ ] Are model, baseline, calibration, source, uncertainty, and policy artifacts exact and hash-matched?
- [ ] Are all outcome branches present and jointly coherent?
- [ ] Does the reported precision reflect total evidence, not simulation draws?
- [ ] Is abstention coverage visible?
- [ ] Is this cohort untouched, or has it already been viewed/spent?
- [ ] Am I mixing research forecast quality with price or execution claims?
- [ ] Will the final packet and later settlement remain reproducible without my memory?

If any answer is “no” or “unknown,” stop at the corresponding gate and record PASS/WATCH.

## 16. Honest user-facing language

### No contract

> I cannot define a trustworthy forecast target yet because the event/market/rules/settlement contract is incomplete. I recorded the request without a probability and listed the missing fields.

### No active model

> There is no ACTIVE model for this exact competition, market, state, and horizon. I recorded a non-probabilistic PASS. The available development card is a design only and supplies no current probability.

### Waiting for a permitted update

> The exact scope is eligible, but a registered decisive input is not yet confirmed. I recorded WATCH with the source needed and an expiry; no probability has been issued.

### Research-only ISSUE, if the system is eventually activated

> This is a calibrated research forecast from the named ACTIVE model and frozen evidence packet. It is not a bet or value claim; no price or execution conclusion is included.

Avoid “safe,” “lock,” “guaranteed,” “value,” “high confidence,” or “calibrated” unless the exact registered evidence supports the precise term.

## 17. Governance and change control

Use the GOVERN/MAP/MEASURE/MANAGE structure of the [NIST AI RMF](https://doi.org/10.6028/NIST.AI.100-1):

- **GOVERN:** owners, reviewers, approvals, conflicts, incident policy, expiry, rights, audit trail.
- **MAP:** intended decision, target, stakeholders, harms, sport/competition context, source and transfer limits.
- **MEASURE:** chronological evaluation, proper scores, calibration, sharpness, uncertainty, coherence, risk/coverage, source/runtime tests.
- **MANAGE:** promotion, monitoring, thresholds, suspension, correction, rollback, retirement, and new-version evidence.

Any change to target, source definition, feature logic, model, calibrator, selection policy, contract, code dependency, or joint constraint creates a new artifact version. Material changes require a new later untouched test and shadow. A documentation-only correction must be labeled as such and may not alter frozen evidence.

## 18. Completion rule

The framework is ready for a next request now because it can preserve the request and refuse unsupported issuance. It is **not** ready to publish a quantitative sports forecast until one exact scope completes every development, test, shadow, approval, and runtime gate in this playbook.

The next milestone should therefore be small and falsifiable: choose one exact scope, prove the source-time reconstruction, freeze a baseline and preregistered plan, and earn a later untouched result. Breadth comes only after repeated independent scope-level evidence.
