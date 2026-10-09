"""Append the final settlement to the active combined log (Part 7).

1. P-126..P-522 (no research-ledger parent) and P-538..P-549 (whose rollover verifier
   pins exactly 12 ledger addenda) are appended as one consolidated block under the
   canonical ledger writer lock, as on 2026-10-08. The block consumes no ID.
2. Ledger cards P-523..P-537 and P-550..P-556 each receive a dated addendum through
   research.operations.log_card.addendum. Addenda consume no ID.
Writes apply_receipt.json beside the table. Run from the repository root:
    python -B research/verification/final_settlement_2026-10-09/build/apply_settlement.py
"""
from __future__ import annotations
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from research.operations import log_card  # noqa: E402
from research.src.combined_log import active_log, custody  # noqa: E402
from research.src.issue import CANONICAL_LEDGER  # noqa: E402
from research.src.ledger import locked, read_records  # noqa: E402

BUILD = Path(__file__).resolve().parent
OUT = BUILD.parent
MARK = b'<!-- BEGIN FINAL SETTLEMENT 2026-10-09 -->'


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def main():
    part7 = active_log(ROOT)
    receipt = {'started_utc': datetime.now(timezone.utc).isoformat(),
               'active_log': part7.relative_to(ROOT).as_posix(),
               'next_id_before': log_card.next_id()}
    if receipt['next_id_before'] != 'P-557':
        raise SystemExit('unexpected next ID: ' + receipt['next_id_before'])
    ledger_before = CANONICAL_LEDGER.read_bytes()
    receipt.update(ledger_before_bytes=len(ledger_before), ledger_before_sha256=sha(ledger_before))
    block = (BUILD / 'older_block.md').read_bytes().decode('utf-8').replace('\r\n', '\n').replace('\n', '\r\n').encode('utf-8')
    with locked(CANONICAL_LEDGER):
        if log_card.pending(read_records(CANONICAL_LEDGER)):
            raise SystemExit('pending research transaction must be recovered first')
        before, _ = custody(part7)
        receipt.update(log_before_bytes=len(before), log_before_sha256=sha(before))
        if MARK in before:
            receipt['older_block'] = 'ALREADY_PRESENT'
        else:
            with part7.open('ab') as handle:
                handle.write(block)
                handle.flush()
                os.fsync(handle.fileno())
            after = part7.read_bytes()
            if not after.startswith(before) or after[len(before):] != block:
                raise SystemExit('consolidated block append did not verify')
            receipt['older_block'] = dict(bytes=len(block), sha256=sha(block), offset=len(before))
    results = []
    for request in sorted((BUILD / 'requests').glob('P-*.addendum.json')):
        card = json.loads(request.read_text(encoding='utf-8'))
        results.append(log_card.addendum(card))
    receipt['addenda'] = results
    after = part7.read_bytes()
    ledger_after = CANONICAL_LEDGER.read_bytes()
    receipt.update(log_after_bytes=len(after), log_after_sha256=sha(after),
                   ledger_after_bytes=len(ledger_after), ledger_after_sha256=sha(ledger_after),
                   ledger_records_added=len(read_records(CANONICAL_LEDGER)) - len(ledger_before.splitlines()),
                   next_id_after=log_card.next_id(), finished_utc=datetime.now(timezone.utc).isoformat(),
                   ids_consumed=0)
    if receipt['next_id_after'] != 'P-557':
        raise SystemExit('an ID was consumed unexpectedly')
    (OUT / 'apply_receipt.json').write_text(json.dumps(receipt, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({k: receipt[k] for k in ('next_id_before', 'next_id_after', 'log_before_bytes', 'log_after_bytes',
                                              'ledger_records_added', 'ids_consumed')}, indent=1))


if __name__ == '__main__':
    main()
