---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Examples

Packages should clearly document their intended usage. Try to provide a runnable example; examples show up in Godoc. Runnable examples belong in the test file, not the production source file. See this example (Godoc, source).

If it isn’t feasible to provide a runnable example, example code can be provided within code comments. As with other code and command-line snippets in comments, it should follow standard formatting conventions.
