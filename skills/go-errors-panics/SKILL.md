---
name: go-errors-panics
description: Source-backed Go error and panic guidance. Use when Codex is writing or reviewing error returns, error wrapping, sentinel or custom errors, errors.Is/errors.As, panic/recover, initialization checks, logging errors, or tests for error behavior.
---

# Go Errors Panics

Use this for error behavior and panic policy.

## Load Protocol

1. Read `references/checklist.md` before writing or reviewing error handling.
2. Read `references/examples.md` before changing wrapping, logging, sentinels,
   or panic behavior.
3. Before citing error strings, `%w`, panic/recover, logging, or sentinel
   guidance, run:
   `python3 scripts/query_chunk_index.py --skill go-errors-panics "<query>"`
4. Open only the returned `sources/chunks/...` files that fit the task budget.
5. Use `references/source-map.md` as fallback when retrieval is too broad.
6. For tests that assert errors, load `go-testing` as an adjacent skill.

## Apply This First

- Errors are ordinary values; return them when callers can handle failure.
- Keep the happy path visible with early returns on failure.
- Add context at boundaries where the caller needs it.
- Use `%w` only when callers should inspect the wrapped error.
- Use `%v` or plain text when exposing identity would be harmful.
- Panic only for programmer errors, impossible states, or init invariants.

## Do

- Keep error strings lower-case and without unnecessary punctuation.
- Log an error once at the layer that can add useful operational context.
- Test error semantics when callers depend on `errors.Is` or `errors.As`.
- Decide whether sentinel/custom errors are part of the public API.

## Avoid

- Ignoring errors with `_`.
- Logging and returning the same error through multiple layers.
- Wrapping every error automatically.
- Using panic for expected runtime failure.

## Review Checklist

Use `references/checklist.md`.

## Source Anchors

Use `references/source-map.md` to choose exact error and panic chunks.
