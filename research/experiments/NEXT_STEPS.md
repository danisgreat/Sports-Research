# Fifteen experiment measures and next steps

Local working files are authoritative. This is the current measurement implementation for all fifteen source-bound retrospective proposals. Original hypotheses, issued forecasts, research P-IDs and qualification states remain unchanged. The [measure register](../experiment_measures.json) binds the [versioned protocols](protocols_v1.json). All fifteen have implemented measurement infrastructure; their motivating sporting games are not new untouched test evidence. No model experiment has been run at registration.

## What is implemented

- Exact, paired candidate/comparator contract Brier scores. Three-state LOSS/PUSH/WIN preserves push mass; regulation 1X2 uses AWAY/DRAW/HOME. Half-line contracts naturally have zero push mass. Multiclass Brier is divided by two, matching the existing binary scale.
- Log loss without silent clipping. An observed zero-probability outcome is explicitly infinite, shown as `null` plus a flag, and blocks automatic statistical review.
- Discrete predictive-distribution CRPS, central 50/80/95-percent interval coverage, width and interval score. Scale-dependent diagnostics stay separate by target; goals and corners are not combined into a raw-unit score.
- Ten fixed reliability bins per outcome category, including empty bins, and paired week-block uncertainty for the candidate-minus-baseline reliability difference. These diagnose a fixed-bin functional, not proof of complete calibration.
- One fixed-weight score per event, even when it has multiple targets or complementary selections. Ranked-row hit rates are descriptive; four related picks do not create four independent games.
- A fixed fifteen-comparison family, family alpha 0.05, per-comparison alpha 0.05/15, 60,000 paired ISO-week bootstrap replicates and a fixed seed. Primary intervals have nominal confidence 99.6667 percent. This is approximate percentile inference, conditional on a predeclared dependence audit; adjacent weeks are not automatically independent.
- A separate-pilot sample plan with at least eight pilot week blocks and at least twenty evaluation blocks. Planning distinguishes the minimum worthwhile improvement from the larger anticipated improvement. It reports a normal-approximation estimate, not achieved power. The cohort must satisfy both the event and block requirements, and enough actual numeric forecasts must remain after voids/abstentions.
- Immutable protocol creation with pinned evaluator code, critical dependencies and Python/NumPy/SciPy versions; real-time hash-chained forecast capture; event/model/source-reference checks; availability/cutoff checks; full chronological cohort accounting; no overwrite of lock/result files.
- No statistical decision while any registered member is pending or missing. Invalid evidence, insufficient numeric coverage, inadequate blocks and infinite log loss remain explicit blockers. Voids and abstentions retain dispositions instead of being scored as losses.
- `INCOMPLETE`, `RETAIN_BASELINE` or `CANDIDATE_FOR_REVIEW` readback. None confers certified performance eligibility, changes a model, or consumes a canonical prediction ID.

## Experiment-specific measures and immediate work

| Source | Required measures/checks | Immediate next implementation/data steps |
|---|---|---|
| P-492, MLB pitcher outs | Exact outs-threshold Brier/log loss; outs PMF CRPS and intervals; removal-risk/lineup/workload inputs | Collect pregame workload, lineup-strength and removal-history features; build a starter-only baseline and removal-risk candidate; retain related side/outs selections as one event. |
| P-524, KBO starter/bullpen | Total-runs PMF and contract measures; starter identity, bullpen workload and reliever availability | Build an as-of bullpen workload table and a starter-only baseline; add a relief component and evaluate the same fixtures, retaining missing workload. |
| P-525, live NPB | Remaining-runs measures; valid inning, 0–2 outs, base bitmask 0–7; frozen current runs; remaining runs equals final runs minus observed current runs | Build an exact live-state parser and baseline at the same observation horizon; archive state before its next play; model remaining runs without final-score leakage. |
| P-526, KBO command/relief/ranks | Margin/total measures; exact four supplied-to-ranked contract IDs; one representative target per family; descriptive top-rank win rate | Define the command and relief features using pre-cutoff sources; build individual feature ablations; freeze original supplied contracts and candidate ranks before final outcomes. |
| P-527, basketball scenarios | Scenario probability normalization; margin/total PMFs derived from the same joint score matrix; calibration and interval measures | Collect rotation-minute expectations and pace scenarios; fit/freeze scenario weights on earlier development data; produce a coherent candidate and unchanged comparator. |
| P-528, AHL empty-net tail | Confirmed goalie, special-teams exposure and empty-net probability; full-game total distribution measures | Build owner-backed goalie confirmation and special-teams inputs; compare otherwise identical models with/without an empty-net component; obtain separate pilot losses. |
| P-529, NHL regulation/OT | Regulation 1X2 and overtime-inclusive winner measures; candidate full-game home-win probability must equal regulation home-win plus regulation draw times conditional OT home-win | Build regulation and overtime components; freeze goalie evidence and exact endpoints; validate regulation/full-game conversions before data collection. |
| P-530, MLB opener/wind | Opener/bulk identity and workload, measured wind direction/speed, total measures, retained original-model and card distributions | Build opener/bulk identification and measured-weather adapters; isolate each feature ablation and retain both unadjusted and adjusted prediction artifacts. |
| P-531, WNBA joint scores | Confirmed starting units, late-separation/scoring-floor features; joint margin/total consistency and tail measures | Build a joint score model and a fixed baseline, using earlier data; add late-separation/scoring-floor components independently; establish starting-unit availability timestamps. |
| P-532, NBL FT/rebounds | Free-throw and offensive-rebound rates separated from pace; joint score consistency; injury availability | Build rate/pace/injury tables with as-of provenance; fit one-feature-at-a-time ablations; collect a numeric shadow cohort without changing requested-research eligibility. |
| P-533, KBO late ties | Exact supplied-to-ranked IDs; explicit regulation/extra-inning contract scope; total PMF measures | Build separate late-regulation and extra-inning components; verify supplied handicaps are never replaced by moneyline selections; freeze the full-game rules. |
| P-534, NRL late scores | Coherent joint margin/total PMF; distinct outright/cover thresholds; late-score probability; interval and calibration measures | Build a joint score baseline, add a late-score branch, and predeclare every gap/threshold. Estimate any lineup/finals feature from earlier evidence instead of this one final. |
| P-535, replacement rotation | Available rotation, matched nonnegative expected minutes and replacement usage; coherent margin/total and tail measures | Build replacement-player minutes/usage inputs; compare a uniform injury penalty against replacement-depth features on the same games. |
| P-536, rest/asymmetric tails | Available rotation, nonnegative elapsed rest, home/away tail features; joint score and interval measures | Calculate elapsed rest from exact timestamps; build separate team-score tails and a fixed total-average comparator; record rotation before cutoff. |
| P-537, football period/provider | Two distinct matching phase/provider records including an authoritative record; perfect declared adapter corpus with extra-time, conflict and wrong-event cases; first-half/corners measures | Build and independently review the phase/corners adapter first; assemble at least twenty real audited cases; resolve owner/provider mappings before fitting or testing forecasts. |

All proposed feature effects remain hypotheses. Required input presence, valid ranges and PMF consistency can be measured now; causal feature effects require the separate candidate/baseline experiments described above.

## Full execution sequence for every experiment

1. Select the exact league/season/population and sporting endpoints. Build owner/phase/provider adapters and validate them on development cases, including wrong-event and conflict handling. Archive raw inputs and parser/code hashes. At least twenty unique declared adapter cases are required; P-537 also requires extra-time cases. The framework reads retained adapter expectations/results and hashes; it does not independently rerun an arbitrary external adapter.
2. Build a simple named comparator and candidate with explicit versions. Record their dependency/code/input references, sports-only flag and last training-outcome timestamp. Source ownership, independent collection and real availability still require their own audits; a JSON flag/hash does not establish these facts.
3. Collect separate pilot event-level candidate-minus-baseline Brier differences, ISO-week IDs, original forecast/outcome provenance and the latest pilot outcome time. Use at least eight pilot weeks. Select a worthwhile improvement and a larger anticipated improvement with a written rationale; specify non-inferiority tolerances for log loss, reliability and each target's interval score, in the correct units.
4. Generate the power plan. Review serial dependence and the ISO-week grouping. The power calculation uses block ratio-estimator influence variation and a normal approximation; if that sampling assumption is unsuitable, revise the versioned protocol instead of treating its estimate as validated power.
5. Register a complete chronological future cohort with unique native event IDs, exact contract IDs, provider, metric, threshold, direction, period and overtime/extra-inning scope. Include all four supplied contracts for P-526/P-533. Freeze the cohort before any member starts, with enough events and weeks for the calculated plan. Make all exclusions/abstention policies explicit before looking at outcomes.
6. Fill the template references and acceptance tolerances. Freeze to a new lock file. Capture each forecast using the CLI's real UTC time, with feature availability no later than the forecast cutoff, which cannot precede the lock. Pregame capture must precede scheduled and subsequently verified actual start. A live forecast must use its actual observed state; no backdating.
7. Collect every outcome/void/pending/abstention disposition. Store normalized facts with exact identity, actual-start semantics, the frozen target contracts, numeric values and retained original-source references. Evaluate only the full registered sample; an unsettled early member cannot be dropped to use later successes.
8. Review primary improvement beyond the worthwhile threshold, secondary non-inferiority, coverage, intervals, missingness and failure cases. A result is eligible for human statistical review only if all checks pass. Obtain the separate model/family/source qualification and prospective shadow requirements before any operational deployment. Preserve every original forecast and version later corrections.

## Commands

Run from the repository root. Runtime outputs belong under `research/experiments/runs/`; all lock/result outputs refuse overwrite. Names below are placeholders for real source-backed artifacts, not generated predictions.

```powershell
py -3.14 -B -m research.experiments.runner verify
py -3.14 -B -m research.experiments.runner status
py -3.14 -B -m research.experiments.runner template RIP-20261005-P-527 research/experiments/runs/P527-v1/draft.json
py -3.14 -B -m research.experiments.runner plan research/experiments/runs/P527-v1/pilot.json <worthwhile-improvement> <anticipated-improvement> research/experiments/runs/P527-v1/power.json --rationale "Source-backed effect-size and tolerance rationale"
py -3.14 -B -m research.experiments.runner freeze research/experiments/runs/P527-v1/draft.json research/experiments/runs/P527-v1/lock.json
py -3.14 -B -m research.experiments.runner capture research/experiments/runs/P527-v1/lock.json research/experiments/runs/P527-v1/payload.json research/experiments/runs/P527-v1/forecasts.jsonl
py -3.14 -B -m research.experiments.runner evaluate research/experiments/runs/P527-v1/lock.json research/experiments/runs/P527-v1/forecasts.jsonl research/experiments/runs/P527-v1/outcomes-v1.json research/experiments/runs/P527-v1/result-v1.json
```

`plan` requires actual numeric choices; angle-bracket placeholders above are not runnable PowerShell arguments. Obtain experiment IDs for all fifteen from `status` or the register. Evaluation exits 2 for incomplete evidence, 1 for invalid inputs, and 0 for a completed development decision, including retaining the baseline. Exit 0 does not mean the candidate won or is qualified.

## Artifact fields

Every reference is `{ "path": "workspace-relative/path", "sha256": "exact 64-character SHA-256" }`; path escapes and changed bytes fail.

| Artifact | Required contents |
|---|---|
| Draft | Source-bound template plus the six artifact references and every acceptance tolerance. No missing numeric value is replaced by a guessed default. |
| Model artifact | `model_version`, `sports_only: true`, `training_last_outcome_utc`, nonempty `dependency_refs`. |
| Pilot | `differences`, `weeks`, `last_outcome_utc`, nonempty `basis_refs`. Values must come from actual paired pilot scoring. Synthetic tests are never a pilot. |
| Power plan | Generated sample fields, `pilot_ref`, `effect_size_rationale`; freeze independently recomputes its planning numbers. |
| Dependence audit | `reviewed_by`, `block_definition: "ISO_WEEK"`, `rationale`, nonempty `basis_refs`. This records an assumption/evidence review, not guaranteed independent weeks. |
| Adapter report | `reviewed_by`, `adapter_code_ref`, at least twenty unique `cases` with `case_id`, `role`, `body_ref`, `expected`, `observed`. Wrong-event/conflict cases must explicitly reject or remain unresolved. |
| Cohort | `events` in scheduled-start order. Each has `league`, `season`, `event_id`, aware `scheduled_start_utc`, and exact `targets` keyed like its protocol. |
| Target contract | `contract_id`, native `event_id`, `metric`, `threshold`, `rule` (`OVER`, `UNDER`, `HOME_1X2`), `period`, `includes_overtime`, `provider`. 1X2 requires a zero margin threshold. |
| Forecast payload | Identity, `disposition: "FORECAST"`, `state`, `cutoff_utc`, `features`, and `candidate`/`baseline` versioned target PMFs. A PMF has ordered integer `support` and normalized `probabilities`. Live payloads also need a `live_state_ref` with matching native event, `state: "LIVE"`, observation time, inning/outs/bases/current score/batting half and original `source_refs`. |
| Feature | `value`, aware `available_utc`, `evidence_ref` to normalized `event_id`, matching `available_utc`, `features` and nonempty original `source_refs`. Types and experiment-specific requirements are enforced. Hash-binding declared availability does not independently prove publisher availability. |
| Joint score forecast | Each arm's `joint` has home/away support and a probability matrix; its margin/total PMFs must equal the matrix's derived marginals. |
| Ranked forecast | P-526/P-533 cohort has four unique `ranked_contracts` (`target`, `contract`); feature `ranked_contract_ids` preserves the candidate order and exact supplied set. |
| Model/card separation | P-530 candidate additionally retains its original unadjusted `model_targets` PMFs alongside card targets. |
| Outcome file | `records` with identity, `state` (`FINAL`, `PENDING`, `VOID`) and `facts_ref`. No duplicate event or out-of-cohort result is accepted. |
| Terminal facts | Identity/state, `actual_start_utc`, `observed_utc`, nonempty original `source_refs`, `targets` containing each exact frozen `contract` and numeric `value`. Voids require a reason. Live remaining runs also require `full_game_runs` and an audited `actual_end_utc`; capture must precede actual game end. |
| Abstention | `disposition: "NO_FORECAST"` and a reason, captured as its own immutable cohort decision. It remains in the denominator and cannot disappear from evaluation. |

## Current readiness and next deliverables

All fifteen protocols have explicit targets, feature types, measures, failure checks and seven next-step items. All currently lack real candidate/comparator artifacts, future cohorts, separate pilot/power evidence, adapter/dependence audits and justified tolerance values. Thus zero are frozen or run at registration. This is an explicit input requirement, not a statistical result.

The next deliverables for each row are: **validated adapter and feature dataset → comparator and candidate artifacts/ablations → separate pilot scores and sample plan → completed future cohort and lock → immutable forecasts and terminal evidence → measured result → separate qualification review**. Build those deliverables with the registered measures; do not relabel the original postgame review as prospective evidence.

Method references: [Gneiting and Raftery, proper scoring rules](https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf), [SciPy paired bootstrap and approximation limitations](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html), and [R multiple-comparison documentation](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/p.adjust.html). The local implementation resamples paired week blocks explicitly; it does not invoke SciPy's IID bootstrap on individual correlated contract rows.
