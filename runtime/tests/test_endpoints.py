"""DST-02: full-game endpoints are coherent (no tied mass where the rules forbid it)."""

import numpy as np
import pytest

from runtime.src.common.contracts import ScoreDistribution
from runtime.src.common.endpoints import (
    HockeyOvertime, baseball_extra_innings, basketball_overtime, extras_margin_one_share, fit_ot_multiplier,
    fit_walk_off_overshoot, hockey_full_game, resolve_ties,
)
from runtime.src.common.errors import MissingInputs


def poisson_grid(lh, la):
    return ScoreDistribution.from_bivariate_poisson(lh, la, 0.0, max_score=20)


def test_resolve_ties_conserves_mass_and_removes_draws():
    reg = poisson_grid(3.0, 2.8)
    assert reg.p_draw() == pytest.approx(0.169, abs=0.005)           # the documented NHL example: ~16.9% regulation draws
    full = resolve_ties(reg, 0.55, increment=1)
    assert full.endpoint == "full_game"
    assert full.grid.sum() == pytest.approx(1.0, abs=1e-12)
    assert full.p_draw() == pytest.approx(0.0, abs=1e-15)
    assert full.p_home_win() + full.p_away_win() == pytest.approx(1.0, abs=1e-12)
    assert full.p_home_win() == pytest.approx(reg.p_home_win() + 0.55 * reg.p_draw(), abs=1e-12)
    # tie winners add exactly one goal: totals of those games are odd, so a regulation 2-2 lands Under 5.5
    reg22 = ScoreDistribution(np.zeros((6, 6)) + np.eye(6)[2][:, None] * np.eye(6)[2][None, :], np.arange(6), np.arange(6))
    assert resolve_ties(reg22, 0.5).p_under(5.5) == pytest.approx(1.0)


def test_resolve_ties_validates_inputs():
    reg = poisson_grid(3.0, 2.8)
    with pytest.raises(ValueError):
        resolve_ties(reg, 1.2)
    with pytest.raises(ValueError):
        resolve_ties(reg, 0.5, increment=0)


def test_hockey_full_game_moneylines_sum_to_one_and_regulation_contracts_unchanged():
    reg = poisson_grid(3.0, 2.8)
    rule = HockeyOvertime(ot_minutes=5.0, ot_rate_multiplier=2.2, shootout_home_share=0.5)
    full = hockey_full_game(reg, 3.0, 2.8, rule)
    assert full.p_home_win() + full.p_away_win() == pytest.approx(1.0, abs=1e-12)
    assert full.p_home_win() > 0.5 and full.p_home_win() > reg.p_home_win()
    assert reg.p_draw() > 0.1                                        # the regulation object keeps its draws
    # P(home | tie) is a weighted mix of the OT goal race and the shootout
    p = rule.p_home_given_tie(3.0, 2.8)
    assert 0.5 < p < 3.0 / 5.8
    # sudden-death playoff overtime decides by scoring rates alone
    assert HockeyOvertime(ot_minutes=None).p_home_given_tie(3.0, 2.8) == pytest.approx(3.0 / 5.8)


def test_ot_multiplier_fit_reproduces_the_observed_share():
    m = fit_ot_multiplier(6.19, 0.68, 5.0)
    rule = HockeyOvertime(ot_minutes=5.0, ot_rate_multiplier=m)
    assert rule.p_decided_in_overtime(6.19) == pytest.approx(0.68, abs=1e-12)
    with pytest.raises(ValueError):
        fit_ot_multiplier(6.19, 1.0)


def normal_basketball_grid(mu_h=112.0, mu_a=110.0, sd=11.0):
    n = 200
    s = np.arange(n)
    ph = np.exp(-0.5 * ((s - mu_h) / sd) ** 2)
    pa = np.exp(-0.5 * ((s - mu_a) / sd) ** 2)
    return ScoreDistribution.from_independent_marginals(ph / ph.sum(), pa / pa.sum())


def test_basketball_overtime_resolves_ties_conserving_mass():
    reg = normal_basketball_grid()
    tie = reg.p_draw()
    assert 0.02 < tie < 0.06                                         # the ~3.5% tie mass of the documented example
    full = basketball_overtime(reg, 112.0, 110.0, 11.0, 11.0, regulation_minutes=48.0, ot_minutes=5.0)
    assert full.endpoint == "full_game"
    assert full.grid.sum() == pytest.approx(1.0, abs=1e-9)
    assert full.p_draw() < 1e-9
    assert full.p_home_win() + full.p_away_win() == pytest.approx(1.0, abs=1e-9)
    # overtime adds about 2 * mean * 5/48 points to the tied games and nothing to the others
    added = sum(full.expected_scores()) - sum(reg.expected_scores())
    # one overtime adds 2 * 111 * 5/48 = 23.1 points; tied overtimes repeat (P(tie) ~ 0.08), so ~25.3 per tied game
    assert added / tie == pytest.approx(2 * 111.0 * 5.0 / 48.0 / (1.0 - 0.0797), rel=0.03)
    assert 24.0 < added / tie < 26.5                                  # the rules file: "overtime adds about 25 points"
    # a slightly stronger home side wins overtime a little more than half the time
    p_home_tie = (full.p_home_win() - reg.p_home_win()) / tie
    assert 0.5 < p_home_tie < 0.6


def test_basketball_overtime_rejects_bad_minutes():
    with pytest.raises(ValueError):
        basketball_overtime(normal_basketball_grid(), 112, 110, 11, 11, regulation_minutes=0)


Q = [0.45, 0.28, 0.14, 0.08, 0.05]


def test_baseball_extra_innings_play_until_decided():
    reg = poisson_grid(4.4, 4.3)
    p_tie = reg.p_draw()
    full = baseball_extra_innings(reg, Q, innings_cap=None)
    assert full.grid.sum() == pytest.approx(1.0, abs=1e-12)
    assert full.p_draw() < 1e-12                                      # MLB: no ties
    assert full.p_home_win() + full.p_away_win() == pytest.approx(1.0, abs=1e-12)
    assert full.metadata["p_tie_after_nine"] == pytest.approx(p_tie, abs=1e-12)
    # both halves share one run distribution, so extras split exactly evenly (no last-bat edge is modelled)
    assert full.p_home_win() == pytest.approx(reg.p_home_win() + 0.5 * p_tie, abs=1e-12)


def test_baseball_tie_leagues_keep_the_exact_residual_tie():
    reg = poisson_grid(3.4, 3.3)
    p_tie = reg.p_draw()
    per_inning_tie = float(np.sum(np.square(Q)))
    for cap in (1, 3):
        full = baseball_extra_innings(reg, Q, innings_cap=cap)
        assert full.p_draw() == pytest.approx(p_tie * per_inning_tie ** cap, rel=1e-9)
        assert full.grid.sum() == pytest.approx(1.0, abs=1e-12)
        assert full.p_home_win() + full.p_away_win() + full.p_draw() == pytest.approx(1.0, abs=1e-12)


def test_baseball_extra_inning_distribution_must_be_a_probability_vector():
    with pytest.raises(MissingInputs):
        baseball_extra_innings(poisson_grid(4, 4), [0.5, 0.3])


def test_walk_off_overshoot_is_linear_and_fit_reproduces_target():
    low, high = extras_margin_one_share(Q, 1.0), extras_margin_one_share(Q, 0.0)
    assert low < high
    mid = extras_margin_one_share(Q, 0.5)
    assert mid == pytest.approx(0.5 * (low + high), abs=1e-9)
    phi = fit_walk_off_overshoot(Q, 0.685 if low < 0.685 < high else 0.5 * (low + high))
    target = 0.685 if low < 0.685 < high else 0.5 * (low + high)
    assert extras_margin_one_share(Q, phi) == pytest.approx(target, abs=1e-9)
    with pytest.raises(ValueError):
        fit_walk_off_overshoot(Q, 0.999)
    with pytest.raises(ValueError):
        baseball_extra_innings(poisson_grid(4, 4), Q, walk_off_overshoot_share=1.5)
