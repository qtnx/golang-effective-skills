---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Comment line length

There is no fixed [line length] for comments in Go.

[line length]: guide#line-length

Long comment lines should be wrapped to ensure that source is readable in tools
which do not perform automatic wrapping of comment lines. If you are uncertain
where to wrap, 80 or 100 columns are common choices. However, this is not a hard
cut-off; there are situations where breaking a long literal text is harmful.
There is no requirement for the specific column width at which wrapping occurs.
Aim to be [consistent](guide#consistency) within a file.

See this [post from The Go Blog on documentation] for more on commentary.

[post from The Go Blog on documentation]: https://blog.golang.org/godoc-documenting-go-code

```text
