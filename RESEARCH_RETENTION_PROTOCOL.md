# Retain local research independently of model availability

**ML/RL scope (MLSCOPE-v1).** Owner instruction, 17 October 2026: ML/RL is not part of game research. Prompts 1–5 run no code, runtime pack, model, shadow or learning command and read no model output. Prompt 1 researches the game and derives every p_card by hand as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY, using [PROBABILITY_TOOLKIT](PROBABILITY_TOOLKIT.md) arithmetic with every input and step shown. Prompts 2–5 create, settle, import and roll over records by hand. ML/RL runs only in prompt 6 (combined-log retrospective: learning-store ingest, model feedback, shadow settlement and comparisons) and prompt 8 (workshop code, releases, shadows and promotion decisions). Its findings reach game research only as reviewed Markdown changes (toolkit constants, base rates, rules) released through prompt 8. This rule supersedes any older text requiring prompts 1–5 to run ML, CYCLE-v1, CHAT-EXEC-v1, a capability receipt, an execution manifest or a learning-store export.

**Executable forecast cycle (CYCLE-v1).** Apply [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md). New contextual forecasts use MODEL_ASSISTED_CYCLE_V1 with a frozen exact-competition release, actual execution receipt, identical-contract baseline shadows and verified settlement feedback. Existing V3/tennis adapters retain their own cohorts; missing/unsupported inputs require a real failure receipt and retained research. This statistical/procedure release authorises experimental execution, not predictive qualification.

**RETAIN-2026.10.16-v2 · MDS/P v19.2 · CR-2026.10.16-R7.** Owner update: prompts 1–3 retain researched events under stable local event keys. Canonical P-IDs are assigned only during prompt 4 import. After every prompt-1 game request, deliver the complete updated mini .md. This supersedes RETAIN-v1's pregame working/permanent P-ID assignment while preserving model-independent research retention, original source bytes, truthful timing and numerical PRIMARY_HEDGE_MIX_V3 policy.

Read [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md), [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md), [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md) and [PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md).

## 1. Local research and delivery before canonical allocation

Retain every identified researched event in the authorized mini under its stable LOCAL-<MINI_KEY>-G0001-style key. Do not assign/reserve a canonical number during research or settlement; use canonical ID NOT_ASSIGNED / PROMPT_4_IMPORT. Append the full card, update intake/manifest/queues and local footer, read back the complete mini and return the complete cumulative updated .md after each request. Missing ML, adapter, interpreter/module, baseline, calibration, data or receipt never by itself prevents the local research record or later canonical import. Duplicates/addenda retain their original key; existing canonical references keep their already assigned ID.

Use RESEARCH_ONLY_NO_MODEL where no verified fitted primary output exists. Keep model p_card NOT_ESTIMATED and supported analyst_p separately NOT_PRIMARY, with source-backed reasoning, assumptions/gaps and actual times/exposure. Incomplete required facts remain INFORMATION_INCOMPLETE under EXH-v1; retaining research is separate from full evidence completion. Never invent probabilities, execution, scores or pregame timing.

Only real event-identity/custody/lease/freeze/write conflicts block the affected append. Preserve independent research and return an honest complete separate draft if the mini cannot be safely updated. Do not reconstruct an inaccessible original. Follow MINI-v1's complete-document, duplicate and blocked-delivery rules.

## 2. Honest execution disposition without a fake receipt

Attempt a supported primary run when accessible. Retain actual success/failure bundles. If it cannot run, record NOT_RUN_CAPABILITY_BLOCKED, NOT_IMPLEMENTED or NOT_RUN_DATA_UNAVAILABLE with the concrete reason. Do not repeat a known capability failure indefinitely or fabricate an execution receipt.

ML_EXECUTION_MANIFEST.csv keeps its existing columns with one row per new card; card_id is the stable local key and event_id is the native/stable event identity. For no actual artifact leave execution_path/execution_sha256 blank, feedback_status NOT_APPLICABLE_NO_MODEL, feedback paths/hashes blank and a substantive reason. C21 accepts honest research-only disposition. Actual model claims require a verified successful bundle. verify-log supports mini-log-10 local cards and preserves legacy8/9 P-card support, without allocating a canonical ID.

New minis use mini-log-10 / mini-settlement-10. Old cores and formats remain unchanged; new local-key work in an old active mini follows the dated lifecycle-addendum rule. Canonical assignment/status never changes a frozen primary request, native event ID, probability, feedback row or hash.

## 3. Import may precede settlement; only prompt 4 assigns canonical IDs

An authorized prompt4 retention-only import can precede settlement or ML execution. Inventory all sources and reconcile exact events against canonical/native aliases; assign genuinely new canonical IDs contiguously only in the verified import plan, preserve already committed mappings/reserved ranges, and append literal local cores inside canonical wrappers. Record the complete local-key → canonical-ID map separately from frozen originals. Update actual highest/next only after successful append/readback. Duplicate/addendum/rerun consumes no new ID. Pending outcomes remain PENDING_SETTLEMENT / OUTCOME_NOT_REVIEWED, never invented finals or performance rows.

Prompt3 before import settles original local keys with canonical mapping NOT_ASSIGNED. After import the same original key has a verified canonical mapping; later revisions preserve that mapping in new evidence, never rewrite the source. New events after freeze go to the next authorized mini namespace. Existing issued legacy P labels remain literal and are mapped explicitly at import, never renumbered in place.

## 4. Two kinds of learning evidence

Future-development targets: retain verified final endpoints/grades, source/time/hash, original research/features, actual availability/exposure, effective revision and feature-admission status. Local prompt3 retains reviewed LABELS.csv and evidence by local key. The current research_learning exporter requires a canonical P-ID, so run it only after prompt4 verifies assignment, using mapped canonical original and settlement wrappers containing the unchanged local source. Do not allocate an early ID for an exporter.

```text
python -m ml.research_learning retain --card-id P-NNN --record CANONICAL_WRAPPER.md --settlement MAPPED_SETTLEMENT_WRAPPER.md --labels LABELS.csv --out research/training_candidates/P-NNN/revision-1
python -m ml.research_learning verify --candidate research/training_candidates/P-NNN/revision-1
```

LABELS.csv retains schema event_id,competition,endpoint,label_key,label_value,label_unit,event_at,final_at,available_at,source_url,evidence_path,evidence_sha256,definition_status,review_status,revision_id,feature_status. review_status is TERMINAL_LABEL_REVIEWED; units GOALS/POINTS/RUNS/GAMES/SETS/WICKETS/BALLS or OUTCOME (WIN/LOSS/PUSH/VOID). The exporter allocates no ID. Reviewed labels are RESEARCH_TRAINING_CANDIDATE / LABELS_RETAINED_NOT_MODEL_FEEDBACK. Independent future-training source/scope/point-in-time/effective-revision admission remains required; a trusted target does not establish pre-start feature availability or prospective skill.

Existing expert feedback: only an actually issued frozen expert bundle supplies its own loss via primary settle. Without one retain verified targets and mark expert feedback NOT_APPLICABLE_NO_MODEL. Never manufacture probabilities, propensities, losses or model feedback. Preserve one effective native-event contribution and existing warm/feedback deduplication.

**Candidate-to-training admission (LEARN-v1).** A verified candidate is linked into an immutable training release by `python -m ml training build --candidates research/training_candidates` when its event's structured research export has been ingested. A candidate without exported history is listed as CANDIDATE_WITHOUT_STRUCTURED_HISTORY, never dropped and never given invented features ([LEARNING_PIPELINE_PROTOCOL](LEARNING_PIPELINE_PROTOCOL.md) §5). Linking a label to features does not create expert feedback.

## 5. Counts and custody

Report local retained-card count, canonical imported-event count, numerical forecast coverage, feedback coverage and future-label export coverage separately. Local retention consumes only a local ordinal; prompt4 canonical import counts the mapped retained event even if qualitative/research-only. Analyst rows never inflate model T2/Brier/calibration/prospective cohorts. Existing cards, canonical state/IDs, issued ranks/grades, old formats and all prior source bytes remain protected. Check C2/C16/C21/C22 and S18 with actual evidence.
