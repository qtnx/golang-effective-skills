---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Named result parameters

<a id="TOC-NamedResultParameters"></a>

When naming parameters, consider how function signatures appear in Godoc. The
name of the function itself and the type of the result parameters are often
sufficiently clear.

```go
// Good:
func (n *Node) Parent1() *Node
func (n *Node) Parent2() (*Node, error)
```

If a function returns two or more parameters of the same type, adding names can
be useful.

```go
// Good:
func (n *Node) Children() (left, right *Node, err error)
```

If the caller must take action on particular result parameters, naming them can
help suggest what the action is:

```go
// Good:
// WithTimeout returns a context that will be canceled no later than d duration
// from now.
//
// The caller must arrange for the returned cancel function to be called when
// the context is no longer needed to prevent a resource leak.
func WithTimeout(parent Context, d time.Duration) (ctx Context, cancel func())
```

In the code above, cancellation is a particular action a caller must take.
However, were the result parameters written as `(Context, func())` alone, it
would be unclear what is meant by "cancel function".

Don't use named result parameters when the names produce
[unnecessary repetition](#repetitive-with-type).

```go
// Bad:
func (n *Node) Parent1() (node *Node)
func (n *Node) Parent2() (node *Node, err error)
```

Don't name result parameters in order to avoid declaring a variable inside the
function. This practice results in unnecessary API verbosity at the cost of
minor implementation brevity.

[Naked returns] are acceptable only in a small function. Once it's a
medium-sized function, be explicit with your returned values. Similarly, do not
name result parameters just because it enables you to use naked returns.
[Clarity](guide#clarity) is always more important than saving a few lines in
your function.

It is always acceptable to name a result parameter if its value must be changed
in a deferred closure.

> **Tip:** Types can often be clearer than names in function signatures.
> [GoTip #38: Functions as Named Types] demonstrates this.
>
> In, [`WithTimeout`] above, the real code uses a [`CancelFunc`] instead of a
> raw `func()` in the result parameter list and requires little effort to
> document.

[Naked returns]: https://tour.golang.org/basics/7
[GoTip #38: Functions as Named Types]: https://google.github.io/styleguide/go/index.html#gotip
[`WithTimeout`]: https://pkg.go.dev/context#WithTimeout
[`CancelFunc`]: https://pkg.go.dev/context#CancelFunc

<a id="package-comments"></a>
