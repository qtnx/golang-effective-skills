goimports command - golang.org/x/tools/cmd/goimports - Go Packages

## Details

-     Valid go.mod <https://cs.opensource.google/go/x/tools/+/v0.45.0:/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/x/tools  <https://cs.opensource.google/go/x/tools>

## Links

-    Report a Vulnerability  <https://go.dev/security/policy>
-    Open Source Insights  <https://deps.dev/go/golang.org%2Fx%2Ftools/v0.45.0>
-    Code Wiki

##   Documentation ¶

Command goimports updates your Go import lines, adding missing ones and removing unreferenced ones.

```go
$ go install golang.org/x/tools/cmd/goimports@latest

```

In addition to fixing imports, goimports also formats your code in the same style as gofmt so it can be used as a replacement for your editor's gofmt-on-save hook.

For emacs, make sure you have the latest go-mode.el:

```go
https://github.com/dominikh/go-mode.el

```

Then in your .emacs file:

```go
(setq gofmt-command "goimports")
(add-hook 'before-save-hook 'gofmt-before-save)

```

For vim, set "gofmt_command" to "goimports":

```go
https://golang.org/change/39c724dd7f252
https://golang.org/wiki/IDEsAndTextEditorPlugins
etc

```

For GoSublime, follow the steps described here:

```go
http://michaelwhatcott.com/gosublime-goimports/

```

For other editors, you probably know what to do.

To exclude directories in your $GOPATH from being scanned for Go files, goimports respects a configuration file at $GOPATH/src/.goimportsignore which may contain blank lines, comment lines (beginning with '#'), or lines naming a directory relative to the configuration file to ignore when scanning. No globbing or regex patterns are allowed. Use the "-v" verbose flag to verify it's working and see what goimports is doing.

File bugs or feature requests at:

```go
https://golang.org/issues/new?title=x/tools/cmd/goimports:+

```

Happy hacking!

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/x/tools/+/v0.45.0:cmd/goimports>

- doc.go <https://cs.opensource.google/go/x/tools/+/v0.45.0:cmd/goimports/doc.go>
- goimports.go <https://cs.opensource.google/go/x/tools/+/v0.45.0:cmd/goimports/goimports.go>
- goimports_gc.go <https://cs.opensource.google/go/x/tools/+/v0.45.0:cmd/goimports/goimports_gc.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
