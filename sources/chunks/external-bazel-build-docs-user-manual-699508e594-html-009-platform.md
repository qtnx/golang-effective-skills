---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Options

### Platform

Use these options to control the host and target platforms that configure how builds work, and to control what execution platforms and toolchains are available to Bazel rules.

Please see background information on Platforms and Toolchains.

#### `--platforms=labels`

The labels of the platform rules describing the target platforms for the current command.

#### `--host_platform=label`

The label of a platform rule that describes the host system.

#### `--extra_execution_platforms=labels`

The platforms that are available as execution platforms to run actions. Platforms can be specified by exact target, or as a target pattern. These platforms will be considered before those declared in MODULE.bazel files by register_execution_platforms(). This option accepts a comma-separated list of platforms in order of priority. If the flag is passed multiple times, the most recent overrides.

#### `--extra_toolchains=labels`

The toolchain rules to be considered during toolchain resolution. Toolchains can be specified by exact target, or as a target pattern. These toolchains will be considered before those declared in MODULE.bazel files by register_toolchains().

#### `--toolchain_resolution_debug=regex`

Print debug information while finding toolchains if the toolchain type matches the regex. Multiple regexes can be separated by commas. The regex can be negated by using a `-` at the beginning. This might help developers of Bazel or Starlark rules with debugging failures due to missing toolchains.
