---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Statements

### For statements

A "for" statement specifies repeated execution of a block. There are three forms: The iteration may be controlled by a single condition, a "for" clause, or a "range" clause.

```go

ForStmt   = "for" [ Condition | ForClause | RangeClause ] Block .
Condition = Expression .

```

#### For statements with single condition

In its simplest form, a "for" statement specifies the repeated execution of a block as long as a boolean condition evaluates to true. The condition is evaluated before each iteration. If the condition is absent, it is equivalent to the boolean value `true`.

```go

for a < b {
	a *= 2
}

```

#### For statements with `for` clause

A "for" statement with a ForClause is also controlled by its condition, but additionally it may specify an _init_ and a _post_ statement, such as an assignment, an increment or decrement statement. The init statement may be a short variable declaration, but the post statement must not.

```go

ForClause = [ InitStmt ] ";" [ Condition ] ";" [ PostStmt ] .
InitStmt  = SimpleStmt .
PostStmt  = SimpleStmt .

```

```go

for i := 0; i < 10; i++ {
	f(i)
}

```

If non-empty, the init statement is executed once before evaluating the condition for the first iteration; the post statement is executed after each execution of the block (and only if the block was executed). Any element of the ForClause may be empty but the semicolons are required unless there is only a condition. If the condition is absent, it is equivalent to the boolean value `true`.

```go

for cond { S() }    is the same as    for ; cond ; { S() }
for      { S() }    is the same as    for true     { S() }

```

Each iteration has its own separate declared variable (or variables) [Go 1.22]. The variable used by the first iteration is declared by the init statement. The variable used by each subsequent iteration is declared implicitly before executing the post statement and initialized to the value of the previous iteration's variable at that moment.

```go

var prints []func()
for i := 0; i < 5; i++ {
	prints = append(prints, func() { println(i) })
	i++
}
for _, p := range prints {
	p()
}

```

prints

```go

1
3
5

```

Prior to [Go 1.22], iterations share one set of variables instead of having their own separate variables. In that case, the example above prints

```go

6
6
6

```

#### For statements with `range` clause

A "for" statement with a "range" clause iterates through all entries of an array, slice, string or map, values received on a channel, integer values from zero to an upper limit [Go 1.22], or values passed to an iterator function's yield function [Go 1.23]. For each entry it assigns _iteration values_ to corresponding _iteration variables_ if present and then executes the block.

```go

RangeClause = [ ExpressionList "=" | IdentifierList ":=" ] "range" Expression .

```

The expression on the right in the "range" clause is called the _range expression_, which may be an array, pointer to an array, slice, string, map, channel permitting receive operations, an integer, or a function with specific signature (see below). As with an assignment, if present the operands on the left must be addressable or map index expressions; they denote the iteration variables. If the range expression is a function, the maximum number of iteration variables depends on the function signature. If the range expression is a channel or integer, at most one iteration variable is permitted; otherwise there may be up to two. If the last iteration variable is the blank identifier, the range clause is equivalent to the same clause without that identifier.

The range expression `x` is evaluated before beginning the loop, with one exception: if at most one iteration variable is present and `x` or `len(x)` is constant, the range expression is not evaluated.

Function calls on the left are evaluated once per iteration. For each iteration, iteration values are produced as follows if the respective iteration variables are present:

```go

Range expression                                       1st value                2nd value

array or slice      a  [n]E, *[n]E, or []E             index    i  int          a[i]       E
string              s  string type                     index    i  int          see below  rune
map                 m  map[K]V                         key      k  K            m[k]       V
channel             c  chan E, <-chan E                element  e  E
integer value       n  integer type, or untyped int    value    i  see below
function, 0 values  f  func(func() bool)
function, 1 value   f  func(func(V) bool)              value    v  V
function, 2 values  f  func(func(K, V) bool)           key      k  K            v          V

```

-  For an array, pointer to array, or slice value `a`, the index iteration values are produced in increasing order, starting at element index 0. If at most one iteration variable is present, the range loop produces iteration values from 0 up to `len(a)-1` and does not index into the array or slice itself. For a `nil` slice, the number of iterations is 0.
-  For a string value, the "range" clause iterates over the Unicode code points in the string starting at byte index 0. On successive iterations, the index value will be the index of the first byte of successive UTF-8-encoded code points in the string, and the second value, of type `rune`, will be the value of the corresponding code point. If the iteration encounters an invalid UTF-8 sequence, the second value will be `0xFFFD`, the Unicode replacement character, and the next iteration will advance a single byte in the string.
-  The iteration order over maps is not specified and is not guaranteed to be the same from one iteration to the next. If a map entry that has not yet been reached is removed during iteration, the corresponding iteration value will not be produced. If a map entry is created during iteration, that entry may be produced during the iteration or may be skipped. The choice may vary for each entry created and from one iteration to the next. If the map is `nil`, the number of iterations is 0.
-  For channels, the iteration values produced are the successive values sent on the channel until the channel is closed. If the channel is `nil`, the range expression blocks forever.
-  For an integer value `n`, where `n` is of integer type or an untyped integer constant, the iteration values 0 through `n-1` are produced in increasing order. If `n` is of integer type, the iteration values have that same type. Otherwise, the type of `n` is determined as if it were assigned to the iteration variable. Specifically: if the iteration variable is preexisting, the type of the iteration values is the type of the iteration variable, which must be of integer type. Otherwise, if the iteration variable is declared by the "range" clause or is absent, the type of the iteration values is the default type for `n`. If `n` <= 0, the loop does not run any iterations.
-  For a function `f`, the iteration proceeds by calling `f` with a new, synthesized `yield` function as its argument. If `yield` is called before `f` returns, the arguments to `yield` become the iteration values for executing the loop body once. After each successive loop iteration, `yield` returns true and may be called again to continue the loop. As long as the loop body does not terminate, the "range" clause will continue to generate iteration values this way for each `yield` call until `f` returns. If the loop body terminates (such as by a `break` statement), `yield` returns false and must not be called again.

The iteration variables may be declared by the "range" clause using a form of short variable declaration (`:=`). In this case their scope is the block of the "for" statement and each iteration has its own new variables [Go 1.22] (see also "for" statements with a ForClause). The variables have the types of their respective iteration values.

If the iteration variables are not explicitly declared by the "range" clause, they must be preexisting. In this case, the iteration values are assigned to the respective variables as in an assignment statement.

```go

var testdata *struct {
	a *[7]int
}
for i, _ := range testdata.a {
	// testdata.a is never evaluated; len(testdata.a) is constant
	// i ranges from 0 to 6
	f(i)
}

var a [10]string
for i, s := range a {
	// type of i is int
	// type of s is string
	// s == a[i]
	g(i, s)
}

var key string
var val interface{}  // element type of m is assignable to val
m := map[string]int{"mon":0, "tue":1, "wed":2, "thu":3, "fri":4, "sat":5, "sun":6}
for key, val = range m {
	h(key, val)
}
// key == last map key encountered in iteration
// val == map[key]

var ch chan Work = producer()
for w := range ch {
	doWork(w)
}

// empty a channel
for range ch {}

// call f(0), f(1), ... f(9)
for i := range 10 {
	// type of i is int (default type for untyped constant 10)
	f(i)
}

// invalid: 256 cannot be assigned to uint8
var u uint8
for u = range 256 {
}

// invalid: 1e3 is a floating-point constant
for range 1e3 {
}

// fibo generates the Fibonacci sequence
fibo := func(yield func(x int) bool) {
	f0, f1 := 0, 1
	for yield(f0) {
		f0, f1 = f1, f0+f1
	}
}
