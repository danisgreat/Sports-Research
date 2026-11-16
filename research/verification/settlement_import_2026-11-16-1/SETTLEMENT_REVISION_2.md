# Settlement revision-2 · 16 November 2026 · P-647, P-661, P-662, P-664, P-678, P-683

Prompt 3 (P-2026.11.16-v25.0), LOCAL_WORKING_TREE, under the owner order of 16 November 2026 (retry the unresolved queue, S-1). It settles the 53 rows left UNRESOLVED by the imports of 14 and 15 November, from the sources the owner's recovery [SRC-RECOVERY-20261116R1](../source_recovery_2026-11-15-1/REPORT.md) located. Every capture named below was re-hashed against [CAPTURE_MANIFEST.csv](../source_recovery_2026-11-15-1/CAPTURE_MANIFEST.csv) and the settling figure re-read from the capture in this run; no blocked page was opened. Result: 26 WIN, 27 LOSS, 0 UNRESOLVED. All rows are chat-local research (NOT_ISSUED, ANALYST_NOT_PRIMARY); the primary count stays zero. One deep loss review (P-662, first lean). Revisions: [SETTLEMENT_REVISIONS.csv](SETTLEMENT_REVISIONS.csv).

<!-- BEGIN SETTLEMENT REVISION P-647 revision-2 -->
### P-647 · Urawa Red Diamonds v Cerezo Osaka · 2026-11-11 · J.League YBC Levain Cup, first leg · revision-2

Original: `prediction logs/PREDICTION_LOG_COMBINED_9.md`, P-647; prior revision revision-1 (rows UNRESOLVED). Effective 2026-11-16T19:22:52+11:00. Rows revised: 3 (1 WIN, 2 LOSS); evidence class A. Every original card, rank, probability and earlier grade is unchanged.

**Verified outcome.** Combined corners 12: Urawa 8, Cerezo 4. Both official club-record tables carry the row of 11 November 2026, YLC, 19:30 JST, Saitama Stadium, 2–0, attendance 10,004, with CK 8 (Urawa's table) and CK 4 (Cerezo's table). The return leg of 15 November is a different row and was not used.

**Source.** Official J.League club pages for [Urawa](https://www.jleague.jp/en/club/urawa/) and [Cerezo Osaka](https://www.jleague.jp/en/club/cosaka/), routes `JLC_URAWA_CK` and `JLC_CEREZO_CK`. Captures `urawa_corners_web_extract.txt` (SHA-256 `764084680edd7b33a3e831a49e9bd3772cf9c77a8a2727cea91c2d510860459c`, 9,039 B, kept outside the repository) and `cerezo_corners_verified_web_extract.txt` (SHA-256 `c97e6502cb41ee0b3faa2a147600509823d723c264b50e98e832d1699a1ad4b5`, 8,542 B, kept outside the repository); hashes re-verified and both dated rows re-read in this run. Official field owner, one lineage: evidence class A.

**Settlement arithmetic.** Over 10.5 corners: WIN (12 > 10.5). Under 10.5 corners: LOSS. 3 rows on two records: 1 WIN, 2 LOSS.

**Deep loss review.** None required. The two losing Under rows are an exploratory row and a legacy v4.12 scenario row; neither is a top side, a top total or a first lean.
<!-- END SETTLEMENT REVISION P-647 revision-2 -->

<!-- BEGIN SETTLEMENT REVISION P-661 revision-2 -->
### P-661 · Hobart Hurricanes Women v Brisbane Heat Women · 2026-11-14 · WBBL|12 · revision-2

Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-661; prior revision revision-1 (rows UNRESOLVED). Effective 2026-11-16T19:22:52+11:00. Rows revised: 10 (5 WIN, 5 LOSS); evidence class C. Every original card, rank, probability and earlier grade is unchanged.

**Verified outcome (threshold bound).** Hobart Hurricanes Women after six completed overs: **23 or 24**. The provider's over-by-over table gives 3+4+3+6+2+5 = 23 for overs 1 to 6 and prints "Powerplay 23/3". Its replayed innings totals 85 against the scorecard's 86, and the page states that one run (a bye or leg bye) was not placed by ball. Wherever that run fell, the six-over score is 23 or 24.

**Source.** [Cricket Field Guide](https://cricketfieldguide.com/match/hobart-hurricanes-women-v-brisbane-heat-women-01m7er2qx1er4sc03wmscpg0h8), route `WBBL_CFG_HOBART_6` (read interactively by the ChatGPT reader, ALLOWED; SCRIPT is blocked and was not used). Capture `hobart_overs_web_extract.txt` (SHA-256 `69d9029d5a9b1ebe566ed77f6e6ab36a2d6ca1263a12bc477adc99a856c731b6`, 14,960 B, kept outside the repository); hash re-verified and the figures re-read from the capture in this run; per-over runs in [research/verification/source_recovery_2026-11-15-1/OBSERVED_OVER_RUNS.csv](../source_recovery_2026-11-15-1/OBSERVED_OVER_RUNS.csv). One provisional feed: evidence class C.

**Settlement arithmetic.** Under 41.5: WIN for both ends of the bound (24 < 41.5, a margin of at least 17.5 runs). Over 41.5: LOSS. 10 rows on five chat cards: 5 WIN, 5 LOSS.

**Deep loss review.** None required. Every card leaned Under 41.5 and won.

**Limit.** The exact six-over score is not asserted. The open Cricsheet WBBL archive reached only 2 November on 15 November (checked through the repository fetcher); when it reaches this match the exact score is checked against this bound.
<!-- END SETTLEMENT REVISION P-661 revision-2 -->

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

<!-- BEGIN SETTLEMENT REVISION P-664 revision-2 -->
### P-664 · Tappara U20 v HPK U20 · 2026-11-14 · Finland U20 SM-sarja · revision-2

Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-664; prior revision revision-1 (rows UNRESOLVED). Effective 2026-11-16T19:22:52+11:00. Rows revised: 24 (12 WIN, 12 LOSS); evidence class C. Every original card, rank, probability and earlier grade is unchanged.

**Verified outcome.** Tappara U20 2–4 HPK U20, Saturday 14 November 2026, 13:00 +02:00, U20 SM-sarja. Periods 1–1, 0–1, 1–2 (home 1+0+1 = 2, away 1+1+2 = 4; sum check passes). The game ended in regulation; total goals 6.

**Source.** [Tulokset](https://tulokset.live/jaakiekko/ottelu/tappara-hpk-2026-11-14-2710291), route `FIN_U20_TULOKSET_FINAL` (SCRIPT reader ALLOWED, checked 2026-11-15T13:08:25+00:00). The page description reads "Tappara – HPK 2–4 la 14.11.2026, U20 SM-sarja (1–1, 0–1, 1–2)". Capture `36fcd7dd8db0541563806d031a76dfdf438cb7db20ed70290feac6401f031a6e.html` (SHA-256 `4ec5e0a14527c1e467aea9f808248f62cc4b42b9184998c083011a05d2919b08`, 550,941 B, kept outside the repository); hash re-verified in this run and the description re-read from the capture. One lineage; the provider's upstream is unknown: evidence class C.

**Settlement arithmetic.** HPK ML: WIN (away side won 4–2 in regulation). Tappara ML: LOSS. Over 5.5 goals: WIN (6 > 5.5). Under 5.5 goals: LOSS. 24 rows on six chat cards: 12 WIN, 12 LOSS.

**Deep loss review.** None required. Every card's ranked rows (HPK ML and Over 5.5) won; the losing rows are the unpreferred complements.

**Limit.** A second permitted lineage was not opened (Leijonat and Elite Prospects were not readable). If one later contradicts this score, a further dated revision follows.
<!-- END SETTLEMENT REVISION P-664 revision-2 -->

<!-- BEGIN SETTLEMENT REVISION P-678 revision-2 -->
### P-678 · Australia v England · 2026-11-15 · second ODI, Adelaide · revision-2

Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-678; prior revision revision-1 (rows UNRESOLVED). Effective 2026-11-16T19:22:52+11:00. Rows revised: 2 (1 WIN, 1 LOSS); evidence class C. Every original card, rank, probability and earlier grade is unchanged.

**Verified outcome.** England 19–1 after five completed overs (first innings). The live report reads "5th over: England 19-1 (Banton 9, Root 0)", preceded by Duckett's wicket at 19–1 and followed by "6th over: England 25-1".

**Source.** The Guardian over-by-over report, route `ODI_GUARDIAN_ENGLAND_5` (read interactively by the ChatGPT reader, ALLOWED at that path). Capture `specific_final_fields_web_extract.txt` (SHA-256 `32fb6e09a1207e1d91d6b6a3300ad89ed9eddb49fc6c1de3681f2b5106795b4e`, 23,100 B, kept outside the repository); hash re-verified and both entries re-read from the capture in this run. The repository agent's own reader is BLOCKED at this path (`ml source-audit`, 16 November) and did not open the page. One media lineage: evidence class C.

**Settlement arithmetic.** Under 26.5: WIN (19 < 26.5). Over 26.5: LOSS. 2 rows on one card.

**Deep loss review.** None required: the losing row (Over 26.5) was the card's second lean, not its top side, top total or first lean.

**Limit.** The open Cricsheet ODI archive had not reached 15 November when checked; it is the second lineage when it does.
<!-- END SETTLEMENT REVISION P-678 revision-2 -->

<!-- BEGIN SETTLEMENT REVISION P-683 revision-2 -->
### P-683 · Kashiwa Reysol v Kawasaki Frontale · 2026-11-15 · J.League YBC Levain Cup · revision-2

Original: `prediction logs/PREDICTION_LOG_COMBINED_10.md`, P-683; prior revision revision-1 (rows UNRESOLVED). Effective 2026-11-16T19:22:52+11:00. Rows revised: 2 (1 WIN, 1 LOSS); evidence class A. Every original card, rank, probability and earlier grade is unchanged.

**Verified outcome.** Combined corners 7: Kashiwa 4, Kawasaki 3. Both official club-record tables carry the row of 15 November 2026, YLC, 17:03 JST, SANKYO F Kashiwa, 5–4, attendance 9,189, with CK 4 (Kashiwa's table) and CK 3 (Kawasaki's table).

**Source.** Official J.League club pages for [Kashiwa](https://www.jleague.jp/en/club/kashiwa/) and [Kawasaki](https://www.jleague.jp/en/club/kawasakif/), routes `JLC_KASHIWA_CK` and `JLC_KAWASAKI_CK`. Captures `specific_final_fields_web_extract.txt` (SHA-256 `32fb6e09a1207e1d91d6b6a3300ad89ed9eddb49fc6c1de3681f2b5106795b4e`, 23,100 B, kept outside the repository) and `club_kawasaki_web_extract.txt` (SHA-256 `e076dea7937d258b4ff9020d256002bffa70669f1bd97edbd09d2af8af1386af`, 8,948 B, kept outside the repository); hashes re-verified and both dated rows re-read in this run. Official field owner, one lineage: evidence class A.

**Settlement arithmetic.** Under 10.5: WIN (7 < 10.5). Over 10.5: LOSS. 2 rows on one card.

**Deep loss review.** None required: the card's lean (Under 10.5) won.
<!-- END SETTLEMENT REVISION P-683 revision-2 -->
