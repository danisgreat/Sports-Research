# ML execution, research retention and future learning

**EXEC-2026.10.16-v2 · MDS-2026.10.16-v17.0 · CR-2026.10.16-R1 · P-2026.10.16-v17.0.** [RESEARCH_RETENTION_PROTOCOL](RESEARCH_RETENTION_PROTOCOL.md) controls recording/import independently of ML availability. This explicitly replaces EXEC-v1's missing-receipt issuance block. Use [GitHub main](https://github.com/danisgreat/Sports-Research/tree/main) when local repository files are inaccessible, under GITHUB_REFERENCE_PROTOCOL.

## 1. Execute when available, retain regardless

Attempt a supported actual primary run when accessible. Missing ML/RL adapter, ml module/interpreter, dependency/history/baseline/calibration or run receipt never by itself blocks a researched P-ID or canonical import. Use RESEARCH_ONLY_NO_MODEL with supported analyst_p/qualitative work and honest real timing; model p_card stays NOT_ESTIMATED. Record actual failures or NOT_RUN_CAPABILITY_BLOCKED / NOT_IMPLEMENTED / NOT_RUN_DATA_UNAVAILABLE. Never invent a successful run or a file to pass a check. Identity/ID/custody/write constraints remain.

```text
python -m ml primary execute --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --out ATTEMPT
python -m ml primary verify-execution --attempt ATTEMPT
python -m ml primary verify-log --manifest ML_EXECUTION_MANIFEST.csv --mini MINI.md
```

An actual execute attempt retains STARTED/INPUTS/EXECUTION and a successful BUNDLE where applicable. It fits its comparator from reviewed exact-competition history without a pre-existing profile. Real failed attempts exit nonzero. An interrupted attempt cannot be claimed successful; an honest no-model record can still be retained. Numerical V3 semantics and source admission are unchanged.

## 2. Honest manifest for each new card

New minis use mini-log-9 / mini-settlement-8; existing minis remain in their original format. Preserve the registered CSV header:

```csv
card_id,event_id,competition,endpoint,execution_path,execution_sha256,feedback_status,feedback_path,feedback_sha256,reason
```

For no actual bundle/attempt, leave execution_path/execution_sha256 empty; set feedback_status=NOT_APPLICABLE_NO_MODEL, blank feedback paths/hashes and the concrete reason. This is a valid research-only disposition, including a real No module named ml capability error. Do not place a nonexistent path in the manifest. If a path/hash is provided it must verify. MODEL_ASSISTED_PRIMARY_V3 requires actual successful execution. C21 verifies honesty and scope, not universal model availability. The verifier accepts mini-log-8/9; legacy formats use their original checks and explicit new record/disposition readback.

## 3. Settle every event and retain future targets

Canonical retention-only import can precede settlement. Preserve original card sources and timing; unreviewed outcomes stay PENDING_SETTLEMENT / OUTCOME_NOT_REVIEWED. Later settle the original contracts under the same P-ID with source/time/definition/revision evidence, regardless of whether a model existed.

For future model development, retain verified terminal labels and original research as RESEARCH_TRAINING_CANDIDATE with ml.research_learning under RESEARCH_RETENTION_PROTOCOL. Unknown features/known-at facts remain explicit; future training admission, deduplication, scope and effective revisions are separate. No model is required to retain these targets.

Only an actual original frozen model bundle supplies per-expert losses:

```text
python -m ml primary settle --bundle ATTEMPT/BUNDLE --home-score HOME --away-score AWAY --final-at ISO --available-at ISO --evidence CAPTURE --evidence-sha256 SHA256 --out NEW_FEEDBACK.csv
```

Keep actual expert feedback retained/pending/blocked dispositions where a model exists. Without a model, NOT_APPLICABLE_NO_MODEL applies to expert losses only; the event remains eligible for future source-reviewed label retention. Never backfill old predictions, Brier losses, propensities or rewards. Candidate targets cannot enter primary feedback directly.

The actual mechanism remains supervised scoring models plus Hedge, not a trained environment-control RL agent. Research IDs, source truth, numerical forecasting, training admission and prospective qualification are separate. All eleven game workflows and all eight lifecycle prompts follow this distinction.


**Model use and mandatory running-log record (owner clarification, 16 October 2026).** Use the supported ML/RL mechanisms when they are available for the exact sport, competition and endpoint. Whether a model exists or not, assign the reconciled permanent P-ID, append the researched game card to the active running mini-log, read it back and advance its footer. A missing sport-specific model must not leave an otherwise recordable game as intake-only, unissued or without an ID. With no verified model output, record RESEARCH_ONLY_NO_MODEL, the actual reason and supported analyst work; never invent model probabilities or receipts. Carry that same P-ID through verified canonical import; do not allocate another ID. Before an authorized import, the local card may truthfully say PENDING_IMPORT; that status never cancels its ID or running-log entry. Identity/allocation conflicts, frozen or inaccessible originals and real write failures still block only the affected mutation. Verified settlements remain available for future model development in both paths.

See [RETAIN-v1](RESEARCH_RETENTION_PROTOCOL.md). This is an editorial clarification of the existing two-path behavior; no model, numerical policy or format change.
