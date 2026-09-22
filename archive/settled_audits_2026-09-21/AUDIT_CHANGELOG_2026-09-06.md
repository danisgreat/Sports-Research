# Audit change log — 2026-09-06

**Pass type:** settlement, retrospective, source audit and algorithm patch. **No forecast was issued.**
**Method produced:** `MDS-2026.09.06-v3.7` / `GFA-2` v3.7.
**Register version:** `DSR-2026.09.06-v1.7`.
**Constraints unchanged:** `SPORTS_ONLY / MARKET_BLIND`; probability state `NOT_GENERATED / NOT_PUBLISHED`; numerical program at Stage S0; no source `APPROVED FOR FEATURE`; no H0 ingestion authorised.

---

## 1. What was settled

| ID | Event | Result | Rank #1 |
|---|---|---|---|
| `P-304` | SK Slavia Praha vs FC Zbrojovka Brno, Chance Liga R7 | Slavia **4–0**, HT 1-0 | `1H Over 0.5 goals` → **WIN** |
| `P-305` | Dublin Guardians vs Amsterdam Flames, ETPL M15 | Amsterdam **169/7** beat Dublin **160/8** by 9 runs; AMF powerplay **60/1** | `Flames PP Over 51.5` (cond. met) → **WIN** |

Both potential-winner calls (Slavia; Amsterdam Flames) were **CORRECT**.

**Rows #2–#5 of both cards are `UNGRADABLE / ARCHIVAL_OMISSION`** — they were never written to any file. Recorded as lost rather than reconstructed.

## 2. Evidence gaps closed

| Item | Field recovered | Effect |
|---|---|---|
| `P-300` powerplay | ECR **28 runs, 3 wickets** (ECR batted first) | `PP Over 50.5` **LOSS**; `PP Under 50.5` **WIN** |
| `P-302-C01` | **Bournemouth 3 corners** (Newcastle 4) | `Bournemouth Over 2.5` **WIN** |
| `P-273` corners | **Palermo 3** (Mantova 2) | `Palermo Over 4.5` **LOSS**, no longer provisional |
| `P-151` corners | **Boca 11** (Lanús 3) | `Boca Over 4.5` **WIN**, no longer provisional |

## 3. Files changed, and exactly what changed in each

| File | Change |
|---|---|
| **`RULES_GENERAL.md`** | Method → `MDS-2026.09.06-v3.7`. New gates `G10.1` (structured-endpoint-first), `G10.2` (settlement-source pre-registration), `G14.2` (coaching/bench/rotation record), `G20.2` (aggregate tail budget), `G21.1` (total-row path geometry), `G26.1` (top-slot separation floor), `G34.1` (archival completeness), `G36.1` (standard-rules settlement). New §11.3F. §4 authority hierarchy gains the synthetic-content exclusion. §3 participant gate extended to bench and coaching. §11.9 checklist items 24–27 added. New §13 amendments section |
| **`RULES_CRICKET.md`** | September 6 section: ESPN cricket powerplay lane registered; runs-**and**-wickets retrieval requirement; bimodal phase-total treatment at ≥1.5 wickets/innings; powerplay-collapse and chasing-side-inflation kill paths; ordering override on high-wicket-rate phase Overs; Sept 5(b) ETPL powerplay evidence cap **withdrawn**; toss-conditional row pattern endorsed |
| **`RULES_SOCCER.md`** | September 6 section: `L-073` blanket corners cap **withdrawn** and replaced by the `G10.2` coverage test; ESPN `wonCorners` registered with verified coverage and non-coverage lists; corner-generation profile split into territorial pressure vs blocked-shot volume; substitute-goal and forced-early-substitution kill paths; `BENCH_NOT_RETRIEVED` blocks full-match total and handicap rows from Rank #1 |
| **`RULES_BASEBALL.md`** | September 6 section: ESPN `injuries[]` and umpire-crew lanes registered; tail budget instantiated on **relief innings** rather than starters; `P-297` re-attributed to the bullpen tail; bullpen-tail and early-inning-slugging kill paths |
| **`RULES_BASKETBALL.md`** | September 6 section: tail budget instantiated as pace × efficiency at the upper decile; `P-299`/`P-303` worked as the two sides of the same arithmetic; upper-decile-pace and quarter-regime-break kill paths |
| **`RULES_NRL_RUGBY.md`** | September 6 section: tail budget instantiated on tries + own goal-kicking percentage + penalty goals with the post-55' window held separately; conversion-rate-compounding, half-time-blowout and own-margin/own-total-incoherence kill paths |
| **`RULES_AFL.md`** | September 6 section: scoring shots and conversion rate budgeted as **separate terms**; `P-292` and `P-298` worked as the high- and low-conversion cases of the same structure; mismatch asymmetry stated explicitly |
| **`RULES_TENNIS.md`** | September 6 section: tail budget instantiated on **set count** rather than total games; retirement branch routed through `G36.1` when terms are unsupplied; path geometry for set/games markets |
| **`RULES_ICE_HOCKEY.md`** | September 6 section: empty-net window held as its own tail term; `P-166` and `P-200` flagged for `G36.1` closure (**not** regraded here) |
| **`RULES_AMERICAN_FOOTBALL.md`** | September 6 section: tail budget as drive count × points-per-drive in both directions, plus a separate special-teams/defensive-score term; `P-150` cited as the origin case |
| **`RULES_RUGBY_UNION.md`** | September 6 section: bonus-point-chase and penalty-count tails; sevens run per seven-minute half; bench capacity flagged as unusually load-bearing given the eight-player "finishers" bench |
| **`LEARNING_REGISTER.md`** | `L-079`–`L-086` added. `L-073` marked **`NARROWED — SUPERSEDED BY L-081`** with the falsifying evidence recorded in the row itself. Three superseded-control rows added to §4. New §3A with three frozen prospective test manifests (`C-TAIL-BUDGET`, `C-PATH-GEOMETRY`, `C-RANK2-GAP`). New 2026-09-06(b) audit disposition |
| **`DATA_SOURCE_REGISTER.md`** | `DSR-2026.09.06-v1.7`: `SRC-ESPN-SITE-API-SOCCER` / `-CRICKET` / `-BASEBALL` registered `CANDIDATE / RESEARCH ONLY` with verified field lists, verified coverage and verified **non**-coverage; Sofascore programmatic access downgraded to `BLOCKED`; synthetic-content sources prohibited; ETPL powerplay cap superseded; ČTK and iSport.cz registered |
| **`GAME_LOG_STATUS_INDEX_2026-09-05.md`** | Six rows updated in place (`P-151`, `P-273`, `P-300`, `P-302`, `P-304`, `P-305`); 2026-09-06 addendum with the revised 306-record category tally and the `T-001`–`T-013` temporary-ID register |
| **`PREDICTION_LOG_COMBINED_2.md`** | Snapshot updated (as-of, queue 17 → 11, method, component order); headline learnings block added at the top; full 2026-09-06 settlement, retrospective and Over/Under-diagnosis section appended |
| **`README.md`** | Status, framework-review date and method updated; two new rows in the document map; the "Latest settlement audit" block rewritten for September 6 |
| **`UPCOMING_GAME_RESEARCH_GUIDE.md`** | §7 acquisition order gains Rung 0 (structured keyless endpoint before any narrative page) and Rung 0.5 (settlement-source pre-registration) |
| **`EXTERNAL_LOGGING_WORKFLOW.md`** | New archival-completeness section implementing `G34.1`, with the four-step promote-and-archive check |
| **`AGENT_ROLE_AND_TASK.md`** | §6 mandatory output list extended with items 10–12 (settlement endpoint per row; coaching/bench/rotation record; tail budget, path geometry and separation-floor result) |
| **`LEAGUE_RULES_CRICKET.md`** | ETPL mandatory powerplay confirmed as `Overs 0.1–6.0`; the two observed rain-reduced variants (1.3-over, 3.4-over) recorded as a `GATE-CONTRACT` settlement hazard; the ETPL 2026 six-over powerplay population recorded as a reference base rate |
| **`IMPROVEMENT_PLAN_2026-09-06.md`** *(new)* | The comprehensive improvement document: settlement, deep retrospective, the three validation questions answered, document-by-document review, source lanes, the Over/Under diagnosis and fixes, and an explicit "what this pass did not do" section |
| **`archive/PREDICTION_MINI_LOG_12_P304_P305_SETTLED_2026-09-06.md`** *(new)* | Archived mini-log component for this settlement pass, with the `G34.1` completeness declaration |
| **`AUDIT_CHANGELOG_2026-09-06.md`** *(this file, new)* | — |

## 4. Controls adopted

| ID | Status | Control |
|---|---|---|
| `L-079` | `PROMOTED_PROCESS` | Synthetic/simulated/preview/fantasy content is tier E and may never settle a contract; results come from scoreboard/scorecard records, not narrative articles; a search-result summary is not a source |
| `L-080` | `PROMOTED_PROCESS` | Structured keyless endpoints are queried before any narrative page |
| `L-081` | `PROMOTED_PROCESS` | Derivative-row gradability is a competition-coverage test, not a market-type ban. **Narrows and supersedes `L-073`** |
| `L-082` | `PROMOTED_PROCESS` | Coaching, bench and rotation-capacity record; `BENCH_NOT_RETRIEVED` blocks margin and full-game total rows from Rank #1 |
| `L-083` | `PROMOTED_PROCESS` | Bimodal phase-total treatment where the phase possession-loss rate is ≥1.5 per innings |
| `L-084` | `PROMOTED_PROCESS` (disclosure) / `CANDIDATE` (ordinal) | Aggregate upper-/lower-tail budget |
| `L-085` | `PROMOTED_PROCESS` (disclosure) / `CANDIDATE` (ordinal) | Total-row path geometry |
| `L-086` | `PROMOTED_PROCESS` | Archival completeness for unsettled cards |

Three prospective test manifests frozen: `C-TAIL-BUDGET-v1` (60 events), `C-PATH-GEOMETRY-v1` (40 within-event pairs), `C-RANK2-GAP-v1` (100 cards, with a standing bar on reordering any slate while open).

## 5. Validation performed

| Check | Result |
|---|---|
| `P-304` result | Two independent Czech-language sources (ČTK match report; iSport.cz progressive headline sequence on the same article URL) agree on FT 4-0, HT 1-0 and the 38th-minute first goal |
| `P-305` result and powerplay | Three independent endpoints agree — ESPN cricket `summary` `notes`, ESPN cricket `scoreboard`, ESPNcricinfo full scorecard. Fall-of-wickets arithmetic independently consistent with the 60/1 powerplay note |
| `P-300` powerplay | ESPN cricket `summary` `notes` (28 runs, 3 wickets) cross-checked against ESPNcricinfo fall of wickets (3 down by 2.6 ov, 4th at 8.4 ov) — consistent |
| `P-151` corners | ESPN `wonCorners` 11–3 exactly reproduces the previously specialist-only figure, from an independent lineage |
| ESPN coverage claims | Every "covered" and "not covered" claim in `DATA_SOURCE_REGISTER.md` §September 6 was produced by an actual HTTP request this session and its status code recorded |
| Ledger arithmetic | 306 index rows re-parsed programmatically: 285 settled + 9 partial + 3 research-settled + 1 unresolved + 7 admin-closed + 1 terminal = 306 |
| Cohort tally | Rank #1 9 W / 8 L enumerated by ID in the log section; Rank #2 7 W / 3 L reproduced from the 2026-09-05(b) settlement table |

## 6. Honest limitations of this pass

1. **No probability was generated or published.** Track B remains at Stage S0. The ESPN lane is `CANDIDATE / RESEARCH ONLY` and its promotion toward `APPROVED FOR FEATURE` requires an explicit user decision at the S1 gate.
2. **No predictive-lift claim.** Every count here is descriptive.
3. **Eight ranked rows are permanently lost** (`P-304` and `P-305`, ranks #2–#5). They are recorded as `UNGRADABLE / ARCHIVAL_OMISSION`, not reconstructed.
4. **Thirteen follow-ups remain open** (`T-001`–`T-013`). Nine share a single cause — four competitions carried by no reachable structured provider. Four are contract-terms questions now closeable under `G36.1`, **flagged rather than regraded**, because changing a historical settlement should be a deliberate decision and not a side effect of a rule change.
5. **`L-084` and `L-085` are disclosures, not weights.** Their ordinal effect waits on the frozen prospective tests. `L-084` is explicitly recorded as a humility gate that will flag rows that go on to win.
6. **The consolidation pass recommended in `IMPROVEMENT_PLAN_2026-09-06.md` §D.3 was not performed.** Merging five dated amendment sections into the numbered gates of a controlling document is a large edit and should be an explicit decision.

---

## Addendum (c) — external blindspot audit received and integrated, same day

**Trigger:** the user supplied an externally produced governance/blindspot audit (`SPORTS_RESEARCH_FULL_BLINDSPOT_AUDIT_P001_P305_2026-09-06.md`, a Google-Drive read-only, no-web-research review) identifying 15 blindspots (`B-01`–`B-15`), and instructed that all its learnings be added to the relevant Markdown documents.

**Received document preserved:** [`archive/EXTERNAL_BLINDSPOT_AUDIT_2026-09-06_RECEIVED.md`](archive/EXTERNAL_BLINDSPOT_AUDIT_2026-09-06_RECEIVED.md), with a provenance header noting one factual discrepancy (its "P-304/P-305 still live" claim predates this repository's own same-day settlement of both) and a note on uncorrected character-encoding artifacts in the received text.

**Files changed in this addendum:**

| File | Change |
|---|---|
| `LEARNING_REGISTER.md` | `L-075`/`L-076`/`L-077` annotated in place with a governance split (disclosure stays `PROMOTED_PROCESS`, magnitude reclassified `CANDIDATE`), per `B-01`. New lessons `L-087`–`L-101`, one per blindspot. New §2 control-taxonomy note. New "2026-09-06(c) external blindspot audit disposition" section. New `C-WEIGHT-PROPAGATION` prospective test manifest in §3A |
| `RULES_GENERAL.md` | Method → `MDS-2026.09.06-v3.8`. `G23` row-robustness record gains a `rank_gap` field (`L-088`). New `G37.1` two-pass result-blind retrospective discipline (`L-089`). §4 bookmaker-independence gate gains a price-blind/market-analysis-blind terminology clarification (`L-100`). New §14 amendments section |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | New addendum requiring the settlement-only scorecard to be stratified by method version, horizon, sport, target family and event/decision-set weighting before any headline figure is presented (`L-090`) |
| `AGENT_ROLE_AND_TASK.md` | §7 post-match duties extended with `ISSUE_TIME_PROCESS_GRADE` / `OUTCOME_DRIVER_GRADE` (two-pass), `CURRENT_RULE_GAP`, `rank_gap`, and the weighting-firewall reminder |
| `RULES_RUGBY_UNION.md`, `RULES_ICE_HOCKEY.md`, `RULES_AMERICAN_FOOTBALL.md` | Evidence-density label `SPARSE` added to the header block (`L-099`) |
| `RULES_NRL_RUGBY.md` | Evidence-density label `MODERATE` added to the header block (`L-099`) |
| `GAME_LOG_STATUS_INDEX_2026-09-05.md` | New addendum formally tagging the `P-241`–`P-267` cohort `REPRODUCIBILITY-LIMITED` (`L-101`) and cross-referencing the received audit |
| `DATA_SOURCE_REGISTER.md` | New table tracking unresolved-rate by market/source-tier class (`L-093`) |
| `README.md` | Framework-review line and document map updated to reference the received audit and its disposition |

**What this addendum did not do, stated plainly:**

- It did **not** reopen, re-rank or re-settle any historical card. `B-01`–`B-15` are governance findings about how the framework is run, not new evidence about any specific event's outcome.
- It did **not** retro-classify the 86 lessons that predate `L-095`'s new control taxonomy (`BLOCKING_INTEGRITY` / `MECHANISM_REQUIRED` / `CONTEXT_MATERIALITY`). That full pass is explicitly named as deferred future work rather than silently skipped.
- It did **not** narrow `EP-2026.09.06-v2`'s settlement-only performance-eligibility gate. `L-090` adds a stratification *reporting* requirement on top of it; it changes how the eligible pool is presented, not who is in it.
- It did **not** attempt to algorithmically repair the character-encoding corruption in the received document's text (a bare "â" standing in for an em dash, "Ã©"/"Ã³"/"Ã¸"-style digraphs for accented Latin letters). A confident, verified byte-level reversal was not available, and guessing risked silently fabricating text into an evidentiary record; the corruption is preserved and flagged instead.
- It did **not** re-transcribe the received document's full per-ID event appendix a second time into the archive file, since every distinct finding it supports is already cited by ID through `B-01`–`B-15` and those same IDs are already fully documented in this repository's own canonical logs.

**Validation performed:** every new lesson ID (`L-087`–`L-101`) was checked for uniqueness against the existing register before insertion; the `C-WEIGHT-PROPAGATION` manifest was checked against the existing `§3A` format for consistency with `C-TAIL-BUDGET`/`C-PATH-GEOMETRY`/`C-RANK2-GAP`; every cross-reference from `RULES_GENERAL.md` §14's table to a `LEARNING_REGISTER.md` lesson ID was confirmed to resolve to an actual row.

---

## Addendum (d) — second independent review, verification and self-correction

**Trigger:** the user supplied a second local document (`GAME_LOG_BLINDSPOT_REVIEW_2026-09-06.md`, found already at the repository root) and asked for it to be fully reviewed and merged, same as addendum (c).

**Discipline applied:** every one of the 30 findings (`F01`–`F30`) was checked against primary source — the settlement table, the ESPN API records retrieved earlier in this session, and the raw preserved component text — before any correction was made. Several findings pointed at genuine errors in **this session's own immediately preceding work**, including three gates (`G20.2`, `G21.1`, `G26.1`) adopted the same day that reintroduced the exact same-session-ordinal-rule pattern the framework had just adopted a firewall (`L-087`) to prevent. That is recorded plainly rather than minimised.

**Corrected, all verified against primary source:**
- The O/U diagnosis (contradicted its own settlement table) — `L-102`.
- Five settlement rows recorded as missing that were fully recoverable (`P-288`, `P-290`–`P-293`) — `L-103`.
- The Rank #1/#2 comparison population (10-card incomplete → 15-card matched: 7/15 vs 10/15) — part of `L-103`.
- `G20.2`/`G21.1`/`G26.1`'s undisclosed hard ordinal bars, withdrawn and reclassified `CANDIDATE` — `L-104`.
- Nine sport-specific tail-budget formulas failing a dimensional check — `L-105`.
- `G21.1`'s union/intersection category error — `L-106`.
- `G20.2`'s "already-observed combination" overclaim — `L-107`.
- `G25.1`'s blanket `DISJOINT` ban (counterexample exists) — `L-108`.
- `G30.1`'s cushion-to-winner overclaim (counterexample exists) — `L-109`.
- A false general claim in `P-291`'s preserved reasoning text — `L-110`.
- An incomplete/mislabelled ETPL reference population (Match 12 mislabelled as 13) — `L-111`.
- An overclaimed "bimodal" statistical shape from n=2 — `L-112`.
- `DATA_SOURCE_REGISTER.md` §6A's overstated "cannot fail" fallback claim — `L-113`.
- An unsupported causal claim about `P-300` using a different match's results — `L-114`.
- `P-303`'s corridor-containment overclaim (falls outside on all four bounds) — `L-115`.
- A team-identity swap (Spain/Mali) in a basketball retrospective — `L-116`.
- Knowability-timestamping reinforcement — `L-117`.
- `G14.2`'s origin story (was partially pre-existing, not wholly absent) — `L-118`.
- `G36.1` split into separate `RESEARCH_GRADE`/`OPERATOR_ACTION` fields — `L-119`.
- Method/version precedence statement — `L-120`.
- Cross-reference confirming `L-090` already answers the "no reliable pooled strike rate" finding — `L-121`.

**Also discovered and repaired, unrelated to the review's own findings:** `RULES_BASEBALL.md`'s entire "September 6 settlement learning" section (written earlier this session) had been lost from the working file at some point before this pass — confirmed by byte-size comparison and a targeted content search. Restored with the `F10` baseball correction (innings-conservation, dual-branch check) incorporated directly rather than restored verbatim and corrected separately. A full re-verification of every file this session had touched found no other such loss.

**What was checked and found already adequate:** `F05`, `F17`, `F20`, `F23`–`F26`, `F30` — no new mechanism created; cross-referenced to existing controls. `F04`'s apparent accounting inconsistency traced to a superseded interim figure.

**What this pass did not do:** it did not change any settled card's contract outcome; it did not re-litigate the ~200-row P-001–P-200 game-by-game table the review supplied individually; it did not resolve the `P-099`/`P-115`/`P-171` ETPL population gap (flagged, not fabricated); it did not retro-classify the 86 pre-`L-095` lessons; and it did not accept any of the review's numerical claims without independent re-derivation first.

**Documents changed:** `RULES_GENERAL.md` (→ `MDS-2026.09.06-v3.9`, new §15), all ten `RULES_<SPORT>.md` files, `LEARNING_REGISTER.md` (`L-102`–`L-121` plus in-place corrections to `L-076`/`L-097`), `DATA_SOURCE_REGISTER.md`, `LEAGUE_RULES_CRICKET.md`, `IMPROVEMENT_PLAN_2026-09-06.md`, `PREDICTION_LOG_COMBINED_2.md`, `GAME_LOG_STATUS_INDEX_2026-09-05.md`, `README.md`, and new `archive/GAME_LOG_BLINDSPOT_REVIEW_2026-09-06_RECEIVED.md`.

## 2026-09-06(f) — settlement and retrospective addendum

Completed user-requested Drive/local unsettled-log reconciliation and per-game retrospective. [Full mini log](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md); validation and changed files (historical artifact `audit_2026-09-06_retrospective/VALIDATION_AND_CHANGES.md` is absent from this checkout). Ten research rows newly recovered/resolved (5 W/5 L), including seven P-304/P-305 ranks, P-290 corners and two P-217 full-innings rows. Nine result-evidence gaps remain honestly open, with four special operator-only follow-ups separately retained. No new ID conflict, no Drive writes, no original-card edits, no fitted-rule promotion. Canonical snapshot and relevant MD companions updated together.
