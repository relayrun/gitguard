#!/usr/bin/env python3
"""Read-only public-content and local-link checks. No network or Git writes."""
import argparse
import hashlib
import json
import pathlib
import posixpath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

MAX_FILE = 2_000_000
MAX_FILES = 3000
PATTERNS = {
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github-token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b"),
    "credential-url": re.compile(r"https?://[^/\s:@]+:[^/\s@]+@"),
    "machine-path": re.compile(r"(?:(?<![A-Za-z0-9_.-])[A-Za-z]:[/\\](?![/\\])[^\s<>\"`]+|/(?:Users|home)/[A-Za-z0-9._-]+/)"),
    "private-address": re.compile(r"(?<![\w.])(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})(?![\w.])"),
}
MD_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")
PRIVATE_ROOT = {"AGENTS.md", "CONTRIBUTING.md", "PLAN.md", "DECISIONS.md"}
TEXT_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml", ".toml", ".txt", ".csv", ".conf", ".sh", ".ps1", ".example"}

def git(root, *args):
    r = subprocess.run(["git", "-C", str(root), *args], capture_output=True, timeout=40)
    if r.returncode:
        raise ValueError("Git read failed; verify repository and requested reference")
    return r.stdout

def working_snapshot(root):
    files = {}
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root).as_posix()
        if ".git" in p.relative_to(root).parts:
            continue
        if p.is_symlink():
            files[rel] = ("symlink", b"")
        elif p.is_file():
            if p.stat().st_size > MAX_FILE:
                files[rel] = ("oversize", b"")
            else:
                try:
                    files[rel] = ("regular", p.read_bytes())
                except OSError:
                    files[rel] = ("unreadable", b"")
        if len(files) > MAX_FILES:
            raise ValueError("File limit exceeded; narrow and review release scope")
    return files

def git_snapshot(root, ref=None):
    files = {}
    command = ["ls-files", "--stage", "-z"] if ref is None else ["ls-tree", "-r", "-z", ref]
    for row in git(root, *command).split(b"\0"):
        if not row:
            continue
        info, raw_path = row.split(b"\t", 1)
        path = raw_path.decode("utf-8")
        parts = info.decode("ascii").split()
        mode = parts[0]
        if ref is None:
            oid, stage = parts[1:]
            if stage != "0":
                raise ValueError("Unmerged index entries require resolution before review")
        else:
            _, oid = parts[1:]
        if mode not in {"100644", "100755"}:
            files[path] = ("non-regular-git-entry", b"")
            continue
        size = int(git(root, "cat-file", "-s", oid))
        files[path] = ("oversize", b"") if size > MAX_FILE else ("regular", git(root, "cat-file", "blob", oid))
        if len(files) > MAX_FILES:
            raise ValueError("File limit exceeded")
    return files

def inspect(files, profile="generic"):
    findings = []
    def flag(path, category, line=None):
        item = {"path": path, "category": category}
        if line is not None:
            item["line"] = line
        findings.append(item)
    paths = set(files)
    directories = {posixpath.dirname(p) for p in paths}
    for p in paths:
        parent = posixpath.dirname(p)
        while parent:
            directories.add(parent)
            parent = posixpath.dirname(parent)
    directories.add(".")
    for path, (kind, raw) in files.items():
        if kind != "regular":
            flag(path, kind)
            continue
        name = pathlib.PurePosixPath(path).name
        if name == ".env" or (name.startswith(".env.") and name != ".env.example") or name.startswith(".dev.vars") or pathlib.PurePosixPath(path).suffix in {".pem", ".key", ".pfx", ".p12", ".db", ".log"}:
            flag(path, "private-or-runtime-file")
        if profile == "gitguard" and (path in PRIVATE_ROOT or path.startswith(("docs/maintainers/", "site/", ".vscode/")) or path.endswith(".code-workspace")):
            flag(path, "outside-public-package")
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            flag(path, "binary-requires-manual-review")
            continue
        if "\x00" in text:
            flag(path, "binary-requires-manual-review")
            continue
        if "\ufffd" in text:
            flag(path, "replacement-character")
        for category, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                flag(path, category, text.count("\n", 0, match.start()) + 1)
        if not path.endswith(".md"):
            continue
        for match in MD_LINK.finditer(text):
            dest = match.group(1).strip().strip("<>")
            parsed = urlsplit(dest)
            if parsed.scheme or parsed.netloc or dest.startswith("#"):
                continue
            target = unquote(parsed.path)
            if not target:
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), target))
            if target.startswith("/") or resolved == ".." or resolved.startswith("../"):
                flag(path, "link-outside-package")
            elif resolved not in paths and resolved not in directories:
                flag(path, "missing-local-link", text.count("\n", 0, match.start()) + 1)
    return findings


def media_review(files, findings, receipt=None):
    """Resolve only exact, manually reviewed binary bytes; retain all other findings."""
    receipt = receipt or {}
    unresolved, reviewed = [], []
    for finding in findings:
        path = finding['path']
        kind, raw = files[path]
        approved = receipt.get(path)
        if (finding['category'] == 'binary-requires-manual-review'
                and kind == 'regular' and pathlib.PurePosixPath(path).suffix.lower() in {'.png', '.mp4'}
                and approved == hashlib.sha256(raw).hexdigest()):
            reviewed.append({**finding, 'sha256': approved, 'disposition': 'matched-external-media-review'})
        else:
            unresolved.append(finding)
    return unresolved, reviewed


def read_media_review(path, root=None):
    if path is None:
        return {}
    if root is not None and path.resolve().is_relative_to(root.resolve()):
        raise ValueError('Media review receipts must remain outside the checked public tree')
    data = json.loads(path.read_text(encoding='utf-8'))
    if data.get('status') != 'reviewed' or not isinstance(data.get('files'), dict):
        raise ValueError('Expected a reviewed media receipt with file hashes')
    for name, digest in data['files'].items():
        if (not isinstance(name, str) or not isinstance(digest, str)
                or not re.fullmatch(r'[a-f0-9]{64}', digest)):
            raise ValueError('Invalid media review entry')
    return data['files']

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parent.parent)
    ap.add_argument("--profile", choices=("generic", "gitguard"), default="generic")
    ap.add_argument("--media-review", type=pathlib.Path, help="Private receipt for exact manually reviewed PNG/MP4 hashes")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--staged", action="store_true")
    group.add_argument("--history", metavar="BASE..HEAD")
    args = ap.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        raise ValueError("Target root must be an existing directory")
    snapshots = []
    if args.history:
        if args.history.startswith("-") or "\n" in args.history:
            raise ValueError("Invalid history range")
        revisions = git(root, "rev-list", "--max-count=201", args.history, "--").decode("ascii").split()
        if len(revisions) > 200:
            raise ValueError("History range exceeds 200 commits; split the review")
        snapshots = [(rev, git_snapshot(root, rev)) for rev in revisions]
    elif args.staged:
        snapshots = [("index", git_snapshot(root))]
    else:
        snapshots = [("working-tree", working_snapshot(root))]
    receipt = read_media_review(args.media_review, root)
    failures = 0
    incomplete = False
    for label, files in snapshots:
        findings = inspect(files, args.profile)
        unresolved, reviewed = media_review(files, findings, receipt)
        failures += len(unresolved)
        incomplete |= any(kind == 'unreadable' for kind, _ in files.values())
        print(json.dumps({"snapshot": label, "files": len(files), "findings": unresolved,
                          "reviewed_media": reviewed}, ensure_ascii=True))
    print(json.dumps({"snapshots": len(snapshots), "findings": failures,
                      "limits": "Heuristics and relative file links only; no semantic privacy, external URL, fragment, permission or license certification."}))
    return 2 if incomplete else (1 if failures else 0)

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        print(json.dumps({"error": type(error).__name__, "message": "Review incomplete; check input, tool availability or documented limits."}))
        sys.exit(2)
