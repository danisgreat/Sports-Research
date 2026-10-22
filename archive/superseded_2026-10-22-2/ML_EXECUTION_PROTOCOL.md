# ML execution, research retention and future learning

**ML/RL scope (MLSCOPE-v2).** Owner instruction, 22 October 2026: models run where they are needed, beside the analyst card and never inside it. Prompt 1 researches the game online and prices every p_card as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY from one declared distribution ([PROBABILITY_TOOLKIT](PROBABILITY_TOOLKIT.md); code may do the arithmetic, with every input and step printed). Only after the card is written to the mini does prompt 1 run the pregame model shadow, which freezes the model and league-baseline rows, and the card's own p_card, on the same contracts when the competition has an active release, or records NOT_RUN_NO_RELEASE. Model output never changes a card's p_card, ranks or picks. Prompt 3 settles the shadow with the card; prompt 6 ingests and evaluates; prompt 8 builds releases and decides promotion. A model is judged only after at least 8 weeks and 50 paired games; a progress review falls due when either is reached first. RL has no forecasting role: online expert weighting updates at settlement. Details: [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md). Supersedes MLSCOPE-v1, NOCODE-v1 and any older text that forbids code or models in prompts 1–5.

**Executable forecast cycle (CYCLE-v1).** Apply [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md). New contextual forecasts use MODEL_ASSISTED_CYCLE_V1 with a frozen exact-competition release, actual execution receipt, identical-contract baseline shadows and verified settlement feedback. Existing V3/tennis adapters retain their own cohorts; missing/unsupported inputs require a real failure receipt and retained research. This statistical/procedure release authorises experimental execution, not predictive qualification.

**Local keys until settlement; updated mini after every game (MINI-v2).** Apply [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md). Research and mini creation (prompts 1–2) use stable local event keys and never assign or reserve canonical P-IDs. A canonical P-ID is assigned only in an event's settlement phase: prompt 3 settles the event and then runs the prompt-4 import, which assigns the ID. After each prompt-1 game request the repository agent appends the card to the active mini under `research/active_minis/`, updates intake and footer, reads the file back, and commits and pushes it. Preserve every owner-entered Upcoming game block and all earlier issued bytes. Formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

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


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Append the researched card regardless of model availability, update intake and the local footer, read the full mini back and commit it after each game request (ENV-v2). Canonical IDs are assigned only in the settlement phase, when prompt 3 hands the settled event to the prompt-4 import, which reconciles duplicates and identity and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.
