---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

# Commands and Options   Stay organized with collections   Save and categorize content based on your preferences.

## Querying the action graph
 **Caution:** The aquery command is still experimental and its API will change.
The `aquery` command allows you to query for actions in your build graph. It operates on the post-analysis configured target graph and exposes information about actions, artifacts and their relationships.

The tool accepts several command-line options. `--output` selects the output format. The default output format (`text`) is human-readable, use `proto` or `textproto` for machine-readable format. Notably, the aquery command runs on top of a regular Bazel build and inherits the set of options available during a build.

It supports the same set of functions that is also available to traditional `query` but `siblings`, `buildfiles` and `tests`.

For more details, see Action Graph Query.
