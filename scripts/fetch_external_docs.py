#!/usr/bin/env python3
"""Fetch documentation-like external links referenced by generated chunks."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import ssl
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse
from urllib.request import Request, urlopen


URL_RE = re.compile(r"https?://[^\s\"'<>)]+" )
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)\s]+)\)")
MAX_BYTES = 2_000_000
USER_AGENT = "golang-effective-skills-doc-fetcher/0.1"

ALLOW_HOSTS = {
    "go.dev",
    "blog.golang.org",
    "golang.org",
    "pkg.go.dev",
    "research.swtch.com",
    "go-proverbs.github.io",
    "testing.googleblog.com",
    "commandcenter.blogspot.com",
    "dave.cheney.net",
    "eli.thegreenplace.net",
    "abseil.io",
    "bazel.build",
    "docs.bazel.build",
    "grpc.io",
    "docs.python.org",
    "golangci-lint.run",
    "go.googlesource.com",
    "raw.githubusercontent.com",
}

SKIP_HOSTS = {
    "example.com",
    "www.google.com",
    "google.com",
    "fonts.googleapis.com",
    "cdnjs.cloudflare.com",
    "github.com",
    "groups.google.com",
    "drive.google.com",
    "youtube.com",
    "www.youtube.com",
    "bsky.app",
    "hachyderm.io",
    "invite.slack.golangbridge.org",
}

SKIP_SUFFIXES = {
    ".css",
    ".js",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
    ".ico",
    ".pdf",
    ".zip",
}


def strip_url(url: str) -> str:
    url = html.unescape(url).strip().rstrip(".,;")
    parsed = urlparse(url)
    parsed = parsed._replace(fragment="")
    if parsed.netloc == "golang.org":
        parsed = parsed._replace(scheme="https", netloc="go.dev")
    if parsed.netloc == "blog.golang.org":
        parsed = parsed._replace(scheme="https", netloc="go.dev", path="/blog" + parsed.path)
    if parsed.query:
        keep = [(k, v) for k, v in parse_qsl(parsed.query) if k in {"id"}]
        parsed = parsed._replace(query=urlencode(keep))
    return urlunparse(parsed)


def extract_urls(path: Path) -> Iterable[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    yield from (match.group(1) for match in MARKDOWN_LINK_RE.finditer(text))
    yield from (match.group(0) for match in URL_RE.finditer(text))


def is_doc_like(url: str) -> tuple[bool, str]:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    path = parsed.path.lower()
    if not parsed.scheme.startswith("http"):
        return False, "non-http"
    if host in SKIP_HOSTS:
        return False, "skipped-host"
    if host == "google.github.io" and path.startswith("/styleguide/go"):
        return False, "already-vendored"
    if host == "go.dev" and path in {"/doc/effective_go", "/doc/effective_go.html"}:
        return False, "already-vendored"
    if host == "go.dev" and path.startswith("/src/"):
        return False, "source-viewer"
    if host == "go.googlesource.com" and re.search(r"/go/\+/.*/src/", path):
        return False, "source-viewer"
    if (
        host == "raw.githubusercontent.com"
        and path.startswith("/google/styleguide/gh-pages/go/")
    ):
        return False, "already-vendored"
    if any(path.endswith(suffix) for suffix in SKIP_SUFFIXES):
        return False, "static-asset"
    if host not in ALLOW_HOSTS:
        return False, "not-in-doc-allowlist"
    if host == "raw.githubusercontent.com" and not path.endswith((".md", ".txt", ".rst")):
        return False, "raw-non-doc"
    return True, "fetch"


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "doc"


def target_path(url: str, output_dir: Path) -> Path:
    parsed = urlparse(url)
    base = slugify(parsed.netloc + parsed.path)
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    suffix = ".md" if parsed.path.endswith((".md", ".rst", ".txt")) else ".html"
    return output_dir / f"{base}-{digest}{suffix}"


def read_url(url: str) -> tuple[str, bytes, bool]:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=20) as response:
                return response.headers.get("content-type", ""), response.read(MAX_BYTES + 1), False
        except HTTPError as exc:
            if exc.code != 429 or attempt == 2:
                raise
            time.sleep(5 * (attempt + 1))
        except Exception as exc:
            if "CERTIFICATE_VERIFY_FAILED" not in str(exc):
                raise
            context = ssl._create_unverified_context()
            with urlopen(request, timeout=20, context=context) as response:
                return response.headers.get("content-type", ""), response.read(MAX_BYTES + 1), True
    raise RuntimeError(f"failed to read {url}")


def fetch(url: str, path: Path) -> dict[str, object]:
    content_type, data, insecure_tls = read_url(url)
    truncated = len(data) > MAX_BYTES
    data = data[:MAX_BYTES]
    text = data.decode("utf-8", errors="replace")
    header = (
        "---\n"
        'source_name: "External Linked Documentation"\n'
        f'source_url: "{url}"\n'
        f'retrieved_at: "{datetime.now(timezone.utc).isoformat()}"\n'
        f'content_type: "{content_type}"\n'
        f"truncated: {str(truncated).lower()}\n"
        f"insecure_tls_fallback: {str(insecure_tls).lower()}\n"
        "---\n\n"
    )
    path.write_text(header + text, encoding="utf-8")
    return {
        "url": url,
        "path": path.as_posix(),
        "status": "fetched",
        "content_type": content_type,
        "bytes": len(data),
        "truncated": truncated,
        "insecure_tls_fallback": insecure_tls,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_dir", type=Path, help="Directory containing chunks or source markdown")
    parser.add_argument("output_dir", type=Path, help="Directory for fetched external docs")
    parser.add_argument("--limit", type=int, default=120, help="Maximum docs to fetch")
    parser.add_argument("--force", action="store_true", help="Refetch existing docs")
    parser.add_argument("--prune", action="store_true", help="Remove stale fetched docs not selected this run")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    seen_refs: dict[str, set[str]] = {}
    for path in sorted(args.input_dir.rglob("*.md")):
        for raw_url in extract_urls(path):
            url = strip_url(raw_url)
            seen_refs.setdefault(url, set()).add(path.as_posix())

    manifest: dict[str, object] = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_dir": args.input_dir.as_posix(),
        "output_dir": args.output_dir.as_posix(),
        "fetched": [],
        "skipped": [],
        "failed": [],
        "pruned": [],
    }

    fetched_count = 0
    kept_paths: set[Path] = set()
    for url in sorted(seen_refs):
        allowed, reason = is_doc_like(url)
        entry = {"url": url, "reason": reason, "referenced_by": sorted(seen_refs[url])[:20]}
        if not allowed:
            manifest["skipped"].append(entry)
            continue
        if fetched_count >= args.limit:
            entry["reason"] = "over-limit"
            manifest["skipped"].append(entry)
            continue
        path = target_path(url, args.output_dir)
        kept_paths.add(path)
        if path.exists() and not args.force:
            manifest["fetched"].append({"url": url, "path": path.as_posix(), "status": "already-present"})
            fetched_count += 1
            continue
        try:
            result = fetch(url, path)
            result["referenced_by"] = sorted(seen_refs[url])[:20]
            manifest["fetched"].append(result)
            fetched_count += 1
            time.sleep(0.1)
        except Exception as exc:  # noqa: BLE001 - preserve fetch diagnostics.
            entry["status"] = "failed"
            entry["error"] = str(exc)
            manifest["failed"].append(entry)

    if args.prune:
        for path in sorted(args.output_dir.glob("*")):
            if path.is_file() and path.suffix in {".html", ".md", ".txt", ".rst"} and path not in kept_paths:
                path.unlink()
                manifest["pruned"].append(path.as_posix())

    manifest["fetched_count"] = len(manifest["fetched"])
    manifest["skipped_count"] = len(manifest["skipped"])
    manifest["failed_count"] = len(manifest["failed"])
    manifest["pruned_count"] = len(manifest["pruned"])
    manifest_path = args.output_dir.parent / "external-docs-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"Fetched {manifest['fetched_count']} docs, skipped {manifest['skipped_count']}, failed {manifest['failed_count']}",
        file=sys.stderr,
    )
    return 0 if manifest["failed_count"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
