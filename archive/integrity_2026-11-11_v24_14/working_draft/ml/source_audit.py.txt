"""Source access check for AI agents (SRC-ALT-v1, CR-2026.11.09-R1; per reader SRC-ALT-v3, CR-2026.11.11-R1).

    python -m ml source-audit --url https://example.org/match/1          one source, before it is opened
    python -m ml source-audit --register SOURCES.md --out NEW_FOLDER     every URL a document names

A source is checked against its site's robots.txt for every Anthropic agent token (ClaudeBot, Claude-User,
Claude-SearchBot, Claude-Web, anthropic-ai), the OpenAI tokens (GPTBot, OAI-SearchBot, ChatGPT-User) and for a
``Content-Signal: ai-input=no`` reservation:

    ALLOWED          the rules were read and permit the path for every token
    NO_RULES_FILE    robots.txt returned 404 or 410: no rules are set
    BLOCKED_FOR_AI   at least one token is disallowed for the path, or ai-input=no is declared
    BLOCKED_FOR_ALL  the path is disallowed for every agent
    RULES_UNKNOWN    403, 429, 5xx, a timeout or an HTML page instead of rules: not permission

Only ALLOWED and NO_RULES_FILE sources may be opened. A blocked or unknown source is never reached another way (a reader
proxy such as r.jina.ai, a cache, a mirror of the same pages or a different user agent): the research looks for an
alternate that publishes the same fields (SOURCES "SRC-ALT-v1") and checks it the same way.

**Per reader (SRC-ALT-v3, owner instruction 11 November 2026).** A site's rules are applied to the reader that opens the
page, by that reader's own published agent name:

    CLAUDE_AGENT       Claude-User    the repository agent opening one page at the owner's request
    CHATGPT_BROWSING   ChatGPT-User   a ChatGPT research chat opening one page at the owner's request
    SCRIPT             all eight      the repository's own fetcher (``ml.source_access``) and every bulk download: unchanged

Each reader's status is ALLOWED, NO_RULES_FILE, BLOCKED or RULES_UNKNOWN (host lists add PARTLY_BLOCKED: the root is open
but named paths are not). ``status`` (the union of all eight tokens) is kept and is the SCRIPT reader's decision. An
``ai-input=no`` signal blocks every reader. A page blocked for a reader is never opened by that reader, and never reached
another way: no other user agent, proxy, cache, mirror or embed.

    python -m ml source-audit --url <url> [--reader CHATGPT_BROWSING]   one page, every reader (or one)
    python -m ml source-audit --lists NEW_FOLDER --hosts-from AUDIT.csv [--use-instead REJECTIONS.csv] [--version v24.13]
                              per-host reader lists for the chats, re-checked weekly (REFRESH_DAYS)
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
from datetime import datetime, timedelta, timezone
from pathlib import Path

AGENTS = ("ClaudeBot", "Claude-User", "Claude-SearchBot", "Claude-Web", "anthropic-ai",
          "GPTBot", "OAI-SearchBot", "ChatGPT-User")
UA = "sports-results-research/1.0"
OPEN = ("ALLOWED", "NO_RULES_FILE")
READERS = {"CLAUDE_AGENT": ("Claude-User",), "CHATGPT_BROWSING": ("ChatGPT-User",), "SCRIPT": AGENTS}
READER_COLUMNS = {"CLAUDE_AGENT": "claude_agent", "CHATGPT_BROWSING": "chatgpt_browsing", "SCRIPT": "script"}
FIELDS = ("host", "url", "robots_http", "status", "agents_blocked", "content_signal", "claude_agent", "chatgpt_browsing", "script",
          "checked_at")
LIST_FIELDS = ("host", "robots_http", "claude_agent", "chatgpt_browsing", "script", "chatgpt_blocked_paths", "claude_blocked_paths",
               "content_signal", "checked_at", "valid_until", "use_instead")
CHAT_LIST_FIELDS = ("host", "chatgpt_browsing", "chatgpt_blocked_paths", "checked_at", "valid_until", "use_instead")
REFRESH_DAYS = 7          # a reader list is re-checked weekly; the repository fetcher still checks live before every fetch


def _parser(text: str) -> urllib.robotparser.RobotFileParser:
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(text.splitlines())
    return rp


def _signal(text: str) -> str:
    return " | ".join(sorted(set(s.strip() for s in re.findall(r"(?im)^content-signal:\s*(.+)$", text))))


def _ai_input_no(signal: str) -> bool:
    return "ai-input=no" in signal.replace(" ", "").lower()


def _rules_unreadable(http: str, text: str | None) -> bool:
    return http != "200" or text is None or "<html" in text[:500].lower()


def reader_status(url: str, http: str, text: str | None, reader: str) -> str:
    """ALLOWED, NO_RULES_FILE, BLOCKED or RULES_UNKNOWN for one reader (SRC-ALT-v3)."""
    if reader not in READERS:
        raise ValueError(f"reader must be one of {', '.join(READERS)}")
    if http in ("404", "410"):
        return "NO_RULES_FILE"
    if _rules_unreadable(http, text):
        return "RULES_UNKNOWN"
    rp = _parser(text)
    if _ai_input_no(_signal(text)) or any(not rp.can_fetch(a, url) for a in READERS[reader]):
        return "BLOCKED"
    return "ALLOWED"


def reader_may_open(url: str, http: str, text: str | None, reader: str) -> bool:
    return reader_status(url, http, text, reader) in OPEN


def classify(url: str, http: str, text: str | None) -> dict:
    """Status of one URL from its host's robots.txt response (pure: no network)."""
    readers = {READER_COLUMNS[r]: reader_status(url, http, text, r) for r in READERS}
    if http in ("404", "410"):
        return dict(status="NO_RULES_FILE", agents_blocked="", content_signal="", **readers)
    if _rules_unreadable(http, text):
        return dict(status="RULES_UNKNOWN", agents_blocked="", content_signal="", **readers)
    rp = _parser(text)
    blocked = [a for a in AGENTS if not rp.can_fetch(a, url)]
    signal = _signal(text)
    if blocked or _ai_input_no(signal):
        status = "BLOCKED_FOR_AI"
    elif not rp.can_fetch("*", url):
        status = "BLOCKED_FOR_ALL"
    else:
        status = "ALLOWED"
    return dict(status=status, agents_blocked=";".join(blocked), content_signal=signal, **readers)


def blocked_paths(text: str, token: str) -> list[str]:
    """The Disallow paths that apply to one agent token: its own group, else the * group (first match, as robotparser)."""
    rp = _parser(text)
    entries = getattr(rp, "entries", [])
    entry = next((e for e in entries if "*" not in e.useragents and e.applies_to(token)), None)
    if entry is None:            # Python 3.14 keeps the * group among the entries; earlier versions as default_entry
        entry = next((e for e in entries if "*" in e.useragents), None) or getattr(rp, "default_entry", None)
    if entry is None:
        return []
    return sorted({line.path for line in entry.rulelines if not line.allowance and line.path})


def host_row(host: str, http: str, text: str | None, checked_at: str, use_instead: str = "") -> dict:
    """One host's per-reader decision at its root, with the paths blocked for each hand reader when the root is open."""
    root = f"https://{host}/"
    readable = not _rules_unreadable(http, text)
    row = dict(host=host, robots_http=http, content_signal=_signal(text) if readable else "", checked_at=checked_at,
               valid_until=(datetime.fromisoformat(checked_at) + timedelta(days=REFRESH_DAYS)).isoformat(timespec="seconds"),
               use_instead=use_instead)
    for reader, column in READER_COLUMNS.items():
        status = reader_status(root, http, text, reader)
        if status == "ALLOWED" and readable and reader != "SCRIPT" and blocked_paths(text, READERS[reader][0]):
            status = "PARTLY_BLOCKED"
        row[column] = status
    for reader, column in (("CHATGPT_BROWSING", "chatgpt_blocked_paths"), ("CLAUDE_AGENT", "claude_blocked_paths")):
        row[column] = " ".join(blocked_paths(text, READERS[reader][0])[:40]) if readable else ""
    return row


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


def reader_lists(hosts, use_instead: dict | None = None, workers: int = 8) -> list[dict]:
    hosts = sorted({h.lower() for h in hosts if h})
    with cf.ThreadPoolExecutor(workers) as ex:
        rules = dict(zip(hosts, ex.map(robots, hosts)))
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return [host_row(h, *rules[h], stamp, (use_instead or {}).get(h, "")) for h in hosts]


def register_urls(path) -> list[str]:
    return re.findall(r"https?://[^\s)`'\"<>|\]]+", Path(path).read_text(encoding="utf-8"))


def _csv(rows: list[dict], fields=FIELDS) -> bytes:
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=list(fields), lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue().encode("utf-8")


def write_lists(out: Path, rows: list[dict], version: str) -> list[Path]:
    """READER_ACCESS_<version>.csv (every host, every reader, with the blocked paths of partly blocked hosts) and
    CHATGPT_DO_NOT_OPEN_<version>.csv: the hosts a chat never opens (blocked at the root for ChatGPT-User, or rules unreadable).
    A partly blocked host stays openable; the chat's own robots check refuses its blocked paths."""
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    paths = [out / f"READER_ACCESS_{version}.csv", out / f"CHATGPT_DO_NOT_OPEN_{version}.csv"]
    paths[0].write_bytes(_csv(rows, LIST_FIELDS))
    chat = [{k: r[k] for k in CHAT_LIST_FIELDS} for r in rows if r["chatgpt_browsing"] in ("BLOCKED", "RULES_UNKNOWN")]
    paths[1].write_bytes(_csv(chat, CHAT_LIST_FIELDS))
    return paths


SLICE_SHARED = ("Weather", "News")


def sport_slices(pregame: Path, reader_access: Path, out: Path, version: str) -> list[Path]:
    """PREGAME_SOURCES rows a ChatGPT research chat may open, one file per sport (shared weather and news rows in each),
    with the host's ChatGPT status. Hosts blocked at the root for ChatGPT-User, or with unreadable rules, are left out; a
    partly blocked host stays, marked CHECK_PATH, because its blocked paths are refused by the chat's own robots check."""
    with open(reader_access, newline="", encoding="utf-8-sig") as fh:
        status = {r["host"]: r for r in csv.DictReader(fh)}
    with open(pregame, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    fields = list(rows[0]) + ["chatgpt_status", "chatgpt_blocked_paths"]
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    written = []
    shared = [r for r in rows if r["sport"] in SLICE_SHARED]
    for sport in sorted({r["sport"] for r in rows} - set(SLICE_SHARED)):
        keep = []
        for r in [r for r in rows if r["sport"] == sport] + shared:
            host = (urllib.parse.urlparse(r["url"]).hostname or "").lower()
            s = status.get(host)
            if s is None or s["chatgpt_browsing"] in ("BLOCKED", "RULES_UNKNOWN"):
                continue
            keep.append(dict(r, chatgpt_status="CHECK_PATH" if s["chatgpt_browsing"] == "PARTLY_BLOCKED" else s["chatgpt_browsing"],
                             chatgpt_blocked_paths=s["chatgpt_blocked_paths"]))
        path = out / f"PREGAME_SOURCES_{sport.upper().replace(' ', '_')}_{version}.csv"
        path.write_bytes(_csv(keep, fields))
        written.append(path)
    return written


def _hosts_from(path: Path) -> list[str]:
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    hosts = [r.get("host") or (urllib.parse.urlparse(r.get("url", "")).hostname or "") for r in rows]
    return [h for h in hosts if h]


def _use_instead(path: Path) -> dict:
    out = {}
    with open(path, newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            host = (urllib.parse.urlparse(r.get("url", "")).hostname or "").lower()
            if host and r.get("use_instead"):
                out.setdefault(host, r["use_instead"])
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--url", action="append", default=[])
    parser.add_argument("--register", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--reader", choices=sorted(READERS), help="print only this reader's decision")
    parser.add_argument("--lists", type=Path, help="new folder for the per-reader host lists")
    parser.add_argument("--hosts-from", type=Path, action="append", default=[], help="CSV with a host or url column (repeatable)")
    parser.add_argument("--use-instead", type=Path, help="CSV with url and use_instead columns (PREGAME_SOURCE_REJECTIONS.csv)")
    parser.add_argument("--version", default="v24.13", help="version carried in the list file names")
    parser.add_argument("--sport-slices", type=Path, help="new folder: PREGAME_SOURCES rows a chat may open, by sport")
    parser.add_argument("--pregame", type=Path, default=Path("research/source_routes/PREGAME_SOURCES.csv"))
    parser.add_argument("--reader-access", type=Path, help="READER_ACCESS_<version>.csv from --lists")
    args = parser.parse_args(argv)
    if args.sport_slices:
        if not args.reader_access:
            parser.error("--sport-slices needs --reader-access")
        for path in sport_slices(args.pregame, args.reader_access, args.sport_slices, args.version):
            print("wrote", path)
        return
    if args.lists:
        hosts = [h for path in args.hosts_from for h in _hosts_from(path)]
        hosts += [urllib.parse.urlparse(u).hostname or "" for u in args.url]
        if not any(hosts):
            parser.error("--lists needs --hosts-from or --url")
        rows = reader_lists(hosts, _use_instead(args.use_instead) if args.use_instead else {})
        for path in write_lists(args.lists, rows, args.version):
            print("wrote", path)
        for column in READER_COLUMNS.values():
            counts = {s: sum(r[column] == s for r in rows) for s in sorted({r[column] for r in rows})}
            print(f"{column}: {counts}")
        return
    urls = list(args.url) + (register_urls(args.register) if args.register else [])
    if not urls:
        parser.error("give --url, --register or --lists")
    rows = audit(urls)
    if args.out:
        args.out.mkdir(parents=True, exist_ok=False)
        (args.out / "SOURCE_ACCESS_AUDIT.csv").write_bytes(_csv(rows))
    for r in rows:
        if args.reader:
            print(r[READER_COLUMNS[args.reader]], args.reader, r["robots_http"], r["url"])
        elif args.url or r["status"] not in OPEN:
            print(r["status"], r["robots_http"], r["url"], r["agents_blocked"],
                  f"| claude_agent {r['claude_agent']} | chatgpt_browsing {r['chatgpt_browsing']} | script {r['script']}")
    counts = {s: sum(r["status"] == s for r in rows) for s in sorted({r["status"] for r in rows})}
    print(f"{len(rows)} URLs: {counts}")


if __name__ == "__main__":
    main()
