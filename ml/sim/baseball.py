"""Inning-level baseball simulator: extras, the automatic runner, the home team's last half-inning (SIM-v2).

The negative-binomial run grid prices totals well but not the structure that decides run lines and first-five markets:
a game tied after nine innings is settled in extras, and the home team stops batting once it leads. Observed one-run
margins are 28.1% of MLB games against 17.4% under a symmetric normal with the model's own mean and SD (22 October 2026
simulation review). This simulator plays each half-inning plate appearance by plate appearance from a team's outcome
probabilities and reproduces both effects mechanically.

A team is described by six plate-appearance outcome probabilities (OUT, BB, 1B, 2B, 3B, HR; BB includes hit by pitch) and
three runner-advancement probabilities. The defaults below are ILLUSTRATIVE and NOT_VALIDATED: they set a plausible
major-league environment (about 4.5 runs per game), not a fitted one. A card uses ``scale_to_runs`` to move a team's
environment to the run mean its own distribution gives, and may use the simulator only after ``structure_check`` against
the competition's observed one-run share and extra-innings rate passes (SIMULATION_PROTOCOL).

    python -m ml sim baseball --home-runs 4.6 --away-runs 4.2 --n 200000 --seed 20261022 --lines "HOME:-1.5,OVER:8.5"
"""
from __future__ import annotations

from dataclasses import dataclass, replace

import numpy as np

from ml.sim import core

OUT, BB, SINGLE, DOUBLE, TRIPLE, HR = range(6)
NO_NEED = 10 ** 6
MAX_EXTRAS = 25


@dataclass(frozen=True)
class Environment:
    probs: tuple = (0.676, 0.085, 0.152, 0.045, 0.004, 0.038)   # ILLUSTRATIVE, NOT_VALIDATED
    p_2nd_scores_on_single: float = 0.60
    p_1st_to_3rd_on_single: float = 0.28
    p_1st_scores_on_double: float = 0.45

    def __post_init__(self):
        if len(self.probs) != 6 or min(self.probs) < 0 or abs(sum(self.probs) - 1) > 1e-9:
            raise core.SimulationError("six non-negative outcome probabilities summing to 1 are required")


def scale(env: Environment, factor: float) -> Environment:
    """Multiply every non-out outcome by ``factor`` (>0) and give the remainder to OUT."""
    p = np.array(env.probs, float)
    p[1:] *= factor
    p[OUT] = 1.0 - p[1:].sum()
    if p[OUT] <= 0.05:
        raise core.SimulationError("scale factor leaves almost no outs")
    return replace(env, probs=tuple(float(x) for x in p))


def half_inning(env: Environment, n: int, g: np.random.Generator, *, ghost_runner: bool = False, need=None) -> np.ndarray:
    """Runs scored in ``n`` independent half-innings. ``need`` (array of n) ends a half-inning once the home team has
    taken the lead: a walk-off HR counts every run, any other walk-off hit counts only the runs needed."""
    outs = np.zeros(n, np.int8)
    b1 = np.zeros(n, bool)
    b2 = np.full(n, bool(ghost_runner))
    b3 = np.zeros(n, bool)
    runs = np.zeros(n, np.int32)
    need = np.full(n, NO_NEED, np.int64) if need is None else np.asarray(need, np.int64)
    active = np.ones(n, bool)
    cum = np.cumsum(env.probs)
    for _ in range(400):
        if not active.any():
            break
        idx = np.flatnonzero(active)
        u = g.random(idx.size)
        o = np.searchsorted(cum, u, side="right").clip(max=5)
        s1, s2, s3 = b1[idx], b2[idx], b3[idx]
        add = np.zeros(idx.size, np.int32)
        n1, n2, n3 = s1.copy(), s2.copy(), s3.copy()
        # outs
        m = o == OUT
        outs[idx[m]] += 1
        # walk: forced advancement
        m = o == BB
        full1, full12 = s1 & m, s1 & s2 & m
        add += (full12 & s3).astype(np.int32)
        n3 = np.where(m & s1 & s2, True, n3)
        n2 = np.where(m & s1, True, n2)
        n1 = np.where(m, True, n1)
        # single
        m = o == SINGLE
        r2 = g.random(idx.size) < env.p_2nd_scores_on_single
        r1 = g.random(idx.size) < env.p_1st_to_3rd_on_single
        add += (m & s3).astype(np.int32) + (m & s2 & r2).astype(np.int32)
        hold2 = s2 & ~r2                       # the runner from second stops at third
        go3 = s1 & r1 & ~hold2                 # the runner from first reaches third only if it is free
        n3 = np.where(m, hold2 | go3, n3)
        n2 = np.where(m, s1 & ~go3, n2)
        n1 = np.where(m, True, n1)
        # double
        m = o == DOUBLE
        d1 = g.random(idx.size) < env.p_1st_scores_on_double
        add += (m & s3).astype(np.int32) + (m & s2).astype(np.int32) + (m & s1 & d1).astype(np.int32)
        n3 = np.where(m, s1 & ~d1, n3)
        n2 = np.where(m, True, n2)
        n1 = np.where(m, False, n1)
        # triple
        m = o == TRIPLE
        add += m * (s1.astype(np.int32) + s2.astype(np.int32) + s3.astype(np.int32))
        n3 = np.where(m, True, n3)
        n2 = np.where(m, False, n2)
        n1 = np.where(m, False, n1)
        # home run
        m = o == HR
        add += m * (1 + s1.astype(np.int32) + s2.astype(np.int32) + s3.astype(np.int32))
        n1, n2, n3 = (np.where(m, False, x) for x in (n1, n2, n3))
        before = runs[idx]
        total = before + add
        capped = (total >= need[idx]) & (o != HR) & (o != OUT)
        total = np.where(capped, np.minimum(total, need[idx]), total)
        runs[idx] = total
        b1[idx], b2[idx], b3[idx] = n1, n2, n3
        done = (outs[idx] >= 3) | (total >= need[idx])
        active[idx[done]] = False
    return runs


def mean_runs_per_game(env: Environment, n: int = 100_000, seed: int = 1, innings: int = 9) -> float:
    return float(half_inning(env, n, core.rng(seed)).mean() * innings)


def scale_to_runs(env: Environment, target_runs_per_game: float, n: int = 100_000, seed: int = 1) -> Environment:
    """Bisect the scale factor so a team's nine-inning mean (no walk-offs) equals the target, with common random numbers."""
    lo, hi = 0.2, 3.0
    for _ in range(18):
        mid = (lo + hi) / 2
        if mean_runs_per_game(scale(env, mid), n, seed) < target_runs_per_game:
            lo = mid
        else:
            hi = mid
    return scale(env, (lo + hi) / 2)


def simulate_game(home: Environment, away: Environment, n: int, seed: int, *, ghost_runner: bool = True, innings: int = 9,
                  card: bool = True) -> dict:
    """``n`` full games with the home team's last-half-inning rule and (optionally) the automatic extra-innings runner."""
    core.check_n(n, card=card)
    g = core.rng(seed)
    hs = np.zeros(n, np.int32)
    as_ = np.zeros(n, np.int32)
    played = np.full(n, innings, np.int16)
    walk_off = np.zeros(n, bool)
    for inning in range(1, innings + 1):
        as_ += half_inning(away, n, g)
        if inning < innings:
            hs += half_inning(home, n, g)
        else:
            bat = np.flatnonzero(hs <= as_)       # the home team does not bat when it already leads
            if bat.size:
                need = as_[bat] - hs[bat] + 1
                got = half_inning(home, bat.size, g, need=need)
                walk_off[bat] = hs[bat] + got > as_[bat]
                hs[bat] += got
    extra = 0
    while True:
        tied = np.flatnonzero(hs == as_)
        if tied.size == 0 or extra >= MAX_EXTRAS:
            break
        extra += 1
        played[tied] += 1
        top = half_inning(away, tied.size, g, ghost_runner=ghost_runner)
        as_[tied] += top
        need = top + 1
        got = half_inning(home, tied.size, g, ghost_runner=ghost_runner, need=need)
        hs[tied] += got
        walk_off[tied] = got > top
    unresolved = int((hs == as_).sum())
    if unresolved:   # a negligible tail; settled by a coin so the grid stays a proper distribution
        flip = np.flatnonzero(hs == as_)
        home_wins = g.random(flip.size) < 0.5
        hs[flip] += home_wins.astype(np.int32)
        as_[flip] += (~home_wins).astype(np.int32)
    return dict(home=hs, away=as_, innings=played, walk_off=walk_off, n=n, seed=seed, unresolved_ties=unresolved)


def structure_check(result: dict) -> dict:
    """The shares a simulator must reproduce before a card may use it: one-run margins and extra-innings games."""
    margin = np.abs(result["home"] - result["away"])
    n = result["n"]
    return dict(n=n, one_run_share=float((margin == 1).mean()), extras_share=float((result["innings"] > 9).mean()),
                walk_off_share=float(result["walk_off"].mean()), mean_total=float((result["home"] + result["away"]).mean()),
                home_win=float((result["home"] > result["away"]).mean()))


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--home-runs", type=float, required=True)
    parser.add_argument("--away-runs", type=float, required=True)
    parser.add_argument("--n", type=int, default=core.CARD_MIN_N)
    parser.add_argument("--seed", type=int, default=core.DEFAULT_SEED)
    parser.add_argument("--no-ghost-runner", action="store_true")
    parser.add_argument("--lines", default="", help="comma list SIDE:LINE, e.g. HOME:-1.5,OVER:8.5")
    args = parser.parse_args(argv)
    base = Environment()
    home, away = scale_to_runs(base, args.home_runs), scale_to_runs(base, args.away_runs)
    result = simulate_game(home, away, args.n, args.seed, ghost_runner=not args.no_ghost_runner)
    grid = core.histogram_grid(result["home"], result["away"])
    print("ILLUSTRATIVE environment, NOT_VALIDATED; seed", args.seed, "N", args.n)
    print({k: round(v, 4) for k, v in structure_check(result).items() if k != "n"})
    for item in filter(None, args.lines.split(",")):
        side, line = item.split(":")
        m = grid.total(float(line), side) if side in ("OVER", "UNDER") else grid.handicap(float(line), side)
        print(f"{item}: W {m.win:.4f} P {m.push:.4f} L {m.loss:.4f} p {m.p_decisive:.4f} (MC se <= {0.5 / args.n ** 0.5:.4f})")


if __name__ == "__main__":
    main()
