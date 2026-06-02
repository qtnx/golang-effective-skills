---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/guide.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Simplicity

Your Go code should be simple for those using, reading, and maintaining it.

Go code should be written in the simplest way that accomplishes its goals, both
in terms of behavior and performance. Within the Google Go codebase, simple
code:

*   Is easy to read from top to bottom
*   Does not assume that you already know what it is doing
*   Does not assume that you can memorize all of the preceding code
*   Does not have unnecessary levels of abstraction
*   Does not have names that call attention to something mundane
*   Makes the propagation of values and decisions clear to the reader
*   Has comments that explain why, not what, the code is doing to avoid future
    deviation
*   Has documentation that stands on its own
*   Has useful errors and useful test failures
*   May often be mutually exclusive with "clever" code

Tradeoffs can arise between code simplicity and API usage simplicity. For
example, it may be worthwhile to have the code be more complex so that the end
user of the API may more easily call the API correctly. In contrast, it may also
be worthwhile to leave a bit of extra work to the end user of the API so that
the code remains simple and easy to understand.

When code needs complexity, the complexity should be added deliberately. This is
typically necessary if additional performance is required or where there are
multiple disparate customers of a particular library or service. Complexity may
be justified, but it should come with accompanying documentation so that clients
and future maintainers are able to understand and navigate the complexity. This
should be supplemented with tests and examples that demonstrate its correct
usage, especially if there is both a "simple" and a "complex" way to use the
code.

This principle does not imply that complex code cannot or should not be written
in Go or that Go code is not allowed to be complex. We strive for a codebase
that avoids unnecessary complexity so that when complexity does appear, it
indicates that the code in question requires care to understand and maintain.
Ideally, there should be accompanying commentary that explains the rationale and
identifies the care that should be taken. This often arises when optimizing code
for performance; doing so often requires a more complex approach, like
preallocating a buffer and reusing it throughout a goroutine lifetime. When a
maintainer sees this, it should be a clue that the code in question is
performance-critical, and that should influence the care that is taken when
making future changes. If employed unnecessarily, on the other hand, this
complexity is a burden on those who need to read or change the code in the
future.

If code turns out to be very complex when its purpose should be simple, this is
often a signal to revisit the implementation to see if there is a simpler way to
accomplish the same thing.

<a id="least-mechanism"></a>
