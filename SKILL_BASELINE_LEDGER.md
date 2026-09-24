# Skill-versus-baseline ledger (`C-BASELINE-SKILL`)

**Opened 2026-09-25(c).** **Status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** This is a descriptive diagnostic, not a performance, calibration or value claim (`PERFORMANCE_ELIGIBILITY_POLICY.md`).

## Why this exists

A Brier score only means something against a baseline. Until now the framework compared its cards with a **coin flip** (0.25). A coin flip is the weakest possible opponent. It ignores things everyone knows before the game: the home side wins about 53% of MLB games, and an MLB total of 7.5 goes Over about 57% of the time.

This ledger compares each card with a **naive population baseline** for the *same* contract. The baseline knows:
- the league's own outcome distribution, using only games completed **before** the event (leak-free);
- which side is at home.

It knows nothing about the teams, players, lineups or conditions. A research process worth its cost should beat it. Until it does, the honest statement is: **no demonstrated skill over what a population table would say.**

## Rules

1. **One row per issued decision.** A forced pair's exact complement is counted once, as the higher-ranked row. A covering pair's two rows are separate decisions: both can win. A winner call is its own decision, unless it duplicates a ranked moneyline row.
2. **Card p** is copied from the issued Field 4 table or winner call (`C-SUMMARY-FROM-CARD`), never retyped.
3. **Baseline p** comes from the competition's population in `BASE_RATES_REGISTER.md` §7 (or its re-runnable query), restricted to games completed before the event's start:
   - **Totals:** the population P(Over/Under the line).
   - **Moneylines:** P(home win) or P(away win).
   - **Handicaps:** P(home or away margin + line > 0).
   - **Tennis:** without side information, 0.5 × P(winner margin ≥ k+1) for −k.5, its complement for +k.5, and 0.5 for a winner.
4. **From `CONTROL_MANIFEST_2026-09-25-3.md` onward,** every card prints `BASELINE_P` beside each ranked row **at issue** (prospective, frozen before the result). The row is appended here at settlement. The seed rows below were computed after the fact from pre-event data only: leak-free, but hindsight-selected.
5. **Competitions with no population reference** (LKL, EuroLeague Women, El Salvador LMB, KBO, NPB, ITF, cricket) record `BASELINE_P: NOT_YET_DERIVED`. They are not scored here until a population query exists.
6. **Report with** `python tools/skill_baseline.py`: paired Brier (card − baseline; negative means the card is better), by family, with a bootstrap interval that resamples whole cards.
7. **Decision rule** (preregistered; `LEARNING_REGISTER.md` §"2026-09-25(c)"). After **100 prospective decisions from at least 30 cards**:
   - **Card − baseline < 0 with the 95% interval below 0:** the framework may state "beats a naive population baseline". This is still not a performance claim.
   - **The interval spans 0:** "no demonstrated skill over the baseline".
   - **The interval is above 0:** the card process is adding noise. Open a method review.

   The seed rows do not count toward the 100.

## Seed rows — 2026-09-24 cohort (hindsight-selected, pre-event data only)

Nine cards had a population reference: P-495, P-500, P-501, P-502, P-503, P-504, P-506, P-508 and P-509. The covering pairs in P-502 and P-506 contribute both rows, since both can win.

**Excluded, with no population reference:** P-496 (ITF), P-497 and P-498 (LKL), P-499 (EuroLeague Women), P-505 (LMB), P-507 (KBO), TMP-G25 and P-493 (NPB, KBO). P-494 is excluded as live-issued.

**Builder:** `research/base_rates_2026-09-25/build_skill_baseline_seed.py`.

| Decision | Card | Rank | Contract (as issued) | Family | Card p | Baseline p | Baseline population (leak-free) | Result |
|---|---|---|---|---|---:|---:|---|---|
| P-500-RL-WSH | P-500 | 1 | Nationals +1.5 | handicap | 0.587 | 0.638 | MLB 2026 before first pitch, n=2357 | W |
| P-500-ML | P-500 | 2 | Tigers ML | moneyline | 0.562 | 0.529 | MLB 2026 before first pitch, n=2357 | L |
| P-500-TOT | P-500 | 3 | Combined Total: Over 7.5 Runs | total | 0.536 | 0.573 | MLB 2026 before first pitch, n=2357 | L |
| P-501-TOT | P-501 | 1 | Combined Total: Over 7.5 Runs | total | 0.662 | 0.573 | MLB 2026 before first pitch, n=2358 | L |
| P-501-ML | P-501 | 2 | Orioles ML | moneyline | 0.576 | 0.529 | MLB 2026 before first pitch, n=2358 | W |
| P-501-RL-TOR | P-501 | 3 | Blue Jays +1.5 | handicap | 0.554 | 0.638 | MLB 2026 before first pitch, n=2358 | L |
| P-502-RL-CWS | P-502 | 1 | White Sox +1.5 | handicap | 0.700 | 0.638 | MLB 2026 before first pitch, n=2366 | W |
| P-502-RL-KC | P-502 | 2 | Royals +1.5 | handicap | 0.558 | 0.638 | MLB 2026 before first pitch, n=2366 | W |
| P-502-TOT | P-502 | 3 | Combined Total: Over 8.5 Runs | total | 0.553 | 0.490 | MLB 2026 before first pitch, n=2366 | W |
| P-502-WIN | P-502 | winner | Winner call: White Sox | moneyline | 0.576 | 0.471 | MLB 2026 before first pitch, n=2366 | L |
| P-506-RL-HOU | P-506 | 1 | Astros +1.5 | handicap | 0.685 | 0.638 | MLB 2026 before first pitch, n=2371 | W |
| P-506-RL-SEA | P-506 | 2 | Mariners +1.5 | handicap | 0.659 | 0.638 | MLB 2026 before first pitch, n=2371 | W |
| P-506-TOT | P-506 | 3 | Combined Total: Under 7.5 Runs | total | 0.506 | 0.428 | MLB 2026 before first pitch, n=2371 | L |
| P-506-WIN | P-506 | winner | Winner call: Astros | moneyline | 0.511 | 0.471 | MLB 2026 before first pitch, n=2371 | L |
| P-503-ML | P-503 | 1 | Stars ML | moneyline | 0.708 | 0.566 | NHL preseason 2025 + 2026 before 23 Sep, n=136 | W |
| P-503-TOT | P-503 | 2 | Combined Total: Under 5.5 Goals | total | 0.605 | 0.566 | NHL preseason 2025 + 2026 before 23 Sep, n=136 | W |
| P-503-RL-MIN | P-503 | 3 | Wild +1.5 | handicap | 0.540 | 0.699 | NHL preseason 2025 + 2026 before 23 Sep, n=136 | L |
| P-504-SPR | P-504 | 1 | Dream -4.5 | handicap | 0.591 | 0.353 | WNBA 2026 before tip, n=331 | W |
| P-504-TOT | P-504 | 2 | Combined Total: Under 173.5 Points | total | 0.553 | 0.514 | WNBA 2026 before tip, n=331 | W |
| P-504-WIN | P-504 | winner | Winner call: Dream | moneyline | 0.692 | 0.459 | WNBA 2026 before tip, n=331 | W |
| P-508-TOT | P-508 | 1 | Combined Total: Under 194.5 Points | total | 0.691 | 0.728 | NBL 2025-26 + 2026-27 before tip, n=184 | W |
| P-508-SPR | P-508 | 2 | Phoenix +2.5 | handicap | 0.515 | 0.603 | NBL 2025-26 + 2026-27 before tip, n=184 | L |
| P-508-WIN | P-508 | winner | Winner call: Melbourne United | moneyline | 0.549 | 0.467 | NBL 2025-26 + 2026-27 before tip, n=184 | W |
| P-509-TOT | P-509 | 1 | Combined Total: Under 184.5 Points | total | 0.613 | 0.530 | NBL 2025-26 + 2026-27 before tip, n=185 | L |
| P-509-SPR | P-509 | 2 | 36ers -1.5 | handicap | 0.516 | 0.422 | NBL 2025-26 + 2026-27 before tip, n=185 | L |
| P-509-WIN | P-509 | winner | Winner call: Adelaide 36ers | moneyline | 0.543 | 0.470 | NBL 2025-26 + 2026-27 before tip, n=185 | L |
| P-495-HCP | P-495 | 1 | Gormaz -5.5 Games Handicap | handicap | 0.591 | 0.248 | WTA 2026 women best-of-3 before match, 0.5 x P(margin>=6)=0.495, n=5126 | L |
| P-495-TOT | P-495 | 2 | Under 19.5 Total Games | total | 0.576 | 0.459 | WTA 2026 women best-of-3 before match, n=5126 | L |
| P-495-WIN | P-495 | winner | Winner call: Romero Gormaz | moneyline | 0.843 | 0.500 | no side information: 0.5 | L |

### Seed result (hindsight; not counted toward the decision rule)

`python tools/skill_baseline.py` on the rows above:

| Scope | n | Card Brier | Baseline Brier | Card − baseline | Rows card better |
|---|---:|---:|---:|---:|---:|
| **All** | 29 | 0.2461 | 0.2360 | **+0.0101** | 15/29 |
| handicap | 11 | 0.2107 | 0.2339 | −0.0232 | 7/11 |
| moneyline | 9 | 0.2753 | 0.2424 | +0.0329 | 4/9 |
| total | 9 | 0.2600 | 0.2322 | +0.0278 | 4/9 |

Card-cluster bootstrap 95% interval for (card − baseline): **[−0.0592, +0.0894]**. There is **no demonstrated difference** from a naive population baseline.

**Reading.**
- On these 29 decisions the cards did slightly *worse* than a table that knows only the league's outcome rates and who is at home. The difference is well inside noise (9 cards).
- **Totals** trailed the baseline (0.2600 v 0.2322). The cards' strongest total leans (P-501 Over 0.662, P-509 Under 0.613, P-495 Under 0.576) lost.
- **Handicaps** were the one family ahead (0.2107 v 0.2339). The biggest gain was P-504's Dream −4.5 (0.591 against a 0.353 baseline), where team-specific research added real information.
- **Moneyline and winner calls** trailed (0.2753 v 0.2424), driven by the confident P-495 winner call (0.843, lost).
- This agrees with the width finding (`BASE_RATES_REGISTER.md` §7.6). Centres are unbiased, but probabilities are stated more confidently than the evidence supports. The fix is the width and reference disclosures already in force (`C-WIDTH-BENCHMARK`, field BR), not a fitted shrink (`L-087`).
- It is also the first quantitative check of the question the 2026-09-25 repository review asked: does the research process add skill? **Not yet shown.**

**One structural fact surfaced by the builder** (MLB 2026, n = 2,373): home teams win by exactly one run **16.7%** of the time and lose by exactly one run **10.9%** (walk-offs). The home and away +1.5 baselines are therefore nearly equal (0.638 / 0.638), even though the home side wins 52.9%. The fact is recorded in `BASE_RATES_REGISTER.md` §7.5.

## Prospective rows (from `CONTROL_MANIFEST_2026-09-25-3.md`)

Append rows here at settlement, with `BASELINE_P` exactly as printed on the card at issue. None yet.

| Decision | Card | Rank | Contract (as issued) | Family | Card p | Baseline p | Baseline population (leak-free) | Result |
|---|---|---|---|---|---:|---:|---|---|
