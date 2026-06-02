---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/sort"
source_path: "sources/raw/external/pkg-go-dev-sort-b0cd968d4c.html"
license_ref: ""
---

```go
Output:
Organs by weight:
prostate (62g)
pancreas (131g)
spleen   (162g)
heart    (290g)
brain    (1340g)
liver    (1494g)
Organs by name:
brain    (1340g)
heart    (290g)
liver    (1494g)
pancreas (131g)
prostate (62g)
spleen   (162g)

```

Share Format Run

-  func Find(n int, cmp func(int) int) (i int, found bool)
-  func Float64s(x []float64)
-  func Float64sAreSorted(x []float64) bool
-  func Ints(x []int)
-  func IntsAreSorted(x []int) bool
-  func IsSorted(data Interface) bool
-  func Search(n int, f func(int) bool) int
-  func SearchFloat64s(a []float64, x float64) int
-  func SearchInts(a []int, x int) int
-  func SearchStrings(a []string, x string) int
-  func Slice(x any, less func(i, j int) bool)
-  func SliceIsSorted(x any, less func(i, j int) bool) bool
-  func SliceStable(x any, less func(i, j int) bool)
-  func Sort(data Interface)
-  func Stable(data Interface)
-  func Strings(x []string)
-  func StringsAreSorted(x []string) bool
-  type Float64Slice
-
-  func (x Float64Slice) Len() int
-  func (x Float64Slice) Less(i, j int) bool
-  func (p Float64Slice) Search(x float64) int
-  func (x Float64Slice) Sort()
-  func (x Float64Slice) Swap(i, j int)

-  type IntSlice
-
-  func (x IntSlice) Len() int
-  func (x IntSlice) Less(i, j int) bool
-  func (p IntSlice) Search(x int) int
-  func (x IntSlice) Sort()
-  func (x IntSlice) Swap(i, j int)

-  type Interface
-
-  func Reverse(data Interface) Interface

-  type StringSlice
-
-  func (x StringSlice) Len() int
-  func (x StringSlice) Less(i, j int) bool
-  func (p StringSlice) Search(x string) int
-  func (x StringSlice) Sort()
-  func (x StringSlice) Swap(i, j int)

- Package
- Package (SortKeys)
- Package (SortMultiKeys)
- Package (SortWrapper)
- Find
- Float64s
- Float64sAreSorted
- Ints
- IntsAreSorted
- Reverse
- Search
- Search (DescendingOrder)
- SearchFloat64s
- SearchInts
- SearchStrings
- Slice
- SliceIsSorted
- SliceStable
- Strings

This section is empty.

This section is empty.

```go
func Find(n int, cmp func(int) int) (i int, found bool)
```

Find uses binary search to find and return the smallest index i in [0, n) at which cmp(i) <= 0. If there is no such index i, Find returns i = n. The found result is true if i < n and cmp(i) == 0. Find calls cmp(i) only for i in the range [0, n).

To permit binary search, Find requires that cmp(i) > 0 for a leading prefix of the range, cmp(i) == 0 in the middle, and cmp(i) < 0 for the final suffix of the range. (Each subrange could be empty.) The usual way to establish this condition is to interpret cmp(i) as a comparison of a desired target value t against entry i in an underlying indexed data structure x, returning <0, 0, and >0 when t < x[i], t == x[i], and t > x[i], respectively.

For example, to look for a particular string in a sorted, random-access list of strings:

```go
i, found := sort.Find(x.Len(), func(i int) int {
    return strings.Compare(target, x.At(i))
})
if found {
    fmt.Printf("found %s at entry %d\n", target, i)
} else {
    fmt.Printf("%s not found, would insert at %d", target, i)
}

```

This example demonstrates finding a string in a list sorted in ascending order.

```go

package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	a := []string{"apple", "banana", "lemon", "mango", "pear", "strawberry"}

for _, x := range []string{"banana", "orange"} {
		i, found := sort.Find(len(a), func(i int) int {
			return strings.Compare(x, a[i])
		})
		if found {
			fmt.Printf("found %s at index %d\n", x, i)
		} else {
			fmt.Printf("%s not found, would insert at %d\n", x, i)
		}
	}

}

```

```go
Output:
found banana at index 1
orange not found, would insert at 4

```

Share Format Run

```go
func Float64s(x []float64)
```

Float64s sorts a slice of float64s in increasing order. Not-a-number (NaN) values are ordered before other values.

Note: as of Go 1.22, this function simply calls slices.Sort.

```go

package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	s := []float64{5.2, -1.3, 0.7, -3.8, 2.6} // unsorted
	sort.Float64s(s)
	fmt.Println(s)

s = []float64{math.Inf(1), math.NaN(), math.Inf(-1), 0.0} // unsorted
	sort.Float64s(s)
	fmt.Println(s)

}

```

```go
Output:
[-3.8 -1.3 0.7 2.6 5.2]
[NaN -Inf 0 +Inf]

```

Share Format Run

```go
func Float64sAreSorted(x []float64) bool
```

Float64sAreSorted reports whether the slice x is sorted in increasing order, with not-a-number (NaN) values before any other values.

Note: as of Go 1.22, this function simply calls slices.IsSorted.

```go

package main

import (
	"fmt"
	"sort"
)

func main() {
	s := []float64{0.7, 1.3, 2.6, 3.8, 5.2} // sorted ascending
	fmt.Println(sort.Float64sAreSorted(s))

s = []float64{5.2, 3.8, 2.6, 1.3, 0.7} // sorted descending
	fmt.Println(sort.Float64sAreSorted(s))

s = []float64{5.2, 1.3, 0.7, 3.8, 2.6} // unsorted
	fmt.Println(sort.Float64sAreSorted(s))

}

```

```go
Output:
true
false
false

```

Share Format Run

```go
func Ints(x []int)
```

Ints sorts a slice of ints in increasing order.

Note: as of Go 1.22, this function simply calls slices.Sort.

```go

package main

import (
	"fmt"
	"sort"
)

func main() {
	s := []int{5, 2, 6, 3, 1, 4} // unsorted
	sort.Ints(s)
	fmt.Println(s)
}

```

```go
Output:
[1 2 3 4 5 6]

```

Share Format Run

```go
func IntsAreSorted(x []int) bool
```

IntsAreSorted reports whether the slice x is sorted in increasing order.

Note: as of Go 1.22, this function simply calls slices.IsSorted.

```go

package main

import (
	"fmt"
	"sort"
)

func main() {
	s := []int{1, 2, 3, 4, 5, 6} // sorted ascending
	fmt.Println(sort.IntsAreSorted(s))

s = []int{6, 5, 4, 3, 2, 1} // sorted descending
	fmt.Println(sort.IntsAreSorted(s))

s = []int{3, 2, 4, 1, 5} // unsorted
	fmt.Println(sort.IntsAreSorted(s))

}

```

```go
Output:
true
false
false

```

Share Format Run

```go
func IsSorted(data Interface) bool
```

IsSorted reports whether data is sorted.

Note: in many situations, the newer slices.IsSortedFunc function is more ergonomic and runs faster.

```go
func Search(n int, f func(int) bool) int
```

Search uses binary search to find and return the smallest index i in [0, n) at which f(i) is true, assuming that on the range [0, n), f(i) == true implies f(i+1) == true. That is, Search requires that f is false for some (possibly empty) prefix of the input range [0, n) and then true for the (possibly empty) remainder; Search returns the first true index. If there is no such index, Search returns n. (Note that the "not found" return value is not -1 as in, for instance, strings.Index.) Search calls f(i) only for i in the range [0, n).

A common use of Search is to find the index i for a value x in a sorted, indexable data structure such as an array or slice. In this case, the argument f, typically a closure, captures the value to be searched for, and how the data structure is indexed and ordered.

For instance, given a slice data sorted in ascending order, the call Search(len(data), func(i int) bool { return data[i] >= 23 }) returns the smallest index i such that data[i] >= 23. If the caller wants to find whether 23 is in the slice, it must test data[i] == 23 separately.

Searching data sorted in descending order would use the <= operator instead of the >= operator.

To complete the example above, the following code tries to find the value x in an integer slice data sorted in ascending order:

```go
x := 23
i := sort.Search(len(data), func(i int) bool { return data[i] >= x })
if i < len(data) && data[i] == x {
	// x is present at data[i]
} else {
	// x is not present in data,
	// but i is the index where it would be inserted.
}

```

As a more whimsical example, this program guesses your number:

```go
func GuessingGame() {
	var s string
	fmt.Printf("Pick an integer from 0 to 100.\n")
	answer := sort.Search(100, func(i int) bool {
		fmt.Printf("Is your number <= %d? ", i)
		fmt.Scanf("%s", &s)
		return s != "" && s[0] == 'y'
	})
	fmt.Printf("Your number is %d.\n", answer)
}

```

```go
func SearchFloat64s(a []float64, x float64) int
```

SearchFloat64s searches for x in a sorted slice of float64s and returns the index as specified by Search. The return value is the index to insert x if x is not present (it could be len(a)). The slice must be sorted in ascending order.

```go
func SearchInts(a []int, x int) int
```

SearchInts searches for x in a sorted slice of ints and returns the index as specified by Search. The return value is the index to insert x if x is not present (it could be len(a)). The slice must be sorted in ascending order.

```go
func SearchStrings(a []string, x string) int
```

SearchStrings searches for x in a sorted slice of strings and returns the index as specified by Search. The return value is the index to insert x if x is not present (it could be len(a)). The slice must be sorted in ascending order.

```go
func Slice(x any, less func(i, j int) bool)
```

Slice sorts the slice x given the provided less function. It panics if x is not a slice.

The sort is not guaranteed to be stable: equal elements may be reversed from their original order. For a stable sort, use SliceStable.

The less function must satisfy the same requirements as the Interface type's Less method.

Note: in many situations, the newer slices.SortFunc function is more ergonomic and runs faster.

```go

package main

import (
	"fmt"
	"sort"
)

func main() {
	people := []struct {
		Name string
		Age  int
	}{
		{"Gopher", 7},
		{"Alice", 55},
		{"Vera", 24},
		{"Bob", 75},
	}
	sort.Slice(people, func(i, j int) bool { return people[i].Name < people[j].Name })
	fmt.Println("By name:", people)
