#!/usr/bin/env python3
"""Fail-closed preflight for Sports Research forecast manifests.


This validator enforces the current deep-research controls, including the 2026-09-21 cricket source patch, before a normal
forecast may be issued. It intentionally validates governance and information
hygiene; it does not claim predictive accuracy.
"""
from __future__ import annotations


import argparse
import json
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from pathlib import Path
from typing import Any, Iterable


METHOD_VERSION = "MDS-2026.09.19-v4.3"
CONTROL_REVISION = "CR-2026.09.21-3"


PROHIBITED_SOURCE_TOKENS = {
    "rotowire", "rotogrinders", "fptrack", "sportsbook", "bookmaker",
    "betting", "best bet", "best-bet", "tipster", "picks service",
    "odds aggregator", "prediction market", "fantasypros", "numberfire",
    "daily fantasy", "dfs", "draftkings", "fanduel", "fantasy projection",
    "fantasy ownership", "waiver advice",
}


PROHIBITED_SOURCE_CLASSES = {
    "PROHIBITED_BETTING_MARKET",
    "PROHIBITED_FANTASY_DFS",
    "PROHIBITED_DERIVED_CONTAMINATION",
}


VALID_SOURCE_CLASSES = {
    "VALID_PRIMARY_FIELD_OWNER",
    "VALID_PRIMARY_TEAM",
    "VALID_SECONDARY_INDEPENDENT",
    "HISTORICAL_STRUCTURED_CANDIDATE",
}


RESERVED_MODEL_INPUT_TOKENS = {
    "contract_line", "requested_line", "user_line", "market_line",
    "closing_line", "opening_line", "sportsbook_line", "bookmaker_line",
    "odds", "price", "implied_probability", "market_probability",
    "market_consensus", "betting_consensus", "line_movement",
    "fantasy_projection", "dfs_projection", "fantasy_ownership",
    "fantasy_points", "dfs_points",
}


FRESH_CRITICAL_STATES = {"CURRENT", "NOT_APPLICABLE"}




NORMAL_PREGAME_STATES = {"PREGAME", "SCHEDULED"}
MELBOURNE_TZ = ZoneInfo("Australia/Melbourne")




def parse_time_preserve_zone(value: Any, field: str, findings: list["Finding"]) -> datetime | None:
    if value in (None, ""):
        findings.append(Finding("PF-TIME-MISSING", "BLOCK", f"Missing timestamp: {field}", field))
        return None
    if not isinstance(value, str):
        findings.append(Finding("PF-TIME-TYPE", "BLOCK", f"Timestamp must be an ISO-8601 string: {field}", field))
        return None
    raw = value.strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(raw)
    except ValueError:
        findings.append(Finding("PF-TIME-PARSE", "BLOCK", f"Invalid ISO-8601 timestamp: {field}={value!r}", field))
        return None
    if dt.tzinfo is None:
        findings.append(Finding("PF-TIME-TZ", "BLOCK", f"Timestamp must include timezone: {field}", field))
        return None
    return dt




@dataclass(frozen=True)
class Finding:
    code: str
    level: str
    message: str
    path: str | None = None




def parse_time(value: Any, field: str, findings: list[Finding]) -> datetime | None:
    if value in (None, ""):
        findings.append(Finding("PF-TIME-MISSING", "BLOCK", f"Missing timestamp: {field}", field))
        return None
    if not isinstance(value, str):
        findings.append(Finding("PF-TIME-TYPE", "BLOCK", f"Timestamp must be an ISO-8601 string: {field}", field))
        return None
    raw = value.strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(raw)
    except ValueError:
        findings.append(Finding("PF-TIME-PARSE", "BLOCK", f"Invalid ISO-8601 timestamp: {field}={value!r}", field))
        return None
    if dt.tzinfo is None:
        findings.append(Finding("PF-TIME-TZ", "BLOCK", f"Timestamp must include timezone: {field}", field))
        return None
    return dt.astimezone(timezone.utc)




def walk_keys(obj: Any, prefix: str = "model_inputs") -> Iterable[tuple[str, str]]:
    if isinstance(obj, dict):
        for key, value in obj.items():
            path = f"{prefix}.{key}"
            yield path, str(key).lower()
            yield from walk_keys(value, path)
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            yield from walk_keys(value, f"{prefix}[{i}]")




def norm_text(*values: Any) -> str:
    return " ".join(str(v).lower() for v in values if v not in (None, ""))




def validate(manifest: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []


    if manifest.get("method_version") != METHOD_VERSION:
        findings.append(Finding(
            "PF-7-METHOD-VERSION", "BLOCK",
            f"method_version must be {METHOD_VERSION!r}; got {manifest.get('method_version')!r}",
            "method_version",
        ))
    if manifest.get("control_revision") != CONTROL_REVISION:
        findings.append(Finding(
            "PF-7-CONTROL-REVISION", "BLOCK",
            f"control_revision must be {CONTROL_REVISION!r}; got {manifest.get('control_revision')!r}",
            "control_revision",
        ))


    sport = str(manifest.get("sport", "")).strip().lower()
    if not sport:
        findings.append(Finding(
            "PF-SPORT", "BLOCK",
            "sport is required so sport-specific integrity controls can be applied.",
            "sport",
        ))


    event_identity = manifest.get("event_identity")
    if not isinstance(event_identity, dict):
        findings.append(Finding(
            "PF-EVENT-IDENTITY", "BLOCK",
            "event_identity object is required for venue/time/state verification.",
            "event_identity",
        ))
    else:
        required_identity = (
            "venue_city", "venue_country", "venue_timezone",
            "scheduled_local_at", "scheduled_melbourne_at",
            "melbourne_timezone", "melbourne_tz_abbr",
            "calendar_date_rollover", "event_state", "state_checked_at",
        )
        for key in required_identity:
            if key not in event_identity or event_identity.get(key) in (None, ""):
                findings.append(Finding(
                    "PF-EVENT-IDENTITY-FIELD", "BLOCK",
                    f"event_identity.{key} is required.",
                    f"event_identity.{key}",
                ))


        venue_tz_name = event_identity.get("venue_timezone")
        venue_zone = None
        if venue_tz_name:
            try:
                venue_zone = ZoneInfo(str(venue_tz_name))
            except ZoneInfoNotFoundError:
                findings.append(Finding(
                    "PF-TIMEZONE-INVALID", "BLOCK",
                    f"Unknown IANA venue timezone: {venue_tz_name!r}",
                    "event_identity.venue_timezone",
                ))


        local_dt = parse_time_preserve_zone(
            event_identity.get("scheduled_local_at"),
            "event_identity.scheduled_local_at",
            findings,
        )
        mel_dt = parse_time_preserve_zone(
            event_identity.get("scheduled_melbourne_at"),
            "event_identity.scheduled_melbourne_at",
            findings,
        )
        parse_time(event_identity.get("state_checked_at"), "event_identity.state_checked_at", findings)


        if event_identity.get("melbourne_timezone") != "Australia/Melbourne":
            findings.append(Finding(
                "PF-MELBOURNE-TZ-NAME", "BLOCK",
                "event_identity.melbourne_timezone must be 'Australia/Melbourne'.",
                "event_identity.melbourne_timezone",
            ))


        if local_dt and venue_zone:
            expected_local = local_dt.astimezone(venue_zone)
            if (
                expected_local.replace(tzinfo=None) != local_dt.replace(tzinfo=None)
                or expected_local.utcoffset() != local_dt.utcoffset()
            ):
                findings.append(Finding(
                    "PF-LOCAL-TIMEZONE-MISMATCH", "BLOCK",
                    "scheduled_local_at does not match the venue IANA timezone on that exact date.",
                    "event_identity.scheduled_local_at",
                ))


        if local_dt and mel_dt:
            if local_dt.astimezone(timezone.utc) != mel_dt.astimezone(timezone.utc):
                findings.append(Finding(
                    "PF-MELBOURNE-CONVERSION", "BLOCK",
                    "scheduled_local_at and scheduled_melbourne_at are not the same instant.",
                    "event_identity.scheduled_melbourne_at",
                ))
            expected_mel = local_dt.astimezone(MELBOURNE_TZ)
            if (
                expected_mel.replace(tzinfo=None) != mel_dt.replace(tzinfo=None)
                or expected_mel.utcoffset() != mel_dt.utcoffset()
            ):
                findings.append(Finding(
                    "PF-MELBOURNE-CONVERSION", "BLOCK",
                    "scheduled_melbourne_at is not the timezone-aware Australia/Melbourne conversion.",
                    "event_identity.scheduled_melbourne_at",
                ))
            expected_abbr = expected_mel.tzname()
            if event_identity.get("melbourne_tz_abbr") != expected_abbr:
                findings.append(Finding(
                    "PF-MELBOURNE-ABBR", "BLOCK",
                    f"melbourne_tz_abbr must be {expected_abbr!r} for this date.",
                    "event_identity.melbourne_tz_abbr",
                ))
            expected_rollover = local_dt.date() != expected_mel.date()
            if event_identity.get("calendar_date_rollover") is not expected_rollover:
                findings.append(Finding(
                    "PF-DATE-ROLLOVER", "BLOCK",
                    f"calendar_date_rollover must be {expected_rollover}.",
                    "event_identity.calendar_date_rollover",
                ))


        event_state = str(event_identity.get("event_state", "")).upper()
        if event_state not in NORMAL_PREGAME_STATES:
            findings.append(Finding(
                "PF-EVENT-STATE", "BLOCK",
                f"Normal pregame issuance requires event_state in {sorted(NORMAL_PREGAME_STATES)}; got {event_state!r}.",
                "event_identity.event_state",
            ))


    cutoff = parse_time(manifest.get("cutoff_at"), "cutoff_at", findings)
    frozen = parse_time(manifest.get("distribution_frozen_at"), "distribution_frozen_at", findings)
    compared = parse_time(manifest.get("line_compared_at"), "line_compared_at", findings)


    if frozen and cutoff and frozen < cutoff:
        findings.append(Finding(
            "PF-8-FREEZE-BEFORE-CUTOFF", "BLOCK",
            "distribution_frozen_at cannot precede cutoff_at.", "distribution_frozen_at",
        ))
    if compared and frozen and compared < frozen:
        findings.append(Finding(
            "PF-2-LINE-BEFORE-FREEZE", "BLOCK",
            "The user-supplied line/total was compared before the independent distribution was frozen.",
            "line_compared_at",
        ))


    if manifest.get("line_visible_to_model") is not False:
        findings.append(Finding(
            "PF-2-LINE-VISIBILITY", "BLOCK",
            "line_visible_to_model must be explicitly false.", "line_visible_to_model",
        ))
    if manifest.get("user_line_used_as_feature") is not False:
        findings.append(Finding(
            "PF-2-LINE-FEATURE", "BLOCK",
            "user_line_used_as_feature must be explicitly false.", "user_line_used_as_feature",
        ))


    contract = manifest.get("contract")
    if not isinstance(contract, dict):
        findings.append(Finding("PF-CONTRACT", "BLOCK", "contract must be an object.", "contract"))
    else:
        for key in ("target_id", "line"):
            if key not in contract:
                findings.append(Finding("PF-CONTRACT", "BLOCK", f"contract.{key} is required.", f"contract.{key}"))


    distribution = manifest.get("distribution")
    if not isinstance(distribution, dict):
        findings.append(Finding("PF-10-DISTRIBUTION", "BLOCK", "distribution metadata is required.", "distribution"))
    else:
        if not distribution.get("id"):
            findings.append(Finding("PF-10-DISTRIBUTION-ID", "BLOCK", "distribution.id is required.", "distribution.id"))
        if not distribution.get("hash"):
            findings.append(Finding("PF-10-DISTRIBUTION-HASH", "BLOCK", "distribution.hash is required.", "distribution.hash"))


    model_inputs = manifest.get("model_inputs", {})
    if not isinstance(model_inputs, (dict, list)):
        findings.append(Finding("PF-9-MODEL-INPUTS", "BLOCK", "model_inputs must be an object or list.", "model_inputs"))
    else:
        for path, key in walk_keys(model_inputs):
            if any(token in key for token in RESERVED_MODEL_INPUT_TOKENS):
                findings.append(Finding(
                    "PF-2-LINE-MARKET-INPUT", "BLOCK",
                    f"Prohibited market/fantasy/contract-derived model input key: {key!r}.", path,
                ))


    evidence = manifest.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        findings.append(Finding("PF-1-EVIDENCE", "BLOCK", "At least one evidence record is required.", "evidence"))
        evidence = []


    critical_by_field: dict[str, list[dict[str, Any]]] = {}
    required_evidence_fields = (
        "source_id", "provider", "source_class", "field_name", "upstream_lineage_id",
        "first_known_at", "retrieved_at", "freshness_status",
    )


    for i, record in enumerate(evidence):
        path = f"evidence[{i}]"
        if not isinstance(record, dict):
            findings.append(Finding("PF-1-EVIDENCE-RECORD", "BLOCK", "Evidence record must be an object.", path))
            continue


        for key in required_evidence_fields:
            if record.get(key) in (None, ""):
                findings.append(Finding("PF-3-PROVENANCE", "BLOCK", f"Missing required provenance field: {key}", f"{path}.{key}"))


        source_class = str(record.get("source_class", "")).upper()
        source_blob = norm_text(record.get("provider"), record.get("domain"), record.get("url"), record.get("source_name"))


        if source_class in PROHIBITED_SOURCE_CLASSES or source_class.startswith("PROHIBITED_"):
            findings.append(Finding(
                "PF-1-SOURCE-CLASS", "BLOCK",
                f"Prohibited source class: {source_class}", f"{path}.source_class",
            ))
        if any(token in source_blob for token in PROHIBITED_SOURCE_TOKENS):
            findings.append(Finding(
                "PF-1-SOURCE-TOKEN", "BLOCK",
                "Betting/fantasy/tipster-derived source detected by provider/domain metadata.", path,
            ))
        if source_class == "DISCOVERY_ONLY":
            findings.append(Finding(
                "PF-1-DISCOVERY-ONLY", "BLOCK",
                "DISCOVERY_ONLY sources may locate an upstream source but may not support a predictive input.", path,
            ))
        elif source_class not in VALID_SOURCE_CLASSES and not source_class.startswith("PROHIBITED_"):
            findings.append(Finding(
                "PF-1-UNADMITTED-CLASS", "BLOCK",
                f"Unadmitted predictive source class: {source_class!r}. Classify/admit the source before use.",
                f"{path}.source_class",
            ))
        if record.get("critical") is True and source_class == "HISTORICAL_STRUCTURED_CANDIDATE":
            findings.append(Finding(
                "PF-1-HISTORICAL-CANDIDATE-CRITICAL", "BLOCK",
                "A historical structured candidate cannot establish a live critical state field.", path,
            ))
        if source_class == "UNKNOWN_LINEAGE" or not record.get("upstream_lineage_id"):
            findings.append(Finding(
                "PF-5-LINEAGE", "BLOCK",
                "Predictive evidence requires a known upstream lineage.", f"{path}.upstream_lineage_id",
            ))


        known = parse_time(record.get("first_known_at"), f"{path}.first_known_at", findings)
        retrieved = parse_time(record.get("retrieved_at"), f"{path}.retrieved_at", findings)
        if known and cutoff and known > cutoff:
            findings.append(Finding(
                "PF-3-POST-CUTOFF", "BLOCK",
                "Evidence was first known after the forecast cutoff.", f"{path}.first_known_at",
            ))
        if retrieved and frozen and retrieved > frozen:
            findings.append(Finding(
                "PF-3-POST-FREEZE", "BLOCK",
                "Evidence was retrieved after the independent distribution freeze.", f"{path}.retrieved_at",
            ))


        if record.get("critical") is True:
            freshness = str(record.get("freshness_status", "")).upper()
            if freshness not in FRESH_CRITICAL_STATES:
                findings.append(Finding(
                    "PF-4-STALE-CRITICAL", "BLOCK",
                    f"Critical dynamic input is not current: freshness_status={freshness!r}",
                    f"{path}.freshness_status",
                ))
            field = str(record.get("field_name") or "<missing>")
            critical_by_field.setdefault(field, []).append(record)


    qualifying_records = [
        r for r in evidence
        if isinstance(r, dict)
        and str(r.get("source_class", "")).upper() in VALID_SOURCE_CLASSES
        and r.get("upstream_lineage_id")
    ]
    qualifying_lineages = {str(r.get("upstream_lineage_id")) for r in qualifying_records}
    if len(qualifying_lineages) < 3:
        findings.append(Finding(
            "PF-SOURCE-COUNT-3", "BLOCK",
            "At least three distinct reliable upstream source lineages are required for every event.",
            "evidence",
        ))


    has_field_owner = any(
        r.get("field_owner") is True
        and str(r.get("source_class", "")).upper() == "VALID_PRIMARY_FIELD_OWNER"
        for r in qualifying_records
    )
    if not has_field_owner:
        findings.append(Finding(
            "PF-SOURCE-MIX-FIELD-OWNER", "BLOCK",
            "At least one qualifying field-owner exact-event source is required for normal verified issuance.",
            "evidence",
        ))


    has_independent_secondary = any(
        str(r.get("source_class", "")).upper() == "VALID_SECONDARY_INDEPENDENT"
        for r in qualifying_records
    )
    if not has_independent_secondary:
        findings.append(Finding(
            "PF-SOURCE-MIX-INDEPENDENT", "BLOCK",
            "At least one independent high-quality secondary lineage is required for normal verified issuance.",
            "evidence",
        ))


    for field, records in critical_by_field.items():
        if any(r.get("field_owner") is True and str(r.get("source_class", "")).upper() in VALID_SOURCE_CLASSES for r in records):
            continue
        lineages = {
            str(r.get("upstream_lineage_id"))
            for r in records
            if r.get("upstream_lineage_id") and str(r.get("source_class", "")).upper() in VALID_SOURCE_CLASSES
        }
        if len(lineages) < 2:
            findings.append(Finding(
                "PF-6-SOURCE-DIVERSITY", "BLOCK",
                f"Critical field {field!r} has no field-owner source and fewer than two independent valid upstream lineages.",
                f"evidence[field_name={field}]",
            ))


    if sport == "cricket":
        cc = manifest.get("cricket_conditions")
        if not isinstance(cc, dict):
            findings.append(Finding(
                "PF-CR-CONDITIONS", "BLOCK",
                "cricket_conditions object is required for cricket forecasts under CR-2026.09.21-3 (preserving the CR-2026.09.21-1 cricket source-state gate).",
                "cricket_conditions",
            ))
        else:
            toss_statuses = {"VERIFIED", "NOT_VERIFIED_AFTER_SEARCH", "NOT_YET_PUBLISHED", "CONFLICTING"}
            strip_statuses = {"OBSERVED", "NOT_FOUND_AFTER_SEARCH", "CONFLICTING", "STALE_ONLY"}
            venue_states = {"COMPUTED", "INSUFFICIENT_VENUE_HISTORY"}
            freeze_states = {"PRE_TOSS", "POST_TOSS"}


            toss_status = str(cc.get("toss_status", "")).upper()
            strip_status = str(cc.get("strip_status", "")).upper()
            venue_state = str(cc.get("venue_history_status", "")).upper()
            freeze_state = str(cc.get("pre_or_post_toss", "")).upper()


            if toss_status not in toss_statuses:
                findings.append(Finding("PF-CR-TOSS-STATUS", "BLOCK",
                    f"toss_status must be one of {sorted(toss_statuses)}.",
                    "cricket_conditions.toss_status"))
            if strip_status not in strip_statuses:
                findings.append(Finding("PF-CR-STRIP-STATUS", "BLOCK",
                    f"strip_status must be one of {sorted(strip_statuses)}.",
                    "cricket_conditions.strip_status"))
            if venue_state not in venue_states:
                findings.append(Finding("PF-CR-VENUE-HISTORY", "BLOCK",
                    f"venue_history_status must be one of {sorted(venue_states)}.",
                    "cricket_conditions.venue_history_status"))
            if freeze_state not in freeze_states:
                findings.append(Finding("PF-CR-TOSS-WINDOW", "BLOCK",
                    f"pre_or_post_toss must be one of {sorted(freeze_states)}.",
                    "cricket_conditions.pre_or_post_toss"))
            if cc.get("toss_search_complete") is not True:
                findings.append(Finding("PF-CR-TOSS-SEARCH", "BLOCK",
                    "toss_search_complete must be true after the required toss search attempt.",
                    "cricket_conditions.toss_search_complete"))
            if cc.get("strip_search_complete") is not True:
                findings.append(Finding("PF-CR-STRIP-SEARCH", "BLOCK",
                    "strip_search_complete must be true after the required strip search attempt.",
                    "cricket_conditions.strip_search_complete"))
            if cc.get("automated_pitch_metadata_used_as_observation") is not False:
                findings.append(Finding("PF-CR-AUTO-PITCH", "BLOCK",
                    "Automated pitch metadata cannot be relabelled as an observed current strip.",
                    "cricket_conditions.automated_pitch_metadata_used_as_observation"))
            if cc.get("duplicate_pitch_lineages_counted_independently") is not False:
                findings.append(Finding("PF-CR-LINEAGE-FINGERPRINT", "BLOCK",
                    "Duplicate/shared pitch-feed lineages cannot be counted as independent sources.",
                    "cricket_conditions.duplicate_pitch_lineages_counted_independently"))
            if cc.get("toss_decision_used_as_strip_report") is not False:
                findings.append(Finding("PF-CR-TOSS-AS-PITCH", "BLOCK",
                    "The toss decision is circumstantial context only and cannot be used as the strip report.",
                    "cricket_conditions.toss_decision_used_as_strip_report"))
            refreshed = parse_time(cc.get("final_conditions_refresh_at"),
                                   "cricket_conditions.final_conditions_refresh_at", findings)
            if refreshed and frozen and refreshed > frozen:
                findings.append(Finding("PF-CR-POST-FREEZE-REFRESH", "BLOCK",
                    "final_conditions_refresh_at cannot be after distribution_frozen_at.",
                    "cricket_conditions.final_conditions_refresh_at"))


    return findings




def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="Path to forecast manifest JSON")
    parser.add_argument("--json", action="store_true", dest="json_output", help="Emit machine-readable result")
    args = parser.parse_args(argv)


    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    except Exception as exc:
        if args.json_output:
            print(json.dumps({"ok": False, "malformed": True, "error": str(exc)}, indent=2))
        else:
            print(f"MALFORMED: {exc}", file=sys.stderr)
        return 2


    if not isinstance(manifest, dict):
        print("MALFORMED: manifest root must be a JSON object", file=sys.stderr)
        return 2


    findings = validate(manifest)
    blocking = [f for f in findings if f.level == "BLOCK"]
    result = {
        "ok": not blocking,
        "method_version": METHOD_VERSION,
        "control_revision": CONTROL_REVISION,
        "blocking_count": len(blocking),
        "findings": [asdict(f) for f in findings],
    }


    if args.json_output:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("PASS" if result["ok"] else "FAIL")
        for f in findings:
            where = f" [{f.path}]" if f.path else ""
            print(f"{f.level} {f.code}{where}: {f.message}")


    return 0 if result["ok"] else 1




if __name__ == "__main__":
    raise SystemExit(main())