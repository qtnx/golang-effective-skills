---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/golang.org/x/time/rate"
source_path: "sources/raw/external/pkg-go-dev-golang-org-x-time-rate-190336c8d1.html"
license_ref: ""
---

func main() {
	// The zero value of Sometimes behaves like sync.Once, though less efficiently.
	var s rate.Sometimes
	s.Do(func() { fmt.Println("1") })
	s.Do(func() { fmt.Println("2") })
	s.Do(func() { fmt.Println("3") })
}

```

```go
Output:
1

```

Share Format Run

```go
func (s *Sometimes) Do(f func())
```

Do runs the function f as allowed by First, Every, and Interval.

The model is a union (not intersection) of filters. The first call to Do always runs f. Subsequent calls to Do run f if allowed by First or Every or Interval.

A non-zero First:N causes the first N Do(f) calls to run f.

A non-zero Every:M causes every Mth Do(f) call, starting with the first, to run f.

A non-zero Interval causes Do(f) to run f if Interval has elapsed since Do last ran f.

Specifying multiple filters produces the union of these execution streams. For example, specifying both First:N and Every:M causes the first N Do(f) calls and every Mth Do(f) call, starting with the first, to run f. See Examples for more.

If Do is called multiple times simultaneously, the calls will block and run serially. Therefore, Do is intended for lightweight operations.

Because a call to Do may block until f returns, if f causes Do to be called, it will deadlock.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/x/time/+/v0.15.0:rate>

- rate.go <https://cs.opensource.google/go/x/time/+/v0.15.0:rate/rate.go>
- sometimes.go <https://cs.opensource.google/go/x/time/+/v0.15.0:rate/sometimes.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
