"""Collector lineage audits and the independence quorum (SRC-04).

Every registered collector is `UNKNOWN` independence until an audit says who actually collects the data it republishes. An audit is a small
JSON file `research/lineage_audits/<source_id>.json` (schema `lineage-audit-1`):

  source_id, audited_utc, terminal_collector (who first records the event), upstream_lineage_id, independence_status
  (INDEPENDENT | SHARED_FEED | UNKNOWN), shares_feed_with (source ids on the same feed), method, evidence[] (url, sha256 of the retained
  body, retrieved_utc with an offset, quote)

`INDEPENDENT` and `SHARED_FEED` both need at least one retained evidence item; `SHARED_FEED` names the sources it shares a feed with and
`INDEPENDENT` names none. The quorum for a league needs `n` DIFFERENT terminal collectors among its INDEPENDENT sources, at least one of
them official; shared feeds and unaudited sources contribute nothing. The tool performs no web access and cannot produce the audit
content: a person or a connected session reads the publisher's own documentation and retains the bodies.

  python -B -m research.operations.lineage_audit validate research/lineage_audits/mlb_official.json
  python -B -m research.operations.lineage_audit quorum [--league MLB] [--n 3]
  python -B -m research.operations.lineage_audit template SOURCE_ID      # prints an empty audit to fill in
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / 'research/sources_registry.json'
AUDIT_DIR = ROOT / 'research/lineage_audits'
STATUSES = ('INDEPENDENT', 'SHARED_FEED', 'UNKNOWN')
_HEX = re.compile(r'^[0-9a-f]{64}$')


def _aware(value) -> bool:
    try:
        return datetime.fromisoformat(str(value).replace('Z', '+00:00')).utcoffset() is not None
    except ValueError:
        return False


def validate(audit: dict, sources: dict | None = None) -> list[str]:
    errors: list[str] = []
    if audit.get('schema') != 'lineage-audit-1':
        errors.append('schema must be lineage-audit-1')
    sid = audit.get('source_id')
    if sources is not None and sid not in sources:
        errors.append(f'source_id {sid!r} is not in the source registry')
    status = audit.get('independence_status')
    if status not in STATUSES:
        errors.append(f'independence_status must be one of {STATUSES}')
    if not _aware(audit.get('audited_utc')):
        errors.append('audited_utc must be ISO 8601 with a UTC offset')
    if status in ('INDEPENDENT', 'SHARED_FEED'):
        for key in ('terminal_collector', 'upstream_lineage_id', 'method'):
            if not isinstance(audit.get(key), str) or not audit[key].strip():
                errors.append(f'{key} is required for a {status} audit')
        evidence = audit.get('evidence')
        if not isinstance(evidence, list) or not evidence:
            errors.append(f'a {status} audit needs at least one retained evidence item')
        else:
            for i, item in enumerate(evidence, 1):
                if not str(item.get('url', '')).startswith('https://'):
                    errors.append(f'evidence {i}: url must be https')
                if not _HEX.match(str(item.get('sha256', ''))):
                    errors.append(f'evidence {i}: sha256 must be 64 lowercase hex characters of the retained body')
                if not _aware(item.get('retrieved_utc')):
                    errors.append(f'evidence {i}: retrieved_utc must carry a UTC offset')
                if not str(item.get('quote', '')).strip():
                    errors.append(f'evidence {i}: quote the sentence that establishes the collector')
        shared = audit.get('shares_feed_with', [])
        if status == 'SHARED_FEED' and not shared:
            errors.append('SHARED_FEED must name the sources it shares a feed with')
        if status == 'INDEPENDENT' and shared:
            errors.append('INDEPENDENT must not list shares_feed_with')
        if sources is not None:
            for other in shared:
                if other not in sources:
                    errors.append(f'shares_feed_with names unknown source {other!r}')
    return errors


def load_audits(audit_dir: Path = AUDIT_DIR) -> dict[str, dict]:
    audits = {}
    for path in sorted(audit_dir.glob('*.json')) if audit_dir.exists() else []:
        obj = json.loads(path.read_text(encoding='utf-8'))
        if path.stem != obj.get('source_id'):
            raise ValueError(f'{path.name}: file name must equal source_id')
        audits[obj['source_id']] = obj
    return audits


def quorum(sources: dict, audits: dict[str, dict], league: str, n: int = 3) -> dict:
    """Is there an independent quorum of n distinct terminal collectors, one of them official, for the league?"""
    collectors: dict[str, list[str]] = {}
    official = False
    for sid, src in sources.items():
        if league not in src.get('leagues', []):
            continue
        audit = audits.get(sid)
        if not audit or validate(audit, sources) or audit['independence_status'] != 'INDEPENDENT':
            continue
        collectors.setdefault(audit['terminal_collector'].strip().lower(), []).append(sid)
        official = official or bool(src.get('official'))
    return {'league': league, 'required': n, 'distinct_collectors': len(collectors), 'collectors': collectors,
            'has_official': official, 'satisfied': len(collectors) >= n and official}


def template(source_id: str) -> dict:
    return {'schema': 'lineage-audit-1', 'source_id': source_id, 'audited_utc': '', 'terminal_collector': '', 'upstream_lineage_id': '',
            'independence_status': 'UNKNOWN', 'shares_feed_with': [], 'method': '',
            'evidence': [{'url': 'https://', 'sha256': '', 'retrieved_utc': '', 'quote': ''}]}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    v = sub.add_parser('validate')
    v.add_argument('files', nargs='+', type=Path)
    q = sub.add_parser('quorum')
    q.add_argument('--league')
    q.add_argument('--n', type=int, default=3)
    t = sub.add_parser('template')
    t.add_argument('source_id')
    args = parser.parse_args(argv)
    sources = json.loads(REGISTRY.read_text(encoding='utf-8'))['sources']
    if args.cmd == 'template':
        print(json.dumps(template(args.source_id), indent=2))
        return 0
    if args.cmd == 'validate':
        bad = 0
        for f in args.files:
            errs = validate(json.loads(f.read_text(encoding='utf-8')), sources)
            bad += bool(errs)
            print(json.dumps({'file': str(f), 'passed': not errs, 'errors': errs}))
        return 1 if bad else 0
    audits = load_audits()
    leagues = sorted({lg for s in sources.values() for lg in s.get('leagues', [])})
    print(json.dumps([quorum(sources, audits, lg, args.n) for lg in ([args.league] if args.league else leagues)], indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
