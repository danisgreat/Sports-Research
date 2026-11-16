"""Generated current state (STATE-v1, CR-2026.11.08-R2): the facts CURRENT_STATE.md used to keep by hand.

    python -m ml state            print the generated block
    python -m ml state --write    replace the block between the STATE markers in CURRENT_STATE.md
    python -m ml state --restamp  print VERSIONS.csv into every prompt file and CORE's version line (G-2, CR-2026.11.16-R2)

Every value is read from validated records: the highest canonical ID from the import mappings, the active mini and its
footer's next local key, the learning-store view and row counts, open local cards and frozen league-day events without a
settlement, the adjustment-ledger and adjustment-table rows, the shadow ledger, the effective-settlement view and the
release gate bindings. A test fails when the committed block differs from what this module generates.
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = "CURRENT_STATE.md"
VERSIONS = "VERSIONS.csv"
VERSION_ITEMS = ("method", "control_revision", "prompt_suite", "scoring", "selection")
CORE_LINE = re.compile(r"\*\*MDS-[^*\n]*? · CR-[^*\n]*? · P-[^*\n]*? · SCV-[^*\n]*? · SEL-[^*\n]*?\.\*\*")
BEGIN, END = "<!-- BEGIN GENERATED STATE (python -m ml state --write) -->", "<!-- END GENERATED STATE -->"
ACTIVE_POINTER = re.compile(r"\| Active local mini \| \[(research/active_minis/[^\]]+\.md)\]")


def _rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def versions(root=ROOT) -> dict:
    """The one place the release identities are written (VERSIONS.csv): item, current, previous."""
    rows = {r["item"]: r for r in _rows(Path(root) / VERSIONS)}
    if tuple(rows) != VERSION_ITEMS or any(not r["current"] for r in rows.values()):
        raise ValueError("VERSIONS.csv must list " + ", ".join(VERSION_ITEMS) + " with a current value each")
    return rows


def version_line(root=ROOT) -> str:
    v = versions(root)
    return "**" + " · ".join(v[i]["current"] for i in VERSION_ITEMS) + ".**"


def restamp(root=ROOT) -> list[str]:
    """Print the current versions where they are repeated: the suite version in every prompt file and CORE's version line.

    Only the previous suite string named in VERSIONS.csv is replaced, so dated history that cites older versions is kept.
    """
    root = Path(root)
    v = versions(root)
    changed = []
    old, new = v["prompt_suite"]["previous"], v["prompt_suite"]["current"]
    if old and old != new:
        for path in sorted((root / "research" / "prompts").rglob("*.md")):
            data = path.read_bytes()
            if old.encode() in data:
                path.write_bytes(data.replace(old.encode(), new.encode()))
                changed.append(path.relative_to(root).as_posix())
    core = root / "CORE.md"
    text = core.read_bytes().decode("utf-8")
    if len(CORE_LINE.findall(text)) != 1:
        raise ValueError("CORE.md must carry exactly one version line")
    fresh = CORE_LINE.sub(lambda _: version_line(root), text)
    if fresh != text:
        core.write_bytes(fresh.encode("utf-8"))
        changed.append("CORE.md")
    return changed


def highest_canonical(root=ROOT) -> int:
    ids = []
    for path in sorted((Path(root) / "research" / "verification").glob("mini_import_*/LOCAL_ID_MAPPING.csv")):
        ids += [int(m.group(1)) for r in _rows(path) if (m := re.fullmatch(r"P-(\d+)", r.get("canonical_id", "")))]
    return max(ids) if ids else 0


def active_mini(root=ROOT) -> Path | None:
    text = (Path(root) / STATE).read_text(encoding="utf-8")
    m = ACTIVE_POINTER.search(text)
    return Path(root) / m.group(1) if m else None


def mini_facts(mini: Path) -> dict:
    text = mini.read_text(encoding="utf-8")
    footer = text[text.rfind("<!-- BEGIN FOOTER -->"):] if "<!-- BEGIN FOOTER -->" in text else ""
    m = re.search(r"Last local event key / next local event key \| `([^`]+)` / `([^`]+)`", footer)
    cards = sorted(set(re.findall(r"<!-- BEGIN CARD (LOCAL-[A-Za-z0-9-]+-G\d{4}) -->", text)))
    if not cards:
        cards = sorted(set(re.findall(r"^## Card · (LOCAL-[A-Za-z0-9-]+-G\d{4})", text, flags=re.M)))
    settled = set(re.findall(r"BEGIN SETTLEMENT (LOCAL-[A-Za-z0-9-]+-G\d{4})", text))
    return dict(last_key=m.group(1) if m else "UNKNOWN", next_key=m.group(2) if m else "UNKNOWN", cards=cards,
                open_cards=[c for c in cards if c not in settled])


def league_day_open(root=ROOT) -> list[str]:
    """Frozen league-day events (cycle attempts) with no settlement feedback folder yet."""
    root = Path(root)
    attempts = sorted(p.name for p in (root / "research" / "cycle_attempts").glob("LOCAL-LEAGUE-*") if p.is_dir())
    feedback = {p.name.split("_REV")[0] for p in (root / "research" / "cycle_feedback").glob("*")} if (root / "research" / "cycle_feedback").exists() else set()
    return [a for a in attempts if a not in feedback]


def generate(root=ROOT) -> str:
    from ml import cycle, research_ingest as ri
    from ml.evaluation import effective_settlement as es
    root = Path(root)
    top = highest_canonical(root)
    mini = active_mini(root)
    if mini is None:  # no repository mini (CR-2026.11.12-R1): each research chat keeps its own
        facts = dict(last_key="NONE", next_key="NONE", cards=[], open_cards=[])
    else:
        facts = mini_facts(mini) if mini.exists() else dict(last_key="UNKNOWN", next_key="UNKNOWN", cards=[], open_cards=[])
    store = ri.load_store(root / "research" / "learning_store")
    ledger = _rows(root / "research" / "adjustment_ledger" / "ADJUSTMENT_LEDGER.csv")
    adjustments = _rows(root / "research" / "adjustment_ledger" / "ADJUSTMENTS.csv")
    from ml import chat
    shadow = _rows(root / chat.LEDGER)
    effective = es.effective_rows(root)
    unresolved = int((effective["sporting_grade"] == "UNRESOLVED").sum())
    releases = []
    for r in _rows(root / "research" / "cycle_releases" / "CURRENT_RELEASES.csv"):
        stale = "CURRENT_CODE" if _rows(root / r["release_path"])[0]["code_sha256"] == cycle.code_hash() else "STALE_FOR_CURRENT_CODE"
        releases.append(f"{r['active_experimental_release']} ({r['competition']}; {cycle.gate_binding(root / r['release_path'])}; {stale})")
    open_league = league_day_open(root)
    historical = sorted((root / "research/card_training").glob("*/ROWS.csv"))
    history_line = "No card-training run recorded"
    if historical:
        from ml.evidence_status import historical_summary
        counts, _, _ = historical_summary(historical[-1].parent)
        history_line = (f"{counts['historical_cards']} cards; {counts['admitted_contract_rows']} admitted contract rows, "
                        f"{counts['probability_rows']} with stated p; historical study, not prospective issuance")
    lines = [
        BEGIN,
        "",
        "*Generated from the records; do not edit by hand. A test fails if this block differs from `python -m ml state`.*",
        "",
        "| Item | Value |",
        "|---|---|",
        f"| Versions (from `{VERSIONS}`) | " + " · ".join(versions(root)[i]["current"] for i in VERSION_ITEMS) + " |",
        f"| Highest canonical ID / next | P-{top:03d} / **P-{top + 1:03d}** (from the import mappings) |",
        f"| Historical cards used for training | {history_line} |",
        f"| Active local mini | `{mini.relative_to(root).as_posix() if mini else 'NONE'}`; last / next local key `{facts['last_key']}` / `{facts['next_key']}` (footer) |",
        f"| Open cards in the active mini | {len(facts['open_cards'])} of {len(facts['cards'])}: " + (", ".join(f"`{c}`" for c in facts["open_cards"]) or "none") + " |",
        f"| Frozen league-day events without settlement | {len(open_league)}: " + (", ".join(f"`{c}`" for c in open_league) or "none") + " |",
        f"| Learning store | view {store.view_seq}; {len(store.events)} events, {len(store.results)} results, "
        f"{len(store.team_game_stats)} team-statistic rows, {len(store.player_availability)} player-availability rows |",
        f"| Adjustment ledger | {len(ledger)} contract rows on {len({r['local_key'] for r in ledger})} cards; {len(adjustments)} adjustment rows |",
        f"| Prospective shadow ledger | {len(shadow)} frozen rows on {len({r['event_id'] for r in shadow})} events (`{chat.LEDGER}`) |",
        f"| Effective settlements (imported local-key rows) | {len(effective)} rows, {int((effective['revision_source'] != '').sum())} revised by settlement imports, {unresolved} UNRESOLVED |",
        f"| Permanently closed unattainable contracts | {len(_rows(root / 'research/historical_resolution/PERMANENT_CLOSURES.csv'))} exact rows; DO_NOT_RETRY; excluded from sporting scores |",
        "| Active releases | " + ("; ".join(releases) or "none") + " |",
        "",
        END,
    ]
    return "\n".join(lines)


def write(root=ROOT) -> bool:
    path = Path(root) / STATE
    text = path.read_bytes().decode("utf-8")
    block = generate(root)
    if BEGIN in text and END in text:
        new = text[:text.index(BEGIN)] + block + text[text.index(END) + len(END):]
    else:
        anchor = "| Item | Value |"
        if anchor not in text:
            raise ValueError("CURRENT_STATE.md has no state table to place the generated block before")
        new = text.replace(anchor, block + "\n\n**Versions and pointers (hand-maintained):**\n\n" + anchor, 1)
    # Legacy readers still consume these rows. Generate them from the same
    # registry rather than leaving a second, hand-maintained current version.
    labels={"Method":"method","Control revision":"control_revision","Scoring":"scoring","Scoring version":"scoring","Selection":"selection","Selection version":"selection","Prompt suite":"prompt_suite"}
    v=versions(root)
    for label,item in labels.items():
        new=re.sub(r"(?m)^\| "+re.escape(label)+r" \|[^\n]*$",lambda _:f"| {label} | {v[item]['current']} (generated from VERSIONS.csv) |",new)
    changed = new != text
    if changed:
        path.write_bytes(new.encode("utf-8"))
    return changed


def committed_block(root=ROOT) -> str | None:
    text = (Path(root) / STATE).read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        return None
    return text[text.index(BEGIN): text.index(END) + len(END)]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--restamp", action="store_true", help="print VERSIONS.csv into the prompt files and CORE's version line")
    args = parser.parse_args(argv)
    if args.restamp:
        print("restamped: " + (", ".join(restamp()) or "nothing to change"))
    elif args.write:
        print("CURRENT_STATE.md updated" if write() else "CURRENT_STATE.md already current")
    else:
        print(generate())


if __name__ == "__main__":
    main()
