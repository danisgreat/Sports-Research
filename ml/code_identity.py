"""Which ml/ source a forecast-cycle release freezes (RELEASE-SCOPE-v1).

A release records one code digest and refuses to run when it changes. The digest used to cover every
ml/*.py file, so editing a report, chat or pregame helper retired every active release even though the
forecast could not change (NHL-CYCLE-3 went stale this way within four days). The digest now covers only
the static import closure of ``ml.cycle`` and ``ml.workflow``: every ml module they can import, including
imports inside functions, read with ``ast``. A new dependency joins the closure automatically.

``read(path)`` returns the bytes of a repository-relative POSIX path such as ``ml/cycle.py``, or None, so the
same rule serves a checkout and a git archive. Line endings never change the digest; any source byte does.
"""
from __future__ import annotations

import ast
import hashlib
from pathlib import Path

ENTRY = ("ml.cycle", "ml.workflow")


def _module_path(name: str, read) -> str | None:
    base = name.replace(".", "/")
    for candidate in (base + ".py", base + "/__init__.py"):
        if read(candidate) is not None:
            return candidate
    return None


def closure(read, entry=ENTRY) -> list[str]:
    """Sorted repository paths of every ml module reachable by import from ``entry``."""
    seen: dict[str, str] = {}
    todo = list(entry)
    while todo:
        name = todo.pop()
        if name in seen:
            continue
        path = _module_path(name, read)
        if path is None:
            continue
        seen[name] = path
        parts = name.split(".")
        todo.extend(".".join(parts[:i]) for i in range(1, len(parts)))  # parent packages run first
        package = name if path.endswith("/__init__.py") else name.rpartition(".")[0]
        for node in ast.walk(ast.parse(read(path))):
            if isinstance(node, ast.Import):
                todo.extend(a.name for a in node.names if a.name == "ml" or a.name.startswith("ml."))
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                if node.level:
                    keep = package.split(".")[: len(package.split(".")) - node.level + 1]
                    module = ".".join(keep + ([module] if module else []))
                if module == "ml" or module.startswith("ml."):
                    todo.append(module)
                    todo.extend(f"{module}.{a.name}" for a in node.names if _module_path(f"{module}.{a.name}", read))
    return sorted(seen.values())


def digest(read, entry=ENTRY) -> str:
    h = hashlib.sha256()
    for path in closure(read, entry):
        h.update(path.encode())
        h.update(read(path).replace(b"\r\n", b"\n"))
    return h.hexdigest()


def checkout_reader(root: Path):
    root = Path(root)

    def read(path: str):
        file = root / path
        return file.read_bytes() if file.is_file() else None
    return read
