# Verification report — canonical import P-550..P-556 (2026-10-09)

## Input integrity

| Input | Bytes | SHA-256 | Result |
|---|---:|---|---|
| `PREDICTION_MINI_RUNNING_LOG_P-551_ONWARD_FROZEN.md` | 175,096 | `fc1c3b4592b1df5e8ac2a9abbabb9f5945b124cf493d62e686ab59360e3f0415` | matches manifest; LF only |
| `PREDICTION_MINI_SETTLED_P-550_P-556.md` | 561,737 | `62447b56fcc75c41695b5b59909a5e1ede610c885d1b3fab736eeae2e005bfe3` | matches manifest; begins with the frozen bytes |

All eight packet files were copied unmodified into `inputs/` and hashed (see `CANONICAL_IMPORT_MANIFEST.json`).

## Independent post-commit checks (`163`, all passed)

Run against the working repository after the 14 commits: ledger append-only and hash-chain links intact (106 records); Combined Log 7 append-only (359,145 → 491,009 B); for each of the seven IDs — PREPARED/COMMITTED linkage for card and addendum, retained source SHA = ledger SHA = build SHA, source is a byte substring of both packet files, projection SHA = ledger, projection byte-equal to its single marker block in the Combined Log, addendum placed after its card, exactly one card heading and one addendum heading, four ranked rows, every original `p_card` present in the preserved card text; and the diagnostics recomputed from the addenda equal the expected set (7 events, 28 rows, 15 W / 13 L, 0 other, Rank-1 4, Hit@2 5, Wins@2 7/14, NDCG@2 0.5162, winners 4/7) and each event's row in `SETTLEMENT_MANIFEST.json`.

## Repository commands (isolated clean `git worktree` at HEAD `1ffbd9f52` + import outputs overlaid)

The working tree contains unrelated user edits (`research/src/control_manifest.py`, `SOURCES.md`), so verification ran in a clean worktree, mirroring `.github/workflows/research.yml`.

| Command | Result |
|---|---|
| `pytest research/tests research/operations research/experiments runtime/tests -q` | **265 passed, 0 failed** |
| `research.operations.log_card verify` | pass; cards P-523..P-556, next_id P-557 |
| `research.operations.verify_custody` | pass; `source_body_failures: []` |
| `research.operations.verify_reconciliation` | pass (freeze `CONTROL_MANIFEST_2026-10-08-3.md`) |
| `research.operations.control_freeze --verify` | pass: 446 files, 0 mismatches (no new manifest needed) |
| `research.operations.verify_all_logs` | pass; original forecasts, ledger and projection bytes preserved |
| `research.experiments.runner verify` | pass |
| `research.operations.verify_rollover` | pass |
| `research.operations.verify_carryover_review` | pass |

## Pre-existing environment note (not caused by this import)

On first run `verify_custody` and `verify_all_logs` failed with `FileNotFoundError` for gitignored raw snapshot bodies absent from a clean checkout (`research/data/raw/source_snapshots/*`, `research/data/benchmark/source_snapshots/*`). After copying the 203 ignored local files from the main tree (read-only reference data, no tracked file changed), both pass. Any fresh clone without those files would fail the same two commands independently of this import.

## Publication readback

Recorded in the final report block of the session (commit SHA, push result, remote HEAD re-read and post-publish re-verification), because a file committed in the publication cannot contain its own commit hash.
