---
source_name: "External Linked Documentation"
source_url: "https://go.dev/design/43651-type-parameters"
source_path: "sources/raw/external/go-dev-design-43651-type-parameters-8b418b79f1.html"
license_ref: ""
---

## Examples

### Absolute difference

Compute the absolute difference between two numeric values, by using an `Abs` method. This uses the same `Numeric` constraint defined in the last example.

This example uses more machinery than is appropriate for the simple case of computing the absolute difference. It is intended to show how the common part of algorithms can be factored into code that uses methods, where the exact definition of the methods can vary based on the kind of type being used.

Note: the code used in this example will not work in Go 1.18. We hope to resolve this and make it work in future releases.

```go
// NumericAbs matches numeric types with an Abs method.
type NumericAbs[T any] interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64 |
		~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr |
		~float32 | ~float64 |
		~complex64 | ~complex128
	Abs() T
}

// AbsDifference computes the absolute value of the difference of
// a and b, where the absolute value is determined by the Abs method.
func AbsDifference[T NumericAbs[T]](a, b T) T {
	d := a - b
	return d.Abs()
}

```

We can define an `Abs` method appropriate for different numeric types.

```go
// OrderedNumeric matches numeric types that support the < operator.
type OrderedNumeric interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64 |
		~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr |
		~float32 | ~float64
}

// Complex matches the two complex types, which do not have a < operator.
type Complex interface {
	~complex64 | ~complex128
}

// OrderedAbs is a helper type that defines an Abs method for
// ordered numeric types.
type OrderedAbs[T OrderedNumeric] T

func (a OrderedAbs[T]) Abs() OrderedAbs[T] {
	if a < 0 {
		return -a
	}
	return a
}

// ComplexAbs is a helper type that defines an Abs method for
// complex types.
type ComplexAbs[T Complex] T

func (a ComplexAbs[T]) Abs() ComplexAbs[T] {
	d := math.Hypot(float64(real(a)), float64(imag(a)))
	return ComplexAbs[T](complex(d, 0))
}

```

We can then define functions that do the work for the caller by converting to and from the types we just defined.

```go
// OrderedAbsDifference returns the absolute value of the difference
// between a and b, where a and b are of an ordered type.
func OrderedAbsDifference[T OrderedNumeric](a, b T) T {
	return T(AbsDifference(OrderedAbs[T](a), OrderedAbs[T](b)))
}

// ComplexAbsDifference returns the absolute value of the difference
// between a and b, where a and b are of a complex type.
func ComplexAbsDifference[T Complex](a, b T) T {
	return T(AbsDifference(ComplexAbs[T](a), ComplexAbs[T](b)))
}

```

It's worth noting that this design is not powerful enough to write code like the following:

```go
// This function is INVALID.
func GeneralAbsDifference[T Numeric](a, b T) T {
	switch (interface{})(a).(type) {
	case int, int8, int16, int32, int64,
		uint, uint8, uint16, uint32, uint64, uintptr,
		float32, float64:
		return OrderedAbsDifference(a, b) // INVALID
	case complex64, complex128:
		return ComplexAbsDifference(a, b) // INVALID
	}
}

```

The calls to `OrderedAbsDifference` and `ComplexAbsDifference` are invalid, because not all the types that implement the `Numeric` constraint can implement the `OrderedNumeric` or `Complex` constraints. Although the type switch means that this code would conceptually work at run time, there is no support for writing this code at compile time. This is another way of expressing one of the omissions listed above: this design does not provide for specialization.
