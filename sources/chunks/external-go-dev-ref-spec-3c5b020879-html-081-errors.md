---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

# The Go Programming Language Specification

## Errors

 The predeclared type `error` is defined as

```go

type error interface {
	Error() string
}

```

 It is the conventional interface for representing an error condition, with the nil value representing no error. For instance, a function to read data from a file might be defined:

```go

func Read(f *File, b []byte) (n int, err error)

```

# The Go Programming Language Specification

## Run-time panics

 Execution errors such as attempting to index an array out of bounds trigger a _run-time panic_ equivalent to a call of the built-in function `panic` with a value of the implementation-defined interface type `runtime.Error`. That type satisfies the predeclared interface type `error`. The exact error values that represent distinct run-time error conditions are unspecified.

```go

package runtime

type Error interface {
	error
	// and perhaps other methods
}

```
