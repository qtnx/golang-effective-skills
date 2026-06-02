---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/os"
source_path: "sources/raw/external/pkg-go-dev-os-f732ab9005.html"
license_ref: ""
---

SameFile reports whether fi1 and fi2 describe the same file. For example, on Unix this means that the device and inode fields of the two underlying structures are identical; on other systems the decision may be based on the path names. SameFile only applies to results returned by this package's Stat. It returns false in other cases.

```go
func Setenv(key, value string) error
```

Setenv sets the value of the environment variable named by the key. It returns an error, if any.

```go
func Symlink(oldname, newname string) error
```

Symlink creates newname as a symbolic link to oldname. On Windows, a symlink to a non-existent oldname creates a file symlink; if oldname is later created as a directory the symlink will not work. If there is an error, it will be of type *LinkError.

```go
func TempDir() string
```

TempDir returns the default directory to use for temporary files.

On Unix systems, it returns $TMPDIR if non-empty, else /tmp. On Windows, it uses GetTempPath, returning the first non-empty value from %TMP%, %TEMP%, %USERPROFILE%, or the Windows directory. On Plan 9, it returns /tmp.

The directory is neither guaranteed to exist nor have accessible permissions.

```go
func Truncate(name string, size int64) error
```

Truncate changes the size of the named file. If the file is a symbolic link, it changes the size of the link's target. If there is an error, it will be of type *PathError.

```go
func Unsetenv(key string) error
```

Unsetenv unsets a single environment variable.

```go

package main

import (
	"os"
)

func main() {
	os.Setenv("TMPDIR", "/my/tmp")
	defer os.Unsetenv("TMPDIR")
}

```

```go
Output:

```

Share Format Run

```go
func UserCacheDir() (string, error)
```

UserCacheDir returns the default root directory to use for user-specific cached data. Users should create their own application-specific subdirectory within this one and use that.

On Unix systems, it returns $XDG_CACHE_HOME as specified by https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html <https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html> if non-empty, else $HOME/.cache. On Darwin, it returns $HOME/Library/Caches. On Windows, it returns %LocalAppData%. On Plan 9, it returns $home/lib/cache.

If the location cannot be determined (for example, $HOME is not defined) or the path in $XDG_CACHE_HOME is relative, then it will return an error.

```go

package main

import (
	"log"
	"os"
	"path/filepath"
	"sync"
)

func main() {
	dir, dirErr := os.UserCacheDir()
	if dirErr == nil {
		dir = filepath.Join(dir, "ExampleUserCacheDir")
	}

getCache := func(name string) ([]byte, error) {
		if dirErr != nil {
			return nil, &os.PathError{Op: "getCache", Path: name, Err: os.ErrNotExist}
		}
		return os.ReadFile(filepath.Join(dir, name))
	}

var mkdirOnce sync.Once
	putCache := func(name string, b []byte) error {
		if dirErr != nil {
			return &os.PathError{Op: "putCache", Path: name, Err: dirErr}
		}
		mkdirOnce.Do(func() {
			if err := os.MkdirAll(dir, 0700); err != nil {
				log.Printf("can't create user cache dir: %v", err)
			}
		})
		return os.WriteFile(filepath.Join(dir, name), b, 0600)
	}

// Read and store cached data.
	// …
	_ = getCache
	_ = putCache

}

```

```go
Output:

```

Share Format Run

```go
func UserConfigDir() (string, error)
```

UserConfigDir returns the default root directory to use for user-specific configuration data. Users should create their own application-specific subdirectory within this one and use that.

On Unix systems, it returns $XDG_CONFIG_HOME as specified by https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html <https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html> if non-empty, else $HOME/.config. On Darwin, it returns $HOME/Library/Application Support. On Windows, it returns %AppData%. On Plan 9, it returns $home/lib.

If the location cannot be determined (for example, $HOME is not defined) or the path in $XDG_CONFIG_HOME is relative, then it will return an error.

```go

package main

import (
	"bytes"
	"log"
	"os"
	"path/filepath"
)

func main() {
	dir, dirErr := os.UserConfigDir()

var (
		configPath string
		origConfig []byte
	)
	if dirErr == nil {
		configPath = filepath.Join(dir, "ExampleUserConfigDir", "example.conf")
		var err error
		origConfig, err = os.ReadFile(configPath)
		if err != nil && !os.IsNotExist(err) {
			// The user has a config file but we couldn't read it.
			// Report the error instead of ignoring their configuration.
			log.Fatal(err)
		}
	}

// Use and perhaps make changes to the config.
	config := bytes.Clone(origConfig)
	// …

// Save changes.
	if !bytes.Equal(config, origConfig) {
		if configPath == "" {
			log.Printf("not saving config changes: %v", dirErr)
		} else {
			err := os.MkdirAll(filepath.Dir(configPath), 0700)
			if err == nil {
				err = os.WriteFile(configPath, config, 0600)
			}
			if err != nil {
				log.Printf("error saving config changes: %v", err)
			}
		}
	}

}

```

```go
Output:

```

Share Format Run

```go
func UserHomeDir() (string, error)
```

UserHomeDir returns the current user's home directory.

On Unix, including macOS, it returns the $HOME environment variable. On Windows, it returns %USERPROFILE%. On Plan 9, it returns the $home environment variable.

If the expected variable is not set in the environment, UserHomeDir returns either a platform-specific default value or a non-nil error.

```go
func WriteFile(name string, data []byte, perm FileMode) error
```

WriteFile writes data to the named file, creating it if necessary. If the file does not exist, WriteFile creates it with permissions perm (before umask); otherwise WriteFile truncates it before writing, without changing permissions. Since WriteFile requires multiple system calls to complete, a failure mid-operation can leave the file in a partially written state.

```go

package main

import (
	"log"
	"os"
)

func main() {
	err := os.WriteFile("testdata/hello", []byte("Hello, Gophers!"), 0666)
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
type DirEntry = fs.DirEntry
```

A DirEntry is an entry read from a directory (using the ReadDir function or a File.ReadDir method).

```go
func ReadDir(name string) ([]DirEntry, error)
```

ReadDir reads the named directory, returning all its directory entries sorted by filename. If an error occurs reading the directory, ReadDir returns the entries it was able to read before the error, along with the error.

```go

package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	files, err := os.ReadDir(".")
	if err != nil {
		log.Fatal(err)
	}

for _, file := range files {
		fmt.Println(file.Name())
	}
}

```

```go
Output:

```

Share Format Run

```go
type File struct {
	// contains filtered or unexported fields
}
```

File represents an open file descriptor.

The methods of File are safe for concurrent use.

```go
func Create(name string) (*File, error)
```

Create creates or truncates the named file. If the file already exists, it is truncated. If the file does not exist, it is created with mode 0o666 (before umask). If successful, methods on the returned File can be used for I/O; the associated file descriptor has mode O_RDWR. The directory containing the file must already exist. If there is an error, it will be of type *PathError.

```go
func CreateTemp(dir, pattern string) (*File, error)
```

CreateTemp creates a new temporary file in the directory dir, opens the file for reading and writing, and returns the resulting file. The filename is generated by taking pattern and adding a random string to the end. If pattern includes a "*", the random string replaces the last "*". The file is created with mode 0o600 (before umask). If dir is the empty string, CreateTemp uses the default directory for temporary files, as returned by TempDir. Multiple programs or goroutines calling CreateTemp simultaneously will not choose the same file. The caller can use the file's Name method to find the pathname of the file. It is the caller's responsibility to remove the file when it is no longer needed.

```go

package main

import (
	"log"
	"os"
)

func main() {
	f, err := os.CreateTemp("", "example")
	if err != nil {
		log.Fatal(err)
	}
	defer os.Remove(f.Name()) // clean up

if _, err := f.Write([]byte("content")); err != nil {
		log.Fatal(err)
	}
	if err := f.Close(); err != nil {
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
)

func main() {
	f, err := os.CreateTemp("", "example.*.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer os.Remove(f.Name()) // clean up

if _, err := f.Write([]byte("content")); err != nil {
		f.Close()
		log.Fatal(err)
	}
	if err := f.Close(); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:

```

Share Format Run

```go
func NewFile(fd uintptr, name string) *File
```

NewFile returns a new File with the given file descriptor and name. The returned value will be nil if fd is not a valid file descriptor.

NewFile's behavior differs on some platforms:

- On Unix, if fd is in non-blocking mode, NewFile will attempt to return a pollable file.
- On Windows, if fd is opened for asynchronous I/O (that is, syscall.FILE_FLAG_OVERLAPPED has been specified in the syscall.CreateFile call), NewFile will attempt to return a pollable file by associating fd with the Go runtime I/O completion port. The I/O operations will be performed synchronously if the association fails.

Only pollable files support File.SetDeadline, File.SetReadDeadline, and File.SetWriteDeadline.

After passing it to NewFile, fd may become invalid under the same conditions described in the comments of File.Fd, and the same constraints apply.

```go
func Open(name string) (*File, error)
```

Open opens the named file for reading. If successful, methods on the returned file can be used for reading; the associated file descriptor has mode O_RDONLY. If there is an error, it will be of type *PathError.

```go
func OpenFile(name string, flag int, perm FileMode) (*File, error)
```

OpenFile is the generalized open call; most users will use Open or Create instead. It opens the named file with specified flag (O_RDONLY etc.). If the file does not exist, and the O_CREATE flag is passed, it is created with mode perm (before umask); the containing directory must exist. If successful, methods on the returned File can be used for I/O. If there is an error, it will be of type *PathError.

```go

package main

import (
	"log"
	"os"
)
