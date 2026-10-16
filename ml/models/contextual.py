"""Competition-local contextual models of FINAL endpoints, not regulation-plus-final scores.

The count branch fits final-score log means; the points branch fits joint final scores.
Baseball's winner class is fitted separately and coherently raked onto the final-score
grid: home wins are not inferred from uncensored nine-inning run means. This is an
experimental final-score approximation, not an inning simulator or a calibrated model.
"""
from __future__ import annotations

import math
import numpy as np
import pandas as pd
from scipy import optimize, special

from ml import primary as p
from ml.core.distributions import ScoreGrid
from ml.models.common import FitError

SPEC = "CONTEXT_FINAL_V1"
# Predeclared sport-family starting recipes, NOT tuned or validated parameters.
RECIPES = {
    "Basketball": (45., 180., 12.), "AFL": (180., 540., 8.),
    "State Level AFL": (180., 540., 8.), "Australian Rules": (180., 540., 8.),
    "American Football": (180., 730., 16.), "College Football": (180., 730., 16.),
    "Canadian Football": (180., 730., 16.), "Rugby League": (90., 365., 12.),
    "Rugby Union": (180., 540., 12.), "Soccer": (180., 730., 16.),
    "Ice Hockey": (90., 365., 24.), "Baseball": (90., 365., 32.),
}
CONTEXT = tuple(f"{s}_{v}" for s in ("home", "away") for v in
                ("rest_days", "L5_net", "L10_net", "L20_net", "L10_pace", "confirmed_out",
                 "confirmed_starters", "lineup_confirmed"))


def supported(competition, endpoint):
    sport = competition.split("/", 1)[0]
    from ml.config import SPORT_RULES
    return sport in RECIPES and endpoint == SPORT_RULES.get(sport, {}).get("endpoint")


class ContextModel:
    def __init__(self, competition, endpoint, half_life, ridge, *, baseline=False):
        if not supported(competition, endpoint):
            raise p.AdmissionError("unsupported exact competition/endpoint adapter")
        self.competition, self.endpoint = competition, endpoint
        self.sport = competition.split("/", 1)[0]
        self.half_life, self.ridge, self.baseline = half_life, ridge, baseline
        self.count = self.sport in ("Soccer", "Ice Hockey", "Baseball")
        self.no_draw = endpoint in ("FULL_GAME_INCL_OT", "FULL_GAME_INCL_OT_SO", "FULL_GAME_INCL_EXTRAS") and self.sport not in ("American Football", "Canadian Football", "College Football")

    def _design(self, rows, fit=False):
        if fit:
            self.teams = sorted(set(rows.home) | set(rows.away))
            self.venues = sorted(set(rows.venue) - {""}) if "venue" in rows else []
            self.context = []
            self.centres, self.scales = {}, {}
            names = list(CONTEXT) + ['neutral_venue'] + sorted(c for c in rows if c.startswith(("home_player_", "away_player_")))
            for name in names:
                x = pd.to_numeric(rows[name], errors="coerce") if name in rows else pd.Series(np.nan, index=rows.index)
                # A feature never observed at a historical issue cannot acquire an invented effect.
                if x.notna().sum() >= 5 and x.std() > 0:
                    self.context.append(name)
                    self.centres[name], self.scales[name] = float(x.mean()), float(x.std())
        cols = [np.ones(len(rows))]
        if not self.baseline:
            for side in ("home", "away"):
                cols += [(rows[side] == team).to_numpy(float) for team in self.teams]
            cols += [(rows.venue == v).to_numpy(float) for v in self.venues]
            for name in self.context:
                x = pd.to_numeric(rows[name], errors="coerce") if name in rows else pd.Series(np.nan, index=rows.index)
                cols += [((x.fillna(self.centres[name])-self.centres[name])/self.scales[name]).to_numpy(), x.isna().to_numpy(float)]
        return np.column_stack(cols)

    def fit(self, rows, horizon):
        if len(rows) < 30:
            raise FitError(f"only {len(rows)} reviewed final-endpoint training events; need 30")
        horizon = p.clock(horizon)
        dates = rows.event_at.map(p.clock)
        if (dates >= horizon.normalize()).any() or (rows.label_available_at.map(p.clock) > horizon).any():
            raise FitError("future event/label in fit")
        if self.no_draw and (rows.hs.astype(float) == rows.as_.astype(float)).any():
            raise FitError("final endpoint prohibits drawn results; resolve endpoint/source")
        self.weights = np.power(.5, (horizon-dates).dt.total_seconds().to_numpy()/86400/self.half_life)
        self.weights /= self.weights.mean()
        X = self._design(rows, True)
        y = rows[["hs", "as_"]].to_numpy(float)
        if not np.isfinite(y).all() or np.any(y < 0):
            raise FitError("invalid endpoint labels")
        transformed = np.log1p(y) if self.count else y
        penalty = np.eye(X.shape[1])*self.ridge
        penalty[0, 0] = 0
        try:
            self.beta = np.linalg.solve(X.T @ (X*self.weights[:,None])+penalty, X.T @ (transformed*self.weights[:,None]))
        except np.linalg.LinAlgError as exc:
            raise FitError("singular contextual design") from exc
        residual = transformed-X@self.beta
        self.smear = np.average(np.exp(residual), weights=self.weights, axis=0) if self.count else np.ones(2)
        residual_score = y-(np.exp(X@self.beta)*self.smear-1 if self.count else X@self.beta)
        self.cov = np.cov(residual_score.T, aweights=self.weights)+np.eye(2)*.25
        self.phi = max(0., float(np.mean((np.diag(self.cov)-y.mean(axis=0))/np.maximum(y.mean(axis=0),.1)**2))) if self.count else 0
        # All final-score dependence, including walk-off home-win censoring, is learned in this class model.
        win = (y[:,0] > y[:,1]).astype(float)
        def objective(b):
            z = X@b
            return float(np.sum(self.weights*(np.logaddexp(0,z)-win*z))+.5*b@penalty@b), X.T@(self.weights*(special.expit(z)-win))+penalty@b
        result = optimize.minimize(objective, np.zeros(X.shape[1]), jac=True, method="L-BFGS-B")
        if not result.success or not np.isfinite(result.x).all():
            raise FitError("winner-class contextual fit failed: "+result.message)
        self.win_beta = result.x
        self.draw_share = float(np.average(y[:,0]==y[:,1], weights=self.weights))
        self.n = len(rows)
        return self

    def grid(self, row):
        if len(row) != 1:
            raise FitError("one exact event required")
        if not self.baseline and (row.home.iloc[0] not in self.teams or row.away.iloc[0] not in self.teams):
            raise FitError("unseen participant; explicit cold-start model not admitted")
        X = self._design(row)
        mu = (np.exp(X@self.beta)*self.smear-1 if self.count else X@self.beta)[0]
        mu = np.maximum(mu, .1)
        grid = ScoreGrid.negbin(*mu, self.phi) if self.count else ScoreGrid.bivariate_normal(*mu, self.cov*1.1)
        if self.no_draw or self.sport == "Baseball":
            masses=grid.winner()
            home = float(special.expit((X@self.win_beta)[0])) if self.sport == "Baseball" else masses[0]/(masses[0]+masses[2])
            draw = 0. if self.no_draw else self.draw_share
            home = min(home, 1-draw)
            grid = grid.reweight_winner((home, draw, 1-home-draw))
        return grid

    def parameters(self, arm):
        # Numeric fitted state is retained as CSV, rather than an unsafe pickle.
        rows = [dict(arm=arm, component="score", row=i, col=j, value=float(v))
                for (i,j),v in np.ndenumerate(self.beta)]
        rows += [dict(arm=arm, component="winner", row=i, col=0, value=float(v)) for i,v in enumerate(self.win_beta)]
        rows += [dict(arm=arm, component="covariance", row=i, col=j, value=float(v)) for (i,j),v in np.ndenumerate(self.cov)]
        rows += [dict(arm=arm, component="smearing", row=i, col=0, value=float(v)) for i,v in enumerate(self.smear)]
        rows += [dict(arm=arm, component="dispersion", row=0, col=0, value=self.phi)]
        columns=['intercept']
        if not self.baseline:
            columns += [s+':'+t for s in ('home','away') for t in self.teams]+['venue:'+v for v in self.venues]
            columns += [v for name in self.context for v in (name,name+'__missing')]
        rows += [dict(arm=arm, component="design_column", row=i, col=0, value=name) for i,name in enumerate(columns)]
        for i,name in enumerate(self.context):
            rows += [dict(arm=arm, component='centre:'+name,row=i,col=0,value=self.centres[name]),dict(arm=arm,component='scale:'+name,row=i,col=0,value=self.scales[name])]
        return rows
