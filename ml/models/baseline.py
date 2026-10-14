"""The two comparators every model row is scored against.

BASELINE_LEAGUE_V1 (SELECTION_RULES §9): league-only. Home and away score levels and their covariance from the
training window, with no team, lineup, recent-form or event-result inputs. Same distribution family and the
same endpoint/tie rule as the candidate.

TB-1 (PROBABILITY_TOOLKIT §4): season-to-date points for/against with k-shrinkage, the toolkit's fixed widths
and home edge, coded exactly as the hand procedure. Its constants were partly measured in seasons that are
test seasons here, which can only flatter TB-1, so comparisons against it are conservative for the model.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from ml.config import League
from ml.core.distributions import ScoreGrid, normal_crps
from ml.models.common import FitError, apply_tie_rule, normal_extra, residual_draw_share


class LeagueBaseline:
    name = "BASELINE_LEAGUE_V1"

    def __init__(self, lg: League):
        self.lg = lg

    def fit(self, train: pd.DataFrame) -> "LeagueBaseline":
        if len(train) < 30:
            raise FitError("too few games for the league baseline")
        if self.lg.tie_rule == "hockey_regulation":
            yh, ya = train["reg_hs"].to_numpy(float), train["reg_as"].to_numpy(float)
        else:
            yh, ya = train["hs"].to_numpy(float), train["as_"].to_numpy(float)
        self.mh, self.ma = float(yh.mean()), float(ya.mean())
        self.cov = np.cov(np.vstack([yh, ya]))
        if not np.isfinite(yh).all() or not np.isfinite(ya).all() or min(self.mh, self.ma) <= 0:
            raise FitError("league baseline needs finite positive score means")
        if self.lg.engine == "gaussian" and (not np.isfinite(self.cov).all() or np.linalg.eigvalsh(self.cov).min() <= 0):
            raise FitError("league baseline covariance is not positive definite")
        self.sd_margin = float(np.sqrt(self.cov[0, 0] + self.cov[1, 1] - 2 * self.cov[0, 1]))
        self.residual_draw = residual_draw_share(train, self.sd_margin)
        if self.lg.engine in ("dixon_coles", "count"):
            self.phi = 0.0
            if self.lg.negbin:
                v = (yh.var() + ya.var()) / 2
                m = (self.mh + self.ma) / 2
                self.phi = float(max((v - m) / (m * m), 0.0))
            if self.lg.tie_rule == "hockey_regulation":
                ot = train[train["decision"].isin(["Overtime", "Shootout"])]
            elif self.lg.tie_rule == "extras":
                ot = train[train["decision"] == "EXTRAS"]
            else:
                ot = train.iloc[:0]
            self.p_home_extra = float((ot["hs"] > ot["as_"]).mean()) if len(ot) >= 20 else 0.5
        self.draw_rate = float((train["hs"] == train["as_"]).mean())
        totals = (train["hs"] + train["as_"]).to_numpy(float)
        self.total_line = float(np.floor(np.median(totals)) + 0.5)
        return self

    def grid(self) -> ScoreGrid:
        if self.lg.engine in ("dixon_coles", "count"):
            g = ScoreGrid.negbin(self.mh, self.ma, self.phi) if self.lg.negbin else ScoreGrid.poisson(self.mh, self.ma)
            tie = g.winner()[1]
            draws = self.draw_rate
            rd = float(np.clip(draws / tie, 0, 1)) if (tie > 0 and self.lg.tie_rule != "draw") else 0.0
            return apply_tie_rule(g, self.lg, {"p_home_extra": self.p_home_extra, "residual_draw": rd,
                                               "winner_bonus": self.lg.winner_bonus})
        g = ScoreGrid.bivariate_normal(self.mh, self.ma, self.cov)
        extra = normal_extra(self.lg, self.mh - self.ma, self.sd_margin, self.mh + self.ma, self.residual_draw)
        return apply_tie_rule(g, self.lg, extra)


class TB1:
    """Season-to-date team baseline by hand (PROBABILITY_TOOLKIT §4.2), vectorised over one fit date."""

    name = "TB1"

    def __init__(self, lg: League, constants=None):
        if lg.tb1 is None and constants is None:
            raise FitError(f"no TB-1 constants for {lg.code}")
        self.lg = lg
        self.c = constants or lg.tb1

    @staticmethod
    def calibrate(lg: League, previous_edition: pd.DataFrame, min_games: int = 30):
        """Competition-specific TB-1 constants for a league the toolkit does not list (§4.3 'Other competitions').

        k stays the nearest sport's. The home edge is the previous edition's mean home margin (the toolkit's own
        refresh rule). The widths are the root-mean-square errors of TB-1 replayed game by game through that edition,
        each game priced from that edition's games before it. Only earlier data is used. Returns None if the edition
        is too small, and the caller keeps the nearest sport's constants.
        """
        from ml.config import TB1 as TB1C

        base = lg.tb1
        if base is None or len(previous_edition) < min_games:
            return None
        g = previous_edition.sort_values("date")
        he = float((g["hs"] - g["as_"]).mean())
        if base.poisson:
            return TB1C(base.k, None, None, he, poisson=True)
        pf, pa, n = {}, {}, {}
        tot_pts = tot_n = 0
        em, et = [], []
        for r in g.itertuples():
            if tot_n > 0:
                lm = tot_pts / tot_n

                def rate(t):
                    nn = n.get(t, 0)
                    return ((pf.get(t, 0) + base.k * lm) / (nn + base.k), (pa.get(t, 0) + base.k * lm) / (nn + base.k))

                (oh, dh), (oa, da) = rate(r.home), rate(r.away)
                t_pred = (oh + da) / 2 + (oa + dh) / 2
                m_pred = ((oh - dh) - (oa - da)) / 2 + he
                em.append(r.hs - r.as_ - m_pred)
                et.append(r.hs + r.as_ - t_pred)
            for team, f, a in ((r.home, r.hs, r.as_), (r.away, r.as_, r.hs)):
                pf[team] = pf.get(team, 0) + f
                pa[team] = pa.get(team, 0) + a
                n[team] = n.get(team, 0) + 1
            tot_pts += r.hs + r.as_
            tot_n += 2
        if len(em) < min_games:
            return None
        return TB1C(base.k, float(np.sqrt(np.mean(np.square(em)))), float(np.sqrt(np.mean(np.square(et)))), he)

    def fit(self, season_games: pd.DataFrame, previous_season: pd.DataFrame,
            fallback_games: pd.DataFrame | None = None) -> "TB1":
        """``season_games``: this season's evaluation-stage games before the fit date. League mean: season to date,
        else the previous edition, else the fit's training window (always earlier data)."""
        pf, pa, n = {}, {}, {}
        for r in season_games.itertuples():
            pf[r.home] = pf.get(r.home, 0) + r.hs
            pa[r.home] = pa.get(r.home, 0) + r.as_
            pf[r.away] = pf.get(r.away, 0) + r.as_
            pa[r.away] = pa.get(r.away, 0) + r.hs
            n[r.home] = n.get(r.home, 0) + 1
            n[r.away] = n.get(r.away, 0) + 1
        if sum(n.values()) > 0:
            lm = sum(pf.values()) / sum(n.values())
        elif len(previous_season):
            lm = float((previous_season["hs"].sum() + previous_season["as_"].sum()) / (2 * len(previous_season)))
        elif fallback_games is not None and len(fallback_games):
            lm = float((fallback_games["hs"].sum() + fallback_games["as_"].sum()) / (2 * len(fallback_games)))
        else:
            raise FitError("no league mean available for TB-1")
        self.pf, self.pa, self.n, self.lm = pf, pa, n, lm
        return self

    def ratings(self, team: str) -> tuple[float, float]:
        k, lm = self.c.k, self.lm
        n = self.n.get(team, 0)
        o = (self.pf.get(team, 0) + k * lm) / (n + k)
        d = (self.pa.get(team, 0) + k * lm) / (n + k)
        return o, d

    def summary(self, home: str, away: str) -> dict:
        oh, dh = self.ratings(home)
        oa, da = self.ratings(away)
        t = (oh + da) / 2 + (oa + dh) / 2
        m = ((oh - dh) - (oa - da)) / 2 + self.c.home_edge
        return {"T": t, "M": m}

    def p_home_win(self, home: str, away: str) -> float:
        s = self.summary(home, away)
        if self.c.poisson:
            return self.grid(home, away).winner()[0]
        return float(stats.norm.cdf(s["M"] / self.c.sd_margin))

    def grid(self, home: str, away: str) -> ScoreGrid:
        s = self.summary(home, away)
        lh = max((s["T"] + s["M"]) / 2, 0.05)
        la = max((s["T"] - s["M"]) / 2, 0.05)
        return ScoreGrid.poisson(lh, la)

    def p_over(self, home: str, away: str, line: float) -> float:
        if self.c.poisson:
            return self.grid(home, away).total(line).win
        s = self.summary(home, away)
        return float(1 - stats.norm.cdf((line - s["T"]) / self.c.sd_total))

    def crps(self, home: str, away: str, margin: int, total: int) -> tuple[float, float]:
        if self.c.poisson:
            g = self.grid(home, away)
            return g.crps_margin(margin), g.crps_total(total)
        s = self.summary(home, away)
        return (float(normal_crps(s["M"], self.c.sd_margin, margin)), float(normal_crps(s["T"], self.c.sd_total, total)))
