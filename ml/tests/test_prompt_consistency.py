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


def test_prompt1_keeps_eleven_sport_workflows_each_with_the_learning_export():
    body = text("1_GAME_CARD")
    starts = [m.start() for m in re.finditer(r"^(## )?Upcoming game — ", body, re.M)]
    assert len(starts) == 11
    sections = [body[a:b] for a, b in zip(starts, starts[1:] + [len(body)])]
    paragraphs = []
    for s in sections:
        assert re.search(r"^Read \[COMMON_OPERATING_PROTOCOL\]", s, re.M), "each Upcoming block is followed by Read"
        assert s.count("## 7. Write, audit and return") == 1 and s.count("**Mandatory output after every game request:**") == 1
        learn = re.findall(r"^\*\*Structured research export \(LEARN-v1\)\.\*\*.*$", s, re.M)
        runtime = re.findall(r"^\*\*Runtime, baseline and contract definitions \(RET-08 / RET-10 / RET-13\)\.\*\*.*$", s, re.M)
        assert len(learn) == 1 and len(runtime) == 1
        paragraphs.append((learn[0], runtime[0]))
    assert len(set(paragraphs)) == 1, "the LEARN-v1 and runtime paragraphs must be identical in every sport workflow"
    tennis = [s for s in sections if s.startswith("## Upcoming game — TENNIS")]
    assert len(tennis) == 1 and "python -m ml prospective rows --kind tennis" in tennis[0]
    assert sum("python -m ml prospective rows --kind tennis" in s for s in sections) == 1
