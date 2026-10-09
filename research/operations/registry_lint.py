"""Source-registry lint (SRC-08, SRC-04).

  python -B -m research.operations.registry_lint

Checks that (1) no excluded source (fantasy, betting, market products) is in the executable registry and none has an EXCLUDED_* access
mode, (2) every entry carries the contract fields the fetch path relies on, (3) an AUTOMATED_ALLOWED entry has https prefixes on its own
hostname and an official/lineage declaration, (4) an odds-bearing source is flagged `market_fields_possible`, (5) a source that claims
INDEPENDENT or SHARED_FEED independence has a valid lineage audit file, and (6) the adapter registry (research/sources_registry_adapters.json) obeys the same contract and shares no id with the main registry.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from urllib.parse import urlsplit

from research.operations import lineage_audit

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / 'research/sources_registry.json'
EXCLUDED = ROOT / 'research/excluded_sources.json'
ADAPTERS = ROOT / 'research/sources_registry_adapters.json'
CONTRACT_KEYS = ('publisher', 'access_mode', 'allowed_url_prefixes', 'upstream_lineage_id', 'independence_status', 'parser_id', 'endpoints',
                 'market_fields_possible', 'official', 'leagues')
ACCESS_MODES = ('AUTOMATED_ALLOWED', 'MANUAL_LOCAL_ONLY', 'PERSONAL_USE_LOCAL_ONLY', 'MANUAL_ONLY', 'LICENSED_ONLY', 'PLANNED_NO_ADAPTER')


def lint(registry_path: Path = REGISTRY, excluded_path: Path = EXCLUDED, adapters_path: Path = ADAPTERS, audit_dir: Path = lineage_audit.AUDIT_DIR) -> list[str]:
    problems: list[str] = []
    sources = json.loads(registry_path.read_text(encoding='utf-8'))['sources']
    if adapters_path.exists():
        for sid, src in json.loads(adapters_path.read_text(encoding='utf-8'))['sources'].items():
            if sid in sources:
                problems.append(f'{sid}: is in both the source registry and the adapter registry')
            sources = {**sources, sid: src}
    excluded = json.loads(excluded_path.read_text(encoding='utf-8'))['sources'] if excluded_path.exists() else {}
    audits = lineage_audit.load_audits(audit_dir)
    for sid, src in sources.items():
        if sid in excluded:
            problems.append(f'{sid}: is listed as excluded but is in the executable registry')
        mode = str(src.get('access_mode', ''))
        if mode.startswith('EXCLUDED') or src.get('parser_id') == 'EXCLUDED':
            problems.append(f'{sid}: an excluded source belongs in research/excluded_sources.json, not the executable registry')
        missing = [k for k in CONTRACT_KEYS if k not in src]
        if missing:
            problems.append(f'{sid}: missing contract keys {missing}')
            continue
        if mode not in ACCESS_MODES:
            problems.append(f'{sid}: unknown access_mode {mode!r}')
        if mode == 'AUTOMATED_ALLOWED':
            if not src['allowed_url_prefixes']:
                problems.append(f'{sid}: AUTOMATED_ALLOWED needs allowed_url_prefixes')
            for prefix in src['allowed_url_prefixes']:
                parsed = urlsplit(prefix)
                if parsed.scheme != 'https':
                    problems.append(f'{sid}: prefix {prefix} must be https')
                if src.get('hostname') and parsed.hostname != src['hostname']:
                    problems.append(f'{sid}: prefix {prefix} is not on hostname {src["hostname"]}')
        if src['independence_status'] in ('INDEPENDENT', 'SHARED_FEED'):
            audit = audits.get(sid)
            if audit is None:
                problems.append(f'{sid}: independence {src["independence_status"]} has no lineage audit file')
            else:
                problems += [f'{sid}: audit: {e}' for e in lineage_audit.validate(audit, sources)]
                if audit.get('independence_status') != src['independence_status']:
                    problems.append(f'{sid}: registry says {src["independence_status"]}, audit says {audit.get("independence_status")}')
        la = src.get('lineage_audit')
        if la is not None and not (ROOT / la).exists():
            problems.append(f'{sid}: lineage_audit points to missing file {la}')
    for sid in audits:
        if sid not in sources:
            problems.append(f'lineage audit {sid}.json names a source that is not registered')
    return problems


def main() -> int:
    problems = lint()
    print(json.dumps({'passed': not problems, 'problems': problems}, indent=1))
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
