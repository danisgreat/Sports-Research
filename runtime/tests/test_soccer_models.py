"""Soccer engine, half-time split (DST-07) and corners (DST-06), validated against BASE_RATES_REGISTER section 7.3."""

import numpy as np
import pytest

from runtime.src.common.errors import InsufficientData, MissingInputs, MissingScore, NotFitted, UnknownTeam
from runtime.src.common.leagues import get_profile
from runtime.src.sports.soccer.corners import CornersModel, concentration_from_team_sd, corner_grid, nb_total_pmf
from runtime.src.sports.soccer.engine import SoccerEngine
from runtime.src.sports.soccer.halves import (HalfSplit, fit_first_half_share, fit_half_split, half_distributions, half_goal_pmf,
                                               p_goal_in_first_half)

EPL = get_profile("soccer", "EPL")


# --------------------------------------------------------------------------- half-time split
def test_epl_first_half_matches_the_register():
    """Register: 1H mean 1.19 of 2.75; P(0/1/2/3/4+) = 0.284/0.382/0.224/0.084/0.026; P(>=1) = 0.716."""
    target = [0.284, 0.382, 0.224, 0.084, 0.026]
    split = fit_half_split(2.75 / 2.0 * 1.06, 2.75 / 2.0 * 0.94, target)          # a mild home edge, total 2.75 goals
    pmf = half_goal_pmf(2.75 / 2.0 * 1.06, 2.75 / 2.0 * 0.94, split)
    assert np.max(np.abs(pmf - target)) < 0.02                                    # acceptance: within +/-3 points (observed ~1.2)
    assert 1.0 - pmf[0] == pytest.approx(0.716, abs=0.005)
    assert 0.40 < split.first_half_share < 0.50 and 0.0 < split.rho < 0.2         # slightly under-dispersed first halves
    # the share quoted in the profile (1.19 / 2.75) is the ratio of means; the fitted share is its Poisson-corrected counterpart
    assert EPL.extra("first_half_goal_share") == pytest.approx(1.19 / 2.75, abs=1e-5)
    with pytest.raises(ValueError):
        fit_half_split(1.4, 1.3, [0.5, 0.6])


def test_first_half_share_can_be_fitted_to_an_observed_rate():
    share = fit_first_half_share(2.75, 0.716, rho=-0.05)
    assert 0.38 < share < 0.50
    assert p_goal_in_first_half(2.75, HalfSplit(share, -0.05)) == pytest.approx(0.716, abs=1e-8)
    with pytest.raises(ValueError):
        fit_first_half_share(2.75, 0.99, rho=-0.05)


def test_halves_compose_into_a_proper_full_time_grid():
    parts = half_distributions(1.5, 1.2, HalfSplit(0.45, -0.04))
    full = parts["full_time"]
    assert full.grid.sum() == pytest.approx(1.0, abs=1e-12) and full.endpoint == "regulation"
    h, a = np.meshgrid(full.home_support, full.away_support, indexing="ij")
    assert (h * full.grid).sum() == pytest.approx(1.5, abs=0.02) and (a * full.grid).sum() == pytest.approx(1.2, abs=0.02)
    # a goalless first half is the "0-0 at half-time" path and is more likely than a goalless full time
    assert parts["first_half"].grid[0, 0] > full.grid[0, 0]
    # P(1H over 0.5) comes from the first-half grid, not from the full-time grid
    assert parts["first_half"].p_over(0.5) < full.p_over(0.5)
    with pytest.raises(ValueError):
        HalfSplit(1.2, 0.0)


def test_engine_halves_need_an_explicit_split():
    engine = SoccerEngine()
    ctx = {"home_xg": 1.5, "away_xg": 1.2}
    with pytest.raises(MissingInputs, match="HalfSplit"):
        engine.predict_halves(ctx)
    out = SoccerEngine(half_split=HalfSplit(0.43, -0.04)).predict_halves(ctx)
    assert set(out) == {"first_half", "second_half", "full_time"}


# --------------------------------------------------------------------------------- engine
def season(teams=10, rounds=3, seed=1):
    rng = np.random.default_rng(seed)
    names = [f"Club{i}" for i in range(teams)]
    att = rng.normal(0, 0.2, teams)
    out = []
    day = 300
    for _ in range(rounds):
        for i in range(teams):
            for j in range(teams):
                if i != j:
                    out.append({"home": names[i], "away": names[j], "home_goals": int(rng.poisson(1.4 * np.exp(att[i] + 0.2))),
                                "away_goals": int(rng.poisson(1.2 * np.exp(att[j]))), "days_ago": float(day)})
                    day = max(day - 0.4, 0)
    return out


def test_explicit_xg_needs_no_fit_but_rho_must_be_known():
    engine = SoccerEngine()
    with pytest.raises(MissingInputs, match="dixon_coles_rho"):
        engine.predict_distribution({"home_xg": 1.8, "away_xg": 0.9})
    dist = engine.predict_distribution({"home_xg": 1.8, "away_xg": 0.9, "dixon_coles_rho": -0.05})
    assert dist.endpoint == "regulation" and dist.grid.sum() == pytest.approx(1.0)
    assert dist.p_home_win() > dist.p_away_win()
    with pytest.raises(NotFitted):
        engine.predict_distribution({"home_team": "A", "away_team": "B"})
    with pytest.raises(ValueError, match="extra time"):
        engine.predict_distribution({"home_xg": 1.8, "away_xg": 0.9, "dixon_coles_rho": -0.05}, endpoint="full_game")


def test_fitted_engine_refuses_unknown_teams_and_rejects_bad_training_rows():
    matches = season()
    engine = SoccerEngine(xi=0.0).fit(matches)
    assert engine.is_fitted and engine.dixon_coles.converged
    assert engine.predict_distribution({"home_team": "Club0", "away_team": "Club1"}).grid.sum() == pytest.approx(1.0)
    with pytest.raises(UnknownTeam):
        engine.predict_distribution({"home_team": "Club0", "away_team": "Newly Promoted"})
    lenient = SoccerEngine(xi=0.0, unknown_team_policy="league_average").fit(matches)
    assert lenient.predict_distribution({"home_team": "Club0", "away_team": "Newly Promoted"}).metadata["warnings"]
    with pytest.raises(MissingScore):
        SoccerEngine().fit(matches + [{"home": "Club0", "away": "Club1", "home_goals": None, "away_goals": 1}])
    with pytest.raises(InsufficientData):
        SoccerEngine().fit(matches[:2])
    with pytest.raises(ValueError):
        SoccerEngine().fit({})


def test_artifact_roundtrip(tmp_path):
    engine = SoccerEngine(xi=0.002, l2_reg=0.05, half_split=HalfSplit(0.43, -0.04)).fit(season())
    path = tmp_path / "soccer.json"
    engine.save_artifact(str(path), {"metrics": {"matches": 270}})
    loaded = SoccerEngine.load_artifact(str(path))
    a = engine.predict_distribution({"home_team": "Club0", "away_team": "Club1"})
    b = loaded.predict_distribution({"home_team": "Club0", "away_team": "Club1"})
    np.testing.assert_allclose(a.grid, b.grid)
    assert loaded.half_split.first_half_share == 0.43


# -------------------------------------------------------------------------------- corners
def test_epl_corner_totals_match_the_register():
    """Register: mean 10.0, SD 3.27; P(total >= 8/9/10/11/12) = 0.755/0.661/0.563/0.437/0.316; per team 5.0 (SD 2.77)."""
    phi = (EPL.extra("corners_sd") ** 2 - EPL.extra("corners_mean")) / EPL.extra("corners_mean") ** 2
    c = concentration_from_team_sd(EPL.extra("corners_mean"), EPL.extra("corners_sd"), EPL.extra("corners_team_sd"))
    grid = corner_grid(5.0, 5.0, phi, c)
    h, a = np.meshgrid(np.arange(grid.shape[0]), np.arange(grid.shape[1]), indexing="ij")
    total = h + a
    mean_total = (total * grid).sum()
    assert mean_total == pytest.approx(10.0, abs=0.01)
    assert np.sqrt(((total - mean_total) ** 2 * grid).sum()) == pytest.approx(3.27, abs=0.02)
    for k, want in zip(range(8, 13), [0.755, 0.661, 0.563, 0.437, 0.316]):
        assert grid[total >= k].sum() == pytest.approx(want, abs=0.03)
    mean_h = (h * grid).sum()
    assert np.sqrt(((h - mean_h) ** 2 * grid).sum()) == pytest.approx(2.77, abs=0.02)
    assert np.corrcoef(np.repeat(h.ravel(), 1), a.ravel(), )[0, 1] is not None
    cov = ((h - mean_h) * (a - (a * grid).sum()) * grid).sum()
    assert cov < 0.0                                             # corner counts are negatively dependent


def test_corner_grid_responds_to_score_state_and_ratings():
    base = corner_grid(5.6, 4.4, 0.01, 12.0)
    leading = corner_grid(5.6, 4.4, 0.01, 12.0, expected_goal_margin=1.0, score_state_beta=0.04)
    h, a = np.meshgrid(np.arange(base.shape[0]), np.arange(base.shape[1]), indexing="ij")
    assert (h * leading).sum() < (h * base).sum()                # the side expected to lead wins fewer corners
    assert (h * base).sum() == pytest.approx(5.6, abs=0.05)
    pmf = nb_total_pmf(10.0, 0.0)
    assert pmf.sum() == pytest.approx(1.0)
    with pytest.raises(ValueError):
        concentration_from_team_sd(10.0, 3.27, 1.0)


def test_corners_model_recovers_dispersion_and_strength_from_synthetic_provider_data():
    rng = np.random.default_rng(11)
    teams = [f"T{i}" for i in range(12)]
    strength = rng.normal(0, 0.15, 12)
    games = []
    for _ in range(1800):
        i, j = rng.choice(12, 2, replace=False)
        mu_h, mu_a = 5.4 * np.exp(strength[i] - 0.5 * strength[j]), 4.6 * np.exp(strength[j] - 0.5 * strength[i])
        mean_t = mu_h + mu_a
        r = 1.0 / 0.02
        total = rng.negative_binomial(r, r / (r + mean_t))
        share = rng.beta(mu_h / mean_t * 12, mu_a / mean_t * 12)
        hc = rng.binomial(total, share)
        games.append({"home": teams[i], "away": teams[j], "home_corners": int(hc), "away_corners": int(total - hc)})
    model = CornersModel().fit(games)
    assert model.phi == pytest.approx(0.02, abs=0.03) and model.concentration > 4.0
    dist = model.distribution("T0", "T1")
    assert dist.grid.sum() == pytest.approx(1.0) and dist.endpoint == "corners_90"
    with pytest.raises(InsufficientData):
        CornersModel().fit(games[:50])
    with pytest.raises(MissingInputs):
        CornersModel().distribution(mean_home=5.0, mean_away=5.0)
