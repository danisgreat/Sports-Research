"""Source access check for AI agents (SRC-ALT-v1, CR-2026.11.09-R1).

    python -m ml source-audit --url https://example.org/match/1          one source, before it is opened
    python -m ml source-audit --register SOURCES.md --out NEW_FOLDER     every URL a document names

A source is checked against its site's robots.txt for every Anthropic agent token (ClaudeBot, Claude-User,
Claude-SearchBot, Claude-Web, anthropic-ai) and for a ``Content-Signal: ai-input=no`` reservation:

    ALLOWED          the rules were read and permit the path for every token
    NO_RULES_FILE    robots.txt returned 404 or 410: no rules are set
    BLOCKED_FOR_AI   at least one token is disallowed for the path, or ai-input=no is declared
    BLOCKED_FOR_ALL  the path is disallowed for every agent
    RULES_UNKNOWN    403, 429, 5xx, a timeout or an HTML page instead of rules: not permission

Only ALLOWED and NO_RULES_FILE sources may be opened. A blocked or unknown source is never reached another way (a reader
proxy such as r.jina.ai, a cache, a mirror of the same pages or a different user agent): the research looks for an
alternate that publishes the same fields (SOURCES "SRC-ALT-v1") and checks it the same way.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import csv
import io
import re
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from datetime import datetime, timezone
from pathlib import Path

AGENTS = ("ClaudeBot", "Claude-User", "Claude-SearchBot", "Claude-Web", "anthropic-ai")
UA = "sports-results-research/1.0"
OPEN = ("ALLOWED", "NO_RULES_FILE")
FIELDS = ("host", "url", "robots_http", "status", "agents_blocked", "content_signal", "checked_at")


def classify(url: str, http: str, text: str | None) -> dict:
    """Status of one URL from its host's robots.txt response (pure: no network)."""
    if http in ("404", "410"):
        return dict(status="NO_RULES_FILE", agents_blocked="", content_signal="")
    if http != "200" or text is None or "<html" in text[:500].lower():
        return dict(status="RULES_UNKNOWN", agents_blocked="", content_signal="")
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(text.splitlines())
    blocked = [a for a in AGENTS if not rp.can_fetch(a, url)]
    signal = " | ".join(sorted(set(s.strip() for s in re.findall(r"(?im)^content-signal:\s*(.+)$", text))))
    if blocked or "ai-input=no" in signal.replace(" ", "").lower():
        status = "BLOCKED_FOR_AI"
    elif not rp.can_fetch("*", url):
        status = "BLOCKED_FOR_ALL"
    else:
        status = "ALLOWED"
    return dict(status=status, agents_blocked=";".join(blocked), content_signal=signal)


def robots(host: str, timeout: int = 25) -> tuple[str, str | None]:
    try:
        r = urllib.request.urlopen(urllib.request.Request(f"https://{host}/robots.txt", headers={"User-Agent": UA}), timeout=timeout)
        return str(r.status), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return str(exc.code), None
    except Exception as exc:          # a timeout or refusal is not permission
        return "ERROR:" + type(exc).__name__, None


def audit(urls, workers: int = 8) -> list[dict]:
    urls = sorted({u.rstrip(".,;:") for u in urls if urllib.parse.urlparse(u).hostname})
    hosts = sorted({urllib.parse.urlparse(u).hostname.lower() for u in urls})
    with cf.ThreadPoolExecutor(workers) as ex:
        rules = dict(zip(hosts, ex.map(robots, hosts)))
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    out = []
    for u in urls:
        host = urllib.parse.urlparse(u).hostname.lower()
        http, text = rules[host]
        out.append(dict(host=host, url=u, robots_http=http, checked_at=stamp, **classify(u, http, text)))
    return out


def register_urls(path) -> list[str]:
    return re.findall(r"https?://[^\s)`'\"<>|\]]+", Path(path).read_text(encoding="utf-8"))


def _csv(rows: list[dict]) -> bytes:
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=list(FIELDS), lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue().encode("utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--url", action="append", default=[])
    parser.add_argument("--register", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)
    urls = list(args.url) + (register_urls(args.register) if args.register else [])
    if not urls:
        parser.error("give --url or --register")
    rows = audit(urls)
    if args.out:
        args.out.mkdir(parents=True, exist_ok=False)
        (args.out / "SOURCE_ACCESS_AUDIT.csv").write_bytes(_csv(rows))
    for r in rows:
        if args.url or r["status"] not in OPEN:
            print(r["status"], r["robots_http"], r["url"], r["agents_blocked"])
    counts = {s: sum(r["status"] == s for r in rows) for s in sorted({r["status"] for r in rows})}
    print(f"{len(rows)} URLs: {counts}")


if __name__ == "__main__":
    main()
