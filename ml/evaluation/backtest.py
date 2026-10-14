"""Rolling-origin development backtest (ML_RL_IMPLEMENTATION_FRAMEWORK §9.2).

For every ISO week of a tune or test season, each method is fitted on games strictly before that week's Monday
(00:00, game-date resolution) and then prices the week's regular-season games. Hyperparameters are chosen on the
league's TUNE seasons only and frozen before any TEST season is scored. All results are HISTORICAL_DEVELOPMENT:
the archive has been opened before, so they are not prospective skill (SCORING_AND_VALIDATION §8).
"""
from __future__ import annotations

import itertools
import time
from dataclasses import asdict

import numpy as np
import pandas as pd

from ml.config import League
from ml.core.distributions import normal_crps
from ml.core.metrics import brier, brier_multiclass_half, iso_week, log_loss
from ml.data.archive import load_league, training_frame
from ml.models.baseline import TB1, LeagueBaseline
from ml.models.common import FitError
from ml.models.count import CountParams, PoissonRatings
from ml.models.gaussian import GaussianRatings, GaussParams

GAUSS_GRID = {
    "half_life_days": [45, 90, 180, 365, 730],
    "ridge": [2.0, 8.0, 32.0],
    "cov_inflation": [1.0, 1.1, 1.2, 1.3],
}
COUNT_GRID = {
    "half_life_days": [45, 90, 180, 365, 730],
    "ridge": [1.0, 4.0, 16.0],
}


def week_start(d: pd.Timestamp) -> pd.Timestamp:
    d = pd.Timestamp(d).normalize()
    return d - pd.Timedelta(days=d.weekday())


def make_model(lg: League, params: dict):
    if lg.engine == "gaussian":
        return GaussianRatings(lg, GaussParams(**params))
    if lg.engine not in ("count", "dixon_coles"):
        raise FitError(f"score-grid engine not supported: {lg.engine}")
    return PoissonRatings(lg, CountParams(
        half_life_days=params["half_life_days"], ridge=params["ridge"],
        use_rho=lg.engine == "dixon_coles", negbin=lg.negbin, promoted_prior=lg.promoted_prior))


def _fit_window(all_games: pd.DataFrame, lg: League, season: int, as_of: pd.Timestamp) -> pd.DataFrame:
    tr = training_frame(all_games)
    return tr[(tr["date"] < as_of) & (tr["season"] >= season - lg.history_seasons)]


def _weeks(games: pd.DataFrame):
    g = games.assign(_ws=games["date"].map(week_start))
    for ws, block in g.groupby("_ws", sort=True):
        yield ws, block.drop(columns="_ws")


def _outcome_idx(hs: int, as_: int) -> int:
    return 0 if hs > as_ else (1 if hs == as_ else 2)


# ------------------------------------------------------------------------------------------------ tuning
def _score_params(lg: League, all_games: pd.DataFrame, params: dict) -> tuple[float, int]:
    scores = []
    failed = False
    for season in lg.tune_seasons:
        games = all_games[(all_games["season"] == season) & (all_games["stage"].isin(lg.eval_stages))]
        for ws, block in _weeks(games):
            train = _fit_window(all_games, lg, season, ws)
            try:
                m = make_model(lg, params)
                m.fit(train, ws, season) if lg.engine != "gaussian" else m.fit(train, ws)
            except FitError:
                failed = True
                continue
            for r in block.itertuples():
                if lg.engine == "gaussian":
                    f = m.fast(r.home, r.away)
                    cm = float(normal_crps(f["mu_m"], f["sd_m"], r.hs - r.as_))
                    ct = float(normal_crps(f["mu_t"], f["sd_t"], r.hs + r.as_))
                else:
                    g, _ = m.grid(r.home, r.away)
                    cm, ct = g.crps_margin(r.hs - r.as_), g.crps_total(r.hs + r.as_)
                scores.append(cm + ct)
    return (float(np.mean(scores)) if scores and not failed else np.inf), len(scores)


def _extend(axis: str, values: list, side: str) -> list:
    """One more grid point beyond a boundary: half-lives and ridges move by a factor 2, inflation by 0.1."""
    v = values[0] if side == "low" else values[-1]
    if axis == "cov_inflation":
        nv = round(v - 0.1, 3) if side == "low" else round(v + 0.1, 3)
        if nv <= 0.5:
            return values
    else:
        nv = v / 2 if side == "low" else v * 2
    return sorted(set(values) | {nv})


def tune(lg: League, all_games: pd.DataFrame | None = None, log=print, max_extensions: int = 3) -> tuple[dict, pd.DataFrame]:
    """Grid search on TUNE seasons. Objective: mean margin CRPS + mean total CRPS (both proper).

    Pre-declared boundary rule (framework change 2026-10-14-3): if the best value of an axis lies on that axis's
    grid boundary, the axis is extended by one point beyond it and the search repeats (at most ``max_extensions``
    times per axis). Only tune seasons are scored, so the rule cannot see test results.
    """
    if all_games is None:
        all_games, _ = load_league(lg)
    grid = {k: list(v) for k, v in (GAUSS_GRID if lg.engine == "gaussian" else COUNT_GRID).items()}
    keys = list(grid)
    done: dict[tuple, dict] = {}
    extensions = {k: 0 for k in keys}
    while True:
        for combo in itertools.product(*(grid[k] for k in keys)):
            if combo in done:
                continue
            params = dict(zip(keys, combo))
            t0 = time.time()
            obj, n = _score_params(lg, all_games, params)
            done[combo] = {**params, "objective": obj, "n": n, "seconds": round(time.time() - t0, 1)}
            log(f"  tune {lg.model_id} {params} -> {obj:.4f} (n={n})")
        table = pd.DataFrame(done.values()).sort_values("objective")
        if not np.isfinite(table["objective"]).any():
            raise FitError("no tuning candidate produced complete finite tune-period scores")
        best = {k: table.iloc[0][k] for k in keys}
        changed = False
        for k in keys:
            vals = grid[k]
            side = "low" if best[k] == vals[0] else ("high" if best[k] == vals[-1] else None)
            if side and extensions[k] < max_extensions:
                new_vals = _extend(k, vals, side)
                if new_vals != vals:
                    grid[k], extensions[k], changed = new_vals, extensions[k] + 1, True
        if not changed:
            break
    best = {k: (float(v) if isinstance(v, (float, np.floating, int, np.integer)) else v) for k, v in best.items()}
    table.attrs["extensions"] = extensions
    return best, table


# ---------------------------------------------------------------------------------------------- evaluation
def evaluate(lg: League, params: dict, seasons: tuple[int, ...], all_games: pd.DataFrame | None = None,
             extra_variants: dict | None = None, log=print) -> pd.DataFrame:
    """Price every regular-season game of ``seasons`` with the model, BASELINE_LEAGUE_V1 and TB-1."""
    if all_games is None:
        all_games, _ = load_league(lg)
    variants = {"MODEL": params, **(extra_variants or {})}
    out = []
    for season in seasons:
        games = all_games[(all_games["season"] == season) & (all_games["stage"].isin(lg.eval_stages))]
        earlier = all_games[(all_games["season"] < season) & (all_games["stage"].isin(lg.eval_stages))]
        prev = earlier[earlier["season"] == earlier["season"].max()] if len(earlier) else earlier  # previous edition
        tb1_const = None
        if lg.tb1 is not None and not lg.tb1_label.startswith("VALIDATED"):
            tb1_const = TB1.calibrate(lg, prev)  # competition-specific, previous edition only
        for ws, block in _weeks(games):
            train = _fit_window(all_games, lg, season, ws)
            season_to_date = games[games["date"] < ws]
            fitted = {}
            for name, prm in variants.items():
                try:
                    m = make_model(lg, prm)
                    m.fit(train, ws, season) if lg.engine != "gaussian" else m.fit(train, ws)
                    fitted[name] = m
                except FitError as e:
                    fitted[name] = e
            try:
                base = LeagueBaseline(lg).fit(train)
                bgrid = base.grid()
            except FitError as e:
                base, bgrid = e, None
            try:
                tb1 = TB1(lg, tb1_const).fit(season_to_date, prev, fallback_games=train) if lg.tb1 else None
            except FitError:
                tb1 = None  # TB-1 columns stay missing for these rows; pairs against TB-1 drop them
            line = base.total_line if not isinstance(base, Exception) else np.nan
            for r in block.itertuples():
                margin, total = r.hs - r.as_, r.hs + r.as_
                y_home = float(margin > 0)
                y_over = float(total > line) if np.isfinite(line) else np.nan
                oi = _outcome_idx(r.hs, r.as_)
                row = {"league": lg.competition, "season": season, "date": r.date, "week": None, "event_id": r.event_id,
                       "home": r.home, "away": r.away, "hs": r.hs, "as_": r.as_, "fit_date": ws,
                       "n_train": len(train), "league_median_line": line}
                for name, m in fitted.items():
                    if isinstance(m, Exception):
                        row[f"{name}_status"] = f"NOT_ISSUED:FIT_FAILED:{m}"
                        continue
                    g, flags = m.grid(r.home, r.away)
                    pw, pd_, pl = g.winner()
                    s = g.summary()
                    row.update({
                        f"{name}_status": "FROZEN" + (f"|{';'.join(flags)}" if flags else ""),
                        f"{name}_p_home": pw, f"{name}_p_draw": pd_, f"{name}_p_away": pl,
                        f"{name}_p_over": g.total(line).win if np.isfinite(line) else np.nan,
                        f"{name}_crps_margin": g.crps_margin(margin), f"{name}_crps_total": g.crps_total(total),
                        f"{name}_mean_home": s["mean_home"], f"{name}_mean_away": s["mean_away"],
                        f"{name}_sd_margin": s["sd_margin"], f"{name}_sd_total": s["sd_total"],
                    })
                if bgrid is not None:
                    pw, pd_, pl = bgrid.winner()
                    row.update({"BASE_p_home": pw, "BASE_p_draw": pd_, "BASE_p_away": pl,
                                "BASE_p_over": bgrid.total(line).win,
                                "BASE_crps_margin": bgrid.crps_margin(margin), "BASE_crps_total": bgrid.crps_total(total)})
                if tb1 is not None:
                    cm, ct = tb1.crps(r.home, r.away, margin, total)
                    row.update({"TB1_p_home": tb1.p_home_win(r.home, r.away),
                                "TB1_p_over": tb1.p_over(r.home, r.away, line), "TB1_crps_margin": cm,
                                "TB1_crps_total": ct})
                    if lg.tb1.poisson:
                        pw, pd_, pl = tb1.grid(r.home, r.away).winner()
                        row.update({"TB1_p_draw": pd_, "TB1_p_away": pl})
                row["y_home"], row["y_over"], row["outcome_idx"] = y_home, y_over, oi
                out.append(row)
        log(f"  evaluated {lg.model_id} {season}: {sum(1 for x in out if x['season'] == season)} games")
    df = pd.DataFrame(out)
    if df.empty:
        raise FitError("no evaluation-stage games in the requested seasons")
    df["week"] = iso_week(df["date"])
    for pref in ["MODEL", *(extra_variants or {}), "BASE", "TB1"]:
        if f"{pref}_p_home" in df:
            df[f"{pref}_brier_home"] = brier(df[f"{pref}_p_home"], df["y_home"])
            df[f"{pref}_logloss_home"] = log_loss(df[f"{pref}_p_home"], df["y_home"], eps=1e-12)
            df[f"{pref}_brier_over"] = brier(df[f"{pref}_p_over"], df["y_over"])
            if f"{pref}_p_draw" in df and lg.tie_rule == "draw":
                probs = df[[f"{pref}_p_home", f"{pref}_p_draw", f"{pref}_p_away"]].to_numpy()
                df[f"{pref}_brier_3way"] = brier_multiclass_half(probs, df["outcome_idx"].to_numpy())
    return df


def params_record(lg: League, params: dict) -> dict:
    return {"league": lg.path, "engine": lg.engine, "endpoint": lg.endpoint, "tie_rule": lg.tie_rule,
            "history_seasons": lg.history_seasons, "tune_seasons": list(lg.tune_seasons),
            "test_seasons": list(lg.test_seasons), **params}
