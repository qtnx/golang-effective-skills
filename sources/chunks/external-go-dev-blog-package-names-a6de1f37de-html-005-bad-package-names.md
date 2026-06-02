---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/package-names"
source_path: "sources/raw/external/go-dev-blog-package-names-a6de1f37de.html"
license_ref: ""
---

# The Go Blog

## Bad package names

Bad package names make code harder to navigate and maintain. Here are some guidelines for recognizing and fixing bad names.

**Avoid meaningless package names.** Packages named `util`, `common`, or `misc` provide clients with no sense of what the package contains. This makes it harder for clients to use the package and makes it harder for maintainers to keep the package focused. Over time, they accumulate dependencies that can make compilation significantly and unnecessarily slower, especially in large programs. And since such package names are generic, they are more likely to collide with other packages imported by client code, forcing clients to invent names to distinguish them.

**Break up generic packages.** To fix such packages, look for types and functions with common name elements and pull them into their own package. For example, if you have

```go
package util
func NewStringSet(...string) map[string]bool {...}
func SortStringSet(map[string]bool) []string {...}

```

then client code looks like

```go
set := util.NewStringSet("c", "a", "b")
fmt.Println(util.SortStringSet(set))

```

Pull these functions out of `util` into a new package, choosing a name that fits the contents:

```go
package stringset
func New(...string) map[string]bool {...}
func Sort(map[string]bool) []string {...}

```

then the client code becomes

```go
set := stringset.New("c", "a", "b")
fmt.Println(stringset.Sort(set))

```

Once you’ve made this change, it’s easier to see how to improve the new package:

```go
package stringset
type Set map[string]bool
func New(...string) Set {...}
func (s Set) Sort() []string {...}

```

which yields even simpler client code:

```go
set := stringset.New("c", "a", "b")
fmt.Println(set.Sort())

```

The name of the package is a critical piece of its design. Work to eliminate meaningless package names from your projects.

**Don’t use a single package for all your APIs.** Many well-intentioned programmers put all the interfaces exposed by their program into a single package named `api`, `types`, or `interfaces`, thinking it makes it easier to find the entry points to their code base. This is a mistake. Such packages suffer from the same problems as those named `util` or `common`, growing without bound, providing no guidance to users, accumulating dependencies, and colliding with other imports. Break them up, perhaps using directories to separate public packages from implementation.

**Avoid unnecessary package name collisions.** While packages in different directories may have the same name, packages that are frequently used together should have distinct names. This reduces confusion and the need for local renaming in client code. For the same reason, avoid using the same name as popular standard packages like `io` or `http`.

# The Go Blog

## Conclusion

Package names are central to good naming in Go programs. Take the time to choose good package names and organize your code well. This helps clients understand and use your packages and helps maintainers to grow them gracefully.

# The Go Blog

## Further reading

- Effective Go
- How to Write Go Code
- Organizing Go Code (2012 blog post)
- Organizing Go Code (2014 Google I/O talk)

 **Next article: **Testable Examples in Go
 **Previous article: **Errors are values
 **Blog Index**
