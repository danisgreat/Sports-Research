## 2026-09-17(c) — current audit corrections

This correction supersedes earlier aggregate and period-bound claims without changing issued probabilities, ranks or contracts. All existing records remain LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. See [the implementation ledger](AUDIT_IMPLEMENTATION_2026-09-17.md) and [scoring specification](SCORING_AND_VALIDATION.md).

**Score arithmetic:** P-344's four Brier cells sum to 1.1337, mean **0.283425**, not 0.3334. Recomputed from canonical rows and latest documented settlements: P-333–P-344 **39 rows, 0.2601307692**; through P-344 **72 rows, 0.2408763889**; through P-371 **177 rows, 0.2423966102**; through P-423 **373 rows, 0.2341018767**; through P-437 **425 rows, 0.2286134118**; through P-451 **477 rows, 273 W/204 L, 0.2265475891**. These are current cumulative-by-ID reconstructions, not claims about what was settled at each historical snapshot date. PRIMARY_SCORED remains **136 rows/33 cards, 71 W/65 L, 0.246825**. Older approximate aggregates are superseded by this row-derived correction. Legacy binary scores retain their original conditioning defect and are labelled LEGACY_MIXED_DIAGNOSTIC; corrected W/P/L and non-push measures are separate.

**Period correction:** P-255-C05 and P-256-C05 are **UNRESOLVED_PERIOD**, not demonstrated research wins. Whole-match corners of 24 and 15 do not establish regulation Over 8.5: losing splits require 16+ and 7+ extra-period corners respectively, and no recovered evidence excludes them. Reopen the existing TMP-AUDIT-20260912-03 and -04 handles. They remain separate documentary/period follow-ups, bringing that queue back to **5**; the primary queue stays **23**. Final scores and other rows remain as recorded. Original Part-1 custody is preserved; Appendix A in Part 4 carries the evidence receipt and correction pointer. No new ID or probability is created.

**Validation correction:** C-OU-GEOMETRY's P-424–P-437 and P-438–P-451 cohorts are historical development observations, with **zero verified prospective cards** until manifest/issue/outcome-time/control-version joins are established. In particular P-425/P-426/P-427/P-429 predate the 16 September manifest. Import time is not issue time. No universal MLB run-line/push ceiling, NFL variance floor, automatic phase preference or Over/Under bias is promoted. Current METHOD v4.1 governs new forecasts only.

# Combined prediction log 3

> **2026-09-12 controlling correction:** All current combined-log material is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under the current user request. Settlement preserves outcome evidence; it does not authorize a performance claim. The [2026-09-12 audit](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-12.md) and [probability/research corrections](audit_2026-09-12/rule_corrections.md) supersede conflicting older operational statements. Original issued records remain unchanged.


> Historical policy block; superseded for current log use by the 2026-09-12 LEARNING_ONLY directive.

<!-- USER FREEZE CONFIRMATION 2026-09-05 -->
**User-confirmed pre-game eligibility:** the existing non-live cards were strictly frozen before play. They are now eligible for historical directional/ranking evaluation under their issued methods, including process failures. The September 5 ten-card v3.4 cohort remains **#1 4/10, #2 4/10, both top two 0/10, preferred O/U 3/10 events (4/12 distinct total/phase targets)**. These results now count in that historical record. Five games found live at first settlement check are pre-game forecasts awaiting settlement, not live-issued cards. Explicit live-issued historical views remain separate. [Policy](PERFORMANCE_ELIGIBILITY_POLICY.md) · [Every ID's eligibility](PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md).

The earlier blanket non-performance-eligible/late-import classification is superseded by the user's confirmation. Original source text and old audit statements are retained as history. This correction does not recreate independent timestamp evidence, change any original rank/result, or count already-observed games as tests of a later rule change.
<!-- END USER FREEZE CONFIRMATION 2026-09-05 -->

> Historical policy block; superseded for current log use by the 2026-09-12 LEARNING_ONLY directive.

<!-- USER DIRECTIVE 2026-09-06 — SETTLEMENT-ONLY PERFORMANCE ELIGIBILITY -->
**2026-09-06 controlling correction — settlement is the sole performance-eligibility gate.** The user directed that any log that has been settled counts for performance eligibility (`PERFORMANCE_ELIGIBILITY_POLICY.md` `EP-2026.09.06-v2`; `LEARNING_REGISTER.md` L-078). This note carries forward from `PREDICTION_LOG_COMBINED.md` and `PREDICTION_LOG_COMBINED_2.md` and supersedes every `E1-Q-LATE_IMPORT`, "not performance-eligible", "not prospective performance evidence" and "clean prospective unit" exclusion-of-eligibility statement anywhere in the closed archives, for every settled row across `P-001`–`P-332`. Two things it does **not** change: (1) the underlying **provenance facts** recorded in those files (first-demonstrable times, hashes, missing-timestamp cards) remain accurate historical records; only the *eligibility conclusion* is superseded; (2) the separate numerical model pipeline (`NUMERICAL_PROGRAM.md`, Stage S0) is unaffected.
<!-- END USER DIRECTIVE 2026-09-06 -->

Status: **CLOSED 2026-09-15 at `P-423` — read/settle only. The active canonical log is now [`PREDICTION_LOG_COMBINED_4.md`](PREDICTION_LOG_COMBINED_4.md) (`P-424` onward).** Open rows issued in this file stay in this file's custody and are settled here when their retry triggers are met; `GAME_LOG_STATUS_CURRENT.md` tracks them. *(Previous status: ACTIVE CANONICAL LOG — ALL NEW FORECASTS APPEND HERE.)*
Opened: **2026-09-07**, as the third combined log per user directive. `PREDICTION_LOG_COMBINED.md` is the closed historical archive for `P-001`–`P-271` (closed 2026-09-04). `PREDICTION_LOG_COMBINED_2.md` is the closed archive for `P-272`–`P-332` (closed 2026-09-07), and also holds the lettered **Appendix — unsettled and incomplete logs**. **This file carries `P-333` onward.**
Current method: **MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND; `UNVALIDATED_SUBJECTIVE` probability + Brier scoring mandatory on every new card (`METHOD.md` §5); historical issued methods preserved; no retrospectively generated probabilities**
Component order: opened empty at `P-333`; new forecasts append below.

## Current controlling snapshot

This is the only queue and next-ID authority for new forecasts. The snapshots in `PREDICTION_LOG_COMBINED.md` and `PREDICTION_LOG_COMBINED_2.md` are frozen at their closures and no longer accept new IDs.

| Field | Current value |
|---|---|
| As of | **2026-09-12 Australia/Sydney; checks from 2026-09-11 14:31 UTC.** P-345-P-371 already imported; no duplicate cards. Twenty mini logs now byte-preserved in `archive/mini_logs/`. Recent and historical evidence, corrected diagnostics and additional recovered P-249-P-267 material are in the [current audit](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-12.md). |
| Next canonical ID | **Closed.** This file ended at `P-423`; new IDs start at **`P-424` in `PREDICTION_LOG_COMBINED_4.md`**, whose snapshot is now the sole queue/next-ID authority. (2026-09-15(b): `P-373`–`P-423` imported as issued; `P-372` RESERVED / UNUSED.) |
| Open / live / pending settlement queue | **2026-09-15(b): NO LIVE EVENT. 23 open handles** — the 13 below plus `TMP-OPEN-20260912-01` (P-377-C02), `TMP-OPEN-20260914-01`/`-02`/`-03`/`-06` (P-399-C02, P-401-C01/C03, P-406 six-over rows) and `TMP-OPEN-20260915-01`…`-05` (P-407-C01, P-409-C02, P-410-C05, **P-418 whole card — identity conflict**, P-419-C05). Retired: `TMP-OPEN-20260914-04`/`-05` (P-402 corners WIN at the Premier League record) and `TMP-SETTLED-20260911-01` (merged into canonical P-374). Table: `GAME_LOG_STATUS_CURRENT.md`. *(Earlier text follows.)* **2026-09-15: NO LIVE EVENT. `P-364` FINAL — England won by 8 wickets (Day 4, 12 Sep); winner label WIN; `TMP-OPEN-20260911-03` retired. Open rows now 13** (four Part-3 corner rows + nine inherited Part-2 rows, below). No new mini log was supplied or found (see §"2026-09-15"). *(Historical 2026-09-12 text follows.)* **One live event:** `P-364` (England v Pakistan 3rd Test — Day 3 at this pass). Its four ranked rows are settled; only the potential-winner label is open (`TMP-OPEN-20260911-03`). **Two new provisional derivative rows:** `P-368-C02` (`TMP-OPEN-20260911-01`, Over 7.5 corners, provisional WIN at 9) and `P-369-C01` (`TMP-OPEN-20260911-02`, Under 10.5 corners, provisional LOSS at 11) — no provider was frozen, so no W/L/Brier is booked. **Carried:** `P-341-C03` (`TMP-OPEN-20260909-01`, unsettleable to standard; ESPN `uga.1` still stale on the 2026-09-11 re-probe) and `P-342-C03` (`TMP-OPEN-20260909-02`, provisional WIN). **Nine inherited Part-2 appendix rows** (`TMP-OPEN-20260909-03`…`-11`; custody Part 2). **Collision record:** `TMP-SETTLED-20260911-01` (unsupplied Fenerbahçe–Roma no-forecast record; final 1–1; non-scorable). **Retired this pass:** `TMP-OPEN-20260910-01`…`-03` (`P-345-C03`, `P-346-C05`, `P-355-C05` — all WIN at their frozen field owners). `P-366-C02/C03` closed as terminal censored. **Total genuinely open rows across all three parts: 14.** |
| Predecessor logs | Part 1 `PREDICTION_LOG_COMBINED.md` — `P-001`–`P-271`, closed 2026-09-04. Part 2 `PREDICTION_LOG_COMBINED_2.md` — `P-272`–`P-332`, closed 2026-09-07 (see its `## 2026-09-07(a)` and `## 2026-09-07(b)` closing sections and its lettered appendix). Raw external mini logs are byte-preserved in `archive/mini_logs/`. |
| Probability state | Every card from `P-333` onward carries `UNVALIDATED_SUBJECTIVE` probabilities on every ranked row (`METHOD.md` §5), scored by Brier score against a trivial `p = 0.5` baseline, accumulated per `PRIMARY_SCORED` population in the running scorecard below. This is analyst judgment, **never** a calibrated or validated model probability. Every card issued before `P-333` keeps its state as recorded in Parts 1–2; no probability is ever minted retroactively. |
| Value state | `NO VALUE DETERMINABLE` unless a future validated model and complete same-time price/terms snapshot pass the value gate. |
| Performance eligibility | **`EP-2026.09.06-v2`** (`PERFORMANCE_ELIGIBILITY_POLICY.md`, `METHOD.md` §7.3): any settled row counts, regardless of pre-game/live-issued horizon or import timing. Descriptive scorecard only — never calibration, ROI, edge or model validation. **User directive (2026-09-09, restated 2026-09-11 — current; overrides for these cohorts):** `P-333`–`P-344` **and `P-345`–`P-371`** are folded into the running scorecard for continuity but are **learning-only, not performance-eligible evidence** — no accuracy/quality verdict is drawn from them. This does not change the standing policy for other cards. |
| v4.0 Brier / calibration scorecard — running total | **After `P-373`–`P-423` (2026-09-15(b)):** mixed **371 rows, 205 W / 166 L, mean Brier 0.2352** (prior 177 rows + 194 new: log A 66 rows 0.2449, log B 67 rows 0.2278, log C 61 rows 0.2088). `PRIMARY_SCORED` **104 rows, 55 W / 49 L, mean 0.2522 — slightly worse than the 0.2500 baseline**: MLB 68 rows 35–33 **0.2473**; EPL 20 rows 12–8 **0.2267**; NRL/AFL 16 rows 8–8 **0.3053**. **`PRIMARY_SCORED` card count: 25 — the first pattern/calibration review was completed in §"2026-09-15(b)".** Learning-only; sample too small for any calibration or superiority claim. *(Earlier state follows.)* **After `P-345`–`P-371` (2026-09-11):** mixed all-scored-rows total **177 rows, 98 W / 79 L, mean Brier 0.2435** vs 0.2500 baseline (prior 72 rows 0.2436 + this import's 105 graded rows 0.2434). `PRIMARY_SCORED`: **34 rows, 18 W / 16 L, mean Brier 0.2373** — EPL 10 rows 5-5 **0.2666**; MLB 24 rows 13-11 **0.2252** (`P-331`, `P-335`, `P-347`, `P-348`, `P-349`, `P-351`); NRL/AFL 0 rows. **`PRIMARY_SCORED` card count: 8** (of 25 needed for the first pattern/calibration review). This import: `P-345`–`P-357` 55 rows **0.2264**; `P-358`–`P-371` 50 rows **0.2621 — worse than the 0.5 baseline**, recorded honestly. Rows stated at `p ≥ 0.70` won 13 of 21 (62%) against a mean stated 74% — mild over-confidence, opened as the prospective test `C-PROB-EXTREMITY`. Sample far too small for any calibration, discrimination or superiority claim — this line says so every time it is read. **Learning-only per user direction.** Every `P-372`+ card adds to these totals in the same edit that appends it. |
| Retained historical field — prior "60 clean units" checkpoint | Unchanged text kept for provenance: 60 new clean, demonstrably pre-result event units; count events, not files. Superseded as a performance-eligibility test by `EP-2026.09.06-v2`; may still be referenced as an internal development milestone. |

## How this file is used — read this before appending anything

1. **Read `METHOD.md` fresh, every session, before touching this file.** It is the single primary statement of the process, the ~12-item mandatory checklist, and the probability/scoring requirement. Read `RULES_GENERAL.md` §16 for the current gate classification and the relevant `RULES_<SPORT>.md` (`SFA-<SPORT>`) for the sport in question; consult `CONTROLS.md`, `SOURCES.md`, and the `PROMOTED` entries in `LEARNING_REGISTER.md`. **Never rely on a remembered method version or a cached copy of these files** — the P-268/P-270/P-271 version-currency finding at the top of `PREDICTION_LOG_COMBINED.md`, and the P-306–P-317 ledger-integrity failure recorded in `PREDICTION_LOG_COMBINED_2.md` §"2026-09-06(e)", are the direct evidenced reasons. An external generating session must be supplied the **current** `METHOD.md`, `RULES_GENERAL.md` §16 and the relevant sport file at the start of its work, not a saved copy from an earlier date.
2. **Check this file's own top snapshot first**, every time, before issuing a new forecast — settle every FINAL event in the queue using the complete settlement protocol (`METHOD.md` §7, `UPCOMING_GAME_RESEARCH_GUIDE.md` §16) before proceeding to a new pick, even if the request only asks for a new pick. The queue currently holds no live event and **23 open handles** (2026-09-15(b); table in `GAME_LOG_STATUS_CURRENT.md`). *(Superseded 2026-09-15 wording:)* no live event (`P-364` settled 2026-09-15) and four soccer corner rows (`P-341-C03`, `P-342-C03`, `P-368-C02`, `P-369-C01`) awaiting a field-owning provider — retry them, but none blocks a new forecast.
3. **Append in strict ascending canonical-ID order** starting at `P-333`. Reconcile the "Next canonical ID" field before assigning a new one; never renumber or reuse an ID. If a batch is supplied out of order or with gaps, resolve the gap explicitly before appending — never silently create a second, parallel numbering.
4. **Update the snapshot table above in the same edit** that appends new forecasts or settlements — including the running Brier scorecard. A stale snapshot pointing at an old "Next canonical ID" while newer content already exists further down the file is exactly the defect that closed Part 1's active status; do not reproduce it here.
5. **Batches from an external generating session:** first fingerprint the mini-log (source filename, byte size, SHA-256, first-demonstrable time), then run the full settlement protocol on every event in it that has already finished, then fold in a dated settlement/retrospective section (settlement tables, full contract-row grades, the three-question retrospective per `METHOD.md` §7.2, and the Brier update), then move the raw component file into `prediction logs/` and update the snapshot. **`METHOD.md` §10 ledger-integrity rule:** an external running log not reconciled into this canonical file within 24 hours of being made available blocks issuing the next new forecast until it is.
6. **The inherited unsettled / incomplete follow-ups are Part 2's, not this file's.** Do not copy them here, do not re-open them here, do not attempt to settle them from this file. They are quarantined in `PREDICTION_LOG_COMBINED_2.md`'s lettered appendix with their existing learnings and their maximum-attempt disposition.
7. This log remains **`SPORTS_ONLY / MARKET_BLIND`** and an audit trail rather than a calibrated betting record. Every settled row is performance-eligible (`EP-2026.09.06-v2`) — but that means "counts in the descriptive historical scorecard," not "proves predictive lift." No entry here may claim calibration, ROI, edge, or statistical validation of a model. The `UNVALIDATED_SUBJECTIVE` Brier scorecard measures internal forecast quality only and is never a market-edge claim.

## Sources of learning carried forward from the predecessor logs

The full promoted-control history lives in `LEARNING_REGISTER.md` (`L-001`–`L-121` at time of opening) and `CONTROLS.md`, and applies to every card in this file without being restated here. Load-bearing for cards issued from here on:

- **`METHOD.md` §5** — every ranked row carries an `UNVALIDATED_SUBJECTIVE` probability; the rank is *derived from* the set of numbers on the card, and both are scored.
- **`METHOD.md` §2** — MLB, EPL and NRL/AFL/AFLW are `PRIMARY_SCORED`; everything else is `EXPLORATORY — NOT SCORED` until separately promoted.
- **`RULES_GENERAL.md` §16.5** — explicit arithmetic (stated prior + signed weighted adjustments + centre/width) replaces prose shrinkage. **§16.5(a) (`G-L1`, 2026-09-09):** additionally enumerate the outcome-state families (score / margin / set-count) with an explicit probability mass on each; every current-evidence `G22` kill path is a weighted branch, not a prose sentence; write one representative Rank-#1 outcome in the settlement unit of every other supplied row. **§16.5(b) (`G-L2`, 2026-09-09):** unit-performance uncertainty is distribution width around the shrunk skill prior, not a signed total lean, unless a named *directional* mechanism exists.
- **`METHOD.md` §7.2** — the three-question retrospective (driver / knowability / smallest routine change) plus a pattern review every 25 settled cards in a `PRIMARY_SCORED` population.
- **`L-087`** predictive-weighting firewall — one session's cohort finding may motivate a mandatory disclosure, never an ordinal rule or a fitted weight; this applies to the framework's own newly drafted controls with the same force as any external lesson.
- **`L-079`/`G10.1`/`G10.2`/`L-081`** — structured field-owning endpoints are queried before narrative pages; synthetic/simulated/AI-generated content never settles a contract; derivative markets are gated by whether the competition has a reachable settlement-source.
- **`G14.2`/`L-082`** — bench/coaching/rotation record; `BENCH_NOT_RETRIEVED` blocks a margin or full-game total row from Rank #1. Named high-impact bench players belong in the second-half scoring component.
- **`G17`/`G17.1`** — a streak in *either* direction carries zero directional weight without a named, currently active mechanism.
- **`G36.1`/`L-119`** — `RESEARCH_GRADE` and `OPERATOR_ACTION` (`UNKNOWN_DEFINITION` where no operator terms exist) are separate fields; neither masks the other.

### Candidate watch items (not promoted rules)

From the `P-318`–`P-332` and `P-333`–`P-344` retrospective sets. Each needs 3+ recurrences in a 25-card `PRIMARY_SCORED` window before it can become a `CANDIDATE` control. **None is a rule, weight or ordinal bar.**

- current route-to-corner / route-to-shot-on-target evidence when a major central attacker is absent (`P-318`);
- explicit second-half / secondary bench-attacker scoring contribution — now cross-sport (`P-329` soccer; `P-344` basketball secondary-scorer usage transfer);
- distance-to-line recorded in every derivative retrospective evaluation (`P-319`, `P-325`, `P-328`, `P-337`);
- a "disrupted-match" flag (red card / GK dismissal / long weather delay / in-game injury) for later population-baseline learning (`P-321`, `P-234`, `P-309`; `P-344` Hayashi);
- **competition-tier / promotion translation as a distinct uncertainty (`G-L3`, `P-341`, `P-342`)** — do not pool the weaker side's lower-tier rates into the total centre; a rotated cup favourite produces territory + late conversion, not early goals.
- **baseball run-centre bias (`C-RUN-CENTRE-BIAS`, 2026-09-11):** across 12 cards `P-335`–`P-365` the stated centre exceeded the realised total in 9, mean signed error −1.58 runs — prospective manifest in `LEARNING_REGISTER.md`;
- **probability extremity (`C-PROB-EXTREMITY`, 2026-09-11):** rows stated at `p ≥ 0.70` won 13 of 21 in `P-345`–`P-371` (mean stated 74%);
- **basketball underdog separation / close-game ↔ total coupling (`C-UNDERDOG-SEPARATION`, 2026-09-11):** `P-358`, `P-359`, `P-371`, with the separation mirror `P-360`, `P-367`.

- **margin tails (`C-MARGIN-TAIL-MASS`, 2026-09-15(b); supersedes `C-UNDERDOG-SEPARATION`):** Rank-#1 underdog cushions `P-345`–`P-423` went 10 W / 13 L at a mean stated 0.61, and log-C margin centres missed toward the favourite on 8 of 10 cards — the disclosure requirement **`G-L12`** (`RULES_GENERAL.md` §16.10) now forbids shrinking a margin centre toward pick'em without a named mechanism.

**Promoted this pass to disclosure requirements (not ordinal bars — `L-087`):** `G-L1` (family enumeration with mass, `RULES_GENERAL.md` §16.5(a)) and `G-L2` (unit uncertainty is width, §16.5(b)).

**Promoted 2026-09-11 (disclosure/process requirements, not ordinal bars — `L-087`):** `G-L9` complement decomposition, `G-L10` joint top-two probability, `G-L11` sampling-noise check (`RULES_GENERAL.md` §16.5(e)–(g)); the `G-L8` median clarification for skewed totals; the §16.8 card completeness block; sport controls in the sport files' §"2026-09-11" sections.

---

## Three-log restructuring — 2026-09-07

Per user directive: this repository now maintains **three** combined logs.

| Log | Role | ID range | Status |
|---|---|---|---|
| `PREDICTION_LOG_COMBINED.md` | Historical archive | `P-001`–`P-271` | **CLOSED 2026-09-04** — read/settle only |
| `PREDICTION_LOG_COMBINED_2.md` | Historical archive + unsettled-log appendix | `P-272`–`P-332` | **CLOSED 2026-09-07** — read/settle only; holds the lettered "Appendix — unsettled and incomplete logs" |
| `PREDICTION_LOG_COMBINED_3.md` (this file) | **Active canonical log** | `P-333` onward | **ACTIVE** — all new forecasts append here, strictly in canonical-ID order |

`RULES_GENERAL.md` §0's file-agnostic rule governs the split: *"README identifies the active prediction log; only that file's top Current controlling snapshot controls queue status and next ID."* `README.md` and `METHOD.md` §10 name `PREDICTION_LOG_COMBINED_3.md` as that active file. Parts 1 and 2 remain fully authoritative evidence for mechanism retrieval and for settling anything that references a `P-001`–`P-332` ID; their own top snapshots no longer accept new appends.

**Why `P-318`–`P-332` are in Part 2, not here:** per user directive, that settled cohort was appended to Part 2 (Part 2 §"2026-09-07(b)"), Part 2 was then closed at `P-332`, and this file continues from `P-333`. The `P-318`–`P-332` raw forecast text is byte-preserved in `archive/mini_logs/PREDICTION_MINI_RUNNING_LOG_P332.md`.

---

# Mandatory pre-query cycle

Before **every** new sports forecast/request:

1. Fresh-read `METHOD.md`, `RULES_GENERAL.md` §16, the relevant `RULES_<SPORT>.md`, `CONTROLS.md` and this file's top snapshot. Record the exact active method version from `METHOD.md`'s own header — never from memory.
2. Read the top queue above (2026-09-15(b): no live event; 23 open handles incl. `P-418` identity conflict and nine new corner/phase rows — `GAME_LOG_STATUS_CURRENT.md`; earlier list: `P-341-C03`, `P-342-C03`, `P-368-C02`, `P-369-C01` — derivative corner rows awaiting a field-owning provider).
3. State-check every `P-333`+ open/live/pending event in canonical-ID order.
4. If an event is **FINAL and verified**, settle every contract under its frozen terms, settle the potential winner, record the Brier score for every `UNVALIDATED_SUBJECTIVE` row, and perform the three-question retrospective (`METHOD.md` §7.2) before issuing the new forecast.
5. If **Rank #1 lost**, or more than one top-ranked row lost, complete the deep retrospective: what went right; what went wrong; actual mechanism; concrete improvement; process grade (background field).
6. If an event remains **LIVE / postponed / suspended / unverified**, leave it in the top queue and continue.
7. Only after the queue pass, research and issue the new event, with `UNVALIDATED_SUBJECTIVE` probabilities on every ranked row and explicit centre/width arithmetic.
8. Append the new forecast before delivery, update the "Next canonical ID", update the running Brier scorecard, and provide the refreshed Markdown running log to the user.
9. **Pattern review** every 25 settled cards in a `PRIMARY_SCORED` population: review the accumulated "smallest change" answers as a set; a pattern recurring 3+ times in 25 cards is a `CANDIDATE` for `CONTROLS.md`/`LEARNING_REGISTER.md`. Review the Brier/calibration scorecard on the same cadence.
10. **Do not touch the Part 2 unsettled-log appendix from this file.**

---

# Carried-forward high-priority controls

| Control | Running-log implementation |
|---|---|
| Method-version currency | Every card records the method version from a fresh in-session read of `METHOD.md`; a stale declaration is a `BLOCKING`-gate failure. |
| Probability mandate (`METHOD.md` §5) | Every ranked row carries an `UNVALIDATED_SUBJECTIVE` probability; complementary rows sum sensibly; nested lines are monotone; the rank is derived from the numbers. Never described as calibrated. |
| Population scoping (`METHOD.md` §2) | MLB / EPL / NRL / AFL / AFLW cards are `PRIMARY_SCORED`; all else `EXPLORATORY — NOT SCORED`. The scorecard tracks them separately. |
| Explicit arithmetic (`RULES_GENERAL.md` §16.5) | Every centre/width is a stated prior + signed weighted adjustments + resulting centre and width, with each supplied line located against that width. No "requires shrinkage" prose. |
| Structured-endpoint-first / synthetic exclusion (`G10.1`/`G10.2`/`L-079`/`L-081`) | Query the field-owning structured endpoint before a narrative page; a search-result summary is not a source; synthetic/AI content never settles a contract; derivative markets are gated by competition coverage. |
| Bench / coaching / rotation (`G14.2`/`L-082`) | Recorded on every card; `BENCH_NOT_RETRIEVED` blocks a margin or full-game total from Rank #1. |
| Streak persistence vs reversion (`G17`/`G17.1`) | A streak in either direction carries zero directional weight without a named currently-active mechanism and a longer-run baseline comparison. |
| Environment / current-surface gate | Every outdoor event needs a venue-coordinate hourly forecast, not a city forecast; the gate fails closed if it cannot be met. |
| Phase / total separation | First-half, full-match, powerplay and full-innings targets are assessed as independent objects. |
| Goals ≠ possession ≠ corners | Corner rows get their own exposure/route analysis; goal volume and possession are not proxies. |
| Winner / margin / total allocation | Each is assessed separately; a correct winner or cushion can coexist with a badly-missed score corridor. |
| Standard-rules settlement split (`G36.1`/`L-119`) | `RESEARCH_GRADE` and `OPERATOR_ACTION` are separate fields; `UNKNOWN_DEFINITION` where no operator ticket exists. |
| Start-crossed / no-forecast discipline | A stale pregame freeze may not be delivered after scheduled start; a live view needs exact verified state; otherwise `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`. |
| Predictive-weighting firewall (`L-087`) | A single cohort finding motivates a disclosure, never an ordinal rule or a fitted weight — including the framework's own new work. |

---

# Settlement / retrospective schema

`METHOD.md` §7.2's three-question schema (driver / knowability / smallest routine change) is the primary retrospective output. The compliance grade (`ISSUE_TIME_PROCESS_GRADE`) is retained as a background field. When a `P-333`+ event becomes final, use this block before moving it out of the top queue.

## P-XXX — Settlement

**Event:** · **Official final:** · **Field-owning source:** · **Settlement time:** · **Method declared on issued card:**

| Rank | Contract | Frozen terms | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier | Boundary / dependence note |
|---:|---|---|---:|---|---:|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |

**Potential winner:** · **Potential-winner result:** · **Card mean Brier vs 0.5 baseline:**

### Three-question retrospective (`METHOD.md` §7.2)
1. **What did the score actually turn on?** (the specific driver — not "process compliant")
2. **Was that driver knowable before issue, and was it in the card?** (yes/no + the specific evidence line, or the specific missing-evidence reason)
3. **What is the smallest change to the research routine that would have surfaced it?** (one sentence; escalate to a `CANDIDATE` only on recurrence)

### Deep Rank-1 retrospective — complete whenever Rank #1 loses

| Question | Finding |
|---|---|
| What went right? | |
| What went wrong? | |
| Actual mechanism | |
| Improvement | |
| Grade (background) | |

---

# Chronological settled / issued events

## 2026-09-09 — `P-333`–`P-344` imported and settled

**Settlement authority:** `MDS-2026.09.06-v4.0`. **Frozen-evidence rule:** every issued rank, probability, candidate, target, issue horizon and pre-game evidence block is immutable; only the settlement, the Brier grades and the retrospectives are added. Full raw card text is byte-preserved in [`archive/mini_logs/PREDICTION_MINI_RUNNING_LOG_P344.md`](archive/mini_logs/PREDICTION_MINI_RUNNING_LOG_P344.md). The external running log had already produced its own 2026-09-09 settlement pass; this section re-verifies every final against an independent public source, corrects one arithmetic error (`P-344` card mean Brier), folds the cohort into the running scorecard, and completes the deep retrospectives and cross-sport learning the user requested.

### Component fingerprint

| Field | Value |
|---|---|
| Supplied source | `PREDICTION_MINI_RUNNING_LOG_P344_RETROSPECTIVE_UPDATED.md` — external local running log, `P-333`–`P-344` plus governance carry-forward; local next slot `P-345` |
| Stored as | `archive/mini_logs/PREDICTION_MINI_RUNNING_LOG_P344.md` |
| Self-reported source fingerprint (from the log's §11) | predecessor `PREDICTION_MINI_RUNNING_LOG_P344_UPDATED - Copy.md`, 151,143 bytes, 2,394 lines, SHA-256 `72ae84b77c7588b2d495b8b55a9314fd044688f057d37dd47a9bfbe22f946307` |
| Canonical mapping | `P-333`–`P-344` → `P-333`–`P-344`; Part 3's next ID at import was `P-333`; no collision; **no `TMP-SETTLED-*` identifier needed** for the main cohort |
| Issuance-horizon notes | `P-333`, `P-343` (cricket) and `P-334` (FIBA) are `START-CROSSED / LIVE STATE NOT VERIFIED` — **no forecast issued**, no ranked rows, no probabilities, no winner. Correct fail-closed behaviour (`RULES_GENERAL.md` start-crossing invariant; cricket `CR-P3` innings-order gate). They contribute zero scored rows. The other nine cards were issued `PREGAME` with cutoff before scheduled start. |
| Independent-verification pass | Every final below cross-checked 2026-09-09 against a public source outside the mini-log's own register (ESPN, SI, WTA, FIBA/TSN, SBS English, Sportnet, Kawowo/GHANAsoccernet, ESPNcricinfo, matchcalendar.football). All nine issued-card finals and all three admin-closure finals confirmed. |

### Settlement table

| ID | Event / competition | Official final (independently re-verified) | Rank #1 | Potential winner | Population / note |
|---|---|---|---|---|---|
| `P-333` | Pakistan Women vs Hong Kong Women — Women's T20 Asia Cup, Group A | **Pakistan 143/8 beat Hong Kong 71 by 72 runs** (Nashra Sandhu 6/7). Pakistan batted first. | — | — | **ADMIN CLOSED / NO FORECAST** — start crossed, toss/innings order unverified at cutoff. Non-scorable. |
| `P-334` | Germany Women vs Mali Women — FIBA Women's Basketball World Cup, Group A | **Germany 83–58 Mali** (Frieda Bühner 21). | — | — | **ADMIN CLOSED / NO FORECAST** — live-state gate failed after tip. Non-scorable. |
| `P-335` | Washington Nationals @ San Diego Padres — MLB | **San Diego 3–2 Washington.** Pivetta 5.0 scoreless IP in his return; Mason Miller 34th save. | `Washington +1.5` (p 0.59) — **WIN** | San Diego Padres — **WIN** | **`MLB — PRIMARY_SCORED`**; card mean Brier **0.2541** |
| `P-336` | Carabobo FC vs Estudiantes de Mérida — Venezuela Primera, Clausura J8 | **Carabobo 1–0 Estudiantes** (HT 1–0; Eric Ramírez 30'). Post-final stats Carabobo 3 corners, Estudiantes 9 (12 total); Estudiantes ~27 shots / ~8 on target. | `Under 2.5 goals` (p 0.60) — **WIN** | Carabobo FC — **WIN** | `EXPLORATORY`; card mean Brier **0.1751**; **top 3 rows all WON** |
| `P-337` | Barracas Central vs Argentinos Juniors — Argentina Liga Profesional, Clausura F8 | **Barracas 0–0 Argentinos** (HT 0–0). Corners Barracas 3, Argentinos 4. | `Under 2.5 goals` (p 0.65) — **WIN** | Argentinos Juniors — **LOSS** (draw) | `EXPLORATORY`; card mean Brier **0.2603**; **deep retro — R2 + R3 lost, winner wrong** |
| `P-338` | Iva Jovic vs Coco Gauff — US Open Women's Singles, R16 | **Gauff def. Jovic 6–1, 6–4** (17 games; Gauff +7 aggregate). | `Gauff -4.5 games` (p 0.54) — **WIN** | Coco Gauff — **WIN** | `EXPLORATORY` (tennis); card mean Brier **0.2163**; **top 2 rows both WON — best card of cohort** |
| `P-339` | Doosan Bears @ Hanwha Eagles — KBO | **Hanwha 6–1 Doosan.** Ryu Hyun-jin 6 IP / 1 R (9th win); Heo In-seo & Kang Baek-ho HR. | `Doosan +1.5` (p 0.60) — **LOSS** | Hanwha Eagles — **WIN** | `EXPLORATORY`; card mean Brier **0.3368**; **deep Rank-#1 retro** |
| `P-340` | Incheon United vs Bucheon FC 1995 — K League 1, R28 | **Incheon 2–1 Bucheon** (HT 1–1; Bucheon 33', Mugoša 43', Ibiza 70'). 7 total corners. | `1H Over 0.5 goals` (p 0.61) — **WIN** | Incheon United — **WIN** | `EXPLORATORY`; card mean Brier **0.2155**; **top 2 rows both WON** |
| `P-341` | BUL FC vs Ntugasaze FC — Uganda Premier League, R3 | **BUL 4–1 Ntugasaze** (HT 2–1; 10', 30', 43', + 2nd half). | `1H Over 0.5 goals` (p 0.61) — **WIN** | BUL FC — **WIN** | `EXPLORATORY`; 4-row partial mean Brier **0.2443**; **C03 corners unsettleable** |
| `P-342` | MŠK Novohrad Lučenec vs KFC Komárno — Slovnaft Cup, R3 | **Komárno 2–0 Lučenec** (HT 0–0; goals 74', 90'). Reported corners 1–15 (16 total) from secondary aggregators only. | `1H Over 0.5 goals` (p 0.68) — **LOSS** | KFC Komárno — **WIN** | `EXPLORATORY`; 4-row settled mean Brier **0.3880**; **deep Rank-#1 retro; C03 provisional** |
| `P-343` | Bangladesh Women vs UAE Women — Women's T20 Asia Cup, Group B | **Bangladesh 103/7 beat UAE 69/9 by 34 runs.** Bangladesh batted first. | — | — | **ADMIN CLOSED / NO FORECAST** — start crossed, innings order unverified. Non-scorable. |
| `P-344` | Hungary Women vs Japan Women — FIBA Women's Basketball World Cup, Qual. to QF | **Hungary 84–63 Japan** (total 147; margin +21). Réka Lelik 23; Japan's Saki Hayashi off with a broken right arm after 8 min. | `Japan +3.0` (p 0.56 win) — **LOSS** | Hungary Women — **WIN** | `EXPLORATORY`; card mean Brier **0.3334** (mini-log's stated 0.2834 corrected — see note); **deep Rank-#1 retro** |

**`P-344` Brier correction.** The mini-log's settlement table lists the four correct per-row Brier values (0.3136, 0.2116, 0.2116, 0.3969) but states a card mean of "0.2834". The arithmetic mean of those four values is **1.3337 / 4 = 0.3334**. The corrected figure is used in the scorecard below. No row result changes.

### Full contract-row grades

- **`P-335`** (`MLB PRIMARY_SCORED`): 1 `WSH +1.5` p0.59 **W** (0.1681) · 2 `Over 8.0` p0.52 **L** (0.2704) · 3 `SD -1.5` p0.41 **L** (0.1681) · 4 `Under 8.0` p0.36 **W** (0.4096). **Mean Brier 0.2541.** (2 W / 2 L) · Potential winner Padres **W**.
- **`P-336`**: 1 `Under 2.5` p0.60 **W** (0.1600) · 2 `Over 7.5 total corners` p0.59 **W** (0.1681) · 3 `1H Over 0.5` p0.56 **W** (0.1936) · 4 `1H Under 0.5` p0.44 **L** (0.1936) · 5 `Over 2.5` p0.40 **L** (0.1600). **Mean Brier 0.1751.** (3 W / 2 L) · Potential winner Carabobo **W**.
- **`P-337`**: 1 `Under 2.5` p0.65 **W** (0.1225) · 2 `1H Over 0.5` p0.60 **L** (0.3600) · 3 `Argentinos team corners Over 4.5` p0.58 **L** (0.3364; had 4 — missed by one) · 4 `1H Under 0.5` p0.40 **W** (0.3600) · 5 `Over 2.5` p0.35 **L** (0.1225). **Mean Brier 0.2603.** (2 W / 3 L) · Potential winner Argentinos **L** (0–0 draw).
- **`P-338`** (tennis, `EXPLORATORY`): 1 `Gauff -4.5 games` p0.54 **W** (0.2116) · 2 `Under 21.5 games` p0.53 **W** (0.2209) · 3 `Over 21.5 games` p0.47 **L** (0.2209) · 4 `Jovic +4.5 games` p0.46 **L** (0.2116). **Mean Brier 0.2163.** (2 W / 2 L) · Potential winner Gauff **W**.
- **`P-339`** (KBO, `EXPLORATORY`): 1 `Doosan +1.5` p0.60 **L** (0.3600) · 2 `Over 9.5` p0.56 **L** (0.3136) · 3 `Under 9.5` p0.44 **W** (0.3136) · 4 `Hanwha -1.5` p0.40 **W** (0.3600). **Mean Brier 0.3368.** (2 W / 2 L) · Potential winner Hanwha **W**.
- **`P-340`**: 1 `1H Over 0.5` p0.61 **W** (0.1521) · 2 `Under 10.5 total corners` p0.59 **W** (0.1681) · 3 `Under 2.5` p0.55 **L** (0.3025) · 4 `Over 2.5` p0.45 **W** (0.3025) · 5 `1H Under 0.5` p0.39 **L** (0.1521). **Mean Brier 0.2155.** (3 W / 2 L) · Potential winner Incheon **W**.
- **`P-341`**: 1 `1H Over 0.5` p0.61 **W** (0.1521) · 2 `Under 2.5` p0.58 **L** (0.3364) · 3 `Over 7.5 total corners` p0.55 **UNSETTLEABLE** (not booked) · 4 `Over 2.5` p0.42 **W** (0.3364) · 5 `1H Under 0.5` p0.39 **L** (0.1521). **4-row settled mean Brier 0.2443.** (2 W / 2 L) · Potential winner BUL **W**.
- **`P-342`**: 1 `1H Over 0.5` p0.68 **L** (0.4624) · 2 `Over 2.5` p0.56 **L** (0.3136) · 3 `Over 8.5 total corners` p0.54 **PROVISIONAL WIN** (16 reported; not booked) · 4 `Under 2.5` p0.44 **W** (0.3136) · 5 `1H Under 0.5` p0.32 **W** (0.4624). **4-row settled mean Brier 0.3880.** (2 W / 2 L) · Potential winner Komárno **W**.
- **`P-344`** (FIBA, `EXPLORATORY`): 1 `Japan +3.0` p0.56 **L** (0.3136) · 2 `Over 146.5` p0.54 **W** (0.2116) · 3 `Under 146.5` p0.46 **L** (0.2116) · 4 `Hungary -3.0` p0.37 **W** (0.3969). **Mean Brier 0.3334.** (2 W / 2 L) · Potential winner Hungary **W**.

### v4.0 Brier / calibration scorecard — after `P-333`–`P-344`

| Population | This cohort — cards | Scored binary rows | W / L | Mean Brier (method) | 0.5 baseline |
|---|---|---:|---:|---:|---:|
| **MLB — `PRIMARY_SCORED`** | `P-335` | 4 | 2 / 2 | **0.2541** | 0.2500 |
| **EPL / NRL / AFL — `PRIMARY_SCORED`** | — | 0 | — | — | — |
| `EXPLORATORY` (soccer `P-336`/`P-337`/`P-340`/`P-341`/`P-342`, KBO `P-339`, tennis `P-338`, FIBA `P-344`) | 8 | 35 | 18 / 17 | **0.2665** | 0.2500 |
| **This cohort — all scored rows** | 9 | **39** | **20 / 19** | **0.2653** | **0.2500** |
| **Running mixed total (prior 33 + this 39)** | 16 | **72** | **37 / 35** | **0.2436** | 0.2500 |
| **Running `PRIMARY_SCORED` (EPL 10 + MLB 8)** | 4 | **18** | **9 / 9** | **0.2466** | 0.2500 |

Combined calibration table (this cohort's 39 rows; buckets ≤ 0.50 are mostly the complement row on each card — a mirror of its pair, not independent evidence):

| Probability bucket | Rows | Wins | Win rate |
|---|---:|---:|---:|
| 0.65–0.70 | 2 | 1 | 50% |
| 0.60–0.64 | 5 | 3 | 60% |
| 0.55–0.59 | 10 | 4 | 40% |
| 0.50–0.54 | 4 | 3 | 75% |
| 0.45–0.49 | 4 | 1 | 25% |
| 0.40–0.44 | 8 | 5 | 63% |
| 0.35–0.39 | 5 | 2 | 40% |
| 0.30–0.34 | 1 | 1 | 100% |
| **Total** | **39** | **20** | **51%** |

**Sample size, stated prominently: 39 scored rows across 9 cards and ~8 competitions, with heavy within-card dependence, 8 of 9 cards `EXPLORATORY`.** The `EXPLORATORY` mean (0.2665) is *worse* than the 0.5 baseline; the single `PRIMARY_SCORED` card (0.2541) is essentially at baseline. The 0.55–0.64 band — where the cards put their "most likely" picks — went 7 W / 15 L this cohort (47%). **Nothing here supports a calibration, discrimination or superiority claim.** Per user direction this cohort is **learning-only, not performance-eligible evidence**; it is folded into the running scorecard for continuity but the running mean is not a quality verdict. `PRIMARY_SCORED` card count is **4**; the pattern/calibration review runs at 25 (`METHOD.md` §7.2).

---

### Per-card three-question retrospective (`METHOD.md` §7.2)

**`P-333` — Pakistan Women 143/8 beat Hong Kong Women 71.** *Administrative closure — no forecast.* Pakistan batted first and cleared the user's 139.5 first-innings threshold at 143/8, then Sandhu's 6/7 dismantled Hong Kong. Those are post-issue facts; the card correctly refused to freeze a Pakistan-first-innings target while the toss was unverified after the scheduled start crossed (`CR-P3`, `RULES_GENERAL.md` start-crossing invariant). *Smallest change:* operational only — begin the toss / live-state handshake earlier when an innings-order-dependent cricket target is requested, so the pregame window is not lost. No sporting-model change; process worked as designed.

**`P-334` — Germany Women 83–58 Mali Women.** *Administrative closure — no forecast.* A draft ranking existed during research but was not delivered before tip, and FIBA never exposed a verified live clock/score. Germany's defensive suppression and Mali's extreme (record 20-three) Japan shooting environment were both identified as uncertainty branches. *Smallest change:* obtain the official live/starting-five state faster on a live request; no retrospective model weight from an unpublished draft (`L-117`).

**`P-335` — San Diego 3–2 Washington (`MLB PRIMARY_SCORED`).** *Driver:* the best-case branch of Nick Pivetta's return distribution — five scoreless innings on 63 pitches. Washington never reached the earlier-relief / upper-total branch that had lifted the total centre to 9.1; the game finished on 5 total runs, and San Diego won by exactly one, the state that made `WSH +1.5` Rank #1 correct and `SD -1.5` a loss. *Knowable:* **yes, more than the first reading allowed.** Second-pass research (2026-09-09) recovered the full rehab **pitch-count ladder**, which the card had retrieved only as innings: **14 pitches → 47 pitches (3 IP) → 64 pitches (4⅓ IP, scoreless, 7 K, 44 strikes)** at Triple-A El Paso on Aug 30. A starter who has just completed 64 pitches scorelessly is stretched to roughly five major-league innings — and he threw **63 pitches / 5.0 scoreless**. The "short start → early relief transition → Over" branch that received the visible **+0.20** net scoring adjustment was therefore **contradicted by evidence the card had partially retrieved**: it recorded the innings and omitted the pitch count, strike rate, strikeout total and scoreless result, which are the four fields that actually forecast the major-league workload ceiling. The exact five scoreless innings were not knowable; the *workload ceiling* was. *Smallest change:* print the **full rehab pitch-count ladder** (pitches / IP / ER / SO / strike rate per outing, in order) before any short-start branch takes a signed total adjustment — new `RULES_BASEBALL.md` control 25, under cross-sport gate **`G-L7`** (§16.5(c)). *What went right:* margin decomposition (control 4/17) and the one-run-favourite-win coexistence were correct; Rank #1 and the potential winner both won.

**`P-336` — Carabobo 1–0 Estudiantes.** *Driver:* Eric Ramírez converted Carabobo's first-half chance; Estudiantes produced heavy territory (≈27 shots, ≈8 on target, 9 corners) without scoring. The 1–0 validated the literal `Under 2.5` but **not** a low-event mechanism. *Knowable:* **yes** — Ramírez's return from suspension was named and directly included; the Under leaned on Carabobo's multi-window home low-output (respecting `G17` — not a single streak). What the card under-did was decomposing **creation vs shot quality vs finishing vs goalkeeping** before treating the clean-sheet history as a low-event mechanism (`RULES_SOCCER.md` control 27). *Smallest change:* when an Under is supported by a clean-sheet/low-score run, place current shots/xG/SOT creation and a goalkeeper/finishing split beside the outcome rates. *What went right:* **top 3 ranked rows all won**; the corner row (R2) had a genuine high-event attacking mechanism, not a possession proxy.

**`P-337` — Barracas 0–0 Argentinos (deep retro — R2 + R3 lost, winner wrong).** See the deep-retrospective block below.

**`P-338` — Gauff def. Jovic 6–1, 6–4 (best card of cohort).** *Driver:* Gauff's return pressure created repeated break chances (converted 5 of 11) and Jovic never forced the deciding-set / close-straight mass. *Knowable:* **yes** — the single shared match tree gave its largest weight (42%) to "Gauff dominant straight-set control" and explicitly flagged Jovic's second-serve/break exposure against Gauff's return; the realized 6–1, 6–4 was even more separated than the representative Rank-#1 scoreline (6–3, 6–4 = 19 games) that the card wrote and verified against both leading directions. *Smallest change:* none beyond continuing to build one tree with explicit branch weights and run the representative-scoreline coherence check (`RULES_TENNIS.md` §4, control 12). **This is the positive model that cross-sport learning G-L1 generalises.** *What went right:* winner, handicap and total all generated coherently from one object; the Rome clay H2H was correctly kept as a kill path, not allowed to dominate the hard-court read (control 3).

**`P-339` — Hanwha 6–1 Doosan (deep Rank-#1 retro).** See the deep-retrospective block below.

**`P-340` — Incheon 2–1 Bucheon.** *Driver:* Bucheon scored first (33'), Incheon replied before half (43') and again at 70'; the match occupied the **exact 2–1 upper-tail state written in the card's own kill paths**. *Knowable:* **yes** — both attacking selections, Incheon's central-defensive suspension (Kim Gun-hee) and "2–1" as an Under kill state were all in the card; those factors received only a modest net signed adjustment, leaving the FT centre at 2.40 and `Under 2.5` at Rank #3 (p 0.55). *Smallest change:* when a named upper-tail score state is supported by **both confirmed attacking shapes plus a current defensive absence**, assign it an explicit branch **mass** in the joint object rather than leaving it as an unquantified kill-path sentence (cross-sport learning **G-L1**). *What went right:* **top 2 rows both won**; 1H model (control 20 reconciliation was clean) and corner-Under model were good; potential winner correct.

**`P-341` — BUL 4–1 Ntugasaze.** *Driver:* a class gap that did not stay a "low-scoring underdog" story — Ntugasaze scored (30' equaliser) and BUL's superior attack converted repeatedly to 4–1. A **mismatch-plus-underdog-contribution** branch, not simple favourite dominance. *Knowable:* **partly** — the card knew Ntugasaze had shipped 4 goals in its first two top-flight games and labelled promoted-team uncertainty as wide, but it shrank aggressively toward BUL's **older** low-event home regime and partly imported Ntugasaze's lower-tier promotion form into a top-flight total centre (2.35). *Smallest change:* for a newly promoted side in its first few top-flight matches, build a separate **promotion-translation defensive branch** before pooling lower-tier form or an older opponent home regime into the total centre (cross-sport learning **G-L3**). *What went right:* R1 `1H Over 0.5` and the BUL winner call were correct; the pre-registered corner-settlement gate ("if the exact provider cannot be verified, the row remains `UNSETTLEABLE` rather than inferred") did its job — no W/L was manufactured from a secondary 12-corner display.

**`P-342` — Komárno 2–0 Lučenec (deep Rank-#1 retro).** See the deep-retrospective block below.

**`P-343` — Bangladesh Women 103/7 beat UAE Women 69/9.** *Administrative closure — no forecast.* Bangladesh batted first, made a low 103/7, then bowled UAE out cheaply. The card correctly refused to treat an unresolved conditional Bangladesh first-innings market as unconditional (`CR-P3`). *Smallest change:* same as `P-333` — earlier toss/XI acquisition for innings-order-dependent targets; no probability may be backfilled.

**`P-344` — Hungary 84–63 Japan (deep Rank-#1 retro).** See the deep-retrospective block below.

---

### Deep Rank-#1 / top-two retrospectives

#### `P-337` — Barracas Central 0–0 Argentinos Juniors — `EXPLORATORY` — R2 and R3 lost, potential winner wrong

| Question | Finding |
|---|---|
| What went right? | **R1 `Under 2.5` (p 0.65) won for the right mechanism** — Barracas' low-output environment was persistent across L5/L10/L15/L20 (combined 1.40 / 1.40 / 1.73 / 1.80), not a single streak, so it survived the `G17`/`G17.1` audit. The draw band was correctly large (31%), which is why the outright Argentinos winner call was explicitly a plurality (46%), not asserted as a lock. `Over 2.5` was correctly bottom-ranked (p 0.35) and lost. |
| What went wrong? | **Internal incoherence at the top of the card.** The same low-event mechanism that drove Rank #1 was not carried into Rank #2: `1H Over 0.5` was given p 0.60 and ranked above its complement mostly on raw venue/phase frequency (a first-half goal in 4/7 Barracas and 6/7 Argentinos current-Clausura matches) rather than on a current early-chance-creation mechanism after Alan Lescano's absence and Barracas' compression. The realized match had only 14 total shots, 4 combined shots on target and 0.88 combined xG — a genuinely low-event game, exactly what Rank #1 implied. The `Argentinos team corners Over 4.5` row (p 0.58) lost by **one corner** (4). The potential-winner call overstated Argentinos' ability to turn a possession/territory edge into scoring separation against a side built to deny clean chances. |
| Actual mechanism | Barracas successfully compressed the match; Argentinos' territory never became high-quality chance volume; the first half stayed 0–0; the corner derivative stopped one below the line. |
| Improvement | **`RULES_SOCCER.md` control 20 is reinforced, not replaced:** before `1H Over 0.5` outranks its complement *inside a card whose own FT centre is Under / low*, require a **named current early-chance-creation mechanism** that survives creator absences and opponent compression — historical first-half occurrence frequency is not sufficient. This is the same class of miss as `P-323` (Everton–Man Utd, cohort `P-318`–`P-332`): a high 1H Over probability sitting on top of a card that also held multiple low-event signals. Second instance → strengthen the disclosure requirement (below), do not yet promote an ordinal bar (`L-087`). |
| Grade (background) | **C+** — Rank #1 mechanism good; top-of-card cross-market coherence weak. |

The `Argentinos team corners Over 4.5` one-corner miss is appended to the **distance-to-line** candidate-watch item (`P-319`/`P-325`/`P-328` prior; now `P-337`). A one-corner miss is **not** a partial win and does not justify an ordinal rule; it is a diagnostic. `P-337` is `EXPLORATORY` and does not advance the 25-card `PRIMARY_SCORED` promotion cadence.

#### `P-339` — Hanwha Eagles 6–1 Doosan Bears — KBO — `EXPLORATORY` — Rank #1 and Rank #2 both lost

| Question | Finding |
|---|---|
| What went right? | **Potential winner Hanwha — correct.** Choi Seung-yong's weak run-prevention profile (5.74 ERA, 1.55 WHIP, .292 opp AVG) and Hanwha's power concentration (152 HR, LH starter matchup) were correctly identified as the mechanism that ultimately produced the runs. The card did not force a binary MLB-style winner — it explicitly preserved the KBO tie branch (3%). `Under 9.5` and `Hanwha -1.5` were correctly the bottom two rows and both won. |
| What went wrong? | **Rank #1 `Doosan +1.5` (p 0.60) lost by 5 runs; Rank #2 `Over 9.5` (p 0.56) lost by 3.** **Corrected diagnosis after second-pass research (2026-09-09):** this was not primarily a weighting error. The card used an **aggregate** — "Ryu 0–3, 7.31 ERA through seven second-half starts" — where the **game log was available on the KBO official English player page, a source already listed in the card's own register.** Opening it shows the aggregate concealed three decisive facts: |
| | **Ryu's actual last four starts:** Aug 13 vs Doosan **3⅓ IP, 7 ER, 2 BB**; Aug 20 vs Kia **6.0 IP, 4 ER, 0 BB**; Aug 26 vs SSG **5.0 IP, 0 ER, 7 K, 0 BB**; Sep 2 vs KT **5.0 IP, 3 ER, 1 BB**. (1) The slump was **front-loaded** — the disaster start was three weeks old. (2) The **most recent quality evidence was a scoreless seven-strikeout start**. (3) **Command never broke**: 2/0/0/1 walks across the window, against **17 walks in 125⅔ innings** for the season (~1.2 BB/9, elite). An ERA-only slump with an intact walk rate and a recent dominant outing is a **noisy-outcome slump**, not a skill decline — which is precisely the distinction `RULES_BASEBALL.md` control 13 exists to force. The card never made it because it never opened the log. Ryu then threw 6.0 IP / 1 ER for his 9th win. |
| Actual mechanism | Ryu's run prevention dominated a weak Doosan lineup; Hanwha's power converted Choi's traffic into separation; final 7 total runs, margin 5. |
| Improvement | **Primary:** `RULES_GENERAL.md` §16.5(c) / **`G-L7`** — an aggregate may not carry directional weight while its disaggregated record sits unopened in a source the card already cites; otherwise mark `AGGREGATE_ONLY` and cap the dependent rows. Instantiated as **new `RULES_BASEBALL.md` control 24**: print the per-start log (IP/ER/SO/**BB**) and state whether the run is front-loaded, back-loaded or uniform and whether **command held**. **Secondary:** control 13 and `G-L2` (§16.5(b)) — the resulting uncertainty is width, not a signed Over lean. **Third:** `G-L8` (§16.5(d)) — the Over's normalised edge was `0.75/4.1 = 0.18`, which does not support 0.56 being ranked above a better-evidenced row. |
| Grade (background) | **C** — correct winner and correct naming of both key branches, but the decisive evidence was one click away in a cited source and was not retrieved. |

#### `P-342` — KFC Komárno 2–0 MŠK Lučenec — Slovnaft Cup — `EXPLORATORY` — Rank #1 lost, Rank #2 lost

| Question | Finding |
|---|---|
| What went right? | **Potential winner Komárno — correct.** The class-gap/territorial-pressure read is consistent with the enormous reported corner edge (1–15). The **2–0 control state was explicitly printed in the card's kill paths** before issue. `Under 2.5` (R4) and `1H Under 0.5` (R5) — the bottom two rows — both won. |
| What went wrong? | **Rank #1 `1H Over 0.5` at p 0.68 was the single worst miss of the cohort** (HT was 0–0; Brier 0.4624). Rank #2 `Over 2.5` (p 0.56) also lost — the final total was 2. The card documented Komárno's heavy rotation and named a 1–0/2–0 control state as an Under kill path, then still gave the class gap enough force to imply early goals and a 3+ total. A heavily rotated cup favourite against a third-tier side produced exactly the "territorial dominance without early conversion" pattern the rotation evidence pointed to: goals at 74' and 90'. |
| Actual mechanism | Komárno controlled territory but its rotated attack did not convert until late; first half scoreless; final total 2; huge corner count from sustained pressure. |
| Improvement | **`RULES_SOCCER.md` controls 2 and 28 are reinforced:** in a cup mismatch with a **heavily rotated favourite**, split *territorial dominance* from *conversion timing* and explicitly weight a "late depth breakthrough / 1–0 or 2–0, 0–0 at half" branch **before** ranking `1H Over` and `FT Over`. Class gap predicts *eventual result* and *corner/territory volume*; it does not predict *early* goals or a *high total* when the favourite is rotated. Cross-instance with `P-341` (opposite direction — promoted side, blowout) → both are tier-translation failures → cross-sport learning **G-L3**. Third cohort instance of a named-kill-path state being under-massed (`P-340`, `P-342`, and `P-344` below) → cross-sport learning **G-L1**. |
| Grade (background) | **C-** — worst-graded card of the cohort on the settled rows. |

#### `P-344` — Hungary 84–63 Japan — FIBA W World Cup — `EXPLORATORY` — Rank #1 lost by a large margin

| Question | Finding |
|---|---|
| What went right? | **Potential winner Hungary — correct.** The size/rebounding mismatch (Hungary 43.7 RPG vs Japan 31.7; Hungary's paint edge through Juhász + Takács-Kiss) was correctly identified as the foundation. `Over 146.5` (R2) survived — total 147 — though by only 0.5, so this is a boundary escape, not validation of the projected 149.5 centre. |
| What went wrong? | **Rank #1 `Japan +3.0` (p 0.56 win) lost by 21.** **Corrected diagnosis after second-pass research (2026-09-09):** the first reading called Réka Lelik's 23 points an under-weighted "breakout". Opening the FIBA official player profiles — **already listed in the card's own source register** — shows it was not a breakout, and that the real failure was a **participant-exposure retrieval gap**. Hungary's pregame scoring across the three group games: Juhász **17.0 PPG** (quantified on the card) · Takács-Kiss **13.0 PPG** (quantified on the card) · **Lelik 8.7 PPG — 8 / 14 / 4, on ~26.3 minutes a game, 4.3 RPG, 3.5 APG — carried on the card as an unquantified name** inside the phrase "leaders include Dorka Juhasz…, Virag Takacs-Kiss…, Reka Lelik and Agnes Studer". She was Hungary's **third-highest scorer**, playing starter minutes, with a pregame range that already included a 14-point game. **A blowout requires a third scorer, and the card's margin distribution contained no third scorer with a number in it** — which is mechanically why averaging cross-opponent scores (Hungary 76.0, Japan 76.35) and applying ±1–2-point tweaks produced a symmetric ±10–12-point width around +0.5. Her 23 was an upside game (~2.6× her pregame mean), not a black swan, and FIBA's own framing of Hungary as a record-setting **"Twin Towers"** side is exactly the shape that transfers usage outward when the paint is collapsed on. Separately, Japan's perimeter **floor** was 11.1% and 23.3% from three in its two European group losses, not the tournament average inflated by a record 20-three game against Mali. Saki Hayashi's 9th-minute broken arm (8 minutes played) was a genuine **in-game shock, not a pregame model miss** (`L-117`) — it explains part of Japan's downside but does not excuse the separately underweighted Hungary separation branch. |
| Actual mechanism | Hungary converted its size foundation into a 21-point two-way margin; Lelik supplied the third scoring axis the card had never quantified; Japan's perimeter attack did not sustain; a mid-game Japan injury compounded it. |
| Improvement | **Primary:** `RULES_GENERAL.md` §16.5(c) / **`G-L7`** — instantiated as **new `RULES_BASKETBALL.md` control 20**: print a quantified exposure line (PPG, minutes, rebounds, assists) for **every top-three scorer and every ~20+-minute player on both sides**; a player carried as a bare name in a "leaders include…" phrase is `AGGREGATE_ONLY` and caps the dependent margin/total rows. **Secondary:** new **control 21** — secondary-scorer usage transfer in a mismatch, plus "a volatile perimeter offence's floor is its worst recent same-regime games, not its average". **Also:** `G-L1` (enumerate margin families — blowout 15+ / clear 6–14 / close 1–5 / underdog win — with explicit mass) and `G-L4` (winner ≠ margin: a right winner with a badly compressed margin distribution is a margin-model failure, not a partial success). |
| Grade (background) | **C** — correct winner, correct mismatch identification, but the third scorer who decided the margin sat quantified in a cited source and was never retrieved. |

---

### Why the picks went right / wrong — cross-card synthesis, linked to prior lessons

**The headline pattern: the preferred full-match total (goals / runs / points) O/U lost on 5 of 9 cards** (`P-335` Over, `P-339` Over, `P-340` Under, `P-341` Under, `P-342` Over). It won on `P-336`, `P-337`, `P-338` (all `Under`, all built on *persistent multi-window low-output environments* that survived `G17`), and `P-344` (`Over`, by 0.5). Every card had at least one O/U row win — that is mechanically guaranteed by complementary pairs and is **not** evidence of skill; the meaningful question is the *ranked* total, and the ranked FT total is 4 W / 5 L this cohort. Of the 5 losses, 3 predicted `Over` and came `Under` (`P-335`, `P-339`, `P-342`) and 2 predicted `Under` and came `Over` (`P-340`, `P-341`) — so the fix is **not** "always predict lower"; it is the three mechanisms below.

**0 — THE ROOT CAUSE, found on second-pass research: all three Rank-#1 losses were the same retrieval failure, not three different weighting errors.** In each case the card leaned on an **aggregate** while the **disaggregated record sat unopened in a source the card had already listed in its own register** — and in each case the disaggregated record pointed the other way.

| Card | Aggregate the card used | Disaggregated record available | What it actually showed |
|---|---|---|---|
| `P-339` | "Ryu 0–3, **7.31 ERA** through seven second-half starts" | KBO official English player-page **game log** (in the card's register) | Last four starts **7 ER/3⅓ (2 BB) → 4 ER/6.0 (0 BB) → 0 ER/5.0, 7 K, 0 BB → 3 ER/5.0 (1 BB)**. Slump **front-loaded** (worst start three weeks old); most recent quality evidence was a **scoreless 7-K start**; **command never broke** (~1.2 BB/9 season, 17 BB in 125⅔ IP). A noisy-outcome slump, not a skill decline. He threw 6.0 IP / 1 ER. |
| `P-335` | "**4.1 innings** for Triple-A El Paso on Aug 30" (innings only) | MLB/MiLB **rehab pitch-count ladder** (same lane the card used) | **14 → 47 → 64 pitches**, the last being **4⅓ scoreless, 7 K, 44 strikes**. That forecasts a ~5-inning major-league ceiling. He threw **63 pitches / 5.0 scoreless** — the `+0.20` short-start Over adjustment was contradicted by evidence the card had half-retrieved. |
| `P-344` | "leaders include Juhász (17.0 PPG), Takács-Kiss (13.0 PPG), **Réka Lelik** and Ágnes Studer" | FIBA official **player profiles** (in the card's register) | Lelik was Hungary's **third-highest scorer at 8.7 PPG (8/14/4) on ~26.3 min**, 4.3 RPG, 3.5 APG. The card quantified the two players above her and left the third as a bare name. **A blowout needs a third scorer; the margin distribution contained no third scorer with a number.** She scored 23. |

**Prior lesson link:** `G8` already requires an exact source record per decisive fact, and `G13.1` requires windowed form — but nothing required the *granularity* to match the claim, so a summary could satisfy both. → **new cross-sport gate `G-L7` (`RULES_GENERAL.md` §16.5(c))**: where a decision-driving claim rests on an aggregate and the disaggregated record is available from a source already in the card's register, open and print it; otherwise mark `AGGREGATE_ONLY` and cap the dependent row. Instantiated as `RULES_BASEBALL.md` controls 24–25 and `RULES_BASKETBALL.md` control 20, and in every other sport file's §"2026-09-09". **This is the highest-value finding of the pass**, because it is cheap, checkable, requires no new source, and would have touched all three losses.

**1 — Downstream of that: uncertainty about a key unit was converted into a directional total lean instead of into distribution width (`P-335`, `P-339`, `P-342`).** In all three the card correctly *named* the reversion / strong-performance branch, then gave it too little mass and let a "they might be worse than expected" argument push the total centre toward `Over` (`P-335` Pivetta return +0.20; `P-339` Ryu slump feeding Doosan runs; `P-342` Komárno rotation net up after adjustments). All three came `Under`. **Prior lesson link:** `RULES_BASEBALL.md` controls 11/13/15 already require the mixture and the "state why the joint upper tail is subordinate" step; `G22` requires the bidirectional-sign audit. The audits were *run* and still produced asymmetric mass — because the evidence that would have re-weighted them was never retrieved (point 0). → **cross-sport learning G-L2**: variance widens the interval around the shrunk skill prior; a *net signed* total adjustment from unit uncertainty needs a *directional* mechanism (a confirmed pitch limit, a confirmed missing starter, a stated tactical shift), not "might underperform".

**2 — Named kill-path score-states were written as prose but not given probability mass in the joint object (`P-340`, `P-342`, `P-344`; also `P-335`, `P-339`).** `P-340` wrote "2–1 is an Under kill state" and finished 2–1. `P-342` wrote "1–0/2–0 control" and finished 0–2. `P-344` wrote the secondary-scorer risk as a sentence and Lelik scored 23. **Prior lesson link:** `RULES_GENERAL.md` §16.5 already requires explicit centre/width arithmetic; `RULES_SOCCER.md` control 20 requires early-goal reconciliation; `L-070` requires making "both competitors' ordinary win/separation states contract-evaluable" rather than a "prose upset/kill-path note". The gap is that a kill path currently satisfies the rule as a sentence. → **cross-sport learning G-L1**: the joint object must **enumerate the discrete score-state families with explicit probability mass** (the `RULES_TENNIS.md` §4 mixture-weights model, which produced the cohort's best card `P-338`), and any G22 kill path supported by current specific evidence must appear as one of those weighted branches. This is a **disclosure/arithmetic** requirement, not a fitted weight — it does not violate `L-087`.

**3 — Tier gap / heavy rotation was translated into scoring direction with the wrong shape (`P-341`, `P-342`).** `P-341` pooled a promoted side's lower-tier form and an old opponent home regime into a 2.35 total centre; the class gap produced a 4–1 blowout. `P-342` let a top-flight-vs-third-tier gap imply early goals and a 3+ total; the rotated favourite produced a late 2–0. **Prior lesson link:** `RULES_SOCCER.md` control 2 ("class gap is a prior, not protection"), control 23 (early-season aggressive shrinkage — but `P-341` over-shrank toward the *wrong* prior), control 28 (condition on the exact knockout population; no universal scoring sign). → **cross-sport learning G-L3**: build an explicit **tier-translation branch** — the stronger side's blowout tail is fatter than its own-division scoring rate suggests once it breaks through; the weaker side's lower-tier defensive numbers do not carry; and a *rotated* favourite specifically produces territory + late conversion, not early goals.

**What went right, and why — so the method keeps it:**

- **`P-338` (tennis, grade A−):** one shared match tree with **explicit branch weights** (42% dominant straight-set, 20% close straight, 12% wide deciding, …), winner + handicap + total all derived from it, and a **representative Rank-#1 scoreline** written out and checked against the other leading rows (`RULES_TENNIS.md` control 12). This is the template G-L1 exports to the other sports.
- **`P-336` / `P-337` Rank #1 `Under 2.5` (both won):** built on *persistent* low-output across every recency window plus the venue split, not a single streak — a clean pass of `G17`/`G17.1` and `RULES_SOCCER.md` §8.8's "use the longest defensible window". `P-336`'s corner Rank #2 also won on a genuine high-event attacking mechanism, not a possession proxy (`RULES_SOCCER.md` control 4, the `P-302` `wonCorners` worked example).
- **`P-335` Rank #1 `WSH +1.5` (won):** correct cushion decomposition (`RULES_BASEBALL.md` control 4) and correct representation of the one-run-favourite-win coexistence (control 17) — the favourite won and the underdog cushion still cashed.
- **Potential-winner calls: 8 of 9 correct** (`P-337` the only miss, a 0–0 draw where the card had already put the draw band at 31% and the winner at a 46% plurality). The winner-identification process is working; the misses are concentrated in the **margin and total corridors**, which is exactly what `RULES_GENERAL.md`'s "winner / margin / total allocation" separation predicts can happen.
- **Pre-registered derivative settlement gates worked** (`P-341-C03`): the card said "if the exact provider cannot be verified the row is `UNSETTLEABLE`, not inferred", and that is what happened — no W/L was manufactured from a secondary display (`G10.2`/`L-081`).

---

### Researched answer to the standing over/under directive

The standing instruction is that the preferred over/under selection should win more often. This section is the researched answer, and it starts by discarding a measure the framework has already retired.

**1. "At least one O/U row won" is meaningless and must not be reported as a success.** Every card in this cohort had at least one O/U row win — 9 of 9 — because an exact half-point Over/Under pair forces one winner on any completed event regardless of analytical quality (`L-055`). The 2026-09-06(d) review already caught this repository reporting "8 of 12" on that basis and corrected it to the honest measure, **highest-ranked O/U selection accuracy (7 of 12)**. That correction is re-applied here: this cohort's honest numbers are **highest-ranked O/U row of any kind 6 / 9**, and **highest-ranked full-match total 4 / 9**.

**2. The full-match goal centres are unbiased but imprecise — so a near-the-line total is genuinely a coin flip for this framework.** Measuring the five soccer cards against their own stated arithmetic:

| Card | Centre | Actual | Signed error | Line | Normalised edge `\|centre−line\|/width` | p assigned | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| `P-336` | 2.39 | 1 | −1.39 | 2.5 | **0.07** | Under 0.60 | **W** |
| `P-337` | 2.00 | 0 | −2.00 | 2.5 | **0.50** | Under 0.65 | **W** |
| `P-340` | 2.41 | 3 | +0.59 | 2.5 | **0.05** | Under 0.55 | **L** |
| `P-341` | 2.35 | 5 | +2.65 | 2.5 | ~0.08 (width never quantified — a §16.5 defect) | Under 0.58 | **L** |
| `P-342` | 2.83 | 2 | −0.83 | 2.5 | **0.17** | Over 0.56 | **L** |

**Mean signed error −0.20 goals. Mean absolute error 1.49 goals.** Stated widths were ±1.55–1.8 — so the widths were roughly *honest*, and the centres carry no systematic bias in either direction. That is the crucial finding, because it kills the obvious "fix": there is no directional correction to apply. The supplied line sat **0.05–0.50 goals** from the centre in every case, and a 0.05-goal edge on a ±1.5-goal error distribution is a coin flip that no additional research will convert into an edge.

**3. The probabilities were not derived from the cards' own arithmetic.** `METHOD.md` §5 requires the rank to be *derived from* the numbers. It was not: `P-335` computed the **largest** normalised edge on the cohort (`1.1/3.2 = 0.34`) and assigned its Over the **lowest** probability (0.52); `P-336` computed the **smallest** (0.07) and assigned nearly the **highest** (0.60). → new **`G-L8` (§16.5(d))**: print the normalised edge beside every total probability and make the probability a monotone function of it. **Honest counter-check, recorded because it cuts against the rule:** re-scoring the eight preferred-total rows at normal-CDF-coherent probabilities gives a mean Brier of **0.2614** versus the issued **0.2538** — on this cohort of eight, mechanical coherence would have been *slightly worse*. `G-L8` is therefore justified on **internal-consistency grounds only**, explicitly not as a demonstrated accuracy improvement.

**4. What the record actually supports: rank the total honestly rather than trying to pick it better.** In this cohort the full-match total went **2 / 2 when it was Rank #1** and **1 / 5 when it was Rank #2** (`P-344` won; `P-335`, `P-339`, `P-341`, `P-342` lost). The two Rank-#1 wins (`P-336`, `P-337`) were both **persistent multi-window low-output `Under`s** — the mechanism type that survives `G17` — and carried the two largest normalised edges. The Rank-#2 losses were near-tied totals promoted above better-evidenced rows. **Promote a full-match total only when it has both (a) a persistent multi-window mechanism — not a single-regime, single-streak or class-gap one — and (b) a normalised edge that justifies its probability.** This is an evidence-grade and disclosure requirement, not an ordinal bar: if a near-tied total genuinely holds the highest marginal likelihood on the slate it still ranks first (`G23.1`), it simply may not carry 0.58–0.60 while doing so.

**5. The phase total has been the more reliable O/U family across three cohorts.**

| Family | `P-294`–`P-305` | `P-318`–`P-332` | `P-333`–`P-344` | Combined |
|---|---|---|---|---|
| Highest-ranked O/U row of any kind | 7 / 12 | — | **6 / 9** | — |
| `1H Over/Under 0.5` | — | 5 W / 2 L | 3 W / 2 L | **8 W / 4 L (67%)** |
| Full-match goals total (soccer) | — | 6 W / 3 L | 2 W / 3 L | **8 W / 6 L (57%)** |

This is the **third** cohort consistent with the observation already written into `RULES_SOCCER.md` §"September 5(b)" — first-half goal markets have been the more resiliently-sourced and more reliably-ranked early-scoring contract type relative to both full-match totals and corners. Under the framework's own 3-recurrence threshold it is now registrable as a **`CANDIDATE`** with a prospective test manifest — **not** an ordinal bar, and **not** a licence to promote a 1H row over a better-evidenced full-match row. Samples are small, mixed-competition and within-card dependent, and both 1H losses this cohort (`P-337`, `P-342`) are explained by the two mechanisms above rather than by the family.

**6. Standing constraint, restated.** `RULES_GENERAL.md` §796 and every sport file's "September 5 implementation" section already forbid promoting an opposite pick **solely to manufacture one O/U win**. Nothing in this section licenses that. The improvement path is better retrieval (`G-L7`), honest width (`G-L2`), enumerated mass (`G-L1`) and coherent probability (`G-L8`) — not direction-shopping.

---

### Cross-sport learnings promoted to disclosure requirements (no fitted weight, no ordinal bar — `L-087` respected)

| ID | Learning | Where instantiated | Status |
|---|---|---|---|
| **G-L1** | The joint event object must **enumerate the discrete outcome-state families (score families / margin families / set-count families) with an explicit probability mass on each**, summing to 1. Every kill path from the `G22` bidirectional-sign audit that is supported by current, specific evidence must appear as one of those weighted branches, not only as a prose sentence. Write one **representative Rank-#1 outcome** in the settlement unit of every other supplied row and verify compatibility before freezing the order. | `RULES_GENERAL.md` §16.5 (extended); `RULES_TENNIS.md` §4 / control 12 (origin, already compliant); `RULES_SOCCER.md` §8.3/§8.7; `RULES_BASEBALL.md` §4/§8.7; `RULES_BASKETBALL.md` §4/§8.7 | **Disclosure requirement — added 2026-09-09.** Not an ordinal bar. Needs 25-card `PRIMARY_SCORED` recurrence data before any weighting rule. |
| **G-L2** | Uncertainty about a key unit's *performance level* (returning starter, veteran in a slump, heavily rotated side, debutant, an out-of-form shooter) widens the distribution around the **shrunk skill prior**; it does not move the centre. A *net signed* total/scoring adjustment attributed to that uncertainty requires a **named directional mechanism** (confirmed pitch-count limit, confirmed missing personnel, stated tactical change), not "they might be worse than expected". | `RULES_GENERAL.md` §16.5; `RULES_BASEBALL.md` controls 11/13/15 (reinforced); `RULES_SOCCER.md` control 2; `RULES_BASKETBALL.md` control 12 | **Disclosure requirement — added 2026-09-09.** Reinforces existing controls; no new weight. |
| **G-L3** | A competition-tier gap (promotion, cup mismatch, cross-division fixture) is a distinct uncertainty. Do **not** pool the weaker side's lower-tier defensive/scoring rates or an older opponent regime into the total/margin centre. Build a **tier-translation branch**: the stronger side's blowout tail is fatter than its own-division rate implies once it breaks through; a *rotated* favourite specifically produces territory + late conversion, not early goals or a high total. | `RULES_SOCCER.md` controls 2 / 23 / 28 (reinforced), new §"2026-09-09" note; candidate cross-sport for cup basketball/cricket | **Observation → candidate.** Two instances this cohort (`P-341`, `P-342`). Needs recurrence before promotion. |
| **G-L4** | Winner and margin/spread are separate questions and must be answered from the same enumerated family set but stated separately. A correct winner call with a badly compressed margin distribution (`P-344`: right winner, +0.5 centre vs +21) is a margin-model failure, not a partial success. | `RULES_GENERAL.md` (winner/margin/total separation, reinforced); `RULES_BASKETBALL.md` controls 9/11/16 | **Reinforcement of existing rule.** |
| **G-L5** | When an `Under`/low-total is supported by a clean-sheet or low-score run, decompose **creation → shot quality → finishing → goalkeeping** and place current shots/xG/SOT beside the outcome rates *before* treating the history as a low-event mechanism. A winning `Under` on a 1–0 where the loser had 27 shots (`P-336`) is an outcome-driven thesis that happened to cash. | `RULES_SOCCER.md` control 27 (reinforced) | **Reinforcement.** |
| **G-L6** | In-game shocks with no pregame forecastability (a 9th-minute injury, `P-344` Hayashi) are aleatory and must be tagged separately in the retrospective — they never become a "should have known" and never a pregame rule (`L-117`), but they also do not excuse a separately-underweighted branch. | `RULES_GENERAL.md` `G37.1` / `L-117` (reinforced, all sports) | **Reinforcement.** |
| **G-L7** | **Aggregate-to-disaggregate retrieval.** Where a decision-driving claim rests on an aggregate (a multi-start ERA, a "leaders" list, a rehab innings count, a form summary) and the **disaggregated record is available from a source already in the card's own register**, open and print it before the aggregate carries directional weight. Otherwise record `AGGREGATE_ONLY`; the dependent row cannot reach `LEAN`/`SUPPORTED`. | `RULES_GENERAL.md` §16.5(c); `RULES_BASEBALL.md` new controls 24–25; `RULES_BASKETBALL.md` new control 20; instantiated in all ten sport files' §"2026-09-09" | **Retrieval requirement — added 2026-09-09 (second pass).** **All three Rank-#1 losses trace to this single failure.** Highest-value finding of the pass; cheap, checkable, needs no new source. |
| **G-L8** | **Total-probability coherence.** A total row's probability must be a monotone function of its own normalised edge `\|centre − line\| / width`, and that normalised edge must be printed beside the probability (`METHOD.md` §5's "derived from"). | `RULES_GENERAL.md` §16.5(d); instantiated in all ten sport files | **Internal-coherence requirement — added 2026-09-09 (second pass).** Justified on consistency grounds **only**: the honest counter-check shows mechanical coherence would have *slightly worsened* this cohort's preferred-total Brier (0.2614 vs 0.2538, n=8). Recorded because it cuts against the rule. |

**No new fitted weight, ordinal bar, gate ID or `CANDIDATE` control is promoted from this cohort** (`L-087` firewall; `METHOD.md` §7.2 pattern-review cadence). G-L1 and G-L2 are added as **disclosure/arithmetic requirements** — the same class of change as §16.5's original "show the arithmetic" rule — because the user directed algorithm improvement and because they require *showing* an enumeration, not *weighting* it a particular way. G-L3 is an **observation with a candidate-watch entry** (2 instances). The 25-card `PRIMARY_SCORED` pattern review remains the gate for any ordinal rule.

### Candidate watch items — updated

| Item | Prior instances | New this cohort | Status |
|---|---|---|---|
| Distance-to-line recorded in every derivative retrospective | `P-319`, `P-325`, `P-328` | `P-337` (`Argentinos team corners Over 4.5` lost by exactly 1 corner) | Watch — 4 instances, all `EXPLORATORY`; still a diagnostic, not a rule |
| Named kill-path state under-massed in the joint object | (`P-323` retrospectively) | `P-340`, `P-342`, `P-344` | **Promoted to disclosure requirement G-L1** (enumerate families with mass); ordinal treatment still needs 25-card cadence |
| Unit-performance uncertainty → directional total lean | (`P-331` retrospectively) | `P-335`, `P-339`, `P-342` | **Promoted to disclosure requirement G-L2** |
| Tier / promotion translation as a distinct uncertainty | — | `P-341`, `P-342` | New candidate-watch item — needs 3+ recurrences in a 25-card window |
| Second-half / secondary bench-scorer contribution | `P-329` | `P-344` (secondary-scorer usage transfer, Lelik) | Watch — now cross-sport (soccer + basketball) |

### New / re-graded information sources (from this cohort)

Evaluated against `SOURCES.md` §1 vocabulary. None reaches `APPROVED FOR FEATURE`; all are prediction-time research / settlement lanes. Full detail folded into `SOURCES.md` and `DATA_SOURCE_REGISTER.md`.

| Source | Role demonstrated | Grade | Note |
|---|---|---|---|
| **Asian Cricket Council** `asiancricket.org/match/<id>` | Field-owning scorecard / innings state for the Women's T20 Asia Cup (`P-333`, `P-343`) | `CANDIDATE` — field owner for ACC events | Native competition body; use ahead of aggregators for ACC finals |
| **FIBA** game-center reports + player profiles (`fiba.basketball/en/events/.../games/<id>`, `.../teams/<team>/<playerid>`) | Field-owning result, per-player tournament minutes, tournament context (`P-334`, `P-344`) | `CANDIDATE` — field owner for FIBA events | Player-profile minutes confirmed Hayashi's 8-minute game post-hoc |
| **KBO** official Korean-language news + `koreabaseball.com` scoreboard; **SBS English** (`news.sbs.co.kr/english`) as an English cross-check | Field-owning KBO final + match detail (`P-339`); SBS English gave an accurate independent confirmation | `CANDIDATE` — reinforces `L-067` native-language sourcing | SBS English is a usable English rung for KBO/K-League when the Korean body page is slow |
| **Kawowo Sports** (`kawowo.com`) | Specialist current Uganda football result + timeline when the league official match detail is sparse (`P-341`) | `CANDIDATE — RESEARCH ONLY / cross-check` | Not automatically a corner-stat field owner; goal timeline reliable |
| **GHANAsoccernet** (`ghanasoccernet.com`) | Independent African-league result/scorer confirmation (`P-341`) | `CANDIDATE — RESEARCH ONLY / cross-check` | Secondary; corroborated Kawowo on `P-341` |
| **PlaymakerStats / zerozero / ceroacero / leballonrond / playmakerstats** family | Post-final structured soccer fields — shots, SOT, corners, xG where present (`P-336`, `P-337`, and the Part-2 `P-178`/`P-176` appendix update) | `CANDIDATE — RESEARCH ONLY / cross-check` | Declares Stats Perform lineage on some competitions; **still secondary** to an official/data-partner definition — aggregator agreement does not promote a niche field (`G10.2`/`L-081`). Frequently returns HTTP 403 to `WebFetch`; readable via search-surfaced snippets. |
| **Futbol24** (`futbol24.com`) | Minute-by-minute event timelines incl. reconstructable corner events (`P-340`) | `CANDIDATE — RESEARCH ONLY / cross-check` | Provenance-clear cross-check only; not a provider-definition substitute |
| **Forebet** post-final corner display | Corroborates niche corner counts in sparse competitions (`P-342-C03`; Part-2 `P-178`) | `CANDIDATE — RESEARCH ONLY / cross-check` | Secondary; cannot repair an unfrozen operator/provider definition |
| **matchcalendar.football** | Independent K League 1 result + scorer cross-check (`P-340`) | `CANDIDATE — RESEARCH ONLY` | Secondary aggregator |
| **`site.api.espn.com` public web box scores** (`espn.com/fiba/boxscore`, `/soccer/match`, `/mlb/game`) | Independent confirmation of `P-335`, `P-336`, `P-337`, `P-338`, `P-344` finals | `CANDIDATE` — same lineage as `SRC-ESPN-SITE-API-*` (`SOURCES.md` §2) | The ESPN structured lane's public web rendering is a reliable settlement cross-check; `fiba` box scores are exposed |

**Access-state observations (route-specific, not universal):** `ceroacero.es`, `forebet.com`, `sofascore.com` match pages returned **HTTP 403** to `WebFetch` on 2026-09-09; their content was still recoverable via `WebSearch` result snippets. This matches the standing `api.sofascore.com` `BLOCKED` note and the `r.jina.ai` cross-check caveat in `SOURCES.md` §6. No niche corner field was upgraded from these.

---

## 2026-09-11 — `P-345`–`P-371` imported, settled and retrospected

**Settlement authority:** `MDS-2026.09.06-v4.0`, read fresh this session from `METHOD.md`'s own header. **Frozen-evidence rule:** every issued rank, probability, contract, target, issue horizon and pre-game evidence block is immutable; this section adds only settlements, Brier grades, retrospectives and learnings. The full issued card text is archived byte-exact in `prediction logs/` (fingerprints below); each card block here reproduces its frozen ranks, contracts and probabilities. **Interpretation restriction (user directive, 2026-09-11, restated):** *"the log is still not performance-eligible, but continue to use it to learn."* These records are folded into the running scorecard for ledger continuity only; **no accuracy, calibration or improvement verdict is drawn from them** (`PERFORMANCE_ELIGIBILITY_POLICY.md` §"2026-09-11").

**Pass scope:** 26 issued cards (`P-345`–`P-369`, `P-371`), 1 administrative no-forecast closure (`P-370`), and 1 unsupplied collision record (`TMP-SETTLED-20260911-01`). Live-state check first; independent re-verification of finals at field owners; settlement of three derivative rows that had been left open; the table-format settlement block and three-question retrospective for every card; a deep retrospective for every Rank-#1 loss; a control-execution audit; cross-sport algorithm changes; source audit; and the researched answer to the standing over/under directive.

### Component fingerprints

| File (archived in `prediction logs/`) | Role | Bytes | Lines | SHA-256 | First on disk (Downloads mtime, AEST) |
|---|---|---:|---:|---|---|
| `PREDICTION_MINI_RUNNING_LOG_P357_RETROSPECTIVE_SETTLED_2026-09-10.md` | `P-345`–`P-357` issued cards + external settlement pass | 217,225 | 4,314 | `df032ce4a29754a49888ad19d4dc623c3f90a15a41a8467f247f6af63eaed20d` | 2026-09-10 17:37 |
| `PREDICTION_MINI_RUNNING_LOG_P358_UPDATED_P371.md` | `P-358`–`P-371` **pre-settlement issued text** | 177,484 | 2,333 | `a9aa720a8de05d75bf3a3ec7b6747d4103daf069a67024587775bd2afed216c9` | 2026-09-11 01:55 |
| `PREDICTION_MINI_RUNNING_LOG_P371_RETROSPECTIVE_SETTLED_2026-09-11.md` | `P-358`–`P-371` external settlement pass | 221,941 | 2,928 | `11ff49556efc9d9342de19c39cb445f28a50dd2174a3df1aced900853f3b04ef` | 2026-09-11 23:18 |
| `PREDICTION_MINI_RUNNING_LOG_P371_RETROSPECTIVE_SETTLED_REFRESHED_2026-09-11.md` | same, refreshed 23:12 AEST (adds the `P-366` result) — **the version reconciled here** | 228,830 | 2,989 | `a55ec0c9010aea8ecf69bbd68a9bbe6d643c75c7c12f7fe072dfc40fcb6eec30` | 2026-09-11 23:22 |
| `PREDICTION_MINI_RUNNING_LOG_P344_RETROSPECTIVE_UPDATED.md` | **byte-exact original** of the `P-333`–`P-344` component reconciled on 2026-09-09 | 202,089 | 3,071 | `b2ec07e8cc3d8840e9f4d3ae4a185e679cb19d5c4659a1299d6d0b3f04fb12a8` | 2026-09-09 12:10 |

- The Downloads copies suffixed ` (1)` are byte-identical re-downloads (same SHA-256) and were not archived twice.
- **`P-344` provenance correction.** The 2026-09-09 pass recorded that its component "was NOT supplied as a filesystem artifact" and archived an 8,118-byte reconstruction (`PREDICTION_MINI_RUNNING_LOG_P344.md`). The original was in fact present in Downloads; it is now archived byte-exact alongside. The reconstruction is kept (not deleted); its caveat is superseded.
- Self-reported fingerprints printed *inside* the mini-logs (`P-357` log: "Source SHA-256 `330b74a6…`", "updated-content `83a58623…`"; `P-371` logs: `d28c7ff4…`, `04594cee…`) were computed by the generating session before it appended its own integrity footer, so they neither equal nor are expected to equal the whole-file hashes above. Recorded as self-reported only.

**Immutability audit.** A line-level comparison of the pre-settlement file against the reconciled settled file found **all 1,638 non-blank issued lines of `P-358`–`P-371` verbatim** in the settled version — the external settlement pass altered no issued rank, probability, target or evidence line. No pre-settlement copy of `P-345`–`P-357` exists, so that block is recorded `IMMUTABILITY_UNVERIFIABLE (no pre-settlement copy supplied)` — a limitation, not a finding of alteration.

### Ledger integrity and ID reconciliation

| Item | Finding | Disposition |
|---|---|---|
| Canonical mapping | Canonical next ID was `P-345`. Local `P-345`–`P-371` map **one-to-one** onto canonical `P-345`–`P-371`. | Imported under their issued labels; no cascade renumbering. |
| Local label collision at `P-358` | The `P-371` log reports that an earlier external artifact issued **"P-358" as an administrative no-forecast record for Fenerbahçe vs Roma** (UCL league phase MD1, start crossed). That artifact was **not supplied** and is not in this repository, `prediction logs/`, or the user's Downloads folder (searched 2026-09-11). | **Canonical `P-358` = Puerto Rico (W) vs China (W)** — the issued, fully documented card with which `P-359`–`P-371` are contiguous. The mini-log's alias **`TMP-CANON-20260911-01` → canonical `P-358`**, retired on import. The Fenerbahçe–Roma record takes the repository's collision namespace **`TMP-SETTLED-20260911-01`** — the **first use** of that namespace (`EXTERNAL_LOGGING_WORKFLOW.md`). Final verified at the field owner: **Fenerbahçe 1–1 Roma** (UEFA `matchstats` FAME feed, match `2049568`: goals 1/1, corners 3/1; scorers per ESPN/VAVEL: Cristante 39', Archie Brown 48'). No forecast was issued, so it is non-scorable; it takes the next free canonical ID only if its text is ever supplied. |
| 24-hour reconciliation rule (`METHOD.md` §10) | The `P-345`–`P-357` settled log was on disk from 2026-09-10 17:37 AEST; it is reconciled here at ~2026-09-11 23:50 AEST — **about 30 hours: outside the 24-hour window.** A 2026-09-10 edit to this file added one sentence referring to "the table below" for `P-345-C03`/`P-346-C05`/`P-355-C05` and never added the table — a dangling reference, corrected in the historical queue section below. The external session meanwhile issued `P-358`–`P-371` against its Drive copy. | **Ledger-integrity finding** — the second after `P-306`–`P-317`. No card is invalidated (every card was frozen before its event), but the window breach is exactly the risk §10 exists to prevent. Remedy in `EXTERNAL_LOGGING_WORKFLOW.md` §"2026-09-11". |
| Control currency on issue | `G-L1`/`G-L2`/`G-L7`/`G-L8` and baseball controls 24–25 / basketball 20–21 were adopted in this repository between **16:41 and 16:55 AEST on 2026-09-09** (file modification times). `P-345`–`P-351` were issued **before** that (02:25–12:10 AEST) and are **not graded against those controls**. `P-352`–`P-357` were issued after the local adoption, but whether the external session's Drive copy carried them cannot be verified from the supplied files. The `P-358` log's own header says the 2026-09-09 controls were "incorporated as active process constraints" — it lists `G-L7`, `G-L8`, `G-L2` and `G14.2`, **but not `G-L1`** — so `P-358`–`P-371` **are** graded against them. | See §"Control-execution audit" below. |

### Live-state check — the first required step

| Event | State at this pass (~23:30–23:50 AEST, 2026-09-11) | Source | Action |
|---|---|---|---|
| `P-364` England v Pakistan, 3rd Test, Edgbaston | **LIVE — Day 3, Session 2: Pakistan 206/3 (46.4 ov), trail by 114** (Masood 92*, Babar 34*) | ESPNcricinfo live page via `r.jina.ai` (direct fetch HTTP 403) | Potential-winner row **stays open** → `TMP-OPEN-20260911-03`. Its four ranked rows were already settled from the completed England first innings. Scheduled through 2026-09-13 BST. |
| `P-366` Rotterdam v Glasgow, ETPL Match 19 | **FINAL** (rain-reduced to 19 overs a side) | ETPL first-party page now reads **COMPLETED** (no scores in the rendered text; it read "Yet to bat" as late as the external pass at 23:12 AEST); scores from CricketEurope / Cricket Ireland-branded archive / Cricbuzz / CricketWorld | 6-over rows graded; the two 20-over rows are **terminal censored** (below). |
| Every other `P-345`–`P-371` event | **FINAL** | re-verification table below | settled |

### Independent re-verification of finals (outside the mini-logs' own registers where possible)

| Card(s) | Final confirmed | Route used this pass | Grade |
|---|---|---|---|
| `P-345` | Aston Villa 3–2 Club Brugge (Brugge 14 attempts / 7 on target, 4 corners; Villa 21 / 8, 5 corners) | `matchstats.uefa.com/v1/team-statistics/2049556` — UEFA, FAME provider; raw JSON via `curl` | FIELD OWNER |
| `P-346` | AEK Athens 1–0 LASK (AEK 17 / 3, 7 corners; LASK 11 / 3, 3 corners) | `matchstats.uefa.com/v1/team-statistics/2049558` | FIELD OWNER |
| `P-347`, `P-348`, `P-349`, `P-351` | TEX 10–5 SEA; TOR 4–2 ATH; SF 2–1 STL; LAD 3–2 CIN — all 9 innings, Final | `statsapi.mlb.com/api/v1/schedule?sportId=1&date=2026-09-08` via `curl` (WebFetch → HTTP 406) | FIELD OWNER |
| `P-352` | SA 348/6; Namibia 162/8 (31 ov); SA won by 99 runs (DLS) | ESPNcricinfo match page title | SNIPPET (field owner's page) |
| `P-355` | Melbourne Victory 2–0 Sydney FC (HT 1–0 Victory); corners 5–4 | FotMob match page via `r.jina.ai` (Opta data) | STRUCTURED SECONDARY — the card's own pre-registered corner provider |
| `P-356` | KT 2–0 Samsung (KT 2 in the 6th; W Ko Young-pyo, S Park Yeong-hyun, L Won Tae-in) | `eng.koreabaseball.com` scoreboard, 2026-09-09 | FIELD OWNER |
| `P-357` | Belfast 107 (19.4); Dublin 111/2 (14.3); Dublin by 8 wickets; both XIs and all bowling figures | Cricket Ireland-branded CricketArchive scorecard `1458971` | FIELD-OWNER LINEAGE |
| `P-358` | China 75–72 Puerto Rico, no OT (PR 3P 38.9%, FT 90%; Trinity San Antonio 35) | FIBA game page `128147-PUR-CHN` | FIELD OWNER |
| `P-362` | SSG 4–3 Hanwha (Hanwha 2 in the 7th; W Ávila, S Jo Byeong-hyeon, L Park Jun-yeong) | `eng.koreabaseball.com` scoreboard, 2026-09-10 | FIELD OWNER |
| `P-366` | Rotterdam 172/4 (19) bt Glasgow 141/9 (19) by 31 | ETPL page (now COMPLETED) + the external pass's concordant structured scorecards | FIELD OWNER (status) + structured |
| `P-367` | France 90–61 China (France led every quarter) | FIBA game page `128149-CHN-FRA` | FIELD OWNER |
| `P-368`, `P-369` | Al Jazira 1–1 Al Nasr (HT 1–0); United 1–1 Shabab Al Ahli (HT 0–0) | FotMob via `r.jina.ai`; The Sports Encounter / Flashscore corroboration | STRUCTURED SECONDARY |
| `P-371` | Germany 93–74 Belgium (Germany won each quarter; five lead changes, not wire-to-wire) | FIBA game page `128150-BEL-GER` | FIELD OWNER |
| `P-350`, `P-353`, `P-354`, `P-359`, `P-360`, `P-361`, `P-363`, `P-364` (1st innings), `P-365` | as settled by the external pass | **not re-fetched this pass** — the external pass cited the field owner (US Open official; NPB BIS ×3; CPBL Advanced Stats; PCB + Guardian over-by-over) or named national reporting (Petra; Yonhap; NRL live blog) | carried; no conflict found |

**17 of 26 issued-card finals independently re-verified; all 17 agree with the external settlement. No settled result is changed.**

### Derivative rows — resolved at their frozen field owners this pass

| Row | Frozen contract / owner | Field-owner reading | Result | Brier | Tracking handle |
|---|---|---|---|---:|---|
| `P-345-C03` (Rank #3) | Club Brugge Over 3.5 team corners — UEFA official match statistics | UEFA FAME `corners`: **Brugge 4**, Villa 5 | **WIN** (+0.5) | 0.1600 | `TMP-OPEN-20260910-01` **retired**. The conflict (Guardian 4 vs VI 3) is resolved in the Guardian's favour; **VI's count was wrong by one**. |
| `P-346-C05` (Rank #5) | Total corners Over 7.5 — UEFA official match statistics | **AEK 7 + LASK 3 = 10** | **WIN** (+2.5) | 0.1600 | `TMP-OPEN-20260910-02` **retired**. The Guardian had reported 7–4 = 11 — **its LASK count was wrong by one**. |
| `P-355-C05` (Rank #5) | Total corners Over 8.5, regulation — Opta/FotMob definition | FotMob: **Sydney 5 + Victory 4 = 9** | **WIN** (+0.5) | 0.1089 | `TMP-OPEN-20260910-03` **retired**. |
| `P-368-C02` (Rank #2) | Total corners Over 7.5 — **no provider frozen** (`UNKNOWN_DEFINITION`) | FotMob **6–3 = 9**, agreeing with Forebet and M9Bet (multiple secondary displays; independence unverified). UEFA-style field owner not found: the UAE Pro League match centre shows corners as "–". | **PROVISIONAL RESEARCH WIN** — not booked | (0.2025 if accepted) | **`TMP-OPEN-20260911-01`** |
| `P-369-C01` (Rank #1) | Total corners Under 10.5 — no provider frozen | FotMob **5–6 = 11** (multiple secondary displays; independence unverified) | **PROVISIONAL RESEARCH LOSS** (−0.5) — not booked | (0.4624 if accepted) | **`TMP-OPEN-20260911-02`** |
| `P-366-C02/C03` | Rotterdam 20-over O/U 166.5 | Rain reduced the innings to **19 overs** (172/4). The 20-over endpoint was never reached; the card made both probabilities conditional on a full 20-over innings. | **TERMINAL — CENSORED** (`RULES_CRICKET.md` control 15: incomplete is not zero). No W/L, no Brier. `OPERATOR_ACTION = UNKNOWN_DEFINITION`. **172@19 is not remapped into an Over-166.5 win.** | — | none — nothing retrievable can change it (same treatment as Part-2 items D/H/I/M) |
| `P-364` potential winner | England to win the Test | Match **LIVE** (above) | pending | — | **`TMP-OPEN-20260911-03`** — retry on the official Test final |

The three frozen-owner corner rows enter the scorecard now. **All three were `WIN`s, two by exactly half a corner** (another pair of entries for the distance-to-line watch).

### Settlement summary — all records in this import

`R#` columns give each ranked row's result (W/L; **P** = provisional; **C** = censored). Brier is the card mean over graded rows (half-up rounding).

| ID | Event | Sport · population | Final | R1 | R2 | R3 | R4 | R5 | Winner call | Card Brier (rows) |
|---|---|---|---|:--:|:--:|:--:|:--:|:--:|---|---|
| `P-345` | Club Brugge v Aston Villa | Soccer UCL · EXPL | Villa 3–2 (HT 1–3) | L | W | W | W | L | Brugge 44% — **L** | 0.2466 (5) |
| `P-346` | AEK Athens v LASK | Soccer UCL · EXPL | AEK 1–0 | W | W | W | W | W | AEK 53% — **W** | 0.0816 (5) |
| `P-347` | Rangers @ Mariners | **MLB · PRIMARY** | TEX 10–5 | W | L | W | L | — | TEX 55% — **W** | 0.2374 (4) |
| `P-348` | Blue Jays @ Athletics | **MLB · PRIMARY** | TOR 4–2 | W | L | L | L | — | TOR 60% — **W** | 0.2803 (4) |
| `P-349` | Cardinals @ Giants | **MLB · PRIMARY** | SF 2–1 | W | W | W | W | — | STL 52% — **L** | 0.1440 (4) |
| `P-350` | Shelton v Alcaraz, US Open QF | Tennis · EXPL | Shelton in 5 (49 games) | L | W | W | W | — | Alcaraz (= R1) — **L** | 0.2574 (4) |
| `P-351` | Reds @ Dodgers | **MLB · PRIMARY** | LAD 3–2 | W | W | L | L | — | LAD 72% — **W** | 0.2460 (4) |
| `P-352` | Namibia v South Africa, 1st ODI | Cricket · EXPL | SA 348/6; won by 99 (DLS) | L | W | W | W | — | SA 67% — **W** | 0.2158 (4) |
| `P-353` | Dragons @ Giants (9 Sep) | NPB · EXPL | YOM 5–1 | W | L | W | L | — | CHU 51% — **L** | 0.2549 (4) |
| `P-354` | Carp @ Tigers | NPB · EXPL | HIR 3–1 | W | L | L | W | — | HAN 63% — **L** | 0.2968 (4) |
| `P-355` | Sydney FC v Melbourne Victory, Aus Cup SF | Soccer · EXPL | Victory 2–0 (HT 0–1) | W | W | L | W | W | Sydney (reg.) 42% — **L** | 0.1531 (5) |
| `P-356` | KT @ Samsung | KBO · EXPL | KT 2–0 | L | W | W | W | — | Samsung 58% — **L** | 0.2418 (4) |
| `P-357` | Dublin v Belfast, ETPL M18 | Cricket · EXPL | Dublin by 8 wkts (BEL 107) | L | L | W | W | — | Belfast 68% — **L** | 0.3377 (4) |
| `P-358` | Puerto Rico W v China W, FIBA WWC | Basketball · EXPL | CHN 75–72 | L | W | L | W | — | China 73% — **W** | 0.2973 (4) |
| `P-359` | Jordan v Chinese Taipei, Asian Games | Basketball · EXPL | TPE 83–80 | W | L | W | L | — | Jordan ~60% — **L** | 0.2467 (4) |
| `P-360` | South Korea v Saudi Arabia, Asian Games | Basketball · EXPL | KOR 82–66 | W | L | W | L | — | Korea ~76% — **W** | 0.2409 (4) |
| `P-361` | Dragons @ Giants (10 Sep) | NPB · EXPL | YOM 5–3 | W | L | W | L | — | YOM ~58% — **W** | 0.2493 (4) |
| `P-362` | Eagles @ Landers | KBO · EXPL | SSG 4–3 | W | L | W | L | — | SSG ~67% — **W** | 0.2450 (4) |
| `P-363` | Roosters W v Bulldogs W, NRLW R11 | Rugby league · EXPL | ROO 42–12 | W | W | L | L | — | Roosters ~97% — **W** | 0.1773 (4) |
| `P-364` | England v Pakistan, 3rd Test (Day-2 card) | Cricket · EXPL | ENG 453 (1st inns); **match LIVE** | L | L | W | W | — | England ~91% — **pending** | 0.3429 (4) |
| `P-365` | Uni-Lions @ CTBC Brothers | CPBL · EXPL | UNI 6–0 | L | W | L | W | — | Uni-Lions ~59% — **W** | 0.2768 (4) |
| `P-366` | Rotterdam v Glasgow, ETPL M19 | Cricket · EXPL | ROT by 31 (19-over match) | W | C | C | L | — | Rotterdam ~62% — **W** | 0.1936 (2) |
| `P-367` | China W v France W, FIBA WWC QF | Basketball · EXPL | FRA 90–61 | W | W | L | L | — | France ~94% — **W** | 0.2071 (4) |
| `P-368` | Al Jazira v Al Nasr | Soccer UAE · EXPL | 1–1 (HT 1–0) | W | P(W) | L | W | L | Al Jazira ~65% — **L** (draw) | 0.1917 (4) |
| `P-369` | Dubai United v Shabab Al Ahli | Soccer UAE · EXPL | 1–1 (HT 0–0) | P(L) | L | L | W | W | Shabab ~60% — **L** (draw) | 0.3909 (4) |
| `P-370` | Jamaica Empress W v TKR W, WCPL | Cricket · — | — | — | — | — | — | — | none issued | **ADMIN CLOSED / NO FORECAST** |
| `P-371` | Belgium W v Germany W, FIBA WWC QF | Basketball · EXPL | GER 93–74 | L | L | W | W | — | Belgium ~74% — **L** | 0.3145 (4) |
| `TMP-SETTLED-20260911-01` | Fenerbahçe v Roma (UCL) — unsupplied no-forecast record | Soccer · — | 1–1 | — | — | — | — | — | none issued | **ADMIN / NON-SCORABLE** |

**Arithmetic reconciliation with the external passes.** Every per-card mean above equals the external pass's figure except (a) `P-345` (0.2683 → **0.2466**), `P-346` (0.0620 → **0.0816**) and `P-355` (0.1641 → **0.1531**), which change only because their frozen-owner corner rows are graded now; and (b) `P-364`, where the external pass printed 0.3428 for an exact mean of 0.34285 (rounding convention only; half-up used here).


### Per-card settlement blocks — `P-345`–`P-357` (schema: `# Settlement / retrospective schema` at the top of this file)

Each block answers, in order: the settlement table; the potential winner; **the three validation questions** the user set for every game — (Q1) were confirmed starting lineups and benches, plus coaching information, retrieved for both teams? (Q2) were the sources accurate, or are newer/better ones needed? (Q3) what were the pre-game blind spots and how are they accounted for next time? — then the `METHOD.md` §7.2 three-question retrospective, and the deep Rank-#1 table wherever Rank #1 lost. "Issued" is the external session's freeze time (AEST).

#### P-345 — Settlement

**Event:** Club Brugge v Aston Villa — UEFA Champions League 2026/27 league phase MD1, Jan Breydelstadion · **Official final:** Aston Villa 3–2 (HT 3–1 Villa; McGinn 11', Vetlesen 19', Buendía 22', Jackson 43', Tresoldi 61' pen) · **Field-owning source:** UEFA `matchstats` FAME (2049556); Opta Analyst · **Settled:** 2026-09-11 · **Method on card:** MDS-2026.09.06-v4.0 · **Population:** EXPLORATORY · **Issued:** 2026-09-09 02:25 (pregame; before the 2026-09-09 controls existed)

| Rank | Contract | Frozen terms | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---|---:|---|---:|---|
| 1 | Club Brugge +0.5 / double chance 1X | 90 min + stoppage | 0.71 | **LOSS** | 0.5041 | Villa won by one. **Positively coupled with R5** — both needed Villa's attack to stay quiet. |
| 2 | Club Brugge team total Over 0.5 | 90 min | 0.70 | **WIN** | 0.0900 | Brugge scored 2. |
| 3 | Club Brugge Over 3.5 team corners | UEFA official stats | 0.60 | **WIN** (settled this pass) | 0.1600 | UEFA FAME 4 — **+0.5**; VI's 3 was wrong |
| 4 | 1st-half Over 0.5 goals | first 45 + stoppage | 0.58 | **WIN** | 0.1764 | Four first-half goals. |
| 5 | Under 2.5 goals | 90 min | 0.55 | **LOSS** | 0.3025 | Five goals (−2.5). |

**Potential winner:** Club Brugge 44% (3-way; Villa 29%, draw 27%) · **Result:** **WRONG** · **Card mean Brier:** 0.2466 (5 rows) vs 0.2500 baseline.

- **Q1 — lineups/bench/coaching:** **Complete.** Confirmed XIs and full matchday benches for both sides (UEFA line-ups + Guardian team sheets), both head coaches (Ivan Leko, Unai Emery), named absences (Ordóñez, Manzambi, Cash). The best participant handshake in the batch.
- **Q2 — sources:** Accurate. The one conflict (Brugge corners: Guardian 4, VI 3) is now resolved at the field owner in the Guardian's favour. **New field-owner lane found for this whole competition family:** `matchstats.uefa.com/v1/team-statistics/{matchId}` (keyless JSON, both teams, corners/attempts/possession).
- **Q3 — blind spots → fix:** (a) Villa's three-match domestic drought (26 shots, **1 on target**) was converted into a **signed −0.20** attacking adjustment immediately after a rebuild. `RULES_SOCCER.md` control 23 already says that through the first two or three matches such droughts are unstable and go to **width**. Villa produced 21 attempts, 8 on target and ~3.00 xG (Opta). (b) **No cross-league strength anchor.** Brugge's Belgian volume (84 shots in five league games) was projected onto the Europa League holders, and the 2024/25 R16 tie (Villa 3–1, 3–0) was reduced to "descriptive". → New soccer control 31 (record the cross-competition translation explicitly). (c) The complement of the 71% Rank #1 — a Villa win — was left at 29% with no itemisation against the named Villa kill paths. → `G-L9` complement decomposition.

**Three-question retrospective.** 1. *Driver:* Villa's rebuilt attack produced a genuine first-half burst (three goals by 43'), not a finishing fluke. 2. *Knowable?* **Partly — yes.** The card named Gomes's return, Jackson's central threat, the deep Villa bench, and the tiny drought sample; it still signed the drought negative. 3. *Smallest change:* apply control 23 literally — an early-season shot-on-target drought with shot volume intact is width, not direction.

| Deep Rank-#1 question | Finding |
|---|---|
| What went right? | Brugge scored twice (R2), four first-half goals (R4) and Brugge won 4 corners (R3). The attacking half of the Brugge thesis was right. |
| What went wrong? | The non-loss (R1) and the Under (R5) both rested on Villa's domestic drought persisting. Both lost together. |
| Actual mechanism | Villa's 21 attempts and 3.00 xG; three goals in 32 minutes; Brugge's high line was exposed. |
| Improvement | Control 23 (drought → width); control 31 (cross-league translation, new); `G-L9` (itemise the 29% complement); `G-L10` (flag R1/R5 as positively coupled on one Villa-attack branch). |
| Grade (background) | C+ — issued before the 2026-09-09 controls existed; failure is of an older soccer control (23). |

##### 2026-09-12 retrospective correction

| What went right | Error / uncertainty | Routine change and evidence |
|---|---|---|
| Brugge team scoring, first-half Over and the now owner-confirmed corner row won | Inherited final Villa 3-2, including three first-half goals, defeated Brugge +0.5 and full Under. A three-match domestic shot-on-target drought was used too confidently against a changed attack. A burst of goals alone does not establish that it was not finishing variance | Retrieve shots by quality/opponent and current personnel; show uncertainty and Villa-win/separation branches. Revisit soccer control 23, G-L7 and cross-competition translation. Do not automatically erase a directional effect solely because it is small-sample |

#### P-346 — Settlement

**Event:** AEK Athens v LASK — UCL league phase MD1, OPAP Arena · **Official final:** AEK 1–0 (HT 1–0; Marin 21' free kick) · **Field-owning source:** UEFA `matchstats` FAME (2049558) · **Settled:** 2026-09-11 · **Population:** EXPLORATORY · **Issued:** 2026-09-09 02:38

| Rank | Contract | Frozen terms | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---|---:|---|---:|---|
| 1 | AEK +0.5 / 1X | 90 min | 0.79 | **WIN** | 0.0441 | AEK won. |
| 2 | AEK team total Over 0.5 | 90 min | 0.78 | **WIN** | 0.0484 | 1 goal (+0.5). |
| 3 | Under 4.5 goals | 90 min | 0.77 | **WIN** | 0.0529 | 1 goal (+3.5). |
| 4 | 1st-half Over 0.5 | | 0.68 | **WIN** | 0.1024 | 21' goal. |
| 5 | Total corners Over 7.5 | UEFA official stats | 0.60 | **WIN** (settled this pass) | 0.1600 | UEFA 7 + 3 = **10** (+2.5); Guardian's 11 was wrong by one |

**Potential winner:** AEK 53% · **Result:** **CORRECT** · **Card mean Brier:** **0.0816** — best card of the import. *(Supplied but unranked: full-match Over 2.5 preferred at 0.58 — LOST, one goal.)*

- **Q1:** Confirmed XIs (UEFA) and both coaches (Marko Nikolić, Dietmar Kühbauer); late goalkeeper change (Strakosha out, Brignoli in) captured. **Benches `SECONDARY_ONLY`** — adequate for `G14.2` (retrieved, but not from the field owner).
- **Q2:** Accurate for every settled field. The Guardian's corner count disagreed with UEFA's own feed by one.
- **Q3:** The supplied full-match Over 2.5 was preferred at 0.58 on a 3.03-goal centre. LASK's inputs were Austrian league/cup scoring (62 GF in L20); a −0.40 translation was applied, but the centre still sat above the line. The ranked rows were robust precisely because they did not need the goal count — this is the **positive** pattern of the batch: large-edge alternate lines and protected sides. → control 31.

**Three-question retrospective.** 1. *Driver:* one set-piece conversion plus AEK's territorial control. 2. *Knowable?* **Yes** — the set-piece/early-goal branch, AEK's home process and the Adeniran-less LASK attack were all on the card. 3. *Smallest change:* none for the ranked rows; for the supplied full-match total, record the cross-league translation (control 31).

#### P-347 — Settlement

**Event:** Texas Rangers (Quantrill) @ Seattle Mariners (Miller), T-Mobile Park · **Official final:** TEX 10–5 (Miller 3.2 IP / 4 ER; Texas five-run 5th; Quantrill 6.0 IP / 3 ER) · **Source:** MLB statsapi (gamePk 823092) · **Population:** **MLB PRIMARY_SCORED** · **Issued:** 2026-09-09 11:26

| Rank | Contract | Frozen terms | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---|---:|---|---:|---|
| 1 | Rangers +1.5 | full game | 0.76 | **WIN** | 0.0576 | TEX won by 5. |
| 2 | Mariners team total Under 4.5 | | 0.71 | **LOSS** | 0.5041 | SEA scored 5 — **missed by 0.5**. |
| 3 | Rangers team total Over 2.5 | | 0.69 | **WIN** | 0.0961 | TEX 10. |
| 4 | Under 7.5 | | 0.54 | **LOSS** | 0.2916 | 15 runs. Card centre 7.60 was *above* the line; Under chosen on skew, not shown numerically. |

**Potential winner:** Texas 55% · **CORRECT** · **Card mean Brier:** 0.2374.

- **Q1:** Starters official (MLB probables); batting orders **`SECONDARY_ONLY`** (MLB page not refreshed); bullpens named; **managers not named.** Partial.
- **Q2:** Accurate. The MLB lineup page lagged at the freeze. → Test route for the next MLB card: the statsapi live feed `battingOrder` field, which is the field owner if populated before first pitch (to be verified prospectively; not yet demonstrated).
- **Q3:** Miller's short-hook / walk / HR-cluster tail was **printed as the principal kill path**, yet Seattle's team total Under was 71%. Quantrill's 2.79 ERA against a 3.96 FIP signalled regression — i.e. a Seattle scoring tail. → `G-L9`: 29% of complement mass cannot cover a hook branch *plus* a Quantrill-regression branch *plus* bullpen/sequencing.

**Three-question retrospective.** 1. *Driver:* Miller's early exit and a failed first relief transition (TEX five-run 5th); Seattle's 3-run homer took it to five. 2. *Knowable?* **Yes, in the card.** 3. *Smallest change:* itemise the complement of every row above 0.65 across its named kill paths (`G-L9`).

#### P-348 — Settlement

**Event:** Toronto Blue Jays (Soriano) @ Athletics (Perkins), Sutter Health Park · **Official final:** TOR 4–2 (Soriano 7.0 IP / 2 ER; Perkins 5.0 IP / 4 ER) · **Source:** MLB statsapi (824957) · **Population:** **MLB PRIMARY_SCORED** · **Issued:** 2026-09-09 11:32

| Rank | Contract | Frozen terms | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---|---:|---|---:|---|
| 1 | Blue Jays team total Over 3.5 | | 0.73 | **WIN** | 0.0729 | Exactly 4 — **+0.5**. |
| 2 | Athletics team total Over 3.5 | | 0.62 | **LOSS** | 0.3844 | ATH 2. |
| 3 | Athletics +1.5 | | 0.61 | **LOSS** | 0.3721 | Lost by 2 — **−0.5**. |
| 4 | Over 9.0 (integer; 54% win / 10% push / 36% loss) | | 0.54 | **LOSS** | 0.2916 | 6 runs. |

**Potential winner:** Toronto 60% · **CORRECT** · **Card mean Brier:** 0.2803. Supplied Toronto −1.5 (39%) and Under 9.0 both won.

- **Q1:** Starters official; batting orders `SECONDARY_ONLY` (MLB "TBD"; team post quoted); Springer's absence noted without inventing a diagnosis; managers not named. Partial.
- **Q2:** Accurate. Baseball Savant 2026 park factors were correctly retrieved — the problem was their use (below), not their accuracy.
- **Q3:** **Mechanism overlap.** The centre was built as 8.42 prior **+0.60 park +0.30 heat +0.45 Perkins +0.20 Athletics form +0.10 bullpen fragility −0.20 Springer = 9.87**. Park run factor, same-park recent scoring and hot-weather carry are largely the *same* causal channel (the ball carries in Sutter), so three increments counted one mechanism up to three times. Soriano's established-skill branch (7.0 IP / 2 ER) got no mass against a "less dominant since the trade" narrative. → New baseball **control 26** (mechanism-overlap audit).

**Three-question retrospective.** 1. *Driver:* Soriano suppressed Oakland for seven innings; Toronto scored exactly four. 2. *Knowable?* **Partly** — the stacking was visible in the card's own arithmetic. 3. *Smallest change:* a same-channel adjustment may take full weight once, not once per restatement (control 26).

#### P-349 — Settlement

**Event:** St. Louis Cardinals (Mathews) @ San Francisco Giants (Roupp), Oracle Park · **Official final:** SF 2–1 (Roupp 6.0 scoreless; Mathews 6.0 IP / 2 ER; STL scored in the 9th) · **Source:** MLB statsapi (823174) · **Population:** **MLB PRIMARY_SCORED** · **Issued:** 2026-09-09 11:42

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Giants +1.5 | 0.68 | **WIN** | 0.1024 | SF won. |
| 2 | Giants team total Under 4.5 | 0.66 | **WIN** | 0.1156 | SF 2. |
| 3 | Cardinals team total Under 4.5 | 0.63 | **WIN** | 0.1369 | STL 1. |
| 4 | Under 7.5 | 0.53 | **WIN** | 0.2209 | 3 runs. Centre 7.70 (mean) sat above 7.5; Under chosen on skew — right here, but not shown as a median. |

**Potential winner:** St. Louis 52% · **WRONG** (a coin-flip label) · **Card mean Brier:** 0.1440 — **all four rows won.**

- **Q1:** Starters official; batting orders "TBD" / secondary mixture; injuries/transactions current (Winn activated; Adames, Chapman out); managers not named. Partial.
- **Q2:** Accurate (Baseball Savant xERA, MLB transactions).
- **Q3:** None material. The one improvement is presentational: for right-skewed run totals, locate the line against the **median of the run-family table**, not the mean (`G-L8` clarification, `RULES_GENERAL.md` §16.5(d)).

**Three-question retrospective.** 1. *Driver:* both starters controlled run scoring (Oracle suppression, Roupp's contact quality). 2. *Knowable?* **Yes, and used.** 3. *Smallest change:* none — keep "protected side + team-total Unders anchored on the stronger starters" as the model pattern for a low-total game.

#### P-350 — Settlement

**Event:** Ben Shelton v Carlos Alcaraz — US Open men's QF, Arthur Ashe, best-of-five · **Official final:** Shelton 6-7(5), 6-1, 6-3, 1-6, 7-6(7) in 4h28; 49 games; aggregate games Shelton 26–23; breaks converted 5–3 · **Source:** US Open official report (external pass; not re-fetched) · **Population:** EXPLORATORY · **Issued:** 2026-09-09 11:49

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Alcaraz match winner | 0.76 | **LOSS** | 0.5776 | Fifth-set tiebreak, 10–7 (score corrected 2026-09-12). Winner alias counted once (`L-014`). |
| 2 | Over 3.5 sets | 0.66 | **WIN** | 0.1156 | 5 sets. |
| 3 | Total games Over 38.5 | 0.60 | **WIN** | 0.1600 | 49 (+10.5). |
| 4 | Shelton +4.5 games | 0.58 | **WIN** | 0.1764 | Shelton +3 won outright. |

**Card mean Brier:** 0.2574.

- **Q1:** Not applicable in the team sense. Identity, fitness (Alcaraz's wrist return; no active limitation) and workload were verified; coaching staff not recorded (not decision-driving here).
- **Q2:** Accurate. **New independent benchmark tested this pass:** Tennis Abstract Elo, last updated **2026-08-31** (before the tournament): Alcaraz overall 2146.8 (#2) / hard 2073.3 (#2); Shelton overall 1977.5 (#7) / hard 1948.5 (#6).
- **Q3:** Converting those ratings to best-of-five with a constant set-win-probability model (my arithmetic, approximate): hard-court Elo → Alcaraz **≈71%**; overall Elo → **≈77%**; 50/50 blend → **≈74%**. **The card's 76% sits inside the independent benchmark's range.** The loss is therefore most plausibly an upset from within the model's own ~24% branch, not evidence of a mis-built tree. The one real blind spot is that a five-month wrist layoff should widen set-level outcomes (`G-L2`), and Elo does not see layoffs either. → New tennis controls 13 (print the Elo benchmark) and 14 (long-layoff width).

**Three-question retrospective.** 1. *Driver:* Shelton's serve held under pressure and his return created five breaks; he won the fifth-set tiebreak 10–7 (corrected 2026-09-12). 2. *Knowable?* The *extension* was known and weighted (66% four-plus sets; three subordinate rows won). The upset branch existed; its probability is not validated by this outcome or the Elo benchmark. 3. *Smallest change:* print an independent rating benchmark so a retrospective can separate variance from model error — and do not over-learn from one tiebreak.

| Deep Rank-#1 question | Finding |
|---|---|
| What went right? | One shared tree produced coherent derived rows: extension (66%), total games (60%), Shelton cushion (58%) — all won. `RULES_TENNIS.md` §4 / control 12 executed as designed. |
| What went wrong? | The winner row lost at 76%. An independent Elo benchmark says ~71–77%, so the probability was reasonable; the Shelton-win branch (24%) was not obviously too small. |
| Actual mechanism | Serve dominance plus timely returns; 7-6(7) in the fifth. |
| Improvement | Tennis control 13 (Elo benchmark beside every winner probability; a >10-point gap needs a named mechanism); control 14 (multi-month layoff → wider set outcomes); keep the tree. |
| Grade (background) | B — sound process; the outcome is consistent with variance. |

##### 2026-09-12 retrospective correction

| What went right | Error / uncertainty | Routine change and evidence |
|---|---|---|
| The issued extension, games Over and Shelton handicap all won; they describe a long match that actually occurred | Alcaraz winner lost. **The deciding tiebreak was 10-7, not 9-7.** Match games remain 49. Elo agreement does not demonstrate the 76% estimate was correct or separate variance from model error. Coaches were not captured on the issued card | Keep the upset/extension tree; examine return-from-layoff and opponent-adjusted serve/return sensitivity with pre-cutoff evidence. Benchmark only; no automatic layoff penalty. Tennis controls 13-14 and G-L9, corrected by section 16.9. [Tennis Australia report](https://ausopen.com/articles/news/i-feel-myself-becoming-more-complete-says-shelton-after-alcaraz-upset) |

#### P-351 — Settlement

**Event:** Cincinnati Reds (Lodolo) @ Los Angeles Dodgers (Skubal) · **Official final:** LAD 3–2 (Smith HR 1st; De La Cruz 2-run HR; T. Hernández go-ahead RBI 5th) · **Source:** MLB statsapi (823901) · **Population:** **MLB PRIMARY_SCORED** · **Issued:** 2026-09-09 12:07

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Reds team total Under 4.5 | 0.74 | **WIN** | 0.0676 | CIN 2. |
| 2 | Dodgers match winner | 0.72 | **WIN** | 0.0784 | by 1. |
| 3 | Dodgers team total Over 3.5 | 0.70 | **LOSS** | 0.4900 | LAD 3 — **−0.5**. **Positively coupled with R4.** |
| 4 | Dodgers −1.5 | 0.59 | **LOSS** | 0.3481 | Won by 1. |

**Potential winner:** Dodgers 72% · **CORRECT** · **Card mean Brier:** 0.2460. Supplied Reds +1.5 and Under 8.0 both won.

- **Q1:** Starters official; orders `SECONDARY_ONLY`; Ohtani not starting and Tucker absent both captured; managers not named. Partial.
- **Q2:** Accurate.
- **Q3:** Ohtani's absence entered as a **flat −0.40 runs**, leaving a 5.24-run Dodgers centre. An elite hitter's absence changes plate-appearance allocation, home-run probability and multi-run-inning frequency — the very branch R3 and R4 both depended on. → New baseball **control 27** (PA-weighted lineup exposure). `G-L10` would have shown R3 and R4 as one bet on one branch.

**Three-question retrospective.** 1. *Driver:* the pitching asymmetry was enough for the Dodgers to win and for the Reds to be held down, but not enough for a four-run Dodgers total or a two-run margin. 2. *Knowable?* **Yes** — the absence was on the card. 3. *Smallest change:* rebuild the lineup's PA/cluster state for a missing elite bat instead of subtracting a scalar.

#### P-352 — Settlement

**Event:** Namibia v South Africa, 1st ODI, Windhoek (Namibia won the toss and fielded) · **Official final:** SA 348/6 (50); Namibia 162/8 (31); SA won by 99 runs (DLS). First five overs: **SA 18/0** · **Source:** ESPNcricinfo; NDTV/myKhel/CricketWorld (external) · **Population:** EXPLORATORY · **Issued:** 2026-09-09 17:34 (after toss)

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | SA 1st innings Under 305.5 | 0.68 | **LOSS** | 0.4624 | 348 (+42.5 over the line). |
| 2 | South Africa match winner | 0.67 | **WIN** | 0.1089 | |
| 3 | SA 1st innings 250+ | 0.66 | **WIN** | 0.1156 | |
| 4 | SA first 5 overs Under 25.5 | 0.58 | **WIN** | 0.1764 | 18/0 — the phase won while keeping all ten wickets. |

**Card mean Brier:** 0.2158.

- **Q1:** **Confirmed XIs for both teams** (toss complete; exact-match pitch report observed); captains named; head coaches not named; no bench concept in ODI selection beyond reserves. Adequate.
- **Q2:** Accurate. **But a decisive, verifiable fact was retrieved and then set aside:** the same ground had produced T20I innings of **228/4 (SA v Namibia, 4 Sep), 217/3 (Namibia's reply) and 205/5 (SA v Zimbabwe final, 6 Sep)** that same week (ESPNcricinfo). The card said "T20 scoring is not transferred directly into ODI rates" and anchored on five April ODIs (highest 268/7).
- **Q3:** → New cricket **control 25**: same-venue, same-week cross-format scoring is *current-surface* evidence — translate it with a stated weight, do not dismiss it. Also existing controls 16/19: the full-innings distribution is conditioned on the **phase-end wickets**, and 18/0 is a very different resource state from 18/2.

**Three-question retrospective.** 1. *Driver:* a wicket-light new-ball phase, then Hermann (150) and de Zorzi (72) built on a surface that had just produced three 200+ T20 totals; the lower order took it to 348. 2. *Knowable?* **Yes** — the card's own pitch report said "plenty of runs once in", and the 305+ route (wicket-light first 15 overs) was named but not given mass. 3. *Smallest change:* weight the same-week surface evidence and condition the innings on phase-end wickets (controls 25, 16/19; `G-L9`).

| Deep Rank-#1 question | Finding |
|---|---|
| What went right? | Phase Under (R4), winner (R2) and 250+ (R3) all won; the new-ball read was correct. |
| What went wrong? | The innings centre (278 ±48) ignored three 200+ T20I innings on the same strip that week and treated a slow phase as low-scoring evidence regardless of wickets. |
| Actual mechanism | 18/0 preserved all resources; 150 + 72 partnership; late acceleration (Bosch 39*). |
| Improvement | Cricket control 25 (new); controls 16/19 enforced (phase-end wickets); `G-L9` (the 32% complement had to hold the wicket-light branch). |
| Grade (background) | C. |

##### 2026-09-12 retrospective correction

| What went right | Error / uncertainty | Routine change and evidence |
|---|---|---|
| Inherited five-over Under won at 18/0; SA winner and 250+ also won | SA reached 348/6, defeating Under 305.5. A low-run phase without wicket losses retained batting resources. Hermann 150 and de Zorzi 72 are individual innings, not an established 222-run partnership. Same-ground T20 totals do not prove the same physical strip or justify direct ODI transfer | Record wickets/resources with phase pace, exact strip evidence and conditional innings scenarios. Cross-format results are context pending comparability, not mandatory signed uplift. Cricket controls 16/19/25, G-L7 and G-L9 |

#### P-353 — Settlement

**Event:** Chunichi Dragons (Ohno) @ Yomiuri Giants (Mata), Tokyo Dome, 9 Sep · **Official final:** YOM 5–1 (Dalbec HR off Ohno) · **Source:** NPB BIS (external; not re-fetched) · **Population:** EXPLORATORY · **Issued:** 2026-09-09 18:47

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Chunichi team total Under 4.5 | 0.75 | **WIN** | 0.0625 | CHU 1. |
| 2 | Yomiuri team total Under 3.5 | 0.69 | **LOSS** | 0.4761 | YOM 5. |
| 3 | Under 6.5 | 0.62 | **WIN** | 0.1444 | 6 — centre 6.03, essentially exact. |
| 4 | Chunichi +0.5 | 0.58 | **LOSS** | 0.3364 | |

**Potential winner:** Chunichi 51% (tie 7%) · **WRONG** · **Card mean Brier:** 0.2549.

- **Q1:** **Complete** — posted lineups and benches for both sides (NPB / SportsNavi), both managers (Shinnosuke Abe, Kazuki Inoue), roster moves (Mata registered, Tima deregistered).
- **Q2:** Accurate.
- **Q3:** The platoon adjustment (−0.20 for "five of Yomiuri's first six hitters bat left-handed against LHP Ohno") was a **headcount**. The decisive plate appearance was the one **right-handed** middle-order bat, Dalbec (#3). → New baseball **control 27** (PA- and slot-weighted platoon exposure). *Note the recurrence:* the next day (`P-361`), against another left-hander, Dalbec homered again.

**Three-question retrospective.** 1. *Driver:* Yomiuri's productive PAs concentrated in Dalbec/Ohshiro/Maru; Mata plus the bullpen held Chunichi to one. 2. *Knowable?* **Yes, structurally.** The total was right; the split between the teams was wrong. 3. *Smallest change:* weight platoon exposure by slot, expected PA and power — not by a count of same-handed hitters.

##### 2026-09-12 evidence supplement

NPB re-fetch confirms Yomiuri 5-1 and Dalbec third-inning solo homer; exact handedness exposure merits review, but one homer does not prove a fitted platoon effect was wrong. See [opened sources and field limits](audit_2026-09-12/sport_evidence.md).

#### P-354 — Settlement

**Event:** Hiroshima Carp (Tokoda) @ Hanshin Tigers (H. Takahashi), Koshien — rain delay to 18:31 JST · **Official final:** HIR 3–1 (Tokoda 8.0 scoreless; Hanshin's only run a 9th-inning solo HR; Hiroshima's three runs all in the 7th) · **Source:** NPB BIS (external) · **Population:** EXPLORATORY · **Issued:** 2026-09-09 18:58

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Hiroshima team total Under 3.5 | 0.76 | **WIN** | 0.0576 | Exactly 3 — **+0.5**. |
| 2 | Hanshin team total Over 1.5 | 0.74 | **LOSS** | 0.5476 | HAN 1. **Positively coupled with R3.** |
| 3 | Hanshin match winner | 0.63 | **LOSS** | 0.3969 | |
| 4 | Hiroshima +1.5 | 0.57 | **WIN** | 0.1849 | |

**Card mean Brier:** 0.2968. Supplied Under 5.5 won.

- **Q1:** Posted lineups and benches for both sides; Hiroshima manager (Arai) and the Suzuki bullpen move captured; **Hanshin's manager not named.** Near-complete.
- **Q2:** Accurate (Koshien park factors; JMA alerts; the rain delay correctly treated as event-order variance, not an automatic Under).
- **Q3:** Tokoda's long-start branch was on the card (recent 8 IP / 1 R start; `−0.35` established-starter term) but carried **no mass** before a 74% Hanshin team-total Over and a 63% Hanshin win. → New baseball **control 28**: before any team-total Over or favourite win on the side facing an established starter, give that starter's "6+ innings, ≤1 run" branch explicit mass and cap the Over accordingly (`G-L9`).

**Three-question retrospective.** 1. *Driver:* Tokoda's length and control; one seventh-inning relief transition decided it. 2. *Knowable?* **Yes.** 3. *Smallest change:* control 28.

##### 2026-09-12 evidence supplement

NPB re-fetch confirms Tokoda eight scoreless and Hiroshima three runs in inning seven; the starter/reliever transition overlapped scoring, but the box alone does not establish managerial fault. See [opened sources and field limits](audit_2026-09-12/sport_evidence.md).

#### P-355 — Settlement

**Event:** Sydney FC v Melbourne Victory — Australia Cup semi-final, Jubilee Stadium · **Official final:** Victory 2–0 (HT 0–1; Jelacic 2', Courtney-Perkins OG 61'). FotMob: shots 9–12, **on target 0–3**, possession 76–24, corners 5–4, xG 1.05–0.76 · **Source:** FotMob (Opta) via proxy; Sydney FC and A-Leagues reports · **Population:** EXPLORATORY · **Issued:** 2026-09-09 19:15

| Rank | Contract | Frozen terms | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---|---:|---|---:|---|
| 1 | 1st-half Under 1.5 | | 0.82 | **WIN** | 0.0324 | One first-half goal. |
| 2 | Under 3.5 goals | regulation | 0.79 | **WIN** | 0.0441 | 2. |
| 3 | Sydney +0.5 / 1X | regulation | 0.70 | **LOSS** | 0.4900 | `FORCED RANK` (XI unresolved) — correctly capped. |
| 4 | Over 1.5 goals | regulation | 0.70 | **WIN** | 0.0900 | Exactly 2 — **+0.5**. |
| 5 | Total corners Over 8.5 | regulation, Opta/FotMob | 0.67 | **WIN** (settled this pass) | 0.1089 | 9 — **+0.5** |

**Potential winner (regulation):** Sydney 42% · **WRONG**; Sydney to advance 57% — WRONG · **Card mean Brier:** 0.1531.

- **Q1:** **Not complete.** Official XIs were not public by the freeze. The card quarantined a secondary lineup feed that listed a player absent from Victory's official 19-man squad — **a good catch that prevented a false handshake.** Both head coaches named (Kisnorbo, Savarese); bench-depth integer unresolved. The side row was capped `FORCED RANK`, exactly as designed.
- **Q2:** Accurate. The A-Leagues match-centre page does not render stats to the fetch tool; **FotMob via proxy does** and was the card's own pre-registered corner provider.
- **Q3:** Territory is not chance quality (soccer control 27): Sydney had 76% possession and **zero shots on target**. The card's goal-family mass (0–1 goals 30%, exactly 2 27%, 3 22%, 4+ 21%) is the model to copy — its three large-edge total rows all won.

**Three-question retrospective.** 1. *Driver:* a second-minute turnover goal, then Victory's block; Sydney's possession never became shots on target. 2. *Knowable?* **Partly** — Victory's regulation clean-sheet run was on the card; the second-minute error was not knowable. 3. *Smallest change:* none beyond control 27; keep the family table.

#### P-356 — Settlement

**Event:** KT Wiz (Ko Young-pyo) @ Samsung Lions (Won Tae-in), Daegu, 9 Sep · **Official final:** KT 2–0 (Ko 7.0 scoreless; Kim Hyun-soo 2-run HR in the 6th; Samsung four hits) · **Source:** KBO English scoreboard · **Population:** EXPLORATORY · **Issued:** 2026-09-09 19:26 (after the local 2026-09-09 controls; the card printed a final-state mass table and a normalised edge — partial execution)

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Samsung team total Over 3.5 | 0.70 | **LOSS** | 0.4900 | Samsung 0. |
| 2 | KT team total Under 5.5 | 0.66 | **WIN** | 0.1156 | KT 2. |
| 3 | KT +1.5 | 0.59 | **WIN** | 0.1681 | KT won. |
| 4 | Under 10.5 (normalised edge 0.12 printed) | 0.56 | **WIN** | 0.1936 | 2 runs. |

**Potential winner:** Samsung 58% · **WRONG** · **Card mean Brier:** 0.2418.

- **Q1:** Samsung's posted order reported; **KT's order unresolved**; bench and managers not recorded. Partial. (Rank #1 was a team total, so `G14.2`'s block did not formally bind.)
- **Q2:** Accurate — the KBO player pages and English scoreboard are the field owner.
- **Q3:** The card **did print Ko's per-start log** (5.1/3, 6/3, 7/1, 3/7) and his 3.05 second-half ERA over 41.1 IP. It then gave the single 3-inning / 7-run start a **+0.25** Samsung term, cancelling the −0.25 second-half term. One start's run total is not a rate: its sampling noise swamps the signal (`G-L11`, new). Three subordinate rows modelled a low-scoring KT-protected game while Rank #1 projected four-plus Samsung runs — a cross-row contradiction that `G-L10` would have printed.

**Three-question retrospective.** 1. *Driver:* Ko's command dominated; one homer decided a 2–0 game. 2. *Knowable?* **Yes — it was printed.** 3. *Smallest change:* one bad start widens the early-hook tail; it cannot offset a 41-inning current regime (`G-L11`; baseball control 28).

| Deep Rank-#1 question | Finding |
|---|---|
| What went right? | Rows 2–4 captured the low-scoring, KT-protected game; the normalised edge and final-state mass table were printed — the only baseball card in the batch to do both. |
| What went wrong? | Rank #1 projected 5.32 Samsung runs; one blow-up start was weighted equal to 41 innings; the Daegu/home-power terms were stacked on top. |
| Actual mechanism | Ko: 7 scoreless innings, command intact; Won also held KT to one swing. |
| Improvement | `G-L11` (sampling noise), control 28 (long-start branch mass), control 26 (stacking audit), `G-L10` (R1 contradicts R2–R4). |
| Grade (background) | C. |

##### 2026-09-12 retrospective correction

| What went right | Error / uncertainty | Routine change and evidence |
|---|---|---|
| The three lower rows captured KT protection and a low total; the original card printed more arithmetic than many peers | Inherited KT 2-0 and Ko's seven scoreless innings defeated Samsung Over 3.5. A single poor recent start and larger recent sample were given offsetting terms without a defensible uncertainty calculation. KT lineup/bench evidence was incomplete. Opposing winning rows are not automatically logically inconsistent unless their joint states make them so | Disaggregate opponent-adjusted starts, actual workload and walk/strikeout/contact evidence; show sensitivity to the outlier and ordinary long-start outcome. Baseball 24/26/28; corrected G-L11. Do not use a binomial formula for runs allowed |

#### P-357 — Settlement

**Event:** Dublin Guardians v Belfast Wolves — ETPL Match 18, Malahide · **Official final:** Belfast 107 all out (19.4), powerplay 43/3, fall of wickets 1-10, 2-29, 3-42, **4-62, 5-62, 6-62**, 7-78…10-107; Dublin 111/2 (14.3); Dublin by 8 wickets. Dublin bowling: Young 4-0-21-5, Willey 4-0-24-2, Hollard 3.4-0-26-2, Little 4-0-22-1, Ashwin 4-0-13-0 · **Source:** Cricket Ireland-branded CricketArchive `1458971` (re-opened this pass) · **Population:** EXPLORATORY · **Issued:** 2026-09-09 23:10 (**toss already complete**)

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Belfast 1st innings 150+ | 0.72 | **LOSS** | 0.5184 | 107. **Anti-coupled with R3** — a slow powerplay *with wickets* is bad news for the innings total. |
| 2 | Belfast match winner | 0.68 | **LOSS** | 0.4624 | |
| 3 | Belfast first 6 overs Under 52.5 | 0.58 | **WIN** | 0.1764 | 43/3. |
| 4 | Belfast innings Under 177.5 (normalised edge 0.19 printed) | 0.56 | **WIN** | 0.1936 | |

**Card mean Brier:** 0.3377.

- **Q1:** **No — and this was a retrieval miss, not an availability gap.** The toss was complete at the freeze, and under MCC Law 1.2 (and every competition's playing conditions) the XIs are nominated **before the toss**. They existed. Dublin: Vince, Willey, Tector, Mitchell, Krishnamurthi, Calitz, Dockrell, Ashwin, Little, Hollard, Young. Belfast: Stirling, Conway, Chapman, Tucker, Manenti, Miller, Maxwell, Adair, Klaassen, Humphreys, Netravalkar. Coaches not named.
- **Q2:** Accurate. The ETPL first-party page is a stale shell for post-match status; CricketArchive (Cricket Ireland) carries full scorecards.
- **Q3:** Belfast 150+ at 72% and a Belfast win at 68% leaned on Dublin's 0–5 record and −1.65 NRR, while the attack actually selected held **five international-level bowlers**. The collapse branch (control 3) — here a **triple-wicket cluster at 62** — had no mass. → New cricket **control 26** (post-toss XI retrieval); control 3 with mass; `G-L9`.

**Three-question retrospective.** 1. *Driver:* Craig Young 5-21 and a three-wicket cluster at 62 destroyed the resource base. 2. *Knowable?* **The XI was knowable (post-toss) but not retrieved**; the attack's strength followed directly from it. 3. *Smallest change:* after a toss, fetch the XIs from the toss commentary before freezing, or record `RETRIEVAL_MISS` and cap.

| Deep Rank-#1 question | Finding |
|---|---|
| What went right? | Both Unders (R3, R4) won on the new-ball / Malahide reading. |
| What went wrong? | The Belfast scoring and winner thesis relied on team record rather than the XI actually selected, which was retrievable. |
| Actual mechanism | 43/3 in the powerplay → 62/6 → 107. |
| Improvement | Cricket control 26 (new), control 3 collapse branch with mass, `G-L9`, `G-L10` (R1 and R3 are anti-coupled). |
| Grade (background) | C−. |

##### 2026-09-12 retrospective correction

| What went right | Error / uncertainty | Routine change and evidence |
|---|---|---|
| Inherited 43/3 phase Under and innings Under won | Belfast 150+ and winner failed at 107, with three wickets falling at 62. Current XIs were not captured. A completed toss establishes nomination, not publicly accessible publication before the cutoff; the earlier certainty that this was a retrievable-publication miss was unsupported | Search exact toss/team-sheet routes, save publication time, and record unavailable versus not retrieved honestly. Model the selected attack and collapse state jointly with innings exposure. Cricket 3/26, G14.2 and G-L9; the five-wicket haul itself was not knowable |

### Per-card settlement blocks — `P-358`–`P-371`

All thirteen issued cards in this block were frozen after the external session had itself declared `G-L7`, `G-L8`, `G-L2` and `G14.2` "incorporated as active process constraints". **None printed a numeric total width, a normalised edge or an outcome-family mass table** (§"Control-execution audit" below). That is recorded on each card as an execution failure, not as a new rule gap.

#### P-358 — Settlement (canonical `P-358`; mini-log alias `TMP-CANON-20260911-01`, retired)

**Event:** Puerto Rico (W) v China (W) — FIBA Women's World Cup 2026, qualification to QF, Berlin · **Official final:** China 75–72, no OT (quarters PR 21-19-13-19; CHN 24-17-11-23). PR 3P **38.9%** (tournament 25.9%), FT 90%; China 3P 34.8%, FT 68.8%. **Trinity San Antonio 35 points**; Han Xu 21/11 · **Source:** FIBA game page `128147-PUR-CHN` · **Population:** EXPLORATORY · **Issued:** 2026-09-10 01:35

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Under 141.5 | 0.64 | **LOSS** | 0.4096 | 147 (+5.5). **Anti-coupled with R2**: a close game keeps late possessions competitive and the underdog scoring. |
| 2 | Puerto Rico +9.5 | 0.57 | **WIN** | 0.1849 | China by 3. |
| 3 | China −9.5 | 0.43 | **LOSS** | 0.1849 | |
| 4 | Over 141.5 | 0.36 | **WIN** | 0.4096 | |

**Potential winner:** China ~73% · **CORRECT** · **Card mean Brier:** 0.2973.

- **Q1:** **Starting fives not confirmed** for either side (FIBA publishes them close to tip). The 12-player rosters — which *are* the bench in FIBA — and both head coaches (Gong Luming, Jerry Batista) were retrieved.
- **Q2:** Accurate. FIBA's team profile now shows San Antonio at 15.5 PPG over **four** games; with 35 against China, her three pre-game group games **average ≈9.0 PPG** (derived arithmetic). Her 35 was a ~4× outlier — an aleatory magnitude (`G-L6`). Her **5.0 steals per game**, though, was the exact transition route the card named as Puerto Rico's counter.
- **Q3:** (a) **No width, no normalised edge** (`G-L8` not executed). (b) Puerto Rico's cold 25.9% three-point rate was used as a **floor** under the Under; small-sample cold shooting regresses *upward* just as hot shooting regresses down (`G-L11`, basketball control 22). (c) Puerto Rico's leaders were carried as **names without numbers** — a direct control-20 violation, adopted two days earlier. (d) The card's own "PR steals/transition" mechanism raises the total precisely in the close-game state that makes +9.5 win (basketball control 24; `G-L10`).

**Three-question retrospective.** 1. *Driver:* Puerto Rico's pressure kept it close (cushion won) while its shooting spiked (38.9% from three, 90% FT) and San Antonio scored 35 — the total cleared by 5.5. 2. *Knowable?* **The mechanism yes; the magnitude no.** 3. *Smallest change:* print the R1–R2 joint probability and shrink small-sample shooting rates in both directions.

| Deep Rank-#1 question | Finding |
|---|---|
| What went right? | Margin read (Puerto Rico's pressure against China's turnovers) and winner both correct. |
| What went wrong? | The total ignored the coupling between a competitive underdog and the scoring level; cold shooting was treated as persistent. |
| Actual mechanism | A three-point close game; PR 38.9% 3P, 90% FT; San Antonio 35. |
| Improvement | Basketball controls 22 and 24 (new); control 20 enforced; `G-L8`, `G-L10`, `G-L11`. |
| Grade (background) | C. |

##### 2026-09-12 retrospective correction

| What went right | Error / uncertainty | Routine change and evidence |
|---|---|---|
| Puerto Rico +9.5 won and China won outright, supporting the broad competitive-game view | Inherited 75-72 defeated Under 141.5. Puerto Rico's cold prior 3P rate did not persist and San Antonio scored 35. The missing quantified player exposure and starting-five capture are real process gaps; the exact individual scoring explosion was not predicted | Print player usage/minutes and shooting attempts, then examine efficiency/turnover/transition scenarios without assigning hindsight weights. Basketball 20-22 and G-L7. Top-two split outcomes do not establish negative correlation |

#### P-359 — Settlement

**Event:** Jordan v Chinese Taipei — Asian Games 2026 men's basketball, Group B · **Official final:** Chinese Taipei 83–80 · **Source:** Petra (Jordan News Agency; external pass, not re-fetched) · **Population:** EXPLORATORY · **Issued:** 2026-09-10 13:43

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Chinese Taipei +10.5 | 0.67 | **WIN** | 0.1089 | Won outright by 3. |
| 2 | Under 162.5 | 0.62 | **LOSS** | 0.3844 | 163 — **lost by 0.5**. Anti-coupled with R1 again (close game → higher total). |
| 3 | Over 162.5 | 0.38 | **WIN** | 0.3844 | |
| 4 | Jordan −10.5 | 0.33 | **LOSS** | 0.1089 | |

**Potential winner:** Jordan ~60% · **WRONG** · **Card mean Brier:** 0.2467.

- **Q1:** Starting fives **not confirmed**; both 12-player rosters (with Chinese Taipei's two late withdrawals and replacements) and both head coaches (Luis Guil Torres, Gianluca Tucci) retrieved.
- **Q2:** Accurate as far as used. The Aichi-Nagoya official schedule was snippet-only (HTTP 403).
- **Q3:** The winner label (Jordan ~60%) sat beside a 67% Chinese Taipei cushion. The latest direct meeting was **Taipei by 14**, so the upset branch was large and should have been printed as a number next to the label (`G-L1`). The total missed by the minimum half-point — a boundary result, not evidence of a directional error.

**Three-question retrospective.** 1. *Driver:* Chinese Taipei's guard core and Gilbeck kept it close and won it. 2. *Knowable?* **Yes** — the card cited the 2025 +14 meeting and the two current-cycle wins over Korea. 3. *Smallest change:* print the underdog's outright-win mass beside every favourite winner label.

##### 2026-09-12 evidence supplement

Petra freshly confirms Taipei 83-80 and the half-point total miss. It does not expose the player box needed to verify the guard-core/Gilbeck causal explanation; retain that explanation as a hypothesis. See [opened sources and field limits](audit_2026-09-12/sport_evidence.md).

#### P-360 — Settlement

**Event:** South Korea v Saudi Arabia — Asian Games men's basketball, Group A · **Official final:** Korea 82–66 (quarters 24-17, 17-11, **33-19**, 8-19 per Yonhap) · **Source:** Yonhap (external) · **Population:** EXPLORATORY · **Issued:** 2026-09-10 16:37

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Under 160.5 | 0.59 | **WIN** | 0.1681 | 148. |
| 2 | Saudi Arabia +12.5 | 0.56 | **LOSS** | 0.3136 | Korea by 16. **Anti-coupled with R1**: the separation that beat the cushion is what kept the total down. |
| 3 | Korea −12.5 | 0.44 | **WIN** | 0.3136 | |
| 4 | Over 160.5 | 0.41 | **LOSS** | 0.1681 | |

**Potential winner:** Korea ~76% · **CORRECT** · **Card mean Brier:** 0.2409.

- **Q1:** Starting fives not confirmed; **availability research was the strongest in the batch** — An Youngjun out (finger), Moon Jeonghyun's late replacement, Choi Junyong not arriving until 15 Sep (Korean-language KBA/Yonhap sources; `L-067` honoured) — and it correctly overrode a secondary preview claiming both teams were at full strength. Both coaches named (Nikolajs Mazurs, Ricardo Maffei).
- **Q2:** Accurate.
- **Q3:** The cushion-plus-Under top two could not both win in the separation state the card itself described (the prior meeting was Korea +13 with a 17-point maximum lead). → `G-L10` / basketball control 24.

**Three-question retrospective.** 1. *Driver:* a 33–19 third quarter created the separation; an 8-point Korean fourth kept it Under. 2. *Knowable?* **Yes.** 3. *Smallest change:* print the top-two joint probability.

##### 2026-09-12 evidence supplement

Yonhap freshly reports a 21-0 third-quarter run and Korea 3/20 from the field in Q4. Those phase facts explain the score more specifically than an assumed universal separation-to-Under effect. Exact shooting sequence was not pregame knowledge. See [opened sources and field limits](audit_2026-09-12/sport_evidence.md).

#### P-361 — Settlement

**Event:** Chunichi Dragons (Kanemaru) @ Yomiuri Giants (Inoue), Tokyo Dome, 10 Sep · **Official final:** YOM 5–3 (Dalbec 2-run HR in the 3rd; 3–3 until two Yomiuri runs in the 8th; each starter allowed 3 ER) · **Source:** NPB BIS (external) · **Population:** EXPLORATORY · **Issued:** 2026-09-10 18:44

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Giants −0.5 | 0.57 | **WIN** | 0.1849 | |
| 2 | Under 5.5 | 0.56 | **LOSS** | 0.3136 | 8 runs. |
| 3 | Over 5.5 | 0.44 | **WIN** | 0.3136 | |
| 4 | Dragons +0.5 | 0.43 | **LOSS** | 0.1849 | |

**Potential winner:** Yomiuri ~58% · **CORRECT** · **Card mean Brier:** 0.2493.

- **Q1:** **Complete** — NPB official batting orders, batteries and full game-day benches for both sides. Managers not re-stated on this card (named on `P-353` the day before).
- **Q2:** Accurate (NPB official game centre, roster notice, SportsNavi per-start logs).
- **Q3:** At 5.5, **one multi-run homer or one relief cluster** crosses the line; the card named both (plus Inoue's 15-day illness gap) and still issued the Under at 56%. → `G-L9`. And Dalbec, a right-handed bat against a left-hander, homered for the **second straight day** (control 27).

**Three-question retrospective.** 1. *Driver:* a two-run homer and an eighth-inning cluster. 2. *Knowable?* **Yes.** 3. *Smallest change:* on a low line, give the single-cluster branch explicit mass before preferring the Under.

##### 2026-09-12 evidence supplement

Correction: Under 5.5 was already lost at 3-3 after inning four. The two eighth-inning runs decided the 5-3 winner/margin, not the total loss. NPB inning record freshly checked; distinguish first threshold crossing from later final-score contributions. See [opened sources and field limits](audit_2026-09-12/sport_evidence.md).

#### P-362 — Settlement

**Event:** Hanwha Eagles (Park Jun-young #96) @ SSG Landers (Ávila), Incheon · **Official final:** SSG 4–3 (SSG 0-0-2-0-0-2-0-0; Hanwha 0-0-1-0-0-0-2-0-0) · **Source:** KBO English scoreboard (re-verified) · **Population:** EXPLORATORY · **Issued:** 2026-09-10 19:16

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Under 9.5 | 0.58 | **WIN** | 0.1764 | 7. |
| 2 | SSG −1.5 | 0.56 | **LOSS** | 0.3136 | By one — **−0.5**. |
| 3 | Hanwha +1.5 | 0.44 | **WIN** | 0.3136 | |
| 4 | Over 9.5 | 0.42 | **LOSS** | 0.1764 | |

**Potential winner:** SSG ~67% · **CORRECT** · **Card mean Brier:** 0.2450.

- **Q1:** **No.** Posted batting orders, catchers and benches were not retrieved; managers not named. **`G14.2` application failure:** `BENCH_NOT_RETRIEVED` should have blocked a full-game total from Rank #1. It won, which does not excuse it.
- **Q2:** Accurate. The external pass settled from secondary reporting (StarNews); the KBO field owner confirms the same line this pass.
- **Q3:** Starter superiority is not margin superiority. SSG winning by exactly one run was the card's own "3–2 / 4–3 / 5–4 once bullpens enter" branch, yet it ranked −1.5 above +1.5 (baseball control 4, cushion decomposition). Hanwha's two 7th-inning runs were the late-bullpen route.

**Three-question retrospective.** 1. *Driver:* Ávila's six strong innings delivered the win and the Under; Hanwha's 7th-inning pair compressed the margin to one. 2. *Knowable?* **Yes.** 3. *Smallest change:* print "favourite wins by exactly one" as a separate mass line before ranking −1.5 over +1.5.

#### P-363 — Settlement

**Event:** Sydney Roosters (W) v Canterbury-Bankstown Bulldogs (W) — NRLW Round 11, Allianz Stadium · **Official final:** Roosters 42–12 (Canterbury led at half-time; six Roosters tries in a 16-minute burst) · **Source:** NRL official match centre / live blog (external) · **Population:** EXPLORATORY (NRLW is a separate population from NRL — `RULES_NRL_RUGBY.md`, `SFA-RUGBY-LEAGUE` preamble) · **Issued:** 2026-09-10 19:40

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Bulldogs +40.5 | 0.61 | **WIN** | 0.1521 | Margin 30. |
| 2 | Under 59.5 | 0.55 | **WIN** | 0.2025 | 54. |
| 3 | Over 59.5 | 0.45 | **LOSS** | 0.2025 | |
| 4 | Roosters −40.5 | 0.39 | **LOSS** | 0.1521 | |

**Potential winner:** Roosters ~97% · **CORRECT** · **Card mean Brier:** 0.1773 — best card of the `P-358`+ block; top two both won.

- **Q1:** **Complete for players** — NRL late mail, 1–17 both sides, no late changes, spines and goal-kickers identified. **Coaches not named.**
- **Q2:** Accurate.
- **Q3:** No width or family mass was printed, but the `RL-B1`–`RL-B8` branch set plus the "40.5+ in only 2 of 10 wins" base-rate line did the equivalent work. The only gap is presentational (`G-L1`, `G-L8`).

**Three-question retrospective.** 1. *Driver:* Canterbury's first-half resistance and 12 points kept both the cushion and the Under alive before the Roosters' second-half surge. 2. *Knowable?* **Yes** — the second-half separation branch and a one-to-two-try Canterbury contribution were both on the card. 3. *Smallest change:* none — a positive model for rugby league.

##### 2026-09-12 evidence supplement

NRL freshly confirms Bulldogs led 12-10 at halftime, Baxter failed HIA and Tagoai was sin-binned at 48 minutes before the Roosters surge. Credit the ordinary competitive-first-half idea; do not backdate the specific dismissal/HIA or call branch prose equivalent to a probability table. See [opened sources and field limits](audit_2026-09-12/sport_evidence.md).

#### P-364 — Settlement (partial: the match is LIVE)

**Event:** England v Pakistan, 3rd Test, Edgbaston — Day-2 card frozen from 156/4 · **Official final (for the ranked rows):** England 210/4 after 45 overs (Guardian over-by-over); 1st innings **453 all out** (89 ov; PCB) · **Match state:** LIVE, Day 3 — Pakistan 206/3, trailing by 114 · **Population:** EXPLORATORY · **Issued:** 2026-09-10 19:51

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | England Under 179.5 after 45 overs | 0.61 | **LOSS** | 0.3721 | 210 — the 24 needed in 6 overs came as **54**. |
| 2 | England 1st innings Under 336.5 | 0.56 | **LOSS** | 0.3136 | 453. **Positively coupled with R1** (one tempo thesis). |
| 3 | England 1st innings Over 336.5 | 0.44 | **WIN** | 0.3136 | |
| 4 | England Over 179.5 after 45 overs | 0.39 | **WIN** | 0.3721 | |

**Potential winner:** England ~91% · **PENDING** (`TMP-OPEN-20260911-03`) · **Card mean Brier (4 rows):** 0.3429.

- **Q1:** **Complete** — both confirmed XIs, Mohammad Ali's ankle knock handled as a workload branch rather than an invented absence; the strip hard gate passed (observed Day-1 evidence). Coaches not named (not decision-driving for a Day-2 phase target).
- **Q2:** Accurate. Direct ESPNcricinfo fetches return HTTP 403; the `r.jina.ai` route works.
- **Q3:** The card assumed a restart block of 17–23 runs in six overs (≈2.8–3.8 runs per over). England's run rate in the Stokes–McCullum era has been **~4.1–4.5 per over** (Sky Sports: a record 4.13 for calendar 2022; 4.40–4.54 in series). The required 4.0 was **at or below England's own norm**, with a set Brook and a 39-over-old ball. → New cricket **control 27**: Test-session phase priors start from the batting side's current-era tempo; an overnight restart widens the distribution and is not a signed slowdown absent direct evidence (`G-L2`).

**Three-question retrospective.** 1. *Driver:* 54 in six overs from the restart, then the old-ball middle order and a deep tail (Smith 69, Lawrence 65, Robinson 50) to 453. 2. *Knowable?* **Yes — unusually clearly**: the card itself listed the ball age, the set batter, the inexperienced support seamers and the batting depth as kill paths. 3. *Smallest change:* use the team's own tempo as the prior; keep the restart as width.

| Deep Rank-#1 question | Finding |
|---|---|
| What went right? | The complements (R3, R4) captured the mechanism; the XI, strip and weather gates all passed. |
| What went wrong? | A generic "overnight reacclimatisation" slowdown was signed negative against England's documented era tempo, and both Unders rested on it. |
| Actual mechanism | Lawrence's aggression, Brook set, old ball, then 297 more runs from 156/4. |
| Improvement | Cricket control 27 (new); `G-L2`; `G-L9` (the 39% complement had to hold the old-ball/set-batter branch). |
| Grade (background) | C. |

##### 2026-09-12 retrospective correction

| What went right | Error / uncertainty | Routine change and evidence |
|---|---|---|
| Original XI and known batting-resource evidence were useful; the issued Over complements won | Under 179.5 at 45 overs and innings Under 336.5 failed: England added 54 over the six-over restart and finished 453. Awarding credit merely because the opposite sides won is not selection success. The mini's Sporting Life betting-tips preview breached MARKET_BLIND; the claim that all sources/gates passed is withdrawn | Use comparable restart-state evidence, ball age, batters and remaining resources; keep generic restart slowdown as an explicit assumption to stress-test. Retrieve original market-blind conditions reporting. Historic 2022/era scoring averages alone do not establish an exact 2026 six-over baseline. Cricket 27 and G-L2/G-L9. Winner remains pending |

##### 2026-09-15 final settlement — potential winner

**Match final:** Pakistan 133 & 449 (96.4 ov); England 453 & 130/2 (24.2 ov) — **England won by 8 wickets**, Day 4, 12 Sep 2026 (ESPNcricinfo full scorecard via `r.jina.ai`; Wikipedia corroborates). **Potential winner England: WIN.** `TMP-OPEN-20260911-03` retired; card `FINAL / SETTLED`. Current-series evidence recovered for the tempo miss: England's innings run rates in Tests 1–2 were 4.55, 4.35 and 3.83 (**907 runs / 210.8 overs = 4.30**) against the 4.00 required — in sources the card already cited. Winner-label blindspot: no win/draw/loss mass or overs-remaining arithmetic; the "Pakistan <200 every innings" aggregate was followed by a 96.4-over 449. → cricket control 27 evidence refresh and new control 28. Full retrospective: §"2026-09-15" at the foot of this file and the archived log B mini (`archive/mini_logs/PREDICTION_MINI_RUNNING_LOG_P390_P406_RETROSPECTIVE_SETTLED_2026-09-15.md` §0.3).

#### P-365 — Settlement

**Event:** Uni-Lions (Dykxhoorn) @ CTBC Brothers (Yu Jun-you), Taichung, CPBL Game 321 · **Official final:** Uni-Lions 6–0 (Dykxhoorn 7 scoreless; Yu 4.2 IP / 3 ER) · **Source:** CPBL Advanced Stats (external) · **Population:** EXPLORATORY · **Issued:** 2026-09-10 20:22

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | CTBC Brothers +1.5 | 0.60 | **LOSS** | 0.3600 | Lost by 6. **Anti-coupled with R2 in the low-total-separation state.** |
| 2 | Under 6.5 | 0.56 | **WIN** | 0.1936 | Exactly 6 — **+0.5**. |
| 3 | Over 6.5 | 0.44 | **LOSS** | 0.1936 | |
| 4 | Uni-Lions −1.5 | 0.40 | **WIN** | 0.3600 | |

**Potential winner:** Uni-Lions ~59% · **CORRECT** · **Card mean Brier:** 0.2768.

- **Q1:** **No.** Batting orders not retrieved (front-end rendering), bench not recorded, managers not named. **`G14.2` application failure:** a margin row ranked #1 with `BENCH_NOT_RETRIEVED`.
- **Q2:** Accurate (CPBL official and Advanced Stats).
- **Q3:** The card wrote "a 4–1 or 5–1 Uni win stays Under while covering −1.5" — the exact result shape — and still ranked the Brothers' cushion first. Yu's sample was 12 first-team innings with **1 strikeout in his last 7 innings** — contact-fragile, and exactly what control 11 (small-sample mixture) and `G-L11` exist to widen.

**Three-question retrospective.** 1. *Driver:* Dykxhoorn's shutout innings plus a Uni-Lions scoring cluster — low-total separation. 2. *Knowable?* **Yes, in the card.** 3. *Smallest change:* baseball control 17 with explicit shutout/one-sided mass; enforce `G14.2`.

| Deep Rank-#1 question | Finding |
|---|---|
| What went right? | The Under (R2) and the winner. |
| What went wrong? | The cushion ranked above the separation state the card itself wrote down, and the bench/lineup gate was not respected. |
| Actual mechanism | 7 scoreless innings against a contact-fragile small-sample starter. |
| Improvement | Control 17 with mass; `G14.2` enforced; `G-L9`, `G-L11`. |
| Grade (background) | C−. |

##### 2026-09-12 retrospective correction

| What went right | Error / uncertainty | Routine change and evidence |
|---|---|---|
| Under 6.5 won at six; Uni's winner call was correct | Brothers +1.5 lost by six. The original card already named a low-total separation state, but its occurrence does not identify the correct pregame mass. Dykxhoorn delivered seven scoreless; Yu allowed seven hits, **five walks and four runs/three earned** in 4.2 innings. Missing lineups/bench/coaches remain a process defect | Model control-loss/early-hook as well as contact variance; show full-game scoring after the starter exits. A long strong start is not itself a guaranteed full-game Under. Baseball 17/28 and G14.2. [CPBL gamebook](https://stats.cpbl.com.tw/schedule/2026-A-321) |

#### P-366 — Settlement (6-over rows graded; 20-over rows terminal censored)

**Event:** Rotterdam Dockers v Glasgow Cosmic — ETPL Match 19, Malahide (rain-delayed; reduced to 19 overs a side) · **Official final:** Rotterdam 172/4 (19) bt Glasgow 141/9 (19) by 31. Rotterdam passed 50 at 6.2 overs, so they were **≤49 at 6.0** (Faf du Plessis 71, Vikramjit 33, Klaasen 30*) · **Source:** ETPL first-party page (now COMPLETED) + CricketEurope / Cricket Ireland archive / Cricbuzz / CricketWorld · **Population:** EXPLORATORY · **Issued:** 2026-09-10 20:25 (pre-ball; start delayed)

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Dockers first 6 overs Under 50.5 | 0.56 | **WIN** | 0.1936 | ≤49. |
| 2 | Dockers Over 166.5 after 20 overs | 0.53 | **CENSORED** | — | Innings reduced to 19 overs; the endpoint was never reached. |
| 3 | Dockers Under 166.5 after 20 overs | 0.47 | **CENSORED** | — | same |
| 4 | Dockers first 6 overs Over 50.5 | 0.44 | **LOSS** | 0.1936 | |

**Potential winner:** Rotterdam ~62% · **CORRECT** · **Card mean Brier (2 rows):** 0.1936.

- **Q1:** **No** — the XI was not retrieved at the freeze, and the toss was reported only by a secondary thread. (Glasgow's actual attack was not re-examined this pass.)
- **Q2:** The ETPL first-party page stayed a **stale "Yet to bat" shell for more than 24 hours** after the match — it read that way at 23:12 AEST on 11 Sep and COMPLETED by ~23:30. Settlement correctly ran through the independent scorecards. → the stale-shell rule and the fallback ladder (`RULES_SOCCER.md` control 17 generalised; `SOURCES.md` §"2026-09-11").
- **Q3:** None material. This is the **worked example of target-by-target settlement**: a reached phase target grades; an unreached endpoint is censored and not remapped (cricket control 15).

**Three-question retrospective.** 1. *Driver:* a cautious new-ball phase, then middle/death acceleration — exactly the joint path the card wrote (≈48/1 after six, then acceleration). 2. *Knowable?* **Yes, and on the card.** 3. *Smallest change:* none for the forecast; settlement routing only.

#### P-367 — Settlement

**Event:** China (W) v France (W) — FIBA WWC quarter-final, Berlin · **Official final:** France 90–61 (quarters FRA 25-23-22-20, CHN 20-11-17-13). China shot **better** — FG 46% v 44%, 3P 43.8% v 37.8% — and still lost by 29 · **Source:** FIBA game page `128149` · **Population:** EXPLORATORY · **Issued:** 2026-09-10 22:21

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | France −24.5 | 0.55 | **WIN** | 0.2025 | +29. |
| 2 | Under 153.5 | 0.54 | **WIN** | 0.2116 | 151. **Positively coupled with R1** (France's defence drives both). |
| 3 | Over 153.5 | 0.46 | **LOSS** | 0.2116 | |
| 4 | China +24.5 | 0.45 | **LOSS** | 0.2025 | |

**Potential winner:** France ~94% · **CORRECT** · **Card mean Brier:** 0.2071 — top two both won.

- **Q1:** Starting fives not confirmed; both final 12s and both coaches (Gong Luming, Jean-Aimé Toupane) retrieved, and **China's absence of Li Yueru (passport) was established from the Chinese Olympic Committee** — the kind of availability fact that matters.
- **Q2:** Accurate. A leaked closed-door scrimmage result was correctly held to low weight.
- **Q3:** None material. The issued centre, **89–63**, against the actual **90–61** — the most accurate basketball centre in the repository's P-333+ record. Winning by 29 while shooting worse is the signature of the possession-volume mechanism the card relied on (turnovers and rest asymmetry).

**Three-question retrospective.** 1. *Driver:* French pressure and depth on a ~21-hour China turnaround. 2. *Knowable?* **Yes, and used.** 3. *Smallest change:* none — keep as the positive basketball model: both rows derived from one score tree whose coupling was positive.

##### 2026-09-12 evidence supplement

Retain the successful France side and full-game Under. Their joint success does not prove all of the proposed possession/rotation mechanisms or the dependence sign; seek full player/possession evidence for that claim. See [opened sources and field limits](audit_2026-09-12/sport_evidence.md).

#### P-368 — Settlement (score rows final; corner row provisional)

**Event:** Al Jazira v Al Nasr — UAE Pro League MW5, Abu Dhabi · **Official final:** 1–1 (HT 1–0; Bruno de Oliveira 10', Ghayedi 61'). FotMob: shots 15–11, **on target 4–1**, possession 61–39, corners **6–3** · **Source:** FotMob via proxy; The Sports Encounter · **Population:** EXPLORATORY · **Issued:** 2026-09-10 23:08

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | 1st-half Over 0.5 | 0.68 | **WIN** | 0.1024 | 10' goal. |
| 2 | Total corners Over 7.5 (no frozen provider) | 0.55 | **PROVISIONAL WIN** | not booked | 9 (multiple secondary displays; independence unverified). `TMP-OPEN-20260911-01`. |
| 3 | Over 2.5 goals | 0.53 | **LOSS** | 0.2809 | 2. |
| 4 | Under 2.5 goals | 0.47 | **WIN** | 0.2809 | |
| 5 | 1st-half Under 0.5 | 0.32 | **LOSS** | 0.1024 | |

**Potential winner:** Al Jazira ~65% · **WRONG** (draw) · **Card mean Brier (4 graded):** 0.1917.

- **Q1:** XIs not confirmed (probable XIs were rightly not promoted); Al Nasr's coach (Milojević) named, Al Jazira's not.
- **Q2:** Accurate; the UAE Pro League's own match centre shows corners as "–", so no field-owner corner lane exists for this league yet.
- **Q3:** The early-goal thesis worked and the full-match Over then failed — a clean case of phase/full decoupling (soccer control 5: the leading-state slowdown). Al Nasr equalised from its **only** shot on target.

**Three-question retrospective.** 1. *Driver:* an early goal, then a leading-state slowdown and a one-shot equaliser. 2. *Knowable?* **Yes** — the 1–1 and 1–0 families were on the card. 3. *Smallest change:* propagate the post-goal slowdown into the full-match distribution; a 1H hit is not evidence that the full-match Over process holds.

#### P-369 — Settlement (score rows final; Rank #1 corner row provisional LOSS)

**Event:** Dubai United v Shabab Al Ahli — UAE Pro League MW5 · **Official final:** 1–1 (HT 0–0; Maouhoub 58', Ezatolahi 74' pen). FotMob: shots 7–17, on target 3–4, corners **5–6 = 11**, possession 44–56 · **Source:** FotMob via proxy; The Sports Encounter · **Population:** EXPLORATORY · **Issued:** 2026-09-10 23:16

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Total corners Under 10.5 (no frozen provider) | 0.68 | **PROVISIONAL LOSS** | not booked | 11 — **−0.5**. `TMP-OPEN-20260911-02`. |
| 2 | 1st-half Over 0.5 | 0.64 | **LOSS** | 0.4096 | 0–0 at HT. |
| 3 | Over 2.5 goals | 0.61 | **LOSS** | 0.3721 | 2. |
| 4 | Under 2.5 goals | 0.39 | **WIN** | 0.3721 | |
| 5 | 1st-half Under 0.5 | 0.36 | **WIN** | 0.4096 | |

**Potential winner:** Shabab Al Ahli ~60% · **WRONG** (draw) · **Card mean Brier (4 graded):** 0.3909 — the worst card of the import.

- **Q1:** XIs not confirmed; both coaches (Andrea Pirlo, André Jardine) named.
- **Q2:** Accurate as far as used.
- **Q3:** Three failures of already-existing rules, all visible on the card itself: (a) **1st-half Over at 64%** against the card's own finding that Shabab had scored **one first-half goal in four league games** and United's only home game was 0–0 at HT — soccer control 20's **third instance** (after `P-323` and `P-337`); (b) full-match **Over at 61%** despite the card noting United's 30% conversion was unsustainable (`G-L2`/`G-L11`: a finishing rate over ~37 shots needs uncertainty and opponent/context checks; no automatic noise label); (c) **corners Under at 68%** on an 8.0 centre with **no width** — an 8.0 centre against a 10.5 line supports a lean, not 0.68, without a stated width (`G-L8`).

**Three-question retrospective.** 1. *Driver:* the suppressed first half the card had documented; one goal each after the break; corners reached 11. 2. *Knowable?* **Yes — all three mechanisms were printed.** 3. *Smallest change:* derive the 1H probability from both teams' current first-half rates (not one team's event hit-rate); print widths on every total.

| Deep Rank-#1 question (provisional) | Finding |
|---|---|
| What went right? | The Under 2.5 and 1H Under complements won; the card did retrieve the right suppression evidence. |
| What went wrong? | The ranking contradicted the card's own evidence on three rows. |
| Actual mechanism | 0–0 HT; 1–1 on a second-half goal and a penalty; 11 corners. |
| Improvement | Control 20 reinforced (both teams' 1H rates); `G-L8` widths; `G-L11`. |
| Grade (background) | D+. |

##### 2026-09-12 retrospective correction

| What went right | Error / uncertainty | Routine change and evidence |
|---|---|---|
| Inherited full-game Under and underdog side won at 1-1 | Rank-1 corners Under 10.5 remains a provisional loss at reported 11; first-half Over lost at 0-0. The corner outcome cannot be promoted by secondary agreement. A half-corner miss does not justify choosing a new line retrospectively | Record exact corner provider and phase-specific route before issue. Keep no-goal early states despite favourite territory. Soccer phase/corner controls, G10.2 and G-L9. Outcome explanation for corners remains provisional, process retrospective complete |

#### P-370 — Administrative closure

**Event:** Jamaica Empress (W) v Trinbago Knight Riders (W), WCPL · **Disposition:** **ADMIN CLOSED / NO FORECAST / NON-SCORABLE.** The supplied Empress innings contracts applied only if the Empress batted first; the toss, innings order and both XIs were unverified when the scheduled start crossed. `CR-P3` failed closed, exactly as `P-333`/`P-343` did. No later result is used to manufacture a view. **Positive administrative control.**

#### P-371 — Settlement

**Event:** Belgium (W) v Germany (W) — FIBA WWC quarter-final, Berlin (Germany are the hosts) · **Official final:** Germany 93–74 (GER won each quarter: 22-20-32-19 v 19-16-24-15; biggest lead 19). Germany 60.6% 2P / **35.5% 3P** / 87% FT; Belgium 48.1% / **23.5%** / 63.2% · **Source:** FIBA game page `128150` (re-verified) · **Population:** EXPLORATORY · **Issued:** 2026-09-11 01:36

| Rank | Contract | `p` | Result | Brier | Boundary / dependence note |
|---:|---|---:|---|---:|---|
| 1 | Belgium −6.5 | 0.59 | **LOSS** | 0.3481 | Germany by 19. |
| 2 | Under 144.5 | 0.53 | **LOSS** | 0.2809 | 167. |
| 3 | Over 144.5 | 0.47 | **WIN** | 0.2809 | |
| 4 | Germany +6.5 | 0.41 | **WIN** | 0.3481 | |

**Potential winner:** Belgium ~74% · **WRONG** · **Card mean Brier:** 0.3145.

- **Q1:** Starting fives not confirmed (Germany's latest official five noted); both final 12s, both coaches (Mike Thibault, Olaf Lange), Satou Sabally's absence and Vervaet's exclusion retrieved.
- **Q2:** Accurate.
- **Q3 (corrected 2026-09-12):** The spread used 38.1% versus 25.2% without frozen attempts; Belgium had three prior games, Germany four. The earlier equal-n/mostly-noise calculation is withdrawn. A Germany-separation scenario and shooting/rotation sensitivity were missing. Actual percentages and quarter scores describe the result; bench, crowd or rest absorption as causal explanations remain hypotheses pending player-level evidence. See the event supplement below and corrected G-L8/G-L10/G-L11.

**Three-question retrospective.** 1. *Driver:* Germany's rebounding and depth plus a shooting reversal, in front of a home crowd. 2. *Knowable?* **Largely yes** — every German mechanism was listed; only the magnitude of the shooting swing was not. 3. *Smallest change:* shrink small-sample shooting gaps with the standard-error arithmetic, and require an underdog-separation family when the underdog has two or more independent current mechanisms.

| Deep Rank-#1 question | Finding |
|---|---|
| What went right? | The German mechanisms were all identified; the complements (R3, R4) won. |
| What went wrong? | A noisy three-game shooting gap was treated as a structural Belgian edge; the family set could not represent the result that happened. |
| Actual mechanism | Germany 35.5% 3P and 87% FT v Belgium 23.5% and 63.2%; led every quarter. |
| Improvement | Basketball controls 22 and 23 (new); `G-L8`, `G-L11`. |
| Grade (background) | C−. |

##### 2026-09-12 retrospective correction

| What went right | Error / uncertainty | Routine change and evidence |
|---|---|---|
| Availability/coaches and German-positive mechanisms were recorded; Over and German cushion won as complements | Both leading picks lost, Belgium -6.5 and Under 144.5, at Germany 93-74. Germany had four prior games versus Belgium three, with no frozen attempt counts. The old assumed equal n and 'mostly noise' claim is withdrawn. Germany won all four quarters but did not lead throughout. Rebounding/bench/crowd as the causal explanation remains incomplete without the full box/game report | Retrieve attempts/minutes and opponent mix, allow Germany to separate in the scenario table, and test shooting/rest/rotation sensitivity. Do not infer the 19-point outcome or correct probability from qualitative possibilities. Basketball 20-24 and corrected G-L8/G-L10/G-L11. [FIBA game](https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128150-BEL-GER) |

#### `TMP-SETTLED-20260911-01` — unsupplied collision record

**Event:** Fenerbahçe v Roma, UEFA Champions League league phase MD1 · **Referenced disposition:** an administrative no-forecast record issued externally under the label "P-358" after the start crossed · **Verified final:** **1–1** (UEFA `matchstats` FAME, match `2049568`) · **Scorable rows:** none · **Status:** ADMIN / NON-SCORABLE; canonical ID deferred until its text is supplied (then the next free ID; no performance consequence either way).


### v4.0 Brier / calibration scorecard — after `P-345`–`P-371` (descriptive; learning-only)

| Scope | Graded rows | W / L | Mean Brier | vs 0.2500 baseline |
|---|---:|---|---:|---|
| `P-345`–`P-357` (incl. the three corner rows settled this pass) | 55 | 36 / 19 | **0.2264** | better |
| `P-358`–`P-371` | 50 | 25 / 25 | **0.2621** | **worse** |
| **This import — all graded rows** | **105** | **61 / 44** | **0.2434** | marginally better |
| — `MLB PRIMARY_SCORED` (`P-347`, `P-348`, `P-349`, `P-351`) | 16 | 9 / 7 | 0.2269 | better |
| — `EXPLORATORY` | 89 | 52 / 37 | 0.2464 | marginally better |
| Research-only diagnostic incl. the two provisional UAE corner rows | 107 | 62 / 45 | 0.2451 | — (not booked) |
| **Running mixed total (all v4.0 scored rows since `P-318`)** | **177** | **98 / 79** | **0.2435** | marginally better |
| **Running `PRIMARY_SCORED`** | **34** | **18 / 16** | **0.2373** | EPL 10 rows 0.2666; **MLB 24 rows 13 / 11, 0.2252** |
| `PRIMARY_SCORED` card count | **8 of 25** | | | first pattern/calibration review still not due |

**Reliability (this import, 105 graded rows):**

| Stated `p` band | Rows | Mean stated `p` | Actual win rate |
|---|---:|---:|---:|
| 0.30–0.39 | 8 | 0.365 | 0.625 |
| 0.40–0.49 | 17 | 0.438 | 0.471 |
| 0.50–0.59 | 30 | 0.563 | 0.600 |
| 0.60–0.69 | 29 | 0.644 | 0.586 |
| 0.70–0.79 | 20 | 0.737 | **0.600** |
| 0.80–0.89 | 1 | 0.820 | 1.000 |

Rows at `p ≥ 0.70` won **13 of 21 (62%) against a mean stated 74%**. A *descriptive, hindsight-only* diagnostic: shrinking every issued probability 25% toward 0.5 would have moved this import's mean Brier from 0.2434 to **0.2411** (50%: 0.2414). **This is not applied to any card** — doing so would be a fitted weight (`L-087`) — but it is consistent evidence of mild over-confidence at the top of the range, and it opens the prospective test `C-PROB-EXTREMITY` (`LEARNING_REGISTER.md`). Sample small, rows dependent within cards; no calibration claim.

**Ordinal record (legacy, structurally limited by slate geometry — `METHOD.md` §7.3):** Rank #1 **16 W / 9 L** plus one provisional loss (`P-369`); Rank #2 **12 W / 12 L** plus one censored (`P-366`) and one provisional win (`P-368`); **top two both won on 6 of 25 decidable cards** (`P-346`, `P-349`, `P-351`, `P-355`, `P-363`, `P-367`; `P-368` would make 7 if its provisional corner row were accepted). Potential-winner labels **13 / 25** against an expected 16.0 from their own stated probabilities; soccer three-way labels **1 / 5**; labels at ≤60% went 5 / 12. **The two halves of this import are not comparable on raw W/L:** `P-345`–`P-357` ranked many analyst-chosen rows (team totals, alternate lines); `P-358`–`P-371` ranked exact complementary pairs, which force one winner per pair — the favoured side of those 25 pairs won **12**.

### Control-execution audit — the finding that matters most in this import

A keyword audit of every issued card (the same check is now scripted as `audit_card_controls.py`) shows that the 2026-09-09 disclosure requirements were **listed but largely not executed**:

| Requirement | Cards issued when it was in force (`P-358`–`P-371`, 13 issued) | Cards that executed it |
|---|---|---|
| `G-L1` outcome-family table with mass | 13 | **0** (and `G-L1` was missing from the external log's carried-control list) |
| Numeric total width | 13 | **0** (corridors only) |
| `G-L8` normalised edge beside every total | 13 | **0** |
| Representative Rank-#1 outcome checked against every row | 13 | **0** |
| `AGGREGATE_ONLY` flag where a disaggregated record was missing | 13 | **0** (`P-358` carried Puerto Rico's leaders as bare names — the control-20 case) |
| `G14.2` — no margin/full-game total at Rank #1 with `BENCH_NOT_RETRIEVED` | 13 | **11** (`P-362` total and `P-365` margin broke it) |

For comparison, among `P-345`–`P-357` (controls not yet in force for most): `P-350` (branch-weighted set tree + representative scoreline), `P-355` (goal/corner/1H families with mass) and `P-356` (final-state mass + normalised edge 0.12) executed the equivalent work — and `P-356` and `P-357` printed normalised edges. **The cards with an explicit family table (`P-350`, `P-355`, `P-363` via its branch set) produced three of the better Brier scores; the cards without one produced every "kill path printed but not weighted" miss below.** This is the same failure one level up from `G-L1`'s origin: a control that exists only as a list item behaves like a kill path that exists only as prose. Response: **`RULES_GENERAL.md` §16.8 card completeness block** — a fixed set of fields printed at the foot of every card and audited at settlement.

### Why the picks went right or wrong — cross-card synthesis, linked to prior lessons

**What went right (keep it):**

1. **Protected sides in low-total baseball games.** `P-347` TEX +1.5, `P-349` SF +1.5, `P-354` HIR +1.5, `P-356` KT +1.5 (Rank #3), `P-362` HAN +1.5 (Rank #3) all won. Baseball control 4 (cushion decomposition) and control 17 (low totals do not imply close margins) worked when applied. The two cushion failures (`P-348`, `P-365`) are the separation states those controls exist to catch.
2. **Team-total Unders anchored on the stronger, established starter: 6 W / 2 L** (`P-349` ×2, `P-351`, `P-353`, `P-354`, `P-356` won; `P-347`, `P-353` Yomiuri lost). Team-total Overs on the side facing the weaker starter went **2 W / 4 L**.
3. **Phase totals: 9 W / 4 L among all graded phase rows; 7 W / 2 L on the favoured side** — soccer 1st-half rows 4/5, limited-overs cricket new-ball phases 3/3. Only `P-364` (a Test restart) and `P-369` lost. A fourth cohort consistent with `C-PHASE-VS-FULL-TOTAL`.
4. **Large-edge alternate lines: 3 / 3** (`P-346` Under 4.5 on a 3.0 centre; `P-355` Under 3.5 and Over 1.5 on a 2.4 centre).
5. **Field-owner participant handshakes:** `P-345` (UEFA XIs + benches), `P-353`/`P-361` (NPB posted orders + benches), `P-363` (NRL late mail) — and good *availability* research where lineups could not be had: `P-360` (An Youngjun out, Choi not yet arrived), `P-367` (Li Yueru's passport), `P-355` (quarantining a lineup feed that listed an ineligible player).
6. **Fail-closed gates worked:** `P-370` (`CR-P3`) and `P-366`'s refusal to remap a 19-over total onto a 20-over contract.

**What went wrong — six mechanisms, each linked to its prior lesson:**

| # | Mechanism | Cards | Prior lesson it repeats | Response this pass |
|---|---|---|---|---|
| A | **Kill path printed, not weighted** — the complement of a high-probability row was left too small for the named threats | `P-347`, `P-351`, `P-352`, `P-354`, `P-356`, `P-357`, `P-361`, `P-362`, `P-364`, `P-365`, `P-371` | `G-L1` (origin `P-340`/`P-342`); `L-070` | **`G-L9` complement decomposition** (§16.5(e)); §16.8 completeness block |
| B | **Small-sample rates treated as direction** — one start, three games' shooting, early-season finishing | `P-345`, `P-356`, `P-358`, `P-369`, `P-371`; `P-365` (Yu) | `G-L2` (origin `P-335`/`P-339`); soccer control 23; basketball control 21 | **`G-L11` sampling-noise check** (§16.5(g)); basketball control 22 |
| C | **Same-channel adjustments stacked** — park + heat + same-park form counted as separate Over reasons | `P-348`, `P-356`, `P-351` | `G22` bidirectional audit; the `P-297` double-count note (`RULES_BASEBALL.md` §"September 6") | **Baseball control 26** (mechanism-overlap audit); `C-RUN-CENTRE-BIAS` |
| D | **Volatile participant state not retrieved although published** — XIs exist after a cricket toss; KBO/CPBL orders post before first pitch | `P-357`, `P-362`, `P-365`, `P-366`; basketball starting fives (`P-358`–`P-360`, `P-367`, `P-371`) | `G14.2`/`L-082`; `BB-P2`; `CR-P3` | **Cricket control 26**; §16.8 item 7 (`RETRIEVAL_MISS` ≠ unavailable); `G14.2` enforcement |
| E | **Current-regime evidence available and set aside** — same-week surface scoring; team tempo | `P-352` (Windhoek 228/217/205 T20Is), `P-364` (England's era run rate) | `G-L7` (origin `P-339`); cricket controls 16/19 | **Cricket controls 25 and 27** |
| F | **Top two structurally anti-coupled** — cushion + Under in basketball; cushion + Under in low-total baseball | `P-358`, `P-359`, `P-360`, `P-365` | basketball controls 11 and 15; baseball control 17 | **`G-L10` joint top-two probability** (§16.5(f)); basketball control 24 |

Plus two narrower items: the **draw band** (soccer three-way winner labels 1 / 5 this import, 5 / 10 across `P-333`+ → soccer control 3 reinforced: print the draw mass beside any plurality winner below 50%) and the **cross-league strength translation** in UEFA fixtures (`P-345`, `P-346` → soccer control 31).

**The honest headline.** Almost every miss in this import was *knowable and printed on the card*. The research found the right facts; the arithmetic did not carry them into the probabilities. The rules responding to that (`G-L9`–`G-L11`, §16.8) are therefore about **forcing the arithmetic to use what the card already knows**, not about finding more facts.

### Researched answer to the standing over/under directive

The ask — *"ideally at least one of the over/under picks needs to win"* — is mechanically guaranteed whenever both sides of the same line are ranked (one of an exact half-point pair always wins; `L-055`). The meaningful question is whether the **preferred** total side wins, and which totals to prefer. Four cohorts of evidence now say:

| Family (favoured side) | `P-318`–`P-332` | `P-333`–`P-344` | `P-345`–`P-371` | Reading |
|---|---|---|---|---|
| Phase totals (1st half; first N overs) — earlier cohorts: soccer 1st-half O/U 0.5 only | 5 W / 2 L | 3 W / 2 L | **7 W / 2 L** (soccer 1H 4 / 5; cricket new-ball phases 3 / 3; Test restart 0 / 1) | the most reliable total family, four cohorts running |
| Alternate lines far from the centre (e.g. Under 4.5 on a 3.0 centre) | — | — | **3 W / 0 L** | large normalised edge — the reason, not the family label |
| Team-total Unders vs the stronger/established starter (baseball) | — | — | **6 W / 2 L** | anchored on starter skill, not on a streak |
| Supplied main-line full-game totals (earlier cohorts: soccer only / all sports) | soccer 6 W / 3 L | **4 W / 5 L** | **13 W / 13 L** (incl. 4 unranked supplied lines) | **a coin flip for three cohorts** |
| — of which the favoured side was an **Over** | | | **1 W / 5 L** by card (six cards; only `P-350`'s tennis extension won) | |
| — of which the favoured side was an **Under** | | | **11 W / 8 L** | |

**Why the main line stays near 50%, measured:** the card's own centres miss by far more than the lines sit from them. Mean absolute centre error — **soccer 1.42 goals** (10 cards, mean signed −0.27: roughly unbiased), **baseball 3.35 runs** (12 cards, mean signed **−1.58**: centres ran **high** — 9 of 12 games finished below the centre), **basketball 8.4 points** (6 cards, mean signed **+4.9**: centres ran **low** in the international games). Supplied lines typically sit 0.05–0.5 of a width from the centre. No amount of fact-finding turns a 0.1-width edge on that error into a reliable pick.

**What to do instead — the concrete algorithm changes adopted this pass (none is an ordinal bar):**

1. **Say "coin flip" when it is one.** `G-L8` already requires the normalised edge; §16.8 makes it a printed field. At an edge under ~0.10 of a width, a total probability belongs at 0.50–0.53, not 0.55–0.64 — the 0.70–0.79 band's 60% hit rate is the cost of doing otherwise.
2. **Fix the bias where it is measured.** Baseball: control 26 (no counting one run-environment channel three times) and the prospective `C-RUN-CENTRE-BIAS` test; Overs built on "weak starter + park + heat" were 0 / 2 on main lines and 2 / 4 on team totals. International basketball: control 24 (a competitive underdog raises the total) and control 22 (shrink small-sample shooting in both directions).
3. **When choosing the analyst's own additional rows (only when the user asks for own picks), prefer the families that have actually held:** phase totals, far-from-centre alternate lines, and team-total Unders anchored on the stronger starter — each with a named mechanism *and* a large normalised edge. **Guidance, not a gate:** the supplied rows are still ranked strictly by marginal probability (`G23.1`), and nothing here licenses promoting a row above a better-evidenced one.
4. **Print the joint top-two probability** (`G-L10`). "Ideally the top two should win" is an aspiration the slate often makes structurally unlikely: a cushion + Under pair in basketball is, by construction, a partial hedge. The card will now say so in a number instead of leaving it to the result.

### Answers to the three standing validation questions — cohort roll-up

**Q1 — Were confirmed starting and bench lineups, plus coaching information, retrieved for both teams?** Complete for both sides on **7 of 26 cards** (`P-345`, `P-352` XIs, `P-353`, `P-354` except Hanshin's manager, `P-361`, `P-363` players, `P-364`); partial on 6 (the four MLB cards had official starters but secondary batting orders and no managers; `P-346` secondary benches; `P-356` one side); not retrieved on 12. Head coaches were named for both sides on 10 cards. **Two cards broke `G14.2`** (`P-362`, `P-365`). **One "unavailable" was actually retrievable** (`P-357`, post-toss XIs). Fixes: §16.8 item 7; cricket control 26; `G14.2` enforcement noted in `RULES_BASEBALL.md`; a statsapi `battingOrder` route to test on the next MLB card.

**Q2 — Were the sources accurate, or are newer, more accurate sources needed?** Every re-verified final (17 of 17) matched. The inaccuracies were all in **niche derivative fields from media secondaries**: the Guardian and VI each misreported a corner count by one against UEFA's own feed (2 of 2 conflicts), and the ETPL first-party page stayed stale for more than a day. **Newer/better lanes adopted this pass:** UEFA `matchstats` FAME (field owner for UEFA club competitions, keyless), FotMob via `r.jina.ai` (Opta data, wide league coverage incl. A-League and UAE), the KBO English scoreboard, FIBA game pages, ESPNcricinfo via proxy, MLB statsapi via `curl`, and Tennis Abstract Elo as an independent benchmark. ClubElo was blocked from this environment (0 bytes on every route) and is **not** graded. Full detail below and in `SOURCES.md` / `DATA_SOURCE_REGISTER.md` §"2026-09-11".

**Q3 — Were there blind spots in the pre-game analysis, and how are they accounted for next time?** Yes — mechanisms A–F above. Each maps to a specific rule added this pass (table above), and the §16.8 completeness block makes each one an auditable field rather than an intention.

### Learnings adopted this pass (disclosure / retrieval / process — no fitted weight, no ordinal bar, `L-087` respected)

| ID | Rule | Where |
|---|---|---|
| **`G-L9`** | **Complement decomposition** — for every ranked row, itemise `1 − p` across the named kill paths (each a weighted branch from the family table); if their honest masses exceed `1 − p`, lower `p`. | `RULES_GENERAL.md` §16.5(e) |
| **`G-L10`** | **Joint top-two probability** — print P(R1 ∧ R2) from the family table and label the pair positively coupled / independent / anti-coupled (`TOP-TWO HEDGE`). Informs; does not reorder. | §16.5(f) |
| **`G-L11`** | **Sampling-noise check** — before a small-sample rate (shooting %, conversion, SoT/shot, a single start's runs, a few innings' strike rate) takes a signed adjustment, print its standard error; a gap under ~2 SE is width. | §16.5(g) |
| `G-L8` clarification | For right-skewed count totals (runs, goals), locate the line against the **median** of the family table, not the mean. | §16.5(d) addendum |
| **§16.8** | **Card completeness block** — fixed fields printed at the foot of every card and audited at settlement (script `audit_card_controls.py`). | `RULES_GENERAL.md` §16.8; `METHOD.md` §4 |
| Sport controls | Baseball **26–28**; basketball **22–24**; soccer **30–31**; cricket **25–27**; tennis **13–14**; NRL positive note. | the sport files, §"2026-09-11" |
| Candidates opened (prospective manifests, no effect on ranking) | `C-RUN-CENTRE-BIAS`, `C-PROB-EXTREMITY`, `C-UNDERDOG-SEPARATION`; `C-PHASE-VS-FULL-TOTAL` updated | `LEARNING_REGISTER.md` §"2026-09-11" |

### New / re-graded information sources (from this import)

| Source | What it did this pass | Grade |
|---|---|---|
| **UEFA `matchstats.uefa.com/v1/team-statistics/{matchId}`** (FAME provider; keyless JSON, both teams) | Settled `P-345-C03` and `P-346-C05`; verified three finals; exposed two media corner errors | **`CANDIDATE` — field owner** for UEFA club competitions. The WebFetch summariser truncates to one team; parse the raw JSON (`curl`). |
| **FotMob match pages via `r.jina.ai`** (Opta data) | Settled `P-355-C05` (its frozen provider); a third lineage for the UAE corners; HT/FT/shots/possession | `CANDIDATE — STRUCTURED SECONDARY`; field-owner-grade only where a card pre-registers it. Direct FotMob/Sofascore API routes remain blocked. |
| **KBO English scoreboard** `eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=` | Verified `P-356`, `P-362` with line scores and decisions | `CANDIDATE — field owner` (English rung; `L-067`) |
| **FIBA game pages** | Quarter scores and team shooting for `P-358`, `P-367`, `P-371` | `CANDIDATE — field owner` (reconfirmed) |
| **ESPNcricinfo via `r.jina.ai`** | Live Test state (`P-364`) and the Windhoek T20I scorecards (`P-352`) | `RESEARCH` route; direct fetch HTTP 403 |
| **MLB statsapi via `curl`** | Four MLB finals | field owner (existing); **WebFetch returns HTTP 406** — use a plain client |
| **Tennis Abstract Elo** `tennisabstract.com/reports/atp_elo_ratings.html` | Independent benchmark for `P-350` (dated 2026-08-31) | `CANDIDATE — BENCHMARK ONLY` (never sets a probability; snapshot date must precede the event) |
| **Cricket Ireland-branded CricketArchive** | Full ETPL scorecards with XIs (`P-357`, `P-366`) | `CANDIDATE` ETPL settlement lane (reconfirmed) |
| Guardian / VI match-stat corner counts | Each off by one against UEFA FAME | **Re-graded: cross-check only; never settles a derivative within ±1 of its line** |
| ETPL first-party match page | Stale "Yet to bat" for >24 h after completion | status field only; never a score source on its own |
| **ClubElo API** | 0 bytes on every route from this environment | **ACCESS FAILED (route-specific) — not graded** |
| ESPN `soccer/uga.1` | Re-probed (the named retry trigger for `P-341-C03`): still season 2025, 0 events on 2026-09-08 | covered-but-stale; retry again later |


---

# Open queue — current (2026-09-11; updated 2026-09-15)

**2026-09-15 update:** `TMP-OPEN-20260911-03` (`P-364` winner) is **retired — WIN** (England won by 8 wickets). **Open rows: 13; no live event.** Retries today: ESPN has no UAE Pro League route (`uae.1`/`are.1`/`uae.pro_league`/`uae.league` all HTTP 400) for `P-368-C02`/`P-369-C01`; `uga.1` still season 2025 with 0 events on 2026-09-08 for `P-341-C03`. `P-342-C03` and the nine Part-2 rows were not re-researched. The current per-row table is `GAME_LOG_STATUS_CURRENT.md` §"Primary result/derivative follow-up queue - 13".

This is the **current** queue. The 2026-09-09 queue section immediately below is retained unchanged as the historical record of that pass (including its ESPN coverage probe), apart from the correction of its dangling 2026-09-10 sentence.

**Tracking-handle conventions.** `TMP-OPEN-<YYYYMMDD>-<seq>` marks an issued row not yet settled to standard (never a canonical ID; never scored; retired on settlement). `TMP-SETTLED-<YYYYMMDD>-<seq>` marks an ID-collision record (`EXTERNAL_LOGGING_WORKFLOW.md`) — first used this pass.

| Handle | Row | Event | Frozen item | Disposition | Retry trigger |
|---|---|---|---|---|---|
| ~~`TMP-OPEN-20260911-03`~~ | `P-364` potential winner | England v Pakistan, 3rd Test — **FINAL (England won by 8 wickets, 12 Sep)** | England to win (~91%) | **RETIRED 2026-09-15 — WIN.** Card `FINAL / SETTLED`. | Official Test result (scheduled through 2026-09-13 BST). Settle the winner label, then close the card. |
| **`TMP-OPEN-20260911-01`** | `P-368-C02` (Rank #2) | Al Jazira 1–1 Al Nasr | Total corners Over 7.5 (no frozen provider) | `PROVISIONAL RESEARCH WIN` — 6–3 = 9 (FotMob/Opta, Forebet, M9Bet). Not booked. | A UAE Pro League official or data-partner match-stat record (the league match centre currently shows "–"). |
| **`TMP-OPEN-20260911-02`** | `P-369-C01` (Rank #1) | Dubai United 1–1 Shabab Al Ahli | Total corners Under 10.5 (no frozen provider) | `PROVISIONAL RESEARCH LOSS` — 5–6 = 11 (multiple secondary displays; independence unverified). Not booked. | Same. |
| `TMP-OPEN-20260909-01` | `P-341-C03` | BUL 4–1 Ntugasaze | Over 7.5 corners | `UNSETTLEABLE` to its pre-registered field-owner standard. **Re-probed 2026-09-11:** ESPN `soccer/uga.1` still season 2025, 0 events on 2026-09-08. | ESPN `uga.1` rolling to 2026-27. |
| `TMP-OPEN-20260909-02` | `P-342-C03` | Komárno 2–0 Lučenec | Over 8.5 corners | `PROVISIONAL RESEARCH WIN` (16) | An SFZ / Niké liga data-partner record. |
| `TMP-OPEN-20260909-03`…`-11` | Part-2 appendix A, B, C, E, F, G, J, K, L | (unchanged) | (unchanged) | Custody stays with `PREDICTION_LOG_COMBINED_2.md`. The external session's 2026-09-11 recheck reported **0 of 9 upgraded**; this pass did not independently re-research them. | as recorded in Part 2 |
| **`TMP-SETTLED-20260911-01`** | unsupplied "P-358" collision record | Fenerbahçe 1–1 Roma | none (no forecast) | ADMIN / NON-SCORABLE | Canonical ID assigned only if the record's text is supplied. |

**Retired this pass (settled at their frozen field owners):** `TMP-OPEN-20260910-01` (`P-345-C03`, WIN, UEFA 4 corners), `TMP-OPEN-20260910-02` (`P-346-C05`, WIN, UEFA 10), `TMP-OPEN-20260910-03` (`P-355-C05`, WIN, FotMob 9). These three handles were issued by the external session on 2026-09-10 and were never recorded in this file until now. **Closed as terminal:** `P-366-C02/C03` (20-over endpoint censored by a rain-reduced innings; no handle — nothing retrievable can change it).

**Open rows across all three parts: 14** — 3 new (`P-364` winner, `P-368-C02`, `P-369-C01`) + 2 carried Part-3 corner rows (`P-341-C03`, `P-342-C03`) + 9 inherited Part-2 rows.


---

# Open queue — 2026-09-09 state (historical record; superseded by "Open queue — current (2026-09-11)" above)

**Temporary-ID convention (introduced 2026-09-09).** `EXTERNAL_LOGGING_WORKFLOW.md` already defines `TMP-SETTLED-<date>-<seq>` for the *ID-collision* case (a distinct new event landing on an occupied canonical ID). That case did **not** arise here — `P-333`–`P-344` mapped one-to-one with no collision. What the ledger lacked was a handle for the separate problem the user has flagged: **rows that are not yet fully settled and therefore cannot yet carry a full retrospective.** A distinct namespace is opened for that, deliberately named so it can never be confused with the collision convention:

> **`TMP-OPEN-<YYYYMMDD>-<seq>`** — a tracking handle for an issued row whose settlement field has not been reached to standard. It is **not** a canonical ID, never enters the scorecard, never receives a W/L or Brier, and is retired the moment the row settles (or is declared terminal), at which point the row is graded under its own canonical `P-###-C##` identifier. Its only function is to guarantee that no unsettled row can be silently lost from the queue.

| Tracking ID | Canonical row | Event (final verified) | Frozen contract | Disposition | Retrospective state | Next action |
|---|---|---|---|---|---|---|
| **`TMP-OPEN-20260909-01`** | `P-341-C03` | BUL FC 4–1 Ntugasaze FC (Uganda Premier League R3) | Over 7.5 total match corners | **`UNSETTLEABLE` to the card's own pre-registered field-owner standard.** Secondary displays indicated ~12 corners (directionally a WIN), but no named official/data-partner endpoint recovered. No W/L/Brier booked. | **Partial.** The card's four score-derived rows have a full three-question retrospective (above). The corner row cannot be retrospected on outcome because no outcome exists to standard; its *process* retrospective is complete and positive — the pre-registered gate worked exactly as written. | **Concrete retry trigger identified (see the settlement attempt below): re-query `soccer/uga.1` once ESPN rolls the feed to 2026-27.** Do not settle from a secondary count (`G10.2`/`L-081`). |
| **`TMP-OPEN-20260909-02`** | `P-342-C03` | Komárno 2–0 Lučenec (Slovnaft Cup R3) | Over 8.5 total match corners | **`PROVISIONAL RESEARCH WIN`** — two secondary structured sources report 1–15 = 16 corners; `RESEARCH_DIRECTION = PROVISIONAL WIN`, `OPERATOR_ACTION = UNKNOWN_DEFINITION`. No frozen provider. If later accepted, row Brier would be 0.2116 and the 5-row card mean 0.3527 — **not entered now.** | **Partial.** Four score-derived rows fully retrospected (deep Rank-#1 block above). The corner row's direction is corroborated but its provider was never frozen, so no outcome-based retrospective is created. | **No ESPN route exists for any Slovak competition (verified below).** Retry only via an SFZ / Niké liga data-partner record. A `PROVISIONAL WIN` never advances the scorecard. |

#### Fresh settlement attempt, 2026-09-09 — the framework's primary structured lane, tested properly

`RULES_SOCCER.md` control 10 requires retrying official/data-partner sources *after* the final before an `UNSETTLEABLE` verdict, and `G10.2` requires confirming whether a structured provider carries **this competition**. The first pass of this session did not test `SRC-ESPN-SITE-API-SOCCER` on either competition — only aggregator pages, which returned HTTP 403. That gap is now closed. Method: direct `curl` to `site.api.espn.com` (default client, per the `SOURCES.md` §2 access note), with `soccer/eng.1` as a positive control.

| Probe | Result |
|---|---|
| `soccer/eng.1/scoreboard?dates=20260908` (control) | **HTTP 200** — method sound |
| `soccer/uga.1/scoreboard?dates=20260908` | **HTTP 200**, league resolves as **"Ugandan Premier League"** — the competition *is* carried |
| `soccer/uga.1` events on 2026-09-08 | **0 events** |
| `soccer/uga.1` events across 2026-09-01 → 2026-09-15 | **0 events** |
| `soccer/uga.1` default scoreboard — season/calendar state | **season `2025`, "2025-26 Ugandan Premier League", 97 calendar entries, last events dated 2026-05-23** (NEC–Calvary, BUL–Entebbe UPPC, KCCA, Kitara, Lugazi, SC Villa, Vipers) |
| `soccer/svk.1`, `svk.2`, `svk.cup`, `svk.slovnaft_cup`, `svk.slovak_cup`, `svk.slovakia_cup`, `svk.fortuna_liga`, `svk.super_liga`, `slk.1`, `slovak.1` | **HTTP 400 on all ten** |
| `sports.core.api.espn.com/v2/sports/soccer/leagues?limit=1000` | 218 leagues returned (`count` = 218, complete). **No Slovak competition of any kind. No Uganda entry either.** Only sub-Saharan African league listed: `rsa.1`. |

**Two findings, both material:**

1. **`P-341-C03` is a season-rollover coverage gap, not absent coverage.** ESPN carries the Ugandan Premier League and its `wonCorners` field is a league-level capability, but the feed had not been rolled to 2026-27 as at 2026-09-09 — its newest event is 2026-05-23. This converts a vague "retry if it ever appears" into a **concrete, checkable retry trigger**: re-query `uga.1` for `dates=20260908` once the feed advances to the 2026-27 season. The row stays `UNSETTLEABLE` today, correctly.

2. **The ESPN core league directory is not authoritative for what the site API serves — probe the site API directly.** `uga.1` returns HTTP 200 with a real league name on the site API while being **absent from the 218-league core directory**. Had the directory been treated as the coverage test, Uganda would have been wrongly written off as uncovered. Conversely, ten Slovak slug forms fail on the site API *and* Slovakia is absent from the core directory — two independent lines agreeing, which is why `P-342-C03` is recorded as genuinely outside this lane rather than a slug-guessing failure. This is a **new standing source-lane rule**, folded into `SOURCES.md` §2 and `DATA_SOURCE_REGISTER.md`.

Verified non-coverage list (`SOURCES.md` §2) is extended accordingly: **Slovak Cup / Slovnaft Cup and all Slovak competitions — no ESPN route (site API 400 × 10 slug forms; absent from the core directory).** Uganda Premier League moves from untested to **covered-but-stale (2025-26)**.

These were the only open `P-333`–`P-344` items. *(Correction 2026-09-11: a 2026-09-10 edit inserted a sentence here pointing to "the table below" for three further derivative rows — `P-345-C03`, `P-346-C05`, `P-355-C05` — but never added that table or the cards they belonged to. All three were settled at their frozen field owners on 2026-09-11 (UEFA FAME; FotMob/Opta) and their external handles `TMP-OPEN-20260910-01`…`-03` are retired — see §"2026-09-11" and "Open queue — current (2026-09-11)".)*

**Applying the same handle to the inherited Part-2 backlog.** For completeness of the ledger — the user's explicit ask that *all* logs be trackable to full settlement — the eight still-open Part-2 appendix rows are also given tracking handles below. **They remain governed by, and are settled in, `PREDICTION_LOG_COMBINED_2.md`'s lettered appendix; Part 3 does not re-open them and does not attempt to settle them.** This table is an index, not a transfer of custody.

| Tracking ID | Appendix letter / canonical row | Frozen open contract | Standing disposition (2026-09-07 maximum attempt, unchanged unless noted) |
|---|---|---|---|
| `TMP-OPEN-20260909-03` | **A** / `P-126` | Total Corners Over 7.5 + whole-event identity | `IDENTITY_STATE_CONFLICT — UNRESOLVED` |
| `TMP-OPEN-20260909-04` | **B** / `P-148-C02` | Toluca team corners | `PROVISIONAL LOSS` |
| `TMP-OPEN-20260909-05` | **C** / `P-149-C02` | Ventura team corners | `PROVISIONAL WIN` |
| `TMP-OPEN-20260909-06` | **E** / `P-176-C05` | Amiens/Versailles Under 10.5 corners | `PROVISIONAL WIN` — **strengthened 2026-09-09** (APWin/Football365/TotalCorner consistent at 5–3 = 8) |
| `TMP-OPEN-20260909-07` | **F** / `P-178-C05` | Cannes/Le Puy Under 10.5 corners | **Updated 2026-09-09: `UNRESOLVED → PROVISIONAL LOSS`** (leballonrond + Forebet independently 8–8 = 16) |
| `TMP-OPEN-20260909-08` | **G** / `P-179-C05` | Thionville/Paris 13 Under 10.5 corners | `PROVISIONAL WIN` (8–1 = 9) |
| `TMP-OPEN-20260909-09` | **J** / `P-233` | Beijing/Lanzhou Over 8.5 corners | `PROVISIONAL WIN` (secondary 13) |
| `TMP-OPEN-20260909-10` | **K** / `P-234-C03` | Dalian/Shenhua Over 8.5 corners | `PROVISIONAL WIN` (secondary 10; disrupted-match flag) |
| `TMP-OPEN-20260909-11` | **L** / `P-235` | Shandong/Shanghai Port Over 8.5 corners | `PROVISIONAL WIN` (secondary 14) |

Items **D** (`P-166`), **H** (`P-200`), **I** (`P-217`) and **M** (`P-274`) are `RESEARCH SETTLED` with `OPERATOR_ACTION = UNKNOWN_DEFINITION` — settled to this framework's standard, awaiting nothing retrievable, and therefore **not** assigned a tracking handle. Item **N** (`P-307`) issued no forecast and is non-scorable. `P-003` is terminal `UNSETTLEABLE`; `P-316` is a canonical alias. **Total genuinely open rows across all three parts: 11** — 2 new (`P-341-C03`, `P-342-C03`) + 9 inherited.

---

# Full game-log settlement status — from the first log

Per user request: every game log settled and yet-to-be-settled, from the start. **The complete per-ID enumeration from `P-001` to `P-371` is [`GAME_LOG_STATUS_INDEX_2026-09-05.md`](GAME_LOG_STATUS_INDEX_2026-09-05.md)** (extended to `P-371` on 2026-09-11) — that file lists every canonical ID individually with its status. The summary below is the roll-up; `P-333`+ detail is in this file.

### `P-001`–`P-332` (Parts 1 & 2 — closed archives)

- **Settled / performance-eligible:** the great majority of `P-001`–`P-332` (`EP-2026.09.06-v2` — settlement is the sole eligibility test).
- **Administrative no-forecast closures (non-scorable):** `P-307`, `P-324`, `P-326`, `P-330`.
- **Identity/state conflict, unresolved:** `P-126` (Part 2 appendix item **A**).
- **Terminal `UNSETTLEABLE`:** `P-003` (historical corners row).
- **Canonical alias (not independently graded):** `P-316` (alias of `P-317`).
- **Open derivative / operator-only rows in the Part 2 lettered appendix (A–N):**
  - **A** `P-126` — identity/state conflict, UNRESOLVED.
  - **B** `P-148-C02` — Toluca team corners, PROVISIONAL LOSS.
  - **C** `P-149-C02` — Ventura team corners, PROVISIONAL WIN.
  - **D** `P-166` — RESEARCH SETTLED; `OPERATOR_ACTION = UNKNOWN_DEFINITION`.
  - **E** `P-176-C05` — Amiens/Versailles Under 10.5 corners, PROVISIONAL WIN (**strengthened 2026-09-09**: APWin/Football365/TotalCorner consistently 5–3 = 8).
  - **F** `P-178-C05` — Cannes/Le Puy Under 10.5 corners — **updated 2026-09-09: `UNRESOLVED → PROVISIONAL LOSS`** (leballonrond + Forebet independently show 8–8 = 16; still not field-owner grade).
  - **G** `P-179-C05` — Thionville/Paris 13 Under 10.5 corners, PROVISIONAL WIN (strengthened; 8–1 = 9).
  - **H** `P-200` — RESEARCH SETTLED; `OPERATOR_ACTION = UNKNOWN_DEFINITION`.
  - **I** `P-217-C01/C02` — RESEARCH SETTLED on the revised 16-over innings; `OPERATOR_ACTION = UNKNOWN_DEFINITION`.
  - **J** `P-233` — Beijing/Lanzhou Over 8.5 corners, PROVISIONAL WIN (secondary 13).
  - **K** `P-234-C03` — Dalian/Shenhua Over 8.5 corners, PROVISIONAL WIN (secondary 10; disrupted-match flag).
  - **L** `P-235` — Shandong/Shanghai Port Over 8.5 corners, PROVISIONAL WIN (secondary 14).
  - **M** `P-274` — RESEARCH SETTLED; `OPERATOR_ACTION = UNKNOWN_DEFINITION`.
  - **N** `P-307` — no forecast issued; non-scorable.
- **Temporary IDs required for Parts 1–2:** none — every open item is an update to an existing canonical ID (Part 2 appendix instruction; reconfirmed 2026-09-09).

### `P-333`–`P-344` (this file — settled 2026-09-09)

| ID | Status | Ranked-row result |
|---|---|---|
| `P-333` | **ADMIN CLOSED / NO FORECAST** | none issued |
| `P-334` | **ADMIN CLOSED / NO FORECAST** | none issued |
| `P-335` | **FINAL / SETTLED** (`MLB PRIMARY_SCORED`) | R1 W, R2 L, R3 L, R4 W; winner W; Brier 0.2541 |
| `P-336` | **FINAL / SETTLED** | R1 W, R2 W, R3 W, R4 L, R5 L; winner W; Brier 0.1751 |
| `P-337` | **FINAL / SETTLED** | R1 W, R2 L, R3 L, R4 W, R5 L; winner L; Brier 0.2603 |
| `P-338` | **FINAL / SETTLED** | R1 W, R2 W, R3 L, R4 L; winner W; Brier 0.2163 |
| `P-339` | **FINAL / SETTLED** | R1 L, R2 L, R3 W, R4 W; winner W; Brier 0.3368 |
| `P-340` | **FINAL / SETTLED** | R1 W, R2 W, R3 L, R4 W, R5 L; winner W; Brier 0.2155 |
| `P-341` | **FINAL / PARTIAL** — C03 corners `UNSETTLEABLE` | R1 W, R2 L, R4 W, R5 L; winner W; 4-row Brier 0.2443 |
| `P-342` | **FINAL / PARTIAL** — C03 corners PROVISIONAL WIN | R1 L, R2 L, R4 W, R5 W; winner W; 4-row Brier 0.3880 |
| `P-343` | **ADMIN CLOSED / NO FORECAST** | none issued |
| `P-344` | **FINAL / SETTLED** | R1 L, R2 W, R3 L, R4 W; winner W; Brier 0.3334 |

**This cohort:** 9 issued cards, 3 admin closures. Ranked rows (settled): **20 W / 19 L**. Rank #1: **6 W / 3 L** (`P-339`, `P-342`, `P-344` lost). Top-two both won: **`P-336`, `P-338`, `P-340`** (3 of 9). Potential winners: **8 / 9 correct** (`P-337` a 0–0 draw). Preferred full-match total O/U: **4 W / 5 L**. **Descriptive only — mixed populations, mixed horizons, complementary-pair geometry; not an accuracy, ROI, edge or calibration claim.**


### `P-345`–`P-371` (this file — settled 2026-09-11)

| ID | Event | Status | Ranked-row result |
|---|---|---|---|
| `P-345` | Club Brugge v Aston Villa — UCL MD1 | **FINAL / SETTLED** (corner row settled at UEFA this pass) — deep Rank-#1 retro | R1 L, R2 W, R3 W, R4 W, R5 L; winner L; Brier 0.2466 |
| `P-346` | AEK Athens v LASK — UCL MD1 | **FINAL / SETTLED** — all five rows won | W W W W W; winner W; Brier 0.0816 |
| `P-347` | Rangers @ Mariners (`MLB PRIMARY_SCORED`) | **FINAL / SETTLED** | W L W L; winner W; Brier 0.2374 |
| `P-348` | Blue Jays @ Athletics (`MLB PRIMARY_SCORED`) | **FINAL / SETTLED** | W L L L; winner W; Brier 0.2803 |
| `P-349` | Cardinals @ Giants (`MLB PRIMARY_SCORED`) | **FINAL / SETTLED** — all four rows won | W W W W; winner L; Brier 0.1440 |
| `P-350` | Shelton v Alcaraz — US Open men's QF | **FINAL / SETTLED** — deep Rank-#1 retro | L W W W; winner = R1; Brier 0.2574 |
| `P-351` | Reds @ Dodgers (`MLB PRIMARY_SCORED`) | **FINAL / SETTLED** — top two won | W W L L; winner W; Brier 0.2460 |
| `P-352` | Namibia v South Africa — 1st ODI | **FINAL / SETTLED** — deep Rank-#1 retro | L W W W; winner W; Brier 0.2158 |
| `P-353` | Dragons @ Giants — NPB, 9 Sep | **FINAL / SETTLED** | W L W L; winner L; Brier 0.2549 |
| `P-354` | Carp @ Tigers — NPB | **FINAL / SETTLED** | W L L W; winner L; Brier 0.2968 |
| `P-355` | Sydney FC v Melbourne Victory — Australia Cup SF | **FINAL / SETTLED** (corner row settled at FotMob this pass) — top two won | W W L W W; winner L; Brier 0.1531 |
| `P-356` | KT @ Samsung — KBO | **FINAL / SETTLED** — deep Rank-#1 retro | L W W W; winner L; Brier 0.2418 |
| `P-357` | Dublin Guardians v Belfast Wolves — ETPL M18 | **FINAL / SETTLED** — deep Rank-#1 retro | L L W W; winner L; Brier 0.3377 |
| `P-358` | Puerto Rico W v China W — FIBA WWC (mini-log alias `TMP-CANON-20260911-01`, retired) | **FINAL / SETTLED** — deep Rank-#1 retro | L W L W; winner W; Brier 0.2973 |
| `P-359` | Jordan v Chinese Taipei — Asian Games | **FINAL / SETTLED** | W L W L; winner L; Brier 0.2467 |
| `P-360` | South Korea v Saudi Arabia — Asian Games | **FINAL / SETTLED** | W L W L; winner W; Brier 0.2409 |
| `P-361` | Dragons @ Giants — NPB, 10 Sep | **FINAL / SETTLED** | W L W L; winner W; Brier 0.2493 |
| `P-362` | Eagles @ Landers — KBO | **FINAL / SETTLED** | W L W L; winner W; Brier 0.2450 |
| `P-363` | Roosters W v Bulldogs W — NRLW R11 | **FINAL / SETTLED** — top two won | W W L L; winner W; Brier 0.1773 |
| `P-364` | England v Pakistan — 3rd Test (Day-2 card) | **FINAL / SETTLED (2026-09-15)** — England won by 8 wickets; winner label settled, `TMP-OPEN-20260911-03` retired — deep Rank-#1 retro | L L W W; winner **W**; Brier 0.3429 |
| `P-365` | Uni-Lions @ CTBC Brothers — CPBL | **FINAL / SETTLED** — deep Rank-#1 retro | L W L W; winner W; Brier 0.2768 |
| `P-366` | Rotterdam v Glasgow — ETPL M19 | **FINAL / SETTLED** — 20-over rows **TERMINAL CENSORED** | W C C L; winner W; Brier 0.1936 (2 rows) |
| `P-367` | China W v France W — FIBA WWC QF | **FINAL / SETTLED** — top two won | W W L L; winner W; Brier 0.2071 |
| `P-368` | Al Jazira v Al Nasr — UAE Pro League | **FINAL / PARTIAL** — C02 corners provisional WIN (`TMP-OPEN-20260911-01`) | W P L W L; winner L (draw); Brier 0.1917 (4 rows) |
| `P-369` | Dubai United v Shabab Al Ahli — UAE Pro League | **FINAL / PARTIAL** — C01 corners provisional LOSS (`TMP-OPEN-20260911-02`) — deep Rank-#1 retro (provisional) | P L L W W; winner L (draw); Brier 0.3909 (4 rows) |
| `P-370` | Jamaica Empress W v TKR W — WCPL | **ADMINISTRATIVE CLOSED / NO FORECAST** (`CR-P3` fail-closed) | none issued |
| `P-371` | Belgium W v Germany W — FIBA WWC QF | **FINAL / SETTLED** — deep Rank-#1 retro | L L W W; winner L; Brier 0.3145 |
| `TMP-SETTLED-20260911-01` | Fenerbahçe v Roma — UCL (unsupplied external "P-358" no-forecast record) | **ADMIN / NON-SCORABLE** | none issued; final 1–1 |

**This import:** 26 issued cards, 1 administrative closure, 1 collision record. Graded ranked rows **61 W / 44 L** (mean Brier 0.2434). Rank #1 **16 W / 9 L** plus one provisional loss. Top two both won on **6 of 25** decidable cards. Potential winners **13 / 25** (one pending). Preferred main-line totals **13 W / 13 L**; phase totals (favoured side) **7 W / 2 L**. **Descriptive only — learning-only per user direction; not an accuracy, ROI, edge or calibration claim.**

---

# Next forecast slot

**Next canonical ID: `P-424`.** (`P-372` is RESERVED / UNUSED; `P-373`–`P-423` imported 2026-09-15(b).)

For the next sports query: refresh `METHOD.md`, `RULES_GENERAL.md` §16 (now including §16.5(e)–(g) and the **§16.8 card completeness block**), the relevant `RULES_<SPORT>.md` (each carries a §"2026-09-11" section), `CONTROLS.md` and this snapshot.

1. **Queue first.** Settle `P-364`'s potential-winner label once the Test has finished (official result: ECB / PCB / ESPNcricinfo scorecard). Retry the four corner rows (`P-341-C03`, `P-342-C03`, `P-368-C02`, `P-369-C01`) only if a new field-owning provider appears; none blocks a new forecast.
2. **Freeze** identity, contract, target, time and participants. **Retrieve published lineups before freezing**: a cricket XI exists once the toss is recorded; baseball, soccer and rugby league line-ups are normally published before the start. `NOT_RETRIEVED` after publication is a `RETRIEVAL_MISS`, not an unavailability — and `G14.2` still blocks a margin or full-game total from Rank #1 when the bench is not retrieved.
3. **Build the joint event object** with the outcome-family mass table (`G-L1`), a numeric width and the normalised edge for every total (`G-L8`; for right-skewed run and goal totals, locate the line against the median). Itemise the complement of Rank #1 and Rank #2 across their named kill paths (`G-L9`). Print **P(R1 ∧ R2)** and the pair's coupling (`G-L10`). Run the sampling-noise check on every small-sample rate that carries a signed adjustment (`G-L11`).
4. **Finish with the §16.8 completeness block**, append the card before delivery, and update this snapshot — including the running Brier scorecard — in the same edit.


## 2026-09-12 controlling audit and learning supplement

Twenty raw mini logs were moved byte-exact to archive/mini_logs; P-345-P-371 were already imported, so no duplicate forecasts or fresh IDs were created. Next ID P-372. [Archive manifest](audit_2026-09-12/archive_manifest.md). Current all-log eligibility is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

**Corrected denominators:** 109 issued rows =105 graded +2 provisional +2 censored; 61 W/44 L, mean Brier 0.243439. Top two: 6/23 with both rows graded, 6/24 logically decidable including P-369 failure through its settled rank 2. P-368 unresolved and P-366 censored. The earlier 6/25 and unreconciled 13W/13L main-line O/U headline are superseded. The 7+6+12 lineup roll-up is withdrawn; use the 26-card matrix below.

## Starting lineups, bench and coaching audit

This matrix reports **what the issued card says it captured**, checked against the preserved mini/canonical text; it does not backdate later source retrieval. A roster is not a confirmed starting lineup. Exact complete-match publication times were not independently recovered for every card. P-370 is administrative and excluded from the 26-card denominator.

| ID | Both starting lineups | Bench/reserves | Both coaches/managers | Combined answer |
|---|---|---|---|---|
| P-345 | Recorded official XIs | Both recorded | Both named | Recorded complete; source-time qualification retained |
| P-346 | Recorded official XIs | Secondary only | Both named | Partial source quality |
| P-347 | Pitchers official; batting orders secondary | Bullpen names, full reserves not demonstrated | Not named | Partial |
| P-348 | Pitchers official; batting orders secondary | Full reserves not demonstrated | Not named | Partial |
| P-349 | Pitchers official; orders mixed/TBD | Full reserves not demonstrated | Not named | Partial |
| P-350 | Tennis players identified; team starters N/A | N/A | Not captured | Coach field missing; team lineup N/A |
| P-351 | Pitchers official; batting orders secondary | Full reserves not demonstrated | Not named | Partial |
| P-352 | Both XIs recorded | Reserves not demonstrated | Not named | XI complete; combined answer no |
| P-353 | Both orders recorded | Both recorded | Both named | Recorded complete; pregame timestamps not reconstructed |
| P-354 | Both orders recorded | Both recorded | Hanshin missing | Combined answer no |
| P-355 | Not confirmed | Official squad context; bench roles unresolved | Both named | No; rejected an inconsistent secondary lineup |
| P-356 | Samsung order; KT unresolved | Not captured | Not captured | No |
| P-357 | Not captured before issue | Not captured | Not captured | No; public pre-cutoff availability not proved by toss alone |
| P-358 | Both fives unconfirmed | Final twelves, starter/bench split unresolved | Both named | No |
| P-359 | Both fives unconfirmed | Final twelves, split unresolved | Both named | No |
| P-360 | Both fives unconfirmed | Availability/roster context; full role split not demonstrated | Both named | No |
| P-361 | Both orders recorded | Both recorded | Carried from prior card, not refreshed here | Partial |
| P-362 | Not captured | Not captured | Not captured | No; missing bench gate affected top full-game total |
| P-363 | Both 1-17 recorded | Included in 1-17 | Not named before issue | Players complete; combined answer no |
| P-364 | Both XIs recorded | Remaining batting order known; reserves not demonstrated | Not named | XI complete; combined answer no |
| P-365 | Not captured | Not captured | Not captured | No; missing bench gate affected top handicap |
| P-366 | Not captured | Squad context only | Not established | No |
| P-367 | Both fives unconfirmed | Both final twelves, split unresolved | Both named | No |
| P-368 | Not confirmed | Not confirmed | Al Jazira missing | No |
| P-369 | Not confirmed | Not confirmed | Both named | No |
| P-371 | Both fives unconfirmed | Both final twelves, split unresolved | Both named | No |

The numerical 7/26 'complete' headline is withdrawn. Only P-345/P-353 are described as capturing all three categories on both sides in the reviewed text. That is **recorded completeness**, not fresh proof of every pre-cutoff publication or complete source accuracy. Coaches were missing even in several otherwise strong lineup captures. Positive retrieval should be preserved without overstating it.




## Recomputed preferred scoring O/U table

Definition: the lowest-numbered ranked scoring total/threshold on each issued card; includes goals, runs, points, innings, phases and sets, and the literal 150+ threshold; excludes corner derivatives and handicap rows. This is not the earlier supplied-main-line population. One observation per card; no retrospective choice of the winner.

**16 W / 10 L over 26 graded preferred scoring targets.** Including corner totals in the selection definition instead gives 16 W / 9 L plus P-369 provisional: a different, explicitly labelled population.

| Card | Original rank | Preferred scoring target | Issued p | Existing research result |
|---|---:|---|---:|---|
| P-345 | 2 | Club Brugge team total Over 0.5 | 0.70 | **WIN** |
| P-346 | 2 | AEK team total Over 0.5 | 0.78 | **WIN** |
| P-347 | 2 | Mariners team total Under 4.5 | 0.71 | **LOSS** |
| P-348 | 1 | Blue Jays team total Over 3.5 | 0.73 | **WIN** |
| P-349 | 2 | Giants team total Under 4.5 | 0.66 | **WIN** |
| P-350 | 2 | Over 3.5 sets | 0.66 | **WIN** |
| P-351 | 1 | Reds team total Under 4.5 | 0.74 | **WIN** |
| P-352 | 1 | SA 1st innings Under 305.5 | 0.68 | **LOSS** |
| P-353 | 1 | Chunichi team total Under 4.5 | 0.75 | **WIN** |
| P-354 | 1 | Hiroshima team total Under 3.5 | 0.76 | **WIN** |
| P-355 | 1 | 1st-half Under 1.5 | 0.82 | **WIN** |
| P-356 | 1 | Samsung team total Over 3.5 | 0.70 | **LOSS** |
| P-357 | 1 | Belfast 1st innings 150+ | 0.72 | **LOSS** |
| P-358 | 1 | Under 141.5 | 0.64 | **LOSS** |
| P-359 | 2 | Under 162.5 | 0.62 | **LOSS** |
| P-360 | 1 | Under 160.5 | 0.59 | **WIN** |
| P-361 | 2 | Under 5.5 | 0.56 | **LOSS** |
| P-362 | 1 | Under 9.5 | 0.58 | **WIN** |
| P-363 | 2 | Under 59.5 | 0.55 | **WIN** |
| P-364 | 1 | England Under 179.5 after 45 overs | 0.61 | **LOSS** |
| P-365 | 2 | Under 6.5 | 0.56 | **WIN** |
| P-366 | 1 | Dockers first 6 overs Under 50.5 | 0.56 | **WIN** |
| P-367 | 2 | Under 153.5 | 0.54 | **WIN** |
| P-368 | 1 | 1st-half Over 0.5 | 0.68 | **WIN** |
| P-369 | 2 | 1st-half Over 0.5 | 0.64 | **LOSS** |
| P-371 | 2 | Under 144.5 | 0.53 | **LOSS** |

Reproduction: read the preserved pre-edit Part-3 settlement tables; for each P-345-P-371 card choose its lowest original rank meeting the definition above; exclude P-370 because no forecast exists. Grade exact original targets. Brier is sum((p-y)^2)/105 with y=1 for WIN and 0 for LOSS. All 105 printed row Briers agree to four decimals. The two provisional and two censored rows contribute neither W/L nor Brier.

### General learnings - 2026-09-12

These corrections apply to future research and to interpretation of the historical retrospectives. They change no issued selection, probability, or outcome. The full log remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under the current user instruction. Older eligibility statements are historical. No numerical model, coefficient, or accuracy improvement is validated by this pass.

## Probability must describe the exact contract

G-L8 correction: use the distribution or joint scenario table for the exact target. For total X and threshold L, P(Under)=P(X<L), P(Over)=P(X>L), and P(push)=P(X=L) when the contract provides a push. State void/censoring separately. On an integer-valued target and a half-line, Under L is X<=floor(L). For integer lines, using P(X<=L) as the Under probability incorrectly includes the push mass.

Print the direction, centre definition (mean/median), width definition (standard deviation, interval coverage, or scenario range), and the signed distance from the line. Absolute distance alone loses direction. Mean and width do not uniquely determine a distribution; a median alone does not determine a probability either. Cross-card probability ordering by absolute normalized distance is justified only under a common specified standardized distribution and comparable width definitions. The old cross-sport normal-CDF comparison is an illustrative sensitivity calculation, not proof that the issued probabilities were incoherent. Do not enforce an invented 0.50-0.53 probability band from an undefined 0.10-width distance.

G-L9 correction: named adverse mechanisms can overlap and need not guarantee a loss. Partition complete outcomes into mutually exclusive, exhaustive states, then add each losing state's mass once. For example, an early pitching hook and bullpen fatigue can happen together; six innings allowing one run does not force a full-game team-total Under if the bullpen subsequently allows runs. If a state crosses a threshold, split it or disclose unresolved within-state mass. A representative score checks compatibility but does not identify the probability of a whole branch. Keep conditional-on-action probabilities distinct from unconditional win/loss/push/void probabilities.

## Top two and over/under assessment

G-L10 correction: derive the intersection q=P(A and B) from the joint outcome table. Verify max(0,pA+pB-1)<=q<=min(pA,pB). Compare q with pA*pB only within that same model and conditioning convention. If dependence is unspecified, publish those bounds and JOINT_UNQUANTIFIED instead of inventing an exact q or declaring independence. For two distinct total targets, P(at least one wins)=pA+pB-q; for more than two, enumerate the union without double counting.

An underdog handicap and Under are not inherently negatively dependent; an underdog rout can be short/low scoring, a favourite rout can be fast/high scoring, and close games can be slow. Similarly, an underdog tennis handicap can win in a short straight-set victory. Observing one winner and one loser on three cards does not establish a correlation. Treat the proposed coupling as a conditional mechanism to test.

Exactly one of an Over/Under half-line pair wins only when both contracts refer to the same completed target and have matching action/settlement conventions. Integer pushes, voids, shortened targets, retirements, and mismatched periods break an unconditional guarantee. Counting both sides is not evidence of successful selection. Freeze one preferred direction per distinct target before play; separately report rank 1, rank 2, both top two, preferred O/U, and at-least-one across distinct targets. Show both-row-graded and logically-decidable denominators; exclude unresolved/censored cases explicitly. Preserve losing and process-defective observations. No after-the-fact choice of a winning direction.

The prior phase-total/team-total-Under advantages are small, selected, mixed-population observations. They do not justify a general preference for those families. Compare fixed target families prospectively within competition, endpoint, line difficulty, and information horizon; use event clusters rather than treating complements as independent observations. Existing candidate manifests remain hypotheses.

## Sampling uncertainty and retrieval provenance

G-L11 correction: retrieve actual makes/attempts, exposure, dates, and roster regime before computing uncertainty. For independent binomial samples, a descriptive standard error for a difference is sqrt[p1(1-p1)/n1+p2(1-p2)/n2]. The sqrt(2) shortcut requires equal variances. Shot quality, player mix, repeated possessions, and game clustering may violate the binomial assumptions. Runs per innings, ERA, and strike rate are not binomial success proportions; do not apply the same formula to them. If denominators or dependence are unknown, record UNCERTAINTY_NOT_QUANTIFIED and show justified sensitivity rather than fabricate attempts.

Withdraw the automatic 'less than two SE means width only/mostly noise; greater means real' rule. A threshold does not establish either a causal effect or its absence. Report sample size, context, uncertainty, and any explicitly assumed shrinkage sensitivity. [NIST's proportion interval guidance](https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm) supports appropriate small-sample intervals; [the ASA statement](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) rejects mechanical threshold-only scientific conclusions. Both are methodology references, not sports-predictive features.

For P-371 specifically, the card had three Belgium games and four Germany games; it did not freeze attempt denominators. The old equal-75-attempt / 1.7-SE calculation cannot establish that the difference was mostly noise. The shooting reversal is an observed result, not evidence that its exact magnitude was forecastable.

Participant audit: record both teams' starters, bench/reserves, and coaches as separate fields, with exact evidence URL and publication/access time. Separate what the issued card captured from what a later box score now exposes. Nominated before the toss does not mean publicly retrievable before the forecast. Call a miss RETRIEVAL_MISS only when accessible publication before cutoff is evidenced; otherwise PUBLICATION_TIME_UNVERIFIED or NOT_RETRIEVED. Tennis benches are NOT_APPLICABLE; named coaching information can still be unknown. Do not label a combined lineup/bench/coaching check complete if one of those applicable fields is missing.

## Source and retrospective discipline

Resolve the exact event, date, competition round, team order, period, field, final status and source lineage after opening the URL. A search excerpt can refer to a different match from the opened page. Different hostnames, translations and proxies do not prove independent upstream scoring. Multiple secondaries cannot repair an unfrozen provider definition. A league-branded shell without the field is not evidence of zero.

Apply the existing MARKET_BLIND boundary to source content as well as to prices. P-364's mini log explicitly used a Sporting Life betting-tips/in-play-preview page for conditions; this was a source-selection breach of METHOD section 1. Preserve it as issued evidence, exclude that material from prospective inputs, and retrieve the original broadcaster/board/venue report for the sporting fact. Review PerformanceOdds, bookmaker, tipster and affiliate pages cited by other cards by claim; their names or availability do not make them approved research sources.

For a failed top pick, identify the target's first decisive checkpoint, actual score/phase facts, assumptions in the original card, what was demonstrably knowable, and plausible alternatives. A narrative listing a possible loss does not prove its probability was too low; a final score alone does not prove the causal story. Credit sound retrieval and successful target logic separately from wins forced by complementary pairs. Retain positive cases and limitations together. Validate candidate predictive changes on future data; do not claim that correcting the explanation would necessarily have changed the pick or made it win.


Current source/queue rechecks: [recent five rows](audit_2026-09-12/recent_queue_evidence.md), [historical nine rows](audit_2026-09-12/historical_queue_evidence.md), [source and sport details](audit_2026-09-12/sport_evidence.md). Every per-ID current status, from P-001: [complete chronological list](GAME_LOG_STATUS_CURRENT.md). Full integrated [audit report](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-12.md).


### Additional historical evidence tasks discovered 2026-09-12

The fourteen result-evidence follow-ups are unchanged. **Five separate TMP-AUDIT-20260912-01 through -05 tasks** now track the missing later corner adjudications for P-250/P-251/P-255/P-256/P-265. Their original forecasts and available retrospectives were recovered into Part 1; the absent P267 settlement artifact must not be treated as present. See [all current IDs and both queues](GAME_LOG_STATUS_CURRENT.md). Older settled labels on these five mean inherited closure, not independently reproduced field settlement.


### Latest state refresh - 2026-09-11 23:43 UTC / 2026-09-12 09:43 AEST

P-364 remains IN PROGRESS, at Day-3 stumps, not a final: Pakistan 133 and 449 all out (96.4), England 453. England's unstarted chase target is 130. [Cricbuzz exact commentary](https://www.cricbuzz.com/live-cricket-scores/129596/pak-vs-eng-3rd-test-pakistan-tour-of-england-2026) and [NDTV exact scorecard](https://sports.ndtv.com/cricket/eng-vs-pak-scorecard-live-cricket-score-pakistan-in-england-3-test-series-2026-3rd-test-enpk09092026264908) agree on the completed Pakistan innings and stumps state. Several official/venue pages still exposed Day-2 52/2, so they were not treated as the freshest state merely because they were official. PCB direct retrieval still failed. Ignore the sites' win-probability widgets. TMP-OPEN-20260911-03 stays open; the four already-graded ranked targets do not change. The earlier 233/4 snapshot below/elsewhere is historical, not the latest score. Recheck final on the next settlement request; no result is predicted or booked here.


## 2026-09-15 — `P-364` final settlement and queue retry (no new mini log supplied)

**LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** Method unchanged (`MDS-2026.09.06-v4.0`). Next canonical ID unchanged: **`P-372`**. Complete per-ID list from `P-001`: [`GAME_LOG_STATUS_CURRENT.md`](GAME_LOG_STATUS_CURRENT.md).

### Input inventory

No mini log was attached, none newer than the 2026-09-11 P-371 refresh exists in the local tree, and the Google Drive "Sports Research" folder (both result pages) holds only 2026-09-11 copies of framework documents. Whole-drive searches (`fullText contains 'P-372'`; `UNVALIDATED_SUBJECTIVE` modified after 2026-09-11 16:00 UTC; titles containing "mini") found no game log. **No card was imported, no canonical ID or temporary ID was created, and nothing was backfilled.**

### Live check and settlement

| Handle | Row | Evidence (2026-09-15 06:06 UTC) | Result |
|---|---|---|---|
| `TMP-OPEN-20260911-03` | `P-364` potential winner — England | ESPNcricinfo full scorecard (via `r.jina.ai`): "England won by 8 wickets"; Pakistan 133 & 449 (96.4); England 453 & 130/2 (24.2); Day 4, 12 Sep. Wikipedia corroborates (same lineage likely). The search-engine summary said "132 for 2" — **wrong; not used**. | **WIN — retired.** `P-364` is `FINAL / SETTLED`. Card Brier unchanged (0.3429, 4 ranked rows); winner labels are not Brier rows. |

**No live event remains.** Other open rows retried: ESPN `soccer/uae.*` (four slugs) HTTP 400 — no UAE Pro League route (`P-368-C02`, `P-369-C01` unchanged); `soccer/uga.1` still season 2025, 0 events on 2026-09-08 (`P-341-C03` unchanged); `P-342-C03` and the nine Part-2 rows not re-researched. **Open rows: 13.**

### Retrospective — `P-364` winner label and the ranked-row miss revisited

| Validation question | Answer |
|---|---|
| Confirmed starting and bench lineups, including coaches? | Both XIs **yes** (published Day 1, before the Day-2 cutoff); bench/reserves **NOT_RETRIEVED**; coaches **NOT_RETRIEVED**. Combined: **No**. Not decision-driving for either miss. |
| Sources accurate / newer sources needed? | Pre-issue facts accurate; the Sporting Life betting-tips preview remains a `MARKET_BLIND` breach (`L-20260912-08`). At settlement, only the opened scorecard was used; the search summary's score was wrong. New recommended route: ESPNcricinfo **series results page** via proxy for current-series priors. |
| Blindspots and how to account for them? | (1) Tempo prior not taken from England's own series innings records although the card cited them — **`G-L7` recurrence**; (2) winner label rested on a series aggregate and had no win/draw/loss mass or time budget — **`G-L1`**; (3) R1 complement not itemised — **`G-L9`**; (4) R1 and R2 were one thesis — **`G-L10`**. |

**Why the winner label went right:** a 320-run first-innings lead, the stronger attack, and enough time — the match ended on Day 4 despite about 27 overs lost on Day 2 and a 96.4-over Pakistan second innings. **What was not right in its reasoning:** the stated reason "Pakistan have failed to reach 200 in any innings" was an aggregate; Pakistan made 449. The draw branch was real and unquantified.

**Why Rank #1 and Rank #2 went wrong (evidence recovered this pass):** England's 2026-series innings run rates to the freeze were **4.55, 4.35, 3.83 — 907 runs in 210.8 overs = 4.30 an over** (ESPNcricinfo scorecards of the Leeds and Lord's Tests; the card cited the PCB versions). The phase row required 4.00. A signed restart slowdown against that record had no support; the restart was width. Both Unders shared this one thesis. This replaces the 2022-era averages the 2026-09-11 retrospective used, as the 2026-09-12 correction requested. One card does not show what the correct probability was (`L-087`).

### Rule changes and dispositions

| Change | Where |
|---|---|
| Cricket **control 27 evidence refresh**: Test phase prior = the batting side's current-series innings table (runs/overs/run rate) printed first. | `RULES_CRICKET.md` §"2026-09-15" |
| Cricket **control 28 (new, disclosure)**: every Test winner label prints win/draw/loss masses with overs-remaining (less a stated weather allowance) against overs the trailing side must survive, plus a 90+-over resistance branch; a series aggregate cannot substitute. | `RULES_CRICKET.md` §"2026-09-15" |
| Kill path: small-target chase early wicket cluster (England 2/2 after six balls). | `RULES_CRICKET.md` §"2026-09-15" |
| `G-L7` recurrence on a winner label; search-summary numeric error; no-mini-log inventory rule. | `LEARNING_REGISTER.md`, `SOURCES.md`, `METHOD.md`, `CONTROLS.md` §"2026-09-15" |
| **Cross-sport rule change: none.** One Test-cricket observation; the other nine sport files already carry `G-L1`/`G-L7`/`G-L9`/`G-L10`. Not editing them is a recorded decision. | this section |

### Scorecard and tallies (descriptive)

Running Brier **unchanged** — mixed 177 rows 0.2435; `PRIMARY_SCORED` 34 rows 0.2373, card count 8 / 25. `P-345`–`P-371` potential-winner labels: **14 / 26** (was 13 / 25 with one pending). No accuracy, ROI, edge or calibration claim follows.


## 2026-09-15(b) — `P-373`–`P-423` imported, settled, retrospected and audited (three external mini logs)

**LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** Method on every card: `MDS-2026.09.06-v4.0`. Issued forecasts are preserved verbatim in the archived raw logs; the settlement sections of logs A and B are appended below exactly as their external sessions wrote them (headings demoted one level), followed by this pass's log-C settlement, retrospectives, cross-log audit and rule dispositions. Full working file: the three updated mini logs archived in `archive/mini_logs/` (`…P373_P389_RETROSPECTIVE_SETTLED_2026-09-15.md`, `…P390_P406_RETROSPECTIVE_SETTLED_2026-09-15.md`, `…P407_P423_RETROSPECTIVE_SETTLED_2026-09-15.md`).

### Component fingerprints

The files appeared in the working folder at 2026-09-15 16:20–16:21 AEST, after the 2026-09-15(a) pass, together with byte-identical copies in `archive/mini_logs/originals_2026-09-15/`. A pre-change snapshot folder (`audit_2026-09-15/before/`) created at the same time was deleted on 2026-09-15 at the user's direction; only archived mini logs are kept outside the MD documents. Reconciled the same session — inside `METHOD.md` §10's 24-hour window.

| Log | File | Bytes | SHA-256 | Range | State on arrival |
|---|---|---:|---|---|---|
| A | `PREDICTION_MINI_RUNNING_LOG_P373_P389_RETROSPECTIVE_2026-09-12.md` | 294,562 | `640b33dc3bde39208a5596f479331537f0fbea9a4f66313d403021d753de8d41` | P-373–P-389 | settled 2026-09-12 by its session |
| A′ | `… 2026-09-12 (1).md` | 294,562 | identical to A | — | duplicate upload; not a second record — removed from the archive after the hash check |
| B | `PREDICTION_MINI_RUNNING_LOG_P390_P406_RETROSPECTIVE_2026-09-14.md` | 287,817 | `2f51d4561d2aa20440feb478a10fbc09b5b18b5f708fda26c738a620d7249dc5` | P-390–P-406 | settled 2026-09-14 by its session |
| C | `PREDICTION_MINI_RUNNING_LOG_THROUGH_P423.md` | 218,707 | `404903fc25c67b3ca74a86265aeed16127ce75c8a68f2cbbb2225f51278b7bbc` | P-407–P-423 | all unsettled |

### Canonical-ID reconciliation

| Item | Finding | Disposition |
|---|---|---|
| `P-372` | Never issued — log A started at P-373 by user instruction; logs B and C at P-390 and P-407 | **RESERVED / UNUSED.** Recorded in the register; never reused |
| `P-373`–`P-423` | No collision with any canonical ID (Part 3 ended at P-371) | Issued labels become canonical as issued |
| `P-374` Fenerbahçe v Roma | Same sporting event as the no-forecast collision record `TMP-SETTLED-20260911-01` | **P-374 is the canonical record** (a genuine pregame forecast); `TMP-SETTLED-20260911-01` and the external `TMP-RECON-20260912-01` are retired into it — not scored twice |
| `P-389`, `P-415` | No forecast issued (toss gate withheld; interrupted) | Administrative, non-scorable |
| Next ID | — | **`P-424`** |

### Live-state check (first step)

Every issued event in logs A, B and C had finished before this pass. **No event is live.** One card cannot be settled for an identity reason, not a live one: **P-418** (Drukpa v RTC) — the fixture is not verified as having been played (`TMP-OPEN-20260915-04`).

### Log C settlement tables (`P-407`–`P-423`)

#### P-407 — Settlement

**Event:** Club Brugge 3–1 Royal Antwerp (Jupiler Pro League MD6) · **Source:** ESPN soccer/bel.1 event 401878991 (goals 13', 19', 50', 78'; corners 9–4; both XIs + benches) · **Settled:** 2026-09-15 · **Population:** EXPLORATORY

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | Club Brugge team corners Over 4.5 | 0.78 | **PROVISIONAL — not booked** | — | ESPN (Opta lineage) 9 — PROVISIONAL WIN; the card's named provider (Pro League match centre) not reached |
| 2 | Royal Antwerp team goals Under 1.5 | 0.74 | **WIN** | 0.0676 | 1 goal |
| 3 | 1st Half total goals Over 0.5 | 0.72 | **WIN** | 0.0784 | 13' goal |
| 4 | Full match total goals Under 3.5 | 0.68 | **LOSS** | 0.4624 | 4 goals |
| 5 | Full match total goals Over 2.5 | 0.56 | **WIN** | 0.1936 | 4 goals |

**Potential winner:** Club Brugge 60% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.2005

**Retrospective:**
- *Driver:* Brugge's chance volume (23 shots, 9 on target) and an early goal took the match to four goals.
- *What went right:* the goal-process rows and the winner, built on current shots and xG.
- *What went wrong:* Under 3.5 (68%) was ranked above Over 2.5; both win only on exactly three goals, and four killed the higher row.
- *Knowable?* The 4+ family existed but its mass was not printed.
- *Smallest change:* print exact-goal masses (0, 1, 2, 3, 4+) whenever two overlapping totals are ranked (`G-L1`).

Rank #1 (Brugge corners Over 4.5, ESPN 9) is provisional — the named Pro League record was not reached. **Validation:** line-ups No (probable XIs only; coaches not named); sources accurate; blind spot = the exact-three overlapping state.

#### P-408 — Settlement

**Event:** Coventry City 0–5 Brighton & Hove Albion (EPL MW4) · **Source:** Premier League official data API, fixture 128956 (won_corners Brighton 3, Coventry 5); ESPN eng.1 401879282 agrees · **Settled:** 2026-09-15 · **Population:** PRIMARY_SCORED (EPL)

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | Brighton team corners Over 3.5 | 0.75 | **LOSS** | 0.5625 | 3 at the Premier League official record — lost by 0.5 |
| 2 | Brighton or Draw (90 min) | 0.74 | **WIN** | 0.0676 | Brighton won |
| 3 | 1st Half total goals Over 0.5 | 0.72 | **WIN** | 0.0784 | 35' goal |
| 4 | Coventry team goals Under 1.5 | 0.68 | **WIN** | 0.1024 | 0 |
| 5 | Full match total goals Over 2.5 | 0.55 | **WIN** | 0.2025 | 5 goals |

**Potential winner:** Brighton 48% · **CORRECT** · **Card mean Brier (5 graded rows):** 0.2027

**Retrospective:** Rank #1 lost — see the P-408 row of the deep Rank-#1 table below. Brighton led from 35' with 69% possession and 22 shots but won 3 corners; the card had noted the absence of Mitoma and Minteh and the early-lead kill path, yet trimmed the centre only to 5.4 (soccer control 33). Ranks 2–5 and the winner won. **Validation:** XIs and full benches yes; coaches not named (No); sources accurate (Premier League data is the field owner); blind spot = personnel-driven corner generation.

#### P-409 — Settlement

**Event:** Lille 2–0 Troyes (Ligue 1 MW4) · **Source:** ESPN soccer/fra.1 event 401876462 (goals 18', 90+3'; corners Lille 2, Troyes 5) · **Settled:** 2026-09-15 · **Population:** EXPLORATORY

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | Lille team goals Over 0.5 | 0.82 | **WIN** | 0.0324 | 2 |
| 2 | Troyes team corners Over 2.5 | 0.79 | **PROVISIONAL — not booked** | — | ESPN 5 — PROVISIONAL WIN; LFP official record not reached |
| 3 | Lille or Draw (90 min) | 0.76 | **WIN** | 0.0576 | Lille won |
| 4 | 1st Half total goals Over 0.5 | 0.70 | **WIN** | 0.09 | 18' goal |
| 5 | Full match total goals Under 3.5 | 0.65 | **WIN** | 0.1225 | 2 goals |

**Potential winner:** Lille 51% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.0756

**Retrospective:** every row landed (Troyes corners Over 2.5 provisional at ESPN 5). *What went right:* a direct corner process for the underdog (Troyes 6/5/11 corners for) instead of possession as a proxy. The unranked Over 2.5 (57%) lost, and the card correctly kept it out of the top five. **Validation:** XIs not retrieved and coaches not named (No); sources accurate; no material blind spot.

#### P-410 — Settlement

**Event:** RB Leipzig 5–0 Hamburger SV (Bundesliga MD3) · **Source:** ESPN soccer/ger.1 event 401884798 (goals 17', 28', 72', 74', 77'; corners 8–7) · **Settled:** 2026-09-15 · **Population:** EXPLORATORY

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | RB Leipzig team goals Over 0.5 | 0.88 | **WIN** | 0.0144 | 5 |
| 2 | RB Leipzig or Draw (90 min) | 0.86 | **WIN** | 0.0196 | won |
| 3 | Hamburger SV team goals Under 1.5 | 0.82 | **WIN** | 0.0324 | 0 |
| 4 | 1st Half total goals Over 0.5 | 0.76 | **WIN** | 0.0576 | 17' goal |
| 5 | RB Leipzig team corners Over 4.5 | 0.68 | **PROVISIONAL — not booked** | — | ESPN 8 — PROVISIONAL WIN; DFL/Bundesliga record not reached |

**Potential winner:** RB Leipzig 64% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.0310

**Retrospective:** all graded rows won (Leipzig corners provisional at ESPN 8). *What went right:* xG suppression of HSV (0.89 xG in two games) and current first-half evidence; the unranked Over 2.5 (59%) also won. **Validation:** XIs not retrieved and coaches not named (No); sources accurate; no material blind spot.

#### P-411 — Settlement

**Event:** Spain (W) 81–58 Germany (W) (FIBA Women's World Cup bronze, Berlin) · **Source:** FIBA game 128154-ESP-GER (quarters 25-15, 15-21, 21-15, 20-7; no OT; Spain biggest lead 26) · **Settled:** 2026-09-15 · **Population:** EXPLORATORY

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | Germany (W) +6.5 | 0.56 | **LOSS** | 0.3136 | lost by 23 |
| 2 | Under 147.5 | 0.53 | **WIN** | 0.2209 | 139 |
| 3 | Over 147.5 | 0.47 | **LOSS** | 0.2209 | 139 |
| 4 | Spain (W) -6.5 | 0.44 | **WIN** | 0.3136 | won by 23 |

**Potential winner:** Spain 60% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.2672

**Retrospective:** Rank #1 lost — see the P-408–P-423 deep table below. The card discarded the same-tournament Spain 83–53 meeting and centred Spain at +5.2; Spain won by 23 (basketball control 25, `G-L12`). **Validation:** starting fives not confirmed (No); sources accurate; blind spot = discarding current evidence.

#### P-412 — Settlement

**Event:** Pittsburgh Steelers 20–13 Atlanta Falcons (NFL Week 1) · **Source:** ESPN football/nfl event 401872658 (final, no OT) · **Settled:** 2026-09-15 · **Population:** EXPLORATORY

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | Atlanta Falcons +6.5 | 0.55 | **LOSS** | 0.3025 | lost by 7 — missed by 0.5 |
| 2 | Under 40.5 | 0.53 | **WIN** | 0.2209 | 33 |
| 3 | Over 40.5 | 0.47 | **LOSS** | 0.2209 | 33 |
| 4 | Pittsburgh Steelers -6.5 | 0.45 | **WIN** | 0.3025 | won by 7 |

**Potential winner:** Pittsburgh 66% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.2617

**Retrospective:** Rank #1 lost at exactly 7 — a half-point boundary loss on a 23-line card with no margin-family table and no key-number mass (American football control 18). **Validation:** partial line-ups (No); sources accurate; blind spot = the missing margin table.

#### P-413 — Settlement

**Event:** Baltimore Ravens 41–23 Indianapolis Colts (NFL Week 1) · **Source:** ESPN football/nfl event 401872659 (final, no OT) · **Settled:** 2026-09-15 · **Population:** EXPLORATORY

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | Indianapolis Colts +3.0 (53% win / 8% push / 39% loss) | 0.53 | **LOSS** | 0.2809 | lost by 18 |
| 2 | Under 48.5 | 0.52 | **LOSS** | 0.2704 | 64 |
| 3 | Over 48.5 | 0.48 | **WIN** | 0.2704 | 64 |
| 4 | Baltimore Ravens -3.0 (39 / 8 / 53) | 0.39 | **WIN** | 0.3721 | won by 18 |

**Potential winner:** Baltimore 56% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.2984

**Retrospective:** Ranks #1 and #2 lost together. The centre was BAL +1.3; the Colts' prior came from a hand-picked 2025 window; one "controlled game" thesis set both rows (`G-L12`, `L-011`, `G-L10`; American football controls 17 and 19). **Validation:** depth charts, inactives and coaching captured (Partial); sources accurate; blind spots = the centre shrink and the selected window.

#### P-414 — Settlement

**Event:** Buffalo Bills 36–31 Houston Texans (NFL Week 1) · **Source:** ESPN football/nfl event 401872660 (final, no OT) · **Settled:** 2026-09-15 · **Population:** EXPLORATORY

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | Houston Texans +1.5 | 0.55 | **LOSS** | 0.3025 | lost by 5 |
| 2 | Under 44.5 | 0.53 | **LOSS** | 0.2809 | 67 |
| 3 | Over 44.5 | 0.47 | **WIN** | 0.2809 | 67 |
| 4 | Buffalo Bills -1.5 | 0.45 | **WIN** | 0.3025 | won by 5 |

**Potential winner:** Buffalo 53% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.2917

**Retrospective:** Ranks #1 and #2 lost together. Houston's 2025 defensive baseline set both a margin compressor (BUF +0.7) and a total suppressor (44.1); the actual was 67 points, Buffalo by 5 (`G-L12`, `G-L2`, `G-L10`; American football control 19). **Validation:** both inactive lists and coaching captured (Partial → nearly complete); sources accurate; blind spot = one thesis driving both top rows.

#### P-415 — Administrative

Not issued (interrupted before any forecast). Nothing is graded or reconstructed.

#### P-416 — Settlement

**Event:** New York Yankees 2–0 New York Mets (MLB; wet-grounds delayed start) · **Source:** MLB statsapi gamePk 823495 (8.5 innings; Schlittler 6.0 IP 0 R; Scott 6.0 IP 2 R) · **Settled:** 2026-09-15 · **Population:** PRIMARY_SCORED (MLB)

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | Under 8.0 (52 / 11 / 37) | 0.52 | **WIN** | 0.2304 | 2 runs |
| 2 | Mets +1.5 | 0.51 | **LOSS** | 0.2601 | lost by 2 |
| 3 | Yankees -1.5 | 0.49 | **WIN** | 0.2601 | won by 2 |
| 4 | Over 8.0 (37 / 11 / 52) | 0.37 | **LOSS** | 0.1369 | 2 runs |

**Potential winner:** NY Yankees 63% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.2219

**Retrospective:**
- *Driver:* Schlittler's six scoreless innings.
- *What went right:* Under 8.0 and the winner; the delay was treated as a state.
- *What went wrong:* Mets +1.5 lost by two — central on the card's own 1.4-run centre and 3.8-run width.
- *Smallest change:* print P(favourite by 2+) before ranking a +1.5 (baseball control 29).

**Validation:** secondary posted orders, managers not named (No); sources accurate; blind spot = the run-line decomposition.

#### P-417 — Settlement

**Event:** Chunichi Dragons 6–0 Hanshin Tigers (NPB Central League, Koshien) · **Source:** NPB official box s2026091401939 (9 innings; Muller complete-game shutout, 4 H, 7 K; Itoh 5 IP 4 R; HR Hosokawa, Muller) · **Settled:** 2026-09-15 · **Population:** EXPLORATORY

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | Chunichi Dragons +1.5 | 0.62 | **WIN** | 0.1444 | won by 6 |
| 2 | Under 5.5 | 0.55 | **LOSS** | 0.3025 | 6 runs — all Chunichi |
| 3 | Over 5.5 | 0.45 | **WIN** | 0.3025 | 6 |
| 4 | Hanshin Tigers -1.5 | 0.38 | **LOSS** | 0.1444 | lost |

**Potential winner:** Hanshin 55% · **WRONG** · **Card mean Brier (4 graded rows):** 0.2234

**Retrospective:**
- *Driver:* Muller's nine-inning shutout.
- *What went right:* Dragons +1.5 — the card printed Muller's stronger profile.
- *What went wrong:* the winner label defaulted to the home side, and Under 5.5 lost at 6 with all runs by one team.
- *Smallest change:* derive the label from the printed starter asymmetry, and give the one-team total branch mass (`G-L9`).

**Validation:** starters probable (correct), orders not recovered (No); sources accurate; blind spot = the home-side default.

#### P-418 — OPEN (identity/state conflict; `TMP-OPEN-20260915-04`)

**Not settled — no W/L, no Brier.**
- The Bhutan Broadcasting Service round report dated 2026-09-15 lists BFF Academy U-20 2–2 Drukpa and RTC 3–3 Tsirang, and no Drukpa–RTC match.
- The Bhutan Football Federation listing shows an undated RTC 1–1 Drukpa report.
- ESPN `bhu.1` returns HTTP 400; Sofascore and AiScore returned HTTP 403.

**Blind spot:** `G0` was passed on aggregator listings that disagreed with each other while the club schedule was stale → `RULES_GENERAL.md` §16.10(i). **Validation:** XI not retrieved, both coaches named (No); fixture sources unreliable. **Retry:** a dated BFF/BBS fixture or report naming Drukpa's opponent for 13–15 September.

#### P-419 — Settlement

**Event:** Djurgårdens IF 2–0 GAIS (Allsvenskan MW21) · **Source:** ESPN soccer/swe.1 event 401873992 (goals 35', 63'; corners 2–2) · **Settled:** 2026-09-15 · **Population:** EXPLORATORY

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | Djurgården team goals Over 0.5 | 0.84 | **WIN** | 0.0256 | 2 |
| 2 | Djurgården or Draw (1X) | 0.83 | **WIN** | 0.0289 | won |
| 3 | GAIS team goals Under 1.5 | 0.79 | **WIN** | 0.0441 | 0 |
| 4 | Under 3.5 total goals | 0.70 | **WIN** | 0.09 | 2 |
| 5 | Total corners Over 7.5 (self-generated alternate) | 0.69 | **PROVISIONAL — not booked** | — | ESPN 4 — PROVISIONAL LOSS; Allsvenskan record not reached |

**Potential winner:** Djurgården 60% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.0471

**Retrospective:** ranks 1–4 won on home chance creation; the unranked 1H Over 0.5 (62%) and Under 2.5 (51%) also won. *What went wrong:* a 69% self-generated corner alternate without a per-team corner table (provisional at ESPN 4; soccer control 23). **Validation:** XIs not retrieved and coaches not named (No); sources accurate; blind spot = the ungrounded derivative alternate.

#### P-420 — Settlement

**Event:** Chicago Cubs 7–3 Atlanta Braves (MLB, Wrigley Field) · **Source:** MLB statsapi gamePk 824629 (López 3.0 IP 5 ER; Peterson 6.0 IP 1 ER) · **Settled:** 2026-09-15 · **Population:** PRIMARY_SCORED (MLB)

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | Atlanta Braves +1.5 | 0.57 | **LOSS** | 0.3249 | lost by 4 |
| 2 | Over 9.5 | 0.53 | **WIN** | 0.2209 | 10 |
| 3 | Under 9.5 | 0.47 | **LOSS** | 0.2209 | 10 |
| 4 | Chicago Cubs -1.5 | 0.43 | **WIN** | 0.3249 | won by 4 |

**Potential winner:** Chicago Cubs 56% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.2729

**Retrospective:** Rank #1 lost. López lasted 3.0 IP (5 ER) after the card had printed his IL-return ladder and "López return collapses" as its first kill path, yet the card centred the margin at Cubs +0.3 (baseball control 29(c), `G-L9`, `G-L12`). **Validation:** orders with source limitation, managers not named (No); sources accurate; blind spot = hook risk kept out of the centre.

#### P-421 — Settlement

**Event:** New York Yankees 8–3 Minnesota Twins (MLB) · **Source:** MLB statsapi gamePk 823656 (NYY six-run 8th; Warren 5.2 IP 0 ER; Kremer 5.2 IP 1 ER) · **Settled:** 2026-09-15 · **Population:** PRIMARY_SCORED (MLB)

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | New York Yankees -1.5 | 0.52 | **WIN** | 0.2304 | won by 5 |
| 2 | Over 8.0 (50 / 12 / 38) | 0.50 | **WIN** | 0.25 | 11 |
| 3 | Minnesota Twins +1.5 | 0.48 | **LOSS** | 0.2304 | lost by 5 |
| 4 | Under 8.0 (38 / 12 / 50) | 0.38 | **LOSS** | 0.1444 | 11 |

**Potential winner:** NY Yankees 65% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.2138

**Retrospective:** the top two both won. *What went right:* official starter identity over stale "Ober" previews, and the Twins' lineup deficit carried with a named mechanism. The Over was decided by one late inning (baseball control 19). **Validation:** partial order, managers not named (No); sources accurate; no material blind spot.

#### P-422 — Settlement

**Event:** Kansas City Chiefs 31–10 Denver Broncos (NFL Week 1) · **Source:** ESPN football/nfl event 401872931 (final, no OT) · **Settled:** 2026-09-15 · **Population:** EXPLORATORY

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | Denver Broncos +2.5 | 0.56 | **LOSS** | 0.3136 | lost by 21 |
| 2 | Under 42.5 | 0.53 | **WIN** | 0.2209 | 41 |
| 3 | Over 42.5 | 0.47 | **LOSS** | 0.2209 | 41 |
| 4 | Kansas City Chiefs -2.5 | 0.44 | **WIN** | 0.3136 | won by 21 |

**Potential winner:** Kansas City 54% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.2672

**Retrospective:** Rank #1 lost by 21. The Mahomes ACL uncertainty moved the centre to KC +1.0 instead of only widening it, and the margin width was ~10.5 against a published NFL residual SD of ≈13.9 (`G-L12`; American football controls 17 and 18). **Validation:** depth charts and Denver inactives captured (Partial); sources accurate; blind spot = the centre shrink.

#### P-423 — Settlement

**Event:** San Diego Padres 8–7 Colorado Rockies (MLB, Coors Field) · **Source:** MLB statsapi gamePk 824308 (Mize 5.0 IP 2 ER; Sugano 5.0 IP 6 ER) · **Settled:** 2026-09-15 · **Population:** PRIMARY_SCORED (MLB)

| Rank | Contract | `p` | Result | Brier | Boundary / note |
|---:|---|---:|---|---:|---|
| 1 | San Diego Padres -1.5 | 0.54 | **LOSS** | 0.2916 | won by 1 |
| 2 | Over 11.0 (48 / 10 / 42) | 0.48 | **WIN** | 0.2704 | 15 |
| 3 | Colorado Rockies +1.5 | 0.46 | **WIN** | 0.2916 | lost by 1 |
| 4 | Under 11.0 (42 / 10 / 48) | 0.42 | **LOSS** | 0.1764 | 15 |

**Potential winner:** San Diego 66% · **CORRECT** · **Card mean Brier (4 graded rows):** 0.2575

**Retrospective:** Rank #1 lost by one run. A road −1.5 at Coors with the home side batting last; the exactly-one-run mass (≈12%) was implied but not printed, although "home-last-bat rally" was a named kill path (baseball control 29(b)). The Over, Rockies +1.5 and the winner won. **Validation:** Colorado order corroborated, San Diego partial (No); sources accurate; blind spot = the unprinted one-run mass.

### Log C (`P-407`–`P-423`) — retrospectives, validation answers and deep Rank-#1 reviews

Every row above was graded on 2026-09-15 against the source named in its block (field owner where reachable; ESPN / MLB statsapi / NPB / FIBA structured records otherwise). Probabilities, ranks and wording are the issued ones — nothing was re-ranked. **Learning-only / not performance-eligible.**

#### Participant capture — confirmed starters, bench/reserves and coaches (as printed on each issued card)

"Yes" means the card itself printed the field for both sides from a source available before its freeze. Later box scores (ESPN rosters exist for every soccer match) are **not** backdated as pre-game capture; their publication time before the freeze is `PUBLICATION_TIME_UNVERIFIED`.

| ID | Both starting line-ups | Bench / reserves / inactives | Both coaches / managers | Combined answer |
|---|---|---|---|---|
| P-407 | No — probable XIs only (`XI_NOT_RETRIEVED_BEFORE_FREEZE`) | No | Not named | **No** |
| P-408 | Yes — both unchanged XIs | Yes — both full benches listed | Not named | **No** (coaches missing) |
| P-409 | No | No | Not named | **No** |
| P-410 | No | No | Not named | **No** |
| P-411 | No — bronze-game starting fives not confirmed | Final 12s both sides (yes) | Not named in the card text | **No** |
| P-412 | Starting QBs and key injuries (partial; 23-line card) | Not demonstrated | Not named | **No** |
| P-413 | Depth charts + key inactives (Ravens full; Colts partial) | Inactives partial | Yes (card marks coaching/scheme transitions PASS; Minter named) | **Partial** |
| P-414 | Depth charts / OL core | Both inactive lists printed | Yes (coaching transition PASS; Brady named) | **Partial → nearly complete** |
| P-416 | Posted orders from secondary threads; starters official | Not demonstrated | Not named | **No** |
| P-417 | Starters probable (correct); orders not recovered | Not recovered | Not named | **No** |
| P-418 | No — no trustworthy XI, GK or bench | No | Yes — Dorji Khandu (Drukpa), Ugyen Dorji (RTC) from BFF | **No** |
| P-419 | No (official squad due one hour pre-kick not exposed) | No | Not named | **No** |
| P-420 | Orders "pass with source limitation" | Not demonstrated | Not named | **No** |
| P-421 | Order partial (Caballero/Volpe conflict preserved) | Not demonstrated | Not named | **No** |
| P-422 | Depth charts; QB status | Denver inactives printed; KC partial | Broncos staff and KC OC named; KC head coach not printed | **Partial** |
| P-423 | Colorado order corroborated; San Diego partial | Not demonstrated | Not named | **No** |

**Answer:** complete starters + bench + coaches for both teams were captured on **0 of 16** issued log-C cards; P-414 came closest. Soccer XIs are published about an hour before kick-off and the cards froze 2–8 minutes before kick-off, so most soccer misses are probably `RETRIEVAL_MISS`, but publication time was not proven, so they stay `PUBLICATION_TIME_UNVERIFIED`. None of the eight Rank-#1 losses turned on a missing name; the NFL and MLB losses turned on margin distributions (below).

#### Were the sources accurate?

- **Accurate on every fact that was checked at settlement.** All four MLB starters matched MLB's box scores (Scott/Schlittler, López/Peterson, Warren/Kremer — P-421 correctly rejected stale "Bailey Ober" previews — and Mize/Sugano). NPB's Itoh v Muller (P-417, marked "probable") was correct. Every soccer final agreed with ESPN, and P-408's corner count agreed with the Premier League's own data.
- **Inaccurate or weak:** P-418's fixture listing (see its block); P-416's lineups came from fan "game threads" (secondary); P-407's absence list came from a lower-tier predicted-lineup page (the card preserved the conflict — good).
- **Newer / better sources found this pass:** the **Premier League official data API** (field owner for EPL corners, shots and XIs), ESPN `wonCorners` for Belgium, France, Germany, Sweden, Spain, Italy and Japan, MLB statsapi box scores for starter lines, BBS (Bhutan Broadcasting Service) round reports. Details in the sources section.

#### Per-card retrospectives (three questions + what went right)

*Each card's retrospective and validation answers now also sit directly under its settlement table above; the fuller text is kept here.*

**P-407 Club Brugge 3–1 Antwerp.** *Driver:* Brugge's chance volume (23 shots, 9 on target) and an early goal; the match went to four goals. *Right:* the goal-process rows (Antwerp Under 1.5, first-half Over, Over 2.5) and the winner. *Wrong:* Under 3.5 (68%) — the card ranked Under 3.5 above Over 2.5 and said both "win on exactly three"; four goals killed the higher row. *Knowable?* The four-goal family existed on the card but its mass was not printed per state. *Smallest change:* print the exact-goal masses (0,1,2,3,4+) whenever two overlapping totals are ranked, and check that `P(U3.5) − P(O2.5 ∧ U3.5)` is coherent with the 4+ mass (`G-L1`). Rank #1 (Brugge corners Over 4.5, ESPN 9) is provisional — the named Pro League record was not reached.

**P-408 Coventry 0–5 Brighton — Rank #1 LOST (deep review below).** Rows 2–5 all won; winner correct.

**P-409 Lille 2–0 Troyes.** All five graded/provisional rows landed (Troyes corners Over 2.5 provisional at ESPN 5). *Right:* a direct corner process for the underdog (Troyes 6/5/11 corners for) rather than possession as a proxy; home goal row at 82%. *Note:* the unranked supplied Over 2.5 (57%) lost — the card correctly kept it out of the top five because the exact-3 state favoured Under 3.5. Grade: good process.

**P-410 RB Leipzig 5–0 Hamburger SV.** All graded rows won; Leipzig corners Over 4.5 provisional at ESPN 8. The unranked Over 2.5 (59%) also won. *Right:* xG-based suppression of HSV (0.89 xG in two games) and first-half early-goal evidence. Grade: good process.

**P-411 Spain (W) 81–58 Germany (W) — Rank #1 LOST (deep review below).** Under 147.5 (Rank #2) won; winner Spain correct.

**P-412 Pittsburgh 20–13 Atlanta — Rank #1 LOST (deep review below).** Under 40.5 won; winner correct.

**P-413 Baltimore 41–23 Indianapolis — Rank #1 and Rank #2 LOST (deep review below).** Winner correct.

**P-414 Buffalo 36–31 Houston — Rank #1 and Rank #2 LOST (deep review below).** Winner correct.

**P-416 Yankees 2–0 Mets.** *Driver:* Schlittler six scoreless innings; the Yankees needed only two runs. *Right:* Under 8.0 (Rank #1) and the winner; the wet-grounds delay was handled as a state, not as information. *Wrong:* Mets +1.5 (51%) lost by two. *Knowable?* A 1.4-run centre and a 2.01-ERA starter made a two-run Yankees win a central state; the card's own margin width (3.8) put most of the Yankees-win mass at 2+. *Smallest change:* the `G-L12` run-line decomposition — print P(favourite by 2+) before ranking a +1.5.

**P-417 Chunichi 6–0 Hanshin (NPB).** *Driver:* Kyle Muller's nine-inning shutout; two two-run homers. *Right:* Dragons +1.5 (Rank #1, 62%) — the card said Muller had "the stronger" profile (6.4 IP/start v Itoh 5.1). *Wrong:* Under 5.5 lost at exactly 6, all scored by Chunichi (two in the 9th); the winner label chose Hanshin (55%) despite that starter asymmetry. *Knowable?* Yes — the starter asymmetry was on the card; the favourite-only (here underdog-only) total branch was not given mass. *Smallest change:* when the stronger starter is on the road side, the winner label must show its arithmetic from the starter asymmetry rather than defaulting to the home side; add the one-team-only total branch (`G-L9`).

**P-418 Drukpa v RTC (Bhutan) — NOT SETTLED: identity/state conflict.** The card itself recorded a fixture-time conflict (AiScore/Sofascore 12:00 UTC, TNT 13:00 UTC) and a stale Drukpa club schedule that omitted the fixture. At settlement: (1) the Bhutan Broadcasting Service round report dated **2026-09-15** lists the concluding first-round results as Paro 5–1 Thimphu, Thimphu City 4–0 Tensung, Transport United 1–0 Ugyen Academy, **RTC 3–3 Tsirang** and **BFF Academy U-20 2–2 Drukpa** — no Drukpa–RTC match; (2) the Bhutan Football Federation's own report list shows an RTC 1–1 Drukpa draw, but undated on the listing (most likely the earlier first-round meeting); (3) ESPN has no Bhutan route (`bhu.1` HTTP 400); Sofascore and AiScore returned HTTP 403. **Disposition:** `IDENTITY_STATE_CONFLICT — UNRESOLVED`, handle `TMP-OPEN-20260915-04`; no W/L, no Brier. *Blindspot:* the identity gate (`G0`) was treated as satisfied on aggregator fixture listings that disagreed with each other while the club's own schedule was stale. *Smallest change:* in sparse competitions, confirm the exact fixture with the federation or national broadcaster before issue, or fail closed (`RULES_GENERAL.md` §16.10(i)). Retry trigger: a dated BFF/BBS report or fixture list for 13–15 September naming Drukpa's opponent.

**P-419 Djurgården 2–0 GAIS.** Ranks 1–4 won (home goals, 1X, GAIS Under 1.5, Under 3.5); the unranked 1H Over 0.5 (62%, 35' goal) and Under 2.5 (51%) also won. The self-generated corners Over 7.5 (69%) is provisional at ESPN **4** — far from the line. *Wrong:* a 69% corner alternate that the card generated itself, in a match whose two sides took 2 corners each. *Knowable?* Partly — no per-team corner-for/against table for these two sides was printed in the extracted card. *Smallest change:* self-generated derivative alternates follow the same `SO-P3` provider and exposure chain as supplied rows; without both, they are not ranked (soccer control 23).

**P-420 Cubs 7–3 Braves — Rank #1 LOST (deep review below).** Over 9.5 (Rank #2) won; winner correct.

**P-421 Yankees 8–3 Twins — top two both won.** *Driver:* a six-run Yankees 8th after a 1–2 game. *Right:* official starter identity over stale previews (Kremer, not Ober); the Twins lineup deficit (Buxton out, Lewis limited) carried as −0.35 with a named mechanism; Over 8.0 push mass printed (12%). *Knowable?* The late-bullpen cluster was a branch on the card. Grade: good process. *Note:* the Over was won by a single inning — a reminder that full-game totals are decided late (baseball control 19).

**P-422 Kansas City 31–10 Denver — Rank #1 LOST (deep review below).** Under 42.5 (Rank #2) won at 41; winner correct.

**P-423 Padres 8–7 Rockies — Rank #1 LOST by one run (deep review below).** Over 11.0 and Rockies +1.5 won; winner correct.

**P-415 Angels @ Nationals.** Not issued (interrupted before any forecast). Administrative; nothing to grade.

#### Deep Rank-#1 reviews (required whenever Rank #1 loses)

| ID | First decisive checkpoint | What went right | What went wrong | Actual mechanism | Was it knowable, and on the card? | Improvement (and earlier lesson) | Grade |
|---|---|---|---|---|---|---|---|
| **P-408** Brighton team corners O3.5 (75%) | Full time: 3 corners (Premier League official) | Rows 2–5 and the winner; both XIs and benches captured; honest n=3 standard error printed | A 75% row on a 3-game corner sample, while the card itself said Brighton had lost Mitoma and Minteh (its natural width) and that an early lead cuts later territory | Brighton led from 35', held 69% possession and took 22 shots but won only **3 corners** (Coventry 5): central combination play plus a leading state | **Yes** — both kill paths were printed with a combined 25% complement; the personnel loss was noted but only trimmed the centre from 6.3 to 5.4 | New soccer control 33: recompute a team-corner centre from the players who generate corners when they are absent, and give the leading-state branch its own mass. Links: `G-L7` (per-player corner generation was available), `G-L9`, soccer controls 4/21 (corners ≠ goals, cf. P-402 0–0 with 11 corners) | C |
| **P-411** Germany +6.5 (56%) | Q4: Spain 20–7 (score 61–51 after three quarters) | Under 147.5 and the winner; final 12s, availability (Peterson illness resolved) | The card explicitly set aside the same-tournament meeting 10 days earlier (**Spain 83–53**) as an extreme-shooting outlier and centred Spain at +5.2 | Spain's pressure and a 15–0 run; Germany shot 31.8% from three; Q4 20–7 for an 81–58 (+23) finish | **Yes** — "Spain pressure recreates the opener's separation" was the first named kill path, inside a 44% complement | Basketball control 25 (new): a same-competition, same-roster meeting is current evidence; decompose it (shooting v possession/turnover/rebound) and give the separation family mass rather than discarding it. Cross-sport `G-L12`. Mirror of P-371, where Germany beat a favoured Belgium by 19 | C |
| **P-412** Falcons +6.5 (55%) | Full time: Pittsburgh by exactly **7** | Under 40.5 (33) and the winner; Cooper Rush / QB-injury state correct | 23-line card: no margin-family table, no key-number mass | A one-score game decided by a touchdown margin | Partly — the centre (PIT +6) was near the line; the loss is a half-point boundary on the most important NFL margin after 3 | American-football control 18 (new): print the exact masses at 3 and 7 for every NFL handicap row; a card without a margin table caps the handicap row at `FORCED RANK` (`G-L1`) | C+ (boundary) |
| **P-413** Colts +3.0 (53/8/39) | Half-time 31–13 Baltimore | Winner Baltimore; push mass at exactly 3 printed (8%); new HC/OC/center held as width | Centre BAL +1.3 on a 56% winner; the Colts' prior used **their first 10 games of 2025 with a healthy Jones** (57.6% scoring possessions) — a selected window; Under 48.5 shared the same "competitive, controlled game" thesis | Baltimore 31 first-half points; 64 total | Partly — "Lamar/Henry explosive separation" was named inside a 39% loss mass, but the 14+ family carried only 12% | `G-L12` (centre not pulled to pick'em; favourite-separation mass printed with its source); `L-011`/`G17` (a hand-picked best window is a streak, not a prior); `G-L10` (R1 and R2 positively coupled — one thesis) | D+ |
| **P-414** Texans +1.5 (55%) | Half-time Buffalo 24–21, then 36–31 | Winner Buffalo; both inactive lists; coaching transition | Houston's **2025 defensive baseline** carried into Week 1 as both a margin compressor and a total suppressor; centre BUF +0.7, total 44.1 | Both offences scored freely (67 points); Buffalo by 5 | Partly — "both QBs efficient" was named, but the defence thesis set the direction of both top rows | `G-L12` + `G-L2`: a prior-season unit rating in a new season is width; `G-L10`: print P(R1 ∧ R2) — both rows needed the same low-event game | D+ |
| **P-420** Braves +1.5 (57%) | Top 3rd: López done after 3.0 IP, 5 ER | Over 9.5 (10) and the winner; the card retrieved López's return ladder (rehab 5 scoreless; return 4.2 IP, 6 ER) | Margin centre **Cubs +0.3** despite printing "López return collapses" as the first kill path and a Sep 9 6-ER return start | Early hook, Cubs 5–0 after three; Peterson 6 IP 1 ER | **Yes** — the ladder and the hook branch were on the card; the complement (43%) had to hold hook + power cluster + Atlanta relief exposure | Baseball control 29 (new): a +1.5 on a recent IL-return starter prints the early-hook branch mass and P(opponent by 2+) separately. Links: control 25 (rehab ladder, P-335), `G-L9` | C |
| **P-422** Broncos +2.5 (56%) | Q3: Kansas City 17–7 → 27–10 | Under 42.5 (41) and the winner; Mahomes' ACL return treated as a two-sided branch | Centre **KC +1.0** on a 54% winner: the Mahomes uncertainty was applied to the centre (toward Denver), not only to width | Kansas City by 21 at home | Partly — "Mahomes fully mobile" was the first named kill path; its mass was not separated from the one-score families | `G-L12`; existing American-football control 16 ("new-regime uncertainty is two-sided") was cited but applied as a centre shrink | D+ |
| **P-423** Padres −1.5 (54%) | Bottom 9th: Colorado within one | Over 11.0 (15), Rockies +1.5 and the winner; Mize identity confirmed over stale TBD pages | A road −1.5 at Coors where the home side bats last; the exactly-one-run Padres-win mass was implied (≈12%) but not printed | Padres led 6–1, Colorado scored in the 6th–8th; SD by 1 | Yes — "Colorado home-last-bat rally" was a named kill path | Baseball control 29(b): print the road favourite's exactly-one-run mass for any −1.5 at a high-scoring park | B− (boundary) |

**What the eight losses share.** Five were underdog cushions whose favourite won by more than the line (P-411, P-413, P-414, P-420, P-422), one was a cushion lost at a key number (P-412), one a boundary favourite run line (P-423), and one a derivative (P-408). In every NFL/MLB/basketball case the printed margin **centre sat within 1.5 points/runs of zero** while the same card's winner label favoured the eventual winner — the uncertainty had been turned into a signed lean toward the underdog. That is the `G-L2` failure mirrored onto the margin, and it is the basis of `G-L12`.

### Log A settlement and retrospective sections (verbatim from the external session, 2026-09-12)

#### P-373 — Tampa Bay Rays @ Atlanta Braves — MLB — 2026-09-10 (Atlanta local)


**Verified final / endpoint:** Atlanta Braves 3–1 Tampa Bay Rays.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **Tampa Bay Rays +1.5** | 65% `UNVALIDATED_SUBJECTIVE` | **LOSS** | Atlanta won by 2 | 0.4225 |
| 2 | **Under 8.5 runs** | 56% `UNVALIDATED_SUBJECTIVE` | **WIN** | 4 total runs | 0.1936 |
| 3 | **Over 8.5 runs** | 44% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 4 total runs | 0.1936 |
| 4 | **Atlanta Braves -1.5** | 35% `UNVALIDATED_SUBJECTIVE` | **WIN** | Atlanta won by 2 | 0.4225 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.3080**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Atlanta Braves — issued 51% `UNVALIDATED_SUBJECTIVE` — **WIN** — Brier **0.2401**.

**Process grade:** `MIXED — RESULT-MARGIN / LATE-BULLPEN-SEPARATION MISS`

**What went right.** The starter-led run-suppression thesis was directionally right. The game finished with only four runs, and the Braves winner lean also landed. Martinez kept Tampa competitive for most of the game, so the forecast correctly rejected a simplistic early Atlanta blowout.

**What went wrong.** Rank #1 failed because the +1.5 cushion did not survive the late separation. The 8.3-run centre was also too high relative to the four-run actual, even though the Under direction won.

**Actual mechanism / kill-path audit.** The decisive branch was a late Atlanta scoring cluster rather than a Martinez collapse. Pérez delivered seven scoreless innings; the game stayed compressed until Atlanta created a three-run bottom eighth, and Tampa's ninth-inning solo run left the final margin at two. The original kill path explicitly named Tampa's reduced bullpen depth, but that state did not carry enough mass against Rank #1.

**Knowability / source-quality audit.** The existence of Tampa bullpen attrition and the possibility of late separation were knowable pregame. The exact eighth-inning cluster was not. This is therefore mainly a branch-mass / margin-distribution issue, not a missing-result-data issue.

**Learning disposition.** For baseball +1.5 rows, a strong-starter/low-total story must still price the post-starter separation family independently. Do not let 'close for six or seven innings' stand in for 'final margin ≤1'. Reinforce the existing `RULES_BASEBALL.md` cushion decomposition and score-state bullpen-transition controls; no new coefficient.

**Post-result sources added in this settlement pass**
- MLB official game/box-score record — final 3–1 and inning sequence.
- MLB/Braves postgame material — Pérez seven scoreless innings and late Atlanta scoring sequence.


##### 2026-09-15 canonical settlement audit — P-373

- **Final re-verified:** MLB statsapi 824872 (3–1).
- **Additional learning:** Rank #1 Rays +1.5 (65%) is one of the 23 Rank-#1 underdog cushions in `P-345`–`P-423` (10 W / 13 L at a mean stated 0.61). P(Atlanta by 2+) was never printed as its own family, and the late three-run eighth was exactly that family → `G-L12`, baseball control 29(a). The 8.3-run centre against a 4-run total is recorded as a residual separate from the Under's win.

#### P-374 — Fenerbahçe vs Roma — UEFA Champions League — 2026-09-10


**Verified final / endpoint:** Fenerbahçe 1–1 Roma; halftime 0–1; four total corners (Fenerbahçe 1, Roma 3).

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **1H Over 0.5 goals** | 68% `UNVALIDATED_SUBJECTIVE` | **WIN** | Roma scored in the first half | 0.1024 |
| 2 | **Under 9.5 total corners** | 63% `UNVALIDATED_SUBJECTIVE` | **WIN** | 4 total corners | 0.1369 |
| 3 | **Under 2.5 total goals** | 52% `UNVALIDATED_SUBJECTIVE` | **WIN** | 2 total goals | 0.2304 |
| 4 | **Over 2.5 total goals** | 48% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 2 total goals | 0.2304 |
| 5 | **1H Under 0.5 goals** | 32% `UNVALIDATED_SUBJECTIVE` | **LOSS** | first-half goal occurred | 0.1024 |

**Ranked-row settlement subtotal:** 5 settled binary rows; 3 W / 2 L; mean Brier **0.1605**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Roma regulation winner — issued 42% `UNVALIDATED_SUBJECTIVE` — **LOSS — draw** — Brier **0.1764**.

**Process grade:** `PROCESS_DEFECT — PARTICIPANT / SOURCE-PROVENANCE GATE`

**What went right.** The early-goal call, low-corner call and slight full-match Under all landed. The low-event full-match shape was substantially closer to reality than the Over branch.

**What went wrong.** The potential winner lost to the draw. More importantly, the card's 'SECONDARY_CURRENT / HIGH-CONVERGENCE' near-kickoff XI was materially wrong for both teams. Several actual starters differed from the converged secondary feeds. That is a process defect even though three ranked rows won.

**Actual mechanism / kill-path audit.** Roma led through Bryan Cristante before halftime; Archie Brown equalised after the break. The match then stayed low-event and finished 1–1. Corner magnitude was even lower than the ~8.7 centre. The draw mass was live in the card (26%) and realised.

**Knowability / source-quality audit.** The exact XI may not have been reachable from the field owner at the frozen instant, but the uncertainty was knowable. Multiple secondary feeds can share one upstream error; convergence is not independence and is not equivalent to official confirmation.

**Learning disposition.** Never upgrade multiple secondary lineup displays into quasi-confirmed status merely because they agree. Record source lineage/independence where possible; if the field owner is unavailable, branch the participant state and cap dependent claims. Candidate disclosure for `RULES_GENERAL.md` participant provenance / `RULES_SOCCER.md`; candidate source-lineage note for `DATA_SOURCE_REGISTER.md`. No fitted weight.

**Post-result sources added in this settlement pass**
- UEFA official match/result material — final score and competition endpoint.
- The Guardian match report/live record — score progression, lineups and match statistics cross-check.


##### 2026-09-15 canonical settlement audit — P-374

- **Final re-verified:** ESPN 401915444 (1–1; corners 1+3 = 4 confirms Under 9.5).
- **Custody:** canonical record for this match; `TMP-SETTLED-20260911-01` and `TMP-RECON-20260912-01` are retired into it.
- **Additional learning:** the participant-provenance defect stays under `L-20260912-07`. A men's Champions League section is now in `LEAGUE_RULES_SOCCER.md`.

#### P-375 — Coco Gauff vs Elena Rybakina — US Open Women — Semifinal


**Verified final / endpoint:** Elena Rybakina def. Coco Gauff 3–6, 6–4, 6–4; 29 total games; aggregate games Rybakina 15, Gauff 14.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **Over 22.5 total games** | 58% `UNVALIDATED_SUBJECTIVE` | **WIN** | 29 games | 0.1764 |
| 2 | **Rybakina -0.5 aggregate games** | 55% `UNVALIDATED_SUBJECTIVE` | **WIN** | 15–14 aggregate games | 0.2025 |
| 3 | **Gauff +0.5 aggregate games** | 45% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 14–15 aggregate games | 0.2025 |
| 4 | **Under 22.5 total games** | 42% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 29 games | 0.1764 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.1895**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Elena Rybakina — issued 54% `UNVALIDATED_SUBJECTIVE` — **WIN** — Brier **0.2116**.

**Process grade:** `GOOD_PROCESS — MATCH-TREE / ENDPOINT-COHERENCE POSITIVE EXAMPLE`

**What went right.** Rank #1, Rank #2 and the winner all landed. The explicit deciding-set family was exactly the relevant structure, and the representative 28-game branch was close to the 29-game actual.

**What went wrong.** No major directional process failure. The aggregate-games margin was only one game, so the -0.5 row was materially closer to its boundary than the representative 17–15 example suggested.

**Actual mechanism / kill-path audit.** Gauff won the opening set, then Rybakina recovered to take two 6–4 sets. That is precisely the split-set / deciding-set extension path the pregame tree elevated above the event-wide deciding-set prior.

**Knowability / source-quality audit.** The completed hard-court H2Hs, current serve/return interaction and Gauff service-volatility tail were all available pregame. The exact set ordering was not.

**Learning disposition.** Retain the tennis two-sided set-count tree and keep match-winner and aggregate-games handicap as separate targets. This is a positive structural example for `RULES_TENNIS.md`; no new rule or probability uplift should be inferred from one success.

**Post-result sources added in this settlement pass**
- USTA / US Open official semifinal result and match report.


##### 2026-09-15 canonical settlement audit — P-375

- **Final:** not re-fetched this pass; the log's source is retained, and the Briers reproduce.
- **What went right:** the six-branch deciding-set tree matched the realised 3–6 6–4 6–4. It is now the reference model in `RULES_TENNIS.md` §"2026-09-15(b)".

#### P-376 — San Francisco 49ers vs Los Angeles Rams — NFL Week 1 — Melbourne


**Verified final / endpoint:** San Francisco 49ers 27–7 Los Angeles Rams; 34 total points.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **San Francisco 49ers +3.5** | 56% `UNVALIDATED_SUBJECTIVE` | **WIN** | 49ers won outright by 20 | 0.1936 |
| 2 | **Over 47.5 total points** | 54% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 34 points | 0.2916 |
| 3 | **Under 47.5 total points** | 46% `UNVALIDATED_SUBJECTIVE` | **WIN** | 34 points | 0.2916 |
| 4 | **Los Angeles Rams -3.5** | 44% `UNVALIDATED_SUBJECTIVE` | **LOSS** | Rams lost outright | 0.1936 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.2426**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Los Angeles Rams — issued 56% `UNVALIDATED_SUBJECTIVE` — **LOSS** — Brier **0.3136**.

**Process grade:** `MIXED — NEW-REGIME / INTERNATIONAL-OPENER WIDTH UNDERSTATED`

**What went right.** Rank #1 won comfortably because the underdog did not merely stay inside +3.5; San Francisco won outright. The card correctly recognized that the neutral/international setting and key-number cushion made Rams -3.5 materially weaker than a simple Rams-winner view.

**What went wrong.** The 2025 drive-efficiency baseline pointed to Rams 25.7–22.6 and Over 47.5; the actual game was a 49ers 27–7 defensive result. The winner and total centre were therefore materially wrong.

**Actual mechanism / kill-path audit.** San Francisco's defence and offensive execution controlled the game while Los Angeles failed to approach its inherited 2025 scoring baseline. The cross-season roster/system and international-opener uncertainty was larger than the central construction represented.

**Knowability / source-quality audit.** The unusual Australia opener, neutral venue and large travel/acclimation difference were knowable. It is not defensible to claim after the result that travel caused the Rams' loss; the result only shows that the regime-change distribution needed more width.

**Learning disposition.** For first-week international games with substantial roster/system discontinuity, print a larger explicit 'prior-regime fails to transfer' family instead of relying mainly on last-season PPD. Candidate for `RULES_AMERICAN_FOOTBALL.md` as a disclosure/scenario-width requirement only; no signed travel penalty or coefficient.

**Post-result sources added in this settlement pass**
- NFL official postgame 'What We Learned' / game record — 49ers 27, Rams 7 and game mechanisms.


##### 2026-09-15 canonical settlement audit — P-376

- **Final re-verified:** ESPN NFL 401872657 (49ers 27–7).
- **Additional learning:** the only one of five NFL underdog cushions (P-376, P-412–P-414, P-422) that won. The Week-1 prior-transfer uncertainty sat in the centre, so log A's CAND-MINI-H is generalised into `G-L12` and American football controls 17–19. No travel coefficient.

#### P-377 — Xelajú MC vs Cobán Imperial — Guatemala Liga Nacional Apertura 2026


**Verified final / endpoint:** Xelajú MC 0–0 Cobán Imperial. The exact corner field remains unresolved to the frozen/source-ownership standard.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **1H Over 0.5 goals** | 68% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 0–0 at halftime | 0.4624 |
| 2 | **Over 8.5 total corners** | 59% `UNVALIDATED_SUBJECTIVE` | **PROVISIONAL RESEARCH LOSS — NOT BOOKED** | secondary display shows 7 total; no field-owning endpoint | — |
| 3 | **Over 2.5 total goals** | 55% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 0 total goals | 0.3025 |
| 4 | **Under 2.5 total goals** | 45% `UNVALIDATED_SUBJECTIVE` | **WIN** | 0 total goals | 0.3025 |
| 5 | **1H Under 0.5 goals** | 32% `UNVALIDATED_SUBJECTIVE` | **WIN** | 0–0 at halftime | 0.4624 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.3825**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Xelajú MC regulation winner — issued 65% `UNVALIDATED_SUBJECTIVE` — **LOSS — draw** — Brier **0.4225**.

**Process grade:** `PROCESS_DEFECT — EARLY-GOAL / CONVERSION-MASS OVERSTATEMENT; DERIVATIVE SOURCE GAP`

**What went right.** The card explicitly preserved 0–0 halftime and low-away-score branches, and Under 2.5 plus 1H Under won. It also correctly capped participant certainty because no field-owner XI was found.

**What went wrong.** Rank #1 at 68% and the Xelajú 65% winner call were both too aggressive for a sparse-participant league match. Xelajú territorial/home advantages did not become a goal; the entire match finished 0–0. The corner row also should never be booked from the current secondary display because the field owner still does not publish the endpoint.

**Actual mechanism / kill-path audit.** The realised state was exactly the compact/low-conversion kill path discussed pregame. Xelajú had enough pressure to remain the stronger side narratively, but Cobán goalkeeper/defensive execution and finishing variance prevented conversion.

**Knowability / source-quality audit.** The lack of confirmed XIs and the recent 0–0 halftime examples were knowable. The exact goalkeeping/finishing outcome was not. The corner-source deficiency was known before issue and must remain unresolved operationally.

**Learning disposition.** For sparse-data soccer early-goal rows, separate chance-generation evidence from conversion/goalkeeper/set-piece conversion and assign explicit mass to 'territorial dominance without a goal'. Keep derivative markets unbooked until the predeclared field-owning provider is available. Candidate for `RULES_SOCCER.md` / `LEARNING_REGISTER.md` testing; source-ownership portion reinforces existing rules.

**Post-result sources added in this settlement pass**
- Liga Bantrab / Liga Nacional official result feed — 0–0 final.
- Guatefutbol match report — score and match narrative.
- Secondary corner display — 7–0/7 total research indication only; explicitly not accepted as field owner.

**Open-row tracking handle:** `TMP-OPEN-20260912-01` — retained outside the scored settlement until the required field-owning endpoint is available.


##### 2026-09-15 canonical settlement audit — P-377

- **Final re-verified:** ESPN `gua.1` 401879547 (0–0).
- **Corner row:** ESPN exposes no statistics for this league, so C02 stays provisional (`TMP-OPEN-20260912-01`).
- **Additional learning:** pressure is not conversion (soccer controls 20 and 27). A Guatemala Liga Nacional section is now in `LEAGUE_RULES_SOCCER.md`.

#### P-378 — Philippines vs Bahrain — 2026 Aichi-Nagoya Asian Games Men's Basketball


**Verified final / endpoint:** Bahrain 89–85 Philippines; 174 total points; Bahrain won by 4.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **Under 163.5 total points** | 59% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 174 points | 0.3481 |
| 2 | **Bahrain -9.5** | 56% `UNVALIDATED_SUBJECTIVE` | **LOSS** | Bahrain won by 4 | 0.3136 |
| 3 | **Philippines +9.5** | 44% `UNVALIDATED_SUBJECTIVE` | **WIN** | Philippines stayed within 9.5 | 0.3136 |
| 4 | **Over 163.5 total points** | 41% `UNVALIDATED_SUBJECTIVE` | **WIN** | 174 points | 0.3481 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.3309**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Bahrain — issued 72% `UNVALIDATED_SUBJECTIVE` — **WIN** — Brier **0.0784**.

**Process grade:** `PROCESS_DEFECT — CURRENT-ROLE / LATE-ADDITION EXPOSURE MIXTURE UNDER-MODELED`

**What went right.** The Bahrain winner call was correct. The card also identified Philippines guard creation and Oftana spacing as the key upset/cover mechanism.

**What went wrong.** Rank #1 Under and Rank #2 Bahrain -9.5 both lost. Philippines scored 85, far above the offensive-floor state derived from the Korea tune-ups. Calvin Oftana, a late addition who had not played in those tune-ups, scored 31 and hit six threes; Bahrain led by 15 after three quarters but the Philippines' fourth-quarter rally killed the spread.

**Actual mechanism / kill-path audit.** A new-roster high-usage perimeter scorer changed the Philippine efficiency distribution. Bahrain's separation branch did occur temporarily, but it was not terminal; late scoring compressed the margin and pushed the total Over.

**Knowability / source-quality audit.** Oftana's return to the final 12 was known pregame, while a 31-point game was not. The avoidable defect was treating the Korea friendlies as too informative about the final-roster offensive centre without a sufficiently wide role/minutes mixture for the added scorer.

**Learning disposition.** When a materially skilled player joins after the principal tune-up sample, model explicit role/minutes/usage states rather than using the tune-up offence as the centre for the final roster. This reinforces the existing `RULES_BASKETBALL.md` lineup/minutes mixture; candidate disclosure only, not a new coefficient.

**Post-result sources added in this settlement pass**
- Philippine/Bahrain postgame reporting (Philstar / Team Pilipinas) — Bahrain 89–85, Oftana 31, game progression.


##### 2026-09-15 canonical settlement audit — P-378

- **Final:** not re-fetched this pass; the log's source is retained.
- **Additional learning:** the late-added high-usage player is a worked example for basketball control 21. Ranks #1 and #2 lost together, so P(R1 ∧ R2) had to be printed (`G-L10`).

#### P-379 — Namibia vs South Africa — 2nd ODI — South Africa tour of Namibia 2026


**Verified final / endpoint:** South Africa 335/9 (50 overs) beat Namibia 178; South Africa were 24/0 after 5 overs.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **South Africa 50-over first innings Over 315.5** | 58% `UNVALIDATED_SUBJECTIVE` | **WIN** | 335/9 | 0.1764 |
| 2 | **South Africa first 5 overs Under 25.5** | 57% `UNVALIDATED_SUBJECTIVE` | **WIN** | 24/0 after 5 | 0.1849 |
| 3 | **South Africa first 5 overs Over 25.5** | 43% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 24/0 after 5 | 0.1849 |
| 4 | **South Africa 50-over first innings Under 315.5** | 42% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 335/9 | 0.1764 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.1807**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** South Africa — issued 86% `UNVALIDATED_SUBJECTIVE` — **WIN** — Brier **0.0196**.

**Process grade:** `GOOD_PROCESS — PHASE→INNINGS DECOUPLING POSITIVE EXAMPLE`

**What went right.** Rank #1, Rank #2 and the winner all landed. The first-five centre (~24.2) was essentially exact at 24, and the full-innings centre (~323) was reasonably close to 335.

**What went wrong.** No material structural miss. The full-innings upper tail was somewhat stronger than the central 323, but it remained inside the forecast's normal Over family.

**Actual mechanism / kill-path audit.** South Africa again began cautiously against Namibia's best new-ball phase, then accelerated across the remaining 45 overs. This independently validates the logic that a slow first five does not imply a low 50-over innings.

**Knowability / source-quality audit.** The prior ODI's 18/0 after five → 348/6 progression, toss, dry conditions and batting-positive surface commentary were all known before the innings.

**Learning disposition.** Retain cricket phase-specific targets as separate random variables connected through a joint phase→innings tree. This is a positive example for `RULES_CRICKET.md`, not evidence for a new weight.

**Post-result sources added in this settlement pass**
- South Africa–Namibia 2nd ODI final scorecard/result; ball-by-ball commentary confirming 24/0 after 5 overs.


##### 2026-09-15 canonical settlement audit — P-379

- **Final:** not re-fetched this pass; the log's scorecard source is retained.
- **What went right:** 24/0 after five became 335/9 — the positive phase-to-innings example in `RULES_CRICKET.md` §"2026-09-15(b)".

#### P-380 — Wests Tigers (W) vs Canberra Raiders (W) — NRLW Round 11, 2026


**Verified final / endpoint:** Canberra Raiders (W) 22–10 Wests Tigers (W); 32 total points; Raiders won by 12.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **Raiders -6.5** | 56% `UNVALIDATED_SUBJECTIVE` | **WIN** | Raiders won by 12 | 0.1936 |
| 2 | **Under 46.5 total points** | 54% `UNVALIDATED_SUBJECTIVE` | **WIN** | 32 points | 0.2116 |
| 3 | **Over 46.5 total points** | 46% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 32 points | 0.2116 |
| 4 | **Wests Tigers +6.5** | 44% `UNVALIDATED_SUBJECTIVE` | **LOSS** | Tigers lost by 12 | 0.1936 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.2026**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Canberra Raiders — issued 65% `UNVALIDATED_SUBJECTIVE` — **WIN** — Brier **0.1225**.

**Process grade:** `GOOD_PROCESS — LOW-TOTAL FAVOURITE-SEPARATION BRANCH REALISED`

**What went right.** Both top-ranked rows and the winner won. The card explicitly rejected the false inference that an Under must support the underdog and printed a low-total separation state; the actual 22–10 result followed that family.

**What went wrong.** The total centre (45) was materially above the 32 actual, so magnitude was still overstated even though the direction was correct.

**Actual mechanism / kill-path audit.** Canberra generated enough separation while suppressing Wests to 10; the favourite did not need a high-event game to cover.

**Knowability / source-quality audit.** The Raiders defensive baseline, intact spine and Tigers personnel losses were known; the exact 32-point total was not.

**Learning disposition.** Retain `RL-B2/RL-B3` favourite-only and low-total separation branches as mandatory coherence checks. Positive example only; no new rule.

**Post-result sources added in this settlement pass**
- NRL official NRLW Round 11 result / match report — Canberra 22, Wests Tigers 10.


##### 2026-09-15 canonical settlement audit — P-380

- **Final:** not re-fetched this pass; the NRL official report is retained.
- **What went right:** the low-total favourite-separation branch was realised (22–10), recorded as the positive model in `RULES_NRL_RUGBY.md` §"2026-09-15(b)". The 45-point centre against 32 is recorded as a residual.

#### P-381 — Chiba Lotte Marines @ Fukuoka SoftBank Hawks — NPB Pacific League


**Verified final / endpoint:** Fukuoka SoftBank Hawks 11–1 Chiba Lotte Marines; 12 total runs.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **SoftBank Hawks -1.5** | 58% `UNVALIDATED_SUBJECTIVE` | **WIN** | SoftBank won by 10 | 0.1764 |
| 2 | **Over 7.5 runs** | 52% `UNVALIDATED_SUBJECTIVE` | **WIN** | 12 runs | 0.2304 |
| 3 | **Under 7.5 runs** | 48% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 12 runs | 0.2304 |
| 4 | **Chiba Lotte Marines +1.5** | 42% `UNVALIDATED_SUBJECTIVE` | **LOSS** | Lotte lost by 10 | 0.1764 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.2034**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Fukuoka SoftBank Hawks — issued 70% `UNVALIDATED_SUBJECTIVE` — **WIN** — Brier **0.0900**.

**Process grade:** `GOOD_PROCESS — ROLE-CHANGE / CONTACT-CLUSTER BRANCH REALISED`

**What went right.** Rank #1, Rank #2 and the winner all won. The forecast correctly treated Ishikawa's move from relief to a first 2026 top-team start as a wide role-change distribution rather than trusting his aggregate ERA.

**What went wrong.** The 5–3 central score materially understated the upper tail. SoftBank's separation was much larger than the central margin.

**Actual mechanism / kill-path audit.** Ishikawa lasted only 3.1 innings and allowed 10 hits / 8 earned runs; SoftBank produced a seven-run fourth. Maeda then protected the separation with seven strong innings. This is the exact early-hook/contact-cluster family described in the card.

**Knowability / source-quality audit.** Ishikawa's role transition and prior SoftBank volatility were known. The exact seven-run inning was not.

**Learning disposition.** Keep starter role-change mixtures and multi-run cluster branches explicit. When a starter-transition branch is a primary mechanism for the favourite's run line, verify that its assigned mass is visible rather than only discussed in prose. Reinforces `RULES_BASEBALL.md`; no fitted uplift.

**Post-result sources added in this settlement pass**
- NPB official Sep 11 SoftBank–Lotte box score — 11–1, pitcher lines and inning scoring.


##### 2026-09-15 canonical settlement audit — P-381

- **Final re-verified:** NPB English scoreboard, 11 Sep (SoftBank 11–1).
- **What went right:** the role-change mixture for Ishikawa's first ichi-gun start (baseball controls 11 and 15) produced the deciding early-failure branch. It counts among the 7 W / 3 L Rank-#1 favourite handicaps.

#### P-382 — Saitama Seibu Lions @ Orix Buffaloes — NPB Pacific League


**Verified final / endpoint:** Orix Buffaloes 5–4 Saitama Seibu Lions; 9 total runs.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **Seibu Lions -1.5** | 54% `UNVALIDATED_SUBJECTIVE` | **LOSS** | Seibu lost outright | 0.2916 |
| 2 | **Over 7.0 runs** | 47% `UNVALIDATED_SUBJECTIVE` | **WIN** | 9 runs; no push | 0.2809 |
| 3 | **Orix Buffaloes +1.5** | 46% `UNVALIDATED_SUBJECTIVE` | **WIN** | Orix won outright | 0.2916 |
| 4 | **Under 7.0 runs** | 39% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 9 runs; no push | 0.1521 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.2540**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Saitama Seibu Lions — issued 65% `UNVALIDATED_SUBJECTIVE` — **LOSS** — Brier **0.4225**.

**Process grade:** `MIXED — BULLPEN-TRANSITION KILL PATH UNDERWEIGHTED`

**What went right.** The Over side won and the pregame card explicitly identified Orix's fresher high-leverage options and Seibu's worked bridge as the main late compression/reversal risk.

**What went wrong.** Rank #1 and the Seibu winner both lost. Seibu held a 4–3 advantage after five, but Orix scored twice in the sixth and protected the lead.

**Actual mechanism / kill-path audit.** The starter/early-scoring edge was not enough; the game moved into the exact bullpen-transition state that threatened the Lions side. The forecast named that state but still left 65% on the Seibu winner.

**Knowability / source-quality audit.** The recent Seibu relief workload and Orix fresher leverage alternatives were known. The exact sixth-inning reversal was not.

**Learning disposition.** When the central side advantage depends on reaching the late innings ahead, map the actual score-state relief chain into the winner/margin tree and ensure a known bullpen disadvantage receives explicit branch mass. Reinforces `RULES_BASEBALL.md` score-state bullpen availability; no 'fresh bullpen = automatic win' rule.

**Post-result sources added in this settlement pass**
- NPB official Sep 11 Orix–Seibu box score — Orix 5–4 and inning sequence.


##### 2026-09-15 canonical settlement audit — P-382

- **Final re-verified:** NPB English scoreboard, 11 Sep (Orix 5–4).
- **Additional learning:** a Rank-#1 favourite −1.5 lost to an underdog win — the other margin tail, which is why the test is `C-MARGIN-TAIL-MASS` (both tails).

#### P-383 — Yokohama DeNA BayStars @ Hiroshima Toyo Carp — NPB Central League


**Verified final / endpoint:** Yokohama DeNA BayStars 6–1 Hiroshima Toyo Carp; 7 total runs.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **Hiroshima Carp +1.5** | 59% `UNVALIDATED_SUBJECTIVE` | **LOSS** | Hiroshima lost by 5 | 0.3481 |
| 2 | **Under 6.5 runs** | 56% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 7 runs | 0.3136 |
| 3 | **Over 6.5 runs** | 44% `UNVALIDATED_SUBJECTIVE` | **WIN** | 7 runs | 0.3136 |
| 4 | **DeNA BayStars -1.5** | 41% `UNVALIDATED_SUBJECTIVE` | **WIN** | DeNA won by 5 | 0.3481 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.3309**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Yokohama DeNA BayStars — issued 57% `UNVALIDATED_SUBJECTIVE` — **WIN** — Brier **0.1849**.

**Process grade:** `PROCESS_DEFECT — BULLPEN FRESHNESS CONFLATED WITH RUN-SUPPRESSION QUALITY`

**What went right.** The DeNA winner lean was correct, and the starter-suppression idea held for much of the game: it was 0–0 through five and only 1–0 Hiroshima after six.

**What went wrong.** Rank #1 and Rank #2 both lost. DeNA scored three in the eighth and three in the ninth, converting a low-event starter game into a 6–1 separation. The pregame card explicitly called Hiroshima's 'very fresh' bullpen a strong run-suppression mechanism; that violates the existing baseball control that freshness is availability, not quality.

**Actual mechanism / kill-path audit.** The starters suppressed scoring early, then the fresh Hiroshima bullpen failed in the exact innings where the forecast expected freshness to protect Carp +1.5 / Under 6.5.

**Knowability / source-quality audit.** Bullpen workload was knowable, but performance quality under that workload cannot be inferred from rest alone. The process error was interpretive and fully avoidable under existing rules.

**Learning disposition.** No new rule is needed: enforce the existing `RULES_BASEBALL.md` control, 'Bullpen freshness is not quality.' Freshness may alter arm availability and role probabilities; direction requires the named arms, quality, platoon/lineup interaction and score-state chain. Add this event as a negative example in the sport-rule learning note if the Drive is later edited.

**Post-result sources added in this settlement pass**
- NPB official Sep 11 Hiroshima–DeNA box score — DeNA 6–1, late 3-run eighth and 3-run ninth.


##### 2026-09-15 canonical settlement audit — P-383

- **Final re-verified:** NPB English scoreboard, 11 Sep (DeNA 6–1).
- **Additional learning:** Rank #1 was a home-underdog +1.5 that lost by five (`G-L12`). "Fresh bullpen = suppression" stays a negative example under baseball control 20.

#### P-384 — Kiwoom Heroes @ Samsung Lions — KBO League


**Verified final / endpoint:** Samsung Lions 6–4 Kiwoom Heroes; 10 total runs; Samsung won by 2.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **Samsung Lions -1.5** | 64% `UNVALIDATED_SUBJECTIVE` | **WIN** | Samsung won by 2 | 0.1296 |
| 2 | **Under 11.5 runs** | 60% `UNVALIDATED_SUBJECTIVE` | **WIN** | 10 runs | 0.1600 |
| 3 | **Over 11.5 runs** | 40% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 10 runs | 0.1600 |
| 4 | **Kiwoom Heroes +1.5** | 36% `UNVALIDATED_SUBJECTIVE` | **LOSS** | Kiwoom lost by 2 | 0.1296 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.1448**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Samsung Lions — issued 75% `UNVALIDATED_SUBJECTIVE` — **WIN** — Brier **0.0625**.

**Process grade:** `GOOD_PROCESS / EVIDENCE-CAPPED — POWER-SEPARATION WITH CONTROLLED TOTAL`

**What went right.** Both top rows and the winner won. Samsung's stronger power/sequencing path created enough separation while the total stayed below the high 11.5 threshold.

**What went wrong.** No major structural miss in the ranked slate. The result sat relatively close to both the -1.5 and total thresholds, so it should not be used to justify stronger future probabilities.

**Actual mechanism / kill-path audit.** Samsung won 6–4, with a concentrated power contribution driving the scoring rather than a game-wide pitching collapse.

**Knowability / source-quality audit.** The lineup/power advantage was knowable; exact home-run clustering was not. The original evidence cap for incomplete participant detail was appropriate.

**Learning disposition.** Positive example of separating margin-cluster mechanisms from a high full-game total. Reinforce the existing baseball cluster/separation logic; no new rule.

**Post-result sources added in this settlement pass**
- Korean postgame reports (Newsis / StarNews) — Samsung 6–4 and key power contribution.


##### 2026-09-15 canonical settlement audit — P-384

- **Final re-verified:** KBO English scoreboard, 11 Sep (Samsung 6–4).
- **Result for the pattern count:** the favourite's −1.5 won by exactly two — a boundary win that supports printing exact one- and two-run masses (baseball control 29).

#### P-385 — KT Wiz @ Lotte Giants — KBO League


**Verified final / endpoint:** KT Wiz 7–1 Lotte Giants; 8 total runs; KT won by 6.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **KT Wiz -1.5** | 56% `UNVALIDATED_SUBJECTIVE` | **WIN** | KT won by 6 | 0.1936 |
| 2 | **Over 9.5 runs** | 51% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 8 runs | 0.2601 |
| 3 | **Under 9.5 runs** | 49% `UNVALIDATED_SUBJECTIVE` | **WIN** | 8 runs | 0.2601 |
| 4 | **Lotte Giants +1.5** | 44% `UNVALIDATED_SUBJECTIVE` | **LOSS** | Lotte lost by 6 | 0.1936 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.2268**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** KT Wiz — issued 68% `UNVALIDATED_SUBJECTIVE` — **WIN** — Brier **0.1024**.

**Process grade:** `GOOD_PROCESS / TOTAL NEAR-COIN-FLIP`

**What went right.** Rank #1 and the winner were correct, and KT created clear separation. The Under side of the nearly even total also won.

**What went wrong.** The 51% Over ranked above the 49% Under but lost. This is not a major diagnostic miss: the card itself had essentially no directional total edge.

**Actual mechanism / kill-path audit.** KT combined strong run prevention with enough offence to win comfortably; the game never needed the high-scoring joint branch.

**Knowability / source-quality audit.** The total was near the model centre and therefore inherently fragile. Nothing in this one result justifies a directional rule change.

**Learning disposition.** When complementary total probabilities are 51/49 or similarly close, label the order as practically coin-flip in the retrospective and avoid extracting a lesson from which side happened to win. Reinforces `RULES_GENERAL.md` §16.9 exact-mass/coherence language; no threshold or new coefficient.

**Post-result sources added in this settlement pass**
- Korean postgame reporting (Newsis / SportsTimes) — KT 7–1, starter and key batting lines.


##### 2026-09-15 canonical settlement audit — P-385

- **Final re-verified:** KBO English scoreboard, 11 Sep (KT 7–1).
- **What went right:** the favourite's −1.5 won on the starter asymmetry, and the total was honestly labelled a coin flip (`G-L2`).

#### P-386 — South Sydney Rabbitohs vs Newcastle Knights — NRL Finals Week 1 Elimination Final


**Verified final / endpoint:** Newcastle Knights 20–10 South Sydney Rabbitohs; 30 total points; Newcastle won by 10.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **Newcastle Knights +8.5** | 63% `UNVALIDATED_SUBJECTIVE` | **WIN** | Knights won outright | 0.1369 |
| 2 | **Over 49.5 total points** | 53% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 30 points | 0.2809 |
| 3 | **Under 49.5 total points** | 47% `UNVALIDATED_SUBJECTIVE` | **WIN** | 30 points | 0.2809 |
| 4 | **South Sydney -8.5** | 37% `UNVALIDATED_SUBJECTIVE` | **LOSS** | South Sydney lost outright | 0.1369 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.2089**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** South Sydney Rabbitohs — issued 63% `UNVALIDATED_SUBJECTIVE` — **LOSS** — Brier **0.3969**.

**Process grade:** `MIXED — CUSHION CALL RIGHT; WINNER/TOTAL REGIME WRONG WITH IN-GAME INJURY SHOCK`

**What went right.** Rank #1 was strong: Newcastle +8.5 survived by winning outright. The card correctly kept a meaningful Knights upset/close-game family despite leaning Souths as winner.

**What went wrong.** The Souths winner and Over both lost. The actual game was a low-scoring Newcastle win.

**Actual mechanism / kill-path audit.** Newcastle controlled enough territory/yardage to win, while Souths lost Cody Walker to a calf injury during the first half. That in-game injury altered the attacking environment and is a material post-issue shock.

**Knowability / source-quality audit.** The pregame uncertainty and dependence on spine execution were knowable; Walker's in-game calf injury was not. It would be hindsight error to treat that injury as a research miss.

**Learning disposition.** Retain spine-injury/terminal-shock states in rugby-league distribution width, but do not retrofit a directional penalty after an unforeseeable in-game injury. Rank #1 cushion decomposition remains useful. No new rule.

**Post-result sources added in this settlement pass**
- Newcastle Knights / NRL official match wrap — Knights 20–10, Ponga performance and Walker injury context.


##### 2026-09-15 canonical settlement audit — P-386

- **Final re-verified:** ESPN `rugby-league/3` 604733 (Knights 20–10).
- **What went right:** the underdog cushion won outright — rugby league's Rank-#1 underdog cushions went 3 / 0.
- **Winner label:** Souths was wrong; `G-L12` now requires the underdog-win mass beside the label.

#### P-387 — Kyoto Sanga F.C. vs Kashiwa Reysol — J1 League


**Verified final / endpoint:** Kashiwa Reysol 3–2 Kyoto Sanga; halftime Kyoto 2–0. Official J.League statistics now show Kyoto with 7 corner kicks.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **1H Over 0.5 goals** | 64% `UNVALIDATED_SUBJECTIVE` | **WIN** | 2 first-half goals | 0.1296 |
| 2 | **Under 2.5 total goals** | 57% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 5 total goals | 0.3249 |
| 3 | **Kyoto team corners Under 4.5** | 55% `UNVALIDATED_SUBJECTIVE` | **LOSS** | official J.League: Kyoto 7 corners | 0.3025 |
| 4 | **Over 2.5 total goals** | 43% `UNVALIDATED_SUBJECTIVE` | **WIN** | 5 total goals | 0.3249 |
| 5 | **1H Under 0.5 goals** | 36% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 2 first-half goals | 0.1296 |

**Ranked-row settlement subtotal:** 5 settled binary rows; 2 W / 3 L; mean Brier **0.2423**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Kashiwa Reysol regulation winner — issued 44% `UNVALIDATED_SUBJECTIVE` — **WIN** — Brier **0.3136**.

**Process grade:** `MIXED — EARLY-GOAL/WINNER RIGHT; SECOND-HALF COMEBACK TAIL UNDERWEIGHTED`

**What went right.** Rank #1 and the potential winner both won. Kyoto scored twice before halftime, then Kashiwa completed the comeback the winner distribution allowed.

**What went wrong.** The Under 2.5 and Kyoto team-corners Under 4.5 both lost. The match reached five goals, and the official J.League club record shows Kyoto had seven corners. The original corner-provider uncertainty is now removed for the underlying sporting endpoint because the field owner has published `CK=7`.

**Actual mechanism / kill-path audit.** Kyoto led 2–0, but Kashiwa scored at 59', 67' and 71'; substitute Yusuke Segawa was central to the comeback. The card's bench record was incomplete/partial, and the second-half attacking-substitution state was not fully represented.

**Knowability / source-quality audit.** The possibility of Kashiwa attacking substitutions and Kyoto's corner volume was knowable in principle; the exact three-goal 12-minute swing was not. The official corner endpoint became available after the match and is now sufficient to settle the team-corner row.

**Learning disposition.** When the bench record is incomplete, full-match total/winner branches must reserve explicit second-half comeback/substitution mass; do not infer a full-match Under from a controlled first-half state. Also add the J.League official club `CK` field as the preferred settlement lane for team corners. Candidate for `RULES_SOCCER.md` / `DATA_SOURCE_REGISTER.md`; no fitted weight.

**Post-result sources added in this settlement pass**
- J.League official match result — Kyoto 2–3 Kashiwa and comeback summary.
- J.League official Kyoto club record — Sep 11 result with `CK = 7`, settling Kyoto Under 4.5 corners as LOSS.


##### 2026-09-15 canonical settlement audit — P-387

- **Final re-verified:** ESPN `jpn.1` 401877647 (2–3). ESPN's Kyoto corners (7) match the J.League official `CK = 7`.
- **Additional learning:** the bench-driven comeback reinforces `G14.2` and the soccer second-half/bench controls; the leading-state concession is an example for soccer control 33.

#### P-388 — Fremantle Dockers vs Geelong Cats — AFL First Semi-Final


**Verified final / endpoint:** Fremantle 18.12 (120) def. Geelong 16.10 (106); 226 total points; Fremantle won by 14.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|
| 1 | **Geelong +11.5** | 60% `UNVALIDATED_SUBJECTIVE` | **LOSS** | Geelong lost by 14 | 0.3600 |
| 2 | **Under 180.5 total points** | 55% `UNVALIDATED_SUBJECTIVE` | **LOSS** | 226 points | 0.3025 |
| 3 | **Over 180.5 total points** | 45% `UNVALIDATED_SUBJECTIVE` | **WIN** | 226 points | 0.3025 |
| 4 | **Fremantle -11.5** | 40% `UNVALIDATED_SUBJECTIVE` | **WIN** | Fremantle won by 14 | 0.3600 |

**Ranked-row settlement subtotal:** 4 settled binary rows; 2 W / 2 L; mean Brier **0.3313**. This is a learning-only descriptive calculation, not a calibration or edge claim.

**Potential-winner settlement:** Fremantle — issued 58% `UNVALIDATED_SUBJECTIVE` — **WIN** — Brier **0.1764**.

**Process grade:** `PROCESS_DEFECT — HIGH-SHOT / CONVERSION KILL PATH NAMED BUT UNDER-MASSED`

**What went right.** The Fremantle winner was correct, and the card explicitly identified upper-conversion/high-shot paths as the main threats to Geelong +11.5 and the Under.

**What went wrong.** Rank #1 and Rank #2 both lost, narrowly on the spread but massively on the total. The 177-ish central total was almost 50 points below the 226 actual. The card had same-season high totals and a high-shot Geelong reference available, yet still left only 45% on Over 180.5.

**Actual mechanism / kill-path audit.** Both teams sustained scoring volume and conversion; Fremantle reached 120 and Geelong 106. The high-shot/high-conversion family was not merely a tail—it dominated the realised game.

**Knowability / source-quality audit.** The exact 226 was not knowable, but the upper-event mechanisms and same-season evidence were visible before the match. This is therefore a branch-mass allocation miss rather than a hidden-data surprise.

**Learning disposition.** Use `G-L9` complement decomposition to force every named high-shot/high-conversion kill path into mutually exclusive threshold-crossing states with explicit mass. In AFL, do not leave AF-B3/AF-B4 as prose when multiple current mechanisms point to the same Over/separation family. Candidate reinforcement for `RULES_AFL.md` + `RULES_GENERAL.md`; no numerical weight promoted under `L-087`.

**Post-result sources added in this settlement pass**
- ABC / AFL finals postgame reporting and The Guardian live report — Fremantle 120, Geelong 106 and final scoring.


##### 2026-09-15 canonical settlement audit — P-388

- **Final re-verified:** ESPN AFL 1133708 (Fremantle 120–106).
- **Additional learning:** Geelong +11.5 lost by 14. AFL finals underdog cushions went 0 / 2 (with P-396), and both times the high-shot / upper-conversion family was under-massed → `RULES_AFL.md` §"2026-09-15(b)".

#### P-389 — Dublin Guardians vs Edinburgh Castle Rockers — ETPL 2026 Match 21


**Verified final / endpoint:** Dublin Guardians won the toss and chose to bowl; Edinburgh Capitals therefore batted first and made 174/4. Dublin made 162/8; Edinburgh won by 12 runs.

| Rank | Frozen issued row | Issued probability | Settlement | Observed endpoint | Brier |
|---:|---|---:|---|---|---:|

**Potential-winner settlement:** none issued; **NO SCORE / NO BRIER**.

**Process grade:** `GOOD_PROCESS — HARD GATE / NO-FORECAST DISCIPLINE`

**What went right.** The card correctly refused to issue ranked picks before the toss/innings-order target was verified. That is the desired behaviour under the cricket target-identity gate.

**What went wrong.** Nothing to score: no ranked selection or potential-winner forecast was issued. The conditional research happened to align with the later toss condition, but it cannot be retroactively converted into a forecast.

**Actual mechanism / kill-path audit.** After the toss, Edinburgh batted first, reached 174/4 and defended the total by 12 runs. Post-result inspection indicates the conditional Under 177.5, first-six Under 51.5 and Edinburgh winner ideas would have landed, but those are counterfactual diagnostics only.

**Knowability / source-quality audit.** The missing innings-order information was genuinely unresolved before the toss and was a blocking target-definition fact. Waiting was correct.

**Learning disposition.** A conditional pre-toss research branch that is not activated and issued before exposure begins remains non-scorable even if the condition later occurs. Reinforce `RULES_CRICKET.md` toss/innings-order hard gate and `METHOD.md` anti-hindsight lifecycle. No new rule.

**Post-result sources added in this settlement pass**
- CricketWorld / contemporary match commentary and final result reporting — toss, Edinburgh 174/4, Dublin 162/8, Edinburgh won by 12.


##### 2026-09-15 canonical settlement audit — P-389

- **Confirmed** administrative / no forecast (the toss gate was withheld correctly). The conditional research is not retro-scored; it is an anti-hindsight example in `RULES_CRICKET.md` §"2026-09-15(b)".

### Log B settlement and retrospective sections (verbatim from the external session, 2026-09-14)

#### P-399 — Genoa vs Frosinone — Serie A


**Verified final:** Genoa **1**, Frosinone **1**. Frosinone led **1-0 at half-time**; Genoa equalised on 50'. Secondary event-stat feeds agree on **Genoa 8, Frosinone 9 corners = 17**.

| Rank | Frozen contract | Issued `p` | Settlement | Brier/status |
|---:|---|---:|---|---|
| 1 | 1H Over 0.5 | 67% | **WIN** | 0.1089 |
| 2 | Combined corners Over 8.5 | 64% | **PROVISIONAL RESEARCH WIN** — 17; **NOT BOOKED** because frozen provider/field-owner settlement remains unresolved | — |
| 3 | FT Under 2.5 | 56% | **WIN** — 2 | 0.1936 |
| 4 | FT Over 2.5 | 44% | **LOSS** | 0.1936 |
| 5 | 1H Under 0.5 | 33% | **LOSS** | 0.1089 |

**Potential regulation winner:** Genoa 40% — **LOSS** (draw). Original 1X2 also reserved 27% for the draw.

**What went right:** early-goal and Under directions. The match also generated very high corner volume while staying Under 2.5, directly supporting the framework's separation of goal and corner processes.

**What could improve:** Genoa missed a first-half penalty and later played the final minutes with ten men after Johan Vásquez's second yellow. Those realised events are not pregame misses. The winner call at 40% should not be over-interpreted against a 27% draw band.

**Source/settlement issue:** OFStats and PlayerStats independently report 8-9 corners, and their event timelines enumerate corner events. However the original card explicitly had `UNKNOWN_DEFINITION` for the exact corner provider and no field-owning Lega Serie A corner endpoint was recovered in this pass. Per `RULES_SOCCER.md`, this remains provisional rather than silently upgraded.

**Learning / proposed placement:** reinforce existing `RULES_SOCCER.md` derivative-settlement and “goals are not corners” controls. No new predictive rule. Source lane candidates (`OFStats`, `PlayerStats`) may be recorded in `DATA_SOURCE_REGISTER.md` as **secondary corroboration only**, not field owners.

**Settlement sources:** OFStats `https://ofstats.com/matches/view/genoa-frosinone-2026-09-12`; PlayerStats `https://playerstats.football/fixture/genoa/frosinone/2026-09-12`.

**Open handle:** `TMP-OPEN-20260914-01` — `P-399-C02`, combined corners O8.5; retry only if a Lega Serie A/official data-partner field or frozen-provider-equivalent record is recovered.

**Disposition:** **PARTIALLY SETTLED / EVENT REMAINS OPEN ONLY FOR C02**.


##### 2026-09-15 canonical settlement audit — P-399

- **Final re-verified:** ESPN `ita.1` 401874991 (1–1; ESPN corners 8+9 = 17).
- **Corner row:** C02 stays provisional (`TMP-OPEN-20260914-01`) — no Serie A record reached.
- **What went right:** Rank #1 1H Over and the Under 2.5 won. 1–1 with 17 corners is the "corners are not goals" counterexample.

#### P-401 — IFK Göteborg vs Halmstads BK — Allsvenskan


**Verified final:** IFK Göteborg **2**, Halmstads BK **1**. Goals: 37', 52', 73', so half-time was **1-0**. Multiple current statistical feeds report **IFK 8, Halmstad 9 corners = 17**.

| Rank | Frozen contract | Issued `p` | Settlement | Brier/status |
|---:|---|---:|---|---|
| 1 | Combined corners Over 8.5 | 80% | **PROVISIONAL RESEARCH WIN** — 17; not owner-standard booked | — |
| 2 | Halmstad team total Under 1.5 | 77% | **WIN** — 1 goal | 0.0529 |
| 3 | IFK team corners Over 4.5 | 76% | **PROVISIONAL RESEARCH WIN** — 8; not owner-standard booked | — |
| 4 | 1H Under 0.5 | 56% | **LOSS** — IFK scored 37' | 0.3136 |
| 5 | FT Over 2.5 | 53% | **WIN** — 3 goals | 0.2209 |

**Potential regulation winner:** IFK Göteborg 67% — **WIN**.

**What went right:** winner, Halmstad scoring suppression, and the full-match Over. The corner mechanism also appears directionally strong: 17 total and eight IFK corners across independent displays.

**What went wrong:** the early-goal Under was only a modest 56% but still ranked above the full-match Over. IFK scored at 37', so the first-half no-goal branch failed without invalidating the separate corner or team-total logic.

**Settlement/source lesson:** Statz and FootyMetrics agree on 8-9 corners, with ScoreBat also reporting 8-9. That is strong research corroboration, but the card's provider definition was not frozen and no Allsvenskan field-owner/data-partner record has been recovered. Per the Drive rule, agreement among secondary feeds does not itself create a frozen field owner.

**Learning / proposed placement:** reinforce `RULES_SOCCER.md` derivative completeness/settleability. Candidate source registration: Statz/FotMob/FootyMetrics/ScoreBat as secondary Opta/statistical lanes for Allsvenskan discovery/corroboration, not definitive settlement unless provider equivalence is documented.

**Settlement sources:** Statz `https://statz.ai/h2h/ifk-gteborg-vs-halmstad/19635884`; FootyMetrics Allsvenskan corner table `https://www.footymetrics.com/statistics/corners/sweden-allsvenskan`; ScoreBat match page `https://www.scorebat.com/goteborg-vs-halmstad-live-stream/`.

**Open handles:** `TMP-OPEN-20260914-02` — `P-401-C01` combined corners O8.5; `TMP-OPEN-20260914-03` — `P-401-C03` IFK team corners O4.5.

**Disposition:** **PARTIALLY SETTLED / EVENT REMAINS OPEN FOR C01 AND C03 ONLY**.


##### 2026-09-15 canonical settlement audit — P-401

- **Final re-verified:** ESPN `swe.1` 401874088 (2–1; ESPN corners 8+9 = 17, IFK 8).
- **Corner rows:** C01 and C03 stay provisional (`TMP-OPEN-20260914-02`/`-03`), so Rank #1 is not booked.
- **Additional learning:** the 56% 1H Under lost at 37' — recorded in the `C-PHASE-VS-FULL-TOTAL` update.

#### P-402 — Tottenham Hotspur vs Everton — Premier League


**Verified final:** Tottenham Hotspur **0**, Everton **0**. Secondary Opta/event-stat lanes agree on **Tottenham 5, Everton 6 corners = 11**.

| Rank | Frozen contract | Issued `p` | Settlement | Brier/status |
|---:|---|---:|---|---|
| 1 | Everton +1.5 | 81% | **WIN** | 0.0361 |
| 2 | Combined corners Over 8.5 | 74% | **PROVISIONAL RESEARCH WIN** — 11; provider unresolved | — |
| 3 | Tottenham team corners Over 4.5 | 71% | **PROVISIONAL RESEARCH WIN** — 5; provider unresolved | — |
| 4 | 1H Over 0.5 | 63% | **LOSS** — 0-0 HT | 0.3969 |
| 5 | FT Over 2.5 | 52% | **LOSS** — 0 goals | 0.2704 |

**Potential regulation winner:** Tottenham 41% — **LOSS** (draw).

**What went right:** the strongest row, Everton +1.5, was robust to the draw. The corner exposure also appears correct: Spurs reached five and the match eleven despite no goals.

**What went wrong:** the goal side of the card overestimated conversion/goal realisation. Tottenham extended its scoreless league start; the match still generated 11 corners and late pressure. This is a clean example of **territory/corner volume not being equivalent to chance conversion or scoreboard production**.

**Knowability:** Tottenham's existing scoring drought was known but had been shrunk rather than blindly extrapolated, which is correct process. The smallest improvement is not “trust droughts more”; it is to keep the shot-quality/keeper/finishing branch sufficiently separate from corner/territory exposure when the attack has repeatedly failed to convert.

**Source/settlement issue:** OFStats reports 5-6 corners and a detailed event timeline; Statz's match-by-match corner table also records 5-6. The exact bookmaker/provider definition was not frozen, so both corner rows remain provisional to the Drive standard.

**Learning / proposed placement:** use as a worked example under `RULES_SOCCER.md` controls 4, 21, 25 and 27: **corners/territory can be high while goals stay at zero**. No new predictive rule. Register OFStats/Statz/PlayerStats only as secondary corroboration lanes unless provider ownership is established.

**Settlement sources:** Guardian final report `https://www.theguardian.com/football/live/2026/sep/12/tottenham-v-everton-premier-league-live-updates`; OFStats `https://ofstats.com/matches/view/tottenham-hotspur-everton-2026-09-12`; Statz Spurs corners `https://statz.ai/team/tottenham-hotspur/corners`.

**Open handles:** `TMP-OPEN-20260914-04` — `P-402-C02` total corners O8.5; `TMP-OPEN-20260914-05` — `P-402-C03` Tottenham team corners O4.5.

**Disposition:** **PARTIALLY SETTLED / EVENT REMAINS OPEN FOR C02 AND C03 ONLY**.


##### 2026-09-15 canonical settlement — P-402 (PRIMARY_SCORED EPL)

- **Final:** Premier League official data (fixture 128962) and ESPN 401879277 — 0–0.
- **Corners at the field owner:** Tottenham 5, Everton 6 = 11. **C02 WIN (0.0676)** and **C03 WIN (0.0841)**; handles `-04`/`-05` retired.
- **Card now FINAL / SETTLED:** W W W L L, mean Brier 0.1710; top two both won.
- **What went right:** Everton +1.5 was protected by a low-event game, and corners were modelled separately from goals. The Premier League record is now pre-registered (soccer control 32).

#### P-406 — Edinburgh Castle Rockers vs Amsterdam Flames — ETPL Match 24


**Verified result:** Edinburgh Castle Rockers **118 all out in 18.3 overs**; Amsterdam Flames **120/2 in 14.5 overs**, Flames won by **8 wickets**. Michael Bracewell took **5/12**. The recovered fall-of-wicket record has Edinburgh 37/1 at 2.6, 37/2 at 3.1 and 77/3 at 7.3, but no trustworthy exact **6.0-over** checkpoint was recovered.

| Rank | Frozen contract | Issued `p` | Settlement | Brier/status |
|---:|---|---:|---|---|
| 1 | ECR first 6 Over 50.5 | 64% | **UNRESOLVED** — exact 6.0 legal-ball score not recovered | — |
| 2 | ECR 20-over Over 172.5 | 54% | **LOSS** — innings ended at 118 | 0.2916 |
| 3 | ECR 20-over Under 172.5 | 46% | **WIN** | 0.2916 |
| 4 | ECR first 6 Under 50.5 | 36% | **UNRESOLVED** — same checkpoint | — |

**Potential winner:** Edinburgh 67% — **LOSS**; Amsterdam won by eight wickets.

**What went wrong:** the full-innings Over and winner materially over-rated Edinburgh's unbeaten/current-form branch. Edinburgh did start aggressively enough to reach 37 by 2.6, but Amsterdam's spin/middle-over resources changed the innings: Bracewell's 5/12 drove a collapse to 118. This is exactly why a fast opening phase cannot be projected directly into a full innings or match winner.

**What cannot be claimed:** the first-six Over/Under cannot be settled from nearby fall-of-wicket markers. A score at 3.1 and 7.3 does not uniquely determine the score after 6.0 legal overs. No interpolation or retrospective inference is permitted.

**Learning / proposed placement:** reinforce `RULES_CRICKET.md` controls 1, 2 and 16: **phase endpoints require exact legal-ball reconstruction; phase and innings are separate; phase→innings must carry wickets/resources and bowling allocation.** Also reinforce winner independence from innings-total direction. No fitted rule change.

**Settlement sources:** Statz scorecard `https://statz.ai/cricket/fixtures/71065/edinburgh-castle-rockers-vs-amsterdam-flames/scorecard`; official ETPL page remained stale/unpopulated in this pass and therefore was not used to invent the missing 6-over field.

**Open handle:** `TMP-OPEN-20260914-06` — `P-406-C01/C04`, exact Edinburgh score after **6.0 completed legal overs**. One exact checkpoint will settle both complementary rows.

**Disposition:** **PARTIALLY SETTLED / EVENT REMAINS OPEN FOR THE 6-OVER TARGET ONLY**.


















##### 2026-09-15 canonical settlement audit — P-406

- **Final** (Edinburgh 118 all out; Amsterdam 120/2). The six-over rows stay unresolved (`TMP-OPEN-20260914-06`): a final score and fall-of-wicket markers do not settle a phase checkpoint (cricket control 15).

#### P-390 — Cincinnati Reds @ Milwaukee Brewers — MLB


**Verified final:** Milwaukee Brewers **20**, Cincinnati Reds **0**. Milwaukee scored six in the second inning and eight in the fifth; Andrew Abbott was removed after allowing eight runs in two innings, while Dustin May worked six scoreless innings.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Over 8.0 runs | 57% win / 10% push / 33% loss | **WIN** — 20 runs | 0.1849 |
| 2 | Reds +1.5 | 56% | **LOSS** — CIN lost by 20 | 0.3136 |
| 3 | Brewers -1.5 | 44% | **WIN** | 0.3136 |
| 4 | Under 8.0 runs | 33% win / 10% push / 57% loss | **LOSS** | 0.1089 |

**Potential winner:** Brewers 62% — **WIN**.

**What went right:** the card preferred Milwaukee outright and correctly left a meaningful upper-total/favourite-separation route. The Over was Rank #1 and won decisively.

**What went wrong / mechanism:** the realised branch was far more extreme than the central ~9.1-run object. Milwaukee's early cluster, Abbott's short/ineffective exposure, and the subsequent relief environment were not independent tails: the same mechanism simultaneously drove the Over and the 2+ run Milwaukee separation. The card assigned only 44% to MIL -1.5 while giving 56% to CIN +1.5, so the separation tail was materially under-massed relative to the kill path already described.

**Knowability:** the exact 20-0 magnitude was not knowable. The *joint* early-cluster → short-start → favourite-separation path was knowable and already present in the card; the process issue is probability-mass allocation, not failure to predict a historic blowout exactly.

**Learning / proposed placement:** reinforce `RULES_BASEBALL.md` controls 19/20/21 and `RULES_GENERAL.md` §16.9 / G-L9 with this as a worked example of **cluster and favourite separation being one joint state rather than two prose risks**. No fitted coefficient or automatic Over/favourite rule is justified from one event. Candidate learning only for `LEARNING_REGISTER.md`; do not promote without broader testing.

**Settlement sources:** MLB game story `https://www.mlb.com/stories/game/823736`; Reuters, *Brewers demolish Reds 20-0...* `https://www.reuters.com/sports/baseball/brewers-demolish-reds-20-0-wrap-up-postseason-berth--flm-2026-09-12/`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-390

- **Final re-verified:** MLB statsapi 823736 (20–0).
- Rank #1 Over 8.0 won. The Reds +1.5 at Rank #2 (56%) lost by 20 — the favourite-separation tail recorded in `C-MARGIN-TAIL-MASS`.

#### P-391 — Cleveland Guardians @ Minnesota Twins — MLB


**Verified final:** Cleveland Guardians **5**, Minnesota Twins **2**. Taj Bradley delivered six scoreless innings, Cleveland scored twice in the seventh, Minnesota tied it 2-2, then Cleveland scored three in the ninth.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Twins +1.5 | 60% | **LOSS** — MIN lost by 3 | 0.3600 |
| 2 | Under 7.5 | 54% | **WIN** — 7 runs | 0.2116 |
| 3 | Over 7.5 | 46% | **LOSS** | 0.2116 |
| 4 | Guardians -1.5 | 40% | **WIN** | 0.3600 |

**Potential winner:** Guardians 59% — **WIN**.

**Deep Rank-1 retrospective:** the +1.5 read was not killed by the starting-pitching/low-total premise. It was alive late in a 2-2 game and failed because Cleveland created a three-run ninth-inning separation. This is exactly where a cushion forecast must model **score-state-specific relief quality and late separation**, not merely starter quality or the fact that bullpens had rest.

**What went right:** Messick/Cleveland as the preferred winner and the modest Under direction both aligned with the final. The total centre (~7.3) was close to the actual seven.

**What went wrong:** the card treated off-day bullpen availability as part of a close-game environment, but availability is not quality and does not guarantee the arms used in a particular tied/late state prevent separation. The final margin was produced after the central starter duel had already occurred.

**Knowability:** the exact ninth-inning sequence was not knowable. The late-leverage branch and the possibility that a low total still ends 5-2 rather than 3-2 were knowable and are already required by the baseball rules.

**Learning / proposed placement:** reinforce `RULES_BASEBALL.md` controls 6 and 20 (bullpen freshness is not quality; bullpen availability is score-state specific) and control 17 (low total does not imply close margin). No new rule; add as a negative Rank-1 worked example if the sport file is next revised.

**Settlement sources:** MLB game story `https://www.mlb.com/stories/game/823659/`; Reuters, *Guardians boost playoff hopes with 3-run ninth vs Twins* `https://www.reuters.com/sports/baseball/guardians-boost-playoff-hopes-with-3-run-ninth-vs-twins--flm-2026-09-12/`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-391

- **Final re-verified:** MLB statsapi 823659 (Guardians 5–2).
- **Additional learning:** Rank #1 Twins +1.5 (60%) lost by three after a ninth-inning separation — an underdog cushion (`G-L12`, baseball control 29(a)).
- **Validation:** orders were TBD (`FORCED RANK`); managers were not named.

#### P-392 — Chicago White Sox @ St. Louis Cardinals — MLB


**Verified final:** St. Louis Cardinals **7**, Chicago White Sox **3** — 10 total runs.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Cardinals +1.5 | 65% | **WIN** | 0.1225 |
| 2 | Over 7.5 | 61% | **WIN** | 0.1521 |
| 3 | Under 7.5 | 39% | **LOSS** | 0.1521 |
| 4 | White Sox -1.5 | 35% | **LOSS** | 0.1225 |

**Potential winner:** White Sox 53% — **LOSS**.

**What went right:** the card correctly identified a high-scoring route through two left-handed starters in poor current run-prevention regimes and the actual right/switch-heavy lineups. Cardinals +1.5 and Over 7.5 both won.

**What went wrong:** the separate outright call leaned White Sox at only 53%, essentially a coin flip. St. Louis' current offensive form and home state ultimately won the 1X2-like baseball winner threshold. This is not evidence that the run-line/Over mechanisms were wrong; it shows the winner and margin thresholds must remain separate queries.

**Knowability:** the exact 7-3 score was not knowable. The upper-total mechanism and the fact that St. Louis retained substantial outright-win mass were known pregame.

**Learning / proposed placement:** positive worked example for `RULES_BASEBALL.md` on lineup-handedness being a named mechanism rather than a generic trend scalar, and for deriving winner/run-line separately. No rule change warranted.

**Settlement sources:** MLB Cardinals postgame video `https://www.mlb.com/cardinals/video/joshua-baez-s-three-hit-game-leads-cardinals-to-a-win`; Baseball Almanac box score `https://www.baseball-almanac.com/box-scores/boxscore.php?boxid=202609110SLN`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-392

- **Final re-verified:** MLB statsapi 823012 (Cardinals 7–3).
- **What went right:** the top two both won, with the underdog winning outright. Both posted nines came from MLB's global lineup feed while the team pages lagged — keep that route.

#### P-393 — Seattle Mariners @ Athletics — MLB


**Verified final:** Athletics **6**, Seattle Mariners **5** in **10 innings**. The game was tied 4-4 after nine; Seattle scored once in the top of the 10th and the Athletics scored twice in the bottom half. Final total: **11**.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Under 10.5 | 68% | **LOSS** — 11 runs | 0.4624 |
| 2 | Athletics +1.5 | 58% | **WIN** | 0.1764 |
| 3 | Mariners -1.5 | 42% | **LOSS** | 0.1764 |
| 4 | Over 10.5 | 32% | **WIN** | 0.4624 |

**Potential winner:** Mariners 59% — **LOSS**.

**Deep Rank-1 retrospective:** this is a clean extra-innings failure. Regulation ended 4-4, only eight runs, which was comfortably inside the Under. The card explicitly named the MLB automatic-runner branch as a kill path, but the tie-after-nine probability and the conditional extra-inning scoring distribution were not large enough in the final 68/32 split. Three runs in the 10th crossed 10.5 immediately.

**What went right:** the Athletics +1.5 close-game thesis was correct and strongly coupled to the regulation tie state. The card also explicitly warned that extra innings protect the underdog cushion while raising the Over tail.

**What went wrong:** the qualitative extra-innings warning did not carry sufficient numerical mass. This is precisely the issue `RULES_GENERAL` G-L9 is intended to prevent.

**Knowability:** reaching a tie after nine was uncertain but modelable; the automatic-runner scoring environment was a known rule, not hindsight information.

**Learning / proposed placement:** reinforce `RULES_BASEBALL.md` control 22 / branch `BB-B7`: **quantify P(tie after 9) separately and then integrate the higher-rate automatic-runner state into exact total/run-line probabilities**. This event is an excellent worked example; it is not evidence for a universal adjustment size.

**Settlement sources:** MLB Film Room/Gameday `https://www.mlb.com/video/game/824954`; Baseball-Reference box score `https://www.baseball-reference.com/boxes/ATH/ATH202609110.shtml`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-393

- **Final re-verified:** MLB statsapi 824954 (Athletics 6–5, 10 innings).
- **Additional learning:** Under 10.5 (68%) was correct through nine innings and lost to the automatic-runner 10th — the MLB worked example under baseball control 22, contrasted with P-405. The tie-after-nine branch needed a number (`G-L9`).

#### P-394 — Parramatta Eels Women vs North Queensland Cowboys Women — NRLW


**Verified final:** Parramatta Eels Women **33**, North Queensland Cowboys Women **28** — total **61**, Eels by **5**. North Queensland led 22-6 early in the second half; Parramatta scored three tries in eight minutes, Rachael Pearson broke a 28-28 tie with a late field goal, and Rory Owen sealed it with a late try.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Cowboys Women +10.5 | 58% | **WIN** | 0.1764 |
| 2 | Over 48.5 | 55% | **WIN** | 0.2025 |
| 3 | Under 48.5 | 45% | **LOSS** | 0.2025 |
| 4 | Eels -10.5 | 42% | **LOSS** | 0.1764 |

**Potential winner:** Eels 66% — **WIN**. **Top two both won.**

**What went right:** the forecast separated winner from cover correctly: Parramatta won but did not cover -10.5. The ~8-point margin centre was close to the actual five. The Over also survived through an explicit comeback/terminal-sequence state rather than requiring an Eels blowout.

**What could improve:** the card's central total was ~51, 10 points below the realised 61. The realised match contained exactly the high-variance second-half sequence rugby league rules require: a 16-point lead, rapid multi-try swing, then terminal scoring. The direction was right, but width/branch visibility was more important than the mean.

**Knowability:** Pearson's role, both spines and the possibility of a terminal field-goal sequence were knowable; the exact 22-6 → 28-28 swing was not.

**Learning / proposed placement:** positive worked example for `RULES_NRL_RUGBY.md` `RL-B4` second-half separation/response and `RL-B5` terminal sequence. No rule change or coefficient promotion.

**Settlement source:** NRL official report `https://www.nrl.com/news/2026/09/12/nrlw-saturday-eels-v-cowboys-sharks-v-dragons/`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-394

- **Final:** not re-fetched this pass; the NRL official report (Eels 33–28) is retained.
- **What went right:** Cowboys W +10.5 and the Over 48.5 both won — the high-total close game the card priced (rugby league's underdog cushions 3 / 0).

#### P-395 — Belfast Wolves vs Rotterdam Dockers — European T20 Premier League


**Target activation:** Belfast **did bat first**, so the conditional first-innings card became the correct frozen target.

**Verified result:** Belfast Wolves **161/6**; Rotterdam Dockers **162/3 in 18 overs**, Dockers won by **7 wickets**. Belfast were **49/1 after 6 overs**.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Wolves 20-over Under 171.5 | 62% | **WIN** — 161 | 0.1444 |
| 2 | Wolves first 6 Under 50.5 | 57% | **WIN** — 49 | 0.1849 |
| 3 | Wolves first 6 Over 50.5 | 43% | **LOSS** | 0.1849 |
| 4 | Wolves 20-over Over 171.5 | 38% | **LOSS** | 0.1444 |

**Potential winner:** Rotterdam Dockers ~58% conditional on Belfast batting first — **WIN**. **Top two both won.**

**What went right:** this is a strong process example rather than merely a result hit. The first-six centre was ~49-51 and actual was 49; the 20-over centre was ~158-163 and actual was 161. The card also kept the phase and innings as dependent but non-identical targets.

**What could improve:** confirmed XIs and the exact strip were unavailable at issue, so evidence appropriately remained `FORCED RANK / MEDIUM-LOW`. The accuracy of this one realised card must not be used to retrospectively remove that missingness penalty.

**Knowability:** the target condition (Belfast batting first) became objectively settleable from the toss; exact run totals were uncertain but the pregame corridor captured them well.

**Learning / proposed placement:** add only as a **worked example** under `RULES_CRICKET.md` control 16 (phase-to-innings transition is joint) and target-identity controls. No numerical weighting change.

**Settlement sources:** CricketWorld commentary `https://www.cricketworld.com/cricket/belfast-wolves-vs-rotterdam-dockers/match/commentary/98345`; Statz fixture/scorecard lane `https://statz.ai/cricket/fixtures/71063/belfast-wolves-vs-rotterdam-dockers/scorecard`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-395

- **Final:** not re-fetched this pass; the CricketWorld/Statz scorecards are retained.
- **What went right:** the top two both won (161 and 49) — a positive phase-to-innings example in `RULES_CRICKET.md` §"2026-09-15(b)".

#### P-396 — Brisbane Lions vs Adelaide Crows — AFL Semi Final


**Verified final:** Brisbane Lions **21.18 (144)** defeated Adelaide Crows **13.13 (91)** — margin **53**, total **235**. Combined scoring shots were **65** (Brisbane 39, Adelaide 26), versus the card's central ~50.3-shot construction.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Adelaide +21.5 | 64% | **LOSS** | 0.4096 |
| 2 | Under 188.5 | 58% | **LOSS** | 0.3364 |
| 3 | Over 188.5 | 42% | **WIN** | 0.3364 |
| 4 | Brisbane -21.5 | 36% | **WIN** | 0.4096 |

**Potential winner:** Brisbane 68% — **WIN**.

**Deep Rank-1 / Rank-2 retrospective:** both preferred rows failed together because the match moved into the correlated **high-shot + favourite-separation** branch. The card had explicitly required `AF-B4` and noted Brisbane's 30+ shot ceiling, the 52-point Round-7 same-venue win, and a 202-point direct matchup; however those known branches received only 36% cover mass and 42% Over mass.

**Key diagnostic:** the total miss was driven primarily by **shot volume/territory**, not extraordinary conversion. Brisbane scored ~3.69 points per scoring shot and Adelaide ~3.50; those are not extreme enough to explain a 235 total by themselves. The central forecast's ~50 scoring shots was the more important miss relative to the realised 65.

**What went right:** Brisbane outright and the existence/direction of the high-shot/high-separation kill path. The original framework correctly separated shot creation from conversion.

**What went wrong:** the scenario was described but under-massed. This is a G-L9 execution issue, not evidence that all finals or all Gabba games should be projected higher.

**Knowability:** Brisbane's same-venue ceiling, midfield rebound route and direct high-shot evidence were knowable. The exact 65-shot explosion was not.

**Learning / proposed placement:** reinforce `RULES_AFL.md` control 9 / `AF-B4` and `RULES_GENERAL.md` §16.9 G-L9: for 180+ totals, the high-shot branch must carry an explicit probability mass that also propagates to the margin distribution when the same territory mechanism drives both. Candidate worked example only; no new coefficient.

**Settlement sources:** AFL fixture/result lane `https://www.afl.com.au/fixture`; Guardian final live report `https://www.theguardian.com/sport/live/2026/sep/12/afl-finals-live-updates-brisbane-lions-vs-adelaide-crows-semi-final-2026-latest`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-396

- **Final re-verified:** ESPN AFL 1133707 (Brisbane 144–91).
- **Additional learning:** Adelaide +21.5 and Under 188.5 lost together to the high-shot branch (65 scoring shots against ~50 central). AFL finals underdog cushions went 0 / 2 → `G-L12`, `G-L10`, `RULES_AFL.md` §"2026-09-15(b)".

#### P-397 — Cronulla-Sutherland Sharks vs North Queensland Cowboys — NRL Elimination Final


**Verified final:** Cronulla Sharks **26**, North Queensland Cowboys **16** — total **42**, Sharks by **10**.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Over 48.5 | 56% | **LOSS** | 0.3136 |
| 2 | Cowboys +7.5 | 55% | **LOSS** | 0.3025 |
| 3 | Sharks -7.5 | 45% | **WIN** | 0.3025 |
| 4 | Under 48.5 | 44% | **WIN** | 0.3136 |

**Potential winner:** Sharks 65% — **WIN**.

**Deep Rank-1 / Rank-2 retrospective:** the realised 26-16 score is almost a textbook version of the card's own `RL-B3 low-total separation` family. The card explicitly listed examples such as 28-12, 30-14 and 26-10: Cronulla controls possession/field position, North Queensland's contribution is suppressed, and the Sharks still cover inside an Under. Yet the final masses placed that combined direction below 50% on both components.

**What went right:** Sharks outright, the structural identification of Cronulla's completion/field-position advantage, and the existence of the favourite-cover/Under branch.

**What went wrong:** the central ~50-52 total / ~6 margin over-weighted the competitive scoring branch relative to the possession-native suppression/separation branch. This is not cured by an automatic finals Under adjustment; the specific set/territory mechanism already existed and needed enough mass.

**Knowability:** Cronulla's stronger completion, restored spine and defence were pregame facts. The exact sequence was not.

**Learning / proposed placement:** reinforce `RULES_NRL_RUGBY.md` controls 13-16 and `RL-B3`, plus `RULES_GENERAL.md` G-L9. Use as a negative Rank-1 worked example showing that **low total and favourite cover can coexist**. No prospective reweight from one game.

**Settlement sources:** Sharks official final/fixture lane `https://www.sharks.com.au/news/2026/09/10/fight-fire-with-fire-sparks-set-to-fly-in-heavyweight-battle/`; NRL match page `https://www.nrl.com/news/2026/09/12/sharks-v-cowboys--finals-week-12026/`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-397

- **Final re-verified:** ESPN `rugby-league/3` 604735 (Sharks 26–16).
- **Additional learning:** Over 48.5 and Cowboys +7.5 both lost to the low-total favourite-cover state that RL-B3 had printed — the rugby-league worked example requiring P(R1 ∧ R2).

#### P-398 — Racing Santander vs Deportivo Alavés — La Liga


**Verified final:** Racing Santander **2**, Deportivo Alavés **1**. Half-time **1-1**. Official Racing/LALIGA event data records **4-6 corners = 10 total**.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Combined corners Over 8.5 | 73% | **WIN** — 10 | 0.0729 |
| 2 | 1H Over 0.5 goals | 64% | **WIN** | 0.1296 |
| 3 | FT Under 2.5 goals | 52% | **LOSS** — 3 | 0.2704 |
| 4 | FT Over 2.5 goals | 48% | **WIN** | 0.2704 |
| 5 | 1H Under 0.5 goals | 36% | **LOSS** | 0.1296 |

**Potential regulation winner:** Alavés 39% — **LOSS**; Racing won. The original 1X2 was broad (Racing 34 / Draw 27 / Alavés 39), so this is not a high-confidence side failure.

**What went right:** the separate corner process and early-goal exposure were both directionally correct. Racing had repeatedly conceded/created high corner volume and the match reached 10 despite only three goals, demonstrating that corner and goal processes should remain distinct.

**What went wrong:** the full-match 2.5 total was genuinely close to a coin flip (52/48) and landed at three. There is no evidence here for a stronger structural total rule.

**Knowability / source lesson:** the postgame official club page exposes the league event feed and corner events. This resolves the corner field to a stronger standard than generic aggregators and should be prioritised for future Racing/LALIGA settlements.

**Learning / proposed placement:** no predictive rule change. Add the **Real Racing official match page / embedded LALIGA event-stat feed** as a candidate settlement lane in `SOURCES.md` / `DATA_SOURCE_REGISTER.md` for LALIGA team/corner fields, subject to coverage testing.

**Settlement sources:** Real Racing official match page `https://www.realracingclub.es/partidos/temporada-2026-2027-laliga-ea-sports-5-r-racing-club-vs-deportivo-alaves-2966`; Reuters LALIGA roundup `https://www.reuters.com/sports/soccer/mbappe-scores-brace-real-madrid-secure-routine-victory-over-rayo-vallecano-2026-09-12/`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-398

- **Final re-verified:** ESPN `esp.1` 401882881 (Racing 2–1). ESPN corners 4+6 = 10 match the official LALIGA event feed, so the Rank #1 corners WIN is confirmed.
- **What went right:** settlement at the official event record — the model for `RULES_GENERAL.md` §16.10(j).

#### P-400 — Trinbago Knight Riders Women vs Guyana Amazon Warriors Women — WCPL


**Target activation:** Guyana Amazon Warriors Women **batted first**, so the conditional innings/phase contracts were active.

**Verified result:** Guyana **119/8**, with **33 runs after six overs**; TKR **94/9**. Guyana won by **25 runs**.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Warriors first 6 Under 37.5 | 64% | **WIN** — 33 | 0.1296 |
| 2 | Warriors 20-over Under 132.5 | 60% | **WIN** — 119 | 0.1600 |
| 3 | Warriors 20-over Over 132.5 | 40% | **LOSS** | 0.1600 |
| 4 | Warriors first 6 Over 37.5 | 36% | **LOSS** | 0.1296 |

**Potential winner:** TKR Women 69% — **LOSS**.

**What went right:** both target-side scoring forecasts were correct. The card explicitly separated a slow powerplay from a still-respectable full innings, and Guyana again started slowly before reaching 119.

**What went wrong:** the winner model was materially overconfident relative to the score forecast. A 119 target was treated as evidence for TKR chase superiority, but cricket winner control 6 requires a separate question: **is that target defendable against this confirmed/current chasing unit?** TKR collapsed to 94/9.

**Knowability:** the exact chase collapse was not knowable. Guyana's bowling resources and the independence of match-winner probability from first-innings total direction were knowable structural requirements.

**Learning / proposed placement:** strong negative worked example for `RULES_CRICKET.md` control 6 (`Winner independence`) and the limited-overs joint-target section. Add to `LEARNING_REGISTER.md` only as a candidate/process example; do not fit a generic “low total is defendable” coefficient.

**Settlement source:** Cricbuzz scorecard `https://m.cricbuzz.com/live-cricket-scorecard/161777/gaww-vs-tkrw-4th-match-womens-caribbean-premier-league-2026`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-400

- **Final:** not re-fetched this pass; the Cricbuzz scorecard is retained.
- **Additional learning:** both innings Unders won, but the TKR winner label lost — innings totals and the winner are independent targets (`RULES_CRICKET.md` §"2026-09-15(b)").

#### P-403 — Colorado Rockies @ Detroit Tigers — MLB


**Verified final:** Detroit Tigers **11**, Colorado Rockies **7** — total **18**. Colorado led **7-4 entering the eighth** before Detroit scored **seven runs in the eighth inning**.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Rockies +1.5 | 57% | **LOSS** | 0.3249 |
| 2 | Over 8.5 | 54% | **WIN** | 0.2116 |
| 3 | Under 8.5 | 46% | **LOSS** | 0.2116 |
| 4 | Tigers -1.5 | 43% | **WIN** | 0.3249 |

**Potential winner:** Tigers 61% — **WIN**.

**Deep Rank-1 retrospective:** Colorado +1.5 was winning outright late and then failed on one seven-run inning. The preferred cushion therefore failed through **late score-state bullpen/cluster separation**, not because the pregame side read never had a chance.

**What went right:** Detroit outright and the Over. The card recognised Detroit's stronger winning profile and a meaningful upper-scoring branch.

**What went wrong:** the late relief chain and clustered-inning tail were not large enough in the margin distribution. A +1.5 line is especially exposed to one late multi-run inning even when the underdog leads for most of the game.

**Knowability:** the exact seven-run eighth was not; score-state relief alternatives, inherited runners and cluster risk were.

**Learning / proposed placement:** reinforce `RULES_BASEBALL.md` controls 6, 20 and 21. Add as another worked example that **bullpen availability/rest cannot be converted into cushion safety** and that total/separation tails are coupled. No new weight.

**Settlement source:** Reuters `https://www.reuters.com/sports/baseball/hao-yu-lee-fuels-tigers-comeback-win-over-rockies--flm-2026-09-12/`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-403

- **Final re-verified:** MLB statsapi 824224 (Tigers 11–7).
- **Additional learning:** Rockies +1.5 (57%) lost to a seven-run Detroit eighth — an underdog cushion (`G-L12`, baseball control 29(a)). The separation family needed a number (`G-L9`).

#### P-404 — Seattle Mariners (Bryan Woo) @ Athletics (Gage Jump) — MLB


**Verified final:** Seattle Mariners **19**, Athletics **1** — total **20**, margin **18**. Seattle hit five home runs; Bryan Woo allowed only an unearned run over six innings.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Under 9.5 | 61% | **LOSS** | 0.3721 |
| 2 | Athletics +1.5 | 55% | **LOSS** | 0.3025 |
| 3 | Mariners -1.5 | 45% | **WIN** | 0.3025 |
| 4 | Over 9.5 | 39% | **WIN** | 0.3721 |

**Potential winner:** Seattle 63% — **WIN**.

**Deep Rank-1 retrospective:** the Under was defeated almost entirely by **one team**. Oakland scored only one, so Woo's strong starter branch occurred; it did *not* protect the game Under because Seattle's offense produced 19. The original Under thesis therefore over-coupled “Seattle starter suppresses Oakland” with “game stays low.”

**What went wrong:** the Gage Jump/first-relief blow-up and Seattle HR-cluster branch did not receive enough mass. Once the Athletics pitching state failed, the same mechanism also killed +1.5 and won Seattle -1.5.

**Knowability:** an 18-run margin was not knowable. The favourite-only scoring route, five-HR-type cluster tail and starter-to-relief cascade were modelable states.

**Learning / proposed placement:** reinforce `RULES_BASEBALL.md` controls 19 and 21 plus `RULES_GENERAL` G-L9: **a strong opponent starter only constrains one team marginal; a game Under still requires the favourite's own scoring tail to be controlled**. Consider a worked-example note analogous to NRL's “one team can carry the total”, but do not promote a new coefficient/rule from this one result.

**Settlement source:** Reuters MLB roundup `https://www.reuters.com/sports/mlb-roundup-mariners-clobber-as-by-franchise-record-18-runs--flm-2026-09-13/`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-404

- **Final re-verified:** MLB statsapi 824955 (Mariners 19–1).
- **Additional learning:** Under 9.5 and Athletics +1.5 lost together because Seattle alone carried the game — the one-team-total kill path added to `RULES_BASEBALL.md` §"2026-09-15(b)" (`G-L10`).

#### P-405 — Chunichi Dragons @ Hanshin Tigers — NPB


**Verified final:** Chunichi Dragons **1**, Hanshin Tigers **0** in **11 innings**. The game was scoreless through ten; Chunichi scored once in the top of the 11th and Hanshin failed to answer.

| Rank | Frozen contract | Issued `p` | Settlement | Brier |
|---:|---|---:|---|---:|
| 1 | Dragons +1.5 | 60% | **WIN** | 0.1600 |
| 2 | Under 5.5 | 55% | **WIN** | 0.2025 |
| 3 | Over 5.5 | 45% | **LOSS** | 0.2025 |
| 4 | Tigers -1.5 | 40% | **LOSS** | 0.1600 |

**Potential winner:** Hanshin 57% — **LOSS**. **Top two both won.**

**What went right:** the close-game/low-run structure was strongly correct. Dragons +1.5 and Under both survived even through extra innings.

**What went wrong:** the slight Hanshin winner lean failed in a one-run extra-inning state. This is a threshold issue rather than evidence the low-total model was wrong.

**Competition-rule lesson:** do not transfer MLB's automatic-runner extra-inning scoring environment to NPB. The actual extra frames remained low scoring. Extra-inning branches must use the exact competition rules already frozen in `LEAGUE_RULES_BASEBALL`/`RULES_BASEBALL.md`.

**Knowability:** the one-run/tie-after-nine branch was knowable; which side scored the lone run was inherently uncertain.

**Learning / proposed placement:** positive worked example for competition-specific extra-inning modelling and winner-vs-cushion separation. No rule change.

**Settlement source:** Yahoo! Japan SportNavi inning-by-inning score `https://baseball.yahoo.co.jp/npb/game/2021039417/score?index=1120301`.

**Disposition:** **SETTLED / CLOSED**.


##### 2026-09-15 canonical settlement audit — P-405

- **Final re-verified:** NPB English scoreboard for 13 Sep — Chunichi 1–0 Hanshin. The 11-inning detail comes from SportsNavi; the NPB scoreboard page does not show innings.
- **What went right:** the top two both won; the underdog won outright.
- **Additional learning:** NPB extras have no automatic runner and a 12-inning tie limit — the contrast to P-393 under baseball control 22.

> **2026-09-15(b) update to P-402 (this pass):** `P-402-C02` Combined corners Over 8.5 and `P-402-C03` Tottenham team corners Over 4.5 are now **settled WIN** at the Premier League official data record (fixture **128962**: Tottenham 5, Everton 6 = 11). Row Briers 0.0676 and 0.0841; card mean over 5 rows 0.1710. `TMP-OPEN-20260914-04`/`-05` retired. The provisional wording in the P-402 block above is preserved as the external session wrote it.

### Cross-log audit — `P-373`–`P-423` (learning-only; descriptive)

#### Settlement roll-up

| Cohort | Issued cards | Admin / no forecast | Graded rows | W / L | Mean Brier | Rank #1 | Rank #2 | Top two both won (both graded) | Potential winners | Preferred scoring O/U | Rows still open |
|---|---:|---:|---:|---|---:|---|---|---|---|---|---:|
| Log A `P-373`–`P-389` | 16 | 1 (`P-389`) | 66 | 33 / 33 | 0.2449 | 10 W / 6 L | 8 W / 7 L | 6 / 15 | 11 / 16 | 9 / 16 | 1 |
| Log B `P-390`–`P-406` | 17 | 0 | 67 | 35 / 32 | 0.2278 | 9 W / 6 L (+1 prov, +1 unresolved) | 11 W / 5 L | 7 / 14 | 9 / 17 | 11 / 17 | 5 |
| Log C `P-407`–`P-423` | 16 | 1 (`P-415`) | 61 | 39 / 22 | 0.2088 | 6 W / 8 L (+1 prov) | 10 W / 4 L (+1 prov) | 3 / 13 | 14 / 15 (+`P-418` open) | 12 / 15 | 4 rows + `P-418` |
| **Import total** | **49** | **2** | **194** | **107 / 87** | **0.2276** | **25 W / 20 L** | **29 W / 16 L** | **16 / 42** | **34 / 48** | **32 / 48** | — |

Every Brier printed in logs A and B was recomputed from its issued probability and result: **131 of 131 reproduce exactly**. Log B's mean changes from 0.2325 to 0.2278 only because `P-402-C02`/`C03` are now booked. "Preferred scoring O/U" = the highest-ranked goal/run/point total (game, team or phase) on each card, corners and handicaps excluded. The W/L split over all rows is partly mechanical (complementary pairs) and is **not** a selection-skill statistic.

#### Finding 1 — Rank-#1 underdog cushions lose more often than their probabilities say (cross-sport)

Rank-#1 handicap rows on the side of the team **not** named as potential winner, `P-345`–`P-423`:

| Sport | Cards (result) | W / L |
|---|---|---|
| Baseball (+1.5) | P-349 W, P-365 L, P-373 L, P-383 L, P-391 L, P-392 W, P-403 L, P-405 W, P-417 W, P-420 L | 4 / 6 |
| American football | P-376 W, P-412 L, P-413 L, P-414 L, P-422 L | 1 / 4 |
| Basketball | P-359 W, P-411 L | 1 / 1 |
| Rugby league | P-363 W, P-386 W, P-394 W | 3 / 0 |
| AFL | P-388 L, P-396 L | 0 / 2 |
| Soccer (+1.5) | P-402 W | 1 / 0 |
| **Total** | **23 rows, mean stated p = 0.61 (expected ≈ 14.0 wins)** | **10 / 13 (43%)** |

For contrast, Rank-#1 **favourite** handicaps (P-361, P-367, P-371, P-380, P-381, P-382, P-384, P-385, P-421, P-423) went **7 / 3** at a mean stated 0.57. The descriptive standard error on 23 rows at p = 0.61 is about 0.10, so the 17-point shortfall is roughly 1.7 SE — **suggestive, not established** (`RULES_GENERAL.md` §16.9: no threshold rule). Rugby league is the exception (3 / 0). No coefficient follows (`L-087`).

#### Finding 2 — margin centres were pulled toward pick'em (log C, where centres were printed)

| Card | Printed favourite margin centre | Actual (favourite-signed) | Residual |
|---|---:|---:|---:|
| P-411 basketball | +5.2 | +23 | +17.8 |
| P-412 NFL | ≈ +6.0 | +7 | +1.0 |
| P-413 NFL | +1.3 | +18 | +16.7 |
| P-414 NFL | +0.7 | +5 | +4.3 |
| P-422 NFL | +1.0 | +21 | +20.0 |
| P-416 MLB | +1.4 | +2 | +0.6 |
| P-420 MLB | +0.3 | +4 | +3.7 |
| P-421 MLB | +1.3 | +5 | +3.7 |
| P-423 MLB | +1.2 | +1 | −0.2 |
| P-417 NPB (Hanshin as favourite) | +0.6 | −6 | −6.6 |

Mean residual **+6.1**, **8 of 10 toward the favourite**. The NFL cards used a margin width of ~10.5 points; the classic published estimate of the spread-to-result standard deviation in the NFL is about **13.9 points** (Stern, 1991, *The American Statistician* 45(3)) — a methodology reference, not a predictive feature. So the NFL margin tables were both too central and too narrow: both tails were under-massed. The earlier basketball-only candidate `C-UNDERDOG-SEPARATION` assumed the opposite direction (underdog states under-weighted; P-358/P-359/P-371); this cohort's P-411 runs the other way. **Disposition:** the candidate is generalised to `C-MARGIN-TAIL-MASS` (both tails, all sports) and the disclosure requirement `G-L12` is added.

Totals residuals (actual − centre): P-413 +16.1 and P-414 +22.9 (NFL, both "defensive" Unders), P-422 −0.8, P-411 −7.4; MLB P-416 −5.4, P-420 +0.5, P-421 +2.3, P-423 +3.8 (MLB mean **+0.3**, n=4 — no support in this cohort for `C-RUN-CENTRE-BIAS`'s "centres run high" direction).

#### Finding 3 — calibration of the 194 new rows (descriptive; complements are dependent)

| Stated p | Rows | Mean stated | Won |
|---|---:|---:|---:|
| < 0.40 | 21 | 0.36 | 0.29 |
| 0.40–0.50 | 62 | 0.45 | 0.53 |
| 0.50–0.60 | 64 | 0.55 | 0.48 |
| 0.60–0.70 | 26 | 0.64 | 0.65 |
| 0.70–0.80 | 14 | 0.74 | 0.93 |
| ≥ 0.80 | 7 | 0.84 | 1.00 |

Rank-#1 rows stated 0.50–0.60 won **10 of 22 (45%)** against a mean 0.56 — this is where the Rank-#1 losses concentrate, and it is the underdog-cushion band. Rows stated ≥ 0.70 won **19 of 21**: `C-PROB-EXTREMITY` (13 of 21 in `P-345`–`P-371`) is **not** supported this time (combined 32 of 42 against a mean stated ≈ 0.75). Both are recorded; neither changes a rule.

#### Finding 4 — what went right, and why

- **Large-edge goal-based soccer rows:** in log C the team-goal, double-chance, first-half-Over and Under-3.5/Over-2.5 rows went **19 W / 1 L** (mean stated ≈ 0.74). They rested on current chance creation (xG, shots on target) and home process, not streaks — the positive pattern first recorded at P-346 (soccer control 31).
- **Winner labels:** 34 of 48 across the import (14 of 15 in log C). The cards identified the better team; the misses were about **by how much**.
- **Positive process models to copy:** P-375 (tennis deciding-set tree mapped to the realised 3-set match), P-379 (cricket phase → innings tree, 24/0 after 5 then 335/9), P-380 (rugby-league low-total favourite-separation branch realised 22–10), P-395 (ETPL phase → innings), P-421 (official starter identity over stale previews), P-409/P-410 (direct corner/xG process), P-389 and P-415 (withheld/not-issued cards not retro-scored).
- **Settlement discipline:** logs A/B refused to book corner rows on secondary displays; this pass booked two of them only once the Premier League's own record was reached.

#### Audit of the imported log A / log B retrospectives

| Imported claim | Audit | Disposition |
|---|---|---|
| A's CAND-MINI-G / B's §8.2-A: "named kill paths still need numeric mass" (P-373, P-382, P-388, P-390, P-393, P-396, P-397, P-403, P-404) | **Agree.** Six Rank-#1 losses in B and three in A had the deciding branch printed. | Recurrence of `G-L9`; recorded in the pattern review. |
| A's CAND-MINI-H: "international Week-1 prior-transfer uncertainty belongs in width" (P-376) | **Agree, and it generalises.** Log C's four NFL cards show the uncertainty was put into the centre. | Folded into `G-L12`. |
| B's §8.2-B: "not 'bet favourites'" | **Agree on the wording, but incomplete.** Across 23 Rank-#1 underdog cushions the favourite separated more often than stated; B attributed P-391/P-403 to late bullpens only. | `G-L12` + `C-MARGIN-TAIL-MASS`; no coefficient. |
| B's P-364 retirement from a Reuters report | **Agree** with the result; the canonical settlement used the ESPNcricinfo scorecard (2026-09-15(a)). | No change. |
| B's five provisional corner wins "cannot be booked" | **Two changed:** P-402-C02/C03 settled at the Premier League official record (5+6=11; Tottenham 5). P-399-C02 and P-401-C01/C03 stay provisional — ESPN (Opta lineage) agrees with the secondary counts (17, 17, 8), but no Serie A / Allsvenskan record was reached. | Handles `-04`/`-05` retired; `-01`–`-03` kept. |
| A's P-387-C03 settled at J.League official `CK = 7` | **Agree;** ESPN also shows Kyoto 7. | Confirmed. |
| A's reconciliation: P-374 = same event as `TMP-SETTLED-20260911-01` | **Agree.** ESPN event 401915444 confirms Fenerbahçe 1–1 Roma, corners 1+3 = 4 (P-374 Under 9.5 WIN). | `TMP-SETTLED-20260911-01` retired into canonical P-374. |

Independent re-verification of logs A and B finals at settlement (2026-09-15): MLB statsapi (P-373, P-390–P-393, P-403, P-404 — including P-393's 10-inning 6–5), NPB English scoreboards (P-381–P-383, P-405 1–0), KBO English scoreboard (P-384, P-385), ESPN NFL (P-376 49ers 27–7), ESPN AFL (P-388 Fremantle 120–106; P-396 Brisbane 144–91), ESPN NRL (P-386 Knights 20–10; P-397 Sharks 26–16), ESPN soccer (P-374, P-377 0–0, P-387 2–3, P-398 2–1 with corners 4+6, P-399 1–1 corners 8+9, P-401 2–1 corners 8+9, P-402 0–0 corners 5+6). **All agree with the mini logs.** Not independently re-checked this pass: P-375, P-378, P-379, P-380, P-394, P-395, P-400, P-406 (their own settlement sources are retained).

#### 25-card `PRIMARY_SCORED` pattern review (`METHOD.md` §7.2) — triggered by this import

`PRIMARY_SCORED` card count reached **25**: the 8 counted before this import plus P-373, P-386, P-388, P-390, P-391, P-392, P-393, P-396, P-397, P-402, P-403, P-404, P-408, P-416, P-420, P-421, P-423 (NRLW cards are not counted, matching the earlier scorecard).

| Measure | Value |
|---|---|
| Running `PRIMARY_SCORED` rows | **104**, 55 W / 49 L, mean Brier **0.2522** — slightly *worse* than the 0.5 baseline (0.2500) |
| MLB | 68 rows, 35 W / 33 L, **0.2473** |
| EPL | 20 rows, 12 W / 8 L, **0.2267** |
| NRL / AFL | 16 rows, 8 W / 8 L, **0.3053** |
| This import's 70 `PRIMARY_SCORED` rows | 0.2595; stated 0.60–0.70 rows won 4 of 11; stated 0.40–0.50 rows won 14 of 21 |

**Recurring "smallest change" answers (3+ in the 25-card window):**

1. **Margin centre pulled toward zero / favourite-separation mass missing** — P-373, P-391, P-396, P-403, P-420 (plus non-primary P-411, P-413, P-414, P-422). → **`G-L12` disclosure requirement** + `C-MARGIN-TAIL-MASS` manifest.
2. **Named kill path without enough mass** — P-373, P-393, P-396, P-397, P-403, P-404, P-420. → already `G-L9`; the §16.8 completeness audit now requires the complement to list the favourite-separation, extra-innings and home-last-bat branches with numbers where they apply.
3. **Line-ups / managers not captured** — every MLB card in the window (orders "TBD" or secondary; managers never named). → existing `G14.2`; retrieval route test opened (MLB statsapi game feed `battingOrder` before first pitch).
4. **Derivative provider not frozen** — P-402, P-408 (both resolvable at the Premier League record). → soccer control 32 pre-registers that record for EPL.

**Honest reading:** after 25 cards the primary population is not beating a coin flip on Brier. The winner identification is sound; the margin and cushion rows are where the score is lost.

#### Over/under — the standing directive (at least one O/U should win)

- **Preferred scoring O/U (one per card):** 32 of 48 across the import (log A 9/16, B 11/17, C 12/15). By direction: Over-preferred **20 of 27**, Under-preferred **13 of 22**. In `P-345`–`P-371` the pattern was reversed (Over-favoured cards 1 of 5). **There is no stable directional edge; nothing here justifies an Over or Under preference.**
- **What actually made O/U rows win:** a large, mechanism-backed edge on a **team** or **phase** target (log C soccer team-goal and first-half rows 11/11; cricket phase rows P-379, P-395, P-400 3/3), not the main game line.
- **What made them lose together:** one thesis setting both top rows (P-413 and P-414: "controlled, defensive game" → underdog cushion **and** Under; both lost to the same favourite blow-out). `P(at least one preferred O/U wins) = pA + pB − P(A ∧ B)` must be printed whenever two top rows share a driver (`G-L10`).
- **Research-backed changes adopted (disclosure only):** (1) centre and width from the sport's own residuals, not shrunk toward the line; (2) for NFL totals, a Week-1 prior carries prior-season defensive ratings as width (P-414); (3) print exact-integer masses where lines are integers (P-413 at 3, P-416/P-421/P-423 run totals at 8 and 11); (4) keep `C-PHASE-VS-FULL-TOTAL` open — soccer 1H Over 0.5 when preferred went 7 of 9 in the import (P-374, P-398, P-399, P-407, P-408, P-409, P-410 W; P-377, P-402 L).

#### Temporary IDs — logs needing a handle

| Handle | Row | Why open | Retry trigger |
|---|---|---|---|
| `TMP-OPEN-20260912-01` | P-377-C02 corners O8.5 | Secondary 7; ESPN `gua.1` summary exposes **no** statistics | Liga Bantrab / data-partner corner record |
| `TMP-OPEN-20260914-01` | P-399-C02 corners O8.5 | ESPN 17 (8+9), secondaries agree; no Serie A record reached | Lega Serie A match-centre record |
| `TMP-OPEN-20260914-02` / `-03` | P-401-C01 / C03 | ESPN 17 and IFK 8; no Allsvenskan record | Allsvenskan / SEF record |
| `TMP-OPEN-20260914-06` | P-406-C01 / C04 six-over rows | exact 6.0-over score not recovered | ball-by-ball or official scorecard at 6.0 |
| **`TMP-OPEN-20260915-01`** | P-407-C01 Brugge corners O4.5 | ESPN 9; Pro League record not reached | Pro League match centre |
| **`TMP-OPEN-20260915-02`** | P-409-C02 Troyes corners O2.5 | ESPN 5; LFP record not reached | LFP / Ligue 1 match centre |
| **`TMP-OPEN-20260915-03`** | P-410-C05 Leipzig corners O4.5 | ESPN 8; DFL record not reached | bundesliga.com match facts |
| **`TMP-OPEN-20260915-04`** | **P-418 whole card** | Identity/state conflict — the fixture is not verified as played | dated BFF/BBS fixture or report naming Drukpa's 13–15 Sep opponent |
| **`TMP-OPEN-20260915-05`** | P-419-C05 corners O7.5 | ESPN 4; Allsvenskan record not reached | Allsvenskan record |
| retired | `TMP-OPEN-20260914-04`/`-05` (P-402 corners) | settled WIN at the Premier League record | — |
| retired | `TMP-SETTLED-20260911-01`, `TMP-RECON-20260912-01` | merged into canonical P-374 | — |

**No ID collision required a new `TMP-SETTLED` handle.** `P-372` is declared **RESERVED / UNUSED** (never issued; not to be reused). The external IDs `P-373`–`P-423` are canonical as issued. **Next canonical ID: `P-424`.**

### Status of every record in this import — `P-372`–`P-423`

| ID | Event | Status | Ranked-row results (W / L / P = provisional) |
|---|---|---|---|
| P-372 | — | RESERVED / UNUSED — no record was ever issued under this ID (both external sessions started at P-373 / P-390 / P-407) | none |
| P-373 | Tampa Bay Rays @ Atlanta Braves — MLB — 2026-09-10 (Atlanta local) | FINAL / SETTLED | L W L W |
| P-374 | Fenerbahçe vs Roma — UEFA Champions League — 2026-09-10 | FINAL / SETTLED — canonical record for Fenerbahçe v Roma; absorbs TMP-SETTLED-20260911-01 | W W W L L |
| P-375 | Coco Gauff vs Elena Rybakina — US Open Women — Semifinal | FINAL / SETTLED | W W L L |
| P-376 | San Francisco 49ers vs Los Angeles Rams — NFL Week 1 — Melbourne | FINAL / SETTLED | W L W L |
| P-377 | Xelajú MC vs Cobán Imperial — Guatemala Liga Nacional Apertura 2026 | FINAL / PARTIAL — C02 corners provisional (TMP-OPEN-20260912-01) | L P L W W |
| P-378 | Philippines vs Bahrain — 2026 Aichi-Nagoya Asian Games Men's Basketball | FINAL / SETTLED | L L W W |
| P-379 | Namibia vs South Africa — 2nd ODI — South Africa tour of Namibia 2026 | FINAL / SETTLED | W W L L |
| P-380 | Wests Tigers (W) vs Canberra Raiders (W) — NRLW Round 11, 2026 | FINAL / SETTLED | W W L L |
| P-381 | Chiba Lotte Marines @ Fukuoka SoftBank Hawks — NPB Pacific League | FINAL / SETTLED | W W L L |
| P-382 | Saitama Seibu Lions @ Orix Buffaloes — NPB Pacific League | FINAL / SETTLED | L W W L |
| P-383 | Yokohama DeNA BayStars @ Hiroshima Toyo Carp — NPB Central League | FINAL / SETTLED | L L W W |
| P-384 | Kiwoom Heroes @ Samsung Lions — KBO League | FINAL / SETTLED | W W L L |
| P-385 | KT Wiz @ Lotte Giants — KBO League | FINAL / SETTLED | W L W L |
| P-386 | South Sydney Rabbitohs vs Newcastle Knights — NRL Finals Week 1 Elimination Final | FINAL / SETTLED | W L W L |
| P-387 | Kyoto Sanga F.C. vs Kashiwa Reysol — J1 League | FINAL / SETTLED | W L L W L |
| P-388 | Fremantle Dockers vs Geelong Cats — AFL First Semi-Final | FINAL / SETTLED | L L W W |
| P-389 | Dublin Guardians vs Edinburgh Castle Rockers — ETPL 2026 Match 21 | ADMINISTRATIVE / NO FORECAST (toss gate withheld correctly) | none issued |
| P-390 | Cincinnati Reds @ Milwaukee Brewers — MLB | FINAL / SETTLED | W L W L |
| P-391 | Cleveland Guardians @ Minnesota Twins — MLB | FINAL / SETTLED | L W L W |
| P-392 | Chicago White Sox @ St. Louis Cardinals — MLB | FINAL / SETTLED | W W L L |
| P-393 | Seattle Mariners @ Athletics — MLB | FINAL / SETTLED | L W L W |
| P-394 | Parramatta Eels Women vs North Queensland Cowboys Women — NRLW | FINAL / SETTLED | W W L L |
| P-395 | Belfast Wolves vs Rotterdam Dockers — European T20 Premier League | FINAL / SETTLED | W W L L |
| P-396 | Brisbane Lions vs Adelaide Crows — AFL Semi Final | FINAL / SETTLED | L L W W |
| P-397 | Cronulla-Sutherland Sharks vs North Queensland Cowboys — NRL Elimination Final | FINAL / SETTLED | L L W W |
| P-398 | Racing Santander vs Deportivo Alavés — La Liga | FINAL / SETTLED | W W L W L |
| P-399 | Genoa vs Frosinone — Serie A | FINAL / PARTIAL — C02 corners provisional (TMP-OPEN-20260914-01) | W P W L L |
| P-400 | Trinbago Knight Riders Women vs Guyana Amazon Warriors Women — WCPL | FINAL / SETTLED | W W L L |
| P-401 | IFK Göteborg vs Halmstads BK — Allsvenskan | FINAL / PARTIAL — C01, C03 corners provisional (TMP-OPEN-20260914-02/-03) | P W P L W |
| P-402 | Tottenham Hotspur vs Everton — Premier League | FINAL / SETTLED (2026-09-15: corners settled at Premier League official record; TMP-OPEN-20260914-04/-05 retired) | W W W L L |
| P-403 | Colorado Rockies @ Detroit Tigers — MLB | FINAL / SETTLED | L W L W |
| P-404 | Seattle Mariners (Bryan Woo) @ Athletics (Gage Jump) — MLB | FINAL / SETTLED | L L W W |
| P-405 | Chunichi Dragons @ Hanshin Tigers — NPB | FINAL / SETTLED | W W L L |
| P-406 | Edinburgh Castle Rockers vs Amsterdam Flames — ETPL Match 24 | FINAL / PARTIAL — six-over rows unresolved (TMP-OPEN-20260914-06) | P L W P |
| P-407 | Club Brugge vs Royal Antwerp FC — Belgium Jupiler Pro League | FINAL / PARTIAL — C01 corners provisional (TMP-OPEN-20260915-01) | P W W L W |
| P-408 | Coventry City vs Brighton & Hove Albion — English Premier League | FINAL / SETTLED | L W W W W |
| P-409 | Lille OSC vs ESTAC Troyes — French Ligue 1 | FINAL / PARTIAL — C02 corners provisional (TMP-OPEN-20260915-02) | W P W W W |
| P-410 | RB Leipzig vs Hamburger SV — German Bundesliga | FINAL / PARTIAL — C05 corners provisional (TMP-OPEN-20260915-03) | W W W W P |
| P-411 | Spain (W) vs Germany (W) — FIBA Women's Basketball World Cup 2026, 3rd Place | FINAL / SETTLED | L W L W |
| P-412 | Atlanta Falcons @ Pittsburgh Steelers — NFL Regular Season Week 1 | FINAL / SETTLED | L W L W |
| P-413 | Baltimore Ravens @ Indianapolis Colts — NFL Regular Season Week 1 | FINAL / SETTLED | L L W W |
| P-414 | Buffalo Bills @ Houston Texans — NFL Regular Season Week 1 | FINAL / SETTLED | L L W W |
| P-415 | LA Angels @ Washington Nationals — MLB | ADMINISTRATIVE / NOT ISSUED (interrupted) | none issued |
| P-416 | New York Mets @ New York Yankees — MLB | FINAL / SETTLED | W L W L |
| P-417 | Chunichi Dragons @ Hanshin Tigers — NPB Central League | FINAL / SETTLED | W L W L |
| P-418 | Drukpa FC vs Royal Thimphu College (RTC) FC — Bhutan Premier League | OPEN — IDENTITY/STATE CONFLICT: fixture not verified as played (TMP-OPEN-20260915-04) | none issued |
| P-419 | Djurgårdens IF vs GAIS — Sweden Allsvenskan | FINAL / PARTIAL — C05 corners provisional (TMP-OPEN-20260915-05) | W W W W P |
| P-420 | Atlanta Braves @ Chicago Cubs — MLB | FINAL / SETTLED | L W L W |
| P-421 | New York Yankees @ Minnesota Twins — MLB | FINAL / SETTLED | W W L L |
| P-422 | Denver Broncos @ Kansas City Chiefs — NFL Regular Season Week 1 | FINAL / SETTLED | L W L W |
| P-423 | San Diego Padres @ Colorado Rockies — MLB | FINAL / SETTLED | L W W L |

### Rule, register and source changes made in this pass

- `RULES_GENERAL.md` §16.10 — `G-L12` margin centre/width; fixture identity; official-record derivative settlement; import checks.
- Sport files §"2026-09-15(b)" — American football controls 17–19; baseball 29; basketball 25; soccer 32–33; cricket, NRL, AFL, tennis, ice hockey and rugby union instantiations/worked examples.
- `LEARNING_REGISTER.md` §"2026-09-15(b)" — L-20260915-06…-19 and the `C-MARGIN-TAIL-MASS` manifest.
- `SOURCES.md` §"2026-09-15(b)" — Premier League official data API (field owner), ESPN coverage, BBS/BFF, and the lanes found by logs A/B.
- `CONTROLS.md`, `METHOD.md`, `README.md`, `GAME_LOG_STATUS_CURRENT.md`, `GAME_LOG_STATUS_INDEX_2026-09-05.md` — dated addenda and ledger rows.


## 2026-09-15(c) — Part 3 closed at `P-423`; Part 4 opened

Per user directive, this file is **closed** after the `P-373`–`P-423` import. `PREDICTION_LOG_COMBINED_4.md` opened empty at **`P-424`** and is now the only file that accepts new forecasts; its top snapshot is the sole queue and next-ID authority.

| Item | Disposition |
|---|---|
| ID range held here | `P-333`–`P-423` (`P-372` RESERVED / UNUSED) |
| Live events at closure | None |
| Open rows issued here (13 handles) | Stay in this file's custody and are settled here when a retry trigger is met: `TMP-OPEN-20260909-01`/`-02`, `-20260911-01`/`-02`, `-20260912-01`, `-20260914-01`/`-02`/`-03`/`-06`, `-20260915-01`…`-05` (incl. the P-418 identity conflict) |
| Part-2 appendix rows (9 handles) | Unchanged — custody stays with `PREDICTION_LOG_COMBINED_2.md` |
| Running scorecard at closure | Mixed 371 rows, mean Brier 0.2352; `PRIMARY_SCORED` 104 rows, 0.2522, card count 25 (first review done). Carried into Part 4's snapshot |
| Controls carried forward | `G-L1`–`G-L12`, `RULES_GENERAL.md` §16.8–§16.10 and the latest sport controls, all restated in Part 4's "Controls carried forward" table |


## 2026-09-16 — queue retry; `P-406` six-over rows settled; `P-418` evidence corrected; external variant C′ of log C reconciled

**LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.**
- **Method:** `MDS-2026.09.06-v4.0`, read from `METHOD.md` this session.
- **Pass type:** a settlement-custody update to this closed part — closed parts accept settlement updates (§"2026-09-15(c)").
- **No card issued.** The next ID is `P-424`, in Part 4.
- Every issued probability and rank is unchanged.

### Inventory and live-state check (first step)

| Location searched (2026-09-16) | Finding |
|---|---|
| Repository tree (every `PREDICTION_MINI*`; files from the last three days) | No new file. `prediction logs/` holds only August component logs |
| `Downloads` (files newer than 2026-09-15 16:00) | Three mini logs. Two are byte-identical to archived logs A and B. **One is an unarchived variant:** `PREDICTION_MINI_RUNNING_LOG_P407_P423_FULL_RETROSPECTIVE_2026-09-15.md` (**C′**) |
| Google Drive (`modifiedTime > 2026-09-14`, title and fullText search) | Only the repository's own synced files (2026-09-15, 09:2x UTC); no new mini log |

**No event is live.** Every issued event through `P-423` is final. `P-418`'s result has not been recovered (see below).

### Component fingerprint — external variant C′

| Log | File | Bytes | SHA-256 | Range | State |
|---|---|---:|---|---|---|
| C′ | `PREDICTION_MINI_RUNNING_LOG_P407_P423_FULL_RETROSPECTIVE_2026-09-15.md` | 266,045 | `f0c77cf8df3b9614422ceb5ad55b684835b3b0fdbe20c6be45fce5765214edc0` | P-407–P-423 | Settled by log C's own external session. Written to Downloads at 2026-09-15 16:46 AEST, 25 minutes after log C's unsettled raw file (`404903fc…`) was archived. The 2026-09-15(b) import never saw it |

- **Archive:** the raw file is at `archive/mini_logs/originals_2026-09-16/`. The reconciled copy with an appended audit (§7) is `archive/mini_logs/PREDICTION_MINI_RUNNING_LOG_P407_P423_FULL_RETROSPECTIVE_RECONCILED_2026-09-16.md`.
- **Issued text:** C′'s 15 settled card tables were compared with the log-C settlement tables above; every rank and probability is identical.

### `P-406` — Settlement (six-over rows, 2026-09-16)

- **Event:** Edinburgh Castle Rockers v Amsterdam Flames, ETPL 2026 Match 24, 13 September 2026.
- **Official final:** Edinburgh 118 all out (18.3 overs); Amsterdam 120/2 (14.5 overs), won by 8 wickets.
- **Field-owning source (opened):** ESPN site API `cricket/1547871/summary?event=1547895` (ESPNcricinfo data), accessed 2026-09-16.
  - Toss note: "Amsterdam Flames, elected to field first". Edinburgh therefore batted first, so the card's condition held.
  - Matchnote 767111, section 1 (Edinburgh innings): **"Powerplay 1: Overs 0.1 - 6.0 (Mandatory - 68 runs, 2 wickets)"**. Section 2 (Amsterdam) shows 45/0.
  - Consistency check: the recovered fall of wickets (37/2 at 3.1, 77/3 at 7.3) and the note "Edinburgh Castle Rockers: 50 runs in 4.1 overs" both agree with 68/2.
- **Settlement time:** 2026-09-16.
- **Method on card:** `MDS-2026.09.06-v4.0`.
- **Population:** EXPLORATORY.

| Rank | Contract | Frozen terms | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier | Boundary / dependence note |
|---:|---|---|---:|---|---:|---|
| 1 | ECR first 6 overs Over 50.5 | Edinburgh batting first; score after 6.0 completed overs | 0.64 | **WIN** (68) | 0.1296 | 17.5 runs clear; exact complement of R4 |
| 2 | ECR 20-over Over 172.5 | innings total | 0.54 | **LOSS** (118) | 0.2916 | settled 2026-09-14/15 |
| 3 | ECR 20-over Under 172.5 | innings total | 0.46 | **WIN** | 0.2916 | settled 2026-09-14/15 |
| 4 | ECR first 6 overs Under 50.5 | as R1 | 0.36 | **LOSS** | 0.1296 | complement of R1 |

- **Potential winner:** Edinburgh 67% — LOSS.
- **Card mean Brier (4 rows):** 0.2106, against 0.25 for the 0.5 baseline.
- **Top two both won?** No (R1 won, R2 lost).
- **Preferred over/under:** R1, the phase Over — **WIN**. Under `G-L15` both targets are forced pairs: the phase preferred side won, the innings preferred side lost.
- Handle `TMP-OPEN-20260914-06` **retired**.

**Three validation questions**
1. **Line-ups, bench and coaches: No.** The card was issued before the toss, using the "last Edinburgh XI" with the toss unresolved. XIs are nominated at the toss (MCC Law 1.2), after this freeze, so this is `NOT_RETRIEVED`, not a `RETRIEVAL_MISS`. Reserves and coaches were not named. The ESPN summary now shows both XIs; that is post-hoc and not backdated.
2. **Sources.** The 2026-09-14/15 settlement sources (Statz scorecard; the stale ETPL official page) were accurate for totals and fall of wickets but did not carry the phase field. The accurate structured record — the ESPN matchnote — was already in `DATA_SOURCE_REGISTER.md`, which has named series `1547871` for ETPL 2026 since 2026-09-06. The 2026-09-15(b) audit line "no ESPN cricket series ID was registered" was wrong.
3. **Blind spots.**
   - *Settlement:* the source register was not consulted → `G-L14`.
   - *Forecast (recorded 2026-09-15):* the innings Over and the winner label carried Edinburgh's current-form branch into the middle overs, where Amsterdam's spin (Bracewell 5/12) decided the innings. Moving from phase to innings needs wickets in hand × the opposition's middle-overs bowling (cricket controls 16/19).

**Three-question retrospective (phase rows)**
1. *What did the result turn on?* Edinburgh's opening tempo: 50 in 4.1 overs, 68/2 at 6.0.
2. *Was it knowable, and on the card?* Yes. The card's recent-phase evidence included Edinburgh 47/2 after six overs on 11 September, and it ranked the powerplay row first on that tempo.
3. *Smallest change:* nothing on the forecast. At settlement, query the registered structured field before calling a phase checkpoint unresolvable (`G-L14`).

**What went right, and why.** The card kept phase and innings as separate targets and ranked the phase row first. The opening burst held even though the innings collapsed. Cricket phase rows in the 2026-09-15(b) import are now **4 of 4** when preferred (P-379, P-395, P-400, P-406; `C-PHASE-VS-FULL-TOTAL`).

### `P-418` — evidence correction (not settled)

- **The misdated report.** The 2026-09-15(b) log-C retrospective above says the Bhutan Broadcasting Service round report "dated 2026-09-15" lists the concluding first-round results and no Drukpa–RTC match. Those results were Paro 5–1 Thimphu, Thimphu City 4–0 Tensung, Transport United 1–0 Ugyen Academy, RTC 3–3 Tsirang and BFF Academy U-20 2–2 Drukpa. **That report is `bbs.bt/244289`, with raw `Published Time` 2026-07-17T09:40:56Z** — the end of the first round. It says nothing about 14 September. The previous round report, `bbs.bt/244138`, was published 2026-07-12.
- **RSSSF** (`rsssf.org/tablesb/bhutan2026.html`, raw HTML, "Last updated: 11 Sep 2026") lists **Round 15: [Sep 14] Drukpa – RTC**, unscored. Its table has both clubs on 14 matches (Drukpa 17 points, RTC 18). External log C′ had reported this correctly.
- **BFF's RTC 1–1 Drukpa report** is the 13 June first-round meeting (RSSSF Round 4: "RTC 1-1 Drukpa").
- **No post-match record** was found on 2026-09-16 (web search; BBS, BFF and RSSSF pages).
- **Disposition:** `IDENTITY_STATE_CONFLICT` → **`RESULT_NOT_RECOVERED`**. No W/L and no Brier. Handle `TMP-OPEN-20260915-04` is kept, with a new retry trigger: an RSSSF update, a BFF match report, or a BBS second-round report dated on or after 14 September.
  - The card's genuine identity defects remain: kickoff 12:00 v 13:00 UTC across aggregators, and a stale club schedule. `RULES_GENERAL.md` §16.10(i) stands on those; its origin sentence is corrected in §16.11(p).
- **What went wrong in the earlier settlement:** evidence was dated from something other than the page's own metadata — the `G-L13` failure class.
- **What went right in C′:** it refused to settle, and cited the fixture list correctly.

### Queue retry — every Part-3 handle (2026-09-16)

| Handle | Row | Probe this pass | Result |
|---|---|---|---|
| `TMP-OPEN-20260914-06` | P-406-C01/C04 | ESPN cricket API matchnote | **Settled — retired** |
| `TMP-OPEN-20260915-04` | P-418 | RSSSF raw HTML, BBS page metadata, web search | Re-classified `RESULT_NOT_RECOVERED` |
| `TMP-OPEN-20260915-03` | P-410-C05 Leipzig team corners O4.5 | bundesliga.com stats: direct HTTP 403; `r.jina.ai` raw text is all-zero placeholders. A WebFetch summary said "7–7", which is not on the page — excluded (`G-L13`) | Open (ESPN 8; C′'s secondary displays 7) |
| `TMP-OPEN-20260915-05` | P-419-C05 | allsvenskan.se match `6529990` — JS / cookie wall | Open (ESPN 2+2) |
| `TMP-OPEN-20260914-02` / `-03` | P-401-C01 / C03 | allsvenskan.se (same lane) | Open |
| `TMP-OPEN-20260915-02` | P-409-C02 | plus.ligue1.com `live/306887` — empty raw text | Open (ESPN 5) |
| `TMP-OPEN-20260915-01` | P-407-C01 | proleague.be 2026-27 match slug → 404 | Open (ESPN 9) |
| `TMP-OPEN-20260914-01` | P-399-C02 | Lega Serie A 2026-27 page not found; Sky Sport Italia tabellino 8–9 (secondary) | Open (ESPN 17) |
| `-20260912-01`, `-20260911-01`/`-02`, `-20260909-01`/`-02` | P-377, P-368, P-369, P-341, P-342 corners | Not re-probed — no route exists (DSR non-coverage list) | Open |

**Part-3 custody is now 13 handles.** The §"2026-09-15(c)" table said "13" but listed 14; this is corrected. Part 2 holds 9, not re-researched this pass.

### External variant C′ — audit of its settlement and retrospective claims

| C′ claim | Verified at (2026-09-16) | Finding | Disposition |
|---|---|---|---|
| Finals and W/L for P-407–P-423 | Canonical tables above | Agree on every final and every booked W/L | No change |
| 60 booked rows, 39 W / 21 L, mean Brier 0.2029 | Recomputation | Reproduces. The canonical 61 rows / 0.2088 is the same set plus P-408-C01 (0.5625) | Canonical stands |
| Potential-winner Brier mean 0.1822 (15 cards) | Recomputation | Reproduces | Recorded |
| P-408-C01 provisional (Brighton 3) | Premier League record (2026-09-15(b)) | Already booked as a LOSS | Canonical stands |
| P-408: Coventry second-half red card; "66 % possession, 21 attempts" | ESPN `eng.1` 401879282 `keyEvents` and box score | Red card **confirmed**: Awoniyi 53', violent conduct, with Brighton already 2–0 up (35', 51'). Possession was **69.4 %** and shots **22** — C′'s figures were slightly wrong | Red card added below; C′ figures corrected |
| P-410: Leipzig 7 corners (Guardian/StatMuse/SoccerNews) v 8 | ESPN `ger.1` 401884798 | ESPN has 8–7 (Leipzig 8, Hamburg 7) | Provider split recorded; row stays open |
| P-412: T.J. Watt's fourth-quarter pick-six decided the cover | ESPN `nfl` 401872658 `scoringPlays` | **Confirmed.** Q4 14:05, "T.J. Watt 35 Yd Interception Return", 13–10 → 20–10. Rush 12/22, 2 INT, 4 sacks | Added below; American football control 20 |
| P-413: 506 yards at 7.9 ypp; Jackson 324; Henry 144 and 3 TD; Flowers 54-yard TD | ESPN 401872659 | **Confirmed** | Added |
| P-414: Buffalo 409 yards on 52 plays, 7.9 ypp | ESPN 401872660 | **Confirmed** (Buffalo 0 turnovers; Houston 2) | Added |
| P-416: both Yankee runs solo home runs; Schlittler allowed one hit | MLB statsapi 823495 | **Confirmed** (Rice in the 1st, Wells in the 3rd; 6.0 IP, 1 H, 8 K) | Added |
| P-417: Muller four RBI, including a two-run homer | NPB box s2026091401939 | **Confirmed** (4 AB, 2 H, 4 RBI; homer in the 5th with one on) | Added; baseball control 31(b) |
| P-419: red-card disruption | ESPN `swe.1` 401873992 | **Confirmed — three red cards:** Ågren (GAIS) 59' at 1–0, Almyras (Djurgården) 86', Sletsjøe (GAIS) 90+10'. Corners 2–2 | Added; soccer control 34 |
| P-420: López 3 IP, 5 R; Smith-Shawver took length; Crow-Armstrong homered off him | MLB statsapi 824629 | **Confirmed.** López 3.0 IP on 62 pitches; Smith-Shawver 5.0 IP, 2 R; Crow-Armstrong's two-run homer in the 6th; Atlanta scored 3 in the 7th off Assad, making the total 10 | Added; baseball control 30 |
| P-421: "trailed 2–1 after six and was tied 2–2 entering the eighth" | MLB statsapi 823656 line score | **Partly wrong.** After six it was NYY 1–2 MIN (correct), and still **1–2 entering the 8th** (no 7th-inning runs), not 2–2. Six-run 8th: Judge three-run homer; Morris 0.1 IP 3 R; Minter 0.0 IP 3 R | Corrected |
| P-423: 6–1 after three innings; 6–5 after six | MLB statsapi 824308 | **Confirmed.** Hart 0.1 IP, 3 R in the 6th, after Mize's 5.0 IP (8 H, 0 K) | Added; baseball control 30 |
| P-418: RSSSF lists the 14 September fixture unscored | RSSSF raw HTML | **Confirmed** — C′ was right and the canonical record was wrong | P-418 re-classified |
| New sources (C′ §4.5) | — | Registered with grades in `SOURCES.md` / `DATA_SOURCE_REGISTER.md` §"2026-09-16" | — |
| Candidates (C′ §4.4) | — | Dispositions in the reconciled archive copy §7.3 and `LEARNING_REGISTER.md` L-20260916-03 and -07 to -10 | — |
| Handles `TMP-OPEN-20260915-02` to `-06` | Canonical queue | Collide with canonical numbering | Recorded as retired aliases in `GAME_LOG_STATUS_CURRENT.md`; canonical numbers unchanged |

### Retrospective addenda from verified facts (issued records unchanged)

| Card | Verified fact added | What it changes in the retrospective | Earlier lesson linked |
|---|---|---|---|
| P-408 (Rank #1 LOSS) | Brighton 2–0 by 51'; Coventry reduced to ten men at 53' | Brighton led early and then played 37-plus minutes against ten men, yet still took only 3 corners. The deep review's mechanism stands: central combination play plus a leading state. The red card came after the second goal and is aleatory. The corner tree had no branch for it, but it is not shown to be the cause of the shortfall | Soccer control 33; §16.11(o) |
| P-412 (Rank #1 LOSS at exactly 7) | The 7-point margin came from a non-offensive TD at Q4 14:05 | The +6.5 was not lost to offensive separation: without the return TD the game was level at 13. The card had no margin table and no non-offensive branch. 2025 reference: 0.217 non-offensive TDs a game, at least one in 18.8 % of games; a margin of exactly 7 in 9.6 % of games | American football controls 18, 20 |
| P-413, P-414 (R1 and R2 LOSS) | Ravens 7.9 ypp; Bills 7.9 ypp with 0 turnovers | Both confirm the explosive-efficiency family carried too little mass | Control 16; `G-L12` |
| P-416 | Both Yankee runs were solo home runs | Favourite −1.5 won through two single-run events: run-line separation can come from home runs without a crooked inning | Baseball control 29(a) |
| P-417 | Muller drove in 4 as the starting pitcher (he batted in this game) | The "one team alone clears the total" branch was partly created by the starting pitcher's bat | Baseball control 31(b) |
| P-419 | Three red cards; corners 2+2 | A disrupted match. The corner alternate missed partly inside a state the card did not model, but the row could not be booked regardless | Soccer controls 23, 34 |
| P-420 (Rank #1 LOSS) | A length reliever took five innings and gave up the two-run homer that made it 7–0 | Separation came from the transition after the starter's exit, not from late leverage relief | Baseball controls 29(c), 30 |
| P-421 | Correction: the Twins led 2–1 into the 8th | "Top two both won" was decided entirely by one relief inning — a transition / late-relief cluster | Baseball controls 19, 30 |
| P-422 (Rank #1 LOSS) | Denver 176 yards (3.7 ypp) and 4 sacks | Favourite separation inside the Under — a branch the card never printed | American football control 21 |
| P-423 (Rank #1 LOSS by one run) | Hart 0.1 IP, 3 R in the 6th | The one-run state was created in the first relief inning after Mize left | Baseball controls 29(b), 30 |

### Over/under — the standing directive (research this pass)

**Question.** How can the analyst make at least one O/U pick win more often?

**Data.**
- **Scope:** every booked O/U row in `P-345`–`P-423` (148 rows on 57 cards), plus P-406's phase pair settled this pass.
- **Method:** rows were parsed from this file's settlement tables and classified by event title (working files are in the session scratchpad only).
- **Excluded:** `P-333`–`P-344`, which use a different table format; see `RULES_GENERAL.md` §"2026-09-09".

| Geometry | Family | Record | Mean stated p |
|---|---|---|---:|
| **Forced pair — preferred side (p > 0.5)** | all | **27 of 45** | — |
| | soccer full-match goals | **1 of 6** | — |
| | MLB full-game runs | 7 of 9 | — |
| | NFL | 2 of 4 | — |
| | basketball | 3 of 6 | — |
| | NPB/KBO/CPBL | 3 of 5 | — |
| | NRL/AFL | 2 of 3 | — |
| | cricket innings/match (incl. Test first innings 0 of 1) | 2 of 4 | — |
| | cricket phase | 4 of 4 | — |
| | soccer first half | 3 of 4 | — |
| **Free (complement not ranked)** | all | **45 of 60** | 0.68 |
| | team totals, all | 18 of 24 | 0.73 |
| | — soccer team goals | **10 of 10** | 0.78 |
| | — MLB team runs | 5 of 8 | 0.69 |
| | — NPB/KBO/CPBL team runs | **3 of 6** | 0.72 |
| | phase (soccer 7 of 9, cricket 2 of 2) | 9 of 11 | 0.67 |
| | full game (soccer 8 of 11, NPB 2 of 2, MLB 1 of 3) | 11 of 16 | 0.61 |
| | corners | 4 of 5 | 0.67 |

**Reading (honest).**
1. **Forced pairs carry no information about "at least one wins".** A supplied Over/Under pair on one target guarantees one winner, so that goal is met automatically. The informative number is the preferred side: 27 of 45 (60 %). That is above a coin flip overall, but soccer main-line goals went 1 of 6, and basketball and the NFL were 50 %.
2. **What has actually delivered:** free rows on low-count thresholds backed by a named mechanism — soccer team goals 10 of 10, phase rows 9 of 11.
3. **Overconfidence pocket:** NPB/KBO team-run totals, 3 of 6 at a mean stated 0.72.
4. **Caveats:** free rows are chosen by the analyst, often at easier thresholds with higher stated p; rows within an event are dependent; n is small. This is not a directional edge, and no ordinal bar follows (`RULES_GENERAL.md` §16.9).

**Changes adopted (disclosure only):**
- **`G-L15`:** label and report O/U geometry. Analyst-chosen O/U rows include one free low-count-tail row with a verified settlement route. Print P(at least one wins) with the joint term.
- **Soccer control 35:** a settlement-route table, so those rows can actually be settled.
- **Baseball control 31:** NPB/KBO team totals need the opposing starter's game log and the posted order before p ≥ 0.65.
- **American football reference base rates:** margin key numbers; total points SD 13.8 (unconditional).
- **`C-OU-GEOMETRY`:** a prospective test.

### Updated roll-ups (descriptive)

| Measure | Before | After this pass |
|---|---|---|
| Log B graded rows / W–L / mean Brier | 67 / 35–32 / 0.2278 | **69 / 36–33 / 0.2250** |
| Log B Rank #1 | 9 W / 6 L (+1 provisional, +1 unresolved) | **10 W / 6 L (+1 provisional: P-401)** |
| Log B top two both won (both rows graded) | 7 / 14 | **7 / 15** |
| Log B preferred scoring O/U | 11 / 17 | **12 / 17**, if the earlier count used P-406's losing Rank-#2 innings Over (the only graded total on the card then). P-406's highest-ranked total is now its Rank #1, a WIN |
| Import `P-373`–`P-423` graded rows / W–L / mean Brier | 194 / 107–87 / 0.2276 | **196 / 108–88 / 0.2266** |
| Import Rank #1 | 25 W / 20 L | **26 W / 20 L** |
| Running mixed scorecard | 371 rows, 205 W / 166 L, 0.2352 | **373 rows, 206 W / 167 L, ≈ 0.2346** — recomputed from the rounded carried mean, so ±0.0001 |
| `PRIMARY_SCORED` | 104 rows, 0.2522, 25 cards | Unchanged (P-406 is EXPLORATORY) |

### Validation questions for this pass

1. **Confirmed line-ups, bench and coaches?**
   - No new card this pass.
   - P-406 (settled this pass): **No.** It was issued before the toss, so the XIs are `NOT_RETRIEVED` (published at the toss, after the freeze), and reserves and coaches were not named.
   - Log C: the 2026-09-15(b) matrix stands (0 of 16 complete).
2. **Were the sources accurate?**
   - **Accurate:** the structured field owners, on every fact checked (ESPN, MLB statsapi, the NPB box score, RSSSF raw HTML).
   - **Inaccurate:**
     - a WebFetch model summary: Bundesliga corners "7–7" not on the page, and a misdated BBS article;
     - the prior pass's "2026-09-15" date on a July BBS report;
     - the 2026-09-15(b) audit line saying no ESPN series ID was registered for ETPL;
     - C′'s P-421 inning narrative and its P-408 possession and shot figures.
   - **Newer or better sources, now used:**
     - ESPN cricket matchnotes for phase settlement (existing, previously unused);
     - ESPN soccer `keyEvents` for disruption facts;
     - MLB statsapi `feed/live` for inning-level narrative;
     - RSSSF raw HTML for sparse leagues;
     - ESPN NFL season data for reference base rates.
   - **Confirmed not usable keylessly:**
     - Bundesliga, Allsvenskan and Ligue 1 official stats pages (JS-only);
     - Pro League and Serie A 2026-27 match pages (not found);
     - Pro-Football-Reference (security verification page).
3. **Blind spots, and the fix for each:**
   - (a) Model summaries treated as records → `G-L13`.
   - (b) Settlement routes neither pre-registered at issue nor consulted at settlement → `G-L14`, soccer control 35, cricket control 29.
   - (c) O/U success reported without its geometry → `G-L15`.
   - (d) Disruption events omitted from settlement → §16.11(o), soccer control 34.
   - (e) No NFL non-offensive-score branch and no favourite-inside-the-Under branch → American football controls 20–21.
   - (f) Starter-exit transition inning not modelled → baseball control 30.
   - (g) NPB/KBO team-total overconfidence → baseball control 31.

### Rule, register and source changes made in this pass

- `RULES_GENERAL.md` §16.11 (l)–(p), and an inline correction pointer in §16.10(i).
- Sport files §"2026-09-16":
  - soccer controls 34–35;
  - American football controls 20–21, with 2025 reference base rates;
  - baseball controls 30–31;
  - cricket control 29;
  - basketball control 25 worked example;
  - AFL, NRL, ice hockey, rugby union and tennis instantiations.
- `LEARNING_REGISTER.md` L-20260916-01 to -12, and the `C-OU-GEOMETRY` manifest.
- `SOURCES.md` and `DATA_SOURCE_REGISTER.md` §"2026-09-16", including the unresolved-rate update.
- `CONTROLS.md`, `METHOD.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `README.md`, `GAME_LOG_STATUS_CURRENT.md`, `GAME_LOG_STATUS_INDEX_2026-09-05.md` and `PREDICTION_LOG_COMBINED_4.md`.

### 2026-09-16(b) — documentary-audit rows recovered (records in Part 4 Appendix A)

Per the user direction of 2026-09-16, settlement records for rows whose parent card sits in a **closed part** are written into [`PREDICTION_LOG_COMBINED_4.md` Appendix A](PREDICTION_LOG_COMBINED_4.md), with custody of the cards unchanged. In the same pass:

- `P-251-C05` (Coppa Italia) — ESPN 6 + 5 = 11: research WIN, threshold-invariant.
- `P-255-C05` and `P-256-C05` (UEFA Women's Champions League) — settled at the UEFA field owner with a period-scope bound (24 corners / 137 played minutes and 15 / 115); handles `TMP-AUDIT-20260912-03` and `-04` retired.
- `P-265-C05` (Leagues Cup) — ESPN 4 + 5 = 9: research WIN at exactly the threshold, provider-sensitive.
- `P-250-C05` and the nine Part-2 corner rows — re-probed, no keyless route (all HTTP 400).

New cross-sport rule from this work: **`G-L16` period scope** (`RULES_GENERAL.md` §16.11(q)); new lane `SRC-UEFA-MATCH-FINDER`.
