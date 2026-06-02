---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/subtests"
source_path: "sources/raw/external/go-dev-blog-subtests-0e125eccbd.html"
license_ref: ""
---

# The Go Blog

## Running specific tests or benchmarks

Both subtests and sub-benchmarks can be singled out on the command line using the `-run` or `-bench` flag. Both flags take a slash-separated list of regular expressions that match the corresponding parts of the full name of the subtest or sub-benchmark.

The full name of a subtest or sub-benchmark is a slash-separated list of its name and the names of all of its parents, starting with the top-level. The name is the corresponding function name for top-level tests and benchmarks, and the first argument to `Run` otherwise. To avoid display and parsing issues, a name is sanitized by replacing spaces with underscores and escaping non-printable characters. The same sanitizing is applied to the regular expressions passed to the `-run` or `-bench` flags.

A few examples:

Run tests that use a timezone in Europe:

```go
$ go test -run=TestTime/"in Europe"
--- FAIL: TestTime (0.00s)
    --- FAIL: TestTime/12:31_in_Europe/Zuri (0.00s)
        time_test.go:85: could not load location

```

Run only tests for times after noon:

```go
$ go test -run=Time/12:[0-9] -v
=== RUN   TestTime
=== RUN   TestTime/12:31_in_Europe/Zuri
=== RUN   TestTime/12:31_in_America/New_York
--- FAIL: TestTime (0.00s)
    --- FAIL: TestTime/12:31_in_Europe/Zuri (0.00s)
        time_test.go:85: could not load location
    --- FAIL: TestTime/12:31_in_America/New_York (0.00s)
        time_test.go:89: got 07:31; want 7:31

```

Perhaps a bit surprising, using `-run=TestTime/New_York` won’t match any tests. This is because the slash present in the location names is treated as a separator as well. Instead use:

```go
$ go test -run=Time//New_York
--- FAIL: TestTime (0.00s)
    --- FAIL: TestTime/12:31_in_America/New_York (0.00s)
        time_test.go:88: got 07:31; want 7:31

```

Note the `//` in the string passed to `-run`. The `/` in time zone name `America/New_York` is handled as if it were a separator resulting from a subtest. The first regular expression of the pattern (`TestTime`) matches the top-level test. The second regular expression (the empty string) matches anything, in this case the time and the continent part of the location. The third regular expression (`New_York`) matches the city part of the location.

Treating slashes in names as separators allows the user to refactor hierarchies of tests without the need to change the naming. It also simplifies the escaping rules. The user should escape slashes in names, for instance by replacing them with backslashes, if this poses a problem.

A unique sequence number is appended to test names that are not unique. So one could just pass an empty string to `Run` if there is no obvious naming scheme for subtests and the subtests can easily be identified by their sequence number.
