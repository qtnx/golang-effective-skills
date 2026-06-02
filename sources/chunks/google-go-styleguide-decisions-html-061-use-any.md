---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Use any

Go 1.18 introduces an `any` type as an alias to `interface{}`. Because it is an alias, `any` is equivalent to `interface{}` in many situations and in others it is easily interchangeable via an explicit conversion. Prefer to use `any` in new code.
