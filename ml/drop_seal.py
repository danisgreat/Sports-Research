"""DROP-SEAL-v1: register requests and seal cards that an external research chat pushes to a drop branch.

An outside chat (for example ChatGPT) cannot run this repository's commands, but it can push files. It pushes:

    drops/requests/<CARD_KEY>/REQUEST.txt, EVENT.csv, CONTRACTS.csv   before research starts
    drops/cards/<any name>.md                                           the finished card, before first play

The `seal-drops` workflow runs this module on every push to the drop branch. It reads the exact pushed blobs and
calls the unchanged ONE-CHAT-v3 code: `forecast_integrity.register_request` + `one_chat.publish_requests` for a
request, and `one_chat.seal` for a card. Nothing here changes a forecast, a contract, the timing rules or the
scoring. Server publication time on the seal branch remains the only timing evidence; the drop push time is not.

    python -m ml.drop_seal --before <sha> --after <sha> [--summary FILE]
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
import time
from pathlib import Path

from ml import forecast_integrity as F
from ml import one_chat as O

RULE = "DROP-SEAL-v1"
DROP_ROOT = "drops"
REQUEST_DROP = re.compile(r"drops/requests/([A-Za-z0-9_-]+)/(REQUEST\.txt|EVENT\.csv|CONTRACTS\.csv)")
CARD_DROP = re.compile(r"drops/cards/[^/]+\.md")
ZERO = "0" * 40
RACE = ("seal push refused", "refresh and retry")    # another drop published first: refetch and publish on top


def _publish(fn, root, attempts=5, pause=4):
    """Run one publication; if a concurrent drop moved the seal branch, refetch and retry. Never forces a push."""
    for n in range(attempts):
        try:
            return fn()
        except O.OneChatError as exc:
            if n == attempts - 1 or not any(r in str(exc) for r in RACE):
                raise
            time.sleep(pause * (n + 1))
            O._git(root, "fetch", "-q", "origin", O.SEAL_BRANCH, check=False)


def changed_drops(root, before: str, after: str) -> list[str]:
    """Files added or modified under drops/ by this push, in path order. A new branch counts every drop it holds."""
    if not before or set(before) == {"0"}:
        out = O._git(root, "ls-tree", "-r", "-z", "--name-only", after, "--", DROP_ROOT).stdout
    else:
        out = O._git(root, "diff", "--name-only", "-z", "--no-renames", "--diff-filter=AM", before, after,
                     "--", DROP_ROOT).stdout
    return sorted(p for p in out.split("\0") if p)


def blob(root, commit: str, path: str) -> bytes:
    """Exact pushed bytes, with no line-ending or text conversion."""
    res = O.subprocess.run(["git", "-C", str(root), "cat-file", "blob", f"{commit}:{path}"], capture_output=True)
    if res.returncode:
        raise O.OneChatError(f"{path} is not in {commit[:12]}")
    return res.stdout


def _restore_published_request(root, key: str) -> None:
    """Copy a registered request from the seal branch into local staging so `seal` can check the card against it."""
    folder = O.request_staging(root) / F.request_path(key)
    if folder.exists():
        return
    ref = f"refs/remotes/origin/{O.SEAL_BRANCH}"
    files = {}
    for name in (*F.REQUEST_FILES, "MANIFEST.csv"):
        res = O.subprocess.run(["git", "-C", str(root), "cat-file", "blob", f"{ref}:{F.request_path(key)}/{name}"],
                               capture_output=True)
        if res.returncode:
            return          # not registered: seal reports the missing registration itself
        files[name] = res.stdout
    folder.mkdir(parents=True)
    for name, raw in files.items():
        (folder / name).write_bytes(raw)


def _published(root, key: str) -> bool:
    """The key is in the published request index on the seal branch."""
    res = O.subprocess.run(["git", "-C", str(root), "cat-file", "blob", f"refs/remotes/origin/{O.SEAL_BRANCH}:{O.REQUEST_INDEX}"],
                           capture_output=True)
    return not res.returncode and any(r["card_key"] == key for r in F.rows(res.stdout))


def process(root, before: str, after: str, *, lookup=None, wait=(0, 3, 6, 12)) -> list[dict]:
    """Register every complete request drop, then seal every card drop. One result row per drop."""
    root = Path(root)
    O._git(root, "fetch", "-q", "origin", O.SEAL_BRANCH, check=False)
    paths = changed_drops(root, before, after)
    results: list[dict] = []
    requests: dict[str, set[str]] = {}
    cards: list[str] = []
    for p in paths:
        m = REQUEST_DROP.fullmatch(p)
        if m:
            requests.setdefault(m[1], set()).add(m[2])
        elif CARD_DROP.fullmatch(p):
            cards.append(p)
        elif not p.endswith("README.md"):
            results.append(dict(drop=p, kind="unknown", status="IGNORED",
                                detail="not a request file or a card; see drops/README.md"))

    registered = []
    with tempfile.TemporaryDirectory(prefix="drop-request-") as temp:
        for key, names in sorted(requests.items()):
            item = dict(drop=f"{DROP_ROOT}/requests/{key}/", kind="request", card_key=key)
            # All three files must be present in this commit, even if only one changed in this push.
            try:
                folder = Path(temp) / key
                folder.mkdir()
                for name in F.REQUEST_FILES:
                    (folder / name).write_bytes(blob(root, after, f"{DROP_ROOT}/requests/{key}/{name}"))
                # Each run starts with empty staging: load any published registration first, so an edited
                # re-push is compared with the immutable published bytes and refused, never reported as registered.
                _restore_published_request(root, key)
                outcome = F.register_request(folder / "REQUEST.txt", folder / "EVENT.csv", folder / "CONTRACTS.csv",
                                             key, O.request_staging(root))
                if outcome["status"] == "ALREADY_REGISTERED" and _published(root, key):
                    results.append(dict(item, status="ALREADY_REGISTERED",
                                        detail=f"identical to the request already published on {O.SEAL_BRANCH}"))
                    continue
                registered.append(key)
                results.append(dict(item, status="STAGED", detail=outcome["status"]))
            except (O.OneChatError, ValueError, OSError) as exc:
                results.append(dict(item, status="FAILED", detail=str(exc)))
    if registered:
        try:
            commit = _publish(lambda: O.publish_requests(registered, root), root)
            for r in results:
                if r.get("card_key") in registered and r["status"] == "STAGED":
                    r.update(status="REGISTERED", commit=commit or "",
                             detail=f"published on {O.SEAL_BRANCH}; start research only after this time")
        except (O.OneChatError, ValueError, OSError) as exc:
            for r in results:
                if r.get("card_key") in registered and r["status"] == "STAGED":
                    r.update(status="FAILED", detail=str(exc))

    with tempfile.TemporaryDirectory(prefix="drop-card-") as temp:
        for i, p in enumerate(cards):
            item = dict(drop=p, kind="card")
            try:
                raw = blob(root, after, p)
                file = Path(temp) / f"card{i:03d}.md"
                file.write_bytes(raw)
                blocks = O.card_blocks(raw.decode("utf-8"), root)
                if not blocks:
                    raise O.OneChatError("no ONECHAT_V1 block found")
                item["card_key"] = ";".join(b[0] for b in blocks)
                for b in blocks:
                    _restore_published_request(root, b[0])
                outcome = _publish(lambda: O.seal([file], root, lookup=lookup, wait=wait), root)
                refused = "; ".join(f"{r['card_key'] or 'card'}: {r['reason']}" for r in outcome.get("refused", []))
                if outcome["sealed"] and not refused:
                    results.append(dict(item, status="SEALED", commit=outcome["commit"],
                                        detail=f"server time {outcome['server_time'] or 'pending'} on {O.SEAL_BRANCH}"))
                elif refused:
                    sealed = f"sealed {outcome['cards']}; " if outcome["sealed"] else ""
                    results.append(dict(item, status="FAILED", commit=outcome.get("commit", ""), detail=sealed + "not sealed: " + refused))
                else:
                    results.append(dict(item, status="ALREADY_SEALED", detail=outcome.get("note", "")))
            except (O.OneChatError, ValueError, OSError, UnicodeDecodeError) as exc:
                results.append(dict(item, status="FAILED", detail=str(exc)))
    return results


def summary(results: list[dict], after: str) -> str:
    lines = [f"## {RULE}: drop {after[:12]} → `{O.SEAL_BRANCH}`", ""]
    if not results:
        return "\n".join(lines + ["No request or card drops in this push."]) + "\n"
    lines += ["| Drop | Kind | Card key | Status | Detail |", "|---|---|---|---|---|"]
    for r in results:
        detail = str(r.get("detail", "")).replace("|", "/").replace("\n", " ")[:400]
        lines.append(f"| `{r['drop']}` | {r['kind']} | {r.get('card_key', '')} | **{r['status']}** | {detail} |")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--before", required=True)
    ap.add_argument("--after", required=True)
    ap.add_argument("--summary", type=Path)
    args = ap.parse_args(argv)
    results = process(O.ROOT, args.before, args.after)
    text = summary(results, args.after)
    print(text)
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as fh:
            fh.write(text)
    return 1 if any(r["status"] == "FAILED" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
