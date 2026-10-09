"""Common utilities for identity, provenance, contracts, splits, calibration, evaluation, ratings, Dixon-Coles, distributional models, stacking, and BigQuery ML."""

from .identity import SportIdentity, MatchIdentity, Contract, ContractType
from .provenance import ProvenanceAuditor, DataLeakageError, PointInTimeFeatureStore
from .contracts import ScoreDistribution, DerivedContracts
from .splits import PurgedRollingOriginSplit, ChronologicalSplit
from .calibration import PlattScaler, IsotonicCalibrator, TemperatureScaler, BetaCalibrator, compute_ece, compute_calibration_slope
from .calibration_layer import CalibrationLayer
from .errors import FitFailed, NotFitted, MissingInputs, UnknownTeam, InsufficientData, MissingScore
from .evaluation import (
    brier_score,
    multiclass_brier_score,
    log_loss,
    crps_score,
    murphy_decomposition,
    FixedCohortEvaluator
)
from .ratings import EloRatingEngine, GlickoRating, SurfaceElo, BradleyTerryDrawEngine
from .dixon_coles import DixonColesEngine
from .distributional import (
    NegativeBinomialCountRegressor,
    StudentTJointScoreModel,
    QuantileDistributionReconstructor
)
from .stacking import ChronologicalStacker, FamilyStacker, evaluate_stack
from .uncertainty import block_bootstrap, wilson_interval, week_block_ids
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
    "BetaCalibrator",
    "CalibrationLayer",
    "FitFailed",
    "NotFitted",
    "MissingInputs",
    "UnknownTeam",
    "InsufficientData",
    "MissingScore",
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
    "GlickoRating",
    "SurfaceElo",
    "BradleyTerryDrawEngine",
    "DixonColesEngine",
    "NegativeBinomialCountRegressor",
    "StudentTJointScoreModel",
    "QuantileDistributionReconstructor",
    "ChronologicalStacker",
    "FamilyStacker",
    "evaluate_stack",
    "block_bootstrap",
    "wilson_interval",
    "week_block_ids",
    "BigQueryMLSQLGenerator",
]
