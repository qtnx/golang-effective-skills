expvar package - expvar - Go Packages

## Details

-     Valid go.mod <https://cs.opensource.google/go/go/+/go1.26.3:src/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/go  <https://cs.opensource.google/go/go>

## Links

-    Report a Vulnerability  <https://go.dev/security/policy>

##   Documentation ¶

Package expvar provides a standardized interface to public variables, such as operation counters in servers. It exposes these variables via HTTP at /debug/vars in JSON format. As of Go 1.22, the /debug/vars request must use GET.

Operations to set or modify these public variables are atomic.

In addition to adding the HTTP handler, this package registers the following variables:

```go
cmdline   os.Args
memstats  runtime.Memstats

```

The package is sometimes only imported for the side effect of registering its HTTP handler and the above variables. To use it this way, link this package into your program:

```go
import _ "expvar"

```

-  func Do(f func(KeyValue))
-  func Handler() http.Handler
-  func Publish(name string, v Var)
-  type Float
-
-  func NewFloat(name string) *Float

-
-  func (v *Float) Add(delta float64)
-  func (v *Float) Set(value float64)
-  func (v *Float) String() string
-  func (v *Float) Value() float64

-  type Func
-
-  func (f Func) String() string
-  func (f Func) Value() any

-  type Int
-
-  func NewInt(name string) *Int

-
-  func (v *Int) Add(delta int64)
-  func (v *Int) Set(value int64)
-  func (v *Int) String() string
-  func (v *Int) Value() int64

-  type KeyValue
-  type Map
-
-  func NewMap(name string) *Map

-
-  func (v *Map) Add(key string, delta int64)
-  func (v *Map) AddFloat(key string, delta float64)
-  func (v *Map) Delete(key string)
-  func (v *Map) Do(f func(KeyValue))
-  func (v *Map) Get(key string) Var
-  func (v *Map) Init() *Map
-  func (v *Map) Set(key string, av Var)
-  func (v *Map) String() string

-  type String
-
-  func NewString(name string) *String

-
-  func (v *String) Set(value string)
-  func (v *String) String() string
-  func (v *String) Value() string

-  type Var
-
-  func Get(name string) Var

This section is empty.

This section is empty.

```go
func Do(f func(KeyValue))
```

Do calls f for each exported variable. The global variable map is locked during the iteration, but existing entries may be concurrently updated.

```go
func Handler() http.Handler
```

Handler returns the expvar HTTP Handler.

This is only needed to install the handler in a non-standard location.

```go
func Publish(name string, v Var)
```

Publish declares a named exported variable. This should be called from a package's init function when it creates its Vars. If the name is already registered then this will log.Panic.

```go
type Float struct {
	// contains filtered or unexported fields
}
```

Float is a 64-bit float variable that satisfies the Var interface.

```go
func NewFloat(name string) *Float
```

```go
func (v *Float) Add(delta float64)
```

Add adds delta to v.

```go
func (v *Float) Set(value float64)
```

Set sets v to value.

```go
func (v *Float) String() string
```

```go
func (v *Float) Value() float64
```

```go
type Func func() any
```

Func implements Var by calling the function and formatting the returned value using JSON.

```go
func (f Func) String() string
```

```go
func (f Func) Value() any
```

```go
type Int struct {
	// contains filtered or unexported fields
}
```

Int is a 64-bit integer variable that satisfies the Var interface.

```go
func NewInt(name string) *Int
```

```go
func (v *Int) Add(delta int64)
```

```go
func (v *Int) Set(value int64)
```

```go
func (v *Int) String() string
```

```go
func (v *Int) Value() int64
```

```go
type KeyValue struct {
	Key   string
	Value Var
}
```

KeyValue represents a single entry in a Map.

```go
type Map struct {
	// contains filtered or unexported fields
}
```

Map is a string-to-Var map variable that satisfies the Var interface.

```go
func NewMap(name string) *Map
```

```go
func (v *Map) Add(key string, delta int64)
```

Add adds delta to the *Int value stored under the given map key.

```go
func (v *Map) AddFloat(key string, delta float64)
```

AddFloat adds delta to the *Float value stored under the given map key.

```go
func (v *Map) Delete(key string)
```

Delete deletes the given key from the map.

```go
func (v *Map) Do(f func(KeyValue))
```

Do calls f for each entry in the map. The map is locked during the iteration, but existing entries may be concurrently updated.

```go
func (v *Map) Get(key string) Var
```

```go
func (v *Map) Init() *Map
```

Init removes all keys from the map.

```go
func (v *Map) Set(key string, av Var)
```

```go
func (v *Map) String() string
```

```go
type String struct {
	// contains filtered or unexported fields
}
```

String is a string variable, and satisfies the Var interface.

```go
func NewString(name string) *String
```

```go
func (v *String) Set(value string)
```

```go
func (v *String) String() string
```

String implements the Var interface. To get the unquoted string use String.Value.

```go
func (v *String) Value() string
```

```go
type Var interface {
	// String returns a valid JSON value for the variable.
	// Types with String methods that do not return valid JSON
	// (such as time.Time) must not be used as a Var.
	String() string
}
```

Var is an abstract type for all exported variables.

```go
func Get(name string) Var
```

Get retrieves a named exported variable. It returns nil if the name has not been registered.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/expvar>

- expvar.go <https://cs.opensource.google/go/go/+/go1.26.3:src/expvar/expvar.go>

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
