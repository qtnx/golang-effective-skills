---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Statements

### Goto statements

 A "goto" statement transfers control to the statement with the corresponding label within the same function.

```go

GotoStmt = "goto" Label .

```

```go

goto Error

```

 Executing the "goto" statement must not cause any variables to come into scope that were not already in scope at the point of the goto. For instance, this example:

```go

	goto L  // BAD
	v := 3
L:

```

 is erroneous because the jump to label `L` skips the creation of `v`.

 A "goto" statement outside a block cannot jump to a label inside that block. For instance, this example:

```go

if n%2 == 1 {
	goto L1
}
for n > 0 {
	f()
	n--
L1:
	f()
	n--
}

```

 is erroneous because the label `L1` is inside the "for" statement's block but the `goto` is not.
