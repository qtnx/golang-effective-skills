---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Statements

### Go statements

 A "go" statement starts the execution of a function call as an independent concurrent thread of control, or _goroutine_, within the same address space.

```go

GoStmt = "go" Expression .

```

 The expression must be a function or method call; it cannot be parenthesized. Calls of built-in functions are restricted as for expression statements.

 The function value and parameters are evaluated as usual in the calling goroutine, but unlike with a regular call, program execution does not wait for the invoked function to complete. Instead, the function begins executing independently in a new goroutine. When the function terminates, its goroutine also terminates. If the function has any return values, they are discarded when the function completes.

```go

go Server()
go func(ch chan<- bool) { for { sleep(10); ch <- true }} (c)

```
