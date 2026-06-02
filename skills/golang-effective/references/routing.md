# Routing

Load one primary skill and at most two adjacent skills.

| Signals | Primary Skill | Adjacent Skills |
| --- | --- | --- |
| idiomatic, readability, formatting, comments, clarity | `go-style-core` | `go-naming-api-design`, `go-code-review-checklist` |
| package, exported API, receiver, getter, stutter, interface boundary | `go-naming-api-design` | `go-style-core`, `go-testing` |
| error, wrap, `%w`, `errors.Is`, panic, recover, logging | `go-errors-panics` | `go-testing`, `go-code-review-checklist` |
| test, table, subtest, helper, fake, benchmark, golden | `go-testing` | `go-errors-panics`, `go-style-core` |
| review, PR, audit, final pass, agent-generated code | `go-code-review-checklist` | one or two issue-specific skills |

Backlog routing:

- goroutine, channel, context, cancellation, leak: `go-concurrency-context`
- generic, `any`, abstraction ownership: `go-interfaces-generics`
- allocation, benchmark, pprof, hot path: `go-performance-allocations`
- module, `internal`, CI, lint, generated code: `go-project-structure-tooling`

If a backlog skill is not implemented yet, use `go-code-review-checklist` plus
the closest MVP skill and read relevant source chunks directly.
