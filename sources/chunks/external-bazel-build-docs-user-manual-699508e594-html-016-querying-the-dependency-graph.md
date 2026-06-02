---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

# Commands and Options   Stay organized with collections   Save and categorize content based on your preferences.

## Querying the dependency graph

Bazel includes a query language for asking questions about the dependency graph used during the build. The query language is used by two commands: query and cquery. The major difference between the two commands is that query runs after the loading phase and cquery runs after the analysis phase. These tools are an invaluable aid to many software engineering tasks.

The query language is based on the idea of algebraic operations over graphs; it is documented in detail in

Bazel Query Reference. Please refer to that document for reference, for examples, and for query-specific command-line options.

The query tool accepts several command-line option. `--output` selects the output format. `--[no]keep_going` (disabled by default) causes the query tool to continue to make progress upon errors; this behavior may be disabled if an incomplete result is not acceptable in case of errors.

The `--[no]tool_deps` option, enabled by default, causes dependencies in non-target configurations to be included in the dependency graph over which the query operates.

The `--[no]implicit_deps` option, enabled by default, causes implicit dependencies to be included in the dependency graph over which the query operates. An implicit dependency is one that is not explicitly specified in the BUILD file but added by bazel.

Example: "Show the locations of the definitions (in BUILD files) of all genrules required to build all the tests in the PEBL tree."

```go

  bazel query --output location 'kind(genrule, deps(kind(".*_test rule", foo/bar/pebl/...)))'

```
