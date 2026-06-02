---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## String concatenation

There are several ways to concatenate strings in Go. Some examples include:

- The “+” operator
- `fmt.Sprintf`
- `strings.Builder`
- `text/template`
- `safehtml/template`

Though there is no one-size-fits-all rule for which to choose, the following guidance outlines when each method is preferred.
