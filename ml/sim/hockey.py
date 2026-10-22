"""Ice-hockey game simulator: Poisson goals, the pulled goalie, overtime and the shootout (SIM-v2).

A regulation Poisson grid prices winner and totals but not the late-game structure that decides puck lines: a team trailing by
one goal pulls its goalie (teams did so in about 98% of such cases in the last two minutes, 2013-14 to 2019-20: Hockey-Graphs
2020), which raises its own scoring and gives the leader a high-rate empty-net chance; a tie after regulation is always
broken by one goal in overtime or the shootout. This simulator plays those mechanics.

The empty-net parameters have NO defaults. They must be estimated from NHL play-by-play (api-web.nhle.com) for the
competition and period, recorded with their sample size, and the simulator is NOT_VALIDATED until ``structure_check`` agrees
with the observed share of one-goal and empty-net finishes (SIMULATION_PROTOCOL). The shootout winner defaults to a coin.

    python -m ml sim hockey --lam-home 3.1 --lam-away 2.9 --pull-minutes 1.5 --pull-attack 2.0 --empty-net-rate 0.9 \
        --ot-rate 0.35 --n 200000 --seed 20261022
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ml.sim import core


@dataclass(frozen=True)
class LateGame:
    pull_minutes: float          # the trailing-by-one team pulls its goalie with this many minutes left
    pull_attack_multiplier: float    # that team's scoring rate multiplier with the extra attacker
    empty_net_rate_per_min: float    # the leader's scoring rate into the empty net, goals per minute
    pull_minutes_two: float = 0.0    # optional: trailing by two pulls with this many minutes left (0 = never)


def simulate_game(lam_home: float, lam_away: float, n: int, seed: int, late: LateGame, *, ot_rate_per_min: float,
                  ot_minutes: float = 5.0, p_home_shootout: float = 0.5, regulation_minutes: float = 60.0, dt: float = 1 / 60,
                  card: bool = True) -> dict:
    """``lam_*`` are expected regulation goals per team before any pulled-goalie effect (the late window scales them)."""
    core.check_n(n, card=card)
    if min(lam_home, lam_away, ot_rate_per_min) <= 0 or late.pull_minutes < 0 or late.pull_attack_multiplier <= 0 or late.empty_net_rate_per_min < 0:
        raise core.SimulationError("rates must be positive and the pull parameters non-negative")
    g = core.rng(seed)
    rh, ra = lam_home / regulation_minutes, lam_away / regulation_minutes
    early = regulation_minutes - max(late.pull_minutes, late.pull_minutes_two)
    hs = g.poisson(rh * early, n).astype(np.int32)
    as_ = g.poisson(ra * early, n).astype(np.int32)
    empty_net_goals = np.zeros(n, np.int32)
    steps = int(round(max(late.pull_minutes, late.pull_minutes_two) / dt))
    for step in range(steps):
        left = max(late.pull_minutes, late.pull_minutes_two) - step * dt
        diff = hs - as_
        home_pulls = ((diff == -1) & (left <= late.pull_minutes)) | ((diff == -2) & (late.pull_minutes_two > 0) & (left <= late.pull_minutes_two))
        away_pulls = ((diff == 1) & (left <= late.pull_minutes)) | ((diff == 2) & (late.pull_minutes_two > 0) & (left <= late.pull_minutes_two))
        rate_h = np.where(home_pulls, rh * late.pull_attack_multiplier, np.where(away_pulls, late.empty_net_rate_per_min, rh))
        rate_a = np.where(away_pulls, ra * late.pull_attack_multiplier, np.where(home_pulls, late.empty_net_rate_per_min, ra))
        goal_h = g.random(n) < rate_h * dt
        goal_a = g.random(n) < rate_a * dt
        empty_net_goals += (goal_h & away_pulls).astype(np.int32) + (goal_a & home_pulls).astype(np.int32)
        hs += goal_h
        as_ += goal_a
    reg_h, reg_a = hs.copy(), as_.copy()
    tied = np.flatnonzero(hs == as_)
    decided_ot = np.zeros(n, bool)
    decided_so = np.zeros(n, bool)
    if tied.size:
        # sudden-death overtime: the first goal ends it; the total OT rate splits between the teams by their regulation rates
        total_rate = ot_rate_per_min
        first_goal_time = g.exponential(1 / total_rate, tied.size)
        scored = first_goal_time <= ot_minutes
        home_first = g.random(tied.size) < lam_home / (lam_home + lam_away)
        winner_home = np.where(scored, home_first, g.random(tied.size) < p_home_shootout)
        hs[tied] += winner_home
        as_[tied] += ~winner_home
        decided_ot[tied] = scored
        decided_so[tied] = ~scored
    return dict(home=hs, away=as_, reg_home=reg_h, reg_away=reg_a, ot=decided_ot, shootout=decided_so, empty_net_goals=empty_net_goals,
                n=n, seed=seed)


def structure_check(result: dict) -> dict:
    margin = np.abs(result["home"] - result["away"])
    return dict(n=result["n"], one_goal_share=float((margin == 1).mean()), two_goal_share=float((margin == 2).mean()),
                regulation_tie_share=float((result["reg_home"] == result["reg_away"]).mean()),
                overtime_share=float(result["ot"].mean()), shootout_share=float(result["shootout"].mean()),
                empty_net_goal_share=float((result["empty_net_goals"] > 0).mean()),
                mean_total=float((result["home"] + result["away"]).mean()))


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--lam-home", type=float, required=True)
    parser.add_argument("--lam-away", type=float, required=True)
    parser.add_argument("--pull-minutes", type=float, required=True)
    parser.add_argument("--pull-attack", type=float, required=True)
    parser.add_argument("--empty-net-rate", type=float, required=True)
    parser.add_argument("--ot-rate", type=float, required=True)
    parser.add_argument("--n", type=int, default=core.CARD_MIN_N)
    parser.add_argument("--seed", type=int, default=core.DEFAULT_SEED)
    args = parser.parse_args(argv)
    result = simulate_game(args.lam_home, args.lam_away, args.n, args.seed,
                           LateGame(args.pull_minutes, args.pull_attack, args.empty_net_rate), ot_rate_per_min=args.ot_rate)
    print("parameters supplied by the caller; NOT_VALIDATED until structure_check agrees with observed shares; seed", args.seed, "N", args.n)
    print({k: round(v, 4) for k, v in structure_check(result).items() if k != "n"})


if __name__ == "__main__":
    main()
