"""Point-in-time provenance tracking and data leakage prevention."""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional
import pandas as pd


class DataLeakageError(ValueError):
    """Raised when data known after the decision cutoff is accessed or used."""
    pass


@dataclass(frozen=True)
class AuditRecord:
    """Provenance and lineage metadata for an extracted feature or observation."""
    match_id: str
    feature_name: str
    source_provider: str
    known_at: datetime
    cutoff_at: datetime
    record_hash: str
    grain: str


class ProvenanceAuditor:
    """Audits data access to ensure strict point-in-time chronological safety."""

    def __init__(self):
        self._audit_log: List[AuditRecord] = []

    def verify_point_in_time(
        self,
        match_id: str,
        feature_name: str,
        source_provider: str,
        known_at: datetime,
        cutoff_at: datetime,
        record_hash: str = "",
        grain: str = "game"
    ) -> None:
        """Verify that known_at <= cutoff_at. Raises DataLeakageError on violation."""
        if known_at > cutoff_at:
            delta = (known_at - cutoff_at).total_seconds()
            raise DataLeakageError(
                f"Data leakage detected for {match_id} (feature: {feature_name}, source: {source_provider}): "
                f"known_at ({known_at.isoformat()}) is {delta:.1f}s after cutoff_at ({cutoff_at.isoformat()})"
            )

        record = AuditRecord(
            match_id=match_id,
            feature_name=feature_name,
            source_provider=source_provider,
            known_at=known_at,
            cutoff_at=cutoff_at,
            record_hash=record_hash,
            grain=grain
        )
        self._audit_log.append(record)

    @property
    def audit_trail(self) -> List[AuditRecord]:
        return list(self._audit_log)


class PointInTimeFeatureStore:
    """Point-in-time feature store enforcing strict cutoff filtering."""

    def __init__(self, auditor: Optional[ProvenanceAuditor] = None):
        self.auditor = auditor or ProvenanceAuditor()
        self._store: Dict[str, List[Dict[str, Any]]] = {}

    def insert_feature(
        self,
        entity_id: str,
        feature_name: str,
        feature_value: Any,
        known_at: datetime,
        source: str
    ) -> None:
        if entity_id not in self._store:
            self._store[entity_id] = []
        self._store[entity_id].append({
            "feature_name": feature_name,
            "feature_value": feature_value,
            "known_at": known_at,
            "source": source
        })

    def get_features_as_of(
        self,
        entity_id: str,
        cutoff_at: datetime
    ) -> Dict[str, Any]:
        """Retrieve features for entity_id strictly known on or before cutoff_at."""
        if entity_id not in self._store:
            return {}

        results: Dict[str, Any] = {}
        for entry in self._store[entity_id]:
            self.auditor.verify_point_in_time(
                match_id=entity_id,
                feature_name=entry["feature_name"],
                source_provider=entry["source"],
                known_at=entry["known_at"],
                cutoff_at=cutoff_at
            )
            # Retain the most recently known value before or at cutoff
            results[entry["feature_name"]] = entry["feature_value"]

        return results

    def filter_dataframe(
        self,
        df: pd.DataFrame,
        known_at_col: str,
        cutoff_at: datetime
    ) -> pd.DataFrame:
        """Filter a DataFrame ensuring no records with known_at > cutoff_at exist."""
        if known_at_col not in df.columns:
            raise KeyError(f"Column '{known_at_col}' not found in DataFrame")

        # Convert to datetime if string
        ts_series = pd.to_datetime(df[known_at_col])
        leaking_mask = ts_series > cutoff_at
        if leaking_mask.any():
            count = leaking_mask.sum()
            raise DataLeakageError(f"DataFrame contains {count} records known after cutoff {cutoff_at.isoformat()}")

        return df[~leaking_mask].copy()

