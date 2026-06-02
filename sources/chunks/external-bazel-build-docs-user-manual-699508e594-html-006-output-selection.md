---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Options

### Output selection

These options determine what to build or test.

#### `--[no]build`

This option causes the execution phase of the build to occur; it is on by default. When it is switched off, the execution phase is skipped, and only the first two phases, loading and analysis, occur.

This option can be useful for validating BUILD files and detecting errors in the inputs, without actually building anything.

#### `--[no]build_tests_only`

If specified, Bazel will build only what is necessary to run the `*_test` and `test_suite` rules that were not filtered due to their size, timeout, tag, or language. If specified, Bazel will ignore other targets specified on the command line. By default, this option is disabled and Bazel will build everything requested, including `*_test` and `test_suite` rules that are filtered out from testing. This is useful because running `bazel test --build_tests_only foo/...` may not detect all build breakages in the `foo` tree.

#### `--[no]check_up_to_date`

This option causes Bazel not to perform a build, but merely check whether all specified targets are up-to-date. If so, the build completes successfully, as usual. However, if any files are out of date, instead of being built, an error is reported and the build fails. This option may be useful to determine whether a build has been performed more recently than a source edit (for example, for pre-submit checks) without incurring the cost of a build.

See also `--check_tests_up_to_date`.

#### `--[no]compile_one_dependency`

Compile a single dependency of the argument files. This is useful for syntax checking source files in IDEs, for example, by rebuilding a single target that depends on the source file to detect errors as early as possible in the edit/build/test cycle. This argument affects the way all non-flag arguments are interpreted: each argument must be a file target label or a plain filename relative to the current working directory, and one rule that depends on each source filename is built. For C++ and Java sources, rules in the same language space are preferentially chosen. For multiple rules with the same preference, the one that appears first in the BUILD file is chosen. An explicitly named target pattern which does not reference a source file results in an error.

#### `--save_temps`

The `--save_temps` option causes temporary outputs from the compiler to be saved. These include .s files (assembler code), .i (preprocessed C) and .ii (preprocessed C++) files. These outputs are often useful for debugging. Temps will only be generated for the set of targets specified on the command line.
 **Note:** The implementation of `--save_temps` does not use the compiler's `-save-temps` flag. Instead, there are two passes, one with `-S` and one with `-E`. A consequence of this is that if your build fails, Bazel may not yet have produced the ".i" or ".ii" and ".s" files. If you're trying to use `--save_temps` to debug a failed compilation, you may need to also use `--keep_going` so that Bazel will still try to produce the preprocessed files after the compilation fails.
The `--save_temps` flag currently works only for cc_* rules.

To ensure that Bazel prints the location of the additional output files, check that your `--show_result n` setting is high enough.

#### `--build_tag_filters=tag[,tag]*`

If specified, Bazel will build only targets that have at least one required tag (if any of them are specified) and does not have any excluded tags. Build tag filter is specified as comma delimited list of tag keywords, optionally preceded with '-' sign used to denote excluded tags. Required tags may also have a preceding '+' sign.

When running tests, Bazel ignores `--build_tag_filters` for test targets, which are built and run even if they do not match this filter. To avoid building them, filter test targets using `--test_tag_filters` or by explicitly excluding them.

#### `--test_size_filters=size[,size]*`

If specified, Bazel will test (or build if `--build_tests_only` is also specified) only test targets with the given size. Test size filter is specified as comma delimited list of allowed test size values (small, medium, large or enormous), optionally preceded with '-' sign used to denote excluded test sizes. For example,

```go

  % bazel test --test_size_filters=small,medium //foo:all

```

and

```go

  % bazel test --test_size_filters=-large,-enormous //foo:all

```

will test only small and medium tests inside //foo.

By default, test size filtering is not applied.

#### `--test_timeout_filters=timeout[,timeout]*`

If specified, Bazel will test (or build if `--build_tests_only` is also specified) only test targets with the given timeout. Test timeout filter is specified as comma delimited list of allowed test timeout values (short, moderate, long or eternal), optionally preceded with '-' sign used to denote excluded test timeouts. See --test_size_filters for example syntax.

By default, test timeout filtering is not applied.

#### `--test_tag_filters=tag[,tag]*`

If specified, Bazel will test (or build if `--build_tests_only` is also specified) only test targets that have at least one required tag (if any of them are specified) and does not have any excluded tags. Test tag filter is specified as comma delimited list of tag keywords, optionally preceded with '-' sign used to denote excluded tags. Required tags may also have a preceding '+' sign.

For example,

```go

  % bazel test --test_tag_filters=performance,stress,-flaky //myproject:all

```

will test targets that are tagged with either `performance` or `stress` tag but are **not** tagged with the `flaky` tag.

By default, test tag filtering is not applied. Note that you can also filter on test's `size` and `local` tags in this manner.

#### `--test_lang_filters=string[,string]*`

Specifies a comma-separated list of strings referring to names of test rule classes. To refer to the rule class `foo_test`, use the string "foo". Bazel will test (or build if `--build_tests_only` is also specified) only targets of the referenced rule classes. To instead exclude those targets, use the string "-foo". For example,

```go

  % bazel test --test_lang_filters=foo,bar //baz/...

```

 will test only targets that are instances of `foo_test` or `bar_test` in `//baz/...`, while

```go

  % bazel test --test_lang_filters=-foo,-bar //baz/...

```

 will test all the targets in `//baz/...` except for the `foo_test` and `bar_test` instances.

 **Tip:** You can use `bazel query --output=label_kind "//p:t"` to learn the rule class name of the target `//p:t`. And you can look at the pair of instantiation stacks in the output of `bazel query --output=build "//p:t"` to learn why that target is an instance of that rule class.**Warning:** The option name "--test_lang_filter" is vestigal and is therefore unfortunately misleading; don't make assumptions about the semantics based on the name.
#### `--test_filter=filter-expression`

Specifies a filter that the test runner may use to pick a subset of tests for running. All targets specified in the invocation are built, but depending on the expression only some of them may be executed; in some cases, only certain test methods are run.

The particular interpretation of filter-expression is up to the test framework responsible for running the test. It may be a glob, substring, or regexp. `--test_filter` is a convenience over passing different `--test_arg` filter arguments, but not all frameworks support it.
