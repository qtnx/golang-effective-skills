---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/guide.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

# Go Style Guide

### Concision

Concise Go code has a high signal-to-noise ratio. It is easy to discern the
relevant details, and the naming and structure guide the reader through these
details.

There are many things that can get in the way of surfacing the most salient
details at any given time:

*   Repetitive code
*   Extraneous syntax
*   [Opaque names](#naming)
*   Unnecessary abstraction
*   Whitespace

Repetitive code especially obscures the differences between each
nearly-identical section, and requires a reader to visually compare similar
lines of code to find the changes. [Table-driven testing] is a good example of a
mechanism that can concisely factor out the common code from the important
details of each repetition, but the choice of which pieces to include in the
table will have an impact on how easy the table is to understand.

When considering multiple ways to structure code, it is worth considering which
way makes important details the most apparent.

Understanding and using common code constructions and idioms are also important
for maintaining a high signal-to-noise ratio. For example, the following code
block is very common in [error handling], and the reader can quickly understand
the purpose of this block.

```go
// Good:
if err := doSomething(); err != nil {
    // ...
}
```

If code looks very similar to this but is subtly different, a reader may not
notice the change. In cases like this, it is worth intentionally ["boosting"]
the signal of the error check by adding a comment to call attention to it.

```go
// Good:
if err := doSomething(); err == nil { // if NO error
    // ...
}
```

[Table-driven testing]: https://go.dev/wiki/TableDrivenTests
[error handling]: https://go.dev/blog/errors-are-values
["boosting"]: best-practices#signal-boost

<a id="maintainability"></a>
