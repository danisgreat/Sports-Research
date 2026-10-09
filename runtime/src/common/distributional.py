"""Distributional regression, Student-t joint score models, and quantile reconstruction with parametric tails."""

from typing import List, Optional

import numpy as np
from scipy.optimize import minimize
from scipy.special import digamma, gammaln
from scipy.stats import nbinom

from .contracts import ScoreDistribution
from .errors import InsufficientData, NotFitted, require_converged


class NegativeBinomialCountRegressor:
    """Negative binomial (NB2) count regression with a mean model and a single dispersion parameter.

    Var(Y | X) = mu + alpha * mu^2, r = 1 / alpha, p = r / (r + mu). The likelihood is maximised with its analytic gradient;
    an optimiser that does not converge raises `FitFailed` instead of leaving a flat model behind (ML-02). The ridge
    penalty never touches the intercept column (`intercept_column`, default 0; None penalises every coefficient).
    """

    def __init__(self, l2_reg: float = 0.01, intercept_column: Optional[int] = 0):
        self.l2_reg = l2_reg
        self.intercept_column = intercept_column
        self.coef: Optional[np.ndarray] = None
        self.alpha: Optional[float] = None

    @property
    def is_fitted(self) -> bool:
        return self.coef is not None and self.alpha is not None

    @staticmethod
    def _objective(params: np.ndarray, X: np.ndarray, y: np.ndarray, penalty: np.ndarray):
        """Penalised NB2 negative log-likelihood and its analytic gradient in (beta, log alpha)."""
        n_features = X.shape[1]
        beta, log_alpha = params[:n_features], params[n_features]
        r = np.exp(-log_alpha)
        raw = X @ beta
        eta_bound = 12.0
        mu = np.exp(np.clip(raw, -eta_bound, eta_bound))
        log_p = np.log(r) - np.log(r + mu)
        ll = gammaln(y + r) - gammaln(r) - gammaln(y + 1.0) + r * log_p + y * (np.log(mu) - np.log(r + mu))
        d_eta = np.where(np.abs(raw) > eta_bound, 0.0, r * (y - mu) / (r + mu))
        d_r = digamma(y + r) - digamma(r) + log_p + (mu - y) / (r + mu)
        grad = np.empty_like(params)
        grad[:n_features] = -(X.T @ d_eta) + penalty * beta
        grad[n_features] = np.sum(d_r) * r                 # d(-ll)/d(log alpha) = -(dll/dr)(dr/dlog alpha) = sum(d_r) * r
        return -np.sum(ll) + 0.5 * np.sum(penalty * beta ** 2), grad

    def fit(self, X: np.ndarray, y: np.ndarray) -> "NegativeBinomialCountRegressor":
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)
        if X.ndim != 2 or y.ndim != 1 or X.shape[0] != y.shape[0]:
            raise ValueError("X must be (n, k) and y must be (n,) with matching n")
        if not (np.isfinite(X).all() and np.isfinite(y).all()):
            raise ValueError("X and y must be finite")
        if (y < 0).any() or (y != np.round(y)).any():
            raise ValueError("y must hold non-negative integer counts")
        n_samples, n_features = X.shape
        if n_samples < n_features + 5:
            raise InsufficientData(f"need at least {n_features + 5} rows to fit {n_features} coefficients, got {n_samples}")
        penalty = np.full(n_features, self.l2_reg)
        if self.intercept_column is not None:
            penalty[self.intercept_column] = 0.0
        init_args = (X, y, penalty)
        init = np.zeros(n_features + 1)
        init[n_features] = np.log(0.1)
        if self.intercept_column is not None:
            init[self.intercept_column] = np.log(max(float(np.mean(y)), 0.1))
        result = minimize(self._objective, init, args=init_args, jac=True, method="L-BFGS-B", bounds=[(None, None)] * n_features + [(-8.0, 5.0)],
                          options={"maxiter": 500})
        require_converged(result, "NegativeBinomialCountRegressor", grad_tol=1e-3 * max(1.0, float(n_samples)))
        self.coef = result.x[:n_features].copy()
        self.alpha = float(np.exp(result.x[n_features]))
        return self

    def _check(self) -> None:
        if not self.is_fitted:
            raise NotFitted("NegativeBinomialCountRegressor: fit before predicting")

    def predict_mean(self, X: np.ndarray) -> np.ndarray:
        self._check()
        assert self.coef is not None
        X = np.asarray(X, dtype=float)
        return np.exp(np.clip(X @ self.coef, -12.0, 12.0))

    def predict_pmf(self, x_single: np.ndarray, max_count: Optional[int] = None, tail_tolerance: float = 1e-6) -> np.ndarray:
        """Count PMF for one feature vector. Without `max_count` the support extends until the lost tail is below 1e-10;
        an explicit `max_count` that cuts off more than `tail_tolerance` of the mass is an error, not a silent renormalisation."""
        self._check()
        assert self.alpha is not None
        mu = float(self.predict_mean(np.asarray(x_single, dtype=float).reshape(1, -1))[0])
        r = 1.0 / max(self.alpha, 1e-8)
        p = r / (r + mu)
        if max_count is None:
            max_count = int(nbinom.ppf(1.0 - 1e-10, r, p)) + 1
        counts = np.arange(max_count + 1)
        pmf = nbinom.pmf(counts, r, p)
        lost = 1.0 - float(pmf.sum())
        if lost > tail_tolerance:
            raise ValueError(f"max_count={max_count} drops {lost:.2e} of the mass (mean {mu:.2f}); raise max_count")
        return pmf / pmf.sum()


class StudentTJointScoreModel:
    """Bivariate Student-t joint score model capturing heavier tail margins and correlation.

    Parameters: mu_h, mu_a (locations), sigma_h, sigma_a (scales), rho (correlation) and df (> 2 for a finite variance).
    The discretised density is normalised on [min_score, max_score]; a support that leaves more than `mass_tolerance`
    of the continuous mass outside is refused so the truncation can not hide in the normalisation.
    """

    def __init__(self, df: float = 5.0):
        if df <= 2.0:
            raise ValueError("Degrees of freedom df must be > 2 for finite variance")
        self.df = df

    def generate_distribution(self, mu_h: float, mu_a: float, sigma_h: float, sigma_a: float, rho: float,
                              min_score: int, max_score: int, endpoint: str = "unspecified",
                              mass_tolerance: float = 0.01) -> ScoreDistribution:
        if sigma_h <= 0 or sigma_a <= 0 or not -1.0 < rho < 1.0:
            raise ValueError("scales must be positive and rho must lie in (-1, 1)")
        if max_score <= min_score:
            raise ValueError("max_score must exceed min_score")
        scores = np.arange(min_score, max_score + 1)
        H, A = np.meshgrid(scores, scores, indexing="ij")
        z_h, z_a = (H - mu_h) / sigma_h, (A - mu_a) / sigma_a
        q = (z_h ** 2 - 2.0 * rho * z_h * z_a + z_a ** 2) / (1.0 - rho ** 2)
        nu = self.df
        norm_const = 1.0 / (2.0 * np.pi * sigma_h * sigma_a * np.sqrt(1.0 - rho ** 2))
        pdf = norm_const * (1.0 + q / nu) ** (-0.5 * (nu + 2.0))
        mass = float(np.sum(pdf))
        if not mass > 0.0 or abs(mass - 1.0) > mass_tolerance:
            raise ValueError(f"support [{min_score}, {max_score}] holds {mass:.4f} of the Student-t mass; widen it")
        pdf = pdf / mass
        full_grid = np.zeros((max_score + 1, max_score + 1), dtype=float)
        full_grid[min_score:max_score + 1, min_score:max_score + 1] = pdf
        support = np.arange(max_score + 1)
        return ScoreDistribution(grid=full_grid, home_support=support, away_support=support, endpoint=endpoint,
                                 metadata={"model": "student_t_joint", "df": self.df})


class QuantileDistributionReconstructor:
    """Rearranges predicted quantiles (no crossing) and prices tails beyond the outer quantiles parametrically (DST-15).

    Between quantiles the CDF interpolates linearly; beyond the outer ones it continues as an exponential
    (`tail_shape=0`) or generalised-Pareto (`tail_shape` != 0, shape fixed by the caller) tail anchored on the two outer
    quantiles. The result is monotone and continuous at every knot.
    """

    def __init__(self, quantiles: List[float], tail_shape: float = 0.0):
        q = np.array(sorted(quantiles), dtype=float)
        if len(q) < 2 or len(set(q.tolist())) != len(q) or q[0] <= 0.0 or q[-1] >= 1.0:
            raise ValueError("quantiles must be at least two distinct levels strictly inside (0, 1)")
        if not -0.5 < tail_shape < 1.0:
            raise ValueError("tail_shape must lie in (-0.5, 1)")
        self.quantiles = q
        self.tail_shape = float(tail_shape)

    def fix_crossing(self, predicted_quantiles: np.ndarray) -> np.ndarray:
        """Monotone non-decreasing quantiles for each sample (Chernozhukov, Fernandez-Val, Galichon 2010 rearrangement)."""
        return np.sort(np.asarray(predicted_quantiles, dtype=float), axis=-1)

    def _survival_beyond(self, excess: float, s_knot: float, width: float, s_inner: float) -> float:
        """Survival `excess` beyond a knot with survival s_knot, whose neighbour `width` inside has survival s_inner."""
        if excess <= 0:
            return s_knot
        ratio = s_knot / s_inner                      # < 1: survival decays over `width`
        xi = self.tail_shape
        if width <= 0 or ratio >= 1.0:
            return 0.0 if width <= 0 else s_knot       # flat inner segment: no decay information, keep the knot mass
        if abs(xi) < 1e-9:
            return float(s_knot * np.exp(-excess * np.log(1.0 / ratio) / width))
        sigma = xi * width / (ratio ** (-xi) - 1.0)    # GPD scale reproducing the inner decay
        sigma_knot = sigma + xi * width                # threshold-stable scale at the knot
        base = 1.0 + xi * excess / sigma_knot
        return float(s_knot * base ** (-1.0 / xi)) if base > 0 else 0.0

    def survival(self, predicted_quantiles: np.ndarray, threshold: float) -> float:
        """P(Y > threshold) from one sample's quantiles, with parametric tails beyond the outer two levels."""
        q_vals = np.sort(np.asarray(predicted_quantiles, dtype=float))
        if len(q_vals) != len(self.quantiles):
            raise ValueError("predicted_quantiles must have one value per quantile level")
        taus = self.quantiles
        if threshold >= q_vals[-1]:
            # use the nearest distinct inner knot when the top quantiles tie
            j = len(q_vals) - 2
            while j > 0 and q_vals[j] >= q_vals[-1]:
                j -= 1
            return self._survival_beyond(threshold - q_vals[-1], 1.0 - taus[-1], q_vals[-1] - q_vals[j], 1.0 - taus[j])
        if threshold <= q_vals[0]:
            j = 1
            while j < len(q_vals) - 1 and q_vals[j] <= q_vals[0]:
                j += 1
            cdf_below = self._survival_beyond(q_vals[0] - threshold, taus[0], q_vals[j] - q_vals[0], taus[j])
            return float(1.0 - cdf_below)
        return float(np.clip(1.0 - np.interp(threshold, q_vals, taus), 0.0, 1.0))

    def to_probabilities_above(self, predicted_quantiles: np.ndarray, threshold: float) -> float:
        """P(Y > threshold); kept for callers of the original API."""
        return self.survival(predicted_quantiles, threshold)
