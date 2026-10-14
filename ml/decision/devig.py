"""Remove the bookmaker margin from a complete set of decimal odds (DECISION_LAB only; never a card input)."""
from __future__ import annotations

import numpy as np
from scipy.optimize import brentq


def multiplicative(odds) -> np.ndarray:
    q = 1 / np.asarray(odds, float)
    return q / q.sum()


def power(odds) -> np.ndarray:
    q = 1 / np.asarray(odds, float)
    if abs(q.sum() - 1) < 1e-12:
        return q
    k = brentq(lambda k: (q ** k).sum() - 1, 0.2, 5.0)
    return q ** k


def shin(odds) -> np.ndarray:
    q = 1 / np.asarray(odds, float)
    s = q.sum()
    if s <= 1 + 1e-12:
        return q / s

    def f(z):
        p = (np.sqrt(z * z + 4 * (1 - z) * q * q / s) - z) / (2 * (1 - z))
        return p.sum() - 1

    z = brentq(f, 0.0, 0.5)
    return (np.sqrt(z * z + 4 * (1 - z) * q * q / s) - z) / (2 * (1 - z))


METHODS = {"multiplicative": multiplicative, "power": power, "shin": shin}


def clv(odds_taken: float, p_fair_close: float) -> float:
    """Closing-line value of a price taken: o_taken * p_fair_close - 1 (positive beats the fair close)."""
    return odds_taken * p_fair_close - 1
