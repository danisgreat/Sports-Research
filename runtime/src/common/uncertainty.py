"""Block-bootstrap uncertainty, Wilson intervals, Cox calibration and power (EVL-02, EVL-03).

Forecasts made in the same week share weather, fixtures, injuries and news, so rows are not independent. The scoring
standard resamples whole blocks (an ISO week, or a match day) and never single rows.
"""

import datetime as _dt
import math
from typing import Callable, Dict, Optional, Sequence, Tuple

import numpy as np
from scipy.special import expit, logit
from scipy.stats import norm

from .errors import FitFailed


def week_block_ids(dates: Sequence[str]) -> np.ndarray:
    """ISO year-week labels (e.g. '2026-W41') for ISO dates ('2026-10-09' or a longer timestamp)."""
    out = []
    for value in dates:
        d = _dt.date.fromisoformat(str(value)[:10])
        iso = d.isocalendar()
        out.append(f"{iso[0]}-W{iso[1]:02d}")
    return np.array(out)


def block_indices(block_ids: np.ndarray, rng: np.random.Generator, groups: Optional[Dict[str, np.ndarray]] = None) -> np.ndarray:
    """Row indices of one block resample: draw as many blocks as exist, with replacement, and concatenate their rows."""
    if groups is None:
        groups = group_rows(block_ids)
    labels = list(groups)
    draw = rng.integers(0, len(labels), size=len(labels))
    return np.concatenate([groups[labels[i]] for i in draw])


def group_rows(block_ids: np.ndarray) -> Dict[str, np.ndarray]:
    ids = np.asarray(block_ids)
    return {str(b): np.flatnonzero(ids == b) for b in np.unique(ids)}


def block_bootstrap(stat: Callable[..., float], arrays: Sequence[np.ndarray], block_ids: np.ndarray,
                    n_resamples: int = 1000, seed: int = 42) -> np.ndarray:
    """`stat(*resampled_arrays)` over block resamples; returns the bootstrap distribution."""
    ids = np.asarray(block_ids)
    if any(len(a) != len(ids) for a in arrays):
        raise ValueError("every array must have one entry per block id")
    groups = group_rows(ids)
    rng = np.random.default_rng(seed)
    out = np.empty(n_resamples)
    for i in range(n_resamples):
        rows = block_indices(ids, rng, groups)
        out[i] = stat(*[a[rows] for a in arrays])
    return out


def percentile_interval(samples: np.ndarray, level: float = 0.95) -> Tuple[float, float]:
    tail = (1.0 - level) / 2.0 * 100.0
    return float(np.percentile(samples, tail)), float(np.percentile(samples, 100.0 - tail))


def wilson_interval(successes: int, n: int, level: float = 0.95) -> Tuple[float, float]:
    """Wilson score interval for a binomial rate; (0, 1) when n = 0."""
    if n <= 0:
        return 0.0, 1.0
    z = norm.ppf(0.5 + level / 2.0)
    p = successes / n
    denom = 1.0 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return max(0.0, centre - half), min(1.0, centre + half)


def cox_calibration(y: np.ndarray, p: np.ndarray, ridge: float = 1e-4, max_iter: int = 100) -> Tuple[float, float]:
    """(alpha, beta) of logit P(Y=1) = alpha + beta * logit(p) by damped Newton iterations with a weak ridge toward (0, 1).

    The objective is convex, so backtracking on the penalised negative log-likelihood always converges; if it does not within
    `max_iter` it raises `FitFailed` instead of returning a default.
    """
    y = np.asarray(y, dtype=float)
    z = logit(np.clip(np.asarray(p, dtype=float), 1e-6, 1.0 - 1e-6))
    x = np.column_stack([np.ones_like(z), z])
    prior = np.array([0.0, 1.0])

    def nll(theta: np.ndarray) -> float:
        eta = x @ theta
        return float(np.sum(np.logaddexp(0.0, eta) - y * eta) + 0.5 * ridge * np.sum((theta - prior) ** 2))

    theta = prior.copy()
    current = nll(theta)
    for _ in range(max_iter):
        mu = expit(x @ theta)
        grad = x.T @ (mu - y) + ridge * (theta - prior)
        hess = (x * (mu * (1 - mu))[:, None]).T @ x + ridge * np.eye(2)
        step = np.linalg.solve(hess, grad)
        scale = 1.0
        while scale > 1e-10:
            candidate = theta - scale * step
            value = nll(candidate)
            if value <= current + 1e-12:
                break
            scale *= 0.5
        else:
            if np.max(np.abs(grad)) < 1e-6 * max(1.0, len(y)):
                return float(theta[0]), float(theta[1])
            break
        theta, current = candidate, value
        if np.max(np.abs(scale * step)) < 1e-9:
            return float(theta[0]), float(theta[1])
    raise FitFailed("cox_calibration", "Newton iterations did not converge")


def power_summary(delta: float, bootstrap_deltas: np.ndarray, alpha: float = 0.05, power: float = 0.80) -> Dict[str, float]:
    """Normal-approximation power for a paired delta using the block-bootstrap standard error.

    `power_at_observed` is the chance a test at level alpha would reject delta = 0 if the true effect equals the observed
    one (one-sided: the gate only cares about improvement); `minimum_detectable_delta` is the effect detectable with the
    stated power at this n and block structure.
    """
    se = float(np.std(bootstrap_deltas, ddof=1))
    if se == 0.0 or not math.isfinite(se):
        return {"standard_error": se, "power_at_observed": float("nan"), "minimum_detectable_delta": float("nan")}
    z_alpha, z_power = norm.ppf(1 - alpha), norm.ppf(power)
    return {"standard_error": se,
            "power_at_observed": float(norm.cdf(-delta / se - z_alpha)),                    # improvement means delta < 0
            "minimum_detectable_delta": float(-(z_alpha + z_power) * se)}
