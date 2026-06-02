---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/golang.org/x/sync/errgroup"
source_path: "sources/raw/external/pkg-go-dev-golang-org-x-sync-errgroup-1521b1c850.html"
license_ref: ""
---

errgroup package - golang.org/x/sync/errgroup - Go Packages
## Details

-     Valid go.mod <https://cs.opensource.google/go/x/sync/+/v0.20.0:/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/x/sync  <https://cs.opensource.google/go/x/sync>

##   Documentation ¶

Package errgroup provides synchronization, error propagation, and Context cancellation for groups of goroutines working on subtasks of a common task.

errgroup.Group is related to sync.WaitGroup but adds handling of tasks returning errors.

-  type Group
-
-  func WithContext(ctx context.Context) (*Group, context.Context)

-
-  func (g *Group) Go(f func() error)
-  func (g *Group) SetLimit(n int)
-  func (g *Group) TryGo(f func() error) bool
-  func (g *Group) Wait() error

- Group (JustErrors)
- Group (Parallel)
- Group (Pipeline)

This section is empty.

This section is empty.

This section is empty.

```go
type Group struct {
	// contains filtered or unexported fields
}
```

A Group is a collection of goroutines working on subtasks that are part of the same overall task. A Group should not be reused for different tasks.

A zero Group is valid, has no limit on the number of active goroutines, and does not cancel on error.

JustErrors illustrates the use of a Group in place of a sync.WaitGroup to simplify goroutine counting and error handling. This example is derived from the sync.WaitGroup example at https://golang.org/pkg/sync/#example-WaitGroup <https://golang.org/pkg/sync/#example-WaitGroup>.

```go

package main

import (
	"fmt"
	"net/http"

	"golang.org/x/sync/errgroup"
)

func main() {
	g := new(errgroup.Group)
	var urls = []string{
		"http://www.golang.org/",
		"http://www.google.com/",
		"http://www.somestupidname.com/",
	}
	for _, url := range urls {
		// Launch a goroutine to fetch the URL.
		url := url // https://golang.org/doc/faq#closures_and_goroutines
		g.Go(func() error {
			// Fetch the URL.
			resp, err := http.Get(url)
			if err == nil {
				resp.Body.Close()
			}
			return err
		})
	}
	// Wait for all HTTP fetches to complete.
	if err := g.Wait(); err == nil {
		fmt.Println("Successfully fetched all URLs.")
	}
}

```

```go
Output:

```

 Share Format Run

Parallel illustrates the use of a Group for synchronizing a simple parallel task: the "Google Search 2.0" function from https://talks.golang.org/2012/concurrency.slide#46 <https://talks.golang.org/2012/concurrency.slide#46>, augmented with a Context and error-handling.

```go

package main

import (
	"context"
	"fmt"
	"os"

	"golang.org/x/sync/errgroup"
)

var (
	Web   = fakeSearch("web")
	Image = fakeSearch("image")
	Video = fakeSearch("video")
)

type Result string
type Search func(ctx context.Context, query string) (Result, error)

func fakeSearch(kind string) Search {
	return func(_ context.Context, query string) (Result, error) {
		return Result(fmt.Sprintf("%s result for %q", kind, query)), nil
	}
}

func main() {
	Google := func(ctx context.Context, query string) ([]Result, error) {
		g, ctx := errgroup.WithContext(ctx)

		searches := []Search{Web, Image, Video}
		results := make([]Result, len(searches))
		for i, search := range searches {
			i, search := i, search // https://golang.org/doc/faq#closures_and_goroutines
			g.Go(func() error {
				result, err := search(ctx, query)
				if err == nil {
					results[i] = result
				}
				return err
			})
		}
		if err := g.Wait(); err != nil {
			return nil, err
		}
		return results, nil
	}

	results, err := Google(context.Background(), "golang")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		return
	}
	for _, result := range results {
		fmt.Println(result)
	}

}

```

```go
Output:
web result for "golang"
image result for "golang"
video result for "golang"

```

 Share Format Run

Pipeline demonstrates the use of a Group to implement a multi-stage pipeline: a version of the MD5All function with bounded parallelism from https://blog.golang.org/pipelines <https://blog.golang.org/pipelines>.

```go

package main

import (
	"context"
	"crypto/md5"
	"fmt"
	"log"
	"os"
	"path/filepath"

	"golang.org/x/sync/errgroup"
)

// Pipeline demonstrates the use of a Group to implement a multi-stage
// pipeline: a version of the MD5All function with bounded parallelism from
// https://blog.golang.org/pipelines.
func main() {
	m, err := MD5All(context.Background(), ".")
	if err != nil {
		log.Fatal(err)
	}

	for k, sum := range m {
		fmt.Printf("%s:\t%x\n", k, sum)
	}
}

type result struct {
	path string
	sum  [md5.Size]byte
}

// MD5All reads all the files in the file tree rooted at root and returns a map
// from file path to the MD5 sum of the file's contents. If the directory walk
// fails or any read operation fails, MD5All returns an error.
func MD5All(ctx context.Context, root string) (map[string][md5.Size]byte, error) {
	// ctx is canceled when g.Wait() returns. When this version of MD5All returns
	// - even in case of error! - we know that all of the goroutines have finished
	// and the memory they were using can be garbage-collected.
	g, ctx := errgroup.WithContext(ctx)
	paths := make(chan string)

	g.Go(func() error {
		defer close(paths)
		return filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
			if !info.Mode().IsRegular() {
				return nil
			}
			select {
			case paths <- path:
			case <-ctx.Done():
				return ctx.Err()
			}
			return nil
		})
	})

	// Start a fixed number of goroutines to read and digest files.
	c := make(chan result)
	const numDigesters = 20
	for i := 0; i < numDigesters; i++ {
		g.Go(func() error {
			for path := range paths {
				data, err := os.ReadFile(path)
				if err != nil {
					return err
				}
				select {
				case c <- result{path, md5.Sum(data)}:
				case <-ctx.Done():
					return ctx.Err()
				}
			}
			return nil
		})
	}
	go func() {
		g.Wait()
		close(c)
	}()

	m := make(map[string][md5.Size]byte)
	for r := range c {
		m[r.path] = r.sum
	}
	// Check whether any of the goroutines failed. Since g is accumulating the
	// errors, we don't need to send them (or check for them) in the individual
	// results sent on the channel.
	if err := g.Wait(); err != nil {
		return nil, err
	}
	return m, nil
}

```

```go
Output:

```

 Share Format Run

```go
func WithContext(ctx context.Context) (*Group, context.Context)
```

WithContext returns a new Group and an associated Context derived from ctx.

The derived Context is canceled the first time a function passed to Go returns a non-nil error or the first time Wait returns, whichever occurs first.

```go
func (g *Group) Go(f func() error)
```

Go calls the given function in a new goroutine.

The first call to Go must happen before a Wait. It blocks until the new goroutine can be added without the number of goroutines in the group exceeding the configured limit.

The first goroutine in the group that returns a non-nil error will cancel the associated Context, if any. The error will be returned by Wait.

```go
func (g *Group) SetLimit(n int)
```

SetLimit limits the number of active goroutines in this group to at most n. A negative value indicates no limit. A limit of zero will prevent any new goroutines from being added.

Any subsequent call to the Go method will block until it can add an active goroutine without exceeding the configured limit.

The limit must not be modified while any goroutines in the group are active.

```go
func (g *Group) TryGo(f func() error) bool
```

TryGo calls the given function in a new goroutine only if the number of active goroutines in the group is currently below the configured limit.

The return value reports whether the goroutine was started.

```go
func (g *Group) Wait() error
```

Wait blocks until all function calls from the Go method have returned, then returns the first non-nil error (if any) from them.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/x/sync/+/v0.20.0:errgroup>

- errgroup.go <https://cs.opensource.google/go/x/sync/+/v0.20.0:errgroup/errgroup.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
