"""DECISION-LAB-v2 (RULES_REFERENCE Part A §5a, owner instruction 2026-11-08): the decision lab is a separate contributor and
never adds to the main prediction. Only its own package, the run-all orchestrator and the results writer may touch it."""
import ast
from pathlib import Path

ML = Path(__file__).resolve().parents[1]
ORCHESTRATOR = ("run.py", "run_decision_lab")          # the only function allowed to import ml.decision outside the package
OUTPUT_WRITERS = {"evaluation/writers.py", "run.py"}   # the only modules allowed to name the lab's output folder
FORECAST_PATH = ("reference.py", "pregame.py", "ledger.py", "picks.py", "primary.py", "cycle.py", "league_day.py", "chat.py",
                 "research_learning.py", "research_ingest.py", "training_admission.py", "releasegate.py", "registry.py",
                 "features.py", "endpoint.py", "workflow.py")


def _modules():
    for path in sorted(ML.rglob("*.py")):
        rel = path.relative_to(ML).as_posix()
        if rel.startswith(("decision/", "tests/")):
            continue
        yield rel, ast.parse(path.read_text(encoding="utf-8"))


def _imports(tree):
    """(imported module, enclosing function name or None) for every import in the file, nested ones included."""
    out = []

    def visit(node, func):
        for child in ast.iter_child_nodes(node):
            name = child.name if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) else func
            if isinstance(child, ast.Import):
                out.extend((a.name, func) for a in child.names)
            elif isinstance(child, ast.ImportFrom) and child.module:
                out.append((child.module, func))
                out.extend((f"{child.module}.{a.name}", func) for a in child.names)
            visit(child, name)
    visit(tree, None)
    return out


def test_only_the_orchestrator_imports_the_decision_lab():
    offenders = [(rel, mod, func) for rel, tree in _modules() for mod, func in _imports(tree)
                 if mod == "ml.decision" or mod.startswith("ml.decision.")
                 if (rel, func) != ORCHESTRATOR]
    assert offenders == []


def test_forecast_path_never_reaches_the_lab_or_its_orchestrator():
    offenders = []
    for rel, tree in _modules():
        if rel not in FORECAST_PATH:
            continue
        for mod, _ in _imports(tree):
            if mod.startswith(("ml.decision", "ml.run")) or mod.endswith("write_decision_lab"):
                offenders.append((rel, mod))
    assert offenders == []


def test_only_the_writers_name_the_lab_output_folder():
    offenders = []
    for rel, tree in _modules():
        if rel in OUTPUT_WRITERS:
            continue
        docstrings = {id(n.value) for n in ast.walk(tree) if isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant)}
        if any(isinstance(n, ast.Constant) and isinstance(n.value, str) and "DECISION_LAB" in n.value and id(n) not in docstrings
               for n in ast.walk(tree)):
            offenders.append(rel)
    assert offenders == []
