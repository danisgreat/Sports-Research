"""Kit commands (KIT-v1, CR-2026.11.11-R1).

    python -m ml kit verify --receipt FILE [--params FILE] [--phases FILE]   re-run a chat's KIT_RECEIPT with the repository kit
    python -m ml kit params --soccer-study DIR --sim-checks DIR [--out DIR]  rebuild the kit's parameter files (ml.kit.params)
    python -m ml kit sha                                                     print the kit's own SHA-256 (what a receipt must show)

A receipt is accepted only when its kit version is the repository's, its parameter-file hash matches the committed file
of that version, and every probability reproduces: exact engines to 1e-9, a simulation (same seed and N) to 3 Monte Carlo
standard errors. Anything else is REFUSED with the reason, and the chat's numbers are not used.
"""
from __future__ import annotations

import argparse
import ast
import csv
import io
import math
import re
from pathlib import Path

from ml.kit import sr_kit as K

ROOT = Path(__file__).resolve().parents[2]
KIT_DIR = ROOT / "research" / "external" / "kit"
VERSION = K.KIT_VERSION.split("-")[-1]


def parse_receipt(text: str) -> dict:
    matches = list(re.finditer(r"<!-- BEGIN KIT_RECEIPT (\S+) -->(.*?)<!-- END KIT_RECEIPT \1 -->", text, re.S))
    if len(matches) != 1:
        raise K.KitError("no complete KIT_RECEIPT block")
    m = matches[0]
    head, rows, inputs, in_rows = {}, [], {}, False
    for ln in m.group(2).strip().splitlines():
        if ln.strip() == "rows:":
            in_rows = True
            continue
        if in_rows:
            rows.append(ln)
            continue
        name, _, value = ln.partition(": ")
        if name in head or (name.startswith("input.") and name[6:] in inputs):
            raise K.KitError(f"duplicate receipt field {name}")
        if name.startswith("input."):
            try:
                inputs[name[6:]] = ast.literal_eval(value)
            except (ValueError, SyntaxError):
                inputs[name[6:]] = value
        else:
            head[name] = value
    if not rows:
        raise K.KitError("receipt is missing output columns and rows")
    reader = csv.DictReader(io.StringIO("\n".join(rows)))
    required = ("label", "family", "side", "line", "w", "p", "l", "final_p")
    if tuple(reader.fieldnames or ()) not in (required, required + ("mc_se",)):
        raise K.KitError("receipt has an invalid output schema")
    table = list(reader)
    if not table or any(None in r or any(v is None for v in r.values()) for r in table):
        raise K.KitError("receipt must contain complete output rows")
    return dict(engine=m.group(1), head=head, inputs=inputs, rows=table)


def verify(text: str, params: Path | None = None, phases: Path | None = None) -> list[str]:
    rec = parse_receipt(text)
    problems = []
    if rec["head"].get("kit_version") != K.KIT_VERSION:
        return [f"kit_version {rec['head'].get('kit_version')} is not the repository's {K.KIT_VERSION}"]
    if rec["head"].get("kit_sha256") != K.file_sha256():
        problems.append("kit_sha256 differs from the repository kit: the chat ran an edited or older file (result re-run with the repository kit)")
    params = params or KIT_DIR / f"KIT_PARAMETERS_{VERSION}.csv"
    phases = phases or KIT_DIR / f"KIT_CRICKET_PHASES_{VERSION}.csv"
    used_params = rec["engine"] in ("points_from_centre", "soccer_from_means", "hockey_from_means", "baseball_from_means")
    used_phases = rec["engine"] == "cricket_innings"
    for field, path, used in (("params_sha256", params, used_params), ("phases_sha256", phases, used_phases)):
        expected = K.file_sha256(path) if used else "NOT_USED"
        if rec["head"].get(field) != expected:
            problems.append(f"{field} differs from the required artifact (NOT_USED cannot bypass a required hash)")
    if problems:
        return problems
    result, _ = K.run(rec["engine"], rec["inputs"], params_path=params, phases_path=phases)
    for field, expected in (("purpose", rec["inputs"].get("purpose", "PRIMARY")),
                            ("qualification", result.get("qualification", "MATHEMATICAL_ARITHMETIC_NOT_CALIBRATION")),
                            ("parameter_basis", result.get("parameter_basis", "CALLER_INPUTS"))):
        if rec["head"].get(field) != expected: problems.append(f"{field} differs from the trusted re-run")
    mine = {r["label"]: r for r in result["rows"]}
    labels = [r["label"] for r in rec["rows"]]
    if len(labels) != len(set(labels)) or set(labels) != set(mine) or len(mine) != len(result["rows"]):
        problems.append("receipt outputs must cover exactly the re-run contracts once each")
    for r in rec["rows"]:
        if r["label"] not in mine:
            problems.append(f"{r['label']}: not produced by the re-run")
            continue
        got = mine[r["label"]]
        for k in ("family", "side"):
            if r[k].upper() != str(got[k]).upper(): problems.append(f"{r['label']}: {k} differs from the re-run contract")
        if str(r["line"]) != str(got["line"]):
            try:
                if not math.isfinite(float(r["line"])) or abs(float(r["line"]) - float(got["line"])) > 1e-9: raise ValueError()
            except (ValueError, TypeError): problems.append(f"{r['label']}: line differs from the re-run contract")
        se = float(got.get("mc_se") or 0)
        if not math.isfinite(se) or se < 0: problems.append(f"{r['label']}: invalid trusted Monte Carlo error"); continue
        if "mc_se" in r:
            try:
                supplied_se = float(r["mc_se"])
                if not math.isfinite(supplied_se) or abs(supplied_se - se) > 1e-9: raise ValueError()
            except ValueError: problems.append(f"{r['label']}: Monte Carlo error must match the trusted re-run")
        elif se:
            problems.append(f"{r['label']}: missing Monte Carlo error")
        tol = 3 * se if se else 1e-9
        for k in ("w", "p", "l", "final_p"):
            try:
                value = float(r[k])
                if not math.isfinite(value) or not 0 <= value <= 1: raise ValueError()
            except ValueError:
                problems.append(f"{r['label']}: {k} must be finite in [0,1]"); continue
            if not math.isfinite(got[k]) or abs(value - got[k]) > max(tol, 1e-9):
                problems.append(f"{r['label']}: {k} {r[k]} does not reproduce ({got[k]:.10f}, tolerance {tol:.2e})")
        try:
            w, push, loss, final = (float(r[k]) for k in ("w", "p", "l", "final_p"))
            if abs(w + push + loss - 1) > 1e-8 or w + loss <= 0 or abs(final - w / (w + loss)) > 1e-8:
                problems.append(f"{r['label']}: submitted W/P/L and decisive probability are incoherent")
        except (ValueError, ZeroDivisionError):
            problems.append(f"{r['label']}: invalid submitted probability masses")
    return problems


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    v = sub.add_parser("verify")
    v.add_argument("--receipt", type=Path, required=True)
    v.add_argument("--params", type=Path)
    v.add_argument("--phases", type=Path)
    sub.add_parser("sha")
    p = sub.add_parser("params")
    p.add_argument("--soccer-study", type=Path, required=True)
    p.add_argument("--sim-checks", type=Path, required=True)
    p.add_argument("--out", type=Path, default=KIT_DIR)
    p.add_argument("--version", default=VERSION)
    args = parser.parse_args(argv)
    if args.command == "sha":
        print(K.KIT_VERSION, K.file_sha256())
        return
    if args.command == "params":
        from ml.kit import params as P
        print(P.build(args.soccer_study, args.sim_checks, args.out, args.version))
        return
    try:
        problems = verify(args.receipt.read_text(encoding="utf-8"), args.params, args.phases)
    except K.KitError as exc:
        print(f"REFUSED: {exc}")
        raise SystemExit(2)
    if problems:
        print(f"KIT_RECEIPT NOT ACCEPTED ({len(problems)}):")
        for p_ in problems:
            print(" -", p_)
        raise SystemExit(1)
    print("KIT_RECEIPT REPRODUCED")


if __name__ == "__main__":
    main()
