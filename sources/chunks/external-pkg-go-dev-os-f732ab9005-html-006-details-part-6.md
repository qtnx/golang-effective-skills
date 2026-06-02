---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/os"
source_path: "sources/raw/external/pkg-go-dev-os-f732ab9005.html"
license_ref: ""
---

WriteString is like Write, but writes the contents of string s rather than a slice of bytes.

```go
func (f *File) WriteTo(w io.Writer) (n int64, err error)
```

WriteTo implements io.WriterTo.

```go
type FileInfo = fs.FileInfo
```

A FileInfo describes a file and is returned by Stat and Lstat.

```go
func Lstat(name string) (FileInfo, error)
```

Lstat returns a FileInfo describing the named file. If the file is a symbolic link, the returned FileInfo describes the symbolic link. Lstat makes no attempt to follow the link. If there is an error, it will be of type *PathError.

On Windows, if the file is a reparse point that is a surrogate for another named entity (such as a symbolic link or mounted folder), the returned FileInfo describes the reparse point, and makes no attempt to resolve it.

```go
func Stat(name string) (FileInfo, error)
```

Stat returns a FileInfo describing the named file. If there is an error, it will be of type *PathError.

```go
type FileMode = fs.FileMode
```

A FileMode represents a file's mode and permission bits. The bits have the same definition on all systems, so that information about files can be moved from one system to another portably. Not all bits apply to all systems. The only required bit is ModeDir for directories.

```go

package main

import (
	"fmt"
	"io/fs"
	"log"
	"os"
)

func main() {
	fi, err := os.Lstat("some-filename")
	if err != nil {
		log.Fatal(err)
	}

fmt.Printf("permissions: %#o\n", fi.Mode().Perm()) // 0o400, 0o777, etc.
	switch mode := fi.Mode(); {
	case mode.IsRegular():
		fmt.Println("regular file")
	case mode.IsDir():
		fmt.Println("directory")
	case mode&fs.ModeSymlink != 0:
		fmt.Println("symbolic link")
	case mode&fs.ModeNamedPipe != 0:
		fmt.Println("named pipe")
	}
}

```

```go
Output:

```

Share Format Run

```go
type LinkError struct {
	Op  string
	Old string
	New string
	Err error
}
```

LinkError records an error during a link or symlink or rename system call and the paths that caused it.

```go
func (e *LinkError) Error() string
```

```go
func (e *LinkError) Unwrap() error
```

```go
type PathError = fs.PathError
```

PathError records an error and the operation and file path that caused it.

```go
type ProcAttr struct {
	// If Dir is non-empty, the child changes into the directory before
	// creating the process.
	Dir string
	// If Env is non-nil, it gives the environment variables for the
	// new process in the form returned by Environ.
	// If it is nil, the result of Environ will be used.
	Env []string
	// Files specifies the open files inherited by the new process. The
	// first three entries correspond to standard input, standard output, and
	// standard error. An implementation may support additional entries,
	// depending on the underlying operating system. A nil entry corresponds
	// to that file being closed when the process starts.
	// On Unix systems, StartProcess will change these File values
	// to blocking mode, which means that SetDeadline will stop working
	// and calling Close will not interrupt a Read or Write.
	Files []*File

// Operating system-specific process creation attributes.
	// Note that setting this field means that your program
	// may not execute properly or even compile on some
	// operating systems.
	Sys *syscall.SysProcAttr
}
```

ProcAttr holds the attributes that will be applied to a new process started by StartProcess.

```go
type Process struct {
	Pid int
	// contains filtered or unexported fields
}
```

Process stores the information about a process created by StartProcess.

```go
func FindProcess(pid int) (*Process, error)
```

FindProcess looks for a running process by its pid.

The Process it returns can be used to obtain information about the underlying operating system process.

On Unix systems, FindProcess always succeeds and returns a Process for the given pid, regardless of whether the process exists. To test whether the process actually exists, see whether p.Signal(syscall.Signal(0)) reports an error.

```go
func StartProcess(name string, argv []string, attr *ProcAttr) (*Process, error)
```

StartProcess starts a new process with the program, arguments and attributes specified by name, argv and attr. The argv slice will become os.Args in the new process, so it normally starts with the program name.

If the calling goroutine has locked the operating system thread with runtime.LockOSThread and modified any inheritable OS-level thread state (for example, Linux or Plan 9 name spaces), the new process will inherit the caller's thread state.

StartProcess is a low-level interface. The os/exec package provides higher-level interfaces.

If there is an error, it will be of type *PathError.

```go
func (p *Process) Kill() error
```

Kill causes the Process to exit immediately. Kill does not wait until the Process has actually exited. This only kills the Process itself, not any other processes it may have started.

```go
func (p *Process) Release() error
```

Release releases any resources associated with the Process p, rendering it unusable in the future. Release only needs to be called if Process.Wait is not.

```go
func (p *Process) Signal(sig Signal) error
```

Signal sends a signal to the Process. Sending Interrupt on Windows is not implemented.

```go
func (p *Process) Wait() (*ProcessState, error)
```

Wait waits for the Process to exit, and then returns a ProcessState describing its status and an error, if any. Wait releases any resources associated with the Process. On most operating systems, the Process must be a child of the current process or an error will be returned.

```go
func (p *Process) WithHandle(f func(handle uintptr)) error
```

WithHandle calls a supplied function f with a valid process handle as an argument. The handle is guaranteed to refer to process p until f returns, even if p terminates. This function cannot be used after Process.Release or Process.Wait.

If process handles are not supported or a handle is not available, it returns ErrNoHandle. Currently, process handles are supported on Linux 5.4 or later (pidfd) and Windows.

```go
type ProcessState struct {
	// contains filtered or unexported fields
}
```

ProcessState stores information about a process, as reported by Wait.

```go
func (p *ProcessState) ExitCode() int
```

ExitCode returns the exit code of the exited process, or -1 if the process hasn't exited or was terminated by a signal.

```go
func (p *ProcessState) Exited() bool
```

Exited reports whether the program has exited. On Unix systems this reports true if the program exited due to calling exit, but false if the program terminated due to a signal.

```go
func (p *ProcessState) Pid() int
```

Pid returns the process id of the exited process.

```go
func (p *ProcessState) String() string
```

```go
func (p *ProcessState) Success() bool
```

Success reports whether the program exited successfully, such as with exit status 0 on Unix.

```go
func (p *ProcessState) Sys() any
```

Sys returns system-dependent exit information about the process. Convert it to the appropriate underlying type, such as syscall.WaitStatus on Unix, to access its contents.

```go
func (p *ProcessState) SysUsage() any
```

SysUsage returns system-dependent resource usage information about the exited process. Convert it to the appropriate underlying type, such as *syscall.Rusage on Unix, to access its contents. (On Unix, *syscall.Rusage matches struct rusage as defined in the getrusage(2) manual page.)

```go
func (p *ProcessState) SystemTime() time.Duration
```

SystemTime returns the system CPU time of the exited process and its children.

```go
func (p *ProcessState) UserTime() time.Duration
```

UserTime returns the user CPU time of the exited process and its children.

```go
type Root struct {
	// contains filtered or unexported fields
}
```

Root may be used to only access files within a single directory tree.

Methods on Root can only access files and directories beneath a root directory. If any component of a file name passed to a method of Root references a location outside the root, the method returns an error. File names may reference the directory itself (.).

Methods on Root will follow symbolic links, but symbolic links may not reference a location outside the root. Symbolic links must not be absolute.

Methods on Root do not prohibit traversal of filesystem boundaries, Linux bind mounts, /proc special files, or access to Unix device files.

Methods on Root are safe to be used from multiple goroutines simultaneously.

On most platforms, creating a Root opens a file descriptor or handle referencing the directory. If the directory is moved, methods on Root reference the original directory in its new location.

Root's behavior differs on some platforms:

- When GOOS=windows, file names may not reference Windows reserved device names such as NUL and COM1.
- On Unix, Root.Chmod, Root.Chown, and Root.Chtimes are vulnerable to a race condition. If the target of the operation is changed from a regular file to a symlink while the operation is in progress, the operation may be performed on the link rather than the link target.
- When GOOS=js, Root is vulnerable to TOCTOU (time-of-check-time-of-use) attacks in symlink validation, and cannot ensure that operations will not escape the root.
- When GOOS=plan9 or GOOS=js, Root does not track directories across renames. On these platforms, a Root references a directory name, not a file descriptor.
- WASI preview 1 (GOOS=wasip1) does not support Root.Chmod.

```go
func OpenRoot(name string) (*Root, error)
```

OpenRoot opens the named directory. It follows symbolic links in the directory name. If there is an error, it will be of type *PathError.

```go
func (r *Root) Chmod(name string, mode FileMode) error
```

Chmod changes the mode of the named file in the root to mode. See Chmod for more details.

```go
func (r *Root) Chown(name string, uid, gid int) error
```

Chown changes the numeric uid and gid of the named file in the root. See Chown for more details.

```go
func (r *Root) Chtimes(name string, atime time.Time, mtime time.Time) error
```
