"""Rugby league engine (DST-12, DST-01, DST-13): negative dependence, kicking and half-time structure."""

import numpy as np
import pytest

from research.src import archive_std
from runtime.src.common.counts import cmp_pmf, count_moments, split_total_grid
from runtime.src.common.errors import InsufficientData, MissingInputs, MissingScore, UnknownTeam
from runtime.src.common.leagues import get_profile
from runtime.src.sports.nrl.engine import NRLEngine, NRLKicking, points_grid, points_matrix

NRL = get_profile("rugby_league", "NRL")
KICK = NRLKicking(conversion_rate=0.80, penalty_goals=0.5, field_goals=0.1)


def moments(dist):
    return count_moments(dist.grid)


def test_points_matrix_places_four_points_per_try_and_conserves_mass():
    m = points_matrix(KICK)
    assert m.shape[0] == 15 and np.allclose(m.sum(axis=1), 1.0)
    assert m[0].argmax() == 0                                          # no tries: most likely nil
    expected = 4 * 3 + 2 * (0.8 * 3 + 0.5) + 0.1
    assert (m[3] * np.arange(m.shape[1])).sum() == pytest.approx(expected, abs=0.05)
    with pytest.raises(ValueError):
        split_total_grid(0.0, 0.0, 0.1, 10.0, 15)


def test_total_plus_share_structure_gives_negative_dependence():
    grid = split_total_grid(4.0, 4.0, 0.05, 12.0, 15)
    mh, ma, vt, vm = count_moments(grid)
    assert vm > vt                                                      # margin more variable than total: negative covariance
    independent = split_total_grid(4.0, 4.0, 0.05, 1e6, 15)
    assert count_moments(independent)[3] < vm
    pg = points_grid(grid, KICK)
    assert pg.sum() == pytest.approx(1.0)


def test_calibrated_engine_reproduces_the_league_spread_and_correlation():
    engine = NRLEngine(league=NRL, kicking=KICK)
    dist = engine.predict_distribution({"home_expected_tries": 4.2, "away_expected_tries": 3.8})
    mh, ma, vt, vm = moments(dist)
    assert np.sqrt(vt) == pytest.approx(NRL.total_sd, rel=0.01) and np.sqrt(vm) == pytest.approx(NRL.margin_sd, rel=0.01)
    cov = (vt - vm) / 4.0
    corr = cov / np.sqrt(((vt + vm) / 4.0) ** 2)
    assert corr == pytest.approx(NRL.score_corr, abs=0.03)             # about -0.3: reproduced rather than assumed zero
    assert dist.metadata["nu"] > 1.0 and dist.metadata["concentration"] > 0.5          # try counts are under-dispersed
    contracts = engine.evaluate_contracts(dist, [{"type": "moneyline", "side": "home"}, {"type": "total", "side": "over", "line": 45.5}])
    assert contracts[0].stated_prob > 0.5 and 0.2 < contracts[1].stated_prob < 0.8


def test_halftime_distribution_uses_the_first_half_share():
    engine = NRLEngine(league=NRL, kicking=KICK)
    ctx = {"home_expected_tries": 4.2, "away_expected_tries": 3.8}
    full, half = engine.predict_distribution(ctx), engine.predict_halftime(ctx)
    assert half.endpoint == "first_half" and half.metadata["period_scale"] == pytest.approx(NRL.extra("first_half_points_share"))
    assert sum(half.expected_scores()) == pytest.approx(NRL.extra("first_half_points_share") * sum(full.expected_scores()), rel=0.08)
    assert sum(half.expected_scores()) < 0.6 * sum(full.expected_scores())
    with pytest.raises(MissingInputs):
        NRLEngine(kicking=KICK, total_sd=13.0, margin_sd=19.0).predict_halftime(ctx)


def test_scoring_multiplier_compresses_a_finals_regime():
    engine = NRLEngine(league=NRL, kicking=KICK)
    ctx = {"home_expected_tries": 4.2, "away_expected_tries": 3.8}
    base = engine.predict_distribution(ctx)
    finals = engine.predict_distribution({**ctx, "scoring_multiplier": 0.93})
    assert sum(finals.expected_scores()) < sum(base.expected_scores())


def synthetic_games(n=900, seed=5):
    rng = np.random.default_rng(seed)
    teams = [f"T{i}" for i in range(8)]
    strength = rng.normal(0, 0.15, 8)
    out = []
    for _ in range(n):
        i, j = rng.choice(8, 2, replace=False)
        total = rng.negative_binomial(20, 20 / (20 + 8.4))
        share = rng.beta(12 * 0.53, 12 * 0.47) * 0 + rng.beta(8 * np.exp(strength[i] - strength[j]) / (1 + np.exp(strength[i] - strength[j])) * 3, 12)
        th = rng.binomial(total, min(share, 0.99))
        ta = total - th
        gh, ga = rng.binomial(th, 0.8) + rng.poisson(0.5), rng.binomial(ta, 0.8) + rng.poisson(0.5)
        out.append({"home_team": teams[i], "away_team": teams[j], "home_tries": int(th), "away_tries": int(ta),
                    "home_goals": int(gh), "away_goals": int(ga), "home_score": int(4 * th + 2 * gh), "away_score": int(4 * ta + 2 * ga)})
    return out


def test_fit_estimates_kicking_and_refuses_bad_rows():
    games = synthetic_games()
    engine = NRLEngine().fit(games)
    assert engine.kicking.conversion_rate == pytest.approx(0.80, abs=0.06)
    assert engine.kicking.penalty_goals == pytest.approx(0.5, abs=0.2)
    assert engine.total_sd > 0 and engine.margin_sd > engine.total_sd * 0.5
    dist = engine.predict_distribution({"home_team": "T0", "away_team": "T1"})
    assert dist.grid.sum() == pytest.approx(1.0)
    with pytest.raises(UnknownTeam):
        engine.predict_distribution({"home_team": "T0", "away_team": "Nobody"})
    bad = [{**games[0], "home_score": 1}] + games[1:]
    with pytest.raises(ValueError, match="fewer than"):
        NRLEngine().fit(bad)
    with pytest.raises(MissingScore):
        NRLEngine().fit([{k: v for k, v in games[0].items() if k != "home_tries"}] + games[1:])
    with pytest.raises(InsufficientData):
        NRLEngine().fit(games[:20])
    with pytest.raises(MissingInputs):
        NRLEngine(league=NRL).predict_distribution({"home_expected_tries": 4.0, "away_expected_tries": 4.0})


def test_archive_round_trip_matches_the_recorded_league():
    """Fit on three real NRL seasons and compare the average game and half-time spread with the archive."""
    events = [e for e in archive_std.iter_events(sport="Rugby League", competition="NRL", seasons=range(2022, 2026), stages={"regular"})
              if e.home_tries is not None and e.home_goals is not None and e.away_tries is not None and e.away_goals is not None]
    assert len(events) > 400
    rows = [{"home_team": e.home, "away_team": e.away, "home_tries": e.home_tries, "away_tries": e.away_tries, "home_goals": e.home_goals,
             "away_goals": e.away_goals, "home_score": e.home_score, "away_score": e.away_score} for e in events]
    engine = NRLEngine(league=NRL).fit(rows)
    assert 0.78 < engine.kicking.conversion_rate < 0.96
    dist = engine.predict_distribution({"home_expected_tries": NRL.extra("tries_mean") * 1.03, "away_expected_tries": NRL.extra("tries_mean") * 0.97})
    mh, ma, vt, vm = moments(dist)
    assert mh + ma == pytest.approx(NRL.mean_home + NRL.mean_away, rel=0.06)
    assert np.sqrt(vm) == pytest.approx(engine.margin_sd, rel=0.02)        # the engine targets the residual spread after team strengths
    ht = [(e.home_halftime, e.away_halftime) for e in archive_std.iter_events(sport="Rugby League", competition="NRL", seasons=range(2022, 2026), stages={"regular"})
          if e.home_halftime is not None]
    half = engine.predict_halftime({"home_expected_tries": NRL.extra("tries_mean") * 1.03, "away_expected_tries": NRL.extra("tries_mean") * 0.97})
    _, _, hvt, hvm = moments(half)
    arch_margin_sd = float(np.std([a - b for a, b in ht], ddof=1))
    arch_total_sd = float(np.std([a + b for a, b in ht], ddof=1))
    assert np.sqrt(hvm) == pytest.approx(arch_margin_sd, rel=0.12)
    assert np.sqrt(hvt) == pytest.approx(arch_total_sd, rel=0.15)


def test_conway_maxwell_poisson_covers_under_and_over_dispersion():
    k = np.arange(60)
    for nu, relation in ((1.0, "equal"), (2.0, "under"), (0.7, "over")):
        pmf = cmp_pmf(8.0, nu, 60)
        mean = float(k @ pmf)
        var = float(((k - mean) ** 2) @ pmf)
        assert pmf.sum() == pytest.approx(1.0) and mean == pytest.approx(8.0, abs=1e-9)
        assert (var == pytest.approx(8.0, rel=1e-3)) if relation == "equal" else (var < 8.0 if relation == "under" else var > 8.0)
    with pytest.raises(ValueError):
        cmp_pmf(8.0, 0.0, 60)
    with pytest.raises(ValueError):
        cmp_pmf(70.0, 1.0, 60)
