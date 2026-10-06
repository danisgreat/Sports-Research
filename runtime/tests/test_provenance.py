"""Unit tests for point-in-time provenance and data leakage protection."""

from datetime import datetime, timezone, timedelta
import pandas as pd
import pytest

from runtime.src.common.provenance import (
    ProvenanceAuditor,
    DataLeakageError,
    PointInTimeFeatureStore
)


def test_provenance_auditor_clean():
    auditor = ProvenanceAuditor()
    t_cutoff = datetime(2026, 10, 10, 12, 0, 0, tzinfo=timezone.utc)
    t_known = t_cutoff - timedelta(hours=2)

    auditor.verify_point_in_time(
        match_id="match_123",
        feature_name="team_pace",
        source_provider="nba_stats",
        known_at=t_known,
        cutoff_at=t_cutoff
    )
    assert len(auditor.audit_trail) == 1
    assert auditor.audit_trail[0].match_id == "match_123"


def test_provenance_auditor_raises_on_leakage():
    auditor = ProvenanceAuditor()
    t_cutoff = datetime(2026, 10, 10, 12, 0, 0, tzinfo=timezone.utc)
    t_leaked = t_cutoff + timedelta(minutes=5)

    with pytest.raises(DataLeakageError) as exc_info:
        auditor.verify_point_in_time(
            match_id="match_123",
            feature_name="final_score",
            source_provider="nba_stats",
            known_at=t_leaked,
            cutoff_at=t_cutoff
        )
    assert "Data leakage detected" in str(exc_info.value)


def test_feature_store_filtering():
    store = PointInTimeFeatureStore()
    t_cutoff = datetime(2026, 10, 10, 12, 0, 0, tzinfo=timezone.utc)
    
    store.insert_feature("match_1", "pace", 102.5, t_cutoff - timedelta(days=1), "nba_stats")
    
    features = store.get_features_as_of("match_1", t_cutoff)
    assert features["pace"] == 102.5


def test_feature_store_dataframe_leakage():
    store = PointInTimeFeatureStore()
    t_cutoff = datetime(2026, 10, 10, 12, 0, 0, tzinfo=timezone.utc)

    df = pd.DataFrame({
        "entity_id": ["e1", "e2"],
        "known_at": [
            datetime(2026, 10, 10, 10, 0, 0, tzinfo=timezone.utc),
            datetime(2026, 10, 10, 14, 0, 0, tzinfo=timezone.utc)  # Leaked!
        ]
    })

    with pytest.raises(DataLeakageError):
        store.filter_dataframe(df, "known_at", t_cutoff)


def test_feature_store_insertion_order_independence():
    """Verify that inserting an older observation after a newer one does not overwrite the newer value."""
    store = PointInTimeFeatureStore()
    t_cutoff = datetime(2026, 10, 10, 12, 0, 0, tzinfo=timezone.utc)

    # Insert newer observation first
    store.insert_feature(
        "team_1", "rating", 1650.0,
        known_at=t_cutoff - timedelta(hours=1),
        source="elo_v2"
    )

    # Insert older observation second (e.g. out-of-order ingestion)
    store.insert_feature(
        "team_1", "rating", 1500.0,
        known_at=t_cutoff - timedelta(days=5),
        source="elo_v1"
    )

    # Also insert future observation (should not be selected or raise leakage for cutoff query)
    store.insert_feature(
        "team_1", "rating", 1700.0,
        known_at=t_cutoff + timedelta(hours=2),
        source="elo_future"
    )

    features = store.get_features_as_of("team_1", t_cutoff)
    assert features["rating"] == 1650.0  # Must be the latest as-of cutoff (1650.0), NOT 1500.0 or 1700.0


