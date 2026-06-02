---
source_name: "External Linked Documentation"
source_url: "https://docs.bazel.build/versions/main/be/general.html"
source_path: "sources/raw/external/docs-bazel-build-versions-main-be-general-html-1d20475b8b.html"
license_ref: ""
---

# General Rules

##  test_suite

```go
test_suite(name, compatible_with, deprecation, distribs, features, licenses, restricted_to, tags, target_compatible_with, testonly, tests, visibility)
```

 A `test_suite` defines a set of tests that are considered "useful" to humans. This allows projects to define sets of tests, such as "tests you must run before checkin", "our project's stress tests" or "all small tests." The `bazel test` command respects this sort of organization: For an invocation like `bazel test //some/test:suite`, Bazel first enumerates all test targets transitively included by the `//some/test:suite` target (we call this "test_suite expansion"), then Bazel builds and tests those targets.

#### Examples

A test suite to run all of the small tests in the current package.

```go

test_suite(
    name = "small_tests",
    tags = ["small"],
)

```

A test suite that runs a specified set of tests:

```go

test_suite(
    name = "smoke_tests",
    tests = [
        "system_unittest",
        "public_api_unittest",
    ],
)

```

A test suite to run all tests in the current package which are not flaky.

```go

test_suite(
    name = "non_flaky_test",
    tags = ["-flaky"],
)

```

### Arguments
        Attributes     `name`
`Name; required`

A unique name for this target.
     `tags`
`List of strings; optional; nonconfigurable`
 List of text tags such as "small" or "database" or "-flaky". Tags may be any valid string.
 Tags which begin with a "-" character are considered negative tags. The preceding "-" character is not considered part of the tag, so a suite tag of "-small" matches a test's "small" size. All other tags are considered positive tags.

 Optionally, to make positive tags more explicit, tags may also begin with the "+" character, which will not be evaluated as part of the text of the tag. It merely makes the positive and negative distinction easier to read.

 Only test rules that match **all** of the positive tags and **none** of the negative tags will be included in the test suite. Note that this does not mean that error checking for dependencies on tests that are filtered out is skipped; the dependencies on skipped tests still need to be legal (e.g. not blocked by visibility constraints).

 The `manual` tag keyword is treated differently than the above by the "test_suite expansion" performed by the `bazel test` command on invocations involving wildcard target patterns <https://docs.bazel.build/versions/main/guide.html#specifying-targets-to-build>. There, `test_suite` targets tagged "manual" are filtered out (and thus not expanded). This behavior is consistent with how `bazel build` and `bazel test` handle wildcard target patterns in general. Note that this is explicitly different from how `bazel query 'tests(E)'` behaves, as suites are always expanded by the `tests` query function, regardless of the `manual` tag.

 Note that a test's `size` is considered a tag for the purpose of filtering.

 If you need a `test_suite` that contains tests with mutually exclusive tags (e.g. all small and medium tests), you'll have to create three `test_suite` rules: one for all small tests, one for all medium tests, and one that includes the previous two.
     `tests`
`List of labels; optional; nonconfigurable`
 A list of test suites and test targets of any language.
 Any `*_test` is accepted here, independent of the language. No `*_binary` targets are accepted however, even if they happen to run a test. Filtering by the specified `tags` is only done for tests listed directly in this attribute. If this attribute contains `test_suite`s, the tests inside those will not be filtered by this `test_suite` (they are considered to be filtered already).

 If the `tests` attribute is unspecified or empty, the rule will default to including all test rules in the current BUILD file that are not tagged as `manual`. These rules are still subject to `tag` filtering.
