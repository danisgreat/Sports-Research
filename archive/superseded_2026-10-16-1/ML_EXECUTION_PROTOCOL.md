# Mandatory game and mini-log ML execution

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

**EXEC-2026.10.15-v1 · MDS-2026.10.15-v16.1 · CR-2026.10.15-R8 · P-2026.10.15-v16.1.** Owner instruction: check every game/mini-log requirement and require actual ML/learning execution even where a league/competition has no baseline to go by. FORMAT + PROCEDURE: new mini-log-8 / mini-settlement-7; canonical-md-1, PRIMARY_HEDGE_MIX_V3, selection and score formulas unchanged. [Primary numerical protocol](PRIMARY_PREDICTION_PROTOCOL.md), [research completion](RESEARCH_COMPLETION_PROTOCOL.md), [audit](research/verification/framework_change_2026-10-15-7/IMPLEMENTATION.md).

## 1. Strict rule: an absent baseline is not an execution exemption

Every newly requested game in every sport/league/competition must enter the actual event-specific execution workflow. An absent published baseline, profile, TB-1 constants, archive routing, calibration certificate, prior model or feedback history is never a reason to skip the attempt. Do not merely name an algorithm, print a generic probability or claim an unexecuted run.

1. Research exact identity/endpoint and reviewed sporting history under [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md). Recover missing local history online first; use fresh reviewed metadata and normalized rows without waiting for permanent archive/profile repair.
2. Prepare the actual request, supported contract subset and source-backed history. Declare unsupported requested families separately so they do not suppress supported full-event inference. Freeze the candidate recipe before pricing. Do not fill unknown times, outcomes or parameters to pass admission.
3. Actually run `primary execute` below. It requires no pre-existing baseline probability/profile. Where supported, it fits the league comparator afresh from the same competition's admitted history, fits both team-rating experts, learns Hedge weights from earlier available losses and prices the coherent mixed distribution.
4. Retain the success/failure receipt and add the exact event/attempt identity to the mini's manifest and card. A failed admission, unsupported adapter, insufficient history or fit failure is an observed failure, not an exemption or a numeric forecast. Repair evidence-supported issues and retry into a new immutable attempt folder. Keep earlier attempts and name the effective one.
5. If no interpreter/tools or access exist, seek an actually accessible runtime or exact-event verified bundle. Record genuine capability evidence and execution NOT_RUN_CAPABILITY_BLOCKED / INCOMPLETE, never EXECUTED or a fabricated `EXECUTION.csv`. This cannot pass C21 or strict log verification. Complete independent research and retain the full draft; request/ID/write limits do not authorize fake runs.

Missing a frozen same-row comparator affects paired scoring only. Do not backfill an old card's baseline from a new fit. If the actual three-expert V3 pipeline cannot fit its own required league grid, retain the executed failure and nonnumeric primary disposition; this procedure does not silently replace V3 with an untested two-expert algorithm or borrow another league's parameters. Unsupported numerical adapters remain explicit implementation work. A strict attempt is not a guarantee that every sport can yield a valid numeric model.

## 2. Execute and verify the actual mechanism

```text
python -m ml primary execute --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --out ATTEMPT
python -m ml primary execute --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --competition-source COMPETITION_SOURCE.csv --feedback EFFECTIVE_FEEDBACK.csv --out NEXT_ATTEMPT
python -m ml primary verify-execution --attempt ATTEMPT
```

Input schemas/admission are in [PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md). Omit optional feedback only when the reconciled effective inventory has no available matching rows; record its searched scope/count. No prior feedback means an honestly labelled warm-start/uniform state, not a reason to skip learning. Reviewed competition-source routing admits exact metadata for a missing/defective archive; it does not invent an unsupported engine or release held historical artifacts.

`ATTEMPT` must be new. `STARTED.csv` precedes input admission/fitting; `INPUTS.csv` records actual source paths/raw and normalized hashes; `EXECUTION.csv` records actual start/completion, code/HEAD, identity, stage, EXECUTED/FAILED, baseline disposition and errors. A successful immutable bundle lives under `ATTEMPT/BUNDLE` and retains its original full grids, loss ledgers, weights, eta, input/output hashes and receipt. Failure exits nonzero and retains its actual receipt. An interrupted STARTED-only attempt is incomplete. `verify-execution` can verify a documented failure as a failure; that never authorizes numeric ML output.

Legacy `primary predict` still works for compatibility. It alone does not produce the new mandatory execution receipt. Never hand-wrap an old forecast as a new executed attempt. These receipts check custody/computed mechanics, not independently verified publication, outcome blindness, source truth or predictive qualification.

## 3. One manifest row for every new game card

New mini-log-8 creation initializes `ML_EXECUTION_MANIFEST.csv` with the following header and zero rows. There is no dummy fit or P-ID allocation:

```csv
card_id,event_id,competition,endpoint,execution_path,execution_sha256,feedback_status,feedback_path,feedback_sha256,reason
```

Every appended card has exactly one matching row and these card fields:

```text
- **ML execution identity:** <exact event_id> | <exact competition path> | <endpoint>
- **ML execution:** <EXEC-v1; actual attempt path/EXECUTION.csv SHA-256; status/error; manifest row and verifier evidence>
- **Learning:** <actual warm/feedback counts, weights/eta from bundle or precise failure; feedback disposition>
```

`execution_path` names the attempt folder, resolved relative to the manifest or explicitly absolute. `execution_sha256` hashes its actual EXECUTION.csv. The mini's native/stable event identity, participant mapping, contract keys, primary rows and bundle must agree; C2/C19/C21 include human readback of the exact correspondence. The machine verifier checks execution identity and coverage; it does not independently parse every narrative fact or certify sources.

```text
python -m ml primary verify-log --manifest ML_EXECUTION_MANIFEST.csv --mini PREDICTION_MINI_RUNNING_LOG.md
```

The verifier rejects omitted/duplicate/wrong-event/tampered/incomplete attempts and numeric model cards backed only by failures. A valid failed attempt can be retained only as its original nonnumeric research, with NOT_APPLICABLE_NO_MODEL and reason. It never supplies an ML probability, numerical gate PASS or feedback observation. At issuance successful runs use PENDING_EVENT with a substantive reason unless a valid other disposition applies.

Requests without a written card retain attempts/capability gaps in intake/A9; they do not manufacture IDs. Existing active mini-log-2 through -7 keep their format: append these fields and a companion manifest only for new EXEC-v1 cards, checking the subset explicitly with C21. The next new mini uses mini-log-8. Historical originals, probabilities, ranks, baselines and grades are never rewritten or retrospectively certified.

## 4. Settlement, actual feedback and future learning

Freeze original mini, original manifest and referenced execution/bundle bytes before settlement. New mini-settlement-7 packages retain those originals and a separate effective manifest. Settle original sporting contract keys first. Then for every successful bundle with supported verified terminal coordinates:

```text
python -m ml primary settle --bundle ATTEMPT/BUNDLE --home-score HOME --away-score AWAY --final-at ISO --available-at ISO --evidence CAPTURE --evidence-sha256 SHA256 --out NEW_FEEDBACK.csv
```

Retain the actual feedback output/hash, parent/effective revision and one reconciled row per event. Feedback is derived from every frozen expert grid and source-backed final, not the baseline difference, selected-row win alone, analyst prose or a reward invented for a missing comparator. A pushed primary row may lack a proper score while the supported expert endpoint still supplies valid learning.

Each effective manifest row has exactly one disposition:

| Disposition | Required evidence |
|---|---|
| FEEDBACK_RETAINED | Actual one-row output path/hash, same event/execution, supported final and reconciled effective revision |
| PENDING_EVENT | Actual event not yet terminal, last source/state check and next action |
| BLOCKED_WITH_EVIDENCE | Precise endpoint, definition, source/time, custody or capability blocker and repair owner; not simply missing baseline/calibration |
| NOT_APPLICABLE_NO_MODEL | Actual failed attempt/no successful model; analyst/qualitative work is never model feedback |

Run `verify-log` on the frozen mini/effective manifest, C21 and S16. A mechanical pending/blocked label is not proof the disposition is true; inspect its terminal/source evidence. Future `execute --feedback EFFECTIVE_FEEDBACK.csv` must consume the actually available, matching-policy, deduplicated source-backed rows. Never learn the target outcome, a future correction, unresolved revision or feedback from an unissued/analyst card. No future execution was scheduled merely by naming the next command.

## 5. Canonical custody, audits and limits

Prompt1 executes and appends; prompt2 initializes the empty manifest; prompt3 freezes/settles/retains feedback; prompt4 verifies exact coverage, copies custody artifacts with resolvable pointers and imports originals; prompt5 preserves continuity pointers; prompt6 audits every included card/attempt/feedback disposition; prompt7 repairs reviewed sporting inputs; prompt8 tests/reviews actual mechanics.

Import reports enumerate new successful/failed/missing execution and retained/pending/blocked/not-applicable feedback per sport/competition/endpoint. Missing attempt evidence blocks a compliant new numeric import, while independent sporting settlement/research continues. Report a documented noncompliance explicitly rather than erase or rewrite an already-issued original. Legacy imports keep original semantics and historical gaps, never fabricated retrospective runs.

The current mechanism is supervised score models plus full-information online expert aggregation (Hedge). There is no newly trained environment-control RL/PPO/DQN policy. Passing execution checks does not establish calibration, prospective advantage, perfect inputs or production readiness. Unknown inputs and unsupported sport/phase/player adapters remain visible.
