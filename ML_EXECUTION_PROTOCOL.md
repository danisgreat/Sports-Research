# ML execution, research retention and future learning

**ML/RL scope (MLSCOPE-v3).** Owner instruction, 22 October 2026 (second instruction of the day, adopting the framework revamp review): models run where they are needed and a competition's declared reference model runs **before** the card. For a tier A competition whose declared reference is its release (NHL, MLB), prompt 1 freezes the model first (`python -m ml pregame reference`) and the card starts from that frozen number; where another reference is declared (the NBA's TB-2-MD) the release is frozen the same way as a challenger. Tier B and C competitions start from TB-2-MD, TB-1-MD or the league-only baseline (`python -m ml reference run`). The analyst's `p_card` (ANALYST_PRIMARY_V1) is that reference plus logged adjustments with sizes from the effect tables ([REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md), [ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md)); a frozen reference is never edited, and the card's own final p is frozen beside it by `python -m ml pregame run`. If no reference could run first, the model is only a post-card shadow and the card says so. Prompt 3 settles the card, then the frozen rows; prompt 6 ingests and evaluates; prompt 8 builds releases and decides promotion. A model is judged only on frozen, pushed, pre-start rows after at least 8 settled weeks and 50 settled paired games; a progress review falls due when either is reached first. A release is frozen for a season and edits outside the cycle's import closure never retire it. RL has no forecasting role: the online expert weighting that updates at settlement is online learning. Supersedes MLSCOPE-v2 (card first, model never feeds the card), MLSCOPE-v1 and NOCODE-v1 for cards under P-2026.10.22-v24.0 and later; earlier cards keep their method.

**Executable forecast cycle (CYCLE-v1).** Defined in [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md); summarised in [CORE](CORE.md) §7.

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**EXEC-2026.10.16-v2 · MDS-2026.10.16-v20.0 · CR-2026.10.16-R7 · P-2026.10.16-v20.0.** [RESEARCH_RETENTION_PROTOCOL](RESEARCH_RETENTION_PROTOCOL.md) controls recording/import independently of ML availability. This explicitly replaces EXEC-v1's missing-receipt issuance block. Use [GitHub main](https://github.com/danisgreat/Sports-Research/tree/main) when local repository files are inaccessible, under GITHUB_REFERENCE_PROTOCOL.

## 1. Execute when available, retain regardless

Attempt a supported actual primary run when accessible. Missing ML/RL adapter, ml module/interpreter, dependency/history/baseline/calibration or run receipt never by itself blocks a local-key research record or later prompt-4 canonical import. Use RESEARCH_ONLY_NO_MODEL with supported analyst_p/qualitative work and honest real timing; model p_card stays NOT_ESTIMATED. Record actual failures or NOT_RUN_CAPABILITY_BLOCKED / NOT_IMPLEMENTED / NOT_RUN_DATA_UNAVAILABLE. Never invent a successful run or a file to pass a check. Identity/ID/custody/write constraints remain.

```text
python -m ml primary execute --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --out ATTEMPT
python -m ml primary verify-execution --attempt ATTEMPT
python -m ml primary verify-log --manifest ML_EXECUTION_MANIFEST.csv --mini MINI.md
```

An actual execute attempt retains STARTED/INPUTS/EXECUTION and a successful BUNDLE where applicable. It fits its comparator from reviewed exact-competition history without a pre-existing profile. Real failed attempts exit nonzero. An interrupted attempt cannot be claimed successful; an honest no-model record can still be retained. Numerical V3 semantics and source admission are unchanged.

## 2. Honest manifest for each new card

New minis use mini-log-10 / mini-settlement-10; existing minis remain in their original format. Preserve the registered CSV header:

```csv
card_id,event_id,competition,endpoint,execution_path,execution_sha256,feedback_status,feedback_path,feedback_sha256,reason
```

For no actual bundle/attempt, leave execution_path/execution_sha256 empty; set feedback_status=NOT_APPLICABLE_NO_MODEL, blank feedback paths/hashes and the concrete reason. This is a valid research-only disposition, including a real No module named ml capability error. Do not place a nonexistent path in the manifest. If a path/hash is provided it must verify. MODEL_ASSISTED_PRIMARY_V3 requires actual successful execution. C21 verifies honesty and scope, not universal model availability. The verifier accepts mini-log-8/9; legacy formats use their original checks and explicit new record/disposition readback.

## 3. Settle every event and retain future targets

Canonical retention-only import can precede settlement. Preserve original card sources and timing; unreviewed outcomes stay PENDING_SETTLEMENT / OUTCOME_NOT_REVIEWED. Later settle the original contracts under the original local key, or the same mapped P-ID after prompt 4 with source/time/definition/revision evidence, regardless of whether a model existed.

For future model development, retain verified terminal labels and original research locally by local key; after prompt 4 assigns and verifies the canonical mapping, export RESEARCH_TRAINING_CANDIDATE with ml.research_learning under RESEARCH_RETENTION_PROTOCOL. Unknown features/known-at facts remain explicit; future training admission, deduplication, scope and effective revisions are separate. No model is required to retain these targets.

Only an actual original frozen model bundle supplies per-expert losses:

```text
python -m ml primary settle --bundle ATTEMPT/BUNDLE --home-score HOME --away-score AWAY --final-at ISO --available-at ISO --evidence CAPTURE --evidence-sha256 SHA256 --out NEW_FEEDBACK.csv
```

Keep actual expert feedback retained/pending/blocked dispositions where a model exists. Without a model, NOT_APPLICABLE_NO_MODEL applies to expert losses only; the event remains eligible for future source-reviewed label retention. Never backfill old predictions, Brier losses, propensities or rewards. Candidate targets cannot enter primary feedback directly.

The actual mechanism remains supervised scoring models plus Hedge, not a trained environment-control RL agent. Research IDs, source truth, numerical forecasting, training admission and prospective qualification are separate. All eleven game workflows and all eight lifecycle prompts follow this distinction.

**Local research record and updated-document delivery (owner update, 16 October 2026).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](CORE.md) §2.

