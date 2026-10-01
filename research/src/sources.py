"""Allowlisted source retrieval with immutable bytes and verifiable receipts.

Source accessibility is not source truth or proof of independent collection.
Odds-bearing responses remain in the ignored local benchmark quarantine.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler

from .load import ROOT

REGISTRY = ROOT / "sources_registry.json"
RECEIPTS = ROOT / "data/source_receipts"
RAW = ROOT / "data/raw/source_snapshots"
QUARANTINE = ROOT / "data/benchmark/source_snapshots"
MAX_BYTES = 12_000_000


def read_registry(path=REGISTRY):
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    sources = obj.get("sources", {})
    if not isinstance(sources, dict) or not sources:
        raise ValueError("source registry must map source IDs to contracts")
    return sources


def allowed_url(url: str, source: dict) -> bool:
    parsed = urlsplit(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password or parsed.fragment:
        return False
    if any(key in parsed.query.lower() for key in ("password=", "api_key=", "access_token=", "authorization=")):
        return False
    for prefix in source.get("allowed_url_prefixes", []):
        approved = urlsplit(prefix)
        if parsed.netloc == approved.netloc and parsed.path.startswith(approved.path):
            return True
    return False


def verified_body(receipt: dict, root=ROOT.parent) -> bytes:
    p = Path(receipt["body_path"])
    path = p if p.is_absolute() else Path(root)/p
    if not path.resolve().is_relative_to(Path(root).resolve()):
        raise ValueError("source body path escapes evidence root")
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != receipt["response_sha256"]:
        raise ValueError("retained source body hash mismatch")
    observed = datetime.fromisoformat(receipt["retrieved_utc"].replace("Z", "+00:00"))
    if observed.tzinfo is None or observed.utcoffset() is None:
        raise ValueError("source retrieval timestamp needs an offset")
    return raw


def fetch_source(source_id: str, url: str, cache_dir: Path | None = None,
                 registry_path=REGISTRY, timeout=20, attempts=2) -> dict:
    sources = read_registry(registry_path)
    source = sources[source_id]
    if source.get("access_mode") != "AUTOMATED_ALLOWED":
        raise ValueError("source requires manual or licensed access; no automated fallback")
    if not allowed_url(url, source):
        raise ValueError("URL is outside the source contract")
    if source.get("market_fields_possible"):
        directory = QUARANTINE
        if cache_dir is not None and Path(cache_dir).resolve() != QUARANTINE.resolve():
            raise ValueError("odds-bearing source bytes require the benchmark quarantine")
    else:
        directory = Path(cache_dir) if cache_dir is not None else RAW
    if not 1 <= attempts <= 3 or not 1 <= timeout <= 30:
        raise ValueError("bounded timeout/attempts required")
    raw = None
    class ApprovedRedirect(HTTPRedirectHandler):
        def redirect_request(self, request, reply, code, message, headers, new_url):
            if not allowed_url(new_url, source):
                raise ValueError("redirect outside source allowlist")
            return super().redirect_request(request, reply, code, message, headers, new_url)
    opener=build_opener(ApprovedRedirect())
    for attempt in range(attempts):
        try:
            with opener.open(Request(url, headers={"User-Agent":"SportsResearch/2026.10 (source-custody research)"}), timeout=timeout) as reply:
                final_url = reply.geturl()
                if not allowed_url(final_url, source):
                    raise ValueError("redirect outside source allowlist")
                raw = reply.read(MAX_BYTES+1)
                if len(raw) > MAX_BYTES:
                    raise ValueError("source exceeds bounded response size")
                content_type = reply.headers.get("Content-Type", "")
            break
        except HTTPError as exc:
            if exc.code in (401, 403, 404, 429) or attempt+1 == attempts:
                raise
            time.sleep(.5*(attempt+1))
        except (URLError, TimeoutError):
            if attempt+1 == attempts:
                raise
            time.sleep(.5*(attempt+1))
    if raw is None or not raw:
        raise ValueError("empty source response")
    now = datetime.now(timezone.utc)
    digest = hashlib.sha256(raw).hexdigest()
    stamp = now.strftime("%Y%m%dT%H%M%S%fZ")
    directory.mkdir(parents=True, exist_ok=True)
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    name = f"{source_id}_{stamp}_{digest[:12]}"
    body = directory/(name+".body")
    with body.open("xb") as handle:
        handle.write(raw)
    rel = body.relative_to(ROOT.parent).as_posix() if body.is_relative_to(ROOT.parent) else str(body)
    receipt = dict(schema_version=1, source_id=source_id, publisher=source["publisher"],
                   upstream_lineage_id=source["upstream_lineage_id"], independence_status=source["independence_status"],
                   source_url=url, final_url=final_url, retrieved_utc=now.isoformat(),
                   response_sha256=digest, body_path=rel, response_bytes=len(raw), content_type=content_type,
                   parser_id=source["parser_id"], registry_sha256=hashlib.sha256(Path(registry_path).read_bytes()).hexdigest(),
                   market_quarantined=bool(source.get("market_fields_possible")),
                   assessment="FETCHED_BYTES_ONLY; event, field, timing and lineage validation remain required")
    target = RECEIPTS/(name+".json")
    with target.open("x", encoding="utf-8") as handle:
        json.dump(receipt, handle, indent=2); handle.write("\n")
    return {**receipt, "receipt_path":target.relative_to(ROOT.parent).as_posix()}


def observe_catalogue(output: Path) -> dict:
    if output.exists():
        raise FileExistsError("source observation is immutable")
    outcomes = []
    for source_id, source in read_registry().items():
        url = source.get("probe_url")
        if source.get("access_mode") != "AUTOMATED_ALLOWED" or not url:
            outcomes.append(dict(source_id=source_id, status="MANUAL_OR_NO_PROBE", reason=source.get("access_mode")))
            continue
        try:
            receipt = fetch_source(source_id, url, timeout=15, attempts=1)
            raw = verified_body(receipt)
            expected = source.get("probe_expected_text", [])
            text = raw.decode("utf-8", errors="replace")
            passed = all(token in text for token in expected)
            outcomes.append(dict(source_id=source_id, status="EXPECTED_CONTENT" if passed else "CONTENT_UNVERIFIED", receipt=receipt))
        except (HTTPError, URLError, TimeoutError, ValueError, KeyError) as exc:
            outcomes.append(dict(source_id=source_id, status="UNAVAILABLE", reason=f"{type(exc).__name__}: {exc}"))
    result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  scope="Accessibility and specified content only; independent truth and upstream collection are not inferred.", sources=outcomes)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2); handle.write("\n")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--observe", type=Path, required=True)
    args = parser.parse_args()
    result = observe_catalogue(args.observe)
    print(json.dumps({r["source_id"]:r["status"] for r in result["sources"]}, indent=2))
