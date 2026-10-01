"""Custodied prospective pilot with chronological membership and terminal stops.

Legacy CSV flags are not an admission authority. Only canonically frozen
issues joined to verified source-backed settlement revisions can be scored.
"""
from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path

import numpy as np
import pandas as pd

from .eligibility import (REGISTRY, _qualification, aware_time, canonical_bytes, checked_json,
                          checked_ref, digest, file_sha, validate_evidence)
from .ledger import (_append_locked, committed_issues, event_key, forecast_core,
                     locked, read_records, validate_universe)

EVENT_COLUMNS = ["lane", "league", "season", "event_id", "week", "issued_utc", "actual_start_utc",
                 "adjusted", "model_logloss", "card_logloss", "baseline_logloss", "model_brier", "card_brier", "baseline_brier"]


def _utc_now():
    return datetime.now(timezone.utc)


def _probabilities(rows: pd.DataFrame, prefix: str):
    by = {(r.market, r.selection, str(r.line)): float(getattr(r, prefix)) for r in rows.itertuples()}
    expected = {("1X2", s, "") for s in ("HOME", "DRAW", "AWAY")} | {("TOTAL", s, "2.5") for s in ("OVER", "UNDER")} | {("BTTS", s, "") for s in ("YES", "NO")}
    if len(rows) != 7 or set(by) != expected:
        raise ValueError("incomplete or duplicate fixed EPL contract families")
    one = np.array([by[("1X2", s, "")] for s in ("HOME", "DRAW", "AWAY")])
    total, btts = by[("TOTAL", "OVER", "2.5")], by[("BTTS", "YES", "")]
    values = np.array(list(by.values()))
    if not np.isfinite(values).all() or (values <= 0).any() or (values >= 1).any():
        raise ValueError("invalid or nonfinite forecast probability")
    if abs(one.sum()-1) > 1e-9 or abs(total+by[("TOTAL", "UNDER", "2.5")]-1) > 1e-9 or abs(btts+by[("BTTS", "NO", "")]-1) > 1e-9:
        raise ValueError("incoherent fixed contract families")
    return one, total, btts


def _score(one, total, btts, home: int, away: int):
    actual = 0 if home > away else 1 if home == away else 2
    over, yes = float(home+away > 2), float(home > 0 and away > 0)
    logloss = (-np.log(one[actual])-(over*np.log(total)+(1-over)*np.log(1-total))-(yes*np.log(btts)+(1-yes)*np.log(1-btts)))/3
    brier = (np.sum((one-np.eye(3)[actual])**2)/2+(total-over)**2+(btts-yes)**2)/3
    return float(logloss), float(brier)


def score_events(path: Path, registry_path: Path = REGISTRY, *, sources_registry_path: Path | None = None,
                 evidence_root: Path | None = None, now: datetime | None = None) -> pd.DataFrame:
    """Return verified event scores and explicit exclusions/abstentions in attrs."""
    path = Path(path)
    if path.suffix.lower() == ".csv":
        raise ValueError("legacy CSV eligibility flags cannot admit a pilot; canonical evidence ledger is required")
    records = read_records(path)
    issues = committed_issues(records)
    registrations = {event_key(r["payload"]): r for r in records if r["record_type"] == "EVENT_REGISTERED"}
    abstentions = {event_key(r["payload"]): r["payload"] for r in records if r["record_type"] == "ABSTENTION"}
    exclusions, output, scored = [], [], set()
    for issue in issues:
        key = event_key(issue)
        try:
            if key not in registrations:
                raise ValueError("issued event is outside the registered universe")
            registered = registrations[key]["payload"]
            root = Path(evidence_root).resolve() if evidence_root else (Path(registry_path).resolve().parent.parent if Path(registry_path).parent.name == "research" else Path(registry_path).resolve().parent)
            universe = validate_universe(registered["universe_ref"], evidence_root=root)
            if registered["universe_sha256"] != registered["universe_ref"]["sha256"] or sum(event_key(e) == key for e in universe.get("events", [])) != 1:
                raise ValueError("universe membership hash or exact event changed")
            if aware_time(registrations[key]["recorded_utc"]) >= aware_time(issue["bundle"]["issued_utc"]):
                raise ValueError("universe registration did not precede issuance")
            if file_sha(Path(issue["frozen_bundle_path"])) != issue["frozen_bundle_file_sha256"]:
                raise ValueError("frozen issued artifact changed")
            from .issue import _projection
            projection = _projection(issue["core"], issue["card_id"], issue["transaction_id"])
            if Path(issue["part6_path"]).read_bytes().count(projection) != 1:
                raise ValueError("canonical issued core is absent or duplicated in Part 6")
            revisions = [r for r in records if r["record_type"] == "SETTLEMENT_REVISION" and event_key(r["payload"]) == key]
            if not revisions:
                raise ValueError("UNSETTLED")
            previous = "0"*64
            for number, revision in enumerate(revisions, 1):
                p = revision["payload"]
                if p.get("revision") != number or p.get("previous_revision_sha256") != previous or p.get("issue_record_sha256") != issue["issue_record_sha256"] or p.get("forecast_core_sha256") != issue["forecast_core_sha256"]:
                    raise ValueError("settlement revision custody chain changed")
                previous = revision["record_sha256"]
            bundle = revisions[-1]["payload"]["bundle"]
            if digest(forecast_core(bundle)) != issue["forecast_core_sha256"]:
                raise ValueError("settlement differs from the frozen issued core")
            verified = validate_evidence(bundle, registry_path, sources_registry_path=sources_registry_path,
                                         evidence_root=evidence_root, now=now, require_terminal=True).require()
            if verified["lane"] != "EPL":
                raise ValueError("pilot v2 scores EPL families only; other lanes need their own frozen scoring protocol")
            frame = pd.DataFrame(verified["rows"])
            frame["line"] = frame["line"].map(lambda x: "" if pd.isna(x) else str(float(x)))
            scores = {label: _score(*_probabilities(frame, f"p_{label}"), verified["score_home"], verified["score_away"])
                      for label in ("model", "card", "baseline")}
            start = aware_time(verified["actual_start_utc"])
            row = {**{f: verified[f] for f in ("lane", "league", "season", "event_id", "issued_utc", "actual_start_utc")},
                   "week": f"{start.isocalendar().year}-W{start.isocalendar().week:02}",
                   "adjusted": verified["adjustment_type"] != "NONE"}
            for label, (logloss, brier) in scores.items():
                row[f"{label}_logloss"], row[f"{label}_brier"] = logloss, brier
            output.append(row)
            scored.add(key)
        except (ValueError, KeyError, OSError, TypeError) as exc:
            exclusions.append({"identity": list(key), "reason": str(exc), "issue_record_sha256": issue["issue_record_sha256"]})
    issued_keys = {event_key(p) for p in issues}
    for key in registrations.keys()-issued_keys:
        abstention = abstentions.get(key)
        exclusions.append({"identity": list(key), "reason": "ABSTENTION" if abstention else "NO_FORECAST",
                           "detail": abstention["reason"] if abstention else "Registered fixture has no frozen forecast decision",
                           "timely": abstention.get("timely") if abstention else None})
    frame = pd.DataFrame(output, columns=EVENT_COLUMNS)
    if not frame.empty:
        frame = frame.sort_values(["issued_utc", "league", "season", "event_id"]).reset_index(drop=True)
    frame.attrs.update(exclusions=sorted(exclusions, key=lambda e: e["identity"]),
                       registered_events=len(registrations), issued_events=len(issues),
                       scored_events=len(scored), abstentions=len(abstentions),
                       issues=issues, ledger_head=records[-1]["record_sha256"] if records else "0"*64)
    return frame


def paired_bootstrap(events: pd.DataFrame, weights: dict[str, float], metric: str, seed: int,
                     reps: int = 10000, minimum_blocks: int = 4, a: str = "card", b: str = "model"):
    if metric not in {"logloss", "brier"} or reps < 1000:
        raise ValueError("fixed score and adequate bootstrap count required")
    rng, estimates = np.random.default_rng(seed), []
    for lane, weight in weights.items():
        subset = events.loc[events.lane == lane].copy()
        if subset.empty:
            raise ValueError(f"missing declared lane {lane}")
        delta = subset[f"{a}_{metric}"]-subset[f"{b}_{metric}"]
        if not np.isfinite(delta).all():
            raise ValueError("nonfinite event score")
        grouped = delta.groupby(subset.week).agg(["sum", "count"])
        if len(grouped) < minimum_blocks:
            raise ValueError("insufficient independent week blocks for declared inference")
        sums, counts = grouped["sum"].to_numpy(), grouped["count"].to_numpy()
        pick = rng.integers(0, len(sums), size=(reps, len(sums)))
        estimates.append((weight, float(sums.sum()/counts.sum()), sums[pick].sum(axis=1)/counts[pick].sum(axis=1)))
    mean = sum(w*m for w, m, _ in estimates)
    boot = sum(w*v for w, _, v in estimates)
    return dict(mean=float(mean), ci95=[float(np.quantile(boot, .025)), float(np.quantile(boot, .975))],
                events=len(events), minimum_week_blocks=minimum_blocks)


def _validate_lock(lock: dict, *, root: Path):
    if lock.get("schema_version") != "pilot-lock-2" or lock.get("status") != "FROZEN":
        raise ValueError("versioned immutable pilot lock is required")
    if lock.get("weights") != {"EPL": 1.0}:
        raise ValueError("pilot v2 is EPL-only with a fixed weight of one")
    if (set(lock.get("model_versions", {})) != {"EPL"} or not lock["model_versions"]["EPL"]
            or lock.get("endpoints") != {"EPL": "REGULATION"}
            or set(lock.get("league_seasons", {})) != {"EPL"}
            or lock["league_seasons"]["EPL"].get("league") != "EPL" or not lock["league_seasons"]["EPL"].get("season")):
        raise ValueError("exact model version, competition, season and endpoint must be frozen")
    target, interim = lock.get("target_adjusted_events"), lock.get("futility_look_events")
    if isinstance(target, bool) or not isinstance(target, int) or isinstance(interim, bool) or not isinstance(interim, int) or not 0 < interim < target:
        raise ValueError("fixed positive integer target and earlier single interim required")
    if not np.isfinite(lock.get("mwi_brier", np.nan)) or not 0 < lock["mwi_brier"] < 1:
        raise ValueError("worthwhile Brier improvement must be frozen")
    if not isinstance(lock.get("minimum_week_blocks"), int) or lock["minimum_week_blocks"] < 4:
        raise ValueError("at least four independent week blocks are required")
    if not isinstance(lock.get("seed"), int) or lock.get("bootstrap_reps") != 10000:
        raise ValueError("seed and 10000 bootstrap repetitions must be frozen")
    created = aware_time(lock.get("lock_created_utc"), "lock creation")
    first, last = aware_time(lock.get("cohort_issue_from_utc")), aware_time(lock.get("cohort_issue_to_utc"))
    if not created < first < last:
        raise ValueError("lock must precede the first eligible issue-time window")
    if lock.get("inclusion_rule") != "FIRST_CHRONOLOGICAL_ADJUSTED_ISSUES":
        raise ValueError("chronological inclusion rule must be declared")
    power = checked_json(lock.get("power_plan_ref", {}), root)
    if (power.get("target_adjusted_events") != target or power.get("futility_look_events") != interim
            or power.get("mwi_brier") != lock["mwi_brier"] or power.get("minimum_week_blocks") != lock["minimum_week_blocks"]
            or not power.get("method") or not power.get("basis_refs")):
        raise ValueError("pilot sample differs from its source-backed power/precision plan")
    for ref in power["basis_refs"]:
        checked_ref(ref, root)
    if not lock.get("universe_refs"):
        raise ValueError("pilot requires a declared frozen fixture universe")
    for ref in lock["universe_refs"]:
        universe = validate_universe(ref, evidence_root=root)
        if universe.get("schema_version") != "event-universe-1" or not universe.get("events"):
            raise ValueError("invalid frozen universe")
    return created, first, last


def freeze_lock(lock_path: Path, definition: dict, *, ledger_path: Path,
                registry_path: Path = REGISTRY, sources_registry_path: Path | None = None,
                evidence_root: Path | None = None, state_path: Path | None = None) -> dict:
    """Create once, pin custody before the cohort, and refuse all overwrites."""
    now, lock_path = _utc_now(), Path(lock_path)
    registry_path = Path(registry_path).resolve()
    source_path = Path(sources_registry_path).resolve() if sources_registry_path else registry_path.with_name("sources_registry.json")
    root = Path(evidence_root).resolve() if evidence_root else (registry_path.parent.parent if registry_path.parent.name == "research" else registry_path.parent)
    state_path = Path(state_path) if state_path else lock_path.with_name(lock_path.stem+".custody.jsonl")
    records = read_records(ledger_path)
    lock = {**definition, "schema_version": "pilot-lock-2", "status": "FROZEN", "lock_created_utc": now.isoformat(),
            "ledger_path": str(Path(ledger_path).resolve()), "ledger_initial_head": records[-1]["record_sha256"] if records else "0"*64,
            "registry_path": str(registry_path), "registry_sha256": file_sha(registry_path),
            "sources_registry_path": str(source_path), "sources_registry_sha256": file_sha(source_path),
            "evidence_root": str(root), "state_path": str(state_path.resolve())}
    _, first, last = _validate_lock(lock, root=root)
    admissions = json.loads(registry_path.read_text(encoding="utf-8")).get("admissions", [])
    if not any(e.get("lane") == "EPL" and e.get("model_version") == lock["model_versions"]["EPL"] and e.get("status") == "LIVE_QUALIFIED" and {"1X2", "TOTAL", "BTTS"} <= set(e.get("families", [])) for e in admissions):
        raise ValueError("no live-qualified EPL composite scope; a retrospective pass cannot start this pilot")
    _qualification(dict(lane="EPL",league="EPL",model_version=lock["model_versions"]["EPL"],endpoint="REGULATION",
                        contracts=[{"market":f} for f in ("1X2","TOTAL","BTTS")]),
                   {"admissions":admissions},root,now,False)
    if any(first <= aware_time(p["bundle"]["issued_utc"]) < last for p in committed_issues(records)):
        raise ValueError("pilot cohort already contains issued events; lock is retrospective")
    if lock_path.exists() or state_path.exists():
        raise FileExistsError("pilot lock/custody already exists; do not overwrite")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with locked(state_path):
        with lock_path.open("xb") as handle:
            handle.write(canonical_bytes(lock)+b"\n")
            handle.flush()
            os.fsync(handle.fileno())
        _append_locked(state_path, "PILOT_LOCK", {"cohort_version": lock["cohort_version"],
                       "lock_sha256": file_sha(lock_path), "lock_path": str(lock_path.resolve()),
                       "lock_created_utc": now.isoformat()}, recorded_utc=now.isoformat())
    return lock


def _membership(issues: list[dict]) -> list[dict]:
    return [{"identity": list(event_key(p)), "issued_utc": p["bundle"]["issued_utc"],
             "issue_record_sha256": p["issue_record_sha256"], "forecast_core_sha256": p["forecast_core_sha256"]}
            for p in issues]


def decision(path: Path, lock_path: Path) -> dict:
    lock_path = Path(lock_path)
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    root = Path(lock.get("evidence_root", lock_path.parent))
    created, first, last = _validate_lock(lock, root=root)
    if created > _utc_now() or Path(path).resolve() != Path(lock["ledger_path"]).resolve():
        raise ValueError("pilot clock or canonical ledger differs from its lock")
    for key in ("registry", "sources_registry"):
        if file_sha(Path(lock[key+"_path"])) != lock[key+"_sha256"]:
            raise ValueError("pilot registry changed since its immutable lock")
    state_path = Path(lock["state_path"])
    with locked(state_path):
        state = read_records(state_path)
        pinned = [r for r in state if r["record_type"] == "PILOT_LOCK"]
        if len(pinned) != 1 or pinned[0]["payload"]["lock_sha256"] != file_sha(lock_path) or pinned[0]["recorded_utc"] != lock["lock_created_utc"]:
            raise ValueError("pilot lock has no matching pre-cohort immutable custody")
        ledger = read_records(path)
        old_head = lock["ledger_initial_head"]
        if old_head != "0"*64 and old_head not in {r["record_sha256"] for r in ledger}:
            raise ValueError("pilot ledger prefix changed after lock")
        events = score_events(path, Path(lock["registry_path"]), sources_registry_path=Path(lock["sources_registry_path"]), evidence_root=root)
        declared = {ref["sha256"] for ref in lock["universe_refs"]}
        registered = {event_key(r["payload"]): r["payload"] for r in ledger if r["record_type"] == "EVENT_REGISTERED"}
        window_issues = [p for p in events.attrs["issues"] if p["lane"] in lock["weights"] and first <= aware_time(p["bundle"]["issued_utc"]) < last]
        def in_scope(p):
            b=p["bundle"]
            return (b["model_version"]==lock["model_versions"][b["lane"]] and b["endpoint"]==lock["endpoints"][b["lane"]]
                    and all(b[k]==lock["league_seasons"][b["lane"]][k] for k in ("league","season")))
        issues = [p for p in window_issues if in_scope(p)]
        if any(registered.get(event_key(p), {}).get("universe_sha256") not in declared for p in issues):
            raise ValueError("cohort issue is outside its preregistered universe")
        adjusted = [p for p in issues if p["bundle"].get("adjustment_type", "NONE") != "NONE"]
        target, interim = lock["target_adjusted_events"], lock["futility_look_events"]
        membership = _membership(adjusted[:target])
        scored_keys = {event_key(row) for row in events.to_dict("records")}
        summary = dict(cohort_version=lock["cohort_version"], registered_events=events.attrs["registered_events"],
                       issued_events=len(issues), scored_events=sum(event_key(p) in scored_keys for p in issues),
                       adjusted_enrolled_events=min(len(adjusted), target), target=target,
                       cohort_membership=membership, membership_sha256=digest(membership),
                       exclusions=events.attrs["exclusions"], abstentions=events.attrs["abstentions"],
                       all_events_logloss=None)
        summary["exclusions"] += [{"identity":list(event_key(p)),"reason":"OUTSIDE_PREREGISTERED_MODEL_COMPETITION_SEASON_ENDPOINT"} for p in window_issues if not in_scope(p)]
        all_keys={event_key(p) for p in issues}
        all_scores=events.loc[[event_key(row) in all_keys for row in events.to_dict("records")]]
        if not all_scores.empty and all_scores.week.nunique()>=lock["minimum_week_blocks"]:
            summary["all_events_logloss"]=paired_bootstrap(all_scores,lock["weights"],"logloss",lock["seed"],minimum_blocks=lock["minimum_week_blocks"])
        saved_interims = [r for r in state if r["record_type"] == "PILOT_INTERIM"]
        saved_finals = [r for r in state if r["record_type"] == "PILOT_FINAL"]
        interim_membership = _membership(adjusted[:interim])
        if saved_interims:
            previous = saved_interims[0]["payload"]
            if len(saved_interims) != 1 or previous["membership_sha256"] != digest(interim_membership):
                raise ValueError("chronological interim membership changed")
            if previous["verdict"] == "FUTILITY_STOP":
                return {**summary, "verdict": "FUTILITY_STOP", "interim": previous, "terminal": True}
        if saved_finals:
            previous = saved_finals[0]["payload"]
            if len(saved_finals) != 1 or previous["membership_sha256"] != digest(membership):
                raise ValueError("final frozen membership changed")
            return {**summary, "verdict": previous["verdict"], "final": previous, "terminal": True}
        if len(adjusted) < interim:
            return {**summary, "verdict": "WAIT_FOR_INTERIM"}
        if any(event_key(p) not in scored_keys for p in adjusted[:interim]):
            return {**summary, "verdict": "WAIT_FOR_INTERIM_SETTLEMENT", "missing_members": [list(event_key(p)) for p in adjusted[:interim] if event_key(p) not in scored_keys]}
        def subset(prefix):
            keys = {event_key(p) for p in prefix}
            return events.loc[[event_key(row) in keys for row in events.to_dict("records")]].copy()
        if not saved_interims:
            sample = subset(adjusted[:interim])
            if sample.week.nunique() < lock["minimum_week_blocks"]:
                return {**summary, "verdict": "WAIT_FOR_INTERIM_WEEK_BLOCKS"}
            score = paired_bootstrap(sample, lock["weights"], "brier", lock["seed"], minimum_blocks=lock["minimum_week_blocks"])
            payload = dict(cohort_version=lock["cohort_version"], membership=interim_membership,
                           membership_sha256=digest(interim_membership), adjusted_brier=score,
                           verdict="FUTILITY_STOP" if score["ci95"][0] > -lock["mwi_brier"] else "CONTINUE_TO_FINAL",
                           ledger_head=events.attrs["ledger_head"])
            _append_locked(state_path, "PILOT_INTERIM", payload)
            if payload["verdict"] == "FUTILITY_STOP":
                return {**summary, "verdict": "FUTILITY_STOP", "interim": payload, "terminal": True}
        if len(adjusted) < target:
            return {**summary, "verdict": "WAIT_FOR_FINAL"}
        if any(event_key(p) not in scored_keys for p in adjusted[:target]):
            return {**summary, "verdict": "WAIT_FOR_FINAL_SETTLEMENT"}
        sample = subset(adjusted[:target])
        if sample.week.nunique() < lock["minimum_week_blocks"]:
            return {**summary, "verdict": "WAIT_FOR_FINAL_WEEK_BLOCKS"}
        log = paired_bootstrap(sample, lock["weights"], "logloss", lock["seed"], minimum_blocks=lock["minimum_week_blocks"])
        brier = paired_bootstrap(sample, lock["weights"], "brier", lock["seed"], minimum_blocks=lock["minimum_week_blocks"])
        comparisons = {f"{a}_minus_baseline": paired_bootstrap(sample, lock["weights"], "logloss", lock["seed"], minimum_blocks=lock["minimum_week_blocks"], a=a, b="baseline") for a in ("model", "card")}
        payload = dict(cohort_version=lock["cohort_version"], membership=membership,
                       membership_sha256=digest(membership), adjusted_logloss=log, adjusted_brier=brier,
                       baseline_comparisons=comparisons, ledger_head=events.attrs["ledger_head"],
                       verdict="KEEP_ADJUSTMENTS" if log["ci95"][1] < 0 and brier["ci95"][1] < -lock["mwi_brier"] else "DEFAULT_TO_MODEL")
        _append_locked(state_path, "PILOT_FINAL", payload)
        return {**summary, "verdict": payload["verdict"], "final": payload, "terminal": True}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger", type=Path)
    parser.add_argument("lock", type=Path)
    parser.add_argument("--freeze-definition",type=Path)
    parser.add_argument("--registry",type=Path,default=REGISTRY)
    parser.add_argument("--sources-registry",type=Path)
    parser.add_argument("--evidence-root",type=Path)
    args = parser.parse_args()
    if args.freeze_definition:
        result=freeze_lock(args.lock,json.loads(args.freeze_definition.read_text(encoding="utf-8")),ledger_path=args.ledger,
            registry_path=args.registry,sources_registry_path=args.sources_registry,evidence_root=args.evidence_root)
    else:
        result=decision(args.ledger,args.lock)
    print(json.dumps(result,indent=2))
