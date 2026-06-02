---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Creating test helper packages

Suppose you want to create a package that contains test doubles for another. We’ll use `package creditcard` (from above) for this example:

One approach is to introduce a new Go package based on the production one for testing. A safe choice is to append the word `test` to the original package name (“creditcard” + “test”):

```go
// Good:
package creditcardtest

```

Unless stated explicitly otherwise, all examples in the sections below are in `package creditcardtest`.
