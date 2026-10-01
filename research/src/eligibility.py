"""Evidence-derived admission. Metadata flags never confer eligibility.

Issue admission uses cached pregame state and scheduled start. Settlement
admission additionally needs a verified actual-start field; a schedule time or
the time of the first reported play is not substituted for actual start.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
from urllib.parse import urlparse

from .emit_card import price, states
from .load import ROOT
from .sports.base import Contract

SCHEMA_VERSION = "forecast-evidence-1"
REGISTRY = ROOT / "admission_registry.json"


def canonical_bytes(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def digest(value) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def aware_time(value, name="timestamp") -> datetime:
    if not isinstance(value, str):
        raise ValueError(f"{name} must be an ISO timestamp with a UTC offset")
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None or result.utcoffset() is None:
        raise ValueError(f"{name} must be timezone aware")
    return result.astimezone(timezone.utc)


def checked_ref(ref: dict, base: Path) -> Path:
    if not isinstance(ref, dict) or not ref.get("path") or not ref.get("sha256"):
        raise ValueError("artifact needs path and SHA-256")
    base = Path(base).resolve()
    path = Path(ref["path"])
    path = (path if path.is_absolute() else base / path).resolve()
    if not path.is_relative_to(base):
        raise ValueError("artifact path escapes evidence workspace")
    expected = ref["sha256"]
    if not isinstance(expected, str) or len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
        raise ValueError("invalid artifact SHA-256")
    if file_sha(path) != expected:
        raise ValueError(f"artifact hash mismatch: {path.name}")
    return path


def checked_json(ref: dict, base: Path) -> dict:
    value = json.loads(checked_ref(ref, base).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("artifact must be a JSON object")
    return value


def integer(value, name="score") -> int:
    if isinstance(value, bool):
        raise ValueError(f"invalid {name}")
    number = float(value)
    if not math.isfinite(number) or number < 0 or not number.is_integer():
        raise ValueError(f"invalid {name}")
    return int(number)


def pointer(obj, pointer_text: str):
    if not isinstance(pointer_text, str) or not pointer_text.startswith("/"):
        raise ValueError("reviewed JSON pointer required")
    for key in pointer_text[1:].split("/"):
        key = key.replace("~1", "/").replace("~0", "~")
        obj = obj[int(key)] if isinstance(obj, list) else obj[key]
    return obj


def _parser_audit(source: dict, base: Path) -> dict:
    audit = checked_json(source.get("parser_audit", {}), base)
    if audit.get("status") != "APPROVED" or not audit.get("reviewed_by") or not audit.get("basis"):
        raise ValueError("source parser mapping has no audited approval")
    if audit.get("field_map") != source.get("field_map"):
        raise ValueError("source parser differs from audited field mapping")
    return audit


def _parse_source(obj: dict, source: dict, event_id: str, base: Path) -> dict:
    """Parse actual publisher bodies, with no row-metadata fallback."""
    parser = source.get("parser", source.get("parser_id"))
    if parser == "NBL_SCHEDULE_V1":
        matches = obj.get("matches", [])
        if obj.get("total") != len(matches):
            raise ValueError("NBL source pagination or coverage changed")
        selected = [m for m in matches if str(m.get("id")) == event_id]
        if len(selected) != 1:
            raise ValueError("NBL exact event absent or duplicated")
        m = selected[0]
        if m.get("season_type") != "regular":
            raise ValueError("NBL model admits regular season only")
        state = {"upcoming": "PREGAME", "complete": "FINAL"}.get(m.get("phase"), "IN_PROGRESS")
        result = dict(event_id=str(m["id"]), home=m["home"]["team_code"], away=m["away"]["team_code"],
                      scheduled_start_utc=datetime.fromtimestamp(m["starts_at_ms"] / 1000, timezone.utc).isoformat(),
                      state=state, endpoint="INCL_OT")
        if state == "FINAL":
            result.update(score_home=integer(m["home_score"]), score_away=integer(m["away_score"]))
    elif parser == "ESPN_SUMMARY_V1":
        h = obj.get("header", {})
        matches = h.get("competitions", [])
        selected = [m for m in matches if str(m.get("id", h.get("id", ""))) == event_id]
        if len(selected) != 1:
            raise ValueError("ESPN exact event absent or duplicated")
        m = selected[0]
        competitors = {c["homeAway"]: c for c in m["competitors"]}
        if set(competitors) != {"home", "away"}:
            raise ValueError("ESPN event teams incomplete")
        status = m.get("status", {}).get("type", {})
        name = status.get("name")
        state = "FINAL" if status.get("completed") and name in {"STATUS_FINAL", "STATUS_FINAL_OT", "STATUS_FINAL_SO"} else "PREGAME" if name == "STATUS_SCHEDULED" and not status.get("completed") else "IN_PROGRESS"
        result = dict(event_id=event_id, home=competitors["home"]["team"]["displayName"],
                      away=competitors["away"]["team"]["displayName"], scheduled_start_utc=m.get("date", h.get("date")),
                      state=state, endpoint="FINAL_SCORE")
        if state == "FINAL":
            result.update(score_home=integer(competitors["home"]["score"]), score_away=integer(competitors["away"]["score"]))
    elif parser == "MLB_STATSAPI_V1":
        g = obj.get("gameData", {})
        if str(g.get("game", {}).get("pk")) != event_id:
            raise ValueError("MLB exact event mismatch")
        status = g.get("status", {})
        state = "FINAL" if status.get("abstractGameState") == "Final" and status.get("detailedState") in {"Final", "Game Over"} else "PREGAME" if status.get("abstractGameState") == "Preview" and status.get("detailedState") in {"Scheduled", "Pre-Game", "Warmup"} else "IN_PROGRESS"
        result = dict(event_id=event_id, home=g["teams"]["home"]["name"], away=g["teams"]["away"]["name"],
                      scheduled_start_utc=g["datetime"]["dateTime"], state=state, endpoint="INCL_EXTRAS")
        if state == "FINAL":
            scores = obj["liveData"]["linescore"]["teams"]
            result.update(score_home=integer(scores["home"]["runs"]), score_away=integer(scores["away"]["runs"]))
    elif parser == "REVIEWED_JSON_POINTER_V1":
        audit = _parser_audit(source, base)
        result = {field: pointer(obj, at) for field, at in source["field_map"].items()}
        required = {"event_id", "home", "away", "scheduled_start_utc", "state", "endpoint"}
        if not required <= result.keys():
            raise ValueError("reviewed source mapping misses event fields")
        if "actual_start_utc" in result and audit.get("actual_start_semantics") != "ACTUAL_START":
            raise ValueError("reviewed source has no actual-start semantics")
        result["event_id"] = str(result["event_id"])
        if result["state"] == "FINAL":
            result["score_home"] = integer(result["score_home"])
            result["score_away"] = integer(result["score_away"])
    else:
        raise ValueError(f"unsupported or unaudited source parser: {parser}")
    if parser != "REVIEWED_JSON_POINTER_V1" and source.get("field_map", {}).get("actual_start_utc"):
        audit = _parser_audit(source, base)
        if audit.get("actual_start_semantics") != "ACTUAL_START":
            raise ValueError("native source mapping cannot certify actual start")
        result["actual_start_utc"] = pointer(obj, source["field_map"]["actual_start_utc"])
    aliases = source.get("team_aliases", {})
    result["home"] = aliases.get(str(result["home"]), str(result["home"]))
    result["away"] = aliases.get(str(result["away"]), str(result["away"]))
    return result


def _receipt(receipt: dict, sources: dict, bundle: dict, base: Path, now: datetime) -> dict:
    source_id = receipt.get("source_id")
    entries = sources.get("sources", {})
    if isinstance(entries, list):
        entries = {e["source_id"]: e for e in entries}
    if source_id not in entries:
        raise ValueError("receipt source is not registered")
    source = entries[source_id]
    if bundle["league"] not in source.get("leagues", []):
        raise ValueError("source is not registered for this competition")
    url = receipt.get("source_url", "")
    parsed = urlparse(url)
    host = source.get("publisher_hostname", source.get("hostname"))
    if parsed.scheme != "https" or parsed.hostname != host:
        raise ValueError("receipt publisher does not match registered source")
    prefixes = source.get("allowed_url_prefixes", [])
    if not prefixes or not any(url.startswith(prefix) and urlparse(prefix).hostname == host for prefix in prefixes):
        raise ValueError("receipt URL is outside registered endpoint scope")
    lineage = source.get("upstream_lineage_id")
    if not lineage or receipt.get("upstream_lineage_id") != lineage:
        raise ValueError("receipt upstream lineage mismatch")
    if source.get("independence_status") != "VERIFIED":
        raise ValueError("upstream independence is unknown or unverified")
    audit = checked_json(source.get("lineage_audit", {}), base)
    if (audit.get("independence_status") != "VERIFIED" or audit.get("source_id") != source_id
            or audit.get("upstream_lineage_id") != lineage or not audit.get("basis") or not audit.get("reviewed_by")):
        raise ValueError("upstream lineage has no auditable mapping")
    if aware_time(audit.get("reviewed_utc"), "lineage review time") > now:
        raise ValueError("lineage review is in the future")
    if not audit.get("evidence_refs"):
        raise ValueError("lineage audit lacks supporting source artifacts")
    for ref in audit["evidence_refs"]:
        checked_ref(ref, base)
    retrieved = aware_time(receipt.get("retrieved_utc"), "source retrieval time")
    if retrieved > now:
        raise ValueError("source retrieval is in the future")
    raw_ref = {"path": receipt.get("body_path"), "sha256": receipt.get("response_sha256")}
    obj = checked_json(raw_ref, base)
    event_audit = checked_json(receipt.get("event_lineage_audit", {}), base)
    if (event_audit.get("event_id") != bundle["event_id"] or event_audit.get("source_id") != source_id
            or event_audit.get("upstream_lineage_id") != lineage or event_audit.get("response_sha256") != receipt["response_sha256"]
            or event_audit.get("independence_status") != "VERIFIED" or not event_audit.get("basis") or not event_audit.get("reviewed_by")):
        raise ValueError("event-specific raw response independence audit is missing or mismatched")
    reviewed = aware_time(event_audit.get("reviewed_utc"), "event lineage review time")
    if not retrieved <= reviewed <= now:
        raise ValueError("event lineage audit time is impossible")
    parsed_event = _parse_source(obj, source, str(bundle["event_id"]), base)
    for field in ("event_id", "home", "away", "endpoint"):
        if parsed_event.get(field) != str(bundle[field]):
            raise ValueError(f"raw source exact-event {field} mismatch")
    if parsed_event.get("league",bundle["league"])!=bundle["league"]:
        raise ValueError("raw source competition mismatch")
    if bundle["endpoint"] not in source.get("endpoints", []):
        raise ValueError("source is not approved for settlement endpoint")
    return dict(**parsed_event, source_id=source_id, upstream_lineage_id=lineage,
                official=source.get("official") is True, retrieved_utc=retrieved.isoformat(),
                lineage_reviewed_utc=reviewed.isoformat(), response_sha256=receipt["response_sha256"])


def _baseline_registration(bundle: dict, registry: dict, admission: dict, base: Path, cutoff: datetime) -> dict:
    """Bind the comparator definition and code, rather than trusting a probability label."""
    version = bundle.get("baseline_version")
    if not isinstance(version, str) or not version.strip() or version != admission.get("baseline_version"):
        raise ValueError("forecast baseline version differs from its model admission registration")
    matches = [entry for entry in registry.get("baseline_definitions", [])
               if entry.get("baseline_version") == version
               and all(entry.get(k) == bundle.get(k) for k in ("lane", "league", "endpoint"))]
    if len(matches) != 1:
        raise ValueError("baseline has no unique exact-scope registration")
    entry = matches[0]
    families = {c["market"] for c in bundle["contracts"]}
    if entry.get("status") != "APPROVED" or not families <= set(entry.get("families", [])):
        raise ValueError("baseline definition is not approved for every contract family")
    approved = aware_time(entry.get("approved_utc"), "baseline definition approval")
    if approved >= cutoff:
        raise ValueError("baseline definition approval was unavailable at cutoff")
    if entry.get("expires_utc") and cutoff >= aware_time(entry["expires_utc"], "baseline expiry"):
        raise ValueError("baseline definition approval has expired")
    artifacts = entry.get("code_artifacts", [])
    if not artifacts or len({ref.get("path") for ref in artifacts}) != len(artifacts):
        raise ValueError("baseline code artifacts are missing or duplicated")
    for ref in artifacts:
        checked_ref(ref, base)
    definition = checked_json(entry.get("definition_ref", {}), base)
    if (definition.get("schema_version") != "baseline-definition-1" or definition.get("status") != "APPROVED"
            or any(definition.get(k) != entry.get(k) for k in ("baseline_version", "lane", "league", "endpoint", "families", "code_artifacts"))
            or aware_time(definition.get("approved_utc"), "pinned baseline approval") != approved
            or aware_time(definition.get("reviewed_utc"), "baseline review") > approved
            or not definition.get("reviewed_by") or not definition.get("basis")):
        raise ValueError("pinned baseline definition disagrees with its auditable registration")
    return entry


def _qualification(bundle: dict, registry: dict, base: Path, cutoff: datetime, shadow: bool) -> dict:
    matches = [entry for entry in registry.get("admissions", [])
               if all(entry.get(k) == bundle.get(k) for k in ("lane", "league", "model_version", "endpoint"))]
    if len(matches) != 1:
        raise ValueError("model/lane/endpoint has no unique admission registration")
    entry = matches[0]
    allowed = {"LIVE_QUALIFIED", "SHADOW_ONLY"} if shadow else {"LIVE_QUALIFIED"}
    if entry.get("status") not in allowed:
        raise ValueError("registered model/lane is not live qualified" if not shadow else "registered model/lane is not shadow qualified")
    families = {c["market"] for c in bundle["contracts"]}
    if not families <= set(entry.get("families", [])):
        raise ValueError("contract family has not been qualified")
    if bundle.get("adjustment_type", "NONE") != "NONE":
        methods = [m for m in entry.get("adjustment_methods", []) if m.get("method_version") == bundle.get("adjustment_method_version")]
        if len(methods) != 1 or methods[0].get("status") != "APPROVED":
            raise ValueError("adjustment method version has not been approved")
        if aware_time(methods[0].get("approved_utc"), "adjustment method approval") > cutoff:
            raise ValueError("adjustment method approval was unavailable at cutoff")
        checked_ref(methods[0].get("artifact_ref", {}), base)
    qualified = aware_time(entry.get("qualified_utc"), "qualification time")
    if qualified > cutoff:
        raise ValueError("qualification was not available before cutoff")
    if entry.get("expires_utc") and cutoff >= aware_time(entry["expires_utc"]):
        raise ValueError("lane qualification has expired")
    if not entry.get("model_artifacts"):
        raise ValueError("model code/artifact custody is missing")
    for ref in entry["model_artifacts"]:
        checked_ref(ref, base)
    baseline = _baseline_registration(bundle, registry, entry, base, cutoff)
    artifacts = entry.get("qualification_artifacts", [])
    if not artifacts:
        raise ValueError("qualification evidence is missing")
    for ref in artifacts:
        checked_ref(ref, base)
    if entry["status"] == "LIVE_QUALIFIED":
        reviews = [checked_json(ref, base) for ref in artifacts if ref.get("kind") == "live_qualification"]
        if len(reviews) != 1:
            raise ValueError("live qualification review is required")
        review = reviews[0]
        if (review.get("status") != "APPROVED" or any(review.get(k) != bundle.get(k) for k in ("lane", "league", "model_version", "endpoint"))
                or not families <= set(review.get("families", []))
                or review.get("baseline_version") != baseline["baseline_version"]
                or review.get("baseline_definition_ref") != baseline["definition_ref"]):
            raise ValueError("live qualification review scope mismatch")
        if aware_time(review.get("reviewed_utc"), "qualification review time") > qualified:
            raise ValueError("qualification predates its review")
        holdout = checked_json(review.get("holdout_ref", {}), base)
        shadow_report = checked_json(review.get("shadow_ref", {}), base)
        if (holdout.get("stage") != "ONE_SHOT_HOLDOUT" or holdout.get("lane_decision") != "M2_PASS"
                or any(holdout.get(k) != bundle.get(k) for k in ("lane", "league", "model_version", "endpoint"))
                or not families <= set(holdout.get("validated_families", []))
                or holdout.get("baseline_version") != baseline["baseline_version"]
                or holdout.get("baseline_definition_ref") != baseline["definition_ref"]):
            raise ValueError("qualified model lacks an untouched exact-model/family holdout")
        for family in families:
            gate = holdout.get("family_gates", {}).get(family, {})
            ci = gate.get("paired_logloss_ci95", [])
            if gate.get("lane_decision") != "M2_PASS" or len(ci) != 2 or not all(math.isfinite(float(x)) for x in ci) or not ci[0] <= ci[1] < 0:
                raise ValueError("contract family has not passed its own holdout gate")
        if review.get("model_artifacts") != entry["model_artifacts"]:
            raise ValueError("live qualification is not bound to unchanged registered model artifacts")
        shadow_n = integer(shadow_report.get("independent_events"), "shadow sample")
        first = aware_time(shadow_report.get("first_forecast_utc"), "first shadow time")
        last = aware_time(shadow_report.get("last_forecast_utc"), "last shadow time")
        manifest = checked_json(review.get("shadow_manifest_ref", {}), base)
        shadow_refs = manifest.get("receipts", [])
        if manifest.get("schema_version") != "shadow-manifest-1" or not shadow_refs:
            raise ValueError("shadow count needs a retained receipt manifest")
        shadow_ids, shadow_times = set(), []
        for ref in shadow_refs:
            row = checked_json(ref, base)
            identity = row.get("event_id")
            issued = aware_time(row.get("forecast_utc", row.get("issued_utc")), "shadow forecast time")
            start = aware_time(row.get("scheduled_start_utc", row.get("start_utc")), "shadow scheduled start")
            data_cutoff = aware_time(row.get("data_cutoff_utc"), "shadow input cutoff")
            if (not isinstance(identity, str) or not identity or identity in shadow_ids or row.get("shadow_only") is not True
                    or row.get("performance_eligible") is not False or not data_cutoff < issued < start
                    or any(row.get(k) != bundle.get(k) for k in ("lane", "league", "model_version", "endpoint"))
                    or row.get("model_artifacts") != entry["model_artifacts"]
                    or row.get("baseline_version") != baseline["baseline_version"]
                    or row.get("baseline_definition_ref") != baseline["definition_ref"]
                    or row.get("baseline_code_artifacts") != baseline["code_artifacts"]):
                raise ValueError("shadow receipt identity/model/timing/code custody failed")
            shadow_ids.add(identity)
            shadow_times.append(issued)
        if len(shadow_ids) != shadow_n or min(shadow_times) != first or max(shadow_times) != last:
            raise ValueError("reported shadow count/duration differs from retained independent receipts")
        minimum_events=max(50,integer(review.get("minimum_shadow_events",50),"minimum shadow events"))
        minimum_days=max(28,integer(review.get("minimum_shadow_days",28),"minimum shadow days"))
        if not first <= last <= qualified or shadow_n < minimum_events or (last-first).total_seconds() < minimum_days*86400:
            raise ValueError("shadow qualification duration/sample has not passed")
        for gate in ("issuer_ref", "terminal_adapter_ref"):
            checked_ref(review.get(gate, {}), base)
        if not review.get("reviewed_by") or not review.get("basis"):
            raise ValueError("live qualification review is unaudited")
    return {**entry, "validated_baseline": baseline}


def _distribution_join(bundle: dict, base: Path, cutoff: datetime, baseline: dict) -> list[dict]:
    artifacts = bundle.get("input_artifacts", [])
    if not artifacts:
        raise ValueError("forecast input custody is missing")
    input_refs = []
    for ref in artifacts:
        checked_ref(ref, base)
        if aware_time(ref.get("available_utc"), "input availability time") > cutoff:
            raise ValueError("forecast input was unavailable at cutoff")
        input_refs.append({"path": ref["path"], "sha256": ref["sha256"], "available_utc": ref["available_utc"]})
    checksum = digest(sorted(input_refs, key=lambda r: r["path"]))
    if bundle.get("input_checksum") != checksum:
        raise ValueError("forecast input checksum mismatch")
    distributions = {}
    for label in ("model", "card", "baseline"):
        spec = checked_json(bundle.get("distributions", {}).get(label, {}), base)
        if spec.get("schema_version") != "score-distribution-1":
            raise ValueError("distribution lacks versioned schema")
        for key in ("event_id", "endpoint", "input_checksum"):
            if spec.get(key) != bundle.get(key):
                raise ValueError(f"{label} distribution {key} mismatch")
        if aware_time(spec.get("data_cutoff_utc"), "distribution cutoff") != cutoff:
            raise ValueError("distribution cutoff mismatch")
        if label != "baseline" and spec.get("model_version") != bundle["model_version"]:
            raise ValueError("distribution model version mismatch")
        if label == "baseline" and (spec.get("baseline_version") != baseline["baseline_version"]
                or spec.get("baseline_definition_ref") != baseline["definition_ref"]
                or spec.get("baseline_code_artifacts") != baseline["code_artifacts"]):
            raise ValueError("baseline distribution version/definition/code artifacts mismatch")
        distributions[label] = states(spec.get("states", []))
    support = [(int(h), int(a)) for h, a in zip(*distributions["model"][:2])]
    for label in ("card", "baseline"):
        if support != [(int(h), int(a)) for h, a in zip(*distributions[label][:2])]:
            raise ValueError("joined distributions have different score support")
    contracts = bundle.get("contracts", [])
    if not contracts:
        raise ValueError("forecast contracts are absent")
    output, keys = [], set()
    for row in contracts:
        c = Contract(str(bundle["event_id"]), row["market"], row.get("side", row.get("selection")),
                     row.get("line"), row.get("endpoint", bundle["endpoint"]), row.get("period", "FULL_GAME"))
        if c.endpoint != bundle["endpoint"] or c.period != "FULL_GAME":
            raise ValueError("contract endpoint/period disagrees with frozen distribution")
        if c.market in {"SPREAD", "TOTAL"} and (not isinstance(c.line, (int, float)) or not math.isfinite(c.line)):
            raise ValueError("invalid contract line")
        key = (c.market, c.side, c.line, c.endpoint, c.period)
        if key in keys:
            raise ValueError("duplicate frozen contract")
        keys.add(key)
        record = {"market": c.market, "selection": c.side, "line": c.line, "endpoint": c.endpoint, "period": c.period}
        for label in distributions:
            priced = price(distributions[label], c)
            p = priced["conditional_win"]
            if not 0 < p < 1:
                raise ValueError("degenerate joined probability")
            for field, value in ((f"p_{label}", p), (f"push_{label}", priced["p"])):
                if field in row and (not math.isfinite(float(row[field])) or abs(float(row[field])-value) > 1e-9):
                    raise ValueError(f"row {field} differs from frozen distribution")
                record[field] = value
        output.append(record)
    if bundle.get("adjustment_type", "NONE") == "NONE":
        if bundle["distributions"]["model"]["sha256"] != bundle["distributions"]["card"]["sha256"]:
            # Event wrappers may differ, but the probability mass must not.
            if not (distributions["model"][2] == distributions["card"][2]).all():
                raise ValueError("NONE adjustment changed the frozen distribution")
    elif not bundle.get("adjustment_reason") or not bundle.get("adjustment_evidence"):
        raise ValueError("adjustment lacks an explanation and source artifacts")
    for ref in bundle.get("adjustment_evidence", []):
        checked_ref(ref, base)
        if aware_time(ref.get("available_utc"), "adjustment evidence availability") > cutoff:
            raise ValueError("adjustment evidence was unavailable at cutoff")
    return output


@dataclass(frozen=True)
class EligibilityResult:
    eligible: bool
    reasons: tuple[str, ...]
    verified: dict

    def require(self) -> dict:
        if not self.eligible:
            raise ValueError("evidence admission rejected: " + "; ".join(self.reasons))
        return self.verified


def validate_evidence(bundle: dict | Path, registry_path: Path = REGISTRY, *,
                      sources_registry_path: Path | None = None, evidence_root: Path | None = None,
                      now: datetime | None = None, require_terminal: bool = False,
                      purpose: str = "ISSUE") -> EligibilityResult:
    """Read and verify artifacts; never issue a card or mutate evidence."""
    now = now or datetime.now(timezone.utc)
    verified = {}
    try:
        if now.tzinfo is None or now.utcoffset() is None:
            raise ValueError("validation clock must be timezone aware")
        if purpose not in {"ISSUE", "SHADOW"}:
            raise ValueError("unknown evidence admission purpose")
        registry_path = Path(registry_path).resolve()
        base = Path(evidence_root).resolve() if evidence_root else (registry_path.parent.parent if registry_path.parent.name == "research" else registry_path.parent)
        source_path = Path(sources_registry_path).resolve() if sources_registry_path else registry_path.with_name("sources_registry.json")
        if isinstance(bundle, (str, Path)):
            bundle = json.loads(Path(bundle).read_text(encoding="utf-8"))
        if not isinstance(bundle, dict) or bundle.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("versioned evidence bundle is required; eligibility booleans are insufficient")
        for field in ("event_id", "lane", "league", "season", "home", "away", "endpoint", "model_version"):
            if not isinstance(bundle.get(field), str) or not bundle[field].strip():
                raise ValueError(f"missing exact identity field: {field}")
        if bundle["home"] == bundle["away"]:
            raise ValueError("event has identical opponents")
        issue = aware_time(bundle.get("issued_utc"), "issue time")
        cutoff = aware_time(bundle.get("data_cutoff_utc"), "input cutoff")
        scheduled = aware_time(bundle.get("scheduled_start_utc"), "scheduled start")
        if not cutoff < issue < scheduled or issue > now:
            raise ValueError("strict cutoff < issue < verified scheduled start is required")
        if file_sha(registry_path) != bundle.get("registry_sha256") or file_sha(source_path) != bundle.get("sources_registry_sha256"):
            raise ValueError("admission/source registry custody mismatch")
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        sources = json.loads(source_path.read_text(encoding="utf-8"))
        qualified = _qualification(bundle, registry, base, cutoff, purpose == "SHADOW")
        rows = _distribution_join(bundle, base, cutoff, qualified["validated_baseline"])
        pregame = [_receipt(r, sources, bundle, base, now) for r in bundle.get("pregame_receipts", [])]
        max_age = min(300, int(qualified.get("max_state_age_seconds", 300)))
        if max_age <= 0 or len({r["upstream_lineage_id"] for r in pregame}) < 3 or not any(r["official"] for r in pregame):
            raise ValueError("three verified independent pregame lineages including an official source are required")
        for r in pregame:
            retrieved = aware_time(r["retrieved_utc"])
            if (r["state"] != "PREGAME" or aware_time(r["scheduled_start_utc"]) != scheduled
                    or not retrieved <= cutoff or aware_time(r["lineage_reviewed_utc"]) > cutoff
                    or (issue-retrieved).total_seconds() > max_age):
                raise ValueError("pregame state is stale, late, nonpregame or a changed start")
        verified = dict(event_id=bundle["event_id"], lane=bundle["lane"], league=bundle["league"],
                        season=bundle["season"], home=bundle["home"], away=bundle["away"], endpoint=bundle["endpoint"],
                        model_version=bundle["model_version"], baseline_version=bundle["baseline_version"],
                        baseline_definition_ref=qualified["validated_baseline"]["definition_ref"],
                        baseline_code_artifacts=qualified["validated_baseline"]["code_artifacts"], qualification_status=qualified["status"],
                        issued_utc=issue.isoformat(), data_cutoff_utc=cutoff.isoformat(),
                        scheduled_start_utc=scheduled.isoformat(), actual_start_utc=None,
                        adjustment_type=bundle.get("adjustment_type", "NONE"), rows=rows,
                        bundle_sha256=digest(bundle), registry_sha256=bundle["registry_sha256"],
                        sources_registry_sha256=bundle["sources_registry_sha256"],
                        identity_lineages=sorted({r["upstream_lineage_id"] for r in pregame}),
                        pregame_receipt_hashes=sorted(r["response_sha256"] for r in pregame))
        if require_terminal:
            terminal = [_receipt(r, sources, bundle, base, now) for r in bundle.get("terminal_receipts", [])]
            if len({r["upstream_lineage_id"] for r in terminal}) < 3 or not any(r["official"] for r in terminal):
                raise ValueError("three verified independent terminal lineages including an official source are required")
            if any(r["state"] != "FINAL" for r in terminal):
                raise ValueError("terminal evidence includes a nonfinal event")
            scores = {(r["score_home"], r["score_away"]) for r in terminal}
            if len(scores) != 1:
                raise ValueError("independent terminal scores disagree")
            start_receipts = terminal
            if bundle.get("actual_start_receipt"):
                start_receipts = terminal + [_receipt(bundle["actual_start_receipt"], sources, bundle, base, now)]
            starts = {aware_time(r["actual_start_utc"]) for r in start_receipts if r.get("actual_start_utc")}
            if len(starts) != 1:
                raise ValueError("verified actual start is absent or conflicting; scheduled start is not substituted")
            actual = starts.pop()
            if not cutoff < issue < actual or any(aware_time(r["retrieved_utc"]) < actual for r in terminal):
                raise ValueError("strict cutoff < issue < verified actual start and post-start settlement are required")
            if bundle.get("actual_start_utc") and aware_time(bundle["actual_start_utc"]) != actual:
                raise ValueError("row actual start conflicts with raw source")
            h, a = scores.pop()
            if bundle["league"] in {"NBL","NBA","WNBA"} and bundle["endpoint"] in {"INCL_OT","INCL_OVERTIME","FINAL_SCORE"} and h==a:
                raise ValueError("completed full-game basketball score cannot be tied")
            verified.update(actual_start_utc=actual.isoformat(), score_home=h, score_away=a,
                            terminal_lineages=sorted({r["upstream_lineage_id"] for r in terminal}),
                            terminal_receipt_hashes=sorted(r["response_sha256"] for r in terminal),
                            settled_utc=max(aware_time(r["retrieved_utc"]) for r in terminal).isoformat())
        return EligibilityResult(True, (), verified)
    except (ValueError, KeyError, TypeError, OSError, OverflowError, IndexError, AttributeError) as exc:
        return EligibilityResult(False, (str(exc),), verified)


if __name__ == "__main__":
    import argparse
    from dataclasses import asdict
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle",type=Path)
    parser.add_argument("--registry",type=Path,default=REGISTRY)
    parser.add_argument("--sources-registry",type=Path)
    parser.add_argument("--evidence-root",type=Path)
    parser.add_argument("--terminal",action="store_true")
    parser.add_argument("--purpose",choices=("ISSUE","SHADOW"),default="ISSUE")
    args=parser.parse_args()
    result=validate_evidence(args.bundle,args.registry,sources_registry_path=args.sources_registry,
        evidence_root=args.evidence_root,require_terminal=args.terminal,purpose=args.purpose)
    print(json.dumps(asdict(result),indent=2))
    raise SystemExit(0 if result.eligible else 1)
