---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Comparison operators

 Comparison operators compare two operands and yield an untyped boolean value.

```go

==    equal
!=    not equal
<     less
<=    less or equal
>     greater
>=    greater or equal

```

 In any comparison, the first operand must be assignable to the type of the second operand, or vice versa.

 The equality operators `==` and `!=` apply to operands of _comparable_ types. The ordering operators `<`, `<=`, `>`, and `>=` apply to operands of _ordered_ types. These terms and the result of the comparisons are defined as follows:

-  Boolean types are comparable. Two boolean values are equal if they are either both `true` or both `false`.
-  Integer types are comparable and ordered. Two integer values are compared in the usual way.
-  Floating-point types are comparable and ordered. Two floating-point values are compared as defined by the IEEE 754 standard.
-  Complex types are comparable. Two complex values `u` and `v` are equal if both `real(u) == real(v)` and `imag(u) == imag(v)`.
-  String types are comparable and ordered. Two string values are compared lexically byte-wise.
-  Pointer types are comparable. Two pointer values are equal if they point to the same variable or if both have value `nil`. Pointers to distinct zero-size variables may or may not be equal.
-  Channel types are comparable. Two channel values are equal if they were created by the same call to `make` or if both have value `nil`.
-  Interface types that are not type parameters are comparable. Two interface values are equal if they have identical dynamic types and equal dynamic values or if both have value `nil`.
-  A value `x` of non-interface type `X` and a value `t` of interface type `T` can be compared if type `X` is comparable and `X` implements `T`. They are equal if `t`'s dynamic type is identical to `X` and `t`'s dynamic value is equal to `x`.
-  Struct types are comparable if all their field types are comparable. Two struct values are equal if their corresponding non-blank field values are equal. The fields are compared in source order, and comparison stops as soon as two field values differ (or all fields have been compared).
-  Array types are comparable if their array element types are comparable. Two array values are equal if their corresponding element values are equal. The elements are compared in ascending index order, and comparison stops as soon as two element values differ (or all elements have been compared).
-  Type parameters are comparable if they are strictly comparable (see below).

 A comparison of two interface values with identical dynamic types causes a run-time panic if that type is not comparable. This behavior applies not only to direct interface value comparisons but also when comparing arrays of interface values or structs with interface-valued fields.

 Slice, map, and function types are not comparable. However, as a special case, a slice, map, or function value may be compared to the predeclared identifier `nil`. Comparison of pointer, channel, and interface values to `nil` is also allowed and follows from the general rules above.

```go

const c = 3 < 4            // c is the untyped boolean constant true

type MyBool bool
var x, y int
var (
	// The result of a comparison is an untyped boolean.
	// The usual assignment rules apply.
	b3        = x == y // b3 has type bool
	b4 bool   = x == y // b4 has type bool
	b5 MyBool = x == y // b5 has type MyBool
)

```

 A type is _strictly comparable_ if it is comparable and not an interface type nor composed of interface types. Specifically:

-  Boolean, numeric, string, pointer, and channel types are strictly comparable.
-  Struct types are strictly comparable if all their field types are strictly comparable.
-  Array types are strictly comparable if their array element types are strictly comparable.
-  Type parameters are strictly comparable if all types in their type set are strictly comparable.
