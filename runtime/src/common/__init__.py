"""Common utilities for identity, provenance, contracts, splits, calibration, evaluation, ratings, Dixon-Coles, distributional models, stacking, and BigQuery ML."""

from .identity import SportIdentity, MatchIdentity, Contract, ContractType
from .provenance import ProvenanceAuditor, DataLeakageError, PointInTimeFeatureStore
from .contracts import ScoreDistribution, DerivedContracts
from .splits import PurgedRollingOriginSplit, ChronologicalSplit
from .calibration import PlattScaler, IsotonicCalibrator, TemperatureScaler, compute_ece, compute_calibration_slope
from .evaluation import (
    brier_score,
    multiclass_brier_score,
    log_loss,
    crps_score,
    murphy_decomposition,
    FixedCohortEvaluator
)
from .ratings import EloRatingEngine, BradleyTerryDrawEngine
from .dixon_coles import DixonColesEngine
from .distributional import (
    NegativeBinomialCountRegressor,
    StudentTJointScoreModel,
    QuantileDistributionReconstructor
)
from .stacking import ChronologicalStacker
from .bigquery_ml import BigQueryMLSQLGenerator

__all__ = [
    "SportIdentity",
    "MatchIdentity",
    "Contract",
    "ContractType",
    "ProvenanceAuditor",
    "DataLeakageError",
    "PointInTimeFeatureStore",
    "ScoreDistribution",
    "DerivedContracts",
    "PurgedRollingOriginSplit",
    "ChronologicalSplit",
    "PlattScaler",
    "IsotonicCalibrator",
    "TemperatureScaler",
    "compute_ece",
    "compute_calibration_slope",
    "brier_score",
    "multiclass_brier_score",
    "log_loss",
    "crps_score",
    "murphy_decomposition",
    "FixedCohortEvaluator",
    "EloRatingEngine",
    "BradleyTerryDrawEngine",
    "DixonColesEngine",
    "NegativeBinomialCountRegressor",
    "StudentTJointScoreModel",
    "QuantileDistributionReconstructor",
    "ChronologicalStacker",
    "BigQueryMLSQLGenerator",
]
