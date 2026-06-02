---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

# Commands and Options   Stay organized with collections   Save and categorize content based on your preferences.

## Running tests

To build and run tests with bazel, type `bazel test` followed by the name of the test targets.

By default, this command performs simultaneous build and test activity, building all specified targets (including any non-test targets specified on the command line) and testing `*_test` and `test_suite` targets as soon as their prerequisites are built, meaning that test execution is interleaved with building. Doing so usually results in significant speed gains.

### Options for `bazel test`

#### `--cache_test_results=(yes|no|auto)` (`-t`)

If this option is set to 'auto' (the default) then Bazel will only rerun a test if any of the following conditions applies:

- Bazel detects changes in the test or its dependencies
- the test is marked as `external`
- multiple test runs were requested with `--runs_per_test`
- the test failed.

If 'no', all tests will be executed unconditionally.

If 'yes', the caching behavior will be the same as auto except that it may cache test failures and test runs with `--runs_per_test`.
 **Note:** Test results are _always_ saved in Bazel's output tree, regardless of whether this option is enabled, so you needn't have used `--cache_test_results` on the prior run(s) of `bazel test` in order to get cache hits. The option only affects whether Bazel will _use_ previously saved results, not whether it will save results of the current run.
Users who have enabled this option by default in their `.bazelrc` file may find the abbreviations `-t` (on) or `-t-` (off) convenient for overriding the default on a particular run.

#### `--check_tests_up_to_date`

This option tells Bazel not to run the tests, but to merely check and report the cached test results. If there are any tests which have not been previously built and run, or whose tests results are out-of-date (for example, because the source code or the build options have changed), then Bazel will report an error message ("test result is not up-to-date"), will record the test's status as "NO STATUS" (in red, if color output is enabled), and will return a non-zero exit code.

This option also implies `--check_up_to_date` behavior.

This option may be useful for pre-submit checks.

#### `--test_verbose_timeout_warnings`

This option tells Bazel to explicitly warn the user if a test's timeout is significantly longer than the test's actual execution time. While a test's timeout should be set such that it is not flaky, a test that has a highly over-generous timeout can hide real problems that crop up unexpectedly.

For instance, a test that normally executes in a minute or two should not have a timeout of ETERNAL or LONG as these are much, much too generous.

This option is useful to help users decide on a good timeout value or sanity check existing timeout values.
 **Note:** Each test shard is allotted the timeout of the entire `XX_test` target. Using this option does not affect a test's timeout value, merely warns if Bazel thinks the timeout could be restricted further.
#### `--[no]test_keep_going`

By default, all tests are run to completion. If this flag is disabled, however, the build is aborted on any non-passing test. Subsequent build steps and test invocations are not run, and in-flight invocations are canceled. Do not specify both `--notest_keep_going` and `--keep_going`.

#### `--flaky_test_attempts=attempts`

This option specifies the maximum number of times a test should be attempted if it fails for any reason. A test that initially fails but eventually succeeds is reported as `FLAKY` on the test summary. It is, however, considered to be passed when it comes to identifying Bazel exit code or total number of passed tests. Tests that fail all allowed attempts are considered to be failed.

By default (when this option is not specified, or when it is set to default), only a single attempt is allowed for regular tests, and 3 for test rules with the `flaky` attribute set. You can specify an integer value to override the maximum limit of test attempts. Bazel allows a maximum of 10 test attempts in order to prevent abuse of the system.

#### `--runs_per_test=[regex@]number`

This option specifies the number of times each test should be executed. All test executions are treated as separate tests (fallback functionality will apply to each of them independently).

The status of a target with failing runs depends on the value of the `--runs_per_test_detects_flakes` flag:

- If absent, any failing run causes the entire test to fail.
- If present and two runs from the same shard return PASS and FAIL, the test will receive a status of flaky (unless other failing runs cause it to fail).

If a single number is specified, all tests will run that many times. Alternatively, a regular expression may be specified using the syntax regex@number. This constrains the effect of `--runs_per_test` to targets which match the regex (`--runs_per_test=^//pizza:.*@4` runs all tests under `//pizza/` 4 times). This form of `--runs_per_test` may be specified more than once.

#### `--[no]runs_per_test_detects_flakes`

If this option is specified (by default it is not), Bazel will detect flaky test shards through `--runs_per_test`. If one or more runs for a single shard fail and one or more runs for the same shard pass, the target will be considered flaky with the flag. If unspecified, the target will report a failing status.

#### `--test_summary=output_style`

Specifies how the test result summary should be displayed.

- `short` prints the results of each test along with the name of the file containing the test output if the test failed. This is the default value.
- `terse` like `short`, but even shorter: only print information about tests which did not pass.
- `detailed` prints each individual test case that failed, not only each test. The names of test output files are omitted.
- `none` does not print test summary.

#### `--test_output=output_style`

Specifies how test output should be displayed:

- `summary` shows a summary of whether each test passed or failed. Also shows the output log file name for failed tests. The summary will be printed at the end of the build (during the build, one would see just simple progress messages when tests start, pass or fail). This is the default behavior.
- `errors` sends combined stdout/stderr output from failed tests only into the stdout immediately after test is completed, ensuring that test output from simultaneous tests is not interleaved with each other. Prints a summary at the build as per summary output above.
- `all` is similar to `errors` but prints output for all tests, including those which passed.
- `streamed` streams stdout/stderr output from each test in real-time.

#### `--java_debug`

This option causes the Java virtual machine of a java test to wait for a connection from a JDWP-compliant debugger before starting the test. This option implies `--test_output=streamed`.

#### `--[no]verbose_test_summary`

By default this option is enabled, causing test times and other additional information (such as test attempts) to be printed to the test summary. If `--noverbose_test_summary` is specified, test summary will include only test name, test status and cached test indicator and will be formatted to stay within 80 characters when possible.

#### `--test_tmpdir=path`

Specifies temporary directory for tests executed locally. Each test will be executed in a separate subdirectory inside this directory. The directory will be cleaned at the beginning of the each `bazel test` command. By default, bazel will place this directory under Bazel output base directory.
 **Note:** This is a directory for running tests, not storing test results (those are always stored under the `bazel-out` directory).
#### `--test_timeout=seconds` OR `--test_timeout=seconds,seconds,seconds,seconds`

Overrides the timeout value for all tests by using specified number of seconds as a new timeout value. If only one value is provided, then it will be used for all test timeout categories.

Alternatively, four comma-separated values may be provided, specifying individual timeouts for short, moderate, long and eternal tests (in that order). In either form, zero or a negative value for any of the test sizes will be substituted by the default timeout for the given timeout categories as defined by the page Writing Tests. By default, Bazel will use these timeouts for all tests by inferring the timeout limit from the test's size whether the size is implicitly or explicitly set.

Tests which explicitly state their timeout category as distinct from their size will receive the same value as if that timeout had been implicitly set by the size tag. So a test of size 'small' which declares a 'long' timeout will have the same effective timeout that a 'large' tests has with no explicit timeout.

#### `--test_arg=arg`

Passes command-line options/flags/arguments to each test process. This option can be used multiple times to pass several arguments. For example, `--test_arg=--logtostderr --test_arg=--v=3`.

Note that, unlike the `bazel run` command, you can't pass test arguments directly as in `bazel test -- target --logtostderr --v=3`. That's because extraneous arguments passed to `bazel test` are interpreted as additional test targets. That is, `--logtostderr` and `--v=3` would each be interpreted as a test target. This ambiguity doesn't exist for a `bazel run` command, which only accepts one target.

`--test_arg` can be passed to a `bazel run` command, but it's ignored unless the target being run is a test target. (As with any other flag, if it's passed in a `bazel run` command after a `--` token, it's not processed by Bazel but forwarded verbatim to the executed target.)

#### `--test_env=variable=_value_` OR `--test_env=variable`

Specifies additional variables that must be injected into the test environment for each test. If value is not specified it will be inherited from the shell environment used to start the `bazel test` command.
