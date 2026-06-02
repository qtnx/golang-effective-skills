---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Language

### Indentation confusion

Avoid introducing a line break if it would align the rest of the line with an
indented code block. If this is unavoidable, leave a space to separate the code
in the block from the wrapped line.

```go
// Bad:
if longCondition1 && longCondition2 &&
    // Conditions 3 and 4 have the same indentation as the code within the if.
    longCondition3 && longCondition4 {
    log.Info("all conditions met")
}
```

See the following sections for specific guidelines and examples:

*   [Function formatting](#func-formatting)
*   [Conditionals and loops](#conditional-formatting)
*   [Literal formatting](#literal-formatting)

<a id="func-formatting"></a>

## Language

### Function formatting

The signature of a function or method declaration should remain on a single line
to avoid [indentation confusion](#indentation-confusion).

Function argument lists can make some of the longest lines in a Go source file.
However, they precede a change in indentation, and therefore it is difficult to
break the line in a way that does not make subsequent lines look like part of
the function body in a confusing way:

```go
// Bad:
func (r *SomeType) SomeLongFunctionName(foo1, foo2, foo3 string,
    foo4, foo5, foo6 int) {
    foo7 := bar(foo1)
    // ...
}
```

See [best practices](best-practices#funcargs) for a few options for shortening
the call sites of functions that would otherwise have many arguments.

Lines can often be shortened by factoring out local variables.

```go
// Good:
local := helper(some, parameters, here)
good := foo.Call(list, of, parameters, local)
```

Similarly, function and method calls should not be separated based solely on
line length.

```go
// Good:
good := foo.Call(long, list, of, parameters, all, on, one, line)
```

```go
// Bad:
bad := foo.Call(long, list, of, parameters,
    with, arbitrary, line, breaks)
```

Avoid adding inline comments to specific function arguments where possible.
Instead, use an [option struct](best-practices#option-structure) or add more
detail to the function documentation.

```go
// Good:
good := server.New(ctx, server.Options{Port: 42})
```

```go
// Bad:
bad := server.New(
    ctx,
    42, // Port
)
```

If the API cannot be changed or if the local call is unusual (whether or not the
call is too long), it is always permissible to add line breaks if it aids in
understanding the call.

```go
// Good:
canvas.RenderHeptagon(fillColor,
    x0, y0, vertexColor0,
    x1, y1, vertexColor1,
    x2, y2, vertexColor2,
    x3, y3, vertexColor3,
    x4, y4, vertexColor4,
    x5, y5, vertexColor5,
    x6, y6, vertexColor6,
)
```

Note that the lines in the above example are not wrapped at a specific column
boundary but are grouped based on vertex coordinates and color.

Long string literals within functions should not be broken for the sake of line
length. For functions that include such strings, a line break can be added after
the string format, and the arguments can be provided on the next or subsequent
lines. The decision about where the line breaks should go is best made based on
semantic groupings of inputs, rather than based purely on line length.

```go
// Good:
log.Warningf("Database key (%q, %d, %q) incompatible in transaction started by (%q, %d, %q)",
    currentCustomer, currentOffset, currentKey,
    txCustomer, txOffset, txKey)
```

```go
// Bad:
log.Warningf("Database key (%q, %d, %q) incompatible in"+
    " transaction started by (%q, %d, %q)",
    currentCustomer, currentOffset, currentKey, txCustomer,
    txOffset, txKey)
```

<a id="conditional-formatting"></a>
