---
source_name: "External Linked Documentation"
source_url: "https://docs.bazel.build/versions/main/be/general.html"
source_path: "sources/raw/external/docs-bazel-build-versions-main-be-general-html-1d20475b8b.html"
license_ref: ""
---

# General Rules

##  genquery

```go
genquery(name, deps, data, compatible_with, deprecation, distribs, exec_compatible_with, exec_properties, expression, features, licenses, opts, restricted_to, scope, strict, tags, target_compatible_with, testonly, visibility)
```

 `genquery()` runs a query specified in the Bazel query language and dumps the result into a file.

 In order to keep the build consistent, the query is allowed only to visit the transitive closure of the targets specified in the `scope` attribute. Queries violating this rule will fail during execution if `strict` is unspecified or true (if `strict` is false, the out of scope targets will simply be skipped with a warning). The easiest way to make sure this does not happen is to mention the same labels in the scope as in the query expression.

 The only difference between the queries allowed here and on the command line is that queries containing wildcard target specifications (e.g. `//pkg:*` or `//pkg:all`) are not allowed here. The reasons for this are two-fold: first, because `genquery` has to specify a scope to prevent targets outside the transitive closure of the query to influence its output; and, second, because `BUILD` files do not support wildcard dependencies (e.g. `deps=["//a/..."]` is not allowed).

 The genquery's output is ordered using `--order_output=full` in order to enforce deterministic output.
 The name of the output file is the name of the rule.

#### Examples

 This example writes the list of the labels in the transitive closure of the specified target to a file.

```go

genquery(
    name = "kiwi-deps",
    expression = "deps(//kiwi:kiwi_lib)",
    scope = ["//kiwi:kiwi_lib"],
)

```

### Arguments
        Attributes     `name`
`Name; required`

A unique name for this target.
     `expression`
`String; required`
 The query to be executed. In contrast to the command line and other places in BUILD files, labels here are resolved relative to the root directory of the workspace. For example, the label `:b` in this attribute in the file `a/BUILD` will refer to the target `//:b`.     `opts`
`List of strings; optional`
 The options that are passed to the query engine. These correspond to the command line options that can be passed to `bazel query`. Some query options are not allowed here: `--keep_going`, `--query_file`, `--universe_scope`, `--order_results` and `--order_output`. Options not specified here will have their default values just like on the command line of `bazel query`.     `scope`
`List of labels; required`
 The scope of the query. The query is not allowed to touch targets outside the transitive closure of these targets.     `strict`
`Boolean; optional; default is True`
 If true, targets whose queries escape the transitive closure of their scopes will fail to build. If false, Bazel will print a warning and skip whatever query path led it outside of the scope, while completing the rest of the query.
