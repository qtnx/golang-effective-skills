---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/os"
source_path: "sources/raw/external/pkg-go-dev-os-f732ab9005.html"
license_ref: ""
---

Chtimes changes the access and modification times of the named file in the root. See Chtimes for more details.

```go
func (r *Root) Close() error
```

Close closes the Root. After Close is called, methods on Root return errors.

```go
func (r *Root) Create(name string) (*File, error)
```

Create creates or truncates the named file in the root. See Create for more details.

```go
func (r *Root) FS() fs.FS
```

FS returns a file system (an fs.FS) for the tree of files in the root.

The result implements io/fs.StatFS, io/fs.ReadFileFS, io/fs.ReadDirFS, and io/fs.ReadLinkFS.

```go
func (r *Root) Lchown(name string, uid, gid int) error
```

Lchown changes the numeric uid and gid of the named file in the root. See Lchown for more details.

```go
func (r *Root) Link(oldname, newname string) error
```

Link creates newname as a hard link to the oldname file. Both paths are relative to the root. See Link for more details.

If oldname is a symbolic link, Link creates new link to oldname and not its target. This behavior may differ from that of Link on some platforms.

When GOOS=js, Link returns an error if oldname is a symbolic link.

```go
func (r *Root) Lstat(name string) (FileInfo, error)
```

Lstat returns a FileInfo describing the named file in the root. If the file is a symbolic link, the returned FileInfo describes the symbolic link. See Lstat for more details.

```go
func (r *Root) Mkdir(name string, perm FileMode) error
```

Mkdir creates a new directory in the root with the specified name and permission bits (before umask). See Mkdir for more details.

If perm contains bits other than the nine least-significant bits (0o777), Mkdir returns an error.

```go
func (r *Root) MkdirAll(name string, perm FileMode) error
```

MkdirAll creates a new directory in the root, along with any necessary parents. See MkdirAll for more details.

If perm contains bits other than the nine least-significant bits (0o777), MkdirAll returns an error.

```go
func (r *Root) Name() string
```

Name returns the name of the directory presented to OpenRoot.

It is safe to call Name after [Close].

```go
func (r *Root) Open(name string) (*File, error)
```

Open opens the named file in the root for reading. See Open for more details.

```go
func (r *Root) OpenFile(name string, flag int, perm FileMode) (*File, error)
```

OpenFile opens the named file in the root. See OpenFile for more details.

If perm contains bits other than the nine least-significant bits (0o777), OpenFile returns an error.

```go
func (r *Root) OpenRoot(name string) (*Root, error)
```

OpenRoot opens the named directory in the root. If there is an error, it will be of type *PathError.

```go
func (r *Root) ReadFile(name string) ([]byte, error)
```

ReadFile reads the named file in the root and returns its contents. See ReadFile for more details.

```go
func (r *Root) Readlink(name string) (string, error)
```

Readlink returns the destination of the named symbolic link in the root. See Readlink for more details.

```go
func (r *Root) Remove(name string) error
```

Remove removes the named file or (empty) directory in the root. See Remove for more details.

```go
func (r *Root) RemoveAll(name string) error
```

RemoveAll removes the named file or directory and any children that it contains. See RemoveAll for more details.

```go
func (r *Root) Rename(oldname, newname string) error
```

Rename renames (moves) oldname to newname. Both paths are relative to the root. See Rename for more details.

```go
func (r *Root) Stat(name string) (FileInfo, error)
```

Stat returns a FileInfo describing the named file in the root. See Stat for more details.

```go
func (r *Root) Symlink(oldname, newname string) error
```

Symlink creates newname as a symbolic link to oldname. See Symlink for more details.

Symlink does not validate oldname, which may reference a location outside the root.

On Windows, a directory link is created if oldname references a directory within the root. Otherwise a file link is created.

```go
func (r *Root) WriteFile(name string, data []byte, perm FileMode) error
```

WriteFile writes data to the named file in the root, creating it if necessary. See WriteFile for more details.

```go
type Signal interface {
	String() string
	Signal() // to distinguish from other Stringers
}
```

A Signal represents an operating system signal. The usual underlying implementation is operating system-dependent: on Unix it is syscall.Signal.

```go
var (
	Interrupt Signal = syscall.SIGINT
	Kill      Signal = syscall.SIGKILL
)
```

The only signal values guaranteed to be present in the os package on all systems are os.Interrupt (send the process an interrupt) and os.Kill (force the process to exit). On Windows, sending os.Interrupt to a process with os.Process.Signal is not implemented; it will return an error instead of sending a signal.

```go
type SyscallError struct {
	Syscall string
	Err     error
}
```

SyscallError records an error from a specific system call.

```go
func (e *SyscallError) Error() string
```

```go
func (e *SyscallError) Timeout() bool
```

Timeout reports whether this error represents a timeout.

```go
func (e *SyscallError) Unwrap() error
```
