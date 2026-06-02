---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/time"
source_path: "sources/raw/external/pkg-go-dev-time-3c0307dd89.html"
license_ref: ""
---

(January 2, 15:04:05, 2006, in time zone seven hours west of GMT). That value is recorded as the constant named Layout, listed below. As a Unix time, this is 1136239445. Since MST is GMT-0700, the reference would be printed by the Unix date command as:

```go
Mon Jan 2 15:04:05 MST 2006

```

It is a regrettable historic error that the date uses the American convention of putting the numerical month before the day.

The example for Time.Format demonstrates the working of the layout string in detail and is a good reference.

Note that the RFC822, RFC850, and RFC1123 formats should be applied only to local times. Applying them to UTC times will use "UTC" as the time zone abbreviation, while strictly speaking those RFCs require the use of "GMT" in that case. When using the RFC1123 or RFC1123Z formats for parsing, note that these formats define a leading zero for the day-in-month portion, which is not strictly allowed by RFC 1123 <https://rfc-editor.org/rfc/rfc1123.html>. This will result in an error when parsing date strings that occur in the first 9 days of a given month. In general RFC1123Z should be used instead of RFC1123 for servers that insist on that format, and RFC3339 should be preferred for new protocols. RFC3339, RFC822, RFC822Z, RFC1123, and RFC1123Z are useful for formatting; when used with time.Parse they do not accept all the time formats permitted by the RFCs and they do accept time formats not formally defined. The RFC3339Nano format removes trailing zeros from the seconds field and thus may not sort correctly once formatted.

Most programs can use one of the defined constants as the layout passed to Format or Parse. The rest of this comment can be ignored unless you are creating a custom layout string.

To define your own format, write down what the reference time would look like formatted your way; see the values of constants like ANSIC, StampMicro or Kitchen for examples. The model is to demonstrate what the reference time looks like so that the Format and Parse methods can apply the same transformation to a general time value.

Here is a summary of the components of a layout string. Each element shows by example the formatting of an element of the reference time. Only these values are recognized. Text in the layout string that is not recognized as part of the reference time is echoed verbatim during Format and expected to appear verbatim in the input to Parse.

```go
Year: "2006" "06"
Month: "Jan" "January" "01" "1"
Day of the week: "Mon" "Monday"
Day of the month: "2" "_2" "02"
Day of the year: "__2" "002"
Hour: "15" "3" "03" (PM or AM)
Minute: "4" "04"
Second: "5" "05"
AM/PM mark: "PM"

```

Numeric time zone offsets format as follows:

```go
"-0700"     ±hhmm
"-07:00"    ±hh:mm
"-07"       ±hh
"-070000"   ±hhmmss
"-07:00:00" ±hh:mm:ss

```

Replacing the sign in the format with a Z triggers the ISO 8601 behavior of printing Z instead of an offset for the UTC zone. Thus:

```go
"Z0700"      Z or ±hhmm
"Z07:00"     Z or ±hh:mm
"Z07"        Z or ±hh
"Z070000"    Z or ±hhmmss
"Z07:00:00"  Z or ±hh:mm:ss

```

Within the format string, the underscores in "_2" and "__2" represent spaces that may be replaced by digits if the following number has multiple digits, for compatibility with fixed-width Unix time formats. A leading zero represents a zero-padded value.

The formats __2 and 002 are space-padded and zero-padded three-character day of year; there is no unpadded day of year format.

A comma or decimal point followed by one or more zeros represents a fractional second, printed to the given number of decimal places. A comma or decimal point followed by one or more nines represents a fractional second, printed to the given number of decimal places, with trailing zeros removed. For example "15:04:05,000" or "15:04:05.000" formats or parses with millisecond precision.

Some valid layouts are invalid time values for time.Parse, due to formats such as _ for space padding and Z for zone information.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/time/time.go;l=934>
```go
const (
	Nanosecond  Duration = 1
	Microsecond          = 1000 * Nanosecond
	Millisecond          = 1000 * Microsecond
	Second               = 1000 * Millisecond
	Minute               = 60 * Second
	Hour                 = 60 * Minute
)
```

Common durations. There is no definition for units of Day or larger to avoid confusion across daylight savings time zone transitions.

To count the number of units in a Duration, divide:

```go
second := time.Second
fmt.Print(int64(second/time.Millisecond)) // prints 1000

```

To convert an integer number of units to a Duration, multiply:

```go
seconds := 10
fmt.Print(time.Duration(seconds)*time.Second) // prints 10s

```

This section is empty.

```go
func After(d Duration) <-chan Time
```

After waits for the duration to elapse and then sends the current time on the returned channel. It is equivalent to NewTimer(d).C.

Before Go 1.23, this documentation warned that the underlying Timer would not be recovered by the garbage collector until the timer fired, and that if efficiency was a concern, code should use NewTimer instead and call Timer.Stop if the timer is no longer needed. As of Go 1.23, the garbage collector can recover unreferenced, unstopped timers. There is no reason to prefer NewTimer when After will do.

```go

package main

import (
	"fmt"
	"time"
)

var c chan int

func handle(int) {}

func main() {
	select {
	case m := <-c:
		handle(m)
	case <-time.After(10 * time.Second):
		fmt.Println("timed out")
	}
}

```

```go
Output:

```

Share Format Run

```go
func Sleep(d Duration)
```

Sleep pauses the current goroutine for at least the duration d. A negative or zero duration causes Sleep to return immediately.

```go

package main

import (
	"time"
)

func main() {
	time.Sleep(100 * time.Millisecond)
}

```

```go
Output:

```

Share Format Run

```go
func Tick(d Duration) <-chan Time
```

Tick is a convenience wrapper for NewTicker providing access to the ticking channel only. Unlike NewTicker, Tick will return nil if d <= 0.

Before Go 1.23, this documentation warned that the underlying Ticker would never be recovered by the garbage collector, and that if efficiency was a concern, code should use NewTicker instead and call Ticker.Stop when the ticker is no longer needed. As of Go 1.23, the garbage collector can recover unreferenced tickers, even if they haven't been stopped. The Stop method is no longer necessary to help the garbage collector. There is no longer any reason to prefer NewTicker when Tick will do.

```go

package main

import (
	"fmt"
	"time"
)

func statusUpdate() string { return "" }

func main() {
	c := time.Tick(5 * time.Second)
	for next := range c {
		fmt.Printf("%v %s\n", next, statusUpdate())
	}
}

```

```go
Output:

```

Share Format Run

```go
type Duration int64
```

A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years.

```go

package main

import (
	"fmt"
	"time"
)

func expensiveCall() {}

func main() {
	t0 := time.Now()
	expensiveCall()
	t1 := time.Now()
	fmt.Printf("The call took %v to run.\n", t1.Sub(t0))
}

```

```go
Output:

```

Share Format Run

```go
func ParseDuration(s string) (Duration, error)
```

ParseDuration parses a duration string. A duration string is a possibly signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300ms", "-1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	hours, _ := time.ParseDuration("10h")
	complex, _ := time.ParseDuration("1h10m10s")
	micro, _ := time.ParseDuration("1µs")
	// The package also accepts the incorrect but common prefix u for micro.
	micro2, _ := time.ParseDuration("1us")

fmt.Println(hours)
	fmt.Println(complex)
	fmt.Printf("There are %.0f seconds in %v.\n", complex.Seconds(), complex)
	fmt.Printf("There are %d nanoseconds in %v.\n", micro.Nanoseconds(), micro)
	fmt.Printf("There are %6.2e seconds in %v.\n", micro2.Seconds(), micro2)
}

```

```go
Output:
10h0m0s
1h10m10s
There are 4210 seconds in 1h10m10s.
There are 1000 nanoseconds in 1µs.
There are 1.00e-06 seconds in 1µs.

```

Share Format Run

```go
func Since(t Time) Duration
```

Since returns the time elapsed since t. It is shorthand for time.Now().Sub(t).

```go

package main

import (
	"fmt"
	"time"
)

func expensiveCall() {}

func main() {
	start := time.Now()
	expensiveCall()
	elapsed := time.Since(start)
	fmt.Printf("The call took %v to run.\n", elapsed)
}

```

```go
Output:

```

Share Format Run

```go
func Until(t Time) Duration
```

Until returns the duration until t. It is shorthand for t.Sub(time.Now()).

```go

package main

import (
	"fmt"
	"math"
	"time"
)

func main() {
	futureTime := time.Now().Add(5 * time.Second)
	durationUntil := time.Until(futureTime)
	fmt.Printf("Duration until future time: %.0f seconds", math.Ceil(durationUntil.Seconds()))
}

```

```go
Output:
Duration until future time: 5 seconds

```

Share Format Run

```go
func (d Duration) Abs() Duration
```

Abs returns the absolute value of d. As a special case, Duration(math.MinInt64) is converted to Duration(math.MaxInt64), reducing its magnitude by 1 nanosecond.

```go

package main

import (
	"fmt"
	"math"
	"time"
)

func main() {
	positiveDuration := 5 * time.Second
	negativeDuration := -3 * time.Second
	minInt64CaseDuration := time.Duration(math.MinInt64)

absPositive := positiveDuration.Abs()
	absNegative := negativeDuration.Abs()
	absSpecial := minInt64CaseDuration.Abs() == time.Duration(math.MaxInt64)

fmt.Printf("Absolute value of positive duration: %v\n", absPositive)
	fmt.Printf("Absolute value of negative duration: %v\n", absNegative)
	fmt.Printf("Absolute value of MinInt64 equal to MaxInt64: %t\n", absSpecial)

}

```

```go
Output:
Absolute value of positive duration: 5s
Absolute value of negative duration: 3s
Absolute value of MinInt64 equal to MaxInt64: true

```

Share Format Run

```go
func (d Duration) Hours() float64
```

Hours returns the duration as a floating point number of hours.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	h, _ := time.ParseDuration("4h30m")
	fmt.Printf("I've got %.1f hours of work left.", h.Hours())
}

```

```go
Output:
I've got 4.5 hours of work left.

```

Share Format Run
