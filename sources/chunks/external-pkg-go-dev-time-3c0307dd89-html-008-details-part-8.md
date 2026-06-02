---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/time"
source_path: "sources/raw/external/pkg-go-dev-time-3c0307dd89.html"
license_ref: ""
---

For a chan-based timer created with NewTimer(d), as of Go 1.23, any receive from t.C after Stop has returned is guaranteed to block rather than receive a stale time value from before the Stop; if the program has not received from t.C already and the timer is running, Stop is guaranteed to return true. Before Go 1.23, the only safe way to use Stop was insert an extra <-t.C if Stop returned false to drain a potential stale value. See the NewTimer documentation for more details.

```go
type Weekday int
```

A Weekday specifies a day of the week (Sunday = 0, ...).

```go
const (
	Sunday Weekday = iota
	Monday
	Tuesday
	Wednesday
	Thursday
	Friday
	Saturday
)
```

```go
func (d Weekday) String() string
```

String returns the English name of the day ("Sunday", "Monday", ...).

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/time>

- format.go <https://cs.opensource.google/go/go/+/go1.26.3:src/time/format.go>
- format_rfc3339.go <https://cs.opensource.google/go/go/+/go1.26.3:src/time/format_rfc3339.go>
- sleep.go <https://cs.opensource.google/go/go/+/go1.26.3:src/time/sleep.go>
- sys_unix.go <https://cs.opensource.google/go/go/+/go1.26.3:src/time/sys_unix.go>
- tick.go <https://cs.opensource.google/go/go/+/go1.26.3:src/time/tick.go>
- time.go <https://cs.opensource.google/go/go/+/go1.26.3:src/time/time.go>
- zoneinfo.go <https://cs.opensource.google/go/go/+/go1.26.3:src/time/zoneinfo.go>
- zoneinfo_goroot.go <https://cs.opensource.google/go/go/+/go1.26.3:src/time/zoneinfo_goroot.go>
- zoneinfo_read.go <https://cs.opensource.google/go/go/+/go1.26.3:src/time/zoneinfo_read.go>
- zoneinfo_unix.go <https://cs.opensource.google/go/go/+/go1.26.3:src/time/zoneinfo_unix.go>

##   Directories ¶
    Show internal   Expand all

tzdata
 Package tzdata provides an embedded copy of the timezone database.

Package tzdata provides an embedded copy of the timezone database.

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
