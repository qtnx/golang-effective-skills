---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/faq"
source_path: "sources/raw/external/go-dev-doc-faq-c6a034d6a5.html"
license_ref: ""
---

# Frequently Asked Questions (FAQ)

## Functions and Methods

### Why do T and *T have different method sets?

As the Go specification says, the method set of a type `T` consists of all methods with receiver type `T`, while that of the corresponding pointer type `*T` consists of all methods with receiver `*T` or `T`. That means the method set of `*T` includes that of `T`, but not the reverse.

This distinction arises because if an interface value contains a pointer `*T`, a method call can obtain a value by dereferencing the pointer, but if an interface value contains a value `T`, there is no safe way for a method call to obtain a pointer. (Doing so would allow a method to modify the contents of the value inside the interface, which is not permitted by the language specification.)

Even in cases where the compiler could take the address of a value to pass to the method, if the method modifies the value the changes will be lost in the caller.

As an example, if the code below were valid:

```go
var buf bytes.Buffer
io.Copy(buf, os.Stdin)

```

it would copy standard input into a _copy_ of `buf`, not into `buf` itself. This is almost never the desired behavior and is therefore disallowed by the language.

### What happens with closures running as goroutines?

Due to the way loop variables work, before Go version 1.22 (see the end of this section for an update), some confusion could arise when using closures with concurrency. Consider the following program:

```go

func main() {
    done := make(chan bool)

    values := []string{"a", "b", "c"}
    for _, v := range values {
        go func() {
            fmt.Println(v)
            done <- true
        }()
    }

    // wait for all goroutines to complete before exiting
    for _ = range values {
        <-done
    }
}

```

One might mistakenly expect to see `a, b, c` as the output. What you’ll probably see instead is `c, c, c`. This is because each iteration of the loop uses the same instance of the variable `v`, so each closure shares that single variable. When the closure runs, it prints the value of `v` at the time `fmt.Println` is executed, but `v` may have been modified since the goroutine was launched. To help detect this and other problems before they happen, run `go vet`.

To bind the current value of `v` to each closure as it is launched, one must modify the inner loop to create a new variable each iteration. One way is to pass the variable as an argument to the closure:

```go

    for _, v := range values {
        go func(**u** string) {
            fmt.Println(**u**)
            done <- true
        }(**v**)
    }

```

In this example, the value of `v` is passed as an argument to the anonymous function. That value is then accessible inside the function as the variable `u`.

Even easier is just to create a new variable, using a declaration style that may seem odd but works fine in Go:

```go

    for _, v := range values {
        **v := v** // create a new 'v'.
        go func() {
            fmt.Println(**v**)
            done <- true
        }()
    }

```

This behavior of the language, not defining a new variable for each iteration, was considered a mistake in retrospect, and has been addressed in Go 1.22, which does indeed create a new variable for each iteration, eliminating this issue.
