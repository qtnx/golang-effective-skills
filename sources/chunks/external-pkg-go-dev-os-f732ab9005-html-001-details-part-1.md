---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/os"
source_path: "sources/raw/external/pkg-go-dev-os-f732ab9005.html"
license_ref: ""
---

os package - os - Go Packages
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
   Rendered for <https://go.dev/about#build-context>  linux/amd64 windows/amd64 darwin/amd64 js/wasm

Package os provides a platform-independent interface to operating system functionality. The design is Unix-like, although the error handling is Go-like; failing calls return values of type error rather than error numbers. Often, more information is available within the error. For example, if a call that takes a file name fails, such as Open or Stat, the error will include the failing file name when printed and will be of type *PathError, which may be unpacked for more information.

The os interface is intended to be uniform across all operating systems. Features not generally available appear in the system-specific package syscall.

Here is a simple example, opening a file and reading some of it.

```go
file, err := os.Open("file.go") // For read access.
if err != nil {
	log.Fatal(err)
}

```

If the open fails, the error string will be self-explanatory, like

```go
open file.go: no such file or directory

```

The file's data can then be read into a slice of bytes. Read and Write take their byte counts from the length of the argument slice.

```go
data := make([]byte, 100)
count, err := file.Read(data)
if err != nil {
	log.Fatal(err)
}
fmt.Printf("read %d bytes: %q\n", count, data[:count])

```

#### Concurrency ¶

The methods of File correspond to file system operations. All are safe for concurrent use. The maximum number of concurrent operations on a File may be limited by the OS or the system. The number should be high, but exceeding it may degrade performance or cause other issues.

- Constants
- Variables
-  func Chdir(dir string) error
-  func Chmod(name string, mode FileMode) error
-  func Chown(name string, uid, gid int) error
-  func Chtimes(name string, atime time.Time, mtime time.Time) error
-  func Clearenv()
-  func CopyFS(dir string, fsys fs.FS) error
-  func DirFS(dir string) fs.FS
-  func Environ() []string
-  func Executable() (string, error)
-  func Exit(code int)
-  func Expand(s string, mapping func(string) string) string
-  func ExpandEnv(s string) string
-  func Getegid() int
-  func Getenv(key string) string
-  func Geteuid() int
-  func Getgid() int
-  func Getgroups() ([]int, error)
-  func Getpagesize() int
-  func Getpid() int
-  func Getppid() int
-  func Getuid() int
-  func Getwd() (dir string, err error)
-  func Hostname() (name string, err error)
-  func IsExist(err error) bool
-  func IsNotExist(err error) bool
-  func IsPathSeparator(c uint8) bool
-  func IsPermission(err error) bool
-  func IsTimeout(err error) bool
-  func Lchown(name string, uid, gid int) error
-  func Link(oldname, newname string) error
-  func LookupEnv(key string) (string, bool)
-  func Mkdir(name string, perm FileMode) error
-  func MkdirAll(path string, perm FileMode) error
-  func MkdirTemp(dir, pattern string) (string, error)
-  func NewSyscallError(syscall string, err error) error
-  func Pipe() (r *File, w *File, err error)
-  func ReadFile(name string) ([]byte, error)
-  func Readlink(name string) (string, error)
-  func Remove(name string) error
-  func RemoveAll(path string) error
-  func Rename(oldpath, newpath string) error
-  func SameFile(fi1, fi2 FileInfo) bool
-  func Setenv(key, value string) error
-  func Symlink(oldname, newname string) error
-  func TempDir() string
-  func Truncate(name string, size int64) error
-  func Unsetenv(key string) error
-  func UserCacheDir() (string, error)
-  func UserConfigDir() (string, error)
-  func UserHomeDir() (string, error)
-  func WriteFile(name string, data []byte, perm FileMode) error
-  type DirEntry
-
-  func ReadDir(name string) ([]DirEntry, error)

-  type File
-
-  func Create(name string) (*File, error)
-  func CreateTemp(dir, pattern string) (*File, error)
-  func NewFile(fd uintptr, name string) *File
-  func Open(name string) (*File, error)
-  func OpenFile(name string, flag int, perm FileMode) (*File, error)
-  func OpenInRoot(dir, name string) (*File, error)

-
-  func (f *File) Chdir() error
-  func (f *File) Chmod(mode FileMode) error
-  func (f *File) Chown(uid, gid int) error
-  func (f *File) Close() error
-  func (f *File) Fd() uintptr
-  func (f *File) Name() string
-  func (f *File) Read(b []byte) (n int, err error)
-  func (f *File) ReadAt(b []byte, off int64) (n int, err error)
-  func (f *File) ReadDir(n int) ([]DirEntry, error)
-  func (f *File) ReadFrom(r io.Reader) (n int64, err error)
-  func (f *File) Readdir(n int) ([]FileInfo, error)
-  func (f *File) Readdirnames(n int) (names []string, err error)
-  func (f *File) Seek(offset int64, whence int) (ret int64, err error)
-  func (f *File) SetDeadline(t time.Time) error
-  func (f *File) SetReadDeadline(t time.Time) error
-  func (f *File) SetWriteDeadline(t time.Time) error
-  func (f *File) Stat() (FileInfo, error)
-  func (f *File) Sync() error
-  func (f *File) SyscallConn() (syscall.RawConn, error)
-  func (f *File) Truncate(size int64) error
-  func (f *File) Write(b []byte) (n int, err error)
-  func (f *File) WriteAt(b []byte, off int64) (n int, err error)
-  func (f *File) WriteString(s string) (n int, err error)
-  func (f *File) WriteTo(w io.Writer) (n int64, err error)

-  type FileInfo
-
-  func Lstat(name string) (FileInfo, error)
-  func Stat(name string) (FileInfo, error)

-  type FileMode
-  type LinkError
-
-  func (e *LinkError) Error() string
-  func (e *LinkError) Unwrap() error

-  type PathError
-  type ProcAttr
-  type Process
-
-  func FindProcess(pid int) (*Process, error)
-  func StartProcess(name string, argv []string, attr *ProcAttr) (*Process, error)

-
-  func (p *Process) Kill() error
-  func (p *Process) Release() error
-  func (p *Process) Signal(sig Signal) error
-  func (p *Process) Wait() (*ProcessState, error)
-  func (p *Process) WithHandle(f func(handle uintptr)) error

-  type ProcessState
-
-  func (p *ProcessState) ExitCode() int
-  func (p *ProcessState) Exited() bool
-  func (p *ProcessState) Pid() int
-  func (p *ProcessState) String() string
-  func (p *ProcessState) Success() bool
-  func (p *ProcessState) Sys() any
-  func (p *ProcessState) SysUsage() any
-  func (p *ProcessState) SystemTime() time.Duration
-  func (p *ProcessState) UserTime() time.Duration

-  type Root
-
-  func OpenRoot(name string) (*Root, error)

-
-  func (r *Root) Chmod(name string, mode FileMode) error
-  func (r *Root) Chown(name string, uid, gid int) error
-  func (r *Root) Chtimes(name string, atime time.Time, mtime time.Time) error
-  func (r *Root) Close() error
-  func (r *Root) Create(name string) (*File, error)
-  func (r *Root) FS() fs.FS
-  func (r *Root) Lchown(name string, uid, gid int) error
-  func (r *Root) Link(oldname, newname string) error
-  func (r *Root) Lstat(name string) (FileInfo, error)
-  func (r *Root) Mkdir(name string, perm FileMode) error
-  func (r *Root) MkdirAll(name string, perm FileMode) error
-  func (r *Root) Name() string
-  func (r *Root) Open(name string) (*File, error)
-  func (r *Root) OpenFile(name string, flag int, perm FileMode) (*File, error)
-  func (r *Root) OpenRoot(name string) (*Root, error)
-  func (r *Root) ReadFile(name string) ([]byte, error)
-  func (r *Root) Readlink(name string) (string, error)
-  func (r *Root) Remove(name string) error
-  func (r *Root) RemoveAll(name string) error
-  func (r *Root) Rename(oldname, newname string) error
-  func (r *Root) Stat(name string) (FileInfo, error)
-  func (r *Root) Symlink(oldname, newname string) error
-  func (r *Root) WriteFile(name string, data []byte, perm FileMode) error

-  type Signal
-  type SyscallError
-
-  func (e *SyscallError) Error() string
-  func (e *SyscallError) Timeout() bool
-  func (e *SyscallError) Unwrap() error

- Chmod
- Chtimes
- CreateTemp
- CreateTemp (Suffix)
- Expand
- ExpandEnv
- FileMode
- Getenv
- LookupEnv
- Mkdir
- MkdirAll
- MkdirTemp
- MkdirTemp (Suffix)
- OpenFile
- OpenFile (Append)
- ReadDir
- ReadFile
- Readlink
- Unsetenv
- UserCacheDir
- UserConfigDir
- WriteFile

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/os/file.go;l=79>
```go
const (
	// Exactly one of O_RDONLY, O_WRONLY, or O_RDWR must be specified.
	O_RDONLY int = syscall.O_RDONLY // open the file read-only.
	O_WRONLY int = syscall.O_WRONLY // open the file write-only.
	O_RDWR   int = syscall.O_RDWR   // open the file read-write.
	// The remaining values may be or'ed in to control behavior.
	O_APPEND int = syscall.O_APPEND // append data to the file when writing.
	O_CREATE int = syscall.O_CREAT  // create a new file if none exists.
	O_EXCL   int = syscall.O_EXCL   // used with O_CREATE, file must not exist.
	O_SYNC   int = syscall.O_SYNC   // open for synchronous I/O.
	O_TRUNC  int = syscall.O_TRUNC  // truncate regular writable file when opened.
)
```

Flags to OpenFile wrapping those of the underlying system. Not all flags may be implemented on a given system.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/os/file.go;l=95>
```go
const (
	SEEK_SET int = 0 // seek relative to the origin of the file
	SEEK_CUR int = 1 // seek relative to the current offset
	SEEK_END int = 2 // seek relative to the end
)
```

Seek whence values.

Deprecated: Use io.SeekStart, io.SeekCurrent, and io.SeekEnd.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/os/path_unix.go;l=9>
```go
const (
	PathSeparator     = '/' // OS-specific path separator
	PathListSeparator = ':' // OS-specific path list separator
)
```
