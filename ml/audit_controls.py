"""AUDIT-v1: contract review and hash-verified chat handovers; no predictive adjustments."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

VERSION = "AUDIT-v1"
FROM = "2026-11-15T00:00:00+11:00"
FIELDS = ("label", "sport", "competition", "event_date", "native_event_id", "game_number", "home", "away",
          "scheduled_start", "schedule_url", "schedule_checked_at", "method_id", "method_status", "method_evidence", "method_evidence_sha256",
          "sample_n", "sample_coverage", "uncertainty", "opponent_check", "opponent_evidence", "opponent_evidence_sha256",
          "availability_status", "availability_evidence", "availability_evidence_sha256", "availability_effect_id", "availability_effect_version",
          "p_with", "p_without", "reason")
HANDOVER_FIELDS = ("path", "bytes", "sha256", "role", "mini_key", "writer", "card_keys", "recorded_at")


def clock(value):
    t = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if t.utcoffset() is None:
        raise ValueError("offset-aware timestamp required")
    return t


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def contained(base, name):
    base = Path(base).resolve()
    path = (base / name).resolve()
    if not path.is_relative_to(base) or path == base:
        raise ValueError("path escapes the declared base")
    return path


def read(path, fields):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if tuple(reader.fieldnames or ()) != fields:
            raise ValueError("CSV columns must be exactly: " + ",".join(fields))
        rows = list(reader)
    if any(set(r) != set(fields) or any(v is None for v in r.values()) for r in rows):
        raise ValueError("malformed CSV row")
    return rows


def csv_bytes(fields, rows):
    out = io.StringIO(newline="")
    w = csv.DictWriter(out, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return out.getvalue().encode("utf-8")


def required(meta):
    if any(meta.get(k) for k in ("audit_policy", "audit_event_key", "audit_review", "audit_review_sha256")):
        return True
    try:
        return clock(meta["issued_at"]) >= clock(FROM)
    except (ValueError, KeyError):
        return False  # The PICKS checker separately rejects missing/malformed clocks.


def problems(meta, picks, root):
    """Validate a bound review for newly issued numeric cards; historical cards stay unchanged.

    This verifies declarations, custody and scope. It cannot certify that a human's
    evidence establishes an effect, source independence or calibration.
    """
    if not required(meta):
        return []
    errors = []
    if meta.get("audit_policy") != VERSION:
        return ["AUDIT-v1: new cards require audit_policy: AUDIT-v1 and a hash-bound contract review"]
    try:
        path = contained(root, meta.get("audit_review", ""))
        raw = path.read_bytes()
        if digest(raw) != meta.get("audit_review_sha256"):
            raise ValueError("contract review SHA-256 mismatch")
        reviews = read(path, FIELDS)
    except (ValueError, OSError) as exc:
        return ["AUDIT-v1: " + str(exc)]
    labels = [r["label"] for r in reviews]
    expected = {r["label"] for r in picks}
    if len(labels) != len(set(labels)) or set(labels) != expected:
        return ["AUDIT-v1: exactly one review per numeric PICKS label required"]
    if not reviews:
        return ["AUDIT-v1: contract review is empty"]
    identity_fields = FIELDS[1:11]
    if len({tuple(r[k] for k in identity_fields) for r in reviews}) != 1:
        errors.append("AUDIT-v1: all contract rows must identify the same exact event and schedule observation")
    by_label = {r["label"]: r for r in picks}
    for r in reviews:
        prefix = "AUDIT-v1 " + r["label"] + ": "
        for field in FIELDS:
            if field not in ("game_number", "p_with", "p_without", "opponent_evidence_sha256", "availability_effect_id", "availability_effect_version") and not r[field].strip():
                errors.append(prefix + "missing " + field)
        try:
            start, checked = clock(r["scheduled_start"]), clock(r["schedule_checked_at"])
            if start != clock(meta["scheduled_start"]) or checked > clock(meta["issued_at"]):
                errors.append(prefix + "schedule differs from card or observation is after issue")
            if r["event_date"] != start.date().isoformat():
                errors.append(prefix + "event_date must match the date in scheduled_start's stated offset")
            from ml.external import event_key
            key = event_key(r["sport"], r["event_date"], r["home"], r["away"], competition=r["competition"],
                            native_event_id=r["native_event_id"], game_number=r["game_number"])
            if meta.get("audit_event_key") != key or (meta.get("event_key", "").startswith("EV2-") and meta["event_key"] != key) or r["competition"] != meta["competition"]:
                errors.append(prefix + "native fixture identity/competition differs from card event_key")
        except (ValueError, KeyError) as exc:
            errors.append(prefix + "invalid identity/clock: " + str(exc))
        if urlparse(r["schedule_url"]).scheme not in ("http", "https") or not urlparse(r["schedule_url"]).hostname:
            errors.append(prefix + "official schedule URL required")
        if r["native_event_id"] in ("UNKNOWN", "UNAVAILABLE", "NOT_VERIFIED"):
            errors.append(prefix + "unresolved native fixture identity cannot support a numeric card")
        if r["method_status"] != "SUPPORTED_REFERENCE" or re.search(r"(?<![0-9])v?4[._]12(?![0-9])", r["method_id"], re.I):
            errors.append(prefix + "legacy/uncalibrated scenarios cannot supply primary probabilities; retain separately")
        if meta.get("reference_status") not in ("EXECUTED", "BASELINE_ONLY"):
            errors.append(prefix + "SUPPORTED_REFERENCE requires an executed reference or league baseline")
        # Evidence is a retained review of the exact method/scope, not an invented certification flag.
        try:
            evidence = contained(root, r["method_evidence"])
            if not evidence.is_file() or not evidence.stat().st_size or digest(evidence.read_bytes()) != r["method_evidence_sha256"]:
                raise ValueError("missing method/scope evidence")
        except (OSError, ValueError) as exc:
            errors.append(prefix + str(exc))
        if not re.fullmatch(r"[1-9][0-9]*", r["sample_n"]):
            errors.append(prefix + "sample_n must be a positive actual observation count, not simulation draws")
        try:
            coverage = float(r["sample_coverage"])
            if not math.isfinite(coverage) or not 0 < coverage <= 1:
                raise ValueError()
        except ValueError:
            errors.append(prefix + "sample_coverage must be a measured fraction in (0,1]")
        pick = by_label[r["label"]]
        try:
            plus = pick["family"] == "HANDICAP" and float(pick["line"]) > 0
        except (ValueError, KeyError):
            plus = False
        if r["opponent_check"] not in ("CHECKED", "UNAVAILABLE", "NOT_APPLICABLE"):
            errors.append(prefix + "invalid opponent_check")
        if plus and r["opponent_check"] != "CHECKED":
            errors.append(prefix + "plus-handicap pricing requires an opponent-strength check; otherwise leave UNPRICED")
        for kind in (("opponent",) if plus else ()) + ("availability",):
            try:
                evidence = contained(root, r[kind + "_evidence"])
                if not evidence.is_file() or not evidence.stat().st_size or digest(evidence.read_bytes()) != r[kind + "_evidence_sha256"]:
                    raise ValueError("missing or changed " + kind + " evidence")
            except (OSError, ValueError) as exc:
                errors.append(prefix + str(exc))
        if r["availability_status"] not in ("NO_MATERIAL_CHANGE_IDENTIFIED", "MEASURED", "UNQUANTIFIED", "SCENARIO_ONLY"):
            errors.append(prefix + "invalid availability_status")
        if r["availability_status"] in ("UNQUANTIFIED", "SCENARIO_ONLY"):
            errors.append(prefix + "material unmeasured availability requires UNPRICED; keep assumptions as sensitivity only")
        if r["availability_status"] == "MEASURED":
            try:
                from ml import ledger as L
                effect = L.effect_rows(root).get(r["availability_effect_id"])
                if not effect or r["availability_effect_id"] in L.superseded(root):
                    raise ValueError("availability effect is missing or superseded")
                if effect["version"] != r["availability_effect_version"] or effect["competition"] != meta["competition"]:
                    raise ValueError("availability effect version/competition mismatch")
                if effect["status"] not in ("MEASURED_CONFIRMED", "MEASURED_NOT_CONFIRMED") or not re.search(r"player|lineup|availability|injur|roster", effect["factor"], re.I):
                    raise ValueError("effect is not an admitted measured availability effect")
                targets = {"MARGIN": ("margin",), "TOTAL": ("total",), "TEAM_TOTAL": ("team",), "PERIOD": ("period",), "COUNT": ("count", "corner")}
                if not any(word in effect["target"].lower() for word in targets.get(pick.get("quantity"), ())):
                    raise ValueError("availability effect target does not match contract")
            except (OSError, ValueError) as exc:
                errors.append(prefix + str(exc))
            for k in ("p_with", "p_without"):
                try:
                    value = float(r[k])
                    if not math.isfinite(value) or not 0 <= value <= 1:
                        raise ValueError()
                except ValueError:
                    errors.append(prefix + "MEASURED availability requires exact-contract " + k + " in [0,1]")
        elif r["p_with"] or r["p_without"]:
            errors.append(prefix + "player probabilities require MEASURED status and effect evidence")
    return errors


def mini_keys(path, mini_key):
    text = Path(path).read_text(encoding="utf-8-sig")
    if not re.fullmatch(r"[A-Z0-9]+", mini_key):
        raise ValueError("MINI_KEY must contain uppercase ASCII letters/digits")
    if text.count("MINI-LOG-FORMAT:") != 1 or "<!-- MINI-LOG-FORMAT: mini-log-10 -->" not in text:
        raise ValueError("new handovers require one mini-log-10 format marker")
    markers = re.findall(r"<!-- (BEGIN|END) CARD ([^\r\n]*?) -->", text)
    if len(markers) != len(re.findall(r"<!--\s*(?:BEGIN|END)\s+CARD\b", text)):
        raise ValueError("malformed card markers")
    active, keys = None, []
    for action, key in markers:
        m = re.fullmatch(r"LOCAL-" + re.escape(mini_key) + r"-G([0-9]{4,})", key)
        if not m or int(m[1]) == 0:
            raise ValueError("foreign namespace or canonical ID in new mini")
        if action == "BEGIN":
            if active or key in keys:
                raise ValueError("duplicate/nested card")
            active = key
            keys.append(key)
        elif active != key:
            raise ValueError("orphaned or mismatched card end")
        else:
            active = None
    if active:
        raise ValueError("unfinished final card")
    if not keys:
        raise ValueError("final mini has no marked cards; scripts cannot substitute for missing originals")
    return keys


def handover(base, mini, mini_key, writer, files, out):
    base = Path(base).resolve()
    if not writer.strip():
        raise ValueError("one declared mini writer required")
    source = contained(base, mini)
    keys = mini_keys(source, mini_key)
    paths = [source] + [contained(base, f) for f in files]
    if len(paths) != len(set(paths)) or Path(out).resolve() in paths:
        raise ValueError("duplicate member or output listed as input")
    rows = []
    for path in paths:
        raw = path.read_bytes()
        rows.append(dict(path=path.relative_to(base).as_posix(), bytes=str(len(raw)), sha256=digest(raw),
                         role="FINAL_MINI" if path == source else "ASSOCIATED", mini_key=mini_key, writer=writer,
                         card_keys="|".join(keys) if path == source else "", recorded_at=datetime.now(timezone.utc).isoformat()))
    # Read every input before creating output; never overwrite an earlier handover.
    with Path(out).open("xb") as f:
        f.write(csv_bytes(HANDOVER_FIELDS, rows))
    return dict(files=len(rows), cards=len(keys), mini_key=mini_key, publication_proof="NO")


def verify_handover(base, manifest):
    rows = read(manifest, HANDOVER_FIELDS)
    if not rows or len({r["path"] for r in rows}) != len(rows):
        raise ValueError("empty/duplicate handover members")
    minis = [r for r in rows if r["role"] == "FINAL_MINI"]
    if len(minis) != 1 or any(r["role"] not in ("FINAL_MINI", "ASSOCIATED") for r in rows):
        raise ValueError("exactly one final mini required")
    if len({(r["mini_key"], r["writer"]) for r in rows}) != 1 or not minis[0]["writer"].strip():
        raise ValueError("handover namespace/writer mismatch")
    for r in rows:
        raw = contained(base, r["path"]).read_bytes()
        if str(len(raw)) != r["bytes"] or digest(raw) != r["sha256"]:
            raise ValueError("missing or changed handover member: " + r["path"])
    m = minis[0]
    keys = mini_keys(contained(base, m["path"]), m["mini_key"])
    if "|".join(keys) != m["card_keys"]:
        raise ValueError("handover card inventory mismatch")
    return dict(files=len(rows), cards=len(keys), mini_key=m["mini_key"], publication_proof="NO")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    a = sub.add_parser("template")
    a.add_argument("--mini", type=Path, required=True); a.add_argument("--key", required=True)
    a.add_argument("--out", type=Path, required=True)
    a = sub.add_parser("handover")
    a.add_argument("--base", type=Path, required=True); a.add_argument("--mini", required=True)
    a.add_argument("--mini-key", required=True); a.add_argument("--writer", required=True)
    a.add_argument("--files", nargs="*", default=[]); a.add_argument("--out", type=Path, required=True)
    a = sub.add_parser("verify-handover")
    a.add_argument("--base", type=Path, required=True); a.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "template":
            from ml import picks
            text = args.mini.read_text(encoding="utf-8")
            meta, priced = picks.parse(picks.block(text, args.key))
            rows = []
            for pick in priced:
                row = dict.fromkeys(FIELDS, "")
                row.update(label=pick["label"], competition=meta.get("competition", ""), scheduled_start=meta.get("scheduled_start", ""))
                rows.append(row)
            with args.out.open("xb") as f:
                f.write(csv_bytes(FIELDS, rows))
            print("DRAFT_ONLY: fill missing evidence; template is not an admission or forecast")
        elif args.command == "handover":
            print(handover(args.base, args.mini, args.mini_key, args.writer, args.files, args.out))
        else:
            print(verify_handover(args.base, args.manifest))
    except (ValueError, OSError) as exc:
        parser.exit(2, "REFUSED: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
