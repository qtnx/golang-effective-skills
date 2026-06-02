---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Options

### Workspace status

Use these options to "stamp" Bazel-built binaries: to embed additional information into the binaries, such as the source control revision or other workspace-related information. You can use this mechanism with rules that support the `stamp` attribute, such as `genrule`, `cc_binary`, and more.

#### `--workspace_status_command=program`

This flag lets you specify a binary that Bazel runs before each build. The program can report information about the status of the workspace, such as the current source control revision.

The flag's value must be a path to a native program. On Linux/macOS this may be any executable. On Windows this must be a native binary, typically an ".exe", ".bat", or a ".cmd" file.

The program should print zero or more key/value pairs to standard output, one entry on each line, then exit with zero (otherwise the build fails). The key names can be anything but they may only use upper case letters and underscores. The first space after the key name separates it from the value. The value is the rest of the line (including additional whitespaces). Neither the key nor the value may span multiple lines. Keys must not be duplicated.

Bazel partitions the keys into two buckets: "stable" and "volatile". (The names "stable" and "volatile" are a bit counter-intuitive, so don't think much about them.)

Bazel then writes the key-value pairs into two files:

- `bazel-out/stable-status.txt` contains all keys and values where the key's name starts with `STABLE_`
- `bazel-out/volatile-status.txt` contains the rest of the keys and their values

The contract is:

-
"stable" keys' values should change rarely, if possible. If the contents of `bazel-out/stable-status.txt` change, Bazel invalidates the actions that depend on them. In other words, if a stable key's value changes, Bazel will rerun stamped actions. Therefore the stable status should not contain things like timestamps, because they change all the time, and would make Bazel rerun stamped actions with each build.

Bazel always outputs the following stable keys:

- `BUILD_EMBED_LABEL`: value of `--embed_label`
- `BUILD_HOST`: the name of the host machine that Bazel is running on
- `BUILD_USER`: the name of the user that Bazel is running as

-
"volatile" keys' values may change often. Bazel expects them to change all the time, like timestamps do, and duly updates the `bazel-out/volatile-status.txt` file. In order to avoid rerunning stamped actions all the time though, **Bazel pretends that the volatile file never changes**. In other words, if the volatile status file is the only file whose contents has changed, Bazel will not invalidate actions that depend on it. If other inputs of the actions have changed, then Bazel reruns that action, and the action will see the updated volatile status, but just the volatile status changing alone will not invalidate the action.

Bazel always outputs the following volatile keys:

- `BUILD_TIMESTAMP`: time of the build in seconds since the Unix Epoch (the value of `System.currentTimeMillis()` divided by a thousand)
- `FORMATTED_DATE`: time of the build Formatted as `yyyy MMM d HH mm ss EEE`(for example 2023 Jun 2 01 44 29 Fri) in UTC.

On Linux/macOS you can pass `--workspace_status_command=/bin/true` to disable retrieving workspace status, because `true` does nothing, successfully (exits with zero) and prints no output. On Windows you can pass the path of MSYS's `true.exe` for the same effect.

If the workspace status command fails (exits non-zero) for any reason, the build will fail.

Example program on Linux using Git:

```go

#!/bin/bash
echo "CURRENT_TIME $(date +%s)"
echo "RANDOM_HASH $(cat /proc/sys/kernel/random/uuid)"
echo "STABLE_GIT_COMMIT $(git rev-parse HEAD)"
echo "STABLE_USER_NAME $USER"

```

Pass this program's path with `--workspace_status_command`, and the stable status file will include the STABLE lines and the volatile status file will include the rest of the lines.

#### `--[no]stamp`

This option, in conjunction with the `stamp` rule attribute, controls whether to embed build information in binaries.

Stamping can be enabled or disabled explicitly on a per-rule basis using the `stamp` attribute. Please refer to the Build Encyclopedia for details. When a rule sets `stamp = -1` (the default for `*_binary` rules), this option determines whether stamping is enabled.

Bazel never stamps binaries that are built for the exec configuration, regardless of this option or the `stamp` attribute. For rules that set `stamp = 0` (the default for `*_test` rules), stamping is disabled regardless of `--[no]stamp`. Specifying `--stamp` does not force targets to be rebuilt if their dependencies have not changed.

Setting `--nostamp` is generally desireable for build performance, as it reduces input volatility and maximizes build caching.
