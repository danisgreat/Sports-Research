"""Current CLI, preserving the model-pinned historical workflow source."""
import importlib.util
from pathlib import Path
from research.src import workflow as historical
from research.operations.canonical_issue import prepare_issue,commit_issue,recover_issue,next_card_id


def _adapter():
    spec=importlib.util.spec_from_file_location('research.src._current_workflow_adapter',Path(historical.__file__))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.prepare_issue=prepare_issue;module.commit_issue=commit_issue
    module.recover_issue=recover_issue;module.next_card_id=next_card_id
    return module


def status():return _adapter().status()


if __name__=='__main__':_adapter().main()
