---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Avoid unnecessary interfaces

The most common mistake is creating an interface before a real need exists.

-
**Don’t confuse the concept with the keyword:** Just because you are designing a “service” or a “repository” or similar pattern doesn’t mean you need a named interface type (e.g., `type Service interface`). Focus on the behavior and its concrete implementation first.

-
**Reuse existing interfaces:** If an interface already exists, especially in generated code, like a RPC client or server, use it (testing RPC). Do not wrap a generated RPC code in a new, manual interface just for the sake of abstraction or testing. Use real transports instead.

-
**Don’t define back doors only for tests:** Do not export a test double implementation of an interface from an API that consumes it. Instead, prefer to design the API so that it can be tested using the public API of the real implementation.

Every exported type increases the cognitive load for the reader. When you export a test double alongside the real implementation, you force the reader to understand three entities (the interface, the real implementation, and the test double) instead of one.

Export an interface for a test double when you have a material need to support substitution.

When it does make sense to create an interface:

-
**Multiple implementations:** When there are two or more concrete types that must be handled by the same logic (e.g., something that operates with both json.Encoder and gob.GobEncoder), the API consumer could define an interface.

-
**Decoupling packages:** To break circular dependencies between two packages (see an example), an API producer could define an interface.

**Caution:** Carefully observe guidance on Package Size. Introducing interfaces to break dependency cycles is often a signal of improperly structured packages.

-
**Hiding complexity:** When a concrete type has a massive API surface, but a specific function only needs one or two methods, an API consumer may define an interface.
