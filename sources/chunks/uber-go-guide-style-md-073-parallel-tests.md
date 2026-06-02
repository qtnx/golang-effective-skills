---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

#### Parallel Tests

Parallel tests, like some specialized loops (for example, those that spawn
goroutines or capture references as part of the loop body),
must take care to explicitly assign loop variables within the loop's scope to
ensure that they hold the expected values.

```go
tests := []struct{
  give string
  // ...
}{
  // ...
}

for _, tt := range tests {
  t.Run(tt.give, func(t *testing.T) {
    t.Parallel()
    // ...
  })
}
```

In the example above, we must declare a `tt` variable scoped to the loop
iteration because of the use of `t.Parallel()` below.
If we do not do that, most or all tests will receive an unexpected value for
`tt`, or a value that changes as they're running.

<!-- TODO: Explain how to use _test packages. -->
