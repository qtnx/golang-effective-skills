---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/guide.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### MixedCaps

Go source code uses `MixedCaps` or `mixedCaps` (camel case) rather than underscores (snake case) when writing multi-word names.

This applies even when it breaks conventions in other languages. For example, a constant is `MaxLength` (not `MAX_LENGTH`) if exported and `maxLength` (not `max_length`) if unexported.

Local variables are considered unexported for the purpose of choosing the initial capitalization.
