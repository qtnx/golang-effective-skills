---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Statements

### Empty statements

 The empty statement does nothing.

```go

EmptyStmt = .

```

## Statements

### Labeled statements

 A labeled statement may be the target of a `goto`, `break` or `continue` statement.

```go

LabeledStmt = Label ":" Statement .
Label       = identifier .

```

```go

Error: log.Panic("error encountered")

```

## Statements

### Expression statements

 With the exception of specific built-in functions, function and method calls and receive operations can appear in statement context. Such statements may be parenthesized.

```go

ExpressionStmt = Expression .

```

 The following built-in functions are not permitted in statement context:

```go

append cap complex imag len make new real
unsafe.Add unsafe.Alignof unsafe.Offsetof unsafe.Sizeof unsafe.Slice unsafe.SliceData unsafe.String unsafe.StringData

```

```go

h(x+y)
f.Close()
<-ch
(<-ch)
len("foo")  // illegal if len is the built-in function

```
