<!-- SETTLEMENT-FORMAT: mini-settlement-10 -->
# SETTLEMENT REVISION DOCUMENT — MINI 20261018Q7N4T9B2 — revision-2 package

**Document:** `research/active_minis/20261018Q7N4T9B2_SETTLEMENT_REVISION_2.md` · written 2026-11-07T21:15:50+11:00 (clock read). The revision-1 document is **not** overwritten.
**Mode / authority:** `LOCAL_MINI_SETTLEMENT` (prompt 3, P-2026.10.22-v24.0) under control **CR-2026.11.07-R1**. Owner decision, 7 November 2026: "all basketball games have overtime inclusive lines, so do it accordingly, if this hasnt been included in the rules, then include it now". The rule was not in the rules (RULES_BASKETBALL BK-P4 required the operator's endpoint), so it is now **BK-OT-1** (RULES_BASKETBALL §0.1, §0.5, §8.1, controls 6 and 13; CORE; CURRENT_RULES). `LOCAL_WORKING_TREE`, branch `main`, HEAD `ef9eb9c7448837fa0e6b2185f8a5b45050d4f457` (= `origin/main`) with the BK-OT-1 rule edits in the same working tree.
**Reading receipt:** as in `2026101679B3FBCC8D_SETTLEMENT_REVISION_3.md` (same folder), plus RULES_BASKETBALL as amended and the revision-1 settlement of this mini.

## Frozen source, prior package and scope
- **FROZEN_SOURCE (unchanged, already canonical):** `research/verification/mini_import_P-601_P-622_2026-10-21-1/inputs/20261018Q7N4T9B2/ORIGINAL_MINI.md` — 172,799 bytes, SHA-256 `89146dbb66e2e49206a92bad4e049bd3d27b701b055f42d8403e259cae8dc85d`, card markers G0001–G0004, first key `LOCAL-20261018Q7N4T9B2-G0001`, last `…-G0004`. Re-hashed before writing; equals the import receipt.
- **Prior settlement:** revision-1 document `…/inputs/20261018Q7N4T9B2/20261018Q7N4T9B2_SETTLEMENT.md` (26,992 bytes, `9580956e315ec3cdc5e4898e1d5559d1ce6cfb777397339b40f9f0ef55a71813`), imported in Part 8.
- **This document appends** `revision-2` for G0002 (P-616) only: the endpoint definition status of all four rows moves from `UNKNOWN_DEFINITION` (grade-changing) to `FROZEN_FRAMEWORK_CONVENTION` under BK-OT-1. **No grade changes:** revision-1 already graded the rows on the full game including overtime, which the card's A2 had declared. G0001 (P-615, B.ONE) and the other cards are untouched: no overtime was played in them, so BK-OT-1 confirms their existing grades.

## LOCAL_ID_MAPPING
Existing canonical reference retained (MINI-v2): `LOCAL-20261018Q7N4T9B2-G0002` → **P-616** (2026-10-21 import). No new event; no P-number planned.

## Source discovery, corroboration and reuse register
**Information completion: `INFORMATION_INCOMPLETE`** — the field-owner (pba.ph) box is still unread; the endpoint is now closed by framework convention.

| Source ID | URL / route | Fields observed / missing | Publisher / independence | Retrieval | Reuse limits |
|---|---|---|---|---|---|
| Q7R2-S01 Tribune | `https://tribune.net.ph/2026/10/18/converge-clips-tnt-in-ot` | Converge 114–112 in OT; 12–2 Converge run to force OT; Stockton layup from 112–112 with 11.3 s left in OT | Independent media | 2026-11-07 (search) | Corroboration only |
| Q7R2-S02 GMA | `https://www.gmanetwork.com/news/sports/basketball/1006322/pba-alec-stockton-saves-the-day-as-converge-overcomes-tnt-in-ot/story/` | 114–112 OT; TNT led 106–101 with 1:33 left in regulation | Independent media | 2026-11-07 (search) | Corroboration only |
| Q7R2-S03 Philstar | `https://www.philstar.com/sports/2026/10/19/2564172/fiberxers-steal-ot-thriller` | Converge erased a 10-point regulation deficit, won in OT | Independent media | 2026-11-07 (search) | Corroboration only |
| revision-1 sources | RealGM box score and five Philippine reports (revision-1 register) | Regulation 106–106 (XERS 27-28-19-32, TNT 35-21-30-20); OT 8–6; final 114–112 | as recorded | 2026-10-21 | unchanged |

**REQUIREMENT_CLOSURE**
| Field | Status | Next · actor · due · automation |
|---|---|---|
| Endpoint (OT in or out) for all four rows | **CLOSED** — `FROZEN_FRAMEWORK_CONVENTION` (BK-OT-1) | — |
| Final and regulation scores | CLOSED (revision-1 B; three more independent reports agree) | pba.ph box for a field-owner upgrade · settlement reviewer · NOT_SCHEDULED |
| Other operator terms (void, abandonment) | OPEN, non-grading for this completed game | owner · NOT_SCHEDULED |
| Exact final wall-clock time | OPEN (`UNKNOWN`) | pba.ph gamebook · settlement reviewer · NOT_SCHEDULED |

<!-- BEGIN SETTLEMENT LOCAL-20261018Q7N4T9B2-G0002 revision-2 -->
### Settlement · LOCAL-20261018Q7N4T9B2-G0002 (P-616) · TNT Tropang 5G v Converge FiberXers — endpoint under BK-OT-1 · 2026-11-07T21:15:50+11:00
**Revision:** revision-2 · parent revision-1 · effective 2026-11-07T21:15:50+11:00 · affected keys: Combined Under 221.5, Giga (TNT) +2.0, Fiberxers (Converge) −2.0, Combined Over 221.5 · changes: definition status `UNKNOWN_DEFINITION` (grade-changing) → **`FROZEN_FRAMEWORK_CONVENTION`**; card state `ENDPOINT_SENSITIVE` → **`SETTLED`**; grades unchanged (reason: owner convention BK-OT-1 of 7 November 2026, under which every basketball line includes overtime; control CR-2026.11.07-R1).
**Final event (unchanged):** **Converge 114 – TNT 112 after overtime.** Regulation 106–106; OT 8–6. Full-game total 226 (regulation 212); full-game TNT margin −2 (regulation 0). Three further independent reports (Q7R2-S01 to S03) agree. Final wall-clock `UNKNOWN`.
**Definition:** full game including overtime, BK-OT-1, `FROZEN_FRAMEWORK_CONVENTION`; it matches the card's own A2 interpretation. The regulation-only reading is withdrawn as a settlement alternative and kept only as attribution (control 13). **Evidence:** B.

| Rank | Exact original proposition | Original p_card (decisive) | Original W / P / L | Grade (incl. OT, BK-OT-1) | Crossed in regulation? | Evidence | Definition | Counts toward wins |
|---|---|---:|---|---|---|---|---|---|
| 1 | **Combined Total Under 221.5** | 0.524 | 0.524 / 0 / 0.476 | **LOSS** (226) | No: regulation 212 was under; OT supplied 14 points | B | FROZEN_FRAMEWORK_CONVENTION | Yes |
| 2 | **Giga (TNT) +2.0** | 0.520 | 0.510 / 0.020 / 0.470 | **PUSH** (lost by exactly 2) | Regulation tie; OT decided it | B | FROZEN_FRAMEWORK_CONVENTION | Yes — PUSH excluded from rate |
| 3 | Fiberxers (Converge) −2.0 | 0.480 | 0.470 / 0.020 / 0.510 | **PUSH** | as above | B | FROZEN_FRAMEWORK_CONVENTION | No |
| 4 | Combined Total Over 221.5 | 0.476 | 0.476 / 0 / 0.524 | **WIN** (226) | No: crossed only in OT | B | FROZEN_FRAMEWORK_CONVENTION | No |

**Top-two result (unchanged):** `ONE_DECISIVE` — R1 LOSS, R2 PUSH; decisive denominator 1; primary wins 0/1; 1 PUSH.
**Proper scores (unchanged):** binary Brier R1 0.2746, R4 0.2746; push rows categorical half-sum 0.7207 (R2, R3). These rows now enter the **headline** view (evidence B with definition `FROZEN_FRAMEWORK_CONVENTION`, SCV §2a) instead of being held for an unknown definition.
**R3 (update):** the endpoint is no longer open; full game 226 ≥ 222 → Over; TNT −2 on a +2.0 handicap → push. **R6/R7/R8:** unchanged; the decisive mechanism was the overtime period, which the card had flagged as an unmodelled branch. **R10 (update):** failure class for R1 stays `OT_TAIL_ENDPOINT / NEAR_COINFLIP`; the endpoint part is now a settled convention, not an open definition. **R11 (update):** BK-OT-1 makes the explicit OT branch mandatory in every basketball price (RULES_BASKETBALL control 6); the PBA-history test stays `PROPOSED_NOT_TESTED`. **R12:** `NO_CHANGE` to grades. Other R sections and the eight-part review are unchanged.
<!-- END SETTLEMENT LOCAL-20261018Q7N4T9B2-G0002 revision-2 -->

## UNRESOLVED_CARRYOVER (supersedes U-603; other rows unchanged)
| ID | Event key | Queue | Original card | Latest revision | Open field | Responsible actor | Next source + exact field | Due | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q7R2-Q1 | G0002 (P-616) | UNRESOLVED_EVIDENCE (upgrade only, non-grading) | G0002 | revision-2 | Field-owner box; final time | Settlement reviewer | pba.ph game page | Next owner-invoked review | UNKNOWN | 2026-11-07 (search; pba.ph not surfaced) | NOT_SCHEDULED |
| — | Other operator terms, final times, revision-1 items | unchanged | — | revision-1 | as recorded | as recorded | as recorded | as recorded | as recorded | no new attempt | NOT_SCHEDULED |

## Learning record additions (LEARN-v2)
| Local key | Final score | Regulation | Decision | Final time | Terminal source |
|---|---|---|---|---|---|
| G0002 (P-616) | Converge 114 – TNT 112 (OT) | 106–106 | Converge | UNKNOWN | revision-1 RealGM box; Q7R2-S01 to S03, retrieved 2026-11-07 |

## SETTLEMENT_MANIFEST (effective state after revision-2)
| Item | revision-1 | after revision-2 |
|---|---|---|
| Rows W / L / PUSH / UNRESOLVED | 8 / 8 / 2 / 0 | 8 / 8 / 2 / 0 (unchanged) |
| Primary (ranks 1–2) | 2 W / 5 L / 1 P | 2 W / 5 L / 1 P (unchanged) |
| Rows with a grade-changing open definition | 4 (P-616) | **0** |
| Revision chain | revision-1 all keys | **revision-2** for G0002; revision-1 for G0001, G0003, G0004 |

**MINI_SETTLEMENT review row:** `2026-11-07 | MINI 20261018Q7N4T9B2 revision-2 | 4 events | grades unchanged | P-616 endpoint closed by BK-OT-1 (FROZEN_FRAMEWORK_CONVENTION) | NO_CHANGE | no rank changes`.

## Verification (S1–S19, revision-2 scope)
S1 PASS · S2 PASS (frozen source re-hashed = import receipt) · S3 PASS (p_card and W/P/L copied literally) · S4 PASS · S5 PASS (evidence B unchanged; definition upgrade made by this new revision, never silently) · S6 PASS (8 + 8 + 2 = 18) · S7 PASS · S8 PASS (Rank-1 loss review unchanged and still valid) · S9 PASS (no rank change) · S10 PASS (nothing backfilled) · S11 PASS (scores unchanged) · S12 PASS · S13 PASS (revision-2 names parent revision-1) · S14 PASS · S15 PASS (no price, line or odds source) · S16 PASS (manual check against the frozen mini: four propositions exact) · S17 PASS · S18 PASS · S19 PASS.
