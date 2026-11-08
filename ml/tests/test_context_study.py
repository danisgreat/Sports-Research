"""REV-10: the walk-forward development study's comparators. Synthetic games only; the full study is run by hand on the store."""
import numpy as np
import pandas as pd
import pytest

from ml import context_study as S


def history(n=120, seed=1):
    rng = np.random.default_rng(seed)
    teams = [f"T{i:02d}" for i in range(6)]
    strength = {t: s for t, s in zip(teams, rng.normal(0, 4, 6))}
    rows = []
    for i in range(n):
        h, a = rng.choice(teams, 2, replace=False)
        margin = strength[h] - strength[a] + 1.5 + rng.normal(0, 12)
        total = 180 + rng.normal(0, 15)
        rows.append(dict(home=h, away=a, hs=round(total / 2 + margin / 2), as_=round(total / 2 - margin / 2), season="2025"))
    return pd.DataFrame(rows), strength


def test_additive_form_is_more_decisive_than_the_average_form_for_a_strong_home_side():
    hist, strength = history()
    best, worst = max(strength, key=strength.get), min(strength, key=strength.get)
    avg = S.tb1_probability(hist, best, worst, "Basketball/NBL", "2025", "average")
    add = S.tb1_probability(hist, best, worst, "Basketball/NBL", "2025", "additive")
    assert 0.5 < avg < add < 1.0


def test_unseen_teams_other_seasons_and_unsupported_leagues_return_none():
    hist, _ = history()
    assert S.tb1_probability(hist, "T00", "NEW", "Basketball/NBL", "2025") is None
    assert S.tb1_probability(hist, "T00", "T01", "Basketball/NBL", "2030") is None
    assert S.tb1_probability(hist, "T00", "T01", "Soccer/Prva Liga RS", "2025") is None


def test_count_leagues_use_the_toolkit_normal_rule():
    rng = np.random.default_rng(2)
    rows = [dict(home="A", away="B", hs=int(rng.poisson(3.4)), as_=int(rng.poisson(2.6)), season="2025") for _ in range(80)]
    p = S.tb1_probability(pd.DataFrame(rows), "A", "B", "Ice Hockey/NHL", "2025", "additive")
    assert p is not None and 0.5 < p < 0.9


def test_summary_reports_both_mixtures_and_the_tb2_comparison():
    rng = np.random.default_rng(3)
    n = 400
    truth = rng.random(n) * 0.6 + 0.2
    y = (rng.random(n) < truth).astype(float)
    frame = pd.DataFrame(dict(event_id=[f"E{i}" for i in range(n)], week=[f"2025-W{1 + i // 20:02d}" for i in range(n)], y=y,
                              p_mix=0.5 + (truth - 0.5) * 0.6, p_hedge=0.5 + (truth - 0.5) * 0.7, p_league=np.full(n, 0.55),
                              p_tb1=0.5 + (truth - 0.5) * 0.5, p_tb2=truth, w_fast=0.4, w_slow=0.4, w_league=0.2,
                              z_margin=rng.normal(0, 1, n), z_total=rng.normal(0, 1, n)))
    out = {r["metric"]: r for r in S.summarise(dict(frame=frame, competition="Basketball/EXAMPLE", test_season="2025"))}
    assert out["calibration_slope_equal-weight mixture"]["value"] > 1.0 and out["calibration_slope_online-Hedge mixture"]["value"] > 1.0
    assert out["paired_brier_TB-2-MD_minus_TB-1-MD (season to date)"]["value"] < 0
    assert "BELOW_ZERO" in out["paired_brier_TB-2-MD_minus_league-only arm"]["detail"]
    assert out["mean_hedge_weights_fast_slow_league"]["detail"] == "0.400 / 0.400 / 0.200"


def test_changing_a_future_result_cannot_change_an_earlier_prediction(monkeypatch):
    """PIT-v2 (review 2026-11-08): the loss scale used the whole data set, so a future result moved earlier Hedge weights."""
    from ml.core.distributions import ScoreGrid

    class Stub:
        def __init__(self, competition, endpoint, recipe, ridge, baseline=False):
            self.shift = 0.0 if baseline else (4.0 if recipe == S.RECIPES["Basketball"][0] else 2.0)

        def fit(self, history, cutoff):
            return self

        def grid(self, row):
            return ScoreGrid.bivariate_normal(100.0 + self.shift, 96.0, np.array([[90.0, 40.0], [40.0, 90.0]]))

    rng = np.random.default_rng(11)
    teams = [f"T{i:02d}" for i in range(8)]
    rows, t = [], pd.Timestamp("2024-10-01T00:00:00Z")
    for i in range(330):
        h, a = rng.choice(teams, 2, replace=False)
        t += pd.Timedelta(hours=14)
        rows.append(dict(event_id=f"E{i}", event_at=t.isoformat(), season="2025" if i >= 260 else "2024", home=h, away=a,
                         hs=int(rng.normal(102, 12)), as_=int(rng.normal(97, 12))))
    base = pd.DataFrame(rows)
    monkeypatch.setattr(S, "ContextModel", Stub)

    def run(frame):
        monkeypatch.setattr(S, "training_frame", lambda *a, **k: frame.copy())
        return S.study("Basketball/NBA", "2025", refit_days=7).get("frame")

    first = run(base)
    changed = base.copy()
    changed.loc[changed.index[-1], ["hs", "as_"]] = [250, 10]        # an absurd final for the last game only
    second = run(changed)
    last_day = pd.Timestamp(base.event_at.iloc[-1]).normalize()
    earlier = first[first.event_at.map(lambda v: pd.Timestamp(v).normalize() < last_day - pd.Timedelta(days=7))]
    assert len(earlier) > 20
    merged = earlier.merge(second, on="event_id", suffixes=("_a", "_b"))
    assert np.allclose(merged.p_hedge_a, merged.p_hedge_b, atol=0, rtol=0)
    assert np.allclose(merged.w_fast_a, merged.w_fast_b, atol=0, rtol=0)
