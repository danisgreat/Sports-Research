# Research-only record without an installed model

**Online history and confirmed players (HIST-2026.10.16-v2 / AVAIL-2026.10.16-v3).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

FORMAT EXAMPLE / NOT_IMPORTABLE. EXAMPLE identifiers are not allocated P-IDs and the examples are not sports evidence. New formats are mini-log-9 / mini-settlement-8 under [RETAIN-v1](../../../RESEARCH_RETENTION_PROTOCOL.md).

If a researched game has no adapter or the environment returns `No module named ml`, write the researched event under the next reconciled P-ID rather than abandon it. Print RESEARCH_ONLY_NO_MODEL; keep model p_card NOT_ESTIMATED and supported analyst_p separately NOT_PRIMARY. Record actual evidence, issue/first-play/exposure times and incomplete research honestly. Update the footer only after the actual append/readback. An inaccessible original, collision or write failure remains a separate reason the mutation cannot complete.

The manifest row has exact identity, empty execution/feedback paths and hashes, feedback_status NOT_APPLICABLE_NO_MODEL and the real missing-model reason. There is no invented EXECUTION.csv. C21 passes this honest research disposition. A model claim using the same missing evidence must fail.

An authorized retention-only prompt4 import preserves the original source/core and advances canonical allocation through the contiguous retained sequence, without requiring a completed settlement or a model. Import time is not forecast issue time. The local working P-ID maps to the same canonical P-ID; no reset or new event is created by import.

When terminal data is reviewed, prompt3 appends original-contract grades and verified targets under the same ID. Without a model bundle, retain the event as a future training candidate using `python -m ml.research_learning retain`; no Hedge loss can be computed for an expert that never predicted. An unresolved result/definition stays in the queue. Future training must separately admit source truth, endpoint, revisions and point-in-time features; late research never becomes prospective validation by being retained.


**Model use and mandatory running-log record (owner clarification, 16 October 2026).** Use the supported ML/RL mechanisms when they are available for the exact sport, competition and endpoint. Whether a model exists or not, assign the reconciled permanent P-ID, append the researched game card to the active running mini-log, read it back and advance its footer. A missing sport-specific model must not leave an otherwise recordable game as intake-only, unissued or without an ID. With no verified model output, record RESEARCH_ONLY_NO_MODEL, the actual reason and supported analyst work; never invent model probabilities or receipts. Carry that same P-ID through verified canonical import; do not allocate another ID. Before an authorized import, the local card may truthfully say PENDING_IMPORT; that status never cancels its ID or running-log entry. Identity/allocation conflicts, frozen or inaccessible originals and real write failures still block only the affected mutation. Verified settlements remain available for future model development in both paths.

See [RETAIN-v1](../../../RESEARCH_RETENTION_PROTOCOL.md). This is an editorial clarification of the existing two-path behavior; no model, numerical policy or format change.

| Model situation | ID and running-log action | Evidence |
|---|---|---|
| Supported model runs successfully | Assign the reconciled P-ID and append/read back the card | Retain actual model output and verified receipt |
| No model/adapter for this sport or competition | Assign the reconciled P-ID and append/read back the card | RESEARCH_ONLY_NO_MODEL, actual gap, no fake receipt |
| Supported model fails or cannot run | Assign the reconciled P-ID and append/read back the card | Actual failure evidence or honest no-run reason |

All three cases preserve the same P-ID on canonical import and queue source-backed settlement; none creates another event or backdates a forecast.
