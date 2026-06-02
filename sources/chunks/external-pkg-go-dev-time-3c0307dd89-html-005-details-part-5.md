---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/time"
source_path: "sources/raw/external/pkg-go-dev-time-3c0307dd89.html"
license_ref: ""
---

```go
func UnixMilli(msec int64) Time
```

UnixMilli returns the local Time corresponding to the given Unix time, msec milliseconds since January 1, 1970 UTC.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	umt := time.Date(2009, time.November, 10, 23, 0, 0, 0, time.UTC)
	fmt.Println(umt.UnixMilli())
	t := time.UnixMilli(umt.UnixMilli()).UTC()
	fmt.Println(t)

}

```

```go
Output:
1257894000000
2009-11-10 23:00:00 +0000 UTC

```

Share Format Run

```go
func (t Time) Add(d Duration) Time
```

Add returns the time t+d.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Date(2009, 1, 1, 12, 0, 0, 0, time.UTC)
	afterTenSeconds := start.Add(time.Second * 10)
	afterTenMinutes := start.Add(time.Minute * 10)
	afterTenHours := start.Add(time.Hour * 10)
	afterTenDays := start.Add(time.Hour * 24 * 10)

fmt.Printf("start = %v\n", start)
	fmt.Printf("start.Add(time.Second * 10) = %v\n", afterTenSeconds)
	fmt.Printf("start.Add(time.Minute * 10) = %v\n", afterTenMinutes)
	fmt.Printf("start.Add(time.Hour * 10) = %v\n", afterTenHours)
	fmt.Printf("start.Add(time.Hour * 24 * 10) = %v\n", afterTenDays)

}

```

```go
Output:
start = 2009-01-01 12:00:00 +0000 UTC
start.Add(time.Second * 10) = 2009-01-01 12:00:10 +0000 UTC
start.Add(time.Minute * 10) = 2009-01-01 12:10:00 +0000 UTC
start.Add(time.Hour * 10) = 2009-01-01 22:00:00 +0000 UTC
start.Add(time.Hour * 24 * 10) = 2009-01-11 12:00:00 +0000 UTC

```

Share Format Run

```go
func (t Time) AddDate(years int, months int, days int) Time
```

AddDate returns the time corresponding to adding the given number of years, months, and days to t. For example, AddDate(-1, 2, 3) applied to January 1, 2011 returns March 4, 2010.

Note that dates are fundamentally coupled to timezones, and calendrical periods like days don't have fixed durations. AddDate uses the Location of the Time value to determine these durations. That means that the same AddDate arguments can produce a different shift in absolute time depending on the base Time value and its Location. For example, AddDate(0, 0, 1) applied to 12:00 on March 27 always returns 12:00 on March 28. At some locations and in some years this is a 24 hour shift. In others it's a 23 hour shift due to daylight savings time transitions.

AddDate normalizes its result in the same way that Date does, so, for example, adding one month to October 31 yields December 1, the normalized form for November 31.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Date(2023, 03, 25, 12, 0, 0, 0, time.UTC)
	oneDayLater := start.AddDate(0, 0, 1)
	dayDuration := oneDayLater.Sub(start)
	oneMonthLater := start.AddDate(0, 1, 0)
	oneYearLater := start.AddDate(1, 0, 0)

zurich, err := time.LoadLocation("Europe/Zurich")
	if err != nil {
		panic(err)
	}
	// This was the day before a daylight saving time transition in Zürich.
	startZurich := time.Date(2023, 03, 25, 12, 0, 0, 0, zurich)
	oneDayLaterZurich := startZurich.AddDate(0, 0, 1)
	dayDurationZurich := oneDayLaterZurich.Sub(startZurich)

fmt.Printf("oneDayLater: start.AddDate(0, 0, 1) = %v\n", oneDayLater)
	fmt.Printf("oneMonthLater: start.AddDate(0, 1, 0) = %v\n", oneMonthLater)
	fmt.Printf("oneYearLater: start.AddDate(1, 0, 0) = %v\n", oneYearLater)
	fmt.Printf("oneDayLaterZurich: startZurich.AddDate(0, 0, 1) = %v\n", oneDayLaterZurich)
	fmt.Printf("Day duration in UTC: %v | Day duration in Zürich: %v\n", dayDuration, dayDurationZurich)

}

```

```go
Output:
oneDayLater: start.AddDate(0, 0, 1) = 2023-03-26 12:00:00 +0000 UTC
oneMonthLater: start.AddDate(0, 1, 0) = 2023-04-25 12:00:00 +0000 UTC
oneYearLater: start.AddDate(1, 0, 0) = 2024-03-25 12:00:00 +0000 UTC
oneDayLaterZurich: startZurich.AddDate(0, 0, 1) = 2023-03-26 12:00:00 +0200 CEST
Day duration in UTC: 24h0m0s | Day duration in Zürich: 23h0m0s

```

Share Format Run

```go
func (t Time) After(u Time) bool
```

After reports whether the time instant t is after u.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	year2000 := time.Date(2000, 1, 1, 0, 0, 0, 0, time.UTC)
	year3000 := time.Date(3000, 1, 1, 0, 0, 0, 0, time.UTC)

isYear3000AfterYear2000 := year3000.After(year2000) // True
	isYear2000AfterYear3000 := year2000.After(year3000) // False

fmt.Printf("year3000.After(year2000) = %v\n", isYear3000AfterYear2000)
	fmt.Printf("year2000.After(year3000) = %v\n", isYear2000AfterYear3000)

}

```

```go
Output:
year3000.After(year2000) = true
year2000.After(year3000) = false

```

Share Format Run

```go
func (t Time) AppendBinary(b []byte) ([]byte, error)
```

AppendBinary implements the encoding.BinaryAppender interface.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Date(2025, 4, 1, 15, 30, 45, 123456789, time.UTC)

var buffer []byte
	buffer, err := t.AppendBinary(buffer)
	if err != nil {
		panic(err)
	}

var parseTime time.Time
	err = parseTime.UnmarshalBinary(buffer[:])
	if err != nil {
		panic(err)
	}

fmt.Printf("t: %v\n", t)
	fmt.Printf("parseTime: %v\n", parseTime)
	fmt.Printf("equal: %v\n", parseTime.Equal(t))

}

```

```go
Output:
t: 2025-04-01 15:30:45.123456789 +0000 UTC
parseTime: 2025-04-01 15:30:45.123456789 +0000 UTC
equal: true

```

Share Format Run

```go
func (t Time) AppendFormat(b []byte, layout string) []byte
```

AppendFormat is like Time.Format but appends the textual representation to b and returns the extended buffer.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Date(2017, time.November, 4, 11, 0, 0, 0, time.UTC)
	text := []byte("Time: ")

text = t.AppendFormat(text, time.Kitchen)
	fmt.Println(string(text))

}

```

```go
Output:
Time: 11:00AM

```

Share Format Run

```go
func (t Time) AppendText(b []byte) ([]byte, error)
```

AppendText implements the encoding.TextAppender interface. The time is formatted in RFC 3339 <https://rfc-editor.org/rfc/rfc3339.html> format with sub-second precision. If the timestamp cannot be represented as valid RFC 3339 <https://rfc-editor.org/rfc/rfc3339.html> (e.g., the year is out of range), then an error is returned.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Date(2025, 4, 1, 15, 30, 45, 123456789, time.UTC)

buffer := []byte("t: ")

buffer, err := t.AppendText(buffer)
	if err != nil {
		panic(err)
	}

fmt.Printf("%s\n", buffer)

}

```

```go
Output:
t: 2025-04-01T15:30:45.123456789Z

```

Share Format Run

```go
func (t Time) Before(u Time) bool
```

Before reports whether the time instant t is before u.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	year2000 := time.Date(2000, 1, 1, 0, 0, 0, 0, time.UTC)
	year3000 := time.Date(3000, 1, 1, 0, 0, 0, 0, time.UTC)

isYear2000BeforeYear3000 := year2000.Before(year3000) // True
	isYear3000BeforeYear2000 := year3000.Before(year2000) // False

fmt.Printf("year2000.Before(year3000) = %v\n", isYear2000BeforeYear3000)
	fmt.Printf("year3000.Before(year2000) = %v\n", isYear3000BeforeYear2000)

}

```

```go
Output:
year2000.Before(year3000) = true
year3000.Before(year2000) = false

```

Share Format Run

```go
func (t Time) Clock() (hour, min, sec int)
```

Clock returns the hour, minute, and second within the day specified by t.

```go
func (t Time) Compare(u Time) int
```

Compare compares the time instant t with u. If t is before u, it returns -1; if t is after u, it returns +1; if they're the same, it returns 0.

```go
func (t Time) Date() (year int, month Month, day int)
```

Date returns the year, month, and day in which t occurs.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	d := time.Date(2000, 2, 1, 12, 30, 0, 0, time.UTC)
	year, month, day := d.Date()

fmt.Printf("year = %v\n", year)
	fmt.Printf("month = %v\n", month)
	fmt.Printf("day = %v\n", day)

}

```

```go
Output:
year = 2000
month = February
day = 1

```

Share Format Run

```go
func (t Time) Day() int
```

Day returns the day of the month specified by t.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	d := time.Date(2000, 2, 1, 12, 30, 0, 0, time.UTC)
	day := d.Day()

fmt.Printf("day = %v\n", day)

}

```

```go
Output:
day = 1

```

Share Format Run

```go
func (t Time) Equal(u Time) bool
```

Equal reports whether t and u represent the same time instant. Two times can be equal even if they are in different locations. For example, 6:00 +0200 and 4:00 UTC are Equal. See the documentation on the Time type for the pitfalls of using == with Time values; most code should use Equal instead.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	secondsEastOfUTC := int((8 * time.Hour).Seconds())
	beijing := time.FixedZone("Beijing Time", secondsEastOfUTC)

// Unlike the equal operator, Equal is aware that d1 and d2 are the
	// same instant but in different time zones.
	d1 := time.Date(2000, 2, 1, 12, 30, 0, 0, time.UTC)
	d2 := time.Date(2000, 2, 1, 20, 30, 0, 0, beijing)

datesEqualUsingEqualOperator := d1 == d2
	datesEqualUsingFunction := d1.Equal(d2)

fmt.Printf("datesEqualUsingEqualOperator = %v\n", datesEqualUsingEqualOperator)
	fmt.Printf("datesEqualUsingFunction = %v\n", datesEqualUsingFunction)

}

```

```go
Output:
datesEqualUsingEqualOperator = false
datesEqualUsingFunction = true

```

Share Format Run

```go
func (t Time) Format(layout string) string
```

Format returns a textual representation of the time value formatted according to the layout defined by the argument. See the documentation for the constant called Layout to see how to represent the layout format.

The executable example for Time.Format demonstrates the working of the layout string in detail and is a good reference.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	// Parse a time value from a string in the standard Unix format.
	t, err := time.Parse(time.UnixDate, "Wed Feb 25 11:06:39 PST 2015")
	if err != nil { // Always check errors even if they should not happen.
		panic(err)
	}

tz, err := time.LoadLocation("Asia/Shanghai")
	if err != nil { // Always check errors even if they should not happen.
		panic(err)
	}

// time.Time's Stringer method is useful without any format.
	fmt.Println("default format:", t)

// Predefined constants in the package implement common layouts.
	fmt.Println("Unix format:", t.Format(time.UnixDate))

// The time zone attached to the time value affects its output.
	fmt.Println("Same, in UTC:", t.UTC().Format(time.UnixDate))

fmt.Println("in Shanghai with seconds:", t.In(tz).Format("2006-01-02T15:04:05 -070000"))

fmt.Println("in Shanghai with colon seconds:", t.In(tz).Format("2006-01-02T15:04:05 -07:00:00"))

// The rest of this function demonstrates the properties of the
	// layout string used in the format.
