#!/usr/bin/env python3
"""Smoke-test the universal chunk router and retrieval ranking."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from query_chunk_index import infer_route, search


CHECKS = [
    {
        "query": "concurrency",
        "route": "go-concurrency-context",
        "top": 6,
        "required_any": [
            "effective-go-effective-go-html-025-share-by-communicating.md",
            "effective-go-effective-go-html-026-goroutines.md",
            "effective-go-effective-go-html-027-channels.md",
            "effective-go-effective-go-html-029-parallelization.md",
        ],
        "forbidden_any": [
            "google-go-styleguide-decisions-md-014-errors.md",
            "google-go-styleguide-guide-md-006-consistency.md",
        ],
    },
    {
        "query": "goroutine leak cancellation",
        "route": "go-concurrency-context",
        "top": 8,
        "required_any": [
            "google-go-styleguide-decisions-md-022-goroutine-lifetimes.md",
            "uber-go-guide-style-md-019-don-t-fire-and-forget-goroutines.md",
            "external-pkg-go-dev-golang-org-x-sync-errgroup-1521b1c850-html-001-details.md",
        ],
    },
    {
        "query": "error wrapping logging",
        "route": "go-errors-panics",
        "top": 5,
        "required_any": [
            "google-go-styleguide-best-practices-md-009-adding-information-to-errors.md",
            "google-go-styleguide-best-practices-md-010-placement-of-w-in-errors.md",
            "google-go-styleguide-best-practices-md-011-logging-errors.md",
            "uber-go-guide-style-md-010-errors.md",
        ],
    },
    {
        "query": "table driven tests subtests got want",
        "route": "go-testing",
        "top": 5,
        "required_any": [
            "google-go-styleguide-decisions-md-041-table-driven-tests.md",
            "google-go-styleguide-decisions-md-040-subtests.md",
            "uber-go-guide-style-md-036-patterns.md",
        ],
    },
    {
        "query": "package names stutter getters exported comments",
        "route": "go-naming-api-design",
        "top": 8,
        "required_any": [
            "google-go-styleguide-decisions-md-003-package-names.md",
            "external-go-dev-wiki-codereviewcomments-46376b7b23-html-016-package-names.md",
            "external-go-dev-blog-package-names-a6de1f37de-html-001-package-names.md",
        ],
    },
]


def contains_any(paths: list[str], fragments: list[str]) -> bool:
    return any(any(fragment in path for fragment in fragments) for path in paths)


def validate_check(index: Path, check: dict[str, object]) -> list[str]:
    query = str(check["query"])
    expected_route = str(check["route"])
    route = infer_route(query)
    if route != expected_route:
        return [f"{query!r}: route {route!r} != {expected_route!r}"]

    results = search(index, query, route, int(check["top"]), 240, False)
    paths = [str(result["path"]) for result in results]
    errors = []
    required_any = list(check.get("required_any", []))
    if required_any and not contains_any(paths, required_any):
        errors.append(f"{query!r}: missing required chunk in top results: {paths}")

    forbidden_any = list(check.get("forbidden_any", []))
    if forbidden_any and contains_any(paths, forbidden_any):
        errors.append(f"{query!r}: forbidden chunk appeared in top results: {paths}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, default=Path("sources/index/chunks.sqlite"))
    args = parser.parse_args()

    errors = []
    for check in CHECKS:
        errors.extend(validate_check(args.index, check))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("Retrieval smoke checks valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
