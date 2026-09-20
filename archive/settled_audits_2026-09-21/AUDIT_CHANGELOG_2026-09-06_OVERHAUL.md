# Audit change log — 2026-09-06 comprehensive framework overhaul

Status: **HISTORICAL RECORD OF THIS PASS.** Origin: `FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md`, a complete review of every game log from `P-001` to `P-317` against the full rule set, requested and delivered the same day, followed by implementation of every recommendation in that review.

## 1. What was reviewed

Every canonical record `P-001`–`P-317`, all 38 root-level Markdown documents, 18 component logs in `prediction logs/`, and the two independently supplied 2026-09-06 blind-spot reviews. Full methodology and findings: `FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md`.

## 2. Ledger reconciliation — `P-306`–`P-317`

**Finding.** Twelve canonical IDs were issued into `PREDICTION_MINI_RUNNING_LOG_P317.md`, an external-session running log never reconciled into the canonical `PREDICTION_LOG_COMBINED_2.md`. Every "no event is awaiting a result" statement in the repository between their issue and this discovery was false.

**Action.** Each card's exact frozen contract terms were read from the source file. Each event's official result was retrieved fresh via live web search/fetch (`WebSearch`/`WebFetch`, September 2026) from field-owning or two-independent-source records, cited per card. Every row was graded under its originally issued terms — no ranking, evidence label, or reasoning was altered; only the settlement outcome was added.

**Sources used for settlement (all retrieved 2026-09-06):**
- ESPN (soccer match/stats endpoints, MLB recaps) — `P-306`, `P-312`, `P-313`, `P-314`
- ATP Tour, ABC News (AU) — `P-308`, `P-310`
- ESPN college football — `P-309`
- ESPNcricinfo, khelnow.com, Barbados Today — `P-311`
- AFL.com.au — `P-315`
- 일간스포츠 (isplus.com) and 네이트 스포츠 (nate.com), two independent Korean-language outlets — `P-316`/`P-317` (official KBO box score not directly fetchable this session; two-independent-source fallback applied per §4 of the source-authority hierarchy)

**Result.** 10 newly settled events (`P-317` supersedes `P-316` as one event; `P-307` closed `NO FORECAST ISSUED`, administrative). Full settlement table, per-row grades, and the new cohort ledger (Rank #1 5-5, Rank #2 1-9, Rank #3 8-2, Rank #4 6-4 — a fresh out-of-sample confirmation of the review's finding that the ordinal ranking does not order): `PREDICTION_LOG_COMBINED_2.md` §"2026-09-06(e)". Updated all-history Rank #1 aggregate: 137-96 across 233 graded events (58.8%).

**Files changed:** `PREDICTION_LOG_COMBINED_2.md` (controlling snapshot corrected, settlement section appended), `PREDICTION_MINI_RUNNING_LOG_P317.md` (closed, header errors corrected, reconciliation note added).

## 3. Version-chaos correction

**Finding.** Fourteen of fifteen active documents declared method version `MDS-2026.09.05-v3.6`; `RULES_GENERAL.md`'s own `GFA-2` algorithm section declared `v3.9`; `README.md` declared `v3.8`. `G0` (fresh method-version read) was unsatisfiable because no single document controlled the answer.

**Action.** Every active document's header now declares `MDS-2026.09.06-v4.0`, with `METHOD.md` as the single source of truth going forward.

**Files changed:** `AGENT_ROLE_AND_TASK.md`, `RULES_GENERAL.md`, `MODEL_AND_DATA_SPEC.md`, `LEARNING_REGISTER.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`, `NUMERICAL_TRAINING_SPEC.md`, `PERFORMANCE_ELIGIBILITY_POLICY.md`, all ten `RULES_<SPORT>.md` files.

## 4. Withdrawn-gate cross-reference defect

**Finding.** `AGENT_ROLE_AND_TASK.md` §6 item 12 and `RULES_GENERAL.md`'s own checklist item 27 continued to mandate `G26.1`'s result and the superseded `UNION_LOW_THRESHOLD`/`INTERSECTION_CONSTRAINT` vocabulary after both were withdrawn/corrected on 2026-09-06(d), the same day.

**Action.** `AGENT_ROLE_AND_TASK.md` item 12 corrected and repointed to the new probability requirement. `RULES_GENERAL.md` §16 supersedes checklist item 27 as the controlling mandatory-item list.

**Files changed:** `AGENT_ROLE_AND_TASK.md`, `RULES_GENERAL.md` (new §16).

## 5. Gate portfolio consolidation

**Finding.** 48 gates, 28 mandatory checklist items, measured compliance between 0% and 28% across 238 parsed cards. The mandatory pre-research read totalled ~570 KB / ~143,000 tokens.

**Action.** Every gate classified `BLOCKING` / `REQUIRED ANALYSIS` / `GUIDANCE` / `REMOVED FROM LIVE CARD` (`RULES_GENERAL.md` §16.2). New ~12-item mandatory checklist (§16.3). `G20.2`/`G21.1`/`G26.1` removed from the mandatory card entirely (already disclosure-only; never executed on a live card). Environment gate (`G15.1`) explicitly reaffirmed, not softened (§16.4) — its ~90% historical failure rate is a reason to enforce it, not relax it. New explicit-arithmetic requirement replacing prose shrinkage (§16.5). Gate-cap and retirement rule added (§16.7).

**No historical gate definition, card, or settlement was deleted or altered in substance.** Every gate discussed remains fully defined in `RULES_GENERAL.md` §§0–15 for reference.

**Files changed:** `RULES_GENERAL.md` (new §16, ~2,000 words).

## 6. Document consolidation

**Finding.** The lifecycle was described four different, drifting ways across `AGENT_ROLE_AND_TASK.md`, `RULES_GENERAL.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md` and `MODEL_AND_DATA_SPEC.md`. `LEARNING_REGISTER.md` (177 KB, 121+ lessons) and `DATA_SOURCE_REGISTER.md` (95 KB) were too large to be read per card. Five numerical-program documents (147 KB combined) described a single Stage-0 design.

**Action — scoping decision, stated explicitly.** Rather than physically merging and deleting the ~300 KB of source documents (high risk: hundreds of historical cards cite exact gate IDs, source IDs and lesson IDs by file), four new short primary documents were created and the originals retained in full with banner pointers:

- **`METHOD.md`** (new) — supersedes `AGENT_ROLE_AND_TASK.md`, `RULES_GENERAL.md` §11 narrative, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `MODEL_AND_DATA_SPEC.md` §§3–8, and `PERFORMANCE_ELIGIBILITY_POLICY.md` as the per-session read.
- **`CONTROLS.md`** (new) — ~15-item quick reference superseding `LEARNING_REGISTER.md` as the per-card read; `LEARNING_REGISTER.md` retained in full as "the lesson archive."
- **`SOURCES.md`** (new) — compact per-sport source table superseding `DATA_SOURCE_REGISTER.md` as the per-card read; the original retained in full as "the full source register."
- **`NUMERICAL_PROGRAM.md`** (new) — entry point superseding `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`, `NUMERICAL_TRAINING_SPEC.md`, `NUMERICAL_MODEL_REGISTER.md`, `H0_DATASET_CARD.md`; all four retained in full as detailed technical reference. Includes a new, fully specified scoped MLB pilot proposal (§5) — not yet authorised to build.

**Result: mandatory per-card reading drops from ~570 KB to roughly ~90 KB** (`METHOD.md` + `CONTROLS.md` + one `RULES_<SPORT>.md` + the active log's snapshot).

**Sport-file stripping (review §7.1 row 4) — scoped down.** The review recommended extracting each `RULES_<SPORT>.md`'s competition-rules section into a `LEAGUE_RULES_<SPORT>.md` companion for every sport (as already exists for cricket and soccer), targeting under 20 KB per file. This was **not done** in this pass: it requires careful per-sport content surgery across ten files with real risk of data loss, and — unlike the cross-cutting documents above — only one sport file is read per card under the new `METHOD.md` process, so the marginal benefit is smaller than for the documents actually merged. Instead, each of the ten `RULES_<SPORT>.md` files received a banner pointing to `METHOD.md` as the primary read, leaving the sport-specific algorithm and competition reference intact and unedited. This remains a legitimate follow-up if the per-sport files are found to still be a bottleneck.

**README.md rewritten** from ~29.8 KB to a ~8 KB document map, reorganised into Primary / Detailed Reference / Historical tiers, with corrected ledger counts and no stale ledger claims.

**Physical archiving (review §7.2) — scoped down.** The review recommended physically moving ~700 KB of dated audit documents into `archive/`. This was **not done**: none of those documents were ever part of the mandatory `G0` read list, so physical relocation delivers little practical benefit while risking broken relative links across dozens of cross-referencing documents. Instead, `README.md`'s new document map explicitly categorises them under "Historical / dated audit documents," achieving the same practical outcome (a reader can immediately see what is live vs. historical) without the link-breakage risk.

**Files created:** `METHOD.md`, `CONTROLS.md`, `SOURCES.md`, `NUMERICAL_PROGRAM.md`, this changelog.
**Files banner-updated (not restructured):** `AGENT_ROLE_AND_TASK.md`, `RULES_GENERAL.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `MODEL_AND_DATA_SPEC.md`, `PERFORMANCE_ELIGIBILITY_POLICY.md`, `LEARNING_REGISTER.md`, `DATA_SOURCE_REGISTER.md`, `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`, `NUMERICAL_TRAINING_SPEC.md`, `NUMERICAL_MODEL_REGISTER.md`, `H0_DATASET_CARD.md`, all ten `RULES_<SPORT>.md`.
**Files rewritten:** `README.md`.

## 7. Probability and scoring mechanism (new)

**Finding.** Zero probabilities were ever issued across 317 events; the ordinal-only rule made the forecast literally unscoreable, and the resulting ordinal record showed no measurable separation between Rank #1 and Rank #4.

**Action.** `METHOD.md` §5 introduces a mandatory `UNVALIDATED_SUBJECTIVE` probability on every ranked row, kept explicitly distinct from a `PUBLISHED` (validated-model) probability, scored with Brier score against a trivial 0.5 baseline and tracked per `PRIMARY_SCORED` population from the first card issued under this version. **Not applied retroactively** — no probability was invented for any card settled before this version, which would be hindsight fabrication.

## 8. Population scoping (new)

**Finding.** 317 events spread across ~11 sports and 60+ competitions; no population large enough to validate or even reliably measure anything.

**Action.** `METHOD.md` §2 designates MLB, EPL, and NRL/AFL as `PRIMARY_SCORED`; every other sport/competition is `EXPLORATORY — NOT SCORED` until separately promoted under a stated threshold (verified structured-data coverage plus a realistic path to a large same-population sample).

## 9. Explicit-arithmetic requirement (new)

**Finding.** Cards routinely stated a corridor (e.g. "27–34") and located a line against it by inspection, missing that a joint two-team sum can straddle a line even when each team's own range looks favourable (documented at `P-309`).

**Action.** `RULES_GENERAL.md` §16.5 requires every joint event object to show its arithmetic: stated prior, signed weighted adjustment, resulting centre and width, each line located against that width with the arithmetic shown.

## 10. Retrospective schema rebuilt (new)

**Finding.** The prior retrospective schema graded compliance more than it examined the sport, producing 121 lesson entries from 317 events and 2 retirements.

**Action.** `METHOD.md` §7.2 replaces it with three questions (driver / knowability / smallest fix) and a pattern review every 25 settled cards in a `PRIMARY_SCORED` population; compliance grading is retained but demoted to a background field.

## 11. Ledger-integrity rule (new)

**Action.** `METHOD.md` §10: an external running log not reconciled into the canonical log within 24 hours of being made available to a session blocks the next new forecast — the direct structural fix for the defect found in §2 above.

## 12. What this pass did not do

- **No settled card's originally issued contract outcome (WIN/LOSS/PUSH) was changed.** Every correction is to reasoning-adjacent text, disclosure, ledger completeness, gate wording, or a previously-missing settlement.
- **No probability was retrofitted onto any card issued before this version.** See §7.
- **Sport-file extraction into per-sport `LEAGUE_RULES_<SPORT>.md` companions was not completed** for the eight sports lacking one (cricket and soccer already have one). See §6.
- **Physical file archiving into `archive/` was not performed.** See §6.
- **The MLB numerical pilot was specified but not built.** Building it requires explicit user authorisation (`NUMERICAL_PROGRAM.md` §5) that this pass did not treat itself as having received, because the review's own recommendation was to *propose* the pilot, and building real data/fitting code is a materially larger and less reversible commitment than editing Markdown.
- **The 86 pre-`L-095` lessons were not retroactively classified** under the taxonomy introduced in September 2026(c) — this was already an explicitly deferred task before this pass and remains one.

## 13. Validation performed

- Every settlement in §2 was checked against at least one field-owning or two independent named sources before being recorded; no result was assumed or inferred.
- Table column counts were verified in every new document (`METHOD.md`, `CONTROLS.md`, `SOURCES.md`, `NUMERICAL_PROGRAM.md`, this changelog, the `PREDICTION_LOG_COMBINED_2.md` addition).
- Every banner-updated file was spot-checked after editing to confirm the header block was not corrupted.
- The updated all-history Rank #1 aggregate (137-96, 58.8%) was computed directly from the settlement table in §2 combined with the review's own 132-91/223 baseline, and is materially unchanged by the reconciliation — consistent with the reconciled cohort itself running close to a coin flip (Rank #1 5-5).

## Documents changed in this pass

**Created:** `METHOD.md`, `CONTROLS.md`, `SOURCES.md`, `NUMERICAL_PROGRAM.md`, `AUDIT_CHANGELOG_2026-09-06_OVERHAUL.md` (this file), `FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md` (prior turn).

**Edited:** `PREDICTION_LOG_COMBINED_2.md`, `PREDICTION_MINI_RUNNING_LOG_P317.md`, `AGENT_ROLE_AND_TASK.md`, `RULES_GENERAL.md`, `MODEL_AND_DATA_SPEC.md`, `LEARNING_REGISTER.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`, `NUMERICAL_TRAINING_SPEC.md`, `NUMERICAL_MODEL_REGISTER.md`, `H0_DATASET_CARD.md`, `PERFORMANCE_ELIGIBILITY_POLICY.md`, `DATA_SOURCE_REGISTER.md`, all ten `RULES_<SPORT>.md`, `README.md`.

**Unchanged (deliberately, per §12):** `PREDICTION_LOG_COMBINED.md`, all 18 files in `prediction logs/`, `GAME_LOG_STATUS_INDEX_2026-09-05.md`, `GAME_LOG_LEDGER_2026-09-06.md`, `GAME_LOG_BLINDSPOT_REVIEW_2026-09-06.md`, `IMPROVEMENT_PLAN_2026-09-06.md`, `PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md`, `COMPREHENSIVE_RETROSPECTIVE_2026-08-22.md`, `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-02.md`, `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md`, `AUDIT_CHANGELOG_2026-09-05.md`, `AUDIT_CHANGELOG_2026-09-06.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `LEAGUE_RULES_CRICKET.md`, `LEAGUE_RULES_SOCCER.md`, `archive/*`.
