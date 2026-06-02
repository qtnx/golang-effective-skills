---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/guide.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### What is the code actually doing?

Go is designed such that it should be relatively straightforward to see what the
code is doing. In cases of uncertainty or where a reader may require prior
knowledge in order to understand the code, it is worth investing time in order
to make the code's purpose clearer for future readers. For example, it may help
to:

*   Use more descriptive variable names
*   Add additional commentary
*   Break up the code with whitespace and comments
*   Refactor the code into separate functions/methods to make it more modular

There is no one-size-fits-all approach here, but it is important to prioritize
clarity when developing Go code.

<a id="clarity-rationale"></a>
