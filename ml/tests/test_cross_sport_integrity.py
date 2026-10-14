"""Cross-sport regressions for malformed sources, legal edge cases and failure custody."""
import csv
from dataclasses import replace
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

from ml.config import League, detect_columns
from ml.core.distributions import CoherenceError, ScoreGrid
from ml.core import metrics
from ml.data import archive
from ml.decision import bandit, devig, kelly, lab
from ml.evaluation import backtest, report, writers
from ml.models import cricket
from ml.models.common import FitError, decay_weights
from ml.models.count import CountParams, PoissonRatings
from ml.models.gaussian import GaussParams
from ml.shadow import lane


def source(tmp_path, monkeypatch, rows, sport="Basketball", year=2025, name=None):
    monkeypatch.setattr(archive, "ARCHIVE", tmp_path)
    monkeypatch.setattr(cricket, "ARCHIVE", tmp_path)
    folder = tmp_path / sport / "Example" / str(year)
    folder.mkdir(parents=True, exist_ok=True)
    header = list(dict.fromkeys(key for row in rows for key in row))
    file = folder / (name or f"{year}_games.csv")
    with file.open("w", newline="", encoding="utf8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)
    return League(path=f"{sport}/Example", sport=sport, competition="Example", model_id="EXAMPLE", engine="gaussian", columns=detect_columns(header)), file


def result(**extra):
    return {"Date": "2025-01-01", "Game Type": "Regular Season", "Home": "A", "Away": "B", "Home Score": "3", "Away Score": "2", "Game ID": "E1", **extra}


SPORTS = ["Basketball", "AFL", "State Level AFL", "Soccer", "Rugby League", "Rugby Union", "American Football", "Canadian Football", "College Football", "Baseball", "Ice Hockey"]


@pytest.mark.parametrize("sport", SPORTS)
@pytest.mark.parametrize("score", ["3.5", "inf", "-1", "nan"])
def test_bad_scores_are_excluded_without_truncation_or_crashing(tmp_path, monkeypatch, sport, score):
    lg, _ = source(tmp_path, monkeypatch, [result(**{"Home Score": score}), result(**{"Game ID": "E2"})], sport)
    loaded, receipt = archive.load_league(lg)
    assert list(loaded.event_id) == ["E2"]
    assert receipt.rows_read == 2 and receipt.rows_kept == 1


def test_schema_changes_are_read_per_file_and_native_ids_scoped_by_season(tmp_path, monkeypatch):
    lg, _ = source(tmp_path, monkeypatch, [result()], year=2025)
    source(tmp_path, monkeypatch, [{"Date": "2024-01-01", "Home Team": "A", "Away Team": "B", "Full Time Home Goals": "1", "Full Time Away Goals": "0", "Game ID": "E1", "Game Type": "Regular Season"}], year=2024)
    games, _ = archive.load_league(lg)
    assert list(games.season) == [2024, 2025]
    assert list(games.hs) == [1, 3]


def test_conflicting_finals_are_not_arbitrarily_first_row(tmp_path, monkeypatch):
    lg, _ = source(tmp_path, monkeypatch, [result(), result(**{"Home Score": "4"})])
    games, receipt = archive.load_league(lg)
    assert games.empty and receipt.dropped["conflicting_event_id"] == 2


def test_exact_duplicates_are_counted_and_native_doubleheaders_preserved(tmp_path, monkeypatch):
    lg, _ = source(tmp_path, monkeypatch, [result(), result(), result(**{"Game ID": "E2"})], "Baseball")
    games, receipt = archive.load_league(lg)
    assert len(games) == 2 and receipt.dropped["duplicate_event_id"] == 1


def test_doubleheaders_without_native_identity_are_not_collapsed_to_one_game(tmp_path, monkeypatch):
    lg, _ = source(tmp_path, monkeypatch, [result(**{"Game ID": ""}), result(**{"Game ID": "", "Home Score": "4"})], "Baseball")
    games, receipt = archive.load_league(lg)
    assert games.empty and receipt.dropped["ambiguous_doubleheader_identity"] == 2


def test_numeric_and_text_arithmetic_are_checked_independently(tmp_path, monkeypatch):
    lg, _ = source(tmp_path, monkeypatch, [result(**{"Total Points": "6", "Winning Margin": ""})])
    assert archive.load_league(lg)[0].empty
    rep = archive.LoadReport("Example")
    cols = detect_columns(["Home", "Away", "Game Score", "Total Points", "Winning Margin"])
    lg = replace(lg, columns=cols)
    assert archive._parse_text({"Home": "A", "Away": "B", "Game Score": "A 3 def. B 2", "Total Points": "6", "Winning Margin": ""}, lg, rep) is None


@pytest.mark.parametrize("value", ["N/A", "Not applicable", "unknown", "junk", "", None])
def test_unknown_extra_time_is_not_yes(value):
    assert not archive._yes(value)
    lg = SimpleNamespace(columns={"decision": None, "shootout": None, "overtime": "OT"})
    assert archive._hockey_decision({"OT": value}, lg) == "Unknown"


def test_real_zero_and_known_overtime_survive(tmp_path, monkeypatch):
    lg, _ = source(tmp_path, monkeypatch, [result(**{"Home Score": "0", "Away Score": "0", "Decision Type": "Regulation"}), result(**{"Game ID": "E2", "Decision Type": "SO"})], "Ice Hockey")
    games, _ = archive.load_league(replace(lg, tie_rule="hockey_regulation"))
    assert len(games) == 2
    assert games.iloc[0].hs == 0
    assert games.iloc[1].reg_hs == games.iloc[1].reg_as == 2
    assert not archive._yes("0-0") and archive._yes("1-0")


def innings(**extra):
    return {"Date": "2025-01-01", "Game Type": "Regular Season", "Game ID": "C1", "First Innings Team": "A", "Second Innings Team": "B", "First Innings Runs": "150", "First Innings Wickets": "5", "First Innings Overs": "20.0", "Method": "Not applicable", **extra}


@pytest.mark.parametrize("sport,cap", [("Cricket T20", 20), ("Cricket One-Day Format", 50)])
def test_cricket_full_length_and_all_out_and_empty_sources(tmp_path, monkeypatch, sport, cap):
    lg, _ = source(tmp_path, monkeypatch, [innings(**{"First Innings Overs": f"{cap}.0"}), innings(**{"Game ID": "C2", "First Innings Overs": "10.5", "First Innings Wickets": "10"}), innings(**{"Game ID": "C3", "First Innings Overs": "10.5"})], sport)
    games, dropped = cricket.load_cricket(replace(lg, engine="cricket", overs_cap=cap))
    assert len(games) == 2 and dropped["short_first_innings"] == 1


@pytest.mark.parametrize("bad", [{"First Innings Runs": "-1"}, {"First Innings Runs": "150.5"}, {"First Innings Runs": "inf"}, {"First Innings Wickets": "11"}, {"First Innings Overs": "19.6"}, {"First Innings Overs": "21.0"}])
def test_invalid_cricket_fields_produce_a_schema_valid_empty_table(tmp_path, monkeypatch, bad):
    lg, _ = source(tmp_path, monkeypatch, [innings(**bad)], "Cricket T20")
    games, dropped = cricket.load_cricket(replace(lg, engine="cricket", overs_cap=20))
    assert games.empty and "event_id" in games and sum(dropped.values()) == 1


def test_cricket_observations_beyond_model_support_are_scored_not_clamped(tmp_path, monkeypatch):
    lg, _ = source(tmp_path, monkeypatch, [innings(**{"First Innings Runs": "601"})], "Cricket T20")
    assert cricket.load_cricket(replace(lg, overs_cap=20))[0].iloc[0].runs == 601
    pmf = np.zeros(601)
    pmf[600] = 1
    scored = cricket.discrete_scores(pmf, 605, 600.5)
    assert scored["crps"] == 5 and scored["pit"] == 1 and scored["in80"] == 0


def test_archive_snapshot_covers_every_actual_games_file(tmp_path, monkeypatch):
    lg, _ = source(tmp_path, monkeypatch, [result()])
    _, extra = source(tmp_path, monkeypatch, [result(**{"Game ID": "E2"})], name="supplement_games.csv")
    before = archive.snapshot_hash(lg, [2025])
    extra.write_text(extra.read_text() + "\n", encoding="utf8")
    assert archive.snapshot_hash(lg, [2025]) != before


def test_shifted_ties_are_resolved_once():
    grid = ScoreGrid(np.diag([.5, .5]))
    resolved = grid.resolve_ties(.6, residual_draw=.5, both_bonus=1)
    assert resolved.winner() == pytest.approx((.3, .5, .2))
    assert resolved.p[1, 1] == resolved.p[2, 2] == .25


def test_push_is_exact_and_mass_classes_are_disjoint():
    grid = ScoreGrid(np.array([[1.0]]), h0=1)
    for masses in [grid.handicap(-1 + 1e-10), grid.total(1 + 1e-10)]:
        assert masses.push == 0
        assert masses.win + masses.push + masses.loss == 1
    with pytest.raises(CoherenceError):
        grid.total(np.nan)
    with pytest.raises(CoherenceError):
        grid.handicap(0, "WRONG")


def test_grid_owns_its_mass_and_rejects_invalid_inputs():
    original = np.array([[1.]])
    grid = ScoreGrid(original)
    original[0, 0] = 0
    assert grid.p.sum() == 1
    for call in [lambda: ScoreGrid(np.empty((0, 1))), lambda: ScoreGrid(np.ones((1, 1)), h0=.5), lambda: ScoreGrid.independent([-1, 2], [1]), lambda: ScoreGrid.negbin(1, 1, -.1), lambda: ScoreGrid.poisson(np.inf, 1), lambda: grid.resolve_ties(.5, winner_bonus=-1), lambda: grid.reweight_winner((np.nan, 1, 0))]:
        with pytest.raises(CoherenceError):
            call()


def test_missing_outcomes_are_not_losses_and_invalid_classes_are_rejected():
    assert np.isnan(metrics.log_loss([.5], [np.nan])[0])
    assert np.isnan(metrics.brier_multiclass_half([[.5, .5]], [np.nan])[0])
    with pytest.raises(ValueError):
        metrics.brier_multiclass_half([[.5, .5]], [-1])
    with pytest.raises(ValueError):
        metrics.log_loss([1.2], [1])
    assert metrics.log_loss([1 + 1e-16], [1])[0] == 0


def test_calibration_missingness_and_zero_variance_intervals():
    assert metrics.calibration_fit([np.nan], [1])["n"] == 0
    assert metrics.reliability_table([np.nan, .5], [1, 0]).n.sum() == 1
    assert np.isnan(metrics.brier_decomposition([], [])["brier"])
    assert np.isnan(metrics.cluster_bootstrap_mean(np.array([]), np.array([]))[0])
    index = pd.Series(range(8))
    iv = metrics.paired_week_interval(pd.Series([-.1] * 8), index, index)
    assert iv["lo"] == iv["hi"] == pytest.approx(-.1)
    assert iv["status"] == "BELOW_ZERO"


def test_training_cutoff_and_decay_are_strict():
    asof = pd.Timestamp("2025-01-01T12:00")
    with pytest.raises(FitError):
        decay_weights(pd.Series([asof]), asof, 2)
    with pytest.raises(FitError):
        decay_weights(pd.Series([asof - pd.Timedelta(days=1)]), asof, 0)
    assert decay_weights(pd.Series([asof - pd.Timedelta(hours=12)]), asof, 1)[0] == pytest.approx(2 ** -.5)


@pytest.mark.parametrize("params", [lambda: CountParams(0, 1), lambda: GaussParams(1, -1, 1), lambda: cricket.CricketParams(1, 1, 1, -1)])
def test_invalid_model_parameters_fail_before_fitting(params):
    with pytest.raises(ValueError):
        params()


def test_abnormal_count_optimization_is_not_a_success(monkeypatch):
    from ml.models import count
    monkeypatch.setattr(count.optimize, "minimize", lambda *args, **kwargs: SimpleNamespace(success=False, message="ABNORMAL", x=np.zeros(4), fun=1.0))
    model = PoissonRatings(League("Soccer/E", "Soccer", "E", "E", "count"), CountParams(365, 1))
    with pytest.raises(FitError, match="optimisation failed"):
        model._optimise(np.array([0]), np.array([0]), np.array([1]), np.array([1]), np.array([1.]), 1, np.zeros(1), np.zeros(1))


def test_empty_evaluation_and_failed_tuning_are_explicit(monkeypatch):
    league = League("Basketball/E", "Basketball", "E", "E", "gaussian", tune_seasons=(2024,))
    games = pd.DataFrame(columns=archive.COLUMNS)
    with pytest.raises(FitError, match="no evaluation"):
        backtest.evaluate(league, {}, (2025,), games)
    monkeypatch.setattr(backtest, "_score_params", lambda *args: (np.inf, 0))
    with pytest.raises(FitError, match="no tuning candidate"):
        backtest.tune(league, games, log=lambda *a: None)
    assert report.development_verdict(pd.DataFrame(), (2025,))["overall"] == "FAIL_DEVELOPMENT"


@pytest.mark.parametrize("odds", [[1.01, 1.01], [1.1, 1.1, 1.1], [100, 100]])
def test_devig_root_brackets_cover_extreme_valid_vectors(odds):
    for method in devig.METHODS.values():
        p = method(odds)
        assert np.isfinite(p).all() and (p >= 0).all() and p.sum() == pytest.approx(1)


@pytest.mark.parametrize("odds", [[1, 2], [np.nan, 2], [-2, 3], [np.inf, 2]])
def test_bad_odds_and_stakes_do_not_create_signals(odds):
    for method in devig.METHODS.values():
        with pytest.raises(ValueError):
            method(odds)
    with pytest.raises(ValueError):
        kelly.cap_slate(np.array([-.1, .2]))
    with pytest.raises(ValueError):
        kelly.kelly_full(.8, 2, .3)


def test_no_bet_policy_reports_a_complete_unchanged_bankroll():
    frame = pd.DataFrame({"wk": ["w1"], "stake_TEST": [0.], "won_k": [0], "o_k": [2], "clv_k": [-.1]})
    summary = lab.simulate(frame, "TEST")
    assert summary["n_bets"] == summary["executed_bets"] == 0
    assert summary["final_bankroll"] == 1 and summary["pnl"] == 0
    assert "mean_clv" in summary and "roi" in summary


def test_price_join_rejects_duplicate_matches():
    frame = pd.DataFrame({"season": [2025], "date": [pd.Timestamp("2025-01-01")], "home": ["A"], "away": ["B"]})
    with pytest.raises(ValueError, match="one-to-one"):
        lab.join(frame, pd.concat([frame, frame]))


def test_invalid_bandit_updates_leave_state_unchanged():
    learner = bandit.LinTS(2)
    before = [a.copy() for a in learner.A]
    for action, reward in [(-1, 0), (0, np.nan)]:
        with pytest.raises(ValueError):
            learner.update(action, np.ones(2), reward)
    assert all(np.array_equal(a, b) for a, b in zip(before, learner.A))
    full = bandit.FullInfoRidge(2)
    with pytest.raises(ValueError):
        full.update_all(np.ones(2), np.array([1.]))


def test_settlement_respects_away_under_failure_and_endpoint():
    rows = [dict(shadow_row_id=str(i), event_key="E", family=family, orientation=side, line=line, endpoint="FULL") for i, (family, side, line) in enumerate([("HANDICAP", "AWAY", 4), ("TOTAL", "UNDER", 10), ("WRONG", "OVER", 1), ("TOTAL", "OVER", np.nan)])]
    rows.append({**rows[0], "shadow_row_id": "failed", "status": "NOT_ISSUED:FIT_FAILED"})
    forecasts = pd.DataFrame(rows)
    finals = pd.DataFrame([dict(event_key="E", hs=5, as_=2, endpoint="FULL")])
    settled = lane.settle_rows(forecasts, finals, "source", "B").set_index("shadow_row_id")
    assert settled.loc["0", "result"] == settled.loc["1", "result"] == "WIN"
    assert settled.loc["2", "result"] == settled.loc["3", "result"] == settled.loc["failed", "result"] == "UNRESOLVED"
    finals["endpoint"] = "REGULATION"
    assert set(lane.settle_rows(forecasts, finals, "source", "B").result) == {"UNRESOLVED"}


def test_model_directory_traversal_and_input_drift_are_rejected(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="directory name"):
        lane.reveal(tmp_path / "unused.csv", "..")
    from ml import run
    monkeypatch.setattr(run, "code_digest", lambda: "code")
    with pytest.raises(RuntimeError, match="archive inputs changed"):
        run.finish_receipt({"code_sha256": "code"}, [("archive inputs", "before", lambda: "after")])
    assert "completed_utc" in run.finish_receipt({"code_sha256": "code"}, [("archive inputs", "same", lambda: "same")])


def test_cli_does_not_silently_succeed_on_mistyped_competition(monkeypatch):
    from ml import run
    monkeypatch.setattr(run, "discover", lambda: [])
    with pytest.raises(ValueError, match="existing modellable"):
        run.run_all(1, ["Missing/Competition"])


@pytest.mark.parametrize("complete", [True, False])
def test_cricket_report_requires_full_season_coverage_and_admission(tmp_path, monkeypatch, complete):
    monkeypatch.setattr(writers, "SHADOW_ROOT", tmp_path)
    monkeypatch.setattr(metrics, "paired_week_interval", lambda *args: dict(mean=-.1, lo=-.2, hi=-.05, k_weeks=8, status="BELOW_ZERO"))
    frame = pd.DataFrame([dict(season=season, date=pd.Timestamp(f"{season}-01-01"), event_id=f"E{season}", bat="A", bowl="B", venue="V", runs=150, line=149.5) for season in ([2024, 2025] if complete else [2025])])
    for lv in ("C0", "C1", "C2", "C2PRE"):
        for suffix, value in [("crps", 5), ("brier_over", .1), ("in80", 1), ("pit", .5), ("mean", 150), ("sigma", 20), ("p_over", .5)]:
            frame[f"{lv}_{suffix}"] = value
    lg = League("Cricket One-Day Format/Example", "Cricket One-Day Format", "Example", "EXAMPLE", "cricket", overs_cap=50, history_seasons=12, test_seasons=(2024, 2025), tune_seasons=(2020,))
    row = writers.write_cricket(dict(league=lg, test=frame, params="fixture", dropped={}, data=frame, seconds=0, tune_table=pd.DataFrame({"objective": [1.]})), {})
    card = (tmp_path / "EXAMPLE" / "MODEL_CARD.md").read_text(encoding="utf8")
    assert row["status"] == ("DATA_HOLD" if complete else "DEVELOPMENT_ONLY")
    assert f"Status: `{row['status']}`" in card
    assert "earlier IPL" not in (tmp_path / "EXAMPLE" / "DEVELOPMENT_RESULTS.md").read_text(encoding="utf8")


def test_bad_quote_rows_are_counted_and_missing_captures_are_schema_valid(tmp_path, monkeypatch):
    monkeypatch.setattr(lab, "FD_DIR", tmp_path)
    assert lab.load_prices().empty
    rows = [{"Date": "not a date", "HomeTeam": "A", "AwayTeam": "B", "FTR": "H", **{col: "2" for col in ("PSH", "PSD", "PSA", "PSCH", "PSCD", "PSCA")}}]
    with (tmp_path / "2025_fixture.csv").open("w", newline="", encoding="utf8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    loaded = lab.load_prices()
    assert loaded.empty and loaded.attrs["invalid_price_rows"] == 1


def test_empty_baseball_loader_preserves_schema(tmp_path, monkeypatch):
    lg, _ = source(tmp_path, monkeypatch, [result(**{"Home Score": ""})], "Baseball")
    games, receipt = archive.load_league(lg)
    assert games.empty and list(games.columns) == archive.COLUMNS and receipt.rows_kept == 0


@pytest.mark.parametrize("unit", ["ov", "overs", "OV"])
def test_real_cricket_overs_unit_is_accepted(tmp_path, monkeypatch, unit):
    lg, _ = source(tmp_path, monkeypatch, [innings(**{"First Innings Overs": f"20.0 {unit}"})], "Cricket T20")
    games, _ = cricket.load_cricket(replace(lg, overs_cap=20))
    assert len(games) == 1 and games.iloc[0].runs == 150


def test_discovery_does_not_crash_on_infinite_observed_score(tmp_path, monkeypatch):
    from ml import config
    source(tmp_path, monkeypatch, [result(**{"Home Score": "inf"}), result(**{"Game ID": "E2"})])
    monkeypatch.setattr(config, "ARCHIVE", tmp_path)
    config._discover_cached.cache_clear()
    try:
        routes = config.discover()
        assert len(routes) == 1 and routes[0].status == "NOT_MODELLED"
    finally:
        config._discover_cached.cache_clear()


@pytest.mark.parametrize("engine", ["gaussian", "dixon_coles", "count"])
@pytest.mark.parametrize("n_teams", [4, 6])
def test_rolling_evaluation_keeps_cutoff_coherence_and_missing_fit_scores(engine, n_teams):
    from ml.tests.test_models import synthetic
    games, _, _ = synthetic(n_teams=n_teams, kind="normal" if engine == "gaussian" else "poisson")
    lg = League("Example/E", "Basketball" if engine == "gaussian" else "Soccer", "E", "E", engine)
    params = dict(half_life_days=365, ridge=2)
    if engine == "gaussian":
        params["cov_inflation"] = 1.1
    evaluated = backtest.evaluate(lg, params, (2021,), games, log=lambda *args: None)
    assert len(evaluated) == len(games[games.season == 2021])
    assert (evaluated.fit_date <= evaluated.date).all()
    issued = evaluated.MODEL_status.str.startswith("FROZEN")
    assert issued.any()
    assert np.isfinite(evaluated.loc[issued, "MODEL_brier_home"]).all()
    assert np.allclose(evaluated.loc[issued, ["MODEL_p_home", "MODEL_p_draw", "MODEL_p_away"]].sum(axis=1), 1)
    if n_teams == 6:
        assert issued.all()
    else:
        assert (~issued).any()  # Legitimately insufficient early history is retained, never default-priced.
        assert evaluated.loc[~issued, "MODEL_brier_home"].isna().all()
        assert evaluated.loc[~issued, "y_over"].isna().all()
