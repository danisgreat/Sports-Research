"""Active append destination, separate from immutable legacy Part-6 custody."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
LEGACY_PART6 = ROOT / 'prediction logs/PREDICTION_LOG_COMBINED_6.md'


def configuration(root=ROOT):
    path = Path(root) / 'research/current_combined_log.json'
    if not path.exists():
        return None
    config = json.loads(path.read_text(encoding='utf-8'))
    relative = config['active_log']
    match = re.fullmatch(r'prediction logs/PREDICTION_LOG_COMBINED_(\d+)\.md', relative)
    if not match or int(match[1]) < 7:
        raise ValueError('Invalid active combined-log destination')
    return config


def active_log(root=ROOT):
    config = configuration(root)
    return Path(root) / config['active_log'] if config else Path(root) / LEGACY_PART6.relative_to(ROOT)


def custody(path):
    # Import lazily: the certified issuer also uses this destination resolver.
    from .issue import _custody, BEGIN_ORIGINAL
    path = Path(path)
    raw = path.read_bytes()
    if BEGIN_ORIGINAL in raw:
        return _custody(path)
    root = path.parents[1]
    config = configuration(root)
    relative = path.relative_to(root).as_posix()
    headers = config.get('log_headers', {config['active_log']: config}) if config else {}
    if relative not in headers:
        raise ValueError('Unconfigured active combined-log destination')
    _custody(root / LEGACY_PART6.relative_to(ROOT))
    receipt = headers[relative]
    before = receipt['header_bytes']
    if len(raw) < before or hashlib.sha256(raw[:before]).hexdigest() != receipt['header_sha256']:
        raise ValueError('Active combined-log header custody changed')
    return raw, raw[before:]
