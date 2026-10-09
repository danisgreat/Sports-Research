import re
from pathlib import Path

from research.operations import dev_check

ROOT = Path(__file__).resolve().parents[2]


def normalise(parts):
    return " ".join(p for p in parts if p != "-B")


def test_every_ci_command_is_in_dev_check_and_vice_versa():
    workflow = (ROOT / ".github/workflows/research.yml").read_text(encoding="utf-8")
    ci = [re.sub(r"^python\s+", "", line.strip()) for line in re.findall(r"^\s+(?:run:\s+|)(python\s+-[^\n]+)$", workflow, re.M)]
    ci = [normalise(c.split()) for c in ci if "pip install" not in c]
    local = [normalise(command) for _, command in dev_check.STEPS]
    assert sorted(ci) == sorted(local), f"CI and dev_check drifted:\nCI only: {set(ci) - set(local)}\nlocal only: {set(local) - set(ci)}"


def test_python_version_is_pinned_to_the_lock():
    lock = (ROOT / "research/requirements.lock.txt").read_text(encoding="utf-8")
    workflow = (ROOT / ".github/workflows/research.yml").read_text(encoding="utf-8")
    assert dev_check.pinned_version() in lock and f"python-version: '{dev_check.pinned_version()}'" in workflow


def test_version_skew_is_reported(monkeypatch):
    monkeypatch.setattr(dev_check.platform, "python_version", lambda: "3.10.0")
    assert "pins" in dev_check.version_problem()
    assert dev_check.main(["--list"]) == 0
    assert dev_check.main([]) == 2
