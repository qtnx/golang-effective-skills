#!/usr/bin/env python3
"""Query the local chunk vector index and return source chunks to load."""

from __future__ import annotations

import argparse
import json
import math
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

from chunk_index_lib import blob_to_vector, dot, hashed_embedding, snippet_for_query, tokenize


SKILL_HINTS = {
    "go-style-core": "clarity simplicity concision maintainability comments formatting gofmt readable idiomatic",
    "go-naming-api-design": "package names receiver names getters initialisms exported comments interface api call site",
    "go-errors-panics": "errors error wrapping sentinel errors.Is errors.As panic recover logging error strings",
    "go-testing": "unit tests table driven subtests test helpers t.Helper got want failure messages benchmark",
    "go-code-review-checklist": "review correctness api errors tests cancellation style findings",
    "golang-effective": "go effective style api errors testing review idiomatic",
}


def load_chunks(connection: sqlite3.Connection) -> list[dict[str, object]]:
    rows = connection.execute(
        """
        SELECT c.id, c.path, c.title, c.source_name, c.source_url, c.token_count,
               c.content, e.vector
        FROM chunks c
        JOIN embeddings e ON e.chunk_id = c.id
        ORDER BY c.id
        """
    ).fetchall()
    return [
        {
            "id": row[0],
            "path": row[1],
            "title": row[2],
            "source_name": row[3],
            "source_url": row[4],
            "token_count": row[5],
            "content": row[6],
            "vector": blob_to_vector(row[7]),
        }
        for row in rows
    ]


def lexical_scores(connection: sqlite3.Connection, query_terms: list[str], total_docs: int) -> dict[int, float]:
    if not query_terms:
        return {}
    unique_terms = sorted(set(query_terms))
    placeholders = ",".join("?" for _ in unique_terms)
    df_rows = connection.execute(
        f"SELECT term, COUNT(*) FROM terms WHERE term IN ({placeholders}) GROUP BY term",
        unique_terms,
    ).fetchall()
    idf = {
        term: math.log((1 + total_docs) / (1 + df)) + 1.0
        for term, df in df_rows
    }
    rows = connection.execute(
        f"SELECT chunk_id, term, tf FROM terms WHERE term IN ({placeholders})",
        unique_terms,
    ).fetchall()
    scores: dict[int, float] = defaultdict(float)
    query_counts = Counter(query_terms)
    for chunk_id, term, tf in rows:
        scores[chunk_id] += (1 + math.log(tf)) * idf.get(term, 0.0) * query_counts[term]
    if not scores:
        return {}
    max_score = max(scores.values())
    return {chunk_id: score / max_score for chunk_id, score in scores.items()}


def search(index: Path, query: str, skill: str | None, top: int) -> list[dict[str, object]]:
    expanded_query = query
    if skill:
        expanded_query = f"{query}\n{SKILL_HINTS.get(skill, skill)}"
    query_terms = tokenize(expanded_query)
    query_vector = hashed_embedding(expanded_query)

    connection = sqlite3.connect(index)
    try:
        chunks = load_chunks(connection)
        lexical = lexical_scores(connection, query_terms, len(chunks))
    finally:
        connection.close()

    query_term_set = set(tokenize(query))
    results = []
    for chunk in chunks:
        vector_score = dot(query_vector, chunk["vector"])
        lexical_score = lexical.get(chunk["id"], 0.0)
        score = 0.68 * vector_score + 0.32 * lexical_score
        results.append(
            {
                "score": round(score, 6),
                "vector_score": round(vector_score, 6),
                "lexical_score": round(lexical_score, 6),
                "path": chunk["path"],
                "title": chunk["title"],
                "source_name": chunk["source_name"],
                "source_url": chunk["source_url"],
                "token_count": chunk["token_count"],
                "snippet": snippet_for_query(str(chunk["content"]), query_term_set),
            }
        )
    results.sort(key=lambda item: item["score"], reverse=True)
    return results[:top]


def print_text(results: list[dict[str, object]]) -> None:
    total_tokens = sum(int(item["token_count"]) for item in results)
    print(f"total_result_tokens: {total_tokens}")
    for index, item in enumerate(results, 1):
        print(f"\n{index}. {item['path']}")
        print(f"   score: {item['score']}  tokens: {item['token_count']}  source: {item['source_name']}")
        print(f"   title: {item['title']}")
        if item["source_url"]:
            print(f"   url: {item['source_url']}")
        print(f"   snippet: {item['snippet']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Natural-language query or review finding text")
    parser.add_argument("--index", type=Path, default=Path("sources/index/chunks.sqlite"))
    parser.add_argument("--skill", choices=sorted(SKILL_HINTS), help="Bias retrieval toward a Go skill")
    parser.add_argument("--top", type=int, default=6)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    results = search(args.index, args.query, args.skill, args.top)
    if args.json:
        print(json.dumps(results, indent=2, sort_keys=True))
    else:
        print_text(results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
