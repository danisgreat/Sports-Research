from research.operations import control_freeze


def test_runtime_code_and_config_are_checkout_line_ending_independent(tmp_path,monkeypatch):
    monkeypatch.setattr(control_freeze,'ROOT',tmp_path)
    for name in ['runtime/src/example.py','runtime/config/sports/example.json','runtime/r_ingestion/example.R','runtime/pyproject.toml']:
        path=tmp_path/name;path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(b'first\nsecond\n');lf=control_freeze.controlled_bytes(path)
        path.write_bytes(b'first\r\nsecond\r\n')
        assert lf==control_freeze.controlled_bytes(path)==('CRLF',b'first\r\nsecond\r\n')


def test_raw_evidence_is_not_normalized(tmp_path,monkeypatch):
    monkeypatch.setattr(control_freeze,'ROOT',tmp_path)
    path=tmp_path/'runtime/data/raw/source.json';path.parent.mkdir(parents=True)
    path.write_bytes(b'first\nsecond\n');lf=control_freeze.controlled_bytes(path)
    path.write_bytes(b'first\r\nsecond\r\n')
    assert lf==('RAW',b'first\nsecond\n')
    assert lf != control_freeze.controlled_bytes(path)
