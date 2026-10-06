"""Unit tests for BigQuery AI & ML SQL generation."""

from runtime.src.common.bigquery_ml import BigQueryMLSQLGenerator


def test_bigquery_arima_plus_generation():
    gen = BigQueryMLSQLGenerator(project_id="test-proj", dataset="sports_models")
    sql = gen.create_arima_plus_model(
        model_name="team_pace_forecast",
        source_table="`test-proj.sports_models.nba_team_history`",
        time_col="game_date",
        target_col="possessions",
        id_col="team_id",
        horizon=10
    )
    assert "model_type='ARIMA_PLUS'" in sql
    assert "`test-proj.sports_models.team_pace_forecast`" in sql
    assert "time_series_timestamp_col='game_date'" in sql
    assert "time_series_id_col='team_id'" in sql
    assert "horizon=10" in sql


def test_bigquery_boosted_tree_generation():
    gen = BigQueryMLSQLGenerator(project_id="test-proj", dataset="sports_models")
    sql = gen.create_boosted_tree_classifier(
        model_name="nfl_drive_outcome_model",
        source_table="`test-proj.sports_models.nfl_drives`",
        label_col="outcome_is_td",
        feature_cols=["yardline_100", "down", "ydstogo", "qb_epa_prior"]
    )
    assert "model_type='BOOSTED_TREE_CLASSIFIER'" in sql
    assert "input_label_cols=['outcome_is_td']" in sql
    assert "qb_epa_prior" in sql


def test_point_in_time_query_generation():
    gen = BigQueryMLSQLGenerator()
    sql = gen.build_point_in_time_feature_query(
        match_table="`prod.nba.matches`",
        events_table="`prod.nba.events`",
        match_id_col="match_id",
        cutoff_timestamp_col="tipoff_timestamp",
        lookback_days=180
    )
    assert "event_timestamp < m.tipoff_timestamp" in sql
    assert "INTERVAL 180 DAY" in sql

