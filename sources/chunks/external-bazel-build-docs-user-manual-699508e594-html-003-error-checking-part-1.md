---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Options

### Error checking

These options control Bazel's error-checking and/or warnings.

#### `--[no]check_visibility`

If this option is set to false, visibility checks are demoted to warnings. The default value of this option is true, so that by default, visibility checking is done.

#### `--output_filter=regex`

The `--output_filter` option will only show build and compilation warnings for targets that match the regular expression. If a target does not match the given regular expression and its execution succeeds, its standard output and standard error are thrown away.

Here are some typical values for this option:
   `--output_filter='^//(first/project|second/project):'` Show the output for the specified packages.   `--output_filter='^//((?!(first/bad_project|second/bad_project):).)*$'` Don't show output for the specified packages.   `--output_filter=` Show everything.    `--output_filter=DONT_MATCH_ANYTHING` Show nothing.

## Options

### Tool flags

These options control which options Bazel will pass to other tools.

#### `--copt=cc-option`

This option takes an argument which is to be passed to the compiler. The argument will be passed to the compiler whenever it is invoked for preprocessing, compiling, and/or assembling C, C++, or assembler code. It will not be passed when linking.

This option can be used multiple times. For example:

```go

% bazel build --copt="-g0" --copt="-fpic" //foo

```

will compile the `foo` library without debug tables, generating position-independent code.
 **Note:** Changing `--copt` settings will force a recompilation of all affected object files. Also note that copts values listed in specific cc_library or cc_binary build rules will be placed on the compiler command line _after_ these options.**Warning:** C++-specific options (such as `-fno-implicit-templates`) should be specified in `--cxxopt`, not in `--copt`. Likewise, C-specific options (such as -Wstrict-prototypes) should be specified in `--conlyopt`, not in `copt`. Similarly, compiler options that only have an effect at link time (such as `-l`) should be specified in `--linkopt`, not in `--copt`.
#### `--host_copt=cc-option`

This option takes an argument which is to be passed to the compiler for source files that are compiled in the exec configuration. This is analogous to the `--copt` option, but applies only to the exec configuration.

#### `--host_conlyopt=cc-option`

This option takes an argument which is to be passed to the compiler for C source files that are compiled in the exec configuration. This is analogous to the `--conlyopt` option, but applies only to the exec configuration.

#### `--host_cxxopt=cc-option`

This option takes an argument which is to be passed to the compiler for C++ source files that are compiled in the exec configuration. This is analogous to the `--cxxopt` option, but applies only to the exec configuration.

#### `--host_linkopt=linker-option`

This option takes an argument which is to be passed to the linker for source files that are compiled in the exec configuration. This is analogous to the `--linkopt` option, but applies only to the exec configuration.

#### `--conlyopt=cc-option`

This option takes an argument which is to be passed to the compiler when compiling C source files.

This is similar to `--copt`, but only applies to C compilation, not to C++ compilation or linking. So you can pass C-specific options (such as `-Wno-pointer-sign`) using `--conlyopt`.
 **Note:** copts parameters listed in specific cc_library or cc_binary build rules are placed on the compiler command line _after_ these options.
#### `--cxxopt=cc-option`

This option takes an argument which is to be passed to the compiler when compiling C++ source files.

This is similar to `--copt`, but only applies to C++ compilation, not to C compilation or linking. So you can pass C++-specific options (such as `-fpermissive` or `-fno-implicit-templates`) using `--cxxopt`.

For example:

```go

% bazel build --cxxopt="-fpermissive" --cxxopt="-Wno-error" //foo/cruddy_code

```
 **Note:** copts parameters listed in specific cc_library or cc_binary build rules are placed on the compiler command line _after_ these options.
#### `--linkopt=linker-option`

This option takes an argument which is to be passed to the compiler when linking.

This is similar to `--copt`, but only applies to linking, not to compilation. So you can pass compiler options that only make sense at link time (such as `-lssp` or `-Wl,--wrap,abort`) using `--linkopt`. For example:

```go

% bazel build --copt="-fmudflap" --linkopt="-lmudflap" //foo/buggy_code

```

Build rules can also specify link options in their attributes. This option's settings always take precedence. Also see cc_library.linkopts.

#### `--strip (always|never|sometimes)`

This option determines whether Bazel will strip debugging information from all binaries and shared libraries, by invoking the linker with the `-Wl,--strip-debug` option. `--strip=always` means always strip debugging information. `--strip=never` means never strip debugging information. The default value of `--strip=sometimes` means strip if the `--compilation_mode` is `fastbuild`.

```go

% bazel build --strip=always //foo:bar

```

will compile the target while stripping debugging information from all generated binaries.
 **Note:** If you want debugging information, it's not enough to disable stripping; you also need to make sure that the debugging information was generated by the compiler, which you can do by using either `-c dbg` or `--copt -g`.
Bazel's `--strip` option corresponds with ld's `--strip-debug` option: it only strips debugging information. If for some reason you want to strip _all_ symbols, not just _debug_ symbols, you would need to use ld's `--strip-all` option, which you can do by passing `--linkopt=-Wl,--strip-all` to Bazel. Also be aware that setting Bazel's `--strip` flag will override `--linkopt=-Wl,--strip-all`, so you should only set one or the other.

If you are only building a single binary and want all symbols stripped, you could also pass `--stripopt=--strip-all` and explicitly build the `//foo:bar.stripped` version of the target. As described in the section on `--stripopt`, this applies a strip action after the final binary is linked rather than including stripping in all of the build's link actions.

#### `--stripopt=strip-option`

This is an additional option to pass to the `strip` command when generating a `*.stripped` binary. The default is `-S -p`. This option can be used multiple times.
 **Note:** `--stripopt` does not apply to the stripping of the main binary with `[--strip](#flag--strip)=(always|sometimes)`.
#### `--fdo_instrument=profile-output-dir`

The `--fdo_instrument` option enables the generation of FDO (feedback directed optimization) profile output when the built C/C++ binary is executed. For GCC, the argument provided is used as a directory prefix for a per-object file directory tree of .gcda files containing profile information for each .o file.

Once the profile data tree has been generated, the profile tree should be zipped up, and provided to the `--fdo_optimize=profile-zip` Bazel option to enable the FDO-optimized compilation.

For the LLVM compiler the argument is also the directory under which the raw LLVM profile data file(s) is dumped. For example: `--fdo_instrument=/path/to/rawprof/dir/`.

The options `--fdo_instrument` and `--fdo_optimize` cannot be used at the same time.

#### `--fdo_optimize=profile-zip`

The `--fdo_optimize` option enables the use of the per-object file profile information to perform FDO (feedback directed optimization) optimizations when compiling. For GCC, the argument provided is the zip file containing the previously-generated file tree of .gcda files containing profile information for each .o file.

Alternatively, the argument provided can point to an auto profile identified by the extension .afdo.
 **Note:** This option also accepts labels that resolve to source files. You may need to add an `exports_files` directive to the corresponding package to make the file visible to Bazel.
For the LLVM compiler the argument provided should point to the indexed LLVM profile output file prepared by the llvm-profdata tool, and should have a .profdata extension.

The options `--fdo_instrument` and `--fdo_optimize` cannot be used at the same time.

#### `--java_language_version=version`

This option specifies the version of Java sources. For example:

```go

% bazel build --java_language_version=8 java/com/example/common/foo:all

```

compiles and allows only constructs compatible with Java 8 specification. Default value is 11. --> Possible values are: 8, 9, 10, 11, 17, and 21 and may be extended by registering custom Java toolchains using `default_java_toolchain`.

#### `--tool_java_language_version=version`

The Java language version used to build tools that are executed during a build. Default value is 11.

#### `--java_runtime_version=version`

This option specifies the version of JVM to use to execute the code and run the tests. For example:

```go

% bazel run --java_runtime_version=remotejdk_11 java/com/example/common/foo:java_application

```

downloads JDK 11 from a remote repository and run the Java application using it.

Default value is `local_jdk`. Possible values are: `local_jdk`, `local_jdk_version`, `remotejdk_11`, `remotejdk_17`, and `remotejdk_21`. You can extend the values by registering custom JVM using either `local_java_repository` or `remote_java_repository` repository rules.

#### `--tool_java_runtime_version=version`

The version of JVM used to execute tools that are needed during a build. Default value is `remotejdk_11`.

#### `--jvmopt=jvm-option`

This option allows option arguments to be passed to the Java VM. It can be used with one big argument, or multiple times with individual arguments. For example:

```go

% bazel build --jvmopt="-server -Xms256m" java/com/example/common/foo:all

```

will use the server VM for launching all Java binaries and set the startup heap size for the VM to 256 MB.

#### `--javacopt=javac-option`

This option allows option arguments to be passed to javac. It can be used with one big argument, or multiple times with individual arguments. For example:

```go

% bazel build --javacopt="-g:source,lines" //myprojects:prog

```

will rebuild a java_binary with the javac default debug info (instead of the bazel default).

The option is passed to javac after the Bazel built-in default options for javac and before the per-rule options. The last specification of any option to javac wins. The default options for javac are:

```go

-source 8 -target 8 -encoding UTF-8

```
 **Note:** Changing `--javacopt` settings will force a recompilation of all affected classes. Also note that javacopts parameters listed in specific java_library or java_binary build rules will be placed on the javac command line _after_ these options.
#### `--strict_java_deps (default|strict|off|warn|error)`

This option controls whether javac checks for missing direct dependencies. Java targets must explicitly declare all directly used targets as dependencies. This flag instructs javac to determine the jars actually used for type checking each java file, and warn/error if they are not the output of a direct dependency of the current target.
