#!/usr/bin/env python3
"""Universal router for querying the local chunk vector index."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

from chunk_index_lib import blob_to_vector, dot, hashed_embedding, snippet_for_query, tokenize


SKILL_HINTS = {
    "go-style-core": "clarity clear simple simplicity concision maintainability comments formatting gofmt readable idiomatic style nesting control flow",
    "go-naming-api-design": "package names naming receiver getters get initialisms exported comments interface api call site stutter constructor",
    "go-errors-panics": "errors error wrap wrapping w sentinel errors.Is errors.As panic recover log logging error strings handle failure",
    "go-testing": "unit tests test table driven subtests test helpers helper t.Helper got want failure messages benchmark assert",
    "go-code-review-checklist": "review correctness api errors tests cancellation style findings",
    "go-concurrency-context": "concurrency concurrent goroutine goroutines channel channels context cancellation cancel canceled deadline timeout leak lifetime sync synchronization mutex atomic errgroup race parallel parallelism worker",
    "go-interfaces-generics": "interface interfaces generic generics type parameter any abstraction dependency ownership boundary implementation method set constraint",
    "go-performance-allocations": "performance allocation allocations allocate benchmark benchmarks pprof profile profiling hot path memory cpu escape capacity slice map",
    "go-project-structure-tooling": "module modules package packages internal cmd go.mod workspace ci lint vet generated code tooling repository project structure",
    "golang-effective": "go effective style api errors testing review idiomatic",
}


def infer_route(query: str) -> str:
    query_terms = set(tokenize(query))
    query_vector = hashed_embedding(query)
    best_route = "golang-effective"
    best_score = -1.0
    best_lexical_overlap = 0.0

    for route, hint in SKILL_HINTS.items():
        if route == "golang-effective":
            continue
        hint_terms = set(tokenize(hint))
        lexical_overlap = len(query_terms & hint_terms) / max(1, len(query_terms))
        vector_score = dot(query_vector, hashed_embedding(hint))
        score = (0.65 * lexical_overlap) + (0.35 * vector_score)
        if score > best_score:
            best_route = route
            best_score = score
            best_lexical_overlap = lexical_overlap

    if best_lexical_overlap > 0:
        return best_route
    return best_route if best_score >= 0.12 else "golang-effective"


def field_overlap_score(query_terms: set[str], text: str) -> float:
    if not query_terms:
        return 0.0
    field_terms = set(tokenize(text))
    if not field_terms:
        return 0.0
    return len(query_terms & field_terms) / len(query_terms)


def ranking_weights(query_terms: set[str]) -> dict[str, float]:
    if len(query_terms) <= 2:
        return {
            "raw_lexical": 0.52,
            "hint_lexical": 0.08,
            "vector": 0.18,
            "title": 0.17,
            "path": 0.05,
        }
    return {
        "raw_lexical": 0.38,
        "hint_lexical": 0.12,
        "vector": 0.34,
        "title": 0.11,
        "path": 0.05,
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


def search(
    index: Path,
    query: str,
    route: str,
    top: int,
    snippet_chars: int | None,
    include_content: bool,
) -> list[dict[str, object]]:
    route_hint = SKILL_HINTS.get(route, route)
    expanded_query = f"{query}\n{route_hint}"
    raw_query_terms = tokenize(query)
    hint_terms = tokenize(route_hint)
    query_vector = hashed_embedding(expanded_query)

    connection = sqlite3.connect(index)
    try:
        chunks = load_chunks(connection)
        raw_lexical = lexical_scores(connection, raw_query_terms, len(chunks))
        hint_lexical = lexical_scores(connection, hint_terms, len(chunks))
    finally:
        connection.close()

    query_term_set = set(tokenize(query))
    weights = ranking_weights(query_term_set)
    results = []
    for chunk in chunks:
        vector_score = max(0.0, dot(query_vector, chunk["vector"]))
        raw_lexical_score = raw_lexical.get(chunk["id"], 0.0)
        hint_lexical_score = hint_lexical.get(chunk["id"], 0.0)
        title_score = field_overlap_score(query_term_set, str(chunk["title"]))
        path_score = field_overlap_score(query_term_set, str(chunk["path"]))
        score = (
            weights["raw_lexical"] * raw_lexical_score
            + weights["hint_lexical"] * hint_lexical_score
            + weights["vector"] * vector_score
            + weights["title"] * title_score
            + weights["path"] * path_score
        )
        result = {
            "score": round(score, 6),
            "vector_score": round(vector_score, 6),
            "lexical_score": round(raw_lexical_score, 6),
            "hint_lexical_score": round(hint_lexical_score, 6),
            "title_score": round(title_score, 6),
            "path_score": round(path_score, 6),
            "_content_sha256": hashlib.sha256(str(chunk["content"]).encode("utf-8")).hexdigest(),
            "path": chunk["path"],
            "title": chunk["title"],
            "source_name": chunk["source_name"],
            "source_url": chunk["source_url"],
            "token_count": chunk["token_count"],
            "snippet": snippet_for_query(str(chunk["content"]), query_term_set, snippet_chars),
        }
        if include_content:
            result["content"] = chunk["content"]
        results.append(result)
    results.sort(key=lambda item: item["score"], reverse=True)
    deduped_results = []
    seen_hashes = set()
    for item in results:
        sha256 = str(item.pop("_content_sha256"))
        if sha256 in seen_hashes:
            continue
        seen_hashes.add(sha256)
        deduped_results.append(item)
        if len(deduped_results) >= top:
            break
    return deduped_results


def print_text(route: str, results: list[dict[str, object]]) -> None:
    total_tokens = sum(int(item["token_count"]) for item in results)
    print(f"route: {route}")
    print(f"total_result_tokens: {total_tokens}")
    for index, item in enumerate(results, 1):
        print(f"\n{index}. {item['path']}")
        print(f"   score: {item['score']}  tokens: {item['token_count']}  source: {item['source_name']}")
        print(f"   title: {item['title']}")
        if item["source_url"]:
            print(f"   url: {item['source_url']}")
        print(f"   snippet: {item['snippet']}")


def query_payload(
    index: Path,
    query: str,
    top: int,
    snippet_chars: int | None,
    include_content: bool,
) -> dict[str, object]:
    route = infer_route(query)
    results = search(index, query, route, top, snippet_chars, include_content)
    return {"query": query, "route": route, "results": results}


def collect_queries(positional_query: str | None, repeated_queries: list[str] | None) -> list[str]:
    queries = []
    if positional_query:
        queries.append(positional_query)
    if repeated_queries:
        queries.extend(repeated_queries)
    return [query.strip() for query in queries if query.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", help="Natural-language query or review finding text")
    parser.add_argument("--query", dest="queries", action="append", help="Repeatable query for batch retrieval")
    parser.add_argument("--index", type=Path, default=Path("sources/index/chunks.sqlite"))
    parser.add_argument("--top", type=int, default=6)
    parser.add_argument("--snippet-chars", type=int, default=320, help="Snippet character budget per result")
    parser.add_argument("--full-snippet", action="store_true", help="Return the full chunk body as the snippet")
    parser.add_argument("--include-content", action="store_true", help="Include full chunk body in JSON output")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    queries = collect_queries(args.query, args.queries)
    if not queries:
        parser.error("provide a positional query or at least one --query value")

    snippet_chars = None if args.full_snippet else args.snippet_chars
    payloads = [
        query_payload(args.index, query, args.top, snippet_chars, args.include_content)
        for query in queries
    ]
    if args.json:
        payload: dict[str, object] = payloads[0] if len(payloads) == 1 else {"queries": payloads}
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        for index, payload in enumerate(payloads):
            if len(payloads) > 1:
                if index:
                    print("\n---")
                print(f"query: {payload['query']}")
            print_text(str(payload["route"]), list(payload["results"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
