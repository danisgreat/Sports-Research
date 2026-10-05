# Sports Research implementation and evidence - 1 October 2026

**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

> **Current authority (October 5):** [METHOD.md](METHOD.md) and [CURRENT_RULES.md](CURRENT_RULES.md) govern new work. Requested qualitative or explicitly uncalibrated research receives canonical Part 6 IDs regardless of calibration; numerical performance certification is separate. Read current IDs/freeze from the [status register](GAME_LOG_STATUS_CURRENT.md), unresolved items from the [carryover](research/verification/closure_2026-10-05/carryover.md), and [current implementation evidence](research/verification/implementation_2026-10-05/REPORT.md). Earlier method, queue, freeze and eligibility statements below retain their historical scope.

Status: **IMPLEMENTED AND LOCALLY VERIFIED; ALL MODELS SHADOW_ONLY**. Method **MDS-2026.10.01-v7.0**, control **CR-2026.10.01-I1**, scoring **SCV-2026.10.01-v3**. This report records executed work under the user's instruction to implement the review, including probability models, sources, historical data and processes. It replaces the earlier in-progress register.

The initial review rated the workspace **5.5/10**. The implementation addresses the engineering and evidence-control defects behind that assessment. A higher predictive-skill rating is not justified by passing tests or inspecting historical outcomes. Live qualification remains zero; prospective skill has not been established.

## 1. Delivered work

| Workstream | Implemented behavior | Inspectable evidence |
|---|---|---|
| Original custody | Retained the original 89-file snapshot, frozen run/shadow/rank bytes and issued forecasts; corrections append with evidence | [Original manifest](research/custody/implementation_2026-10-01/manifest.json), [acceptance verifier](research/src/acceptance.py) |
| Probability models | Versioned coherent EPL result candidate and chronological NBL residual-width candidate; original models remain reproducible | [Candidate models](research/src/candidate_models.py), [four pinned builds](research/model_builds/current.json) |
| Evaluation | Earlier-period selection, later-period diagnostics, population and stronger comparators, family-specific scores, calibration uncertainty and week-block bootstrap | [Protocol](research/runs/implementation_2026-10-01/development_protocol.json), [results](research/runs/implementation_2026-10-01/family_diagnostics.json), [per-event forecasts](research/runs/implementation_2026-10-01/family_forecasts.csv) |
| Source access | Fifteen scoped routes, retained bodies/receipts, bounded HTTPS fetches, redirect checks and restricted-route/market quarantine | [Registry](research/sources_registry.json), [observations](research/runs/implementation_2026-10-01/source_observations.json), [fetcher](research/src/sources.py) |
| Daily research | Dated immutable observations, complete fixture dispositions, model/baseline freezes and diagnostic grades; recorded source failures | [Executed run](research/daily/20261001T021702970997Z/run.json), [daily workflow](research/src/daily.py) |
| Historical forecasts | Normalized learning views with explicit conflicts/missingness and retained anchors; retrospective rows cannot gain prospective eligibility | [2,004 contracts](research/data/processed/legacy_learning/contracts.csv), [522 cards](research/data/processed/legacy_learning/cards.csv), [manifest](research/data/processed/legacy_learning/manifest.json) |
| League CSVs | Sports-only active-lane exports with hashes and explicit ID/timing gaps | [EPL](research/data/processed/league_csv/epl_results.csv), [NBL](research/data/processed/league_csv/nbl_results.csv), [manifest](research/data/processed/league_csv/manifest.json) |
| Archive | Numeric event grain, source joins, deduplication, separate narratives, measured coverage, conservative label admission and source-backed repairs | [Guide](Previous%20Sports%20Results/README.md), [manifest](Previous%20Sports%20Results/_canonical/manifest.json), [validation](Previous%20Sports%20Results/_canonical/validation.json) |
| Temporal features | Availability/temporal-role gates, lagged form with explicit assumptions and same-day/future/postgame exclusion | [Point-in-time utilities](research/src/point_in_time.py) |
| Eligibility | Exact event/endpoint/model/family/baseline scope; source-body parsing, lineage audits, freshness and actual-start checks | [Validator](research/src/eligibility.py), [admission registry](research/admission_registry.json), [evidence template](research/schemas/forecast_evidence_TEMPLATE.json) |
| Issuance/settlement | Source-backed universe, no-ID draft preparation, locked journaled issuance, exact crash recovery and append-only settlement revisions | [Ledger](research/src/ledger.py), [issuer](research/src/issue.py), [operator CLI](research/src/workflow.py) |
| Adjustment pilot | Immutable scoped lock, source-backed power plan, chronological membership, earlier-unsettled protection and persistent interim/futility | [Pilot](research/src/pilot.py), [unfrozen template](research/PILOT_LOCK_TEMPLATE.json) |
| Operating documents | One current authority, consistent schemas/prompts and dated historical references | [Rules](CURRENT_RULES.md), [method](METHOD.md), [commands](research/README.md), [scoring](SCORING_AND_VALIDATION.md) |
| Reproducibility | Exact runtime/package lock, code/input receipts, immutable outputs, offline regression workflow and control freeze | [Dependencies](research/requirements.lock.txt), [CI](.github/workflows/research.yml), [manifest](CONTROL_MANIFEST_2026-10-01-1.md) |

## 2. Prediction changes and evidence

### EPL

`epl-coherent-ensemble-0.2.0` combines **0.75 Dixon-Coles and 0.25 TB1-MD** in one score matrix. Result probabilities and diagnostic totals/BTTS are projections of that matrix rather than separately entered percentages. Operational research registration covers **regulation 1X2 only**. Original `epl-dc-0.1.0` remains a comparison model.

Five candidates were evaluated chronologically on 1,900 games in three separate families: 1X2, total 2.5 and both-teams-to-score. Selection uses 2021-22 to 2023-24; the later development check uses 2024-25 and 2025-26, 760 events in 72 week blocks. There are 10,000 block-bootstrap replicates, seed 20261001. The experiment protocol was frozen before calculation, but the underlying historical data had already been inspected. These are **development comparisons**, not a new untouched holdout.

| Later family | Earlier-selected candidate | Candidate minus population log loss, 95% interval | Candidate minus TB1-MD log loss, 95% interval | Disposition |
|---|---|---|---|---|
| 1X2 | 0.75 DC mixture | -0.075882 [-0.097834, -0.053016] | -0.027945 [-0.041191, -0.014813] | SHADOW_ONLY research candidate |
| BTTS | 0.50 DC mixture | +0.003628 [-0.005454, +0.012668] | -0.004334 [-0.009595, +0.000633] | No clear improvement against all comparators; diagnostic only |
| Total 2.5 | 0.50 DC mixture | +0.005902 [-0.004728, +0.016759] | -0.007128 [-0.013859, -0.000591] | Does not establish improvement against population; diagnostic only |

Negative differences favour the candidate. The selected 1X2 mixture's later log loss is **1.006821**, versus **1.005560** for original Dixon-Coles. This does **not** demonstrate improvement over the original model. Its selection is retained because it was chosen on earlier periods, rather than changing the winner after seeing later outcomes. Future evidence must establish any numerical improvement.

### NBL

`nbl-oof-width-0.2.0` retains the joint model's margin mean and estimates uncertainty from **strictly earlier out-of-fold residuals**, with at least 100 observations. This avoids relying solely on optimistic in-sample residual widths. Its registered scope is regular-season moneyline **including overtime**. Original `nbl-joint-0.1.0` remains reproducible.

Four candidates were evaluated on 590 games. Selection uses NBL23/NBL24; the later check uses NBL25/NBL26, 310 events in 42 week blocks. Later candidate-minus-population log loss is **-0.061946 [-0.099014, -0.023371]**; against fixed Elo it is **-0.027671 [-0.043828, -0.012940]**. Later candidate log loss is **0.630724**, versus **0.630858** for the original joint model. That small difference is not proof of superior future predictions.

### Calibration, comparators and release

Reliability bins, observed-rate intervals and descriptive calibration intercept/slope are retained in the family report. No calibration fitted to final test outcomes is deployed. Baselines have approved pinned definitions with exact lane/league/endpoint/family/version and code artifacts. A qualification review, forecast distribution, shadow and pilot must use the same baseline version. Approval must precede cutoff; replacing a missing baseline with 0.500 after the result cannot satisfy admission.

September tuning/holdout outputs were preserved. They cannot qualify a changed model version or untested family. More complexity, websites or CSV rows is not itself evidence of improved prediction.

## 3. Sources and daily operation

The fifteen-route registry covers official NBL, MLB, Premier League, AFLW, Iowa State, Kansas State, NFL gamebooks, Perth Wildcats and NBL news; ESPN EPL/NBL structured routes; openfootball; and restricted/excluded routes. Ten probes returned the expected specified content, two ESPN routes returned HTTP 403, and three routes were manual/restricted/excluded. Successful probes retain raw bytes and retrieval/hash receipts. Accessibility does not prove every field's truth or independent upstream collection.

Football-Data and FixtureDownload acquisition remain manual/restricted under their documented access conditions. Fantasy Premier League is excluded from forecasting inputs. Restricted or odds-bearing raw benchmarks stay isolated; forecast modules use sports-only processed fields. HTTPS allowlists, pre-request redirect checks, size/time/retry limits, credential-URL rejection and body quarantine are implemented.

The first integrated daily run completed at **2026-10-01T02:17:02.970997Z**:

| Lane | Completed results observed | Upcoming fixtures | New frozen shadows within 48 hours | Diagnostic grades |
|---|---:|---:|---:|---:|
| EPL | 50 | 330 | 0 | 0 |
| NBL | 15 | 150 | 3 | 2 |

No EPL fixtures fell in the declared window. All fixture dispositions are retained. The three new NBL shadows freeze population and Elo comparators, model version, complete build artifacts, input/source hashes and missing lineup/adjustment status. The two grades concern September shadows; missing original baselines are explicitly **NOT_FROZEN**, never reconstructed after the result.

Current EPL observations are single-publisher openfootball data; derived identities stay separate from missing official event IDs. NBL uses native league UUIDs. Both lanes' current inputs are **SINGLE_PUBLISHER_PROVISIONAL** for research. Fresh retrieval is not independent terminal corroboration. The operator-run daily command issues no cards; no recurring automation is asserted.

## 4. Historical forecast learning

The normalized view retains **2,004 contract rows across 522 card IDs**, including **630 literal probabilities** and **598 diagnostic probability/grade pairs**. There are 1,765 source-linked literal-only rows and 239 conflict/gap dispositions. These describe extraction/custody, not independent result verification. Blank baselines, cutoffs, identities and grades stay blank; q remains a historical ranking quantity, not an event probability.

Every reconstructed row remains **performance-ineligible**. Forty-one status pointers whose displayed lines moved after the new dated header were anchored to the retained original status snapshot, preserving file/line hashes. Original logs and the original rank CSV remain intact. The sparse 522-slot settled-outcomes index was not regenerated to turn missingness into invented data.

## 5. Archive repairs and CSV usefulness

Final archive validation passed with:

| Measurement | Verified count |
|---|---:|
| Yearly input CSVs | 21,799 |
| Header-only inputs | 20,943 |
| Raw rows | 128,768 |
| Canonical events | 127,460 |
| Source-matched result labels | 94,448 |
| Admitted historical full-game training labels | 84,486 |
| Narratives excluded from pregame features | 128,539 |
| Duplicate / subset / mirror exclusions | 331 / 188 / 790 |
| Source receipts checked | 1,615 |
| Retained source bodies with verified hashes | 1,614 |
| Original repair backups checked | 36 |

Data snapshot hash: `8deb26297c5d36149f4bb0493612f8711c58202864ad3ec1dad1d49ae1a4ed0e`. All input/output hashes, two archive implementation hashes, original repair backups and retained receipt bodies were checked. There are 186 used receipt lineages; this is not a claim of 186 independently collected sources.

One legacy NFL receipt has no retained body and cannot verify results. MLB 2011 source record game 308207 lacks a team name and is individually excluded. These declared limitations are separate from source-body custody errors, of which there were zero.

Source-backed corrections cover **230 existing rows**, with **two completed MLB results appended**: both copies of the 2025 Dublin college-football result, the NFL Brazil venue, three AFLW aliases, 222 Brisbane Bears identities from 1987-1996 and two transposed AFL dates in 1905. Unsupported people metadata was cleared where required. Originals and evidence remain in the [custody journal](Previous%20Sports%20Results/_custody/corrections.jsonl). Twenty-seven official MLB season bodies were retained for reconciliation.

Canonical output separates numeric results from prose, retains source/parser identity and time precision, measures source populations, excludes mirrors/subsets/duplicates and records uncertainty about missing years. Thirteen formerly empty helpers now perform meaningful canonical compatibility operations. Retired enrichment builders are preserved as historical originals and do not purport to complete the archive.

**Historical league-result CSVs are useful and recommended** for baseline estimation, chronological backtesting, opponent-strength features, uncertainty and drift detection. Sports-only exports now provide **2,280 EPL games** across six 380-game seasons and **738 NBL games** across five source seasons. These are lossless views of reconciled processed data, not newly invented official EPL IDs or historical publication/actual-start timestamps.

Accept further CSVs after checking event grain, exact teams, dates, score endpoint, stage, duplication, access terms, provenance and season completeness. Prefer a retained field-owner source and compare its full event population. Date-only labels can support explicitly conservative earlier-date features; they cannot prove that a lineup, injury, venue condition or award was known before a past forecast.

The archive remains broadly incomplete: **20,943 files are headers only**. Most competition populations, postseason coverage, player participation, coaching/officiating and pregame condition histories are not complete. Historical narratives remain reference material pending field-level verification. Folder structure or an inactive label without evidence does not resolve these gaps. Do not describe the complete collection as finished or uniformly accurate.

## 6. Evidence gates and operating safeguards

```mermaid
flowchart LR
    A[Approved source] --> B[Retained body and receipt]
    B --> C[Identity, endpoint and timing review]
    C --> D[Verified model and baseline build]
    D --> E[Immutable shadow and fixture coverage]
    E --> F[Exact version and family qualification]
    F --> G[Prepared draft]
    G --> H[Locked issue journal and Part 6 append]
    H --> I[Terminal evidence and settlement revision]
    I --> J[Paired scoring and frozen pilot decision]
```

Live admission rejects self-reported VALIDATED flags and generic historical M2_PASS reports. It checks exact cached event/teams/endpoint, supported parsers, complete model/baseline artifacts, declared pre-cutoff inputs, freshness and qualification scope. It requires three audited independent pregame lineages including an official source; UNKNOWN upstream/event independence is insufficient. Terminal admission requires three independent matching finals and an explicitly audited actual-start field. Schedule time and first play cannot silently substitute.

Preparation consumes no permanent ID. Real commit revalidates under a lock with a start-time buffer, freezes the exact bundle and journals preparation before the Part 6 append. Recovery completes the exact pending projection and prevents ID reuse. Settlements append against the unchanged core; issued probabilities and baselines cannot be replaced.

All four registrations remain **SHADOW_ONLY**. Qualification requires the exact applicable untouched holdout, a model/family/endpoint review and at least **50 unique audited shadows spanning at least 28 days**, plus source/adapter evidence. Those minimums are gates, not a statistical guarantee. Qualification cannot be borrowed across versions, families, endpoints, leagues or baselines.

The pilot implementation supports the fixed seven-family EPL composite only. All its families must qualify. A source-backed fixture universe, retained power/sample plan, at least four week blocks and frozen chronological cohort are required. It waits on earlier unsettled members, records one persistent interim and makes futility terminal. NBL or another composite needs a separately versioned scoring protocol. No live pilot is frozen.

Hash joins prove retained bytes and consistency with declared metadata; they do not independently prove every historical availability time or recompute every distribution. The point-in-time utility states this limitation and cannot confer live admission. Review the original source field, model calculation and baseline construction before certifying evidence.

## 7. Executed verification

The full offline suite passed: **107 tests in 64.39 seconds**. Coverage includes temporal exclusion, probability/contracts, source hashes/native identity, admission rejection, baseline scope, ledger chains, crash recovery, settlement revisions, archive admission and persistent pilot decisions. Retained evidence: [tests](research/verification/implementation_2026-10-01/tests.json), [acceptance](research/verification/implementation_2026-10-01/acceptance.json), [archive validation](research/verification/implementation_2026-10-01/archive_validation.json).

Acceptance checks **89 original snapshot files**, **17 frozen original research artifacts**, historical Parts 1-5, the exact **141,740-byte** original Part 6 block, **four model builds**, research source bodies and learning source anchors. No live card was issued during implementation. P-523 remains next. P-518/P-522 have pre-existing learning settlement appends; P-519/P-520/P-521 retain reconciliation requirements. All five remain reserved and performance-ineligible.

Use CPython **3.14.6** and the exact dependency lock. Run from the repository root:

```powershell
python -B -m pytest -p no:cacheprovider research/tests -q
python -B -m research.src.acceptance
python -B -m research.src.archive validate
python -B -m research.src.control_manifest verify
python -B -m research.src.workflow status
```

Collect a new dated research snapshot with:

```powershell
python -B -m research.src.daily --window-hours 48
```

Frozen outputs refuse overwrite. A numerical/operational edit requires a versioned new build and appropriate new experiment/review; never silently rehash an issued model. Bulky canonical exports are local regenerable products with manifest hashes. Missing restricted local benchmarks must be reported rather than downloaded through an unauthorized route or replaced with different bytes.

The Windows GitHub workflow has a pinned runtime and action commits and runs offline tests plus manifest verification. It was added and inspected locally; **remote CI has not been verified by this implementation**. Interfaces were checked against [official checkout documentation](https://github.com/actions/checkout) and [official setup-python documentation](https://github.com/actions/setup-python).

The final receipt is [CONTROL_MANIFEST_2026-10-01-1.md](CONTROL_MANIFEST_2026-10-01-1.md). Its normalized hash and final verification are recorded in the living [status register](GAME_LOG_STATUS_CURRENT.md) and [completion receipt](research/verification/implementation_2026-10-01/completion.json). A passing manifest certifies its listed custody scope, not all narrative truth or future skill.

## 8. Remaining evidence and ordered operating plan

These data gaps and release conditions must not be closed with fabricated timestamps, grades, sources, qualifications or season contents.

| Priority | Next operation | Acceptance condition | Current state |
|---|---|---|---|
| 1 | Collect dated EPL/NBL shadows through the daily workflow | Immutable pregame cutoff, full dispositions, frozen model/population/strong comparator and build/input/source hashes | First run passed; 3 new NBL shadows; prospective sample/duration incomplete |
| 1 | Audit source collection and field semantics | Global upstream and event/body lineage audits; native IDs; actual-start mapping; fresh state and three independent finals | Routes implemented; independence UNKNOWN; live admission closed |
| 1 | Reconcile open historical cards | Exact operator/period/void contract, unchanged issued literals and independent terminal evidence; appended revision | P-519/P-520/P-521 unresolved; learning only |
| 2 | Freeze exact candidate/family holdouts before opening outcomes | Pinned code/features, baseline version, complete population, paired family scores and uncertainty; no repeated selection on test outcomes | Changed models have development evidence only |
| 2 | Review live qualification | Applicable passed holdout, exact scope, at least 50 audited shadows over at least 28 days, source and issuer evidence | Four SHADOW_ONLY versions; no promotion |
| 2 | Measure failures over the complete population | Separate source/identity/endpoint/timing defects, model misses, adjustment misses and censored fields; frozen cohort | Coverage/scoring implemented; no qualified live cohort |
| 3 | Expand result populations one competition at a time | Authorized retained source bodies, exact endpoints/IDs, complete population reconciliation, canonical admission, explicit unfilled years | MLB/AFL/AFLW/NFL results substantially represented; most other folders incomplete |
| 3 | Expand pregame covariates where historically timed evidence exists | Player/lineup/injury/venue/condition provenance and availability; no same-game outcome or retrospectively inferred lineup | Temporal gates implemented; broad historical covariates unavailable |
| 4 | Test totals/BTTS and other leagues separately | Chronological development, untouched baseline comparisons, calibration and prospective source gates | Diagnostic families and NO_MODEL leagues remain outside numerical live issuance |
| 4 | Freeze an adjustment pilot after full family qualification | Complete universe, source-backed power plan, adequate blocks and immutable coefficients/sample/interim rules | Implementation ready; live pilot NOT_FROZEN |

Prioritize source reliability, exact endpoints and calibration over untested additions. More historical CSVs are worthwhile when they improve verified coverage or chronological features. More files without source and temporal quality increase apparent volume without increasing trustworthy predictive information.
