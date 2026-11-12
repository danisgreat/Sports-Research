<!-- SETTLEMENT-FORMAT: mini-settlement-10 -->
# SETTLEMENT REVISION DOCUMENT — MINI 20261018X7Q4M9R2 — revision-2 package

**Document:** `research/active_minis/20261018X7Q4M9R2_SETTLEMENT_REVISION_2.md` · written 2026-11-07T20:53:07+11:00 (clock read). The revision-1 document is **not** overwritten.
**Mode / authority:** `LOCAL_MINI_SETTLEMENT` (prompt 3, P-2026.10.22-v24.0), owner-invoked 2026-11-07. `LOCAL_WORKING_TREE`, branch `main`, HEAD `749bca06d2b63f358fce19a1969d6887ecfb8815` (= `origin/main`). Reading receipt as in `2026101679B3FBCC8D_SETTLEMENT_REVISION_3.md` (same folder), plus RULES_CRICKET and the revision-1 settlement of this mini.

## Frozen source, prior package and scope
- **FROZEN_SOURCE (unchanged, already canonical):** `research/verification/mini_import_P-601_P-622_2026-10-21-1/inputs/20261018X7Q4M9R2/ORIGINAL_MINI.md` — 150,699 bytes, SHA-256 `8bca9a3ee2876da831e7ac5a26753e42acbce16c5d1cfd37493a9d7e86452748`, 3 card markers G0001–G0003, first key `LOCAL-20261018X7Q4M9R2-G0001`, last `…-G0003`. Re-hashed before any text was written; equals the import receipt.
- **Prior settlement:** revision-1 document `…/inputs/20261018X7Q4M9R2/20261018X7Q4M9R2_SETTLEMENT.md` (32,081 bytes, `4a9907c056963a14f6805b6539353e2e8f7da6c32b10c266ac3840087f26ad28`), imported in Part 8.
- **This document appends** `revision-2` for G0001 (P-620) only: the qualitative Test-winner call `PENDING_EVENT → settled`, the first-innings learning record completed, and the innings-contract evidence lifted from E (invariant bound) to B (final total). **No contract grade changes.** G0002 (P-621) and G0003 (P-622) are untouched; a new corroboration attempt for P-621 is logged in the carryover only.

## LOCAL_ID_MAPPING
Existing canonical reference retained (MINI-v2): `LOCAL-20261018X7Q4M9R2-G0001` → **P-620** (2026-10-21 import). No new event; no P-number planned.

## Source discovery, corroboration and reuse register
**Information completion: `INFORMATION_INCOMPLETE`** — no field-owner scorecard read for P-620 (two independent match reports with an arithmetic check); exact final time; operator terms.

| Source ID | URL / route | Fields observed / missing | Publisher / independence | Retrieval | Reuse limits |
|---|---|---|---|---|---|
| X7R2-S01 ARY News match report | `https://arynews.tv/south-africa-complete-innings-victory-over-australia-in-2nd-test` | **South Africa 425/9 declared**; Australia **99** and **295** all out; South Africa won by **an innings and 31 runs**; dated Thursday 22 October 2026 | Independent media | 2026-11-07 (web fetch) | Result fields only |
| X7R2-S02 Times of Oman (ANI) report, search-visible | `https://timesofoman.com/article/178285-bavuma-jansen-stars-as-south-africa-crush-australia-by-an-innings-and-31-runs-to-level-test-series-1-1` | Innings and 31 runs; SA recovered from 110/6 to 425/9 dec; Bavuma 179; Jansen 5-33 and an 80; Harmer 80; follow-on enforced; Head 121 in Australia's 295; series level 1–1; St George's Park, Gqeberha | Independent wire (ANI) | 2026-11-07 (search) | Result fields only |
| X7R2-S03 other reports, search-visible | Qatar Tribune ("innings and 31 runs"); Outlook India (Australia 99 all out); JagoNews24 headline "34" | Agree on innings win; JagoNews24's "34" is a lone headline value, contradicted by the arithmetic below | Independent media | 2026-11-07 (search) | JagoNews24 value rejected |
| X7R2-S04 cricket.com.au series page | `https://www.cricket.com.au/matches/series/CA:4568/south-africa-v-australia-test-series-2026` | Match list not rendered ("No matches available") | Board media | 2026-11-07 | Nothing used |

**Arithmetic check:** 425 − 99 − 295 = **31** → an innings and 31 runs. Consistent with the revision-1 bound (SA ≥ 324/7 after 102.4 overs).

**REQUIREMENT_CLOSURE**
| Field | Status | Next · actor · due · automation |
|---|---|---|
| P-620 Test result | CLOSED (two independent reports + arithmetic) | — |
| P-620 SA first-innings final total | CLOSED (425/9 dec, same evidence) | ESPNcricinfo 1525660 scorecard for a field-owner upgrade · settlement reviewer · NOT_SCHEDULED |
| P-620 exact final time | OPEN (`UNKNOWN`; ended 22 Oct per reports) | scorecard close of play · settlement reviewer · NOT_SCHEDULED |
| Operator terms | OPEN | owner |

<!-- BEGIN SETTLEMENT LOCAL-20261018X7Q4M9R2-G0001 revision-2 -->
### Settlement · LOCAL-20261018X7Q4M9R2-G0001 (P-620) · South Africa v Australia, 2nd Test — result and learning record · 2026-11-07T20:53:07+11:00
**Revision:** revision-2 · parent revision-1 · effective 2026-11-07T20:53:07+11:00 · affected keys: `SA-I1-U2825`, `SA-I1-O2825` (evidence field only) and the qualitative winner call · changes: winner call `PENDING_EVENT → settled`; innings evidence E → B; **no contract grade changes** (reason: the Test ended 22 October 2026 and the final first-innings total is now published).
**Card state:** `SETTLED` (all four contract rows decisive, unchanged); winner call settled.
**Final event:** **South Africa won by an innings and 31 runs** at St George's Park, Gqeberha, on 22 October 2026. South Africa 1st innings **425/9 declared**; Australia **99** and (following on) **295**. Arithmetic 425 − 99 − 295 = 31. Final wall-clock time `UNKNOWN`.
**Definition:** first Test innings until all out or declaration, as the card's A2 froze; a declaration ends the innings. Operator `UNKNOWN_DEFINITION`. **Evidence:** innings rows B (two independent reports with an arithmetic check; no field-owner scorecard read); 5-over rows B (unchanged).

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins |
|---|---|---:|---|---|---|---|
| 1 | South Africa 1st innings **Under 282.5** runs | 0.537 | `NO_LEAGUE_PROFILE` | **LOSS** (unchanged) | B (was E) | Yes (primary) |
| 2 | South Africa after first **5.0 overs Under 13.5** runs | 0.524 | `PROFILE_LACKS_ENDPOINT` | **WIN** (unchanged) | B | Yes (primary) |
| 3 | South Africa after 5.0 overs **Over 13.5** | 0.476 | `PROFILE_LACKS_ENDPOINT` | **LOSS** (unchanged) | B | No (informational) |
| 4 | South Africa 1st innings **Over 282.5** | 0.463 | `NO_LEAGUE_PROFILE` | **WIN** (unchanged) | B (was E) | No (informational) |

**Top-two result:** `SPLIT` (unchanged) — R1 LOSS, R2 WIN; primary 1/2.
**Proper scores:** unchanged from revision-1 (R1 0.2884, R2 0.2266, R3 0.2266, R4 0.2884); the R1 and R4 rows now enter the headline evidence view (B) instead of the sensitivity view (E). Paired BASELINE_P 0/4 → `NOT_COMPUTABLE`.
**Expected vs final:** innings centre 272.0 (σ ≈ 115 base) → **425**: error **+153.0**, z ≈ **+1.33** (revision-1 had the lower bound ≥ +52, z ≥ +0.45). 425 − 282.5 = +142.5 runs past the line.
**Winner call:** card's qualitative call **Australia** (no probability issued) → **INCORRECT** (South Africa won). Qualitative only; it enters no proper score and no primary win count.
**R2 (update):** final 425/9 dec v 99 and 295; innings and 31 runs. **R5 (update):** winner call incorrect. **R7 (update):** +153 above the centre, +1.33σ; the lower order carried South Africa from 110/6 (Bavuma 179; Jansen and Harmer in the 80s). **R8 (update):** the revision-1 reading stands and is stronger: the card's scenario mixture did not condition the total on surviving an early collapse; a recovery to 425 lay in its upper tail. Australia's 99 shows the same damp seam conditions cut both ways; not attributed to a pre-start input. **R10:** failure class for R1 stays `NEAR_COINFLIP_RANKED / VARIANCE`, with `TAIL_UNDERWEIGHTED / LOWER-ORDER RECOVERY` noted. **R12:** `MONITOR`; learning record complete. Other R sections and the eight-part review are unchanged, except part 2 now reads: SA **425/9 declared**, so the claim failed by 143 runs.
<!-- END SETTLEMENT LOCAL-20261018X7Q4M9R2-G0001 revision-2 -->

## UNRESOLVED_CARRYOVER (supersedes U-604; other rows unchanged)
| ID | Event key | Queue | Original card | Latest revision | Open field | Responsible actor | Next source + exact field | Due | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X7R2-Q1 | G0001 (P-620) | UNRESOLVED_EVIDENCE (upgrade only, non-grading) | G0001 | revision-2 | Field-owner scorecard; exact final time | Settlement reviewer | ESPNcricinfo 1525660 scorecard, close of play | Next owner-invoked review | UNKNOWN (ended 22 Oct per reports) | 2026-11-07 (X7R2-S04 not rendered) | NOT_SCHEDULED |
| X7R2-Q2 | G0002 (P-621) | UNRESOLVED_EVIDENCE (corroboration, non-grading) | G0002 | revision-1 | Field-owner box (LBA) | Settlement reviewer | legabasket.it game page | Next owner-invoked review | UNKNOWN | 2026-11-07: Eurohoops (Milano 98–82 at Napoli) and Sofascore (Napoli 25-13-23-21 = 82; Milano 18-24-25-31 = 98, from cumulative 25–18, 38–42, 61–67, 82–98) agree with revision-1; legabasket.it not surfaced | NOT_SCHEDULED |
| — | Operator terms, final times, other revision-1 items | unchanged | — | revision-1 | as recorded | as recorded | as recorded | as recorded | as recorded | no new attempt | NOT_SCHEDULED |

## Learning record additions (LEARN-v2)
| Local key | Final score | Regulation | Decision | Final time | Terminal source |
|---|---|---|---|---|---|
| G0001 (P-620) | South Africa 425/9 dec; Australia 99 & 295 | — (Test) | South Africa by an innings and 31 runs | UNKNOWN (22 Oct 2026) | X7R2-S01 ARY News; X7R2-S02 Times of Oman/ANI, retrieved 2026-11-07 |

## SETTLEMENT_MANIFEST (effective state after revision-2)
| Item | revision-1 | after revision-2 |
|---|---|---|
| Cards / terminal events | 3 / 3 (P-620 winner call pending) | 3 / 3, **no pending call** |
| Rows W / L / PUSH / UNRESOLVED | 6 / 6 / 0 / 0 | 6 / 6 / 0 / 0 (unchanged) |
| Primary (ranks 1–2) | 2 W / 4 L | 2 W / 4 L (unchanged) |
| Evidence E rows | 2 (P-620 innings) | **0** (now B) |
| Revision chain | revision-1 all keys | **revision-2** for G0001; revision-1 for G0002, G0003 |

**MINI_SETTLEMENT review row:** `2026-11-07 | MINI 20261018X7Q4M9R2 revision-2 | 3 events | 6W-6L, primary 2W-4L (unchanged) | P-620 winner call settled (incorrect), innings E→B | NO_CHANGE | no rank changes`.

## Verification (S1–S19, revision-2 scope)
S1 PASS · S2 PASS (frozen source re-hashed = import receipt) · S3 PASS (p_card and BASELINE_P copied literally) · S4 PASS · S5 PASS (E → B upgrade made by this new revision, never silently; SCV §2a) · S6 PASS (6 + 6 = 12) · S7 PASS · S8 PASS (Rank-1 loss review updated, part 2) · S9 PASS (no rank change) · S10 PASS (nothing backfilled into the card) · S11 PASS (proper scores unchanged) · S12 PASS · S13 PASS (revision-2 names parent revision-1) · S14 PASS · S15 PASS (no price, line or odds source) · S16 PASS (manual check against the frozen mini) · S17 PASS · S18 PASS (existing mapping; prompt 4 appends the revision) · S19 PASS.
