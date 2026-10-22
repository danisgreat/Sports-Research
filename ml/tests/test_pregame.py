"""MLSCOPE-v2 / ENV-v2: the pregame model shadow runs in the repository only after the analyst card is written.

Synthetic EXAMPLE competitions and LOCAL-EXAMPLE keys only; no live P-ID, store or ledger is touched.
"""
import subprocess
import sys
from pathlib import Path as Path_

import pytest

from ml import chat, code_identity, cycle as C, pregame
from ml.evaluation import prospective as PS
from ml.tests.test_chat_execution import KEY, _write, runtime  # noqa: F401  (pytest fixture)


def _mini(rt, card_text="Over 200.5 p_card 0.612"):
    mini = rt["work"] / "MINI.md"
    mini.write_text("<!-- MINI-LOG-FORMAT: mini-log-10 -->\n# EXAMPLE mini\n"
                    + (f"<!-- BEGIN CARD {KEY} -->\n{card_text}\n<!-- END CARD {KEY} -->\n" if card_text is not None else "")
                    + "# RUNNING FOOTER\n", encoding="utf-8")
    return mini


def _lines(rt, card_p="0.612"):
    rows = [dict(r, card_p="", card_rank="") for r in rt["lines"]]
    rows[1] = dict(rows[1], card_p=card_p, card_rank="1")
    _write(rt["work"] / "PREGAME_LINES.csv", rows)
    return rt["work"] / "PREGAME_LINES.csv"


def _run(rt, mini, lines):
    return pregame.run(mini, rt["work"] / "GAME.csv", lines, rt["work"] / "fixture.txt", confirmed=True, root=rt["root"])


def test_model_runs_only_after_the_card_is_written(runtime):
    with pytest.raises(pregame.PregameError, match="before the model runs"):
        _run(runtime, _mini(runtime, card_text=None), _lines(runtime))
    assert not (runtime["root"] / chat.LEDGER).exists()


def test_card_probability_must_be_the_one_printed_on_the_card(runtime):
    with pytest.raises(pregame.PregameError, match="not printed in card"):
        _run(runtime, _mini(runtime), _lines(runtime, card_p="0.71"))
    # A value that only appears inside a longer number is not the card's value either.
    with pytest.raises(pregame.PregameError, match="not printed in card"):
        _run(runtime, _mini(runtime, card_text="p_card 0.6125"), _lines(runtime))


def test_run_freezes_model_baseline_and_card_rows_on_identical_contracts(runtime):
    result = _run(runtime, _mini(runtime), _lines(runtime))
    assert result["status"] == "EXECUTED" and result["timing_at_generation"] == "PRE_START"
    ledger = PS.verify_ledger(runtime["root"] / chat.LEDGER)
    model = [r for r in ledger if r["model_id"] == C.POLICY]
    card = [r for r in ledger if r["model_id"] == pregame.CARD_MODEL]
    assert len(model) == 3 and len(card) == 1 and int(result["ledger_card_rows"]) == 1
    over = next(r for r in model if r["side"] == "OVER")
    assert card[0]["contract_key"] == over["contract_key"] and card[0]["p"] == "0.612"
    assert card[0]["evidence_status"] == "PRE_START_VERIFIED" and card[0]["role"] == "CHAMPION"
    receipt = chat._rows(result["receipt"])[0]
    assert receipt["status"] == "EXECUTED" and receipt["mini_sha256"] == chat._sha((runtime["work"] / "MINI.md").read_bytes())
    block = pregame.markdown(result)
    assert "Model shadow" in block and "unchanged by this block" in block


def test_competition_without_a_release_is_recorded_not_invented(runtime):
    game = dict(runtime["game"], competition="Basketball/EXAMPLE-UNRELEASED")
    _write(runtime["work"] / "GAME.csv", [game])
    result = _run(runtime, _mini(runtime), _lines(runtime))
    assert result["status"] == "NOT_RUN_NO_RELEASE" and result["results"] == []
    assert not (runtime["root"] / chat.LEDGER).exists()
    assert "Model shadow" in pregame.markdown(result) and "Reason:" in pregame.markdown(result)


def test_release_frozen_for_other_code_is_not_run(runtime, monkeypatch):
    monkeypatch.setattr(C, "code_hash", lambda: "0" * 64)
    result = _run(runtime, _mini(runtime), _lines(runtime))
    assert result["status"] == "NOT_RUN_STALE_RELEASE"
    assert not (runtime["root"] / chat.LEDGER).exists()


def test_refused_input_keeps_the_card_and_writes_a_receipt(runtime):
    game = dict(runtime["game"], home="T0O")
    _write(runtime["work"] / "GAME.csv", [game])
    result = _run(runtime, _mini(runtime), _lines(runtime))
    assert result["status"] == "NOT_RUN_INPUT_REFUSED" and "closest: T0" in result["reason"]


def test_status_reports_progress_after_a_run(runtime):
    _run(runtime, _mini(runtime), _lines(runtime))
    rows = pregame.status(root=runtime["root"])
    assert len(rows) == 1
    row = rows[0]
    assert (row["frozen_events"], row["pre_start_events"], row["settled_events"], row["state"]) == (1, 1, 0, "ACCUMULATING")


@pytest.mark.parametrize("events,weeks,state", [
    (49, 7, "ACCUMULATING"),
    (50, 1, "PROGRESS_REVIEW_DUE"),   # 50 games first
    (12, 8, "PROGRESS_REVIEW_DUE"),   # 8 weeks first
    (60, 7, "PROGRESS_REVIEW_DUE"),   # a decision still needs 8 weeks
    (50, 8, "DECISION_FLOOR_MET"),
])
def test_review_is_due_at_either_floor_and_a_decision_needs_both(events, weeks, state):
    assert pregame.lane_state(events, weeks, 50, 8) == state


# ------------------------------------------------------------------ release code scope (RELEASE-SCOPE-v1)
def _repo_files():
    return {f.relative_to(chat.ROOT).as_posix(): f.read_bytes() for f in (chat.ROOT / "ml").rglob("*.py")}


def test_release_digest_covers_the_cycle_import_closure_only():
    files = _repo_files()
    paths = code_identity.closure(files.get)
    assert {"ml/cycle.py", "ml/workflow.py", "ml/primary.py", "ml/code_identity.py"} <= set(paths)
    assert not {"ml/pregame.py", "ml/chat.py", "ml/evaluation/card_history.py"} & set(paths)
    base = code_identity.digest(files.get)
    assert base == C.code_hash()
    crlf = {k: v.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n") for k, v in files.items()}
    assert code_identity.digest(crlf.get) == base
    outside = dict(files, **{"ml/pregame.py": files["ml/pregame.py"] + b"# edit\n"})
    assert code_identity.digest(outside.get) == base
    inside = dict(files, **{"ml/cycle.py": files["ml/cycle.py"] + b"# edit\n"})
    assert code_identity.digest(inside.get) != base


def test_static_closure_contains_every_module_the_cycle_actually_imports():
    probe = ("import sys, ml.cycle, ml.workflow; "
             "print('\\n'.join(sorted(m.__file__ for n, m in sys.modules.items() "
             "if (n == 'ml' or n.startswith('ml.')) and getattr(m, '__file__', None))))")
    out = subprocess.run([sys.executable, "-c", probe], cwd=chat.ROOT, capture_output=True, text=True, check=True).stdout
    loaded = {chat.Path(f).resolve().relative_to(chat.ROOT).as_posix() for f in out.splitlines() if f.strip()}
    assert loaded <= set(code_identity.closure(code_identity.checkout_reader(chat.ROOT)))


def test_closure_follows_relative_and_function_level_imports():
    files = {"ml/__init__.py": b"", "ml/cycle.py": b"def f():\n    from . import helper\n",
             "ml/helper.py": b"import ml.deep\n", "ml/deep.py": b"", "ml/workflow.py": b"", "ml/unrelated.py": b""}
    assert code_identity.closure(files.get) == ["ml/__init__.py", "ml/cycle.py", "ml/deep.py", "ml/helper.py", "ml/workflow.py"]


# ------------------------------------------------------------------ REFMODEL-v1: the model runs before the card
def _reference(rt):
    return pregame.reference(rt["work"] / "GAME.csv", rt["work"] / "LINES.csv", rt["work"] / "fixture.txt", confirmed=True, root=rt["root"])


def test_reference_stage_needs_the_outcome_confirmation(runtime):
    with pytest.raises(pregame.PregameError, match="confirm-no-outcome-seen"):
        pregame.reference(runtime["work"] / "GAME.csv", runtime["work"] / "LINES.csv", runtime["work"] / "fixture.txt", root=runtime["root"])


def test_reference_stage_freezes_the_model_before_any_card_exists(runtime):
    result = _reference(runtime)
    assert result["status"] == "EXECUTED" and result["stage"] == "REFERENCE" and result["timing_at_generation"] == "PRE_START"
    ledger = PS.verify_ledger(runtime["root"] / chat.LEDGER)
    assert len([r for r in ledger if r["model_id"] == C.POLICY]) == 3 and not [r for r in ledger if r["model_id"] == pregame.CARD_MODEL]
    text = pregame.markdown(result)
    assert "Reference (REFMODEL-v1, frozen before this card)" in text and "adjustment ledger" in text and "MLSCOPE-v3" not in text
    receipt = Path_(result["receipt"])
    assert receipt.name.endswith("_REFERENCE_CYCLE.csv") and chat._rows(receipt)[0]["stage"] == "REFERENCE"


def test_run_after_a_reference_reuses_the_attempt_and_adds_only_the_card_row(runtime):
    reference = _reference(runtime)
    before = PS.verify_ledger(runtime["root"] / chat.LEDGER)
    result = _run(runtime, _mini(runtime), _lines(runtime))
    after = PS.verify_ledger(runtime["root"] / chat.LEDGER)
    assert result["status"] == "EXECUTED" and result["stage"] == "REFERENCE_REUSED" and result["attempt_path"] == reference["attempt_path"]
    assert len(after) == len(before) + 1 and [r for r in after if r["model_id"] == pregame.CARD_MODEL][0]["p"] == "0.612"
    assert len([r for r in after if r["model_id"] == C.POLICY]) == 3               # the model was not run or accepted twice
    block = pregame.markdown(result)
    assert "reference reused" in block and "model frozen before the card" in block        # the table was printed with the Reference block


def test_a_missing_release_at_the_reference_stage_is_recorded_and_the_card_still_runs_its_shadow_path(runtime):
    game = dict(runtime["game"], competition="Basketball/EXAMPLE-UNRELEASED")
    _write(runtime["work"] / "GAME.csv", [game])
    result = _reference(runtime)
    assert result["status"] == "NOT_RUN_NO_RELEASE" and result["results"] == []
    later = _run(runtime, _mini(runtime), _lines(runtime))
    assert later["status"] == "NOT_RUN_NO_RELEASE" and later["stage"] == "SHADOW"


def test_a_reference_that_did_not_execute_is_not_reused(runtime, monkeypatch):
    real = C.code_hash
    monkeypatch.setattr(C, "code_hash", lambda: "0" * 64)
    assert _reference(runtime)["status"] == "NOT_RUN_STALE_RELEASE"
    monkeypatch.setattr(C, "code_hash", real)
    result = _run(runtime, _mini(runtime), _lines(runtime))
    assert result["stage"] == "SHADOW" and result["status"] == "EXECUTED" and result["ledger_card_rows"] == "1"


def test_tb2_reference_rows_freeze_beside_the_model_and_status_counts_them(runtime):
    reference = _reference(runtime)
    attempt = runtime["root"] / reference["attempt_path"]
    rows = pregame.card_rows(attempt, {"HOME_ML": ("0.5978", ""), "OVER_200.5": ("0.4100", "")}, chat._now().isoformat(), champion="TB2")
    PS.freeze(runtime["root"] / chat.LEDGER, rows, now=chat._now().isoformat())
    ledger = PS.verify_ledger(runtime["root"] / chat.LEDGER)
    tb2 = [r for r in ledger if r["model_id"] == pregame.REFERENCE_MODEL]
    assert len(tb2) == 2 and {r["role"] for r in tb2} == {"CHAMPION"} and tb2[0]["model_version"] == pregame.REFERENCE_VERSION
    status = pregame.status(root=runtime["root"])[0]
    assert status["reference_paired_settled"] == 0 and status["frozen_events"] == 1
