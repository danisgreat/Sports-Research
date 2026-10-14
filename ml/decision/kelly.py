"""Fractional Kelly with shrinkage for estimation error (Baker & McHale 2013 style), with hard caps."""
from __future__ import annotations

import numpy as np


def kelly_full(p_win: float, odds: float, p_push: float = 0.0) -> float:
    """Log-optimal fraction for win (+b f), push (0), loss (-f): f* = (p_w b - p_l) / (b (p_w + p_l))."""
    b = odds - 1.0
    p_loss = 1.0 - p_win - p_push
    if b <= 0 or p_win * b - p_loss <= 0:
        return 0.0
    return (p_win * b - p_loss) / (b * (p_win + p_loss))


def shrink_factor(f: float, odds: float, sigma_p: float) -> float:
    """f^2 / (f^2 + Var(f_hat)), with Var(f_hat) ~= (sigma_p * df/dp)^2 and df/dp = odds / (odds - 1) (no push)."""
    if f <= 0:
        return 0.0
    if sigma_p <= 0:
        return 1.0
    var_f = (sigma_p * odds / (odds - 1.0)) ** 2
    return f * f / (f * f + var_f)


def stake(p_win: float, odds: float, sigma_p: float, fraction: float = 0.25, cap: float = 0.02) -> float:
    f = kelly_full(p_win, odds)
    return float(min(cap, fraction * shrink_factor(f, odds, sigma_p) * f))


def cap_slate(stakes: np.ndarray, slate_cap: float = 0.10) -> np.ndarray:
    total = float(np.sum(stakes))
    return stakes if total <= slate_cap or total == 0 else stakes * (slate_cap / total)
