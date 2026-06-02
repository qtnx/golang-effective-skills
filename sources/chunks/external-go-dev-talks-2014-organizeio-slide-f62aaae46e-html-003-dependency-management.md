---
source_name: "External Linked Documentation"
source_url: "https://go.dev/talks/2014/organizeio.slide"
source_path: "sources/raw/external/go-dev-talks-2014-organizeio-slide-f62aaae46e.html"
license_ref: ""
---

# Organizing Go code

## Dependency management
 16
### In production, versions matter.

 `go` `get` always fetches the latest code, even if your build breaks.

 That's fine when developing. It's not fine when releasing.
 We need other tools.
 17
### Versioning

 My favorite technique: vendoring.

 For building binaries, import the packages you care about
 into a `_vendor` workspace.

```go
GOPATH=/tmp/gows/_vendor:/tmp/gows
```

 For building libraries, import the packages you care about
 into your repository. Rename the imports to:

```go
import "github.com/you/proj/vendor/github.com/them/lib"
```

 Long paths, but trivial to automate. Write a Go program!

 Another technique: gopkg.in <http://gopkg.in>, provides versioned package paths:

```go
gopkg.in/user/pkg.v3 -> github.com/user/pkg (branch/tag v3, v3.N, or v.3.N.M)
```

 18

# Organizing Go code

## Naming
 19
### Names matter

 Programs are full of names. Names have costs and benefits.

 **Costs**: **space** **and** **time**
 Names need to be in short term memory when reading code.
 You can only fit so many. Longer names take up more space.

 **Benefits:** **information**
 A good name is not only a referent, it conveys information.

 Use the shortest name that carries the right amount of information in its context.

 Devote time to naming.
 20
### Name style

 Use `camelCase`, `not_underscores`.
 Local variable names should be short, typically one or two characters.

 Package names are usually one lowercase word.

 Global variables should have longer names.

 Don't stutter.

- `bytes.Buffer` not `bytes.ByteBuffer`
- `zip.Reader` not `zip.ZipReader`
- `errors.New` not `errors.NewError`
- `r` not `bytesReader`
- `i` not `loopIterator`
 21
### Doc comments

 Doc comments precede the declaration of an exported identifier:

```go
// Join concatenates the elements of elem to create a single string.
// The separator string sep is placed between elements in the resulting string.
func Join(elem []string, sep string) string {
```

 The godoc tool extracts such comments and presents them on the web:

 22
### Writing doc comments

 Doc comments should be English sentences and paragraphs.
 They use no special formatting beyond indentation for preformatted text.

 Doc comments should begin with the noun they describe.

```go
// Join concatenates…         good
// This function…             bad
```

 Package docs go above the package declaration:

```go
// Package fmt…
package fmt
```

 Read the world's Go docs on pkg.go.dev <https://pkg.go.dev>. E.g.

 pkg.go.dev/golang.org/x/tools/txtar <https://pkg.go.dev/golang.org/x/tools/txtar>
 23

# Organizing Go code

## Questions?
 24
### Thank you

 David Crawshaw

crawshaw@golang.org

  Use the left and right arrow keys or click the left and right edges of the page to navigate between slides.
 (Press 'H' or navigate to hide this message.)
