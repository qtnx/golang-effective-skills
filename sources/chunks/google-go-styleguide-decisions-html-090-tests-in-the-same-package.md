---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Tests in the same package

Tests may be defined in the same package as the code being tested.

To write a test in the same package:

- Place the tests in a `foo_test.go` file
- Use `package foo` for the test file
- Do not explicitly import the package to be tested

```go
