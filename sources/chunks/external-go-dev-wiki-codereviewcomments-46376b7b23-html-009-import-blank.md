---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## Import Blank

Packages that are imported only for their side effects (using the syntax `import _ "pkg"`) should only be imported in the main package of a program, or in tests that require them.

# Go Wiki: Go Code Review Comments

## Import Dot

The import . form can be useful in tests that, due to circular dependencies, cannot be made part of the package being tested:

```go
package foo_test

import (
    "bar/testutil" // also imports "foo"
    . "foo"
)

```

In this case, the test file cannot be in package foo because it uses bar/testutil, which imports foo. So we use the ‘import .’ form to let the file pretend to be part of package foo even though it is not. Except for this one case, do not use import . in your programs. It makes the programs much harder to read because it is unclear whether a name like Quux is a top-level identifier in the current package or in an imported package.
