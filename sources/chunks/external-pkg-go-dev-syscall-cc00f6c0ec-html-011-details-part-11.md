---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/syscall"
source_path: "sources/raw/external/pkg-go-dev-syscall-cc00f6c0ec.html"
license_ref: ""
---

```go
type SysProcAttr struct {
	Chroot     string      // Chroot.
	Credential *Credential // Credential.
	// Ptrace tells the child to call ptrace(PTRACE_TRACEME).
	// Call runtime.LockOSThread before starting a process with this set,
	// and don't call UnlockOSThread until done with PtraceSyscall calls.
	Ptrace bool
	Setsid bool // Create session.
	// Setpgid sets the process group ID of the child to Pgid,
	// or, if Pgid == 0, to the new child's process ID.
	Setpgid bool
	// Setctty sets the controlling terminal of the child to
	// file descriptor Ctty. Ctty must be a descriptor number
	// in the child process: an index into ProcAttr.Files.
	// This is only meaningful if Setsid is true.
	Setctty bool
	Noctty  bool // Detach fd 0 from controlling terminal.
	Ctty    int  // Controlling TTY fd.
	// Foreground places the child process group in the foreground.
	// This implies Setpgid. The Ctty field must be set to
	// the descriptor of the controlling TTY.
	// Unlike Setctty, in this case Ctty must be a descriptor
	// number in the parent process.
	Foreground bool
	Pgid       int // Child's process group ID if Setpgid.
	// Pdeathsig, if non-zero, is a signal that the kernel will send to
	// the child process when the creating thread dies. Note that the signal
	// is sent on thread termination, which may happen before process termination.
	// There are more details at https://go.dev/issue/27505 <https://go.dev/issue/27505>.
	Pdeathsig    Signal
	Cloneflags   uintptr        // Flags for clone calls.
	Unshareflags uintptr        // Flags for unshare calls.
	UidMappings  []SysProcIDMap // User ID mappings for user namespaces.
	GidMappings  []SysProcIDMap // Group ID mappings for user namespaces.
	// GidMappingsEnableSetgroups enabling setgroups syscall.
	// If false, then setgroups syscall will be disabled for the child process.
	// This parameter is no-op if GidMappings == nil. Otherwise for unprivileged
	// users this should be set to false for mappings work.
	GidMappingsEnableSetgroups bool
	AmbientCaps                []uintptr // Ambient capabilities.
	UseCgroupFD                bool      // Whether to make use of the CgroupFD field.
	CgroupFD                   int       // File descriptor of a cgroup to put the new process into.
	// PidFD, if not nil, is used to store the pidfd of a child, if the
	// functionality is supported by the kernel, or -1. Note *PidFD is
	// changed only if the process starts successfully.
	PidFD *int
}
```

```go
type SysProcIDMap struct {
	ContainerID int // Container ID.
	HostID      int // Host ID.
	Size        int // Size.
}
```

SysProcIDMap holds Container ID to Host ID mappings used for User Namespaces in Linux. See user_namespaces(7).

Note that User Namespaces are not available on a number of popular Linux versions (due to security issues), or are available but subject to AppArmor restrictions like in Ubuntu 24.04.

```go
type Sysinfo_t struct {
	Uptime    int64
	Loads     [3]uint64
	Totalram  uint64
	Freeram   uint64
	Sharedram uint64
	Bufferram uint64
	Totalswap uint64
	Freeswap  uint64
	Procs     uint16
	Pad       uint16
	Pad_cgo_0 [4]byte
	Totalhigh uint64
	Freehigh  uint64
	Unit      uint32
	X_f       [0]byte
	Pad_cgo_1 [4]byte
}
```

```go
type TCPInfo struct {
	State          uint8
	Ca_state       uint8
	Retransmits    uint8
	Probes         uint8
	Backoff        uint8
	Options        uint8
	Pad_cgo_0      [2]byte
	Rto            uint32
	Ato            uint32
	Snd_mss        uint32
	Rcv_mss        uint32
	Unacked        uint32
	Sacked         uint32
	Lost           uint32
	Retrans        uint32
	Fackets        uint32
	Last_data_sent uint32
	Last_ack_sent  uint32
	Last_data_recv uint32
	Last_ack_recv  uint32
	Pmtu           uint32
	Rcv_ssthresh   uint32
	Rtt            uint32
	Rttvar         uint32
	Snd_ssthresh   uint32
	Snd_cwnd       uint32
	Advmss         uint32
	Reordering     uint32
	Rcv_rtt        uint32
	Rcv_space      uint32
	Total_retrans  uint32
}
```

```go
type Termios struct {
	Iflag     uint32
	Oflag     uint32
	Cflag     uint32
	Lflag     uint32
	Line      uint8
	Cc        [32]uint8
	Pad_cgo_0 [3]byte
	Ispeed    uint32
	Ospeed    uint32
}
```

```go
type Time_t int64
```

```go
func Time(t *Time_t) (tt Time_t, err error)
```

```go
type Timespec struct {
	Sec  int64
	Nsec int64
}
```

```go
func NsecToTimespec(nsec int64) Timespec
```

NsecToTimespec converts a number of nanoseconds into a Timespec.

```go
func (ts *Timespec) Nano() int64
```

Nano returns the time stored in ts as nanoseconds.

```go
func (ts *Timespec) Unix() (sec int64, nsec int64)
```

Unix returns the time stored in ts as seconds plus nanoseconds.

```go
type Timeval struct {
	Sec  int64
	Usec int64
}
```

```go
func NsecToTimeval(nsec int64) Timeval
```

NsecToTimeval converts a number of nanoseconds into a Timeval.

```go
func (tv *Timeval) Nano() int64
```

Nano returns the time stored in tv as nanoseconds.

```go
func (tv *Timeval) Unix() (sec int64, nsec int64)
```

Unix returns the time stored in tv as seconds plus nanoseconds.

```go
type Timex struct {
	Modes     uint32
	Pad_cgo_0 [4]byte
	Offset    int64
	Freq      int64
	Maxerror  int64
	Esterror  int64
	Status    int32
	Pad_cgo_1 [4]byte
	Constant  int64
	Precision int64
	Tolerance int64
	Time      Timeval
	Tick      int64
	Ppsfreq   int64
	Jitter    int64
	Shift     int32
	Pad_cgo_2 [4]byte
	Stabil    int64
	Jitcnt    int64
	Calcnt    int64
	Errcnt    int64
	Stbcnt    int64
	Tai       int32
	Pad_cgo_3 [44]byte
}
```

```go
type Tms struct {
	Utime  int64
	Stime  int64
	Cutime int64
	Cstime int64
}
```

```go
type Ucred struct {
	Pid int32
	Uid uint32
	Gid uint32
}
```

```go
func GetsockoptUcred(fd, level, opt int) (*Ucred, error)
```

```go
func ParseUnixCredentials(m *SocketControlMessage) (*Ucred, error)
```

ParseUnixCredentials decodes a socket control message that contains credentials in a Ucred structure. To receive such a message, the SO_PASSCRED option must be enabled on the socket.

```go
type Ustat_t struct {
	Tfree     int32
	Pad_cgo_0 [4]byte
	Tinode    uint64
	Fname     [6]int8
	Fpack     [6]int8
	Pad_cgo_1 [4]byte
}
```

```go
type Utimbuf struct {
	Actime  int64
	Modtime int64
}
```

```go
type Utsname struct {
	Sysname    [65]int8
	Nodename   [65]int8
	Release    [65]int8
	Version    [65]int8
	Machine    [65]int8
	Domainname [65]int8
}
```

```go
type WaitStatus uint32
```

```go
func (w WaitStatus) Continued() bool
```

```go
func (w WaitStatus) CoreDump() bool
```

```go
func (w WaitStatus) ExitStatus() int
```

```go
func (w WaitStatus) Exited() bool
```

```go
func (w WaitStatus) Signal() Signal
```

```go
func (w WaitStatus) Signaled() bool
```

```go
func (w WaitStatus) StopSignal() Signal
```

```go
func (w WaitStatus) Stopped() bool
```

```go
func (w WaitStatus) TrapCause() int
```
