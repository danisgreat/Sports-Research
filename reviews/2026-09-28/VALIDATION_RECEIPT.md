# Review validation receipt

Date: 28 September 2026, Australia/Sydney. These are review checks, not proof of forecast quality.

| Check executed | Result |
|---|---|
| `python -m unittest discover -s . -p 'test_*.py'` | 79 tests passed. Expected empty-card error messages were emitted by negative tests; the suite finished OK. |
| `python -m unittest discover -s tools -p 'test_*.py'` | 126 tests passed. |
| `python tools/verify_manifest.py` | CONTROL_MANIFEST_2026-09-27.md: 124 entries matched; no missing/mismatched entries. |
| `python tools/repo_hygiene.py` | 688 tracked files; zero reported problems. New untracked review files are outside that tracked-file count. |
| `python tools/evidence_status.py` | No prospective baseline decisions, RM-1 cards in the retained CSV or shadow rows; one 12-event universe with no dispositions; rule freeze in force. |
| `python audit_card_controls.py <P518 mini log> --settlement --strict` | All five cards printed all applicable blocking fields. This is a presence check. |
| `python tools/skill_baseline.py --boot 2000` | Prospective zero; seed 29 decisions/9 cards, Brier 0.2461 versus 0.2360; paired interval spans zero. |
| Independent `audit_evidence.py` | 71-document inventory; 1,264-row dataset arithmetic; 20 issue/settlement baseline mismatches; 40/40 Brier cells agree with printed probabilities and claimed outcomes within 0.00015. |
| Existing extractor, output redirected to extraction_preview/ | 1,284 rows/320 cards; 20 additional rows from P-518–P-522. Preview not approved for use. |
| RM-1 CLI replay for AFLW, KBO and ACB sample slates | Reproduced capped-tier top-two labelling, near-tied-flip ordering and P-522 covering-pair q inconsistency. |
| Card-math CLI replay of P-518 Normal margin, no zero | Mets +1.5 about 0.5855; Nationals +1.5 about 0.6039. Card family table prints 0.640 and 0.635. |
| Official MLB 822678 retrieval | Final 7–1 confirmed; process-stat contradictions retained in mlb_822678_verification.json. |
| Official AFLW 8942 match centre/report | Final and quarter scores confirmed; official report includes injuries; current settlement uses a different event reference. |

The original model validation experiments were not all rerun. No full external re-settlement of all five cards or the historical corpus is claimed. The control checker explicitly tests printed fields, not their factual truth. The review's negative findings are therefore compatible with its passing result.

The extraction preview can be regenerated without overwriting production outputs with the following Python code, executed from the repository root:

```python
from pathlib import Path
import importlib.util

source = Path('research/settled_rows_2026-09-25/extract_settled_rows.py').resolve()
spec = importlib.util.spec_from_file_location('review_extractor', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
destination = Path('reviews/2026-09-28/extraction_preview').resolve()
destination.mkdir(exist_ok=True)
module.HERE = str(destination)
module.main()
```

This intentionally uses the current parser as a reproduction of its behaviour, not as independent verification of source truth. The separate arithmetic in audit_evidence.py reads the committed CSV directly.
