"""One-time document repair; original versions remain in opening Git HEAD."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).parent
if (OUT/'document_changes.json').exists():
    raise FileExistsError('This one-time repair already has a receipt; do not replay it.')
REPORT = 'research/verification/implementation_2026-10-05/REPORT.md'
records = []


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def change(name, transform):
    path = ROOT/name
    raw = path.read_bytes()
    text = raw.decode('utf-8-sig').replace('\r\n', '\n')
    updated = transform(text)
    if updated == text:
        return
    newline = '\r\n' if b'\r\n' in raw else '\n'
    body = updated.replace('\n', newline).encode('utf-8')
    if raw.startswith(b'\xef\xbb\xbf'):
        body = b'\xef\xbb\xbf'+body
    path.write_bytes(body)
    records.append(dict(path=name, before_sha256=sha(raw), after_sha256=sha(body),
                        before_bytes=len(raw), after_bytes=len(body)))


def replace(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Expected one exact document fragment: '+old[:90])
    return text.replace(old, new, 1)


def prepend_after_title(text, note):
    first, rest = text.split('\n', 1)
    return first+'\n\n'+note+'\n'+rest


note = ('> **Current authority (October 5):** [METHOD.md](METHOD.md) and '
        '[CURRENT_RULES.md](CURRENT_RULES.md) govern new work. Requested qualitative or explicitly '
        'uncalibrated research receives canonical Part 6 IDs regardless of calibration; numerical '
        'performance certification is separate. Read current IDs/freeze from the '
        '[status register](GAME_LOG_STATUS_CURRENT.md), unresolved items from the '
        '[carryover](research/verification/closure_2026-10-05/carryover.md), and '
        '[current implementation evidence]('+REPORT+'). Earlier method, queue, freeze and '
        'eligibility statements below retain their historical scope.')

for path in sorted(ROOT.glob('RULES_*.md')):
    name = path.name
    # The earlier administrative header incorrectly prohibited unregistered
    # uncalibrated research; competition mechanics below are left intact.
    change(name, lambda text: note+'\n\n'+text.split('\n\n', 1)[1]
           if text.startswith('> **Current research controls (2026-10-01):**') else note+'\n\n'+text)
for name in ['LEAGUE_RULES_SOCCER.md', 'LEAGUE_RULES_CRICKET.md']:
    change(name, lambda text: note+'\n\n'+text.split('\n\n', 1)[1])
for name in ['BASE_RATES_REGISTER.md', 'PROBABILITY_TOOLKIT.md', 'SKILL_BASELINE_LEDGER.md',
             'MARKET_BENCHMARK_LEDGER.md', 'SOURCES.md', 'VALIDATION_EVIDENCE.md',
             'LEARNING_REGISTER.md', 'LEARNINGS_INDEX.md', 'P518_P522_RECONCILIATION.md',
             'PIPELINE_IMPLEMENTATION_2026-09-29.md', 'IMPLEMENTATION_2026-10-01.md',
             'VERIFICATION_RECEIPT_2026-09-28.md']:
    change(name, lambda text: prepend_after_title(text, note))

change('README.md', lambda text: replace(replace(replace(text,
    'controls: **CR-2026.10.01-I2**', 'controls: **CR-2026.10.05-I2**'),
    'Use [the implementation report](IMPLEMENTATION_2026-10-01.md) for changes, evidence and outstanding prospective gates.',
    'Use [the October 5 implementation evidence]('+REPORT+') for current reconciliation, cleanup and verification. The [October 1 report](IMPLEMENTATION_2026-10-01.md) retains its historical results.'),
    'P-523 remains the next unconsumed new issue ID. A separate mini-log is intake only and cannot assign IDs.',
    'P-523–P-537 are canonical research records; the verified next ID at this repair is P-538. Always read the live allocator before issuance. The [status register](GAME_LOG_STATUS_CURRENT.md) links both closed mini archives and all 15 unresolved carryover records. Eleven diagnostic settlements and 132 retrospective sections remain learning evidence, with zero certified/performance-eligible settlements. Closed minis cannot assign IDs.')
    .replace('python -B -m pytest -p no:cacheprovider research/tests -q',
             'py -3.14 -B -m pytest -p no:cacheprovider research/tests research/operations -q')
    .replace('py -3.14 -B -m research.operations.control_freeze --verify',
             'py -3.14 -B -m research.operations.verify_custody\npy -3.14 -B -m research.operations.verify_reconciliation\npy -3.14 -B -m research.operations.control_freeze --verify'))

change('METHOD.md', lambda text: replace(replace(text,
    'Control revision **CR-2026.10.05-I1**', 'Control revision **CR-2026.10.05-I2**'),
    'Active freeze: [CONTROL_MANIFEST_2026-10-05-1.md](CONTROL_MANIFEST_2026-10-05-1.md)',
    'Active freeze: [CONTROL_MANIFEST_2026-10-05-2.md](CONTROL_MANIFEST_2026-10-05-2.md)')
    .replace('Status: **ACTIVE**.',
             'The subsequent [October 5 implementation]('+REPORT+') aligns all current document authorities, removes the redundant closed mini pointer after archive readback, retains all eleven retrospective hypotheses as untested proposals, and reports every source-body custody failure. The full custody gate remains strict; local and clean-checkout results are recorded separately. Earlier receipt 1 describes the earlier closure.\n\nStatus: **ACTIVE**.', 1))
change('CURRENT_RULES.md', lambda text: replace(text,
    'MDS-2026.10.01-v7.1 / CR-2026.10.05-I1', 'MDS-2026.10.01-v7.1 / CR-2026.10.05-I2')
    .replace('## Earlier October 1 settlement readback — historical snapshot',
             '## October 5 reconciliation and closure — current guidance\n\n'
             'P-523–P-537 are already canonical. Do not reimport or reissue them. Four overlapping versions are dated addenda. The eleven P-527–P-537 sporting reviews are diagnostic, with 132 retained retrospective sections; they do not certify operator settlements or prospective skill. All 15 records retain separate carryover requirements, including P-537 first-half/corners conflicts. [Carryover](research/verification/closure_2026-10-05/carryover.md) and [implementation evidence]('+REPORT+') bind the exact records.\n\n'
             'Before removing a redundant mini, verify its complete archived original against the retained length/hash and map all entries/addenda to the existing canonical IDs. Remove only the redundant working pointer/copy; keep original archive bodies, source receipts, issued cores and historical audit snapshots. Do not allocate an ID for closure.\n\n'
             'Missing or damaged source bodies fail full custody verification, including quarantined bodies omitted from Git. Local mechanics PASS is distinct from clean-checkout evidence completeness and sporting/operator certification. Run all required checks even if another check fails. A new administrative receipt records reviewed changes only after failures and evidence limits are retained.\n\n'
             '## Earlier October 1 settlement readback — historical snapshot', 1))

change('research/README.md', lambda text: text.replace(
    '## Requested analyses and canonical logging',
    'Current reconciliation: [October 5 evidence](verification/implementation_2026-10-05/REPORT.md). P-523–P-537 are already canonical; P-538 is next at this repair, subject to the live allocator. The two closed mini archives, all 15 carryovers, eleven diagnostic settlements and 132 retrospective sections are retained. No reimport, new certification or forecast rewrite is needed.\n\n## Requested analyses and canonical logging', 1)
    .replace('research/tests -q', 'research/tests research/operations -q')
    .replace('py -3.14 -B -m research.operations.verify_custody\n',
             'py -3.14 -B -m research.operations.verify_custody\npy -3.14 -B -m research.operations.verify_reconciliation\n')
    .replace('Restricted Football-Data/FixtureDownload snapshots remain local',
             'Full custody reports every missing/hash-invalid/length-invalid receipt body and returns nonzero for any failure. There is no clean-checkout bypass. At this repair all 78 receipt bodies verify locally, while 42 are local-only benchmark bodies excluded from Git; an export containing tracked bodies alone fails their custody checks. CI runs freeze verification even after custody failure and retains an overall failure. Do not refetch a different body or publish quarantined bytes to mask that gap.\n\nRestricted Football-Data/FixtureDownload snapshots remain local'))

change('PROMPTS.md', lambda text: text.replace('## Settle and learn',
    '## Reconcile mini references and close duplicates\n\n'
    '> Read METHOD.md, current status and the ledger-backed allocator. Inventory every mini entry, exact event, source version and immutable body. Recover pending research transactions before allocation. Exact existing event/source/body combinations keep their canonical ID; changed versions become dated addenda. Before importing, check Part 6 and ledger custody so closure never reissues an already canonical event. Separate diagnostic sporting grades from operator certification, retain every unresolved contract/field in carryover, and never invent p/baseline/start/quorum evidence. Verify complete original archive bytes and canonical coverage before deleting redundant working copies. Keep necessary source/archive/audit evidence. Run regressions, canonical verification, strict custody, reconciliation readback and freeze independently. Report local and clean-checkout failures separately with zero new IDs where all entries are already canonical.\n\n## Settle and learn', 1))
change('CARD_AND_LOG_TEMPLATES.md', lambda text: text.replace('## Settlement revision',
    '## Research diagnostic addendum and mini closure\n\n'
    'Bind the existing canonical ID/event, immutable original source/projection hashes, actual observation/review time, exact endpoint and each original source version. Retain conditional grade, operator definition status, actual-start admission, audited terminal-lineage status and performance eligibility separately. UNKNOWN_DEFINITION, UNRESOLVED_PERIOD, UNRESOLVED_PROVIDER_FIELD and missing p/baseline remain literal missingness; NO_FORECAST and late/live classifications remain unchanged. List every unresolved requirement in carryover. A diagnostic addendum does not create an ISSUE or certified settlement record.\n\n'
    'An archive receipt binds original length/hash, archive path/hash, preserved-body offset, canonical entry mappings, overlap/addendum disposition, carryover and actual next-ID readback. Closure allocates no ID for an already represented event. Remove redundant working copies only after exact archive/readback checks.\n\n## Settlement revision', 1))
change('RECORD_ELIGIBILITY_SCHEMA.md', lambda text: text.replace(
    '| Historical literal learning |',
    '| Research diagnostic addendum | Sporting arithmetic only; operator/performance certification remains unresolved until admitted evidence passes | Existing canonical ID/core; original version hashes; conditional period/action; actual review time; source/definition conflicts; carryover |\n'
    '| Closed mini reference | Evidence archive, never an allocation authority | Full original bytes, archived length/hash/offset, canonical event/addendum map, retained unresolved requirements |\n'
    '| Historical literal learning |', 1))
change('SCORING_AND_VALIDATION.md', lambda text: text.replace('## Release and failure policy',
    '## October 5 diagnostic cohort\n\n'
    'P-527–P-537 retain eleven completed-game diagnostic reviews, not certified prospective outcomes. Missing literal probabilities/baselines make Brier/log loss and adjustment improvement NOT_COMPUTABLE; ordinal ranks, duplicated rows, alternative versions and complementary picks do not create extra trials. P-537 first-half and corners rows remain unresolved. The [carryover](research/verification/closure_2026-10-05/carryover.md) also retains P-523–P-526 custody requirements. No original NO_FORECAST or LATE_RESEARCH state is upgraded.\n\n'
    'All eleven retrospective hypotheses are recorded verbatim in [the improvement register](research/improvement_register.json) as PROPOSED_NOT_TESTED. A written acceptance criterion is not a passed experiment; no weights, probabilities or model qualifications change from those proposals.\n\n## Release and failure policy', 1))
for name in ['LEARNINGS_INDEX.md', 'LEARNING_REGISTER.md']:
    change(name, lambda text: prepend_after_title(text,
        'October 5 retrospective suggestions: [eleven source-bound proposals](research/improvement_register.json), all **PROPOSED_NOT_TESTED / NOT PERFORMANCE_ELIGIBLE**. Each retains its original hypothesis/acceptance criterion; none changes a model weight, cap or ranking rule. [Implementation and limits]('+REPORT+').'))
change('CONTRIBUTING.md', lambda text: text.replace(
    'then regenerate and verify the active manifest.',
    'then create a new versioned manifest and verify it. Never overwrite an existing receipt.')
    .replace('Scientific and process failures must be visible.',
    'Verify archived source length/hash/offset and canonical coverage before deleting redundant working minis. Preserve unique archive bodies, frozen source/projection stores and audit evidence. Use `research.operations.verify_reconciliation` for current document, archive, carryover and hypothesis readback.\n\nScientific and process failures must be visible.'))
change('VERIFICATION_PROTOCOL.md', lambda text: text.replace(
    'python -B -m pytest -p no:cacheprovider research/tests -q',
    'py -3.14 -B -m pytest -p no:cacheprovider research/tests research/operations -q')
    .replace('py -3.14 -B -m pytest -p no:cacheprovider research/operations/test_log_card.py -q',
             'py -3.14 -B -m research.operations.verify_reconciliation')
    .replace('Failure notifications report the job\'s actual failure;',
             'Each verification step runs after earlier failures unless the workflow is cancelled, so custody failure no longer hides freeze results. No step uses continue-on-error. Root Markdown edits also trigger checks. Failure notifications report the job\'s actual failure;')
    .replace('Run live-source jobs separately from tests.',
             'Full custody is strict in every environment: the wrapper aggregates all missing, hash-invalid, length-invalid and malformed-receipt failures, retains nonzero failure, and restores its in-memory schema adapter after each run. At the October 5 implementation readback 78 bodies verify locally; 42 receipt bodies are intentionally local-only in ignored benchmark quarantine. A tracked-body export fails those 42 checks, rather than just reporting the first missing AFC body. [Complete local/publication inventory and outcomes]('+REPORT+'). The separate archive source-body gap disclosed by closure is not the same issue as Git omitting local benchmark bodies.\n\nRun live-source jobs separately from tests.'))
change('SOURCES.md', lambda text: text.replace(
    '**New sources found during a card** go into the mini log\'s document mapping with their route. They are added here at the next import.',
    '**New sources found during a card** go into the canonical Part 6 card\'s source/document mapping with their route and retained receipts. Use a mini only if canonical writing fails, then reconcile transactionally. Source registry additions require explicit access/lineage/field contracts; a URL list does not grant admission.'))
change('CHANGELOG.md', lambda text: text.replace('## Entries from 2026-09-25(c)',
    '## Entries from 2026-09-25(c)\n\n'
    '### 2026-10-05 — document reconciliation and strict custody reporting (I2)\n\n'
    'Aligned current documents with canonical P-523–P-537, next P-538 and the selected October 5 receipt; corrected the sport-reference header that wrongly blocked uncalibrated requested research. Retained the two original closed mini archives and all carryover/diagnostic history; removed the redundant working mini pointer after hash readback. Registered eleven retrospective hypotheses as untested proposals. Custody now reports every failed body while preserving strict failure; CI runs canonical/custody/freeze checks independently. All original logs, ledger and four model builds remain unchanged. [Implementation evidence]('+REPORT+').', 1))

head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
(OUT/'document_changes.json').write_text(json.dumps(dict(observed_utc=datetime.now(timezone.utc).isoformat(),
    opening_head=head, original_recovery='git show OPENING_HEAD:PATH', files=records), indent=2)+'\n', encoding='utf-8')
print(f'Updated {len(records)} documents; original versions retained at {head}')
