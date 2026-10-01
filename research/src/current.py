"""Compatibility entry point for immutable EPL source snapshots.

September 29 files remain historical receipts. New observations use dated
folders and remain provisional until event-specific corroboration passes.
"""
from datetime import datetime, timezone
from .daily import DAILY, snapshot


def build(snapshot_utc=None):
    if snapshot_utc is not None:
        raise ValueError("source retrieval time cannot be supplied or backdated")
    target=DAILY/(datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")+"_snapshot")/"EPL"
    target.mkdir(parents=True,exist_ok=False)
    _,_,manifest=snapshot("EPL",target)
    return {**manifest,"output_path":str(target),"stage":"PROVISIONAL_SOURCE_SNAPSHOT_ONLY"}


if __name__=="__main__":
    import json
    print(json.dumps(build(),indent=2))
