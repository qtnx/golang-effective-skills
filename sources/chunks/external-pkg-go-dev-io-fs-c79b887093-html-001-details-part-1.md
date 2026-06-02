---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/io/fs"
source_path: "sources/raw/external/pkg-go-dev-io-fs-c79b887093.html"
license_ref: ""
---

fs package - io/fs - Go Packages
## Details

-     Valid go.mod <https://cs.opensource.google/go/go/+/go1.26.3:src/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/go  <https://cs.opensource.google/go/go>

##   Documentation ¶

Package fs defines basic interfaces to a file system. A file system can be provided by the host operating system but also by other packages.

#### Path Names ¶

The interfaces in this package all operate on the same path name syntax, regardless of the host operating system.

Path names are UTF-8-encoded, unrooted, slash-separated sequences of path elements, like “x/y/z”. Path names must not contain an element that is “.” or “..” or the empty string, except for the special case that the name "." may be used for the root directory. Paths must not start or end with a slash: “/x” and “x/” are invalid.

#### Testing ¶

See the testing/fstest package for support with testing implementations of file systems.

- Variables
-  func FormatDirEntry(dir DirEntry) string
-  func FormatFileInfo(info FileInfo) string
-  func Glob(fsys FS, pattern string) (matches []string, err error)
-  func ReadFile(fsys FS, name string) ([]byte, error)
-  func ReadLink(fsys FS, name string) (string, error)
-  func ValidPath(name string) bool
-  func WalkDir(fsys FS, root string, fn WalkDirFunc) error
-  type DirEntry
-
-  func FileInfoToDirEntry(info FileInfo) DirEntry
-  func ReadDir(fsys FS, name string) ([]DirEntry, error)

-  type FS
-
-  func Sub(fsys FS, dir string) (FS, error)

-  type File
-  type FileInfo
-
-  func Lstat(fsys FS, name string) (FileInfo, error)
-  func Stat(fsys FS, name string) (FileInfo, error)

-  type FileMode
-
-  func (m FileMode) IsDir() bool
-  func (m FileMode) IsRegular() bool
-  func (m FileMode) Perm() FileMode
-  func (m FileMode) String() string
-  func (m FileMode) Type() FileMode

-  type GlobFS
-  type PathError
-
-  func (e *PathError) Error() string
-  func (e *PathError) Timeout() bool
-  func (e *PathError) Unwrap() error

-  type ReadDirFS
-  type ReadDirFile
-  type ReadFileFS
-  type ReadLinkFS
-  type StatFS
-  type SubFS
-  type WalkDirFunc

- Glob
- ReadFile
- ValidPath
- WalkDir

This section is empty.

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/fs.go;l=153>
```go
var (
	ErrInvalid    = errInvalid()    // "invalid argument"
	ErrPermission = errPermission() // "permission denied"
	ErrExist      = errExist()      // "file already exists"
	ErrNotExist   = errNotExist()   // "file does not exist"
	ErrClosed     = errClosed()     // "file already closed"
)
```

Generic file system errors. Errors returned by file systems can be tested against these errors using errors.Is.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/walk.go;l=20>
```go

```

SkipAll is used as a return value from WalkDirFunc to indicate that all remaining files and directories are to be skipped. It is not returned as an error by any function.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/walk.go;l=15>
```go

```

SkipDir is used as a return value from WalkDirFunc to indicate that the directory named in the call is to be skipped. It is not returned as an error by any function.

```go
func FormatDirEntry(dir DirEntry) string
```

FormatDirEntry returns a formatted version of dir for human readability. Implementations of DirEntry can call this from a String method. The outputs for a directory named subdir and a file named hello.go are:

```go
d subdir/
- hello.go

```

```go
func FormatFileInfo(info FileInfo) string
```

FormatFileInfo returns a formatted version of info for human readability. Implementations of FileInfo can call this from a String method. The output for a file named "hello.go", 100 bytes, mode 0o644, created January 1, 1970 at noon is

```go
-rw-r--r-- 100 1970-01-01 12:00:00 hello.go

```

```go
func Glob(fsys FS, pattern string) (matches []string, err error)
```

Glob returns the names of all files matching pattern or nil if there is no matching file. The syntax of patterns is the same as in path.Match. The pattern may describe hierarchical names such as usr/*/bin/ed.

Glob ignores file system errors such as I/O errors reading directories. The only possible returned error is path.ErrBadPattern, reporting that the pattern is malformed.

If fs implements GlobFS, Glob calls fs.Glob. Otherwise, Glob uses ReadDir to traverse the directory tree and look for matches for the pattern.

```go

package main

import (
	"fmt"
	"io/fs"
	"log"
	"testing/fstest"
)

func main() {
	fsys := fstest.MapFS{
		"file.txt":        {},
		"file.go":         {},
		"dir/file.txt":    {},
		"dir/file.go":     {},
		"dir/subdir/x.go": {},
	}

patterns := []string{
		"*.txt",
		"*.go",
		"dir/*.go",
		"dir/*/x.go",
	}

for _, pattern := range patterns {
		matches, err := fs.Glob(fsys, pattern)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%q matches: %v\n", pattern, matches)
	}

}

```

```go
Output:
"*.txt" matches: [file.txt]
"*.go" matches: [file.go]
"dir/*.go" matches: [dir/file.go]
"dir/*/x.go" matches: [dir/subdir/x.go]

```

Share Format Run

```go
func ReadFile(fsys FS, name string) ([]byte, error)
```

ReadFile reads the named file from the file system fs and returns its contents. A successful call returns a nil error, not io.EOF. (Because ReadFile reads the whole file, the expected EOF from the final Read is not treated as an error to be reported.)

If fs implements ReadFileFS, ReadFile calls fs.ReadFile. Otherwise ReadFile calls fs.Open and uses Read and Close on the returned File.

```go

package main

import (
	"fmt"
	"io/fs"
	"log"
	"testing/fstest"
)

func main() {
	fsys := fstest.MapFS{
		"hello.txt": {
			Data: []byte("Hello, World!\n"),
		},
	}

data, err := fs.ReadFile(fsys, "hello.txt")
	if err != nil {
		log.Fatal(err)
	}

fmt.Print(string(data))

}

```

```go
Output:
Hello, World!

```

Share Format Run

```go
func ReadLink(fsys FS, name string) (string, error)
```

ReadLink returns the destination of the named symbolic link.

If fsys does not implement ReadLinkFS, then ReadLink returns an error.

```go
func ValidPath(name string) bool
```

ValidPath reports whether the given path name is valid for use in a call to Open.

Note that paths are slash-separated on all systems, even Windows. Paths containing other characters such as backslash and colon are accepted as valid, but those characters must never be interpreted by an FS implementation as path element separators. See the Path Names <https://pkg.go.dev/io/fs#hdr-Path_Names> section for more details.

```go

package main

import (
	"fmt"
	"io/fs"
)

func main() {
	paths := []string{
		".",
		"x",
		"x/y/z",
		"",
		"..",
		"/x",
		"x/",
		"x//y",
		"x/./y",
		"x/../y",
	}

for _, path := range paths {
		fmt.Printf("ValidPath(%q) = %t\n", path, fs.ValidPath(path))
	}

}

```

```go
Output:
ValidPath(".") = true
ValidPath("x") = true
ValidPath("x/y/z") = true
ValidPath("") = false
ValidPath("..") = false
ValidPath("/x") = false
ValidPath("x/") = false
ValidPath("x//y") = false
ValidPath("x/./y") = false
ValidPath("x/../y") = false

```

Share Format Run

```go
func WalkDir(fsys FS, root string, fn WalkDirFunc) error
```

WalkDir walks the file tree rooted at root, calling fn for each file or directory in the tree, including root.

All errors that arise visiting files and directories are filtered by fn: see the fs.WalkDirFunc documentation for details.

The files are walked in lexical order, which makes the output deterministic but requires WalkDir to read an entire directory into memory before proceeding to walk that directory.

WalkDir does not follow symbolic links found in directories, but if root itself is a symbolic link, its target will be walked.

```go

package main

import (
	"fmt"
	"io/fs"
	"log"
	"os"
)

func main() {
	root := "/usr/local/go/bin"
	fileSystem := os.DirFS(root)

fs.WalkDir(fileSystem, ".", func(path string, d fs.DirEntry, err error) error {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(path)
		return nil
	})
}

```

```go
Output:

```

Share Format Run

```go
type DirEntry interface {
	// Name returns the name of the file (or subdirectory) described by the entry.
	// This name is only the final element of the path (the base name), not the entire path.
	// For example, Name would return "hello.go" not "home/gopher/hello.go".
	Name() string

// IsDir reports whether the entry describes a directory.
	IsDir() bool

// Type returns the type bits for the entry.
	// The type bits are a subset of the usual FileMode bits, those returned by the FileMode.Type method.
	Type() FileMode

// Info returns the FileInfo for the file or subdirectory described by the entry.
	// The returned FileInfo may be from the time of the original directory read
	// or from the time of the call to Info. If the file has been removed or renamed
	// since the directory read, Info may return an error satisfying errors.Is(err, ErrNotExist).
	// If the entry denotes a symbolic link, Info reports the information about the link itself,
	// not the link's target.
	Info() (FileInfo, error)
}
```

A DirEntry is an entry read from a directory (using the ReadDir function or a ReadDirFile's ReadDir method).

```go
func FileInfoToDirEntry(info FileInfo) DirEntry
```

FileInfoToDirEntry returns a DirEntry that returns information from info. If info is nil, FileInfoToDirEntry returns nil.

```go
func ReadDir(fsys FS, name string) ([]DirEntry, error)
```

ReadDir reads the named directory and returns a list of directory entries sorted by filename.

If fs implements ReadDirFS, ReadDir calls fs.ReadDir. Otherwise ReadDir calls fs.Open and uses ReadDir and Close on the returned file.

```go
type FS interface {
	// Open opens the named file.
	// [File.Close] must be called to release any associated resources.
	//
	// When Open returns an error, it should be of type *PathError
	// with the Op field set to "open", the Path field set to name,
	// and the Err field describing the problem.
	//
	// Open should reject attempts to open names that do not satisfy
	// ValidPath(name), returning a *PathError with Err set to
	// ErrInvalid or ErrNotExist.
	Open(name string) (File, error)
}
```
