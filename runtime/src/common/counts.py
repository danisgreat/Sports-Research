"""Joint count distributions with negative dependence: negative-binomial total, beta-binomial split.

Two teams that trade possession (rugby league, AFL, football corners) produce counts that are negatively
correlated: when one side does more, the other does less. Independent marginals cannot reproduce that
(NRL home/away scores correlate at about -0.3). Here the total is over-dispersed and the home share varies
around its expectation, which gives the right covariance with two interpretable parameters.
"""

import numpy as np
from scipy.optimize import brentq
from scipy.special import gammaln
from scipy.stats import betabinom, binom, nbinom, poisson


def nb_pmf(mean: float, phi: float, size: int) -> np.ndarray:
    """Negative binomial with Var = mean + phi * mean^2 over 0..size-1 (Poisson when phi is ~0), renormalised."""
    if mean < 0:
        raise ValueError("mean must be non-negative")
    if mean == 0:
        out = np.zeros(size)
        out[0] = 1.0
        return out
    if phi < 1e-6:
        pmf = poisson.pmf(np.arange(size), mean)
    else:
        r = 1.0 / phi
        pmf = nbinom.pmf(np.arange(size), r, r / (r + mean))
    return pmf / pmf.sum()


def cmp_pmf(mean: float, nu: float, size: int) -> np.ndarray:
    """Conway-Maxwell-Poisson with the given mean: P(k) proportional to lambda^k / (k!)^nu.

    nu = 1 is Poisson, nu > 1 is under-dispersed (variance below the mean, as in rugby league try counts),
    nu < 1 is over-dispersed. lambda is solved so that the mean is exact on the truncated support.
    """
    if mean <= 0:
        raise ValueError("mean must be positive")
    if nu <= 0:
        raise ValueError("nu must be positive")
    k = np.arange(size)
    log_base = -nu * gammaln(k + 1.0)

    def pmf_for(log_lambda: float) -> np.ndarray:
        logits = k * log_lambda + log_base
        logits -= logits.max()
        weights = np.exp(logits)
        return weights / weights.sum()

    def gap(log_lambda: float) -> float:
        return float(k @ pmf_for(log_lambda)) - mean

    if mean >= size - 1:
        raise ValueError("support too small for the requested mean")
    return pmf_for(brentq(gap, -60.0, 60.0, xtol=1e-12))


def split_given_total(totals: np.ndarray, share: float, concentration: float, size: int) -> np.ndarray:
    """Joint (home, away) grid from a total-count pmf and a beta-binomial split with the given home share."""
    grid = np.zeros((size, size))
    a, b = share * concentration, (1.0 - share) * concentration
    for t, p_t in enumerate(totals):
        if p_t < 1e-14:
            continue
        split = betabinom.pmf(np.arange(t + 1), t, a, b) if concentration < 1e5 else binom.pmf(np.arange(t + 1), t, share)
        idx = np.arange(t + 1)
        in_bounds = (idx < size) & (t - idx < size)
        grid[idx[in_bounds], (t - idx)[in_bounds]] += p_t * split[in_bounds]
    return grid / grid.sum()


def split_total_grid(mean_home: float, mean_away: float, phi: float, concentration: float, size: int,
                     share_shift: float = 0.0, total_pmf=None) -> np.ndarray:
    """Joint (home, away) count grid: total ~ NB(mean_home + mean_away, phi); home | total ~ BetaBinomial(total, share, concentration).

    share_shift is subtracted from the expected home share (score-state or regime adjustments). A very large
    concentration makes the split binomial; a small one makes the teams' counts strongly negatively dependent.
    `total_pmf` replaces the negative-binomial total (for example a `cmp_pmf` when counts are under-dispersed).
    """
    total_mean = mean_home + mean_away
    if total_mean <= 0:
        raise ValueError("expected total must be positive")
    share = float(np.clip(mean_home / total_mean - share_shift, 0.02, 0.98))
    totals = nb_pmf(total_mean, phi, 2 * size) if total_pmf is None else total_pmf
    return split_given_total(totals, share, concentration, size)


def count_moments(grid: np.ndarray):
    """(mean_home, mean_away, var_total, var_margin) of a joint count grid."""
    h, a = np.meshgrid(np.arange(grid.shape[0]), np.arange(grid.shape[1]), indexing="ij")
    mh, ma = float((h * grid).sum()), float((a * grid).sum())
    return mh, ma, float(((h + a - mh - ma) ** 2 * grid).sum()), float(((h - a - mh + ma) ** 2 * grid).sum())
