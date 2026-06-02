---
source_name: "External Linked Documentation"
source_url: "https://go.dev/talks/2014/organizeio.slide"
source_path: "sources/raw/external/go-dev-talks-2014-organizeio-slide-f62aaae46e.html"
license_ref: ""
---

# Organizing Go code

## Code organization
 8
### Introducing workspaces

 Your Go code is kept in a _workspace_.

 A workspace contains _many_ source repositories (git, hg).

 The Go tool understands the layout of a workspace.
 You don't need a `Makefile`. The file layout is everything.

 Change the file layout, change the build.

```go
$GOPATH/
    src/
        github.com/user/repo/
            mypkg/
                mysrc1.go
                mysrc2.go
            cmd/mycmd/
                main.go
    bin/
        mycmd
```

 9
### Let's make a workspace

```go
mkdir /tmp/gows
GOPATH=/tmp/gows
```

 The `GOPATH` environment variable tells the Go tool where your workspace is located.

```go
go get github.com/dsymonds/fixhub/cmd/fixhub
```

 The `go` `get` command fetches source repositories from the internet and places them in your workspace.

 Package paths matter to the Go tool. Using "github.com/..."
 means the tool knows how to fetch your repository.

```go
go install github.com/dsymonds/fixhub/cmd/fixhub
```

 The go install command builds a binary and places it in `$GOPATH/bin/fixhub`.
 10
### Our workspace

```go
$GOPATH/
    bin/fixhub                              # installed binary
    pkg/darwin_amd64/                       # compiled archives
        code.google.com/p/goauth2/oauth.a
        github.com/...
    src/                                    # source repositories
        code.google.com/p/goauth2/
            .hg
            oauth                           # used by package go-github
            ...
        github.com/
            golang/lint/...                 # used by package fixhub
                .git
            google/go-github/...            # used by package fixhub
                .git
            dsymonds/fixhub/
                .git
                client.go
                cmd/fixhub/fixhub.go        # package main
```

 `go` `get` fetched many repositories.
 `go` `install` built a binary out of them.
 11
### Why prescribe file layout?

 Using file layout for builds means less configuration.
 In fact, it means no configuration.
 No `Makefile`, no `build.xml`.

 Less time configuring means more time programming.

 Everyone in the community uses the same layout.
 This makes it easier to share code.

 The Go tool helps build the Go community.
 12
### Where's your workspace?

 It is possible to have multiple workspaces, but most people just use one.

 So where do you point your `GOPATH`? A common preference:

 This puts `src`, `bin`, and `pkg` directories in your home directory.

 (Convenient, because `$HOME/bin` is probably already in your `PATH`.)
 13
### Working with workspaces

 Unix eschews typing:

```go
CDPATH=$GOPATH/src/github.com:$GOPATH/src/code.google.com/p

$ cd dsymonds/fixhub
/tmp/gows/src/github.com/dsymonds/fixhub
$ cd goauth2
/tmp/gows/src/code.google.com/p/goauth2
$
```

 A shell function for your `~/.profile`:

```go
gocd () { cd `go list -f '{{.Dir}}' $1` }
```

 This lets you move around using the Go tool's path names:

```go
$ gocd .../lint
/tmp/gows/src/github.com/golang/lint
$
```

 14
### The Go tool's many talents

```go
$ go help
Go is a tool for managing Go source code.

Usage:

    go command [arguments]

The commands are:
```

 Worth exploring! Some highlights:

```go
build       compile packages and dependencies
get         download and install packages and dependencies
install     compile and install packages and dependencies
test        test packages
```

 There are more useful subcommands. Check out `vet` and `fmt`.
 15
