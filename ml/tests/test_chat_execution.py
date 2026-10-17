"""CHAT-EXEC-v1: pack the committed runtime, run the unchanged cycle in a chat sandbox, accept it back.

Synthetic EXAMPLE competitions and LOCAL-EXAMPLE keys only; no live P-ID, store or ledger is touched.
"""
import csv
import io
import subprocess
import zipfile
from pathlib import Path

import pandas as pd
import pytest

from ml import chat, cycle as C, primary as p, research_ingest as ri
from ml.evaluation import prospective as PS
from ml.run import code_digest
from ml.tests import learning_fixtures as lf

KEY = "LOCAL-EXAMPLE-G0001"


def _write(path: Path, rows: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = io.StringIO(newline="")
    writer = csv.DictWriter(text, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    path.write_bytes(text.getvalue().encode())


@pytest.fixture
def runtime(tmp_path, monkeypatch):
    root = tmp_path / "runtime"
    (root / "ml").mkdir(parents=True)
    (root / "ml" / "workflow.py").write_text("# runtime marker for the root check\n")
    frame = lf.season_frame(n_teams=6)
    frame = frame[frame.hs != frame.as_].head(65)
    lf.ingest_frame(tmp_path, root / chat.STORE, frame, "history")
    release = root / chat.RELEASES / "EXAMPLE-CHAT-v1.csv"
    release.parent.mkdir(parents=True, exist_ok=True)
    C.freeze_release(release, lf.COMPETITION, lf.ENDPOINT, "EXAMPLE-CHAT-v1")
    _write(root / chat.CURRENT, [dict(competition=lf.COMPETITION, endpoint=lf.ENDPOINT, active_experimental_release="EXAMPLE-CHAT-v1",
                                      release_path=chat.RELEASES + "/EXAMPLE-CHAT-v1.csv", release_sha256=p.digest(release.read_bytes()),
                                      source_code_sha256=code_digest(), qualification="EXPERIMENTAL_NOT_QUALIFIED", prospective_events="0")])
    start = pd.Timestamp.now(tz="UTC") + pd.Timedelta(days=1)
    game = dict(local_key=KEY, competition=lf.COMPETITION, native_event_id="EXAMPLE:1", season="2026",
                scheduled_start=start.isoformat(), home="T00", away="T01", venue="EXAMPLE-ARENA", source_url="https://example.org/fixture")
    lines = [dict(label="HOME_ML", family="winner", side="HOME", line=""),
             dict(label="OVER_200.5", family="total", side="OVER", line="200.5"),
             dict(label="UNDER_200.5", family="total", side="UNDER", line="200.5")]
    work = tmp_path / "work"
    _write(work / "GAME.csv", [game])
    _write(work / "LINES.csv", lines)
    (work / "fixture.txt").write_text("EXAMPLE fixture page text: T00 v T01, EXAMPLE-ARENA", encoding="utf-8")
    monkeypatch.chdir(root)
    return dict(root=root, work=work, game=game, lines=lines)


def _run(rt, out="OUT", **kw):
    return chat.run(rt["work"] / "GAME.csv", rt["work"] / "LINES.csv", kw.pop("capture", rt["work"] / "fixture.txt"),
                    rt["root"] / out, confirmed=kw.pop("confirmed", True))


def test_mirrored_schemas_match_the_learning_store():
    assert chat.TARGET_FIELDS == ri.TARGET_FIELDS
    assert chat.EMPTY_EXPORTS == {"GAME_OBSERVATIONS.csv": ri.GAME_FIELDS, "TEAM_GAME_STATS.csv": ri.STAT_FIELDS,
                                  "AVAILABILITY.csv": ri.AVAIL_FIELDS}


def test_archive_digest_reproduces_the_release_code_digest():
    files = {f.relative_to(chat.ROOT).as_posix(): f.read_bytes() for f in (chat.ROOT / "ml").rglob("*.py")}
    assert chat.archive_code_digest(files) == code_digest()
    # Line endings never change the digest; any source byte does.
    crlf = {k: v.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n") for k, v in files.items()}
    assert chat.archive_code_digest(crlf) == code_digest()
    edited = dict(files, **{"ml/chat.py": files["ml/chat.py"] + b"# edit\n"})
    assert chat.archive_code_digest(edited) != code_digest()


def test_run_executes_verifies_and_packages_then_accept_freezes_pre_start(runtime):
    result = _run(runtime)
    assert result["status"] == "EXECUTED"
    rows = {r["label"]: r for r in result["results"]}
    assert set(rows) == {"HOME_ML", "OVER_200.5", "UNDER_200.5"}
    assert float(rows["OVER_200.5"]["p_card"]) + float(rows["UNDER_200.5"]["p_card"]) == pytest.approx(1)
    assert all(r["timing_at_generation"] == "PRE_START" and r["baseline_p"] not in ("", "NOT_ESTIMATED") for r in rows.values())
    with zipfile.ZipFile(result["upload"]) as zf:
        names = zf.namelist()
    assert all(n.startswith((f"{chat.ATTEMPTS}/{KEY}/", f"{chat.CAPTURES}/{KEY}/")) for n in names)
    assert any(n.endswith("/EXECUTION.csv") for n in names) and f"{chat.CAPTURES}/{KEY}/fixture.txt" in names
    accepted = chat.accept(result["upload"], KEY, root=runtime["root"])
    assert accepted["status"] == "EXECUTED" and accepted["evidence_status"] == "PRE_START_VERIFIED"
    ledger = PS.verify_ledger(runtime["root"] / chat.LEDGER)
    assert len(ledger) == int(accepted["ledger_rows"]) == 6 and {r["role"] for r in ledger} == {"CANDIDATE", "CHAMPION"}
    assert accepted["manifest_row"]["execution_sha256"] == accepted["execution_sha256"]
    with pytest.raises(chat.ChatError, match="already accepted"):
        chat.accept(result["upload"], KEY, root=runtime["root"])


def test_accept_after_start_is_never_pre_start(runtime):
    result = _run(runtime)
    late = pd.Timestamp(runtime["game"]["scheduled_start"]) + pd.Timedelta(minutes=5)
    rows = C.shadow_rows(Path(result["attempt"]) / "BUNDLE", now_at=late.isoformat())
    assert {r["evidence_status"] for r in rows} == {"TIMING_UNVERIFIED"}
    with pytest.raises(p.AdmissionError):
        PS.freeze(runtime["root"] / "late.csv", [dict(r, evidence_status="PRE_START_VERIFIED") for r in rows], now=late.isoformat())


@pytest.mark.parametrize("defect,message", [
    ("no_confirm", "confirm-no-outcome-seen"),
    ("unknown_team", "closest: T0"),
    ("unsupported_family", "not priced by the model"),
    ("no_release", "no active model release"),
    ("html_capture", ".txt/.csv/.md"),
    ("pid_identity", "never a P-ID"),
    ("naive_time", "explicit UTC offset"),
    ("bad_line", "numeric line"),
    ("existing_out", "new output folder"),
])
def test_run_refuses_inputs_it_cannot_price_honestly(runtime, defect, message):
    rt, kw = runtime, {}
    game, lines = dict(rt["game"]), list(rt["lines"])
    if defect == "no_confirm":
        kw["confirmed"] = False
    elif defect == "unknown_team":
        game["home"] = "T0O"
    elif defect == "unsupported_family":
        lines.append(dict(label="CORNERS_O10.5", family="corners", side="OVER", line="10.5"))
    elif defect == "no_release":
        game["competition"] = "Basketball/EXAMPLE-UNRELEASED"
    elif defect == "html_capture":
        html = rt["work"] / "fixture.html"
        html.write_text("<p>EXAMPLE</p>", encoding="utf-8")
        kw["capture"] = html
    elif defect == "pid_identity":
        game["native_event_id"] = "P-601"
    elif defect == "naive_time":
        game["scheduled_start"] = "2030-01-01T10:00:00"
    elif defect == "bad_line":
        lines[1] = dict(lines[1], line="two hundred")
    elif defect == "existing_out":
        (rt["root"] / "OUT").mkdir()
    _write(rt["work"] / "GAME.csv", [game])
    _write(rt["work"] / "LINES.csv", lines)
    with pytest.raises(chat.ChatError, match=message.replace(".", r"\.").replace("+", r"\+")):
        _run(rt, **kw)
    assert not (rt["root"] / chat.LEDGER).exists()


def test_failed_attempt_is_returned_with_its_real_error_and_no_ledger_rows(runtime, monkeypatch):
    def broken(*a, **k):
        raise p.AdmissionError("EXAMPLE injected fit failure")
    monkeypatch.setattr(C, "forecast", broken)
    result = _run(runtime)
    assert result["status"] == "FAILED" and "EXAMPLE injected fit failure" in result["results"][0]["error"]
    accepted = chat.accept(result["upload"], KEY, root=runtime["root"])
    assert accepted["status"] == "FAILED" and accepted["ledger_rows"] == "0"
    assert accepted["manifest_row"]["feedback_status"] == "NOT_APPLICABLE_NO_MODEL"


@pytest.mark.parametrize("member", ["../escape.csv", "research/learning_store/EVENTS.csv",
                                    f"{chat.ATTEMPTS}/{KEY}/A/BUNDLE/x.json"])
def test_accept_refuses_uploads_outside_scope_or_type(tmp_path, member):
    upload = tmp_path / "up.zip"
    with zipfile.ZipFile(upload, "w") as zf:
        zf.writestr(f"{chat.ATTEMPTS}/{KEY}/A/EXECUTION.csv", "x\n")
        zf.writestr(member, "x\n")
    with pytest.raises(chat.ChatError):
        chat.accept(upload, KEY, root=tmp_path)


def test_accept_commit_basis_requires_a_committed_attempt(runtime):
    result = _run(runtime)
    folder = runtime["root"] / chat.ATTEMPTS / KEY / Path(result["attempt"]).name
    with zipfile.ZipFile(result["upload"]) as zf:
        for name in zf.namelist():
            (runtime["root"] / name).parent.mkdir(parents=True, exist_ok=True)
            (runtime["root"] / name).write_bytes(zf.read(name))
    with pytest.raises(chat.ChatError):
        chat.accept(folder, KEY, freeze_basis="commit", root=runtime["root"])
    with pytest.raises(chat.ChatError, match="already committed"):
        chat.accept(result["upload"], KEY, freeze_basis="commit", root=runtime["root"])


def _git(root, *args):
    subprocess.run(["git", "-c", "user.name=EXAMPLE", "-c", "user.email=example@example.org", *args], cwd=root, check=True,
                   capture_output=True)


@pytest.mark.parametrize("stale", [False, True])
def test_pack_contains_committed_runtime_and_refuses_stale_releases(tmp_path, stale):
    repo = tmp_path / "repo"
    (repo / "ml").mkdir(parents=True)
    (repo / "ml" / "a.py").write_text("X = 1\n")
    _write(repo / chat.STORE / "SOURCE_OBSERVATIONS.csv", [dict(observation_id="o1", capture_path="research/verified_history/x/OWNER.csv")])
    _write(repo / "research/verified_history/x/OWNER.csv", [dict(a="1")])
    code = chat.archive_code_digest({"ml/a.py": b"X = 1\n"})
    release = repo / chat.RELEASES / "EX-1.csv"
    _write(release, [dict(version="EX-1", code_sha256="0" * 64 if stale else code)])
    _write(repo / chat.CURRENT, [dict(competition="Basketball/EXAMPLE", endpoint=lf.ENDPOINT, active_experimental_release="EX-1",
                                      release_path=chat.RELEASES + "/EX-1.csv", release_sha256=p.digest(release.read_bytes()))])
    _git(repo, "init", "-q")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "EXAMPLE")
    (repo / "ml" / "a.py").write_text("X = 2  # uncommitted\n")
    with pytest.raises(chat.ChatError, match="outside the repository"):
        chat.pack(repo / "packs", root=repo)
    if stale:
        with pytest.raises(chat.ChatError, match="different code"):
            chat.pack(tmp_path / "packs", root=repo)
        return
    result = chat.pack(tmp_path / "packs", root=repo)
    with zipfile.ZipFile(result["path"]) as zf:
        assert zf.read("ml/a.py") == b"X = 1\n"  # committed bytes, never the dirty working copy
        assert "research/verified_history/x/OWNER.csv" in zf.namelist()
        receipt = next(csv.DictReader(io.StringIO(zf.read("CHAT_PACK_RECEIPT.csv").decode())))
    assert receipt["code_sha256"] == code and receipt["format"] == chat.FORMAT
    assert "ml/a.py" in result["uncommitted_not_packed"]
