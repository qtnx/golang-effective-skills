---
name: go-testing
description: Source-backed Go testing guidance. Use when Codex is writing or reviewing Go unit tests, table-driven tests, subtests, test helpers, useful failure messages, fakes, examples, benchmarks, golden files, or deterministic test setup.
---

# Go Testing

Use this for Go tests and test review.

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

Read `references/checklist.md`.

## Source Anchors

Read `references/source-map.md` when grounding test guidance.
