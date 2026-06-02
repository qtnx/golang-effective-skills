---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

# Commands and Options   Stay organized with collections   Save and categorize content based on your preferences.

## Running executables

The `bazel run` command is similar to `bazel build`, except it is used to build _and run_ a single target. Here is a typical session (`//java/myapp:myapp` says hello and prints out its args):

```go

  % bazel run java/myapp:myapp -- --arg1 --arg2
  INFO: Analyzed target //java/myapp:myapp (13 packages loaded, 27 targets configured).
  INFO: Found 1 target...
  Target //java/myapp:myapp up-to-date:
    bazel-bin/java/myapp/myapp
  INFO: Elapsed time: 14.290s, Critical Path: 5.54s, ...
  INFO: Build completed successfully, 4 total actions
  INFO: Running command line: bazel-bin/java/myapp/myapp <args omitted>
  Hello there
  $EXEC_ROOT/java/myapp/myapp
  --arg1
  --arg2

```
 **Note:** `--` is needed so that Bazel does not interpret `--arg1` and `--arg2` as Bazel options, but rather as part of the command line for running the binary. Additionally, Bazel will avoid logging these arguments to the console in case they contain sensitive information.
`bazel run` is similar, but not identical, to directly invoking the binary built by Bazel and its behavior is different depending on whether the binary to be invoked is a test or not.

When the binary is not a test, the current working directory will be the runfiles tree of the binary.

When the binary is a test, the current working directory will be the exec root and a good-faith attempt is made to replicate the environment tests are usually run in. The emulation is not perfect, though, and tests that have multiple shards cannot be run this way (the `--test_sharding_strategy=disabled` command line option can be used to work around this)

The following extra environment variables are also available to the binary:

- `BUILD_WORKSPACE_DIRECTORY`: the root of the workspace where the build was run.
- `BUILD_WORKING_DIRECTORY`: the current working directory where Bazel was run from.
- `BUILD_ID`: the build ID of the `bazel run` invocation. This is usually unique, except if Bazel was run with `--script_path` and the resulting script is re-used.
- `BUILD_EXECROOT`: the execution root of the `bazel run` invocation.

These can be used, for example, to interpret file names on the command line in a user-friendly way.

### Options for `bazel run`

#### `--run_under=command-prefix`

This has the same effect as the `--run_under` option for `bazel test` (see above), except that it applies to the command being run by `bazel run` rather than to the tests being run by `bazel test` and cannot run under label.

#### Filtering logging outputs from Bazel

When invoking a binary with `bazel run`, Bazel prints logging output from Bazel itself and the binary under invocation. To make the logs less noisy, you can suppress the outputs from Bazel itself with the `--ui_event_filters` and `--noshow_progress` flags.

For example: `bazel run --ui_event_filters=-info,-stdout,-stderr --noshow_progress //java/myapp:myapp`

### Executing tests

`bazel run` can also execute test binaries, which has the effect of running the test in a close approximation of the environment described at Writing Tests. Note that none of the `--test_*` arguments have an effect when running a test in this manner except `--test_arg` .
