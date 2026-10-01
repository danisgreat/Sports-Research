"""Freeze a versioned model/dependency receipt; no automatic live promotion."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from importlib.metadata import version
import json
import platform
from pathlib import Path
from .load import ROOT, sha


def create(name="build_2026-10-01.json"):
    directory=ROOT/"model_builds";directory.mkdir(exist_ok=True)
    output=directory/name
    if output.exists() or (directory/"current.json").exists():
        raise FileExistsError("build already frozen; version the model/build before replacing a pointer")
    packages={p:version(p) for p in ("numpy","pandas","scipy","pyarrow")}
    paths=[p for p in (ROOT/"src").rglob("*.py") if "__pycache__" not in p.parts]
    paths.extend([ROOT/"requirements.lock.txt",ROOT/"runs/implementation_2026-10-01/development_protocol.json",
                  ROOT/"runs/implementation_2026-10-01/family_diagnostics.json",
                  ROOT/"runs/implementation_2026-10-01/family_forecasts.csv",
                  ROOT/"runs/epl_2025-26_holdout.json",ROOT/"runs/epl_tuning_lock.json",
                  ROOT/"runs/nbl_2025-26_holdout.json",ROOT/"runs/nbl_tuning_lock.json"])
    artifacts=[dict(path=p.relative_to(ROOT.parent).as_posix(),sha256=sha(p)) for p in sorted(set(paths))]
    builds=[]
    for lane,model,families in (("EPL","epl-dc-0.1.0",["1X2"]),("NBL","nbl-joint-0.1.0",["ML"]),
                              ("EPL","epl-coherent-ensemble-0.2.0",["1X2"]),("NBL","nbl-oof-width-0.2.0",["ML"])):
        builds.append(dict(lane=lane,model_version=model,status="SHADOW_ONLY",retrospective_families=families,
                           artifacts=artifacts,packages=packages,python_version=platform.python_version(),
                           reason="Pinned operational build. Old tests are historical; new candidate evidence is opened development data. Live qualification requires separate prospective evidence."))
    data=dict(schema_version="model-build-1",created_utc=datetime.now(timezone.utc).isoformat(),builds=builds)
    text=json.dumps(data,indent=2)+"\n"
    with output.open("x",encoding="utf-8") as handle:handle.write(text)
    with (directory/"current.json").open("x",encoding="utf-8") as handle:handle.write(text)
    return data


if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--name",default="build_2026-10-01.json")
    args=parser.parse_args();data=create(args.name)
    print(f"Frozen {len(data['builds'])} SHADOW_ONLY builds")
