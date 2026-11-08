"""SRC-ALT-v1: a source that blocks AI agents, or whose rules cannot be read, is not opened (offline; no network)."""
import pytest

from ml import source_audit as S

URL = "https://example.org/match/1"


@pytest.mark.parametrize("http,text,status", [
    ("200", "User-agent: *\nAllow: /\n", "ALLOWED"),
    ("404", None, "NO_RULES_FILE"),
    ("410", None, "NO_RULES_FILE"),
    ("200", "User-agent: Claude-User\nDisallow: /\n\nUser-agent: *\nAllow: /\n", "BLOCKED_FOR_AI"),
    ("200", "User-agent: ClaudeBot\nDisallow: /match/\n", "BLOCKED_FOR_AI"),
    ("200", "User-agent: *\nContent-Signal: search=yes, ai-input=no\nAllow: /\n", "BLOCKED_FOR_AI"),
    ("200", "User-agent: *\nDisallow: /match/\n", "BLOCKED_FOR_AI"),
    ("403", None, "RULES_UNKNOWN"),
    ("429", None, "RULES_UNKNOWN"),
    ("ERROR:TimeoutError", None, "RULES_UNKNOWN"),
    ("200", "<html><body>challenge</body></html>", "RULES_UNKNOWN"),
])
def test_classification(http, text, status):
    assert S.classify(URL, http, text)["status"] == status


def test_a_block_on_another_path_does_not_block_this_one():
    text = "User-agent: ClaudeBot\nDisallow: /api/\n"
    assert S.classify(URL, "200", text)["status"] == "ALLOWED"
    assert S.classify("https://example.org/api/scores", "200", text)["agents_blocked"] == "ClaudeBot"


def test_only_allowed_and_no_rules_may_be_opened():
    assert set(S.OPEN) == {"ALLOWED", "NO_RULES_FILE"}
