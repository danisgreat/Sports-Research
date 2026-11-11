"""EXT-v2: immutable CSV event manifests, dependency-bound lane intake and one issuing-card gate.

No chat execution or source truth is inferred. Original returns (including refusals) are retained;
only the manifest-bound admission command produces an issuance-ready evidence receipt.
"""
from __future__ import annotations

import argparse
import contextlib
import csv
import hashlib
import io
import math
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from ml import external as X

ROOT = Path(__file__).resolve().parents[1]
VERSION = "EXT-v2"
EVENT_FIELDS = ("manifest_version", "profile_version", "commit", "event_key", "sport", "competition", "native_event_id",
                "home", "away", "scheduled_start", "game_number", "mini_path", "local_key", "writer", "created_at")
CONTRACT_FIELDS = ("label", "family", "side", "line", "period", "endpoint", "action", "unit")
REQ_FIELDS = ("lane", "requirement_id", "side", "field", "required", "corroboration_required")
LANE_FIELDS = ("lane", "chat_label", "depends_on")
ART_FIELDS = ("role", "path", "sha256")
REVIEW_FIELDS = ("source_url", "collector_id", "lineage_status", "review_evidence_path", "review_evidence_sha256", "reviewed_at")
INTAKE_FIELDS = ("sequence", "lane", "chat_label", "return_sha256", "file", "packet_sha256", "parent_sha256", "status",
                 "problems", "recorded_at", "prev_sha256", "row_sha256")
IMMUTABLE = ("EVENT.csv", "CONTRACTS.csv", "REQUIREMENTS.csv", "LANES.csv", "ARTIFACTS.csv")
COMPLETE = ("DONE", "UNAVAILABLE", "NOT_APPLICABLE")
GENESIS = "0" * 64


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def artifact_sha(raw: bytes) -> str:
    """Canonical LF for UTF-8 text artifacts; original returns/mini/lineage receipts always use raw byte hashes."""
    raw.decode("utf-8-sig")
    return sha(raw.replace(b"\r\n", b"\n"))


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def clock(value: str):
    if not X._time_ok(value):
        raise X.ExternalError(f"offset-aware ISO time required: {value!r}")
    return X.clock_time(value)


def csv_bytes(fields, rows):
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue().encode("utf-8")


def read(path, fields=None):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        if fields and tuple(r.fieldnames or ()) != tuple(fields):
            raise X.ExternalError(f"{path}: exact columns required: {','.join(fields)}")
        rows = list(r)
    if any(None in r or any(v is None for v in r.values()) for r in rows):
        raise X.ExternalError(f"{path}: malformed CSV row")
    return rows


def contained(base, name):
    base = Path(base).resolve()
    path = (base / name).resolve()
    if not path.is_relative_to(base):
        raise X.ExternalError(f"path escapes its authorized folder: {name}")
    return path


@contextlib.contextmanager
def locked(folder):
    path = Path(folder) / "INTAKE_LOCK.txt"
    try:
        f = path.open("x", encoding="utf-8")
    except FileExistsError:
        raise X.ExternalError(f"another writer holds {path}; investigate before retrying") from None
    try:
        with f:
            f.write(now())
        yield
    finally:
        path.unlink()


def manifest_hash(folder):
    folder = Path(folder)
    return sha(b"".join(name.encode() + b"\0" + (folder / name).read_bytes() for name in IMMUTABLE))


def load(folder, root=ROOT):
    folder = Path(folder)
    events = read(folder / "EVENT.csv", EVENT_FIELDS)
    if len(events) != 1:
        raise X.ExternalError("one immutable event manifest required")
    e = events[0]
    saved = folder / "MANIFEST_SHA256.txt"
    if saved.exists() and saved.read_text(encoding="utf-8").strip() != manifest_hash(folder):
        raise X.ExternalError("immutable manifest files changed")
    if e["manifest_version"] != VERSION or e["profile_version"] != X.PROFILE_VERSION:
        raise X.ExternalError("manifest/profile version is not the current release")
    expected = X.event_key(e["sport"], clock(e["scheduled_start"]).date().isoformat(), e["home"], e["away"],
                           competition=e["competition"], native_event_id=e["native_event_id"], game_number=e["game_number"])
    if expected != e["event_key"] or not re.fullmatch(r"LOCAL-[A-Z0-9]+-G[0-9]{4,}", e["local_key"]):
        raise X.ExternalError("manifest event/local identity mismatch")
    for art in read(folder / "ARTIFACTS.csv", ART_FIELDS):
        path = contained(root, art["path"])
        if not path.is_file() or artifact_sha(path.read_bytes()) != art["sha256"]:
            raise X.ExternalError(f"stale or missing pinned artifact {art['path']}")
        committed = subprocess.run(["git", "show", e["commit"] + ":" + art["path"]], cwd=root, capture_output=True)
        if committed.returncode or artifact_sha(committed.stdout) != art["sha256"]:
            raise X.ExternalError(f"artifact is not present unchanged at pinned commit: {art['path']}")
        if art["role"] == "kit":
            from ml.kit import sr_kit as K
            if art["sha256"] != K.file_sha256(): raise X.ExternalError("pinned kit differs from the runtime used for verification")
    return e


def initialize(event, contracts, requirements, out, *, artifacts, root=ROOT, at=None):
    """Create only after controls/kit/reference inputs exist at the supplied committed revision."""
    stamp = at or now()
    e = {k: str(event.get(k, "")) for k in EVENT_FIELDS}
    for k in ("sport", "competition", "native_event_id", "home", "away", "scheduled_start", "mini_path", "local_key", "writer"):
        if not e[k]: raise X.ExternalError(f"event missing {k}")
    if e["home"] == e["away"]:
        raise X.ExternalError("distinct participants required")
    clock(e["scheduled_start"])  # Late requests can be retained, but intake/admit never calls them pregame.
    contained(root, e["mini_path"])
    if not re.fullmatch(r"LOCAL-[A-Z0-9]+-G[0-9]{4,}", e["local_key"]):
        raise X.ExternalError("invalid stable local key")
    if not re.fullmatch(r"[0-9a-f]{40}", e["commit"]):
        raise X.ExternalError("event must pin a full committed release SHA")
    e.update(manifest_version=VERSION, profile_version=X.PROFILE_VERSION, created_at=stamp,
             event_key=X.event_key(e["sport"], clock(e["scheduled_start"]).date().isoformat(), e["home"], e["away"],
                                   competition=e["competition"], native_event_id=e["native_event_id"], game_number=e["game_number"]))
    labels = [r["label"] for r in contracts]
    if not labels or len(labels) != len(set(labels)):
        raise X.ExternalError("nonempty unique supplied contracts required")
    for r in contracts:
        if set(r) != set(CONTRACT_FIELDS) or any(not r[k] for k in CONTRACT_FIELDS if k != "line"):
            raise X.ExternalError("contracts need exact endpoint, period, action and unit fields")
    reqs = [r["requirement_id"] for r in requirements]
    if not reqs or len(reqs) != len(set(reqs)):
        raise X.ExternalError("nonempty unique research requirements required")
    for r in requirements:
        if set(r) != set(REQ_FIELDS) or r["lane"] not in X.LANES or r["side"] not in X.SIDES:
            raise X.ExternalError("invalid research requirement")
        if r["required"] not in ("YES", "NO") or r["corroboration_required"] not in ("YES", "NO"):
            raise X.ExternalError("requirement flags are YES/NO")
    lanes = [dict(lane=f"L{i}", chat_label=f"CHAT-{i}", depends_on="L1" if i == 4 else "L1|L2|L3|L4" if i == 5 else "") for i in range(1, 6)]
    ars = []
    for role, relative in artifacts.items():
        p = contained(root, relative)
        if not p.is_file(): raise X.ExternalError(f"missing {role} artifact {relative}")
        committed = subprocess.run(["git", "show", e["commit"] + ":" + relative], cwd=root, capture_output=True)
        if committed.returncode or artifact_sha(committed.stdout) != artifact_sha(p.read_bytes()):
            raise X.ExternalError(f"{relative}: commit this exact artifact before starting an event")
        ars.append(dict(role=role, path=relative, sha256=artifact_sha(p.read_bytes())))
    if not {"kit", "params", "phases", "reference", "access"} <= set(artifacts):
        raise X.ExternalError("kit, params, phases, access rules and frozen reference artifacts are required")
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    for name, fields, rows in (("EVENT.csv", EVENT_FIELDS, [e]), ("CONTRACTS.csv", CONTRACT_FIELDS, contracts),
                              ("REQUIREMENTS.csv", REQ_FIELDS, requirements), ("LANES.csv", LANE_FIELDS, lanes),
                              ("ARTIFACTS.csv", ART_FIELDS, ars), ("SOURCE_REVIEW.csv", REVIEW_FIELDS, []),
                              ("INTAKE.csv", INTAKE_FIELDS, [])):
        (out / name).write_bytes(csv_bytes(fields, rows))
    load(out, root)
    (out / "MANIFEST_SHA256.txt").write_text(manifest_hash(out) + "\n", encoding="utf-8")
    return e


def ledger(folder):
    rows = read(Path(folder) / "INTAKE.csv", INTAKE_FIELDS)
    prev = GENESIS
    for i, r in enumerate(rows, 1):
        actual = sha("\x1f".join(r[k] for k in INTAKE_FIELDS[:-1]).encode())
        if r["sequence"] != str(i) or r["prev_sha256"] != prev or r["row_sha256"] != actual:
            raise X.ExternalError("intake history hash chain/sequence is broken")
        if sha(contained(folder, r["file"]).read_bytes()) != r["return_sha256"]:
            raise X.ExternalError("original intake bytes changed")
        prev = r["row_sha256"]
    return rows


def accepted(folder):
    out = {}
    for r in ledger(folder):
        if r["status"] == "ACCEPTED": out[r["lane"]] = r
    return out


def packet_hash(folder, lane):
    assignments = {r["lane"]: r for r in read(Path(folder) / "LANES.csv", LANE_FIELDS)}
    if lane not in assignments: raise X.ExternalError("lane is not assigned in this event")
    acc = accepted(folder)
    dep = assignments[lane]["depends_on"].split("|") if assignments[lane]["depends_on"] else []
    if any(d not in acc for d in dep): raise X.ExternalError(f"{lane} awaits {','.join(d for d in dep if d not in acc)}")
    for d in dep:
        if acc[d]["packet_sha256"] != packet_hash(folder, d):
            raise X.ExternalError(f"dependency {d} is stale after an upstream correction")
    payload = manifest_hash(folder) + "".join(d + acc[d]["return_sha256"] for d in dep)
    if lane == "L5": payload += sha((Path(folder) / "SOURCE_REVIEW.csv").read_bytes())
    return sha(payload.encode())


def validate_return(ret, text, folder, *, root=ROOT, at=None):
    e = load(folder, root)
    problems = X.check(ret)
    h = ret["header"]
    for field, expected in (("event_key", e["event_key"]), ("commit", e["commit"]),
                            ("manifest_sha256", manifest_hash(folder)), ("outcome_exposure", "NONE_DECLARED")):
        if h.get(field) != expected: problems.append(f"header {field} does not match the event admission contract")
    lane = h.get("lane", "")
    assignment = next((r for r in read(Path(folder) / "LANES.csv", LANE_FIELDS) if r["lane"] == lane), None)
    if not assignment or h.get("chat_label") != assignment["chat_label"]:
        problems.append("unassigned lane/chat")
    try:
        expected = packet_hash(folder, lane)
        if h.get("input_package_sha256") != expected: problems.append("stale or missing dependency-bound input package")
    except X.ExternalError as exc: problems.append(str(exc))
    horizon = clock(e["scheduled_start"])
    if clock(at or now()) >= horizon: problems.append("post-start intake is retained but cannot be admitted as pregame")
    for field in ("started_at", "completed_at"):
        if X._time_ok(h.get(field, "")) and clock(h[field]) >= horizon: problems.append(f"{field} is outside pregame horizon")
    if X._time_ok(h.get("completed_at", "")) and clock(h["completed_at"]) > clock(at or now()):
        problems.append("completion is in the future relative to actual intake")
    if X._time_ok(h.get("started_at", "")) and clock(h["started_at"]) < clock(e["created_at"]):
        problems.append("research starts before this event package exists")
    if assignment and X._time_ok(h.get("started_at", "")):
        current = accepted(folder)
        for dep in filter(None, assignment["depends_on"].split("|")):
            if dep in current and clock(h["started_at"]) < clock(current[dep]["recorded_at"]):
                problems.append(f"{lane} starts before accepted dependency {dep}")
    for r in ret["EVIDENCE"]:
        for field in ("published_at", "retrieved_at"):
            if not X._time_ok(r[field]) or clock(r[field]) >= horizon:
                problems.append(f"{r['field']}: {field} is unknown or outside the pregame horizon")
    for r in ret["ACCESS_LOG"]:
        if not X._time_ok(r["checked_at"]): continue
        if clock(r["checked_at"]) >= horizon or (X._time_ok(h.get("completed_at", "")) and clock(r["checked_at"]) > clock(h["completed_at"])):
            problems.append("access check is after completion or the horizon")
    arts = {r["role"]: r for r in read(Path(folder) / "ARTIFACTS.csv", ART_FIELDS)}
    rules = read(contained(root, arts["access"]["path"]))
    by_host = {r["host"].lower(): r for r in rules}
    from urllib.parse import urlparse
    reader_column = {"CHATGPT_BROWSING": "chatgpt_browsing", "CLAUDE_AGENT": "claude_agent"}.get(h.get("reader"))
    path_column = "chatgpt_blocked_paths" if h.get("reader") == "CHATGPT_BROWSING" else "claude_blocked_paths"
    access_sources = [dict(source_url=r["url"], source_class="PROVIDER" if r["url"].startswith("https://") else "OWNER_CAPTURE")
                      for r in ret["ACCESS_LOG"] if r["result"] == "OPENED"]
    for r in ret["EVIDENCE"] + access_sources:
        if r["source_class"] == "OWNER_CAPTURE":
            # An actual received owner file must exist, with its own access record; never open the blocked platform.
            try:
                if not contained(folder, r["source_url"]).is_file(): problems.append("owner capture file is missing")
            except X.ExternalError as exc: problems.append(str(exc))
            continue
        parsed = urlparse(r["source_url"])
        if reader_column is None:
            problems.append("OWNER input must use an actual owner capture; no automated owner-reader access is inferred"); continue
        rule = by_host.get((parsed.hostname or "").lower())
        if not rule: problems.append(f"{r['source_url']}: no pinned reader access decision"); continue
        status = rule.get(reader_column, "RULES_UNKNOWN")
        if status not in ("ALLOWED", "NO_RULES_FILE", "PARTLY_BLOCKED"):
            problems.append(f"{r['source_url']}: blocked or unknown reader access")
        if not X._time_ok(rule.get("valid_until", "")) or clock(rule["valid_until"]) <= clock(at or now()):
            problems.append("reader access decision expired; refresh the versioned package")
        if status == "PARTLY_BLOCKED":
            for path in rule.get(path_column, "").split():
                pattern = re.escape(path).replace(r"\*", ".*")
                if pattern.endswith(r"\$"): pattern = pattern[:-2] + "$"
                if re.match(pattern, parsed.path + ("?" + parsed.query if parsed.query else "")):
                    problems.append(f"{r['source_url']}: path is blocked; a root allowance is not path permission")
    reqs = [r for r in read(Path(folder) / "REQUIREMENTS.csv", REQ_FIELDS) if r["lane"] == lane]
    disp = {r["requirement_id"]: r for r in ret.get("REQUIREMENTS", [])}
    if len(disp) != len(ret.get("REQUIREMENTS", [])) or set(disp) != {r["requirement_id"] for r in reqs}:
        problems.append("requirement dispositions must cover exactly the assigned requirements, once each")
    for r in reqs:
        d = disp.get(r["requirement_id"], {})
        if d.get("status") not in COMPLETE: problems.append(f"{r['requirement_id']}: procedure not completed")
        if d.get("status") in ("UNAVAILABLE", "NOT_APPLICABLE") and not d.get("reason", "").strip():
            problems.append(f"{r['requirement_id']}: missing evidence-bound reason")
        if d.get("status") == "DONE" and not any(v["side"] == r["side"] and v["field"] == r["field"] for v in ret["EVIDENCE"]):
            if lane != "L5": problems.append(f"{r['requirement_id']}: DONE without its evidence")
    if lane in X.PRICING_LANES:
        problems += verify_prices(ret, text, folder, root)
    return sorted(set(problems))


def verify_prices(ret, text, folder, root=ROOT):
    from ml.kit import cli as KC, sr_kit as K
    problems = []
    e = read(Path(folder) / "EVENT.csv", EVENT_FIELDS)[0]
    arts = {r["role"]: contained(root, r["path"]) for r in read(Path(folder) / "ARTIFACTS.csv", ART_FIELDS)}
    expected = {r["label"]: r for r in read(Path(folder) / "CONTRACTS.csv", CONTRACT_FIELDS)}
    rows = ret["PROBABILITIES"]
    if len(rows) != len(expected) or {r["label"] for r in rows} != set(expected):
        problems.append("pricing must cover every expected supplied contract exactly once")
    receipts = {}
    for m in re.finditer(r"<!-- BEGIN KIT_RECEIPT (\S+) -->.*?<!-- END KIT_RECEIPT \1 -->", text, re.S):
        receipt = m.group(0)
        try:
            errors = KC.verify(receipt, params=arts["params"], phases=arts["phases"])
            if errors: problems.extend(errors); continue
            rec = KC.parse_receipt(receipt)
            if rec["inputs"].get("competition") != e["competition"]: problems.append("receipt prices a different competition")
            if rec["inputs"].get("purpose", "PRIMARY") != "PRIMARY": problems.append("sensitivity receipt cannot supply a primary card")
            receipts[K.receipt_sha256(receipt)] = {r["label"]: r for r in rec["rows"]}
        except (ValueError, KeyError, TypeError) as exc: problems.append(f"receipt refused: {exc}")
    for r in rows:
        c = expected.get(r["label"])
        if c is None: continue
        if any(str(r[k]).upper() != str(c[k]).upper() for k in ("family", "side")) or not same_number(r["line"], c["line"]):
            problems.append(f"{r['label']}: supplied contract differs from manifest")
        got = receipts.get(r["kit_receipt_sha256"], {}).get(r["label"])
        if got is None: problems.append(f"{r['label']}: no matching verified receipt output")
        elif any(not same_number(r[k], got[k]) for k in ("line", "w", "p", "l", "final_p")) or any(r[k].upper() != got[k].upper() for k in ("family", "side")):
            problems.append(f"{r['label']}: probability row differs from its receipt")
    return problems


def same_number(a, b):
    if str(a) == "" or str(b) == "": return str(a) == str(b)
    try: return math.isfinite(float(a)) and math.isfinite(float(b)) and abs(float(a) - float(b)) <= 1e-9
    except (ValueError, TypeError): return False


def intake(folder, source, *, parent="", root=ROOT, at=None):
    folder, source = Path(folder), Path(source)
    raw = source.read_bytes()
    digest = sha(raw)
    with locked(folder):
        rows = ledger(folder)
        if any(r["return_sha256"] == digest for r in rows):
            return dict(status="ALREADY_EXISTS", return_sha256=digest, problems=[])
        file = "received/" + digest + ".md"
        target = contained(folder, file)
        target.parent.mkdir(exist_ok=True)
        target.write_bytes(raw)  # retain exact originals, even if parsing/admission fails
        try:
            text = raw.decode("utf-8-sig")
            ret = X.parse(text)
            problems = validate_return(ret, text, folder, root=root, at=at)
            h = ret["header"]
        except (ValueError, UnicodeError, KeyError) as exc:
            h, problems = {}, [str(exc)]
        prior = accepted(folder).get(h.get("lane", ""))
        if (folder / "CARD_BINDING.csv").exists(): problems.append("event is frozen by its card binding; use a dated addendum package")
        if prior and parent != prior["return_sha256"]: problems.append("replacement requires the exact accepted parent return hash")
        if parent and not prior: problems.append("replacement parent has no accepted lane")
        r = dict(sequence=str(len(rows) + 1), lane=h.get("lane", "UNKNOWN"), chat_label=h.get("chat_label", "UNKNOWN"),
                 return_sha256=digest, file=file, packet_sha256=h.get("input_package_sha256", ""), parent_sha256=parent,
                 status="REFUSED" if problems else "ACCEPTED", problems=" | ".join(problems), recorded_at=at or now(),
                 prev_sha256=rows[-1]["row_sha256"] if rows else GENESIS)
        r["row_sha256"] = sha("\x1f".join(r[k] for k in INTAKE_FIELDS[:-1]).encode())
        with (folder / "INTAKE.csv").open("ab") as f: f.write(csv_bytes(INTAKE_FIELDS, [r]).split(b"\n", 1)[1])
        return dict(status=r["status"], return_sha256=digest, problems=problems)


def reviews(folder):
    rows = read(Path(folder) / "SOURCE_REVIEW.csv", REVIEW_FIELDS)
    urls = [r["source_url"] for r in rows]
    if len(urls) != len(set(urls)): raise X.ExternalError("duplicate source reviews")
    for r in rows:
        if sha(contained(folder, r["review_evidence_path"]).read_bytes()) != r["review_evidence_sha256"]:
            raise X.ExternalError("source-lineage review bytes changed")
    return rows


def review_source(folder, url, collector, evidence, *, status="UNKNOWN", at=None):
    raw = Path(evidence).read_bytes()
    if Path(evidence).suffix.lower() not in (".txt", ".md", ".csv") or b"<html" in raw[:500].lower():
        raise X.ExternalError("retain sporting-only review text, not raw HTML or binary captures")
    if status not in ("VERIFIED", "UNKNOWN") or not collector:
        raise X.ExternalError("source review needs a collector and VERIFIED/UNKNOWN status")
    with locked(folder):
        if (Path(folder) / "CARD_BINDING.csv").exists(): raise X.ExternalError("event is frozen; source corrections need an addendum package")
        rows = reviews(folder)
        if any(r["source_url"] == url for r in rows): raise X.ExternalError("source review is immutable; create a new versioned event package for correction")
        name = "reviews/" + sha(raw) + ".txt"
        p = contained(folder, name); p.parent.mkdir(exist_ok=True); p.write_bytes(raw)
        r = dict(source_url=url, collector_id=collector, lineage_status=status, review_evidence_path=name,
                 review_evidence_sha256=sha(raw), reviewed_at=at or now())
        with (Path(folder) / "SOURCE_REVIEW.csv").open("ab") as f: f.write(csv_bytes(REVIEW_FIELDS, [r]).split(b"\n", 1)[1])


def admit(folder, *, root=ROOT, at=None):
    with locked(folder):
        return _admit(folder, root=root, at=at)


def _admit(folder, *, root=ROOT, at=None):
    e = load(folder, root)
    acc = accepted(folder)
    expected = {r["lane"] for r in read(Path(folder) / "LANES.csv", LANE_FIELDS)}
    if set(acc) != expected: raise X.ExternalError("missing accepted lanes: " + ",".join(sorted(expected - set(acc))))
    returns = []
    for lane, r in acc.items():
        text = contained(folder, r["file"]).read_text(encoding="utf-8-sig")
        ret = X.parse(text)
        errors = validate_return(ret, text, folder, root=root, at=at)
        if errors: raise X.ExternalError(f"{lane} is stale/refused: {' | '.join(errors)}")
        returns.append(ret)
    source_rows = reviews(folder)
    res = X.merge(returns, e["event_key"], source_reviews=source_rows)
    if res["conflicts"]: raise X.ExternalError("conflicting facts require a new corrected lane return or explicit scenario contract package")
    reqs = read(Path(folder) / "REQUIREMENTS.csv", REQ_FIELDS)
    gaps = []
    for r in reqs:
        if r["required"] != "YES": continue
        facts = [v for v in res["evidence"] if v["side"] == r["side"] and v["field"] == r["field"]]
        if r["lane"] == "L5": continue
        if not facts or (r["corroboration_required"] == "YES" and any(v["corroboration"] != "CORROBORATED" for v in facts)):
            gaps.append(r["requirement_id"])
    if gaps: raise X.ExternalError("information remains incomplete: " + ",".join(gaps))
    res.update(admission="READY_FOR_CARD", manifest_sha256=manifest_hash(folder), input_package_sha256=packet_hash(folder, "L5"),
               admitted_at=at or now(), predictive_qualification="UNPROVEN")
    return res


def bind_card(folder, receipt_path, *, root=ROOT, at=None):
    """Gate an already appended central card through existing card/learning/ledger validators; never issue a second card."""
    from ml import picks, learning_log, ledger as card_ledger
    target = Path(folder) / "CARD_BINDING.csv"
    if target.exists():
        prior = read(target)[0]
        e = read(Path(folder) / "EVENT.csv", EVENT_FIELDS)[0]
        mini = contained(root, e["mini_path"])
        raw = mini.read_bytes()
        begin, end = f"<!-- BEGIN CARD {e['local_key']} -->".encode(), f"<!-- END CARD {e['local_key']} -->".encode()
        if raw.count(begin) != 1 or raw.count(end) != 1: raise X.ExternalError("bound card markers changed")
        block = raw[raw.index(begin):raw.index(end)+len(end)]
        if sha(block) != prior.get("card_block_sha256") or manifest_hash(folder) != prior["manifest_sha256"] or packet_hash(folder, "L5") != prior["input_package_sha256"]:
            raise X.ExternalError("bound card or package changed; retain a dated addendum")
        return prior
    res = admit(folder, root=root, at=at)
    e = load(folder, root)
    mini = contained(root, e["mini_path"])
    meta, rows, problems = picks.lint_card(mini, e["local_key"], root=root)
    if problems: raise X.ExternalError("card lint: " + " | ".join(problems))
    if meta.get("event_key") != e["event_key"] or meta.get("competition") != e["competition"] or meta.get("scheduled_start") != e["scheduled_start"]:
        raise X.ExternalError("final card identity differs from its admitted event manifest")
    expected = {r["label"]: r for r in read(Path(folder) / "CONTRACTS.csv", CONTRACT_FIELDS)}
    if meta.get("external_manifest_sha256") != res["manifest_sha256"] or meta.get("external_packet_sha256") != res["input_package_sha256"]:
        raise X.ExternalError("card does not name its exact admitted manifest and final input package")
    definitions = "|".join(c["label"] + "=" + "~".join(c[k] for k in ("period", "endpoint", "action", "unit")) for c in expected.values())
    if meta.get("contract_definitions") != definitions:
        raise X.ExternalError("final card endpoint/period/action/unit definitions differ from manifest")
    if {r["label"] for r in rows} != set(expected): raise X.ExternalError("final card contract coverage differs from admitted package")
    for r in rows:
        c = expected[r["label"]]
        if r["family"].lower() != c["family"].lower() or r["side"].upper() != c["side"].upper() or not same_number(r["line"], c["line"]):
            raise X.ExternalError("final card contract differs from admitted package")
    from ml.kit import sr_kit as K
    receipt_text = Path(receipt_path).read_text(encoding="utf-8")
    pricing = {"PROBABILITIES": [{k: str(r[k]).lower() if k == "family" else str(r[k]) for k in ("label", "family", "side", "line", "w", "p", "l", "final_p")}
                                for r in rows]}
    for r in pricing["PROBABILITIES"]: r["kit_receipt_sha256"] = K.receipt_sha256(receipt_text)
    errors = verify_prices(pricing, receipt_text, folder, root)
    if errors: raise X.ExternalError("central pricing receipt: " + " | ".join(errors))
    errors = learning_log.check(e["local_key"], "pregame", root=root)
    if errors: raise X.ExternalError("learning log: " + " | ".join(errors))
    card = card_ledger._card_text(mini, e["local_key"])
    errors = card_ledger.check_adjustments(card_ledger.parse_adjustments(card, e["local_key"]), meta, rows, root=root)
    if errors: raise X.ExternalError("card adjustments: " + " | ".join(errors))
    saved_rows = card_ledger.read(Path(root) / card_ledger.LEDGER)
    saved_rows = saved_rows[saved_rows.local_key == e["local_key"]]
    if len(saved_rows) != len(rows) or set(saved_rows.label) != set(expected):
        raise X.ExternalError("card must be ledgered exactly once before its external binding")
    for r in rows:
        saved = saved_rows[saved_rows.label == r["label"]].iloc[0]
        if not same_number(saved.final_p, r["final_p"]): raise X.ExternalError("card probability differs from its frozen ledger")
    raw = mini.read_bytes()
    begin, end = f"<!-- BEGIN CARD {e['local_key']} -->".encode(), f"<!-- END CARD {e['local_key']} -->".encode()
    block = raw[raw.index(begin):raw.index(end)+len(end)]
    receipt = dict(event_key=e["event_key"], local_key=e["local_key"], manifest_sha256=res["manifest_sha256"],
                   input_package_sha256=res["input_package_sha256"], mini_sha256=sha(mini.read_bytes()),
                   card_block_sha256=sha(block), bound_at=at or now(), status="CARD_BOUND_NOT_PUBLICATION_PROOF")
    if target.exists():
        prior = read(target)[0]
        if any(prior[k] != receipt[k] for k in receipt if k != "bound_at"):
            raise X.ExternalError("card binding is immutable; corrections need a dated addendum")
        return prior
    if packet_hash(folder, "L5") != res["input_package_sha256"]: raise X.ExternalError("input package changed during card binding")
    if not target.exists(): target.write_bytes(csv_bytes(tuple(receipt), [receipt]))
    return receipt


def append_card(folder, card_path, receipt_path, expected_mini_sha256, writer, *, root=ROOT, at=None, research_only=None):
    """Lease-held, compare-before-write mini append. Existing bytes before the footer are preserved exactly."""
    import os
    import tempfile
    from ml import picks
    e = load(folder, root)
    if research_only not in (None, "NO_FORECAST", "QUALITATIVE"): raise X.ExternalError("invalid research retention disposition")
    res = admit(folder, root=root, at=at) if research_only is None else dict(manifest_sha256=manifest_hash(folder), input_package_sha256="NOT_ADMITTED")
    if writer != e["writer"]: raise X.ExternalError("only the manifest writer may append")
    mini, card = contained(root, e["mini_path"]), Path(card_path).read_bytes()
    text = card.decode("utf-8")
    begin, end = f"<!-- BEGIN CARD {e['local_key']} -->", f"<!-- END CARD {e['local_key']} -->"
    if text.count(begin) != 1 or text.count(end) != 1 or any(not re.search(rf"\bA{i}\b", text) for i in range(1, 10)):
        raise X.ExternalError("complete unique card markers and A1-A9 appendix required")
    if research_only:
        if "BEGIN PICKS_V2" in text or f"<!-- RESEARCH_STATUS: {research_only} -->" not in text:
            raise X.ExternalError("research-only retention needs its explicit status and cannot carry a priced PICKS_V2 block")
        if any(v not in text for v in (e["event_key"], e["competition"], e["scheduled_start"])):
            raise X.ExternalError("research-only record must state event key, competition and scheduled start")
    else:
        meta, priced = picks.parse(picks.block(text, e["local_key"]))
        errors = picks.lint(meta, priced, root=root)
        if errors: raise X.ExternalError("candidate card: " + " | ".join(errors))
        if meta.get("external_manifest_sha256") != res["manifest_sha256"] or meta.get("external_packet_sha256") != res["input_package_sha256"]:
            raise X.ExternalError("candidate does not bind the admitted package")
        if meta.get("event_key") != e["event_key"] or meta.get("competition") != e["competition"] or meta.get("scheduled_start") != e["scheduled_start"]:
            raise X.ExternalError("candidate event identity differs from the manifest")
        contracts = read(Path(folder) / "CONTRACTS.csv", CONTRACT_FIELDS)
        definitions = "|".join(c["label"] + "=" + "~".join(c[k] for k in ("period", "endpoint", "action", "unit")) for c in contracts)
        if meta.get("contract_definitions") != definitions: raise X.ExternalError("candidate endpoint/action definitions differ from manifest")
        from ml.kit import sr_kit as K
        rec = Path(receipt_path).read_text(encoding="utf-8")
        probs = [{k: str(r[k]).lower() if k == "family" else str(r[k]) for k in ("label", "family", "side", "line", "w", "p", "l", "final_p")} for r in priced]
        for r in probs: r["kit_receipt_sha256"] = K.receipt_sha256(rec)
        errors = verify_prices({"PROBABILITIES": probs}, rec, folder, root)
        if errors: raise X.ExternalError("candidate pricing: " + " | ".join(errors))
    with locked(mini.parent):
        original = mini.read_bytes()
        if sha(original) != expected_mini_sha256: raise X.ExternalError("mini changed since read")
        prior = original.decode("utf-8")
        if begin in prior:
            if prior[prior.index(begin):prior.index(end)+len(end)].strip() == text.strip():
                return dict(status="ALREADY_EXISTS", local_key=e["local_key"])
            raise X.ExternalError("existing card is immutable; use an addendum")
        lease_rows = [line for line in prior.splitlines() if re.search(r"^\|[^|]*writer[^|]*lease[^|]*\|", line, re.I)]
        lease_lines = lease_rows[-1] if lease_rows else ""
        leases = re.findall(r"(?:expires|extended to)\s*([0-9T:+.Z-]+)", lease_lines, re.I)
        if writer not in lease_lines or not leases or max(clock(v) for v in leases) <= clock(at or now()):
            raise X.ExternalError("mini lease absent, expired or held by another writer")
        marker = b"<!-- BEGIN FOOTER -->"
        if original.count(marker) != 1 or original.count(b"<!-- END FOOTER -->") != 1:
            raise X.ExternalError("mini needs exactly one complete footer")
        prefix, tail = original.split(marker)
        ft = tail.decode("utf-8")
        frozen_rows = [line for line in prior.splitlines() if re.search(r"^\| Frozen for settlement \|", line, re.I)]
        if frozen_rows and re.search(r"\| YES\s*\|", frozen_rows[-1], re.I): raise X.ExternalError("mini is frozen for settlement")
        if re.search(r"\| Mini status \|[^\n]*(FROZEN|CLOSED)", ft, re.I): raise X.ExternalError("mini is frozen")
        keyrow = next((line for line in ft.splitlines() if "Last local event key / next local event key" in line), "")
        keys = re.findall(r"`([^`]+)`", keyrow)
        if len(keys) != 2 or keys[-1] != e["local_key"]: raise X.ExternalError("mini next key differs from manifest")
        stem, ordinal = e["local_key"].rsplit("G", 1)
        next_key = stem + "G" + str(int(ordinal)+1).zfill(len(ordinal))
        ft = ft.replace(keyrow, f"| Last local event key / next local event key | `{e['local_key']}` / `{next_key}` |")
        def bump(m):
            counts = [int(m.group(i)) for i in range(2, 6)]
            counts[0] += 1; counts[1 if not research_only else 2 if research_only == "QUALITATIVE" else 3] += 1
            return m.group(1) + " / ".join(map(str, counts))
        ft, count = re.subn(r"(\| New cards / numeric / qualitative / NO_FORECAST \|\s*)(\d+)\s*/\s*(\d+)\s*/\s*(\d+)\s*/\s*(\d+)", bump, ft)
        if count != 1: raise X.ExternalError("unambiguous mini counts required")
        ft = ft.replace("ACTIVE / EMPTY", "ACTIVE")
        nl = b"\r\n" if b"\r\n" in original else b"\n"
        addition = f"\n<!-- EXT-v2 INTAKE {e['local_key']} manifest={res['manifest_sha256']} -->\n".encode() + card + b"\n"
        addition = addition.replace(b"\r\n", b"\n").replace(b"\n", nl)
        updated = prefix + addition + marker + ft.replace("\r\n", "\n").replace("\n", nl.decode()).encode()
        with tempfile.NamedTemporaryFile(dir=mini.parent, prefix=".mini-append-", suffix=".txt", delete=False) as f:
            temp = Path(f.name); f.write(updated)
        try:
            if sha(mini.read_bytes()) != expected_mini_sha256: raise X.ExternalError("mini changed immediately before write")
            os.replace(temp, mini)
        finally:
            if temp.exists(): temp.unlink()
        if mini.read_bytes() != updated or not updated.startswith(prefix): raise X.ExternalError("mini readback/prefix verification failed")
        receipt = dict(status="RETAINED_" + research_only + "_NOT_ISSUED" if research_only else "APPENDED_NOT_YET_FROZEN", local_key=e["local_key"], before_sha256=sha(original), after_sha256=sha(updated),
                       preserved_prefix_bytes=str(len(prefix)), next_local_key=next_key, canonical_ids_assigned="0")
        (Path(folder) / "APPEND_RECEIPT.csv").write_bytes(csv_bytes(tuple(receipt), [receipt]))
        return receipt


def package_check(root=ROOT):
    root = Path(root)
    paths = ["ml/kit/sr_kit.py", "research/external/EXTERNAL_PROFILE_v24.14.md", "research/external/LANE_BRIEFS_v24.14.md",
             "research/external/kit/KIT_PARAMETERS_v24.14.csv", "research/external/kit/KIT_CRICKET_PHASES_v24.14.csv",
             "research/external/access/READER_ACCESS_v24.14.csv", "research/external/access/CHATGPT_DO_NOT_OPEN_v24.14.csv"]
    missing = [p for p in paths if not (root / p).is_file()]
    if missing: raise X.ExternalError("incomplete release package: " + ",".join(missing))
    from ml.kit import sr_kit as K
    K.load_params(root / paths[3])
    phases = read(root / paths[4])
    if not phases or any(r.get("kit_version") != K.KIT_VERSION for r in phases):
        raise X.ExternalError("phase package is empty or has a different kit version")
    access = read(root / paths[5])
    if not access or any(not X._time_ok(r.get("valid_until", "")) or clock(r["valid_until"]) <= clock(now()) for r in access):
        raise X.ExternalError("reader-access package is empty or expired; refresh before research")
    return [dict(path=p, sha256=sha((root / p).read_bytes())) for p in paths]


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    i = sub.add_parser("init")
    i.add_argument("--event-csv", type=Path, required=True); i.add_argument("--contracts", type=Path, required=True)
    i.add_argument("--requirements", type=Path, required=True); i.add_argument("--artifacts", type=Path, required=True)
    i.add_argument("--out", type=Path, required=True)
    for command in ("packet", "intake", "status", "admit", "bind-card", "append-card", "append-research", "review-source"):
        a = sub.add_parser(command); a.add_argument("--event", type=Path, required=True)
        if command == "packet": a.add_argument("--lane", required=True)
        if command == "intake": a.add_argument("--return", dest="source", type=Path, required=True); a.add_argument("--parent", default="")
        if command == "bind-card": a.add_argument("--receipt", type=Path, required=True)
        if command == "append-card":
            a.add_argument("--card", type=Path, required=True); a.add_argument("--receipt", type=Path, required=True)
            a.add_argument("--expected-mini-sha256", required=True); a.add_argument("--writer", required=True)
        if command == "append-research":
            a.add_argument("--card", type=Path, required=True); a.add_argument("--disposition", choices=("NO_FORECAST", "QUALITATIVE"), required=True)
            a.add_argument("--expected-mini-sha256", required=True); a.add_argument("--writer", required=True)
        if command == "review-source":
            a.add_argument("--url", required=True); a.add_argument("--collector", required=True); a.add_argument("--evidence", type=Path, required=True)
            a.add_argument("--status", choices=("VERIFIED", "UNKNOWN"), default="UNKNOWN")
    sub.add_parser("package-check")
    ev = sub.add_parser("evaluate"); ev.add_argument("--forecasts", type=Path, required=True); ev.add_argument("--outcomes", type=Path, required=True)
    ev.add_argument("--out", type=Path, required=True)
    args = p.parse_args(argv)
    try:
        if args.command == "init":
            print(initialize(read(args.event_csv)[0], read(args.contracts, CONTRACT_FIELDS), read(args.requirements, REQ_FIELDS), args.out,
                             artifacts={r["role"]: r["path"] for r in read(args.artifacts)}))
        elif args.command == "packet":
            load(args.event); print("manifest_sha256:", manifest_hash(args.event)); print("input_package_sha256:", packet_hash(args.event, args.lane))
            print("Dependencies are the exact accepted originals under this event's received/ folder; pricing uses the reviewed merged evidence.")
        elif args.command == "intake":
            result = intake(args.event, args.source, parent=args.parent); print(result)
            if result["status"] == "REFUSED": raise SystemExit(1)
        elif args.command == "status":
            load(args.event)
            for r in read(args.event / "LANES.csv", LANE_FIELDS):
                try:
                    current = packet_hash(args.event, r["lane"])
                    saved = accepted(args.event).get(r["lane"], {})
                    status = "STALE" if saved and saved["packet_sha256"] != current else saved.get("status", "AWAITING_RETURN")
                    print(r["lane"], status, current)
                except X.ExternalError as exc: print(r["lane"], "BLOCKED_OR_STALE", str(exc))
        elif args.command == "review-source": review_source(args.event, args.url, args.collector, args.evidence, status=args.status)
        elif args.command == "admit":
            result = admit(args.event)
            output = args.event / ("ADMISSION_" + sha(str(result["inputs"]).encode())[:16] + ".csv")
            receipt = {k: result[k] for k in ("event_key", "admission", "manifest_sha256", "input_package_sha256", "admitted_at", "predictive_qualification")}
            if output.exists():
                prior = read(output)[0]
                if any(str(receipt[k]) != prior.get(k) for k in receipt if k != "admitted_at"):
                    raise X.ExternalError("admission receipt collision; preserve both versions")
                print("ALREADY_EXISTS", prior); return
            output.write_bytes(csv_bytes(tuple(receipt), [receipt])); print(receipt)
        elif args.command == "bind-card": print(bind_card(args.event, args.receipt))
        elif args.command == "append-card": print(append_card(args.event, args.card, args.receipt, args.expected_mini_sha256, args.writer))
        elif args.command == "append-research": print(append_card(args.event, args.card, None, args.expected_mini_sha256, args.writer, research_only=args.disposition))
        elif args.command == "package-check": print(package_check())
        elif args.command == "evaluate":
            from ml.external_evaluation import evaluate
            print(evaluate(args.forecasts, args.outcomes, args.out))
    except (X.ExternalError, ValueError, OSError, KeyError) as exc:
        print(f"REFUSED: {exc}"); raise SystemExit(2)
