"""Settlement SLA (GOV-07): every card is settled within 72 h of its final, and open carryover stays at or below 5.

  python -B -m research.operations.settlement_sla MINI.md [--now 2026-10-14T09:00:00+11:00] [--max-carryover 5]

Applies to a mini-log that has not been settled yet. For each card the deadline is the scheduled start, plus a per-sport allowance for the
event to finish, plus 72 h. A card is `DUE` before its deadline and `BREACHED` after it. Carryover blocks in the mini count against the
cap of 5. The tool exits 1 on any breach or cap excess. The final-time allowance is deliberately generous; the evidence hierarchy
(A/B/C/E/OP/X) still applies, and an unfindable detail is settled as a literal gap rather than waited for (prompt 3).
"""
from __future__ import annotations
import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from research.operations import evidence_snapshot, mini_log

SLA_HOURS = 72
MAX_CARRYOVER = 5
ALLOWANCE_HOURS = {'baseball': 5, 'cricket': 12, 'tennis': 8, 'american football': 5, 'football': 4, 'soccer': 4, 'basketball': 4,
                   'ice hockey': 4, 'hockey': 4, 'rugby': 4, 'aussie rules': 4, 'australian football': 4}
DEFAULT_ALLOWANCE = 6


def allowance(sport: str) -> int:
    s = sport.lower()
    for key, hours in ALLOWANCE_HOURS.items():
        if key in s:
            return hours
    return DEFAULT_ALLOWANCE


def evaluate(raw: bytes, now: datetime, max_carryover: int = MAX_CARRYOVER) -> dict:
    cards, carryover = [], 0
    for block in mini_log.blocks(raw):
        if block['kind'] == 'CARRYOVER':
            carryover += 1
        elif block['kind'] == 'CARD':
            meta = mini_log.parse_card(block, 3)['meta']
            start = meta.get('Scheduled start', '')
            try:
                deadline = evidence_snapshot._moment(start) + timedelta(hours=allowance(meta.get('Sport', '')) + SLA_HOURS)
            except (ValueError, evidence_snapshot.EvidenceError):
                cards.append({'id': block['id'], 'state': 'NO_SCHEDULED_START'})
                continue
            cards.append({'id': block['id'], 'deadline': deadline.isoformat(), 'state': 'BREACHED' if now > deadline else 'DUE',
                          'hours_left': round((deadline - now).total_seconds() / 3600, 1)})
    breached = [c['id'] for c in cards if c['state'] == 'BREACHED']
    problems = [f'{i} is past its 72 h settlement deadline' for i in breached]
    if carryover > max_carryover:
        problems.append(f'{carryover} open carryover records exceed the cap of {max_carryover}')
    return {'cards': cards, 'open_carryover': carryover, 'problems': problems, 'passed': not problems}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('mini', type=Path)
    parser.add_argument('--now')
    parser.add_argument('--max-carryover', type=int, default=MAX_CARRYOVER)
    args = parser.parse_args(argv)
    now = evidence_snapshot._moment(args.now) if args.now else datetime.now(timezone.utc)
    result = evaluate(args.mini.read_bytes(), now, args.max_carryover)
    print(json.dumps(result, indent=1))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
