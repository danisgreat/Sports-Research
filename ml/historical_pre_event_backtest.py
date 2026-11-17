"""Strict point-in-time retrospective algorithm study; never original-forecast proof.

Fixed L2=1 logistic regression, no test-outcome tuning. Each evaluation trains on
earlier sporting events whose feature records AND outcomes were available before
the test forecast's verified issue time. The entire test event is held out.
"""

from __future__ import annotations

import json
import math
import tempfile
from pathlib import Path

import numpy as np

from ml import historical_pre_event as H
from ml.card_training import fit_logistic

MIN_TRAIN_EVENTS = 30
FIELDS = (
    "row_id",
    "event_id",
    "issued_at",
    "y",
    "model_p",
    "training_base_rate",
    "train_events",
    "train_rows",
    "status",
)


def walk_forward(examples):
    """Examples have reviewed, real availability times; no invented outcome lag."""
    examples = sorted(
        examples, key=lambda r: (H.timestamp(r["issued_at"]), r["row_id"])
    )
    out = []
    for test in examples:
        cutoff = H.timestamp(test["issued_at"])
        if H.timestamp(test["features_available_at"]) > cutoff:
            raise ValueError("test features were unavailable at forecast cutoff")
        train = [
            r
            for r in examples
            if r["event_id"] != test["event_id"]
            and H.timestamp(r["issued_at"]) < cutoff
            and H.timestamp(r["features_available_at"]) < cutoff
            and H.timestamp(r["outcome_available_at"]) < cutoff
        ]
        events = len({r["event_id"] for r in train})
        row = dict(
            row_id=test["row_id"],
            event_id=test["event_id"],
            issued_at=test["issued_at"],
            y=test["y"],
            model_p="",
            training_base_rate="",
            train_events=events,
            train_rows=len(train),
            status="INSUFFICIENT_PRIOR_EVENTS",
        )
        if events >= MIN_TRAIN_EVENTS:
            X = np.array([[1.0, *r["values"]] for r in train])
            y = np.array([int(r["y"]) for r in train])
            beta = fit_logistic(X, y, l2=1.0)
            z = float(np.array([1.0, *test["values"]]) @ beta)
            p = 1 / (1 + math.exp(-max(-700.0, min(700.0, z))))
            row.update(
                model_p=p,
                training_base_rate=float(y.mean()),
                status="RETROSPECTIVE_ALGORITHM_STUDY_ONLY",
            )
        out.append(row)
    return out


def run(features, out, root=H.ROOT):
    root, features, out = Path(root), Path(features), Path(out)
    if out.exists():
        raise FileExistsError(out)
    ledger_raw = (root / H.BASE / "EVIDENCE_REVISIONS.csv").read_bytes()
    _, inputs, _ = H.build(root, ledger_raw=ledger_raw)
    inputs["ml/historical_pre_event_backtest.py"] = H.digest(
        (root / "ml/historical_pre_event_backtest.py").read_bytes()
    )
    inputs["ml/card_training.py"] = H.digest(
        (root / "ml/card_training.py").read_bytes()
    )
    # Reuse exactly the evidence admission decisions, not the old approximate dates.
    ledger = H.load_ledger(raw=ledger_raw)
    latest = {r["row_id"]: json.loads(r["payload"]) for r in ledger}
    known = {r["row_id"]: r for r in H.read_csv(root / H.TRAIN)}
    raw = features.read_bytes()
    feature_rows = H.read_csv(features)
    if len({r["row_id"] for r in feature_rows}) != len(feature_rows):
        raise ValueError("duplicate feature row")
    examples, schema = [], None
    for f in feature_rows:
        if f["row_id"] not in known:
            raise ValueError("feature row absent from frozen census")
        d = H.assess(known[f["row_id"]], latest.get(f["row_id"], {}), root, inputs)
        if not d["accuracy"]:
            raise ValueError(
                "strict study needs Tier A and independent decisive outcomes"
            )
        if (
            latest[f["row_id"]]["outcome"]["proof"].get("availability_time_verified")
            is not True
        ):
            raise ValueError(
                "strict study needs independently verified outcome availability time"
            )
        # A feature record contains the names, values and availability cutoff. The
        # review binds its sporting source extraction and point-in-time integrity.
        record = json.loads(H.artifact(root, json.loads(f["capture"]), inputs))
        proof = json.loads(f["proof"])
        H.reviewed(root, proof, inputs)
        if (
            proof.get("pre_event_data_verified") is not True
            or record["row_id"] != f["row_id"]
        ):
            raise ValueError("feature extraction or availability unverified")
        names = sorted(record["values"])
        schema = names if schema is None else schema
        if not names or names != schema:
            raise ValueError("feature schema differs between events")
        values = [float(record["values"][k]) for k in schema]
        if not all(math.isfinite(v) for v in values):
            raise ValueError("nonfinite feature")
        if H.timestamp(record["available_at"]) > H.timestamp(d["issued_at"]):
            raise ValueError("feature information leakage")
        examples.append(
            dict(
                known[f["row_id"]],
                **d,
                values=values,
                features_available_at=record["available_at"],
            )
        )
    H.deduplicate(examples)
    examples = [e for e in examples if e["accuracy"]]
    pred = walk_forward(examples)
    if features.read_bytes() != raw:
        raise ValueError("features changed during study")
    # One CSV row per evaluation is retained, including no-prediction warm-up rows.
    outputs = {"PREDICTIONS.csv": H.csv_bytes(pred, FIELDS)}
    scores = []
    for p in pred:
        if p["model_p"] == "":
            continue
        d = next(e for e in examples if e["row_id"] == p["row_id"])
        scores.append(
            dict(
                d,
                p=p["model_p"],
                baseline_p=p["training_base_rate"],
                paired=True,
                rank=known[d["row_id"]]["rank"],
            )
        )
    metric, sensitivity, calibration = H.metrics(
        scores, "ALGORITHM_STUDY", "FIXED_L2_1"
    )
    outputs["SCORES.csv"] = H.csv_bytes([metric], list(metric))
    outputs["DEPENDENCE_SENSITIVITY.csv"] = H.csv_bytes(
        sensitivity, list(sensitivity[0])
    )
    outputs["CALIBRATION.csv"] = H.csv_bytes(calibration, list(calibration[0]))
    outputs["REPORT.md"] = (
        "# Strict chronological historical model study\n\n"
        "RETROSPECTIVE_ALGORITHM_STUDY_ONLY; no evidence of original model authorship, "
        "no prospective certification. Fixed L2=1 logistic regression; 30 prior events "
        "minimum; no test-outcome tuning. Entire test event held out. Training features "
        "and labels must precede test issue time. Feature names: "
        + ", ".join(schema or [])
        + ".\n\nInput feature-table SHA-256: "
        + H.digest(raw)
        + "\n"
    ).encode()
    outputs["EVIDENCE_SNAPSHOT.csv"] = ledger_raw
    manifest = [dict(role="INPUT", path=k, sha256=v) for k, v in sorted(inputs.items())]
    manifest += [
        dict(role="FEATURE_TABLE", path=str(features.resolve()), sha256=H.digest(raw))
    ]
    manifest += [
        dict(role="OUTPUT", path=p, sha256=H.digest(raw))
        for p, raw in sorted(outputs.items())
    ]
    outputs["MANIFEST.csv"] = H.csv_bytes(manifest, ("role", "path", "sha256"))
    for name, expected in inputs.items():
        if H.input_digest(root, name) != expected:
            raise ValueError("study source changed during generation")
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=out.parent) as temp:
        staging = Path(temp) / "study"
        staging.mkdir()
        for name, data in outputs.items():
            (staging / name).write_bytes(data)
        staging.rename(out)
    return metric
