"""Limited-overs first-innings totals (any T20 or one-day competition): the C0 -> C1 -> C2 ladder (ML_RL_IMPLEMENTATION_FRAMEWORK §8.4).

Contract: runs of the team batting first in a full-length innings (the competition's overs cap bowled, or all out). Rows with a
weather or DLS method, or a short first innings that was not all out, are excluded and counted.

C0  league only:   y ~ N(mu, sigma), time-decayed mean and SD of the competition's recent first innings.
C1  + venue:       mu + v[venue], v shrunk by n_eff / (n_eff + k_venue).
C2  + teams:       mu + v[venue] + bat[batting team] + bowl[bowling team], weighted ridge.
C2_PRE uses the declared symmetric scenario 0.5 * F(A bats) + 0.5 * F(B bats).
The weight is an unfitted assumption: a fair toss alone does not imply equal batting-first probabilities
when the two teams' toss decisions differ. This prototype is not a verified pre-toss production model.
"""
from __future__ import annotations

import csv
import re
from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy import stats

from ml.config import ARCHIVE
from ml.core.distributions import normal_crps
from ml.models.common import FitError, decay_weights

SUPPORT = np.arange(0, 601)


def _venue_key(v: str) -> str:
    return re.sub(r"\s+", " ", (v or "").split(",")[0].strip().lower())


def load_cricket(lg) -> tuple[pd.DataFrame, dict]:
    """First innings of any limited-overs competition (lg.overs_cap overs, e.g. 20 for T20, 50 for one-day)."""
    c = lg.columns
    rows, dropped = [], {}

    def drop(k):
        dropped[k] = dropped.get(k, 0) + 1

    for f in sorted((ARCHIVE / lg.path).glob("*/*_games.csv")):
        if not f.parent.name.isdigit():
            continue
        with open(f, newline="", encoding="utf-8-sig", errors="replace") as fh:
            for r in csv.DictReader(fh):
                method = (r.get(c["method"]) or "").strip() if c["method"] else ""
                if method not in ("", "Normal", "N/A"):
                    drop(f"method:{method}")
                    continue
                try:
                    runs = int(float(r[c["fi_runs"]]))
                    wk = int(float(r[c["fi_wkts"]]))
                    overs = float(re.sub(r"[^0-9.]", "", r[c["fi_overs"]] or "") or "nan")
                except (ValueError, KeyError, TypeError):
                    drop("unparsed_first_innings")
                    continue
                if not (overs >= lg.overs_cap or wk == 10):
                    drop("short_first_innings")
                    continue
                bat = lg.aliases.get((r.get(c["fi_team"]) or "").strip(), (r.get(c["fi_team"]) or "").strip())
                bowl = lg.aliases.get((r.get(c["si_team"]) or "").strip(), (r.get(c["si_team"]) or "").strip())
                date = pd.to_datetime(r.get(c["date"]), errors="coerce") if c["date"] else pd.NaT
                if pd.isna(date) or not bat or not bowl or bat == bowl:
                    drop("invalid_identity_or_date")
                    continue
                season = int(f.parent.name)
                rows.append({"season": season, "date": date,
                             "event_id": (r.get(c["id"]) or "").strip() or f"{lg.model_id}:{date.date()}:{bat}:{bowl}",
                             "bat": bat, "bowl": bowl, "venue": _venue_key(r.get(c["venue"] or "", "")),
                             "runs": runs})
    df = pd.DataFrame(rows).drop_duplicates("event_id").sort_values(["date", "event_id"]).reset_index(drop=True)
    return df, dropped


@dataclass(frozen=True)
class CricketParams:
    half_life_days: float
    ridge: float
    k_venue: float
    sd_inflation: float


class FirstInningsModel:
    def __init__(self, level: str, p: CricketParams):
        if level not in ("C0", "C1", "C2"):
            raise ValueError(level)
        self.level = level
        self.p = p

    def fit(self, train: pd.DataFrame, as_of: pd.Timestamp) -> "FirstInningsModel":
        if len(train) < 40:
            raise FitError("too few first innings")
        w = decay_weights(train["date"], as_of, self.p.half_life_days)
        y = train["runs"].to_numpy(float)
        self.mu = float(np.average(y, weights=w))
        self.venue = {}
        self.bat, self.bowl = {}, {}
        resid = y - self.mu
        if self.level in ("C1", "C2"):
            for v, g in train.assign(_r=resid, _w=w).groupby("venue"):
                sw = g["_w"].sum()
                self.venue[v] = float((g["_w"] * g["_r"]).sum() / (sw + self.p.k_venue))
            resid = resid - train["venue"].map(self.venue).fillna(0.0).to_numpy()
        if self.level == "C2":
            teams = sorted(set(train["bat"]) | set(train["bowl"]))
            ix = {t: i for i, t in enumerate(teams)}
            T = len(teams)
            X = np.zeros((len(train), 2 * T))
            X[np.arange(len(train)), train["bat"].map(ix).to_numpy()] = 1
            X[np.arange(len(train)), T + train["bowl"].map(ix).to_numpy()] = 1
            A = X.T @ (X * w[:, None]) + self.p.ridge * np.eye(2 * T)
            beta = np.linalg.solve(A, X.T @ (w * resid))
            self.bat = {t: float(beta[ix[t]]) for t in teams}
            self.bowl = {t: float(beta[T + ix[t]]) for t in teams}
            resid = resid - X @ beta
        self.sigma = float(np.sqrt(np.average(resid ** 2, weights=w))) * self.p.sd_inflation
        if not np.isfinite(self.sigma) or self.sigma <= 0:
            raise FitError("invalid first-innings SD")
        self.line = float(np.floor(np.median(y[-120:])) + 0.5)
        return self

    def mean(self, bat: str, bowl: str, venue: str) -> float:
        return self.mu + self.venue.get(venue, 0.0) + self.bat.get(bat, 0.0) + self.bowl.get(bowl, 0.0)

    def pmf(self, bat: str, bowl: str, venue: str) -> np.ndarray:
        m = self.mean(bat, bowl, venue)
        c = stats.norm.cdf((np.append(SUPPORT, SUPPORT[-1] + 1) - 0.5 - m) / self.sigma)
        p = np.diff(c)
        return p / p.sum()


def discrete_scores(pmf: np.ndarray, y: int, line: float) -> dict:
    cdf = np.cumsum(pmf)
    crps = float(np.sum((cdf - (SUPPORT >= y)) ** 2))
    p_over = float(pmf[SUPPORT > line].sum())
    lo = int(SUPPORT[np.searchsorted(cdf, 0.10)])
    hi = int(SUPPORT[np.searchsorted(cdf, 0.90)])
    pit = float(cdf[y - 1] if y > 0 else 0.0) + 0.5 * float(pmf[y])
    return {"crps": crps, "p_over": p_over, "in80": float(lo <= y <= hi), "pit": pit}


def tune_and_evaluate(lg, log=print):
    seasons_tune, seasons_test = lg.tune_seasons, lg.test_seasons
    df, dropped = load_cricket(lg)
    def run(params: CricketParams, seasons, levels=("C0", "C1", "C2")):
        out = []
        for season in seasons:
            games = df[df["season"] == season]
            for d, block in games.groupby("date"):
                train = df[(df["date"] < d) & (df["season"] >= season - 4)]
                fitted = {lv: FirstInningsModel(lv, params).fit(train, d) for lv in levels}
                line = fitted[levels[0]].line
                for r in block.itertuples():
                    row = {"season": season, "date": d, "event_id": r.event_id, "bat": r.bat, "bowl": r.bowl,
                           "venue": r.venue, "runs": r.runs, "line": line, "y_over": float(r.runs > line)}
                    for lv, m in fitted.items():
                        sc = discrete_scores(m.pmf(r.bat, r.bowl, r.venue), r.runs, line)
                        row.update({f"{lv}_{k}": v for k, v in sc.items()})
                        row[f"{lv}_mean"] = m.mean(r.bat, r.bowl, r.venue)
                        row[f"{lv}_sigma"] = m.sigma
                    if "C2" in fitted:
                        m = fitted["C2"]
                        mix = 0.5 * m.pmf(r.bat, r.bowl, r.venue) + 0.5 * m.pmf(r.bowl, r.bat, r.venue)
                        sc = discrete_scores(mix, r.runs, line)
                        row.update({f"C2PRE_{k}": v for k, v in sc.items()})
                    out.append(row)
        res = pd.DataFrame(out)
        for lv in [*levels, *(["C2PRE"] if "C2" in levels else [])]:
            res[f"{lv}_brier_over"] = (res[f"{lv}_p_over"] - res["y_over"]) ** 2
        return res

    axes = {"half_life_days": [365.0, 730.0, 1460.0], "ridge": [5.0, 20.0, 80.0], "k_venue": [5.0, 20.0],
            "sd_inflation": [1.0, 1.1]}
    done, ext = {}, {k: 0 for k in axes}
    while True:  # same pre-declared boundary rule as backtest.tune: extend an axis whose best value is on its edge
        for combo in __import__("itertools").product(*axes.values()):
            if combo not in done:
                prm = CricketParams(*combo)
                done[combo] = {**prm.__dict__, "objective": run(prm, seasons_tune, levels=("C2",))["C2_crps"].mean()}
        tune_table = pd.DataFrame(done.values()).sort_values("objective")
        top = tune_table.iloc[0]
        changed = False
        for k, vals in axes.items():
            side = "low" if top[k] == vals[0] else ("high" if top[k] == vals[-1] else None)
            if side and ext[k] < 2:
                step = 0.1 if k == "sd_inflation" else None
                nv = (vals[0] - step if side == "low" else vals[-1] + step) if step else (vals[0] / 2 if side == "low" else vals[-1] * 2)
                if nv > 0.5 if step else nv > 0:
                    axes[k] = sorted(set(vals) | {round(nv, 3)})
                    ext[k] += 1
                    changed = True
        if not changed:
            break
    best = CricketParams(**{k: float(top[k]) for k in ("half_life_days", "ridge", "k_venue", "sd_inflation")})
    log(f"  {lg.model_id} best params {best}")
    test = run(best, seasons_test)
    return {"data": df, "dropped": dropped, "tune_table": tune_table, "params": best, "test": test}
