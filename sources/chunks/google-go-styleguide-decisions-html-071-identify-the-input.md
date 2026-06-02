---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Identify the input

In most tests, failure messages should include the function inputs if they are short. If the relevant properties of the inputs are not obvious (for example, because the inputs are large or opaque), you should name your test cases with a description of what’s being tested and print the description as part of your error message.
