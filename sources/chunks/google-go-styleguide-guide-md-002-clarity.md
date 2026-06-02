---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/guide.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

# Go Style Guide

### Clarity

The core goal of readability is to produce code that is clear to the reader.

Clarity is primarily achieved with effective naming, helpful commentary, and
efficient code organization.

Clarity is to be viewed through the lens of the reader, not the author of the
code. It is more important that code be easy to read than easy to write. Clarity
in code has two distinct facets:

*   [What is the code actually doing?](#clarity-purpose)
*   [Why is the code doing what it does?](#clarity-rationale)

<a id="clarity-purpose"></a>

#### What is the code actually doing?

Go is designed such that it should be relatively straightforward to see what the
code is doing. In cases of uncertainty or where a reader may require prior
knowledge in order to understand the code, it is worth investing time in order
to make the code's purpose clearer for future readers. For example, it may help
to:

*   Use more descriptive variable names
*   Add additional commentary
*   Break up the code with whitespace and comments
*   Refactor the code into separate functions/methods to make it more modular

There is no one-size-fits-all approach here, but it is important to prioritize
clarity when developing Go code.

<a id="clarity-rationale"></a>

#### Why is the code doing what it does?

The code's rationale is often sufficiently communicated by the names of
variables, functions, methods, or packages. Where it is not, it is important to
add commentary. The "Why?" is especially important when the code contains
nuances that a reader may not be familiar with, such as:

*   A nuance in the language, e.g., a closure will be capturing a loop variable,
    but the closure is many lines away
*   A nuance of the business logic, e.g., an access control check that needs to
    distinguish between the actual user and someone impersonating a user

An API might require care to use correctly. For example, a piece of code may be
intricate and difficult to follow for performance reasons, or a complex sequence
of mathematical operations may use type conversions in an unexpected way. In
these cases and many more, it is important that accompanying commentary and
documentation explain these aspects so that future maintainers don't make a
mistake and so that readers can understand the code without needing to
reverse-engineer it.

It is also important to be aware that some attempts to provide clarity (such as
adding extra commentary) can actually obscure the code's purpose by adding
clutter, restating what the code already says, contradicting the code, or adding
maintenance burden to keep the comments up-to-date. Allow the code to speak for
itself (e.g., by making the symbol names themselves self-describing) rather than
adding redundant comments. It is often better for comments to explain why
something is done, not what the code is doing.

The Google codebase is largely uniform and consistent. It is often the case that
code that stands out (e.g., by using an unfamiliar pattern) is doing so for a
good reason, typically for performance. Maintaining this property is important
to make it clear to readers where they should focus their attention when reading
a new piece of code.

The standard library contains many examples of this principle in action. Among
them:

*   Maintainer comments in
    [`package sort`](https://cs.opensource.google/go/go/+/refs/tags/go1.19.2:src/sort/sort.go).
*   Good
    [runnable examples in the same package](https://cs.opensource.google/go/go/+/refs/tags/go1.19.2:src/sort/example_search_test.go),
    which benefit both users (they
    [show up in godoc](https://pkg.go.dev/sort#pkg-examples)) and maintainers
    (they [run as part of tests](decisions#examples)).
*   [`strings.Cut`](https://pkg.go.dev/strings#Cut) is only four lines of code,
    but they improve the
    [clarity and correctness of callsites](https://github.com/golang/go/issues/46336).

<a id="simplicity"></a>
