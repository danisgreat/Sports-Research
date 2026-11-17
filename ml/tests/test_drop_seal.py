"""DROP-SEAL-v1: pushed request/card drops are registered and sealed by the unchanged ONE-CHAT-v3 code."""
import os
import subprocess
import sys

from ml import drop_seal as D
from ml import forecast_integrity as F
from ml import one_chat as O
from ml.tests import test_one_chat as M

repo = M.repo


def request_files(text):
    """The owner request, event and contract definitions that match a test card, as an outside chat would push them."""
    key, _, meta, picks, _, problems, _ = O.card_blocks(text)[0]
    assert not problems
    event = {f: meta[f] for f in ("sport", "competition", "home", "away", "scheduled_start")}
    event.update(event_id="TEST:" + O.game_id(meta), schedule_source="https://example.org/official-schedule")
    contracts = [dict(**{f: r[f] for f in ("label", "family", "side", "line")}, period="FULL_MATCH",
                      endpoint="REGULATION", action="NORMAL", unit="POINTS",
                      request_excerpt=f"{r['family']} {r['side']} {r['line']}", baseline_p="",
                      baseline_id="UNAVAILABLE:NO_FROZEN_LEAGUE_BASELINE") for r in picks]
    return key, {
        "REQUEST.txt": "\n".join(r["request_excerpt"] for r in contracts).encode(),
        "EVENT.csv": O.csv_bytes(F.EVENT_FIELDS, [event]),
        "CONTRACTS.csv": O.csv_bytes(F.CONTRACT_FIELDS, contracts),
    }


def push_drop(repo, files: dict[str, bytes], message="drop"):
    """Commit files on the drop branch and return (before, after) as the workflow receives them."""
    if M.git(repo, "rev-parse", "--abbrev-ref", "HEAD") != "card-drops":
        M.git(repo, "checkout", "-q", "-b", "card-drops")
        before = D.ZERO
    else:
        before = M.git(repo, "rev-parse", "HEAD")
    for path, raw in files.items():
        target = repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    M.git(repo, "add", "-A")
    M.git(repo, "commit", "-q", "-m", message)
    return before, M.git(repo, "rev-parse", "HEAD")


def seal_branch(repo, path):
    return subprocess.run(["git", "-C", str(repo), "cat-file", "blob", f"refs/remotes/origin/{O.SEAL_BRANCH}:{path}"],
                          capture_output=True).stdout


def request_drop(key, files):
    return {f"drops/requests/{key}/{name}": raw for name, raw in files.items()}


def test_request_then_card_is_registered_and_sealed_exactly(repo):
    text = M.card()
    key, files = request_files(text)
    results = D.process(repo, *push_drop(repo, request_drop(key, files)))
    assert [(r["kind"], r["card_key"], r["status"]) for r in results] == [("request", key, "REGISTERED")]
    assert key in seal_branch(repo, O.REQUEST_INDEX).decode()
    assert seal_branch(repo, F.request_path(key) + "/REQUEST.txt") == files["REQUEST.txt"]
    M.Server("2026-11-20T04:30:00Z")(repo)              # GitHub times the registration before research started

    raw = text.encode()
    results = D.process(repo, *push_drop(repo, {"drops/cards/alpha-beta.md": raw}),
                        lookup=M.Server("2026-11-20T07:00:00Z"), wait=(0,))
    assert [(r["kind"], r["status"]) for r in results] == [("card", "SEALED")]
    seals = F.rows(seal_branch(repo, O.SEALS))
    assert [s["card_key"] for s in seals] == [key]
    assert seal_branch(repo, seals[0]["sealed_path"]) == raw     # exact pushed bytes, nothing re-encoded
    assert M.git(repo, "rev-parse", "--abbrev-ref", "HEAD") == "card-drops"   # HEAD and main untouched

    again = D.process(repo, *push_drop(repo, {"drops/cards/alpha-beta.md": raw, "drops/notes.txt": b"x"}),
                      lookup=M.Server("2026-11-20T07:10:00Z"), wait=(0,))
    assert [r["status"] for r in again] == ["IGNORED"]   # unchanged card is not a new drop; stray file is reported

    edited = text.replace("0.62", "0.64").replace("0.38", "0.36").encode()
    changed = D.process(repo, *push_drop(repo, {"drops/cards/alpha-beta.md": edited}),
                        lookup=M.Server("2026-11-20T07:20:00Z"), wait=(0,))
    assert changed[0]["status"] == "FAILED" and "already sealed" in changed[0]["detail"]
    assert len(F.rows(seal_branch(repo, O.SEALS))) == 1


def test_a_card_pushed_with_its_own_request_cannot_be_sealed(repo):
    text = M.card()
    key, files = request_files(text)
    drop = request_drop(key, files) | {"drops/cards/same-push.md": text.encode()}
    results = D.process(repo, *push_drop(repo, drop), lookup=M.Server("2026-11-20T07:00:00Z"), wait=(0,))
    status = {r["kind"]: r for r in results}
    assert status["request"]["status"] == "REGISTERED"
    assert status["card"]["status"] == "FAILED" and "before research starts" in status["card"]["detail"]
    assert not seal_branch(repo, O.SEALS)


def test_an_unregistered_or_blockless_card_fails_with_a_reason(repo):
    results = D.process(repo, *push_drop(repo, {"drops/cards/a.md": M.card().encode(),
                                                "drops/cards/b.md": b"# notes only\n"}),
                        lookup=M.Server("2026-11-20T07:00:00Z"), wait=(0,))
    by = {r["drop"]: r for r in results}
    assert by["drops/cards/a.md"]["status"] == "FAILED" and "register" in by["drops/cards/a.md"]["detail"]
    assert by["drops/cards/b.md"]["status"] == "FAILED" and "ONECHAT_V1" in by["drops/cards/b.md"]["detail"]
    assert "**FAILED**" in D.summary(results, "f" * 40)


def test_an_incomplete_request_drop_is_refused(repo):
    key, files = request_files(M.card())
    files.pop("CONTRACTS.csv")
    results = D.process(repo, *push_drop(repo, request_drop(key, files)))
    assert results[0]["status"] == "FAILED" and "CONTRACTS.csv" in results[0]["detail"]
    assert not seal_branch(repo, O.REQUEST_INDEX)


def test_the_seal_branch_override_accepts_only_rehearsal_branches():
    def load(value):
        env = dict(os.environ, ONE_CHAT_SEAL_BRANCH=value)
        return subprocess.run([sys.executable, "-c", "from ml import one_chat as O; print(O.SEAL_BRANCH)"],
                              cwd=O.ROOT, env=env, capture_output=True, text=True)
    assert load("test-forecast-seals-dry-run").stdout.strip() == "test-forecast-seals-dry-run"
    assert load("forecast-seals").stdout.strip() == "forecast-seals"
    assert load("main").returncode != 0


def test_a_concurrent_publication_is_retried_and_other_errors_are_not(repo, monkeypatch):
    calls = []
    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise O.OneChatError("seal push refused; no force or main push attempted: rejected")
        return "ok"
    monkeypatch.setattr(D.time, "sleep", lambda s: None)
    assert D._publish(flaky, repo) == "ok" and len(calls) == 3
    def invalid():
        calls.append(1)
        raise O.OneChatError("not sealed: incomplete or invalid card")
    calls.clear()
    try:
        D._publish(invalid, repo)
    except O.OneChatError:
        pass
    assert len(calls) == 1
