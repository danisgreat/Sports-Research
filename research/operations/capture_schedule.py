"""Settlement-field capture schedule (SRC-02).

A card that prices a corners, half-time, period or player row names the exact provider in `Settlement fields` and a `Capture due` time
(by default within 24 h of the start, before the route rots). This tool turns the cards of a mini-log into that schedule, reports which
captures are done (a `capture` receipt stored with `evidence_snapshot store --kind capture --key P-NNN...`), which are due and which are
overdue, and exits non-zero when a capture is overdue.

  python -B -m research.operations.capture_schedule MINI.md [--now 2026-10-11T12:00:00+11:00] [--receipts DIR]

A done capture is any stored capture receipt whose key starts with the card's ID. `--now` defaults to the current time.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from research.operations import evidence_snapshot, mini_log


def schedule(raw: bytes, now: datetime, root: Path = evidence_snapshot.STORE) -> list[dict]:
    captured = {m[1] for r in evidence_snapshot.receipts(root) if r['kind'] == 'capture' for m in [re.match(r'(P-\d{3,})', r['key'])] if m}
    rows = []
    for block in mini_log.blocks(raw):
        if block['kind'] != 'CARD':
            continue
        card = mini_log.parse_card(block, 3)
        meta = card['meta']
        due_text = meta.get('Capture due', '')
        if not due_text:
            rows.append({'id': block['id'], 'state': 'NO_SCHEDULE', 'fields': meta.get('Settlement fields', ''), 'due': None})
            continue
        due = evidence_snapshot._moment(due_text)
        if block['id'] in captured:
            state = 'DONE'
        else:
            state = 'OVERDUE' if now > due else 'PENDING'
        rows.append({'id': block['id'], 'event': card['heading'], 'fields': meta.get('Settlement fields', ''), 'start': meta.get('Scheduled start'),
                     'due': due_text, 'state': state, 'hours_to_due': round((due - now).total_seconds() / 3600, 1)})
    return rows


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('mini', type=Path)
    parser.add_argument('--now')
    parser.add_argument('--receipts', type=Path, default=evidence_snapshot.STORE)
    args = parser.parse_args(argv)
    now = evidence_snapshot._moment(args.now) if args.now else datetime.now(timezone.utc)
    rows = schedule(args.mini.read_bytes(), now, args.receipts)
    print(json.dumps(rows, indent=1))
    return 1 if any(r['state'] == 'OVERDUE' for r in rows) else 0


if __name__ == '__main__':
    sys.exit(main())
