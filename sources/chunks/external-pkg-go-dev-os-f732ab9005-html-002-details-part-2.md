---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/os"
source_path: "sources/raw/external/pkg-go-dev-os-f732ab9005.html"
license_ref: ""
---

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/os/types.go;l=37>
```go
const (
	// The single letters are the abbreviations
	// used by the String method's formatting.
	ModeDir        = fs.ModeDir        // d: is a directory
	ModeAppend     = fs.ModeAppend     // a: append-only
	ModeExclusive  = fs.ModeExclusive  // l: exclusive use
	ModeTemporary  = fs.ModeTemporary  // T: temporary file; Plan 9 only
	ModeSymlink    = fs.ModeSymlink    // L: symbolic link
	ModeDevice     = fs.ModeDevice     // D: device file
	ModeNamedPipe  = fs.ModeNamedPipe  // p: named pipe (FIFO)
	ModeSocket     = fs.ModeSocket     // S: Unix domain socket
	ModeSetuid     = fs.ModeSetuid     // u: setuid
	ModeSetgid     = fs.ModeSetgid     // g: setgid
	ModeCharDevice = fs.ModeCharDevice // c: Unix character device, when ModeDevice is set
	ModeSticky     = fs.ModeSticky     // t: sticky
	ModeIrregular  = fs.ModeIrregular  // ?: non-regular file; nothing else is known about this file

// Mask for the type bits. For regular files, none will be set.
	ModeType = fs.ModeType

ModePerm = fs.ModePerm // Unix permission bits, 0o777
)
```

The defined file mode bits are the most significant bits of the FileMode. The nine least-significant bits are the standard Unix rwxrwxrwx permissions. The values of these bits should be considered part of the public API and may be used in wire protocols or disk representations: they must not be changed, although new bits might be added.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/os/file_unix.go;l=242>
```go
const DevNull = "/dev/null"
```

DevNull is the name of the operating system's “null device.” On Unix-like systems, it is "/dev/null"; on Windows, "NUL".

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/os/error.go;l=16>
```go
var (
	// ErrInvalid indicates an invalid argument.
	// Methods on File will return this error when the receiver is nil.
	ErrInvalid = fs.ErrInvalid // "invalid argument"

ErrPermission = fs.ErrPermission // "permission denied"
	ErrExist      = fs.ErrExist      // "file already exists"
	ErrNotExist   = fs.ErrNotExist   // "file does not exist"
	ErrClosed     = fs.ErrClosed     // "file already closed"

ErrNoDeadline       = errNoDeadline()       // "file type does not support deadline"
	ErrDeadlineExceeded = errDeadlineExceeded() // "i/o timeout"
)
```

Portable analogs of some common system call errors.

Errors returned from this package may be tested against these errors with errors.Is.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/os/exec.go;l=17>
```go
var (
	// ErrProcessDone indicates a [Process] has finished.
	ErrProcessDone = errors.New("os: process already finished")

// ErrNoHandle indicates a [Process] does not have a handle.
	ErrNoHandle = errors.New("os: process handle unavailable")
)
```

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/os/file.go;l=71>
```go
var (
	Stdin  = NewFile(uintptr(syscall.Stdin), "/dev/stdin")
	Stdout = NewFile(uintptr(syscall.Stdout), "/dev/stdout")
	Stderr = NewFile(uintptr(syscall.Stderr), "/dev/stderr")
)
```

Stdin, Stdout, and Stderr are open Files pointing to the standard input, standard output, and standard error file descriptors.

Note that the Go runtime writes to standard error for panics and crashes; closing Stderr may cause those messages to go elsewhere, perhaps to a file opened later.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/os/proc.go;l=16>
```go
var Args []string
```

Args hold the command-line arguments, starting with the program name.

```go
func Chdir(dir string) error
```

Chdir changes the current working directory to the named directory. If there is an error, it will be of type *PathError.

```go
func Chmod(name string, mode FileMode) error
```

Chmod changes the mode of the named file to mode. If the file is a symbolic link, it changes the mode of the link's target. If there is an error, it will be of type *PathError.

A different subset of the mode bits are used, depending on the operating system.

On Unix, the mode's permission bits, ModeSetuid, ModeSetgid, and ModeSticky are used.

On Windows, only the 0o200 bit (owner writable) of mode is used; it controls whether the file's read-only attribute is set or cleared. The other bits are currently unused. For compatibility with Go 1.12 and earlier, use a non-zero mode. Use mode 0o400 for a read-only file and 0o600 for a readable+writable file.

On Plan 9, the mode's permission bits, ModeAppend, ModeExclusive, and ModeTemporary are used.

```go

package main

import (
	"log"
	"os"
)

func main() {
	if err := os.Chmod("some-filename", 0644); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:

```

Share Format Run

```go
func Chown(name string, uid, gid int) error
```

Chown changes the numeric uid and gid of the named file. If the file is a symbolic link, it changes the uid and gid of the link's target. A uid or gid of -1 means to not change that value. If there is an error, it will be of type *PathError.

On Windows or Plan 9, Chown always returns the syscall.EWINDOWS or syscall.EPLAN9 error, wrapped in *PathError.

```go
func Chtimes(name string, atime time.Time, mtime time.Time) error
```

Chtimes changes the access and modification times of the named file, similar to the Unix utime() or utimes() functions. A zero time.Time value will leave the corresponding file time unchanged.

The underlying filesystem may truncate or round the values to a less precise time unit. If there is an error, it will be of type *PathError.

```go

package main

import (
	"log"
	"os"
	"time"
)

func main() {
	mtime := time.Date(2006, time.February, 1, 3, 4, 5, 0, time.UTC)
	atime := time.Date(2007, time.March, 2, 4, 5, 6, 0, time.UTC)
	if err := os.Chtimes("some-filename", atime, mtime); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:

```

Share Format Run

```go
func Clearenv()
```

Clearenv deletes all environment variables.

```go
func CopyFS(dir string, fsys fs.FS) error
```

CopyFS copies the file system fsys into the directory dir, creating dir if necessary.

Files are created with mode 0o666 plus any execute permissions from the source, and directories are created with mode 0o777 (before umask).

CopyFS will not overwrite existing files. If a file name in fsys already exists in the destination, CopyFS will return an error such that errors.Is(err, fs.ErrExist) will be true.

Symbolic links in dir are followed.

New files added to fsys (including if dir is a subdirectory of fsys) while CopyFS is running are not guaranteed to be copied.

Copying stops at and returns the first error encountered.

```go
func DirFS(dir string) fs.FS
```

DirFS returns a file system (an fs.FS) for the tree of files rooted at the directory dir.

Note that DirFS("/prefix") only guarantees that the Open calls it makes to the operating system will begin with "/prefix": DirFS("/prefix").Open("file") is the same as os.Open("/prefix/file"). So if /prefix/file is a symbolic link pointing outside the /prefix tree, then using DirFS does not stop the access any more than using os.Open does. Additionally, the root of the fs.FS returned for a relative path, DirFS("prefix"), will be affected by later calls to Chdir. DirFS is therefore not a general substitute for a chroot-style security mechanism when the directory tree contains arbitrary content.

Use Root.FS to obtain a fs.FS that prevents escapes from the tree via symbolic links.

The directory dir must not be "".

The result implements io/fs.StatFS, io/fs.ReadFileFS, io/fs.ReadDirFS, and io/fs.ReadLinkFS.

```go
func Environ() []string
```

Environ returns a copy of strings representing the environment, in the form "key=value".

```go
func Executable() (string, error)
```

Executable returns the path name for the executable that started the current process. There is no guarantee that the path is still pointing to the correct executable. If a symlink was used to start the process, depending on the operating system, the result might be the symlink or the path it pointed to. If a stable result is needed, path/filepath.EvalSymlinks might help.

Executable returns an absolute path unless an error occurred.

The main use case is finding resources located relative to an executable.

```go
func Exit(code int)
```

Exit causes the current program to exit with the given status code. Conventionally, code zero indicates success, non-zero an error. The program terminates immediately; deferred functions are not run.

For portability, the status code should be in the range [0, 125].

```go
func Expand(s string, mapping func(string) string) string
```

Expand replaces ${var} or $var in the string based on the mapping function. For example, os.ExpandEnv(s) is equivalent to os.Expand(s, os.Getenv).

```go

package main

import (
	"fmt"
	"os"
)

func main() {
	mapper := func(placeholderName string) string {
		switch placeholderName {
		case "DAY_PART":
			return "morning"
		case "NAME":
			return "Gopher"
		}

return ""
	}

fmt.Println(os.Expand("Good ${DAY_PART}, $NAME!", mapper))

}

```

```go
Output:
Good morning, Gopher!

```

Share Format Run

```go
func ExpandEnv(s string) string
```

ExpandEnv replaces ${var} or $var in the string according to the values of the current environment variables. References to undefined variables are replaced by the empty string.

```go

package main

import (
	"fmt"
	"os"
)

func main() {
	os.Setenv("NAME", "gopher")
	os.Setenv("BURROW", "/usr/gopher")

fmt.Println(os.ExpandEnv("$NAME lives in ${BURROW}."))

}

```

```go
Output:
gopher lives in /usr/gopher.

```

Share Format Run

```go
func Getegid() int
```

Getegid returns the numeric effective group id of the caller.

On Windows, it returns -1.

```go
func Getenv(key string) string
```

Getenv retrieves the value of the environment variable named by the key. It returns the value, which will be empty if the variable is not present. To distinguish between an empty value and an unset value, use LookupEnv.

```go

package main

import (
	"fmt"
	"os"
)

func main() {
	os.Setenv("NAME", "gopher")
	os.Setenv("BURROW", "/usr/gopher")

fmt.Printf("%s lives in %s.\n", os.Getenv("NAME"), os.Getenv("BURROW"))

}

```

```go
Output:
gopher lives in /usr/gopher.

```

Share Format Run

```go
func Geteuid() int
```

Geteuid returns the numeric effective user id of the caller.

On Windows, it returns -1.

```go
func Getgid() int
```

Getgid returns the numeric group id of the caller.

On Windows, it returns -1.

```go
func Getgroups() ([]int, error)
```

Getgroups returns a list of the numeric ids of groups that the caller belongs to.

On Windows, it returns syscall.EWINDOWS. See the os/user package for a possible alternative.

```go
func Getpagesize() int
```

Getpagesize returns the underlying system's memory page size.

```go
func Getpid() int
```

Getpid returns the process id of the caller.
