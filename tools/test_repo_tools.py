"""Tests for tools/manifest_lib.py, verify_manifest.py, make_manifest.py and repo_hygiene.py (2026-09-25(c))."""
import datetime as dt
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_manifest as mk  # noqa: E402
import manifest_lib as ml  # noqa: E402
import repo_hygiene as rh  # noqa: E402
import verify_manifest as vm  # noqa: E402


def write(p: Path, data: bytes):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)


class ManifestLib(unittest.TestCase):
    def test_crlf_form_is_idempotent_and_eol_independent(self):
        self.assertEqual(ml.crlf_bytes(b"a\nb\n"), b"a\r\nb\r\n")
        self.assertEqual(ml.crlf_bytes(b"a\r\nb\r\n"), b"a\r\nb\r\n")
        self.assertEqual(ml.crlf_bytes(b"a\r\nb\n"), b"a\r\nb\r\n")

    def test_binary_untouched(self):
        self.assertEqual(ml.crlf_bytes(b"\x00\n\x01"), b"\x00\n\x01")

    def test_living_logs(self):
        self.assertTrue(ml.is_living("PREDICTION_LOG_COMBINED_5.md"))
        self.assertTrue(ml.is_living("GAME_LOG_STATUS_CURRENT.md"))
        self.assertFalse(ml.is_living("archive/x/PREDICTION_LOG_COMBINED_5.md"))
        self.assertFalse(ml.is_living("METHOD.md"))

    def test_current_manifest_read_from_method(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            write(repo / "METHOD.md", "Freeze the SHA-256 file receipt from [CONTROL_MANIFEST_X.md](CONTROL_MANIFEST_X.md) with".encode())
            self.assertEqual(ml.current_manifest(repo).name, "CONTROL_MANIFEST_X.md")


class MakeAndVerify(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        write(self.repo / "METHOD.md", b"rules\nmore\n")
        write(self.repo / "GAME_LOG_STATUS_CURRENT.md", b"status\n")
        sha = hashlib.sha256(b"rules\r\nmore\r\n").hexdigest()
        prev = (f"| File | SHA-256 | Bytes |\n|---|---|---:|\n| `METHOD.md` | `{sha}` | 13 |\n"
                f"| `GAME_LOG_STATUS_CURRENT.md` | `{'0' * 64}` | 1 |\n")
        write(self.repo / "CONTROL_MANIFEST_A.md", prev.encode())
        write(self.repo / "new_tool.py", b"print(1)\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_lf_checkout_verifies_against_crlf_hash(self):
        res = vm.verify(self.repo / "CONTROL_MANIFEST_A.md", self.repo)
        self.assertEqual(res["match"], ["METHOD.md"])
        self.assertEqual(res["living_changed"], ["GAME_LOG_STATUS_CURRENT.md"])
        self.assertEqual(res["mismatch"], [])
        strict = vm.verify(self.repo / "CONTROL_MANIFEST_A.md", self.repo, include_living=True)
        self.assertEqual(strict["mismatch"], ["GAME_LOG_STATUS_CURRENT.md"])

    def test_governance_change_is_a_mismatch(self):
        write(self.repo / "METHOD.md", b"rules changed\n")
        res = vm.verify(self.repo / "CONTROL_MANIFEST_A.md", self.repo)
        self.assertEqual(res["mismatch"], ["METHOD.md"])

    def test_build_reports_changes_and_round_trips(self):
        text, info = mk.build(self.repo / "CONTROL_MANIFEST_A.md", "CONTROL_MANIFEST_B.md", "test", "Note.",
                              add=["new_tool.py"], repo=self.repo,
                              now=dt.datetime(2026, 9, 25, 0, 0, tzinfo=dt.timezone.utc))
        self.assertEqual(info["new"], ["new_tool.py"])
        self.assertEqual(info["changed"], ["GAME_LOG_STATUS_CURRENT.md"])
        self.assertIn("2026-09-25 10:00 AEST", text)
        write(self.repo / "CONTROL_MANIFEST_B.md", text.encode("utf-8"))
        res = vm.verify(self.repo / "CONTROL_MANIFEST_B.md", self.repo, include_living=True)
        self.assertEqual(len(res["match"]), 3)
        self.assertEqual(res["mismatch"] + res["missing"], [])

    def test_build_never_lists_itself(self):
        _, info = mk.build(self.repo / "CONTROL_MANIFEST_A.md", "METHOD.md", "t", "n", repo=self.repo)
        self.assertNotIn("METHOD.md", info["files"])


    def test_category_rules_for_the_rule_freeze(self):  # added 2026-09-26 (C-RULE-FREEZE)
        self.assertEqual(mk.category_errors("DOCUMENTATION", None, None, True, 0), [])
        self.assertTrue(mk.category_errors("CHORE", None, None, False, 0))
        self.assertTrue(mk.category_errors("MODEL_CHANGE", None, None, False, 0))            # needs --model-change
        self.assertTrue(mk.category_errors("INTEGRITY", "new cap", None, False, 0))          # model change mislabelled
        self.assertTrue(mk.category_errors("MODEL_CHANGE", "refit RM-1", None, True, 0))     # freeze needs override
        self.assertEqual(mk.category_errors("MODEL_CHANGE", "refit RM-1", "user: refit now", True, 0), [])
        self.assertTrue(mk.category_errors("MEASUREMENT", None, None, True, 1))              # second manifest today
        self.assertEqual(mk.category_errors("VALIDITY_REPAIR", None, None, True, 2), [])

    def test_build_prints_category_and_override(self):  # added 2026-09-26
        text, _ = mk.build(self.repo / "CONTROL_MANIFEST_A.md", "CONTROL_MANIFEST_C.md", "t", "n", repo=self.repo,
                           category="MODEL_CHANGE", model_change="x", freeze_override="user said so")
        self.assertIn("**Category (C-RULE-FREEZE):** MODEL_CHANGE.", text)
        self.assertIn("**Freeze override (user instruction):** user said so", text)


class Hygiene(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_forbidden_paths(self):
        paths = ["node_modules/x/index.js", "a/__pycache__/m.cpython-314.pyc", ".codex_spreadsheet_tmp/p.json",
                 ".claude/settings.local.json", "METHOD.md"]
        probs = rh.check(paths, self.repo)
        self.assertEqual(len(probs), 4)

    def test_control_character_and_literal_newline(self):
        write(self.repo / "A.md", "| a |\\n| b |\n**MDS**\\nControl revision\n".encode())
        write(self.repo / "b.py", b"x = '\x08'\n")
        write(self.repo / "C.md", "```python\nprint('a\\nb')\n```\n".encode())
        probs = rh.check(["A.md", "b.py", "C.md"], self.repo)
        self.assertEqual(sum("LITERAL" in p for p in probs), 2)
        self.assertEqual(sum("CONTROL CHARACTER" in p for p in probs), 1)
        self.assertFalse(any("C.md" in p for p in probs))

    def test_large_file_rule(self):
        write(self.repo / "big.bin", b"0" * (2 * 1024 * 1024))
        write(self.repo / "PREDICTION_LOG_COMBINED_9.md", b"1" * (2 * 1024 * 1024))  # distinct bytes (duplicate rule, 2026-09-26)
        probs = rh.check(["big.bin", "PREDICTION_LOG_COMBINED_9.md"], self.repo, max_mb=1)
        self.assertEqual(len(probs), 1)
        self.assertIn("big.bin", probs[0])

    def test_duplicate_rule_live_versus_historical(self):  # added 2026-09-26
        body = b"x" * 4096
        for rel in ("archive/a/f.md", "archive/b/f.md", "prediction logs/f.md", "tools/one.py", "tools/two.py"):
            write(self.repo / rel, body if rel.startswith(("archive", "prediction")) else b"y" * 4096)
        write(self.repo / "small1.md", b"z" * 10)
        write(self.repo / "small2.md", b"z" * 10)
        probs = rh.duplicate_problems(["archive/a/f.md", "archive/b/f.md", "prediction logs/f.md",
                                       "tools/one.py", "tools/two.py", "small1.md", "small2.md"], self.repo)
        self.assertEqual(len(probs), 1)
        self.assertIn("tools/one.py", probs[0])
        write(self.repo / "crlf.md", b"a\r\n" * 600)
        write(self.repo / "lf.md", b"a\n" * 600)
        self.assertEqual(len(rh.duplicate_problems(["crlf.md", "lf.md"], self.repo)), 1)


if __name__ == "__main__":
    unittest.main()
