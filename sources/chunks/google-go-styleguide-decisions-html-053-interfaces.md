---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Interfaces

Avoid creating interfaces until a real need exists. Focus on the required behavior rather than just abstract named patterns like “service” or “repository” and the like.

-
Do not wrap RPC clients in new manual interfaces just for the sake of abstraction or testing. Use real transports instead (testing RPC).

-
Do not define back doors or export test double implementations of an interface solely for testing. Prefer testing via the public API of the real implementation instead.

Design interfaces to be small for easier implementation and composition (GoTip #78: Minimal Viable Interfaces). Document interfaces appropriately including their contract, edge cases, and expected errors. Keep interface types unexported if they are only used internally within a package.

The consumer of the interface should define it (not the package implementing the interface), ensuring it includes only the methods they actually use. The producer package may export the interface if the interface is the product (a common protocol) to prevent interface redefinition bloat.

There is an adage: Functions should take interfaces as arguments but return concrete types (GoTip #49: Accept Interfaces, Return Concrete Types). Returning concrete types allows the caller to have access to every public method and field of that specific implementation, not just the subset of methods defined in a pre-chosen interface. The caller can still pass that concrete result into any other function that expects an interface. Sometimes returning an interface is acceptable for encapsulation (e.g., `error` interface), and certain constructs like command, chaining, factory, and strategy patterns.

Deeper discussion on interfaces exists in the Best Practices’ section on interfaces.
