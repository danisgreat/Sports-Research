"""Poisson / Dixon–Coles team ratings for low-scoring sports (soccer goals, NHL regulation goals, MLB runs).

    log lambda_home = c + home + att[h] + dfn[a]
    log lambda_away = c        + att[a] + dfn[h]
Time-decayed weighted likelihood, ridge penalty towards a prior centre, optional Dixon–Coles low-score
dependence rho (soccer), optional negative-binomial dispersion phi estimated by moments (MLB).
The gradient is analytic and the likelihood is vectorised (the 9 October retrospective's F-ML-3).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy import optimize

from ml.config import League
from ml.core.distributions import ScoreGrid
from ml.models.common import FitError, apply_tie_rule, decay_weights


@dataclass(frozen=True)
class CountParams:
    half_life_days: float
    ridge: float
    use_rho: bool = False
    negbin: bool = False
    promoted_prior: bool = False

    def __post_init__(self):
        if not np.isfinite(self.half_life_days) or self.half_life_days <= 0 or not np.isfinite(self.ridge) or self.ridge < 0:
            raise ValueError("invalid count-model decay or regularization parameters")


class PoissonRatings:
    name = "DIXON_COLES"

    def __init__(self, lg: League, params: CountParams):
        self.lg = lg
        self.p = params
        self.fitted = False

    # ---------------------------------------------------------------------------------------------- fitting
    def _scores(self, train: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
        if self.lg.tie_rule == "hockey_regulation":
            return train["reg_hs"].to_numpy(float), train["reg_as"].to_numpy(float)
        return train["hs"].to_numpy(float), train["as_"].to_numpy(float)

    def _optimise(self, hi, ai, yh, ya, w, T, centre_att, centre_dfn):
        use_rho = self.p.use_rho
        k0 = 3 if use_rho else 2
        m00 = (yh == 0) & (ya == 0)
        m01 = (yh == 0) & (ya == 1)
        m10 = (yh == 1) & (ya == 0)
        m11 = (yh == 1) & (ya == 1)
        ridge = self.p.ridge

        def unpack(th):
            c, home = th[0], th[1]
            rho = th[2] if use_rho else 0.0
            att, dfn = th[k0:k0 + T], th[k0 + T:]
            return c, home, rho, att, dfn

        def f_and_g(th):
            c, home, rho, att, dfn = unpack(th)
            eh = c + home + att[hi] + dfn[ai]
            ea = c + att[ai] + dfn[hi]
            lh, la = np.exp(eh), np.exp(ea)
            ll = yh * eh - lh + ya * ea - la
            gh = yh - lh
            ga = ya - la
            grho = 0.0
            if use_rho:
                tau = np.ones_like(lh)
                tau[m00] = 1 - lh[m00] * la[m00] * rho
                tau[m01] = 1 + lh[m01] * rho
                tau[m10] = 1 + la[m10] * rho
                tau[m11] = 1 - rho
                if np.any(tau <= 0):
                    return 1e100, np.zeros_like(th)
                ll = ll + np.log(tau)
                dh = np.zeros_like(lh)
                da = np.zeros_like(lh)
                dr = np.zeros_like(lh)
                dh[m00] = -lh[m00] * la[m00] * rho / tau[m00]
                da[m00] = dh[m00]
                dr[m00] = -lh[m00] * la[m00] / tau[m00]
                dh[m01] = lh[m01] * rho / tau[m01]
                dr[m01] = lh[m01] / tau[m01]
                da[m10] = la[m10] * rho / tau[m10]
                dr[m10] = la[m10] / tau[m10]
                dr[m11] = -1 / tau[m11]
                gh = gh + dh
                ga = ga + da
                grho = float(np.sum(w * dr))
            obj = -np.sum(w * ll) + 0.5 * ridge * (np.sum((att - centre_att) ** 2) + np.sum((dfn - centre_dfn) ** 2))
            g = np.zeros_like(th)
            wgh, wga = w * gh, w * ga
            g[0] = -(wgh.sum() + wga.sum())
            g[1] = -wgh.sum()
            if use_rho:
                g[2] = -grho
            g_att = -(np.bincount(hi, wgh, T) + np.bincount(ai, wga, T)) + ridge * (att - centre_att)
            g_dfn = -(np.bincount(ai, wgh, T) + np.bincount(hi, wga, T)) + ridge * (dfn - centre_dfn)
            g[k0:k0 + T] = g_att
            g[k0 + T:] = g_dfn
            return obj, g

        mean_goals = max(float(np.average(np.concatenate([yh, ya]), weights=np.concatenate([w, w]))), 0.05)
        th0 = np.zeros(k0 + 2 * T)
        th0[0] = np.log(mean_goals)
        th0[k0:k0 + T] = centre_att
        th0[k0 + T:] = centre_dfn
        bounds = [(None, None), (-1.0, 1.0)] + ([(-0.25, 0.25)] if use_rho else []) + [(-3.0, 3.0)] * (2 * T)
        res = optimize.minimize(f_and_g, th0, jac=True, method="L-BFGS-B", bounds=bounds,
                                options={"maxiter": 2000, "gtol": 1e-7})
        if not res.success:
            raise FitError(f"likelihood optimisation failed: {res.message}")
        if not np.all(np.isfinite(res.x)) or not np.isfinite(res.fun) or res.fun >= 1e99:
            raise FitError("optimiser returned an invalid point")
        return unpack(res.x)

    def fit(self, train: pd.DataFrame, as_of: pd.Timestamp, season: int | None = None) -> "PoissonRatings":
        if len(train) < 30:
            raise FitError(f"only {len(train)} training games")
        w = decay_weights(train["date"], as_of, self.p.half_life_days)
        teams = sorted(set(train["home"]) | set(train["away"]))
        idx = {t: i for i, t in enumerate(teams)}
        T = len(teams)
        hi = train["home"].map(idx).to_numpy()
        ai = train["away"].map(idx).to_numpy()
        yh, ya = self._scores(train)
        centre_att = np.zeros(T)
        centre_dfn = np.zeros(T)
        self.new_centre = (0.0, 0.0)
        c, home, rho, att, dfn = self._optimise(hi, ai, yh, ya, w, T, centre_att, centre_dfn)
        if self.p.promoted_prior:
            season = int(train["season"].max()) if season is None else int(season)
            centre = self._promoted_centre(train, idx, att, dfn, season)
            if centre is not None:
                self.new_centre = centre
                newcomers = self._newcomers(train, season)
                for t in newcomers:
                    centre_att[idx[t]], centre_dfn[idx[t]] = centre
                if newcomers:
                    c, home, rho, att, dfn = self._optimise(hi, ai, yh, ya, w, T, centre_att, centre_dfn)
        self.teams, self.idx = teams, idx
        self.c, self.home, self.rho, self.att, self.dfn = c, home, rho, att, dfn
        lam_h = np.exp(c + home + att[hi] + dfn[ai])
        lam_a = np.exp(c + att[ai] + dfn[hi])
        self.phi = 0.0
        if self.p.negbin:
            num = np.sum(w * ((yh - lam_h) ** 2 - lam_h)) + np.sum(w * ((ya - lam_a) ** 2 - lam_a))
            den = np.sum(w * lam_h ** 2) + np.sum(w * lam_a ** 2)
            self.phi = float(max(num / den, 0.0))
        self.p_home_extra = self._p_home_extra(train)
        self.residual_draw = self._residual_draw(train, float(np.average(yh, weights=w)), float(np.average(ya, weights=w)))
        self.n_train = len(train)
        self.as_of = as_of
        self.fitted = True
        return self

    @staticmethod
    def _newcomers(train: pd.DataFrame, cur: int) -> list[str]:
        prior = set(train.loc[train["season"] < cur, "home"]) | set(train.loc[train["season"] < cur, "away"])
        now = set(train.loc[train["season"] == cur, "home"]) | set(train.loc[train["season"] == cur, "away"])
        return sorted(now - prior) if prior else []

    @staticmethod
    def _promoted_centre(train: pd.DataFrame, idx: dict, att: np.ndarray, dfn: np.ndarray, season: int):
        """Mean (attack, defence) of the bottom three teams by points in the season before ``season``."""
        prev = train[train["season"] == season - 1]
        if prev.empty:
            return None
        pts = {}
        for r in prev.itertuples():
            ph = 3 if r.hs > r.as_ else (1 if r.hs == r.as_ else 0)
            pa = 3 if r.as_ > r.hs else (1 if r.hs == r.as_ else 0)
            pts[r.home] = pts.get(r.home, 0) + ph
            pts[r.away] = pts.get(r.away, 0) + pa
        bottom = sorted(pts, key=pts.get)[:3]
        ii = [idx[t] for t in bottom if t in idx]
        if not ii:
            return None
        return float(np.mean(att[ii])), float(np.mean(dfn[ii]))

    def _residual_draw(self, train: pd.DataFrame, mh: float, ma: float) -> float:
        """Share of tied regulation mass that stays drawn: observed full-game draw rate / regulation tie mass at the
        league means (method of moments). 0 in the modern NHL/MLB; positive where ties are allowed (NPB, KBO, old eras)."""
        if self.lg.tie_rule == "draw" or len(train) == 0:
            return 0.0
        draws = float((train["hs"] == train["as_"]).mean())
        g = ScoreGrid.negbin(mh, ma, self.phi) if self.p.negbin else ScoreGrid.poisson(max(mh, 0.05), max(ma, 0.05))
        tie = g.winner()[1]
        return float(np.clip(draws / tie, 0.0, 1.0)) if tie > 0 else 0.0

    def _p_home_extra(self, train: pd.DataFrame) -> float:
        if self.lg.tie_rule == "hockey_regulation":
            ot = train[train["decision"].isin(["Overtime", "Shootout"])]
        elif self.lg.tie_rule == "extras":
            ot = train[train["decision"] == "EXTRAS"]
        else:
            return 0.5
        if len(ot) < 20:
            return 0.5
        return float((ot["hs"] > ot["as_"]).mean())

    # ------------------------------------------------------------------------------------------- prediction
    def rates(self, home: str, away: str) -> tuple[float, float, list[str]]:
        flags = []
        h, a = self.idx.get(home), self.idx.get(away)
        ca, cd = self.new_centre
        if h is None:
            flags.append(f"NEW_TEAM_PRIOR:{home}")
        if a is None:
            flags.append(f"NEW_TEAM_PRIOR:{away}")
        att_h = self.att[h] if h is not None else ca
        dfn_h = self.dfn[h] if h is not None else cd
        att_a = self.att[a] if a is not None else ca
        dfn_a = self.dfn[a] if a is not None else cd
        return (float(np.exp(self.c + self.home + att_h + dfn_a)), float(np.exp(self.c + att_a + dfn_h)), flags)

    def grid(self, home: str, away: str) -> tuple[ScoreGrid, list[str]]:
        if not self.fitted:
            raise FitError("model not fitted")
        lh, la, flags = self.rates(home, away)
        if self.p.negbin:
            g = ScoreGrid.negbin(lh, la, self.phi)
        else:
            rho = self.rho if self.p.use_rho else 0.0
            lo, hi = ScoreGrid.rho_domain(lh, la)
            if not (lo < rho < hi):
                flags = flags + ["RHO_CLAMPED"]
            g = ScoreGrid.poisson(lh, la, rho, clamp_rho=True)
        extra = {"p_home_extra": self.p_home_extra, "residual_draw": self.residual_draw,
                 "winner_bonus": self.lg.winner_bonus}
        return apply_tie_rule(g, self.lg, extra), flags

    def parameter_table(self) -> pd.DataFrame:
        return pd.DataFrame({"team": self.teams, "attack": self.att, "defence": self.dfn,
                             "net_log_rate": self.att - self.dfn}).sort_values("net_log_rate", ascending=False)
