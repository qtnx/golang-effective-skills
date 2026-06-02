---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Shadowing

**Note:** This explanation uses two informal terms, *stomping* and *shadowing*.
They are not official concepts in the Go language spec.

Like many programming languages, Go has mutable variables: assigning to a
variable changes its value.

```go
// Good:
func abs(i int) int {
    if i < 0 {
        i *= -1
    }
    return i
}
```

When using [short variable declarations] with the `:=` operator, in some cases a
new variable is not created. We can call this *stomping*. It's OK to do this
when the original value is no longer needed.

```go
// Good:
// innerHandler is a helper for some request handler, which itself issues
// requests to other backends.
func (s *Server) innerHandler(ctx context.Context, req *pb.MyRequest) *pb.MyResponse {
    // Unconditionally cap the deadline for this part of request handling.
    ctx, cancel := context.WithTimeout(ctx, 3*time.Second)
    defer cancel()
    ctxlog.Info(ctx, "Capped deadline in inner request")

    // Code here no longer has access to the original context.
    // This is good style if when first writing this, you anticipate
    // that even as the code grows, no operation legitimately should
    // use the (possibly unbounded) original context that the caller provided.

    // ...
}
```

Be careful using short variable declarations in a new scope, though: that
introduces a new variable. We can call this *shadowing* the original variable.
Code after the end of the block refers to the original. Here is a buggy attempt
to shorten the deadline conditionally:

```go
// Bad:
func (s *Server) innerHandler(ctx context.Context, req *pb.MyRequest) *pb.MyResponse {
    // Attempt to conditionally cap the deadline.
    if *shortenDeadlines {
        ctx, cancel := context.WithTimeout(ctx, 3*time.Second)
        defer cancel()
        ctxlog.Info(ctx, "Capped deadline in inner request")
    }

    // BUG: "ctx" here again means the context that the caller provided.
    // The above buggy code compiled because both ctx and cancel
    // were used inside the if statement.

    // ...
}
```

A correct version of the code might be:

```go
// Good:
func (s *Server) innerHandler(ctx context.Context, req *pb.MyRequest) *pb.MyResponse {
    if *shortenDeadlines {
        var cancel func()
        // Note the use of simple assignment, = and not :=.
        ctx, cancel = context.WithTimeout(ctx, 3*time.Second)
        defer cancel()
        ctxlog.Info(ctx, "Capped deadline in inner request")
    }
    // ...
}
```

In the case we called stomping, because there's no new variable, the type being
assigned must match that of the original variable. With shadowing, an entirely
new entity is introduced so it can have a different type. Intentional shadowing
can be a useful practice, but you can always use a new name if it improves
[clarity](guide#clarity).

It is not a good idea to use variables with the same name as standard packages
other than very small scopes, because that renders free functions and values
from that package inaccessible. Conversely, when picking a name for your
package, avoid names that are likely to require
[import renaming](decisions#import-renaming) or cause shadowing of otherwise
good variable names at the client side.

```go
// Bad:
func LongFunction() {
    url := "https://example.com/"
    // Oops, now we can't use net/url in code below.
}
```

[short variable declarations]: https://go.dev/ref/spec#Short_variable_declarations

<a id="util-packages"></a>
