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
