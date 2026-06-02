---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/time"
source_path: "sources/raw/external/pkg-go-dev-time-3c0307dd89.html"
license_ref: ""
---

func main() {
	timeWithNanoseconds := time.Date(2000, 2, 1, 12, 13, 14, 15, time.UTC)
	withNanoseconds := timeWithNanoseconds.String()

timeWithoutNanoseconds := time.Date(2000, 2, 1, 12, 13, 14, 0, time.UTC)
	withoutNanoseconds := timeWithoutNanoseconds.String()

fmt.Printf("withNanoseconds = %v\n", withNanoseconds)
	fmt.Printf("withoutNanoseconds = %v\n", withoutNanoseconds)

}

```

```go
Output:
withNanoseconds = 2000-02-01 12:13:14.000000015 +0000 UTC
withoutNanoseconds = 2000-02-01 12:13:14 +0000 UTC

```

Share Format Run

```go
func (t Time) Sub(u Time) Duration
```

Sub returns the duration t-u. If the result exceeds the maximum (or minimum) value that can be stored in a Duration, the maximum (or minimum) duration will be returned. To compute t-d for a duration d, use t.Add(-d).

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Date(2000, 1, 1, 0, 0, 0, 0, time.UTC)
	end := time.Date(2000, 1, 1, 12, 0, 0, 0, time.UTC)

difference := end.Sub(start)
	fmt.Printf("difference = %v\n", difference)

}

```

```go
Output:
difference = 12h0m0s

```

Share Format Run

```go
func (t Time) Truncate(d Duration) Time
```

Truncate returns the result of rounding t down to a multiple of d (since the zero time). If d <= 0, Truncate returns t stripped of any monotonic clock reading but otherwise unchanged.

Truncate operates on the time as an absolute duration since the zero time; it does not operate on the presentation form of the time. Thus, Truncate(Hour) may return a time with a non-zero minute, depending on the time's Location.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	t, _ := time.Parse("2006 Jan 02 15:04:05", "2012 Dec 07 12:15:30.918273645")
	trunc := []time.Duration{
		time.Nanosecond,
		time.Microsecond,
		time.Millisecond,
		time.Second,
		2 * time.Second,
		time.Minute,
		10 * time.Minute,
	}

for _, d := range trunc {
		fmt.Printf("t.Truncate(%5s) = %s\n", d, t.Truncate(d).Format("15:04:05.999999999"))
	}
	// To round to the last midnight in the local timezone, create a new Date.
	midnight := time.Date(t.Year(), t.Month(), t.Day(), 0, 0, 0, 0, time.Local)
	_ = midnight

}

```

```go
Output:
t.Truncate(  1ns) = 12:15:30.918273645
t.Truncate(  1µs) = 12:15:30.918273
t.Truncate(  1ms) = 12:15:30.918
t.Truncate(   1s) = 12:15:30
t.Truncate(   2s) = 12:15:30
t.Truncate( 1m0s) = 12:15:00
t.Truncate(10m0s) = 12:10:00

```

Share Format Run

```go
func (t Time) UTC() Time
```

UTC returns t with the location set to UTC.

```go
func (t Time) Unix() int64
```

Unix returns t as a Unix time, the number of seconds elapsed since January 1, 1970 UTC. The result does not depend on the location associated with t. Unix-like operating systems often record time as a 32-bit count of seconds, but since the method here returns a 64-bit value it is valid for billions of years into the past or future.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	// 1 billion seconds of Unix, three ways.
	fmt.Println(time.Unix(1e9, 0).UTC())     // 1e9 seconds
	fmt.Println(time.Unix(0, 1e18).UTC())    // 1e18 nanoseconds
	fmt.Println(time.Unix(2e9, -1e18).UTC()) // 2e9 seconds - 1e18 nanoseconds

t := time.Date(2001, time.September, 9, 1, 46, 40, 0, time.UTC)
	fmt.Println(t.Unix())     // seconds since 1970
	fmt.Println(t.UnixNano()) // nanoseconds since 1970

}

```

```go
Output:
2001-09-09 01:46:40 +0000 UTC
2001-09-09 01:46:40 +0000 UTC
2001-09-09 01:46:40 +0000 UTC
1000000000
1000000000000000000

```

Share Format Run

```go
func (t Time) UnixMicro() int64
```

UnixMicro returns t as a Unix time, the number of microseconds elapsed since January 1, 1970 UTC. The result is undefined if the Unix time in microseconds cannot be represented by an int64 (a date before year -290307 or after year 294246). The result does not depend on the location associated with t.

```go
func (t Time) UnixMilli() int64
```

UnixMilli returns t as a Unix time, the number of milliseconds elapsed since January 1, 1970 UTC. The result is undefined if the Unix time in milliseconds cannot be represented by an int64 (a date more than 292 million years before or after 1970). The result does not depend on the location associated with t.

```go
func (t Time) UnixNano() int64
```

UnixNano returns t as a Unix time, the number of nanoseconds elapsed since January 1, 1970 UTC. The result is undefined if the Unix time in nanoseconds cannot be represented by an int64 (a date before the year 1678 or after 2262). Note that this means the result of calling UnixNano on the zero Time is undefined. The result does not depend on the location associated with t.

```go
func (t *Time) UnmarshalBinary(data []byte) error
```

UnmarshalBinary implements the encoding.BinaryUnmarshaler interface.

```go
func (t *Time) UnmarshalJSON(data []byte) error
```

UnmarshalJSON implements the encoding/json.Unmarshaler interface. The time must be a quoted string in the RFC 3339 <https://rfc-editor.org/rfc/rfc3339.html> format.

```go
func (t *Time) UnmarshalText(data []byte) error
```

UnmarshalText implements the encoding.TextUnmarshaler interface. The time must be in the RFC 3339 <https://rfc-editor.org/rfc/rfc3339.html> format.

```go
func (t Time) Weekday() Weekday
```

Weekday returns the day of the week specified by t.

```go
func (t Time) Year() int
```

Year returns the year in which t occurs.

```go
func (t Time) YearDay() int
```

YearDay returns the day of the year specified by t, in the range [1,365] for non-leap years, and [1,366] in leap years.

```go
func (t Time) Zone() (name string, offset int)
```

Zone computes the time zone in effect at time t, returning the abbreviated name of the zone (such as "CET") and its offset in seconds east of UTC.

```go
func (t Time) ZoneBounds() (start, end Time)
```

ZoneBounds returns the bounds of the time zone in effect at time t. The zone begins at start and the next zone begins at end. If the zone begins at the beginning of time, start will be returned as a zero Time. If the zone goes on forever, end will be returned as a zero Time. The Location of the returned times will be the same as t.

```go
type Timer struct {
	C <-chan Time
	// contains filtered or unexported fields
}
```

The Timer type represents a single event. When the Timer expires, the current time will be sent on C, unless the Timer was created by AfterFunc. A Timer must be created with NewTimer or AfterFunc.

```go
func AfterFunc(d Duration, f func()) *Timer
```

AfterFunc waits for the duration to elapse and then calls f in its own goroutine. It returns a Timer that can be used to cancel the call using its Stop method. The returned Timer's C field is not used and will be nil.

```go
func NewTimer(d Duration) *Timer
```

NewTimer creates a new Timer that will send the current time on its channel after at least duration d.

Before Go 1.23, the garbage collector did not recover timers that had not yet expired or been stopped, so code often immediately deferred t.Stop after calling NewTimer, to make the timer recoverable when it was no longer needed. As of Go 1.23, the garbage collector can recover unreferenced timers, even if they haven't expired or been stopped. The Stop method is no longer necessary to help the garbage collector. (Code may of course still want to call Stop to stop the timer for other reasons.)

Before Go 1.23, the channel associated with a Timer was asynchronous (buffered, capacity 1), which meant that stale time values could be received even after Timer.Stop or Timer.Reset returned. As of Go 1.23, the channel is synchronous (unbuffered, capacity 0), eliminating the possibility of those stale values.

The GODEBUG setting asynctimerchan=1 restores both pre-Go 1.23 behaviors: when set, unexpired timers won't be garbage collected, and channels will have buffered capacity. This setting may be removed in Go 1.27 or later.

```go
func (t *Timer) Reset(d Duration) bool
```

Reset changes the timer to expire after duration d. It returns true if the timer had been active, false if the timer had expired or been stopped.

For a func-based timer created with AfterFunc(d, f), Reset either reschedules when f will run, in which case Reset returns true, or schedules f to run again, in which case it returns false. When Reset returns false, Reset neither waits for the prior f to complete before returning nor does it guarantee that the subsequent goroutine running f does not run concurrently with the prior one. If the caller needs to know whether the prior execution of f is completed, it must coordinate with f explicitly.

For a chan-based timer created with NewTimer, as of Go 1.23, any receive from t.C after Reset has returned is guaranteed not to receive a time value corresponding to the previous timer settings; if the program has not received from t.C already and the timer is running, Reset is guaranteed to return true. Before Go 1.23, the only safe way to use Reset was to call Timer.Stop and explicitly drain the timer first. See the NewTimer documentation for more details.

```go
func (t *Timer) Stop() bool
```

Stop prevents the Timer from firing. It returns true if the call stops the timer, false if the timer has already expired or been stopped.

For a func-based timer created with AfterFunc(d, f), if t.Stop returns false, then the timer has already expired and the function f has been started in its own goroutine; Stop does not wait for f to complete before returning. If the caller needs to know whether f is completed, it must coordinate with f explicitly.
