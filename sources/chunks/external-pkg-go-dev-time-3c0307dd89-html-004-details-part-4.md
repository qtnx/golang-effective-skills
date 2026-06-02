---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/time"
source_path: "sources/raw/external/pkg-go-dev-time-3c0307dd89.html"
license_ref: ""
---

Reset stops a ticker and resets its period to the specified duration. The next tick will arrive after the new period elapses. The duration d must be greater than zero; if not, Reset will panic.

```go
func (t *Ticker) Stop()
```

Stop turns off a ticker. After Stop, no more ticks will be sent. Stop does not close the channel, to prevent a concurrent goroutine reading from the channel from seeing an erroneous "tick".

```go
type Time struct {
	// contains filtered or unexported fields
}
```

A Time represents an instant in time with nanosecond precision.

Programs using times should typically store and pass them as values, not pointers. That is, time variables and struct fields should be of type time.Time, not *time.Time.

A Time value can be used by multiple goroutines simultaneously except that the methods Time.GobDecode, Time.UnmarshalBinary, Time.UnmarshalJSON and Time.UnmarshalText are not concurrency-safe.

Time instants can be compared using the Time.Before, Time.After, and Time.Equal methods. The Time.Sub method subtracts two instants, producing a Duration. The Time.Add method adds a Time and a Duration, producing a Time.

The zero value of type Time is January 1, year 1, 00:00:00.000000000 UTC. As this time is unlikely to come up in practice, the Time.IsZero method gives a simple way of detecting a time that has not been initialized explicitly.

Each time has an associated Location. The methods Time.Local, Time.UTC, and Time.In return a Time with a specific Location. Changing the Location of a Time value with these methods does not change the actual instant it represents, only the time zone in which to interpret it.

Representations of a Time value saved by the Time.GobEncode, Time.MarshalBinary, Time.AppendBinary, Time.MarshalJSON, Time.MarshalText and Time.AppendText methods store the Time.Location's offset, but not the location name. They therefore lose information about Daylight Saving Time.

In addition to the required “wall clock” reading, a Time may contain an optional reading of the current process's monotonic clock, to provide additional precision for comparison or subtraction. See the “Monotonic Clocks” section in the package documentation for details.

Note that the Go == operator compares not just the time instant but also the Location and the monotonic clock reading. Therefore, Time values should not be used as map or database keys without first guaranteeing that the identical Location has been set for all values, which can be achieved through use of the UTC or Local method, and that the monotonic clock reading has been stripped by setting t = t.Round(0). In general, prefer t.Equal(u) to t == u, since t.Equal uses the most accurate comparison available and correctly handles the case when only one of its arguments has a monotonic clock reading.

```go
func Date(year int, month Month, day, hour, min, sec, nsec int, loc *Location) Time
```

Date returns the Time corresponding to

```go
yyyy-mm-dd hh:mm:ss + nsec nanoseconds

```

in the appropriate zone for that time in the given location.

The month, day, hour, min, sec, and nsec values may be outside their usual ranges and will be normalized during the conversion. For example, October 32 converts to November 1.

A daylight savings time transition skips or repeats times. For example, in the United States, March 13, 2011 2:15am never occurred, while November 6, 2011 1:15am occurred twice. In such cases, the choice of time zone, and therefore the time, is not well-defined. Date returns a time that is correct in one of the two zones involved in the transition, but it does not guarantee which.

Date panics if loc is nil.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Date(2009, time.November, 10, 23, 0, 0, 0, time.UTC)
	fmt.Printf("Go launched at %s\n", t.Local())
}

```

```go
Output:
Go launched at 2009-11-10 15:00:00 -0800 PST

```

Share Format Run

```go
func Now() Time
```

Now returns the current local time.

```go
func Parse(layout, value string) (Time, error)
```

Parse parses a formatted string and returns the time value it represents. See the documentation for the constant called Layout to see how to represent the format. The second argument must be parseable using the format string (layout) provided as the first argument.

The example for Time.Format demonstrates the working of the layout string in detail and is a good reference.

When parsing (only), the input may contain a fractional second field immediately after the seconds field, even if the layout does not signify its presence. In that case either a comma or a decimal point followed by a maximal series of digits is parsed as a fractional second. Fractional seconds are truncated to nanosecond precision.

Elements omitted from the layout are assumed to be zero or, when zero is impossible, one, so parsing "3:04pm" returns the time corresponding to Jan 1, year 0, 15:04:00 UTC (note that because the year is 0, this time is before the zero Time). Years must be in the range 0000..9999. The day of the week is checked for syntax but it is otherwise ignored.

For layouts specifying the two-digit year 06, a value NN >= 69 will be treated as 19NN and a value NN < 69 will be treated as 20NN.

The remainder of this comment describes the handling of time zones.

In the absence of a time zone indicator, Parse returns a time in UTC.

When parsing a time with a zone offset like -0700, if the offset corresponds to a time zone used by the current location (Local), then Parse uses that location and zone in the returned time. Otherwise it records the time as being in a fabricated location with time fixed at the given zone offset.

When parsing a time with a zone abbreviation like MST, if the zone abbreviation has a defined offset in the current location, then that offset is used. The zone abbreviation "UTC" is recognized as UTC regardless of location. If the zone abbreviation is unknown, Parse records the time as being in a fabricated location with the given zone abbreviation and a zero offset. This choice means that such a time can be parsed and reformatted with the same layout losslessly, but the exact instant used in the representation will differ by the actual zone offset. To avoid such problems, prefer time layouts that use a numeric zone offset, or use ParseInLocation.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	// See the example for Time.Format for a thorough description of how
	// to define the layout string to parse a time.Time value; Parse and
	// Format use the same model to describe their input and output.

// longForm shows by example how the reference time would be represented in
	// the desired layout.
	const longForm = "Jan 2, 2006 at 3:04pm (MST)"
	t, _ := time.Parse(longForm, "Feb 3, 2013 at 7:54pm (PST)")
	fmt.Println(t)

// shortForm is another way the reference time would be represented
	// in the desired layout; it has no time zone present.
	// Note: without explicit zone, returns time in UTC.
	const shortForm = "2006-Jan-02"
	t, _ = time.Parse(shortForm, "2013-Feb-03")
	fmt.Println(t)

// Some valid layouts are invalid time values, due to format specifiers
	// such as _ for space padding and Z for zone information.
	// For example the RFC3339 layout 2006-01-02T15:04:05Z07:00
	// contains both Z and a time zone offset in order to handle both valid options:
	// 2006-01-02T15:04:05Z
	// 2006-01-02T15:04:05+07:00
	t, _ = time.Parse(time.RFC3339, "2006-01-02T15:04:05Z")
	fmt.Println(t)
	t, _ = time.Parse(time.RFC3339, "2006-01-02T15:04:05+07:00")
	fmt.Println(t)
	_, err := time.Parse(time.RFC3339, time.RFC3339)
	fmt.Println("error", err) // Returns an error as the layout is not a valid time value

}

```

```go
Output:
2013-02-03 19:54:00 -0800 PST
2013-02-03 00:00:00 +0000 UTC
2006-01-02 15:04:05 +0000 UTC
2006-01-02 15:04:05 +0700 +0700
error parsing time "2006-01-02T15:04:05Z07:00": extra text: "07:00"

```

Share Format Run

```go
func ParseInLocation(layout, value string, loc *Location) (Time, error)
```

ParseInLocation is like Parse but differs in two important ways. First, in the absence of time zone information, Parse interprets a time as UTC; ParseInLocation interprets the time as in the given location. Second, when given a zone offset or abbreviation, Parse tries to match it against the Local location; ParseInLocation uses the given location.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	loc, _ := time.LoadLocation("Europe/Berlin")

// This will look for the name CEST in the Europe/Berlin time zone.
	const longForm = "Jan 2, 2006 at 3:04pm (MST)"
	t, _ := time.ParseInLocation(longForm, "Jul 9, 2012 at 5:02am (CEST)", loc)
	fmt.Println(t)

// Note: without explicit zone, returns time in given location.
	const shortForm = "2006-Jan-02"
	t, _ = time.ParseInLocation(shortForm, "2012-Jul-09", loc)
	fmt.Println(t)

}

```

```go
Output:
2012-07-09 05:02:00 +0200 CEST
2012-07-09 00:00:00 +0200 CEST

```

Share Format Run

```go
func Unix(sec int64, nsec int64) Time
```

Unix returns the local Time corresponding to the given Unix time, sec seconds and nsec nanoseconds since January 1, 1970 UTC. It is valid to pass nsec outside the range [0, 999999999]. Not all sec values have a corresponding time value. One such value is 1<<63-1 (the largest int64 value).

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	unixTime := time.Date(2009, time.November, 10, 23, 0, 0, 0, time.UTC)
	fmt.Println(unixTime.Unix())
	t := time.Unix(unixTime.Unix(), 0).UTC()
	fmt.Println(t)

}

```

```go
Output:
1257894000
2009-11-10 23:00:00 +0000 UTC

```

Share Format Run

```go
func UnixMicro(usec int64) Time
```

UnixMicro returns the local Time corresponding to the given Unix time, usec microseconds since January 1, 1970 UTC.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	umt := time.Date(2009, time.November, 10, 23, 0, 0, 0, time.UTC)
	fmt.Println(umt.UnixMicro())
	t := time.UnixMicro(umt.UnixMicro()).UTC()
	fmt.Println(t)

}

```

```go
Output:
1257894000000000
2009-11-10 23:00:00 +0000 UTC

```

Share Format Run
