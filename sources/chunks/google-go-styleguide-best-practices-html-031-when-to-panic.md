---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### When to panic

The standard library panics on API misuse. For example, `reflect` issues a panic in many cases where a value is accessed in a way that suggests it was misinterpreted. This is analogous to the panics on core language bugs such as accessing an element of a slice that is out of bounds. Code review and tests should discover such bugs, which are not expected to appear in production code. These panics act as invariant checks that do not depend on a library, as the standard library does not have access to the levelled `log` package that the Google codebase uses.

Another case in which panics can be useful, though uncommon, is as an internal implementation detail of a package which always has a matching recover in the callchain. Parsers and similar deeply nested, tightly coupled internal function groups can benefit from this design, where plumbing error returns adds complexity without value.

The key attribute of this design is that these **panics are never allowed to escape across package boundaries** and do not form part of the package’s API. This is typically accomplished with a top-level deferred function that uses `recover` to translate a propagated panic into a returned error at the public API boundary. It requires the code that panics and recovers to distinguish between panics that the code raises itself and those that it doesn’t:

```go
// Good:
type syntaxError struct {
  msg string
}

func parseInt(in string) int {
  n, err := strconv.Atoi(in)
  if err != nil {
    panic(&syntaxError{"not a valid integer"})
  }
}

func Parse(in string) (_ *Node, err error) {
  defer func() {
    if p := recover(); p != nil {
      sErr, ok := p.(*syntaxError)
      if !ok {
        panic(p) // Propagate the panic since it is outside our code's domain.
      }
      err = fmt.Errorf("syntax error: %v", sErr.msg)
    }
  }()
  ... // Parse input calling parseInt internally to parse integers
}

```

**Warning:** Code employing this pattern must take care to manage any resources associated with the code run in such defer-managed sections (e.g., close, free, or unlock).

See: Go Tip #81: Avoiding Resource Leaks in API Design

Panic is also used when the compiler cannot identify unreachable code, for example when using a function like `log.Fatal` that will not return:

```go
// Good:
func answer(i int) string {
    switch i {
    case 42:
        return "yup"
    case 54:
        return "base 13, huh"
    default:
        log.Fatalf("Sorry, %d is not the answer.", i)
        panic("unreachable")
    }
}

```

Do not call `log` functions before flags have been parsed. If you must die in a package initialization function (an `init` or a “must” function), a panic is acceptable in place of the fatal logging call.

See also:

- Handling panics and Run-time Panics in the language specification
- Defer, Panic, and Recover
- On the uses and misuses of panics in Go
