# Historical pre-event evidence — HPPV-v1

**Track H is implemented separately from current-method Track P.**
[Registration](REGISTRATION.md) · [initial report](HISTORICAL_PROSPECTIVE_VALIDATION_REPORT.md)
· [full census](HISTORICAL_CENSUS.csv) · [qualification](HISTORICAL_QUALIFICATION.csv).

The initial assessment accounts for **685 cards and 3,150 contract rows**. It does
not invent custody evidence. Zero contracts are independently Tier-A qualified by
this initial import; the verdict is `HISTORICAL_EVIDENCE_INSUFFICIENT`. This means
original issuance still needs verification, not that historical forecasts were
necessarily late or lacked predictive information. Existing historical training
scores and admissions are preserved. The strict ML backtest is implemented but no
real run can be issued until verified availability records are recovered.

## Commands

Run from the repository root with `research/requirements.txt` installed:

```bash
python -m ml historical-pre-event verify --run research/verification/historical_pre_event_v1
python -m ml historical-pre-event run --out research/verification/hppv_runs/EXAMPLE_RUN
python -m ml historical-pre-event append --row-id R00001 --evidence /path/to/reviewed-evidence.txt --reviewer 'Reviewer name' --reason 'Recovered original independently timed publication'
python -m ml historical-pre-event backtest --features /path/to/reviewed-features.csv --out research/verification/hppv_model_studies/EXAMPLE_RUN
```

Run directories must be new. The append command validates evidence before writing
one full assessment revision, chains it to the previous ledger hash and locks the
file against competing writers. Downgrades and withdrawals are appended too.
Each run freezes its own `EVIDENCE_SNAPSHOT.csv`, so appending future reviews does
not invalidate earlier runs. Verification uses that frozen snapshot, validates
every historical revision, checks complete input/output hashes and regenerates all
tables byte for byte. Regenerate using the implementation commit that made the run.

## Eight stages and outputs

| Stage | Output | Admission/control |
|---|---|---|
| Census | HISTORICAL_CENSUS.csv, COVERAGE.csv | All P-001–P-685 and all 3,150 rows; duplicate IDs or omissions fail |
| Original recovery | ORIGINAL_FORECASTS.csv | Frozen values retained; raw capture + exact reviewed transcription required |
| Timing/custody | TIMING_AND_CUSTODY_AUDIT.csv | Independent timestamp bound to raw original; compare to actual first play |
| Qualification | HISTORICAL_QUALIFICATION.csv, QUALIFICATION_HISTORY.csv | A–E evidence tiers; revisions preserved |
| Settlement | VERIFIED_OUTCOMES.csv | Independent result, grading rule, exact endpoint; original and revised grades separate |
| Benchmark | HISTORICAL_BASELINES.csv | Same endpoint, sports-only, verified feature/label/tuning cutoffs |
| Statistics | HISTORICAL_PERFORMANCE.csv, CALIBRATION.csv, DEPENDENCE_SENSITIVITY.csv, EVIDENCE_TIER_SENSITIVITY.csv | Event-level primary inference; exploratory strata and block sensitivities |
| Verdict | HISTORICAL_PROSPECTIVE_VALIDATION_REPORT.md, MANIFEST.csv | Deterministic registered gates; no promotion into Track P |

`SOURCE_RECONCILIATION.csv` records original training receipt hashes and frozen
Git blob hashes at commit `4e0cb198c50230d8e2abf2f1a976d92338301520`. Full Git
history is required to regenerate. Later additions to active Combined Logs do not
alter this historical cohort. Census rows, admissions, receipts and audit must still
match that registered commit. Ten older CSV input hashes use Windows CRLF; where the
Git blob is LF, only exact reconstruction of that CRLF representation is accepted
and explicitly labelled. Any other input change fails. Original forecast captures
always require exact SHA-256; this newline exception never authenticates issuance.
The initial root documents are a frozen assessment, not a live prospective scoreboard.

## Evidence record format

The append input is a UTF-8 `.txt` file containing a JSON object (no new JSON/binary
repository artifacts are required). It can contain `original`, `event`, `outcome`,
`baseline`, `known_outcome_exposed`, `exposure_proof`, `incomplete_reason`. Omit
unavailable evidence; do not fill missing fields with invented data. Each revision
is a full replacement assessment, not an implicit merge with earlier revisions.
The CSV ledger stores its canonical payload and chain hash. See the synthetic
`fixture` in [tests](../../../../ml/tests/test_historical_pre_event.py) for a complete
working example; those example sources are fixtures, not real evidence.

An artifact reference has exactly these required provenance fields:

```json
{"path":"research/verification/hppv_captures/EXAMPLE.txt","sha256":"<exact 64-character SHA-256>","url":"https://<original-source>"}
```

A review proof contains `capture` (an artifact reference), `reviewer`, `finding`,
and timezone-qualified `reviewed_at`. The capture retains the independently
reviewed source, not just an unsupported true/false checkbox. **A reviewer must
actually authenticate the evidence:** the program checks hashes, identity,
cutoffs and consistency, but cannot prove the truth of a human finding.

| Object | Required fields and findings |
|---|---|
| original | `capture`, `transcription`, `integrity_review`; optional `publication` |
| transcription capture | JSON object with `forecast` and `identity` below, plus actual original `method` version |
| forecast | Exact strings `row_id`, `card`, `rank`, `contract`, `p` from the frozen ROWS.csv, including empty p |
| integrity_review | Review proof; `first_recoverable_unchanged: true`; for Tier A also `no_post_issue_information: true`, actual `information_cutoff` <= issue time |
| publication | Review proof; independently verified `issued_at`, `independent_timestamp: true`, `bound_original_sha256` matching original raw capture |
| event | Stable independently verified `event_id`, `actual_first_play`, `teams` (at least two participant names), `competition`, `proof` with `actual_first_play_verified: true` |
| outcome | Exact `identity`, `grade`, `available_at`, `grading_rule`, `proof` with `independent_result: true` |
| outcome.settlement_revision | Required if independently verified grade differs from frozen grade: review proof with `previous_grade` and `corrected_grade`; original remains unchanged |
| baseline | Exact `identity`, original `p`, `kind`, `information_cutoff`, `feature_cutoff`, `training_outcome_cutoff`, `hyperparameter_cutoff`, `recipe`, `proof` |
| baseline.recipe | Artifact whose JSON content is exactly the baseline's identity, p, kind and four cutoff fields, supported by sporting-data extraction and algorithm details in the proof capture |
| baseline.proof | Review proof with `sports_only_market_blind: true`; frozen baseline also needs independent `issued_at` <= original issue, `independent_timestamp: true` and `bound_recipe_sha256` matching the recipe capture; reconstructed baseline requires `outcome_blind_reconstruction: true` |
| exposure_proof | Review proof required when `known_outcome_exposed: true` |

Every timestamp must include an explicit timezone. Actual first play should come
from official competition records wherever available. A scheduled start, date
printed inside a file, author-controlled commit date, later settlement or later
GitHub import does not suffice. All captures must be real files inside the repository;
external paths, missing sources and changed hashes fail closed. Private original
exports should be reviewed/redacted appropriately before committing any capture.

`identity` contains exactly these fields:

```json
{
  "event_id":"EXAMPLE-OFFICIAL-EVENT-ID",
  "market":"HANDICAP",
  "selection":"HOME",
  "line":"-1.5",
  "period":"FULL_GAME",
  "unit":"POINTS",
  "overtime":"INCLUDED",
  "probability_basis":"CONDITIONAL_DECISIVE",
  "origin":"USER_SUPPLIED"
}
```

Allowed markets: `WINNER`, `HANDICAP`, `TOTAL`, `PROP`. Use an empty line for an
unlined winner contract. Handicap magnitude **and sign** must appear in the original
literal contract. Canonical endpoint terms must be consistent across recovered
forecasts, results and benchmarks; no unit/period/overtime substitution is allowed.
`origin` is `USER_SUPPLIED`, `ANALYST_ALTERNATIVE` or `UNKNOWN`.
`probability_basis` is `UNCONDITIONAL_BINARY`, `CONDITIONAL_DECISIVE` or `THREE_WAY`;
three-way rows are retained but unscored by this binary protocol. Only user-supplied
lines enter the paired primary comparison. Missing numeric probabilities can still
support authentic ranked accuracy, but never a fabricated Brier score.

## Strict chronological algorithm study

This is a separate retrospective study, not recovery of the original algorithm.
Input CSV fields are `row_id,capture,proof`; the last two cells contain JSON objects
in the reference/review formats above. The feature capture contains:

```json
{"row_id":"R00001","available_at":"2026-01-01T09:00:00Z","values":{"EXAMPLE_feature":0.25}}
```

Its proof additionally requires `pre_event_data_verified: true`. Feature names
must be identical across rows; values must be finite. Reviewers must verify the
source data and feature engineering were available by the actual original issue
cutoff. Unknown feature/label availability is rejected rather than assigned a lag.
Each row must have Tier A and an independently verified decisive result whose
outcome proof also has `availability_time_verified: true`. Logistic
regression uses fixed L2=1 and at least 30 distinct prior events, excludes the entire
test event, and trains only on features **and outcomes** available strictly before
the test issue time. It performs no test-outcome hyperparameter selection. Warm-up
abstentions remain in predictions. Its training base rate is explicitly a
retrospective model-study comparator, never a historical frozen benchmark.

The strict backtest command does not change card probabilities or rankings and
does not promote a model. To verify a study, repeat it into a new directory from
the pinned inputs and compare all output bytes and manifest hashes. Feature-table
hash, evidence input hashes, model code and outputs are included in its manifest.

## Current-method prospective evidence

Track P remains ONE-CHAT-v3 / v27.0. Its sealed registry and 400-game sequential
protocol are unchanged. The 17 November implementation snapshot has zero registered
qualifying games and `NOT_YET_DEMONSTRATED`; use the current one-chat command with
its required intake/outcome arguments (see `python -m ml one-chat score --help`)
for later updates. Never add H counts to P, pool their verdicts, or infer that a
historical result validates the current method.
