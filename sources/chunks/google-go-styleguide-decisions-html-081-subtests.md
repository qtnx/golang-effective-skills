---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Subtests

The standard Go testing library offers a facility to define subtests. This allows flexibility in setup and cleanup, controlling parallelism, and test filtering. Subtests can be useful (particularly for table-driven tests), but using them is not mandatory. See also the Go blog post about subtests.

Subtests should not depend on the execution of other cases for success or initial state, because subtests are expected to be able to be run individually with using `go test -run` flags or with Bazel test filter expressions.
