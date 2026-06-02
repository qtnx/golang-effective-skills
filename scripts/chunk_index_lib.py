#!/usr/bin/env python3
"""Shared local chunk-index utilities."""

from __future__ import annotations

import hashlib
import math
import re
from array import array
from dataclasses import dataclass
from pathlib import Path


DIMENSIONS = 768
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FIELD_RE = re.compile(r'^([A-Za-z_]+):\s*"([^"]*)"', re.MULTILINE)
TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|[0-9]+")
APPROX_TOKEN_RE = re.compile(r"`[^`]*`|[A-Za-z_][A-Za-z0-9_]*|[0-9]+|[^\s]")
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "if",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "use",
    "when",
    "with",
}


@dataclass(frozen=True)
class ChunkRecord:
    path: str
    title: str
    source_name: str
    source_url: str
    source_path: str
    license_ref: str
    word_count: int
    token_count: int
    sha256: str
    content: str


def strip_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    metadata = dict(FIELD_RE.findall(match.group(1)))
    return metadata, text[match.end() :].strip() + "\n"


def title_from_content(content: str) -> str:
    for line in content.splitlines():
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return "Untitled"


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def approx_token_count(text: str) -> int:
    return len(APPROX_TOKEN_RE.findall(text))


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_chunk(path: Path, repo_root: Path) -> ChunkRecord:
    text = path.read_text(encoding="utf-8", errors="replace")
    metadata, content = strip_frontmatter(text)
    return ChunkRecord(
        path=path.relative_to(repo_root).as_posix(),
        title=title_from_content(content),
        source_name=metadata.get("source_name", ""),
        source_url=metadata.get("source_url", ""),
        source_path=metadata.get("source_path", ""),
        license_ref=metadata.get("license_ref", ""),
        word_count=word_count(content),
        token_count=approx_token_count(content),
        sha256=content_hash(text),
        content=content,
    )


def tokenize(text: str) -> list[str]:
    tokens = [token.lower() for token in TOKEN_RE.findall(text)]
    return [token for token in tokens if token not in STOPWORDS and len(token) > 1]


def features(text: str) -> list[str]:
    tokens = tokenize(text)
    items = tokens[:]
    items.extend(f"{left}_{right}" for left, right in zip(tokens, tokens[1:]))
    return items


def hashed_embedding(text: str, dimensions: int = DIMENSIONS) -> array:
    vector = array("f", [0.0]) * dimensions
    for feature in features(text):
        digest = hashlib.blake2b(feature.encode("utf-8"), digest_size=8).digest()
        value = int.from_bytes(digest, "big")
        index = value % dimensions
        sign = 1.0 if value & 1 else -1.0
        vector[index] += sign
    norm = math.sqrt(sum(value * value for value in vector))
    if norm:
        for index, value in enumerate(vector):
            vector[index] = value / norm
    return vector


def vector_to_blob(vector: array) -> bytes:
    return vector.tobytes()


def blob_to_vector(blob: bytes) -> array:
    vector = array("f")
    vector.frombytes(blob)
    return vector


def dot(left: array, right: array) -> float:
    return float(sum(a * b for a, b in zip(left, right)))


def snippet_for_query(content: str, query_terms: set[str], limit: int | None = 320) -> str:
    if limit is None:
        return content.strip()
    clean = re.sub(r"\s+", " ", content).strip()
    if not clean:
        return ""
    lowered = clean.lower()
    positions = [lowered.find(term) for term in query_terms if lowered.find(term) >= 0]
    start = max(0, min(positions) - 80) if positions else 0
    snippet = clean[start : start + limit].strip()
    if start:
        snippet = "..." + snippet
    if start + limit < len(clean):
        snippet += "..."
    return snippet
