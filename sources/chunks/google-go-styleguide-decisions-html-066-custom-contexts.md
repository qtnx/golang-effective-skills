---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Custom contexts

Do not create custom context types or use interfaces other than `context.Context` in function signatures. There are no exceptions to this rule.

Imagine if every team had a custom context. Every function call from package `p` to package `q` would have to determine how to convert a `p.Context` to a `q.Context`, for all pairs of packages `p` and `q`. This is impractical and error-prone for humans, and it makes automated refactorings that add context parameters nearly impossible.

If you have application data to pass around, put it in a parameter, in the receiver, in globals, or in a `Context` value if it truly belongs there. Creating your own context type is not acceptable since it undermines the ability of the Go team to make Go programs work properly in production.
