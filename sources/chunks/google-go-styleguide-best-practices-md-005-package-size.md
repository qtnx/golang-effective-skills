---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

# Go Style Best Practices

## Package size

If you're asking yourself how big your Go packages should be and whether to
place related types in the same package or split them into different ones, a
good place to start is the [Go blog post about package names][blog-pkg-names].
Despite the post title, it's not solely about naming. It contains some helpful
hints and cites several useful articles and talks.

Here are some other considerations and notes.

Users see [godoc] for the package in one page, and any methods exported by types
supplied by the package are grouped by their type. Godoc also group constructors
along with the types they return. If *client code* is likely to need two values
of different type to interact with each other, it may be convenient for the user
to have them in the same package.

Code within a package can access unexported identifiers in the package. If you
have a few related types whose *implementation* is tightly coupled, placing them
in the same package lets you achieve this coupling without polluting the public
API with these details. A good test for this coupling is to imagine a
hypothetical user of two packages, where the packages cover closely related
topics: if the user must import both packages in order to use either in any
meaningful way, combining them together is usually the right thing to do. The
standard library generally demonstrates this kind of scoping and layering well.

All of that being said, putting your entire project in a single package would
likely make that package too large. When something is conceptually distinct,
giving it its own small package can make it easier to use. The short name of the
package as known to clients together with the exported type name work together
to make a meaningful identifier: e.g. `bytes.Buffer`, `ring.New`. The
[Package Names blog post][blog-pkg-names] has more examples.

Go style is flexible about file size, because maintainers can move code within a
package from one file to another without affecting callers. But as a general
guideline: it is usually not a good idea to have a single file with many
thousands of lines in it, or having many tiny files. There is no "one type, one
file" convention as in some other languages. As a rule of thumb, files should be
focused enough that a maintainer can tell which file contains something, and the
files should be small enough that it will be easy to find once there. The
standard library often splits large packages to several source files, grouping
related code by file. The source for [package `bytes`] is a good example.
Packages with long package documentation may choose to dedicate one file called
`doc.go` that has the [package documentation](decisions#package-comments), a
package declaration, and nothing else, but this is not required.

Within the Google codebase and in projects using Bazel, directory layout for Go
code is different than it is in open source Go projects: you can have multiple
`go_library` targets in a single directory. A good reason to give each package
its own directory is if you expect to open source your project in the future.

A few non-canonical reference examples to help demonstrate these ideas in
action:

*   small packages that contain one cohesive idea that warrant nothing more
    being added nor nothing being removed:

    *   [package `csv`][package `csv`]: CSV data encoding and decoding with
        responsibility split respectively between [reader.go] and [writer.go].
    *   [package `expvar`][package `expvar`]: whitebox program telemetry all
        contained in [expvar.go].

*   moderately sized packages that contain one large domain and its multiple
    responsibilities together:

    *   [package `flag`][package `flag`]: command line flag management all
        contained in [flag.go].

*   large packages that divide several closely related domains across several
    files:

    *   [package `http`][package `http`]: the core of HTTP:
        [client.go][http-client], support for HTTP clients;
        [server.go][http-client], support for HTTP servers; [cookie.go], cookie
        management.
    *   [package `os`][package `os`]: cross-platform operating system
        abstractions: [exec.go], subprocess management; [file.go], file
        management; [tempfile.go], temporary files.

See also:

*   [Test double packages](#naming-doubles)
*   [Organizing Go Code (Blog Post)]
*   [Organizing Go Code (Presentation)]

[blog-pkg-names]: https://go.dev/blog/package-names
[package `bytes`]: https://go.dev/src/bytes/
[Organizing Go Code (Blog Post)]: https://go.dev/blog/organizing-go-code
[Organizing Go Code (Presentation)]: https://go.dev/talks/2014/organizeio.slide
[package `csv`]: https://pkg.go.dev/encoding/csv
[reader.go]: https://go.googlesource.com/go/+/refs/heads/master/src/encoding/csv/reader.go
[writer.go]: https://go.googlesource.com/go/+/refs/heads/master/src/encoding/csv/writer.go
[package `expvar`]: https://pkg.go.dev/expvar
[expvar.go]: https://go.googlesource.com/go/+/refs/heads/master/src/expvar/expvar.go
[package `flag`]: https://pkg.go.dev/flag
[flag.go]: https://go.googlesource.com/go/+/refs/heads/master/src/flag/flag.go
[godoc]: https://pkg.go.dev/
[package `http`]: https://pkg.go.dev/net/http
[http-client]: https://go.googlesource.com/go/+/refs/heads/master/src/net/http/client.go
[http-server]: https://go.googlesource.com/go/+/refs/heads/master/src/net/http/server.go
[cookie.go]: https://go.googlesource.com/go/+/refs/heads/master/src/net/http/cookie.go
[package `os`]: https://pkg.go.dev/os
[exec.go]: https://go.googlesource.com/go/+/refs/heads/master/src/os/exec.go
[file.go]: https://go.googlesource.com/go/+/refs/heads/master/src/os/file.go
[tempfile.go]: https://go.googlesource.com/go/+/refs/heads/master/src/os/tempfile.go

<a id="imports"></a>
