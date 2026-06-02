---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Interfaces

Interfaces in Go are powerful but can be overused or misunderstood. Because Go
interfaces are satisfied implicitly, they are a structural tool rather than a
declarative one. The following guidance provides the best practices for how to
design and return interfaces in Go without over-engineering your codebase.

Refer to [Decisions' section on interfaces](decisions#interfaces) for a summary.

<a id="avoid-unnecessary-interfaces"></a>
