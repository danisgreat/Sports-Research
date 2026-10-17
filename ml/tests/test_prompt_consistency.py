"""Prompt-suite consistency (Improvement 28): versions, links, dependency map and prompt-1 sport files.

Owner-entered Upcoming game blocks are never compared to a fixed text: their contents change with every game.
Prompt 1 is a core file plus one sport file per sport in research/prompts/1_sports/ (P-2026.10.17-v22.1).
"""
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = ROOT / "research" / "prompts"
SPORT_FILES = sorted("1_sports/" + p.stem for p in (PROMPTS / "1_sports").glob("*.md"))
NAMES = ["1_GAME_CARD", "2_START_LOCAL_MINI", "3_SETTLE_LOCAL_MINI", "4_CANONICAL_IMPORT",
         "5_START_THE_NEXT_COMBINED_LOG", "6_COMBINED_LOG_RETROSPECTIVE", "7_EXPAND_PREVIOUS_RESULTS",
         "8_IMPROVE_THE_FRAMEWORK", "COMMON_OPERATING_PROTOCOL"] + SPORT_FILES
VERSION = re.compile(r"P-\d{4}\.\d{2}\.\d{2}-v\d+\.\d+")
CONTROLS = sorted(p.stem for p in ROOT.glob("*.md") if re.fullmatch(r"[A-Z0-9_]+", p.stem) and p.stem != "README")


def text(name: str) -> str:
    return (PROMPTS / f"{name}.md").read_text(encoding="utf-8")


def current_suite() -> str:
    row = re.search(r"^\| Prompt suite \| (P-[^ ]+) ", (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8"), re.M)
    assert row, "CURRENT_STATE must declare the prompt suite"
    return row.group(1)


@pytest.mark.parametrize("name", NAMES + ["README", "DEPENDENCY_MAP"])
def test_every_prompt_declares_the_current_suite_version(name):
    found = set(VERSION.findall(text(name)))
    assert current_suite() in found
    if name != "README":  # the index may cite earlier releases historically
        assert found == {current_suite()}


@pytest.mark.parametrize("name", NAMES + ["README", "DEPENDENCY_MAP"])
def test_relative_links_resolve(name):
    folder = (PROMPTS / f"{name}.md").parent
    for target in re.findall(r"\]\(([^)\s]+)\)", text(name)):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        assert (folder / target.split("#")[0]).exists(), f"{name}: broken link {target}"


def _map() -> dict:
    rows = re.findall(r"^\| \[([^\]]+)\.md\]\([^)]+\) \| ([^|]+) \|$", text("DEPENDENCY_MAP"), re.M)
    return {name: [c.strip() for c in deps.split(",")] for name, deps in rows}


def test_dependency_map_covers_every_prompt_in_both_directions():
    deps = _map()
    assert set(deps) == set(NAMES)
    for name, listed in deps.items():
        body = text(name)
        named = {c for c in CONTROLS if re.search(r"(?<![A-Z_])" + c + r"(?![A-Z_])", body)}
        assert all((ROOT / f"{c}.md").exists() for c in listed), f"{name}: map lists a missing control"
        assert set(listed) == named, f"{name}: map {sorted(set(listed) ^ named)} out of date"


def test_prompt1_core_indexes_eleven_sport_files_each_with_the_no_code_paragraphs():
    core = text("1_GAME_CARD")
    assert len(SPORT_FILES) == 11
    assert all(f"]({name}.md)" in core for name in SPORT_FILES), "the core must link every sport file"
    assert "Upcoming game — " not in core, "Upcoming game blocks live in the sport files"
    assert core.count("**No code in game research (NOCODE-v1, MLSCOPE-v1).**") == 1
    paragraphs = []
    for name in SPORT_FILES:
        s = text(name)
        assert "](../1_GAME_CARD.md)" in s, f"{name}: must point to the core"
        assert len(re.findall(r"^(## )?Upcoming game — ", s, re.M)) == 1, f"{name}: exactly one Upcoming game block"
        assert re.search(r"^Read \[COMMON_OPERATING_PROTOCOL\]", s, re.M), "each Upcoming block is followed by Read"
        assert s.count("## 7. Write, audit and return") == 1 and s.count("**Mandatory output after every game request:**") == 1
        found = [re.findall(r"^\*\*" + re.escape(title) + r"\*\*.*$", s, re.M) for title in (
            "Analyst primary probability (ANALYST_PRIMARY_V1, no code).",
            "Learning record (LEARN-v2).",
            "Contract definitions and comparator (RET-10 / RET-13).",
            "Mandatory output after every game request:")]
        assert all(len(f) == 1 for f in found), name
        paragraphs.append(tuple(f[0] for f in found))
    assert len(set(paragraphs)) == 1, "the shared paragraphs must be identical in every sport file"


@pytest.mark.parametrize("name", ["1_GAME_CARD", "2_START_LOCAL_MINI", "3_SETTLE_LOCAL_MINI", "5_START_THE_NEXT_COMBINED_LOG"]
                         + SPORT_FILES)
def test_game_research_prompts_give_no_commands_to_run(name):
    """MLSCOPE-v1: prompts 1-3 and 5 are research frameworks; ML/RL commands belong to prompts 6 and 8."""
    body = text(name)
    assert not re.search(r"`python |python -m |`git |pip install", body), f"{name} must not instruct running code"
    assert "PRIMARY_PREDICTION_PROTOCOL" not in body and "FORECAST_CYCLE_PROTOCOL" not in body


@pytest.mark.parametrize("name", ["1_GAME_CARD", "2_START_LOCAL_MINI", "3_SETTLE_LOCAL_MINI"] + SPORT_FILES)
def test_external_chat_prompts_are_read_only_and_pinned_to_latest_main(name):
    """ENV-v1: prompts 1-3 run in an external chat; they never use local controls or claim file writes."""
    body = text(name)
    if not name.startswith("1_sports/"):
        assert "EXECUTION_ENVIRONMENT_PROTOCOL" in body and "EXTERNAL_CHAT" in body
    assert "latest `main`" in body or name.startswith("1_sports/")
    for phrase in ("explicitly local", "or from the local working tree", "Copy exact original working bytes",
                   "complete frozen prefix plus settlement", "working attachment/download"):
        assert phrase not in body, f"{name}: {phrase}"


def test_prompt4_is_the_intake_point_for_external_chat_output():
    body = text("4_CANONICAL_IMPORT")
    assert "## 0. External-chat intake (ENV-v1)" in body and "PENDING_PROMPT_4" in body
