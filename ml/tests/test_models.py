"""Model fitting, leakage and failure-behaviour checks (C-ML-06, C-ML-11, C-ML-12, C-ML-13, C-ML-15)."""
import numpy as np
import pandas as pd
import pytest

from ml.config import League

SOCCER = League(path="Soccer/X", sport="Soccer", competition="X", model_id="SOC-X-DC-r1", engine="dixon_coles",
                tie_rule="draw")
BASKET = League(path="Basketball/Y", sport="Basketball", competition="Y", model_id="BKB-Y-JOINT-r1",
                engine="gaussian", tie_rule="overtime", extra_fraction=5 / 48)
from ml.models.common import FitError, decay_weights
from ml.models.count import CountParams, PoissonRatings
from ml.models.gaussian import GaussianRatings, GaussParams


def synthetic(n_teams=12, seasons=(2020, 2021), seed=1, kind="poisson"):
    rng = np.random.default_rng(seed)
    teams = [f"T{i:02d}" for i in range(n_teams)]
    att = rng.normal(0, 0.25 if kind == "poisson" else 4, n_teams)
    dfn = rng.normal(0, 0.25 if kind == "poisson" else 4, n_teams)
    rows = []
    day = pd.Timestamp("2020-01-01")
    for s in seasons:
        for rep in range(2):
            for i in range(n_teams):
                for j in range(n_teams):
                    if i == j:
                        continue
                    day += pd.Timedelta(hours=7)
                    if kind == "poisson":
                        hs = rng.poisson(np.exp(0.3 + 0.25 + att[i] + dfn[j]))
                        as_ = rng.poisson(np.exp(0.3 + att[j] + dfn[i]))
                    else:
                        hs = int(round(100 + 2 + att[i] + dfn[j] + rng.normal(0, 11)))
                        as_ = int(round(100 + att[j] + dfn[i] + rng.normal(0, 11)))
                    rows.append({"league": "X", "season": s, "date": day.normalize(), "stage": "REG",
                                 "event_id": f"{s}-{rep}-{i}-{j}", "home": teams[i], "away": teams[j], "hs": hs,
                                 "as_": as_, "reg_hs": hs, "reg_as": as_, "decision": ""})
    return pd.DataFrame(rows), dict(zip(teams, att)), dict(zip(teams, dfn))


def test_dixon_coles_recovers_ratings():
    df, att, dfn = synthetic()
    m = PoissonRatings(SOCCER, CountParams(10_000, 0.5, use_rho=True))
    m.fit(df, df["date"].max() + pd.Timedelta(days=1))
    est = m.parameter_table().set_index("team")
    assert np.corrcoef([att[t] for t in est.index], est["attack"])[0, 1] > 0.85
    assert m.home == pytest.approx(0.25, abs=0.08)


def test_gaussian_recovers_ratings_and_home_edge():
    df, att, dfn = synthetic(kind="normal")
    m = GaussianRatings(BASKET, GaussParams(10_000, 1.0, 1.0))
    m.fit(df, df["date"].max() + pd.Timedelta(days=1))
    est = m.parameter_table().set_index("team")
    assert np.corrcoef([att[t] - dfn[t] for t in est.index], est["net_margin_vs_average"])[0, 1] > 0.9
    assert m.mu_h - m.mu_a == pytest.approx(2.0, abs=0.8)


# C-ML-06 known-at: a training row on or after the fit date is refused
def test_c_ml_06_rejects_same_date_training_row():
    dates = pd.Series(pd.to_datetime(["2024-01-01", "2024-01-05"]))
    with pytest.raises(FitError):
        decay_weights(dates, pd.Timestamp("2024-01-04"), 100)


def test_c_ml_06_previous_day_is_fine():
    w = decay_weights(pd.Series(pd.to_datetime(["2024-01-03"])), pd.Timestamp("2024-01-04"), 100)
    assert 0 < w[0] < 1


# C-ML-11 no silent fallback
def test_c_ml_11_too_little_data_raises():
    df, _, _ = synthetic()
    with pytest.raises(FitError):
        GaussianRatings(BASKET, GaussParams(100, 1, 1)).fit(df.head(10), df["date"].max() + pd.Timedelta(days=1))


# C-ML-12 unknown team gets an explicit labelled prior, never a silent default
def test_c_ml_12_new_team_is_flagged():
    df, _, _ = synthetic()
    m = PoissonRatings(SOCCER, CountParams(365, 2.0, use_rho=True)).fit(df, df["date"].max() + pd.Timedelta(days=1))
    _, flags = m.grid("NEWCOMER", "T01")
    assert flags == ["NEW_TEAM_PRIOR:NEWCOMER"]


# C-ML-13 calibration is fitted on an earlier season only
def test_c_ml_13_calibrator_ignores_current_season_labels():
    from ml.evaluation.report import platt_by_previous_season
    rng = np.random.default_rng(0)
    n = 400
    p = rng.uniform(0.2, 0.8, n)
    y = (rng.uniform(size=n) < p).astype(float)
    base = pd.DataFrame({"season": [2023] * n + [2024] * n, "MODEL_p_home": np.r_[p, p], "y_home": np.r_[y, y],
                         "event_id": range(2 * n), "week": [f"W{i % 20}" for i in range(2 * n)]})
    base["MODEL_brier_home"] = (base["MODEL_p_home"] - base["y_home"]) ** 2
    flipped = base.copy()
    flipped.loc[flipped["season"] == 2024, "y_home"] = 1 - flipped.loc[flipped["season"] == 2024, "y_home"]
    flipped["MODEL_brier_home"] = (flipped["MODEL_p_home"] - flipped["y_home"]) ** 2
    a = platt_by_previous_season(base, "MODEL", (2024,))
    b = platt_by_previous_season(flipped, "MODEL", (2024,))
    assert a["slope"].iloc[0] == pytest.approx(b["slope"].iloc[0])


# C-ML-15 pre-toss mixture
def test_c_ml_15_pre_toss_mixture_is_a_distribution():
    from ml.models.cricket import CricketParams, FirstInningsModel
    rng = np.random.default_rng(3)
    teams = ["A", "B", "C", "D"]
    rows = [{"date": pd.Timestamp("2023-01-01") + pd.Timedelta(days=i), "bat": teams[i % 4], "bowl": teams[(i + 1) % 4],
             "venue": "v", "runs": int(rng.normal(170, 25))} for i in range(120)]
    df = pd.DataFrame(rows)
    m = FirstInningsModel("C2", CricketParams(365, 10, 10, 1.0)).fit(df, pd.Timestamp("2024-01-01"))
    mix = 0.5 * m.pmf("A", "B", "v") + 0.5 * m.pmf("B", "A", "v")
    assert mix.sum() == pytest.approx(1.0)
    assert m.pmf("A", "B", "v").sum() == pytest.approx(1.0)


def test_tb1_calibration_uses_previous_edition_only():
    from ml.config import TB1 as TB1C
    from ml.models.baseline import TB1
    import dataclasses
    lg = dataclasses.replace(BASKET, tb1=TB1C(5, 15.2, 18.7, 1.57), tb1_label="CALIBRATED_PREV_EDITION(k:NBL)")
    df, _, _ = synthetic(kind="normal")
    prev = df[df["season"] == 2020]
    c = TB1.calibrate(lg, prev)
    assert c.k == 5 and c.home_edge == pytest.approx(float((prev["hs"] - prev["as_"]).mean()))
    assert 5 < c.sd_margin < 40 and 5 < c.sd_total < 40
    assert TB1.calibrate(lg, prev.head(10)) is None  # too small: caller keeps the nearest sport's constants


def test_tb1_league_mean_falls_back_to_training_window():
    from ml.config import TB1 as TB1C
    from ml.models.baseline import TB1
    import dataclasses
    lg = dataclasses.replace(BASKET, tb1=TB1C(5, 15.2, 18.7, 1.57))
    df, _, _ = synthetic(kind="normal")
    t = TB1(lg).fit(df.iloc[:0], df.iloc[:0], fallback_games=df)
    assert t.lm == pytest.approx(float((df["hs"].sum() + df["as_"].sum()) / (2 * len(df))))
