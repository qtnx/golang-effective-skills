#!/usr/bin/env python3
"""Validate generated source chunks and linked-doc cache."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
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


def validate_index(root: Path, errors: list[str]) -> None:
    index_path = root / "sources" / "index" / "chunks.sqlite"
    if not index_path.exists():
        errors.append(f"{index_path}: missing chunk index; run scripts/build_chunk_index.py")
        return

    chunk_paths = sorted((root / "sources" / "chunks").glob("*.md"))
    expected_hashes = {
        path.relative_to(root).as_posix(): path.read_text(encoding="utf-8", errors="replace")
        for path in chunk_paths
    }
    expected_hashes = {
        path: hashlib.sha256(text.encode("utf-8")).hexdigest()
        for path, text in expected_hashes.items()
    }

    connection = sqlite3.connect(index_path)
    try:
        chunk_count = connection.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        embedding_count = connection.execute("SELECT COUNT(*) FROM embeddings").fetchone()[0]
        if chunk_count != len(expected_hashes):
            errors.append(f"{index_path}: chunk_count {chunk_count} != {len(expected_hashes)}")
        if embedding_count != len(expected_hashes):
            errors.append(f"{index_path}: embedding_count {embedding_count} != {len(expected_hashes)}")

        rows = connection.execute("SELECT path, sha256, token_count FROM chunks").fetchall()
        indexed_paths = {path for path, _, _ in rows}
        missing = sorted(set(expected_hashes) - indexed_paths)
        extra = sorted(indexed_paths - set(expected_hashes))
        for path in missing[:20]:
            errors.append(f"{index_path}: missing indexed chunk {path}")
        for path in extra[:20]:
            errors.append(f"{index_path}: stale indexed chunk {path}")
        for path, sha256, token_count in rows:
            if path in expected_hashes and expected_hashes[path] != sha256:
                errors.append(f"{index_path}: stale hash for {path}")
            if token_count <= 0:
                errors.append(f"{index_path}: non-positive token_count for {path}")

        dimensions = connection.execute("SELECT DISTINCT dimensions FROM embeddings").fetchall()
        if len(dimensions) != 1 or dimensions[0][0] <= 0:
            errors.append(f"{index_path}: invalid embedding dimensions {dimensions!r}")
    finally:
        connection.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()

    root = args.root.resolve()
    errors: list[str] = []
    validate_chunks(root, errors)
    validate_source_maps(root, errors)
    validate_external_cache(root, errors)
    validate_index(root, errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("Source chunks valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
