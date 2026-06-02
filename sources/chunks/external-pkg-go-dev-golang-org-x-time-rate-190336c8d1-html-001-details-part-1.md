---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/golang.org/x/time/rate"
source_path: "sources/raw/external/pkg-go-dev-golang-org-x-time-rate-190336c8d1.html"
license_ref: ""
---

rate package - golang.org/x/time/rate - Go Packages
## Details

-     Valid go.mod <https://cs.opensource.google/go/x/time/+/v0.15.0:/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/x/time  <https://cs.opensource.google/go/x/time>

##   Documentation ¶

Package rate provides a rate limiter.

- Constants
-  type Limit
-
-  func Every(interval time.Duration) Limit

-  type Limiter
-
-  func NewLimiter(r Limit, b int) *Limiter

-
-  func (lim *Limiter) Allow() bool
-  func (lim *Limiter) AllowN(t time.Time, n int) bool
-  func (lim *Limiter) Burst() int
-  func (lim *Limiter) Limit() Limit
-  func (lim *Limiter) Reserve() *Reservation
-  func (lim *Limiter) ReserveN(t time.Time, n int) *Reservation
-  func (lim *Limiter) SetBurst(newBurst int)
-  func (lim *Limiter) SetBurstAt(t time.Time, newBurst int)
-  func (lim *Limiter) SetLimit(newLimit Limit)
-  func (lim *Limiter) SetLimitAt(t time.Time, newLimit Limit)
-  func (lim *Limiter) Tokens() float64
-  func (lim *Limiter) TokensAt(t time.Time) float64
-  func (lim *Limiter) Wait(ctx context.Context) (err error)
-  func (lim *Limiter) WaitN(ctx context.Context, n int) (err error)

-  type Reservation
-
-  func (r *Reservation) Cancel()
-  func (r *Reservation) CancelAt(t time.Time)
-  func (r *Reservation) Delay() time.Duration
-  func (r *Reservation) DelayFrom(t time.Time) time.Duration
-  func (r *Reservation) OK() bool

-  type Sometimes
-
-  func (s *Sometimes) Do(f func())

- Sometimes (Every)
- Sometimes (First)
- Sometimes (Interval)
- Sometimes (Mix)
- Sometimes (Once)

View Source <https://cs.opensource.google/go/x/time/+/v0.15.0:rate/rate.go;l=22>
```go
const Inf = Limit(math.MaxFloat64)
```

Inf is the infinite rate limit; it allows all events (even if burst is zero).
  View Source <https://cs.opensource.google/go/x/time/+/v0.15.0:rate/rate.go;l=144>
```go
const InfDuration = time.Duration(math.MaxInt64)
```

InfDuration is the duration returned by Delay when a Reservation is not OK.

This section is empty.

This section is empty.

```go
type Limit float64
```

Limit defines the maximum frequency of some events. Limit is represented as number of events per second. A zero Limit allows no events.

```go
func Every(interval time.Duration) Limit
```

Every converts a minimum time interval between events to a Limit.

```go
type Limiter struct {
	// contains filtered or unexported fields
}
```

A Limiter controls how frequently events are allowed to happen. It implements a "token bucket" of size b, initially full and refilled at rate r tokens per second. Informally, in any large enough time interval, the Limiter limits the rate to r tokens per second, with a maximum burst size of b events. As a special case, if r == Inf (the infinite rate), b is ignored. See https://en.wikipedia.org/wiki/Token_bucket <https://en.wikipedia.org/wiki/Token_bucket> for more about token buckets.

The zero value is a valid Limiter, but it will reject all events. Use NewLimiter to create non-zero Limiters.

Limiter has three main methods, Allow, Reserve, and Wait. Most callers should use Wait.

Each of the three methods consumes a single token. They differ in their behavior when no token is available. If no token is available, Allow returns false. If no token is available, Reserve returns a reservation for a future token and the amount of time the caller must wait before using it. If no token is available, Wait blocks until one can be obtained or its associated context.Context is canceled.

The methods AllowN, ReserveN, and WaitN consume n tokens.

Limiter is safe for simultaneous use by multiple goroutines.

```go
func NewLimiter(r Limit, b int) *Limiter
```

NewLimiter returns a new Limiter that allows events up to rate r and permits bursts of at most b tokens.

```go
func (lim *Limiter) Allow() bool
```

Allow reports whether an event may happen now.

```go
func (lim *Limiter) AllowN(t time.Time, n int) bool
```

AllowN reports whether n events may happen at time t. Use this method if you intend to drop / skip events that exceed the rate limit. Otherwise use Reserve or Wait.

```go
func (lim *Limiter) Burst() int
```

Burst returns the maximum burst size. Burst is the maximum number of tokens that can be consumed in a single call to Allow, Reserve, or Wait, so higher Burst values allow more events to happen at once. A zero Burst allows no events, unless limit == Inf.

```go
func (lim *Limiter) Limit() Limit
```

Limit returns the maximum overall event rate.

```go
func (lim *Limiter) Reserve() *Reservation
```

Reserve is shorthand for ReserveN(time.Now(), 1).

```go
func (lim *Limiter) ReserveN(t time.Time, n int) *Reservation
```

ReserveN returns a Reservation that indicates how long the caller must wait before n events happen. The Limiter takes this Reservation into account when allowing future events. The returned Reservation’s OK() method returns false if n exceeds the Limiter's burst size. Usage example:

```go
r := lim.ReserveN(time.Now(), 1)
if !r.OK() {
  // Not allowed to act! Did you remember to set lim.burst to be > 0 ?
  return
}
time.Sleep(r.Delay())
Act()

```

Use this method if you wish to wait and slow down in accordance with the rate limit without dropping events. If you need to respect a deadline or cancel the delay, use Wait instead. To drop or skip events exceeding rate limit, use Allow instead.

```go
func (lim *Limiter) SetBurst(newBurst int)
```

SetBurst is shorthand for SetBurstAt(time.Now(), newBurst).

```go
func (lim *Limiter) SetBurstAt(t time.Time, newBurst int)
```

SetBurstAt sets a new burst size for the limiter.

```go
func (lim *Limiter) SetLimit(newLimit Limit)
```

SetLimit is shorthand for SetLimitAt(time.Now(), newLimit).

```go
func (lim *Limiter) SetLimitAt(t time.Time, newLimit Limit)
```

SetLimitAt sets a new Limit for the limiter. The new Limit, and Burst, may be violated or underutilized by those which reserved (using Reserve or Wait) but did not yet act before SetLimitAt was called.

```go
func (lim *Limiter) Tokens() float64
```

Tokens returns the number of tokens available now.

```go
func (lim *Limiter) TokensAt(t time.Time) float64
```

TokensAt returns the number of tokens available at time t.

```go
func (lim *Limiter) Wait(ctx context.Context) (err error)
```

Wait is shorthand for WaitN(ctx, 1).

```go
func (lim *Limiter) WaitN(ctx context.Context, n int) (err error)
```

WaitN blocks until lim permits n events to happen. It returns an error if n exceeds the Limiter's burst size, the Context is canceled, or the expected wait time exceeds the Context's Deadline. The burst limit is ignored if the rate limit is Inf.

```go
type Reservation struct {
	// contains filtered or unexported fields
}
```

A Reservation holds information about events that are permitted by a Limiter to happen after a delay. A Reservation may be canceled, which may enable the Limiter to permit additional events.

```go
func (r *Reservation) Cancel()
```

Cancel is shorthand for CancelAt(time.Now()).

```go
func (r *Reservation) CancelAt(t time.Time)
```

CancelAt indicates that the reservation holder will not perform the reserved action and reverses the effects of this Reservation on the rate limit as much as possible, considering that other reservations may have already been made.

```go
func (r *Reservation) Delay() time.Duration
```

Delay is shorthand for DelayFrom(time.Now()).

```go
func (r *Reservation) DelayFrom(t time.Time) time.Duration
```

DelayFrom returns the duration for which the reservation holder must wait before taking the reserved action. Zero duration means act immediately. InfDuration means the limiter cannot grant the tokens requested in this Reservation within the maximum wait time.

```go
func (r *Reservation) OK() bool
```

OK returns whether the limiter can provide the requested number of tokens within the maximum wait time. If OK is false, Delay returns InfDuration, and Cancel does nothing.

```go
type Sometimes struct {
	First    int           // if non-zero, the first N calls to Do will run f.
	Every    int           // if non-zero, every Nth call to Do will run f.
	Interval time.Duration // if non-zero and Interval has elapsed since f's last run, Do will run f.
	// contains filtered or unexported fields
}
```

Sometimes will perform an action occasionally. The First, Every, and Interval fields govern the behavior of Do, which performs the action. A zero Sometimes value will perform an action exactly once.

#### Example: logging with rate limiting ¶

```go
var sometimes = rate.Sometimes{First: 3, Interval: 10*time.Second}
func Spammy() {
        sometimes.Do(func() { log.Info("here I am!") })
}

```

```go

package main

import (
	"fmt"

"golang.org/x/time/rate"
)

func main() {
	s := rate.Sometimes{Every: 2}
	s.Do(func() { fmt.Println("1") })
	s.Do(func() { fmt.Println("2") })
	s.Do(func() { fmt.Println("3") })
}

```

```go
Output:
1
3

```

Share Format Run

```go

package main

import (
	"fmt"

"golang.org/x/time/rate"
)

func main() {
	s := rate.Sometimes{First: 2}
	s.Do(func() { fmt.Println("1") })
	s.Do(func() { fmt.Println("2") })
	s.Do(func() { fmt.Println("3") })
}

```

```go
Output:
1
2

```

Share Format Run

```go

package main

import (
	"fmt"
	"time"

"golang.org/x/time/rate"
)

func main() {
	s := rate.Sometimes{Interval: 1 * time.Second}
	s.Do(func() { fmt.Println("1") })
	s.Do(func() { fmt.Println("2") })
	time.Sleep(1 * time.Second)
	s.Do(func() { fmt.Println("3") })
}

```

```go
Output:
1
3

```

Share Format Run

```go

package main

import (
	"fmt"
	"time"

"golang.org/x/time/rate"
)

func main() {
	s := rate.Sometimes{
		First:    2,
		Every:    2,
		Interval: 2 * time.Second,
	}
	s.Do(func() { fmt.Println("1 (First:2)") })
	s.Do(func() { fmt.Println("2 (First:2)") })
	s.Do(func() { fmt.Println("3 (Every:2)") })
	time.Sleep(2 * time.Second)
	s.Do(func() { fmt.Println("4 (Interval)") })
	s.Do(func() { fmt.Println("5 (Every:2)") })
	s.Do(func() { fmt.Println("6") })
}

```

```go
Output:
1 (First:2)
2 (First:2)
3 (Every:2)
4 (Interval)
5 (Every:2)

```

Share Format Run

```go

package main

import (
	"fmt"

"golang.org/x/time/rate"
)
