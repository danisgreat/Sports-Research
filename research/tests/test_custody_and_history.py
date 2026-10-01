import hashlib
import json
from datetime import datetime, timezone
import pytest
from research.src.history import literal_probability, pointer_receipt
from research.src.sources import allowed_url, verified_body
from research.src.emit_card import states
from research.src.sports.base import Contract
from research.src.settle import FinalReceipt


def test_receipt_hash_and_evidence_path_are_required(tmp_path):
    path=tmp_path/"body";path.write_bytes(b"data")
    receipt=dict(body_path="body",response_sha256=hashlib.sha256(b"data").hexdigest(),retrieved_utc="2026-10-01T00:00Z")
    assert verified_body(receipt,tmp_path)==b"data"
    path.write_bytes(b"tamper")
    with pytest.raises(ValueError,match="hash"):
        verified_body(receipt,tmp_path)
    receipt["body_path"]="../outside"
    with pytest.raises(ValueError,match="escapes"):
        verified_body(receipt,tmp_path)


def test_allowlist_rejects_impersonation_and_credentials():
    source=dict(allowed_url_prefixes=["https://statsapi.mlb.com/api/"])
    assert allowed_url("https://statsapi.mlb.com/api/v1/schedule",source)
    assert not allowed_url("https://statsapi.mlb.com.attacker.test/api/v1",source)
    assert not allowed_url("https://user:pass@statsapi.mlb.com/api/v1",source)
    assert not allowed_url("https://statsapi.mlb.com/api/v1?api_key=secret",source)


def test_unknown_historical_probabilities_remain_missing():
    assert literal_probability("") is None
    assert literal_probability("NOT_YET_DERIVED (0.500)") is None
    assert literal_probability("nan") is None
    assert literal_probability("1.01") is None
    assert literal_probability(".75")==.75


def test_noninteger_score_states_and_nan_lines_are_rejected():
    with pytest.raises(ValueError,match="integers"):
        states([dict(home=1.4,away=0,p=1)])
    with pytest.raises(ValueError,match="finite"):
        Contract("x","TOTAL","OVER",float("nan"),"REGULATION")
    with pytest.raises(ValueError,match="checksum"):
        FinalReceipt("x","FINAL",2,1,"REGULATION","https://example.org",datetime.now(timezone.utc),"x"*64,"2-1")
