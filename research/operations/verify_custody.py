"""Strict custody readback with complete source failures and unchanged originals.

Quarantined bodies are required, even in a clean checkout. Missing evidence
never becomes a passing check. Pinned acceptance/model code is not rewritten.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from unittest.mock import patch

from research.src import acceptance
from research.src.custody_text import custody_bytes, windows_path
from research.src.sources import verified_body
from research.src.ledger import read_records
from research.src.issue import CANONICAL_LEDGER, PART6
from research.operations.log_card import research_cards, verify_projection, next_id


def compatible_body(receipt, root):
    if not isinstance(receipt, dict):
        raise ValueError('source receipt must be a JSON object')
    if 'response_sha256' not in receipt and 'content_sha256' in receipt:
        receipt = {**receipt, 'response_sha256': receipt['content_sha256'],
                   'body_path': receipt['stored_snapshot_path'],
                   'source_url': receipt.get('url')}
    if '\\' in str(receipt.get('body_path', '')):                                  # a Windows-recorded relative path, read on any platform
        receipt = {**receipt, 'body_path': windows_path(receipt['body_path']).as_posix()}
    raw = verified_body(receipt, root)
    if 'response_bytes' in receipt and len(raw) != receipt['response_bytes']:
        raise ValueError('retained source body length mismatch')
    return raw


def audit_sources(receipt_dir, root):
    """Check every receipt, preserving all failures instead of stopping at one."""
    rows = []
    for path in sorted(Path(receipt_dir).glob('*.json')):
        row = {'receipt_path': path.relative_to(root).as_posix(), 'verified': False}
        try:
            receipt = json.loads(path.read_text(encoding='utf-8-sig'))
            if not isinstance(receipt, dict):
                raise ValueError('source receipt must be a JSON object')
            row.update(body_path=receipt.get('body_path', receipt.get('stored_snapshot_path')),
                       expected_sha256=receipt.get('response_sha256', receipt.get('content_sha256')),
                       market_quarantined=bool(receipt.get('market_quarantined')))
            raw = compatible_body(receipt, root)
            row.update(verified=True, verified_bytes=len(raw))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            row.update(error_type=type(exc).__name__, error=str(exc))
        rows.append(row)
    return rows


def run():
    root = PART6.parents[1]
    sources = audit_sources(root/'research/data/source_receipts', root)
    failures = [row for row in sources if not row['verified']]
    # Acceptance only verifies these body bytes; it does not parse or use them.
    # Collect each error while letting its other invariants run. A failed body
    # always contributes an issue and makes the final result invalid.
    body_issues = []

    def collect_body(receipt, evidence_root):
        try:
            return compatible_body(receipt, evidence_root)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            path = receipt.get('body_path', receipt.get('stored_snapshot_path')) if isinstance(receipt, dict) else 'INVALID_SCHEMA'
            body_issues.append(f'SOURCE_BODY_INVALID:{path}:{type(exc).__name__}')
            return b''

    def custody_sha(path):
        # Parts 1-5 and the rank CSV were hashed over CRLF bytes; hash the same bytes on an LF checkout (GOV-02).
        return hashlib.sha256(custody_bytes(Path(path))).hexdigest()

    try:
        with patch.object(acceptance, 'verified_body', collect_body), patch.object(acceptance, 'sha', custody_sha):
            result = acceptance.run()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result = {'observed_utc': datetime.now(timezone.utc).isoformat(), 'valid': False,
                  'checks': {}, 'issues': [f'ACCEPTANCE_FAILED:{type(exc).__name__}:{exc}'],
                  'limitation': 'Incomplete acceptance; no custody or predictive certification.'}
    result['issues'].extend(body_issues)
    result['issues'].extend('SOURCE_RECEIPT_INVALID:'+row['receipt_path'] for row in failures)
    try:
        cards = research_cards(read_records(CANONICAL_LEDGER))
        for card in cards:
            verify_projection(card, PART6)
        result['checks'].update(canonical_research_cards=[c['card_id'] for c in cards],
                                research_next_id=next_id())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result['issues'].append(f'CANONICAL_CUSTODY_FAILED:{type(exc).__name__}:{exc}')
    result['checks'].update(source_receipts_examined=len(sources),
                            source_receipt_bodies_verified=len(sources)-len(failures),
                            source_receipt_body_failures=len(failures),
                            receipt_schema_adapter='IN_MEMORY_ONLY_NO_SOURCE_REWRITES')
    result['source_body_failures'] = failures
    result['valid'] = result['valid'] and not result['issues']
    result['limitation'] += (' Research IDs are canonical storage identities, not certified prospective ISSUE records.'
                            ' Quarantined bodies remain mandatory; absent or damaged bytes fail this check.')
    return result


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(not result['valid'])
