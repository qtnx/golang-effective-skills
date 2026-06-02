---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Miscellaneous commands and options

### `version` and `--version`

The version command prints version details about the built Bazel binary, including the changelist at which it was built and the date. These are particularly useful in determining if you have the latest Bazel, or if you are reporting bugs. Some of the interesting values are:

- `changelist`: the changelist at which this version of Bazel was released.
- `label`: the release label for this Bazel instance, or "development version" if this is not a released binary. Very useful when reporting bugs.

`bazel --version`, with no other args, will emit the same output as `bazel version --gnu_format`, except without the side-effect of potentially starting a Bazel server or unpacking the server archive. `bazel --version` can be run from anywhere - it does not require a workspace directory.
