---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Single-letter variable names

Single-letter variable names can be a useful tool to minimize repetition, but can also make code needlessly opaque. Limit their use to instances where the full word is obvious and where it would be repetitive for it to appear in place of the single-letter variable.

In general:

- For a method receiver variable, a one-letter or two-letter name is preferred.
- Using familiar variable names for common types is often helpful:
- `r` for an `io.Reader` or `*http.Request`
- `w` for an `io.Writer` or `http.ResponseWriter`

- Single-letter identifiers are acceptable as integer loop variables, particularly for indices (e.g., `i`) and coordinates (e.g., `x` and `y`).
- Abbreviations can be acceptable loop identifiers when the scope is short, for example `for _, n := range nodes { ... }`.
