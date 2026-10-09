"""Baseball engine: shared game environment, starter-leash mixture, home-ninth truncation and an extra-innings endpoint (DST-08)."""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from scipy.optimize import least_squares
from scipy.stats import nbinom, norm

from ..base import BaseSportEngine, collect_games
from ...common.contracts import ScoreDistribution
from ...common.endpoints import baseball_extra_innings
from ...common.errors import FitFailed, MissingInputs
from ...common.leagues import LeagueProfile
from ...common.strengths import AttackDefenceModel

MAX_RUNS = 30
STARTER_IP_SD = 1.3          # UNFITTED analyst scenario value: spread of starter innings around the expected IP
EARLY_SHARE, LATE_SHARE = 8.0 / 9.0, 1.0 / 9.0
GH_NODES, GH_WEIGHTS = np.polynomial.hermite_e.hermegauss(7)
GH_WEIGHTS = GH_WEIGHTS / GH_WEIGHTS.sum()


def nb_pmf(mean: float, phi: float, size: int) -> np.ndarray:
    """Negative binomial with Var = mean + phi * mean^2 over 0..size-1 (Poisson as phi -> 0), renormalised."""
    if mean <= 0:
        out = np.zeros(size)
        out[0] = 1.0
        return out
    if phi < 1e-6:
        from scipy.stats import poisson
        pmf = poisson.pmf(np.arange(size), mean)
    else:
        r = 1.0 / phi
        pmf = nbinom.pmf(np.arange(size), r, r / (r + mean))
    return pmf / pmf.sum()


def innings_pmf(mean_ip: float, sd: float) -> Tuple[np.ndarray, np.ndarray]:
    """Discretised normal over whole innings 1..8 for the starter's length (the starter leash)."""
    support = np.arange(1, 9)
    edges = np.concatenate([[-np.inf], np.arange(1, 8) + 0.5, [np.inf]])
    weights = np.diff(norm.cdf(edges, loc=mean_ip, scale=sd))
    return support, weights / weights.sum()


def game_grid(mean_h: float, mean_a: float, phi_block: float, walk_off_overshoot: float, size: int = MAX_RUNS + 1,
              ninth_factor: float = 1.0) -> np.ndarray:
    """Nine-inning (home, away) grid: independent early and late blocks, home ninth played only when needed.

    Vectorised. With p = home runs through eight innings, q = visitors' nine-inning runs and r = home ninth runs:
      * visitors behind after the top of the ninth (a < h8): the game ends, final (h8, a);
      * otherwise the home ninth is played. If h8 + r9 <= a the home side finishes without the lead, final (h8 + r9, a);
        if h8 + r9 > a it walks off, credited a + 1 runs with probability 1 - overshoot and h8 + r9 with probability overshoot.
    """
    p = nb_pmf(EARLY_SHARE * mean_h, phi_block, size)
    a8 = nb_pmf(EARLY_SHARE * mean_a, phi_block, size)
    a9 = nb_pmf(LATE_SHARE * ninth_factor * mean_a, phi_block, size)
    r = nb_pmf(LATE_SHARE * ninth_factor * mean_h, phi_block, size)
    q = np.convolve(a8, a9)[:size]
    q = q / q.sum()
    t = np.arange(size)[:, None]                                    # home final runs (rows)
    a = np.arange(size)[None, :]                                    # visitors' final runs (columns)
    toeplitz = np.zeros((size, size))                               # R[h8, t] = r[t - h8]
    for h8 in range(size):
        toeplitz[h8, h8:] = r[:size - h8]
    cum = np.cumsum(p[:, None] * toeplitz, axis=0)                  # cum[a, t] = sum_{h8 <= a} p[h8] r[t - h8]
    cum_t = cum.T                                                   # (t, a)
    grid = np.where(t > a, p[:, None] * q[None, :], 0.0)            # home already ahead: row index is h8
    grid = grid + np.where(t <= a, cum_t * q[None, :], 0.0)          # bottom ninth finishes without the lead
    walk_off_mass = (np.where(t > a, cum_t, 0.0) * q[None, :]).sum(axis=0)
    grid = grid + overshoot_part(cum_t, q, t, a, walk_off_overshoot)
    for visitors in range(size):
        grid[min(visitors + 1, size - 1), visitors] += (1.0 - walk_off_overshoot) * walk_off_mass[visitors]
    return grid / grid.sum()


def overshoot_part(cum_t: np.ndarray, q: np.ndarray, t: np.ndarray, a: np.ndarray, overshoot: float) -> np.ndarray:
    """Walk-offs credited with the full inning's runs: cells (h8 + r9, a) with h8 + r9 > a."""
    return overshoot * np.where(t > a, cum_t, 0.0) * q[None, :]


def game_grid_reference(mean_h: float, mean_a: float, phi_block: float, walk_off_overshoot: float, size: int = MAX_RUNS + 1,
                        ninth_factor: float = 1.0) -> np.ndarray:
    """Straightforward loop implementation of `game_grid`, kept as the test oracle."""
    h8 = nb_pmf(EARLY_SHARE * mean_h, phi_block, size)
    a8 = nb_pmf(EARLY_SHARE * mean_a, phi_block, size)
    a9 = nb_pmf(LATE_SHARE * ninth_factor * mean_a, phi_block, size)
    h9 = nb_pmf(LATE_SHARE * ninth_factor * mean_h, phi_block, size)
    away_total = np.convolve(a8, a9)[:size]
    away_total = away_total / away_total.sum()
    grid = np.zeros((size, size))
    for hr in range(size):
        for a_runs in range(size):
            weight = h8[hr] * away_total[a_runs]
            if a_runs < hr:
                grid[hr, a_runs] += weight
                continue
            for r9 in range(size):
                total = hr + r9
                w = weight * h9[r9]
                if total <= a_runs:
                    grid[total, a_runs] += w
                else:
                    grid[min(a_runs + 1, size - 1), a_runs] += w * (1 - walk_off_overshoot)
                    if total < size:
                        grid[total, a_runs] += w * walk_off_overshoot
    return grid / grid.sum()


@dataclass(frozen=True)
class BaseballStructure:
    """League-level shape parameters (dimensionless, so they transfer across matchups)."""
    phi: float             # latent negative-binomial dispersion
    tau: float             # matchup shock: home x e^{tau z}, away x e^{-tau z}
    targets: Tuple[float, ...]


class BaseballEngine(BaseSportEngine):
    """Predictive engine for baseball (MLB, NPB, KBO).

    A game's runs share one environment factor E ~ lognormal(mean 1, sigma) (park, weather), which induces positive
    covariance between the teams. A matchup shock (home x e^{tau z}, away x e^{-tau z}, z standard normal) adds
    margin variance without adding total variance, the footprint of day-to-day starter and lineup differences.
    Each team's runs are negative binomial given both factors, split into eight early innings and a ninth, with the
    home ninth played only when the visitors lead or tie. Starter length is a mixture, not a fixed 5.2 innings.

    The supplied or fitted run expectations are read as expected FINAL scores; the latent rates, the dispersion and
    tau are solved so that the modelled final scores reproduce the target means, `total_sd` and `margin_sd`.
    """

    def __init__(self, league: Optional[LeagueProfile] = None, unknown_team_policy: str = "refuse",
                 environment_sigma: Optional[float] = None, total_sd: Optional[float] = None, margin_sd: Optional[float] = None,
                 starter_ip_sd: float = STARTER_IP_SD, innings_cap: Optional[int] = None,
                 walk_off_overshoot_share: float = 0.275, extra_inning_pmf: Optional[List[float]] = None,
                 ninth_factor: float = 1.0):
        super().__init__("baseball", league, unknown_team_policy)
        self.environment_sigma = environment_sigma
        self.total_sd = total_sd
        self.margin_sd = margin_sd
        self.starter_ip_sd = starter_ip_sd
        self.innings_cap = innings_cap
        self.walk_off_overshoot_share = walk_off_overshoot_share
        self.extra_inning_pmf = extra_inning_pmf
        self.ninth_factor = ninth_factor        # ninth-inning scoring relative to other innings; 1.0 = no closer effect modelled
        self.model: Optional[AttackDefenceModel] = None
        self._structures: Dict[Tuple[float, ...], BaseballStructure] = {}

    # ------------------------------------------------------------------ fitting
    def fit(self, train_data: Any) -> "BaseballEngine":
        games = collect_games(train_data, ("home_runs", "home_score"), ("away_runs", "away_score"))
        self.model = AttackDefenceModel().fit(games)
        total_res, margin_res = [], []
        for home, away, hs, as_ in games:
            mu_h, mu_a = self.model.expected(home, away)
            total_res.append((hs + as_) - (mu_h + mu_a))
            margin_res.append((hs - as_) - (mu_h - mu_a))
        self.total_sd = float(np.sqrt(np.mean(np.square(total_res))))
        self.margin_sd = float(np.sqrt(np.mean(np.square(margin_res))))
        self.is_fitted = True
        return self

    # ------------------------------------------------------------------- inputs
    def _parameter(self, ctx: Dict[str, Any], key: str, own: Optional[float], profile_key: str) -> float:
        if ctx.get(key) is not None:
            return float(ctx[key])
        if own is not None:
            return float(own)
        if self.league is not None and profile_key == "__profile_total_sd__":
            return float(self.league.total_sd)
        if self.league is not None and profile_key == "__profile_margin_sd__":
            return float(self.league.margin_sd)
        if self.league is not None and profile_key in self.league.extras:
            return float(self.league.extras[profile_key])
        raise MissingInputs(f"baseball: {key} is required (pass it, fit the engine, or use a league profile that carries {profile_key})")

    def _team_means(self, ctx: Dict[str, Any]) -> Tuple[float, float]:
        if ctx.get("home_expected_runs") is not None and ctx.get("away_expected_runs") is not None:
            return float(ctx["home_expected_runs"]), float(ctx["away_expected_runs"])
        home, away = ctx.get("home_team"), ctx.get("away_team")
        if self.is_fitted and self.model is not None:
            for team in (home, away):
                if not self.model.knows(team):
                    self._warn(f"unknown team {team!r}: league-average strength used; uncertainty not modelled")
            return self.model.expected(home, away, unknown="average" if self.unknown_team_policy == "league_average" else "refuse")
        if self.league is not None and self.unknown_team_policy == "league_average":
            self._warn("no fitted team strengths: league-average run expectation from the profile")
            return self.league.mean_home, self.league.mean_away
        self._need_fit_or_profile()
        raise MissingInputs("baseball: pass home_expected_runs/away_expected_runs, or fit the engine, "
                            "or use unknown_team_policy='league_average' with a league profile")

    def _staff_adjustment(self, ctx: Dict[str, Any], side: str) -> List[Tuple[float, float]]:
        """[(weight, runs allowed per 9 relative multiplier)] for the starter leash facing this batting side."""
        sp, bp, ip = ctx.get(f"{side}_sp_ra9"), ctx.get(f"{side}_bp_ra9"), ctx.get(f"{side}_sp_expected_ip")
        if sp is None and bp is None and ip is None:
            return [(1.0, 1.0)]
        if sp is None or bp is None or ip is None:
            raise MissingInputs(f"baseball: {side}_sp_ra9, {side}_bp_ra9 and {side}_sp_expected_ip must be given together")
        support, weights = innings_pmf(float(ip), self.starter_ip_sd)
        if ctx.get("league_ra9") is not None:
            league_ra9 = float(ctx["league_ra9"])
        elif self.league is not None:
            league_ra9 = self.league.mean_team_score            # a nine-inning game: runs per team per game ~ runs per nine
        else:
            raise MissingInputs("baseball: league_ra9 (league runs per nine) or a league profile is required to scale starter and bullpen RA9")
        out = []
        for innings, weight in zip(support, weights):
            ra9 = (float(sp) * innings + float(bp) * (9.0 - innings)) / 9.0
            out.append((float(weight), ra9 / league_ra9))
        return out

    # --------------------------------------------------------------- prediction
    def _mixture_grid(self, mean_h: float, mean_a: float, phi: float, sigma: float, tau: float, overshoot: float,
                      park: float = 1.0, staff_h=((1.0, 1.0),), staff_a=((1.0, 1.0),), ninth_factor: float = 1.0) -> np.ndarray:
        phi_block = phi / (EARLY_SHARE ** 2 + LATE_SHARE ** 2)             # keep the nine-inning variance when splitting blocks
        grid = np.zeros((MAX_RUNS + 1, MAX_RUNS + 1))
        match_nodes = [(0.0, 1.0)] if tau <= 0 else list(zip(GH_NODES, GH_WEIGHTS))
        for z, w_env in zip(GH_NODES, GH_WEIGHTS):
            env = float(np.exp(sigma * z - 0.5 * sigma ** 2)) * park
            for u, w_match in match_nodes:
                shock_h, shock_a = float(np.exp(tau * u - 0.5 * tau ** 2)), float(np.exp(-tau * u - 0.5 * tau ** 2))
                for w_h, mult_h in staff_h:
                    for w_a, mult_a in staff_a:
                        grid += (w_env * w_match * w_h * w_a) * game_grid(mean_h * env * shock_h * mult_h, mean_a * env * shock_a * mult_a,
                                                                          phi_block, overshoot, ninth_factor=ninth_factor)
        return grid / grid.sum()

    def _extras_inputs(self, ctx: Dict[str, Any]):
        """(pmf, cap) for the full-game endpoint, or (None, None) when the engine cannot resolve extras."""
        pmf = ctx.get("extra_inning_pmf", self.extra_inning_pmf)
        if pmf is None and self.league is not None and "extra_inning_runs_p0" in self.league.extras:
            pmf = [self.league.extras[f"extra_inning_runs_p{r}"] for r in range(6)]
        cap = ctx.get("innings_cap", self.innings_cap)
        if pmf is not None and cap is None and self.league is not None and self.league.extras.get("tie_share", 0.0) > 0.0:
            return pmf, "missing"
        return pmf, cap

    # -- calibration -------------------------------------------------------------------
    def _final_moments(self, lh, la, structure_phi, tau, ninth, sigma, overshoot, pmf, cap):
        support = np.arange(MAX_RUNS + 1)
        reg = ScoreDistribution(self._mixture_grid(lh, la, structure_phi, sigma, tau, overshoot, ninth_factor=ninth), support, support,
                                endpoint="regulation")
        tie_after_nine = float(np.trace(reg.grid))
        dist = reg if pmf is None else baseball_extra_innings(reg, pmf, innings_cap=cap, walk_off_overshoot_share=overshoot)
        h, a = np.meshgrid(dist.home_support, dist.away_support, indexing="ij")
        mh, ma = float((h * dist.grid).sum()), float((a * dist.grid).sum())
        vt = float(((h + a - mh - ma) ** 2 * dist.grid).sum())
        vm = float(((h - a - mh + ma) ** 2 * dist.grid).sum())
        return mh, ma, vt, vm, tie_after_nine

    def _structure(self, target_h: float, target_a: float, total_sd: float, margin_sd: float, sigma: float, overshoot: float,
                   ninth: float, pmf, cap) -> BaseballStructure:
        """Solve (latent means, phi, tau) for the league's final-score mean, total SD and margin SD.

        Observed scores already include the skipped home ninth and any extra innings, so feeding them in as latent
        run rates would apply both effects twice. The solution is cached; per-game predictions re-solve only the means.
        Known limit: the negative-binomial shape leaves the margin distribution somewhat too peaked (see the engine
        tests: one-run share about 2 points high, tie-after-nine about 1.4 points high against the archive).
        """
        key = (round(target_h, 6), round(target_a, 6), round(total_sd, 6), round(margin_sd, 6), round(sigma, 6), round(overshoot, 6),
               round(ninth, 6), -1.0 if cap is None else float(cap), 0.0 if pmf is None else float(sum(pmf[1:])))
        if key in self._structures:
            return self._structures[key]
        mean_team = 0.5 * (target_h + target_a)
        phi0 = max((0.25 * total_sd ** 2 - mean_team) / mean_team ** 2, 0.02)

        def residuals(x):
            lh, la, phi, tau = x
            mh, ma, vt, vm, _ = self._final_moments(lh, la, phi, tau, ninth, sigma, overshoot, pmf, cap)
            return np.array([mh / target_h - 1.0, ma / target_a - 1.0, vt / total_sd ** 2 - 1.0, vm / margin_sd ** 2 - 1.0])

        fit = least_squares(residuals, [target_h, target_a, phi0, 0.1], xtol=1e-9, ftol=1e-9, diff_step=1e-3,
                            bounds=([0.4 * target_h, 0.4 * target_a, 1e-3, 0.0], [2.5 * target_h, 2.5 * target_a, 2.0, 0.6]))
        worst = float(np.max(np.abs(fit.fun)))
        if worst > 0.01:
            raise FitFailed("BaseballEngine", f"league structure did not reach its targets (worst relative error {worst:.4f})")
        structure = BaseballStructure(phi=float(fit.x[2]), tau=float(fit.x[3]), targets=(target_h, target_a, total_sd, margin_sd))
        self._structures[key] = structure
        return structure

    def _solve_means(self, structure: BaseballStructure, target_h: float, target_a: float, sigma: float, overshoot: float,
                     ninth: float, pmf, cap):
        lh, la = target_h, target_a
        for _ in range(25):
            mh, ma, *_ = self._final_moments(lh, la, structure.phi, structure.tau, ninth, sigma, overshoot, pmf, cap)
            if abs(mh / target_h - 1.0) < 2e-4 and abs(ma / target_a - 1.0) < 2e-4:
                break
            lh, la = lh * target_h / mh, la * target_a / ma
        return lh, la

    def predict_distribution(self, match_context: Dict[str, Any], endpoint: str = "regulation") -> ScoreDistribution:
        """endpoint "regulation" = nine innings; "full_game" = final score including extra innings.

        Unless `mean_basis="latent"`, the supplied or fitted run expectations are read as expected FINAL scores
        and the latent rates are solved to reproduce them (see `_calibrate`).
        """
        if endpoint not in ("regulation", "full_game"):
            raise ValueError("endpoint must be 'regulation' (nine innings) or 'full_game'")
        target_h, target_a = self._team_means(match_context)
        park = float(match_context.get("park_factor", 1.0))
        sigma = self._parameter(match_context, "environment_sigma", self.environment_sigma, "park_environment_sigma")
        total_sd = self._parameter(match_context, "total_sd", self.total_sd, "__profile_total_sd__")
        margin_sd = self._parameter(match_context, "margin_sd", self.margin_sd, "__profile_margin_sd__")
        overshoot = float(match_context.get("walk_off_overshoot_share", self.walk_off_overshoot_share))
        pmf, cap = self._extras_inputs(match_context)
        if cap == "missing":
            raise MissingInputs(f"baseball: {self.league.league} permits ties; give the rulebook innings_cap")
        if endpoint == "full_game" and pmf is None:
            raise MissingInputs("baseball: full_game needs an extra-inning run distribution (extra_inning_pmf or a profile carrying one)")
        ninth = float(match_context.get("ninth_factor", self.ninth_factor))
        if match_context.get("mean_basis", "final_score") == "latent":
            lh, la, tau = target_h, target_a, float(match_context.get("matchup_tau", 0.0))
            phi = float(match_context.get("latent_dispersion_phi", 0.3))
        else:
            mean_h0, mean_a0 = (self.league.mean_home, self.league.mean_away) if self.league is not None else (target_h, target_a)
            structure = self._structure(mean_h0, mean_a0, total_sd, margin_sd, sigma, overshoot, ninth, pmf, cap)
            phi, tau = structure.phi, structure.tau
            lh, la = self._solve_means(structure, target_h, target_a, sigma, overshoot, ninth, pmf, cap)
        staff_h = self._staff_adjustment(match_context, "away")              # home batters face the visitors' pitchers
        staff_a = self._staff_adjustment(match_context, "home")
        grid = self._mixture_grid(lh, la, phi, sigma, tau, overshoot, park, staff_h, staff_a, ninth)
        meta = {"model": "baseball_nb_environment", "target_final_mean_home": target_h, "target_final_mean_away": target_a,
                "latent_mean_home": lh, "latent_mean_away": la, "environment_sigma": sigma, "dispersion_phi": phi,
                "matchup_tau": tau, "ninth_factor": ninth, "total_sd": total_sd, "margin_sd": margin_sd,
                "starter_ip_sd": self.starter_ip_sd, "warnings": self._take_warnings()}
        dist = ScoreDistribution(grid, np.arange(MAX_RUNS + 1), np.arange(MAX_RUNS + 1), endpoint="regulation", metadata=meta)
        if endpoint == "regulation":
            return dist
        return baseball_extra_innings(dist, pmf, innings_cap=cap, walk_off_overshoot_share=overshoot)
