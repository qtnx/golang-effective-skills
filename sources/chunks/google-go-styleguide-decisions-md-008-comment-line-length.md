---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Commentary
The conventions around commentary (which include what to comment, what style to
use, how to provide runnable examples, etc.) are intended to support the
experience of reading the documentation of a public API. See
[Effective Go](http://golang.org/doc/effective_go.html#commentary) for more
information.
The best practices document's section on [documentation conventions] discusses
this further.
**Best Practice:** Use [doc preview] during development and code review to see
whether the documentation and runnable examples are useful and are presented the
way you expect them to be.
**Tip:** Godoc uses very little special formatting; lists and code snippets
should usually be indented to avoid linewrapping. Apart from indentation,
decoration should generally be avoided.
[doc preview]: best-practices#documentation-preview
[documentation conventions]:  best-practices#documentation-conventions
<a id="comment-line-length"></a>
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
# Good:
// This is a comment paragraph.
// The length of individual lines doesn't matter in Godoc;
// but the choice of wrapping makes it easy to read on narrow screens.
//
// Don't worry too much about the long URL:
// https://supercalifragilisticexpialidocious.example.com:8080/Animalia/Chordata/Mammalia/Rodentia/Geomyoidea/Geomyidae/
//
// Similarly, if you have other information that is made awkward
// by too many line breaks, use your judgment and include a long line
// if it helps rather than hinders.
```

Avoid comments that fit large amounts of text onto a single line, which is a
poor reader experience.

```text
# Bad:
// This is a comment paragraph. While some code editors and viewers will wrap the paragraph for the reader, others will display a very long line that will overflow most windows and require users to scroll horizontally. In addition, even on a screen capable of displaying the entire line, it is easier to read a narrower paragraph than very wide one.
//
// Don't worry too much about the long URL:
// https://supercalifragilisticexpialidocious.example.com:8080/Animalia/Chordata/Mammalia/Rodentia/Geomyoidea/Geomyidae/
```

<a id="doc-comments"></a>
