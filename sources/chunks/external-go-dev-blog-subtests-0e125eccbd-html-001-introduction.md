---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/subtests"
source_path: "sources/raw/external/go-dev-blog-subtests-0e125eccbd.html"
license_ref: ""
---

# The Go Blog

Using Subtests and Sub-benchmarks - The Go Programming Language
# The Go Blog
# Using Subtests and Sub-benchmarks
 Marcel van Lohuizen
 3 October 2016
## Introduction

In Go 1.7, the `testing` package introduces a Run method on the `T` and `B` types that allows for the creation of subtests and sub-benchmarks. The introduction of subtests and sub-benchmarks enables better handling of failures, fine-grained control of which tests to run from the command line, control of parallelism, and often results in simpler and more maintainable code.

# The Go Blog

## Table-driven tests basics

Before digging into the details, let’s first discuss a common way of writing tests in Go. A series of related checks can be implemented by looping over a slice of test cases:

```go
func TestTime(t *testing.T) {
    testCases := []struct {
        gmt  string
        loc  string
        want string
    }{
        {"12:31", "Europe/Zuri", "13:31"},     // incorrect location name
        {"12:31", "America/New_York", "7:31"}, // should be 07:31
        {"08:08", "Australia/Sydney", "18:08"},
    }
    for _, tc := range testCases {
        loc, err := time.LoadLocation(tc.loc)
        if err != nil {
            t.Fatalf("could not load location %q", tc.loc)
        }
        gmt, _ := time.Parse("15:04", tc.gmt)
        if got := gmt.In(loc).Format("15:04"); got != tc.want {
            t.Errorf("In(%s, %s) = %s; want %s", tc.gmt, tc.loc, got, tc.want)
        }
    }
}

```

This approach, commonly referred to as table-driven tests, reduces the amount of repetitive code compared to repeating the same code for each test and makes it straightforward to add more test cases.
