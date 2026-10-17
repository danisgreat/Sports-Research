# Change proposal — browser-chat execution (CHAT-EXEC-v1)

**Instruction (owner, 17 October 2026, prompt 8):** push all changes and make the ML/RL cycle usable from an external ChatGPT web chat that has GitHub access. **Classification:** PROCEDURE + workshop code. **Lane:** primary runtime access only; no model, parameter, selection, scoring, format or ID change.

## Defect and evidence

| Finding | Evidence |
|---|---|
| A web chat's GitHub connector reads files but cannot import or run `ml`. | Mini `PREDICTION_MINI_RUNNING_LOG_2026101679B3FBCC8D.md` (owner-supplied, 7 cards G0001–G0007): every card records `/opt/pyvenv/bin/python: No module named ml` and `git ls-remote`/`git clone` exit 128 `Could not resolve host: github.com`; all 7 are RESEARCH_ONLY_NO_MODEL with analyst-only numbers. |
| The sandbox itself has Python and the scientific stack. | The same cards ran `python -m ml capability` (the module, not Python, was missing) and computed SciPy/NumPy analyst arithmetic. |
| The cycle runs outside a checkout once the right files are present. | A `git archive` of `ml/`, the learning store, releases and the store's capture files ran under Python 3.12.10 / pandas 2.2.3 / numpy 1.26.4 / scipy 1.13.1 with no `.git` and reproduced the Python 3.14 / pandas 3.0.5 probabilities exactly. Without the capture files it fails (`No such file ... nhl_all_2024_25_rev2/INDEPENDENT_RESULTS.csv`), so the pack must include them. |
| Hand-built inputs fail on details. | Building the G0007 request by hand failed first on a shell-style capture path; the store uses team codes (`COL`, `PIT`), not full names; contract semantics (`handicap,AWAY,1.5`) are not obvious. |
| Freeze evidence must leave the sandbox. | The prospective ledger guard requires issue and freeze before the start; a sandbox ledger is lost with the session and is not a publication. |

## Proposed change

1. `ml/chat.py` with `pack` (committed runtime zip outside the repository, receipt, stale-release refusal), `run` (two small CSVs plus a capture → exact cycle inputs → `ml.workflow` execute/verify → RESULT.csv + upload zip) and `accept` (scoped extraction, re-verification, shadow-ledger freeze with the actual or pushed-commit clock, acceptance receipt and manifest values).
2. New release versions NHL-CYCLE-3 / MLB-CYCLE-3 with identical frozen parameters, because any `ml/*.py` change alters the normalized source digest that releases bind; registry entries for v3 and retirement of the unused v2.
3. One prompt-1 header paragraph, a FORECAST_CYCLE_PROTOCOL section, one CURRENT_RULES rule, version bumps (MDS-2026.10.17-v20.1 / CR-2026.10.17-R1 / P-2026.10.17-v20.1), CHANGELOG/CURRENT_STATE/index/README notes, and `-text` attributes for hashed captures, attempts, feedback and this release's evidence.

## Recommendations

| Item | Decision | Acceptance evidence | Status |
|---|---|---|---|
| Chat runtime pack/run/accept | ADOPT | Focused tests with rejecting and edge cases; end-to-end pack → clean folder → older stack → accept | Implemented |
| v3 releases replacing unused v2 | ADOPT (administrative) | Release-integrity tests; registry chain verify; initial evaluations INSUFFICIENT_EVIDENCE | Implemented |
| GitHub Actions execution worker | DEFER | Needs an explicit owner amendment (workflow files are prohibited by prompt 8) | Not started |
| Uploading attempts through the GitHub web UI as freeze proof | ADAPT | `accept --freeze-basis commit` uses only the pushed adding commit's committer time for an unchanged committed attempt | Implemented; first real use pending |
| Any predictive claim | REJECT | Mechanics are not skill; frozen evaluation still needs 50 paired events / 8 weeks | Unchanged |

## Rollback

Revert `ml/chat.py`, its test, the prompt/protocol/rule text and the two v3 releases; append registry rows returning the v2 versions only together with a restored source digest (a new version is required if the source differs). Archived originals: `archive/superseded_2026-10-17-1/` with `ARCHIVE_HASHES.csv`. No issued card, grade, ID or ledger row depends on this change.
