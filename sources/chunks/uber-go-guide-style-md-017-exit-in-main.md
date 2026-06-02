---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

## Guidelines

### Exit in Main

Go programs use [`os.Exit`](https://pkg.go.dev/os#Exit) or [`log.Fatal*`](https://pkg.go.dev/log#Fatal) to exit immediately. (Panicking
is not a good way to exit programs, please [don't panic](#dont-panic).)

Call one of `os.Exit` or `log.Fatal*` **only in `main()`**. All other
functions should return errors to signal failure.

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
func main() {
  body := readFile(path)
  fmt.Println(body)
}

func readFile(path string) string {
  f, err := os.Open(path)
  if err != nil {
    log.Fatal(err)
  }

  b, err := io.ReadAll(f)
  if err != nil {
    log.Fatal(err)
  }

  return string(b)
}
```

</td><td>

```go
func main() {
  body, err := readFile(path)
  if err != nil {
    log.Fatal(err)
  }
  fmt.Println(body)
}

func readFile(path string) (string, error) {
  f, err := os.Open(path)
  if err != nil {
    return "", err
  }

  b, err := io.ReadAll(f)
  if err != nil {
    return "", err
  }

  return string(b), nil
}
```

</td></tr>
</tbody></table>

Rationale: Programs with multiple functions that exit present a few issues:

- Non-obvious control flow: Any function can exit the program so it becomes
  difficult to reason about the control flow.
- Difficult to test: A function that exits the program will also exit the test
  calling it. This makes the function difficult to test and introduces risk of
  skipping other tests that have not yet been run by `go test`.
- Skipped cleanup: When a function exits the program, it skips function calls
  enqueued with `defer` statements. This adds risk of skipping important
  cleanup tasks.

#### Exit Once

If possible, prefer to call `os.Exit` or `log.Fatal` **at most once** in your
`main()`. If there are multiple error scenarios that halt program execution,
put that logic under a separate function and return errors from it.

This has the effect of shortening your `main()` function and putting all key
business logic into a separate, testable function.

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
package main

func main() {
  args := os.Args[1:]
  if len(args) != 1 {
    log.Fatal("missing file")
  }
  name := args[0]

  f, err := os.Open(name)
  if err != nil {
    log.Fatal(err)
  }
  defer f.Close()

  // If we call log.Fatal after this line,
  // f.Close will not be called.

  b, err := io.ReadAll(f)
  if err != nil {
    log.Fatal(err)
  }

  // ...
}
```

</td><td>

```go
package main

func main() {
  if err := run(); err != nil {
    log.Fatal(err)
  }
}

func run() error {
  args := os.Args[1:]
  if len(args) != 1 {
    return errors.New("missing file")
  }
  name := args[0]

  f, err := os.Open(name)
  if err != nil {
    return err
  }
  defer f.Close()

  b, err := io.ReadAll(f)
  if err != nil {
    return err
  }

  // ...
}
```

</td></tr>
</tbody></table>

The example above uses `log.Fatal`, but the guidance also applies to
`os.Exit` or any library code that calls `os.Exit`.

```go
func main() {
  if err := run(); err != nil {
    fmt.Fprintln(os.Stderr, err)
    os.Exit(1)
  }
}
```

You may alter the signature of `run()` to fit your needs.
For example, if your program must exit with specific exit codes for failures,
`run()` may return the exit code instead of an error.
This allows unit tests to verify this behavior directly as well.

```go
func main() {
  os.Exit(run(args))
}

func run() (exitCode int) {
  // ...
}
```

More generally, note that the `run()` function used in these examples
is not intended to be prescriptive.
There's flexibility in the name, signature, and setup of the `run()` function.
Among other things, you may:

- accept unparsed command line arguments (e.g., `run(os.Args[1:])`)
- parse command line arguments in `main()` and pass them onto `run`
- use a custom error type to carry the exit code back to `main()`
- put business logic in a different layer of abstraction from `package main`

This guidance only requires that there's a single place in your `main()`
responsible for actually exiting the process.
