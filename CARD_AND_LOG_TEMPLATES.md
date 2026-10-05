# Card and log templates

**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

Current authority: [CURRENT_RULES.md](CURRENT_RULES.md), MDS-2026.10.01-v7.1. Requested research uses the following template and receives a canonical ID regardless of calibration. Later sections describe the separate frozen certified-issuer protocol; its gates do not block requested research.

## Requested research card — default workflow

Prepare JSON with `event_key`, `native_event_id` (unknown if not verified), `league`, `title`, `tracking_handle`, `analysis_status`, `source_path` and full Markdown `body`. Body: exact fixture/time/state and source update time; supplied contracts and sporting/operator semantics; posted participants; season/recent/exposure/bullpen/environment evidence; ranked four picks and potential winner; rationale and failure routes; calibration/assumption/missingness labels; full sources and retained receipts. Use `UNCALIBRATED_QUALITATIVE` and `NOT_ESTIMATED` for unsupported percentages. Analyst scenarios may contain explicit uncalibrated reproducible estimates.

Run `py -3.14 -m research.operations.log_card commit card.json`, then `verify`. Retain actual log time, original source bytes and exact projection. Import original cards literally beneath a dated canonical correction; do not retroactively rewrite probabilities, claim times or fabricate missing ranks. Part 6 is the destination; existing events retain their ID for dated additions. No retrospective until requested.

## Complete universe

A retained `event-universe-1` JSON has `captured_utc`, nonempty hashed `source_refs`, and every relevant event: lane, league, season, durable event_id, home/away, scheduled_start_utc, endpoint and period. Capture and registration precede issuance. Register all fixtures before selecting successful candidates. Append an evidence-backed abstention for every omitted fixture. A model-only provider surrogate belongs to daily research coverage, not a live official-ID universe.

## Evidence bundle

The version is `forecast-evidence-1`. Required identity includes lane, league, season, event_id, exact home/away, model_version, endpoint, scheduled_start_utc, data_cutoff_utc and issued_utc. Registries are pinned by hash. Every input artifact has path, SHA-256 and available_utc no later than cutoff. Model/card/baseline distributions have exact event, endpoint, cutoff and input checksum plus retained score states. Contracts specify market, side, line, period, endpoint and void rule. No missing field is filled by narrative.

Attach three agreeing pregame body receipts with exact source/parser, league scope, official owner, retained content hash, independent upstream audits and event-specific lineage audits. Unknown collector independence blocks issuance. Source states must be fresh within the registered cap of at most five minutes. Actual-start evidence is added only after the event.

An adjustment requires an approved method version, reason, frozen parameters and pre-cutoff hashed evidence. `NONE` leaves the distribution unchanged. Do not supply subjective percentages or counterfeit source URLs to make a template pass.

## Issued core

The issuer's Markdown includes permanent P-ID, exact event/endpoint, issue/cutoff/start times, model version, model/input/registry hashes, source lineages, contract rows with coherent win/push/loss masses and separate p_model/p_card/p_baseline, adjustment status and transaction ID. Rendered ordering follows p_card. The machine bundle is immutable; the Part 6 projection and canonical ledger bind its bytes.

A preparation is **PREPARED_DRAFT_NOT_ISSUED** and consumes no ID. A committed pregame card is **ISSUED_PENDING_TERMINAL_ADMISSION**. Existing issued forecasts retain their own original format and ranking arithmetic.

## Research diagnostic addendum and mini closure

Bind the existing canonical ID/event, immutable original source/projection hashes, actual observation/review time, exact endpoint and each original source version. Retain conditional grade, operator definition status, actual-start admission, audited terminal-lineage status and performance eligibility separately. UNKNOWN_DEFINITION, UNRESOLVED_PERIOD, UNRESOLVED_PROVIDER_FIELD and missing p/baseline remain literal missingness; NO_FORECAST and late/live classifications remain unchanged. List every unresolved requirement in carryover. A diagnostic addendum does not create an ISSUE or certified settlement record.

An archive receipt binds original length/hash, archive path/hash, preserved-body offset, canonical entry mappings, overlap/addendum disposition, carryover and actual next-ID readback. Closure allocates no ID for an already represented event. Remove redundant working copies only after exact archive/readback checks.

## Settlement revision

Add exact final native body receipts, three independent agreeing terminal collectors, actual-start receipt and supporting field semantics. `append_settlement_revision` derives W/L/P from the fixed contracts and final scores. Each revision records reason, revision number, previous revision hash and unchanged issue-core hash. A disputed score, unknown actual start, wrong period or incomplete source quorum stays unresolved and outside performance scoring.

## Retrospective

For each event record: observed endpoint/outcome; issued probability and baseline literal; diagnostic surprise without claiming certainty; source, timing and contract validity; predeclared mechanism that occurred; mechanism that did not occur; adjustment vs model effect; and the next testable hypothesis. Review wins under the same evidence criteria as losses. Postgame awards, season-end knowledge and narrative explanation are postgame information.

## Model-only research

Daily shadows contain no P-number, no issued card, no researched lineup claim and no performance-eligible row. Include their family/version, probability vector, input/body/build hashes, forecast/cutoff times, fixture state and provisional source quality. Report all frozen and abstained fixtures in coverage. A diagnostic grade remains a diagnostic grade until separate live admission gates pass.

## Experiment forecasts and canonical cards

The [experiment protocol](research/experiments/NEXT_STEPS.md) defines separate development artifacts and actual-timestamp forecast journals. Creating a draft, power plan, experiment lock or measured result never allocates a P-ID or backfills a historical card. Requested game cards still use the canonical Part 6 workflow independently of calibration. Retain original `p`, ranking `q`, targets and issued versions; experiment probabilities are PMFs, and `q` is not scored as an event probability.
