---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/fuzz"
source_path: "sources/raw/external/go-dev-doc-fuzz-ee5f17aa89.html"
license_ref: ""
---

# Go Fuzzing

## Running fuzz tests

There are two modes of running your fuzz test: as a unit test (default `go test`), or with fuzzing (`go test -fuzz=FuzzTestName`).

Fuzz tests are run much like a unit test by default. Each seed corpus entry will be tested against the fuzz target, reporting any failures before exiting.

To enable fuzzing, run `go test` with the `-fuzz` flag, providing a regex matching a single fuzz test. By default, all other tests in that package will run before fuzzing begins. This is to ensure that fuzzing won’t report any issues that would already be caught by an existing test.

Note that it is up to you to decide how long to run fuzzing. It is very possible that an execution of fuzzing could run indefinitely if it doesn’t find any errors. There will be support to run these fuzz tests continuously using tools like OSS-Fuzz in the future, see Issue #50192.

**Note:** Fuzzing should be run on a platform that supports coverage instrumentation (currently AMD64 and ARM64) so that the corpus can meaningfully grow as it runs, and more code can be covered while fuzzing.

### Command line output

While fuzzing is in progress, the fuzzing engine generates new inputs and runs them against the provided fuzz target. By default, it continues to run until a failing input is found, or the user cancels the process (e.g. with Ctrl^C).

The output will look something like this:

```go
~ go test -fuzz FuzzFoo
fuzz: elapsed: 0s, gathering baseline coverage: 0/192 completed
fuzz: elapsed: 0s, gathering baseline coverage: 192/192 completed, now fuzzing with 8 workers
fuzz: elapsed: 3s, execs: 325017 (108336/sec), new interesting: 11 (total: 202)
fuzz: elapsed: 6s, execs: 680218 (118402/sec), new interesting: 12 (total: 203)
fuzz: elapsed: 9s, execs: 1039901 (119895/sec), new interesting: 19 (total: 210)
fuzz: elapsed: 12s, execs: 1386684 (115594/sec), new interesting: 21 (total: 212)
PASS
ok      foo 12.692s

```

The first lines indicate that the “baseline coverage” is gathered before fuzzing begins.

To gather baseline coverage, the fuzzing engine executes both the seed corpus and the generated corpus, to ensure that no errors occurred and to understand the code coverage the existing corpus already provides.

The lines following provide insight into the active fuzzing execution:

- elapsed: the amount of time that has elapsed since the process began
- execs: the total number of inputs that have been run against the fuzz target (with an average execs/sec since the last log line)
- new interesting: the total number of “interesting” inputs that have been added to the generated corpus during this fuzzing execution (with the total size of the entire corpus)

For an input to be “interesting”, it must expand the code coverage beyond what the existing generated corpus can reach. It’s typical for the number of new interesting inputs to grow quickly at the start and eventually slow down, with occasional bursts as new branches are discovered.

You should expect to see the “new interesting” number taper off over time as the inputs in the corpus begin to cover more lines of the code, with occasional bursts if the fuzzing engine finds a new code path.

### Failing input

A failure may occur while fuzzing for several reasons:

- A panic occurred in the code or the test.
- The fuzz target called `t.Fail`, either directly or through methods such as `t.Error` or `t.Fatal`.
- A non-recoverable error occurred, such as an `os.Exit` or stack overflow.
- The fuzz target took too long to complete. Currently, the timeout for an execution of a fuzz target is 1 second. This may fail due to a deadlock or infinite loop, or from intended behavior in the code. This is one reason why it is suggested that your fuzz target be fast.

If an error occurs, the fuzzing engine will attempt to minimize the input to the smallest possible and most human readable value which will still produce an error. To configure this, see the custom settings section.

Once minimization is complete, the error message will be logged, and the output will end with something like this:

```go
    Failing input written to testdata/fuzz/FuzzFoo/a878c3134fe0404d44eb1e662e5d8d4a24beb05c3d68354903670ff65513ff49
    To re-run:
    go test -run=FuzzFoo/a878c3134fe0404d44eb1e662e5d8d4a24beb05c3d68354903670ff65513ff49
FAIL
exit status 1
FAIL    foo 0.839s

```

The fuzzing engine wrote this failing input to the seed corpus for that fuzz test, and it will now be run by default with `go test`, serving as a regression test once the bug has been fixed.

The next step for you will be to diagnose the problem, fix the bug, verify the fix by re-running `go test`, and submit the patch with the new testdata file acting as your regression test.

### Custom settings

The default go command settings should work for most use cases of fuzzing. So typically, an execution of fuzzing on the command line should look like this:

```go
$ go test -fuzz={FuzzTestName}

```

However, the `go` command does provide a few settings when running fuzzing. These are documented in the `cmd/go` package docs <https://pkg.go.dev/cmd/go>.

To highlight a few:

- `-fuzztime`: the total time or number of iterations that the fuzz target will be executed before exiting, default indefinitely.
- `-fuzzminimizetime`: the time or number of iterations that the fuzz target will be executed during each minimization attempt, default 60sec. You can completely disable minimization by setting `-fuzzminimizetime 0` when fuzzing.
- `-parallel`: the number of fuzzing processes running at once, default `$GOMAXPROCS`. Currently, setting -cpu during fuzzing has no effect.
