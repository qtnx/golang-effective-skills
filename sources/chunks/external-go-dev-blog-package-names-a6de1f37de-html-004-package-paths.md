---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/package-names"
source_path: "sources/raw/external/go-dev-blog-package-names-a6de1f37de.html"
license_ref: ""
---

# The Go Blog

## Package paths

A Go package has both a name and a path. The package name is specified in the package statement of its source files; client code uses it as the prefix for the package’s exported names. Client code uses the package path when importing the package. By convention, the last element of the package path is the package name:

```go
import (
    "context"                // package context
    "fmt"                    // package fmt
    "golang.org/x/time/rate" // package rate
    "os/exec"                // package exec
)

```

Build tools map package paths onto directories. The go tool uses the GOPATH environment variable to find the source files for path `"github.com/user/hello"` in directory `$GOPATH/src/github.com/user/hello`. (This situation should be familiar, of course, but it’s important to be clear about the terminology and structure of packages.)

**Directories.** The standard library uses directories like `crypto`, `container`, `encoding`, and `image` to group packages for related protocols and algorithms. There is no actual relationship among the packages in one of these directories; a directory just provides a way to arrange the files. Any package can import any other package provided the import does not create a cycle.

Just as types in different packages can have the same name without ambiguity, packages in different directories can have the same name. For example, runtime/pprof provides profiling data in the format expected by the pprof <https://github.com/google/pprof> profiling tool, while net/http/pprof provides HTTP endpoints to present profiling data in this format. Client code uses the package path to import the package, so there is no confusion. If a source file needs to import both `pprof` packages, it can rename one or both locally. When renaming an imported package, the local name should follow the same guidelines as package names (lower case, no `under_scores` or `mixedCaps`).
