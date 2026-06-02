---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/time"
source_path: "sources/raw/external/pkg-go-dev-time-3c0307dd89.html"
license_ref: ""
---

// The layout string used by the Parse function and Format method
	// shows by example how the reference time should be represented.
	// We stress that one must show how the reference time is formatted,
	// not a time of the user's choosing. Thus each layout string is a
	// representation of the time stamp,
	//	Jan 2 15:04:05 2006 MST
	// An easy way to remember this value is that it holds, when presented
	// in this order, the values (lined up with the elements above):
	//	  1 2  3  4  5    6  -7
	// There are some wrinkles illustrated below.

// Most uses of Format and Parse use constant layout strings such as
	// the ones defined in this package, but the interface is flexible,
	// as these examples show.

// Define a helper function to make the examples' output look nice.
	do := func(name, layout, want string) {
		got := t.Format(layout)
		if want != got {
			fmt.Printf("error: for %q got %q; expected %q\n", layout, got, want)
			return
		}
		fmt.Printf("%-16s %q gives %q\n", name, layout, got)
	}

// Print a header in our output.
	fmt.Printf("\nFormats:\n\n")

// Simple starter examples.
	do("Basic full date", "Mon Jan 2 15:04:05 MST 2006", "Wed Feb 25 11:06:39 PST 2015")
	do("Basic short date", "2006/01/02", "2015/02/25")

// The hour of the reference time is 15, or 3PM. The layout can express
	// it either way, and since our value is the morning we should see it as
	// an AM time. We show both in one format string. Lower case too.
	do("AM/PM", "3PM==3pm==15h", "11AM==11am==11h")

// When parsing, if the seconds value is followed by a decimal point
	// and some digits, that is taken as a fraction of a second even if
	// the layout string does not represent the fractional second.
	// Here we add a fractional second to our time value used above.
	t, err = time.Parse(time.UnixDate, "Wed Feb 25 11:06:39.1234 PST 2015")
	if err != nil {
		panic(err)
	}
	// It does not appear in the output if the layout string does not contain
	// a representation of the fractional second.
	do("No fraction", time.UnixDate, "Wed Feb 25 11:06:39 PST 2015")

// Fractional seconds can be printed by adding a run of 0s or 9s after
	// a decimal point in the seconds value in the layout string.
	// If the layout digits are 0s, the fractional second is of the specified
	// width. Note that the output has a trailing zero.
	do("0s for fraction", "15:04:05.00000", "11:06:39.12340")

// If the fraction in the layout is 9s, trailing zeros are dropped.
	do("9s for fraction", "15:04:05.99999999", "11:06:39.1234")

}

```

```go
Output:
default format: 2015-02-25 11:06:39 -0800 PST
Unix format: Wed Feb 25 11:06:39 PST 2015
Same, in UTC: Wed Feb 25 19:06:39 UTC 2015
in Shanghai with seconds: 2015-02-26T03:06:39 +080000
in Shanghai with colon seconds: 2015-02-26T03:06:39 +08:00:00

Formats:

Basic full date  "Mon Jan 2 15:04:05 MST 2006" gives "Wed Feb 25 11:06:39 PST 2015"
Basic short date "2006/01/02" gives "2015/02/25"
AM/PM            "3PM==3pm==15h" gives "11AM==11am==11h"
No fraction      "Mon Jan _2 15:04:05 MST 2006" gives "Wed Feb 25 11:06:39 PST 2015"
0s for fraction  "15:04:05.00000" gives "11:06:39.12340"
9s for fraction  "15:04:05.99999999" gives "11:06:39.1234"

```

Share Format Run

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	// Parse a time value from a string in the standard Unix format.
	t, err := time.Parse(time.UnixDate, "Sat Mar 7 11:06:39 PST 2015")
	if err != nil { // Always check errors even if they should not happen.
		panic(err)
	}

// Define a helper function to make the examples' output look nice.
	do := func(name, layout, want string) {
		got := t.Format(layout)
		if want != got {
			fmt.Printf("error: for %q got %q; expected %q\n", layout, got, want)
			return
		}
		fmt.Printf("%-16s %q gives %q\n", name, layout, got)
	}

// The predefined constant Unix uses an underscore to pad the day.
	do("Unix", time.UnixDate, "Sat Mar  7 11:06:39 PST 2015")

// For fixed-width printing of values, such as the date, that may be one or
	// two characters (7 vs. 07), use an _ instead of a space in the layout string.
	// Here we print just the day, which is 2 in our layout string and 7 in our
	// value.
	do("No pad", "<2>", "<7>")

// An underscore represents a space pad, if the date only has one digit.
	do("Spaces", "<_2>", "< 7>")

// A "0" indicates zero padding for single-digit values.
	do("Zeros", "<02>", "<07>")

// If the value is already the right width, padding is not used.
	// For instance, the second (05 in the reference time) in our value is 39,
	// so it doesn't need padding, but the minutes (04, 06) does.
	do("Suppressed pad", "04:05", "06:39")

}

```

```go
Output:
Unix             "Mon Jan _2 15:04:05 MST 2006" gives "Sat Mar  7 11:06:39 PST 2015"
No pad           "<2>" gives "<7>"
Spaces           "<_2>" gives "< 7>"
Zeros            "<02>" gives "<07>"
Suppressed pad   "04:05" gives "06:39"

```

Share Format Run

```go
func (t Time) GoString() string
```

GoString implements fmt.GoStringer and formats t to be printed in Go source code.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Date(2009, time.November, 10, 23, 0, 0, 0, time.UTC)
	fmt.Println(t.GoString())
	t = t.Add(1 * time.Minute)
	fmt.Println(t.GoString())
	t = t.AddDate(0, 1, 0)
	fmt.Println(t.GoString())
	t, _ = time.Parse("Jan 2, 2006 at 3:04pm (MST)", "Feb 3, 2013 at 7:54pm (UTC)")
	fmt.Println(t.GoString())

}

```

```go
Output:
time.Date(2009, time.November, 10, 23, 0, 0, 0, time.UTC)
time.Date(2009, time.November, 10, 23, 1, 0, 0, time.UTC)
time.Date(2009, time.December, 10, 23, 1, 0, 0, time.UTC)
time.Date(2013, time.February, 3, 19, 54, 0, 0, time.UTC)

```

Share Format Run

```go
func (t *Time) GobDecode(data []byte) error
```

GobDecode implements the gob.GobDecoder interface.

```go
func (t Time) GobEncode() ([]byte, error)
```

GobEncode implements the gob.GobEncoder interface.

```go
func (t Time) Hour() int
```

Hour returns the hour within the day specified by t, in the range [0, 23].

```go
func (t Time) ISOWeek() (year, week int)
```

ISOWeek returns the ISO 8601 year and week number in which t occurs. Week ranges from 1 to 53. Jan 01 to Jan 03 of year n might belong to week 52 or 53 of year n-1, and Dec 29 to Dec 31 might belong to week 1 of year n+1.

```go
func (t Time) In(loc *Location) Time
```

In returns a copy of t representing the same time instant, but with the copy's location information set to loc for display purposes.

In panics if loc is nil.

```go
func (t Time) IsDST() bool
```

IsDST reports whether the time in the configured location is in Daylight Savings Time.

```go
func (t Time) IsZero() bool
```

IsZero reports whether t represents the zero time instant, January 1, year 1, 00:00:00 UTC.

```go
func (t Time) Local() Time
```

Local returns t with the location set to local time.

```go
func (t Time) Location() *Location
```

Location returns the time zone information associated with t.

```go
func (t Time) MarshalBinary() ([]byte, error)
```

MarshalBinary implements the encoding.BinaryMarshaler interface.

```go
func (t Time) MarshalJSON() ([]byte, error)
```

MarshalJSON implements the encoding/json.Marshaler interface. The time is a quoted string in the RFC 3339 <https://rfc-editor.org/rfc/rfc3339.html> format with sub-second precision. If the timestamp cannot be represented as valid RFC 3339 <https://rfc-editor.org/rfc/rfc3339.html> (e.g., the year is out of range), then an error is reported.

```go
func (t Time) MarshalText() ([]byte, error)
```

MarshalText implements the encoding.TextMarshaler interface. The output matches that of calling the Time.AppendText method.

See Time.AppendText for more information.

```go
func (t Time) Minute() int
```

Minute returns the minute offset within the hour specified by t, in the range [0, 59].

```go
func (t Time) Month() Month
```

Month returns the month of the year specified by t.

```go
func (t Time) Nanosecond() int
```

Nanosecond returns the nanosecond offset within the second specified by t, in the range [0, 999999999].

```go
func (t Time) Round(d Duration) Time
```

Round returns the result of rounding t to the nearest multiple of d (since the zero time). The rounding behavior for halfway values is to round up. If d <= 0, Round returns t stripped of any monotonic clock reading but otherwise unchanged.

Round operates on the time as an absolute duration since the zero time; it does not operate on the presentation form of the time. Thus, Round(Hour) may return a time with a non-zero minute, depending on the time's Location.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Date(0, 0, 0, 12, 15, 30, 918273645, time.UTC)
	round := []time.Duration{
		time.Nanosecond,
		time.Microsecond,
		time.Millisecond,
		time.Second,
		2 * time.Second,
		time.Minute,
		10 * time.Minute,
		time.Hour,
	}

for _, d := range round {
		fmt.Printf("t.Round(%6s) = %s\n", d, t.Round(d).Format("15:04:05.999999999"))
	}
}

```

```go
Output:
t.Round(   1ns) = 12:15:30.918273645
t.Round(   1µs) = 12:15:30.918274
t.Round(   1ms) = 12:15:30.918
t.Round(    1s) = 12:15:31
t.Round(    2s) = 12:15:30
t.Round(  1m0s) = 12:16:00
t.Round( 10m0s) = 12:20:00
t.Round(1h0m0s) = 12:00:00

```

Share Format Run

```go
func (t Time) Second() int
```

Second returns the second offset within the minute specified by t, in the range [0, 59].

```go
func (t Time) String() string
```

String returns the time formatted using the format string

```go
"2006-01-02 15:04:05.999999999 -0700 MST"

```

If the time has a monotonic clock reading, the returned string includes a final field "m=±<value>", where value is the monotonic clock reading formatted as a decimal number of seconds.

The returned string is meant for debugging; for a stable serialized representation, use t.MarshalText, t.MarshalBinary, or t.Format with an explicit format string.

```go

package main

import (
	"fmt"
	"time"
)
