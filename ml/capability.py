"""Runtime capability receipt (RET-08): can this environment actually run the primary model?

Every card records this receipt before claiming ML_NOT_RUN. In the full card history (P-001–P-600) the primary model
never priced a card, and seven V3-era cards recorded only `No module named ml`, i.e. they were written where the
repository checkout did not exist. When this command itself cannot start, the card records the exact command and
error text instead, plus the bootstrap attempt of prompt 1 (pinned checkout and `pip install -r ml/requirements.txt`).

    python -m ml capability [--out CAPABILITY_RECEIPT.csv]
"""
from __future__ import annotations

import argparse
import importlib
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

MODULES = ("numpy", "pandas", "scipy")


def receipt() -> dict:
    from ml import primary as p
    rec = dict(checked_at=datetime.now(timezone.utc).isoformat(), python=sys.version.split()[0],
               platform=platform.platform(), executable=sys.executable,
               repository_root=str(Path(__file__).resolve().parents[1]), repository_head=p.repository_head(),
               code_sha256=p.source_hash(), primary_policy=p.POLICY)
    missing = []
    for name in MODULES:
        try:
            rec[name] = importlib.import_module(name).__version__
        except ImportError:
            rec[name] = "MISSING"
            missing.append(name)
    required = Path(__file__).resolve().parent / "requirements.txt"
    pins = {}
    for line in required.read_text(encoding="utf-8").splitlines():
        if "==" in line and not line.strip().startswith("#"):
            k, v = line.split("==", 1)
            pins[k.strip().lower()] = v.strip()
    drift = [f"{k} {rec.get(k)}!={v}" for k, v in pins.items() if k in MODULES and rec.get(k) not in (v, "MISSING")]
    rec["pinned_version_drift"] = ";".join(drift) or "NONE"
    rec["status"] = "RUNTIME_AVAILABLE" if not missing else "RUNTIME_DEPENDENCIES_MISSING:" + ",".join(missing)
    return rec


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, help="write the receipt as a one-row CSV (never overwrites)")
    args = parser.parse_args(argv)
    rec = receipt()
    for k, v in rec.items():
        print(f"{k}: {v}")
    if args.out:
        from ml.primary import csv_bytes
        with args.out.open("xb") as f:
            f.write(csv_bytes([rec]))


if __name__ == "__main__":
    main()
