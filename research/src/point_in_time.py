"""Feature availability and lagged-result transforms with explicit missingness."""
from __future__ import annotations
from datetime import datetime, timedelta, timezone
import math
import re


def aware(value):
    result = value if isinstance(value, datetime) else datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    if result.tzinfo is None or result.utcoffset() is None:
        raise ValueError("timezone-aware timestamp required")
    return result.astimezone(timezone.utc)


def eligible_features(records, cutoff):
    """Filter declared temporal metadata; source semantics need separate review.

    A well-formed receipt hash is a reference, not verification of its body or
    its pregame meaning. This filter cannot confer live forecast admission.
    """
    cutoff = aware(cutoff)
    accepted, excluded = [], []
    seen = set()
    for record in records:
        identity = (record.get("event_id"), record.get("entity_id"), record.get("feature"))
        reason = None
        if any(not part for part in identity):
            reason = "FEATURE_IDENTITY_MISSING"
        elif identity in seen:
            reason = "DUPLICATE_FEATURE"
        elif record.get("temporal_role") != "PREGAME":
            reason = "POSTGAME_OR_UNDEFINED_TEMPORAL_ROLE"
        elif not record.get("available_at_utc"):
            reason = "AVAILABILITY_NOT_RECORDED"
        elif not re.fullmatch(r"[0-9a-f]{64}",str(record.get("source_receipt_sha256",""))):
            reason = "MISSING_SOURCE_RECEIPT"
        else:
            try:
                observed = aware(record["available_at_utc"])
                if observed > cutoff:
                    reason = "AVAILABLE_AFTER_CUTOFF"
                elif record.get("value") is None:
                    reason = "VALUE_MISSING"
                elif isinstance(record.get("value"),float) and not math.isfinite(record["value"]):
                    reason = "NONFINITE_FEATURE_VALUE"
            except ValueError:
                reason = "INVALID_AVAILABILITY_TIMESTAMP"
        seen.add(identity)
        if reason:
            excluded.append({"identity": identity, "reason": reason})
        else:
            accepted.append(dict(record))
    return {"records": accepted, "excluded": excluded, "cutoff_utc": cutoff.isoformat(),
            "admission_basis":"DECLARED_FEATURE_METADATA_ONLY; SOURCE_BODY_AND_FIELD_REVIEW_REQUIRED", "live_admission":False}


def lagged_form(events, team_id, cutoff, n=10, allow_date_assumption=False):
    """One event once; no awards, summaries, actual lineups or future games.

    DATE_PLUS_2_DAYS is explicitly an archive backtest assumption, never proof
    of historical receipt availability. Operational snapshots should use the
    actual verified availability timestamp.
    """
    cutoff = aware(cutoff)
    if isinstance(n,bool) or not isinstance(n,int) or n<=0:
        raise ValueError("positive integer rolling window required")
    eligible, excluded = [], []
    seen = set()
    for row in events:
        if team_id not in (row.get("home_team_id"), row.get("away_team_id")):
            continue
        event_id = row.get("event_id")
        reason = None
        if not event_id or event_id in seen:
            reason = "DUPLICATE_OR_MISSING_EVENT_ID"
        elif str(row.get("training_eligible", False)).lower() != "true":
            reason = "SOURCE_OR_QUALITY_GATE_FAILED"
        elif row.get("phase") not in ("Regular Season", "regular", "REGULAR_SEASON"):
            reason = "ENDPOINT_OR_STAGE_OUT_OF_SCOPE"
        elif row.get("available_at_utc"):
            available = aware(row["available_at_utc"])
        elif allow_date_assumption and row.get("event_date"):
            available = datetime.fromisoformat(row["event_date"]).replace(tzinfo=timezone.utc)+timedelta(days=2)
        else:
            reason = "RESULT_AVAILABILITY_UNKNOWN"
        seen.add(event_id)
        if reason is None and available >= cutoff:
            reason = "RESULT_NOT_AVAILABLE_BEFORE_CUTOFF"
        if reason:
            excluded.append({"event_id": event_id, "reason": reason}); continue
        hs, aws = float(row["home_score"]), float(row["away_score"])
        if not all(math.isfinite(v) and v >= 0 for v in (hs, aws)):
            raise ValueError("invalid result scores")
        home = row["home_team_id"] == team_id
        eligible.append((available, event_id, hs if home else aws, aws if home else hs))
    eligible.sort(key=lambda r:(r[0], r[1]))
    sample = eligible[-n:]
    return {"team_id":team_id, "n":len(sample),
            "points_for":sum(r[2] for r in sample)/len(sample) if sample else None,
            "points_against":sum(r[3] for r in sample)/len(sample) if sample else None,
            "event_ids":[r[1] for r in sample], "excluded":excluded,
            "availability_policy":"DATE_PLUS_2_DAYS_ASSUMPTION" if allow_date_assumption else "VERIFIED_AVAILABILITY_REQUIRED"}
