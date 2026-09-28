# Prospective evidence-record contract

**Version:** 1. **Purpose:** an append-only, machine-readable record for a forecast decision and its later settlement. Markdown remains the human-readable record; this JSON is the evidence join used by the scoring and progress gates. Shape validation alone never grants performance eligibility.

The normative structure is [prospective_record.schema.json](prospective_record.schema.json). The initially empty admission file is [prospective_records.json](prospective_records.json). Run:

```powershell
python tools/semantic_validation.py research/settled_rows_2026-09-28/prospective_records.json
python tools/evidence_status.py
python tools/skill_baseline.py
```

## Required v1 record fields

Every record must carry the complete field set below. The JSON Schema checks shape and types;
tools/semantic_validation.py checks meaning; tools/prospective_eligibility.py joins that record
back to the human ledger and independently applies the issue, settlement, baseline, and RM-1 gates.
A valid JSON object alone never becomes an eligible result.

| Group | Required fields | Meaning and rule |
|---|---|---|
| Version and identity | schema_version, event_id, event_cluster_id, forecast_id, card_id, decision_id, target_id, contract_id | Version is 1. IDs are separate, stable keys: an exact official event, a cluster for same-event uncertainty, immutable issue snapshot, human card, one scored choice, outcome being forecast, and exact settlement contract. One decision cannot be duplicated within a forecast. |
| Event scope | sport, competition, season, participant_ids | Store the exact competition and season plus at least two distinct, nonempty official participant IDs. Display names are not identity keys. |
| Contract | contract, contract_spec | Human label plus structured terms: measure, period, line, side, units, overtime_rule, draw_rule, push_rule, void_rule, action_rule, and contract_version. line is a finite number or null; all rule terms are explicit strings. |
| Selection and time | rank, horizon, input_cutoff_utc, input_availability_latest_utc, issued_at_utc, event_start_utc, preferred_at_issue, selection_policy_version | Rank is a positive integer. Timestamps are timezone-aware ISO-8601 values. Pregame eligibility requires latest input ≤ cutoff < issue < actual start and at least three distinct issue-source lineages observed by the cutoff. Preferred status is frozen before result publication; it is never inferred from probability direction or outcome. |
| Forecast object | distribution_id, distribution_type, distribution_sha256, probabilities, q, q_semantics | Store the versioned distribution identity and content hash, complete W/P/L masses, and V only when void is explicitly modelled. Every mass is finite in [0,1] and the total is 1. q may be null; its meaning must be declared. RM-1 requires ROW_CALIBRATED_NOT_JOINT, so q is not a marginal or joint event probability. |
| Baseline and model | baseline, method_version, method_sha256, control_sha256, manifest_sha256, ranking_model_version, ranking_model_sha256, ranking_model_code_sha256 | Baseline has a status, probability/vector as applicable, version, same event/target/contract/horizon/input cutoff, and a training cutoff no later than the frozen input cutoff. Each hash is a 64-character SHA-256 hex digest. RM-1 coefficient and executable hashes must match the shipped code and reproduce the recorded q. |
| Settlement revision | settlement_revision_id, observed_value, result, outcome_verified, issue_receipts, terminal_receipts | Verified results require an observed value and resolved W/P/L/V category. A corrected label creates a new settlement revision; it never rewrites the issued forecast. Terminal receipts identify the same event, result and terminal state, retain source reference, retrieval timestamp and response hash, and must contain at least three distinct upstream lineages observed after event start. |
| Pairing and cohort weight | complementary_pair_id, covering_pair_id, target_weight, missingness | Use pair IDs to connect forced complements or covering contracts; null means no such relationship. Target weight is finite and positive. Missing fields are represented with explicit status/reason in missingness, never filled with a guessed value. |

The full field spelling, type, required/nullable rules, and nested receipt shapes are authoritative in
the JSON Schema. The semantic validator's REQUIRED set is regression-tested against the schema's
required properties so the machine gate and written contract cannot silently drift apart.

## Identity and grain

One `records[]` object is one issued target decision at one forecast freeze and one settlement revision. Keep the identities separate:

- `event_id` is the exact league/organizer event identifier; `event_cluster_id` groups all rows from the same sporting event for uncertainty and equal-event weighting.
- `forecast_id` identifies the immutable forecast snapshot; `card_id` names the human card; `decision_id` uniquely identifies the scored selection; `target_id` names the outcome being predicted; `contract_id` pins period, line, side, units, overtime, push, void and action terms.
- A later corrected label gets a new `settlement_revision_id`, points to the superseded revision, and explains why. Never rewrite issued probabilities or preferred-selection state.

Store competition, season and participant IDs when available. Human-readable team names alone do not establish event identity. Two opposite sides of a forced pair are separate contract rows, share a target and forecast, and are linked in `complements`; count the frozen preferred side once in a binary decision score. Distinct nested lines keep distinct target IDs while sharing the event cluster.

## Required evidence and timing

Record the timezone-aware `input_cutoff_utc`, latest input availability, issue time and verified event start. A prospective pregame row requires latest input ≤ cutoff < issue < event start. Issue receipts must identify the event, show pregame state and start time, retain the source URL/reference, retrieval time, response hash and upstream lineage. Terminal receipts must identify the same event, contain a terminal result/status, and be observed after event start. The semantic gate deduplicates upstream lineages; three copied pages do not become three sources.

Declare a complete `probabilities` outcome vector: W/P/L, plus V only when void is a distinct modelled category. Every mass must be finite, between zero and one, and sum to one. Store `q` only with its interpretation. RM-1's value is `ROW_CALIBRATED_NOT_JOINT`; it is not a marginal event probability and its product is not a joint-success estimate. Push-capable records are excluded from the present binary baseline ledger until a vector-aware paired ledger is implemented and validated.

`preferred_at_issue` must be frozen from the pre-result selection policy. Never infer it from whether p is above 0.5, which side won, or a settlement-time rank. Baseline p needs the same exact event, target, contract, horizon and cutoff plus a training cutoff earlier than the frozen input cutoff; missing or unavailable means missing, never 0.500.

## Eligibility is derived, not authored

There is intentionally no trusted `performance_eligible: true` field. `tools/prospective_eligibility.py` recomputes whether a record clears semantic, issue/settlement, baseline, exact-join, model-build and source-lineage checks. The Markdown ledger must cite `prospective_records.json#<decision_id>`; every scored card probability, baseline, result, rank and contract must match that record. The rules fail closed and return exclusion reasons.

The structured register is currently empty. The historical extractor's rows do not contain enough surviving issue-time identity, time, source and freeze evidence to be upgraded into this schema by inference. Its generated CSV is a descriptive legacy view only.
