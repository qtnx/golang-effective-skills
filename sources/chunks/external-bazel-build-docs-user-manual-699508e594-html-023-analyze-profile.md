---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Miscellaneous commands and options

### `analyze-profile`

The `analyze-profile` command analyzes a JSON trace profile previously gathered during a Bazel invocation.

## Miscellaneous commands and options

### `canonicalize-flags`

The `canonicalize-flags` command, which takes a list of options for a Bazel command and returns a list of options that has the same effect. The new list of options is canonical. For example, two lists of options with the same effect are canonicalized to the same new list.

The `--for_command` option can be used to select between different commands. At this time, only `build` and `test` are supported. Options that the given command does not support cause an error.
 **Note:** A small number of options cannot be reordered, because Bazel cannot ensure that the effect is identical. Also note that this command _does not_ expand flags from `--config`.
As an example:

```go

  % bazel canonicalize-flags -- --config=any_name --test_tag_filters="-lint"
  --config=any_name
  --test_tag_filters=-lint

```
