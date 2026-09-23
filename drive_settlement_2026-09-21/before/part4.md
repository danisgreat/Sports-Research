# Combined prediction log 4

> **Controlling status (carried from Part 3):** all combined-log material is **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** under the current user direction. Settlement preserves outcome evidence; it does not authorise a performance claim. Issued records are never rewritten.

Status: **ACTIVE CANONICAL LOG — ALL NEW FORECASTS APPEND HERE**
Opened: **2026-09-15**, as the fourth combined log per user directive.
Component order: opened empty at **`P-424`**; new forecasts append below in strict ascending canonical-ID order.
Current method: **MDS-2026.09.17-v4.1 — SPORTS_ONLY / MARKET_BLIND; `UNVALIDATED_SUBJECTIVE` probability + Brier scoring mandatory on every ranked row (`METHOD.md` §5).** Read the version from `METHOD.md`'s own header each session — never from this line.

| Part | File | ID range | Status |
|---|---|---|---|
| 1 | `PREDICTION_LOG_COMBINED.md` | `P-001`–`P-271` | CLOSED 2026-09-04 — read/settle only |
| 2 | `PREDICTION_LOG_COMBINED_2.md` | `P-272`–`P-332` | CLOSED 2026-09-07 — read/settle only; holds the lettered "Appendix — unsettled and incomplete logs" |
| 3 | `PREDICTION_LOG_COMBINED_3.md` | `P-333`–`P-423` (`P-372` reserved/unused) | CLOSED 2026-09-15 — read/settle only |
| **4** | **`PREDICTION_LOG_COMBINED_4.md` (this file)** | **`P-424` onward** | **ACTIVE** |

## Current controlling snapshot

This is the only queue and next-ID authority for new forecasts. The snapshots in Parts 1–3 are frozen at their closures.

| Field | Current value |
|---|---|
| As of | **2026-09-17(c), Australia/Sydney** — audit implementation; no new forecast or final retrieved. P-451 remains the highest canonical ID. |
| Next canonical ID | **`P-452`** |
| Live events | **None.** Every issued event through `P-451` is final — `P-451`'s LNBP Jornada 20 final (Dorados 97–86) was recovered on 2026-09-17(b) from the rendered club page. `P-430` is final on the scoreboard with one derivative row unresolved on a source rule. |
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

