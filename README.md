# Golang Effective Skills

Source-backed Go skills and agent profiles for Codex: idiomatic Golang code
implementation, Go code review, Effective Go guidance, Google Go Style Guide
checks, Uber Go Style Guide checks, tests, errors, and API naming without
context bloat.

## Why This Exists

General Go style documents are excellent, but they are too broad to load into
an agent context for every task. This repo turns Effective Go, the Google Go
Style Guide, and the Uber Go Style Guide into small task-routed skills.

Agents load one primary skill, optionally load one or two adjacent skills, and
query the local chunk index before opening source chunks for detailed
grounding.

Keywords this project is built around: Go agent skills, Golang best practices,
Codex skills, AI coding agents, Go code review, Effective Go, Google Go Style
Guide, Uber Go Style Guide, Go testing, Go error handling, and idiomatic Go.

## Install

```bash
git clone https://github.com/qtnx/golang-effective-skills.git
cd golang-effective-skills
./scripts/install.sh
```

To overwrite previously installed copies:

```bash
./scripts/install.sh --force
```

Install only skills or only agent profiles:

```bash
./scripts/install.sh --skills-only
./scripts/install.sh --agents-only
```

## Skills

| Skill | Use When | Status |
| --- | --- | --- |
| `golang-effective` | Route broad Go implementation, refactor, debug, or review tasks | MVP |
| `go-style-core` | Improve idiomatic style, readability, formatting, and comments | MVP |
| `go-naming-api-design` | Name packages, exported APIs, receivers, and public comments | MVP |
| `go-errors-panics` | Design/review errors, wrapping, panics, recover, and logging | MVP |
| `go-testing` | Write/review tests, tables, helpers, examples, and benchmarks | MVP |
| `go-code-review-checklist` | Review Go PRs or agent-generated Go code | MVP |
| `go-concurrency-context` | Goroutines, channels, context, cancellation, leaks | Roadmap |
| `go-interfaces-generics` | Interface ownership, abstraction boundaries, generics | Roadmap |
| `go-performance-allocations` | Allocation, benchmarks, pprof, hot paths | Roadmap |
| `go-project-structure-tooling` | Modules, internal packages, CI, lint, generated code | Roadmap |

## Special Agents

These root-level profiles orchestrate the skills above for repeatable subagent
roles.

| Agent | Use When |
| --- | --- |
| `go-implementer` | Implement a Go feature, bug fix, refactor, or test update end to end |
| `go-best-practice-reviewer` | Review Go code against best practices before merge or after agent-generated code |

See [docs/agents.md](docs/agents.md).

## Example Prompts

```text
Use $golang-effective to review this Go package for idiomatic style and test gaps.
```

```text
Use $go-errors-panics to audit this error handling path and tell me where wrapping or logging is wrong.
```

```text
Use $go-testing to rewrite these tests as clear table-driven tests with useful failure messages.
```

## Repository Layout

```text
skills/      Codex skill folders
sources/     Raw, normalized, and chunked source corpus
sources/index/
             Local SQLite chunk index with token counts and hashed embeddings
scripts/     Install, validation, and source-processing scripts
agents/      Reusable implementation and review subagent profiles
fixtures/    Small intentionally flawed Go snippets for validation
docs/        Architecture, provenance, roadmap, and validation notes
```

## Chunk Retrieval

Build or refresh the local embedding index:

```bash
python3 scripts/build_chunk_index.py
```

Query source chunks by task:

```bash
python3 scripts/query_chunk_index.py "when should Go code wrap errors with %w"
python3 scripts/query_chunk_index.py "concurrency"
```

The command is a universal router: it prints the inferred `route`, ranked chunk
paths, token counts, scores, source URLs, and snippets. The index is SQLite and
uses deterministic local hashed n-gram embeddings, so it does not require an API
key. Routes can point to implemented MVP skills or roadmap domains such as
`go-concurrency-context`; roadmap routes still retrieve source chunks directly.

Useful output controls:

```bash
python3 scripts/query_chunk_index.py "error wrapping" --full-snippet
python3 scripts/query_chunk_index.py "error wrapping" --snippet-chars 1000
python3 scripts/query_chunk_index.py "error wrapping" --json --include-content
```

Validate retrieval quality:

```bash
python3 scripts/validate_retrieval.py
```

## Source Provenance

The pack is grounded in:

- [Effective Go](https://go.dev/doc/effective_go)
- [Google Go Style Guide](https://google.github.io/styleguide/go/)
- [Uber Go Style Guide](https://github.com/uber-go/guide/blob/master/style.md)
- Linked external docs referenced by those sources, cached under
  `sources/raw/external/` with a manifest at
  `sources/raw/external-docs-manifest.json`

This is not an official Google, Go, or Uber project. See
[docs/source-provenance.md](docs/source-provenance.md) and
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for source and license
details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New guidance should be task-routed,
source-backed, concise, and validated against fixtures or realistic prompts.

## Security

Report malicious prompt-injection, unsafe install behavior, or source tampering
privately. See [SECURITY.md](SECURITY.md).

## License

Original repository content is MIT licensed. Third-party source documents keep
their own licenses. See [NOTICE.md](NOTICE.md).
