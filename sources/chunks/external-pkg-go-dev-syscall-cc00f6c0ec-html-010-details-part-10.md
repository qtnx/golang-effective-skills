---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/syscall"
source_path: "sources/raw/external/pkg-go-dev-syscall-cc00f6c0ec.html"
license_ref: ""
---

```go
func GetsockoptICMPv6Filter(fd, level, opt int) (*ICMPv6Filter, error)
```

```go
type IPMreq struct {
	Multiaddr [4]byte /* in_addr */
	Interface [4]byte /* in_addr */
}
```

```go
func GetsockoptIPMreq(fd, level, opt int) (*IPMreq, error)
```

```go
type IPMreqn struct {
	Multiaddr [4]byte /* in_addr */
	Address   [4]byte /* in_addr */
	Ifindex   int32
}
```

```go
func GetsockoptIPMreqn(fd, level, opt int) (*IPMreqn, error)
```

```go
type IPv6MTUInfo struct {
	Addr RawSockaddrInet6
	Mtu  uint32
}
```

```go
func GetsockoptIPv6MTUInfo(fd, level, opt int) (*IPv6MTUInfo, error)
```

```go
type IPv6Mreq struct {
	Multiaddr [16]byte /* in6_addr */
	Interface uint32
}
```

```go
func GetsockoptIPv6Mreq(fd, level, opt int) (*IPv6Mreq, error)
```

```go
type IfAddrmsg struct {
	Family    uint8
	Prefixlen uint8
	Flags     uint8
	Scope     uint8
	Index     uint32
}
```

```go
type IfInfomsg struct {
	Family     uint8
	X__ifi_pad uint8
	Type       uint16
	Index      int32
	Flags      uint32
	Change     uint32
}
```

```go
type Inet4Pktinfo struct {
	Ifindex  int32
	Spec_dst [4]byte /* in_addr */
	Addr     [4]byte /* in_addr */
}
```

```go
type Inet6Pktinfo struct {
	Addr    [16]byte /* in6_addr */
	Ifindex uint32
}
```

```go
type InotifyEvent struct {
	Wd     int32
	Mask   uint32
	Len    uint32
	Name   [0]uint8
}
```

```go
type Iovec struct {
	Base *byte
	Len  uint64
}
```

```go
func (iov *Iovec) SetLen(length int)
```

```go
type Linger struct {
	Onoff  int32
	Linger int32
}
```

```go
type Msghdr struct {
	Name       *byte
	Namelen    uint32
	Pad_cgo_0  [4]byte
	Iov        *Iovec
	Iovlen     uint64
	Control    *byte
	Controllen uint64
	Flags      int32
	Pad_cgo_1  [4]byte
}
```

```go
func (msghdr *Msghdr) SetControllen(length int)
```

```go
type NetlinkMessage struct {
	Data   []byte
}
```

NetlinkMessage represents a netlink message.

```go
func ParseNetlinkMessage(b []byte) ([]NetlinkMessage, error)
```

ParseNetlinkMessage parses b as an array of netlink messages and returns the slice containing the NetlinkMessage structures.

```go
type NetlinkRouteAttr struct {
	Attr  RtAttr
	Value []byte
}
```

NetlinkRouteAttr represents a netlink route attribute.

```go
func ParseNetlinkRouteAttr(m *NetlinkMessage) ([]NetlinkRouteAttr, error)
```

ParseNetlinkRouteAttr parses m's payload as an array of netlink route attributes and returns the slice containing the NetlinkRouteAttr structures.

```go
type NetlinkRouteRequest struct {
	Data   RtGenmsg
}
```

NetlinkRouteRequest represents a request message to receive routing and link states from the kernel.

```go
type NlAttr struct {
	Len  uint16
	Type uint16
}
```

```go
type NlMsgerr struct {
	Error int32
	Msg   NlMsghdr
}
```

```go
type NlMsghdr struct {
	Len   uint32
	Type  uint16
	Flags uint16
	Seq   uint32
	Pid   uint32
}
```

```go
type ProcAttr struct {
	Dir   string    // Current working directory.
	Env   []string  // Environment.
	Files []uintptr // File descriptors.
	Sys   *SysProcAttr
}
```

ProcAttr holds attributes that will be applied to a new process started by StartProcess.

```go
type PtraceRegs struct {
	R15      uint64
	R14      uint64
	R13      uint64
	R12      uint64
	Rbp      uint64
	Rbx      uint64
	R11      uint64
	R10      uint64
	R9       uint64
	R8       uint64
	Rax      uint64
	Rcx      uint64
	Rdx      uint64
	Rsi      uint64
	Rdi      uint64
	Orig_rax uint64
	Rip      uint64
	Cs       uint64
	Eflags   uint64
	Rsp      uint64
	Ss       uint64
	Fs_base  uint64
	Gs_base  uint64
	Ds       uint64
	Es       uint64
	Fs       uint64
	Gs       uint64
}
```

```go
func (r *PtraceRegs) PC() uint64
```

```go
func (r *PtraceRegs) SetPC(pc uint64)
```

```go
type RawConn interface {
	// Control invokes f on the underlying connection's file
	// descriptor or handle.
	// The file descriptor fd is guaranteed to remain valid while
	// f executes but not after f returns.
	Control(f func(fd uintptr)) error

// Read invokes f on the underlying connection's file
	// descriptor or handle; f is expected to try to read from the
	// file descriptor.
	// If f returns true, Read returns. Otherwise Read blocks
	// waiting for the connection to be ready for reading and
	// tries again repeatedly.
	// The file descriptor is guaranteed to remain valid while f
	// executes but not after f returns.
	Read(f func(fd uintptr) (done bool)) error

// Write is like Read but for writing.
	Write(f func(fd uintptr) (done bool)) error
}
```

A RawConn is a raw network connection.

```go
type RawSockaddr struct {
	Family uint16
	Data   [14]int8
}
```

```go
type RawSockaddrAny struct {
	Addr RawSockaddr
	Pad  [96]int8
}
```

```go
type RawSockaddrInet4 struct {
	Family uint16
	Port   uint16
	Addr   [4]byte /* in_addr */
	Zero   [8]uint8
}
```

```go
type RawSockaddrInet6 struct {
	Family   uint16
	Port     uint16
	Flowinfo uint32
	Addr     [16]byte /* in6_addr */
	Scope_id uint32
}
```

```go
type RawSockaddrLinklayer struct {
	Family   uint16
	Protocol uint16
	Ifindex  int32
	Hatype   uint16
	Pkttype  uint8
	Halen    uint8
	Addr     [8]uint8
}
```

```go
type RawSockaddrNetlink struct {
	Family uint16
	Pad    uint16
	Pid    uint32
	Groups uint32
}
```

```go
type RawSockaddrUnix struct {
	Family uint16
	Path   [108]int8
}
```

```go
type Rlimit struct {
	Cur uint64
	Max uint64
}
```

```go
type RtAttr struct {
	Len  uint16
	Type uint16
}
```

```go
type RtGenmsg struct {
	Family uint8
}
```

```go
type RtMsg struct {
	Family   uint8
	Dst_len  uint8
	Src_len  uint8
	Tos      uint8
	Table    uint8
	Protocol uint8
	Scope    uint8
	Type     uint8
	Flags    uint32
}
```

```go
type RtNexthop struct {
	Len     uint16
	Flags   uint8
	Hops    uint8
	Ifindex int32
}
```

```go
type Rusage struct {
	Utime    Timeval
	Stime    Timeval
	Maxrss   int64
	Ixrss    int64
	Idrss    int64
	Isrss    int64
	Minflt   int64
	Majflt   int64
	Nswap    int64
	Inblock  int64
	Oublock  int64
	Msgsnd   int64
	Msgrcv   int64
	Nsignals int64
	Nvcsw    int64
	Nivcsw   int64
}
```

```go
type Signal int
```

A Signal is a number describing a process signal. It implements the os.Signal interface.

```go
func (s Signal) Signal()
```

```go
func (s Signal) String() string
```

```go
type SockFilter struct {
	Code uint16
	Jt   uint8
	Jf   uint8
	K    uint32
}
```

```go
func LsfJump(code, k, jt, jf int) *SockFilter
```

Deprecated: Use golang.org/x/net/bpf instead.

```go
func LsfStmt(code, k int) *SockFilter
```

Deprecated: Use golang.org/x/net/bpf instead.

```go
type SockFprog struct {
	Len       uint16
	Pad_cgo_0 [6]byte
	Filter    *SockFilter
}
```

```go
type Sockaddr interface {
	// contains filtered or unexported methods
}
```

```go
func Accept(fd int) (nfd int, sa Sockaddr, err error)
```

```go
func Accept4(fd int, flags int) (nfd int, sa Sockaddr, err error)
```

```go
func Getpeername(fd int) (sa Sockaddr, err error)
```

```go
func Getsockname(fd int) (sa Sockaddr, err error)
```

```go
func Recvfrom(fd int, p []byte, flags int) (n int, from Sockaddr, err error)
```

```go
func Recvmsg(fd int, p, oob []byte, flags int) (n, oobn int, recvflags int, from Sockaddr, err error)
```

```go
type SockaddrInet4 struct {
	Port int
	Addr [4]byte
	// contains filtered or unexported fields
}
```

```go
type SockaddrInet6 struct {
	Port   int
	ZoneId uint32
	Addr   [16]byte
	// contains filtered or unexported fields
}
```

```go
type SockaddrLinklayer struct {
	Protocol uint16
	Ifindex  int
	Hatype   uint16
	Pkttype  uint8
	Halen    uint8
	Addr     [8]byte
	// contains filtered or unexported fields
}
```

```go
type SockaddrNetlink struct {
	Family uint16
	Pad    uint16
	Pid    uint32
	Groups uint32
	// contains filtered or unexported fields
}
```

```go
type SockaddrUnix struct {
	Name string
	// contains filtered or unexported fields
}
```

```go
type SocketControlMessage struct {
	Data   []byte
}
```

SocketControlMessage represents a socket control message.

```go
func ParseSocketControlMessage(b []byte) ([]SocketControlMessage, error)
```

ParseSocketControlMessage parses b as an array of socket control messages.

```go
type Stat_t struct {
	Dev       uint64
	Ino       uint64
	Nlink     uint64
	Mode      uint32
	Uid       uint32
	Gid       uint32
	X__pad0   int32
	Rdev      uint64
	Size      int64
	Blksize   int64
	Blocks    int64
	Atim      Timespec
	Mtim      Timespec
	Ctim      Timespec
	X__unused [3]int64
}
```

```go
type Statfs_t struct {
	Type    int64
	Bsize   int64
	Blocks  uint64
	Bfree   uint64
	Bavail  uint64
	Files   uint64
	Ffree   uint64
	Fsid    Fsid
	Namelen int64
	Frsize  int64
	Flags   int64
	Spare   [4]int64
}
```
