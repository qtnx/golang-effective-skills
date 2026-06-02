---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Statements

### Fallthrough statements

 A "fallthrough" statement transfers control to the first statement of the next case clause in an expression "switch" statement. It may be used only as the final non-empty statement in such a clause.

```go

FallthroughStmt = "fallthrough" .

```

## Statements

### Defer statements

 A "defer" statement invokes a function whose execution is deferred to the moment the surrounding function returns, either because the surrounding function executed a return statement, reached the end of its function body, or because the corresponding goroutine is panicking.

```go

DeferStmt = "defer" Expression .

```

 The expression must be a function or method call; it cannot be parenthesized. Calls of built-in functions are restricted as for expression statements.

 Each time a "defer" statement executes, the function value and parameters to the call are evaluated as usual and saved anew but the actual function is not invoked. Instead, deferred functions are invoked immediately before the surrounding function returns, in the reverse order they were deferred. That is, if the surrounding function returns through an explicit return statement, deferred functions are executed _after_ any result parameters are set by that return statement but _before_ the function returns to its caller. If a deferred function value evaluates to `nil`, execution panics when the function is invoked, not when the "defer" statement is executed.

 For instance, if the deferred function is a function literal and the surrounding function has named result parameters that are in scope within the literal, the deferred function may access and modify the result parameters before they are returned. If the deferred function has any return values, they are discarded when the function completes. (See also the section on handling panics.)

```go

lock(l)
defer unlock(l)  // unlocking happens before surrounding function returns

// prints 3 2 1 0 before surrounding function returns
for i := 0; i <= 3; i++ {
	defer fmt.Print(i)
}

// f returns 42
func f() (result int) {
	defer func() {
		// result is accessed after it was set to 6 by the return statement
		result *= 7
	}()
	return 6
}

```
