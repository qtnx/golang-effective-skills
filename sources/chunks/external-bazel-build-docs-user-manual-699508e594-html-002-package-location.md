---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Options
The following sections describe the options available during a build. When `--long` is used on a help command, the on-line help messages provide summary information about the meaning, type and default value for each option.
Most options can only be specified once. When specified multiple times, the last instance wins. Options that can be specified multiple times are identified in the on-line help with the text 'may be used multiple times'.
### Package location

#### `--package_path`

**WARNING:** The `--package_path` option is deprecated. Bazel prefers packages in the main repository to be under the workspace root.

This option specifies the set of directories that are searched to find the BUILD file for a given package.

Bazel finds its packages by searching the package path. This is a colon separated ordered list of bazel directories, each being the root of a partial source tree.

_To specify a custom package path_ using the `--package_path` option:

```go

  % bazel build --package_path %workspace%:/some/other/root

```

Package path elements may be specified in three formats:

- If the first character is `/`, the path is absolute.
- If the path starts with `%workspace%`, the path is taken relative to the nearest enclosing bazel directory. For instance, if your working directory is `/home/bob/clients/bob_client/bazel/foo`, then the string `%workspace%` in the package-path is expanded to `/home/bob/clients/bob_client/bazel`.
- Anything else is taken relative to the working directory. This is usually not what you mean to do, and may behave unexpectedly if you use Bazel from directories below the bazel workspace. For instance, if you use the package-path element `.`, and then cd into the directory `/home/bob/clients/bob_client/bazel/foo`, packages will be resolved from the `/home/bob/clients/bob_client/bazel/foo` directory.

If you use a non-default package path, specify it in your Bazel configuration file for convenience.

_Bazel doesn't require any packages to be in the current directory_, so you can do a build from an empty bazel workspace if all the necessary packages can be found somewhere else on the package path.

Example: Building from an empty client

```go

  % mkdir -p foo/bazel
  % cd foo/bazel
  % touch MODULE.bazel
  % bazel build --package_path /some/other/path //foo

```

#### `--deleted_packages`

This option specifies a comma-separated list of packages which Bazel should consider deleted, and not attempt to load from any directory on the package path. This can be used to simulate the deletion of packages without actually deleting them. This option can be passed multiple times, in which case the individual lists are concatenated.
