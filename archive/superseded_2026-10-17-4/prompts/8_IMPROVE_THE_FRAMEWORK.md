# PROMPT 8 — Implement, verify and release a framework or workshop change

**Local keys until import; updated mini after every game (MINI-v1).** Apply [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md). Prompts 1–3 use stable local event keys and never assign/reserve canonical P-IDs; prompt 4 alone assigns them during verified import. After each prompt-1 game request, append the research/addendum, update and read back the mini, and return its complete updated .md document. Preserve every owner-entered Upcoming game block and all earlier issued bytes. New formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](../../RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**P-2026.10.17-v21.0 · FRAMEWORK_CHANGE · LOCAL_WORKING_TREE.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). Writes: declared operating Markdown/CSV/text, archived originals, fixtures and a unique verification folder. Python/tests/requirements are permitted only under ml/ by CURRENT_RULES §0. No JSON, notebooks, pickles, workflows or binaries. Publish when this full prompt is invoked unless explicitly local-only.

**ML/RL scope (MLSCOPE-v1).** Owner instruction, 17 October 2026: ML/RL is not part of game research. Prompts 1–5 run no code, runtime pack, model, shadow or learning command and read no model output. Prompt 1 researches the game and derives every p_card by hand as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY, using [PROBABILITY_TOOLKIT](../../PROBABILITY_TOOLKIT.md) arithmetic with every input and step shown. Prompts 2–5 create, settle, import and roll over records by hand. ML/RL runs only in prompt 6 (combined-log retrospective: learning-store ingest, model feedback, shadow settlement and comparisons) and prompt 8 (workshop code, releases, shadows and promotion decisions). Its findings reach game research only as reviewed Markdown changes (toolkit constants, base rates, rules) released through prompt 8. This rule supersedes any older text requiring prompts 1–5 to run ML, CYCLE-v1, CHAT-EXEC-v1, a capability receipt, an execution manifest or a learning-store export.

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

## Inputs

- User instruction or concrete finding, with exact scope.
- Relevant retrospective/source/model evidence and prior exposure, or discover.
- Allowed writes, independent/assisted/shadow lanes and publication instruction.
- Workshop targets, if requested: exact competition/endpoint/model/config and evidence question.
- Decision-lab audit only when expressly authorized; its material remains outside card learning.

## 1. Read current authority and inspect actual mechanisms

Read common controls/protocol, scoring/verification/hypotheses, contribution rules, latest three changelog entries, affected prompts/dependencies, latest completed retrospective and relevant learning. For workshop work read source/tests, model cards, generated artifact and run receipts. An unfinished report, placeholder or unavailable STATUS is not implemented evidence. Print branch/HEAD/dirty inventory and a full receipt; fetch the publication ref without overwriting work.

Assess data admission/known-at, coherent physical support/endpoints, same-row baselines, chronology/tuning/calibration separation, independent prospective freeze, artifact loading and operational failure paths separately. Tests prove only their actual checks. Exposed historical evaluation cannot become untouched/prospective by renaming it.

## 2. Write a concrete proposal and dependency map

Create a unique framework_change_<date>-<run> folder with CHANGE_PROPOSAL and IMPLEMENTATION. Record instruction/date, defects and exact file/evidence, scope, classification, before/after behaviour, dependencies/versions, verification and rollback.

For every recommendation state adopt/adapt/shadow/defer/reject, exact change/task/owner, acceptance evidence, remaining sample/design requirements and status. Administrative/source/integrity repairs can be authorized without pretending a predictive test passed. Selection/model/threshold/qualification changes need their own frozen comparison.

Archive replaced working documents byte-for-byte, including dirty baselines. Store retired code as text outside active execution or in permitted workshop version history. Preserve issued originals, grades, old hypotheses and dated reports. Do not erase concurrent work or finish another process's partial artifact by inventing values.

## 3. Implement in dependency order

1. Establish authorized scope and evidence lane, then data/source/identity/availability contracts.
2. Complete preregistration before confirmatory use: scope, candidate/baseline, horizon, primary metric, meaningful effect, precision/dependence/power, missingness, multiplicity and stopping. Unknown design inputs keep promotion BLOCKED_DESIGN.
3. Implement numerical contracts and serious simple baselines before complex challengers. Winner/handicap/total/push must be projections of a compatible event state; cricket/tennis/extras require their own structure.
4. Fit/tune/calibrate/evaluate chronologically with all attempted candidates logged. Each transform, player cluster, rating, encoder and roster state must be training/cutoff-safe. A calibrator must not use the outcomes being evaluated.
5. Implement actual shadow guards: code/data/config/input identity, timing, committed receipt retrieval, unchanged bytes, per-event reveal, exact settlement convention and revision validation. A locally written receipt is not proof of commitment. An earliest-start slate release cannot expose later manual forecasts.
6. Align rules/templates/prompts/examples/source registers/status/indexes together. FORMAT/STATISTICAL changes bump prompt major; PROCEDURE bumps minor; truly editorial wording keeps version. Old minis/cards retain their semantics.

For RL/decision work, verify observable action-time inputs and delayed feedback, exact logged behaviour probabilities and support, identical opportunities/baselines, payoffs/costs/reserved cash/settlement time and limitations. CLV-based reward is a surrogate; a drawdown penalty is not CVaR or a hard guarantee. Date-only prices permit an assumption-labelled paper replay, not verified execution. RL cannot be promoted by a favourable seed or inherited forecasts.

## 4. Verify implementation and artifact integrity

Run relevant focused tests and the required workshop suite, python -m pytest ml/tests, when code changes. Every material new check needs a rejecting negative case and a legitimate edge case. Exercise deterministic/rerun recovery, future-input injection, wrong source/schema/hash, uncommitted receipt, early reveal, incomplete/duplicate final and endpoint mismatch as relevant. Use throwaway EXAMPLE IDs, no live P-IDs.

An altered generating code/config/data hash invalidates current-artifact claims. Regenerate affected outputs from an actual controlled run or retain the old run with its exact recoverable implementation and label it historical/unqualified; never hand-edit generated scores or stamp a new receipt onto old numbers. Record failures/limits instead of publishing missing runs as complete.

Check generated scopes/coverage/receipts against actual source/population and code. A league-name LABEL_A allowlist is not field-owner admission. Store raw market data outside the research repository, export permitted aggregates only, and verify forecast/model files contain no market fields. Logs and card learning never ingest decision-lab signals.

Run VERIFICATION_PROTOCOL §6: versions/dependencies/links, archive hashes, old-format preservation, actual readback, full intended diff, allowed types/paths and protected-record identities. Label manual walkthroughs and executed tests accurately. Summarise model quality, calibration, predictive evidence and operational readiness separately.

## 5. Release, rollback and report

Release only the authorized scope whose evidence gates passed. A tested development candidate stays development/shadow until its registered prospective evidence, sufficient precision and owner-approved exact-scope integration exist. Owner-authorised experimental primary use follows PRIMARY_PREDICTION_PROTOCOL and actual receipt-bound per-event execution; a prompt rewrite alone is not a fitted model or predictive qualification. Rejection/inconclusive/data-hold results remain visible.

Stage exact reviewed paths and inspect staged diff/status. Recheck source/artifact hashes and concurrent writes immediately before commit. Publish without force under authorization; fetch/compare main or named destination SHA and read back key artifacts. A remote advance needs normal reconciliation, never history overwrite.

Return current prompt/index and implementation/review links, before/after behaviour, exact versions, measured checks/results, qualified versus blocked scopes, effects on in-progress minis, remaining data/experiment tasks and verified commit/remote state. Rollback targets the changed code/config/scope only, preserving canonical history and all failed forecasts.


Research-completion changes must exercise uncalibrated inference, missing/failed runtime, unsupported families, missing history/lineups, active-mini/lease conflicts and post-start/outcome-exposed cases. Reject an intake-only or NO_FORECAST-only deliverable as completed analysis; accept genuine exhausted gaps only with substantive A1-A9 work and the evidence matrix. Keep numerical ML guards and truthful custody intact.

## Research retention and execution disposition (RETAIN-v1)

**Retain the research (RETAIN-v3).** Record the full research and its ANALYST_PRIMARY_V1 probabilities (or a bounded range / UNCALIBRATED_QUALITATIVE / NO_FORECAST row with the reason) under a stable local event key, and deliver the complete updated mini Markdown after every game request. No model, runtime, receipt or manifest is needed or recorded. Canonical P-ID assignment belongs exclusively to prompt 4 import. Settle original contracts and keep verified outcomes for prompt 6 learning; never invent probabilities, sources or pregame timing. C21 checks that the probability method, inputs and arithmetic are disclosed; C22 checks updated-document delivery.

Verify EXEC-v1 lifecycle coverage through actual `primary execute`, rejected attempts, `primary verify-log`, delayed `primary settle` feedback and future consumption. Exercise a supported exact competition with no pre-existing archive/profile/TB-1 baseline: recover reviewed inputs, fit the league comparator from its own history, execute the ML/Hedge pipeline and retain receipts. Also reject unsupported/insufficient/unknown inputs honestly. Preserve all historical forecasts and local prompt inputs; a failed attempt is not a fitted model and passing mechanics is not predictive qualification.


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Append the researched card regardless of model availability, update intake and the local footer, verify the full mini and return its complete updated .md file after each game request. Prompt 4 alone assigns canonical IDs after duplicate/identity reconciliation and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](../../RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.


## Preserve owner-entered event inputs during instruction edits

When the task asks to align prompt instructions while retaining event details, snapshot every Upcoming game block through its first Read paragraph. Keep those bytes identical in working and committed prompt 1, including populated event names, times, contracts and research constraints. Edit the instruction body from Read onward. Verify all eleven sport/general blocks, not only the basketball example. Do not convert populated owner inputs back into empty templates.

## Persistent sourcing and information closure (EXH-v1)

Propagate EXH-v1, mini-settlement-10 and S17 consistently through current rules, all sport workflows, templates/examples and source reuse. Preserve earlier issued formats, canonical IDs, current prompt-1 game-input bytes and immutable reports. Verify negative single-source/mirror/partial/conflict/unavailable cases; never claim research was performed because its template exists.

## ML/RL ownership (MLSCOPE-v1)

Prompt 8 owns every `ml/` code change, release, prospective shadow freeze and promotion decision. No change may make prompts 1–5 run code or read model output without a new owner instruction. An improvement found by ML reaches game research only as reviewed Markdown (PROBABILITY_TOOLKIT constants or tables, BASE_RATES_REGISTER rows, LEAGUE_PROFILES, rule text) with its evidence. A model shadow for a future game is frozen here, in the repository, before the start, and never changes the analyst card.

## Data, training, calibration, shadow and promotion gates (LEARN-v1)

Apply [LEARNING_PIPELINE_PROTOCOL](../../LEARNING_PIPELINE_PROTOCOL.md) §§3–8 to every model, parameter, calibration or learning-rate change:

1. **Data:** inputs come from the learning store with point-in-time views; quarantine and missingness are reported; no retired-store or market data.
2. **Training data:** an immutable training release that `python -m ml training verify` rebuilds byte-identically.
3. **Chronological evidence:** development, tuning, calibration and evaluation windows are separate and in time order. Backtests, ablations and Hedge/calibration studies carry receipts and evidence classes. Every attempted candidate is logged.
4. **Prospective shadow:** freeze the candidate before each start in the hash-chained ledger, alongside the unchanged champion, with a preregistered minimum effect `delta`, metric and stopping rule.
5. **Decision:** promotion only after `python -m ml prospective evaluate` returns PROMOTION_ELIGIBLE, without unacceptable calibration or coverage deterioration, and the owner approves. Record each state change with `python -m ml registry append`. A rollback is a new ROLLED_BACK row naming the restored version.

No new model may retroactively change issued probabilities, ranks, grades or feedback. Run `python -m pytest ml/tests`, including the end-to-end lifecycle and prompt-consistency tests. A CI workflow file or branch protection requires an explicit owner amendment.


**Connected cycle handoff (CYCLE-v1).** Apply [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md). Preserve and verify actual workflow attempts and frozen version/contract identities. For contextual bundles, run `python -m ml cycle settle` with the verified structured settlement export into the authorised local/shared scope; preserve expert feedback and OUTCOMES.csv. Research-only labels never fabricate an expert loss. Prompt 4 re-ingests source exports idempotently into the shared store and records actual counts, quarantine and custody. Reconcile collided historical aliases by source/body addresses, never P-ID alone. Use `cycle evaluate` for frozen paired Brier/log-loss/calibration reports; insufficient future data remains INSUFFICIENT_EVIDENCE. No historical grade or model promotion follows automatically.
