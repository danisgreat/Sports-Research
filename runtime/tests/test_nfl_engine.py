"""NFL drive model (DST-14): 6/8-point drives, structure from league moments, key-number calibration validated out of sample."""

import numpy as np
import pytest

from research.src import archive_std
from runtime.src.common.errors import InsufficientData, MissingInputs, MissingScore, UnknownTeam
from runtime.src.common.leagues import get_profile
from runtime.src.sports.nfl.engine import DriveRules, NFLEngine, apply_margin_weights, drive_pmf, margin_weights, team_points_pmf

NFL = get_profile("american_football", "NFL")


def test_touchdown_drives_score_six_seven_or_eight():
    rules = DriveRules()
    pmf = drive_pmf(0.22, 0.17, rules)
    assert pmf.sum() == pytest.approx(1.0) and pmf[1] == 0 and pmf[4] == pmf[5] == 0
    assert pmf[7] == pytest.approx(0.22 * 0.95 * 0.94) and pmf[8] == pytest.approx(0.22 * 0.05 * 0.48)
    assert pmf[6] == pytest.approx(0.22 * 0.95 * 0.06 + 0.22 * 0.05 * 0.52)
    assert pmf[3] == pytest.approx(0.17) and pmf[2] == pytest.approx(rules.safety)
    with pytest.raises(ValueError):
        drive_pmf(0.9, 0.2, rules)
    # a team with a high field-goal rate leaves more mass on the 3-point multiples than a touchdown team
    values = np.arange(81)
    fg_team, td_team = team_points_pmf(0.10, 0.30, rules), team_points_pmf(0.30, 0.04, rules)
    assert fg_team[[3, 6, 9, 12]].sum() > td_team[[3, 6, 9, 12]].sum()
    assert float(values @ fg_team) > 0 and fg_team.sum() == pytest.approx(1.0)


def test_structure_reproduces_the_league_team_mean_and_spread():
    sd = float(np.sqrt((NFL.total_sd ** 2 + NFL.margin_sd ** 2) / 4.0))
    engine = NFLEngine(league=NFL)
    td, fg = engine._structure(NFL.mean_team_score, sd)
    pmf = team_points_pmf(td, fg, engine.rules)
    values = np.arange(81)
    mean = float(values @ pmf)
    assert mean == pytest.approx(NFL.mean_team_score, rel=1e-3)
    assert np.sqrt(float(((values - mean) ** 2) @ pmf)) == pytest.approx(sd, rel=1e-3)
    assert 0.1 < td < 0.35 and 0.05 < fg < 0.3


def test_distribution_contracts_and_scaling():
    engine = NFLEngine(league=NFL)
    d = engine.predict_distribution({"home_expected_points": 25.0, "away_expected_points": 20.0})
    assert d.grid.sum() == pytest.approx(1.0) and d.expected_scores() == pytest.approx((25.0, 20.0), abs=0.05)
    # covering pair: P(home -3.5) >= P(home -6.5); home +3 covers at least as often as the moneyline
    c = engine.evaluate_contracts(d, [{"type": "spread", "side": "home", "line": -3.5}, {"type": "spread", "side": "home", "line": -6.5},
                                      {"type": "moneyline", "side": "home"}, {"type": "total", "side": "over", "line": 44.5}])
    assert c[0].stated_prob >= c[1].stated_prob and 0.5 < c[2].stated_prob < 0.9
    stronger = engine.predict_distribution({"home_expected_points": 28.0, "away_expected_points": 20.0})
    assert stronger.p_home_win() > d.p_home_win()
    with pytest.raises(ValueError):
        engine.predict_distribution({"home_expected_points": 25.0, "away_expected_points": 20.0}, endpoint="regulation")
    with pytest.raises(MissingInputs):
        NFLEngine().predict_distribution({"home_expected_points": 25.0, "away_expected_points": 20.0})


def test_key_number_mass_is_validated_out_of_sample():
    """Weights come from 2015-2025 (profile); the check is against 2023-2025 games, so it is not a pure in-sample fit.

    Acceptance: key-number margin frequencies within 1 point. Uncalibrated independent drives give margin 3 about 6% against 14%.
    """
    test = list(archive_std.iter_events(sport="American Football", competition="NFL", seasons=range(2023, 2026), stages={"regular"}))
    h = np.array([e.home_score for e in test])
    a = np.array([e.away_score for e in test])
    margin = np.abs(h - a)
    sd = float(np.sqrt((h.var() + a.var()) / 2))
    engine = NFLEngine(league=NFL)
    ctx = {"home_expected_points": h.mean(), "away_expected_points": a.mean(), "team_sd": sd}
    calibrated = engine.predict_distribution(ctx)
    raw = engine.predict_distribution({**ctx, "margin_calibration": False})
    home, away = np.meshgrid(calibrated.home_support, calibrated.away_support, indexing="ij")
    gap = np.abs(home - away)
    assert calibrated.metadata["margin_calibrated"] and not raw.metadata["margin_calibrated"]
    for k in (3, 6, 7, 10, 14):
        assert 100 * abs(calibrated.grid[gap == k].sum() - np.mean(margin == k)) < 1.0
    assert raw.grid[gap == 3].sum() < 0.08 < np.mean(margin == 3)                  # the gap the calibration closes
    assert calibrated.expected_scores() == pytest.approx((h.mean(), a.mean()), abs=0.02)   # team means are preserved
    assert calibrated.grid[gap == 0].sum() < 0.01                                    # overtime resolves ties


def test_margin_weights_and_ipf_are_well_behaved():
    engine = NFLEngine(league=NFL)
    raw = engine.predict_distribution({"home_expected_points": 24.0, "away_expected_points": 21.0, "margin_calibration": False})
    weights = margin_weights(raw.grid, NFL.margin_pmf)
    assert weights.shape == (81,) and np.all(weights >= 0.1) and np.all(weights <= 6.0)
    fixed = apply_margin_weights(raw.grid, weights)
    assert fixed.sum() == pytest.approx(1.0) and np.allclose(fixed.sum(axis=1), raw.grid.sum(axis=1), atol=2e-4)
    assert np.allclose(fixed.sum(axis=0), raw.grid.sum(axis=0), atol=2e-4)
    values = np.arange(81)
    assert float(values @ fixed.sum(axis=1)) == pytest.approx(float(values @ raw.grid.sum(axis=1)), abs=0.05)


def test_fit_unknown_team_and_missing_scores():
    rng = np.random.default_rng(8)
    teams = [f"T{i}" for i in range(10)]
    games = [{"home_team": h, "away_team": a, "home_score": int(np.clip(rng.normal(23.5, 9.8), 0, 60)),
              "away_score": int(np.clip(rng.normal(21.5, 9.8), 0, 60))} for h, a in (rng.choice(teams, 2, replace=False) for _ in range(500))]
    engine = NFLEngine().fit(games)
    assert engine.team_sd > 5
    d = engine.predict_distribution({"home_team": "T0", "away_team": "T1"})
    assert d.grid.sum() == pytest.approx(1.0)
    with pytest.raises(UnknownTeam):
        engine.predict_distribution({"home_team": "T0", "away_team": "Nobody"})
    with pytest.raises(MissingScore):
        NFLEngine().fit(games + [{"home_team": "T0", "away_team": "T1", "home_score": None, "away_score": 3}])
    with pytest.raises(InsufficientData):
        NFLEngine().fit(games[:10])
