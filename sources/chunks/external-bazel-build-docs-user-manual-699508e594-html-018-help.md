---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Miscellaneous commands and options
### `help`

The `help` command provides on-line help. By default, it shows a summary of available commands and help topics, as shown in Building with Bazel. Specifying an argument displays detailed help for a particular topic. Most topics are Bazel commands, such as `build` or `query`, but there are some additional help topics that do not correspond to commands.

#### `--[no]long` (`-l`)

By default, `bazel help [topic]` prints only a summary of the relevant options for a topic. If the `--long` option is specified, the type, default value and full description of each option is also printed.

## Miscellaneous commands and options

### `shutdown`

Bazel server processes may be stopped by using the `shutdown` command. This command causes the Bazel server to exit as soon as it becomes idle (for example, after the completion of any builds or other commands that are currently in progress). For more details, see Client/server implementation.

Bazel servers stop themselves after an idle timeout, so this command is rarely necessary; however, it can be useful in scripts when it is known that no further builds will occur in a given workspace.

`shutdown` accepts one option, `--iff_heap_size_greater_than _n_`, which requires an integer argument (in MB). If specified, this makes the shutdown conditional on the amount of memory already consumed. This is useful for scripts that initiate a lot of builds, as any memory leaks in the Bazel server could cause it to crash spuriously on occasion; performing a conditional restart preempts this condition.
