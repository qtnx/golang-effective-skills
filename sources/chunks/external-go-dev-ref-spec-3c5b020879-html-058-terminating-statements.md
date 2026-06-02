---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Statements
 Statements control execution.
```go
Statement  = Declaration | LabeledStmt | SimpleStmt |
             GoStmt | ReturnStmt | BreakStmt | ContinueStmt | GotoStmt |
             FallthroughStmt | Block | IfStmt | SwitchStmt | SelectStmt | ForStmt |
             DeferStmt .
SimpleStmt = EmptyStmt | ExpressionStmt | SendStmt | IncDecStmt | Assignment | ShortVarDecl .
```
### Terminating statements

 A _terminating statement_ interrupts the regular flow of control in a block. The following statements are terminating:

-  A "return" or "goto" statement.

-  A call to the built-in function `panic`.

-  A block in which the statement list ends in a terminating statement.

-  An "if" statement in which:
- the "else" branch is present, and
- both branches are terminating statements.

-  A "for" statement in which:
- there are no "break" statements referring to the "for" statement, and
- the loop condition is absent, and
- the "for" statement does not use a range clause.

-  A "switch" statement in which:
- there are no "break" statements referring to the "switch" statement,
- there is a default case, and
- the statement lists in each case, including the default, end in a terminating statement, or a possibly labeled "fallthrough" statement.

-  A "select" statement in which:
- there are no "break" statements referring to the "select" statement, and
- the statement lists in each case, including the default if present, end in a terminating statement.

-  A labeled statement labeling a terminating statement.

 All other statements are not terminating.

 A statement list ends in a terminating statement if the list is not empty and its final non-empty statement is terminating.
