# METHOD — version and freeze receipt

Status: **ACTIVE**
Method version: **MDS-2026.09.28-v5.0 (md-only)**
Control revision: **CR-2026.09.28-MD2**. Freeze the SHA-256 file receipt from [CONTROL_MANIFEST_2026-09-28-5.md](CONTROL_MANIFEST_2026-09-28-5.md) with every new card. Copy the manifest name and its SHA-256 onto the card. The SHA is printed in the **Current freeze receipt** line at the top of `GAME_LOG_STATUS_CURRENT.md`, a living file the manifest does not hash, so it can carry the manifest's own SHA.
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
