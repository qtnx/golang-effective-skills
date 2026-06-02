---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/io/fs"
source_path: "sources/raw/external/pkg-go-dev-io-fs-c79b887093.html"
license_ref: ""
---

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
