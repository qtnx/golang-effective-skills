---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Repetition

<!--
Note to future editors:

Do not use the term "stutter" to refer to cases when a name is repetitive.
-->

A piece of Go source code should avoid unnecessary repetition. One common source
of this is repetitive names, which often include unnecessary words or repeat
their context or type. Code itself can also be unnecessarily repetitive if the
same or a similar code segment appears multiple times in close proximity.

Repetitive naming can come in many forms, including:

<a id="repetitive-with-package"></a>
