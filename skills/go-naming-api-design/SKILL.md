---
name: go-naming-api-design
description: Source-backed Go naming and API design guidance. Use when Codex is choosing or reviewing package names, exported identifiers, receiver names, getters, comments, constructors, interface boundaries, or public API call-site readability.
---

# Go Naming API Design

Use this when names or exported API shape affect the caller.

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

Read `references/checklist.md`.

## Source Anchors

Read `references/source-map.md` for source-backed naming and API rules.
