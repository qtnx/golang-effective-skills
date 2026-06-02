---
name: go-naming-api-design
description: Source-backed Go naming and API design guidance. Use when Codex is choosing or reviewing package names, exported identifiers, receiver names, getters, comments, constructors, interface boundaries, or public API call-site readability.
---

# Go Naming API Design

Use this when names or exported API shape affect the caller.

## Load Protocol

1. Read `references/checklist.md` before reviewing exported names or APIs.
2. Read `references/examples.md` before proposing renames or API reshapes.
3. Before citing package naming, getters, receivers, comments, or interface
   guidance, run:
   `python3 scripts/query_chunk_index.py --skill go-naming-api-design "<query>"`
4. Open only the returned `sources/chunks/...` files that fit the task budget.
5. Use `references/source-map.md` as fallback when retrieval is too broad.
6. For tests or error APIs, load `go-testing` or `go-errors-panics` as an
   adjacent skill.

## Apply This First

- Read names from the call site.
- Keep package names short, lower-case, and domain-specific.
- Avoid `util`, `common`, and `helper` when a domain name exists.
- Avoid stutter between package and exported symbol names.
- Use `Name()`, not `GetName()`, for ordinary getters.
- Keep receiver names short and consistent for the type.

## Do

- Put exported comments on exported API.
- Make interface ownership explicit; prefer consumer-owned narrow interfaces.
- Return concrete types unless an interface return is a deliberate boundary.
- Use initialisms consistently, such as `ID`, `URL`, and `HTTP`.
- Check whether an API reads naturally in realistic caller code.

## Avoid

- Broad exported interfaces for future-proofing.
- Package names that describe architecture layers instead of capability.
- Comments that duplicate the identifier without adding behavior or contract.
- Renaming imports unless it prevents real ambiguity.

## Review Checklist

Use `references/checklist.md`.

## Source Anchors

Use `references/source-map.md` to choose exact naming and API chunks.
