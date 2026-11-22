# Prediction Log (Combined) — Part 11

**ACTIVE · OPENING_SNAPSHOT · canonical-md-1 · RESEARCH_ONLY · MARKET_BLIND**

Opened 2026-11-16T19:19:56+11:00, Australia/Melbourne (AEDT, UTC+11), by prompt 5 (P-2026.11.16-v25.0 · COMBINED_LOG_ROLLOVER) under the owner order of 16 November 2026. Authority LOCAL_WORKING_TREE `C:\Users\danie\Projects\Sports-Research`, branch main, base HEAD `c1d0403ed9c754758e1e1d96bc256197ce67470d`. Method **MDS-2026.11.16-v25.0**; control **CR-2026.11.16-R2**; scoring **SCV-2026.11.16-v16**; selection **SEL-2026.10.22-v4**; mini-log-10 / mini-settlement-10; chat cards from this release end with an `ONECHAT_V1` block (ONE-CHAT-v1).

## Identity at opening

Highest canonical ID **P-685**; next **P-686**, unchanged. Reserved **P-518–P-522** must not be reused. Zero IDs assigned or reserved by this opening. This part opens with **zero canonical originals, forecasts, settlements or addendum blocks**. Prompts 1–3 use local keys; prompt 4 alone assigns canonical IDs. No repository mini is active (CR-2026.11.12-R1); each research chat keeps its own mini under its own MINI_KEY.

## Previous-part continuity

| Part | Immutable predecessor |
|---|---|
| 1 | [Combined log 1](PREDICTION_LOG_COMBINED.md) |
| 2 | [Combined log 2](PREDICTION_LOG_COMBINED_2.md) |
| 3 | [Combined log 3](PREDICTION_LOG_COMBINED_3.md) |
| 4 | [Combined log 4](PREDICTION_LOG_COMBINED_4.md) |
| 5 | [Combined log 5](PREDICTION_LOG_COMBINED_5.md) |
| 6 | [Combined log 6](PREDICTION_LOG_COMBINED_6.md) |
| 7 | [Combined log 7](PREDICTION_LOG_COMBINED_7.md) |
| 8 | [Combined log 8](PREDICTION_LOG_COMBINED_8.md) |
| 9 | [Combined log 9](PREDICTION_LOG_COMBINED_9.md) |
| 10 | [Combined log 10](PREDICTION_LOG_COMBINED_10.md) |

Part 10 closed with 1,530,426 pre-closure raw bytes and 26 canonical originals P-660–P-685 (imported on 15 November 2026: one ID per game, parallel chat records as addenda). Its complete prefix is preserved. Trigger: the default 1.5 MB size threshold was exceeded. [Closure and byte/readback receipt](../research/verification/combined_rollover_2026-11-16-1/README.md). No card is copied here. Later revisions for closed-part originals append here with `Original: <closed-part path>, <P-ID>` and prior-revision pointers.

## Both queues at opening

- **PENDING_EVENT:** none.
- **Terminal UNRESOLVED_EVIDENCE / DEFINITION / CUSTODY:** 50 UNRESOLVED rows of P-660–P-685 (P-664 final, P-661 and P-662 six-over scores, P-678 five-over score, P-683 corners) and the three P-647 corner rows, with sources located by SRC-RECOVERY-20261116R1 and a settlement revision to follow in this part; P-657–P-659 MISSING_ORIGINAL; unverified final wall-clocks and first-play times; single-lineage results; earlier queues at their existing dispositions. [Queue continuity](../research/verification/combined_rollover_2026-11-16-1/QUEUE_CONTINUITY.md); [latest unresolved list](../research/verification/mini_import_P-660_P-685_2026-11-15-1/UNRESOLVED_POST_IMPORT.csv); [located sources](../research/verification/source_recovery_2026-11-15-1/REPORT.md).

## Independent source, execution and learning custody

[RESEARCH_SOURCE_REGISTER](../RESEARCH_SOURCE_REGISTER.md), [settlement sources](../research/source_routes/SETTLEMENT_SOURCES.csv), [latest source register](../research/verification/mini_import_P-660_P-685_2026-11-15-1/SOURCE_DISCOVERY_REGISTER.csv), [audit of the owner drop](../research/verification/mini_import_P-660_P-685_2026-11-15-1/AUDIT_REPORT.md), [on-request audit of P-001 to P-685](../research/verification/retrospective_2026-11-16-1/RETROSPECTIVE_REPORT.md). Learning store, shadow ledger, releases, one-chat intakes and the deep loss register stay at their own locations; see the generated block in [CURRENT_STATE](../CURRENT_STATE.md).

<!-- END ACTIVE COMBINED LOG HEADER -->

<!-- BEGIN SETTLEMENT REVISION BATCH 2026-11-16 revision-2 -->
## Settlement revision batch · 16 November 2026 · revision-2

Prompts 3→4 under the owner order of 16 November 2026. Fifty-three rows left UNRESOLVED at import are settled from located permitted sources: 26 WIN, 27 LOSS. No canonical ID is consumed; originals in closed parts are unchanged. Package: [report](../research/verification/settlement_import_2026-11-16-1/CANONICAL_IMPORT_REPORT.md).
<!-- END SETTLEMENT REVISION BATCH HEADER -->

<!-- BEGIN RESEARCH ADDENDUM P-647 2026-11-16-settlement-revision-2 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_9.md`, P-647; prior revision revision-1. Source: `research/verification/settlement_import_2026-11-16-1/SETTLEMENT_REVISION_2.md` (event block P-647); 1722 B, SHA-256 `33d11e59ad9a847f3d477833d06436c5d2982d0860e311589a9b66d44e5416b4`; exact bytes follow.

<!-- BEGIN SETTLEMENT REVISION P-647 revision-2 -->
### P-647 · Urawa Red Diamonds v Cerezo Osaka · 2026-11-11 · J.League YBC Levain Cup, first leg · revision-2

Original: `prediction logs/PREDICTION_LOG_COMBINED_9.md`, P-647; prior revision revision-1 (rows UNRESOLVED). Effective 2026-11-16T19:22:52+11:00. Rows revised: 3 (1 WIN, 2 LOSS); evidence class A. Every original card, rank, probability and earlier grade is unchanged.

**Verified outcome.** Combined corners 12: Urawa 8, Cerezo 4. Both official club-record tables carry the row of 11 November 2026, YLC, 19:30 JST, Saitama Stadium, 2–0, attendance 10,004, with CK 8 (Urawa's table) and CK 4 (Cerezo's table). The return leg of 15 November is a different row and was not used.

**Source.** Official J.League club pages for [Urawa](https://www.jleague.jp/en/club/urawa/) and [Cerezo Osaka](https://www.jleague.jp/en/club/cosaka/), routes `JLC_URAWA_CK` and `JLC_CEREZO_CK`. Captures `urawa_corners_web_extract.txt` (SHA-256 `764084680edd7b33a3e831a49e9bd3772cf9c77a8a2727cea91c2d510860459c`, 9,039 B, kept outside the repository) and `cerezo_corners_verified_web_extract.txt` (SHA-256 `c97e6502cb41ee0b3faa2a147600509823d723c264b50e98e832d1699a1ad4b5`, 8,542 B, kept outside the repository); hashes re-verified and both dated rows re-read in this run. Official field owner, one lineage: evidence class A.

**Settlement arithmetic.** Over 10.5 corners: WIN (12 > 10.5). Under 10.5 corners: LOSS. 3 rows on two records: 1 WIN, 2 LOSS.

**Deep loss review.** None required. The two losing Under rows are an exploratory row and a legacy v4.12 scenario row; neither is a top side, a top total or a first lean.
<!-- END SETTLEMENT REVISION P-647 revision-2 -->

<!-- END RESEARCH ADDENDUM P-647 2026-11-16-settlement-revision-2 -->

<!-- BEGIN RESEARCH ADDENDUM P-661 2026-11-16-settlement-revision-2 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-661; prior revision revision-1. Source: `research/verification/settlement_import_2026-11-16-1/SETTLEMENT_REVISION_2.md` (event block P-661); 2043 B, SHA-256 `cb65b651f584e28d0261c60e9e3a4278835c1706b1cc6f990cc64b0d254613bd`; exact bytes follow.

<!-- BEGIN SETTLEMENT REVISION P-661 revision-2 -->
### P-661 · Hobart Hurricanes Women v Brisbane Heat Women · 2026-11-14 · WBBL|12 · revision-2

Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-661; prior revision revision-1 (rows UNRESOLVED). Effective 2026-11-16T19:22:52+11:00. Rows revised: 10 (5 WIN, 5 LOSS); evidence class C. Every original card, rank, probability and earlier grade is unchanged.

**Verified outcome (threshold bound).** Hobart Hurricanes Women after six completed overs: **23 or 24**. The provider's over-by-over table gives 3+4+3+6+2+5 = 23 for overs 1 to 6 and prints "Powerplay 23/3". Its replayed innings totals 85 against the scorecard's 86, and the page states that one run (a bye or leg bye) was not placed by ball. Wherever that run fell, the six-over score is 23 or 24.

**Source.** [Cricket Field Guide](https://cricketfieldguide.com/match/hobart-hurricanes-women-v-brisbane-heat-women-01m7er2qx1er4sc03wmscpg0h8), route `WBBL_CFG_HOBART_6` (read interactively by the ChatGPT reader, ALLOWED; SCRIPT is blocked and was not used). Capture `hobart_overs_web_extract.txt` (SHA-256 `69d9029d5a9b1ebe566ed77f6e6ab36a2d6ca1263a12bc477adc99a856c731b6`, 14,960 B, kept outside the repository); hash re-verified and the figures re-read from the capture in this run; per-over runs in [research/verification/source_recovery_2026-11-15-1/OBSERVED_OVER_RUNS.csv](../source_recovery_2026-11-15-1/OBSERVED_OVER_RUNS.csv). One provisional feed: evidence class C.

**Settlement arithmetic.** Under 41.5: WIN for both ends of the bound (24 < 41.5, a margin of at least 17.5 runs). Over 41.5: LOSS. 10 rows on five chat cards: 5 WIN, 5 LOSS.

**Deep loss review.** None required. Every card leaned Under 41.5 and won.

**Limit.** The exact six-over score is not asserted. The open Cricsheet WBBL archive reached only 2 November on 15 November (checked through the repository fetcher); when it reaches this match the exact score is checked against this bound.
<!-- END SETTLEMENT REVISION P-661 revision-2 -->

<!-- END RESEARCH ADDENDUM P-661 2026-11-16-settlement-revision-2 -->

<!-- BEGIN RESEARCH ADDENDUM P-662 2026-11-16-settlement-revision-2 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-662; prior revision revision-1. Source: `research/verification/settlement_import_2026-11-16-1/SETTLEMENT_REVISION_2.md` (event block P-662); 6296 B, SHA-256 `757f48c5262f44ad1f4aa25945b25b137532a48f952cae902cbc44ef5d08613a`; exact bytes follow.

<!-- BEGIN SETTLEMENT REVISION P-662 revision-2 -->
### P-662 · Perth Scorchers Women v Adelaide Strikers Women · 2026-11-14 · WBBL|12 Match 22 · revision-2

Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-662; prior revision revision-1 (rows UNRESOLVED). Effective 2026-11-16T19:22:52+11:00. Rows revised: 12 (6 WIN, 6 LOSS); evidence class C. Every original card, rank, probability and earlier grade is unchanged.

**Verified outcome (threshold bound).** Adelaide Strikers Women after six completed overs: **39 or 40**. The provider's over-by-over table gives 6+6+3+9+8+7 = 39 for overs 1 to 6 and prints "Powerplay 39/1". Its replayed innings totals 201 against the scorecard's 202, and the page states that one run was not placed by ball. Wherever that run fell, the six-over score is 39 or 40.

**Source.** [Cricket Field Guide](https://cricketfieldguide.com/match/adelaide-strikers-women-v-perth-scorchers-women-01m7er2qx1erbbjrzatatsg1s7), route `WBBL_CFG_ADELAIDE_6` (read interactively by the ChatGPT reader, ALLOWED; SCRIPT is blocked and was not used). Capture `adelaide_card_web_extract.txt` (SHA-256 `cb7469b97cdacd6ef59325963a89e81bfbdef17eb6836ccde3e98829447473d3`, 15,778 B, kept outside the repository); hash re-verified and the figures re-read from the capture in this run. One provisional feed: evidence class C. The same page gives Perth 151 where the retained audit has 150; that conflict concerns the other innings and is not used here.

**Settlement arithmetic.** Under 41.5: WIN for both ends of the bound (40 < 41.5). Over 41.5: LOSS. 12 rows on six chat cards: 6 WIN, 6 LOSS. Three chats leaned Under (won) and three leaned Over (lost).

**Limit.** The margin is 1.5 runs on a single provisional feed. The exact score is not asserted. The open Cricsheet WBBL archive reached only 2 November on 15 November; when it reaches this match the score is checked, and a further dated revision follows if it is 42 or more.

#### Deep loss review · P-662 / LOCAL-CHAT20261114DDA525E495-G0003 · RANK_1 · Adelaide 6 overs Over 41.5

**1. Exact frozen claim.** "Over 41.5 runs after 6 completed overs", PERIOD family, Adelaide first innings; stated p 0.648317 from the chat's own simulation (R6 mean 47.63, SD 15.24); listed first and labelled "Preferred LEAN, <0.65 gate". No reference, no baseline (REFERENCE_NONE, BASELINE not estimated), no ledger rows. NOT_ISSUED chat-local research; last recorded 19:07:36 AEDT against a 19:10 AEDT scheduled start.
**2. Verified outcome.** 39 or 40 after six completed overs (bound above). Distance from the line: -1.5 to -2.5 runs, about -0.1 to -0.16 of the card's SD. Distance from the card's centre: about -8 runs, -0.53 SD.
**3. Distribution check.** The card gave 0.352 to this side of the line; the outcome sits near the 30th percentile of its own distribution. Row Brier (0.648 - 0)^2 = 0.420 against 0.250 for a constant 0.5: the card's number made this row worse than a coin by 0.170. No reference or baseline row exists to compare.
**4. Error decomposition.** Centre 47.6 against 39–40: 8 runs high. The width (SD 15.2) was wide enough to contain the outcome comfortably. No adjustments were made, so none can be signed.
**5. Research audit, fact by fact.** "Four current-season matches, six-over average 48.5, 4 of 4 at 42 or more": taken from the card; not re-verified here (UNVERIFIED), and the card itself calls the four innings overlapping and not independent. "Three of the 20-over innings were chases": stated by the card as a weakness of its own baseline. "Toss: Adelaide batting first confirmed": consistent with the result page (TRUE). Prior seasons and head-to-head were declared not recovered. No market content; no outcome exposure recorded.
**6. What decided the row.** Adelaide scored 6, 6, 3, 9, 8, 7 in the first six overs for the loss of one wicket, then 163 off the last fourteen (202/4). The start was slower than the four-game sample; the innings as a whole was far above every estimate.
**7. Knowable at the cutoff?** That four innings cannot fix a six-over centre to within the 6 runs separating it from the line: KNOWABLE, and the card said so. The slow start itself: NOT_KNOWABLE.
**8. Process audit.** The endpoint was read correctly (six completed overs, not the four-over mandatory powerplay). The number was computed and its sensitivity printed: a 5-run lower centre gives 51.85%. The defect is in what was done with it: a number resting on n = 4, whose own sensitivity makes it a coin flip, was listed as the first lean. The card's label "LEAN ONLY, below the gate" is honest, but a row that is listed first is counted as Rank 1.
**9. Verdict.** MIXED. Outcome: VARIANCE (a 35% event by the card's own number, half an SD from its centre). Process: DEFICIENT in one respect — small-sample strength treated as a direction. Not an error of fact.
**10. Cutoff-only counterfactual.** With the centre shrunk halfway to the line for n = 4 (about 44.5), the same SD gives roughly 0.57 to 0.58. Diagnostic only; no row is replaced.
**11. Failure class and recurrence.** SMALL_SAMPLE_STRENGTH_OVERREACH. The register holds two earlier reviews of this class (P-660, P-685, alias PLUS_HANDICAP_WITHOUT_OPPONENT_CHECK), so by class this is the third and it is routed to prompt 8.
**12. Correction.** NO_CHANGE during the cohort (FREEZE-v1). The v25.0 brief already tells the chat not to dress a number it cannot support as a pick, and the intake flags numbers within 5 points of 0.5. Candidate for the post-cohort release: a `sample_n` column beside `centre` in the PICKS table, so small-sample centres can be tested (owner prompt 8; acceptance: flagged rows scored against unflagged; rollback: drop the column).
**13. Matched wins.** None on this card: its other line (20-over total) was left unselected at 51.3%. Across the six chats on this game, three leaned Under 41.5 and won and three leaned Over and lost, on the same public figures: the line was a coin flip, and the three wins are not evidence of skill either.
**14. Honesty checklist.** No hindsight fact used as if known; the variance claim is supported by sections 2 and 3; frozen rows, ranks and grades unchanged; the card's own four-game figures are marked UNVERIFIED: PASS.
<!-- END SETTLEMENT REVISION P-662 revision-2 -->

<!-- END RESEARCH ADDENDUM P-662 2026-11-16-settlement-revision-2 -->

<!-- BEGIN RESEARCH ADDENDUM P-664 2026-11-16-settlement-revision-2 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-664; prior revision revision-1. Source: `research/verification/settlement_import_2026-11-16-1/SETTLEMENT_REVISION_2.md` (event block P-664); 1829 B, SHA-256 `ca5c0bf862c3159a5ee6ff441572f05d62f7e38e097cb831d546d1688c7e732c`; exact bytes follow.

<!-- BEGIN SETTLEMENT REVISION P-664 revision-2 -->
### P-664 · Tappara U20 v HPK U20 · 2026-11-14 · Finland U20 SM-sarja · revision-2

Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-664; prior revision revision-1 (rows UNRESOLVED). Effective 2026-11-16T19:22:52+11:00. Rows revised: 24 (12 WIN, 12 LOSS); evidence class C. Every original card, rank, probability and earlier grade is unchanged.

**Verified outcome.** Tappara U20 2–4 HPK U20, Saturday 14 November 2026, 13:00 +02:00, U20 SM-sarja. Periods 1–1, 0–1, 1–2 (home 1+0+1 = 2, away 1+1+2 = 4; sum check passes). The game ended in regulation; total goals 6.

**Source.** [Tulokset](https://tulokset.live/jaakiekko/ottelu/tappara-hpk-2026-11-14-2710291), route `FIN_U20_TULOKSET_FINAL` (SCRIPT reader ALLOWED, checked 2026-11-15T13:08:25+00:00). The page description reads "Tappara – HPK 2–4 la 14.11.2026, U20 SM-sarja (1–1, 0–1, 1–2)". Capture `36fcd7dd8db0541563806d031a76dfdf438cb7db20ed70290feac6401f031a6e.html` (SHA-256 `4ec5e0a14527c1e467aea9f808248f62cc4b42b9184998c083011a05d2919b08`, 550,941 B, kept outside the repository); hash re-verified in this run and the description re-read from the capture. One lineage; the provider's upstream is unknown: evidence class C.

**Settlement arithmetic.** HPK ML: WIN (away side won 4–2 in regulation). Tappara ML: LOSS. Over 5.5 goals: WIN (6 > 5.5). Under 5.5 goals: LOSS. 24 rows on six chat cards: 12 WIN, 12 LOSS.

**Deep loss review.** None required. Every card's ranked rows (HPK ML and Over 5.5) won; the losing rows are the unpreferred complements.

**Limit.** A second permitted lineage was not opened (Leijonat and Elite Prospects were not readable). If one later contradicts this score, a further dated revision follows.
<!-- END SETTLEMENT REVISION P-664 revision-2 -->

<!-- END RESEARCH ADDENDUM P-664 2026-11-16-settlement-revision-2 -->

<!-- BEGIN RESEARCH ADDENDUM P-678 2026-11-16-settlement-revision-2 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-678; prior revision revision-1. Source: `research/verification/settlement_import_2026-11-16-1/SETTLEMENT_REVISION_2.md` (event block P-678); 1578 B, SHA-256 `2cdb6c73fb459e9dac2dd066d9770346eca01719c12c3039246f0c071de271af`; exact bytes follow.

<!-- BEGIN SETTLEMENT REVISION P-678 revision-2 -->
### P-678 · Australia v England · 2026-11-15 · second ODI, Adelaide · revision-2

Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-678; prior revision revision-1 (rows UNRESOLVED). Effective 2026-11-16T19:22:52+11:00. Rows revised: 2 (1 WIN, 1 LOSS); evidence class C. Every original card, rank, probability and earlier grade is unchanged.

**Verified outcome.** England 19–1 after five completed overs (first innings). The live report reads "5th over: England 19-1 (Banton 9, Root 0)", preceded by Duckett's wicket at 19–1 and followed by "6th over: England 25-1".

**Source.** The Guardian over-by-over report, route `ODI_GUARDIAN_ENGLAND_5` (read interactively by the ChatGPT reader, ALLOWED at that path). Capture `specific_final_fields_web_extract.txt` (SHA-256 `32fb6e09a1207e1d91d6b6a3300ad89ed9eddb49fc6c1de3681f2b5106795b4e`, 23,100 B, kept outside the repository); hash re-verified and both entries re-read from the capture in this run. The repository agent's own reader is BLOCKED at this path (`ml source-audit`, 16 November) and did not open the page. One media lineage: evidence class C.

**Settlement arithmetic.** Under 26.5: WIN (19 < 26.5). Over 26.5: LOSS. 2 rows on one card.

**Deep loss review.** None required: the losing row (Over 26.5) was the card's second lean, not its top side, top total or first lean.

**Limit.** The open Cricsheet ODI archive had not reached 15 November when checked; it is the second lineage when it does.
<!-- END SETTLEMENT REVISION P-678 revision-2 -->

<!-- END RESEARCH ADDENDUM P-678 2026-11-16-settlement-revision-2 -->

<!-- BEGIN RESEARCH ADDENDUM P-683 2026-11-16-settlement-revision-2 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-683; prior revision revision-1. Source: `research/verification/settlement_import_2026-11-16-1/SETTLEMENT_REVISION_2.md` (event block P-683); 1524 B, SHA-256 `c0aff45f2deff4afd1055545e77ebe650a4a41e520636cf89918af7844ce2cef`; exact bytes follow.

<!-- BEGIN SETTLEMENT REVISION P-683 revision-2 -->
### P-683 · Kashiwa Reysol v Kawasaki Frontale · 2026-11-15 · J.League YBC Levain Cup · revision-2

Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-683; prior revision revision-1 (rows UNRESOLVED). Effective 2026-11-16T19:22:52+11:00. Rows revised: 2 (1 WIN, 1 LOSS); evidence class A. Every original card, rank, probability and earlier grade is unchanged.

**Verified outcome.** Combined corners 7: Kashiwa 4, Kawasaki 3. Both official club-record tables carry the row of 15 November 2026, YLC, 17:03 JST, SANKYO F Kashiwa, 5–4, attendance 9,189, with CK 4 (Kashiwa's table) and CK 3 (Kawasaki's table).

**Source.** Official J.League club pages for [Kashiwa](https://www.jleague.jp/en/club/kashiwa/) and [Kawasaki](https://www.jleague.jp/en/club/kawasakif/), routes `JLC_KASHIWA_CK` and `JLC_KAWASAKI_CK`. Captures `specific_final_fields_web_extract.txt` (SHA-256 `32fb6e09a1207e1d91d6b6a3300ad89ed9eddb49fc6c1de3681f2b5106795b4e`, 23,100 B, kept outside the repository) and `club_kawasaki_web_extract.txt` (SHA-256 `e076dea7937d258b4ff9020d256002bffa70669f1bd97edbd09d2af8af1386af`, 8,948 B, kept outside the repository); hashes re-verified and both dated rows re-read in this run. Official field owner, one lineage: evidence class A.

**Settlement arithmetic.** Under 10.5: WIN (7 < 10.5). Over 10.5: LOSS. 2 rows on one card.

**Deep loss review.** None required: the card's lean (Under 10.5) won.
<!-- END SETTLEMENT REVISION P-683 revision-2 -->

<!-- END RESEARCH ADDENDUM P-683 2026-11-16-settlement-revision-2 -->

<!-- END SETTLEMENT REVISION BATCH 2026-11-16 revision-2 -->

<!-- BEGIN IMPORT BATCH 2026-11-22 P-686..P-696 20261118DA6D9F6251746B979F5895FA -->
## Import batch · 22 November 2026 · P-686 to P-696 (20261118DA6D9F6251746B979F5895FA)

Owner-invoked prompts 3→4 on GitHub mini `20261118DA6D9F6251746B979F5895FA` (10 sealed cards on `origin/forecast-seals`, 1 unsealed card `G0001` on `origin/card-drops`, plus 2 non-card requests `G0004` and `G0007` consuming zero IDs). **One canonical ID per game (P-686 to P-696)** in scheduled-start UTC order, ties broken by card key order. Original card bytes follow verbatim inside `canonical-md-1` wrappers; verified settlements and deep loss reviews follow as dated addenda. Import metadata is not a forecast issue time. Full package: [CANONICAL_IMPORT_REPORT.md](../research/verification/mini_import_P-686_P-696_2026-11-22-1/CANONICAL_IMPORT_REPORT.md).
<!-- END IMPORT BATCH HEADER -->

<!-- BEGIN CANONICAL RESEARCH P-686 -->
## P-686 — Basketball/NBA Regular Season (game 0022600254) — Portland Trail Blazers @ Minnesota Timberwolves · 2026-11-17 CT

Canonical retention by prompt-4 import `2026-11-22T06:40:00+00:00`. Scheduled start `2026-11-18T12:00:00+11:00`. Original `20261118DA6D9F6251746B979F5895FA-G0001` (17197 B, SHA-256 `c7e736f010ef6793f7c450f8662e4bede49b9162c136e1b36473632bfed84e05`, source `origin/card-drops`, seal `UNSEALED` at `UNSEALED`). Original card follows verbatim; no forecast reissued; Track P scored separately via `ml one-chat score`.

# Pre-game forecast card · LOCAL-20261118DA6D9F6251746B979F5895FA-G0001 · NBA:0022600254

**Custody:** Chat-owned mini `20261118DA6D9F6251746B979F5895FA`; immutable first issue, ONECHAT_V1. **Repository governing main:** `cb97bbc2a9f882e7f8a093648b6137315951da8b`; MDS-v29.1 / CR-R2 / P-v29.1 / SCV-v20. **Request registration:** card-drops `0d1ef2cd423e560b6bca87c347ffd4457dd4c569`; GitHub `seal-drops` run 44211358497 SUCCESS and `forecast-seals` request index independently read. Official game: https://www.nba.com/game/por-vs-min-0022600254. No historical prediction or market prices used.

## Original owner request (exact UTF-8 contents)
```text
Upcoming Basketball Game: POR Trailblazers @ MIN Timberwolves, NBA Regular Season,
Estimated Game Time Start: 18 November 2026, 11:00 AM AEDT (can be delayed so continue the process as normal)

Trailblazers +4.5
Timberwolves -4.5
Combined Total Points: Over/Under 225.5 points
```

## A1. Identity, timestamps and cutoff
- Game: POR Trail Blazers at MIN Timberwolves; NBA Regular Season; Target Center; `NBA:0022600254`; 17 November 2026 8:00 PM ET = 18 November 2026 12:00 PM AEDT (owner estimated 11:00 AM AEDT).
- request_at: `2026-11-18T11:51:14+11:00` is the first reliably observed chat-processing time, NOT independently verifiable original delivery instant.
- research_start_at: `2026-11-18T11:53:49+11:00`, after registration succeeded, as recorded in tool time.
- not_started_source: https://www.nba.com/timberwolves/game/0022600254-blazers-vs-timberwolves-minneapolis-mn-11-17-2026/event-details; pregame fixture page showed date/7:00 PM CST and no current-game result, observed conservatively by `2026-11-18T11:55:13+11:00` (within research).
- research_end_at: `2026-11-18T11:59:28+11:00`. Outcome exposure: NONE for the target 17 Nov game; prior 16 Nov final used as historical input. Actual first-play capture has NOT been independently secured.
- Original request official registry, contract-definition CSV and result source must remain paired with this exact card. Sealing is NOT established by this local file; must await separate workflow and independently published first seal.

## A2. Exact supplied contracts and grades
- L1 away `Trailblazers +4.5`, home `Timberwolves -4.5`: full game including all NBA overtime periods; home minus away final points > 4.5 yields HOME; less yields AWAY; no push at half-point. `HANDICAP`, settlement at final official score.
- L2 combined total `Over/Under 225.5 points`: full game including overtime; over is final combined points >225.5; under is <225.5; no push at half-point. `TOTAL`, settlement at final official score.
- No winner contract added, because none was supplied. No spread or threshold was changed. The posted owner lines are contract metadata, not pricing inputs.

## A3. Evidence and raw pregame histories
**Data basis:** https://www.askscores.com/nba/team/minnesota-timberwolves/2026-27 and https://www.askscores.com/nba/team/portland-trail-blazers/2026-27 (ESPN-derived individual dated results); source table's separate aggregate PPG/defensive fields conflict materially with its displayed dated results, so all rolling scoring means are recomputed from the dated results below. For efficiency use the dated 16 Nov advanced ratings at https://gridironandwine.com/nba/advanced/teams/, excluding every price/tip/prediction field from that page. Official availability as at 11/17 6:15 PM ET: https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_06_15PM.pdf, screenshot-inspected page 2. All field observations are no later than `2026-11-18T11:56:26+11:00`.

Minnesota prior 14 games (date, opponent, MIN scored, opponent scored):
2026-10-21 MIA 131-106; 2026-10-23 ORL 115-93; 2026-10-25 TOR 117-94; 2026-10-26 CLE 125-127; 2026-10-28 GSW 114-119; 2026-10-30 LAC 127-101; 2026-10-31 SAS 111-121; 2026-11-02 MIL 112-100; 2026-11-04 HOU 117-107; 2026-11-06 NOP 115-109; 2026-11-08 UTA 115-100; 2026-11-12 DAL 133-94; 2026-11-14 CHI 106-117; 2026-11-16 POR 106-98.

Portland prior 13 games (date, opponent, POR scored, opponent scored):
2026-10-21 PHX 124-83; 2026-10-23 SAC 128-120; 2026-10-27 LAL 136-129; 2026-10-29 MEM 103-124; 2026-10-31 UTA 112-90; 2026-11-02 DEN 118-110; 2026-11-04 PHX 132-119; 2026-11-06 LAL 118-124; 2026-11-07 SAS 103-125; 2026-11-10 OKC 123-103; 2026-11-11 OKC 118-108; 2026-11-13 SAC 120-107; 2026-11-16 MIN 98-106.

| Window | MIN PF | MIN PA | POR PF | POR PA |
|---|---:|---:|---:|---:|
| last 5 (n=5) | 115.00 | 103.60 | 112.40 | 109.80 |
| last 10 (n=10) | 115.60 | 106.60 | 114.50 | 111.60 |
| season available (MIN n=14; POR n=13, NOT full L20) | 117.43 | 106.14 | 117.92 | 111.38 |

2026-11-16 previous H2H: MIN 106, POR 98. Both clubs played that date at Target Center, with no full rest day or venue travel before the 17 Nov rematch. Previous H2H beyond this is unquantified; do not use unsourced longer series as numeric input.

Official 6:15 PM ET report: MIN Anthony Edwards, Jonathan Kuminga, Donte DiVincenzo, Jaylen Clark and Zyon Pullin OUT; Joan Beringer AVAILABLE. POR Ja Morant, Shaedon Sharpe, Vit Krejci and Chris Youngblood OUT; Deni Avdija QUESTIONABLE; Branden Carlson AVAILABLE. No confirmed starting fives or verified bench substitutions at research cutoff. Missing opponent-strength adjustments and measured availability effects remain explicit; sources do not justify treating questionable players as active or making numeric injury adjustments. Coaching: MIN Chris Finch; POR Micah Nori (club rosters above). No travel/weather adjustment applied.

## A4. Distribution and arithmetic (transparent analyst approximation, NOT calibrated)
Observed advanced team ratings snapshot on 16 Nov: MIN ORtg 115.2, DRtg 104.1, pace 101.2; POR ORtg 117.2, DRtg 110.7, pace 100.7 (https://gridironandwine.com/nba/advanced/teams/). No opponent-by-opponent adjusted efficiencies were verified; these are observed season efficiency inputs only.

- Projected pace `(101.2 + 100.7)/2 = 100.95` possessions. Efficiency neutral centres: MIN `100.95 × (115.2+110.7)/200 = 114.023`; POR `100.95 × (117.2+104.1)/200 = 111.701`.
- Last-five points matchup centres: MIN `(115.0+109.8)/2=112.4`; POR `(112.4+103.6)/2=108.0`.
- Registered analyst recipe: **70% season efficiency cross-matchup + 30% last-five cross-matchup** (a declared transparent heuristic, not a previously calibrated or learned weight). No added numerical home/rest/injury adjustment because reliable magnitude unavailable. MIN `0.7×114.023025+0.3×112.4=113.536`; POR `0.7×111.701175+0.3×108.0=110.591`.
- Forecast expected total `224.127`, expected MIN-POR margin `2.945`. Widths: pooled raw 2026-27 completed-game sample SD (13 POR and 14 MIN games, `n−1` sample variance weighted by n−1) gives total SD `15.933` points and signed-margin SD `16.149`. Independence/normal tails and width transport to this matchup are assumptions; no Monte Carlo was run. Explicit overtime is included as a full-game result convention; an extra separately fitted overtime mixture was NOT computed, so point probabilities are approximate rather than a rigorously overtime-mixture-calibrated model.
- `P(POR +4.5)=Φ((4.5−2.945)/16.149)=0.538347`; complement `P(MIN -4.5)=0.461653`.
- `P(Over225.5)=1−Φ((225.5−224.127)/15.933)=0.465662`; complement `P(Under225.5)=0.534338`.
- Deni Avdija status, missing starters and absence impacts are unmeasured; all probabilities are marked `UNMEASURED`. Sensitivity cannot be quantified honestly without sourced replacement effects; a material status change can reverse both marginal directions. These numbers must not be presented as calibrated probabilities or qualified Rank-1 picks.

## Decision block — exact supplied rows
| Rank among supplied sides | Contract | Analyst p | Principal failure route |
|---|---|---:|---|
| 1 (below gate) | Trail Blazers +4.5 | 53.8% | Minnesota's interior defence/Portland missing scorers; Avdija ruled out |
| 2 (below gate) | Under 225.5 | 53.4% | Hot three-point shooting and high-possession foul/OT finish |
| — | Timberwolves -4.5 | 46.2% | Portland protects possessions and remains within 4 |
| — | Over 225.5 | 46.6% | Two short-rest offences and Minnesota defence suppress scoring |

**Official Rank 1 and Rank 2:** `NO_FORECAST_GATE_NOT_MET` (highest supported numeric side 53.8%, below 62% Rank-1 and 58% Rank-2 thresholds). These are exact contract-side *diagnostic probabilities*, not qualified selections. Main failure: unconfirmed availability and short L5 samples. No odds, market baseline, betting tips, outside forecasts or model outputs used.

## A5–A9. Audit, limitations, custody and settlement source
- A5: All four sides of all two supplied half-point lines are present; no push, no void expected barring official cancellation; family sums are one to numerical precision. No separate winner line priced because not requested.
- A6: No numerical availability, travel or home adjustment; all unmeasured impact retained, not silently set to zero. Site aggregate/dated-result inconsistency flagged. 70/30 blending is a transparent uncalibrated heuristic; alternate weights or injury scenarios not numerically scored.
- A7: Opponent-by-opponent strength adjustment unavailable; fitted ML/RL NOT_RUN; simulation NOT_RUN; independence of statistical source lineage not established; last 20 games unavailable this season for both clubs.
- A8: Official NBA game status/source https://www.nba.com/timberwolves/game/0022600254-blazers-vs-timberwolves-minneapolis-mn-11-17-2026/event-details; official injury report https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_06_15PM.pdf; source histories https://www.askscores.com/nba/team/minnesota-timberwolves/2026-27, https://www.askscores.com/nba/team/portland-trail-blazers/2026-27; advanced snapshot https://gridironandwine.com/nba/advanced/teams/. Confirmed starters not found before freeze. No access to unverified live post-start data. Result/settlement official NBA match centre https://www.nba.com/game/por-vs-min-0022600254. Any actual first-play evidence requires later independent time-stamped capture, not scheduled start alone.
- A9: Original REQUEST.txt verified with SHA-256 `65a4fb3452ef863a4fe76dbaed7d2375fce1433deef7fc997c73e3e712700c66`. Registered EVENT.csv and CONTRACTS.csv confirmed independently under `forecast-seals`. The original forecast is this complete file; subsequent chat display/reformat does not supersede its first independently sealed Git blob. `seal_status` PENDING_GITHUB until verified. Research-time and document-create-time clocks come from actual available tool time; user's exact message-received instant is not independently exposed. No claims of prospective admission or predictive skill.

<!-- BEGIN ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0001 -->
format: ONECHAT_V1
card_key: 20261118DA6D9F6251746B979F5895FA-G0001
sport: Basketball
competition: NBA Regular Season
home: Minnesota Timberwolves
away: Portland Trail Blazers
scheduled_start: 2026-11-18T12:00:00+11:00
request_at: 2026-11-18T11:51:14+11:00
research_start_at: 2026-11-18T11:53:49+11:00
research_end_at: 2026-11-18T11:59:28+11:00
not_started_source: https://www.nba.com/timberwolves/game/0022600254-blazers-vs-timberwolves-minneapolis-mn-11-17-2026/event-details
not_started_observed_at: 2026-11-18T11:55:13+11:00
outcome_exposure: NONE

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,HANDICAP,AWAY,4.5,0.538347,,-2.945,UNMEASURED,https://www.nba.com/game/por-vs-min-0022600254
L1,HANDICAP,HOME,-4.5,0.461653,,2.945,UNMEASURED,https://www.nba.com/game/por-vs-min-0022600254
L2,TOTAL,OVER,225.5,0.465662,,224.127,UNMEASURED,https://www.nba.com/game/por-vs-min-0022600254
L2,TOTAL,UNDER,225.5,0.534338,,224.127,UNMEASURED,https://www.nba.com/game/por-vs-min-0022600254

FACTS
side,field,value,source,observed_at
HOME,season_games,14,https://www.askscores.com/nba/team/minnesota-timberwolves/2026-27,2026-11-18T11:56:26+11:00
HOME,season_score_for_pg,117.43,https://www.askscores.com/nba/team/minnesota-timberwolves/2026-27,2026-11-18T11:56:26+11:00
HOME,season_score_against_pg,106.14,https://www.askscores.com/nba/team/minnesota-timberwolves/2026-27,2026-11-18T11:56:26+11:00
HOME,last5_score_for_pg,115.0,https://www.askscores.com/nba/team/minnesota-timberwolves/2026-27,2026-11-18T11:56:26+11:00
HOME,last5_score_against_pg,103.6,https://www.askscores.com/nba/team/minnesota-timberwolves/2026-27,2026-11-18T11:56:26+11:00
HOME,last10_score_for_pg,115.6,https://www.askscores.com/nba/team/minnesota-timberwolves/2026-27,2026-11-18T11:56:26+11:00
HOME,last10_score_against_pg,106.6,https://www.askscores.com/nba/team/minnesota-timberwolves/2026-27,2026-11-18T11:56:26+11:00
HOME,rest_days,0,https://www.askscores.com/nba/team/minnesota-timberwolves/2026-27,2026-11-18T11:56:26+11:00
HOME,back_to_back,YES,https://www.askscores.com/nba/team/minnesota-timberwolves/2026-27,2026-11-18T11:56:26+11:00
HOME,key_absences,Edwards OUT; Kuminga OUT; DiVincenzo OUT; Clark OUT; Pullin OUT,https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_06_15PM.pdf,2026-11-18T11:56:26+11:00
HOME,lineup_confirmed,MISSING,No verified confirmed official starting five during recorded research,2026-11-18T11:56:26+11:00
HOME,venue,"Target Center, Minneapolis",https://www.nba.com/timberwolves/game/0022600254-blazers-vs-timberwolves-minneapolis-mn-11-17-2026/event-details,2026-11-18T11:56:26+11:00
HOME,travel_km,0,Same venue as 2026-11-16 fixture; no intervening venue transfer / https://www.askscores.com/nba/team/minnesota-timberwolves/2026-27,2026-11-18T11:56:26+11:00
HOME,opponent_strength,MISSING,Opponent-by-opponent adjusted ratings not verified in research window,2026-11-18T11:56:26+11:00
HOME,opponent_strength_method,MISSING,Opponent-by-opponent schedule strength adjustment NOT_COMPUTED,2026-11-18T11:56:26+11:00
HOME,availability_effect,MISSING,No admitted measured on/off or replacement-minute effect for current injury set,2026-11-18T11:56:26+11:00
HOME,adjustment_basis,NO_PLAYER_ADJUSTMENT,Pre-start historical team-performance mix; lineup uncertainty retained without numeric adjustment,2026-11-18T11:56:26+11:00
HOME,last20_score_for_pg,MISSING,Only 14 completed 2026-27 regular-season games before tip-off; insufficient full 20-game window,2026-11-18T11:56:26+11:00
HOME,last20_score_against_pg,MISSING,Only 14 completed 2026-27 regular-season games before tip-off; insufficient full 20-game window,2026-11-18T11:56:26+11:00
AWAY,season_games,13,https://www.askscores.com/nba/team/portland-trail-blazers/2026-27,2026-11-18T11:56:26+11:00
AWAY,season_score_for_pg,117.92,https://www.askscores.com/nba/team/portland-trail-blazers/2026-27,2026-11-18T11:56:26+11:00
AWAY,season_score_against_pg,111.38,https://www.askscores.com/nba/team/portland-trail-blazers/2026-27,2026-11-18T11:56:26+11:00
AWAY,last5_score_for_pg,112.4,https://www.askscores.com/nba/team/portland-trail-blazers/2026-27,2026-11-18T11:56:26+11:00
AWAY,last5_score_against_pg,109.8,https://www.askscores.com/nba/team/portland-trail-blazers/2026-27,2026-11-18T11:56:26+11:00
AWAY,last10_score_for_pg,114.5,https://www.askscores.com/nba/team/portland-trail-blazers/2026-27,2026-11-18T11:56:26+11:00
AWAY,last10_score_against_pg,111.6,https://www.askscores.com/nba/team/portland-trail-blazers/2026-27,2026-11-18T11:56:26+11:00
AWAY,rest_days,0,https://www.askscores.com/nba/team/portland-trail-blazers/2026-27,2026-11-18T11:56:26+11:00
AWAY,back_to_back,YES,https://www.askscores.com/nba/team/portland-trail-blazers/2026-27,2026-11-18T11:56:26+11:00
AWAY,key_absences,Morant OUT; Sharpe OUT; Krejci OUT; Youngblood OUT; Avdija QUESTIONABLE,https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_06_15PM.pdf,2026-11-18T11:56:26+11:00
AWAY,lineup_confirmed,MISSING,No verified confirmed official starting five during recorded research,2026-11-18T11:56:26+11:00
AWAY,venue,"Target Center, Minneapolis",https://www.nba.com/timberwolves/game/0022600254-blazers-vs-timberwolves-minneapolis-mn-11-17-2026/event-details,2026-11-18T11:56:26+11:00
AWAY,travel_km,0,Same venue as 2026-11-16 fixture; no intervening venue transfer / https://www.askscores.com/nba/team/portland-trail-blazers/2026-27,2026-11-18T11:56:26+11:00
AWAY,opponent_strength,MISSING,Opponent-by-opponent adjusted ratings not verified in research window,2026-11-18T11:56:26+11:00
AWAY,opponent_strength_method,MISSING,Opponent-by-opponent schedule strength adjustment NOT_COMPUTED,2026-11-18T11:56:26+11:00
AWAY,availability_effect,MISSING,No admitted measured on/off or replacement-minute effect for current injury set,2026-11-18T11:56:26+11:00
AWAY,adjustment_basis,NO_PLAYER_ADJUSTMENT,Pre-start historical team-performance mix; lineup uncertainty retained without numeric adjustment,2026-11-18T11:56:26+11:00
AWAY,last20_score_for_pg,MISSING,Only 13 completed 2026-27 regular-season games before tip-off; insufficient full 20-game window,2026-11-18T11:56:26+11:00
AWAY,last20_score_against_pg,MISSING,Only 13 completed 2026-27 regular-season games before tip-off; insufficient full 20-game window,2026-11-18T11:56:26+11:00
<!-- END ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0001 -->
<!-- END CANONICAL RESEARCH P-686 -->

<!-- BEGIN RESEARCH ADDENDUM P-686 2026-11-22-settlement-revision-1 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_11.md`, P-686. Source: `research/verification/mini_import_P-686_P-696_2026-11-22-1/SETTLEMENT.md` (P-686); exact settlement block follows.

<!-- BEGIN SETTLEMENT P-686 LOCAL-20261118DA6D9F6251746B979F5895FA-G0001 revision-1 -->
### P-686 · Basketball/NBA Regular Season (game 0022600254) — Portland Trail Blazers @ Minnesota Timberwolves · 2026-11-17 CT · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0001` · `NBA:0022600254` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `UNSEALED` (server push `NONE`; assessment `UNSEALED_DROP_REFUSED`; actual first play `NOT_VERIFIED`).
- **Verified final (B):** **Minnesota Timberwolves 106-105 Portland Trail Blazers** · Linescore: `POR 17-31-31-26=105; MIN 29-20-30-27=106 (sum check: 17+31+31+26=105, 29+20+30+27=106)`.
- **Permitted source & capture:** `https://www.foxsports.com/nba/portland-trail-blazers-vs-minnesota-timberwolves-nov-17-2026-game-boxscore-106739` · capture `2026-11-22/G0001_fox_box.html` (SHA-256 `f3af78436756f7609a31e9afe90763ca3fc4588754d51f590b74bf8d896112b8`). Corroboration: https://basketball.realgm.com/nba/scores/2026-11-17 (web search corroboration; script blocked, not fetched by script).
- **Card-mean Brier / d:** `0.2150` / `+0.0350`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | AWAY | 4.5 | 0.538347 | -2.945 | UNMEASURED | **WIN** | 0.2131 |
| L1 | NOT_RANKED | HANDICAP | HOME | -4.5 | 0.461653 | 2.945 | UNMEASURED | **LOSS** | 0.2131 |
| L2 | NOT_RANKED | TOTAL | OVER | 225.5 | 0.465662 | 224.127 | UNMEASURED | **LOSS** | 0.2168 |
| L2 | R2 | TOTAL | UNDER | 225.5 | 0.534338 | 224.127 | UNMEASURED | **WIN** | 0.2168 |

**R1–R12 retrospective:** Jaden McDaniels hit the go-ahead basket with 2.6s left; Ayo Dosunmu scored 30, Damian Lillard 25, Jrue Holiday 23. Both card leans won (POR +4.5 by 3.5 pts; Under 225.5 by 14.5 pts). Card failed DROP-SEAL due to 4 FACTS rows missing source URLs. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

**Deep loss review:** None required (Rank 1, top side, and top total all won).
<!-- END SETTLEMENT P-686 LOCAL-20261118DA6D9F6251746B979F5895FA-G0001 revision-1 -->
<!-- END RESEARCH ADDENDUM P-686 2026-11-22-settlement-revision-1 -->

<!-- BEGIN CANONICAL RESEARCH P-687 -->
## P-687 — Basketball/NCAAB 2026-27 — Michigan State Spartans @ Tennessee Volunteers · 2026-11-17 ET

Canonical retention by prompt-4 import `2026-11-22T06:40:00+00:00`. Scheduled start `2026-11-18T13:00:00+11:00`. Original `20261118DA6D9F6251746B979F5895FA-G0002` (13942 B, SHA-256 `9ad324b35cae22ecd30abc0ed2c7475ac2b29cfdb06eb7040ec3104768e8f998`, source `ded1252bd7e0a5bfad19afd968c9f21d4c5e9471`, seal `SEALED` at `2026-11-18T01:59:51Z`). Original card follows verbatim; no forecast reissued; Track P scored separately via `ml one-chat score`.

# Pregame card — LOCAL-20261118DA6D9F6251746B979F5895FA-G0002 — Michigan State at Tennessee — 17 Nov 2026 ET

**Forecast custody:** First written original at 2026-11-18T12:58:17+11:00; registered G0002 on `forecast-seals` before research, card is not sealed until independently verified. Governance `main@cb97bbc2a9f882e7f8a093648b6137315951da8b`, MDS-2026.11.18-v29.1 / CR-2026.11.18-R2 / P-2026.11.18-v29.1 / SCV-2026.11.18-v20, ONE-CHAT-v3, DROP-SEAL-v1. MARKET_BLIND / SPORTS_ONLY. No external predictions or odds read or used.

## Original owner request — exact text, preserved

```text
Upcoming Basketball Game: Michigan State @ Tennessee, NCAAB,
Estimated Game Time Start: 18 November 2026, 1:00 PM AEDT (can be delayed so continue the process as normal)

Michigan -2.5
Tennnessee +2.5
Combined Total Points: Over/Under 149.5 points
```

## A1 — Identity, timing, state
- Native official host game-center identity: `UTK_GAMECENTER:30166`; away `Michigan State`; home `Tennessee`; college basketball 2026–27 regular season. University game page https://utsports.com/game-center/30166.
- Official scheduled tip: `2026-11-18T13:00:00+11:00` = Nov 17 2026 9:00 PM America/New_York. The owner stated the same estimated time. Food City Center, Knoxville.
- Request receipt clock: approximately `2026-11-18T12:52:00+11:00` at minute-level only (the original request's seconds are not known); GitHub published registration is the timing authority, not this receipt.
- Registration drop commit `64b13076d2957cc4c89423355598d94d175fc1e2`, workflow run `44219203995` green. Independently read `research/one_chat/REQUEST_INDEX.csv` and all three request files from `forecast-seals` before research.
- Research start `2026-11-18T12:54:27+11:00` after registration verification; official NOT_STARTED check https://utsports.com/game-center/30166 read `2026-11-18T12:54:56+11:00`, showed 'Stats for upcoming game' and no game outcome. Research completed 2026-11-18T12:58:17+11:00. Outcome exposure NONE.
- Actual tip/first-play: NOT_VERIFIED. Even a successful seal is only potentially eligible until official first-play timing is independently captured during settlement.

## A2 — Frozen supplied contracts
| Label | Family | Away | Home / alternate | Settlement endpoint |
|---|---|---|---|---|
| L1 | HANDICAP | Michigan -2.5 | Tennnessee +2.5 (verbatim request typo, represents home Tennessee) | Full game points differential inclusive of any overtime |
| L2 | TOTAL | OVER 149.5 | UNDER 149.5 | Full game combined points inclusive of any overtime |

No separate winner contract requested; no winner probability added to the ONECHAT_V1 block. No push possible at half-point lines. No bookmaker price, tips or external forecast inputs. There is no frozen sporting league baseline in the registered CONTRACTS.csv.

## A3 — Verified sporting observations / form
- Michigan State 4–0 this season. Results before cutoff: Nov 2 Quinnipiac W 96–59, Nov 5 Toledo W 91–61, Nov 10 Duke W 79–73 (neutral), Nov 13 Northern Iowa W 106–72. Source https://msuspartans.com/sports/mens-basketball/schedule. Season points scored 372 / 4 = 93.00 and allowed 265 / 4 = 66.25.
- Tennessee 3–0 this season, all at home. Nov 3 Wofford W 90–59, Nov 9 Radford W 70–47, Nov 13 Tennessee State W 83–78. Source https://utsports.com/sports/mbball/schedule. Points scored 243 / 3 = 81.00 and allowed 184 / 3 = 61.33.
- Neither side has five current-season completed games: last-five/ten/twenty full windows are unavailable and are not silently represented by three or four observations. Opponent strengths differ substantially; Michigan State's Duke victory offers a stronger opponent reference than Tennessee's opening run, but no opponent-adjusted efficiency was quantified. Sources https://msuspartans.com/sports/mens-basketball/schedule and https://utsports.com/sports/mbball/schedule.
- Both last played Nov 13, three full calendar rest days before the Nov 17 game; not back-to-back. Michigan State's first true road contest of the season at Tennessee. Home court is an uncertainty, and Tennessee's all-home recent performance is already embedded in its raw samples (do not double count an invented home adjustment).
- Michigan State starting forward Jordan Scott injured his shoulder in the prior game; coach said the injury was not severe but return remained uncertain. Source https://www.aol.com/articles/msu-head-basketball-coach-izzo-160517000.html. No verified final availability, starting five or measured replacement-minute impact at cutoff. Tennessee complete roster availability also unconfirmed. Avoid invented injury points adjustment.
- The sole recent head-to-head in an official competitive game was 2010; not assigned predictive weight. Coaches: Tom Izzo and Rick Barnes. No verified in-game target score accessed. Official future result source https://utsports.com/game-center/30166.

## A4 — Transparent low-sample analyst approximation, not calibrated
Model is a simple last-completed-season-to-date attack/defence cross-mean calculation, **not** a simulated or fitted predictive model. Equal weights per team's offence and the opponent's defence; team schedules are not strength-normalised. Explicit no numeric availability, travel or venue modification because measurements were not obtained.

- MSU expected points = (93.00 + 61.3333)/2 = **77.1667**.
- Tennessee expected points = (81.00 + 66.25)/2 = **73.6250**.
- Mean total = **150.7917**; mean away-minus-home margin = **+3.5417**.
- Diagnostic normal approximation with **assumed, non-calibrated** margin SD = 12 and total SD = 16 points, only to articulate uncertainty. These widths are declared analyst assumptions, *not estimated from 3–4 games or certified NCAA parameters*. Conditional on that approximation:
  - P(Michigan -2.5) = Φ((3.5417 − 2.5)/12) = **0.5346**. P(Tennessee +2.5) = **0.4654**.
  - P(OVER 149.5) = Φ((150.7917 − 149.5)/16) = **0.5322**. P(UNDER 149.5) = **0.4678**.
- Sensitivity: an unmeasured 3-point shift in the matchup margin moves Michigan's cover p approximately from 0.44 to 0.63; a 6-point shift in the total centre moves over p approximately 0.39–0.67. These are conditional illustrative bounds, not calibrated intervals. Estimated player unavailability could materially alter either centre. Pregame probabilities are deliberately close to 0.5; unsupported precision is not treated as confidence.

## Decision block — supplied lines only
| Rank diagnostic | Supplied contract | p | Principal failure route |
|---|---|---:|---|
| 1 (below gate) | Michigan -2.5 | 53.46% | Tennessee home defence and Scott uncertainty leave road favourites with narrow win or loss |
| 2 (below gate) | OVER 149.5 | 53.22% | Slower-than-assumed pace, efficient Tennessee interior defence, limited-season sample |
| — | Tennessee +2.5 | 46.54% | Michigan State superior opposition experience and outside shooting create >2-point separation |
| — | UNDER 149.5 | 46.78% | Michigan State transition scoring and three-point volatility push both clubs above expected means |

No Rank-1 >=62% or Rank-2 >=58%; **NO RANKED SELECTION**, despite nonzero illustrative probabilities. Distinguish indicative centre scores from validated forward skill. Both sides of exactly two supplied lines preserved.

## A5–A9 — Missingness, sources, checks, settlement readiness
- A5 Outcomes: four decisive contract sides; no line push possible. No unexpected contracts and no winner row supplied. Expected scores: Michigan State 77.17, Tennessee 73.63.
- A6 Adjustments: NONE. Key Jordan Scott availability status UNMEASURED; no absence effect guessed. In the card block set all `availability_basis=UNMEASURED` so subsequent calibration audit can test those forecasts.
- A7 Model status: MODEL_NOT_RUN; NO Monte Carlo, no repository kit executed, no independent posterior validation, no historical result data from after the research cutoff. Priors/tail normal widths are purely illustrative analyst assumptions.
- A8 Sources opened during this session: official schedule pages https://msuspartans.com/sports/mens-basketball/schedule, https://utsports.com/sports/mbball/schedule; official pregame game-center https://utsports.com/game-center/30166; Michigan State official media https://msuspartans.com/news/2026/11/16/mens-basketball-no-2-michigan-state-faces-no-14-tennessee-on-tuesday-night-in-knoxville ; injury quotation https://www.aol.com/articles/msu-head-basketball-coach-izzo-160517000.html. Publication times are distinct from review timestamps. Official source capture is not persisted independently outside this chat; settlement must save original result/first-play captures and hashes. Last5/10/20, starters, opponent adjusted rates, confirmed player impacts all have unresolved missingness.
- A9 No model fit, card linter or calibrated model claimed. ONECHAT_V1 fields completed exactly from registered request; source fields for every observed FACTS row are page URLs (to avoid G0001's failure). Keep original card bytes unchanged after issuing; request is already frozen independently on forecast-seals.

<!-- BEGIN ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0002 -->
format: ONECHAT_V1
card_key: 20261118DA6D9F6251746B979F5895FA-G0002
sport: Basketball
competition: NCAAB
home: Tennessee
away: Michigan State
scheduled_start: 2026-11-18T13:00:00+11:00
request_at: 2026-11-18T12:52:00+11:00
research_start_at: 2026-11-18T12:54:27+11:00
research_end_at: 2026-11-18T12:58:17+11:00
not_started_source: https://utsports.com/game-center/30166
not_started_observed_at: 2026-11-18T12:54:56+11:00
outcome_exposure: NONE

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,HANDICAP,AWAY,-2.5,0.5346,,3.5417,UNMEASURED,https://utsports.com/game-center/30166
L1,HANDICAP,HOME,2.5,0.4654,,-3.5417,UNMEASURED,https://utsports.com/game-center/30166
L2,TOTAL,OVER,149.5,0.5322,,150.7917,UNMEASURED,https://utsports.com/game-center/30166
L2,TOTAL,UNDER,149.5,0.4678,,150.7917,UNMEASURED,https://utsports.com/game-center/30166

FACTS
side,field,value,source,observed_at
HOME,season_games,3,https://utsports.com/sports/mbball/schedule,2026-11-18T12:55:54+11:00
HOME,season_score_for_pg,81.0,https://utsports.com/sports/mbball/schedule,2026-11-18T12:55:54+11:00
HOME,season_score_against_pg,61.333333,https://utsports.com/sports/mbball/schedule,2026-11-18T12:55:54+11:00
HOME,last5_score_for_pg,MISSING,Only 3 completed regular season games as of research cutoff,
HOME,last5_score_against_pg,MISSING,Only 3 completed regular season games as of research cutoff,
HOME,last10_score_for_pg,MISSING,Only 3 completed regular season games as of research cutoff,
HOME,last10_score_against_pg,MISSING,Only 3 completed regular season games as of research cutoff,
HOME,rest_days,3,https://utsports.com/sports/mbball/schedule,2026-11-18T12:55:54+11:00
HOME,back_to_back,NO,https://utsports.com/sports/mbball/schedule,2026-11-18T12:55:54+11:00
HOME,key_absences,MISSING,No verified comprehensive injury report by research cutoff,
HOME,lineup_confirmed,MISSING,No confirmed starting five in accessible official prematch sources,
HOME,venue,Food City Center Knoxville TN,https://utsports.com/game-center/30166,2026-11-18T12:55:54+11:00
HOME,travel_km,MISSING,No verifiable traveled route distance established,
HOME,opponent_strength,MISSING,Opponent adjusted efficiencies not computed before cutoff,
HOME,opponent_strength_method,MISSING,No independently verified schedule strength adjustment method fitted,
HOME,availability_effect,MISSING,No measured with without team outcome impact for pending or unknown absences,
HOME,adjustment_basis,MISSING,No measured or admitted numeric lineup travel or home adjustment applied,
HOME,last20_score_for_pg,MISSING,Only 3 completed regular season games; fewer than 20,
HOME,last20_score_against_pg,MISSING,Only 3 completed regular season games; fewer than 20,
AWAY,season_games,4,https://msuspartans.com/sports/mens-basketball/schedule,2026-11-18T12:55:54+11:00
AWAY,season_score_for_pg,93.0,https://msuspartans.com/sports/mens-basketball/schedule,2026-11-18T12:55:54+11:00
AWAY,season_score_against_pg,66.25,https://msuspartans.com/sports/mens-basketball/schedule,2026-11-18T12:55:54+11:00
AWAY,last5_score_for_pg,MISSING,Only 4 completed regular season games as of research cutoff,
AWAY,last5_score_against_pg,MISSING,Only 4 completed regular season games as of research cutoff,
AWAY,last10_score_for_pg,MISSING,Only 4 completed regular season games as of research cutoff,
AWAY,last10_score_against_pg,MISSING,Only 4 completed regular season games as of research cutoff,
AWAY,rest_days,3,https://msuspartans.com/sports/mens-basketball/schedule,2026-11-18T12:55:54+11:00
AWAY,back_to_back,NO,https://msuspartans.com/sports/mens-basketball/schedule,2026-11-18T12:55:54+11:00
AWAY,key_absences,Jordan Scott shoulder status uncertain per 16 Nov coach remarks,https://www.aol.com/articles/msu-head-basketball-coach-izzo-160517000.html,2026-11-18T12:55:54+11:00
AWAY,lineup_confirmed,MISSING,No confirmed starting five in accessible official prematch sources,
AWAY,venue,Food City Center Knoxville TN,https://utsports.com/game-center/30166,2026-11-18T12:55:54+11:00
AWAY,travel_km,MISSING,No verifiable traveled route distance established,
AWAY,opponent_strength,MISSING,Opponent adjusted efficiencies not computed before cutoff,
AWAY,opponent_strength_method,MISSING,No independently verified schedule strength adjustment method fitted,
AWAY,availability_effect,MISSING,No measured with without team outcome impact for pending or unknown absences,
AWAY,adjustment_basis,MISSING,No measured or admitted numeric lineup travel or home adjustment applied,
AWAY,last20_score_for_pg,MISSING,Only 4 completed regular season games; fewer than 20,
AWAY,last20_score_against_pg,MISSING,Only 4 completed regular season games; fewer than 20,
<!-- END ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0002 -->
<!-- END CANONICAL RESEARCH P-687 -->

<!-- BEGIN RESEARCH ADDENDUM P-687 2026-11-22-settlement-revision-1 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_11.md`, P-687. Source: `research/verification/mini_import_P-686_P-696_2026-11-22-1/SETTLEMENT.md` (P-687); exact settlement block follows.

<!-- BEGIN SETTLEMENT P-687 LOCAL-20261118DA6D9F6251746B979F5895FA-G0002 revision-1 -->
### P-687 · Basketball/NCAAB 2026-27 — Michigan State Spartans @ Tennessee Volunteers · 2026-11-17 ET · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0002` · `UTK_GAMECENTER:30166` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-18T01:59:51Z`; assessment `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (A):** **Tennessee 61-46 Michigan State** · Linescore: `MSU 25-21=46; TENN 27-34=61 (sum check: 25+21=46, 27+34=61)`.
- **Permitted source & capture:** `https://www.foxsports.com/college-basketball/michigan-state-spartans-vs-tennessee-volunteers-nov-17-2026-game-boxscore-264973` · capture `2026-11-22/G0002_fox_box.html` (SHA-256 `2eb3a3d42da1d9407edad4f3d4a8afb53769459e9b7635cebf59e5e1ee3d9694`). Corroboration: https://utsports.com/game-center/30166 (official host game center captured in G0002_utk.html).
- **Card-mean Brier / d:** `0.2845` / `-0.0345`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | AWAY | -2.5 | 0.5346 | 3.5417 | UNMEASURED | **LOSS** | 0.2858 |
| L1 | NOT_RANKED | HANDICAP | HOME | 2.5 | 0.4654 | -3.5417 | UNMEASURED | **WIN** | 0.2858 |
| L2 | R2 | TOTAL | OVER | 149.5 | 0.5322 | 150.7917 | UNMEASURED | **LOSS** | 0.2832 |
| L2 | NOT_RANKED | TOTAL | UNDER | 149.5 | 0.4678 | 150.7917 | UNMEASURED | **WIN** | 0.2832 |

**R1–R12 retrospective:** Tennessee held Michigan State to 9-50 FG (18.0%) and 4-19 3PT (21.1%); MSU scored 24 of its 46 points at the free-throw line (Jeremy Fears Jr. 0-3 FG, 16-18 FT). Total finished 42.5 points below 149.5. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-001 · P-687 · Michigan -2.5 (TOP_SIDE_AND_RANK_1) — Verdict: `VARIANCE` · Class: `VARIANCE`**
1. **Contract & trigger:** Michigan -2.5 (TOP_SIDE_AND_RANK_1).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Tennessee 61-46 Michigan State (MSU 25-21=46; TENN 27-34=61 (sum check: 25+21=46, 27+34=61)).
4. **Outcome in frozen distribution & what decided the game:** MSU shot an extreme-tail 9-50 FG (18.0%), a multi-sigma shooting collapse despite drawing 30 FTAs and committing only 3 turnovers. However, stated p=0.5346 sat inside the H-NODIR coin-flip band (|p-0.5| < 0.05) and carried availability_basis=UNMEASURED.
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `VARIANCE` (`VARIANCE`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.

**DLR-2026-11-22-002 · P-687 · Over 149.5 (TOP_TOTAL) — Verdict: `MODEL_LIMIT` · Class: `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`**
1. **Contract & trigger:** Over 149.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Tennessee 61-46 Michigan State (MSU 25-21=46; TENN 27-34=61 (sum check: 25+21=46, 27+34=61)).
4. **Outcome in frozen distribution & what decided the game:** Card projected 150.79 (p=0.5322) from raw early-season scoring averages without a tempo/defensive-efficiency model for Tennessee's elite half-court defense; actual total was 107 (-42.5 vs line, z approx -2.4).
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `MODEL_LIMIT` (`BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.

**Joint side + total loss note (P-687):** Both top side and top total lost on this card (card-mean Brier `0.2845`, `d = -0.0345`). Shared root causes: unmeasured availability / opponent-strength overreach paired with unadjusted total Over bias.
<!-- END SETTLEMENT P-687 LOCAL-20261118DA6D9F6251746B979F5895FA-G0002 revision-1 -->
<!-- END RESEARCH ADDENDUM P-687 2026-11-22-settlement-revision-1 -->

<!-- BEGIN CANONICAL RESEARCH P-688 -->
## P-688 — Basketball/Japan B.LEAGUE Premier 2026-27 (ScheduleKey 506605) — Chiba Jets vs Akita Northern Happinets · 2026-11-18 JST

Canonical retention by prompt-4 import `2026-11-22T06:40:00+00:00`. Scheduled start `2026-11-18T21:05:00+11:00`. Original `20261118DA6D9F6251746B979F5895FA-G0003` (10449 B, SHA-256 `5fe6e94aed7a6bf660fed795c720d58519fcd6b299b37d068962ee29e68c7347`, source `964f9360919906978d527b02441773baf285901d`, seal `SEALED` at `2026-11-18T10:05:22Z`). Original card follows verbatim; no forecast reissued; Track P scored separately via `ml one-chat score`.

# Pre-game ONECHAT_V1 card — LOCAL-20261118DA6D9F6251746B979F5895FA-G0003 — Chiba Jets vs Akita Northern Happinets

**Source custody:** Original user request registered and independently verified on forecast-seals before research. This original is issued once, and a rejected seal is not silently revised. GitHub main strictly read-only. Sports-only / market-blind; no odds or external tip inputs. Analytical approximation; no fitted model, independent calibration, or Monte Carlo execution claimed.

## Original request (verbatim)
```text
[$github](app://connector_76869538009648d5b282a4bb21c3d157) Upcoming Basketball Game: Chiba Jets vs Akita Northern happinets, Japan B league Premier,\
Estimated Game Time Start: 18 November 2026, 9:05 PM AEDT (can be delayed so continue the process as normal)\
\
Jets -8.5\
Happinets +8.5\
Combined Total: Over/Under 180.5 Points
```

## Event / preregistration evidence
- Official match: https://www.bleague.jp/game_detail/?ScheduleKey=506605, B.LEAGUE PREMIER 2026–27, 18 Nov 2026 19:05 JST = 21:05 AEDT. Chiba Jets HOME at LaLa arena TOKYO-BAY, Akita Northern Happinets AWAY; official native schedule key 506605.
- REQUEST/EVENT/CONTRACTS were dropped together at `0959252ca305f13fc5d1301c7aba2483ac631e45`; workflow `44281123788` seal-drops SUCCESS and index and original files independently read on `forecast-seals` before sports research.
- Official page before tip showed 19:05 TIP OFF without live score. Outcome exposure NONE. Actual first play not independently verified; prospective eligibility remains pending a server push record and first-play capture.

## Pre-game sporting research / dated evidence
- Season at pre-game: Chiba 9-10, 92.8 for / 95.9 against in 19 games (official https://www.bleague.jp/club_detail/?TeamID=704); Akita 5-13, 83.3 for / 90.7 against in 18 (official https://www.bleague.jp/club_detail/?TeamID=693); team pages state 17 Nov 2026 22:44 JST data refresh.
- Last five Chiba results newest first: 104-110 San-en (Nov 16, overtime), 86-80 Nagasaki (Nov 14), 90-87 Shiga (Nov 12), 106-94 Osaka (Nov 10), 111-103 Saga (Nov 8). Last five averages 99.4 for / 94.8 against. Dated official rows https://www.bleague.jp/club_detail/?TeamID=704 and https://www.bleague-db.com/teams/704.
- Last five Akita: 82-76 Osaka (Nov 15), 94-110 Nagoya (Nov 13), 83-95 Ibaraki (Nov 11), 96-101 Shinshu (Nov 8), 118-123 Hokkaido (Nov 6). Last five averages 94.6 for / 101.0 against. Official https://www.bleague.jp/club_detail/?TeamID=693 and https://www.bleague-db.com/teams/693.
- Last ten Chiba averages 92.3 for / 91.1 against; Akita 89.1 / 95.9. Dated rows and true n=10 from https://www.bleague-db.com/teams/704 and https://www.bleague-db.com/teams/693. Insufficient 20-game current-season windows (19 Chiba, 18 Akita).
- Chiba had one full intervening rest day (17 Nov) after Nov 16 home game, no B2B; Akita had two full intervening days (16-17 Nov) after Nov 15 home game and travelled to Chiba; verified route distance unavailable.
- Chiba official: Nate Williams placed on injury list Nov 9, Matt Costello removed from injury list Nov 9; Luke Maye contract terminated Nov 13. Sources https://chibajets.jp/news/detail/id=27523, https://chibajets.jp/news/detail/id=27524, https://chibajets.jp/news/detail/id=27543. Akita Reid Travis placed on injury list Nov 5, Angelo Chol removed: https://www.bleague.jp/media_news/detail/id=667179. The official pregame starting fives and full active benches were NOT independently confirmed. Absence-to-points effects NOT measured.
- Opponent-adjusted efficiencies, independent pace/possessions samples, official late-minute rotation, exact venue travel km and live starting lineup not confirmed. No unsupported adjustments are hidden in numeric forecasts.

## Coherent analytic approximation (not a fitted predictive model)
- Season-only expected home points = (Chiba PF 92.8 + Akita PA 90.7) /2 = 91.75. Season-only away = (Akita PF 83.3 + Chiba PA 95.9) /2 = 89.60.
- Last-five cross-team terms: Chiba 100.20; Akita 94.70. Pre-declared arithmetic weights: 75% season, 25% last-five, to restrain pace/OT recency noise. No invented home-court or availability shift; both season samples include existing venue and roster regimes.
- Expected Chiba = 93.8625; Akita = 90.8750; combined 184.7375; Chiba winning margin 2.9875. Symmetric normal margin SD 15.0 and total SD 20.0 reflect approximate historical B League raw 14.94 / 17.66 point widths in repo PARAMETERS.md, widened for new Premier regime and unconfirmed lineups; they are analyst assumptions, not calibrated to the 2026–27 Premier season.
- Both distributions use **final scores inclusive of overtime**. The historical inputs already include observed overtime results; B.PREMIER regulation-tie frequency and regulation-only distributions could not be independently identified in time for a separate OT mass branch. This approximation is not a verified pace × efficiency model and has potentially material OT bias; no simulation was executed. Spread and total use independent marginal normals; joint covariance is not supported.
- P(Chiba wins by >=9) = 1-Φ((8.5−2.9875)/15.0) = 0.356623; complement 0.643377. P(total >=181) = 1-Φ((180.5−184.7375)/20.0) = 0.583898; complement 0.416102. Continuous half-point approximation avoids pushes.
- Most material failure branches: missing lineup effects, Chiba offensive loss/rebalancing after player departures, Akita road fatigue, overtime-affected totals and nonstationary 2026-27 scoring. The apparent ~64% Akita cushion is UNQUALIFIED and cannot be represented as a proven rank-1 pick with lineups unconfirmed. Sensitivity (illustrative): margin ±4 points moves Akita +8.5 probability materially; total mean ±7 points moves over probability materially.

<!-- BEGIN ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0003 -->
format: ONECHAT_V1
card_key: 20261118DA6D9F6251746B979F5895FA-G0003
sport: Basketball
competition: Japan B league Premier
home: Chiba Jets
away: Akita Northern Happinets
scheduled_start: 2026-11-18T21:05:00+11:00
request_at: 2026-11-18T20:58:00+11:00
research_start_at: 2026-11-18T21:00:44+11:00
research_end_at: 2026-11-18T21:03:59+11:00
not_started_source: https://www.bleague.jp/game_detail/?ScheduleKey=506605
not_started_observed_at: 2026-11-18T21:01:22+11:00
outcome_exposure: NONE

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,HANDICAP,HOME,-8.5,0.356623,,2.9875,UNMEASURED,https://www.bleague.jp/game_detail/?ScheduleKey=506605
L1,HANDICAP,AWAY,8.5,0.643377,,-2.9875,UNMEASURED,https://www.bleague.jp/game_detail/?ScheduleKey=506605
L2,TOTAL,OVER,180.5,0.583898,,184.7375,UNMEASURED,https://www.bleague.jp/game_detail/?ScheduleKey=506605
L2,TOTAL,UNDER,180.5,0.416102,,184.7375,UNMEASURED,https://www.bleague.jp/game_detail/?ScheduleKey=506605

FACTS
side,field,value,source,observed_at
HOME,season_games,19,https://www.bleague.jp/club_detail/?TeamID=704,2026-11-18T21:02:15+11:00
HOME,season_score_for_pg,92.8,https://www.bleague.jp/club_detail/?TeamID=704,2026-11-18T21:02:15+11:00
HOME,season_score_against_pg,95.9,https://www.bleague.jp/club_detail/?TeamID=704,2026-11-18T21:02:15+11:00
HOME,last5_score_for_pg,99.4,https://www.bleague-db.com/teams/704,2026-11-18T21:02:15+11:00
HOME,last5_score_against_pg,94.8,https://www.bleague-db.com/teams/704,2026-11-18T21:02:15+11:00
HOME,last10_score_for_pg,92.3,https://www.bleague-db.com/teams/704,2026-11-18T21:02:15+11:00
HOME,last10_score_against_pg,91.1,https://www.bleague-db.com/teams/704,2026-11-18T21:02:15+11:00
HOME,rest_days,1,https://www.bleague.jp/club_detail/?TeamID=704,2026-11-18T21:02:15+11:00
HOME,back_to_back,NO,https://www.bleague.jp/club_detail/?TeamID=704,2026-11-18T21:02:15+11:00
HOME,key_absences,Nate Williams injury list since Nov 9; Luke Maye contract terminated Nov 13; Matt Costello returned,https://chibajets.jp/news/detail/id=27523,2026-11-18T21:02:15+11:00
HOME,lineup_confirmed,MISSING,No official confirmed starting five verified before freeze,
HOME,venue,LaLa arena TOKYO-BAY,https://www.bleague.jp/game_detail/?ScheduleKey=506605,2026-11-18T21:02:15+11:00
HOME,travel_km,MISSING,No verified team-specific journey distance,
HOME,opponent_strength,MISSING,No opponent-adjusted efficiency computation,
HOME,opponent_strength_method,MISSING,No fitted strength-of-schedule method,
HOME,availability_effect,MISSING,Absence-to-points impact not quantified,
HOME,adjustment_basis,MISSING,No independently estimated numeric adjustment applied,
HOME,last20_score_for_pg,MISSING,Only 19 completed league matches,
HOME,last20_score_against_pg,MISSING,Only 19 completed league matches,
AWAY,season_games,18,https://www.bleague.jp/club_detail/?TeamID=693,2026-11-18T21:02:15+11:00
AWAY,season_score_for_pg,83.3,https://www.bleague.jp/club_detail/?TeamID=693,2026-11-18T21:02:15+11:00
AWAY,season_score_against_pg,90.7,https://www.bleague.jp/club_detail/?TeamID=693,2026-11-18T21:02:15+11:00
AWAY,last5_score_for_pg,94.6,https://www.bleague-db.com/teams/693,2026-11-18T21:02:15+11:00
AWAY,last5_score_against_pg,101.0,https://www.bleague-db.com/teams/693,2026-11-18T21:02:15+11:00
AWAY,last10_score_for_pg,89.1,https://www.bleague-db.com/teams/693,2026-11-18T21:02:15+11:00
AWAY,last10_score_against_pg,95.9,https://www.bleague-db.com/teams/693,2026-11-18T21:02:15+11:00
AWAY,rest_days,2,https://www.bleague.jp/club_detail/?TeamID=693,2026-11-18T21:02:15+11:00
AWAY,back_to_back,NO,https://www.bleague.jp/club_detail/?TeamID=693,2026-11-18T21:02:15+11:00
AWAY,key_absences,Reid Travis injury list since Nov 5; Angelo Chol returned,https://www.bleague.jp/media_news/detail/id=667179,2026-11-18T21:02:15+11:00
AWAY,lineup_confirmed,MISSING,No official confirmed starting five verified before freeze,
AWAY,venue,LaLa arena TOKYO-BAY,https://www.bleague.jp/game_detail/?ScheduleKey=506605,2026-11-18T21:02:15+11:00
AWAY,travel_km,MISSING,No verified team-specific journey distance,
AWAY,opponent_strength,MISSING,No opponent-adjusted efficiency computation,
AWAY,opponent_strength_method,MISSING,No fitted strength-of-schedule method,
AWAY,availability_effect,MISSING,Absence-to-points impact not quantified,
AWAY,adjustment_basis,MISSING,No independently estimated numeric adjustment applied,
AWAY,last20_score_for_pg,MISSING,Only 18 completed league matches,
AWAY,last20_score_against_pg,MISSING,Only 18 completed league matches,
<!-- END ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0003 -->
<!-- END CANONICAL RESEARCH P-688 -->

<!-- BEGIN RESEARCH ADDENDUM P-688 2026-11-22-settlement-revision-1 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_11.md`, P-688. Source: `research/verification/mini_import_P-686_P-696_2026-11-22-1/SETTLEMENT.md` (P-688); exact settlement block follows.

<!-- BEGIN SETTLEMENT P-688 LOCAL-20261118DA6D9F6251746B979F5895FA-G0003 revision-1 -->
### P-688 · Basketball/Japan B.LEAGUE Premier 2026-27 (ScheduleKey 506605) — Chiba Jets vs Akita Northern Happinets · 2026-11-18 JST · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0003` · `B.LEAGUE:506605` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-18T10:05:22Z`; assessment `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (A):** **Chiba Jets 89-84 Akita Northern Happinets** · Linescore: `CHB 24-24-16-25=89; AKI 18-27-15-24=84 (sum check: 24+24+16+25=89, 18+27+15+24=84)`.
- **Permitted source & capture:** `https://www.bleague.jp/game_detail/?ScheduleKey=506605` · capture `2026-11-22/G0003_bleague.html` (SHA-256 `740da59fec86f6c659e0dc2fe18b16a2eb065cfdb9100eb2060cbe7cd5e09055`). Corroboration: https://www.bleague.jp/en/game_detail/?ScheduleKey=506605 (captured in G0003_bleague_en.html).
- **Card-mean Brier / d:** `0.2341` / `+0.0159`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | NOT_RANKED | HANDICAP | HOME | -8.5 | 0.356623 | 2.9875 | UNMEASURED | **LOSS** | 0.1272 |
| L1 | R1 | HANDICAP | AWAY | 8.5 | 0.643377 | -2.9875 | UNMEASURED | **WIN** | 0.1272 |
| L2 | R2 | TOTAL | OVER | 180.5 | 0.583898 | 184.7375 | UNMEASURED | **LOSS** | 0.3409 |
| L2 | NOT_RANKED | TOTAL | UNDER | 180.5 | 0.416102 | 184.7375 | UNMEASURED | **WIN** | 0.3409 |

**R1–R12 retrospective:** Chiba won by 5 (Akita +8.5 Rank 1 won comfortably at p=0.6434); slow Q3 (16-15, 31 pts) kept combined total at 173 vs 180.5. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-003 · P-688 · Over 180.5 (TOP_TOTAL) — Verdict: `MODEL_LIMIT` · Class: `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`**
1. **Contract & trigger:** Over 180.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Chiba Jets 89-84 Akita Northern Happinets (CHB 24-24-16-25=89; AKI 18-27-15-24=84 (sum check: 24+24+16+25=89, 18+27+15+24=84)).
4. **Outcome in frozen distribution & what decided the game:** Card projected 184.74 (p=0.5839) from blended scoring rates without adjusting for Akita's slower defensive tempo; Q3 produced only 31 combined points and final total finished 173 (-7.5 vs line).
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `MODEL_LIMIT` (`BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.
<!-- END SETTLEMENT P-688 LOCAL-20261118DA6D9F6251746B979F5895FA-G0003 revision-1 -->
<!-- END RESEARCH ADDENDUM P-688 2026-11-22-settlement-revision-1 -->

<!-- BEGIN CANONICAL RESEARCH P-689 -->
## P-689 — Ice Hockey/AHL 2026-27 (game 1029340) — Rochester Americans @ Syracuse Crunch · 2026-11-18 ET

Canonical retention by prompt-4 import `2026-11-22T06:40:00+00:00`. Scheduled start `2026-11-19T11:00:00+11:00`. Original `20261118DA6D9F6251746B979F5895FA-G0005` (12469 B, SHA-256 `ea96d8355694abc09090fdaa23269dbc9205832a48bbaa18324fe33c00cde2f3`, source `89d2239cabe6ba7e73a65acc30c9152f3e015b4e`, seal `SEALED` at `2026-11-18T23:57:40Z`). Original card follows verbatim; no forecast reissued; Track P scored separately via `ml one-chat score`.

# Pregame research card — LOCAL-20261118DA6D9F6251746B979F5895FA-G0005 — AHL ROC at SYR

**Custody and identity.** Chat mini `20261118DA6D9F6251746B979F5895FA`; corrected G0005 owner request replacing FAILED/UNREGISTERED G0004 intake for the *same* `AHL:1029340` fixture. Never count G0004 as a separate match. Request registration commit `a037a0e17bac2436780e84c56cf606e8c773fc84` verified green via GitHub check `44424017311`, and all request files plus request index independently inspected on `forecast-seals` before research. Read-only governing main `cb97bbc2a9f882e7f8a093648b6137315951da8b`; ONECHAT_V1 / DROP-SEAL-v1; no GitHub source files modified. Original request is preserved verbatim below.

## Owner request, exact bytes

```text
Upcoming Ice Hockey Game: ROC Americans @ SYR Crunch, AHL,
Estimated Game Time Start: 19 November 2026, 11:00 AM AEDT (can be delayed so continue the process as normal)

Americans -0.5
Crunch -0.5
Combined Total Goals: Over/Under 5.5 goals
```

## Evidence and event gate

- Scheduled start: 2026-11-18 7:00 PM EST / 2026-11-19 11:00 AM AEDT, Syracuse home at Upstate Medical University Arena. League fixture ID `1029340` from https://theahl.com/stats/schedule/323/94.
- At `2026-11-19T10:51:08+11:00`, https://www.hockey.com/ahl/teams/rochester-americans/schedule listed this fixture as **Next** with a 7:00 PM EST tip and *no* result, independently cross-checked against https://www.hockey.com/ahl/teams/syracuse-crunch/schedule. No game scores for this fixture were accessed; exposure `NONE`.
- Source collection and calculator window: `2026-11-19T10:51:00+11:00` to `2026-11-19T10:55:18+11:00`. Sources checked are official 17–18 November previews and season-to-date game logs. Online pages with unconfirmed starters were not treated as starting confirmation.
- User requested two separate team −0.5 handicaps. Each is preserved as a separately labeled contract with the opposite +0.5 side. Under AHL full-game final-score settlement including one winner goal after any shootout, those two −0.5 selections are **exactly opposite outcomes**. They are not independent performance observations and must not inflate the number of independent games.

## Dated evidence: team profiles and forms

Official Syracuse weekly report https://syracusecrunch.com/news/2026/11/17/syracuse-crunch-weekly-release-vol-33-no-7.aspx records Syracuse 15 played, GF 40, GA 49 (2.667 scored; 3.267 conceded per game), W6–L6–OTL3, 2–2–3 at home, last10 4–3–3, power-play 19% (12/63), penalty kill 75.8% (47/62), and 24.87 shots for vs 26.67 against per game. Rochester 15 played, GF 48, GA 39 (3.20 scored; 2.60 conceded), W8–L6–SOL1, road 2–3–0–1, last10 W5–L5. Both last played Saturday 14 November, yielding three off-days, not back-to-back.

- Rochester dated last five, oldest to newest: Nov 4 Cleveland 4–1; Nov 6 Hartford 4–2; Nov 7 Utica 1–4; Nov 13 Laval 1–3; Nov 14 Laval 5–4 OT. **5-game GF/GA 3.00/2.80**. Last 10 **3.10/3.10**. Full 15 **3.20/2.60**. Underlying results: https://www.hockey.com/ahl/teams/rochester-americans/schedule and https://www.hockey.com/ahl/teams/syracuse-crunch/schedule.
- Syracuse dated last five: Nov 6 Utica 2–5; Nov 7 Hartford 2–3 OT; Nov 11 Laval 0–5; Nov 13 Toronto 2–3 OT; Nov 14 Utica 3–2. **5-game GF/GA 1.80/3.60**. Last 10 **3.00/3.10**. Full 15 **2.667/3.267**. Underlying results: https://www.hockey.com/ahl/teams/syracuse-crunch/schedule and https://syracusecrunch.com/news/2026/11/17/syracuse-crunch-weekly-release-vol-33-no-7.aspx.
- Head-to-head this season before the subject game: Rochester 7–1 Syracuse on Oct 9, Syracuse 4–2 Rochester on Oct 17, Rochester 3–2 OT Syracuse on Oct 23. Three meetings are not a stable predictive win-rate. Official corroboration: https://www.amerks.com/news/detail/game-preview-amerks-begin-three-game-roadie-in-syracuse.
- The official Rochester preview notes that its penalty kill allowed six power-play goals in its last 14 attempts and now stood at 77.4%; Syracuse's PP was 19%. ROC road record 2–3–0–1 contrasts with its 6–3 home record, without a measured points-of-goals home impact. https://www.amerks.com/news/detail/game-preview-amerks-begin-three-game-roadie-in-syracuse
- Candidate goalies only: Syracuse's Mads Søgaard was reported at .892 through the Nov 17 weekly release; Rochester's Matthew Villalta at .913 in the Nov 18 Syracuse preview search listing. Neither was independently verified as **this match's starter**. These candidate percentages were **not** used as confirmed-starter inputs. Scratch list/injury and exact unit changes not confirmed. Do not infer a healthy full roster.
- No 20-completed-fixture current-season window: both had 15. No opponent-adjusted full-strength method was executed. Travel distance and numerical lineup impact not measured.

## Transparent quantitative scenario, not independently calibrated

Reconstruct **season** GF/GA, **last 10**, **last five**, with fixed disclosed weights 50%, 30%, 20% respectively. These periods overlap and so weights are analyst choices, *not* fitted coefficients or independent evidence. No off-league parameter or player-effect value is introduced. Rochester weighted GF 3.13; GA 2.79. Syracuse weighted GF 2.5933; GA 3.2833. A simple equal team attack/opponent defence mean gives expected **Rochester 3.2065** and **Syracuse 2.6917** goals, regulation combined **5.8982** and Rochester advantage **0.5148**. No additional numeric home, roster, rest or goalie effect is assigned.

Compute independent regulation Poisson grids P(R=r,S=s) = Pois(r;3.2065) Pois(s;2.6915) for integers r,s = 0…34, residual tail negligible; use 50/50 neutral share for regulation ties through overtime/shootout since neither side's conditional OT strength is supported. Outputs: Rochester regulation win **0.4998**, Syracuse regulation win **0.3354**, tied after 60 minutes **0.1648**, Rochester full-game win **0.5822**, Syracuse **0.4178**. Full-game total Over 5.5 **0.5378**, Under **0.4622**. On the model's one-extra-goal-for-tie convention, a regulation tie has an even total and gains only one goal, so OT/SO does not move any tied match across the 5.5 threshold. Report these as **uncalibrated analytical estimates**, not a trained league model, executed Monte Carlo sample, or measured precision.

**Sensitivity:** ±0.35 expected goals on either side (one axis at a time) changes Rochester win estimate to approximately **52.6–64.0%**, and Over 5.5 to **47.9–59.3%**. This is a scenario range, not a confidence interval; goalie and venue/rotation uncertainty could be larger. High-impact missing goalie confirmation makes all lines `UNMEASURED`; no qualified rank was issued. There is no frozen league-only baseline for this request (`baseline_p` empty and `baseline_id=UNAVAILABLE:NO_FROZEN_SPORTING_BASELINE`), so independent skill comparison cannot rely on a league baseline. The two handicap labels share an event and are mirror outcomes and must not be treated as separate independent trials.

## Exact frozen ONECHAT_V1 block

<!-- BEGIN ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0005 -->
format: ONECHAT_V1
card_key: 20261118DA6D9F6251746B979F5895FA-G0005
sport: Ice Hockey
competition: AHL
home: Syracuse Crunch
away: Rochester Americans
scheduled_start: 2026-11-19T11:00:00+11:00
request_at: 2026-11-19T10:44:00+11:00
research_start_at: 2026-11-19T10:51:00+11:00
research_end_at: 2026-11-19T10:55:18+11:00
not_started_source: https://www.hockey.com/ahl/teams/rochester-americans/schedule
not_started_observed_at: 2026-11-19T10:51:08+11:00
outcome_exposure: NONE

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,HANDICAP,AWAY,-0.5,0.5822,,0.5150,UNMEASURED,https://theahl.com/stats/schedule/323/94
L1,HANDICAP,HOME,0.5,0.4178,,-0.5150,UNMEASURED,https://theahl.com/stats/schedule/323/94
L2,HANDICAP,HOME,-0.5,0.4178,,-0.5150,UNMEASURED,https://theahl.com/stats/schedule/323/94
L2,HANDICAP,AWAY,0.5,0.5822,,0.5150,UNMEASURED,https://theahl.com/stats/schedule/323/94
L3,TOTAL,OVER,5.5,0.5378,,5.8980,UNMEASURED,https://theahl.com/stats/schedule/323/94
L3,TOTAL,UNDER,5.5,0.4622,,5.8980,UNMEASURED,https://theahl.com/stats/schedule/323/94

FACTS
side,field,value,source,observed_at
HOME,season_games,15,https://www.hockey.com/ahl/teams/syracuse-crunch/schedule,2026-11-19T10:52:29+11:00
HOME,season_score_for_pg,2.6667,https://www.hockey.com/ahl/teams/syracuse-crunch/schedule,2026-11-19T10:52:29+11:00
HOME,season_score_against_pg,3.2667,https://www.hockey.com/ahl/teams/syracuse-crunch/schedule,2026-11-19T10:52:29+11:00
HOME,last10_score_for_pg,3.0000,https://www.hockey.com/ahl/teams/syracuse-crunch/schedule,2026-11-19T10:52:29+11:00
HOME,last10_score_against_pg,3.1000,https://www.hockey.com/ahl/teams/syracuse-crunch/schedule,2026-11-19T10:52:29+11:00
HOME,rest_days,3,https://www.hockey.com/ahl/teams/syracuse-crunch/schedule,2026-11-19T10:52:29+11:00
HOME,back_to_back,NO,https://www.hockey.com/ahl/teams/syracuse-crunch/schedule,2026-11-19T10:52:29+11:00
HOME,starting_goalie_confirmed,MISSING,Neither official team preview nor checked fixture has a verified announced starter at cutoff,
HOME,starting_goalie_save_pct,MISSING,Starter not confirmed; a candidate goalie career or season percentage is not a confirmed-starter input,
HOME,key_absences,MISSING,No fully verified game-day active and scratch list for this exact fixture,
HOME,venue,Upstate Medical University Arena Syracuse NY,https://www.amerks.com/news/detail/game-preview-amerks-begin-three-game-roadie-in-syracuse,2026-11-19T10:52:29+11:00
HOME,travel_km,MISSING,No verified measured traveled distance for this game,
HOME,opponent_strength,MISSING,No fully audited opponent-adjusted team strength in pregame record,
HOME,opponent_strength_method,MISSING,No admitted opponent-strength method run,
HOME,availability_effect,MISSING,No measured with-versus-without goalie or skater adjustment for this match,
HOME,adjustment_basis,MISSING,No independently measured numeric roster travel or home adjustment applied,
HOME,last20_score_for_pg,MISSING,Only 15 current-season fixtures completed; cross-season 20-game window not certified,
HOME,last20_score_against_pg,MISSING,Only 15 current-season fixtures completed; cross-season 20-game window not certified,
AWAY,season_games,15,https://www.hockey.com/ahl/teams/rochester-americans/schedule,2026-11-19T10:52:29+11:00
AWAY,season_score_for_pg,3.2000,https://www.hockey.com/ahl/teams/rochester-americans/schedule,2026-11-19T10:52:29+11:00
AWAY,season_score_against_pg,2.6000,https://www.hockey.com/ahl/teams/rochester-americans/schedule,2026-11-19T10:52:29+11:00
AWAY,last10_score_for_pg,3.1000,https://www.hockey.com/ahl/teams/rochester-americans/schedule,2026-11-19T10:52:29+11:00
AWAY,last10_score_against_pg,3.1000,https://www.hockey.com/ahl/teams/rochester-americans/schedule,2026-11-19T10:52:29+11:00
AWAY,rest_days,3,https://www.hockey.com/ahl/teams/rochester-americans/schedule,2026-11-19T10:52:29+11:00
AWAY,back_to_back,NO,https://www.hockey.com/ahl/teams/rochester-americans/schedule,2026-11-19T10:52:29+11:00
AWAY,starting_goalie_confirmed,MISSING,Neither official team preview nor checked fixture has a verified announced starter at cutoff,
AWAY,starting_goalie_save_pct,MISSING,Starter not confirmed; a candidate goalie career or season percentage is not a confirmed-starter input,
AWAY,key_absences,MISSING,No fully verified game-day active and scratch list for this exact fixture,
AWAY,venue,Upstate Medical University Arena Syracuse NY,https://www.amerks.com/news/detail/game-preview-amerks-begin-three-game-roadie-in-syracuse,2026-11-19T10:52:29+11:00
AWAY,travel_km,MISSING,No verified measured traveled distance for this game,
AWAY,opponent_strength,MISSING,No fully audited opponent-adjusted team strength in pregame record,
AWAY,opponent_strength_method,MISSING,No admitted opponent-strength method run,
AWAY,availability_effect,MISSING,No measured with-versus-without goalie or skater adjustment for this match,
AWAY,adjustment_basis,MISSING,No independently measured numeric roster travel or home adjustment applied,
AWAY,last20_score_for_pg,MISSING,Only 15 current-season fixtures completed; cross-season 20-game window not certified,
AWAY,last20_score_against_pg,MISSING,Only 15 current-season fixtures completed; cross-season 20-game window not certified,
<!-- END ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0005 -->
<!-- END CANONICAL RESEARCH P-689 -->

<!-- BEGIN RESEARCH ADDENDUM P-689 2026-11-22-settlement-revision-1 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_11.md`, P-689. Source: `research/verification/mini_import_P-686_P-696_2026-11-22-1/SETTLEMENT.md` (P-689); exact settlement block follows.

<!-- BEGIN SETTLEMENT P-689 LOCAL-20261118DA6D9F6251746B979F5895FA-G0005 revision-1 -->
### P-689 · Ice Hockey/AHL 2026-27 (game 1029340) — Rochester Americans @ Syracuse Crunch · 2026-11-18 ET · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0005` · `AHL:1029340` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-18T23:57:40Z`; assessment `SEALED_PRE_START_SERVER`; actual first play `2026-11-18T19:05:00-05:00`).
- **Verified final (A):** **Rochester Americans 2-1 Syracuse Crunch (Regulation)** · Linescore: `ROC 0-1-1=2; SYR 0-0-1=1 (sum check: 0+1+1=2, 0+0+1=1; shots ROC 20, SYR 24; 3 PPG total)`.
- **Permitted source & capture:** `https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameSummary&game_id=1029340&key=50c2cd9b5e18e390&site_id=1&client_code=ahl&lang=en` · capture `2026-11-22/G0005_ahl_api.json` (SHA-256 `a6f3993e2999c3f45d7af74104235746df02e3b6340016db19c878b904c51f19`). Corroboration: https://theahl.com/stats/game-center/1029340 (captured in G0005_ahl_web.html) + amerks.com / syracusecrunch.com.
- **Card-mean Brier / d:** `0.2128` / `+0.0372`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | AWAY | -0.5 | 0.5822 | 0.5150 | UNMEASURED | **WIN** | 0.1746 |
| L1 | NOT_RANKED | HANDICAP | HOME | 0.5 | 0.4178 | -0.5150 | UNMEASURED | **LOSS** | 0.1746 |
| L2 | NOT_RANKED | HANDICAP | HOME | -0.5 | 0.4178 | -0.5150 | UNMEASURED | **LOSS** | 0.1746 |
| L2 | R2 | HANDICAP | AWAY | 0.5 | 0.5822 | 0.5150 | UNMEASURED | **WIN** | 0.1746 |
| L3 | R3 | TOTAL | OVER | 5.5 | 0.5378 | 5.8980 | UNMEASURED | **LOSS** | 0.2892 |
| L3 | NOT_RANKED | TOTAL | UNDER | 5.5 | 0.4622 | 5.8980 | UNMEASURED | **WIN** | 0.2892 |

**R1–R12 retrospective:** Official HockeyTech JSON verifies puck drop 7:05 pm EST (00:05Z), 7m20s AFTER GitHub server seal (23:57:40Z) — first SEALED_PRE_START_SERVER qualifying game in Track P. Rochester won 2-1 in regulation (both L1 -0.5 and L2 +0.5 won, though L1 and L2 are duplicate representations of the same 2-way OT/SO-inclusive side). Low-event game (44 combined shots, scoreless P1) finished 3 goals vs 5.5. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-004 · P-689 · Over 5.5 (TOP_TOTAL) — Verdict: `VARIANCE` · Class: `VARIANCE`**
1. **Contract & trigger:** Over 5.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Rochester Americans 2-1 Syracuse Crunch (Regulation) (ROC 0-1-1=2; SYR 0-0-1=1 (sum check: 0+1+1=2, 0+0+1=1; shots ROC 20, SYR 24; 3 PPG total)).
4. **Outcome in frozen distribution & what decided the game:** Card projected 5.90 goals (p=0.5378, inside H-NODIR band). Game had 44 combined shots and 9 power plays (3 PPG) but zero even-strength goals; 3 total goals is routine Poisson variance (approx 16% tail under lambda=5.9).
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_PRE_START_SERVER`, exposure `NONE`.
6. **Plain verdict & process lesson:** `VARIANCE` (`VARIANCE`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.
<!-- END SETTLEMENT P-689 LOCAL-20261118DA6D9F6251746B979F5895FA-G0005 revision-1 -->
<!-- END RESEARCH ADDENDUM P-689 2026-11-22-settlement-revision-1 -->

<!-- BEGIN CANONICAL RESEARCH P-690 -->
## P-690 — Basketball/NBA Regular Season (game 0022600259) — Houston Rockets @ Indiana Pacers · 2026-11-18 ET

Canonical retention by prompt-4 import `2026-11-22T06:40:00+00:00`. Scheduled start `2026-11-19T11:00:00+11:00`. Original `20261118DA6D9F6251746B979F5895FA-G0006` (12163 B, SHA-256 `e385306fe7eadb78036e31c0b760117a5f5a5fda52584fb29d856064ca02a359`, source `a96ee8e8e782527b568b017b7b21e8500e1f87e0`, seal `SEALED` at `2026-11-19T00:06:05Z`). Original card follows verbatim; no forecast reissued; Track P scored separately via `ml one-chat score`.

# Original pre-start research card — LOCAL-20261118DA6D9F6251746B979F5895FA-G0006

**Research custody:** REGISTERED request G0006 under forecast-seals after GitHub Actions run `44425278135` green; registration drop `3696fefd994035cd4d626524f4f88c534615bd19`. Same user game was submitted twice in immediate succession, and the later message with `[$github]` is the frozen original request. SPORTS_ONLY / MARKET_BLIND. Main read-only `cb97bbc2a9f882e7f8a093648b6137315951da8b`, governing ONECHAT_V1 / DROP-SEAL-v1. This is an analyst numeric card **not a fitted or independently validated prediction model**. No price source or third-party tip was used. Sealing is not claimed in this original.

## Original request (exact frozen UTF-8 text)

```text
Upcoming Basketball Game: HOU Rockets @ IND Pacers, NBA,\
Estimated Game Time Start: 19 November 2026, 11:10 AM AEDT (can be delayed so continue the process as normal)\
\
Rockets -8.5\
Packers +8.5\
Combined Total Points: Over/Under 224.5 Points [$github](app://connector_76869538009648d5b282a4bb21c3d157)
```

## A1 — Identity and timing

- Official NBA matchup `NBA:0022600259`, Houston Rockets (away) @ Indiana Pacers (home), Gainbridge Fieldhouse Indianapolis. Official schedule **November 18 2026 7:00 PM EST / November 19 2026 11:00 AM AEDT**: https://www.nba.com/game/HOU-vs-IND-0022600259. The owner's estimated 11:10 AM differs from the official scheduled time by 10 minutes; the owner allows delays.
- Request receipt is approximate minute level and not independently timestamped to the second. The registration action succeeded and original REQUEST.txt/EVENT.csv/CONTRACTS.csv were fetched from `forecast-seals` before research.
- Research started 2026-11-19 11:00:16 AEDT. The official NBA fixture page was checked at 11:00:45 AEDT and returned a pre-game schedule with no live result or game outcome rendered in the accessible page. That absence is not independent proof of actual first play. Source https://www.nba.com/game/HOU-vs-IND-0022600259.
- The research concluded 2026-11-19 11:02:50 AEDT. Official actual first-play time and GitHub server push activity are **NOT VERIFIED**, so prospective eligibility is explicitly pending. No target-game result or live score was viewed.

## A2 — Exact owner's requested contracts

- L1: HOU -8.5 and IND +8.5 (owner typo `Packers` is retained verbatim in request excerpt). Full game including overtime.
- L2: Combined total OVER and UNDER 224.5 points, full game including overtime.
- No added winner contract. Each side of each requested line retained. No observed market price was used.

## A3 — Dated sporting evidence at research cutoff

The NBA official team schedules https://www.nba.com/team/1610612745/schedule and https://www.nba.com/team/1610612754/schedule gave:
- Houston 11-4, 15 completed regular-season games. Scored **117.80** and allowed **109.53** per game; last five **121.40 / 114.60**, last ten **115.20 / 109.90**. Latest five: Denver 110-100, Warriors 115-108, Jazz 125-118, Wizards 147-119, Heat 110-128. The last ten are fully represented in the schedule; postseason and preseason results excluded.
- Indiana 5-9, 14 completed. Scored **112.07** and allowed **114.50** per game; last five **113.60 / 115.00**, last ten **110.30 / 114.30**. Latest five: Denver 102-114, Dallas 122-125, Washington 114-101, New York 106-104, Philadelphia 124-131.
- Last current-season 20-game windows do not exist for either team. Neither an opponent-adjusted ORtg/DRtg model nor verified complete lineup minutes were fitted. No numeric home adjustment was guessed.
- Houston last played Monday November 16 (one full calendar day off before Wednesday game), after a Sunday/Monday consecutive-game sequence, with Washington and Miami away trips. Indiana last played Sunday Nov 15 (two full days off); it is home for this game. Both are not on an immediate back-to-back.
- The NBA's 18 November 6:00 PM ET official injury sheet https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-18_06_00PM.pdf lists HOU: **Clint Capela OUT**, Amen Thompson **QUESTIONABLE** (left knee), Quadir Copeland and Julian Phillips **OUT** (G League); IND: **Tyrese Haliburton OUT**, **Andrew Nembhard OUT**, **Johnny Furphy OUT**, **Ben Sheppard OUT**, T.J. McConnell **AVAILABLE**. These statuses are source-backed but no independently measured with/without points impact is available; therefore no invented injury adjustment.
- Official Indiana preview https://www.nba.com/pacers/news/preview-pacers-rockets-261118 gives a *probable* five, not certified starters. Starters are not independently confirmed. Match context includes road-trip load for Houston and Indiana's home venue.
- H2H prior Feb 2 2026: HOU 118 IND 114. This is not assigned quantitative weight because its previous roster regime need not match.

## A4 — Transparent joint-score approximation

For each team's for/against PPG, compute a rolling blend: `0.60×last-five + 0.25×last-ten + 0.15×current-season`, overlapping windows and explicitly **analyst-chosen, not statistically fitted** weights. Then expected visitor score is midpoint of visitor blended points for and home blended points conceded; expected home score is midpoint of home blended points for and visitor blended points conceded.

- HOU weighted scored 119.310; conceded 112.665; IND weighted scored 112.546; conceded 114.750.
- Forecast Houston **117.030**, Indiana **112.605**, combined **229.635**, margin Houston **+4.425**.
- Uncalibrated Normal approximation for full-game margin and total: margin SD **15.43** points and total SD **19.90**, chosen as conservative NBA competition raw width references in `PARAMETERS.md` `COMPETITION_PARAMETERS.csv` from governing main. The reference development row does not constitute an independently certified user model. The actual joint score covariance and overtime mass were not separately fitted, so these family probabilities are marginal estimates from one coherent pair of central scores, not a trained multivariate simulator.
- `P(HOU -8.5) = 1 - Φ((8.5 - 4.4246)/15.43) = 0.3958`; reciprocal IND +8.5 **0.6042**. `P(OVER 224.5) = 1 - Φ((224.5 - 229.6354)/19.90) = 0.6018`; Under **0.3982**.
- Sensitivity: unresolved Amen Thompson participation, both clubs' confirmed starting fives, Indiana's confirmed absences, travel and matchup-specific pace could each change the projection. No numeric adjustment without a measured effect. The nearest plausible alternative is IND +8.5, but the central estimate of **60.4%** is below the Rank-1 gate of 62%; total Over **60.2%** is also below. No qualifying Rank-1 card was issued. Absence basis is UNMEASURED on all four sides; no calibration, confidence bounds, 100k Monte Carlo, or ML/RL training is claimed.
- A frozen independent sporting baseline was unavailable and not created post-hoc; `baseline_p` blank in original registered contracts. This forecast cannot independently demonstrate predictive skill without admissible prospective settlement and baseline comparison.
- Result/first-play evidence needed later: official NBA game `https://www.nba.com/game/HOU-vs-IND-0022600259`, retained capture and actual first play. Do not settle during research.

## A5 — Exact ONECHAT_V1 block

<!-- BEGIN ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0006 -->
format: ONECHAT_V1
card_key: 20261118DA6D9F6251746B979F5895FA-G0006
sport: Basketball
competition: NBA
home: Indiana Pacers
away: Houston Rockets
scheduled_start: 2026-11-19T11:00:00+11:00
request_at: 2026-11-19T10:58:00+11:00
research_start_at: 2026-11-19T11:00:16+11:00
research_end_at: 2026-11-19T11:02:50+11:00
not_started_source: https://www.nba.com/game/HOU-vs-IND-0022600259
not_started_observed_at: 2026-11-19T11:00:45+11:00
outcome_exposure: NONE

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,HANDICAP,AWAY,-8.5,0.3958,,4.4246,UNMEASURED,https://www.nba.com/game/HOU-vs-IND-0022600259
L1,HANDICAP,HOME,8.5,0.6042,,-4.4246,UNMEASURED,https://www.nba.com/game/HOU-vs-IND-0022600259
L2,TOTAL,OVER,224.5,0.6018,,229.6354,UNMEASURED,https://www.nba.com/game/HOU-vs-IND-0022600259
L2,TOTAL,UNDER,224.5,0.3982,,229.6354,UNMEASURED,https://www.nba.com/game/HOU-vs-IND-0022600259

FACTS
side,field,value,source,observed_at
HOME,season_games,14,https://www.nba.com/team/1610612754/schedule,2026-11-19T11:01:07+11:00
HOME,season_score_for_pg,112.0714,https://www.nba.com/team/1610612754/schedule,2026-11-19T11:01:07+11:00
HOME,season_score_against_pg,114.5000,https://www.nba.com/team/1610612754/schedule,2026-11-19T11:01:07+11:00
HOME,last5_score_for_pg,113.6000,https://www.nba.com/team/1610612754/schedule,2026-11-19T11:01:07+11:00
HOME,last5_score_against_pg,115.0000,https://www.nba.com/team/1610612754/schedule,2026-11-19T11:01:07+11:00
HOME,last10_score_for_pg,110.3000,https://www.nba.com/team/1610612754/schedule,2026-11-19T11:01:07+11:00
HOME,last10_score_against_pg,114.3000,https://www.nba.com/team/1610612754/schedule,2026-11-19T11:01:07+11:00
HOME,rest_days,2,https://www.nba.com/team/1610612754/schedule,2026-11-19T11:01:07+11:00
HOME,back_to_back,NO,https://www.nba.com/team/1610612754/schedule,2026-11-19T11:01:07+11:00
HOME,key_absences,Haliburton out; Nembhard out; Furphy out; Sheppard out,https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-18_06_00PM.pdf,2026-11-19T11:02:10+11:00
HOME,lineup_confirmed,MISSING,Official game-day starting five not independently confirmed at freeze,
HOME,venue,Gainbridge Fieldhouse Indianapolis,https://www.nba.com/team/1610612754/schedule,2026-11-19T11:01:07+11:00
HOME,travel_km,MISSING,No measured verified route distance available,
HOME,opponent_strength,MISSING,No reproducible opponent-adjusted numerical series evaluated,
HOME,opponent_strength_method,MISSING,No audited opponent adjustment fitted,
HOME,availability_effect,MISSING,Missing measured player on-off effect for the confirmed status mix,
HOME,adjustment_basis,MISSING,No measured numeric injury rest travel or home adjustment applied,
HOME,last20_score_for_pg,MISSING,Only current season 14 or 15 games completed,
HOME,last20_score_against_pg,MISSING,Only current season 14 or 15 games completed,
AWAY,season_games,15,https://www.nba.com/team/1610612745/schedule,2026-11-19T11:01:07+11:00
AWAY,season_score_for_pg,117.8000,https://www.nba.com/team/1610612745/schedule,2026-11-19T11:01:07+11:00
AWAY,season_score_against_pg,109.5333,https://www.nba.com/team/1610612745/schedule,2026-11-19T11:01:07+11:00
AWAY,last5_score_for_pg,121.4000,https://www.nba.com/team/1610612745/schedule,2026-11-19T11:01:07+11:00
AWAY,last5_score_against_pg,114.6000,https://www.nba.com/team/1610612745/schedule,2026-11-19T11:01:07+11:00
AWAY,last10_score_for_pg,115.2000,https://www.nba.com/team/1610612745/schedule,2026-11-19T11:01:07+11:00
AWAY,last10_score_against_pg,109.9000,https://www.nba.com/team/1610612745/schedule,2026-11-19T11:01:07+11:00
AWAY,rest_days,1,https://www.nba.com/team/1610612745/schedule,2026-11-19T11:01:07+11:00
AWAY,back_to_back,NO,https://www.nba.com/team/1610612745/schedule,2026-11-19T11:01:07+11:00
AWAY,key_absences,Capela out; Thompson questionable; Copeland out; Phillips out,https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-18_06_00PM.pdf,2026-11-19T11:02:10+11:00
AWAY,lineup_confirmed,MISSING,Official game-day starting five not independently confirmed at freeze,
AWAY,venue,Gainbridge Fieldhouse Indianapolis,https://www.nba.com/team/1610612745/schedule,2026-11-19T11:01:07+11:00
AWAY,travel_km,MISSING,No measured verified route distance available,
AWAY,opponent_strength,MISSING,No reproducible opponent-adjusted numerical series evaluated,
AWAY,opponent_strength_method,MISSING,No audited opponent adjustment fitted,
AWAY,availability_effect,MISSING,Missing measured player on-off effect for the confirmed status mix,
AWAY,adjustment_basis,MISSING,No measured numeric injury rest travel or home adjustment applied,
AWAY,last20_score_for_pg,MISSING,Only current season 14 or 15 games completed,
AWAY,last20_score_against_pg,MISSING,Only current season 14 or 15 games completed,
<!-- END ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0006 -->
<!-- END CANONICAL RESEARCH P-690 -->

<!-- BEGIN RESEARCH ADDENDUM P-690 2026-11-22-settlement-revision-1 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_11.md`, P-690. Source: `research/verification/mini_import_P-686_P-696_2026-11-22-1/SETTLEMENT.md` (P-690); exact settlement block follows.

<!-- BEGIN SETTLEMENT P-690 LOCAL-20261118DA6D9F6251746B979F5895FA-G0006 revision-1 -->
### P-690 · Basketball/NBA Regular Season (game 0022600259) — Houston Rockets @ Indiana Pacers · 2026-11-18 ET · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0006` · `NBA:0022600259` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-19T00:06:05Z`; assessment `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (B):** **Houston Rockets 119-104 Indiana Pacers** · Linescore: `HOU 39-23-31-26=119; IND 28-18-30-28=104 (sum check: 39+23+31+26=119, 28+18+30+28=104)`.
- **Permitted source & capture:** `https://www.foxsports.com/nba/houston-rockets-vs-indiana-pacers-nov-18-2026-game-boxscore-106744` · capture `2026-11-22/G0006_fox_box.html` (SHA-256 `9912841ae4cfdef255429da28a6958457165ab404b604ba832f0aec611edad18`). Corroboration: https://basketball.realgm.com/nba/scores/2026-11-18 (web search corroboration; script blocked).
- **Card-mean Brier / d:** `0.3636` / `-0.1136`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | NOT_RANKED | HANDICAP | AWAY | -8.5 | 0.3958 | 4.4246 | UNMEASURED | **WIN** | 0.3651 |
| L1 | R1 | HANDICAP | HOME | 8.5 | 0.6042 | -4.4246 | UNMEASURED | **LOSS** | 0.3651 |
| L2 | R2 | TOTAL | OVER | 224.5 | 0.6018 | 229.6354 | UNMEASURED | **LOSS** | 0.3622 |
| L2 | NOT_RANKED | TOTAL | UNDER | 224.5 | 0.3982 | 229.6354 | UNMEASURED | **WIN** | 0.3622 |

**R1–R12 retrospective:** Houston jumped to a 62-46 halftime lead (Kevin Durant 21, Reed Sheppard 20 on 6-7 3PT, Jabari Smith Jr. 17) against an Indiana backcourt missing Tyrese Haliburton and Andrew Nembhard. Both Pacers +8.5 (p=0.6042) and Over 224.5 (p=0.6018, actual 223) lost. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-005 · P-690 · Packers +8.5 (TOP_SIDE_AND_RANK_1) — Verdict: `ERROR` · Class: `UNFITTED_ANALYST_ADJUSTMENT` (alias `UNMEASURED_AVAILABILITY_PRICED`)**
1. **Contract & trigger:** Packers +8.5 (TOP_SIDE_AND_RANK_1).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Houston Rockets 119-104 Indiana Pacers (HOU 39-23-31-26=119; IND 28-18-30-28=104 (sum check: 39+23+31+26=119, 28+18+30+28=104)).
4. **Outcome in frozen distribution & what decided the game:** Indiana was missing both starting guards (Haliburton, Nembhard); card marked availability_basis=UNMEASURED yet priced Pacers +8.5 at 0.6042 (Rank 1) with an expected margin of -4.42 instead of leaving the line UNPRICED per AUDIT-v1. Houston won by 15.
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `ERROR` (`UNFITTED_ANALYST_ADJUSTMENT` / `UNMEASURED_AVAILABILITY_PRICED`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.

**DLR-2026-11-22-006 · P-690 · Over 224.5 (TOP_TOTAL) — Verdict: `VARIANCE` · Class: `VARIANCE`**
1. **Contract & trigger:** Over 224.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Houston Rockets 119-104 Indiana Pacers (HOU 39-23-31-26=119; IND 28-18-30-28=104 (sum check: 39+23+31+26=119, 28+18+30+28=104)).
4. **Outcome in frozen distribution & what decided the game:** Actual total 223 missed 224.5 by 1.5 points despite a 67-point Q1; Q2 slowed to 41 combined points (23-18). Within 0.4 SD of card's 229.6 centre.
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `VARIANCE` (`VARIANCE`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.

**Joint side + total loss note (P-690):** Both top side and top total lost on this card (card-mean Brier `0.3636`, `d = -0.1136`). Shared root causes: unmeasured availability / opponent-strength overreach paired with unadjusted total Over bias.
<!-- END SETTLEMENT P-690 LOCAL-20261118DA6D9F6251746B979F5895FA-G0006 revision-1 -->
<!-- END RESEARCH ADDENDUM P-690 2026-11-22-settlement-revision-1 -->

<!-- BEGIN CANONICAL RESEARCH P-691 -->
## P-691 — Basketball/NBA Regular Season (game 0022600265) — Atlanta Hawks @ Oklahoma City Thunder · 2026-11-18 CT

Canonical retention by prompt-4 import `2026-11-22T06:40:00+00:00`. Scheduled start `2026-11-19T12:00:00+11:00`. Original `20261118DA6D9F6251746B979F5895FA-G0008` (11706 B, SHA-256 `89730b0f5699dc0274b9102f0674365098c1186fc0b15c2ffe0e65764016440b`, source `d08928dc88d631dca68abd26f30bc467b1952843`, seal `SEALED` at `2026-11-19T00:55:08Z`). Original card follows verbatim; no forecast reissued; Track P scored separately via `ml one-chat score`.

# Pregame research card — LOCAL-20261118DA6D9F6251746B979F5895FA-G0008 — Atlanta Hawks @ Oklahoma City Thunder

**Original prediction preparation:** `2026-11-19T11:51:37+11:00`; research began only after GitHub confirmed and independently published the original request. This original card does **not** itself claim to be GitHub-sealed. Governance from `main@cb97bbc2a9f882e7f8a093648b6137315951da8b`, MDS-2026.11.18-v29.1 / CR-2026.11.18-R2, ONECHAT_V1 and DROP-SEAL-v1. MARKET_BLIND / SPORTS_ONLY. No price data or external tip is a modelling input.

## Original owner request — exact UTF-8 text

```text
Upcoming Basketball Game: ATL Hawks @ OKC Thunder, NBA,\
Estimated Game Time Start: 19 November 2026, 12:10 PM AEDT (can be delayed so continue the process as normal)\
\
Hawks +6.5\
Thunder -6.5\
Combined Total Points: Over/Under 228.5 Points  [$github](app://connector_76869538009648d5b282a4bb21c3d157)
```

## A1 — Fixture, time and evidence custody

- Official fixture is NBA:0022600265, Atlanta Hawks (away) at Oklahoma City Thunder (home), Paycom Center, Oklahoma City, source https://www.nba.com/game/atl-vs-okc-0022600265.
- The official scheduled start is Nov 18 2026 at 8:00 PM EST = **Nov 19 2026 at 12:00 PM AEDT**. This is 10 minutes before the user-estimated 12:10 PM; no actual first-play time independently established.
- Registered request G0008 at GitHub `card-drops` commit `ab1625ca1d830392f2367c6780d97108ff76c127`; `seal-drops` registration Actions run `44432023241` returned green. All three files were independently read from `forecast-seals` before sporting research.
- Request receipt clock is minute-level approximate; request_at 11:47 AM AEDT is not an independently retrieved user message event timestamp.
- Research window 11:49:54–11:51:37 AM AEDT. Official NBA game page inspected at 11:50:44 AM AEDT and displayed upcoming schedule without a visible live target-game score; the visible information did not expose the eventual game outcome. Actual first-play and server push times remain **UNVERIFIED** and must be proven later for prospective acceptance.
- No target-game live or final score was used for data inputs.

## A2 — Requested exact contracts

- L1: Atlanta Hawks +6.5 (AWAY) versus Oklahoma City Thunder −6.5 (HOME).
- L2: combined full-game OVER/UNDER 228.5 points.
- All settlements include overtime per current basketball convention. Both sides of each line are in PICKS; no additional market created. Baseline unavailable on the registered contracts (`UNAVAILABLE:NO_FROZEN_SPORTING_BASELINE`), with no price input.

## A3 — Verified sporting evidence as of pregame cutoff

- Official 2026–27 completed NBA results for both teams, excluding preseason: Atlanta **8–6** in 14 games; scored 117.79 and allowed 116.07 points/game, last five 121.40/121.60, last ten 116.50/117.80. Source https://www.nba.com/team/1610612737/schedule.
- Oklahoma City **9–5** in 14 games; scored 112.14 and allowed 107.07 points/game; last five 112.40/106.40, last ten 112.50/109.60. Source https://www.nba.com/team/1610612760/thunder/schedule.
- Latest Atlanta five chronologically: Nov 6 Washington W139–132, Nov 7 Brooklyn W124–121, Nov 9 Lakers L114–124, Nov 13 Bulls L117–125, Nov 15 Milwaukee W113–106. Latest Oklahoma City five: Nov 7 Wizards W114–75, Nov 10 Portland L103–123, Nov 11 Portland L108–118, Nov 13 Clippers L112–113, Nov 15 Sacramento W125–103. Both last played November 15 and had two full calendar rest days (Nov 16–17); neither is on an immediate back-to-back. Both have fewer than 20 completed current-season games.
- Official NBA 6:45 PM ET injury report https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-18_06_45PM.pdf, page 5: Atlanta CJ McCollum, Kingston Flemings, Mouhamed Gueye, Jock Landale, Asa Newell, Henri Veesaar, Rafael Castro **OUT**. Oklahoma City Chet Holmgren, Jalen Williams, Cason Wallace, Thomas Sorber **OUT**; Jaylin Williams **AVAILABLE**. These are documented states only. No measured player-points effects, confirmed lineups, pace/efficiency opponent adjustments, verified travel distance or starting-minute rotations are available at the freeze.
- Context: Atlanta arrives from a road win at Milwaukee; Oklahoma City returns from a road win at Sacramento. The former Thunder players Luguentz Dort and Aaron Wiggins now play for Atlanta, offering a familiarity storyline, not an input coefficient. Team preview: https://www.nba.com/news/atlanta-hawks-dort-wiggins-face-oklahoma-city-thunder .
- Opponent-adjusted offensive/defensive ratings, current starting fives and H2H regime adjustments were not sufficiently verified to assign numerical effect sizes; these are explicitly missing rather than invented.

## A4 — Transparent statistical approximation (not a fitted predictive model)

For each team and for/against PPG, compute overlapping-window recency blend `0.60×last-five + 0.25×last-ten + 0.15×season`; **analyst-selected weights**, not learned or independently validated. Estimate visitor expected points as mean(visitor blended scored, home blended allowed); home expected points as mean(home blended scored, visitor blended allowed). This uses completed pregame scores only.

- Atlanta weighted for/against 119.6329/119.8207; Oklahoma City 112.3864/107.3007.
- Joint score centre **Atlanta 113.467 – Oklahoma City 116.104**; combined **229.570**, margin OKC **+2.637**.
- Normal-margin SD 15.43 points and Normal-total SD 19.90 points retained from the NBA competition reference widths in governing `PARAMETERS.md` / `research/competition_parameters/COMPETITION_PARAMETERS.csv`. They are general development-data widths, **not** model-certified uncertainty intervals for this particular AHL/NBA game. No Monte Carlo or joint covariance estimation was run.
- `P(OKC −6.5)=1−Φ((6.5−2.6368)/15.43) = 0.4012`; `P(ATL +6.5)=0.5988`. `P(Over 228.5)=1−Φ((228.5−229.5704)/19.90)=0.5214`; `P(Under)=0.4786`. The two sides of each line sum to 1.
- Primary failure route for ATL +6.5: Shai Gilgeous-Alexander-led Oklahoma City separation despite injuries, or significantly slower Atlanta production with CJ McCollum absent. Principal Over failure route: OKC scoring inefficiency/lineup absences, tempo slowdown and missing interior scorers. Major injuries on both sides have **UNMEASURED** effects, so there is no supported numerical adjustment; the line can swing materially.
- Neither top line clears the 62% Rank-1 criterion; 58% Rank-2 threshold is a gate only and doesn't overcome lack of calibration and lineup confirmation. All probabilities are **uncalibrated analyst approximations** and not independently admitted predictive skill.

## A5 — Frozen ONECHAT_V1

<!-- BEGIN ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0008 -->
format: ONECHAT_V1
card_key: 20261118DA6D9F6251746B979F5895FA-G0008
sport: Basketball
competition: NBA
home: Oklahoma City Thunder
away: Atlanta Hawks
scheduled_start: 2026-11-19T12:00:00+11:00
request_at: 2026-11-19T11:47:00+11:00
research_start_at: 2026-11-19T11:49:54+11:00
research_end_at: 2026-11-19T11:51:37+11:00
not_started_source: https://www.nba.com/game/atl-vs-okc-0022600265
not_started_observed_at: 2026-11-19T11:50:44+11:00
outcome_exposure: NONE

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,HANDICAP,AWAY,6.5,0.5988,,-2.6368,UNMEASURED,https://www.nba.com/game/atl-vs-okc-0022600265
L1,HANDICAP,HOME,-6.5,0.4012,,2.6368,UNMEASURED,https://www.nba.com/game/atl-vs-okc-0022600265
L2,TOTAL,OVER,228.5,0.5214,,229.5704,UNMEASURED,https://www.nba.com/game/atl-vs-okc-0022600265
L2,TOTAL,UNDER,228.5,0.4786,,229.5704,UNMEASURED,https://www.nba.com/game/atl-vs-okc-0022600265

FACTS
side,field,value,source,observed_at
HOME,season_games,14,https://www.nba.com/team/1610612760/thunder/schedule,2026-11-19T11:50:44+11:00
HOME,season_score_for_pg,112.1429,https://www.nba.com/team/1610612760/thunder/schedule,2026-11-19T11:50:44+11:00
HOME,season_score_against_pg,107.0714,https://www.nba.com/team/1610612760/thunder/schedule,2026-11-19T11:50:44+11:00
HOME,last5_score_for_pg,112.4000,https://www.nba.com/team/1610612760/thunder/schedule,2026-11-19T11:50:44+11:00
HOME,last5_score_against_pg,106.4000,https://www.nba.com/team/1610612760/thunder/schedule,2026-11-19T11:50:44+11:00
HOME,last10_score_for_pg,112.5000,https://www.nba.com/team/1610612760/thunder/schedule,2026-11-19T11:50:44+11:00
HOME,last10_score_against_pg,109.6000,https://www.nba.com/team/1610612760/thunder/schedule,2026-11-19T11:50:44+11:00
HOME,rest_days,2,https://www.nba.com/team/1610612760/thunder/schedule,2026-11-19T11:50:44+11:00
HOME,back_to_back,NO,https://www.nba.com/team/1610612760/thunder/schedule,2026-11-19T11:50:44+11:00
HOME,key_absences,Chet Holmgren OUT; Jalen Williams OUT; Cason Wallace OUT; Thomas Sorber OUT; Jaylin Williams AVAILABLE,https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-18_06_45PM.pdf,2026-11-19T11:50:44+11:00
HOME,lineup_confirmed,MISSING,No independently verified official starting five before card freeze,
HOME,venue,Paycom Center Oklahoma City,https://www.nba.com/game/atl-vs-okc-0022600265,2026-11-19T11:50:44+11:00
HOME,travel_km,MISSING,Exact route travel distance not measured,
HOME,opponent_strength,MISSING,No opponent adjusted efficiency series fitted,
HOME,opponent_strength_method,MISSING,No verified strength model calculation,
HOME,availability_effect,MISSING,No measured player absence effect,
HOME,adjustment_basis,MISSING,No numerical injury home travel adjustment applied,
HOME,last20_score_for_pg,MISSING,Fewer than 20 completed games in current season,
HOME,last20_score_against_pg,MISSING,Fewer than 20 completed games in current season,
AWAY,season_games,14,https://www.nba.com/team/1610612737/schedule,2026-11-19T11:50:44+11:00
AWAY,season_score_for_pg,117.7857,https://www.nba.com/team/1610612737/schedule,2026-11-19T11:50:44+11:00
AWAY,season_score_against_pg,116.0714,https://www.nba.com/team/1610612737/schedule,2026-11-19T11:50:44+11:00
AWAY,last5_score_for_pg,121.4000,https://www.nba.com/team/1610612737/schedule,2026-11-19T11:50:44+11:00
AWAY,last5_score_against_pg,121.6000,https://www.nba.com/team/1610612737/schedule,2026-11-19T11:50:44+11:00
AWAY,last10_score_for_pg,116.5000,https://www.nba.com/team/1610612737/schedule,2026-11-19T11:50:44+11:00
AWAY,last10_score_against_pg,117.8000,https://www.nba.com/team/1610612737/schedule,2026-11-19T11:50:44+11:00
AWAY,rest_days,2,https://www.nba.com/team/1610612737/schedule,2026-11-19T11:50:44+11:00
AWAY,back_to_back,NO,https://www.nba.com/team/1610612737/schedule,2026-11-19T11:50:44+11:00
AWAY,key_absences,CJ McCollum OUT; Kingston Flemings OUT; Mouhamed Gueye OUT; Jock Landale OUT; Asa Newell OUT; Henri Veesaar OUT; Rafael Castro OUT,https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-18_06_45PM.pdf,2026-11-19T11:50:44+11:00
AWAY,lineup_confirmed,MISSING,No independently verified official starting five before card freeze,
AWAY,venue,Paycom Center Oklahoma City,https://www.nba.com/game/atl-vs-okc-0022600265,2026-11-19T11:50:44+11:00
AWAY,travel_km,MISSING,Exact route travel distance not measured,
AWAY,opponent_strength,MISSING,No opponent adjusted efficiency series fitted,
AWAY,opponent_strength_method,MISSING,No verified strength model calculation,
AWAY,availability_effect,MISSING,No measured player absence effect,
AWAY,adjustment_basis,MISSING,No numerical injury home travel adjustment applied,
AWAY,last20_score_for_pg,MISSING,Fewer than 20 completed games in current season,
AWAY,last20_score_against_pg,MISSING,Fewer than 20 completed games in current season,
<!-- END ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0008 -->
<!-- END CANONICAL RESEARCH P-691 -->

<!-- BEGIN RESEARCH ADDENDUM P-691 2026-11-22-settlement-revision-1 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_11.md`, P-691. Source: `research/verification/mini_import_P-686_P-696_2026-11-22-1/SETTLEMENT.md` (P-691); exact settlement block follows.

<!-- BEGIN SETTLEMENT P-691 LOCAL-20261118DA6D9F6251746B979F5895FA-G0008 revision-1 -->
### P-691 · Basketball/NBA Regular Season (game 0022600265) — Atlanta Hawks @ Oklahoma City Thunder · 2026-11-18 CT · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0008` · `NBA:0022600265` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-19T00:55:08Z`; assessment `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (B):** **Atlanta Hawks 117-112 Oklahoma City Thunder** · Linescore: `ATL 31-33-19-34=117; OKC 29-22-32-29=112 (sum check: 31+33+19+34=117, 29+22+32+29=112)`.
- **Permitted source & capture:** `https://www.foxsports.com/nba/atlanta-hawks-vs-oklahoma-city-thunder-nov-18-2026-game-boxscore-106749` · capture `2026-11-22/G0008_fox_box.html` (SHA-256 `b23f869d9f53b087b49a1254313a09fba051faacf4d2a59b8ff9e06d9efb134c`). Corroboration: https://basketball.realgm.com/nba/scores/2026-11-18 (web search corroboration; script blocked).
- **Card-mean Brier / d:** `0.1950` / `+0.0550`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | AWAY | 6.5 | 0.5988 | -2.6368 | UNMEASURED | **WIN** | 0.1610 |
| L1 | NOT_RANKED | HANDICAP | HOME | -6.5 | 0.4012 | 2.6368 | UNMEASURED | **LOSS** | 0.1610 |
| L2 | R2 | TOTAL | OVER | 228.5 | 0.5214 | 229.5704 | UNMEASURED | **WIN** | 0.2291 |
| L2 | NOT_RANKED | TOTAL | UNDER | 228.5 | 0.4786 | 229.5704 | UNMEASURED | **LOSS** | 0.2291 |

**R1–R12 retrospective:** Atlanta won outright 117-112 behind 20-50 3PT shooting (Okongwu 28, Alexander-Walker 19, Jalen Johnson 16/12/11 triple-double). Both ATL +6.5 (Rank 1, p=0.5988) and Over 228.5 (Rank 2, p=0.5214, total 229) won. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

**Deep loss review:** None required (Rank 1, top side, and top total all won).
<!-- END SETTLEMENT P-691 LOCAL-20261118DA6D9F6251746B979F5895FA-G0008 revision-1 -->
<!-- END RESEARCH ADDENDUM P-691 2026-11-22-settlement-revision-1 -->

<!-- BEGIN CANONICAL RESEARCH P-692 -->
## P-692 — Basketball/NBA Regular Season (game 0022600264) — Detroit Pistons @ New Orleans Pelicans · 2026-11-18 CT

Canonical retention by prompt-4 import `2026-11-22T06:40:00+00:00`. Scheduled start `2026-11-19T12:00:00+11:00`. Original `20261118DA6D9F6251746B979F5895FA-G0009` (12361 B, SHA-256 `7e490b0b53e02e66d00389748c7e8bb177dd8dba41cd250bdd00d39b0deb13f8`, source `574cfeb9ead8a22d7a227b1180bb92ec29c8a1c2`, seal `SEALED` at `2026-11-19T01:06:10Z`). Original card follows verbatim; no forecast reissued; Track P scored separately via `ml one-chat score`.

# Research card — LOCAL-20261118DA6D9F6251746B979F5895FA-G0009 — Detroit Pistons @ New Orleans Pelicans

**Custody:** The original request was registered to `forecast-seals` after the three-file atomic request drop on `card-drops` commit `651c2ca14a6fef47ce58cb4e28dc80cb381b63b1`; GitHub workflow `44433371531` and all three independently published request file blobs verified before research. Governing main `cb97bbc2a9f882e7f8a093648b6137315951da8b`, ONECHAT_V1 / DROP-SEAL-v1; SPORTS_ONLY / MARKET_BLIND. No market prices or outside predictions used. This original research card is **not itself a guarantee of pre-first-play research or successful forecast sealing**.

## Original request — exact UTF-8 bytes

```text
Upcoming Basketball Game: DET Pistons @ NO Pelicans, NBA,\
Estimated Game Time Start: 19 November 2026, 12:10 PM AEDT (can be delayed so continue the process as normal)\
\
Pistons +3.5\
Pelicans -3.5\
Combined Total Points: Over/Under 224.5 Points [$github](app://connector_76869538009648d5b282a4bb21c3d157)
```

## A1 — Fixture and timing

Official NBA event `0022600264`: visiting Detroit Pistons, home New Orleans Pelicans, Smoothie King Center, New Orleans; official scheduled start Nov 18 2026 8:00 PM ET = **Nov 19 2026 12:00 PM AEDT**, ten minutes before the owner's estimate. Source https://www.nba.com/game/0022600264. Actual first play not independently verified. Original user receipt time recorded at approximate-minute resolution, not a verified delivery timestamp.

Research began only after independent registration verification, approximately `2026-11-19T12:00:14+11:00`. The official NBA game page at `2026-11-19T12:00:45+11:00` displayed the schedule, without a target-game live score in its accessible text; that observation **cannot prove first play had not occurred**, as the page may omit dynamic scoreboard content. Other sources during research were pre-event team fixtures, completed results and existing preview articles. Outcome exposure: NONE seen in the retrieved target-game page. Research ended 2026-11-19T12:04:29+11:00. This may be ineligible under the prospective cutoff; do not infer compliance from the scheduled time alone.

## A2 — Exact contracts

L1 Detroit Pistons **+3.5** versus New Orleans Pelicans **−3.5**. L2 combined total **OVER/UNDER 224.5**. Both are full game including all overtime. Two sides each with no pushes possible. No winner contract requested. Registered baseline unavailable (`UNAVAILABLE:NO_FROZEN_SPORTING_BASELINE`).

## A3 — Sporting observations

Detroit went **9–4** through its 13 completed games, scoring 114.85 and conceding 108.92 per game; last-five 120.80 scored / 120.40 conceded; last-ten 113.80 / 109.90. Results source: https://www.cbssports.com/nba/teams/DET/detroit-pistons/schedule/regular/, with the November 17 win at San Antonio **105–93** corroborated independently via https://www.nba.com/game/det-vs-sas-0022600255. Previous 12-game table is stale by one game and was augmented with this verified San Antonio result.

New Orleans went **5–10** through 15 games, scoring 115.80 and conceding 122.87; last-five 106.40/127.00; last-ten 114.00/123.50. Source https://www.cbssports.com/nba/teams/NO/new-orleans-pelicans/schedule/. The latest five were losses at Golden State and to Brooklyn, Memphis and Denver, then a 115–94 home win against Golden State.

**Fatigue:** Detroit last played Nov 17 in San Antonio, a true back-to-back on the fourth road game in a row (zero off days). New Orleans last played Nov 16 and has one full off day, playing at home. Source https://www.nba.com/pistons/schedule, https://www.nba.com/pelicans/schedule.

**Availability:** The official New Orleans preview https://www.nba.com/pelicans/news/pelicans-vs-pistons-injury-report-game-preview-11-18-2026 reports Detroit **Jalen Duren OUT, Ronald Holland II OUT, Taurean Prince OUT, Duncan Robinson OUT**, and **Cade Cunningham QUESTIONABLE**; it lists New Orleans **Bennedict Mathurin, Bryce McGowens, Trey Murphy III, Dejounte Murray, Trendon Watford OUT**. A subsequent contemporaneous team reporter additionally described Cunningham as out, but because it was not confirmed through an independent official game-day roster/availability record in this research window, the published FACTS retain the official preview's questionable status and note unresolved uncertainty here. The preview shows **previous-game** lineups, not confirmed starting fives. No measured injury on/off effects, verified opponent-adjusted efficiencies or exact travel km were available.

No 20-game current-season window exists for either team; those metrics stay MISSING. H2H was not weighted because 2025–26 personnel differs. No source-backed coach or matchup points adjustments were applied.

## A4 — Model recipe and uncertainty

Analyst-chosen recency blend: for scored and conceded PPG per team, **0.60×last-five + 0.25×last-ten + 0.15×current-season**. Windows overlap; the weights are not trained or independently validated. The blended PPG scored/conceded are Detroit 118.157/116.053 and New Orleans 109.710/125.505. Forecast Detroit score is the mean of Detroit blended scored and New Orleans blended conceded; New Orleans score is the mean of New Orleans blended scored and Detroit blended conceded.

**Estimated scoring centres:** Detroit 121.831, New Orleans 112.882, combined 234.713, visiting Detroit margin **+8.949**. These centres are **not adjusted** for the materially uncertain Cunningham availability or Detroit's back-to-back; such unmeasured inputs can invalidate the direction. The framework's NBA raw SD references **15.43 margin and 19.90 total** are used as broad Normal-distribution approximations, not proof of calibrated uncertainty for this match. A joint covariance or explicit overtime branch was not fitted; the available scalar estimates are marginal diagnostics only, not the output of a calibrated joint-score model.

`P(DET +3.5)=Φ((8.9492+3.5)/15.43)=0.7901`; reciprocal `P(NOP −3.5)=0.2099`. `P(OVER 224.5)=Φ((234.7127−224.5)/19.90)=0.6961`; reciprocal Under `0.3039`. There is no draw at the given half-point lines. All four have `UNMEASURED` availability status; **no qualified Rank-1 or Rank-2 selection** is issued despite any numeric threshold because lineup, rest and impact uncertainties have no measurable effect sizes. Most serious DET +3.5 failure: the back-to-back and Cunningham's uncertain absence remove sufficient Detroit creation; most serious Over failure: Detroit's shooting/pace drop and the absence of multiple leading players.

The full-time score and the independent first-play time must be sourced later from https://www.nba.com/game/0022600264 with retained capture; do not settle here. If first play predates publication, **this card must be excluded** from prospective validation irrespective of its apparent numeric hit rate.

## A5 — Exact ONECHAT_V1 frozen original

<!-- BEGIN ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0009 -->
format: ONECHAT_V1
card_key: 20261118DA6D9F6251746B979F5895FA-G0009
sport: Basketball
competition: NBA
home: New Orleans Pelicans
away: Detroit Pistons
scheduled_start: 2026-11-19T12:00:00+11:00
request_at: 2026-11-19T11:58:00+11:00
research_start_at: 2026-11-19T12:00:14+11:00
research_end_at: 2026-11-19T12:04:29+11:00
not_started_source: https://www.nba.com/game/0022600264
not_started_observed_at: 2026-11-19T12:00:45+11:00
outcome_exposure: NONE

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,HANDICAP,AWAY,3.5,0.7901,,8.9492,UNMEASURED,https://www.nba.com/game/0022600264
L1,HANDICAP,HOME,-3.5,0.2099,,-8.9492,UNMEASURED,https://www.nba.com/game/0022600264
L2,TOTAL,OVER,224.5,0.6961,,234.7127,UNMEASURED,https://www.nba.com/game/0022600264
L2,TOTAL,UNDER,224.5,0.3039,,234.7127,UNMEASURED,https://www.nba.com/game/0022600264

FACTS
side,field,value,source,observed_at
HOME,season_games,15,https://www.cbssports.com/nba/teams/NO/new-orleans-pelicans/schedule/,2026-11-19T12:02:55+11:00
HOME,season_score_for_pg,115.8000,https://www.cbssports.com/nba/teams/NO/new-orleans-pelicans/schedule/,2026-11-19T12:02:55+11:00
HOME,season_score_against_pg,122.8667,https://www.cbssports.com/nba/teams/NO/new-orleans-pelicans/schedule/,2026-11-19T12:02:55+11:00
HOME,last5_score_for_pg,106.4000,https://www.cbssports.com/nba/teams/NO/new-orleans-pelicans/schedule/,2026-11-19T12:02:55+11:00
HOME,last5_score_against_pg,127.0000,https://www.cbssports.com/nba/teams/NO/new-orleans-pelicans/schedule/,2026-11-19T12:02:55+11:00
HOME,last10_score_for_pg,114.0000,https://www.cbssports.com/nba/teams/NO/new-orleans-pelicans/schedule/,2026-11-19T12:02:55+11:00
HOME,last10_score_against_pg,123.5000,https://www.cbssports.com/nba/teams/NO/new-orleans-pelicans/schedule/,2026-11-19T12:02:55+11:00
HOME,rest_days,1,https://www.nba.com/pelicans/schedule,2026-11-19T12:02:55+11:00
HOME,back_to_back,NO,https://www.nba.com/pelicans/schedule,2026-11-19T12:02:55+11:00
HOME,key_absences,Bennedict Mathurin OUT; Bryce McGowens OUT; Trey Murphy III OUT; Dejounte Murray OUT; Trendon Watford OUT,https://www.nba.com/pelicans/news/pelicans-vs-pistons-injury-report-game-preview-11-18-2026,2026-11-19T12:02:55+11:00
HOME,lineup_confirmed,MISSING,No full certified official starting five independently verified before research cutoff,
HOME,venue,Smoothie King Center New Orleans,https://www.nba.com/pelicans/news/pelicans-vs-pistons-injury-report-game-preview-11-18-2026,2026-11-19T12:02:55+11:00
HOME,travel_km,MISSING,No sourced actual travel route distance,
HOME,opponent_strength,MISSING,No audited opponent-adjusted numerical model,
HOME,opponent_strength_method,MISSING,No fitted opponent adjusted ORtg or DRtg,
HOME,availability_effect,MISSING,No measured injury or rotation point effect,
HOME,adjustment_basis,MISSING,No supported numeric player injury or road fatigue adjustment fitted,
HOME,last20_score_for_pg,MISSING,Fewer than 20 completed games in 2026-27 season,
HOME,last20_score_against_pg,MISSING,Fewer than 20 completed games in 2026-27 season,
AWAY,season_games,13,https://www.cbssports.com/nba/teams/DET/detroit-pistons/schedule/regular/,2026-11-19T12:02:55+11:00
AWAY,season_score_for_pg,114.8462,https://www.cbssports.com/nba/teams/DET/detroit-pistons/schedule/regular/,2026-11-19T12:02:55+11:00
AWAY,season_score_against_pg,108.9231,https://www.cbssports.com/nba/teams/DET/detroit-pistons/schedule/regular/,2026-11-19T12:02:55+11:00
AWAY,last5_score_for_pg,120.8000,https://www.cbssports.com/nba/teams/DET/detroit-pistons/schedule/regular/,2026-11-19T12:02:55+11:00
AWAY,last5_score_against_pg,120.4000,https://www.cbssports.com/nba/teams/DET/detroit-pistons/schedule/regular/,2026-11-19T12:02:55+11:00
AWAY,last10_score_for_pg,113.8000,https://www.cbssports.com/nba/teams/DET/detroit-pistons/schedule/regular/,2026-11-19T12:02:55+11:00
AWAY,last10_score_against_pg,109.9000,https://www.cbssports.com/nba/teams/DET/detroit-pistons/schedule/regular/,2026-11-19T12:02:55+11:00
AWAY,rest_days,0,https://www.nba.com/pistons/schedule,2026-11-19T12:02:55+11:00
AWAY,back_to_back,YES,https://www.nba.com/pistons/schedule,2026-11-19T12:02:55+11:00
AWAY,key_absences,Jalen Duren OUT; Ronald Holland II OUT; Taurean Prince OUT; Duncan Robinson OUT; Cade Cunningham QUESTIONABLE in the official pregame preview,https://www.nba.com/pelicans/news/pelicans-vs-pistons-injury-report-game-preview-11-18-2026,2026-11-19T12:02:55+11:00
AWAY,lineup_confirmed,MISSING,No full certified official starting five independently verified before research cutoff,
AWAY,venue,Smoothie King Center New Orleans,https://www.nba.com/pelicans/news/pelicans-vs-pistons-injury-report-game-preview-11-18-2026,2026-11-19T12:02:55+11:00
AWAY,travel_km,MISSING,No sourced actual travel route distance,
AWAY,opponent_strength,MISSING,No audited opponent-adjusted numerical model,
AWAY,opponent_strength_method,MISSING,No fitted opponent adjusted ORtg or DRtg,
AWAY,availability_effect,MISSING,No measured injury or rotation point effect,
AWAY,adjustment_basis,MISSING,No supported numeric player injury or road fatigue adjustment fitted,
AWAY,last20_score_for_pg,MISSING,Fewer than 20 completed games in 2026-27 season,
AWAY,last20_score_against_pg,MISSING,Fewer than 20 completed games in 2026-27 season,
<!-- END ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0009 -->
<!-- END CANONICAL RESEARCH P-692 -->

<!-- BEGIN RESEARCH ADDENDUM P-692 2026-11-22-settlement-revision-1 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_11.md`, P-692. Source: `research/verification/mini_import_P-686_P-696_2026-11-22-1/SETTLEMENT.md` (P-692); exact settlement block follows.

<!-- BEGIN SETTLEMENT P-692 LOCAL-20261118DA6D9F6251746B979F5895FA-G0009 revision-1 -->
### P-692 · Basketball/NBA Regular Season (game 0022600264) — Detroit Pistons @ New Orleans Pelicans · 2026-11-18 CT · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0009` · `NBA:0022600264` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-19T01:06:10Z`; assessment `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (B):** **Detroit Pistons 122-109 New Orleans Pelicans** · Linescore: `DET 31-36-25-30=122; NOP 31-29-26-23=109 (sum check: 31+36+25+30=122, 31+29+26+23=109)`.
- **Permitted source & capture:** `https://www.foxsports.com/nba/detroit-pistons-vs-new-orleans-pelicans-nov-18-2026-game-boxscore-106748` · capture `2026-11-22/G0009_fox_box.html` (SHA-256 `994cc432a25fd1625c413b8a32bc3e880febc9b965b7fc802bdf959c0136fe81`). Corroboration: https://basketball.realgm.com/nba/scores/2026-11-18 (web search corroboration; script blocked).
- **Card-mean Brier / d:** `0.0682` / `+0.1818`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | AWAY | 3.5 | 0.7901 | 8.9492 | UNMEASURED | **WIN** | 0.0441 |
| L1 | NOT_RANKED | HANDICAP | HOME | -3.5 | 0.2099 | -8.9492 | UNMEASURED | **LOSS** | 0.0441 |
| L2 | R2 | TOTAL | OVER | 224.5 | 0.6961 | 234.7127 | UNMEASURED | **WIN** | 0.0924 |
| L2 | NOT_RANKED | TOTAL | UNDER | 224.5 | 0.3039 | 234.7127 | UNMEASURED | **LOSS** | 0.0924 |

**R1–R12 retrospective:** Detroit shot 53.2% FG / 53.1% 3PT (17-32) to win 122-109 despite Zion Williamson's 24 and Jordan Poole's 22. Both DET +3.5 (p=0.7901) and Over 224.5 (p=0.6961, total 231) won decisively (best card Brier 0.0682, d=+0.1818). Note: sealed 6m10s after scheduled start (actual tip unverified). All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

**Deep loss review:** None required (Rank 1, top side, and top total all won).
<!-- END SETTLEMENT P-692 LOCAL-20261118DA6D9F6251746B979F5895FA-G0009 revision-1 -->
<!-- END RESEARCH ADDENDUM P-692 2026-11-22-settlement-revision-1 -->

<!-- BEGIN CANONICAL RESEARCH P-693 -->
## P-693 — Basketball/NCAAB 2026-27 — Samford Bulldogs @ USC Upstate Spartans · 2026-11-18 ET

Canonical retention by prompt-4 import `2026-11-22T06:40:00+00:00`. Scheduled start `2026-11-19T12:30:00+11:00`. Original `20261118DA6D9F6251746B979F5895FA-G0010` (12011 B, SHA-256 `cde21124a93f5afe01093baf70cf5d563bb68d64541919f8b502bbc5cae7eca8`, source `ae2367145977f2d59f3b638097a7537b945bf4c7`, seal `SEALED` at `2026-11-19T01:29:43Z`). Original card follows verbatim; no forecast reissued; Track P scored separately via `ml one-chat score`.

# Pregame research card — LOCAL-20261118DA6D9F6251746B979F5895FA-G0010 — Samford @ USC Upstate — 18 Nov 2026 ET

**Immutable original authored at** 2026-11-19T12:28:22+11:00. Request first registered through `card-drops` atomic commit `977d717d6edeed240fba09e2e378c4b9485e41b3`, workflow `44436631519` success and independently published REQUEST.txt/EVENT.csv/CONTRACTS.csv on `forecast-seals` **before** sports research. Policy repository `main@cb97bbc2a9f882e7f8a093648b6137315951da8b` read-only; `ONECHAT_V1`, `DROP-SEAL-v1`; `SPORTS_ONLY` and `MARKET_BLIND`. This original file does not claim successful card sealing unless separately verified.

## Original owner request — preserved verbatim

```text
Upcoming Basketball Game: Samford vs USC Upstate, NCAB,\
Estimated Game Time Start: 19 November 2026, 12:30 PM AEDT (can be delayed so continue the process as normal)\
\
Upstate +8.5\
Samford -8.5\
Combined Total Points: Over/Under 150.5 Points  [$github](app://connector_76869538009648d5b282a4bb21c3d157)
```

## A1 — Verified fixture, unusual relocation and timing

- Competition NCAAB (user wrote `NCAB`); official USC Upstate native game centre `UPSTATE_GAMECENTER:6709`: https://upstatespartans.com/game-center/6709. Nominal home USC Upstate, visitor Samford.
- **Important change:** USC Upstate's 18 Nov 4:12 PM ET relocation notice https://upstatespartans.com/news/2026/11/18/usc-upstate-mens-basketball-contest-against-samford-relocated-to-furman-university-due-to-spartanburg-water-issues supersedes earlier advertised 6:30 PM ET start and Hodge Center location. The contest moved to **Timmons Arena at Furman University in Greenville, South Carolina**, with a tip-off **no earlier than 8:30 PM US Eastern**, equivalent to **19 Nov 2026 12:30 PM AEDT**. The notice specifies no fans and no television/video broadcast. Do not use stale team schedule's 6:30 PM time as the official cutoff.
- The official game centre at https://upstatespartans.com/game-center/6709 was observed during research around **12:26:14 PM AEDT**, still displaying `Stats for upcoming game`, no target-game final or live scores. This is a pre-event status indication only; independently verified actual first play remains required. Outcome exposure NONE.
- Request receipt `12:23` AEDT is an approximate minute; no user-transport seconds available. Registration GitHub workflow `44436631519` succeeded before research started 12:25:24 AEDT. Research ended 2026-11-19T12:28:22+11:00.
- Full-game settlement includes overtime; the supplied half-point spreads/totals cannot push.

## A2 — Frozen contracts

- L1 HANDICAP: USC Upstate **+8.5** (HOME) versus Samford **−8.5** (AWAY).
- L2 TOTAL: full-game **OVER/UNDER 150.5** points.
- The owner did not request winner/ML; do not issue a winner contract. There is no frozen independent sporting baseline (`UNAVAILABLE:NO_FROZEN_SPORTING_BASELINE`), and no price, bookmaker, external tip or betting prediction was read or used.

## A3 — Verified completed results only

- **Samford 1–2** in three 2026–27 non-exhibition games (Nov 2 Berry W 87–58; Nov 7 at UNLV L 79–88; Nov 13 Wright State L 66–90). Mean **77.33 scored / 78.67 allowed**, source https://samfordsports.com/sports/mens-basketball/schedule; first game Berry is a non-Division I opponent. Last-five, last-ten and last-twenty current-season full windows **MISSING**, not substituted by all three games.
- **USC Upstate 1–4**, five completed games: Nov 2 at East Carolina L 70–83; Nov 6 SC State L 70–78; Nov 9 at Coastal Carolina L 56–65; Nov 11 Bob Jones W 104–49; Nov 14 at Campbell L 77–93. Mean and full last-five **75.40 scored / 73.60 allowed**; source https://bigsouthsports.com/schedule.aspx?schedule=4481. Bob Jones was a non-Division I opponent, substantially inflating the five-game scoring average. Last-ten/twenty full current-season windows unavailable.
- **Sample-quality sensitivity, D-I opponents only:** excluding Berry and Bob Jones gives Samford 72.50 for/89.00 against (2 games) and Upstate 68.25 for/79.75 against (4 games), with estimated centres 76.125 Samford and 78.625 Upstate, total 154.75. The same directional cushion appears, but both the all-games and DI-only samples are too small and opponent strength too disparate to support reliable calibration.
- Last completed games Samford Nov 13 (four full calendar rest days) and Upstate Nov 14 (three); neither on a back-to-back. Samford travels, but a measured travel distance and any adjustment due to the neutral substitute venue were not established. No crowd also substantially changes the conventional home dynamic, without a measured points effect.
- Prior true official H2H: none (schools' first meeting according to both official previews https://upstatespartans.com/news/2026/11/18/usc-upstate-mens-basketball-contest-against-samford-relocated-to-furman-university-due-to-spartanburg-water-issues and https://samfordsports.com/news/2026/11/17/mens-basketball-bulldogs-set-for-midweek-road-contest-at-usc-upstate).
- Samford early-season scorer Will Shaver 15.3 points/game and USC Upstate David Tubek 13.8 points/game reported by the official pregame preview. No official certified starting fives or comprehensive absences were found; no absence points or replacement minutes were fabricated. No opponent-adjusted ORtg/DRtg or play-by-play possession pace was computed.

## A4 — Transparent diagnostic, not a calibrated forecast

Using only the **current-season raw per-game averages** (3 Samford, 5 Upstate), estimate each team's score as the midpoint of its own average points for and opponent's average points conceded. Thus Samford `(77.3333+73.6000)/2` = **75.4667**, USC Upstate `(75.4000+78.6667)/2` = **77.0333**, combined **152.5000**, home margin Upstate **+1.5667**. This is a simple heuristic that **does not adjust for schedule difficulty or the distorted non-DI games**, and is not a trained model.

For transparency only, assume *subjective*, uncalibrated Gaussian spreads: full-game margin SD **16 points**, total SD **18 points**, chosen broadly due to limited history; neither a competition-fitted standard deviation nor an admitted reference. No joint covariance, possessions model, Monte Carlo or quantified OT branch was executed. `P(Upstate +8.5)=Φ((1.5667+8.5)/16)=0.7354`, Samford −8.5 reciprocal **0.2646**. `P(Over 150.5)=Φ((152.5000−150.5)/18)=0.5442`, Under reciprocal **0.4558**. Because the underlying samples are tiny and uneven, these are **analytical diagnostics, not calibrated or qualified selections**. Do not interpret 73.5% as evidence of a statistical advantage; the principal failure route is Samford's stronger opposition schedule masking underlying team strength and the venue/roster uncertainty. Over fails if either team's scoring resembles its lower offensive outputs versus D-I opponents.

The NCAA venue change, absent crowd, opponents' unequal quality, no confirmed starters and non-DI outliers are material limits. In the absence of an independently qualified model, **no Rank-1 or Rank-2 issuance**. Actual first-play timing and GitHub server push activity must later be independently captured before prospective acceptance. Official future result source https://upstatespartans.com/game-center/6709.

## A5 — ONECHAT_V1 original block

<!-- BEGIN ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0010 -->
format: ONECHAT_V1
card_key: 20261118DA6D9F6251746B979F5895FA-G0010
sport: Basketball
competition: NCAAB
home: USC Upstate
away: Samford
scheduled_start: 2026-11-19T12:30:00+11:00
request_at: 2026-11-19T12:23:00+11:00
research_start_at: 2026-11-19T12:25:24+11:00
research_end_at: 2026-11-19T12:28:22+11:00
not_started_source: https://upstatespartans.com/game-center/6709
not_started_observed_at: 2026-11-19T12:26:14+11:00
outcome_exposure: NONE

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,HANDICAP,HOME,8.5,0.7354,,1.5667,UNMEASURED,https://upstatespartans.com/game-center/6709
L1,HANDICAP,AWAY,-8.5,0.2646,,-1.5667,UNMEASURED,https://upstatespartans.com/game-center/6709
L2,TOTAL,OVER,150.5,0.5442,,152.5000,UNMEASURED,https://upstatespartans.com/game-center/6709
L2,TOTAL,UNDER,150.5,0.4558,,152.5000,UNMEASURED,https://upstatespartans.com/game-center/6709

FACTS
side,field,value,source,observed_at
HOME,season_games,5,https://bigsouthsports.com/schedule.aspx?schedule=4481,2026-11-19T12:26:14+11:00
HOME,season_score_for_pg,75.4000,https://bigsouthsports.com/schedule.aspx?schedule=4481,2026-11-19T12:26:14+11:00
HOME,season_score_against_pg,73.6000,https://bigsouthsports.com/schedule.aspx?schedule=4481,2026-11-19T12:26:14+11:00
HOME,last5_score_for_pg,75.4000,https://bigsouthsports.com/schedule.aspx?schedule=4481,2026-11-19T12:26:14+11:00
HOME,last5_score_against_pg,73.6000,https://bigsouthsports.com/schedule.aspx?schedule=4481,2026-11-19T12:26:14+11:00
HOME,last10_score_for_pg,MISSING,Fewer than ten completed current season games,
HOME,last10_score_against_pg,MISSING,Fewer than ten completed current season games,
HOME,rest_days,3,https://bigsouthsports.com/schedule.aspx?schedule=4481,2026-11-19T12:26:14+11:00
HOME,back_to_back,NO,https://bigsouthsports.com/schedule.aspx?schedule=4481,2026-11-19T12:26:14+11:00
HOME,key_absences,MISSING,No complete verified injury and suspension status at research cutoff,
HOME,lineup_confirmed,MISSING,No certified official starting five verified,
HOME,venue,Timmons Arena Furman University Greenville South Carolina,https://upstatespartans.com/game-center/6709,2026-11-19T12:26:14+11:00
HOME,travel_km,MISSING,No measured actual team travel route distance,
HOME,opponent_strength,MISSING,No adjusted opponent strength estimate independently validated,
HOME,opponent_strength_method,MISSING,No auditable opponent adjustment calculation,
HOME,availability_effect,MISSING,No measured injury replacement or availability impact,
HOME,adjustment_basis,MISSING,No supported numerical home venue travel or lineup adjustment,
HOME,last20_score_for_pg,MISSING,Fewer than twenty current season completed games,
HOME,last20_score_against_pg,MISSING,Fewer than twenty current season completed games,
AWAY,season_games,3,https://samfordsports.com/sports/mens-basketball/schedule,2026-11-19T12:26:14+11:00
AWAY,season_score_for_pg,77.3333,https://samfordsports.com/sports/mens-basketball/schedule,2026-11-19T12:26:14+11:00
AWAY,season_score_against_pg,78.6667,https://samfordsports.com/sports/mens-basketball/schedule,2026-11-19T12:26:14+11:00
AWAY,last5_score_for_pg,MISSING,Fewer than five completed current season games,
AWAY,last5_score_against_pg,MISSING,Fewer than five completed current season games,
AWAY,last10_score_for_pg,MISSING,Fewer than ten completed current season games,
AWAY,last10_score_against_pg,MISSING,Fewer than ten completed current season games,
AWAY,rest_days,4,https://samfordsports.com/sports/mens-basketball/schedule,2026-11-19T12:26:14+11:00
AWAY,back_to_back,NO,https://samfordsports.com/sports/mens-basketball/schedule,2026-11-19T12:26:14+11:00
AWAY,key_absences,MISSING,No complete verified injury and suspension status at research cutoff,
AWAY,lineup_confirmed,MISSING,No certified official starting five verified,
AWAY,venue,Timmons Arena Furman University Greenville South Carolina,https://upstatespartans.com/game-center/6709,2026-11-19T12:26:14+11:00
AWAY,travel_km,MISSING,No measured actual team travel route distance,
AWAY,opponent_strength,MISSING,No adjusted opponent strength estimate independently validated,
AWAY,opponent_strength_method,MISSING,No auditable opponent adjustment calculation,
AWAY,availability_effect,MISSING,No measured injury replacement or availability impact,
AWAY,adjustment_basis,MISSING,No supported numerical home venue travel or lineup adjustment,
AWAY,last20_score_for_pg,MISSING,Fewer than twenty current season completed games,
AWAY,last20_score_against_pg,MISSING,Fewer than twenty current season completed games,
<!-- END ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0010 -->
<!-- END CANONICAL RESEARCH P-693 -->

<!-- BEGIN RESEARCH ADDENDUM P-693 2026-11-22-settlement-revision-1 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_11.md`, P-693. Source: `research/verification/mini_import_P-686_P-696_2026-11-22-1/SETTLEMENT.md` (P-693); exact settlement block follows.

<!-- BEGIN SETTLEMENT P-693 LOCAL-20261118DA6D9F6251746B979F5895FA-G0010 revision-1 -->
### P-693 · Basketball/NCAAB 2026-27 — Samford Bulldogs @ USC Upstate Spartans · 2026-11-18 ET · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0010` · `UPSTATE_GAMECENTER:6709` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-19T01:29:43Z`; assessment `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (A):** **Samford 74-64 USC Upstate** · Linescore: `SAM 37-37=74; UPST 27-37=64 (sum check: 37+37=74, 27+37=64)`.
- **Permitted source & capture:** `https://samfordsports.com/boxscore.aspx?id=13967` · capture `2026-11-22/G0010_samford_box.html` (SHA-256 `5d6331f79e9b10982a3186fd322967aca776517d22231128967baa750efb69c6`). Corroboration: https://upstatespartans.com/game-center/6709 (captured in G0010_upstate.html).
- **Card-mean Brier / d:** `0.4185` / `-0.1685`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | HOME | 8.5 | 0.7354 | 1.5667 | UNMEASURED | **LOSS** | 0.5408 |
| L1 | NOT_RANKED | HANDICAP | AWAY | -8.5 | 0.2646 | -1.5667 | UNMEASURED | **WIN** | 0.5408 |
| L2 | R2 | TOTAL | OVER | 150.5 | 0.5442 | 152.5000 | UNMEASURED | **LOSS** | 0.2962 |
| L2 | NOT_RANKED | TOTAL | UNDER | 150.5 | 0.4558 | 152.5000 | UNMEASURED | **WIN** | 0.2962 |

**R1–R12 retrospective:** Samford led 37-27 at half and won 74-64 (Cooper Noard 19, Will Shaver 15/11, Cade Norris 14/7/7). Worst Brier card of mini (0.4185, d=-0.1685): Upstate +8.5 was priced at 0.7354 (expected margin +1.57 home) on a 1-5 mid-major without opponent-strength adjustment. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-007 · P-693 · Upstate +8.5 (TOP_SIDE_AND_RANK_1) — Verdict: `ERROR` · Class: `SMALL_SAMPLE_STRENGTH_OVERREACH` (alias `PLUS_HANDICAP_WITHOUT_OPPONENT_CHECK`)**
1. **Contract & trigger:** Upstate +8.5 (TOP_SIDE_AND_RANK_1).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Samford 74-64 USC Upstate (SAM 37-37=74; UPST 27-37=64 (sum check: 37+37=74, 27+37=64)).
4. **Outcome in frozen distribution & what decided the game:** Card priced USC Upstate +8.5 at 0.7354 (centre +1.57 home!) from raw early-season PPG on a tiny sample (1-5 record) with no opponent-strength adjustment against a stronger SoCon opponent (Samford). This repeats the exact PLUS_HANDICAP_WITHOUT_OPPONENT_CHECK failure class from P-660 and P-685, causing a -0.2908 Brier loss on L1 alone.
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `ERROR` (`SMALL_SAMPLE_STRENGTH_OVERREACH` / `PLUS_HANDICAP_WITHOUT_OPPONENT_CHECK`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.

**DLR-2026-11-22-008 · P-693 · Over 150.5 (TOP_TOTAL) — Verdict: `MODEL_LIMIT` · Class: `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`**
1. **Contract & trigger:** Over 150.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Samford 74-64 USC Upstate (SAM 37-37=74; UPST 27-37=64 (sum check: 37+37=74, 27+37=64)).
4. **Outcome in frozen distribution & what decided the game:** Card projected 152.50 (p=0.5442, inside H-NODIR band) from unadjusted early-season averages; actual total finished 138 (-12.5 vs line).
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `MODEL_LIMIT` (`BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.

**Joint side + total loss note (P-693):** Both top side and top total lost on this card (card-mean Brier `0.4185`, `d = -0.1685`). Shared root causes: unmeasured availability / opponent-strength overreach paired with unadjusted total Over bias.
<!-- END SETTLEMENT P-693 LOCAL-20261118DA6D9F6251746B979F5895FA-G0010 revision-1 -->
<!-- END RESEARCH ADDENDUM P-693 2026-11-22-settlement-revision-1 -->

<!-- BEGIN CANONICAL RESEARCH P-694 -->
## P-694 — Basketball/NBA Regular Season (game 0022600268) — Utah Jazz @ Los Angeles Lakers · 2026-11-18 PT

Canonical retention by prompt-4 import `2026-11-22T06:40:00+00:00`. Scheduled start `2026-11-19T14:00:00+11:00`. Original `20261118DA6D9F6251746B979F5895FA-G0011` (11647 B, SHA-256 `95a55a7bd3d9ed198b2268b163fcfdb967a9b70ad1b30a61c07b2bf86bf4c9ad`, source `5638c8ed3ab4771cf296c6aff418bb4333908450`, seal `SEALED` at `2026-11-19T03:14:19Z`). Original card follows verbatim; no forecast reissued; Track P scored separately via `ml one-chat score`.

# ORIGINAL RESEARCH CARD — LOCAL-20261118DA6D9F6251746B979F5895FA-G0011

**Mode:** ONECHAT_V1 / registered request; sports-only evidence, not an independently validated or qualified model. Research ran after the official **scheduled** 14:00 AEDT tip-off, and could not verify actual first play. **Prospective eligibility NOT ESTABLISHED** and cannot be inferred from an apparently upcoming website. Historical research only if actual play had begun. No game score was knowingly used; if such a score becomes visible, this original must be tagged outcome-exposed, not revised in place. Repo `main` read only `cb97bbc2a9f882e7f8a093648b6137315951da8b`.

## Original owner request — verbatim

```text
\
Upcoming Basketball Game: UTA Jazz @ LA Lakers, NBA,\
Estimated Game Time Start: 19 November 2026, 2:10 PM AEDT (can be delayed so continue the process as normal)\
\
Jazz +11.5\
Lakers -11.5\
Combined Total Points: Over/Under 229.5 Points \
&#x20;[$github](app://connector_76869538009648d5b282a4bb21c3d157)
```

## A1 — Fixture identity, request custody, event state

- Official NBA regular-season event `NBA:0022600268`, Utah Jazz away at Los Angeles Lakers home, Crypto.com Arena. Official local tip-off 7:00 PM PST Wed November 18, equivalently **Thursday Nov 19 2026 14:00 AEDT**, 10 minutes before user estimated 14:10. Fixture page https://www.nba.com/game/uta-vs-lal-0022600268 and official team schedule https://www.nba.com/team/1610612747/lakers/schedule.
- Original REQUEST.txt / EVENT.csv / CONTRACTS.csv atomically pushed to `card-drops` commit `ff71b3250d2735dc35bc10cf52e08faf821ed243`; `seal-drops` request workflow 44449118139 completed SUCCESS and the frozen originals were independently inspected in `forecast-seals` before research.
- Exact user message includes literal first-line backslash and last-line `&#x20;` entity. They are copied without post-hoc modification.
- Research began 14:08:07 AEDT, **after scheduled tip**. At 14:10:45 AEDT, official Lakers page still listed the Nov 18 Jazz game as upcoming (with no score visible); other live trackers had placeholder empty quarters. **This does not independently prove play had not begun.** Outcome exposure NONE from consulted target-game pages; event state remains `FIRST_PLAY_NOT_VERIFIED`. Any later live score discovery invalidates pregame classification. End time 2026-11-19T14:12:22+11:00.
- The user's requested wager period defaults to full final score INCLUDING overtime; exact +11.5 / −11.5 and 229.5 contracts are separately represented on both sides. No additional winner contract requested. No external price, market reference or prediction was used, and `baseline_p` was not frozen at registration (`UNAVAILABLE:NO_FROZEN_SPORTING_BASELINE`).

## A2 — Current sporting evidence before target game

- From official NBA Utah team schedule https://www.nba.com/team/1610612762/jazz/schedule, completed 15 regular-season games: **2–13**; scored 108.73 and conceded 117.27 per game, last five scored/allowed **113.80/116.00**, last ten **106.90/115.80**. Five newest: Nov 10 vs Miami 109–115; Nov 11 vs Orlando 108–123; Nov 13 at Houston 118–125; Nov 15 vs San Antonio 102–110; Nov 17 at Clippers **132–107**. No 20-game current-season window exists.
- Official Lakers team schedule https://www.nba.com/team/1610612747/lakers/schedule: **13–2** in 15 regular-season games; scored 122.47, conceded 114.80, last five **123.40/115.80**, last ten **122.10/115.40**. Newest: Nov 8 Detroit 121–116; Nov 9 Atlanta 124–114; Nov 11 Milwaukee 123–112; Nov 15 Phoenix 131–123; Nov 17 Charlotte **118–114 OT**. Nine consecutive Lakers wins, but the most recent required overtime and a large comeback.
- **Schedule:** both played November 17 local US time and are on immediate second nights of back-to-backs, zero calendar rest days. Jazz travelled from LA Clippers' Inglewood arena to the Lakers' Los Angeles arena, a short transfer but no measured km; Lakers remain home after overtime versus Charlotte.
- **Roster status**, official 8:15 PM ET injury bulletin https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-18_08_15PM.pdf, page 8: Jazz **Lauri Markkanen OUT** (hand), **Jaren Jackson Jr OUT** (knee), **Jusuf Nurkic OUT** (foot), **Jaxson Hayes QUESTIONABLE** (knee). Lakers **Austin Reaves OUT** (heel), **Quentin Grimes AVAILABLE** (finger). Neither starting five was independently confirmed. No defensible player-specific with/without effect was estimated, so no points adjustment is applied. Current official injury information is significantly more relevant than an old healthy-roster projection.
- H2H Oct 25 at Utah: Lakers 132–123 Jazz, total 255; a single high-scoring meeting cannot be assumed to repeat. Home venue favourable for Lakers qualitatively, but no separately fitted home advantage; opponent-adjusted efficiency and possession pace measurements were not independently verified.

## A3 — Transparent score distribution diagnostic

A simple overlapping recency blend, chosen by analyst rather than calibrated: `0.60×last5 PPG + 0.25×last10 PPG + 0.15×season PPG`, separately for for and against on each team. Mean expected Utah points = average(Utah blended for; Lakers blended against) = **113.4325**; expected Lakers = average(Lakers blended for; Utah blended against) = **119.5375**. Total **232.9700** and Lakers signed margin **+6.1050**.

- Utah blended for/against **111.3150/116.1400**; Lakers **122.9350/115.5500**.
- Illustrative Normal SDs 15.43 margin, 19.90 total, borrowed as unqualified NBA broad development-data widths rather than a fitted and validated team-specific model. No 100k simulations, independent calibration, explicit overtime model, covariance or numeric injury effects were run.
- `P(Jazz +11.5)=Φ((11.5−6.1050)/15.43) = 0.6367`; `P(Lakers −11.5)=0.3633`. `P(OVER 229.5)=Φ((232.9700−229.5)/19.90)=0.5692`, under reciprocal **0.4308**.
- Principal Jazz +11.5 failure route: Lakers' concentrated Doncic creation versus injury-depleted Jazz frontcourt generates a 12+ margin. Principal total Over failure: fatigue from both back-to-backs plus major shot creators missing suppresses scoring. Potential increase in Utah variance after a high outlier 132-point game is not quantified. No calibrated Rank-1 or Rank-2 recommendation issued; any seeming high probability below is **uncalibrated and not a validated betting edge**.
- Prospective use: **NOT ADMITTED** absent independently captured official actual first play AFTER all research and GitHub seal push activity. An absent score on a schedule page is *not* evidence sufficient to establish that.

## A4 — Original ONECHAT_V1 block (append-only; never revise after dropping)

<!-- BEGIN ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0011 -->
format: ONECHAT_V1
card_key: 20261118DA6D9F6251746B979F5895FA-G0011
sport: Basketball
competition: NBA
home: Los Angeles Lakers
away: Utah Jazz
scheduled_start: 2026-11-19T14:00:00+11:00
request_at: 2026-11-19T14:05:00+11:00
research_start_at: 2026-11-19T14:08:07+11:00
research_end_at: 2026-11-19T14:12:22+11:00
not_started_source: https://www.nba.com/team/1610612747/lakers/schedule
not_started_observed_at: 2026-11-19T14:10:45+11:00
outcome_exposure: NONE

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,HANDICAP,AWAY,11.5,0.6367,,-6.1050,UNMEASURED,https://www.nba.com/game/uta-vs-lal-0022600268
L1,HANDICAP,HOME,-11.5,0.3633,,6.1050,UNMEASURED,https://www.nba.com/game/uta-vs-lal-0022600268
L2,TOTAL,OVER,229.5,0.5692,,232.9700,UNMEASURED,https://www.nba.com/game/uta-vs-lal-0022600268
L2,TOTAL,UNDER,229.5,0.4308,,232.9700,UNMEASURED,https://www.nba.com/game/uta-vs-lal-0022600268

FACTS
side,field,value,source,observed_at
HOME,season_games,15,https://www.nba.com/team/1610612747/lakers/schedule,2026-11-19T14:10:45+11:00
HOME,season_score_for_pg,122.4667,https://www.nba.com/team/1610612747/lakers/schedule,2026-11-19T14:10:45+11:00
HOME,season_score_against_pg,114.8000,https://www.nba.com/team/1610612747/lakers/schedule,2026-11-19T14:10:45+11:00
HOME,last5_score_for_pg,123.4000,https://www.nba.com/team/1610612747/lakers/schedule,2026-11-19T14:10:45+11:00
HOME,last5_score_against_pg,115.8000,https://www.nba.com/team/1610612747/lakers/schedule,2026-11-19T14:10:45+11:00
HOME,last10_score_for_pg,122.1000,https://www.nba.com/team/1610612747/lakers/schedule,2026-11-19T14:10:45+11:00
HOME,last10_score_against_pg,115.4000,https://www.nba.com/team/1610612747/lakers/schedule,2026-11-19T14:10:45+11:00
HOME,rest_days,0,https://www.nba.com/team/1610612747/lakers/schedule,2026-11-19T14:10:45+11:00
HOME,back_to_back,YES,https://www.nba.com/team/1610612747/lakers/schedule,2026-11-19T14:10:45+11:00
HOME,key_absences,Austin Reaves OUT; Quentin Grimes AVAILABLE,https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-18_08_15PM.pdf,2026-11-19T14:10:45+11:00
HOME,lineup_confirmed,MISSING,No certified starting five independently verified,
HOME,venue,Crypto.com Arena Los Angeles California,https://www.nba.com/game/uta-vs-lal-0022600268,2026-11-19T14:10:45+11:00
HOME,travel_km,MISSING,No measured travel distance to venue,
HOME,opponent_strength,MISSING,No independently calculated opponent strength,
HOME,opponent_strength_method,MISSING,No reproducible opponent adjustment fitted,
HOME,availability_effect,MISSING,No measured point effects of injuries,
HOME,adjustment_basis,MISSING,No quantified lineup rest home or travel adjustment,
HOME,last20_score_for_pg,MISSING,Current season has fewer than twenty completed games,
HOME,last20_score_against_pg,MISSING,Current season has fewer than twenty completed games,
AWAY,season_games,15,https://www.nba.com/team/1610612762/jazz/schedule,2026-11-19T14:10:45+11:00
AWAY,season_score_for_pg,108.7333,https://www.nba.com/team/1610612762/jazz/schedule,2026-11-19T14:10:45+11:00
AWAY,season_score_against_pg,117.2667,https://www.nba.com/team/1610612762/jazz/schedule,2026-11-19T14:10:45+11:00
AWAY,last5_score_for_pg,113.8000,https://www.nba.com/team/1610612762/jazz/schedule,2026-11-19T14:10:45+11:00
AWAY,last5_score_against_pg,116.0000,https://www.nba.com/team/1610612762/jazz/schedule,2026-11-19T14:10:45+11:00
AWAY,last10_score_for_pg,106.9000,https://www.nba.com/team/1610612762/jazz/schedule,2026-11-19T14:10:45+11:00
AWAY,last10_score_against_pg,115.8000,https://www.nba.com/team/1610612762/jazz/schedule,2026-11-19T14:10:45+11:00
AWAY,rest_days,0,https://www.nba.com/team/1610612762/jazz/schedule,2026-11-19T14:10:45+11:00
AWAY,back_to_back,YES,https://www.nba.com/team/1610612762/jazz/schedule,2026-11-19T14:10:45+11:00
AWAY,key_absences,Lauri Markkanen OUT; Jaren Jackson Jr OUT; Jusuf Nurkic OUT; Jaxson Hayes QUESTIONABLE,https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-18_08_15PM.pdf,2026-11-19T14:10:45+11:00
AWAY,lineup_confirmed,MISSING,No certified starting five independently verified,
AWAY,venue,Crypto.com Arena Los Angeles California,https://www.nba.com/game/uta-vs-lal-0022600268,2026-11-19T14:10:45+11:00
AWAY,travel_km,MISSING,No measured travel distance to venue,
AWAY,opponent_strength,MISSING,No independently calculated opponent strength,
AWAY,opponent_strength_method,MISSING,No reproducible opponent adjustment fitted,
AWAY,availability_effect,MISSING,No measured point effects of injuries,
AWAY,adjustment_basis,MISSING,No quantified lineup rest home or travel adjustment,
AWAY,last20_score_for_pg,MISSING,Current season has fewer than twenty completed games,
AWAY,last20_score_against_pg,MISSING,Current season has fewer than twenty completed games,
<!-- END ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0011 -->
<!-- END CANONICAL RESEARCH P-694 -->

<!-- BEGIN RESEARCH ADDENDUM P-694 2026-11-22-settlement-revision-1 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_11.md`, P-694. Source: `research/verification/mini_import_P-686_P-696_2026-11-22-1/SETTLEMENT.md` (P-694); exact settlement block follows.

<!-- BEGIN SETTLEMENT P-694 LOCAL-20261118DA6D9F6251746B979F5895FA-G0011 revision-1 -->
### P-694 · Basketball/NBA Regular Season (game 0022600268) — Utah Jazz @ Los Angeles Lakers · 2026-11-18 PT · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0011` · `NBA:0022600268` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-19T03:14:19Z`; assessment `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (B):** **Utah Jazz 109-97 Los Angeles Lakers** · Linescore: `UTA 29-27-22-31=109; LAL 34-20-22-21=97 (sum check: 29+27+22+31=109, 34+20+22+21=97)`.
- **Permitted source & capture:** `https://www.foxsports.com/nba/utah-jazz-vs-los-angeles-lakers-nov-18-2026-game-boxscore-106753` · capture `2026-11-22/G0011_fox_box.html` (SHA-256 `c855ad9a03274036f90f90482c61e4499d6e72c6b985696424d3fa2d70b244c8`). Corroboration: https://basketball.realgm.com/nba/scores/2026-11-18 (web search corroboration; script blocked).
- **Card-mean Brier / d:** `0.2280` / `+0.0220`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | AWAY | 11.5 | 0.6367 | -6.1050 | UNMEASURED | **WIN** | 0.1320 |
| L1 | NOT_RANKED | HANDICAP | HOME | -11.5 | 0.3633 | 6.1050 | UNMEASURED | **LOSS** | 0.1320 |
| L2 | R2 | TOTAL | OVER | 229.5 | 0.5692 | 232.9700 | UNMEASURED | **LOSS** | 0.3240 |
| L2 | NOT_RANKED | TOTAL | UNDER | 229.5 | 0.4308 | 232.9700 | UNMEASURED | **WIN** | 0.3240 |

**R1–R12 retrospective:** Utah upset the 13-2 Lakers 109-97 (Keyonte George 30/10, Ace Bailey 19; Luka Doncic 10-28 FG / 2-12 3PT for 29, LAL 38.2% FG / 27.3% 3PT on 0-day B2B). Jazz +11.5 (Rank 1, p=0.6367) won by 23.5 pts; Over 229.5 (Rank 2, p=0.5692) lost by 23.5 pts (total 206). Note: sealed 14m19s after scheduled start (request arrived 5m after schedule). All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-009 · P-694 · Over 229.5 (TOP_TOTAL) — Verdict: `MODEL_LIMIT` · Class: `REGIME_IGNORED` (alias `BACK_TO_BACK_FATIGUE_TOTAL_OVER`)**
1. **Contract & trigger:** Over 229.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Utah Jazz 109-97 Los Angeles Lakers (UTA 29-27-22-31=109; LAL 34-20-22-21=97 (sum check: 29+27+22+31=109, 34+20+22+21=97)).
4. **Outcome in frozen distribution & what decided the game:** Card explicitly noted BOTH teams were on the second night of a back-to-back (0 rest days, Jazz flying from Sacramento) yet projected 232.97 (Over 229.5 at p=0.5692) with no fatigue discount. LAL shot 38.2% FG / 27.3% 3PT and both teams committed 41 combined turnovers, finishing 206 (-23.5 vs line).
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `MODEL_LIMIT` (`REGIME_IGNORED` / `BACK_TO_BACK_FATIGUE_TOTAL_OVER`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.
<!-- END SETTLEMENT P-694 LOCAL-20261118DA6D9F6251746B979F5895FA-G0011 revision-1 -->
<!-- END RESEARCH ADDENDUM P-694 2026-11-22-settlement-revision-1 -->

<!-- BEGIN CANONICAL RESEARCH P-695 -->
## P-695 — Basketball/Australia NBL 2026-27 Round 10 — Adelaide 36ers @ Illawarra Hawks · 2026-11-19 AEDT

Canonical retention by prompt-4 import `2026-11-22T06:40:00+00:00`. Scheduled start `2026-11-19T19:30:00+11:00`. Original `20261118DA6D9F6251746B979F5895FA-G0012` (12268 B, SHA-256 `8809933b4a3a4d6137a5efa10be32e11328a27e898840f9c77f01400b3932854`, source `4864f28e3dc2d1fd4a0c07080879df3d82cdd642`, seal `SEALED` at `2026-11-19T08:38:16Z`). Original card follows verbatim; no forecast reissued; Track P scored separately via `ml one-chat score`.

# G0012 — Illawarra Hawks vs Adelaide 36ers — original research card

**Status: RESEARCH_ONLY / NOT CERTIFIED PRE-FIRST-PLAY.** This diagnostic was created **after the official scheduled 19:30 AEDT tip-off**. An independent source for the actual first play is missing; the non-live third-party page's word `Upcoming` is **not** proof the game had not started. No live target-game score was knowingly read or entered. No prospective scoring admission or qualified rank is claimed. The original card must not be retroactively treated as a prediction issued before first play.

## Original request — exact user text preserved

```text
Upcoming Basketball Game: Illawarra Hawks vs Adelaide 36ers, Australia NBL,\
Estimated Game Start Time: 19 November 2026, 7:30 PM AEDT (can be delayed so continue the process as normal)\
\
Hawks +4.5
36ers -4.5\
Combined Total Points: Over/Under 196.5 Points  [$github](app://connector_76869538009648d5b282a4bb21c3d157)
```

## Evidence and custody

- **Card key:** `20261118DA6D9F6251746B979F5895FA-G0012`. **Native official NBL event identifier:** `NBL:illawarra-hawks-v-adelaide-36ers-men-19-11-2026` linked to the unique official event page https://www.nbl.com.au/matches/illawarra-hawks-v-adelaide-36ers-men-19-11-2026 and official match API UUID `3748b33b-58ad-11f1-9f9a-71e9315f7411` from https://schedule.nbl.com.au/match?hide_back=true&league=nbl&match=3748b33b-58ad-11f1-9f9a-71e9315f7411.
- Original user request frozen in `card-drops` commit `499529ed4dd150af118e175a243052151ee88953`; registration workflow `44487993555` returned SUCCESS. The request index and each original `REQUEST.txt`, `EVENT.csv` and `CONTRACTS.csv` file were independently verified on `forecast-seals` **before this research**.
- Official NBL source https://www.nbl.com.au/matches/illawarra-hawks-v-adelaide-36ers-men-19-11-2026 and https://league.nbl.com.au/news/how-to-watch-talking-points-illawarra-v-adelaide-2027: **19 November 2026 19:30 AEDT**, WIN Entertainment Centre, Wollongong; Illawarra HOME, Adelaide AWAY.
- Research started around 19:31:03 AEDT, ended 2026-11-19T19:36:05+11:00. Third-party https://www.nblfixtures.com/games/illawarra-hawks-vs-adelaide-36ers-2026-11-19 still rendered `Upcoming` at observation 19:31:37 AEDT, but states its scores are not live. Official dynamic game centre https://schedule.nbl.com.au/match?hide_back=true&league=nbl&match=3748b33b-58ad-11f1-9f9a-71e9315f7411 returned `Could not load match data`. Neither page verifies actual first-play or delay. Thus this card is ineligible unless **independent retained time evidence** establishes all research and seal events precede actual first play.
- No odds, other people's predictions, price movements or third-party betting analysis were used; `SPORTS_ONLY / MARKET_BLIND`. Only authorised `card-drops` file staging; GitHub `main` read-only.

## Pre-existing completed game history

- Illawarra **5–10** over 15 games, **97.47 scored / 104.73 allowed**; last five **102.00 / 104.00**, last ten **97.60 / 104.70**. Latest five (newest first): L at Perth 100–111 Nov 14 (OT), W vs South East Melbourne 120–110 Nov 11, L at Adelaide 78–106 Nov 7, W at Cairns 107–95 Nov 5, W at Perth 105–98 Oct 31. Sources https://www.nblfixtures.com/teams/illawarra-hawks, https://www.nbl.com.au/club-schedule/ill.
- Adelaide **7–6** over 13 games, **92.92 scored / 92.46 allowed**; last five **99.60 / 95.20**, last ten **93.10 / 94.00**. Latest five: W vs Melbourne 101–93 Nov 12, W vs Illawarra 106–78 Nov 7, L vs Brisbane 89–96 Nov 1, W at New Zealand 108–101 Oct 30, L at South East Melbourne 94–108 Oct 24. Sources https://www.nblfixtures.com/teams/adelaide-36ers, https://www.nbl.com.au/club-schedule/adl.
- **H2H 2026–27:** Illawarra won 114–92 at home on Oct 2, then lost 78–106 in Adelaide on Nov 7. The split is large; the pregame scoring recipe does not treat this as a reliable repeatable margin. The latest 111–100 Illawarra loss at Perth included OT.
- **Rest / venue:** Illawarra last played Nov 14, four full off days; Adelaide last played Nov 12, six full off days; Adelaide enters with more rest while Illawarra returns from a five-game road swing and now plays before a home crowd. Quantitative travel, venue and fatigue impact unavailable.
- **Availability:** Official NBL announcement on Nov 19 https://league.nbl.com.au/news/illawarra-hawks-star-will-hickey-ruled-out-of-crucial-clash-adelaide confirms **Will Hickey OUT through illness** (10.7 PPG and 4.9 APG, not a direct point-impact estimate); Mason Peatling OUT with a foot injury. Official NBL roster report https://league.nbl.com.au/news/how-to-watch-talking-points-illawarra-v-adelaide-2027 lists Adelaide **Bul Kuol OUT** (ACL). Depth charts are **not** confirmed starting fives. No independently measured with/without effects and no supported numeric offset for Hickey.
- **Model missingness:** no full last-20 current-season window; no opponent-adjusted efficiency, verified starting five, measured injury impact, complete play-by-play possession rates, or quantified travel. These limitations disqualify calibrated confidence.

## Transparent unqualified score approximation

For each side, use a declared overlapping weighted scoring/allowing blend: **60% last-five + 25% last-ten + 15% season**. Expected HOME Illawarra points = 0.5 × (Illawarra blended scored + Adelaide blended conceded); expected AWAY Adelaide points = 0.5 × (Adelaide blended scored + Illawarra blended conceded). No lineup, travel or home adjustment applied without evidence.

- Illawarra blended scored/against: **100.220/104.285**; Adelaide **96.973/94.489**.
- Centre: **Illawarra 97.355 – Adelaide 100.629**, combined **197.984**, Illawarra margin **-3.275**.
- Heuristic Normal margin SD 16.08 and total SD 19.38, from the NBL historical development row `Basketball/NBL` in `research/competition_parameters/COMPETITION_PARAMETERS.csv` on governing `main`. Row carries `FIELD_OWNER_ADMISSION_UNVERIFIED` and `HISTORICAL_DEVELOPMENT_UNADMITTED` flags, therefore *not* an independently qualified user predictor. No covariance, Monte Carlo, fitted opponent model or explicit OT branch was executed.
- `P(Hawks +4.5) = Φ((-3.2746+4.5)/16.08) = 0.5304`, `P(36ers -4.5) = 0.4696`; `P(Over 196.5) = Φ((197.9838-196.5)/19.38) = 0.5305`, `P(Under 196.5) = 0.4695`.
- **No Rank-1 or Rank-2 issued.** Both closest sides are approximately 53%, and unmeasured Will Hickey impact could materially change the scoring margin. Primary failure route for Hawks +4.5 is the guard absence and Cotton/Rakocevic shot creation; for Over 196.5, Adelaide controlling pace and repeated Illawarra poor execution would reduce the total. Both estimates are model-only *shadow diagnostics*, not certified prospective probabilities.
- **Result source for future independent settlement:** https://www.nbl.com.au/matches/illawarra-hawks-v-adelaide-36ers-men-19-11-2026. No post-event result was used, and settlement not authorised here.

## ONECHAT_V1 — exact original machine-readable card

<!-- BEGIN ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0012 -->
format: ONECHAT_V1
card_key: 20261118DA6D9F6251746B979F5895FA-G0012
sport: Basketball
competition: Australia NBL
home: Illawarra Hawks
away: Adelaide 36ers
scheduled_start: 2026-11-19T19:30:00+11:00
request_at: 2026-11-19T19:27:00+11:00
research_start_at: 2026-11-19T19:31:03+11:00
research_end_at: 2026-11-19T19:36:05+11:00
not_started_source: https://www.nblfixtures.com/games/illawarra-hawks-vs-adelaide-36ers-2026-11-19
not_started_observed_at: 2026-11-19T19:31:37+11:00
outcome_exposure: NONE

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,HANDICAP,HOME,4.5,0.5304,,-3.2746,UNMEASURED,https://www.nbl.com.au/matches/illawarra-hawks-v-adelaide-36ers-men-19-11-2026
L1,HANDICAP,AWAY,-4.5,0.4696,,3.2746,UNMEASURED,https://www.nbl.com.au/matches/illawarra-hawks-v-adelaide-36ers-men-19-11-2026
L2,TOTAL,OVER,196.5,0.5305,,197.9838,UNMEASURED,https://www.nbl.com.au/matches/illawarra-hawks-v-adelaide-36ers-men-19-11-2026
L2,TOTAL,UNDER,196.5,0.4695,,197.9838,UNMEASURED,https://www.nbl.com.au/matches/illawarra-hawks-v-adelaide-36ers-men-19-11-2026

FACTS
side,field,value,source,observed_at
HOME,season_games,15,https://www.nblfixtures.com/teams/illawarra-hawks,2026-11-19T19:33:46+11:00
HOME,season_score_for_pg,97.4667,https://www.nblfixtures.com/teams/illawarra-hawks,2026-11-19T19:33:46+11:00
HOME,season_score_against_pg,104.7333,https://www.nblfixtures.com/teams/illawarra-hawks,2026-11-19T19:33:46+11:00
HOME,last5_score_for_pg,102.0000,https://www.nblfixtures.com/teams/illawarra-hawks,2026-11-19T19:33:46+11:00
HOME,last5_score_against_pg,104.0000,https://www.nblfixtures.com/teams/illawarra-hawks,2026-11-19T19:33:46+11:00
HOME,last10_score_for_pg,97.6000,https://www.nblfixtures.com/teams/illawarra-hawks,2026-11-19T19:33:46+11:00
HOME,last10_score_against_pg,104.7000,https://www.nblfixtures.com/teams/illawarra-hawks,2026-11-19T19:33:46+11:00
HOME,rest_days,4,https://www.nblfixtures.com/teams/illawarra-hawks,2026-11-19T19:33:46+11:00
HOME,back_to_back,NO,https://www.nblfixtures.com/teams/illawarra-hawks,2026-11-19T19:33:46+11:00
HOME,key_absences,Will Hickey OUT through illness; Mason Peatling OUT foot,https://league.nbl.com.au/news/illawarra-hawks-star-will-hickey-ruled-out-of-crucial-clash-adelaide,2026-11-19T19:33:46+11:00
HOME,lineup_confirmed,MISSING,No verified official starting five available during research,
HOME,venue,WIN Entertainment Centre Wollongong NSW Australia,https://www.nbl.com.au/matches/illawarra-hawks-v-adelaide-36ers-men-19-11-2026,2026-11-19T19:33:46+11:00
HOME,travel_km,MISSING,Actual team travel route distance unverified,
HOME,opponent_strength,MISSING,No computed opponent adjusted schedule strength,
HOME,opponent_strength_method,MISSING,No reproducible opponent strength method fitted,
HOME,availability_effect,MISSING,No measured points impact of confirmed absences,
HOME,adjustment_basis,MISSING,No numeric home rest absence or travel adjustments admitted,
HOME,last20_score_for_pg,MISSING,Current 2026-27 season fewer than twenty completed games,
HOME,last20_score_against_pg,MISSING,Current 2026-27 season fewer than twenty completed games,
AWAY,season_games,13,https://www.nblfixtures.com/teams/adelaide-36ers,2026-11-19T19:33:46+11:00
AWAY,season_score_for_pg,92.9231,https://www.nblfixtures.com/teams/adelaide-36ers,2026-11-19T19:33:46+11:00
AWAY,season_score_against_pg,92.4615,https://www.nblfixtures.com/teams/adelaide-36ers,2026-11-19T19:33:46+11:00
AWAY,last5_score_for_pg,99.6000,https://www.nblfixtures.com/teams/adelaide-36ers,2026-11-19T19:33:46+11:00
AWAY,last5_score_against_pg,95.2000,https://www.nblfixtures.com/teams/adelaide-36ers,2026-11-19T19:33:46+11:00
AWAY,last10_score_for_pg,93.1000,https://www.nblfixtures.com/teams/adelaide-36ers,2026-11-19T19:33:46+11:00
AWAY,last10_score_against_pg,94.0000,https://www.nblfixtures.com/teams/adelaide-36ers,2026-11-19T19:33:46+11:00
AWAY,rest_days,6,https://www.nblfixtures.com/teams/adelaide-36ers,2026-11-19T19:33:46+11:00
AWAY,back_to_back,NO,https://www.nblfixtures.com/teams/adelaide-36ers,2026-11-19T19:33:46+11:00
AWAY,key_absences,Bul Kuol OUT ACL,https://league.nbl.com.au/news/how-to-watch-talking-points-illawarra-v-adelaide-2027,2026-11-19T19:33:46+11:00
AWAY,lineup_confirmed,MISSING,No verified official starting five available during research,
AWAY,venue,WIN Entertainment Centre Wollongong NSW Australia,https://www.nbl.com.au/matches/illawarra-hawks-v-adelaide-36ers-men-19-11-2026,2026-11-19T19:33:46+11:00
AWAY,travel_km,MISSING,Actual team travel route distance unverified,
AWAY,opponent_strength,MISSING,No computed opponent adjusted schedule strength,
AWAY,opponent_strength_method,MISSING,No reproducible opponent strength method fitted,
AWAY,availability_effect,MISSING,No measured points impact of confirmed absences,
AWAY,adjustment_basis,MISSING,No numeric home rest absence or travel adjustments admitted,
AWAY,last20_score_for_pg,MISSING,Current 2026-27 season fewer than twenty completed games,
AWAY,last20_score_against_pg,MISSING,Current 2026-27 season fewer than twenty completed games,
<!-- END ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0012 -->
<!-- END CANONICAL RESEARCH P-695 -->

<!-- BEGIN RESEARCH ADDENDUM P-695 2026-11-22-settlement-revision-1 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_11.md`, P-695. Source: `research/verification/mini_import_P-686_P-696_2026-11-22-1/SETTLEMENT.md` (P-695); exact settlement block follows.

<!-- BEGIN SETTLEMENT P-695 LOCAL-20261118DA6D9F6251746B979F5895FA-G0012 revision-1 -->
### P-695 · Basketball/Australia NBL 2026-27 Round 10 — Adelaide 36ers @ Illawarra Hawks · 2026-11-19 AEDT · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0012` · `NBL:illawarra-hawks-v-adelaide-36ers-men-19-11-2026` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-19T08:38:16Z`; assessment `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (A):** **Illawarra Hawks 103-97 Adelaide 36ers** · Linescore: `ILL 23-23-25-32=103; ADE 26-23-24-24=97 (sum check: 23+23+25+32=103, 26+23+24+24=97)`.
- **Permitted source & capture:** `https://www.nblfixtures.com/games/illawarra-hawks-vs-adelaide-36ers-2026-11-19` · capture `2026-11-22/G0012_nblfixtures.html` (SHA-256 `5f026797ecd8d38c1d0d038524a37f5bd0bc0fc0bc2b66527d274b9e94e1e8a1`). Corroboration: https://www.nbl.com.au/matches/illawarra-hawks-v-adelaide-36ers-men-19-11-2026 (official match page captured in G0012_nbl.html + nbl.com.au recap corroboration).
- **Card-mean Brier / d:** `0.2205` / `+0.0295`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R2 | HANDICAP | HOME | 4.5 | 0.5304 | -3.2746 | UNMEASURED | **WIN** | 0.2205 |
| L1 | NOT_RANKED | HANDICAP | AWAY | -4.5 | 0.4696 | 3.2746 | UNMEASURED | **LOSS** | 0.2205 |
| L2 | R1 | TOTAL | OVER | 196.5 | 0.5305 | 197.9838 | UNMEASURED | **WIN** | 0.2204 |
| L2 | NOT_RANKED | TOTAL | UNDER | 196.5 | 0.4695 | 197.9838 | UNMEASURED | **LOSS** | 0.2204 |

**R1–R12 retrospective:** Illawarra closed with a 32-24 Q4 to win 103-97 (Makur Maker 23/13, Tyler Harvey 22, Milton Doyle 19; Bryce Cotton 28/9). Both Over 196.5 (Rank 1, p=0.5305, total 200) and Hawks +4.5 (Rank 2, p=0.5304) won. Card itself explicitly self-labelled RESEARCH_ONLY / POST_SCHEDULED_START (sealed 8m16s after 19:30 AEDT schedule). All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

**Deep loss review:** None required (Rank 1, top side, and top total all won).
<!-- END SETTLEMENT P-695 LOCAL-20261118DA6D9F6251746B979F5895FA-G0012 revision-1 -->
<!-- END RESEARCH ADDENDUM P-695 2026-11-22-settlement-revision-1 -->

<!-- BEGIN CANONICAL RESEARCH P-696 -->
## P-696 — Cricket/Weber WBBL|12 Match 28 (CA:40648) — Adelaide Strikers Women vs Melbourne Renegades Women · 2026-11-20 AEDT

Canonical retention by prompt-4 import `2026-11-22T06:40:00+00:00`. Scheduled start `2026-11-20T19:10:00+11:00`. Original `20261118DA6D9F6251746B979F5895FA-G0013` (13878 B, SHA-256 `aab54dc69d5b2eb4b1d10f71eab798f51d8799a0618229693c3eb9b903871c69`, source `2df8b196b53c4009a4b15f3c720073f62b5e3f2c`, seal `SEALED` at `2026-11-20T08:07:03Z`). Original card follows verbatim; no forecast reissued; Track P scored separately via `ml one-chat score`.

# Original sports-only G0013 cricket research card — 20261118DA6D9F6251746B979F5895FA-G0013

**Event:** Adelaide Strikers Women (home) vs Melbourne Renegades Women (away), Weber WBBL|12 Match 28, Cricket Australia native `CA:40648`. Official commencement **2026-11-20T19:10:00+11:00** at Adelaide Oval (6:40 PM ACDT); source https://www.cricket.com.au/matches/CA%3A40648/adelaide-strikers-women-melbourne-renegades-women-weber-wbbl-12. Registration is separate from any prospective forecast issuance. Governing repo `danisgreat/Sports-Research` main SHA `cb97bbc2a9f882e7f8a093648b6137315951da8b` read-only, ONECHAT_V1 / DROP-SEAL-v1, SPORTS_ONLY MARKET_BLIND. This immutable original research artifact does **not** claim to have been sealed unless independently verified.

## Owner's original request: frozen exact UTF-8 text

```text
[$github](app://connector_76869538009648d5b282a4bb21c3d157) Upcoming Cricket Game: Adelaide Strikers(W) vs Melbourne Renegades(W), T20 Big Bash Women,\
Estimated Game Time Start: 20 November 2026, 7:10 PM AEDT (can be delayed so continue the process as normal)\
\
\
Renegades(W) 1st Innings Runs at end of 20 overs Total: Over/Under 157.5 Runs\
Renegades(W) 1st Innings Runs at the end of 6 overs: Over/Under 42.5 Runs
```

## Timing and request custody

- Intake approximate local minute: 2026-11-20T18:57:00+11:00; no exact transport timestamp available.
- First request drop commit `6582f3c935a4b5a6d2414a9b8fe4c92d155ed579` on authorised `card-drops`, green CI `seal-drops` run `44698927489`; independently registered in `forecast-seals/research/one_chat/REQUEST_INDEX.csv` and all three immutable original request files read back. Registry branch commit `a90324e58167aa9a59c96f090d87b42cb36dd7cf`, recorded 2026-11-20T18:59:32+11:00. Research began only after green registration, 19:00:00 AEDT.
- Match marked UPCOMING on official Melbourne Renegades fixture site https://www.melbournerenegades.com.au/fixtures during research at approximately 2026-11-20T19:03:40+11:00; official Cricket Australia match centre scorecard https://www.cricket.com.au/matches/CA%3A40648/adelaide-strikers-women-melbourne-renegades-women-weber-wbbl-12 had no target-game live score. No outcome or target-game runs were observed. Actual first ball remains unverified independent of scheduled time.
- Research concluded 2026-11-20T19:05:31+11:00 AEDT. Card drop, GitHub seal, first-play timestamp, and GitHub server push time **NOT** assumed in this original document.

## Exact requested contract scope and settlement uncertainty

- L1 `TEAM_TOTAL`: **Melbourne Renegades Women's own batting innings runs at the end of 20 overs**, Over/Under **157.5**. Includes the team being all-out before 20 overs as terminal runs. If a chase finishes early or rain reduces allocated overs, the 20-over contract settlement is **not independently established**; do not assign a win/loss without the actual operator's rules. This contract is NOT the sum of both teams and NOT the Strikers' innings total.
- L2 `TEAM_TOTAL`: **Renegades Women's own innings runs at the end of six completed overs**, Over/Under **42.5**; a team all-out sooner or reduced-overs match requires settlement rule verification. Not necessarily the game's first match innings. A previous match's powerplay score is a six-over measurement, independent of which innings the team batted.
- No requested winner/handicap lines; no betting prices, markets, external tipster forecasts or in-play target-match data consulted.

## Historical inputs at time of freeze

**Renegades batting 2026 WBBL:** Latest five completed batting innings in chronological descending order (Nov 15, Nov 12, Nov 7, Nov 4, Oct 31): `[156, 129, 188, 155, 136]` runs, average **152.80**. Their six-over scores in the same order `[37, 30, 47, 50, 23]`, average **37.40**. The sixth game Oct 29 is 138 runs and 41 after six overs; whole 2026 season means **150.33** runs per batting innings and **38.00** after six. The Nov 4 chase concluded at 19.5 overs, so 155 is an observed terminal *chase* score, not 120-ball exposure; this is censored for literal end-20 contract. The Nov 15 early updating scorecard mirrored 128/6 at 17.2 overs, but independently displayed published final match summaries show Renegades **156/8 in 20**; the 37 six-over figure was already settled well before the conflicting snapshot.

Pre-event result evidence: 
- Nov 15 156/8 in 20 / six-over 37: https://cricketsix.com/series/12677/wbbl-2026/ and https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/sydney-sixers-women-vs-melbourne-renegades-women-23rd-match
- Nov 12 129 all out / six-over 30: https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/melbourne-renegades-women-vs-sydney-sixers-women-20th-match
- Nov 7 188/3 / six-over 47 versus this opponent: https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/melbourne-renegades-women-vs-adelaide-strikers-women-13th-match
- Nov 4 155/6 (19.5-over chase) / six-over 50: https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/hobart-hurricanes-women-vs-melbourne-renegades-women-9th-match
- Oct 31 136/6 / six-over 23: https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/perth-scorchers-women-vs-melbourne-renegades-women-5th-match
- Oct 29 138/9 / six-over 41: https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/melbourne-renegades-women-vs-sydney-thunder-women-1st-match

**Adelaide bowling context:** Strikers last five outcomes involved opponents scoring Brisbane Heat 184/4, Renegades 188/3, Hurricanes 138/5, Perth 151/9 and Sixers 126/1 in a 15-over winning chase. Opponent innings do **not** represent five full 20-over exposure windows, so no naive average of these as full innings par. The 188 Renegades total in the Nov 7 head-to-head occurred at Junction Oval Melbourne, not Adelaide Oval. Adelaide's latest five batting totals are 170, 152, 139, 202, 124 (mean 157.4), across first and second match innings.

**Availability:** Official Adelaide Strikers injury report dated Nov 19 https://www.adelaidestrikers.com.au/news/4611063/adelaide-strikers-injury-report-19november: fast bowler Darcie Brown **OUT**, spinner Sophie Ecclestone **OUT** (back injuries). Their confirmed absences plausibly affect Renegades run scoring but no measured replacement bowling run effect was fitted. Renegades full game-day playing XI and injury absences not independently confirmed; the Cricket Australia page displays teams to be announced. Toss/batting first also unverified at original cutoff; no invented toss advantage, pitch adjustment, travel distance or opponent-adjusted efficiency.

**Weather:** Australian Bureau of Meteorology hourly forecast https://www.bom.gov.au/places/sa/adelaide-airport/forecast/detailed/ reports roughly **0% rain at 4:30 PM** and **5% at 7:30 PM Adelaide local time**, close to the start/early innings window. Not a guarantee against rain interruption. The venue's comparable WBBL 2026 20-over first-innings par was not verified from a sufficient admitted sample; left MISSING rather than importing a prediction-site 'par'.

## Numeric calculation — uncalibrated small-sample analytical diagnostic

From the five innings only, estimate sample means and sample standard deviations: 20-over mean **152.8000**, sample SD **22.9281**, six-over mean **37.4000**, sample SD **11.3270**. The *illustrative* uninformative-prior Student-t predictive assumption with n=5 uses `df=4`, scale `sample_sd×sqrt(1+1/5)`, giving 20-over scale **25.1165**, six-over scale **12.4081**. This includes sample-mean uncertainty but **does not** capture non-iid changes in opposition strength, actual allocation or major bowler absences. It is NOT a trained, independently calibrated predictive model.

- `P(Renegades runs at 20 overs >157.5) = t.sf((157.5−152.8000)/25.1165,df=4) = 0.4303`. Under side **0.5697**. Score centre ~152.8 runs.
- `P(Renegades runs at 6 overs >42.5) = t.sf((42.5−37.4000)/12.4081,df=4) = 0.3511`. Under side **0.6489**. Score centre ~37.4 runs.
- These are marginal estimates from related innings, not a joint model of the first six overs and full innings. Mathematically the samples are coupled (early score influences final total), but no joint Monte Carlo, validated batting-order player model or covariance was fitted. Explicit playing XI, match toss, innings reduction, bowling attack, field layout and venue mean unresolved.
- Principal failure route of the nominal **Under 42.5** lean is Renegades' explosive openers (one recent 50 powerplay and one 47), combined with missing Adelaide frontline bowlers. For the 20-over Under side, a repeat of the prior 188 against Adelaide or late-innings acceleration breaks it. The incomplete chase and compromised 23rd-match scorecard are additional data-quality limitations.
- Despite Under42.5 estimate **64.9%** exceeding the owner's numerical Rank-1 threshold, it is **NOT qualified for a Ranked pick** without independent calibration, official playing XI and measured availability effects. No claim of a 100k simulation, ML/RL training or independent forecast skill is made.

## Frozen ONECHAT_V1 original block

<!-- BEGIN ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0013 -->
format: ONECHAT_V1
card_key: 20261118DA6D9F6251746B979F5895FA-G0013
sport: Cricket
competition: T20 Big Bash Women
home: Adelaide Strikers Women
away: Melbourne Renegades Women
scheduled_start: 2026-11-20T19:10:00+11:00
request_at: 2026-11-20T18:57:00+11:00
research_start_at: 2026-11-20T19:00:00+11:00
research_end_at: 2026-11-20T19:05:31+11:00
not_started_source: https://www.melbournerenegades.com.au/fixtures
not_started_observed_at: 2026-11-20T19:03:40+11:00
outcome_exposure: NONE

PICKS
label,family,side,line,p,lean,centre,availability_basis,result_source
L1,TEAM_TOTAL,OVER,157.5,0.4303,,152.8000,UNMEASURED,https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/adelaide-strikers-women-vs-melbourne-renegades-women-28th-match
L1,TEAM_TOTAL,UNDER,157.5,0.5697,,152.8000,UNMEASURED,https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/adelaide-strikers-women-vs-melbourne-renegades-women-28th-match
L2,TEAM_TOTAL,OVER,42.5,0.3511,,37.4000,UNMEASURED,https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/adelaide-strikers-women-vs-melbourne-renegades-women-28th-match
L2,TEAM_TOTAL,UNDER,42.5,0.6489,,37.4000,UNMEASURED,https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/adelaide-strikers-women-vs-melbourne-renegades-women-28th-match

FACTS
side,field,value,source,observed_at
HOME,venue_first_innings_avg,MISSING,No source verified a compatible Adelaide Oval womens T20 first innings cohort,
HOME,last5_first_innings_avg,157.4000,https://cricketsix.com/series/12677/wbbl-2026/,2026-11-20T19:03:40+11:00
HOME,last5_powerplay_avg,MISSING,Could not assemble five independently verified Strikers six over scores,
HOME,key_absences,Darcie Brown OUT; Sophie Ecclestone OUT,https://www.adelaidestrikers.com.au/news/4611063/adelaide-strikers-injury-report-19november,2026-11-20T19:03:40+11:00
HOME,lineup_confirmed,MISSING,Official Cricket Australia game page still shows teams to be announced,
HOME,batting_first,MISSING,No authoritative toss choice independently confirmed before research cutoff,
HOME,rain_probability_pct,5,https://www.bom.gov.au/places/sa/adelaide-airport/forecast/detailed/,2026-11-20T19:03:40+11:00
HOME,venue,Adelaide Oval Adelaide Australia,https://www.cricket.com.au/matches/CA%3A40648/adelaide-strikers-women-melbourne-renegades-women-weber-wbbl-12,2026-11-20T19:03:40+11:00
HOME,travel_km,MISSING,No verified measured team travel distance,
HOME,opponent_strength,MISSING,No independent opponent adjusted bowling and batting strength calculation,
HOME,opponent_strength_method,MISSING,No validated opponent strength calculation,
HOME,availability_effect,MISSING,Measured player run impact not available for absences,
HOME,adjustment_basis,MISSING,No measured pace pitch toss or injury run adjustment applied,
HOME,last10_first_innings_avg,MISSING,Only six completed 2026 WBBL team batting innings,
HOME,last20_first_innings_avg,MISSING,Only six completed 2026 WBBL team batting innings,
AWAY,venue_first_innings_avg,MISSING,No source verified a compatible Adelaide Oval womens T20 first innings cohort,
AWAY,last5_first_innings_avg,152.8000,https://cricketsix.com/series/12677/wbbl-2026/,2026-11-20T19:03:40+11:00
AWAY,last5_powerplay_avg,37.4000,https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/melbourne-renegades-women-vs-sydney-sixers-women-20th-match,2026-11-20T19:03:40+11:00
AWAY,key_absences,MISSING,No complete official Renegades match-day absentee report verified,
AWAY,lineup_confirmed,MISSING,Official Cricket Australia game page still shows teams to be announced,
AWAY,batting_first,MISSING,No authoritative toss choice independently confirmed before research cutoff,
AWAY,rain_probability_pct,5,https://www.bom.gov.au/places/sa/adelaide-airport/forecast/detailed/,2026-11-20T19:03:40+11:00
AWAY,venue,Adelaide Oval Adelaide Australia,https://www.cricket.com.au/matches/CA%3A40648/adelaide-strikers-women-melbourne-renegades-women-weber-wbbl-12,2026-11-20T19:03:40+11:00
AWAY,travel_km,MISSING,No verified measured team travel distance,
AWAY,opponent_strength,MISSING,No independent opponent adjusted bowling and batting strength calculation,
AWAY,opponent_strength_method,MISSING,No validated opponent strength calculation,
AWAY,availability_effect,MISSING,Measured player run impact not available for absences,
AWAY,adjustment_basis,MISSING,No measured pace pitch toss or injury run adjustment applied,
AWAY,last10_first_innings_avg,MISSING,Only six completed 2026 WBBL team batting innings,
AWAY,last20_first_innings_avg,MISSING,Only six completed 2026 WBBL team batting innings,
<!-- END ONECHAT_V1 20261118DA6D9F6251746B979F5895FA-G0013 -->
<!-- END CANONICAL RESEARCH P-696 -->

<!-- BEGIN RESEARCH ADDENDUM P-696 2026-11-22-settlement-revision-1 -->
Original: `prediction logs/PREDICTION_LOG_COMBINED_11.md`, P-696. Source: `research/verification/mini_import_P-686_P-696_2026-11-22-1/SETTLEMENT.md` (P-696); exact settlement block follows.

<!-- BEGIN SETTLEMENT P-696 LOCAL-20261118DA6D9F6251746B979F5895FA-G0013 revision-1 -->
### P-696 · Cricket/Weber WBBL|12 Match 28 (CA:40648) — Adelaide Strikers Women vs Melbourne Renegades Women · 2026-11-20 AEDT · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0013` · `CA:40648` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-20T08:07:03Z`; assessment `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (A):** **Melbourne Renegades W 165/4 (20 ov; 32/1 after 6 ov); Adelaide Strikers W 168/5 (19.5 ov)** · Linescore: `Renegades 1st inns: Powerplay (1-6) 32/1 + Middle (7-16) 84/2 + Death (17-20) 49/1 = 165/4 (sum check: 32+84+49=165); Strikers 168/5 (19.5 ov)`.
- **Permitted source & capture:** `https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/adelaide-strikers-women-vs-melbourne-renegades-women-28th-match` · capture `2026-11-22/G0013_sportsguff.html` (SHA-256 `6f023f45466529c3aca35147dc6869c929a2a5e26e348564a24bfddc11bc967a`). Corroboration: https://www.cricket.com.au/matches/CA:40648 (official Cricket Australia captured in G0013_ca.html).
- **Card-mean Brier / d:** `0.2239` / `+0.0261`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | NOT_RANKED | TEAM_TOTAL | OVER | 157.5 | 0.4303 | 152.8000 | UNMEASURED | **WIN** | 0.3246 |
| L1 | R2 | TEAM_TOTAL | UNDER | 157.5 | 0.5697 | 152.8000 | UNMEASURED | **LOSS** | 0.3246 |
| L2 | NOT_RANKED | TEAM_TOTAL | OVER | 42.5 | 0.3511 | 37.4000 | UNMEASURED | **LOSS** | 0.1233 |
| L2 | R1 | TEAM_TOTAL | UNDER | 42.5 | 0.6489 | 37.4000 | UNMEASURED | **WIN** | 0.1233 |

**R1–R12 retrospective:** Renegades started slowly (32/1 after 6 overs, winning Rank 1 Under 42.5 at p=0.6489 by 10.5 runs), then Sophie Molineux (63* off 38) and a 49-run final 4 overs pushed the 20-over total to 165/4, defeating Rank 2 Under 157.5 (p=0.5697). All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-010 · P-696 · Renegades(W) 1st Innings Runs at end of 20 overs Total: Under 157.5 (TOP_TOTAL) — Verdict: `VARIANCE` · Class: `VARIANCE`**
1. **Contract & trigger:** Renegades(W) 1st Innings Runs at end of 20 overs Total: Under 157.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Melbourne Renegades W 165/4 (20 ov; 32/1 after 6 ov); Adelaide Strikers W 168/5 (19.5 ov) (Renegades 1st inns: Powerplay (1-6) 32/1 + Middle (7-16) 84/2 + Death (17-20) 49/1 = 165/4 (sum check: 32+84+49=165); Strikers 168/5 (19.5 ov)).
4. **Outcome in frozen distribution & what decided the game:** Renegades were 32/1 after 6 overs and 34/2 after 7 overs (on track well below 157.5), before Sophie Molineux (63* off 38) and 49 runs in overs 17-20 pushed the total to 165/4 (+7.5 vs line, +12.2 vs 152.8 centre; within 0.5 SD of T20 innings SD approx 25 runs).
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `VARIANCE` (`VARIANCE`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.
<!-- END SETTLEMENT P-696 LOCAL-20261118DA6D9F6251746B979F5895FA-G0013 revision-1 -->
<!-- END RESEARCH ADDENDUM P-696 2026-11-22-settlement-revision-1 -->

<!-- END IMPORT BATCH 2026-11-22 P-686..P-696 20261118DA6D9F6251746B979F5895FA -->
