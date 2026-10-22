"""Prompt-suite consistency (Improvement 28): versions, links, dependency map and prompt-1 sport files.

Owner-entered Upcoming game blocks are never compared to a fixed text: their contents change with every game.
Prompt 1 is a core file plus one sport file per sport in research/prompts/1_sports/ (P-2026.10.17-v22.1); all prompts run here and freeze the reference before the card (P-2026.10.22-v24.0).
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


SHARED_TITLES = ("Analyst primary probability (ANALYST_PRIMARY_V1, v24.0).", "Learning record (LEARN-v2).",
                 "Contract definitions and comparator (RET-10 / RET-13).", "Mandatory output after every game request:",
                 "Pricing basis (PR-03).", "Retain the research (RETAIN-v3).", "Strict research completion (RC-2026.10.16-v2).",
                 "Current evidence requirement:")


def test_prompt1_core_holds_the_shared_steps_and_indexes_eleven_sport_files():
    core = text("1_GAME_CARD")
    assert len(SPORT_FILES) == 11
    assert all(f"]({name}.md)" in core for name in SPORT_FILES), "the core must link every sport file"
    assert "Upcoming game — " not in core, "Upcoming game blocks live in the sport files"
    assert core.count("**Reference stage and card freeze (MLSCOPE-v3).**") == 1
    shared = core[core.index("## Shared steps for every sport"):]
    for title in SHARED_TITLES:
        assert len(re.findall(r"^\*\*" + re.escape(title) + r"\*\*", shared, re.M)) == 1, f"core must hold {title} once"
    for step in ("Before step 1", "Step 1 —", "Step 3 —", "Step 4 —", "Step 5 —", "Step 7 —"):
        assert f"### {step}" in shared
    for name in SPORT_FILES:
        s = text(name)
        assert "](../1_GAME_CARD.md)" in s, f"{name}: must point to the core"
        assert len(re.findall(r"^(## )?Upcoming game — ", s, re.M)) == 1, f"{name}: exactly one Upcoming game block"
        assert re.search(r"^Read \[COMMON_OPERATING_PROTOCOL\]", s, re.M), "each Upcoming block is followed by Read"
        assert all(len(re.findall(rf"^## {n}\. ", s, re.M)) == 1 for n in range(1, 8)), f"{name}: steps 1-7 keep their headings"
        assert not any(re.search(r"^\*\*" + re.escape(t) + r"\*\*", s, re.M) for t in SHARED_TITLES), f"{name}: shared rule duplicated"
        assert s.count("shared rules ([prompt 1 core](../1_GAME_CARD.md))") == 5, f"{name}: steps 1, 3, 4, 5 and 7 point to the core"


def test_prompt1_freezes_the_reference_before_the_card_and_the_card_after_it():
    """MLSCOPE-v3: the reference is frozen before any probability is typed; the card is written and read back, then its own p is frozen."""
    core = text("1_GAME_CARD")
    stage = core.index("**Reference stage and card freeze (MLSCOPE-v3).**")
    block = core[stage:core.index("\n", stage)]
    assert "Before any probability is typed" in block and "python -m ml pregame reference" in block
    assert "The reference is never edited." in block
    assert "read no other model, shadow, cycle or decision-lab output and no benchmark" in block
    assert "`python -m ml pregame run --mini" in block and "freezes the card's own final p" in block
    assert block.index("python -m ml pregame reference") < block.index("python -m ml pregame run --mini")
    step7 = core[core.index("### Step 7 \u2014"):]
    assert step7.index("Insert one complete local-key card") < step7.index("Then freeze the card with the pregame command")
    assert step7.index("python -m ml card lint") < step7.index("Insert one complete local-key card")


@pytest.mark.parametrize("name", ["2_START_LOCAL_MINI", "5_START_THE_NEXT_COMBINED_LOG"] + SPORT_FILES)
def test_prompts_without_a_model_step_give_no_model_commands(name):
    body = text(name)
    assert not re.search(r"`python -m ml |python -m ml ", body), f"{name} runs no model"
    assert "PRIMARY_PREDICTION_PROTOCOL" not in body


@pytest.mark.parametrize("name", ["1_GAME_CARD", "2_START_LOCAL_MINI", "3_SETTLE_LOCAL_MINI"] + SPORT_FILES)
def test_game_prompts_run_in_the_working_tree(name):
    """ENV-v2: prompts 1-3 run in this repository, read local controls and write their own files."""
    body = text(name)
    assert "LOCAL_WORKING_TREE" in body
    assert "**EXTERNAL_CHAT**" not in body and "PUBLISHED_MAIN_PINNED`) (EXTERNAL_CHAT)" not in body
    if not name.startswith("1_sports/"):
        assert "EXECUTION_ENVIRONMENT_PROTOCOL" in body and "ENV-v2" in body


def test_canonical_ids_are_assigned_in_the_settlement_phase():
    settle, imp = text("3_SETTLE_LOCAL_MINI"), text("4_CANONICAL_IMPORT")
    assert "## 6. Settlement-phase canonical assignment" in settle and "cycle settle" in settle
    assert "## 0. Intake (ENV-v2)" in imp and "PENDING_PROMPT_4" in imp
