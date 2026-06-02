---
name: go-code-review-checklist
description: Source-backed Go code review checklist. Use when Codex is reviewing a Go pull request, auditing agent-generated Go code, doing a final pre-merge pass, or deciding which Go style, API, error, or testing skill should inspect a change.
---

# Go Code Review Checklist

Use this for Go review passes.

## Load Protocol

1. Read `references/checklist.md` before producing review findings.
2. Read `references/examples.md` to calibrate severity and finding shape.
3. For broad review grounding, run:
   `python3 scripts/query_chunk_index.py --skill go-code-review-checklist "<query>"`
4. Read `references/source-map.md` to route each source-backed finding to the
   right task skill.
5. For each non-trivial finding, load the relevant task skill and follow its
   Load Protocol before finalizing the claim.

## Review Order

1. Behavior and API correctness.
2. Error and cancellation paths.
3. Tests and failure quality.
4. Package boundaries and abstractions.
5. Readability and idiomatic style.
6. Performance only when the change touches a hot path or claims speed.

## Do

- Lead with actionable findings and file/line references.
- Verify compile, `gofmt`, and tests when possible.
- Route detailed comments to `go-style-core`, `go-naming-api-design`,
  `go-errors-panics`, or `go-testing`.
- Treat local repository convention as important context.
- Distinguish correctness risk from style preference.

## Avoid

- Bikeshedding formatting that `gofmt` owns.
- Asking for abstractions without a concrete caller or repeated complexity.
- Raising performance folklore without measurement.
- Commenting on a source-backed rule without checking the relevant source map.

## Checklist

Use `references/checklist.md`.

## Source Anchors

Use `references/source-map.md` to route review findings to source-backed
skills and chunks.
