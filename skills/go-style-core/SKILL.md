---
name: go-style-core
description: Source-backed Go style guidance. Use when Codex is writing, rewriting, or reviewing Go code for idiomatic readability, formatting, comments, clarity, simplicity, concision, maintainability, and local consistency.
---

# Go Style Core

Use this for general Go readability and idiom work.

## Apply This First

- Prefer clarity over cleverness.
- Prefer simple control flow over dense one-liners.
- Let `gofmt` decide formatting.
- Explain why in comments; avoid restating obvious code behavior.
- Follow local style when it is readable and correct.

## Do

- Keep happy paths easy to scan.
- Name intermediate values when they make logic clearer.
- Remove abstraction that does not reduce real complexity.
- Use comments to document invariants, decisions, and non-obvious tradeoffs.
- Run `gofmt` after edits.

## Avoid

- Hand-aligned formatting.
- Clever expressions that hide error paths or side effects.
- Generic style nits that do not improve behavior or readability.
- Loading naming, errors, or tests detail when a task is only broad style.

## Review Checklist

Read `references/checklist.md` for a compact style review checklist.

## Source Anchors

Read `references/source-map.md` only when grounding a rule or updating this
skill.
