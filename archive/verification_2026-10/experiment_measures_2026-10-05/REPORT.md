# Fifteen experiment measurement implementation

Local working files are authoritative. This implements the user's request to add measures for all fifteen proposed experiments and provide every next step. Opening main commit: `cf3453eb9b1b2e964b256950f68da70485d0929f`.

## Delivered scope

All fifteen original proposals have source-bound executable definitions in the [protocol catalog](../../experiments/protocols_v1.json) and [measure register](../../experiment_measures.json). Their hypothesis text, original `PROPOSED_NOT_TESTED` status and false performance eligibility are retained. Eleven proposals come from the original improvement register and four from the later all-log review. No proposal is omitted or duplicated.

The implementation supplies paired contract Brier/log-loss scoring, predictive-distribution CRPS, central interval coverage and interval scores, fixed-bin reliability, paired week-block uncertainty, a fifteen-comparison family, separate-pilot sample planning, exact contract checks, immutable development locks, real-time forecast capture and complete cohort readback. Experiment-specific checks cover live baseball states, scenario probabilities, joint score marginals, overtime winner conversion, original model/card artifacts, exact supplied/ranked contracts, replacement/rest inputs and football phase/provider records.

The [complete next-step guide](../../experiments/NEXT_STEPS.md) contains a separate measures/actions row for each of P-492 and P-524–P-537, the shared eight-stage execution sequence, artifact schemas and CLI commands. The [registration readiness](readiness_at_registration.json) preserves missing inputs for every experiment. A filled template is validated again at freeze; presence alone does not establish valid evidence.

**Measurement infrastructure is implemented; zero real experiments are frozen or run.** Candidate/comparator models, source-backed feature datasets, untouched future cohorts, separate pilot scores, audited adapters/dependence and justified tolerances must be supplied. No numeric forecast, feature coefficient, sample size or improvement result has been fabricated. Synthetic fixtures exercise code only and are stored solely in temporary test directories.

## Document and custody integration

Ten existing current documents link the same canonical catalog and next-step guide: METHOD, CURRENT_RULES, SCORING_AND_VALIDATION, VERIFICATION_PROTOCOL, CARD_AND_LOG_TEMPLATES, both READMEs, LEARNING_REGISTER, LEARNINGS_INDEX and CHANGELOG. [Final document changes](document_changes_v2.json) retain their opening/current hashes; the [first draft hashes](document_changes.json) also remain. This adds no redundant operating manual.

The selected control revision is `CR-2026.10.05-I8`, with [receipt 8](../../../CONTROL_MANIFEST_2026-10-05-8.md). The first draft receipt 7 is retained before the final integer joint-score correction. Experiment run stores are excluded from the living inventory and instead have pinned lock/code/model references, hash-chained forecasts and versioned evaluation outputs. Existing model-pinned source modules and earlier receipts are unchanged. CI now executes the experiment tests and verifies exact fifteen-proposal catalog coverage even if another gate fails.

The [opening inventory](opening.json) protects 104 artifacts, including all six logs, the canonical ledger, issued/research records, original proposal registers, model builds and frozen source modules. [Readback](readback.json) verifies their original bytes, catalog coverage, newly added local document links, zero real run artifacts and the allocator's next ID. Its link check covers the added sections and the complete new guide/report; inherited historical link breaks are listed explicitly rather than rewritten or described as resolved. No canonical ID is consumed; the next remains P-538.

## Validation

The first focused experiment suite passed 42 tests; its full suite passed 169. Three further joint-score tests reject fractional team scores and boolean/string matrix entries, and the original-model sporting supports are checked too. The final full suite passed **172 tests**, and all nine local check commands succeeded. The [final local checks](local_checks_v3.json) contain exact commands, UTC times, return codes and output for the corrected full regression suite, proposal/catalog verification, canonical storage, source custody, reconciliation, control freeze and all-log readback. The [first check run](local_checks.json) also remains: its initial link scan encountered inherited historical breaks. The [second version](local_checks_v2.json) records the corrected link scope and retained unchanged results. The final version reruns the complete suite after the joint-score code correction. These checks establish software/custody mechanics, not model skill or independent sporting truth.

The new tests independently check proper-score formulas and CRPS, push mass, zero-probability outcomes, paired event weighting, reproducibility, sample planning beyond the worthwhile threshold, immutable capture, no pending-member removal, contract/start conflicts, model/code mutation, joint score consistency, NHL conditional overtime, opener artifact retention, football record matching, live-state bounds, ranked contract substitution, impossible negative totals and a missing entire forecast journal. A complete synthetic result can reach statistical review while performance admission remains false; equal models retain the baseline.

Existing clean-checkout limitations remain material: 52 mandatory source bodies are present only in ignored local storage, and 152 ignored local cache files are included in the control inventory. A clean GitHub checkout therefore cannot pass those two gates. The all-log checker also requires the retained KFU owner body. These gaps are reported and have not been waived or replaced by fabricated bytes. Publication and its actual workflow outcome must be checked against the pushed commit.

## Interpretation limits and next work

Hash matches and declared normalized timestamps do not independently prove original publisher availability, official truth or independent collection. Adapter checks validate retained expectations/results and code/body hashes; they do not rerun arbitrary external parsers. Pilot inputs need original event-level provenance review. The power plan is a normal approximation conditional on reviewed block sampling, and the percentile intervals assume suitable exchangeable week blocks. Fixed-bin reliability is a descriptive functional, not proof of complete calibration. These limits appear in the guide, protocol and result readback.

For every experiment, complete the guide's sequence: audited inputs/adapters; named comparator/candidate and ablations; separate pilot and justified tolerances; reviewed sample/dependence plan; complete chronological future cohort; frozen lock and timed forecasts; all terminal dispositions; paired results and separate qualification review. The measurement runner never changes an issued forecast, original hypothesis, model build or operational admission state.

Method sources and their role are recorded in the [next-step guide](../../experiments/NEXT_STEPS.md): proper scoring definitions, paired bootstrap assumptions and multiple-comparison control.
