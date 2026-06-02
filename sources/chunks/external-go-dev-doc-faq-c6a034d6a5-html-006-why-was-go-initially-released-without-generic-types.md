---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

## Design

### Why was Go initially released without generic types?

Go was intended as a language for writing server programs that would be easy to maintain over time. (See this article for more background.) The design concentrated on things like scalability, readability, and concurrency. Polymorphic programming did not seem essential to the language’s goals at the time, and so was initially left out for simplicity.

Generics are convenient but they come at a cost in complexity in the type system and run-time. It took a while to develop a design that we believe gives value proportionate to the complexity.

## Design

### Why does Go not have exceptions?

We believe that coupling exceptions to a control structure, as in the `try-catch-finally` idiom, results in convoluted code. It also tends to encourage programmers to label too many ordinary errors, such as failing to open a file, as exceptional.

Go takes a different approach. For plain error handling, Go’s multi-value returns make it easy to report an error without overloading the return value. A canonical error type, coupled with Go’s other features, makes error handling pleasant but quite different from that in other languages.

Go also has a couple of built-in functions to signal and recover from truly exceptional conditions. The recovery mechanism is executed only as part of a function’s state being torn down after an error, which is sufficient to handle catastrophe but requires no extra control structures and, when used well, can result in clean error-handling code.

See the Defer, Panic, and Recover article for details. Also, the Errors are values blog post describes one approach to handling errors cleanly in Go by demonstrating that, since errors are just values, the full power of Go can be deployed in error handling.
