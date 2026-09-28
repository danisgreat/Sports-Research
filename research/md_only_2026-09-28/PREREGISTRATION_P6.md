# P6 — does TB-1-MD have resolution in the other top soccer leagues? (preregistered 2026-09-28, before any run)

**Why.** About 80 soccer cards spread over more than 30 competitions, but TB-1 is validated only for the EPL. The existing rule, authorised by the user on 2026-09-25(e), is "anchor on TB-1 where it has resolution". A league that passes this test gains the anchor under that rule. This is not a new coefficient: k = 2 and the formula are the EPL's, unchanged. The user's bar applies: held-out, 95% interval below 0.

**Data.** openfootball `football.json` (results only: date, teams, full-time score), seasons 2020-21 to 2025-26:
- EPL (`en.1`), as the replication control;
- La Liga (`es.1`), Bundesliga (`de.1`), Serie A (`it.1`), Ligue 1 (`fr.1`).

No odds are read.

**Model.** TB-1-MD exactly as in `PROBABILITY_TOOLKIT.md` §4:
- Poisson, with k = 2 fixed (the EPL tool value, not tuned);
- λh = (T + M)/2 and λa = (T − M)/2;
- home edge HE = the previous season's mean home goal margin in the same league. So 2020-21 only supplies HE, and the scored seasons are 2021-22 to 2025-26;
- each game is forecast only from games strictly before its date. A team must have played at least 1 game and the league at least 10 games;
- no previous-season carry-over.

**Comparator (population).** The running, in-season league rates before each game: P(home), P(draw), P(away), and P(total ≥ 3).

**Metrics.**
- **Primary, results:** three-way Brier, the sum over home/draw/away of (p − y)².
- **Primary, totals:** the Brier of P(Over 2.5).
- **Secondary:** the Brier of P(home win).
- **Intervals:** 95% ISO-week block bootstrap (2,000 draws, seed 20260928) on the per-game difference MD − population.

**Decision rule, per league and target.** Fixed now; it cannot move after the results are seen.
- **RESOLUTION:** the pooled 2021-22 to 2025-26 difference has its 95% interval entirely below 0 **and** the difference is below 0 in at least 4 of the 5 seasons.
- **Otherwise NO RESOLUTION.** The league's cards keep the population anchor, and TB-1-MD is printed as `UNVALIDATED`/reference.
- **The EPL result is the replication check.** It is expected to pass for results and fail for totals, as in 2025-26. If the EPL fails results, the whole test is reported, and nothing is promoted for any league.

**What happens next.**
- A league that passes becomes a TB-1-MD anchor for the passed target in `PROBABILITY_TOOLKIT.md` §4.3 and the soccer §0 page.
- A league that fails keeps the population anchor.
- Either way the result is recorded in `LEARNING_REGISTER.md`.

Script: `p6_soccer_tb1md.py`, results in `p6_soccer_tb1md.json`.
