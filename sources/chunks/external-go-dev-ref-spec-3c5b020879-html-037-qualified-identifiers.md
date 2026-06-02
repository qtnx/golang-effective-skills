---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Expressions

### Qualified identifiers

 A _qualified identifier_ is an identifier qualified with a package name prefix. Both the package name and the identifier must not be blank.

```go

QualifiedIdent = PackageName "." identifier .

```

 A qualified identifier accesses an identifier in a different package, which must be imported. The identifier must be exported and declared in the package block of that package.

```go

math.Sin // denotes the Sin function in package math

```

## Expressions

### Composite literals

 Composite literals construct new values for structs, arrays, slices, and maps each time they are evaluated. They consist of the type of the literal followed by a (possibly empty) brace-bound list of elements. Each element may optionally be preceded by a corresponding key.

```go

CompositeLit = LiteralType LiteralValue .
LiteralType  = StructType | ArrayType | "[" "..." "]" ElementType |
               SliceType | MapType | TypeName [ TypeArgs ] .
LiteralValue = "{" [ ElementList [ "," ] ] "}" .
ElementList  = KeyedElement { "," KeyedElement } .
KeyedElement = [ Key ":" ] Element .
Key          = FieldName | Expression | LiteralValue .
FieldName    = identifier .
Element      = Expression | LiteralValue .

```

 Unless the LiteralType is a type parameter, its underlying type must be a struct, array, slice, or map type (the syntax enforces this constraint except when the type is given as a TypeName). If the LiteralType is a type parameter, all types in its type set must have the same underlying type which must be a valid composite literal type.

 The types of the elements and keys must be assignable to the respective field, element, and key types of the LiteralType; there is no additional conversion. The key is interpreted as a field name for struct literals, an index for array and slice literals, and a key for map literals. It is an error to specify multiple elements with the same field name or constant key value. A literal may omit the element list; such a literal evaluates to the zero value for its type.

 A parsing ambiguity arises when a composite literal using the TypeName form of the LiteralType appears as an operand between the keyword and the opening brace of the block of an "if", "for", or "switch" statement, and the composite literal is not enclosed in parentheses, square brackets, or curly braces. In this rare case, the opening brace of the literal is erroneously parsed as the one introducing the block of statements. To resolve the ambiguity, the composite literal must appear within parentheses.

```go

if x == (T{a,b,c}[i]) { … }
if (x == T{a,b,c}[i]) { … }

```

#### Struct literals

 For struct literals without keys, the element list must contain an element for each struct field in the order in which the fields are declared.

 For struct literals with keys the following rules apply:

- Every element must have a key.
- Each key must be a field name declared in the struct type.
- The element list does not need to have an element for each struct field. Omitted fields get the zero value for that field.
- It is an error to specify an element for a non-exported field of a struct belonging to a different package.

 Given the declarations

```go

type Point3D struct { x, y, z float64 }
type Line struct { p, q Point3D }

```

 one may write

```go

origin := Point3D{}                            // zero value for Point3D
line := Line{origin, Point3D{y: -4, z: 12.3}}  // zero value for line.q.x

```

#### Array and slice literals

 For array and slice literals the following rules apply:

- Each element has an associated integer index marking its position in the array.
- An element with a key uses the key as its index. The key must be a non-negative constant representable by a value of type `int`; and if it is typed it must be of integer type.
- An element without a key uses the previous element's index plus one. If the first element has no key, its index is zero.

 Taking the address of a composite literal generates a pointer to a unique variable initialized with the literal's value.

```go

var pointer *Point3D = &Point3D{y: 1000}

```

 Note that the zero value for a slice or map type is not the same as an initialized but empty value of the same type. Consequently, taking the address of an empty slice or map composite literal does not have the same effect as allocating a new slice or map value with new.

```go

p1 := &[]int{}    // p1 points to an initialized, empty slice with value []int{} and length 0
p2 := new([]int)  // p2 points to an uninitialized slice with value nil and length 0

```

 The length of an array literal is the length specified in the literal type. If fewer elements than the length are provided in the literal, the missing elements are set to the zero value for the array element type. It is an error to provide elements with index values outside the index range of the array. The notation `...` specifies an array length equal to the maximum element index plus one.

```go

buffer := [10]string{}             // len(buffer) == 10
intSet := [6]int{1, 2, 3, 5}       // len(intSet) == 6
days := [...]string{"Sat", "Sun"}  // len(days) == 2

```

 A slice literal describes the entire underlying array literal. Thus the length and capacity of a slice literal are the maximum element index plus one. A slice literal has the form

```go

[]T{x1, x2, … xn}

```

 and is shorthand for a slice operation applied to an array:

```go

tmp := [n]T{x1, x2, … xn}
tmp[0 : n]

```

#### Map literals

 For map literals, each element must have a key. For non-constant map keys, see the section on evaluation order.

#### Elision of element types

 Within a composite literal of array, slice, or map type `T`, elements or map keys that are themselves composite literals may elide the respective literal type if it is identical to the element or key type of `T`. Similarly, elements or keys that are addresses of composite literals may elide the `&T` when the element or key type is `*T`.

```go

[...]Point{{1.5, -3.5}, {0, 0}}     // same as [...]Point{Point{1.5, -3.5}, Point{0, 0}}
[][]int{{1, 2, 3}, {4, 5}}          // same as [][]int{[]int{1, 2, 3}, []int{4, 5}}
[][]Point{{{0, 1}, {1, 2}}}         // same as [][]Point{[]Point{Point{0, 1}, Point{1, 2}}}
map[string]Point{"orig": {0, 0}}    // same as map[string]Point{"orig": Point{0, 0}}
map[Point]string{{0, 0}: "orig"}    // same as map[Point]string{Point{0, 0}: "orig"}

type PPoint *Point
[2]*Point{{1.5, -3.5}, {}}          // same as [2]*Point{&Point{1.5, -3.5}, &Point{}}
[2]PPoint{{1.5, -3.5}, {}}          // same as [2]PPoint{PPoint(&Point{1.5, -3.5}), PPoint(&Point{})}

```

 Examples of valid array, slice, and map literals:

```go

// list of prime numbers
primes := []int{2, 3, 5, 7, 9, 2147483647}

// vowels[ch] is true if ch is a vowel
vowels := [128]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'y': true}

// the array [10]float32{-1, 0, 0, 0, -0.1, -0.1, 0, 0, 0, -1}
filter := [10]float32{-1, 4: -0.1, -0.1, 9: -1}

// frequencies in Hz for equal-tempered scale (A4 = 440Hz)
noteFrequency := map[string]float32{
	"C0": 16.35, "D0": 18.35, "E0": 20.60, "F0": 21.83,
	"G0": 24.50, "A0": 27.50, "B0": 30.87,
}

```
