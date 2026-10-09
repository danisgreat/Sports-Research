"""BigQuery as a feature warehouse and boosted-tree challenger trainer (ML-09, reduced scope).

Scope, stated plainly:
- Allowed: point-in-time feature joins (strictly before each fixture's cutoff, both teams) and BOOSTED_TREE challengers
  trained on the H0 feature tables.
- Not offered: ARIMA_PLUS / time-series forecasting of match outcomes. Outcomes are not a single autocorrelated series.
- No project or dataset is hard-coded. They come from the constructor or SPORTS_BQ_PROJECT / SPORTS_BQ_DATASET, and a
  missing value is an error rather than a default that points at somebody's production project.
The class only generates SQL text; it never connects to BigQuery.
"""

import os
import re
from typing import List, Optional

_IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_PROJECT = re.compile(r"^[a-z][a-z0-9\-]{4,28}[a-z0-9]$")
_QUOTED_TABLE = re.compile(r"^`[A-Za-z0-9_\-\.]+`$")


class BigQueryConfigError(ValueError):
    """The project or dataset is not configured, or an identifier is not safe to embed in SQL."""


def _identifier(value: str, what: str) -> str:
    if not _IDENTIFIER.match(value):
        raise BigQueryConfigError(f"{what} {value!r} is not a plain SQL identifier")
    return value


def _table(value: str) -> str:
    if not _QUOTED_TABLE.match(value):
        raise BigQueryConfigError(f"table reference {value!r} must be a back-quoted `project.dataset.table` string")
    return value


class BigQueryMLSQLGenerator:
    """Generates BigQuery ML SQL for feature joins and boosted-tree challengers."""

    def __init__(self, project_id: Optional[str] = None, dataset: Optional[str] = None):
        project_id = project_id or os.environ.get("SPORTS_BQ_PROJECT")
        dataset = dataset or os.environ.get("SPORTS_BQ_DATASET")
        if not project_id or not dataset:
            raise BigQueryConfigError("set project_id and dataset (or SPORTS_BQ_PROJECT and SPORTS_BQ_DATASET); there is no default")
        if not _PROJECT.match(project_id):
            raise BigQueryConfigError(f"project id {project_id!r} is not a valid BigQuery project id")
        self.project_id = project_id
        self.dataset = _identifier(dataset, "dataset")

    def full_table(self, table_name: str) -> str:
        return f"`{self.project_id}.{self.dataset}.{_identifier(table_name, 'table')}`"

    def _boosted_tree(self, kind: str, model_name: str, source_table: str, label_col: str, feature_cols: List[str],
                      max_depth: int, subsample: float, holdout_column: Optional[str]) -> str:
        if not feature_cols:
            raise BigQueryConfigError("at least one feature column is required")
        features = ",\n  ".join(_identifier(c, "feature column") for c in feature_cols)
        label = _identifier(label_col, "label column")
        if not 1 <= max_depth <= 15 or not 0.1 <= subsample <= 1.0:
            raise ValueError("max_depth must be in [1, 15] and subsample in [0.1, 1]")
        # A chronological split keeps the validation set later than the training set; random splits would leak the future.
        split = (f",\n  data_split_method='CUSTOM',\n  data_split_col='{_identifier(holdout_column, 'split column')}'"
                 if holdout_column else ",\n  data_split_method='SEQ',\n  data_split_eval_fraction=0.2")
        select_cols = f"{label},\n  {features}" + (f",\n  {holdout_column}" if holdout_column else "")
        return f"""CREATE OR REPLACE MODEL {self.full_table(model_name)}
OPTIONS(
  model_type='{kind}',
  input_label_cols=['{label}'],
  max_tree_depth={max_depth},
  subsample={subsample},
  learn_rate=0.05,
  early_stop=TRUE,
  min_rel_progress=0.001{split}
) AS
SELECT
  {select_cols}
FROM
  {_table(source_table)};"""

    def create_boosted_tree_classifier(self, model_name: str, source_table: str, label_col: str, feature_cols: List[str],
                                       max_depth: int = 6, subsample: float = 0.85, holdout_column: Optional[str] = None) -> str:
        """Boosted-tree classifier for a binary label; the table must be ordered by event time for the SEQ split."""
        return self._boosted_tree("BOOSTED_TREE_CLASSIFIER", model_name, source_table, label_col, feature_cols, max_depth, subsample, holdout_column)

    def create_boosted_tree_regressor(self, model_name: str, source_table: str, label_col: str, feature_cols: List[str],
                                      max_depth: int = 6, subsample: float = 0.85, holdout_column: Optional[str] = None) -> str:
        """Boosted-tree regressor for a distribution parameter (expected goals, margin, total), not for outcomes directly."""
        return self._boosted_tree("BOOSTED_TREE_REGRESSOR", model_name, source_table, label_col, feature_cols, max_depth, subsample, holdout_column)

    def batch_predict(self, model_name: str, input_table: str) -> str:
        return f"""SELECT
  *
FROM
  ML.PREDICT(MODEL {self.full_table(model_name)},
    (SELECT * FROM {_table(input_table)}));"""

    def build_point_in_time_feature_query(self, match_table: str, events_table: str, match_id_col: str, cutoff_timestamp_col: str,
                                          lookback_days: int = 365) -> str:
        """Rolling event features for BOTH teams, using only events strictly before the fixture's cutoff and inside the look-back."""
        match_id, cutoff = _identifier(match_id_col, "match id column"), _identifier(cutoff_timestamp_col, "cutoff column")
        if not 1 <= int(lookback_days) <= 3650:
            raise ValueError("lookback_days must be between 1 and 3650")
        parts = []
        for side in ("home", "away"):
            parts.append(f"""  SELECT
    m.{match_id} AS {match_id},
    '{side}' AS side,
    COUNT(e.event_id) AS n_events,
    AVG(e.metric_value) AS avg_metric
  FROM {_table(match_table)} AS m
  LEFT JOIN {_table(events_table)} AS e
    ON e.team_id = m.{side}_team_id
    AND e.event_timestamp < m.{cutoff}
    AND e.event_timestamp >= TIMESTAMP_SUB(m.{cutoff}, INTERVAL {int(lookback_days)} DAY)
  GROUP BY m.{match_id}""")
        return f"""WITH side_features AS (
{chr(10).join([parts[0], "  UNION ALL", parts[1]])}
)
SELECT
  m.*,
  h.n_events AS home_n_events,
  h.avg_metric AS home_avg_metric,
  a.n_events AS away_n_events,
  a.avg_metric AS away_avg_metric
FROM {_table(match_table)} AS m
LEFT JOIN side_features AS h ON h.{match_id} = m.{match_id} AND h.side = 'home'
LEFT JOIN side_features AS a ON a.{match_id} = m.{match_id} AND a.side = 'away';"""
