---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/guide.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Maintainability

Code is edited many more times than it is written. Readable code not only makes sense to a reader who is trying to understand how it works, but also to the programmer who needs to change it. Clarity is key.

Maintainable code:

- Is easy for a future programmer to modify correctly
- Has APIs that are structured so that they can grow gracefully
- Is clear about the assumptions that it makes and chooses abstractions that map to the structure of the problem, not to the structure of the code
- Avoids unnecessary coupling and doesn’t include features that are not used
- Has a comprehensive test suite to ensure promised behaviors are maintained and important logic is correct, and the tests provide clear, actionable diagnostics in case of failure

When using abstractions like interfaces and types which by definition remove information from the context in which they are used, it is important to ensure that they provide sufficient benefit. Editors and IDEs can connect directly to a method definition and show the corresponding documentation when a concrete type is used, but can only refer to an interface definition otherwise. Interfaces are a powerful tool, but come with a cost, since the maintainer may need to understand the specifics of the underlying implementation in order to correctly use the interface, which must be explained within the interface documentation or at the call-site.

Maintainable code also avoids hiding important details in places that are easy to overlook. For example, in each of the following lines of code, the presence or lack of a single character is critical to understand the line:

```go
// Bad:
// The use of = instead of := can change this line completely.
if user, err = db.UserByID(userID); err != nil {
    // ...
}

```

```go
// Bad:
// The ! in the middle of this line is very easy to miss.
leap := (year%4 == 0) && (!(year%100 == 0) || (year%400 == 0))

```

Neither of these are incorrect, but both could be written in a more explicit fashion, or could have an accompanying comment that calls attention to the important behavior:

```go
// Good:
u, err := db.UserByID(userID)
if err != nil {
    return fmt.Errorf("invalid origin user: %s", err)
}
user = u

```

```go
// Good:
// Gregorian leap years aren't just year%4 == 0.
// See https://en.wikipedia.org/wiki/Leap_year#Algorithm.
var (
    leap4   = year%4 == 0
    leap100 = year%100 == 0
    leap400 = year%400 == 0
)
leap := leap4 && (!leap100 || leap400)

```

In the same way, a helper function that hides critical logic or an important edge-case could make it easy for a future change to fail to account for it properly.

Predictable names are another feature of maintainable code. A user of a package or a maintainer of a piece of code should be able to predict the name of a variable, method, or function in a given context. Function parameters and receiver names for identical concepts should typically share the same name, both to keep documentation understandable and to facilitate refactoring code with minimal overhead.

Maintainable code minimizes its dependencies (both implicit and explicit). Depending on fewer packages means fewer lines of code that can affect behavior. Avoiding dependencies on internal or undocumented behavior makes code less likely to impose a maintenance burden when those behaviors change in the future.

When considering how to structure or write code, it is worth taking the time to think through ways in which the code may evolve over time. If a given approach is more conducive to easier and safer future changes, that is often a good trade-off, even if it means a slightly more complicated design.
