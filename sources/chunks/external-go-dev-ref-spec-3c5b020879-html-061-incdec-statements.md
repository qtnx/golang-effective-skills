---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Statements

### IncDec statements

 The "++" and "--" statements increment or decrement their operands by the untyped constant `1`. As with an assignment, the operand must be addressable or a map index expression.

```go

IncDecStmt = Expression ( "++" | "--" ) .

```

 The following assignment statements are semantically equivalent:

```go

IncDec statement    Assignment
x++                 x += 1
x--                 x -= 1

```

## Statements

### Assignment statements

 An _assignment_ replaces the current value stored in a variable with a new value specified by an expression. An assignment statement may assign a single value to a single variable, or multiple values to a matching number of variables.

```go

Assignment = ExpressionList assign_op ExpressionList .

assign_op  = [ add_op | mul_op ] "=" .

```

 Each left-hand side operand must be addressable, a map index expression, or (for `=` assignments only) the blank identifier. Operands may be parenthesized.

```go

x = 1
*p = f()
a[i] = 23
(k) = <-ch  // same as: k = <-ch

```

 An _assignment operation_ `x` _op_`=` `y` where _op_ is a binary arithmetic operator is equivalent to `x` `=` `x` _op_ `(y)` but evaluates `x` only once. The _op_`=` construct is a single token. In assignment operations, both the left- and right-hand expression lists must contain exactly one single-valued expression, and the left-hand expression must not be the blank identifier.

```go

a[i] <<= 2
i &^= 1<<n

```

 A tuple assignment assigns the individual elements of a multi-valued operation to a list of variables. There are two forms. In the first, the right hand operand is a single multi-valued expression such as a function call, a channel or map operation, or a type assertion. The number of operands on the left hand side must match the number of values. For instance, if `f` is a function returning two values,

```go

x, y = f()

```

 assigns the first value to `x` and the second to `y`. In the second form, the number of operands on the left must equal the number of expressions on the right, each of which must be single-valued, and the _n_th expression on the right is assigned to the _n_th operand on the left:

```go

one, two, three = '一', '二', '三'

```

 The blank identifier provides a way to ignore right-hand side values in an assignment:

```go

_ = x       // evaluate x but ignore it
x, _ = f()  // evaluate f() but ignore second result value

```

 The assignment proceeds in two phases. First, the operands of index expressions and pointer indirections (including implicit pointer indirections in selectors) on the left and the expressions on the right are all evaluated in the usual order. Second, the assignments are carried out in left-to-right order.

```go

a, b = b, a  // exchange a and b

x := []int{1, 2, 3}
i := 0
i, x[i] = 1, 2  // set i = 1, x[0] = 2

i = 0
x[i], i = 2, 1  // set x[0] = 2, i = 1

x[0], x[0] = 1, 2  // set x[0] = 1, then x[0] = 2 (so x[0] == 2 at end)

x[1], x[3] = 4, 5  // set x[1] = 4, then panic setting x[3] = 5.

type Point struct { x, y int }
var p *Point
x[2], p.x = 6, 7  // set x[2] = 6, then panic setting p.x = 7

i = 2
x = []int{3, 5, 7}
for i, x[i] = range x {  // set i, x[2] = 0, x[0]
	break
}
// after this loop, i == 0 and x is []int{3, 5, 3}

```

 In assignments, each value must be assignable to the type of the operand to which it is assigned, with the following special cases:

-  Any typed value may be assigned to the blank identifier.
-  If an untyped constant is assigned to a variable of interface type or the blank identifier, the constant is first implicitly converted to its default type.
-  If an untyped boolean value is assigned to a variable of interface type or the blank identifier, it is first implicitly converted to type `bool`.

 When a value is assigned to a variable, only the data that is stored in the variable is replaced. If the value contains a reference, the assignment copies the reference but does not make a copy of the referenced data (such as the underlying array of a slice).

```go

var s1 = []int{1, 2, 3}
var s2 = s1                    // s2 stores the slice descriptor of s1
s1 = s1[:1]                    // s1's length is 1 but it still shares its underlying array with s2
s2[0] = 42                     // setting s2[0] changes s1[0] as well
fmt.Println(s1, s2)            // prints [42] [42 2 3]

var m1 = make(map[string]int)
var m2 = m1                    // m2 stores the map descriptor of m1
m1["foo"] = 42                 // setting m1["foo"] changes m2["foo"] as well
fmt.Println(m2["foo"])         // prints 42

```
