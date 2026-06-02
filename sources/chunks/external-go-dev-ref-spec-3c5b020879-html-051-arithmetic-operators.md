---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Arithmetic operators

 Arithmetic operators apply to numeric values and yield a result of the same type as the first operand. The four standard arithmetic operators (`+`, `-`, `*`, `/`) apply to integer, floating-point, and complex types; `+` also applies to strings. The bitwise logical and shift operators apply to integers only.

```go

+    sum                    integers, floats, complex values, strings
-    difference             integers, floats, complex values
*    product                integers, floats, complex values
/    quotient               integers, floats, complex values
%    remainder              integers

&    bitwise AND            integers
|    bitwise OR             integers
^    bitwise XOR            integers
&^   bit clear (AND NOT)    integers

<<   left shift             integer << integer >= 0
>>   right shift            integer >> integer >= 0

```

 If the operand type is a type parameter, the operator must apply to each type in that type set. The operands are represented as values of the type argument that the type parameter is instantiated with, and the operation is computed with the precision of that type argument. For example, given the function:

```go

func dotProduct[F ~float32|~float64](v1, v2 []F) F {
	var s F
	for i, x := range v1 {
		y := v2[i]
		s += x * y
	}
	return s
}

```

 the product `x * y` and the addition `s += x * y` are computed with `float32` or `float64` precision, respectively, depending on the type argument for `F`.

#### Integer operators

 For two integer values `x` and `y`, the integer quotient `q = x / y` and remainder `r = x % y` satisfy the following relationships:

```go

x = q*y + r  and  |r| < |y|

```

 with `x / y` truncated towards zero ("truncated division" <https://en.wikipedia.org/wiki/Modulo_operation>).

```go

 x     y     x / y     x % y
 5     3       1         2
-5     3      -1        -2
 5    -3      -1         2
-5    -3       1        -2

```

 The one exception to this rule is that if the dividend `x` is the most negative value for the int type of `x`, the quotient `q = x / -1` is equal to `x` (and `r = 0`) due to two's-complement integer overflow:

```go

                         x, q
int8                     -128
int16                  -32768
int32             -2147483648
int64    -9223372036854775808

```

 If the divisor is a constant, it must not be zero. If the divisor is zero at run time, a run-time panic occurs. If the dividend is non-negative and the divisor is a constant power of 2, the division may be replaced by a right shift, and computing the remainder may be replaced by a bitwise AND operation:

```go

 x     x / 4     x % 4     x >> 2     x & 3
 11      2         3         2          3
-11     -2        -3        -3          1

```

 The shift operators shift the left operand by the shift count specified by the right operand, which must be non-negative. If the shift count is negative at run time, a run-time panic occurs. The shift operators implement arithmetic shifts if the left operand is a signed integer and logical shifts if it is an unsigned integer. There is no upper limit on the shift count. Shifts behave as if the left operand is shifted `n` times by 1 for a shift count of `n`. As a result, `x << 1` is the same as `x*2` and `x >> 1` is the same as `x/2` but truncated towards negative infinity.

 For integer operands, the unary operators `+`, `-`, and `^` are defined as follows:

```go

+x                          is 0 + x
-x    negation              is 0 - x
^x    bitwise complement    is m ^ x  with m = "all bits set to 1" for unsigned x
                                      and  m = -1 for signed x

```

#### Integer overflow

 For unsigned integer values, the operations `+`, `-`, `*`, and `<<` are computed modulo 2_n_, where _n_ is the bit width of the unsigned integer's type. Loosely speaking, these unsigned integer operations discard high bits upon overflow, and programs may rely on "wrap around".

 For signed integers, the operations `+`, `-`, `*`, `/`, and `<<` may legally overflow and the resulting value exists and is deterministically defined by the signed integer representation, the operation, and its operands. Overflow does not cause a run-time panic. A compiler may not optimize code under the assumption that overflow does not occur. For instance, it may not assume that `x < x + 1` is always true.

#### Floating-point operators

 For floating-point and complex numbers, `+x` is the same as `x`, while `-x` is the negation of `x`. The result of a floating-point or complex division by zero is not specified beyond the IEEE 754 standard; whether a run-time panic occurs is implementation-specific.

 An implementation may combine multiple floating-point operations into a single fused operation, possibly across statements, and produce a result that differs from the value obtained by executing and rounding the instructions individually. An explicit floating-point type conversion rounds to the precision of the target type, preventing fusion that would discard that rounding.

 For instance, some architectures provide a "fused multiply and add" (FMA) instruction that computes `x*y + z` without rounding the intermediate result `x*y`. These examples show when a Go implementation can use that instruction:

```go

// FMA allowed for computing r, because x*y is not explicitly rounded:
r  = x*y + z
r  = z;   r += x*y
t  = x*y; r = t + z
*p = x*y; r = *p + z
r  = x*y + float64(z)

// FMA disallowed for computing r, because it would omit rounding of x*y:
r  = float64(x*y) + z
r  = z; r += float64(x*y)
t  = float64(x*y); r = t + z

```

#### String concatenation

 Strings can be concatenated using the `+` operator or the `+=` assignment operator:

```go

s := "hi" + string(c)
s += " and good bye"

```

 String addition creates a new string by concatenating the operands.
