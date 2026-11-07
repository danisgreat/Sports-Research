<!-- SETTLEMENT-FORMAT: mini-settlement-10 / EXTERNAL_DRAFT_WITHOUT_FROZEN_MINI — revision-2 package -->
# REVISION-2 — Seven-event sporting settlement review, row DRAFT-E06 (Henderson Silver Knights @ Ontario Reign)

**Document:** `SEVEN_GAME_REVIEW_DRAFT-E06_REVISION_2.md` · prepared 2026-10-21 ≈01:20 AEDT.
**Parent document:** `MINI LOGS TO BE SETTLED/Sports_Research_Seven_Game_Settlement_2026-10-17_18_READ_ONLY.md` (revision-1 for DRAFT-E01…E07). That file is not edited.
**Mode / authority:** `LOCAL_MINI_SETTLEMENT` (evidence-only, no frozen mini exists for these drafts); `PUBLISHED_MAIN_PINNED 3e29a58693e2ed02ff862e9bf0f751af2feadee1`; run in the repository session (ENV-v1 deviation disclosed); no repository writes. Reading receipt as in `20261018X7Q4M9R2_SETTLEMENT.md` (same folder).
**Scope:** revision-1 left E06 `PROVISIONAL_SPORTING` because the AHL game centre showed a stale 0–0 placeholder and the only final came from an automated Reddit bot. This revision supplies the official league record. No other row changes.

## Sources
| Source ID | URL / route | Fields observed | Publisher | Retrieval |
|---|---|---|---|---|
| E6-S01 HockeyTech AHL game summary (official league stats feed) | `https://lscluster.hockeytech.com/feed/index.php?feed=gc&tab=gamesummary&game_id=1029155&key=50c2cd9b5e18e390&client_code=ahl&fmt=json&lang_code=en` (also `feed=statviewfeed&view=gameSummary`) | `final=1`, status 4; Ontario (home) **2**, Henderson (visitor) **5**; goals by period HSK 0/2/3, ONT 0/1/1; three periods only, `shootout 0`; Henderson goals P3 18:42 and 19:31 flagged **empty net**; start 18:05 PDT, end 20:42 PDT; attendance 6,274; Toyota Arena | AHL / HockeyTech (league stats owner) | 2026-10-21 ≈00:42 AEDT |
| E6-S02 Club and independent recaps (search-visible) | `https://lakingsinsider.com/2026/10/17/reign-final-hsk-5-ont-2-lord-hicketts/`; `https://hockeyroyalty.com/2026/10/18/penalties-continue-to-be-a-problem-in-the-ontario-reigns-5-2-loss-to-the-henderson-silver-knights/`; `https://www.hendersonsilverknights.com/game-break-down-10-17-at-ontario/` | 5–2 Henderson; two empty-netters; Henderson's first road win | Independent + club | search 2026-10-21 |

Note: one search hit, "SILVER KNIGHTS DEFEATED, 5-2, BY REIGN", is an older reverse result at Orleans Arena and was rejected as a different event.

<!-- BEGIN SETTLEMENT DRAFT-E06 revision-2 -->
### Settlement · DRAFT-E06 · Henderson Silver Knights @ Ontario Reign (AHL game 1029155) · 2026-10-21T01:20+11:00
**Revision:** revision-2 · parent revision-1 · effective 2026-10-21T01:20+11:00 · affected keys: Henderson ML, Ontario ML, Over 5.5, Under 5.5 (+ four derived diagnostic lines) · changes: `WIN_PROVISIONAL/LOSS_PROVISIONAL → WIN/LOSS` (reason: official league record E6-S01 plus independent recaps now corroborate the bot feed exactly).
**Card state:** `SETTLED_SPORTING` (original draft `NOT_ISSUED`; operator terms unknown).
**Final event:** **Henderson 5 – Ontario 2**, regulation (HSK 0-2-3, ONT 0-1-1); no OT/SO. Start 18:05 PDT, end 20:42 PDT (2026-10-18 12:05–14:42 AEDT). Two Henderson empty-net goals at 18:42 and 19:31 of P3.
**Evidence:** A (league stats owner) + independent recaps.

| Original supplied proposition | Original estimated p | revision-1 | revision-2 grade |
|---|---:|---|---|
| Henderson Silver Knights ML (full match incl. OT/SO assumed) | 0.471 | WIN_PROVISIONAL | **WIN** |
| Ontario Reign ML | 0.529 | LOSS_PROVISIONAL | **LOSS** |
| Total Over 5.5 goals | 0.511 | WIN_PROVISIONAL | **WIN** (7) |
| Total Under 5.5 goals | 0.489 | LOSS_PROVISIONAL | **LOSS** |
| Derived (diagnostic, not offered): Over 3.5 ≈0.819 | — | WIN_PROVISIONAL | **WIN** |
| Derived: Under 7.5 ≈0.774 | — | WIN_PROVISIONAL | **WIN** |
| Derived: Ontario +1.5 ≈0.754 | — | LOSS_PROVISIONAL | **LOSS** (lost by 3) |
| Derived: Henderson +1.5 ≈0.710 | — | WIN_PROVISIONAL | **WIN** |

**Expected vs final:** regulation centres HSK 2.80 / ONT 2.95 / total 5.75 → 5 / 2 / 7: total +1.25; Ontario −0.95; Henderson +2.20.
**Winner call:** Ontario ≈0.529 → **incorrect**.
**R2/R3:** official 5–2 regulation; 7 ≥ 6; Henderson outright. **R8:** both empty-net goals came after Ontario pulled its goalie at 2–3/2–4; the revision-1 conditional review anticipated an empty-net margin tail for Ontario +1.5 — confirmed. **R9:** the original draft could not be checked against an official starting-goalie release; post-game goalie usage (Slukynsky for Ontario; Whitehead credited with the win in relief for Henderson, per E6-S02) is outcome evidence only. **R10:** `PULL_GOALIE_TAIL` for the derived Ontario +1.5 row (non-cohort). **R12:** `NO_CHANGE / LEARNING_LABEL_CANDIDATE`.
<!-- END SETTLEMENT DRAFT-E06 revision-2 -->

## Effective manifest for the seven-event review after this revision
| Metric | revision-1 | after revision-2 |
|---|---|---|
| Source-confirmed completed events | 6 | **7** |
| Provisional terminal | 1 (E06) | **0** |
| Source-confirmed supplied-proposition grades | 28: 14 W / 14 L | **32: 16 W / 16 L** |
| Formal issued primary decisions | 0 | 0 |
| Winner diagnostics (source-confirmed) | 4 correct / 2 incorrect | **4 correct / 3 incorrect** |
| Still open | original mini custody, E07 original document, operator terms, final times | unchanged (E06 final time now known: 20:42 PDT) |

## UNRESOLVED_CARRYOVER update
U02 (AHL terminal corroboration) → **CLOSED** by E6-S01. All other revision-1 queue items (U01, U03–U06) unchanged; no new attempts on them in this revision.

## Verification (revision-2 scope)
S1 PASS (E06 only) · S3 PASS (original p copied) · S4 PASS · S5 PASS · S6 PASS (32 = 16 + 16) · S13 PASS (revision-2 names parent revision-1) · S17 PARTIAL (Markdown sources; CSVs at prompt 4) · S18 PASS (no IDs assigned; `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT`). Other checks unchanged from revision-1.
