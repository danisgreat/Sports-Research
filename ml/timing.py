"""Shared TIMING-v3 declarations. Checks consistency, not the truth of an official observation."""
from datetime import datetime
from urllib.parse import urlparse

FIELDS = ("research_started_at", "not_started_observed_at", "not_started_source", "outcome_exposure")


def clock(value, name):
    try:
        t = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if t.utcoffset() is None:
            raise ValueError()
        return t
    except (ValueError, AttributeError):
        raise ValueError(f"header: {name} must be an offset-aware ISO timestamp") from None


def problems(meta, *, actual_start=None):
    errors = [f"header: timing PRE_START_RESEARCH requires {f}" for f in FIELDS if not meta.get(f)]
    if errors:
        return errors
    if meta["outcome_exposure"] != "NONE_RECORDED":
        errors.append("header: PRE_START_RESEARCH requires outcome_exposure NONE_RECORDED; an exposed card is not a forecast of record")
    url = urlparse(meta["not_started_source"].strip())
    if url.scheme not in ("http", "https") or not url.hostname or any(c.isspace() for c in meta["not_started_source"]):
        errors.append("header: not_started_source must be the URL of the official live page or match centre that showed play had not begun")
    try:
        began = clock(meta["research_started_at"], "research_started_at")
        seen = clock(meta["not_started_observed_at"], "not_started_observed_at")
        issued = clock(meta["issued_at"], "issued_at")
        if seen < began:
            errors.append("header: not_started_observed_at must be at or after research_started_at")
        if seen > issued or began > issued:
            errors.append("header: research_started_at and not_started_observed_at must not be after issued_at")
        if actual_start is not None:
            start = clock(actual_start, "actual_start")
            if began >= start or seen >= start:
                errors.append("header: research and not-started observation must precede verified actual first play")
    except (ValueError, KeyError) as exc:
        errors.append(str(exc))
    return errors
