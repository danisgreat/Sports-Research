"""BigQuery AI & ML SQL generator for sports analytics and automated forecasting.

Supports:
- Cloud Time-Series Forecasting: ARIMA_PLUS & AI.FORECAST
- Distributed In-Warehouse ML: Boosted Tree Classifiers & Regressors
- Point-in-time warehouse joins with strict temporal cutoff guards
"""

from typing import List, Optional


class BigQueryMLSQLGenerator:
    """Generates standard Google Cloud BigQuery ML SQL statements for model training and inference."""

    def __init__(self, project_id: str = "sports-analytics-prod", dataset: str = "sports_ml"):
        self.project_id = project_id
        self.dataset = dataset

    def full_table(self, table_name: str) -> str:
        return f"`{self.project_id}.{self.dataset}.{table_name}`"

    def create_arima_plus_model(
        self,
        model_name: str,
        source_table: str,
        time_col: str,
        target_col: str,
        id_col: Optional[str] = None,
        horizon: int = 14,
        confidence_level: float = 0.95
    ) -> str:
        """Generate SQL to train an ARIMA_PLUS multi-series forecasting model."""
        id_clause = f", time_series_id_col='{id_col}'" if id_col else ""
        sql = f"""CREATE OR REPLACE MODEL {self.full_table(model_name)}
OPTIONS(
  model_type='ARIMA_PLUS',
  time_series_timestamp_col='{time_col}',
  time_series_data_col='{target_col}'{id_clause},
  horizon={horizon},
  auto_arima=TRUE,
  data_frequency='AUTO_FREQUENCY'
) AS
SELECT
  {f"{id_col}, " if id_col else ""}{time_col},
  {target_col}
FROM
  {source_table}
WHERE
  {target_col} IS NOT NULL;"""
        return sql

    def forecast_arima_plus(
        self,
        model_name: str,
        horizon: int = 14,
        confidence_level: float = 0.95
    ) -> str:
        """Generate SQL to forecast from a trained ARIMA_PLUS model."""
        sql = f"""SELECT
  *
FROM
  ML.FORECAST(MODEL {self.full_table(model_name)},
    STRUCT({horizon} AS horizon, {confidence_level} AS confidence_level));"""
        return sql

    def create_boosted_tree_classifier(
        self,
        model_name: str,
        source_table: str,
        label_col: str,
        feature_cols: List[str],
        max_depth: int = 6,
        subsample: float = 0.85
    ) -> str:
        """Generate SQL to train a BigQuery ML Boosted Tree classifier."""
        features_str = ",\n  ".join(feature_cols)
        sql = f"""CREATE OR REPLACE MODEL {self.full_table(model_name)}
OPTIONS(
  model_type='BOOSTED_TREE_CLASSIFIER',
  input_label_cols=['{label_col}'],
  max_tree_depth={max_depth},
  subsample={subsample},
  learn_rate=0.05,
  early_stop=TRUE,
  min_rel_progress=0.001
) AS
SELECT
  {label_col},
  {features_str}
FROM
  {source_table};"""
        return sql

    def batch_predict(
        self,
        model_name: str,
        input_table: str
    ) -> str:
        """Generate SQL to run batch predictions against a BigQuery ML model."""
        sql = f"""SELECT
  *
FROM
  ML.PREDICT(MODEL {self.full_table(model_name)},
    (SELECT * FROM {input_table}));"""
        return sql

    def build_point_in_time_feature_query(
        self,
        match_table: str,
        events_table: str,
        match_id_col: str,
        cutoff_timestamp_col: str,
        lookback_days: int = 365
    ) -> str:
        """Generate BigQuery SQL for joining match metadata with event history strictly before cutoff."""
        sql = f"""WITH filtered_events AS (
  SELECT
    m.{match_id_col},
    e.team_id,
    COUNT(e.event_id) AS n_events,
    AVG(e.metric_value) AS avg_metric
  FROM
    {match_table} AS m
  INNER JOIN
    {events_table} AS e
    ON e.team_id = m.home_team_id
    AND e.event_timestamp < m.{cutoff_timestamp_col}
    AND e.event_timestamp >= TIMESTAMP_SUB(m.{cutoff_timestamp_col}, INTERVAL {lookback_days} DAY)
  GROUP BY
    m.{match_id_col},
    e.team_id
)
SELECT
  m.*,
  fe.n_events,
  fe.avg_metric
FROM
  {match_table} AS m
LEFT JOIN
  filtered_events AS fe
  ON m.{match_id_col} = fe.{match_id_col};"""
        return sql

