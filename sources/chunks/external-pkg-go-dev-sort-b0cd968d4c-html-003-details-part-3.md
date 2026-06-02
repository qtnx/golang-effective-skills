---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/sort"
source_path: "sources/raw/external/pkg-go-dev-sort-b0cd968d4c.html"
license_ref: ""
---

sort.Slice(people, func(i, j int) bool { return people[i].Age < people[j].Age })
	fmt.Println("By age:", people)
}

```

```go
Output:
By name: [{Alice 55} {Bob 75} {Gopher 7} {Vera 24}]
By age: [{Gopher 7} {Vera 24} {Alice 55} {Bob 75}]

```

Share Format Run

```go
func SliceIsSorted(x any, less func(i, j int) bool) bool
```

SliceIsSorted reports whether the slice x is sorted according to the provided less function. It panics if x is not a slice.

Note: in many situations, the newer slices.IsSortedFunc function is more ergonomic and runs faster.

```go

package main

import (
	"fmt"
	"sort"
)

func main() {
	numbers := []int{1, 2, 3, 4, 5, 6}

isSortedAsc := sort.SliceIsSorted(numbers, func(i, j int) bool {
		return numbers[i] < numbers[j]
	})
	fmt.Printf("%v sorted ascending: %t\n", numbers, isSortedAsc)

numbersDesc := []int{6, 5, 4, 3, 2, 1}

isSortedDesc := sort.SliceIsSorted(numbersDesc, func(i, j int) bool {
		return numbersDesc[i] > numbersDesc[j]
	})
	fmt.Printf("%v sorted descending: %t\n", numbers, isSortedDesc)

unsortedNumbers := []int{1, 3, 2, 4, 5}

isSortedUnsorted := sort.SliceIsSorted(unsortedNumbers, func(i, j int) bool {
		return unsortedNumbers[i] < unsortedNumbers[j]
	})
	fmt.Printf("%v unsorted slice sorted: %t\n", unsortedNumbers, isSortedUnsorted)

}

```

```go
Output:
[1 2 3 4 5 6] sorted ascending: true
[1 2 3 4 5 6] sorted descending: true
[1 3 2 4 5] unsorted slice sorted: false

```

Share Format Run

```go
func SliceStable(x any, less func(i, j int) bool)
```

SliceStable sorts the slice x using the provided less function, keeping equal elements in their original order. It panics if x is not a slice.

The less function must satisfy the same requirements as the Interface type's Less method.

Note: in many situations, the newer slices.SortStableFunc function is more ergonomic and runs faster.

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
		{"Alice", 25},
		{"Elizabeth", 75},
		{"Alice", 75},
		{"Bob", 75},
		{"Alice", 75},
		{"Bob", 25},
		{"Colin", 25},
		{"Elizabeth", 25},
	}

// Sort by name, preserving original order
	sort.SliceStable(people, func(i, j int) bool { return people[i].Name < people[j].Name })
	fmt.Println("By name:", people)

// Sort by age preserving name order
	sort.SliceStable(people, func(i, j int) bool { return people[i].Age < people[j].Age })
	fmt.Println("By age,name:", people)

}

```

```go
Output:
By name: [{Alice 25} {Alice 75} {Alice 75} {Bob 75} {Bob 25} {Colin 25} {Elizabeth 75} {Elizabeth 25}]
By age,name: [{Alice 25} {Bob 25} {Colin 25} {Elizabeth 25} {Alice 75} {Alice 75} {Bob 75} {Elizabeth 75}]

```

Share Format Run

```go
func Sort(data Interface)
```

Sort sorts data in ascending order as determined by the Less method. It makes one call to data.Len to determine n and O(n*log(n)) calls to data.Less and data.Swap. The sort is not guaranteed to be stable.

Note: in many situations, the newer slices.SortFunc function is more ergonomic and runs faster.

```go
func Stable(data Interface)
```

Stable sorts data in ascending order as determined by the Less method, while keeping the original order of equal elements.

It makes one call to data.Len to determine n, O(n*log(n)) calls to data.Less and O(n*log(n)*log(n)) calls to data.Swap.

Note: in many situations, the newer slices.SortStableFunc function is more ergonomic and runs faster.

```go
func Strings(x []string)
```

Strings sorts a slice of strings in increasing order.

Note: as of Go 1.22, this function simply calls slices.Sort.

```go

package main

import (
	"fmt"
	"sort"
)

func main() {
	s := []string{"Go", "Bravo", "Gopher", "Alpha", "Grin", "Delta"}
	sort.Strings(s)
	fmt.Println(s)
}

```

```go
Output:
[Alpha Bravo Delta Go Gopher Grin]

```

Share Format Run

```go
func StringsAreSorted(x []string) bool
```

StringsAreSorted reports whether the slice x is sorted in increasing order.

Note: as of Go 1.22, this function simply calls slices.IsSorted.

```go
type Float64Slice []float64
```

Float64Slice implements Interface for a []float64, sorting in increasing order, with not-a-number (NaN) values ordered before other values.

```go
func (x Float64Slice) Len() int
```

```go
func (x Float64Slice) Less(i, j int) bool
```

Less reports whether x[i] should be ordered before x[j], as required by the sort Interface. Note that floating-point comparison by itself is not a transitive relation: it does not report a consistent ordering for not-a-number (NaN) values. This implementation of Less places NaN values before any others, by using:

```go
x[i] < x[j] || (math.IsNaN(x[i]) && !math.IsNaN(x[j]))

```

```go
func (p Float64Slice) Search(x float64) int
```

Search returns the result of applying SearchFloat64s to the receiver and x.

```go
func (x Float64Slice) Sort()
```

Sort is a convenience method: x.Sort() calls Sort(x).

```go
func (x Float64Slice) Swap(i, j int)
```

```go
type IntSlice []int
```

IntSlice attaches the methods of Interface to []int, sorting in increasing order.

```go
func (x IntSlice) Len() int
```

```go
func (x IntSlice) Less(i, j int) bool
```

```go
func (p IntSlice) Search(x int) int
```

Search returns the result of applying SearchInts to the receiver and x.

```go
func (x IntSlice) Sort()
```

Sort is a convenience method: x.Sort() calls Sort(x).

```go
func (x IntSlice) Swap(i, j int)
```

```go
type Interface interface {
	// Len is the number of elements in the collection.
	Len() int

// Less reports whether the element with index i
	// must sort before the element with index j.
	//
	// If both Less(i, j) and Less(j, i) are false,
	// then the elements at index i and j are considered equal.
	// Sort may place equal elements in any order in the final result,
	// while Stable preserves the original input order of equal elements.
	//
	// Less must describe a [Strict Weak Ordering]. For example:
	//  - if both Less(i, j) and Less(j, k) are true, then Less(i, k) must be true as well.
	//  - if both Less(i, j) and Less(j, k) are false, then Less(i, k) must be false as well.
	//
	// Note that floating-point comparison (the < operator on float32 or float64 values)
	// is not a strict weak ordering when not-a-number (NaN) values are involved.
	// See Float64Slice.Less for a correct implementation for floating-point values.
	//
	// [Strict Weak Ordering]: https://en.wikipedia.org/wiki/Weak_ordering#Strict_weak_orderings <https://en.wikipedia.org/wiki/Weak_ordering#Strict_weak_orderings>
	Less(i, j int) bool

// Swap swaps the elements with indexes i and j.
	Swap(i, j int)
}
```

An implementation of Interface can be sorted by the routines in this package. The methods refer to elements of the underlying collection by integer index.

```go
func Reverse(data Interface) Interface
```

Reverse returns the reverse order for data.

```go

package main

import (
	"fmt"
	"sort"
)

func main() {
	s := []int{5, 2, 6, 3, 1, 4} // unsorted
	sort.Sort(sort.Reverse(sort.IntSlice(s)))
	fmt.Println(s)
}

```

```go
Output:
[6 5 4 3 2 1]

```

Share Format Run

```go
type StringSlice []string
```

StringSlice attaches the methods of Interface to []string, sorting in increasing order.

```go
func (x StringSlice) Len() int
```

```go
func (x StringSlice) Less(i, j int) bool
```

```go
func (p StringSlice) Search(x string) int
```

Search returns the result of applying SearchStrings to the receiver and x.

```go
func (x StringSlice) Sort()
```

Sort is a convenience method: x.Sort() calls Sort(x).

```go
func (x StringSlice) Swap(i, j int)
```

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/sort>

- search.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sort/search.go>
- slice.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sort/slice.go>
- sort.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sort/sort.go>
- zsortfunc.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sort/zsortfunc.go>
- zsortinterface.go <https://cs.opensource.google/go/go/+/go1.26.3:src/sort/zsortinterface.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
