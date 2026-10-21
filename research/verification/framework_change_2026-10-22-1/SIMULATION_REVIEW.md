# Is simulation needed or helpful? Review across sports, 22 October 2026

**Status: REVIEW evidence for framework change 2026-10-22-1.** Owner question: check whether simulation is needed or helpful for the sports other than basketball (basketball is in the [21 October review](../review_2026-10-21_league_neutral_ml_sim/REPORT.md) §5).

**Evidence class:** `HISTORICAL_DEVELOPMENT`. The data are the stored development predictions in `research/model_shadow/*-r1/DEVELOPMENT_PREDICTIONS.csv` (test seasons 2023 onward, FROZEN rows). Their source admission is unverified (`FIELD_OWNER_ADMISSION_UNVERIFIED`). Good enough to judge whether a distribution *shape* fits; not evidence of skill.

**Method.** For each sport, the model's mean and SD are compared with the actual result: z = (actual − mean) ÷ SD, for margins and totals, then the share of games beyond 1, 2 and 2.5 SD. A normal distribution gives 31.7%, 4.55% and 1.24%. For count sports, the observed share of one- and two-goal or one- and two-run margins is set against a discretised normal with the model's own mean and SD. The script ran outside the repository (MD-only rule) and is described here instead of committed.

## Results

### Points sports with a normal model (AFL, NFL, NRL)

| League | Games | Margin \|z\|>1 / >2 / >2.5 | Margin z SD | Total \|z\|>1 / >2 / >2.5 | Total z SD | Over: mean p − realised |
|---|---:|---|---:|---|---:|---:|
| AFL | 621 | 33.3% / 5.6% / 1.3% | 1.04 | 32.4% / 5.8% / 2.1% | 1.03 | +0.005 |
| NFL | 816 | 31.4% / 6.1% / 1.6% | 1.05 | 32.2% / 5.3% / 2.5% | 1.04 | +0.029 |
| NRL | 612 | 32.7% / 7.5% / 2.5% | 1.10 | 36.4% / 5.9% / 1.1% | 1.07 | +0.050 |

**NFL key numbers.** Margins of exactly 3 occurred in **14.2%** of games against **5.7%** under a discretised normal; exactly 7 in **8.3%** against **5.2%**. The stored key-number variant scored the same as the normal on winners (Brier 0.2260 v 0.2258) and on the median-line total (0.2412 v 0.2413). Those are lines far from 3 and 7. The gap shows up only on handicap lines at or next to the key numbers.

### Count sports (NHL, MLB)

| League | Games | Observed \|M\|=1 | Normal \|M\|=1 | Normal tie mass | Normal \|M\|=1 + tie mass | Observed \|M\|=2 | Normal \|M\|=2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| NHL | 3,936 | **39.9%** | 28.7% | 15.5% | 44.2% | 19.9% | 22.9% |
| MLB | 9,718 | **28.1%** | 17.4% | 8.9% | 26.3% | 17.9% | 16.1% |

Ties never stand in either league. A tied game is decided by overtime, a shootout or extra innings, almost always by one goal or run, and the home team stops batting in its last half-inning once ahead. That is why one-goal and one-run games are so much more common than a symmetric distribution says. NHL two-goal margins are also shaped by empty-net goals.

The fitted count grids that handle extras explicitly scored better than the league baseline on winners (NHL 0.2401 v 0.2483; MLB 0.2445 v 0.2499) but not on totals (0.2481 v 0.2477; 0.2495 v 0.2500).

### Soccer (EPL, Dixon–Coles grid)

1,140 games. Draws 24.5% observed against 23.3% in the model. Over at the median line: Brier 0.2305 v baseline 0.2310, mean p − realised −0.014. Winner Brier 0.2143 v 0.2458. The exact score grid is already the full distribution; nothing is left for simulation to add.

### Cricket (IPL first innings, normal C2)

211 innings. \|z\|>1 / >2 / >2.5 = 34.1% / 7.6% / **3.8%**, z SD 1.10, mean z +0.10 (scores slightly under-predicted). Over-line Brier: the team model C2 0.2402 against the team-free C0 0.2423 (no meaningful skill). Tails are about three times heavier than normal beyond 2.5 SD (collapses and late-over explosions).

### Tennis

No stored data route (the serve/return source is NOT_READY). The point → game → set → match chain is an exact Markov recursion (PROBABILITY_TOOLKIT §6), so it needs no simulation. Simulation is needed only to add a match-level form shock (XCARD-4) or retirement risk, and even that can be integrated numerically.

## Answer: needed or helpful?

| Sport | Is simulation needed? | What actually helps | Where it may run |
|---|---|---|---|
| Basketball, AFL | No | Normal fits; widen slightly for big spreads (margin tails a little heavy) | Normal table by hand or code |
| NFL | No | An **empirical margin table** for spreads at or near 3 and 7 (the normal under-states those margins by 8.5 and 3.1 percentage points) | Lookup table, no simulation |
| NRL | No | Wider margin and total widths (z SD 1.07–1.10) and a lower total centre (the Over was priced 5 percentage points above its realised rate) | Normal with a Student-t or widened SD |
| Ice hockey | Helpful for puck lines | Regulation grid **plus** explicit OT/shootout (decided by one goal) and an empty-net adjustment for ±1.5 and ±2.5 | Exact grid in code; Monte Carlo of late-game pulls is optional, in code only |
| Baseball | Helpful for run lines | Extra innings plus the home team's final half-inning (one-run games 28% v 17%); an inning-level recursion or simulation | Code only; by hand use the tie-mass-to-one-run reassignment (gets 26.3% v 28.1%) |
| Soccer | No | The Dixon–Coles grid is exact | Code or the toolkit tables |
| Cricket | Helpful only with ball-by-ball data | Wider tails now; a ball-outcome simulator (C4) only after phase models pass, and the current team model shows no skill | Code only, after data capture |
| Tennis | No for the chain; helpful for form shocks | Exact recursion; form-shock integration | Code only |

**Rules adopted in prompt 1 (core step 4).** Use exact calculation. Handle the three structural cases above (NFL key numbers, hockey one-goal games, baseball one-run games) explicitly. Run Monte Carlo only through repository code, for path-dependent families, with the seed and N ≥ 100,000 printed. At 100,000 draws the standard error of a probability is at most 0.0016, below the 0.01-Brier effects the framework measures; at 1,000 it is 0.016. A chat or agent never "simulates" without running code.

## Limits

- Unadmitted development data; the shapes are trustworthy, the skill numbers are not.
- The count-sport comparison uses a normal with the model's mean and SD, not the model's own count grid (which handles extras and is closer).
- No tennis data; the tennis row is reasoned from the method, not measured.
