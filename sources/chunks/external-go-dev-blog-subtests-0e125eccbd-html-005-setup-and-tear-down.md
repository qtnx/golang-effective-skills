---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/subtests"
source_path: "sources/raw/external/go-dev-blog-subtests-0e125eccbd.html"
license_ref: ""
---

# The Go Blog

## Setup and Tear-down

Subtests and sub-benchmarks can be used to manage common setup and tear-down code:

```go
func TestFoo(t *testing.T) {
    // <setup code>
    t.Run("A=1", func(t *testing.T) { ... })
    t.Run("A=2", func(t *testing.T) { ... })
    t.Run("B=1", func(t *testing.T) {
        if !test(foo{B:1}) {
            t.Fail()
        }
    })
    // <tear-down code>
}

```

The setup and tear-down code will run if any of the enclosed subtests are run and will run at most once. This applies even if any of the subtests calls `Skip`, `Fail`, or `Fatal`.

# The Go Blog

## Control of Parallelism

Subtests allow fine-grained control over parallelism. To understand how to use subtests in the way it is important to understand the semantics of parallel tests.

Each test is associated with a test function. A test is called a parallel test if its test function calls the Parallel method on its instance of `testing.T`. A parallel test never runs concurrently with a sequential test and its execution is suspended until its calling test function, that of the parent test, has returned. The `-parallel` flag defines the maximum number of parallel tests that can run in parallel.

A test blocks until its test function returns and all of its subtests have completed. This means that the parallel tests that are run by a sequential test will complete before any other consecutive sequential test is run.

This behavior is identical for tests created by `Run` and top-level tests. In fact, under the hood top-level tests are implemented as subtests of a hidden master test.

### Run a group of tests in parallel

The above semantics allows for running a group of tests in parallel with each other but not with other parallel tests:

```go
func TestGroupedParallel(t *testing.T) {
    for _, tc := range testCases {
        tc := tc // capture range variable
        t.Run(tc.Name, func(t *testing.T) {
            t.Parallel()
            if got := foo(tc.in); got != tc.out {
                t.Errorf("got %v; want %v", got, tc.out)
            }
            ...
        })
    }
}

```

The outer test will not complete until all parallel tests started by `Run` have completed. As a result, no other parallel tests can run in parallel to these parallel tests.

Note that we need to capture the range variable to ensure that `tc` gets bound to the correct instance.

### Cleaning up after a group of parallel tests

In the previous example we used the semantics to wait on a group of parallel tests to complete before commencing other tests. The same technique can be used to clean up after a group of parallel tests that share common resources:

```go
func TestTeardownParallel(t *testing.T) {
    // <setup code>
    // This Run will not return until its parallel subtests complete.
    t.Run("group", func(t *testing.T) {
        t.Run("Test1", parallelTest1)
        t.Run("Test2", parallelTest2)
        t.Run("Test3", parallelTest3)
    })
    // <tear-down code>
}

```

The behavior of waiting on a group of parallel tests is identical to that of the previous example.
