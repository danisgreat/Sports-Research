"""ENG-01: every runtime module imports (an undefined name at import time must fail CI, not hide behind a collection error)."""

import importlib
import pkgutil

import runtime.src


def test_every_runtime_module_imports():
    failures = []
    count = 0
    for info in pkgutil.walk_packages(runtime.src.__path__, "runtime.src."):
        count += 1
        try:
            importlib.import_module(info.name)
        except Exception as exc:                      # noqa: BLE001 - report all failures together
            failures.append(f"{info.name}: {type(exc).__name__}: {exc}")
    assert count >= 30, f"only {count} modules found; the package layout changed"
    assert not failures, "\n".join(failures)


def test_evaluation_module_has_its_typing_imports():
    from runtime.src.common import evaluation
    assert evaluation.Optional is not None and evaluation.FixedCohortEvaluator.evaluate.__annotations__["event_ids_cand"] is not None
