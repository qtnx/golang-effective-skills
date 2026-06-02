#!/usr/bin/env python3
"""Build a local SQLite vector index for generated Go source chunks."""

from __future__ import annotations

import argparse
import json
import math
import sqlite3
from collections import Counter
from pathlib import Path

from chunk_index_lib import DIMENSIONS, hashed_embedding, read_chunk, tokenize, vector_to_blob


SCHEMA_VERSION = "1"


def create_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        PRAGMA journal_mode = OFF;
        PRAGMA synchronous = OFF;

        CREATE TABLE metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );

        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY,
            path TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            source_name TEXT NOT NULL,
            source_url TEXT NOT NULL,
            source_path TEXT NOT NULL,
            license_ref TEXT NOT NULL,
            word_count INTEGER NOT NULL,
            token_count INTEGER NOT NULL,
            sha256 TEXT NOT NULL,
            content TEXT NOT NULL
        );

        CREATE TABLE embeddings (
            chunk_id INTEGER PRIMARY KEY REFERENCES chunks(id) ON DELETE CASCADE,
            dimensions INTEGER NOT NULL,
            vector BLOB NOT NULL
        );

        CREATE TABLE terms (
            chunk_id INTEGER NOT NULL REFERENCES chunks(id) ON DELETE CASCADE,
            term TEXT NOT NULL,
            tf INTEGER NOT NULL,
            PRIMARY KEY (chunk_id, term)
        );

        CREATE INDEX terms_term_idx ON terms(term);
        """
    )


def build_index(repo_root: Path, chunks_dir: Path, output: Path) -> dict[str, object]:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()

    records = [read_chunk(path, repo_root) for path in sorted(chunks_dir.glob("*.md"))]
    connection = sqlite3.connect(output)
    try:
        create_schema(connection)
        connection.executemany(
            "INSERT INTO metadata(key, value) VALUES (?, ?)",
            [
                ("schema_version", SCHEMA_VERSION),
                ("embedding_provider", "local-hashed-ngram"),
                ("embedding_dimensions", str(DIMENSIONS)),
                ("chunk_count", str(len(records))),
            ],
        )

        document_frequency: Counter[str] = Counter()
        term_counters: list[Counter[str]] = []

        for chunk_id, record in enumerate(records, 1):
            terms = Counter(tokenize(record.title + "\n" + record.content))
            term_counters.append(terms)
            document_frequency.update(terms)
            connection.execute(
                """
                INSERT INTO chunks(
                    id, path, title, source_name, source_url, source_path,
                    license_ref, word_count, token_count, sha256, content
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    chunk_id,
                    record.path,
                    record.title,
                    record.source_name,
                    record.source_url,
                    record.source_path,
                    record.license_ref,
                    record.word_count,
                    record.token_count,
                    record.sha256,
                    record.content,
                ),
            )
            vector = hashed_embedding(record.title + "\n" + record.content)
            connection.execute(
                "INSERT INTO embeddings(chunk_id, dimensions, vector) VALUES (?, ?, ?)",
                (chunk_id, DIMENSIONS, vector_to_blob(vector)),
            )

        for chunk_id, terms in enumerate(term_counters, 1):
            connection.executemany(
                "INSERT INTO terms(chunk_id, term, tf) VALUES (?, ?, ?)",
                [(chunk_id, term, tf) for term, tf in sorted(terms.items())],
            )

        avg_tokens = math.floor(sum(record.token_count for record in records) / len(records))
        summary = {
            "schema_version": SCHEMA_VERSION,
            "embedding_provider": "local-hashed-ngram",
            "embedding_dimensions": DIMENSIONS,
            "chunk_count": len(records),
            "avg_token_count": avg_tokens,
            "total_token_count": sum(record.token_count for record in records),
            "unique_terms": len(document_frequency),
        }
        connection.execute(
            "INSERT INTO metadata(key, value) VALUES (?, ?)",
            ("summary_json", json.dumps(summary, sort_keys=True)),
        )
        connection.commit()
        return summary
    finally:
        connection.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--chunks-dir", type=Path, default=Path("sources/chunks"))
    parser.add_argument("--output", type=Path, default=Path("sources/index/chunks.sqlite"))
    args = parser.parse_args()

    repo_root = args.root.resolve()
    chunks_dir = (repo_root / args.chunks_dir).resolve()
    output = (repo_root / args.output).resolve()
    summary = build_index(repo_root, chunks_dir, output)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
