---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/syscall"
source_path: "sources/raw/external/pkg-go-dev-syscall-cc00f6c0ec.html"
license_ref: ""
---

- Constants

- Variables

-  func Access(path string, mode uint32) (err error)

-  func Acct(path string) (err error)

-  func Adjtimex(buf *Timex) (state int, err error)

-  func AttachLsf(fd int, i []SockFilter) errordeprecated

-  func Bind(fd int, sa Sockaddr) (err error)

-  func BindToDevice(fd int, device string) (err error)

-  func BytePtrFromString(s string) (*byte, error)

-  func ByteSliceFromString(s string) ([]byte, error)

-  func Chdir(path string) (err error)

-  func Chmod(path string, mode uint32) (err error)

-  func Chown(path string, uid int, gid int) (err error)

-  func Chroot(path string) (err error)

-  func Clearenv()

-  func Close(fd int) (err error)

-  func CloseOnExec(fd int)

-  func CmsgLen(datalen int) int

-  func CmsgSpace(datalen int) int

-  func Connect(fd int, sa Sockaddr) (err error)

-  func Creat(path string, mode uint32) (fd int, err error)

-  func DetachLsf(fd int) errordeprecated

-  func Dup(oldfd int) (fd int, err error)

-  func Dup2(oldfd int, newfd int) (err error)

-  func Dup3(oldfd int, newfd int, flags int) (err error)

-  func Environ() []string

-  func EpollCreate(size int) (fd int, err error)

-  func EpollCreate1(flag int) (fd int, err error)

-  func EpollCtl(epfd int, op int, fd int, event *EpollEvent) (err error)

-  func EpollWait(epfd int, events []EpollEvent, msec int) (n int, err error)

-  func Exec(argv0 string, argv []string, envv []string) (err error)

-  func Exit(code int)

-  func Faccessat(dirfd int, path string, mode uint32, flags int) (err error)

-  func Fallocate(fd int, mode uint32, off int64, len int64) (err error)

-  func Fchdir(fd int) (err error)

-  func Fchmod(fd int, mode uint32) (err error)

-  func Fchmodat(dirfd int, path string, mode uint32, flags int) error

-  func Fchown(fd int, uid int, gid int) (err error)

-  func Fchownat(dirfd int, path string, uid int, gid int, flags int) (err error)

-  func FcntlFlock(fd uintptr, cmd int, lk *Flock_t) error

-  func Fdatasync(fd int) (err error)

-  func Flock(fd int, how int) (err error)

-  func ForkExec(argv0 string, argv []string, attr *ProcAttr) (pid int, err error)

-  func Fstat(fd int, stat *Stat_t) (err error)

-  func Fstatfs(fd int, buf *Statfs_t) (err error)

-  func Fsync(fd int) (err error)

-  func Ftruncate(fd int, length int64) (err error)

-  func Futimes(fd int, tv []Timeval) (err error)

-  func Futimesat(dirfd int, path string, tv []Timeval) (err error)

-  func Getcwd(buf []byte) (n int, err error)

-  func Getdents(fd int, buf []byte) (n int, err error)

-  func Getegid() (egid int)

-  func Getenv(key string) (value string, found bool)

-  func Geteuid() (euid int)

-  func Getgid() (gid int)

-  func Getgroups() (gids []int, err error)

-  func Getpagesize() int

-  func Getpgid(pid int) (pgid int, err error)

-  func Getpgrp() (pid int)

-  func Getpid() (pid int)

-  func Getppid() (ppid int)

-  func Getpriority(which int, who int) (prio int, err error)

-  func Getrlimit(resource int, rlim *Rlimit) (err error)

-  func Getrusage(who int, rusage *Rusage) (err error)

-  func GetsockoptInet4Addr(fd, level, opt int) (value [4]byte, err error)

-  func GetsockoptInt(fd, level, opt int) (value int, err error)

-  func Gettid() (tid int)

-  func Gettimeofday(tv *Timeval) (err error)

-  func Getuid() (uid int)

-  func Getwd() (wd string, err error)

-  func Getxattr(path string, attr string, dest []byte) (sz int, err error)

-  func InotifyAddWatch(fd int, pathname string, mask uint32) (watchdesc int, err error)

-  func InotifyInit() (fd int, err error)

-  func InotifyInit1(flags int) (fd int, err error)

-  func InotifyRmWatch(fd int, watchdesc uint32) (success int, err error)

-  func Ioperm(from int, num int, on int) (err error)

-  func Iopl(level int) (err error)

-  func Kill(pid int, sig Signal) (err error)

-  func Klogctl(typ int, buf []byte) (n int, err error)

-  func Lchown(path string, uid int, gid int) (err error)

-  func Link(oldpath string, newpath string) (err error)

-  func Listen(s int, n int) (err error)

-  func Listxattr(path string, dest []byte) (sz int, err error)

-  func LsfSocket(ifindex, proto int) (int, error)deprecated

-  func Lstat(path string, stat *Stat_t) (err error)

-  func Madvise(b []byte, advice int) (err error)

-  func Mkdir(path string, mode uint32) (err error)

-  func Mkdirat(dirfd int, path string, mode uint32) (err error)

-  func Mkfifo(path string, mode uint32) (err error)

-  func Mknod(path string, mode uint32, dev int) (err error)

-  func Mknodat(dirfd int, path string, mode uint32, dev int) (err error)

-  func Mlock(b []byte) (err error)

-  func Mlockall(flags int) (err error)

-  func Mmap(fd int, offset int64, length int, prot int, flags int) (data []byte, err error)

-  func Mount(source string, target string, fstype string, flags uintptr, data string) (err error)

-  func Mprotect(b []byte, prot int) (err error)

-  func Munlock(b []byte) (err error)

-  func Munlockall() (err error)

-  func Munmap(b []byte) (err error)

-  func Nanosleep(time *Timespec, leftover *Timespec) (err error)

-  func NetlinkRIB(proto, family int) ([]byte, error)

-  func Open(path string, mode int, perm uint32) (fd int, err error)

-  func Openat(dirfd int, path string, flags int, mode uint32) (fd int, err error)

-  func ParseDirent(buf []byte, max int, names []string) (consumed int, count int, newnames []string)

-  func ParseUnixRights(m *SocketControlMessage) ([]int, error)

-  func Pause() (err error)

-  func Pipe(p []int) error

-  func Pipe2(p []int, flags int) error

-  func PivotRoot(newroot string, putold string) (err error)

-  func Pread(fd int, p []byte, offset int64) (n int, err error)

-  func PtraceAttach(pid int) (err error)

-  func PtraceCont(pid int, signal int) (err error)

-  func PtraceDetach(pid int) (err error)

-  func PtraceGetEventMsg(pid int) (msg uint, err error)

-  func PtraceGetRegs(pid int, regsout *PtraceRegs) (err error)

-  func PtracePeekData(pid int, addr uintptr, out []byte) (count int, err error)

-  func PtracePeekText(pid int, addr uintptr, out []byte) (count int, err error)

-  func PtracePokeData(pid int, addr uintptr, data []byte) (count int, err error)

-  func PtracePokeText(pid int, addr uintptr, data []byte) (count int, err error)

-  func PtraceSetOptions(pid int, options int) (err error)

-  func PtraceSetRegs(pid int, regs *PtraceRegs) (err error)

-  func PtraceSingleStep(pid int) (err error)

-  func PtraceSyscall(pid int, signal int) (err error)

-  func Pwrite(fd int, p []byte, offset int64) (n int, err error)

-  func Read(fd int, p []byte) (n int, err error)

-  func ReadDirent(fd int, buf []byte) (n int, err error)

-  func Readlink(path string, buf []byte) (n int, err error)

-  func Reboot(cmd int) (err error)

-  func Removexattr(path string, attr string) (err error)

-  func Rename(oldpath string, newpath string) (err error)

-  func Renameat(olddirfd int, oldpath string, newdirfd int, newpath string) (err error)

-  func Rmdir(path string) error

-  func Seek(fd int, offset int64, whence int) (off int64, err error)

-  func Select(nfd int, r *FdSet, w *FdSet, e *FdSet, timeout *Timeval) (n int, err error)

-  func Sendfile(outfd int, infd int, offset *int64, count int) (written int, err error)

-  func Sendmsg(fd int, p, oob []byte, to Sockaddr, flags int) (err error)

-  func SendmsgN(fd int, p, oob []byte, to Sockaddr, flags int) (n int, err error)

-  func Sendto(fd int, p []byte, flags int, to Sockaddr) (err error)

-  func SetLsfPromisc(name string, m bool) errordeprecated

-  func SetNonblock(fd int, nonblocking bool) (err error)

-  func Setdomainname(p []byte) (err error)

-  func Setegid(egid int) (err error)

-  func Setenv(key, value string) error

-  func Seteuid(euid int) (err error)

-  func Setfsgid(gid int) (err error)

-  func Setfsuid(uid int) (err error)

-  func Setgid(gid int) (err error)

-  func Setgroups(gids []int) (err error)

-  func Sethostname(p []byte) (err error)

-  func Setpgid(pid int, pgid int) (err error)

-  func Setpriority(which int, who int, prio int) (err error)

-  func Setregid(rgid, egid int) (err error)

-  func Setresgid(rgid, egid, sgid int) (err error)

-  func Setresuid(ruid, euid, suid int) (err error)

-  func Setreuid(ruid, euid int) (err error)

-  func Setrlimit(resource int, rlim *Rlimit) error

-  func Setsid() (pid int, err error)

-  func SetsockoptByte(fd, level, opt int, value byte) (err error)

-  func SetsockoptICMPv6Filter(fd, level, opt int, filter *ICMPv6Filter) error

-  func SetsockoptIPMreq(fd, level, opt int, mreq *IPMreq) (err error)

-  func SetsockoptIPMreqn(fd, level, opt int, mreq *IPMreqn) (err error)

-  func SetsockoptIPv6Mreq(fd, level, opt int, mreq *IPv6Mreq) (err error)

-  func SetsockoptInet4Addr(fd, level, opt int, value [4]byte) (err error)

-  func SetsockoptInt(fd, level, opt int, value int) (err error)

-  func SetsockoptLinger(fd, level, opt int, l *Linger) (err error)

-  func SetsockoptString(fd, level, opt int, s string) (err error)

-  func SetsockoptTimeval(fd, level, opt int, tv *Timeval) (err error)

-  func Settimeofday(tv *Timeval) (err error)

-  func Setuid(uid int) (err error)

-  func Setxattr(path string, attr string, data []byte, flags int) (err error)

-  func Shutdown(fd int, how int) (err error)

-  func SlicePtrFromStrings(ss []string) ([]*byte, error)

-  func Socket(domain, typ, proto int) (fd int, err error)

-  func Socketpair(domain, typ, proto int) (fd [2]int, err error)

-  func Splice(rfd int, roff *int64, wfd int, woff *int64, len int, flags int) (n int64, err error)

-  func StartProcess(argv0 string, argv []string, attr *ProcAttr) (pid int, handle uintptr, err error)

-  func Stat(path string, stat *Stat_t) (err error)

-  func Statfs(path string, buf *Statfs_t) (err error)

-  func StringBytePtr(s string) *bytedeprecated

-  func StringByteSlice(s string) []bytedeprecated

-  func StringSlicePtr(ss []string) []*bytedeprecated

-  func Symlink(oldpath string, newpath string) (err error)

-  func Sync()

-  func SyncFileRange(fd int, off int64, n int64, flags int) (err error)

-  func Sysinfo(info *Sysinfo_t) (err error)

-  func Tee(rfd int, wfd int, len int, flags int) (n int64, err error)

-  func Tgkill(tgid int, tid int, sig Signal) (err error)

-  func Times(tms *Tms) (ticks uintptr, err error)

-  func TimespecToNsec(ts Timespec) int64

-  func TimevalToNsec(tv Timeval) int64

-  func Truncate(path string, length int64) (err error)

-  func Umask(mask int) (oldmask int)

-  func Uname(buf *Utsname) (err error)

-  func UnixCredentials(ucred *Ucred) []byte
