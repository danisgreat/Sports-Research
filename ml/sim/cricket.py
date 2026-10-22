"""Ball-by-ball limited-overs innings simulator: phases, wickets in hand and the chase (SIM-v2).

The cricket cards need a first-innings total distribution with its heavy tails (collapses and late-over surges: about three
times the normal tail beyond 2.5 SD in the IPL development data) and a chase that stops at the winning run. This simulator
plays an innings delivery by delivery from phase tables of outcome probabilities, with optional multipliers for wickets
already lost.

There are NO default tables. A table is built from ball-by-ball history for the exact competition, format and venue class
(Cricsheet: every international and league match in ball-by-ball CSV), recorded with its sample size, and the simulator is
NOT_VALIDATED until its simulated total distribution covers the held-out totals (SIMULATION_PROTOCOL).

A phase table maps a phase name to ``(first_ball, last_ball, {outcome: probability})`` with outcomes
``0,1,2,3,4,6`` (runs off the bat), ``W`` (wicket) and ``X`` (a wide or no-ball: one run, the delivery is not counted).

    python -m ml sim cricket --table TABLE.csv --n 200000 --seed 20261022 [--target 168]
"""
from __future__ import annotations

import numpy as np

from ml.sim import core

OUTCOME_RUNS = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "6": 6, "W": 0, "X": 1}


def _validate(table: dict, balls: int) -> list:
    phases = []
    covered = np.zeros(balls, bool)
    for name, (first, last, probs) in table.items():
        if set(probs) - set(OUTCOME_RUNS) or abs(sum(probs.values()) - 1) > 1e-6 or min(probs.values()) < 0:
            raise core.SimulationError(f"phase {name}: outcomes must be a subset of {sorted(OUTCOME_RUNS)} and sum to 1")
        if not 1 <= first <= last <= balls or covered[first - 1:last].any():
            raise core.SimulationError(f"phase {name}: ball range must lie inside 1..{balls} and not overlap another phase")
        covered[first - 1:last] = True
        keys = sorted(probs)
        phases.append((first, last, keys, np.array([probs[k] for k in keys], float)))
    if not covered.all():
        raise core.SimulationError("the phase tables must cover every legal delivery")
    return phases


def simulate_innings(table: dict, n: int, seed: int, *, balls: int = 120, wickets: int = 10, target: int | None = None,
                     wicket_run_factor=None, wicket_prob_factor=None, card: bool = True) -> dict:
    """``n`` innings. ``target`` (runs to win) makes this a chase: it stops once the target is reached.

    ``wicket_run_factor[w]`` scales the non-wicket outcome weights other than dot balls when ``w`` wickets are down;
    ``wicket_prob_factor[w]`` scales the wicket probability. Both default to 1 (no dependence on wickets in hand).
    """
    core.check_n(n, card=card)
    g = core.rng(seed)
    phases = _validate(table, balls)
    run_f = np.ones(wickets + 1) if wicket_run_factor is None else np.asarray(wicket_run_factor, float)
    wick_f = np.ones(wickets + 1) if wicket_prob_factor is None else np.asarray(wicket_prob_factor, float)
    if run_f.size != wickets + 1 or wick_f.size != wickets + 1 or min(run_f.min(), wick_f.min()) < 0:
        raise core.SimulationError("wicket factors need one non-negative value per wickets-lost count (0..wickets)")
    runs = np.zeros(n, np.int32)
    lost = np.zeros(n, np.int8)
    legal = np.zeros(n, np.int16)
    active = np.ones(n, bool)
    for _ in range(balls * 2 + 20):
        if not active.any():
            break
        idx = np.flatnonzero(active)
        ball_no = legal[idx] + 1
        out = np.empty(idx.size, "<U1")
        for first, last, keys, base in phases:
            m = (ball_no >= first) & (ball_no <= last)
            if not m.any():
                continue
            weights = np.tile(base, (m.sum(), 1))
            for j, k in enumerate(keys):
                if k == "W":
                    weights[:, j] *= wick_f[lost[idx[m]]]
                elif k not in ("0", "X"):
                    weights[:, j] *= run_f[lost[idx[m]]]
            weights /= weights.sum(axis=1, keepdims=True)
            draw = (g.random(m.sum())[:, None] > np.cumsum(weights, axis=1)).sum(axis=1).clip(max=len(keys) - 1)
            out[m] = np.array(keys)[draw]
        add = np.array([OUTCOME_RUNS[o] for o in out], np.int32) if out.size else np.zeros(0, np.int32)
        is_w, is_x = out == "W", out == "X"
        runs[idx] += add
        lost[idx] += is_w
        legal[idx] += ~is_x
        done = (lost[idx] >= wickets) | (legal[idx] >= balls)
        if target is not None:
            done |= runs[idx] >= target
        active[idx[done]] = False
    result = dict(runs=runs, wickets=lost, balls=legal, n=n, seed=seed)
    if target is not None:
        result["chase_won"] = runs >= target
    return result


def total_summary(result: dict) -> dict:
    r = result["runs"].astype(float)
    mean, sd = r.mean(), r.std()
    z = (r - mean) / sd
    return dict(n=result["n"], mean=float(mean), sd=float(sd), beyond_2sd=float((np.abs(z) > 2).mean()), beyond_2_5sd=float((np.abs(z) > 2.5).mean()),
                all_out_share=float((result["wickets"] >= 10).mean()))


def main(argv=None):
    import argparse
    import csv
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--table", required=True, help="CSV: phase,first_ball,last_ball,outcome,probability")
    parser.add_argument("--n", type=int, default=core.CARD_MIN_N)
    parser.add_argument("--seed", type=int, default=core.DEFAULT_SEED)
    parser.add_argument("--target", type=int)
    parser.add_argument("--balls", type=int, default=120)
    args = parser.parse_args(argv)
    table: dict = {}
    with open(args.table, newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            row = table.setdefault(r["phase"], [int(r["first_ball"]), int(r["last_ball"]), {}])
            row[2][r["outcome"]] = float(r["probability"])
    result = simulate_innings({k: tuple(v) for k, v in table.items()}, args.n, args.seed, balls=args.balls, target=args.target)
    print("table supplied by the caller; NOT_VALIDATED until held-out coverage passes; seed", args.seed, "N", args.n)
    print({k: round(v, 4) for k, v in total_summary(result).items() if k != "n"})
    if args.target is not None:
        print("chase win probability", round(float(result["chase_won"].mean()), 4))


if __name__ == "__main__":
    main()
