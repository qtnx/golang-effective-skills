---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

# Commands and Options   Stay organized with collections   Save and categorize content based on your preferences.

## Cleaning build outputs

### The `clean` command

Bazel has a `clean` command, analogous to that of Make. It deletes the output directories for all build configurations performed by this Bazel instance, or the entire working tree created by this Bazel instance, and resets internal caches. If executed without any command-line options, then the output directory for all configurations will be cleaned.

Recall that each Bazel instance is associated with a single workspace, thus the `clean` command will delete all outputs from all builds you've done with that Bazel instance in that workspace.

To completely remove the entire working tree created by a Bazel instance, you can specify the `--expunge` option. When executed with `--expunge`, the clean command simply removes the entire output base tree which, in addition to the build output, contains all temp files created by Bazel. It also stops the Bazel server after the clean, equivalent to the `shutdown` command. For example, to clean up all disk and memory traces of a Bazel instance, you could specify:

```go

  % bazel clean --expunge

```

Alternatively, you can expunge in the background by using `--expunge_async`. It is safe to invoke a Bazel command in the same client while the asynchronous expunge continues to run.
 **Note:** This may introduce IO contention.
The `clean` command is provided primarily as a means of reclaiming disk space for workspaces that are no longer needed. Bazel's incremental rebuilds may not be perfect so `clean` can be used to recover a consistent state when problems arise.

Bazel's design is such that these problems are fixable and these bugs are a high priority to be fixed. If you ever find an incorrect incremental build, file a bug report, and report bugs in the tools rather than using `clean`.
