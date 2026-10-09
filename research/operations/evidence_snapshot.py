"""Retained pregame evidence and settlement-field captures (SRC-03, SRC-02).

A card's lineup, goalie, injury and weather claims, and its settlement fields (corners, half-time, periods, players), live on pages that
change or disappear. This tool stores the bytes received, hashes them and prints the token that goes into the card's
`Evidence snapshots` field:  sha256:<64 hex>@<ISO time with offset>

Two kinds share one store, `research/data/raw/evidence/<kind>/`:
  evidence   pregame pages used on a card (kind of claim: lineup, goalie, injury, weather, ...)
  capture    post-game settlement-field pages (SRC-02), recorded against the card they will settle

Each stored item is `<key>_<sha12>.body` (the bytes verbatim; gitignored because publisher text may not be redistributable) and a
tracked receipt `<key>_<sha12>.json` (sha256, url, retrieved time, byte count, claim). A hashed text extract (`--extract`) can stand in for
a body that may not be retained: the receipt then says `retained: EXTRACT` and the hash is of the extract.

  python -B -m research.operations.evidence_snapshot store --kind evidence --key P-900-goalie --file page.html --url https://... [--claim "NHL confirmed goalie"] [--retrieved 2026-10-10T08:41:00+11:00] [--extract]
  python -B -m research.operations.evidence_snapshot verify-card MINI.md [--require-bodies]
  python -B -m research.operations.evidence_snapshot verify-store [--require-bodies]

`verify-card` checks that every `Evidence snapshots` token on every card resolves to a stored receipt with the same hash and a retrieval time
at or before the card's research-completed time; `--require-bodies` also re-hashes the retained body.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from research.operations import mini_log

ROOT = Path(__file__).resolve().parents[2]
STORE = ROOT / 'research/data/raw/evidence'
KINDS = ('evidence', 'capture')
_KEY = re.compile(r'^[A-Za-z0-9][A-Za-z0-9._\-]*$')
TOKEN = re.compile(r'^sha256:([0-9a-f]{64})@(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:\d{2}))$')


class EvidenceError(ValueError):
    pass


def _moment(value: str) -> datetime:
    m = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if m.tzinfo is None or m.utcoffset() is None:
        raise EvidenceError('time needs a UTC offset')
    return m


def store(kind: str, key: str, body: bytes, url: str, retrieved: str | None = None, claim: str = '', extract: bool = False,
          root: Path = STORE) -> dict:
    if kind not in KINDS:
        raise EvidenceError(f'kind must be one of {KINDS}')
    if not _KEY.match(key):
        raise EvidenceError('key may contain letters, digits, ".", "_" and "-"')
    if not body:
        raise EvidenceError('an empty page is not evidence')
    if not url.startswith('https://'):
        raise EvidenceError('url must be https')
    when = retrieved or datetime.now(timezone.utc).isoformat()
    _moment(when)
    digest = hashlib.sha256(body).hexdigest()
    directory = root / kind
    directory.mkdir(parents=True, exist_ok=True)
    stem = f'{key}_{digest[:12]}'
    receipt = {'schema': 'evidence-receipt-1', 'kind': kind, 'key': key, 'sha256': digest, 'bytes': len(body), 'url': url,
               'retrieved_utc': when, 'claim': claim, 'retained': 'EXTRACT' if extract else 'BODY',
               'token': f'sha256:{digest}@{when}'}
    with (directory / (stem + '.body')).open('xb') as handle:
        handle.write(body)
    with (directory / (stem + '.json')).open('x', encoding='utf-8') as handle:
        json.dump(receipt, handle, indent=2, sort_keys=True)
        handle.write('\n')
    return receipt


def receipts(root: Path = STORE) -> list[dict]:
    out = []
    for path in sorted(root.glob('*/*.json')) if root.exists() else []:
        obj = json.loads(path.read_text(encoding='utf-8'))
        obj['_path'] = path
        out.append(obj)
    return out


def verify_store(root: Path = STORE, require_bodies: bool = False) -> list[str]:
    problems = []
    for r in receipts(root):
        path: Path = r['_path']
        if r.get('schema') != 'evidence-receipt-1' or not re.match(r'^[0-9a-f]{64}$', str(r.get('sha256', ''))):
            problems.append(f'{path.name}: malformed receipt')
            continue
        if r['token'] != f"sha256:{r['sha256']}@{r['retrieved_utc']}":
            problems.append(f'{path.name}: token does not match sha256 and retrieved_utc')
        body = path.with_suffix('.body')
        if body.exists():
            if hashlib.sha256(body.read_bytes()).hexdigest() != r['sha256']:
                problems.append(f'{path.name}: retained body no longer matches its hash')
        elif require_bodies:
            problems.append(f'{path.name}: retained body is missing')
    return problems


def verify_card_text(raw: bytes, root: Path = STORE, require_bodies: bool = False) -> dict:
    """Check every `Evidence snapshots` token on every v3 card in a mini-log or combined-log text."""
    index = {(r['sha256'], r['retrieved_utc']): r for r in receipts(root)}
    by_hash = {r['sha256']: r for r in receipts(root)}
    problems, checked = [], 0
    for block in mini_log.blocks(raw):
        if block['kind'] != 'CARD':
            continue
        card = mini_log.parse_card(block, 3)
        value = card['meta'].get('Evidence snapshots', '')
        if not value or value == 'NONE':
            continue
        done = card['meta'].get('Research completed', '')
        for item in [s.strip() for s in value.split(';') if s.strip()]:
            m = TOKEN.match(item)
            if not m:
                problems.append(f'{block["id"]}: malformed token {item!r}')
                continue
            checked += 1
            receipt = index.get((m[1], m[2])) or by_hash.get(m[1])
            if receipt is None:
                problems.append(f'{block["id"]}: snapshot {m[1][:12]} has no stored receipt')
                continue
            if _moment(receipt['retrieved_utc']) != _moment(m[2]):
                problems.append(f'{block["id"]}: snapshot {m[1][:12]} time {m[2]} differs from the receipt {receipt["retrieved_utc"]}')
            if done and _moment(receipt['retrieved_utc']) > _moment(done):
                problems.append(f'{block["id"]}: snapshot {m[1][:12]} was retrieved after the research was completed')
            body = receipt['_path'].with_suffix('.body')
            if require_bodies and not body.exists():
                problems.append(f'{block["id"]}: retained body for {m[1][:12]} is missing')
            elif body.exists() and hashlib.sha256(body.read_bytes()).hexdigest() != m[1]:
                problems.append(f'{block["id"]}: retained body for {m[1][:12]} no longer matches its hash')
    return {'checked_tokens': checked, 'problems': problems, 'passed': not problems}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('store')
    s.add_argument('--kind', choices=KINDS, required=True)
    s.add_argument('--key', required=True)
    s.add_argument('--file', type=Path, required=True)
    s.add_argument('--url', required=True)
    s.add_argument('--claim', default='')
    s.add_argument('--retrieved')
    s.add_argument('--extract', action='store_true')
    v = sub.add_parser('verify-card')
    v.add_argument('mini', type=Path)
    v.add_argument('--require-bodies', action='store_true')
    w = sub.add_parser('verify-store')
    w.add_argument('--require-bodies', action='store_true')
    args = parser.parse_args(argv)
    if args.cmd == 'store':
        receipt = store(args.kind, args.key, args.file.read_bytes(), args.url, args.retrieved, args.claim, args.extract)
        print(receipt['token'])
        return 0
    if args.cmd == 'verify-card':
        result = verify_card_text(args.mini.read_bytes(), require_bodies=args.require_bodies)
    else:
        problems = verify_store(require_bodies=args.require_bodies)
        result = {'passed': not problems, 'problems': problems}
    print(json.dumps(result, indent=1))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
