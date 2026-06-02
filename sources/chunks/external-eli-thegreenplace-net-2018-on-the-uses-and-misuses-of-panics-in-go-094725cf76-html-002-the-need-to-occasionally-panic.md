---
source_name: "External Linked Documentation"
source_url: "https://eli.thegreenplace.net/2018/on-the-uses-and-misuses-of-panics-in-go/"
source_path: "sources/raw/external/eli-thegreenplace-net-2018-on-the-uses-and-misuses-of-panics-in-go-094725cf76.html"
license_ref: ""
---

## The need to occasionally panic

Go is a _safe_ language with run-time checks for some serious programming errors. For example, when you try to access a slice out of bounds, the result is not undefined behavior. Rather, the Go runtime will _panic_. For example, this minimal program:

```go
package main

import (
  "fmt"
)

func main() {
  s := make([]string, 3)
  fmt.Println(s[5])
}

```

Will die with a runtime error followed by a stack trace:

```go
panic: runtime error: index out of range

goroutine 1 [running]:
main.main()
  /tmp/sandbox209906601/main.go:9 +0x40

```

Other common things that panic include accessing nil structure fields through pointers, closing an already-closed channel, etc. What are the alternatives to panicking here? We _could_ make slice access return a result, err pair, and we could also make slice element assignment a function that potentially returns an error, but this would result in cumbersome code. Imagine rewriting this snippet, where foo, bar and baz are all slices of strings:

```go
foo[i] = bar[i] + baz[i]

```

Into something like:

```go
br, err := bar[i]
if err != nil {
  return err
}
bz, err := baz[i]
if err != nil {
  return err
}
err := assign_slice_element(foo, i, br + bz)
if err != nil {
  return err
}

```

Looks like fun? Nope. Different languages handle this in different ways: Python and Java throw an exception if i points out of bounds in either of the slices/lists/arrays. C will emit code without bounds checking, with a good chance of accessing/trampling the wrong memory area, crashing the process or exposing it to security vulnerabilities. C++ takes the middle way, with some "performance oriented" modes that are unsafe and other modes (std::vector::at) that could throw an exception.

Since the verbosity of the rewritten snippet above is unacceptable, Go chose to have _panics_, which is an exception-like mechanism reserved for _truly exceptional conditions_ such as bugs in the code.

This isn't restricted to built-ins; user code can also panic if needed. Sometimes code encounters errors that can only mean something went horribly wrong - a bug, or some key invariant being violated. For example, a switch case that just can't happen in the current context. The panic function exists for just such cases; it's morally equivalent to Python's raise and C++'s throw. That said, subtle but powerful restrictions on how exceptions are caught make Go's exception handling unique.
