# Combined prediction log 4

> **Controlling status (carried from Part 3):** all combined-log material is **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** under the current user direction. Settlement preserves outcome evidence; it does not authorise a performance claim. Issued records are never rewritten.

Status: **CLOSED 2026-09-21 — P-424 THROUGH P-481; READ/SETTLE ONLY**
Opened: **2026-09-15**, as the fourth combined log per user directive.
Component order: opened empty at **`P-424`** and closed after contiguous import through **`P-481`**. New forecasts begin in `PREDICTION_LOG_COMBINED_5.md` at **`P-482`**.
Current method: **MDS-2026.09.17-v4.1 — SPORTS_ONLY / MARKET_BLIND; `UNVALIDATED_SUBJECTIVE` probability + Brier scoring mandatory on every ranked row (`METHOD.md` §5).** Read the version from `METHOD.md`'s own header each session — never from this line.

| Part | File | ID range | Status |
|---|---|---|---|
| 1 | `PREDICTION_LOG_COMBINED.md` | `P-001`–`P-271` | CLOSED 2026-09-04 — read/settle only |
| 2 | `PREDICTION_LOG_COMBINED_2.md` | `P-272`–`P-332` | CLOSED 2026-09-07 — read/settle only; holds the lettered "Appendix — unsettled and incomplete logs" |
| 3 | `PREDICTION_LOG_COMBINED_3.md` | `P-333`–`P-423` (`P-372` reserved/unused) | CLOSED 2026-09-15 — read/settle only |
| **4** | **`PREDICTION_LOG_COMBINED_4.md` (this file)** | **`P-424`–`P-481`** | **CLOSED 2026-09-21 — read/settle only** |
| **5** | **`PREDICTION_LOG_COMBINED_5.md`** | **`P-482` onward** | **ACTIVE** |

## Current controlling snapshot

This is the only queue and next-ID authority for new forecasts. The snapshots in Parts 1–3 are frozen at their closures.

| Field | Current value |
|---|---|
| As of | **2026-09-21, Australia/Melbourne — Part 4 rollover complete. P-452–P-473 and P-474–P-481 imported from settled mini logs; Part 4 closed at P-481.** |
| Next canonical ID | **`P-482` — issue only in `PREDICTION_LOG_COMBINED_5.md` after normal fresh reconciliation.** |
| Live events | **None in the P-452–P-481 rollover batch.** Historical open derivative/result handles remain governed by `GAME_LOG_STATUS_CURRENT.md`. |
| Open / pending settlement queue (checked first, every session) | **23 handles** (2026-09-17), full table in `GAME_LOG_STATUS_CURRENT.md` §"Primary result/derivative follow-up queue". **Part-3 custody (13):**<ul><li>`TMP-OPEN-20260915-04` — **P-418 whole card, `RESULT_NOT_RECOVERED`** (re-classified 2026-09-16; fixture listed by RSSSF)</li><li>`-20260915-01` P-407-C01, `-02` P-409-C02, `-03` P-410-C05, `-05` P-419-C05</li><li>`-20260914-01` P-399-C02, `-02` P-401-C01, `-03` P-401-C03</li><li>`-20260912-01` P-377-C02</li><li>`-20260911-01` P-368-C02, `-02` P-369-C01</li><li>`-20260909-01` P-341-C03, `-02` P-342-C03</li></ul>**Retired 2026-09-16:** `-20260914-06` (P-406 six-over rows — settled in Part 3 §"2026-09-16"). *Count correction: the 2026-09-15 version of this row said "Part-3 custody (13)" while listing 14 handles; 14 − 1 = 13 now.* **Part-4 custody (1):** `TMP-OPEN-20260917-01` — `P-430-C05` Al Ain team corners Over 3.5; the card pre-registered the AFC official match-stat record, which publishes no corner field. ESPN and two secondary displays agree on Al Ain 2 (a research LOSS) but were not pre-registered, so the row is **not booked** (§16.10(j)). Retry: an AFC field-owning statistics record, or an explicitly reconciled approved provider. **Part-2 custody (9):** `TMP-OPEN-20260909-03`…`-11` (P-126, P-148-C02, P-149-C02, P-176-C05, P-178-C05, P-179-C05, P-233, P-234-C03, P-235). **Documentary/period audits (separate, 5 after 2026-09-17(c)):** `TMP-AUDIT-20260912-01` (P-250 — no route), `-02` (P-251 — reproducible, provider still unreached), `-05` (P-265 — reproducible, knife-edge). `-03` and `-04` (P-255-C05, P-256-C05) **REOPENED — UNRESOLVED_PERIOD**: whole-match counts do not prove regulation Overs. See the correction and Appendix A. None blocks a new forecast. |
| Custody rule for open rows | An open row is settled **in the part that issued it** (closed parts accept settlement updates only), and its handle is retired in `GAME_LOG_STATUS_CURRENT.md` in the same edit. This file records a one-line pointer in its dated section whenever it retires one. Nothing is copied or re-opened here. |
| Probability state | Every ranked row carries an `UNVALIDATED_SUBJECTIVE` probability for the exact contract (`METHOD.md` §5; `RULES_GENERAL.md` §16.9), scored under SCORING_AND_VALIDATION: complete W/P/L plus a separately labelled decisive diagnostic and same-event baseline. Never described as calibrated or validated. |
| Value state | `NO VALUE DETERMINABLE` unless a validated model and a complete same-time price snapshot pass the value gate. |
| Performance eligibility | **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** (current user direction). Settled rows enter the descriptive scorecard for continuity only. |
| Historical scorecard — LEGACY_MIXED_DIAGNOSTIC | **477 rows, 114 cards, 273 W / 204 L, mean 0.2265475891**; **PRIMARY_SCORED 136 rows, 33 cards, 71 W / 65 L, mean 0.246825**. Recomputed from row sums. No model-skill or calibration claim; current log remains learning-only. Latest MLB forced pairs: 32 rows / 16 decisions, 10 correct (run lines 6/8, totals 4/8). Preferred eight MLB totals: legacy 0.2591; decisive q-Brier 0.245720512; W/P/L Brier/2 0.259225. Different conditioning, not improvement. Next pattern review at 50 primary cards; no automatic promotion. |

## 2026-09-17(c) — current audit corrections

This correction supersedes earlier aggregate and period-bound claims without changing issued probabilities, ranks or contracts. All existing records remain LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. See [the implementation ledger](AUDIT_IMPLEMENTATION_2026-09-17.md) and [scoring specification](SCORING_AND_VALIDATION.md).

**Score arithmetic:** P-344's four Brier cells sum to 1.1337, mean **0.283425**, not 0.3334. Recomputed from canonical rows and latest documented settlements: P-333–P-344 **39 rows, 0.2601307692**; through P-344 **72 rows, 0.2408763889**; through P-371 **177 rows, 0.2423966102**; through P-423 **373 rows, 0.2341018767**; through P-437 **425 rows, 0.2286134118**; through P-451 **477 rows, 273 W/204 L, 0.2265475891**. These are current cumulative-by-ID reconstructions, not claims about what was settled at each historical snapshot date. PRIMARY_SCORED remains **136 rows/33 cards, 71 W/65 L, 0.246825**. Older approximate aggregates are superseded by this row-derived correction. Legacy binary scores retain their original conditioning defect and are labelled LEGACY_MIXED_DIAGNOSTIC; corrected W/P/L and non-push measures are separate.

**Period correction:** P-255-C05 and P-256-C05 are **UNRESOLVED_PERIOD**, not demonstrated research wins. Whole-match corners of 24 and 15 do not establish regulation Over 8.5: losing splits require 16+ and 7+ extra-period corners respectively, and no recovered evidence excludes them. Reopen the existing TMP-AUDIT-20260912-03 and -04 handles. They remain separate documentary/period follow-ups, bringing that queue back to **5**; the primary queue stays **23**. Final scores and other rows remain as recorded. Original Part-1 custody is preserved; Appendix A in Part 4 carries the evidence receipt and correction pointer. No new ID or probability is created.

**Validation correction:** C-OU-GEOMETRY's P-424–P-437 and P-438–P-451 cohorts are historical development observations, with **zero verified prospective cards** until manifest/issue/outcome-time/control-version joins are established. In particular P-425/P-426/P-427/P-429 predate the 16 September manifest. Import time is not issue time. No universal MLB run-line/push ceiling, NFL variance floor, automatic phase preference or Over/Under bias is promoted. Current METHOD v4.1 governs new forecasts only.

## How this file is used — read before appending anything

1. **Fresh-read each session:** `METHOD.md`, `RULES_GENERAL.md` §16 (including §16.5(a)–(g), §16.8, §16.9 and §16.10), `CONTROLS.md`, `SOURCES.md`, the relevant `RULES_<SPORT>.md` and, for soccer or cricket competition rules, `LEAGUE_RULES_SOCCER.md` / `LEAGUE_RULES_CRICKET.md`. Never rely on a remembered version.
2. **Queue first.** Check every handle in the snapshot. Settle any row whose retry trigger is met (in its issuing part), leave the rest, and record live events as live — then research the new event.
3. **Append in strict ascending canonical-ID order from `P-424`.** Never renumber or reuse an ID. Declare any skipped ID as RESERVED / UNUSED.
4. **Update the snapshot in the same edit** as any new card or settlement, including the running scorecard.
5. **External mini logs** follow `EXTERNAL_LOGGING_WORKFLOW.md` §"2026-09-15". First fingerprint the file and drop byte-identical duplicates. Then run a live check, and settle each finished game **inside the mini log itself** (under that game's section), with temp IDs and general learnings/rule changes/sources at the bottom. Then append the relevant sections here. Only after that, archive the updated mini log in `archive/mini_logs/` beside the byte-exact raw upload. **No separate settlement documents and no working files outside the MD documents.** Reconcile within 24 hours of availability (`METHOD.md` §10).
6. **Record learnings where they belong:** per-game learnings under that game's block; general learnings at the top of the relevant dated section; rule changes in `RULES_GENERAL.md` or the sport file; dispositions in `LEARNING_REGISTER.md`; sources in `SOURCES.md` and `DATA_SOURCE_REGISTER.md`; workflow in `EXTERNAL_LOGGING_WORKFLOW.md`.
7. This log is **SPORTS_ONLY / MARKET_BLIND**. Odds, prices, tipster or betting-preview prose are never evidence (`L-20260912-08`). No entry may claim calibration, ROI, edge or model validation.

## Controls carried forward — load-bearing for every `P-424`+ card

The full history is in `LEARNING_REGISTER.md` and `CONTROLS.md`. The controls that govern new cards:

| Control | Requirement | Home |
|---|---|---|
| Probability mandate | Exact-contract `UNVALIDATED_SUBJECTIVE` probability on every ranked row; the rank is derived from the probabilities; push/void/censoring stated separately | `METHOD.md` §5; `RULES_GENERAL.md` §16.9 |
| `G-L1` | Outcome-state families with explicit mass; every kill path a weighted branch; representative Rank-#1 outcome | §16.5(a) |
| `G-L2` | Declared priors/scenarios may change mean and variance; no unsupported directional adjustment | §16.5(b) |
| `G-L7` | Open the disaggregated record (game log, current-series table, rehab ladder) before an aggregate carries direction | §16.5(c) |
| `G-L8` | Total probability from the card's own centre and width, with exact `P(X<L)`, `P(X>L)` and push mass | §16.5(d); §16.9 |
| `G-L9` | Complement partitioned into disjoint losing states, each with mass | §16.5(e); §16.9 |
| `G-L10` | `P(R1 ∧ R2)` from the joint table, or `JOINT_UNQUANTIFIED` with bounds; print P(at least one preferred over/under wins) when two top rows share a driver | §16.5(f); §16.9 |
| `G-L11` | Real numerators/denominators and an appropriate uncertainty model before a small-sample rate takes a signed adjustment | §16.5(g); §16.9 |
| **`G-L12`** | State margin prior and shrinkage target/strength; derive conditional width and key-value masses. Historical NFL 13.9 is a benchmark, not a floor. | RULES_GENERAL section 16.10(h); SCORING_AND_VALIDATION |
| **`G-L13`** | A model-summarised retrieval (search answer, WebFetch summary) is never a record — confirm every number, date and name in raw text or JSON, or mark `SUMMARY_ONLY` | §16.11(l) |
| **`G-L14`** | Print each derivative/phase row's settlement route and its verified status at issue; consult `DATA_SOURCE_REGISTER.md` before calling a row unresolvable; no self-generated alternate without a verified route | §16.11(m) |
| **`G-L15`** | Label every O/U row `FORCED_PAIR` or `FREE`; report the preferred side for forced pairs and "at least one wins" only across free rows or distinct targets | §16.11(n) |
| **`G-L16`** | The settling record's period scope must match the contract's: check `played_time`/period fields before settling a 90-minute, regulation or phase row from a whole-match feed | §16.11(q) |
| **`G-L17`** | For two ranked rows sharing a driver, print `P(¬R1 ∧ ¬R2)` — the mass in which both fail — and name the single state that produces it | §16.12(a) |
| **`G-L18`** | Allocation marginals: for any multi-participant total, print each side's own score marginal and the opponent-contribution branch | §16.12(b) |
| **`G-L19`** | Build the competition's complete terminal end-state family (including ties/draws/shoot-outs) before issuing any winner label | §16.12(c) |
| **`G-L20`** | A direct current-regime comparable that already cleared the line gets explicit mass; contradicting it above 0.50 needs a named mechanism | §16.12(d) |
| **`G-L21`** | Card-level shared-driver failure mass: when 3+ ranked rows share one driver, print `P(all of them fail)` with Fréchet bounds and name the single state; the winner label must inherit the same evidence as the ranked rows | §16.13(a) |
| **`G-L22`** | A `FORCED_PAIR` is **one** decision, not two rows. Report the preferred side as the trial and keep free-row and forced-pair Brier in separate lines of the scorecard | §16.13(b) |
| **`G-L23`** | Before amending any control from a result, open the structured process record (shots, xG, disruption events, inning splits) and separate a process failure from a conversion/endpoint outlier | §16.13(c) |
| **`G-L24`** | Exact signed-margin queries including draw/push; pooled league bands are contextual priors, not universal matchup bounds. | RULES_GENERAL section 16.13(e) |
| Disruption facts | At settlement, copy red cards, sin bins, injury exits and weather stoppages with minute and score from the structured feed | §16.11(o) |
| Fixture identity | Sparse competitions: confirm the exact fixture with the federation or national broadcaster, or `G0` fails closed | §16.10(i) |
| Derivative settlement | Pre-register the settling provider (`G10.2`); settle at the competition's official data record; data-partner displays stay provisional unless pre-registered | §16.10(j); soccer control 32 |
| Participants | Both starters, full bench/reserves and both coaches as separate fields, with publication versus retrieval time; `BENCH_NOT_RETRIEVED` blocks a margin or full-game total from Rank #1 | `G14.2`; §16.9 |
| Completeness block | The six-field METHOD section 4 object, preserving detailed gate checks | `RULES_GENERAL.md` §16.8 |
| Environment | Venue-coordinate hourly forecast for outdoor events (`G15.1`) | `CONTROLS.md` |
| Firewall | One cohort motivates a disclosure, never a fitted weight or ordinal bar (`L-087`) | `CONTROLS.md` |
| Latest sport controls | Baseball 24–37; basketball 20–26; soccer 20–41; cricket 25–32; tennis 13–14; American football 16–21 (with 2025 reference base rates); AFL, NRL, ice hockey and rugby union instantiations | sport files §"2026-09-11" to §"2026-09-17(b)" |
| Open prospective tests | `C-MARGIN-TAIL-MASS`, `C-PHASE-VS-FULL-TOTAL`, `C-PROB-EXTREMITY`, `C-RUN-CENTRE-BIAS`, `C-OU-GEOMETRY` — record their fields; none changes a rank | `LEARNING_REGISTER.md` |

## Mandatory pre-query cycle

1. Fresh-read the documents in item 1 above and record the method version from `METHOD.md`.
2. Check this snapshot's queue; settle any retry-ready row in its issuing part; record live events.
3. Freeze identity, contract, target, time and participants (`G0`–`G6`), including §16.10(i) fixture confirmation in sparse competitions.
4. Retrieve volatile facts first — line-ups, bench, coaches, availability, weather, strip/surface — from field owners and structured keyless endpoints (`SOURCES.md`), opening each record **in raw text or JSON** (`G-L13`: a search summary and a model-summarised fetch are never a source). Print each derivative or phase row's settlement route and verified status (`G-L14`), and check the route's period scope against the contract (`G-L16`).
5. Build the joint event object with every control in the table above, including the §16.8 completeness block.
6. Refresh immediately before issue, append the card here, update the snapshot, then deliver.
7. At settlement, use the schema below. Run a deep Rank-#1 review whenever Rank #1 loses. Run the `PRIMARY_SCORED` pattern review at 50 cards.
8. **Run the mechanical completeness audit** — `python audit_card_controls.py <log.md> --settlement` — and record the per-card result (§16.8, settlement-protocol Step 6a). It detects printed fields, not analysis quality: a PASS is weak evidence, a FAIL is strong evidence.

## Settlement / retrospective schema

### P-XXX — Settlement

**Event:** · **Official final:** · **Field-owning source (opened, with access time):** · **Settlement time:** · **Method on card:** · **Population:**

| Rank | Contract | Frozen terms | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier | Boundary / dependence note |
|---:|---|---|---:|---|---:|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |

**Potential winner:** · **Result:** · **Card mean Brier vs 0.5 baseline:** · **Top two both won?** · **Preferred over/under result:**

**Three validation questions**
1. Were confirmed starting line-ups **and** bench/reserves obtained for both teams, including coaching information? *(Record each field separately: yes / no / `PUBLICATION_TIME_UNVERIFIED` / `RETRIEVAL_MISS`.)*
2. Were the sources accurate, or are newer/more accurate sources needed? *(Name each source, its field and any error found.)*
3. Were there blind spots in the pre-game analysis, and how will the next game account for them?

**Three-question retrospective (`METHOD.md` §7.2)**
1. What did the result actually turn on?
2. Was that driver knowable before issue, and was it on the card?
3. What is the smallest research-routine change that would have surfaced it? *(Link the earlier lesson it confirms or breaks.)*

**What went right, and why** — one line even when the card lost.

**Deep Rank-#1 review — required whenever Rank #1 loses**

| Question | Finding |
|---|---|
| First decisive checkpoint | |
| What went right | |
| What went wrong | |
| Actual mechanism | |
| Knowable, and on the card? | |
| Improvement (and earlier lesson) | |
| Grade (background) | |

---

# Chronological issued / settled events

## 2026-09-17(b) — `P-438`–`P-451` imported, settled, retrospected and audited (external mini log)

**LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** Method on every card: `MDS-2026.09.06-v4.0`. Issued text, ranks and probabilities are preserved exactly as issued; settlement and retrospective material is appended. Source file: `PREDICTION_MINI_RUNNING_LOG_P438_P451_FULL_SETTLEMENT_RETROSPECTIVE_2026-09-17.md` (171,419 bytes, SHA-256 `24e60bb35a068ea715b58fe5985239a7939334d80f6889fda16f23086bd14702`), archived under `archive/mini_logs/` beside its pre-settlement raw upload `PREDICTION_MINI_RUNNING_LOG_FROM_P438_UPDATED_P451.md` (116,470 bytes, SHA-256 `a1d98a39e2089bf68c10b00b0f4b5ec6fb82b3acc25bf80b9ee4336b213729bb`).

**This is the first cohort since Part 4 opened that contains `PRIMARY_SCORED` cards.** Eight of the fourteen records are MLB. The `PRIMARY_SCORED` card count moves 25 → **33**; the 50-card pattern review is still pending.

### Pre-update integrity check

| Check | Finding |
|---|---|
| Predictions in the mini log | 14 IDs, `P-438`–`P-451`, each used exactly once |
| Canonical position | Part 4's snapshot named `P-438` as the next canonical ID; the log begins exactly there |
| Duplicate IDs | **None.** `P-438`–`P-451` appear nowhere in Parts 1–3; the only prior occurrences of the string `P-438` in this repository are the four "next canonical ID" pointers in this file, which this edit updates |
| Duplicate events | **None.** The two ACL2 Group A fixtures, the two UEL MD1 fixtures, the eight MLB games of 16 Sep 2026, the CPL Eliminator and the LNBP Jornada 20 game are all distinct from every earlier record. `P-451` is explicitly **not** the Jornada 19 game (Dorados 91–89, 15 Sep), which no earlier card covered either |
| Already in the combined log? | No |
| Temporary IDs | **None required.** The mini log declares no temp prediction IDs and no canonical conflict. One *derivative/result-recovery* handle was opened and closed inside this pass — `TMP-OPEN-20260917-02` (`P-451` Jornada 20 final) — which is not a prediction ID |
| Event states | 13 complete; 1 blocked-at-issue with no forecast (`P-451`). None live, delayed, suspended, postponed, abandoned or cancelled. One completed event produced **no active ranked contract** (`P-445` — conditional activation not met) |
| Next canonical ID | **`P-452`** |

### Independent verification of the finals (`G-L13` — raw records, not the log's own narrative)

Every final below was reproduced from raw JSON in this pass. Nothing is carried on the mini log's own narrative.

| Card(s) | Verified at | Result |
|---|---|---|
| `P-442`–`P-444`, `P-446`–`P-450` (8 MLB) | `statsapi.mlb.com/api/v1/schedule?sportId=1&date=2026-09-16&hydrate=linescore` | **All eight finals confirmed exactly.** Inning-by-inning linescores also pulled: `P-443` **regulation 4–4** (10 innings, final 6–5 = 11 runs); `P-444` **regulation 2–2** (13 innings, final 5–4 = 9 runs). Both extras claims in the mini log are independently correct |
| `P-438`, `P-439` | ESPN site API `soccer/**afc.cup**` (= AFC Champions League Two), events 401912815 / 401912814 | **Confirmed.** Al-Wahda 3–2 Kuwait SC; Khaldiya 0–0 Nasaf Qarshi. **New lane — see `SOURCES.md` §"2026-09-17(b)"** |
| `P-440`, `P-441` | ESPN site API `soccer/uefa.europa`, events 401915594 / 401915611 | **Confirmed**, with timelines: Ararat-Armenia 1–4 Sparta (goals 20', 22', 53', 55', 71'; **HT 0–2**); Omonia 1–0 Celta (Balkovec **88'**; **HT 0–0**) |
| `P-445` | ESPN site API `cricket/**1534175**/summary?event=1534214` (CPL 2026 series ID, already in `DATA_SOURCE_REGISTER.md` from `P-217`) | **Confirmed**, including the decisive field: **`section 1` is Barbados**, so Barbados batted first and the frozen Jamaica-batting-first rows never activated. Matchnotes give Barbados powerplay **24/4**, Barbados 144/6 (20), Jamaica chase powerplay **79/0**, Sadaqat **100 off 44** |
| `P-451` | **`lnbp.mx/Dorados/team_results.html`, rendered** (the page is JS-only; `curl` returns a 16 KB shell with no scores) | **RECOVERED THIS PASS: Jornada 20 — Dorados de Chihuahua 97, El Calor de Cancún 86.** Distinct from the Jornada 19 91–89 the mini log warned about. No forecast was issued, so nothing is graded |

**Two material facts the mini log's settlement did not carry** (both required by §16.11(o) and both found in the structured feed on the first call):

1. **`P-438`: Kuwait SC's Mohamed Marhoon was sent off in the 60th minute**, at 1–2. Al-Wahda's equaliser (87') and winner (90+7') both came after it. No red card appears anywhere in the mini log's P-438 block.
2. **`P-438` shot process: Al-Wahda 41 shots / 16 on target / 64.5% possession / 11 corners; Kuwait SC 2 shots / 2 on target / 1 corner.** Kuwait scored **two goals from two shots, all match**. This inverts the mini log's own diagnosis and is dealt with in the deep Rank-#1 review below.

No red card, penalty or abandonment appears in `P-439`, `P-440` or `P-441` (checked in the same feed).

---
### `P-438` — Al-Wahda Abu Dhabi 3–2 Kuwait SC (AFC Champions League Two, Group A) — **Rank #1 LOSS; worst card of the batch**

**Settled from:** AFC official match report; **verified this pass** at ESPN `soccer/afc.cup` event 401912815. **HT 1–2** (Khenissi 5', Gonzalez 8', Diarra 23'); Rivas 87'; Benteke 90+7'. **Marhoon (Kuwait) red card 60'.**

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | First Half Under 1.5 | 0.84 | **LOSS** | 0.7056 |
| 2 | Full Match Under 3.5 | 0.83 | **LOSS** | 0.6889 |
| 3 | Al Wahda team total Under 2.5 | 0.82 | **LOSS** | 0.6724 |
| 4 | Kuwait SC +1.5 | 0.75 | **WIN** | 0.0625 |
| 5 | Full Match Under 2.5 | 0.63 | **LOSS** | 0.3969 |

**Winner:** Al Wahda — WIN. **Card Brier 0.5053** (worst in Part 4 to date). Rank #1 LOSS · **Hit@2 NO** · Wins@2 0/2. Supplied 1H Over 0.5 and FT Over 2.5 both WIN.

**Deep Rank-#1 review** *(this review departs from the mini log's own diagnosis; the departure is the point)*

| Question | Finding |
|---|---|
| Why it was ranked first | The first-half phase was judged lower-variance than the 90-minute distribution and insulated from late substitution and game-state effects — the same structure that carried `P-439`, `P-440` and `P-441` |
| Was 0.84 justified? | **No, and for a reason the mini log missed.** The card put 0.84 on a **U1.5** while its three sibling cards that round put 0.87–0.92 on a **U2.5**. One goal of line is worth far more than 3–8 points when the modal first-half count is 0–1. `P-441` printed its first-half distribution (0g 46%, 1g 36%, 2g 10%, 3+ 8%), which yields U1.5 = 82% and U2.5 = 92% — a **10-point gap**. `P-438` printed **no first-half distribution at all**, so its 0.84 was never derived. That is a `G-L8` (§16.5(d)) requirement listed and not executed — an `M15` instance |
| Round base rate | Across all **17** ACL2 + UEL matchday-1 fixtures of 16 Sep 2026 (reconstructed this pass from ESPN goal minutes): first-half goals 0/1/2/3/4 = 8/3/4/1/1. **P(1H ≥ 2) = 35.3%** → a 1H U1.5 wins **64.7%** of that round; **P(1H ≥ 3) = 11.8%** → a 1H U2.5 wins **88.2%**. The three U2.5 cards at 87–92% sat on the round's own number. `P-438`'s U1.5 at 84% was **~19 points above it**. (n = 17; SE ≈ 12 points — suggestive, not conclusive, and recorded as evidence only) |
| Should another row have ranked higher? | Yes, and not on hindsight: Kuwait +1.5 (the only winner) had the widest survival set on the card, and three of the five rows were near-duplicates of one thesis. The defect was **slate construction**, not the choice between R1 and R2 |
| Actual mechanism | **Not "an open, high-tempo game."** Kuwait took **2 shots in 90 minutes and scored 2 goals** — 100% conversion on a two-shot sample. Al-Wahda took **41 shots (16 on target, 64.5% possession, 11 corners)**. The card's low-scoring *process* read was vindicated; the loss came from (a) extreme finishing variance on a tiny shot base and (b) a **60' red card** that turned the last half-hour into a one-sided siege and produced the 4th and 5th goals |
| Failure class | **Correlated-slate construction plus probability extremity**, with the goal count driven by finishing variance and a disruption event. It is **not** an early-goal-mass modelling failure. Treating it as one — as the mini log proposed — would push the model to raise early-goal mass in low-process matches, which is the wrong correction |
| Card-level arithmetic | Four rows (0.84, 0.83, 0.82, 0.63) all needed "few goals". Under independence P(all four lose) = 0.16 × 0.17 × 0.18 × 0.37 ≈ **0.0018**. Under the card's own marginals with perfect positive dependence the bound is **min(0.16, 0.17, 0.18, 0.37) = 0.16**. The realised state lay somewhere in `[0.0018, 0.16]` and **the card never printed which**. `G-L17` covers only the top two → new **`G-L21`** |
| Rule gap | `G-L17` stops at two rows; `G-L8` was not executed; §16.11(o) disruption facts were not copied at settlement. → `G-L21`, `G-L23`, soccer controls 40–41 |

**Why each row:** three goals by the 23rd minute killed R1; the red card and the 41-shot siege produced goals four and five, killing R2, R3 and R5; Kuwait's one-goal defeat saved R4. **What went right:** the outright Al-Wahda label survived a 0–2 deficit, and the card's process judgment — that Kuwait would not create — was correct to an extreme degree.

---

### `P-439` — Al Khaldiya 0–0 Nasaf Qarshi (ACL2 Group A) — all five rows won

**Verified this pass** at ESPN `afc.cup` event 401912814: 0–0, HT 0–0, Khaldiya 16 shots / 4 on target, Nasaf 11 / 3. No red card.

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | First Half Under 2.5 | 0.87 | **WIN** | 0.0169 |
| 2 | Nasaf team total Under 2.5 | 0.85 | **WIN** | 0.0225 |
| 3 | Full Match Under 4.5 | 0.82 | **WIN** | 0.0324 |
| 4 | Al Khaldiya +1.5 | 0.79 | **WIN** | 0.0441 |
| 5 | First Half Under 1.5 | 0.73 | **WIN** | 0.0729 |

**Winner:** Al Khaldiya — **LOSS** (drawn). **Card Brier 0.0378.** Rank #1 WIN · Hit@2 YES · Wins@2 2/2. Supplied FT Under 2.5 WIN.

**Why:** 27 shots produced 7 on target and no goal. Every ranked row was structurally wide — even a two-goal first half wins R1. The protected handicap absorbed the draw that the winner label could not. **Note the same slate shape as `P-438`** — five rows on one low-event thesis — which here paid in full. That is precisely why `G-L21` is a *disclosure* and not a prohibition: a correlated slate is high-variance at card level in **both** directions, and the card must say so before the result is known. **Learning:** confirms soccer control 3 (draw-band discipline); no change.

---

### `P-440` — Ararat-Armenia 1–4 Sparta Praha (UEL league phase MD1)

**Verified this pass** at ESPN `uefa.europa` event 401915594: **HT 0–2**; goals 20', 22', 53', 55', 71'. Sparta 23 shots / 8 on target / 13 corners; Ararat 13 / 2 / 2.

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | First Half Under 2.5 | 0.89 | **WIN** | 0.0121 |
| 2 | Ararat-Armenia team total Under 2.5 | 0.87 | **WIN** | 0.0169 |
| 3 | Sparta Praha +1.5 | 0.86 | **WIN** | 0.0196 |
| 4 | Full Match Under 4.5 | 0.83 | **LOSS** | 0.6889 |
| 5 | Sparta Praha team total Over 0.5 | 0.76 | **WIN** | 0.0576 |

**Winner:** Sparta — WIN. **Card Brier 0.1590.** Rank #1 WIN · Hit@2 YES · Wins@2 2/2.

**Why:** exactly two first-half goals — the phase cap held with nothing to spare. The full-match U4.5 died on the fifth goal (71'), with three of the five goals arriving between 53' and 71'. **This is the cleanest phase-versus-full separation in the batch and a direct `C-PHASE-VS-FULL-TOTAL` data row:** on one card, in one match, the phase Under won and the 90-minute Under lost — the discriminating variable being the second half of a side with a 23-to-13 shot advantage. **Blind spot:** second-half scoring tail under a large shot advantage. Soccer control 39 already covers cross-league separation; this adds the *timing* dimension.

---

### `P-441` — Omonia Nicosia 1–0 Celta Vigo (UEL league phase MD1) — all five rows won

**Verified this pass** at ESPN `uefa.europa` event 401915611: **HT 0–0**; Balkovec **88'**. Celta 19 shots / 5 on target / 12 corners **and lost**; Omonia 10 / 4 / 3.

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | First Half Under 2.5 | 0.92 | **WIN** | 0.0064 |
| 2 | Full Match Under 4.5 | 0.91 | **WIN** | 0.0081 |
| 3 | Celta Vigo team total Under 2.5 | 0.90 | **WIN** | 0.0100 |
| 4 | Omonia team total Under 2.5 | 0.89 | **WIN** | 0.0121 |
| 5 | Celta Vigo +1.5 Asian Handicap | 0.86 | **WIN** | 0.0196 |

**Winner:** Celta — **LOSS**. **Card Brier 0.0112** — the best card in Part 4 to date. Rank #1 WIN · Hit@2 YES · Wins@2 2/2 · all rows WIN. Supplied FT Under 2.5 WIN; supplied 1H Over 0.5 LOSS, consistent with the card's own 46% zero-goal first half.

**Why — and the one methodological thing to keep from this card:** `P-441` is the only card in the batch that **printed a full goal-count distribution for both the phase and the 90 minutes** (1H 46/36/10/8 for 0/1/2/3+; FT 10/24/30/19/8/9 for 0/1/2/3/4/5+) and read every row off it. Its Rank #1 is therefore the only 0.90+ row in the batch that is reconstructable from the card. It also printed its own Fréchet bounds for `P(R1 ∩ R2)` (83%–91%) — the `G-L10` disclosure, executed. Celta's 19 shots and 12 corners without a goal vindicate the card's own "the shot/xG process is better than two goals suggests, but conversion is the problem" read: the process was right and the finishing failed — the mirror image of `P-438`, in the same import. **Preserve:** print the distribution, then read the rows off it. **Blind spot:** the winner label still leaned Celta at 43% against a home side for which the card itself listed four explicit upset branches.

---
### The eight MLB cards — read this before the individual entries

All eight were issued on the same supplied structure: `{underdog +1.5, favourite −1.5, Over L, Under L}`. That structure is **two forced pairs**, so every one of the eight cards scores exactly **2 W / 2 L by construction**, whatever happens. The row tally is therefore meaningless on its own and the honest unit is the **preferred side of each pair** — 16 decisions across the eight cards (`G-L15` labels the rows; the scorecard had not been segregating them → new **`G-L22`**).

| Decision family | Record | Mean Brier of the preferred side | Mean stated `p` | Realised |
|---|---|---:|---:|---:|
| Run line (which side, and by how much) | **6 W / 2 L** | 0.2074 | 60.9% | 75% |
| Total (which side of L) | **4 W / 4 L** | 0.2591 | 47.4% | 50% |
| **All 16 MLB decisions** | **10 / 16** | 0.2333 | — | 62.5% |

The totals result is **not** a failure: every preferred total sat at 44–53%, i.e. the cards correctly said they had almost no signal, and 4/8 is what a no-signal forecast should produce. Honest near-50% probabilities are preserved, not corrected.

**Empirical priors derived in this pass** from `statsapi.mlb.com`, all 2026 regular-season games completed through 16 Sep (**n = 2,286**), used below as the reference geometry. Full derivation in `RULES_BASEBALL.md` §"2026-09-17(b)".

| Quantity | 2026 value |
|---|---:|
| P(final margin = 1 run) | **27.8%** |
| P(margin = 1 \| winner), by winner-minus-loser season W% gap | −0.2: 28.4% · −0.1: 30.1% · 0.0: 28.2% · +0.1: 26.8% · **+0.2: 22.9%** |
| P(margin ≥ 2) / P(margin ≥ 3) | 72.2% / 53.3% |
| P(tie after 9 → extras) | **8.75%** (200 games) |
| In extras games: P(final margin = 1) | **68.5%** |
| Runs added by extras | mean **2.88**; P(≥ 2 added) **60.5%**; regulation total in those games mean 6.81 |
| Mean / median total runs; sd | 8.98 / 8; 4.53 |
| Largest push mass at any integer total | **11.5% at 7**; 8 → 8.1%, 9 → 9.1%, 11 → 7.3% |
| Share of total-runs variance explained by park identity | **4.3%** |

**Two systematic arithmetic defects fall straight out of this, both outcome-independent.**

**(1) The favourite −1.5 rows compressed the one-run band.** `P(fav −1.5) = P(fav wins) × (1 − r)` where `r = P(margin = 1 | winner)`.

| Card | Rank-#1 run line | Card `p` | Card's own implied `r` | Identity `p` at `r = 0.28` / `0.23` | Gap | Result |
|---|---|---:|---:|---:|---:|---|
| `P-444` | **NYY −1.5** (w = 0.69) | 0.56 | **18.8%** | 0.497 / 0.531 | **+3 to +6** | LOSS |
| `P-446` | **CHC −1.5** (w = 0.66) | 0.56 | **15.2%** | 0.475 / 0.508 | **+5 to +9** | WIN |
| `P-449` | **SD −1.5** (w = 0.64) | 0.55 | **14.1%** | 0.461 / 0.493 | **+6 to +9** | WIN |
| `P-442` | CWS +1.5 (dog) | 0.65 | 38.6% | 0.590 | +6 | LOSS |
| `P-443` | SF +1.5 (dog) | 0.61 | 29.1% | **0.610** | **0.0** | WIN |
| `P-447` | TEX +1.5 (dog side, card's winner) | 0.66 | 17.1% (opponent side) | 0.705 | **−5** | WIN |
| `P-448` | KC +1.5 (dog) | 0.65 | 36.4% | 0.604 | +5 | WIN |
| `P-450` | MIA +1.5 (dog) | 0.63 | 31.5% | 0.611 | +2 | WIN |

Every card that ranked a **favourite −1.5** first implied a one-run conditional of **14–19%**, against a 2026 league range of **23–28%**. Applying the identity moves all three to **0.46–0.53** — at or below the coin flip, which would have taken the −1.5 row out of Rank #1 on all three cards. The five underdog `+1.5` rows were within ±6 points of the identity and one (`P-443`) matched it exactly. **Structural consequence:** since `P(fav −1.5) ≤ 0.77 × P(fav wins)` and an MLB win probability above ~0.70 is not derivable, **a −1.5 row above ≈ 0.53 is not derivable from 2026 MLB margin geometry at all.** → new baseball control 34.

**(2) Push mass was over-stated on seven of eight cards.** The cards used 11–15% at their integer totals; the venue's own 2026 realised P(total = L) was 5.4–13.2%, and **no integer MLB total has an unconditional push mass above 11.5%**. Because park identity — the largest known between-game total driver — explains only **4.3%** of total-runs variance, a game-specific predictive distribution cannot be materially narrower than the league's, so a push mass above ~12% is not derivable. Over-stating it deflates *both* sides of the pair, which flatters Brier on a loss and, more importantly, **pushes total rows down the rank order against side rows** — which is plausibly why a side row was ranked #1 on all eight cards. → new baseball control 35.

**(3) Venue base-rate anchoring.** On 4 of the 8 cards the preferred total side opposed the venue's own 2026 base rate, and those went **1 W / 3 L**; the 4 that agreed with it went **3 W / 1 L**. Descriptive only at n = 8 — but the *disclosure* (print the venue base rate beside the line before choosing a side) costs nothing and was absent on all eight. → baseball control 35.

| Card | Venue | L | Card O / push / U | Venue 2026 O / push / U (n) | Preferred side vs venue |
|---|---|---:|---|---|---|
| `P-442` | Progressive Field | 7.0 | 48 / 15 / 37 | 53.8 / 10.3 / 35.9 (78) | agrees (Over) — **WIN** |
| `P-443` | Busch Stadium | 8.0 | 45 / 13 / 42 | 41.0 / 11.5 / 47.4 (78) | **opposes** — WIN |
| `P-444` | Target Field | 8.0 | 41 / 13 / 46 | 50.6 / 9.1 / 40.3 (77) | **opposes** — LOSS |
| `P-446` | Wrigley Field | 7.5 | 47 / — / 53 | 60.3 / — / 39.7 (78) | **opposes** — LOSS |
| `P-447` | Globe Life Field | 8.0 | 42 / 14 / 44 | 48.6 / 5.4 / 45.9 (74) | **opposes** — LOSS |
| `P-448` | Daikin Park | 9.0 | 36 / 15 / 49 | 40.3 / 10.4 / 49.4 (77) | agrees (Under) — **WIN** |
| `P-449` | Coors Field | 11.0 | 40 / 11 / 49 | 47.3 / 5.4 / 47.3 (74) | agrees (Under) — LOSS |
| `P-450` | Chase Field | 9.0 | 42 / 14 / 44 | 34.2 / 13.2 / 52.6 (76) | agrees (Under) — **WIN** |

`P-449` is worth naming separately: at Coors in 2026, **P(total ≥ 12) = 47.3%** and the median is 11. The card put 40% on Over 11.0. Its own retrospective said the Coors upper tail was "still too low" — the venue record says by roughly 7 points, before any matchup adjustment.

---

### `P-442` — Cleveland Guardians 6–3 Chicago White Sox (MLB) — **Rank #1 LOSS**

**Verified this pass:** `statsapi` gamePk 824382, Final, 9 innings, CWS 3 @ CLE 6. Total 9.

| Rank | Contract | `p` | Push | Result | Brier |
|---:|---|---:|---:|---|---:|
| 1 | White Sox +1.5 | 0.65 | 0 | **LOSS** | 0.4225 |
| 2 | Combined Total Over 7.0 | 0.48 | 0.15 | **WIN** | 0.2704 |
| 3 | Combined Total Under 7.0 | 0.37 | 0.15 | **LOSS** | 0.1369 |
| 4 | Guardians −1.5 | 0.35 | 0 | **WIN** | 0.4225 |

**Winner:** Cleveland — WIN. **Card Brier 0.3131.** Rank #1 LOSS · Hit@2 YES · Wins@2 1/2. No push (9 runs).

**Deep Rank-#1 review**

| Question | Finding |
|---|---|
| Why it was ranked first | The +1.5 cushion covers every Chicago win plus a one-run Cleveland win, and the platoon evidence was genuinely two-sided: Chicago .739 season / .781 L30 OPS vs LHP against Cleveland .665 / .650 |
| Was 0.65 supported? | **Not by the margin identity.** The card's own decomposition (CWS win 43%, CLE by exactly 1 = 22%) implies `r = 38.6%`, well above the 2026 conditional of 28–30% at this strength gap. At `r = 0.28` the row is **0.59**, not 0.65. It would still have been Rank #1 — but 6 points less confident, and the Brier cost of the loss would have fallen from 0.4225 to 0.348 |
| Should another row have ranked higher? | No. The Over was 48% and CLE −1.5 was 35%; promoting either now is hindsight |
| Actual mechanism | **Not the starter matchup the card worried about.** Anthony Kay allowed only two *unearned* runs in four innings — the "Kay collapses early" branch the card leaned on did not occur. Chicago led 3–2 on Pham's three-run homer. The game turned on the **relief transition**: Sean Newcomb allowed Petey Halpin's three-run homer in a four-run sixth. Messick went 6.0 IP / 3 ER / 8 K |
| Failure class | **Score-state bullpen mapping not executed.** Baseball controls 19–21 already require a relief chain by score state; the card printed bullpen *workload* (Cade Smith's five outs the night before) but never a leverage ladder for "starter contained → first damage in middle relief" |
| Knowable? | The branch was knowable; the specific Halpin homer was not. Cleveland's leverage arms were the researched object; the *middle*-relief matchup that actually decided it was not |
| Improvement | A `+1.5` may be ranked #1 only after the opponent's `starter contained → middle-relief damage → 2+ separation` path is printed as a weighted branch, even when the starter matchup favours the cushion. → baseball control 36 |

**What went right:** the Cleveland winner label was correct, and the card refused to convert Messick's quality into an automatic −1.5 — which was the right call on the geometry even though the −1.5 won. **O/U:** the Over won through the same sixth-inning cluster that broke the cushion — a `G-L18` coupling the card did not print.

---

### `P-443` — San Francisco Giants 6–5 St. Louis Cardinals, 10 innings (MLB)

**Verified this pass:** gamePk 823004; inning-by-inning **regulation 4–4**, away 10th +2, home 10th +1. Final total **11**.

| Rank | Contract | `p` | Push | Result | Brier |
|---:|---|---:|---:|---|---:|
| 1 | Giants +1.5 | 0.61 | 0 | **WIN** | 0.1521 |
| 2 | Combined Total Over 8.0 | 0.45 | 0.13 | **WIN** | 0.3025 |
| 3 | Combined Total Under 8.0 | 0.42 | 0.13 | **LOSS** | 0.1764 |
| 4 | Cardinals −1.5 | 0.39 | 0 | **LOSS** | 0.1521 |

**Winner:** St. Louis — **LOSS**. **Card Brier 0.1958.** Rank #1 WIN · Hit@2 YES · Wins@2 2/2.

**Why, and the single most important settlement fact in the batch:** **regulation ended 4–4, exactly on the push.** Had the game ended after nine, Over 8.0 and Under 8.0 would both have been void. The extras innings added three runs and settled the pair. `P-443`'s Rank #1 is also the **only** run-line row in the cohort whose probability exactly equals the margin identity (0.45 + 0.55 × 0.29 = 0.61). **What went right:** the card kept Molina's good-start branch alive on his better FIP/xERA rather than letting one bad prior start own the forecast — he threw 5.2 scoreless. **Blind spot:** `P(tie after 9)` was never printed; at an integer total it is the single largest determinant of whether the pair even settles. → baseball control 37.

---

### `P-444` — Minnesota Twins 5–4 New York Yankees, 13 innings (MLB) — **Rank #1 LOSS; both top two lost**

**Verified this pass:** gamePk 823655; **regulation 2–2**; innings 10–13 added 2 (away) and 3 (home). Final total **9**.

| Rank | Contract | `p` | Push | Result | Brier |
|---:|---|---:|---:|---|---:|
| 1 | Yankees −1.5 | 0.56 | 0 | **LOSS** | 0.3136 |
| 2 | Combined Total Under 8.0 | 0.46 | 0.13 | **LOSS** | 0.2116 |
| 3 | Twins +1.5 | 0.44 | 0 | **WIN** | 0.3136 |
| 4 | Combined Total Over 8.0 | 0.41 | 0.13 | **WIN** | 0.3481 |

**Winner:** Yankees — **LOSS**. **Card Brier 0.2967.** Rank #1 LOSS · **Hit@2 NO** · Wins@2 0/2.

**Deep Rank-#1 review**

| Question | Finding |
|---|---|
| Why it was ranked first | Rodón/Matthews season gap, Yankees-vs-RHP strength, Twins-vs-LHP weakness and bullpen freshness all pointed at separation, and the card projected NYY to win at 69% |
| Was 0.56 supported? | **No.** The card's own decomposition put NYY-by-exactly-1 at 13% against a 69% win probability — an implied one-run conditional of **18.8%**, against 22.9% for the strongest 2026 favourites and 28% league-wide. At `r = 0.23` the row is **0.531**; at `r = 0.28` it is **0.497**. Either way it is **not** a 0.56 row, and at 0.497 it would not have been Rank #1 |
| Should another row have ranked higher? | On the corrected geometry, **Twins +1.5** becomes 0.31 + 0.69 × 0.28 = **0.503** — i.e. the two run-line rows were effectively a coin flip, not a 56/44 split. The card's own contrary evidence (Matthews' 2.84 home ERA, an explicit 3–2/4–3 branch) was never priced |
| Extras interaction — the decisive one | The card never printed `P(tie after 9)`. The 2026 prior is **8.75%**, and **in extras games the final margin is one run 68.5% of the time**. So the extras branch is nearly a dead zone for a −1.5 row and nearly pure profit for a +1.5 row: `P(dog +1.5 \| extras) ≈ 0.84`. That branch alone contributes ~7.4 points to a +1.5 row and ~1.4 to a −1.5 row — a **6-point swing** that no card in this cohort priced |
| Both-top-two failure | R1 (NYY −1.5) and R2 (Under 8.0) share a driver in the *opposite* direction from how the card read it: a Rodón-suppressed low-scoring game makes the Under likelier **and the −1.5 less likely**. The card treated "starter suppression" as supporting both. `P(¬R1 ∧ ¬R2)` was never printed, and the state that produced it — **close low-scoring game → tie after nine → automatic-runner extras** — is a single named state. → `G-L17` executed, and `G-L21` for the direction check |
| Unforeseeable element | Aaron Judge exited with lower-right-leg tightness in-game. Genuine realised variance, not a sourcing failure |
| Failure class | **Margin geometry plus an un-priced endpoint**, not a starting-pitcher read. Rodón's run-prevention case was accurate (2 runs in 6 innings) |

**Regulation truth:** the nine-inning total was **4**. Grading this as a failed run-environment read would be wrong; it is an extras-endpoint miss, and the paired opposite of `P-443`. **What went right:** the starter read.

---

### `P-446` — Chicago Cubs 8–4 Atlanta Braves (MLB)

**Verified this pass:** gamePk 824626, 9 innings, total 12.

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Cubs −1.5 | 0.56 | **WIN** | 0.1936 |
| 2 | Combined Total Under 7.5 | 0.53 | **LOSS** | 0.2809 |
| 3 | Combined Total Over 7.5 | 0.47 | **WIN** | 0.2809 |
| 4 | Braves +1.5 | 0.44 | **LOSS** | 0.1936 |

**Winner:** Cubs — WIN. **Card Brier 0.2373.** Rank #1 WIN · Hit@2 YES · Wins@2 1/2.

**Why:** the side read was the card's best work — Chicago's .838 OPS vs RHP against Ritchie's 5.41 FIP and 14.1% walk rate, with Imanaga controlling Atlanta (1 run in 6). Ritchie went 4.2 and allowed six. **The Rank #1 won despite the same compressed one-run band as `P-444` and `P-449`** (implied `r` = 15.2%): the identity value is 0.475–0.508, so the row was right for the right mechanism at the wrong confidence. **The Under lost to the identical branch that won the side** — Cubs separation *is* an Over mechanism at a 7.5 line, and the venue made it worse: **Wrigley 2026 mean total 9.85, P(Over 7.5) = 60.3%**, against the card's 47%. A wind-in note was allowed to override a venue base rate it should only have modified. → `G-L18` plus baseball control 35.

---

### `P-447` — Texas Rangers 7–3 Boston Red Sox (MLB)

**Verified this pass:** gamePk 822846, 9 innings, total 10.

| Rank | Contract | `p` | Push | Result | Brier |
|---:|---|---:|---:|---|---:|
| 1 | Rangers +1.5 | 0.66 | 0 | **WIN** | 0.1156 |
| 2 | Combined Total Under 8.0 | 0.44 | 0.14 | **LOSS** | 0.1936 |
| 3 | Combined Total Over 8.0 | 0.42 | 0.14 | **WIN** | 0.3364 |
| 4 | Red Sox −1.5 | 0.34 | 0 | **LOSS** | 0.1156 |

**Winner:** Texas — WIN. **Card Brier 0.1903.** Rank #1 WIN · Hit@2 YES · Wins@2 1/2.

**A structural note worth keeping:** this is the only card in the cohort where the Rank-#1 contract and the projected winner are **the same team on the plus side of the line** — Texas was given 59% to win *and* ranked as the +1.5 cushion. That is internally coherent but it makes the row's probability almost entirely a statement about the *opponent's* one-run band, which the card left at an implied 17.1%. The identity gives **0.705**, five points above the stated 0.66 — the one case in the batch where the arithmetic would have made the card *more* confident in a row that won. **Why it won:** Texas' .869 L30 OPS vs LHP (best in MLB, .936 at home) produced 13 hits and a three-run seventh. **Unforeseeable:** Gore left after four-plus with back spasms; Eovaldi's four scoreless relief innings then suppressed the Boston side of the total. **Blind spot:** the card let Globe Life Field's suppressive reputation hold down a team-score marginal that its own platoon evidence had just made extreme — the venue's 2026 realised P(Over 8.0) was 48.6%, not the 42% used. → `G-L18` team-score marginal.

---

### `P-448` — Kansas City Royals 5–2 Houston Astros (MLB) — both top two won

**Verified this pass:** gamePk 824140, 9 innings, total 7.

| Rank | Contract | `p` | Push | Result | Brier |
|---:|---|---:|---:|---|---:|
| 1 | Royals +1.5 | 0.65 | 0 | **WIN** | 0.1225 |
| 2 | Combined Total Under 9.0 | 0.49 | 0.15 | **WIN** | 0.2601 |
| 3 | Combined Total Over 9.0 | 0.36 | 0.15 | **LOSS** | 0.1296 |
| 4 | Astros −1.5 | 0.35 | 0 | **LOSS** | 0.1225 |

**Winner:** Houston — **LOSS**. **Card Brier 0.1587.** Rank #1 WIN · Hit@2 YES · Wins@2 2/2.

**Why:** Lynch threw five scoreless (2 H, 1 BB, 3 K); Rave and Massey homered. The card's explicit separation of *winner* from *margin* is the thing to preserve: it refused to let Houston's home last-bat and bullpen quality force an Astros −1.5, and both top rows won while the winner label lost. **Best-calibrated card of the eight on the margin identity** alongside `P-443`: implied `r` = 36.4%, slightly generous but on the right side of the prior, and the +1.5 at 0.65 is 4.6 points above the identity's 0.604 — the smallest over-statement among the +1.5 rows that won.

---

### `P-449` — San Diego Padres 9–3 Colorado Rockies (MLB)

**Verified this pass:** gamePk 824306, 9 innings, total 12.

| Rank | Contract | `p` | Push | Result | Brier |
|---:|---|---:|---:|---|---:|
| 1 | Padres −1.5 | 0.55 | 0 | **WIN** | 0.2025 |
| 2 | Combined Total Under 11.0 | 0.49 | 0.11 | **LOSS** | 0.2401 |
| 3 | Rockies +1.5 | 0.45 | 0 | **LOSS** | 0.2025 |
| 4 | Combined Total Over 11.0 | 0.40 | 0.11 | **WIN** | 0.3600 |

**Winner:** San Diego — WIN. **Card Brier 0.2513.** Rank #1 WIN · Hit@2 YES · Wins@2 1/2.

**Why:** the favourite-separation thesis was right — Adams' 5.68 FIP and pitch cap plus Colorado bullpen exposure outweighed Ray's two poor September starts, and Ray returned six innings with six strikeouts. **Both defects in one card:** the −1.5 implied a **14.1%** one-run conditional (the most compressed in the batch, identity 0.461–0.493) and the Under used an **11% push mass at Coors where the 2026 realised P(total = 11) is 5.4%** and **P(≥12) is 47.3%** against the card's 40%. Correcting both would have moved the Under below the Over and the −1.5 to a coin flip. The card won on the side and lost on the total; the arithmetic says it should have been less confident about both. **What went right:** refusing to let Ray's two-start sample define him (`G-L7`).

---

### `P-450` — Miami Marlins 4–3 Arizona Diamondbacks (MLB) — both top two won

**Verified this pass:** gamePk 825031, 9 innings, total 7.

| Rank | Contract | `p` | Push | Result | Brier |
|---:|---|---:|---:|---|---:|
| 1 | Marlins +1.5 | 0.63 | 0 | **WIN** | 0.1369 |
| 2 | Combined Total Under 9.0 | 0.44 | 0.14 | **WIN** | 0.3136 |
| 3 | Combined Total Over 9.0 | 0.42 | 0.14 | **LOSS** | 0.1764 |
| 4 | Diamondbacks −1.5 | 0.37 | 0 | **LOSS** | 0.1369 |

**Winner:** Arizona — **LOSS**. **Card Brier 0.1910.** Rank #1 WIN · Hit@2 YES · Wins@2 2/2.

**Why:** Miami's recent RHP split and Kelly's season vulnerability held; Arizona's three runs all came on solo homers with no multi-run inning. Marsee's two-run homer supplied the margin. Implied `r` = 31.5%, within two points of the identity — one of the two best-specified run lines in the batch. **The one incoherence the card itself named:** Arizona was given 54% to win on the *same* evidence base that made Miami +1.5 the strongest contract. The winner distribution and the run-line distribution must inherit the same platoon evidence; here they did not. → `G-L21` direction check.

---

### `P-445` — Barbados Tridents 144/6 lost to Jamaica Kingsmen 145/1 (14.1) by 9 wickets — CPL Eliminator — **CONDITION NOT MET / NO ACTION**

**Verified this pass** at ESPN `cricket/1534175/summary?event=1534214`: `section 1` of the matchnotes is the **Barbados** innings, so **Barbados batted first**. Barbados powerplay **24/4**; Barbados 144/6 (20); Jamaica chase powerplay **79/0**; Maaz Sadaqat **100 off 44**, finishing 112 off 49; Jamaica 145/1 in 14.1. Saim Ayub, unresolved at the freeze, **did play**.

| Rank | Frozen conditional contract | Result |
|---:|---|---|
| 1 | Jamaica first 6 overs Under 55.5 | **NO ACTION — CONDITION NOT MET** |
| 2 | Jamaica first innings Under 169.5 | **NO ACTION** |
| 3 | Jamaica first 6 overs Over 34.5 | **NO ACTION** |
| 4 | Jamaica first innings Under 157.5 | **NO ACTION** |

**Winner:** Barbados — **LOSS**. **No Brier.** Rank-#1 and top-two metrics are undefined and the card is excluded from every cohort rate below.

**This is the process success of the batch.** The card froze, before the toss, that every Jamaica innings and powerplay row was conditional on Jamaica batting first, and named the failure explicitly: *"If Barbados bats first, these exact targets are not silently transferred to Jamaica's second innings."* Jamaica won the toss and bowled. Nothing was transferred. Had the rows been silently reassigned to Jamaica's chase, the powerplay row would have been settled against a **79/0** target-censored chase powerplay — a different contract in a different tactical state — and the innings rows against a target-capped 145/1. That is exactly the [chase-total cap](RULES_CRICKET.md) failure mode, avoided. **Preserve the gate verbatim.** → cricket control 32 records it as positive evidence.

**Why the winner call lost:** Jamaica's new ball removed four Barbados batters inside the powerplay (24/4), and Sadaqat's century ended the chase in 14.1 overs. The card's four-straight-wins/home-form case for Barbados was outweighed by Jamaica's batting ceiling, which the card itself had flagged as "higher than the venue sample implies" and then under-weighted in the 62/38 split. **Blind spots:** confirmed XIs and the toss were both unretrieved at the freeze — and the toss is the single field that decided whether the card had any active contract at all.

---

### `P-451` — Dorados de Chihuahua 97–86 El Calor de Cancún, LNBP Jornada 20 — **BLOCKED AT ISSUE / NO FORECAST; result now recovered**

**Disposition:** `FINAL / NO ISSUED FORECAST / NO SCORED TRIAL`. `BK-P1 = FAIL` under `RULES_BASKETBALL.md` §9.5: no current LNBP competition-regulation packet closing period length, foul-out/bonus, challenges, overtime resolution, roster activation, import eligibility or abandonment treatment was recoverable before the tip. The card issued **no rank, probability, winner or direction**, so nothing enters any W/L, Brier, Rank-#1 or winner count.

**Result recovery — the mini log left this open; it is closed here.** The mini log recorded `RESULT_NOT_RELIABLY_RECOVERED` and correctly warned against reusing the Jornada 19 91–89. This pass recovered the field-owner record: **`lnbp.mx/Dorados/team_results.html`, Jornada 20 filter — Dorados 97, El Calor 86.** The page is JavaScript-only (a `curl` returns a 16 KB shell containing no scores), which is why every text-fetch route in the mini log's pass failed; it renders correctly in a browser. The handle `TMP-OPEN-20260917-02` is opened and retired in the same edit. A separate search for a 2026 LNBP regulation packet again returned nothing, so **`BK-P1` stays FAIL** and the block remains correct.

| Frozen supplied contract | Realised (183 total, 11-point margin) | Grade |
|---|---|---|
| Dorados −4.5 | Covered | `NOT GRADED` — nothing was issued |
| El Calor +4.5 | Lost | `NOT GRADED` |
| Over 176.5 | Over | `NOT GRADED` |
| Under 176.5 | Lost | `NOT GRADED` |

**What the block cost, measured honestly:** the card listed four shortcuts it refused to take — home record → Dorados, close first game → El Calor +4.5, the 180-point first game → Over, season scoring averages → Under. Two would have won and two would have lost. The fail-close was free on this occasion as well as correct. **What went right:** the gate held under pressure from a same-opponent, next-night fixture where the search surface was saturated with the previous game's result — the exact `§16.10(i)` collision the rule exists for.

---
### Cohort audit — the twelve cards that issued ranked probabilities

`P-445` (conditional rows never activated) and `P-451` (blocked, nothing issued) are excluded from every metric below.

| Measure | Value |
|---|---|
| Graded ranked rows | **52** (31 W / 21 L) |
| Mean Brier | **0.2097** against 0.25 for the 0.5 baseline. **All 52 rows and all 12 card means recomputed from probability and result — 52 of 52 reproduce**, and the mini log's own 0.2097 reproduces exactly |
| Rank #1 | **9 W / 3 L** (losses: `P-438`, `P-442`, `P-444`) |
| Hit@2 | **10 / 12** (`P-438` and `P-444` failed) |
| Both top two won | **6 / 12** |
| Top-two slots | **16 W / 24** |
| Potential winners | **6 / 13** (13 labels, including `P-445`, whose ranked rows were void but whose winner label settled) |
| Population | **8 MLB = `PRIMARY_SCORED`** (32 rows); 4 soccer = `EXPLORATORY` (20 rows). This is the first `PRIMARY_SCORED` material in Part 4 |

**Split by population and by row type — the split that matters here.**

| Subset | Rows | W / L | Mean Brier | Note |
|---|---:|---|---:|---|
| MLB (`PRIMARY_SCORED`) | 32 | 16 / 16 | **0.2293** | **All 32 are `FORCED_PAIR`**; the 16/16 is arithmetic, not performance |
| Soccer (`EXPLORATORY`) | 20 | 15 / 5 | **0.1783** | All 20 are `FREE` |
| MLB as *decisions* (preferred side of each pair) | 16 | **10 / 6** | 0.2333 | Run lines 6/8 at 0.2074; totals 4/8 at 0.2591 |

**Calibration by stated-probability band** (dependence caveat below):

| Band | Rows | W | Realised | Mean stated | Gap |
|---|---:|---:|---:|---:|---:|
| ≥ 0.80 | 15 | 11 | 73.3% | 86.4% | **−13.1** |
| 0.60–0.79 | 10 | 8 | 80.0% | 68.6% | +11.4 |
| 0.50–0.59 | 4 | 2 | 50.0% | 55.0% | −5.0 |
| 0.40–0.49 | 16 | 9 | 56.3% | 44.5% | +11.8 |
| < 0.40 | 7 | 1 | 14.3% | 36.1% | **−21.8** |

The shape is over-extremity at both ends and under-confidence in the middle — the classic signature `C-PROB-EXTREMITY` was opened to watch. **Three caveats that stop this being a finding:** (a) **3 of the 4 losses in the ≥ 0.80 band come from one card** (`P-438`), so the effective independent sample in that band is about two events, not fifteen; (b) the 0.40–0.49 and < 0.40 bands are mechanically complementary inside forced pairs and cannot both be read as independent evidence; (c) n = 52 rows in 12 cards. **No cap, bar or shrinkage is imposed.** It is recorded as a `C-PROB-EXTREMITY` row, and the response is the `G-L21` card-level disclosure, which addresses cause (a) directly — the right unit for extremity is the card, not the row.

**Why the soccer Brier (0.1783) beat the MLB Brier (0.2293):** contract geometry, not forecasting skill. The soccer cards chose wide alternate lines far from the centre; the MLB cards were handed two near-centre forced pairs and had no wide alternate available. Comparing the two is comparing the lines, not the analysis.

### Over/under review (the standing directive)

| Family | Record this batch | Rows |
|---|---|---|
| Low-threshold team totals (team U2.5 / team O0.5) | **5 W / 1 L** | `P-438` AW U2.5 L; `P-439`, `P-440` ×2, `P-441` ×2 W |
| Phase totals (1H U1.5 / U2.5) | **4 W / 1 L** | only `P-438`'s U1.5 lost |
| Wide full-match alternates (U3.5 / U4.5) | **2 W / 2 L** | `P-438` U3.5 and `P-440` U4.5 lost |
| Near-centre supplied main lines (FT U2.5; all eight MLB combined totals) | **4 W / 5 L** | the eight MLB preferred sides went 4/4 |

**Third consecutive cohort consistent with `C-OU-GEOMETRY`:** free, tail-ward and single-side totals outperform near-centre preferred sides. The manifest requires 50 cards before promotion and **no ordinal bar follows**. Note honestly that this cohort's wide-alternate row went only 2/4 — the previous cohort's 4/4 did not repeat.

**Three distinct totals failure mechanisms, all of which are allocation or endpoint problems rather than run/goal-environment problems:**

1. **Allocation** (`P-438`, `P-446`, `P-449`) — the total landed through a distribution of scoring the card did not forecast. `P-438` is the extreme: five goals where two came from a side that took **two shots all match**. A correct or incorrect total says nothing about the allocation that produced it. → `G-L18`.
2. **Endpoint** (`P-443`, `P-444`) — a clean matched pair. `P-443` regulation ended **exactly on the push** (4–4 at L = 8) and extras made it an Over; `P-444` regulation produced **4 runs** at L = 8 and four extra frames made it an Over. Neither is a nine-inning run-environment miss. → baseball control 37.
3. **Venue anchoring** (`P-444`, `P-446`, `P-447`) — the preferred side opposed the venue's own 2026 base rate with no named mechanism. → baseball control 35.

**No artificial hedging was introduced, and none is recommended.** The MLB cards' near-50% totals are the correct output of a genuinely uncertain read, and forcing separation between the two sides of a forced pair would be the opposite of an improvement.

### Line-up, bench and availability audit

| Card | Starters | Bench / reserves | Coaches | Availability |
|---|---|---|---|---|
| `P-438` | `RETRIEVAL_MISS` | `RETRIEVAL_MISS` | context only | partial |
| `P-439` | `RETRIEVAL_MISS` | `RETRIEVAL_MISS` | context only | partial |
| `P-440` | official squad list; same-day XI `RETRIEVAL_MISS` | `RETRIEVAL_MISS` | obtained | checked |
| `P-441` | **`RETRIEVAL_MISS`, explicitly recorded**; UEFA squad list retrieved | `RETRIEVAL_MISS` | **both obtained** (Berg, Giráldez) | Aspas **confirmed out**; three secondary "out" claims correctly rejected against the official travelling squad |
| `P-442` | MLB page `TBD` at freeze | leverage workload researched | not modelled | Martínez / DeLauter day-to-day, unresolved |
| `P-443` | `TBD` | broad state only | not material | Giants depletion and Wetherholt return checked |
| `P-444` | `TBD`; Judge return a **high-quality projection**, correctly not labelled official | incomplete | **Boone's Judge plan captured** | Judge played and exited injured in-game |
| `P-445` | `RETRIEVAL_MISS`; **the toss was also unretrieved** | prior-match XIs only | not material | Saim Ayub unresolved (he played) |
| `P-446` | reported, not field-owner confirmed | incomplete | Ritchie/Sale rest decision captured | IL changes captured |
| `P-447` | BOS `TBD`; **TEX same-day lineup stored as "current reported", explicitly not upgraded to `CONFIRMED_OFFICIAL`** | incomplete | partial | IL checked; Gore's in-game spasms unforeseeable |
| `P-448` | `RETRIEVAL_MISS` | leverage usage checked | none material | Correa shutdown checked |
| `P-449` | projected, not confirmed | recent workload well researched | **Adams pitch cap captured** | Goodman uncertainty and both ILs checked |
| `P-450` | `RETRIEVAL_MISS` | **prior-night relief workload well documented** | Nelson/Gallen bullpen role changes researched | Fairbanks loss and roster moves checked |
| `P-451` | previous-game five only | partial | **both obtained** | McKinney cramps, Chapman registration, González departure — all researched with uncertainty preserved |

**Headline: 0 of 13 cards obtained a confirmed official starting line-up for both sides.** That is the most universal gap in the batch and it recurs from every previous cohort.

**But it was the binding constraint on none of them.** This needs saying plainly, because the obvious conclusion — "try harder on line-ups" — would misdirect the fix. Working through what actually decided each card: margin arithmetic (`P-444`, `P-446`, `P-449`), the extras endpoint (`P-443`, `P-444`), venue base rate (`P-444`, `P-446`, `P-447`), the **toss** (`P-445`), slate correlation and finishing variance (`P-438`), and a **middle reliever** who would not appear on any batting order (`P-442`). A confirmed line-up would have changed none of these. The two availability facts that did matter were **the toss** in cricket and **bullpen role state** in baseball — neither of which is a line-up field. `P-447` and `P-444` both show the correct handling of partial information: store it at its true grade and cap accordingly.

**Positive practice to preserve:** `P-441` rejecting three third-party "player X is out" claims because the player appeared in the club's own published travelling squad; `P-447` refusing to upgrade a reported lineup to `CONFIRMED_OFFICIAL`; `P-451` holding McKinney's and Chapman's status at `UNCERTAIN` rather than assuming either way.

### Source audit

| Source | Field it owned here | Verdict |
|---|---|---|
| `statsapi.mlb.com` schedule + `/game/{pk}/linescore` | All 8 MLB finals, **and inning-by-inning regulation splits** | **Authoritative, keyless, fast, complete.** It settled the `P-443`/`P-444` extras question that narrative recaps could not. Remains the primary MLB lane and is now also the **base-rate lane** (§"Algorithm changes") |
| ESPN site API `soccer/afc.cup` | **= AFC Champions League Two.** Finals, goal minutes, red cards, shots, corners, possession | **New lane, first use, verified.** The mini log settled `P-438`/`P-439` from AFC narrative reports and consequently **missed a 60' red card and a 41-vs-2 shot count**. → `SOURCES.md` |
| ESPN site API `soccer/uefa.europa` | UEL finals, HT states, goal minutes, match stats | Verified; reproduced both finals and both half-time scores exactly |
| ESPN site API `cricket/1534175` | CPL 2026 innings order, powerplays, matchnotes, XIs | **Verified.** The series ID was **already in `DATA_SOURCE_REGISTER.md`** from `P-217`; the mini log searched for a CPL scorecard route instead of consulting the register — a `G-L14` miss |
| `lnbp.mx/<Team>/team_results.html` | LNBP per-Jornada finals | **Field owner, but JavaScript-only.** `curl` returns a 16 KB shell with no scores; the rendered page returns them immediately. This is why the mini log recorded `RESULT_NOT_RECOVERED` |
| AFC / UEFA official reports | Scores, scorers, narrative | Accurate on what they publish; **no shot, corner or disciplinary field** on the AFC report — the same limitation that left `P-430-C05` open |
| AP / Reuters / CBS recaps | Mechanism narrative, injury context | Accurate on mechanism; they gave the `P-443`/`P-444` finals but **not** the regulation split that the analysis needed |
| `hs-consumer-api.espncricinfo.com` | (attempted) current/results index | **403 Access Denied — degraded.** Record as unavailable |
| `cricketworld.com` (the mini log's cited `P-445` route) | CPL scorecard | **Cloudflare interstitial through `r.jina.ai`** — the cited URL is not reproducible by this repository's ladder. The ESPN series route is the replacement |
| `sportytrader.es` | surfaced an "83-77" LNBP line in search | **Rejected.** Tipster/odds display, not a field owner, and the figure matched no verified Dorados–El Calor game |

**Newly recommended or re-prioritised sources** are written up in `SOURCES.md` §"2026-09-17(b)" and `DATA_SOURCE_REGISTER.md` with retrieval method, sport, field, reliability and tier.

### Blind-spot audit

| # | Blind spot | Available pre-game? | How much it mattered | Mitigation | Disposition |
|---|---|---|---|---|---|
| 1 | **MLB margin identity** — the one-run band compressed to 14–19% on every favourite −1.5 | **Yes** — a season of finals is one keyless call | Decided the ranking on 3 cards | Derive the run line from `P(win) × (1 − r)` with `r` printed | **New rule** — baseball control 34 |
| 2 | **Extras endpoint never priced** | **Yes** — `P(tie after 9)` = 8.75% is computable from the same feed | Settled the total on 2 of 8 MLB cards | Print `P(tie after 9)` and the extras branch beside any integer total | **New rule** — baseball control 37 |
| 3 | **Push mass over-stated on 7 of 8 cards** | **Yes** | Distorted the rank order of total vs side rows on every MLB card | Cap the derivable push at the venue/league realised rate | **New rule** — baseball control 35 |
| 4 | **Venue base rate not printed beside the line** | **Yes** | Preferred side opposed it on 4 cards; those went 1/3 | Print it; a contrary side needs a named mechanism | **New rule** — baseball control 35 |
| 5 | **Card-level correlated slate** — 4 of 5 `P-438` rows on one thesis | **Yes**, from the card's own marginals | Produced the worst card in Part 4 | Print `P(all correlated rows fail)` with Fréchet bounds | **New rule** — `G-L21` |
| 6 | **Result-vs-process confusion at settlement** — `P-438`'s retrospective inferred an early-goal modelling failure from a 2-shot/2-goal match | n/a (settlement-side) | Would have produced a harmful rule change | Pull shots/SOT/disruptions before amending any control | **New rule** — `G-L23` |
| 7 | **Disruption facts not copied** — the 60' red card in `P-438` | n/a (settlement-side) | Removed the actual mechanism for goals 4 and 5 | §16.11(o) already requires it; it was listed and not executed | **Execution** (`M15`) |
| 8 | **Phase distribution not printed** — `P-438` assigned 0.84 to a U1.5 with no goal-count distribution | **Yes** | The whole Rank-#1 failure | `G-L8` already requires it | **Execution** (`M15`); soccer control 40 makes it explicit for sibling lines |
| 9 | **Confirmed line-ups on 0 of 13 cards** | Partly — MLB orders post late; UEFA/AFC publish ~60 min out | **Binding on none of them** (see the line-up audit) | Keep the existing caps; do not escalate | **Observation** — no new rule |
| 10 | **`DATA_SOURCE_REGISTER.md` not consulted before searching for a CPL route** | Yes — the series ID was already recorded | Cost a settlement route | `G-L14` already requires it | **Execution** (`M15`) |
| 11 | **Toss unretrieved at freeze** (`P-445`) | Marginal — the toss is ~30 min pre-match and the freeze was earlier | Determined whether the card had any active contract | The conditional gate handled it correctly | **No change** — preserve the gate |
| 12 | **Winner label and ranked-row evidence diverged** (`P-450`, `P-448`, `P-441`, `P-439`) | Yes | Cost 4 winner labels; cost no ranked row | Winner and handicap distributions must inherit the same evidence | **Rule** — `G-L21`(c) |

### Comparison against previous lessons

| Observation | Seen before? | Rule existed? | Followed? | Verdict |
|---|---|---|---|---|
| Correlated top rows failing together | `P-397`, `P-413`, `P-414`, `P-426`, **`P-427`** | `G-L17` (2026-09-17, one day old) | **Not executed on `P-438` or `P-444`** | Recurring and now 6 cards across 4 sports. `G-L17` is right but too narrow → **extend to `G-L21`** |
| Total correct for the wrong allocation | `P-425`, `P-430`, `P-433` | `G-L18` | Not executed on `P-438`, `P-446`, `P-449` | Recurring; **no new rule**, execution gap |
| Aggregate used where a disaggregated record existed | `M13`, `G-L7` | Yes | **Followed well** — `P-449` (Ray's 2-start sample), `P-443` (Molina's FIP/xERA) both refused the aggregate and both were vindicated | **Working. Preserve** |
| Small-sample rate taken as direction | `G-L11`, `M17` | Yes | Followed — `P-449` handled Adams' small sample as width | **Working** |
| Margin centred toward pick'em by uncertainty | `G-L12` (NFL width floor) | Yes, for NFL | **No baseball instantiation existed** | **Genuine gap** → baseball control 34 |
| Control listed but not executed | `M15`, §16.8 | Yes | **4 instances this batch** (§16.11(o), `G-L8`, `G-L14`, `G-L17`) | The §16.8 completeness block is the right mechanism and is still being skipped → `G-L21`(d) makes the block's failure-mass line mandatory rather than advisory |
| Conditional contract not transferred to the wrong innings | `P-445` | cricket target-identity gate | **Followed exactly** | **Working. Preserve verbatim** |
| Fail-closed on unresolved competition rules | `P-451`, and `P-424`/`P-428` last cohort | `BK-P1`, §16.10(i) | **Followed** | **Working**; three consecutive correct fail-closes |

### What went right — preserve these

1. **`P-441`'s printed goal-count distribution.** The only card in the batch whose 0.90+ rows are reconstructable, and the best Brier in Part 4 (0.0112). Print the distribution, then read the rows off it.
2. **`P-445`'s conditional activation gate.** It prevented a first-innings target from being settled against a target-censored chase. This is the batch's clearest process win and it produced *no* score at all — which is the point.
3. **`P-451`'s fail-close** under maximum collision pressure (same opponents, consecutive nights, search surface saturated with the previous night's score).
4. **Winner/margin separation** (`P-448`, `P-450`, `P-442`). Three cards refused to convert a home-field or bullpen-quality edge into a favourite run line. The two that held the separation cleanly won both top rows.
5. **Disaggregated records beating aggregates** (`P-449` Ray, `P-443` Molina). Both cards kept a good-start branch alive against a bad recent sample and both branches realised.
6. **Honest near-50% probabilities on MLB totals.** All eight sat at 44–53% and went 4/4. The correct response to no signal.
7. **Evidence hygiene**: `P-441` rejecting unofficial absence claims against the club's own squad list; `P-447` refusing to upgrade a reported lineup.
8. **Process reads vindicated even where results went against them** — `P-441` (Celta 19 shots, 12 corners, no goal) and `P-438` (Kuwait 2 shots all match). Both confirm the shot-process model was working; only `P-438`'s conversion variance made it look otherwise.

### Rule and algorithm changes made in this pass

| Change | Type | Home | Evidence |
|---|---|---|---|
| **`G-L21`** — card-level shared-driver failure mass; extends `G-L17` past the top two, adds the winner/ranked-row direction check | Disclosure | `RULES_GENERAL.md` §16.13(a) | `P-438` (4 rows, one thesis), `P-444` (R1 and R2 needed opposite things), `P-450`/`P-448` (winner ≠ row evidence) |
| **`G-L22`** — `FORCED_PAIR` rows are one decision, not two; the scorecard reports free and forced subsets separately | Measurement | §16.13(b) | All 8 MLB cards scored 2 W / 2 L by construction |
| **`G-L23`** — result-versus-process separation at settlement; pull the structured process record and disruption facts before amending any control | Integrity | §16.13(c) | `P-438` (2 shots → 2 goals; 60' red card, both absent from the mini log's diagnosis) |
| **Baseball control 34** — MLB run-line margin identity with a printed `r` | Derivation | `RULES_BASEBALL.md` | 3 favourite −1.5 rows at implied `r` = 14–19% vs 2026's 23–28% |
| **Baseball control 35** — venue base rate and push-mass ceiling printed beside every integer total | Derivation | same | Push over-stated on 7/8; preferred side opposed the venue on 4/8 |
| **Baseball control 36** — `starter contained → middle relief → 2+ separation` branch before a run line is ranked #1 | Disclosure | same | `P-442` (Kay 2 unearned in 4; Newcomb gave up the decisive homer) |
| **Baseball control 37** — the three-layer MLB total object: 9-inning distribution → `P(tie after 9)` → extras distribution | Derivation | same | `P-443` and `P-444`, opposite endpoints of the same mechanism |
| **Soccer control 40** — sibling phase lines must come from one printed phase distribution and be mutually consistent | Disclosure | `RULES_SOCCER.md` | `P-438` U1.5 at 0.84 vs three U2.5 siblings at 0.87–0.92 |
| **Soccer control 41** — settle from a feed that carries shots, cards and minutes, not from a narrative report | Integrity | same | `P-438`'s missing red card and shot counts |
| **Cricket control 32** — the conditional-activation gate, recorded as validated positive evidence | Preserve | `RULES_CRICKET.md` | `P-445` |
| **Basketball §9.5 update** — LNBP result lane (rendered club page) recorded; `BK-P1` unchanged and still `FAIL` | Source | `RULES_BASKETBALL.md` | `P-451` |

**No coefficient, ordinal bar, fitted weight or automatic market preference is promoted from this cohort** (`L-087`). Every item above is a printed-arithmetic, disclosure, measurement or retrieval requirement. In particular: **no "take +1.5" rule**, **no Coors Over rule**, **no AFC/UEFA Under bias**, and **no probability cap** — the last because 3 of the 4 high-band losses came from one card, which is an argument for `G-L21`, not for a cap.

### Updated running scorecard and queue

| Field | Before this import | After |
|---|---|---|
| Mixed running total | 425 rows, 242 W / 183 L, mean ≈ 0.2291 | **477 rows, 273 W / 204 L, mean ≈ 0.2270** |
| `PRIMARY_SCORED` | 104 rows, 55 W / 49 L, mean 0.2522; **25 cards** | **136 rows, 71 W / 65 L, mean ≈ 0.2468; 33 cards** |
| — MLB component | 68 rows, 0.2473 | **100 rows, ≈ 0.2415** |
| — EPL / NRL-AFL components | 20 rows 0.2267 / 16 rows 0.3053 | unchanged |
| `PRIMARY_SCORED` pattern review | first done at 25 | **next due at 50 — 33 of 50** |
| Next canonical ID | `P-438` | **`P-452`** |

**New `PRIMARY_SCORED` sub-line required by `G-L22`, reported from this cohort forward:** of the 136 `PRIMARY_SCORED` rows, the 32 added here are **all `FORCED_PAIR`** and represent **16 decisions, 10 correct**. Earlier cohorts were not labelled, so the retrospective split cannot be reconstructed; labelling starts here.

**Queue:** `TMP-OPEN-20260917-02` (`P-451` Jornada 20 final) was opened and retired inside this pass. No other handle changes. The open queue stays at **23 handles** — Part-3 custody 13, Part-4 custody 1 (`P-430-C05`), Part-2 custody 9 — plus 3 documentary audits. Nothing in this cohort is unsettled on a source rule.

### Mechanical completeness audit — `audit_card_controls.py` rebuilt and run

`RULES_GENERAL.md` §16.8 and `EXTERNAL_LOGGING_WORKFLOW.md` §"2026-09-11" both instruct the settlement pass to run `audit_card_controls.py` over the running log. **That file did not exist at the repository root** — it survives only inside the archived `audit_2026-09-12/before/` snapshot's prose. The §16.8 block has therefore been self-reported since 2026-09-11, which is precisely how four fresh `M15` instances reached this cohort unnoticed.

It has been rebuilt at the repository root, extended to the fields added today (**5a** shared-failure mass, **5b** forced-pair labelling, **10** settlement process record), and run. Two correctness properties matter for reading the output:

- **Issue-time fields are matched only against issue-time text.** Fields 1–9 are scoped to the card body *before* its settlement heading; field 10 only to the settlement text. Without this, a retrospective sentence such as "both top two lost to the same state" credits the card with having printed `P(¬R1 ∧ ¬R2)` beforehand, which is the opposite of the truth. The first run of the script made exactly that error on `P-438` and `P-444`.
- **Detection is deliberately generous**, so a PASS is weak evidence and a FAIL is strong evidence — the correct asymmetry for an execution audit. It detects *printed fields*, never analysis quality.

| Card | 1 | 2 | 3 | 4 | 5 | 5a | 5b | 6 | 7 | 8 | 9 | 10 | Missing BLOCKING |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| `P-438` | d | **N** | **N** | n | n | **N** | n | n | **N** | n | n | **N** | 2, 3, 5a, 7, 10 |
| `P-439` | d | **N** | **N** | n | n | **N** | n | n | **N** | n | n | **N** | 2, 3, 5a, 7, 10 |
| `P-440` | d | **N** | **N** | n | n | **N** | n | n | **N** | n | n | **N** | 2, 3, 5a, 7, 10 |
| `P-441` | d | Y | Y | n | Y | **N** | Y | Y | Y | n | n | **N** | 5a, 10 |
| `P-442` | d | Y | Y | n | n | **N** | n | Y | Y | n | n | **N** | 5a, 10 |
| `P-443` | d | Y | Y | n | n | **N** | n | Y | Y | Y | n | Y | 5a |
| `P-444` | d | Y | Y | n | n | **N** | n | Y | Y | n | n | Y | 5a |
| `P-445` | d | **N** | **N** | Y | n | **N** | Y | n | Y | n | n | Y | 2, 3, 5a |
| `P-446` | d | **N** | **N** | n | n | **N** | n | Y | Y | n | n | **N** | 2, 3, 5a, 10 |
| `P-447` | d | Y | Y | n | n | **N** | n | Y | Y | Y | Y | **N** | 5a, 10 |
| `P-448` | d | Y | Y | n | Y | **N** | n | Y | Y | n | Y | **N** | 5a, 10 |
| `P-449` | d | Y | Y | n | n | **N** | n | Y | Y | Y | n | **N** | 5a, 10 |
| `P-450` | d | Y | Y | n | n | **N** | n | Y | Y | n | Y | **N** | 5a, 10 |
| `P-451` | d | – | – | – | – | – | – | – | Y | – | Y | – | — |

`Y` printed · `d` declared document-wide · `n` missing, non-blocking · **`N`** missing, BLOCKING · `–` not applicable.

**Result: 13 of 14 cards are missing at least one BLOCKING field.** The field-level counts:

| Field | Class | Missing |
|---|---|---|
| **5a** shared-failure mass (`G-L17`, `G-L21`) | BLOCKING | **13 of 13 auditable cards** |
| 4 complement decomposition (`G-L9`) | defect | 12 / 14 |
| 5 `P(R1 ∧ R2)` coupling (`G-L10`) | defect | 11 / 14 |
| 5b `FORCED_PAIR`/`FREE` labelling (`G-L15`, `G-L22`) | defect | 11 / 14 |
| **10** process record + disruption facts (`G-L23`) | BLOCKING | 10 / 14 |
| 9 settlement route per row (`G-L14`) | defect | 10 / 14 |
| 8 `AGGREGATE_ONLY` / sampling noise | defect | 10 / 14 |
| **2** outcome-family masses (`G-L1`) | BLOCKING | 5 / 14 |
| **3** centre/width/normalised edge (`G-L8`) | BLOCKING | 5 / 14 |
| 6 representative Rank-#1 outcome | defect | 4 / 14 |
| **7** participant state (`G14.2`) | BLOCKING | 3 / 14 |

**This is the single most important number in the audit, and it is larger than the hand count.** By hand I identified two `G-L17` failures (`P-438`, `P-444`). The mechanical check finds the field missing on **every card that could be audited** — including `P-441`, the batch's best card. `G-L17` was promoted one day earlier, on 2026-09-17, from `P-427`; not one card in the next cohort executed it. That is the `M15` pattern in its purest form, and it is the reason §16.8 field 5a is now **card-blocking** rather than advisory, and the reason the script is back.

**A caution on reading rows `P-438`–`P-440`.** Their `N`s on fields 2, 3 and 7 are **not** evidence that those cards omitted the geometry. The mini log carried only a *Ranked picks* table for those three, with no card body — so their issue-time compliance is unauditable, not failed. The distinction is invisible in the output and produces opposite conclusions, which is why `EXTERNAL_LOGGING_WORKFLOW.md` now requires an imported mini log to carry the issued card body or mark the card `BODY_NOT_CARRIED`.

**Baseline comparison.** Run against the `P-424`–`P-437` mini log, **0 of 14** cards have any auditable issue-time text at all — that log is settlement blocks only. Its twelve apparent "missing everything" rows are an artefact of the log's structure, not a finding about those cards. Recorded in full at `EXTERNAL_LOGGING_WORKFLOW.md` §"2026-09-17(b)".

**What this does not license.** A completeness failure is a **process** defect, not a retroactive invalidation: every issued rank, probability and Brier value in this cohort stands exactly as issued. What it constrains is *interpretation* — a cohort in which the mandatory block was essentially never executed cannot be read as evidence about the method's quality, because the method as written was not the method that was run (`PERFORMANCE_ELIGIBILITY_POLICY.md` §"2026-09-17(b)").

---

### Second-pass implementation — making the findings operative

The findings above were recorded in this section and in the sport files on the first pass. A follow-up pass moved each one from *recorded* to *operative*, because a rule that lives only in a dated settlement section is the same failure mode the audit just measured.

| Finding | Where it is now enforced |
|---|---|
| Shared-failure mass (`G-L21`) | `RULES_GENERAL.md` **§16.3 item 8a** — the mandatory card checklist, blocking — and §16.8 field 5a; checked by `audit_card_controls.py` |
| Forced pairs are one decision (`G-L22`) | `METHOD.md` **§5 counting rule**, inlined into the operative scoring text; §16.3 item 8b; §16.8 field 5b; a new scorecard line in this file's snapshot |
| Result-versus-process (`G-L23`) | `UPCOMING_GAME_RESEARCH_GUIDE.md` **settlement protocol Step 4a**; §16.3 item 13; §16.8 field 10 |
| Handicap identity, generalised (**`G-L24`**, new) | `RULES_GENERAL.md` **§16.13(e)**; §16.3 item 8; instantiated in **all ten sport files** with each sport's own band status; bands in `BASE_RATES_REGISTER.md` §1 |
| Push-mass ceiling | `METHOD.md` §5 coherence rules; baseball control 35; `BASE_RATES_REGISTER.md` §3 |
| Venue base rate beside the line | `UPCOMING_GAME_RESEARCH_GUIDE.md` §19 checklist; baseball control 35 |
| Calibration tables mislead on correlated cards | `METHOD.md` §5 — report the **distinct-card count** beside the row count |
| Base rates scattered across sport files | New **[`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md)** — one maintained copy, with `n`, query, date and refresh cadence |
| §16.8 audit was self-reported | **`audit_card_controls.py`** rebuilt at the repository root; run at Step 6a of the settlement protocol |
| Mini logs that cannot be audited | `EXTERNAL_LOGGING_WORKFLOW.md` §"2026-09-17(b)" — carry the card body or mark `BODY_NOT_CARRIED` |

**`G-L24` is the one genuinely new rule of the second pass**, and it generalises the cohort's largest finding beyond baseball. The MLB defect — a favourite `−1.5` row asserted at 0.55–0.56 when the league's own margin geometry caps it near 0.53 — is an instance of a general error: *a handicap probability being read off a winner probability without passing through the competition's cushion band.* Every sport in this repository has that band; **only baseball's has ever been computed.** `BASE_RATES_REGISTER.md` §1 now records the other nine as `NOT_YET_DERIVED` with the query that would derive each, and `G-L24` makes an underived band fail closed: print `BAND_NOT_DERIVED` and decline Rank #1, rather than guessing the band and presenting the product as arithmetic.

---

### Final validation checklist for this import

| Check | Result |
|---|---|
| All 14 mini-log records processed | **Yes** — `P-438`–`P-451` |
| No completed event left unsettled | **Yes.** 12 graded, `P-445` `NO ACTION` (correctly), `P-451` `NOT GRADED` (nothing issued) and its final now recovered |
| No live event settled | **Yes** — none was live |
| Temporary-ID events included | **Yes** — no temp prediction IDs existed; the one derivative handle is recorded and retired |
| Rank-#1 failures given enhanced review | **Yes** — `P-438`, `P-442`, `P-444`, all three with the full table |
| Every pick has a win/loss explanation | **Yes** |
| Top-two reviewed | **Yes**, per card and in the cohort audit |
| Totals reviewed | **Yes**, by family and by failure mechanism |
| Line-ups, bench, coaching audited | **Yes** — 13-row table; 0/13 confirmed both sides |
| Source accuracy audited; new sources recorded | **Yes** — 10-row table; `afc.cup`, the MLB base-rate lane and the rendered LNBP lane added |
| Blind spots documented with disposition | **Yes** — 12 rows, each marked rule / execution / observation |
| Sport rules updated | **Yes** — baseball 34–37, soccer 40–41, cricket 32, basketball §9.5 |
| Cross-sport rules updated | **Yes** — `G-L21`–`G-L23` (§16.13) |
| Prediction log updated | **Yes** — this section, plus the controlling snapshot |
| Mini log archived | **Yes** — `archive/mini_logs/`, settled variant and raw upload |
| Remaining unsettled items tracked | **Yes** — 23 handles unchanged; none from this cohort |
| Performance eligibility | **Unchanged: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**; carve-out extended in `PERFORMANCE_ELIGIBILITY_POLICY.md` §"2026-09-17(b)" |
| Mechanical §16.8 audit run | **Yes** — `audit_card_controls.py` rebuilt at the repository root (it was missing entirely) and run over both mini logs; per-card table above |
| Findings made operative, not only recorded | **Yes** — §16.3 checklist items 8/8a/8b/13, `METHOD.md` §5 counting and coherence rules, settlement-protocol Steps 4a and 6a, `G-L24` in all ten sport files, new `BASE_RATES_REGISTER.md` |

---

## 2026-09-17 — `P-424`–`P-437` imported, settled, retrospected and audited (external mini log)

**LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** Method on every card: `MDS-2026.09.06-v4.0`. Issued text, ranks and probabilities are preserved exactly as issued; settlement and retrospective material is appended. Source file: `PREDICTION_MINI_RUNNING_LOG_P424_P437_FULL_SETTLEMENT_RETROSPECTIVE_2026-09-17.md` (211,510 bytes, SHA-256 `b0b11de0d6eaba61a6f89f6a5e60e44f4de15804ba651859bbe41bc548092839`), archived under `archive/mini_logs/`.

### Pre-update integrity check

| Check | Finding |
|---|---|
| Predictions in the mini log | 14 IDs, `P-424`–`P-437`, each used exactly once |
| Canonical position | Part 4 opened empty at `P-424`; the log begins exactly there |
| Duplicate IDs | **None** — no ID appears twice, and none collides with `P-001`–`P-423` |
| Duplicate events | **None.** `P-424` (Amsterdam v Dublin, ETPL M26) is a different fixture from `P-305` (Dublin v Amsterdam, 5 Sep) and `P-406` (Edinburgh v Amsterdam, M24); `P-428` (Edinburgh v Rotterdam, M27) is distinct from `P-406`. The five ACLE MD1 fixtures, the BCL qualifier, the two internationals and the four KBO games are all new events |
| Already in the combined log? | No; Part 4 held no cards before this import |
| Temporary IDs | One: `TMP-OPEN-20260917-01`, a derivative follow-up handle for `P-430-C05` only — **not** a prediction ID and not a canonical conflict |
| Event states | 13 complete; **1 partial** (`P-430`: final verified, one derivative row unresolved). None live, delayed, suspended, postponed, abandoned or cancelled |
| Next canonical ID | **`P-438`** |

### Independent verification of the finals (`G-L13` — raw records, not the log's own narrative)

| Card(s) | Verified at | Result |
|---|---|---|
| `P-424`, `P-428` | ESPN cricket API, ETPL series 1547871 (events 1547897, 1547898) | **Confirmed exactly**, including both powerplay matchnotes: Amsterdam 214/5 with **0.1–6.0 = 48/2**; Rotterdam 181/6 with **54/2**. Toss notes confirm Dublin fielded and Rotterdam batted |
| `P-425`, `P-426`, `P-430`, `P-436`, `P-437` | ESPN `soccer/afc.champions` (events 401912672, 401912671, 401912656, 401912670, 401912654) | **All five finals confirmed.** Corner fields also confirmed: Daejeon 4–3 Kyoto; Gamba 1–3 CAHN; **Al Ain 2–10 Al Nassr**; Kashiwa 6–0 Jeonbuk; Port 4–4 Vissel. Goal minutes match every card |
| `P-427` | Not independently re-verified this pass | Carried from the log's cited Kolossos official report, SDNA and Eurohoops |
| `P-429`, `P-431` | Not independently re-verified this pass | Carried from the log's cited ICC / Reuters / ABC / NDTV records |
| `P-432`–`P-435` (KBO) | **Route failure — not independently re-verified** | KBO English scoreboard returned 174 bytes; `r.jina.ai` proxy 385; mykbostats and Naver are JS-only. Finals carried from the log's cited Korean reports (fnnews, SPOTV, SportsChosun, OSEN, Nate). Logged as a lane degradation in `SOURCES.md` §"2026-09-17" |

**`G-L14` note.** ESPN is a data partner, not the pre-registered settlement route for these cards. Where it confirms a field it is recorded as corroboration; it does not convert `P-430-C05` into a booked row.

---

### `P-424` — Amsterdam Flames v Dublin Guardians, ETPL Match 26 — ADMINISTRATIVE CLOSURE

**Disposition:** `FINAL / ADMINISTRATIVELY CLOSED — NO ISSUED FORECAST / NO SCORED TRIAL`. The scheduled start crossed during research and no field owner established a verified live or zero-play state, so the card fail-closed. Two supplied contracts were frozen but **never issued**: no rank, probability, winner or direction.

**Official final:** Amsterdam 214/5 (20) beat Dublin 155/9 by 59 runs; Amsterdam powerplay 48/2 (verified this pass).

| Frozen supplied contract | Realised | Grade |
|---|---|---|
| Amsterdam batting-first 20-over O/U 170.5 | Over (214/5) | `NOT GRADED` — nothing was issued |
| Amsterdam first 6 completed overs O/U 50.5 | Under (48/2) | `NOT GRADED` |

The pre-fail-close research note favoured **Under 170.5** and would have lost. It was explicitly labelled *not an issued forecast*, so it stays out of every W/L, Brier, Rank-#1 and winner count. **What went right:** the fail-close was correct and on this occasion also avoided booking a losing direction. **Learning:** confirms `L-009`/`L-039` — 48/2 after six became 214/5, so phase runs alone do not bound an innings; the phase-end *resource* state is what carries.

---

### `P-425` — Daejeon Hana Citizen 1–0 Kyoto Sanga (ACLE MD1)

**Settled from:** AFC official report; corners from the J.LEAGUE ACLE match-data route and Kyoto's club record (CK 3). **Verified here at ESPN:** 1–0, corners 4–3, Daejeon 17 shots to Kyoto's 1, Bobsin 78'.

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Daejeon team total Over 0.5 | 0.76 | **WIN** | 0.0576 |
| 2 | Match total Over 1.5 | 0.73 | **LOSS** | 0.5329 |
| 3 | Daejeon +0.5 / 1X | 0.70 | **WIN** | 0.0900 |
| 4 | Match Over 2.5 | 0.57 | **LOSS** | 0.3249 |
| 5 | Daejeon team corners Over 3.5 | 0.55 | **WIN** | 0.2025 |

**Winner:** Daejeon — WIN. **Card Brier 0.2416.** Rank #1 WIN · Hit@2 YES · Wins@2 1/2. Supplied 1H Over 0.5 LOSS; supplied full Over 2.5 LOSS.

**Why:** Daejeon dominated (17 shots to 1) but converted once, late. Both match-total Overs needed *Kyoto* to contribute, and Kyoto produced a single shot all match. The team-total row needed only Daejeon. **Blind spot:** the total's opponent-contribution branch was under-massed. **Confirms `L-037`**, and with `P-430` and `P-433` forms the strongest recurring pattern of this batch.

---

### `P-426` — Gamba Osaka 4–1 Cong An Ha Noi (ACLE MD1)

**Settled from:** AFC official report, Gamba club report, J.LEAGUE ACLE match data. **Verified here at ESPN:** 4–1, HT 1–0, corners Gamba 1 / CAHN 3, goals 29', 58', 67', 79', 90+3'.

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | 1st Half Under 1.5 | 0.77 | **WIN** | 0.0529 |
| 2 | Cong An Ha Noi +1.5 | 0.75 | **LOSS** | 0.5625 |
| 3 | Full Match Under 3.5 | 0.74 | **LOSS** | 0.5476 |
| 4 | Gamba team corners Over 2.5 | 0.63 | **LOSS** | 0.3969 |
| 5 | Full Match Under 2.5 | 0.59 | **LOSS** | 0.3481 |

**Winner:** Gamba — WIN. **Card Brier 0.3816** (worst of the batch). Rank #1 WIN · Hit@2 YES · Wins@2 1/2.

**Why:** the contained first half was correctly forecast, then Gamba's class separated after the break (three goals from 58'). CAHN's four straight clean sheets came against materially weaker domestic and preliminary opposition and did not transfer. **Gamba scored four goals from one corner** — the clearest corners-are-not-a-dominance-proxy case since `P-402`. **Blind spot:** cross-league defensive translation, which then killed three rows at once (R2, R3 and R5 all needed the same low-separation state). → soccer control 39 and `G-L17`.

---

### `P-427` — Biotekno Körfez 91–79 Kolossos H Hotels (BCL qualification) — **Rank #1 LOSS**

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Kolossos +2.5 | 0.61 | **LOSS** | 0.3721 |
| 2 | Under 162.5 | 0.58 | **LOSS** | 0.3364 |
| 3 | Over 162.5 | 0.42 | **WIN** | 0.3364 |
| 4 | Biotekno Körfez −2.5 | 0.39 | **WIN** | 0.3721 |

**Winner:** Kolossos — LOSS. **Card Brier 0.3542.** Rank #1 LOSS · **Hit@2 NO** · Wins@2 0/2 — the only card in the batch where both top rows failed. Regulation total 170; no overtime.

**Deep Rank-#1 review**

| Question | Finding |
|---|---|
| Why it was ranked first | Kolossos' steadier preparation form (78-78, 82-80, 89-80) against Körfez's swings, a neutral venue, and the +2.5 cushion judged more robust than a coin-flip winner label |
| Was the evidence genuinely supportive? | Partly. The central thesis was not fabricated — Kolossos led 70–66 after three quarters. The error was the size of the late-separation tail, not the centre |
| Should another row have ranked higher? | Not on pregame evidence. Promoting the 42% Over or the 39% −2.5 now would be hindsight |
| Failure class | **Poor weighting of a shared tail** — not missing information, weak sources or bad data. Körfez shot 12/24 from three and won Q4 25–9 |
| Existing rule that applied | `RULES_BASKETBALL` already requires late-game, closing-lineup and foul/bonus branches; `G-L10` already requires a coupling label. Both were *stated*; neither was *quantified as a joint failure* |
| Rule gap | `G-L10` prints `P(R1 ∧ R2)` — the probability both **win**. Nothing required `P(¬R1 ∧ ¬R2)`, the mass that actually governs top-two reliability. → new **`G-L17`** |

**Why each row:** a four-point lead after Q3 became a 12-point loss (R1); the 52-point fourth quarter lifted the game to 170 (R2 lost, R3 won); the 25–9 period gave clean separation (R4 won). **What went right:** the card called the winner a coin flip rather than overstating Kolossos, and it did flag the coupling.

---

### `P-428` — Edinburgh Castle Rockers v Rotterdam Dockers, ETPL Match 27 — ADMINISTRATIVE CLOSURE

**Disposition:** `FINAL / ADMINISTRATIVELY CLOSED — NO ISSUED FORECAST / NO SCORED TRIAL`. Same start-crossing gate as `P-424`; both supplied contracts were activation-conditional on Rotterdam batting first and were never issued.

**Official final (verified this pass):** Rotterdam 181/6 beat Edinburgh 176/5 by 5 runs; Rotterdam batted first; powerplay 54/2.

| Frozen supplied contract | Realised | Grade |
|---|---|---|
| Dockers 20-over first-innings O/U 168.5 | Over (181/6) | `NOT GRADED` |
| Dockers first 6 overs O/U 47.5 | Over (54/2) | `NOT GRADED` |

The research-only **Under 168.5** direction would also have lost. **What went right:** the fail-close again prevented a post-start pseudo-pregame card. **Learning:** sparse venue medians do not cap a team-specific upper tail.

---

### `P-429` — Afghanistan 159/8 lost to India 163/3 (2nd T20I, Delhi)

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Afghanistan lose 1+ wicket in first 6 overs | 0.79 | **WIN** | 0.0441 |
| 2 | Arshdeep Singh 1+ wicket | 0.66 | **WIN** | 0.1156 |
| 3 | Afghanistan first 6 overs Under 47.5 | 0.55 | **WIN** | 0.2025 |
| 4 | Afghanistan 20-over innings Over 167.5 | 0.54 | **LOSS** | 0.2916 |

**Winner:** India — WIN. **Card Brier 0.1635.** Rank #1 WIN · Hit@2 YES · **Wins@2 2/2.** Afghanistan powerplay 41/1; Arshdeep 2 wickets.

**Why:** the card used *same-opponent, same-venue, unchanged-top-order* evidence (41/4 against this attack two days earlier) for the early-wicket rows rather than generic batting-first totals — the strongest single piece of reasoning in the batch. The innings Over failed because India squeezed overs 7–15 (64 runs, 5 wickets; Nitish Kumar Reddy 3/24). **Blind spot:** Varun Chakaravarthy's absence was treated as a simple scoring-ceiling positive instead of an `outgoing role → incoming bowler → residual attack` chain (`L-006`). → cricket control 31. **Line-ups: both XIs confirmed** — the only card in the batch where that is true.

---

### `P-430` — Al Ain 4–0 Al Nassr (ACLE MD1) — **Rank #1 LOSS; one row still open**

**Verified here at ESPN:** 4–0, HT 1–0, goals 25', 63', 72', 85'; corners **Al Ain 2, Al Nassr 10**.

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Al Nassr team total Over 0.5 | 0.85 | **LOSS** | 0.7225 |
| 2 | Match Over 1.5 | 0.81 | **WIN** | 0.0361 |
| 3 | 1st Half Over 0.5 | 0.75 | **WIN** | 0.0625 |
| 4 | Al Nassr +0.5 / X2 | 0.75 | **LOSS** | 0.5625 |
| 5 | Al Ain team corners Over 3.5 | 0.70 | **UNRESOLVED** | not booked |

**Winner:** Al Nassr — LOSS. **Four-row Brier 0.3459** (not a final card mean while R5 is open). Rank #1 LOSS · Hit@2 YES · Wins@2 1/2. Supplied 1H Over 0.5 and full Over 2.5 both WIN.

**`P-430-C05` stays open (`TMP-OPEN-20260917-01`).** The card pre-registered the AFC official match-stat record; the reachable AFC report carries the score but not the corner field. ESPN and two secondary displays agree on **Al Ain 2** — a research LOSS — but ESPN was not pre-registered, so under §16.10(j) the row is not booked. This is the correct outcome-independent application: the evidence points to a loss and the row still is not silently promoted.

**Deep Rank-#1 review**

| Question | Finding |
|---|---|
| Why it was ranked first | One Al Nassr goal was judged less demanding than a match total or side result, with Ronaldo/Félix/Mané/Ângelo in the latest confirmed attacking core and Al Nassr scoring in all five recent league matches |
| Was 85% justified? | **No.** The mechanism was credible but the number was too assertive for `MEDIUM` evidence with **no official XI or bench**. Al Nassr had 15 shots and 10 corners and still did not score |
| Should another row have ranked higher? | R2 (Match Over 1.5) had a genuinely two-sided path and won. The pregame gap between R1 (85%) and R2 (81%) was too wide given R1 depended on one specific team scoring |
| Failure class | **Probability extremity under unresolved participant state** — over-conversion of a class prior into near-certainty, not missing availability data |
| Existing rule | `G14.2` / `SO-P2` cap participant-sensitive rows; the cap was applied to *rank* (R2 was blocked from #1) but not to *probability extremity* |
| Disposition | Evidence row for `C-PROB-EXTREMITY`; **no** automatic cap (the ≥0.70 band went 22/27 across this batch, so a blanket cap is unsupported). New soccer control 37 instead |

**Over/under lesson:** the full-match Over won **entirely through Al Ain's four goals** while the Rank-#1 Al Nassr scoring thesis failed. A correct total does not validate the allocation that produced it.

---

### `P-431` — England 254/4 beat Sri Lanka 135 by 119 runs (1st T20I, Southampton)

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | England first innings Over 149.5 | 0.84 | **WIN** | 0.0256 |
| 2 | Adil Rashid 1+ wicket | 0.76 | **WIN** | 0.0576 |
| 3 | England first 6 overs Under 60.5 | 0.62 | **LOSS** | 0.3844 |
| 4 | England first innings Under 193.5 | 0.55 | **LOSS** | 0.3025 |

**Winner:** England — WIN. **Card Brier 0.1925.** Rank #1 WIN · Hit@2 YES · **Wins@2 2/2.** England powerplay 90/1; Rashid 1 wicket.

**Why:** the low alternate Over and the opponent-specific wicket role both held, through different mechanisms. Both Unders lost to a right tail **the card had already documented**: England made 257/3 at the same venue in July, and still the card placed 55% on Under 193.5 and 62% on the powerplay Under. Brook 114*, Buttler 80, a 128-run second-wicket stand. **This is the same failure class as `P-411`** (basketball, where a same-competition 83–53 meeting was set aside) — a directly comparable current-regime performance that already cleared the line was not given explicit mass. → cricket control 30 and cross-sport `G-L18`.

**Contract identity note preserved:** if an operator ticket literally named Afghanistan for these England first-innings lines, that ticket is void rather than an England contract.

---

### `P-432` — KT Wiz 4–4 Hanwha Eagles (KBO; tied after 11 innings)

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | KT Wiz +1.5 | 0.68 | **WIN** | 0.1024 |
| 2 | Under 9.5 | 0.55 | **WIN** | 0.2025 |
| 3 | Over 9.5 | 0.45 | **LOSS** | 0.2025 |
| 4 | Hanwha −1.5 | 0.32 | **LOSS** | 0.1024 |

**Winner:** KT — **did not realise; the game was a tie.** **Card Brier 0.1525.** Rank #1 WIN · Hit@2 YES · **Wins@2 2/2.**

**The finding of this card is an ontology defect, not a forecasting error.** The winner family was issued as KT 55% / Hanwha 45%, summing to 100% — but this competition can end in a **terminal tie** after its capped extra innings, and it did. A two-outcome family on a three-outcome competition is structurally invalid regardless of which side is favoured. The handicap and total rows were unaffected (both won), which is exactly why this surfaced as a labelling defect rather than a scoring one. → new baseball control 32 and cross-sport **`G-L19`**.

---

### `P-433` — LG Twins 9–2 NC Dinos (KBO)

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | LG Twins +1.5 | 0.68 | **WIN** | 0.1024 |
| 2 | LG team total Over 3.5 | 0.65 | **WIN** | 0.1225 |
| 3 | NC team total Over 3.5 | 0.63 | **LOSS** | 0.3969 |
| 4 | Combined Over 10.5 | 0.57 | **WIN** | 0.1849 |

**Winner:** LG — WIN. **Card Brier 0.2017.** Rank #1 WIN · Hit@2 YES · **Wins@2 2/2.**

**Why:** the sport-native, current-regime mechanism — Clevinger's manager-stated 50–60 pitch cap on a KBO debut, forcing early middle-relief exposure — drove LG's scoring and the combined Over. It was not a generic "debut" narrative. The combined Over won with **LG supplying nine of the eleven runs**, while the NC team-total Over lost: a third allocation case in one batch. → `G-L18`.

---

### `P-434` — Doosan Bears 3–1 Samsung Lions (KBO) — all four rows won

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Chris Paddack 3+ strikeouts | 0.87 | **WIN** | 0.0169 |
| 2 | Under 10.5 runs | 0.75 | **WIN** | 0.0625 |
| 3 | Doosan +2.5 | 0.74 | **WIN** | 0.0676 |
| 4 | Under 8.5 runs | 0.58 | **WIN** | 0.1764 |

**Winner:** Samsung — LOSS. **Card Brier 0.0809.** Rank #1 WIN · Hit@2 YES · **Wins@2 2/2.** Paddack struck out 6.

**Why:** a strikeout floor with a genuinely stable exposure base (3+ K in all nine KBO starts, 59 K in 55⅓ IP) plus a wide Under and a protected handicap. Every ranked row won while the 54% winner label lost — the clearest demonstration in the batch that **contract selection, not winner identification, is where these cards earn their score**.

---

### `P-435` — SSG Landers 4–1 Lotte Giants (KBO) — all four rows won

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Pedro Avila 4+ strikeouts | 0.88 | **WIN** | 0.0144 |
| 2 | SSG +1.5 | 0.75 | **WIN** | 0.0625 |
| 3 | Lotte team total Under 4.5 | 0.72 | **WIN** | 0.0784 |
| 4 | SSG team total Over 3.5 | 0.69 | **WIN** | 0.0961 |

**Winner:** SSG — WIN. **Card Brier 0.0629** (best of the batch). Rank #1 WIN · Hit@2 YES · **Wins@2 2/2.** Avila: 7 IP, 11 K, 1 R.

**Why:** the same structure as `P-434` — an established strikeout floor (4+ K in all ten KBO starts, 6 K in each of two starts against Lotte) with direct opponent evidence, plus team totals resolved from each side's own marginal rather than a single game total. A low total again coexisted with a three-run margin (`SSG 4–1`), consistent with the standing baseball rule that low totals do not imply close margins.

---

### `P-436` — Jeonbuk 2–1 Kashiwa Reysol (ACLE MD1) — all five rows won

**Verified here at ESPN:** 2–1, HT 0–1 (Yuba 30'), corners Kashiwa 6 / Jeonbuk 0.

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Match Under 4.5 | 0.90 | **WIN** | 0.0100 |
| 2 | Kashiwa +1.5 | 0.84 | **WIN** | 0.0256 |
| 3 | 1st Half Under 1.5 | 0.73 | **WIN** | 0.0729 |
| 4 | Kashiwa team total Over 0.5 | 0.72 | **WIN** | 0.0784 |
| 5 | Kashiwa team corners Over 3.5 | 0.68 | **WIN** | 0.1024 |

**Winner:** Kashiwa — LOSS. **Card Brier 0.0579.** Rank #1 WIN · Hit@2 YES · **Wins@2 2/2.** Supplied full-match Under 2.5 LOSS at three goals.

**Why:** the card took the **wide** total (Under 4.5, against a 2.4–2.5 centre) rather than the knife-edge supplied Under 2.5, and the protected side rather than the plurality winner. The match landed at three goals: the wide Under won, the narrow Under lost by one goal, and the winner label failed — while all five ranked rows survived. This is the batch's cleanest illustration of line geometry.

---

### `P-437` — Port FC 1–2 Vissel Kobe (ACLE MD1) — all five rows won

**Verified here at ESPN:** 1–2, HT 1–1 (Komatsu 10', own goal 45+4', Muto 61'), corners 4–4.

| Rank | Contract | `p` | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Match Under 4.5 | 0.86 | **WIN** | 0.0196 |
| 2 | Vissel Kobe +1.5 | 0.84 | **WIN** | 0.0256 |
| 3 | Vissel team total Over 0.5 | 0.81 | **WIN** | 0.0361 |
| 4 | Match Over 1.5 | 0.78 | **WIN** | 0.0484 |
| 5 | 1st Half Over 0.5 | 0.70 | **WIN** | 0.0900 |

**Winner:** Vissel — WIN. **Card Brier 0.0439** (lowest of the batch). Rank #1 WIN · Hit@2 YES · **Wins@2 2/2.** Both supplied totals won. Unranked Port corners Over 3.5 also realised but is excluded from scoring.

**Why:** the three-goal result sat inside a deliberately wide 2–4 corridor, so **Over 1.5 and Under 4.5 both won** — not a contradiction but an overlap interval, and the card said so in advance. Weather was treated as distribution width rather than an automatic Under sign, which is the behaviour `G-L2` asks for.

---

### Cohort audit — the twelve cards that issued ranked probabilities

`P-424` and `P-428` issued nothing and are excluded from every metric below.

| Measure | Value |
|---|---|
| Graded ranked rows | **52** (36 W / 16 L); `P-430-C05` unresolved and excluded |
| Mean Brier | **0.1892** against 0.25 for the 0.5 baseline. **All 52 rows recomputed from probability and result — 52 of 52 reproduce**, and every card mean reproduces |
| Rank #1 | **10 W / 2 L** (losses: `P-427`, `P-430`) |
| Hit@2 (at least one of the top two) | **11 / 12** (only `P-427` failed) |
| Both top two won | **8 / 12** |
| Top-two slots | **19 W / 24** |
| Potential winners | **7 / 12** (`P-432` was a tie, so the label did not realise) |
| Highest-ranked total per card | **10 / 12** |
| Population | **All twelve are `EXPLORATORY`** — no MLB, EPL, NRL or AFL card. The `PRIMARY_SCORED` count stays at 25 and its 0.2522 is unchanged |

**Why the Brier is so much better than the previous cohort's (0.2276):** it is mostly *contract selection*, not better forecasting of events. Nine of the twelve cards put a wide alternate line, a low-threshold team total, a protected handicap or a player-prop floor at Rank #1. The two losing Rank #1s were the two cards that put a *specific team's* scoring (`P-430`) or a *close-game margin* (`P-427`) first. The sample is twelve cards in five sports and proves nothing on its own.

### Over/under review (the standing directive)

| Family | Record this batch |
|---|---|
| Wide alternate totals far from the centre (U4.5 at a 2.4 centre, U10.5, O149.5) | **4 / 4** |
| Low-threshold team totals (team O0.5 / opponent U1.5 / team U4.5) | **6 / 7** |
| Phase totals (1H U1.5, 1H O0.5, powerplay U47.5) | **4 / 5** |
| Near-centre supplied main lines (U2.5, O2.5, O/U 9.5, O10.5, U8.5, O/U 162.5, O167.5) | **6 / 13** |

This is the **first prospective evidence for `C-OU-GEOMETRY`**, the manifest opened on 2026-09-16 from `P-345`–`P-423`. That manifest predicted exactly this split — free, low-count-tail rows outperforming near-centre preferred sides — and an independently generated batch reproduced it (10 of 12 highest-ranked totals won). It is now **2 cohorts consistent**; the manifest requires 50 cards before any promotion, and no ordinal bar follows.

**Allocation is the recurring totals error.** Three separate cards (`P-425`, `P-430`, `P-433`) had a match/game total whose thesis rested on one side, and in each the *allocation* failed even when the total direction was right or wrong for the wrong reason. → `G-L18`.

### Line-up, bench and availability audit

| Card | Starters | Bench / reserves | Coaches | Availability |
|---|---|---|---|---|
| `P-429` | **Both XIs confirmed** | Squad context adequate | Not material | Yes — Varun out, Bishnoi in |
| `P-431` | England XI confirmed; Sri Lanka not | Partial | Not material | Yes, both sides' key absences |
| `P-425`, `P-426`, `P-430`, `P-436`, `P-437` | **No** confirmed XIs | **No** full benches | Yes on all five | Partial |
| `P-427` | No confirmed fives | Rosters only | Yes | Partial (Harris/Upson minutes) |
| `P-432`–`P-435` | Posted orders not fully retrieved | Bullpen partial | Manager pitch-cap obtained on `P-433` | Yes |

**Answer to the standing question: confirmed starters *and* bench for both sides were obtained on 0 of 12 cards; only `P-429` had both XIs.** Notably, the two Rank-#1 losses were **not** caused by a missing name — `P-430` failed on probability extremity and `P-427` on tail weighting. The participant gap remains a real process defect but was not the proximate cause of any loss in this batch.

### Source audit

| Source | Verdict |
|---|---|
| ESPN cricket API (ETPL powerplay matchnotes) | **Accurate and decisive** — reproduced both powerplay figures exactly. Keep as the phase-settlement route (cricket control 29) |
| ESPN `soccer/afc.champions` | **New verified lane** — finals, corners, goal minutes for all five ACLE fixtures. Corroboration tier; pre-register it on the card to make it a settling route |
| J.LEAGUE ACLE match data / club records | **Accurate** — settled corners for the Japanese-club fixtures; AFC's own report settles the score but **not** corners |
| AFC official reports | Accurate for score and narrative; **no corner field** — the direct cause of `P-430-C05` remaining open |
| Cricket Ireland / CricketArchive | Strong ETPL settlement route |
| KBO English scoreboard | **Degraded** — 174 bytes direct, 385 via proxy; mykbostats and Naver JS-only. Korean on-site reports carried the finals instead |
| Betting/tipster/preview pages | Correctly excluded throughout; `P-424`'s pitch-report ladder failed closed rather than using them |

### Blind-spot audit

| Blind spot | Was it available pre-game? | How much it mattered | Mitigation | Formal change? |
|---|---|---|---|---|
| Coupled top-two rows share a single losing state (`P-427`; also `P-426` R2/R3/R5) | Yes — the coupling was named on the card; the joint *failure* mass was never computed | Decisive: the only Hit@2 failure in the batch | Print `P(¬R1 ∧ ¬R2)` and name the state | **Yes — `G-L17`** |
| Total driven by one side's attack (`P-425`, `P-430`, `P-433`) | Yes — each card had both sides' scoring records | Cost three rows directly and produced two "right total, wrong reason" wins | Print each side's marginal and the opponent-contribution branch | **Yes — `G-L18`** |
| Competition permits a terminal tie (`P-432`) | Yes — a KBO rule, not a surprise | The winner family was structurally invalid, though the graded rows were unaffected | Build the complete discrete end-state family before any winner label | **Yes — `G-L19`** |
| Direct same-venue current-regime ceiling ignored (`P-431`; mirrors `P-411`) | Yes — the 257/3 comparable was *on the card* | Killed both Unders | Give the comparable explicit mass; an upper Under above it needs a named mechanism | **Yes — `G-L20`** |
| Probability extremity with no confirmed XI (`P-430` R1 at 0.85) | Participant state was known to be unresolved | Largest single Brier in the batch (0.7225) | Print opponent-suppression and finishing-failure branches for single-team scoring rows above 0.80 | Soccer control 37; no blanket cap |
| Cross-league defensive translation (`P-426`) | Yes — CAHN's clean sheets came against weaker opposition | Three rows | Widen the favourite-separation tail when the underdog's sample is from a weaker pool | Soccer control 39 |
| Replacement treated as a one-sign adjustment (`P-429`) | Yes — the replacement was named in the XI | One row | `outgoing role → incoming role → residual unit` | Cricket control 31 |
| Confirmed XIs / benches missing on 11 of 12 cards | Mostly yes, near kickoff | Not the proximate cause of any loss this batch | Existing `G14.2` retrieval requirement stands | Observation; no new rule |

### Comparison against previous lessons

| Observation | Seen before? | Rule already existed? | Was it followed? | Disposition |
|---|---|---|---|---|
| Corners are not a dominance proxy (`P-426` 4 goals / 1 corner; `P-430` 4 goals / 2 corners) | Yes — `P-402`, `P-408`, `P-419` | Soccer controls 4, 21, 33, 34 | Yes, and the corner rows were still ranked low or capped | Confirms existing controls; no change |
| One-sided allocation (`L-037`) | Yes — `P-404`, `P-417` | `L-037` exists as a principle | **Not executed as arithmetic** | Escalated to `G-L18` after three recurrences in one batch |
| Coupled top two failing together | Yes — `P-413`, `P-414`, `P-397` | `G-L10` (coupling label + joint win) | Label printed; joint failure never quantified | Escalated to `G-L17` (4th+ recurrence, 3 sports) |
| Direct comparable discarded | Yes — `P-411` (basketball control 25) | Control 25 is basketball-only | Not generalised to cricket | Escalated to cross-sport `G-L20` |
| Phase and innings are separate targets | Yes — `P-379`, `P-395`, `P-400`, `P-406` | Cricket controls 16, 19, 29 | Yes | `P-424` (48/2 → 214/5) is a clean confirming example |
| Fail-close on start-crossing | Yes — `P-389`, `P-415` | `RULES_GENERAL` start-crossing gate | **Yes, twice** (`P-424`, `P-428`) | Working as designed — preserve |
| `C-PROB-EXTREMITY` (p ≥ 0.70 overconfidence) | Under test since 2026-09-11 | Manifest only | — | **Not supported.** This batch: 22 W / 27 at a mean stated ≈ 0.79. Combined with earlier cohorts, 54 / 69 ≈ 78% against ≈ 0.77 stated. Keep TESTING; no cap |

### What went right — preserve these

1. **Contract geometry.** Wide alternates, low-threshold team totals, protected handicaps and exposure-backed player props carried the batch: `P-434`, `P-435`, `P-436` and `P-437` won **18 of 18** ranked rows between them.
2. **Player-prop floors with a real exposure base.** `P-434` (3+ K in all nine KBO starts) and `P-435` (4+ K in all ten, 6 K in each of two starts against this opponent) are the model to copy — a rate floor plus direct opponent evidence plus a named exit-risk branch.
3. **Same-opponent, same-venue, unchanged-personnel evidence** (`P-429`) beat generic form.
4. **Sport-native current-regime mechanisms** (`P-433`'s manager-stated 50–60 pitch cap) beat narrative.
5. **Weather as width, not sign** (`P-437`), exactly as `G-L2` requires.
6. **Outcome-independent settlement discipline** (`P-430-C05` left open although the evidence points to a loss).
7. **Two correct fail-closes** (`P-424`, `P-428`), both of which would have booked a losing research direction.

### Rule and algorithm changes made in this pass

| Change | Type | Evidence | Home |
|---|---|---|---|
| **`G-L17`** — for any two ranked rows sharing a driver, print `P(¬R1 ∧ ¬R2)` and name the single state that produces it | Cross-sport disclosure | `P-427`, `P-426`; recurrence of `P-397`, `P-413`, `P-414` | `RULES_GENERAL.md` §16.12(a); basketball control 26 |
| **`G-L18`** — allocation marginals for every multi-participant total | Cross-sport disclosure | `P-425`, `P-430`, `P-433`; `L-037` | §16.12(b) |
| **`G-L19`** — complete competition end-state family before any winner label (ties, draws, shoot-outs, capped extras) | Cross-sport integrity | `P-432` | §16.12(c); baseball control 32 |
| **`G-L20`** — a direct comparable that already cleared the line gets explicit mass | Cross-sport disclosure | `P-431`; mirrors `P-411` | §16.12(d); cricket control 30 |
| Soccer control 37 — single-team scoring row above 0.80 without a confirmed XI | Sport disclosure | `P-430` | `RULES_SOCCER.md` |
| Soccer control 38 — AFC/ACLE settlement routes added to the control 35 table | Sport process | `P-425`, `P-430`, `P-436` | `RULES_SOCCER.md` |
| Soccer control 39 — cross-league defensive translation widens the separation tail | Sport disclosure | `P-426` | `RULES_SOCCER.md` |
| Cricket control 30 — same-venue current-regime ceiling | Sport disclosure | `P-431` | `RULES_CRICKET.md` |
| Cricket control 31 — bowling replacement chain | Sport disclosure | `P-429` | `RULES_CRICKET.md` |
| Baseball control 32 — terminal-tie end-state | Sport integrity | `P-432` | `RULES_BASEBALL.md` |
| Baseball control 33 — strikeout-floor prop gate (positive model) | Sport disclosure | `P-434`, `P-435` | `RULES_BASEBALL.md` |
| Basketball control 26 — shared late-game kill state | Sport disclosure | `P-427` | `RULES_BASKETBALL.md` |

None of these is a fitted weight, an ordinal bar or a calibration claim (`L-087`). Each is a disclosure, retrieval or integrity requirement.

### Updated running scorecard and queue

| Measure | Before | After this import |
|---|---|---|
| Mixed running scorecard | 373 rows, 206 W / 167 L, ≈ 0.2346 | **425 rows, 242 W / 183 L, ≈ 0.2291** |
| `PRIMARY_SCORED` | 104 rows, 0.2522, 25 cards | **Unchanged** — all twelve scored cards are `EXPLORATORY`; next review still at 50 cards |
| Canonical IDs | `P-001`–`P-423` | **`P-001`–`P-437`**; next ID **`P-438`** |
| Open handles | 22 primary + 3 documentary audits | **23 primary** (`TMP-OPEN-20260917-01` added, Part 4 custody) + 3 documentary audits |

### Final validation checklist for this import

- All 14 mini-log entries processed; 12 scored, 2 administratively closed.
- No completed event left unsettled, and no live event settled: `P-430-C05` is the only open row and it is open on a **source rule**, not an event-state question.
- The one temporary ID (`TMP-OPEN-20260917-01`) is recorded, with Part 4 holding custody.
- Both Rank-#1 failures (`P-427`, `P-430`) received enhanced reviews.
- Every ranked row has a win/loss explanation; top-two and totals reviewed separately.
- Line-up, bench, coaching and availability audited per card; the 0-of-12 result is recorded rather than smoothed over.
- Sources audited; one new verified lane (ESPN `afc.champions`) and one degradation (KBO English scoreboard) recorded.
- Mini log archived byte-exact plus a reconciled copy.


## 2026-09-16 — settlement and learning pass (no card issued)

**LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** Method unchanged (`MDS-2026.09.06-v4.0`). No event was live. Next ID remains **`P-424`**. Full evidence: [Part 3 §"2026-09-16"](PREDICTION_LOG_COMBINED_3.md); settled rows whose parent card sits in a closed part are recorded in **Appendix A** below, per the user direction of 2026-09-16.

### General learnings (cross-sport; full text in `RULES_GENERAL.md` §16.11)

1. **`G-L13` — a model-summarised retrieval is not a record.** A WebFetch summary reported official Bundesliga corners ("7–7") that the page does not contain; the raw page holds only zero placeholders and the direct route returns HTTP 403. A BBS article was summarised with a September date when its raw `Published Time` is 2026-07-12. Confirm every number, date and name in raw text or JSON.
2. **`G-L14` — settlement-route execution.** Print the settling record and its verified status on every derivative or phase row at issue, and consult `DATA_SOURCE_REGISTER.md` before declaring a row unresolvable. `P-406` closed in one request after two passes had left it open; four of the five documentary-audit corner rows became reproducible the same way.
3. **`G-L15` — over/under geometry.** Forced Over/Under pairs win exactly once by construction, so report the preferred side (27 of 45) rather than "at least one won". Free low-threshold team and phase rows went 27 of 35.
4. **`G-L16` — period scope (new this pass).** UEFA's team-statistics feed reports whole-match totals, including extra time (`played_time` 137 and 115 on the two Women's Champions League ties). A 90-minute, regulation or phase contract cannot be settled exactly from a whole-match feed; settle with an explicit bound and mark `PERIOD_SCOPE_BOUNDED`.
5. **Disruption facts at settlement** — `P-408`'s red card (53', with Brighton 2–0 up) and `P-419`'s three red cards were missing from the canonical settlement.
6. **External variants** — fingerprint every drop location each session; never renumber canonical handles; verify each external narrative fact at a field owner (C′ was right about P-418 and wrong about P-421).
7. **Correction** — `P-418`'s "identity conflict" rested on a broadcaster report dated 2026-07-17. RSSSF lists the 14 September fixture, so the card is `RESULT_NOT_RECOVERED`.

### Settlements completed in this pass

| Row | Parent custody | Outcome (2026-09-16) |
|---|---|---|
| `P-406-C01` / `P-406-C04` | Part 3 | **WIN / LOSS** — Edinburgh 68/2 after 6.0 overs at the ESPN cricket matchnote; `TMP-OPEN-20260914-06` retired |
| `P-251-C05` | Part 1 (documentary audit) | **Research WIN, threshold-invariant** — ESPN Coppa Italia 6 + 5 = 11 |
| `P-255-C05` | Part 1 (documentary audit) | **UNRESOLVED_PERIOD** — whole-match 24 over 137 does not bound regulation; TMP-AUDIT-20260912-03 reopened 2026-09-17(c) |
| `P-256-C05` | Part 1 (documentary audit) | **UNRESOLVED_PERIOD** — whole-match 15 over 115 does not bound regulation; TMP-AUDIT-20260912-04 reopened 2026-09-17(c) |
| `P-265-C05` | Part 1 (documentary audit) | **Research WIN at exactly the threshold** — ESPN Leagues Cup 4 + 5 = 9; provider-sensitive |
| `P-250-C05` | Part 1 (documentary audit) | Still unsettleable — no keyless route (re-probed) |
| `P-418` | Part 3 | Re-classified `RESULT_NOT_RECOVERED` (not settled) |

**Queue after this pass:** 22 primary handles (13 Part-3, 9 Part-2) and **3** documentary audits. Only `P-406`'s two rows enter the Brier scorecard; every other row above stays provisional or bounded and is excluded.

---

---

# Next forecast slot

**Next canonical ID: `P-452`.** Check the queue in the snapshot first, then follow the mandatory pre-query cycle.

---

# Appendix A — settled open items imported into Part 4 (user direction, 2026-09-16)

Rows whose **parent card sits in a closed part** but whose settlement work was completed in this pass. The issuing part keeps custody of the card; this appendix carries the settlement record, the evidence and the learning, so that the active log shows every item that closed. **Learning-only / not performance-eligible.** No issued rank or probability is altered.

## A.1 `P-406-C01` / `P-406-C04` — Edinburgh Castle Rockers, first six overs (ETPL Match 24, 13 Sep 2026)

- **Settling record (opened 2026-09-16):** ESPN cricket API `cricket/1547871/summary?event=1547895`, matchnote id 767111 in the Edinburgh innings section — *"Powerplay 1: Overs 0.1 - 6.0 (Mandatory - 68 runs, 2 wickets)"*. Toss note: Amsterdam elected to field, so Edinburgh batted first and the card's condition held.
- **Result:** Rank #1 **Over 50.5 WIN** (68; Brier 0.1296); Rank #4 **Under 50.5 LOSS** (0.1296). Card mean Brier 0.2106 over four rows.
- **Handle `TMP-OPEN-20260914-06` retired.** Full settlement, validation answers and retrospective: [Part 3 §"2026-09-16"](PREDICTION_LOG_COMBINED_3.md).
- **Learning:** the row was never unsettleable — the field had been in `DATA_SOURCE_REGISTER.md` since 2026-09-06 and was not queried (`G-L14`).

## A.2 `P-251-C05` — Sassuolo v Frosinone, total corners Over 8.5 (Coppa Italia Round of 32, 2 Sep 2026)

- **Record opened:** ESPN `soccer/ita.coppa_italia/summary?event=401911806` — Sassuolo **6**, Frosinone **5** = **11 corners**; 1–1 at full time, Sassuolo through on penalties.
- **Result: RESEARCH WIN — threshold-invariant.** Every count recovered across three weeks (10, 11, 11) clears 8.5.
- **Booking:** stays provisional under §16.10(j) — Lega Serie A's own record was not reached and the card never pre-registered a provider. `TMP-AUDIT-20260912-02` **kept**, but its "cannot be reproduced" premise is now false.

## A.3 `P-255-C05` — Inter Women v Wolfsburg Women, total corners Over 8.5 (UWCL third qualifying round, second leg, 2 Sep 2026)

> **Current disposition 2026-09-17(c): UNRESOLVED_PERIOD; existing audit handle reopened.** The earlier bounded-win paragraph below is preserved as a superseded settlement receipt. It is not the current grade; see the correction above.


- **Field owner opened:** UEFA `matchstats.uefa.com/v1/team-statistics/2049369` (FAME) — Inter **12**, Wolfsburg **12** = **24 corners**, `played_time` **137**.
- **UEFA score record** (`match.uefa.com/v5/matches`, match 2049369): `regular` **2–0 Inter** — agreeing with the card's 90-minute final — `total` 3–1, penalties 5–4 Inter.
- **Result: RESEARCH WIN, `PERIOD_SCOPE_BOUNDED`.** The contract is 90-minute corners; UEFA reports the whole match. The row loses only if **16 or more of the 24 corners fell in the 30 minutes of extra time** — about six times the match's own rate.
- **`TMP-AUDIT-20260912-03` retired:** the field-owner record is recovered and reproducible; the residual is a period-scope limit, not a missing source.

## A.4 `P-256-C05` — PSG Women v Eintracht Frankfurt Women, total corners Over 8.5 (same round and date)

> **Current disposition 2026-09-17(c): UNRESOLVED_PERIOD; existing audit handle reopened.** The earlier bounded-win paragraph below is preserved as a superseded settlement receipt. It is not the current grade; see the correction above.


- **Field owner opened:** UEFA `team-statistics/2049367` — PSG **11**, Frankfurt **4** = **15 corners**, `played_time` **115**; `regular` **1–1** (agrees with the card), `total` 5–1, PSG won in extra time.
- **Result: RESEARCH WIN, `PERIOD_SCOPE_BOUNDED`** — loses only if 7 or more of the 15 corners fell in extra time.
- **`TMP-AUDIT-20260912-04` retired** on the same basis as A.3.

## A.5 `P-265-C05` — Toluca v Club León, total corners Over 8.5 (Leagues Cup semi-final, 2 Sep 2026)

- **Record opened:** ESPN `soccer/concacaf.leagues.cup/summary?event=401914297` — Toluca **4**, León **5** = **9 corners**; Toluca won 2–0.
- **Result: RESEARCH WIN at exactly the threshold** (9 against 8.5). The earlier secondary display (4–5) agrees exactly.
- **Provider-sensitive:** one corner the other way flips the row, so it stays provisional and `TMP-AUDIT-20260912-05` is **kept**.
- **Contrast with A.2:** P-251 is threshold-invariant, P-265 is knife-edge. That difference is exactly why `G-L14` demands the provider *before* the row is issued, and why it must be recorded on the card.

## A.6 `P-250-C05` — Yunnan Yukun v Chongqing Tonglianglong (China FA Cup quarter-final) — still unsettleable

Re-probed 2026-09-16: ESPN `chn.fa`, `chn.cup`, `chn.fa_cup`, `chn.super_cup` and `chn.2` all return HTTP 400. No keyless route exists. `TMP-AUDIT-20260912-01` **kept**.

## A.7 Part-2 inherited corner rows — re-probed, unchanged

Liga MX Femenil (`mex.w.1`, `mex.femenil`, `mex.liga_mx_femenil`), MLS Next Pro (`usa.nextpro`, `usa.mlsnp`), Championnat National (`fra.3`, `fra.national`), China FA Cup (`chn.fa`, `chn.cup`) and Sikkim (`ind.sikkim`) all returned HTTP 400 on 2026-09-16. The nine Part-2 handles keep their existing provisional dispositions; custody stays with `PREDICTION_LOG_COMBINED_2.md`.

## A.8 What these rows teach, and where it is written

1. **Period scope** — a whole-match feed cannot settle a 90-minute contract exactly → **`G-L16`** (`RULES_GENERAL.md` §16.11(q)), soccer control 36.
2. **Settlement-route execution** — four of five parked rows became reproducible from routes that already existed → `G-L14` (§16.11(m)).
3. **Threshold invariance versus knife edge** — record which one a derivative row is when it is issued; A.2 survives any provider, A.5 does not.
4. **Scorecard effect:** only `P-406`'s two rows are booked. Every other row here remains provisional or bounded and is excluded from the Brier scorecard, so the mixed total moves to 373 rows at ≈ 0.2346 and `PRIMARY_SCORED` is unchanged.

---

## 2026-09-21 — canonical import of P-452–P-473 from settled external mini log

**Disposition:** imported as historical evidence into Part 4. Every canonical prediction from P-452 through P-473 is settled and retrospectively reviewed in the source mini log. Original issued predictions, probabilities, ranks, reasoning and source records are preserved below verbatim. Operational instructions embedded in the historical mini log remain historical evidence; the current governing methodology is read fresh from the root framework documents.

**Source mini log:** `PREDICTION_MINI_RUNNING_LOG_P452_ONWARD.md`  
**Source SHA-256:** `e492c8c3d2bb2d3d302b3482fd6b2512d8eda62fcaf5e3ba9c7e53ec7e86ce0e`

# Prediction Mini Running Log — P-452 Onward

**Created:** 2026-09-17 (Australia/Melbourne)  
**Last settlement / retrospective pass:** 2026-09-20 (Australia/Melbourne)  
**Canonical authority:** `PREDICTION_LOG_COMBINED_4.md`  
**Next canonical ID:** **P-474** (P-452 through P-473 issued in the running sequence; fresh reconciliation required before the next issue)
**Historical issued-card method(s):** preserve each card's recorded version (including MDS-2026.09.06-v4.0); do not retrofit.  
**Governing version for next issue:** **MDS-2026.09.19-v4.3 / CR-2026.09.19-4**  
**Operating mode:** **SPORTS_ONLY / MARKET_BLIND**  
**Performance status:** **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** unless the governing documents are later changed by explicit user direction.  
**Drive-write boundary:** **This existing mini-log remains writable. The user separately authorised the 2026-09-19 framework implementation across the governing Sports Research files; historical issued forecasts remain immutable evidence.**  
**Retrospective policy:** Do **not** run retrospectives automatically. P-452–P-456 were retrospectively reviewed on the prior explicit request. On 2026-09-19/20 the user explicitly requested settlement/retrospective passes over every non-live completed card; **P-452–P-473 are now settled and retrospectively reviewed below. No active unsettled card remains.**

---

<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->

### Prospective control transition — 2026-09-19

The deep-research implementation applies **only to forecasts issued after this transition**. Existing P-452 onward entries retain their original probabilities, reasoning, sources and method versions for audit integrity. Any historical use of a source now classified as betting/fantasy/DFS-derived remains visible as historical evidence but cannot be reused prospectively unless the fact is independently recovered from a permitted upstream source.

Before P-469 or any later new issue: reconcile the current root authority, quarantine the supplied line/total from forecasting, build/freeze the independent sporting distribution first, attach field-level provenance, and obtain a PASS from `prediction_preflight.py`. A `PF-7` version mismatch or any other BLOCK result prevents normal issuance.

## Prospective total-projection display rule — user directive, 19 Sep 2026

Applies to **all future prediction cards in this chat across every sport**. It is prospective only and does not rewrite historical issued cards.

1. **Projected total must be highlighted prominently** before the supplied total is evaluated.
2. Every totals section must print:
   - independent projected total / distribution centre;
   - supplied total line;
   - raw gap = projected total minus supplied line;
   - distribution width / uncertainty;
   - normalized gap where available.
3. The supplied total remains quarantined until the independent sporting distribution is frozen. This display rule does **not** permit line-anchoring.
4. A total whose supplied line lies close to the projected centre must be labelled **CLOSE TO PROJECTION / WEAK MAIN-TOTAL EDGE** rather than being presented as a strong Over/Under merely because it is Rank #1 among weak options.
5. "A few points/runs/goals" is **sport-relative**, not one absolute number. The primary closeness test is the distance from the line relative to the forecast distribution width. As a working presentation rule:
   - normalized gap `<= 0.20 SD`: **CLOSE / weak main-total edge**;
   - `0.20–0.40 SD`: **modest separation**;
   - `> 0.40 SD`: **meaningful separation**, still subject to evidence quality and model validity.
   These are presentation/decision-strength labels, not fitted calibration claims.
6. When the main total is CLOSE to the projection, search the same frozen distribution for a **more conservative alternate total**. Prefer an alternate only if it materially improves the modelled win probability and is directionally supported by the score distribution.
7. Do **not** force an alternate Over solely because the user prefers Overs. If the model supports a lower alternate Over, state it explicitly (for example, `Over X or lower`). If the model instead supports an alternate Under, report that. If neither side achieves a materially safer probability, say **NO STRONG TOTAL / no justified alternate**.
8. Never invent sportsbook availability. If an exact alternate line has not been supplied or independently verified as available, state it as a **model target threshold** (for example, `Model alternate target: Over 179.5 or lower`) rather than claiming it is currently offered.
9. The alternate-total row must come from the **same frozen joint distribution** as the primary total. No re-centering after seeing the supplied line.
10. The headline summary for every future card must contain a compact total block in this form:

   **Projected total:** X  
   **Supplied total:** Y  
   **Gap:** X - Y = Z  
   **Main-total assessment:** strong / modest / close-to-projection  
   **Preferred main side:** Over / Under / no strong edge  
   **Alternate-total target:** exact threshold or `NONE JUSTIFIED`

11. If the projected total is only slightly below a supplied Over/Under line, do not automatically rank the Under highly. Explicitly test whether a lower alternate Over produces a materially stronger probability than the supplied Under. Likewise, if the projection is slightly above the supplied line, test a higher alternate Under as the symmetric conservative alternative.
12. Rank #1 must still be the highest-probability justified selection under the governing methodology. An alternate total may replace the supplied total in the top ranks if its probability is genuinely higher and its definition is clear.
13. All alternate-total selections remain `UNVALIDATED_SUBJECTIVE` unless governed by a promoted numerical model.
14. No retrospective is triggered by this directive.

**Document mapping:** candidate clarification for `METHOD.md` compact output / totals presentation and `RULES_GENERAL.md` line-distance/alternate-line handling. No Drive files are modified by this local directive.

## Prospective offensive / defensive ceiling-floor audit — user directive, 19 Sep 2026

**Purpose:** prevent underestimating or overestimating a team's game-specific scoring ceiling/floor when forecasting totals. Applies prospectively to every sport and every new prediction card in this chat. Historical cards remain immutable.

### Hard gate before any total can be Rank #1

A total cannot be Rank #1 until the card shows:
1. Team A offensive floor / centre / ordinary high / tail ceiling.
2. Team B offensive floor / centre / ordinary high / tail ceiling.
3. Team A defensive allowance floor / centre / ordinary high / tail concession state.
4. Team B defensive allowance floor / centre / ordinary high / tail concession state.
5. A joint interaction grid crossing offence and defence.
6. A mutual-offence / shootout branch where the sport permits both sides to score well.
7. A mutual-suppression branch.
8. A one-sided separation branch for each side.
9. A threshold/component budget showing how each side/component can cross the supplied line.
10. The likely scoring corridor, not only a single projected total.

If those items are materially unresolved, the total is capped at FORCED RANK / LOW and cannot be presented as a strong total.

### Baseline construction

For each team, separate:
- long-run scoring/prevention strength;
- current personnel/role/tactical mechanism;
- opponent-specific interaction;
- available exposure/opportunity (possessions, entries, innings, overs, shots, drives, etc.).

L5/L10/L15/L20 outcomes remain descriptive unless a named mechanism explains persistence.

### Ceiling/floor definitions

- **Floor:** low but ordinary outcome, not an extreme collapse.
- **Centre:** central/median scoring state.
- **Ordinary high:** strong but plausible outcome under normal current-game variance.
- **Tail ceiling:** rarer upper state requiring exceptional conversion/sequencing/game script.

Do not use one team's single best or worst game as its ceiling/floor.

### Mandatory interaction families

Model disjoint branches when applicable:
1. both suppressed / low-total close;
2. Team A normal-high, Team B suppressed;
3. Team B normal-high, Team A suppressed;
4. both central;
5. both score well / competitive high-total;
6. high-total Team A separation;
7. high-total Team B separation;
8. conversion/sequencing tail.

P-469 specifically exposed the missing importance of branch 5: a high AFL total did not require Brisbane to separate; Hawthorn's own strong offence could combine with normal Brisbane scoring.

### Threshold budget

For supplied line L, print:
- Team A centre and ordinary high;
- Team B centre and ordinary high;
- combined centre;
- gap to L;
- whether A-high + B-centre crosses L;
- whether A-centre + B-high crosses L;
- whether A-high + B-high crosses L;
- corresponding low/centre combinations below L.

If multiple ordinary combinations fall on both sides of L, classify it as INSIDE CENTRAL CORRIDOR / WEAK DIRECTIONAL TOTAL unless scenario weights genuinely separate the sides.

### Sport-specific research

**AFL/AFLW:** points for/against; inside-50 volume/differential; scores/goals per inside 50; marks inside 50; shot quality/expected score where available; scoring shots; clearance and centre-bounce scoring; turnover scoring; defensive-half transition; pressure; goal/behind conversion; forward/defender availability; venue/wind/surface; fourth-quarter interchange/durability. Men's totals >=180 require a both-teams high-shot branch.

**Baseball:** confirmed starter role/exposure; K/BB; contact quality and expected metrics; batting order; bullpen quality/workload; platoon; park/roof/weather; extra-inning and home-last-bat tail; separate starter/middle/late run states.

**Basketball:** pace/possessions; OffRtg/DefRtg; eFG/TS; turnover and offensive-rebound rates; FT generation; opponent shot profile; starters/bench/minute restrictions; rest/travel through pace/minutes; blowout compression; both-hot and both-cold shooting branches.

**Soccer:** xG for/against from one provider lineage; shots and shots-in-box; shot quality; finishing and goalkeeper effects separately; transitions; set pieces; XI/striker/creator/CB/GK availability; game-state effects; venue/competition scoring environment.

**Cricket:** toss/innings order; full XI and roles; powerplay/middle/death scoring and wicket rates; wickets as both scoring and remaining-ceiling variables; batter/bowler matchups; strip/boundaries/weather/dew; chase cap/DLS; low/central/high phase budgets with cross-phase dependence.

Other sports use the same principle with their native opportunity chain.

### Mandatory total output block

Every future prediction containing a total must visibly print:

- Team A floor / centre / ordinary high
- Team B floor / centre / ordinary high
- Projected combined total
- Central scoring corridor
- Upper ordinary corridor
- Supplied total
- Distance from centre
- Main Over/Under probability
- Main total strength: STRONG / MODEST / WEAK / NO EDGE
- Safer alternate Over threshold
- Safer alternate Under threshold
- Biggest Under failure path
- Biggest Over failure path

Alternate thresholds are model targets unless operator availability is actually verified.

**Status:** prospective execution control for this chat. No historical probabilities are rewritten and no Google Drive file is modified.

## Hard settlement-source gate — correction after P-469 false-final incident, 19 Sep 2026

This rule is prospective and applies to every sport before moving an entry from **Incomplete / Unsettled** to **Fully Settled**.

1. **Search-result snippets, generated search summaries, headlines, recap blurbs and inferred winner language are never sufficient to establish `FINAL`.**
2. Prefer a **field-owner exact-event record** carrying an explicit terminal state such as `FINAL`, `FT`, `Completed`, `Game Over`, `Result`, or the sport's equivalent.
3. **Superseded by the universal CR-4 gate below:** settlement requires **at least three distinct reliable source lineages**. If the field-owner endpoint is unavailable or delayed, do not fall back to a two-source settlement.
4. A score by itself is **not** proof of finality. Quarter/period/inning/time state must also be checked where applicable.
5. If any reliable source still labels the event `LIVE`, `IN PROGRESS`, `Q1/Q2/Q3/Q4`, `inning/over in progress`, or otherwise non-terminal, the event remains **UNRESOLVED**.
6. If sources conflict on event status, **fail closed**: keep the log unresolved and do not perform settlement or retrospective work.
7. Never infer finality from language such as “advanced”, “secured a place”, “won”, or a recap-style paragraph unless the underlying source itself is verified as a completed-event record.
8. Before a Drive write that moves any event to settled, run a final **event-state recheck immediately before the write**.
9. After the Drive write, read the file back and verify that no still-live event was moved to the settled section.
10. If a false settlement is discovered, restore the last correct unresolved state, remove all hindsight-contaminated retrospective material, document the source failure, and do not reuse the contaminated settlement reasoning later.

**P-469 incident:** a search-result summary for a live Guardian page described Brisbane as having already advanced even though the underlying Guardian live page and ABC live coverage still identified Hawthorn–Brisbane as live. That summary was an invalid settlement source and must not be used for final-state verification.

**Document mapping:** candidate reinforcement for `EXTERNAL_LOGGING_WORKFLOW.md`, `SOURCES.md`, and retrospective/settlement controls. No governing Markdown file is changed by this local rule unless separately authorised.

## Universal three-source + date/time verification gate — user directive, 19 Sep 2026

**Scope:** applies prospectively to **every sport, competition and game log**, including pregame forecasts, live-state checks, settlements and retrospectives. Historical issued predictions remain immutable evidence; this gate controls all new research and all future status changes.

### A. Minimum source requirement — every event

1. Every event/game log must use **at least three distinct reliable source lineages**.
2. Three mirrors, syndicated copies, reposts, or search summaries of the same upstream report count as **one lineage**, not three.
3. At least one source should be the **field owner / governing competition / official team or club** for event identity, schedule, participants, roster state or result whenever such a source is available.
4. A game log with fewer than three qualifying source lineages is **SOURCE-INCOMPLETE** and must not be presented as fully verified.
5. Search-result snippets, AI/search summaries, headlines and aggregator blurbs are **discovery only**. They do not count toward the three-source minimum until the underlying source is opened and verified.
6. Where a material fact is central to a pick — starting pitcher, starting XI/five, injury, scratch, venue, weather, toss, roof state, late change, etc. — prefer direct field-owner/team evidence and corroborate it when possible.
7. If the three sources conflict on a material event fact, fail closed: print the conflict, lower confidence, and do not silently choose the convenient version.

### B. Mandatory event date/time verification

Before issuing, refreshing, settling or retrospectively analysing an event, record and verify:

- **venue / host city / country**;
- **official scheduled local calendar date**;
- **official scheduled local clock time**;
- **venue-local timezone name and UTC offset on that exact date**;
- **Australia/Melbourne converted calendar date and clock time**;
- **Melbourne timezone label on that exact date: AEST or AEDT**;
- whether the conversion crosses midnight / changes the calendar date.

The conversion must be done from the event's actual local timezone using a timezone-aware conversion. Do **not** apply a fixed offset by memory.

### C. Time-source hierarchy

For date/time identity, use this hierarchy:

1. governing competition / league / federation exact-event page;
2. official home/host club or team exact-event page;
3. official away/visitor club or team exact-event page;
4. high-quality broadcaster / wire / established statistical provider;
5. lower-tier secondary source only as corroboration.

The event must still satisfy the **minimum three-source** rule overall.

### D. User-supplied time handling

- User-supplied start times are treated as **estimated contract metadata**, not authoritative schedule evidence.
- Always independently verify the event's local date/time.
- If the verified time differs from the user-supplied time, print the correction explicitly before analysis.
- Never silently retain an incorrect user timezone label.
- Example rule: `18:00 JST on 19 Sep 2026 = 19:00 AEST on 19 Sep 2026`; a European or American evening game may convert to the **next Melbourne calendar day**.
- For dates when Melbourne observes daylight saving, use **AEDT (UTC+11)** rather than AEST (UTC+10).

### E. Pregame / live-state status gate

Immediately before issuing a card or doing a late refresh:

1. Re-check the exact event on at least **three qualifying source lineages**.
2. Verify that the event state is mutually consistent: `SCHEDULED/PREGAME`, `LIVE`, `POSTPONED/CANCELLED`, or terminal.
3. If a credible current source says the event is live while another says scheduled/final, mark `EVENT_STATE_CONFLICT` and fail closed on settlement.
4. Do not infer state solely from the scheduled clock time. Delays, postponements, timezone mistakes and provider latency must be considered.
5. A card issued after verified start must be labelled as a **live-state analysis**, not retrospectively called pregame.

### F. Settlement gate — minimum three sources

No event may move from **Incomplete / Unsettled** to **Fully Settled** unless all of the following are true:

1. **At least three distinct reliable source lineages** verify the exact event.
2. All three agree on:
   - event identity;
   - date;
   - terminal/final state;
   - final score/result;
   - any derivative field needed to settle the logged contracts.
3. Preferably, at least one of the three is the **field owner / league / federation**. If the field-owner final is temporarily unavailable, settlement remains blocked unless three independent high-quality sources explicitly show the same terminal result and no reliable current source conflicts.
4. A score without an explicit terminal marker is **not finality evidence**.
5. Any reliable `LIVE / IN PROGRESS / Qx / inning / over / set / period remaining` state blocks settlement.
6. Search summaries and snippets **never count** as a settlement source.
7. If one source is stale or clearly wrong, exclude it and find another qualifying source; do not count a known-bad source just to reach three.
8. Immediately before the Drive write, re-check event state again. Immediately after the write, read back the log and verify that no live event was moved to settled.

### G. Three-source source-record block required in every future game log

Every new event must contain a compact verification table with at least:

| Source # | Source / lineage | Role | Event date/time verified? | Participant/state/result verified? | Quality |
|---:|---|---|---|---|---|
| 1 | field owner / league / federation | identity + official schedule / final | YES/NO | YES/NO | PRIMARY |
| 2 | official team/club or equivalent | participant / roster / exact-event corroboration | YES/NO | YES/NO | PRIMARY/TEAM |
| 3 | independent high-quality source | independent corroboration | YES/NO | YES/NO | HIGH-QUALITY SECONDARY |

Additional sources may be added for weather, stats, injuries, derivative markets and venue-specific fields.

### H. Cross-sport application

This gate applies without exception to:

- AFL / AFLW
- MLB / NPB / other baseball
- NBA / NBL / WNBA / other basketball
- soccer / football
- cricket
- tennis
- rugby league / rugby union
- ice hockey
- American football
- combat sports
- motorsport
- any new sport added later.

Sport-specific rules still govern the substantive modelling, but **source count, event identity, date/time conversion and final-state verification are universal hard gates**.

### I. Failure-state labels

Use these labels when applicable:

- `SOURCE_COUNT_LT_3`
- `SOURCE_LINEAGE_NOT_INDEPENDENT`
- `EVENT_DATE_NOT_VERIFIED`
- `EVENT_LOCAL_TIME_NOT_VERIFIED`
- `EVENT_TIMEZONE_NOT_VERIFIED`
- `MELBOURNE_TIME_CONVERSION_NOT_VERIFIED`
- `EVENT_STATE_CONFLICT`
- `FINAL_STATE_NOT_VERIFIED_BY_3_SOURCES`
- `DERIVATIVE_SETTLEMENT_FIELD_NOT_VERIFIED_BY_3_SOURCES`

Any of these labels prevents a normal fully-verified issuance/settlement claim for the affected field.

### J. P-469 incident disposition

The P-469 false-final incident is the reference failure case:
- a search-result summary was treated as if it were a terminal event source;
- the underlying live pages still showed the match in progress;
- the event should therefore have remained unresolved.

Prospectively, **three-source event-state verification plus timezone-aware date/time verification is mandatory before any settlement or status transition.**

**Document mapping:** this is a cross-sport execution control for the writable running log. It is a candidate reinforcement for `METHOD.md`, `RULES_GENERAL.md`, `SOURCES.md`, `EXTERNAL_LOGGING_WORKFLOW.md` and sport-specific settlement sections if the user later requests governing-file edits.


### CR-4 authority synchronization — 19 Sep 2026

The universal three-source/date-time gate in this running log is now promoted into the governing Drive framework under **MDS-2026.09.19-v4.3 / CR-2026.09.19-4**. Existing P-452–P-471 issued cards retain their historical method/control versions; only future issues and future status/settlement checks use CR-4.

## 1. Incomplete / Unsettled Logs

**Audit refresh:** 20 Sep 2026, approximately 08:00 AEST. **No active unsettled game logs remain.** P-472 and P-473 were verified terminal under the current settlement gate, fully settled, retrospectively reviewed, and moved into the canonical running sequence below.

**Current unsettled queue:** **NONE.**

## 2. Temporary-ID / Canonical-ID Conflict Logs

**None in this pass.** Direct fresh checks of `PREDICTION_LOG_COMBINED_4.md` found no P-452–P-462 card collision. P-458, previously issued in chat but not successfully written to Drive, remains restored in sequence; P-460, P-461 and P-462 have now been issued locally with no canonical collision. No canonical ID was overwritten or reassigned.

---

## 3. Fully Settled Logs

The original pre-game cards are preserved. Statements inside those frozen cards such as “no retrospective performed” or “unsettled at issue” describe the **issued pre-game state** and are not retroactively edited. Each card is followed by its dated settlement/retrospective.


### P-452 — Cricket / Afghanistan vs India T20I Series 2026 — Afghanistan vs India, 3rd T20I

- **Canonical ID:** P-452
- **Sport / competition:** Cricket — Men's T20I bilateral series, Afghanistan vs India in India, 2026
- **Event:** Afghanistan vs India, 3rd T20I
- **Venue:** Arun Jaitley Stadium, New Delhi, India
- **Scheduled start:** 17 Sep 2026, 19:30 IST = 18 Sep 2026, 00:00 AEST (Australia/Melbourne)
- **Game state at issue:** **PREGAME — toss complete; scheduled first ball not yet due at frozen cutoff**
- **Research cutoff / final refresh:** 17 Sep 2026, 19:26:54 IST / 23:56:54 AEST
- **Method version:** MDS-2026.09.06-v4.0
- **Population status:** EXPLORATORY — NOT SCORED for primary-performance purposes; learning-only per controlling log

#### Identity / market validation

1. **Actual fixture verified:** Afghanistan vs India, 3rd T20I, Delhi, 17 Sep 2026. BCCI and Afghanistan Cricket Board both list the three-match series ending with this fixture at Arun Jaitley Stadium.
2. **Innings-market team verified from supplied contract:** both supplied markets explicitly name **India**. A current toss report states Afghanistan won the toss and chose to field, so **India are batting first** and the supplied India first-innings targets are activated.
3. **Operative supplied lines frozen:** India 20-over runs **216.5** and India first-six-over runs **66.5**. No independent operator page was recovered confirming those exact numbers before cutoff, so market-threshold provenance remains **USER_SUPPLIED / OPERATOR_NOT_INDEPENDENTLY_VERIFIED**.
4. **Stale inconsistencies flagged, not silently corrected:** the prompt's mandatory-validation text mentions **England vs Sri Lanka**, says the supplied markets refer to **Afghanistan**, and separately asks to verify **193.5 / 60.5**. Those statements conflict with the actual heading and listed India 216.5 / 66.5 markets. They are treated as stale copied validation text, not alternative contracts.
5. **First-innings definition:** because India are confirmed to bat first, the India innings is the match's first innings; there is no silent transfer to a chase target.

#### Toss / participants / availability

- **Toss:** Afghanistan won and elected to field; India bat first.
- **India:** current live reporting confirms **Vaibhav Sooryavanshi is not in the XI** and **Yash Thakur replaces Arshdeep Singh**. The same report preserves the established opening combination of **Sanju Samson + Abhishek Sharma**.
- **India squad changes/fitness:** Harshit Rana was ruled out before the series after a rectus-femoris strain and Yash Thakur replaced him in the squad. Varun Chakaravarthy was reported ruled out of the third T20I with a side strain.
- **Afghanistan:** squad includes Ibrahim Zadran (c), Rahmanullah Gurbaz, Sediqullah Atal, Darwish Rasooli, Gulbadin Naib, Azmatullah Omarzai, Mohammad Nabi, Rashid Khan, Noor Ahmad, Mujeeb Ur Rahman, Fazalhaq Farooqi, Naveen-ul-Haq, Nangeyalia Kharote, Abdullah Ahmadzai and Noor ul Rahman. A full independently captured official XI was **not recovered before cutoff**, so exact Afghanistan bowling-combination status remains a material uncertainty.
- **Coaches / bench:** prior current-series records list Gautam Gambhir as India head coach and Richard Pybus as Afghanistan head coach. Full match-day bench was not independently recovered at cutoff; this reduces evidence strength but does not invalidate the two phase/team-total contracts.

#### Venue / pitch / dimensions / conditions

- **STRIP STATUS:** **NOT FOUND AFTER SEARCH** for an exact toss-time field-owner strip report. The search covered current live/toss coverage, exact-match pitch reports, venue pitch-report/curator searches, specialist previews, and ICC/DDCA searches. No reliable match-specific curator or broadcast strip quote was recovered.
- **Historical/current-regime pitch context:** exact-match previews consistently describe Arun Jaitley Stadium as batting-friendly with compact boundaries and true enough bounce for strokeplay, while acknowledging spin/pace-off can matter in the middle overs.
- **Ground dimensions:** reported recent venue references place square boundaries roughly in the low-to-mid 60 m range and the straight boundary near 68–70 m. This is contextual, not an exact rope measurement for this match.
- **Venue scoring context:** a Cricsheet-derived venue analysis reports men's T20I first-innings average about **168** (12 matches through Mar 2026) and IPL first-innings average about **173** over the long sample. These broad baselines are well below 216.5, but the current India batting regime is materially stronger than a generic venue mean.
- **Current series:** Afghanistan made **156/8** and **159/8** batting first in the first two games. India chased both in 13.4 and 14.5 overs.
- **Weather / rain:** forecast evidence is **CONFLICTING**. Weather.com showed roughly 30°C around 19:30 IST, humidity rising from the low 60s, light WNW wind and very low near-term rain probability, while the structured forecast carried an **India Meteorological Department yellow watch for heavy rainfall/thunderstorms in Delhi until 22:00 IST**. Therefore interruption risk is non-zero and wider than a single commercial forecast suggests.
- **Dew:** warm humid evening conditions make dew plausible later, but India bat first, so any stronger second-innings dew advantage helps Afghanistan's chase more than India's first-innings scoring. Dew is not used as a positive India-total adjustment.
- **Contract assumption for weather:** probabilities below are conditional on a normal 20-over first innings. Operator treatment of a rain-shortened innings was not supplied; any reduced-overs/DLS action must follow the operator's actual rules and is not silently graded as a normal full-innings result.

#### Recent form / phase evidence

- **India powerplay:** India scored **82 runs in the first six overs in each of the first two T20Is** at this same venue against this same opponent. That directly clears the supplied 66.5 line twice and is the highest-value current-regime comparable under `G-L20`.
- **Second T20I disaggregation:** India were 82/0 after six, 88/1 at 6.2 when Rashid Khan dismissed Abhishek Sharma, and finished 163/3 in 14.5 overs. This demonstrates both the extreme opening ceiling and the real post-powerplay spin slowdown/wicket branch.
- **First T20I:** India chased 157/3 in 13.4 overs; Abhishek Sharma made 82 off 32. The powerplay was again 82.
- **Afghanistan bowling:** Rashid remains the strongest middle-overs wicket mechanism; the current series shows Afghanistan have not contained India's first-six scoring, but Rashid's post-powerplay wickets are a meaningful reason not to extrapolate the 82-run opening pace linearly to 20 overs.

#### Joint event object / component budget

**India 0–6 overs target**
- Centre: **73 runs**
- Width: approximately **15 runs** (high T20 powerplay variance; widened for uncertain exact Afghanistan XI and weather)
- Main branches: explosive 0–1 wicket start 48%; ordinary aggressive start 34%; early 2+ wicket disruption 18%.

**India 20-over first-innings target**
- Centre: **207 runs**
- Width: approximately **25 runs**
- Component budget: powerplay **73** + overs 7–15 **85** + overs 16–20 **49** = **207**.
- Transition logic: a fast powerplay does **not** imply a 230+ innings. Rashid/Noor/Mujeeb-style middle-overs control, wickets, and phase change pull the central innings projection below a straight extrapolation of India's two 82-run chases. Conversely, batting first removes the chase-target cap, preserving a substantial 220+ ceiling.

**Top-two coupling:** `P(R1 ∧ R2)` ≈ **0.44**. `P(neither preferred side wins)` ≈ **0.12**. The principal both-fail state is **India score ≤66 in the powerplay but then surge through the middle/death to exceed 216.5**. At least one preferred side wins ≈ **0.88**. These are `UNVALIDATED_SUBJECTIVE` joint masses, not calibrated model outputs.

#### Ranked picks

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence | Geometry | Why this rank | Main failure path |
|---:|---|---:|---|---|---|---|
| **1** | **India 1st innings, first 6 overs — OVER 66.5 runs** | **0.67** | MEDIUM-HIGH | FORCED_PAIR preferred side | Same opponent, same venue, same established opening pair; India scored 82 in both prior powerplays. `G-L20` requires those direct clears to carry explicit mass. | Farooqi/Mujeeb/new-ball combination takes 2+ early wickets, weather interrupts, or India deliberately starts slower batting first. |
| **2** | **India 1st innings, 20 overs — UNDER 216.5 runs** | **0.65** | MEDIUM | FORCED_PAIR preferred side | 216.5 is materially above broad Delhi T20/T20I baselines. The 20-over centre is ~207 after explicitly separating powerplay from middle/death phases; Afghanistan's spin wicket path is more relevant after over six. | India preserve wickets through a 70–80 powerplay and convert the no-chase-cap batting-first scenario into a 220–240 finish. |
| **3** | **India 1st innings, 20 overs — OVER 216.5 runs** | **0.35** | MEDIUM-LOW | FORCED_PAIR non-preferred side | Live ceiling is real because India have twice scored at >11 RPO while chasing; batting first removes target censorship. | Middle-overs spin/wickets or a merely average opening leaves India around 185–210. |
| **4** | **India 1st innings, first 6 overs — UNDER 66.5 runs** | **0.33** | MEDIUM-LOW | FORCED_PAIR non-preferred side | Requires a meaningful departure from the two direct 82-run current-series comparables. | The unchanged India opening pair again attacks successfully and clears 67 before the sixth over ends. |

**Decision interpretation:** the card contains two complementary O/U pairs, so under `G-L22` these are **two decisions, not four independent bets**. The preferred decisions are **Powerplay Over 66.5** and **20-over Under 216.5**.

#### Projected match winner

- **Projected winner: India**
- **Winner endpoint:** eventual match winner if a result is produced under T20I/Super Over rules.
- **Outcome-state family (unvalidated subjective):** India eventual win **0.73**, Afghanistan eventual win **0.23**, no-result/abandonment **0.04**.
- Rationale: India lead the series 2–0, won both matches by seven wickets, and have dominated Afghanistan's attack in the powerplay. Counterweight: India are batting first after Afghanistan won the toss, India have rotated at least one bowler, and weather/dew can improve Afghanistan's chase conditions.

#### Information not confirmed / integrity flags

- Exact operator page for the **216.5 / 66.5** thresholds not independently recovered.
- The **193.5 / 60.5** values in the copied validation text were not verified and are **not used**.
- Exact toss-time field-owner pitch/strip report not recovered.
- Full official Afghanistan XI and full match-day benches not independently captured before cutoff.
- Weather sources conflict materially; rain/interruption branch therefore remains wider than the low-rain commercial forecast alone.
- No retrospective performed.
- **Current settlement status:** **UNSETTLED — PREGAME AT ISSUE**.

#### Settlement routes pre-registered

- Match result / innings total / scorecard: official or field-owning cricket match record first; ICC/board match centre where available, with ESPN/NDTV/other structured scorecard only as documented fallback/corroboration.
- First-six-over runs: a structured ball-by-ball or scorecard that explicitly records the end-of-six-over state; reduced-innings powerplays must not be treated as a normal six-over contract.

#### Sources

| Source | Link / record | Contribution | Quality / limitation |
|---|---|---|---|
| BCCI | https://www.bcci.tv/news/article/indias-squad-for-afghanistan-t20i-series-announced | Official India squad and series schedule | Primary |
| BCCI | https://www.bcci.tv/news/article/yash-thakur-replaces-harshit-rana-in-indias-t20is-squads-for-afghanistan-t20is-and-asian-games | Harshit Rana ruled out; Yash Thakur replacement | Primary |
| Afghanistan Cricket Board | https://acb.af/en-US/post/acb-names-squad-for-the-t20i-series-against-india | Official Afghanistan squad, Naveen return, schedule | Primary |
| Afghanistan Cricket Board | https://acb.af/en-US/post/acb-to-host-india-for-three-match-t20i-series-in-delhi | Official fixture/venue confirmation | Primary |
| ICC | https://www.icc-cricket.com/news/batting-fireworks-delight-delhi-as-india-go-up-2-0 | Series state and second-match result/context | Primary/high-quality |
| Reuters | India-Afghanistan 1st T20I report, 13 Sep 2026 | 1st match result; India 157 chase; Abhishek 82; Afghanistan 41/4 PP context | High-quality secondary |
| NDTV Sports / SportsTak / Times of India scorecards | 1st/2nd T20I scorecards, 13 & 15 Sep 2026 | Scores, wickets, second-match chase details | Structured secondary/corroboration |
| Times of India 2nd T20 live score | 15 Sep 2026 | India 82 after six for second consecutive match; 88/1 at 6.2 | Current-series disaggregated record |
| Current Jansatta live report | 17 Sep 2026 | Afghanistan won toss/fielded; India bat first; Yash for Arshdeep; Vaibhav out | Current secondary; exact full XI page not independently opened |
| India Today / Cricbuzz current previews | 17 Sep 2026 | Current lineup uncertainty, Varun injury, matchup/pitch context | Reputable/specialist secondary |
| Weather.com hourly New Delhi | 17 Sep 2026 | 19:30–22:30 temperature, humidity, wind, low near-term rain signal | Commercial forecast |
| India Meteorological Department alert surfaced through structured weather source | 17 Sep 2026 | Yellow watch for rainfall/thunderstorms in Delhi until 22:00 IST | Government field owner; conflicts with low-rain commercial point forecast |
| Crickettaken venue analysis (Cricsheet-derived) | 2026 venue profile | T20I/IPL first-innings baselines | Secondary analysis; historical, not today's strip |
| Current exact-match pitch previews (Jagran, ABP, Moneycontrol) | 17 Sep 2026 | Consistent batting-friendly/short-boundary context | Secondary; not a field-owner strip report |
| User-supplied market text | Current query | Exact 216.5 and 66.5 contract thresholds | Contract source only; operator not independently verified |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| Direct same-venue India powerplay clears (82, 82) must be printed against 66.5 | `RULES_CRICKET.md` control 30 / `G-L20` | Existing control correctly applied; **NO CHANGE** |
| First-innings activation became valid only after toss confirmed India bat first | `RULES_CRICKET.md` conditional-activation / `G-L14` | Existing control correctly applied; **NO CHANGE** |
| Exact-strip report not recovered despite six-rung search | `RULES_CRICKET.md` §2 / source register | Evidence limitation only; **NO CHANGE** |
| IMD alert conflicts with low-rain commercial hourly forecast | `SOURCES.md` / `DATA_SOURCE_REGISTER.md` | Candidate source-quality note; retain government alert as higher-authority risk signal, no forecast-weight rule change |
| Stale copied validation block contained wrong fixture/team/lines | `EXTERNAL_LOGGING_WORKFLOW.md` / event integrity notes | Process observation only; preserve explicit contradiction flag, no automatic rule promotion |

#### Settlement and retrospective — 18 Sep 2026

- **Final status:** `SETTLED — FINAL`.
- **Final result:** India **221/7 (20.0)**; Afghanistan **94 all out (14.1)**. India won by **127 runs**.
- **Exact phase result:** India were **100/0 after 6.0 overs**. ICC reports the opening pair reached 100 in the powerplay; the structured scorecard independently records the mandatory powerplay as 100/0.
- **Canonical-ID audit:** no P-452 entry exists in `PREDICTION_LOG_COMBINED_4.md`; no collision was found. P-452 remains the mini-log canonical ID.
- **Original prediction preserved:** the pre-game card above is unchanged. The following section is post-result analysis only.

##### A. Ranked-pick and winner settlement

| Rank | Frozen selection | Final target | Result | Settlement note |
|---:|---|---:|---|---|
| 1 | India first 6 overs **Over 66.5** | **100/0** | **WIN** | Cleared by 33.5 runs. |
| 2 | India 20-over innings **Under 216.5** | **221/7** | **LOSS** | Missed by 4.5 runs. |
| 3 | India 20-over innings **Over 216.5** | **221/7** | **WIN** | Cleared by 4.5 runs. |
| 4 | India first 6 overs **Under 66.5** | **100/0** | **LOSS** | Exact complement of Rank #1. |
| — | Projected eventual winner: **India** | India by 127 runs | **WIN** | Match result was decisive; no Super Over/no-result ambiguity. |

**Forced-pair decision view:** powerplay preferred side Over 66.5 = **WIN**; 20-over preferred side Under 216.5 = **LOSS**. The four table rows are two forced-pair decisions, not four independent trials.

**Top-of-list diagnostics:** Rank #1 = **WIN**; Wins@2 = **1**; Hit@2 = **1**; both top two won = **NO**. Binary-relevance NDCG@2 = **0.613** because the two winning rows were ranks #1 and #3. This is a learning-only diagnostic, not a performance claim.

##### B. Why each pick won or lost

**Rank #1 — powerplay Over 66.5: WIN.** The strongest pre-game evidence was unusually direct: India had scored 82 in each of the first two powerplays at the same venue against the same opponent, with the same opening combination. That mechanism did not merely persist; it intensified. India reached 51/0 in 3.3 overs and 100/0 after six. Abhishek Sharma reached fifty from 16 balls and the opening pair attacked both pace and spin. The card was therefore correct to give the direct same-regime comparables explicit weight. The result does not prove 0.67 was calibrated, but the **direction and Rank-1 placement were justified by information available before play**.

**Rank #2 — innings Under 216.5: LOSS.** The pre-game innings centre was 207, built as 73 powerplay + 85 overs 7–15 + 49 overs 16–20. The main miss was not that the analysis failed to imagine middle-overs spin or wickets. Those mechanisms did appear: Abhishek was dismissed at 9.5 overs, India were 201/4 after 17, and finished seven wickets down. The miss was the **starting phase magnitude**. A 100-run powerplay was 27 runs above the printed powerplay centre, and India were already 142/1 at 9.5 overs. Once that branch occurred, even meaningful post-powerplay deceleration left 217+ highly reachable. The card gave too little joint mass to the state “extreme powerplay + later slowdown + full-innings Over”.

**Rank #3 — innings Over 216.5: WIN.** Its stated upside path was an intact explosive opening followed by enough conversion without a chase target cap. That path occurred. The Over was only narrowly successful at 221, which is important: the later wickets and slowdown did matter. The correct retrospective is therefore not “India were unstoppable for 20 overs”; it is that the first ten overs created enough resource/scoring surplus to survive the later drag.

**Rank #4 — powerplay Under 66.5: LOSS.** This was the non-preferred complement and required a sharp departure from the two directly comparable 82-run powerplays. No such early disruption occurred. The card appropriately ranked this fourth.

##### C. Rank-1 review

No deep failure review is triggered because Rank #1 won. The ranking process was defensible: current, same-opponent, same-venue phase evidence was stronger than generic Delhi averages. The retrospective improvement belongs instead to **conditional dependence between the winning powerplay thesis and the full-innings total**. A card can correctly rank a powerplay Over first yet still mis-rank a full-innings Under if it does not sufficiently condition the later total on the high-powerplay branch.

##### D. Top-two review

Rank #1 won but Rank #2 lost. The relative ordering was correct; the issue was the second selection’s robustness. The top two were positively coupled through India’s early batting strength, but in opposite ways at the full-innings line: an extreme Rank-1 win materially increased the chance Rank #2 would fail. Future cricket cards should explicitly print the full-innings target distribution conditional on **low / central / high powerplay states** when both markets are on the same innings. This is a candidate process refinement, not a new forecast coefficient.

##### E. Over/under review

The powerplay Over was supported by direct phase comparables. The full-innings Under relied heavily on the high absolute threshold relative to venue history and expected middle-overs control. The event shows why broad venue means cannot dominate a current-regime phase state when the same batting unit has demonstrated extraordinary early scoring. The useful improvement is **state-conditional component budgeting**: if the six-over branch lands around 90–100, recompute what overs 7–20 must average for each 20-over side to win. Do not infer a universal “prefer Overs” rule from this match.

##### F. What went right

- Exact fixture, toss and first-innings activation were correctly verified.
- Same-venue/same-opponent powerplay evidence was correctly elevated under `G-L20`.
- The card did not linearly extrapolate 82 runs across 20 overs; it correctly anticipated a post-powerplay slowdown/wicket mechanism.
- India as projected winner was well supported and correct.
- Weather uncertainty was kept as uncertainty rather than assigned an unsupported signed scoring effect; material rain did not decide the match.

##### G. Blind spots and smallest fixes

| Blind spot | Effect here | Future treatment |
|---|---|---|
| Conditional phase dependence insufficiently quantified | Extreme 100-run PP made the 216.5 Under much weaker than its marginal 0.65 presentation implied | Print `P(full-innings side | PP low/centre/high)` or an equivalent branch table whenever phase + innings markets share one batting unit. |
| Generic venue baseline too influential against current-regime ceiling | Venue history supported the Under but did not capture this India opening regime | Keep venue prior, but state the current-regime override branch and its mass explicitly. |
| Full Afghanistan XI was not independently captured pre-cutoff | Limited precise bowling-phase allocation | Continue marking the missingness; do not invent an XI. If publicly released before cutoff, prioritize the board/official match centre. |
| Dropped chance at 4.3 overs | Samson survived and India accelerated | Treat as realized variance, not a pre-game analytical failure unless a fielding-quality mechanism had been available and quantified. |

##### H. Mandatory validation questions

1. **Confirmed starting XIs before issue?** India was substantially confirmed; a full independently captured official Afghanistan XI was **not** recovered before cutoff. Post-match scorecards show the participants, but that does not backfill pre-game certainty.
2. **Bench/reserve information?** Not fully captured; less material than the playing XI for the two innings-phase contracts, but still a completeness gap.
3. **Coaching information?** Head coaches were recorded and no post-match evidence indicates a coaching change drove the result.
4. **Injuries/rest/late changes?** Material India squad changes and Varun/Harshit context were checked; no hindsight-only availability fact is treated as a pre-game miss without proof it was public before cutoff.
5. **Were original sources accurate/current?** Mostly yes for fixture, toss and series form. The copied prompt’s stale alternative lines were correctly rejected.
6. **Better sources available?** ICC/board sources remain preferred for identity/result. A structured scorecard is useful for exact powerplay states when the official narrative lacks a full phase table.
7. **Blind spots?** The principal one was joint phase-to-innings conditioning, not event identity.
8. **Future fix?** Add a state-conditional innings budget whenever a phase market and a full-innings market share the same scoring process.

##### I. Source audit / settlement evidence

| Source | Settlement contribution | Assessment |
|---|---|---|
| ICC — `Sensational Abhishek blazes to record hundred` — https://www.icc-cricket.com/news/sensational-abhishek-blazes-to-record-hundred | Official report: record hundred, dismissal just before halfway, **100-run powerplay** | Primary/high-authority narrative; strong for phase mechanism |
| NDTV structured scorecard — https://sports.ndtv.com/apps/cricket/live-scores/afin09172026273950?template=scorecard | **221/7**, **94 all out**, 127-run win, mandatory PP **100/0**, 142/1 at 9.5, 201/4 at 17 | Structured secondary; highly useful exact phase settlement fallback |
| Indian Express post-match report | 221/7, 127-run win, Abhishek 108 and opening partnership context | High-quality secondary corroboration |
| Original BCCI / ACB / ICC pre-game sources listed above | Squad, fixture, series context | Remain appropriate pre-game field-owner sources |

**Source-quality disposition:** no source is promoted solely because it agreed on this match. Official ICC/board remains the first lane; structured scorecard providers remain corroboration/fallback for exact phase fields.

##### J. Learning / rule disposition

- **Existing rule worked:** `G-L20` direct comparable treatment correctly supported Rank #1.
- **Candidate learning:** `C-CRIC-PHASE-CONDITIONAL-INNINGS` — when a phase target and full-innings target share the same innings, print conditional full-innings states under low/central/high phase outcomes before ranking. **Status: CANDIDATE / needs prospective testing.**
- **No permanent Over bias** and no retrospective probability refit.
- **Proposed document homes:** `RULES_CRICKET.md` (process clarification if eventually adopted), `LEARNING_REGISTER.md` (candidate/test manifest), and `RULES_GENERAL.md` only if later evidence shows the conditional-dependence issue is genuinely cross-sport.

---

### P-453 — Baseball / MLB — Milwaukee Brewers @ Pittsburgh Pirates

- **Canonical ID:** P-453 (mini-log sequence; combined-log reconciliation pending)
- **Sport / competition:** Baseball — MLB, 2026 regular season
- **Event:** Milwaukee Brewers @ Pittsburgh Pirates
- **Venue:** PNC Park, Pittsburgh, Pennsylvania
- **Scheduled start:** 17 Sep 2026, 12:35 PM EDT = 18 Sep 2026, 02:35 AEST (Australia/Melbourne)
- **Game state at issue:** **PREGAME** — latest current-state check still showed pre-game; no pitch had been thrown.
- **Research cutoff / final refresh:** 18 Sep 2026, **02:17:31 AEST** / 17 Sep 2026, **12:17:31 PM EDT**
- **Method version:** MDS-2026.09.06-v4.0
- **Population status:** **PRIMARY_SCORED — MLB**, but controlling user direction remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.
- **Operating mode:** SPORTS_ONLY / MARKET_BLIND. User-supplied thresholds define contracts only; no price/odds/market movement entered the forecast.

#### Identity / contract validation

- Official MLB schedule/probable-pitcher pages confirm **Milwaukee Brewers @ Pittsburgh Pirates**, PNC Park, 12:35 PM EDT.
- Official probable pitchers: **Kyle Harrison (MIL, LHP)** and **Wilber Dotel (PIT, RHP)**.
- Important role correction: latest reporting says **Dotel is the opening pitcher, not a conventional starter**, with **Khristian Curtis available as the likely multi-inning bulk arm**. The card therefore models PIT as **Dotel opener → Curtis bulk → middle/leverage relief**, not as a six-inning Dotel start.
- Supplied contracts frozen exactly as: **PIT +1.5**, **MIL -1.5**, **Over 8.5**, **Under 8.5**.
- No operator-specific listed-pitcher/suspension/action rules were supplied. Weather/shortening settlement is therefore **UNKNOWN_DEFINITION**; forecast probabilities below are conditional on ordinary MLB action/full-game settlement.

#### Latest lineups / availability

**Latest secondary-confirmed batting orders (official MLB starting-lineup page had not yet populated the orders at cutoff):**

**Milwaukee:** Brice Turang 2B (L), Luis Lara CF (S), Jackson Chourio LF (R), Andrew Vaughn 1B (R), Gary Sánchez DH (R), Joey Ortiz SS (R), Sal Frelick RF (L), Bo Naylor C (L), David Hamilton 3B (L).

**Pittsburgh:** Konnor Griffin SS (R), Oneil Cruz CF (L), Bryan Reynolds LF (S), Rafael Flores 1B (R), Brandon Lowe 2B (L), Nick Gonzales DH (R), Ronny Simon RF (S), Jared Triolo 3B (R), Henry Davis C (R).

- **Milwaukee rests several regulars from the starting nine:** William Contreras, Christian Yelich, Jake Bauers and Cooper Pratt are absent from the reported starting order. This is a material reduction in Milwaukee's separation/offensive-ceiling branch versus its normal lineup.
- Pittsburgh is without OF **Esmerlyn Valdez** (hamstring, IL), SP **Braxton Ashcraft** (right arm discomfort, IL), RP **Isaac Mattson** (hip impingement, IL), RP **Kirby Yates** (right shoulder impingement, IL at latest official update), and C/1B **Endy Rodríguez** (hip, 60-day IL). Ashcraft's absence is the reason Pittsburgh is piecing this game together with an opener/bulk arrangement.
- Milwaukee pitching absences include **Brandon Woodruff** (60-day IL, shoulder capsule) and **Grant Anderson** (15-day IL, biceps); Bryse Wilson was on rehab from a back strain at the latest official update.

**Participant-status grade:** Harrison and Dotel are **PROBABLE_OFFICIAL** from MLB field-owner pages; lineups are **SECONDARY_CONFIRMED / OFFICIAL_LINEUP_NOT_POPULATED_AT_CUTOFF**, so no hitter prop is introduced and lineup-dependent conclusions remain slightly capped.

#### Starting-pitcher and bulk-relief research

**Kyle Harrison, MIL**
- Season: **10-4, 3.98 ERA, 110.2 IP, 134 SO**.
- Last seven: **7.00 ERA in 27 IP**, 42 H, 21 ER, 13 BB, 33 K — the current deterioration is not just an ERA narrative.
- Required disaggregated last-three log: **Aug 31 @ CHC: 3.2 IP, 10 H, 9 ER, 2 BB, 3 K; Sep 6 @ CIN: 3.2 IP, 9 H, 4 ER, 4 BB, 4 K; Sep 12 vs CIN: 0.0 IP, 4 H, 4 ER, 0 BB, 0 K.** That is **17 ER in 7.1 IP**, with a genuine recent command/contact problem rather than a front-loaded noisy aggregate.
- Counter-evidence is unusually strong and opponent-specific: Harrison is **2-0 with a 0.00 ERA and 29 K in 17 career innings vs Pittsburgh**, and Baseball Savant's current-roster sample is **39 PA, .135 AVG, .168 wOBA, 53.8% K, 5.1% BB, .167 xwOBA**. The sample is small and cannot erase the last-three-start collapse, but it is a real matchup branch.
- Brewers manager Pat Murphy explicitly said the club has enough pitching behind Harrison to protect the game if he starts slowly. This reduces the probability that one bad Harrison inning automatically becomes six-plus innings of starter exposure; it shifts some risk into the relief transition instead.

**Wilber Dotel / Khristian Curtis, PIT**
- Dotel season: **1-5, 4.84 ERA, 35.1 IP, 36 SO**; only **one prior MLB start**.
- Last three MLB appearances: **Sep 15 vs MIL 0.2 IP, 1 H, 0 ER, 0 BB, 1 K; Sep 11 @ CHC 2.0 IP, 4 H, 3 ER, 0 BB, 1 K; Sep 8 @ CWS 2.0 IP, 2 H, 1 ER, 0 BB, 1 K.**
- Dotel has not covered more than three innings in any MLB/minor-league outing since May 10. He is therefore an opener by role, not a normal starter.
- **Curtis** is expected to be available on six days' rest for multiple innings after Dotel. The comparable rookie chain of Dotel + Curtis + Antwone Kelly allowed **12 runs in eight innings** to Chicago on Sep 11, but that single game is a tail/context example rather than a fitted Over coefficient.
- Baseball Savant's Dotel-vs-current-MIL sample is only **12 PA**; the observed .364 AVG conflicts with a much lower .148 xBA/.199 xwOBA. It is too small to own the centre and is treated as width.

#### Bullpen / workload state

- Milwaukee used **JoJo Romero, Antonio Senzatela, Shane Drohan, Abner Uribe and Trevor Megill** in the previous night's 5-4 win. Reported pitch counts were modest for most arms (14, 14, 11, 6, 8 respectively), so this is not a blanket “bullpen unavailable” state, but the whole late-game chain is not maximally fresh.
- Pittsburgh used **Yohan Ramírez (16 pitches), Carmen Mlodzinski (38) and Camilo Doval (11)** the previous night. Mlodzinski's 38-pitch workload is the clearest availability downgrade for today's middle-relief ladder.
- Pittsburgh still has fresher late-game options such as Mason Montgomery/Luke Weaver/Gregory Soto available in the broader active bullpen, so the Dotel/Curtis early-inning uncertainty should not be treated as nine innings of poor relief quality.

#### Team / matchup context

- Milwaukee enters **95-57**; Pittsburgh **75-77**.
- Baseball-Reference's current split snapshot has Milwaukee **60-43 vs RHP** and Pittsburgh **16-32 vs LHP**. The Pittsburgh lefty split supports Harrison's matchup branch, but the current lineup and Harrison's deterioration prevent using it as a deterministic side adjustment.
- Milwaukee won the first two games of this series **5-1 and 5-4**. Per the Drive controls, those results themselves receive no directional weight; their useful information is the bullpen workload, today's Milwaukee lineup rotation, and the Pirates' continued opener/bulk necessity.
- PNC Park's 2026 one-year Baseball-Reference park factor is **113** (over 100 favors hitters), while the multi-year factor is **105**. This supports a non-pitcher-friendly context, but is not a substitute for control 35's exact current-season PNC distribution at 8.5.

#### Weather / environment

- Government forecast around game time: warm/humid with showers and thunderstorms possible; roughly **79–83°F (26–28°C)** in the early afternoon, humidity around the upper-70s/low-80s, and light west wind around **6–8 mph**.
- Rain probability was materially elevated around/after first pitch, with the forecast improving through the afternoon. Current baseball-weather monitoring still listed the game as **not delayed/postponed** at the final check.
- Mechanistic treatment: rain is **not an automatic Under**. A delay can shorten Harrison/Dotel/Curtis exposure, change the named relief chain, or create inherited-runner/relief-transition variance. It therefore widens the run distribution and adds an early-hook branch.

#### Control 35 venue-rate limitation

- The active Drive base-rate register does **not yet contain PNC Park's exact 2026 `P(>8.5) / P(<8.5)` distribution**; PNC is one of the 22 parks marked `NOT_YET_DERIVED`.
- An accessible field-owner season query sufficient to recompute the exact PNC 8.5 distribution was not recovered before cutoff. Therefore the total rows carry **`PNC_8.5_BASE_RATE_NOT_DERIVED`** and are capped at **FORCED RANK / MEDIUM-LOW** evidence.
- League reference only: 2026 MLB mean/median total through Sep 16 is **8.98 / 8**, SD **4.53**. This anchors width/scale, not a venue-specific direction.

#### Joint event object / arithmetic

**Winner centre:** Milwaukee **0.59**, Pittsburgh **0.41** (`UNVALIDATED_SUBJECTIVE`).

The Milwaukee edge comes from team-strength gap, Pittsburgh's 16-32 record vs LHP, Harrison's direct matchup history, and the Dotel→Curtis opener/bulk uncertainty. It is pulled down by Harrison's back-loaded three-start collapse, Milwaukee's heavily rotated batting order, Pittsburgh home last-bat, and weather/relief-chain uncertainty.

**Run-line identity (`G-L24` / baseball control 34):** Brewers season win% ~.625 vs Pirates ~.493 gives a winner-minus-loser season-W% gap around **+0.13**, so the current 2026 `+0.1` MLB cushion band is **r = 0.268** (base-rate register, n=2,286 league games through Sep 16).

- `P(MIL -1.5) = 0.59 × (1 - 0.268) = 0.432 ≈ 0.43`
- `P(PIT +1.5) = 0.41 + 0.59 × 0.268 = 0.568 ≈ 0.57`

This is why the protected Pittsburgh side can rank above Milwaukee -1.5 **while Milwaukee remains the projected winner**.

**Game-total centre:** approximately **9.0 runs**, width **~4.5 runs**. Normalised edge versus 8.5 is only **|9.0-8.5| / 4.5 ≈ 0.11**, so this is a narrow total lean, not a strong call.

Drivers upward: Dotel/Curtis early exposure, Harrison's last-three collapse, PNC's hitter-favouring 2026 park factor, warm/humid conditions, relief-transition/delay risk.

Drivers downward: Milwaukee's rotated lineup, Harrison's historically excellent PIT matchup/current-roster contact profile, Pittsburgh's weak season record vs LHP, and the availability of competent back-end relief once the rookie bulk phase ends.

**Discrete final-state family (conditional on ordinary game action):**

| State | Mass |
|---|---:|
| MIL wins by 2+ & total Over 8.5 | 0.21 |
| MIL wins by 2+ & total Under 8.5 | 0.22 |
| MIL wins by exactly 1 & total Over 8.5 | 0.08 |
| MIL wins by exactly 1 & total Under 8.5 | 0.08 |
| PIT wins & total Over 8.5 | 0.24 |
| PIT wins & total Under 8.5 | 0.17 |
| **Total** | **1.00** |

This yields exactly: **PIT +1.5 0.57; MIL -1.5 0.43; Over 8.5 0.53; Under 8.5 0.47.**

- **P(Rank #1 AND Rank #2) = 0.32** (PIT +1.5 and Over 8.5 both win).
- **P(neither preferred decision wins) = 0.22** (MIL wins by 2+ in an 8-or-fewer-run game).
- Representative Rank-#1 compatible outcome: **MIL 5-4 PIT** — Milwaukee wins, Pittsburgh +1.5 wins, Over 8.5 wins.
- 2026 MLB tie-after-nine/extras base rate is **8.75%**; extras materially favour the +1.5 geometry because 68.5% of extras games finish by one run. This endpoint effect is already reflected in the league-derived cushion identity rather than double-counted as a separate bonus.

#### Ranked picks

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence | Geometry | Why this rank | Main failure path |
|---:|---|---:|---|---|---|---|
| **1** | **Pittsburgh Pirates +1.5** | **0.57** | MEDIUM | FORCED_PAIR preferred side | Derived directly from MIL win p=0.59 and current MLB one-run band r=0.268. Milwaukee's rested bats and Pittsburgh's home last-bat increase the credibility of the one-run/PIT-win branches. | Harrison's PIT matchup dominance returns while Dotel/Curtis fail early, producing a 4-1/5-2/6-2 MIL separation game. |
| **2** | **Combined Total OVER 8.5** | **0.53** | FORCED RANK / MEDIUM-LOW | FORCED_PAIR preferred side | Centre ~9.0; both pitching plans carry short-start/relief-transition tails, and weather can force another transition. PNC is hitter-friendly by 2026 park factor. | Rotated MIL lineup plus Harrison's direct PIT suppression produces a 4-2/5-2/4-3 type game; exact PNC 8.5 venue rate not derived. |
| **3** | **Combined Total UNDER 8.5** | **0.47** | FORCED RANK / MEDIUM-LOW | FORCED_PAIR non-preferred side | Strong Harrison-vs-PIT history/current-roster sample and a weakened MIL lineup keep the lower branch substantial. | Either Harrison's current collapse persists or the PIT opener/bulk chain yields an early crooked inning; relief transition then pushes total to 9+. |
| **4** | **Milwaukee Brewers -1.5** | **0.43** | MEDIUM | FORCED_PAIR non-preferred side | Milwaukee is the projected winner, but MLB's one-run geometry and the rested MIL lineup make a two-plus-run win materially less likely than a win outright. | PIT wins outright or loses by exactly one; extras especially compress final margins. |

**Decision interpretation:** this slate is **two forced-pair decisions, not four independent picks**. Preferred decisions: **PIT +1.5** and **Over 8.5**.

#### Projected match winner

- **Projected winner: Milwaukee Brewers**
- **Winner endpoint:** eventual MLB game winner including extra innings, conditional on the game being played to an actionable result under operator rules.
- **Probability:** **0.59 `UNVALIDATED_SUBJECTIVE`** (Pittsburgh 0.41).
- Reasoning: Milwaukee remains the stronger overall team, has the better season matchup against the handedness it faces, and Pittsburgh's opener/bulk plan is a larger pitching-depth uncertainty. The margin is deliberately modest because Harrison's last three starts are genuinely poor, Milwaukee is resting major bats, and Pittsburgh has home last-bat.

#### Information not confirmed / integrity flags

- Official MLB lineup page still showed **TBD** batting orders at cutoff; the detailed orders above are secondary-confirmed and not upgraded to `CONFIRMED_OFFICIAL`.
- Dotel remains the official MLB probable pitcher, but current reporting establishes an **opener role** and Curtis as likely bulk; the analysis models that role rather than silently treating Dotel as a conventional starter.
- Exact operator listed-pitcher, suspension and rain-shortening action terms not supplied (`UNKNOWN_DEFINITION`).
- Exact PNC Park 2026 total distribution at 8.5 was not recoverable to the current Drive standard (`PNC_8.5_BASE_RATE_NOT_DERIVED`), so total rows are evidence-capped.
- Umpire was not announced/recovered before cutoff; under the 2026 ABS challenge environment, no unsupported umpire-zone adjustment is used.
- No retrospective or settlement performed.
- **Current settlement status:** **UNSETTLED — PREGAME AT ISSUE**.

#### Settlement routes pre-registered

- Final score/run line/game total: **MLB StatsAPI / MLB Gameday official final**.
- Extra-innings/regulation split if material: MLB linescore/box score.
- Pitcher usage and lineup identities at settlement: MLB official box score / Statcast where needed.

#### Sources

| Source | Link / record | Contribution | Quality / limitation |
|---|---|---|---|
| MLB probable pitchers | https://www.mlb.com/probable-pitchers | Official fixture, start time, Harrison/Dotel probable-pitcher identities | Primary / field owner |
| MLB Brewers/Pirates starting-lineup pages | https://www.mlb.com/starting-lineups | Official schedule and prior lineup; today's batting orders still TBD at cutoff | Primary but incomplete for today's order |
| Baseball Savant probable pitchers | https://baseballsavant.mlb.com/probable-pitchers | Harrison vs current PIT roster; Dotel vs current MIL roster Statcast samples | Primary data partner; small samples |
| MLB Kyle Harrison player page / Savant | https://www.mlb.com/player/kyle-harrison-690986 ; https://baseballsavant.mlb.com/savant-player/kyle-harrison-690986 | Season + last-seven + last-three disaggregated starts | Primary/statistical |
| MLB Wilber Dotel player page / Savant | https://www.mlb.com/player/wilber-dotel-696062 ; https://baseballsavant.mlb.com/savant-player/wilber-dotel-696062 | Season, role, last-three usage | Primary/statistical |
| MLB game preview | https://www.mlb.com/stories/game-preview/823334 | Harrison's 2-0, 0.00 ERA, 29 K/17 IP career record vs PIT | Primary editorial citing MLB record |
| MLB Brewers article, 17 Sep | https://www.mlb.com/news/christian-yelich-brewers-beat-pirates-for-95th-win | Harrison 17 ER/7.1 IP last 3; Murphy bullpen-protection plan | Primary team/league reporting |
| RotoWire daily lineups | https://www.rotowire.com/baseball/daily-lineups.php | Latest secondary-confirmed batting orders; Curtis marked primary/bulk | Secondary; not field owner |
| RotoWire Dotel report | https://www.rotowire.com/baseball/headlines/wilber-dotel-news-opening-thursdays-contest-1025896 | Dotel opener role; Curtis multi-inning availability; workload ceiling | Secondary, named reporter lineage |
| MLB Pirates injury page | https://www.mlb.com/pirates/news/pirates-injuries-and-roster-moves | Valdez, Ashcraft, Mattson, Yates, Endy Rodríguez availability | Primary |
| MLB Brewers injury page | https://www.mlb.com/cubs/news/brewers-injuries-and-roster-moves | Woodruff, Wilson, Anderson availability | Primary content on MLB domain; unusual URL path noted |
| MLB Pirates rookie-pitching report | https://www.mlb.com/news/wilber-dotel-khristian-curtis-antwone-kelly-allow-12-runs-to-cubs | Dotel/Curtis/Kelly prior bulk-game failure context | Primary team/league reporting; one game only |
| Reuters, 17 Sep | https://www.reuters.com/sports/baseball/christian-yelich-comes-through-clutch-brewers-nip-pirates--flm-2026-09-17/ | Prior-night final and bullpen usage context | High-quality secondary |
| Baseball-Reference Sep 17 preview | https://www.baseball-reference.com/previews/2026/PIT202609170.shtml | Team handedness split records and series context | Statistical secondary; snapshot showed slightly stale overall records but split structure useful |
| Baseball-Reference PIT 2026 | https://www.baseball-reference.com/teams/PIT/2026.shtml | PNC one-year/multi-year park factors | Statistical secondary |
| U.S. National Weather Service point forecast | weather.gov point/hourly forecast for Pittsburgh/PNC area | Government game-window temperature, precip, humidity, wind | Government field owner for weather |
| RotoWire MLB weather | https://www.rotowire.com/baseball/weather.php | Current operational delay/rainout check; no delay/rainout flagged | Secondary monitoring only |
| Drive `RULES_BASEBALL.md` | Sports Research Drive | Controls 24–37, starter log, opener/bulk, relief chain, total/run-line geometry | Governing methodology |
| Drive `BASE_RATES_REGISTER.md` | Sports Research Drive | 2026 MLB one-run band, extras rate, league total width; PNC exact rate marked not derived | Governing quantitative identity input |
| User-supplied market slate | Current query | Exact +1.5/-1.5 and O/U 8.5 contracts | Contract source only |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| Dotel listed as probable starter but functionally opener with Curtis bulk | `RULES_BASEBALL.md` starter-role / BB-S2–S4 | Existing role control correctly applied; **NO CHANGE** |
| Harrison season history vs PIT conflicts sharply with last-three current regime | `RULES_BASEBALL.md` controls 13/24 + `G-L2/G-L7` | Existing mixture/disaggregation controls correctly applied; **NO CHANGE** |
| Milwaukee resting four regular bats materially affects separation before winner direction | `RULES_BASEBALL.md` control 27 / G14.2 | Existing PA/lineup control correctly applied; **NO CHANGE** |
| Exact PNC 8.5 venue base rate absent from register | `BASE_RATES_REGISTER.md` §3 | **DATA GAP / future derivation candidate**, not a rule change |
| Rain threatens pitcher-role continuity more than it supplies a one-sign total lean | `RULES_BASEBALL.md` control 18 | Existing control correctly applied; **NO CHANGE** |


---

#### Settlement and retrospective — 18 Sep 2026

- **Final status:** `SETTLED — FINAL`.
- **Final result:** Pittsburgh Pirates **7**, Milwaukee Brewers **4**.
- **Canonical-ID audit:** no P-453 entry exists in `PREDICTION_LOG_COMBINED_4.md`; no collision was found.
- **Original prediction preserved:** the pre-game card above remains frozen.

##### A. Ranked-pick and winner settlement

| Rank | Frozen selection | Final target | Result | Settlement note |
|---:|---|---:|---|---|
| 1 | Pittsburgh Pirates **+1.5** | PIT won 7-4 | **WIN** | Covered outright; cushion not needed. |
| 2 | Combined **Over 8.5** | **11 runs** | **WIN** | Cleared by 2.5. |
| 3 | Combined **Under 8.5** | 11 | **LOSS** | Exact complement of Rank #2. |
| 4 | Milwaukee Brewers **-1.5** | MIL lost by 3 | **LOSS** | Failed outright and on margin. |
| — | Projected winner: **Milwaukee** | Pittsburgh won | **LOSS** | Winner projection wrong. |

**Top-of-list diagnostics:** Rank #1 = **WIN**; Wins@2 = **2**; Hit@2 = **1**; both top two won = **YES**; NDCG@2 = **1.000**. The top two were dependent through the state in which Pittsburgh generated enough offense to stay inside +1.5 while pitching uncertainty raised total variance; this is a learning-only scorecard.

##### B. Why each pick won or lost

**Rank #1 — Pittsburgh +1.5: WIN.** The card’s strongest protection was not merely generic one-run MLB geometry. It explicitly recognized Kyle Harrison’s severe current deterioration: the prior three outings had produced 17 earned runs in 7.1 innings. That current-regime warning proved more important than his excellent historical Pittsburgh matchup. Harrison lasted only 1.2 innings and was charged with four earned runs; Pittsburgh scored five in the second and never surrendered the lead. The protected home side therefore had a much broader winning region than Milwaukee -1.5.

**Rank #2 — Over 8.5: WIN.** The Over was supported by the Harrison failure branch plus Pittsburgh’s opener/bulk uncertainty and relief-transition width. The realized path was asymmetric: the largest early damage came against Harrison, while Dotel/Curtis were much better than the pessimistic Pittsburgh pitching tail. Pittsburgh later added a two-run Henry Davis homer in the eighth, taking the game to 11. Thus the total call succeeded even though only one of the two starting-plan risk branches broke badly.

**Rank #3 — Under 8.5: LOSS.** The Under case depended on Harrison’s historically strong Pittsburgh matchup and Milwaukee’s rotated lineup suppressing scoring. Milwaukee’s lineup did show some conversion weakness, but Pittsburgh’s five-run second inning made the Under’s remaining path too narrow.

**Rank #4 — Milwaukee -1.5: LOSS.** It required the projected stronger team to separate. Milwaukee instead trailed by four after two innings. The pre-game card correctly warned that Harrison’s recent collapse could produce a 4-1/5-2/6-2 Pittsburgh-type state; the failure path occurred on the wrong side of the Milwaukee margin.

**Projected Milwaukee winner: LOSS.** This is the key forecast miss on the card. Team-strength prior, Pittsburgh’s poor season split against left-handers and Harrison’s career dominance of Pittsburgh were overweighted relative to the recency evidence. The official post-game MLB report now puts Harrison at a 21.00 ERA over his last four outings, confirming the deterioration was not a one-start aberration.

##### C. Rank-1 review

Rank #1 won, so no failure-triggered deep review is required. Its placement was justified and more robust than the outright winner label. The important lesson is that **side contract and projected winner were correctly allowed to disagree**: Pittsburgh +1.5 was stronger than Milwaukee to win.

##### D. Top-two review

Both top selections won. Their ordering was reasonable: Pittsburgh +1.5 had the broadest win region because it won under a Pittsburgh victory and a one-run Milwaukee victory. The Over required an additional scoring condition. This is a useful example of the separation/total decomposition working correctly.

##### E. Over/under review

The 11-run final supports the Over result, but it should not be turned into an unconditional PNC Over rule. The game crossed 8.5 because the Harrison collapse produced a five-run Pittsburgh inning and a late two-run homer extended the margin. The opener/bulk risk did **not** explode: Curtis earned the win with 3.1 innings and one earned run. Future totals should continue separating each starter/bulk path instead of adding every uncertainty as same-sign Over evidence.

##### F. What went right

- Harrison’s recent workload/results were disaggregated rather than hidden behind season ERA.
- Dotel was modeled as an opener and Curtis as bulk, not as a conventional starter.
- Milwaukee lineup rotation was identified and correctly reduced the favorite’s separation ceiling.
- Run-line geometry allowed Pittsburgh +1.5 to rank above the Milwaukee winner call.
- Exact final MLB lineup records show the secondary pre-game batting orders were accurate.

##### G. Blind spots and smallest fixes

| Blind spot | Effect | Future treatment |
|---|---|---|
| Historical Harrison-vs-PIT success retained too much winner weight | Milwaukee winner lost despite severe current-regime collapse | When current disaggregated deterioration is extreme and mechanistically supported, run an explicit “career matchup reversion vs current regime persists” mixture and print the weights. |
| Team-strength prior and starter current state not reconciled tightly enough | Winner label remained MIL while Rank #1 correctly leaned PIT cushion | Require winner narrative to pass the same strongest-kill-path audit as ranked rows; do not let the winner label inherit a stale stronger-team prior. |
| Official lineups were unavailable at the frozen pre-game cutoff | Secondary order was used | Keep secondary-confirmed status; when official lineup posts before first pitch, use a final refresh if still pre-start. Do not backfill it after play. |
| PIT five-run second included traffic/error-type conversion beyond pure contact | Large early scoring swing | Treat inning sequencing as variance unless a pre-game walk/defense mechanism was specifically supported. |

##### H. Mandatory validation questions

1. **Confirmed starting lineups before issue?** No field-owner order was available at the frozen cutoff; secondary orders were used. MLB’s final lineup record now confirms those orders were accurate, but that is post hoc verification.
2. **Bench/reserves?** Not fully field-owner captured pregame.
3. **Coaching/manager info?** Manager comments on Harrison protection were captured and materially relevant.
4. **Injuries/rest/rotation?** Yes, major Brewers rest and both teams’ pitching absences/workload were researched.
5. **Original sources accurate/current?** Generally yes. The largest analytical miss was weighting, not stale identity data.
6. **Better future sources?** MLB starting-lineup pages and MLB Gameday should remain first choice once populated; secondary lineup services remain fallback only.
7. **Blind spots?** Current-regime starter risk was known but still underweighted in the projected winner.
8. **Future fix?** Explicit regime-mixture weighting and winner-label kill-path audit.

##### I. Source audit / settlement evidence

| Source | Contribution | Assessment |
|---|---|---|
| MLB scoreboard — https://www.mlb.com/scores/2026-09-17 | Official final **PIT 7-4 MIL** | Primary / field owner |
| MLB Film Room game 823334 — https://www.mlb.com/video/game/823334 | Line score; Curtis 3.1 IP/1 ER; Harrison 1.2 IP/4 ER | Primary |
| MLB Harrison post-game report — https://www.mlb.com/news/kyle-harrison-struggles-brewers-postseason-role | Harrison’s continuing current-regime collapse, now 21.00 ERA over four outings | Primary league/team reporting |
| MLB Brewers starting-lineup archive | Final batting orders | Primary; also verifies the pregame secondary lineup happened to be correct |
| MLB Henry Davis highlight | Two-run eighth-inning HR that extended PIT to seven | Primary event evidence |

##### J. Learning / rule disposition

- **Existing controls were directionally correct:** disaggregate current starter form; model opener/bulk roles; separate winner and cushion.
- **Process weakness:** projected-winner weighting did not give enough mass to a known severe current-regime starter branch.
- **No new rule yet.** Record as a candidate example under `RULES_BASEBALL.md` current-regime mixture / `G-L23` result-vs-process review and `LEARNING_REGISTER.md` if the same weighting error repeats prospectively.
- No source is newly promoted based on one successful verification.

---

### P-454 — Soccer / Denmark DBU Pokalen (Betano Pokalen) — Vejle Boldklub vs Brøndby IF

- **Canonical ID:** P-454
- **Sport / competition:** Soccer — Denmark DBU Pokalen / Betano Pokalen 2026/27, Round 3
- **Event:** Vejle Boldklub vs Brøndby IF
- **Official event identity:** DBU match no. **486247**, Round 3
- **Venue:** Vejle Stadion, Vejle, Denmark
- **Scheduled start:** 17 Sep 2026, 18:30 CEST = 18 Sep 2026, 02:30 AEST (Australia/Melbourne)
- **Game state at issue:** **PREGAME**
- **Research cutoff / final volatile refresh:** **18 Sep 2026, 02:24:06 AEST / 17 Sep 2026, 18:24:06 CEST** — six minutes before scheduled kickoff. No live/post-start information is used in this card.
- **Method version:** MDS-2026.09.06-v4.0
- **Population status:** **EXPLORATORY — NOT SCORED** for primary-performance purposes; LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under current user direction.

#### Identity / competition / contract freeze

- DBU's official match page confirms **Vejle Boldklub vs Brøndby IF**, Betano Pokalen 2026/27, Round 3, at Vejle Stadion, 17 September 18:30 local time.
- `LEAGUE_RULES_SOCCER.md` §4.11 already documents the DBU Pokalen, so this is **not** an undocumented new-competition onboarding case. The competition is single-elimination; tied knockout matches proceed through extra time and, if still level, penalties. DBU 2026/27 match records independently demonstrate this mechanism in earlier rounds.
- **90-minute markets** in this card stop at the end of regulation plus stoppage time and **exclude** extra time / penalties unless explicitly labelled as an advancement market.
- User-supplied goal contracts frozen exactly as **1st-half O/U 0.5 goals** and **90-minute total O/U 2.5 goals**.
- Self-selected markets below are explicitly defined as regulation-time markets unless stated otherwise.

#### Participants / squads / availability

**Brøndby — official match squad retrieved:** 21 players: Patrick Pentz, Adrian Kappenberger, William Sonne-Schmidt, Oliver Villadsen, Christopher Olivier, Luis Binks, Olti Hyseni, Patrick Mortensen, Daniel Wass, Filip Bundgaard, Casper Winther, Max Ejdum, Sho Fukuda, Marcus Younis, Marko Divkovic, Mats Köhlert, Mads Frøkjær, Jordi Vanlerberghe, Raphael Canut, Jacob Ambæk and Bartosz Slisz.

- **Jacob Ambæk returns to the squad after roughly a month / four matches out injured.** This increases Brøndby's attacking bench ceiling but his exact minutes and sharpness are uncertain.
- **Luis Binks returns** after missing the previous league game through suspension.
- **Frederik Alves and Oskar Fenger drop out** relative to the prior Brøndby squad.
- The official club source did **not** publish the starting XI in the retrievable page before the 02:24 AEST cutoff.

**Vejle — lineup status:** a final official starting XI / full bench was **not retrieved before cutoff**. The last official Vejle league XI (0-0 at Hobro on 11 Sep) was Nicolai Larsen; Johan Karlsson, Gunnar Vatnhamar, Lasse Nielsen, Christian Sørensen; Lundrim Hetemi, Mathias Jensen; Tobias Bach, Mikkel Duelund, Gustav Marcussen; Lucas From, with a bench including Kasper Kristensen, Thomas Gundelund, Valdemar Lund, Mike Vestergård, Wahid Faghir, Abdoulaye Camara, Max Jensen, Nicolas Gammelgaard and Bismark Edjeodji.

- A secondary lineup site listed several injuries/suspensions for both clubs, but that page demonstrably conflicted with Brøndby's official match squad (for example it marked players unavailable who were named by the club). Those secondary availability labels are therefore **not promoted to fact** and are excluded from signed adjustments.
- **Participant-completeness limitation:** exact XIs/benches were not fully confirmed for both sides. Under the governing controls, this blocks a margin/full-game-total row from being Rank #1 and lowers evidence quality on rotation-sensitive markets.

#### Current form / process evidence

**Vejle**
- Enter after a **0-0 away draw at Hobro** on 11 Sep. Their official report shows a full senior-strength XI and substitutions, but an inability to break down a deep defensive block.
- In this cup, Vejle have already beaten **TPI 3-0** and then **Silkeborg 3-0**. The Silkeborg win is directly relevant because it shows Vejle can eliminate Superliga opposition at this venue / in this competition, but one cup result is not treated as a forecast coefficient.
- Vejle's recent home corner record is unusually compressed: the secondary statistical record shows **12 consecutive home matches under 11.5 total corners**, including 2026 home totals of 9, 8, 10, 11 and 9 in several recent fixtures.

**Brøndby**
- Their last three league matches are **1-3 at Nordsjælland, 0-3 vs Randers, 1-4 at Midtjylland**: three straight defeats, 10 goals conceded.
- The *mechanism* matters more than the streak: the official reports document Brøndby conceding after **4 minutes** to Randers and after **45 seconds**, then again at 23 minutes, against Midtjylland. That is direct recent evidence of first-half defensive instability, not simply a narrative losing run.
- Brøndby remain the higher-tier side and have a stronger senior attacking squad than Vejle, but recent defensive control is materially poor.
- Recent Brøndby corner totals from a secondary statistical database: 8 at Midtjylland, 13 vs Randers, 9 at Nordsjælland, 13 vs Silkeborg, 11 vs SønderjyskE, 9 at Horsens, 11 vs Viborg. Away first-half corner output has been notably lower than home output in the available sample.

#### Head-to-head continuity

Recent senior competitive H2H is mixed rather than dominant:
- Vejle 2-1 Brøndby (Dec 2025) — **0-0 at half-time**, corners 1-6.
- Brøndby 2-1 Vejle (Aug 2025) — **2-1 at half-time** with goals at 8', 22', 29'; corners 3-5.
- Earlier 2025/2024 meetings include 2-2, 2-1 and 1-1.

Current squads/coaches and league status have changed enough that H2H is contextual only. It supports neither a deterministic first-half goal nor a one-sided winner projection.

#### Environment

- Venue-coordinate / local forecast at the pregame cutoff: approximately **14–15°C with light rain**, with shower/rain probabilities around the 50–60% range through the early match window.
- A second weather source was less aggressive on rain timing, so the exact rainfall intensity is uncertain.
- Mechanism treatment: rain/wet surface is **uncertainty width**, not an automatic Under. It can reduce clean passing/finishing but also increase defensive errors, slips and transition volatility.

#### Joint event object

**90-minute goal centre:** ~**2.7 goals**, wide uncertainty because of the tier gap, Brøndby's defensive instability, Vejle's cup resilience, rotation uncertainty and wet conditions.

Approximate regulation score-family masses (`UNVALIDATED_SUBJECTIVE`):
- 0–1 total goals: **25%**
- exactly 2 goals: **19%**
- exactly 3 goals: **24%**
- 4+ goals: **32%**

This implies `P(Over 2.5)` ≈ **0.56**, `P(Under 2.5)` ≈ **0.44**.

**First-half state:** `P(at least one first-half goal)` ≈ **0.68**. The strongest positive mechanism is Brøndby's repeated very-early concessions in the last two league defeats; the counter-state is Vejle's recent 0-0 and the prior Vejle-Brøndby H2H that was goalless at half-time.

**90-minute result family:**
- Vejle win: **0.27**
- Draw: **0.28**
- Brøndby win: **0.45**

Therefore **Brøndby or Draw (X2)** = **0.73** mathematically, but the row is evidence-capped below its raw marginal due unconfirmed final XIs and Brøndby's poor recent regime. Published row probability: **0.66** `UNVALIDATED_SUBJECTIVE`.

**Eventual advancement / projected winner:** conditional on a draw after 90, Brøndby are given a small quality/depth edge through extra time and penalties. Overall advancement state ≈ **Brøndby 0.60 / Vejle 0.40**.

**Representative Rank-#1 outcome:** HT **0-1**, FT **1-2 Brøndby**, total corners **10** (e.g. Vejle 4, Brøndby 6). This representative state is compatible with all five ranked selections.

#### Ranked picks

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Geometry | Why this rank | Primary failure path |
|---:|---|---:|---|---|---|---|
| **1** | **1st Half — OVER 0.5 goals** | **0.68** | MEDIUM | FREE supplied target | Brøndby's last two league defeats both featured extremely early concessions (4' and 1'), and the Midtjylland match had a second first-half goal by 23'. This is direct process evidence; 1H total is also less bench-dependent than a full-match margin/total with unconfirmed XIs. | Wet/slower game plus conservative cup opening; Vejle repeat their 0-0 first-half profile and Brøndby stabilise defensively. |
| **2** | **Total corners — UNDER 11.5 (90 min)** | **0.64** | MEDIUM-LOW | FREE self-selected derivative | Vejle's secondary statistical record shows 12 straight home matches below 11.5 corners; Brøndby's recent away totals are usually in the 8–9 range, with one 16-corner exception. The line allows a fairly normal 5-5 / 4-6 corner game. | Early goal creates sustained trailing-side pressure; repeated blocked crosses/clearances drive a 12+ corner match. |
| **3** | **Brøndby or Draw (X2), 90 minutes** | **0.66 raw / 0.63 published** | MEDIUM-LOW | FREE | Higher-tier squad, Binks and Ambæk back in the match squad, and Vejle's difficulty breaking down Hobro support Brøndby avoiding defeat; however Brøndby's three-game defensive collapse and Vejle's 3-0 cup win over Silkeborg prevent a stronger projection. | Brøndby's early-concession/duel problems persist and Vejle convert home-cup momentum into a regulation win. |
| **4** | **Brøndby team total — OVER 0.5 goals (90 min)** | **0.62** | MEDIUM-LOW | FREE | Brøndby scored in 4 of their last 5 league matches despite poor results and retain multiple senior attackers; Vejle's recent clean-sheet form pulls this well below a high-confidence team-goal pick. | Vejle reproduce the Hobro/Silkeborg defensive control and Brøndby's finishing remains poor. |
| **5** | **Total Combined Goals — OVER 2.5 (90 min)** | **0.56** | LOW-MEDIUM | FORCED_PAIR preferred side of supplied O/U | Brøndby's last five league games produced totals of 5, 3, 4, 4 and 5; the current defensive regime creates genuine 2-1/2-2/3-1 branches. Vejle have scored six goals in two cup matches. | Cup caution, rain, Vejle defensive resilience, and/or Brøndby rotation compress the match into 0-1, 1-1 or 2-0. |

**Supplied total complement:** `Under 2.5` ≈ **0.44** and is the non-preferred side of the supplied forced pair.  
**Supplied first-half complement:** `Under 0.5` ≈ **0.32** and is the non-preferred side of the supplied forced pair.

#### Coupling / shared-driver audit

- The scoring rows (#1, #4, #5) share an attacking/defensive-regime driver. Estimated **P(all three fail)** ≈ **0.14**. The representative all-fail family is **0-0 at HT, Brøndby held scoreless, final 0-0 / 1-0 / 2-0 Vejle**.
- Rank #1 (1H O0.5) and Rank #2 (corners U11.5) have only moderate coupling. A reasonable joint mass is ≈ **0.44**; an early goal can actually *reduce* corner accumulation if the leading team controls territory, but can also increase corners if the trailing side chases.
- No claim of calibrated joint probabilities is made.

#### Corner settlement route / integrity

- Corner row is pre-registered for **research-grade settlement** at the exact Sofascore match page, which advertises detailed corner statistics for this fixture, with TNT/Eurosport's exact-match statistics page as an independent secondary cross-check.
- DBU remains the field owner for event identity/result, but its match page has not been shown to publish the corner field. Therefore operator-action settlement remains separate from research-grade corner grading.
- If the two pre-registered corner providers conflict materially, the row remains `UNRESOLVED` until reconciled; it is not silently settled from an unregistered source.

#### Projected match winner

- **Projected eventual winner / qualifier: Brøndby IF — 60%** `UNVALIDATED_SUBJECTIVE`.
- **Vejle — 40%.**
- This is an **advancement** label including extra time / penalties if required, not a 90-minute moneyline selection.
- Brøndby's squad depth and higher-tier baseline give them the edge, but their recent defensive regime and Vejle's home cup performance keep this substantially below a dominant-favourite projection.

#### Information not confirmed / integrity flags

- Final official starting XIs were **not retrieved before the frozen cutoff**. No later live/post-start lineup information may be backfilled into this pregame card.
- Vejle full match-day bench was not confirmed at cutoff.
- Several secondary injury/suspension claims conflicted with official squad evidence and were excluded rather than silently adopted.
- Exact user sportsbook prices were not supplied and are not used. `NO VALUE DETERMINABLE` under the market-blind framework.
- Corner evidence is materially lower-quality than the official identity/result evidence; the corner pick is intentionally not Rank #1.
- Weather is treated as width because rain can have bidirectional effects on goals/corners.
- No retrospective or settlement performed.
- **Current settlement status:** `UNSETTLED — PREGAME AT ISSUE`.

#### Sources

| Source | Link / record | Contribution | Quality / limitation |
|---|---|---|---|
| DBU official match page | https://www.dbu.dk/resultater/kamp/486247_508655/kampinfo | Exact fixture, competition, round, venue, kickoff, match number | **Primary / field owner** |
| Google Drive `LEAGUE_RULES_SOCCER.md` §4.11 | Drive authoritative reference | DBU Pokalen format, regulation vs ET/penalty endpoint | Governing methodology reference |
| DBU 2026/27 completed cup records | e.g. match 852798 and other Round 1/2 records | Independent confirmation that tied cup matches use ET then penalties | **Primary / field owner** |
| Brøndby official squad | https://brondby.com/nyheder/herrer/2026/september/truppen-til-pokalkampen-ude-mod-vejle-boldklub | 21-player cup squad; Binks/Ambæk included; Alves/Fenger omitted | **Primary club source** |
| Campo | https://campo.dk/2026/09/17/mulig-comeback-til-broendby-angriber-i-pokalkamp/ | Ambæk return after four-match injury absence; Binks return context | Reputable secondary, squad corroborated by club |
| Brøndby official report vs Midtjylland | https://brondby.com/nyheder/herrer/2026/september/skuffende-4-1-nederlag-til-fc-midtjylland | 4-1 loss; goals conceded at ~1' and 23'; recent defensive mechanism | **Primary club report** |
| Brøndby official report vs Randers | https://brondby.com/nyheder/herrer/2026/september/skuffende-3-0-nederlag-til-randers-fc | 3-0 loss; conceded at 4'; pressure problems | **Primary club report** |
| Vejle official Hobro report | https://vejle-boldklub.dk/ny-nulloesning-paa-udebane/ | 0-0 result; latest official XI/bench; inability to break low block | **Primary club report** |
| Vejle official news / matchday status | https://vejle-boldklub.dk/nyt | Current cup context; Vejle beat TPI and Silkeborg to reach Round 3 | **Primary club source** |
| TNT/Eurosport exact match page | https://www.tntsports.co.uk/football/oddset-pokalen/2026-2027/vejle-bk-brondby-if_mtc21918035/live.shtml | Recent team results, H2H, exact-match stats route | Reputable secondary; not field owner |
| ESPN H2H match records | Brøndby-Vejle Aug 2025 and Vejle-Brøndby Dec 2025 | Goal timing, HT states, corners, shots | High-quality structured secondary; historical |
| Statz.ai Brøndby corners | https://statz.ai/team/brondby-if/corners | 2026/27 Brøndby corner-for/against and match-by-match totals | Specialist statistical secondary |
| FootyBets Vejle statistics | https://footybets.io/statistics/vejle/ | Vejle home under-11.5 corner sequence and recent totals | Lower-tier statistical secondary; used conservatively, not as sole source |
| Sofascore exact match page | https://www.sofascore.com/football/match/vejle-brondby-if/GAsxXb | Pre-registered corner/stat settlement route | Secondary; interactive exact-match field coverage advertised |
| Structured weather forecast for Vejle | Retrieved 17 Sep 2026 18:23 CEST | 14–15°C, light rain, ~50–60% shower/rain risk through match window | Current structured forecast |
| WorldWeatherOnline Vejle | https://www.worldweatheronline.com/vejle-weather-history/syddanmark/dk.aspx | Weather cross-check; somewhat less rainy at 18:00 than primary structured forecast | Secondary weather cross-check |
| Google Drive `RULES_SOCCER.md` | Drive authoritative reference | Current soccer-specific controls, phase/goal/corner/source logic | Governing methodology reference |
| Google Drive `RULES_GENERAL.md`, `CONTROLS.md`, `SOURCES.md` | Drive authoritative reference | Cross-sport source, participant, derivative and coupling gates | Governing methodology reference |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| DBU Pokalen identity/ET+pens already documented | `LEAGUE_RULES_SOCCER.md` §4.11 | Existing reference correctly applied — **NO CHANGE** |
| Secondary injury page conflicted with official Brøndby squad | `SOURCES.md` / `DATA_SOURCE_REGISTER.md` | Reinforces field-owner participant handshake; **NO CHANGE** |
| Exact corner route available at Sofascore/TNT but DBU corner field not established | `DATA_SOURCE_REGISTER.md` | Candidate competition-specific derivative route for later audit; no source promotion yet |
| Rain at kickoff has bidirectional goal/corner effects | `RULES_SOCCER.md` environment control | Existing width-not-direction treatment; **NO CHANGE** |
| Brøndby recent early concessions are process evidence, not merely streak evidence | `RULES_SOCCER.md` first-half state / G17 mechanism rule | Existing mechanism rule correctly applied; **NO CHANGE** |

---

#### Settlement and retrospective — 18 Sep 2026

- **Final status:** `SETTLED — FINAL`.
- **Final result:** Vejle Boldklub **1-2 Brøndby IF**; half-time **1-1**.
- **Goal times:** Vejle 38'; Brøndby 40' and 84'.
- **Corner result:** Vejle **3**, Brøndby **7**; **10 total corners**. The corner field is supported by multiple structured secondary records; DBU/Vejle official reporting controls the match result but does not expose the corner total in the retrieved record.
- **Canonical-ID audit:** no P-454 entry exists in `PREDICTION_LOG_COMBINED_4.md`; no collision was found.

##### A. Ranked-pick and winner settlement

| Rank | Frozen selection | Final target | Result |
|---:|---|---:|---|
| 1 | 1st Half **Over 0.5 goals** | HT 1-1 | **WIN** |
| 2 | Total corners **Under 11.5** | 10 | **WIN** |
| 3 | Brøndby or Draw **X2, 90 min** | Brøndby won 2-1 | **WIN** |
| 4 | Brøndby team total **Over 0.5** | 2 | **WIN** |
| 5 | Combined goals **Over 2.5** | 3 | **WIN** |
| — | Projected eventual winner/qualifier: **Brøndby** | Brøndby advanced in regulation | **WIN** |

**Top-of-list diagnostics:** Rank #1 = **WIN**; Wins@2 = **2**; Hit@2 = **1**; both top two = **YES**; NDCG@2 = **1.000**. All five ranked rows won. That outcome is descriptive and does not make this card performance-eligible.

##### B. Why each pick won

**Rank #1 — 1H Over 0.5: WIN.** The card’s mechanism was Brøndby’s recent first-half defensive instability. The exact recent “concede in minute 1/4” pattern did not repeat; instead Vejle scored in the 38th minute and Brøndby equalized two minutes later. The useful conclusion is therefore broader: the first half did not stay controlled for 45 minutes. The pick won for a defensible process reason, but not because the precise early-concession timing repeated.

**Rank #2 — corners Under 11.5: WIN.** The final 3-7 corner count totaled 10. Vejle’s long home sequence below 11.5 and Brøndby’s typical away corner totals supported this broad band. The result was close enough to the line that source discipline matters: this retrospective records the count from corroborating structured secondary sources and does **not** relabel them as official DBU statistics.

**Rank #3 — Brøndby or Draw: WIN.** Brøndby’s higher-tier squad depth and the return of senior options gave a wide no-loss region. Vejle were competitive and led, showing why a straight Brøndby regulation-win row would have been more fragile than X2.

**Rank #4 — Brøndby team Over 0.5: WIN.** They scored twice. The pre-game reasoning that senior attacking depth could generate at least one goal survived even though Vejle’s defensive cup form was strong.

**Rank #5 — Over 2.5: WIN.** The game landed exactly at three. This was not a runaway attacking game; the Over needed the late winner. That distinction matters when assessing the quality of the thesis.

##### C. Rank-1 review

Rank #1 won. Its placement above participant-sensitive full-match rows was methodologically sound because exact starting XIs/benches were not fully confirmed. The phase row depended less on 90-minute substitution exposure.

##### D. Top-two review

Both won and the ordering remained reasonable. The corner Under had a broad empirical band but a weaker source lane; the first-half goal row had stronger direct process evidence and therefore deserved Rank #1 despite slightly similar marginal probabilities.

##### E. Over/under review

Both the first-half Over 0.5 and full-match Over 2.5 won. They should not be treated as independent confirmations of an “Over environment”: they share scoring-state dependence. The full total only cleared via an 84th-minute goal. Wet conditions did not force an Under, supporting the existing rule that rain/wet surfaces primarily widen uncertainty unless a specific directional mechanism exists.

##### F. What went right

- Event/competition/endpoint identity was correctly frozen as DBU Pokalen regulation markets versus advancement winner.
- Brøndby’s early-concession process was used rather than a simple losing-streak narrative.
- Vejle’s cup competitiveness was respected, preventing an overconfident Brøndby side call.
- Participant incompleteness kept the full-game rows below Rank #1.
- The corner line was treated as lower-evidence than official score/result markets.

##### G. Blind spots and smallest fixes

The official Vejle report says the winning goal was created and scored by **substitutes**: Mads Frøkjær-Jensen crossed for substitute Sho Fukuda. That is direct evidence that bench quality affected the decisive late state. The card had the Brøndby match squad but not complete field-owner starting XI/bench information for both teams. This is not a new discovery requiring a new gate; it **validates the existing `G14.2` bench-completeness control**.

Vejle also missed a penalty in the second half. That is realized match variance and should not be converted into a pre-game rule. It does show the 2-1 final was not a one-way game and supports the card’s decision to avoid an aggressive Brøndby margin.

##### H. Mandatory validation questions

1. **Confirmed starting XIs pregame?** No, not both from field-owner sources at the frozen cutoff.
2. **Bench/reserves?** Brøndby’s official match squad was captured; Vejle’s full match-day bench was not fully confirmed pregame.
3. **Coaching info?** Current coaching context was available; no post-match coaching surprise requires revision.
4. **Injuries/returns?** Brøndby returns/omissions were checked; conflicting secondary availability claims were correctly rejected where they contradicted the club squad.
5. **Original sources accurate/current?** Core official sources were strong. The corner evidence was and remains lower tier.
6. **Better sources?** DBU/Vejle/Brøndby official sources remain best for identity, score and squad. For corners, an accessible structured provider should be frozen before issue when the field owner does not expose them.
7. **Blind spots?** Full two-team bench completeness and derivative-source fragility.
8. **Future fix?** Continue enforcing `G14.2`; pre-register an accessible derivative-stat route and keep operator-action status separate.

##### I. Source audit / settlement evidence

| Source | Contribution | Assessment |
|---|---|---|
| Vejle official report — https://vejle-boldklub.dk/vb-braendte-straffe-og-roeg-ud-af-betano-pokalen/ | Official **1-2 (1-1)**, goal times, missed penalty, wet conditions, substitute-to-substitute winning goal | Primary club report |
| DBU exact match page — https://www.dbu.dk/resultater/kamp/486247_508655/kampinfo | Event identity / competition ownership | Primary field owner |
| GioScore — https://gioscore.com/football/match/brondby-if-vejle-boldklub/19872994 | **Corners 3-7**, shots 11-16, possession 40-60 | Structured secondary; claims official-data recomputation but is not the field owner |
| Forebet exact match record — https://www.forebet.com/en/football/matches/vejle-bk-br%C3%B8ndby-2548493 | Independent corner corroboration **3-7**, final 1-2 | Secondary; corroboration only |
| Sofascore exact fixture search record | Exact cup fixture and detailed-stat capability | Pre-registered route, but the generic slug was unstable in direct retrieval; do not treat the stale H2H page as settlement evidence |

**Derivative-field disposition:** research-grade corner settlement = **10, corroborated secondary**. Operator-specific corner action remains unknown because no operator terms were supplied. No source is promoted to permanent field-owner status from one case.

##### J. Learning / rule disposition

- `G14.2` bench-depth control is **supported as a process safeguard** by the substitute-created winning goal; **NO NEW RULE**.
- Derivative-source accessibility should be logged in `DATA_SOURCE_REGISTER.md` / `SOURCES.md` as a source-quality observation, not a forecast weight.
- No permanent “cup Over” or “rain Over” rule is warranted.

---

### P-455 — Baseball / MLB — Los Angeles Dodgers @ Cincinnati Reds

- **Canonical ID:** P-455 (mini-log sequence; combined-log reconciliation pending)
- **Sport / competition:** Baseball — MLB, 2026 regular season
- **Event:** Los Angeles Dodgers @ Cincinnati Reds
- **Venue:** Great American Ball Park, Cincinnati, Ohio
- **Scheduled start:** 17 Sep 2026, 12:40 PM EDT = 18 Sep 2026, 02:40 AEST (Australia/Melbourne)
- **Game state at issue:** **PREGAME AT FROZEN CUTOFF**. Final volatile freeze was taken before scheduled first pitch; no live/post-start information is permitted into this forecast.
- **Research cutoff / final volatile refresh:** 18 Sep 2026, **02:33:31 AEST** / 17 Sep 2026, **12:33:31 PM EDT**
- **Method version:** MDS-2026.09.06-v4.0
- **Population status:** **PRIMARY_SCORED — MLB**, while the controlling user direction remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.
- **Operating mode:** SPORTS_ONLY / MARKET_BLIND. User-supplied lines define contracts only; no odds, prices, implied probabilities, tipster selections or market movement are forecast evidence.

#### Identity / contract validation

- MLB official probable-pitcher pages confirm the exact fixture, venue and scheduled start: **Los Angeles Dodgers (92-60) @ Cincinnati Reds (71-81)**, 12:40 PM EDT.
- Official probable pitchers: **Justin Wrobleski (LAD, LHP; 11-5, 3.78 ERA, 111 SO)** and **Brady Singer (CIN, RHP; 6-14, 5.38 ERA, 125 SO)**.
- Supplied contracts frozen exactly as **CIN +1.5**, **LAD -1.5**, **Over 10.0**, **Under 10.0**.
- No operator-specific listed-pitcher, suspension, shortening or action rules were supplied. Settlement/action treatment outside an ordinary completed MLB game remains **UNKNOWN_DEFINITION**.

#### Mandatory completeness / forced-rank disclosure

- The MLB field-owner starting-lineup page still displayed the batting orders as **TBD** at the pregame freeze. Two current pregame secondary sources subsequently showed matching "confirmed" orders, but they are not upgraded to `CONFIRMED_OFFICIAL`.
- A complete current field-owner bench/reserve record was **not cleanly recoverable before freeze**. Some MLB roster pages had internally stale active/IL presentation, so this card records **`BENCH_NOT_RETRIEVED_TO_GATE_STANDARD`** rather than laundering a reconstructed bench as official.
- Under `G14.2`, `BENCH_NOT_RETRIEVED` blocks a margin or full-game total from an **uncapped Rank #1**. Since the user's entire four-row slate consists only of a run-line pair and full-game total pair, the table below is a **FORCED ORDERING of the supplied slate**. No row is represented as a rule-clean high-confidence Rank #1.
- The Drive's current `BASE_RATES_REGISTER.md` also leaves Great American Ball Park among the 22 parks whose exact current-season `P(>L) / P(=L) / P(<L)` total distribution is **NOT_YET_DERIVED**. Therefore both 10.0 total rows carry **`GABP_10.0_BASE_RATE_NOT_DERIVED`** and are evidence-capped.

#### Latest pregame batting orders / rest state

**Secondary-confirmed LAD order:** Tommy Edman CF (S), Freddie Freeman 1B (L), Kyle Tucker RF (L), Teoscar Hernández LF (R), Max Muncy 3B (L), Josue De Paula DH (L), Hunter Feduccia C (L), Alex Freeland 2B (S), Miguel Rojas SS (R).

**Secondary-confirmed CIN order:** Dane Myers CF (R), Elly De La Cruz DH (S), Sal Stewart 1B (R), Tyler Stephenson C (R), Juan Brito 2B (S), Matt McLain SS (R), Héctor Rodríguez RF (L), Ke'Bryan Hayes 3B (R), TJ Friedl LF (L).

- **Los Angeles is materially below its normal offensive ceiling:** Shohei Ohtani is on the IL; **Mookie Betts and Will Smith are not in the reported starting nine**. Freeman, Tucker, Teoscar and Muncy still leave a dangerous top/middle core, but the PA-weighted lineup is not the full-strength Dodgers order.
- Ohtani is on the 15-day IL with left-knee/right-biceps issues; Blake Snell left the previous game after one inning with left-groin tightness; Edgardo Henriquez is on the IL with a low-grade back strain; Edwin Díaz and Roki Sasaki were not active late-inning/full-start certainties at the frozen point.
- Cincinnati's official injury record includes Spencer Steer (right wrist, likely out for 2026), Hunter Greene (second Tommy John surgery) and Blake Dunn (elbow surgery). Matt McLain had recently been day-to-day with a sore shoulder but is present in the current reported starting order.

#### Starter disaggregation — required current-regime read

**Justin Wrobleski, LAD**

Season: **11-5, 3.78 ERA, 133.1 IP, 1.16 WHIP**, with 111 SO. The season centre is materially better than Singer's, but current workload shape is not a conventional six-inning-starter regime.

Required recent log:
- **Sep 12 @ MIA:** 2.0 IP, 2 H, **0 ER**, 1 BB, 1 K, 25 pitches.
- **Sep 6 vs WSH:** 3.0 IP, 8 H, **4 ER**, 1 BB, 6 K, 73 pitches.
- **Sep 1 vs STL:** 2.0 IP, 2 H, **2 ER** (3 R), 1 BB, 4 K, 36 pitches.
- **Aug 15 vs MIL:** 6.0 IP, 4 H, **4 ER**, 1 BB, 6 K, 107 pitches.

Interpretation: the last-three window is **7 IP, 6 ER, 3 BB, 11 K**. Command has not collapsed, but exposure has shortened sharply. Per the Drive, short length is primarily **width/relief exposure**, not an automatic Over sign. Same-day Dodgers reporting says the club hoped Wrobleski could provide more length because the bullpen had been heavily used after Snell's one-inning exit.

**Brady Singer, CIN**

Season: **6-14, 5.38 ERA, 150.2 IP, 1.51 WHIP, 125 SO**.

Required recent log:
- **Sep 12 @ MIL:** 4.0 IP, 8 H, **8 ER**, 3 HR, **5 BB**, 5 K.
- **Sep 6 vs MIL:** 5.0 IP, 4 H, **6 ER**, 1 HR, **6 BB**, 3 K.
- **Aug 31 vs SD:** 4.1 IP, 10 H, **4 ER**, 0 BB, 5 K.
- **Aug 25 @ SF:** 5.2 IP, 6 H, **3 ER**, 2 BB, 5 K.

The last two starts total **9 IP, 14 ER, 11 BB and 4 HR**. This is more than an ERA-only bad streak: the walk and home-run channels provide a named current mechanism for a wider/upward Dodgers scoring tail. Counter-evidence remains real: Singer has historically pitched well against Los Angeles (**2-1, 1.89 ERA in three career starts**), so the two-start collapse is shrunk rather than treated as destiny.

#### Bullpen / workload chain

- The previous game materially taxed Los Angeles after Snell exited after one inning. LA used **Blake Treinen (1.0 IP), Seth Halvorsen (1.0), Bobby Miller (2.1), Alex Vesia (0.2), Jack Dreyer (1.0) and Kris Bubic (1.0)**. The team then called up **Landon Knack** and optioned Miller to create fresh length; Bubic had just been activated from the 60-day IL.
- This makes Wrobleski's hook point unusually important. Fresh length exists, but the preferred leverage tree is not fully fresh/healthy, so a 2–4 inning Wrobleski outing carries greater downstream variance than his season ERA alone implies.
- Cincinnati used **Julian Garcia, Tejay Antone, Brock Burke, Graham Ashcraft and Emilio Pagán** behind Andrew Abbott the previous day. Exact pregame availability for every reliever was not recoverable to the field-owner gate standard, so no blanket "fresh" or "gassed" bullpen sign is applied.

#### Venue / weather / environment

- Great American Ball Park is open-air. At the frozen game window the structured weather feed showed roughly **31°C / 88°F**, rising to about **33–35°C**, with some afternoon thunderstorm risk. A current pregame lineup/weather source showed **89°F, partly cloudy, ~7 mph wind out toward left field**.
- Environment treatment is mechanistic only: heat/wind can expand the HR/carry tail, but they do **not** automatically make the Over the correct side.
- A current secondary park-factor page built from Baseball Savant/MLB venue data reports **74 completed 2026 games, 8.85 runs/game**, 2026 run index **98**, three-year run index **102**, and three-year HR index **114**. The venue is therefore near neutral on overall run volume but remains homer-friendly. Its recent September scoring is high, but that is a tiny sample and is not fitted into a weight.
- The active Drive base-rate register does **not** yet publish the exact Great American Ball Park distribution at **10.0**, so control 35 cannot be completed to field-owner identity standard for this row.

#### Joint event object / component and separation budgets

**Winner centre:** LAD **0.61**, CIN **0.39** (`UNVALIDATED_SUBJECTIVE`).

Why LAD remains ahead: much stronger season record/team-strength prior, Wrobleski's materially better season run-prevention baseline, and Singer's back-loaded command/HR failure. Why the gap is not larger: LAD is on the road, its lineup is missing Ohtani/Betts/Smith from the starting group, Wrobleski's recent exposure is short, and the Dodgers' relief chain was heavily used the previous day.

**Run-line identity (`G-L24` / baseball control 34):** LAD season win% ≈ .605 vs CIN ≈ .467, winner-minus-loser W% gap ≈ **+0.14**, so use the current `+0.1` MLB one-run band **r = 0.268**, `n = 2,286` completed 2026 MLB games through Sep 16.

- `P(LAD -1.5) = 0.61 × (1 - 0.268) = 0.4465 ≈ 0.45`
- `P(CIN +1.5) = 0.39 + 0.61 × 0.268 = 0.5535 ≈ 0.55`

The 2026 MLB extras branch reinforces the protected side structurally: tie-after-nine rate **8.75%**, and **68.5%** of extra-inning finals have been one-run margins.

**Game-total centre:** approximately **9.6 runs**, width **~4.6 runs**. Normalised distance to the 10.0 line is only **|9.6-10.0| / 4.6 ≈ 0.09** — a narrow edge and therefore not a strong total call.

Component logic (mechanism-overlap audited):
- neutral-ish 2026 GABP raw scoring environment as prior;
- **Singer current command/HR breakdown:** signed upward adjustment;
- **Wrobleski short exposure + taxed/reshaped LAD relief chain:** mainly width, slight upward tail only because the prior-night usage/IL state is an active mechanism;
- **LAD missing Ohtani/Betts/Smith from the start:** signed downward PA-weighted lineup adjustment;
- **hot/out-to-LF conditions:** tail widening / small carry channel, not double-counted with park HR factor.

Because the exact venue 10.0 distribution is not derived, the total probabilities are explicitly **capped estimates**. Push mass is anchored near the league's current **6.7% at total 10** rather than invented as a narrow game-specific certainty.

**Discrete coherent final-state family:**

| State | Mass |
|---|---:|
| LAD wins by 2+ & total <10 | 0.18 |
| LAD wins by 2+ & total =10 | 0.03 |
| LAD wins by 2+ & total >10 | 0.237 |
| LAD wins by exactly 1 & total <10 | 0.09 |
| LAD wins by exactly 1 & total =10 | 0.01 |
| LAD wins by exactly 1 & total >10 | 0.063 |
| CIN wins & total <10 | 0.24 |
| CIN wins & total =10 | 0.03 |
| CIN wins & total >10 | 0.12 |
| **Total** | **1.00** |

This yields: **CIN +1.5 0.553; LAD -1.5 0.447; Under 10.0 0.51; push exactly 10 0.07; Over 10.0 0.42.**

- `P(R1 ∧ R2)` ≈ **0.33** for CIN +1.5 and Under 10 both winning.
- `P(neither preferred decision wins)` ≈ **0.237** — the key both-fail state is **LAD win by 2+ in an 11+ run game**, most naturally Singer breaks early and the Dodgers continue scoring while Cincinnati also contributes enough against the short-start/relief chain.
- Representative Rank-#1-compatible state: **LAD 5-4 CIN** — Dodgers win, Reds +1.5 covers, Under 10 wins.

#### Ranked picks — forced ordering of the supplied slate

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Geometry | Why this rank | Primary failure path |
|---:|---|---:|---|---|---|---|
| **1** | **Cincinnati Reds +1.5** | **0.55** | **FORCED RANK / MEDIUM** (`G14.2` cap) | FORCED_PAIR preferred side | Derived from LAD win p=0.61 and league one-run band r=0.268. Home last-bat, extra-inning one-run geometry and LAD's weakened starting lineup preserve the close-loss/win branches. | Singer's command/HR collapse persists and LAD's top five turn it into a 6-2/7-3/8-4 separation game. |
| **2** | **Combined Total UNDER 10.0 runs** | **0.51** | **FORCED RANK / MEDIUM-LOW** (`G14.2` + control-35 cap) | FORCED_PAIR preferred side; **PUSH 0.07** | The line is high relative to GABP's 8.85 current-season raw mean; LAD is missing three premium starting bats and Wrobleski still owns a 3.78 season ERA. Centre ~9.6. | Singer's walks/HRs produce an early LAD crooked inning and the short Wrobleski/bullpen chain allows Cincinnati enough response to reach 11+. |
| **3** | **Los Angeles Dodgers -1.5** | **0.45** | **FORCED RANK / MEDIUM** (`G14.2` cap) | FORCED_PAIR non-preferred side | LAD is the projected winner and Singer is the weakest current-regime starter, but the league's one-run band mathematically limits a two-plus-run win probability. | CIN wins outright or loses by exactly one; extras disproportionately create one-run finals. |
| **4** | **Combined Total OVER 10.0 runs** | **0.42** | **FORCED RANK / MEDIUM-LOW** (`G14.2` + control-35 cap) | FORCED_PAIR non-preferred side; **PUSH 0.07** | Singer's 14 ER/9 IP + 11 BB/4 HR last two and LAD's stressed pitching chain create a real 11+ tail, amplified by warm HR-friendly conditions. | Singer stabilises toward his career-vs-LAD history, LAD's rested bats reduce conversion, and Wrobleski/Knack hold CIN to 2–4 runs. |

**Decision interpretation:** this is **two forced-pair decisions**, not four independent bets. Within the forced slate the preferred sides are **CIN +1.5** and **Under 10.0**, but the entire card is gate-capped because full benches were not retrieved to standard; the total pair carries the additional exact-venue-base-rate cap.

#### Projected match winner

- **Projected winner: Los Angeles Dodgers**
- **Winner endpoint:** eventual MLB game winner including extra innings, conditional on actionable completion under operator rules.
- **Probability:** **0.61 `UNVALIDATED_SUBJECTIVE`**; Cincinnati 0.39.
- The winner label is coherent with the ranked rows: LAD can be more likely to win while CIN +1.5 remains the more likely exact run-line contract because a meaningful share of LAD wins are expected to finish by one run.

#### Information not confirmed / integrity flags

- **`BENCH_NOT_RETRIEVED_TO_GATE_STANDARD`** — no uncapped margin/full-game-total Rank #1 is permitted under `G14.2`; rankings are forced by the user-required four-row slate.
- Official MLB starting-lineup page still displayed TBD at frozen cutoff; detailed orders are secondary-confirmed, not field-owner confirmed.
- **`GABP_10.0_BASE_RATE_NOT_DERIVED`** — exact venue `P(>10)/P(=10)/P(<10)` not present in the active base-rate register. Secondary park mean/factors are context only, not a substitute identity input.
- Exact operator listed-pitcher/suspension/shortening rules were not supplied (`UNKNOWN_DEFINITION`).
- No umpire-zone adjustment is used under the 2026 ABS challenge environment.
- No post-start/live information is incorporated after the 02:33:31 AEST freeze.
- No retrospective or settlement performed.
- **Current settlement status:** **UNSETTLED — PREGAME AT ISSUE**.

#### Settlement routes pre-registered

- Final score / run line / game total: **MLB StatsAPI / MLB Gameday official final**.
- Exactly-10 push and extra-inning endpoint: official MLB linescore/box score with scheduled-vs-current innings fields.
- Pitcher/lineup participation: MLB official box score and Statcast where needed.

#### Sources

| Source | Link / record | Contribution | Quality / limitation |
|---|---|---|---|
| MLB Dodgers/Reds probable pitchers | https://www.mlb.com/dodgers/roster/probable-pitchers ; https://www.mlb.com/reds/roster/probable-pitchers | Exact fixture, time and Wrobleski/Singer official probable identities | Primary / field owner |
| MLB starting lineups | https://www.mlb.com/starting-lineups | At frozen cutoff the orders remained TBD; establishes official-lineup incompleteness | Primary but incomplete |
| InsidetheLineup pregame page | https://insidethelineup.com/mlb/reds-lineup.html | Secondary-confirmed current batting orders; 89°F, 7 mph out-to-LF snapshot | Secondary; not upgraded to field-owner confirmed |
| CBS pregame GameTracker | https://www.cbssports.com/mlb/gametracker/preview/MLB_20260917_LAD%40CIN/ | Corroborated lineups; Singer recent failure and career-vs-LAD counter-evidence | Secondary statistical |
| Baseball Savant Brady Singer | https://baseballsavant.mlb.com/savant-player/brady-singer-663903 | Sep 6/Sep 12 disaggregated start line; season context | MLB/Statcast primary statistical lane |
| Baseball-Reference / CBS Justin Wrobleski game log | https://www.baseball-reference.com/players/w/wroblju01.shtml ; CBS Wrobleski game log | Last-three/four exposure, pitches, ER, BB, K | High-quality statistical secondary |
| MLB current game preview | https://www.mlb.com/stories/game-preview/824464 | Singer 14 ER in 9 IP last two; Freeman matchup note | Primary editorial / MLB record |
| MLB Dodgers injury/transaction page | https://www.mlb.com/news/dodgers-injuries-and-roster-moves | Ohtani, Snell, Henriquez, Díaz, Sasaki and current transactions | Primary |
| MLB Reds injury page | https://www.mlb.com/reds/news/reds-injuries-and-roster-moves | McLain, Steer, Greene, Dunn availability | Primary |
| Reuters Sep 16/17 | Dodgers-Reds prior-game report and Snell injury report | Prior-game state; Snell one-inning exit; series/bullpen context | High-quality secondary |
| Baseball Almanac Sep 16 box score | https://www.baseball-almanac.com/box-scores/boxscore.php?boxid=202609160CN5 | Exact previous-day reliever chain/innings/pitches for workload context | Structured secondary; field-owner cross-check preferred at settlement |
| True Blue LA pregame/roster reports | Sep 17 Wrobleski/Knack reports | Wrobleski expected to provide length; Knack recall/Miller option; bullpen-plan context | Team-specialist secondary |
| Great American Ball Park 2026 park-factor page | https://www.bestmlbhandicapper.com/parks/great-american-ball-park-park-factors.html | 74-game raw mean 8.85; 2026 run index 98; 3-year HR index 114; dimensions/splits | Secondary derived from Savant/MLB; context only, not Drive identity source |
| Structured weather source | Great American Ball Park hourly, frozen pregame | ~31–35°C, afternoon thunderstorm risk | Current structured weather |
| Drive `RULES_BASEBALL.md` | Sports Research Drive | SFA-BASEBALL, controls 24–37, run-line/total/relief requirements | Governing methodology |
| Drive `CONTROLS.md` | Sports Research Drive | `G14.2` bench completeness; gate/cap behaviour | Governing methodology |
| Drive `BASE_RATES_REGISTER.md` | Sports Research Drive | 2026 MLB r=0.268 bin; extras; line-10 league push 6.7%; GABP not yet derived | Governing quantitative identity input |
| User-supplied slate | Current query | Exact ±1.5 and O/U 10.0 contracts | Contract source only |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| Singer's ERA slump is accompanied by 11 BB + 4 HR in 9 IP | `RULES_BASEBALL.md` controls 13/24 | Existing disaggregate/current-regime control correctly applied; **NO CHANGE** |
| Wrobleski short recent exposure plus prior-night six-reliever usage | `RULES_BASEBALL.md` controls 15/19/20/29 | Existing hook/relief-chain controls correctly applied; **NO CHANGE** |
| Missing Ohtani plus Betts/Smith rest changes PA-weighted LAD scoring ceiling | `RULES_BASEBALL.md` control 27 / `G14.2` | Existing lineup-exposure control correctly applied; **NO CHANGE** |
| Great American Ball Park exact 10.0 distribution absent from register | `BASE_RATES_REGISTER.md` §3 | **DATA GAP / future derivation candidate**, not a rule change |
| Full current bench could not be field-owner verified despite lineup recovery | `DATA_SOURCE_REGISTER.md` / `SOURCES.md` | Source-coverage note; `G14.2` cap correctly triggered; **NO CHANGE** |


---

#### Settlement and retrospective — 18 Sep 2026

- **Final status:** `SETTLED — FINAL`.
- **Final result:** Los Angeles Dodgers **8**, Cincinnati Reds **2**.
- **Game total:** **10 runs exactly**.
- **Canonical-ID audit:** no P-455 entry exists in `PREDICTION_LOG_COMBINED_4.md`; no collision was found.

##### A. Ranked-pick and winner settlement

| Rank | Frozen selection | Final target | Result | Exact treatment |
|---:|---|---:|---|---|
| 1 | Cincinnati Reds **+1.5** | CIN lost by 6 | **LOSS** | Dodgers separated 8-2. |
| 2 | Combined **Under 10.0** | **10** | **PUSH** | Integer boundary; not a win. |
| 3 | Los Angeles Dodgers **-1.5** | LAD won by 6 | **WIN** | Covered by 4.5 runs. |
| 4 | Combined **Over 10.0** | **10** | **PUSH** | Same integer boundary; not a win/loss. |
| — | Projected winner: **Dodgers** | LAD won 8-2 | **WIN** | Correct winner. |

**Top-of-list diagnostics:** Rank #1 = **LOSS**. Wins@2 = **0**; Hit@2 = **0** because a push is not a win; both top two = **NO**. With binary relevance where pushes carry 0 win relevance, NDCG@2 = **0.000**; the sole ranked winner was Rank #3. This is a learning-only diagnostic.

##### B. Why each selection won, lost or pushed

**Rank #1 — Cincinnati +1.5: LOSS.** The card derived the protected Reds side from a Dodgers winner centre plus a generic 2026 one-run-margin band. But its own strongest failure path was explicit: **Singer’s current command/HR collapse persists and Los Angeles separates early**. That is exactly what happened. Singer was charged with **seven earned runs in 3.1 innings**, allowed nine hits and four walks, and recorded no strikeouts. Los Angeles scored two in the first, two in the second and three in the fourth. This was not an unforeseeable shock. The key failure is **weighting**: a known, mechanistically supported current-regime starter branch was not given enough mass relative to generic one-run geometry and the weakened Dodgers lineup.

**Rank #2 — Under 10.0: PUSH.** The pre-game total centre was 9.6 with explicit push mass. The game landed exactly on 10, so preserving integer-boundary probability was essential. Singer alone created a seven-run Dodgers base by the fourth, but Cincinnati’s offense remained suppressed. Wrobleski threw three perfect innings and Landon Knack added four scoreless innings. Thus one side of the scoring distribution exploded while the other remained low enough to stop the game at the boundary.

**Rank #3 — Dodgers -1.5: WIN.** This was the non-preferred run-line side but its exact failure-path logic was strong: if Singer’s severe recent walk/home-run failure persisted, Los Angeles had a separation route even with Ohtani/Betts/Smith absent from the starting group. The official game story shows that route occurred immediately.

**Rank #4 — Over 10.0: PUSH.** The Over branch received support from Singer and the potentially stressed Dodgers pitching chain. Singer delivered the upward half, but Cincinnati did not. The Reds scored only twice, one in the fourth and one in the ninth. This illustrates why “one bad starter” can create a high team score without guaranteeing the full-game Over.

**Projected Dodgers winner: WIN.** The stronger-team prior and Singer disadvantage were enough for the outright result. The error was specifically the **margin distribution**, not the winner direction.

##### C. Deep Rank-1 failure review

**Why it was ranked first.** The card used the league one-run identity: with LAD winner p≈0.61 and one-run band r≈0.268, it mechanically produced Cincinnati +1.5 ≈0.55. Home last-bat, extras geometry and the reduced Dodgers lineup added plausibility.

**Was that justified pregame?** The arithmetic was internally coherent, but the final ordering was not robust enough to event-specific separation evidence. Singer entered with **14 earned runs, 11 walks and four home runs in nine innings over his prior two starts**. That is a named mechanism directly capable of creating a multi-run Dodgers lead. The card identified it but allowed the generic margin band to dominate.

**Should another row reasonably have ranked higher?** On the frozen evidence, **Dodgers -1.5 had a stronger case than its 0.45 placement suggests**, although this retrospective must not assign a hindsight probability. The ranking should at minimum have been closer to a toss-up after event-specific separation stress. The projected Dodgers winner plus Singer’s current-regime failure branch made the favorite margin the strongest candidate to challenge Rank #1.

**Missed/underweighted variable:** no critical fact was missing. The decisive variable was **underweighted current-regime starter separation risk**. Missing bench information correctly triggered a cap, but it was not the cause of the loss.

**Existing rule that should have helped:** `G20.1` separation budgets, `G-L23` result-vs-process, the strongest-kill-path audit and baseball current-regime starter disaggregation were already applicable. This is therefore primarily an **execution/weighting failure**, not evidence that another permanent rule is immediately required.

**Smallest fix:** when a generic run-line cushion identity conflicts with a strong event-specific separation mechanism, print the generic identity as a reference but re-solve the separation state by starter/relief phase. If the event-specific “2+ run favorite win” branch is substantial, the generic band cannot own the ordinal by itself.

##### D. Top-two review

Neither top selection won. Rank #1 lost and Rank #2 pushed. The top-two failure state was correctly described in advance as a Dodgers 2+ run win with enough scoring pressure to reach the total boundary/high side. The outcome was 8-2: the margin failure fully materialized, while the total stopped on the push boundary. Future top-two ranking should stress **shared dependence on Singer not fully imploding**: Cincinnati +1.5 and Under 10 were not independent defensive positions.

##### E. Over/under review

This game is a direct example of why integer totals need three-way W/P/L treatment. At exactly 10:
- Under 10.0 = **PUSH**
- Over 10.0 = **PUSH**

Neither side “won”. It also illustrates allocation risk. Eight of ten runs belonged to Los Angeles. A full-game total must model both sides’ contribution; one team’s explosive branch does not automatically imply an Over if the opponent is suppressed. The printed pre-game push mass was therefore conceptually correct even though its exact 0.07 is unvalidated.

##### F. What went right

- Singer’s deterioration was not hidden: the correct mechanism was explicitly identified.
- Wrobleski’s recent short exposure was treated as width/relief exposure rather than automatically signed Over.
- The card preserved push mass at 10.0.
- Projected winner Los Angeles was correct.
- The final official lineup archive confirms the secondary pre-game lineups were accurate.

##### G. Blind spots and future treatment

| Blind spot | What happened | Future treatment |
|---|---|---|
| Generic one-run band dominated event-specific separation | LAD won by six after Singer allowed seven ER | Re-solve margin by starter/relief phases whenever a current-regime starter failure can create early separation. |
| Shared dependency of +1.5 and Under not emphasized enough | Both top rows depended on Cincinnati avoiding a large deficit; one lost, one only pushed | Print the top-two shared failure branch in score units and test it against the strongest starter kill path. |
| Full bench not retrieved pregame | Gate cap triggered | Keep cap; do not use this result to claim bench absence caused the miss. |
| Opponent contribution under total | CIN only scored 2 | Continue allocation-marginal requirement; do not turn starter weakness on one team into unconditional full-game Over. |

##### H. Mandatory validation questions

1. **Confirmed starting lineups before issue?** MLB field-owner page had TBD at freeze; secondary lineups were used. The final official archive confirms they were accurate.
2. **Bench/reserve info?** Not retrieved to gate standard, correctly disclosed.
3. **Coaching/manager info?** No decisive unrecorded managerial change is identified; bullpen-plan context was researched.
4. **Injuries/rest/availability?** Major Dodgers absences/rest and Reds injuries were checked.
5. **Original sources sufficiently accurate/current?** Yes on participants/starters and current form. The failure was analytical weighting.
6. **Better sources?** Official MLB lineup/Gameday once populated remain preferred; no new source gap explains the outcome.
7. **Blind spot?** Event-specific separation risk was underweighted against generic run-line geometry.
8. **Future fix?** Phase-specific separation budget must be allowed to override a descriptive league one-run reference when the two conflict.

##### I. Source audit / settlement evidence

| Source | Contribution | Assessment |
|---|---|---|
| MLB scoreboard — https://www.mlb.com/scores/2026-09-17 | Official **LAD 8-2 CIN** | Primary |
| MLB Film Room game 824464 — https://www.mlb.com/video/game/824464 | Line score; Singer 3.1 IP/7 ER; Knack 4.0 scoreless | Primary |
| MLB game story — https://www.mlb.com/stories/game/824464 | Early scoring sequence: 2 in 1st, 2 in 2nd, 3 in 4th; later CIN runs | Primary |
| MLB Dodgers clinch report — https://www.mlb.com/news/dodgers-clinch-2026-nl-west-title | Official narrative and 8-2 final | Primary |
| MLB Reds starting-lineup archive | Exact final batting orders; confirms pre-game secondary order | Primary |

##### J. Learning / rule disposition

- **Existing controls already contained the fix:** separation budget + kill-path weighting. The first disposition is therefore **PROCESS EXECUTION ISSUE / NO NEW RULE**.
- Proposed candidate for prospective audit only: `C-MLB-GENERIC-RUNLINE-VS-EVENT-SEPARATION` — track cases where the league one-run identity and event-specific starter/relief separation disagree, without changing live weights until enough prospective cases exist.
- Record under `RULES_BASEBALL.md`, `LEARNING_REGISTER.md` (candidate only if formally tested), and `BASE_RATES_REGISTER.md` only if the league margin identity itself is later recomputed. Do not rewrite the identity from this one result.

---

### P-456 — Soccer / Spain LaLiga — Real Betis vs Getafe CF

- **Canonical ID:** P-456 (mini-log sequence; combined-log reconciliation pending)
- **Sport / competition:** Soccer — Spain LaLiga 2026/27, Matchday 6
- **Event:** Real Betis vs Getafe CF
- **Official/structured identity:** scheduled LaLiga event `72478570`; Betis current matchday shell; Getafe official J6 exact-match page.
- **Venue:** **Estadio La Cartuja de Sevilla, Seville**. A current LaLiga exact-match shell displays Benito Villamarín, but LaLiga's Betis club profile identifies La Cartuja as Betis' current stadium and Getafe's official exact-match page identifies this fixture at La Cartuja. The metadata conflict is retained as an integrity note rather than silently ignored.
- **Scheduled start:** 17 Sep 2026, 19:00 CEST = 18 Sep 2026, 03:00 AEST (Australia/Melbourne)
- **Game state at issue:** **PREGAME** — structured schedule still showed `Scheduled` at the frozen refresh; no live/post-start information used.
- **Research cutoff / final volatile refresh:** **18 Sep 2026, 02:49:06 AEST / 17 Sep 2026, 18:49:06 CEST**, ~11 minutes before scheduled kickoff.
- **Method version:** MDS-2026.09.06-v4.0 / SFA-SOCCER
- **Population status:** EXPLORATORY — NOT SCORED for primary-performance purposes; current user direction remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.
- **Operating mode:** SPORTS_ONLY / MARKET_BLIND.

#### Contract / endpoint freeze

- User-supplied contracts frozen exactly as **1st-half goals O/U 0.5** and **90-minute combined goals O/U 2.5**.
- Self-selected rows considered: 1H Under 1.5, Getafe team total Under 1.5, Betis team total Over 0.5, Getafe team corners Under 5.5.
- All full-match goal/team-goal/corner markets settle at **90 minutes plus stoppage time**. First-half markets settle at the end of first-half stoppage time.
- **Potential winner endpoint:** regulation 1X2 result after 90 minutes plus stoppage time.

#### Participants / availability / rotation

**Field-owner XI/bench state at cutoff: NOT RELIABLY RETRIEVED.** Getafe's official exact-match page still showed that lineups would be available before kickoff but the retrieved record did not contain a current XI/bench. Betis' official current matchday shell also did not expose a reliable current XI/bench. A same-day AS lineup page showed complete lineups but listed **Borja Mayoral on Getafe's bench**, directly conflicting with same-day reporting that Mayoral was left out of the travelling squad. That secondary lineup is therefore not promoted to `CONFIRMED_OFFICIAL`.

- **Betis absences:** Diego Llorente and Aitor Ruibal unavailable. Current squad reporting otherwise describes a deep senior group.
- **Betis rotation:** Pellegrini was expected to make roughly 4–5 changes after Monday's Villarreal match and before another Sunday fixture. Facundo Bernal, Dani Ceballos, Antony and Troy Parrott were among reported candidates to enter. This remains a participant mixture, not a confirmed XI.
- **Getafe availability:** same-day reporting says **Borja Mayoral did not travel / remains in recovery**. Kiko Femenía and Christantus Uche remain unavailable; Abdel Abqar had physical issues. Bordalás' pre-match comments said **Andrés García and Zaid had recovered**, superseding earlier previews that listed them as doubts.
- **Getafe width constraint:** Bordalás explicitly said the squad lacks natural wingers and explained using Satriano wide because of that shortage. This is a direct wide/corner-generation mechanism.
- **Coaches:** Manuel Pellegrini (Betis); José Bordalás (Getafe).
- **Participant gate:** exact field-owner starting XIs/full benches were not reliably recovered. `SO-P2` / `G14.2` is therefore not a clean pass. Full-game side/team-total/full-game total rows are **FORCED RANK / evidence-capped**; a research-complete phase row can occupy Rank #1 while those participant-sensitive full-game rows cannot.

#### Current team / process evidence

- Current official LaLiga state after five matches: **Betis 4-0-1, 7 GF, 6 GA, 64 shots**; **Getafe 1-2-2, 3 GF, 6 GA, 44 shots**.
- Current previews put Betis around **1.4 goals/match** and Getafe around **0.6**; Betis also hold the stronger current shot, passing and possession profile.
- **Betis league results:** 1-0 Real Sociedad, 1-0 at Valencia, 2-5 at Levante, 1-0 Real Madrid, 2-1 at Villarreal. Betis have scored in all five; the Levante match is a major defensive upper-tail result and not treated as the central state by itself.
- **Getafe league results:** 0-3 at Alavés, 1-0 vs Racing, 0-1 at Osasuna, 1-1 vs Celta, 1-1 vs Deportivo. Four of five finished below 2.5 goals. Getafe have scored **0 league goals in their two away league matches**.
- Secondary xG providers disagree materially on exact values. Their figures are not averaged or merged; official goal/shot evidence remains the primary process anchor.

#### First-half phase audit — controls 20 and 40

Goal timing was reconstructed from current LaLiga/official match records before the cutoff:

- **Betis:** 0 first-half goals in the match vs Real Sociedad; 0 at Valencia; 2 combined first-half goals at Levante; 0 vs Real Madrid; 3 combined first-half goals at Villarreal. Thus **3/5 Betis league matches were 0-0 at HT** and **2/5 contained 2+ first-half goals**.
- **Getafe:** 0-0 HT at Alavés; 0-0 HT vs Racing; Osasuna scored at 45+2; Getafe scored at 21' vs Celta; 0-0 HT vs Deportivo. Thus **3/5 Getafe league matches were 0-0 at HT**, and none contained 2+ first-half goals.

These are direct current-regime phase observations, not ten independent Bernoulli trials.

**Printed first-half goal-count distribution (`UNVALIDATED_SUBJECTIVE`):**

| 1H goals | Mass |
|---|---:|
| 0 | **0.56** |
| 1 | **0.29** |
| 2 | **0.11** |
| 3+ | **0.04** |
| **Total** | **1.00** |

Sibling lines derived from the same distribution:
- `P(1H Under 0.5)` = **0.56**; `P(1H Over 0.5)` = **0.44**.
- `P(1H Under 1.5)` = **0.85**; `P(1H Over 1.5)` = **0.15**.

The supplied 0.5 line is therefore only a modest Under lean; the stronger phase expression is the self-selected **1H Under 1.5**.

#### Full-match goal object

**90-minute goal centre:** ~**2.2 goals**, width ~**1.6 goals**. Downward mechanisms: Getafe's 0.6 GF/match, low attacking volume, no away league goals, Mayoral absence, compact profile. Upward branches: Betis' superior shot volume, trailing-state transitions, rotation-driven defensive variance, and the demonstrated 2-1 / 5-2 Betis upper tails.

**Printed regulation goal-count distribution (`UNVALIDATED_SUBJECTIVE`):**

| FT goals | Mass |
|---|---:|
| 0 | 0.09 |
| 1 | 0.26 |
| 2 | 0.28 |
| 3 | 0.20 |
| 4+ | 0.17 |
| **Total** | **1.00** |

Implications:
- **Under 2.5 = 0.63 / Over 2.5 = 0.37**.
- Nested Under 3.5 ≈ **0.83**, but it is deliberately not added as another ranked row because it is the same suppression thesis at a looser threshold rather than a distinct decision.
- Normalised U2.5 edge: `|2.2 - 2.5| / 1.6 ≈ 0.19`, consistent with a moderate, not high-confidence, main-line total lean.
- Betis score 1+ ≈ **0.75**.
- Getafe score 0–1 ≈ **0.81** (`Getafe Under 1.5`).

**90-minute result family:** Betis win **0.54**, draw **0.28**, Getafe win **0.18**.

#### Corner process

- Current secondary season rates: Betis ~**4.8 corners for/match**; Getafe ~**4.0**.
- Getafe current league corner-for sequence in the accessible record: **3, 8, 3, 3, 3**. They stayed **Under 5.5 team corners in 4/5** and recorded exactly **3 corners in both away league matches**.
- Bordalás' lack-of-natural-wingers comment is a direct width mechanism consistent with a lower Getafe corner ceiling.
- A complete current cross/blocked-cross/end-line/clearance dataset and confirmed final XI were not recovered. Therefore **Getafe team corners Under 5.5 = FORCED RANK / MEDIUM-LOW**, not `SUPPORTED`.
- **Pre-registered settlement route:** Getafe official exact-match statistics page first; ESPN `soccer/esp.1` `wonCorners` as structured research-grade fallback/cross-check, consistent with the Drive's LaLiga derivative-route table.

#### Weather / venue

- Venue-local structured forecast at ~18:47 CEST: ~**28°C, sunny/dry**, with **0% precipitation** indicated from 19:00 through 22:00.
- No material rain/wind disruption mechanism identified. Weather therefore contributes little uncertainty and no automatic scoring sign.
- Venue metadata conflict is preserved: LaLiga exact-match shell says Benito Villamarín, while LaLiga's Betis profile and Getafe's official exact-match page point to **La Cartuja**, which controls this card.

#### Ranked picks — gate-aware

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Geometry | Why this rank | Main failure path |
|---:|---|---:|---|---|---|---|
| **1** | **1st Half — UNDER 1.5 goals** | **0.85** | MEDIUM-HIGH | FREE self-selected phase | Directly derived from the printed phase distribution: P(0)=0.56, P(1)=0.29. Getafe have no 2+ goal first half in five league games; both teams show 3/5 0-0 HT rates. Less bench-sensitive than a full-game row. | Betis score early and Getafe respond before HT, reproducing the high-phase Levante/Villarreal Betis tails. |
| **2** | **Getafe team total — UNDER 1.5 goals (90 min)** | **0.81** | FORCED RANK / MEDIUM | FREE | Only 3 league goals in 5, zero in two away league games, Mayoral unavailable, and low current attacking volume. | Betis rotation/errors give Getafe two high-quality transition/set-piece goals; an early Getafe goal opens the game. |
| **3** | **Real Betis team total — OVER 0.5 goals (90 min)** | **0.75** | FORCED RANK / MEDIUM | FREE | Betis have scored in all five league games, hold the stronger attacking-volume profile and retain deep attacking alternatives despite rotation. | Rotated attack fails to break a deep block; Soria/finishing variance produces 0-0 or 0-1. |
| **4** | **Getafe team corners — UNDER 5.5 (90 min)** | **0.69** | FORCED RANK / MEDIUM-LOW | FREE derivative | 4/5 league games below line, exactly 3 in both away league matches, ~4.0 current rate, plus explicit lack-of-natural-wingers mechanism. | Getafe concede first and spend a long trailing phase forcing crosses, blocks and clearances into 6+ corners. |
| **5** | **Combined goals — UNDER 2.5 (90 min)** | **0.63** | FORCED RANK / MEDIUM-LOW | FORCED_PAIR preferred supplied side | Centre ~2.2; Getafe low-output/away-scoring profile makes 1-0, 2-0 and 1-1 states substantial. | Betis convert superior volume efficiently or an early goal opens transitions into 2-1/3-0/3-1. |

**Supplied 1H 0.5 decision:** Under **0.56**, Over **0.44**. Under is preferred, but the line is too tight to make the top five. It is derived from the same phase distribution as Rank #1, not a separate classifier.

**Supplied FT 2.5 decision:** Under **0.63**, Over **0.37**; Under is Rank #5.

#### Coupling / representative state

- Representative state: **HT 0-0, FT Real Betis 1-0 Getafe, Getafe 3 corners** — compatible with all five ranked selections.
- Main shared #2/#3/#5 failure state: a more open Betis-led game such as **3-1**, where Betis score, Getafe reach 2, and the full total clears 2.5.
- Main #1/#4 shared failure state: an early Betis goal forces Getafe into a wide chase, simultaneously raising first-half scoring and Getafe corner volume.
- No calibrated joint-probability claim is made.

#### Projected match winner

- **Projected regulation winner: Real Betis — 0.54** `UNVALIDATED_SUBJECTIVE`.
- **Draw: 0.28; Getafe: 0.18**.
- Betis' 4-win start, current home venue, stronger attacking volume and deeper squad support the edge. It remains modest because rotation is expected, participant certainty is incomplete, and Getafe's compact style preserves a large draw band.

#### Information not confirmed / integrity flags

- Field-owner confirmed starting XIs/full benches were **not reliably captured before the 18:49 CEST freeze**; conflicting secondary lineups were not silently upgraded.
- Same-day secondary lineup material included Mayoral on the bench while same-day squad reporting said he did not travel; Mayoral is treated as unavailable and the lineup source downgraded.
- Exact cross/blocked-cross/end-line/clearance counts were not recovered; corner row is evidence-capped.
- Venue metadata conflict remains documented; La Cartuja is used based on current club-level field-owner records.
- No validated calibrated model and no same-time price snapshot: **NO VALUE DETERMINABLE**.
- No retrospective or settlement performed.
- **Current settlement status:** `UNSETTLED — PREGAME AT ISSUE`.

#### Settlement routes

- Regulation/HT score, goal minutes and participants: **LALIGA exact match record** first, cross-check club exact-match pages.
- Corners: **Getafe official exact-match stats page** first; ESPN `soccer/esp.1` `wonCorners` fallback/cross-check.
- Red cards, penalties, goalkeeper changes or stoppages: structured LALIGA/ESPN timeline with minute and score at event.

#### Sources

| Source | Contribution | Quality / limitation |
|---|---|---|
| LALIGA exact match page | Fixture, kickoff, standings, team aggregate goals/shots, referee | Primary; venue shell conflicts with club-level field-owner records |
| LALIGA Betis profile/results | Betis results; current stadium listed as La Cartuja | Primary |
| LALIGA Getafe profile/results | Getafe results and away scoring context | Primary |
| Getafe official exact-match J6 page | Fixture, La Cartuja venue, lineup availability state, H2H, settlement route | Primary club; some cached table fields stale |
| Real Betis official matchday | Current fixture/start and matchday state | Primary club; current XI not reliably exposed |
| Mundo Deportivo, 16 Sep | Llorente/Ruibal absences; Betis rotation expectation | Reputable current secondary |
| Estadio Deportivo, 16 Sep | Betis squad context; Llorente/Ruibal unavailable | Current secondary citing club squad release |
| AS Bordalás presser, 16 Sep | Andrés/Zaid recovered; lack of natural wingers; Mayoral recovery | Current secondary quoting coach |
| Estadio Deportivo, 17 Sep | Mayoral left out of travelling squad | Current same-day secondary |
| AS possible Getafe XI | Uche/Femenía/Abqar context; projected shape | Secondary projection only; not confirmed XI |
| Current LALIGA match records | First-half goal timings / 0-0 HT and late-goal patterns | Primary |
| Statz.ai current corner record | Match-by-match Getafe corners and season rates | Specialist secondary; direct width-event layer incomplete |
| Structured La Cartuja weather | ~28°C, dry/sunny, no rain in match window | Current structured forecast |
| Drive `RULES_SOCCER.md` | SFA-SOCCER; controls 20–41 | Governing methodology |
| Drive `CONTROLS.md` / `RULES_GENERAL.md` | Participant/bench cap, source/state/distribution controls | Governing methodology |
| User-supplied slate | Exact 1H 0.5 and FT 2.5 contracts | Contract source only |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| LaLiga exact-match venue shell conflicts with club-level La Cartuja records | `DATA_SOURCE_REGISTER.md` / fixture-integrity notes | Source-quality observation; **NO NEW RULE** |
| Same-day secondary XI includes a player reported out of travelling squad | `SOURCES.md` / participant provenance | Reinforces SO-P2/G14.2; **NO CHANGE** |
| Getafe lack natural wingers plus current 3-corner away outputs | `RULES_SOCCER.md` corner process | Existing direct-width mechanism applied; **NO CHANGE** |
| 1H U0.5 and U1.5 derived from one phase distribution | `RULES_SOCCER.md` control 40 | Existing sibling-line coherence applied; **NO CHANGE** |
| Nested U3.5 omitted beside U2.5 to avoid duplicate suppression thesis | `RULES_GENERAL.md` dependence/portfolio disclosure | Process note only |


---

#### Settlement and retrospective — 18 Sep 2026

- **Final status:** `SETTLED — FINAL`.
- **Final result:** Real Betis **1-0 Getafe CF**; half-time **1-0**.
- **Goal:** Abde Ezzalzouli 44' (the official event log records VAR confirmation in first-half stoppage context).
- **Corners:** Real Betis **4**, Getafe **3**.
- **Important identity correction:** the final RFEF competition record and Getafe’s exact-match page identify the venue as **Benito Villamarín**. The pre-game card selected La Cartuja after resolving conflicting metadata the wrong way. This is preserved as a **venue-identity process error**, not silently rewritten.
- **Canonical-ID audit:** no P-456 entry exists in `PREDICTION_LOG_COMBINED_4.md`; no collision was found.

##### A. Ranked-pick and winner settlement

| Rank | Frozen selection | Final target | Result |
|---:|---|---:|---|
| 1 | 1st Half **Under 1.5 goals** | 1 goal | **WIN** |
| 2 | Getafe team total **Under 1.5** | 0 | **WIN** |
| 3 | Real Betis team total **Over 0.5** | 1 | **WIN** |
| 4 | Getafe team corners **Under 5.5** | 3 | **WIN** |
| 5 | Combined goals **Under 2.5** | 1 | **WIN** |
| — | Projected regulation winner: **Real Betis** | Betis 1-0 | **WIN** |

**Supplied tighter first-half pair:** 1H Under 0.5 = **LOSS**; 1H Over 0.5 = **WIN**, because Betis scored before halftime. This pair was not in the ranked top five but is retained because it was an explicit supplied target.

**Top-of-list diagnostics:** Rank #1 = **WIN**; Wins@2 = **2**; Hit@2 = **1**; both top two = **YES**; NDCG@2 = **1.000**. All five ranked rows won; the unranked preferred 1H Under 0.5 did not.

##### B. Why each pick won

**Rank #1 — 1H Under 1.5: WIN.** The printed phase distribution assigned 0 or 1 first-half goal 85% subjective mass. One Betis goal occurred, so the broader U1.5 sibling line absorbed the late-half score. This is a good example of **threshold robustness**: the supplied U0.5 lean was fragile to any goal and lost, while U1.5 had a materially wider winning region.

**Rank #2 — Getafe team Under 1.5: WIN.** Getafe finished scoreless. The official page records only eight total shots, two on target and zero big chances versus Betis’ four. The pre-game mechanisms — low scoring output, no away league goals, Mayoral absence and limited natural width — were directionally appropriate.

**Rank #3 — Betis team Over 0.5: WIN.** Betis generated 22 shots, eight on target and four big chances, but converted only once. The pick needed only one conversion and therefore had a broad win region despite finishing variance.

**Rank #4 — Getafe corners Under 5.5: WIN.** Getafe recorded three corners. Their previous away output of three corners and the width limitation identified in the Bordalás comments were consistent with the realized territorial pattern.

**Rank #5 — full-match Under 2.5: WIN.** Only one goal was scored. Betis’ dominant volume did not translate into multiple goals, while Getafe contributed none. This was an allocation/finishing state rather than simply “both teams played slowly”.

**Projected Betis winner: WIN.** Betis’ stronger attacking volume and home edge translated into the narrow regulation victory projected.

##### C. Rank-1 review

Rank #1 won. Its superiority over the supplied U0.5 side is analytically important: both came from the same phase distribution, and the looser threshold was correctly recognized as much more robust. This is exactly the intended sibling-line coherence behavior rather than hindsight line shopping.

##### D. Top-two review

Both won. They also represented related low-scoring mechanisms, so Hit@2 should not be interpreted as independent coverage. The outcome state — Betis 1-0 — was close to the representative pre-game state. The ordering remained defensible because Rank #1 was less dependent on exact full-game participants and substitutions.

##### E. Over/under review

The main full-match Under won, while the tighter first-half Under 0.5 lost. This illustrates why “Under” is not a single team/style label; thresholds and phases must be modeled separately. A 44th-minute goal was enough to defeat U0.5 but was still fully compatible with U1.5 and FT U2.5.

No universal Getafe Under rule should be promoted. The official process record shows Betis created four big chances and 22 shots; a different finishing realization could have produced 2-0 or 3-0 without invalidating much of the pre-game territorial analysis.

##### F. What went right

- Current phase rates were explicitly reconstructed before issuing the first-half rows.
- One coherent phase distribution generated both U0.5 and U1.5 rather than contradictory independent classifiers.
- Getafe’s low attacking/corner profile was tied to a specific width/availability mechanism.
- The corner settlement route was pre-registered to Getafe’s exact-match page, which now supplies the official club statistic directly.
- The winner label, team totals and full total were coherent with the realized 1-0 state.

##### G. Major blind spot: venue identity

The pre-game card documented a conflict between a LaLiga match shell and club-level records, then chose **La Cartuja**. The final RFEF Jornada 6 record lists **Benito Villamarín**, and Getafe’s exact-match page now does the same. This is an integrity error even though both are in Seville and the weather/market conclusions were not materially driven by venue-specific history.

**Why it happened:** a generic/current club-profile venue field was allowed to outweigh the exact fixture record.  
**Smallest fix:** exact-event governing-body/match-centre metadata must own event venue over a generic club “current stadium” profile. If two exact-event primary records conflict pregame, keep venue `CONFLICTED` and avoid venue-specific signed adjustments until reconciled.

This does not require a new predictive coefficient. It is a source/identity-control enforcement issue under existing G0/G8 hierarchy.

##### H. Mandatory validation questions

1. **Confirmed starting XIs pregame?** No reliable field-owner XI/bench was captured before the freeze. The post-match Getafe record contains final lineups, but that does not prove pre-cutoff availability.
2. **Bench/reserves?** Not pregame to the required field-owner standard.
3. **Coaching info?** Pellegrini/Bordalás were known and Bordalás’ width comments were materially used.
4. **Injuries/rest/late changes?** Major Betis/Getafe availability and expected rotation were researched. Same-day conflicting Mayoral lineup data was correctly downgraded.
5. **Original sources accurate/current?** Most participant/process sources were useful; **venue resolution was wrong**.
6. **Better future sources?** For exact fixture venue, RFEF/LALIGA exact-event match record must outrank a general club profile. Getafe’s exact-match page is a strong derivative-stat lane for this fixture.
7. **Blind spots?** Venue source-priority conflict; full pregame XI/bench incompleteness.
8. **Future fix?** Enforce exact-event > generic-profile field ownership and preserve unresolved conflict when exact primary records disagree.

##### I. Source audit / settlement evidence

| Source | Contribution | Assessment |
|---|---|---|
| RFEF Jornada 6 results — https://rfef.es/es/resultados?competition=33836084&group=33836085&journey=6 | Official result **Betis 1-0 Getafe** and venue **Benito Villamarín** | Governing-body primary source |
| Getafe official exact-match page — https://www.getafecf.com/partidos/temporada-2026-2027-laliga-ea-sports-6-real-betis-vs-getafe-cf-2979 | Final, HT 1-0, goal/event log, **corners 4-3**, shots 22-8, passes, lineups/subs, venue Benito Villamarín | Primary club exact-event source; excellent for derivative stats |
| Betis official match record | Final result corroboration | Primary club |
| Pre-game LaLiga/club profile records | Created conflicting venue state | Useful but demonstrates why field ownership must be exact-event-specific |

**New-source observation:** Getafe’s exact-match page exposes corners and rich event statistics and is a strong candidate derivative source for Getafe fixtures. It should be logged as a **candidate** in `SOURCES.md` / `DATA_SOURCE_REGISTER.md`, not globally promoted after one case.

##### J. Learning / rule disposition

- **Existing source hierarchy should have prevented the venue resolution error.** Record as `PROCESS / IDENTITY ENFORCEMENT FAILURE`, not a new forecast rule.
- Sibling-line phase coherence worked well: U1.5 survived the one-goal first half while U0.5 did not.
- Candidate source discovery: exact Getafe match pages for corners/shot fields; requires repeated coverage checks before broader source promotion.
- No permanent Getafe Under coefficient or LaLiga scoring rule is created.

---


### P-457 — Cricket / Zimbabwe v Australia ODIs 2026 — Zimbabwe vs Australia, 2nd ODI

- **Canonical ID:** P-457 (mini-log sequence; combined-log reconciliation pending)
- **Sport / competition:** Cricket — Men's ODI bilateral series, Zimbabwe v Australia 2026
- **Event:** Zimbabwe vs Australia, 2nd ODI
- **Venue:** Harare Sports Club, Harare, Zimbabwe
- **Scheduled start:** 18 Sep 2026, 09:30 CAT = 18 Sep 2026, 17:30 AEST (Australia/Melbourne)
- **Game state at issue:** **PREGAME / TOSS NOT RETRIEVED AT FREEZE**. Cricket Australia's exact match centre still showed the event as Upcoming with both teams "Team to be announced"; current specialist scorecards also still displayed no toss/XIs. No post-start information is permitted into this forecast.
- **Research cutoff / final volatile freeze:** **18 Sep 2026, 17:21:49 AEST / 09:21:49 CAT**
- **Method version:** MDS-2026.09.06-v4.0
- **Population status:** EXPLORATORY — NOT SCORED for primary-performance purposes; current user direction remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.
- **Operating mode:** SPORTS_ONLY / MARKET_BLIND.

#### Identity / contract activation

- Official Cricket Australia and ICC records confirm the exact fixture, date, venue and scheduled 09:30 local start.
- User-supplied contracts are frozen exactly as **Australia match-first-innings 50-over O/U 309.5** and **Australia match-first-innings end-of-5-overs O/U 31.5**.
- The user explicitly defines "first innings" as **the team batting first**, not simply Australia's innings. Therefore these two Australia targets activate **only if Australia bat first**.
- At the frozen cutoff no reliable toss record was available. Consequently all four ranked rows below are **CONDITIONAL — ACTIVE ONLY IF AUSTRALIA BAT FIRST**. If Zimbabwe bat first, these four rows become `TARGET_NOT_ACTIVATED / NO ACTION` for this card; they must not be silently transferred to Australia's chase.
- If a sportsbook's wording instead means "Australia team innings" even when Australia chase, that is a different contract from the user's stated definition and is not modelled here.

#### Squads / availability / participant state

**Australia official squad:** Mitchell Marsh (c), Xavier Bartlett, Alex Carey, Cooper Connolly, Joel Davies, Nathan Ellis, Cameron Green, Josh Hazlewood, Travis Head, Josh Inglis, Spencer Johnson, Oliver Peake, Matthew Renshaw, Billy Stanlake, Adam Zampa.

- First-ODI XI: Marsh, Head, Connolly, Inglis, Carey, Renshaw, Peake, Bartlett, Ellis, Zampa, Johnson.
- Cameron Green missed the first ODI with **right-shoulder soreness**. Cricket Australia stated it was not considered serious; he had batted in the nets and was doing running drills, but his second-ODI availability was **not confirmed at the freeze**.
- Josh Hazlewood was deliberately managed out of the first ODI with the Test tour in mind. His second-ODI inclusion was **not confirmed at the freeze**.
- No official second-ODI XI or full match-day bench was captured before the cutoff.

**Zimbabwe official squad:** Sikandar Raza (c), Ben Curran, Blessing Muzarabani, Brad Evans, Brendan Taylor, Brian Bennett, Craig Ervine, Ernest Masuku, Graeme Cremer, Innocent Kaia, Newman Nyamhuri, Ryan Burl, Tadiwanashe Marumani, Wellington Masakadza, Wessly Madhevere.

- Richard Ngarava remains out while recovering from a **lower-back injury**.
- Tanaka Chivanga is out with an **Achilles injury**.
- Clive Madande is unavailable; Brendan Taylor returned and kept wicket in the first ODI.
- First-ODI XI: Bennett, Ben Curran, Kaia, Taylor (wk), Ervine, Raza, Madhevere, Evans, Nyamhuri, Masakadza, Muzarabani.
- No official second-ODI XI was captured at the freeze.

**Participant-state implication:** the direct phase comparator preserves the likely Marsh/Head opening combination, but Green/Hazlewood and any Zimbabwe change remain unresolved. Probabilities are therefore capped at MEDIUM rather than treated as high-certainty participant-complete forecasts.

#### Six-rung pitch / conditions audit

| Rung | Attempt | Result at freeze |
|---:|---|---|
| 1 | Rights-broadcast/toss-time pitch commentary; exact-match CA/Fox/Kayo/toss searches | **ATTEMPTED — no toss-time captain/curator/presenter strip quote recovered.** |
| 2 | `"Harare Sports Club" curator pitch`, `groundsman pitch`, board/venue searches | **ATTEMPTED — no current 18-Sep exact-strip curator statement recovered.** Historical venue profiles only. |
| 3 | Exact-match specialist facts/match centres (SportsTak, MyKhel/current scorecard searches) | **ATTEMPTED — event still marked yet-to-begin/upcoming; toss and XIs blank; no field-owner strip description.** |
| 4 | Exact-match specialist preview / ESPNcricinfo pitch-and-conditions search | **ATTEMPTED — no accessible exact ESPNcricinfo preview/strip report recovered before cutoff.** |
| 5 | Named reporting quoting curator/team management | **ATTEMPTED — no current-strip quote.** Cricket Australia's first-ODI on-site report described the 15-Sep surface as unusually grassy and later easy-paced; retained only as a same-series historical comparator, not today's strip. |
| 6 | Harare ODI historical/current-regime scoring baseline | **COMPUTED.** Cricket Australia cites long-run first-innings average ~231. The four most recent men's ODIs at Harare before this match had first-innings totals **141, 247/6, 199 and 294/8**, mean **220.25**. |

- **STRIP STATUS:** `NOT FOUND AFTER SEARCH` for today's exact pitch.
- **MATCH CONDITIONS STATUS:** `VERIFIED WEATHER / STRIP UNKNOWN`.
- Same-series comparator: the first ODI was played on an unusually grassy strip but Cricket Australia described it as **easy-paced once set**; Australia still reached 294/8.
- Weather at ~09:17 CAT: **sunny, ~22°C**, forecast high around **28°C**; no meaningful rain signal. This is a daytime ODI, so no material dew mechanism is applied.
- Mechanistic interpretation: cool morning/new-ball conditions preserve early seam/swing risk; batting should become easier once set, but today's exact grass/hardness cannot be asserted.

#### Venue / recent same-ground ODI baseline

- Cricket Australia: Harare is generally not a high-scoring ODI venue, with long-run first-innings average around **231**.
- Recent men's ODIs at Harare before this game:
  - Zimbabwe 141 vs Bangladesh (6 Jul 2026)
  - Zimbabwe 247/6 vs Bangladesh (9 Jul 2026)
  - Zimbabwe 199 vs Bangladesh (11 Jul 2026)
  - Australia 294/8 vs Zimbabwe (15 Sep 2026)
- Current four-match mean = **220.25**. This is not fitted as a universal pitch coefficient; it is the mandatory current venue/format baseline and shows that **309.5 is a very high threshold** for this ground.

#### Direct same-series phase evidence

- In the 1st ODI, Australia batted first with Marsh and Head opening and were **42/1 after exactly 5 completed overs**, clearing the supplied 31.5 line by 10.5 runs despite Head falling at 1.5 overs.
- Australia were **30/1 after 4 overs**, then Marsh took 12 from the fifth to reach 42/1.
- Australia finished **294/8**, 15.5 runs below the supplied 309.5 line.
- Full-innings mechanism: Head 4, Marsh 36, Connolly 51, Inglis 4 and Carey 27 left Australia requiring a Renshaw 109 rescue plus Peake 30 to reach 294. Zimbabwe took wickets often enough to prevent a 310+ finish; Nyamhuri took five.
- Counter-evidence: Australia's top order has substantial latent ceiling. A normal Head/Marsh/Connolly conversion day, plus a possible Green return, creates a credible 310–340 branch. The first ODI is therefore a strong comparator, not a deterministic template.

#### Conditional joint event object — **only if Australia bat first**

**Australia first 5 completed overs (30 legal balls):**
- Centre: ~**37 runs**
- Width: ~**12 runs**
- Preferred side: **Over 31.5**
- Direct comparator 42/1 carries material weight; early seam and unconfirmed exact strip keep the lower tail substantial.

**Australia 50-over first innings:**
- Centre: ~**292 runs**
- Width: ~**40 runs**
- Preferred side: **Under 309.5**
- Component logic: elite batting raises Australia far above the ~231 venue prior; direct same-series 294 is the highest-value baseline; 309.5 still requires sustained >6.19 RPO across 50 overs and is vulnerable to Harare's new-ball wickets/middle-overs slowdown.

**Coherent two-decision joint family (`UNVALIDATED_SUBJECTIVE`):**

| State | Mass |
|---|---:|
| 5-over **Over 31.5** + 50-over **Under 309.5** | 0.42 |
| 5-over **Over 31.5** + 50-over **Over 309.5** | 0.21 |
| 5-over **Under 31.5** + 50-over **Under 309.5** | 0.24 |
| 5-over **Under 31.5** + 50-over **Over 309.5** | 0.13 |
| **Total** | **1.00** |

This yields conditional marginals: **Under 309.5 = 0.66**, **Over 309.5 = 0.34**, **5-over Over 31.5 = 0.63**, **5-over Under 31.5 = 0.37**.

- `P(Rank #1 AND Rank #2)` = **0.42**.
- `P(neither preferred decision wins)` = **0.13** — the main both-fail state is a cautious/wicket-hit first five followed by a large middle/death acceleration to 310+.
- Representative state: **Australia 38/1 after 5 overs, 292/8 after 50**.

#### Ranked picks — **conditional on Australia batting first**

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Geometry | Why this rank | Primary failure path |
|---:|---|---:|---|---|---|---|
| **1** | **Australia match-first-innings 50 overs — UNDER 309.5 runs** | **0.66** | MEDIUM / CONDITIONAL | FORCED_PAIR preferred side | 309.5 is ~79 above Harare's long-run first-innings average and 15.5 above Australia's direct same-series 294. Current recent-venue mean is ~220. Australia are much stronger than that prior, hence centre ~292 rather than venue mean. | Head/Marsh/Connolly preserve wickets, Green strengthens the XI if fit, and the middle/death phases convert into 310–340. |
| **2** | **Australia match-first-innings first 5 overs — OVER 31.5 runs** | **0.63** | MEDIUM / CONDITIONAL | FORCED_PAIR preferred side | Same venue/opponent/opening pair scored 42/1 after five on the prior unusually grassy strip. 31.5 requires 6.3 RPO and Australia's opening intent is aggressive. | Muzarabani/Evans/Nyamhuri exploit cool-morning movement, take 2+ wickets and hold Australia to ~22–30. |
| **3** | **Australia match-first-innings first 5 overs — UNDER 31.5 runs** | **0.37** | MEDIUM-LOW / CONDITIONAL | FORCED_PAIR non-preferred | Early seam is the best Zimbabwe phase and Head fell in the second over in ODI1; the exact strip is unknown. | Marsh/Head repeat the direct fast-start comparator and clear 32 despite a wicket. |
| **4** | **Australia match-first-innings 50 overs — OVER 309.5 runs** | **0.34** | MEDIUM-LOW / CONDITIONAL | FORCED_PAIR non-preferred | Australia's ceiling is real and the first ODI reached 294 despite four top/middle batters failing; one additional major partnership can clear 310. | Harare baseline, regular wickets and middle-overs control hold Australia in the 270–305 band. |

**Decision interpretation:** these four rows are **two complementary O/U decisions, not four independent bets**. Preferred conditional decisions: **Australia Under 309.5** and **Australia first-five Over 31.5**.

#### Projected match winner

- **Projected eventual match winner: Australia — 0.79** `UNVALIDATED_SUBJECTIVE`.
- Zimbabwe **0.20**; tie/no-result aggregate **0.01**.
- Winner endpoint is the eventual ODI result if a result is produced under ODI/DLS rules; the winner projection is independent of which side bats first.
- Rationale: Australia won ODI1 by 59 runs despite multiple top-order failures; its batting depth and bowling resources remain materially stronger. Zimbabwe retain a real home upset branch through new-ball wickets, Nyamhuri/Muzarabani, and experienced Raza/Ervine batting.

#### Information not confirmed / integrity flags

- **TOSS_NOT_RETRIEVED_AT_FREEZE** — supplied Australia first-innings targets are not yet activated. No silent assumption that Australia bat first.
- **XI_NOT_CONFIRMED_AT_FREEZE** for both teams.
- Green second-ODI availability remains uncertain after first-ODI shoulder soreness; Hazlewood selection remains uncertain after workload management.
- Today's exact strip was not observed/reported to the six-rung standard; no weather-to-pitch inference is made.
- Exact sportsbook operator terms for reduced overs/DLS and the phrase "Australia 1st innings" were not supplied. This card follows the user's explicit first-innings definition.
- No post-start information is incorporated after 17:21:49 AEST.
- No retrospective or settlement performed.
- **Current settlement status:** `UNSETTLED — PREGAME / CONDITIONAL TARGETS PENDING TOSS`.

#### Settlement routes pre-registered

- Event/toss/XIs/result/innings total: Cricket Australia exact match centre / host-board or ICC exact-event record where exposed; structured specialist scorecard only as fallback/corroboration.
- End of first five overs: exact legal-ball/over state at **5.0 overs** from a structured ball-by-ball/scorecard, with 30 legal balls required unless the operator's contract says otherwise.
- Reduced-overs/DLS action must follow the operator's actual rules; no automatic grading from a shortened innings.

#### Sources

| Source | Link / record | Contribution | Quality / limitation |
|---|---|---|---|
| Cricket Australia exact match centre | https://www.cricket.com.au/matches/CA%3A40289 | Exact fixture/venue and pregame state; teams still TBA at freeze | Primary Australian board; not host field owner, but strong exact-event lane |
| Cricket Australia series guide | https://www.cricket.com.au/news/4573207/zimbabwe-australia-odis-one-day-internationals-harare-2026-preview-guide-tv-television-stream-broadcast-details-how-to-watch-team-squad-news-session-start-times | Schedule, 09:30 local / 17:30 AEST, squads | Primary team/board reporting |
| ICC Zimbabwe squad release | https://www.icc-cricket.com/news/zimbabwe-name-squad-for-odi-series-against-australia | Zimbabwe squad; Ngarava, Chivanga, Madande availability | Governing-body reporting |
| Cricket Australia first-ODI toss/team report | https://www.cricket.com.au/news/4576529/australia-zimbabwe-toss-teams-first-odi-harare-mitch-marsh-100-games-sikandar-raza-green-hazlewood-managed | Green shoulder soreness; Hazlewood managed; first-ODI XI; unusually grassy strip; venue average ~231 | High-quality on-site same-series report; 15-Sep strip is not today's strip |
| Cricket Australia first-ODI match report | https://www.cricket.com.au/news/4576624/australia-zimbabwe-match-report-scores-highlights-first-odi-harare-mitch-marsh-100-games-sikandar-raza-connolly-peake-renshaw-zampa | 294/8, batting roles, Renshaw/Connolly, Nyamhuri, both XIs | High-quality same-series report |
| Reuters first-ODI report | 15 Sep 2026 | 294/8 v 235, 59-run result, major performers | High-quality independent secondary |
| CricketWorld first-ODI ball-by-ball | https://www.cricketworld.com/cricket/zimbabwe-vs-australia/match/commentary/96673 | Australia 42/1 after exactly five; over-by-over early phase | Specialist secondary; exact phase corroboration route |
| ABC / Wisden Harare ODI records | Jul 6, Jul 9, Jul 11 2026 | Recent Harare first-innings totals 141, 247/6, 199 | High-quality structured secondary |
| Structured Harare Sports Club weather | Retrieved 18 Sep 2026 ~09:17 CAT | Sunny ~22°C; high ~28°C; low rain/interruption concern | Current structured weather |
| Drive `RULES_CRICKET.md` | Sports Research Drive | SFA-CRICKET, innings-order activation, phase/innings separation, pitch hard gate | Governing methodology |
| Drive `DATA_SOURCE_REGISTER.md` §6A | Sports Research Drive | Mandatory six-rung cricket conditions ladder | Governing source procedure |
| User-supplied slate | Current query | Exact 309.5 and 31.5 thresholds + explicit first-innings definition | Contract source only; operator terms not independently verified |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| Supplied Australia first-innings market cannot activate before toss under user's explicit definition | `RULES_CRICKET.md` innings-order/conditional activation | Existing control correctly applied — **NO CHANGE** |
| Australia cleared 31.5 at 5 overs on a grassy direct comparator while finishing below 309.5 | `RULES_CRICKET.md` phase-to-innings transition / direct comparator controls | Existing phase≠innings logic correctly applied — **NO CHANGE** |
| Exact 18-Sep strip unavailable despite full ladder; prior-match grass report must not be copied forward | `DATA_SOURCE_REGISTER.md` §6A / `SOURCES.md` | Existing strip-missingness control correctly applied — **NO CHANGE** |
| CA board match centre remained Upcoming/TBA inside toss window | `DATA_SOURCE_REGISTER.md` source-state/freshness | Source-latency observation; do not infer toss from silence — **NO NEW RULE** |

#### Settlement and retrospective — 19 Sep 2026

- **Final status:** `SETTLED — FINAL`.
- **Final result:** Australia **356/6 (50.0 overs)**; Zimbabwe **272 all out (48.3 overs)**. Australia won by **84 runs** and took a 2-0 series lead.
- **Toss / activation:** Zimbabwe won the toss and elected to bowl, so Australia batted first and all four conditional Australia-innings contracts activated exactly as defined in the frozen card.
- **Exact five-over state:** Australia were **29/0 after 5.0 overs**. The separately surfaced **35/0** score is the end of **6.0 overs**, not 5.0.
- **Canonical-ID audit:** fresh read of `PREDICTION_LOG_COMBINED_4.md` found no P-457 collision.
- **Original card preserved:** everything above this subsection is the frozen pre-game record. No forecast probability or rank has been rewritten after the result.

##### A. Prediction outcome

| Rank | Frozen selection | Final target | Result | Settlement |
|---:|---|---:|---|---|
| **1** | Australia 50-over first innings **UNDER 309.5** | **356/6** | **LOSS** | Australia cleared the line by 46.5 runs. |
| **2** | Australia first 5 overs **OVER 31.5** | **29/0** | **LOSS** | Australia finished 2.5 runs below the line at exactly 5.0 overs. |
| **3** | Australia first 5 overs **UNDER 31.5** | **29/0** | **WIN** | Exact complement of Rank #2. |
| **4** | Australia 50-over first innings **OVER 309.5** | **356/6** | **WIN** | Australia cleared the line by 46.5 runs. |
| — | Projected eventual winner: **Australia** | Australia by 84 runs | **WIN** | Final ODI result; no DLS/no-result ambiguity. |

**Forced-pair decision view:** preferred 50-over Under 309.5 = **LOSS**; preferred first-five Over 31.5 = **LOSS**. The four rows are two complementary decisions, not four independent trials.

**Top-of-list diagnostics:** Rank #1 = **LOSS**; Hit@2 = **0**; Wins@2 = **0/2**; both top two won = **NO**; binary NDCG@2 = **0**. The four ranked rows produce a descriptive mean Brier score of **0.4163** versus the binary 0.25 reference baseline. This remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** and is not a calibration claim. The projected winner was correct.

##### B. Why each pick won or lost

**Rank #1 — Australia Under 309.5: LOSS.** The Under was built primarily from Harare's low long-run/recent first-innings environment and Australia's 294/8 in the first ODI. The core process error was that the card did not give enough mass to Australia's already-identified batting ceiling. The first ODI had reached 294 despite failures from several top/middle-order batters, which was evidence that a more normal conversion day could push the same batting unit well beyond 310. That exact ceiling branch materialised: Travis Head made **112 from 84**, Mitchell Marsh **53 from 63**, Cooper Connolly **78 from 69**, and Ollie Peake added **41* from 18**. Australia reached 356 despite the pitch slowing somewhat through the middle overs. The venue prior was directionally useful, but it was overweighted relative to current batting quality and the direct same-series evidence near the supplied line.

**Rank #2 — first-five Over 31.5: LOSS.** The strongest support was Australia's 42/1 after five in the first ODI, but the frozen card also identified cool-morning new-ball movement and the unknown exact strip as the main kill path. That early-risk branch occurred. Zimbabwe's new-ball bowlers found movement, Marsh survived a difficult chance first ball, and Australia were only 29/0 after five. A single direct 42-run comparator was not enough to justify a 0.63 Over probability with the exact strip unresolved.

**Rank #3 — first-five Under 31.5: WIN.** This lower-ranked complement captured the early seam/movement state correctly. The important point is that the Under did **not** imply a low full-innings total. Australia preserved both wickets and accelerated sharply immediately afterwards.

**Rank #4 — Australia Over 309.5: WIN.** The stated upside mechanism was a normal or strong Head/Marsh/Connolly conversion day plus enough middle/death support. It occurred even without Cameron Green. Australia were 35/0 after six, **78/0 after ten**, put on **130 for the first wicket**, and then received both Connolly's middle-order acceleration and Peake's late 41* cameo. The Over therefore won through a known ceiling path rather than an entirely unforeseen event.

##### C. Rank-1 failure review

Rank #1 was first because 309.5 sat well above Harare's long-run first-innings average (~231), above the recent four-match venue mean (~220), and 15.5 runs above Australia's first-ODI 294. That reasoning was understandable but **too venue-heavy for this exact current-regime batting unit**.

The most important knowable pre-game fact was not merely that Australia had made 294. It was that they had made 294 **despite multiple top/middle-order failures**. That should have widened the upper tail materially. The frozen card did name the correct failure route — normal Head/Marsh/Connolly conversion producing a 310–340 branch — but it remained only a secondary branch while the Under was assigned 0.66.

The event also realised the card's explicit “both preferred decisions fail” state: **a cautious/wicket-risk first five followed by a major middle/death acceleration to 310+**. That state had been assigned only **0.13** joint mass. One realised event cannot calibrate that number, but the available same-series evidence supports the conclusion that the branch deserved more structural attention before the ranking was frozen.

Should another row have ranked first? Hindsight alone does not justify simply promoting the eventual winning complement. The defensible process conclusion is narrower: **Rank #1 confidence was too high**, and the full-innings distribution should have carried substantially more high-score width. The smallest prospective fix is conditional phase-to-innings modelling, not a blanket Australia-Over rule.

##### D. Top-two review

Both top-two selections failed. They were not redundant bets, but they were jointly vulnerable to one coherent state that had already been identified: **slow first five + strong later acceleration**. That is exactly what occurred.

The relative ordering of R1 (0.66) and R2 (0.63) was not the main problem. The larger issue was that both were presented above 0.60 while the joint object gave insufficient emphasis to their shared failure state. Future top-two construction should print the full-innings distribution conditional on a low, central and high first-five state before assigning the final ordinal.

##### E. Over/Under and phase-to-innings review

This match is a particularly clean example of why a short phase and a full innings cannot be linked by simple directional extrapolation:

- **5 overs:** 29/0 — Under 31.5 won.
- **6 overs:** 35/0.
- **10 overs:** 78/0 — Australia added 49 runs in overs 6–10.
- **18.6 overs:** 130/1 — the opening stand had transformed the innings.
- **50 overs:** 356/6 — full-innings Over 309.5 won comfortably.

The pitch did slow somewhat in the middle overs, which was one of the pre-game Under mechanisms, but Australia had preserved enough wickets and generated enough scoring surplus that the slowdown was not sufficient. This supports the existing phase-versus-innings separation principle and strengthens the already-open `C-CRIC-PHASE-CONDITIONAL-INNINGS` candidate. It does **not** justify a new signed Over preference.

##### F. What went right

- The conditional activation rule was correct: no Australia innings contract was activated until Australia actually batted first.
- The card explicitly separated the first-five and full-innings processes rather than treating them as one market.
- The exact “slow first five, later 310+ acceleration” kill path was identified before the match.
- The projected winner **Australia** was correct. Australia also showed the broader team-strength edge that the 0.79 winner call was based on, dismissing Zimbabwe for 272 and winning by 84 runs.
- The exact-strip evidence gap was disclosed instead of inventing pitch characteristics.
- Green/Hazlewood availability uncertainty was not fabricated into certainty at issue.

##### G. Blind spots and future handling

- **Venue prior overweighting:** Harare's generic/recent average was too influential relative to Australia's current batting strength. Future cards should shrink venue history against current opponent-adjusted batting/attack quality rather than use the venue mean as an implicit anchor.
- **Direct-comparator interpretation:** 294/8 with several top-order failures was treated mainly as evidence below 309.5 rather than also as strong upper-tail evidence. Future same-series comparators must record whether the score was achieved with normal, weak or exceptional conversion.
- **Phase-to-full conditional state:** the model named but underrepresented a low first-five / high full-innings pathway. Future linked-phase cards should explicitly solve the full-innings distribution conditional on low/central/high phase outcomes.
- **Single-match first-five comparator:** 42/1 in ODI1 carried too much directional weight for R2 despite missing exact-strip evidence and known new-ball movement risk.
- **Fielding variance:** Marsh was reprieved first ball and Zimbabwe also missed later chances. These contributed to the realised ceiling but are mostly stochastic execution events, not a pre-game information failure.
- **Source latency:** Cricket Australia's match-centre state lagged the actual match. The user has now explicitly authorised ESPNcricinfo/Cricbuzz as structured cricket fallback sources when official feeds lag.

##### H. Mandatory validation questions

| Question | Retrospective answer |
|---|---|
| Confirmed starting lineups obtained at issue? | **No.** The frozen card explicitly recorded `XI_NOT_CONFIRMED_AT_FREEZE` for both sides. Post-start lineups are not backfilled into the pre-game evidence state. |
| Bench/reserve/rotation context obtained? | **Squads and major availability issues yes; final match-day reserves were not fully known at freeze.** |
| Coaching/captaincy information material? | Captain/toss decision became relevant to activation; no coaching surprise is required to explain the result. |
| Injuries/rest/availability checked? | **Yes, materially:** Green shoulder status, Hazlewood management and Zimbabwe injuries were checked. Green did not play; Hazlewood returned. |
| Original sources sufficiently current? | Strong for pregame identity/squads, but the official match-centre final state lagged. |
| Better sources available? | **Yes:** Cricbuzz/ESPNcricinfo structured scorecards and ball-by-ball are acceptable fallback lanes under the user's explicit instruction when official cricket feeds lag. |
| Blind spots? | Upper-tail weighting, phase-to-full conditional linkage, single-comparator overconfidence, source latency. |
| Future accounting? | Conditional phase tree; current-regime batting-strength shrinkage; explicit ceiling-state mass; fallback structured scorecard route. |

##### I. Source audit

- **Cricket Australia match/innings report:** https://www.cricket.com.au/news/4578209/match-report-second-odi-zimbabwe-australia-harare-sports-club-hazlewood-stanlake-return-head-century-ollie-peake — Australia 356/6; Head 112, Marsh 53, Connolly 78, Peake 41*; current XI and innings mechanism; notes that the dry Harare pitch slowed scoring somewhat through the middle. **High-quality team/board report.**
- **Cricbuzz final commentary:** https://www.cricbuzz.com/live-cricket-scores/152742/vs-australia-2026-09-18-harare-sports-club — Australia 356/6, Zimbabwe 272 in 48.3, Australia won by 84 runs. **Structured specialist final source authorised by the user for cricket fallback use.**
- **Cricbuzz final scorecard:** https://m.cricbuzz.com/live-cricket-scorecard/152742/zim-vs-aus-2nd-odi-australia-tour-of-zimbabwe-2026 — batting/bowling figures and fall of wickets. **Structured specialist scorecard.**
- **Cricbuzz match report:** https://m-aws.cricbuzz.com/cricket-news/140219/heads-century-leads-australias-clinical-win — final 84-run result and causal match narrative. **High-quality specialist secondary.**
- **Sky Sports / independent ball-by-ball corroboration:** exact over summaries show Australia **29/0 after 5 overs** and **35/0 after 6**. Used only to pin the exact 5.0-over contract boundary where the accessible Cricbuzz scorecard surfaced the six-over state more readily.
- **Drive `RULES_CRICKET.md` / `DATA_SOURCE_REGISTER.md`:** official/field-owner first, with legality-reconciled structured scorecards/ball-by-ball for exact phases and settlement.

**Learning disposition:** P-457 strengthens the existing phase-to-full-event conditional-modelling candidate and the existing “weighted kill path, not prose only” control. It does **not** justify a permanent Over rule or retrospective fitted coefficient.

---

### P-458 — Baseball / NPB Central League — Chunichi Dragons @ Yomiuri Giants

- **Canonical ID:** P-458 (mini-log sequence; fresh reconciliation found no P-458 collision in `PREDICTION_LOG_COMBINED_4.md`)
- **Sport / competition:** Baseball — Nippon Professional Baseball (NPB), Central League, 2026 regular season
- **Event:** Chunichi Dragons @ Yomiuri Giants
- **Official event identity:** NPB 2026-09-18, Giants–Dragons game 24 (`G-D-24`)
- **Venue:** Tokyo Dome, Tokyo, Japan
- **Scheduled start:** 18 Sep 2026, 18:00 JST = 18 Sep 2026, 19:00 AEST
- **Game state at issue:** `PREGAME`; official exact-event page still showed before game at the final pre-start refresh.
- **Research cutoff / final volatile refresh:** **18 Sep 2026, 17:54:53 JST / 18:54:53 AEST**
- **Method version:** MDS-2026.09.06-v4.0 / SFA-BASEBALL
- **Population status:** EXPLORATORY — NOT SCORED; LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE
- **Operating mode:** SPORTS_ONLY / MARKET_BLIND
- **Supplied contracts:** Chunichi +1.5; Yomiuri -1.5; Combined Total O/U 5.5.

#### Participants / availability / event context

- Official probable starters: **Haruto Inoue (Yomiuri, LHP)** and **Yumeto Kanemaru (Chunichi, LHP)**.
- Inoue entered at **10-7, 2.30 ERA, 125.1 IP, 123 K, 28 BB**. Kanemaru entered at **5-10, 2.75 ERA, 147.1 IP, 132 K, 31 BB**.
- Same-starter/same-venue comparator, 10 Sep: Yomiuri won **5-3**; Inoue 6.1 IP/3 ER/9 K/0 BB; Kanemaru 6 IP/3 ER.
- Yomiuri officially registered **Naoki Yoshikawa** and **Misaki Sasahara** on 18 Sep and deregistered **Trey Cabbage**. Same-day Japanese reporting had Yoshikawa returning after a left-hamstring absence. **Shunsuke Urata** had been deregistered a day earlier with a reported right-elbow ligament injury.
- Chunichi officially registered **Ryuku Tsuchida** and **Yutaro Itayama** and deregistered **Mikiya Tanaka** under the infectious-disease special rule.
- Exact official batting orders and full game-day benches were not reliably retrieved before the cutoff: `STARTING_LINEUPS_NOT_RETRIEVED_AT_FREEZE` / `BENCH_NOT_RETRIEVED_AT_FREEZE`.
- Official standings entering the game: **Yomiuri 70-59-2 (.543)**; **Chunichi 57-74-2 (.435)**. Yomiuri home 34-30-2; Chunichi road 21-41-2; Yomiuri season H2H 13-10.
- Official team snapshot had both clubs on **442 runs**; Yomiuri team ERA **2.89**, Chunichi **3.18**.
- Nine 2026 Yomiuri–Chunichi games at Tokyo Dome before this fixture were **5-4 Yomiuri**, 49 combined runs / 9 = **5.44/game**.
- NPB Central League had no DH in 2026 and regular-season games could finish tied after 12 innings.
- The maintained Drive did **not** contain a formally derived NPB +1.5 cushion band or exact Tokyo Dome 5.5 distribution. MLB geometry was not transferred. Flags: `NPB_1.5_BAND_NOT_FIELD_OWNER_DERIVED`, `TOKYO_DOME_5.5_EXACT_RATE_NOT_DERIVED`.

#### Joint object / ranked picks

Central budget: approximately **Yomiuri 3.1 – Chunichi 2.6**, total centre **5.7–5.8** with broad baseball width.

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Geometry | Main rationale / failure path |
|---:|---|---:|---|---|---|
| **1** | **Chunichi Dragons +1.5** | **0.62** | FORCED RANK / LOW-MEDIUM; NPB band not derived | FORCED_PAIR preferred | Yomiuri only modest winner edge in a low-centre matchup; Kanemaru quality and close states protect +1.5. Fails if Inoue suppresses Chunichi and Yomiuri creates multi-run separation. |
| **2** | **Combined Total OVER 5.5** | **0.53** | FORCED RANK / LOW-MEDIUM; exact venue rate not derived | FORCED_PAIR preferred | Centre slightly above line; same starters produced eight runs eight days earlier; both teams retain HR/sequencing tails. |
| **3** | **Combined Total UNDER 5.5** | **0.47** | FORCED RANK / LOW-MEDIUM | FORCED_PAIR non-preferred | Strong starter ERAs, Central League pitcher batting and rested relief create a material low branch. |
| **4** | **Yomiuri Giants -1.5** | **0.38** | FORCED RANK / LOW-MEDIUM; NPB band not derived | FORCED_PAIR non-preferred | Requires two-plus-run separation in addition to the Yomiuri winner thesis. |

- **Projected official NPB winner:** **Yomiuri 0.55**, Chunichi 0.43, official tie 0.02 (`UNVALIDATED_SUBJECTIVE`).
- **Winner endpoint:** official NPB result through the 12-inning cap.
- **Operator action terms:** tie/suspension/listed-pitcher terms not supplied (`UNKNOWN_DEFINITION`).
- **Current settlement status:** `UNSETTLED — FROZEN PREGAME VIEW`.
- **No retrospective performed.**

#### Sources

| Source | Link / record | Contribution | Quality / limitation |
|---|---|---|---|
| NPB schedule / probable pitchers | https://npb.jp/bis/eng/2026/games/s20260918.html ; https://npb.jp/announcement/starter/ | Fixture/time/venue/starters | Primary / field owner |
| NPB exact game page | https://npb.jp/scores/2026/0918/g-d-24/box.html | Event identity and pregame state | Primary / field owner |
| NPB standings / team batting / pitching | https://npb.jp/bis/eng/2026/stats/ | Team records/aggregates | Primary |
| NPB player records | 2026 Inoue / Kanemaru records | Starter season lines | Primary |
| NPB roster transactions | https://npb.jp/announcement/roster/ | 17–18 Sep registrations/deregistrations | Primary |
| Nikkan Sports same-day reporting | 18 Sep 2026 | Yoshikawa / Urata context | High-quality Japanese secondary |
| Official/structured Sep10 game record | Yomiuri 5-3 Chunichi | Same-starter comparator | Primary + corroboration |
| Drive baseball/general/source/base-rate files | Sports Research Drive | Governing process and missing-band treatment | Governing |
| User-supplied slate | Prior query | Exact ±1.5 and O/U 5.5 contracts | Contract source only |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| NPB +1.5 cushion band absent | `BASE_RATES_REGISTER.md` | DATA GAP — derive prospectively; no guessed identity |
| Tokyo Dome exact 5.5 distribution not reproduced | `BASE_RATES_REGISTER.md` / `DATA_SOURCE_REGISTER.md` | DATA GAP / future derivation candidate |
| Native Japanese reporting materially improved roster context | `LEARNING_REGISTER.md` `L-067` / `SOURCES.md` | Existing promoted process applied; NO NEW RULE |

---

#### Settlement and retrospective — 19 Sep 2026

- **Final status:** `SETTLED — FINAL`.
- **Official final:** Yomiuri Giants **2-0** Chunichi Dragons at Tokyo Dome. The game was 0-0 through eight innings before Tomoya Izumiguchi hit a **two-run walk-off home run in the bottom of the ninth**.
- **Canonical-ID audit:** fresh read of `PREDICTION_LOG_COMBINED_4.md` found no P-458 collision.
- **Original card preserved:** everything above this subsection is the frozen pre-game record.

##### A. Prediction outcome

| Rank | Frozen selection | Final | Result | Exact settlement |
|---:|---|---:|---|---|
| 1 | Chunichi Dragons +1.5 | Chunichi lost by 2 | **LOSS** | A +1.5 side loses when its final deficit is 2. |
| 2 | Over 5.5 runs | 2 total runs | **LOSS** | Final total stayed 3.5 runs below the line. |
| 3 | Under 5.5 runs | 2 total runs | **WIN** | Final total stayed below 5.5. |
| 4 | Yomiuri Giants -1.5 | Yomiuri won by 2 | **WIN** | The two-run walk-off cleared -1.5 by the minimum possible half-run margin. |
| — | Projected winner: Yomiuri | Yomiuri 2-0 | **WIN** | Official NPB regulation endpoint. |

**Diagnostics:** Rank-1 = **LOSS**; Hit@2 = **0**; Wins@2 = **0/2**; binary NDCG@2 = **0**. Winner projection = **correct**.

##### B. Why each pick won or lost

**R1 Chunichi +1.5 — LOSS.** The core pre-game close-game thesis was not broadly wrong: the match was scoreless through eight innings and Chunichi starter Yumeto Kanemaru held Yomiuri down until the ninth. But a +1.5 contract is exposed to a single two-run swing. Izumiguchi's walk-off two-run homer converted a 0-0 game directly into a two-run final margin, bypassing the one-run state that the cushion needed. The card named late Yomiuri separation as a kill path, but assigned too little mass to the discrete two-run-home-run branch.

**R2 Over 5.5 — LOSS.** Both starters controlled the game and neither offence created sustained scoring. With a pre-game centre only around 5.7-5.8, the Over at 0.53 was fragile. The exact result demonstrates that the card's low-scoring evidence should have had more ordinal weight: Central League pitcher batting, strong starter form and a cluster of low Tokyo Dome/H2H totals were all already available.

**R3 Under 5.5 — WIN.** The starter-dominance and run-suppression mechanisms materialised almost perfectly. The only scoring event was the final swing. The Under winning does not establish a universal NPB Under preference; it shows the event-specific centre was too low to justify ranking Over above its complement.

**R4 Yomiuri -1.5 — WIN.** This row won in the narrowest plausible way: a two-run walk-off from a tie. It therefore does **not** validate a broad blowout thesis. The process should classify it as a tail/separation success, not evidence that Yomiuri controlled the contest.

##### C. Rank-1 failure review

R1 was ranked first because the forecast expected a close game and the +1.5 cushion was supposed to absorb a narrow Yomiuri win. The logic was reasonable but incomplete because **no NPB 1.5 cushion band had been field-owner-derived**. The precise failure state was available pre-game: a home team can win by 2+ on one late swing even in a very low-total game. Under the existing `G-L1` weighted-kill-path requirement, that branch needed explicit probability mass, not just prose.

A different row should reasonably have ranked higher. Given the printed event centre and the strong starter evidence, **Under 5.5** was more internally coherent than Over 5.5 and had a stronger case for a top-two position. The smallest prospective fix is not “fade +1.5”; it is to derive the NPB one-run/2+ margin band and to represent walk-off two-run-home-run states explicitly in the separation tree.

##### D. Top-two review

Both top-two selections lost. The problem was not simple bad luck across two independent theses: R1 and R2 were jointly vulnerable to the same misallocated game-shape mass. The forecast wanted “close but enough scoring to edge Over”; the realised state was “extremely close and extremely low scoring, then one terminal two-run swing.” Future top-two construction should avoid giving two top slots to rows whose support comes from an internally narrow and weakly justified score corridor.

##### E. Total review

The Under won by a large distance. The pre-game total centre itself was near the line, but the available starter evidence was stronger than the offensive ceiling evidence. No weather/venue surprise was required to explain the low total. The lesson is event-specific: when the centre is below/near a total and the dominant mechanisms are starter suppression, do not rank the opposite side above 0.5 without a clearly weighted offensive or bullpen route.

##### F. What went right

- Projected winner Yomiuri was correct.
- The card recognised a low-centre game and strong starting pitching.
- The missing NPB +1.5 base-rate band was honestly disclosed rather than fabricated.
- The lower-ranked Under correctly captured the dominant run environment.

##### G. Blind spots and future handling

- **Walk-off margin geometry:** a two-run homer can instantly defeat +1.5 in a tied low-total game. Add this as a weighted branch in the existing baseball separation tree.
- **No NPB cushion band:** derive prospectively from NPB official completed games before relying heavily on +1.5/-1.5 identity arithmetic.
- **Lineup/bench incompleteness at freeze:** exact posted orders and full benches were not retrieved; keep the evidence cap and improve source retrieval rather than retrospectively inventing participant certainty.

##### H. Mandatory validation questions

| Question | Retrospective answer |
|---|---|
| Confirmed starters / starting lineups obtained? | **Starters yes; full posted batting orders were not retrieved to gate standard at issue.** |
| Bench/reserve/substitution context obtained? | **No, not fully.** This was disclosed pre-game. |
| Coaching information obtained/material? | Manager context was not decision-driving; no post-result coaching surprise explains the outcome. |
| Injuries/rest/availability adequately checked? | Material starter/rest context was checked, but full match-day participant completeness was limited. |
| Sources accurate/current? | Pre-game starter sources were useful; settlement is controlled by official NPB. |
| Better sources available? | **Yes:** official NPB game page/order/bench tabs should be opened directly once posted. |
| Blind spots? | Walk-off two-run separation mass and unresolved NPB 1.5 band. |
| Future accounting? | Derive NPB band; explicitly weight tied-bottom-9 two-run-HR and other 2+ terminal states. |

##### I. Source audit

- **NPB official exact game:** https://npb.jp/scores/2026/0918/g-d-24/ — final 2-0, inning line, pitchers, lineups and Izumiguchi ninth-inning two-run homer. **Primary settlement source.**
- NPB monthly schedule: https://npb.jp/games/2026/schedule_09.html — independent official final confirmation.

**Learning disposition:** existing `G-L1`/separation controls were sufficient in principle but under-executed. No permanent new predictive rule from one game. `NPB_1.5_BAND_NOT_DERIVED` remains a prospective data task for `BASE_RATES_REGISTER.md`.

---

### P-459 — AFL / 2026 Toyota AFL Finals Series — Sydney Swans vs Fremantle Dockers, Preliminary Final

- **Canonical ID:** P-459 (mini-log sequence; fresh reconciliation found no P-459 collision in `PREDICTION_LOG_COMBINED_4.md`)
- **Sport / competition:** Australian Football — AFL men's, 2026 Toyota AFL Finals Series, Second Preliminary Final
- **Event:** Sydney Swans vs Fremantle Dockers
- **Venue:** Sydney Cricket Ground (SCG), Sydney, NSW
- **Scheduled start:** **18 Sep 2026, 19:40 AEST**
- **Game state at issue:** `PREGAME` at latest research refresh; no first-bounce performance information used.
- **Research cutoff / latest volatile refresh:** **18 Sep 2026, 19:26:37 AEST**. The user explicitly requested continued late-news monitoring rather than an early freeze. Selected teams and late news were refreshed inside the final pre-bounce window. No information first learned after the bounce may revise this card.
- **Method version:** MDS-2026.09.06-v4.0 / SFA-AFL
- **Population status:** PRIMARY_SCORED sport population, while this running log remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.
- **Operating mode:** SPORTS_ONLY / MARKET_BLIND.
- **Supplied contracts:** Fremantle -11.5; Sydney +11.5; Combined Total O/U 189.5.
- **Self-selected candidates:** standard player 1+ goal milestones, labelled `MODEL_PROPOSED`; operator availability/price not independently verified and no value claim is made.

#### Identity / rules / endpoint validation

- AFL and club field-owner pages verify **Sydney v Fremantle**, SCG, Friday 18 Sep, **7:40pm AEST**, for a place in the Grand Final.
- Finals cannot end drawn under the 2026 competition rules; if level after the fourth quarter, extra time is played until a winner emerges.
- **Potential-winner endpoint:** eventual preliminary-final winner including AFL finals extra time.
- Exact sportsbook treatment of the supplied handicap/total if extra time is required was not supplied. Research-grade line/total probabilities below are anchored to the **end of the fourth quarter**; operator action is `UNKNOWN_DEFINITION` if its terms include extra time.

#### AF-P gate status / selected teams / availability

**AF-P1 — PASS.** AFL men's preliminary final, 2026 rules, 75-rotation cap and finals extra-time structure verified from the governing Drive rule set and AFL fixture.

**AF-P2 — SUBSTANTIALLY VERIFIED; final substitute/late-change detail incomplete.**
- Sydney forced changes: **IN Lewis Melican, Justin McInerney; OUT Callum Mills (ACL/knee), Harry Cunningham (calf)**.
- McInerney returns for his first AFL match since Round 13 after a significant hamstring injury: positive wing/link exposure, but with conditioning/full-match uncertainty.
- Melican returns to improve Sydney's tall-defender matchup resources.
- **Joel Amartey** was not recalled. Sydney retained the QF forward setup after Logan McDonald 6, Charlie Curnow 5, Tom Papley 5 and Hayden McLean 3 against Brisbane.
- Sydney also remains without **Isaac Heeney, Nick Blakey, Chad Warner, Riley Bice and James Jordon**, all unavailable for the remainder of the 2026 season/finals under club suspensions. This is a major current-regime midfield/transition/defensive-depth deficit rather than new late news.
- Fremantle named an **unchanged side** from the 120-106 semi-final win over Geelong.
- **Brennan Cox** was not rushed back from a calf injury and was directed to the WAFL Grand Final. Brandon Walker was not recalled after the prior ankle issue. Fremantle therefore has strong continuity but is not at theoretical maximum list strength.
- Latest official-domain searches inside the final pre-bounce window did **not** recover a separate current final-interchange/substitute/late-change bulletin. The selected teams above are the last independently verified pre-bounce participant state. `FINAL_SUBSTITUTE_NOT_RETRIEVED` is retained rather than asserting no late change.
- **Coaches:** Dean Cox (Sydney); Justin Longmuir (Fremantle).

#### AF-P3 / AF-P4 — venue and conditions

- Venue: SCG, outdoor.
- Current SCG-area conditions around 19:15 AEST were mostly clear and ~22°C. Match-window forecast showed essentially **0% precipitation**; BOM Moore Park indicated north-easterly/easterly winds in the afternoon becoming **light during the evening**.
- No rain-suppression sign is used.
- Exact near-bounce ground-level wind direction mapped to the SCG scoring ends was **not independently verified to AF-P4's full standard**. Therefore `AF-P4_PARTIAL` applies: total and handicap rows are capped at **LEAN** and width is increased instead of treating wind as exactly neutral.

#### Team-strength / home-away baseline

Home-and-away season:
- **Fremantle:** **19-4, 76 points, 137.2%**, minor premier; **99.4 points/game for, 72.4 against**; home 11-0, away 8-4.
- **Sydney:** **18-5, 72 points, 136.1%**; league-best **110.6 points/game for**, 81.3 against; **11-1 at home**.
- Fremantle owns the stronger defensive season; Sydney owns the stronger scoring season and elite home profile.

#### Current territory / shot-creation state

Current structured statistical snapshots including available finals:
- Sydney: approximately **60.8 inside-50s/game**, **14.0 marks inside 50**, **38.0 clearances**, **14.5 centre clearances**, **138.9 contested possessions**.
- Fremantle: approximately **54.3 inside-50s/game**, **13.8 marks inside 50**, **35.5 clearances**, **13.2 centre clearances**, **129.1 contested possessions**, with the stronger ruck-hitout profile.
- These descriptive secondary rates establish that a **high-shot branch is genuinely available**, as required for a men's total above 180, but do not force an Over because Fremantle's defensive suppression and conversion uncertainty remain substantial.

#### Finals / recent mechanism audit

**Sydney qualifying final — beat Brisbane 141-88 at the SCG**
- Logan McDonald **6**, Charlie Curnow **5**, Tom Papley **5**, Hayden McLean **3** goals.
- The 53-point result shows the depleted Sydney side retains a high shot/score ceiling. It is not copied forward as a points-rate coefficient.
- Mills' injury occurred during this match, so Sydney's defensive structure tonight is reshuffled.

**Fremantle qualifying final — lost Hawthorn 40-72**
- Fremantle's forward process was heavily suppressed, a real low-total / Sydney-win branch. It is not assumed to repeat automatically.

**Fremantle semi-final — beat Geelong 120-106**
- Fremantle's response was strongly driven by centre-square/clearance work; Luke Jackson was a major ruck/midfield influence.
- The 40-to-120 swing across consecutive finals is treated as **distribution width and game-state sensitivity**, not as permission to choose whichever recent total supports the desired side.

**Round 18 — Fremantle beat Sydney 111-73 at Optus**
- Sydney led by as much as 25; Fremantle was goalless in the first half, then scored **100 points after half-time** and seven unanswered late.
- Second-half mechanism: contested possession **80-53**, clearances **25-15**, inside-50s **40-22** to Fremantle.
- Charlie Curnow still kicked **5** for Sydney.
- Continuity is incomplete: Logan McDonald was sidelined in that meeting and Sydney's current forward configuration is materially stronger, while tonight is at the SCG after Sydney's extra week of rest.
- R18 therefore supports Fremantle's **late-separation / midfield-domination branch**, not a deterministic -11.5 call.

#### Player-goal candidate evidence

**Charlie Curnow — 1+ goal**
- Current 2026 record: **74 goals in 23 games, 3.2/game**, around **5.5 shots at goal/game**.
- Kicked **5** in the qualifying final and **5 against Fremantle in R18**.
- Main failure: Fremantle's league-best defence wins territory/entry quality, or Sydney's limited chances are allocated to other forwards.

**Jye Amiss — 1+ goal**
- Current record: **61 goals in 24 games, 2.5/game**.
- Available milestone record: **21/24 games with 1+ goals (88%)**, 17/24 with 2+.
- Finals: **1 vs Hawthorn, 2 vs Geelong**; R18 vs Sydney: **2**.
- Main failure: Sydney pressure suppresses entries and Melican/McCartin control the tall matchup.

**Logan McDonald — 1+ goal**
- Current record: **48 goals in 22 games, 2.2/game**.
- Official AFL reporting: **15 consecutive games with a goal, 12 multiple-goal games**, culminating in six against Brisbane.
- He did not play in R18, so that H2H does not measure tonight's current Sydney forward mix.

#### Joint score / conversion / separation object

**Central four-quarter budget (`UNVALIDATED_SUBJECTIVE`):**
- Sydney centre: ~**90**
- Fremantle centre: ~**94**
- Combined centre: ~**184**
- Central margin: Fremantle by ~**4**
- Width remains substantial because both teams have demonstrated high-shot/high-conversion ceilings and suppression/late-separation branches.

**Conversion / shot-volume branches**
- **Lower / suppression:** ~165–175 combined.
- **Central:** ~180–190 combined.
- **High-shot / upper-conversion:** ~205–215+, requiring both teams to sustain high entry volume and convert efficiently.
- Because ordinary conversion branches can cross 189.5, the total is `INSIDE_CENTRAL / LEAN`, not a robust high-confidence Under.

**Four-quarter winner / margin family (`UNVALIDATED_SUBJECTIVE`):**
- Sydney regulation win: **0.48**
- Fremantle regulation win: **0.51**
- Regulation draw reaching extra time: **0.01**
- Eventual winner after allocating the extra-time branch: **Fremantle 0.52 / Sydney 0.48**.

**Supplied handicap geometry**
- The Drive's `BASE_RATES_REGISTER.md` has **no derived AFL 11.5-point cushion band**. `AFL_11.5_BAND_NOT_DERIVED` applies and no other sport's band is transferred.
- Coherent subjective margin-tree queries, **not** claimed G-L24 identities:
  - Sydney +11.5 ≈ **0.62**
  - Fremantle -11.5 ≈ **0.38**
- Under the Drive fail-closed rule, neither handicap may be overall Rank #1.

**Supplied total family**
- Under 189.5 ≈ **0.57**
- Over 189.5 ≈ **0.43**
- Total evidence capped at LEAN because AF-P4 is partial and the line sits inside meaningful conversion width.

**Representative central state:** Fremantle **94-90 Sydney** (184 points): Fremantle wins, Sydney +11.5 covers, Under 189.5 wins.

#### Ranked picks — most likely to least likely

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Candidate type | Why this rank | Primary failure path |
|---:|---|---:|---|---|---|---|
| **1** | **Charlie Curnow — 1+ goal** | **0.84** | MEDIUM-HIGH | FREE / MODEL_PROPOSED | Elite 2026 scoring/shot exposure; five in QF and five in direct Freo matchup; primary Sydney target. | Freo's defence wins territory/entry quality or allocation/finishing variance. |
| **2** | **Jye Amiss — 1+ goal** | **0.82** | MEDIUM-HIGH | FREE / MODEL_PROPOSED | 21/24 1+ record, 61 goals, scored in both finals and twice vs Sydney in R18. | Sydney pressure starves Freo's tall forwards; Melican/McCartin win matchup. |
| **3** | **Logan McDonald — 1+ goal** | **0.81** | MEDIUM-HIGH | FREE / MODEL_PROPOSED | Officially 15 straight games with a goal, 12 multiples; six-goal QF; current forward setup retained. | Freo denies clean entries or Sydney scoring is allocated elsewhere. |
| **4** | **Sydney Swans +11.5** | **0.62** | LEAN / `AFL_11.5_BAND_NOT_DERIVED` | FORCED_PAIR preferred supplied side | Freo is only a slight eventual winner in the joint object; Sydney is 11-1 at home with extra rest and elite forward ceiling, so a 12+ Freo win is narrower than close-Freo or Sydney-win states. | Freo repeats the R18 clearance/I50 takeover and depleted Sydney cannot arrest late separation. |

#### Supplied slate ordering

| Supplied contract | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Interpretation |
|---|---:|---|---|
| **Sydney +11.5** | **0.62** | LEAN; AFL cushion band not derived | Preferred handicap side |
| **Under 189.5** | **0.57** | LEAN; AF-P4 partial | Preferred total side |
| **Over 189.5** | **0.43** | LEAN; AF-P4 partial | High-shot/high-conversion branch remains live |
| **Fremantle -11.5** | **0.38** | LEAN; AFL cushion band not derived | Requires Freo winner + 12-point separation |

- The supplied spread and total are **two forced-pair decisions**, not four independent trials.
- `P(Sydney +11.5 AND Under 189.5)` ≈ **0.37**.
- Main both-fail supplied state ≈ **0.18**: Fremantle wins by 12+ in a high-scoring game through sustained midfield/inside-50 advantage plus efficient conversion.

#### Potential game winner

- **Projected eventual winner: Fremantle Dockers — 0.52 `UNVALIDATED_SUBJECTIVE`**
- **Sydney Swans — 0.48**
- Endpoint includes finals extra time if tied after the fourth quarter.
- Freo's edge is intentionally small: minor-premier season, league-best defence, more midfield continuity and R18 separation mechanism versus Sydney's SCG/home strength, extra rest and stronger current forward mix.
- Winner call is **not** equivalent to Fremantle -11.5.

#### Information not confirmed / integrity flags

- Final official 2026 substitute nomination / separate late-change bulletin was **not recovered** by 19:26:37 AEST; selected teams and known changes were otherwise verified.
- Exact operator line/total treatment if extra time occurs not supplied (`UNKNOWN_DEFINITION`).
- `AFL_11.5_BAND_NOT_DERIVED` — handicap cannot be overall Rank #1.
- `AF-P4_PARTIAL` — dry/light-wind evening well supported, exact ground-level vector by scoring end not fully verified; total/handicap capped at LEAN.
- Player 1+ goal rows are `MODEL_PROPOSED`; sportsbook availability/prices not supplied; **NO VALUE DETERMINABLE**.
- Current team-stat rates from structured secondaries are descriptive, not field-owner numerical model inputs.
- No post-bounce performance information used.
- No retrospective performed.
- **Current settlement status:** `UNSETTLED — PREGAME AT ISSUE`.

#### Settlement routes pre-registered

- Final score / fourth-quarter state / eventual winner: **AFL official match centre**.
- Selected players / late changes / substitute if exposed: AFL official final-team or match-centre record.
- Player 1+ goal milestones: official AFL final player/stat line.
- Handicap / total: arithmetic from official fourth-quarter score for research-grade grading; operator-action grading follows actual sportsbook extra-time terms if later supplied.

#### Sources

| Source | Link / record | Contribution | Quality / limitation |
|---|---|---|---|
| AFL prelim fixture | https://www.afl.com.au/news/1609182/prelim-finals-fixture-venues-times-ticket-details-confirmed | Exact event, SCG, 19:40 AEST | Primary |
| AFL preliminary-final teams | https://www.afl.com.au/news/1613143/preliminary-finals-teams-sydney-swans-veteran-out-brisbane-lions-defender-to-miss-fremantle-dockers-play-it-safe | Sydney changes; Freo unchanged; Brennan Cox not selected | Primary |
| Sydney Finals Hub | https://www.sydneyswans.com.au/matchday/finals | Ball-up / matchday state | Primary club |
| AFL Sydney forward-selection report | https://www.afl.com.au/news/1613196/sydney-swans-explain-joel-amarteys-omission-veteran-harry-cunningham-in-doubt-after-training-mishap | Forward setup retained / Amartey context | Primary league reporting |
| AFL Sydney suspension reporting | AFL.com.au current 2026 reports | Heeney, Warner, Blakey, Bice, Jordon unavailable | Primary league reporting |
| AFL Sydney v Brisbane QF | https://www.afl.com.au/afl/matches/9029 | 141-88; forward goals; Mills injury | Primary |
| AFL Fremantle v Hawthorn QF report | https://www.afl.com.au/news/1600660/ | 40-72 suppression branch | Primary |
| Fremantle v Geelong semi report | https://www.fremantlefc.com.au/news/2126694/ | 120-106; attack/ruck/clearance recovery | Primary club |
| AFL R18 Freo v Sydney | https://www.afl.com.au/afl/matches/8189 | 111-73 and second-half mechanism | Primary |
| Footy Scores Live season review | https://footyscores.live/articles/afl-season-review-2026/ | H&A record, home/away, points-for/against | Structured secondary |
| Zero Hanger current matchup stats | https://www.zerohanger.com/sydney-fremantle-round-preliminary-finals-2026-mc169126-182588/ | Current clearances/I50/MI50/contested stats | Structured secondary |
| AFL Logan McDonald feature | https://www.afl.com.au/news/1613071/ | 15 straight 1+ goal, 12 multiples | Primary league reporting |
| Footyinfo / Footystatr Charlie Curnow | Current 2026 pages | 74 goals/23, 3.2 goals, shot volume | Secondary statistical |
| ThePropTool / Legz Jye Amiss | Current 2026 pages | 61 goals/24; 21/24 1+ goals | Secondary statistical |
| BOM Moore Park + current SCG-area forecast | 18 Sep game window | Dry; evening wind easing/light | Government / structured weather |
| Drive `RULES_AFL.md` | Sports Research Drive | SFA-AFL, AF-P1–P4, high-total, conversion, wind, finals endpoint | Governing |
| Drive `BASE_RATES_REGISTER.md` | Sports Research Drive | AFL handicap band not yet derived | Governing quantitative register |
| Drive `METHOD.md`, `RULES_GENERAL.md`, `CONTROLS.md`, `SOURCES.md`, `LEARNING_REGISTER.md` | Sports Research Drive | Cross-sport gates/ranking/source discipline | Governing |
| User-supplied slate | Current query | Exact ±11.5 and O/U 189.5 contracts | Contract source only |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| AFL 11.5 cushion band absent | `BASE_RATES_REGISTER.md` | DATA GAP — derive prospectively; no guessed identity |
| Exact SCG near-bounce wind vector not fully mapped | `DATA_SOURCE_REGISTER.md` / `SOURCES.md` | Source-coverage observation; existing AF-P4 cap applied |
| Sydney forward ceiling remains high despite major midfield/defensive absences | `RULES_AFL.md` availability-to-conversion controls | Existing role-chain control applied; NO NEW RULE |
| R18 Freo separation arrived through second-half clearance/I50 takeover | `RULES_AFL.md` separation / Q4 durability | Existing process branch applied; NO NEW RULE |
| 1+ goal milestones can outrank supplied side/total when exposure is more robust, while market availability remains explicit | `RULES_AFL.md` player exposure / `SOURCES.md` | Process observation only; no new weight/source promotion |

---

#### Settlement and retrospective — 19 Sep 2026

- **Final status:** `SETTLED — FINAL`.
- **Official final:** Fremantle **12.11 (83)** defeated Sydney **10.11 (71)** by **12 points** at the SCG. Sydney led by 21 at three-quarter time; Fremantle won the last quarter 5.4 to 0.1.
- **Canonical-ID audit:** no P-459 collision in the fresh combined-log check.

##### A. Prediction outcome

| Rank | Frozen selection | Final evidence | Result |
|---:|---|---|---|
| 1 | Charlie Curnow 1+ goal | Curnow 1 goal | **WIN** |
| 2 | Jye Amiss 1+ goal | Amiss 1 goal | **WIN** |
| 3 | Logan McDonald 1+ goal | McDonald 3 goals | **WIN** |
| 4 | Sydney +11.5 | Fremantle by 12 | **LOSS** — missed by **0.5 points** |
| — | Under 189.5 | 154 total points | **WIN** |
| — | Over 189.5 | 154 total points | **LOSS** |
| — | Fremantle -11.5 | Fremantle by 12 | **WIN** |
| — | Projected winner: Fremantle | Fremantle won | **WIN** |

**Diagnostics:** Rank-1 = **WIN**; Hit@2 = **1**; Wins@2 = **2/2**; binary NDCG@2 = **1.000**.

##### B. Why each pick won or lost

**R1 Curnow 1+ — WIN.** Sydney's forward role remained stable despite team absences. Curnow only needed one conversion and got it in the third term. The row succeeded on role/exposure rather than a requirement for Sydney to win or post a large total.

**R2 Amiss 1+ — WIN.** Amiss also converted once, with his third-quarter goal helping Fremantle start the comeback. The pre-game role-based goal exposure survived a game in which Fremantle were inefficient for long stretches.

**R3 McDonald 1+ — WIN.** McDonald was the strongest realised player-goal result, kicking three. The role/minutes thesis was robust even though Sydney ultimately lost.

**R4 Sydney +11.5 — LOSS.** This was a boundary failure: Fremantle won by 12, so the row missed by 0.5. But the causal failure was not random rounding. The pre-game card explicitly named a late-Fremantle separation path. That branch materialised with extraordinary force: the Dockers dominated the final term, with the official/club reporting showing a 5.4-to-0.1 scoring quarter and a major inside-50/clearance swing. A known kill path was present but underweighted.

##### C. Rank-1 review

Rank #1 won, so no failure escalation is required. The player-event ranking was justified by stable forward roles and modest 1+ thresholds. The result supports the **process** of prioritising low-threshold player exposure over a more fragile margin line; it does not validate the exact 0.84 probability as calibrated.

##### D. Top-two review

Both top-two rows won. They were related through a generally functional forward environment but not duplicates: one was Sydney forward exposure, the other Fremantle forward exposure. The ordering was defensible and materially safer than placing the Sydney cushion above them.

##### E. Over/Under review

The Under 189.5 won comfortably at 154. The realised total was suppressed by Sydney scoring only one behind in Q4 despite Fremantle's huge territorial dominance. The pre-game central total around the mid-180s was too high for the realised defensive/finishing state, but the preferred Under direction was correct. No global finals-Under rule follows.

##### F. What went right

- All three ranked player-goal selections won.
- Fremantle was correctly projected as the potential winner despite Sydney's home advantage.
- The supplied Under and Fremantle -11.5 both won.
- The card had already identified late Fremantle separation as a live kill path.

##### G. Blind spots and future handling

- **Q4 durability/separation mass:** Fremantle's final-quarter midfield/territory ceiling deserved more mass relative to Sydney +11.5. This is a candidate strengthening of an existing AFL phase branch, not a new rule from one result.
- **Boundary sensitivity:** +11.5 lost by 0.5, so retrospective conclusions must be about the distribution branch, not “the handicap was wildly wrong.”
- **Final interchange/sub bulletin:** not fully recovered at issue; however post-match evidence did not reveal a late participant change that explains the miss.

##### H. Mandatory validation questions

| Question | Retrospective answer |
|---|---|
| Confirmed teams/starters obtained? | **Yes, selected teams were materially verified.** |
| Bench/sub/rotation obtained? | Main team/interchange context yes; final substitute bulletin was not complete to ideal standard. |
| Coaching information obtained/material? | Yes; tactical/phase context was considered. |
| Injuries/suspensions/rest adequately checked? | **Yes**, including Sydney's major absences; no late surprise explains settlement. |
| Sources accurate/current? | Yes; AFL/club final sources confirm score and goalkickers. |
| Better sources available? | Official AFL match centre remains first choice for final stats and player events. |
| Blind spots? | Insufficient mass on Fremantle's late clearance/I50 takeover branch. |
| Future accounting? | Weight current-regime Q4 durability/clearance/territory branches explicitly when a margin line sits close to that tail. |

##### I. Source audit

- AFL official match report: https://www.afl.com.au/news/1613373/dockers-storm-home-to-seal-gf-berth-in-epic-finish-over-swans — final 83-71, quarter scores and goalkickers. **Primary.**
- Fremantle official report: https://www.fremantlefc.com.au/news/2132870/freo-storm-home-to-seal-grand-final-berth-in-epic-finish-over-swans — match flow and Amiss/Curnow/McDonald goal context. **Primary club corroboration.**
- AFL post-match analysis: https://www.afl.com.au/news/1613378/the-fairytale-finish-never-came-but-the-cinderella-sydney-swans-won-back-a-city-against-the-fremantle-dockers — fourth-quarter inside-50 collapse context.

**Learning disposition:** existing weighted-kill-path and AFL phase controls should have carried more mass. Track recurrence before formal promotion.

---

### P-460 — Baseball / Taiwan CPBL — Rakuten Monkeys @ Fubon Guardians

- **Canonical ID:** P-460 (fresh pre-issue reconciliation against `PREDICTION_LOG_COMBINED_4.md` found no P-460 collision)
- **Sport / competition:** Baseball — Chinese Professional Baseball League (CPBL), Taiwan, 2026 first-team regular season
- **Event:** Rakuten Monkeys @ Fubon Guardians
- **Official event identity:** CPBL 2026 Game 338 (`2026-A-338`)
- **Venue:** Xinzhuang Baseball Stadium, New Taipei City, Taiwan
- **Scheduled start:** **18 Sep 2026, 18:35 Taiwan time (UTC+8) = 18 Sep 2026, 20:35 AEST (Australia/Melbourne)**
- **Game state at latest research refresh:** **PREGAME / NOT STARTED.** CPBL's exact advanced-stat event page and official box-score shell still showed the game as not started; no in-game information is used.
- **Latest pre-first-pitch volatile refresh:** **18 Sep 2026, approximately 18:19 Taiwan / 20:19 AEST**, with exact-event and lineup-release routes rechecked again immediately before issue. The user explicitly requested late-news monitoring rather than an early freeze.
- **Method version:** **MDS-2026.09.06-v4.0 / SFA-BASEBALL**
- **Population status:** **EXPLORATORY — NOT SCORED / LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. CPBL-specific margin and exact venue-total base rates required for stronger quantitative identity treatment are not present in the active register.
- **Operating mode:** **SPORTS_ONLY / MARKET_BLIND**. User-supplied thresholds define the contracts only; no odds, implied probabilities, market movement, bookmaker previews or tipster opinions enter the forecast.
- **Supplied contracts:** **Rakuten Monkeys ML**; **Fubon Guardians -1.5**; **Combined Total Over 6.5**; **Combined Total Under 6.5**.

#### Identity / rules / endpoint validation

- CPBL field-owner pages verify Rakuten as the **visiting** side, Fubon as the **home** side, Game 338 at Xinzhuang on 18 Sep 2026.
- CPBL regular-season games can finish tied after the extra-inning cap. A 13 Jun 2026 official CPBL record shows Rakuten and CTBC ending **9-9 after 12 innings**, confirming the tie branch is active in the current rules era.
- **Moneyline operator terms were not supplied.** Therefore the model prints the official CPBL result family (**Rakuten win / Fubon win / tie**) and separately notes that sportsbook treatment of a 12-inning tie is `UNKNOWN_DEFINITION`. No tie is silently counted as a Rakuten loss or win for operator-action grading.
- Fubon's supplied **-1.5** contract requires a Fubon win by **2+ runs**. It is not the complement of Rakuten ML.
- The active `BASE_RATES_REGISTER.md` has **no field-owner-derived CPBL 1.5-run cushion band** and no exact 2026 Xinzhuang distribution at 6.5. Flags: `CPBL_1.5_BAND_NOT_FIELD_OWNER_DERIVED` and `XINZHUANG_6.5_BASE_RATE_NOT_DERIVED`. MLB identities are **not transferred** into CPBL.

#### Participant handshake / latest lineups / availability

**Starting pitchers**

- **Rakuten — Tyler Eppler / 艾菩樂, RHP:** official CPBL season record **4-8, 3.12 ERA, 20 starts, 127.0 IP, 128 H, 44 ER, 24 BB, 93 K, 1.20 WHIP**. Same-day starter information lists **1-1, 2.52 ERA vs Fubon** in 2026.
- **Fubon — A.J. Candelario / 悍里歐, RHP:** same-day starter record **1-2, 4.95 ERA**; **0-1, 6.00 ERA vs Rakuten**.
- Starter identities are treated as current/probable for the exact event. The CPBL exact event/box pages had not populated the full game-day batting orders in the retrievable record at the latest refresh.

**Starting batting orders**

- `STARTING_LINEUPS_NOT_RETRIEVED_AT_FINAL_REFRESH` for **both teams**. CPBL's official lineup-history pages still stopped at **17 Sep**.
- Latest official Rakuten order (17 Sep, contextual only): **Lin Cheng-hua, Adam Walker, Lin Hung-yu, Lin Chih-ping, Liang Chia-jung, Ma Chieh-sen, Lin Cheng-fei, Sung Chia-hsiang, Cheng Chin**.
- Latest official Fubon order (17 Sep, contextual only): **Chang Yu-cheng, Lin Tse-pin, Shen Hao-wei, Fan Kuo-chen, Tung Tzu-en, Lin Shu-yi, Wang Nien-hao, Lin Tai-an, Yeh Tzu-ting**.
- Those 17-Sep orders are **not backfilled as 18-Sep confirmed lineups**. No player prop is introduced because the current nine-man orders and exact exposure are not confirmed.

**Rakuten material absences / doubts**

- **Chen Chen-wei / 陳晨威:** away with Taiwan's Asian Games squad. He is a meaningful lost offensive/defensive exposure; reporting before departure described him as one of Rakuten's most important hitters and baserunners.
- **Lin Tzu-wei / 林子偉:** **out**. Same-day reporting says his planned 19-Sep return was cancelled after continued right-side/oblique discomfort in a 17-Sep farm appearance; reassessment is pushed into next week.
- **Lin Li / 林立:** **day-to-day / unresolved for tonight**. Same-day reporting says he has side inflammation/tightness, resumed batting on 17 Sep and was to test outdoor batting on 18 Sep. No official 18-Sep lineup was retrieved to prove activation.
- **Chuang Hsin-yen / 莊昕諺 (reliever): unavailable.** Rakuten and CNA reported facial fracture, laceration and broken teeth after a 14-Sep line drive; surgery was arranged 15 Sep. This removes an important bullpen option.
- Manager: **Tseng Hao-chu / 曾豪駒**.

**Fubon availability state**

- No comparably material same-day Fubon absence was independently identified in the final search, but **the exact 18-Sep starting nine and full bench were not retrieved**, so this is not equivalent to declaring Fubon fully healthy.
- The 17-Sep order contains the central active bats **Chang Yu-cheng** and **Fan Kuo-chen**. Current team records also preserve closer **Tseng Chun-yue / 曾峻岳** as a major late-inning resource.
- Manager: **Mitsunori Gotoh / 後藤光尊**.

**Gate consequence:** `BENCH_NOT_RETRIEVED_TO_GATE_STANDARD`. Under `G14.2`, a full-game total or margin row cannot be an uncapped overall Rank #1. The moneyline may occupy Rank #1, while the total and -1.5 rows remain evidence-capped.

#### Starter current-regime audit

**Tyler Eppler — Rakuten**

- Official season line: **3.12 ERA / 1.20 WHIP across 127.0 IP**, with substantially more strikeouts (93) than walks (24).
- On **25 Aug**, CNA documented **7 IP, 3 H, 1 ER, 6 K, 2 BB, 93 pitches** and noted it was his **fourth consecutive quality start**.
- On **14 Aug**, CNA documented **7 scoreless innings with 9 strikeouts** against Wei Chuan before Rakuten's bullpen lost the game 2-1. This is useful separation between starter quality and bullpen/result noise.
- Direct same-venue comparator, **5 Apr at Xinzhuang vs Fubon:** Eppler threw **6.0 IP, 5 H, 0 ER, 7 K on 95 pitches** in a 5-1 Rakuten win.
- Same-day starter information gives Eppler **2.52 ERA vs Fubon** in 2026.
- **Counter-path:** Fubon is not powerless against him. Chang Yu-cheng has produced direct power damage against Eppler in the season series, and Rakuten's weakened relief chain means an Eppler lead is not treated as a nine-inning guarantee.

**A.J. Candelario — Fubon**

- Current season headline: **1-2, 4.95 ERA**.
- **29 Aug:** CNA documented a strong **6 IP, 7 H, 2 ER, 5 K, 2 BB, 110 pitches** win over CTBC.
- **5 Sep vs Rakuten:** official CPBL record shows **6 IP, 7 H, 4 ER, 4 K, 1 BB, 99 pitches** in a **4-0 Rakuten win**.
- **12 Sep vs TSG:** official CPBL record shows only **2 IP, 4 H, 4 ER, 68 pitches** in an **8-3 Fubon loss**.
- Therefore the last two starts total only **8 IP and 8 ER**. The deterioration is back-loaded enough to matter, but the 29-Aug quality start prevents treating 4.95/6.00 ERA as deterministic.

**Starter edge:** **Rakuten materially ahead**, but not by enough to ignore its depleted offense and missing bullpen arm.

#### Team-state / current-regime context

- Current CPBL homepage after 17 Sep: **Rakuten 25-20 (.556), 2nd in the second half**; **Fubon 20-26 (.435), tied 5th**. The broader second-half form baseline therefore favours Rakuten, while Fubon's recent wins keep the home upset branch alive.
- Rakuten's current offensive state is weaker than its season-average roster because **Chen Chen-wei is away, Lin Tzu-wei is out, and Lin Li is unresolved**.
- Fubon has the home last-bat advantage and retains middle-order power through players such as Chang Yu-cheng and Fan Kuo-chen.

#### Same-matchup / Xinzhuang scoring context

Descriptive 2026 Rakuten–Fubon games at **Xinzhuang** recovered from CPBL records before this fixture include combined totals of approximately:

- **5 Apr:** Rakuten 5-1 Fubon — **6 runs**
- **6 May:** Rakuten 1-7 Fubon — **8**
- **26 Jun:** Rakuten 3-1 Fubon — **4**
- **27 Jun:** Rakuten 2-9 Fubon — **11**
- **7 Jul:** Rakuten 5-3 Fubon — **8**
- **8 Jul:** Rakuten 1-0 Fubon — **1**
- **17 Sep:** Fubon 1-0 Rakuten — **1**

That seven-game descriptive set has mean about **5.6** and median **6**, with **4/7 below 6.5**. It is **not** promoted to an official venue base rate: it is a same-team matchup subset with schedule/participant dependence and cannot substitute for the missing field-owner Xinzhuang 6.5 distribution.

Recent matchup width is large: Fubon also beat Rakuten **13-0 on 4 Sep**, while Rakuten answered **4-0 on 5 Sep**. The correct use is therefore **distribution width**, not a simplistic H2H Over/Under streak.

#### Environment / weather

- Xinzhuang is an outdoor venue.
- Current structured conditions in Xinzhuang were around **27°C and cloudy** in the pregame window; same-day starter-weather reporting carried a low rain signal (~10%). No clear postponement/interruption mechanism was identified.
- Exact field-level wind vector was not independently retrieved. `WEATHER_BASIC_VERIFIED / WIND_VECTOR_NOT_RETRIEVED`.
- Weather therefore contributes little signed adjustment; it is not used as an automatic Over/Under input.

#### Joint run / winner / separation object

**Central nine-inning-equivalent run budget (`UNVALIDATED_SUBJECTIVE`):**

- **Rakuten centre:** ~**3.2 runs**
- **Fubon centre:** ~**2.8 runs**
- **Combined centre:** ~**6.0 runs**
- **Width:** roughly **3.3–3.5 runs**, widened for Candelario's recent instability, Rakuten bullpen depletion, lineup uncertainty and possible extra innings.

**Signed component audit**

Rakuten scoring **up:** Candelario's 8 ER in 8 IP over the last two starts; 4 ER allowed to Rakuten on 5 Sep; stronger second-half team baseline.  
Rakuten scoring **down:** Chen Chen-wei absent; Lin Tzu-wei out; Lin Li unresolved; Rakuten was shut out 17 Sep; full 18-Sep order unknown.  
Fubon scoring **down:** Eppler's 3.12 season ERA/1.20 WHIP, four-quality-start run in August, 2.52 season ERA vs Fubon, and direct 6-scoreless-inning Xinzhuang comparator.  
Fubon scoring **up:** Chang Yu-cheng/Fubon power ceiling, home last bat, Rakuten's missing late-inning reliever, and bullpen-transition variance after Eppler exits.

**Official CPBL result family (`UNVALIDATED_SUBJECTIVE`):**

- **Rakuten win: 0.57**
- **Fubon win: 0.41**
- **Tie after CPBL endpoint: 0.02**

If a two-way sportsbook moneyline **voids ties**, Rakuten's conditional win probability among decisive results would be approximately **0.57 / 0.98 = 0.582**. That is an interpretation aid only; operator terms were not supplied.

**Total family:**

- **Under 6.5: 0.56**
- **Over 6.5: 0.44**
- No push is possible at a half-run line.

**Fubon -1.5 separation budget:**

- Fubon official win: ~**0.41**
- Fubon win by exactly 1: ~**0.15**
- Fubon win by **2+**: ~**0.26** → supplied **Fubon -1.5**
- Rakuten win or official tie: ~**0.59**

This separation split is `UNVALIDATED_SUBJECTIVE` and evidence-capped because **no CPBL 1.5-run cushion identity has been derived**. It is not an imported MLB one-run rate.

**Coherent winner × total family:**

| State | Mass |
|---|---:|
| Rakuten win + Under 6.5 | 0.34 |
| Rakuten win + Over 6.5 | 0.23 |
| Fubon win + Under 6.5 | 0.21 |
| Fubon win + Over 6.5 | 0.20 |
| Official tie + Under 6.5 | 0.01 |
| Official tie + Over 6.5 | 0.01 |
| **Total** | **1.00** |

This reproduces Rakuten 0.57 / Fubon 0.41 / tie 0.02 and Under 0.56 / Over 0.44 without contradictory independent classifiers.

- `P(Rank #1 AND Rank #2)` = **0.34** for **Rakuten ML + Under 6.5**.
- `P(neither preferred selection wins)` ≈ **0.21** on the official-result representation: Fubon/tie with Over 6.5. Operator treatment of a tie could change the moneyline settlement label, not the baseball state.
- Representative central state: **Rakuten 3-2 Fubon** — Rakuten wins and Under 6.5 wins.

#### Ranked picks — most likely to least likely

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Geometry | Why this rank | Primary failure path |
|---:|---|---:|---|---|---|---|
| **1** | **Rakuten Monkeys ML** | **0.57 official-win probability**; ~**0.582 conditional on decisive result if ties void** | **MEDIUM**; operator tie treatment unknown | FREE supplied contract | Clear starter edge through Eppler, stronger second-half record, Candelario's recent 8 ER/8 IP and direct 4-ER loss vs Rakuten. Ranked only modestly above 50% because Rakuten's batting/relief availability is materially weakened. | Candelario rebounds toward his 29-Aug quality start, Eppler allows Fubon power damage, and Rakuten's depleted batting order cannot create separation; home last-bat/bullpen converts a Fubon win. |
| **2** | **Combined Total UNDER 6.5 runs** | **0.56** | **LEAN / MEDIUM-LOW**; `G14.2` cap + `XINZHUANG_6.5_BASE_RATE_NOT_DERIVED` | FORCED_PAIR preferred side | Eppler is the best run-prevention mechanism on the field; Rakuten is missing/doubting major bats; the retrieved Xinzhuang matchup subset centres below the line. Full-game total is kept below Rank #1 because exact lineups/bench and official venue distribution are incomplete. | Candelario exits early again and/or Rakuten's depleted bullpen leaks late runs; one crooked inning plus extra-inning/late-game scoring pushes the game to 7+. |
| **3** | **Combined Total OVER 6.5 runs** | **0.44** | **LEAN / MEDIUM-LOW**; same caps | FORCED_PAIR non-preferred side | Candelario's recent failure, Rakuten relief injury, Fubon's power ceiling and the 8/11/13-run matchup tails keep 7+ very live. | Eppler controls Fubon for 6–7 innings while Rakuten's reduced lineup scores only 2–4, creating a 3-1 / 3-2 / 4-1 type game. |
| **4** | **Fubon Guardians -1.5** | **0.26** | **LOW-MEDIUM / FORCED supplied contract**; `CPBL_1.5_BAND_NOT_FIELD_OWNER_DERIVED` | FREE supplied handicap, not complementary to Rakuten ML | Fubon can win through home last bat and Rakuten's current offensive/relief absences, but this contract additionally requires **2+ run separation** against the stronger starting pitcher. | Eppler wins the starter matchup, or Fubon wins only by one; either state defeats -1.5. |

**Ranking interpretation:** Rank #1 and Rank #2 are close. Rakuten ML earns the top spot because its exact winning region is supported by the largest event-specific mismatch (starting pitcher) and is not blocked by the `G14.2` full-game margin/total Rank-1 cap. Under 6.5 is the preferred total but remains a **lean**, not a high-confidence call.

#### Potential game winner

- **Projected official CPBL winner: Rakuten Monkeys — 0.57 `UNVALIDATED_SUBJECTIVE`**
- **Fubon Guardians — 0.41**
- **Official tie — 0.02**
- This is a **modest**, not dominant, Rakuten edge. Eppler is the primary reason; Rakuten's missing/doubtful hitters and unavailable reliever are the primary reasons the projection is not stronger.

#### Information not confirmed / integrity flags

- **18-Sep starting batting orders not retrieved** from the field owner at latest refresh. Yesterday's lineups are context only.
- **Full game-day benches/reserves not retrieved**; `BENCH_NOT_RETRIEVED_TO_GATE_STANDARD` applies.
- **Lin Li final active/starting status unresolved** at issue; same-day reporting only establishes day-to-day evaluation.
- **Exact operator moneyline treatment of a 12-inning CPBL tie not supplied** (`UNKNOWN_DEFINITION`).
- **No CPBL-specific +1.5 cushion band** in the active base-rate register; no MLB transfer.
- **No exact Xinzhuang 2026 O/U 6.5 field-owner distribution** in the active base-rate register.
- **Exact field-level wind vector not retrieved**; basic weather state only.
- No bookmaker odds/prices/market movement used.
- No retrospective performed.
- **Current settlement status:** `UNSETTLED — PREGAME AT ISSUE`.

#### Settlement routes pre-registered

- Official result, inning line, starters, final batting orders and pitching use: **CPBL official box score / CPBL advanced exact Game 338 page**.
- Moneyline research-grade grading: official CPBL endpoint (**Rakuten win / Fubon win / tie**). Operator-action grading requires the user's sportsbook tie/void rule if a tie occurs.
- Fubon -1.5: arithmetic from official final score; requires Fubon margin ≥2.
- O/U 6.5: arithmetic from official final combined score under operator completion/action terms; exact shortening/suspension terms are `UNKNOWN_DEFINITION` unless supplied later.

#### Sources

| Source | Link / record | Contribution | Quality / limitation |
|---|---|---|---|
| CPBL advanced exact event | https://stats.cpbl.com.tw/schedule/2026-A-338 | Game 338 identity, teams, venue, pregame/not-started state | **Primary / field owner** |
| CPBL official box-score shell | https://cpbl.com.tw/box/index?gameSno=338&kindCode=A&year=2026 | Exact 18-Sep event and final settlement route; batting fields not yet populated | **Primary / field owner** |
| CPBL Rakuten lineup history | https://cpbl.com.tw/team/lineuprecord?ClubNo=AJL | Latest official posted order was 17 Sep; proves 18-Sep lineup not retrieved | **Primary**, but not current lineup |
| CPBL Fubon lineup history | https://cpbl.com.tw/team/lineuprecord?ClubNo=AEO | Latest official posted order was 17 Sep | **Primary**, but not current lineup |
| CPBL standings / homepage | https://cpbl.com.tw/standings/season ; https://cpbl.com.tw/ | Current second-half records, standings | **Primary** |
| CPBL pitching records | https://cpbl.com.tw/stats/recordall?kindcode=A&position=02&sortby=01 | Eppler season 3.12 ERA, 127 IP, K/BB/WHIP | **Primary statistical** |
| CPBL 5 Apr exact game | https://stats.cpbl.com.tw/schedule/2026-A-19 | Eppler 6 scoreless at Xinzhuang vs Fubon; 5-1 result | **Primary** direct comparator |
| CPBL 5 Sep exact game | https://stats.cpbl.com.tw/schedule/2026-A-311 | Candelario 6 IP / 4 ER vs Rakuten; Rakuten 4-0 | **Primary** direct comparator |
| CPBL 12 Sep exact game | https://stats.cpbl.com.tw/schedule/2026-A-325 | Candelario 2 IP / 4 ER / 68 pitches vs TSG | **Primary** current-regime start |
| CNA, 25 Aug | https://www.cna.com.tw/news/aspt/202608250364.aspx | Eppler 7 IP/1 ER and fourth straight quality start | High-quality current secondary |
| CNA, 29 Aug | https://www.cna.com.tw/news/aspt/202608290198.aspx | Candelario 6 IP/2 ER quality start; prevents one-direction recency bias | High-quality current secondary |
| UDN, 18 Sep 17:02 | https://udn.com/news/story/7001/9763446 | Lin Tzu-wei return cancelled; Lin Li side inflammation/day-to-day; manager comments | High-quality **same-day** secondary |
| CNA / Asian Games reporting | https://www.cna.com.tw/news/aspt/202609100304.aspx ; https://www.cna.com.tw/news/aspt/202607150261.aspx | Chen Chen-wei national-team absence and stated Rakuten impact | High-quality secondary; national-team context |
| Rakuten official site + CNA, 15 Sep | https://monkeys.rakuten.com.tw/ ; https://www.cna.com.tw/news/aspt/202609150132.aspx | Chuang Hsin-yen facial fracture/surgery; unavailable bullpen arm | Primary club + high-quality secondary |
| CPBL current 12-inning tie example | https://cpbl.com.tw/box/news?gameSno=162&kindCode=A&year=2026 | Confirms current regular-season tie endpoint exists | **Primary / field owner** |
| Current structured Xinzhuang weather | Retrieved 18 Sep 2026 pregame | ~27°C/cloudy; no clear interruption signal | Current structured weather; field-level wind not recovered |
| Drive `METHOD.md` | Sports Research Drive | v4.0 probabilities, rank, market-blind and joint-object discipline | Governing; read-only |
| Drive `RULES_GENERAL.md` / `CONTROLS.md` | Sports Research Drive | G14.2, G15.1, G16, G20/G20.1, source/state gates | Governing; read-only |
| Drive `RULES_BASEBALL.md` | Sports Research Drive | CPBL as distinct baseball population; starter/lineup/bullpen/run-distribution procedure | Governing; read-only |
| Drive `BASE_RATES_REGISTER.md` | Sports Research Drive | Confirms no transferable CPBL margin/venue identity may be guessed | Governing quantitative register; read-only |
| Drive `SOURCES.md` / `DATA_SOURCE_REGISTER.md` | Sports Research Drive | CPBL official/advanced pages as competition source lane | Governing source register; read-only |
| User-supplied slate | Current query | Exact ML, Fubon -1.5 and O/U 6.5 contracts | Contract source only; operator terms not supplied |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| CPBL +1.5/one-run cushion identity absent | `BASE_RATES_REGISTER.md` | **DATA GAP** — prospectively derive from CPBL field-owner finals; no MLB transfer |
| Xinzhuang exact 6.5 total distribution absent | `BASE_RATES_REGISTER.md` / `DATA_SOURCE_REGISTER.md` | **DATA GAP** — do not promote seven same-team games into venue base rate |
| CPBL lineup-history page lagged current 18-Sep order inside pregame window | `DATA_SOURCE_REGISTER.md` / `SOURCES.md` | Source-release latency observation; keep participant missingness explicit |
| Rakuten starter advantage conflicts with offensive/relief absences | `RULES_BASEBALL.md` participant/exposure-chain controls | Existing phase/exposure decomposition correctly applied — **NO NEW RULE** |
| Current CPBL tie endpoint materially affects ML definition | `RULES_BASEBALL.md` endpoint/contract identity | Existing competition-endpoint control applied — **NO NEW RULE** |

---


---

#### Settlement and retrospective — 19 Sep 2026

- **Final status:** `SETTLED — FINAL`.
- **Final:** Fubon Guardians **2-1** Rakuten Monkeys, walk-off in the bottom of the ninth.
- **Canonical-ID audit:** no P-460 collision in the fresh combined-log check.

##### A. Prediction outcome

| Rank | Frozen selection | Final | Result |
|---:|---|---:|---|
| 1 | Rakuten Monkeys ML | Fubon 2-1 | **LOSS** |
| 2 | Under 6.5 | 3 total runs | **WIN** |
| 3 | Over 6.5 | 3 total runs | **LOSS** |
| 4 | Fubon -1.5 | Fubon by 1 | **LOSS** |
| — | Projected winner: Rakuten | Fubon won | **LOSS** |

**Diagnostics:** Rank-1 = **LOSS**; Hit@2 = **1**; Wins@2 = **1/2**; binary NDCG@2 ≈ **0.631**.

##### B. Why each pick won or lost

**R1 Rakuten ML — LOSS.** The starter-quality premise was strongly supported in the actual game: Tyler Eppler retired the first 18 Fubon hitters and carried a perfect game through six innings. The forecast failed because it converted that starter edge too directly into full-game win probability. Rakuten scored only once, Fubon tied it in the seventh on Fan Kuo-chen's RBI double, and Fan delivered the walk-off single in the ninth. Low run support plus the home last-bat branch overwhelmed the starter edge.

**R2 Under 6.5 — WIN.** This was the most accurate game-shape read. A.J. Candelario allowed one run in six innings, Eppler allowed only two over 8.2, and the game finished with three total runs. The card was right to treat both starters as meaningful suppression mechanisms.

**R3 Over 6.5 — LOSS.** The necessary tail — early Candelario failure, Rakuten offensive breakout, or bullpen collapse — never developed.

**R4 Fubon -1.5 — LOSS.** Fubon won, but by exactly one. This is precisely why the card had ranked the -1.5 branch low and flagged the missing CPBL cushion band.

##### C. Rank-1 failure review

Rakuten ML was ranked first because Eppler's current form and direct Fubon matchup were substantially stronger than Candelario's recent line. That information was correct. The ranking error was in **team-level translation**: Rakuten's known offensive absences/uncertainty (Chen Chen-wei, Lin Tzu-wei, Lin Li context) were not given enough weight, and the joint object did not reserve enough mass for “Eppler dominates but Rakuten score 0-1 and Fubon wins late.”

The smallest fix is not to discount elite starting pitching. It is to separate starter-run suppression from **win conversion**, explicitly including run-support and home-last-bat/leverage branches. The fact that Eppler stayed in into the ninth also shows the post-starter chain can be “starter continuation” rather than an assumed bullpen handoff.

##### D. Top-two review

At least one of the top two won; the Under at #2 was the robust piece. The relative ordering should be questioned: the Under thesis depended directly on both starters, while the ML thesis required starter edge **plus** Rakuten run support and successful late-game conversion. In hindsight and process terms, the Under had fewer extra conditions and could reasonably have ranked above the ML.

##### E. Total review

Under 6.5 won 3-0 in distance terms. The central scoring budget around six runs correctly leaned Under, but the realised state was even more suppressed. This result supports the event-specific strong-starter mechanism; it does not validate a generic CPBL Under rule.

##### F. What went right

- Eppler evaluation was highly accurate: six perfect innings and only three hits allowed over 8.2.
- Under 6.5 won clearly.
- Fubon -1.5 was correctly kept low because a narrow Fubon win was a live branch.
- Missing CPBL +1.5/one-run base-rate and lineup/bench limitations were disclosed rather than fabricated.

##### G. Blind spots and future handling

- **Starter edge ≠ match winner:** require run-support and late-game conversion branches.
- **Starter continuation:** model the possibility an effective starter remains in deep enough to become the ninth-inning leverage arm.
- **Rakuten offensive absences:** these were known but underweighted in winner conversion.
- **Lineup/bench retrieval:** exact match-day starting nine/full bench were not available to gate standard at freeze, so winner confidence should remain capped.

##### H. Mandatory validation questions

| Question | Retrospective answer |
|---|---|
| Confirmed starters/lineups obtained? | Starters **yes**; exact full 18-Sep batting orders were **not retrieved** at freeze. |
| Bench/reserve context obtained? | **No, not to gate standard.** |
| Coaching information obtained/material? | Managers were identified; no coaching surprise is needed to explain the result. |
| Injuries/rest/availability checked? | **Yes**, with Rakuten absences materially documented; Lin Li remained unresolved. |
| Sources accurate/current? | Starter/injury reporting was useful; final narrative from CNA was timely and specific. |
| Better sources available? | CPBL exact advanced/box pages remain the settlement owner when fully hydrated; crawl latency is a known access issue. |
| Blind spots? | Run-support conversion, home last bat, starter continuation. |
| Future accounting? | Separate starter RA distribution from team-win branch; explicit home-ninth leverage state. |

##### I. Source audit

- CPBL exact box shell: https://cpbl.com.tw/box/index?gameSno=338&kindCode=A&year=2026 — official event identity; crawl hydration can lag.
- CPBL advanced exact event: https://stats.cpbl.com.tw/schedule/2026-A-338 — official event route; also showed access latency.
- CNA exact-match report: https://www.cna.com.tw/news/aspt/202609180299.aspx — 2-1 final, Eppler perfect through six, Candelario six innings/one run, Fan Kuo-chen tying double and walk-off single. **High-quality causal source.**

**Learning disposition:** existing exposure-chain logic is adequate if starter dominance, offence and home-last-bat states are separated. CPBL margin-band derivation remains a data task, not a guessed rule.

---

### P-461 — Tennis / WTA 125 Valencia — Clara Burel vs Guiomar Maristany Zuleta De Reales, Quarterfinal

- **Canonical ID:** P-461 (fresh pre-issue reconciliation against `PREDICTION_LOG_COMBINED_4.md` found no P-461 collision)
- **Sport / competition:** Tennis — WTA 125, BBVA Open Internacional de Valencia 2026, women's singles
- **Event:** Clara Burel vs Guiomar Maristany Zuleta De Reales
- **Round:** Quarterfinal
- **Venue:** Sporting Club de Tenis de València, Av. de les Balears 29, València, Spain
- **Court / surface:** Center Court; outdoor clay
- **Scheduled start:** **18 Sep 2026, 11:00 UTC = 13:00 CEST = 18 Sep 2026, 21:00 AEST (Australia/Melbourne)**
- **Game state at issue:** **PREGAME / SCHEDULED**. Latest exact-match schedule sources still showed the quarterfinal as scheduled; no live point information used.
- **Research cutoff / final volatile refresh:** **18 Sep 2026, 20:42:31 AEST / 12:42:31 CEST**
- **Method version:** MDS-2026.09.06-v4.0 / SFA-TENNIS
- **Population status:** EXPLORATORY — tennis has no approved fitted target/source/model card; running log remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.
- **Operating mode:** SPORTS_ONLY / MARKET_BLIND.
- **Supplied contracts:** Maristany +3.5 games; Burel -3.5 games; total games Over 20.5; total games Under 20.5.
- **Operator / retirement terms:** **NOT SUPPLIED / UNKNOWN_DEFINITION**. Forecast probabilities are conditional on an ordinarily completed best-of-three match. Match-winner, game-handicap and total-games operator settlement can differ after a retirement/walkover.

#### Identity / rules / tournament validation

- WTA's official tournament page identifies Valencia as a **WTA 125**, **outdoor clay** event running 14–20 Sep 2026.
- Tournament/local-government pages identify the venue as the **Sporting Club de Tenis de València**.
- Exact schedule sources identify **Burel vs Maristany** as the quarterfinal on **Center Court at 11:00 UTC**.
- Standard WTA singles match structure is best-of-three tiebreak sets. The exact sportsbook's retirement/void rules were not supplied and are not invented.
- `G14.2` team bench/coach gate is **N/A for individual tennis**; the controlling tennis participant questions are player identity, current fitness/completion risk, surface, recent workload and current tournament state.

#### Rankings / current-regime context

**Clara Burel**
- Current WTA singles rank: **301**; career high: **42**.
- WTA 2026 record shown as **17-11**; a secondary surface database records **17-10 on clay** in 2026.
- The current ranking is materially affected by her injury-disrupted 2025 season, when WTA notes she played only one event. Ranking is therefore treated as a prior with a major comeback-context caveat rather than a complete current-strength measure.
- No credible current Burel injury report was recovered for this quarterfinal. Her round-of-16 advancement was a **walkover because Martina Trevisan withdrew**, not because of a Burel issue.

**Guiomar Maristany Zuleta De Reales**
- Current WTA singles rank: **178**; current official WTA record **24-18**; secondary surface database records approximately **19-14 on clay** in 2026.
- Current ranking is materially stronger than Burel's, but Burel owns the much higher historical ceiling. The card therefore does not let ranking alone own the winner centre.
- No credible current Maristany injury report was recovered. Her Bassols match was suspended because of **weather/court conditions**, not a medical problem.

#### Direct H2H — highest-value matchup comparator

The players met **seven days ago**, also on clay, in the Montreux WTA 125 quarterfinal. **Maristany won 6-3, 1-6, 6-1** in 2h05m57s.

Official/corroborated match statistics:
- Total points: **Maristany 83 – Burel 76**.
- Service points won: Maristany **46/88 (52.3%)**; Burel **34/71 (47.9%)**.
- Breaks converted: Maristany **6/10**; Burel **5/13**.
- First serve in: Maristany **67.0%**; Burel **66.2%**.
- Burel produced **37 winners** to Maristany's **25**, but also **42 unforced errors** to Maristany's **24**.
- Average rally length was about **6.4 shots** for both sides.

**Mechanism:** Burel showed the greater first-strike/winner ceiling, while Maristany won the consistency/error-control and service-point battle. The 23-game, three-set result is highly relevant to both the +3.5 handicap and 20.5 total, but one H2H is not treated as a fitted coefficient.

#### Valencia current-event evidence

**Burel path**
- R1: beat Aran Teixido Garcia **7-6(3), 6-0** in **1h34m14s**.
- Burel won total points **70-49**, converted **6/9** break points, and won 6 of 9 return games.
- Her first-serve percentage was only **48.4%**, so the scoreline should not be read as a pure serve-dominance result; Teixido also committed eight double faults.
- R16: advanced by **walkover** when Martina Trevisan withdrew. Burel therefore has had no competitive points since Tuesday.

**Maristany path**
- R1: beat Berfu Cengiz **7-5, 7-5**.
- R16: beat No. 4 seed Marina Bassols Ribera **6-3, 3-6, 6-4**.
- Completed-match statistics vs Bassols: **108-99 points**, 0 aces / 5 double faults, **9/14 service games held (64%)**, **6/14 return games won (43%)**.
- Important workload correction: the Bassols match's total recorded duration was about **3h06**, but it was **split across Wednesday and Thursday** after rain suspended play in the third set. On Thursday Maristany only completed the remaining portion of the deciding set. The fatigue disadvantage to Burel is therefore real but **smaller than a full 3h06 match played entirely the previous day**.

#### Broader recent clay form

- Burel's 2026 clay record is roughly **17-10** in the available secondary surface log; Maristany's is roughly **19-14**. Both are positive and close enough that neither receives a large generic surface-form adjustment.
- Burel's recent clay sequence contains multiple dominant straight-set wins, but those include lower-tier opposition; against comparable WTA-125-level resistance she has also played several long/competitive matches.
- Maristany reached the Montreux semifinal immediately before Valencia and has now won five of her last six completed matches, but per the Drive's streak rule the streak itself carries no directional weight. The useful evidence is the repeated competitive clay process and the direct Burel matchup.

#### Weather / court-state gate

- Tournament venue is outdoor clay at Sporting Club de Tenis de València.
- AEMET hourly forecast for València around **13:00 CEST**: approximately **24°C**, easterly wind around **8 km/h**, **0 mm** expected at that hour, humidity around the mid-60s, no active hazard.
- Rain/storm probability increases later in the afternoon (AEMET showed roughly **35% for 14:00–20:00**), so interruption risk is non-zero if the match runs long.
- The tournament had significant rain disruption on 16–17 Sep and maintenance was required to restore the clay courts. No exact same-day field-owner court-moisture/pace report was recovered for this quarterfinal.
- Treatment: weather/court state adds **width**, not an automatic Over/Under sign. A delay can also partially reduce Maristany's relative fatigue disadvantage.

#### Joint match object

**Winner family (`UNVALIDATED_SUBJECTIVE`):**
- Burel match win: **0.54**
- Maristany match win: **0.46**

**Set-count / winner family:**
- Burel 2-0: **0.29**
- Burel 2-1: **0.25**
- Maristany 2-0: **0.18**
- Maristany 2-1: **0.28**
- Three-set match mass: **0.53**

**Why Burel is only a slight winner:** higher historical level/ceiling, fresher schedule and strong recent return performance are offset by Maristany's current ranking, direct 11-Sep win, current clay consistency and Burel's error volatility in the H2H.

**Total-games component:**
- Central total: approximately **21.7 games**.
- Width: approximately **4.2 games**.
- Normalised edge vs 20.5: `|21.7 - 20.5| / 4.2 ≈ 0.29`.
- The three-set branch supplies most of the Over mass. Two-set Over paths still exist through 7-5/7-6 type sets; the Under is concentrated in cleaner 6-2/6-3-type straight-set wins.

**Handicap / separation:**
- Central game margin: approximately **Burel +1 game**, with broad width because both players have produced lopsided individual sets and high break rates.
- `TENNIS_3.5_GAME_BAND_NOT_DERIVED`: `BASE_RATES_REGISTER.md` has no field-owner-derived tennis 3.5-game cushion band. The handicap probability is therefore an event-tree estimate, **not** a published base-rate identity. Under the Drive fail-closed rule it cannot be promoted to Rank #1 merely because of the cushion.

**Coherent supplied-contract marginals:**
- Maristany +3.5 games: **0.62**
- Burel -3.5 games: **0.38**
- Over 20.5 games: **0.63**
- Under 20.5 games: **0.37**

**Coupling family:**
- Over 20.5 + Maristany +3.5: **0.43**
- Over 20.5 + Burel -3.5: **0.20**
- Under 20.5 + Maristany +3.5: **0.19**
- Under 20.5 + Burel -3.5: **0.18**
- Total = **1.00**.

Thus:
- `P(Rank #1 AND Rank #2)` ≈ **0.43**.
- `P(neither preferred decision wins)` ≈ **0.18** — principally a relatively clean Burel straight-set win such as 6-3, 6-3.
- Representative central state: **Burel 6-4, 4-6, 6-3** (29 games): Burel wins the match, **Over 20.5 wins**, and **Maristany +3.5 wins** by a three-game match margin.

#### Ranked picks — most likely to least likely under the governing gate structure

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Geometry | Why this rank | Primary failure path |
|---:|---|---:|---|---|---|---|
| **1** | **Total Games — OVER 20.5** | **0.63** | MEDIUM | FORCED_PAIR preferred side | Direct H2H reached 23 in three sets; joint set-count tree places ~53% on three sets; Maristany's two Valencia matches have been 24 and 28 games; both players' current clay games feature frequent breaks and score-state volatility. | Burel's freshness converts into a clean 6-2/6-3 or 6-3/6-3 win, or Maristany repeats a dominant straight-set branch. |
| **2** | **Guiomar Maristany Zuleta De Reales +3.5 games** | **0.62** | MEDIUM / `TENNIS_3.5_GAME_BAND_NOT_DERIVED` | FORCED_PAIR preferred side | Maristany won the direct clay H2H by three games, is 19-14 on clay in the available 2026 log, and has repeatedly stayed competitive at WTA 125 level. The cushion wins under every Maristany victory plus many close Burel wins. | Burel's rest/ceiling edge produces two efficient sets and 4+ games of separation; the most dangerous state is a 6-3, 6-3 or 6-4, 6-2 Burel win. |
| **3** | **Clara Burel -3.5 games** | **0.38** | MEDIUM-LOW / `TENNIS_3.5_GAME_BAND_NOT_DERIVED` | FORCED_PAIR non-preferred side | Burel has the stronger historical ceiling, is fresher after the walkover, and has multiple recent clay wins by 6+ games. A decisive Burel straight-set state is real. | Maristany wins outright or extends the match into a close three-set contest; either path usually defeats -3.5. |
| **4** | **Total Games — UNDER 20.5** | **0.37** | MEDIUM-LOW | FORCED_PAIR non-preferred side | Break-heavy clay can still create short sets, and both players have recent 15-19-game straight-set outcomes. | Any three-set match almost automatically clears 20.5; a pair of close straight sets can also clear the line. |

**Decision interpretation:** the four supplied rows are **two forced-pair decisions, not four independent bets**. Preferred sides are **Over 20.5** and **Maristany +3.5**.

#### Potential match winner

- **Projected match winner: Clara Burel — 0.54 `UNVALIDATED_SUBJECTIVE`**.
- **Maristany: 0.46**.
- This is intentionally a narrow winner edge. Burel's freshness and former top-50 ceiling give her the smallest advantage, while Maristany's direct clay win and current WTA-125 form keep the upset branch large.
- Winner call is **not equivalent** to Burel -3.5; a Burel match win by 1–3 games is a meaningful central branch and is exactly why Maristany +3.5 can rank above Burel -3.5.

#### Information not confirmed / integrity flags

- Exact sportsbook operator and **retirement/walkover settlement rules** were not supplied. `UNKNOWN_DEFINITION` applies to operator action after a retirement.
- No same-day field-owner report describing exact clay moisture/pace was recovered. Recent rain history is used only as uncertainty width.
- No current injury report was found for either player, but absence of a report is not proof of perfect health.
- Burel's current rank is a weak standalone proxy because of the injury-disrupted 2025 season; Maristany's ranking edge is therefore not treated as decisive.
- `TENNIS_3.5_GAME_BAND_NOT_DERIVED` — no field-owner-derived 3.5-game handicap cushion identity exists in the Drive base-rate register.
- No bookmaker odds, implied probabilities, market movement, prediction-site model outputs or tipster opinions are used as forecast evidence.
- No retrospective or settlement performed.
- **Current settlement status:** `UNSETTLED — PREGAME AT ISSUE`.

#### Settlement routes pre-registered

- Match result / sets / games: WTA official exact-event score record first.
- Exact set/game totals and match completion state: WTA official match stats/score; structured tennis match centre as corroboration if WTA page state is incomplete.
- Retirement/walkover operator action: cannot be graded without the user's sportsbook rules; research-grade sporting result remains separate from operator settlement.

#### Sources

| Source | Link / record | Access / state | Contribution | Quality / limitation |
|---|---|---|---|---|
| WTA official Valencia tournament page | https://www.wtatennis.com/tournaments/2061/Valencia/2026 | Opened 18 Sep 2026 | WTA 125 identity, outdoor clay, tournament dates/current round | Primary / field owner |
| Valencia municipal event page | https://www.fdmvalencia.es/es/eventos/bbva-open-internacional-de-valencia-wta-125-2026/ | Opened 18 Sep | Sporting Club venue/address | Government/local official |
| Official tournament site | https://openinternacionalvalencia.com/en/tournament/ | Opened 18 Sep | Venue, clay facilities, tournament context | Tournament field owner |
| WTA Schedule exact match | https://www.wtaschedule.com/matches/MTgzNzcw/guiomar-maristany-zuleta-de-reales-vs-clara-burel | Opened 18 Sep | Exact QF, 11:00 UTC, Center Court, pregame Scheduled state | Structured secondary; used because exact WTA match slug was not reliably surfaced |
| WTA Clara Burel profile/record | https://www.wtatennis.com/players/325320/clara-burel | Opened 18 Sep | Rank 301, career high 42, 2026 W/L, 2025 injury context | Primary WTA player record |
| WTA Guiomar Maristany profile/record | https://www.wtatennis.com/players/324786/guiomar-maristany-zuleta-de-reales/record | Opened 18 Sep | Rank 178, 2026 W/L, current tournament record | Primary WTA player record |
| WTA official Montreux H2H match page | https://www.wtatennis.com/tournaments/1112/montreux-125/2026/scores/LS007 | Opened 18 Sep | Direct same-surface H2H and in-match stats | Primary WTA record; crawl state partially stale but core stats corroborated |
| WTA Schedule Montreux match | exact 11 Sep Burel-Maristany result | Opened 18 Sep | 6-3,1-6,6-1; duration; points/serve/break stats | Structured secondary/corroboration |
| Tennis.com Burel-Teixido Valencia | 15 Sep 2026 exact match | Opened 18 Sep | Burel R1 score and serve/return/break stats | High-quality structured secondary |
| WTA Martina Trevisan record | WTA official 2026 Valencia entry | Opened 18 Sep | Trevisan-Burel W/O verification | Primary |
| Tennis.com Maristany-Bassols Valencia | 17 Sep completed match | Opened 18 Sep | Maristany R16 stats | High-quality structured secondary |
| Tennis Majors Maristany-Bassols | 17 Sep result | Opened 18 Sep | 6-3,3-6,6-4 and 3h06 total recorded duration | Secondary match record; duration spans interrupted match |
| Valencia rain/resumption report | Valencia Plaza / local reporting, 17 Sep | Opened 18 Sep | Bassols-Maristany suspended in third set; courts restored after heavy rain | Current local reporting; explains workload timing |
| Visibilitas tournament report | 18 Sep 2026 | Opened 18 Sep | Confirms Maristany completed suspended deciding set Thursday | Current tournament-specialist secondary |
| Tennis Explorer 2026 surface records | Burel / Maristany profiles | Opened 18 Sep | Approx 2026 clay records 17-10 and 19-14 | Secondary; mixed competition levels; contextual only |
| AEMET hourly València forecast | https://www.aemet.es/en/eltiempo/prediccion/municipios/horas/tabla/valencia-id46250 | Opened 18 Sep | 13:00 weather; later rain/storm risk | Spanish government weather; city station near venue rather than on-court sensor |
| Drive `RULES_TENNIS.md` | Sports Research Drive | Fresh-read 18 Sep | SFA-TENNIS, surface/current-regime, completion, score-tree and total requirements | Governing methodology |
| Drive `METHOD.md`, `RULES_GENERAL.md`, `CONTROLS.md` | Sports Research Drive | Fresh-read 18 Sep | v4.0, market-blind, joint object, G20/G31 and missingness handling | Governing methodology |
| Drive `BASE_RATES_REGISTER.md` | Sports Research Drive | Fresh-read 18 Sep | Tennis handicap band marked NOT_YET_DERIVED | Governing quantitative register |
| User-supplied slate | Current query | Current | Exact ±3.5 and O/U 20.5 contracts | Contract source only; operator terms absent |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| Direct same-surface H2H and current ranking point in opposite directions once Burel's injury-return context is considered | `RULES_TENNIS.md` regime-dominance / H2H continuity | Existing controls correctly applied — **NO CHANGE** |
| Maristany's long R16 duration was split by weather across two days | `RULES_TENNIS.md` workload / `RULES_GENERAL.md` source-state | Existing disaggregation rule correctly applied; do not label 3h06 as all previous-day load |
| Burel walkover creates meaningful rest but no performance sample | `RULES_TENNIS.md` workload/completion | Existing exposure logic — **NO NEW RULE** |
| Tennis 3.5-game cushion band absent | `BASE_RATES_REGISTER.md` | **DATA GAP** — derive prospectively from field-owner record before using an identity |
| Rain-disrupted clay can alter rest and court state in opposite directions | `RULES_TENNIS.md` weather/court mechanism | Width-only unless a current same-day directional surface mechanism is verified |

#### Settlement and retrospective — 19 Sep 2026

- **Final status:** `SETTLED — FINAL`.
- **Final:** Clara Burel defeated Guiomar Maristany Zuleta De Reales **6-2, 6-4** on clay in the Valencia WTA 125 quarterfinal. Total games = **18**; Burel game margin = **+6**.
- **Canonical-ID audit:** no P-461 collision in the fresh combined-log check.

##### A. Prediction outcome

| Rank | Frozen selection | Final | Result |
|---:|---|---:|---|
| 1 | Over 20.5 games | 18 games | **LOSS** |
| 2 | Maristany +3.5 games | Burel +6 | **LOSS** |
| 3 | Burel -3.5 games | Burel +6 | **WIN** |
| 4 | Under 20.5 games | 18 games | **WIN** |
| — | Projected winner: Burel | Burel won | **WIN** |

**Diagnostics:** Rank-1 = **LOSS**; Hit@2 = **0**; Wins@2 = **0/2**; binary NDCG@2 = **0**. This is the most important top-two ranking failure in this settlement batch.

##### B. Why each pick won or lost

**R1 Over 20.5 — LOSS.** The card allocated roughly 53% to a three-set match and leaned on the 23-game Montreux meeting from seven days earlier. The actual match followed the known but underweighted Burel straight-set-control branch. At 6-2, 6-4, there was neither a third set nor an extended close set to clear 20.5.

**R2 Maristany +3.5 — LOSS.** Burel won by six games. The cushion depended on Maristany either winning or keeping a Burel victory narrow. Burel's freshness and improved control made the separation branch larger than forecast.

**R3 Burel -3.5 — WIN.** The exact path described pre-game — Burel's superior historical ceiling plus a rest advantage producing a decisive straight-set result — occurred. The card recognised this path but ranked it too low.

**R4 Under 20.5 — WIN.** Once the match resolved in two sets with a 6-2 first set, the Under had substantial room.

##### C. Rank-1 failure review

Over 20.5 was ranked first because the forecast expected a competitive replay of the Montreux matchup, with a large deciding-set branch. The direct H2H was relevant — same players, clay, only seven days earlier — but the context had changed: Burel had a walkover in Valencia and materially more recovery, while Maristany came through a long, rain-interrupted three-set round of 16. The analysis noticed the freshness differential, then deliberately reduced it after correcting the 3h06 workload interpretation. The eventual mistake was **not the correction itself**; it was failing to let the still-real rest differential move enough mass from “three sets/close” to “Burel 2-0”.

The pre-game card explicitly named short decisive Burel scorelines such as 6-3 6-3 / 6-4 6-2 as the both-fail state for the top two. That is exactly the class that occurred (6-2 6-4). Under existing Tennis control 12 and `G-L1`, a named kill path should have had enough branch mass to affect rank order. Burel -3.5 or Under 20.5 could reasonably have been above at least one top-two row once freshness was treated as a current-regime mechanism.

##### D. Top-two review

Both top-two selections lost and both lower complements won. This is a clean ranking failure, not just boundary variance. The two top rows shared the same assumption: Maristany remains competitive enough to extend the match and/or stay within three games. Once Burel controlled the match, both failed together. Future top-two construction should explicitly identify this shared-driver dependence and avoid treating two correlated “competitive match” rows as diversification.

##### E. Total review

The total missed because the three-set weight was too high. The prior H2H total of 23 was descriptive but should not have dominated a current workload-adjusted match tree. There is no evidence for a permanent “rematch Under” rule; the process fix is to reweight the straight-set branch when a current, named mechanism materially changes player readiness.

##### F. What went right

- Projected winner Burel was correct.
- The analysis correctly identified Burel's higher historical ceiling and freshness edge.
- The decisive Burel straight-set path was explicitly present before the match.
- The handicap-band data gap was honestly disclosed.

##### G. Blind spots and future handling

- **H2H overweight:** one same-surface meeting cannot automatically control a rematch when workload/rest states differ.
- **Shared-driver top-two dependence:** Over 20.5 and Maristany +3.5 both needed a competitive match.
- **Branch-weight execution:** the Burel 2-0 kill path was named but underweighted. Existing rules already cover this; execution needs improvement rather than a new permanent rule.

##### H. Mandatory validation questions

| Question | Retrospective answer |
|---|---|
| Participants/starting status obtained? | **Yes.** Singles participants, surface, round and schedule were verified. |
| Bench/reserve context relevant? | **N/A** for tennis. |
| Coaching information material? | No material coach-change evidence was required for this card. |
| Injuries/rest/late withdrawals checked? | **Yes.** Burel's prior injury history, Valencia walkover and Maristany workload were explicitly researched. |
| Sources accurate/current? | Workload/H2H sources were useful; WTA exact-match page later showed stale/suspended crawl state. |
| Better sources available? | Use WTA draw/result plus a second high-quality exact-match result when WTA live-page cache is stale. |
| Blind spots? | Too much mass on competitive/three-set rematch state. |
| Future accounting? | Rebuild straight-set/three-set mixture after workload/rest changes; do not merely mention them. |

##### I. Source audit

- WTA exact-match page: https://www.wtatennis.com/tournaments/2061/valencia-125/2026/scores/LS006 — official identity/stats route, but crawl state was stale/suspended during retrospective retrieval and therefore was not used alone to declare the final.
- TennisActu final report: https://www.tennisactu.net/news-wta-valence-clara-burel-prend-sa-revanche-et-fonce-en-demi-finales-127082.html — confirms Burel 6-2, 6-4 and the prior Montreux 6-3, 1-6, 6-1 result. **High-quality secondary corroboration.**

**Learning disposition:** no new tennis rule. Existing scoreline-coherence and weighted-branch controls were sufficient but under-executed.

---

### P-462 — Soccer / Chinese Super League — Zhejiang FC vs Wuhan Three Towns

- **Canonical ID:** P-462 (local mini-log sequence; fresh pre-issue reconciliation found no P-462 collision in `PREDICTION_LOG_COMBINED_4.md`)
- **Sport / competition:** Soccer — Chinese Super League, 2026 regular season, Round 22 postponed fixture
- **Event:** Zhejiang FC vs Wuhan Three Towns FC
- **Venue:** Huanglong Sports Center Stadium, Hangzhou, Zhejiang, China
- **Scheduled start:** 18 Sep 2026, 19:35 CST (China) = 18 Sep 2026, 21:35 AEST (Australia/Melbourne)
- **Game state at issue:** `PREGAME / SCHEDULED`; the exact structured match record still showed Scheduled at the final volatile refresh.
- **Research cutoff / final volatile refresh:** 18 Sep 2026, 21:16:42 AEST / 19:16:42 CST
- **Method version:** MDS-2026.09.06-v4.0 / SFA-SOCCER
- **Population status:** EXPLORATORY — NOT SCORED; LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE
- **Operating mode:** SPORTS_ONLY / MARKET_BLIND. No odds, implied probabilities, market movement, consensus or tipster selections entered the forecast.
- **User-supplied contracts:** First-half goals O/U 0.5; full-time combined goals O/U 2.5.
- **Additional model-selected contracts:** Zhejiang team total Over 0.5; Zhejiang or Draw (1X); total corners Over 8.5. The corner line is a model-selected reference threshold and is actionable only if the user's operator actually offers the same standard 90-minute corner contract.

#### Identity / rules / endpoint

- Exact fixture identity, venue and 19:35 China kickoff were verified for the postponed Round 22 CSL fixture.
- Standard league endpoint: regulation 90 minutes plus stoppage time; draw live. No extra time/penalties.
- Current CSL population is a 16-club balanced calendar-year league. VAR is in use.
- Operator-specific abandonment, player-stat, corner and settlement wording was not supplied; those fields remain `UNKNOWN_DEFINITION` where relevant.

#### Final starting XIs / benches / availability

**Zhejiang starting XI:** Zhao Bo; Xu Junchi, Sun Guowen, Lucas Possignolo, Zhang Aihui; Park Jin-seop, Marko Tolić, Cheng Jin; Alexandru Mitriță, Tao Qianglong, Gao Di.

**Zhejiang bench:** Dong Chunyu, Huo Shenping, Wang Yang, Bao Shengxin, Tong Lei, Wang Shiqin, Qian Jiegei, Wu Wei, Zhang Jiaqi, Jiang Yuxuan, Ning Fangze.

- Zhejiang started **four foreign players**: Lucas, Park Jin-seop, Tolić and Mitriță.
- **Wang Yudong** and **Liu Haofan** are absent while with China's Asian Games/U23 group. Wang had been a major attacking contributor; Liu was an established defensive starter.
- **Felippe Cardoso** did not make the XI or bench after a reported muscle problem and missed pre-match field work.
- Mitriță was monitored after a training concern in the pre-match press conference but passed the practical participant handshake and starts.

**Wuhan Three Towns starting XI:** Fang Jingqi; He Guan, Xu Haofeng, Li Ang, Ming Tian; Zhang Xiaobin, Adriano Firmino; Gustavo Sauer, Kilian Bevis, Antoine Lotet; Jhonder Cádiz.

**Wuhan bench:** Guo Jiayu, Li Shenyuan, Long Wei, Wang Jinxian, Zheng Haoqian, Liao Chengjian, Chen Zhechao, Min Zixi, Liu Yiming, Xiong Jizheng, Wang Yi, Zhong Jinbao.

- Wuhan started **five foreign players**: Sauer, Adriano, Bevis, Cádiz and Lotet.
- **Zheng Kaimu** is absent from the match-day group, consistent with the pre-match suspension listing.
- Earlier pre-match reporting that He Guan would miss out is superseded by the final XI: **He Guan starts**.
- Coach **Suárez** said Wuhan's overall physical condition was very good, with only ordinary late-season niggles not expected to materially affect the match.
- Zhejiang head coach **Ross Aloisi** had flagged Mitriță for monitoring; the final XI resolves that uncertainty in favour of availability.

**Participant completeness:** starting XI, goalkeeper and full named bench were retrieved for both teams. `G14.2` participant/bench completeness is satisfied for this card.

#### Current team / venue state

**Zhejiang 2026:** 25 league matches, **9-6-10**, 41 GF / 42 GA, 28 points after the recorded starting deduction; 10th entering the match.

**Zhejiang at home:** 12 matches, **6-3-3**, 24 GF / 17 GA; approximately **2.00 scored and 1.42 conceded per home match**. Current statistical lane gives home xG about **1.78** and xGA about **1.49**.

**Wuhan 2026:** 25 league matches, **5-11-9**, 38 GF / 42 GA, 21 points; 15th entering the match.

**Wuhan away:** 12 matches, **1-6-5**, 20 GF / 26 GA; approximately **1.67 scored and 2.17 conceded per away match**. Current statistical lane gives away xG about **1.29** and xGA about **1.84**. Wuhan had **0 clean sheets in 12 away league matches** in the retrieved current split.

- Zhejiang's home attacking level remains strong, but Wang Yudong + Cardoso absences reduce the finishing/creation ceiling relative to season-long full-squad numbers.
- Wuhan's away defence is the clearest structural vulnerability, but its confirmed five-foreigner attacking group preserves a credible away-scoring branch, especially against a Zhejiang defence missing Liu Haofan.
- Table position gives Wuhan strong relegation-pressure incentive, but motivation is not used as a free positive coefficient; it enters only through plausible trailing-state attacking exposure.

#### Mandatory L5 / L10 / L15 / L20 trend audit

From the current league-results sequence at research time:

| Window | Zhejiang | Wuhan Three Towns |
|---|---|---|
| L5 | 11 GF / 8 GA; O2.5 ~80%; BTTS ~80% | 10 GF / 7 GA; O2.5 ~60%; BTTS ~80% |
| L10 | 21 GF / 19 GA; O2.5 ~80%; BTTS ~90% | 16 GF / 12 GA; O2.5 ~40%; BTTS ~60% |
| L15 | 30 GF / 28 GA; O2.5 ~73%; BTTS ~80% | 25 GF / 21 GA; O2.5 ~47%; BTTS ~73% |
| L20 | 34 GF / 36 GA; O2.5 ~70%; BTTS ~70% | 30 GF / 31 GA; O2.5 ~50%; BTTS ~65% |

- Zhejiang's recent match environment has been consistently open, while Wuhan's middle windows are less Over-heavy. This is **diagnostic**, not a streak coefficient.
- The directional mechanisms used are current home/away creation and prevention, confirmed attackers/absences, and score-state behaviour; the raw streak percentages do not independently move the forecast.

#### Same-season H2H / continuity

- First 2026 meeting, 21 Apr at Wuhan: **Wuhan 2-0 Zhejiang**, with goals by **Jhonder Cádiz (41')** and **Kilian Bevis (78')**.
- That direct comparator also produced a first-half goal and a meaningful set-piece/corner route to Cádiz's opener.
- It is not treated as controlling because venue is reversed and the current participant sets differ materially. Wang Yudong played the first meeting but is absent tonight; Zhejiang now have Mitriță and Lucas available, while Wuhan's current XI/roles have also evolved.

#### Weather / surface

- Exact-venue current conditions around the game window: approximately **28°C at 19:00–20:00 local, easing to ~27°C**, clear, with only a small precipitation signal (~7%).
- `G15.1` exact-venue weather requirement is satisfied.
- No automatic Over/Under adjustment is applied from warm, dry conditions. The main effect is normal late-match fatigue width, not a directional goal coefficient.

#### Goal-process budget

One coherent regulation goal object is used for the supplied first-half/full-time totals and winner state.

**Zhejiang regulation goal centre:** approximately **1.7–1.8**.
- Baseline support: 2.00 home scoring, ~1.78 home xG, Wuhan 2.17 away GA / ~1.84 away xGA.
- Downward current-participant adjustment: Wang Yudong and Cardoso unavailable.
- Countervailing support: Mitriță starts after the injury-monitoring concern; Wuhan's away clean-sheet rate is 0/12 in the retrieved split.

**Wuhan regulation goal centre:** approximately **1.4–1.5**.
- Baseline support: 1.67 away scoring / ~1.29 away xG against Zhejiang 1.42 home GA / ~1.49 home xGA.
- Upward current-participant mechanism: Cádiz, Bevis, Sauer, Adriano and Lotet all start; Liu Haofan is absent for Zhejiang.
- Downward constraint: Wuhan's away creation has been less stable than its raw goal average and Zhejiang retain the stronger home territorial profile.

**Combined centre:** approximately **3.1–3.3 regulation goals**, with wide soccer finishing variance.

**First-half centre:** approximately **1.35–1.45 goals**. Zhejiang's retrieved home 1H O0.5 rate is around 75%; Wuhan's away figure around 67%. The first H2H also had a 41st-minute opener, but that single match is only a comparator.

#### Corner process

- Current 2026 corner lanes place Zhejiang near **5.4 corners won per match** and Wuhan near **4.8**, with each conceding enough corners to keep the combined expectation around the league's ~10-corner region.
- Secondary current corner datasets put Zhejiang matches around **10.4 total corners** and Wuhan matches around **10.5**, with Over 8.5 occurring roughly **68%** and **72%** respectively in their season samples.
- The first 2026 H2H produced **13 total corners (Wuhan 6, Zhejiang 7)**.
- Mechanism: both teams retain wide attacking routes; Wuhan's credible trailing-state branch raises cross/set-play exposure, while Zhejiang's home territorial edge raises their own corner opportunity.
- Limitation: a complete field-owner cross/block/end-line-event chain was not available. Therefore the corner row is capped at **MEDIUM-LOW / FORCED RANK**, and the current secondary corner sources are not promoted to field-owner status.
- Research-grade settlement route pre-registered: exact-match detailed-stat provider (Sofascore or equivalent structured record) with independent corroboration if needed. Operator-action grading remains unknown without operator terms.

#### Joint outcome-state families (`UNVALIDATED_SUBJECTIVE`)

| Family | Approx. mass | Representative scores / mechanism |
|---|---:|---|
| Zhejiang home-control + normal conversion | 0.31 | 2-0, 2-1; home territory, Wuhan away defensive weakness |
| Open / mutual-conversion state | 0.27 | 2-2, 3-1, 3-2; early goal creates chase/counter space |
| Tight / finishing-weak state | 0.22 | 1-0, 1-1, 0-0; Zhejiang missing attacking pieces, finishing variance |
| Wuhan counter / upset state | 0.20 | 1-2, 0-1, 1-3; five-foreigner attack punishes Zhejiang defensive absences |

Representative central state: **Zhejiang 2-1 Wuhan Three Towns**.

#### Ranked five picks

| Rank | Contract | P (`UNVALIDATED_SUBJECTIVE`) | Evidence | Status / rationale | Primary kill path |
|---:|---|---:|---|---|---|
| **1** | **Zhejiang team total OVER 0.5 goals** | **0.82** | MEDIUM-HIGH | Wuhan have conceded in all 12 retrieved away league matches; Zhejiang average 2.00 home goals and ~1.78 home xG. Wang/Cardoso absences are already priced as a downward adjustment, while Mitriță starts. | Wuhan reproduce a low-event away defensive performance and Zhejiang's reduced front line wastes its chances. |
| **2** | **Zhejiang or Draw (1X), regulation** | **0.76** | MEDIUM | Zhejiang are 6-3-3 at home; Wuhan 1-6-5 away. Home territorial/xG matchup favors Zhejiang, but draw mass is substantial because Zhejiang are missing Wang Yudong/Cardoso and Liu Haofan. | Wuhan's confirmed foreign front five exploit transition space and win outright. |
| **3** | **1st Half Goals OVER 0.5** | **0.75** | MEDIUM | `FORCED_PAIR` preferred side. Home/away first-half profiles are both above two-thirds, first H2H opened at 41', and both confirmed XIs preserve attacking threats. | Cautious opening + poor finishing produces 0-0 at HT. |
| **4** | **Total Corners OVER 8.5** | **0.67** | MEDIUM-LOW / FORCED RANK | Model-selected reference line; season corner environments are ~10.4–10.5 and direct H2H had 13. Separate corner mechanism exists, but field-owner event-chain depth is incomplete. | Early efficient scoring or central possession suppresses wide/corner-generating sequences. |
| **5** | **Total Combined Goals OVER 2.5** | **0.62** | MEDIUM | `FORCED_PAIR` preferred side. Joint goal centre ~3.1–3.3; Zhejiang home/Wuhan away profiles are high-event, but Zhejiang's attacking absences materially cap confidence. | 1-0 / 1-1 / 2-0 finishing-weak state dominates. |

**Supplied opposite sides:**
- 1H **Under 0.5**: **0.25** — non-preferred side of the forced pair.
- Full-time **Under 2.5**: **0.38** — non-preferred side of the forced pair.

#### Winner projection

- **Zhejiang win: 0.47**
- **Draw: 0.29**
- **Wuhan Three Towns win: 0.24**
- **Potential game winner: Zhejiang FC**, but only as a moderate plurality rather than a high-confidence outright call.

Rationale: Zhejiang's home split and Wuhan's away defence give Zhejiang the territorial/scoring edge. The margin is reduced by the absences of Wang Yudong, Cardoso and Liu Haofan, while Wuhan's final XI retains its strongest foreign attacking group.

#### Cross-row dependence / top-two check

- Rank #1 and Rank #2 share the Zhejiang-home-control driver but are not duplicates: Zhejiang can score and still lose; 1X can win in a 0-0 draw.
- Approx. **P(R1 ∧ R2) = 0.68**.
- Approx. **P(¬R1 ∧ ¬R2) = 0.13**, concentrated in Wuhan win-to-nil states.
- Rank #3 and Rank #5 share an early-goal/open-game pathway; Rank #4 corners can still win in a poor-finishing state, so it is only partially coupled to the goal Overs.

#### Integrity / missingness flags

- Exact starting XIs and full benches retrieved for both teams; no `BENCH_NOT_RETRIEVED` cap.
- Earlier secondary claim that He Guan would be unavailable was superseded by the final XI and is not used.
- Secondary speculation about a special foreign-player restriction is not used as a rule input; the actual released XI is controlling and shows Wuhan with five foreign starters.
- Corner event-chain source depth remains incomplete: `CORNER_FIELD_OWNER_EVENT_CHAIN_NOT_FULLY_RETRIEVED`.
- Exact operator settlement rules for corners/abandonment are `UNKNOWN_DEFINITION`.
- No soccer 1.5 handicap is ranked, so the Drive's `SOCCER_1.5_BAND_NOT_DERIVED` gap does not affect the ordinal.
- No retrospective or settlement performed.
- **Current settlement status:** `UNSETTLED — PREGAME`.

#### Sources

| Source | Record / URL | Contribution | Quality / limitation |
|---|---|---|---|
| Chinese Super League / Wuhan Three Towns match-day notice | Official CSL / Wuhan club social record, 18 Sep 2026 | Exact postponed Round 22 fixture, 19:35 kickoff, Huanglong venue | Field-owning/club identity lane |
| Zhibo8 final lineup report | https://m.zhibo8.com/news/web/zuqiu/2026-09-18/6aace17c15293native.htm | Final XIs and full benches; Zhejiang 4 foreign starters, Wuhan 5 | Current secondary reproducing released lineups; exact participant record |
| Zhejiang pre-match press conference / China football report | https://m.zhibo8.cc/news/web/zuqiu/2026-09-17/6aabd8716495anative.htm | Ross Aloisi; Mitriță monitored after training concern | Primary-quote secondary relay; final XI resolves availability |
| Wuhan Three Towns pre-match press conference | https://m.zhibo8.cc/news/web/zuqiu/2026-09-17/6aabe51708f5fnative.htm | Suárez; team physical condition; match importance | Club-origin quotes via current sports relay |
| Current Zhejiang team statistics | https://footystats.org/clubs/zhejiang-professional-fc-839 | 25-match season record, home 6-3-3, 24-17 goals, home xG/xGA, first-half splits | Statistical secondary; no betting/odds fields used |
| Current Wuhan team statistics | https://footystats.org/clubs/wuhan-three-towns-fc-672253 | 25-match record, away 1-6-5, 20-26 goals, away xG/xGA, totals/BTTS/1H splits | Statistical secondary; no odds/market fields used |
| CSL corner statistics / FootyStats | https://footystats.org/cn/china/chinese-super-league/corner-stats | Current competition/team corner environment | Secondary derivative; capped evidence |
| TotalCorner / current team corner record | Current 2026 CSL team pages retrieved 18 Sep | Zhejiang/Wuhan corner for-against totals and Over 8.5 sample rates | Secondary derivative; field-owner promotion prohibited |
| Sofascore exact Apr-21 H2H | https://www.sofascore.com/football/match/wuhan-three-towns-zhejiang/XTnscdtc | 2-0 first meeting, 41'/78' goals, lineups, detailed-stat route including corners | Structured secondary; direct comparator / future settlement fallback |
| Structured exact-venue weather | Huanglong Sports Center Stadium, 18 Sep 2026 game window | Clear ~28→27°C, ~7% precipitation signal | Current structured weather; satisfies G15.1 |
| Drive `METHOD.md`, `RULES_GENERAL.md`, `CONTROLS.md` | Sports Research Drive | MDS-v4.0, gates, probability/ranking/source discipline | Governing methodology |
| Drive `RULES_SOCCER.md`, `LEAGUE_RULES_SOCCER.md` | Sports Research Drive | SFA-SOCCER, goal/corner chains, CSL identity/rules | Governing sport/competition methodology |
| Drive `BASE_RATES_REGISTER.md` | Sports Research Drive | Soccer 1.5 band gap; not used because no handicap ranked | Governing quantitative register |
| User-supplied slate | Current query | Exact 1H O/U 0.5 and full-time O/U 2.5 contracts | Contract source only |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| Final XI superseded earlier He Guan absence reporting | `SOURCES.md` / participant-handshake discipline | Existing final-participant handshake correctly applied — **NO CHANGE** |
| Wang Yudong + Cardoso absence lowers Zhejiang attack while Liu Haofan absence raises Wuhan scoring route | `RULES_SOCCER.md` SO-S1/SO-S2 participant-to-exposure chain | Existing mechanism; **NO NEW RULE** |
| Secondary foreign-player-rule speculation conflicted with actual released XI | `LEAGUE_RULES_SOCCER.md` / source hierarchy | Competition-rule verification candidate; actual XI controls this card; **NO FORECAST WEIGHT FROM RUMOUR** |
| CSL corner secondary data supports an 8.5 reference but field-owner event-chain detail is incomplete | `DATA_SOURCE_REGISTER.md` / `SOURCES.md` | Source-coverage gap; maintain MEDIUM-LOW cap |

---

#### Settlement and retrospective — 19 Sep 2026

- **Final status:** `SETTLED — FINAL`.
- **Final:** Zhejiang **4-1** Wuhan Three Towns; **half-time 2-0**; corners **4-7** (11 total).
- **Canonical-ID audit:** no P-462 collision in the fresh combined-log check.

##### A. Prediction outcome

| Rank | Frozen selection | Final | Result |
|---:|---|---:|---|
| 1 | Zhejiang team total Over 0.5 | Zhejiang 4 | **WIN** |
| 2 | Zhejiang or Draw (1X) | Zhejiang won | **WIN** |
| 3 | 1H Goals Over 0.5 | 2 first-half goals | **WIN** |
| 4 | Total Corners Over 8.5 | 11 corners | **WIN** |
| 5 | Total Goals Over 2.5 | 5 goals | **WIN** |
| — | Projected winner: Zhejiang | Zhejiang won | **WIN** |
| — | 1H Under 0.5 (supplied complement) | 2 first-half goals | **LOSS** |
| — | Under 2.5 (supplied complement) | 5 total goals | **LOSS** |

**Diagnostics:** Rank-1 = **WIN**; Hit@2 = **1**; Wins@2 = **2/2**; binary NDCG@2 = **1.000**. All five published ranked selections won.

##### B. Why each pick won

**R1 Zhejiang team Over 0.5 — WIN.** It cleared in the second minute. The lineup-adjusted attack remained sufficiently dangerous despite Wang Yudong and Cardoso absences because Mitriță and Tolić both started and were central to the scoring.

**R2 Zhejiang/Draw — WIN.** Zhejiang's home strength and Wuhan's weak away record translated into a decisive home result. The safer 1X framing was still methodologically appropriate even though the realised margin was large.

**R3 1H Over 0.5 — WIN.** This was not a historical-frequency-only call: the card required a current early-chance mechanism. Tolić scored from an early corner sequence in minute 2 and Mitriță made it 2-0 in minute 14. The current lineup and attacking roles directly supported the branch.

**R4 corners Over 8.5 — WIN.** The match produced 11 corners, with Wuhan winning the corner count 7-4 despite losing 4-1. That is consistent with the trailing-state chase mechanism: Wuhan had 65% possession and much higher attacking volume but poor finishing, which can generate corners without goals.

**R5 Over 2.5 — WIN.** It cleared before the late red card could be the main cause: Zhejiang were already 4-0 by the 80th minute, while Li Ang was sent off in the 86th. The Over therefore should be credited primarily to Zhejiang's early/efficient transition and set-piece conversion, not to dismissal variance.

##### C. Rank-1 review

Rank #1 won immediately and was robust to most game states. It required only one Zhejiang goal, supported by a strong home scoring baseline and a confirmed XI containing Mitriță, Tolić, Tao Qianglong and Gao Di. The ranking was justified. The 0.82 figure remains unvalidated, but the ordinal process was strong.

##### D. Top-two review

Both top-two rows won. They shared a Zhejiang-home-strength driver, but Rank #1 required less than Rank #2 and therefore deserved first place. This is a good example of ordering by number of extra conditions: Zhejiang O0.5 needed a goal; 1X additionally needed Wuhan not to outscore them.

##### E. Over/Under review

Both preferred Over directions won: 1H Over 0.5 and FT Over 2.5. The early goal mechanism was validated by the actual opening; the full-game Over was then aided by match state but already had strong home/away scoring support. The realised 4-1 is wider than the 2-1 representative centre and reflects high Zhejiang finishing efficiency (four goals from six shots on target). Do not turn that into a permanent finishing coefficient.

##### F. What went right

- Late starting-XI retrieval materially improved the card. Earlier uncertainty around Mitriță was resolved by the actual XI.
- Earlier He Guan absence reporting was correctly discarded once the confirmed XI showed him starting.
- The model properly downgraded Zhejiang's season-long attack for Wang Yudong/Cardoso absences without overcorrecting to a low-scoring thesis.
- Corner reasoning was independent from goal reasoning and succeeded via Wuhan's trailing-state pressure.

##### G. Blind spots and future handling

No major participant blind spot remained at issue because both XIs and benches were obtained. The main source-quality limitation was derivative corners: the exact 4-7 field was recovered from a secondary exact-match report rather than a stable field-owner CSL statistical endpoint. Keep corner source quality capped until a stronger reusable route is established.

##### H. Mandatory validation questions

| Question | Retrospective answer |
|---|---|
| Confirmed starting XIs obtained? | **Yes, both.** |
| Full benches/subs obtained? | **Yes, both match-day benches were retrieved.** |
| Coaches/managers obtained? | **Yes**, and pre-match fitness comments were checked. |
| Injuries/suspensions/rest/late changes checked? | **Yes.** Wang Yudong/Liu Haofan/Cardoso and Wuhan availability were explicitly handled. |
| Sources accurate/current? | Confirmed-XI reporting was accurate; final secondary event data are internally consistent. |
| Better sources available? | A stable official CSL/CFA detailed event-stat endpoint would be preferable, especially for corners. |
| Blind spots? | Mainly settlement-source ownership for corners, not participant modelling. |
| Future accounting? | Preserve final-XI refresh; continue separate corner process and pre-register stronger settlement route where available. |

##### I. Source audit

- Exact final/result report with HT and corners: https://www.qiumiwu.com/news/2006152218971 — 4-1, HT 2-0, corners 4-7, event timeline and team stats. **Secondary exact-event source.**
- Match video/result page: https://www.qiumiwu.com/game/video-110534337681 — independently displays 4-1, HT 2-0 and corners 4-7.
- Chinese match report: https://www.sohu.com/a/1077957651_463728 — 4-1 narrative, early Tolić/Mitriță goals, later events.
- Sina/Qianjiang context: https://k.sina.com.cn/article_2265295433_8705aa4902001cwmm.html — final and lineup-absence context.

**Learning disposition:** final-XI and current-mechanism workflow worked well. Do not promote the secondary corner provider solely because this one settlement was accurate.

---

---

### P-463 — Baseball / MLB — Chicago Cubs @ Cincinnati Reds

- **Canonical ID:** P-463 (fresh pre-issue reconciliation against `PREDICTION_LOG_COMBINED_4.md` found no P-463 collision)
- **Sport / competition:** Baseball — Major League Baseball, 2026 regular season
- **Event:** Chicago Cubs @ Cincinnati Reds
- **Official event / preview identity:** MLB game preview record `824463`
- **Venue:** Great American Ball Park, Cincinnati, Ohio
- **Scheduled start:** 18 Sep 2026, 18:40 EDT = **19 Sep 2026, 08:40 AEST**
- **Game state at issue:** `PREGAME / SCHEDULED` at the final volatile refresh. No first-pitch/live information is used.
- **Research cutoff / final volatile refresh:** **19 Sep 2026, 08:36:05 AEST / 18 Sep 2026, 18:36:05 EDT**
- **Method version:** MDS-2026.09.06-v4.0 / SFA-BASEBALL
- **Population status:** MLB = `PRIMARY_SCORED` population, while this mini-log remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**
- **Operating mode:** `SPORTS_ONLY / MARKET_BLIND`
- **User-supplied contracts:** Cubs -1.5; Reds +1.5; Combined Total Over 8.5; Combined Total Under 8.5
- **At issue:** no retrospective was performed.

#### Identity / participant handshake

**Official starters**
- **Chicago:** Clay Holmes, RHP — MLB probable-pitcher page: **6-7, 2.85 ERA, 71 SO**
- **Cincinnati:** Chase Burns, RHP — **15-3, 2.80 ERA, 151.1 IP, 181 SO, 1.15 WHIP**; StatMuse/MLB current record also shows ~29.4% K%, 8.8% BB%, ~3.16 FIP.
- Baseball Savant current-roster matchup sample: Holmes vs current Reds hitters, 30 PA / .236 wOBA (tiny descriptive sample); Burns vs current Cubs hitters, 32 PA / .274 wOBA. Neither tiny sample is allowed to own the forecast.

**Burns workload / role is the largest pitching-state variable**
- MLB's own game preview says Burns is making a **shortened outing**, with a piggyback/bulk plan after him.
- Current reporting places the target around **50–55 pitches**. On 13 Sep he worked only **3.0 IP, 2 ER, 5 K** against Milwaukee after returning from a grade-1 right flexor strain.
- The nominal follow-on lefty **Brandon Williamson** is not treated as a fresh normal piggyback: he threw **2.0 innings on 17 Sep**, the day before this game. His 2026 line entering today is roughly **5.62 ERA / 1.56 WHIP over 41.2 IP**.
- Cincinnati recalled **Julian Aguiar** on 18 Sep after placing Julian Garcia on the IL; current lineup/bulk sources list Aguiar as a plausible post-Burns length option.
- This creates a materially wider Cincinnati pitching distribution after Burns exits.

**Holmes current form**
- Recent five starts recovered:
  - 12 Sep vs PIT: **5.2 IP, 2 ER**
  - 6 Sep @ MIA: **4.1 IP, 8 ER**
  - 31 Aug vs MIL: **6.0 IP, 0 ER**
  - 25 Aug @ ARI: **7.0 IP, 0 ER**
  - 19 Aug vs CWS: **5.1 IP, 1 ER**
- The Miami blow-up remains an explicit contact/sequencing tail; otherwise the current five-start run is strong.

#### Batting-order / availability state

- MLB's official starting-lineup page still showed the two batting orders as **TBD** at the 08:36 AEST cutoff.
- Current secondary lineup feeds consistently showed:
  - **Cubs expected/secondary order:** Pete Crow-Armstrong, Seiya Suzuki, Michael Busch, Alex Bregman, Ian Happ, Nico Hoerner, Michael Conforto, Dansby Swanson, Carson Kelly (exact 8/9 ordering varied slightly by provider).
  - **Reds expected/secondary order:** Carlos Jorge, Elly De La Cruz, Sal Stewart, Tyler Stephenson, JJ Bleday, Eugenio Suárez, Héctor Rodríguez, Jose Trevino, Matt McLain.
- **Dansby Swanson was officially activated from the 10-day IL on 18 Sep** after an oblique injury; BJ Murray Jr. was optioned.
- Cincinnati moved **Spencer Steer** to the 60-day IL (right wrist sprain), placed **Julian Garcia** on the 15-day IL (right elbow loose bodies), recalled Julian Aguiar and claimed Oswaldo Cabrera.
- Because the field-owner batting orders were not published in the accessible MLB lineup endpoint at freeze, `STARTING_LINEUPS_NOT_OFFICIAL_AT_FREEZE` applies. All four supplied rows therefore carry a participant-missingness evidence cap; no player prop is ranked.

#### Team-strength / current-regime baseline

- **Cubs:** 85-68, **817 RS / 674 RA**, +143 run differential, 40-35 away; season scoring approximately **5.34 runs/game**.
- **Reds:** 71-82, **633 RS / 787 RA**, -154 run differential, 37-41 home; season scoring approximately **4.14 runs/game** and allowing ~5.14/game.
- Cubs recent five games: **25 runs scored** (5.0/game).
- Reds recent five games: **13 runs scored** (2.6/game).
- Reds current last-10 record: **2-8**; the losing streak itself carries zero forecast weight. The usable mechanisms are the weakened pitching depth, lineup availability and current scoring/allowance processes.
- 2026 season H2H entering this game: Cubs lead the series **7-3**. Old H2H is descriptive only; it does not override the current Burns/Holmes/pitching-depth state.

#### Venue / weather / park

- Great American Ball Park exact-venue weather around first pitch: roughly **26°C**, humid, with a small shower signal around 19:00 local and mostly clear conditions thereafter; no strong rain-delay expectation.
- Field-level wind from a current structured lineup-weather source: roughly **NNE 6 mph**.
- Baseball Savant rolling park factors: 2024–26 run index about **102** and HR index about **114**; 2026 single-season run index is near neutral while the HR factor remains elevated.
- Treatment: no crude “warm weather = Over” coefficient. The park mainly widens the home-run/cluster tail rather than forcing the mean upward.

#### Bullpen / rest state

- Chicago did **not** play on 17 Sep, so its relief group has at least one full calendar day of rest after the 16 Sep game.
- Cincinnati played on 17 Sep and starter Brady Singer lasted only **3.1 innings**, forcing **5.2 bullpen innings**.
- Williamson, the nominal Burns piggyback/bulk option, worked **2.0 innings on 17 Sep**. This is a direct availability/exposure concern, not merely a “tired bullpen” label.
- Julian Aguiar's same-day recall provides length but adds current-role/return uncertainty.

#### Joint run object

**Cubs run centre: ~4.8**
- blended season offense/opponent-prevention prior: `(5.34 Cubs RS/G + 5.14 Reds RA/G) / 2 ≈ 5.24`
- Burns elite short-start adjustment: **-0.55**
- post-Burns bulk/relief uncertainty (Williamson worked yesterday; Aguiar just recalled): **+0.20**
- Swanson return / current expected top-order continuity: **+0.05**
- 2026 park mean near neutral, HR tail handled as width rather than a large signed mean shift: **-0.10**
- **centre ≈ 4.84**

**Reds run centre: ~3.6**
- blended season offense/opponent-prevention prior: `(4.14 Reds RS/G + 4.41 Cubs RA/G) / 2 ≈ 4.28`
- Holmes current-quality adjustment: **-0.55**
- Chicago relief freshness: **-0.15**
- GABP HR-tail / home ninth exposure: **+0.10**
- Steer absence / thinner current offensive mix: **-0.05**
- **centre ≈ 3.63**

**Combined centre:** approximately **8.4–8.5 runs**  
**Width:** broad (~4+ runs) because Great American Ball Park preserves HR clustering and Cincinnati's post-Burns pitching chain is uncertain.

Representative central state: **Cubs 4-3 Reds**.

#### Winner / run-line geometry

- **Projected eventual winner:** Cubs **0.63**, Reds **0.37** (`UNVALIDATED_SUBJECTIVE`).
- Drive `BASE_RATES_REGISTER.md` gives the current MLB 1.5-run cushion band. The clubs' season winning-percentage separation is closest to the register's **+0.1 winner-strength bucket**, where `b_1 ≈ 0.268`.
- Coherent run-line identity:
  - `P(Cubs -1.5) = 0.63 × (1 - 0.268) ≈ 0.461`
  - `P(Reds +1.5) = 1 - 0.461 ≈ 0.539`
- This prevents the Cubs winner lean from being incorrectly translated into a strong -1.5 lean.

#### Total 8.5 query

The total line sits essentially through the centre. Burns' first-turn quality and Holmes' form push downward; Cincinnati's shortened-starter/bulk uncertainty and the HR-cluster environment push upward.

- **Under 8.5:** **0.53**
- **Over 8.5:** **0.47**
- The edge is intentionally small. This is not a strong total card.

#### Ranked picks

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Why this rank | Primary failure path |
|---:|---|---:|---|---|---|
| **1** | **Cincinnati Reds +1.5** | **0.54** | LOW-MEDIUM / participant-order cap | Cubs are the better winner call, but the derived MLB one-run cushion materially protects Cincinnati. Burns' first turn also suppresses early Cubs separation. | Burns exits early, Cincinnati's length chain fails, and Chicago creates a 2+ run gap. |
| **2** | **Combined Total UNDER 8.5** | **0.53** | LOW-MEDIUM / participant-order cap | Holmes has a strong current run outside one Miami blow-up; Burns is elite for his shortened exposure; central total is only ~8.4. | Post-Burns Cincinnati pitching unravels or GABP HR clusters create a one-sided Cubs scoring spike. |
| **3** | **Combined Total OVER 8.5** | **0.47** | LOW-MEDIUM / participant-order cap | Burns is expected to leave after ~50–55 pitches and Williamson worked 2 IP yesterday; Aguiar/bulk uncertainty gives the Cubs a real late scoring route. | Burns + Cincinnati length cover 6+ competent innings while Holmes suppresses the weaker Reds offense. |
| **4** | **Chicago Cubs -1.5** | **0.46** | LOW-MEDIUM / derived cushion geometry | Chicago has the stronger club and deeper run-production case, but -1.5 requires the Cubs winner thesis **plus** 2+ separation. | Cincinnati wins outright or loses by exactly one; the MLB one-run band is meaningful. |

**Forced-pair interpretation:** Reds +1.5 vs Cubs -1.5 is one run-line decision; Under 8.5 vs Over 8.5 is one total decision. Preferred sides are **Reds +1.5** and **Under 8.5**, both only modestly above 50%.

#### Dependence / kill paths

- Approx. `P(Rank #1 ∧ Rank #2)` ≈ **0.30**: low/medium-scoring Reds win or one-run Cubs win states.
- Main both-top-two failure state ≈ **0.20–0.22**: Cubs win by 2+ in a 9+ run game after Burns exits and Cincinnati's bulk/relief chain gives up a clustered inning.
- Representative Rank-1-compatible score: **Cubs 4-3 Reds** — Reds +1.5 wins, Under 8.5 wins, projected winner Cubs wins.
- Representative kill state: **Cubs 7-3 Reds** — Reds +1.5 and Under both fail, while Cubs winner and -1.5 succeed.

#### Potential game winner

- **Chicago Cubs — 0.63 `UNVALIDATED_SUBJECTIVE`**
- Cincinnati Reds — 0.37
- The winner lean comes from the large season run-differential gap, stronger offensive baseline, Holmes' starter edge over a limited Burns-plus-bulk structure, a rested Chicago relief group, and Cincinnati's current pitching-depth issues.
- This is **not equivalent to Cubs -1.5**.

#### Integrity / missingness flags

- `STARTING_LINEUPS_NOT_OFFICIAL_AT_FREEZE`: field-owner MLB batting-order page still showed TBD at 08:36 AEST.
- Secondary lineup feeds were consistent enough to construct a participant mixture, but no player-specific contract is ranked.
- Exact sportsbook listed-pitcher / extra-innings / suspension terms were not supplied: `UNKNOWN_DEFINITION`.
- No bookmaker odds, implied probabilities, consensus or line movement are used as forecast evidence.
- Burns' intended post-start piggyback is uncertain because Williamson pitched 2.0 innings the day before; no assumption that he will carry a normal bulk load.
- **Historical issued-card status at issue:** `UNSETTLED — PREGAME CARD; NO RETROSPECTIVE`.

#### Settlement routes pre-registered

- Result, innings, starter identity, run line and total: **MLB official Gameday / final box score**.
- Starting lineups: MLB official lineup/game record once populated.
- Run-line settlement includes extra innings under standard full-game MLB scoring unless the user's operator has different stated rules.

#### Sources

| Source | Record / URL | Contribution | Quality / limitation |
|---|---|---|---|
| MLB schedule / probable pitchers | https://www.mlb.com/schedule/2026-09-18 ; https://www.mlb.com/probable-pitchers/2026-09-18 | Exact fixture, venue, start, Holmes/Burns starter handshake | Field owner |
| MLB starting lineups | https://www.mlb.com/starting-lineups/2026-09-18 | Batting orders still TBD at pregame cutoff | Field owner; participant release lag |
| MLB game preview / story `824463` | Cubs @ Reds, 18 Sep 2026 | Burns shortened outing / piggyback plan | Field-owner preview |
| MLB Burns player page | https://www.mlb.com/player/chase-burns-695505 | 2026 workload, ERA/IP/K/WHIP, flexor-injury return context | Primary |
| Baseball Savant probable pitchers | https://baseballsavant.mlb.com/probable-pitchers | Tiny current-roster matchup samples | MLB/Statcast; descriptive only |
| MLB transactions | https://www.mlb.com/transactions | Swanson activation, Reds Steer/Garcia/Aguiar moves | Field owner |
| MLB standings | https://www.mlb.com/standings/ | 85-68 / 71-82, RS/RA, home-away, run differentials | Field owner |
| MLB / Baseball Savant park factors | https://baseballsavant.mlb.com/leaderboard/statcast-park-factors | GABP run/HR environment | Primary structured Statcast |
| Structured exact-venue weather | Great American Ball Park, 18 Sep 2026 game window | ~26°C, small shower signal | Exact-venue structured weather |
| CBS Clay Holmes game log | 2026 Holmes game log | Last five starter outcomes | Structured secondary |
| MLB Burns video / current reports | 13 Sep 2026 | Burns limited to 3 IP in prior outing | Primary + current reporting |
| MLB Brandon Williamson player page / StatMuse log | 2026 Williamson line and 17 Sep 2.0-IP outing | Post-Burns availability/quality | Primary + structured secondary |
| RotoGrinders / RotoWire / FPTrack current lineup feeds | 18 Sep 2026 | Current expected/secondary batting-order mixture | Secondary; not promoted to official |
| StatMuse current team windows | Cubs last 5, Reds last 5/10 and recent RA | Current descriptive trend context | Structured secondary |
| Drive `RULES_BASEBALL.md`, `METHOD.md`, `RULES_GENERAL.md`, `CONTROLS.md`, `BASE_RATES_REGISTER.md` | Sports Research Drive | SFA-BASEBALL, joint object, run-line cushion, ranking and missingness controls | Governing methodology |
| User-supplied slate | Current query | Exact ±1.5 and O/U 8.5 contracts | Contract source only |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| Burns limited start + nominal piggyback worked 2 IP previous day | `RULES_BASEBALL.md` bullpen/role-chain logic | Existing control correctly applied; no new rule |
| MLB lineup endpoint still TBD inside final minutes while secondary feeds were populated | `DATA_SOURCE_REGISTER.md` / `SOURCES.md` | Source-latency observation; retain official-vs-secondary status |
| Reds post-Burns depth widened by Aguiar same-day recall | `RULES_BASEBALL.md` participant/relief-chain process | Existing current-role uncertainty control |
| MLB +1.5 geometry materially differs from winner call | `BASE_RATES_REGISTER.md` / `G-L24` | Existing derived cushion identity applied |

---

---

#### Settlement and retrospective — 19 Sep 2026

**Final status:** `COMPLETED / SETTLED / RETROSPECTIVE COMPLETE`  
**Official final:** Cincinnati Reds **6**, Chicago Cubs **4** — combined **10** runs.

##### A. Prediction outcome

| Original rank | Original selection | Result | Settlement |
|---:|---|---:|---|
| 1 | Cincinnati Reds +1.5 | CIN won 6-4 | **WIN** |
| 2 | Under 8.5 | 10 runs | **LOSS** |
| 3 | Over 8.5 | 10 runs | **WIN** |
| 4 | Chicago Cubs -1.5 | CHC lost outright | **LOSS** |
| — | Projected winner: Chicago Cubs | CIN won | **LOSS** |

**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 1/2. **NDCG@2:** 1.000 under the binary top-two diagnostic.  
The forced total pair settled exactly once by construction; the meaningful totals decision was that the preferred **Under** lost.

##### B. Why each pick won or lost

**#1 Reds +1.5 — WIN.** The cushion thesis was stronger than the Cubs-winner thesis because the original model correctly separated “better team” from “wins by 2+.” Cincinnati did not need the cushion: it won outright. Burns gave the Reds the planned short start (3.0 IP, 2 ER), Julian Aguiar supplied three innings of length, and Cincinnati’s later relief group shut Chicago out after the fourth. That directly defeated the pregame kill path that Cincinnati’s post-Burns bridge would unravel.

**#2 Under 8.5 — LOSS.** The miss was driven principally by the *other* starter. Clay Holmes’ command collapsed: he was charged with all six Cincinnati runs and issued five walks. Cincinnati scored twice in the first, retook the lead in the third, then turned Holmes/Assad traffic into a three-run sixth. The pregame Under gave substantial weight to Holmes’ strong recent run outside one Miami blow-up; it did not allocate enough mass to a walk/command-driven high Cincinnati state. This was not primarily a home-run-cluster miss: Chicago’s Ian Happ hit the game’s lone home run, while Cincinnati’s scoring came through baserunners, contact, sacrifice/ground-ball sequencing and a late two-run Trevino single.

**#3 Over 8.5 — WIN.** The total reached 10 even though the exact Over mechanism forecast before the game was imperfect. The card emphasized Cincinnati’s uncertain post-Burns pitching chain as the main upside route. In reality, Burns/Aguiar plus the Reds bullpen held Chicago to four; the decisive upward shock was Holmes’ six-run concession. Therefore the Over result does **not** validate the original bullpen-unravelling thesis. It validates the need to preserve starter command tails on both sides.

**#4 Cubs -1.5 — LOSS.** The -1.5 required the Cubs winner thesis plus separation. Neither condition occurred. The model’s own MLB one-run-cushion geometry had already warned that winner and run line were different targets; ranking this last was correct.

**Projected winner Cubs — LOSS.** Chicago’s season run-differential and overall strength edge did not survive the single-game starter state. The key lesson is not to discard season strength; it is to keep a sufficiently wide starter-specific adverse branch so one strong recent run does not make a pitcher’s command failure too cheap in the distribution.

##### C. Rank-1 review

No enhanced Rank-1 failure review is triggered because **Reds +1.5 won**. The ordering of the two run-line sides was justified by the pregame margin geometry and was one of the strongest parts of the card.

##### D. Top-two review

Rank #1 won, Rank #2 lost. The relative ordering was justified: the +1.5 cushion was more robust to both the Reds-win state that occurred and a one-run Cubs-win state, whereas Under 8.5 was vulnerable to either starter producing a crooked inning. Future top-two construction should continue to prefer contracts robust across more ordinary score-allocation states.

##### E. Over/Under review

The central estimate (~8.4) sat almost directly on 8.5, so this was always a weak directional total. The result reinforces the new prospective ceiling rule:
- test **Reds ordinary-high + Cubs centre/floor**, not only a Cubs offensive spike;
- separate starter **walk/zone/command** risk from contact/HR risk;
- when the line is effectively through the centre, downgrade the preferred total unless the component branches are genuinely asymmetric.

##### F. What went right

- Burns’ shortened role and Aguiar length possibility were researched correctly.
- The model correctly refused to translate a Cubs winner lean into Cubs -1.5.
- The Reds +1.5 rank survived the eventual outright upset.
- The original card already described the total as small-edge rather than strong.

##### G. Blind spots / source audit

- **Confirmed batting orders:** not obtained from MLB before freeze; the field-owner endpoint was still TBD. Postgame lineups are available, but cannot be backdated as pregame confirmation.
- **Bench / relief availability:** materially researched, especially Burns’ short role, Williamson’s previous-day work and Aguiar’s recall; this was useful.
- **Coaching/manager context:** not a material forecast driver and no specific managerial uncertainty was identified.
- **Injuries/availability:** Swanson activation and Cincinnati roster moves were checked adequately.
- **Source quality:** MLB/Statcast/transactions were strong. The historical card also listed RotoGrinders, RotoWire and FPTrack as secondary lineup feeds. Under current v4.2 source policy these are **prohibited predictive sources** and must not be reused; the fact that the card won Rank #1 does not rehabilitate them.
- **Main analytical blind spot:** Holmes’ adverse command branch was too light relative to how close the total line was to the centre.

##### H. Validation questions

1. **Confirmed starting lineups for both teams?** No; MLB’s accessible field-owner page remained TBD before freeze.
2. **Bench/reserve/relief state obtained?** Partially and usefully; Cincinnati’s bulk/relief chain was investigated in detail.
3. **Coaching/manager information material?** No material coaching change was identified.
4. **Injuries/rest/late availability checked?** Yes for the material roster moves; exact final batting order still lagged.
5. **Were original sources accurate/current?** Core MLB sources were; prohibited secondary lineup services are now a documented historical source defect.
6. **Better sources for future?** MLB exact game feed/lineup record and club transaction pages first; no fantasy/DFS-derived lineup feed.
7. **Blind spots?** Starter walk/command tail and one-sided opponent scoring ceiling.
8. **Future treatment?** Add a recent strike/ball, BB%, zone/first-pitch-strike and velocity/command audit where available before a starter-dominant total or ML receives a top rank.

##### Settlement sources

- MLB official Gameday final box: `https://www.mlb.com/gameday/cubs-vs-reds/2026/09/18/824463/final/box`
- MLB official game story/timeline, game 824463.
- MLB final box records Burns 3.0 IP / 2 ER and the final 6-4 result; the settlement source is the field owner.

##### Event-specific learning / document mapping

| Learning | Proposed home | Status |
|---|---|---|
| Starter command failure can defeat a near-centre Under without a HR cluster | `RULES_BASEBALL.md` starter-state / total component budget | **Candidate reinforcement**, not a fitted rule |
| Historical RotoWire/RotoGrinders/FPTrack use must not recur under v4.2 | `SOURCES.md` source firewall | **Current rule already exists; historical defect recorded** |
| Winner vs -1.5 separation geometry worked | `RULES_BASEBALL.md` / `BASE_RATES_REGISTER.md` | Existing control validated descriptively |

---

### P-464 — Baseball / MLB — Milwaukee Brewers @ Baltimore Orioles

- **Canonical ID:** P-464 (fresh pre-issue reconciliation against `PREDICTION_LOG_COMBINED_4.md` found no P-464 collision)
- **Sport / competition:** Baseball — Major League Baseball, 2026 regular season
- **Event:** Milwaukee Brewers @ Baltimore Orioles
- **Venue:** Oriole Park at Camden Yards, Baltimore, Maryland
- **Scheduled start:** 18 Sep 2026, 19:05 EDT = **19 Sep 2026, 09:05 AEST**
- **Game state at issue:** `PREGAME / SCHEDULED` at final volatile refresh; no post-first-pitch information is used.
- **Research cutoff / final volatile refresh:** **19 Sep 2026, 09:01:25 AEST / 18 Sep 2026, 19:01:25 EDT**
- **Method version:** MDS-2026.09.06-v4.0 / SFA-BASEBALL
- **Population status:** MLB = `PRIMARY_SCORED`; this mini-log remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**
- **Operating mode:** `SPORTS_ONLY / MARKET_BLIND`
- **User-supplied contracts:** Brewers ML; Orioles +1.5; Combined Total Over 8.5; Combined Total Under 8.5
- **At issue:** no retrospective was performed.

#### Identity / starter handshake

**Milwaukee — Dustin May, RHP**
- MLB probable-pitcher record: **7-9, 4.49 ERA, 133 SO**.
- Recent starts recovered:
  - 11 Sep vs CIN: **6.0 IP, 2 H, 0 ER, 1 BB, 6 K**
  - 5 Sep @ CIN: **3.2 IP, 5 H, 2 ER, 0 BB, 5 K**
  - 30 Aug vs TEX: **4.1 IP, 6 H, 4 ER, 3 BB, 4 K**
  - 19 Aug vs SEA: **2.0 IP, 7 H, 7 ER, 2 BB**
  - 12 Aug @ SDP: **7.0 IP, 4 H, 1 ER, 2 BB, 6 K**
- Interpretation: current form is genuinely volatile; the latest outing was strong but does not erase the recent contact/sequencing tail.

**Baltimore — Cade Povich, LHP**
- Baltimore officially **recalled Povich on 18 Sep**; current club reporting announced him as the starter and MASN's game-day lineup post lists him as Baltimore's starting pitcher.
- 2026 MLB line entering this start: approximately **2-1, 4.05 ERA, 1.44 WHIP, 25 K, 13 BB in 33.1 IP**.
- Triple-A 2026 ERA approximately **6.28**; recent minor-league line includes **8 ER in 5 IP on 5 Sep** and **3 ER in 6 IP on 11 Sep**.
- Under `RULES_BASEBALL.md`, Povich is treated as a **small-sample/recall mixture** rather than allowing the MLB 4.05 ERA alone to collapse the uncertainty.

#### Confirmed / current lineups and availability

**Baltimore starting lineup (MASN game-day post):**
1. Dylan Beavers — LF  
2. Pete Alonso — 1B  
3. Gunnar Henderson — SS  
4. Coby Mayo — 3B  
5. Samuel Basallo — C  
6. Christian Encarnacion-Strand — DH  
7. Colton Cowser — CF  
8. Jeremiah Jackson — 2B  
9. Leody Taveras — RF  
SP Cade Povich — LHP

- Beavers returns after leaving Wednesday with **neck stiffness**.
- **Jackson Holliday** remains on the IL with left-wrist inflammation.
- **Kyle Bradish** is on the IL with lower-abdominal discomfort.
- **Luis Robert Jr.**, **Blaze Alexander**, **Christian Franklin** and **Ryan Mountcastle** are unavailable on current IL listings.
- **Félix Bautista** and **Ryan Helsley** are not active despite rehab progress.

**Milwaukee current starting lineup:**
1. Jackson Chourio — LF  
2. Brice Turang — 2B  
3. William Contreras — C  
4. Andrew Vaughn — 1B  
5. Christian Yelich — DH  
6. Joey Ortiz — 3B  
7. Garrett Mitchell — CF  
8. Luis Lara — RF  
9. Cooper Pratt — SS  
SP Dustin May — RHP

- **Jake Bauers** sits again.
- **Grant Anderson** is on the IL with right-biceps inflammation.
- **Brandon Woodruff** and **Quinn Priester** are unavailable for this series.
- Milwaukee recalled **LHP Colton Gordon** on 18 Sep and optioned Garrett Stallings.

#### Team-strength / current-regime baseline

**Milwaukee**
- Record: **95-58 (.621)**
- Runs scored / allowed: **792 / 595**
- Run differential: **+197**
- Away: **43-32**
- Against left-handed starters: **33-14**
- Season scoring: ~**5.18 runs/game**
- Season prevention: ~**3.89 runs/game**

**Baltimore**
- Record: **75-78 (.490)**
- Runs scored / allowed: **688 / 714**
- Run differential: **-26**
- Home: **36-39**
- Season scoring: ~**4.50 runs/game**
- Season prevention: ~**4.67 runs/game**

Recent-run windows are descriptive only: Milwaukee's current scoring has been stronger than Baltimore's, but no streak receives a free directional coefficient.

#### Bullpen / workload state

**Milwaukee**
- Played 17 Sep at Pittsburgh and starter Kyle Harrison lasted only **1.2 innings**, requiring **6.1 relief innings**.
- Chad Patrick 1.1 IP; JoJo Romero 1.0; Garrett Stallings 3.0; Aaron Ashby 1.0.
- Stallings was subsequently optioned.
- High-leverage arms **Abner Uribe and Trevor Megill did not pitch on 17 Sep** and have a day of rest after working on 16 Sep.
- Treatment: middle/length flexibility is somewhat constrained, but Milwaukee's primary late-leverage chain remains usable.

**Baltimore**
- Off day on 17 Sep after playing on 16 Sep.
- Bullpen is materially **better rested** than Milwaukee's.
- This is a real late-game Baltimore offset to Milwaukee's stronger overall team profile.

#### Park / weather

- Oriole Park exact-game-window conditions: approximately **27°C / 80°F** around first pitch, dry, partly cloudy, very low precipitation risk.
- Wind approximately **N 8-9 mph**, with current game-day reporting indicating it is generally **in from left field**.
- Baseball Savant multi-year Camden factors are mildly hitter-friendly overall (around **103**), with a stronger left-handed HR factor in the recent rolling sample.
- Treatment: warm conditions and park shape preserve a HR/cluster tail, while wind in from left is a mild opposing mechanism. No automatic weather-Over adjustment.

#### Joint run object

**Milwaukee run centre: ~5.1**
- blended season offense/opponent prevention prior:
  `(5.18 MIL RS/G + 4.67 BAL RA/G) / 2 ≈ 4.93`
- Povich recall/small-sample + AAA instability: **+0.20**
- Milwaukee 33-14 vs left-handed starters / current right-handed core: **+0.10**
- Camden mild hitter environment: **+0.05**
- Baltimore rested bullpen + wind-in drag: **-0.15**
- **centre ≈ 5.13**

**Baltimore run centre: ~4.2**
- blended season offense/opponent prevention prior:
  `(4.50 BAL RS/G + 3.89 MIL RA/G) / 2 ≈ 4.20`
- May current-volatility/contact tail: **+0.10**
- Milwaukee middle-relief workload constraint: **+0.05**
- usable Uribe/Megill late chain: **-0.10**
- lineup absences + wind-in drag: **-0.05**
- **centre ≈ 4.20**

**Combined centre:** approximately **9.3 runs**  
**Width:** broad because May carries meaningful bad-start/contact tail and Povich is a recall/small-sample starter.

Representative central score: **Brewers 5-4 Orioles**.

#### Winner / run-line geometry

- **Projected eventual winner:** Brewers **0.62**, Orioles **0.38** (`UNVALIDATED_SUBJECTIVE`).
- The current MLB 1.5-run cushion identity from `BASE_RATES_REGISTER.md` uses a winner-strength gap closest to the **+0.1 bucket**, `b1 ≈ 0.268`.
- Coherent derived geometry:
  - `P(Brewers -1.5) = 0.62 × (1 - 0.268) ≈ 0.454`
  - `P(Orioles +1.5) = 1 - 0.454 ≈ 0.546`
- Therefore Baltimore +1.5 can rank below Brewers ML while remaining more likely than a Milwaukee 2+ run win.

#### Total 8.5 query

- **Over 8.5: 0.58**
- **Under 8.5: 0.42**

The total leans Over because:
- Povich's current role is a small-sample recall with weak Triple-A context;
- Milwaukee has been very strong against left-handed starters;
- May's run distribution remains wide despite the latest strong outing;
- Camden preserves HR/cluster upside.

Counterweights:
- Baltimore's bullpen is fully rested;
- Milwaukee's primary late leverage remains usable;
- wind is modestly in from left.

#### Ranked picks

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Why this rank | Primary failure path |
|---:|---|---:|---|---|---|
| **1** | **Milwaukee Brewers ML** | **0.62** | MEDIUM | Much stronger full-season run differential, elite 33-14 record vs lefty starters, Povich recall/small-sample uncertainty, and stronger overall roster quality. | May's bad-contact tail appears and Baltimore's rested bullpen protects a lead. |
| **2** | **Combined Total OVER 8.5** | **0.58** | MEDIUM | Combined centre ~9.3; Povich/AAA instability and May volatility create multiple 9+ run branches. | Povich gives Baltimore 5+ competent innings, May suppresses BAL, and rested Orioles relief keeps Milwaukee near 4-5. |
| **3** | **Baltimore Orioles +1.5** | **0.55** | MEDIUM | Derived from the same 0.62 Brewers winner tree using the current MLB one-run cushion band; every Baltimore win plus one-run Milwaukee wins cash this contract. | Milwaukee converts its roster/start matchup edge into 2+ separation. |
| **4** | **Combined Total UNDER 8.5** | **0.42** | MEDIUM-LOW | Rested Baltimore bullpen, usable Milwaukee leverage arms and mild wind-in effect preserve a meaningful lower-total state. | Either starter exits early or a HR/cluster inning pushes the game beyond 8.5. |

#### Dependence / kill paths

- Approx. `P(Rank #1 ∧ Rank #2)` ≈ **0.38**: Milwaukee wins in an ordinary/high scoring state.
- Rank #3 is partly diversifying against a narrow Milwaukee win: `P(Brewers ML ∧ Orioles +1.5)` is approximately the Milwaukee exactly-one-run branch, around **0.17** under the derived cushion geometry.
- Main both-top-two failure state ≈ **0.17-0.18**: Baltimore wins a lower-scoring game through May suppression failure + rested relief.
- Representative state: **MIL 5-4 BAL** — Brewers ML, Over 8.5 and Orioles +1.5 all win.
- Main separation kill state: **MIL 6-3 BAL** — Brewers ML and Over win, Orioles +1.5 loses.
- Main total kill state: **MIL 4-2 BAL** — Brewers ML wins but Over loses.

#### Potential game winner

- **Milwaukee Brewers — 0.62 `UNVALIDATED_SUBJECTIVE`**
- Baltimore Orioles — 0.38
- Winner endpoint: eventual MLB result including extra innings.
- Winner lean is driven by Milwaukee's +197 differential, stronger run production/prevention, excellent record vs LHP and Povich uncertainty, partially offset by Baltimore's bullpen-rest advantage and May's volatile current regime.

#### Integrity / missingness

- Povich confirmation required combining official roster transaction + current club/game-day reporting because MLB's generic starter/lineup endpoint lagged near first pitch.
- No bookmaker odds, market movement or consensus used.
- Exact operator listed-pitcher/suspension terms not supplied: `UNKNOWN_DEFINITION`.
- No retrospective performed.
- **Historical issued-card status at issue:** `UNSETTLED — PREGAME CARD`.

#### Settlement routes pre-registered

- Result, starter identity, total and ML: **MLB official Gameday / final box score**.
- Run-line derivation/settlement: same MLB final score, extra innings included unless operator-specific terms differ.
- Starting lineup record: MLB/MASN current game-day participant record.

#### Sources

| Source | Contribution | Quality / limitation |
|---|---|---|
| MLB probable pitchers / Brewers probable pitcher page | Dustin May official/probable starter, current season line | Field owner |
| Baltimore Orioles official transactions | Cade Povich recall, Codi Heuer option | Field owner |
| MASN game-day lineup article | Exact Orioles lineup, Povich starter, Brewers lineup, Beavers availability | High-quality club broadcaster/current |
| RotoWire Povich update | Club announced Povich as Friday starter; Triple-A ERA context | Current secondary |
| CBS Sports Povich game log | MLB start-by-start results | Structured secondary |
| Baseball Savant minor-league game log | Povich AAA recent workload/results | MLB/Statcast structured |
| MLB standings | Team records, RS/RA, run differential, splits | Field owner |
| MLB/Brewers transactions | Colton Gordon recall / Stallings option; active roster changes | Field owner |
| Brewers previous-game official/structured record | Sep17 bullpen workload | Primary/structured |
| NWS Baltimore hourly forecast | Exact game-window temperature, wind, precipitation | Government weather |
| Baseball Savant park factors | Camden rolling run/HR environment | Primary structured |
| Reuters / current May reporting | May's most recent shutout start | High-quality secondary |
| CBS May game log | May recent-start sequence | Structured secondary |
| StatMuse team windows | Current L5/L10 descriptive run windows | Structured secondary |
| Drive `RULES_BASEBALL.md`, `METHOD.md`, `BASE_RATES_REGISTER.md` | Governing starter, bullpen, run-line and probability rules | Governing methodology |
| User-supplied slate | Brewers ML, BAL +1.5, O/U 8.5 | Contract source only |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| Povich official transaction + current club reporting outran generic MLB probable endpoint | `SOURCES.md` / `DATA_SOURCE_REGISTER.md` | Source-latency observation only |
| Brewers middle-relief workload but rested leverage arms | `RULES_BASEBALL.md` relief-chain logic | Existing “freshness is not quality / name the chain” control applied |
| Povich small MLB sample conflicts with weak AAA results | `RULES_BASEBALL.md` small-sample starter mixture | Existing control applied |
| Brewers ML can rank above BAL +1.5 while MIL -1.5 would remain below both | `BASE_RATES_REGISTER.md` / `G-L24` | Existing coherent margin identity applied |

---

---

#### Settlement and retrospective — 19 Sep 2026

**Final status:** `COMPLETED / SETTLED / RETROSPECTIVE COMPLETE`  
**Official final:** Milwaukee Brewers **6**, Baltimore Orioles **5** in **10 innings** — combined **11** runs.

##### A. Prediction outcome

| Original rank | Original selection | Result | Settlement |
|---:|---|---:|---|
| 1 | Milwaukee Brewers ML | MIL won 6-5 | **WIN** |
| 2 | Over 8.5 | 11 runs | **WIN** |
| 3 | Baltimore Orioles +1.5 | BAL lost by 1 | **WIN** |
| 4 | Under 8.5 | 11 runs | **LOSS** |
| — | Projected winner: Milwaukee | MIL won | **WIN** |

**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 2/2. **NDCG@2:** 1.000.

##### B. Why each pick won or lost

**#1 Brewers ML — WIN.** Milwaukee’s stronger full-game club profile and deeper late-game routes survived a game that was tied twice. The Brewers created a 3-0 lead on Jackson Chourio’s three-run homer, regained a two-run lead in the ninth through William Contreras and Christian Yelich, and then won in the 10th on Sal Frelick’s RBI single.

**#2 Over 8.5 — WIN.** The game produced exactly the sort of multi-route scoring distribution the card needed: early three-run homers on both sides, late bullpen scoring, then an extra-inning run. Dustin May and Cade Povich both carried genuine volatility in the original analysis, and neither side required one isolated freak inning to create the Over.

**#3 Orioles +1.5 — WIN.** Baltimore lost by exactly one, so the cushion did its job. The 10th-inning endpoint also illustrates why a favourite ML and opponent +1.5 can both win: those contracts are overlapping, not contradictory.

**#4 Under 8.5 — LOSS.** It was the forced-pair non-preferred side and failed as the distribution intended.

**Projected winner Milwaukee — WIN.** The winner call survived Baltimore’s ninth-inning comeback and extra innings, which is important because the card modelled the full-game endpoint rather than treating nine innings as guaranteed.

##### C. Rank-1 review

No enhanced failure review: Rank #1 won.

##### D. Top-two review

Both top selections won. Their ordering was defensible: Milwaukee ML depended on winner sign, while Over 8.5 had wider game-state support but also more sensitivity to starter and bullpen execution. The result should not be interpreted as two independent confirmations because both benefited from Milwaukee continuing to score late.

##### E. Over/Under review

The Over mechanism was strong:
- Chourio 3-run HR off Povich;
- Pete Alonso 3-run HR off May;
- Milwaukee scored twice in the ninth;
- Baltimore tied it with two ninth-inning sacrifice flies;
- Frelick drove in the automatic runner in the 10th.

Extra innings contributed only one additional run, so the game had already reached 10 through nine. The Over did not depend solely on the automatic-runner rule.

##### F. What went right

- Povich’s recall/small-sample uncertainty was appropriately preserved.
- May’s current-start volatility was not erased by one good outing.
- Full-game extras were included in endpoint logic.
- The model correctly allowed **Brewers ML + Orioles +1.5** to coexist.
- The representative close, high-scoring Milwaukee-win geometry was directionally excellent.

##### G. Blind spots / source audit

- **Confirmed lineups:** yes to a much better standard than P-463; MASN/current club reporting identified Povich and both orders.
- **Bench/relief state:** adequately researched for the full-game contracts.
- **Coaching:** no material coaching uncertainty.
- **Availability:** Povich recall and current player availability were captured.
- **Sources:** MLB field-owner result/timeline and MASN participant reporting were strong.
- **Residual blind spot:** dependence. Three winning ranked rows should not be treated as three independent predictive successes because ML/+1.5 overlap structurally and the Over shared late-game scoring drivers.

##### H. Validation questions

1. Confirmed lineups? **Yes / strong current game-day support**, with Baltimore particularly well grounded.
2. Bench/reserves? **Adequate for team-level contracts**, though not every unused bench player was prediction-critical.
3. Coaching information? **No material unresolved change.**
4. Injuries/rest/availability? **Yes**, including Povich recall/current role.
5. Source accuracy/currentness? **Strong.**
6. Better future sources? Continue MLB exact game feed + club broadcaster/official team where generic MLB lineup endpoint lags.
7. Blind spots? Mainly **correlated-contract accounting**, not a missed game mechanism.
8. Future treatment? Keep explicit joint probabilities and avoid presenting ML/+1.5/Over simultaneous hits as independent evidence.

##### Settlement sources

- MLB official game story/timeline: `https://www.mlb.com/stories/game/824790`
- MLB official final scoreboard, 18 Sep 2026.
- MLB game report: Brewers 6, Orioles 5 in 10 innings.

##### Event-specific learning / document mapping

| Learning | Proposed home | Status |
|---|---|---|
| ML and opponent +1.5 overlap naturally in one-run favourite wins | `RULES_GENERAL.md` / `RULES_BASEBALL.md` dependence section | Existing control confirmed |
| Extra innings must remain an explicit endpoint transition | `RULES_BASEBALL.md` / `BASE_RATES_REGISTER.md` | Existing control confirmed |
| Do not count correlated row wins as independent model evidence | `SCORING_AND_VALIDATION.md` / `RULES_GENERAL.md` | Existing principle reinforced |

---

### P-465 — Basketball / WNBA — Indiana Fever @ Toronto Tempo

- **Canonical ID:** P-465 (fresh pre-issue reconciliation against `PREDICTION_LOG_COMBINED_4.md` found no P-465 collision)
- **Sport / competition:** Basketball — WNBA, 2026 regular season
- **Event:** Indiana Fever @ Toronto Tempo
- **Venue:** Coca-Cola Coliseum, Toronto, Ontario
- **Scheduled start:** 18 Sep 2026, 19:30 ET = **19 Sep 2026, 09:30 AEST**
- **Game state at issue:** `PREGAME / SCHEDULED`; official WNBA game page still showed the 7:30 PM ET scheduled start and no live score at the final refresh.
- **Research cutoff / final volatile refresh:** **19 Sep 2026, 09:19:49 AEST / 18 Sep 2026, 19:19:49 ET**
- **Method version:** MDS-2026.09.06-v4.0 / SFA-BASKETBALL
- **Population status:** EXPLORATORY — NOT SCORED; mini-log remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE
- **Operating mode:** SPORTS_ONLY / MARKET_BLIND
- **User-supplied contracts:** Fever -15.5; Tempo +15.5; Total Over 187.5; Total Under 187.5
- **Model-selected additional contract:** Fever moneyline / eventual winner
- **At issue:** no retrospective was performed.

#### Participant / coach / rotation state

**Indiana**
- Head coach: **Stephanie White**.
- Caitlin Clark: **Probable (back)**. She has not missed a game since July 5 and returned from Team USA's World Cup gold-medal run with Aliyah Boston.
- Damiris Dantas: **out for season** after left-knee meniscus surgery.
- Projected starting five from current preview sources: **Caitlin Clark, Kelsey Mitchell, Lexie Hull, Aliyah Boston, Makayla Timpson**.
- Current official roster also includes Sophie Cunningham, Myisha Hines-Allen, Raven Johnson, Mercedes Russell, Grace VanSlooten, Michelle Onyiah, Bree Hall, Monique Billings and Tyasha Harris.
- Rotation signal: Indiana is healthy relative to Toronto, but Clark/Boston are returning from international travel; a large lead creates a real fourth-quarter starter-minute compression branch.

**Toronto**
- Head coach: **Sandy Brondello**.
- **OUT:** Marina Mabrey (right adductor; season-ending final stretch), Brittney Sykes (foot; season), Aneesah Morrow (knee; season).
- **Maria Conde: Questionable (illness)** after missing recent time.
- **Nyara Sabally** and **Julie Allemand** are available/expected back after prior absence/World Cup duty.
- Toronto converted hardship/development players **Ornella Bankole and Zaay Green** to regular contracts.
- Projected starting five from current preview sources: **Kiki Rice, Julie Allemand, Laura Juskaite, Isabelle Harrison, Temi Fagbenle**.
- Active-role mixture also includes Sabally, Kia Nurse, Teonni Key, Bankole, Green and potentially Conde.
- Rotation signal: Toronto has more bodies than in its most depleted August games, but its three major season-ending absences remove large creation, scoring, perimeter-defence and rebounding shares.

**Lineup integrity flag:** exact official starting fives were not published in the retrieved field-owner game page by the final pre-tip refresh. `STARTING_FIVES_NOT_OFFICIALLY_CONFIRMED_AT_FREEZE` applies. Full current rosters/coaches and injury states were retrieved, so the model uses explicit lineup/minutes mixtures rather than asserting the projected fives as official.

#### Team baseline / possession profile

**Indiana season**
- Record: **26-14**
- Scoring: **97.0 PPG**
- Opponent scoring: **91.0 PPG**
- Pace: about **81.2**
- Offensive rating: about **117.9**
- Defensive rating: about **110.5**
- Net rating: about **+7.4**
- Recent L5: **102.4 PPG**, with scores 101, 85, 102, 113, 111.
- Recent L10: approximately **97-101 PPG** across current StatMuse snapshots; source snapshots differ slightly by crawl date.
- Recent L15/L20 remain strong; latest retrieved L20 snapshot: **14-6, 99.3 PPG**.

**Toronto season**
- Record: **11-29**
- Scoring: **86.2 PPG**
- Opponent scoring: **93.8 PPG**
- Pace: about **79.4**
- Offensive rating: about **108.2**
- Defensive rating: about **117.7**
- Net rating: about **-9.5**
- Recent L5 actual sequence: **82, 78, 78, 73, 69 = 76.0 PPG**, while allowing **90.2 PPG**.
- Recent L10: **82.3 PPG**, opponents about **94.3 PPG**.
- Recent L15 retrieved snapshot: roughly **82.9-84.1 PPG**, with pace about **79.65**.
- Recent L20: **5-15, 86.9 PPG**.

These windows are diagnostic. The raw losing/scoring streak is not itself a signed coefficient. The current participant mechanism matters: Mabrey/Sykes/Morrow are out, while Sabally/Allemand returning partially repairs Toronto's floor.

#### Head-to-head continuity

Indiana leads the 2026 series **2-0**:
- 16 Jun: Indiana **113-91** Toronto — 204 total, Fever +22.
- 18 Aug: Indiana **101-95** Toronto — 196 total, Fever +6.

Both previous games cleared 187.5, but continuity is materially broken for Toronto because Mabrey, Sykes and Morrow were major current-regime contributors and are now unavailable. H2H is therefore retained as a ceiling comparator, not a direct total-rate coefficient.

#### Current-depleted Toronto regime

After Toronto lost the Mabrey/Sykes/Morrow combination, its final four games before the World Cup break were:
- 78-88 vs Las Vegas
- 78-90 at Seattle
- 73-93 at Las Vegas
- 69-101 at Phoenix

Toronto averaged **74.5 points** and those four games averaged **167.5 total points**. This is not copied forward mechanically because Sabally and Allemand return tonight, but it establishes a genuine low Toronto scoring-floor branch.

#### Possession / score budget

**Central possessions:** approximately **80.0**.

**Indiana team-score centre: ~100**
- season matchup baseline from Indiana scoring / Toronto prevention: `(97.0 + 93.8) / 2 = 95.4`
- Toronto missing Sykes/Morrow/Mabrey defensive/rebounding/rotation impact: **+2.0**
- Indiana elite current offensive ceiling / top creator availability: **+2.0**
- Clark/Boston return continuity: **+1.0**
- Toronto home court + possible blowout minute compression: **-0.5**
- **centre ≈ 99.9**

**Toronto team-score centre: ~84**
- season matchup baseline: `(86.2 + 91.0) / 2 = 88.6`
- current loss of Mabrey/Sykes/Morrow creation/scoring/rebounding: **-7.5**
- Sabally + Allemand return: **+3.0**
- Conde-questionable mixture: **-0.8**
- home / bench-garbage-time floor: **+0.7**
- **centre ≈ 84.0**

**Combined centre:** ~**184 points**  
**Central margin:** Indiana by ~**16 points**, with wide spread tails because 15.5 is an extreme line and fourth-quarter rotations matter.

#### Joint game-state tree (`UNVALIDATED_SUBJECTIVE`)

| State | Mass | Representative score | Contract implications |
|---|---:|---|---|
| Indiana control + Toronto suppression | **0.33** | IND 100-76 TOR | Fever ML; Fever -15.5; Under |
| Indiana control + Toronto respectable scoring | **0.24** | IND 104-86 TOR | Fever ML; Fever -15.5; Over |
| Indiana win + fourth-quarter compression | **0.24** | IND 97-85 TOR | Fever ML; Tempo +15.5; Under |
| Open/competitive Indiana win | **0.10** | IND 103-95 TOR | Fever ML; Tempo +15.5; Over |
| Toronto upset/chaos — lower total | **0.06** | TOR 92-89 IND | Tempo +15.5; Under |
| Toronto upset/chaos — higher total | **0.03** | TOR 99-96 IND | Tempo +15.5; Over |
| **Total** | **1.00** | — | — |

Derived exact-contract marginals:
- **Fever ML: 0.91**
- **Under 187.5: 0.63**
- **Fever -15.5: 0.57**
- **Tempo +15.5: 0.43**
- **Over 187.5: 0.37**

`BASKETBALL_15.5_MARGIN_BAND_NOT_DERIVED`: the Drive base-rate register has no WNBA 15.5-point cushion identity. Spread probabilities above are therefore event-tree estimates, not a league-wide historical identity.

#### Ranked best four

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Why | Primary failure path |
|---:|---|---:|---|---|---|
| **1** | **Indiana Fever ML** | **0.91** | MEDIUM-HIGH | Indiana owns the major team-quality, offensive-efficiency and current-player-availability advantage; Toronto is missing three high-impact contributors. | Clark is materially limited, Toronto's returners immediately restore creation, and Indiana shoots poorly / turns it over. |
| **2** | **Combined Total UNDER 187.5** | **0.63** | MEDIUM | Team-score centre ~184; Toronto's current roster has a materially lower scoring floor than the earlier H2Hs, and blowout compression can reduce late Indiana starter minutes. | Toronto returners lift the offense into the high 80s/90s while Indiana's elite offense scores 100+ efficiently. |
| **3** | **Indiana Fever -15.5** | **0.57** | MEDIUM-LOW / `BASKETBALL_15.5_MARGIN_BAND_NOT_DERIVED` | Toronto's current roster mismatch supports a real 20+ point branch; Indiana's offence and depth are much stronger. | Toronto keeps the game within 10-15, or Indiana leads big but late bench minutes compress the final margin. |
| **4** | **Toronto Tempo +15.5** | **0.43** | MEDIUM-LOW / forced-pair complement | Every Toronto win plus all Indiana wins by 15 or fewer cash; home court and returning Sabally/Allemand make this branch non-trivial. | Toronto's depleted creation cannot sustain scoring and Indiana maintains separation through the bench phase. |

**Supplied contract outside the top four:** **Over 187.5 = 0.37**.

#### Top-two dependence / kill paths

- Approx. `P(Rank #1 ∧ Rank #2)` = **0.57** (all Indiana-win Under states: 0.33 + 0.24).
- Approx. `P(neither Rank #1 nor Rank #2)` = **0.03** (Toronto upset + high total).
- Rank #1 and #2 are positively related through the Indiana-control/Toronto-suppression state but are not duplicates.
- Main Under kill path: Toronto returns enough shot creation to score ~88-95 while Indiana reaches 100+.
- Main Fever -15.5 kill path: fourth-quarter rotation compression after Indiana establishes a double-digit lead.

#### Potential game winner

- **Indiana Fever — 0.91 `UNVALIDATED_SUBJECTIVE`**
- Toronto Tempo — 0.09
- Endpoint: eventual WNBA winner including overtime.
- Winner is much stronger than the -15.5 spread because a 1-15 point Indiana win still wins the ML contract.

#### Integrity / missingness flags

- Official WNBA game page remained pregame at final refresh.
- Caitlin Clark remained listed **Probable**, not newly confirmed out/limited.
- Maria Conde remained **Questionable** at the final retrieved status.
- Exact official starting fives were not surfaced before the issue cutoff; projected starters are not relabelled as official.
- Full current rosters and coaches were retrieved from WNBA team pages; Toronto's hardship additions were verified through current Sportsnet reporting.
- Exact operator OT/abandonment terms were not supplied. Research-grade full-game interpretation includes overtime for winner/spread/total unless operator rules differ.
- No odds, line movement, consensus or tipster forecast entered the model.
- **Historical issued-card status at issue:** `UNSETTLED — PREGAME; NO RETROSPECTIVE`.

#### Settlement routes pre-registered

- Result, quarter scores, final total and margin: **WNBA official exact-game box score / game summary**.
- Injury/active state: official team/WNBA injury updates where exposed.
- Operator action on unusual suspension/abandonment: `UNKNOWN_DEFINITION` until operator terms are supplied.

#### Sources

| Source | Contribution | Quality / limitation |
|---|---|---|
| WNBA exact game page `1022600306` | Exact event/start/current pregame state | Field owner |
| WNBA Indiana team/roster pages | Official roster, coach, season team profile | Field owner |
| WNBA Toronto team/roster pages | Official roster, coach, season team profile | Field owner |
| Sportsnet, 18 Sep 2026 | Toronto hardship contracts; Sykes/Morrow/Mabrey out; Conde questionable | High-quality current Canadian source |
| Current injury-report reporting / Fever status | Clark probable; Dantas out; Conde questionable | Current secondary relay of team designations |
| StatMuse WNBA team windows | L5/L10/L15/L20 scoring, pace and game logs | Structured secondary; snapshot timing disclosed |
| WNBA official / structured H2H records | 113-91 and 101-95 prior 2026 meetings | Primary/structured |
| WNBA World Cup release | Clark, Boston, Conde, Sabally, Allemand international participation | Field owner |
| Drive `RULES_BASKETBALL.md` | Possession/efficiency, minutes, blowout, large-spread and total-budget controls | Governing methodology |
| Drive `METHOD.md`, `RULES_GENERAL.md`, `CONTROLS.md` | v4.0, joint-event, ranking, missingness and final-refresh requirements | Governing methodology |
| Drive `BASE_RATES_REGISTER.md` | Confirms basketball 15.5 margin band is not derived | Governing quantitative register |
| User-supplied slate | Exact ±15.5 and O/U 187.5 contracts | Contract source only |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| Toronto current three-player absence materially breaks earlier H2H continuity | `RULES_BASKETBALL.md` roster-regime control | Existing control applied |
| Large spread and Under can coexist via Toronto scoring suppression | `RULES_BASKETBALL.md` mismatch total/margin state tree | Existing control applied |
| Sabally/Allemand returns partially reverse the depleted scoring floor | `RULES_BASKETBALL.md` replacement-minutes process | Existing mixture logic |
| WNBA 15.5-point cushion identity absent | `BASE_RATES_REGISTER.md` | DATA GAP; no guessed league band |

---

---

#### Settlement and retrospective — 19 Sep 2026

**Final status:** `COMPLETED / SETTLED / RETROSPECTIVE COMPLETE`  
**Official final:** Indiana Fever **103**, Toronto Tempo **85** — combined **188**, margin **18**.

##### A. Prediction outcome

| Original rank | Original selection | Result | Settlement |
|---:|---|---:|---|
| 1 | Indiana Fever ML | IND won | **WIN** |
| 2 | Under 187.5 | 188 points | **LOSS by 0.5** |
| 3 | Indiana -15.5 | IND won by 18 | **WIN** |
| 4 | Toronto +15.5 | TOR lost by 18 | **LOSS** |
| — | Projected winner: Indiana | IND won | **WIN** |

**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 1/2. **NDCG@2:** 1.000.

##### B. Why each pick won or lost

**#1 Indiana ML — WIN.** The major talent/availability gap was real. Indiana ultimately won by 18 and pulled away 24-12 in the fourth quarter. Kelsey Mitchell scored 33 and Caitlin Clark added 28 points with 14 assists, giving Indiana the elite primary-creation advantage anticipated pregame.

**#2 Under 187.5 — LOSS by 0.5.** This is the most important retrospective point. Toronto scored 85 — not an extreme offensive outlier — while Indiana reached 103. The Under therefore failed through an **Indiana offensive-high + Toronto ordinary** state, not because both teams produced an exceptional shootout. Mitchell hit seven threes; Clark generated both scoring and elite playmaking. The pregame card explicitly listed “Indiana scores 100+ while Toronto reaches the high-80s” as a kill path, but the scenario received too little mass for a line this close to the central range.

**#3 Indiana -15.5 — WIN.** The separation thesis was correct. Toronto remained competitive into the third quarter but Indiana finished on a major late run, converting the talent gap into an 18-point final margin.

**#4 Toronto +15.5 — LOSS.** The same late separation killed the cushion. Toronto’s 31-point second quarter and brief third-quarter lead kept this live for much of the game, but the closing-depth/shotmaking gap was decisive.

**Projected winner Indiana — WIN.**

##### C. Rank-1 review

No Rank-1 failure review is required. Indiana ML was correctly made the most robust selection.

##### D. Top-two review

Rank #1 won, Rank #2 lost. The order was correct: ML had far more support across scoring states than a total sitting near its threshold. Future top-two construction should continue to demote totals whose central corridor materially straddles the line.

##### E. Over/Under review

The Under missed by the minimum half point, but that does not make the process automatically good. The relevant question is whether 103 from Indiana was an ordinary supported state. It was. Indiana had elite creators available, and Mitchell’s season-long scoring form made a 100+ team outcome plausible. The postgame result therefore validates the **prospective ceiling-floor audit** introduced after P-469:
- favourite ordinary-high + opponent centre must be tested;
- blowout/late compression cannot be assumed to suppress the favourite enough;
- a close threshold should be labelled weak even if one side computes slightly above 50%.

##### F. What went right

- Winner and separation hierarchy was strong.
- Toronto’s depleted roster and lower late-game resilience were correctly identified.
- The margin distribution preserved a real 20+ branch.
- Rank #1 was robust even though the preferred total failed.

##### G. Blind spots / source audit

- **Confirmed starting fives:** no; exact official starting fives were not surfaced before freeze.
- **Bench/rotation:** current rosters/coaches and key absences were researched, but exact five-man rotation deployment was uncertain.
- **Coaching:** Stephanie White and Sandy Brondello were identified.
- **Availability:** major absences were checked; Toronto was without key offensive players including Brittney Sykes and Marina Mabrey in the final reporting.
- **Sources:** WNBA official recap/result is strong. Some pregame projected-five material was secondary and correctly flagged as not official.
- **Blind spot:** Indiana’s offensive ceiling was too compressed relative to the total line.

##### H. Validation questions

1. Confirmed starting fives? **No.**
2. Bench/reserve/rotation lineups? **Partial; roster and projected rotation, not complete confirmed deployment.**
3. Coaching information? **Yes.**
4. Injuries/rest/late withdrawals? **Material absences checked, but exact official five still absent.**
5. Original sources sufficiently current? **Mostly, with lineup-confirmation limitation already disclosed.**
6. Better sources? WNBA official gamebook/injury report as close to tip as available; team beat reporting only as secondary role context.
7. Blind spots? **Favourite offensive-high + opponent-centre total state.**
8. Future treatment? Apply the new team-specific floor/centre/ordinary-high grid before ranking any basketball total.

##### Settlement sources

- WNBA official recap: `https://www.wnba.com/watch/video/game-recap-indiana-fever-103-toronto-tempo-85-09-18-2026`
- WNBA official recap archive: Indiana 103, Toronto 85.
- AP/Canadian Press corroboration: Mitchell 33; Clark 28/14; final 103-85.

##### Event-specific learning / document mapping

| Learning | Proposed home | Status |
|---|---|---|
| One-team ordinary-high scoring can defeat a close Under without a two-team shootout | `RULES_BASKETBALL.md` total component budget | **Strong candidate; now supported again by P-467 cross-sport analogue** |
| Blowout compression cannot be assumed to cancel favourite offensive ceiling | `RULES_BASKETBALL.md` late-game state branches | Candidate reinforcement |
| Total at/inside central corridor should be evidence-capped | `RULES_GENERAL.md` corridor rule | Existing current control; P-465 is supporting retrospective evidence |

---

### P-466 — Soccer / Argentina Torneo Clausura — Racing Club vs Sarmiento

- **Canonical ID:** P-466 (fresh pre-issue reconciliation against `PREDICTION_LOG_COMBINED_4.md` found no P-466 collision)
- **Sport / competition:** Soccer — Argentina Torneo Clausura 2026, Zona B, Fecha 10
- **Event:** Racing Club de Avellaneda vs CA Sarmiento de Junín
- **Venue:** Estadio Presidente Juan Domingo Perón, Avellaneda
- **Scheduled start:** 18 Sep 2026, 21:15 ART = **19 Sep 2026, 10:15 AEST**. The user's 10:15 PM AEST estimate was 12 hours late.
- **Game state at issue:** `PREGAME / SCHEDULED`; current live-preview pages still showed pre-match state at final refresh.
- **Research cutoff / final volatile refresh:** **19 Sep 2026, 09:50:25 AEST / 18 Sep 2026, 20:50:25 ART**
- **Method version:** MDS-2026.09.06-v4.0 / SFA-SOCCER
- **Population status:** EXPLORATORY — NOT SCORED; mini-log remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE
- **Operating mode:** SPORTS_ONLY / MARKET_BLIND
- **User-supplied contracts:** 1H Goals O/U 0.5; Full-time Total Goals O/U 2.5
- **Model-selected reference contracts:** Racing team total Over 0.5; Racing or Draw (1X); Total Corners Over 7.5
- **At issue:** no retrospective was performed.

#### Identity / rules / officials

- AFA confirms Racing–Sarmiento, Zona B, 21:15 ART.
- Referee: Leandro Rey Hilfer; assistants Pablo Gualtieri and Walter Ferreyra; fourth official Cristian Cernadas; VAR Salomé Di Iorio; AVAR Gastón Suárez.
- Regulation endpoint: 90 minutes plus stoppage time; draw is a terminal league result.
- Standard current Argentine top-flight substitution regime applies; operator-specific abandonment/corner wording was not supplied.

#### Participant / coach / availability state

**Racing — DT Juan Pablo Vojvoda**
- Current widely reported XI: **Facundo Cambeses; Mateo Martínez, Marcos Rojo, Gonzalo Escudero; Matías Zaracho, Leonel/Leandro Pérez, Matko Miljevic, Gastón Lodico, Ignacio Rodríguez; Lautaro Díaz, Adrián Martínez.**
- Racing's 23-man call-up is confirmed and includes Tagliamonte, Colombo, Espino, Kranevitter, Ortegoza, Leiva, Fernández, Tello, Campo, Conechny, Torres and Vergara among the non-starters.
- Material absences: **Juan Barinaga** (rectus-anterior tear), **Matías Pérez** (right-ankle sprain), **Ezequiel Cannavo** (right-adductor fatigue / preserved) and **Leandro Córdoba** unavailable.
- Nazareno Colombo returned to the call-up because of the defensive shortage.

**Sarmiento — DT Facundo Sava**
- Current consistently reported XI: **Thyago Ayala; Santiago Salle, Renzo Orihuela, Juan Manuel Insaurralde, Lucas Suárez; Julián Contrera, Mauricio Martínez, Cristian Zabala, Julián Mavilla; Jonathan Herrera, Junior Marabel.**
- Marabel is the principal current scoring threat and enters with six Clausura goals in the latest competition reporting.
- **Full official Sarmiento bench not retrieved at freeze.** `BENCH_NOT_RETRIEVED_SARMIENTO` applies; no margin/full-game-total row is allowed Rank #1.
- Exact lineup publication status was inconsistent across current media (some labelled the XIs confirmed, stronger outlets still described them as probable). The named XI is therefore treated as a high-probability participant state, not falsely relabelled as field-owner confirmed.

#### Current team / venue profile

**Racing 2026 Primera División**
- 27 matches: **7-8-12, 27 GF / 32 GA**
- Home: **3-4-5, 12 GF / 15 GA**
- Home xG ~**1.63**, xGA ~**1.11**
- Home shots ~**15.1/match**, but only ~**7% conversion**
- Home match Over 2.5 ~**42%**
- Home 1H Over 0.5 ~**75%**
- Racing has materially underconverted its chance volume: 1.0 home goal/match versus 1.63 home xG.

**Sarmiento current 2026 split**
- Current retrieved snapshot: 20-match lane **8-1-11, 21 GF / 28 GA**
- Away: **2-0-8, 8 GF / 18 GA**
- Away xG ~**1.03**, away xGA ~**2.01**
- Away scoring ~**0.8**, conceding ~**1.8**
- Away clean sheets: **0%** in the retrieved 10-match split
- Away failed-to-score rate ~**50%**
- Away 1H goal average: **0.2 scored / 0.5 conceded**
- Away 1H Over 0.5 ~**50%**; away second-half goal environment materially higher.

#### Mandatory L5/L10/L15/L20 trend audit

Using current 2026 league sequences, with overlapping windows treated as one evidence unit:

| Window | Racing GF/GA | O2.5 | BTTS | Sarmiento GF/GA | O2.5 | BTTS |
|---|---:|---:|---:|---:|---:|---:|
| L5 | 4 / 9 | 60% | 80% | 8 / 5 | 20% | 40% |
| L10 | 8 / 15 | 60% | 70% | 16 / 15 | 50% | 60% |
| L15 | 12 / 21 | 47% | 67% | 21 / 24 | 60% | 60% |
| L20 | 18 / 22 | 40% | 55% | 25 / 29 | 50% | 50% |

- Racing's recent result environment is more open than its longer 20-match baseline, but the mechanism is not a streak coefficient: defensive absences, repeated concession, and continuing shot volume matter.
- Sarmiento's L5 is less Over-heavy than its L10/L15 despite strong Clausura scoring. No single window owns the direction.

#### H2H continuity

Recent meetings:
- 11 Mar 2026: Sarmiento **0-0** Racing
- 24 Jul 2024: Sarmiento **1-0** Racing
- 5 Mar 2024: Racing **0-1** Sarmiento
- Oct 2023: **1-1**
- Mar 2023: Racing **1-0** Sarmiento

This is a low-scoring historical series, but current coach/role/personnel continuity is incomplete. It is descriptive only and does not override the 2026 home/away chance-creation profiles.

#### Weather / surface gate

- Exact stadium-area match-window conditions: around **17°C**, partly/intermittently cloudy, no material precipitation signal.
- No automatic goal/Under sign is assigned from mild dry conditions.
- `G15.1` match-window weather requirement satisfied.

#### Goal-process budget

**Racing regulation goal centre: ~1.55**
- Home xG 1.63 against Sarmiento away xGA 2.01 supports a strong chance-creation state.
- Downward adjustment for Racing's persistent low finishing conversion and unstable attacking execution.
- Sarmiento's retrieved away clean-sheet rate is 0%, preserving a high probability Racing score at least once.

**Sarmiento regulation goal centre: ~1.15**
- Away xG 1.03 / away scoring 0.8 are modest.
- Racing home xGA 1.11 is solid on the longer sample.
- Upward current-participant adjustment for Racing's depleted defensive unit and Sarmiento's direct-counter pair Herrera/Marabel.

**Combined centre:** ~**2.70 goals**  
**1H centre:** ~**0.95 goals**  
Representative state: **Racing 2-1 Sarmiento**.

Independent-score-tree diagnostics around those centres:
- Racing score 1+ ~**0.79**
- Racing-or-draw ~**0.72**
- 1H Over 0.5 ~**0.61**
- FT Over 2.5 ~**0.51–0.53**; final card uses **0.53** after current defensive/transition adjustment
- FT Under 2.5 ~**0.47**

#### Corner process

Current 2026 secondary corner lanes:
- Racing: about **4.30 for / 3.74 against / 8.04 total corners per match**
- Sarmiento: about **3.76 for / 5.72 against / 9.48 total**
- Racing home corner-for rate in the retrieved venue split is about **4.6**
- Sarmiento's opponent-corner allowance is the stronger directional mechanism.
- Expected combined corner centre: roughly **8.7–9.0**.

Mechanism:
- Racing's high home shot volume and likely territorial push can create blocked shots/end-line events.
- Sarmiento's direct counterattacks and trailing-state response preserve its own corner path.
- Racing's defensive reshuffle can create clearance/blocked-action exposure.

Limitation: complete field-owner cross/block/end-line/clearance chain and exact event settlement endpoint were not fully retrieved. `CORNER_EVENT_CHAIN_INCOMPLETE` applies; the row is capped at **MEDIUM-LOW / FORCED RANK**.

#### Ranked five picks

| Rank | Contract | P (`UNVALIDATED_SUBJECTIVE`) | Evidence | Rationale | Main kill path |
|---:|---|---:|---|---|---|
| **1** | **Racing team total OVER 0.5 goals** | **0.79** | MEDIUM | Racing home xG ~1.63 and ~15 shots/game; Sarmiento away xGA ~2.01 and 0% away clean sheets in retrieved split. | Racing's finishing underperformance persists and Ayala/Sarmiento survive the home pressure. |
| **2** | **Racing or Draw (1X), regulation** | **0.72** | MEDIUM-LOW / bench cap | Home chance profile favours Racing despite poor results; Sarmiento remains dangerous but its away baseline is much weaker than home. | Sarmiento's direct counter pair punishes Racing's defensive absences and wins outright. |
| **3** | **Total Corners OVER 7.5** | **0.64** | MEDIUM-LOW / FORCED RANK | Combined corner environment projects ~8.7–9.0; Sarmiento concedes ~5.7 corners/game and Racing generates home pressure. | Efficient early scoring reduces blocked/end-line sequences; central play suppresses wide/corner volume. |
| **4** | **1st Half Goals OVER 0.5** | **0.61** | MEDIUM | Racing home 1H O0.5 ~75%; current home-pressure mechanism plus weakened Racing defence provides two ways to an opener. | Sarmiento's low away 1H scoring and compact initial block produce 0-0 HT. |
| **5** | **Total Combined Goals OVER 2.5** | **0.53** | LOW-MEDIUM | Combined centre ~2.7; Racing defensive injuries plus Sarmiento's current counter threat lift the upper branch, but Racing finishing and low H2H keep the edge small. | 1-0, 1-1 or 2-0 state; Racing dominates volume without converting enough. |

**Supplied opposite sides:**
- 1H Under 0.5: **0.39**
- FT Under 2.5: **0.47**

#### Outcome-state families

| Family | Mass | Representative state |
|---|---:|---|
| Racing home-control / normal conversion | 0.31 | 2-0, 2-1 |
| Open / mutual conversion | 0.24 | 2-2, 3-1, 1-2 |
| Tight / finishing-weak | 0.25 | 1-0, 1-1, 0-0 |
| Sarmiento counter/upset | 0.20 | 0-1, 1-2 |

Derived regulation winner family:
- **Racing win ~0.46**
- **Draw ~0.26**
- **Sarmiento win ~0.28**
- **Potential winner: Racing Club**, but only as a plurality / moderate lean.

#### Cross-row dependence

- R1 and R2 share Racing territorial control but are not duplicates: Racing can score and still lose; 1X can win in a 0-0 draw.
- Approx. `P(R1 ∧ R2)` ~**0.63**.
- Approx. `P(neither R1 nor R2)` ~**0.12**, concentrated in Sarmiento win-to-nil states.
- R4 and R5 are positively coupled through an early-goal/open-game branch.
- Corner Over is only partially coupled to goals because poor finishing can still generate high blocked-shot/end-line volume.

#### Potential game winner

- **Racing Club — 0.46**
- Draw — 0.26
- Sarmiento — 0.28
- Racing is not a high-confidence winner. The call rests on its substantially stronger home xG/shot profile and Sarmiento's poor away prevention, offset by Racing's defensive injuries, poor finishing, and Sarmiento's superior current Clausura results.

#### Integrity / missingness flags

- User's scheduled AEST time was corrected from 22:15 to **10:15 AEST** using official AFA 21:15 ART kickoff.
- Racing call-up retrieved; full official Sarmiento bench not retrieved: `BENCH_NOT_RETRIEVED_SARMIENTO`.
- Starting XIs are highly consistent across current reports but not independently field-owner-confirmed in the retrieved sources.
- Corner event-chain depth incomplete; corner row capped.
- Exact sportsbook settlement wording not supplied; `UNKNOWN_DEFINITION`.
- No bookmaker odds, implied probabilities, line movement or tipster selections used.
- **Historical issued-card status at issue:** `UNSETTLED — PREGAME; NO RETROSPECTIVE`.

#### Settlement routes pre-registered

- Result / goals / lineups: AFA/LPF official result first, structured exact-event record as corroboration.
- Corners: structured Argentina Liga Profesional exact-match statistics route (ESPN/Opta-lineage `wonCorners` or another exact-event provider) with identity verification before settlement.
- Operator-specific abandonment action: unknown until terms supplied.

#### Sources

| Source | Contribution | Quality / limitation |
|---|---|---|
| AFA official fixture/officials notice | 21:15 ART kickoff, Zona B, referee/VAR crew | Field owner |
| TyC Sports current preview/live shell | Current XI expectations, coaches, match state | High-quality current secondary |
| Racing Sello / Racing-focused call-up report | Confirmed 23-player Racing call-up | Current club-specialist source |
| Racing de Alma / La Brújula | Barinaga/Pérez/Cannavo defensive availability | Current local/specialist reporting |
| FootyStats Racing 2026 | Home xG/xGA, goals, shots, 1H/FT goal rates | Structured secondary |
| FootyStats Sarmiento 2026 | Away xG/xGA, scoring/prevention, 1H split | Structured secondary |
| Global Sports Archive / current result sources | Current league result windows and H2H chronology | Structured secondary |
| Statz / current corner databases | Racing/Sarmiento corner for-against environments | Secondary derivative; not field owner |
| Exact-venue structured weather | Avellaneda match-window ~17°C, dry | Current weather |
| Drive `RULES_SOCCER.md`, `LEAGUE_RULES_SOCCER.md`, `METHOD.md`, `RULES_GENERAL.md`, `BASE_RATES_REGISTER.md` | Governing goal/corner/participant/ranking rules | Governing methodology |
| User-supplied slate | Exact 1H 0.5 and FT 2.5 thresholds | Contract source only |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| User time conversion was 12h late | `EXTERNAL_LOGGING_WORKFLOW.md` event-identity/time validation | Existing exact-time control applied |
| Racing defensive injuries alter Sarmiento transition branch | `RULES_SOCCER.md` participant-to-exposure process | Existing control applied |
| Sarmiento full bench unavailable near issue | `SOURCES.md` / participant-release lane | Source-coverage observation |
| Corner row supported by for/against rates but not full event chain | `DATA_SOURCE_REGISTER.md` | Maintain MEDIUM-LOW cap; no provider promotion |
| Current Racing volume materially exceeds finishing output | `RULES_SOCCER.md` creation-vs-finishing separation | Existing control applied |

---

---

#### Settlement and retrospective — 19 Sep 2026

**Final status:** `COMPLETED / SETTLED / RETROSPECTIVE COMPLETE`  
**Authoritative schedule correction:** AFA scheduled Racing–Sarmiento for **18 Sep 2026, 21:15 ART**, which converts to **19 Sep 2026, 10:15 AEST**. The earlier estimated Australian start time in the user-facing request was late; the AFA field-owner schedule controls.  
**Final:** Racing Club **3**, Sarmiento **1**. **Half-time:** 1-1. **Corners:** Racing 7, Sarmiento 2 = **9**.

##### A. Prediction outcome

| Rank | Original selection | Result | Settlement |
|---:|---|---:|---|
| 1 | Racing team total Over 0.5 | Racing scored 3 | **WIN** |
| 2 | Racing or Draw (1X) | Racing won | **WIN** |
| 3 | Total corners Over 7.5 | 9 corners | **WIN — secondary structured settlement** |
| 4 | 1H Goals Over 0.5 | 2 first-half goals | **WIN** |
| 5 | Full-time Goals Over 2.5 | 4 goals | **WIN** |
| — | Potential winner: Racing Club | Racing won | **WIN** |

**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 2/2. **NDCG@2:** 1.000. All five ranked selections won.

##### B. Why each pick won

**#1 Racing TT Over 0.5 — WIN.** Racing generated sustained territorial pressure and scored three times. This was the most robust way to express the home attacking edge because it did not require Racing to keep a clean sheet or win by a margin.

**#2 Racing/Draw — WIN.** Sarmiento’s counter threat did materialise — Junior Marabel equalised shortly after Racing’s opener — but Racing’s superior home creation eventually separated the sides.

**#3 Corners Over 7.5 — WIN.** The final count was 9 (7-2), almost exactly around the pregame 8.7–9.0 central expectation. Racing’s 62% possession, 16 shots and repeated attacking-third entries supported the territorial/corner mechanism. Settlement limitation: the exact corner count was recovered from consistent structured secondary records rather than an AFA field-owner stats feed, so this row remains a **research settlement with provider-quality notation**, not a newly promoted settlement lane.

**#4 First-half Over 0.5 — WIN.** Gonzalo Escudero scored around 23' and Marabel equalised around 26'; the first half produced two goals.

**#5 Full-time Over 2.5 — WIN.** Adrián Martínez and Ignacio Rodríguez added second-half goals, taking the game to four total. The pregame upper branch explicitly allowed Racing’s chance creation plus Sarmiento’s counter threat to coexist; that is the path that occurred.

**Projected winner Racing — WIN.**

##### C. Rank-1 review

No failure review. Racing TT Over 0.5 was correctly more robust than the outright winner because it survived the possibility of Sarmiento also scoring.

##### D. Top-two review

Both won. Their ordering was sound: a single Racing goal was easier to satisfy than avoiding a Sarmiento win, even though both were supported by the same territorial advantage.

##### E. Over/Under review

The full-game Over 2.5 was ranked only fifth at 0.53, reflecting genuine uncertainty. The eventual 3-1 should not be used to retroactively claim the total was obvious. The useful mechanism was that Racing’s strong home shot/xG profile and Sarmiento’s transition route could both score; the low historical H2H was correctly prevented from dominating the current matchup.

##### F. What went right

- Current home/away creation mattered more than stale low-scoring H2H.
- Defensive absences were translated into a Sarmiento counter branch instead of a crude point adjustment.
- Corners were tied to territory/pressure rather than goals alone.
- The winner call remained a moderate plurality, not false certainty.

##### G. Blind spots / source audit

- **Confirmed XIs:** not independently field-owner-confirmed at freeze.
- **Bench:** full official Sarmiento bench was not retrieved.
- **Coaches:** current coaches were identified.
- **Injuries:** Racing defensive availability was researched; Sarmiento bench completeness remained weak.
- **Schedule source:** AFA is authoritative and corrects the earlier Australian-time estimate.
- **Corners:** exact 7-2 count is supported by multiple structured secondary records and a play-by-play chronology, but an AFA statistical corner feed was not recovered.
- **Process blind spot that remains despite a perfect card:** five wins are highly dependent on one underlying Racing-territory state. Do not treat this as five independent confirmations.

##### H. Validation questions

1. Confirmed starting XIs? **High-probability current XIs, but not field-owner confirmed at freeze.**
2. Bench/substitutes? **Incomplete for Sarmiento.**
3. Coaching information? **Yes.**
4. Injuries/suspensions/rest/late changes? **Material Racing availability checked; Sarmiento depth not complete.**
5. Sources accurate/current? **AFA schedule strong; match result robust; corner settlement secondary.**
6. Better future sources? LPF/AFA official match statistical feed if it exposes corners and final XIs.
7. Blind spots? Bench completeness and dependence among ranked rows.
8. Future treatment? Keep lineup/bench missingness caps and explicitly quantify shared territorial drivers across goals/corners.

##### Settlement sources

- AFA official fixture/time: `https://www.afa.com.ar/es/posts/cronograma-y-designaciones-arbitrales-para-la-decima-fecha-del-torneo-clausura-y-de-las-categorias-de-ascenso`
- Final/result chronology: Racing 3-1 Sarmiento.
- Structured secondary match stats: 62%-38% possession, 16-9 shots, **7-2 corners**, 1.37-0.52 xG.

##### Event-specific learning / document mapping

| Learning | Proposed home | Status |
|---|---|---|
| Territory can support team-goal, 1X and corner rows simultaneously, but those hits are dependent | `RULES_SOCCER.md` / `RULES_GENERAL.md` dependence | Existing principle reinforced |
| AFA official schedule must override user-estimated converted start | `RULES_GENERAL.md` identity/time gate | Existing rule correctly applied at settlement |
| Corner provider remains secondary rather than promoted after one correct result | `SOURCES.md` / `DATA_SOURCE_REGISTER.md` | **No promotion** |

---

### P-467 — Baseball / MLB — Toronto Blue Jays @ Texas Rangers

- **Canonical / running ID:** P-467. The dedicated mini-log sequence had P-452 through P-466 already issued. A fresh check of `PREDICTION_LOG_COMBINED_4.md` found no P-467 or P-466 collision; the combined file is still awaiting mini-log import and therefore remains stale at its older queue pointer.
- **Sport / competition:** Baseball — Major League Baseball, 2026 regular season
- **Event:** Toronto Blue Jays @ Texas Rangers
- **Venue:** Globe Life Field, Arlington, Texas
- **Scheduled start:** 18 Sep 2026, 19:05 CDT / 20:05 EDT = **19 Sep 2026, 10:05 AEST (Australia/Melbourne)**
- **Pregame information freeze:** **19 Sep 2026, 10:01 AEST / 18 Sep 2026, 19:01 CDT**, approximately four minutes before scheduled first pitch. Research completed after first pitch was permitted only to corroborate facts already available pregame; no live score, plate appearance, pitch, injury occurring during the game, or other post-start information is used in this forecast.
- **Game state at freeze:** `PREGAME / SCHEDULED`
- **Method version:** **MDS-2026.09.06-v4.0 / SFA-BASEBALL**
- **Population status:** MLB = `PRIMARY_SCORED` under the method; this mini-log remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** under the current project status.
- **Operating mode:** `SPORTS_ONLY / MARKET_BLIND`
- **User-supplied contracts:** Toronto Blue Jays ML; Texas Rangers +1.5; Combined Total Over 7.5; Combined Total Under 7.5
- **Operator-specific listed-pitcher / suspension / shortening rules:** not supplied; `UNKNOWN_DEFINITION`. Full-game contracts are analysed on the standard MLB eventual-result / full-game-including-extras interpretation unless the user's operator states otherwise.
- **At issue:** no retrospective was performed.

#### Identity / starter handshake

MLB's probable-pitcher records identify the exact fixture and starters:

- **Toronto — Dylan Cease, RHP:** **11-5, 2.38 ERA, 236 SO**.
- **Texas — Kumar Rocker, RHP:** **5-11, 4.54 ERA, 132 SO**.
- MLB schedules the game at Globe Life Field at **7:05 PM CDT / 8:05 PM EDT**.
- Starter identity therefore passes `BB-P1` at field-owner level.

#### Current starter state

**Dylan Cease**

Recent recovered starts entering the game:
- 13 Sep vs Baltimore: **5.0 IP, 4 H, 1 ER, 5 BB, 9 K**
- 7 Sep at Athletics: **5.0 IP, 4 H, 4 ER (5 R), 2 BB, 6 K**
- 2 Sep at Cleveland: **6.0 IP, 4 H, 0 ER, 0 BB, 4 K**
- 28 Aug vs Seattle: **6.0 IP, 4 H, 1 ER, 1 BB, 8 K**

Current season context recovered from structured game/player records: roughly **166.1 IP, 1.06 WHIP**, with the elite strikeout line reflected in MLB's 236 strikeouts. The Baltimore start also preserves the walk-volatility branch: strong run prevention does not erase a five-walk inning/traffic route.

Baseball Savant's current-roster matchup sample shows Cease against current Texas hitters at **96 PA, 32.3% K, 11.5% BB, .332 observed wOBA, .295 xwOBA**. This is descriptive current-roster matchup evidence only; it does not override current-season form or the joint run object.

**Kumar Rocker**

Recent recovered starts entering the game:
- 12 Sep at Arizona: **4.0 IP, 2 H, 1 ER, 2 BB, 5 K**
- 4 Sep vs Tampa Bay: **5.0 IP, 9 H, 5 ER (6 R), 0 BB, 3 K**
- 30 Aug at Milwaukee: **3.0 IP, 4 H, 2 ER, 4 BB, 7 K**
- 24 Aug at Chicago White Sox: **5.2 IP, 5 H, 2 ER, 3 BB, 8 K**

Season context: **4.54 ERA, ~1.43 WHIP**. The last four starts also show a materially shorter/more variable innings path than a workhorse starter, so the Texas middle-relief transition must remain in the distribution rather than treating Rocker's first-turn quality as nine-inning prevention.

Baseball Savant's current-roster sample for Rocker versus Toronto is only **26 PA** (.190 observed wOBA, .263 xwOBA). That sample is too small to own the forecast and receives only descriptive weight.

#### Batting orders / participant state

At the final accessible field-owner refresh, MLB's September 18 starting-lineup page still displayed **TBD** for both batting orders. Current same-game secondary feeds had populated lineups, and the Rangers order was independently repeated by current team-focused reporting. Because the MLB field-owner lineup endpoint had not populated before the frozen cutoff, this card retains `STARTING_LINEUPS_NOT_OFFICIAL_AT_FREEZE` and caps participant-sensitive confidence.

**Current Toronto order from agreeing same-game secondary feeds:**
1. Brett Bateman — CF
2. Nathan Lukes — RF
3. Vladimir Guerrero Jr. — 1B
4. George Springer — DH
5. Alejandro Kirk — C
6. Kazuma Okamoto — 3B
7. Josh Smith — 2B
8. Ernie Clement — SS
9. Myles Straw — LF

**Current Texas order from agreeing same-game sources:**
1. Ezequiel Duran — 3B
2. Corey Seager — SS
3. Josh Jung — DH
4. Brandon Nimmo — RF
5. Wyatt Langford — LF
6. Jake Burger — 1B
7. Nicky Lopez — 2B
8. Elias Díaz — C
9. Evan Carter — CF

**Material lineup availability:**
- Toronto's **Andrés Giménez is not starting because of hamstring soreness**. Current reporting says he could be available off the bench but Toronto preferred to rest him for a potential Saturday return; Clement shifts to shortstop and Josh Smith to second base.
- Texas activated **Josh Jung** from the IL on 12 Sep. He is in the current order at DH, preserving his bat while reducing defensive/calf exposure.
- Texas **Joc Pederson** remains unavailable with a left-hand fracture according to MLB's current injury update.
- Texas catcher **Kyle Higashioka** remains in the return/rehab process from a right flexor strain; Elias Díaz is the current catcher in the same-game lineup feeds.

No player prop is ranked because the field-owner batting-order endpoint was still unresolved at the pregame freeze.

#### Injury / roster audit

**Toronto material current absences / restrictions**
- Andrés Giménez — hamstring soreness; not starting, possible bench availability.
- Trey Yesavage — recovering from left meniscus surgery; rehab progression, not available for this start.
- Shane Bieber — right teres-major inflammation.
- Anthony Santander — recovering from left shoulder labral surgery.
- Rudy Martin Jr. — 10-day IL with left hamstring strain.
- Toronto selected **RHP José Rodríguez** from Triple-A Buffalo on 18 Sep and designated Michael Lorenzen for assignment, adding a fresh relief option but with current-role uncertainty.

**Texas material current absences / restrictions**
- Joc Pederson — left hand fracture, not yet back to swinging as of the most recent MLB update.
- Jack Leiter — recovering from right ankle surgery and subsequent rehab interruption; not active for this game.
- Kyle Higashioka — right flexor strain / rehab-return process.
- Cole Winn — transferred to the 60-day IL on 18 Sep with a right rotator-cuff strain.
- Josh Jung is active after his calf injury and appears as DH in the current same-game order.

These are roster/context inputs, not automatic signed run adjustments; only absences that change the current batting/relief exposure chain receive directional weight.

#### Team-strength / current-regime baseline

MLB's current standings entering the game put the clubs essentially level in record:

- **Toronto: 76-77**, 619 runs scored / 656 allowed, approximately **4.05 RS/G and 4.29 RA/G**.
- **Texas: 76-77**, 638 runs scored / 677 allowed, approximately **4.17 RS/G and 4.42 RA/G**; Texas is **42-33 at home**.

A neutral first-pass scoring blend before the starter/park/availability layer is therefore:

- Toronto prior = `(4.05 TOR RS/G + 4.42 TEX RA/G) / 2 ≈ 4.24`
- Texas prior = `(4.17 TEX RS/G + 4.29 TOR RA/G) / 2 ≈ 4.23`
- Raw combined prior ≈ **8.47 runs**

Recent scores are retained as descriptive context only. Toronto's previous five contained both high and low outputs; Texas also entered from a mixed current window. No streak or last-game result receives a free coefficient.

#### Bullpen / workload state

**Toronto**
- Toronto last played on 16 Sep, beating Detroit 5-1, and then had **17 Sep off**.
- Max Scherzer covered 5.0 innings in that game; Louis Varland handled the ninth after other relief work.
- The calendar rest materially improves Toronto's ability to use its preferred late-game arms behind Cease.

**Texas**
- Texas played on **17 Sep**, losing 4-3 to Boston, and used a broad pitching chain: Tyler Alexander, Cody Bradford, Chase Silseth, Gunnar Ahlstrom, Jakob Junis, Jacob Latz and Jordan Montgomery.
- Rocker's recent starts have often ended around the fourth-to-sixth inning, so prior-day relief exposure matters more here than it would behind a dependable seven-inning starter.
- Jacob Latz entered this series as an effective closer overall, but his recent run prevention had wobbled and he surrendered part of the decisive late damage against Boston. This is not treated as proof he will pitch poorly; the direct forecast input is **workload/availability plus likely score-state role**, not a narrative “bullpen is bad” label.

Bullpen conclusion: **Toronto has the cleaner rest/availability position**, while Texas retains enough quality arms that this is a modest adjustment rather than an automatic Toronto late-game edge.

#### Venue / environment

- Globe Life Field is a **retractable-dome** venue. A current same-game structured source listed the **roof closed**, so external wind/temperature is not given a signed forecast role.
- Baseball Savant's rolling 2024-26 park factors show Globe Life Field as **run-suppressive**: overall Statcast park factor around 94, **Runs factor 88**, HR factor around 94.
- Park treatment: lower the scoring centre modestly and preserve the cluster/HR tail; do not mechanically force an Under merely because the park is suppressive.

#### Head-to-head continuity check

- Cease has a poor-looking historical career ERA versus Texas, while Rocker has had very good run prevention in his small prior sample against Toronto.
- Baseball Savant's **current-roster** samples are more informative than old team-name H2H but are still limited, especially Rocker's 26 PA.
- Under the Drive controls, neither old H2H nor one prior 2026 meeting is permitted to override current starter quality, current lineups, bullpen state and park.

#### Joint run object / centre-width arithmetic

This is an analyst distribution, not a fitted or calibrated model. Adjustments are deliberately small and explicit.

**Toronto run centre**
- season/opponent-prevention prior: **4.24**
- Rocker current-quality / shorter-start transition: **+0.15**
- Texas previous-day relief exposure behind a starter with a variable hook point: **+0.10**
- Globe Life Field run suppression: **-0.15**
- Giménez absence / current bottom-half lineup downgrade: **-0.09**
- **Toronto centre ≈ 4.25**

**Texas run centre**
- season/opponent-prevention prior: **4.23**
- Cease current/season run-prevention and strikeout profile: **-0.75**
- Toronto rested relief chain: **-0.10**
- Globe Life Field run suppression: **-0.15**
- Pederson absence / current lineup availability mix: **-0.03**
- **Texas centre ≈ 3.20**

**Combined centre:** approximately **7.45 runs**.

**Distribution width:** broad enough that the 7.5 total is close to a coin flip. Rocker's short/variable-start route, Toronto's middle-order power, Cease's walk/traffic tail, inherited-runner states and MLB extra innings preserve a meaningful 8+ run branch even with the park and Cease pulling the centre downward.

**Total normalised edge:** `|7.45 - 7.5| / ~3.5 ≈ 0.014`. That is deliberately treated as a **very small** directional edge, not a strong total signal.

Representative central score family: **Toronto 4-3 Texas**.

#### Winner object

**Potential eventual winner:**
- **Toronto Blue Jays — 0.64 `UNVALIDATED_SUBJECTIVE`**
- Texas Rangers — 0.36

Main Toronto mechanisms:
1. Clear current starter-quality edge: Cease 2.38 ERA / elite strikeout volume versus Rocker's 4.54 ERA and shorter recent starts.
2. Toronto's relief group enters better rested.
3. Texas's prior-day seven-pitcher chain increases uncertainty in the Rocker-to-middle-relief transition.

Main Texas kill paths:
1. Rocker repeats the strong first-turn contact suppression he has shown in some recent starts.
2. Cease's walk/traffic volatility creates a clustered Rangers inning despite his strong central run prevention.
3. Seager/Jung/Nimmo/Langford/Burger convert one or two high-leverage mistakes and Texas gets home-last-bat leverage.
4. Toronto's Giménez absence and road lineup reduce the offensive separation enough that a one-run or Texas-win state dominates.

#### Rangers +1.5 geometry — `G-L24`

Because Toronto and Texas enter with essentially identical season winning percentages, the current MLB `BASE_RATES_REGISTER.md` **0.0 winner-strength bucket** is the closest applicable 1.5-run cushion band:

- `b_1 = P(winner margin <= 1 | winner) ≈ 0.282`
- register sample: MLB 2026 completed games through 16 Sep; overall margin sample `n=2,286`, with the 0.0 bucket published separately in the register.

Using Toronto winner probability 0.64:

- `P(TOR wins by exactly 1) ≈ 0.64 × 0.282 = 0.180`
- `P(TOR wins by 2+) ≈ 0.64 × (1 - 0.282) = 0.460`
- `P(TEX +1.5) = P(TEX wins) + P(TOR wins by exactly 1)`
- `= 0.36 + 0.180 ≈ 0.540`

Therefore **Texas +1.5 = 0.54 `UNVALIDATED_SUBJECTIVE`**, even though Toronto is the stronger moneyline call. This is the required separation between winner probability and run-line geometry.

#### Total 7.5 decision

There is **no push mass** on 7.5.

Downward mechanisms:
- Cease's current run prevention and strikeout ability.
- Toronto's rested bullpen.
- Globe Life Field's run-suppressive rolling environment.
- Pederson absent for Texas and Giménez absent from Toronto's starting order.

Upward mechanisms:
- Rocker has a variable hook/innings distribution and a 4.54 season ERA.
- Texas used a wide relief chain the previous day.
- Toronto retains Guerrero/Springer/Okamoto/Kirk power/conversion routes.
- Cease's walk tail can create a multi-run inning without requiring sustained hard contact.
- Extra innings, if reached, use MLB's runner-on-second environment and materially widen the upper tail.

Because the modelled centre is only ~0.05 below 7.5, the preferred side is **Under**, but only narrowly:
- **Under 7.5: 0.52 `UNVALIDATED_SUBJECTIVE`**
- **Over 7.5: 0.48 `UNVALIDATED_SUBJECTIVE`**

The Over/Under pair is one `FORCED_PAIR` decision under `G-L22`; the **preferred side is Under 7.5**. The complement remains logged and ranked because the user supplied both sides.

#### Coherent outcome-state families

One explicit state decomposition is used to keep the winner, +1.5 and total rows arithmetically coherent:

| Outcome family | Mass | Contract consequences |
|---|---:|---|
| Toronto wins by 2+ and total <=7 | 0.21 | TOR ML W; TEX +1.5 L; Under W |
| Toronto wins by 2+ and total >=8 | 0.25 | TOR ML W; TEX +1.5 L; Over W |
| Toronto wins by exactly 1 and total <=7 | 0.11 | TOR ML W; TEX +1.5 W; Under W |
| Toronto wins by exactly 1 and total >=8 | 0.07 | TOR ML W; TEX +1.5 W; Over W |
| Texas wins and total <=7 | 0.20 | TOR ML L; TEX +1.5 W; Under W |
| Texas wins and total >=8 | 0.16 | TOR ML L; TEX +1.5 W; Over W |
| **Total** | **1.00** |  |

Marginals from the same object:
- Toronto ML = **0.64**
- Texas +1.5 = **0.54**
- Under 7.5 = **0.52**
- Over 7.5 = **0.48**

#### Ranked picks

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Decision type | Why this rank | Primary failure path |
|---:|---|---:|---|---|---|---|
| **1** | **Toronto Blue Jays ML** | **0.64** | **MEDIUM** | FREE | Cease provides the clearest current matchup edge, Toronto has the cleaner bullpen-rest state, and Texas's Rocker-to-middle-relief chain is less stable. | Rocker suppresses Toronto through 5+, Cease's walk/cluster tail is punished, and Texas converts home-last-bat leverage. |
| **2** | **Texas Rangers +1.5** | **0.54** | **MEDIUM** | DERIVED HANDICAP | The MLB 0.0-strength 1-run cushion band (`b1≈0.282`) protects Texas in a large share of Toronto-win states; derived from the 0.64 winner object rather than asserted independently. | Toronto wins by 2+; most naturally through an early Rocker exit plus a stressed Texas middle-relief transition. |
| **3** | **Combined Total UNDER 7.5** | **0.52** | **LOW-MEDIUM** | FORCED_PAIR — preferred | Cease + rested Toronto relief + run-suppressive park pull the centre to ~7.45. | Rocker exits early, Texas relief exposure compounds, or Cease's walk/HR cluster creates enough Texas scoring to push the game to 8+. |
| **4** | **Combined Total OVER 7.5** | **0.48** | **LOW-MEDIUM** | FORCED_PAIR — complement | Rocker's hook uncertainty and Texas's prior-day bullpen usage preserve a substantial high-run branch despite the low centre. | Cease controls Texas and Rocker/available Texas relief perform near their central or better state in the suppressive park. |

**Rank #1 is the strongest available selection by probability: Toronto Blue Jays ML.** The total is intentionally not ranked above the moneyline or +1.5 because its reconstructed edge is extremely small.

#### Top-two dependence / kill-path audit

- `P(Rank #1 ∧ Rank #2)` = probability Toronto wins by exactly one ≈ **0.18**.
- `P(neither Rank #1 nor Rank #2)` = **0.00 by contract geometry**: if Toronto ML loses, Texas has won outright and therefore Texas +1.5 wins; if Texas +1.5 loses, Toronto necessarily won by 2+ and Toronto ML wins.
- This is **structural coverage, not two independent predictive edges**. It must not be interpreted as evidence that the top two are jointly “safe.”
- Main Rank-1 loss family: Texas outright win ≈ **0.36**.
- Main Rank-2 loss family: Toronto win by 2+ ≈ **0.46**.

Representative Rank-1 state: **Toronto 4-3 Texas** — Toronto ML wins, Texas +1.5 wins, Under 7.5 wins, Over loses.

Representative high-scoring kill state: **Toronto 5-3 Texas** — Toronto ML wins, Texas +1.5 loses, Under loses, Over wins.

Representative Toronto-ML failure state: **Texas 3-2 Toronto** — Toronto ML loses, Texas +1.5 wins, Under wins.

#### Final recommendation summary

1. **Toronto Blue Jays ML — 64%**
2. **Texas Rangers +1.5 — 54%**
3. **Under 7.5 — 52%**
4. **Over 7.5 — 48%**

**Potential game winner: Toronto Blue Jays (64%)**.

No probability is described as calibrated or validated. The numbers are exact-contract `UNVALIDATED_SUBJECTIVE` probabilities required by the current Drive methodology.

#### Integrity / missingness flags

- `STARTING_LINEUPS_NOT_OFFICIAL_AT_FREEZE`: MLB's accessible field-owner starting-lineup endpoint still showed TBD at the pregame freeze; current secondary feeds agreed on both orders, with the Texas lineup additionally corroborated by current team-focused reporting.
- No player prop is promoted because of that participant-source limitation.
- `UNKNOWN_DEFINITION`: operator-specific listed-pitcher, postponement, suspension and shortened-game action wording was not supplied.
- Roof-closed status comes from a current same-game structured secondary source rather than an MLB field-owner roof notice.
- Small H2H samples are descriptive only and do not own the forecast.
- No bookmaker price, implied probability, market movement, consensus, sportsbook preview or tipster selection is used as forecast evidence.
- **Historical issued-card status at issue:** `UNSETTLED — PREGAME CARD; NO RETROSPECTIVE`.

#### Settlement routes pre-registered

- **Result / innings / starter identity / final total:** MLB official Gameday / final box score.
- **Starting lineups:** MLB official same-game lineup / box-score record once populated.
- **Run-line settlement:** official final score, including extra innings under standard full-game MLB treatment unless operator wording proves different.
- **Operator-specific void/shortening terms:** unresolved unless the user's book rules are later supplied.

#### Sources

| Source | Link / record | Contribution | Quality / limitation |
|---|---|---|---|
| MLB probable pitchers / Blue Jays & Rangers probable-pitcher pages | https://www.mlb.com/probable-pitchers/2026-09-18 ; team probable-pitcher pages | Exact fixture, Globe Life Field, 19:05 CDT start, Cease/Rocker handshake, season ERA/K records | Field owner / primary |
| MLB starting lineups, 18 Sep 2026 | https://www.mlb.com/starting-lineups/2026-09-18 | Field-owner lineup endpoint still TBD at frozen cutoff | Primary; release-latency limitation |
| Current CBS / RotoWire same-game lineup and player updates | Blue Jays @ Rangers, 18 Sep 2026; Andrés Giménez hamstring update | Current Toronto/Texas orders; Giménez out of starting XI and possible bench availability | Strong secondary; not field owner for lineup publication |
| Current structured same-game lineup/weather feed | Blue Jays @ Rangers, Globe Life Field | Corroborated same-game orders; roof closed | Secondary; roof status not independently field-owner-confirmed |
| MLB Blue Jays injuries / transactions | MLB injury tracker; https://www.mlb.com/bluejays/roster/transactions | Yesavage/Bieber/Santander context; José Rodríguez selected; Rudy Martin IL | Field owner / primary |
| MLB Rangers injuries / transactions | MLB injury tracker; https://www.mlb.com/rangers/roster/transactions | Pederson, Leiter, Higashioka, Jung activation; current roster availability | Field owner / primary |
| MLB standings | MLB standings, 18 Sep 2026 | Records, RS/RA, home/away context | Field owner / primary |
| Baseball Savant probable pitchers | https://baseballsavant.mlb.com/probable-pitchers | Current-roster Cease/Rocker matchup samples | Primary Statcast; small-sample descriptive use only |
| Baseball Savant park factors | https://baseballsavant.mlb.com/leaderboard/statcast-park-factors | Globe Life Field rolling run/HR environment | Primary Statcast |
| Current Cease / Rocker game logs | Structured current player game logs | Recent innings, runs, walks, strikeouts, hook distribution | Structured secondary; checked against official starter identity |
| MLB 16 Sep Toronto final / box record | Tigers 1, Blue Jays 5 | Toronto's most recent pitching usage and subsequent off day | Field owner |
| 17 Sep Rangers vs Red Sox final / box record and current reporting | Red Sox 4, Rangers 3 | Seven-pitcher Texas usage and late-relief workload before this game | Primary/strong current reporting |
| Drive `METHOD.md` | Sports Research Drive | MDS-2026.09.06-v4.0, MARKET_BLIND, probability/rank requirements | Governing methodology |
| Drive `RULES_BASEBALL.md` | Sports Research Drive | SFA-BASEBALL, starter/order handshake, exposure chain, bullpen and cluster controls | Governing methodology |
| Drive `RULES_GENERAL.md` / `CONTROLS.md` | Sports Research Drive | G-L24 handicap identity, forced-pair, joint kill-path and missingness controls | Governing methodology |
| Drive `BASE_RATES_REGISTER.md` | Sports Research Drive | MLB 1.5-run cushion band: overall 0.278; 0.0 strength bucket 0.282 | Governing empirical register |
| User-supplied slate | Current query | Exact ML, +1.5 and O/U 7.5 contracts | Contract source only |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| Official MLB lineup page remained TBD while multiple same-game secondary feeds had populated orders | `SOURCES.md` / `DATA_SOURCE_REGISTER.md` | Source-latency observation; preserve official-vs-secondary distinction |
| Equal-record matchup makes the MLB 0.0-strength 1.5-run cushion bucket directly applicable | `BASE_RATES_REGISTER.md` / `G-L24` usage examples | Existing control correctly applied; no new rule |
| Rocker's variable hook plus Texas's previous-day seven-pitcher usage changes the post-starter chain | `RULES_BASEBALL.md` bullpen/exposure logic | Existing score-state bullpen control applied |
| Total 7.5 sits almost exactly on reconstructed centre despite strong Cease signal | `RULES_BASEBALL.md` total / width guidance | Existing G-L2/G-L8 control correctly prevents overconfidence |
| Top two cannot both lose due ML/+1.5 geometry | `RULES_GENERAL.md` shared-driver/coverage interpretation | Existing joint-mass control; do not count as independent diversification |

---

---


---

#### Settlement and retrospective — 19 Sep 2026

**Final status:** `COMPLETED / SETTLED / RETROSPECTIVE COMPLETE`  
**Official final:** Texas Rangers **7**, Toronto Blue Jays **1** — combined **8** runs.

##### A. Prediction outcome

| Original rank | Original selection | Result | Settlement |
|---:|---|---:|---|
| 1 | Toronto Blue Jays ML | TOR lost 1-7 | **LOSS** |
| 2 | Texas Rangers +1.5 | TEX won outright | **WIN** |
| 3 | Under 7.5 | 8 runs | **LOSS by 0.5** |
| 4 | Over 7.5 | 8 runs | **WIN** |
| — | Projected winner: Toronto | TEX won | **LOSS** |

**Rank-1:** **LOSS — enhanced review required.** **Hit@2:** YES because Rank #2 won. **Wins@2:** 1/2. **NDCG@2:** **0.631** (the only top-two winner was at Rank #2).

##### B. Why each pick won or lost

**#1 Toronto ML — LOSS.** Dylan Cease, the central reason Toronto was ranked first, lasted only 2⅔ innings. He allowed four runs (one earned), three hits and a season-high **six walks**, threw only 36 of 74 pitches for strikes and struck out a season-low three. More importantly for process review, MLB’s postgame reporting shows the warning mechanism existed *before* this start: his four-seam velocity had already fallen below 95 mph in each of his prior two September outings. On Friday it averaged **93.6 mph** versus **96.9 mph** for the season. The original card documented his elite ERA/K/FIP profile but did not document a recent velocity audit. That is a material pregame information gap.

Toronto also suffered a known defensive-position downgrade. Andrés Giménez was out with hamstring soreness, moving Ernie Clement to shortstop; Clement’s throwing error in the second allowed two runs and contributed to three unearned runs charged in the inning. The pregame analysis treated Giménez mostly as an offensive/availability change, not as a defensive run-prevention mechanism.

**#2 Texas +1.5 — WIN.** The cushion won easily because Texas won outright. The original model correctly recognised that Toronto ML could coexist with Rangers +1.5 in close states, but it understated the outright Texas branch.

**#3 Under 7.5 — LOSS by 0.5.** The game reached eight via an asymmetric **Texas-high / Toronto-floor** state. Toronto scored only one. This is analytically important: an Under can fail without both offences being hot. The old total tree placed too much attention on mutual scoring and too little on one side reaching seven by itself through starter command + fielding disruption.

**#4 Over 7.5 — WIN.** It won at exactly eight, but again the mechanism was one-sided. Rocker and the Texas bullpen suppressed Toronto; the Over came from Texas exploiting Cease’s command and Toronto’s defensive mistakes.

**Projected winner Toronto — LOSS.**

##### C. Enhanced Rank-1 failure review

**Why was Toronto #1?** Cease entered with elite season-level run prevention/strikeout indicators, Toronto had the cleaner projected bullpen/rest picture, and the game model gave Toronto the stronger starter edge.

**Was the ranking justified with the information actually used?** Partly. The season-long Cease evidence was real, not fabricated. But the ranking process was incomplete because the card did not show a recent velocity/command-state check even though the decision was starter-dominant.

**Could another selection reasonably have ranked higher pregame?** Yes. With a proper recent pitch-velocity audit and the defensive-position consequence of Giménez’s absence, Texas +1.5 should have received more weight and Toronto ML less. It is not defensible to claim after the fact that Texas ML was obviously superior; the strongest correction is to shrink the Toronto starter edge and widen the Texas scoring/separation branch.

**Missed/underweighted variables**
1. Cease’s multi-start fastball-velocity decline.
2. The possibility that lower velocity and poor zone control interact, increasing walks rather than merely contact quality.
3. Giménez’s absence as **defensive-position quality**, not only batting-order quality.
4. One-sided 7+ run states in the total model.

**Could an existing rule have prevented it?** Yes in spirit: the baseball exposure/rate chain requires current starter state rather than relying on aggregate ERA, and the general rules require participant changes to propagate through their actual mechanisms. Execution was incomplete.

**New rule warranted?** A permanent numerical adjustment is not warranted from one game. A **prospective audit requirement** is warranted as a candidate: whenever starter quality materially owns an ML/total rank, record recent fastball velocity (or sport-appropriate pitch-quality proxy), strike/zone/BB process over the last 3–5 starts, and any active defensive-position downgrade behind the pitcher. This should be tested across more cards before becoming a fitted coefficient.

##### D. Top-two review

Rank #1 lost but Rank #2 won, so Hit@2 succeeded. The order was the problem. The result demonstrates why the top two should not merely contain opposite-ish coverage; Rank #1 must be the contract most robust to the strongest ordinary adverse branch. The missing velocity information would have materially changed that robustness assessment.

##### E. Over/Under review

Under 7.5 lost by 0.5. The central total may still have been reasonable, but the component distribution was not:
- Toronto floor ≈ 1 materialised.
- Texas high ≈ 7 materialised.
- That combination alone crossed 7.5.

Going forward, every baseball total should explicitly test `Away high + Home floor`, `Away floor + Home high`, and starter-failure + fielding-error/defensive-downgrade branches before a low Under is promoted.

##### F. What went right

- Texas +1.5 remained in the top two and preserved Hit@2.
- The card correctly disclosed that official starting lineups were not field-owner-confirmed at freeze.
- Giménez’s absence was identified before the game, even though its defensive consequence was underweighted.
- The forced total pair remained coherent.

##### G. Blind spots / source audit

- **Confirmed lineups:** MLB official endpoint was still TBD at freeze; postgame official lineup shows Clement at SS and the exact orders.
- **Bench/relief:** material bullpen state was investigated.
- **Coaching:** no material coaching change.
- **Availability:** Giménez absence was known; Pederson/Higashioka states were checked.
- **Source quality:** MLB injury/transaction sources were strong. Historical use of RotoWire in the secondary lineup layer would be prohibited under current v4.2 and must not recur.
- **Best new/underused source lane:** MLB/Statcast pitch-velocity and zone/command data should be part of the same-day starter state when the starter drives Rank #1.

##### H. Validation questions

1. Confirmed starting lineups? **No at freeze; official postgame lineup later available.**
2. Bench/reserve/relief state? **Adequately researched for team markets.**
3. Coaching information? **No material unresolved change.**
4. Injuries/late changes? **Yes, including Giménez, but defensive impact was under-modelled.**
5. Were sources sufficiently accurate/current? **Core MLB sources yes; participant release lag and prohibited secondary source use are limitations.**
6. Better sources? MLB exact game feed + Baseball Savant/Statcast pitch-level current-state data.
7. Blind spots? **Velocity decline, command interaction, defensive-position downgrade, one-sided scoring ceiling.**
8. Future treatment? Add a starter-state audit and propagate defensive replacements into opponent run-creation scenarios.

##### Settlement sources

- MLB official report: `https://www.mlb.com/news/dylan-cease-struggles-in-blue-jays-loss-to-rangers`
- MLB official starting lineups: `https://www.mlb.com/bluejays/roster/starting-lineups/2026-09-18`
- Final: Texas 7, Toronto 1.
- MLB reports Cease 2⅔ IP, 6 BB, 3 K, 93.6 mph average fastball vs 96.9 season; prior two starts 94.8/94.9 mph.

##### Event-specific learning / document mapping

| Learning | Proposed home | Status |
|---|---|---|
| Starter-dominant ranks need recent pitch-velocity + command-state audit | `RULES_BASEBALL.md` | **Strong candidate control; needs more-event validation** |
| Position-player absence can change fielding/run prevention, not only batting | `RULES_BASEBALL.md` participant replacement chain | **Candidate mechanism extension** |
| One-sided high + opponent floor can break a low total | `RULES_GENERAL.md` / `RULES_BASEBALL.md` component budget | Current prospective ceiling rule strongly supported |
| Historical RotoWire-derived participant evidence must not recur | `SOURCES.md` | Existing v4.2 firewall |

---

### P-468 — Basketball / WNBA — Portland Fire @ Golden State Valkyries

- **Canonical / running ID:** P-468. Fresh reconciliation found no P-468 collision in `PREDICTION_LOG_COMBINED_4.md`; the canonical combined file remains behind the dedicated mini-log sequence.
- **Sport / competition:** Basketball — WNBA, 2026 regular season
- **Event:** Portland Fire @ Golden State Valkyries
- **Official event ID:** WNBA game `1022600308`
- **Venue:** Chase Center, San Francisco, California
- **Scheduled start:** 18 Sep 2026, 19:00 PT = **19 Sep 2026, 12:00 AEST**
- **Forecast evidence cutoff:** **pre-tip information only, approximately 19 Sep 2026, 11:59 AEST**. Research completion extended beyond the scheduled start as explicitly permitted by the user, but no live possessions, score, substitutions or post-tip game information are used.
- **Method version:** MDS-2026.09.06-v4.0 / SFA-BASKETBALL
- **Population status:** WNBA = `EXPLORATORY — NOT SCORED`; mini-log remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**
- **Operating mode:** `SPORTS_ONLY / MARKET_BLIND`
- **User-supplied contracts:** Golden State Valkyries -12.5; Portland Fire +12.5; Combined Total Over 159.5; Combined Total Under 159.5
- **At issue:** no retrospective was performed.

#### Identity / rules / endpoint

- WNBA exact-game record and Golden State official schedule confirm Portland at Golden State, Chase Center, Friday 18 Sep at 7:00 PM PT.
- Full-game spread and total are treated as including WNBA overtime for research-grade settlement unless the user's operator has different terms. Exact operator overtime/abandonment wording was not supplied: `UNKNOWN_DEFINITION`.
- No bookmaker price, implied probability, line movement or consensus is used. The supplied -12.5 and 159.5 numbers define the contracts only.

#### Availability / coaches / projected rotations

**Golden State — head coach Natalie Nakase**
- **OUT:** Gabby Williams — reconditioning after the FIBA World Cup.
- **OUT:** Janelle Salaün — reconditioning after the FIBA World Cup.
- **QUESTIONABLE / reconditioning:** Cecilia Zandalasini in the latest pre-tip report; she had not yet returned to normal practice with the other late World Cup returnees in the latest strong local reporting.
- **OUT for season:** Iliana Rupert.
- Full current official roster was retrieved. The likely starting mixture is anchored to the most recent short-handed five used against Portland on 30 Aug: **Veronica Burton, Kaila Charles, Tiffany Hayes, Kayla Thornton, Kiah Stokes**, with Kaitlyn Chen, Laeticia Amihere, Justė Jocytė, Miela Sowah, Ashten Prechtel and Nadia Fingall supplying available depth depending on final active status.

**Portland — head coach Alex Sarama**
- Exact-event pregame sources list **Carla Leite (rest), Bridget Carleton (ankle), Megan DiLeo (finger) and Teja Oblak (knee) out**; Barker and Feagin remain season-long absences. Teja Oblak's Friday absence is independently dated by RotoWire.
- Portland played **the previous night**, losing 94-91 to Phoenix, so this is the second leg of a back-to-back with travel from Portland to San Francisco.
- Thursday's replacement-heavy starting five was **Karlie Samuelson, Emily Engstler, Serah Williams, Nyadiew Puoch and Jordan Harrison**. That group is used as the principal starting mixture rather than being falsely relabelled as an officially confirmed Friday five.
- The official Portland roster and current coach were retrieved; rotation alternatives include Holly Winterburn, Amy Okonkwo, Frieda Bühner and Charisma Osborne among available players.

**Participant integrity:** exact official starting fives were not independently surfaced before tip. `BK-P2 / STARTING_FIVES_NOT_OFFICIALLY_CONFIRMED` applies. Player props are not introduced, and all lineup-dependent full-game rows carry an evidence cap.

#### Rest / schedule / motivation

- Portland: second night of a back-to-back after a high-effort 94-91 loss to Phoenix. Emily Engstler scored 21; Holly Winterburn 18; Karlie Samuelson 14; Jordan Harrison had 10 assists but 6 turnovers. Portland made 12-of-30 threes (40%), a strong shooting result that is treated as an upper-state example, not copied forward as the central shooting rate.
- Golden State: first WNBA game since 30 Aug after the World Cup break. The non-World-Cup core is rested; World Cup returnees are being reintegrated. Golden State also plays Seattle the next day, so a large lead creates a real starter-minute / late-game compression branch.
- Golden State still has seeding/home-court incentive; Portland is eliminated. Motivation is not converted into a free coefficient, but it informs rotation-risk branches.

#### Team baseline / pace / recent windows

**Golden State season:** 29-11; **82.6 PPG / 75.4 allowed**, pace about **74.5**, ORtg ~110.9, DRtg ~101.3 by Basketball-Reference; the club's own preview cites a league-best **99.8 defensive rating** and 75.4 points allowed.

**Portland season:** 16-25 after the Phoenix loss; pre-Phoenix full-season snapshot approximately **86.6 PPG / 91.1 allowed**, pace ~78.5-79.4, ORtg ~108, DRtg ~113-115 depending provider methodology.

Mandatory trend audit, reconstructed from current game logs:

| Window | Golden State | Portland |
|---|---|---|
| **L5** | 4-1; **80.8 PF / 66.4 PA** | 1-4; **87.8 PF / 92.8 PA** |
| **L10** | 8-2; **81.7 PF / 70.4 PA** | 4-6; **87.1 PF / 89.1 PA** |
| **L15** | 11-4; **83.3 PF / 74.3 PA** | 5-10; **89.8 PF / 92.7 PA** |
| **L20** | 16-4; **82.5 PF / 73.0 PA** | 7-13; **89.2 PF / 90.9 PA** |

The trend signal is not “Golden State hot / Portland cold” as a coefficient. The usable mechanism is Golden State's persistent low-possession elite defense versus a Portland rotation now missing multiple high-usage creators/scorers and playing without rest.

#### Head-to-head continuity

Golden State leads the 2026 series **2-0**:
- 2 Jun: Golden State **95-77** Portland — GSV +18, 172 total.
- 30 Aug: Golden State **86-69** Portland — GSV +17, 155 total.

The 30 Aug meeting has unusually useful continuity: Golden State was already without Williams, Salaün and Zandalasini and still won by 17, leading by as many as 26. Portland was without Leite but had more of its normal scoring/rotation structure than the currently depleted group. This does **not** become a two-game fitted spread rule; it is a current-regime comparator supporting the defensive-suppression/separation branch.

#### Possession / team-score budget

**Central possessions:** ~**76**. Golden State's league-slowest ~74.5 pace is expected to pull Portland below its ~79.4 season pace. The lower possession count suppresses both the total and the probability of an extreme margin, so it is not double-counted as purely pro-favourite evidence.

**Golden State score centre: ~85.5**
- matchup prior: `(82.6 GSV scoring + 91.1 PDX allowance) / 2 = 86.85`
- Williams + Salaün out, Zandalasini uncertain/reconditioning; replacement-adjusted offensive downgrade: **-2.5**
- Portland second-night / thinned defensive rotation: **+0.9**
- home + rested non-World-Cup core: **+0.3**
- **centre ≈ 85.6**

**Portland score centre: ~71.5**
- matchup prior: `(86.6 PDX scoring + 75.4 GSV allowance) / 2 = 81.0`
- Leite + Carleton + DiLeo + Oblak absence mixture, replacement-adjusted rather than gross PPG subtraction: **-5.5**
- Golden State recent defensive regime / same-short-handed 30 Aug comparator: **-2.0**
- second-night travel/fatigue, weighted mainly to the second half: **-1.2**
- Golden State missing Williams/Salaün/Zandalasini defensive offset: **+0.8**
- expected pace compression versus Portland's normal tempo: **-1.5**
- **centre ≈ 71.6**

**Combined centre:** ~**157.2 points**.  
**Central margin:** Golden State by ~**14.0**.  
**Total width:** ~16 points; `|157.2 - 159.5| / 16 ≈ 0.14`, so the Under is a moderate rather than extreme edge.

#### Large-spread separation audit

`BASKETBALL_12.5_MARGIN_BAND_NOT_DERIVED`: the current Drive `BASE_RATES_REGISTER.md` has no WNBA 12.5-point cushion band. Under `G-L24`, neither spread side can be Rank #1; the spread probabilities below are event-tree estimates, not a league-derived handicap identity.

Factorised separation:
1. **Possessions:** ~76 possessions limits raw separation relative to a fast game — Fire +12.5 positive mechanism.
2. **Efficiency/defense:** GSV's league-best defense plus Portland's depleted creator mix strongly favours GSV separation.
3. **Turnover/ball-handling:** Jordan Harrison's 10-assist/6-turnover expanded role against Phoenix shows both creation and pressure risk; one game only, so this is a small GSV-separation branch, not a fitted coefficient.
4. **Bench/rotation:** Golden State's short-handed depth already produced an 86-69 win in Portland on 30 Aug. Portland now asks multiple reserves/development players to absorb starter creation and minutes. This favours GSV separation.
5. **Late-game compression:** Golden State is playoff-bound, starts a back-to-back, and could reduce core minutes with a large lead. Portland's young/reserve group can score against bench lineups. This is the main +12.5 protection branch.

#### Coherent outcome-state tree (`UNVALIDATED_SUBJECTIVE`)

| State | Mass | Representative score | Spread | Total |
|---|---:|---|---|---|
| GSV 13+ win, lower total | **0.34** | GSV 85-70 | GSV -12.5 | Under |
| GSV 13+ win, higher total | **0.20** | GSV 91-76 | GSV -12.5 | Over |
| GSV 1-12 win, lower total | **0.19** | GSV 82-74 | PDX +12.5 | Under |
| GSV 1-12 win, higher total | **0.15** | GSV 86-80 | PDX +12.5 | Over |
| Portland upset, lower total | **0.05** | PDX 75-72 | PDX +12.5 | Under |
| Portland upset, higher total | **0.07** | PDX 85-81 | PDX +12.5 | Over |
| **Total** | **1.00** | — | — | — |

Derived marginals:
- **Golden State eventual winner: 0.88**
- **Under 159.5: 0.58**
- **Golden State -12.5: 0.54**
- **Portland +12.5: 0.46**
- **Over 159.5: 0.42**

#### Ranked four supplied picks

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Geometry | Why this rank | Main failure path |
|---:|---|---:|---|---|---|---|
| **1** | **Combined Total UNDER 159.5** | **0.58** | **MEDIUM-LOW / BK-P2 cap** | FORCED_PAIR preferred side | Centre ~157.2; Golden State plays the league's slowest pace and best defense; Portland is missing multiple primary creators/scorers on a back-to-back. | Portland repeats Thursday's 3-point conversion and reaches ~78-82 while Golden State still scores mid/high-80s. |
| **2** | **Golden State Valkyries -12.5** | **0.54** | **MEDIUM-LOW / `BAND_NOT_DERIVED`** | FORCED_PAIR preferred side | Same short-handed GSV core beat Portland by 17 on 30 Aug; Portland is now even more depleted and on zero rest. | Low possessions plus GSV's missing scorers and late blowout rotation compress an otherwise comfortable win into 7-12 points. |
| **3** | **Portland Fire +12.5** | **0.46** | **MEDIUM-LOW / `BAND_NOT_DERIVED`** | FORCED_PAIR non-preferred side | Large cushion benefits from a ~76-possession game, Golden State's missing top scorers and possible fourth-quarter minute management. | Portland's depleted ball-handling breaks against GSV pressure and the game follows the 86-69 / 95-77 season-series separation pattern. |
| **4** | **Combined Total OVER 159.5** | **0.42** | **MEDIUM-LOW / BK-P2 cap** | FORCED_PAIR non-preferred side | Portland scored 91 the night before and replacement shooters can create a high-variance 3-point branch; GSV can reach 90 against Portland's defense. | GSV holds Portland around 68-74 while its own short-handed offence remains in the low/mid-80s. |

**Decision interpretation:** this is **two forced-pair decisions**, not four independent bets. Preferred sides: **Under 159.5** and **Golden State -12.5**. The spread decision is materially less secure than the winner call because 12.5 is an extreme basketball margin and no WNBA 12.5 cushion band is yet derived in the Drive.

#### Dependence / kill paths

- `P(Rank #1 ∧ Rank #2)` ≈ **0.34** — GSV controls the game defensively and wins by 13+ without the total reaching 160.
- `P(neither Rank #1 nor Rank #2)` ≈ **0.22** — Portland stays within 12 while the game reaches 160+, usually through strong Portland 3-point shooting and/or Golden State bench scoring after a competitive game.
- The most important shared-driver failure is Portland's replacement offense performing far above the depressed centre while Golden State's short-handed offense remains efficient enough to keep the game high-scoring.

#### Potential game winner

- **Golden State Valkyries — 0.88 `UNVALIDATED_SUBJECTIVE`**
- Portland Fire — 0.12
- Endpoint: eventual WNBA winner including overtime under research-grade interpretation.
- The winner probability is much stronger than -12.5 because all Golden State wins by 1-12 still satisfy the winner call while failing the spread.

#### Integrity / missingness

- Exact official starting fives were not independently retrieved before tip: `STARTING_FIVES_NOT_OFFICIALLY_CONFIRMED / BK-P2`.
- Portland's Friday injury report was late because of the back-to-back; exact-event current secondary reporting lists Leite/Carleton/DiLeo/Oblak out, with Oblak independently dated out for Friday. This is retained as a source-quality limitation rather than upgraded to a field-owner injury bulletin.
- Zandalasini remained questionable in the latest dated pre-tip source; no assumption that she plays normal minutes.
- `BASKETBALL_12.5_MARGIN_BAND_NOT_DERIVED`; no spread row may be Rank #1 under the current quantitative register.
- Exact operator overtime/abandonment wording not supplied: `UNKNOWN_DEFINITION`.
- Research completion crossed the scheduled tip; **no live score, possession, lineup substitution or in-game information is used**.
- No retrospective performed.
- **Historical issued-card status at issue:** `UNSETTLED — PRETIP-EVIDENCE FORECAST; NO RETROSPECTIVE`.

#### Settlement routes pre-registered

- Final score, regulation/OT, total and final margin: **WNBA official exact-game page / box score for game 1022600308**.
- Player availability/participation: WNBA official box score plus dated team/league injury reporting; do not backfill pregame certainty from postgame participation.
- Operator action for unusual suspension/abandonment remains unknown until operator terms are supplied.

#### Sources

| Source | Contribution | Quality / limitation |
|---|---|---|
| WNBA exact game page `1022600308` | Event identity, date/time, venue/game endpoint | Field owner |
| Golden State official 18 Sep game preview | 29-11 context, 86-69 prior meeting, league-best 75.4 PA defense, defensive rating, short-handed depth | Primary club/league source |
| Golden State official roster | Full current roster, Natalie Nakase coaching staff | Field owner/club |
| Portland official WNBA roster | Full current roster, Alex Sarama coaching staff | Field owner/club |
| RotoWire Williams/Salaün/Zandalasini/Oblak updates | Williams and Salaün out; Zandalasini questionable; Oblak out Friday | Current secondary, dated player-status reporting |
| AP / StatMuse exact matchup preview | Current team records, L10, current injury list, exact prior H2H | Structured secondary using Sportradar/AP; market fields ignored |
| AP Phoenix-Portland recap | Portland 94-91 loss, personnel absent, replacement scoring, second-leg B2B context | High-quality secondary |
| Basketball-Reference / StatMuse team pages | Season PPG, allowed PPG, pace, ORtg/DRtg and game logs | Structured statistical secondary; provider definitions differ slightly |
| Hoops Menu exact-match page | Principal projected starters from each team's most recent starting five | Secondary; explicitly not treated as confirmed lineup |
| San Francisco Chronicle current reporting | World Cup reintegration, practice/reconditioning and playoff-rest context | High-quality local secondary |
| Drive `METHOD.md`, `RULES_BASKETBALL.md`, `RULES_GENERAL.md`, `CONTROLS.md`, `BASE_RATES_REGISTER.md` | MDS-v4.0, SFA-BASKETBALL, BK-P2, large-spread, total-budget, forced-pair and underived-margin-band controls | Governing methodology |
| User-supplied slate | Exact -12.5 / +12.5 and O/U 159.5 contracts | Contract source only |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| Same short-handed GSV core beat PDX 86-69; current PDX more depleted | `RULES_BASKETBALL.md` current-regime/H2H continuity | Existing continuity + minutes-mixture logic; no new rule |
| Portland B2B while several primary creators are unavailable | `RULES_BASKETBALL.md` rest/rotation controls | Existing segmented-rest control applied |
| WNBA 12.5 cushion band absent | `BASE_RATES_REGISTER.md` | Data gap remains; no guessed band |
| Exact starting fives unavailable at pre-tip evidence cutoff | `DATA_SOURCE_REGISTER.md` / source-latency notes | BK-P2 cap correctly applied |
| Portland scored 91 with replacement group vs Phoenix but now faces league-best GSV defense | `RULES_BASKETBALL.md` opponent-adjusted efficiency / recent-result mechanism | Existing mechanism-over-streak rule applied |

#### Settlement and retrospective — 19 Sep 2026

**Final status:** `COMPLETED / SETTLED / RETROSPECTIVE COMPLETE`  
**Official final:** Golden State Valkyries **82**, Portland Fire **66** — combined **148**, margin **16**.

##### A. Prediction outcome

| Original rank | Original selection | Result | Settlement |
|---:|---|---:|---|
| 1 | Under 159.5 | 148 points | **WIN** |
| 2 | Golden State -12.5 | GSV won by 16 | **WIN** |
| 3 | Portland +12.5 | POR lost by 16 | **LOSS** |
| 4 | Over 159.5 | 148 points | **LOSS** |
| — | Projected winner: Golden State | GSV won | **WIN** |

**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 2/2. **NDCG@2:** 1.000.

##### B. Why each pick won or lost

**#1 Under 159.5 — WIN.** Golden State’s defensive/pace thesis was stronger than Portland’s depleted creation. The Valkyries forced **21 Portland turnovers**, generated **14 steals**, and held the Fire to their lowest scoring output of the season at 66. The total finished 11.5 points below the line.

**#2 Golden State -12.5 — WIN.** The same asymmetric defense/depth mechanism created separation. Golden State led by as many as 26 and used a 19-6 second-half run. Even while short-handed, Kaitlyn Chen and Laeticia Amihere each scored 17 at 60% shooting, while Tiffany Hayes and Kayla Thornton added 13 each. The expected bench/depth advantage materialised.

**#3 Portland +12.5 — LOSS.** Its primary protection branch was late compression/Golden State reduced core minutes. That was not enough: Portland’s turnover burden and low scoring prevented a backdoor cover.

**#4 Over 159.5 — LOSS.** Portland never generated the efficient-shooting branch required to lift the game above 159.5.

**Projected winner Golden State — WIN.**

##### C. Rank-1 review

No failure review. Under 159.5 was properly ranked above the spread because the low-possession/Portland-creation constraints were supported across more margin states.

##### D. Top-two review

Both won. Their shared mechanism was **asymmetric Golden State defensive control**, so the two successes are not independent. Still, the distribution was coherent: a low total did not automatically imply a close game because Portland’s own score could collapse while Golden State remained around the low-80s.

##### E. Over/Under review

This is a useful positive example of a correctly structured Under:
- Portland offensive floor was genuinely low due to missing creators.
- Golden State’s slow/defensive identity directly reduced Portland’s half-court efficiency.
- The opponent’s floor plus Golden State’s ordinary centre kept the total well below the line.
- The model did not need both teams to shoot poorly.

A bidirectional caution remains: turnovers can reduce opponent half-court scoring **and** create transition scoring for the defense. Here the effect was asymmetric enough that the total stayed Under while Golden State covered.

##### F. What went right

- Portland’s missing creation was correctly treated as a structural scoring-floor issue.
- Golden State’s defense and depth were weighted strongly.
- Late-game compression was identified as the main spread risk rather than assumed to be guaranteed.
- Under + favourite spread were allowed to coexist through a one-sided low score.

##### G. Blind spots / source audit

- **Confirmed starting fives:** not independently obtained before tip.
- **Bench/rotation:** current rosters and principal short-handed rotations were researched, but exact starts were a known limitation.
- **Coaches:** Natalie Nakase and Alex Sarama identified.
- **Availability:** key Portland and Golden State absences were researched; the late Friday injury report remained a timing limitation.
- **Sources:** official Valkyries/WNBA postgame reporting strongly supports final/result and turnover/steal mechanisms. Projected-start sources remained secondary and were correctly capped.
- **Blind spot:** exact turnover rate was not predictable; do not convert 21 turnovers into a permanent expected value from one game.

##### H. Validation questions

1. Confirmed starting fives? **No.**
2. Bench/rotation information? **Partial but material depth state was captured.**
3. Coaching information? **Yes.**
4. Injuries/rest/late changes? **Material absences checked; exact-event late injury timing remained imperfect.**
5. Original sources sufficiently current? **Core roster/team sources yes; projected-five sources were secondary.**
6. Better sources? Official WNBA gamebook/injury release and club pregame availability first.
7. Blind spots? Exact turnover magnitude and confirmed-five timing.
8. Future treatment? Model turnover pressure bidirectionally and retain lineup-confirmation caps.

##### Settlement sources

- Golden State Valkyries official recap: `https://valkyries.wnba.com/news/gameday-recap-20260918`
- WNBA official recap: `https://www.wnba.com/watch/video/game-recap-golden-state-valkyries-82-portland-fire-66-09-18-2026`
- Final: Golden State 82, Portland 66; 14 steals, 21 Portland turnovers, largest lead 26.

##### Event-specific learning / document mapping

| Learning | Proposed home | Status |
|---|---|---|
| Turnover pressure can support Under and favourite separation simultaneously when effect is asymmetric | `RULES_BASKETBALL.md` possession/transition chain | Existing mechanism reinforced |
| Do not infer future exact turnover count from one extreme game | `RULES_BASKETBALL.md` variance/overdispersion | Caution only |
| Missing confirmed starting fives should retain evidence cap even when outcome is correct | `RULES_BASKETBALL.md` / `SOURCES.md` | Existing control confirmed |



### P-469 — Australian Rules Football / AFL Finals — Hawthorn vs Brisbane Lions

**Latest audit status (19 Sep 2026, 19:34 AEST): `LIVE — DO NOT SETTLE`.** Current live coverage shows the preliminary final still in progress; no retrospective or settlement information is imported into the frozen pregame card.
- **Canonical ID:** P-469 (fresh reconciliation against `PREDICTION_LOG_COMBINED_4.md` found no P-469 collision; active combined log remains behind the dedicated mini-log sequence)
- **Sport / competition:** Australian Rules Football — 2026 Toyota AFL Premiership, First Preliminary Final
- **Event:** Hawthorn vs Brisbane Lions
- **Venue:** Melbourne Cricket Ground (MCG), Melbourne, Victoria
- **Official scheduled start:** **19 Sep 2026, 17:15 AEST**. The user-supplied 15:15 AEST time was corrected from the AFL field-owner fixture.
- **Game state at issue:** `PREGAME / SCHEDULED`
- **Research cutoff / final volatile refresh:** **19 Sep 2026, 15:17:50 AEST**
- **Method / controls:** **MDS-2026.09.19-v4.2 / CR-2026.09.19-3**
- **Population status:** AFL = separate AFL population; this mini-log remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**
- **Operating mode:** `SPORTS_ONLY / MARKET_BLIND`
- **User-supplied contracts:** Brisbane Lions -3.5; Hawthorn +3.5; Combined Total Over 191.5; Combined Total Under 191.5
- **Threshold quarantine:** the supplied lines were held as contract metadata and queried only after the independent sporting distribution was frozen.
- **Preflight:** `prediction_preflight.py` **PASS**, 0 blocking findings. Distribution ID `P-469-dist-v1`, SHA-256 `f1cd71e90d8badd66ea4bc7302262042faa51c2fbaebf8972ba6247ae8665436`.
- **No retrospective performed.**

#### Identity / selections / availability

- AFL's official preliminary-final fixture places this game at the **MCG at 5:15pm AEST**, not 3:15pm.
- **Hawthorn: unchanged selected line-up** from the qualifying-final win over Fremantle.
- **Brisbane: unchanged selected line-up** from the semi-final win over Adelaide.
- **Noah Answerth is OUT** for Brisbane with the ankle injury. His absence matters structurally because he was Brisbane's preferred shutdown match-up for Nick Watson; Watson was held goalless in Round 22 while closely watched by Answerth.
- **Logan Morris remains in the selected Brisbane side.** He finished the Adelaide semi-final with calf soreness/ice but was expected to be fit and Brisbane subsequently named an unchanged team.
- Hawthorn's current injury list includes **Conor Nash (neck, season)**; Cody Anderson and Sam Butler were listed as tests outside the selected AFL side. Brisbane's longer-term unavailable list includes Jack Payne, Henry Smith, Reece Torrent and Zane Zakostelsky.
- **Late-change caveat:** no official late change was verified by the 15:17:50 AEST cutoff. Because bounce is 17:15 AEST, final late changes/interchange activation can still alter the state after this card is issued.

#### Current team-strength / process evidence

- Final home-and-away ladder: **Brisbane 3rd, 64 points, 121.7%**; **Hawthorn 4th, 64 points, 120.1%**. This is a near-even season-strength base rather than a large class gap.
- Brisbane's 2026 Champion Data process profile entering finals was elite through territory and stoppage: **111.1 points for (2nd), 82.6 against (5th), clearance differential +7.3 (1st), centre-bounce score differential +5.6 (1st), contested-possession differential +6.1 (3rd), inside-50 differential +6.8 (3rd)**.
- Hawthorn's home-and-away defence ranked **4th for points conceded and 3rd for scores per inside-50 against**. In its qualifying-final win it held minor premier Fremantle to **5.10 (40)** despite Fremantle recording **57 inside-50s**, and forced 32 defensive-half turnovers.
- Round 22 at the Gabba: Brisbane beat Hawthorn **125-58** (183 total), won contested ball by 11 and used 94 uncontested marks. This is relevant matchup evidence but **not** treated as a direct repeat forecast or rebound/hangover signal.
- Hawthorn's qualifying final: **72-40 over Fremantle**. Brisbane's finals: **88-141 loss to Sydney**, then **144-91 over Adelaide**. These scores are descriptive only; the model uses the underlying territory/pressure/availability mechanisms rather than a short-window recency coefficient.

#### Venue / weather / rest

- Current Melbourne/MCG window is warm and dry: roughly **25°C around 5pm**, easing into the low 20s through the game, with very low rain risk.
- BOM's Melbourne-area guidance has a northerly/north-westerly breeze easing later in the afternoon. **An exact near-bounce MCG field-level wind vector aligned to scoring ends was not independently verified**, so no automatic wind-based Under/Over adjustment is applied; uncertainty is widened instead.
- Hawthorn enters from the qualifying-final week off; Brisbane played Adelaide seven days earlier and travels to Melbourne. No fixed "freshness points" are assigned because the framework has no validated coefficient for that effect.

#### Frozen independent joint distribution

This is an explicit **UNVALIDATED_SUBJECTIVE scenario mixture**, not a fitted/calibrated AFL model:

| Scenario | Weight | Total-points mean / SD | Brisbane-minus-Hawthorn margin mean / SD | Interpretation |
|---|---:|---:|---:|---|
| Hawthorn pressure / defensive-control | 0.36 | 176 / 19 | -5 / 20 | Hawks suppress clean entries and keep Brisbane below its normal scoring ceiling |
| Balanced one-score / normal-territory | 0.44 | 190 / 21 | +1 / 21 | near-even season strengths produce a close game around the high-180s/low-190s |
| Brisbane clearance / territory separation | 0.20 | 207 / 24 | +18 / 23 | Lions reproduce a meaningful stoppage/inside-50 edge and create a high-scoring separation tail |

- **Weighted total centre:** ~**188.4**
- **Weighted margin centre:** Brisbane by ~**2.2**
- Representative central state: **Brisbane 95 – Hawthorn 93**.
- The width is deliberately broad because Brisbane has shown both 140+ scoring and large concession tails, while Hawthorn's pressure defence can sharply suppress conversion.

#### Contract queries after distribution freeze

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` win probability | Evidence state | Forced pair | Why this rank | Main failure path |
|---:|---|---:|---|---|---|---|
| **1** | **Combined Total UNDER 191.5** | **0.570** | MEDIUM / subjective-distribution | O/U 191.5 | Independent total centre is ~188.4; Hawthorn's defensive efficiency and finals pressure create substantial low/central-total mass. | Brisbane wins territory decisively and both sides convert efficiently in warm/dry conditions. |
| **2** | **Hawthorn +3.5** | **0.533** | MEDIUM / subjective-distribution | ±3.5 | Season-strength gap is very small, MCG/rest context helps Hawthorn keep the margin compact, and Answerth's absence modestly widens Hawthorn's scoring route. | Brisbane's elite clearance/inside-50 process recreates the Round-22 separation pattern. |
| **3** | **Brisbane Lions -3.5** | **0.467** | MEDIUM / exact complement | ±3.5 | Brisbane remains the slightly more likely outright winner, but a 1-3 point Lions win belongs to Hawthorn +3.5 rather than this row. | Close-game state or Hawthorn outright win. |
| **4** | **Combined Total OVER 191.5** | **0.430** | MEDIUM / exact complement | O/U 191.5 | Brisbane's 2026 attack and separation branch preserve a real 200+ tail, but that branch is smaller than the combined defensive/central states. | Hawthorn pressure forces low-quality entries and the game stays in the 170s-180s. |

**Forced-pair interpretation:** Under 191.5 is preferred to Over 191.5; Hawthorn +3.5 is preferred to Brisbane -3.5. The four displayed probabilities are derived from the same frozen distribution; the two half-line pairs are exact complements.

#### Potential game winner

- **Brisbane Lions — 0.529 `UNVALIDATED_SUBJECTIVE`**
- Hawthorn — 0.471
- This is deliberately a **narrow** winner lean. Brisbane has the stronger clearance/inside-50 process and demonstrated a decisive Round-22 matchup route, while Hawthorn's MCG/rest/defensive profile makes the margin materially tighter than that earlier game.
- **Winner and -3.5 are not the same claim:** the model assigns meaningful mass to Brisbane winning by 1-3 points, which is why Brisbane can be the winner pick while Hawthorn +3.5 ranks above Brisbane -3.5.

#### Dependence / kill paths

- Approx. `P(UNDER 191.5 ∧ Hawthorn +3.5)` = **0.344**.
- Approx. `P(OVER 191.5 ∧ Brisbane -3.5)` = **0.241**; this is the principal shared-driver both-top-two failure state.
- Main top-two win family: contested, pressure-heavy game in which Hawthorn limits Brisbane's clean forward-half supply and the margin stays within one score.
- Main kill family: Brisbane's clearance and centre-bounce edge creates repeated high-quality entries, forcing Hawthorn to chase and lifting both the margin and total.
- Answerth's absence creates a specific Hawthorn small-forward risk for Brisbane, but it is not converted into an arbitrary signed points adjustment.

#### Integrity / missingness flags

- `LATE_CHANGES_NOT_YET_FINAL_AT_ISSUE`: named teams are official and unchanged, but final late changes closer to 17:15 AEST were not yet available/verified.
- `MCG_GROUND_WIND_VECTOR_NOT_VERIFIED`: general BOM/weather state is current, but exact end-by-end ground vector was not recovered; distribution width is retained.
- `NO_VALIDATED_AFL_NUMERICAL_MODEL`: every probability on this card is `UNVALIDATED_SUBJECTIVE`.
- No sportsbook odds, betting consensus, market movement, tipster material, fantasy/DFS projection or user line was used as a predictive input.
- **Current settlement status:** `UNSETTLED — PREGAME / NO RETROSPECTIVE`.

#### Settlement routes pre-registered

- Final score, quarter scores, match result, team changes and player participation: AFL official match centre / field-owner final record.
- Injury/late-change verification: AFL official + Hawthorn/Brisbane official team channels.
- Full-game ±3.5 and 191.5 research rows use the official final match score under the supplied full-game interpretation; if operator-specific extra-time/void terms differ, operator action is recorded separately.

#### Sources

| Source | Record / URL | Contribution | Quality / limitation |
|---|---|---|---|
| AFL Finals | `https://www.afl.com.au/finals/tickets/preliminary-final-1` | Exact event, MCG, **17:15 AEST** start | Field owner |
| AFL preliminary-finals teams | `https://www.afl.com.au/news/1613143/` | Both sides unchanged; Answerth unavailable | Field owner |
| Hawthorn team announcement | `https://www.hawthornfc.com.au/news/2130904/prelim-final-team-unchanged` | Hawthorn unchanged selected side | Team field owner |
| Brisbane team announcement | `https://www.lions.com.au/news/2131864/afl-team-announcement` | Brisbane unchanged; Answerth unable to recover; interchange/emergencies | Team field owner |
| AFL preliminary-final injury list | `https://www.afl.com.au/news/1612592/` | Current Hawthorn/Brisbane injury states | AFL official |
| AFL Hawthorn-Brisbane mega-preview | `https://www.afl.com.au/news/1612496/` | R22 process facts, Hawthorn defensive ranks, Morris fitness context | AFL / Champion Data; factual statistics only, **its editorial prediction is not used** |
| AFL Round 22 match report | `https://www.afl.com.au/news/1578402/` | Brisbane 125-58 Hawthorn; matchup context | AFL official |
| AFL Hawthorn-Fremantle QF | `https://www.afl.com.au/news/1600660/` | Hawthorn 72-40; defensive-pressure process | AFL official |
| AFL Brisbane-Adelaide SF | `https://www.afl.com.au/news/1609432/` | Brisbane 144-91; Morris calf flag | AFL official |
| AFL / Champion Data Brisbane process article | `https://www.afl.com.au/news/1606949/` | Brisbane season points/clearance/I50/process metrics | Structured statistics; the article's rebound narrative is **not used** |
| AFL ladder | `https://www.afl.com.au/` | Brisbane 3rd 121.7%; Hawthorn 4th 120.1% | AFL field owner |
| Bureau of Meteorology / current Melbourne-area forecast + current weather feed | 19 Sep 2026 match window | warm/dry conditions; breeze context | Weather field owner/current structured feed; exact ground vector not verified |
| Drive `METHOD.md`, `RULES_AFL.md`, `CONTROLS.md`, `SOURCES.md`, active mini-log | Sports Research Drive | v4.2/CR-3 pipeline, source firewall, joint-distribution/ranking requirements | Governing methodology |
| User-supplied slate | Current query | Exact ±3.5 and O/U 191.5 contract thresholds | Contract metadata only; quarantined from predictive inputs |

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| Answerth absence changes the Nick Watson matchup but should not receive a name-only points bump | `RULES_AFL.md` availability-to-conversion handshake | Existing control correctly applied |
| Hawthorn can concede I50 volume while suppressing score quality | `RULES_AFL.md` territory → shot-quality decomposition | Existing control correctly applied |
| MCG wind vector still not field-level verified | `DATA_SOURCE_REGISTER.md` / AFL weather-source lane | Source-coverage gap; no signed weather rule |
| Brisbane winner lean can coexist with Hawthorn +3.5 | `RULES_AFL.md` winner/handicap geometry | Existing control correctly applied |

#### Late pregame refresh — 19 Sep 2026, 17:06 AEST

- **Refresh type:** same-event update to **P-469**; **no new canonical ID** assigned and P-470 remains the next intended new-event ID.
- **Event state at refresh:** `PREGAME / SCHEDULED`; official AFL fixture remains Hawthorn v Brisbane Lions at the MCG, **17:15 AEST**.
- **User-time correction retained:** the supplied 15:15 AEST estimate is not the official bounce time.
- **Method / controls:** **MDS-2026.09.19-v4.2 / CR-2026.09.19-3**.
- **Operating mode:** `SPORTS_ONLY / MARKET_BLIND`.
- **Refreshed distribution:** `P-469-dist-v2-late-refresh`.
- **Distribution SHA-256:** `d52897c905a11f37e638f10eb5c1c4c24f6abd0a1285e52b680b8efea5070db1`.
- **Fail-closed preflight:** **PASS — 0 blocking findings**.
- **Retrospective:** **not performed**.

##### Late participant / availability handshake

- Latest official selected-team information still has **Hawthorn unchanged** and **Brisbane unchanged** from their previous finals.
- **Noah Answerth remains unavailable** for Brisbane with the ankle injury.
- **Logan Morris remains in Brisbane's selected side** after the calf-soreness concern from the Adelaide semi-final.
- Brisbane's named interchange remains **Sam Draper, Jaspa Fletcher, Hugh McCluggage, Levi Ashcroft and Conor McKenna**; emergencies are **Lincoln McCarthy, Cody Curtin and Bruce Reville**.
- A fresh, explicit field-owner receipt stating **"NO LATE CHANGES"** for this exact match was **not recovered** before this refresh. Therefore `LATE_CHANGES_NOT_FINAL_VERIFIED` remains active.
- No new verified injury, withdrawal, suspension or rest decision was found that warrants changing the score or margin distribution.

##### Near-bounce conditions / AFL gate correction

- BOM Melbourne (Olympic Park) remains the preferred government weather lane for the MCG precinct.
- The accessible observation record confirms dry conditions and northerly wind earlier in the day, but the exact **near-bounce, end-relative MCG wind vector mapped to the scoring ends** was still not recovered to `AF-P4` standard.
- Under `RULES_AFL.md` §8.6, **no total or handicap row may be graded above `LEAN`** while AF-P4 is unresolved.
- The original P-469 probabilities are not retrospectively rewritten. This refresh corrects the current evidence label to **LEAN** and keeps distribution width broad.

##### Refreshed independent distribution

No material valid sporting input changed enough to justify an ad-hoc centre move, so the independently rebuilt late-refresh distribution retains the same scenario masses:

| Scenario | Weight | Total mean / SD | Brisbane-minus-Hawthorn margin mean / SD |
|---|---:|---:|---:|
| Hawthorn pressure / defensive-control | 0.36 | 176 / 19 | -5 / 20 |
| Balanced one-score / normal-territory | 0.44 | 190 / 21 | +1 / 21 |
| Brisbane clearance / territory separation | 0.20 | 207 / 24 | +18 / 23 |

- **Total centre:** ~188.4
- **Margin centre:** Brisbane by ~2.2
- **Representative central score:** Brisbane 95 – Hawthorn 93.
- All probabilities remain **`UNVALIDATED_SUBJECTIVE`**.

##### Refreshed ranking — unchanged

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Refreshed evidence grade | Status |
|---:|---|---:|---|---|
| **1** | **Combined Total UNDER 191.5** | **0.570** | **LEAN — AF-P4 wind-vector cap** | Unchanged |
| **2** | **Hawthorn +3.5** | **0.533** | **LEAN — AF-P2/AF-P4 cap** | Unchanged |
| **3** | **Brisbane Lions -3.5** | **0.467** | **LEAN — exact complement** | Unchanged |
| **4** | **Combined Total OVER 191.5** | **0.430** | **LEAN — exact complement** | Unchanged |

**Potential winner:** **Brisbane Lions 0.529**, Hawthorn 0.471.

##### Why the ranking did not change

1. Hawthorn's defensive-suppression mechanism is unchanged.
2. Brisbane's clearance/territory mechanism is unchanged.
3. Answerth's absence was already incorporated; it is not double-counted.
4. Morris remains selected; the earlier calf flag has not become a verified withdrawal.
5. No final wind-vector evidence supports a signed scoring adjustment.
6. No final explicit late-change receipt was recovered, so missingness lowers evidence strength rather than creating a guessed directional change.

##### Refreshed sources

| Source | Record / URL | Contribution | Quality / limitation |
|---|---|---|---|
| AFL Finals | https://www.afl.com.au/finals/tickets/preliminary-final-1 | Exact event, MCG and 17:15 AEST start | Field owner |
| AFL match centre | https://www.afl.com.au/afl/matches/9027 | Exact 2026 preliminary-final match shell / identity | Field owner; accessible snapshot did not expose final late-change receipt |
| AFL preliminary-finals teams | AFL.com.au preliminary-finals team announcement | Both selected sides unchanged; Answerth unavailable | Field owner |
| Brisbane Lions team announcement | Brisbane Lions official AFL team announcement | Unchanged side, interchange and emergencies | Team field owner |
| Hawthorn team announcement | Hawthorn official preliminary-final team announcement | Unchanged selected side | Team field owner |
| AFL mega-preview | https://www.afl.com.au/news/1612496/ | Morris expected fit; Round-22 process facts | AFL / Champion Data factual material only; editorial prediction excluded |
| ABC Sport live blog | https://www.abc.net.au/news/2026-09-19/afl-prelim-final-hawthorn-hawks-brisbane-lions-live-blog/107165006 | Same-day pre-bounce state and 17:15 first-bounce confirmation | Independent current secondary |
| The Guardian live blog | https://www.theguardian.com/sport/live/2026/sep/19/afl-hawthorn-vs-brisbane-live-preliminary-final-hawks-v-lions-score-game-today | Same-day pre-match corroboration | Independent secondary; editorial views excluded |
| Bureau of Meteorology — Melbourne (Olympic Park) | https://www.bom.gov.au/products/IDV60901/IDV60901.95936.shtml | Near-MCG official observation lane | Government field owner; exact end-relative near-bounce vector not recovered |
| Drive `METHOD.md`, `CONTROLS.md`, `RULES_AFL.md`, `SOURCES.md` | Sports Research Drive | v4.2/CR-3 quarantine, source firewall and AFL gates | Governing methodology |
| User-supplied slate | Current query | Brisbane -3.5 / Hawthorn +3.5 / O/U 191.5 | Contract metadata only |

##### Document mapping / learning status

| Observation | Proposed home | Status |
|---|---|---|
| Exact end-relative MCG wind vector still not recoverable in final minutes | `DATA_SOURCE_REGISTER.md` / AFL weather lane | Existing source-coverage gap; no signed rule |
| Final explicit "no late changes" receipt not recovered | `SOURCES.md` / AFL participant-release lane | Source-latency/coverage observation; retain AF-P2 cap |
| Original P-469 evidence labels were too strong given AF-P4 | `RULES_AFL.md` execution audit / `LEARNING_REGISTER.md` | Execution correction: apply LEAN cap while AF-P4 unresolved |
| No valid new mechanism changed the score object | `METHOD.md` no-ad-hoc-centre discipline | Existing rule correctly prevents forecast drift |

- **Current settlement status:** `UNSETTLED — PREGAME / LATE REFRESH COMPLETE / NO RETROSPECTIVE`.


---

---


#### Settlement / retrospective — 20 Sep 2026 AEST

- **Verified final:** Brisbane Lions **131–122** Hawthorn; total **253**; Brisbane margin **9**.
- **Terminal-state gate:** PASS — AFL official exact-event final plus independent ABC and Guardian terminal coverage agreed on event/date/final.
- **Pick settlement:** Rank #1 Under 191.5 **LOSS**; Rank #2 Hawthorn +3.5 **LOSS**; Rank #3 Brisbane -3.5 **WIN**; Rank #4 Over 191.5 **WIN**; projected winner Brisbane **WIN**.
- **Rank-1 enhanced review:** the card had already named the Over + Brisbane-separation failure state, but weighted it too lightly. The larger miss was allocation: Hawthorn itself scored 122, so a very high total did not require Brisbane to separate heavily. Brisbane still won the underlying territory/clearance battle, validating part of the winner thesis while invalidating the total ordering.
- **Smallest justified change:** enforce the existing AFL high-shot / both-offences-high stress state and the global rule that a named kill path must carry enough mass to affect the ordinal. No fitted coefficient is created from one game.
- **Settlement sources:** AFL official match report; ABC Sport final/live record; The Guardian final live report; Hawthorn official postgame report.
- **Status:** **SETTLED / RETROSPECTIVE COMPLETE**.


### P-470 — Baseball / NPB — Saitama Seibu Lions @ Chiba Lotte Marines

**Latest audit status (19 Sep 2026, 19:34 AEST): `UNRESOLVED / OFFICIAL NPB PAGE STILL SHOWS 試合開始前 (BEFORE START) AFTER THE SCHEDULED 18:00 JST START`.** Do not settle; no final result exists.
- **Canonical ID:** P-470. Fresh reconciliation against `PREDICTION_LOG_COMBINED_4.md` found no P-470 collision.
- **Sport / competition:** Baseball — Nippon Professional Baseball, Pacific League, 2026 regular season
- **Event:** Saitama Seibu Lions @ Chiba Lotte Marines, 21st meeting
- **Venue:** ZOZO Marine Stadium, Chiba
- **Official scheduled start:** **19 Sep 2026, 18:00 JST = 19:00 AEST**
- **Forecast cutoff:** **19 Sep 2026, 18:57:22 AEST / 17:57:22 JST**
- **Game state at cutoff:** `PREGAME / 試合開始前`
- **Method / controls:** **MDS-2026.09.19-v4.2 / CR-2026.09.19-3**
- **Population status:** NPB is separate from MLB; current mini-log remains `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`
- **Operating mode:** `SPORTS_ONLY / MARKET_BLIND`
- **User-supplied contracts:** Seibu Lions ML; Lotte Marines +1.5; Full-game Over 6.5; Full-game Under 6.5
- **Distribution ID:** `P-470-dist-v1`
- **Distribution SHA-256:** `b943db5ff18c5a5269f718b294f3eaeb2d8582af97cefe0aac38a016af02e988`
- **Preflight:** current `prediction_preflight.py` **PASS — 0 blocking findings**
- **No retrospective performed.**

### Identity / starters / lineup availability

**Official probable starters**
- **Seibu: Chihiro Sumida, LHP** — 22 starts, 9-7, **2.21 ERA**, 159.0 IP, 128 H, 10 HR, **21 BB**, **143 K**, 4 complete games and 3 shutouts.
- **Lotte: Shuta Takano, LHP** — 29 appearances / 50.0 IP, 3-3, **2.88 ERA**, 42 H, 6 HR, 16 BB, 49 K.
- Lotte's official game-day page lists Takano at **1-0 with a 0.68 ERA against Seibu** in 2026.
- The strongest direct current matchup comparable is **1 Sep at ZOZO: Lotte 1-0 Seibu**, with Takano credited with the win. It is one game and is not treated as a deterministic repeat.

**Batting-order / bench limitation**
- At the 18:57:22 AEST cutoff the official NPB exact-game page still showed `試合開始前` and had **not exposed a complete confirmed batting order / bench list in the retrieved record**.
- Same-day NPB registration reporting did not show a Sep 19 Seibu/Lotte transaction requiring a new roster-state adjustment.
- `STARTING_LINEUPS_NOT_OFFICIAL_AT_FREEZE` therefore applies. No player prop is ranked and lineup-sensitive confidence is capped.
- No unsupported injury is inferred from absence from a search result.

### Team-strength / scoring-prevention baseline

Official Pacific League data entering the game:

| Team | Record | Runs/game | Team ERA | Runs allowed/game |
|---|---:|---:|---:|---:|
| **Seibu** | 73-56-4 (.566) | ~3.51 | **2.86** | ~3.22 |
| **Lotte** | 58-67-3 (.464) | ~3.52 | 3.89 | ~4.16 |

- Seibu's advantage is primarily **run prevention**, not a large raw season scoring advantage.
- Lotte and Seibu have nearly identical season scoring rates, so Lotte's offensive ceiling cannot be dismissed simply because Seibu has the stronger record.
- Seibu's 2026 team ERA is materially stronger and Sumida is substantially stronger than the generic Seibu staff baseline.
- Conversely, Takano's current 2.88 ERA and direct success against Seibu are materially stronger than Lotte's overall 3.89 staff ERA. This prevents the model from simply importing Lotte's season-long prevention weakness into tonight's first five-plus innings.

### Recent windows — diagnostic only

- **Seibu last five completed games:** approximately 10 runs scored / 20 allowed (2.0 / 4.0 per game).
- **Seibu last ten:** approximately 33 / 28 (3.3 / 2.8).
- **Lotte last five:** approximately 16 / 27 (3.2 / 5.4).
- **Lotte last ten:** approximately 39 / 45 (3.9 / 4.5).
- These windows conflict materially and are not used as streak coefficients. The named starter matchup, underlying season scoring/prevention, bullpen transition uncertainty and lineup availability control the distribution.

### H2H continuity

- Official Pacific League standings show the 2026 season series at **10-10** entering this game.
- The 1 Sep 1-0 Lotte win at ZOZO is retained as a high-continuity starter/venue comparator because Takano is again starting, but it remains a single-game observation.

### Weather / environment

- ZOZO Marine is outdoors.
- Current Chiba conditions are humid/cloudy with rain/showers possible around the game window and a JMA thunderstorm advisory.
- **Exact stadium-level wind direction/speed mapped to the field was not recovered at freeze.**
- Weather is therefore represented as **width / delay / pitcher-transition uncertainty**, not as an automatic Under or Over adjustment.

### Offensive / defensive ceiling-floor audit

These are **scenario-state summaries**, not fitted empirical quantiles.

| Team | Offensive floor | Centre | Ordinary high | Tail ceiling |
|---|---:|---:|---:|---:|
| **Seibu** | ~1-2 | **~3.0** | **~4-5** | 6+ |
| **Lotte** | ~1-2 | **~2.6** | **~4** | 5+ |

Defensive interaction:
- **Seibu prevention centre:** strong because of Sumida's 2.21 ERA, elite walk suppression and the league-leading-level staff prevention behind him.
- **Seibu concession high:** still preserved through Lotte's roughly 3.5 R/G season offense, home-last-bat leverage, Sumida's ordinary bad-contact/traffic tail and bullpen transition.
- **Lotte prevention centre:** much stronger tonight than Lotte's generic season ERA because Takano is the actual starter.
- **Lotte concession high:** remains meaningful because the club's full-season prevention is weak and Takano has only 50 innings on the year, so his starter-to-bullpen exposure is less certain than a 7-inning workhorse state.

### Independent joint run distribution

Explicit `UNVALIDATED_SUBJECTIVE` scenario mixture, built **before** querying 6.5:

| Scenario | Weight | Seibu mean | Lotte mean | Combined mean | Interpretation |
|---|---:|---:|---:|---:|---|
| Dual-starter control | 0.32 | 2.3 | 1.9 | 4.2 | Sumida and Takano both suppress the first two/three batting turns |
| Sumida control + Seibu moderate scoring | 0.25 | 3.3 | 2.0 | 5.3 | Seibu gains modest edge after Takano exits |
| Takano control + Lotte moderate scoring | 0.17 | 2.0 | 3.0 | 5.0 | Takano repeats strong Seibu suppression while Lotte scratches runs off Sumida/relief |
| Both central-high / bullpen leakage | 0.16 | 4.0 | 3.4 | 7.4 | Both offenses reach ordinary-high states as starters exit |
| Mutual-offense high / disruption tail | 0.10 | 5.0 | 4.4 | 9.4 | Starter failure, weather/delay or bullpen sequencing opens both offenses |

**Independent centres**
- Seibu: **3.04**
- Lotte: **2.60**
- Combined: **5.64**
- Representative score family: **Seibu 3 – Lotte 2**
- Approximate mixture SD: **2.88 runs**

### TOTAL MODEL — mandatory ceiling audit

- **Seibu floor / centre / ordinary high:** ~1-2 / **3.0** / **4-5**
- **Lotte floor / centre / ordinary high:** ~1-2 / **2.6** / **~4**
- **Projected combined total:** **5.64**
- **Central 50% scoring corridor:** approximately **4-7 runs**
- **Broader ordinary/tail corridor:** approximately **2-10 runs**
- **Supplied total:** **6.5**
- **Raw distance:** `5.64 - 6.5 = -0.86 runs`
- **Normalised distance:** about **0.30 SD**
- **Line position:** **upper part of the central corridor**
- **Main-total strength:** **MODEST UNDER, not safe / not strong**
- **Main Under failure path:** either `Seibu ordinary high + Lotte centre` or `Seibu centre + Lotte ordinary high` already approaches/crosses 6.5; both offenses need not explode simultaneously.
- **Main Over failure path:** both starters work near their current central states and neither bullpen is forced into a long early transition.

**Threshold budget**
- Seibu centre 3.0 + Lotte centre 2.6 = **5.6 → Under**
- Seibu ordinary high 4-5 + Lotte centre 2.6 = **6.6-7.6 → crosses**
- Seibu centre 3.0 + Lotte ordinary high ~4 = **~7.0 → crosses**
- Both ordinary high = **8+ → clear Over**
- Both floor/low-centre states remain comfortably Under.

This explicitly prevents treating 6.5 as a "safe Under": multiple ordinary scoring combinations clear it.

### NPB extra-inning / tie uncertainty

- Current official NPB standings through Sep 18 imply **15 actual ties across 787 league games (~1.9%)**.
- The Drive NPB terminal-tie and 1.5-run cushion identities remain `NOT_YET_DERIVED`; MLB geometry is **not imported**.
- The regulation score mixture produces more nine-inning tie mass than the observed terminal-tie rate, so extra innings must be treated explicitly.
- Exact 2026 NPB runs-added-in-extras distribution is not available in the current register. Therefore full-game total and +1.5 estimates carry additional uncertainty rather than pretending MLB extras behavior transfers exactly.

For the 6.5 total, a regulation 3-3 tie that is later decided necessarily reaches at least 7 runs. Lower tied states may or may not cross 6.5 depending on extra-inning scoring. The full-game Under estimate below therefore includes an explicit extras uncertainty cap rather than simply using the nine-inning 66.6% figure.

### Supplied-contract queries

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` estimate | Evidence | Why | Main failure path |
|---:|---|---:|---|---|---|
| **1** | **Lotte Marines +1.5** | **~0.66** | **LOW-MEDIUM / `NPB_1.5_MARGIN_BAND_NOT_DERIVED`** | Lotte keeps every outright win/tie plus Seibu one-run wins; Takano's current starter state reduces early Seibu separation. The estimate uses the joint score tree, not MLB cushion data. | Sumida dominates and Seibu creates 2+ separation once Takano exits / through Lotte relief. |
| **2** | **Combined Total UNDER 6.5** | **~0.62** | **MEDIUM-LOW / extras + lineup cap** | Independent centre 5.64; both starting pitchers have strong current prevention profiles. | One offense reaches ordinary-high while the other merely stays central; 3-3 after nine also threatens the Under immediately in extras. |
| **3** | **Seibu Lions ML** | **~0.57 conditional on a decisive result** | **MEDIUM-LOW / operator tie wording unknown** | Sumida + Seibu's materially stronger run prevention and overall record create the winner edge. | Takano again suppresses Seibu and Lotte wins a low-scoring one-run game at home. |
| **4** | **Combined Total OVER 6.5** | **~0.38** | **MEDIUM-LOW / complement of full-game subjective total view** | The line is still inside the ordinary scoring corridor; Seibu-high + Lotte-centre and Seibu-centre + Lotte-high both cross it. | Both starters control early traffic and the game stays in a 2-1 / 3-1 / 3-2 state. |

**Moneyline endpoint note:** the joint endpoint view is approximately Seibu win **55.7%**, Lotte win **42.4%**, terminal tie **1.9%**. If the user's two-way ML treats a tie as no-action/refund, the decisive conditional Seibu probability is approximately **56.8%**. Exact operator tie rules were not supplied.

### Alternate-total ladder from the same frozen distribution

These are **model target thresholds, not claims that the user's operator currently offers them**:

- **Under 7.5:** materially safer than Under 6.5; regulation estimate ~77%, but full-game extras uncertainty lowers that. Conservative endpoint range is roughly **65-77%**.
- **Under 8.5:** stronger protection again; conservative endpoint range roughly **71-85%**.
- **Over 4.5:** regulation estimate ~61%; this is the only lower alternate Over in the checked ladder that clears ~60%, but its full-game endpoint is not the same as saying tonight is an "Over game."
- **Over 5.5:** ~46% regulation; not preferred.

The model therefore does **not** automatically switch to an alternate Over merely because 5.64 is close to 6.5. The stronger alternate-total direction remains a **higher Under threshold**.

### Potential game winner

**Saitama Seibu Lions — narrow/moderate lean**

- Eventual win estimate: **~55.7%**
- Lotte win: **~42.4%**
- Terminal tie: **~1.9%**
- Conditional on a decisive result: Seibu **~56.8%**

The winner lean is driven by Sumida's 2.21 ERA / 143 K / 21 BB profile, Seibu's much stronger team prevention and the season-record gap. It is deliberately not high confidence because Takano has a credible direct suppression route against Seibu and Lotte has home-last-bat leverage.

### Dependence / kill-path audit

- Rank #1 (+1.5) and Rank #2 (Under) overlap most strongly in Lotte wins / Seibu one-run wins in low-scoring states.
- A principal both-top-two failure family is **Seibu wins by 2+ in a 7+ run game**, usually requiring Lotte relief to fail after Takano exits while Lotte still scores enough to break the Under.
- The Over does **not** require both offenses to hit their tail ceiling; 4-3, 5-2 and 4-4-type scoring states are sufficient.

### Integrity / missingness flags

- `STARTING_LINEUPS_NOT_OFFICIAL_AT_FREEZE`
- `NPB_1.5_MARGIN_BAND_NOT_DERIVED`
- `NPB_EXTRAS_RUNS_DISTRIBUTION_NOT_DERIVED`
- `EXACT_OPERATOR_TIE_ACTION_UNKNOWN`
- `ZOZO_EXACT_GAME_WIND_VECTOR_NOT_VERIFIED`
- No bookmaker odds, betting consensus, market movement, tipster material or fantasy/DFS projection entered the forecast.
- **Current status:** `UNSETTLED — PREGAME / NO RETROSPECTIVE`

### Sources

| Source | Contribution | Quality / limitation |
|---|---|---|
| NPB exact match centre — `https://npb.jp/scores/2026/0919/m-l-21/` | exact event, venue, 18:00 JST start, pregame state | field owner |
| NPB Sep 19 schedule / probable starters | Sumida / Takano official starter handshake | field owner |
| NPB official 2026 Pacific standings | records, ties, H2H 10-10, season status | field owner |
| NPB official Pacific batting statistics | team scoring rates | field owner |
| NPB official Pacific pitching statistics | team ERA / prevention | field owner |
| NPB Sumida official statistics | 9-7, 2.21 ERA, 159 IP, 143 K, 21 BB | field owner |
| Chiba Lotte official Sep 19 game page | Takano 3-3, 2.88 ERA; 1-0 / 0.68 ERA vs Seibu | team field owner |
| NPB Sep 1 Lotte-Seibu result | Lotte 1-0, Takano win | field owner |
| NPB same-day roster announcement | Sep 19 registration/deregistration state | field owner |
| Seibu / Lotte official roster/transaction pages | current roster continuity context | team field owner |
| Japan Meteorological Agency / current Chiba forecast | rain/thunderstorm risk | government weather owner; exact stadium wind unresolved |
| Drive `METHOD.md`, `RULES_BASEBALL.md`, `CONTROLS.md`, `SOURCES.md`, `BASE_RATES_REGISTER.md` | v4.2/CR-3 pipeline, source firewall, NPB gaps, endpoint controls | governing methodology |
| User-supplied slate | exact ML, +1.5 and O/U 6.5 contracts | contract metadata only |

### Document mapping / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|
| NPB 1.5-run cushion identity remains absent | `BASE_RATES_REGISTER.md` | data gap; do not import MLB |
| 6.5 sits within central scoring corridor despite strong starters | local prospective total ceiling-floor rule / `RULES_BASEBALL.md` | ceiling audit correctly prevents "safe Under" framing |
| Takano's starter-specific state differs materially from Lotte's generic staff ERA | `RULES_BASEBALL.md` starter/relief chain | existing role-specific mechanism applied |
| Official batting orders were not retrievable before freeze | `DATA_SOURCE_REGISTER.md` / NPB lineup lane | source-latency gap; no player props |
| NPB extra-inning runs-added distribution absent | `BASE_RATES_REGISTER.md` endpoint section | future derivation candidate; no MLB transfer |

---


#### Settlement / retrospective — 20 Sep 2026 AEST

- **Verified final:** Saitama Seibu Lions **4–2** Chiba Lotte Marines; total **6**.
- **Terminal-state gate:** PASS — NPB official exact-event page (`試合終了`) plus SportsNavi structured final and Nikkan Sports reporting agreed on event/date/final.
- **Pick settlement:** Rank #1 Lotte +1.5 **LOSS**; Rank #2 Under 6.5 **WIN**; Rank #3 Seibu ML **WIN**; Rank #4 Over 6.5 **LOSS**; projected winner Seibu **WIN**.
- **Rank-1 enhanced review:** the Under thesis worked, but the cushion did not. A low total can still produce a two-run margin; the card explicitly lacked a derived NPB +1.5 margin-band baseline. Takano allowed enough isolated power damage for a 4–2 state while Sumida maintained the low total.
- **Smallest justified change:** reinforce the existing baseball rule `low total != close margin`; derive NPB-specific win / one-run-loss / 2+-loss cushion geometry before treating +1.5 as strongly evidenced. Do not import MLB rates.
- **Settlement sources:** NPB official match centre; SportsNavi/Yahoo Japan structured box score; Nikkan Sports match report.
- **Status:** **SETTLED / RETROSPECTIVE COMPLETE**.


### P-471 — Basketball / Australia NBL — Melbourne United vs Adelaide 36ers

**Latest audit status (19 Sep 2026, 19:34 AEST): `LIVE — DO NOT SETTLE`.** NBL's current league page labels Melbourne United v Adelaide 36ers `LIVE NOW`; no live score is used to alter the pregame card.
- **Canonical ID:** P-471. Fresh reconciliation against `PREDICTION_LOG_COMBINED_4.md` found no P-471 collision.
- **Competition:** Hungry Jack's NBL27, Round 1
- **Event:** Melbourne United vs Adelaide 36ers
- **Venue:** John Cain Arena, Melbourne
- **Official scheduled tip:** **19 Sep 2026, 19:30 AEST**
- **Final research / distribution freeze:** **19 Sep 2026, 19:24:17 AEST**
- **Game state at freeze:** **PREGAME / official NBL schedule still displayed 0-0 / scheduled**
- **Method / controls:** **MDS-2026.09.19-v4.2 / CR-2026.09.19-3**
- **Operating mode:** `SPORTS_ONLY / MARKET_BLIND`
- **Status:** `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`
- **Supplied contracts:** Melbourne United -6.5; Adelaide 36ers +6.5; Over 188.5; Under 188.5
- **Distribution ID:** `P-471-dist-v1`
- **Distribution SHA-256:** `7d74b11df3fe25c861067824662cdfb75db15ebdf5abb118fca8f70288800099`
- **Preflight:** PASS, **0 blocking findings**
- **No retrospective performed.**

### Late participant / availability state

Official NBL current expected depth chart:
- **Melbourne PG:** Cole Anthony / Shea Ili (injured) / Christian D'Angelo / Sean Macdonald
- **Melbourne SG:** Chris Goulding / Tom Wilson / Will Hynes / Austin Shelley
- **Melbourne SF:** Luke Travers / Joe Ingles / Malith Machar / Jai Fa'ale
- **Melbourne PF:** Sam Waardenburg / Kyle Bowen / Jensen Bradtke
- **Melbourne C:** Josh Oduro / Fabijan Krslovic
- **Adelaide PG:** Bryce Cotton / Isaac White / Keanu Rasmussen / Harvey White
- **Adelaide SG:** Flynn Cameron / John Jenkins III (injured) / Deonte Williams
- **Adelaide SF:** Bul Kuol (injured) / Matt Kenyon / Jacob Rigoni
- **Adelaide PF:** Zylan Cheatham / Nick Rakocevic
- **Adelaide C:** Isaac Humphries (injured) / Ben Griscti

Official current missing list:
- Melbourne: **Shea Ili — hamstring; Sean Macdonald — ACL / season**
- Adelaide: **Isaac Humphries — knee; John Jenkins — back; Bul Kuol — ACL**
- Melbourne club separately confirmed Ili would miss Round 1 and Austin Shelley would take his lineup place.
- Adelaide club confirmed Humphries and Jenkins did not travel and would miss the opener.
- Cole Anthony publicly declared himself fit/ready and is included at the top of the current official NBL expected depth chart.
- **No confirmed starting five was recovered before freeze.** Expected depth charts are not relabelled as confirmed starters.
- Matt Kenyon is retained as expected available because the current NBL official depth chart lists him and the current official missing list does not; his earlier Blitz concussion absence is not carried forward as a current injury.

### Regime / continuity context

- This is the first regular-season game of NBL27, creating high uncertainty around pace, rotation and lineup-stint efficiencies.
- Melbourne has substantial roster and coaching change: Cole Anthony, Joe Ingles, Luke Travers, Josh Oduro and others enter a new Jacob Chance system.
- Adelaide returns much of the NBL26 runner-up core around Bryce Cotton, Flynn Cameron, Zylan Cheatham and Nick Rakocevic but has new coach Trevor Gleeson.
- Gleeson has publicly emphasized a more aggressive defensive identity with trapping, rotation and full-court pressure.
- Adelaide is nevertheless missing three players who matter structurally:
  - Humphries: interior scoring, size/rim protection and defensive rebounding;
  - Jenkins: perimeter shooting/spacing and secondary scoring;
  - Kuol: high-level perimeter defence.
- Melbourne loses Ili's point-of-attack defence and secondary handling, but Anthony restores primary creation and rim/paint pressure. Anthony's limited preseason exposure creates a minutes/conditioning uncertainty branch.

### Baseline and current-regime diagnostics

**NBL26 full-season official team averages (historical prior only):**
- Adelaide: **92.8 PPG**, **90.1 conceded**, **46.7% FG**, **36.2% 3PT**, **21.4 assists**, **40.9 rebounds**.
- Melbourne: **91.4 PPG**, **87.7 conceded**, **43.9% FG**, **18.7 assists**, **42.9 rebounds**.
- These are not copied directly into NBL27 because Melbourne's roster/coach changed materially and Adelaide's defensive scheme changed.

**Melbourne recent current-roster preseason scores:**
- lost SEM 89-91;
- beat Cairns 113-97;
- beat Perth 97-82;
- beat Illawarra 103-98;
- lost New Zealand 86-90.
The raw five-game combined-total average is ~189, but the samples have major participant discontinuity:
- Anthony played only the Cairns game among these key recent fixtures;
- Ili played at the Blitz but is out today;
- Ingles and Anthony missed the Blitz;
- Anthony and Ili both missed the 86-90 New Zealand game.
Therefore recent totals are diagnostic only.

**Adelaide Blitz:**
- lost Illawarra **99-100**;
- beat Cairns **112-86**.
These high totals are not carried over mechanically:
- Jenkins scored **16** vs Illawarra and **19** vs Cairns and is out today;
- Humphries and Kuol were already absent, so their absence is not a new adjustment relative to those Blitz samples;
- Cairns was undermanned and Adelaide shot an unsustainably high **61% FG** in the 112-point game.

### Possession / efficiency mechanism

No NBL27 regular-season pace sample exists yet. The model therefore does not publish a fabricated exact possession estimate.

The scenario tree is built from:
1. likely NBL possession environment / transition opportunities;
2. half-court creation by Anthony/Goulding/Travers/Ingles/Oduro vs Cotton/Cameron/Cheatham;
3. Adelaide's new pressure/trapping defensive scheme;
4. Melbourne's loss of Ili at point of attack;
5. Adelaide's loss of Humphries at the rim and Jenkins as a spacer;
6. offensive rebounding / free-throw pathways;
7. both-hot and both-cold shooting branches;
8. late-game foul/bonus behavior;
9. blowout-compression risk in a Melbourne-control state.

### Offensive / defensive ceiling-floor audit

These are **scenario summaries**, not fitted empirical quantiles.

| Team | Offensive floor | Centre | Ordinary high | Tail ceiling |
|---|---:|---:|---:|---:|
| **Melbourne** | ~84-87 | **~95** | **~102-105** | 110+ |
| **Adelaide** | ~80-84 | **~90** | **~97-100** | 105+ |

Defensive allowance states:
- **Melbourne defensive centre:** upper-80s to low-90s allowed, but Ili's absence raises the Cotton/Cameron perimeter-creation branch.
- **Melbourne concession ordinary high:** Adelaide ~98-101 if Cotton/Cameron create efficient paint/free-throw/three-point sequences and Cheatham/Rakocevic win enough second chances.
- **Adelaide defensive centre:** improved-scheme potential under Gleeson, but without Humphries rim protection and Kuol perimeter defence the first-game defensive ceiling is uncertain.
- **Adelaide concession ordinary high:** Melbourne ~103-106 through Anthony ball pressure, Goulding spacing, Travers transition and Oduro interior finishing.

### Independent joint score distribution

Frozen before querying 188.5 / ±6.5.

Within each scenario, team score uncertainty is represented by ~8.5-point SD per team with modest positive game-level correlation (~0.15); this is an explicit **UNVALIDATED_SUBJECTIVE** uncertainty representation, not a calibrated NBL model.

| Scenario | Weight | MEL mean | ADL mean | Total | Margin |
|---|---:|---:|---:|---:|---:|
| Melbourne control | **0.28** | 96 | 84 | 180 | MEL +12 |
| Competitive central | **0.34** | 94 | 91 | 185 | MEL +3 |
| Both efficient / shootout | **0.23** | 101 | 96 | 197 | MEL +5 |
| Adelaide resistance / low-close | **0.15** | 89 | 91 | 180 | ADL +2 |

Frozen distribution:
- **Melbourne centre:** **95.42**
- **Adelaide centre:** **90.19**
- **Projected combined total:** **185.61**
- **Projected Melbourne margin:** **+5.23**
- Approx combined-total SD: **14.48**
- Approx margin SD: **12.05**
- Central 50% total corridor: approximately **175.7–195.3**
- Broader 10–90% total corridor: approximately **167.2–204.4**
- Representative score: **Melbourne 95 – Adelaide 90**

### TOTAL MODEL — mandatory ceiling audit

- **Projected total:** **185.61**
- **Supplied total:** **188.5**
- **Raw gap:** **-2.89 points**
- **Normalized gap:** about **0.20 SD**
- **Line position:** **INSIDE the central scoring corridor**
- **Main total strength:** **MODEST / weak directional separation**
- **Preferred supplied side:** **Under 188.5**
- **Modelled Under 188.5:** **~58.5%**
- **Modelled Over 188.5:** **~41.5%**

Threshold/component budget:
- MEL centre 95 + ADL centre 90 = **~185 → Under**
- MEL ordinary high 103 + ADL centre 90 = **~193 → Over**
- MEL centre 95 + ADL ordinary high 99 = **~194 → Over**
- both ordinary high = **~202+ → Over**
- MEL floor 86 + ADL centre 90 = **~176 → Under**
- MEL centre 95 + ADL floor 82 = **~177 → Under**

**Interpretation:** 188.5 is not a safe Under. Multiple ordinary, non-tail offensive combinations clear it. The Under leads only because the most-supported central and Melbourne-control states land below 188.5.

**Biggest Under failure path:** Anthony/Goulding/Travers drive Melbourne above 100 while Cotton/Cameron/Cheatham keep Adelaide near 90-95; Adelaide's missing Humphries/Kuol weakens the defensive mechanisms that would otherwise suppress Melbourne.

**Biggest Over failure path:** Jenkins' absence reduces Adelaide spacing/shotmaking, Melbourne controls the half court, and Adelaide's new defensive pressure lowers shot quality/pace enough to produce a game in the low/mid-180s.

### Alternate-total ladder from same frozen distribution

Model target thresholds only; availability at a user's operator is **not asserted**:
- **Over 174.5:** ~77.6%
- **Over 178.5:** ~68.3%
- **Over 182.5:** ~57.8%
- **Under 188.5:** ~58.5%
- **Under 192.5:** ~68.7%
- **Under 194.5:** ~73.3%
- **Under 198.5:** ~81.3%

The model does not automatically flip to an alternate Over merely because the centre is below 188.5. A lower Over and a higher Under can both be strong because they overlap around the 180s central corridor.

### Spread / winner distribution

From the same frozen joint score model:
- **Melbourne win:** **~66.7%**
- **Adelaide +6.5:** **~54.3%**
- **Melbourne -6.5:** **~45.7%**

This is coherent rather than contradictory:
- Melbourne is more likely to win outright because its margin distribution is centred at **+5.23**.
- Adelaide +6.5 still wins in every Adelaide victory plus Melbourne wins by 1–6.
- The line therefore sits just beyond the model's central Melbourne margin.

### Ranked supplied contracts

| Rank | Pick | UNVALIDATED_SUBJECTIVE estimate | Evidence | Main rationale | Main failure |
|---:|---|---:|---|---|---|
| **1** | **Under 188.5** | **~58.5%** | **LOW-MEDIUM / line inside corridor** | Central total 185.6; Adelaide missing Jenkins/Humphries/Kuol; opening-night rotation uncertainty supports lower central efficiency. | Melbourne reaches 100+ while Adelaide remains near 90-95; ordinary-high + centre crosses 188.5. |
| **2** | **Adelaide 36ers +6.5** | **~54.3%** | **LOW-MEDIUM** | Melbourne is favoured to win but central margin is only +5.2; Cotton/Cameron/Cheatham/Rakocevic keep an Adelaide close-game branch alive. | Adelaide's missing interior/wing pieces expose them defensively and Melbourne separates late. |
| **3** | **Melbourne United -6.5** | **~45.7%** | **LOW-MEDIUM** | Home court, Anthony active, deeper expected lineup and Adelaide absences produce real separation upside. | First-game chemistry/Anthony conditioning plus Cotton/Cameron shot creation keeps margin inside six. |
| **4** | **Over 188.5** | **~41.5%** | **LOW-MEDIUM** | Both-efficient state is real; Melbourne has 100+ ceiling and Adelaide retains elite primary scoring. | Jenkins absence + Melbourne half-court control suppress Adelaide enough that total finishes ~175-186. |

### Potential winner

**Melbourne United — ~66.7%**

Representative outcome: **Melbourne 95 – Adelaide 90**.

This is a stronger outright-winner lean than a -6.5-cover lean. The model expects Melbourne to win more often than not but does not require a seven-point separation.

### Dependence / rank audit

- Rank #1 Under and Rank #2 Adelaide +6.5 overlap most strongly in competitive 89-87 / 94-91 / 95-90 type games.
- The main both-top-two failure family is a **Melbourne 100+ win by 7+ while Adelaide still contributes enough to clear 188.5**, e.g. 102-91.
- The Under does not logically imply Adelaide +6.5; the model separately checks separation and total.
- Melbourne -6.5 and Over 188.5 share a positive dependence in the high-efficiency Melbourne-separation branch, but either can win without the other.

### Missingness / integrity flags

- `NO_CONFIRMED_STARTING_FIVES_AT_FREEZE` — official NBL current page supplied expected depth charts, not a confirmed five.
- `NBL27_REGULAR_SEASON_ZERO_GAME_SAMPLE` — first game of season; prior-season and preseason data are regime-adjusted diagnostics only.
- `MELBOURNE_HIGH_ROSTER_TURNOVER`
- `COLE_ANTHONY_LIMITED_PRESEASON_EXPOSURE`
- `ADELAIDE_HUMPHRIES_JENKINS_KUOL_OUT`
- `NO_MARKET_OR_FANTASY_PREDICTIVE_INPUT`
- supplied 6.5/188.5 thresholds were queried only after the independent distribution was frozen.

### Sources

| Source | Contribution | Class |
|---|---|---|
| NBL official schedule / Game Centre | exact event, 19:30 AEST start, John Cain Arena, 0-0 scheduled state at freeze | primary field owner |
| NBL official 19 Sep talking points | current expected depth charts and missing-in-action list | primary field owner |
| Melbourne United Round 1 squad update, 18 Sep | Ili out; Shelley replacement; D'Angelo/Hynes suit up | primary team |
| Adelaide 36ers injury update, 18 Sep | Humphries and Jenkins ruled out / did not travel | primary team |
| NBL Cole Anthony update, 14 Sep | Anthony declared himself ready for opener | official competition report carrying direct player statement |
| NBL official NBL26 team-stat review | prior-season PPG, points allowed, rebounds, assists, FG%, 3P% | field-owner historical |
| NBL / club Blitz reports and schedules | Melbourne 97-82 Perth, 103-98 Illawarra; Adelaide 99-100 Illawarra, 112-86 Cairns; participant context | field-owner / primary team |
| NBL Gleeson defensive-overhaul reporting | Adelaide's planned aggressive defensive scheme | official competition report |
| Drive `METHOD.md`, `CONTROLS.md`, `RULES_GENERAL.md`, `RULES_BASKETBALL.md`, `SOURCES.md` | v4.2/CR-3 governance and basketball mechanism requirements | governing methodology |
| User-supplied slate | ±6.5 and 188.5 contract definitions only | contract metadata |

### Document mapping / candidate learning

- Season-opening basketball totals require a wider roster/coach regime uncertainty branch; do not copy prior-season OffRtg/DefRtg directly.
- If a player absence was already present in preseason comparables (Humphries, Kuol), do not count it again as a new scoring downgrade relative to those samples.
- A newly missing shooter who scored materially in the comparables (Jenkins) changes the current offense/spacing state and must be separated from the older game result.
- A star's return (Anthony) raises Melbourne's offensive ceiling but limited current-regime minutes widen the distribution instead of guaranteeing a centre increase.
- When a total threshold sits inside the central corridor, explicitly publish both safer alternate Over and higher Under thresholds rather than presenting the nominal side as safe.

**Settlement status:** `UNSETTLED — PREGAME / NO RETROSPECTIVE`.


#### Settlement / retrospective — 20 Sep 2026 AEST

- **Verified final:** Adelaide 36ers **97–95** Melbourne United; total **192**.
- **Terminal-state gate:** PASS — NBL official result/recap, Melbourne United official recap and independent AAP reporting agreed on event/date/final.
- **Pick settlement:** Rank #1 Under 188.5 **LOSS**; Rank #2 Adelaide +6.5 **WIN**; Rank #3 Melbourne -6.5 **LOSS**; Rank #4 Over 188.5 **WIN**; projected winner Melbourne **LOSS**.
- **Rank-1 / top-O/U enhanced review:** the 192 total landed inside the card's own central scoring corridor. The pregame component budget already showed Melbourne-centre + Adelaide-ordinary-high around 194, so the failure path was not missing; it was underweighted in the ordinal. Adelaide +6.5 correctly captured the close-game branch.
- **Smallest justified change:** enforce the existing central-corridor and ordinary-high team-score budget rules more strongly when ranking basketball totals. No new signed coefficient follows from one result.
- **Settlement sources:** NBL official recap/result; Melbourne United official recap; Adelaide 36ers official match wrap; AAP independent report.
- **Status:** **SETTLED / RETROSPECTIVE COMPLETE**.




### P-472 — American Football / NCAA FBS — Coastal Carolina @ Delaware

- **Canonical ID:** P-472 (next mini-log sequence ID; fresh combined-log collision check required at eventual import).
- **Sport / competition:** American Football — NCAA FBS, non-conference regular season.
- **Event:** Coastal Carolina Chanticleers @ Delaware Fightin' Blue Hens.
- **Venue:** Tubby Raymond Field at Delaware Stadium, Newark, Delaware, United States.
- **Official scheduled start:** **19 Sep 2026, 11:30 EDT (America/New_York) = 20 Sep 2026, 01:30 AEST (Australia/Melbourne)**. No correction to the user's estimate.
- **Final volatile event-state refresh:** structured college-football feed and both official team schedule surfaces still showed the game **PREGAME / created** at approximately **11:23 EDT / 01:23 AEST**.
- **Forecast freeze:** **20 Sep 2026, 01:22:45 AEST / 19 Sep 2026, 11:22:45 EDT**, before scheduled kickoff; final volatile refresh did not change the distribution.
- **Method / controls:** **MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-AMERICAN-FOOTBALL**.
- **Operating mode:** `SPORTS_ONLY / MARKET_BLIND`.
- **Population status:** NCAA FBS kept separate from NFL/CFL/UFL; **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.
- **User-supplied contracts, quarantined until after distribution freeze:** Coastal Carolina +4.5; Delaware -4.5; full-game Over 56.5; full-game Under 56.5.
- **Distribution ID:** `P-472-dist-v1`.
- **Distribution SHA-256:** `251cd5fb9e07ee529eb34808c1a3ba38f20a39dfb1cf5d7e863fd842eb401fb2`.
- **Governance preflight:** `prediction_preflight.py` **PASS — 0 blocking findings**.
- **No retrospective performed.**

#### Identity / rules / participant state

- NCAA's current football rules hub carries the 2026 rules material; this is an NCAA FBS regular-season full-game endpoint with NCAA overtime included.
- This is the **first meeting** between Coastal Carolina and Delaware.
- **Delaware expected QB: Nick Minicucci.** He started the first two 2026 games and is the established incumbent after 3,683 passing yards in 2025. Through two 2026 games: **31/63, 512 yards, 3 TD, 3 INT**.
- Delaware's current skill core includes RB **Jo Silver** and WRs **Da'Wain Lofton**, **Sean Wilson** and **Donovan Lewis**. Protection remains a key downside after heavy Vanderbilt pressure.
- **Coastal expected QB: Deuce Bailey.** Official current statistics: **33/62, 576 yards, 6 TD, 0 INT** through two starts. His explosive output is real, but the two-start Coastal sample and pressure exposure keep uncertainty broad.
- Coastal's receiving leaders include **Colton Hinton** and **Robby Washington**; its backfield has been distributed rather than one workhorse.
- **No comprehensive field-owner day-of inactive report or confirmed starting 22 was recovered before freeze.** College availability missingness remains explicit. Betting/fantasy injury lists and projected depth charts were excluded.

#### Current-regime process evidence

**Delaware (1-1)**
- Beat Merrimack **42-7**; lost at Vanderbilt **35-26**.
- Current official team figures are roughly **34.0 points/game and 442.5 yards/game**, including **337.5 passing yards/game**; two-game averages are descriptive only.
- Vanderbilt is the stronger-quality comparator: Delaware was essentially level in yardage (**338-339**), led **17-14 at halftime**, and finished with 240 passing / 98 rushing yards. Special-teams scoring inflated the final, so 61 raw points are not copied into today's centre.

**Coastal Carolina (1-1)**
- Lost at West Virginia **31-24**; beat Fordham **45-7**.
- Current official figures: **34.5 points/game, 442.5 yards/game, 291 passing yards/game and 6.7 yards/play**; again only descriptive.
- At West Virginia, Coastal produced **425 yards** and Bailey threw for **373 yards / 3 TD**, but Coastal ran for only 52 net yards, lost two fumbles and absorbed heavy pressure.
- Against Fordham, Coastal ran for **251 yards** and won 45-7, but takeaways/short fields materially aided scoring.

#### Matchup mechanisms

1. Delaware's established QB/home passing game has a credible 28-35 point path, but protection is the main kill path.
2. Bailey's explosive passing gives Coastal a real 30+ branch; Delaware's pressure/front creates the opposite sack/turnover branch.
3. Delaware can attack Coastal's high rushing-volume concession state, but opponent/context effects prevent a direct raw-average translation.
4. Turnovers, return scores and short fields remain explicit tails rather than expected repeats.
5. NWS Newark, Delaware: mostly sunny, high around 26°C, light NE-to-E wind. No rain/strong-wind suppression mechanism; no arbitrary Over adjustment.

#### Independent joint score distribution — frozen before querying 4.5 / 56.5

| Scenario | Weight | Delaware mean | Coastal mean | Mechanism |
|---|---:|---:|---:|---|
| Delaware home/trench control | 0.30 | 31 | 23 | Delaware sustains drives; pressure limits Coastal explosives |
| Competitive pass-led game | 0.35 | 30 | 29 | both QBs create chunk plays; little separation |
| Coastal explosive/pressure upside | 0.20 | 25 | 31 | Bailey chunks + Coastal disruption |
| Short-field / shootout tail | 0.15 | 37 | 34 | explosives, fourth downs, short fields/non-offensive scores |

Within-scenario team-score uncertainty is about 7.5-9 points per team with positive game-level correlation. This is an explicit **`UNVALIDATED_SUBJECTIVE`** scenario model, not a fitted/calibrated NCAA model.

- **Delaware projected points:** **30.35**
- **Coastal projected points:** **28.35**
- **Independent projected total:** **58.70**
- **Projected Delaware margin:** **+2.00**
- Approx total SD: **13.97**
- Approx margin SD: **11.61**
- Representative quantised score: **Delaware 31 – Coastal Carolina 28**

#### Total model / ceiling-floor audit

- Delaware floor / centre / ordinary high: ~**21-24 / 30-31 / 37-41**
- Coastal floor / centre / ordinary high: ~**20-23 / 27-29 / 33-36**
- **Projected total: 58.7**
- **Supplied total: 56.5**
- Raw gap: **+2.2**
- Normalised gap: **~0.16 SD**
- **Classification: CLOSE TO PROJECTION / WEAK MAIN-TOTAL EDGE**
- Ordinary states cross both sides: 31-23 (54 Under), 30-29 (59 Over), 25-31 (56 Under), 37-34 (71 Over).

#### Ranked supplied contracts

| Rank | Exact selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence | Core reason |
|---:|---|---:|---|---|
| **1** | **Coastal Carolina +4.5** | **0.577** | **LOW-MEDIUM / FORCED_PAIR** | Independent margin centre is Delaware +2; Coastal wins every upset plus Delaware wins by 1-4. |
| **2** | **Combined Total OVER 56.5** | **0.548** | **LOW / CLOSE TO PROJECTION** | Centre 58.7; both passing attacks have chunk-play ceilings, but the threshold sits inside the ordinary corridor. |
| **3** | **Combined Total UNDER 56.5** | **0.452** | **LOW / exact complement** | Pressure/control states can land in the high-40s/low-50s; this remains a real complement, not a hedge recommendation. |
| **4** | **Delaware -4.5** | **0.423** | **LOW-MEDIUM / exact complement** | Delaware is the likelier winner, but the central margin is only about two. |

#### Potential winner

- **Delaware — 0.576 `UNVALIDATED_SUBJECTIVE`**
- Coastal Carolina — 0.424
- Winner and spread are coherent: meaningful probability mass sits on Delaware winning by 1-4.

#### Dependence / kill paths

- `P(Coastal +4.5 AND Over 56.5)` ≈ **0.322**
- `P(both top two fail = Delaware -4.5 AND Under 56.5)` ≈ **0.196**
- `P(Delaware -4.5 AND Over 56.5)` ≈ **0.227**
- `P(Coastal +4.5 AND Under 56.5)` ≈ **0.255**
- Main both-top-two failure: Delaware controls without a shootout — efficient Minicucci/Silver drives create 7+ separation while pressure holds Bailey below the explosive branch.

#### Missingness / integrity flags

- `NO_CONFIRMED_DAY_OF_STARTING_22`
- `COLLEGE_AVAILABILITY_NOT_COMPREHENSIVE`
- `OFFENSIVE_LINE_SNAP_CONTINUITY_INCOMPLETE`
- `TWO_GAME_CURRENT_REGIME_SAMPLE`
- `COASTAL_NEW_COACH_QB_REGIME`
- `NO_MARKET_ODDS_CONSENSUS_FANTASY_OR_DFS_INPUT`

#### Material sources

- University of Delaware Athletics: exact-event preview/schedule, 2026 cumulative statistics, Vanderbilt recap/box.
- Coastal Carolina Athletics: 2026 cumulative statistics, Fordham recap/box, 2026 schedule.
- NCAA Football Playing Rules: 2026 rules/rule-change reference.
- National Weather Service Newark, Delaware point forecast.
- Structured college-football feed: final pre-kick state.
- SportsTalkSC Ryan Beard press-conference report: independent coaching context only; stated intent was not converted into a points adjustment.
- Sports Research Drive: `METHOD.md`, `RULES_GENERAL.md`, `RULES_AMERICAN_FOOTBALL.md`, `CONTROLS.md`, `SOURCES.md`, `LEARNING_REGISTER.md`.

#### Document mapping

- Bailey's explosive start remains a new-QB/new-coach width state, not a stable coefficient -> `RULES_AMERICAN_FOOTBALL.md`.
- Turnover/special-teams distortion -> existing `AM-B4` / `G-L1`.
- College day-of availability coverage gap -> `SOURCES.md` / `DATA_SOURCE_REGISTER.md`.
- 56.5 inside ordinary score families -> existing central-corridor / total-budget control.

- **Current settlement status:** `UNSETTLED — PREGAME / NO RETROSPECTIVE`.

#### Settlement and retrospective — 20 Sep 2026 AEST

- **Final status:** `SETTLED — FINAL`.
- **Verified final:** **Delaware 22–14 Coastal Carolina**; halftime Delaware 15–14; total **36**; Delaware margin **8**.
- **Terminal-state gate:** **PASS.** University of Delaware's official box score carries `Final`; the independent AP/CBS final record carries `FINAL / End 4th`; and the structured college-football event feed carries `closed / Q4 00:00`, all for the same 19 Sep 2026 Delaware Stadium event.
- **Original card preserved:** the pre-game probabilities, ranks and reasoning above are not rewritten.

##### A. Pick-by-pick settlement

| Rank | Frozen selection | Final target | Result |
|---:|---|---:|---|
| **1** | **Coastal Carolina +4.5** | Coastal lost by **8** | **LOSS** |
| **2** | **Combined Total OVER 56.5** | **36 points** | **LOSS** |
| **3** | **Combined Total UNDER 56.5** | 36 | **WIN** |
| **4** | **Delaware -4.5** | Delaware won by 8 | **WIN** |
| — | Projected winner: **Delaware** | Delaware won 22–14 | **WIN** |

**Top-of-list diagnostics:** Rank #1 = **LOSS**; Rank #2 = **LOSS**; Wins@2 = **0/2**; Hit@2 = **NO**; both top two lost = **YES**; binary NDCG@2 = **0.000**.  
**TOP_OU_REVIEW:** triggered because the highest-ranked O/U, Over 56.5, lost.

##### B. Actual game process

The final score looks much more one-sided than the underlying yardage. Delaware gained **395 yards** and Coastal **385**, and both averaged about **6.3 yards per play**. Nick Minicucci finished **24/32 for 302 yards, 2 TD, 0 INT**; Deuce Bailey was **16/26 for 250 yards, 2 TD, 0 INT**.

The decisive margin swing was not sustained Delaware offensive dominance. With Delaware leading only **15–14** in the fourth quarter, Coastal muffed a punt at its own 38. Delaware recovered at the Coastal 36 and, one play later, Minicucci hit Sean Wilson for a **36-yard touchdown** to make it 22–14. Coastal then reached Delaware territory but failed on fourth down and Delaware ran out the clock.

Coastal also had a long third-quarter rushing touchdown erased by an offensive-holding penalty. That is realised game variance, not evidence that a pre-game model should have "predicted" a specific penalty.

##### C. Mandatory Rank-1 failure review — Coastal +4.5

**Why it ranked first.** The frozen margin centre was Delaware +2, so Coastal +4.5 won in every Coastal victory plus Delaware wins by 1–4. The research correctly recognised Coastal's explosive passing route and Delaware's modest separation centre.

**Was the placement supported pre-game?** Broadly yes, but the **57.7% precision was stronger than the evidence quality justified**. This was an early-season two-game regime with incomplete day-of availability and a wide margin distribution.

**What actually broke it.** The card's principal both-top-two failure state was "Delaware controls without a shootout." The realised path was narrower: the game was **15–14 deep into Q4**, then a special-teams turnover created an immediate short-field touchdown. That single state flipped Coastal +4.5 while leaving the total far Under.

**Should another row have ranked above it on frozen information?** The eventual winner Delaware was already slightly favoured, but Delaware -4.5 was correctly below Coastal +4.5 because a normal Delaware win did not require five-point separation. There is no defensible hindsight basis to say -4.5 should automatically have been Rank #1. The more important issue is that the margin tree needed more explicit mass on **special-teams/turnover separation late in an otherwise close game**.

**Failure classification:** mainly **tail-allocation / execution of an existing rule**, with genuine realised variance. `AM-B4` already requires special-teams, non-offensive-score and short-field states. The issue was not absence of the mechanism; it was insufficient explicit mass in the margin distribution.

##### D. Enhanced preferred-total review — Over 56.5

This is the larger process miss.

The model projected **58.7** with Over 56.5 at **54.8%**, but the actual total was only **36**. More importantly, the frozen scenario table had **no true mutual-suppression / both-low branch**. Its four representative means were 54, 59, 56 and 71. The lowest ordinary state was already near the supplied line.

That conflicts with the prospective ceiling/floor control in this running log, which requires a **mutual-suppression branch** and explicit ordinary low/centre/high interaction states before a total can be trusted. The actual game showed exactly why: both teams moved the ball reasonably well but repeatedly failed to turn yards into points after halftime. There were only **7 second-half points**.

The miss was therefore not simply "bad luck on an Over." The distribution was **too thin in the low drive-finishing tail**. Raw early-season points/yards and explosive passing evidence were better represented than stalled drives, penalties, fourth-down failures, red-zone/field-position friction and long scoreless stretches.

**Smallest justified future change:** enforce the existing football drive-outcome requirement literally: every total model must include a declared `both offences move the ball but finish poorly` branch, separate yards/play from points/drive, and preserve turnover/penalty/failed-fourth-down states. This is an **execution reinforcement**, not a new Under coefficient or anti-Over rule.

##### E. What went right

- **Projected winner Delaware was correct.**
- The card correctly identified Minicucci's established passing continuity as Delaware's strongest offensive mechanism; he threw for 302 yards with no interceptions.
- Coastal's explosive-pass branch was real: Bailey averaged roughly 9.6 yards per attempt and threw two touchdowns.
- The analysis explicitly retained special-teams and turnover tails rather than treating them as impossible.
- Weather correctly received no arbitrary Under/Over sign; conditions were sunny and did not decide the game.

##### F. Availability / lineup audit

The expected quarterbacks were correct. A comprehensive field-owner starting 22/inactive list was not recovered before issue, and nothing in the post-game record demonstrates that a hidden late participant change was the main cause of the forecast miss. The limitation therefore remains a **completeness gap**, not a hindsight excuse.

##### G. Source audit

| Source | Settlement / retrospective contribution | Disposition |
|---|---|---|
| University of Delaware official box score — `https://bluehens.com/sports/football/stats/2026/coastal-carolina/boxscore/35196` | Official **Final 22–14**, quarter scores, play-by-play, team/player statistics, game timing | **PRIMARY / FIELD-OWNER TEAM** |
| CBS Sports / AP final — `https://www.cbssports.com/college-football/gametracker/recap/NCAAF_20260919_CSTCAR%40DE/` | Independent `FINAL`, 22–14, special-teams turnover and Wilson TD | **HIGH-QUALITY INDEPENDENT** |
| Structured college-football event feed, game `a580dbf1-45e8-467a-a6b8-21b0f5548c55` | `closed / Q4 00:00`, 22–14, final stats | **STRUCTURED EVENT LINEAGE** |
| Delaware official post-game report | Wilson/defensive performance context | Same Delaware lineage; corroboration, **not an extra independent lineage** |
| Yahoo/AP | Same AP story as CBS | Same AP lineage; **not double-counted** |

**Source learning:** the team official box score is excellent for drive-level settlement. Mirrors of the AP report are one lineage and must not be counted multiple times.

##### H. Blind spots / rule disposition

| Finding | Was it knowable? | Future mitigation | Document home |
|---|---|---|---|
| No true mutual-suppression branch in the total tree | **Yes — required by existing local control** | Explicit low drive-finishing state on every gridiron total | `RULES_AMERICAN_FOOTBALL.md` / execution audit |
| Special-teams turnover could create late separation in a close game | Mechanism yes; exact event no | Keep explicit `AM-B4` short-field branch in margin family | `RULES_AMERICAN_FOOTBALL.md` |
| Early-season points/yards overstated scoring conversion certainty | Yes, as uncertainty | Separate yards/play from scoring-drive conversion and widen finishing tail | `RULES_AMERICAN_FOOTBALL.md`; `LEARNING_REGISTER.md` observation |
| Full day-of availability not captured | Known pre-game | Continue missingness flag; do not infer health | `SOURCES.md` / `DATA_SOURCE_REGISTER.md` |

**Algorithm disposition:** **NO NEW PERMANENT FORECAST WEIGHT.** Existing controls were under-executed; enforce them before adding new rules.

- **Status:** **SETTLED / RETROSPECTIVE COMPLETE**.


### P-473 — Soccer / English Premier League — Nottingham Forest vs Coventry City

- **Canonical ID:** P-473.
- **Competition:** English Premier League, 2026/27 Matchweek 5.
- **Event:** Nottingham Forest vs Coventry City.
- **Venue:** The City Ground, Nottingham, England.
- **Official scheduled start:** **19 Sep 2026, 17:30 BST (Europe/London, UTC+1) = 20 Sep 2026, 02:30 AEST (Australia/Melbourne, UTC+10)**; Melbourne calendar-date rollover = YES. User estimate was correct.
- **Final pregame state check used for freeze:** **SCHEDULED / 0-0**, approximately 02:27 AEST, before scheduled kickoff.
- **Method / controls:** **MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-SOCCER**.
- **Operating mode:** `SPORTS_ONLY / MARKET_BLIND`.
- **Population:** EPL separate population; current running log remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.
- **Supplied contracts, quarantined until after distribution freeze:** 1H O/U 0.5 goals; regulation O/U 2.5 goals.
- **Distribution:** `P-473-dist-v1`; SHA-256 `b7796567f534a57824c67c29c5bc4b77fee64ae4a34ac924f205612c2b323a79`.
- **Prediction preflight:** **PASS — 0 blocking findings**.
- **No retrospective performed.**

#### Participant / availability status

- A reliable field-owner confirmed XI + full bench for both clubs was **not recovered to gate standard before the pregame freeze**. Projected lineups are not relabelled as confirmed.
- Forest: Oliver Glasner confirmed **Nikola Milenkovic OUT** for Coventry and **Nicolo Savona OUT**; Jair Cunha returned to light training and was to be assessed. Otherwise Glasner indicated the squad was expected available.
- Coventry: **Taiwo Awoniyi suspended**. Current independent team-news reporting also has Haji Wright, Josh Eccles, Luke Woolfenden and Kaine Kesler-Hayden unavailable, while Aurele Amenda was highly doubtful after an early calf injury in the midweek cup match.
- Because XI/bench completeness is unresolved, lineup-sensitive player props are **not ranked**. Side/full-match-total evidence remains capped.

#### Current process evidence

- Forest through four PL games: **4 goals, 4 conceded, 7.12 xG, 4.16 xGA, 58 shots, 14 SOT, 11 corners**.
- Coventry through four PL games: **0 goals, 10 conceded, ~4.72 xG, ~7.46 xGA, 41 shots, 13 SOT, 18 corners**.
- Coventry's 0 goals are therefore not treated as a stable zero-scoring rate; they have generated chance volume materially above zero and are aggressively shrunk away from the observed finishing drought.
- Forest won 2-1 at Aston Villa last round after 0-0 vs Spurs and 2-2 at Liverpool. Coventry lost its first four PL games and then lost 3-1 to Aston Villa in the League Cup.
- Coventry's opponent set has been unusually difficult, so the raw 0-10 league goal difference is not transferred directly into a Forest blowout forecast.

#### Weather / environment

- Met Office game-window forecast: dry by late afternoon/evening, roughly low-20s °C easing later, precipitation probability below 5% around 17:00-18:00; winds easing.
- Exact end-relative stadium wind vector was not recovered to a directional standard. Weather therefore does **not** create a signed goals/corners adjustment.

#### Frozen regulation goal distribution

Explicit `UNVALIDATED_SUBJECTIVE` scenario mixture, frozen before querying 0.5 / 2.5:

| Scenario | Weight | Forest mean | Coventry mean | 1H goal mean |
|---|---:|---:|---:|---:|
| Forest control / Coventry suppressed | 0.30 | 1.9 | 0.5 | 1.00 |
| Balanced Forest edge | 0.32 | 1.8 | 0.8 | 1.15 |
| Coventry conversion / close game | 0.18 | 1.4 | 1.2 | 1.10 |
| Open transition / set-piece tail | 0.20 | 2.6 | 1.5 | 1.65 |

- **Forest goal centre:** ~1.92
- **Coventry goal centre:** ~0.92
- **Projected combined total:** **2.84**
- Mixture total SD: ~**1.80 goals**
- Representative central score: **Forest 2-1 Coventry**.
- Regulation result: Forest win ~0.606, draw ~0.215, Coventry win ~0.178; **Forest or Draw ~0.822**.
- 1H Over 0.5 ~**0.690**.
- Full-match Over 2.5 ~**0.525** / Under 2.5 ~0.475.

#### Mandatory total ceiling/floor audit

| Team | Floor | Centre | Ordinary high | Tail ceiling |
|---|---:|---:|---:|---:|
| Nottingham Forest | 0-1 | ~1.9 | 2-3 | 4+ |
| Coventry City | 0 | ~0.9 | 1-2 | 3+ |

Defensive allowance:
- Forest central allowance ~0.8-1.0; ordinary high concession ~1-2 if Coventry's current xG under-finishing corrects.
- Coventry central allowance ~1.8-2.0; ordinary high concession ~2-3 through set-piece/transition or repeated box entries.

**Projected total:** 2.84  
**Supplied total:** 2.5  
**Gap:** +0.34 goals  
**Width:** ~1.80 goals  
**Normalised gap:** ~0.19 SD  
**Assessment:** **CLOSE TO PROJECTION / WEAK MAIN-TOTAL EDGE**  
**Preferred main side:** **Over 2.5 (~52.5%)**, only marginally.  
**Safer model alternate Over target:** **Over 1.5 (~75.7%)**.  
**Safer model alternate Under target:** **Under 3.5 (~68.4%)**.  
Operator availability of alternates is not asserted.

Threshold budget:
- Forest centre 1.9 + Coventry centre 0.9 = ~2.8.
- Forest ordinary high 2-3 + Coventry centre ~1 = 3-4 -> Over 2.5.
- Forest centre ~2 + Coventry ordinary high 1-2 = 3-4 -> Over 2.5.
- Forest 1 + Coventry 0-1 = 1-2 -> Under 2.5.
- Multiple ordinary states fall on both sides, so 2.5 is a weak directional total.

#### Corner process

Early-season direct data:
- Forest corners for: **2.75 per PL match** (11 in four).
- Coventry corners for: **4.5 per match** (18 in four); Coventry have also allowed about 4.5 per match.
- Forest's early sample has conceded materially more corners than it wins; Coventry's likely trailing state can preserve away-corner volume.
- Separate corner scenario centre: approximately **8.9 total corners**, with overdispersed width around 3-3.5.
- **Model target: Under 11.5 total corners (90 min) ~0.79 `UNVALIDATED_SUBJECTIVE`.**
- This is a self-selected model target; operator availability is not asserted.
- Settlement route pre-registered: Premier League official match stats/field-owner corner count where exposed, with independent structured corroboration under CR-4. If the exact derivative field cannot be verified across the required lineages, settlement remains unresolved.

#### Ranked picks

| Rank | Selection | UNVALIDATED_SUBJECTIVE estimate | Evidence |
|---:|---|---:|---|
| **1** | **Nottingham Forest or Draw (1X), 90 min** | **~0.82** | **MEDIUM-LOW / FORCED RANK — XI/bench cap** |
| **2** | **Total corners UNDER 11.5, 90 min — model target** | **~0.79** | **LOW-MEDIUM / derivative-source cap** |
| **3** | **Full-match OVER 1.5 goals — model alternate target** | **~0.76** | **MEDIUM-LOW / full-game participant cap** |
| **4** | **1st Half OVER 0.5 goals** | **~0.69** | **MEDIUM-LOW** |
| **5** | **Coventry team total UNDER 1.5 goals — model target** | **~0.76 raw; lower ordinal due full-game participant/role uncertainty** | **LOW-MEDIUM / FORCED RANK** |

**Important ranking note:** the fifth row's raw marginal is high but its participant-sensitive full-game team-total mechanism is less completely verified than the phase row; it is retained as a forced-rank research pick rather than presented as a stronger clean forecast. The supplied full-match **Over 2.5 (~52.5%)** is the preferred side of that forced pair but is **not strong enough to enter the best five**.

#### Potential winner

- **Nottingham Forest — ~0.61**
- Draw ~0.22
- Coventry ~0.18
- Winner lean is moderate, not dominant; Coventry's finishing drought is aggressively shrunk and their opening opposition has been unusually strong.

#### Main kill paths

- Rank #1 failure: Coventry finally convert their underlying chance creation while Forest's weakened centre-back availability creates transition/set-piece vulnerability.
- Corner Under failure: early Forest lead forces Coventry into prolonged wing/cross pressure, or repeated blocks/clearances generate a 12+ corner tail.
- 1H Over failure: Forest dominate territory without creating clean shots and Coventry maintain a low block through halftime.
- Main Over 2.5 failure: Forest control possession/territory but convert only once while Coventry's missing forwards fail to turn xG into goals, producing 1-0/2-0.
- Main Under 2.5 failure: Coventry's finishing regresses toward their xG while Forest exploit Coventry's defensive/set-piece problems, producing 2-1/3-1.

#### Verification/source block

| Source | Role | Quality |
|---|---|---|
| Premier League official fixture schedule / live fixture feed | event identity, date/time, state | PRIMARY / FIELD OWNER |
| Reuters (17 Sep) | Coventry current regime and Lampard context | HIGH-QUALITY INDEPENDENT |
| Guardian weekend team news/current match reporting | availability and current context | HIGH-QUALITY INDEPENDENT |
| StatMuse current EPL stats | xG/shots/SOT/corners current four-match diagnostics | STRUCTURED SECONDARY |
| Met Office | venue-area match-window weather | GOVERNMENT WEATHER OWNER |
| Sports Research Drive | method, soccer rules, CR-4, source firewall, total ceiling/floor controls | GOVERNING METHODOLOGY |


#### Late pre-kickoff lineup refresh — 20 Sep 2026, ~02:28 AEST

TNT Sports' exact-match live page published the match teamsheet before kickoff:

- **Forest XI:** Sels; Murillo, Diomande, Jair Cunha; Neco Williams, Xaver Schlager, James McAtee, Daniel Muñoz; Morgan Gibbs-White, Dan Ndoye; Liam Delap.
- **Forest bench:** Ola Aina, Nicolás Domínguez, Callum Hudson-Odoi, John Victor, Igor Jesus, Luca Netz, Ibrahim Sangaré, Chris Wood, Ryan Yates.
- **Coventry XI:** Carl Rushworth; Stephen Mfuni, Bobby Thomas, Ethan Pinnock; Jay Dasilva, Matt Grimes, Caleb Yirenkyi, Jack Rudoni; Ephron Mason-Clark, Frank Onyeka; Brandon Thomas-Asante.
- **Coventry bench:** Dan Bentley, Sidiki Cherif, Bassirou Gboho, Gustavo Hamer, Joel Latibeaudiere, Tatsuhiro Sakamoto, Ellis Simms, Loum Tchaouna, Victor Torp.

The lineup is consistent with the frozen scenario tree: Jair Cunha returns for Forest; Milenkovic/Savona remain absent; Awoniyi remains absent for Coventry. No unsupported signed goal adjustment is applied and **the ranking/distribution remain unchanged**. Because this exact teamsheet was recovered from one high-quality secondary lineage rather than two independent lineages or the field owner, participant state remains evidence-capped rather than upgraded to a full CR-4 field-owner handshake.


#### Integrity flags

- `CONFIRMED_XI_BENCH_NOT_RECOVERED_TO_GATE_STANDARD`
- `EARLY_SEASON_FOUR_MATCH_SAMPLE`
- `COVENTRY_FINISHING_DROUGHT_SHRUNK`
- `CORNER_DERIVATIVE_PROVIDER_REQUIRES_SETTLEMENT_RECHECK`
- `CITY_GROUND_EXACT_WIND_VECTOR_NOT_VERIFIED`
- `NO_MARKET_ODDS_TIPSTER_FANTASY_DFS_INPUT`
- **Current settlement status:** `UNSETTLED — PREGAME AT FREEZE / NO RETROSPECTIVE`.

---

#### Settlement and retrospective — 20 Sep 2026 AEST

- **Final status:** `SETTLED — FINAL`.
- **Verified final:** **Coventry City 1–0 Nottingham Forest**; **HT 0–0**; Jay Dasilva 55'.
- **Terminal-state gate:** **PASS.** The Premier League structured event record marks the fixture `Complete`; Reuters reports Coventry's 1–0 win; and Sky Sports carries `FT` at the City Ground with the same result and scorer.
- **Original card preserved:** the pre-game probabilities, rankings and reasoning above remain unchanged.

##### A. Pick-by-pick settlement

| Rank | Frozen selection | Final target | Result |
|---:|---|---:|---|
| **1** | **Nottingham Forest or Draw (1X), 90 min** | Coventry won 1–0 | **LOSS** |
| **2** | **Total corners UNDER 11.5, 90 min** | Final research-grade count **Forest 6–2 Coventry = 8** | **WIN** |
| **3** | **Full-match OVER 1.5 goals** | 1 goal | **LOSS** |
| **4** | **1st Half OVER 0.5 goals** | HT 0–0 | **LOSS** |
| **5** | **Coventry team total UNDER 1.5 goals** | Coventry 1 | **WIN** |
| — | Projected winner: **Nottingham Forest** | Coventry won | **LOSS** |

**Supplied full-match O/U:** preferred **Over 2.5 (~52.5%) = LOSS**; Under 2.5 = WIN.  
**Supplied first-half O/U:** preferred **Over 0.5 = LOSS**.  
**Top-of-list diagnostics:** Rank #1 = **LOSS**; Rank #2 = **WIN**; Wins@2 = **1/2**; Hit@2 = **YES**; both top two won = **NO**; binary NDCG@2 ≈ **0.631**.  
**TOP_OU_REVIEW:** triggered for the highest-ranked goal O/U / alternate-goal row that failed; the supplied 1H Over 0.5 and supplied full-match Over 2.5 are also reviewed.

##### B. Actual game process

Coventry's winner came in the **55th minute**, when goalkeeper Carl Rushworth's long pass found Jay Dasilva, who finished past Matz Sels. Forest dominated territory and shot volume but failed to turn it into goals. Sky Sports records **14 Forest attempts in the first half** and **20 combined first-half attempts with no goal**. Final structured records show roughly **24 Forest shots to 10 Coventry**, only **3 on target each**, and around **63% Forest possession**.

Forest also had a late Igor Jesus equaliser disallowed after VAR review, and Bobby Thomas cleared another Forest effort off the line. Those incidents show genuine realised variance around a low-scoring state, but they do not erase the underlying forecasting issue: the game produced much less effective finishing than the pre-game 2.84-goal centre implied.

##### C. Mandatory Rank-1 failure review — Forest or Draw (1X)

**Why it ranked first.** The frozen result tree had Forest ~60.6%, draw ~21.5%, Coventry ~17.8%, making 1X roughly 82%. The rationale was Forest's home/quality baseline plus Coventry's 0-goal, 0-point start, while still shrinking Coventry's finishing drought.

**Was the placement genuinely supported?** The **direction was defensible**, but **~82% was too numerically assertive for the evidence state**. Only four current league matches existed, final participant confirmation was source-capped, Forest were missing important defenders, and Coventry's chance creation was materially better than their zero goals suggested.

**Did another pick deserve Rank #1 on frozen information?** Corners Under 11.5 had a similar raw marginal (~79%) but a weaker derivative-source lane. It was therefore reasonable not to force the corner row above 1X. The lesson is not "the winning pick should have been first"; it is that the **three-point probability gap between 1X and the corner Under was not robust enough to justify treating 1X as substantially safer**.

**What caused the failure?** Coventry's away-win branch was under-massed. The card correctly noted Coventry's difficult opening schedule and positive chance creation, but the final result distribution still compressed that information into only ~18% away-win mass. Forest's home attacking floor was also too optimistic.

**Failure classification:** **early-season sparse-sample uncertainty + result-tail allocation**, mainly an **execution issue under existing controls** rather than a missing rule.

##### D. Goal O/U reviews

**1st Half Over 0.5 — LOSS.** This was not a quiet half: there were **20 attempts**, with Forest taking 14. The failure came through **conversion/shot quality**, not lack of attacking activity. That distinction matters. A phase-goal model cannot use shot volume alone as a proxy for goal probability; shots on target, box quality and keeper/defensive blocking must remain separate.

**Full-match Over 1.5 — LOSS / supplied Over 2.5 — LOSS.** The frozen combined centre was **2.84**, but the game finished at one goal. Forest generated large shot volume but only three shots on target and no legal goal. Coventry scored once from a direct long-ball transition. The model placed too much mass on Forest converting its territorial advantage into 1–3 goals.

The pre-game card had already identified 1–0/2–0 as the primary Over-2.5 failure family, but it did not give enough weight to the broader state **"Forest have lots of attempts but poor shot quality / blocked shots / weak finishing"**. Forest's early-season home scoring record was also a knowable warning: the result left them still without a home goal in the new league campaign.

**Smallest justified future change:** when an early-season soccer side has high shot volume but weak home conversion, explicitly separate **shot count → shots in box / big chances → shots on target → goals** before raising the scoring centre. Do not create a permanent Under bias from one match.

##### E. Corner settlement and source conflict

Three completed structured records — PlaymakerStats, OFStats and MyKhel — report **Forest 6, Coventry 2 = 8 corners**, so Under 11.5 wins. Playmaker's final chronology specifically records a **90+6 Forest corner** immediately before the final whistle.

A Sporting Life stats snapshot shows **5–2 corners** and an obviously malformed `90+163'` state while its commentary is incomplete. It is therefore treated as a **stale/incomplete snapshot**, not a terminal derivative source. It is preserved as a source-quality warning rather than silently harmonised.

Even if the stale 5–2 value were retained as a raw conflicting value, **both 7 and 8 total corners settle Under 11.5**. The research result is therefore threshold-invariant; operator-specific action remains separate because no operator rules were supplied.

##### F. What went right

- **Corners Under 11.5 won** and the model centre of ~8.9 was close to the final research-grade count of 8.
- **Coventry team Under 1.5 won**; the card correctly avoided assuming Coventry's prior zero goals meant they could not score at all.
- The pre-game analysis **shrunk Coventry's finishing drought instead of treating zero goals as a stable rate**. Coventry scored once, which is consistent with that methodological choice.
- The late teamsheet refresh was accurate: the starting XIs and benches recovered pre-kick matched the final team records.
- Weather was correctly treated as non-directional.

##### G. What went wrong / blind spots

- Forest's home attacking floor and conversion rate were too high relative to the observed early-season home evidence.
- Coventry's upset branch was acknowledged but underweighted.
- The goal distribution needed a stronger **high-shot / low-quality / low-conversion** state.
- A single secondary lineup lineage before kickoff prevented a full CR-4 participant upgrade; this was correctly disclosed.
- Derivative corner providers can remain stale through full time, so terminal chronology matters as much as the displayed stat table.

##### H. Source audit

| Source | Settlement / retrospective contribution | Disposition |
|---|---|---|
| Premier League structured event record, game `72221288` | `Complete`, Forest 0–1 Coventry | **FIELD-OWNER STRUCTURED EVENT LINEAGE** |
| Reuters — `https://www.reuters.com/sports/soccer/lampards-coventry-earn-landmark-first-premier-league-win-25-years-2026-09-19/` | Independent final, Dasilva 55', VAR-disallowed Forest equaliser | **HIGH-QUALITY INDEPENDENT** |
| Sky Sports — `https://www.skysports.com/football/nottingham-forest-vs-coventry-city/report/559492` | `FT`, final, teams, first-half 20-shot process, match chronology | **HIGH-QUALITY INDEPENDENT** |
| PlaymakerStats — `https://www.playmakerstats.com/live/2026-09-19-nottingham-forest-coventry-city/12253137` | Final 0–1, HT 0–0, **corners 6–2**, 90+6 final corner, shots/xG | **STRUCTURED DERIVATIVE** |
| OFStats — `https://ofstats.com/matches/view/nottingham-forest-coventry-city-2026-09-19` | Finished 0–1; **corners 6–2** | **STRUCTURED DERIVATIVE** |
| MyKhel match centre | 0–1, **corners 6–2**, final lineups/statistics | **STRUCTURED SECONDARY** |
| Sporting Life exact-match stats | Stale **5–2** corner snapshot with malformed `90+163'` state | **EXCLUDED FROM FINAL DERIVATIVE COUNT; SOURCE-STATE WARNING** |

No structured corner source is promoted to permanent field-owner status from this one case.

##### I. Rule / learning disposition

| Finding | Future treatment | Proposed home |
|---|---|---|
| High shot volume can coexist with a goalless half/full-game suppression | Require shot-quality/on-target/box-chance branch before translating volume into goals | `RULES_SOCCER.md` execution clarification |
| Sparse four-match result tree gave too little Coventry away-win tail | Widen early-season result families; no ad-hoc favourite penalty | `RULES_SOCCER.md` / `LEARNING_REGISTER.md` observation |
| Forest home scoring weakness was knowable but should not become a raw streak coefficient | Use home-specific process branch, not result streak weighting | `RULES_SOCCER.md` |
| Live derivative providers can omit late stoppage-time events | Require terminal timestamp/chronology before derivative settlement | `SOURCES.md` / `DATA_SOURCE_REGISTER.md` |

**Algorithm disposition:** **NO NEW PERMANENT FORECAST WEIGHT.** The failures reinforce existing sparse-sample, conversion-chain and source-state controls. A formal rule change would require recurrence/prospective evidence.

- **Status:** **SETTLED / RETROSPECTIVE COMPLETE**.

## 4. General Learnings, Rule Changes, Observations, and New Sources

### 20 Sep 2026 settlement batch — P-472 / P-473

1. **P-472 total-tree execution failure:** the American-football card did not include a genuine mutual-suppression / poor-drive-finishing branch even though the active ceiling-floor control requires one. The 36-point final therefore reinforces an existing control rather than creating a new Under coefficient.
2. **P-472 margin-tail lesson:** Coastal +4.5 lost to a late special-teams short field after a 15–14 game state. `AM-B4` already owns this mechanism; future margin trees must allocate it explicitly rather than merely mention it.
3. **P-473 result-tail lesson:** Coventry's positive chance creation and difficult opening schedule were acknowledged, but the away-win family was still only ~18%. Early-season result distributions need wider tail representation when observed goals materially understate underlying chance creation.
4. **P-473 goal-conversion lesson:** 20 first-half attempts still produced 0 goals. Shot volume is not goal probability; soccer phase/full totals must keep shot quality, shots on target, blocked attempts, box chances and finishing separate.
5. **Derivative source-state lesson:** the P-473 corner field exposed a stale live-stat snapshot. Final derivative settlement should verify terminal chronology, not just a stats table. Playmaker's 90+6 corner explains the 5-to-6 Forest corner revision.
6. **No forecast-weight promotion:** two events are insufficient for a new signed rule. These are execution/source-process reinforcements under the existing controls.


### 4.1 Cross-sport learnings

1. **A known kill path must affect the ordinal, not merely appear in prose.** P-455 is the clearest example: Singer’s current command/HR collapse was explicitly named as the failure path for Cincinnati +1.5, then occurred almost exactly. A forecast has not fully used information just because the risk was written down; the branch must carry enough mass in the joint object to change the ranking when warranted.
2. **Phase and full-event markets require conditional linkage, not directional copying.** P-452’s powerplay Over won while the 20-over Under lost; P-456’s 1H Under 1.5 won while the tighter 1H Under 0.5 lost. Phase direction, full-event direction and sibling thresholds are separate queries against one coherent distribution.
3. **Integer boundaries must retain push mass.** P-455 finished at exactly 10 runs, so both Over 10.0 and Under 10.0 pushed. A binary-only grading would have been wrong.
4. **Bench/substitution exposure can decide the full-event state.** P-454’s winning goal was created by one Brøndby substitute and scored by another. This supports the existing bench-completeness control; it does not by itself justify a new coefficient.
5. **Exact-event source ownership outranks generic profile metadata.** P-456’s venue was ultimately Benito Villamarín. The pre-game resolution to La Cartuja demonstrates a source-priority execution failure even where both records were “official-looking”.
6. **Result success and process quality are distinct.** P-454 and P-456 produced very strong row outcomes, but that does not validate every probability, source choice or underlying assumption. Conversely, P-455’s wrong Rank #1 did not make its winner direction or Singer diagnosis wrong.
7. **No five-event retrospective warrants a universal signed rule.** All proposed changes below remain process clarifications or candidate tests unless already required by the governing method.

### 4.2 Sport-specific learnings

**Cricket**
- When a phase market and a full-innings market concern the same batting innings, the full-innings distribution should be printed conditionally on low/central/high phase states. P-452 shows why an extreme first six overs can dominate a high full-innings threshold even if middle-overs slowdown is correctly anticipated.
- Direct same-venue/current-regime phase comparables remain high-value, but they should not be extrapolated linearly to the full innings.

**Baseball**
- A generic run-line one-run-band identity is descriptive geometry, not a substitute for an event-specific separation budget. P-455 shows that an extreme current-regime starter failure can materially reshape 2+ run margin probability.
- Starter uncertainty must be separated from opponent contribution. P-455 had a severe Singer failure yet only 10 total runs because Cincinnati contributed two; P-453’s Over arrived through a different allocation.
- Historical pitcher-vs-opponent success should be explicitly mixed against current-regime deterioration rather than allowed to dominate by reputation.

**Soccer**
- Full bench depth remains material for late-state goals in cup matches. P-454 supports, rather than changes, the existing `G14.2` control.
- Exact-event governing-body metadata should control venue identity. Generic current-stadium or club-profile fields are fallback context only.
- Derivative fields such as corners need field-specific settlement routes. Core score can be official while the corner field remains secondary-grade.

### 4.3 Potential rule changes / candidate tests

| Candidate | Proposed change | Status |
|---|---|---|
| `C-CRIC-PHASE-CONDITIONAL-INNINGS` | For cards containing both phase and full-innings targets on one batting unit, print full-innings W/P/L states conditional on low/central/high phase outcomes. | **CANDIDATE — prospective testing required** |
| `C-MLB-GENERIC-RUNLINE-VS-EVENT-SEPARATION` | Track cases where league one-run geometry conflicts with a strong event-specific starter/relief separation branch; test whether explicit phase separation improves ranking. | **CANDIDATE — no live weight change** |
| Exact-event venue ownership clarification | State explicitly that governing-body/exact-event match metadata outranks generic club-profile stadium metadata. | **Process clarification; likely existing hierarchy already implies this. No new predictive rule.** |
| Accessible derivative-route check | Before ranking a niche stat, confirm at least one actually retrievable settlement route at issue time, not only a provider family/slug. | **Process/source candidate; evaluate against current `G10.2/G36` before adding anything new.** |

### 4.4 Algorithm improvements

- Convert every important prose kill path into a weighted outcome-state branch before ranking.
- For linked phase/full markets, use conditional trees or a joint state object rather than independent marginal narratives.
- For margin markets, preserve generic historical geometry as a prior/reference but allow event-specific separation budgets to move the conditional branch masses.
- For top-two diagnostics, explicitly label shared dependence. A high Hit@2 generated by two rows sharing one causal thesis is not equivalent to diversified coverage.
- Preserve three-way W/P/L vectors for integer thresholds and avoid scoring pushes as wins or losses.

### 4.5 Source improvements

- **Cricket:** ICC/board source first for identity/result; structured scorecard fallback for exact powerplay/over state when the official narrative lacks the field.
- **MLB:** official Gameday/scoreboard and final lineup archive remain first choice; secondary confirmed lineups may be used only with explicit status before official publication.
- **Danish cup corners:** the match result is official via DBU/Vejle, but the 3-7 corner field was only recovered from corroborating structured secondary sources in this pass. Do not promote those providers to field-owner status.
- **Getafe exact-match pages:** demonstrated rich exact-event fields including corners, shots and substitutions. Add as a **candidate source lane**, subject to repeated coverage/definition checks.
- **Venue identity:** RFEF/exact-event match record should be opened whenever a LaLiga venue field conflicts with a club profile or cached match shell.

### 4.6 Data-quality observations

- `PREDICTION_LOG_COMBINED_4.md` contains no P-452–P-457 card, so no canonical collision was found in this settlement pass.
- P-454’s pre-registered Sofascore generic slug proved unstable and surfaced an older league meeting in direct retrieval; exact fixture/date identity must be checked after opening a derivative provider.
- P-456’s pre-game venue conflict was resolved incorrectly. This is retained as an audit finding rather than rewritten out of the card.
- P-455 demonstrates why a recorded push probability is not optional metadata at an integer line.
- Post-match recovery of an official lineup cannot be used to claim that lineup was publicly available before the forecast cutoff.

### 4.7 Recurring blind spots

- Known risk recorded in prose but insufficiently represented in the numerical/joint branch.
- Participant/bench completeness close to kickoff.
- Derivative-stat provider identity/access.
- Current-regime evidence competing with longer-run/historical priors.
- Source records that are official at the organization level but not field-owning for the exact event/field.

### 4.8 Items requiring more evidence before formal rules

- Whether conditional phase-to-full-innings modeling materially improves cricket ranking out of sample.
- Whether event-specific starter deterioration should systematically alter the MLB one-run band rather than only the winner centre/separation budget.
- Whether Getafe/club exact-match pages have stable enough historical/current coverage to be a reusable LaLiga derivative lane.
- Whether a pre-issue “accessible route smoke test” adds enough reliability beyond existing `G10.2/G36` controls to justify another explicit gate.


### 4.9 2026-09-19 P-458–P-462 settlement-batch additions

**Cross-sport learnings**
- P-458, P-459 and P-461 all repeat the same execution issue already covered by `G-L1`: a kill path can be correctly *named* and still be analytically underused if it does not receive enough probability mass to affect the ordinal. The repeated issue supports stricter execution of the existing control; it does not justify a new signed predictive rule.
- Top-two dependence matters. P-461's Over 20.5 and Maristany +3.5 shared one “competitive match” driver and failed together. P-458's +1.5 and Over also depended on a narrow score-shape corridor. Print shared-driver failure states before freezing top-two ranks.
- A correct component read does not guarantee the winner: P-460's Eppler starter thesis was excellent while the Rakuten winner call failed. Translation from a subcomponent to the final endpoint needs explicit conversion states.

**Sport-specific learnings**
- **NPB/baseball:** a tied low-total game can jump directly to a 2-run final margin on one home run. Derive the NPB 1.5 margin band prospectively and represent terminal two-run walk-off states in the separation tree.
- **CPBL/baseball:** starter dominance must be combined with run support, home-last-bat and starter-continuation/bullpen transition states. The missing CPBL margin band remains a data gap.
- **AFL:** the same type of late clearance/inside-50 takeover that was identified pre-game defeated Sydney +11.5 by 0.5. Track Q4 durability/separation recurrence before any formal change.
- **Tennis:** same-surface recent H2H can be outweighed by a changed workload/rest regime. Rebuild straight-set/three-set mass after a walkover or long prior round; do not merely describe the difference.
- **Soccer:** P-462 supports the current requirement for a **current early-chance mechanism** before ranking 1H Over 0.5, and supports a separate trailing-state corner process.

**Potential rule changes / candidates**
- `C-NPB-1P5-BAND`: derive NPB one-run/2+ winning-margin identity from official completed games. **DATA TASK / CANDIDATE; no forecast weight now.**
- `C-CPBL-1P5-BAND`: derive CPBL one-run/2+ winning-margin identity from official completed games. **DATA TASK / CANDIDATE; no forecast weight now.**
- `C-AFL-Q4-DURABILITY`: track cards where current-regime fourth-quarter clearance/I50 strength is a named margin kill path and test whether explicit phase mass improves handicap ranking. **CANDIDATE; more evidence required.**
- No new tennis rule is proposed; existing scoreline-coherence and weighted-branch controls already cover the P-461 miss.

**Algorithm improvements**
- For baseball winner cards, print `starter phase -> post-starter/continuation phase -> home-last-bat/extras` conversion rather than treating a starter edge as a direct win edge.
- For tennis, print the straight-set/three-set mixture **after** rest/workload adjustments and show how each leading score family settles the handicap and total simultaneously.
- For AFL margins, explicitly allocate probability to fourth-quarter separation branches when current personnel/clearance evidence supports them.
- For top-two rows in every sport, state whether both fail under one shared driver and ensure that branch's mass is visible in the joint object.

**Source improvements**
- **NPB:** exact official game pages are strong settlement sources and include lineups, pitchers, inning score and home runs.
- **CPBL:** keep official box/advanced pages as field-owner routes, but retain CNA as a strong causal fallback when CPBL crawl hydration lags.
- **AFL:** AFL.com.au and club reports provided final, goalkickers and phase narrative cleanly.
- **WTA:** exact live pages can remain cache-stale after a match; require a second high-quality final source before settlement when this occurs.
- **CSL corners:** exact-event Chinese secondary reports provided the 4-7 corner field, but this single success is not enough to promote the provider to field-owner grade.

**Data-quality observations**
- Fresh `PREDICTION_LOG_COMBINED_4.md` reconciliation still shows no P-457–P-462 collisions.
- P-457 demonstrates source-latency discipline and fallback routing: withhold settlement while strong routes conflict, then complete it once an authorised high-quality structured final (Cricbuzz/ESPNcricinfo class) is stable.
- P-461's official WTA page had stale/suspended crawl state even after a high-quality secondary confirmed the final.

**Recurring blind spots**
- Named kill path without enough numeric/branch mass.
- Translating player/starter quality directly to final winner without enough endpoint-conversion modelling.
- Correlated top-two rows presented as if they were diversified.
- Derivative stat fields whose final source is weaker than the core result source.

**Items requiring more evidence before formal rules**
- Whether NPB/CPBL league-specific margin bands materially improve future handicap ordering out of sample.
- Whether AFL Q4 durability should become a mandatory explicit margin component beyond the existing phase process.
- Whether workload-adjusted rematch trees consistently outperform simple recent-H2H weighting in tennis.
- Whether the exact-event CSL secondary corner source has stable enough coverage/definitions for promotion.

No permanent forecast weight, calibration claim or global Over/Under preference is created from this settlement batch.

### 4.10 P-457 final-settlement additions

**Cricket / cross-sport learning**
- P-457 is the cleanest current example of the existing “kill path must carry mass” problem: the frozen card explicitly described the both-fail state as **a cautious first five followed by a large acceleration to 310+**, assigned it 0.13, and that state occurred. This strengthens execution of `G-L1`; it does not establish that 0.13 was statistically miscalibrated from one observation.
- P-457 also strengthens `C-CRIC-PHASE-CONDITIONAL-INNINGS`. A five-over Under and a 50-over Over both won: **29/0 after five → 356/6 after fifty**. The full-innings tree should be solved conditionally on low/central/high early-phase states.
- Same-series comparators need a **conversion-quality annotation**. Australia's prior 294/8 contained multiple top/middle failures; treating 294 mainly as “below 309.5” understated the fact that normal conversion could create a much higher ceiling.
- Venue averages should be shrunk against current opponent-adjusted team strength. Harare's low historical baseline remained relevant, but it was too dominant against an elite Australian batting unit.

**Source improvement**
- By explicit user instruction, **ESPNcricinfo/Cricbuzz are approved structured cricket fallback sources** for live state, ball-by-ball and scorecards when official/board feeds are stale. Official/field-owner records remain preferred when current.
- Exact phase settlement must still use the precise legal-ball boundary. P-457 demonstrates why a six-over score (**35/0**) cannot be substituted for a five-over contract (**29/0**).

**No permanent signed rule:** do not convert this result into a blanket Australia Over, Harare Over or early-Under rule. The warranted changes are conditional-distribution and source-process improvements only.
---

### 4.11 P-463–P-468 settlement-batch additions — 19 Sep 2026

#### Cross-sport learnings

1. **Close totals need component budgets, not just central means.** P-465 (188 vs 187.5) and P-467 (8 vs 7.5) both lost their preferred Unders by exactly 0.5, and both failed through a one-sided offensive-high state rather than a symmetric shootout. This directly supports the prospective floor/centre/ordinary-high audit already added to this running log.
2. **One-sided high + opponent floor/centre is a mandatory total stress state.** A total can go Over when only one side scores heavily. P-467 is the clearest example: Texas 7, Toronto 1.
3. **Top-two robustness is more important than narrative agreement.** P-467 Rank #1 failed but Rank #2 Texas +1.5 preserved Hit@2. P-463 likewise showed a cushion could be more robust than the projected winner.
4. **Successful rows can be highly dependent.** P-464's Brewers ML and Orioles +1.5 both won in a one-run Brewers victory; P-466's five winning rows largely shared the same Racing-territory mechanism. Do not count those as independent evidence of model quality.

#### Baseball-specific learnings

- **Starter state must include recent stuff/command, not only ERA/FIP/K season strength.** MLB's postgame report shows Cease's velocity decline existed in his prior starts before P-467. The card did not document a same-day velocity audit.
- **Defensive replacement chains matter.** Giménez's known absence moved Clement to shortstop; Clement's throwing error materially contributed to Texas' big inning. Availability should propagate into defensive run prevention as well as batting.
- P-463 and P-467 together strengthen, but do not yet statistically validate, a prospective audit of velocity/zone/walk process for starter-driven MLB ranks.

#### Basketball-specific learnings

- **Favourite scoring ceiling must survive a blowout branch.** P-465 lost the Under because Indiana reached 103 while Toronto scored an ordinary 85.
- **Turnover pressure is bidirectional for totals.** P-468's 21 Portland turnovers suppressed Portland half-court scoring but also generated Golden State transition opportunities. Here the asymmetric effect still supported Under + favourite cover; future models must represent both signs.

#### Soccer-specific learnings

- Racing–Sarmiento validates the usefulness of territory/chance creation for team goals and corners, but it does not justify treating five correlated wins as independent confirmations.
- Official schedule identity must control time conversion. AFA's 21:15 ART start corrected the earlier user-estimated AEST time.
- The 7-2 corner settlement remains secondary-source supported; one successful recovery does **not** promote the provider.

#### Potential rule changes / algorithm improvements

| Candidate | Evidence from this batch | Status |
|---|---|---|
| Require recent pitch-velocity + strike/zone/BB process audit when a starting pitcher materially drives Rank #1 | P-467 direct; P-463 command-tail reinforcement | **Strong candidate — test prospectively before formal numerical weighting** |
| Propagate position-player absences through defensive-position/run-prevention branches | P-467 Giménez → Clement at SS | **Candidate mechanism extension** |
| Explicitly test `A-high+B-centre`, `A-centre+B-high`, `A-high+B-floor`, `A-floor+B-high` before ranking totals | P-465, P-467 | **Already implemented prospectively in local/mini-log ceiling audit; retain** |
| Keep correlation accounting for same-game ranked rows | P-464, P-466 | Existing rule; reinforce reporting |

#### Source improvements

- MLB exact game feed/Statcast should be the preferred route for starter velocity/command state and final lineups.
- Current v4.2 prohibition on RotoWire/RotoGrinders/FPTrack is reaffirmed; their presence in older cards is retained only as immutable historical evidence.
- WNBA/NBL official gamebooks, injury reports and club availability should outrank projected-five aggregators.
- AFA/LPF field-owner sources remain preferred for schedule, result and lineups; exact corner statistics need a stronger field-owner route before provider promotion.

#### Data-quality observations

- A final result can be authoritative while a derivative statistic such as corners has lower source quality; settlement grade should be field-specific.
- Schedule-time errors can make an event look unresolved when it is already complete. Always reconcile local time against the governing-body fixture.
- Postgame reports may reveal that a mechanism existed pregame (Cease velocity decline), but the retrospective must distinguish “could have been retrieved before the game” from information learned only after the result.

#### Recurring blind spots

- Official lineup publication lag near event start.
- Overreliance on central totals when the threshold lies inside the ordinary score corridor.
- Participant absences modelled offensively but not defensively.
- Correlated ranked rows being visually mistaken for independent confirmations.

#### Items requiring more evidence before formal rules

- No fixed points/runs adjustment for pitcher velocity loss is authorised.
- No automatic Under/Over switch follows from a close projection.
- No permanent WNBA blowout-compression coefficient follows from P-465/P-468.
- No corner-stat provider is promoted from the Racing–Sarmiento settlement alone.

## 5. Document Update Mapping

The files below remain **read-only in this chat**. These are proposed eventual homes only; no governing/history document was edited.

| Observation / proposed update | Intended Markdown document | Disposition |
|---|---|---|
| P-452 conditional powerplay-to-full-innings branch | `RULES_CRICKET.md`; test manifest in `LEARNING_REGISTER.md` | Candidate only; prospective evidence required |
| P-453 current-regime Harrison weighting vs historical PIT matchup | `RULES_BASEBALL.md` current-regime/mixture guidance; `LEARNING_REGISTER.md` if repeated | Existing controls largely sufficient; no rule change now |
| P-454 substitute-created winning goal supports bench completeness | `RULES_GENERAL.md` / `CONTROLS.md` `G14.2`; `RULES_SOCCER.md` | Existing process control supported; no change |
| P-454 derivative corner route instability | `SOURCES.md`, `DATA_SOURCE_REGISTER.md` | Source-quality observation; no provider promotion |
| P-455 generic run-line identity vs event-specific separation | `RULES_BASEBALL.md`; prospective candidate in `LEARNING_REGISTER.md` | Candidate test only; no coefficient/ordinal change |
| P-455 exact integer push example | `RULES_GENERAL.md` push treatment / settlement examples | Existing rule correctly applied; no change |
| P-456 exact-event venue ownership error | `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, event-identity guidance in `RULES_GENERAL.md` | Process clarification / enforcement note |
| P-456 Getafe exact-match page carries corners + detailed stats | `SOURCES.md`, `DATA_SOURCE_REGISTER.md` | Candidate source lane; verify repeated coverage before promotion |
| P-452–P-456 settlement/retrospective status | `GAME_LOG_STATUS_CURRENT.md` and eventual canonical log reconciliation | Do not edit now; mini-log is current writable staging record |
| This mini-log settlement workflow | `EXTERNAL_LOGGING_WORKFLOW.md` | Reconciliation note only when later imported |
| P-458 NPB +1.5 cushion / Tokyo Dome 5.5 gaps | `BASE_RATES_REGISTER.md`, `DATA_SOURCE_REGISTER.md` | Data-gap candidates only; no guessed rates |
| P-459 AFL 11.5 cushion gap / SCG wind-vector coverage | `BASE_RATES_REGISTER.md`, `DATA_SOURCE_REGISTER.md`, `SOURCES.md` | Data/source-gap candidates only |
| P-459 participant/forward-exposure findings | `RULES_AFL.md`; `LEARNING_REGISTER.md` only if repeated | Existing controls applied; no new rule |

| P-457 slow first five (29/0) followed by 356/6 full innings | `RULES_CRICKET.md`, `LEARNING_REGISTER.md` | Strengthens conditional phase-to-innings candidate; no signed rule |
| P-457 official-feed latency / Cricbuzz-ESPN fallback authorisation | `SOURCES.md`, `DATA_SOURCE_REGISTER.md` | Source-process update candidate; user-authorised fallback when official cricket feed lags |
| P-458 two-run walk-off defeats +1.5 despite 0-0 through eight | `RULES_BASEBALL.md`, `BASE_RATES_REGISTER.md` | Existing weighted-tail control + NPB 1.5 data task; no new signed rule |
| P-459 late Fremantle Q4 separation defeated Sydney +11.5 by 0.5 | `RULES_AFL.md`, `LEARNING_REGISTER.md` | Candidate Q4 durability test only |
| P-460 starter dominance did not convert to Rakuten win | `RULES_BASEBALL.md` / CPBL competition notes | Clarify starter-to-winner conversion branch; CPBL 1.5 band remains data gap |
| P-461 workload/rest changed rematch score-family weights | `RULES_TENNIS.md` | Existing scoreline-coherence control under-executed; no new rule |
| P-462 confirmed XIs + early mechanism + trailing-state corners | `RULES_SOCCER.md`, `SOURCES.md`, `DATA_SOURCE_REGISTER.md` | Existing process supported; corner source remains candidate only |
| P-458–P-462 settlement status | `GAME_LOG_STATUS_CURRENT.md` / eventual canonical reconciliation | Running mini-log updated now; authoritative files remain read-only |

### 5.4 P-463–P-468 settlement-batch mapping — 19 Sep 2026

| Observation / proposed change | Existing Markdown home | Treatment |
|---|---|---|
| Starter velocity/command audit before starter-dominant MLB ranks | `RULES_BASEBALL.md` | Candidate control; prospectively test, no fixed coefficient |
| Defensive-position consequence of player absence | `RULES_BASEBALL.md` participant/replacement chain | Candidate mechanism extension |
| One-sided offensive-high total stress tests | `RULES_GENERAL.md` component-budget section; sport rules | Already covered by prospective ceiling-floor audit; retain explicitly |
| Basketball turnover pressure has opposite total effects | `RULES_BASKETBALL.md` possession/transition chain | Existing mechanism; add retrospective example only |
| Correlated same-game wins are not independent confirmations | `RULES_GENERAL.md`, `SCORING_AND_VALIDATION.md` | Existing control reinforced |
| RotoWire/RotoGrinders/FPTrack historical appearances | `SOURCES.md` | Preserve old evidence; prospectively prohibited |
| Racing corner settlement provider remains secondary | `DATA_SOURCE_REGISTER.md`, `SOURCES.md` | Do not promote |
| AFA schedule corrected P-466 Australian-time interpretation | `RULES_GENERAL.md` G0–G6 identity/time gate | Existing rule; field owner controls |
| Current running status P-472 | `GAME_LOG_STATUS_CURRENT.md` / running mini log | Keep unresolved; no retrospective |

**New Markdown document required?** No. All findings fit existing rule, learning, source, status or workflow documents.

---

## 6. Settlement Lists

### Settled logs

1. **P-452** — Afghanistan vs India, 3rd T20I — **SETTLED / RETROSPECTIVE COMPLETE**
2. **P-453** — Milwaukee Brewers @ Pittsburgh Pirates — **SETTLED / RETROSPECTIVE COMPLETE**
3. **P-454** — Vejle Boldklub vs Brøndby IF — **SETTLED / RETROSPECTIVE COMPLETE**
4. **P-455** — Los Angeles Dodgers @ Cincinnati Reds — **SETTLED / RETROSPECTIVE COMPLETE**
5. **P-456** — Real Betis vs Getafe CF — **SETTLED / RETROSPECTIVE COMPLETE**
6. **P-457** — Zimbabwe vs Australia, 2nd ODI — **SETTLED / RETROSPECTIVE COMPLETE**
7. **P-458** — Chunichi Dragons @ Yomiuri Giants — **SETTLED / RETROSPECTIVE COMPLETE**
8. **P-459** — Sydney Swans vs Fremantle Dockers — **SETTLED / RETROSPECTIVE COMPLETE**
9. **P-460** — Rakuten Monkeys @ Fubon Guardians — **SETTLED / RETROSPECTIVE COMPLETE**
10. **P-461** — Clara Burel vs Guiomar Maristany Zuleta De Reales — **SETTLED / RETROSPECTIVE COMPLETE**
11. **P-462** — Zhejiang FC vs Wuhan Three Towns — **SETTLED / RETROSPECTIVE COMPLETE**
12. **P-463** — Chicago Cubs @ Cincinnati Reds — **SETTLED / RETROSPECTIVE COMPLETE**
13. **P-464** — Milwaukee Brewers @ Baltimore Orioles — **SETTLED / RETROSPECTIVE COMPLETE**
14. **P-465** — Indiana Fever @ Toronto Tempo — **SETTLED / RETROSPECTIVE COMPLETE**
15. **P-466** — Racing Club vs Sarmiento — **SETTLED / RETROSPECTIVE COMPLETE**
16. **P-467** — Toronto Blue Jays @ Texas Rangers — **SETTLED / RETROSPECTIVE COMPLETE**
17. **P-468** — Portland Fire @ Golden State Valkyries — **SETTLED / RETROSPECTIVE COMPLETE**
18. **P-469** — Hawthorn vs Brisbane Lions — **SETTLED / RETROSPECTIVE COMPLETE**
19. **P-470** — Saitama Seibu Lions @ Chiba Lotte Marines — **SETTLED / RETROSPECTIVE COMPLETE**
20. **P-471** — Melbourne United vs Adelaide 36ers — **SETTLED / RETROSPECTIVE COMPLETE**
21. **P-472** — Coastal Carolina @ Delaware — **SETTLED / RETROSPECTIVE COMPLETE**
22. **P-473** — Nottingham Forest vs Coventry City — **SETTLED / RETROSPECTIVE COMPLETE**

### Logs still awaiting settlement

**None.**

No mini-log canonical ID was overwritten. The next intended new-event mini-log ID remains **P-474**, subject to fresh reconciliation.

> **Performance status:** all entries remain **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. Settlements are used for methodology, source and process learning only; no ROI/EV/performance claim follows.

# Operational Reference Appendices

## 3. Governing Method / Controls Snapshot

Fresh-read baseline for this mini-log session:

- `METHOD.md` — active method **MDS-2026.09.06-v4.0**; probabilities on ranked rows are `UNVALIDATED_SUBJECTIVE`; ranks derive from the card probabilities; no probability may be called calibrated or validated.
- `PREDICTION_LOG_COMBINED_4.md` — active canonical queue; next ID **P-452** at mini-log creation; carries current cross-sport controls through **G-L24**.
- `RULES_GENERAL.md` — §16 controls current mandatory gate classification, identity/contract/time/participant freeze, source provenance, state handling, coherent contract geometry, and source hierarchy.
- `CONTROLS.md` — compact per-card gate and non-gate hard-rule reference.
- `SOURCES.md` / `DATA_SOURCE_REGISTER.md` — source ownership, field coverage, access state, settlement-route requirements, and source-quality guidance.
- `LEARNING_REGISTER.md` — lesson/prospective-test archive; only promoted controls and relevant active tests may affect current process.
- `EXTERNAL_LOGGING_WORKFLOW.md` — governs mini-log generation, settlement, reconciliation, and eventual promotion/archive workflow.
- Relevant `RULES_<SPORT>.md` and, where applicable, `LEAGUE_RULES_SOCCER.md` / `LEAGUE_RULES_CRICKET.md` must be fresh-read for each event before issuance.

### Current high-priority cross-sport controls carried forward

- Verify exact event, competition, rules era, participants, venue, market contract, phase/horizon, start time, and current state before modelling.
- Use field-owning/official sources for identity, volatile participant facts, live state and finals wherever available.
- A search summary, snippet, model-generated preview, simulated result, tipster article or bookmaker commentary is not decision evidence.
- Market prices/odds do not drive the forecast. Supplied lines define the contracts only.
- Every ranked row must carry an exact-contract `UNVALIDATED_SUBJECTIVE` probability and evidence state.
- Complementary/nested contracts must arise from one coherent event distribution/corridor; preserve push mass on integer lines.
- `FORCED_PAIR` opposite sides are one decision; identify the preferred side.
- Full bench/reserve and coaching/rotation information is required where relevant; `BENCH_NOT_RETRIEVED` blocks a margin/full-game total from Rank #1.
- Outdoor/open-roof events require venue-coordinate, game-window weather/conditions research where material under the sport controls.
- Build explicit outcome-state families and weighted kill paths; probability mass must be coherent with centre/width and exact contract geometry.
- For shared-driver top rows, quantify joint success/failure where the methodology requires it.
- Handicap probabilities must be derived consistently from winner probability and the applicable cushion-band/base-rate treatment; do not assert an incoherent independent handicap probability.
- Pre-register/verify a settlement route for derivative or niche markets before ranking them where the rules require it.
- Do not fabricate missing lineups, injuries, statistics, weather, or settlement fields. Mark missingness explicitly and cap/block affected rows as required.

---

## 4. Source Recording Standard

For every prediction entry, record every material source used with:

| Field | Requirement |
|---|---|
| Source name | Official body/team/league/provider/publication |
| Link / record | Direct URL or exact record identifier where available |
| Field ownership | What the source legitimately controls or contributes |
| Access time | Timestamp of the research check |
| Source state | `OPENED`, `SNIPPET`, `ASSUMED`, blocked/restricted, or other applicable state |
| Contribution | Exact fact(s) used in the prediction |
| Limitations/conflicts | Any stale, partial, secondary, conflicting or unverified aspect |

Primary and structured sources take priority over secondary reporting. Weak sources do not become strong merely because several repeat the same claim.

---

## 5. Document Mapping Register

For every meaningful observation, source discovery, learning, or possible process change, record its eventual home without editing the authoritative files during this mini-log session.

| Update type | Intended document |
|---|---|
| Cross-sport process/control clarification | `RULES_GENERAL.md` and/or `CONTROLS.md`; disposition in `LEARNING_REGISTER.md` if warranted |
| Sport-specific process learning | Relevant `RULES_<SPORT>.md` |
| Competition-specific rules/format/settlement reference | Relevant sport file or `LEAGUE_RULES_SOCCER.md` / `LEAGUE_RULES_CRICKET.md` |
| New/changed research or settlement source | `SOURCES.md` and `DATA_SOURCE_REGISTER.md` |
| Prospective hypothesis requiring testing | `LEARNING_REGISTER.md` as `CANDIDATE` / `TESTING`, not an immediate forecast weight |
| Numerical/base-rate finding | `BASE_RATES_REGISTER.md` and/or numerical program/spec documents if it passes their evidence requirements |
| Mini-log workflow/reconciliation finding | `EXTERNAL_LOGGING_WORKFLOW.md` |
| Canonical-status/queue issue | Active combined log snapshot and `GAME_LOG_STATUS_CURRENT.md` at reconciliation time |
| No existing suitable home | Propose a new `.md` file with a stated purpose; do not create it unless explicitly authorised |

---

## 6. Prediction Entry Template

Each new unsettled event will be appended under Section 1 using the following minimum structure:

### P-### — [Sport / Competition] — [Event]

- **Canonical ID:**
- **Sport / competition:**
- **Event:**
- **Official event ID (if available):**
- **Scheduled start:** venue-local + Australia/Melbourne conversion
- **Game state at issue:**
- **Research cutoff / final refresh:**
- **Method version:** MDS-2026.09.06-v4.0 unless fresh-read authority changes
- **Population status:** PRIMARY_SCORED or EXPLORATORY — NOT SCORED, per current method
- **Supplied contracts / market definitions:**
- **Participant / lineup / bench / coach status:**
- **Injuries / suspensions / rest / rotation:**
- **Venue / environment / weather:**
- **Recent-form and disaggregated evidence:**
- **Head-to-head continuity test:**
- **Sport-native exposure chain:**
- **Joint event object / centre-width / outcome states:**
- **Component or separation budget:**
- **Kill paths / complement decomposition / shared-driver failure state:**
- **Settlement route(s):**

#### Ranked picks

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence state | Forced pair/free | Key rationale | Primary failure path |
|---:|---|---:|---|---|---|---|
| 1 |  |  |  |  |  |  |

- **Projected / potential winner:**
- **Winner endpoint:** regulation / eventual / advance / exact applicable contract
- **Information not confirmed:**
- **Integrity flags:**
- **Current settlement status:** `UNSETTLED — PREGAME` / `LIVE` / other exact state

#### Sources

| Source | Link / record | Accessed | Contribution | Quality / limitation |
|---|---|---|---|---|

#### Document mappings / candidate learnings

| Observation | Proposed home | Status |
|---|---|---|

---

## 7. Running Integrity Notes

- **2026-09-19 settlement pass:** P-457 through P-462 are fully settled with detailed retrospectives. P-457 was completed after the user authorised ESPNcricinfo/Cricbuzz structured cricket fallbacks and Cricbuzz exposed the stable final.
- **2026-09-19:** User explicitly authorised synchronising this running mini log to the existing writable Google Drive mini-log file. This authorisation does not extend to canonical combined logs or governing/reference/history files.

- **P-452 through P-473 have been issued and are fully settled in this mini log. The next intended mini-log ID is P-474, subject to fresh canonical reconciliation.**
- No Google Drive authoritative/reference/history file was edited during initialization.
- **Drive write scope:** only the dedicated running mini-log file is authorised for synchronisation. Canonical combined logs and governing/reference/history files remain read-only unless separately authorised.
- Before each prediction, the canonical next-ID authority and event state must be checked again.
- After every new prediction query, update this Markdown file and synchronise the dedicated Drive mini-log copy under the current explicit authorisation; do not write to any other Drive document.
- No automatic retrospective or settlement analysis will be performed unless explicitly requested. P-452–P-456 were settled/retrospected on 2026-09-18 by explicit request; P-457 onward were subsequently processed in explicit settlement passes. On 2026-09-20, P-472 and P-473 were terminal-state verified and fully settled/retrospected by explicit request.

---

## 2026-09-21 — canonical import of P-474–P-481 from settled external mini log

**Disposition:** imported as historical evidence into Part 4. Every canonical prediction from P-474 through P-481 is settled and retrospectively reviewed in the source mini log. Original issued predictions, probabilities, ranks, reasoning and source records are preserved below verbatim.

**Source mini log:** `PREDICTION_MINI_RUNNING_LOG_P474_ONWARD.md`  
**Source SHA-256:** `5239a9894d441c46d63ffd633f94b4ac00bd9c145d96ee7bfc7b175b710719a7`

# Prediction Mini Running Log — P-474 Onward


Created: Sep 20, 2026
Location/time basis: Australia/Melbourne
Governing method: MDS-2026.09.19-v4.3 / CR-2026.09.19-4
Control hashes: METHOD da544d4c47efdf33bdbcc130a5ef0adc23055f77f80fd25284c1dc55f3d1b1b6; RULES_BASEBALL 1e0b5a0e9636469f7b75fcc21d19f9fe3c557c691724e67bba821b145889a411; RULES_BASKETBALL f5ad8787a08fe6b1533c0f273058f26ab3ff3f731bc5307ebe40423993c14421
Operating mode: SPORTS_ONLY / MARKET_BLIND
Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE
Next intended ID after this card: P-482, subject to fresh reconciliation.
Retrospective policy: settle completed events only after required verification; live/unresolved events remain pending.


## 1. Incomplete / Unsettled Logs


None. All P-474 through P-481 events are now fully settled and retrospectively reviewed.


## 2. Fully Settled Logs


### P-474 — MLB — Athletics @ Cleveland Guardians




- Canonical / staging ID: P-474
- Venue: Progressive Field, Cleveland, Ohio, United States
- Venue timezone: America/New_York
- Official venue-local start: Sep 19, 2026 at 6:10 PM EDT
- Australia/Melbourne conversion: Sep 20, 2026 at 8:10 AM AEST; calendar-date rollover = YES
- Research cutoff / distribution freeze: Sep 20, 2026 at approximately 8:14 AM AEST
- Issuance state: START_CROSSED_UNVERIFIED. The official scheduled start had passed before delivery. Per the user's explicit instruction, research continued, but no live score, pitches, baserunners, or other in-game observations were admitted into the predictive model.
- Normal pregame preflight: FAIL with exactly one blocking finding, PF-EVENT-STATE. Source-count, lineage, field-owner, timezone, line-quarantine and freeze-order checks passed. This is therefore a late-issued research forecast, not a normal pregame PASS.




#### Identity / contracts




Supplied contracts were quarantined until after the sporting distribution was frozen:
- Cleveland Guardians moneyline
- Athletics +1.5 runs
- Full-game Over 7.5 runs
- Full-game Under 7.5 runs




Research endpoint treats a completed MLB regular-season game as including extra innings. Exact sportsbook suspension/action rules were not supplied, so operator action is not asserted.




#### Starters / lineups / availability




Official probable-starter handshake:
- Athletics: Jacob Lopez, LHP — 6-4, 5.02 ERA, 107 K in 114.2 IP.
- Guardians: Tanner Bibee, RHP — 6-15, 4.16 ERA, 140 K in 177.1 IP.




Latest pregame lineup cross-check recovered from CBS/STATS-Field Level and an MLB-derived automated game feed:
- Athletics: Henry Bolte CF; Jeff McNeil 1B; Shea Langeliers DH; Lawrence Butler RF; Zack Gelof 3B; Donovan Walton 2B; Carlos Cortes LF; Brian Serven C; Alika Williams SS.
- Guardians: Steven Kwan CF; José Ramírez 3B; Chase DeLauter DH; Jo Adell RF; Angel Martínez LF; David Fry 1B; Travis Bazzana 2B; Austin Hedges C; Brayan Rocchio SS.




Lineup integrity note: the MLB starting-lineups index retrieved during the research window still rendered the matchup as TBD, so a field-owner posted-order capture was not recovered to gate standard. The secondary lineup cross-check is used with an evidence cap; no player prop is ranked.




Major Athletics absences materially reduce their offensive depth: Brent Rooker, Nick Kurtz and Jacob Wilson are on the 60-day IL with 2027 expected returns; Tyler Soderstrom underwent season-ending hip surgery. Shea Langeliers is available and is a key surviving power bat.




Guardians availability: Rhys Hoskins remains out; Colin Holderman's wrist rehab suffered a setback; Shawn Armstrong was still on rehab progression. Chase DeLauter and Angel Martínez had recent day-to-day issues but were listed in the latest pregame lineup cross-check, so they are treated as available with residual uncertainty.




#### Pitching / team process evidence




Tanner Bibee:
- Latest completed start: 6 2/3 IP, 2 ER, 7 K.
- Baseball Savant 2026 line: 28 HR allowed, .307 wOBA, .318 xwOBA, 39.2% hard-hit and 8.3% barrel rate. This supports a credible Athletics home-run/cluster tail even though Cleveland is preferred overall.




Jacob Lopez:
- Season line remains volatile at 5.02 ERA / 1.48 WHIP.
- One recent quality-start branch is real: 6 IP, 2 ER, 7 K in the official MLB record against Texas.
- But the immediate recent window also contains material contact/home-run damage; CBS/Field Level reported nine runs on 13 hits in 9 2/3 innings over his prior two starts and five homers allowed across his prior three outings.




Current-regime team context since early August, used descriptively rather than as a fitted coefficient:
- Athletics: 91 wRC+, -15 defensive runs in the cited metric, 6.17 starter ERA, 4.53 bullpen ERA.
- Guardians: 101 wRC+, approximately neutral/positive defense, 3.11 bullpen ERA.




Bullpen workload note: Cleveland used Joey Cantillo for six relief innings in the preceding game; Hunter Gaddis and Cade Smith each handled late innings. Cantillo's immediate availability is therefore reduced, while the strongest one-inning leverage arms were used but not multi-inning exhausted. Workload informs availability only, not quality.




#### Weather / park




National Weather Service Cleveland forecast around the game window was roughly low-70s °F, mostly cloudy with a chance of showers and modest winds. No reliable park-orientation transformation justified a signed wind adjustment, so weather widens interruption/environment uncertainty but does not force an Over or Under direction.




#### Frozen independent joint run distribution




Model: explicit UNVALIDATED_SUBJECTIVE scenario mixture; independent Poisson team-run kernels within each scenario, then a separate MLB extra-inning branch. This is not a fitted, calibrated or prospectively validated model.




Scenario 1 — Cleveland control: weight 0.33; CLE 5.0, ATH 2.7.
Scenario 2 — competitive central: weight 0.34; CLE 4.2, ATH 3.4.
Scenario 3 — Athletics power / Bibee HR tail: weight 0.15; CLE 3.8, ATH 5.0.
Scenario 4 — high-run starter-to-bullpen cluster: weight 0.18; CLE 6.2, ATH 4.3.




Frozen centre:
- Cleveland runs: 4.76
- Athletics runs: 3.57
- PROJECTED TOTAL: 8.34 runs
- Projected Cleveland margin: +1.19 runs
- Regulation total SD: approximately 3.09 runs
- Regulation margin SD: approximately 3.12 runs
- Representative score family: Cleveland 5-3 Athletics
- Distribution ID: P-474-dist-v1
- Distribution SHA-256: 80ed1ee27b0e8c1958bbe2ce07fbca5d9ce2a8ffb06c4dd974e4eb9f2ca6467d




##### Mandatory total projection / ceiling audit




PROJECTED TOTAL: 8.34
SUPPLIED TOTAL: 7.5
RAW GAP: +0.84 runs
DISTRIBUTION WIDTH: ~3.09 runs SD
NORMALIZED GAP: ~+0.27 SD
ASSESSMENT: MODEST SEPARATION, not a strong total edge.
PREFERRED SUPPLIED SIDE: Over 7.5.
MODEL ALTERNATE TARGET: Over 6.5, roughly 71-72% from the same frozen distribution before minor extras uplift. Operator availability is not asserted.




Component / failure-state budget:
- Cleveland centre 4.8 + Athletics centre 3.6 = about 8.4 -> Over.
- Cleveland ordinary high 6 + Athletics centre 3-4 -> 9-10 -> Over.
- Cleveland centre 4-5 + Athletics ordinary high 5 -> 9-10 -> Over.
- Bibee-control + depleted Oakland branch can still produce 4-2 / 5-2 -> Under 7.5.
- A strong Lopez outing plus Cleveland home-last-bat suppression can produce 3-2 / 4-2 -> Under.
- A tie after nine activates MLB's automatic runner at second, increasing the scoring rate of the extra-inning branch and modestly helping the Over relative to a regulation-only calculation.




#### Ranked supplied contracts




1. GUARDIANS ML — ~65.5% UNVALIDATED_SUBJECTIVE — Rank #1.
   Why: Cleveland owns the stronger current bullpen/process profile; Oakland's lineup is missing several of its highest-impact bats; Bibee's central branch is more stable than Lopez's; Cleveland also has home-last-bat and extra-inning home advantage.
   Main failure: Bibee's 28-HR season tail is hit by Langeliers/Butler/Gelof, while Lopez reaches his quality-start branch and Cleveland's depleted relief depth is exposed.




2. OVER 7.5 RUNS — ~60.6% — Rank #2.
   Why: independent centre is 8.34; Lopez's contact/HR volatility plus Bibee's own HR tail produces several ordinary 5-3, 5-4 and 6-3 states; MLB extras add upper-tail scoring when regulation ends tied.
   Main failure: Bibee suppresses the depleted Oakland lineup and Lopez lands his good-start branch, producing a 4-2 / 5-2 or lower state; a Cleveland lead can also remove the bottom of the ninth.




3. ATHLETICS +1.5 — ~52.8% — Rank #3.
   Why: the +1.5 wins in every Athletics victory and every Cleveland one-run win. The regulation model puts about 13.1% mass specifically on a Cleveland one-run win, which creates meaningful overlap with Guardians ML.
   Main failure: Cleveland separates by 2+ through the Lopez-to-middle-relief transition, a multi-run homer/sequence cluster, or late bullpen separation.




4. UNDER 7.5 RUNS — ~39.4% — Rank #4.
   Why it remains live: Cleveland has a legitimate run-prevention path against a heavily depleted Athletics lineup, and Bibee just delivered a strong start.
   Why it ranks last: 7.5 is below the 8.34 centre, both starters retain home-run/contact tails, and several ordinary rather than extreme score combinations clear eight runs.




Forced-pair integrity: Over 7.5 + Under 7.5 = 100% conditional on action; there is no push at a half-run line. Guardians ML and Athletics +1.5 are not complements because both win when Cleveland wins by exactly one run.




#### Potential game winner




CLEVELAND GUARDIANS — approximately 65.5% eventual-win estimate.




Regulation decomposition before the extra-inning branch:
- Cleveland win ~59.1%
- Tie after nine ~12.1%
- Athletics win ~28.8%




The MLB automatic-runner branch is assigned a small home-side edge, lifting Cleveland's eventual research endpoint to about 65.5%. This is an unvalidated scenario assumption, not a calibrated MLB win model.




#### Dependence / kill-path audit




Top two: Guardians ML + Over 7.5.
- Approximate joint success: ~40%.
- Approximate both-fail state: ~14%.
- Approximate probability at least one of top two wins: ~86%.
- Main both-fail family: Athletics win a low-scoring game because Lopez reaches his strong branch while Bibee allows one decisive power cluster, e.g. 4-3 / 3-2 Athletics.




Guardians ML and Athletics +1.5 positively overlap in Cleveland one-run wins; they should not be treated as independent confirmation.




#### Self-selected model targets outside the supplied slate




These are model thresholds, not claims that an operator offers them:
- Over 6.5 runs: ~71-72%, safer than the supplied Over 7.5.
- Athletics team total Under 4.5: ~70% regulation-model target; slightly lower after accounting for extra-inning exposure.
- Cleveland team total Over 3.5: ~68% regulation-model target.




These are not promoted above the supplied four in the official ranked slate because the user explicitly supplied those four contracts and the Drive baseball rule requires every supplied row to be ranked.




#### Integrity flags




- START_CROSSED_USER_OVERRIDE / PF-EVENT-STATE BLOCK
- NO_LIVE_GAME_STATE_USED_IN_MODEL
- MLB_FIELD_OWNER_POSTED_LINEUPS_NOT_RECOVERED_TO_GATE_STANDARD
- EXACT_OPERATOR_SUSPENSION/ACTION_RULES_UNKNOWN
- UNVALIDATED_SUBJECTIVE_DISTRIBUTION
- MARKET_ODDS / LINE_MOVEMENT / TIPSTERS / FANTASY-DFS EXCLUDED
- Original issue status: UNSETTLED — LATE-ISSUED RESEARCH FORECAST / NO RETROSPECTIVE




#### Sources / provenance




1. MLB Probable Pitchers — exact event, venue, scheduled time, official probable starters and season starter lines — PRIMARY FIELD OWNER — https://www.mlb.com/probable-pitchers
2. MLB Scores / schedule — exact event/date/state route — PRIMARY FIELD OWNER — https://www.mlb.com/scores/2026-09-19
3. MLB Athletics injuries and roster moves — Rooker/Kurtz/Wilson and other current IL status — PRIMARY FIELD OWNER — https://www.mlb.com/athletics/news/athletics-injuries-and-roster-moves
4. MLB Athletics report on Wilson/Kurtz/Soderstrom — season-ending availability context — PRIMARY TEAM/FIELD OWNER — https://www.mlb.com/news/jacob-wilson-nick-kurtz-expected-to-miss-rest-of-2026-season
5. MLB Guardians injuries and roster moves — Hoskins/Holderman/Armstrong and recent day-to-day availability — PRIMARY FIELD OWNER — https://www.mlb.com/guardians/news/guardians-injuries-and-roster-moves
6. MLB Guardians transactions — Holderman rehab status and bullpen roster context — PRIMARY FIELD OWNER — https://www.mlb.com/guardians/roster/transactions
7. Baseball Savant / MLB — Bibee Statcast contact, xwOBA, hard-hit, barrel and HR data — PRIMARY MLB TRACKING SOURCE — https://baseballsavant.mlb.com/team/114_4
8. MLB game video, Athletics at Rangers — official Lopez 6 IP / 2 ER / 7 K quality-start branch — PRIMARY FIELD OWNER — https://www.mlb.com/video/game/822851
9. Reuters — Bibee latest 6 2/3 IP / 2 ER / 7 K and Cleveland recent offense — HIGH-QUALITY INDEPENDENT — https://www.reuters.com/sports/baseball/guardians-creep-closer-al-central-lead-by-hammering-twins--flm-2026-09-13/
10. Covering the Corner series preview — current-regime wRC+, defense, starter ERA and bullpen ERA diagnostics — INDEPENDENT SECONDARY — https://www.coveringthecorner.com/cleveland-guardians-analysis/74254/series-preview-athletics-at-guardians
11. Covering the Corner game discussion — pregame matchup / lineup corroboration — INDEPENDENT SECONDARY — https://www.coveringthecorner.com/cleveland-guardians-discussion/74401/athletics-at-guardians-bibee-vs-lopez-discussion
12. CBS Sports / STATS LLC / Field Level Media exact-game preview — posted lineup cross-check, Lopez recent-contact/HR window, WHIP and starter context — INDEPENDENT SECONDARY — exact Athletics-at-Guardians game preview.
13. National Weather Service Cleveland — venue-area game-window temperature/cloud/showers/wind context — GOVERNMENT FIELD OWNER — https://forecast.weather.gov/MapClick.php?FcstType=digital&lat=41.4797&lon=-81.6785
14. MLB Automatic Runner glossary — extra-inning runner-on-second rule — RULES FIELD OWNER — https://www.mlb.com/glossary/rules/designated-runner
15. MLB Regulation Game glossary — nine-inning/home-last-bat/extra-inning endpoint definition — RULES FIELD OWNER — https://www.mlb.com/glossary/rules/regulation-game
16. Sports Research Drive — METHOD.md, RULES_BASEBALL.md, RULES_GENERAL.md, CONTROL_MANIFEST_2026-09-19.md, DATA_SOURCE_REGISTER.md and FORECAST_PREFLIGHT_MANIFEST.md — governing methodology.




Source firewall: no sportsbook odds, betting picks, tipster predictions, line movement, fantasy/DFS projections, or market consensus were used as predictive inputs. The user-supplied 7.5/+1.5/ML contracts were queried only after distribution freeze.




#### Document mapping / candidate learnings




- Starter HR/contact tail plus depleted opponent lineup should remain a two-sided mixture rather than a one-sign Under adjustment -> existing RULES_BASEBALL starter/current-regime and cluster controls; no new fixed coefficient.
- Exact posted-lineup field-owner retrieval remained incomplete at the issuance gate -> DATA_SOURCE_REGISTER source-latency/retrieval observation.
- Start crossing with explicit user direction demonstrates that normal preflight can fail while a clearly labelled research-only late forecast is still recorded without live-state contamination -> EXTERNAL_LOGGING_WORKFLOW process note candidate; do not weaken normal pregame gate.




---




#### Settlement and retrospective — P-474


Settlement status: SETTLED / RETROSPECTIVE COMPLETE.
Verified final: Cleveland Guardians 12, Athletics 6.
Actual full-game total: 18 runs.
Actual margin: Cleveland +6.


Three-source final-state gate: PASS.
- MLB official scoreboard/game story: FINAL, Cleveland 12-6.
- Associated Press / CBS reporting: Cleveland 12-6 final.
- Athletics Nation / Field Level Media independent recap: Cleveland 12-6 final.


Settlement sources:
- MLB official scoreboard: https://www.mlb.com/scores/2026-09-19
- MLB official game story: https://www.mlb.com/stories/game/824380
- AP/CBS final recap: CBS Sports exact-game recap, Sep 19, 2026.
- Athletics Nation final recap: https://www.athleticsnation.com/athletics-scores-and-standings/109853/as-fall-to-guardians-12-6
- Field Level Media final recap: https://fieldlevelmedia.com/mlb/angel-martinez-homers-twice-guardians-dominate-athletics/


##### Pick-by-pick settlement — supplied slate


1. Guardians ML — WIN. Cleveland won 12-6.
2. Over 7.5 — WIN. Final total was 18.
3. Athletics +1.5 — LOSS. Oakland lost by six.
4. Under 7.5 — LOSS.


Potential game winner: Cleveland Guardians — WIN.


Self-selected model targets:
- Over 6.5 — WIN.
- Athletics team total Under 4.5 — LOSS; Athletics scored 6.
- Cleveland team total Over 3.5 — WIN; Cleveland scored 12.


##### Ranking / top-two / totals review


Rank #1 Guardians ML succeeded, so no Rank-1 failure trigger applies.
Highest-ranked full-game O/U, Over 7.5, succeeded; no mandatory top-O/U failure trigger applies.
Top two supplied selections both succeeded: Guardians ML WIN + Over 7.5 WIN. Hit@2 = YES; both-win = YES.


The ordering of Guardians ML above Over 7.5 was defensible on pre-game evidence because Cleveland had the stronger side profile, while the total was only ~0.27 SD above the supplied line and retained a genuine low-scoring branch.


##### What the outcome turned on


Cleveland's upper-tail offensive cluster arrived immediately. The Athletics led 2-0 in the top of the first, but Cleveland scored five before Jacob Lopez recorded an out, including Chase DeLauter's three-run homer and Angel Martínez's two-run homer. Cleveland added five more in the third. Lopez was charged with 10 runs and 10 hits in 2 2/3 innings.


The important second mechanism was that Tanner Bibee also failed to suppress Oakland. Bibee allowed six runs on 12 hits in 4 2/3 innings. The final therefore came from a two-sided starter-failure / sequencing / home-run state rather than a simple Cleveland-control state.


##### Expected script vs reality


What went right:
- Cleveland was correctly preferred to win.
- Lopez's contact/home-run and early-hook risk was explicitly identified before issue.
- The Over was correctly preferred to the Under.
- Cleveland team total Over 3.5 and Over 6.5 both captured the favourite's offensive upside.


What went wrong:
- The 8.34-run centre badly understated the realized 18-run upper tail.
- The model's Athletics team-total Under 4.5 depended too much on Bibee/depleted-lineup suppression; Bibee instead allowed six runs himself.
- The high-run branch existed, but its two-sided form — Lopez collapse plus Bibee collapse in the same game — was not given enough prominence.


This does not justify adding a fixed Over coefficient. One realised extreme game is not evidence that the centre itself should be shifted by an arbitrary amount.


##### Availability / lineup / source audit


The issue-time card explicitly recorded that field-owner posted orders were not recovered to gate standard and therefore did not rank player props. That limitation was handled correctly. The final was settled from multiple explicit terminal-state sources rather than search snippets.


Source-quality result:
- MLB official final/game story: retained as field owner.
- AP/CBS and Field Level Media: retained as high-quality independent final/result sources.
- Athletics Nation: useful secondary game-script corroboration, not a substitute for MLB field ownership.


##### Blind spots and mitigation


Blind spot: simultaneous failure of both starters was under-emphasized even though each had a documented contact/HR tail.
Pre-game knowability: PARTLY KNOWABLE — the component risks were known; the exact joint realization was not.
Materiality: HIGH for the total and Athletics team total; LOW for the Cleveland winner.
Mitigation: when both starters carry credible upper-tail contact/HR risk, explicitly show a joint two-starter-failure branch before ranking a total or team-total Under.


Existing control check: RULES_BASEBALL already requires BB-B2 joint early-hook, BB-B3 cluster and BB-B5 relief-transition states. This is principally an execution/emphasis observation, not evidence for a new permanent rule.


##### Document mapping


- RULES_BASEBALL.md — existing BB-B2/BB-B3/BB-B5 controls; reinforce execution only, no new coefficient.
- DATA_SOURCE_REGISTER.md — retain the issue-time official-lineup retrieval-latency observation.
- Prediction log — record the two-sided starter-collapse learning with P-474.




---


### P-475 — WNBA — Chicago Sky @ Atlanta Dream




- Canonical / staging ID: P-475
- Competition: WNBA 2026 regular season
- Official event ID: WNBA game 1022600310
- Venue: State Farm Arena, Atlanta, Georgia, United States
- Venue timezone: America/New_York
- Official venue-local start: Sep 19, 2026 at 7:00 PM EDT
- Australia/Melbourne conversion: Sep 20, 2026 at 9:00 AM AEST; calendar-date rollover = YES
- Research cutoff / independent distribution freeze: Sep 20, 2026 at approximately 9:04:40 AM AEST
- Issuance state: START_CROSSED_UNVERIFIED. Research crossed scheduled tip while completing the required source and methodology checks. No live score, possession, lineup-on-court, shot, foul, injury-in-game or other post-tip performance information was admitted into the predictive model.
- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-BASKETBALL
- Operating mode: SPORTS_ONLY / MARKET_BLIND
- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE
- Preflight: FAIL with exactly one blocking finding, PF-EVENT-STATE. Source count/lineage, field-owner mix, timezone conversion, source firewall, line quarantine and freeze order otherwise passed.
- No retrospective performed.




#### Identity / supplied contracts




The supplied thresholds were quarantined until after the independent basketball distribution was frozen:
- Atlanta Dream -15.5
- Chicago Sky +15.5
- Full-game Over 176.5
- Full-game Under 176.5




Exact operator overtime/action/void terms were not independently supplied. The research endpoint is a normal completed WNBA game including the explicit overtime tail; operator settlement remains a separate field if later required.




#### Participant / availability state




Official WNBA injury-report process was checked, but the dynamically rendered league page did not expose the exact current team rows through the accessible research route. Current pre-tip reporting was therefore reconciled across team/league records and independent current sources and is evidence-capped rather than relabelled field-owner-confirmed.




Chicago:
- Natasha Cloud — QUESTIONABLE, left knee, after leaving the Sep. 17 Washington game in the first half and not returning.
- Azurá Stevens — OUT, right knee.
- DiJonai Carrington — OUT, left foot.
- Skylar Diggins — OUT for the remainder of the season, right knee.
- Rickea Jackson — OUT for the remainder of the season after a torn left ACL.
- Current available core includes Kamilla Cardoso, Courtney Vandersloot, Sydney Taylor, Rachel Banham, Gabriela Jaquez, Aicha Coulibaly, Jacy Sheldon and Elizabeth Williams.
- Cloud's unresolved availability is represented as a minutes/role mixture; no binary full-workload assumption is made.




Atlanta:
- Brionna Jones — OUT for the remainder of the season, left leg.
- Current core available in pre-tip records: Jordin Canada, Allisha Gray, Rhyne Howard, Angel Reese, Naz Hillmon, DeWanna Bonner, Madina Okot and the supporting guard/wing rotation.
- Atlanta's long-running most-used starting unit has been Canada / Gray / Howard / Hillmon / Reese, but a confirmed five for this exact game was not recovered to gate standard before the research cutoff and is not relabelled as confirmed.




Because both confirmed starting fives were not recovered to the governing gate standard, lineup-sensitive player props are not promoted. Full-game side/total rows carry a participant-evidence cap.




#### Current regime / recent form




Current records immediately before the event:
- Atlanta: 27-14, 8-2 over the latest league-recorded ten-game form window.
- Chicago: 15-26, four straight losses; the current standings snapshot shows Chicago materially behind Atlanta.




Descriptive score windows calculated from the latest completed game sequence:
- Atlanta L5: 4-1; 90.4 scored / 80.2 allowed.
- Atlanta L10: 8-2; 97.5 scored / 83.0 allowed.
- Atlanta L15: 11-4; 94.1 scored / 84.7 allowed.
- Atlanta L20: 15-5; 94.9 scored / 86.3 allowed.
- Chicago L5: 1-4; 78.0 scored / 93.0 allowed.
- Chicago L10: 3-7; 81.0 scored / 90.9 allowed.
- Chicago L15: 6-9; 85.2 scored / 91.3 allowed.
- Chicago L20: 8-12; 86.9 scored / 91.6 allowed.




These result windows are diagnostic only. They are not converted into a mechanical points adjustment.




Latest completed games:
- Atlanta beat Connecticut 103-59. Angel Reese scored 30 with 10 rebounds in under 25 minutes; Atlanta's blowout reduced her exposure rather than requiring full star minutes.
- Chicago lost 110-80 to Washington. Chicago was heavily outrebounded and Washington converted Chicago turnovers into transition/early-offense scoring. Cloud left with the knee issue.
- Those two blowouts widen today's mismatch branches but do not by themselves justify a 15.5-point central margin.




Current-season head-to-head:
- Atlanta 82-75 Chicago on June 9.
- Atlanta 93-91 Chicago on July 19.
Atlanta is 2-0, but the margins were only 7 and 2. Those games are retained as direct matchup context; today's much more depleted Chicago roster means they do not control the current margin distribution.




#### Possession / efficiency mechanism




Historical structured current-season baselines before the last game placed Atlanta around:
- 90.8 points per game;
- 80.6 pace;
- 112.3 offensive rating;
- 106.0 defensive rating;
- +6.3 net rating.




Chicago's comparable baseline before the last game was around:
- 86.7 points per game;
- 81.7 pace;
- 105.5 offensive rating;
- 109.1 defensive rating;
- -3.6 net rating.




The current model does not add arbitrary points for injuries or recent results. Instead, it uses an explicit scenario mixture spanning Cloud active/functional, Cloud limited/out, Atlanta favourite sustain, Atlanta blowout slowdown/bench compression, Chicago shooting resistance and a higher-pace late-scoring branch.




Expected possession environment: approximately 80-82 regulation possessions, with material variance from Chicago transition defence/turnovers and Atlanta's ability to control the game state.




Decision-driving mechanisms:
1. Atlanta's Gray/Howard/Canada perimeter creation against a depleted Chicago guard/wing rotation.
2. Reese/Hillmon/Okot/Bonner frontcourt rebounding and second-chance pressure against a Chicago group missing Stevens.
3. Chicago's Cardoso interior scoring/rebounding as its clearest stable half-court floor.
4. Cloud's uncertain creation/defence and replacement minutes for Vandersloot/Taylor/Banham/Jaquez/Coulibaly/Sheldon.
5. Atlanta's blowout rotation: starter minutes can fall while bench pace/offence persists.
6. Chicago's garbage-time response: reduced Atlanta defensive intensity can compress the margin and lift the total simultaneously.
7. Late-foul and overtime branches remain explicit but low-mass.




#### Frozen independent joint score distribution




Model: explicit UNVALIDATED_SUBJECTIVE scenario mixture. Within each scenario, team-score uncertainty is represented with approximately 10-point team SD and modest positive game-level correlation (~0.15). This is an uncertainty representation, not a calibrated WNBA model.




Scenario 1 — Cloud active / competitive central: weight 0.22; ATL 95, CHI 80.
Scenario 2 — Cloud limited/out / Atlanta central: weight 0.22; ATL 97, CHI 76.
Scenario 3 — favourite sustain / shooting-rebound separation: weight 0.22; ATL 104, CHI 74.
Scenario 4 — blowout slowdown / bench compression: weight 0.18; ATL 91, CHI 82.
Scenario 5 — Chicago resistance / shooting-high: weight 0.10; ATL 92, CHI 87.
Scenario 6 — higher-pace bench / late-scoring branch: weight 0.06; ATL 101, CHI 85.




Frozen distribution:
- Atlanta centre: 96.76
- Chicago centre: 79.16
- PROJECTED TOTAL: 175.92
- PROJECTED ATLANTA MARGIN: +17.60
- Approx total SD including scenario uncertainty: 15.54
- Approx margin SD including scenario uncertainty: 15.40
- Representative score family: Atlanta 97-79
- Distribution ID: P-475-dist-v1
- Distribution SHA-256: 0392fe62912bad317ee0ffae5adb0d08ce9bd73b6c044eb9543ae1889d443968




##### Mandatory total projection / team-score budget




PROJECTED TOTAL: 175.92
SUPPLIED TOTAL: 176.5
RAW GAP: -0.58 points
DISTRIBUTION WIDTH: ~15.54 points SD
NORMALIZED GAP: ~-0.04 SD
ASSESSMENT: CLOSE TO PROJECTION / WEAK MAIN-TOTAL EDGE.
Preferred supplied side: Under 176.5, but only marginally.




Team-score threshold budget:
- Chicago floor 70-74 requires Atlanta roughly 103-107 to cross 176.5; the favourite-sustain branch can do it, while many suppression/blowout states remain Under.
- Chicago centre 78-81 requires Atlanta about 96-99; this is almost exactly Atlanta's central score range, so ordinary states land on both sides.
- Chicago ordinary high 86-88 requires only Atlanta 89-91; that underdog-response branch tends to push the game Over even when the final margin compresses.
- Atlanta ordinary high 101-104 can push the game Over even with Chicago in the mid-70s.
- Therefore Chicago's depleted offence is not an automatic Under: Atlanta's own ceiling can consume the total budget.




Model alternate-total targets from the same frozen distribution:
- Under 184.5 ~71.0%.
- Under 188.5 ~80%+.
These are model thresholds only; operator availability is not asserted.




##### Mandatory large-spread separation audit




Projected margin: Atlanta +17.60
Supplied spread: Atlanta -15.5
Raw separation beyond line: +2.10 points
Margin width: ~15.40 points SD
Normalized separation: ~0.14 SD
ASSESSMENT: LINE INSIDE THE CENTRAL MARGIN CORRIDOR / weak-to-modest supplied spread edge.




Mismatch states:
- Favourite sustain: Atlanta keeps pressure, rebounding and transition efficiency high -> 25-30+ margin possible.
- Favourite slowdown: starter minutes fall; Atlanta bench scores enough to win but Chicago response compresses the closing margin -> 7-12 point final possible.
- Underdog response: Cardoso plus secondary guards score against reduced defensive intensity -> margin can fall inside 15.5 while total rises.
- Underdog suppression: Chicago's missing creators/wings reduce half-court quality and defensive resistance -> wide Atlanta margin with a lower total.




The two 2026 H2H margins (7 and 2) are a warning against treating -15.5 as automatic; today's roster state is worse for Chicago, but the current model still keeps substantial compression mass.




#### Best four model-selected picks




These are model target thresholds, not claims that a sportsbook currently offers each exact line.




1. ATLANTA DREAM ML — ~87.3% UNVALIDATED_SUBJECTIVE.
   Rationale: stronger current roster continuity, superior current team process, home venue, Chicago's depleted creation/wing defence and Atlanta's multiple scoring/rebounding pathways.
   Main failure: Chicago shoots above its ordinary range, Cardoso controls the paint and Atlanta's post-World-Cup/rotation efficiency underperforms.




2. ATLANTA TEAM TOTAL OVER 88.5 — ~77.2%.
   Rationale: Atlanta's independent team centre is ~96.8, every central scenario keeps the favourite above 90 before within-scenario shooting variance, and Chicago just allowed 110 while losing transition/rebounding control.
   Main failure: Atlanta builds an early lead, sharply cuts primary creators and the bench shoots poorly enough to stall in the mid-80s.




3. CHICAGO TEAM TOTAL UNDER 86.5 — ~75.1%.
   Rationale: independent Chicago centre ~79.2; Diggins/Jackson/Carrington/Stevens unavailable and Cloud uncertain; Atlanta owns a strong current defensive/rebounding structure.
   Main failure: garbage-time response, Cardoso paint efficiency, secondary shooting variance or Atlanta defensive-intensity reduction lifts Chicago into the high 80s.




4. ATLANTA -8.5 — ~71.9%.
   Rationale: materially safer than -15.5 while preserving the same current-regime mismatch mechanism; survives more blowout-compression states.
   Main failure: Cloud plays effectively, Chicago's secondary guards shoot well and Atlanta wins only narrowly, as in the two prior 2026 meetings.




#### Supplied slate ranking




1. DREAM -15.5 — ~55.1% — preferred supplied side / LOW evidence because line sits close to margin centre.
2. UNDER 176.5 — ~51.6% — preferred supplied total / CLOSE TO PROJECTION / very weak directional separation.
3. OVER 176.5 — ~48.4% — live ordinary-high/garbage-time branch but slightly below the frozen centre query.
4. SKY +15.5 — ~44.9% — substantial compression path remains, but current roster depletion makes Atlanta 16+ more likely than Chicago +15.5 in the model.




Forced-pair integrity:
- Dream -15.5 + Sky +15.5 = 100% conditional on action.
- Over 176.5 + Under 176.5 = 100% conditional on action.
- No push exists at either half-point threshold.




#### Potential game winner




ATLANTA DREAM — ~87.3% eventual-win estimate.




This winner view is materially stronger than Atlanta -15.5. The model is confident Atlanta wins much more often than not but only modestly prefers a 16+ point final margin.




#### Dependence / kill-path audit




Top two model picks: Atlanta ML + Atlanta team total Over 88.5.
- Approx joint win: ~73.3%.
- Approx both-fail: ~8.9%.
- Approx at least one wins: ~91.1%.
- Main both-fail state: Atlanta's shooting/turnover process collapses enough to keep the Dream at 88 or below while Chicago's remaining creators/Cardoso produce the upset.




Across all four model-selected targets, approximate all-four-win mass is ~55.6%; approximate all-four-fail mass is ~5.4%. These are derived from the same unvalidated joint scenario object and are not independence calculations.




Top two supplied sides: Atlanta -15.5 + Under 176.5.
- Approx joint win: ~28%.
- Approx both-fail: ~21.5%.
- Main both-fail family: Atlanta wins narrowly or Chicago stays within 15.5 while garbage-time/late-foul scoring pushes the total Over 176.5.




#### Information not confirmed / integrity flags




- START_CROSSED_USER_OVERRIDE / PF-EVENT-STATE BLOCK
- NO_LIVE_GAME_STATE_USED_IN_MODEL
- CONFIRMED_STARTING_FIVES_NOT_RECOVERED_TO_GATE_STANDARD
- CLOUD_FINAL_ACTIVE/INACTIVE_STATUS_NOT_RECOVERED_PRETIP_TO_FIELD_OWNER_STANDARD
- WNBA_OFFICIAL_INJURY_PAGE_DYNAMIC_ROWS_NOT_EXPOSED_IN_RESEARCH_ROUTE
- EXACT_OPERATOR_OVERTIME/ACTION_TERMS_UNKNOWN
- UNVALIDATED_SUBJECTIVE_DISTRIBUTION
- NO SPORTSBOOK ODDS / MARKET MOVEMENT / TIPSTER / FANTASY-DFS PREDICTIVE INPUT
- Original issue status: UNSETTLED — LATE-ISSUED RESEARCH FORECAST / NO RETROSPECTIVE




#### Sources / provenance




1. WNBA exact game page, game 1022600310 — exact event, 7:00 PM ET start, State Farm Arena, prior 2026 H2H — PRIMARY FIELD OWNER — https://www.wnba.com/game/1022600310/chi-vs-atl
2. WNBA official injury-report page — reporting rules and current-update process; exact dynamic rows were not exposed through the accessible text route — PRIMARY FIELD OWNER — https://www.wnba.com/wnba-injury-report
3. WNBA official current standings/homepage — current Atlanta record and league context — PRIMARY FIELD OWNER — https://www.wnba.com/
4. Atlanta Dream official Sep. 17 recap — 103-59 win, Reese 30/10 in under 25 minutes, current player/rotation context — PRIMARY TEAM — https://dream.wnba.com/news/dream-returns-with-a-decisive-win
5. Atlanta Dream official current roster — Canada/Gray/Howard/Reese/Hillmon and current rotation — PRIMARY TEAM — https://dream.wnba.com/roster
6. Chicago Sky official WNBA team page — current 15-26 record and roster — PRIMARY FIELD OWNER / TEAM — https://www.wnba.com/team/1611661329/chicago-sky
7. WNBA official Sep. 17 Chicago recap — Washington 110, Chicago 80 — PRIMARY FIELD OWNER — WNBA game recap archive.
8. Reuters, Sep. 1 — Skylar Diggins shut down for the 2026 season with knee injury — HIGH-QUALITY INDEPENDENT.
9. Reuters / NBC Chicago / WNBA player archive — Rickea Jackson torn ACL, out for season — HIGH-QUALITY INDEPENDENT + LEAGUE ARCHIVE.
10. Athlon final pre-tip injury report, published 2:00 PM EDT — Cloud questionable; Stevens/Carrington/Diggins out; Jones out — CURRENT INDEPENDENT SECONDARY; source lineage is not treated as a field owner.
11. Field Level Media current Chicago recap — Cloud left Sep. 17 with left-knee injury; Chicago lost 110-80 — INDEPENDENT SECONDARY.
12. Basketball-Reference 2026 Atlanta / Chicago schedules and team pages — pace, ORtg/DRtg, season process and disaggregated game sequence — HISTORICAL STRUCTURED CANDIDATE / diagnostic only.
13. Basketball-Reference Atlanta starting-lineup history — long-running Canada/Gray/Hillmon/Howard/Reese lineup continuity — HISTORICAL STRUCTURED CANDIDATE; not a confirmed exact-game five.
14. Sports Research Drive — METHOD.md, RULES_BASKETBALL.md, RULES_GENERAL.md, CONTROL_MANIFEST_2026-09-19.md, DATA_SOURCE_REGISTER.md and FORECAST_PREFLIGHT_MANIFEST.md — governing methodology.




Source firewall: sportsbook odds, consensus, betting picks, line movement, fantasy/DFS projections and betting-derived analysis were not admitted as predictive inputs. User-supplied -15.5/+15.5/176.5 contracts were queried only after the independent distribution freeze.




#### Document mapping / candidate learnings




- Large-spread Chicago depletion does not eliminate blowout-compression/garbage-time response -> existing RULES_BASKETBALL mismatch-state controls; no new coefficient.
- Main 176.5 total sits almost exactly on independent centre despite strong Atlanta-side mismatch -> reinforces team-score-budget requirement rather than a one-sign depleted-underdog Under.
- Exact official injury-row/confirmed-five retrieval remained incomplete near tip -> DATA_SOURCE_REGISTER source-access/latency observation.
- Start-crossing late-research handling remains a process exception only; do not weaken the normal pregame issuance gate in METHOD/FORECAST_PREFLIGHT.




---




#### Settlement and retrospective — P-475


Settlement status: SETTLED / RETROSPECTIVE COMPLETE.
Verified final: Atlanta Dream 106, Chicago Sky 81.
Actual full-game total: 187 points.
Actual margin: Atlanta +25.


Three-source final-state gate: PASS.
- WNBA official recap: Atlanta 106-81 Chicago, explicit completed game recap.
- Atlanta Dream official team recap: 106-81 final.
- CBS/AP / independent box-score reporting: 106-81 final.


Settlement sources:
- WNBA official recap: https://www.wnba.com/watch/video/game-recap-atlanta-dream-106-chicago-sky-81-09-19-2026
- Atlanta Dream official recap: https://dream.wnba.com/news/dream-dominate-in-final-regular-season-home-game
- CBS Sports exact-game recap / box score, Sep 19, 2026.
- StatMuse exact-game team-stat record, Sep 19, 2026.


##### Pick-by-pick settlement — model-selected slate


1. Atlanta Dream ML — WIN.
2. Atlanta team total Over 88.5 — WIN; Atlanta scored 106.
3. Chicago team total Under 86.5 — WIN; Chicago scored 81.
4. Atlanta -8.5 — WIN; Atlanta won by 25.


##### Pick-by-pick settlement — supplied slate


1. Dream -15.5 — WIN.
2. Under 176.5 — LOSS; final total 187.
3. Over 176.5 — WIN.
4. Sky +15.5 — LOSS.


Potential game winner: Atlanta Dream — WIN.


##### Ranking / top-two review


Model-selected Rank #1 Atlanta ML succeeded.
The model-selected top two both succeeded: Atlanta ML WIN + Atlanta team total Over 88.5 WIN.
All four model-selected targets won.


Supplied Rank #1 Dream -15.5 succeeded. The second supplied row, Under 176.5, lost, so at least one of the supplied top two hit but both did not.


The spread read was materially better than the full-game-total read: projected Atlanta +17.6 versus actual +25 correctly identified the wide-margin family, while the projected total 175.92 sat almost exactly on the supplied 176.5 line.


##### Enhanced full-game O/U review


Under 176.5 was the preferred supplied full-game total and lost. It receives the enhanced totals review even though the higher-ranked model-selected Atlanta team-total Over 88.5 won.


Why Under was preferred:
- Independent centre 175.92 was 0.58 below the line.
- Chicago's depleted creation supported an underdog-suppression branch.
- Favourite blowout states could reduce starter minutes.


Why it failed:
- Atlanta scored 106, materially above the central Atlanta score.
- Atlanta shot 52.9% from the field and 50.0% from three (13-of-26), while producing 29 assists and 13 steals.
- The decisive separation occurred in a 32-point Atlanta third quarter, and Isobel Borlase supplied 18 points as depth scoring remained productive.
- Chicago scored 81, close to the model's ordinary Chicago centre. The Under miss was driven primarily by Atlanta's favourite-offensive-ceiling branch, not by an unexpected Chicago offensive explosion.


Could another supplied total side have ranked above it ex ante?
The pre-game gap was only ~0.04 SD, so the Under/Over ordering was inherently fragile. The outcome alone does not prove Over should have been preferred. However, the card itself simultaneously gave Atlanta team total Over 88.5 a much stronger ~77% model probability. That should have made the full-game Under's vulnerability to an Atlanta 100+ state even more explicit in the ranking narrative.


Smallest justified improvement:
Before ranking a full-game Under in a mismatch, reconcile the favourite team-total upper tail and bench-offence branch directly with the game-total budget. If the favourite's high-confidence team-total Over can consume most of the total by itself, the full-game Under must remain low evidence unless the underdog floor is sufficiently low in the same joint states.


This is already substantially covered by RULES_BASKETBALL controls 11, 17 and 18 plus PF-10 distribution-first. No new fixed adjustment is justified from one game.


##### What went right


- Atlanta winner and separation were correctly identified.
- The safer Atlanta -8.5 alternate won comfortably.
- Atlanta TT Over 88.5 correctly captured the favourite's scoring ceiling.
- Chicago TT Under 86.5 correctly captured Chicago's limited scoring output.
- The model explicitly warned that a depleted underdog does not automatically make the full game Under; Atlanta's own ceiling could consume the budget. That warning described the realised mechanism.


##### What went wrong


- The preferred supplied Under 176.5 was too close to the centre to deserve much directional confidence.
- Atlanta's shooting/ball-movement ceiling was realized at an extreme level: 50% from three and 29 assists.
- The full-game total ranking did not fully reflect how strongly the model already liked Atlanta's own team-total Over.


##### Availability / lineup audit


Pre-game, confirmed starting fives were not recovered to gate standard and the card correctly capped participant-sensitive confidence. Post-game reporting shows the available Atlanta core delivered across multiple roles, including Reese, Gray, Howard, Canada and Borlase. No retrospective assumption is used to pretend the exact final five was known pre-tip.


The unresolved pre-game Natasha Cloud status remains a source-process limitation; no prohibited fantasy source is used to backfill it.


##### Source audit


- WNBA official recap and Dream official recap: retained as primary result/game-script sources.
- CBS/AP: retained as high-quality independent box-score/final corroboration.
- StatMuse: useful structured diagnostic for team-stat cross-check, not the sole terminal-state source.


##### Blind spots and mitigation


Blind spot: favourite bench/depth scoring staying efficient after separation.
Pre-game knowability: PARTLY KNOWABLE — roster depth and blowout states were known, exact 50% three-point shooting was not.
Materiality: HIGH for the full-game total; LOW for winner.
Mitigation: explicitly couple favourite team-total ceiling, starter-minute reduction and bench offensive quality in the game-total state tree.


##### Document mapping


- RULES_BASKETBALL.md — controls 11/17/18 already govern mismatch total, team-score budget and late-blowout multi-axis states; reinforce execution, no new fixed rule.
- DATA_SOURCE_REGISTER.md — WNBA exact-injury/starting-five retrieval latency remains a source-access observation.
- Prediction log — record the full-game Under miss alongside the successful favourite team-total Over.




---


### P-476 — MLB — Minnesota Twins @ Los Angeles Angels




- Canonical / staging ID: P-476
- Competition: MLB 2026 regular season
- Venue: Angel Stadium, Anaheim, California, United States
- Venue timezone: America/Los_Angeles
- Official venue-local start: Sep 19, 2026 at 6:38 PM PDT
- Australia/Melbourne conversion: Sep 20, 2026 at 11:38 AM AEST; calendar-date rollover = YES
- Research cutoff / independent distribution freeze: Sep 20, 2026 at 11:29:34 AM AEST
- Issuance state: PREGAME / SCHEDULED at freeze.
- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-BASEBALL
- Operating mode: SPORTS_ONLY / MARKET_BLIND
- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE
- Preflight: PASS, zero blocking findings. Source count/lineage, field-owner mix, timezone conversion, current event state, source firewall, line quarantine and freeze order all passed.
- Distribution ID: P-476-dist-v1
- Distribution SHA-256: 780302c06f545698c2e893258d8e928cc4ed9a601d0876cf2cb749c654e23d57
- No retrospective performed.




#### Identity / supplied contracts




The user-supplied contracts were parsed for identity and quarantined from predictive construction until after the independent joint run distribution was frozen:
- Los Angeles Angels ML
- Minnesota Twins +1.5 runs
- Full-game Over 7.0 runs
- Full-game Under 7.0 runs




Research endpoint assumes a normally completed MLB regular-season game including extra innings. Exact operator-specific listed-pitcher, suspension, shortening, action and void terms were not supplied, so operator action is not asserted.




The integer 7.0 total is push-capable. Over / Push / Under are therefore reported as a three-state probability set; Over and Under are not falsely forced to sum to 100%.




#### Official starters / posted lineups




Official starter handshake:
- Minnesota: Joe Ryan, RHP — 6-10, 3.84 ERA, 146 SO.
- Los Angeles: Reid Detmers, LHP — 6-8, 3.36 ERA, 199 SO.




The current MLB all-club starting-lineup index recovered complete posted orders:
Minnesota — Luke Keaschall RF; Austin Martin LF; Ryan Jeffers C; Josh Bell DH; Brooks Lee 3B; Royce Lewis 2B; Victor Caratini 1B; Walker Jenkins CF; Ryan Kreidler SS.
Los Angeles — Zach Neto SS; Mike Trout DH; Wade Meckler LF; Vaughn Grissom 2B; Moisés Ballesteros 1B; Denzer Guzman 3B; Josh Lowe RF; Jose Siri CF; Tyler Heineman C.




Retrieval note: team-specific MLB lineup subpages still rendered this matchup as TBD while MLB's current all-club lineup index exposed the full orders. The full orders are retained as the newest field-owner index view, while the intra-MLB cache inconsistency is recorded rather than hidden.




#### Availability / roster state




Minnesota:
- Byron Buxton — OUT, right hip; underwent hip labrum repair on Sep. 18 and expected back in 2027.
- Trevor Larnach — 10-day IL, left wrist sprain.
- Kaelen Culpepper — 10-day IL, left hamstring strain.
- Joe Ryan was activated Sep. 7 after a left glute strain.
- Royce Lewis is in the posted lineup after the recent shoulder-soreness episode, so he is treated as available rather than carrying forward an obsolete absence flag.




Los Angeles:
- Kyren Paris — 10-day IL, right index-finger fracture; expected 2027.
- Nolan Schanuel — right intercostal strain, expected 2027 after rehab irritation.
- Samy Natera Jr. — 15-day IL, left forearm inflammation.
- Sam Bachman was activated Sep. 16.
- Mike Trout, Zach Neto, Josh Lowe and the currently posted starting position-player group are treated as available.




Both offences are therefore below ideal full-season roster strength. Minnesota is missing Buxton/Larnach/Culpepper; Los Angeles is missing Schanuel/Paris. No one-sided injury multiplier was applied.




#### Starter process




Joe Ryan:
- Underlying 2026 Statcast snapshot: 27.1% K, 5.0% BB, .289 xwOBA, 3.46 xERA.
- Contact-tail warning: 11.1% barrel rate and 42.6% hard-hit rate in that snapshot.
- Returned from the glute IL on Sep. 7.
- Latest start versus Cleveland: 4.0 IP, 4 ER, 84 pitches; his first MLB start back was also only four innings.
- Current modelling therefore separates Ryan's per-batter skill from his length/hook distribution. A central Ryan branch does not assume six-plus innings simply from his season reputation.
- Career matchup context: official MLB preview states Ryan is 2-0 with a 3.10 ERA and 41 K in five career starts versus the Angels. This remains weak contextual evidence and does not override current workload state.




Reid Detmers:
- Current official line: 3.36 ERA, 199 K.
- Latest start: 6.0 IP, 3 ER, 8 K versus Seattle.
- That was his seventh consecutive quality start, supporting a materially longer central exposure than Ryan's current post-IL branch.
- 2026 Statcast snapshot: 28.3% K, 7.4% BB, .290 xwOBA, 3.48 xERA, 8.7% barrel rate.
- Pitch mix snapshot: roughly 45% four-seam and 32% slider, with curve/change secondary usage.




Starter comparison: Detmers has the stronger current length/form branch; Ryan retains strong underlying strikeout/control indicators but has a meaningful short-start and hard-contact tail. This produces only a modest Angels winner lean, not a large separation.




#### Bullpen transition / workload




Minnesota's preceding Sep. 18 game:
- Connor Prielipp worked seven innings.
- Tommy Nance handled the eighth and escaped a bases-loaded, no-out jam.
- Travis Adams worked a clean ninth for the save.
- Nance had also worked the 13th inning on Sep. 16; Adams had appeared in that extra-inning game as well. Their recent use is treated as a modest availability/workload consideration, not a quality penalty.
- Jeff Hoffman was not required in the Sep. 18 shutout and remains part of the late-leverage path.




Los Angeles's preceding Sep. 18 game:
- Grayson Rodriguez worked 6 2/3 innings.
- Sammy Peralta covered the transition and Luke Murphy pitched the ninth.
- Ben Joyce, Tayler Saucedo and Blake Weiman were not all forced back into the Sep. 18 game after the Sep. 17 ten-inning contest; the late bullpen therefore has a better-rested branch than if the prior game had been a short-start bullpen game.
- Ben Joyce had allowed the tying two-run Walker Jenkins homer on Sep. 17, which is retained as a realised tail, not converted into an automatic negative performance adjustment.




#### Current offensive diagnostics




Recent results are descriptive only; they do not mechanically shift the model without a current mechanism.




- Minnesota last 30 days: 4.12 R/G, .231/.299/.388.
- Minnesota Sep. 5-19 window: 3.08 R/G, lowest in the cited current MLB-team comparison; the roster has also lost Buxton and Larnach.
- Los Angeles last 30 days: 3.96 R/G, .227/.303/.350.
- Los Angeles latest 15-day window: 3.43 R/G.
- Current series: Angels won 5-4 in 10 innings on Sep. 17; Twins won 3-0 on Sep. 18. These outcomes widen the plausible branches but do not become predictive coefficients.




#### Environment




National Weather Service Anaheim hourly forecast around first pitch:
- about 78°F at 6 PM PDT, falling toward 74°F at 7 PM;
- dewpoint around 64°F;
- southwest wind roughly 7 mph;
- 0% precipitation in the relevant evening window.




No audited park-orientation transform was recovered that justifies assigning the wind a signed run effect, so weather is treated as benign/low-disruption rather than as an Over or Under coefficient.




#### Frozen independent joint run distribution




Model: explicit UNVALIDATED_SUBJECTIVE scenario mixture. Regulation team runs use independent Poisson kernels within each scenario; ties then enter a separately declared MLB automatic-runner extra-inning branch. This is not a fitted, calibrated or prospectively validated model.




1. Central starter control — weight 0.34 — MIN 3.2, LAA 3.6.
2. Detmers suppression / Ryan stable — weight 0.22 — MIN 2.4, LAA 3.3.
3. Ryan short / Angels relief-transition attack — weight 0.18 — MIN 3.2, LAA 4.8.
4. Twins power/contact cluster — weight 0.14 — MIN 5.0, LAA 3.4.
5. Bullpen / HR cluster — weight 0.12 — MIN 4.7, LAA 5.0.




Frozen centre:
- Minnesota runs: 3.456
- Los Angeles runs: 3.890
- PROJECTED TOTAL: 7.346
- PROJECTED ANGELS MARGIN: +0.434
- Regulation total SD: about 2.99 runs
- Regulation margin SD: about 2.87 runs
- Representative score family: Angels 4-3 / Twins 4-3
- Regulation state: MIN win ~36.3%; tie ~14.25%; LAA win ~49.45%.
- Eventual Angels winner branch after explicit extras assumption: ~56.9%.




Extra-inning assumptions are scenario parameters, not empirical calibration:
- Angels win 52% of regulation-tie states.
- Twins +1.5 covers 90% of regulation-tie extra-inning branches.
- Exact total-7 treatment explicitly reallocates low tied scores into eventual Over/Push/Under states rather than pretending extra innings do not exist.




#### Mandatory total projection / 7.0 push audit




PROJECTED TOTAL: 7.346
SUPPLIED TOTAL: 7.0
RAW GAP: +0.346 runs
REGULATION TOTAL SD: ~2.99
NORMALIZED GAP: ~+0.12 SD
ASSESSMENT: CLOSE TO PROJECTION / WEAK MAIN-TOTAL EDGE.




Full-game research probabilities after the explicit extra-inning branch:
- OVER 7.0: ~46.6% WIN
- EXACTLY 7: ~15.9% PUSH
- UNDER 7.0: ~37.5% WIN




Conditional on a non-push:
- Over q ≈ 55.4%
- Under q ≈ 44.6%




The preferred supplied total side is therefore Over 7.0, but it is not a strong total call. The large push mass is why neither total direction belongs near the top of the overall supplied ranking by unconditional win probability.




Team-score budget:
- MIN 2-3 + LAA 3-4 produces 5-7 and is Under/Push territory.
- MIN 3-4 + LAA 4 produces 7-8 and straddles the target.
- Ryan-short states with LAA 5 plus ordinary MIN 3-4 clear the total.
- Detmers suppression plus weak Angels conversion can produce 2-3 / 3-3 regulation states.
- A 3-3 regulation tie is especially important: the automatic runner can convert what was an Under through nine into a final Push or Over.




#### Supplied-slate ranking




1. MINNESOTA TWINS +1.5 — ~63.4% UNVALIDATED_SUBJECTIVE.
   Decomposition: every Minnesota win covers, every Angels one-run win covers, and most tied-regulation extra-inning decisions still finish within one run.
   Main failure: Ryan's short-start/contact tail plus a multi-run Angels sequence produces a 2+ Los Angeles win.




2. LOS ANGELES ANGELS ML — ~56.9%.
   Why: Detmers owns the stronger current length/form branch; Minnesota's offence is missing Buxton/Larnach and has been weak in the latest current-regime window; Ryan's post-IL outings have both been short.
   Main failure: Ryan's underlying K/BB skill reasserts, Walker Jenkins/Keaschall/Jeffers generate enough damage against Detmers, and the stronger Minnesota overall season profile wins a close game.




3. OVER 7.0 — ~46.6% win / ~15.9% push / ~37.5% loss; q(non-push) ~55.4%.
   Why preferred to Under: independent centre is 7.35 and Ryan's length/contact tail plus the MLB extra-inning branch supply plausible 5-3 / 4-4-to-extras states.
   Why not high-ranked: the target is only 0.12 SD below the centre and both offences have current suppression mechanisms.




4. UNDER 7.0 — ~37.5% win / ~15.9% push / ~46.6% loss; q(non-push) ~44.6%.
   Why live: Detmers' seven-QS run, Ryan's underlying skill and both offences' current scoring weakness create genuine 3-2 / 4-2 / 3-3 regulation states.
   Why last: a push is not a win under the ranking objective, and the frozen centre sits slightly above seven.




Supplied-line dependence:
- Angels ML and Twins +1.5 are not independent and can both win when Los Angeles wins by exactly one run.
- They cannot both lose in a normally actioned completed game: a Twins win cashes +1.5, while an Angels 2+ win cashes Angels ML.
- Approximate overlap is the Angels one-run-win state, including extra-inning one-run decisions; the model places material mass there.
- Over 7.0 and Under 7.0 are push-capable opposites, not binary complements.




#### Best four model-selected targets




Candidate-slate discipline: to avoid trivially inflating hit probability by choosing arbitrarily wide alternates, self-selected lines are limited to nearby/common thresholds around the user's requested markets plus one exposure-linked pitcher threshold. Operator availability is not asserted.




1. REID DETMERS 5+ STRIKEOUTS — ~82% UNVALIDATED_SUBJECTIVE.
   Exposure chain: seven consecutive quality starts support roughly 21-27 batter central exposure; 2026 Statcast K% snapshot is 28.3%; latest start produced eight strikeouts in six innings.
   Main failure: early contact/traffic forces a short outing or Minnesota suppresses two-strike conversion.




2. MINNESOTA TWINS +2.5 — ~76-77%.
   Why: the joint margin distribution is centred near Angels +0.43; this survives Minnesota wins plus one- and two-run Angels wins and is much more robust to the Ryan-short branch than +1.5.
   Main failure: Angels separation through Ryan's early exit followed by middle-relief damage.




3. MINNESOTA TEAM TOTAL UNDER 4.5 — ~70%.
   Why: independent MIN centre is 3.46; Detmers' current length plus strikeout profile and Minnesota's depleted/low-scoring current regime support a four-or-fewer central outcome.
   Main failure: Detmers' home-run/contact variance or late Angels bullpen leakage after a competitive start.




4. FULL-GAME UNDER 8.5 — ~63-64%.
   Why: 8.5 sits materially above the 7.35 independent centre and protects against the exact-7 push issue.
   Main failure: Ryan exits early and both middle-relief groups encounter an HR/sequence cluster; extra innings also erode Under protection in tied high-regulation states.




The model-selected slate is not independent: Detmers 5+ K, Minnesota TT Under 4.5 and Under 8.5 share a Detmers-control / Minnesota-suppression driver.




Top-two model dependence cannot be honestly assigned a single joint probability from the current joint score object because the Detmers strikeout module is exposure-linked but not fully coupled to the team-score simulator. Valid Fréchet bounds for Detmers 5+ K (~82%) and Twins +2.5 (~76-77%) put joint success roughly between 59% and 77%; JOINT_UNQUANTIFIED beyond those bounds.




#### Potential game winner




LOS ANGELES ANGELS — ~56.9% eventual-win estimate.




This is a modest lean, not a strong winner call. Twins +1.5 ranks above Angels ML because a low-scoring close game creates a broad overlap region in which Los Angeles wins by one and both contracts succeed.




#### Integrity flags




- PREGAME / SCHEDULED AT FREEZE
- PREFLIGHT PASS / ZERO BLOCKS
- MLB_ALL_CLUB_LINEUP_INDEX_POSTED_ORDERS; TEAM_SPECIFIC_LINEUP_CACHE_TBD
- EXACT_OPERATOR_LISTED_PITCHER/ACTION/VOID TERMS UNKNOWN
- UNVALIDATED_SUBJECTIVE_DISTRIBUTION
- INTEGER_TOTAL_PUSH_EXPLICIT
- MARKET ODDS / IMPLIED PROBABILITY / LINE MOVEMENT / SPORTSBOOK PREVIEWS / TIPSTERS / FANTASY-DFS EXCLUDED
- Original issue status: UNSETTLED — PREGAME FORECAST / NO RETROSPECTIVE




#### Sources / provenance




1. MLB Probable Pitchers — exact event, venue, scheduled time, Ryan/Detmers identities and current headline stats — PRIMARY FIELD OWNER — https://www.mlb.com/probable-pitchers
2. MLB Starting Lineups — current all-club posted batting orders — PRIMARY FIELD OWNER — https://www.mlb.com/starting-lineups
3. MLB Twins/Angels probable-pitcher pages — team-side exact-event corroboration — PRIMARY TEAM/FIELD OWNER.
4. MLB Twins injury/transaction records — Buxton, Larnach, Culpepper and Ryan availability — PRIMARY TEAM/FIELD OWNER.
5. MLB Angels injury/transaction records — Paris, Schanuel, Natera and Bachman availability — PRIMARY TEAM/FIELD OWNER.
6. MLB Joe Ryan Sep. 13 report / film record — 4.0 IP, 4 ER, 84 pitches and current post-IL workload context — PRIMARY FIELD OWNER.
7. MLB Reid Detmers Sep. 14 film record — 6.0 IP, 3 ER, 8 K and seventh straight quality start — PRIMARY FIELD OWNER.
8. Baseball Savant / MLB — Ryan and Detmers Statcast xwOBA/xERA/K/BB/contact and arsenal snapshots — PRIMARY MLB TRACKING SOURCE.
9. Reuters / Field Level Media — Detmers latest start and current series/game context — HIGH-QUALITY INDEPENDENT.
10. AP / StatMuse exact Sep. 18 game record — bullpen transition and preceding-game usage cross-check — INDEPENDENT SECONDARY / structured diagnostic.
11. StatMuse / Retrosheet — current L14/L15/L30 scoring diagnostics — INDEPENDENT STRUCTURED DIAGNOSTIC.
12. National Weather Service — venue-area hourly temperature, dewpoint, wind and precipitation — GOVERNMENT FIELD OWNER.
13. Sports Research Drive — METHOD.md, RULES_BASEBALL.md, RULES_GENERAL.md, UPCOMING_GAME_RESEARCH_GUIDE.md, DATA_SOURCE_REGISTER.md, CONTROL_MANIFEST_2026-09-19.md and forecast preflight validator — GOVERNING METHODOLOGY.




Source firewall: no sportsbook odds, market consensus, implied probabilities, line movement, betting previews/picks, tipsters, fantasy/DFS projections or ownership data were admitted as predictive inputs. User-supplied contracts were queried only after the independent distribution was frozen and hashed.




#### Document mapping / candidate learnings




- Ryan's post-IL skill and current starter length must remain separate exposure dimensions -> existing RULES_BASEBALL starter-BF/pitch-count/hook control.
- Exact 7.0 produces material push mass -> current SCORING_AND_VALIDATION push-capable W/P/L requirement; no new rule needed.
- Full MLB lineup index versus lagging team-specific TBD cache -> DATA_SOURCE_REGISTER retrieval/latency observation only.
- Detmers current length plus Twins roster depletion supports a suppression branch, but Ryan hard-contact/short-start and MLB extras preserve an upper tail -> existing cluster, relief-transition and extras controls; no fixed coefficient added.




---




#### Settlement and retrospective — P-476


Settlement status: SETTLED / RETROSPECTIVE COMPLETE.
Verified final: Los Angeles Angels 6, Minnesota Twins 5 in 11 innings.
Actual full-game total: 11 runs.
Actual margin: Angels +1.


Three-source final-state gate: PASS.
- Reuters / Field Level Media: explicit Angels 6-5 final in 11 innings.
- CBS/AP exact-game recap/box score: explicit 6-5 final and 11-inning pitching/stat record.
- Independent local/secondary game recap corroboration plus MLB event video/stat records for pitcher-specific settlement.


Settlement sources:
- Reuters final recap: https://www.reuters.com/sports/baseball/angels-rally-ninth-take-down-twins-11th--flm-2026-09-20/
- CBS Sports exact-game recap / box score, Sep 19, 2026.
- MLB Joe Ryan game video: https://www.mlb.com/video/joe-ryan-strikes-out-five-x4706
- MLB scores/event record, Sep 19, 2026.


##### Pick-by-pick settlement — supplied slate


1. Twins +1.5 — WIN; Minnesota lost by one.
2. Angels ML — WIN.
3. Over 7.0 — WIN; final total 11.
4. Under 7.0 — LOSS.


Potential game winner: Los Angeles Angels — WIN.


##### Pick-by-pick settlement — model-selected slate


1. Reid Detmers 5+ strikeouts — WIN, exactly 5 strikeouts in 5.0 innings.
2. Twins +2.5 — WIN.
3. Minnesota team total Under 4.5 — LOSS; Minnesota scored 5.
4. Full-game Under 8.5 — LOSS; final total 11.


##### Ranking / top-two review


Supplied Rank #1 Twins +1.5 and Rank #2 Angels ML both won. This is the precise overlap state described pre-game: Los Angeles won by exactly one run, so both contracts succeeded. Hit@2 = YES; both-win = YES; the dependence logic was correct and important.


Model-selected Rank #1 Detmers 5+ K won exactly at the threshold, and Rank #2 Twins +2.5 also won.


No Rank-1 failure trigger applies.


##### Enhanced totals review


The supplied Over 7.0 won, but the self-selected Under 8.5 lost. Because the card contained competing total targets across separate slates, the Under 8.5 miss is reviewed to the enhanced standard rather than ignored.


Why Under 8.5 was selected:
- Independent centre was 7.346.
- Detmers' current length/strikeout form plus Minnesota roster depletion supported suppression.
- 8.5 appeared to provide a meaningful cushion above the centre.


Why it failed:
- Minnesota had already built a 5-2 lead entering the bottom of the eighth.
- Adam Frazier's two-run pinch-hit double cut it to 5-4.
- Vaughn Grissom's ninth-inning solo homer tied the game 5-5.
- The game then entered MLB automatic-runner extra innings and Christian Moore drove in the winning run in the 11th, producing the 6-5 final.
- Thus the late relief-transition + tie + extra-inning branch added four runs after the game stood at seven through seven innings.


The supplied Over 7.0 benefited from exactly the extra-inning/late-cluster mechanism that the pre-game card explicitly preserved. The self-selected Under 8.5 did not leave enough room for that same tail.


Pitcher reality:
- Joe Ryan: 5 innings, 2 runs, 5 strikeouts.
- Reid Detmers: 5 innings, 4 runs, 5 strikeouts.
Ryan did not realize the forecast's most damaging short-start branch. Detmers also failed to produce the central six-plus-inning quality-start suppression branch, though his 5+ K prop still landed exactly.


Could Under 8.5 have been ranked lower ex ante?
Yes, relative to the supplied Over 7.0, because the same joint object carried ~14% regulation-tie mass and explicitly acknowledged automatic-runner scoring. An Under above the centre can still be reasonable, but the card should not let the central 7.35 estimate dominate the tie/late-bullpen tail when selecting a nearby 8.5 threshold.


Smallest justified improvement:
For MLB self-selected Unders, explicitly report the probability mass of tie-after-nine and late relief-transition states that can cross the alternate threshold, not merely the distance from the central total. This is already required conceptually by BB-B5 and BB-B7; the issue is execution, not a new fixed penalty.


##### What went right


- Angels winner was correct.
- Twins +1.5 correctly captured the close-game distribution.
- The exact one-run Angels win validated the non-independence explanation for the top two supplied picks.
- Over 7.0 was correctly preferred to Under 7.0.
- Detmers 5+ strikeouts won exactly.
- The pre-game analysis explicitly warned that a 3-3 or other tied regulation state could turn an Under/Push into an Over through automatic-runner extras; the realised game followed that general late/extras mechanism.


##### What went wrong


- Minnesota scored 5, defeating the Minnesota TT Under 4.5.
- Detmers allowed four runs in five innings, so the Detmers-suppression branch was too strong relative to his realised run prevention.
- Under 8.5 understated late bullpen/extras scoring despite the model already identifying those states.
- The game did not require Ryan's early-collapse branch to reach 11 runs; late-game scoring was enough.


##### Availability / lineup / source audit


The pre-game card recovered MLB's all-club posted orders but recorded an intra-MLB cache inconsistency on team-specific lineup pages. That uncertainty was transparently logged rather than hidden. No material postgame evidence shows that an unmodelled late scratch was the central cause of the miss; the dominant mechanism was late relief/extras.


For Detmers 5+ K, CBS box-score data records 5.0 IP and 5 strikeouts, so the prop settles as a WIN.


##### Source audit


- Reuters: retained as high-quality independent game-script/final source.
- CBS/AP: retained for final and detailed box score.
- MLB official event/player video: retained as field-owner pitcher-event corroboration.
- Search snippets or stale live feeds are not used to override the explicit final sources.


##### Blind spots and mitigation


Blind spot: underweighting late relief + automatic-runner extras when selecting Under 8.5.
Pre-game knowability: YES as a structural tail, but not its exact realization.
Materiality: HIGH for Under 8.5 and MIN TT Under 4.5; LOW for winner/+run-line selections.
Mitigation: display the tie-after-nine and late-relief threshold-crossing mass before ranking a nearby alternate Under.


##### Document mapping


- RULES_BASEBALL.md — BB-B5 relief transition and BB-B7 extras already cover the failure mechanism; execution reminder only.
- SCORING_AND_VALIDATION.md — preserve push-aware 7.0 handling; the supplied Over correctly won outright rather than pushing.
- DATA_SOURCE_REGISTER.md — retain MLB all-club versus team-page lineup-cache latency observation.
- Prediction log — record the exact one-run top-two overlap success and Under 8.5 extras-tail miss.




---




### P-477 — Australia NBL — Sydney Kings vs Cairns Taipans
- Canonical / staging ID: P-477
- Competition: Australia NBL27, Round 1
- Venue: Afterpay Arena, Sydney Olympic Park, New South Wales, Australia
- Official scheduled start: Sep 20, 2026 at 5:00 PM AEST
- Original research state: PREGAME / SCHEDULED at final pre-issue refresh
- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-BASKETBALL
- Operating mode: SPORTS_ONLY / MARKET_BLIND
- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE
- No retrospective performed.
#### Original pre-game prediction
Independent frozen centre:
- Sydney Kings: approximately 97 points
- Cairns Taipans: approximately 90 points
- PROJECTED TOTAL: approximately 186.7
- PROJECTED SYDNEY MARGIN: approximately +7.2
- Representative score: Sydney 97-90 Cairns
Best four model-selected targets:
1. SYDNEY KINGS ML — ~70% UNVALIDATED_SUBJECTIVE.
2. OVER 179.5 TOTAL POINTS — ~69%.
3. UNDER 191.5 TOTAL POINTS — ~63%.
4. CAIRNS TAIPANS +11.5 — ~61%.
Supplied-slate ranking:
1. OVER 185.5 — ~53.3%.
2. CAIRNS +8.5 — ~52.9%.
3. SYDNEY -8.5 — ~47.1%.
4. UNDER 185.5 — ~46.7%.
Potential game winner:
SYDNEY KINGS — ~70%.
#### Original research reasoning / availability
- Sydney retained a championship-level core led by Kendric Davis, Matthew Dellavedova, Torrey Craig and Xavier Cooks, with Andrew Carr added to the frontcourt.
- Davis had a shortened preparation because passport issues delayed his return to Australia; availability was not treated as equivalent to perfect opening-night rhythm.
- Cairns' current roster was treated as materially stronger offensively than the prior-season team, with Jack McVeigh, Keanu Pinder, Jaylon Brown, Reyne Smith and Malique Lewis providing multiple scoring paths.
- Confirmed absences at issue: Sydney — Keli Leaupepe; Cairns — Jaylin Galloway and Luke Paul.
- Expected/projected starting fives were retrieved, but a formal final confirmed starting five for both clubs was not recovered to gate standard before issue. Rotation-sensitive player props were therefore not promoted.
- The supplied -8.5 and 185.5 thresholds were close to the independent centre, so the winner and nearby alternate thresholds were considered more robust.
#### Material pre-game sources
1. NBL exact-game preview / talking points — event identity, expected depth charts and current team context — PRIMARY LEAGUE — https://league.nbl.com.au/news/how-to-watch-talking-points-sydney-v-cairns-fnm29
2. NBL / Cairns club schedule — exact event/date/time — PRIMARY LEAGUE — https://www.nbl.com.au/club-schedule/cairns
3. Sydney Kings club schedule / team material — schedule and roster context — PRIMARY TEAM — https://www.nbl.com.au/club-schedule/syd
4. Cairns Taipans injury report — Jaylin Galloway and Luke Paul availability — PRIMARY TEAM — https://www.taipans.com/news/injury-report-round-1-nbl27
5. NBL team/statistical and preseason reports — current roster/process context and Cairns final preseason scoring — PRIMARY LEAGUE.
6. Sydney Kings official preseason reporting — current rotation/process context — PRIMARY TEAM.
7. Sports Research Drive — METHOD.md, RULES_BASKETBALL.md, RULES_GENERAL.md, CONTROLS.md, DATA_SOURCE_REGISTER.md and current control manifest — GOVERNING METHODOLOGY.
Source firewall: sportsbook odds, betting picks, prediction markets, line movement, fantasy/DFS projections and betting-derived analysis were excluded from predictive inputs.


#### Settlement and retrospective — P-477


Settlement status: SETTLED / RETROSPECTIVE COMPLETE.
Verified final: Sydney Kings 111, Cairns Taipans 90.
Actual full-game total: 201 points.
Actual margin: Sydney +21.


Three-source terminal-state gate: PASS.
1. NBL / AAP postgame report — explicit Sydney 111-90 Cairns final, quarter-by-quarter scoring and player statistics — PRIMARY LEAGUE / INDEPENDENT AAP REPORTING — https://league.nbl.com.au/news/kings-open-title-defence-in-style
2. Cairns Taipans official postgame report — explicit 111-90 defeat plus game script and player statistics — PRIMARY TEAM — https://www.taipans.com/news/pinder-stars-but-taipans-fall-to-kings
3. Austadiums exact-event record — explicit 111-90 Final, Sep 20 2026, 5:00 PM at Afterpay Arena — INDEPENDENT EVENT RECORD — https://www.austadiums.com/sport/event/34482


##### Pick-by-pick settlement — model-selected slate


1. Sydney Kings ML — WIN.
2. Over 179.5 total points — WIN; actual total 201.
3. Under 191.5 total points — LOSS; actual total 201.
4. Cairns Taipans +11.5 — LOSS; Cairns lost by 21.


##### Pick-by-pick settlement — supplied slate


1. Over 185.5 — WIN; actual total 201.
2. Cairns +8.5 — LOSS; Cairns lost by 21.
3. Sydney -8.5 — WIN; Sydney won by 21.
4. Under 185.5 — LOSS.


Potential game winner: Sydney Kings — WIN.


##### Rank-1 / top-two review


Model-selected Rank #1 Sydney ML won and Rank #2 Over 179.5 also won.
Rank-1 success = YES.
Hit@2 = YES.
Both top-two win = YES.
No Rank-1 failure trigger applies.


The ordering was defensible: Sydney's deeper championship core and the independent +7.2 margin centre supported the winner, while Over 179.5 sat materially below the 186.7 total centre. The realised 21-point margin was substantially wider than projected, but that does not invalidate Sydney ML being ranked first.


##### Enhanced totals review


The highest-ranked model-selected over/under, Over 179.5, WON. The highest-ranked supplied over/under, Over 185.5, also WON. No TOP_OU_REVIEW failure trigger applies.


The nearby upper Under 191.5 lost because the game reached 201. Sydney scored 32 in Q1, 59 by halftime and 31 more in Q3, including 6/9 from three in that third period. The pre-game centre of 186.7 therefore underweighted the upper scoring tail. The correct lesson is not to reverse every nearby Under; it is to make the high-variance perimeter/transition branch explicit before ranking an upper Under close to the centre.


##### Expected game script vs actual


Expected: Sydney as the more likely winner, Cairns materially improved offensively, central score around 97-90, and a competitive game with enough scoring to prefer a lower Over.
Actual: Cairns led 14-8 early and remained within six at halftime, 59-53, so the competitive early branch was real. Sydney then separated decisively in the third quarter, leading 90-73 after three and finishing 111-90.


The largest forecast miss was separation/upper-tail magnitude, not winner direction. Projected Sydney margin was +7.2 versus +21 actual; projected total was 186.7 versus 201 actual.


##### What went right


- Sydney winner call was correct.
- Model Rank #1 and Rank #2 both won.
- The lower alternate Over 179.5 correctly captured a game with significant offensive upside.
- Supplied Over 185.5 was correctly preferred to Under 185.5.
- The pre-game absence check correctly had Luke Paul and Jaylin Galloway unavailable for Cairns; the NBL postgame report says Cairns still had both to come into the team.
- Pinder was correctly treated as a major Cairns offensive path; he delivered 27 points.


##### What went wrong


- Under 191.5 was too aggressive relative to the model's own uncertainty and lost by 9.5 points.
- Cairns +11.5 and +8.5 underestimated Sydney's separation tail.
- The central forecast did not place enough weight on a Sydney perimeter burst: six Kings finished in double figures and the third quarter was driven by hot outside shooting.
- Cairns' 13/44 three-point shooting created a high-volume, low-efficiency possession profile that widened the margin while still allowing the combined total to reach 201.
- Jack McVeigh scored only seven, while Cairns' foul trouble also reduced their ability to sustain the halftime response.


##### Starting-lineup / availability audit


Confirmed pre-game absences that were modelled: Sydney — Keli Leaupepe; Cairns — Jaylin Galloway and Luke Paul.
Exact field-owner starting fives were not recovered before issue and this remains an evidence limitation. No postgame source recovered in this settlement pass indicates that an unmodelled late withdrawal was the primary cause of the result.


##### Blind spots and mitigation


Blind spot: insufficient mass on a high-scoring Sydney separation branch in an opening-round game with strong shooting depth.
Pre-game knowability: PARTLY. Sydney's depth was known, but the exact 6/9 third-quarter three-point burst was not predictable.
Materiality: HIGH for Under 191.5 and Cairns spreads; LOW for Sydney ML and the lower Over.
Mitigation: when the centre supports an Over but an upper Under is also selected, explicitly quantify the branch in which favourite shooting efficiency plus opponent high-volume perimeter attempts create both a larger margin and a higher total. This is an execution reinforcement of existing distribution/tail controls, not a new fixed coefficient.


##### Source-quality audit


- NBL/AAP: retained as a high-quality league-hosted final/game-script source.
- Cairns Taipans official: retained as a primary team result and availability source.
- Austadiums: useful independent explicit-final corroboration for exact event/date/venue.
- NBL public schedule shell: do not use its generic LIVE NOW label as proof of event state; it displayed that label on future fixtures during the earlier check.


##### Document mapping / learnings


- DATA_SOURCE_REGISTER.md: candidate source-state observation — NBL public schedule LIVE NOW labels can be shell-level and must not control event state without an exact-event terminal source.
- RULES_BASKETBALL.md / SCORING_AND_VALIDATION.md: execution note only — nearby upper Unders require explicit upper-tail/separation mass when the same card already recognizes strong favourite shooting depth.
- No permanent sport-specific or cross-sport rule promoted from this single event.
- Dataset status remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.


---




### P-478 — Soccer / Sweden Allsvenskan — Djurgårdens IF vs IF Elfsborg
- Canonical / staging ID: P-478
- Competition: Sweden Allsvenskan 2026, Round 22
- Venue: 3Arena, Stockholm, Sweden; artificial surface
- Official venue-local start: Sep 20, 2026 at 14:00 CEST (Europe/Stockholm, UTC+2)
- Australia/Melbourne conversion: Sep 20, 2026 at 22:00 AEST (UTC+10); calendar-date rollover = NO
- Independent distribution freeze: approximately Sep 20, 2026 at 22:01 AEST
- Issuance state: START_CROSSED_UNVERIFIED / LATE-ISSUED RESEARCH FORECAST. The scheduled kickoff crossed while the required research was being completed; the structured event feed still showed Scheduled. No live score, shot, corner, card, substitution, possession or other in-game observation is admitted into the forecast.
- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-SOCCER
- Operating mode: SPORTS_ONLY / MARKET_BLIND
- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE
- Distribution ID: P-478-dist-v1
- Distribution SHA-256: 605b2c4ca216a77088c4df63f4f8224373c70b9370fd59e7b90d4e481d78b8ea
- No retrospective performed.
#### Identity / supplied contracts
User-supplied contracts were parsed only for identity and quarantined until after the independent goal distribution was frozen:
- First-half Over 0.5 goals
- First-half Under 0.5 goals
- Full-game Over 2.5 goals
- Full-game Under 2.5 goals
Research endpoint is regulation 90 minutes plus stoppage time. No extra-time/penalty endpoint applies to this Allsvenskan league fixture. Exact operator-specific action/void rules were not supplied.
#### Event/time/source gate
Official Djurgården and Elfsborg pages both identify Sunday Sep 20 at 14:00 local at 3Arena. The Allsvenskan round schedule independently lists the same fixture in Round 22. Melbourne conversion is 22:00 AEST.
At the final state refresh after the scheduled time crossed, the structured soccer event route still returned Scheduled and a zero-filled shell rather than a verified live sequence. Because scheduled-start crossing itself blocks a normal pregame issuance under the active controls, this is recorded as a late-issued research forecast rather than retroactively called a normal pregame PASS.
#### Participants / availability
Exact field-owner starting XIs were not recoverable through the accessible official Djurgården page: its preview still stated that the squad would be published one hour before kickoff. High-quality/current lineup feeds and recent official club selections converge on the following role-continuity XI shapes, but they are not relabelled official-confirmed:
Djurgården 4-2-3-1:
Jacob Rinne; Adam Ståhl, Miro Tenho, Jacob Une Larsson, Piotr Johansson; Daniel Stensson, Matias Siltanen; Patric Åslund, Bo Hegland, Jeppe Okkels; Kristian Lien.
Elfsborg 4-2-3-1:
Isak Pettersson; Alexander Jensen, Rasmus Wikström, Thomas Isherwood, Niklas Hult; Julius Magnússon, Simon Olsson; Momoh Kamara, Julius Beck, Arbër Zeneli; Leo Östman.
Role continuity is strong: Djurgården's official Sep 14 2-0 win over GAIS used the same XI; Elfsborg's official Sep 13 1-0 win over Kalmar used the same XI.
Material availability:
- Djurgården: Christos Almyras suspended after the red card versus GAIS. He was not part of the above recent starting XI, so this is primarily a bench/rotation loss rather than a starting-XI removal.
- Elfsborg: Per Frick is unavailable with a broken hand in current independent availability feeds. He was used as a late substitute in the Sep 13 official match record, so his loss affects late attacking depth more than the projected starting structure.
- No unsupported late-scratch claim is added.
Participant limitation: exact official matchday benches/final XIs were not recovered to field-owner standard before issue. Player props are therefore not ranked, and lineup-sensitive rows retain an evidence cap.
#### Current team/process evidence
Season through 21 Allsvenskan matches:
- Djurgården: 2nd, 41 points, 46 goals for / 19 against; xG 40.3 / xGA 26.0.
- Elfsborg: 34 points, 29 goals for / 21 against; xG 29.1 / xGA 25.7.
Djurgården have five straight Allsvenskan wins entering this fixture. The latest official home result was 2-0 over GAIS, with Lien scoring before halftime and Hegland after halftime. The streak is treated as descriptive; the signed view comes from current creation/defence/roster mechanisms rather than a momentum coefficient.
Elfsborg's latest official league result was 1-0 over Kalmar, with a 0-0 first half and Momoh Kamara scoring in the 51st minute. Their recent league sequence includes 1-1 at Göteborg, 2-0 over Degerfors, 1-2 at Brommapojkarna and 1-0 over Kalmar.
First-half evidence:
- Djurgården have scored in the first half in 67% of league matches overall and approximately 82% of home matches in the current sample.
- Elfsborg have scored in the first half in 43% overall / 40% away, while conceding about 0.40 first-half goals per away match.
- Recent Djurgården first-half xG examples include 0.80 vs GAIS, 2.10 vs Mjällby at home, 0.72 away to Mjällby and 0.44 at Malmö.
- Elfsborg's recent first-half creation has varied rather than consistently spiked.
This creates an early-goal lean driven mainly by Djurgården home creation, while Elfsborg's first-half defensive record prevents treating Over 0.5 as a high-certainty row.
#### Corner process
Corners are modelled separately from goals.
- Djurgården: 6.4 corners taken per Allsvenskan match, third-highest league rate in the cited current table.
- Elfsborg: 4.1 taken per match.
- Allsvenskan baseline: approximately 5.1 corners per team per match; home teams about 5.5, away teams about 4.8.
- Djurgården's recent individual corner counts: 2, 6, 3, 4, 7, 5, 7, 5, 6, 13 across the cited ten-match sequence.
- Score-state mechanism: a Djurgården lead can reduce their later attacking/corner demand, while an Elfsborg chasing state can add width/cross/end-line exposure. This prevents treating Djurgården territorial superiority as a one-sign team-corner guarantee.
Explicit corner-total scenario mixture produces an expected total around 9.4 corners. Over 7.5 is approximately 71% under the unvalidated subjective model. Exact operator/provider availability is not asserted.
#### Environment
SMHI's Stockholm-area forecast for Sep 20 shows roughly 12-16 C, south-westerly wind around 6 m/s with gusts around 14 m/s and some precipitation risk. 3Arena uses an artificial surface. Weather is retained as a mechanism/variance factor for long balls, crossing and set plays; no automatic Over/Under coefficient is applied.
#### Frozen independent goal distribution
Model: UNVALIDATED_SUBJECTIVE scenario mixture with independent Poisson goal kernels inside each state. It is not fitted, calibrated or prospectively validated.
1. Central Djurgården territorial/home-control state — weight 0.36 — DJU 1.9, ELF 0.9.
2. Djurgården pressure + Elfsborg compact/suppressed attack — 0.24 — DJU 2.2, ELF 0.7.
3. Elfsborg counter/resistance branch — 0.18 — DJU 1.6, ELF 1.2.
4. Closed top-table/keeper branch — 0.14 — DJU 1.4, ELF 0.6.
5. Open transition/set-piece/weather-variance branch — 0.08 — DJU 2.5, ELF 1.5.
Frozen centre:
- Djurgården goals: ~1.90
- Elfsborg goals: ~0.91
- PROJECTED TOTAL: ~2.81
- Representative score family: Djurgården 2-1 / 2-0 / 1-1
- Djurgården regulation win: ~60.2%
- Draw: ~21.9%
- Elfsborg regulation win: ~17.9%
- Djurgården-or-draw: ~82.1%
Full-game total:
- Over 2.5: ~52.6%
- Under 2.5: ~47.4%
The supplied 2.5 line is therefore close to the independent centre and is not a strong full-game-total call.
First-half model:
- first-half centre ~1.11 goals
- Over 0.5 first-half goals: ~66.5%
- Under 0.5: ~33.5%
#### Best five model-selected targets
Candidate-slate discipline: thresholds are common/nearby soccer contracts, not arbitrarily wide alternates, and operator availability is not asserted.
1. DJURGÅRDEN TEAM TOTAL OVER 0.5 GOALS — ~84.2% UNVALIDATED_SUBJECTIVE.
   Main mechanism: ~1.90 home scoring centre, 46 season goals, 40.3 xG, and a current XI retaining Lien/Hegland/Åslund/Okkels.
   Main failure: Elfsborg's defensive/keeper branch plus finishing variance produces 0-0 or a narrow away result.
2. DJURGÅRDEN OR DRAW (1X) — ~82.1%.
   Main mechanism: stronger current season attack/defence profile and home control.
   Main failure: Elfsborg absorbs territory and wins a low-event transition/set-piece game.
3. ELFSBORG TEAM TOTAL UNDER 1.5 GOALS — ~76.8%.
   Main mechanism: Elfsborg centre ~0.91, Djurgården 19 goals conceded in 21 matches and recent defensive suppression.
   Main failure: Djurgården turnover/set-piece errors or an early Elfsborg goal forcing an open score-state.
4. TOTAL CORNERS OVER 7.5 — ~71.2%.
   Main mechanism: Djurgården 6.4 corners taken/game, Elfsborg 4.1, plus trailing-state width/cross exposure.
   Main failure: early efficient finishing reduces shot-block/end-line sequences or both sides attack centrally with low corner conversion.
5. FULL-GAME UNDER 3.5 GOALS — ~68.9%.
   Main mechanism: the central total is 2.81; Elfsborg's attack is materially below Djurgården's and both clubs have credible low-event/keeper branches.
   Main failure: an early goal creates transition space and the match enters the open 2-2 / 3-1 family.
The user-supplied first-half Over 0.5 (~66.5%) is narrowly outside the model top five but remains the preferred supplied first-half side.
#### Supplied-market ranking
1. FIRST-HALF OVER 0.5 GOALS — ~66.5% — preferred.
2. FULL-GAME OVER 2.5 GOALS — ~52.6% — very weak lean / close to projection.
3. FULL-GAME UNDER 2.5 GOALS — ~47.4%.
4. FIRST-HALF UNDER 0.5 GOALS — ~33.5%.
Forced-pair integrity:
- 1H Over 0.5 + 1H Under 0.5 = 100% conditional on action.
- FT Over 2.5 + FT Under 2.5 = 100% conditional on action.
No push exists at either half-goal threshold.
#### Potential game winner
DJURGÅRDEN — ~60.2% regulation-win estimate.
This is a clear but not overwhelming winner lean. Draw mass remains approximately 21.9%, which is why 1X ranks materially above the outright win.
#### Dependence / kill-path audit
The top selections are not independent:
- Djurgården TT Over 0.5 and 1X share the home attack/control driver.
- Elfsborg TT Under 1.5 also positively overlaps with a Djurgården-control state.
- Under 3.5 can win with 1X in 1-0, 2-0, 1-1 and 2-1 outcomes, but loses in high-separation/open states.
- Corner Over 7.5 is only partially linked to goals because trailing-state width can raise corners even when finishing is poor.
Top-two exact joint probability is not honestly identified by the current marginal goal model beyond the same score grid; the pair is highly dependent and is not presented as a parlay probability.
#### Integrity flags
- START_CROSSED_USER_OVERRIDE / PF-EVENT-STATE BLOCK
- NO_LIVE_GAME_STATE_USED_IN_MODEL
- EXACT_OFFICIAL_MATCHDAY_XIS/BENCHES_NOT_RECOVERED_TO FIELD-OWNER STANDARD
- CURRENT ROLE-CONTINUITY XIS RECOVERED FROM OFFICIAL PRIOR MATCHES + INDEPENDENT CURRENT LINEUP FEEDS
- MARKET ODDS / IMPLIED PROBABILITY / LINE MOVEMENT / SPORTSBOOK PREVIEWS / TIPSTERS / FANTASY-DFS EXCLUDED
- UNVALIDATED_SUBJECTIVE_DISTRIBUTION
- Current status: UNSETTLED — LATE-ISSUED RESEARCH FORECAST / NO RETROSPECTIVE
#### Sources / provenance
1. Djurgården official preview — exact event, 3Arena, 14:00 local, suspension/warning state — PRIMARY TEAM — https://www.dif.se/nyheter/2026/infor-djurgarden-elfsborg
2. Djurgården official schedule / date announcement — exact fixture time — PRIMARY TEAM — https://www.dif.se/nyheter/2026/speldatum-satta-for-omgang-18-23-i-allsvenskan
3. IF Elfsborg official supporter/schedule information — exact event/date/time — PRIMARY TEAM — https://elfsborg.se/2026/09/15/supporterinfo-djurgardens-if-borta-1/
4. Allsvenskan official round schedule — competition/round identity — PRIMARY COMPETITION — https://allsvenskan.se/nyheter/sa-spelas-omgang-18-23-av-allsvenskan/
5. Djurgården official Sep 14 GAIS report — recent official starting XI, availability and 2-0 game script — PRIMARY TEAM — https://www.dif.se/nyheter/2026/norsk-briljans-visade-vagen-mot-gais
6. Elfsborg official Sep 13 Kalmar report — recent official starting XI, bench usage and 1-0 game script — PRIMARY TEAM — https://elfsborg.se/2026/09/13/kamaras-mal-avgjorde-mot-kalmar/
7. xGstats — current Allsvenskan record, goals and xG/xGA for both clubs — INDEPENDENT STRUCTURED STATISTICAL SOURCE — https://xgstats.com/teams/djurgardens-if and https://xgstats.com/teams/if-elfsborg
8. FootyStats / SoccerStats — current first-half scoring/conceding splits and home/away scoring rates — INDEPENDENT STRUCTURED DIAGNOSTIC.
9. FootyMetrics / Statz — current Allsvenskan corner-for rates and league home/away corner baselines — INDEPENDENT STRUCTURED DIAGNOSTIC.
10. OFStats — Djurgården current shot/possession/corner diagnostics and match-by-match corners — INDEPENDENT STRUCTURED DIAGNOSTIC.
11. FotMob/GioScore current match pages — lineup-role continuity and current availability cross-check; not promoted above official club records — INDEPENDENT CURRENT SECONDARY.
12. SMHI — Stockholm-area current weather forecast — GOVERNMENT WEATHER FIELD OWNER.
13. Structured soccer event feed — exact event ID 67126774 and final pre-issue scheduled-state check — CURRENT EVENT-STATE SOURCE.
14. Sports Research Drive — METHOD.md, RULES_SOCCER.md, RULES_GENERAL.md, CONTROLS.md and current control manifest — GOVERNING METHODOLOGY.
Source firewall: betting-academy, bookmaker, odds, tipster, prediction-market and fantasy/DFS sources surfaced during discovery but were excluded from predictive evidence.
#### Document mapping / candidate learnings
- Official club preview can remain cache-lagged past its promised one-hour-before squad publication -> DATA_SOURCE_REGISTER source-latency observation candidate.
- Early-goal lean was reconciled against Elfsborg's strong first-half defensive numbers rather than driven by Djurgården's recent scoring streak -> existing RULES_SOCCER early-goal control executed; no new rule.
- Corners were derived independently from corner exposure/rates and score-state width rather than from possession/xG dominance -> existing RULES_SOCCER corner-process control executed; no new rule.
- Scheduled-start crossing while the structured event route still shows Scheduled remains a process exception only; do not weaken the normal pregame gate.
#### Completed-event settlement check — derivative still unresolved
Factual event state: COMPLETED.
Verified regulation result: Djurgårdens IF 1, IF Elfsborg 2.
Verified halftime state: Djurgården 0, Elfsborg 1.
Three independent result lineages agree on the completed 1-2 result: the structured exact-event feed (event 67126774, COMPLETE), Aftonbladet/TT's explicit postgame report, and current independent match reporting. The final corner count required to settle Rank #4 Total Corners Over 7.5 was not recovered from a trustworthy final field after attempts through the exact Sofascore match page and additional indexed/stat-provider routes. Pre-match/market-derived corner pages and stale in-game snapshots are not used to manufacture the endpoint.
Resolved-row grading:
1. Djurgården team total Over 0.5 — WIN; Djurgården scored once.
2. Djurgården or Draw (1X) — LOSS; Elfsborg won 2-1.
3. Elfsborg team total Under 1.5 — LOSS; Elfsborg scored twice.
4. Total Corners Over 7.5 — UNRESOLVED_DERIVATIVE / FINAL CORNER FIELD NOT VERIFIED.
5. Full-game Under 3.5 — WIN; three goals.
Supplied slate:
1. First-half Over 0.5 — WIN; Elfsborg led 1-0 at halftime.
2. Full-game Over 2.5 — WIN; final total three.
3. Full-game Under 2.5 — LOSS.
4. First-half Under 0.5 — LOSS.
Potential game winner: Djurgården — LOSS.
##### Partial retrospective on resolved rows
Rank #1 Djurgården TT Over 0.5 won. Rank #2 Djurgården-or-draw lost, so Hit@2 = YES but both-win = NO. No Rank-1 failure trigger applies.
The biggest modelling miss was team/winner separation: the forecast assigned only ~17.9% to an Elfsborg regulation win and ~76.8% to Elfsborg Under 1.5, yet Elfsborg scored twice and won. Aftonbladet/TT reports that Rasmus Wikström's 0-1 just before halftime came through a weak Jacob Rinne intervention. Djurgården improved after halftime and equalised, but Fotbollskanalen's postgame analysis identifies a second structural failure: offensive substitutions increased the home threat but two substitutes failed their defensive assignments, allowing Alexander Jensen to run free and set up Simon Olsson for the decisive 2-1.
What went right:
- Djurgården did score, landing Rank #1.
- First-half Over 0.5 landed.
- Full-game Over 2.5 landed while Under 3.5 also landed, correctly illustrating the 3-goal overlap band.
- The pre-game analysis explicitly preserved an Elfsborg counter/resistance branch rather than treating Djurgården home control as certain.
What went wrong:
- The Elfsborg counter/resistance branch was materially underweighted relative to the realised 2-1 away win.
- Djurgården-or-draw and Elfsborg Under 1.5 both failed.
- The pre-game model did not quantify goalkeeper-error and substitution-driven defensive-transition tails strongly enough for the side/away-team-total distribution.
- Exact matchday XI/bench confirmation was missing at issue; that mattered because the decisive second goal involved substitute defensive responsibilities.
Source audit:
- Aftonbladet/TT postgame — explicit 1-2 final and goal sequence — https://www.aftonbladet.se/senastenytt/ttsport/sport/a/JOdbOX/mardrom-for-djurgarden-jattetavla-och-forlust
- Fotbollskanalen postgame — detailed tactical/substitution explanation of the decisive 1-2 goal — https://www.fotbollskanalen.se/artiklar/allsvenskan/fem-spaningar-slarvigt-och-svagt-av-djurgarden
- Sofascore exact-event route — confirms the correct event and exposes detailed-stat capability, but the accessible indexed response did not expose the final corner count — https://www.sofascore.com/football/match/if-elfsborg-djurgardens-if/jKsmK
- Market/betting pages that surfaced while searching for corners were rejected as settlement evidence.
Document mapping:
- RULES_SOCCER.md: existing bench/substitution and score-state transition controls are relevant; execution reinforcement only.
- DATA_SOURCE_REGISTER.md: exact-event derivative-source latency/coverage note for Allsvenskan corners.
- No final retrospective closeout or permanent rule promotion until the corner derivative is settled.
Formal status: COMPLETED / GOAL+SIDE ROWS GRADED / CORNER DERIVATIVE PENDING / NOT FULLY SETTLED.


#### Final settlement and retrospective — P-478


Settlement status: SETTLED / RETROSPECTIVE COMPLETE.
Verified final: Djurgårdens IF 1, IF Elfsborg 2.
Halftime: Djurgården 0, Elfsborg 1.
Verified final corners: Djurgården 4, Elfsborg 7; total 11.


Three-source terminal-state gate: PASS.
- Structured exact-event soccer feed, event 67126774 — COMPLETE at 1-2.
- IF Elfsborg official postgame report — explicit 1-2 away win and goal sequence — https://ipv6.elfsborg.se/2026/09/20/stark-trepoangare-borta-mot-djurgarden/
- Aftonbladet/TT postgame report — explicit 1-2 final and game narrative — https://www.aftonbladet.se/senastenytt/ttsport/sport/a/JOdbOX/mardrom-for-djurgarden-jattetavla-och-forlust


Corner endpoint cross-check:
- WinDrawWin exact result page: 4-7 corners.
- BetStudy exact result page: 4-7 corners.
- TotalCorner exact H2H/result row: 4-7 corners, total 11.
These are used only for the final derivative field; sportsbook odds/tips are not used as predictive evidence.


##### Pick-by-pick settlement — model-selected slate


1. Djurgården team total Over 0.5 — WIN; Djurgården scored once.
2. Djurgården or Draw (1X) — LOSS; Elfsborg won 2-1.
3. Elfsborg team total Under 1.5 — LOSS; Elfsborg scored twice.
4. Total Corners Over 7.5 — WIN; 11 corners.
5. Full-game Under 3.5 goals — WIN; total three.


Model-selected slate: 3 W / 2 L.


##### Supplied-market settlement


1. First-half Over 0.5 — WIN; Elfsborg led 1-0 at halftime.
2. Full-game Over 2.5 — WIN; total three.
3. Full-game Under 2.5 — LOSS.
4. First-half Under 0.5 — LOSS.


Potential game winner: Djurgården — LOSS.


##### Rank-1 / top-two review


Rank #1 Djurgården TT Over 0.5 — WIN.
Rank #2 Djurgården or Draw — LOSS.
Hit@2 = YES.
Both top-two win = NO.
No Rank-1 failure trigger applies.


The highest-ranked over/under in the model-selected slate was Total Corners Over 7.5 at Rank #4, and it WON with 11 corners. The highest-ranked goal-total row, Under 3.5 at Rank #5, also WON. No TOP_OU_REVIEW failure trigger applies.


##### Expected vs actual game script


The forecast correctly retained an Elfsborg counter/resistance branch, but assigned it too little mass: Elfsborg's regulation-win estimate was only ~17.9%. Rasmus Wikström put Elfsborg ahead at 44', Djurgården equalised through Jacob Une Larsson at 66', and Simon Olsson restored the away lead at 76'.


The side/winner miss was driven by two concrete mechanisms. First, the 0-1 involved a major Jacob Rinne error. Second, after Djurgården made more attacking substitutions, the decisive 1-2 exposed defensive-transition assignments; postgame tactical reporting identified the space that allowed Alexander Jensen to create the winner.


##### What went right


- Rank #1 landed.
- The first-half Over 0.5 direction landed.
- The model's 3-goal overlap band was coherent: Over 2.5 and Under 3.5 both won.
- The corner model was directionally correct; 11 actual corners cleared 7.5.
- The forecast did preserve an Elfsborg counter/resistance scenario instead of treating home control as deterministic.


##### What went wrong


- Djurgården-or-draw was materially overestimated at ~82.1%.
- Elfsborg Under 1.5 was too strong at ~76.8%; Elfsborg scored twice.
- Goalkeeper-error and substitution/transition tails were present conceptually but underweighted in the side and away-team-total distribution.
- The potential winner call was wrong.
- Exact field-owner matchday XI/bench confirmation was unavailable before issue, and the decisive second-half mechanism involved substitution-linked defensive responsibilities.


##### Source/lineup audit


The projected starting XIs were broadly close to the eventual starting structures, but the issue-time card correctly did not label them field-owner confirmed. This limitation mattered more for the bench/substitution state than for the opening XI. The final should therefore not be used to claim that the pregame lineup retrieval was complete.


##### Blind spots and mitigation


Blind spot: insufficient weight on goalkeeper-error plus transition exposure after attacking substitutions.
Pre-game knowability: PARTLY. The exact Rinne error was irreducible event variance; the possibility that aggressive substitutions widen transition risk was knowable structurally.
Materiality: HIGH for 1X and Elfsborg Under 1.5; LOW for Rank #1, corners and Under 3.5.
Mitigation: execute the existing bench/substitution score-state branch explicitly inside winner/team-total scenario weights rather than leaving it only as prose.
Rule status: execution reinforcement only; no new permanent rule from one event.


##### Document mapping


- RULES_SOCCER.md: existing bench/substitution and score-state transition controls; execution reinforcement.
- DATA_SOURCE_REGISTER.md: Allsvenskan derivative final-field routes (WinDrawWin / BetStudy / TotalCorner) as research-only fallback observations, not predictive sources.
- No permanent algorithm change promoted.
- Dataset remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.


---
### P-479 — Cricket / European T20 Premier League Final — Edinburgh Castle Rockers vs Belfast Wolves
- Canonical / staging ID: P-479
- Competition: European T20 Premier League 2026 Final
- Venue: The Village, Malahide, Ireland
- Official venue-local start: Sep 20, 2026 at 14:15 IST (Europe/Dublin, UTC+1)
- Australia/Melbourne conversion: Sep 20, 2026 at 23:15 AEST (UTC+10); date rollover = NO
- Original issue state: PREGAME; final pre-issue refresh did not recover toss/confirmed XI.
- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-CRICKET
- Operating mode: SPORTS_ONLY / MARKET_BLIND
- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE
#### Original pre-game prediction
Frozen Belfast batting-first centre:
- Powerplay / first six overs: ~45 runs.
- Full first innings: ~160 runs.
- Working first-innings central corridor: ~145-175.
Best four model-selected targets:
1. Belfast Wolves first six overs UNDER 55.5 — ~73% UNVALIDATED_SUBJECTIVE.
2. Belfast Wolves first innings OVER 144.5 — ~66%.
3. Belfast Wolves first innings UNDER 174.5 — ~64%.
4. Edinburgh Castle Rockers to win — ~56%.
Supplied-line ranking:
1. Belfast first six UNDER 46.5 — ~56%.
2. Belfast first innings OVER 158.5 — ~53%.
3. Belfast first innings UNDER 158.5 — ~47%.
4. Belfast first six OVER 46.5 — ~44%.
Potential game winner: Edinburgh Castle Rockers — ~56%.
#### Original research reasoning / availability
- Belfast's four prior Malahide first-innings powerplays in the retrieved sample were 43/3, 49/1, 54/1 and 36/2, producing a 45.5-run mean and supporting the powerplay-Under direction.
- The full-innings sample was 107, 161, 187 and 190, showing that a subdued powerplay could still recover into a high final score; the Sep 17 meeting was 36/2 after six but 190/4 after 20.
- Edinburgh's attack carried multiple wicket paths through Boult, Curran, Jarvis, Santner and Watt.
- Charlie Tear was officially ruled out for Edinburgh. Mark Chapman had retired hurt in the prior meeting, but no reliable current source confirmed a continuing injury; Chapman and David Miller were treated as selection uncertainties rather than invented absences.
- Strip status: NOT FOUND AFTER SEARCH after the required pitch-report ladder. Venue/format historical scoring and the preceding Malahide match were used only as historical context.
- Match-window conditions were low-disruption with no material rain signal.
#### Material sources
1. ETPL exact final page — event identity / official competition route — https://www.etplofficial.com/matches/6a688c61b30844b0969df8c2
2. Tixr official event listing — exact local date/time and Malahide venue — https://www.tixr.com/groups/etplofficial/events/etpl-2026-final-edinburgh-castle-rockers-v-belfast-wolves-198572
3. CricketWorld Sep 17 exact scorecard — Belfast 190/4 and 36/2 powerplay against Edinburgh — https://www.cricketworld.com/cricket/edinburgh-castle-rockers-vs-belfast-wolves/match/scorecard/98352
4. CricketEurope tournament results — current ETPL result/scoring context — https://www.cricketeurope.com/FINALSCORE/RESULTS/TOURNAMENTS/EuropeanT20PremierLeague.shtml
5. ETPL qualifier page — Belfast's immediate prior qualifier result and workload — https://www.etplofficial.com/matches/6a688c61b30844b0969df8c1
6. CricketArchive / Cricket Ireland scorecard — prior exact Edinburgh-Belfast match context — https://www.cricketarchive.com/CricketIreland/Scorecards/1458/1458982.html
7. Pitchcare Malahide groundskeeping profile — historical venue tendency only, not current strip — https://www.pitchcare.com/blogs/news/the-craic-of-leather-on-willow-at-malahide
8. Weather forecast — match-window temperature/rain context.
9. Sports Research Drive — governing method and cricket rules.
Source firewall: betting picks, fantasy/DFS projections, market odds and prediction-site recommendations were excluded from predictive inputs.
#### Current state check
CURRENT STATUS: LIVE / NO SETTLEMENT.
A current CricTracker exact-event page reports Play Ongoing, Edinburgh elected to bowl, with Belfast 69/1 after 9.1 overs at the observed refresh. This is a moving live state and is recorded separately from the immutable pre-game prediction. No row is graded and no retrospective is performed while the match remains live.
Live-state source: https://www.crictracker.com/live-scores/ecr-vs-tba-final-t20-european-t20-premier-league-20-sep-2026/
Document mapping: no new lesson promoted while live. Any post-match learning waits for terminal-state verification.


#### Settlement and retrospective — P-479


Settlement status: SETTLED / RETROSPECTIVE COMPLETE.
Verified final: Belfast Wolves 150/5 (20 overs); Edinburgh Castle Rockers 151/3 (18.4 overs).
Result: Edinburgh Castle Rockers won by 7 wickets.
Belfast powerplay: 41/1 after six overs.


Three-source terminal-state gate: PASS.
- CricketWorld exact scorecard — Completed; Belfast 150/5, Edinburgh 151/3, Edinburgh won by 7 wickets; exact powerplay 41/1 — https://www.cricketworld.com/cricket/edinburgh-castle-rockers-vs-belfast-wolves/match/scorecard/98355
- BBC report syndicated by Yahoo Sports — explicit Edinburgh seven-wicket final and full innings totals — https://ca.sports.yahoo.com/news/edinburgh-castle-rockers-beat-belfast-174958677.html
- MyKhel exact scorecard — Result; Edinburgh 151/3 beat Belfast 150/5 by 7 wickets — https://www.mykhel.com/cricket/edinburgh-castle-rockers-vs-belfast-wolves-2026-final-scorecard-m273640/


##### Pick-by-pick settlement — model-selected slate


1. Belfast first six Under 55.5 — WIN; powerplay 41/1.
2. Belfast first innings Over 144.5 — WIN; 150/5.
3. Belfast first innings Under 174.5 — WIN; 150/5.
4. Edinburgh Castle Rockers to win — WIN.


Model-selected slate: 4 W / 0 L.


##### Supplied-line settlement


1. Belfast first six Under 46.5 — WIN; 41 runs.
2. Belfast first innings Over 158.5 — LOSS; 150.
3. Belfast first innings Under 158.5 — WIN.
4. Belfast first six Over 46.5 — LOSS.


Potential game winner: Edinburgh Castle Rockers — WIN.


##### Rank-1 / top-two / total review


Rank #1 Under 55.5 powerplay — WIN.
Rank #2 Over 144.5 innings — WIN.
Hit@2 = YES.
Both top-two win = YES.
The highest-ranked over/under selection was Rank #1 and won, so no enhanced failure trigger applies.


##### Expected vs actual game script


The pregame powerplay centre was ~45 and the realised powerplay was 41/1, strongly validating the early-phase direction. Belfast then recovered through Tim Tector's 84 and Devon Conway's 29 but lost middle/death acceleration when Glenn Maxwell made 3 and Lorcan Tucker 6, finishing at 150/5. That landed inside the forecast's 145-175 central corridor and simultaneously won Over 144.5 and Under 174.5.


Edinburgh chased efficiently to 151/3 in 18.4 overs, driven by Andries Gous' unbeaten 90. The winner call therefore landed through both bowling control and chase quality.


##### What went right


- All four model-selected targets won.
- Both top-two selections won.
- The powerplay model correctly separated early scoring from the full-innings ceiling.
- The 145-175 innings corridor was well centred around the actual 150.
- The explicit possibility that a subdued powerplay could still recover into a respectable final total was correct.
- Edinburgh winner was correct.


##### What went wrong / limitations


- The exact supplied 158.5 full-innings line was on the wrong side: Over 158.5 lost while Under won.
- The pregame analysis could not confirm the final XI or exact current strip before issue.
- Mark Chapman and David Miller did not appear in the final Belfast batting XI; the pregame card appropriately treated them as selection uncertainties rather than asserting availability.
- Postgame CricketWorld metadata describes the surface as spinning/average with swing favourable, but this is retrospective information and is not retroactively inserted as known pregame strip evidence.


##### Availability / participant audit


Belfast's realised batting group included Stirling, Tector, Conway, Maxwell, Tucker and Manenti. The uncertainty around Chapman/Miller was material to the ceiling branch, but because it was disclosed rather than fabricated, this is an evidence-quality limitation rather than a hindsight error.


##### Blind spots and mitigation


Blind spot: exact 158.5 threshold sensitivity around a central innings corridor.
Pre-game knowability: YES. A centre around 160 with meaningful uncertainty means 158.5 should remain a low-separation call.
Materiality: HIGH only for the supplied 158.5 pair; LOW for the broader model-selected corridor and winner.
Mitigation: retain corridor-first modelling and avoid overstating confidence when a supplied line lies within a few runs of the independent centre.
Rule status: existing threshold-separation and phase-to-innings controls worked; no new rule.


##### Document mapping


- RULES_CRICKET.md: powerplay-to-innings separation worked as intended.
- DATA_SOURCE_REGISTER.md: CricketWorld exact match notes successfully exposed the final powerplay field for settlement.
- No permanent rule change promoted.
- Dataset remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.


---
### P-480 — Soccer / Denmark Superligaen — Viborg FF vs FC Nordsjælland
- Canonical / staging ID: P-480
- Competition: Denmark Superligaen
- Venue: Energi Viborg Arena, Viborg, Denmark
- Official venue-local start: Sep 20, 2026 at 18:00 CEST (Europe/Copenhagen, UTC+2)
- Australia/Melbourne conversion: Sep 21, 2026 at 02:00 AEST; date rollover = YES
- Original issue state: PREGAME / NOT STARTED
- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-SOCCER
- Operating mode: SPORTS_ONLY / MARKET_BLIND
- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE
#### Original pre-game prediction
Frozen goal centre:
- Viborg ~1.26
- FC Nordsjælland ~1.42
- Projected total ~2.68
Best five:
1. First-half UNDER 1.5 goals — ~75% UNVALIDATED_SUBJECTIVE.
2. FC Nordsjælland team total OVER 0.5 — ~75%.
3. Full-game UNDER 3.5 goals — ~72%.
4. Total corners OVER 7.5 — ~70%.
5. FC Nordsjælland or Draw (X2) — ~66%.
Supplied lines:
- First-half Over 0.5 ~60.9%; Under 0.5 ~39.1%.
- Full-game Under 2.5 ~50.2%; Over 2.5 ~49.8%.
Potential game winner: FC Nordsjælland ~41.1%; Draw ~25.4%; Viborg ~33.5%.
#### Original research reasoning / availability
- Viborg entered with 11 goals scored / 7 conceded; FCN 13 / 6, while current xG data indicated FCN's attack was stronger than the raw 13 goals.
- Viborg's official Opta preview noted all five of FCN's most recent league goals had arrived after the 60th minute, supporting a distinction between a quieter first half and later FCN scoring.
- Corners were modelled separately: Viborg home match-corner environment around 12.25 and FCN away around 9.00 in the retrieved small samples, then shrunk for uncertainty.
- Official/current lineup sources converged on likely XI shapes but the accessible final feed still labelled them predicted rather than field-owner confirmed, so no player prop was promoted.
- Viborg: Riahi long-term knee injury officially confirmed; current feeds also listed Anyembe, Freriks and Njoh unavailable.
- FCN: current feed listed Salquist, Araphat Mohammed and Souleymane Alio unavailable; no suspensions were reported by Viborg's official preview.
- Weather near kickoff included showers and wind; treated as variance, not an automatic total direction.
#### Material sources
1. Viborg official schedule — exact event/time — https://vff.dk/ligaen/kampprogram
2. Viborg official Opta/Superstats preview — H2H, goal timing, passing/tackling and suspension context — https://www.vff.dk/nyhedsarkiv/8-sport/15936-info-og-stats-for-vff-fcn-4
3. FC Nordsjælland official material — recent team/result context — https://fcn.dk/nyheder/2026/september/highlights-fc-nordsjaelland-agf-1
4. MatchPulse — current-season xG/xGA — https://matchpulsestats.com/en/league/119/xg
5. SoccerStats — current home/away goal and corner splits — https://www.soccerstats.com/pmatch.asp?league=denmark&stats=50-1-10-2027
6. FotMob exact-event page — projected XI/current availability; not promoted above official sources — https://www.fotmob.com/en-GB/matches/viborg-vs-nordsjaelland/3crs0u?player=1382135
7. Viborg official Riahi medical update — https://vff.dk/nyhed/sport/15790-mohamed-riahi-alvorligt-knaeskadet
8. FCN official squad/availability material — https://fcn.dk/nyheder/2026/september/truppen-til-aftenens-kamp-i-herning
9. Weather forecast and Sports Research Drive methodology.
#### Current state check
CURRENT STATUS: LIVE / NO SETTLEMENT.
The structured soccer event feed (event 71925034) showed Viborg vs FC Nordsjælland live at the state refresh. No row is graded and no retrospective is performed while live.
Document mapping: none while live; retain for terminal-state settlement.


#### Settlement and retrospective — P-480


Settlement status: SETTLED / RETROSPECTIVE COMPLETE.
Verified final: Viborg FF 4, FC Nordsjælland 1.
Halftime: Viborg 3, FC Nordsjælland 1.
Final corners: Viborg 4, FC Nordsjælland 5; total 9.


Three-source terminal-state gate: PASS.
- Structured exact-event soccer feed, event 71925034 — COMPLETE at 4-1.
- Eurosport exact match page — completed 4-1 with final stats including 4-5 corners — https://www.eurosport.nl/voetbal/3f-superliga/2026-2027/live-viborg-ff-fc-nordsjaelland_mtc21873592/live.shtml
- Sky Sports exact fixture/result page — full-time Viborg 4-1 FC Nordsjælland — https://www.skysports.com/football/viborg-ff-vs-fc-nordsjaelland/6482622979768878232


Derivative cross-check:
- Abseits exact match page: HT 3-1, corners 4-5.
- Campo/Ritzau report: four first-half goals and 3-1 halftime, final 4-1.
- Eurosport: corners 4-5.


##### Pick-by-pick settlement — model-selected slate


1. First-half Under 1.5 goals — LOSS; halftime total was four.
2. FC Nordsjælland team total Over 0.5 — WIN; FCN scored once.
3. Full-game Under 3.5 goals — LOSS; final total five.
4. Total Corners Over 7.5 — WIN; total nine.
5. FC Nordsjælland or Draw (X2) — LOSS; Viborg won 4-1.


Model-selected slate: 2 W / 3 L.


##### Supplied-line settlement


- First-half Over 0.5 — WIN.
- First-half Under 0.5 — LOSS.
- Full-game Under 2.5 — LOSS.
- Full-game Over 2.5 — WIN.


Potential game winner: FC Nordsjælland — LOSS.


##### Mandatory enhanced Rank-1 / TOP_OU failure review


Rank #1 First-half Under 1.5 — LOSS.
This row was also the highest-ranked over/under selection, so one enhanced review covers both the Rank-1 and TOP_OU triggers.
Rank #2 FCN team total Over 0.5 — WIN.
Hit@2 = YES.
Both top-two win = NO.


Why Rank #1 was placed first:
- the first-half centre was ~0.95 goals;
- FCN's previous five league goals had all arrived after the 60th minute;
- FCN's two immediately preceding league matches had reached halftime 0-0;
- the forecast expected a patient opening and separated late FCN scoring from early scoring.


Why that ranking failed:
- Viborg scored at 16', 33' and 41'; FCN scored at 26'. The match had four first-half goals before the model's preferred slow-opening branch could establish itself.
- The pregame reasoning overweighted FCN's recent late-goal timing and underweighted Viborg's own home first-half attacking capacity and the possibility of early conversion from both sides.
- The 75% estimate was too confident for a phase total built from small, overlapping timing samples and without field-owner confirmed lineups/bench state.
- The supplied 1H Over 0.5 at ~60.9% actually won and was the structurally safer early-goal target because it needed only one event, whereas Under 1.5 required the entire first half to avoid a second goal.


Should another row have ranked above it?
YES. On the frozen information, FC Nordsjælland team total Over 0.5 was also estimated around 75% and was less sensitive to exact first-half timing. Given the unresolved XI/bench state and the small timing sample, FCN TT Over 0.5 should have been Rank #1 or at minimum tied ahead of the first-half Under after an uncertainty penalty.


Failure classification:
- Small/overlapping sample timing inference: YES.
- Poor uncertainty handling: YES.
- Missing confirmed lineup/bench information: CONTRIBUTORY.
- Existing rule not fully executed: YES — the phase-total path geometry and evidence-grade cap should have prevented a 75% phase Under from being treated as clearly strongest without stronger first-half suppression evidence.
- Genuine variance: PARTLY, but not sufficient to excuse the ranking.


##### Full-match total review


Under 3.5 also lost, with five total goals. The same underlying miss carried forward: the distribution underweighted the high-conversion/open branch. Viborg's 3-1 halftime score meant the Under 3.5 was already dead by the break.


The preferred supplied full-game side had been Under 2.5 at only ~50.2%, essentially no separation. It lost, while Over 2.5 won. This was not a strong pregame opinion and should remain classified as near-coin-flip rather than a major directional failure.


##### Actual game script


Viborg led through Mads Søndergaard at 16'. Alexander Lind equalised for FCN at 26'. Dorian Hanza restored Viborg's lead at 33', and Charly Horneman made it 3-1 at 41'. Adam Kleis-Kristoffersen completed the 4-1 at 81'.


The decisive feature was not late FCN scoring. It was Viborg's first-half attacking efficiency and FCN's inability to suppress repeated home chances. FCN still scored once, preserving Rank #2.


##### What went right


- FCN team total Over 0.5 won.
- Total corners Over 7.5 won with nine.
- Supplied first-half Over 0.5 won.
- Supplied full-game Over 2.5 won.
- The corner model remained independent of the incorrect goal-total direction and still landed.


##### What went wrong


- Rank #1 failed badly: four first-half goals versus an Under 1.5 call.
- Under 3.5 failed by 1.5 goals.
- FCN X2 and the potential winner call failed.
- The model over-weighted FCN's recent late-goal pattern and under-weighted Viborg's home attacking ceiling.
- The 2.68 full-game centre was materially too low for the realised high-conversion game.


##### Lineup / availability audit


The pregame card explicitly said the accessible lineup feeds were projected rather than field-owner confirmed. The realised scorers included Dorian Hanza and Alexander Lind, both consistent with the expected attacking structures. No postgame evidence indicates a late withdrawal was the central cause. The main failure was distribution/ranking, not an undisclosed injury.


##### Blind spots and mitigation


1. First-half phase Under built from small timing samples.
   - Pre-game knowability: YES.
   - Materiality: VERY HIGH.
   - Mitigation: shrink recent goal-timing streaks more aggressively toward competition/home-away first-half base rates and require stronger bilateral suppression evidence before assigning ~75% to U1.5.


2. Viborg home attacking ceiling.
   - Pre-game knowability: YES.
   - Materiality: HIGH.
   - Mitigation: give the home side's multi-window chance/goal production an explicit branch independent of opponent recent scoring timing.


3. No confirmed XI/bench.
   - Pre-game knowability: known missingness.
   - Materiality: MODERATE.
   - Mitigation: preserve a wider phase-total distribution when final participant state is unresolved.


Rule status: these are execution corrections to existing phase-total, recency and uncertainty controls. Do not promote a new fixed coefficient from one match.


##### Source audit / document mapping


- Campo/Ritzau: strong same-day game-script source.
- Eurosport and Abseits: useful exact-event final/halftime/corner fields.
- Structured soccer feed: reliable terminal-state confirmation.
- RULES_SOCCER.md: execution reinforcement for phase-total geometry, recency shrinkage and XI uncertainty.
- DATA_SOURCE_REGISTER.md: Danish Superliga exact-event derivative field routes as research-only settlement candidates.
- Dataset remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.


---
### P-481 — Soccer / Spain La Liga — Villarreal vs Levante
- Canonical / staging ID: P-481
- Competition: Spain La Liga, Matchday 7
- Venue: Estadio de la Cerámica, Vila-real, Spain
- Official venue-local start: Sep 20, 2026 at 18:30 CEST (Europe/Madrid, UTC+2)
- Australia/Melbourne conversion: Sep 21, 2026 at 02:30 AEST; date rollover = YES
- Original issue state: PREGAME / SCHEDULED
- Method / controls: MDS-2026.09.19-v4.3 / CR-2026.09.19-4 / SFA-SOCCER
- Operating mode: SPORTS_ONLY / MARKET_BLIND
- Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE
#### Original pre-game prediction
Frozen goal centre:
- Villarreal ~1.85
- Levante ~1.13
- Projected total ~2.98
- Villarreal win ~54.0%; Draw ~22.6%; Levante win ~23.4%.
Best five:
1. Villarreal team total OVER 0.5 — ~83% UNVALIDATED_SUBJECTIVE.
2. Full-game UNDER 4.5 — ~81%.
3. Villarreal or Draw (1X) — ~77%.
4. First-half OVER 0.5 — ~72%.
5. Villarreal OVER 4.5 corners — ~68%.
Supplied lines:
- First-half Over 0.5 ~72%; Under 0.5 ~28%.
- Full-game Over 2.5 ~56%; Under 2.5 ~44%.
Potential game winner: Villarreal ~54%.
#### Original research reasoning / availability
- Villarreal's underlying attack was materially stronger than its early results: current sources placed them around 12.3-12.5 xG from six league matches, with 91 shots and 39 on target.
- Levante had conceded nine in five league matches and carried an away scoring weakness in the small current sample.
- The Villarreal attack included Pépé, Moleiro, Gerard Moreno and Mikautadze in the freshest accessible lineup feed.
- A source conflict was resolved in favour of the fresher same-day team news: Juan Foyth was back available, while Santi Comesaña was out with a right-ankle problem; an older page still listing Comesaña starting was treated as stale.
- Levante's official call-up ruled out Álex Primo, Karl Etta Eyong and Hugo Sotelo.
- Villarreal had shorter rest after the Sep 17 Málaga match; Levante's scheduled midweek Athletic fixture had been postponed.
- Weather was dry and low-disruption around kickoff.
#### Material sources
1. LaLiga official exact fixture page — event/stadium/kickoff and current competition records — https://www.laliga.com/es-GB/partido/temporada-2026-2027-laliga-ea-sports-villarreal-cf-levante-ud-7
2. Villarreal official calendar — independent kickoff confirmation — https://villarrealcf.es/en/calendario-primer-equipo/
3. Levante official match call-up — confirmed Álex Primo, Karl Etta Eyong and Hugo Sotelo absences — https://www.levanteud.com/en/news/convocatoria-or-villarreal-cf-levante-ud-2627
4. AS exact-match lineup page — freshest lineup state — https://as.com/resultados/futbol/primera/2026_2027/directo/regular_a_7_6a4496c62a77870/alineaciones/amp/
5. EFE / Mundo Deportivo — same-day Foyth return and Comesaña unavailability corroboration — https://www.mundodeportivo.com/futbol/laliga/20260920/1004229059/villarreal-mide-mejoria-pujante-levante.html
6. StatMuse — xG/xGA/shots/SOT/possession diagnostics — https://www.statmuse.com/fc/ask/villarreal-levante-xg-xga-xgot?l=laliga
7. MatchPulse — current-season xG cross-check — https://matchpulsestats.com/es/league/140/xg
8. SoccerStats / PrematchStats — home/away, first-half and corner splits.
9. Weather forecast and Sports Research Drive methodology.
Source firewall: sportsbook odds, line movement, betting previews/tips and fantasy/DFS projections were excluded.
#### Current state check
CURRENT STATUS: LIVE / NO SETTLEMENT.
The structured soccer event feed (event 72478604) showed Villarreal vs Levante live at the state refresh. No row is graded and no retrospective is performed while live.
Document mapping: none while live; retain for terminal-state settlement.


#### Settlement and retrospective — P-481


Settlement status: SETTLED / RETROSPECTIVE COMPLETE.
Verified final: Villarreal 3, Levante 1.
Halftime: 1-1.
Final corners: Villarreal 7, Levante 1.


Three-source terminal-state gate: PASS.
- Structured exact-event soccer feed, event 72478604 — COMPLETE at 3-1.
- Cadena SER / EFE exact postgame report — explicit 3-1 final and goal sequence — https://cadenaser.com/nacional/2026/09/20/villarreal-levante-resumen-resultado-y-goles-del-partido-de-la-jornada-7-de-laliga-ea-sports-cadena-ser/
- Europa Press exact match report — explicit 3-1 final, goals and final statistics — https://www.europapress.es/deportes/estadisticas-deportivas/noticia-villareal-levante-resumen-goles-resultado-partido-hoy-20260920202832.html


Corner endpoint cross-check:
- Europa Press: corners 7-1.
- Soccerzz exact match page: corners 7-1.
- Sofascore postgame analysis explicitly states the 7-1 corner count.
The corner settlement is therefore verified independently of market pages.


##### Pick-by-pick settlement — model-selected slate


1. Villarreal team total Over 0.5 — WIN; Villarreal scored three.
2. Full-game Under 4.5 goals — WIN; total four.
3. Villarreal or Draw (1X) — WIN.
4. First-half Over 0.5 goals — WIN; halftime 1-1.
5. Villarreal Over 4.5 corners — WIN; Villarreal had seven.


Model-selected slate: 5 W / 0 L.


##### Supplied-line settlement


- First-half Over 0.5 — WIN.
- First-half Under 0.5 — LOSS.
- Full-game Over 2.5 — WIN.
- Full-game Under 2.5 — LOSS.


Potential game winner: Villarreal — WIN.


##### Rank-1 / top-two / total review


Rank #1 Villarreal TT Over 0.5 — WIN.
Rank #2 Under 4.5 — WIN.
Hit@2 = YES.
Both top-two win = YES.
The highest-ranked over/under selection, Under 4.5, WON. No enhanced failure trigger applies.


##### Expected vs actual game script


The independent centre was Villarreal 1.85, Levante 1.13, total 2.98. The actual 3-1 sat in the forecast's open Villarreal-control family. Ayoze Pérez scored at 41', Iván Romero equalised at 42', Alberto Moleiro restored the lead at 54', and substitute Georges Mikautadze completed the scoring at 86'.


The territorial mechanism was strongly supported postgame: Soccerzz records approximately 2.90 xG to 0.94, 21-6 shots, 7-1 shots on target and 7-1 corners. Villarreal's stronger attacking process therefore translated into both goals and corners.


##### What went right


- All five model-selected picks won.
- Both top-two selections won.
- Villarreal winner call won.
- The supplied 1H Over 0.5 and FT Over 2.5 directions both won.
- Villarreal TT Over 0.5 was robust to lineup changes and landed comfortably.
- Under 4.5 correctly protected against a 3-1 open game.
- Villarreal Over 4.5 corners was supported by actual territorial pressure and landed at seven.


##### Important pre-game mistake despite the wins — lineup audit


The pregame card described the freshest accessible lineup feed as showing Pépé, Moleiro, Gerard Moreno and Mikautadze in the attacking structure. The verified final lineup did NOT match that description:
- Starters included Tajon Buchanan, Alberto Moleiro, Ilias Akhomach and Ayoze Pérez.
- Nicolas Pépé, Gerard Moreno and Georges Mikautadze started on the bench.
- Mikautadze later came on and scored the 86' goal.


This is a genuine pre-game source-latency/lineup-classification defect. The fact that every team-level pick won does not erase it. The selections were robust because they were team-level, but a player prop based on the stated projected attack could have been badly wrong.


##### What went wrong / limitations


- The lineup source was treated as fresher/more definitive than it actually was.
- The final total centre of ~2.98 was somewhat low versus the realised four goals, although the distribution retained sufficient upper-tail mass for Under 4.5 and Over 2.5 to coexist.
- Levante's scoring branch was not negligible; Iván Romero's 42' equaliser confirmed that the away side could punish Villarreal despite the territorial mismatch.


##### Source-quality audit


- Europa Press / EFE-style match reporting: strong for final, scorers and team stats.
- Soccerzz: useful detailed exact-event lineup/xG/corner record.
- Sofascore postgame article: useful independent derivative corroboration.
- The pregame AS lineup page was not reliable enough to be treated as a confirmed team sheet at the issue timestamp. Future cards must preserve the label PROJECTED until a field-owner or exact-event provider explicitly marks the XI confirmed.


##### Blind spots and mitigation


Blind spot: near-kickoff lineup freshness/confirmation.
Pre-game knowability: YES — the missing official confirmation was itself observable.
Materiality: LOW for the team-level selections that were issued; potentially HIGH for any player prop.
Mitigation: do not upgrade a lineup from projected to confirmed solely because a page is same-day or recently refreshed. Require an explicit confirmation marker or field-owner team sheet.
Rule status: this is enforcement of an existing lineup-verification rule, not a new rule.


##### Document mapping


- RULES_SOCCER.md / RULES_GENERAL.md: existing projected-vs-confirmed XI distinction was not executed strictly enough; record as an execution failure.
- DATA_SOURCE_REGISTER.md: AS same-day lineup route should remain secondary unless explicit confirmation state is exposed.
- No new permanent rule required.
- Dataset remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.


---


## 3. Temporary-ID / Canonical-ID Conflict Logs


None. P-474 through P-481 were collision-checked against the active mini-log sequence. P-479, P-480 and P-481 were issued in this chat after the prior Drive snapshot and have now been incorporated without overwriting any existing canonical ID.


## 4. Settlement Lists


Settled in this mini log:
- P-474 — Athletics @ Cleveland Guardians — SETTLED / RETROSPECTIVE COMPLETE.
- P-475 — Chicago Sky @ Atlanta Dream — SETTLED / RETROSPECTIVE COMPLETE.
- P-476 — Minnesota Twins @ Los Angeles Angels — SETTLED / RETROSPECTIVE COMPLETE.
- P-477 — Sydney Kings vs Cairns Taipans — SETTLED / RETROSPECTIVE COMPLETE.
- P-478 — Djurgårdens IF vs IF Elfsborg — SETTLED / RETROSPECTIVE COMPLETE; final 1-2, HT 0-1, corners 4-7.
- P-479 — Edinburgh Castle Rockers vs Belfast Wolves — SETTLED / RETROSPECTIVE COMPLETE; Edinburgh won by 7 wickets, Belfast 150/5, PP 41/1.
- P-480 — Viborg FF vs FC Nordsjælland — SETTLED / RETROSPECTIVE COMPLETE; final 4-1, HT 3-1, corners 4-5.
- P-481 — Villarreal vs Levante — SETTLED / RETROSPECTIVE COMPLETE; final 3-1, HT 1-1, corners 7-1.


Awaiting settlement:
- None.


## 5. Running Integrity Notes


- The governing methodology remains MDS-2026.09.19-v4.3 / CR-2026.09.19-4.
- The dataset remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.
- Every P-474 through P-481 entry is now in the Fully Settled section. The Incomplete / Unsettled section is empty.
- P-478's previously unresolved corner derivative is now settled: three exact-event statistical routes independently report Djurgården 4 and Elfsborg 7 corners, so Total Corners Over 7.5 is a WIN. Final model-selected result: 3 W / 2 L.
- P-479 settled 4 W / 0 L on the model-selected slate. Belfast's powerplay finished 41/1 and first innings 150/5; Edinburgh won by seven wickets. The exact supplied 158.5 innings Over lost, while Under won.
- P-480 settled 2 W / 3 L on the model-selected slate. Rank #1 First-half Under 1.5 and Rank #3 Under 3.5 both lost in a 4-1 game that was already 3-1 at halftime. The mandatory Rank-1 and TOP_OU enhanced review was completed. The primary correction is stronger recency shrinkage/uncertainty for phase Unders and more weight on Viborg's home first-half attacking ceiling.
- P-481 settled 5 W / 0 L on the model-selected slate. Villarreal won 3-1, the game had four total goals, and Villarreal won the corner count 7-1. The retrospective nevertheless records a genuine pregame lineup-source defect: several players presented as starting attackers were actually substitutes, so team-level success does not validate that lineup retrieval.
- Across P-478 through P-481, the model-selected slates were 14 W / 5 L descriptively. Rank #1 was 3 W / 1 L; Hit@2 was 4/4. These are learning-only diagnostics and are not performance-eligible or prospective validation.
- The final-state/source gate passed for all four newly settled events. Derivative endpoints were separately verified rather than inferred from scores.
- Market odds, line movement, betting tips and fantasy/DFS material were not admitted as predictive evidence. A small number of betting-branded/statistical pages were used only as independent final-stat cross-checks where stronger field-owner derivative feeds were not exposed; that limitation is explicitly recorded.
- No governing methodology file, historical combined prediction log or canonical archive was edited in this pass. Only the dedicated mini running log was updated.
- No new permanent sport-specific or cross-sport rule was promoted. P-480 and P-481 expose execution failures of existing phase-total uncertainty and lineup-confirmation controls; P-479 validates the existing cricket phase-to-innings separation process; P-478 reinforces bench/transition and derivative-source controls.
- Next intended prediction ID: P-482, subject to fresh reconciliation before issue.

---

# Part 4 closure — 2026-09-21

- Canonical range: **P-424–P-481**.
- Newly reconciled in this closure: **P-452–P-481**.
- P-452–P-473: **22/22 settled and retrospectively reviewed**.
- P-474–P-481: **8/8 settled and retrospectively reviewed**.
- No P-452–P-481 event remains live or awaiting settlement.
- Historical derivative/result handles outside this rollover remain tracked in `GAME_LOG_STATUS_CURRENT.md`; they are not silently regraded here.
- Performance state remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.
- Part 4 is now read/settle-only.
- **Next canonical ID: P-482**, controlled by `PREDICTION_LOG_COMBINED_5.md`.

