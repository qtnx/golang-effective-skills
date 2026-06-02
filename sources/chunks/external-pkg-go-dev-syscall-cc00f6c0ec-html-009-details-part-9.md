---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/syscall"
source_path: "sources/raw/external/pkg-go-dev-syscall-cc00f6c0ec.html"
license_ref: ""
---

```go
func Pread(fd int, p []byte, offset int64) (n int, err error)
```

```go
func PtraceAttach(pid int) (err error)
```

```go
func PtraceCont(pid int, signal int) (err error)
```

```go
func PtraceDetach(pid int) (err error)
```

```go
func PtraceGetEventMsg(pid int) (msg uint, err error)
```

```go
func PtraceGetRegs(pid int, regsout *PtraceRegs) (err error)
```

```go
func PtracePeekData(pid int, addr uintptr, out []byte) (count int, err error)
```

```go
func PtracePeekText(pid int, addr uintptr, out []byte) (count int, err error)
```

```go
func PtracePokeData(pid int, addr uintptr, data []byte) (count int, err error)
```

```go
func PtracePokeText(pid int, addr uintptr, data []byte) (count int, err error)
```

```go
func PtraceSetOptions(pid int, options int) (err error)
```

```go
func PtraceSetRegs(pid int, regs *PtraceRegs) (err error)
```

```go
func PtraceSingleStep(pid int) (err error)
```

```go
func PtraceSyscall(pid int, signal int) (err error)
```

```go
func Pwrite(fd int, p []byte, offset int64) (n int, err error)
```

```go
func Read(fd int, p []byte) (n int, err error)
```

```go
func ReadDirent(fd int, buf []byte) (n int, err error)
```

```go
func Readlink(path string, buf []byte) (n int, err error)
```

```go
func Reboot(cmd int) (err error)
```

```go
func Removexattr(path string, attr string) (err error)
```

```go
func Rename(oldpath string, newpath string) (err error)
```

```go
func Renameat(olddirfd int, oldpath string, newdirfd int, newpath string) (err error)
```

```go
func Rmdir(path string) error
```

```go
func Seek(fd int, offset int64, whence int) (off int64, err error)
```

```go
func Select(nfd int, r *FdSet, w *FdSet, e *FdSet, timeout *Timeval) (n int, err error)
```

```go
func Sendfile(outfd int, infd int, offset *int64, count int) (written int, err error)
```

```go
func Sendmsg(fd int, p, oob []byte, to Sockaddr, flags int) (err error)
```

```go
func SendmsgN(fd int, p, oob []byte, to Sockaddr, flags int) (n int, err error)
```

```go
func Sendto(fd int, p []byte, flags int, to Sockaddr) (err error)
```

```go
func SetLsfPromisc(name string, m bool) error
```

Deprecated: Use golang.org/x/net/bpf instead.

```go
func SetNonblock(fd int, nonblocking bool) (err error)
```

```go
func Setdomainname(p []byte) (err error)
```

```go
func Setegid(egid int) (err error)
```

```go
func Setenv(key, value string) error
```

```go
func Seteuid(euid int) (err error)
```

```go
func Setfsgid(gid int) (err error)
```

```go
func Setfsuid(uid int) (err error)
```

```go
func Setgid(gid int) (err error)
```

```go
func Setgroups(gids []int) (err error)
```

```go
func Sethostname(p []byte) (err error)
```

```go
func Setpgid(pid int, pgid int) (err error)
```

```go
func Setpriority(which int, who int, prio int) (err error)
```

```go
func Setregid(rgid, egid int) (err error)
```

```go
func Setresgid(rgid, egid, sgid int) (err error)
```

```go
func Setresuid(ruid, euid, suid int) (err error)
```

```go
func Setreuid(ruid, euid int) (err error)
```

```go
func Setrlimit(resource int, rlim *Rlimit) error
```

```go
func Setsid() (pid int, err error)
```

```go
func SetsockoptByte(fd, level, opt int, value byte) (err error)
```

```go
func SetsockoptICMPv6Filter(fd, level, opt int, filter *ICMPv6Filter) error
```

```go
func SetsockoptIPMreq(fd, level, opt int, mreq *IPMreq) (err error)
```

```go
func SetsockoptIPMreqn(fd, level, opt int, mreq *IPMreqn) (err error)
```

```go
func SetsockoptIPv6Mreq(fd, level, opt int, mreq *IPv6Mreq) (err error)
```

```go
func SetsockoptInet4Addr(fd, level, opt int, value [4]byte) (err error)
```

```go
func SetsockoptInt(fd, level, opt int, value int) (err error)
```

```go
func SetsockoptLinger(fd, level, opt int, l *Linger) (err error)
```

```go
func SetsockoptString(fd, level, opt int, s string) (err error)
```

```go
func SetsockoptTimeval(fd, level, opt int, tv *Timeval) (err error)
```

```go
func Settimeofday(tv *Timeval) (err error)
```

```go
func Setuid(uid int) (err error)
```

```go
func Setxattr(path string, attr string, data []byte, flags int) (err error)
```

```go
func Shutdown(fd int, how int) (err error)
```

```go
func SlicePtrFromStrings(ss []string) ([]*byte, error)
```

SlicePtrFromStrings converts a slice of strings to a slice of pointers to NUL-terminated byte arrays. If any string contains a NUL byte, it returns (nil, EINVAL).

```go
func Socket(domain, typ, proto int) (fd int, err error)
```

```go
func Socketpair(domain, typ, proto int) (fd [2]int, err error)
```

```go
func Splice(rfd int, roff *int64, wfd int, woff *int64, len int, flags int) (n int64, err error)
```

```go
func StartProcess(argv0 string, argv []string, attr *ProcAttr) (pid int, handle uintptr, err error)
```

StartProcess wraps ForkExec for package os.

```go
func Stat(path string, stat *Stat_t) (err error)
```

```go
func Statfs(path string, buf *Statfs_t) (err error)
```

```go
func StringBytePtr(s string) *byte
```

StringBytePtr returns a pointer to a NUL-terminated array of bytes. If s contains a NUL byte this function panics instead of returning an error.

Deprecated: Use BytePtrFromString instead.

```go
func StringByteSlice(s string) []byte
```

StringByteSlice converts a string to a NUL-terminated []byte, If s contains a NUL byte this function panics instead of returning an error.

Deprecated: Use ByteSliceFromString instead.

```go
func StringSlicePtr(ss []string) []*byte
```

StringSlicePtr converts a slice of strings to a slice of pointers to NUL-terminated byte arrays. If any string contains a NUL byte this function panics instead of returning an error.

Deprecated: Use SlicePtrFromStrings instead.

```go
func Symlink(oldpath string, newpath string) (err error)
```

```go
func Sync()
```

```go
func SyncFileRange(fd int, off int64, n int64, flags int) (err error)
```

```go
func Sysinfo(info *Sysinfo_t) (err error)
```

```go
func Tee(rfd int, wfd int, len int, flags int) (n int64, err error)
```

```go
func Tgkill(tgid int, tid int, sig Signal) (err error)
```

```go
func Times(tms *Tms) (ticks uintptr, err error)
```

```go
func TimespecToNsec(ts Timespec) int64
```

TimespecToNsec returns the time stored in ts as nanoseconds.

```go
func TimevalToNsec(tv Timeval) int64
```

TimevalToNsec returns the time stored in tv as nanoseconds.

```go
func Truncate(path string, length int64) (err error)
```

```go
func Umask(mask int) (oldmask int)
```

```go
func Uname(buf *Utsname) (err error)
```

```go
func UnixCredentials(ucred *Ucred) []byte
```

UnixCredentials encodes credentials into a socket control message for sending to another process. This can be used for authentication.

```go
func UnixRights(fds ...int) []byte
```

UnixRights encodes a set of open file descriptors into a socket control message for sending to another process.

```go
func Unlink(path string) error
```

```go
func Unlinkat(dirfd int, path string) error
```

```go
func Unmount(target string, flags int) (err error)
```

```go
func Unsetenv(key string) error
```

```go
func Unshare(flags int) (err error)
```

```go
func Ustat(dev int, ubuf *Ustat_t) (err error)
```

```go
func Utime(path string, buf *Utimbuf) (err error)
```

```go
func Utimes(path string, tv []Timeval) (err error)
```

```go
func UtimesNano(path string, ts []Timespec) (err error)
```

```go
func Wait4(pid int, wstatus *WaitStatus, options int, rusage *Rusage) (wpid int, err error)
```

```go
func Write(fd int, p []byte) (n int, err error)
```

```go
type Cmsghdr struct {
	Len   uint64
	Level int32
	Type  int32
}
```

```go
func (cmsg *Cmsghdr) SetLen(length int)
```

```go
type Conn interface {
	// SyscallConn returns a raw network connection.
	SyscallConn() (RawConn, error)
}
```

Conn is implemented by some types in the net and os packages to provide access to the underlying file descriptor or handle.

```go
type Credential struct {
	Uid         uint32   // User ID.
	Gid         uint32   // Group ID.
	Groups      []uint32 // Supplementary group IDs.
	NoSetGroups bool     // If true, don't set supplementary groups
}
```

Credential holds user and group identities to be assumed by a child process started by StartProcess.

```go
type Dirent struct {
	Ino       uint64
	Off       int64
	Reclen    uint16
	Type      uint8
	Name      [256]int8
	Pad_cgo_0 [5]byte
}
```

```go
type EpollEvent struct {
	Events uint32
	Fd     int32
	Pad    int32
}
```

```go
type Errno uintptr
```

An Errno is an unsigned number describing an error condition. It implements the error interface. The zero Errno is by convention a non-error, so code to convert from Errno to error should use:

```go
err = nil
if errno != 0 {
	err = errno
}

```

Errno values can be tested against error values using errors.Is. For example:

```go
_, _, err := syscall.Syscall(...)
if errors.Is(err, fs.ErrNotExist) ...

```

```go
func AllThreadsSyscall(trap, a1, a2, a3 uintptr) (r1, r2 uintptr, err Errno)
```

AllThreadsSyscall performs a syscall on each OS thread of the Go runtime. It first invokes the syscall on one thread. Should that invocation fail, it returns immediately with the error status. Otherwise, it invokes the syscall on all of the remaining threads in parallel. It will terminate the program if it observes any invoked syscall's return value differs from that of the first invocation.

AllThreadsSyscall is intended for emulating simultaneous process-wide state changes that require consistently modifying per-thread state of the Go runtime.

AllThreadsSyscall is unaware of any threads that are launched explicitly by cgo linked code, so the function always returns ENOTSUP in binaries that use cgo.

```go
func AllThreadsSyscall6(trap, a1, a2, a3, a4, a5, a6 uintptr) (r1, r2 uintptr, err Errno)
```

AllThreadsSyscall6 is like AllThreadsSyscall, but extended to six arguments.

```go
func RawSyscall(trap, a1, a2, a3 uintptr) (r1, r2 uintptr, err Errno)
```

```go
func RawSyscall6(trap, a1, a2, a3, a4, a5, a6 uintptr) (r1, r2 uintptr, err Errno)
```

```go
func Syscall(trap, a1, a2, a3 uintptr) (r1, r2 uintptr, err Errno)
```

```go
func Syscall6(trap, a1, a2, a3, a4, a5, a6 uintptr) (r1, r2 uintptr, err Errno)
```

```go
func (e Errno) Error() string
```

```go
func (e Errno) Is(target error) bool
```

```go
func (e Errno) Temporary() bool
```

```go
func (e Errno) Timeout() bool
```

```go
type FdSet struct {
	Bits [16]int64
}
```

```go
type Flock_t struct {
	Type      int16
	Whence    int16
	Pad_cgo_0 [4]byte
	Start     int64
	Len       int64
	Pid       int32
	Pad_cgo_1 [4]byte
}
```

```go
type Fsid struct {
	X__val [2]int32
}
```

```go
type ICMPv6Filter struct {
	Data [8]uint32
}
```
