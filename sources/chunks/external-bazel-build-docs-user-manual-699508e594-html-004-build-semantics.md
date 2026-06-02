---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Options

### Build semantics

These options affect the build commands and/or the output file contents.

#### `--compilation_mode (fastbuild|opt|dbg)` (-c)

The `--compilation_mode` option (often shortened to `-c`, especially `-c opt`) takes an argument of `fastbuild`, `dbg` or `opt`, and affects various C/C++ code-generation options, such as the level of optimization and the completeness of debug tables. Bazel uses a different output directory for each different compilation mode, so you can switch between modes without needing to do a full rebuild _every_ time.

- `fastbuild` means build as fast as possible: generate minimal debugging information (`-gmlt -Wl,-S`), and don't optimize. This is the default. Note: `-DNDEBUG` will **not** be set.
- `dbg` means build with debugging enabled (`-g`), so that you can use gdb (or another debugger).
- `opt` means build with optimization enabled and with `assert()` calls disabled (`-O2 -DNDEBUG`). Debugging information will not be generated in `opt` mode unless you also pass `--copt -g`.

#### `--cpu=cpu`

This option specifies the target CPU architecture to be used for the compilation of binaries during the build.
 **Note:** A particular combination of crosstool version, compiler version, and target CPU is allowed only if it has been specified in the currently used CROSSTOOL file.
#### `--action_env=VAR=VALUE`

Specifies the set of environment variables available during the execution of all actions. Variables can be either specified by name, in which case the value will be taken from the invocation environment, or by the `name=value` pair which sets the value independent of the invocation environment.

This `--action_env` flag can be specified multiple times. If a value is assigned to the same variable across multiple `--action_env` flags, the latest assignment wins.

#### `--experimental_action_listener=label`
 **Warning:** Extra actions are deprecated. Use aspects instead.
The `experimental_action_listener` option instructs Bazel to use details from the `action_listener` rule specified by label to insert `extra_actions` into the build graph.

#### `--[no]experimental_extra_action_top_level_only`
 **Warning:** Extra actions are deprecated. Use aspects instead.
If this option is set to true, extra actions specified by the  `--experimental_action_listener` command line option will only be scheduled for top level targets.

#### `--experimental_extra_action_filter=regex`
 **Warning:** Extra actions are deprecated. Use aspects instead.
The `experimental_extra_action_filter` option instructs Bazel to filter the set of targets to schedule `extra_actions` for.

This flag is only applicable in combination with the `--experimental_action_listener` flag.

By default all `extra_actions` in the transitive closure of the requested targets-to-build get scheduled for execution. `--experimental_extra_action_filter` will restrict scheduling to `extra_actions` of which the owner's label matches the specified regular expression.

The following example will limit scheduling of `extra_actions` to only apply to actions of which the owner's label contains '/bar/':

```go
% bazel build --experimental_action_listener=//test:al //foo/... \
  --experimental_extra_action_filter=.*/bar/.*

```

#### `--host_cpu=cpu`

This option specifies the name of the CPU architecture that should be used to build host tools.

#### `--android_platforms=platform[,platform]*`

The platforms to build the transitive `deps` of `android_binary` rules (specifically for native dependencies like C++). For example, if a `cc_library` appears in the transitive `deps` of an `android_binary` rule it is be built once for each platform specified with `--android_platforms` for the `android_binary` rule, and included in the final output.

There is no default value for this flag: a custom Android platform must be defined and used.

One `.so` file is created and packaged in the APK for each platform specified with `--android_platforms`. The `.so` file's name prefixes the name of the `android_binary` rule with "lib". For example, if the name of the `android_binary` is "foo", then the file is `libfoo.so`.

#### `--per_file_copt=[+-]regex[,[+-]regex]...@option[,option]...`

When present, any C++ file with a label or an execution path matching one of the inclusion regex expressions and not matching any of the exclusion expressions will be built with the given options. The label matching uses the canonical form of the label (i.e //`package`:`label_name`).

The execution path is the relative path to your workspace directory including the base name (including extension) of the C++ file. It also includes any platform dependent prefixes.
 **Note:** If only one of the label or the execution path matches the options will be used.
To match the generated files (such as genrule outputs) Bazel can only use the execution path. In this case the regexp shouldn't start with '//' since that doesn't match any execution paths. Package names can be used like this: `--per_file_copt=base/.*\.pb\.cc@-g0`. This will match every `.pb.cc` file under a directory called `base`.

This option can be used multiple times.

The option is applied regardless of the compilation mode used. For example, it is possible to compile with `--compilation_mode=opt` and selectively compile some files with stronger optimization turned on, or with optimization disabled.

**Caveat**: If some files are selectively compiled with debug symbols the symbols might be stripped during linking. This can be prevented by setting `--strip=never`.

**Syntax**: `[+-]regex[,[+-]regex]...@option[,option]...` Where `regex` stands for a regular expression that can be prefixed with a `+` to identify include patterns and with `-` to identify exclude patterns. `option` stands for an arbitrary option that is passed to the C++ compiler. If an option contains a `,` it has to be quoted like so `\,`. Options can also contain `@`, since only the first `@` is used to separate regular expressions from options.

**Example**: `--per_file_copt=//foo:.*\.cc,-//foo:file\.cc@-O0,-fprofile-arcs` adds the `-O0` and the `-fprofile-arcs` options to the command line of the C++ compiler for all `.cc` files in `//foo/` except `file.cc`.

#### `--dynamic_mode=mode`

Determines whether C++ binaries will be linked dynamically, interacting with the linkstatic attribute on build rules.

Modes:

- `default`: Allows bazel to choose whether to link dynamically. See linkstatic for more information.
- `fully`: Links all targets dynamically. This will speed up linking time, and reduce the size of the resulting binaries.
- `off`: Links all targets in mostly static mode. If `-static` is set in linkopts, targets will change to fully static.

#### `--fission (yes|no|[dbg][,opt][,fastbuild])`

Enables Fission <https://gcc.gnu.org/wiki/DebugFission>, which writes C++ debug information to dedicated .dwo files instead of .o files, where it would otherwise go. This substantially reduces the input size to links and can reduce link times.

When set to `[dbg][,opt][,fastbuild]` (example: `--fission=dbg,fastbuild`), Fission is enabled only for the specified set of compilation modes. This is useful for bazelrc settings. When set to `yes`, Fission is enabled universally. When set to `no`, Fission is disabled universally. Default is `no`.

#### `--force_ignore_dash_static`

If this flag is set, any `-static` options in linkopts of `cc_*` rules BUILD files are ignored. This is only intended as a workaround for C++ hardening builds.

#### `--[no]force_pic`

If enabled, all C++ compilations produce position-independent code ("-fPIC"), links prefer PIC pre-built libraries over non-PIC libraries, and links produce position-independent executables ("-pie"). Default is disabled.
 **Note:** Dynamically linked binaries (for example `--dynamic_mode fully`) generate PIC code regardless of this flag's setting. So this flag is for cases where users want PIC code explicitly generated for static links.
#### `--android_resource_shrinking`

Selects whether to perform resource shrinking for android_binary rules. Sets the default for the shrink_resources attribute on android_binary rules; see the documentation for that rule for further details. Defaults to off.

#### `--custom_malloc=malloc-library-target`

When specified, always use the given malloc implementation, overriding all `malloc="target"` attributes, including in those targets that use the default (by not specifying any `malloc`).

#### `--crosstool_top=label`

This option specifies the location of the crosstool compiler suite to be used for all C++ compilation during a build. Bazel will look in that location for a CROSSTOOL file and uses that to automatically determine settings for `--compiler`.

#### `--host_crosstool_top=label`

If not specified, Bazel uses the value of `--crosstool_top` to compile code in the exec configuration, such as tools run during the build. The main purpose of this flag is to enable cross-compilation.

#### `--apple_crosstool_top=label`

The crosstool to use for compiling C/C++ rules in the transitive `deps` of objc_*, ios__*, and apple_* rules. For those targets, this flag overwrites `--crosstool_top`.

#### `--compiler=version`

This option specifies the C/C++ compiler version (such as `gcc-4.1.0`) to be used for the compilation of binaries during the build. If you want to build with a custom crosstool, you should use a CROSSTOOL file instead of specifying this flag.
 **Note:** Only certain combinations of crosstool version, compiler version, and target CPU are allowed.
#### `--android_sdk=label`

Deprecated. This shouldn't be directly specified.

This option specifies the Android SDK/platform toolchain and Android runtime library that will be used to build any Android-related rule.

The Android SDK will be automatically selected if an `android_sdk_repository` rule is defined in the WORKSPACE file.

#### `--java_toolchain=label`

No-op. Kept only for backwards compatibility.

#### `--host_java_toolchain=label`

No-op. Kept only for backwards compatibility.

#### `--javabase=(label)`

No-op. Kept only for backwards compatibility.

#### `--host_javabase=label`

No-op. Kept only for backwards compatibility.
