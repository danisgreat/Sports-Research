# Changelog

**Opened 2026-09-25(c).** This is the project's dated history. Until 2026-09-25(c) it lived in the body of `README.md`, which had grown into about twenty dated sections. That buried what the project is and how to use it. The complete former README body is preserved **verbatim** below, in its original order (SHA-256 of the whole former README: `003a7eaecb6b64e70a28811449a34e5f4a7572ef03dffca621675c7d200a9b71`). Its links are unchanged and still resolve, because this file sits in the same folder.

New entries go at the top, under **Entries from 2026-09-25(c)**. The governing rules live in [`CURRENT_RULES.md`](CURRENT_RULES.md) and the files it cites; this changelog is history, not instruction (`METHOD.md` §9).

## Entries from 2026-09-25(c)

### 2026-09-25(e) — Rank 1 and Rank 2: the ranking model, the team baseline, oval references, settlement integrity

- **Ask.** A sport-by-sport review of sources and reasoning, to make Rank 1 and Rank 2 far more likely to win than lose, and a new probability model if one could be built.
- **Data fixes.**
  - The settled-row extractor was reading narrative columns: 17 rows had been graded the wrong way round and 55 dropped. P-514 was classed as NPB.
  - The dataset is rebuilt: 1,264 rows; 641 with p.
- **RM-1** (`tools/rank_model.py`; user-authorised `L-087` exception).
  - The model: logit(q) = −0.187 + 1.543·logit(p) − 1.127·[a +k.5 cushion outside baseball, hockey and soccer].
  - It beat the stated p on log loss in grouped CV and in four forward splits.
  - Ranking by q raised held-out top-two wins by +0.068 per card [+0.007, +0.128] and never lowered Rank 1 or Rank 2 in any forward split.
  - A per-sport/per-class challenger failed.
  - Controls: `C-RANK-MODEL`, `C-TOP2-QUALITY` (`SLATE_ADVISORY`).
- **TB-1** (`tools/team_baseline.py`).
  - A leak-free team-strength baseline, validated on 12 league-seasons plus 1,704 newly pulled NFL, AFL and NRL games.
  - It has resolution for sides in NBA, WNBA, NBL, NFL, AFL, NRL and EPL (5–19% Brier) and for NBA, WNBA and NFL totals; none in MLB or the NHL.
  - Control: `C-TEAM-BASELINE`.
- **References.**
  - The first NFL, AFL and NRL population rows, and the NFL key numbers.
  - Underdog-cushion cover rates by league (`BASE_RATES_REGISTER.md` §7.7). A small cushion on the weaker team covers 32–54%: the mechanism of M32.
  - `C-PLUS-CUSHION` amended.
- **Settlement integrity.**
  - The P-510–P-515 settlement had been script-typed. P-510, P-511 and P-514 lineup diffs were false; P-515's score was 36–20, not 36–14. Grades are unchanged.
  - New controls: `C-SETTLEMENT-FROM-FEED` and audit field `10n`.
  - P-514 is a `LINEUP_CLAIM_FALSE` process defect.
  - P-510–P-515 are imported into Part 5 §"2026-09-25(f)"; that mini log is archived; the next ID is P-516.
- **Sources.** Verified and admitted: ESPN NFL, AFL and NRL scoreboards; ESPN team schedules; the KBO English scoreboard; the NPB official score page. The NRL team schedule returns HTTP 500.
- **Audit.** New fields `RM`, `TB` and `10n`.
- **Sport files.** Each has a §"2026-09-25(e)".
- **Receipt.** `CONTROL_MANIFEST_2026-09-25-5.md`.

### 2026-09-25(d) — review of every settled log: calibration findings, construction tools

- **Dataset.** `research/settled_rows_2026-09-25/` extracts every graded row from Parts 1–5: 1,185 rows from 307 cards, 600 with probabilities from 149 cards. It reproduces the logged cohort figures.
- **Findings.**
  - Calibration overall is good: Brier 0.2249, slope 1.06, reliability 0.002. Skill is modest (resolution 0.019).
  - The skill sits at p ≥ 0.65 (80.3% won); 0.50–0.65 is coin-flip-grade (53.6%).
  - Non-baseball underdog cushions are over-confident: 17/40 at 0.642.
  - Soccer shows clear skill; MLB and basketball near-zero resolution; tennis, NFL/NCAA and AFL none.
  - Ranks #2–#4 are indistinguishable. Top-two joint failure equals independence.
- **Controls.** `C-PLUS-CUSHION` (CANDIDATE, audit field `PC`, M32), `C-DEPARTURE-LEDGER` (audit field `DL`), `C-TRACK-RECORD`, `C-LOW-RESOLUTION-BAND`, and the `SCORING_AND_VALIDATION.md` §14 review standard.
- **Tools.** `tools/card_math.py`: normal, negative-binomial, Poisson and Skellam queries, `no_zero` margins, push mass, exact joints, and the departure ledger. It reproduces the issued P-509 and P-500 probabilities. `tools/calibration_report.py`: reliability, Murphy decomposition, slope, card-cluster slices. A canonical settlement table format.
- **Tests.** `T-PLUS-CUSHION`, `T-TOTAL-DIRECTION-LEAGUE`, `C-LOW-RESOLUTION-BAND`; interim rows for `C-PROB-EXTREMITY` and `C-PHASE-VS-FULL-TOTAL`.
- **Receipt.** `CONTROL_MANIFEST_2026-09-25-4.md`.

### 2026-09-25(c) — repository hygiene, CI, current-rules summary, baseline skill check

- **Hygiene.** Untracked 16,142 files: two `node_modules` trees in `.codex_spreadsheet_tmp/`, a retired runtime's `node_modules`, `__pycache__`/`.pyc` and `.claude/settings.local.json`. They stay on disk. Added `.gitignore` and `.gitattributes` (CRLF checkout everywhere, so manifest hashes reproduce on any platform) and `LICENSE` (all rights reserved; third-party note). Removed three betting domains from the local permission allowlist. Fixed two literal-`\n` rendering bugs (README custody table; RULES_GENERAL header).
- **CI.** `.github/workflows/checks.yml` runs every test, `tools/repo_hygiene.py`, `tools/verify_manifest.py` and the strict card audit of the active mini logs on every push and pull request.
- **Tools.** `tools/verify_manifest.py`, `tools/make_manifest.py`, `tools/repo_hygiene.py`, `tools/skill_baseline.py` (with tests). `audit_card_controls.py` gains `--allow-empty` and field `BP`.
- **Docs.** `CURRENT_RULES.md` is the live operating summary and step 0 of the reading gate. `README.md` is rewritten as an overview and quickstart. `CONTRIBUTING.md` covers the branch/PR workflow, commit conventions and local checks.
- **Skill check.** `SKILL_BASELINE_LEDGER.md` and `C-BASELINE-SKILL`. The seed comparison of 29 decisions from 9 cards shows no demonstrated skill over a naive population baseline: card Brier 0.2461 v baseline 0.2360, interval [−0.059, +0.089].
- **Receipt.** `CONTROL_MANIFEST_2026-09-25-3.md`.

## Former README body (verbatim, as of 2026-09-25(b))

Current method: **MDS-2026.09.19-v4.3**, control revision **CR-2026.09.21-3**. All existing game logs remain **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. This project records research forecasts, exact settlement evidence and testable model improvements in Markdown; no numerical model is fitted or validated yet.




<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
## Universal event-verification gate — CR-2026.09.19-4 component (preserved under CR-2026.09.21-3)




Every new sports event now requires **at least three distinct reliable upstream source lineages**. Mirrors, syndicated copies, reposts, search-result snippets and generated summaries do not create independent verification.




Before issue or refresh, verify the official venue-local date/time and IANA timezone, then convert that exact instant to `Australia/Melbourne`, recording the correct **AEST/AEDT** label and any calendar-date rollover. User-supplied start times are estimates until independently verified.




Settlement requires **three independent reliable lineages** agreeing on the exact event/date, explicit terminal state and final result. A score without a terminal marker is insufficient; any credible current live/in-progress source or material source conflict blocks settlement. P-469 is the reference false-final incident that prompted this gate.




The executable preflight now enforces source-count/lineage diversity, event time-zone conversion and normal pregame state before a new card can pass.




## Cricket source-control implementation — 2026-09-21




**CR-2026.09.21-1** preserves the current forecasting method and CR-4 cross-sport gates while repairing cricket source retrieval.




- Separate `TOSS STATUS`, `STRIP STATUS` and `MATCH CONDITIONS STATUS`.
- Use field-owner match centres first for the toss; add verified board/competition/rightsholder video and sanctioned NV Play/board-branded Match Centre to the late-information ladder.
- Only named current-match P1–P5 sources in `RULES_CRICKET.md` §2 can establish today's strip. Previous same-venue matches, venue averages and ICC post-match ratings are context.
- A transcript and its underlying broadcast are one lineage. Identical/near-identical unusual pitch metadata across front ends is one suspected upstream feed until provenance proves independence.
- `AUTOMATED_PITCH_METADATA` cannot masquerade as an observed strip.
- `INSUFFICIENT_VENUE_HISTORY` is valid; no fabricated venue sample.
- Official dynamic pages are field-specifically stale when fresher reliable evidence proves the displayed state is outdated.
- Toss-window and final pre-issue refreshes are required.




See [Cricket rules](RULES_CRICKET.md) §2, [source register](DATA_SOURCE_REGISTER.md) §6A, [sources](SOURCES.md), [research guide](UPCOMING_GAME_RESEARCH_GUIDE.md), [implementation ledger](archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-21.md), and [control manifest](CONTROL_MANIFEST_2026-09-21.md). This is an integrity/retrieval change; no predictive-lift claim is made.








## Current canonical rollover — 21 September 2026




Part 4 is closed at P-481. Part 5 (`PREDICTION_LOG_COMBINED_5.md`) is the active queue/next-ID authority; the rollover next ID is P-482. `GAME_LOG_STATUS_CURRENT.md` is the current state register. All current log material remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.




## Historical state snapshot — 17 September 2026(c) *(superseded for active queue state)*




- Active canonical log remains [Part 4](PREDICTION_LOG_COMBINED_4.md). **Do not use this README to infer the next ID**; read the top Part-4 snapshot or the active mini-log reconciliation. P-372 remains reserved/unused.
- **No live event; 23 primary result/derivative handles plus 5 separate documentary/period follow-ups.** The top Part-4 snapshot is the sole queue/next-ID authority. The [status register](GAME_LOG_STATUS_CURRENT.md) provides the per-ID details.
- P-255-C05/P-256-C05 are **UNRESOLVED_PERIOD**. Whole-match corner counts do not prove their regulation Overs; existing audit handles -03/-04 are reopened. Other recorded rows remain unchanged.
- Corrected legacy scorecard: **477 rows, 114 cards, 273 W/204 L, mean 0.2265475891**. PRIMARY_SCORED subset: **136 rows, 33 cards, mean 0.246825**. P-344's mean is **0.283425**. These are descriptive legacy diagnostics, not improved-model results or calibration evidence.
- C-OU-GEOMETRY has **zero verified prospective cards** under the required timestamp/control-version join. Historical imports are development evidence.




## Audit and implementation - 2026-09-19




**Tested the bounce-back hypothesis empirically and it does not hold.** MLB 2026, 4,594 team-games and 108 starters: after a 0-run game teams score **0.102 runs BELOW** their own mean next time (95% CI [−0.456, +0.251]); top-10 offences behave no differently from bottom-10 (−0.126 vs −0.093); a starter's next-start ER after being hit for 6+ lands **−0.017** from his own average and his strikeouts do **not** spike (−0.070). Out-of-sample, shorter recency windows predict monotonically **worse** — last-1 RMSE 2.7677 against a flat league constant's 1.9844. New document [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md) and control **`R-1`**: recent results revise an estimated *rate* through a named mechanism, never forecast a *deviation*.




- **New user directive implemented:** a loss **or push** on the card's highest-ranked over/under now triggers the same enhanced failure review as a Rank #1 loss (`METHOD.md` §7, logged as `TOP_OU_REVIEW`).
- **Social media tested directly, and it fails.** X: HTTP 200 login wall, 1,644 chars of visible text, zero post content; syndication lane 0 bytes; jina proxy 403 abuse-blocked. Reddit: interstitial, no JSON. Bluesky: API works but **6 of 6 sports handles failed identity** — `jeffpassan.bsky.social` is a squatter who posts *"I continue to not be Jeff Passan"*, `fabrizioromano.bsky.social` is a different Fabrizio posting in Turkish. New control **`S-1`**.
- **Press conferences (`S-2`):** admissible for availability, workload and role intent; never a signed adjustment to pace, efficiency or scoring rate.
- **Three structured lanes added instead:** MLB `hydrate=lineups` (distinguishes `LINEUPS_NOT_YET_PUBLISHED` from a `RETRIEVAL_MISS` — most prior flags were the former), `boxscore` `battingOrder`/`bench`/`bullpen`, and **debutant detection** via MLB `mlbDebutDate` and ESPN cricket `debuts[]`. A 6-day rookie batted 6th in `P-455` unflagged.
- **Cricket pitch-ladder drift repaired prospectively by CR-2026.09.21-1:** toss facts and exact-strip evidence now use separate ladders; preceding same-venue matches remain different-strip context unless reuse is confirmed; official video/NV Play are explicit late-information lanes; duplicate structured pitch feeds are one lineage; `INSUFFICIENT_VENUE_HISTORY` is legitimate.
- **One recorded success reclassified:** `P-453`'s Rank #1 rested on three-start form — the third-worst predictor measured. Directionally lucky, not validation.




[Recency & rebound](RECENCY_AND_REBOUND.md) · [Controls](CONTROLS.md) · [Sources](SOURCES.md) · [Forecast preflight manifest](FORECAST_PREFLIGHT_MANIFEST.md) · [Control manifest](CONTROL_MANIFEST_2026-09-19.md).




## Audit implementation




[Implementation ledger](archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-17.md) · [Original model review](archive/audit_documents_implemented_2026-09-25/MODEL_REVIEW_2026-09-17.md) · Original evidence (`audit_2026-09-17_models/REVIEW_EVIDENCE.md`, not present in this repository) · Validation and control hashes (`audit_2026-09-17_implementation/VALIDATION.md`, not present in this repository).




The revision fixes integer push scoring, removes unsupported MLB run-line/push caps and fixed variance floors, corrects extra-inning completion logic, replaces overlapping-window pseudo-tests, permits declared hierarchical uncertainty, and prevents numerical row caps from contradicting a printed distribution. It preserves frozen issued predictions and appends settlement/score corrections. The old README's dated history is preserved in the before snapshot (`audit_2026-09-17_implementation/before/README_with_margin_band_addition.md`, not present in this repository); it is not current policy.




## Read first




| Document | Purpose |
|---|---|
| [METHOD](METHOD.md) | Single workflow, six-field forecast object, current authority and honesty rules |
| [Scoring and validation](SCORING_AND_VALIDATION.md) | Exact W/P/L/action conditioning, decision/event denominators, baseline comparison and prospective admission |
| [Controls](CONTROLS.md) | Compact current gate index and candidate dispositions |
| [General rules](RULES_GENERAL.md) | Detailed gate definitions and historical origins; METHOD replaces repeated presentation lists |
| Relevant RULES sport file and competition file | Sport-native exposures, state transitions, endpoints and source requirements |
| [Sources](SOURCES.md) / [full source register](DATA_SOURCE_REGISTER.md) | Field-owner routes, availability and numerical admission requirements |
| [Learning register](LEARNING_REGISTER.md) | Historical observations, current dispositions and prospective manifests |




## Numerical model work




| Document | Purpose / real state |
|---|---|
| [Numerical program](NUMERICAL_PROGRAM.md) | MLB A0/A1 first, soccer phase/full-match second; one stage/publication sequence |
| [Implementation recipes](MODEL_IMPLEMENTATION_RECIPES.md) | Executable empirical/count/scoring/phase/extra-state primitives and sport-specific estimation specifications inside Markdown |
| [H0 dataset card](H0_DATASET_CARD.md) | Restored root dependency; schema and source/time-join gates; NOT BUILT / NOT QUALITY-APPROVED |
| [Numerical model register](NUMERICAL_MODEL_REGISTER.md) | Existing models plus explicit tennis/union scopes; all NOT FIT; M0/M1 retired; advanced models dormant |
| [Training specification](NUMERICAL_TRAINING_SPEC.md), [model/data specification](MODEL_AND_DATA_SPEC.md), [algorithm portfolio](ALGORITHM_PORTFOLIO_AND_EVALUATION.md) | Detailed design reference under the current method, scoring specification and numerical program |
| [Base-rates register](BASE_RATES_REGISTER.md) | Historical reference estimates with populations and provenance; never universal matchup limits |




The user has authorized the audit implementation and asked for improvements within Markdown as far as possible. No new permission gate is imposed on this work. Real data admission, fitting, held-out comparison and future prospective shadow cannot be claimed as completed by writing their specifications. No external data was pulled or fitted for this implementation. The supplied calculation tests are synthetic correctness checks, not measured prediction gains.




## Canonical custody




| Part | Coverage | Custody |
|---|---|---|
| [Part 1](PREDICTION_LOG_COMBINED.md) | P-001–P-271 | Closed; settlement corrections only, including reopened P-255/P-256 period questions |
| [Part 2](PREDICTION_LOG_COMBINED_2.md) | P-272–P-332 | Closed; nine inherited primary follow-up handles |
| [Part 3](PREDICTION_LOG_COMBINED_3.md) | P-333–P-423; P-372 reserved | Closed; 13 primary follow-up handles |
| [Part 4](PREDICTION_LOG_COMBINED_4.md) | P-424–P-481 | Closed at P-481; historical custody and unresolved follow-up handles remain tracked in the status register |
| [Part 5](PREDICTION_LOG_COMBINED_5.md) | P-482 onward | **ACTIVE queue / next-ID authority** |




The [current status register](GAME_LOG_STATUS_CURRENT.md) supersedes dated status indexes for current questions. Older component logs, archived mini variants and dated audits remain evidence; they do not create extra forecasts or new instructions. Preserve canonical IDs and temporary aliases. Follow [external-log workflow](EXTERNAL_LOGGING_WORKFLOW.md) for variant discovery, reconciliation and archival.




## Complete Markdown recording




Record every substantive change, source status, lesson, forecast, settlement correction and validation result in Markdown. Preserve issued records and immutable archival copies. Do not invent missing probabilities, lineups, timestamps or model outputs. Odds and market analysis never enter the SPORTS_ONLY / MARKET_BLIND forecast. Missing validated probabilities or required prices/terms means **NO VALUE DETERMINABLE**.




<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## Deep-research implementation — 19 September 2026




This revision makes the project **strictly market-independent at prediction time** and converts the audit findings into blocking controls.




- **Hard source firewall:** sportsbook/bookmaker material, odds aggregators, betting previews/picks/tipsters, prediction-market sentiment, fantasy/DFS projections/rankings/ownership/start-sit advice, and secondary material derived from those sources are **PROHIBITED as predictive evidence**. RotoWire, RotoGrinders and FPTrack are explicitly prohibited. They may only be used as discovery pointers to an upstream valid source; if the upstream fact cannot be recovered, the fact is `UNAVAILABLE`.
- **Threshold quarantine:** a user-supplied total/spread/alternate line is contract metadata only. It is kept out of priors, features, model inputs, scenario weights, calibration and narrative direction until the independent sports-outcome distribution has been frozen. Only then is the line queried.
- **Point-in-time provenance:** every material predictive fact records source class, field owner, upstream lineage, publication/first-known time, retrieval time, cutoff compatibility and freshness. Mirrors that share one upstream feed count as one lineage.
- **Fail closed:** contaminated source, post-cutoff fact, stale critical state, missing lineage, line leakage, postgame leakage or method/control-version mismatch blocks a normal forecast rather than merely lowering confidence.
- **Distribution-first evaluation:** future numerical builds are evaluated with distribution scores (CRPS/RPS/log score where applicable), W/P/L Brier/log loss, RMSE/MAE, interval coverage/width and calibration diagnostics, with chronological event-grouped validation. Hit rate and Rank@k remain secondary diagnostics.
- **No performance claim from documentation changes:** these controls are expected to reduce leakage and false confidence, but no accuracy improvement is claimed until a frozen out-of-sample/prospective comparison demonstrates it.




Executable gate: [`prediction_preflight.py`](prediction_preflight.py). Full rationale and implementation record: [`archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-19.md`](archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-19.md).




## Final implementation synchronization — CR-2026.09.19-3




CR-3 is a **control/read-back synchronization revision**, not a new forecasting method. It removes stale active references to v4.1/v0.4 and obsolete hard-coded next-ID state, aligns the preflight schema/executable with the current authority, and records a fresh control-file receipt. Forecasting semantics remain MDS-2026.09.19-v4.2.




This synchronization does **not** establish predictive skill. H0 remains not built/quality-approved and no numerical model has been fitted, calibrated, held-out validated or prospectively promoted.




<!-- ALL-SPORTS-AUDIT-RECONCILIATION-2026-09-21-CR2 -->
## All-sports historical-audit reconciliation — CR-2026.09.21-2




[`archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md`](archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md) is the current supersession/duplication ledger for historical audit findings across baseball, cricket, soccer, basketball, AFL/AFLW, rugby league, rugby union/sevens, American football, ice hockey and tennis. It prevents an older finding from being reintroduced after later evidence rejected or narrowed it, and prevents an already-implemented finding from being double-counted.




This reconciliation does not claim improved prediction accuracy and does not complete empirical tasks by documentation. H0 remains not quality-approved; no numerical champion is promoted; non-MLB rebound/recency magnitudes remain un-derived; and historical settlement/documentary gaps remain separate operational work.








## All-sports live-rule cleanup — CR-2026.09.21-3




CR-3 removes residual active wording that conflicted with the CR-2 supersession ledger, synchronizes the active log to Part 5 / P-482, and aligns the preflight control revision. Current analysis is distribution-first; rejected historical shortcut rules remain provenance only. This is a governance/consistency correction, not a predictive-lift claim.


<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-23 -->
## Consolidated mini-log import — 23 September 2026

- Four mini-log files were consolidated, settled and imported to Part 5 §"2026-09-23(c)":
  - **P-489**: the 22 Sep game 24, DeNA 7–3. Rank #1 Under 6.5 lost; `TOP_OU_REVIEW`.
  - **P-491**: Orix 1–0; both top rows won.
  - Two temporary-ID records: the NBL card and a previously unregistered WNBA card, which both claim **P-487**. P-487 is held.
- The P-489 "R1" was a **different game** (23 Sep game 25) and is now `TMP-20260923-NPB-CHU-DB-G25`.
- Live records (TMP-G25, P-493, P-494) were carried unsettled to the new active mini log, `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-495 onward - 2026-09-23/`.
- The consolidated log is archived at `archive/mini_logs/Mini Prediction Log - P-487 to P-494 CONSOLIDATED - 2026-09-23/`.
- Content receipt: [CONTROL_MANIFEST_2026-09-23.md](CONTROL_MANIFEST_2026-09-23.md). Method and control revision are unchanged (MDS-2026.09.19-v4.3 / CR-2026.09.21-3).
- Everything remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.


<!-- AUDIT-2026-09-24F -->
## Verification audit of the P-495–P-508 import — 24 September 2026(f)

**Scope.**
- A peer session settled TMP-G25 and P-493–P-508 at 22:47 AEST (`cb95acd`).
- This pass re-verified every final against field-owner or structured feeds and checked every causal claim against the real process record. Full record: Part 5 §"2026-09-24(f)".
- **P-509 (NBL, Perth v Adelaide) was live throughout and is not settled**, per the operator's instruction. It stays in the active mini log `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-509 onward - 2026-09-24/`.

**Finals and grades.** All 17 finals are right. **One grade pair was wrong**: P-496 Vasa +0.5 is now a WIN and Marek −0.5 a LOSS, because the ITF draw sheet gives 15–15 games.

**The peer's process record was largely invented.** Linescores, decisions, goal types, goalies, quarter lines, coaches and game IDs were written rather than read. For example, TMP-G25 went 12 innings, not 9, and P-503 had no empty-net goal. The six single-game rules built on those narratives are **withdrawn or demoted**:
- doubleheader-G1 deflation: 2026 G1 P(total ≤ 7) is 0.435 (n=23) against 0.427 for other games;
- derby Under suppression: P-508's margin came from 4/41 three-point shooting;
- "dual run-line arbitrage": a mechanical cover, since both opposite +1.5 rows win in any one-run game (27.6%);
- FIBA qualifier pace;
- the clay handicap cap;
- NHL pre-season asymmetry.

**The biggest real defect is at issue time.** In 5 of the 7 cards that could be checked, the printed "reported/confirmed" lineups were wrong. P-501's Rank-1 Over was built on a Baltimore lineup of which only 2 of the 9 named players started. Two losing MLB Overs also printed the wind as blowing out when the official record says it was blowing in.

**Controls added.** All are integrity, measurement or retrieval controls; none is a forecasting coefficient: `C-PROCESS-RECORD-PROVENANCE`, `C-LINEUP-DIFF` with S-1 Rev 2 receipt enforcement, `G-L22(c) COVERING_PAIR`, `C-SUMMARY-FROM-CARD`, `C-PROMOTION-RECEIPT`, and MLB gamefeed weather at freeze.

**Where to look.** The descriptive batch record, the verified source lanes and the base rates are in Part 5 §(f) part M, `DATA_SOURCE_REGISTER.md` §"2026-09-24(f)" and `BASE_RATES_REGISTER.md` §5. Everything remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.


<!-- AUDIT-CLOSURE-2026-09-25 -->
## Audit closure and archive — 25 September 2026

**Every audit's implementable recommendations are now in the governing files, and the audit documents are archived.** The 15 audit documents (2026-09-05 to 2026-09-23) moved to [`archive/audit_documents_implemented_2026-09-25/`](archive/audit_documents_implemented_2026-09-25/). Their index and item-by-item receipt is [`AUDIT_CLOSURE_LEDGER_2026-09-25.md`](archive/audit_documents_implemented_2026-09-25/AUDIT_CLOSURE_LEDGER_2026-09-25.md).

**What was still missing** came mainly from three sources:
- the 2026-09-22 cohort audit, whose mapping had never been written in;
- the 2026-09-23 read-only audit, items 4–10;
- the propagation of the 2026-09-24(f) controls.

**Key changes:**
- cricket phase totals by innings order;
- the tennis benchmark as a blocking precondition, and matchup holds from serve × return;
- the METHOD probability-wording contradiction resolved;
- `COVERING_PAIR` and settlement-integrity labels;
- the recurring-mistake registry (M1–M30) now in-repo;
- the audit script repaired (it had silently truncated issue-time cards) and extended;
- a preflight `participants` object.

**Still open** (empirical, not documentable): the H0 dataset, chronological fits, prospective shadow, ~~non-MLB `R-1` magnitudes~~ (derived for five competitions in the 2026-09-25(b) research pass, below) and every TESTING manifest. These are tracked in `NUMERICAL_PROGRAM.md`, `H0_DATASET_CARD.md` and `LEARNING_REGISTER.md`.

**Custody:**
- P-509 settled (Part 5 §"2026-09-24(g)").
- P-484–P-486, P-488 and P-492 imported verbatim (Part 5 §"2026-09-25(a)").
- Active mini log: `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-510 onward - 2026-09-25/PREDICTION_MINI_RUNNING_LOG_P510_ONWARD.md`.
- Next ID: **P-510**.
- Control receipt: [`CONTROL_MANIFEST_2026-09-25.md`](CONTROL_MANIFEST_2026-09-25.md), superseded the same day by `CONTROL_MANIFEST_2026-09-25-2.md` (below).
- Everything remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.

<!-- RESEARCH-2026-09-25 -->
## Research pass — 25 September 2026(b)

**Question asked:** what else can be implemented to improve future results? **Answer, in short:** the recurring losses of the last cohorts were mostly *retrieval* failures (lineups, weather, invented process records) and *uncalibrated widths*, not missing model sophistication. This pass therefore did two kinds of work.

**1. Derived the base rates the framework had marked `NOT_YET_DERIVED`,** from population data rather than the log's own cards.
- **Recency (`R-1`) in five more competitions** (NBA, WNBA, NBL, NHL, EPL) — [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md) §7. There is no rebound anywhere. The previous game is the worst predictor in 6 of 6 competitions, 18–40% worse than the league average. In basketball, the opponent's defence to date is worth more than any recency window.
- **Reference rates** — [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md) §7:
  - league totals, margin bands, quarter shapes and width benchmarks;
  - NBL early season **−8.5** and WNBA early season **+6.5** points (three seasons each, opposite signs);
  - the WNBA 2026 regime shift of **+10.7** points;
  - the NHL empty-net structure (73% of two-goal wins) and preseason rates;
  - EPL first-half goals and corners;
  - WTA/ATP total-games and games-handicap conditionals, which close the recorded WTA gap;
  - all 30 MLB parks and first-five-innings rates.
- **Width check** of the 2026-09-24 cohort: basketball total widths ran about 39% too narrow (mean z² 1.93, n = 7).

**2. Built and wired the controls that act on it.**
- [`receipts.py`](receipts.py) prints freeze and settlement receipts with endpoints: MLB lineups, weather and probables; NHL goalies and empty-net goals; ESPN starters and DNPs; the regulation score; and the `C-LINEUP-DIFF` lines. It replays the settled P-500, P-503, P-504 and P-506 facts exactly. Tests: [`test_receipts.py`](test_receipts.py), 17.
- The controls themselves are in [`RULES_GENERAL.md`](RULES_GENERAL.md) §"2026-09-25(b)":
  - `C-WIDTH-BENCHMARK` (disclosure);
  - `C-WIDTH-Z` (measurement; prospective manifest in `LEARNING_REGISTER.md`);
  - `C-RECEIPT-TOOL`;
  - early-season and regime references;
  - the `R-1` one-game corollary;
  - tennis `C-HCP-COHERENCE`.
- The sport files each have a §"2026-09-25(b)"; the research guide and logging workflow have new checklist steps.
- `audit_card_controls.py` gained fields `WB`, `HC` and `10z`, and a settlement-key fix. Tests: 70 in total.
- Registry item **M31** was added: width chosen without a reference.

**None of this moves a probability, centre, width or rank by itself.** Everything is disclosure, measurement or retrieval, and no coefficient was fitted from the log (`L-087`).
- Queries, scripts and results: [`research/base_rates_2026-09-25/`](research/base_rates_2026-09-25/README.md).
- Custody: the stray root `PREDICTION_MINI_RUNNING_LOG_P474_ONWARD.md` was checked and moved intact into its archive folder.
- Control receipt: [`CONTROL_MANIFEST_2026-09-25-2.md`](CONTROL_MANIFEST_2026-09-25-2.md).
