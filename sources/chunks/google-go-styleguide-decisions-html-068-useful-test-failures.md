---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Useful test failures

It should be possible to diagnose a test’s failure without reading the test’s source. Tests should fail with helpful messages detailing:

- What caused the failure
- What inputs resulted in an error
- The actual result
- What was expected

Specific conventions for achieving this goal are outlined below.
