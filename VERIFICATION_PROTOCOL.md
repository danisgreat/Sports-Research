# Verification protocol

Current authority: [METHOD.md](METHOD.md). Run checks from the repository root with the pinned Python environment.

```powershell
python -B -m pytest -p no:cacheprovider research/tests -q
python -B -m research.src.archive validate
py -3.14 -B -m research.operations.verify_custody
py -3.14 -B -m research.operations.log_card verify
py -3.14 -B -m research.operations.control_freeze --verify
py -3.14 -B -m pytest -p no:cacheprovider research/operations/test_log_card.py -q
```

The automated acceptance receipt covers original issued Part 1-5 bytes, the frozen Part 6 source block, historical tuning/holdout/shadow bytes, current model dependency/runtime checks, the historical learning view, source-body receipts and no live promotion. Archive validation checks every indexed raw CSV, canonical output, receipt body and implementation hash, and score arithmetic/admission invariants. The active freeze manifest covers root controls, research code/data/receipts and the archive manifest; the archive manifest chains the full archive data scope.

Canonical bulk CSVs are local regenerable exports and can be ignored for publication while their hashes and coverage remain in the archive manifest. Restricted or odds-bearing benchmark raw files are intentionally excluded from publication. Retained raw source paths and their hashes remain in individual data receipts. A fresh checkout missing a restricted local file must report the gap, not download it through an unauthorized route or substitute different bytes.

Run live-source jobs separately from tests. Record source failures with time and reason. A reachable page is not event-specific evidence, and distinct publishers do not automatically constitute independent lineages.

Historical links and receipts retain their original scope. Current active documents link to the present workflow. Freeze changes once, verify after writing, and put the freeze's own hash in the living status register. Verification output written after freeze lives in the explicitly excluded verification directory to avoid self-reference.

The current receipt is selected by METHOD. The current operations verifier reuses the frozen inventory/normalization module with that filename, current method/control metadata and the ledger-custodied research store excluded. It never edits a dependency pinned by the four model builds. The original control_manifest command addresses receipt 1. The earlier settlement audit receipt verifies its state at that earlier pass; subsequent canonical imports and current administrative headers have their own dated repair receipt. Do not rerun a historical next-P-523 expectation as if it were the current ID state.

The current custody wrapper recognizes the imported NPB receipt's content_sha256/stored_snapshot_path fields and verifies the same original bytes in memory. It does not rewrite source receipts or claim independent collection. Research commits remain separate from certified ISSUE records, and their exact projections and original sources are verified. A passing mechanics check establishes neither calibration nor source truth.
