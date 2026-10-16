# Retain research under P-IDs independently of model availability

**RETAIN-2026.10.16-v1 · MDS-2026.10.16-v17.0 · CR-2026.10.16-R1 · P-2026.10.16-v17.0 · SCV-2026.10.16-v11.** Owner instruction: store researched events under their reconciled P-IDs even when no ML/RL model, runtime, baseline or execution receipt exists, so verified settlements can support future development. Supersedes EXEC-v1's model-execution prerequisite for recording/import. It does not change the numerical PRIMARY_HEDGE_MIX_V3 policy or invent an RL agent.

## 1. Recording is independent of a numerical model

Retain every identified researched event in the authorized mini under the next reconciled working P-ID. A missing adapter, interpreter/module (`No module named ml`), dependency, input history, baseline, calibration or execution receipt must never by itself prevent a research card, ID consumption or canonical retention. Advance the local footer only after the actual card is written/read back. Canonical status follows verified append-only import; no numbering reset, duplicate, skipped outstanding sequence or guessed original.

Use **RESEARCH_ONLY_NO_MODEL** where no verified fitted primary output exists. Retain source-backed facts, exact requested contracts, actual times/exposure, substantive qualitative reasoning, supported `analyst_p` calculations, assumptions and gaps. Model `p_card`, gate and model metrics stay NOT_ESTIMATED/NOT_APPLICABLE. Analyst estimates are NOT_PRIMARY and never relabelled as fitted probabilities. Complete independent research; an incomplete procedure remains INCOMPLETE, but its existing research can still be retained transparently rather than discarded.

Only actual identity/allocation conflicts, an inaccessible original needed for append, a frozen/wrong-writer mini, or a real write failure block the dependent mutation. Preserve the completed research separately while resolving those issues. Missing ML is not such a conflict. Preserve the [GitHub fallback](GITHUB_REFERENCE_PROTOCOL.md) and do not fabricate inaccessible local originals.

## 2. Honest execution disposition, without a fake receipt

Attempt the supported primary route when it is actually available. Retain real success/failure bundles. If it cannot run or no adapter exists, record NOT_RUN_CAPABILITY_BLOCKED, NOT_IMPLEMENTED or NOT_RUN_DATA_UNAVAILABLE and the concrete reason. A model does not need to be installed to write a research-only card. Do not loop indefinitely on a known capability failure or fabricate EXECUTION.csv to satisfy a template.

The existing execution-disposition manifest keeps one row per new card. For no actual attempt artifact, leave execution_path/execution_sha256 empty, set feedback_status=NOT_APPLICABLE_NO_MODEL, leave feedback paths/hashes empty and record the observed reason. Actual artifact paths, if provided, must verify. C21 passes for this honest research-only disposition. MODEL_ASSISTED_PRIMARY_V3 still requires its actual verified successful bundle. `primary verify-log` accepts this distinction for mini-log-8/9 and never approves a missing-model card as a model forecast.

New minis use mini-log-9 / mini-settlement-8; earlier minis retain their original formats and new process information as dated additions. Add a future-learning disposition: PENDING_SETTLEMENT, LABEL_CANDIDATE_RETAINED, or BLOCKED_WITH_EVIDENCE, with the label/custody pointer or actual missing field. A research card's original conclusions and timestamps never change retrospectively.

## 3. Canonical import can precede settlement

Under an authorized prompt4 retention-only import, preserve the complete source mini, inventory/mapping and every original core, append the contiguous researched events to the active Combined Log, and update actual highest/next IDs and queues. A completed settlement package or ML bundle is not a prerequisite. Unreviewed outcomes remain PENDING_SETTLEMENT / OUTCOME_NOT_REVIEWED; do not assume an already scheduled match is still in play, invent a final, or add ungraded rows to performance totals. Import records the real import time, not a backdated prediction.

Later prompt3 work freezes the applicable source, verifies terminal fields and appends settlement revisions under the same P-ID. New events after a settlement freeze use the next authorized mini. Pending imports, settlements and future-learning queues retain their original identities. A source draft previously blocked only by ML may be promoted to a retained research record now with a dated reason and real recording time, never a retroactive pregame claim.

## 4. Two different kinds of learning evidence

**Future model-development labels:** settle every retained event whether or not any model existed. Retain verified final score/endpoint and contract outcomes, source/time/hash, original research/features, actual availability/exposure, effective revision, missingness and feature-admission status. Unresolved fields remain queued. Reviewed targets may be exported with:

```text
python -m ml.research_learning retain --card-id P-NNN --record CARD.md --settlement SETTLEMENT.md --labels LABELS.csv --out research/training_candidates/P-NNN/revision-1
python -m ml.research_learning verify --candidate research/training_candidates/P-NNN/revision-1
```

LABELS.csv schema is `event_id,competition,endpoint,label_key,label_value,label_unit,event_at,final_at,available_at,source_url,evidence_path,evidence_sha256,definition_status,review_status,revision_id,feature_status`. `review_status=TERMINAL_LABEL_REVIEWED`; units are GOALS/POINTS/RUNS/GAMES/SETS/WICKETS/BALLS or OUTCOME (WIN/LOSS/PUSH/VOID). The exporter retains originals, labels and a hash-bound receipt as RESEARCH_TRAINING_CANDIDATE / LABELS_RETAINED_NOT_MODEL_FEEDBACK. It allocates no ID and does not require a model. Source truth, exact event/contract correspondence and effective revision remain reviewer responsibilities.

Future training must independently admit competition/stage/endpoint, source truth, deduplication, effective revisions and point-in-time features. A trusted final can be a target while pre-start features remain unavailable. Unknown or post-outcome facts cannot become pregame predictors. Historical/late research is not prospective validation, and no automatic training/calibration or performance promotion occurs merely because a candidate exists.

**Existing Hedge/expert feedback:** only an actually issued frozen expert bundle can supply that expert's loss. Use `primary settle` when such a bundle exists. Without it, retain the target for future models and set expert feedback NOT_APPLICABLE_NO_MODEL; never manufacture past probabilities, rewards, propensities or losses. NOT_APPLICABLE_NO_MODEL does not mean the event is useless for future training.

## 5. Scoring and custody

Canonical IDs count retained research records, including qualitative/NO_FORECAST/research-only events. Research retention, numerical forecast coverage, model-feedback coverage and future-training candidate coverage are distinct counts. Research-only analyst rows never inflate model T2, Brier, calibration or clean prospective cohorts. Historical records keep their original policies and any already issued numbers literally; do not retrospectively reclassify their original picks as model predictions.

All timing, source, immutable-original, known-at, contract and operator-definition controls remain. Missing ML must be visible as metadata, never used to discard the research or prevent a supported settlement.


**Model use and mandatory running-log record (owner clarification, 16 October 2026).** Use the supported ML/RL mechanisms when they are available for the exact sport, competition and endpoint. Whether a model exists or not, assign the reconciled permanent P-ID, append the researched game card to the active running mini-log, read it back and advance its footer. A missing sport-specific model must not leave an otherwise recordable game as intake-only, unissued or without an ID. With no verified model output, record RESEARCH_ONLY_NO_MODEL, the actual reason and supported analyst work; never invent model probabilities or receipts. Carry that same P-ID through verified canonical import; do not allocate another ID. Before an authorized import, the local card may truthfully say PENDING_IMPORT; that status never cancels its ID or running-log entry. Identity/allocation conflicts, frozen or inaccessible originals and real write failures still block only the affected mutation. Verified settlements remain available for future model development in both paths.

See [RETAIN-v1](RESEARCH_RETENTION_PROTOCOL.md). This is an editorial clarification of the existing two-path behavior; no model, numerical policy or format change.
