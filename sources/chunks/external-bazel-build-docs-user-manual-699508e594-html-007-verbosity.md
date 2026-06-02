---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Options

### Verbosity

These options control the verbosity of Bazel's output, either to the terminal, or to additional log files.

#### `--explain=logfile`

This option, which requires a filename argument, causes the dependency checker in `bazel build`'s execution phase to explain, for each build step, either why it is being executed, or that it is up-to-date. The explanation is written to _logfile_.

If you are encountering unexpected rebuilds, this option can help to understand the reason. Add it to your `.bazelrc` so that logging occurs for all subsequent builds, and then inspect the log when you see an execution step executed unexpectedly. This option may carry a small performance penalty, so you might want to remove it when it is no longer needed.

#### `--verbose_explanations`

This option increases the verbosity of the explanations generated when the --explain option is enabled.

In particular, if verbose explanations are enabled, and an output file is rebuilt because the command used to build it has changed, then the output in the explanation file will include the full details of the new command (at least for most commands).

Using this option may significantly increase the length of the generated explanation file and the performance penalty of using `--explain`.

If `--explain` is not enabled, then `--verbose_explanations` has no effect.

#### `--profile=file`

This option, which takes a filename argument, causes Bazel to write profiling data into a file. The data then can be analyzed or parsed using the `bazel analyze-profile` command. The Build profile can be useful in understanding where Bazel's `build` command is spending its time.

#### `--[no]show_loading_progress`

This option causes Bazel to output package-loading progress messages. If it is disabled, the messages won't be shown.

#### `--[no]show_progress`

This option causes progress messages to be displayed; it is on by default. When disabled, progress messages are suppressed.

#### `--show_progress_rate_limit=n`

This option causes bazel to display at most one progress message per `n` seconds, where n is a real number. The default value for this option is 0.02, meaning bazel will limit the progress messages to one per every 0.02 seconds.

#### `--show_result=n`

This option controls the printing of result information at the end of a `bazel build` command. By default, if a single build target was specified, Bazel prints a message stating whether or not the target was successfully brought up-to-date, and if so, the list of output files that the target created. If multiple targets were specified, result information is not displayed.

While the result information may be useful for builds of a single target or a few targets, for large builds (such as an entire top-level project tree), this information can be overwhelming and distracting; this option allows it to be controlled. `--show_result` takes an integer argument, which is the maximum number of targets for which full result information should be printed. By default, the value is 1. Above this threshold, no result information is shown for individual targets. Thus zero causes the result information to be suppressed always, and a very large value causes the result to be printed always.

Users may wish to choose a value in-between if they regularly alternate between building a small group of targets (for example, during the compile-edit-test cycle) and a large group of targets (for example, when establishing a new workspace or running regression tests). In the former case, the result information is very useful whereas in the latter case it is less so. As with all options, this can be specified implicitly via the `.bazelrc` file.

The files are printed so as to make it easy to copy and paste the filename to the shell, to run built executables. The "up-to-date" or "failed" messages for each target can be easily parsed by scripts which drive a build.

#### `--sandbox_debug`

This option causes Bazel to print extra debugging information when using sandboxing for action execution. This option also preserves sandbox directories, so that the files visible to actions during execution can be examined.

#### `--subcommands` (`-s`)

This option causes Bazel's execution phase to print the full command line for each command prior to executing it.

```go

  >>>>> # //examples/cpp:hello-world [action 'Linking examples/cpp/hello-world']
  (cd /home/johndoe/.cache/bazel/_bazel_johndoe/4c084335afceb392cfbe7c31afee3a9f/bazel && \
    exec env - \
    /usr/bin/gcc -o bazel-out/local-fastbuild/bin/examples/cpp/hello-world -B/usr/bin/ -Wl,-z,relro,-z,now -no-canonical-prefixes -pass-exit-codes -Wl,-S -Wl,@bazel-out/local_linux-fastbuild/bin/examples/cpp/hello-world-2.params)

```

Where possible, commands are printed in a Bourne shell compatible syntax, so that they can be easily copied and pasted to a shell command prompt. (The surrounding parentheses are provided to protect your shell from the `cd` and `exec` calls; be sure to copy them!) However some commands are implemented internally within Bazel, such as creating symlink trees. For these there's no command line to display.

`--subcommands=pretty_print` may be passed to print the arguments of the command as a list rather than as a single line. This may help make long command lines more readable.

See also --verbose_failures, below.

For logging subcommands to a file in a tool-friendly format, see --execution_log_json_file and --execution_log_binary_file.

#### `--verbose_failures`

This option causes Bazel's execution phase to print the full command line for commands that failed. This can be invaluable for debugging a failing build.

Failing commands are printed in a Bourne shell compatible syntax, suitable for copying and pasting to a shell prompt.
