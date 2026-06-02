---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/time"
source_path: "sources/raw/external/pkg-go-dev-time-3c0307dd89.html"
license_ref: ""
---

```go
func (d Duration) Microseconds() int64
```

Microseconds returns the duration as an integer microsecond count.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	u, _ := time.ParseDuration("1s")
	fmt.Printf("One second is %d microseconds.\n", u.Microseconds())
}

```

```go
Output:
One second is 1000000 microseconds.

```

Share Format Run

```go
func (d Duration) Milliseconds() int64
```

Milliseconds returns the duration as an integer millisecond count.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	u, _ := time.ParseDuration("1s")
	fmt.Printf("One second is %d milliseconds.\n", u.Milliseconds())
}

```

```go
Output:
One second is 1000 milliseconds.

```

Share Format Run

```go
func (d Duration) Minutes() float64
```

Minutes returns the duration as a floating point number of minutes.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	m, _ := time.ParseDuration("1h30m")
	fmt.Printf("The movie is %.0f minutes long.", m.Minutes())
}

```

```go
Output:
The movie is 90 minutes long.

```

Share Format Run

```go
func (d Duration) Nanoseconds() int64
```

Nanoseconds returns the duration as an integer nanosecond count.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	u, _ := time.ParseDuration("1µs")
	fmt.Printf("One microsecond is %d nanoseconds.\n", u.Nanoseconds())
}

```

```go
Output:
One microsecond is 1000 nanoseconds.

```

Share Format Run

```go
func (d Duration) Round(m Duration) Duration
```

Round returns the result of rounding d to the nearest multiple of m. The rounding behavior for halfway values is to round away from zero. If the result exceeds the maximum (or minimum) value that can be stored in a Duration, Round returns the maximum (or minimum) duration. If m <= 0, Round returns d unchanged.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	d, err := time.ParseDuration("1h15m30.918273645s")
	if err != nil {
		panic(err)
	}

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

for _, r := range round {
		fmt.Printf("d.Round(%6s) = %s\n", r, d.Round(r).String())
	}
}

```

```go
Output:
d.Round(   1ns) = 1h15m30.918273645s
d.Round(   1µs) = 1h15m30.918274s
d.Round(   1ms) = 1h15m30.918s
d.Round(    1s) = 1h15m31s
d.Round(    2s) = 1h15m30s
d.Round(  1m0s) = 1h16m0s
d.Round( 10m0s) = 1h20m0s
d.Round(1h0m0s) = 1h0m0s

```

Share Format Run

```go
func (d Duration) Seconds() float64
```

Seconds returns the duration as a floating point number of seconds.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	m, _ := time.ParseDuration("1m30s")
	fmt.Printf("Take off in t-%.0f seconds.", m.Seconds())
}

```

```go
Output:
Take off in t-90 seconds.

```

Share Format Run

```go
func (d Duration) String() string
```

String returns a string representing the duration in the form "72h3m0.5s". Leading zero units are omitted. As a special case, durations less than one second format use a smaller unit (milli-, micro-, or nanoseconds) to ensure that the leading digit is non-zero. The zero duration formats as 0s.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println(1*time.Hour + 2*time.Minute + 300*time.Millisecond)
	fmt.Println(300 * time.Millisecond)
}

```

```go
Output:
1h2m0.3s
300ms

```

Share Format Run

```go
func (d Duration) Truncate(m Duration) Duration
```

Truncate returns the result of rounding d toward zero to a multiple of m. If m <= 0, Truncate returns d unchanged.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	d, err := time.ParseDuration("1h15m30.918273645s")
	if err != nil {
		panic(err)
	}

trunc := []time.Duration{
		time.Nanosecond,
		time.Microsecond,
		time.Millisecond,
		time.Second,
		2 * time.Second,
		time.Minute,
		10 * time.Minute,
		time.Hour,
	}

for _, t := range trunc {
		fmt.Printf("d.Truncate(%6s) = %s\n", t, d.Truncate(t).String())
	}
}

```

```go
Output:
d.Truncate(   1ns) = 1h15m30.918273645s
d.Truncate(   1µs) = 1h15m30.918273s
d.Truncate(   1ms) = 1h15m30.918s
d.Truncate(    1s) = 1h15m30s
d.Truncate(    2s) = 1h15m30s
d.Truncate(  1m0s) = 1h15m0s
d.Truncate( 10m0s) = 1h10m0s
d.Truncate(1h0m0s) = 1h0m0s

```

Share Format Run

```go
type Location struct {
	// contains filtered or unexported fields
}
```

A Location maps time instants to the zone in use at that time. Typically, the Location represents the collection of time offsets in use in a geographical area. For many Locations the time offset varies depending on whether daylight savings time is in use at the time instant.

Location is used to provide a time zone in a printed Time value and for calculations involving intervals that may cross daylight savings time boundaries.

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	// China doesn't have daylight saving. It uses a fixed 8 hour offset from UTC.
	secondsEastOfUTC := int((8 * time.Hour).Seconds())
	beijing := time.FixedZone("Beijing Time", secondsEastOfUTC)

// If the system has a timezone database present, it's possible to load a location
	// from that, e.g.:
	//    newYork, err := time.LoadLocation("America/New_York")

// Creating a time requires a location. Common locations are time.Local and time.UTC.
	timeInUTC := time.Date(2009, 1, 1, 12, 0, 0, 0, time.UTC)
	sameTimeInBeijing := time.Date(2009, 1, 1, 20, 0, 0, 0, beijing)

// Although the UTC clock time is 1200 and the Beijing clock time is 2000, Beijing is
	// 8 hours ahead so the two dates actually represent the same instant.
	timesAreEqual := timeInUTC.Equal(sameTimeInBeijing)
	fmt.Println(timesAreEqual)

}

```

```go
Output:
true

```

Share Format Run

```go
var Local *Location = &localLoc
```

Local represents the system's local time zone. On Unix systems, Local consults the TZ environment variable to find the time zone to use. No TZ means use the system default /etc/localtime. TZ="" means use UTC. TZ="foo" means use file foo in the system timezone directory.

```go
var UTC *Location = &utcLoc
```

UTC represents Universal Coordinated Time (UTC).

```go
func FixedZone(name string, offset int) *Location
```

FixedZone returns a Location that always uses the given zone name and offset (seconds east of UTC).

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	loc := time.FixedZone("UTC-8", -8*60*60)
	t := time.Date(2009, time.November, 10, 23, 0, 0, 0, loc)
	fmt.Println("The time is:", t.Format(time.RFC822))
}

```

```go
Output:
The time is: 10 Nov 09 23:00 UTC-8

```

Share Format Run

```go
func LoadLocation(name string) (*Location, error)
```

LoadLocation returns the Location with the given name.

If the name is "" or "UTC", LoadLocation returns UTC. If the name is "Local", LoadLocation returns Local.

Otherwise, the name is taken to be a location name corresponding to a file in the IANA Time Zone database, such as "America/New_York".

LoadLocation looks for the IANA Time Zone database in the following locations in order:

- the directory or uncompressed zip file named by the ZONEINFO environment variable
- on a Unix system, the system standard installation location
- $GOROOT/lib/time/zoneinfo.zip
- the time/tzdata package, if it was imported

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	location, err := time.LoadLocation("America/Los_Angeles")
	if err != nil {
		panic(err)
	}

timeInUTC := time.Date(2018, 8, 30, 12, 0, 0, 0, time.UTC)
	fmt.Println(timeInUTC.In(location))
}

```

```go
Output:
2018-08-30 05:00:00 -0700 PDT

```

Share Format Run

```go
func LoadLocationFromTZData(name string, data []byte) (*Location, error)
```

LoadLocationFromTZData returns a Location with the given name initialized from the IANA Time Zone database-formatted data. The data should be in the format of a standard IANA time zone file (for example, the content of /etc/localtime on Unix systems).

```go
func (l *Location) String() string
```

String returns a descriptive name for the time zone information, corresponding to the name argument to LoadLocation or FixedZone.

```go
type Month int
```

A Month specifies a month of the year (January = 1, ...).

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	_, month, day := time.Now().Date()
	if month == time.November && day == 10 {
		fmt.Println("Happy Go day!")
	}
}

```

```go
Output:

```

Share Format Run

```go
const (
	January Month = 1 + iota
	February
	March
	April
	May
	June
	July
	August
	September
	October
	November
	December
)
```

```go
func (m Month) String() string
```

String returns the English name of the month ("January", "February", ...).

```go
type ParseError struct {
	Layout     string
	Value      string
	LayoutElem string
	ValueElem  string
	Message    string
}
```

ParseError describes a problem parsing a time string.

```go
func (e *ParseError) Error() string
```

Error returns the string representation of a ParseError.

```go
type Ticker struct {
	C <-chan Time // The channel on which the ticks are delivered.
	// contains filtered or unexported fields
}
```

A Ticker holds a channel that delivers “ticks” of a clock at intervals.

```go
func NewTicker(d Duration) *Ticker
```

NewTicker returns a new Ticker containing a channel that will send the current time on the channel after each tick. The period of the ticks is specified by the duration argument. The ticker will adjust the time interval or drop ticks to make up for slow receivers. The duration d must be greater than zero; if not, NewTicker will panic.

Before Go 1.23, the garbage collector did not recover tickers that had not yet expired or been stopped, so code often immediately deferred t.Stop after calling NewTicker, to make the ticker recoverable when it was no longer needed. As of Go 1.23, the garbage collector can recover unreferenced tickers, even if they haven't been stopped. The Stop method is no longer necessary to help the garbage collector. (Code may of course still want to call Stop to stop the ticker for other reasons.)

```go

package main

import (
	"fmt"
	"time"
)

func main() {
	ticker := time.NewTicker(time.Second)
	defer ticker.Stop()
	done := make(chan bool)
	go func() {
		time.Sleep(10 * time.Second)
		done <- true
	}()
	for {
		select {
		case <-done:
			fmt.Println("Done!")
			return
		case t := <-ticker.C:
			fmt.Println("Current time: ", t)
		}
	}
}

```

```go
Output:

```

Share Format Run

```go
func (t *Ticker) Reset(d Duration)
```
