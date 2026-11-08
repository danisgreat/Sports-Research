"""Mandatory fail-closed source admission for every research HTTP fetch (SRC-ALT-v2)."""
from __future__ import annotations

import urllib.parse
import urllib.request

from ml import source_audit


class SourceAccessError(ValueError):
    pass


def ensure_allowed(url: str) -> dict:
    if urllib.parse.urlparse(url).scheme not in ("https", "http"):
        raise SourceAccessError("SOURCE_SCHEME: only public HTTP(S) sources are supported")
    row = source_audit.audit([url])[0]
    if row["status"] not in source_audit.OPEN:
        raise SourceAccessError(f"SOURCE_ACCESS_REFUSED: {row['status']} {url}; find a permitted independent alternate")
    return row


class _CheckedRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        ensure_allowed(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_bytes(url: str, *, user_agent: str = source_audit.UA, timeout: int = 45) -> bytes:
    """Check the exact path before opening it; check redirect destinations before following them."""
    ensure_allowed(url)
    request = urllib.request.Request(url, headers={"User-Agent": user_agent})
    response = urllib.request.build_opener(_CheckedRedirect()).open(request, timeout=timeout)
    with response:
        return response.read()
