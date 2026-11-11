"""EXT-v3 operational controls; sporting truth and chat execution are never inferred.

Append-only delay/access amendments preserve original event manifests and returns. Numeric
coverage, reduced research, prospective comparisons and factual accuracy remain distinct.
"""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
from pathlib import Path

from ml import external as X
from ml import research_intake as I

POLICY_FIELDS = ("method_version", "research_mode", "pricing_policy", "omitted_lanes", "reason")
UNPRICED_FIELDS = ("label", "status", "reason")
UNPRICED_STATUSES = ("UNSUPPORTED", "UNAVAILABLE", "ALL_PUSH", "NOT_VALIDATED")
DELAY_FIELDS = ("sequence", "previous_start", "effective_start", "status", "source_url", "authority",
                "observed_at", "evidence_file", "evidence_sha256", "recorded_at", "prev_sha256", "row_sha256")
ACCESS_FIELDS = ("sequence", "path", "sha256", "commit", "activated_at", "prev_sha256", "row_sha256")


def policy(folder):
    rows = I.read(Path(folder) / "POLICY.csv", POLICY_FIELDS)
    if len(rows) != 1 or rows[0]["research_mode"] not in ("FULL_FIVE", "REDUCED", "FULL_SIX"):
        raise X.ExternalError("one explicit supported research policy required")
    return rows[0]


def lane_assignments(mode, selected, requirements):
    default = ("L1", "L2", "L3", "L4", "L5", "L6") if mode == "FULL_SIX" else ("L1", "L2", "L3", "L4", "L5")
    chosen = list(selected or default)
    if len(chosen) != len(set(chosen)) or not set(chosen) <= set(X.LANES) - {"FULL"} or "L5" not in chosen:
        raise X.ExternalError("unique assigned L1-L6 lanes including L5 required")
    if mode == "FULL_FIVE" and set(chosen) != {"L1", "L2", "L3", "L4", "L5"}:
        raise X.ExternalError("FULL_FIVE requires its five roles")
    if mode == "FULL_SIX" and set(chosen) != {"L1", "L2", "L3", "L4", "L5", "L6"}:
        raise X.ExternalError("FULL_SIX requires six roles")
    if mode == "REDUCED" and not 2 <= len(chosen) < 5:
        raise X.ExternalError("REDUCED requires 2-4 explicit lanes; never call it five-chat evidence")
    if any(r["lane"] not in chosen for r in requirements):
        raise X.ExternalError("requirements name an omitted lane; explicitly revise scope before initialization")
    return [dict(lane=l, chat_label="CHAT-" + l[1:], depends_on=("L1" if l == "L4" and "L1" in chosen else
                 "|".join(sorted(set(chosen) - {"L5"})) if l == "L5" else "")) for l in sorted(chosen)]


def chain(folder, name, fields):
    path = Path(folder) / name
    rows = I.read(path, fields) if path.exists() else []
    prev = I.GENESIS
    for n, r in enumerate(rows, 1):
        if r["sequence"] != str(n) or r["prev_sha256"] != prev or r["row_sha256"] != I.sha("\x1f".join(r[k] for k in fields[:-1]).encode()):
            raise X.ExternalError(name + ": amendment chain changed")
        prev = r["row_sha256"]
    return rows


def append_chain(folder, name, fields, row):
    rows = chain(folder, name, fields)
    r = dict(sequence=str(len(rows) + 1), **row, prev_sha256=rows[-1]["row_sha256"] if rows else I.GENESIS)
    r["row_sha256"] = I.sha("\x1f".join(r[k] for k in fields[:-1]).encode())
    path = Path(folder) / name
    with path.open("ab") as f:
        data = I.csv_bytes(fields, [r]); f.write(data.split(b"\n", 1)[1] if rows else data)
    return r


def effective_start(folder, event=None):
    e = event or I.read(Path(folder) / "EVENT.csv", I.EVENT_FIELDS)[0]
    start = e["scheduled_start"]
    for r in chain(folder, "DELAYS.csv", DELAY_FIELDS):
        if r["previous_start"] != start or I.clock(r["effective_start"]) <= I.clock(start):
            raise X.ExternalError("delay amendment start chain changed")
        if I.sha(I.contained(folder, r["evidence_file"]).read_bytes()) != r["evidence_sha256"]:
            raise X.ExternalError("delay evidence changed")
        start = r["effective_start"]
    return start


def operations_sha(folder):
    """Bind append-only operational amendments without invalidating earlier research packets."""
    return I.sha(b"".join(name.encode() + b"\0" + ((Path(folder) / name).read_bytes() if (Path(folder) / name).exists() else b"")
                         for name in ("DELAYS.csv", "ACCESS_UPDATES.csv")))


def delay(folder, new_start, url, authority, observed_at, evidence, *, status="NOT_STARTED", root=I.ROOT, at=None):
    stamp = at or I.now()
    e = I.load(folder, root)
    if status != "NOT_STARTED" or not authority.strip() or not url.startswith("https://"):
        raise X.ExternalError("delay requires an official authority, exact source and NOT_STARTED confirmation")
    if not 0 <= (I.clock(stamp) - I.clock(observed_at)).total_seconds() <= 900:
        raise X.ExternalError("official no-play observation must be within 15 minutes before this amendment")
    previous = effective_start(folder, e)
    if I.clock(new_start) <= max(I.clock(stamp), I.clock(previous)):
        raise X.ExternalError("new verified start must be in the future and later than the previous start")
    raw = Path(evidence).read_bytes()
    if Path(evidence).suffix.lower() not in (".txt", ".md", ".csv") or not raw.strip() or b"<html" in raw[:500].lower():
        raise X.ExternalError("delay needs a retained sporting-only official evidence note")
    with I.locked(folder):
        if any((Path(folder) / f).exists() for f in ("APPEND_RECEIPT.csv", "CARD_BINDING.csv", "COMPARISON_FIVE.csv")):
            raise X.ExternalError("issued/frozen event cannot change horizon; retain an addendum")
        previous = effective_start(folder, e)
        if I.clock(new_start) <= max(I.clock(stamp), I.clock(previous)):
            raise X.ExternalError("delay horizon changed while acquiring the writer lock")
        name = "delay_evidence/" + I.sha(raw) + ".txt"
        target = I.contained(folder, name); target.parent.mkdir(exist_ok=True); target.write_bytes(raw)
        return append_chain(folder, "DELAYS.csv", DELAY_FIELDS, dict(previous_start=previous, effective_start=new_start,
                            status=status, source_url=url, authority=authority, observed_at=observed_at, evidence_file=name,
                            evidence_sha256=I.sha(raw), recorded_at=stamp))


def refresh_access(folder, path, commit, *, root=I.ROOT, at=None):
    """Activate an actually audited committed snapshot; never extend clocks or alter method identity."""
    I.load(folder, root)
    path = I.contained(root, path)
    relative = path.relative_to(Path(root).resolve()).as_posix()
    if not re.fullmatch(r"[0-9a-f]{40}", commit): raise X.ExternalError("full access snapshot commit required")
    blob = subprocess.run(["git", "show", commit + ":" + relative], cwd=root, capture_output=True)
    if blob.returncode or I.artifact_sha(blob.stdout) != I.artifact_sha(path.read_bytes()):
        raise X.ExternalError("access snapshot must exist unchanged at its pinned commit")
    stamp = at or I.now()
    rows = I.read(path)
    hosts = [r.get("host", "") for r in rows]
    if not rows or "" in hosts or len(hosts) != len(set(hosts)):
        raise X.ExternalError("access snapshot needs unique hosts")
    for r in rows:
        if I.clock(r["checked_at"]) > I.clock(stamp) or I.clock(r["valid_until"]) <= I.clock(stamp):
            raise X.ExternalError("access observations must be actual, already checked and still valid")
    with I.locked(folder):
        if (Path(folder) / "CARD_BINDING.csv").exists(): raise X.ExternalError("bound event access history is frozen")
        return append_chain(folder, "ACCESS_UPDATES.csv", ACCESS_FIELDS,
                            dict(path=relative, sha256=I.artifact_sha(path.read_bytes()), commit=commit, activated_at=stamp))


def access_rows(folder, root, retrieved_at):
    arts = {r["role"]: r for r in I.read(Path(folder) / "ARTIFACTS.csv", I.ART_FIELDS)}
    active = arts["access"]
    for r in chain(folder, "ACCESS_UPDATES.csv", ACCESS_FIELDS):
        p = I.contained(root, r["path"])
        blob = subprocess.run(["git", "show", r["commit"] + ":" + r["path"]], cwd=root, capture_output=True)
        if blob.returncode or I.artifact_sha(blob.stdout) != r["sha256"] or I.artifact_sha(p.read_bytes()) != r["sha256"]:
            raise X.ExternalError("access amendment artifact changed")
        if I.clock(r["activated_at"]) <= I.clock(retrieved_at): active = r
    return I.read(I.contained(root, active["path"]))


def pricing_coverage(ret, expected):
    numeric = [r["label"] for r in ret.get("PROBABILITIES", [])]
    unpriced = ret.get("UNPRICED", [])
    labels = numeric + [r["label"] for r in unpriced]
    errors = []
    if len(labels) != len(set(labels)) or set(labels) != set(expected):
        errors.append("pricing dispositions must cover every supplied contract exactly once")
    for r in unpriced:
        if r["status"] not in UNPRICED_STATUSES or not r["reason"].strip():
            errors.append("unpriced contract needs a supported status and evidence-bound reason")
    return errors


def card_unpriced(text, key):
    begin, end = f"<!-- BEGIN UNPRICED {key} -->", f"<!-- END UNPRICED {key} -->"
    if begin not in text and end not in text: return []
    if text.count(begin) != 1 or text.count(end) != 1 or text.index(end) < text.index(begin):
        raise X.ExternalError("one complete unpriced contract block required")
    import io
    r = csv.DictReader(io.StringIO(text.split(begin)[1].split(end)[0].strip()))
    if tuple(r.fieldnames or ()) != UNPRICED_FIELDS: raise X.ExternalError("exact unpriced contract columns required")
    return list(r)


def check_card_coverage(text, key, rows, folder):
    expected = {r["label"] for r in I.read(Path(folder) / "CONTRACTS.csv", I.CONTRACT_FIELDS)}
    ret = dict(PROBABILITIES=rows, UNPRICED=card_unpriced(text, key))
    errors = pricing_coverage(ret, expected)
    current = I.accepted(folder).get("L5")
    if current:
        accepted = X.parse(I.contained(folder, current["file"]).read_text(encoding="utf-8-sig"))
        if {r["label"] for r in rows} != {r["label"] for r in accepted["PROBABILITIES"]} or ret["UNPRICED"] != accepted.get("UNPRICED", []):
            errors.append("card pricing dispositions differ from accepted L5")
        by_label = {r["label"]: r for r in accepted["PROBABILITIES"]}
        if any(r["label"] in by_label and any(not I.same_number(r[k], by_label[r["label"]][k]) for k in ("w", "p", "l", "final_p")) for r in rows):
            errors.append("card probabilities differ from admitted pricing; correct L5 before issuing")
    if errors: raise X.ExternalError(" | ".join(errors))
    return ret["UNPRICED"]


def freeze_comparison(folder, receipt_path, *, which="SINGLE", root=I.ROOT, at=None, unpriced=()):
    """Actual pre-exposure SINGLE; current full-five evidence for FIVE. No historical backfill."""
    from ml.kit import cli as KC, sr_kit as K
    from ml.evaluation import prospective as P
    e = I.load(folder, root); stamp = at or I.now(); start = effective_start(folder, e)
    if I.clock(stamp) >= I.clock(start): raise X.ExternalError("comparison must freeze before the evidenced start")
    if which not in ("SINGLE", "FIVE", "REFERENCE", "BASELINE"): raise X.ExternalError("unknown comparison lane")
    target = Path(folder) / ("COMPARISON_" + which + ".csv")
    with I.locked(folder):
        if target.exists(): raise X.ExternalError("comparison is immutable; never replace a forecast")
        if which != "FIVE" and (I.ledger(folder) or (Path(folder) / "PACKET_RELEASES.csv").exists()):
            raise X.ExternalError("pre-research comparison must freeze before external packet release or return exposure")
        if which == "FIVE":
            if policy(folder)["research_mode"] != "FULL_FIVE": raise X.ExternalError("reduced/six-lane research is a separate experimental cohort")
            I._admit(folder, root=root, at=stamp)
        raw = Path(receipt_path).read_text(encoding="utf-8-sig")
        rec = KC.parse_receipt(raw)
        probabilities = [dict(r, kit_receipt_sha256=K.receipt_sha256(raw)) for r in rec["rows"]]
        errors = I.verify_prices(dict(PROBABILITIES=probabilities, UNPRICED=list(unpriced)), raw, folder, root)
        if errors: raise X.ExternalError("comparison receipt: " + " | ".join(errors))
        if not probabilities: raise X.ExternalError("no numeric comparison")
        if which == "FIVE":
            ret = X.parse(I.contained(folder, I.accepted(folder)["L5"]["file"]).read_text(encoding="utf-8-sig"))
            accepted_prices = {r["label"]: r for r in ret["PROBABILITIES"]}
            if set(accepted_prices) != {r["label"] for r in probabilities} or any(not I.same_number(r["final_p"], accepted_prices[r["label"]]["final_p"]) for r in probabilities):
                raise X.ExternalError("FIVE comparison differs from admitted L5")
        contracts = {r["label"]: r for r in I.read(Path(folder) / "CONTRACTS.csv", I.CONTRACT_FIELDS)}
        rows = []
        for rank, r in enumerate(probabilities, 1):
            c = contracts[r["label"]]
            contract_key = I.sha(I.csv_bytes(I.CONTRACT_FIELDS, [c]))
            rows.append(dict(forecast_id=e["event_key"] + ":" + which, model_id={"SINGLE": "SINGLE_RESEARCH", "FIVE": "FIVE_LANES", "REFERENCE": "REFERENCE", "BASELINE": "BASELINE"}[which],
                             model_version=policy(folder)["method_version"], role="CANDIDATE" if which == "FIVE" else "CHAMPION",
                             event_id=e["event_key"], competition=e["competition"], endpoint=c["endpoint"], contract_key=contract_key,
                             family=c["family"], side=c["side"], line=c["line"], p=r["final_p"], rank=str(rank), issued_at=stamp,
                             scheduled_start=start, training_release="NONE", param_version=policy(folder)["method_version"],
                             code_sha256=I.sha(Path(__file__).read_bytes()), evidence_status="PRE_START_VERIFIED"))
        P.freeze(target, rows, now=stamp)
        (Path(folder) / ("COMPARISON_" + which + "_RECEIPT.md")).write_text(raw, encoding="utf-8")
    return dict(status="FROZEN_LOCAL_NOT_PUBLICATION_PROOF", rows=len(rows), model=which, ledger=str(target))


def packet(folder, lane, *, root=I.ROOT, at=None, out=None):
    e = I.load(folder, root); stamp = at or I.now()
    digest = I.packet_hash(folder, lane)
    assignment = next(r for r in I.read(Path(folder) / "LANES.csv", I.LANE_FIELDS) if r["lane"] == lane)
    reqs = [r for r in I.read(Path(folder) / "REQUIREMENTS.csv", I.REQ_FIELDS) if r["lane"] == lane]
    lines = ["# Research packet", "", *[k + ": " + e[k] for k in ("event_key", "commit", "sport", "competition", "home", "away")],
             "profile_version: " + X.PROFILE_VERSION, "lane: " + lane, "chat_label: " + assignment["chat_label"],
             "research_mode: " + policy(folder)["research_mode"], "scheduled_start: " + e["scheduled_start"],
             "effective_start: " + effective_start(folder, e), "manifest_sha256: " + I.manifest_hash(folder),
             "input_package_sha256: " + digest, "generated_at: " + stamp, "", "## Exact contracts", "",
             (Path(folder) / "CONTRACTS.csv").read_text(encoding="utf-8-sig"), "## Assigned requirements", "",
             I.csv_bytes(I.REQ_FIELDS, reqs).decode(), "## Pinned artifacts", "", (Path(folder) / "ARTIFACTS.csv").read_text(encoding="utf-8-sig")]
    current = I.accepted(folder)
    for dep in filter(None, assignment["depends_on"].split("|")):
        lines += ["## Accepted " + dep, "", I.contained(folder, current[dep]["file"]).read_text(encoding="utf-8-sig")]
    if lane == "L5": lines += ["## Reviewed collectors", "", (Path(folder) / "SOURCE_REVIEW.csv").read_text(encoding="utf-8-sig")]
    text = "\n".join(lines) + "\n"
    if out:
        target = Path(out)
        if target.exists(): raise X.ExternalError("packet output exists; retain prior versions")
        target.write_text(text, encoding="utf-8")
    with I.locked(folder):
        path = Path(folder) / "PACKET_RELEASES.csv"
        fields = ("lane", "packet_sha256", "released_at")
        with path.open("ab") as f:
            data = I.csv_bytes(fields, [dict(lane=lane, packet_sha256=digest, released_at=stamp)])
            f.write(data.split(b"\n", 1)[1] if path.stat().st_size else data)
    return text


FACT_FIELDS = ("fact_id", "actual_value", "disposition", "source_url", "observed_at", "reason")


def facts(folder):
    result = []
    for lane, intake in I.accepted(folder).items():
        ret = X.parse(I.contained(folder, intake["file"]).read_text(encoding="utf-8-sig"))
        for n, r in enumerate(ret["EVIDENCE"]):
            result.append(dict(fact_id=I.sha((intake["return_sha256"] + ":" + str(n)).encode()), lane=lane,
                               return_sha256=intake["return_sha256"], **r))
    return result


def score_facts(folder, observations, out, final_at, *, root=I.ROOT, at=None):
    I.load(folder, root); stamp = at or I.now()
    if not I.clock(effective_start(folder)) < I.clock(final_at) <= I.clock(stamp):
        raise X.ExternalError("fact scoring is settlement-only, with a verified final time")
    claims = facts(folder); known = {r["fact_id"]: r for r in claims}
    obs = I.read(observations, FACT_FIELDS)
    if len({r["fact_id"] for r in obs}) != len(obs) or any(r["fact_id"] not in known for r in obs):
        raise X.ExternalError("observations must reference unique exact accepted facts")
    for r in obs:
        if r["disposition"] not in ("CORRECT", "INCORRECT", "UNRESOLVED", "NOT_APPLICABLE") or not r["reason"].strip():
            raise X.ExternalError("fact dispositions need an explicit evidence-bound reason")
        if r["disposition"] in ("CORRECT", "INCORRECT") and (not r["actual_value"] or not r["source_url"].startswith("https://")):
            raise X.ExternalError("scored facts need an actual value and settlement evidence URL")
        if I.clock(r["observed_at"]) > I.clock(stamp): raise X.ExternalError("future fact observation")
        if known[r["fact_id"]]["confirmation"] == "PROJECTED" and r["disposition"] in ("CORRECT", "INCORRECT"):
            raise X.ExternalError("projected statements need a separately defined forecast target; exclude from confirmed-fact accuracy")
    by_id = {r["fact_id"]: r for r in obs}
    reviews = {r["source_url"]: r for r in I.reviews(folder)}
    scored = []
    for r in claims:
        o = by_id.get(r["fact_id"], dict(actual_value="", disposition="UNRESOLVED", source_url="", observed_at="", reason="No settlement observation supplied"))
        scored.append(dict(fact_id=r["fact_id"], lane=r["lane"], side=r["side"], field=r["field"], claimed_value=r["value"],
                           pregame_source=r["source_url"], collector=reviews.get(r["source_url"], {}).get("collector_id", "UNKNOWN"),
                           **{k: o[k] for k in FACT_FIELDS if k != "fact_id"}))
    out = Path(out); out.mkdir(parents=True, exist_ok=False)
    (out / "FACT_SCORES.csv").write_bytes(I.csv_bytes(tuple(scored[0]) if scored else ("fact_id",), scored))
    summaries = []
    for field in ("lane", "collector"):
        for key in sorted({r[field] for r in scored}):
            group = [r for r in scored if r[field] == key]
            count = {d: sum(r["disposition"] == d for r in group) for d in ("CORRECT", "INCORRECT", "UNRESOLVED", "NOT_APPLICABLE")}
            n = count["CORRECT"] + count["INCORRECT"]
            summaries.append(dict(group_type=field, group=key, **count, scored=n, total=len(group), accuracy=count["CORRECT"] / n if n else "",
                                  interpretation="DESCRIPTIVE_DEPENDENT_FACTS_NOT_PREDICTIVE_SKILL"))
    (out / "SUMMARY.csv").write_bytes(I.csv_bytes(tuple(summaries[0]) if summaries else ("group_type",), summaries))
    receipt = dict(manifest_sha256=I.manifest_hash(folder), intake_sha256=I.sha((Path(folder) / "INTAKE.csv").read_bytes()),
                   observations_sha256=I.sha(Path(observations).read_bytes()), verified_final_at=final_at, scored_at=stamp)
    (out / "RECEIPT.csv").write_bytes(I.csv_bytes(tuple(receipt), [receipt]))
    return summaries


EFFORT_FIELDS = ("category", "minutes", "recorded_at", "notes")


def record_effort(folder, category, minutes, notes, *, at=None):
    import math
    if category not in ("WRITER_REVIEW", "OWNER_TRANSFER", "OTHER_LABOUR") or not math.isfinite(float(minutes)) or float(minutes) < 0:
        raise X.ExternalError("effort requires a supported category and finite nonnegative minutes")
    with I.locked(folder):
        path = Path(folder) / "EFFORT.csv"
        row = dict(category=category, minutes=str(minutes), recorded_at=at or I.now(), notes=notes)
        with path.open("ab") as f:
            data = I.csv_bytes(EFFORT_FIELDS, [row]); f.write(data.split(b"\n", 1)[1] if path.stat().st_size else data)
    return row


def operating_report(folder, out, *, root=I.ROOT, at=None):
    e = I.load(folder, root); stamp = at or I.now(); current = I.accepted(folder); seconds = 0.0
    for r in current.values():
        h = X.parse(I.contained(folder, r["file"]).read_text(encoding="utf-8-sig"))["header"]
        seconds += (I.clock(h["completed_at"]) - I.clock(h["started_at"])).total_seconds()
    efforts = I.read(Path(folder) / "EFFORT.csv", EFFORT_FIELDS) if (Path(folder) / "EFFORT.csv").exists() else []
    row = dict(event_key=e["event_key"], research_mode=policy(folder)["research_mode"], accepted_lanes=len(current),
               refused_attempts=sum(r["status"] == "REFUSED" for r in I.ledger(folder)),
               elapsed_wall_minutes=(I.clock(stamp) - I.clock(e["created_at"])).total_seconds() / 60,
               declared_lane_labour_minutes=seconds / 60, recorded_owner_writer_minutes=sum(float(r["minutes"]) for r in efforts),
               owner_effort_status="RECORDED" if efforts else "MISSING_NOT_ZERO", evaluated_at=stamp,
               clock_limit="CHAT_CLOCKS_ARE_DECLARED_LOCAL_INTAKE_CLOCK_IS_MEASURED")
    out = Path(out); out.mkdir(parents=True, exist_ok=False)
    (out / "OPERATING_REPORT.csv").write_bytes(I.csv_bytes(tuple(row), [row]))
    return row


def collect_comparisons(events, out, *, root=I.ROOT):
    """Derived evaluation view of verified originals; original issue clocks never change.

    Rechaining an export is not a new freeze/publication. Preserve source hashes so an
    auditor can reproduce every row from each event's immutable comparison ledger.
    """
    from ml.evaluation import prospective as P
    originals, sources, coverage, seen = [], [], [], set()
    for folder in map(Path, events):
        e = I.load(folder, root)
        if e["event_key"] in seen: raise X.ExternalError("duplicate event in comparison collection")
        seen.add(e["event_key"]); ledgers = {}
        for which in ("SINGLE", "FIVE", "REFERENCE", "BASELINE"):
            path = folder / ("COMPARISON_" + which + ".csv")
            if not path.exists(): continue
            raw = path.read_bytes(); rows = P.verify_ledger(path)
            if raw != path.read_bytes(): raise X.ExternalError("comparison changed during collection")
            expected = {"SINGLE": "SINGLE_RESEARCH", "FIVE": "FIVE_LANES", "REFERENCE": "REFERENCE", "BASELINE": "BASELINE"}[which]
            if any(r["event_id"] != e["event_key"] or r["model_id"] != expected or r["model_version"] != policy(folder)["method_version"] for r in rows):
                raise X.ExternalError("comparison identity differs from its source event")
            ledgers[which] = rows
            sources.append(dict(event_key=e["event_key"], kind=which, path=str(path), sha256=I.sha(raw), provenance="DERIVED_EXPORT_NOT_NEW_ISSUANCE"))
        status = "PAIRED" if {"SINGLE", "FIVE"} <= set(ledgers) else "UNPAIRED"
        if policy(folder)["research_mode"] != "FULL_FIVE": status = "SEPARATE_MODE"
        if status == "PAIRED" and {r["scheduled_start"] for rs in ledgers.values() for r in rs} != {effective_start(folder, e)}:
            status = "CHANGED_HORIZON_EXCLUDED"
        coverage.append(dict(event_key=e["event_key"], mode=policy(folder)["research_mode"], status=status,
                             single_rows=len(ledgers.get("SINGLE", [])), five_rows=len(ledgers.get("FIVE", [])), reference_rows=len(ledgers.get("REFERENCE", [])), baseline_rows=len(ledgers.get("BASELINE", []))))
        if status == "PAIRED": originals += [r for rs in ledgers.values() for r in rs]
    rows, prev = [], P.GENESIS
    for original in sorted(originals, key=lambda r: (r["issued_at"], r["event_id"], r["model_id"], r["contract_key"])):
        r = dict(original); r["prev_row_sha256"] = prev; r["row_sha256"] = prev = P._row_hash(r); rows.append(r)
    out = Path(out); out.mkdir(parents=True, exist_ok=False)
    (out / "FORECASTS.csv").write_bytes(I.csv_bytes(P.LEDGER_FIELDS, rows))
    (out / "SOURCES.csv").write_bytes(I.csv_bytes(tuple(sources[0]) if sources else ("event_key",), sources))
    (out / "EVENT_COVERAGE.csv").write_bytes(I.csv_bytes(tuple(coverage[0]) if coverage else ("event_key",), coverage))
    P.verify_ledger(out / "FORECASTS.csv")
    return coverage


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__); sub = p.add_subparsers(dest="command", required=True)
    c = sub.add_parser("clock"); c.add_argument("--out", type=Path)
    d = sub.add_parser("delay"); d.add_argument("--event", type=Path, required=True); d.add_argument("--new-start", required=True)
    for flag in ("url", "authority", "observed-at"): d.add_argument("--" + flag, required=True)
    d.add_argument("--evidence", type=Path, required=True)
    a = sub.add_parser("refresh-access"); a.add_argument("--event", type=Path, required=True); a.add_argument("--path", required=True); a.add_argument("--commit", required=True)
    for cmd in ("freeze-single", "freeze-five", "freeze-reference", "freeze-baseline"):
        a = sub.add_parser(cmd); a.add_argument("--event", type=Path, required=True); a.add_argument("--receipt", type=Path, required=True)
        a.add_argument("--unpriced", type=Path)
    a = sub.add_parser("fact-template"); a.add_argument("--event", type=Path, required=True); a.add_argument("--out", type=Path, required=True)
    a = sub.add_parser("score-facts"); a.add_argument("--event", type=Path, required=True); a.add_argument("--observations", type=Path, required=True)
    a.add_argument("--out", type=Path, required=True); a.add_argument("--final-at", required=True)
    a = sub.add_parser("intake-batch"); a.add_argument("--event", type=Path, required=True); a.add_argument("--files", type=Path, nargs="+", required=True)
    a = sub.add_parser("review-sources"); a.add_argument("--event", type=Path, required=True); a.add_argument("--mapping", type=Path, required=True)
    a.add_argument("--evidence", type=Path, required=True)
    a = sub.add_parser("effort"); a.add_argument("--event", type=Path, required=True); a.add_argument("--category", required=True)
    a.add_argument("--minutes", type=float, required=True); a.add_argument("--notes", default="")
    a = sub.add_parser("report"); a.add_argument("--event", type=Path, required=True); a.add_argument("--out", type=Path, required=True)
    a = sub.add_parser("collect-comparisons"); a.add_argument("--events", nargs="+", type=Path, required=True); a.add_argument("--out", type=Path, required=True)
    args = p.parse_args(argv)
    try:
        if args.command == "clock":
            row = dict(utc=I.now(), clock_basis="PYTHON_DATETIME_UTC", publication_proof="NO")
            if args.out:
                with args.out.open("xb") as f: f.write(I.csv_bytes(tuple(row), [row]))
            print(row)
        elif args.command == "delay": print(delay(args.event, args.new_start, args.url, args.authority, args.observed_at, args.evidence))
        elif args.command == "refresh-access": print(refresh_access(args.event, args.path, args.commit))
        elif args.command in ("freeze-single", "freeze-five", "freeze-reference", "freeze-baseline"):
            print(freeze_comparison(args.event, args.receipt, which=args.command.split("-", 1)[1].upper(),
                                    unpriced=I.read(args.unpriced, UNPRICED_FIELDS) if args.unpriced else ()))
        elif args.command == "fact-template":
            I.load(args.event)
            rows = [dict(fact_id=r["fact_id"], actual_value="", disposition="UNRESOLVED", source_url="", observed_at="", reason="") for r in facts(args.event)]
            with args.out.open("xb") as f: f.write(I.csv_bytes(FACT_FIELDS, rows))
            with args.out.with_suffix(".CLAIMS.csv").open("xb") as f:
                claims = facts(args.event); f.write(I.csv_bytes(tuple(claims[0]) if claims else ("fact_id",), claims))
        elif args.command == "score-facts": print(score_facts(args.event, args.observations, args.out, args.final_at))
        elif args.command == "intake-batch":
            failed = False
            for path in args.files:
                result = I.intake(args.event, path); print(path, result); failed |= result["status"] == "REFUSED"
            if failed: raise SystemExit(1)
        elif args.command == "review-sources":
            I.load(args.event)
            for r in I.read(args.mapping, ("source_url", "collector_id", "lineage_status")):
                prior = next((p for p in I.reviews(args.event) if p["source_url"] == r["source_url"]), None)
                if prior:
                    if prior["collector_id"] != r["collector_id"] or prior["lineage_status"] != r["lineage_status"]:
                        raise X.ExternalError("source review correction needs a new package")
                    continue
                I.review_source(args.event, r["source_url"], r["collector_id"], args.evidence, status=r["lineage_status"])
        elif args.command == "effort":
            I.load(args.event); print(record_effort(args.event, args.category, args.minutes, args.notes))
        elif args.command == "report": print(operating_report(args.event, args.out))
        elif args.command == "collect-comparisons": print(collect_comparisons(args.events, args.out))
    except (X.ExternalError, ValueError, OSError, KeyError) as exc: raise SystemExit(str(exc)) from exc
