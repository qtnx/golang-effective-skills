---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

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
