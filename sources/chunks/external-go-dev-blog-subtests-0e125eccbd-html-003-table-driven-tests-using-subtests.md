---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/subtests"
source_path: "sources/raw/external/go-dev-blog-subtests-0e125eccbd.html"
license_ref: ""
---

# The Go Blog

## Table-driven tests using subtests

Go 1.7 also introduces a `Run` method for creating subtests. This test is a rewritten version of our earlier example using subtests:

```go
func TestTime(t *testing.T) {
    testCases := []struct {
        gmt  string
        loc  string
        want string
    }{
        {"12:31", "Europe/Zuri", "13:31"},
        {"12:31", "America/New_York", "7:31"},
        {"08:08", "Australia/Sydney", "18:08"},
    }
    for _, tc := range testCases {
        t.Run(fmt.Sprintf("%s in %s", tc.gmt, tc.loc), func(t *testing.T) {
            loc, err := time.LoadLocation(tc.loc)
            if err != nil {
                t.Fatal("could not load location")
            }
            gmt, _ := time.Parse("15:04", tc.gmt)
            if got := gmt.In(loc).Format("15:04"); got != tc.want {
                t.Errorf("got %s; want %s", got, tc.want)
            }
        })
    }
}

```

The first thing to note is the difference in output from the two implementations. The original implementation prints:

```go
--- FAIL: TestTime (0.00s)
    time_test.go:62: could not load location "Europe/Zuri"

```

Even though there are two errors, execution of the test halts on the call to `Fatalf` and the second test never runs.

The implementation using `Run` prints both:

```go
--- FAIL: TestTime (0.00s)
    --- FAIL: TestTime/12:31_in_Europe/Zuri (0.00s)
        time_test.go:84: could not load location
    --- FAIL: TestTime/12:31_in_America/New_York (0.00s)
        time_test.go:88: got 07:31; want 7:31

```

`Fatal` and its siblings causes a subtest to be skipped but not its parent or subsequent subtests.

Another thing to note is the shorter error messages in the new implementation. Since the subtest name uniquely identifies the subtest there is no need to identify the test again within the error messages.

There are several other benefits to using subtests or sub-benchmarks, as clarified by the following sections.
