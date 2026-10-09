"""Settlement lint (GOV-03): a settlement's R1 must describe THIS card's ranking, and the rank index never calls a blank contract a push.

  python -B -m research.operations.settlement_lint addenda "prediction logs/PREDICTION_LOG_COMBINED_6.md" [more logs...]
  python -B -m research.operations.settlement_lint rank-log GAME_PREDICTION_RANK_LOG.csv

R1 ("Original prediction") is copied from the card. The refresh blocks written for P-539-P-545 repeated P-538's ranking, so the
lint (1) compares each "Rank N <text>" clause in R1 with the card's own proposition for rank N and (2) flags one R1 text reused
for two different cards. In the rank index a row graded `P` (push) needs a stated contract: a push is defined by a line. A blank
contract means the row is `UNKNOWN_CONTRACT` and must not be counted as a push.
"""
from __future__ import annotations
import argparse
import csv
import json
import re
import sys
from pathlib import Path

from research.operations.card_validator import markdown_tables

ROOT = Path(__file__).resolve().parents[2]
STOP = {'the', 'a', 'an', 'of', 'to', 'in', 'on', 'at', 'for', 'and', 'or', 'vs', 'v', 'full', 'game', 'incl', 'including', 'points', 'point', 'ml',
        'moneyline', 'rank', 'total', 'combined', 'team'}
RANK_CLAUSE = re.compile(r'Rank\s*(\d)\s*[:\-–]?\s*([^;\n]+?)(?=(?:;|\n|$|\.\s+[A-Z]))', re.I)
MIN_OVERLAP = 0.5


def tokens(text: str) -> set[str]:
    cleaned = re.sub(r'[*`_]', ' ', text.lower())
    return {t.rstrip('.') for t in re.findall(r'[a-z0-9.+\-−]+', cleaned) if t.rstrip('.') not in STOP and len(t.rstrip('.')) > 1}


def overlap(a: str, b: str) -> float:
    ta, tb = tokens(a), tokens(b)
    return len(ta & tb) / len(tb) if tb else 1.0


def card_propositions(card_text: str) -> dict[int, str]:
    """rank -> proposition from the card's own pick table (any header with a Rank column and a proposition/contract column)."""
    for _, header, rows in markdown_tables(card_text):
        lower = [h.lower() for h in header]
        if 'rank' not in lower:
            continue
        col = next((i for i, h in enumerate(lower) if 'proposition' in h or h in {'contract', 'exact contract', 'contract (issued)', 'issued contract'}), None)
        if col is None:
            continue
        out = {}
        for row in rows:
            rank = row[lower.index('rank')].strip('* `') if len(row) > lower.index('rank') else ''
            if rank.isdigit() and len(row) > col:
                out[int(rank)] = re.sub(r'[*`]', '', row[col]).strip()
        if out:
            return out
    return {}


def r1_text(settlement_text: str) -> str | None:
    match = re.search(r'(?ms)^(?:#{2,4}\s*R1\.[^\n]*\n|\*\*R1\.[^*]*\*\*)(.*?)(?=^(?:#{2,4}\s*R2\.|\*\*R2\.)|\Z)', settlement_text)
    return match[1].strip() if match else None


def check_r1(r1: str, propositions: dict[int, str]) -> list[str]:
    """Findings for an R1 text against the card's table. R1 without 'Rank N ...' clauses (for example 'ranks as issued above') is accepted."""
    findings = []
    for rank, clause in ((int(m[1]), m[2]) for m in RANK_CLAUSE.finditer(r1)):
        want = propositions.get(rank)
        if want is None:
            findings.append(f'R1 names rank {rank} but the card has no such row')
        elif overlap(clause, want) < MIN_OVERLAP:
            findings.append(f'R1 rank {rank} reads {clause.strip()!r} but the card ranks {want!r}')
    return findings


def normalise_r1(r1: str) -> str:
    return ' '.join(sorted(tokens(r1)))[:400]


def scan_addenda(log_paths: list[Path]) -> dict[str, list[str]]:
    """card id -> findings, over the research cards and dated addenda in the given logs."""
    cards: dict[str, dict[int, str]] = {}
    addenda: dict[str, list[str]] = {}
    for path in log_paths:
        text = Path(path).read_text(encoding='utf-8', errors='replace').replace('\r\n', '\n')
        for m in re.finditer(r'<!-- BEGIN CANONICAL RESEARCH (P-\d+) \S+ -->\n(.*?)<!-- END CANONICAL RESEARCH \1 ', text, re.S):
            props = card_propositions(m[2])
            if props:
                cards[m[1]] = props
        for m in re.finditer(r'<!-- BEGIN RESEARCH ADDENDUM (P-\d+) \S+ -->\n(.*?)<!-- END RESEARCH ADDENDUM \1 ', text, re.S):
            addenda.setdefault(m[1], []).append(m[2])
    findings: dict[str, list[str]] = {}
    seen_r1: dict[str, str] = {}
    for cid, blocks in sorted(addenda.items(), key=lambda kv: int(kv[0][2:])):
        for block in blocks:
            r1 = r1_text(block)
            if not r1:
                continue
            if cid in cards:
                for f in check_r1(r1, cards[cid]):
                    findings.setdefault(cid, []).append(f)
            key = normalise_r1(r1)
            if key and len(tokens(r1)) >= 6:
                if key in seen_r1 and seen_r1[key] != cid:
                    findings.setdefault(cid, []).append(f'R1 text is identical to the one written for {seen_r1[key]} (copy-paste)')
                seen_r1.setdefault(key, cid)
    return findings


# The five historical rows the retrospective found (F-GOV-4). They stay in the index literally, as issued; the lint reports any OTHER
# offender, so a new blank-contract push cannot be added unnoticed.
KNOWN_HISTORICAL = frozenset({('P-407', '1'), ('P-409', '2'), ('P-410', '5'), ('P-419', '5'), ('P-430', '5')})


def lint_rank_log(path: Path = ROOT / 'GAME_PREDICTION_RANK_LOG.csv', include_known: bool = False) -> list[dict]:
    """Rows graded P with no stated contract (the blank-contract-as-push defect); known historical rows only when asked."""
    bad = []
    with open(path, encoding='utf-8-sig', newline='') as handle:
        for line, row in enumerate(csv.DictReader(handle), start=2):
            if row['logged_result'].strip().upper() == 'P' and not row['selection_or_contract'].strip():
                known = (row['card_id'], row['rank']) in KNOWN_HISTORICAL
                if include_known or not known:
                    bad.append({'card': row['card_id'], 'rank': row['rank'], 'line': line, 'issue': 'BLANK_CONTRACT_ENCODED_AS_PUSH',
                                'should_read': 'UNKNOWN_CONTRACT', 'known_historical': known})
    return bad


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    a = sub.add_parser('addenda')
    a.add_argument('logs', nargs='+', type=Path)
    sub.add_parser('active', help='lint the active combined log (CI)')
    r = sub.add_parser('rank-log')
    r.add_argument('csv', type=Path, nargs='?', default=ROOT / 'GAME_PREDICTION_RANK_LOG.csv')
    r.add_argument('--all', action='store_true', help='include the five known historical rows')
    args = parser.parse_args(argv)
    if args.command == 'addenda':
        found = scan_addenda(args.logs)
        print(json.dumps(found, indent=1, ensure_ascii=False))
        return 1 if found else 0
    if args.command == 'active':
        from research.src.combined_log import active_log
        found = scan_addenda([active_log(ROOT)])
        print(json.dumps(found, indent=1, ensure_ascii=False))
        return 1 if found else 0
    bad = lint_rank_log(args.csv, include_known=args.all)
    print(json.dumps(bad, indent=1))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
