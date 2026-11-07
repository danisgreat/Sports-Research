# METHOD — version and freeze receipt

Status: **ACTIVE**
Method version: **MDS-2026.09.29-v6.0**
Control revision: **CR-2026.09.29-P1**. Freeze the normalized-CRLF SHA-256 file receipt from [CONTROL_MANIFEST_2026-09-29-3.md](CONTROL_MANIFEST_2026-09-29-3.md) with every new card. Copy the manifest name and its SHA-256 onto the card. The SHA is printed in the **Current freeze receipt** line at the top of `GAME_LOG_STATUS_CURRENT.md`, a living file the manifest does not hash, so it can carry the manifest's own SHA.
Scoring version: **SCV-2026.09.19-v2**

**This file is a pointer, not a procedure.** On 2026-09-29 the user authorized non-Markdown research code and data in this repository. [Pipeline implementation and gate register](PIPELINE_IMPLEMENTATION_2026-09-29.md) controls P-523+ numerical cards and the separate pilot; the older Markdown procedures below remain historical/learning-only where they conflict.

| Need | File |
|---|---|
| The operating manual: every live rule, the workflow, custody | [`CURRENT_RULES.md`](CURRENT_RULES.md) |
| Research code, data, tests and run receipts | [`research/README.md`](research/README.md) |
| Probability arithmetic, TB-1-MD, RM-1, Elo, scoring | [`PROBABILITY_TOOLKIT.md`](PROBABILITY_TOOLKIT.md) |
| Card, settlement and log templates; the self-audit | [`CARD_AND_LOG_TEMPLATES.md`](CARD_AND_LOG_TEMPLATES.md) |
| Sources | [`SOURCES.md`](SOURCES.md) |
| Sport rules | `RULES_<SPORT>.md` §0 |

**History of this method.** Previous method text and dated control receipts remain in Git history. Issued cards keep the method, controls and manifest they were frozen under.

**What changed in v5.0.**
- Procedures are unchanged in substance. Every Python step was replaced by a Markdown procedure that reproduces it (`PROBABILITY_TOOLKIT.md`, checked against the tools).
- No probability, width, centre or ranking rule changed.
- The manifest remains the maintainers' integrity receipt. A maintainer updates and verifies the Markdown receipt; the model only copies its name and SHA.

**2026-09-28 MD3 evidence repair.** Forecast coefficients and ranking arithmetic are unchanged. The current tree now includes [P-518–P-522 reconciliation](P518_P522_RECONCILIATION.md), [historical validation evidence](VALIDATION_EVIDENCE.md), [prospective record requirements](RECORD_ELIGIBILITY_SCHEMA.md), [historical link recovery](HISTORICAL_LINK_INDEX.md), and a [verification protocol](VERIFICATION_PROTOCOL.md). Historical aggregate baseline effects remain provisional until game-level data permit independent replication. Parts 1–4 and the P-518 onward working mini log remain frozen.

**What changed in v5.1 (2026-09-28(e), MD4; user-instructed review improvements).** No probability, width, centre, family mass or in-domain rank rule changed. The changes are to the card's issue process and to the consistency of the documents:
- **Core first, annex after** (`CURRENT_RULES.md` §B). The core, meaning everything that sets a probability or rank, is frozen before the start. Disclosures follow in an annex that cannot change a frozen number. The long documents are read once per session.
- **RM-1 domain guard restored** (`PROBABILITY_TOOLKIT.md` §5.0). A sport outside RM-1's eight fitted sport groups gets `RM1_OUT_OF_DOMAIN` and ranks by p, as the retired tool did. A `SIDE_FLIP` row in the top two carries a plain-language disclosure; its rank is unchanged.
- **One rule for scoring q, and one meaning for the checkpoints.** The rule is in `SCORING_AND_VALIDATION.md` §15 and `SKILL_BASELINE_LEDGER.md` rule 7. The preregistered decision-weighted estimate is restored as the read-out statistic.
- **Removed paths are audited** (`VERIFICATION_PROTOCOL.md` §4, rules L1 and L2), and indexed in `HISTORICAL_LINK_INDEX.md`.
- **The rule inventory is closed** until the checkpoints read out (`CURRENT_RULES.md` §D9).

**2026-09-28(f), MD5 source coverage.** `SOURCES.md` adds field-specific immediate fallback routes and audited official-source paths for all ten sport sections. An original, timestamped, authenticated organisation social announcement is admissible for its own field and remains one lineage with its website. This repairs the overbroad categorical social ban; it does not change forecast arithmetic, probabilities, ranks or prior cards.

**2026-09-28(g), MD6 log consolidation.** The only files in `prediction logs/` are combined Parts 1–6. Parts 1–5 preserve canonical history through P-517. Part 6 embeds the original P-518–P-522 source bytes unchanged, quarantines those disputed claims and continues new prediction IDs from P-523 by the user's explicit instruction. This continuation does not certify the earlier five records. Former standalone logs and intermediate Part-5 snapshots are recoverable at pinned Git history through `HISTORICAL_LINK_INDEX.md`. Forecast arithmetic, prior issued values and scoring rules are unchanged.

**2026-09-29(a), MD7 custody close-out and source/social lanes.** This pass finishes the MD6 consolidation. Manifest `-9` no longer verified, because nine files were edited after it was written; the active receipt is now `CONTROL_MANIFEST_2026-09-29-1.md`. It also removes the last "next ID on hold / use TMP" instructions, and `GAME_LOG_STATUS_CURRENT.md` now carries P-518–P-522 as reserved and P-523 as the next ID. `SOURCES.md` adds live-tested routes for every sport, a social-platform access matrix (X read routes now work; Bluesky, YouTube and Threads routes are documented) and a source-by-source fallback chain with each source's authenticated official accounts (§3.12). Retrieval and traceability only: no forecast arithmetic, probability, rank, issued card or scoring rule changed.

**Receipts.** The `-4` through `-9` manifests of 2026-09-28 remain historical receipts, even though their original headers call them current. This header and `CONTROL_MANIFEST_2026-09-29-1.md` identify the active receipt. Cards frozen under an earlier manifest keep it.
