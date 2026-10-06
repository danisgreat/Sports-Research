"""Distributional regression, Student-t joint score models, and quantile reconstruction."""

from typing import Dict, List, Optional, Tuple
import numpy as np
from scipy.optimize import minimize
from scipy.special import gamma as gamma_fn, gammaln
from scipy.stats import nbinom
from .contracts import ScoreDistribution


class NegativeBinomialCountRegressor:
    """Negative binomial count regression modeling conditional mean and overdispersion:
    
    Var(Y | X) = mu + alpha * mu^2.
    Parameterization: r = 1 / alpha, p = 1 / (1 + alpha * mu).
    """

    def __init__(self, l2_reg: float = 0.01):
        self.l2_reg = l2_reg
        self.coef: np.ndarray = np.array([])
        self.alpha: float = 0.1  # Dispersion parameter

    def fit(self, X: np.ndarray, y: np.ndarray) -> "NegativeBinomialCountRegressor":
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)
        n_samples, n_features = X.shape

        # Objective: Negative log-likelihood of NB2
        def loss(params):
            beta = params[:n_features]
            log_alpha = params[n_features]
            alpha = np.exp(log_alpha)
            r = 1.0 / alpha

            mu = np.exp(np.clip(X @ beta, -10.0, 10.0))
            p = r / (r + mu)

            # Log-likelihood of Negative Binomial
            ll = (
                gammaln(y + r)
                - gammaln(r)
                - gammaln(y + 1.0)
                + r * np.log(np.clip(p, 1e-12, 1.0))
                + y * np.log(np.clip(1.0 - p, 1e-12, 1.0))
            )
            nll = -np.sum(ll) + 0.5 * self.l2_reg * np.sum(beta ** 2)
            return nll

        init_params = np.zeros(n_features + 1)
        init_params[n_features] = np.log(0.1)  # Initial log alpha
        # Initialize intercept to log mean of y
        mean_y = max(np.mean(y), 1.0)
        init_params[0] = np.log(mean_y)

        res = minimize(loss, init_params, method="L-BFGS-B")
        if res.success:
            self.coef = res.x[:n_features]
            self.alpha = float(np.exp(res.x[n_features]))
        else:
            self.coef = np.zeros(n_features)
            self.coef[0] = np.log(mean_y)
            self.alpha = 0.1

        return self

    def predict_mean(self, X: np.ndarray) -> np.ndarray:
        X = np.asarray(X, dtype=float)
        return np.exp(np.clip(X @ self.coef, -10.0, 10.0))

    def predict_pmf(self, x_single: np.ndarray, max_count: int = 30) -> np.ndarray:
        """Produce discrete count PMF for a single feature vector."""
        mu = float(self.predict_mean(x_single.reshape(1, -1))[0])
        r = 1.0 / max(self.alpha, 1e-6)
        p = r / (r + mu)

        counts = np.arange(max_count + 1)
        pmf = nbinom.pmf(counts, r, p)
        pmf /= np.sum(pmf)
        return pmf


class StudentTJointScoreModel:
    """Bivariate Student-t joint score model capturing heavier tail margins and correlation.
    
    Parameters:
    - mu_h, mu_a: Marginal location parameters
    - sigma_h, sigma_a: Scale parameters
    - rho: Correlation between home and away scores
    - df: Degrees of freedom (nu > 2 ensures finite variance; lower nu yields heavier tails)
    """

    def __init__(self, df: float = 5.0):
        if df <= 2.0:
            raise ValueError("Degrees of freedom df must be > 2 for finite variance")
        self.df = df

    def generate_distribution(
        self,
        mu_h: float,
        mu_a: float,
        sigma_h: float,
        sigma_a: float,
        rho: float,
        min_score: int,
        max_score: int
    ) -> ScoreDistribution:
        """Discretize bivariate Student-t density over support [0, max_score]."""
        scores = np.arange(min_score, max_score + 1)
        H, A = np.meshgrid(scores, scores, indexing="ij")

        # Standardized residuals
        z_h = (H - mu_h) / sigma_h
        z_a = (A - mu_a) / sigma_a

        # Quadratic form
        inv_det = 1.0 / (1.0 - rho ** 2)
        q = (z_h ** 2 - 2.0 * rho * z_h * z_a + z_a ** 2) * inv_det

        # Bivariate Student-t PDF:
        # f(x, y) = [1 / (2*pi*sigma_h*sigma_a*sqrt(1-rho^2))] * [1 + q/nu]^(-(nu+2)/2)
        nu = self.df
        norm_const = 1.0 / (2.0 * np.pi * sigma_h * sigma_a * np.sqrt(1.0 - rho ** 2))
        kernel = (1.0 + q / nu) ** (-0.5 * (nu + 2.0))
        pdf = norm_const * kernel

        # Normalize
        total_mass = np.sum(pdf)
        if total_mass > 0:
            pdf /= total_mass

        # Embed into full matrix [0, max_score]
        full_grid = np.zeros((max_score + 1, max_score + 1), dtype=float)
        full_grid[min_score:max_score + 1, min_score:max_score + 1] = pdf

        return ScoreDistribution(
            grid=full_grid,
            home_support=np.arange(max_score + 1),
            away_support=np.arange(max_score + 1)
        )


class QuantileDistributionReconstructor:
    """Validates and sorts estimated quantiles to prevent quantile crossing and reconstructs CDF/PMF.
    
    Implements rearrangement (Chernozhukov, Fernández-Val, Galichon 2010).
    """

    def __init__(self, quantiles: List[float]):
        self.quantiles = np.array(sorted(quantiles))

    def fix_crossing(self, predicted_quantiles: np.ndarray) -> np.ndarray:
        """Ensure monotonic non-decreasing quantiles for each sample."""
        # predicted_quantiles: shape (n_samples, n_quantiles)
        rearranged = np.sort(predicted_quantiles, axis=-1)
        return rearranged

    def to_probabilities_above(self, predicted_quantiles: np.ndarray, threshold: float) -> float:
        """Estimate P(Y > threshold) via linear interpolation across monotonically sorted quantiles."""
        q_vals = np.sort(predicted_quantiles)
        # If threshold < min quantile, P > threshold is >= (1 - min_tau)
        if threshold <= q_vals[0]:
            return 1.0 - self.quantiles[0]
        if threshold >= q_vals[-1]:
            return 1.0 - self.quantiles[-1]

        # Interpolate percentile of threshold
        pct = float(np.interp(threshold, q_vals, self.quantiles))
        return float(np.clip(1.0 - pct, 0.0, 1.0))
