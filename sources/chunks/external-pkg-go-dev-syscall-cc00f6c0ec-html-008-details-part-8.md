---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/syscall"
source_path: "sources/raw/external/pkg-go-dev-syscall-cc00f6c0ec.html"
license_ref: ""
---

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/syscall/ztypes_linux_amd64.go;l=512>
```go
const SizeofInotifyEvent = 0x10
```

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/syscall/syscall_unix.go;l=22>
```go
var (
	Stdin  = 0
	Stdout = 1
	Stderr = 2
)
```

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/syscall/exec_unix.go;l=65>
```go
var ForkLock sync.RWMutex
```

ForkLock is used to synchronize creation of new file descriptors with fork.

We want the child in a fork/exec sequence to inherit only the file descriptors we intend. To do that, we mark all file descriptors close-on-exec and then, in the child, explicitly unmark the ones we want the exec'ed program to keep. Unix doesn't make this easy: there is, in general, no way to allocate a new file descriptor close-on-exec. Instead you have to allocate the descriptor and then mark it close-on-exec. If a fork happens between those two events, the child's exec will inherit an unwanted file descriptor.

This lock solves that race: the create new fd/mark close-on-exec operation is done holding ForkLock for reading, and the fork itself is done holding ForkLock for writing. At least, that's the idea. There are some complications.

Some system calls that create new file descriptors can block for arbitrarily long times: open on a hung NFS server or named pipe, accept on a socket, and so on. We can't reasonably grab the lock across those operations.

It is worse to inherit some file descriptors than others. If a non-malicious child accidentally inherits an open ordinary file, that's not a big deal. On the other hand, if a long-lived child accidentally inherits the write end of a pipe, then the reader of that pipe will not see EOF until that child exits, potentially causing the parent program to hang. This is a common problem in threaded C programs that use popen.

Luckily, the file descriptors that are most important not to inherit are not the ones that can take an arbitrarily long time to create: pipe returns instantly, and the net package uses non-blocking I/O to accept on a listening socket. The rules for which file descriptor-creating operations use the ForkLock are as follows:

- Pipe. Use pipe2 if available. Otherwise, does not block, so use ForkLock.
- Socket. Use SOCK_CLOEXEC if available. Otherwise, does not block, so use ForkLock.
- Open. Use O_CLOEXEC if available. Otherwise, may block, so live with the race.
- Dup. Use F_DUPFD_CLOEXEC or dup3 if available. Otherwise, does not block, so use ForkLock.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/syscall/syscall_unix.go;l=263>
```go
var SocketDisableIPv6 bool
```

For testing: clients can set this flag to force creation of IPv6 sockets to return EAFNOSUPPORT.

```go
func Access(path string, mode uint32) (err error)
```

```go
func Acct(path string) (err error)
```

```go
func Adjtimex(buf *Timex) (state int, err error)
```

```go
func AttachLsf(fd int, i []SockFilter) error
```

Deprecated: Use golang.org/x/net/bpf instead.

```go
func Bind(fd int, sa Sockaddr) (err error)
```

```go
func BindToDevice(fd int, device string) (err error)
```

BindToDevice binds the socket associated with fd to device.

```go
func BytePtrFromString(s string) (*byte, error)
```

BytePtrFromString returns a pointer to a NUL-terminated array of bytes containing the text of s. If s contains a NUL byte at any location, it returns (nil, EINVAL).

```go
func ByteSliceFromString(s string) ([]byte, error)
```

ByteSliceFromString returns a NUL-terminated slice of bytes containing the text of s. If s contains a NUL byte at any location, it returns (nil, EINVAL).

```go
func Chdir(path string) (err error)
```

```go
func Chmod(path string, mode uint32) (err error)
```

```go
func Chown(path string, uid int, gid int) (err error)
```

```go
func Chroot(path string) (err error)
```

```go
func Clearenv()
```

```go
func Close(fd int) (err error)
```

```go
func CloseOnExec(fd int)
```

```go
func CmsgLen(datalen int) int
```

CmsgLen returns the value to store in the Len field of the Cmsghdr structure, taking into account any necessary alignment.

```go
func CmsgSpace(datalen int) int
```

CmsgSpace returns the number of bytes an ancillary element with payload of the passed data length occupies.

```go
func Connect(fd int, sa Sockaddr) (err error)
```

```go
func Creat(path string, mode uint32) (fd int, err error)
```

```go
func DetachLsf(fd int) error
```

Deprecated: Use golang.org/x/net/bpf instead.

```go
func Dup(oldfd int) (fd int, err error)
```

```go
func Dup2(oldfd int, newfd int) (err error)
```

```go
func Dup3(oldfd int, newfd int, flags int) (err error)
```

```go
func Environ() []string
```

```go
func EpollCreate(size int) (fd int, err error)
```

```go
func EpollCreate1(flag int) (fd int, err error)
```

```go
func EpollCtl(epfd int, op int, fd int, event *EpollEvent) (err error)
```

```go
func EpollWait(epfd int, events []EpollEvent, msec int) (n int, err error)
```

```go
func Exec(argv0 string, argv []string, envv []string) (err error)
```

Exec invokes the execve(2) system call.

```go
func Exit(code int)
```

```go
func Faccessat(dirfd int, path string, mode uint32, flags int) (err error)
```

```go
func Fallocate(fd int, mode uint32, off int64, len int64) (err error)
```

```go
func Fchdir(fd int) (err error)
```

```go
func Fchmod(fd int, mode uint32) (err error)
```

```go
func Fchmodat(dirfd int, path string, mode uint32, flags int) error
```

```go
func Fchown(fd int, uid int, gid int) (err error)
```

```go
func Fchownat(dirfd int, path string, uid int, gid int, flags int) (err error)
```

```go
func FcntlFlock(fd uintptr, cmd int, lk *Flock_t) error
```

FcntlFlock performs a fcntl syscall for the F_GETLK, F_SETLK or F_SETLKW command.

```go
func Fdatasync(fd int) (err error)
```

```go
func Flock(fd int, how int) (err error)
```

```go
func ForkExec(argv0 string, argv []string, attr *ProcAttr) (pid int, err error)
```

Combination of fork and exec, careful to be thread safe.

```go
func Fstat(fd int, stat *Stat_t) (err error)
```

```go
func Fstatfs(fd int, buf *Statfs_t) (err error)
```

```go
func Fsync(fd int) (err error)
```

```go
func Ftruncate(fd int, length int64) (err error)
```

```go
func Futimes(fd int, tv []Timeval) (err error)
```

```go
func Futimesat(dirfd int, path string, tv []Timeval) (err error)
```

```go
func Getcwd(buf []byte) (n int, err error)
```

```go
func Getdents(fd int, buf []byte) (n int, err error)
```

```go
func Getegid() (egid int)
```

```go
func Getenv(key string) (value string, found bool)
```

```go
func Geteuid() (euid int)
```

```go
func Getgid() (gid int)
```

```go
func Getgroups() (gids []int, err error)
```

```go
func Getpagesize() int
```

```go
func Getpgid(pid int) (pgid int, err error)
```

```go
func Getpgrp() (pid int)
```

```go
func Getpid() (pid int)
```

```go
func Getppid() (ppid int)
```

```go
func Getpriority(which int, who int) (prio int, err error)
```

```go
func Getrlimit(resource int, rlim *Rlimit) (err error)
```

```go
func Getrusage(who int, rusage *Rusage) (err error)
```

```go
func GetsockoptInet4Addr(fd, level, opt int) (value [4]byte, err error)
```

```go
func GetsockoptInt(fd, level, opt int) (value int, err error)
```

```go
func Gettid() (tid int)
```

```go
func Gettimeofday(tv *Timeval) (err error)
```

```go
func Getuid() (uid int)
```

```go
func Getwd() (wd string, err error)
```

```go
func Getxattr(path string, attr string, dest []byte) (sz int, err error)
```

```go
func InotifyAddWatch(fd int, pathname string, mask uint32) (watchdesc int, err error)
```

```go
func InotifyInit() (fd int, err error)
```

```go
func InotifyInit1(flags int) (fd int, err error)
```

```go
func InotifyRmWatch(fd int, watchdesc uint32) (success int, err error)
```

```go
func Ioperm(from int, num int, on int) (err error)
```

```go
func Iopl(level int) (err error)
```

```go
func Kill(pid int, sig Signal) (err error)
```

```go
func Klogctl(typ int, buf []byte) (n int, err error)
```

```go
func Lchown(path string, uid int, gid int) (err error)
```

```go
func Link(oldpath string, newpath string) (err error)
```

```go
func Listen(s int, n int) (err error)
```

```go
func Listxattr(path string, dest []byte) (sz int, err error)
```

```go
func LsfSocket(ifindex, proto int) (int, error)
```

Deprecated: Use golang.org/x/net/bpf instead.

```go
func Lstat(path string, stat *Stat_t) (err error)
```

```go
func Madvise(b []byte, advice int) (err error)
```

```go
func Mkdir(path string, mode uint32) (err error)
```

```go
func Mkdirat(dirfd int, path string, mode uint32) (err error)
```

```go
func Mkfifo(path string, mode uint32) (err error)
```

```go
func Mknod(path string, mode uint32, dev int) (err error)
```

```go
func Mknodat(dirfd int, path string, mode uint32, dev int) (err error)
```

```go
func Mlock(b []byte) (err error)
```

```go
func Mlockall(flags int) (err error)
```

```go
func Mmap(fd int, offset int64, length int, prot int, flags int) (data []byte, err error)
```

```go
func Mount(source string, target string, fstype string, flags uintptr, data string) (err error)
```

```go
func Mprotect(b []byte, prot int) (err error)
```

```go
func Munlock(b []byte) (err error)
```

```go
func Munlockall() (err error)
```

```go
func Munmap(b []byte) (err error)
```

```go
func Nanosleep(time *Timespec, leftover *Timespec) (err error)
```

```go
func NetlinkRIB(proto, family int) ([]byte, error)
```

NetlinkRIB returns routing information base, as known as RIB, which consists of network facility information, states and parameters.

```go
func Open(path string, mode int, perm uint32) (fd int, err error)
```

```go
func Openat(dirfd int, path string, flags int, mode uint32) (fd int, err error)
```

```go
func ParseDirent(buf []byte, max int, names []string) (consumed int, count int, newnames []string)
```

ParseDirent parses up to max directory entries in buf, appending the names to names. It returns the number of bytes consumed from buf, the number of entries added to names, and the new names slice.

```go
func ParseUnixRights(m *SocketControlMessage) ([]int, error)
```

ParseUnixRights decodes a socket control message that contains an integer array of open file descriptors from another process.

```go
func Pause() (err error)
```

```go
func Pipe(p []int) error
```

```go
func Pipe2(p []int, flags int) error
```

```go
func PivotRoot(newroot string, putold string) (err error)
```
