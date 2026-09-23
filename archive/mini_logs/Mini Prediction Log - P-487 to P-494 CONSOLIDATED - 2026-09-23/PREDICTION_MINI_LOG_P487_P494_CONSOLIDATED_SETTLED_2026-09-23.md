# Prediction Mini Log — CONSOLIDATED P-487 to P-494 (games of 22–23 Sep 2026) — settlement and retrospective

**Created:** 2026-09-23 ~21:30 AEST (Australia/Melbourne, UTC+10), by consolidating every local mini log in `Mini logs (to be sent to actual log later)/` into one file, then settling it.
**Last updated:** 2026-09-23 21:46:42 +10:00 (AEST)
**Disposition:** imported to `PREDICTION_LOG_COMBINED_5.md` §"2026-09-23(c)" on 2026-09-23, then archived to `archive/mini_logs/Mini Prediction Log - P-487 to P-494 CONSOLIDATED - 2026-09-23/`. The three live records were carried to `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-495 onward - 2026-09-23/PREDICTION_MINI_RUNNING_LOG_P495_ONWARD.md`, which is their single custodian.
**Method (for settlement):** METHOD.md MDS-2026.09.19-v4.3 / CR-2026.09.21-3; SCORING_AND_VALIDATION.md SCV-2026.09.19-v2; RULES_BASEBALL.md (SFA-BASEBALL, §8.5–§8.8, §9.3–§9.4), RULES_TENNIS.md (§6, §7, §10.6), RULES_BASKETBALL.md (§5, §6); CONTROLS.md; SOURCES.md. Each issued card keeps the method/control version it was issued under.
**Operating mode:** SPORTS_ONLY / MARKET_BLIND. No odds, prices, tipsters, prediction markets or fantasy/DFS material were used in settlement or retrospective.
**Performance status:** **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** No ROI, EV, calibrated-edge or validated-model claim. Every W/L count below is descriptive.
**Drive:** Google Drive was read only, to check the Drive "Mini logs" folder for mini logs not present locally. None was found: Drive holds an older copy of the merged P-482 log and an append file whose P-491 card and walkover record are already local. **No Drive file was created, edited, moved or deleted.**

## 0. Consolidation receipt

### 0.1 What was in the mini-log folder, and what happened to each file

| # | Local file (before this pass) | Bytes | SHA-256 | Content | Disposition |
|---|---|---:|---|---|---|
| 1 | `Mini Prediction Log - P-482 onward - 2026-09-21/PREDICTION_MINI_RUNNING_LOG_P482_ONWARD.md` | 572 | `914503c6…c59d1` | Receipt stub only. Its card content (P-482, P-483) was imported to Part 5 on 2026-09-22; the byte-exact original is already archived. | **Deleted as redundant.** Stub copied to `archive/mini_logs/originals_2026-09-23/STUB_P482_ONWARD_RECEIPT_PRE_CONSOLIDATION_2026-09-23.md` |
| 2 | `Mini Prediction Log - P-484 onward - 2026-09-23/PREDICTION_MINI_RUNNING_LOG_P484_ONWARD.md` | 728 | `88cf046f…a20a` | Receipt stub only; original archived (`…P484_ONWARD_PRE_RECON…`, SHA `a79c9e37…c0a`) | **Deleted as redundant.** Stub archived as `STUB_P484_ONWARD_RECEIPT_PRE_CONSOLIDATION_2026-09-23.md` |
| 3 | `Mini Prediction Log - TMP WTA Singapore Andreeva-Sasnovich - 2026-09-23/PREDICTION_MINI_RUNNING_LOG_TMP_20260923_WTA_SGP.md` | 703 | `de23b997…72a1` | Receipt stub. A peer session had already merged the WTA card into file 4 as P-494 at about 21:10 AEST; original archived (`…TMP_20260923_WTA_SGP_PRE_RECON…`) | **Deleted as redundant.** Stub archived as `STUB_TMP_20260923_WTA_SGP_RECEIPT_PRE_CONSOLIDATION_2026-09-23.md` |
| 4 | `Mini Prediction Log - P-494 onward - 2026-09-23/PREDICTION_MINI_RUNNING_LOG_P494_ONWARD.md` | 77,390 | `aba5f510…87c7` | Carried P-489 (card summary plus R1), P-491, P-493, P-494 (WTA live view), TMP-20260923-NBL-CNS-TAS and the Khonkaen no-forecast disposition | **Consolidated.** Settled records (P-489, P-491, TMP-NBL) and the Khonkaen disposition are in this file; the live records (R1 → TMP-G25, P-493, P-494) were carried as-is to the P-495-onward log. The folder was removed. Byte-exact copy: `archive/mini_logs/originals_2026-09-23/PREDICTION_MINI_RUNNING_LOG_P494_ONWARD_PRE_CONSOLIDATION_2026-09-23.md` |

**Other sources pulled into this consolidation**, because the mini-log files pointed at them or left gaps:

| Source | Bytes | SHA-256 | Why it was needed | Archived copy |
|---|---:|---|---|---|
| `C:\Users\danie\.codex\attachments\8d873c0b…\Pasted text.txt` — the **original P-489 card** | 21,597 | `984eb962…405e` | The mini log carried only a four-line summary of P-489. The full card was only in this external attachment, outside the repository. | `archive/mini_logs/originals_2026-09-23/P489_ORIGINAL_CARD_CODEX_ATTACHMENT_8d873c0b.txt` |
| `C:\Users\danie\.codex\attachments\4c5e0ff5…\Pasted text.txt` — the P-488 card output | 21,962 | `079d9fbb…1b78` | Carries the unregistered **P-487 = Dallas Wings @ Phoenix Mercury** claim and the P-488 cutoff (22 Sep 12:56 AEST) | `archive/mini_logs/originals_2026-09-23/P488_CARD_WITH_P487_WNBA_CLAIM_CODEX_ATTACHMENT_4c5e0ff5.txt` |
| `C:\Users\danie\Documents\Sports Research\PREDICTION_MINI_RUNNING_LOG_MERGED_P482_ONWARD.md` — the predecessor merged log | 181,259 | `942d344e…f8a` | It is the **only** full record of the settled P-484, P-485, P-486, P-488 and P-492 cards and retrospectives. Part 5 has custody rows only, and the P-494 log's "settled index" wrongly pointed back to Part 5. It lived outside the git repository. | `archive/mini_logs/originals_2026-09-23/PREDICTION_MINI_RUNNING_LOG_MERGED_P482_ONWARD_DOCUMENTS_COPY_2026-09-23.md` (the Documents original is left in place) |
| `C:\Users\danie\Documents\Sports Research\PREDICTION_MINI_RUNNING_LOG_P484_ONWARD_SETTLED_2026-09-23.md` | 88,262 | `93adb69b…45dd` | Superseded variant (provisional P-490 mapping); preserved for provenance | `archive/…/PREDICTION_MINI_RUNNING_LOG_P484_ONWARD_SETTLED_DOCUMENTS_COPY_2026-09-23.md` |

Every archived copy was verified against its source's byte length and SHA-256 before any folder was removed.

### 0.2 ID and identity findings made during consolidation

1. **P-489 was two different games merged under one ID.**
   - The original P-489 card is about **22 Sep, game 24** (Azuma v Muller; its own schedule line says "22 Sep 2026, 7:00 PM AEST").
   - The R1 card frozen at 18:59:17 AEST on 23 Sep is about **23 Sep, game 25** (Fukazawa v Nakachi).
   - The 2026-09-23 reconciliation treated R1 as a "same-event reforecast". **Corrected here:** P-489 stays with game 24 (settled below), and R1 becomes `TMP-20260923-NPB-CHU-DB-G25`. P-489 is not reused or overwritten; it keeps the event it was issued on.
2. **P-487 has two claimants.**
   - A WNBA card (**Dallas Wings @ Phoenix Mercury**, 22 Sep 12:00 AEST) was issued as P-487 by the same external session that issued P-484 to P-489 on 22 Sep. Its body was never registered.
   - The NBL card (Cairns v Tasmania, 23 Sep) later claimed P-487 too.
   - Both are held as temporary IDs: `TMP-20260922-WNBA-DAL-PHX` and `TMP-20260923-NBL-CNS-TAS`. P-487 stays **held**. Recommended resolution: P-487 → the WNBA card, by issue order.
3. **P-494** — the WTA Andreeva–Sasnovich **live-issued** view. A peer session assigned it P-494 at about 21:10 AEST. No other claimant exists, so the assignment is retained. It stays outside pregame metrics.
4. **P-491 and P-493** — uncontested; retained.
5. **Khonkaen United v Royal Thai Navy** — no forecast and no ID; a disposition record only.
6. **Next canonical ID remains P-495.** Temporary IDs do not reserve numbers. At reconciliation they take the next free number then available (the P-492 precedent).

### 0.3 Ordering

Entries are ordered by **scheduled game start (AEST)** within each section, as instructed:

| Game start (AEST) | ID / handle | Event |
|---|---|---|
| 22 Sep 12:00 | TMP-20260922-WNBA-DAL-PHX (claims P-487) | Dallas Wings @ Phoenix Mercury |
| 22 Sep 19:00 | P-489 | Chunichi @ Yokohama DeNA (game 24) |
| 23 Sep 18:00 | P-491 | Orix @ Chiba Lotte |
| 23 Sep 19:00 | TMP-20260923-NPB-CHU-DB-G25 (formerly merged into P-489) | Chunichi @ Yokohama DeNA (game 25) |
| 23 Sep 19:30 | P-493 | KIA @ Doosan |
| 23 Sep 19:30 | TMP-20260923-NBL-CNS-TAS (claims P-487) | Cairns v Tasmania |
| 23 Sep ~20:38 (live view frozen 20:51:54) | P-494 | Andreeva v Sasnovich (WTA Singapore) |
| 23 Sep ~21:00 (unverified) | no ID | Khonkaen v Royal Thai Navy — no forecast |

**Heading convention.** Issued cards are reproduced with their text unchanged. Their Markdown heading levels are demoted by two (`#` → `###`) so each card nests under its entry. No selection, probability, rank, reasoning or source was altered.

## 1. Incomplete / Unsettled Logs

**User direction (2026-09-23, during this pass):** events still live are **carried over as-is to the new mini log** and are not settled or retrospected here.

These three records were live at the last check. Their complete issued records, byte-identical to the P-494-onward log, were moved into `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-495 onward - 2026-09-23/PREDICTION_MINI_RUNNING_LOG_P495_ONWARD.md` §1. **That file is now their single custodian**, so they are not duplicated here and cannot drift apart.

| ID / handle | Sport and event | Scheduled start (AEST) | Horizon at issue | State at carry-over (source, time AEST) | Settlement status |
|---|---|---|---|---|---|
| `TMP-20260923-NPB-CHU-DB-G25` (formerly appended to P-489 as "R1"; see §0.2) | NPB Central League — Chunichi Dragons @ Yokohama DeNA BayStars, **23 Sep, game 25** (Fukazawa v Nakachi) | 19:00, 23 Sep | PREGAME: frozen 18:59:17 with the NPB box at 試合開始前 | **LIVE** — 【試合中 7回表】 Chunichi 3, DeNA 3 (NPB box, 21:40); Sports Navi "3 - 3 7回表" (21:40) | Not settled; carried over |
| `P-493` | KBO — KIA Tigers @ Doosan Bears, Jamsil | 19:30, 23 Sep | PREGAME: frozen 19:28:29 | **LIVE** — top 7th, KIA 2, Doosan 2 (KBO English scoreboard, 21:38) | Not settled; carried over |
| `P-494` | WTA 500 Singapore R16 — Mirra Andreeva v Aliaksandra Sasnovich (match LS008) | ~20:35 listed; first ball ≈20:38 | **LIVE-ISSUED** view frozen 20:51:54 (excluded from pregame metrics) | **LIVE** — Andreeva 6-2, 3-2 (WTA feed and ESPN, 21:39) | Not settled; carried over |

**Nothing else is unsettled.** Every other entry in this file reached a verified final and is settled below.

**Custody note on the P-489 / R1 split.** The R1 card keeps every word as issued. Its text calls itself "same-event" and says the canonical ID was "unresolved". The consolidation found it is a **different game** from the P-489 original (§0.2), so it travels under `TMP-20260923-NPB-CHU-DB-G25`. At its own settlement it is graded against the **23 Sep game-25** result: NPB box `npb.jp/scores/2026/0923/db-d-25/`.


## 2. Temporary-ID / Canonical-ID Conflict Logs

These entries are fully settled where final (Phase 8) but keep a temporary ID until the canonical sequence is reconciled. They are ordered by game start.

### TMP-20260922-WNBA-DAL-PHX — WNBA — Dallas Wings @ Phoenix Mercury — 22 Sep 2026 12:00 AEST (claims **P-487**; `BODY_NOT_CARRIED`; partially SETTLED 2026-09-23)

**Why this entry is here.** Two archived Codex session transcripts list a **P-487** card that no repository file carries:
- the P-488 card (archived `P488_CARD_WITH_P487_WNBA_CLAIM_CODEX_ATTACHMENT_4c5e0ff5.txt`);
- the original P-489 card (`P489_ORIGINAL_CARD_CODEX_ATTACHMENT_8d873c0b.txt`).

Both are the same external session's outputs. Its summary row reads:

> `| P-487 | DAL Wings @ PHX Mercury | Mercury +5.5 ~62% | Dallas ~58% |` (P-488 output, cutoff "~22 Sep 2026, 12:56 PM AEST")

That session issued P-484 (WNBA, 22 Sep 10:00 AEST), P-485, P-486, **P-487**, P-488 (cutoff 12:56 AEST 22 Sep) and P-489 (22 Sep 19:00 AEST) in sequence. So **this card is the original P-487 claimant by issue order**. The NBL card (`TMP-20260923-NBL-CNS-TAS`, 23 Sep, 19:30 AEST game) claimed P-487 more than a day later.

The 2026-09-23 reconciliation recorded P-487 as a "noncanonical issue-time hold" and never saw this claimant.

**ID decision in this pass.** Two events claim one number, and only one card body exists in the repository, so neither is promoted:
- P-487 stays **held**;
- the WNBA card gets temporary ID `TMP-20260922-WNBA-DAL-PHX`;
- the NBL card keeps `TMP-20260923-NBL-CNS-TAS`.

**Recommended resolution** (for the operator to confirm): assign **P-487 → Dallas Wings @ Phoenix Mercury** on the issue-order evidence above, and give the NBL card the next free canonical ID at reconciliation. Before promotion, the WNBA card body must be recovered from the external session history. It is `BODY_NOT_CARRIED` here.

#### Identity and state

| Field | Record |
|---|---|
| Event | WNBA regular season, Dallas Wings @ Phoenix Mercury, Mortgage Matchup Center, Phoenix. ESPN event 401857207. |
| Start | 2026-09-21 19:00 MST (UTC−7; Arizona has no DST) = 2026-09-22 02:00 UTC = **2026-09-22 12:00 AEST** |
| Issue horizon | **UNKNOWN**: the card body is not carried. The row existed by 12:56 AEST on 22 Sep, the P-488 cutoff. |
| Terminal state | **FINAL** (ESPN `STATUS_FINAL`, completed: true) |
| Final | **Phoenix Mercury 87, Dallas Wings 86.** Quarters: PHX 19-24-18-26, DAL 26-21-21-18. Kahleah Copper's go-ahead layup came with 2.4 s left. Total 173; margin PHX +1. |
| Records after the game | PHX 16-27; DAL 26-17 (six-game winning streak ended) |
| Result lineages | (1) **ESPN site API** summary (independent data publisher): STATUS_FINAL, 87–86, full box. (2) **Dallas Wings official site** (wings.wnba.com, club/league publisher): "Wings Drop Close Road Game with Mercury, 87-86". (3) **Northeast Valley News** (independent local news, bylined reporter): "Copper scored with 2.4 seconds left, giving Phoenix an 87-86 lead … Phoenix won 87-86". **Gate PASS.** |

#### Settlement of the rows that survive

| Row | Issued | p | Result | Settlement | Brier |
|---|---|---:|---|---|---:|
| Rank #1 (from the summary row) | Mercury +5.5 | ~0.62 | Mercury won by 1 | **WIN** | 0.1444 |
| Projected winner | Dallas Wings | ~0.58 | Mercury won | **INCORRECT** | 0.3364 |
| Ranks #2–#4, totals, reasoning, sources | — | — | — | **`BODY_NOT_CARRIED` — cannot be settled or audited** | — |

**Metrics.** Rank-1 **WIN**. Hit@2, Wins@2, NDCG@2, the top over/under and the decision count are **UNKNOWN** because the ranks below #1 are not carried.

#### Retrospective (limited to what survives)

- **What happened.**
  - Dallas led after the 1st (26–19), at half-time (47–43) and after three quarters (68–61), per ESPN quarter scores.
  - Phoenix won the 4th quarter 26–18, led by Copper (31 points, 16 in the 4th) and Alyssa Thomas's triple-double (15 pts, 11 reb, 12 ast).
  - Paige Bueckers scored 30 and set Dallas's single-season points record (853). Her final three-point attempt missed.
- **Mercury +5.5 won and the Dallas lean lost.** This is internally consistent with a card that expected a close game with a slight Dallas edge.
  - The cushion covered in every Dallas-by-1-to-5 state as well as the Phoenix-win state that occurred.
  - The "Dallas ~58%" winner call lost on a last-second basket. That is **variance on a near coin flip**, not a demonstrable process error.
- **Why nothing more can be said.**
  - No distribution, total row, lineup or availability record is carried.
  - The record-based question — why a 26-17 team was only ~58% against a 16-27 team — cannot be audited without the body.
  - Its rest, lineup and injury reasoning cannot be checked.
- **Mandatory validation questions 1–8:** *cannot be answered*; the body is not carried. This is recorded as an **unauditable record**, not as a process defect (EXTERNAL_LOGGING_WORKFLOW §"2026-09-17(b)" `BODY_NOT_CARRIED` rule).
- **Lesson.** A card that exists only in an external chat transcript leaves the canonical sequence with a hole, and a later card then claims the same ID. See `O-EXTERNAL-ID-CLAIM-SWEEP` in the General Learnings section.

#### Sources

| Source | Link | Contribution |
|---|---|---|
| ESPN WNBA summary API | https://site.api.espn.com/apis/site/v2/sports/basketball/wnba/summary?event=401857207 (opened 2026-09-23 ~21:24 AEST; request sent without a browser User-Agent) | Final, quarters, box, records, attendance 11,941 |
| ESPN WNBA scoreboard | https://site.api.espn.com/apis/site/v2/sports/basketball/wnba/scoreboard?dates=20260921 | Event identity and date (same lineage as above) |
| Dallas Wings official | https://wings.wnba.com/news/wings-drop-close-road-game-with-mercury-87-86 | Final 87–86 (headline, opened) |
| Northeast Valley News | https://nevalleynews.org/21133/sports/copper-scores-go-ahead-basket-with-2-4-seconds-left-lifts-mercury-to-87-86-win-over-dallas/ | Final, 2.4 s layup, Copper 31 / Bueckers 30 (opened via fetch; bylined) |
| Claim evidence | `archive/mini_logs/originals_2026-09-23/P488_CARD_WITH_P487_WNBA_CLAIM_CODEX_ATTACHMENT_4c5e0ff5.txt` (SHA-256 `079d9fbb…1b78`), line 458; `P489_ORIGINAL_CARD_CODEX_ATTACHMENT_8d873c0b.txt` | P-487 summary row and issue sequence |

### TMP-20260923-NBL-CNS-TAS — NBL — Cairns Taipans v Tasmania JackJumpers — 23 Sep 2026, 19:30 AEST (claims **P-487**; card body partly carried) — **SETTLED 2026-09-23 (temporary ID retained)**

**ID status.**
- The card claimed P-487, but a Dallas @ Phoenix WNBA card issued more than 30 hours earlier also claimed it (see `TMP-20260922-WNBA-DAL-PHX`). The NBL card therefore keeps its temporary ID.
- **Recommended resolution:** the next free canonical ID at reconciliation. This card cannot take P-487 by issue order.
- **Card-body status.** The card is a four-row summary table with a rationale paragraph. It has no probabilities, distribution, sources list at issue, freeze timestamp or branch masses. Settlement is possible; the process audit is limited to what the table states.

#### Identity, state and settlement status

| Field | Record |
|---|---|
| Event | NBL27 Round 2, Cairns Taipans (home) v Tasmania JackJumpers, Cairns Convention Centre (venue timezone Australia/Brisbane, UTC+10, the same clock as AEST). NBL match id `36e0818b-58ad-11f1-89d2-fb9d3a8baf78`; ESPN event 401875241. |
| Scheduled start | 19:30 AEST, 23 Sep 2026. **Tip-off about 19:36:09 AEST**: the first live play-by-play event in the official feed is at 09:36:09 UTC. |
| Issue horizon | **PREGAME, bounded — not timestamped.** The card has no freeze time. The append-only 19:34:50 AEST refresh in the same log states "a pregame card is preserved above", so the card existed before tip-off at ≈19:36:09. The bound depends on that refresh's own record; it is not independent proof. |
| Terminal state | Official NBL feed: `match_status = complete`, `status = COMPLETE`, `match_status_string = FINAL`, `display_clock = FINAL`, period 4, clock 00:00, no OT. ESPN: `STATUS_FINAL`, completed true (it lagged the league feed by about 7 minutes and briefly reverted to "In Progress"). Flashscore/Livesport NBL results feed: event `SbVfnAPa`, status code `AB÷3` (finished), listed on the **results** page. |
| Final | **Cairns Taipans 93, Tasmania JackJumpers 87** (regulation; no overtime). Total **180**; margin CNS +6. Quarters (ESPN): CNS 32-13-21-27, TAS 16-28-22-21. It was 45–44 at half-time and 66–66 after three quarters. |
| Team box (ESPN) | CNS 33-75 FG, **14-32 3PT (44%)**, 11-12 FT, 20 AST, 7 TO, largest lead 20. TAS 31-65 FG, 9-30 3PT (30%), **16-26 FT (62%)**, 15 AST, 12 TO, largest lead 4. Official lead tracker: Cairns led for 24:16, Tasmania for 15:47; tied 3 times. |
| Players who decided it | Cairns: Jaylon Brown 20; **Kyrin Galloway 19 off the bench (5-7 3PT in 18 min)**; **Jack McVeigh 17 (starter)**; Pinder 11; Lewis 10 pts/10 reb. Tasmania: Armstrong 20; Johnson 18; Magnay 17 (7-12 FT); Mathias 15 (3-12 3PT); Marshall 13. **Josh Bannan did not play.** |
| Result lineages (CR-4 gate) | (1) **NBL official match data** (league field owner; Sportradar-powered): COMPLETE / FINAL, 93–87, period 4. (2) **ESPN site API** (independent publisher): Final 93–87, quarters, box. (3) **Flashscore / Livesport** results feed (independent data operation): finished, CNS 93 (32/13/21/27), TAS 87 (16/28/22/21). **Gate PASS: three lineages with terminal markers agree.** Caveat: whether ESPN's NBL feed shares the league's data vendor is unverified. Flashscore is a separate collection operation, so the three-lineage requirement holds even if ESPN and the NBL feed are counted as one. |
| Operator terms / contract definition | **Contract inconsistency, unresolved.** The user's prompt said "Under 18.5". The card read it as a clerical error for 186.5 and ranked Under 186.5 and Over 186.5. The 19:34:50 refresh declined to change 18.5 to 186.5 and asked for clarification, which never came. Graded below on **the card's stated contract (186.5)**, with the literal-18.5 alternative shown. The full-game handicap and total include OT by standard basketball convention; no OT occurred. |

#### Settlement

| Rank | As-issued selection (no probability published) | Result | Settlement |
|---:|---|---|---|
| 1 | JackJumpers +2.5 | Lost by 6 | **LOSS** |
| 2 | Combined total Under 186.5 (the card's reading; prompt said "Under 18.5") | 180 | **WIN** as issued. If the contract was literally Under 18.5, it is a LOSS. `CONTRACT_DEFINITION_AMBIGUOUS` is recorded; the research endpoint uses the card's 186.5. |
| 3 | Combined total Over 186.5 | 180 | **LOSS** |
| 4 | Taipans −2.5 | Won by 6 | **WIN** |
| Winner | Tasmania JackJumpers (lean; representative 91–88 TAS) | Cairns won | **INCORRECT** |

**Diagnostics (learning-only; no probabilities, so no Brier).**

| Metric | Value |
|---|---|
| Rank-1 | **LOSS** → enhanced review |
| Hit@2 | **YES** (#2 won on the 186.5 reading; **NO** on the literal 18.5 reading) |
| Wins@2 | 1 / 2 (186.5 reading) |
| NDCG@2 | 0.387 (two winners, #2 and #4; DCG 0.6309 / IDCG 1.6309) on the 186.5 reading |
| Decisions | Two forced pairs (Tasmania +2.5 / Cairns −2.5 is an exact complement at a half-line; so is Over/Under 186.5): **1 W / 1 L** |
| Top over/under | Under 186.5 (#2) — **WIN** on the card's reading; `TOP_OU_REVIEW` not triggered (it **would** be under the literal 18.5 reading) |
| Winner call | **LOSS** |

**Row-geometry note.** #1 and #4 are exact complements (+2.5 / −2.5 at a half point), as are #2 and #3. The four-row card is two decisions, so its row W/L (2 W / 2 L) is **mechanical** (see memory: forced-pair record is mechanical). The honest measures are the two preferred sides: **Tasmania +2.5 lost; Under won.**

#### What happened

- **Q1 32–16 Cairns.** Cairns opened hot from three and reached a 20-point lead at some point in the game (ESPN "largest lead 20").
- **Q2 28–13 Tasmania**, so it was 45–44 at half-time.
- **Q3 even at 66–66.**
- **Q4 27–21 Cairns.** Tasmania's 16-26 free-throw shooting and 3-12 from Mathias limited the comeback.
- **The deciding difference was Cairns' perimeter shooting.** They made 14 threes (44%). Kyrin Galloway (5-7) and Jack McVeigh — neither of whom appears in the card's Cairns roster — supplied 36 of the 93 points.

#### Pick-by-pick causal review

**#1 JackJumpers +2.5 — LOSS (by 6).**
- *Card reasoning:* Roth's defensive discipline; Magnay's rim deterrence; Cairns' "defensive collapse in R1 (surrendered 111 to Sydney)"; Cairns "missing perimeter depth (Galloway, Paul)"; dual cover branches.
- *What was correct.* Tasmania's defence held Cairns to 13 in Q2 and forced a tie after three quarters. Magnay was influential (17 points, 3 blocks).
- *What was wrong.*
  1. **Roster identity.** The card listed Cairns' available players as Pinder, Bruce, Dech, Brown, Bolden, Lewis and Smith.
     - It omitted **Jack McVeigh**, who started and scored 17.
     - It omitted **Kyrin Galloway**, who scored 19 off the bench.
     - "Galloway out" referred to *Jaylin* Galloway. The rotation Cairns actually fielded contained the perimeter depth the card said was missing. The official NBL preview's expected depth chart, verified in this pass, reads "**PF: J.McVeigh / K.Galloway**" and "SG: J.Galloway *(out)*". A same-day NBL article, "Jack be nimble: Baynes demands McVeigh spark" (23 Sep), flagged McVeigh's role. **Both were published pregame.**
  2. **Single-game recency as a rate.** "Surrendered 111 to Sydney in R1" is one game (R-1: recency revises a rate only through a named mechanism).
  3. **A one-sided mechanism.** "Cross-country travel fatigue on 48-hour rest" was applied only to the total (Under). It was not applied to Tasmania's side, although fatigue lowers the travelling side's efficiency (G-L2 bidirectional sign; M11). Tasmania shot 62% from the line.
  4. **Home court unpriced.** The card named the away side as winner without printing a home-court term or a margin distribution.
  5. **Availability error.** "Return: Josh Bannan" was wrong. The official preview listed him out (ribs) and he did not play. The 19:34:50 refresh caught this, but after issue.
- *Driver classification.* Mainly **information and identity error** (roster), plus **model absence** (no distribution; recency as a rate). Variance was secondary: a 6-point margin after a 66–66 tie is within ordinary spread. The roster error removed the players who produced the margin.

**#2 Under 186.5 — WIN (180) on the card's reading.**
- The rationale was Tasmania's deliberate half-court pace, travel fatigue and fewer transition chances. The game went Under by 6.5 despite Cairns' 44% three-point shooting, helped by Tasmania's 62% free-throw shooting and 30% from three.
- The card gave no numbers: no pace, no points per possession, no centre. So it cannot be verified that the Under won *for the card's reason*. Grade: RESULT-RIGHT / PROCESS-UNVERIFIABLE.
- The unresolved contract (18.5 v 186.5) is itself a defect. METHOD §1 says: "Do not silently correct an inconsistent market or event. Flag the issue first." The card did flag it, in a parenthesis, but then graded its own correction. The correct handling was to seek confirmation or issue both readings.

**#3 Over 186.5 — LOSS; #4 Taipans −2.5 — WIN.** Forced complements; no independent information.

**Projected winner — Tasmania — INCORRECT.** See #1.

#### Rank-1 failure review (enhanced)

1. **Why #1?** A cushion with "dual cover branches" on the side the card thought would win.
2. **Justified by pregame information?** **No.**
   - The official NBL expected depth chart and injury list (published before tip; last updated 23 Sep 09:30 AEST) show the Cairns rotation. The card's roster omitted two of Cairns' four top scorers on the night and wrongly returned Bannan.
   - No probability or distribution was computed, so the rank was not derived from a marginal likelihood, which G23.1 requires.
3. **Should another row have ranked higher?** On the card's own reasoning, **Under 186.5 (#2)** had a stated mechanism (pace plus fatigue) that does not depend on the roster error. A compliant process might well have ranked it first. The side pair needed a home-court-adjusted margin distribution that was never built.
4. **Variable missed or mis-weighted.** Cairns' actual rotation (McVeigh, K. Galloway); home court; a travel-fatigue sign applied to one market only; one game of recency as a rate.
5. **Did existing rules cover it?**
   - Yes:
     - RULES_BASKETBALL §7 step 2: "Retrieve official injury/availability status and likely starters before process history";
     - G14.2 / M19 (posted lineup);
     - R-1;
     - G-L2 (bidirectional mechanisms);
     - G23.1 (rank by derived marginal likelihood);
     - METHOD §4 (the six-field object).
   - **None were executed**; the card has no six-field object. It is the clearest **M15** (control listed, not executed) case in this batch.
6. **New rule warranted?** No new rule; the existing rules would have prevented it. One process observation is recorded, **O-ROSTER-NAME-COLLISION**: when an injury note names a player who shares a surname with an active teammate (Jaylin v Kyrin Galloway), print first names and the confirmed active list. It stays an observation until it recurs.

#### Top-two review

- #1 lost, #2 won. They were **anti-coupled** (M18): a Tasmania +2.5 cover state implies a close game, which in basketball raises late fouling and totals; a Cairns separation often comes with runs of made threes, which raise the total. Here Cairns separated and the total still stayed under.
- The ordering was not justified: see the Rank-1 review.
- **Improvement.** Build one margin/total joint from pace and efficiency before ranking, and print `P(R1 ∧ R2)`.

#### Over/under review

| Factor | Card | Actual | Note |
|---|---|---|---|
| Pace / tempo | "Tasmania's deliberate half-court pace" | Possessions not computed; FGA 75 + 65, FTA 38, TO 19 → a moderate pace | Plausible, not quantified |
| Offensive / defensive efficiency | "Cairns defensive collapse in R1 (111 v Sydney)" | Cairns allowed 87 | One-game recency, not a rate (R-1) |
| Venue / travel | Tasmania "cross-country travel, 48 h rest" | Tasmania 62% FT, 30% 3PT | Fatigue plausibly real, but applied to the total only |
| Lineups | Cairns roster wrong (McVeigh, K. Galloway omitted); Bannan wrongly "returning" | Cairns' bench scored 31 | Identity error |
| Market number | 186.5 | 180 | The line sat above an outcome decided by 6.5 points |
| Distribution around the line | Not built | — | No centre, no width: **not auditable** |
| Contract | 18.5 v 186.5 unresolved | — | Definition defect |

**Verdict.** Right side, unverifiable process, contract ambiguity unresolved. This is not evidence for any totals rule.

#### What went right

- The **19:34:50 refresh** did three things right: it corrected the Bannan availability error from the official NBL preview; it refused to issue live picks from an unverifiable live state; and it quarantined an endpoint that exposed bookmaker data. This is the market-blind firewall working.
- The card **flagged** the 18.5/186.5 inconsistency rather than silently rewriting it. The correct next step would have been to confirm it.
- The Under's pace and fatigue mechanism is a sport-appropriate totals driver.

#### Blind spots and future handling

| Blind spot | Knowable pregame? | Impact | Handling | Disposition |
|---|---|---|---|---|
| Cairns rotation misidentified (McVeigh, K. Galloway missing) | **Yes**: the official depth chart listed both at PF | High (36 points) | Build the roster from the official preview/depth chart and the team's last box score; print first names | Existing rule (§7 step 2; G14.2) — **not executed** |
| Bannan "return" asserted | Yes (the official injury list) | Low on the result; high on process | Official injury list first; the card's claim was unsupported | Existing rule |
| Single-game R1 score used as a defensive rate | n/a | Medium | R-1: season or prior-season possessions-based ratings | Existing rule |
| Travel fatigue applied to the total only | Yes | Medium | Apply G-L2 in both directions | Existing rule |
| No distribution or probabilities | Yes | High (rank not derivable) | METHOD §4 six-field object | Existing rule |
| Contract 18.5 v 186.5 | Yes | Definition | Seek confirmation before issue; if unanswered, rank the literal contract and show the reading used | Existing rule (METHOD §1 identity/contract) |
| No freeze timestamp | Yes | Horizon only bounded | Stamp the freeze time on every card | Existing rule (§16.8) |

#### Mandatory validation questions

1. **Confirmed starting lineups?** **No.** Only a partial roster list, which was wrong for Cairns. The NBL does not publish confirmed starting fives much before tip; the official expected depth chart was available and was not used correctly.
2. **Bench / rotation?** **No.** The Cairns bench scorer who decided it (K. Galloway) was not identified.
3. **Coaching?** Scott Roth (Tasmania) was named. Cairns' coaching staff was not, although the official NBL article "Baynes demands McVeigh spark" (23 Sep) described the coach's expectation of McVeigh's role, and that was material. Tactical claims were not quantified.
4. **Injuries and availability?** Partly, with one error (Bannan) that the 19:34:50 refresh corrected.
5. **Sources accurate and current?** The card listed only homepages (nbl.com.au, taipans.com, jackjumpers.com.au) and no exact pages. The refresh's official preview and injury list were accurate.
6. **Better sources?**
   - The NBL official preview/depth chart and injury list.
   - The ESPN NBL summary API (box and lineups; `?dates=` parameter; no browser User-Agent).
   - The NBL match-data endpoint for **settlement only**: status and score fields, parsed so the betting and odds objects are never read.
7. **Blind spots?** Yes; see the table above.
8. **How to account for them?** Execute RULES_BASKETBALL §7 steps 1–2 and METHOD §4 before any rank.

*Not a pregame failure (hindsight-only):* Kyrin Galloway's 5-7 from three; Tasmania's 62% free-throw shooting.

#### Connection to prior lessons

| Lesson | Status |
|---|---|
| M15 (control listed, not executed) | **Recurred — the most severe instance in this batch.** |
| M19 / G14.2 (lineup not retrieved) | Recurred, with the added defect of a *wrong* roster. |
| M11 / G-L2 (a unit mechanism given one sign) | Recurred (travel fatigue). |
| R-1 | Breached (one R1 score as a rate). |
| M18 (anti-coupled top two) | Present, not disclosed. |
| Basketball Rank #1 record | Adds a basketball Rank-#1 loss. It is *not* the P-427 mechanism (qualification), so no pattern claim. |

**G37 grade: RESULT-WRONG / PROCESS-WRONG** (Rank #1); RESULT-RIGHT / PROCESS-UNVERIFIABLE (the Under).

#### Settlement sources

| Source | Link | Lineage | Access (AEST) | Contribution |
|---|---|---|---|---|
| NBL official match data | https://schedule.nbl.com.au/api/calendar/match?match=36e0818b-58ad-11f1-89d2-fb9d3a8baf78&league=NBL | League field owner (data by Sportradar) | OPENED ~21:32; **status and score fields only; the `betting` and `odds` keys were programmatically skipped and never read** | COMPLETE / FINAL 93–87; period 4; tip ≈19:36:09; lead tracker |
| ESPN NBL summary / scoreboard | https://site.api.espn.com/apis/site/v2/sports/basketball/nbl/summary?event=401875241 | Independent publisher; the upstream vendor may overlap with the NBL feed (unverified) | OPENED ~21:28–21:36 (Final) | Quarters; team and player box |
| Flashscore (Livesport) NBL results | https://www.flashscore.com.au/basketball/australia/nbl/results/ (raw feed fields `AB`, `AG`/`AH`, `BA`–`BH`) | Independent data publisher | OPENED ~21:41 | Finished status; 93–87; quarter scores |

<!-- BEGIN VERBATIM ISSUED RECORD: TMP-20260923-NBL-CNS-TAS (heading levels demoted by two; text unchanged) -->

##### TMP-20260923-NBL-CNS-TAS (source card and status corrections follow verbatim; no canonical ID assigned)
##### TMP-20260923-NBL-CNS-TAS — Cairns Taipans vs Tasmania JackJumpers (claimed P-487; unsettled)

| Field | Current audit / pregame record |
|---|---|
| Matchup & Schedule | Cairns Taipans (Home) vs Tasmania JackJumpers (Away), Australia NBL 2026–27 Round 2. Scheduled: 23 September 2026, 7:30 PM AEST, Cairns Convention Centre. |
| Key Rosters & Availability | **Cairns:** Keanu Pinder, Shaun Bruce, Sunday Dech, Jaylon Brown, Jonah Bolden, Malique Lewis, Reyne Smith. *Out/Injured:* Jaylin Galloway (shoulder/arm), Luke Paul.<br>**Tasmania:** David Johnson, Taran Armstrong, Will Magnay, Dakota Mathias, Nick Marshall, Majok Deng, Ben Gold. *Return:* Josh Bannan. |
| Card as supplied | Four-ranked forecast: #1 JackJumpers +2.5; #2 Combined Total Under 186.5 Points (noting prompt text "Under 18.5" as clerical typo); #3 Combined Total Over 186.5 Points; #4 Taipans -2.5. Potential winner: Tasmania JackJumpers (lean, representative score Tasmania 91 – Cairns 88). |
| Event status | UPCOMING / PRE-GAME at issuance verification. Verified against official NBL schedule. No live score, in-game play, or outcome data used. |
| Issue-time integrity | Analysis-only pregame entry; no postgame retrospective or settlement fabricated. Operating under MARKET_BLIND / SPORTS_ONLY rules without odds or fantasy data. |
| Settlement | NOT SETTLED / AWAITING TERMINAL RESULT. Retain all picks unchanged until official final NBL box score. |
| Key Rationale | JackJumpers +2.5 provides dual cover branches (Tasmania outright win + 1–2 pt Cairns win). Scott Roth's defensive discipline and interior rim deterrence (Will Magnay) contrast with Cairns' defensive collapse in R1 (surrendered 111 pts to Sydney). Cairns is missing perimeter depth (Galloway, Paul). Total 186.5 favors Under given Tasmania's deliberate half-court pace, cross-country travel fatigue on 48h rest, and reduced offensive transition opportunities. |

Event identity/status sources: [NBL official schedule](https://www.nbl.com.au/), [Taipans official site](https://www.taipans.com/), [JackJumpers official site](https://www.jackjumpers.com.au/). This event stays in Incomplete / Unsettled Logs.

###### 2026-09-23 19:34:50 AEST research refresh — no new forecast; no retrospective

This is an append-only issue-time status update to the existing event record, not a second forecast and not a result review. At retrieval, the official NBL homepage marked Cairns–Tasmania **LIVE NOW**. The fixture is scheduled for 19:30 AEST at Cairns Convention Centre, but the official Game Centre page returned “Could not load match data.” I could not verify whether play had actually begun, the score, period/clock, possessions, active on-court lineups, fouls/bonus, or rotation minutes. With no reliable live-state feed, the live-state requirements in `RULES_BASKETBALL.md` §5 cannot be met. No new picks or winner are issued from this refresh.

The latest official NBL preview provides an **expected depth chart**, not confirmed starting fives. It lists Cairns absences Jaylin Galloway (shoulder; Round 6) and Luke Paul (ankle; Round 3), and Tasmania absences Ben Ayre (hip flexor; Round 3), Josh Bannan (ribs; TBC), Anthony Drmic (back; TBC), and Bryce Hamilton (ACL; TBC). The official league injury list was updated 23 Sep at 9:30am AEST. The existing roster note above saying “Return: Josh Bannan” is therefore unsupported by the current official preview and is superseded for availability: Bannan was listed out in the expected depth chart and injury section. No confirmed late change or starting five was retrieved.

The submitted total pair is contract-inconsistent as written: **Over 186.5** and **Under 18.5** are not complements. I have not changed 18.5 to 186.5. A clarification is needed before this can be treated as a matched Over/Under decision.

Historical ID custody note (superseded for sequence only): at this 19:34:50 AEST refresh, the earlier P-484/P-487 claims had not been reconciled, so no canonical ID was assigned in that update. The later 2026-09-23 reconciliation resolves the next ID as P-494 and keeps this NBL event under TMP-20260923-NBL-CNS-TAS with P-487 on issue-time hold. No pick, result or retrospective is changed.

Sources checked for this refresh:
- [Official NBL homepage](https://league.nbl.com.au/) — event indicator displayed LIVE NOW at retrieval.
- [Official NBL Game Centre](https://schedule.nbl.com.au/match?from=%2Fnbl%2F2026%3Flogo%3D0&league=NBL&match=36e0818b-58ad-11f1-89d2-fb9d3a8baf78&season=67d4a190-40bc-4bfb-a9a2-11bd0b93f020&year=2026) — exact match page; match data unavailable at retrieval.
- [Official NBL game preview and expected depth charts](https://www.nbl.com.au/news/how-to-watch-talking-points-cairns-v-tasmania-round2).
- [Official NBL injury list](https://www.nbl.com.au/news/nbl26-the-latest-injury-updates) — page states last updated 23 Sep 2026, 9:30am AEST.
- [Taipans official Round 1 injury report](https://www.taipans.com/news/injury-report-round-1-nbl27) and [official Cairns schedule](https://www.taipans.com/schedule) — cross-check of the published availability note and fixture.
- [Official Tasmania club schedule](https://www.nbl.com.au/club-schedule/tas) — fixture and prior-game context.

###### 2026-09-23 19:36 AEST official-feed correction — game in progress; no live forecast

The earlier 19:34:50 status note is supplemented by a raw response observed from the official NBL match-data endpoint: it reported `IN_PROGRESS` / `phase=live`, Cairns 0–Tasmania 0, Q1 9:45 with the clock running, and incomplete on-court data (zero Cairns player records versus five Tasmania player records). **That response is quarantined under the correction below and is not usable evidence**; do not treat its status, score or clock as verified. The NBL homepage displayed `LIVE NOW`, while the browser-readable Game Centre failed to load match data, so exact live score, clock and lineups remain unavailable from an admissible source. The supplied pregame lines cannot be freshly forecast in this unverified live state. The `Under 18.5` contract discrepancy is also unresolved. No picks or winner issued; no retrospective or settlement entered.

Additional source initially checked: [official NBL match-data endpoint for this fixture](https://schedule.nbl.com.au/api/calendar/match?match=36e0818b-58ad-11f1-89d2-fb9d3a8baf78&league=NBL). The full response also contained a separate bookmaker/market object; see the quarantine correction below. No market-derived value was used in forecasting.

###### Data-source quarantine correction

The full JSON response from the NBL match-data endpoint unexpectedly included a separate bookmaker/market object. The initial response was emitted in full before that field was recognized. No price or market-derived value was used in analysis, but this accidental exposure breaches the requested market-blind source boundary. Quarantine that endpoint from forecast evidence; specifically, do not rely on the `IN_PROGRESS` / score / Q1 9:45 snapshot above. Keep it only as a process-integrity receipt. The usable official page-level evidence is the NBL homepage's `LIVE NOW` indicator; the browser-readable Game Centre failed to load data, so exact score, clock and live lineups are unverified for this task. No forecast or retrospective was issued.

Method: local `METHOD.md` MDS-2026.09.19-v4.3 / CR-2026.09.21-3 and `RULES_BASKETBALL.md` SFA-BASKETBALL, especially BK-P2/BK-P3/BK-P4 and §5 live-state requirements. No bookmaker/fantasy/tipster material was used as forecast evidence; inadvertent API exposure is disclosed in the quarantine correction above.

<!-- END VERBATIM ISSUED RECORD: TMP-20260923-NBL-CNS-TAS -->


## 3. Fully Settled Logs (canonical IDs, ordered by game start)

### P-489 — NPB Central League — Chunichi Dragons @ Yokohama DeNA BayStars — **22 Sep 2026, game 24** (SETTLED 2026-09-23)

> **Identity correction made in this pass (read first).** The original P-489 card is about the **22 September** game (game 24 of 25; starters Katsuki Azuma v Kyle Muller). Its own schedule line reads "Correct scheduled start: 22 Sep 2026, 7:00 PM AEST / 18:00 JST", and the NPB box for 22 September confirms Azuma and Muller as the starters. The 2026-09-23 local reconciliation mapped P-489 to the **23 September** game (game 25; Fukazawa v Nakachi) and appended the 18:59:17 AEST "R1" card as a "same-event reforecast". **They are two different events.** P-489 keeps its canonical ID for the event it was issued on (22 Sep). The R1 card is a separate event and moves to the Temporary-ID section as `TMP-20260923-NPB-CHU-DB-G25`. The earlier "ISSUE_HORIZON_UNVERIFIED — conflicts with the official pre-game state" note was caused by checking the 23 Sep page for a 22 Sep card. It is superseded as to event identity, but not as to horizon (see below). No pick, probability or reasoning in either card was changed.

#### Identity, state and settlement status

| Field | Record |
|---|---|
| Event | NPB Central League regular season, Chunichi Dragons (visitor) @ Yokohama DeNA BayStars (home), game 24 of 25. Yokohama Stadium (open air). NPB box `npb.jp/scores/2026/0922/db-d-24/`. |
| Scheduled / actual start | 18:00 JST (UTC+9) on **22 Sep 2026** = 09:00 UTC = **19:00 AEST (Australia/Melbourne, UTC+10), 22 Sep 2026**. NPB: 開始 18:00, 終了 21:26 JST, 3 h 26 min, attendance 33,443. |
| Issue horizon | **START_CROSSED / live state unverified.** The card says "I completed the final research pass just after the scheduled start" and "did not use the live score". The first run scored in the bottom of the 1st. A score-free state is not proof of a pregame freeze. Per RULES_GENERAL §"four distinct fields", live-state-unverified views stay **outside pre-game metrics**. Learning-only whatever the canonical number (same treatment as P-485 and P-492). |
| Terminal state | **FINAL — 【試合終了】** on the NPB official box, retrieved 2026-09-23 21:17 AEST. |
| Final score | **Yokohama DeNA 7, Chunichi 3.** Total **10**; margin DeNA +4. Nine innings; bottom 9th not played (x). |
| Linescore | CHU 020 010 000 — 3 R, 9 H, 1 E. DeNA 301 300 00x — 7 R, 9 H, 0 E. |
| Decisions | W: Azuma (12th win). L: Muller (8th loss). |
| Result lineages (CR-4 gate) | (1) **NPB official box** (league field owner): 試合終了, 7–3, full pitching lines. (2) **Sports Navi / Yahoo! Japan** schedule-result page (independent statistics publisher): "DeNA (勝)東 7 - 3 試合終了 中日 (敗)マラー 横浜". (3) **Kyodo News** via Yahoo! News, "D7―3中（22日） 牧が30号先制2ラン", 9/22 21:37 (independent wire): "DeNAが快勝…東は5回3失点と粘り、今季12勝目。中日のマラーは今季ワースト7失点で8敗目". **Gate PASS: three independent lineages agree on event, date, terminal state and 7–3.** |
| Excluded source | Mynavi News "【プロ野球試合結果】ＤｅＮＡ 7-3 中日" is labelled "※本記事はAIを活用して作成されています" (AI-generated). It omits DeNA's three-run 4th and gives Muller "3回4失点". It is **excluded** from settlement under the synthetic-content rule. The score agrees, but it is not counted as a lineage. |
| Operator terms | Tie, rain and action terms were not supplied (`UNKNOWN_DEFINITION`). No tie or interruption occurred, so every standard rule gives the same grading. NO VALUE DETERMINABLE. |

#### Settlement

| Rank | As-issued selection (`UNVALIDATED_SUBJECTIVE`) | p | Result | Settlement | Row Brier |
|---:|---|---:|---|---|---:|
| 1 | Under 6.5 runs | ~0.62 | 10 runs | **LOSS** | 0.3844 |
| 2 | BayStars ML / outright win (three-way distribution DeNA .60 / CHU .35 / tie .05) | ~0.60 | DeNA won 7–3 | **WIN** | 0.1600 |
| 3 | Dragons +1.5 | ~0.57 | lost by 4 | **LOSS** | 0.3249 |
| 4 | Over 6.5 runs (forced complement of #1) | ~0.38 | 10 runs | **WIN** | 0.3844 (same target as #1; not a separate decision) |
| Winner | Yokohama DeNA BayStars | ~0.60 | DeNA won | **CORRECT** | 0.1600 |

**Decision and ranking diagnostics (learning-only).**

| Metric | Value | Note |
|---|---|---|
| Rank-1 | **LOSS** | Enhanced review below |
| Hit@2 | **YES** | #2 won |
| Wins@2 | **1 / 2** | |
| NDCG@2 | **0.387** | The slate holds two winners (#2, #4), so IDCG@2 = 1.6309; DCG@2 = 0 + 1/log2(3) = 0.6309 |
| Decisions (forced pair counted once) | 3 decisions: total (Under preferred) **L**, DeNA ML **W**, Dragons +1.5 **L** → **1 W / 2 L**; mean decision Brier 0.2898 | |
| Top over/under | Under 6.5 (= Rank #1) — **LOSS** → **`TOP_OU_REVIEW` triggered**; one review covers both triggers |
| Winner call | **WIN** (Brier 0.1600) | |
| Horizon | START_CROSSED → outside pregame metrics | |

#### What happened in the game (process record: NPB box, Kyodo)

- **Bottom 1st, DeNA 3–0.** Watarai reached on a third-base error (三ゴ失). Maki hit a two-run homer to left, his 30th of the season and 8th in September. Furuichi added an RBI single. The error made part of Muller's run total unearned: NPB charges him 7 R but only 4 ER. The per-inning split of unearned runs is not reconstructed here.
- **Top 2nd, 3–2.** Fukunaga's two-run homer.
- **Bottom 3rd, 4–2.** Encarnación's RBI double.
- **Bottom 4th, 7–2.** Naruse doubled, Azuma's bunt went for a fielder's choice, Watarai drove in a run on a fielder's choice and Sano hit a two-run double. **Muller left in the 4th**: 3+ IP, 87 pitches, 19 batters faced, 6 H, 1 HR, 2 BB, 3 K, **7 R (4 ER)**, his season-worst run total per Kyodo.
- **Top 5th, 7–3.** Hanada's sacrifice fly.
- **Innings 6–9: scoreless.** DeNA's bullpen (Wakamatsu, Yoshino, Ise, Sasaki; one inning each) and Chunichi's bullpen (Miyauchi, Kusaka for two innings, Hashimoto, Saito) allowed nothing.
- **Azuma** went 5 IP, 96 pitches, 26 batters faced, 7 H, 1 HR, **4 BB, 1 K**, 3 R/3 ER. He was not sharp but held on. DeNA clinched a Climax Series place.
- **Posted orders.**
  - Chunichi: Fukunaga 2B, Muramatsu SS, Hosokawa LF, Sano 1B, Ishikawa 3B, Hanada RF, Okabayashi CF, Muller P, Kato C.
  - DeNA: Watarai LF, Maki 2B, Sano 1B, Encarnación RF, Miyazaki 3B, Ebina CF, Furuichi C, Naruse SS, Azuma P. Tsutsugo pinch-hit rather than starting.

#### Pick-by-pick causal review

**#1 Under 6.5 — LOSS (10 runs).**

- *What happened.* DeNA scored 7 before the 5th off Muller, with three unearned runs following a third-base error. Chunichi scored 3 off Azuma through a homer and a sacrifice fly. The last five innings were scoreless, so the whole total was set by the starter phase.
- *Correct assumptions.*
  - Both bullpens were effective late: nine scoreless relief innings combined.
  - No weather disruption.
  - Chunichi's scoring was held near the card's 2.2 centre, at 3.
- *Incorrect assumptions.*
  1. **"Muller is also a genuine run-suppression starter" as the centre anchor.** His 2.45 ERA, 0-4-1-2-0 L5 and "2.33 ERA in 3 starts v DeNA" are all one starter-quality channel. The card counted it three times: season ERA, L5 and opponent split. The same was done for Azuma: 2.22 ERA, "33 IP / 3 ER over L5" and "1.85 ERA v Chunichi".
  2. **ERA-based centres omit unearned runs.** ERA excludes unearned runs by definition; team run totals do not. Three of the ten runs here were unearned. An ERA-anchored centre is biased low by construction unless unearned-run mass is added back.
  3. **The team run baselines were never printed.** The card gave W-L records only (66-66-3 v 59-76-2). DeNA scored 3.93 runs per game and Chunichi 3.36 (NPB, through 22 Sep, as printed in the later R1 card), so the two teams' own scoring rates sum to about 7.3 before any starter adjustment. The card's 5.3 centre sat about 2 runs below that without a printed adjustment chain.
- *Driver classification.* **Model weakness (centre construction), plus ordinary in-game variance** (a fielding error, a two-run homer by a 30-HR hitter, and one bad start from a starter with a 4-ER start inside his own L5). Not an unforeseeable shock: the realised state is B2 "early hook" combined with DeNA separation, and both were on the card's own branch list.
- *Weighting.* The most important factor, starter run prevention, was weighted heavily. But it was triple-counted and never reconciled with team run rates or the 1.08–1.11 Yokohama run factor the card itself printed.

**#2 BayStars ML — WIN.**
- The card's case held: Azuma over Muller on current form, home last at-bat, and a stronger season profile.
- DeNA's worked bullpen, which the card treated as widening the upper tail against DeNA, threw four scoreless innings. The feared Chunichi late-relief branch (B5, 13%) never arose because the game was decided by the 4th.
- The card rightly described the bullpen asymmetry as width that kept DeNA near 60%, not as a directional fade.

**#3 Dragons +1.5 — LOSS (by 4).**
- The card explicitly named this kill path: "Low totals do not automatically imply close margins … 4-1, 4-0, 5-2 all lose Dragons +1.5".
- It lost to a high-scoring separation rather than a low-scoring one. Its principal mechanism was the same as #1's: the starter centre was too low, and Muller did not survive.
- Ranking it third, below the ML, was correct on the card's own reasoning.

**#4 Over 6.5 — WIN.**
- Its named mechanisms were "Muller's occasional ordinary/poor-start state", "Yokohama's 1.11 run factor" and "Chunichi's Hosokawa-led home-run threat". The first two operated; the Chunichi homer came from Fukunaga, not Hosokawa.
- As a forced complement it carries no independent information.

**Projected winner — DeNA (~60%) — CORRECT.** The card called it "most likely in a low-scoring one-run game". The winner was right; the game shape was wrong.

#### Rank-1 failure review (enhanced; also `TOP_OU_REVIEW`)

1. **Why it ranked first.**
   - Two strong starters (2.22 and 2.45 ERA), the no-DH Central League, and both starters' 2026 records against this opponent.
   - The Under's 62% sat 2 points above the ML's 60%.
2. **Was that justified on information available before issue?** Only partly.
   - The inputs were real and correctly sourced. The failure is in how they were combined:
     - **Control 26 (mechanism-overlap audit)** requires listing each signed adjustment's channel and justifying a net move of more than one run from the season-prior sum. The card stacked season ERA, L5 and opponent split for each starter, then the no-DH effect, without that line.
     - **§8.6 override 2** requires stating why the joint `BB-B2`/`BB-B3` upper tail is subordinate before an Under outranks its Over. The card gave B2+B3 19% and wrote a kill-path list, but no argument that the tail was subordinate at a 6.5 line.
     - **The §8.5 kill-path library already contains "One ordinary cluster — a multi-run homer or one relief inning — crossing a low line | Under 5.5 / 6.5 at 0.56+"** (origin P-361, NPB). The card's #1 is exactly that contract at 0.62.
   - Illustrative pregame-only arithmetic: anchoring on the teams' own scoring rates, then adjusting for both starters, gives roughly 6.0–6.3. At that centre, P(Under 6.5) is in the mid-50s, which is below the ML. This is indicative only; it is not a fitted number.
3. **Should another row have ranked higher?** On the card's own probabilities the two top rows were near-tied (62 v 60). With an honestly built centre, the ML (#2) would most likely have ranked #1. It also had the broader evidence base: starter gap, home last at-bat and season profile. The ranking error was the centre, not the winner read.
4. **Missed, under-weighted or over-weighted variables.**
   - *Over-weighted:* starter-quality inputs, triple-counted per starter.
   - *Under-weighted:* unearned-run mass; team run rates; the venue run factor. The card printed the factor and then applied "no automatic" adjustment to the centre.
   - *Missed:* DeNA's lineup power in exposure terms. Maki had 30 HR and was not mentioned. BB-P2 was PARTIAL, so no PA-weighted exposure (control 27) was possible.
5. **Did an existing rule cover it, and was it executed?** Yes, and no:
   - control 26;
   - §8.6 override 2;
   - the P-361 kill-path row (§8.5);
   - `G-L9` complement itemisation, which the card did at branch level (B2 9%, B3 10%, B9 4%, extras 8%) but without reconciling it to a team-rate prior.
   - This is the **M15 pattern** (control listed, not executed), with **M3** "totals stacking off one factor" as the specific leak.
6. **New rule warranted?** Not a new rule. Control 26 already covers the stacking; it was not executed. One **observation** is registered in the General Learnings section: **O-NPB-ERA-CENTRE** — an ERA-anchored run centre must add back the unearned-run share and be reconciled with team runs per game before an Under is ranked #1. One game is not evidence of size. Link it to `C-RUN-CENTRE-BIAS`; this card is a data point *against* the historical "centres biased high" direction, which argues for building centres consistently, not tilting them.
7. **Variance share.** Material. A two-run homer after an error, and a 4-run 4th, are within-distribution. But the card's own centre put the realised total at roughly the 95th percentile, and a properly anchored centre would have put it near the 85th–90th. The process defect changed the rank; variance decided the magnitude.

#### Top-two review

- Pick #1 lost; pick #2 won; so Hit@2 = yes and "both won" = no.
- The two were **positively coupled** in the card's own representative state (DeNA 3–2 wins both). The realised state (DeNA by 4, high total) decoupled them: DeNA separation helps the ML and kills the Under.
- The card did not print `P(R1 ∧ R2)` (`G-L10`), although its branch table would have supported it. Branches B1, B4 and B6 win both rows (about 53%); B2 and B9 win the ML and lose the Under.
- **Ordering.** Not justified on an honestly anchored centre; the ML should likely have been #1.
- **Improvement.** When the top two are within 2–3 points and one is a total resting on a starter-derived centre, re-derive the total from team run rates first. This is a disclosure step, not a coefficient.

#### Over/under review

| Factor | Pregame assumption | What happened | Assessment |
|---|---|---|---|
| Scoring environment | Two strong starters; no DH | Muller shelled; Azuma 4 BB / 1 K | Starter channel over-trusted |
| Venue | Yokohama run factor 1.11 (same-league) / 1.08 (all games), HR 1.12 — "not a pitchers' park" | Two homers (Maki, Fukunaga) | Printed but not propagated to the centre |
| Lineups | BB-P2 PARTIAL; Sep 21 cores used | Sano, Maki, Encarnación, Miyazaki drove the runs | PA-weighted exposure not possible (control 27) |
| Defence / unearned | Not modelled | 3 of 10 runs unearned | Structural omission of ERA-based centres |
| Weather | 45–52% shower risk; no automatic Under adjustment | No interruption | Correctly handled as a termination branch, not a signed lean |
| Distribution at the line | Centre 5.3; P(U6.5) 0.62 | 10 | Line sat inside a corridor built too low |
| Sensitivity | "Stop around 62% because of the upper tail" | Upper tail realised | Evidence grade MEDIUM-LOW was right; rank was not |

**Verdict.** The Under was a defensible side at a *lower* probability, but not a defensible #1 over the ML on this construction. This connects to baseball **control 26**, the **P-361 kill-path row** and `C-RUN-CENTRE-BIAS` (NPB leg). No totals-direction rule is proposed.

#### What went right

- **Winner identification**, on the right reasons: the starter gap plus home last at-bat.
- **Bullpen asymmetry as width, not direction.** Correct: DeNA's taxed pen still threw four scoreless innings, and the card had refused to fade DeNA on it.
- **Weather.** A 45–52% shower risk was treated as a termination branch with unknown action terms, not as an automatic Under. This matches RULES_BASEBALL control 18 and the §8.5 "rain after runs" row.
- **Chunichi's venue record (2.0 runs per game at Yokohama)** was kept diagnostic-only. Right: it bundled many starters.
- **The 12-inning tie endpoint and ML tie ambiguity** were disclosed correctly (RULES_BASEBALL §9.3).
- **Refusing to relabel the previous day's batting orders** as today's confirmed orders was correct discipline (BB-P2 PARTIAL). Tsutsugo did not start.

#### Blind spots and future handling

| Blind spot | Knowable pregame? | Impact | Future handling | Rule or observation |
|---|---|---|---|---|
| Starter-quality channel counted three times per starter | Yes | High (decided the rank) | Execute control 26: list channels and print the net versus a team-rate prior | Existing rule, not executed |
| Unearned-run omission in an ERA-anchored centre | Yes (structural) | Medium (3 of 10 runs here) | Add the league unearned-run share when converting ERA to runs, or build from RA/9 | Observation O-NPB-ERA-CENTRE |
| Team runs per game not printed | Yes (NPB BIS) | High | Print both teams' R/G and RA/G before starter adjustment (as P-491 did) | Existing requirement (§8.2 exposure chain; M13) |
| Posted batting orders not retrieved | Probably yes (the NPB box posts スタメン about 1 h before first pitch — P-491 lane) | Medium | Use the NPB box pre-game スタメン fields; else `RETRIEVAL_MISS` and no full-game total at #1 (G14.2) | Existing rule (G14.2; M19) |
| DeNA power exposure (Maki 30 HR) absent | Yes | Medium | PA-weighted exposure for the top of each order (control 27) | Existing rule |
| Start-crossed issuance | n/a | Eligibility | Finish the final refresh before first pitch or label the view LIVE at issue | Existing CR-4 gate |
| Card date/ID identity mis-mapped later (22 v 23 Sep) | Yes, from the card's own schedule line | Custody | Reconcile a card to the event by date **and** starters before any "same event" merge | New process observation O-ID-DATE-STARTER-MATCH |

#### Mandatory validation questions

1. **Confirmed starting lineups?** Starting pitchers: yes (official probables, and correct). Batting orders: **no** — BB-P2 PARTIAL, disclosed. The NPB box posts orders pregame, and the P-491 card later showed this lane works.
2. **Bench, reserve and rotation?** Bullpen workloads from 21 Sep were captured for both sides (good). Benches were not.
3. **Coaching/manager information?** Not retrieved. Not material to this outcome.
4. **Injuries, suspensions, rest and late changes?** Registration moves for 21 Sep were captured (Katsumata up, Takeda down; Ohno down). No injury issue affected the game.
5. **Were sources accurate and current?** Yes, for starters, ERAs and bullpen usage. Baseball Chronicle park factors were used but not propagated. Source quality was not the problem.
6. **Better sources available?**
   - NPB box pre-game スタメン (lineups).
   - NPB BIS team batting/pitching tables (R/G, RA/G).
   - Sports Navi game page (bench and pitcher-v-team).
7. **Blind spots?** Yes; see the table above.
8. **How to account for them?** Execute control 26 and §8.6 override 2 as written; print team run rates; add back unearned runs; retrieve posted orders.

*Not treated as pregame failures (hindsight-only):* Ishikawa's first-inning error; the exact 4th-inning sequence; Azuma's 4-walk command.

#### Connection to prior lessons (Phase 5)

| Lesson / rule | Status here |
|---|---|
| RULES_BASEBALL **control 26** (mechanism overlap) | **Not executed.** This is the main cause. Recurring: P-348, P-356, P-351 (2026-09-11). |
| §8.5 kill path **"one ordinary cluster crossing a low line — Under 5.5/6.5 at 0.56+"** (P-361, NPB) | **Recurred** in the same league and contract family. Recurring sport-specific pattern: **NPB Under 6.5 at #1 has now failed twice (P-361, P-489)**. |
| §8.6 override 2 (why the upper tail is subordinate) | Branch masses given; the subordination argument was not made. |
| `C-RUN-CENTRE-BIAS` (centres historically *above* actuals, 9/12) | This card's centre was 4.7 runs *below* the actual total. It argues for consistent construction, not a directional tilt. |
| `M13` / `G-L7` (aggregate where the disaggregated record exists) | Partly honoured: game logs were printed for both starters. But team scoring rates were never opened. |
| `M3` (totals stacking off one factor) | **Recurred.** |
| `M19` / `G14.2` (posted lineup not retrieved) | **Recurred** (BB-P2 PARTIAL, with a full-game total at #1). |
| START_CROSSED issuance (P-485, P-492) | **Recurred.** The same external session issued P-485, P-489 and P-492 at or after the start. |

**G37 grade: RESULT-WRONG / PROCESS-WRONG IN PART.** The winner process was right; the Rank-1 total construction breached controls 26 and G14.2.

#### Settlement sources (P-489)

| Source | Link | Field ownership | Access / time (AEST) | Contribution | Limitation |
|---|---|---|---|---|---|
| NPB official box | https://npb.jp/scores/2026/0922/db-d-24/box.html | League field owner | OPENED (raw HTML), 2026-09-23 21:17 | 試合終了; linescore; batting and pitching lines; start/end/attendance | Muller IP shown as "3 +" |
| Sports Navi schedule/results | https://baseball.yahoo.co.jp/npb/schedule/?date=2026-09-22 | Independent statistics publisher | OPENED, 21:20 | 7–3 試合終了; W 東 / L マラー | Summary line only |
| Kyodo News via Yahoo! News | https://news.yahoo.co.jp/articles/6c2748829a9e4c55b2b35b6b0caa76432e3f2066 | Independent wire | OPENED, 21:23 | Final; Maki's 30th HR; Azuma 5 IP 3 R W12; Muller season-worst 7 R, L8 | Wire copy; also syndicated elsewhere (counted once) |
| Mynavi News (excluded) | https://news.mynavi.jp/article/20260922-baseball_game02/ | AI-generated summary | OPENED, 21:23 | — | **Excluded**: AI-generated; omits the 4th-inning runs |
| Original card | `archive/mini_logs/originals_2026-09-23/P489_ORIGINAL_CARD_CODEX_ATTACHMENT_8d873c0b.txt` (SHA-256 `984eb962…405e`) | Issued card | Read 2026-09-23 | Card text, ranks, probabilities, branch table | Contains unresolved `:chatgpt-content-reference` tokens; source URLs not recoverable |

#### Original P-489 card (complete Codex attachment, text byte-identical except that Markdown heading levels are demoted by two so the card nests under this entry; the embedded mini-log snapshot is part of the attachment and is also the P-487 claim evidence)

<!-- BEGIN VERBATIM ISSUED RECORD: P-489 original card (Codex attachment 8d873c0b) (heading levels demoted by two; text unchanged) -->

### Chunichi Dragons @ Yokohama DeNA BayStars — NPB

The first correction is the start time: **NPB lists this game for 18:00 JST, which is 7:00 PM AEST**, not 7:40 PM. The official probable starters are **Katsuki Azuma for DeNA and Kyle Muller for Chunichi**. :chatgpt-content-reference{index="0"}

I completed the final research pass just after the scheduled start. I used only information that was pregame-relevant, such as confirmed starters, roster status and prior bullpen workloads. **I did not use the live score, hits, outs, inning state or any in-game performance.**

#### Final ranking

| Rank | Pick | Estimated sporting probability* | Evidence |
|---|---|---:|---|
| **1** | **Under 6.5 runs** | **~62%** | **MEDIUM-LOW** |
| **2** | **BayStars ML / outright win** | **~60%** | **MEDIUM-LOW** |
| **3** | **Dragons +1.5** | **~57%** | **MEDIUM-LOW** |
| **4** | **Over 6.5 runs** | **~38%** | LOW / forced complement |

##### Potential game winner
#### **Yokohama DeNA BayStars — ~60% outright**

My approximate three-way sporting distribution is:

**DeNA ~60% | Chunichi ~35% | Draw ~5%**

##### Representative score
#### **BayStars 3 – Dragons 2**

That central score simultaneously gives:

- **Under 6.5 ✅**
- **BayStars outright ✅**
- **Dragons +1.5 ✅**
- Over 6.5 ❌

\*These are `UNVALIDATED_SUBJECTIVE` research probabilities, not calibrated betting probabilities. The current Drive has **no fitted and validated NPB model**.

---

#### 1. Methodology and the NPB moneyline issue

This forecast uses the current Drive framework, **MDS-2026.09.19-v4.3 / CR-2026.09.21-3**, `SFA-BASEBALL`, with the supplied betting lines quarantined until after the sporting run distribution was constructed.

There is an important NPB-specific contract issue. In the **2026 regular season, games can continue through 12 innings and then finish tied**. Unlike MLB, a draw is therefore a genuine terminal result. The exact operator's treatment of a tie on **“BayStars ML”** was not supplied.

So:

- my **~60%** means DeNA **wins the sporting event outright**;
- I am **not** claiming your operator necessarily settles an NPB draw as a loss, push or void;
- exact moneyline value therefore remains `UNKNOWN_DEFINITION / NO VALUE DETERMINABLE`.

That distinction is required by the Drive methodology.

---

### 2. Starting pitching is the strongest reason for the Under

#### Katsuki Azuma — DeNA

Official NPB figures entering today:

- **11-5**
- **2.22 ERA**
- **150 IP**
- 121 hits
- just **21 walks**
- 116 strikeouts
- 11 HR allowed. :chatgpt-content-reference{index="1"}

His recent five-start block has been exceptionally stable:

| Date | Opponent | IP | ER |
|---|---|---:|---:|
| Sep 15 | Giants | 6.0 | 2 |
| Sep 8 | Yakult | 7.0 | **0** |
| Sep 2 | Giants | 7.0 | 1 |
| Aug 26 | Hiroshima | 6.0 | 0 |
| Aug 19 | Giants | 7.0 | **0** |

That is **33 innings and only three earned runs** across those five outings. :chatgpt-content-reference{index="2"}

His September 8 start is particularly relevant mechanically rather than just statistically: he went **seven scoreless innings, five hits, two walks and six strikeouts**. :chatgpt-content-reference{index="3"}

##### Against Chunichi

A secondary current-season split database has Azuma at approximately:

- **6 starts**
- **39 IP**
- **1.85 ERA**
- 23 hits
- 7 walks
- 27 strikeouts
- **0.77 WHIP**

against Chunichi in 2026. :chatgpt-content-reference{index="4"}

I do **not** treat that as six independent confirmations. The same opponent roster appears repeatedly and lineups change. But it supports the broader mechanism already visible in Azuma's current form: he limits free baserunners and is difficult to turn over for clustered innings.

---

### 3. Kyle Muller is also a genuine run-suppression starter

Muller is not simply the weaker pitcher in a "DeNA ace vs ordinary Chunichi starter" setup.

Official NPB figures:

- **7-7**
- **2.45 ERA**
- **117⅓ IP**
- 97 hits
- 24 walks
- 93 strikeouts
- 10 HR. :chatgpt-content-reference{index="5"}

His recent five starts:

| Date | Opponent | IP | ER |
|---|---|---:|---:|
| Sep 14 | Hanshin | **9.0** | **0** |
| Sep 5 | Yakult | 6.0 | 4 |
| Aug 29 | DeNA | 6.0 | **1** |
| Aug 22 | Yakult | 7.0 | 2 |
| Aug 15 | Giants | 7.0 | **0** | :chatgpt-content-reference{index="6"}


The latest start was especially strong: **nine scoreless innings on 106 pitches**, seven hits and only one walk against Hanshin. :chatgpt-content-reference{index="7"}

##### Against DeNA

A current-season split database has Muller at:

- 3 starts
- **19⅓ IP**
- **2.33 ERA**
- 13 hits
- just 2 walks
- 13 strikeouts

against DeNA. :chatgpt-content-reference{index="8"}

On August 29 at this same venue, Muller gave DeNA **six innings of one-run baseball** in a 1-0 Dragons loss.

That materially strengthens the Under rather than merely serving as generic recent form.

---

### 4. Central League rules also lower the ordinary scoring baseline

This is a **Central League regular-season game**.

In 2026, the Central League still **does not use the designated hitter**. The DH starts there in 2027.

That means both starting pitchers occupy lineup spots tonight.

Ordinarily this reduces offensive depth.

There is one amusing but legitimate wrinkle: **Muller is unusually useful with the bat for a pitcher**. Official NPB records show him hitting:

- **8-for-40**
- **2 home runs**
- **10 RBI**
- .200/.200/.425. :chatgpt-content-reference{index="9"}

He even hit a two-run homer and two-run double while throwing his shutout against Hanshin.

So I do not model Chunichi's pitcher spot as quite the normal automatic offensive sink. It still does not remove the overall no-DH suppression mechanism.

---

### 5. Lineup availability: important limitation

The official NPB and club feeds confirmed the starting pitchers, but I did **not recover a reliable source exposing both final nine-man starting orders before issuance**.

A game-information feed explicitly said the starting members would be updated around 30 minutes before first pitch, but its indexed version still had the field blank when retrieved. :chatgpt-content-reference{index="10"}

Therefore `BB-P2` is **PARTIAL / NOT RETRIEVED**.

I will not relabel yesterday's batting orders as today's confirmed orders.

The current regular cores are nevertheless clear. Chunichi's September 21 lineup included **Fukunaga, Muramatsu, Hosokawa, Sano, Ishikawa, Hanada, Okabayashi and Ishii**, while DeNA's September 21 lineup contained **Watarai, Maki, Tsutsugo, Encarnacion, Sano and Ebina** among its first six. :chatgpt-content-reference{index="11"}

Because today's exact batting slots/catcher combinations were not recovered from a primary source, **none of my picks receives a HIGH evidence grade**.

---

### 6. Availability and roster changes

NPB does not publish an NFL-style injury report. The correct current-availability hierarchy is roster registration/deregistration plus team reporting.

On September 21:

- DeNA registered **Katsumata** and deregistered pitcher **Takeda**.
- Chunichi deregistered starter **Yudai Ohno** after his turn. :chatgpt-content-reference{index="12"}

Nothing there changes today's Azuma-Muller matchup.

The bigger late-game availability difference comes from **bullpen workload**.

---

### 7. Bullpen condition strongly favors Chunichi late

This is an important counterweight to DeNA's starter advantage.

#### DeNA bullpen

Yesterday's 3-2, 11-inning loss to Hanshin required:

- Naoki Wakamatsu: 18 pitches
- **Hiromu Ise: 11**
- Hamachi: 16
- **Reynolds: 16**
- Yoshino: 15
- Nakagawa: 9

after the starter departed. :chatgpt-content-reference{index="13"}

So DeNA used **six relievers**, including important leverage arms, and played 11 innings.

That does not mean they are unavailable tonight. It means expected late-game quality and availability have to be widened.

This is one reason I am not making DeNA ML a 65-70% selection.

#### Chunichi bullpen

Chunichi had a much easier bullpen day yesterday.

Hiroto Takahashi went **seven scoreless**, and only **Haruki Miyauchi and Sakurai** were required to cover the eighth and ninth. :chatgpt-content-reference{index="14"}

Closer **Shinya Matsuyama**, who has 30 saves, was not needed in the 10-0 win after having recorded his 30th save on September 20. :chatgpt-content-reference{index="15"}

##### Consequence

**Starter innings:** meaningful DeNA advantage.

**Late bullpen condition:** meaningful Chunichi advantage.

That is a large reason **Dragons +1.5 remains competitive** despite DeNA being my outright winner.

---

### 8. Recent offensive form: useful for dispersion, not direction

The Drive forbids using one or two high-scoring games as evidence that an offence has permanently changed.

That matters especially for Chunichi.

Their recent sequence includes:

- 1-0 win
- 6-0 win
- 4-1 win
- 0-2 loss
- **1-14 loss**
- **8-5 win**
- **10-0 win**. :chatgpt-content-reference{index="16"}

That is enormous dispersion.

The 10-run game yesterday does **not** cause another high-scoring game tonight. It came against a completely different starting-pitcher environment.

DeNA's recent results are similarly mixed, including 13-2, 2-1, 1-3, 5-3, 1-8 and 2-3. :chatgpt-content-reference{index="17"}

So I preserve **run-cluster upper tails**, but the current starters control the centre.

---

### 9. Yokohama Stadium pushes back against the Under

This is the strongest environmental argument against Pick #1.

Yokohama Stadium has been a **hitter-friendlier Central League venue in 2026**.

Current park factors:

- HR factor: **1.12**
- run factor: **1.11** for same-league games
- all-games run factor: **1.08**. :chatgpt-content-reference{index="18"}

So I am **not** treating Yokohama as a pitchers' park.

That prevents the Under from getting into a 65-70% type range.

##### Current venue matchup diagnostic

In the 2026 data through the latest update, Chunichi at Yokohama is:

- **2-8-1**
- batting about .189
- **22 runs in 11 games**, roughly 2.0/game. :chatgpt-content-reference{index="19"}

That supports a low Chunichi centre, but I treat it only as diagnostic because it bundles many different starters and batting orders.

---

### 10. Weather

Current pregame conditions carried a meaningful shower/interruption possibility. Around the game window, the retrieved forecast showed roughly **45-52% precipitation probability**, humid conditions and temperatures in the mid-20s Celsius.



::chatgpt-content-reference{index="20"}



NPB's schedule itself described the Yokohama weather broadly as cloudy with some sun. :chatgpt-content-reference{index="21"}

I did **not** retrieve an authoritative field-relative wind vector.

Therefore:

- no automatic rain = Under adjustment;
- no unsupported wind/home-run adjustment;
- weather adds a **termination/delay and pitcher-rhythm uncertainty branch**.

Because your operator's rain/suspension action rules were not supplied, that branch remains `UNKNOWN_DEFINITION`.

---

### 11. Independent run tree

Built before querying the 6.5 total and the supplied sides.

##### `P-489-NPB-joint-v1`
**`UNVALIDATED_SUBJECTIVE`**

| Branch | Weight | Representative state | Mechanism |
|---|---:|---|---|
| **BB-B1 starter-control centre** | 32% | DeNA 3-2 | Azuma/Muller both work deep |
| **BB-B2 early hook** | 9% | DeNA 5-4 | one starter loses command/HR cluster |
| **BB-B3 sequencing/HR cluster** | 10% | Chunichi 5-3 | Yokohama park + right-handed power beats the starter centre |
| **BB-B4 low opponent floor** | 12% | DeNA 4-0 | Azuma controls Chunichi and DeNA creates separation |
| **BB-B5 relief transition** | 13% | Chunichi 3-2 | DeNA's worked bullpen loses a late one-run state |
| **BB-B6 home ninth suppressed** | 9% | DeNA 3-1 | DeNA leads after 8½ and does not bat ninth |
| **BB-B7 extra innings / tie** | 8% | 2-2 / 3-2 state | no automatic runner; game can end tied after 12 |
| **BB-B8 weather interruption** | 3% | action-dependent | interruption/restart/shortening uncertainty |
| **BB-B9 late separation** | 4% | DeNA 5-2 | close starter phase expands after relief transition |

##### Integrated sporting distribution

My best estimate is approximately:

- **DeNA: 60% outright**
- **Chunichi: 35% outright**
- **tie: 5%**
- projected DeNA runs: **~3.1**
- projected Chunichi runs: **~2.2**
- total centre: **~5.3 runs**
- **Under 6.5 ~62%**
- **Over 6.5 ~38%**
- **Dragons +1.5 ~57%**

These probabilities include broader score variation inside each branch; the representative score is not assumed to occur exactly.

---

### 12. Why Under 6.5 is #1

#### **Under 6.5 — ~62%**

This is the most robust sporting contract because the central path has **two legitimate run-prevention starters**.

At 6.5:

- DeNA 3 + Chunichi 3 = Under
- DeNA 4 + Chunichi 2 = Under
- DeNA 3 + Chunichi 2 = comfortably Under
- 4-3 or 5-2 is enough to lose it.

##### Main supporting mechanisms

**Azuma:** 2.22 season ERA and outstanding current five-start run prevention. :chatgpt-content-reference{index="22"}

**Muller:** 2.45 season ERA, with 0, 4, 1, 2, 0 earned runs across his most recent five starts. :chatgpt-content-reference{index="23"}

**No DH:** pitchers bat in the 2026 Central League.

**Direct opponent history:** Azuma and Muller have both prevented runs effectively against today's opponent this season. :chatgpt-content-reference{index="24"}

##### Kill paths

The Under can still fail through:

1. Yokohama's hitter-friendly HR environment;
2. Hosokawa/Sano/right-handed Chunichi power finding Azuma;
3. Muller's less dominant 4-run branch;
4. a taxed DeNA bullpen;
5. one multi-run relief inning;
6. extra innings;
7. weather disrupting starter rhythm rather than suppressing scoring.

That upper tail is why I stop around **62%**.

---

### 13. Why BayStars ML is #2

#### **BayStars outright — ~60%**

DeNA has three meaningful advantages:

**Azuma > Muller**, although the gap is not huge on current form.

**Home last bat**, which is particularly valuable in a low-scoring close game.

**Stronger season-level team profile:** DeNA enters **66-66-3**, while Chunichi is **59-76-2**. :chatgpt-content-reference{index="25"}

Azuma has also been extremely effective against Chunichi during the current season.

##### Why it isn't #1

Muller is genuinely pitching well, and **DeNA's bullpen is considerably more worked than Chunichi's**.

The most likely BayStars-loss mechanism is not a blowout. It is:

> Azuma and Muller both pitch well, the game reaches the seventh/eighth tied or within one, and Chunichi has the fresher leverage chain.

That is a real enough branch to keep DeNA around 60%.

And again, the **operator's ML tie rule is unknown**.

---

### 14. Why Dragons +1.5 is #3

#### **Dragons +1.5 — ~57%**

This is very close to BayStars ML in my distribution.

A **3-2 DeNA win** gives both:

- BayStars outright win;
- Dragons +1.5 cover.

Chunichi +1.5 also benefits from:

- Muller pitching well;
- the low expected run count;
- the stronger-rested bullpen;
- NPB's possibility of a terminal tie.

##### Why it doesn't rank higher

Low totals do **not automatically imply close margins**.

Azuma can shut Chunichi down completely.

Scores such as:

- 3-1,
- 4-1,
- 4-0,
- 5-2

all lose Dragons +1.5 even while remaining mostly consistent with the Under thesis.

That explicit one-sided low-scoring branch is mandatory under the Drive methodology.

---

### 15. Over 6.5

#### **Over 6.5 — ~38%**

This is the weakest of the supplied four, but it has a credible tail.

The best Over mechanisms are:

- Yokohama's 1.11 run factor;
- Chunichi's Hosokawa-led home-run threat;
- Muller's occasional ordinary/poor-start state;
- DeNA's six-reliever workload yesterday;
- rain/delay interrupting starter rhythm;
- a 4-3 game;
- extra innings.

The Over does **not** require both offences to dominate. One 4-run inning can fundamentally change the target.

I still put most probability below seven because **both starting-pitching distributions are unusually strong for this threshold**.

---

### Cross-market coherence

My representative state is:

#### **DeNA 3-2 Chunichi**

| Contract | Result in central state |
|---|---|
| Under 6.5 | **WIN** |
| BayStars outright | **WIN** |
| Dragons +1.5 | **WIN** |
| Over 6.5 | LOSS |

So the top three are coherent rather than contradictory.

The distinction is:

> I expect DeNA to be **more likely to win**, but I do **not** expect DeNA to be highly likely to win by multiple runs.

---

### Source ledger

The key sources were:

1. **NPB official schedule / Central League page** for event identity, correct 18:00 JST start and official starters. :chatgpt-content-reference{index="26"}
2. **NPB official pitching leaders** for Azuma's current season record. :chatgpt-content-reference{index="27"}
3. **NPB official Muller player page** for his current pitching and batting record. :chatgpt-content-reference{index="28"}
4. **SportsNavi starter game logs** for the recent Azuma/Muller workload and results. :chatgpt-content-reference{index="29"}
5. **Nikkansports** for Muller's September 14 complete-game shutout. :chatgpt-content-reference{index="30"}
6. **DeNA official September 21 box score** for exact prior-day bullpen workload. :chatgpt-content-reference{index="31"}
7. **SportsNavi September 21 Chunichi box score** for Takahashi/Miyauchi/Sakurai bullpen usage. :chatgpt-content-reference{index="32"}
8. **NPB registration notices** for current roster transactions. :chatgpt-content-reference{index="33"}
9. **Baseball Chronicle** for current Yokohama park factors and venue splits. :chatgpt-content-reference{index="34"}
10. **NPB official September results** for recent-team windows; used diagnostically rather than as a predictive streak. :chatgpt-content-reference{index="35"}
11. **Sports Research Google Drive** for `METHOD.md`, `RULES_GENERAL.md`, `RULES_BASEBALL.md`, `DATA_SOURCE_REGISTER.md`, `BASE_RATES_REGISTER.md` and current controls.
12. The user-provided GitHub repository remains a requested research source; no GitHub-only claim was admitted without independent verification. :chatgpt-content-reference{index="36"}

No sportsbook prediction, betting consensus, market movement, fantasy projection or tipster analysis was used.

---

### Updated Prediction Mini Running Log

Per the mini-log instructions, unsettled forecasts stay tracked and no retrospective is done unless requested. :chatgpt-content-reference{index="37"}

#### Prediction Mini Running Log — P-482 onward

**Method:** MDS-2026.09.19-v4.3 / CR-2026.09.21-3  
**Mode:** SPORTS_ONLY / MARKET_BLIND  
**Performance:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE  
**Next canonical ID:** **P-490**

| ID | Event | Rank #1 | Potential winner | Status |
|---|---|---|---|---|
| P-482 | Antigua vs Jamaica, CPL | Jamaica 1st 6 O47.5 ~59.9% | Antigua ~53% | Unsettled |
| P-483 | Volynets vs Kalieva | Over 19.5 ~65.2% | Volynets ~62% | Unsettled |
| P-484 | Atlanta @ NY Liberty | Under 177.5 ~54% | Atlanta ~58% | Unsettled |
| P-485 | NY Giants @ LA Rams | Giants +6.5 ~61% | Rams ~64% | Unsettled |
| P-486 | Twins @ Giants MLB | Twins ML ~59% | Twins ~59% | Unsettled |
| P-487 | Wings @ Mercury | Mercury +5.5 ~62% | Dallas ~58% | Unsettled |
| P-488 | Wolff vs Oliynykova | Under 20.5 ~60% | Oliynykova ~74% | Unsettled |
| **P-489** | **Chunichi @ DeNA** | **Under 6.5 ~62%** | **DeNA ~60%** | **Unsettled** |

##### P-489 — NPB — Chunichi Dragons @ Yokohama DeNA BayStars

**Status:** `UNSETTLED — PREGAME FORECAST / NO RETROSPECTIVE`

**Correct scheduled start:** 22 Sep 2026, **7:00 PM AEST / 18:00 JST**.  
**Venue:** Yokohama Stadium.  
**Starters:** Katsuki Azuma vs Kyle Muller, official NPB probables.  
**Exact lineups:** not recovered from an eligible current source before issuance; `BB-P2 PARTIAL`.  
**Operator ML/tie and weather-action terms:** `UNKNOWN_DEFINITION`.

**Independent centre:** DeNA approximately **3.1**, Chunichi approximately **2.2**, total approximately **5.3**.

**Ranked picks**
1. **Under 6.5 — ~62% — MEDIUM-LOW**
2. **BayStars outright — ~60% — MEDIUM-LOW**
3. **Dragons +1.5 — ~57% — MEDIUM-LOW**
4. **Over 6.5 — ~38% — LOW**

**Potential winner:** **Yokohama DeNA BayStars ~60%**, with Chunichi ~35% and draw ~5%.

**Main Rank-1 kill path:** Yokohama HR/cluster state or DeNA's taxed relief chain turns a 3-2/3-1 game into 4-3/5-3 or an extended extra-inning game.

**Document mapping:** `RULES_BASEBALL.md` starter identity, no-DH NPB regime, bullpen score-state, home-last-bat, tie/12-inning endpoint, weather termination, low-total separation, joint scoring and line-quarantine controls applied. No new methodology rule proposed.

**No retrospective was performed.**

#### Bottom line

**#1 Under 6.5**  
**#2 BayStars ML / outright**  
**#3 Dragons +1.5**  
**#4 Over 6.5**

**Potential winner: Yokohama DeNA BayStars, most likely in a low-scoring one-run game.**

For future NPB cards, I can also monitor the official starter/lineup release near first pitch and flag any change that materially alters the ranking.

<!-- END VERBATIM ISSUED RECORD: P-489 original card (Codex attachment 8d873c0b) -->

### P-491 — NPB Pacific League — Orix Buffaloes @ Chiba Lotte Marines — 23 Sep 2026 (SETTLED 2026-09-23)

#### Identity, state and settlement status

| Field | Record |
|---|---|
| Event | NPB Pacific League regular season, Orix Buffaloes (visitor) @ Chiba Lotte Marines (home), game 25 of 25. ZOZO Marine Stadium, Chiba (open air). NPB box `npb.jp/scores/2026/0923/m-b-25/`. |
| Scheduled / actual start | 17:00 JST (UTC+9) = 08:00 UTC = **18:00 AEST, 23 Sep 2026**. NPB: 開始 17:02, 終了 19:37 JST, **2 h 35 min**, attendance 24,065. |
| Issue horizon | **PREGAME (clean).** Frozen about 17:53–17:56 AEST, before the 18:00 AEST first pitch, with the NPB box showing 【試合開始前】 and both starting orders posted. |
| Terminal state | **FINAL — 【試合終了】** on the NPB official box, retrieved 2026-09-23 21:07 AEST. |
| Final score | **Orix 1, Chiba Lotte 0.** Total **1**; margin Orix +1. Nine innings. |
| Linescore | ORX 000 000 010 — 1 R, 4 H, 0 E. LOT 000 000 000 — 0 R, 3 H, 0 E. |
| Decisions | W: Kuri (9th win). Hold: Yamasaki. S: Machado (35th, league lead). L: Suzuki (Shota). |
| Result lineages (CR-4 gate) | (1) **NPB official box**: 試合終了, 1–0, full lines. (2) **Sports Navi / Yahoo! Japan**: "ロッテ (敗)鈴木 0 - 1 試合終了 オリックス (勝)九里 (Ｓ)マチャド ZOZOマリン". (3) **Nikkan Sports** via Yahoo! News, staff report with a staff photographer's credit: "＜ロッテ0－1オリックス＞◇23日◇ZOZOマリン … 5連敗 … ルケーシー 7回3安打無失点7奪三振 … 8回表オリックス2死、池田陵真に先制ソロ". Daily Sports ("ロ０-１オ（２３日）") also agrees; it is possibly Kyodo wire copy, so it is not counted separately. **Gate PASS: three independent lineages.** |
| Excluded source | Mynavi "ロッテ 0-1 オリックス" is AI-generated (same series as the P-489 exclusion). The score agrees, but it is not counted. |
| Operator terms | Not supplied. No tie, and the total is not 7, so no push; no interruption. Standard grading is unambiguous. |

#### Settlement

| Rank | As-issued selection (`UNVALIDATED_SUBJECTIVE`) | p (W / P / L) | Result | Settlement | Score |
|---:|---|---|---|---|---:|
| 1 | Buffaloes +1.5 | ~0.67 (component sum 0.476 + 0.170 + 0.030 = 0.676) | Orix won by 1 | **WIN** | Brier 0.1089 (0.1050 at 0.676) |
| 2 | Under 7.0 | 0.50 / 0.10 / 0.40 (exact 0.499 / 0.104 / 0.397) | 1 run | **WIN** | Half-scaled W/P/L Brier 0.2100 (0.2097 exact); decisive q 0.556 → 0.1975 |
| 3 | Marines ML | ~0.49 (tie 0.03 = no-win) | Lotte lost 0–1 | **LOSS** | 0.2401 |
| 4 | Over 7.0 (complement of #2) | 0.40 / 0.10 / 0.50 | 1 run | **LOSS** | Same target as #2 |
| Winner | Chiba Lotte (0.494 v Orix 0.476, tie 0.030) | 0.494 | Orix won | **INCORRECT** | 0.2440 |

**Decision and ranking diagnostics (learning-only).**

| Metric | Value |
|---|---|
| Rank-1 | **WIN** |
| Hit@2 | **YES** |
| Wins@2 | **2 / 2** — both top rows won |
| NDCG@2 | **1.000** (two winners in the slate, both in the top two) |
| Decisions (Over/Under counted once) | Orix +1.5 **W**, total (Under preferred) **W**, Marines ML **L** → **2 W / 1 L** |
| Top over/under | Under 7.0 (#2) — **WIN**; `TOP_OU_REVIEW` not triggered |
| Winner call | **LOSS** — a declared toss-up (0.494) |
| Horizon | PREGAME, clean |

#### What happened in the game (NPB box; Nikkan Sports)

- **Starters.** A 14-inning shutout duel.
  - Kuri: 7 IP, 97 pitches, 24 batters faced, **2 H, 2 BB, 4 K, 0 R**.
  - Lucchesi: 7 IP, 87 pitches, 24 batters faced, **3 H, 0 BB, 7 K, 0 R**. He struck out the side in the 1st and escaped a one-out runner-on-third jam in the 4th by striking out Sugimoto (Nikkan).
- **Decisive run.** Top 8th, two outs: Ryoma Ikeda's first professional home run, a solo shot to left off Suzuki (Lotte's second pitcher).
- **Late innings.** Yamasaki (8th, one hit) and Machado (9th) closed it. Ishigaki Genki pitched a scoreless 9th for Lotte.
- **Lotte's offence.** Three singles (Terachi and Soto in the 5th, Ogawa in the 8th) and one walk. It was Lotte's fifth straight loss.
- **Batting orders** matched the pregame posted orders exactly for both clubs.

#### Pick-by-pick causal review

**#1 Buffaloes +1.5 — WIN.**
- *Why it won.* The card's thesis — "a low-scoring game between two weak offences puts heavy mass on margins of one run or fewer" — is exactly what happened. Orix won outright, so the cushion was not even needed.
- *Kill path.* The named kill path (a Lotte two-plus-run separation, about 0.32, via a Lotte HR cluster or a walk-driven Kuri early hook) never started. Kuri walked two and allowed two hits.
- *Correct assumptions.*
  - Both offences were bottom-half: Orix last in HR, Lotte .297 OBP.
  - Override 8 was applied: Lucchesi's small sample was attached to **Orix's** scoring branch as width, not direction.
  - Kuri's recent walk spike was treated under R-1 as width only, with no signed lean.
- *Incorrect or untested assumptions.* The upper-tail mechanisms (walk rates of 10 BB / 15 IP and 14 BB over three starts) did not appear: 2 walks in 14 starter innings. One game says nothing about whether the width was right.
- *Driver.* Predictable structure (two weak offences, competent starters) plus low-scoring variance.

**#2 Under 7.0 — WIN (by 6).**
- *Why it won.* Two starters combined for 14 scoreless innings with 5 hits, 2 walks and 11 strikeouts. There was light wind (NE 2 m/s) and it was cool and humid. Both offences were weak.
- *Calibration note.* The card's centre was **7.19** runs. The realised total of 1 sits deep in the lower tail: under the card's per-inning Poisson–gamma model it is roughly the 2nd–5th percentile (an estimate; the distribution file was not preserved).
  - Correct side, correct reasons, but the centre was far from the outcome.
  - One game cannot say the centre was too high. But this is the NPB leg of `C-RUN-CENTRE-BIAS` (historically, centres sat above actuals in 9 of 12 cards), and it is recorded there.
- *Assumptions.*
  - Correct: offence quality; light-wind conditions; home-ninth cap (B6). Lotte trailed and batted in the 9th, so B6 did not apply.
  - Untested: bullpen fatigue from 22 Sep. It was recorded as `UNQUANTIFIED`, and one late relief inning decided the game.

**#3 Marines ML — LOSS.**
- A declared near-coin-flip (0.49). Lotte's three singles could not overcome Kuri. The one run came from a relief pitcher conceding a solo homer to a hitter with no previous professional home run.
- This is **genuine variance**, not a process error. The card itself called it "effectively a toss-up".

**#4 Over 7.0 — LOSS (forced complement).** No independent information.

**Projected winner — Lotte (narrow) — INCORRECT.** 0.494 v 0.476 is a statement of near-indifference, so the miss carries almost no information.

#### Rank-1 review — a win, audited (METHOD §7: "inspect wins as well as losses")

1. **Why #1.**
   - Largest derived probability (0.676) among four rows.
   - The row covers three outcome families: Orix win, Lotte by exactly 1, and a tie.
2. **Justified?**
   - **Yes on process.** The card printed the margin distribution: Lotte by one 0.170 was modal, and Lotte by 2+ was about 0.32.
   - It did **not** exclude the BB-B4 separation. It named that separation as the kill path with mass, which is the honest form of override 3.
   - It re-solved the total conditional on the cushion (override 9: P(U ∧ +1.5) ≈ 0.354).
3. **Was the result right for the reasons the card gave?** Mostly yes.
   - The low-scoring, weak-offence mechanism operated.
   - The specific path — an Orix outright win — was the card's second-largest component (0.476), not the "Lotte by exactly one" state.
4. **Anything that would have made it wrong despite correct reasoning?** A single Lotte relief-inning cluster: the B9 late-separation branch. The card named it.
5. **Rule change?** None. This card is the reference example for override 3, 8 and 9 compliance in NPB.

#### Top-two review

- Both top picks won, and `P(R1 ∧ R2)` ≈ 0.354 was printed with a positive-coupling label (PR-3). The realised state (1–0 Orix) sits in the joint-success region.
- **Ordering.** Justified: 0.676 v 0.50 (W) / 0.556 (q). The cushion's broader support — three outcome families — correctly outranked an integer total that carries push mass.
- **Why the card could print the joint probability.** It had one joint simulation, so `P(R1 ∧ R2)` came from the model rather than from bounds. This is the construction P-489 lacked.

#### Over/under review

| Factor | Pregame | Actual | Note |
|---|---|---|---|
| Environment | Cool (21–22 °C), humid, NE 2 m/s — mildly suppressive, no signed park factor | Consistent | Correct handling (no stacked conditions adjustment) |
| Offence | Orix 3.46 R/G (fewest HR in PL), Lotte 3.51 R/G | 1 run in total, 7 hits | Consistent |
| Starters | Kuri 3.35 ERA (recent walk spike: width only); Lucchesi small sample (10 BB / 15 IP) | 14 IP, 0 R, 2 BB | Walk-tail mechanisms did not fire |
| Lineups | Both orders posted and captured | Orders matched | Strong |
| Bullpens | 22 Sep usage `UNQUANTIFIED` | Late relief conceded the only run | Could have been quantified (see blind spots) |
| Distribution | Mean 7.19; P(≤6) 0.499; P(=7) 0.104 | 1 | Deep lower tail |
| Integer line | Push mass 0.104 disclosed | No push | Correctly ranked below the half-line-equivalent rows |

**Verdict.** The side was right and the reasons were right. The centre was a long way from the outcome. Record as a `C-RUN-CENTRE-BIAS` NPB data point (centre 7.19, actual 1, −6.19). No rule change.

#### What went right

- **First verified pre-start freeze with both batting orders posted** in this log lineage (the PR-1 note on the card). The NPB box `スタメン` lane works.
- **One joint simulation** generated every row: winner, margin, total and joint probabilities. This made override 9 and G-L10 printable.
- **Override 3 in its honest form.** The separation mass was named (about 0.32) rather than wished away.
- **R-1 and override 8** stopped the recent walk spikes and Lucchesi's three-start sample from becoming a signed Over lean. In this game neither pitcher walked many.
- **Integer push mass** printed and carried into the ranking.

#### Blind spots and future handling

| Blind spot | Knowable pregame? | Impact | Handling | Rule or observation |
|---|---|---|---|---|
| Reliever pitch counts from 22 Sep not extracted (the summarising fetch returned an inconsistent box) | **Yes.** The raw NPB 22 Sep box HTML parses cleanly with a plain script; this pass did so for other boxes. | Low–medium: a late reliever conceded the only run | Parse NPB box HTML directly (curl plus tag-strip); never rely on a summarising fetch for box scores (M20) | Source note (DATA_SOURCE_REGISTER) |
| Registration/injury list not retrieved | Yes (NPB 公示 page) | Low here | Add the NPB 公示 (roster transactions) page to the BB-P2 lane | Existing rule (BB-P2) |
| Umpire not retrieved | Partly | Low | NPB box pages list 審判 post-game; pregame crew assignments are not reliably published | No change |
| Lucchesi v Orix history (now 3 starts, 18 IP, 2 ER) | Yes | Low | Still diagnostic (n = 3); do not promote | Observation only |

#### Mandatory validation questions

1. **Confirmed starting lineups?** **Yes.** Both posted orders came from the NPB box before first pitch and matched the game exactly.
2. **Bench, reserve and rotation?** Benches were not captured. Bullpen workload from 22 Sep was noted qualitatively only (`UNQUANTIFIED`).
3. **Coaching/manager information?** Not retrieved. Not material.
4. **Injuries, suspensions, rest and late changes?** Registration and injury list: `RETRIEVAL_MISS`, disclosed. Lucchesi's health was confirmed via the Mynavi interview (S-2, availability only).
5. **Were sources accurate and current?** Yes:
   - NPB box (starters, orders, state);
   - NPB BIS team tables;
   - gurazeni per-start logs (reconciled with NPB for Lucchesi);
   - tenki.jp venue forecast (conditions matched).
6. **Better sources available?** Raw-HTML parse of the NPB box for reliever pitch counts, and the NPB 公示 page.
7. **Blind spots?** Minor ones; see the table above.
8. **How to account for them?** Parse box HTML directly, and add the 公示 retrieval to the NPB BB-P2 checklist.

#### Connection to prior lessons

| Lesson | Status |
|---|---|
| §8.6 overrides 3, 8 and 9 | **Followed, and they worked as designed.** A positive example. |
| `M18` (anti-coupled top two: baseball +1.5 with Under) | Correctly identified as **positively** coupled in a low-total, close-game environment (P(R1 ∧ R2) printed). M18's warning concerns low-total *separation* games; the card budgeted separation (0.32). |
| `C-RUN-CENTRE-BIAS` | NPB data point: centre 7.19, actual 1. Consistent with the historical "centres above actuals" direction. P-489 was the opposite, so the two NPB cards from the same night straddle it. **No tilt is justified.** |
| R-1 (recency revises a rate only via a named mechanism) | Followed. Kuri's walk spike did not persist in this game. That is one game, not validation. |
| Baseball underdog +1.5 record (2026-09-15(b)) | This win is a near-even pick (0.476 v 0.494), not a true underdog. Do not count it as evidence for underdog cushions. |

**G37 grade: RESULT-RIGHT / PROCESS-RIGHT** for the top two. The winner call was an honest toss-up.

#### Settlement sources (P-491)

| Source | Link | Field ownership | Access / time (AEST) | Contribution |
|---|---|---|---|---|
| NPB official box | https://npb.jp/scores/2026/0923/m-b-25/box.html | League field owner | OPENED (raw HTML), 21:07 | 試合終了 1–0; start/end/attendance; batting and pitching lines |
| Sports Navi results | https://baseball.yahoo.co.jp/npb/schedule/?date=2026-09-23 | Independent statistics publisher | OPENED, 21:20 | 0–1 試合終了; W 九里 / S マチャド / L 鈴木 |
| Nikkan Sports (Yahoo! News) | https://news.yahoo.co.jp/articles/c209a9a9df0e9c03d60b56ea4263a018cc533c83 | Independent newspaper (staff report) | OPENED, 21:26 | 0–1; Lucchesi 7 IP 3 H 0 R 7 K; Ikeda solo off Suzuki in the 8th; 5-game losing streak |
| Daily Sports | https://www.daily.co.jp/baseball/2026/09/23/0020852122.shtml | Newspaper (possible wire copy) | OPENED, 21:24 | 0–1; Ikeda's first pro HR; Kuri 7 scoreless, 9th win; Machado 35th save; Lotte "単打３本" |
| Mynavi (excluded) | https://news.mynavi.jp/article/20260923-baseball_game05/ | AI-generated | OPENED | Excluded (synthetic-content rule) |

#### Original P-491 card (preserved verbatim from the P-494-onward mini log)

<!-- BEGIN VERBATIM ISSUED RECORD: P-491 (heading levels demoted by two; text unchanged) -->

##### P-491 - NPB - Orix Buffaloes @ Chiba Lotte Marines (ZOZO Marine, 23 Sep 2026)

**Status:** UNSETTLED — PREGAME FORECAST / NO RETROSPECTIVE (none requested).

**Identity / timing**
- Canonical mini-log ID: `P-491`. NPB game page: `npb.jp/scores/2026/0923/m-b-25/`.
- Competition: NPB Pacific League regular season. Chiba Lotte Marines (home, bat last) vs Orix Buffaloes. ZOZO Marine Stadium, Chiba; outdoor, no roof.
- Scheduled start: 17:00 JST = **18:00 AEST, 23 Sep 2026** (NPB schedule and box page).
- Final refresh before issue: NPB official box page showed **【試合開始前】 ◇開始 17:00** with both スタメン posted. Captured about 17:53–17:56 AEST; picks were delivered to the user at about 17:54 AEST. **Horizon: CLEAN (pre-start).** The freeze preceded the 18:00 AEST scheduled first pitch.
- Method / controls: `MDS-2026.09.19-v4.3 / CR-2026.09.21-3`; `SFA-BASEBALL`; `SPORTS_ONLY / MARKET_BLIND`; `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`.

**Supplied contracts**
- Buffaloes +1.5; Marines ML; game total Over 7.0 / Under 7.0.
- The integer total carries **push** mass at exactly 7.
- NPB regular-season games are capped at 12 innings, and a tie is terminal (RULES_BASEBALL §9.3). Operator tie and action rules were **not supplied** (`UNKNOWN_DEFINITION`).
  - Marines ML is graded "not a win" on a tie. It is a push or void if the operator uses tie-no-bet.
  - Buffaloes +1.5 wins on a tie.
  - Totals settle on the 12-inning final.
- The lines were visible in the request. The run centres below were built from team and starter rates, and the lines were located only afterwards.

**BB-P gates**
- `BB-P1` starters: **CONFIRMED_OFFICIAL** from the NPB box page 先発 fields.
  - Orix: **九里 亜蓮 (Aren Kuri)**, RHP.
  - Lotte: **ジョーイ・ルケーシー (Joey Lucchesi)**, LHP.
  - Cross-check: SKY PerfecTV's starter page marks both as 予告先発.
- `BB-P2` batting orders: **both posted** (NPB box page).
  - Orix: 1 西川 左, 2 来田 中, 3 太田 二, 4 杉本 指, 5 宗 三, 6 紅林 遊, 7 内藤 一, 8 若月 捕, 9 池田 右.
  - Lotte: 1 藤原 中, 2 上田 一, 3 山口 左, 4 西川 右, 5 寺地 三, 6 ソト 指, 7 佐藤 捕, 8 山﨑 遊, 9 小川 二.
  - Individual injury lists and ichi-gun registration moves were **not retrieved** (`RETRIEVAL_MISS`). Absences are therefore only what the posted orders imply.
  - Bench and bullpen availability were not captured beyond the 9/22 game note below.
- `BB-P3`: Pacific League uses the DH (both sides). 9 innings, capped at 12, tie terminal. No roof.
- `BB-P4`: official-game rule per NPB. Operator terms unknown.
- `BB-P5`: Lotte bats last. The total includes extras up to the 12th.

**Starter evidence (G14.1 deficit attribution)**
- **Kuri (Orix).**
  - NPB official 2026 line: 25 G, 8–11, 150.2 IP, 132 H, 13 HR, 60 BB, 139 K, 65 R, 56 ER, **3.35 ERA**. His 2025 line was a 2.41 ERA over 164.1 IP.
  - Last ten starts (gurazeni per-game log; secondary source): 9/16 SoftBank 6 IP 0 R; 9/09 Seibu 4 IP 6 ER; 9/01 Rakuten 5 IP 3 ER, 5 BB; 8/25 Rakuten 5 IP 4 ER, 6 BB; 8/18 Seibu 3 IP 6 R (3 ER); 8/11 7 IP 1 ER; 8/03 6 IP 6 R (2 ER); **7/26 vs Lotte 6 IP 3 ER, 10 K, 127 pitches**; 7/20 7 IP 0 R; 7/14 6 IP 2 ER.
  - Recent walks and short starts are recorded. Under R-1 no named mechanism (velocity, injury or role change) was found, so the season rate is used and the recent form only **widens** Lotte's scoring distribution.
  - Hook distribution: usually 5–7 IP at 80–127 pitches. Early-hook (≤4 IP) share in the last ten starts: 2 of 10.
- **Lucchesi (Lotte).**
  - Ex-MLB left-hander, joined Lotte in mid-July. NPB: 3 G, 1–1, 15 IP, 7 ER, **4.20 ERA**. His three logged starts give 9 H, 1 HR, **10 BB**, 12 K.
  - Starts: 8/9 vs Orix 4 IP 2 ER, 71 pitches; **9/6 vs Orix 7 IP 0 R, 1 H, 4 BB, 103 pitches**; 9/13 vs SoftBank 4 IP 5 ER, 4 BB, 100 pitches.
  - Mynavi (23 Sep) confirms today is his fourth NPB start. It reports no health issue or pitch limit.
  - **Small-sample starter** (3 starts): his profile is a prior, not a rate. Per §8.6 override 8 this is attached to **Orix's** scoring branch as extra width.
  - His walk rate is the main upper-tail mechanism for Orix. He is 11 IP / 2 ER against Orix, but that is two games and is `E — diagnostic only`.

**Team context (NPB official, to 21 Sep)**
- Standings: Orix 63–71–2 (4th); Lotte 58–68–3 (5th). Both are out of contention.
- Runs scored per game: Orix 470/136 = **3.46** (.245/.307/.357, 90 HR, fewest in the PL); Lotte 453/129 = **3.51** (.237/.297/.363, 117 HR).
- Runs allowed per game: Orix 570/136 = **4.19** (3.93 ERA); Lotte 537/129 = **4.16** (3.88 ERA).
- The two teams' games average roughly 7.6–7.7 total runs on season rates.
- Previous game (22 Sep, same venue): **Orix 6–4 Lotte** (NPB box; linescore Orix 0-1-0-0-1-2-2-0-0, Lotte 1-2-0-0-0-0-0-0-1; 3 h 21 min). Both bullpens were used. Individual reliever lines were **not reliably extracted** (the fetched box summary was internally inconsistent), so bullpen fatigue is carried as `UNQUANTIFIED`, not as a signed input.
- Recent H2H (Mynavi): Orix 3–2 over the last five meetings. `E — diagnostic`.

**Environment (§8.9)**
- tenki.jp ZOZO Marine hourly forecast, issued 23 Sep 09:00: cloudy; 21.5–22.1°C; 30% rain probability with 0 mm/h; humidity 81–88%; **NE wind at 2 m/s** from 17:00 to 21:00.
- Light wind removes ZOZO Marine's usual wind-driven variance. Cool, humid air is mildly suppressive, but no signed park factor is applied beyond that.
- Umpire crew was not retrieved.
- Termination branch (rain) is small: 0 mm/h forecast.

**Joint run object (frozen before querying the lines)**
- Team centres, from partially pooled offence × opponent run prevention × starter adjustment around a PL run environment of ~3.8 runs per team-game: **Orix ≈ 3.6, Lotte ≈ 3.7** runs per 9.
- Simulation: per-inning Poisson with a gamma team-game multiplier (k = 2). Includes the home-ninth rule and extras to 12 with a tie cap. `UNVALIDATED_SUBJECTIVE`; not fitted or calibrated.
- Derived: mean total **7.19**; P(total ≥ 8) **0.397**; P(total = 7) **0.104**; P(total ≤ 6) **0.499**.
- Outcomes: Lotte win 0.494; Orix win 0.476; tie 0.030.
- Margin (Lotte minus Orix): +1 0.170 (modal); +2 0.097; +3 0.068; +4 0.048; −1 0.136; −2 0.091.
- Sensitivity (±0.2 runs per side): the Under minus Over gap stays at 3–17 points; Orix +1.5 stays at 0.66–0.70; the winner stays within ±3 points of 50/50.

**Nine-branch coverage**
- **B1** both starters central (~5–6 IP each) → 3–4 runs each, the modal family.
- **B2** early hook: Kuri 2/10 recent starts ≤4 IP; Lucchesi 2/3 starts at 4 IP. This is the largest Over and swing driver.
- **B3** HR cluster: Lotte has more power (117 HR) than Orix (90).
- **B4** one-sided separation with a 0–2 opponent floor. It defeats Orix +1.5 when Lotte is the side separating.
- **B5** relief transition after both pens were used on 9/22.
- **B6** Lotte skips the bottom 9th when leading. This caps the total and favours the Under.
- **B7** extras to 12 with no runner rule.
- **B8** rain is negligible.
- **B9** late separation through the bullpens.

**Ranked picks**
1. **Buffaloes +1.5 — ~0.67 `UNVALIDATED_SUBJECTIVE`. Evidence: LOW–MEDIUM.**
   - Wins: Orix win 0.476 + Lotte by exactly 1 (0.170) + tie 0.030.
   - Override 3: BB-B4 separations by Lotte (2+ runs, ~0.32) are **not** excluded. They are the kill path: a Lotte HR cluster (B3), or Kuri's walk-driven early hook (B2) followed by a pen used on 9/22. The row ranks first because a low-scoring game between two weak offences puts heavy mass on margins of one run or fewer, not because separation is impossible.
   - G30.1: the potential winner named below is Lotte. The separating states are Lotte by exactly 1 (+1.5 wins, Lotte ML wins) and Lotte by 2+ (+1.5 loses).
2. **Under 7.0 — ~0.50 win / 0.10 push / 0.40 loss (~0.56 excluding push). Evidence: LOW.**
   - Override 2 (why the upper tail is subordinate): both offences are bottom-half on OBP and SLG; Orix is last in HR; conditions are cool with light wind; and the home ninth is capped.
   - Named upper-tail kill path, with its mass: both starters are walk-prone (Lucchesi 10 BB in 15 IP; Kuri 14 BB over 9/1–9/9 and 8/25). Early-hook states (B2) plus pens used on 9/22 feed the ~0.40 Over mass.
   - Override 9 re-solve: P(Under 7 ∧ Orix +1.5) ≈ 0.354, so P(Under | +1.5 wins) ≈ 0.52. The rows are positively dependent through low-scoring, close games.
3. **Marines ML — ~0.49 (tie 0.03 counts as no-win). Evidence: LOW.**
   - Home, last at-bat, and Kuri's recent command issues on one side. Against that: Lucchesi's small-sample walk rate and Orix winning 9/22.
   - This is a near coin flip. Coherence check: P(Orix +1.5) 0.676 ≥ 1 − P(Marines ML) = 0.506 ✔.
4. **Over 7.0 — ~0.40 (0.10 push).** Live through B2/B3: early hooks, walk clusters and Lotte's power. It ranks last because the centre (7.19) sits barely above the line and the integer push absorbs part of the upper mass.

**Potential winner:** **Chiba Lotte Marines, narrowly — ~0.49 vs Orix ~0.48, tie ~0.03. LOW confidence; effectively a toss-up.** Endpoint: the eventual result including extras to 12; a tie is possible.

**Dependence / coherence**
- Representative Rank-1 scoreline: **Lotte 3–2**. That is Orix +1.5 **WIN**, Under 7 **WIN** (5 runs) and Marines ML **WIN**. All three top rows are compatible.
- Top-two both-fail state (Lotte by 2+ ∧ total ≥ 8), e.g. Lotte 6–3: **≈0.152** from the same simulation. Shared failure driver: **Lotte offensive separation after an early Kuri exit**.
- C-MODAL-BRANCH-CHECK: the modal margin (Lotte +1) and the modal total region (≤6) **satisfy** Rank #1 and #2. The modal branch does not defeat the top two.
- PR-3 shared driver: the top two share the "low-scoring, close game" driver. Positive coupling is disclosed.
- Forced pairs: Over/Under 7.0 is one decision. Marines ML and Buffaloes +1.5 are **not** complements; a Lotte one-run win cashes both.

**Sources**
1. [NPB official box/preview page — m-b-25](https://npb.jp/scores/2026/0923/m-b-25/box.html): state 【試合開始前】, 17:00 start, both 先発, both スタメン. Field owner.
2. [NPB 2026 September schedule](https://npb.jp/games/2026/schedule_09_detail.html): fixture, ZOZOマリン, 17:00.
3. [NPB English schedule 23 Sep](https://npb.jp/bis/eng/2026/games/gm20260923.html): fixture cross-check.
4. [SKY PerfecTV starter page](https://baseball.skyperfectv.co.jp/starter/): 予告先発 cross-check (ルケーシー / 九里).
5. [NPB — Kuri year-by-year](https://npb.jp/bis/players/71775139.html): 2026 and 2025 lines.
6. [NPB — Lucchesi year-by-year](https://npb.jp/bis/players/93095152.html): 2026 NPB line, LHP.
7. [gurazeni — Kuri game log](https://www.gurazeni.com/player/910) and [gurazeni — Lucchesi game log](https://www.gurazeni.com/player_pitching/2932/year:2026): per-start IP, pitches, BB, K, R, ER. Secondary source; totals reconcile with NPB for Lucchesi (15 IP, 7 ER).
8. [Mynavi — Lucchesi interview, 23 Sep](https://news.mynavi.jp/article/20260923-5013260/): fourth NPB start today; last start 9/13. Availability evidence only (S-2).
9. [Mynavi — pre-game page](https://news.mynavi.jp/article/20260923-5011451/): last-five H2H 3–2 Orix.
10. [NPB PL standings](https://npb.jp/bis/2026/stats/std_p.html), [team batting](https://npb.jp/bis/2026/stats/tmb_p.html), [team pitching](https://npb.jp/bis/2026/stats/tmp_p.html): to 21 Sep.
11. [NPB box 22 Sep (m-b-24)](https://npb.jp/scores/2026/0922/m-b-24/box.html) and [Weekly Baseball Online game flash 22 Sep](https://sp.baseball.findfriends.jp/?pid=game_flash&game_id=2026092205): prior-game result 6–4 Orix and linescore. Reliever lines not used (extraction inconsistent).
12. [tenki.jp — ZOZO Marine hourly forecast](https://tenki.jp/leisure/baseball/3/15/31009/1hour.html): conditions.
13. Drive methodology: `RULES_BASEBALL.md` (§8, §8.6 overrides 2/3/8/9, §9.3 NPB ties, 2026-09-19 R-1, CR-2026.09.21-3), `METHOD.md`, `RULES_GENERAL.md`.

**Source firewall / limitations**
- No odds, betting previews, prediction markets, tipsters or fantasy pages were used. Betting-preview results that appeared in searches were not opened.
- Missing inputs:
  - injury and registration list (`RETRIEVAL_MISS`);
  - reliever availability and pitch counts from 9/22;
  - umpire;
  - Statcast-grade arsenal data for NPB (not available);
  - handedness splits for both lineups (not retrieved).
- Several numbers came through a summarising fetch tool. Values used were cross-checked where two sources existed (Lucchesi totals; starters; lineups from the field owner).

**Document mapping / candidate observations**
- `RULES_BASEBALL.md`: no change. §9.3 tie handling is applied (Buffaloes +1.5 wins a tie; ML needs the operator's tie rule).
- `DATA_SOURCE_REGISTER.md`: the NPB box page (`/scores/YYYY/MMDD/<home>-<away>-NN/box.html`) exposes pre-game 先発 and スタメン about an hour before first pitch. Use it as the BB-P1/BB-P2 lane. The `/announcement/starter/` and `/scores/.../` index routes redirect-loop through the fetch tool.
- PR-1: this card is the first in the log with a verified pre-start freeze and both lineups posted.

<!-- END VERBATIM ISSUED RECORD: P-491 -->


# General Learnings, Rule Changes, Observations, and New Sources

**Status of everything in this section:** learning-only. One night of events proves nothing statistically. Items marked **OBSERVATION** or **TESTING** are not rules. Where a finding coincides with an existing rule that was not executed, the fix is to execute that rule; no new rule is added (MODEL_REVIEW / `L-087`: no single-game coefficient).

## Batch summary (descriptive only — not a performance record)

| ID / handle | Event (game date) | Horizon at issue | Final | Rank-1 | Hit@2 | Wins@2 | NDCG@2 | Decisions (forced pairs once) | Top O/U | Winner call | G37 grade |
|---|---|---|---|:-:|:-:|:-:|:-:|---|---|:-:|---|
| TMP-20260922-WNBA-DAL-PHX (claims P-487) | Dallas @ Phoenix (22 Sep) | Unknown (body not carried) | PHX 87–86 | **W** (Mercury +5.5) | unknown | unknown | unknown | unknown | unknown | **L** (Dallas) | Unauditable (`BODY_NOT_CARRIED`) |
| P-489 | Chunichi @ DeNA, game 24 (22 Sep) | START_CROSSED | DeNA 7–3 (10 runs) | **L** (Under 6.5) | Y | 1/2 | 0.387 | 1 W / 2 L; mean Brier 0.2898 | **L** → `TOP_OU_REVIEW` | **W** (DeNA) | Result-wrong / process-wrong in part |
| P-491 | Orix @ Lotte (23 Sep) | PREGAME (clean) | Orix 1–0 (1 run) | **W** (Orix +1.5) | Y | 2/2 | 1.000 | 2 W / 1 L; mean Brier 0.1863 | **W** (Under 7.0) | **L** (Lotte, 0.494 toss-up) | Result-right / process-right |
| TMP-20260923-NBL-CNS-TAS (claims P-487) | Cairns v Tasmania (23 Sep) | PREGAME, bounded (untimestamped) | CNS 93–87 (180) | **L** (TAS +2.5) | Y* | 1/2* | 0.387* | 1 W / 1 L* (no probabilities) | **W*** (Under 186.5) | **L** (Tasmania) | Result-wrong / process-wrong |

\* On the card's reading of the total as 186.5. The prompt said "Under 18.5": literally that is a loss, which would make Hit@2 NO and trigger `TOP_OU_REVIEW`.

**Descriptive totals (four settled records; two canonical).**
- Rank #1: 2 W / 2 L (canonical 1 W / 1 L).
- Top-two both-won: 1 of 3 auditable records (P-491).
- Winner calls: 1 W / 3 L. Two of the misses were near-coin-flips (P-491 at 0.494; WNBA lost on a last-second basket); the NBL miss was a process failure.
- Carried over live and unscored: TMP-G25, P-493, P-494.
- **None of this is performance evidence.**

## A. Cross-sport learnings

1. **Event identity must be matched on date *and* participants before a "same-event" merge.**
   - *Evidence:* P-489 original (22 Sep, Azuma v Muller) and "R1" (23 Sep, Fukazawa v Nakachi) were merged as one event. The mismatch was visible in the card's own schedule line and starters. The merge produced a false "issue horizon conflict" (22 Sep card checked against the 23 Sep page) and would have settled a 22 Sep card against a 23 Sep game.
   - *Status:* **OBSERVATION → proposed process control `O-ID-DATE-STARTER-MATCH`.** Before any "same event / reforecast" label, print a four-field match: date, venue, home/away, and starters (or lineups, or players). Any mismatch means a separate event.
   - *Home:* `EXTERNAL_LOGGING_WORKFLOW.md` (import checklist) and `RULES_GENERAL.md` identity gates (G0–G6).
   - Promotable now as an integrity control, since it has a clear mechanism. It changes no forecast.
2. **External transcripts carry ID claims the repository never sees.**
   - *Evidence:* P-487 (Dallas @ Phoenix) existed in the external session's own running-log tables (P-488 and P-489 outputs) and was never registered. A later NBL card claimed the same number, and the 2026-09-23 reconciliation recorded a "no claimant" gap.
   - *Status:* **OBSERVATION → proposed control `O-EXTERNAL-ID-CLAIM-SWEEP`.** On every import, parse the ID tables embedded in *every* supplied transcript or attachment, and list any ID/event pair absent from the repository as `BODY_NOT_CARRIED`.
   - *Home:* `EXTERNAL_LOGGING_WORKFLOW.md`.
3. **Start-crossed issuance recurs in one external session.** P-485, P-489 and P-492 were all issued "just after" the scheduled start. The CR-4 gate exists (README, METHOD §"three-source"). This is **M15 (control listed, not executed)**, not a missing rule.
4. **Cards without a six-field object cannot be audited or ranked honestly.**
   - The NBL card (no probabilities, no distribution, wrong roster) produced this batch's clearest Rank-#1 process failure.
   - P-491 (one joint simulation) and P-494 (exact Markov tree) produced fully auditable records.
   - *Home:* existing METHOD §4. No change; execution only.
5. **AI-generated match reports must be excluded from settlement lineages.** Mynavi's "【プロ野球試合結果】" pages are labelled AI-generated, and one omitted a three-run inning. This **confirms** the existing synthetic-content rule (memory: synthetic content settlement trap; METHOD §3 step 4). No new rule; add Mynavi's AI series to the source register as *excluded for settlement*.
6. **Recency-as-rate and one-sided mechanisms remain the commonest reasoning leak** (NBL: one R1 score used as a defensive rate; travel fatigue applied to the total only). These are existing R-1 and G-L2 breaches.

7. **Settlement-lineage independence needs data-vendor awareness.** The NBL match feed is Sportradar-powered; ESPN's NBL vendor is unverified. The independent third lineage was Flashscore/Livesport, which collects its own data. Record the data vendor wherever a feed exposes it (`sportradar_timestamp` here). *Home:* `SOURCES.md` lineage rules. Observation.

## B. Sport-specific learnings

### Baseball — NPB / KBO

1. **NPB Under 6.5 at Rank #1 has now failed twice: P-361 (2026-09-11) and P-489.**
   - The existing §8.5 kill-path row ("one ordinary cluster crossing a low line — Under 5.5/6.5 at 0.56+") names this exactly.
   - In P-489 the centre (5.3) was built from starter ERAs counted three times per starter (season, L5, v-opponent). No team R/G baseline was printed, and unearned runs were omitted.
   - **Execution of control 26 is the fix.**
   - **OBSERVATION `O-NPB-ERA-CENTRE`:** an ERA-anchored team-run projection must add back the unearned-run share (by definition ERA excludes it; here 3 of 10 runs were unearned) and must be reconciled with team R/G and RA/G before an Under is ranked #1. This is disclosure and arithmetic, not a coefficient.
2. **P-491 is the positive NPB model card.**
   - One joint simulation from partially pooled team rates.
   - Overrides 3, 8 and 9 applied in their honest forms: named separation mass, a small-sample starter attached to the opponent's branch as width, and a conditional total re-solve.
   - The pregame NPB-box starting-order lane verified.
   - Both top rows won. Preserve this construction.
3. **`C-RUN-CENTRE-BIAS` (NPB leg):**
   - P-489: centre 5.3, actual 10 (+4.7).
   - P-491: centre 7.19, actual 1 (−6.19).
   - TMP-20260923-NPB-CHU-DB-G25: carried over live; the card published no numeric centre (forced rank). Accrue at settlement if a centre can be recovered.
   - P-493 (KBO): centre 8.68; carried over live; accrue at settlement.
   - The two settled NPB errors point in opposite directions. **No directional tilt is supported.** Construction consistency (control 26; team-rate anchoring) is the supported lesson.
4. **NPB bullpen fatigue can be quantified.** The 22 Sep NPB box parses cleanly from raw HTML. The P-491 card's "`UNQUANTIFIED` — summary inconsistent" was a fetch-tool artefact (M20), not a data gap.
5. **KBO (P-493):** carried over live. No KBO learning is drawn in this pass.

### Basketball — NBL / WNBA

1. **NBL: roster identity before process history.**
   - The Cairns roster on the NBL card omitted Jack McVeigh (starter, 17 points) and Kyrin Galloway (bench, 19 points). "Galloway out" referred to Jaylin Galloway.
   - **OBSERVATION `O-ROSTER-NAME-COLLISION`:** print first names and the official active list whenever an injury note shares a surname with an active teammate.
   - *Home:* `RULES_BASKETBALL.md` §7 step 2 note. Observation until it recurs.
2. **NBL tip-off lags the scheduled time.** The official feed's first live play-by-play event was 19:36:09 AEST against a 19:30 schedule. A freeze made between 19:30 and 19:36 is inside that window. Use the first-play timestamp in the official match data as the start marker for horizon audits.
3. **WNBA (P-487 claimant).** Mercury +5.5 won on a last-second basket; the Dallas winner lean lost. The body is not carried, so there is **no learning beyond custody.**

### Tennis — WTA

P-494 (Andreeva v Sasnovich, a live-issued view) was **still live at carry-over**, so no tennis learning is drawn. Source note only: the WTA match feed dropped the live match (state `P`) from its list at 21:33 AEST, and it reappeared later; the ESPN tennis scoreboard (competition 184095) carried it throughout.

## C. Potential rule changes (proposed; the operator decides)

| ID | Proposed change | Evidence | Type | Home | Status |
|---|---|---|---|---|---|
| O-ID-DATE-STARTER-MATCH | Four-field event match (date, venue, home/away, starters/participants) required before any "same-event" merge or reforecast label | P-489 / TMP-G25 merge | Integrity control (no forecast effect) | `EXTERNAL_LOGGING_WORKFLOW.md`; `RULES_GENERAL.md` G0–G6 | **Promote as PROMOTED_PROCESS** (mechanism clear; zero predictive claim) |
| O-EXTERNAL-ID-CLAIM-SWEEP | Parse every supplied transcript's embedded ID table at import; register absent IDs as `BODY_NOT_CARRIED` | P-487 WNBA claimant | Integrity control | `EXTERNAL_LOGGING_WORKFLOW.md` | **Promote as PROMOTED_PROCESS** |
| O-NPB-ERA-CENTRE | Add back unearned runs and print team R/G before an ERA-anchored Under can rank #1 | P-489 (and P-361 by pattern) | Disclosure/arithmetic | `RULES_BASEBALL.md` §8.7 checklist | **TESTING** (two NPB cases; mechanism clear; no coefficient) |
| O-ROSTER-NAME-COLLISION | First names plus official active list when an injury note shares a surname with a teammate | NBL card | Disclosure | `RULES_BASKETBALL.md` §7 | OBSERVATION |
| O-START-MARKER | Use the official feed's first-event timestamp as the actual start marker in horizon audits (NBL, WTA) | NBL (19:36:09 v 19:30); WTA (10:38Z v 10:35Z) | Integrity | `RULES_GENERAL.md` horizon fields | OBSERVATION |

## D. Algorithm improvements (test prospectively; nothing fitted)

- **Baseball:** build every run centre from partially pooled team R/G and RA/G first, then apply the starter adjustment once (P-491 method), and print the net starter adjustment. This is already implied by §8.2 and control 26. The algorithm change is to **make the P-491 order of operations the default template**.
- **Basketball:** no rank without a pace × efficiency joint (existing §8). The NBL card is not evidence about the algorithm; it is evidence the algorithm was not run.
- **Tennis:** none this pass (P-494 carried over).

## E. Source improvements (new or re-prioritised)

| Source | Link / method | Sport | Information | Why useful | Reliability considerations | Tier |
|---|---|---|---|---|---|---|
| NPB official box, parsed from raw HTML | `https://npb.jp/scores/YYYY/MMDD/<home>-<away>-NN/box.html` fetched with curl and a tag-strip | NPB | Pre-game スタメン and 先発; post-game 試合終了, full batting and pitching lines, pitch counts, start/end/attendance | Field owner; the summarising fetch tool garbled the box (P-491), raw HTML does not | Japanese labels; "3 +" style innings notation needs care | **Primary** (already registered as a lane; upgrade the method note) |
| Sports Navi (Yahoo! Japan) schedule/results | `https://baseball.yahoo.co.jp/npb/schedule/?date=YYYY-MM-DD` | NPB | Final state, W/L/S pitchers for every game on a date | Independent statistics publisher; one request covers the whole slate | Summary only; its game pages carry bench and pitcher-v-team splits | **Secondary** (settlement lineage 2) |
| Kyodo News via Yahoo! News | `news.yahoo.co.jp/articles/...` "X7―3Y（22日）" wire format | NPB | Final score, key plays, W/L | Independent wire; fast | The same wire is syndicated to many papers; count once | **Secondary** (settlement lineage 3) |
| Nikkan Sports (Yahoo! News) | staff reports | NPB | Final, starter lines, decisive play | Staff-bylined, independent of Kyodo | Narrative | **Secondary** |
| Mynavi News "プロ野球試合結果" series | `news.mynavi.jp/article/YYYYMMDD-baseball_gameNN/` | NPB | — | — | **AI-generated; omitted a 3-run inning** | **EXCLUDED for settlement** |
| NBL official match data | `schedule.nbl.com.au/api/calendar/match?match=<uuid>&league=NBL` | NBL | Status/phase (`COMPLETE`/`FINAL`), scores, play-by-play timestamps (actual tip), lead tracker | Field owner; exposes the actual start | **Contains `betting`/`odds` objects: parse programmatically and skip those keys; never display the raw JSON.** Data vendor is Sportradar, which may be shared with other publishers | **Primary for settlement only**; quarantined from forecast evidence (existing note) |
| ESPN NBL / WNBA / WTA site API | `site.api.espn.com/apis/site/v2/sports/basketball/nbl/scoreboard?dates=YYYYMMDD`; `…/summary?event=<id>`; `…/tennis/wta/scoreboard` | NBL, WNBA, WTA | Status, box, linescores | Keyless; independent publisher | **Returns HTTP 403 with a browser User-Agent**; the NBL scoreboard needs `?dates=` or a UA-less request; the ESPN "Final" flag can lag the league feed by minutes | **Secondary** |
| WTA match feed | `api.wtatennis.com/tennis/tournaments/<id>/<year>/matches/` | WTA | State, set scores, ResultString | Field owner | **Live (state P) matches can drop out of the list** (observed 21:33 AEST on LS008). Re-query, or use ESPN as a live cross-check | **Primary** |

## F. Data-quality observations

- The P-494-onward log's "Settled Logs" index said P-484–P-488 and P-492 were recorded in Part 5. **Part 5 holds custody rows only.** The full cards and retrospectives existed only in `C:\Users\danie\Documents\Sports Research\…MERGED_P482_ONWARD.md`, outside git. They are now archived in-repo (`archive/mini_logs/originals_2026-09-23/…DOCUMENTS_COPY_2026-09-23.md`). Part 5's pointers are corrected in the import.
- The Drive copy of `PREDICTION_LOG_COMBINED_5.md` is still the 21 Sep rollover template (3,361 bytes: "None yet"), while the local copy holds P-482 onward. **Drive is stale relative to local.** It was not touched here.
- A summarising fetch returned an internally inconsistent NPB box (P-491 card). Raw HTML parse fixes it. This recurs with M20.

### F.1 Card-completeness audit (`audit_card_controls.py --settlement`, RULES_GENERAL §16.8)

**Mechanical output.**
- Run on the as-issued P-494-onward log: every card was flagged as missing BLOCKING fields 2, 3 and 5a, and P-491, P-493 and P-494 also field 7.
- Run on the P-489 attachment: fields 2, 3, 5a, 7 and 10 flagged.

**Known false negatives.**
- The script opens a card at a `P-###` heading and closes it at the next `## ` heading. P-494's family table, centre/width and dependence fields sit under "## Entry 1" / "## Entry 2" headings, so they were cut away. P-491's fields sit in bold-label paragraphs rather than the phrasings the script looks for.
- **A mechanical FAIL here is not a finding without the manual check below.** A tooling fix is proposed in the Document Update Mapping.

**Manual field check of the issued cards** (Y = printed; P = partial; N = not printed):

| Card | 1 method/controls | 2 families with mass | 3 centre/width/edge | 4 complements R1/R2 | 5 P(R1∧R2) | 5a P(¬R1∧¬R2) | 5b FORCED_PAIR / push | 6 representative R1 outcome | 7 participants (lineup/bench/coach) | 8 AGGREGATE_ONLY / SE | 9 settlement route |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P-489 (22 Sep) | Y | Y (BB-B1–B9 weights) | P (centre 5.3; no numeric width) | P (kill paths listed, not itemised by mass) | N | N | P ("forced complement") | Y (3–2) | P (starters Y; orders N; bullpens Y; coaches N) | N | N |
| P-491 | Y | Y (nine branches; simulated masses) | Y (mean 7.19; P(≥8), P(=7), P(≤6); ±0.2 sensitivity) | Y | Y (0.354) | Y (0.152) | Y (push 0.104) | Y (Lotte 3–2) | P (orders Y; bench/coach N) | N | P (NPB box named) |
| TMP-G25 (R1) *(carried)* | Y | N (forced rank) | N | N | P ("joint unknown", no bounds) | N | Y ("one forced total decision") | N | P (orders Y; bench partial) | N | P |
| P-493 *(carried)* | Y | P (low/high branches described, no masses) | Y (8.68; NB shape 4) | P | Y (Fréchet bounds) | Y (bounds) | Y | Y (5–4 KIA) | P (orders Y; national-team absences Y; bench N) | N | N |
| TMP-NBL | N | N | N | N | N | N | N | Y (91–88) | P (roster wrong) | N | N |
| P-494 *(carried)* | Y | Y (B1–B6, sum 1.0000) | Y (mean/median/SD; normalised edges) | Y | Y (0.106) | Y (0.046) | Y | Y (6-2 6-2) | Y (bench N/A; coaches `COACH_NOT_RETRIEVED`) | Y | Y (S1+S4+S5) |

`BODY_NOT_CARRIED`: TMP-20260922-WNBA-DAL-PHX (one row survives). It is recorded as unauditable, not as non-compliant.

## G. Recurring blind spots

| Blind spot | Cards this batch | Prior occurrences | Classification |
|---|---|---|---|
| Control listed, not executed (M15) | P-489 (control 26, override 2), NBL (METHOD §4) | P-345–P-371 (0/13), P-482 | **Cross-sport recurring** |
| Posted lineup / roster not retrieved or wrong (M19, G14.2) | P-489 (BB-P2 PARTIAL), NBL (wrong roster) | P-357, P-362, P-365, P-492 | **Cross-sport recurring** |
| START_CROSSED issuance | P-489 | P-485, P-492, P-483 | **Recurring (one external session)** |
| Totals stacking off one channel (M3 / control 26) | P-489 | P-348, P-356, P-351 | **Baseball recurring** |
| One-game recency used as a rate (R-1) | NBL | P-453, P-492 | **Cross-sport recurring** |
| One-sided mechanism (G-L2) | NBL (travel fatigue) | P-335, P-339, P-342, P-492 | **Cross-sport recurring** |
| ID claims living only in external transcripts | P-487 WNBA | P-484 collision (P-492) | **Emerging (ID custody)** |

## H. Items requiring more evidence before becoming formal rules

- `O-NPB-ERA-CENTRE`: a third NPB/KBO Under-at-#1 case built on ERA anchoring before any checklist promotion. It must also be shown that team-rate anchoring would have changed the rank *prospectively*.
- `O-ROSTER-NAME-COLLISION`: one case.
- `O-START-MARKER`: two feeds observed; confirm the field definitions (NBL `play_by_play[].timestamp`, WTA elapsed-time back-calculation) before use.
- `C-RUN-CENTRE-BIAS`: the NPB/KBO leg now has contradictory signs. Keep collecting; no tilt.
- WNBA/NBL: no pattern claim from one unauditable card and one card without a distribution.
- Three carried-over records (TMP-G25, P-493, P-494) contribute nothing until they are settled in the P-495-onward log.


# Document Update Mapping

"Implemented 2026-09-23" means the change was made in the local repository in this pass, as part of the combined-log import (Part 5 §"2026-09-23(c)"). "Proposed" means it is recorded for a later pass or for the operator to decide. **No Google Drive document was modified.**

| Learning / change | Existing document | Section | Status |
|---|---|---|---|
| Settled records P-489, P-491 (cards, settlement, retrospectives) | `PREDICTION_LOG_COMBINED_5.md` | new §"2026-09-23(c)" | Implemented 2026-09-23 |
| Temporary-ID records TMP-20260922-WNBA-DAL-PHX, TMP-20260923-NBL-CNS-TAS (settled), TMP-20260923-NPB-CHU-DB-G25 (pending) | `PREDICTION_LOG_COMBINED_5.md` §"2026-09-23(c)"; `GAME_LOG_STATUS_CURRENT.md` noncanonical table | — | Implemented 2026-09-23 |
| P-489 identity correction (22 Sep game; R1 split to TMP-G25) and P-487 two-claimant hold | `PREDICTION_LOG_COMBINED_5.md` (appended correction; the earlier reconciliation table is preserved); `GAME_LOG_STATUS_CURRENT.md` rows P-487, P-489 | — | Implemented 2026-09-23 |
| Pointer repair: full P-484–P-486, P-488, P-492 records live in `archive/mini_logs/originals_2026-09-23/PREDICTION_MINI_RUNNING_LOG_MERGED_P482_ONWARD_DOCUMENTS_COPY_2026-09-23.md` | `GAME_LOG_STATUS_CURRENT.md` rows; `PREDICTION_LOG_COMBINED_5.md` custody note | — | Implemented 2026-09-23 |
| L-20260923-01 `O-ID-DATE-STARTER-MATCH` (PROMOTED_PROCESS) | `EXTERNAL_LOGGING_WORKFLOW.md`; `RULES_GENERAL.md` (identity gates G0–G6 pointer); `LEARNING_REGISTER.md` | new dated sections | Implemented 2026-09-23 |
| L-20260923-02 `O-EXTERNAL-ID-CLAIM-SWEEP` (PROMOTED_PROCESS) | `EXTERNAL_LOGGING_WORKFLOW.md`; `LEARNING_REGISTER.md` | new dated sections | Implemented 2026-09-23 |
| L-20260923-03 `O-NPB-ERA-CENTRE` (TESTING); P-489 control-26 non-execution; P-361 kill-path recurrence | `RULES_BASEBALL.md` §"2026-09-23" settlement learning; `LEARNING_REGISTER.md` | new dated sections | Implemented 2026-09-23 (TESTING, no checklist promotion) |
| L-20260923-04 P-491 construction as the default baseball template | `RULES_BASEBALL.md` §"2026-09-23" | — | Implemented 2026-09-23 (construction note, no coefficient) |
| L-20260923-05 `C-RUN-CENTRE-BIAS` NPB leg data points | `LEARNING_REGISTER.md` | — | Implemented 2026-09-23 (accrual) |
| L-20260923-06 `O-ROSTER-NAME-COLLISION`; NBL Rank-1 review | `RULES_BASKETBALL.md` §"2026-09-23"; `LEARNING_REGISTER.md` | — | Implemented 2026-09-23 (OBSERVATION) |
| L-20260923-07 `O-START-MARKER` (NBL tip 19:36:09 v 19:30) | `RULES_BASKETBALL.md` §"2026-09-23"; `LEARNING_REGISTER.md` | — | Implemented 2026-09-23 (OBSERVATION) |
| L-20260923-08 Mynavi AI-generated recaps excluded | `DATA_SOURCE_REGISTER.md` §"2026-09-23"; `SOURCES.md` §"2026-09-23" | — | Implemented 2026-09-23 |
| L-20260923-09 Feed behaviour: WTA live-drop; ESPN NBL lag; ESPN 403 with browser UA; NBL feed betting keys; Flashscore feed fields | `DATA_SOURCE_REGISTER.md`; `SOURCES.md` | — | Implemented 2026-09-23 |
| NPB box raw-HTML parse, Sports Navi results, Kyodo wire, Nikkan staff reports as settlement lineages | `DATA_SOURCE_REGISTER.md`; `SOURCES.md` | — | Implemented 2026-09-23 |
| L-20260923-10 "record location" pointer check at import | `EXTERNAL_LOGGING_WORKFLOW.md` §"2026-09-23" | — | Implemented 2026-09-23 |
| Audit-script segmentation false negatives (a card whose fields sit under non-`P-###` `##` headings is truncated) | `audit_card_controls.py` | — | **Proposed** (tooling change not made in this pass; recorded in `EXTERNAL_LOGGING_WORKFLOW.md`) |
| Recover the P-487 (Dallas @ Phoenix) card body from the external session; operator confirms P-487 → WNBA | `PREDICTION_LOG_COMBINED_5.md` / `GAME_LOG_STATUS_CURRENT.md` at reconciliation | — | **Proposed — operator action** |
| Full verbatim import of P-484–P-486, P-488 and P-492 retrospectives into Part 5 (currently custody rows plus an in-repo archive copy) | `PREDICTION_LOG_COMBINED_5.md` | — | **Proposed** (needs G-L13 re-verification of those finals) |
| Carried-over live records TMP-G25, P-493, P-494 | New mini log `Mini Prediction Log - P-495 onward - 2026-09-23/`; `GAME_LOG_STATUS_CURRENT.md` | — | Implemented 2026-09-23 (custody transfer) |
| Proposed new document | none | — | No new Markdown document is justified; every item has an existing home |

## Settled logs (first to most recent, by game start)

1. `TMP-20260922-WNBA-DAL-PHX` — Dallas Wings @ Phoenix Mercury, 22 Sep 12:00 AEST — PHX 87–86. Rank #1 (Mercury +5.5) **W**; winner call **L**. Remaining rows `BODY_NOT_CARRIED`. Claims P-487 (held).
2. `P-489` — Chunichi @ Yokohama DeNA, **game 24**, 22 Sep 19:00 AEST — DeNA 7–3. #1 Under 6.5 **L**, #2 DeNA ML **W**, #3 Dragons +1.5 **L**, #4 Over 6.5 **W**; winner **W**.
3. `P-491` — Orix @ Chiba Lotte, 23 Sep 18:00 AEST — Orix 1–0. #1 Buffaloes +1.5 **W**, #2 Under 7.0 **W**, #3 Marines ML **L**, #4 Over 7.0 **L**; winner **L**.
4. `TMP-20260923-NBL-CNS-TAS` — Cairns v Tasmania, 23 Sep 19:30 AEST — CNS 93–87. #1 JackJumpers +2.5 **L**, #2 Under 186.5 **W** (contract ambiguity recorded), #3 Over 186.5 **L**, #4 Taipans −2.5 **W**; winner **L**. Claims P-487 (held).

## Logs still awaiting settlement (first to most recent, by game start) — carried over to the P-495-onward mini log

1. `TMP-20260923-NPB-CHU-DB-G25` — Chunichi @ Yokohama DeNA, **game 25**, 23 Sep 19:00 AEST — LIVE at 21:40 (3–3, 7th).
2. `P-493` — KIA @ Doosan, 23 Sep 19:30 AEST — LIVE at 21:38 (2–2, 7th).
3. `P-494` — Andreeva v Sasnovich (live-issued view), 23 Sep ≈20:38 AEST — LIVE at 21:39 (Andreeva 6-2, 3-2).

**Performance status reminder:** this mini log is **not performance-eligible**. Its results serve learning, methodology refinement, source evaluation and algorithm improvement only.


## Appendix A — Request disposition carried from the P-494-onward log (no forecast, no ID, nothing to settle)

<!-- BEGIN VERBATIM ISSUED RECORD: Khonkaen United v Royal Thai Navy disposition (heading levels demoted by two; text unchanged) -->

##### Request disposition — Khonkaen United vs Royal Thai Navy FC (2026-09-23)

**Disposition:** NO FORECAST ISSUED for this soccer event; no canonical ID was allocated to the request. No retrospective performed. P-494 belongs to the earlier WTA live view; this no-issue disposition consumes no ID, and P-495 is next.

**Event/time check.** The request’s estimated 21:00 AEST start converts to 11:00 UTC. The Thai League’s official 2026/27 Chang FA Cup notice confirms the qualifying-round date window (22–23 September), but not this exact pairing or its kickoff. FotMob, SportScore, and AiScore’s timezone-explicit match details list Khonkaen United vs Siam/Royal Thai Navy at 11:00 UTC (21:00 AEST); AiScore also displays “19:00” with no timezone label. Global Sports Archive’s current-season Navy FC listing shows Khon Kaen United vs Navy FC at 13:00, also without a timezone. These records do not establish one exact kickoff. At the final state refresh, 2026-09-23 21:00:30 AEST, SportScore still showed “Upcoming,” no events and no announced lineups; FotMob and AiScore exposed no verified live-state transition. Since neither the kickoff conflict nor an official/field-owner PREGAME state was resolved, the framework’s pregame-state gate failed closed.

**Other blocking items.** No confirmed starting XI, goalkeeper, bench, or team-specific availability report was retrievable by the final check. A Scores24 page listed Khonkaen player Phanuphong Phonsa as injured, but I could not corroborate it with an official club/competition source; it is not treated as verified availability evidence. The user supplied first-half O/U 0.5 and match O/U 2.5 goal contracts, but supplied no exact corner market, line, or settlement definition. No corner exposure/rate chain or scenario branches were established. These gaps prevent an honest ordered five-pick card or potential-winner claim under `RULES_SOCCER.md` and the current pregame controls.

**Source record (retrieved 2026-09-23, approximately 20:56–21:04 AEST; final state check 21:00:30 AEST).**

- [Thai League announcement: Chang FA Cup 2026/27 qualifying-round draw and schedule window](https://thaileague.co.th/v1/news-index/%E0%B8%99%E0%B8%B3%E0%B9%81%E0%B8%A3%E0%B8%98%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%8A%E0%B8%B2%E0%B8%95%E0%B8%A3%E0%B8%B2%E0%B8%8A%E0%B8%B2%E0%B8%87-%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B8%81%E0%B8%B1%E0%B8%9A-%E0%B8%AA%E0%B8%A1%E0%B8%B2%E0%B8%84%E0%B8%A1%E0%B8%AF-%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%9E%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%88%E0%B8%B1%E0%B8%9A%E0%B8%AA%E0%B8%A5%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%81%E0%B8%82%E0%B9%88%E0%B8%87%E0%B8%82%E0%B8%B1%E0%B8%99%E0%B8%9F%E0%B8%B8%E0%B8%95%E0%B8%9A%E0%B8%AD%E0%B8%A5-%E0%B8%8A%E0%B9%89%E0%B8%B2%E0%B8%87-%E0%B9%80%E0%B8%AD%E0%B8%9F%E0%B9%80%E0%B8%AD-%E0%B8%84%E0%B8%B1%E0%B8%9E-%E0%B8%A4%E0%B8%94%E0%B8%B9%E0%B8%81%E0%B8%B2%E0%B8%A5-202627-%E0%B8%A3%E0%B8%AD%E0%B8%9A%E0%B8%84%E0%B8%B1%E0%B8%94%E0%B9%80%E0%B8%A5%E0%B8%B7%E0%B8%AD%E0%B8%81/) — official competition context/date window; not an exact match-state source.
- [FotMob event page](https://www.fotmob.com/matches/siam-navy-fc-vs-khonkaen-united-fc/403mxthy) — fixture identity, 11:00 UTC listing, venue/form; no confirmed lineup or live transition visible at final check.
- [SportScore event page](https://sportscore.com/football/match/khonkaen-united-vs-royal-thai-navy-fc/) — fixture/time cross-check; at final check page still said upcoming, no events, lineup not announced, exact ground unconfirmed on its feed. The page also displayed adjacent price fields; those were incidentally visible and not used.
- [AiScore event page](https://www.aiscore.com/live/football-khonkaen-united-vs-royal-thai-navy-fc) — fixture, 11:00 UTC in its match-info text, recent results and no verified state transition; its separate “19:00” display is timezone-ambiguous.
- [Global Sports Archive Navy FC page](https://globalsportsarchive.com/en/soccer/team/navy-fc/1210/overview) — identifies Navy FC in the 2026/27 Thai League III and lists the 23 Sep Khon Kaen fixture at 13:00 without a timezone; this conflicts with the 11:00 UTC listings and does not settle kickoff time.
- [FA Thailand Thai League 2 results page](https://fathailand.org/match-results/26/132?language=en) — shows a Navy Football Club result dated 19 Sep but the year/season context was not clear in the retrieved view; quarantined and not treated as proof of a different current club or used directionally.
- [Sanook fixture page](https://www.sanook.com/sport/1672379/) — Thai-language fixture and historical results; not used for live state or current lineups.
- [Scores24 event page](https://scores24.live/hu/soccer/m-23-09-2026-khonkaen-united-royal-thai-navy-fc) — uncorroborated Phanuphong Phonsa injury listing only; quarantined from directional use.

Method: local `METHOD.md` MDS-2026.09.19-v4.3 / CR-2026.09.21-3, `CONTROLS.md`, `RULES_SOCCER.md` identity, participant, corner-process and pregame-state gates. No prices, odds, fantasy, or tipster claims were used as evidence. A match-state page and one search-result snippet incidentally surfaced adjacent odds/market fields; they were not used or cited for any forecast reasoning. This is a request disposition only, not a scored prediction.

<!-- END VERBATIM ISSUED RECORD: Khonkaen United v Royal Thai Navy disposition -->
