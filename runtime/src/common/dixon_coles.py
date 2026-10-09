"""Dixon-Coles Poisson regression with time decay and low-score dependency (vectorised).

The likelihood and its analytic gradient are computed with array operations, so a season of
league football fits in well under a second (ML-04). A fit that does not converge raises
`FitFailed` instead of leaving a flat model that looks valid (ML-02), and an unknown team is
refused unless the caller opts into a league-average stand-in, which is recorded in the
distribution's metadata (DST-13).
"""

from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln
from scipy.stats import poisson

from .contracts import ScoreDistribution
from .errors import FitFailed, InsufficientData, NotFitted, UnknownTeam, require_converged

TAU_FLOOR = 1e-6


class DixonColesEngine:
    """Dixon & Coles (1997) model for association football.

    Estimates team attack alpha_i and defence beta_j, home advantage gamma, the low-score
    dependence rho, with exponential time decay exp(-xi * days_ago).
    """

    def __init__(self, xi: float = 0.002, l2_reg: float = 0.05, unknown_team: str = "refuse", min_matches: int = 3):
        if unknown_team not in ("refuse", "league_average"):
            raise ValueError("unknown_team must be 'refuse' or 'league_average'")
        self.xi = xi                      # daily decay rate; 0.002 is a half-life of about 346 days
        self.l2_reg = l2_reg
        self.unknown_team = unknown_team
        self.min_matches = min_matches   # tiny samples are fitted but strongly shrunk by the ridge
        self.teams: List[str] = []
        self.team_idx: Dict[str, int] = {}
        self.attacks: np.ndarray = np.array([])
        self.defences: np.ndarray = np.array([])
        self.home_adv: float = 0.0
        self.rho: float = 0.0
        self.converged: bool = False

    # ------------------------------------------------------------------ pieces
    @staticmethod
    def tau(x: int, y: int, lambda_h: float, mu_a: float, rho: float) -> float:
        """Dixon-Coles low-score dependency factor."""
        if x == 0 and y == 0:
            return 1.0 - lambda_h * mu_a * rho
        elif x == 0 and y == 1:
            return 1.0 + lambda_h * rho
        elif x == 1 and y == 0:
            return 1.0 + mu_a * rho
        elif x == 1 and y == 1:
            return 1.0 - rho
        return 1.0

    @staticmethod
    def _prepare(matches: Sequence[Dict[str, Any]], team_idx: Dict[str, int]):
        hi = np.array([team_idx[m["home"]] for m in matches], dtype=int)
        ai = np.array([team_idx[m["away"]] for m in matches], dtype=int)
        hg = np.array([int(m["home_goals"]) for m in matches], dtype=float)
        ag = np.array([int(m["away_goals"]) for m in matches], dtype=float)
        days = np.array([float(m.get("days_ago", 0.0)) for m in matches], dtype=float)
        return hi, ai, hg, ag, days

    def _objective(self, params, n, hi, ai, hg, ag, w):
        alphas, betas = params[:n], params[n:2 * n]
        gamma, rho = params[2 * n], params[2 * n + 1]
        eta_h = alphas[hi] + betas[ai] + gamma
        eta_a = alphas[ai] + betas[hi]
        lam, mu = np.exp(eta_h), np.exp(eta_a)
        # low-score factor and its derivatives with respect to log lambda, log mu and rho
        tau = np.ones_like(lam)
        d_tau_dlam = np.zeros_like(lam)       # d tau / d log(lambda)
        d_tau_dmu = np.zeros_like(lam)        # d tau / d log(mu)
        d_tau_drho = np.zeros_like(lam)
        m00 = (hg == 0) & (ag == 0)
        m01 = (hg == 0) & (ag == 1)
        m10 = (hg == 1) & (ag == 0)
        m11 = (hg == 1) & (ag == 1)
        tau[m00] = 1.0 - lam[m00] * mu[m00] * rho
        d_tau_dlam[m00] = -lam[m00] * mu[m00] * rho
        d_tau_dmu[m00] = -lam[m00] * mu[m00] * rho
        d_tau_drho[m00] = -lam[m00] * mu[m00]
        tau[m01] = 1.0 + lam[m01] * rho
        d_tau_dlam[m01] = lam[m01] * rho
        d_tau_drho[m01] = lam[m01]
        tau[m10] = 1.0 + mu[m10] * rho
        d_tau_dmu[m10] = mu[m10] * rho
        d_tau_drho[m10] = mu[m10]
        tau[m11] = 1.0 - rho
        d_tau_drho[m11] = -1.0
        safe = tau > TAU_FLOOR
        tau_c = np.where(safe, tau, TAU_FLOOR)
        log_tau = np.log(tau_c)
        inv_tau = np.where(safe, 1.0 / tau_c, 0.0)
        ll = w * (log_tau + hg * eta_h - lam + ag * eta_a - mu - gammaln(hg + 1.0) - gammaln(ag + 1.0))
        nll = -np.sum(ll)
        s_alpha = np.sum(alphas)
        nll += 100.0 * s_alpha ** 2 + 0.5 * self.l2_reg * (np.sum(alphas ** 2) + np.sum(betas ** 2)) \
            + 0.5 * self.l2_reg * (gamma ** 2 + rho ** 2)
        # gradient
        g_lam = w * (hg - lam + d_tau_dlam * inv_tau)       # d ll / d eta_h
        g_mu = w * (ag - mu + d_tau_dmu * inv_tau)          # d ll / d eta_a
        grad_alpha = np.bincount(hi, weights=g_lam, minlength=n) + np.bincount(ai, weights=g_mu, minlength=n)
        grad_beta = np.bincount(ai, weights=g_lam, minlength=n) + np.bincount(hi, weights=g_mu, minlength=n)
        grad = np.empty_like(params)
        grad[:n] = -grad_alpha + 200.0 * s_alpha + self.l2_reg * alphas
        grad[n:2 * n] = -grad_beta + self.l2_reg * betas
        grad[2 * n] = -np.sum(g_lam) + self.l2_reg * gamma
        grad[2 * n + 1] = -np.sum(w * d_tau_drho * inv_tau) + self.l2_reg * rho
        return nll, grad

    def _minimise(self, matches: Sequence[Dict[str, Any]], team_idx: Dict[str, int], xi: float):
        n = len(team_idx)
        hi, ai, hg, ag, days = self._prepare(matches, team_idx)
        w = np.exp(-xi * days)
        x0 = np.zeros(2 * n + 2)
        x0[2 * n] = 0.25
        x0[2 * n + 1] = -0.04
        bounds = [(-3.0, 3.0)] * (2 * n) + [(0.0, 1.5)] + [(-0.25, 0.25)]
        res = minimize(self._objective, x0, args=(n, hi, ai, hg, ag, w), jac=True, method="L-BFGS-B", bounds=bounds,
                       options={"maxiter": 1000})
        require_converged(res, "DixonColesEngine", grad_tol=1e-3 * max(1.0, float(np.sum(w))))
        return res.x, (hi, ai, hg, ag)

    # ----------------------------------------------------------------- fitting
    def fit(self, matches: List[Dict[str, Any]], current_time_days: Optional[float] = None) -> "DixonColesEngine":
        """Fit by weighted maximum likelihood. Raises `FitFailed` if the optimiser does not converge.

        matches: [{"home": "Arsenal", "away": "Chelsea", "home_goals": 2, "away_goals": 1, "days_ago": 14.0}]
        """
        if len(matches) < self.min_matches:
            raise InsufficientData(f"Dixon-Coles needs at least {self.min_matches} matches, got {len(matches)}")
        teams = sorted({m["home"] for m in matches} | {m["away"] for m in matches})
        if len(teams) < 2:
            raise InsufficientData("Dixon-Coles needs at least two teams")
        team_idx = {t: i for i, t in enumerate(teams)}
        params, (hi, ai, hg, ag) = self._minimise(matches, team_idx, self.xi)
        n = len(teams)
        alphas, betas = params[:n], params[n:2 * n]
        gamma, rho = float(params[2 * n]), float(np.clip(params[2 * n + 1], -0.25, 0.25))
        lam, mu = np.exp(alphas[hi] + betas[ai] + gamma), np.exp(alphas[ai] + betas[hi])
        for goals, tau in ((((hg == 0) & (ag == 0)), 1.0 - lam * mu * rho), (((hg == 0) & (ag == 1)), 1.0 + lam * rho),
                           (((hg == 1) & (ag == 0)), 1.0 + mu * rho), (((hg == 1) & (ag == 1)), np.full_like(lam, 1.0 - rho))):
            if np.any(tau[goals] <= 0.0):
                raise FitFailed("DixonColesEngine", "fitted low-score factor is non-positive for an observed match")
        self.teams, self.team_idx = teams, team_idx
        self.attacks, self.defences, self.home_adv, self.rho = alphas.copy(), betas.copy(), gamma, rho
        self.converged = True
        return self

    def tune_xi(self, matches: List[Dict[str, Any]], xis: Sequence[float] = (0.0, 0.0005, 0.001, 0.002, 0.004, 0.008),
                folds: int = 4, min_train: int = 60) -> Tuple[float, Dict[float, float]]:
        """Choose the decay rate by rolling-origin log loss on the 1X2 result; sets and returns the best xi.

        Matches are ordered by decreasing `days_ago` (oldest first); each fold trains on the earlier
        matches, weights them relative to the fold's own origin, and scores the next block.
        """
        ordered = sorted(matches, key=lambda m: -float(m.get("days_ago", 0.0)))
        n = len(ordered)
        if n < min_train + folds:
            raise InsufficientData(f"tune_xi needs at least {min_train + folds} matches")
        cuts = [int(round(min_train + (n - min_train) * k / folds)) for k in range(folds + 1)]
        scores: Dict[float, float] = {}
        for xi in xis:
            total, used = 0.0, 0
            for k in range(folds):
                train, test = ordered[:cuts[k]], ordered[cuts[k]:cuts[k + 1]]
                if not test:
                    continue
                origin = min(float(m.get("days_ago", 0.0)) for m in train)
                rebased = [{**m, "days_ago": float(m.get("days_ago", 0.0)) - origin} for m in train]
                teams = sorted({m["home"] for m in train} | {m["away"] for m in train})
                try:
                    candidate = DixonColesEngine(xi=xi, l2_reg=self.l2_reg).fit(rebased)
                except FitFailed:
                    total += 1e6
                    continue
                for m in test:
                    if m["home"] not in teams or m["away"] not in teams:
                        continue
                    dist = candidate.predict_score_distribution(m["home"], m["away"])
                    probs = {"h": dist.p_home_win(), "d": dist.p_draw(), "a": dist.p_away_win()}
                    outcome = "h" if m["home_goals"] > m["away_goals"] else "a" if m["home_goals"] < m["away_goals"] else "d"
                    total += -float(np.log(max(probs[outcome], 1e-12)))
                    used += 1
            scores[float(xi)] = total / used if used else float("inf")
        best = min(scores, key=lambda x: scores[x])
        self.xi = best
        return best, scores

    # -------------------------------------------------------------- prediction
    def knows(self, team: str) -> bool:
        return team in self.team_idx

    def _rates(self, home_team: str, away_team: str):
        warnings: List[str] = []
        idx_h, idx_a = self.team_idx.get(home_team), self.team_idx.get(away_team)
        if (idx_h is None or idx_a is None) and self.unknown_team != "league_average":
            missing = [t for t, i in ((home_team, idx_h), (away_team, idx_a)) if i is None]
            raise UnknownTeam(f"no fitted strength for {missing}; set unknown_team='league_average' to accept a stand-in")
        if idx_h is None and idx_a is None and not len(self.attacks):
            raise NotFitted("DixonColesEngine.predict called before fit")
        mean_att, mean_def = (float(np.mean(self.attacks)), float(np.mean(self.defences))) if len(self.attacks) else (0.0, 0.0)
        att_h = self.attacks[idx_h] if idx_h is not None else mean_att
        def_h = self.defences[idx_h] if idx_h is not None else mean_def
        att_a = self.attacks[idx_a] if idx_a is not None else mean_att
        def_a = self.defences[idx_a] if idx_a is not None else mean_def
        for team, idx in ((home_team, idx_h), (away_team, idx_a)):
            if idx is None:
                warnings.append(f"unknown team {team!r}: league-average strength used; uncertainty is not modelled")
        return float(np.exp(att_h + def_a + self.home_adv)), float(np.exp(att_a + def_h)), warnings

    def predict_score_distribution(self, home_team: str, away_team: str, max_goals: int = 12) -> ScoreDistribution:
        """Joint 90-minute score distribution."""
        lambda_h, mu_a, warnings = self._rates(home_team, away_team)
        for (x, y) in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            factor = self.tau(x, y, lambda_h, mu_a, self.rho)
            if factor <= 0.0:
                raise ValueError(
                    f"Invalid Dixon-Coles parameters: tau({x},{y})={factor} <= 0 "
                    f"for lambda_h={lambda_h:.3f}, mu_a={mu_a:.3f}, rho={self.rho:.4f}"
                )
        return score_grid(lambda_h, mu_a, self.rho, max_goals, endpoint="regulation",
                          metadata={"model": "dixon_coles", "lambda_home": lambda_h, "mu_away": mu_a, "rho": self.rho,
                                    "warnings": warnings})


def score_grid(lambda_h: float, mu_a: float, rho: float, max_goals: int = 12, endpoint: str = "regulation",
               metadata: Optional[Dict[str, Any]] = None) -> ScoreDistribution:
    """Independent Poisson grid with the Dixon-Coles low-score correction applied."""
    ph = poisson.pmf(np.arange(max_goals + 1), lambda_h)
    pa = poisson.pmf(np.arange(max_goals + 1), mu_a)
    grid = np.outer(ph, pa)
    grid[0, 0] *= DixonColesEngine.tau(0, 0, lambda_h, mu_a, rho)
    grid[0, 1] *= DixonColesEngine.tau(0, 1, lambda_h, mu_a, rho)
    grid[1, 0] *= DixonColesEngine.tau(1, 0, lambda_h, mu_a, rho)
    grid[1, 1] *= DixonColesEngine.tau(1, 1, lambda_h, mu_a, rho)
    grid /= grid.sum()
    return ScoreDistribution(grid=grid, home_support=np.arange(max_goals + 1), away_support=np.arange(max_goals + 1),
                             endpoint=endpoint, metadata=metadata or {})
