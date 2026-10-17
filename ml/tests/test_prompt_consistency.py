"""Prompt-suite consistency (Improvement 28): versions, links, dependency map and prompt-1 sport workflows.

Owner-entered Upcoming game blocks are never compared to a fixed text: their contents change with every game.
"""
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = ROOT / "research" / "prompts"
NAMES = ["1_GAME_CARD", "2_START_LOCAL_MINI", "3_SETTLE_LOCAL_MINI", "4_CANONICAL_IMPORT",
         "5_START_THE_NEXT_COMBINED_LOG", "6_COMBINED_LOG_RETROSPECTIVE", "7_EXPAND_PREVIOUS_RESULTS",
         "8_IMPROVE_THE_FRAMEWORK", "COMMON_OPERATING_PROTOCOL"]
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
    for target in re.findall(r"\]\(([^)\s]+)\)", text(name)):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        assert (PROMPTS / target.split("#")[0]).exists(), f"{name}: broken link {target}"


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


def test_prompt1_keeps_eleven_sport_workflows_each_with_the_no_code_paragraphs():
    body = text("1_GAME_CARD")
    starts = [m.start() for m in re.finditer(r"^(## )?Upcoming game — ", body, re.M)]
    assert len(starts) == 11
    sections = [body[a:b] for a, b in zip(starts, starts[1:] + [len(body)])]
    paragraphs = []
    for s in sections:
        assert re.search(r"^Read \[COMMON_OPERATING_PROTOCOL\]", s, re.M), "each Upcoming block is followed by Read"
        assert s.count("## 7. Write, audit and return") == 1 and s.count("**Mandatory output after every game request:**") == 1
        found = [re.findall(r"^\*\*" + re.escape(title) + r"\*\*.*$", s, re.M) for title in (
            "Analyst primary probability (ANALYST_PRIMARY_V1, no code).",
            "Learning record (LEARN-v2).",
            "Contract definitions and comparator (RET-10 / RET-13).")]
        assert all(len(f) == 1 for f in found)
        paragraphs.append(tuple(f[0] for f in found))
    assert len(set(paragraphs)) == 1, "the analyst, learning-record and definitions paragraphs must be identical in every sport workflow"
    assert body.count("**No code in game research (NOCODE-v1, MLSCOPE-v1).**") == 1


@pytest.mark.parametrize("name", ["1_GAME_CARD", "2_START_LOCAL_MINI", "3_SETTLE_LOCAL_MINI", "5_START_THE_NEXT_COMBINED_LOG"])
def test_game_research_prompts_give_no_commands_to_run(name):
    """MLSCOPE-v1: prompts 1-3 and 5 are research frameworks; ML/RL commands belong to prompts 6 and 8."""
    body = text(name)
    assert not re.search(r"`python |python -m |`git |pip install", body), f"{name} must not instruct running code"
    assert "PRIMARY_PREDICTION_PROTOCOL" not in body and "FORECAST_CYCLE_PROTOCOL" not in body
