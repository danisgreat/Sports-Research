"""Player-prop engine: minutes x per-minute rates with a shared game environment (REV-11 / SIM-v2).

A player's points, rebounds or assists are not independent of the game: they share the game's pace and total, and a blowout
sends starters to the bench. Pricing a prop from the player's average alone, or two props from independent normals, mis-prices
exactly the correlated and same-game combinations. This engine draws one game environment per simulated game (total and margin
from the card's own distribution), then each player's availability, minutes and stat counts conditional on it:

    availability  Bernoulli(availability_p)            a questionable player is a mixture, never a guess at "plays"
    minutes       normal(minutes_mean, minutes_sd), cut at 0 and ``max_minutes``; starters lose
                  ``blowout_minutes_loss`` x min(1, (|margin| - threshold) / ramp) in a blowout
    count         gamma-Poisson (negative binomial) with mean  rate_per_min x minutes x (total / total_mean) ** elasticity
                  and variance mean + dispersion x mean ** 2

Every parameter is supplied by the caller and recorded with its basis; there are no fitted defaults. The engine is
NOT_VALIDATED until ``coverage`` on held-out games lies within 3 points of nominal at the 50% and 80% central bands for every
stat it will price (SIMULATION_PROTOCOL). Output is samples, so any single or joint probability carries its Monte Carlo error.

    python -m ml sim props --players PLAYERS.csv --total-mean 229 --total-sd 18.7 --margin-mean -9.5 --margin-sd 14 \
        --n 200000 --seed 20261022
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from ml.sim import core


@dataclass
class Player:
    name: str
    team: str                      # HOME or AWAY
    starter: bool
    minutes_mean: float
    minutes_sd: float
    rates: dict = field(default_factory=dict)       # stat -> (rate per minute, dispersion)
    availability_p: float = 1.0
    max_minutes: float = 48.0


@dataclass(frozen=True)
class Environment:
    total_mean: float
    total_sd: float
    margin_mean: float             # home minus away
    margin_sd: float
    elasticity: dict = field(default_factory=dict)  # stat -> exponent on (total / total_mean); missing stats use 1.0
    blowout_threshold: float = 15.0
    blowout_ramp: float = 10.0
    blowout_minutes_loss: float = 6.0


def simulate(players: list[Player], env: Environment, n: int, seed: int, *, card: bool = True) -> dict:
    core.check_n(n, card=card)
    if env.total_sd <= 0 or env.margin_sd <= 0 or env.total_mean <= 0:
        raise core.SimulationError("environment needs a positive total mean and positive SDs")
    g = core.rng(seed)
    total = np.maximum(g.normal(env.total_mean, env.total_sd, n), 1.0)
    margin = g.normal(env.margin_mean, env.margin_sd, n)
    blowout = np.clip((np.abs(margin) - env.blowout_threshold) / env.blowout_ramp, 0.0, 1.0)
    out = {}
    for p in players:
        if not 0 <= p.availability_p <= 1 or p.minutes_sd < 0 or p.minutes_mean < 0:
            raise core.SimulationError(f"{p.name}: invalid availability or minutes")
        plays = g.random(n) < p.availability_p
        minutes = g.normal(p.minutes_mean, p.minutes_sd, n)
        if p.starter:
            minutes = minutes - env.blowout_minutes_loss * blowout
        minutes = np.where(plays, np.clip(minutes, 0.0, p.max_minutes), 0.0)
        stats = {}
        for stat, (rate, dispersion) in p.rates.items():
            mean = rate * minutes * (total / env.total_mean) ** env.elasticity.get(stat, 1.0)
            if dispersion > 1e-9:
                lam = g.gamma(1.0 / dispersion, np.maximum(mean, 1e-12) * dispersion)
            else:
                lam = mean
            stats[stat] = g.poisson(np.maximum(lam, 0.0)).astype(np.int32)
        stats["MIN"] = minutes
        out[p.name] = stats
    return dict(players=out, total=total, margin=margin, n=n, seed=seed)


def prob_over(samples: np.ndarray, line: float, seed: int) -> dict:
    """P(over), P(push), P(under) for one stat sample at ``line`` with the Monte Carlo error of the decisive probability."""
    return core.decisive(samples > line, samples < line, seed)


def joint(seed: int, *conditions: np.ndarray) -> dict:
    """Probability that every boolean condition holds in the same simulated game (same-game combinations)."""
    return core.probability(np.logical_and.reduce([np.asarray(c, bool) for c in conditions]), seed)


def coverage(samples: list[np.ndarray], actual: np.ndarray, bands=(0.5, 0.8)) -> dict:
    """Share of held-out actuals inside the central ``band`` interval of each game's predictive sample (randomised PIT-free)."""
    actual = np.asarray(actual, float)
    if len(samples) != actual.size:
        raise core.SimulationError("one predictive sample per held-out actual")
    out = {}
    for band in bands:
        lo, hi = (1 - band) / 2, 1 - (1 - band) / 2
        inside = [np.quantile(s, lo) <= a <= np.quantile(s, hi) for s, a in zip(samples, actual)]
        out[band] = float(np.mean(inside))
    return out


def main(argv=None):
    import argparse
    import csv
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--players", required=True, help="CSV: name,team,starter,minutes_mean,minutes_sd,availability_p,stat,rate,dispersion")
    parser.add_argument("--total-mean", type=float, required=True)
    parser.add_argument("--total-sd", type=float, required=True)
    parser.add_argument("--margin-mean", type=float, required=True)
    parser.add_argument("--margin-sd", type=float, required=True)
    parser.add_argument("--n", type=int, default=core.CARD_MIN_N)
    parser.add_argument("--seed", type=int, default=core.DEFAULT_SEED)
    args = parser.parse_args(argv)
    players: dict = {}
    with open(args.players, newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            p = players.setdefault(r["name"], Player(r["name"], r["team"], r["starter"].lower() in ("1", "true", "yes", "y"),
                                                      float(r["minutes_mean"]), float(r["minutes_sd"]), {}, float(r["availability_p"])))
            p.rates[r["stat"]] = (float(r["rate"]), float(r["dispersion"]))
    env = Environment(args.total_mean, args.total_sd, args.margin_mean, args.margin_sd)
    result = simulate(list(players.values()), env, args.n, args.seed)
    print("parameters supplied by the caller; NOT_VALIDATED until held-out coverage passes; seed", args.seed, "N", args.n)
    for name, stats in result["players"].items():
        for stat, s in stats.items():
            print(f"{name} {stat}: mean {s.mean():.2f} sd {s.std():.2f} p10/p50/p90 {np.quantile(s, [.1, .5, .9]).round(1).tolist()}")


if __name__ == "__main__":
    main()
