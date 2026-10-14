"""Joint score distributions on the integer lattice, and every contract priced from one of them.

A ``ScoreGrid`` holds P(H = h, A = a) for h in [h0, h0 + nh) and a in [a0, a0 + na).
Winner, handicap and total probabilities are deterministic functions of the grid,
so they are coherent by construction (CURRENT_RULES §7, Rule P4).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import stats

MASS_TOL = 1e-9


class CoherenceError(ValueError):
    """Raised when a grid or a priced contract breaks a coherence invariant."""


@dataclass(frozen=True)
class Masses:
    """Unconditional WIN/PUSH/LOSS masses of one contract (void is not modelled)."""

    win: float
    push: float
    loss: float

    @property
    def p_decisive(self) -> float | None:
        d = self.win + self.loss
        return None if d <= 0 else self.win / d


class ScoreGrid:
    def __init__(self, p: np.ndarray, h0: int = 0, a0: int = 0, check: bool = True):
        p = np.asarray(p, dtype=float)
        if p.ndim != 2:
            raise CoherenceError("grid must be two-dimensional")
        if p.size == 0 or any(not np.isfinite(x) or x != int(x) for x in (h0, a0)):
            raise CoherenceError("nonempty grid and integer support origins required")
        self.p = p.copy()
        self.h0 = int(h0)
        self.a0 = int(a0)
        if check:
            self.check()

    # ------------------------------------------------------------------ construction
    @classmethod
    def independent(cls, ph: np.ndarray, pa: np.ndarray, h0: int = 0, a0: int = 0) -> "ScoreGrid":
        for marginal in (ph, pa):
            marginal = np.asarray(marginal, float)
            if marginal.ndim != 1 or marginal.size == 0 or not np.isfinite(marginal).all() or np.any(marginal < 0) or marginal.sum() <= 0:
                raise CoherenceError("marginals must have finite nonnegative positive mass")
        g = np.outer(ph, pa)
        return cls(g / g.sum(), h0, a0)

    @staticmethod
    def rho_domain(lam_h: float, lam_a: float) -> tuple[float, float]:
        """Dixon & Coles (1997): tau > 0 on all four cells iff max(-1/lam_h, -1/lam_a) < rho < min(1/(lam_h lam_a), 1)."""
        return max(-1.0 / lam_h, -1.0 / lam_a), min(1.0 / (lam_h * lam_a), 1.0)

    @classmethod
    def poisson(cls, lam_h: float, lam_a: float, rho: float = 0.0, max_goals: int | None = None,
                clamp_rho: bool = False) -> "ScoreGrid":
        """Poisson grid with the Dixon–Coles low-score correction tau(rho).

        With ``clamp_rho`` a rho outside the pair's valid domain is moved to 99% of the nearest bound (the model is
        undefined outside it); the caller records the flag RHO_CLAMPED. Without it, an invalid rho raises.
        """
        if not all(np.isfinite(v) for v in (lam_h, lam_a, rho)) or lam_h <= 0 or lam_a <= 0:
            raise CoherenceError("Poisson means must be positive")
        if max_goals is not None and (not np.isfinite(max_goals) or max_goals != int(max_goals) or max_goals < 1):
            raise CoherenceError("Poisson support maximum must be a positive integer")
        lo, hi = cls.rho_domain(lam_h, lam_a)
        if clamp_rho and not (lo < rho < hi):
            rho = 0.99 * (lo if rho <= lo else hi)
        if max_goals is None:
            max_goals = int(max(10, np.ceil(max(lam_h, lam_a) + 8 * np.sqrt(max(lam_h, lam_a)))))
        k = np.arange(max_goals + 1)
        g = np.outer(stats.poisson.pmf(k, lam_h), stats.poisson.pmf(k, lam_a))
        if rho != 0.0:
            tau = np.ones((2, 2))
            tau[0, 0] = 1 - lam_h * lam_a * rho
            tau[0, 1] = 1 + lam_h * rho
            tau[1, 0] = 1 + lam_a * rho
            tau[1, 1] = 1 - rho
            if np.any(tau <= 0):
                raise CoherenceError("Dixon–Coles tau is not positive for these parameters")
            g[:2, :2] *= tau
        return cls(g / g.sum())

    @classmethod
    def negbin(cls, mu_h: float, mu_a: float, phi: float, max_runs: int | None = None) -> "ScoreGrid":
        """Independent negative-binomial scores with Var = mu + phi * mu^2 (phi = 0 gives Poisson)."""
        if not all(np.isfinite(v) for v in (mu_h, mu_a, phi)) or min(mu_h, mu_a) <= 0 or phi < 0:
            raise CoherenceError("negative-binomial means must be positive and dispersion nonnegative")
        if max_runs is not None and (not np.isfinite(max_runs) or max_runs != int(max_runs) or max_runs < 1):
            raise CoherenceError("negative-binomial support maximum must be a positive integer")
        if phi <= 1e-9:
            return cls.poisson(mu_h, mu_a, 0.0, max_runs)
        if max_runs is None:
            m = max(mu_h, mu_a)
            max_runs = int(np.ceil(m + 10 * np.sqrt(m + phi * m * m)))
        k = np.arange(max_runs + 1)
        n = 1.0 / phi

        def pmf(mu: float) -> np.ndarray:
            return stats.nbinom.pmf(k, n, n / (n + mu))

        return cls.independent(pmf(mu_h), pmf(mu_a))

    @classmethod
    def bivariate_normal(cls, mean_h: float, mean_a: float, cov: np.ndarray, n_sd: float = 6.5) -> "ScoreGrid":
        """Discretised bivariate normal on non-negative integers (density at lattice points, renormalised)."""
        cov = np.asarray(cov, dtype=float)
        if cov.shape != (2, 2) or not np.isfinite(cov).all() or not np.allclose(cov, cov.T) or np.linalg.eigvalsh(cov).min() <= 0:
            raise CoherenceError("score covariance must be finite, symmetric and positive definite")
        if not all(np.isfinite(v) for v in (mean_h, mean_a, n_sd)) or n_sd <= 0:
            raise CoherenceError("finite means and positive support width required")
        sh, sa = np.sqrt(cov[0, 0]), np.sqrt(cov[1, 1])
        if not (sh > 0 and sa > 0):
            raise CoherenceError("score standard deviations must be positive")
        h_lo = max(0, int(np.floor(mean_h - n_sd * sh)))
        h_hi = int(np.ceil(mean_h + n_sd * sh))
        a_lo = max(0, int(np.floor(mean_a - n_sd * sa)))
        a_hi = int(np.ceil(mean_a + n_sd * sa))
        hh, aa = np.meshgrid(np.arange(h_lo, h_hi + 1), np.arange(a_lo, a_hi + 1), indexing="ij")
        pts = np.stack([hh.ravel(), aa.ravel()], axis=1)
        dens = stats.multivariate_normal(mean=[mean_h, mean_a], cov=cov, allow_singular=False).pdf(pts)
        g = dens.reshape(hh.shape)
        return cls(g / g.sum(), h_lo, a_lo)

    # ------------------------------------------------------------------ invariants
    def check(self) -> None:
        if np.any(~np.isfinite(self.p)):
            raise CoherenceError("non-finite mass")
        if np.any(self.p < -1e-15):
            raise CoherenceError("negative mass")
        s = self.p.sum()
        if abs(s - 1.0) > 1e-7:
            raise CoherenceError(f"masses sum to {s!r}, not 1")
        if self.h0 < 0 or self.a0 < 0:
            raise CoherenceError("negative score support")

    # ------------------------------------------------------------------ marginals
    def _hv(self) -> np.ndarray:
        return np.arange(self.h0, self.h0 + self.p.shape[0])

    def _av(self) -> np.ndarray:
        return np.arange(self.a0, self.a0 + self.p.shape[1])

    def margin_pmf(self) -> tuple[np.ndarray, np.ndarray]:
        """Support and mass of M = H - A."""
        hv, av = self._hv(), self._av()
        m = hv[:, None] - av[None, :]
        lo = int(m.min())
        out = np.zeros(int(m.max()) - lo + 1)
        np.add.at(out, (m - lo).ravel(), self.p.ravel())
        return np.arange(lo, lo + out.size), out

    def total_pmf(self) -> tuple[np.ndarray, np.ndarray]:
        hv, av = self._hv(), self._av()
        t = hv[:, None] + av[None, :]
        lo = int(t.min())
        out = np.zeros(int(t.max()) - lo + 1)
        np.add.at(out, (t - lo).ravel(), self.p.ravel())
        return np.arange(lo, lo + out.size), out

    def means(self) -> tuple[float, float]:
        ph = self.p.sum(axis=1)
        pa = self.p.sum(axis=0)
        return float(ph @ self._hv()), float(pa @ self._av())

    def summary(self) -> dict:
        hv, av = self._hv(), self._av()
        mh, ma = self.means()
        vh = float(self.p.sum(axis=1) @ (hv - mh) ** 2)
        va = float(self.p.sum(axis=0) @ (av - ma) ** 2)
        cov = float(((hv[:, None] - mh) * (av[None, :] - ma) * self.p).sum())
        return {
            "mean_home": mh,
            "mean_away": ma,
            "sd_margin": float(np.sqrt(max(vh + va - 2 * cov, 0.0))),
            "sd_total": float(np.sqrt(max(vh + va + 2 * cov, 0.0))),
            "cov_home_away": cov,
        }

    # ------------------------------------------------------------------ contracts
    def winner(self) -> tuple[float, float, float]:
        """(P(home wins), P(draw), P(away wins)) at this grid's endpoint."""
        hv, av = self._hv(), self._av()
        m = hv[:, None] - av[None, :]
        return float(self.p[m > 0].sum()), float(self.p[m == 0].sum()), float(self.p[m < 0].sum())

    def handicap(self, line: float, side: str = "HOME") -> Masses:
        """Home (or away) with handicap ``line`` added to its score: win if score + line beats the other."""
        if side not in ("HOME", "AWAY") or not np.isfinite(line):
            raise CoherenceError("handicap requires HOME/AWAY and a finite line")
        mv, mp = self.margin_pmf()
        x = mv + line if side == "HOME" else -mv + line
        return Masses(float(mp[x > 0].sum()), float(mp[x == 0].sum()), float(mp[x < 0].sum()))

    def total(self, line: float, side: str = "OVER") -> Masses:
        if side not in ("OVER", "UNDER") or not np.isfinite(line):
            raise CoherenceError("total requires OVER/UNDER and a finite line")
        tv, tp = self.total_pmf()
        x = tv - line if side == "OVER" else line - tv
        return Masses(float(tp[x > 0].sum()), float(tp[x == 0].sum()), float(tp[x < 0].sum()))

    # ------------------------------------------------------------------ tie resolution
    def resolve_ties(self, p_home_extra: float, residual_draw: float = 0.0, winner_bonus: int = 1,
                     both_bonus: int = 0) -> "ScoreGrid":
        """Move tied regulation mass into an extra-time branch.

        Each tied state (k, k) keeps ``residual_draw`` of its mass as a draw at (k + both_bonus, k + both_bonus);
        the rest goes to (k + both_bonus + winner_bonus, k + both_bonus) with probability ``p_home_extra``
        or the mirror state otherwise. Mass is conserved exactly.
        """
        if not 0 <= p_home_extra <= 1 or not 0 <= residual_draw <= 1:
            raise CoherenceError("extra-time probabilities must lie in [0, 1]")
        if any(not np.isfinite(x) or x != int(x) or x < 0 for x in (winner_bonus, both_bonus)) or winner_bonus == 0:
            raise CoherenceError("extra-time bonuses must be nonnegative integers with a positive winner bonus")
        winner_bonus, both_bonus = int(winner_bonus), int(both_bonus)
        hv, av = self._hv(), self._av()
        pad = winner_bonus + both_bonus
        nh, na = self.p.shape[0] + pad, self.p.shape[1] + pad
        g = np.zeros((nh, na))
        g[: self.p.shape[0], : self.p.shape[1]] = self.p
        for i, h in enumerate(hv):
            j = h - self.a0
            if 0 <= j < self.p.shape[1]:
                m = self.p[i, j]
                if m == 0:
                    continue
                g[i, j] -= m  # Retain incoming shifted mass from earlier original tied states.
                base_i, base_j = i + both_bonus, j + both_bonus
                g[base_i, base_j] += m * residual_draw
                g[base_i + winner_bonus, base_j] += m * (1 - residual_draw) * p_home_extra
                g[base_i, base_j + winner_bonus] += m * (1 - residual_draw) * (1 - p_home_extra)
        return ScoreGrid(g, self.h0, self.a0)

    def reweight_winner(self, target: tuple[float, float, float]) -> "ScoreGrid":
        """Coherent calibration: rescale every state inside each winner class to the target class mass."""
        cur = self.winner()
        if len(target) != 3 or not all(np.isfinite(t) and t >= 0 for t in target):
            raise CoherenceError("three finite nonnegative target winner masses required")
        if any(t > 0 and c <= 0 for t, c in zip(target, cur)):
            raise CoherenceError("cannot give mass to a winner class with zero support")
        if abs(sum(target) - 1) > 1e-9:
            raise CoherenceError("target winner masses must sum to 1")
        hv, av = self._hv(), self._av()
        m = hv[:, None] - av[None, :]
        g = self.p.copy()
        for cls_mask, c, t in ((m > 0, cur[0], target[0]), (m == 0, cur[1], target[1]), (m < 0, cur[2], target[2])):
            if c > 0:
                g[cls_mask] *= t / c
        return ScoreGrid(g / g.sum(), self.h0, self.a0)

    # ------------------------------------------------------------------ scoring
    def crps_margin(self, observed: int) -> float:
        return discrete_crps(*self.margin_pmf(), observed)

    def crps_total(self, observed: int) -> float:
        return discrete_crps(*self.total_pmf(), observed)


def discrete_crps(support: np.ndarray, mass: np.ndarray, y: float) -> float:
    """CRPS of a distribution on consecutive integers: sum_t (F(t) - 1{y <= t})^2."""
    lo = int(min(support[0], np.floor(y)))
    hi = int(max(support[-1], np.ceil(y)))
    full = np.zeros(hi - lo + 1)
    full[support[0] - lo: support[0] - lo + mass.size] = mass
    cdf = np.cumsum(full)
    t = np.arange(lo, hi + 1)
    return float(np.sum((cdf - (t >= y)) ** 2))


def normal_crps(mu: float | np.ndarray, sigma: float | np.ndarray, y: float | np.ndarray) -> np.ndarray:
    """Closed-form CRPS of N(mu, sigma^2) (Gneiting & Raftery 2007)."""
    z = (np.asarray(y) - mu) / sigma
    return sigma * (z * (2 * stats.norm.cdf(z) - 1) + 2 * stats.norm.pdf(z) - 1 / np.sqrt(np.pi))
