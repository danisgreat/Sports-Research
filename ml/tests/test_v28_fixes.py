"""v28.0 review fixes: portable locks, branch-scoped staging, explicit GitHub activity, registered constants."""
import ast
import os
import subprocess
import sys
from pathlib import Path

import pytest

from ml import file_lock
from ml import forecast_integrity as F
from ml import one_chat as O

ROOT = Path(__file__).resolve().parents[2]
POSIX_ONLY = {"fcntl", "termios", "pwd", "grp", "resource", "posix"}


def test_no_module_outside_the_lock_helper_imports_a_posix_only_library():
    offenders = []
    for path in sorted((ROOT / "ml").rglob("*.py")):
        if path.name == "file_lock.py" or "tests" in path.parts:
            continue
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            names = [a.name.split(".")[0] for a in node.names] if isinstance(node, ast.Import) else \
                    [node.module.split(".")[0]] if isinstance(node, ast.ImportFrom) and node.module else []
            offenders += [f"{path.relative_to(ROOT).as_posix()}: {n}" for n in names if n in POSIX_ONLY]
    assert offenders == [], "use ml.file_lock instead: " + "; ".join(offenders)


def test_the_lock_refuses_a_second_writer_waits_briefly_and_is_released_on_exit(tmp_path):
    target = tmp_path / "LEDGER.csv"
    target.write_text("x\n")
    with file_lock.exclusive(target, what="the ledger"):
        with pytest.raises(RuntimeError, match="the ledger is locked by another writer"):
            with file_lock.exclusive(target, wait=0.5, what="the ledger"):
                pass
    with file_lock.exclusive(target):
        pass
    assert not list(tmp_path.glob("*.lock")), "no lock file is left in the protected folder"


def test_a_lock_held_by_another_live_process_is_never_taken_over(tmp_path):
    target = tmp_path / "LEDGER.csv"
    target.write_text("x\n")
    ready = tmp_path / "ready"
    holder = subprocess.Popen([sys.executable, "-c", (
        "import sys, time, pathlib; sys.path.insert(0, sys.argv[1]); from ml import file_lock\n"
        "with file_lock.exclusive(pathlib.Path(sys.argv[2])):\n"
        "    pathlib.Path(sys.argv[3]).write_text('1'); time.sleep(30)\n"), str(ROOT), str(target), str(ready)])
    try:
        for _ in range(100):
            if ready.exists():
                break
            subprocess.run([sys.executable, "-c", "import time; time.sleep(0.1)"])
        assert ready.exists()
        old = os.path.getmtime(file_lock.lock_path(target)) - 7 * 86400
        os.utime(file_lock.lock_path(target), (old, old))
        with pytest.raises(RuntimeError, match="locked by another writer"):
            with file_lock.exclusive(target, wait=0.5):
                pass
    finally:
        holder.kill()
        holder.wait()
    with file_lock.exclusive(target, wait=5):           # released when the holder died
        pass


def _probe(branch):
    env = dict(os.environ, ONE_CHAT_SEAL_BRANCH=branch)
    out = subprocess.run([sys.executable, "-c", "from ml import one_chat as O; print(O.STAGING, O.PENDING_REFS)"],
                         cwd=ROOT, env=env, capture_output=True, text=True, check=True)
    return out.stdout.split()


def test_staging_and_pending_refs_are_kept_per_seal_branch():
    assert _probe("forecast-seals") == ["forecast-staging", "refs/forecast-pending"]
    assert _probe("test-forecast-seals-rehearsal") == ["forecast-staging-test-forecast-seals-rehearsal",
                                                       "refs/forecast-pending-test-forecast-seals-rehearsal"]


def _repo(tmp_path):
    root = tmp_path / "repo"
    subprocess.run(["git", "init", "-q", "-b", "main", str(root)], check=True)
    for k, v in (("user.email", "example@example.org"), ("user.name", "Example"), ("core.autocrlf", "false")):
        subprocess.run(["git", "-C", str(root), "config", k, v], check=True)
    (root / "README.md").write_text("example\n")
    subprocess.run(["git", "-C", str(root), "add", "README.md"], check=True)
    subprocess.run(["git", "-C", str(root), "commit", "-q", "-m", "start"], check=True)
    return root


def test_a_rehearsal_seal_left_in_local_staging_is_invisible_to_the_registered_evaluation(tmp_path):
    root = _repo(tmp_path)
    rehearsal = root / ".git" / "forecast-staging-test-forecast-seals"
    rehearsal.mkdir(parents=True)
    (rehearsal / "PENDING.csv").write_bytes(O.csv_bytes(O.SEAL_FIELDS, [dict(
        card_key="REHEARSAL-G0001", block_sha256="a" * 64, file_sha256="b" * 64,
        sealed_path=f"{O.SEALED}/x.md", sealed_at_client="2026-11-17T00:00:00+00:00", policy_sha256="", policy_commit="")]))
    assert O.STAGING == "forecast-staging"
    assert O.Repo(root).seals == []


def test_github_activity_is_fetched_only_when_a_server_time_is_needed_and_a_failure_is_explicit(tmp_path, monkeypatch):
    root = _repo(tmp_path)
    calls = []

    def failing(r):
        calls.append(r)
        raise O.OneChatError("GitHub push activity could not be fetched (gh api): offline")

    monkeypatch.setattr(O, "github_push_activity", failing)
    repo = O.Repo(root)
    assert calls == []                                   # reading blobs and registries needs no network
    head = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    assert repo.pushed_at(head) == "" and "could not be fetched" in repo.activity_error
    assert repo.pushed_at(head) == "" and len(calls) == 1  # fetched once per read of the repository


def test_a_failed_gh_call_raises_instead_of_reading_as_no_pushes(tmp_path, monkeypatch):
    monkeypatch.setattr(O, "_remote_slug", lambda root: "example/repo")
    monkeypatch.setattr(O.subprocess, "run", lambda *a, **kw: subprocess.CompletedProcess(a, 1, "", "HTTP 503"))
    with pytest.raises(O.OneChatError, match="could not be fetched"):
        O.github_push_activity(tmp_path)


def test_registered_constants_match_the_published_plan():
    plan = (ROOT / O.PLAN).read_text(encoding="utf-8")
    assert O.PLAN.endswith("EVALUATION_PLAN_v29.0.md") and O.HORIZON == 600 and F.LAMBDAS == (0.5, 0.7, 0.9)
    assert "(0.5, 0.7, 0.9)" in plan and "600 games" in plan and "Alpha: 0.05" in plan and "0.01" in plan


def test_power_study_is_deterministic_and_reports_every_scenario():
    a = F.power_study(horizon=40, runs=3, null_runs=3, seed=1)
    assert a == F.power_study(horizon=40, runs=3, null_runs=3, seed=1)
    assert [r["scenario"] for r in a] == [s for s, _ in F.POWER_SCENARIOS]
