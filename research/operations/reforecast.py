"""Re-forecast trigger and dated addendum (PRD-06).

A confirmed starter, goalie or quarterback change - or a lineup change above a threshold - that becomes public AFTER the card's
research time and BEFORE the event starts stale-dates the card's ranks (P-274 and P-531 were both starter changes). The card itself
stays immutable and is what gets graded; the tool writes a dated `ADDENDUM` block with the trigger, its source and time, and a
re-forecast table that is explicitly diagnostic (its header is not the pick-table header, so `mini_log` accepts it as an addendum).

  python -B -m research.operations.reforecast check --type goalie --card-time T --event-start T --change-time T
  python -B -m research.operations.reforecast addendum --card P-NNN --type starter --change-time T --source "..." \
         --detail "..." --rows rows.json --out ADDENDUM.md
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KEY_ROLES = {'STARTER': 'confirmed starting pitcher change', 'GOALIE': 'confirmed starting goalie change',
             'QB': 'confirmed starting quarterback change'}
LINEUP_STARTERS_MIN = 2
LINEUP_SHARE_MIN = 0.20
REFORECAST_TABLE = ['Rank', 'Proposition', 'p_reforecast']
ISO = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?(Z|[+-]\d{2}:\d{2})$')


def parse_time(value: str) -> datetime:
    if not ISO.match(value):
        raise ValueError(f'{value!r} is not an ISO 8601 time with a UTC offset')
    return datetime.fromisoformat(value.replace('Z', '+00:00'))


def decide(change_type: str, card_time: str, event_start: str, change_time: str, starters_changed: int = 0, minutes_share_changed: float = 0.0) -> dict:
    """Whether a change obliges a re-forecast addendum.

    change_type: STARTER | GOALIE | QB (any confirmed change triggers) or LINEUP (>= 2 starters or >= 20% of expected minutes/possessions).
    The change must be public after the card's research time and before the event starts.
    """
    kind = change_type.upper()
    card, start, changed = parse_time(card_time), parse_time(event_start), parse_time(change_time)
    if kind in KEY_ROLES:
        material, reason = True, KEY_ROLES[kind]
    elif kind == 'LINEUP':
        material = starters_changed >= LINEUP_STARTERS_MIN or minutes_share_changed >= LINEUP_SHARE_MIN
        reason = (f'lineup change: {starters_changed} starters, {minutes_share_changed:.0%} of expected minutes '
                  f'(threshold {LINEUP_STARTERS_MIN} starters or {LINEUP_SHARE_MIN:.0%})')
    else:
        raise ValueError(f'unknown change type {change_type!r}; use STARTER, GOALIE, QB or LINEUP')
    if not changed > card:
        return {'reforecast': False, 'reason': 'the change was already public when the card was researched; it is in the original forecast'}
    if not changed < start:
        return {'reforecast': False, 'reason': 'the change became public after the event started; a pregame re-forecast is no longer possible',
                'late_information': True}
    return {'reforecast': material, 'reason': reason if material else f'below threshold: {reason}', 'late_information': False}


def addendum_block(card_id: str, change_type: str, change_time: str, source: str, detail: str, rows: list[dict], written_at: str) -> str:
    """The dated addendum markdown (a mini-log ADDENDUM block). `rows`: [{'proposition','p_reforecast'}] in the new rank order."""
    parse_time(written_at)
    parse_time(change_time)
    if not rows or any('proposition' not in r or not 0.0 < float(r['p_reforecast']) < 1.0 for r in rows):
        raise ValueError('rows need a proposition and a p_reforecast strictly between 0 and 1')
    lines = [f'<!-- BEGIN ADDENDUM {card_id} -->', f'### Addendum · {card_id} · {written_at}', '',
             f'**Re-forecast trigger:** {KEY_ROLES.get(change_type.upper(), "lineup change")} — public at {change_time}; source: {source}.', '',
             detail.strip(), '',
             '| ' + ' | '.join(REFORECAST_TABLE) + ' |', '|---|---|---|']
    for rank, row in enumerate(rows, 1):
        lines.append(f"| {rank} | {row['proposition']} | {100 * float(row['p_reforecast']):.1f}% |")
    lines += ['', 'The re-forecast is diagnostic. The original card above stays unchanged and is what gets graded.', f'<!-- END ADDENDUM {card_id} -->', '']
    return '\n'.join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    c = sub.add_parser('check')
    c.add_argument('--type', required=True)
    c.add_argument('--card-time', required=True)
    c.add_argument('--event-start', required=True)
    c.add_argument('--change-time', required=True)
    c.add_argument('--starters-changed', type=int, default=0)
    c.add_argument('--minutes-share', type=float, default=0.0)
    a = sub.add_parser('addendum')
    a.add_argument('--card', required=True)
    a.add_argument('--type', required=True)
    a.add_argument('--change-time', required=True)
    a.add_argument('--source', required=True)
    a.add_argument('--detail', required=True)
    a.add_argument('--rows', type=Path, required=True)
    a.add_argument('--written-at', required=True)
    a.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)
    if args.command == 'check':
        result = decide(args.type, args.card_time, args.event_start, args.change_time, args.starters_changed, args.minutes_share)
        print(json.dumps(result, indent=1))
        return 0 if not result['reforecast'] else 3
    rows = json.loads(args.rows.read_text(encoding='utf-8'))
    args.out.write_text(addendum_block(args.card, args.type, args.change_time, args.source, args.detail, rows, args.written_at), encoding='utf-8', newline='\n')
    print(json.dumps({'written': str(args.out)}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
