"""Remove the bookmaker margin from a complete set of decimal odds (DECISION_LAB only; never a card input)."""
from __future__ import annotations

import numpy as np
from scipy.optimize import brentq


def _implied(odds) -> np.ndarray:
    odds = np.asarray(odds, float)
    if odds.ndim != 1 or odds.size < 2 or not np.isfinite(odds).all() or np.any(odds <= 1):
        raise ValueError("a complete vector of finite decimal odds greater than 1 is required")
    return 1 / odds


def multiplicative(odds) -> np.ndarray:
    q = _implied(odds)
    return q / q.sum()


def power(odds) -> np.ndarray:
    q = _implied(odds)
    if abs(q.sum() - 1) < 1e-12:
        return q
    upper = 1.0
    while (q ** upper).sum() > 1:
        upper *= 2
    k = brentq(lambda k: (q ** k).sum() - 1, 0.0, upper)
    return q ** k


def shin(odds) -> np.ndarray:
    q = _implied(odds)
    s = q.sum()
    if s <= 1 + 1e-12:
        return q / s

    def probabilities(z):
        return (2 * q * q / s) / (np.sqrt(z * z + 4 * (1 - z) * q * q / s) + z)

    z = brentq(lambda z: probabilities(z).sum() - 1, 0.0, np.nextafter(1.0, 0.0))
    return probabilities(z)


METHODS = {"multiplicative": multiplicative, "power": power, "shin": shin}


def clv(odds_taken: float, p_fair_close: float) -> float:
    """Closing-line value of a price taken: o_taken * p_fair_close - 1 (positive beats the fair close)."""
    return odds_taken * p_fair_close - 1
