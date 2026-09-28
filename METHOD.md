# METHOD — version and freeze receipt

Status: **ACTIVE**
Method version: **MDS-2026.09.28-v5.0 (md-only)**
Control revision: **CR-2026.09.28-MD3**. Freeze the normalized-CRLF SHA-256 file receipt from [CONTROL_MANIFEST_2026-09-28-6.md](CONTROL_MANIFEST_2026-09-28-6.md) with every new card. Copy the manifest name and its SHA-256 onto the card. The SHA is printed in the **Current freeze receipt** line at the top of `GAME_LOG_STATUS_CURRENT.md`, a living file the manifest does not hash, so it can carry the manifest's own SHA.
Scoring version: **SCV-2026.09.19-v2**

**This file is a pointer, not a procedure.** From 2026-09-28 the forecasting model works from Markdown documents only:

| Need | File |
|---|---|
| The operating manual: every live rule, the workflow, custody | [`CURRENT_RULES.md`](CURRENT_RULES.md) |
| Probability arithmetic, TB-1-MD, RM-1, Elo, scoring | [`PROBABILITY_TOOLKIT.md`](PROBABILITY_TOOLKIT.md) |
| Card, settlement and log templates; the self-audit | [`CARD_AND_LOG_TEMPLATES.md`](CARD_AND_LOG_TEMPLATES.md) |
| Sources | [`SOURCES.md`](SOURCES.md) |
| Sport rules | `RULES_<SPORT>.md` §0 |

**History of this method.** Previous method text and dated control receipts remain in Git history. Issued cards keep the method, controls and manifest they were frozen under.

**What changed in v5.0.**
- Procedures are unchanged in substance. Every Python step was replaced by a Markdown procedure that reproduces it (`PROBABILITY_TOOLKIT.md`, checked against the tools).
- No probability, width, centre or ranking rule changed.
- The manifest remains the maintainers' integrity receipt. A maintainer updates and verifies the Markdown receipt; the model only copies its name and SHA.

**2026-09-28 MD3 evidence repair.** Forecast coefficients and ranking arithmetic are unchanged. The current tree now includes [P-518–P-522 reconciliation](P518_P522_RECONCILIATION.md), [historical validation evidence](VALIDATION_EVIDENCE.md), [prospective record requirements](RECORD_ELIGIBILITY_SCHEMA.md), [historical link recovery](HISTORICAL_LINK_INDEX.md), and a [verification protocol](VERIFICATION_PROTOCOL.md). Historical aggregate baseline effects remain provisional until game-level data permit independent replication. Parts 1–4 and the P-518 onward working mini log remain frozen. The `-4` and `-5` manifests remain historical receipts even if their original headers call them current; this header and `-6` identify the active receipt.
