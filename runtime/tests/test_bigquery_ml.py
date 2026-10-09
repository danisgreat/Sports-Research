"""BigQuery SQL generation: reduced scope, configuration-driven, point-in-time safe (ML-09)."""

import pytest

from runtime.src.common.bigquery_ml import BigQueryConfigError, BigQueryMLSQLGenerator


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    monkeypatch.delenv("SPORTS_BQ_PROJECT", raising=False)
    monkeypatch.delenv("SPORTS_BQ_DATASET", raising=False)


def test_no_hard_coded_project_or_dataset(monkeypatch):
    with pytest.raises(BigQueryConfigError):
        BigQueryMLSQLGenerator()
    monkeypatch.setenv("SPORTS_BQ_PROJECT", "my-sports-proj")
    monkeypatch.setenv("SPORTS_BQ_DATASET", "h0_features")
    gen = BigQueryMLSQLGenerator()
    assert gen.full_table("nba_features") == "`my-sports-proj.h0_features.nba_features`"
    assert "sports-analytics-prod" not in gen.full_table("x")
    with pytest.raises(BigQueryConfigError):
        BigQueryMLSQLGenerator("x", "ds")                      # not a valid project id
    with pytest.raises(BigQueryConfigError):
        BigQueryMLSQLGenerator("test-proj", "bad dataset; DROP")


def test_time_series_forecasting_of_outcomes_is_not_offered():
    gen = BigQueryMLSQLGenerator("test-proj", "sports_models")
    assert not hasattr(gen, "create_arima_plus_model") and not hasattr(gen, "forecast_arima_plus")


def test_boosted_tree_classifier_and_regressor_generation():
    gen = BigQueryMLSQLGenerator("test-proj", "sports_models")
    sql = gen.create_boosted_tree_classifier("nfl_drive_outcome_model", "`test-proj.sports_models.nfl_drives`", "outcome_is_td",
                                             ["yardline_100", "down", "ydstogo", "qb_epa_prior"])
    assert "model_type='BOOSTED_TREE_CLASSIFIER'" in sql and "input_label_cols=['outcome_is_td']" in sql and "qb_epa_prior" in sql
    assert "data_split_method='SEQ'" in sql                                    # chronological validation, never a random split
    reg = gen.create_boosted_tree_regressor("epl_lambda", "`test-proj.sports_models.epl_h0`", "home_goals", ["home_elo", "rest_days"], holdout_column="is_eval")
    assert "BOOSTED_TREE_REGRESSOR" in reg and "data_split_col='is_eval'" in reg and "home_elo" in reg
    with pytest.raises(BigQueryConfigError):
        gen.create_boosted_tree_classifier("m", "`test-proj.sports_models.t`", "y", [])
    with pytest.raises(BigQueryConfigError):
        gen.create_boosted_tree_classifier("m", "t; DROP TABLE x", "y", ["a"])
    with pytest.raises(BigQueryConfigError):
        gen.create_boosted_tree_classifier("m", "`test-proj.sports_models.t`", "y", ["a b"])
    with pytest.raises(ValueError):
        gen.create_boosted_tree_classifier("m", "`test-proj.sports_models.t`", "y", ["a"], max_depth=99)


def test_point_in_time_query_covers_both_teams_and_never_peeks():
    gen = BigQueryMLSQLGenerator("test-proj", "sports_models")
    sql = gen.build_point_in_time_feature_query("`prod.nba.matches`", "`prod.nba.events`", "match_id", "tipoff_timestamp", 180)
    assert sql.count("e.event_timestamp < m.tipoff_timestamp") == 2           # home and away
    assert "e.team_id = m.home_team_id" in sql and "e.team_id = m.away_team_id" in sql
    assert "INTERVAL 180 DAY" in sql and "home_n_events" in sql and "away_avg_metric" in sql
    assert "<=" not in sql
    with pytest.raises(ValueError):
        gen.build_point_in_time_feature_query("`prod.nba.matches`", "`prod.nba.events`", "match_id", "tipoff_timestamp", 0)
    assert gen.batch_predict("m", "`prod.nba.upcoming`").startswith("SELECT")
