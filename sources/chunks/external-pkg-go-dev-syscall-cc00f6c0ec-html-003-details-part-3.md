---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/syscall"
source_path: "sources/raw/external/pkg-go-dev-syscall-cc00f6c0ec.html"
license_ref: ""
---

-  func UnixRights(fds ...int) []byte
-  func Unlink(path string) error
-  func Unlinkat(dirfd int, path string) error
-  func Unmount(target string, flags int) (err error)
-  func Unsetenv(key string) error
-  func Unshare(flags int) (err error)
-  func Ustat(dev int, ubuf *Ustat_t) (err error)
-  func Utime(path string, buf *Utimbuf) (err error)
-  func Utimes(path string, tv []Timeval) (err error)
-  func UtimesNano(path string, ts []Timespec) (err error)
-  func Wait4(pid int, wstatus *WaitStatus, options int, rusage *Rusage) (wpid int, err error)
-  func Write(fd int, p []byte) (n int, err error)
-  type Cmsghdr
-
-  func (cmsg *Cmsghdr) SetLen(length int)

-  type Conn
-  type Credential
-  type Dirent
-  type EpollEvent
-  type Errno
-
-  func AllThreadsSyscall(trap, a1, a2, a3 uintptr) (r1, r2 uintptr, err Errno)
-  func AllThreadsSyscall6(trap, a1, a2, a3, a4, a5, a6 uintptr) (r1, r2 uintptr, err Errno)
-  func RawSyscall(trap, a1, a2, a3 uintptr) (r1, r2 uintptr, err Errno)
-  func RawSyscall6(trap, a1, a2, a3, a4, a5, a6 uintptr) (r1, r2 uintptr, err Errno)
-  func Syscall(trap, a1, a2, a3 uintptr) (r1, r2 uintptr, err Errno)
-  func Syscall6(trap, a1, a2, a3, a4, a5, a6 uintptr) (r1, r2 uintptr, err Errno)

-
-  func (e Errno) Error() string
-  func (e Errno) Is(target error) bool
-  func (e Errno) Temporary() bool
-  func (e Errno) Timeout() bool

-  type FdSet
-  type Flock_t
-  type Fsid
-  type ICMPv6Filter
-
-  func GetsockoptICMPv6Filter(fd, level, opt int) (*ICMPv6Filter, error)

-  type IPMreq
-
-  func GetsockoptIPMreq(fd, level, opt int) (*IPMreq, error)

-  type IPMreqn
-
-  func GetsockoptIPMreqn(fd, level, opt int) (*IPMreqn, error)

-  type IPv6MTUInfo
-
-  func GetsockoptIPv6MTUInfo(fd, level, opt int) (*IPv6MTUInfo, error)

-  type IPv6Mreq
-
-  func GetsockoptIPv6Mreq(fd, level, opt int) (*IPv6Mreq, error)

-  type IfAddrmsg
-  type IfInfomsg
-  type Inet4Pktinfo
-  type Inet6Pktinfo
-  type InotifyEvent
-  type Iovec
-
-  func (iov *Iovec) SetLen(length int)

-  type Linger
-  type Msghdr
-
-  func (msghdr *Msghdr) SetControllen(length int)

-  type NetlinkMessage
-
-  func ParseNetlinkMessage(b []byte) ([]NetlinkMessage, error)

-  type NetlinkRouteAttr
-
-  func ParseNetlinkRouteAttr(m *NetlinkMessage) ([]NetlinkRouteAttr, error)

-  type NetlinkRouteRequest
-  type NlAttr
-  type NlMsgerr
-  type NlMsghdr
-  type ProcAttr
-  type PtraceRegs
-
-  func (r *PtraceRegs) PC() uint64
-  func (r *PtraceRegs) SetPC(pc uint64)

-  type RawConn
-  type RawSockaddr
-  type RawSockaddrAny
-  type RawSockaddrInet4
-  type RawSockaddrInet6
-  type RawSockaddrLinklayer
-  type RawSockaddrNetlink
-  type RawSockaddrUnix
-  type Rlimit
-  type RtAttr
-  type RtGenmsg
-  type RtMsg
-  type RtNexthop
-  type Rusage
-  type Signal
-
-  func (s Signal) Signal()
-  func (s Signal) String() string

-  type SockFilter
-
-  func LsfJump(code, k, jt, jf int) *SockFilterdeprecated
-  func LsfStmt(code, k int) *SockFilterdeprecated

-  type SockFprog
-  type Sockaddr
-
-  func Accept(fd int) (nfd int, sa Sockaddr, err error)
-  func Accept4(fd int, flags int) (nfd int, sa Sockaddr, err error)
-  func Getpeername(fd int) (sa Sockaddr, err error)
-  func Getsockname(fd int) (sa Sockaddr, err error)
-  func Recvfrom(fd int, p []byte, flags int) (n int, from Sockaddr, err error)
-  func Recvmsg(fd int, p, oob []byte, flags int) (n, oobn int, recvflags int, from Sockaddr, err error)

-  type SockaddrInet4
-  type SockaddrInet6
-  type SockaddrLinklayer
-  type SockaddrNetlink
-  type SockaddrUnix
-  type SocketControlMessage
-
-  func ParseSocketControlMessage(b []byte) ([]SocketControlMessage, error)

-  type Stat_t
-  type Statfs_t
-  type SysProcAttr
-  type SysProcIDMap
-  type Sysinfo_t
-  type TCPInfo
-  type Termios
-  type Time_t
-
-  func Time(t *Time_t) (tt Time_t, err error)

-  type Timespec
-
-  func NsecToTimespec(nsec int64) Timespec

-
-  func (ts *Timespec) Nano() int64
-  func (ts *Timespec) Unix() (sec int64, nsec int64)

-  type Timeval
-
-  func NsecToTimeval(nsec int64) Timeval

-
-  func (tv *Timeval) Nano() int64
-  func (tv *Timeval) Unix() (sec int64, nsec int64)

-  type Timex
-  type Tms
-  type Ucred
-
-  func GetsockoptUcred(fd, level, opt int) (*Ucred, error)
-  func ParseUnixCredentials(m *SocketControlMessage) (*Ucred, error)

-  type Ustat_t
-  type Utimbuf
-  type Utsname
-  type WaitStatus
-
-  func (w WaitStatus) Continued() bool
-  func (w WaitStatus) CoreDump() bool
-  func (w WaitStatus) ExitStatus() int
-  func (w WaitStatus) Exited() bool
-  func (w WaitStatus) Signal() Signal
-  func (w WaitStatus) Signaled() bool
-  func (w WaitStatus) StopSignal() Signal
-  func (w WaitStatus) Stopped() bool
-  func (w WaitStatus) TrapCause() int

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/syscall/exec_linux.go;l=18>
```go
const (
	CLONE_VM             = 0x00000100 // set if VM shared between processes
	CLONE_FS             = 0x00000200 // set if fs info shared between processes
	CLONE_FILES          = 0x00000400 // set if open files shared between processes
	CLONE_SIGHAND        = 0x00000800 // set if signal handlers and blocked signals shared
	CLONE_PIDFD          = 0x00001000 // set if a pidfd should be placed in parent
	CLONE_PTRACE         = 0x00002000 // set if we want to let tracing continue on the child too
	CLONE_VFORK          = 0x00004000 // set if the parent wants the child to wake it up on mm_release
	CLONE_PARENT         = 0x00008000 // set if we want to have the same parent as the cloner
	CLONE_THREAD         = 0x00010000 // Same thread group?
	CLONE_NEWNS          = 0x00020000 // New mount namespace group
	CLONE_SYSVSEM        = 0x00040000 // share system V SEM_UNDO semantics
	CLONE_SETTLS         = 0x00080000 // create a new TLS for the child
	CLONE_PARENT_SETTID  = 0x00100000 // set the TID in the parent
	CLONE_CHILD_CLEARTID = 0x00200000 // clear the TID in the child
	CLONE_DETACHED       = 0x00400000 // Unused, ignored
	CLONE_UNTRACED       = 0x00800000 // set if the tracing process can't force CLONE_PTRACE on this clone
	CLONE_CHILD_SETTID   = 0x01000000 // set the TID in the child
	CLONE_NEWCGROUP      = 0x02000000 // New cgroup namespace
	CLONE_NEWUTS         = 0x04000000 // New utsname namespace
	CLONE_NEWIPC         = 0x08000000 // New ipc namespace
	CLONE_NEWUSER        = 0x10000000 // New user namespace
	CLONE_NEWPID         = 0x20000000 // New pid namespace
	CLONE_NEWNET         = 0x40000000 // New network namespace
	CLONE_IO             = 0x80000000 // Clone io context

CLONE_CLEAR_SIGHAND = 0x100000000 // Clear any signal handler and reset to SIG_DFL.
	CLONE_INTO_CGROUP   = 0x200000000 // Clone into a specific cgroup given the right permissions.

CLONE_NEWTIME = 0x00000080 // New time namespace
)
```
