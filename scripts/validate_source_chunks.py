#!/usr/bin/env python3
"""Validate generated source chunks and linked-doc cache."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


MIN_CHUNK_WORDS = 120
MAX_CHUNK_WORDS = 1600
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
SOURCE_PATH_RE = re.compile(r'^source_path:\s*"([^"]+)"', re.MULTILINE)
SOURCE_MAP_RE = re.compile(r"`(sources/chunks/[^`]+)`")
SOURCE_VIEWER_RE = re.compile(r"(go-googlesource-com-go-refs-.*-src-|go-dev-src-)")


def word_count(text: str) -> int:
    body = FRONTMATTER_RE.sub("", text, count=1)
    return len(re.findall(r"\S+", body))


def source_path(text: str) -> str | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    source_match = SOURCE_PATH_RE.search(match.group(1))
    return source_match.group(1) if source_match else None


def validate_chunks(root: Path, errors: list[str]) -> None:
    chunks_dir = root / "sources" / "chunks"
    for path in sorted(chunks_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        count = word_count(text)
        if count < MIN_CHUNK_WORDS:
            errors.append(f"{path}: {count} words, below {MIN_CHUNK_WORDS}")
        if count > MAX_CHUNK_WORDS:
            errors.append(f"{path}: {count} words, above {MAX_CHUNK_WORDS}")
        raw_source = source_path(text)
        if not raw_source:
            errors.append(f"{path}: missing source_path frontmatter")
        elif not (root / raw_source).exists():
            errors.append(f"{path}: source_path does not exist: {raw_source}")


def validate_source_maps(root: Path, errors: list[str]) -> None:
    for path in sorted((root / "skills").glob("*/references/source-map.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in SOURCE_MAP_RE.finditer(text):
            chunk_path = root / match.group(1)
            if not chunk_path.exists():
                errors.append(f"{path}: missing chunk reference: {match.group(1)}")


def validate_external_cache(root: Path, errors: list[str]) -> None:
    external_dir = root / "sources" / "raw" / "external"
    if external_dir.exists():
        for path in sorted(external_dir.glob("*")):
            if SOURCE_VIEWER_RE.search(path.name):
                errors.append(f"{path}: source-code viewer should not be cached")

    manifest_path = root / "sources" / "raw" / "external-docs-manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        failed_count = manifest.get("failed_count", 0)
        if failed_count:
            errors.append(f"{manifest_path}: failed_count is {failed_count}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()

    root = args.root.resolve()
    errors: list[str] = []
    validate_chunks(root, errors)
    validate_source_maps(root, errors)
    validate_external_cache(root, errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("Source chunks valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
