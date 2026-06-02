---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Identify the function

In most tests, failure messages should include the name of the function that failed, even though it seems obvious from the name of the test function. Specifically, your failure message should be `YourFunc(%v) = %v, want %v` instead of just `got %v, want %v`.
