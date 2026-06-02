---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Package size

If you’re asking yourself how big your Go packages should be and whether to place related types in the same package or split them into different ones, a good place to start is the Go blog post about package names. Despite the post title, it’s not solely about naming. It contains some helpful hints and cites several useful articles and talks.

Here are some other considerations and notes.

Users see godoc for the package in one page, and any methods exported by types supplied by the package are grouped by their type. Godoc also group constructors along with the types they return. If _client code_ is likely to need two values of different type to interact with each other, it may be convenient for the user to have them in the same package.

Code within a package can access unexported identifiers in the package. If you have a few related types whose _implementation_ is tightly coupled, placing them in the same package lets you achieve this coupling without polluting the public API with these details. A good test for this coupling is to imagine a hypothetical user of two packages, where the packages cover closely related topics: if the user must import both packages in order to use either in any meaningful way, combining them together is usually the right thing to do. The standard library generally demonstrates this kind of scoping and layering well.

All of that being said, putting your entire project in a single package would likely make that package too large. When something is conceptually distinct, giving it its own small package can make it easier to use. The short name of the package as known to clients together with the exported type name work together to make a meaningful identifier: e.g. `bytes.Buffer`, `ring.New`. The Package Names blog post has more examples.

Go style is flexible about file size, because maintainers can move code within a package from one file to another without affecting callers. But as a general guideline: it is usually not a good idea to have a single file with many thousands of lines in it, or having many tiny files. There is no “one type, one file” convention as in some other languages. As a rule of thumb, files should be focused enough that a maintainer can tell which file contains something, and the files should be small enough that it will be easy to find once there. The standard library often splits large packages to several source files, grouping related code by file. The source for package `bytes` is a good example. Packages with long package documentation may choose to dedicate one file called `doc.go` that has the package documentation, a package declaration, and nothing else, but this is not required.

Within the Google codebase and in projects using Bazel, directory layout for Go code is different than it is in open source Go projects: you can have multiple `go_library` targets in a single directory. A good reason to give each package its own directory is if you expect to open source your project in the future.

A few non-canonical reference examples to help demonstrate these ideas in action:

-
small packages that contain one cohesive idea that warrant nothing more being added nor nothing being removed:

- package `csv`: CSV data encoding and decoding with responsibility split respectively between reader.go and writer.go.
- package `expvar`: whitebox program telemetry all contained in expvar.go.

-
moderately sized packages that contain one large domain and its multiple responsibilities together:

- package `flag`: command line flag management all contained in flag.go.

-
large packages that divide several closely related domains across several files:

- package `http`: the core of HTTP: client.go, support for HTTP clients; server.go, support for HTTP servers; cookie.go, cookie management.
- package `os`: cross-platform operating system abstractions: exec.go, subprocess management; file.go, file management; tempfile.go, temporary files.

See also:

- Test double packages
- Organizing Go Code (Blog Post)
- Organizing Go Code (Presentation)
