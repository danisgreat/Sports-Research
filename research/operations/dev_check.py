"""Run every CI check locally, in CI order (ENG-03).

    uv venv --python 3.14.6 && uv pip install -r research/requirements.lock.txt -r research/requirements-lint.txt
    python -B -m research.operations.dev_check

The interpreter must match `.python-version` (the version the build receipts and the lock were produced on). A mismatch
fails loudly instead of skipping tests, so a green local run means the same thing as a green CI run.
`--only <substring>` runs the matching steps; `--list` prints them.
"""

from __future__ import annotations

import argparse
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PY = [sys.executable]

STEPS: list[tuple[str, list[str]]] = [
    ("ruff (runtime and operations)", ["-m", "ruff", "check", "runtime", "research/operations"]),
    ("ruff (undefined names in research/src)", ["-m", "ruff", "check", "--select", "F821,F822,F823,F811,F63,F7,F82", "research/src"]),
    ("mypy", ["-m", "mypy", "--config-file", "mypy.ini", "runtime/src", "research/src", "research/operations"]),
    ("pytest", ["-B", "-m", "pytest", "-p", "no:cacheprovider", "research/tests", "research/operations", "research/experiments", "runtime/tests", "-q"]),
    ("log_card verify", ["-B", "-m", "research.operations.log_card", "verify"]),
    ("verify_custody", ["-B", "-m", "research.operations.verify_custody"]),
    ("verify_reconciliation", ["-B", "-m", "research.operations.verify_reconciliation"]),
    ("control_freeze --verify", ["-B", "-m", "research.operations.control_freeze", "--verify"]),
    ("verify_all_logs", ["-B", "-m", "research.operations.verify_all_logs"]),
    ("experiments verify", ["-B", "-m", "research.experiments.runner", "verify"]),
    ("verify_rollover", ["-B", "-m", "research.operations.verify_rollover"]),
    ("verify_carryover_review", ["-B", "-m", "research.operations.verify_carryover_review"]),
    ("scoreboard verify", ["-B", "-m", "research.operations.scoreboard", "verify"]),
    ("regimes verify", ["-B", "-m", "research.operations.regimes", "verify"]),
    ("cross_card verify", ["-B", "-m", "research.experiments.cross_card", "verify"]),
    ("settlement_lint active", ["-B", "-m", "research.operations.settlement_lint", "active"]),
    ("settlement_lint rank-log", ["-B", "-m", "research.operations.settlement_lint", "rank-log", "GAME_PREDICTION_RANK_LOG.csv"]),
    ("registry_lint", ["-B", "-m", "research.operations.registry_lint"]),
    ("reachability verify", ["-B", "-m", "research.operations.reachability", "verify"]),
    ("evidence_snapshot verify-store", ["-B", "-m", "research.operations.evidence_snapshot", "verify-store"]),
    ("current_state verify", ["-B", "-m", "research.operations.current_state", "verify"]),
    ("fit_runtime_models verify", ["-B", "-m", "research.operations.fit_runtime_models", "verify"]),
    ("boosted_challenger verify", ["-B", "-m", "research.operations.boosted_challenger", "verify"]),
]


def pinned_version() -> str:
    return (ROOT / ".python-version").read_text(encoding="utf-8").strip()


def version_problem() -> str | None:
    want, have = pinned_version(), platform.python_version()
    return None if want == have else f"Python {have} is running but .python-version pins {want}; install it with `uv python install {want}`"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--only", help="run only steps whose name contains this text")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--allow-version-skew", action="store_true", help="run on another interpreter; results are not CI-equivalent")
    args = parser.parse_args(argv)
    if args.list:
        for name, _ in STEPS:
            print(name)
        return 0
    problem = version_problem()
    if problem and not args.allow_version_skew:
        print(f"ERROR: {problem}", file=sys.stderr)
        return 2
    failures = []
    for name, command in STEPS:
        if args.only and args.only.lower() not in name.lower():
            continue
        print(f"== {name}", flush=True)
        if subprocess.run(PY + command, cwd=ROOT).returncode != 0:
            failures.append(name)
    print("FAILED: " + ", ".join(failures) if failures else "all checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
