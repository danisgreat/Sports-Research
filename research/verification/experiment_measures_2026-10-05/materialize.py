"""Create the first source-bound catalog once; never overwrite an issued file."""
from datetime import datetime,timezone
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from research.experiments.catalog import catalog,VERSION
from research.experiments.runner import write_new,readiness
from research.src.eligibility import digest,file_sha

protocols=catalog();path=ROOT/'research/experiments/protocols_v1.json'
write_new(path,dict(schema=VERSION,protocols=protocols))
records=[dict(experiment_id=p['experiment_id'],source_card_id=p['source_card_id'],protocol_sha256=digest(p),
              measures_status='IMPLEMENTED',experiment_status='NOT_RUN_AT_REGISTRATION',performance_eligible=False,
              next_steps=p['required_next_steps']) for p in protocols]
write_new(ROOT/'research/experiment_measures.json',dict(schema=VERSION,created_utc=datetime.now(timezone.utc).isoformat(),
          protocols_path=path.relative_to(ROOT).as_posix(),protocols_sha256=file_sha(path),records=records,
          instructions_path='research/experiments/NEXT_STEPS.md',evidence_path='research/verification/experiment_measures_2026-10-05/REPORT.md'))
write_new(Path(__file__).parent/'readiness_at_registration.json',dict(measures_implemented=15,experiments_run=0,
          protocols=[readiness(p) for p in protocols],performance_eligible=False))
print('15 measurement protocols materialized; 0 experiments run')
