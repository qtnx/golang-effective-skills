---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/os"
source_path: "sources/raw/external/pkg-go-dev-os-f732ab9005.html"
license_ref: ""
---

func main() {
	f, err := os.OpenFile("notes.txt", os.O_RDWR|os.O_CREATE, 0644)
	if err != nil {
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
	// If the file doesn't exist, create it, or append to the file
	f, err := os.OpenFile("access.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatal(err)
	}
	if _, err := f.Write([]byte("appended some data\n")); err != nil {
		f.Close() // ignore error; Write error takes precedence
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
func OpenInRoot(dir, name string) (*File, error)
```

OpenInRoot opens the file name in the directory dir. It is equivalent to OpenRoot(dir) followed by opening the file in the root.

OpenInRoot returns an error if any component of the name references a location outside of dir.

See Root for details and limitations.

```go
func (f *File) Chdir() error
```

Chdir changes the current working directory to the file, which must be a directory. If there is an error, it will be of type *PathError.

```go
func (f *File) Chmod(mode FileMode) error
```

Chmod changes the mode of the file to mode. If there is an error, it will be of type *PathError.

```go
func (f *File) Chown(uid, gid int) error
```

Chown changes the numeric uid and gid of the named file. If there is an error, it will be of type *PathError.

On Windows, it always returns the syscall.EWINDOWS error, wrapped in *PathError.

```go
func (f *File) Close() error
```

Close closes the File, rendering it unusable for I/O. On files that support File.SetDeadline, any pending I/O operations will be canceled and return immediately with an ErrClosed error. Close will return an error if it has already been called.

```go
func (f *File) Fd() uintptr
```

Fd returns the system file descriptor or handle referencing the open file. If f is closed, the descriptor becomes invalid. If f is garbage collected, a finalizer may close the descriptor, making it invalid; see runtime.SetFinalizer for more information on when a finalizer might be run.

Do not close the returned descriptor; that could cause a later close of f to close an unrelated descriptor.

Fd's behavior differs on some platforms:

- On Unix and Windows, File.SetDeadline methods will stop working.
- On Windows, the file descriptor will be disassociated from the Go runtime I/O completion port if there are no concurrent I/O operations on the file.

For most uses prefer the f.SyscallConn method.

```go
func (f *File) Name() string
```

Name returns the name of the file as presented to Open.

It is safe to call Name after [Close].

```go
func (f *File) Read(b []byte) (n int, err error)
```

Read reads up to len(b) bytes from the File and stores them in b. It returns the number of bytes read and any error encountered. At end of file, Read returns 0, io.EOF.

```go
func (f *File) ReadAt(b []byte, off int64) (n int, err error)
```

ReadAt reads len(b) bytes from the File starting at byte offset off. It returns the number of bytes read and the error, if any. ReadAt always returns a non-nil error when n < len(b). At end of file, that error is io.EOF.

```go
func (f *File) ReadDir(n int) ([]DirEntry, error)
```

ReadDir reads the contents of the directory associated with the file f and returns a slice of DirEntry values in directory order. Subsequent calls on the same file will yield later DirEntry records in the directory.

If n > 0, ReadDir returns at most n DirEntry records. In this case, if ReadDir returns an empty slice, it will return an error explaining why. At the end of a directory, the error is io.EOF.

If n <= 0, ReadDir returns all the DirEntry records remaining in the directory. When it succeeds, it returns a nil error (not io.EOF).

```go
func (f *File) ReadFrom(r io.Reader) (n int64, err error)
```

ReadFrom implements io.ReaderFrom.

```go
func (f *File) Readdir(n int) ([]FileInfo, error)
```

Readdir reads the contents of the directory associated with file and returns a slice of up to n FileInfo values, as would be returned by Lstat, in directory order. Subsequent calls on the same file will yield further FileInfos.

If n > 0, Readdir returns at most n FileInfo structures. In this case, if Readdir returns an empty slice, it will return a non-nil error explaining why. At the end of a directory, the error is io.EOF.

If n <= 0, Readdir returns all the FileInfo from the directory in a single slice. In this case, if Readdir succeeds (reads all the way to the end of the directory), it returns the slice and a nil error. If it encounters an error before the end of the directory, Readdir returns the FileInfo read until that point and a non-nil error.

Most clients are better served by the more efficient ReadDir method.

```go
func (f *File) Readdirnames(n int) (names []string, err error)
```

Readdirnames reads the contents of the directory associated with file and returns a slice of up to n names of files in the directory, in directory order. Subsequent calls on the same file will yield further names.

If n > 0, Readdirnames returns at most n names. In this case, if Readdirnames returns an empty slice, it will return a non-nil error explaining why. At the end of a directory, the error is io.EOF.

If n <= 0, Readdirnames returns all the names from the directory in a single slice. In this case, if Readdirnames succeeds (reads all the way to the end of the directory), it returns the slice and a nil error. If it encounters an error before the end of the directory, Readdirnames returns the names read until that point and a non-nil error.

```go
func (f *File) Seek(offset int64, whence int) (ret int64, err error)
```

Seek sets the offset for the next Read or Write on file to offset, interpreted according to whence: 0 means relative to the origin of the file, 1 means relative to the current offset, and 2 means relative to the end. It returns the new offset and an error, if any. The behavior of Seek on a file opened with O_APPEND is not specified.

```go
func (f *File) SetDeadline(t time.Time) error
```

SetDeadline sets the read and write deadlines for a File. It is equivalent to calling both SetReadDeadline and SetWriteDeadline.

Only some kinds of files support setting a deadline. Calls to SetDeadline for files that do not support deadlines will return ErrNoDeadline. On most systems ordinary files do not support deadlines, but pipes do.

A deadline is an absolute time after which I/O operations fail with an error instead of blocking. The deadline applies to all future and pending I/O, not just the immediately following call to Read or Write. After a deadline has been exceeded, the connection can be refreshed by setting a deadline in the future.

If the deadline is exceeded a call to Read or Write or to other I/O methods will return an error that wraps ErrDeadlineExceeded. This can be tested using errors.Is(err, os.ErrDeadlineExceeded). That error implements the Timeout method, and calling the Timeout method will return true, but there are other possible errors for which the Timeout will return true even if the deadline has not been exceeded.

An idle timeout can be implemented by repeatedly extending the deadline after successful Read or Write calls.

A zero value for t means I/O operations will not time out.

```go
func (f *File) SetReadDeadline(t time.Time) error
```

SetReadDeadline sets the deadline for future Read calls and any currently-blocked Read call. A zero value for t means Read will not time out. Not all files support setting deadlines; see SetDeadline.

```go
func (f *File) SetWriteDeadline(t time.Time) error
```

SetWriteDeadline sets the deadline for any future Write calls and any currently-blocked Write call. Even if Write times out, it may return n > 0, indicating that some of the data was successfully written. A zero value for t means Write will not time out. Not all files support setting deadlines; see SetDeadline.

```go
func (f *File) Stat() (FileInfo, error)
```

Stat returns the FileInfo structure describing file. If there is an error, it will be of type *PathError.

```go
func (f *File) Sync() error
```

Sync commits the current contents of the file to stable storage. Typically, this means flushing the file system's in-memory copy of recently written data to disk.

```go
func (f *File) SyscallConn() (syscall.RawConn, error)
```

SyscallConn returns a raw file. This implements the syscall.Conn interface.

```go
func (f *File) Truncate(size int64) error
```

Truncate changes the size of the file. It does not change the I/O offset. If there is an error, it will be of type *PathError.

```go
func (f *File) Write(b []byte) (n int, err error)
```

Write writes len(b) bytes from b to the File. It returns the number of bytes written and an error, if any. Write returns a non-nil error when n != len(b).

```go
func (f *File) WriteAt(b []byte, off int64) (n int, err error)
```

WriteAt writes len(b) bytes to the File starting at byte offset off. It returns the number of bytes written and an error, if any. WriteAt returns a non-nil error when n != len(b).

If file was opened with the O_APPEND flag, WriteAt returns an error.

```go
func (f *File) WriteString(s string) (n int, err error)
```
