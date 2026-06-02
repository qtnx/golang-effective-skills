---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

## Guidelines

### Channel Size is One or None

Channels should usually have a size of one or be unbuffered. By default,
channels are unbuffered and have a size of zero. Any other size
must be subject to a high level of scrutiny. Consider how the size is
determined, what prevents the channel from filling up under load and blocking
writers, and what happens when this occurs.

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
// Ought to be enough for anybody!
c := make(chan int, 64)
```

</td><td>

```go
// Size of one
c := make(chan int, 1) // or
// Unbuffered channel, size of zero
c := make(chan int)
```

</td></tr>
</tbody></table>

## Guidelines

### Start Enums at One

The standard way of introducing enumerations in Go is to declare a custom type
and a `const` group with `iota`. Since variables have a 0 default value, you
should usually start your enums on a non-zero value.

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
type Operation int

const (
  Add Operation = iota
  Subtract
  Multiply
)

// Add=0, Subtract=1, Multiply=2
```

</td><td>

```go
type Operation int

const (
  Add Operation = iota + 1
  Subtract
  Multiply
)

// Add=1, Subtract=2, Multiply=3
```

</td></tr>
</tbody></table>

There are cases where using the zero value makes sense, for example when the
zero value case is the desirable default behavior.

```go
type LogOutput int

const (
  LogToStdout LogOutput = iota
  LogToFile
  LogToRemote
)

// LogToStdout=0, LogToFile=1, LogToRemote=2
```
