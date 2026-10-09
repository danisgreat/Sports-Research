"""Candidate ladder, Rank-1 gate, Rank-2 diversification, adjustment dependence (PRD-02/03/04/05)."""

import itertools

import numpy as np
import pytest

from runtime.src.common.contracts import ScoreDistribution
from runtime.src.common.errors import MissingInputs
from runtime.src.common.leagues import get_profile
from runtime.src.common.selection import (
    Adjustment, adjustment_dependence, are_complements, btts_row, double_chance_row, handicap_row, joint_failure, ladder, load_rules,
    outcome_space, propose, rank1_gate, rank_by_p, row_from_spec, team_total_row, total_row, winner_row,
)
from runtime.src.sports.baseball.engine import BaseballEngine
from runtime.src.sports.basketball.engine import bivariate_grid
from runtime.src.sports.nhl.engine import HockeyLateGame, NHLEngine
from runtime.src.sports.soccer.engine import SoccerEngine
from runtime.src.sports.tennis.engine import TennisEngine

RULES = load_rules()


def soccer(h=1.7, a=1.0):
    return SoccerEngine().predict_distribution({"home_xg": h, "away_xg": a, "dixon_coles_rho": -0.05})


def nba_like(mean_h, mean_a, sd=12.3, corr=0.256):
    grid = bivariate_grid(mean_h, mean_a, sd, sd, corr)
    return ScoreDistribution(grid, np.arange(grid.shape[0]), np.arange(grid.shape[1]), endpoint="full_game")


def test_rows_price_exactly_like_the_distribution_methods():
    dist = soccer()
    space = outcome_space(dist)
    assert winner_row(space, "home").p_win == pytest.approx(dist.p_home_win())
    assert winner_row(space, "draw").p_win == pytest.approx(dist.p_draw())
    assert double_chance_row(space, "1X").p_win == pytest.approx(dist.p_double_chance("1X"))
    over, under = total_row(space, "over", 2.5), total_row(space, "under", 2.5)
    assert over.p_win == pytest.approx(dist.p_over(2.5)) and under.p_win == pytest.approx(dist.p_under(2.5))
    assert over.p_win + under.p_win == pytest.approx(1.0) and over.p_push == pytest.approx(0.0, abs=1e-12)
    cover = handicap_row(space, "home", -1.0)                                  # whole line pushes on a one-goal win
    assert cover.p_win == pytest.approx(dist.p_home_cover(-1.0)) and cover.p_push == pytest.approx(dist.p_push_spread(-1.0))
    assert cover.p_card == pytest.approx(cover.p_win / (cover.p_win + cover.p_lose)) and cover.p_card > cover.p_win
    assert team_total_row(space, "home", "over", 1.5).p_win == pytest.approx(dist.p_team_total_over("home", 1.5))
    assert btts_row(space, True).p_win == pytest.approx(dist.p_btts_yes())


def test_joint_failure_is_exact_and_complements_are_detected():
    dist = soccer()
    space = outcome_space(dist)
    a, b = total_row(space, "under", 2.5), handicap_row(space, "home", 0.5)
    value, exact = joint_failure(a, b, space)
    brute = sum(dist.grid[i, j] for i in range(dist.grid.shape[0]) for j in range(dist.grid.shape[1]) if i + j > 2.5 and i - j + 0.5 < 0)
    assert exact and value == pytest.approx(brute)
    assert are_complements(total_row(space, "over", 2.5), total_row(space, "under", 2.5))
    assert are_complements(handicap_row(space, "home", -1.5), handicap_row(space, "away", 1.5))
    assert not are_complements(a, b)
    first_half = outcome_space(soccer(0.7, 0.5), "first_half")
    cross, cross_exact = joint_failure(a, total_row(first_half, "over", 0.5), space)
    assert not cross_exact and cross == pytest.approx(min(a.p_lose, total_row(first_half, "over", 0.5).p_lose))


def test_tennis_winner_is_priced_from_the_split_not_the_games_grid():
    dist = TennisEngine(form_sigma=0.04).predict_distribution({"p_serve1": 0.67, "p_serve2": 0.61})
    space = outcome_space(dist)
    assert winner_row(space, "home").p_win == pytest.approx(dist.p_home_win(), abs=1e-9)
    assert winner_row(space, "away").p_win == pytest.approx(dist.p_away_win(), abs=1e-9)
    games_only = handicap_row(space, "home", 0.5)                               # games handicap, not the winner
    assert games_only.p_win != pytest.approx(winner_row(space, "home").p_win, abs=1e-3)
    # the favourite who loses the match can still win more games: winner and games are not the same event
    both = winner_row(space, "home")
    assert 0.0 < float(space.mass[both.lose & handicap_row(space, "home", 0.5).win].sum())


def test_ladder_is_monotone_and_covers_every_family():
    dist = soccer()
    space = outcome_space(dist)
    rows = ladder(space, RULES["ladders"]["soccer"], names=("Arsenal", "Chelsea"))
    families = {r.family for r in rows}
    assert {"winner", "double_chance", "handicap", "total", "team_total", "btts"} <= families
    overs = sorted((float(r.kind.split(":")[2]), r.p_win) for r in rows if r.kind.startswith("total:over:"))
    assert all(a[1] >= b[1] - 1e-12 for a, b in zip(overs, overs[1:])) and len(overs) >= 4
    homes = sorted((float(r.kind.split(":")[2]), r.p_win) for r in rows if r.kind.startswith("handicap:home:"))
    assert all(a[1] <= b[1] + 1e-12 for a, b in zip(homes, homes[1:]))
    assert all(abs(float(r.kind.split(":")[-1]) % 1) == 0.5 for r in rows if r.kind.startswith(("total", "handicap")))      # half lines only
    nfl_rows = ladder(outcome_space(nba_like(24, 21, 9, 0.0)), RULES["ladders"]["american_football"])
    assert any(float(r.kind.split(":")[-1]) % 1 == 0 for r in nfl_rows if r.kind.startswith("handicap"))                   # key numbers priced


def test_proposal_obeys_the_ranking_rules():
    dist = soccer()
    space = outcome_space(dist)
    supplied = [row_from_spec(space, s) for s in ({"type": "total", "side": "over", "line": 2.5}, {"type": "spread", "side": "home", "line": -1.5},
                                                  {"type": "moneyline", "side": "home"})]
    proposal = propose(ladder(space, RULES["ladders"]["soccer"]), space, supplied, RULES)
    ps = [p.p_card for p in proposal.picks]
    assert len(proposal.picks) == 4 and ps == sorted(ps, reverse=True)           # non-increasing: the card validator accepts it
    assert all(p <= RULES["p_card_max"] for p in ps)
    first, second = proposal.picks[0].row, proposal.picks[1].row
    assert not are_complements(first, second) and first.kind != second.kind
    assert proposal.joint_failure_top2 == pytest.approx(joint_failure(first, second, space)[0]) and proposal.joint_exact
    # Rank 2 is the minimum-joint-failure row among eligible candidates, not simply the next-highest probability
    eligible = [r for r in ladder(space, RULES["ladders"]["soccer"]) + supplied if RULES["rank2"]["p_min"] <= r.p_card <= 0.90
                and not are_complements(first, r) and r.kind != first.kind]
    best = min(joint_failure(first, r, space)[0] for r in eligible)
    assert proposal.joint_failure_top2 == pytest.approx(best)
    table = proposal.pick_table("soccer_dc")
    assert table.count("\n") == 5 and "FROM_DISTRIBUTION:soccer_dc" in table and "TO_FILL" in table
    assert proposal.as_dict()["ladder"] and {t["selected_rank"] for t in proposal.ladder_table} >= {1, 2, 3, 4}


def test_supplied_rows_are_tagged_and_replacements_named():
    space = outcome_space(soccer())
    supplied = [row_from_spec(space, {"type": "total", "side": "over", "line": 2.5, "label": "Over 2.5 (supplied)"})]
    proposal = propose(ladder(space, RULES["ladders"]["soccer"]), space, supplied, RULES)
    for pick in proposal.picks:
        if pick.row.tag == "SUPPLIED":
            assert pick.row.label == "Over 2.5 (supplied)"
        elif pick.row.family == "total":
            assert pick.row.replaces == "Over 2.5 (supplied)"


def test_rank1_gate_thresholds():
    assert rank1_gate(0.64, 0.58, RULES)["passed"] is True
    assert rank1_gate(0.61, 0.50, RULES)["passed"] is False                                        # below p_min
    assert rank1_gate(0.70, 0.67, RULES)["passed"] is False                                        # no clear lead
    gate = rank1_gate(0.70, 0.60, RULES)
    assert gate["margin"] == pytest.approx(0.10) and gate["status"] == "provisional"


def test_degenerate_rows_are_excluded_and_a_thin_pool_is_an_error():
    space = outcome_space(soccer(3.5, 0.2))
    proposal = propose(ladder(space, RULES["ladders"]["soccer"]), space, rules=RULES)
    assert all(p.p_card <= 0.90 for p in proposal.picks)
    with pytest.raises(MissingInputs):
        propose(ladder(space, RULES["ladders"]["soccer"])[:3], space, rules=RULES)


def test_weak_slate_is_flagged_and_unstable_rank1_is_labelled():
    space = outcome_space(nba_like(100, 100, 6.0, 0.0))
    # a tight single-team ladder leaves nothing above the gate when only near-coin-flip rows are offered
    rows = [r for r in ladder(space, RULES["ladders"]["basketball"]) if 0.45 <= r.p_card <= 0.56]
    if len(rows) >= 6:
        proposal = propose(rows, space, rules=RULES)
        assert "RANK1_UNSTABLE" in proposal.flags and "RANK2_WEAK_SLATE" in proposal.flags
        assert proposal.rank1_gate["passed"] is False


def test_joint_failure_target_holds_on_most_simulated_cards():
    """PRD-02 acceptance, on a simulated battery (historical cards do not retain their distributions, so a literal replay is impossible)."""
    cases = []
    for h, a in itertools.product((0.9, 1.4, 2.0), (0.7, 1.1, 1.6)):
        cases.append(("soccer", soccer(h, a)))
    for mh, ma in ((112, 108), (118, 104), (105, 105), (121, 116), (99, 94)):
        cases.append(("basketball", nba_like(mh, ma)))
    cases.append(("ice_hockey", NHLEngine(league=get_profile("ice_hockey", "NHL"), late_game=HockeyLateGame.ILLUSTRATIVE)
                  .predict_distribution({"home_xg": 3.1, "away_xg": 2.8})))
    cases.append(("baseball", BaseballEngine(league=get_profile("baseball", "MLB")).predict_distribution({"home_expected_runs": 4.7, "away_expected_runs": 4.2})))
    jf = []
    for sport, dist in cases:
        space = outcome_space(dist)
        proposal = propose(ladder(space, RULES["ladders"][sport]), space, rules=RULES)
        jf.append(proposal.joint_failure_top2)
        assert proposal.joint_exact
    share = np.mean(np.array(jf) <= RULES["rank2"]["joint_failure_target"])
    assert share >= 0.80, f"only {share:.0%} of simulated cards reach joint failure <= 0.30 ({np.round(jf, 3)})"


def test_p553_style_adjustment_flips_the_top_two_and_is_flagged():
    """Card P-553: the analyst shifted Kobe by -3.75 points (margin -4.75, total -2.75); that judgement decided which row led."""
    unadjusted = outcome_space(nba_like(84.75, 85.0))
    adjusted = outcome_space(nba_like(81.0, 86.0))
    spec = [{"type": "total", "side": "under", "line": 171.5}, {"type": "spread", "side": "home", "line": 6.5},
            {"type": "spread", "side": "away", "line": -6.5}, {"type": "total", "side": "over", "line": 171.5}]
    before = rank_by_p([row_from_spec(unadjusted, s) for s in spec])
    after = rank_by_p([row_from_spec(adjusted, s) for s in spec])
    assert after[0].kind == "total:under:171.5" and before[0].kind == "handicap:home:6.5"
    assert after[0].p_card == pytest.approx(0.576, abs=0.03) and after[1].p_card == pytest.approx(0.544, abs=0.03)         # close to the card's own numbers (the card also modelled OT)
    adjustments = [Adjustment("kobe_margin_shift", "margin", -4.75, 4.75 / 15.0, "analyst_judgement"),
                   Adjustment("total_shift", "total", -2.75, 2.75 / 19.5, "analyst_judgement")]
    result = adjustment_dependence(before, after, adjustments)
    assert result["flag"] == "ADJUSTMENT_DEPENDENT" and result["large_adjustments"] == ["kobe_margin_shift"]
    assert "kobe_margin_shift" in result["judgement_only"]
    small = adjustment_dependence(before, after, [Adjustment("tiny", "margin", -1.0, 0.07, "fitted")])
    assert small["flag"] == "NONE" and small["ranks_changed"] is True                           # flips, but no adjustment large enough to blame
    same = adjustment_dependence(after, after, adjustments)
    assert same["flag"] == "NONE" and same["ranks_changed"] is False


def test_rules_file_is_complete():
    assert RULES["rank1_gate"]["p_min"] == 0.62 and RULES["rank1_gate"]["margin_min"] == 0.04 and RULES["rank2"]["p_min"] == 0.58
    assert RULES["p_card_max"] == 0.90 and RULES["adjustment_threshold_sd"] == 0.25
    assert set(RULES["family_rules"]) == {"first_half_over_0_5", "baseball_plus_1_5", "tennis_games", "corners"}
