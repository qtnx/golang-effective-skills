---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/os"
source_path: "sources/raw/external/pkg-go-dev-os-f732ab9005.html"
license_ref: ""
---

```go
func Getppid() int
```

Getppid returns the process id of the caller's parent.

```go
func Getuid() int
```

Getuid returns the numeric user id of the caller.

On Windows, it returns -1.

```go
func Getwd() (dir string, err error)
```

Getwd returns an absolute path name corresponding to the current directory. If the current directory can be reached via multiple paths (due to symbolic links), Getwd may return any one of them.

On Unix platforms, if the environment variable PWD provides an absolute name, and it is a name of the current directory, it is returned.

```go
func Hostname() (name string, err error)
```

Hostname returns the host name reported by the kernel.

```go
func IsExist(err error) bool
```

IsExist returns a boolean indicating whether its argument is known to report that a file or directory already exists. It is satisfied by ErrExist as well as some syscall errors.

This function predates errors.Is. It only supports errors returned by the os package. New code should use errors.Is(err, fs.ErrExist).

```go
func IsNotExist(err error) bool
```

IsNotExist returns a boolean indicating whether its argument is known to report that a file or directory does not exist. It is satisfied by ErrNotExist as well as some syscall errors.

This function predates errors.Is. It only supports errors returned by the os package. New code should use errors.Is(err, fs.ErrNotExist).

```go
func IsPathSeparator(c uint8) bool
```

IsPathSeparator reports whether c is a directory separator character.

```go
func IsPermission(err error) bool
```

IsPermission returns a boolean indicating whether its argument is known to report that permission is denied. It is satisfied by ErrPermission as well as some syscall errors.

This function predates errors.Is. It only supports errors returned by the os package. New code should use errors.Is(err, fs.ErrPermission).

```go
func IsTimeout(err error) bool
```

IsTimeout returns a boolean indicating whether its argument is known to report that a timeout occurred.

This function predates errors.Is, and the notion of whether an error indicates a timeout can be ambiguous. For example, the Unix error EWOULDBLOCK sometimes indicates a timeout and sometimes does not. New code should use errors.Is with a value appropriate to the call returning the error, such as os.ErrDeadlineExceeded.

```go
func Lchown(name string, uid, gid int) error
```

Lchown changes the numeric uid and gid of the named file. If the file is a symbolic link, it changes the uid and gid of the link itself. If there is an error, it will be of type *PathError.

On Windows, it always returns the syscall.EWINDOWS error, wrapped in *PathError.

```go
func Link(oldname, newname string) error
```

Link creates newname as a hard link to the oldname file. If there is an error, it will be of type *LinkError.

```go
func LookupEnv(key string) (string, bool)
```

LookupEnv retrieves the value of the environment variable named by the key. If the variable is present in the environment the value (which may be empty) is returned and the boolean is true. Otherwise the returned value will be empty and the boolean will be false.

```go

package main

import (
	"fmt"
	"os"
)

func main() {
	show := func(key string) {
		val, ok := os.LookupEnv(key)
		if !ok {
			fmt.Printf("%s not set\n", key)
		} else {
			fmt.Printf("%s=%s\n", key, val)
		}
	}

os.Setenv("SOME_KEY", "value")
	os.Setenv("EMPTY_KEY", "")

show("SOME_KEY")
	show("EMPTY_KEY")
	show("MISSING_KEY")

}

```

```go
Output:
SOME_KEY=value
EMPTY_KEY=
MISSING_KEY not set

```

Share Format Run

```go
func Mkdir(name string, perm FileMode) error
```

Mkdir creates a new directory with the specified name and permission bits (before umask). If there is an error, it will be of type *PathError.

```go

package main

import (
	"log"
	"os"
)

func main() {
	err := os.Mkdir("testdir", 0750)
	if err != nil && !os.IsExist(err) {
		log.Fatal(err)
	}
	err = os.WriteFile("testdir/testfile.txt", []byte("Hello, Gophers!"), 0660)
	if err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:

```

Share Format Run

```go
func MkdirAll(path string, perm FileMode) error
```

MkdirAll creates a directory named path, along with any necessary parents, and returns nil, or else returns an error. The permission bits perm (before umask) are used for all directories that MkdirAll creates. If path is already a directory, MkdirAll does nothing and returns nil.

```go

package main

import (
	"log"
	"os"
)

func main() {
	err := os.MkdirAll("test/subdir", 0750)
	if err != nil {
		log.Fatal(err)
	}
	err = os.WriteFile("test/subdir/testfile.txt", []byte("Hello, Gophers!"), 0660)
	if err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:

```

Share Format Run

```go
func MkdirTemp(dir, pattern string) (string, error)
```

MkdirTemp creates a new temporary directory in the directory dir and returns the pathname of the new directory. The new directory's name is generated by adding a random string to the end of pattern. If pattern includes a "*", the random string replaces the last "*" instead. The directory is created with mode 0o700 (before umask). If dir is the empty string, MkdirTemp uses the default directory for temporary files, as returned by TempDir. Multiple programs or goroutines calling MkdirTemp simultaneously will not choose the same directory. It is the caller's responsibility to remove the directory when it is no longer needed.

```go

package main

import (
	"log"
	"os"
	"path/filepath"
)

func main() {
	dir, err := os.MkdirTemp("", "example")
	if err != nil {
		log.Fatal(err)
	}
	defer os.RemoveAll(dir) // clean up

file := filepath.Join(dir, "tmpfile")
	if err := os.WriteFile(file, []byte("content"), 0666); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:

```

Share Format Run

```go

package main

import (
	"log"
	"os"
	"path/filepath"
)

func main() {
	logsDir, err := os.MkdirTemp("", "*-logs")
	if err != nil {
		log.Fatal(err)
	}
	defer os.RemoveAll(logsDir) // clean up

// Logs can be cleaned out earlier if needed by searching
	// for all directories whose suffix ends in *-logs.
	globPattern := filepath.Join(os.TempDir(), "*-logs")
	matches, err := filepath.Glob(globPattern)
	if err != nil {
		log.Fatalf("Failed to match %q: %v", globPattern, err)
	}

for _, match := range matches {
		if err := os.RemoveAll(match); err != nil {
			log.Printf("Failed to remove %q: %v", match, err)
		}
	}
}

```

```go
Output:

```

Share Format Run

```go
func NewSyscallError(syscall string, err error) error
```

NewSyscallError returns, as an error, a new SyscallError with the given system call name and error details. As a convenience, if err is nil, NewSyscallError returns nil.

```go
func Pipe() (r *File, w *File, err error)
```

Pipe returns a connected pair of Files; reads from r return bytes written to w. It returns the files and an error, if any.

```go
func ReadFile(name string) ([]byte, error)
```

ReadFile reads the named file and returns the contents. A successful call returns err == nil, not err == EOF. Because ReadFile reads the whole file, it does not treat an EOF from Read as an error to be reported.

```go

package main

import (
	"log"
	"os"
)

func main() {
	data, err := os.ReadFile("testdata/hello")
	if err != nil {
		log.Fatal(err)
	}
	os.Stdout.Write(data)

}

```

```go
Output:
Hello, Gophers!

```

Share Format Run

```go
func Readlink(name string) (string, error)
```

Readlink returns the destination of the named symbolic link. If there is an error, it will be of type *PathError.

If the link destination is relative, Readlink returns the relative path without resolving it to an absolute one.

```go

package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func main() {
	// First, we create a relative symlink to a file.
	d, err := os.MkdirTemp("", "")
	if err != nil {
		log.Fatal(err)
	}
	defer os.RemoveAll(d)
	targetPath := filepath.Join(d, "hello.txt")
	if err := os.WriteFile(targetPath, []byte("Hello, Gophers!"), 0644); err != nil {
		log.Fatal(err)
	}
	linkPath := filepath.Join(d, "hello.link")
	if err := os.Symlink("hello.txt", filepath.Join(d, "hello.link")); err != nil {
		if errors.Is(err, errors.ErrUnsupported) {
			// Allow the example to run on platforms that do not support symbolic links.
			fmt.Printf("%s links to %s\n", filepath.Base(linkPath), "hello.txt")
			return
		}
		log.Fatal(err)
	}

// Readlink returns the relative path as passed to os.Symlink.
	dst, err := os.Readlink(linkPath)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s links to %s\n", filepath.Base(linkPath), dst)

var dstAbs string
	if filepath.IsAbs(dst) {
		dstAbs = dst
	} else {
		// Symlink targets are relative to the directory containing the link.
		dstAbs = filepath.Join(filepath.Dir(linkPath), dst)
	}

// Check that the target is correct by comparing it with os.Stat
	// on the original target path.
	dstInfo, err := os.Stat(dstAbs)
	if err != nil {
		log.Fatal(err)
	}
	targetInfo, err := os.Stat(targetPath)
	if err != nil {
		log.Fatal(err)
	}
	if !os.SameFile(dstInfo, targetInfo) {
		log.Fatalf("link destination (%s) is not the same file as %s", dstAbs, targetPath)
	}

}

```

```go
Output:
hello.link links to hello.txt

```

Share Format Run

```go
func Remove(name string) error
```

Remove removes the named file or (empty) directory. If there is an error, it will be of type *PathError.

```go
func RemoveAll(path string) error
```

RemoveAll removes path and any children it contains. It removes everything it can but returns the first error it encounters. If the path does not exist, RemoveAll returns nil (no error). If there is an error, it will be of type *PathError.

```go
func Rename(oldpath, newpath string) error
```

Rename renames (moves) oldpath to newpath. If newpath already exists and is not a directory, Rename replaces it. If newpath already exists and is a directory, Rename returns an error. OS-specific restrictions may apply when oldpath and newpath are in different directories. Even within the same directory, on non-Unix platforms Rename is not an atomic operation. If there is an error, it will be of type *LinkError.

```go
func SameFile(fi1, fi2 FileInfo) bool
```
