---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Simple case

You want to add a set of test doubles for `Service`. Because `Card` is effectively a dumb data type, similar to a Protocol Buffer message, it needs no special treatment in tests, so no double is required. If you anticipate only test doubles for one type (like `Service`), you can take a concise approach to naming the doubles:

```go
// Good:
import (
    "path/to/creditcard"
    "path/to/money"
)

// Stub stubs creditcard.Service and provides no behavior of its own.
type Stub struct{}

func (Stub) Charge(*creditcard.Card, money.Money) error { return nil }

```

This is strictly preferable to a naming choice like `StubService` or the very poor `StubCreditCardService`, because the base package name and its domain types imply what `creditcardtest.Stub` is.

Finally, if the package is built with Bazel, make sure the new `go_library` rule for the package is marked as `testonly`:

```go
