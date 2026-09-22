# Sports research rebuild retrospective — 2026-07-16

Status: **research retrospective; non-authorizing**  
Operational conclusion at the time of writing: **SUSPENDED — NO ACTIVE MODELS**

This document records what the legacy evidence can and cannot establish, what the rebuild actually implements, what still has to be proved, and how the next development cycle should avoid repeating the same errors. It is intentionally conservative. It does not activate a model, validate a sport, certify a probability, or turn a historical result into prospective evidence.

## 1. Executive conclusion

The workspace contains useful research, failure evidence, model architecture ideas, source catalogs, and a new fail-closed runtime foundation. It does **not** contain an ACTIVE fitted model or the end-to-end activation evidence needed to publish a current quantitative forecast.

The legacy headline record cannot be treated as a verified hit rate, calibration result, or profitability result. The newest inspected structured workbook has 449 non-template rows and a gross 253-190-2 record, or 57.11% over 443 win/loss decisions. That apparent result is not prospectively auditable because the records mix forecast states, the creation-time evidence is incomplete, exact complementary outcomes are heavily duplicated, some rows were mutable after settlement, and executable prices, stakes, and fills are absent. The older CSV has 437 non-template rows, not 449, so even the source population depends on which artifact is chosen.

The correct current output is therefore a frozen non-probabilistic PASS, usually `CONTRACT_UNRESOLVED` or `MODEL_UNAVAILABLE`, with the failed gate and missing prerequisites recorded. It would be a mistake to produce a number merely because a model architecture, simulation function, source URL, or historical percentage exists.

## 2. What the evidence actually says

### 2.1 Reconciled legacy facts

The July 2026 audit established the following facts:

- `SPORTS_CALIBRATION_LEDGER_v2.csv` contains 437 non-template records; the latest inspected settled workbook contains 449.
- The latest workbook's gross settled record is 253 wins, 190 losses, and 2 pushes, plus non-decision statuses. This is a descriptive count, not a verified prospective KPI.
- In the CSV, 300 of 437 rows (68.6%) are exact complementary selections, spread across 75 of 102 card IDs. Counting both sides of one partition can manufacture an apparent success opportunity and destroys the interpretation of an ordinary independent pick record.
- Phase and innings totals were frequently entered as complementary over/under pairs. Their combined behavior was approximately coin-flip-like; presenting both branches as separate selections hid the lack of useful ranking.
- Forecasts, live updates, research notes, and post-settlement information were not cleanly separated by immutable timestamps and versions.
- Prices, bookmaker terms, stake decisions, executions, void rules, and closing prices were not preserved in a way that supports ROI, yield, CLV, or profitability claims.
- Ten legacy probability-bucket labels disagreed with their numeric values, showing that even descriptive bucket summaries need machine validation.
- Feature and source coverage varied over time and was materially incomplete. Missingness was not random, so simple before/after process comparisons are confounded.
- Competition taxonomy was too broad. For example, different soccer competitions and materially different basketball environments were pooled despite different rules, data quality, roster stability, and generating processes.

These facts support a diagnosis of process failure and a redesign. They do not support reverse-engineering a trustworthy probability from the apparent 57.1% record.

### 2.2 Claims that remain prohibited

| Claim | Why it is not established | What would establish it |
|---|---|---|
| “The system wins 57.1%” | Duplicated complements, mutable evidence, mixed modes and unresolved population | Immutable forward cohort, one declared opportunity unit, complete selection ledger, event-clustered uncertainty |
| “The probabilities are calibrated” | Creation-time probability and calibrator evidence are not independently locked | Later disjoint calibration fit, untouched evaluation, declared calibration notion, reliability uncertainty and proper scores |
| “The model beats a baseline” | No frozen same-row baseline comparison for an eligible forward cohort | Preregistered baseline, identical eligible rows/weights, paired loss deltas with event clustering |
| “The system is profitable” | No executable price, stake, fill, fee, limit, void or closing-line record | Separate price/execution ledger and realized settlement under the exact contract |
| “All listed sports are covered” | Architecture and source catalogs are not fitted or approved models | Exact ACTIVE model and coverage rows for each competition/market/state/horizon |
| “Simulation makes the result precise” | More draws reduce Monte Carlo error only; they do not repair model, parameter, input or calibration error | Validated predictive model plus separately reported uncertainty components |

## 3. Root causes

### 3.1 A prediction was treated as prose instead of an immutable event

The legacy workflow mixed analysis, recommendation, update, and settlement in mutable documents. That made it impossible to prove what the system knew, what it predicted, and which version existed before the event. A reliable system needs a frozen request, frozen candidate universe, point-in-time source packet, model artifact identifiers, a decision snapshot, and a later separate settlement and evaluation.

### 3.2 The target contract was under-specified

“Winner,” “total,” “phase,” and “live” are not enough. The contract must bind the event identity, competition and ruleset, market definition, line, overtime or extra-time treatment, abandonment and retirement rules, forecast state, live-state bucket, horizon, and settlement convention. A probability for regulation winner is not interchangeable with a probability for winner including overtime; a cricket innings total is not a phase total; a tennis retirement convention can change the target itself.

### 3.3 Information timing was described, not enforced

A source being reputable does not make a feature cutoff-safe. Every decisive observation needs `published_at`, `known_at`, `fetched_at`, applicability time, raw content hash, parser version, and membership in the frozen source packet. Feature logic must use what was actually knowable at the decision cutoff, including publication and ingestion latency. This directly addresses the temporal leakage failure modes cataloged by Kapoor and Narayanan in their cross-field review of leakage and reproducibility ([Patterns, 2023](https://doi.org/10.1016/j.patter.2023.100804)).

### 3.4 Selection effects were ignored

Evaluating only the attractive outcomes that survived research is not the same as evaluating a fixed forecast population. Complementary entries, changing card sizes, manual “best pick” selection, and retrospective exclusions alter the denominator. The complete candidate universe and every rejection reason have to be frozen before selection. Evaluation then reports both predictive loss and risk as a function of coverage.

### 3.5 Model scope was broader than the evidence

Player props, phase markets, live forecasts, unfamiliar leagues, and different competition rules require separate exposure, availability, definition, and calibration evidence. A sport family label does not authorize transfer. The rebuild's model registry correctly leaves all architecture cards in DEVELOPMENT; a card is a design hypothesis, not an empirical result.

### 3.6 Controls existed mainly in prose

Earlier specifications named good gates but did not provide a complete executable store, contract registry, source map, schema validation, settlement lineage, or negative test suite. A static document check could prove that required words existed while proving nothing about a production packet. One earlier validator also assumed that zero ACTIVE rows was permanently correct, which contradicted the stated future activation process. Safe suspension and safe activation must be two explicit release modes, each with machine-checkable conditions.

### 3.7 Audit tooling also needed audit controls

Independent review found defects in the earlier retrospective analysis tooling: hard-coded input/output locations, incomplete input hashing and tool-version capture, an exact floating-point boundary that changed a probability-bin count, overlapping calibration-bin boundaries, an empty duplicate report without a header, mixed Markdown table schemas that were not surfaced as parse failures, and complementary `U/U` records labeled as contradictions when they were a duplication problem. Only part of the evidence bundle was covered by the old integrity manifest, and later root-file changes made that manifest stale.

Those are not cosmetic concerns. A retrospective script can create false confidence just as a forecast model can. Future audit runs need immutable input manifests, deterministic/no-clobber output directories, explicit parse-failure reports, boundary fixtures, and full artifact hashing. This retrospective does not assert that every historical audit script has been repaired.

## 4. What the rebuild has implemented

The workspace now contains executable foundations in addition to prose specifications:

- controlled vocabularies and machine-readable registries;
- an exact-scope coverage lookup that currently finds no ACTIVE model;
- a decision-packet builder that fails closed when a request, contract, mode, or model is unavailable;
- strict canonical JSON and SHA-256 hashing utilities intended to make snapshots reproducible;
- a packet validator with named gates and a structured gate-failure report;
- an append-only JSONL decision/settlement/evaluation journal with chained hashes and a local head anchor;
- scoring primitives for proper probability scores and development utilities for chronological partitions, risk/coverage, clustered comparison, and multiplicity bookkeeping;
- templates for requests, settlements, evaluations, development plans, and dataset datasheets;
- a Node test harness and command-line workflow.

These are important controls, but they must be described accurately:

1. Code presence is not the same as independent verification of every acceptance rule.
2. A hash chain with a local anchor is tamper-evident only relative to that anchor. It is not an immutable external ledger; deletion or coordinated replacement of both local files requires an independently retained head/count to detect.
3. A registered source URL is not an approved production source map. Parser behavior, definition, license, latency, coverage, conflicts, and cutoff-safe snapshots remain model-specific evidence.
4. Development model rows are not fitted artifacts. They have no learned parameters, calibrator, untouched test, prospective shadow, approval, or expiry evidence.
5. Header-only contract, source-map, test-evaluation, or experiment ledgers satisfy no activation gate.
6. The runtime is designed to make unsupported issuance difficult. It does not make any current probability correct.

No test count or “all tests pass” claim is made in this retrospective; verification output belongs in a dated, hashed release bundle generated by the final run.

## 5. Activation proof that is still missing

At least the following evidence must exist for one exact scope before the first ACTIVE row can be justified:

- a resolved event/market/rules/settlement contract with effective dates;
- a competition registry row and exact sport/competition/market/state/horizon scope;
- a dataset datasheet, immutable event manifest, schema/version history, source licenses and deletion/correction policy;
- an approved source map that binds every required fact class to source IDs, parser versions, latency rules, fallbacks, conflict resolution, and raw snapshot hashes;
- feature definitions with lineage and an enforceable `known_at <= cutoff` check;
- a transparent sport-native baseline;
- a fitted model artifact, exact code/config/data/feature hashes, deterministic seed/PRNG where relevant, and reproducible environment metadata;
- preregistered training, tuning, calibration, untouched-test, and prospective-shadow periods, grouped so the same event cannot cross partitions;
- complete raw and decision distributions, not just the chosen side;
- an out-of-sample calibration assessment appropriate to the target, with reliability uncertainty and sharpness;
- typed parameter, input, structural, calibration, scenario, and Monte Carlo uncertainty;
- cross-market coherence checks tied to a shared joint distribution where markets overlap;
- a complete candidate-universe and selection-policy test;
- paired baseline comparison with event-clustered uncertainty and protected-scope non-inferiority checks;
- a spent/untouched test ledger and hypothesis-family multiplicity control;
- a later prospective shadow report with no post-view tuning;
- explicit owner, independent reviewer, approval, expiry, monitoring thresholds, incident procedure, and rollback artifact;
- for price-enabled use, a separately validated price, vig, limit, timestamp, execution, settlement, and CLV/P&L pipeline.

Until those items are backed by exact artifacts and the release validator accepts the activation candidate, status remains DEVELOPMENT or SUSPENDED.

## 6. Research principles adopted for the next cycle

### 6.1 Chronological validation by `known_at`

Sports data are nonstationary: rosters, rules, schedules, providers, and team strength change. Validation therefore follows time and uses what was actually knowable, not a random row split. Rolling-origin evaluation is the default design ([Tashman, 2000](https://doi.org/10.1016/S0169-2070(00)00065-0)); empirical work on nonstationary time series likewise supports time-aware out-of-sample procedures ([Cerqueira et al., 2020](https://doi.org/10.1007/s10994-020-05910-7)). Cross-validation can be valid under stated residual/dependence assumptions, but those assumptions are not a license to shuffle evolving sports events ([Bergmeir, Hyndman & Koo, 2018](https://doi.org/10.1016/j.csda.2017.11.003)).

The operational rule is stricter than `event_date`: for each input, the recorded `known_at` and ingestion state must precede the forecast cutoff. Train, tune, calibrate, untouched test, and prospective shadow are disjoint half-open time intervals, and all rows from the same event stay in one partition.

### 6.2 Proper scores, calibration, and sharpness

A forecast is a distribution, so evaluation uses proper scoring rules that reward honest probabilities ([Gneiting & Raftery, 2007](https://doi.org/10.1198/016214506000001437)). Binary targets report Brier and log loss; ordered or continuous/count targets add an appropriate distribution score. The baseline and model must be scored on identical rows and weights.

Calibration is always qualified by target and notion: marginal, classwise, conditional/segment, or joint. A reliability diagram alone is not proof, especially with small or adaptively chosen bins. Calibration tests and diagnostics must state the estimand and uncertainty ([Vaicenavicius et al., 2019](https://proceedings.mlr.press/v89/vaicenavicius19a.html)); binning itself has an unavoidable confidence-versus-resolution tradeoff ([Arrieta-Ibarra et al., 2022](https://www.jmlr.org/papers/v23/22-0658.html)). After calibration is adequate, sharper forecasts are preferable, but sharpness cannot compensate for miscalibration ([Gneiting, Balabdaoui & Raftery, 2007](https://doi.org/10.1111/j.1467-9868.2007.00587.x)).

### 6.3 Selective prediction is evaluated as a curve

Abstention is legitimate only when its costs and coverage are visible. A system that predicts one easy case and passes on everything else can look accurate while being useless. Each fixed decision policy therefore reports risk versus coverage, area under the risk-coverage curve, and performance at preregistered coverage or risk targets. The methodology follows selective-classification work rather than a hand-tuned confidence threshold ([El-Yaniv & Wiener, 2010](https://jmlr.org/papers/v11/el-yaniv10a.html); [Geifman & El-Yaniv, 2017](https://papers.nips.cc/paper_files/paper/2017/hash/4a8423d5e91fda00bb7e46540e2b0cf1-Abstract.html)). Where a formal finite-sample guarantee is claimed, the assumptions and target risk must match a method such as conformal risk control ([Angelopoulos et al.](https://research.google/pubs/conformal-risk-control/)); the label “conformal” is not itself a guarantee.

### 6.4 Related markets must come from a coherent joint object

Winner, handicap, total, team total, period total, and player/count markets often share the same primitive events. Independently fitted marginal probabilities can violate arithmetic or logical constraints. Overlapping outputs must reference a common `joint_distribution_id`, state space, and constraint set, or explicitly declare why they are unrelated. This treats coherence as an accuracy-relevant property, not cosmetic tidiness ([Predd et al., 2009](https://doi.org/10.1109/TIT.2009.2027573)). Complete branch probabilities must sum to one within numerical tolerance. Distributional comparison for multivariate forecasts can include an energy score and, for dependence-sensitive evaluation, a variogram score ([Scheuerer & Hamill, 2015](https://doi.org/10.1175/MWR-D-14-00269.1)).

### 6.5 Uncertainty is typed, not collapsed into a decorative interval

The rebuild separates:

- outcome or aleatoric uncertainty;
- parameter-estimation uncertainty;
- input and lineup/availability uncertainty;
- structural/model-form uncertainty;
- calibration-mapping uncertainty;
- scenario/regime uncertainty;
- Monte Carlo numerical error;
- source and definition uncertainty.

Each component needs a target, method, level where applicable, data period, artifact hash, and sensitivity result. They must not be added as if independent unless a registered joint method justifies that operation. A predictive interval for an outcome is not a confidence interval for its probability. A small Monte Carlo standard error says only that the chosen model was simulated precisely.

### 6.6 Repeated testing spends evidence

Trying many features, leagues, thresholds, markets, or model variants and reporting only the winner creates selection bias. Every proposed test belongs to a `hypothesis_family_id`, has a preregistered rule and event-manifest hash, and changes from `PLANNED_UNTOUCHED` to `SPENT` on first inspection. A spent cohort cannot be relabeled untouched.

The family uses a declared control appropriate to the question: Holm for strong family-wise error control ([Holm, 1979](https://www.jstor.org/stable/4615733)), Benjamini-Hochberg for a declared false-discovery-rate setting ([Benjamini & Hochberg, 1995](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x)), a reality-check-style procedure for data-snooped strategy comparisons ([White, 2000](https://doi.org/10.1111/1468-0262.00152), subject to its assumptions), or a preregistered sequential alpha-spending rule ([Lan & DeMets, 1983](https://doi.org/10.1093/biomet/70.3.659)). Always-valid monitoring requires an explicit confidence-sequence/e-process design, not repeated ordinary confidence intervals ([Howard et al., 2021](https://doi.org/10.1214/20-AOS1991)).

### 6.7 Governance artifacts are part of the model

Each dataset has a datasheet describing origin, collection, definitions, coverage, known limitations, temporal behavior, and maintenance ([Gebru et al., 2021](https://doi.org/10.1145/3458723)). Each model version has a model card describing intended use, excluded use, exact scope, metrics, evaluation strata, limitations, ethical or integrity concerns, owner, approval, and expiry ([Mitchell et al., 2019](https://doi.org/10.1145/3287560.3287596)). These are evidence indices, not marketing documents.

The operating framework adopts the GOVERN/MAP/MEASURE/MANAGE logic of the [NIST AI Risk Management Framework](https://doi.org/10.6028/NIST.AI.100-1), with monitoring treated as a lifecycle control rather than a one-time validation exercise ([NIST AI 800-4](https://doi.org/10.6028/NIST.AI.800-4)).

## 7. Sport-source retrospective and strategy

The old approach often equated “search multiple reputable sites” with source validity. The correct unit is a fact-specific chain:

`registered source -> exact route/document -> raw snapshot -> parser/version -> observation timestamps -> conflict rule -> feature lineage -> model snapshot`

The machine source catalog now includes official starting points across Australian football, rugby league and union, cricket, soccer, baseball, basketball, hockey, American football, tennis, volleyball, golf, motorsport, combat, and government weather. Its presence narrows the search surface; it does not prove production readiness.

Practical lessons by source class:

- **Rules and settlement:** use the exact effective competition document, not a generic sport page. IFAB, ICC, FIVB, FIA, league rulebooks, and commission rules can have season, event, or jurisdiction variants.
- **Event identity and final result:** retain the official match/game/event sheet and correction chain. A media recap is a discovery aid, not the controlling settlement source.
- **Lineups, starters, goalies, withdrawals, and availability:** distinguish announced, projected, confirmed, warm-up, and actual participation states. Absence of a centralized official injury report is a real coverage gap, not permission to treat rumors as facts.
- **Live state:** require a tested low-latency route, snapshot hash, sport-native state schema, clock/possession/exposure validation, and a stale-data cutoff. A page that can be viewed manually is not automatically suitable for a live model.
- **Weather:** retain issue time, valid time, location/coordinates, units, venue roof state, and the exact government forecast observation used.
- **Advanced provider data:** definition, revision policy, license, coverage, and latency matter as much as authority. Do not combine vendor statistics with the same label until a reconciliation test passes.
- **Fallbacks:** every fallback has an authority downgrade, latency expectation, and conflict rule. Silent substitution invalidates the model snapshot.

Volleyball, motorsport, and combat were especially underdeveloped in the legacy framework. They now have official rules/event-source starting points, but still lack approved point-in-time datasets, fitted sport-native models, calibration evidence, and shadows. They remain DEVELOPMENT.

## 8. Monitoring, suspension, and learning without leakage

Activation would start a new evidence phase, not end validation. Monitoring must be stratified by exact model version and homogeneous competition/market/state scope. It reports:

- request volume, ISSUE/WATCH/PASS counts, and selection coverage;
- source failures, staleness, parser changes, missingness, and conflict frequency;
- proper scores and paired baseline deltas;
- calibration and sharpness with sample counts and uncertainty;
- interval/tail behavior for count or continuous targets;
- protected segment performance and cluster concentration;
- drift statistics tied to preregistered responses;
- price availability, execution, CLV, and P&L only for an independently validated price-enabled mode;
- incidents, corrections, suspension events, and time to resolution.

Immediate suspension triggers include leakage, a broken definition, out-of-scope issuance, artifact/hash mismatch, unresolvable settlement error, invalid source lineage, regression-test failure, or a preregistered critical drift breach. Resume requires a new version, correction record, later untouched evidence, prospective shadow, review, approval, and expiry. Tuning on the monitoring window spends that evidence and creates a new development cycle.

## 9. What “better next time” means

The next cycle is successful only if it produces a small, exact, reproducible scope with honest abstention—not a broad catalog of plausible probabilities. The minimum definition of done is:

- [ ] one exact competition/market/state/horizon contract is registered;
- [ ] all decisive facts have approved point-in-time source lineage;
- [ ] the dataset and model are documented with a datasheet and model card;
- [ ] a transparent baseline is frozen before challenger comparison;
- [ ] partitions are chronological by `known_at`, event-disjoint, and manifest-hashed;
- [ ] tuning, calibration, untouched test, and prospective shadow are separately registered;
- [ ] the primary metric, guardrails, risk/coverage rule, strata, and multiplicity family are preregistered;
- [ ] complete distributions are calibrated and coherent for the claimed target;
- [ ] typed uncertainty and sensitivity results are recorded;
- [ ] the test shows a practically relevant paired improvement with uncertainty, without failing calibration, tail, subgroup, or operational guardrails;
- [ ] the shadow run reproduces the decision path prospectively;
- [ ] runtime negative tests prove that missing or mismatched evidence fails closed;
- [ ] promotion, expiry, monitoring, suspension, and rollback are approved together;
- [ ] a dated no-clobber release bundle captures all inputs, outputs, hashes, commands, tool versions, tests, warnings, and limitations.

If any item is missing, the honest result is DEVELOPMENT, SHADOW, WATCH, or PASS. “Almost ready” is not an ACTIVE state.

## 10. Final non-claims

As of this retrospective:

- there is no ACTIVE model;
- there is no authorized current probability, pick, edge, price claim, or staking recommendation;
- there is no verified historical calibration, ROI, yield, or profitability result;
- no development architecture card supplies fitted parameters;
- no source-registry row proves an approved model-specific source chain;
- no simulation count converts structural uncertainty into confidence;
- no static validator or unit-test result, by itself, proves empirical model quality;
- no future activation should rewrite or rehabilitate the legacy rows as prospective evidence.

The rebuild's most valuable result is not a new number. It is a framework that can say “not known” in a reproducible way and a concrete path for earning the right to say more.
