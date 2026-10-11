<!-- BEGIN RESEARCH ADDENDUM P-578 A8-20261011-210851 -->
### A8. Pre-tip roster verification and conditional repricing — P-578 (11 October 2026)

**Record identity:** NBA preseason Dallas Mavericks @ Houston Rockets, official game `0012600016`, at Venetian Arena, Macao. **Type:** `IMMUTABLE_RESEARCH_ADDENDUM`, not a new game, settlement, retrospective, or overwrite of the original P-578 card. **Research cutoff:** `2026-10-11T21:08:51+11:00` (AEDT) = `2026-10-11T18:08:51+08:00` (Macao), after the published scheduled first-tip 18:00 local. **Actual first jump:** `NOT_INDEPENDENTLY_VERIFIED`; user reports delayed start, but no owner-sourced delay/tip timestamp retrieved. Consequently: `LATE_START_UNVERIFIED` retained; NOT performance-certified. No second-game score, player points, game clock, play-by-play or observed in-game information is an input.

#### A8.1 Starter and game-state handshake

**Dallas five — confirmed in the live-dated RotoWire starting-five listing (label exactly “Confirmed Lineup”):**
1. Kyrie Irving — PG
2. Zaccharie Risacher — SG
3. Cooper Flagg — SF
4. P.J. Washington — PF
5. Daniel Gafford — C

**Houston five — still ONLY “Expected Lineup” on the same page:** Fred VanVleet (PG), Amen Thompson (SG), Tari Eason (SF), Jabari Smith Jr. (PF), Alperen Sengun (C). **Houston confirmation is NOT verified.** Kevin Durant marked `Ques`/may not play there; a prior dated secondary injury report said out for rest, but this discrepancy is not resolved to an official active/inactive field. Do not reclassify Durant as officially OUT or claim that Houston's five is confirmed. Dallas Dereck Lively II, Santi Aldama, Morez Johnson and Marcus Sasser remain flagged questionable on the accessible secondary lineups page, not declared ruled out.

**Timestamp/source ledger:**
- Official NBA fixture and published 06:00 EDT (21:00 AEDT) scheduled time: https://www.nba.com/game/DAL-vs-HOU-0012600016 ; rechecked 2026-10-11 21:08 AEDT. Official game page did not expose a verifiable first-jump or posted two-team lineup at this cutoff.
- RotoWire daily lineups https://aws-prod-web9.rotowire.com/basketball/nba-lineups.php ; accessed 2026-10-11 21:08 AEDT. Direct excerpt `Confirmed Lineup` / `Kyrie Irving` / `Z. Risacher` / `Cooper Flagg` / `P. Washington` / `D. Gafford`; opposing listing excerpt `Expected Lineup` / `Fred VanVleet` / `Amen Thompson` / `Tari Eason` / `Jabari Smith` / `A. Sengun`; `K. Durant Ques`. Source: reputable independent feed, not firsthand NBA game book. Page's market/odds sections were not used for research input.
- Official 2026 China Games schedule, league's 18:00 Macao tip: https://www.nba.com/news/2026-nba-china-games-everything-to-know . Arena 17:30 event opening is not proof of on-court tip.
- User reports tip delayed; supported as user-supplied qualitative observation only, precise delay and actual pregame status not independently certified. Thus this analysis cannot be backdated as definitely pre-tip.

#### A8.2 New distribution — sensitivity update, not refitted prospective calibration

**Frozen original P-578:** `basketball_nba_pre_pace_eff_joint_ot_v1`, 1,800,000 endpoint draws, seed 20261011578; DAL 113.29, HOU 115.08, total 228.37, Houston–Dallas margin +1.78; Houston outright 53.7%. The original already assumed limited Irving participation (+0.7 Dallas points) and Durant resting (−2.9 HOU) via analyst weights. Thus the roster news is *not* a fresh full-strength Irving upgrade and must not double-count his historical 24+ PPG.

**A8 delta assumptions** (analyst judgment, no prospective validation): DAL **+1.5 points total** vs original, comprising +1.0 more minutes/creation certainty for Irving *on top of his original +0.7* and +0.5 for Washington's confirmed start vs ambiguous availability. Neutral-site advantage stays zero; no change to pace (101.195), opponent rates, 23.2 regulation total SD, 18.8 regulation margin SD, or OT parameters. Houston remains on the **conditional Durant-resting branch** because his status is unresolved and the original scenario used that branch. Do not attach a false official injury status to this calculation.

**Repricing procedure:** load original frozen full-game joint-score draws in `P-578_DISTRIBUTION_GRID.npz`; add +1 Dallas point to every draw and a second point to half the draws with seeded RNG `202610112108`. If a new tie arises solely through this additive shift, model the final NBA overtime continuation by assigning one additional point to Dallas or Houston at 50/50, yielding nonzero final margins. All props are counted from this **same modified terminal game grid**; N=1,800,000. This is a reproducible *post-issue reweighting* rather than a newly independently fitted pace model. Companion file `P-578_A8_CONFIRMED_DALLAS_SCENARIO_GRID.npz`. No second-game play or result fed into it.

| Quantity | Original P-578 | A8 conditional repricing |
|---|---:|---:|
| Dallas expected points | 113.29 | **114.80** (SD 14.96) |
| Houston expected points | 115.08 | **115.09** (SD 15.43) |
| Combined expected points | 228.37 | **229.89** (SD 23.86) |
| Margin Houston − Dallas | +1.78 | **+0.29** (SD 18.82) |
| P(Houston wins) | 53.7% | **51.7%** |
| P(Dallas wins) | 46.3% | **48.3%** |
| P(Dallas +1.5) | 48.0% | **52.0%** |
| P(Houston −1.5) | 52.0% | **48.0%** |
| P(Over 230.5) | 46.1% | **48.7%** |
| P(Under 230.5) | 53.9% | **51.3%** |

**Top-four A8 derived research thresholds** (re-ranked within the candidate set, not edits to frozen Rank 1–4; exact line availability NOT_VERIFIED):

| Rank | Role | Conditional proposition — full game incl. OT | p_A8 | Principal failure route |
|---|---|---|---:|---|
| 1 | PICK | Combined total **Over 199.5** | **89.98%** | Reduced offensive minutes, slow pace or cold shooting causes 199 or fewer |
| 2 | PICK | Combined total **Under 259.5** | **89.32%** | Both teams score at extreme pace / unusually good efficiency, or overtime(s) |
| 3 | INFORMATIONAL | Dallas Mavericks **+23.5** | **89.15%** | Houston wins by 24+ |
| 4 | INFORMATIONAL | Houston Rockets **+22.5** | **88.80%** | Dallas wins by 23+ |

*Why rank 2:* choose the Under 259.5 to minimise P(both Rank-1 and Rank-2 lose)=**0.0% by construction** (a completed total cannot be ≤199 and ≥260). A Houston +23.5 alternative is 89.77% but shares a nonzero joint-failure channel with Over 199.5; the zero-joint-loss choice is prioritised under selection §3. The 89.98% Rank-1 is **below** the unrounded 90% ceiling (display to two decimal places to avoid a 90.0-rounding ambiguity). **RANK1_UNSTABLE**: Rank-1 vs best non-complementary candidate, Houston +23.5 at 89.77%, a +0.21 percentage-point lead, below required +4.0. The derived pairs are largely tautological wide thresholds, not demonstrated real-world bet edges.

**Threshold consistency checks:** P(DAL +1.5) 51.9782% + P(HOU −1.5) 48.0218% = 100%; P(Over 230.5) 48.6928% + P(Under 230.5) 51.3072% = 100%. The 23.86 total SD reflects original NBA preseason scenario width, not fitted 2026 preseason variance. Ranks rely on unverified Houston starters and minute exposure. 

**Sensitivity to uncertainty:** if Irving is restricted to a very short shift, remove the A8 +1.0 Irving increment; Washington's +0.5 may remain. If he plays a longer meaningful workload, a larger Dallas increment (e.g. another +1.0) is a scenario, not a confirmed point estimate. If Durant unexpectedly plays, remove/revise the frozen Houston −2.9 rest assumption and rerun the entire grid; a confirmed starter switch would require a fresh addendum before treating any ranks as operative. **A8 status:** `UNCALIBRATED_ANALYST_SCENARIO`, `LATE_START_UNVERIFIED`, `HOUSTON_LINEUP_NOT_CONFIRMED`, `IRVING_MINUTES_UNVERIFIED`, `CANONICAL_IMPORT_PENDING`, `NO_SETTLEMENT`.

**Custody:** Original P-578 card remains byte-for-byte unchanged, original p_card/ranks remain the issued historical record. This A8 is a timestamped diagnostic/conditional secondary scenario only, no canonical commit and no new P-ID; the next available working ID remains P-579.
<!-- END RESEARCH ADDENDUM P-578 A8-20261011-210851 -->
