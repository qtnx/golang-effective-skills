---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Type aliases

Use a _type definition_, `type T1 T2`, to define a new type. Use a _type alias_, `type T1 = T2`, to refer to an existing type without defining a new type. Type aliases are rare; their primary use is to aid migrating packages to new source code locations. Don’t use type aliasing when it is not needed.
