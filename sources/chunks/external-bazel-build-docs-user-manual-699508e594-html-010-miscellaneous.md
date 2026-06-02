---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Options

### Miscellaneous

#### `--flag_alias=alias_name=target_path`

A convenience flag used to bind longer Starlark build settings to a shorter name. For more details, see the Starlark Configurations.

#### `--symlink_prefix=string`

Changes the prefix of the generated convenience symlinks. The default value for the symlink prefix is `bazel-` which will create the symlinks `bazel-bin`, `bazel-testlogs`, and `bazel-genfiles`.

If the symbolic links cannot be created for any reason, a warning is issued but the build is still considered a success. In particular, this allows you to build in a read-only directory or one that you have no permission to write into. Any paths printed in informational messages at the conclusion of a build will only use the symlink-relative short form if the symlinks point to the expected location; in other words, you can rely on the correctness of those paths, even if you cannot rely on the symlinks being created.

Some common values of this option:

-
**Suppress symlink creation:** `--symlink_prefix=/` will cause Bazel to not create or update any symlinks, including the `bazel-out` and `bazel-<workspace>` symlinks. Use this option to suppress symlink creation entirely.

-
**Reduce clutter:** `--symlink_prefix=.bazel/` will cause Bazel to create symlinks called `bin` (etc) inside a hidden directory `.bazel`.

#### `--platform_suffix=string`

Adds a suffix to the configuration short name, which is used to determine the output directory. Setting this option to different values puts the files into different directories, for example to improve cache hit rates for builds that otherwise clobber each others output files, or to keep the output files around for comparisons.

#### `--default_visibility=(private|public)`

Temporary flag for testing bazel default visibility changes. Not intended for general use but documented for completeness' sake.

#### `--starlark_cpu_profile=_file_`

This flag, whose value is the name of a file, causes Bazel to gather statistics about CPU usage by all Starlark threads, and write the profile, in pprof <https://github.com/google/pprof> format, to the named file.

Use this option to help identify Starlark functions that make loading and analysis slow due to excessive computation. For example:

```go

$ bazel build --nobuild --starlark_cpu_profile=/tmp/pprof.gz my/project/...
$ pprof /tmp/pprof.gz
(pprof) top
Type: CPU
Time: Feb 6, 2020 at 12:06pm (PST)
Duration: 5.26s, Total samples = 3.34s (63.55%)
Showing nodes accounting for 3.34s, 100% of 3.34s total
      flat  flat%   sum%        cum   cum%
     1.86s 55.69% 55.69%      1.86s 55.69%  sort_source_files
     1.02s 30.54% 86.23%      1.02s 30.54%  expand_all_combinations
     0.44s 13.17% 99.40%      0.44s 13.17%  range
     0.02s   0.6%   100%      3.34s   100%  sorted
         0     0%   100%      1.38s 41.32%  my/project/main/BUILD
         0     0%   100%      1.96s 58.68%  my/project/library.bzl
         0     0%   100%      3.34s   100%  main

```

For different views of the same data, try the `pprof` commands `svg`, `web`, and `list`.
