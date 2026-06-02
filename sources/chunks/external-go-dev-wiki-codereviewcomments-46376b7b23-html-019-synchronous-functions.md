---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## Synchronous Functions

Prefer synchronous functions - functions which return their results directly or finish any callbacks or channel ops before returning - over asynchronous ones.

Synchronous functions keep goroutines localized within a call, making it easier to reason about their lifetimes and avoid leaks and data races. They’re also easier to test: the caller can pass an input and check the output without the need for polling or synchronization.

If callers need more concurrency, they can add it easily by calling the function from a separate goroutine. But it is quite difficult - sometimes impossible - to remove unnecessary concurrency at the caller side.

# Go Wiki: Go Code Review Comments

## Useful Test Failures

Tests should fail with helpful messages saying what was wrong, with what inputs, what was actually got, and what was expected. It may be tempting to write a bunch of assertFoo helpers, but be sure your helpers produce useful error messages. Assume that the person debugging your failing test is not you, and is not your team. A typical Go test fails like:

```go
if got != tt.want {
    t.Errorf("Foo(%q) = %d; want %d", tt.in, got, tt.want) // or Fatalf, if test can't test anything more past this point
}

```

Note that the order here is actual != expected, and the message uses that order too. Some test frameworks encourage writing these backwards: 0 != x, “expected 0, got x”, and so on. Go does not.

If that seems like a lot of typing, you may want to write a table-driven test.

Another common technique to disambiguate failing tests when using a test helper with different input is to wrap each caller with a different TestFoo function, so the test fails with that name:

```go
func TestSingleValue(t *testing.T) { testHelper(t, []int{80}) }
func TestNoValues(t *testing.T)    { testHelper(t, []int{}) }

```

In any case, the onus is on you to fail with a helpful message to whoever’s debugging your code in the future.

# Go Wiki: Go Code Review Comments

## Variable Names

Variable names in Go should be short rather than long. This is especially true for local variables with limited scope. Prefer `c` to `lineCount`. Prefer `i` to `sliceIndex`.

The basic rule: the further from its declaration that a name is used, the more descriptive the name must be. For a method receiver, one or two letters is sufficient. Common variables such as loop indices and readers can be a single letter (`i`, `r`). More unusual things and global variables need more descriptive names.

See also the longer discussion in the Google Go Style Guide <https://google.github.io/styleguide/go/decisions#variable-names>.

 _This content is part of the Go Wiki._
