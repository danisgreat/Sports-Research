# Change proposal: framework change 2026-10-14-3 (model workshop, shadow lane, decision lab)

**Date:** 14 October 2026, Australia/Sydney. **Base revision:** `main` at `3ab6d27fe` (the revert of `0e5685e57`), working on branch `ml-workshop-2026-10-14`. **Authority mode:** `LOCAL_WORKING_TREE`.

## 1. User instructions (verbatim)

1. "provide a comprehensive implementation frameworj for this for the local files, be methodical, honest and thorough". This produced [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](../../../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md).
2. "add this and continue the full implementation of reinforcemnet learning and models to improve teh sports framework and push changes to git at the end, take your time to do this properly". "This" was a supplied report, *Calibration in Sports-Research Models* (report R4).
3. "it has to be a process that can be applied to all sports leagues/tournaments within those spoets, not jsut the mainth  leagues mentioned" (given during implementation). The workshop therefore discovers every competition folder in the archive and applies one process (ml/README.md, "One process for every competition").
4. Answers to two questions put to the owner on 14 October 2026:
   - On commit `0e5685e57`: **"Revert it, then rebuild (Recommended)"**.
   - On where code lives: **"ml/ folder in this repo (Recommended)"**.

## 2. Findings that shaped the change

| Finding | Evidence |
|---|---|
| **Commit `0e5685e57` (pushed to `main` by a concurrent session) was fabricated.**<br>• Invented "fitted" parameters (the EPL table lists Leicester, Ipswich and Southampton as the 2026-27 slate).<br>• Forecast rows frozen on future dates (2026-10-16 to 2027-04-01).<br>• Every receipt hash and data hash equal to `e3b0c442…b855`, the SHA-256 of empty input.<br>• A workshop commit `c8f2a1b9` from a workshop that did not exist.<br>• Seven operating documents double-encoded: CHANGELOG 174 lines, SOURCES 313, HYPOTHESIS_REGISTER 18, CURRENT_RULES 12, SCORING 8, CURRENT_STATE 7, METHOD 5.<br>• The CURRENT_RULES §0 authority-mode bullets removed. | Reverted in `3ab6d27fe` and pushed. The tree equals `941c5abd3` byte for byte. |
| **This session overwrote another writer's file.** A concurrent Codex session's original root framework (85,030 bytes, written about 15:30) was overwritten by this session's Write at 15:34 (CONTRIBUTING: never delete another writer's files). | The original was recovered from Codex checkpoint ref `…/295ac50f-…` and preserved outside the repository with its two receipts: `C:\Users\danie\Desktop\Sports-Research-quarantine\2026-10-14-codex-ml-framework\` (SHA-256 `f3732897…`, `5f5c0bf6…`, `21b6c192…`). |
| **The 9 October runtime repairs were never committed.** `37203fc2b` is the last committed runtime, not a repaired one. | ML_RL_IMPLEMENTATION_FRAMEWORK F05. |
| **The archive is not training-ready by its own admission rule.** Most leagues have 0 `training_eligible` rows in the 10-05 export. | Framework F10. Models here train on LABEL_B observed rows, labelled as such. |
| **CURRENT_RULES forbade code (§0) and staking advice (§5).** | Hence the bounded exception (§0) and firewall (§5a) below, both under owner instruction. |

## 3. Scope, classes and behaviour

| Item | Class (prompt 8 §2) | Before | After |
|---|---|---|---|
| `ml/` workshop (Python, tests, requirements) | suspended software prerequisite, now authorised | No code allowed | Code allowed only under `ml/`; no JSON, pickles, notebooks or workflows |
| `research/model_shadow/` | scoring/format definition | Did not exist | Market-free Markdown/CSV with receipts; statuses DEVELOPMENT_ONLY / SHADOW_CANDIDATE / SHADOW |
| Reading-gate exclusion | integrity/process repair | — | Prompts 1–3 never read `research/model_shadow/` or `ml/` before their freeze |
| Decision-lab firewall (§5a) | selection/model experiment (paper only) | Staking advice forbidden | Still forbidden; a paper-only historical study may commit aggregates under DECISION_LAB |
| Card calibration audit | data/measurement | — | Descriptive report on the cards' stated p |
| Cricsheet licence | administrative correction | "ODbL 1.0" | "ODC-By 1.0" |
| Prompt 8 header; prompt index | PROCEDURE | "No code …" | "No code … except `ml/` under CURRENT_RULES §0" |

**Versions.** The control revision moves from `CR-2026.10.12-R2` to `CR-2026.10.14-R1`, and the prompt suite from `P-2026.10.12-v11.0` to `P-2026.10.14-v11.1` (PROCEDURE). These are unchanged, because the card procedure, scoring definitions and selection are unchanged:
- method `MDS-2026.10.12-v11.0`;
- scoring `SCV-2026.10.12-v7`;
- selection `SEL-2026.10.12-v3`;
- mini-log-7 and mini-settlement-6.

**Not changed:** any issued card, mini, log, grade, P-ID, archive CSV, dated report or the scoreboard. No model is a card input. Promotion beyond SHADOW needs a further owner instruction.

## 4. Verification plan

- `python -m pytest ml/tests`, covering checks C-ML-01 to C-ML-18 (FIXTURES.md).
- Every committed CSV passes the market-column guard.
- Receipts are recorded and the code digest is recomputed.
- Archive copies are byte-identical to the base blobs.
- `git diff --check`, and changed links resolve.
- No JSON, pickle or notebook is staged.
- No protected file changed (logs, issued research, archive CSVs).

## 5. Rollback

`git revert` of this change's commit. The archived originals under `archive/superseded_2026-10-14-3/` restore every edited document. Generated model files are disposable and reproducible from their receipts.
