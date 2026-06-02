---
name: go-testing
description: Source-backed Go testing guidance. Use when Codex is writing or reviewing Go unit tests, table-driven tests, subtests, test helpers, useful failure messages, fakes, examples, benchmarks, golden files, or deterministic test setup.
---

# Go Testing

Use this for Go tests and test review.

## Load Protocol

1. Read `references/checklist.md` before writing or reviewing tests.
2. Read `references/examples.md` before rewriting table tests, helpers, or
   failure messages.
3. Before citing table-test, subtest, helper, `t.Fatal`, or failure output
   guidance, run:
   `python3 scripts/query_chunk_index.py --skill go-testing "<query>"`
4. Open only the returned `sources/chunks/...` files that fit the task budget.
5. Use `references/source-map.md` as fallback when retrieval is too broad.
6. For error semantics or API design under test, load `go-errors-panics` or
   `go-naming-api-design` as an adjacent skill.

## Apply This First

- Test behavior, not implementation details.
- Use table-driven tests when cases share setup and assertions.
- Give table rows names that explain the scenario.
- Use subtests for named cases.
- Call `t.Helper()` inside helper functions.
- Make failures identify input, got, and want.

## Do

- Keep setup scoped to the tests that need it.
- Prefer simple fakes over complex mocks when feasible.
- Control time, randomness, filesystem, network, and concurrency.
- Use `t.Fatal` only when continuing would make later checks invalid.
- Keep benchmark setup outside the measured section.

## Avoid

- Assertion output that hides the scenario.
- Table tests with unrelated behaviors in one table.
- Calling `t.Fatal` from a separate goroutine.
- Shared mutable test state without reset.

## Review Checklist

Use `references/checklist.md`.

## Source Anchors

Use `references/source-map.md` to choose exact testing chunks.
