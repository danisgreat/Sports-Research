"""Read the selected, hash-bound settlement register without reissuing IDs.

The pointer `research/current_settlement_register.json` names the CURRENT register and, in `history`, every register it
superseded, each with its SHA-256. Dated verifiers (GOV-01) therefore check the snapshot they were written for by hash through
`pinned`, and ask only whether that snapshot is in the pointer's lineage (`in_lineage`), instead of requiring it to be the
current selection - which made every legitimate settlement update break them.

Two register kinds exist: `carryover` (open requirements per event, schema 1) and `settled` (final settlement of every record,
schema 2). A pointer without `kind` is a `carryover` pointer.
"""
import hashlib
import json
from pathlib import Path

KINDS = ('carryover', 'settled')
CARRYOVER_KEYS = ('event', 'competition', 'original_scheduled_start', 'current_state', 'unresolved_contracts_or_fields',
                  'remaining_requirement', 'canonical_pointer', 'source_custody_notes')
SETTLED_KEYS = ('event', 'state', 'card_outcome')


def _pointer(root):
    path = Path(root).resolve() / 'research/current_settlement_register.json'
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else None


def _load(root, relative, expected_sha):
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root / 'research/verification'):
        raise ValueError('Settlement manifest outside verification store')
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_sha:
        raise ValueError('Selected settlement manifest changed')
    return json.loads(raw)


def _validate(manifest, kind):
    rows = manifest['records']
    ids = [r['canonical_id'] for r in rows]
    if len(ids) != len(set(ids)) or manifest['event_count'] != len(rows):
        raise ValueError('Duplicate or incomplete settlement coverage')
    for r in rows:
        if kind == 'carryover':
            for key in CARRYOVER_KEYS:
                if not r.get(key):
                    raise ValueError('Incomplete settlement carryover: ' + r['canonical_id'] + ':' + key)
        else:
            for key in SETTLED_KEYS:
                if not r.get(key):
                    raise ValueError('Incomplete final settlement: ' + r['canonical_id'] + ':' + key)
        if r.get('performance_eligible') is not False:
            raise ValueError('Historical settlement admission cannot be inferred from register')
    if kind == 'settled' and not isinstance(manifest.get('open_sporting_settlements'), int):
        raise ValueError('A settled register states its open_sporting_settlements count')
    reservations = manifest.get('local_reservations', [])
    reserved_ids = [r.get('local_id') for r in reservations]
    if len(reserved_ids) != len(set(reserved_ids)) or set(reserved_ids) & set(ids):
        raise ValueError('Local reservation duplicated or counted as reviewed canonical event')
    for r in reservations:
        if r.get('status') != 'LOCAL_ONLY_PENDING_IMPORT' or not all(r.get(k) for k in
                ('native_event_id', 'tracking_alias', 'source_path', 'source_sha256', 'next_local_working_id')):
            raise ValueError('Incomplete local-only reservation')


def lineage(root):
    """Oldest-to-newest [{manifest_path, manifest_sha256, kind}] ending with the current selection (empty without a pointer)."""
    config = _pointer(root)
    if config is None:
        return []
    older = [{'manifest_path': h['manifest_path'], 'manifest_sha256': h['manifest_sha256'], 'kind': h.get('kind', 'carryover')}
             for h in config.get('history', [])]
    return older + [{'manifest_path': config['manifest_path'], 'manifest_sha256': config['manifest_sha256'], 'kind': config.get('kind', 'carryover')}]


def in_lineage(root, manifest_path):
    return any(entry['manifest_path'] == manifest_path for entry in lineage(root))


def pinned(root, manifest_path):
    """A dated snapshot verified by the SHA-256 the pointer recorded for it, whether or not it is still the current selection."""
    for entry in lineage(root):
        if entry['manifest_path'] == manifest_path:
            manifest = _load(root, manifest_path, entry['manifest_sha256'])
            _validate(manifest, entry['kind'])
            return manifest
    raise ValueError(f'{manifest_path} is not in the settlement-register lineage')


def selected(root):
    config = _pointer(root)
    if config is None:
        return None
    kind = config.get('kind', 'carryover')
    if kind not in KINDS:
        raise ValueError('Unknown settlement register kind: ' + str(kind))
    manifest = _load(root, config['manifest_path'], config['manifest_sha256'])
    _validate(manifest, kind)
    for entry in lineage(root)[:-1]:                       # every superseded snapshot must still match its recorded hash
        _load(root, entry['manifest_path'], entry['manifest_sha256'])
    return {**config, 'kind': kind, 'manifest': manifest}
