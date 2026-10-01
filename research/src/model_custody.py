"""Verify immutable current model build receipts before every operational fit."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from .load import ROOT
from importlib.metadata import version
import platform

BUILDS = ROOT / "model_builds/current.json"

def verify_model_build(lane: str, model_version: str, path: Path = BUILDS) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    matches = [b for b in data["builds"] if b["lane"]==lane and b["model_version"]==model_version]
    if len(matches) != 1:
        raise ValueError("exact lane/model build is not registered")
    build = matches[0]
    if not build.get("artifacts"):
        raise ValueError("empty model dependency receipt")
    if platform.python_version()!=build.get("python_version"):
        raise ValueError("Python runtime differs from the frozen model build")
    for package,expected in build.get("packages",{}).items():
        if version(package)!=expected:
            raise ValueError("runtime dependency changed: "+package)
    for item in build["artifacts"]:
        target = (ROOT.parent / item["path"]).resolve()
        if not target.is_relative_to(ROOT.parent.resolve()):
            raise ValueError("model artifact escapes repository")
        if hashlib.sha256(target.read_bytes()).hexdigest() != item["sha256"]:
            raise ValueError("model build changed: "+item["path"])
    return build
