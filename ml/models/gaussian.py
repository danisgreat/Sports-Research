"""Joint-normal team ratings for high-scoring sports (basketball, AFL, NFL, NRL).

Model, for a game between home team h and away team a:
    home score = mu_home + att[h] + dfn[a] + e1
    away score = mu_away + att[a] + dfn[h] + e2,   (e1, e2) ~ N(0, Sigma)
fitted by time-decayed weighted ridge least squares (ridge pulls att/dfn towards a prior centre, 0 by default).
Sigma is the weighted covariance of the residuals, multiplied by a tuned inflation factor because in-sample
residuals understate out-of-sample spread. Prices come from the discretised joint on the integer lattice.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy import stats

from ml.config import League
from ml.core.distributions import ScoreGrid
from ml.models.common import FitError, apply_tie_rule, decay_weights, normal_extra, residual_draw_share


@dataclass(frozen=True)
class GaussParams:
    half_life_days: float
    ridge: float
    cov_inflation: float
    key_numbers: bool = False   # NFL only: margin reweighting towards observed key-number frequencies
    key_pseudo: float = 20.0


class GaussianRatings:
    name = "JOINT_NORMAL"

    def __init__(self, lg: League, params: GaussParams):
        self.lg = lg
        self.p = params
        self.fitted = False

    def fit(self, train: pd.DataFrame, as_of: pd.Timestamp) -> "GaussianRatings":
        if len(train) < 30:
            raise FitError(f"only {len(train)} training games")
        w = decay_weights(train["date"], as_of, self.p.half_life_days)
        teams = sorted(set(train["home"]) | set(train["away"]))
        idx = {t: i for i, t in enumerate(teams)}
        T = len(teams)
        hi = train["home"].map(idx).to_numpy()
        ai = train["away"].map(idx).to_numpy()
        n = len(train)
        P = 2 + 2 * T
        X = np.zeros((2 * n, P))
        r = np.arange(n)
        X[r, 0] = 1.0
        X[r, 2 + hi] = 1.0
        X[r, 2 + T + ai] = 1.0
        X[n + r, 1] = 1.0
        X[n + r, 2 + ai] = 1.0
        X[n + r, 2 + T + hi] = 1.0
        y = np.concatenate([train["hs"].to_numpy(float), train["as_"].to_numpy(float)])
        ww = np.concatenate([w, w])
        lam = np.zeros(P)
        lam[2:] = self.p.ridge
        A = X.T @ (X * ww[:, None]) + np.diag(lam)
        b = X.T @ (ww * y)
        try:
            beta = np.linalg.solve(A, b)
        except np.linalg.LinAlgError as e:
            raise FitError(f"normal equations singular: {e}") from e
        if not np.all(np.isfinite(beta)):
            raise FitError("non-finite coefficients")
        res = y - X @ beta
        e1, e2 = res[:n], res[n:]
        sw = w.sum()
        m1, m2 = (w * e1).sum() / sw, (w * e2).sum() / sw
        c11 = (w * (e1 - m1) ** 2).sum() / sw
        c22 = (w * (e2 - m2) ** 2).sum() / sw
        c12 = (w * (e1 - m1) * (e2 - m2)).sum() / sw
        cov = np.array([[c11, c12], [c12, c22]]) * self.p.cov_inflation
        if np.linalg.det(cov) <= 0:
            raise FitError("residual covariance not positive definite")
        self.teams, self.idx, self.T = teams, idx, T
        self.mu_h, self.mu_a = beta[0], beta[1]
        self.att, self.dfn = beta[2:2 + T], beta[2 + T:]
        self.cov = cov
        self.sd_margin = float(np.sqrt(c11 + c22 - 2 * c12) * np.sqrt(self.p.cov_inflation))
        self.residual_draw = residual_draw_share(train, self.sd_margin)
        self.n_train = n
        self.as_of = as_of
        if self.p.key_numbers:
            self._fit_key_numbers(train, X[:n] @ beta - X[n:] @ beta)
        self.fitted = True
        return self

    # NFL key numbers --------------------------------------------------------------------------------------
    def _fit_key_numbers(self, train: pd.DataFrame, mu_margin: np.ndarray, max_abs: int = 21) -> None:
        """Factor w(|m|) = (observed + kappa) / (predicted + kappa) over |m| <= max_abs, from the training fit."""
        ms = np.arange(-max_abs, max_abs + 1)
        dens = stats.norm.pdf((ms[None, :] - mu_margin[:, None]) / self.sd_margin) / self.sd_margin
        pred = np.zeros(max_abs + 1)
        obs = np.zeros(max_abs + 1)
        np.add.at(pred, np.abs(ms), dens.sum(axis=0))
        actual = (train["hs"] - train["as_"]).abs().to_numpy()
        for v in actual[actual <= max_abs]:
            obs[int(v)] += 1
        k = self.p.key_pseudo
        self.key_w = (obs + k) / (pred + k)

    def _apply_key_numbers(self, g: ScoreGrid) -> ScoreGrid:
        hv = np.arange(g.h0, g.h0 + g.p.shape[0])
        av = np.arange(g.a0, g.a0 + g.p.shape[1])
        m = np.abs(hv[:, None] - av[None, :])
        f = np.ones_like(g.p)
        inside = m < self.key_w.size
        f[inside] = self.key_w[m[inside]]
        q = g.p * f
        return ScoreGrid(q / q.sum(), g.h0, g.a0)

    # prediction ---------------------------------------------------------------------------------------------
    def means(self, home: str, away: str) -> tuple[float, float, list[str]]:
        flags = []
        h = self.idx.get(home)
        a = self.idx.get(away)
        if h is None:
            flags.append(f"NEW_TEAM_PRIOR:{home}")
        if a is None:
            flags.append(f"NEW_TEAM_PRIOR:{away}")
        att_h = self.att[h] if h is not None else 0.0
        att_a = self.att[a] if a is not None else 0.0
        dfn_h = self.dfn[h] if h is not None else 0.0
        dfn_a = self.dfn[a] if a is not None else 0.0
        return float(self.mu_h + att_h + dfn_a), float(self.mu_a + att_a + dfn_h), flags

    def fast(self, home: str, away: str) -> dict:
        """Closed-form normal summaries, used for tuning only (no lattice, no tie branch)."""
        mh, ma, _ = self.means(home, away)
        c = self.cov
        return {"mu_m": mh - ma, "sd_m": float(np.sqrt(c[0, 0] + c[1, 1] - 2 * c[0, 1])),
                "mu_t": mh + ma, "sd_t": float(np.sqrt(c[0, 0] + c[1, 1] + 2 * c[0, 1]))}

    def grid(self, home: str, away: str) -> tuple[ScoreGrid, list[str]]:
        if not self.fitted:
            raise FitError("model not fitted")
        mh, ma, flags = self.means(home, away)
        mh, ma = max(mh, 0.5), max(ma, 0.5)
        g = ScoreGrid.bivariate_normal(mh, ma, self.cov)
        if self.p.key_numbers:
            g = self._apply_key_numbers(g)
        extra = normal_extra(self.lg, mh - ma, self.sd_margin, mh + ma, self.residual_draw)
        return apply_tie_rule(g, self.lg, extra), flags

    def parameter_table(self) -> pd.DataFrame:
        return pd.DataFrame({"team": self.teams, "attack": self.att, "defence": self.dfn,
                             "net_margin_vs_average": self.att - self.dfn}).sort_values(
            "net_margin_vs_average", ascending=False)
