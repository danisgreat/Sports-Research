# Documents retired on 2026-09-28 (md-only restructure), and where their live rules went

**Why.** The user asked for redundant information and documents to be removed, and for the forecasting model to use Markdown documents only. Before this pass, the live rules were spread across about 30 overlapping documents, each with layers of dated addenda. The model had to reconcile precedence on every card, and many steps called Python tools.

**What was done.**
- Every rule that was still live was consolidated into a small set of operating documents.
- The documents below were moved here **verbatim** (git history also keeps them).
- Nothing was deleted.
- An old citation such as "`RULES_GENERAL.md` §16.8" or "`DATA_SOURCE_REGISTER.md` §6A" now resolves to the file in this folder.

**Precedence.** These files are evidence and history. They never override the operating documents, and they cannot reinstate a rule withdrawn in `CURRENT_RULES.md` §I.

| Retired file | What it held | Where the live content is now |
|---|---|---|
| `RULES_GENERAL.md` | Cross-sport gates (G0–G31, G-L1–G-L24), GFA-2, and the dated controls 2026-09-05 → 2026-09-26(e) | `CURRENT_RULES.md` §A–§F and §I. Sport files cite "RULES_GENERAL (archived) §…" for GFA-2 detail |
| `METHOD_v4.3.md` (the old `METHOD.md` text) | Lifecycle, the six-field card, scoring rules, honesty boundary, precedence | `CURRENT_RULES.md` §B–§D; `CARD_AND_LOG_TEMPLATES.md` §1; `METHOD.md` is now the version and freeze-receipt pointer |
| `AGENT_ROLE_AND_TASK.md` | Role and honesty boundary | `CURRENT_RULES.md` §A |
| `CONTROLS.md` | An index of about 100 control IDs and their statuses | Live controls are stated in `CURRENT_RULES.md` and the sport §0 pages; test IDs and statuses in `LEARNINGS_INDEX.md` |
| `EXTERNAL_LOGGING_WORKFLOW.md` | Mini-log import, variant discovery, settlement procedure | `CARD_AND_LOG_TEMPLATES.md` §2, §3, §7; `PROMPTS.md` §3–§4 |
| `FORECAST_PREFLIGHT_MANIFEST.md` | The automated preflight JSON (`prediction_preflight.py`) | Replaced by the self-audit, `CARD_AND_LOG_TEMPLATES.md` §5 |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | The pregame research sequence and the §19 checklist | `CURRENT_RULES.md` §B; `CARD_AND_LOG_TEMPLATES.md` §5; `PROMPTS.md` §2 |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | Eligibility of historical records | `CURRENT_RULES.md` §A3 and §D7 (learning-only; zero eligible rows) |
| `RECENCY_AND_REBOUND.md` | Recency and rebound evidence (no rebound in 6 of 6 competitions) | `CURRENT_RULES.md` §D5; `BASE_RATES_REGISTER.md` §7 |
| `DATA_SOURCE_REGISTER.md`, `SOURCES_before_2026-09-28.md` | The full and quick source registers, with every dated source audit | `SOURCES.md`, re-verified 2026-09-28; the cricket toss and strip ladders are carried in full in §3.3 |
| `numerical_program/` (`NUMERICAL_PROGRAM.md`, `NUMERICAL_MODEL_REGISTER.md`, `NUMERICAL_TRAINING_SPEC.md`, `MODEL_AND_DATA_SPEC.md`, `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`, `MODEL_IMPLEMENTATION_RECIPES.md`, `H0_DATASET_CARD.md`) | Design and status of the Python numerical models (maintainer research) | Research record only. The results that matter to cards are in the sport §0 pages, `BASE_RATES_REGISTER.md` §7.7–§7.8 and `PROBABILITY_TOOLKIT.md` §4 |
| `snapshots/` (`GAME_LOG_STATUS_INDEX_2026-09-05.md`, `PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md`) | Historical status snapshots | `GAME_LOG_STATUS_CURRENT.md` is the live register |
| `sport_history/RULES_<SPORT>_history_to_2026-09-28.md` | Each sport file's dated sections (settlement learnings, the evidence behind numbered controls) | The live rules are each sport file's §0, which the 2026-09-26 pass consolidated from these sections |

**Also moved:** the control manifests before `CONTROL_MANIFEST_2026-09-28-3.md` went to `archive/manifests/`. Issued cards keep citing their manifest by name.

**Tools replaced for the model** (they remain as maintainer tooling):

| Tool | Now |
|---|---|
| `tools/card_math.py` | `PROBABILITY_TOOLKIT.md` §1–§3, §8, §9 |
| `tools/team_baseline.py` | `PROBABILITY_TOOLKIT.md` §4 (TB-1-MD) |
| `tools/rank_model.py` | `PROBABILITY_TOOLKIT.md` §5 |
| `receipts.py` | The endpoints in `SOURCES.md` |
| `tools/slate_universe.py` | `CARD_AND_LOG_TEMPLATES.md` §4 |
| `audit_card_controls.py` | `CARD_AND_LOG_TEMPLATES.md` §5 |
| `tools/evidence_status.py`, `tools/skill_baseline.py` | `CURRENT_RULES.md` §D9 and `SKILL_BASELINE_LEDGER.md` |
| `tools/mlb_model.py`, `tools/sport_models.py` | The shadow lanes are suspended for md-only operation (`SHADOW: NO_LANE (md-only)`) |
