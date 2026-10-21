<!-- SETTLEMENT-FORMAT: mini-settlement-10 -->
# SETTLEMENT AND RETROSPECTIVES — MINI 20261018K9V4R2M7F6

**Document:** `20261018K9V4R2M7F6_SETTLEMENT.md` · settlement-document revision 1 · prepared 2026-10-21 ≈00:45 AEDT.
**Mode / authority / reading receipt / model scope:** identical to `20261018X7Q4M9R2_SETTLEMENT.md` in this folder — `LOCAL_MINI_SETTLEMENT`; `PUBLISHED_MAIN_PINNED 3e29a58693e2ed02ff862e9bf0f751af2feadee1`; Prompt 3 run inside the repository session (ENV-v1 deviation disclosed), no repository writes; receipt = pasted Prompt 3, prompt-3 file lines 1–30, CARD_AND_LOG_TEMPLATES §6/§9, SCORING_AND_VALIDATION §§1–11, PROBABILITY_TOOLKIT §§10–11; RULES_SOCCER and COMMON_OPERATING_PROTOCOL not reopened; no model output read.

## Frozen source and inventory
**FROZEN_SOURCE:** `20261018K9V4R2M7F6_UPDATED_G0001.md` (owner attachment; not on disk); format `mini-log-10`; blocks: §A–§D (intake `INTAKE-20261018-MACHIDA-FUKUOKA-001`) → `CARD LOCAL-20261018K9V4R2M7F6-G0001` → `FOOTER`. Card count 1 (first = last = G0001). Addenda 0; prior revisions 0. Freeze 2026-10-21T00:45+11:00; documentary lease (17:15 18 Oct → 17:15 19 Oct) expired; hand-over `NONE`. Bytes/SHA-256 `PENDING_PROMPT_4`. Source growth: none after `END FOOTER` (next key G0002) — `NO_GROWTH_OBSERVED`.

## LOCAL_ID_MAPPING
| Local key | Native identity | Canonical ID |
|---|---|---|
| `LOCAL-20261018K9V4R2M7F6-G0001` | J1 League 2026-27 Matchweek 10, FC Machida Zelvia v Avispa Fukuoka, 18 Oct 2026 16:00 JST, Machida GION Stadium; J.League path `j1/2026/101812`; ESPN event 401877601 | `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT` |

## Source discovery, corroboration and reuse register
**Information completion: `INFORMATION_INCOMPLETE`** — Machida's corner count conflicts between the two providers (invariant for the 10.5 line); operator definitions unknown; exact final whistle time unknown.

| Source ID | URL / route | Fields observed / missing | Publisher / independence | Retrieval | Reuse limits |
|---|---|---|---|---|---|
| K9-S01 ESPN soccer scoreboard jpn.1 | `https://site.api.espn.com/apis/site/v2/sports/soccer/jpn.1/scoreboard?dates=20261018` | Machida 3–0 Fukuoka, Full Time, KO 07:00Z | ESPN (Opta feed) | 2026-10-21 ≈00:05 AEDT | — |
| K9-S02 ESPN summary 401877601 | `…/soccer/jpn.1/summary?event=401877601` | Half scores 1–0 / 2–0; goals Yengi 22', Mae 73', Mochizuki 76'; `wonCorners` Machida **2**, Fukuoka **5** | ESPN/Opta | ≈00:08 AEDT | Corner provider per RULES_SOCCER §0 default route |
| K9-S03 J.League match page (field owner) | `https://www.jleague.jp/match/j1/2026/101812/live/` | 試合終了 3–0; goals 22', 73', 76'; attendance 10,336; sunny 21.1 °C | J.League (owner) | ≈00:30 AEDT | — |
| K9-S04 J.League stats tab | `https://www.jleague.jp/match/j1/2026/101812/stats/` and match page summary | コーナーキック Machida **1**, Fukuoka **5**; shots 8/6; possession 54/46; playing time 95:10 | J.League (owner; independent of Opta) | ≈00:32 AEDT | Raw HTML parsed; side assignment from table order (home first) |

**SOURCE_SEARCH_ATTEMPTS:** ESPN scoreboard → summary (found); J.League live/stats pages (found; corner count differs from ESPN by 1 for Machida). No other route needed for the grade, which is invariant.

**REQUIREMENT_CLOSURE**
| Field | Status | Sources | Next |
|---|---|---|---|
| FT and HT goals, team goals, result | CLOSED (owner + Opta agree) | K9-S02, S03 | — |
| FT corners vs 10.5 | CLOSED_BY_INVARIANT (6 or 7, both ≤10); Machida count CONFLICT 1 vs 2 | K9-S02, S04 | J.League official match report PDF CK line · prompt-4 · NOT_SCHEDULED |
| Operator definitions | OPEN — UNKNOWN_DEFINITION | — | Owner |
| Final whistle time | OPEN — UNKNOWN (playing time 95:10 known) | K9-S04 | Owner gamebook |

<!-- BEGIN SETTLEMENT LOCAL-20261018K9V4R2M7F6-G0001 revision-1 -->
### Settlement · LOCAL-20261018K9V4R2M7F6-G0001 · FC Machida Zelvia v Avispa Fukuoka · 2026-10-21T00:45+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:45+11:00 · affected contract keys ALL (4 ranked + 4 remaining supplied directions) · changes NONE.
**Card state:** `SETTLED`.
**Final event:** **Machida 3–0 Fukuoka**, half-time 1–0 (Yengi 22'), second-half goals Mae 73', Mochizuki 76'. 90 min + stoppage; no extra time in the league. Corners: Machida 1 (J.League) / 2 (ESPN), Fukuoka 5 → total **6 or 7**. Kick-off 07:00Z (18:00 AEDT). Final wall-clock `UNKNOWN`.
**Definition status:** card's 90-minute regulation convention; corners under the card's proposed J.League CK route (K9-S04, total 6) cross-checked with ESPN `wonCorners` (7). Operator `UNKNOWN_DEFINITION`.
**Evidence grade:** goals A (field owner + Opta); corners E (invariant across conflicting values).
**Expected vs final:** Machida 1.90 → 3 (+1.10); Fukuoka 1.05 → 0 (−1.05); total 2.95 → 3 (+0.05; Poisson SD √2.95 = 1.72 → z +0.03); first half 1.10 → 1 (−0.10); corners 8.40 → 6/7 (−2.4/−1.4; Poisson SD 2.90 → z −0.83/−0.48).

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | **Machida over 0.5 team goals** (90 min) — ANALYST_DERIVED | 0.848 | NOT_AVAILABLE | **WIN** | A | Yes | 3 goals |
| 2 | **Machida or draw (1X / +0.5)** — ANALYST_DERIVED | 0.791 | NOT_AVAILABLE | **WIN** | A | Yes | Machida won |
| 3 | Combined corners **Under 10.5** — SUPPLIED | 0.769 | ≈0.69 (unvalidated diagnostic, not a frozen baseline) | **WIN** | E | No | 6 or 7 |
| 4 | Combined 1st-half goals **Over 0.5** — SUPPLIED | 0.666 | ≈0.657 (diagnostic) | **WIN** | A | No | HT 1–0 |
| — | FT goals Over 2.5 — SUPPLIED, unranked | 0.565 | ≈0.56 (diagnostic) | WIN | A | No | 3 goals |
| — | FT goals Under 2.5 | 0.435 | — | LOSS | A | No | |
| — | 1st-half Under 0.5 | 0.334 | — | LOSS | A | No | |
| — | Corners Over 10.5 | 0.231 | — | LOSS | E | No | |
| — | Winner (3-way, informational): Machida 0.571 / Draw 0.220 / Fukuoka 0.209 | — | — | Machida | A | No | |

**Top-two result:** `ALL_WON` — decisive denominator 2, primary 2/2. Note: Ranks 1–2 are nested team-strength claims (dependent), not mechanically protected; zero joint loss is an outcome, not evidence of protection.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores (binary Brier):** R1 (1−0.848)² = 0.0231; R2 (1−0.791)² = 0.0437; R3 (1−0.769)² = 0.0534 [E]; R4 (1−0.666)² = 0.1116; FT O2.5 0.1892; FT U2.5 0.1892; 1H U0.5 0.1116; corners O10.5 0.0534. Three-way winner half-sum multiclass Brier: 0.5×[(1−0.571)² + 0.220² + 0.209²] = 0.5×(0.1840+0.0484+0.0437) = **0.1381** (labelled half-sum scaling). Paired frozen baselines: 0 → d_Brier `NOT_COMPUTABLE`.
**Shadow results:** none.
**Form-window check:** unadjusted centres Machida 1.918 / Fukuoka 1.195 vs adjusted 1.90 / 1.05; observed 3 / 0. The −0.05 Fukuoka adjustment moved toward the outcome; the −0.22 Machida rest/travel adjustment moved away from it. Net effect small relative to the result.
**Winner call:** Machida → **correct**.

**R1. Original prediction:** Rank 1 Machida team goals Over 0.5 at 0.848; Rank 2 Machida-or-draw at 0.791.
**R2. Final event:** 3–0, HT 1–0, verified by owner and Opta.
**R3. Contract settlement:** team goals 3 ≥ 1; 1X satisfied by the win; corners ≤10 under both providers; 1H goals 1 ≥ 1; FT goals 3 ≥ 3.
**R4. Rank diagnostics:** primary 2/2; Hit@2 hit; NDCG@2 for the four ranked rows (all four won) → DCG 1.631 / IDCG 1.631 = 1.0.
**R5. Winner call:** correct.
**R6. Line assessment:** team goals +2.5 over the 0.5 line; 1X margin +3 vs threshold 0; corners 3.5–4.5 under 10.5; 1H +0.5; FT +0.5 over 2.5.
**R7. Expected versus realised:** goals near the 2.95 centre (z +0.03); Fukuoka scoreless vs 1.05 expected; corners below centre.
**R8. Missed mechanism:** none material for the ranked rows. Process check on the win (S8): the card issued without a confirmed XI (`LINEUP_UNCONFIRMED`) — the same defect that appears in losses elsewhere; the wins do not validate that gap.
**R9. Source/timing review:** kick-off 18:00 AEDT; the card records research at 17:40–17:47 AEDT and no verified issue time — issue phase `UNVERIFIED` (possibly pre-start, not proven). No freeze receipt.
**R10. Classification:** process `NOT_ASSESSABLE` for pre-start certification; lineup closure `DEFICIENT` per card's own C20; outcomes consistent with the issued distribution.
**R11. Hypothesis:** `PROPOSED_NOT_TESTED` — none specific from one aligned result.
**R12. Disposition:** `NO_CHANGE`; record the J.League vs Opta corner-count conflict as a data-integrity note.
<!-- END SETTLEMENT LOCAL-20261018K9V4R2M7F6-G0001 revision-1 -->

## Shadows and legacy bundles for prompt 6
None.

## UNRESOLVED_CARRYOVER
| ID | Event key | Queue | Original card | Latest revision | Open field | Responsible actor | Next source + exact field | Due | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| K9-Q1 | `LOCAL-20261018K9V4R2M7F6-G0001` | UNRESOLVED_EVIDENCE (data integrity, non-grading) | G0001 | revision-1 | Machida CK 1 (J.League) vs 2 (ESPN) | Prompt-4 agent | J.League official match report: CK per side | NEXT_OWNER_INVOKED | UNKNOWN final time | 2026-10-21 ≈00:32 AEDT | NOT_SCHEDULED |
| K9-Q2 | G0001 | UNRESOLVED_EVIDENCE | G0001 | revision-1 | Operator terms | Owner | Written rules | NEXT_OWNER_INVOKED | N/A | not supplied | NOT_SCHEDULED |

## Learning record (LEARN-v2)
| Local key | Final score | Regulation | Decision | Final time | Terminal source |
|---|---|---|---|---|---|
| G0001 | Machida 3–0 Fukuoka (HT 1–0); corners 6 (J.League) / 7 (ESPN) | same | Machida win | UNKNOWN (KO 07:00Z; playing time 95:10) | J.League `j1/2026/101812` · ESPN 401877601 · retrieved 2026-10-21 ≈00:05–00:32 AEDT |

## SETTLEMENT_MANIFEST
| Item | Value |
|---|---|
| Frozen source | `20261018K9V4R2M7F6_UPDATED_G0001.md`; 1 card; bytes/SHA PENDING_PROMPT_4 |
| Rows | 8 supplied/derived directions: **5 W / 3 L / 0 PUSH / 0 VOID / 0 UNRESOLVED** (+ informational 3-way winner) |
| Primary | 2 W / 0 L; class ALL_WON; Hit@2 1/1 |
| Mean Brier primary | (0.0231+0.0437)/2 = **0.0334** |
| Evidence mix (primary) | A 2 |
| Timing | issue phase UNVERIFIED |
| Rank-1 LOSS deep reviews | 0 required |
| Canonical import / GitHub writes | PENDING / NO |

**MINI_SETTLEMENT review row:** `2026-10-21 | MINI 20261018K9V4R2M7F6 | 1 card | primary 2W-0L, mean Brier 0.033 | INSUFFICIENT_EVIDENCE (n=1) | data: corner-provider conflict noted | no rank changes`.

## Verification S1–S18
S1 PASS · S2 PENDING_PROMPT_4 · S3 PASS · S4 PASS · S5 PASS (corner conflict disclosed) · S6 PASS (5 W + 3 L = 8) · S7 PASS · S8 PASS (no R1 loss; wins checked for the lineup defect) · S9 PASS (no shadows; 0 frozen baselines) · S10 PASS · S11 PASS · S12 PARTIAL (local untracked write only) · S13 PASS · S14 PARTIAL (SHA pending) · S15 PASS · S16 PASS · S17 PARTIAL (Markdown tables; CSVs at prompt 4) · S18 PASS.
