---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/math/rand"
source_path: "sources/raw/external/pkg-go-dev-math-rand-ccaeadbdbe.html"
license_ref: ""
---

Uint64 returns a pseudo-random 64-bit value as a uint64 from the default Source.

```go
type Rand struct {
	// contains filtered or unexported fields
}
```

A Rand is a source of random numbers.

```go
func New(src Source) *Rand
```

New returns a new Rand that uses random values from src to generate other random values.

```go
func (r *Rand) ExpFloat64() float64
```

ExpFloat64 returns an exponentially distributed float64 in the range (0, +[math.MaxFloat64]] with an exponential distribution whose rate parameter (lambda) is 1 and whose mean is 1/lambda (1). To produce a distribution with a different rate parameter, callers can adjust the output using:

```go
sample = ExpFloat64() / desiredRateParameter

```

```go
func (r *Rand) Float32() float32
```

Float32 returns, as a float32, a pseudo-random number in the half-open interval [0.0,1.0).

```go
func (r *Rand) Float64() float64
```

Float64 returns, as a float64, a pseudo-random number in the half-open interval [0.0,1.0).

```go
func (r *Rand) Int() int
```

Int returns a non-negative pseudo-random int.

```go
func (r *Rand) Int31() int32
```

Int31 returns a non-negative pseudo-random 31-bit integer as an int32.

```go
func (r *Rand) Int31n(n int32) int32
```

Int31n returns, as an int32, a non-negative pseudo-random number in the half-open interval [0,n). It panics if n <= 0.

```go
func (r *Rand) Int63() int64
```

Int63 returns a non-negative pseudo-random 63-bit integer as an int64.

```go
func (r *Rand) Int63n(n int64) int64
```

Int63n returns, as an int64, a non-negative pseudo-random number in the half-open interval [0,n). It panics if n <= 0.

```go
func (r *Rand) Intn(n int) int
```

Intn returns, as an int, a non-negative pseudo-random number in the half-open interval [0,n). It panics if n <= 0.

```go
func (r *Rand) NormFloat64() float64
```

NormFloat64 returns a normally distributed float64 in the range -math.MaxFloat64 through +[math.MaxFloat64] inclusive, with standard normal distribution (mean = 0, stddev = 1). To produce a different normal distribution, callers can adjust the output using:

```go
sample = NormFloat64() * desiredStdDev + desiredMean

```

```go
func (r *Rand) Perm(n int) []int
```

Perm returns, as a slice of n ints, a pseudo-random permutation of the integers in the half-open interval [0,n).

```go
func (r *Rand) Read(p []byte) (n int, err error)
```

Read generates len(p) random bytes and writes them into p. It always returns len(p) and a nil error. Read should not be called concurrently with any other Rand method.

```go
func (r *Rand) Seed(seed int64)
```

Seed uses the provided seed value to initialize the generator to a deterministic state. Seed should not be called concurrently with any other Rand method.

```go
func (r *Rand) Shuffle(n int, swap func(i, j int))
```

Shuffle pseudo-randomizes the order of elements. n is the number of elements. Shuffle panics if n < 0. swap swaps the elements with indexes i and j.

```go
func (r *Rand) Uint32() uint32
```

Uint32 returns a pseudo-random 32-bit value as a uint32.

```go
func (r *Rand) Uint64() uint64
```

Uint64 returns a pseudo-random 64-bit value as a uint64.

```go
type Source interface {
	Int63() int64
	Seed(seed int64)
}
```

A Source represents a source of uniformly-distributed pseudo-random int64 values in the range [0, 1<<63).

A Source is not safe for concurrent use by multiple goroutines.

```go
func NewSource(seed int64) Source
```

NewSource returns a new pseudo-random Source seeded with the given value. Unlike the default Source used by top-level functions, this source is not safe for concurrent use by multiple goroutines. The returned Source implements Source64.

```go
type Source64 interface {
	Source
	Uint64() uint64
}
```

A Source64 is a Source that can also generate uniformly-distributed pseudo-random uint64 values in the range [0, 1<<64) directly. If a Rand r's underlying Source s implements Source64, then r.Uint64 returns the result of one call to s.Uint64 instead of making two calls to s.Int63.

```go
type Zipf struct {
	// contains filtered or unexported fields
}
```

A Zipf generates Zipf distributed variates.

```go
func NewZipf(r *Rand, s float64, v float64, imax uint64) *Zipf
```

NewZipf returns a Zipf variate generator. The generator generates values k ∈ [0, imax] such that P(k) is proportional to (v + k) ** (-s). Requirements: s > 1 and v >= 1.

```go
func (z *Zipf) Uint64() uint64
```

Uint64 returns a value drawn from the Zipf distribution described by the Zipf object.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/math/rand>

- exp.go <https://cs.opensource.google/go/go/+/go1.26.3:src/math/rand/exp.go>
- normal.go <https://cs.opensource.google/go/go/+/go1.26.3:src/math/rand/normal.go>
- rand.go <https://cs.opensource.google/go/go/+/go1.26.3:src/math/rand/rand.go>
- rng.go <https://cs.opensource.google/go/go/+/go1.26.3:src/math/rand/rng.go>
- zipf.go <https://cs.opensource.google/go/go/+/go1.26.3:src/math/rand/zipf.go>

##   Directories ¶
    Show internal   Expand all

v2
 Package rand implements pseudo-random number generators suitable for tasks such as simulation, but it should not be used for security-sensitive work.

Package rand implements pseudo-random number generators suitable for tasks such as simulation, but it should not be used for security-sensitive work.

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
