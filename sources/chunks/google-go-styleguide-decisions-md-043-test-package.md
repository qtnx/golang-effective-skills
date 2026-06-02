---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Test structure

### Test package

<a id="TOC-TestPackage"></a>

<a id="test-same-package"></a>

#### Tests in the same package

Tests may be defined in the same package as the code being tested.

To write a test in the same package:

*   Place the tests in a `foo_test.go` file
*   Use `package foo` for the test file
*   Do not explicitly import the package to be tested

```build
# Good:
go_library(
    name = "foo",
    srcs = ["foo.go"],
    deps = [
        ...
    ],
)

go_test(
    name = "foo_test",
    size = "small",
    srcs = ["foo_test.go"],
    library = ":foo",
    deps = [
        ...
    ],
)
```

A test in the same package can access unexported identifiers in the package.
This may enable better test coverage and more concise tests. Be aware that any
[examples] declared in the test will not have the package names that a user will
need in their code.

[`library`]: https://github.com/bazelbuild/rules_go/blob/master/docs/go/core/rules.md#go_library
[examples]: #examples

<a id="test-different-package"></a>

#### Tests in a different package

It is not always appropriate or even possible to define a test in the same
package as the code being tested. In these cases, use a package name with the
`_test` suffix. This is an exception to the "no underscores" rule to
[package names](#package-names). For example:

*   If an integration test does not have an obvious library that it belongs to

    ```go
    // Good:
    package gmailintegration_test

    import "testing"
    ```

*   If defining the tests in the same package results in circular dependencies

    ```go
    // Good:
    package fireworks_test

    import (
      "fireworks"
      "fireworkstestutil" // fireworkstestutil also imports fireworks
    )
    ```

<a id="use-package-testing"></a>
