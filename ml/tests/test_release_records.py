"""One version file (G-2), the deep loss register (S-4) and the template the chat fills (ONE-CHAT-v1)."""
import csv
import re
import shutil

import pytest

from ml import deep_loss as D
from ml import one_chat as O
from ml import state as S


def test_versions_file_is_what_core_the_prompts_and_current_state_print():
    v = S.versions()
    core = (S.ROOT / "CORE.md").read_text(encoding="utf-8")
    assert S.version_line() in core
    suite = v["prompt_suite"]["current"]
    for path in (S.ROOT / "research" / "prompts").rglob("*.md"):
        found = set(re.findall(r"P-2026\.\d\d\.\d\d-v\d+\.\d+", path.read_text(encoding="utf-8")[:6000]))
        if path.parent.name == "prompts" and path.name[0].isdigit():
            assert suite in found, path.name
    state = (S.ROOT / S.STATE).read_text(encoding="utf-8")
    assert all(v[i]["current"] in state for i in S.VERSION_ITEMS)
    assert S.restamp() == [], "a release leaves nothing for restamp to change"


def test_restamp_replaces_only_the_previous_suite_and_the_core_line(tmp_path):
    (tmp_path / "research/prompts").mkdir(parents=True)
    (tmp_path / "research/prompts/1_X.md").write_text("**P-2026.01.01-v1.0 · X.** history cites P-2025.12.01-v0.9\n", encoding="utf-8")
    (tmp_path / "CORE.md").write_text("# CORE\n\n**MDS-2026.01.01-v1.0 · CR-2026.01.01-R1 · P-2026.01.01-v1.0 · SCV-2026.01.01-v1 · SEL-2026.01.01-v1.** text\n", encoding="utf-8")
    (tmp_path / "VERSIONS.csv").write_text("item,current,previous\nmethod,MDS-2026.02.01-v2.0,MDS-2026.01.01-v1.0\ncontrol_revision,CR-2026.02.01-R1,CR-2026.01.01-R1\n"
                                           "prompt_suite,P-2026.02.01-v2.0,P-2026.01.01-v1.0\nscoring,SCV-2026.01.01-v1,SCV-2026.01.01-v1\nselection,SEL-2026.01.01-v1,SEL-2026.01.01-v1\n", encoding="utf-8")
    assert S.restamp(tmp_path) == ["research/prompts/1_X.md", "CORE.md"]
    assert (tmp_path / "research/prompts/1_X.md").read_text(encoding="utf-8") == "**P-2026.02.01-v2.0 · X.** history cites P-2025.12.01-v0.9\n"
    assert "**MDS-2026.02.01-v2.0 · CR-2026.02.01-R1 · P-2026.02.01-v2.0 · SCV-2026.01.01-v1 · SEL-2026.01.01-v1.** text" in (tmp_path / "CORE.md").read_text(encoding="utf-8")
    assert S.restamp(tmp_path) == []
    (tmp_path / "VERSIONS.csv").write_text("item,current,previous\nmethod,,x\n", encoding="utf-8")
    with pytest.raises(ValueError, match="VERSIONS.csv"):
        S.versions(tmp_path)


def test_committed_deep_loss_register_is_valid_and_tallies_patterns():
    assert D.problems() == []
    by = {r["failure"]: r for r in D.tally()}
    assert by["UNMEASURED_AVAILABILITY_PRICED"]["status"] == "PATTERN_ROUTE_TO_PROMPT_8"
    assert by["VARIANCE"]["status"] == "BELOW_PATTERN" and by["MODEL_LIMIT_NO_CLASS_RECORDED"]["status"] == "CLASS_NOT_RECORDED"


def test_register_refuses_unknown_classes_verdicts_and_missing_sources(tmp_path):
    shutil.copytree(S.ROOT / "research/deep_loss", tmp_path / "research/deep_loss")
    shutil.copy(S.ROOT / "RULES_REFERENCE.md", tmp_path / "RULES_REFERENCE.md")
    path = tmp_path / D.REGISTER
    rows = D.read(tmp_path)
    rows[0].update(registered_class="BAD_LUCK", verdict="UNLUCKY")
    rows[1].update(registered_class="OTHER", alias="")
    rows.append(dict(rows[2]))
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=D.FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    text = " | ".join(D.problems(tmp_path))
    for needle in ("registered_class must be", "verdict is one of", "OTHER needs an alias", "unique", "source is the settlement document"):
        assert needle in text


def test_the_printed_template_parses_once_filled():
    text = O.template("Ice Hockey").replace("<MINI_KEY>", "CHATX")
    m = O.BLOCK.search(text)
    meta, picks, facts = O.parse(m["body"])
    assert len(picks) == 4 and {r["field"] for r in facts} == set(O.required_facts("Ice Hockey")) and meta["format"] == "ONECHAT_V1"


def test_the_briefs_worked_example_is_a_valid_block_apart_from_its_elided_facts():
    brief = (S.ROOT / "research/external/ONE_CHAT_BRIEF_v27.0.md").read_text(encoding="utf-8").replace("<MINI_KEY>", "CHATX")
    body = re.sub(r"https://<[^>]+>", "https://example.org/x", O.BLOCK.search(brief)["body"].replace(chr(10) + "...", ""))
    meta, picks, facts = O.parse(body)
    problems, derived = O.check(meta, picks, facts, "CHATX-G0001")
    assert problems and all(p.startswith("FACTS ") and "required for Basketball" in p for p in problems)
    rows = O.rows_for("CHATX-G0001", "GAME-X", derived)
    assert {r["label"]: r["p"] for r in rows if r["side"] in ("HOME", "OVER")} == {"L1": "0.61", "L2": "0.52", "L3": "UNPRICED"}
