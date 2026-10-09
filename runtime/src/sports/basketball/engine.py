"""Basketball engine: possessions x efficiency means, data-driven support and a repeatable-overtime endpoint (DST-03, DST-09)."""

from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import numpy as np
from scipy.optimize import least_squares
from scipy.special import gammaln

from ..base import BaseSportEngine, collect_games
from ...common.contracts import ScoreDistribution
from ...common.endpoints import basketball_overtime
from ...common.errors import FitFailed, MissingInputs
from ...common.leagues import LeagueProfile
from ...common.strengths import AttackDefenceModel

SUPPORT_SD = 6.0     # grid half-width in standard deviations: mu +/- 6 sigma, floored at zero


@dataclass(frozen=True)
class BasketballStructure:
    """League-level shape: per-team SD and the home/away score correlation (shared pace)."""
    sd: float
    corr: float


def with_tie_share(grid: np.ndarray, tie_share: float) -> np.ndarray:
    """Rescale the diagonal (tied regulation scores) to `tie_share`, spreading the rest proportionally.

    A normal margin gives about 1/(sd * sqrt(2 pi)) ties (2.5% in the NBA) while about 4.7% of NBA games go to
    overtime; the tied mass is what overtime resolves, so it is calibrated to the observed overtime rate.
    """
    if not 0.0 < tie_share < 0.5:
        raise ValueError("tie_share must lie in (0, 0.5)")
    n = min(grid.shape)
    diag = np.zeros_like(grid, dtype=bool)
    diag[np.arange(n), np.arange(n)] = True
    current = float(grid[diag].sum())
    if current <= 0.0:
        raise ValueError("grid has no tied mass to rescale")
    out = grid.copy()
    out[diag] *= tie_share / current
    out[~diag] *= (1.0 - tie_share) / (1.0 - current)
    return out


def bivariate_grid(mean_h: float, mean_a: float, sd_h: float, sd_a: float, corr: float, df: Optional[float] = None) -> np.ndarray:
    """Discretised bivariate normal (or Student-t when `df` is given) on a data-driven support, embedded in 0..max.

    The support runs from max(0, mu - 6 sd) to mu + 6 sd for each team (DST-03): no fixed 60-160 window, so low-scoring
    leagues are not truncated and the grid mean equals the input mean.
    """
    if not -0.99 < corr < 0.99:
        raise ValueError("score correlation must lie in (-0.99, 0.99)")
    lo_h, hi_h = max(0, int(np.floor(mean_h - SUPPORT_SD * sd_h))), int(np.ceil(mean_h + SUPPORT_SD * sd_h))
    lo_a, hi_a = max(0, int(np.floor(mean_a - SUPPORT_SD * sd_a))), int(np.ceil(mean_a + SUPPORT_SD * sd_a))
    zh = (np.arange(lo_h, hi_h + 1) - mean_h) / sd_h
    za = (np.arange(lo_a, hi_a + 1) - mean_a) / sd_a
    q = (zh[:, None] ** 2 - 2.0 * corr * zh[:, None] * za[None, :] + za[None, :] ** 2) / (1.0 - corr ** 2)
    if df is None:
        block = np.exp(-0.5 * q)
    else:
        if df <= 2.0:
            raise ValueError("df must exceed 2 for a finite variance")
        # scale so the marginal variance equals sd^2: a t variable has variance scale^2 * df / (df - 2)
        q = q * df / (df - 2.0)
        block = np.exp(-0.5 * (df + 2.0) * np.log1p(q / df) + gammaln(0.5 * (df + 2.0)) - gammaln(0.5 * df))
    grid = np.zeros((hi_h + 1, hi_a + 1))
    grid[lo_h:, lo_a:] = block / block.sum()
    return grid


class BasketballEngine(BaseSportEngine):
    """Predictive engine for basketball (NBA, WNBA, EuroLeague, NBL ...).

    Means come from (a) the context (`home_expected_points`/`away_expected_points`, or `pace` x `home_ppp`/`away_ppp`),
    (b) the fitted opponent-adjusted strengths. The spread of scores comes from the league's total and margin SDs
    (which fix the per-team SD and the shared-pace correlation) and is calibrated so that the FULL-GAME scores,
    overtime included, reproduce those SDs.
    """

    def __init__(self, league: Optional[LeagueProfile] = None, unknown_team_policy: str = "refuse",
                 regulation_minutes: Optional[float] = None, ot_minutes: float = 5.0, margin_df: Optional[float] = None,
                 total_sd: Optional[float] = None, margin_sd: Optional[float] = None):
        super().__init__("basketball", league, unknown_team_policy)
        self.regulation_minutes = regulation_minutes
        self.ot_minutes = ot_minutes
        self.margin_df = margin_df
        self.total_sd = total_sd
        self.margin_sd = margin_sd
        self.model: Optional[AttackDefenceModel] = None
        self._structures: Dict[Tuple[float, ...], BasketballStructure] = {}

    def fit(self, train_data: Any) -> "BasketballEngine":
        games = collect_games(train_data, ("home_score", "home_points"), ("away_score", "away_points"))
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

    # ------------------------------------------------------------------ inputs
    def _means(self, ctx: Dict[str, Any]) -> Tuple[float, float]:
        if ctx.get("home_expected_points") is not None and ctx.get("away_expected_points") is not None:
            return float(ctx["home_expected_points"]), float(ctx["away_expected_points"])
        if ctx.get("pace") is not None:
            self._require(ctx, "home_ppp", "away_ppp")
            return float(ctx["pace"]) * float(ctx["home_ppp"]), float(ctx["pace"]) * float(ctx["away_ppp"])
        home, away = ctx.get("home_team"), ctx.get("away_team")
        if self.is_fitted and self.model is not None:
            for team in (home, away):
                if not self.model.knows(team):
                    self._warn(f"unknown team {team!r}: league-average strength used; uncertainty not modelled")
            return self.model.expected(home, away, unknown="average" if self.unknown_team_policy == "league_average" else "refuse")
        if self.league is not None and self.unknown_team_policy == "league_average":
            self._warn("no fitted team strengths: league-average points from the profile")
            return self.league.mean_home, self.league.mean_away
        self._need_fit_or_profile()
        raise MissingInputs("basketball: pass home/away expected points (or pace and ppp), or fit the engine, "
                            "or use unknown_team_policy='league_average' with a league profile")

    def _sds(self, ctx: Dict[str, Any]) -> Tuple[float, float]:
        total_sd = ctx.get("total_sd", self.total_sd if self.total_sd is not None else (self.league.total_sd if self.league else None))
        margin_sd = ctx.get("margin_sd", self.margin_sd if self.margin_sd is not None else (self.league.margin_sd if self.league else None))
        if total_sd is None or margin_sd is None:
            raise MissingInputs("basketball: total_sd and margin_sd are required (pass them, fit the engine, or use a league profile); "
                                "no NBA default is borrowed for another league")
        return float(total_sd), float(margin_sd)

    def _minutes(self, ctx: Dict[str, Any]) -> Optional[float]:
        if ctx.get("regulation_minutes") is not None:
            return float(ctx["regulation_minutes"])
        if self.regulation_minutes is not None:
            return float(self.regulation_minutes)
        if self.league is not None and "regulation_minutes" in self.league.extras:
            return float(self.league.extras["regulation_minutes"])
        return None

    # ----------------------------------------------------------------- shapes
    def _tie_share(self, ctx: Dict[str, Any]) -> Optional[float]:
        if ctx.get("tie_share") is not None:
            return float(ctx["tie_share"])
        if self.league is not None and "overtime_share" in self.league.extras:
            return float(self.league.extras["overtime_share"])
        return None

    def _full_grid(self, mean_h, mean_a, sd, corr, minutes, df, tie_share=None):
        grid = bivariate_grid(mean_h, mean_a, sd, sd, corr, df)
        if tie_share is not None:
            grid = with_tie_share(grid, tie_share)
        dist = ScoreDistribution(grid, np.arange(grid.shape[0]), np.arange(grid.shape[1]), endpoint="regulation")
        if minutes is None:
            return dist, dist
        return dist, basketball_overtime(dist, mean_h, mean_a, sd, sd, regulation_minutes=minutes, ot_minutes=self.ot_minutes)

    @staticmethod
    def _moments(dist: ScoreDistribution):
        h, a = np.meshgrid(dist.home_support, dist.away_support, indexing="ij")
        mh, ma = float((h * dist.grid).sum()), float((a * dist.grid).sum())
        vt = float(((h + a - mh - ma) ** 2 * dist.grid).sum())
        vm = float(((h - a - mh + ma) ** 2 * dist.grid).sum())
        return mh, ma, vt, vm

    def _structure(self, mean_h: float, mean_a: float, total_sd: float, margin_sd: float, minutes, df, tie_share) -> BasketballStructure:
        key = (round(mean_h, 4), round(mean_a, 4), round(total_sd, 4), round(margin_sd, 4), -1.0 if minutes is None else minutes,
               -1.0 if df is None else df, -1.0 if tie_share is None else round(tie_share, 5))
        if key in self._structures:
            return self._structures[key]
        sd0 = float(np.sqrt((total_sd ** 2 + margin_sd ** 2) / 4.0))
        corr0 = float(np.clip((total_sd ** 2 - margin_sd ** 2) / (total_sd ** 2 + margin_sd ** 2), -0.9, 0.9))

        def residuals(x):
            sd, corr = x
            _, full = self._full_grid(mean_h, mean_a, sd, corr, minutes, df, tie_share)
            _, _, vt, vm = self._moments(full)
            return np.array([vt / total_sd ** 2 - 1.0, vm / margin_sd ** 2 - 1.0])

        fit = least_squares(residuals, [sd0, corr0], bounds=([0.3 * sd0, -0.95], [3.0 * sd0, 0.95]), xtol=1e-10, ftol=1e-10, diff_step=1e-3)
        if float(np.max(np.abs(fit.fun))) > 5e-3:
            raise FitFailed("BasketballEngine", f"score spread did not reach its targets (worst relative error {np.max(np.abs(fit.fun)):.4f})")
        structure = BasketballStructure(sd=float(fit.x[0]), corr=float(fit.x[1]))
        self._structures[key] = structure
        return structure

    # -------------------------------------------------------------- prediction
    def predict_distribution(self, match_context: Dict[str, Any], endpoint: str = "regulation") -> ScoreDistribution:
        """endpoint "regulation" = 4 quarters; "full_game" = final score including repeatable overtimes (needs the clock length)."""
        if endpoint not in ("regulation", "full_game"):
            raise ValueError("endpoint must be 'regulation' or 'full_game'")
        target_h, target_a = self._means(match_context)
        scale = float(match_context.get("scoring_multiplier", 1.0))               # explicit regime adjustment (rule change etc.)
        target_h, target_a = target_h * scale, target_a * scale
        minutes = self._minutes(match_context)
        if endpoint == "full_game" and minutes is None:
            raise MissingInputs("basketball: full_game needs regulation_minutes (context, constructor, or a profile that records it)")
        df = match_context.get("margin_df", self.margin_df)
        meta: Dict[str, Any] = {"model": "basketball_bivariate", "endpoint_basis": "final_score"}
        if match_context.get("mean_basis") == "latent" or match_context.get("sd_home") is not None:
            self._require(match_context, "sd_home", "sd_away")
            sd_h, sd_a = float(match_context["sd_home"]), float(match_context["sd_away"])
            corr = float(match_context.get("pace_correlation", 0.0))
            mean_h, mean_a = target_h, target_a
            meta["endpoint_basis"] = "regulation_latent"
            grid = bivariate_grid(mean_h, mean_a, sd_h, sd_a, corr, df)
            reg = ScoreDistribution(grid, np.arange(grid.shape[0]), np.arange(grid.shape[1]), endpoint="regulation")
            full = basketball_overtime(reg, mean_h, mean_a, sd_h, sd_a, regulation_minutes=minutes, ot_minutes=self.ot_minutes) \
                if endpoint == "full_game" else reg
        else:
            total_sd, margin_sd = self._sds(match_context)
            m_h0, m_a0 = (self.league.mean_home, self.league.mean_away) if self.league is not None else (target_h, target_a)
            tie_share = self._tie_share(match_context)
            structure = self._structure(m_h0, m_a0, total_sd, margin_sd, minutes, df, tie_share)
            mean_h, mean_a = target_h, target_a
            for _ in range(25):                                                        # latent regulation means that reproduce the final-score targets
                reg, full = self._full_grid(mean_h, mean_a, structure.sd, structure.corr, minutes, df, tie_share)
                mh, ma, _, _ = self._moments(full)
                if abs(mh - target_h) < 0.01 and abs(ma - target_a) < 0.01:
                    break
                mean_h, mean_a = mean_h + (target_h - mh), mean_a + (target_a - ma)
            sd_h = sd_a = structure.sd
            corr = structure.corr
            meta.update(structure_sd=structure.sd, structure_corr=structure.corr)
        out = full if endpoint == "full_game" else reg
        out.metadata.update(meta, latent_mean_home=mean_h, latent_mean_away=mean_a, target_home=target_h, target_away=target_a,
                            regulation_minutes=minutes, warnings=self._take_warnings())
        return out
