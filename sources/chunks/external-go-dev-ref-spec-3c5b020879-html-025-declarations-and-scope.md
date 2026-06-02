---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Declarations and scope
 A _declaration_ binds a non-blank identifier to a constant, type, type parameter, variable, function, label, or package. Every identifier in a program must be declared. No identifier may be declared twice in the same block, and no identifier may be declared in both the file and package block.
 The blank identifier may be used like any other identifier in a declaration, but it does not introduce a binding and thus is not declared. In the package block, the identifier `init` may only be used for `init` function declarations, and like the blank identifier it does not introduce a new binding.
```go
Declaration  = ConstDecl | TypeDecl | VarDecl .
TopLevelDecl = Declaration | FunctionDecl | MethodDecl .
```
 The _scope_ of a declared identifier is the extent of source text in which the identifier denotes the specified constant, type, variable, function, label, or package.
 Go is lexically scoped using blocks:
- The scope of a predeclared identifier is the universe block.
- The scope of an identifier denoting a constant, type, variable, or function (but not method) declared at top level (outside any function) is the package block.
- The scope of the package name of an imported package is the file block of the file containing the import declaration.
- The scope of an identifier denoting a method receiver, function parameter, or result variable is the function body.
- The scope of an identifier denoting a type parameter of a function or declared by a method receiver begins after the name of the function and ends at the end of the function body.
- The scope of an identifier denoting a type parameter of a type begins after the name of the type and ends at the end of the TypeSpec.
- The scope of a constant or variable identifier declared inside a function begins at the end of the ConstSpec or VarSpec (ShortVarDecl for short variable declarations) and ends at the end of the innermost containing block.
- The scope of a type identifier declared inside a function begins at the identifier in the TypeSpec and ends at the end of the innermost containing block.
 An identifier declared in a block may be redeclared in an inner block. While the identifier of the inner declaration is in scope, it denotes the entity declared by the inner declaration.
 The package clause is not a declaration; the package name does not appear in any scope. Its purpose is to identify the files belonging to the same package and to specify the default package name for import declarations.
