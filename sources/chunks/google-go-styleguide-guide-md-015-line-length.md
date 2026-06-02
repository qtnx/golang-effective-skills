---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/guide.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Line length

There is no fixed line length for Go source code. If a line feels too long,
prefer refactoring instead of splitting it. If it is already as short as it is
practical for it to be, the line should be allowed to remain long.

Do not split a line:

*   Before an [indentation change](decisions#indentation-confusion) (e.g.,
    function declaration, conditional)
*   To make a long string (e.g., a URL) fit into multiple shorter lines

<a id="naming"></a>
