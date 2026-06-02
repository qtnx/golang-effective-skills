---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/guide.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Least mechanism

Where there are several ways to express the same idea, prefer the one that uses
the most standard tools. Sophisticated machinery often exists, but should not be
employed without reason. It is easy to add complexity to code as needed, whereas
it is much harder to remove existing complexity after it has been found to be
unnecessary.

1.  Aim to use a core language construct (for example a channel, slice, map,
    loop, or struct) when sufficient for your use case.
2.  If there isn't one, look for a tool within the standard library (like an
    HTTP client or a template engine).
3.  Finally, consider whether there is a core library in the Google codebase
    that is sufficient before introducing a new dependency or creating your own.

As an example, consider production code that contains a flag bound to a variable
with a default value which must be overridden in tests. Unless intending to test
the program's command-line interface itself (say, with `os/exec`), it is simpler
and therefore preferable to override the bound value directly rather than by
using `flag.Set`.

Similarly, if a piece of code requires a set membership check, a boolean-valued
map (e.g., `map[string]bool`) often suffices. Libraries that provide set-like
types and functionality should only be used if more complicated operations are
required that are impossible or overly complicated with a map.

<a id="concision"></a>
