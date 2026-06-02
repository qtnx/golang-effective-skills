---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

# Commands and Options   Stay organized with collections   Save and categorize content based on your preferences.

## Using Bazel for releases

Bazel is used both by software engineers during the development cycle, and by release engineers when preparing binaries for deployment to production. This section provides a list of tips for release engineers using Bazel.

### Significant options

When using Bazel for release builds, the same issues arise as for other scripts that perform a build. For more details, see Call Bazel from scripts. In particular, the following options are strongly recommended:

- `--bazelrc=/dev/null`
- `--nokeep_state_after_build`

These options are also important:

- `--package_path`
- `--symlink_prefix`: for managing builds for multiple configurations, it may be convenient to distinguish each build with a distinct identifier, such as "64bit" vs. "32bit". This option differentiates the `bazel-bin` (etc.) symlinks.
