---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Util packages

Go packages have a name specified on the `package` declaration, separate from the import path. The package name matters more for readability than the path.

Go package names should be related to what the package provides. Naming a package just `util`, `helper`, `common` or similar is usually a poor choice (it can be used as _part_ of the name though). Uninformative names make the code harder to read, and if used too broadly they are liable to cause needless import conflicts.

Instead, consider what the callsite will look like.

```go
// Good:
db := spannertest.NewDatabaseFromFile(...)

_, err := f.Seek(0, io.SeekStart)

b := elliptic.Marshal(curve, x, y)

```

You can tell roughly what each of these do even without knowing the imports list (`cloud.google.com/go/spanner/spannertest`, `io`, and `crypto/elliptic`). With less focused names, these might read:

```go
// Bad:
db := test.NewDatabaseFromFile(...)

_, err := f.Seek(0, common.SeekStart)

b := helper.Marshal(curve, x, y)

```
