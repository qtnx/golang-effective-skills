---
name: golang-effective
description: Source-backed Go task router and baseline workflow. Use when Codex is writing, refactoring, debugging, reviewing, or designing Go code and needs to choose the right Effective Go, Google Go Style, or Uber Go Style guidance without loading unnecessary context.
---

# Golang Effective

Use this as the router for broad Go work.

## Workflow

1. Identify the task type from the prompt and touched code.
2. Read `references/routing.md`, then load one primary adjacent skill.
3. Follow that skill's Load Protocol before giving advice or editing code.
4. Load at most two secondary adjacent skills when the task crosses domains.
5. Prefer local repository conventions unless they harm correctness,
   readability, or testability.
6. When editing Go code, run `gofmt` and the narrowest useful test command.
7. Open source chunks through the selected skill's `source-map.md` when
   grounding a claim, resolving conflicting guidance, or updating a skill.

## Routing

- Style/readability/formatting: `go-style-core`
- Package names, exported API, comments, receiver names: `go-naming-api-design`
- Errors, wrapping, panic/recover, logging: `go-errors-panics`
- Unit tests, table tests, helpers, examples, benchmarks: `go-testing`
- PR/code review: `go-code-review-checklist`

## Guardrails

- Do not load full raw or normalized source docs during ordinary coding tasks.
- Do not treat Effective Go as a complete modern guide for modules or generics.
- Do not invent style rules when a repository has a clear local pattern.
- Do not optimize Go code without evidence when the task is not performance work.

## Source Priority

Read `references/source-priority.md` when guidance conflicts.
