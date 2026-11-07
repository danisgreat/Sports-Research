# Contradictions removed from the merged documents — MDS/P v24.3 / CR-2026.11.07-R3

**Owner instruction, 7 November 2026:** "do comprehensive research to remove the contradictions in merged files and to shorten anything when necessary, you may find that additional research and information is needed". Base: `main` at `4b4573e80` (the verbatim merge, CR-2026.11.07-R2).

**Method.**
1. Every merged document (RULES_REFERENCE, RESEARCH_PROTOCOL, WORKFLOW, ML_PIPELINE, PARAMETERS) and every appended section (in REFERENCE_MODEL_PROTOCOL, RULES_ICE_HOCKEY, RULES_SOCCER, RULES_CRICKET and CORE) was read in full.
2. Each claim was checked against the documents that govern it: CORE, ADJUSTMENT_LEDGER_PROTOCOL, the v24 prompts, CARD_AND_LOG_TEMPLATES, the `ml` code, the CSV tables and the repository itself. Facts likely to have gone stale were checked on the web.
3. Each contradiction was resolved by the framework's own precedence: owner instruction; then CORE for cards from P-2026.10.22-v24.0 (a pre-v24 sentence anywhere yields to it); then the v24 protocols and prompts; then older text. Where precedence did not decide, nothing was chosen, and the item is listed for the owner (§4).
4. Part and section numbers were kept, so the many references of the form "CURRENT_RULES section 7" or "SELECTION_RULES §9" still resolve. Pre-v24 rules that matter only for reading old cards are kept by link to their archived text. The verbatim R2 text stays in git (`4b4573e80`), and the originals stay in `archive/consolidation_2026-11-07/merged_sources/`.

**Class.** PROCEDURE: the reading lists in the prompts changed, so the prompt suite moves from P-2026.10.22-v24.0 to **P-2026.11.07-v24.1**, and method and control move to MDS-2026.11.07-v24.3 / CR-2026.11.07-R3. No probability method, width, selection constant, reference, release, ID or grade changed. One item does change a card input in principle: regime multipliers, R-18 below. It follows from two existing rules and is flagged for the owner.

**Size.** The five merged documents plus CORE went from 256,423 to 171,308 bytes (−33%). PARAMETERS went from 59 KB to 21 KB; its historical Part C remains verbatim in the archive.

## 1. Contradictions resolved

| # | Where | Contradiction | Resolution | Governing rule |
|---|---|---|---|---|
| R-01 | RULES_REFERENCE header | Declared MDS v22.2 / CR-R6 / SEL v3 as in force | Versions now come from CURRENT_STATE | CURRENT_STATE governs current values |
| R-02 | RULES_REFERENCE A§0 | Write-scope list named folders that do not exist (`research/primary_predictions/`, `primary_policy/`, `benchmarks/`) | General rule: code writes under the folders its command names, with receipts | Repository state |
| R-03 | RULES_REFERENCE A§1 | The reading gate for other tasks named METHOD, CURRENT_RULES and SELECTION_RULES (now merged) and an ENV-v1 "section budget" | Names the merged files; ENV-v1 budget removed | ENV-v2; the 2026-11-07 merge |
| R-04 | RULES_REFERENCE A§2 (T2) | "Only Rank 1 and 2 count as primary wins" against "from v24 a descriptive count, the headline is the paired proper score" | Split by card era | CORE §3; ADJUSTMENT_LEDGER §4 |
| R-05 | RULES_REFERENCE A§4 (P4) | "Rank-1 gate constants remain provisional; the alternative-quantity gate is a shadow" | Removed for v24 cards (gate and shadows retired) | SEL v4 |
| R-06 | RULES_REFERENCE A§5 | Three overlapping timing statements (timing paragraph, PR-04 workflow, known-at), none naming the owner's never-rush rule or the fast card | One timing paragraph plus the known-at rule; the never-rush rule and FASTCARD stated | Owner rule; TIMING-v2; REFERENCE_MODEL §7 |
| R-07 | RULES_REFERENCE A§6 | "One hand-built coherent distribution with actual arithmetic" | Reference plus ledger; code may do the arithmetic | CORE §1, §6; ANALYST_PRIMARY_V1 (v24) |
| R-08 | RULES_REFERENCE A§7 (PR-03) | "The gate and ranks come from the mixture" and a required `p_base` shadow | The mixture is a `SCENARIO` ledger row; `p_base` is pre-v24 only | SEL v4; ADJUSTMENT_LEDGER §1 |
| R-09 | RULES_REFERENCE A§7 (PR-01) | The form blend "goes in the adjustment table" against v24 adjustments needing an effect-table row, the TB-2-MD and release references already carrying form, and the no-double-count rule | No form adjustment where the reference uses form; the R2 blend only for tier C (no reference) | ADJUSTMENT_LEDGER §1; CORE §6 |
| R-10 | RULES_REFERENCE A§9 (R20) | "This repository runs with `core.autocrlf=true`", and a finding that the committed `.gitattributes` had been deleted | Updated: the committed `.gitattributes` exists; work with `core.autocrlf=false` (the 2026-11-07 hash mismatch) | Repository state |
| R-11 | RULES_REFERENCE A§9 | "Commit/push only when authorised by the invoked task" against "every run that changes files ends with a commit and push" | CORE's rule stated | CORE §1; ENV-v2 |
| R-12 | RULES_REFERENCE B header and §1 | SEL v3 constants (Rank-1 gate, Rank-2 floor) in the live constants table | v24 constants (abstain 0.65, information 0.03); SEL v3 text linked from the archive | SEL v4; ADJUSTMENT_LEDGER §4 |
| R-13 | RULES_REFERENCE B§2 | The Rank-1 gate procedure and SHADOW_GATE_RET03 described as current | Replaced by the most-likely list; R14 precision kept for ordering ties | SEL v4 |
| R-14 | RULES_REFERENCE B§3 | The Rank-2 floor and four shadows (RET04, XCARD6, RANK_DELTA, BASE_ONLY) as current | Removed for v24; joint-failure reporting kept | SEL v4 |
| R-15 | RULES_REFERENCE B§9 | A RETAIN-v1 paragraph: "write every researched event under its reconciled working P-ID" | Removed: RETAIN-v1 was superseded and the rule contradicts local keys | MINI-v2; RETAIN-v3 |
| R-16 | RULES_REFERENCE B§10 | Repeated A§7 | Pointer to A§7 | GOV-v2: a rule is stated once |
| R-17 | RULES_REFERENCE B§7 | No rule for an owner convention arriving after a result | States that it applies from its date and is recorded as a revision (as BK-OT-1 was for P-616) | R17 revisions; the BK-OT-1 precedent |
| R-18 | RULES_REFERENCE B§6 with PARAMETERS C | "Use the recommended regime multiplier" from a table estimated on 2026-10-09 from the results archive. The register's own status (16 October) retires archive-derived populations for new use, and v24 adjustments need an effect-table row | A regime flag labels context; a regime effect enters only as an effect-table row or a `SCENARIO` row; the multipliers are historical | HIST-v2/LP-v4 retirement; ADJUSTMENT_LEDGER §1 (**owner check, §4**) |
| R-19 | RESEARCH_PROTOCOL A§3 | "Experimental ML first, then an analyst comparison labelled NOT_PRIMARY" | Reference stage, then ANALYST_PRIMARY_V1, then qualitative | MLSCOPE-v1 and v3 |
| R-20 | RESEARCH_PROTOCOL A§2.7, A§4, B§5 | "Prompts 1–3 make no canonical/GitHub writes" and "return the complete updated .md" | Prompts 1–3 commit and push their own records; the committed mini is the deliverable; no canonical IDs | ENV-v2; CORE §1 |
| R-21 | RESEARCH_PROTOCOL A§4 | Matrix row "actual primary run" | "Reference stage receipt / pregame freeze receipt" | MLSCOPE-v3 |
| R-22 | RESEARCH_PROTOCOL B header | "mini-log-10 follows MINI-v1" | MINI-v2 | MINI-v2 |
| R-23 | RESEARCH_PROTOCOL C (and its banner) | Described RETAIN-v2, while every prompt cites RETAIN-v3 | Rewritten to RETAIN-v3 as the prompts state it | Prompt 1 "Retain the research (RETAIN-v3)" |
| R-24 | RESEARCH_PROTOCOL C§2; WORKFLOW B§1–2; ML_PIPELINE B§2 | "One execution-manifest row per new card" and "prompt 2 creates a header-only manifest", while prompts 2 and 3 say new minis have none | No manifest for new minis; legacy manifests untouched | Prompts 2 and 3 |
| R-25 | RESEARCH_PROTOCOL C§2; ML_PIPELINE B§1 | Old disposition words (NOT_RUN_CAPABILITY_BLOCKED…) for cards | The card uses the R36 freeze dispositions; the old words are kept for workshop and legacy runs | R36 |
| R-26 | RESEARCH_PROTOCOL C§4 | Expert loss "via primary settle" only | `cycle settle` / `league-day settle` for current rows, `primary settle` for legacy V3 bundles | Prompt 3 §4; prompt 6 step 2 |
| R-27 | RESEARCH_PROTOCOL E (primary-model amendment) | "PRIMARY_PREDICTION_PROTOCOL permits the primary runtime" on cards | Models reach cards only as the frozen reference | MLSCOPE-v3 |
| R-28 | WORKFLOW A§1 | "PUBLISHED_MAIN_PINNED only for the retired ENV-v1 route", while REQ-v2 external requests were added at the owner's request after ENV-v2 | Describes any outside agent neutrally; the route decision stays open (§4) | Owner instructions of 22 October (both) |
| R-29 | WORKFLOW B§6; CARD_AND_LOG_TEMPLATES | "Current checklists S1–S18" and "settlement-10 runs S1–S18", while S19 is defined and prompt 3 runs S1–S19 | S1–S19 for mini-settlement-10 | Prompt 3 §5; templates S19 row |
| R-30 | ML_PIPELINE A | "Copy PREDICTIONS.csv probabilities into the card; do not replace them with subjective adjustments" | V3 runtime marked historical cohort and workshop tool; cards never copy it | MLSCOPE-v1 and v3; CORE §6 |
| R-31 | ML_PIPELINE C§2 | "Prompt 1 writes RESEARCH_EXPORT alongside every card", while prompt 1 no longer does and prompt 6 transcribes the cards' Markdown learning records | Prompt 1 records Markdown tables; prompt 6 builds and ingests the export | Prompt 6 step 1; RULES_REFERENCE A§10 |
| R-32 | ML_PIPELINE C§3 | "Prompt 4 writes the learning store", while prompt 4 says "import does not ingest" and the rules say only prompt 6 ingests | Prompt 6 (or prompt 8) only | Prompt 4; RULES_REFERENCE A§10 |
| R-33 | ML_PIPELINE C header and §1 | "New contextual forecasts use MODEL_ASSISTED_CYCLE_V1"; models layer listed only V3 | Cycle releases and TB-2-MD listed; the MODEL_ASSISTED_CYCLE_V1 card label is historical | MLSCOPE-v3 |
| R-34 | ML_PIPELINE C§9 | "All new tools were exercised on synthetic data; no run on real data", while §11 describes the NBA backfill and releases | Records the real NBA and NHL runs | Repository state (`research/cycle_releases/`) |
| R-35 | ML_PIPELINE C§8 | Promotion ends in "a PRIMARY_PREDICTION_PROTOCOL change" | Ends in a change of the declared reference (REFERENCE_CHOICE.csv) at a season boundary | REFSEL-v1; STATFREEZE-v1 |
| R-36 | ML_PIPELINE header; REFERENCE_MODEL merged section | MLSCOPE-v3 defined twice in full | Defined once (REFERENCE_MODEL's merged section, as CORE §9 lists); ML_PIPELINE links | GOV-v2 |
| R-37 | REFERENCE_MODEL merged FORECAST_CYCLE | "Every request must attempt execution… use the execution manifest… return the updated Markdown"; CYCLE header citing v20 and SEL v3 | Execution goes through the reference stage and freeze with their receipts; no manifest; historical labels marked | MLSCOPE-v3; prompts 2 and 3 |
| R-38 | REFERENCE_MODEL merged FORECAST_CYCLE | CHAT-EXEC-v1 described as an active route | Marked retired for game research (maintainer tooling) | RULES_REFERENCE A§10; ENV-v2 |
| R-39 | REFERENCE_MODEL: merged section against §8 | Context features (form, rest, starters) described as fitted, against §8 "not fitted, because backfilled history has no known-at times" | States that the current releases fit none of them | REFERENCE_MODEL §8 |
| R-40 | RULES_ICE_HOCKEY NHL section | Authority MDS v7.1 with a "numerical runtime extension"; "totals with an unconfirmed goalie are barred from Rank 1" | NHL is tier A from NHL-CYCLE-4; the goalie mixture is a `SCENARIO` row; no rank bar (SEL v4 §4 says conflicting sport-file rules are historical) | SEL v4; REFERENCE_CHOICE.csv |
| R-41 | RULES_SOCCER / RULES_CRICKET competition sections | "Does not change … any gate"; maintenance under "RULES_GENERAL (archived) §3, G2"; bet and market wording | "Any selection rule"; G2 kept here; contract wording; a no-result cricket contract is VOID only under its frozen rule | SEL v4; MARKET_BLIND; RULES_REFERENCE B§7 |
| R-42 | CORE + merged METHOD | METHOD's steps 1–6 repeated CORE §3; METHOD declared v24.0 as active | Steps 7–9 kept; versions in CURRENT_STATE | GOV-v2 |
| R-43 | Prompt-1 sport files (all 11) | Receipt sentence: "after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES…", against the v24 gate (CORE, prompt core and sport file in full, other files by named section); it also named merged files | Follows the gate and names RULES_REFERENCE, PARAMETERS and the merged sport sections | CORE §3; RULES_REFERENCE A§1 |
| R-44 | CURRENT_STATE table | Method and control rows still read v24.0 / CR-2026.10.22-R2 after the v24.1 and v24.2 releases | Updated to v24.3 / CR-2026.11.07-R3 with the chain | Release notes |
| R-45 | `.gitattributes` | A `-text` entry for the root path of the extended supplied-first prompt, archived on 2026-11-07 | Entry moved to the archive path (`git check-attr` now `-text`) | Custody (R20) |
| R-46 | PARAMETERS A and B | "Script outside the repository, MD-only rule", while code may live in `ml/` | "A disclosed helper outside the repository" | Owner instruction 2026-10-14 (workshop) |
| R-47 | PARAMETERS C | Section titles "consumed by RULES_BASEBALL controls 35 and 37, G-L24, G-L19", whose rules no longer read these numbers | Index notes that those consumers were archived or rewritten (RULES_BASEBALL §8.10 checked) | Repository state |

## 2. Facts rechecked on the web (7 November 2026)

| Claim | Result | Sources |
|---|---|---|
| NBA injury report timing | Game-day report 11 a.m.–1 p.m. local (8–10 a.m. for tip-offs at 5 p.m. or earlier), except the second game of a back-to-back; adjusted in December 2025. The day-before 5 p.m. deadline was not re-confirmed (the official page now returns 404) | [official.nba.com](https://official.nba.com/nba-injury-report-2025-26/) (search snippet), [AP via News4Jax](https://www.news4jax.com/sports/2025/12/19/nba-tweaks-its-injury-reporting-rules-still-wants-changes-to-prop-betting/) |
| Premier League team sheets | Confirmed XIs at least 75 minutes before kick-off; the one-hour embargo was removed from 2024/25; EFL still 60 minutes (reports, not the current handbook text) | [Liverpool FC explainer](https://liverpoolfc.com/news/explained-premier-league-changes-2024-25-season), [Shields Gazette](https://shieldsgazette.com/sport/football/newcastle-united/premier-league-to-introduce-subtle-rule-change-that-will-impact-newcastle-united-everton-co-4670105) |
| AFL team lists | 6:20 p.m. on fixed days (Wednesday for Thursday games, Friday for Sunday, Sunday for Monday); final teams lodged by 60 minutes before the start; late changes need AFL approval; three or four emergencies still unsettled across sources | [Champion Data schedule](https://docs.api.afl.championdata.com/support/selected-team-schedule/), [AFL.com.au](https://www.afl.com.au/news/922861/more-late-changes-incoming-afl-clarifies-team-selection-rules) |
| NRL team lists | Tuesday list; two omitted 24 hours out; final 19 confirmed 90 minutes before kick-off (2026 round pages) | [NRL.com round 2, 2026](https://www.nrl.com/news/2026/03/10/nrl-team-lists-round-2/) |
| NFL inactives | About 90 minutes before kick-off: long-standing practice, not confirmed for 2026 | (no 2026 source found) |
| NHL overtime | Regular season: 5-minute 3-on-3 then a shootout of three rounds (then sudden death); playoffs: 20-minute 5-on-5 periods, no shootout (secondary sources) | [SI](https://www.si.com/nhl/nhl-overtime-rules-explained-playoffs-and-regular-season-01jnm1y8qd0e) |
| NHL empty-net share | Empty-net goals 2.4% of goals in 2005-06 against 7.0% early in 2024-25. The old claim "over 70% of two-goal wins include an empty-net goal" has no source and was removed | [Daily Faceoff](https://www.dailyfaceoff.com/news/how-empty-net-goals-have-changed-the-nhl) |

Repository facts checked: the PARAMETERS rows against COMPETITION_PARAMETERS.csv; the effect-table statuses and `E-NEED-GOALIE` in EFFECT_TABLES.csv; `PLAYER_AVAILABILITY.csv` (still header only); REFERENCE_CHOICE.csv (NHL-CYCLE-4); `ml primary verify-log` (`--manifest` optional); `ml card lint` threshold checks (`ml/picks.py`); `card-history --rank-log`; the cycle release files; no tracked JSON.

## 3. Erratum (7 November 2026 settlement documents)

The settlement revision documents written earlier on 7 November (`research/active_minis/2026101679B3FBCC8D_SETTLEMENT_REVISION_3.md`, `20261018X7Q4M9R2_SETTLEMENT_REVISION_2.md`, `20261018Q7N4T9B2_SETTLEMENT_REVISION_2.md`) each list "S19 PASS" with a meaning that S19 does not have. The first gave it as "owner-drop folder reconciled". **S19 is the v24 ledger settlement** (RESULTS.csv and ACTUALS.csv), and it is **N/A** for those pre-v24 cards. The documents are settled records and are not edited; this note is the correction. No grade, ID or settlement value is affected.

## 4. Left for the owner

1. **Regime multipliers (R-18).** The resolution follows two existing rules, but it stops v24 cards from applying the 2026-10-09 multipliers (for example NBA early season 0.988), which SELECTION_RULES had allowed. Confirm it, or ask for the multipliers to be re-estimated on verified finals as effect-table rows.
2. **External request route (R-28),** from the 7 November review §3.6.
3. **Decision lab (§5a),** from the review §3.7.
4. **R1 eight-part review for v24 cards** is applied to the first row of the most-likely list (RULES_REFERENCE A§3). This is the natural reading of prompt 3; confirm it.
5. **Competition reference sections** (soccer and cricket, last reviewed 2026-09-04) are re-verified competition by competition before each competition's first card of a new season, under their maintenance rule G2. They were not re-verified wholesale here.

## 5. Verification

- Prompt-consistency tests pass with the new suite version and the regenerated dependency map.
- No new broken links in live documents.
- Full test suite: see the commit message.
