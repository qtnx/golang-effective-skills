---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

# Commands and Options   Stay organized with collections   Save and categorize content based on your preferences.

The environment can be accessed from within a test by using `System.getenv("var")` (Java), `getenv("var")` (C or C++),

#### `--run_under=command-prefix`

This specifies a prefix that the test runner will insert in front of the test command before running it. The command-prefix is split into words using Bourne shell tokenization rules, and then the list of words is prepended to the command that will be executed.

If the first word is a fully-qualified label (starts with `//`) it is built. Then the label is substituted by the corresponding executable location that is prepended to the command that will be executed along with the other words.

Some caveats apply:

- The PATH used for running tests may be different than the PATH in your environment, so you may need to use an **absolute path** for the `--run_under` command (the first word in command-prefix).
- **`stdin` is not connected**, so `--run_under` can't be used for interactive commands.

Examples:

```go

--run_under=/usr/bin/strace
        --run_under='/usr/bin/strace -c'
        --run_under=/usr/bin/valgrind
        --run_under='/usr/bin/valgrind --quiet --num-callers=20'

```

#### Test selection

As documented under Output selection options, you can filter tests by size, timeout, tag, or language. A convenience general name filter can forward particular filter args to the test runner.

#### Other options for `bazel test`

The syntax and the remaining options are exactly like `bazel build`.
