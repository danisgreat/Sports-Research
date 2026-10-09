# Prediction repairs — October 9, 2026

Authority: MDS-2026.10.09-v8.4 / CR-2026.10.09-R4 / SCV-2026.10.09-v5.

The requested repairs make the prediction path use fitted, versioned models and independent winner calibration, and remove misleading historical evaluation claims. The inputs are the retained `Previous Sports Results` archive and existing EPL population CSV. These are historical development results; no live qualification is asserted.

## Changes and evidence

| Problem | Repair | Verification |
|---|---|---|
| Estimated league parameters included test seasons | Derive scoring, dispersion, overtime, shootout and baseball environment profiles solely from each earlier TRAIN population | Cutoff guard, fold dates and retained profile dates |
| Draws were removed from a home-win cohort but probabilities were unconditional | Retain draws as home non-wins, with the same population and definition for the baseline | Draw-inclusive regression and saved event forecasts |
| Candidate generation bypassed fitted artifacts | Default to the saved engine plus joint winner calibrator, with exact sport/competition/stage/endpoint and actual build-time checks | Real artifact smoke check plus scope/time regression |
| Independently adjusted probabilities could break cross-contract coherence | Fit one temperature on CAL home/away/draw vectors and reweight the joint score grid before pricing every candidate | Normalization, structural-zero, win/push/loss and monotonicity checks |
| MLB doubleheaders and repeated NBA dates could collapse into one game | Retain native game IDs; deduplicate identical rows; quarantine every row of conflicting identities with source locations | Doubleheader, conflict and quarantine regression |
| MLB probability-vector rounding prevented extra-inning resolution | Preserve full empirical precision for profile extras | Empirical vector through the full-game endpoint regression |
| NHL final OT/SO goals were used as regulation training goals | Require an explicit OT flag and remove the recorded deciding goal from OT/SO finals; reject inconsistent margins | OT normalization and missing-flag regression |
| Missing historical Rank-1 gates were treated as passes | Separate recorded PASS, LEGACY_P_ONLY and UNKNOWN_GATE cohorts | Published-scoreboard verification and unknown-gate regression |
| Genuine zero probabilities disappeared as if missing | Retain 0 and 1 in scoreboard probability scoring; protect only logarithm evaluation | Boundary-probability regression |
| Windows validation failed on paths and fixture newline changes | Publish POSIX paths; edit only appended fixture bytes, preserving the frozen prefix | Original failing scoreboard and pending-import checks |

The production candidate pipeline uses chronological, disjoint TRAIN → CAL → TEST ranges. It saves the exact engine and calibrator evaluated on TEST, without refitting on TEST. CAL fits winner temperature only; total, handicap and team-total probabilities are coherent derived research values, not independently calibrated claims. Too little CAL evidence produces `IDENTITY_INSUFFICIENT_CAL`, never an invented fitted status. Candidate issuance refuses unknown teams and requires verified regular-season scope.

The separate rolling evaluation refits monthly and uses training-frequency comparators and training-median half-point lines. Every forecast retains its game identity, date and cutoff, so paired measurements can be inspected. Archive result dates are conservative calendar cutoffs, not proof of historical source-publication or actual-start timestamps.

## Rebuilt measurements

Build measurements and validation results are being completed before this report is finalized.

## Custody and limits

The original `runtime_h0/` build evidence is retained. Corrected receipts and engine-plus-calibrator artifacts are under `research/model_builds/runtime_h0_v2/`. Receipts pin code dependencies and every input file hash. Original forecasts, canonical IDs, logs, ledger records and archive CSVs are unchanged. Conflicting archive rows are retained in receipt exclusion metadata; their source files are not edited.

All saved pipelines remain **SHADOW_ONLY**. The historical data has already been opened during development. Winner temperature fitting, passing mechanics tests and an improved loss estimate do not prove reliable real-event probabilities, current lineup coverage or live performance. Prospective frozen forecasts, complete eligible outcomes, scope-specific calibration and monitoring are still needed. No challenger is deployed by this repair.

## Reproduction

Use the pinned CPython 3.14.6 interpreter and repository dependency locks. From the repository root:

```powershell
$env:OPENBLAS_NUM_THREADS = '1'
$env:OMP_NUM_THREADS = '1'
$env:MKL_NUM_THREADS = '1'
py -3.14 -B -m research.operations.fit_runtime_models run
py -3.14 -B -m research.operations.boosted_challenger run
py -3.14 -B -m research.operations.scoreboard publish
py -3.14 -B -m research.operations.current_state write
py -3.14 -B -m research.operations.dev_check
```

Build timestamps and measured runtimes will differ on reproduction. An intentional rebuild changes controlled artifacts and requires a new versioned control freeze; never overwrite an existing freeze. The candidate request example is in [runtime/README.md](../../../runtime/README.md).
