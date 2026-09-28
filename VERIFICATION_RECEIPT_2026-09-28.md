# Verification receipt — 2026-09-28(d)

This receipt records executed checks for the Markdown evidence and custody repair. The [protocol](VERIFICATION_PROTOCOL.md) defines the gates. It is a living execution note, excluded from the stable control manifest so the manifest's own SHA-256 can be recorded here without a circular hash.

## Executed results

| Gate | Result |
|---|---|
| Repository layout | 57 current content files; all `.md`; all at root or directly in `prediction logs/`; no other content directory. Git internals excluded. |
| Frozen source custody | P-518 onward mini log raw SHA-256 `c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30`, matching the pre-repair snapshot. The Part 5 edit is limited to its current header/snapshot links; no issued card body changed. |
| Queue | Part 5 and current status say canonical through P-517, P-518–P-522 reserved and unimported, next ID HOLD. The mini log's conflicting P-523 claim remains frozen and quarantined in [reconciliation](P518_P522_RECONCILIATION.md). |
| Seed Brier | Independently recalculated from all 29 published seed rows: card 0.2461, population 0.2360, difference +0.0101. Prospective rows: 0. These results do not demonstrate skill. |
| Historical validation bundle | All nine embedded historical artifacts match their parent Git blob contents after documented newline normalization. Five embedded JSON artifacts parsed successfully. The full game-level evaluation was not rerun because its input data and dependent modules are absent from the Markdown tree. |
| Link audit | 178 broken local link occurrences in preserved historical documents, across 74 distinct targets. [Recovery index](HISTORICAL_LINK_INDEX.md) maps 61 targets to reachable Git commits and marks 13 unavailable. Zero broken local links in current operating/evidence documents or the current status header. |
| Freeze receipt | [Manifest -6](CONTROL_MANIFEST_2026-09-28-6.md) lists 53 stable files; all 53 normalized-CRLF SHA-256 values and byte counts matched on independent readback. Its normalized-CRLF SHA-256 is `f74d0369cd91770c54ee32a9c548467023ee19fa3cd2de26114795c6ef26b392`, matching the first status line. |
| Diff syntax | `git diff --check` passed. The staged diff and remote equality are checked as separate publication steps. |

## Remaining evidence limits

- None of P-518–P-522 has a certified complete issue and settlement lineage. Event-result checks do not release the ID hold or make a row performance eligible.
- The historical TB-1-MD aggregate outputs are preserved and inspectable, but their original game-level inputs are absent from the current tree. Independent replication remains open.
- Thirteen deleted link targets have no reachable Git version. The preserved historical text is not silently rewritten to invent replacements.
- No prospective card-skill or RM-1 validation cohort exists yet. `C-RULE-FREEZE` remains in force.
