# Verification protocol

Current October-5 all-log custody: 111 receipt bodies verify locally; 52 are intentionally excluded from Git (42 prior benchmark bodies plus 10 new restricted/market-bearing narrative captures). A clean checkout has 59 bodies and must fail strict custody for the other 52; no CI bypass or fabricated recapture is authorized. See the all-log source inventory and publication evidence.

**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

Current authority: [METHOD.md](METHOD.md). Run checks from the repository root with the pinned Python environment.

October 5 repair evidence is retained in `research/verification/closure_2026-10-05/`. The CI job runs both regression suites, canonical projection/source verification, custody/acceptance checks and the selected freeze verifier. Checkout includes Git history because custody compares original committed blobs. Each verification step runs after earlier failures unless the workflow is cancelled, so custody failure no longer hides freeze results. No step uses continue-on-error. Root Markdown edits also trigger checks. Failure notifications report the job's actual failure; checks must be repaired rather than disabled. Mini archive readback verifies each preserved body using its recorded byte offset and SHA-256.

```powershell
py -3.14 -B -m pytest -p no:cacheprovider research/tests research/operations -q
python -B -m research.src.archive validate
py -3.14 -B -m research.operations.verify_custody
py -3.14 -B -m research.operations.log_card verify
py -3.14 -B -m research.operations.control_freeze --verify
py -3.14 -B -m research.operations.verify_reconciliation
py -3.14 -B -m research.operations.verify_all_logs
```

The automated acceptance receipt covers original issued Part 1-5 bytes, the frozen Part 6 source block, historical tuning/holdout/shadow bytes, current model dependency/runtime checks, the historical learning view, source-body receipts and no live promotion. Archive validation checks every indexed raw CSV, canonical output, receipt body and implementation hash, and score arithmetic/admission invariants. The active freeze manifest covers root controls, research code/data/receipts and the archive manifest; the archive manifest chains the full archive data scope.

Canonical bulk CSVs are local regenerable exports and can be ignored for publication while their hashes and coverage remain in the archive manifest. Restricted or odds-bearing benchmark raw files are intentionally excluded from publication. Retained raw source paths and their hashes remain in individual data receipts. A fresh checkout missing a restricted local file must report the gap, not download it through an unauthorized route or substitute different bytes.

Full custody is strict in every environment: the wrapper aggregates all missing, hash-invalid, length-invalid and malformed-receipt failures, retains nonzero failure, and restores its in-memory schema adapter after each run. At the October 5 implementation readback 78 bodies verify locally; 42 receipt bodies are intentionally local-only in ignored benchmark quarantine. A tracked-body export fails those 42 checks, rather than just reporting the first missing AFC body. [Complete local/publication inventory and outcomes](research/verification/implementation_2026-10-05/REPORT.md). The separate archive source-body gap disclosed by closure is not the same issue as Git omitting local benchmark bodies.

Run live-source jobs separately from tests. Record source failures with time and reason. A reachable page is not event-specific evidence, and distinct publishers do not automatically constitute independent lineages.

Historical links and receipts retain their original scope. Current active documents link to the present workflow. Freeze changes once, verify after writing, and put the freeze's own hash in the living status register. Verification output written after freeze lives in the explicitly excluded verification directory to avoid self-reference.

The current receipt is selected by METHOD. The current operations verifier reuses the frozen inventory/normalization module with that filename, current method/control metadata and the ledger-custodied research store excluded. It never edits a dependency pinned by the four model builds. The original control_manifest command addresses receipt 1. The earlier settlement audit receipt verifies its state at that earlier pass; subsequent canonical imports and current administrative headers have their own dated repair receipt. Do not rerun a historical next-P-523 expectation as if it were the current ID state.

The current custody wrapper recognizes the imported NPB receipt's content_sha256/stored_snapshot_path fields and verifies the same original bytes in memory. It does not rewrite source receipts or claim independent collection. Research commits remain separate from certified ISSUE records, and their exact projections and original sources are verified. A passing mechanics check establishes neither calibration nor source truth.

Publication readback: 152 ignored local cache files listed in the full local control freeze remain absent from Git. The first publication also had one workflow line-ending mismatch, corrected with byte-preserving Git attributes. Remote validation remains incomplete; the local freeze does not establish clean-checkout evidence availability. The exact paths are retained in `research/verification/all_log_resolution_2026-10-05/published_freeze_inventory.json`.

## Experiment-measure verification

Run `py -3.14 -B -m research.experiments.runner verify` and include `research/experiments` in regression tests. The [catalog](research/experiment_measures.json) must cover all fifteen original hypotheses with preserved source hashes, fixed target/feature/measure definitions and explicit pending inputs. Test arithmetic independently and exercise overwrite, data leakage, period/provider, duplicate, pending-cohort, PMF and code/runtime-custody failures. Synthetic test success is never an experiment result. Runtime experiment stores use their own source/lock/journal/result hashes; original model builds, forecasts and ledger remain protected.
