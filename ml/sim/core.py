"""Seeded Monte Carlo helpers shared by the simulators (SIM-v2).

A simulation is run only in code, with the seed and N printed and the Monte Carlo standard error reported. A probability
that sits within 3 standard errors of a gate or of another row is not resolved by the simulation (it is printed
MC_UNRESOLVED). Common random numbers are used when two contracts are compared: both read the same simulated games.
"""
from __future__ import annotations

import math

import numpy as np

CARD_MIN_N = 100_000      # SIM-v2: the smallest N a card may use near a threshold (standard error <= 0.0016 at p = 0.5)
DEFAULT_SEED = 20261022


class SimulationError(ValueError):
    pass


def rng(seed: int | None) -> np.random.Generator:
    if seed is None:
        raise SimulationError("a seed is required: simulations are reproducible or they are not reported")
    return np.random.default_rng(int(seed))


def check_n(n: int, *, card: bool = True) -> int:
    if int(n) != n or n < 1:
        raise SimulationError("N must be a positive integer")
    if card and n < CARD_MIN_N:
        raise SimulationError(f"N = {n} is below the card minimum {CARD_MIN_N}; pass card=False only for tests and development")
    return int(n)


def probability(hits: np.ndarray, seed: int, n: int | None = None) -> dict:
    """p and its Monte Carlo standard error from a boolean (or 0/1) array of simulated outcomes."""
    hits = np.asarray(hits, bool)
    n = int(hits.size) if n is None else int(n)
    p = float(hits.mean())
    se = math.sqrt(max(p * (1 - p), 0.0) / n)
    return dict(p=p, se=se, n=n, seed=int(seed))


def decisive(win: np.ndarray, loss: np.ndarray, seed: int) -> dict:
    """W/P/L masses and the decisive probability W/(W+L) with a delta-method standard error."""
    win, loss = np.asarray(win, bool), np.asarray(loss, bool)
    n = int(win.size)
    w, l = float(win.mean()), float(loss.mean())
    push = max(0.0, 1.0 - w - l)
    d = w + l
    p = w / d if d > 0 else float("nan")
    se = math.sqrt(p * (1 - p) / (n * d)) if d > 0 else float("nan")
    return dict(w=w, p=push, l=l, p_decisive=p, se=se, n=n, seed=int(seed))


def unresolved(p: float, se: float, threshold: float, sigmas: float = 3.0) -> bool:
    return abs(p - threshold) <= sigmas * se


def histogram_grid(home: np.ndarray, away: np.ndarray):
    """Empirical ScoreGrid of simulated (home, away) scores, so contracts are priced by the same code as every card."""
    from ml.core.distributions import ScoreGrid
    home, away = np.asarray(home, int), np.asarray(away, int)
    if home.min() < 0 or away.min() < 0:
        raise SimulationError("scores must be non-negative")
    grid = np.zeros((home.max() + 1, away.max() + 1))
    np.add.at(grid, (home, away), 1.0)
    return ScoreGrid(grid / grid.sum())
