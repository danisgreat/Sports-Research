# Implementation — browser-chat execution (CHAT-EXEC-v1)

**MDS-2026.10.17-v20.1 · CR-2026.10.17-R1 · P-2026.10.17-v20.1 · PROCEDURE + workshop code.** Owner prompt 8, 17 October 2026. Proposal: [CHANGE_PROPOSAL.md](CHANGE_PROPOSAL.md). Read at HEAD `7e59f83b7` (origin/main, after the peer NBA evidence commit, which changed no `ml/` source); working-tree baseline included the owner's uncommitted prompt-1 game-block edits.

## Before and after

| | Before | After |
|---|---|---|
| Web chat with GitHub connector | Reads files; `No module named ml`; every card RESEARCH_ONLY_NO_MODEL | Runs the cycle from the owner's runtime pack inside its Python sandbox; refusals keep RESEARCH_ONLY_NO_MODEL with reasons |
| Building cycle inputs | Hand-written REQUEST/CONTRACTS/EXPORT; easy schema, path, team-code and contract-sign errors | `python -m ml.chat run` writes them from GAME.csv/LINES.csv and validates release, team codes, families, sides, lines, identity and times |
| Getting results back | Sandbox output lost; no freeze | Upload zip at repository paths; `accept` re-verifies, extracts only into scoped folders, freezes shadow rows with the actual or pushed-commit clock and writes an acceptance receipt with manifest values |
| Active releases | NHL-CYCLE-2 / MLB-CYCLE-2 (code digest `d5a7063a…`) | NHL-CYCLE-3 / MLB-CYCLE-3 (code digest `0303f967…`), identical parameters; v2 retired unused (registry entries 13–16) |

## Files

- Code: [ml/chat.py](../../../ml/chat.py); tests [ml/tests/test_chat_execution.py](../../../ml/tests/test_chat_execution.py).
- Releases: [NHL-CYCLE-3](../../cycle_releases/NHL-CYCLE-3.csv), [MLB-CYCLE-3](../../cycle_releases/MLB-CYCLE-3.csv), [CURRENT_RELEASES](../../cycle_releases/CURRENT_RELEASES.csv); [registry](../../model_registry/MODEL_REGISTRY.csv); initial evaluations [NHL](PROSPECTIVE_NHL_INITIAL_V3/REPORT.md) and [MLB](PROSPECTIVE_MLB_INITIAL_V3/REPORT.md): INSUFFICIENT_EVIDENCE, 0 paired events.
- Controls: prompt 1 header paragraph, [FORECAST_CYCLE_PROTOCOL](../../../FORECAST_CYCLE_PROTOCOL.md) section, one CURRENT_RULES rule, suite version in all prompts/README/DEPENDENCY_MAP, CURRENT_STATE, CHANGELOG, PROMPTS, README, ACTIVE_FILE_INDEX, ml/README. Originals: `archive/superseded_2026-10-17-1/` (19 files, ARCHIVE_HASHES.csv).
- `.gitattributes`: exact bytes for `research/chat_captures/`, `research/cycle_attempts/`, `research/cycle_feedback/`, the archive and this folder (captures, attempts and evaluations are hash-bound).

## Prompt 1 owner blocks

Ten owner-entered Upcoming blocks are byte-identical to the pre-change working copy, including the owner's new soccer game and blanked ice-hockey template. The owner's uncommitted edit had deleted the whole BASKETBALL block, heading included, which left the basketball workflow without an input block and broke the eleven-workflow structure; an empty `Upcoming game — BASKETBALL` template (four blank fields) was restored. The earlier Huima vs NMKY entry was not restored.

## Verification (measured)

See [VERIFICATION_CHECKS.csv](VERIFICATION_CHECKS.csv).

- Focused suite: 20 passed (pack committed-bytes and stale-release refusal, mirrored schemas, digest reproduction and CRLF stability, end-to-end run → accept with PRE_START_VERIFIED ledger rows, late acceptance never pre-start, nine run refusals, failed-attempt retention without ledger rows, three upload scope/type refusals, commit-basis refusals).
- Full suite `python -m pytest ml/tests -q`: **432 passed in 301.71 s**.
- End-to-end on real data in scratch only: `pack` from commit `84c9d5718` (105 files, 753,326 bytes) → unzip into a folder without `.git` → Python 3.12.10 / pandas 2.2.3 / numpy 1.26.4 / scipy 1.13.1:
  - full team names refused with the stored NHL codes listed;
  - card G0007 (PIT @ COL, start 01:00 UTC) returned FAILED with `release frozen after information horizon`, the intended retrospective guard, with receipts and an upload zip;
  - an upcoming NHL game (`NHL:2026020121`, state FUT, start 17:00 UTC) returned EXECUTED / PRE_START with p_card and baseline_p for all four contracts; `accept` froze 8 rows PRE_START_VERIFIED and the ledger chain verified.
  - These were mechanics checks: nothing was written to the real store, ledger or a mini, and the numbers are not issued forecasts.
- Earlier evidence: the same cycle from a `git archive` copy under the older stack reproduced the Python 3.14 / pandas 3.0.5 probabilities exactly.

## Limits

- Mechanics are not skill. Both releases remain EXPERIMENTAL_NOT_QUALIFIED; the NHL store still holds only 2024–25 and MLB only September 2025.
- Only full-game winner/handicap/total in competitions with an active release are priced; halves, corners and props stay research-only.
- A chat sandbox's library versions vary; drift is recorded by `capability`, and only the stack above was exercised.
- PRE_START_VERIFIED requires the owner's acceptance and commit (or a pushed upload) before the start; chat transcripts and sandbox ledgers are not freezes.
- Any later `ml/*.py` change requires new release versions before a new pack; the 8-week window should freeze code.
- A GitHub Actions worker remains deferred (workflow files need an owner amendment).
