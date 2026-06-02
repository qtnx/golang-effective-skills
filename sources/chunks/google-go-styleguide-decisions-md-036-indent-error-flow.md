---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Indent error flow

<a id="TOC-IndentErrorFlow"></a>

Handle errors before proceeding with the rest of your code. This improves the
readability of the code by enabling the reader to find the normal path quickly.
This same logic applies to any block which tests a condition then ends in a
terminal condition (e.g., `return`, `panic`, `log.Fatal`).

Code that runs if the terminal condition is not met should appear after the `if`
block, and should not be indented in an `else` clause.

```go
// Good:
if err != nil {
    // error handling
    return // or continue, etc.
}
// normal code
```

```go
// Bad:
if err != nil {
    // error handling
} else {
    // normal code that looks abnormal due to indentation
}
```

> **Tip:** If you are using a variable for more than a few lines of code, it is
> generally not worth using the `if`-with-initializer style. In these cases, it
> is usually better to move the declaration out and use a standard `if`
> statement:
>
> ```go
> // Good:
> x, err := f()
> if err != nil {
>   // error handling
>   return
> }
> // lots of code that uses x
> // across multiple lines
> ```
>
> ```go
> // Bad:
> if x, err := f(); err != nil {
>   // error handling
>   return
> } else {
>   // lots of code that uses x
>   // across multiple lines
> }
> ```

See [Go Tip #1: Line of Sight] and
[TotT: Reduce Code Complexity by Reducing Nesting](https://testing.googleblog.com/2017/06/code-health-reduce-nesting-reduce.html)
for more details.

[Go Tip #1: Line of Sight]: https://google.github.io/styleguide/go/index.html#gotip

<a id="language"></a>
