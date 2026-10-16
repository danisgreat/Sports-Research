"""An intentionally absent history store must not break reviewed-web research."""
import pytest
from ml import config


def test_missing_history_root_has_no_discoveries_or_fallback(tmp_path, monkeypatch):
    missing = tmp_path / "not-created"
    monkeypatch.setattr(config, "ARCHIVE", missing)
    config._discover_cached.cache_clear()
    try:
        assert config.discover() == []
        with pytest.raises(KeyError, match="Basketball/EXAMPLE"):
            config.get_league("Basketball/EXAMPLE")
        assert not missing.exists()
    finally:
        config._discover_cached.cache_clear()
