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

## Links

-    Report a Vulnerability  <https://go.dev/security/policy>

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

An FS provides access to a hierarchical file system.

The FS interface is the minimum implementation required of the file system. A file system may implement additional interfaces, such as ReadFileFS, to provide additional or optimized functionality.

testing/fstest.TestFS may be used to test implementations of an FS for correctness.

```go
func Sub(fsys FS, dir string) (FS, error)
```

Sub returns an FS corresponding to the subtree rooted at fsys's dir.

If dir is ".", Sub returns fsys unchanged. Otherwise, if fs implements SubFS, Sub returns fsys.Sub(dir). Otherwise, Sub returns a new FS implementation sub that, in effect, implements sub.Open(name) as fsys.Open(path.Join(dir, name)). The implementation also translates calls to ReadDir, ReadFile, ReadLink, Lstat, and Glob appropriately.

Note that Sub(os.DirFS("/"), "prefix") is equivalent to os.DirFS("/prefix") and that neither of them guarantees to avoid operating system accesses outside "/prefix", because the implementation of os.DirFS does not check for symbolic links inside "/prefix" that point to other directories. That is, os.DirFS is not a general substitute for a chroot-style security mechanism, and Sub does not change that fact.

```go
type File interface {
	Stat() (FileInfo, error)
	Read([]byte) (int, error)
	Close() error
}
```

A File provides access to a single file. The File interface is the minimum implementation required of the file. Directory files should also implement ReadDirFile. A file may implement io.ReaderAt or io.Seeker as optimizations.

```go
type FileInfo interface {
	Name() string       // base name of the file
	Size() int64        // length in bytes for regular files; system-dependent for others
	Mode() FileMode     // file mode bits
	ModTime() time.Time // modification time
	IsDir() bool        // abbreviation for Mode().IsDir()
	Sys() any           // underlying data source (can return nil)
}
```

A FileInfo describes a file and is returned by Stat.

```go
func Lstat(fsys FS, name string) (FileInfo, error)
```

Lstat returns a FileInfo describing the named file. If the file is a symbolic link, the returned FileInfo describes the symbolic link. Lstat makes no attempt to follow the link.

If fsys does not implement ReadLinkFS, then Lstat is identical to Stat.

```go
func Stat(fsys FS, name string) (FileInfo, error)
```

Stat returns a FileInfo describing the named file from the file system.

If fs implements StatFS, Stat calls fs.Stat. Otherwise, Stat opens the File to stat it.

```go
type FileMode uint32
```

A FileMode represents a file's mode and permission bits. The bits have the same definition on all systems, so that information about files can be moved from one system to another portably. Not all bits apply to all systems. The only required bit is ModeDir for directories.

```go
const (
	// The single letters are the abbreviations
	// used by the String method's formatting.
	ModeDir        FileMode = 1 << (32 - 1 - iota) // d: is a directory
	ModeAppend                                     // a: append-only
	ModeExclusive                                  // l: exclusive use
	ModeTemporary                                  // T: temporary file; Plan 9 only
	ModeSymlink                                    // L: symbolic link
	ModeDevice                                     // D: device file
	ModeNamedPipe                                  // p: named pipe (FIFO)
	ModeSocket                                     // S: Unix domain socket
	ModeSetuid                                     // u: setuid
	ModeSetgid                                     // g: setgid
	ModeCharDevice                                 // c: Unix character device, when ModeDevice is set
	ModeSticky                                     // t: sticky
	ModeIrregular                                  // ?: non-regular file; nothing else is known about this file

	// Mask for the type bits. For regular files, none will be set.
	ModeType = ModeDir | ModeSymlink | ModeNamedPipe | ModeSocket | ModeDevice | ModeCharDevice | ModeIrregular

	ModePerm FileMode = 0777 // Unix permission bits
)
```

The defined file mode bits are the most significant bits of the FileMode. The nine least-significant bits are the standard Unix rwxrwxrwx permissions. The values of these bits should be considered part of the public API and may be used in wire protocols or disk representations: they must not be changed, although new bits might be added.

```go
func (m FileMode) IsDir() bool
```

IsDir reports whether m describes a directory. That is, it tests for the ModeDir bit being set in m.

```go
func (m FileMode) IsRegular() bool
```

IsRegular reports whether m describes a regular file. That is, it tests that no mode type bits are set.

```go
func (m FileMode) Perm() FileMode
```

Perm returns the Unix permission bits in m (m & ModePerm).

```go
func (m FileMode) String() string
```

```go
func (m FileMode) Type() FileMode
```

Type returns type bits in m (m & ModeType).

```go
type GlobFS interface {
	FS

	// Glob returns the names of all files matching pattern,
	// providing an implementation of the top-level
	// Glob function.
	Glob(pattern string) ([]string, error)
}
```

A GlobFS is a file system with a Glob method.

```go
type PathError struct {
	Op   string
	Path string
	Err  error
}
```

PathError records an error and the operation and file path that caused it.

```go
func (e *PathError) Error() string
```

```go
func (e *PathError) Timeout() bool
```

Timeout reports whether this error represents a timeout.

```go
func (e *PathError) Unwrap() error
```

```go
type ReadDirFS interface {
	FS

	// ReadDir reads the named directory
	// and returns a list of directory entries sorted by filename.
	ReadDir(name string) ([]DirEntry, error)
}
```

ReadDirFS is the interface implemented by a file system that provides an optimized implementation of ReadDir.

```go
type ReadDirFile interface {
	File

	// ReadDir reads the contents of the directory and returns
	// a slice of up to n DirEntry values in directory order.
	// Subsequent calls on the same file will yield further DirEntry values.
	//
	// If n > 0, ReadDir returns at most n DirEntry structures.
	// In this case, if ReadDir returns an empty slice, it will return
	// a non-nil error explaining why.
	// At the end of a directory, the error is io.EOF.
	// (ReadDir must return io.EOF itself, not an error wrapping io.EOF.)
	//
	// If n <= 0, ReadDir returns all remaining DirEntry values from the directory
	// in a single slice. In this case, if ReadDir succeeds (reads all the way
	// to the end of the directory), it returns the slice and a nil error.
	// If it encounters an error before the end of the directory,
	// ReadDir returns the DirEntry list read until that point and a non-nil error.
	ReadDir(n int) ([]DirEntry, error)
}
```

A ReadDirFile is a directory file whose entries can be read with the ReadDir method. Every directory file should implement this interface. (It is permissible for any file to implement this interface, but if so ReadDir should return an error for non-directories.)

```go
type ReadFileFS interface {
	FS

	// ReadFile reads the named file and returns its contents.
	// A successful call returns a nil error, not io.EOF.
	// (Because ReadFile reads the whole file, the expected EOF
	// from the final Read is not treated as an error to be reported.)
	//
	// The caller is permitted to modify the returned byte slice.
	// This method should return a copy of the underlying data.
	ReadFile(name string) ([]byte, error)
}
```

ReadFileFS is the interface implemented by a file system that provides an optimized implementation of ReadFile.

```go
type ReadLinkFS interface {
	FS

	// ReadLink returns the destination of the named symbolic link.
	// If there is an error, it should be of type [*PathError].
	ReadLink(name string) (string, error)

	// Lstat returns a [FileInfo] describing the named file.
	// If the file is a symbolic link, the returned [FileInfo] describes the symbolic link.
	// Lstat makes no attempt to follow the link.
	// If there is an error, it should be of type [*PathError].
	Lstat(name string) (FileInfo, error)
}
```

ReadLinkFS is the interface implemented by a file system that supports reading symbolic links.

```go
type StatFS interface {
	FS

	// Stat returns a FileInfo describing the file.
	// If there is an error, it should be of type *PathError.
	Stat(name string) (FileInfo, error)
}
```

A StatFS is a file system with a Stat method.

```go
type SubFS interface {
	FS

	// Sub returns an FS corresponding to the subtree rooted at dir.
	Sub(dir string) (FS, error)
}
```

A SubFS is a file system with a Sub method.

```go
type WalkDirFunc func(path string, d DirEntry, err error) error
```

WalkDirFunc is the type of the function called by WalkDir to visit each file or directory.

The path argument contains the argument to WalkDir as a prefix. That is, if WalkDir is called with root argument "dir" and finds a file named "a" in that directory, the walk function will be called with argument "dir/a".

The d argument is the DirEntry for the named path.

The error result returned by the function controls how WalkDir continues. If the function returns the special value SkipDir, WalkDir skips the current directory (path if d.IsDir() is true, otherwise path's parent directory). If the function returns the special value SkipAll, WalkDir skips all remaining files and directories. Otherwise, if the function returns a non-nil error, WalkDir stops entirely and returns that error.

The err argument reports an error related to path, signaling that WalkDir will not walk into that directory. The function can decide how to handle that error; as described earlier, returning the error will cause WalkDir to stop walking the entire tree.

WalkDir calls the function with a non-nil err argument in two cases.

First, if the initial Stat on the root directory fails, WalkDir calls the function with path set to root, d set to nil, and err set to the error from fs.Stat.

Second, if a directory's ReadDir method (see ReadDirFile) fails, WalkDir calls the function with path set to the directory's path, d set to an DirEntry describing the directory, and err set to the error from ReadDir. In this second case, the function is called twice with the path of the directory: the first call is before the directory read is attempted and has err set to nil, giving the function a chance to return SkipDir or SkipAll and avoid the ReadDir entirely. The second call is after a failed ReadDir and reports the error from ReadDir. (If ReadDir succeeds, there is no second call.)

The differences between WalkDirFunc compared to path/filepath.WalkFunc are:

- The second argument has type DirEntry instead of FileInfo.
- The function is called before reading a directory, to allow SkipDir or SkipAll to bypass the directory read entirely or skip all remaining files and directories respectively.
- If a directory read fails, the function is called a second time for that directory to report the error.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs>

- format.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/format.go>
- fs.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/fs.go>
- glob.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/glob.go>
- readdir.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/readdir.go>
- readfile.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/readfile.go>
- readlink.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/readlink.go>
- stat.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/stat.go>
- sub.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/sub.go>
- walk.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/walk.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
