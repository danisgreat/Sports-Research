# Verification receipt — 2026-09-28(d), (e) and (f)

This receipt records executed checks for the Markdown evidence and custody repair. The [protocol](VERIFICATION_PROTOCOL.md) defines the gates. It is a living execution note, excluded from the stable control manifest so the manifest's own SHA-256 can be recorded here without a circular hash.

## Executed results — 2026-09-28(f) source and fallback expansion (manifest -8)

These checks were run after the source edits, against the local working tree on `main`. The research reviewed official competition and club routes across all ten sport sections; route-specific access and limits are in `SOURCES.md`. No game card or settled result was generated from this source pass.

| Gate | Result |
|---|---|
| Repository layout | 59 content files; all `.md`, at the root or directly in `prediction logs/` |
| Source coverage | Ten sport sections (§3.1–§3.10), a field-specific fallback (§1.7), conditional original official-social evidence (§1.8), and ten sport-specific fallback rows (§3.11). Dated examples, the NBA `JS_ONLY` page and untested exact-game coverage are visibly qualified |
| Local links | New/current links in `METHOD.md`, `CURRENT_RULES.md`, `PROMPTS.md`, `SOURCES.md` and manifest -8 resolve locally. Historical broken links in the preserved `CHANGELOG.md` remain governed by `HISTORICAL_LINK_INDEX.md` |
| Frozen source custody | P-518 onward mini log raw SHA-256 remains `c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30`; no prediction log or numeric toolkit was edited |
| Freeze receipt | [Manifest -8](CONTROL_MANIFEST_2026-09-28-8.md) lists 55 stable files. All 55 normalized-CRLF SHA-256 values and byte counts matched an independent readback. Its normalized SHA-256 `6dc64b2d74178335b76dc8180983a8d51b104c1cbe50f463148927d675bf6a0f` matches the first status line and `METHOD.md` points to -8 |
| Diff syntax and publication | `git diff --check` passed; these local edits were not committed or pushed. The publish gate in protocol §5 remains unrun |

## Executed results — 2026-09-28(e) review improvements (manifest -7)

These checks were run by a maintainer session after the last edit, against the uncommitted working tree on `main` (base `f2da4ce`).

| Gate | Result |
|---|---|
| Repository layout | 58 content files, all `.md`, at the root or directly in `prediction logs/`. The one new file is `CONTROL_MANIFEST_2026-09-28-7.md` |
| Frozen source custody | The P-518 onward mini log's raw SHA-256 is still `c4d497bf…cf30`. Parts 1–5, everything in `prediction logs/`, and `P518_P522_RECONCILIATION.md` are unchanged (`git diff --quiet`) |
| Numbers unchanged | Every numeric table row that existed at `f2da4ce` is present, unchanged and in order: toolkit 337 rows, base-rates register 149, current rules 20, ledger 33, sport files 29. The only differing row is the intended version line in the mini-log header template. The seed Brier still recomputes to 0.2461 against 0.2360 (n = 29) |
| Contradictions | No operating document still says "score both p and q", "must not be scored as an event probability", "review checkpoints, not proof thresholds", or makes the event-weighted estimate principal. The four documents in protocol §3 agree |
| Path audit (protocol §4) | 30 operating documents. On the unmodified tree: 11 L1 failures (broken local links) and 86 L2 failures (unqualified dead code-span paths). After repair: **0 L1, 0 L2**. There are 113 qualified references to 62 removed paths, all indexed and all recoverable from reachable Git history |
| Freeze receipt | [Manifest -7](CONTROL_MANIFEST_2026-09-28-7.md) lists 54 stable files: the 53 in -6 plus -6 itself. All 54 normalized-CRLF SHA-256 values and byte counts matched on independent readback. Its own normalized SHA-256 is `a25f89fa04ef02d80e985f3f9f3a829a2a2780922923de9cfbabc339bb6df969`, matching the first status line and the `METHOD.md` pointer. Manifest -6 is unchanged (`f74d0369…`) |
| Line endings | Six files had mixed line endings, either from earlier edits or from being written with LF; they were converted to CRLF. The conversion was verified to leave each file's manifest-normalized hash unchanged. `git diff --check` passed |
| Publication | **Not committed or pushed** in this session. Protocol §5 (stage, commit, push, `HEAD` = `origin/main`) remains to be run when the user authorises publication |

## Executed results — 2026-09-28(d)

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
