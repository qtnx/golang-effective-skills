---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Statements

### Break statements

 A "break" statement terminates execution of the innermost "for", "switch", or "select" statement within the same function.

```go

BreakStmt = "break" [ Label ] .

```

 If there is a label, it must be that of an enclosing "for", "switch", or "select" statement, and that is the one whose execution terminates.

```go

OuterLoop:
	for i = 0; i < n; i++ {
		for j = 0; j < m; j++ {
			switch a[i][j] {
			case nil:
				state = Error
				break OuterLoop
			case item:
				state = Found
				break OuterLoop
			}
		}
	}

```

## Statements

### Continue statements

 A "continue" statement begins the next iteration of the innermost enclosing "for" loop by advancing control to the end of the loop block. The "for" loop must be within the same function.

```go

ContinueStmt = "continue" [ Label ] .

```

 If there is a label, it must be that of an enclosing "for" statement, and that is the one whose execution advances.

```go

RowLoop:
	for y, row := range rows {
		for x, data := range row {
			if data == endOfRow {
				continue RowLoop
			}
			row[x] = data + bias(x, y)
		}
	}

```
