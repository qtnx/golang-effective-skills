fstest package - testing/fstest - Go Packages

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

Package fstest implements support for testing implementations and users of file systems.

-  func TestFS(fsys fs.FS, expected ...string) error
-  type MapFS
-
-  func (fsys MapFS) Glob(pattern string) ([]string, error)
-  func (fsys MapFS) Lstat(name string) (fs.FileInfo, error)
-  func (fsys MapFS) Open(name string) (fs.File, error)
-  func (fsys MapFS) ReadDir(name string) ([]fs.DirEntry, error)
-  func (fsys MapFS) ReadFile(name string) ([]byte, error)
-  func (fsys MapFS) ReadLink(name string) (string, error)
-  func (fsys MapFS) Stat(name string) (fs.FileInfo, error)
-  func (fsys MapFS) Sub(dir string) (fs.FS, error)

-  type MapFile

This section is empty.

This section is empty.

```go
func TestFS(fsys fs.FS, expected ...string) error
```

TestFS tests a file system implementation. It walks the entire tree of files in fsys, opening and checking that each file behaves correctly. Symbolic links are not followed, but their Lstat values are checked if the file system implements fs.ReadLinkFS. It also checks that the file system contains at least the expected files. As a special case, if no expected files are listed, fsys must be empty. Otherwise, fsys must contain at least the listed files; it can also contain others. The contents of fsys must not change concurrently with TestFS.

If TestFS finds any misbehaviors, it returns either the first error or a list of errors. Use errors.Is or errors.AsType to inspect.

Typical usage inside a test is:

```go
if err := fstest.TestFS(myFS, "file/that/should/be/present"); err != nil {
	t.Fatal(err)
}

```

```go
type MapFS map[string]*MapFile
```

A MapFS is a simple in-memory file system for use in tests, represented as a map from path names (arguments to Open) to information about the files, directories, or symbolic links they represent.

The map need not include parent directories for files contained in the map; those will be synthesized if needed. But a directory can still be included by setting the [MapFile.Mode]'s fs.ModeDir bit; this may be necessary for detailed control over the directory's fs.FileInfo or to create an empty directory.

File system operations read directly from the map, so that the file system can be changed by editing the map as needed. An implication is that file system operations must not run concurrently with changes to the map, which would be a race. Another implication is that opening or reading a directory requires iterating over the entire map, so a MapFS should typically be used with not more than a few hundred entries or directory reads.

```go
func (fsys MapFS) Glob(pattern string) ([]string, error)
```

```go
func (fsys MapFS) Lstat(name string) (fs.FileInfo, error)
```

Lstat returns a FileInfo describing the named file. If the file is a symbolic link, the returned FileInfo describes the symbolic link. Lstat makes no attempt to follow the link.

```go
func (fsys MapFS) Open(name string) (fs.File, error)
```

Open opens the named file after following any symbolic links.

```go
func (fsys MapFS) ReadDir(name string) ([]fs.DirEntry, error)
```

```go
func (fsys MapFS) ReadFile(name string) ([]byte, error)
```

```go
func (fsys MapFS) ReadLink(name string) (string, error)
```

ReadLink returns the destination of the named symbolic link.

```go
func (fsys MapFS) Stat(name string) (fs.FileInfo, error)
```

```go
func (fsys MapFS) Sub(dir string) (fs.FS, error)
```

```go
type MapFile struct {
	Data    []byte      // file content or symlink destination
	Mode    fs.FileMode // fs.FileInfo.Mode
	ModTime time.Time   // fs.FileInfo.ModTime
	Sys     any         // fs.FileInfo.Sys
}
```

A MapFile describes a single file in a MapFS.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/testing/fstest>

- mapfs.go <https://cs.opensource.google/go/go/+/go1.26.3:src/testing/fstest/mapfs.go>
- testfs.go <https://cs.opensource.google/go/go/+/go1.26.3:src/testing/fstest/testfs.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
