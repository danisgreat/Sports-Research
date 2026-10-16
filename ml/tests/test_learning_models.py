"""Challenger, Hedge schedules, V3-equivalent backtest and calibration studies (EXAMPLE data only)."""
import math

import numpy as np
import pandas as pd
import pytest

from ml import calibration as C
from ml import hedge as H
from ml import primary as p
from ml import research_ingest as ri
from ml import training_admission as ta
from ml.config import League
from ml.core.distributions import CoherenceError, ScoreGrid
from ml.evaluation import v3_backtest as vb
from ml.models import basketball_features as bf
from ml.models.common import FitError
from ml.tests import learning_fixtures as lf

LG = League(lf.COMPETITION, "Basketball", "EXAMPLE-LEARN", "EX", "gaussian", endpoint=lf.ENDPOINT,
            tie_rule="overtime", extra_fraction=5 / 40)


@pytest.fixture(scope="module")
def release(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("rel")
    frame = lf.season_frame(n_teams=8, seasons=(2025, 2026))
    lf.ingest_frame(tmp, tmp / "s", frame, "all")
    ta.build_release(tmp / "s", lf.COMPETITION, lf.ENDPOINT, tmp / "r", "R1")
    return ta.load_rows(tmp / "r" / "R1"), tmp


def test_challenger_grid_is_one_coherent_distribution_and_refuses_leakage(release):
    rows, _ = release
    cut = rows.event_at.iloc[150]
    m = bf.FeatureRidge(LG, bf.FEATURE_SETS["FULL"], bf.RidgeParams(10.0, 1.0, "scale_mixture"))
    m.fit(rows[rows.event_at < cut], cut)
    g = m.grid(rows.iloc[[160]])
    assert g.p.sum() == pytest.approx(1) and g.winner()[1] < 1e-9  # overtime resolves basketball ties
    assert g.handicap(0.5, "HOME").win == pytest.approx(g.winner()[0])  # contracts are projections of one grid
    assert g.total(200.5, "OVER").win + g.total(200.5, "UNDER").win == pytest.approx(1)
    with pytest.raises(FitError, match="leakage"):
        bf.FeatureRidge(LG, bf.FEATURE_SETS["L5"], bf.RidgeParams()).fit(rows, cut)
    assert "home_confirmed_out" not in m.columns  # never-observed availability is dropped, not imputed


def test_rolling_ablation_scores_identical_games_against_exact_v3_experts(release):
    rows, _ = release
    start = rows.event_at.iloc[-40]
    scored = bf.complete_events(bf.rolling(rows, LG, {"L10": (bf.FEATURE_SETS["L10"], bf.RidgeParams()), "V3": "V3"},
                                           start, start + pd.Timedelta(days=10)))
    assert set(scored.arm) == {"L10", *bf.V3_ARMS}
    assert scored.groupby("arm").event_uid.nunique().nunique() == 1  # identical events in every arm
    summary, paired = bf.summarise(scored, reference="L10")
    assert set(paired.reference) >= {"L10"} and (summary.events > 0).all()
    assert {"cover80_margin", "crps_total"} <= set(summary.columns)


def _ledger(n=120, seed=0, shift_at=None):
    rng = np.random.default_rng(seed)
    t0 = pd.Timestamp("2026-01-05T10:00:00Z")
    rows = []
    for i in range(n):
        y_home, y_over = float(rng.random() < .55), float(rng.random() < .5)
        good = 0 if shift_at is None or i < shift_at else 1  # expert 0 accurate, then expert 1 after the shift
        row = dict(event_id=f"E{i}", issued_at=(t0 + pd.Timedelta(days=i)).isoformat(),
                   available_at=(t0 + pd.Timedelta(days=i, hours=3)).isoformat(), week=f"W{i // 7}", season=2026 if i < n // 2 else 2027,
                   y_home=y_home, y_over=y_over, ctx="A" if i % 2 else "B")
        for k, a in enumerate(p.ARMS):
            noise = .05 if k == good else .35
            row[f"p_home_{a}"] = float(np.clip(y_home + rng.normal(0, noise) - .5 * (2 * y_home - 1) * noise, .01, .99))
            row[f"p_over_{a}"] = float(np.clip(y_over + rng.normal(0, noise) - .5 * (2 * y_over - 1) * noise, .01, .99))
            row[f"crps_margin_{a}"], row[f"crps_total_{a}"] = 8 + 4 * noise, 9 + 4 * noise
        rows.append(row)
    return pd.DataFrame(rows)


def test_fixed_hedge_reproduces_v3_and_uses_only_available_feedback():
    led = _ledger(30)
    losses = H.common_losses(led)
    w = H.run_policy(led, H.FixedHedge(2.0), losses)
    assert np.allclose(w[0], 1 / 3)  # nothing available before the first event
    cum = losses[:4].sum(axis=0)  # events 0..3 settled before event 4 was issued
    assert np.allclose(w[4], p.hedge_weights(cum, 2.0), atol=1e-12)
    late = led.copy()
    late.loc[0, "available_at"] = (pd.Timestamp(late.issued_at[10]) + pd.Timedelta(hours=1)).isoformat()
    w2 = H.run_policy(late, H.FixedHedge(2.0), losses)
    assert np.allclose(w2[4], p.hedge_weights(losses[1:4].sum(axis=0), 2.0))  # delayed feedback not yet seen


def test_schedules_keep_valid_weights_and_the_ess_floor_prevents_collapse():
    led = _ledger(80)
    losses = H.common_losses(led)
    for policy in (H.AdaHedge(), H.DiscountedHedge(2.0, .99), H.SeasonResetHedge(2.0), H.ShrunkContextHedge(2.0, 5),
                   H.ESSFloorHedge(50.0, 2.0)):
        w = H.run_policy(led, policy, losses, "ctx")
        assert np.allclose(w.sum(axis=1), 1) and (w >= 0).all()
    collapsed = H.run_policy(led, H.FixedHedge(50.0), losses)
    floored = H.run_policy(led, H.ESSFloorHedge(50.0, 2.0), losses)
    assert min(map(H.ess, collapsed[10:])) < 1.5 and min(map(H.ess, floored[10:])) >= 2.0 - 1e-6


def test_study_selects_on_the_tune_window_and_alerts_on_regime_change():
    led = _ledger(120, shift_at=70)
    res = H.study(led, led.issued_at[60], context_col="ctx")
    s = res["summary"].set_index("policy")
    assert s.loc[res["selected"], "tune_common_loss"] == s.tune_common_loss.min()
    assert (s.test_events == 60).all() and "V3_FIXED_ETA_2" not in set(res["paired"].policy)
    shifted = H.regime_alerts(led, H.common_losses(led), threshold=2.0)
    hit = shifted[(shifted.worse == p.ARMS[0]) & (shifted.than == p.ARMS[1])]
    assert bool(hit.alarm.iloc[0]) and int(hit.event_id.iloc[0][1:]) >= 70
    with pytest.raises(ValueError):
        H.study(led, led.issued_at[0])


def test_v3_equivalent_backtest_uses_runtime_policy_and_delayed_feedback(release):
    _, tmp = release
    hist = ri.history_rows(ri.load_store(tmp / "s"), lf.COMPETITION, lf.ENDPOINT, "2027-06-01T00:00:00Z")
    start = pd.Timestamp(hist[-6]["date"])
    expected = sum(pd.Timestamp(r["date"]) >= start for r in hist)
    led = vb.run(hist, LG, start)
    assert len(led) == expected and led.attrs["coverage"]["requested"] == expected
    w = led[[f"w_{a}" for a in p.ARMS]].to_numpy()
    assert np.allclose(w.sum(axis=1), 1)
    assert (led.n_feedback.diff().fillna(0) >= 0).all() and led.n_feedback.iloc[0] == 0
    mix = led[[f"p_home_{a}" for a in p.ARMS]].to_numpy()
    assert np.allclose((w * mix).sum(axis=1), led["p_home_" + p.MIX_ARM])  # linear in weights: exact mixture
    summary, _ = vb.summarise(led)
    assert set(summary.arm) == {*p.ARMS, p.MIX_ARM}


def _preds(n=900, seed=1, bias=.35):
    rng = np.random.default_rng(seed)
    t0 = pd.Timestamp("2026-01-01T00:00:00Z")
    q = rng.uniform(.1, .9, n)
    y = (rng.random(n) < q).astype(float)
    shown = np.clip(q + bias * (q - .5) * 2, .01, .99)  # overconfident forecasts
    return pd.DataFrame(dict(issued_at=[(t0 + pd.Timedelta(hours=6 * i)).isoformat() for i in range(n)],
                             outcome_available_at=[(t0 + pd.Timedelta(hours=6 * i + 3)).isoformat() for i in range(n)],
                             competition=np.where(np.arange(n) % 3, "Basketball/A", "Basketball/B"), p=shown, y=y))


def test_calibration_is_chronological_and_improves_overconfidence_only_out_of_sample():
    rows = _preds()
    issued = rows.issued_at.map(p.clock)
    tune_start, tune_end = issued.iloc[400], issued.iloc[600]
    train = C.available_before(rows, tune_start)
    assert (train.outcome_available_at.map(p.clock) <= tune_start).all() and len(train) == 400
    res = C.study(rows, tune_start, tune_end)
    assert res["selection"]["selected"] != "IDENTITY" and res["calibrated_brier"] < res["raw_brier"]
    assert res["raw_slope"] < 1 and abs(res["calibrated_slope"] - 1) < abs(res["raw_slope"] - 1)
    iso = C.fit_isotonic(rows.p[:300], rows.y[:300])
    xs = np.linspace(0, 1, 50)
    assert (np.diff(iso(xs)) >= -1e-12).all()
    calibrated = _preds(bias=0.0)
    assert C.study(calibrated, tune_start, tune_end)["selection"]["results"]["IDENTITY"]["status"] == "FITTED"


def test_grid_recalibration_hits_winner_and_total_targets_coherently():
    g = ScoreGrid.bivariate_normal(102, 98, np.array([[120., 30.], [30., 110.]]))
    out = C.calibrate_grid(g, .6, total_line=199.5, over_target=.45)
    assert out.winner()[0] == pytest.approx(.6, abs=1e-9) and out.total(199.5, "OVER").win == pytest.approx(.45, abs=1e-9)
    assert out.p.sum() == pytest.approx(1) and out.handicap(-0.5, "HOME").win == pytest.approx(out.winner()[0])
    assert out.winner()[1] == pytest.approx(g.winner()[1])  # the regulation draw class keeps its mass
    with pytest.raises(CoherenceError):
        C.calibrate_grid(g, 1.2)
    with pytest.raises(CoherenceError):
        C.calibrate_grid(g, .6, total_line=200.0, over_target=.5)
