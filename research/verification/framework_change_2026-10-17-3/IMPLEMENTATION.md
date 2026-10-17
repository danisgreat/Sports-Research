# Implementation — no-code game research; ML/RL in prompts 6 and 8 (MLSCOPE-v1)

**MDS-2026.10.17-v21.0 · CR-2026.10.17-R3 · P-2026.10.17-v21.0 · MLSCOPE-v1 / NOCODE-v1 / ANALYST_PRIMARY_V1 / DRIVE-v2 · STATISTICAL + PROCEDURE.**

Owner instruction, 17 October 2026: "ML/RL doesn't seem to be implemented when I want to do research for each individual game log, so I guess it'll have to be relegated to the combined log retrospective section and the improve the framework sections, so change the code where necessary accordingly, including the prompts and push to git and remove any requirement to push to google drive as well. When prompt 1 aspects are being run in ChatGPT chat or an external chat, it shouldn't need to use any python code or anything, just a framework for research and providing the accurate probability... and prompt 1 and prompt 2 should refer to the latest main branch in the git repo for sports research."

Read at HEAD `bc8ddd7dd` (equal to origin/main). The peer's untracked `research/verified_history/2026-10-17-nba-gap-fill/` was neither used nor staged.

## Why

- No card has ever been priced by the model in an external chat: 0 of 24 V3 runs in the last cohort, and every recent chat card recorded `No module named ml`.
- Both active cycle releases show 0 prospective events, and the learning store's NHL history ends on 18 April 2025.
- The model requirements therefore added steps a chat could not perform without improving the probabilities it produced. The framework already holds a complete by-hand method in PROBABILITY_TOOLKIT, written for the 2026-09-28 Markdown-only operation.

## Before and after

| | Before (v20.2) | After (v21.0) |
|---|---|---|
| Prompt 1 primary p_card | MODEL_ASSISTED_CYCLE_V1 / V3 runtime output; analyst work NOT_PRIMARY | ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY: one hand-built distribution, every input and step written out |
| Code in a chat | Runtime pack, `python -m ml.chat run`, capability receipt, ingest dry-run, shadow freezes | None. No Python, code interpreter, runtime pack or command-line tool |
| Learning data from prompt 1 | RESEARCH_EXPORT CSV files plus ingest commands | Markdown tables of prior-game rows and availability snapshots inside the card (LEARN-v2) |
| Baseline | `python -m ml baseline` when the model could not run | BASELINE_LEAGUE_V1 computed by hand (SELECTION_RULES §9) |
| Prompts 2–5 | Execution manifest, `verify-log`, `primary settle`, `cycle settle`, learning-store ingest, learning-status | Removed. Settlement by hand; import only; legacy pointers carried unchanged |
| ML/RL | Prompts 1–8 | Prompt 6 (ingest, feedback, shadow settlement, paired comparisons) and prompt 8 (code, releases, shadow freezes, promotion) only |
| Feedback into cards | Model grid became p_card | Only reviewed Markdown changes (toolkit constants, base rates, rules) released through prompt 8 |
| Authority for prompts 1–2 | One pinned `main` commit | The latest `main` commit, pinned by full SHA for the run |
| Google Drive | DRIVE-v1 mirror, sync receipt, push to both | DRIVE-v2 optional drop box; no push or mirror requirement |

## Files

- **Prompt 1.** Header paragraphs LEARN-v2 and NOCODE-v1, a new mode line, and a latest-`main` repository reference. In each of the eleven workflows:
  - removed: the CYCLE-v1 paragraph;
  - new: the Read sentence, the ANALYST_PRIMARY_V1 paragraph, and the restored pre-ML sport distribution paragraph from `archive/superseded_2026-10-15-2/` (basketball overtime reworded from "simulated" to the regulation-tie mass) with a pointer to the toolkit section;
  - restored: the PR-03 pricing basis and the PR-01 form-window bullet;
  - also new: RETAIN-v3, the LEARN-v2 learning record and the contract-definitions/hand-baseline paragraph.
- **Prompt 2.** Latest-`main` reference; no execution manifest, no `verify-log`.
- **Prompt 3.** Settlement by hand. Shadow comparison, feedback and the learning-store dry-run are deferred to prompt 6. LEARN-v2 Markdown outcome records and hand-computed Brier diagnostics.
- **Prompt 4.** No learning-store handoff; legacy model cohorts imported literally; an optional structural `verify-log --mini` check in the repository.
- **Prompt 5.** Legacy pointers carried unchanged.
- **Prompt 6.** New section "ML/RL review (MLSCOPE-v1)".
- **Prompt 8.** New section "ML/RL ownership (MLSCOPE-v1)".
- **COMMON_OPERATING_PROTOCOL.** Task table, version paragraph, LEARN-v2, lifecycle and CYCLE-v1 scope.
- **MLSCOPE-v1 paragraph** added to CURRENT_RULES, CURRENT_STATE, README, PROMPTS, ACTIVE_FILE_INDEX, CONTRIBUTING, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, METHOD, PRIMARY_PREDICTION_PROTOCOL, FORECAST_CYCLE_PROTOCOL, ML_EXECUTION_PROTOCOL, LEARNING_PIPELINE_PROTOCOL, RESEARCH_COMPLETION_PROTOCOL, RESEARCH_RETENTION_PROTOCOL, MINI_LOG_IDENTITY_PROTOCOL, PROBABILITY_TOOLKIT and ml/README, and to prompts 2–8 and the prompt index.
- **CURRENT_RULES** operative rewrites:
  - §0 "Who uses it";
  - §1 model reading gate;
  - §6 numeric primary;
  - §7 analyst pricing;
  - §9 Drive mirror removed;
  - §10 R35, R36 and CHAT-EXEC retired for game research.
- **Other controls.**
  - SELECTION_RULES §10 is now "Primary probability source".
  - CARD_AND_LOG_TEMPLATES card lines and C21.
  - GOOGLE_DRIVE_EXCHANGE_PROTOCOL rewritten as DRIVE-v2.
  - GITHUB_REFERENCE_PROTOCOL steps 5–6.
  - DEPENDENCY_MAP regenerated from the prompts' actual text.
- **Code.**
  - `ml/execution.py`: `verify_log(None, mini)` checks a no-code mini (format marker, local-key card markers, one ANALYST_PRIMARY_V1 / UNCALIBRATED_QUALITATIVE / NO_FORECAST status per card) and accepts ANALYST_PRIMARY_V1 rows in a legacy manifest.
  - `ml/primary.py`: `verify-log --manifest` is optional.
  - Tests: two new cases in `ml/tests/test_execution.py`. `ml/tests/test_prompt_consistency.py` requires the three identical no-code paragraphs in all eleven workflows and the NOCODE header, and fails if prompts 1–3 or 5 instruct running `python`, `git` or `pip`, or name PRIMARY_PREDICTION_PROTOCOL or FORECAST_CYCLE_PROTOCOL.
- **Originals.** `archive/superseded_2026-10-17-3/` (32 files, ARCHIVE_HASHES.csv).

`ml/chat.py`, the cycle releases, the learning store and the registry are unchanged and remain available to prompts 6 and 8. CHAT-EXEC-v1 is retired for game research, not deleted.

## Verification

See [VERIFICATION_CHECKS.csv](VERIFICATION_CHECKS.csv).

## Google Drive

DRIVE-v1's mirror of `bc8ddd7dd` had started (2 files uploaded) when the instruction to remove the Drive requirement arrived. The mirror was stopped, and its partial copies and empty folders were moved to the Drive trash. A short status note at the folder root says the remaining files are an unmaintained snapshot of `b01b035b1`, so a chat reading Drive is not misled. The `uploads/` folder stays for optional use. Nothing in this release was pushed to Drive, and nothing requires it.

## Limits

- ANALYST_PRIMARY_V1 probabilities are uncalibrated analyst judgements made with transparent arithmetic. They are not certified, and this change claims no predictive improvement. The first prompt-6 review compares them with BASELINE_P and with any frozen model shadow.
- A chat may still make arithmetic mistakes. The written-out steps and the toolkit §11 checks are the control.
- Older documents not listed above may still mention model-assisted primary cards. MLSCOPE-v1 in CURRENT_RULES §0 supersedes them, and CURRENT_RULES outranks sport and league rules.
