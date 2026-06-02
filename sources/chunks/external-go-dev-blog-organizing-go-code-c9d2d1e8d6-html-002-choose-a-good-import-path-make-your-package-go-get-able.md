---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/organizing-go-code"
source_path: "sources/raw/external/go-dev-blog-organizing-go-code-c9d2d1e8d6.html"
license_ref: ""
---

# The Go Blog

## Choose a good import path (make your package “go get”-able)

An import path is the string with which users import a package. It specifies the directory (relative to `$GOROOT/src/pkg` or `$GOPATH/src`) in which the package’s source code resides.

Import paths should be globally unique, so use the path of your source repository as its base. For instance, the `websocket` package from the `go.net` sub-repository has an import path of `"golang.org/x/net/websocket"`. The Go project owns the path `"github.com/golang"`, so that path cannot be used by another author for a different package. Because the repository URL and import path are one and the same, the `go get` command can fetch and install the package automatically.

If you don’t use a hosted source repository, choose some unique prefix such as a domain, company, or project name. As an example, the import path of all Google’s internal Go code starts with the string `"google"`.

The last element of the import path is typically the same as the package name. For instance, the import path `"net/http"` contains package `http`. This is not a requirement - you can make them different if you like - but you should follow the convention for predictability’s sake: a user might be surprised that import `"foo/bar"` introduces the identifier `quux` into the package name space.

Sometimes people set `GOPATH` to the root of their source repository and put their packages in directories relative to the repository root, such as `"src/my/package"`. On one hand, this keeps the import paths short (`"my/package"` instead of `"github.com/me/project/my/package"`), but on the other it breaks `go get` and forces users to re-set their `GOPATH` to use the package. Don’t do this.
