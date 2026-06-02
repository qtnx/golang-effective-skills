---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/sort"
source_path: "sources/raw/external/pkg-go-dev-sort-b0cd968d4c.html"
license_ref: ""
---

sort package - sort - Go Packages
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

##   Documentation ¶

Package sort provides primitives for sorting slices and user-defined collections.

```go

package main

import (
	"fmt"
	"sort"
)

type Person struct {
	Name string
	Age  int
}

func (p Person) String() string {
	return fmt.Sprintf("%s: %d", p.Name, p.Age)
}

// ByAge implements sort.Interface for []Person based on
// the Age field.
type ByAge []Person

func (a ByAge) Len() int           { return len(a) }
func (a ByAge) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByAge) Less(i, j int) bool { return a[i].Age < a[j].Age }

func main() {
	people := []Person{
		{"Bob", 31},
		{"John", 42},
		{"Michael", 17},
		{"Jenny", 26},
	}

fmt.Println(people)
	// There are two ways to sort a slice. First, one can define
	// a set of methods for the slice type, as with ByAge, and
	// call sort.Sort. In this first example we use that technique.
	sort.Sort(ByAge(people))
	fmt.Println(people)

// The other way is to use sort.Slice with a custom Less
	// function, which can be provided as a closure. In this
	// case no methods are needed. (And if they exist, they
	// are ignored.) Here we re-sort in reverse order: compare
	// the closure with ByAge.Less.
	sort.Slice(people, func(i, j int) bool {
		return people[i].Age > people[j].Age
	})
	fmt.Println(people)

}

```

```go
Output:
[Bob: 31 John: 42 Michael: 17 Jenny: 26]
[Michael: 17 Jenny: 26 Bob: 31 John: 42]
[John: 42 Bob: 31 Jenny: 26 Michael: 17]

```

Share Format Run

Example_sortKeys demonstrates a technique for sorting a struct type using programmable sort criteria.

```go

package main

import (
	"fmt"
	"sort"
)

// A couple of type definitions to make the units clear.
type earthMass float64
type au float64

// A Planet defines the properties of a solar system object.
type Planet struct {
	name     string
	mass     earthMass
	distance au
}

// By is the type of a "less" function that defines the ordering of its Planet arguments.
type By func(p1, p2 *Planet) bool

// Sort is a method on the function type, By, that sorts the argument slice according to the function.
func (by By) Sort(planets []Planet) {
	ps := &planetSorter{
		planets: planets,
		by:      by, // The Sort method's receiver is the function (closure) that defines the sort order.
	}
	sort.Sort(ps)
}

// planetSorter joins a By function and a slice of Planets to be sorted.
type planetSorter struct {
	planets []Planet
	by      func(p1, p2 *Planet) bool // Closure used in the Less method.
}

// Len is part of sort.Interface.
func (s *planetSorter) Len() int {
	return len(s.planets)
}

// Swap is part of sort.Interface.
func (s *planetSorter) Swap(i, j int) {
	s.planets[i], s.planets[j] = s.planets[j], s.planets[i]
}

// Less is part of sort.Interface. It is implemented by calling the "by" closure in the sorter.
func (s *planetSorter) Less(i, j int) bool {
	return s.by(&s.planets[i], &s.planets[j])
}

var planets = []Planet{
	{"Mercury", 0.055, 0.4},
	{"Venus", 0.815, 0.7},
	{"Earth", 1.0, 1.0},
	{"Mars", 0.107, 1.5},
}

// Example_sortKeys demonstrates a technique for sorting a struct type using programmable sort criteria.
func main() {
	// Closures that order the Planet structure.
	name := func(p1, p2 *Planet) bool {
		return p1.name < p2.name
	}
	mass := func(p1, p2 *Planet) bool {
		return p1.mass < p2.mass
	}
	distance := func(p1, p2 *Planet) bool {
		return p1.distance < p2.distance
	}
	decreasingDistance := func(p1, p2 *Planet) bool {
		return distance(p2, p1)
	}

// Sort the planets by the various criteria.
	By(name).Sort(planets)
	fmt.Println("By name:", planets)

By(mass).Sort(planets)
	fmt.Println("By mass:", planets)

By(distance).Sort(planets)
	fmt.Println("By distance:", planets)

By(decreasingDistance).Sort(planets)
	fmt.Println("By decreasing distance:", planets)

}

```

```go
Output:
By name: [{Earth 1 1} {Mars 0.107 1.5} {Mercury 0.055 0.4} {Venus 0.815 0.7}]
By mass: [{Mercury 0.055 0.4} {Mars 0.107 1.5} {Venus 0.815 0.7} {Earth 1 1}]
By distance: [{Mercury 0.055 0.4} {Venus 0.815 0.7} {Earth 1 1} {Mars 0.107 1.5}]
By decreasing distance: [{Mars 0.107 1.5} {Earth 1 1} {Venus 0.815 0.7} {Mercury 0.055 0.4}]

```

Share Format Run

Example_sortMultiKeys demonstrates a technique for sorting a struct type using different sets of multiple fields in the comparison. We chain together "Less" functions, each of which compares a single field.

```go

package main

import (
	"fmt"
	"sort"
)

// A Change is a record of source code changes, recording user, language, and delta size.
type Change struct {
	user     string
	language string
	lines    int
}

type lessFunc func(p1, p2 *Change) bool

// multiSorter implements the Sort interface, sorting the changes within.
type multiSorter struct {
	changes []Change
	less    []lessFunc
}

// Sort sorts the argument slice according to the less functions passed to OrderedBy.
func (ms *multiSorter) Sort(changes []Change) {
	ms.changes = changes
	sort.Sort(ms)
}

// OrderedBy returns a Sorter that sorts using the less functions, in order.
// Call its Sort method to sort the data.
func OrderedBy(less ...lessFunc) *multiSorter {
	return &multiSorter{
		less: less,
	}
}

// Len is part of sort.Interface.
func (ms *multiSorter) Len() int {
	return len(ms.changes)
}

// Swap is part of sort.Interface.
func (ms *multiSorter) Swap(i, j int) {
	ms.changes[i], ms.changes[j] = ms.changes[j], ms.changes[i]
}

// Less is part of sort.Interface. It is implemented by looping along the
// less functions until it finds a comparison that discriminates between
// the two items (one is less than the other). Note that it can call the
// less functions twice per call. We could change the functions to return
// -1, 0, 1 and reduce the number of calls for greater efficiency: an
// exercise for the reader.
func (ms *multiSorter) Less(i, j int) bool {
	p, q := &ms.changes[i], &ms.changes[j]
	// Try all but the last comparison.
	var k int
	for k = 0; k < len(ms.less)-1; k++ {
		less := ms.less[k]
		switch {
		case less(p, q):
			// p < q, so we have a decision.
			return true
		case less(q, p):
			// p > q, so we have a decision.
			return false
		}
		// p == q; try the next comparison.
	}
	// All comparisons to here said "equal", so just return whatever
	// the final comparison reports.
	return ms.less[k](p, q)
}

var changes = []Change{
	{"gri", "Go", 100},
	{"ken", "C", 150},
	{"glenda", "Go", 200},
	{"rsc", "Go", 200},
	{"r", "Go", 100},
	{"ken", "Go", 200},
	{"dmr", "C", 100},
	{"r", "C", 150},
	{"gri", "Smalltalk", 80},
}

// Example_sortMultiKeys demonstrates a technique for sorting a struct type using different
// sets of multiple fields in the comparison. We chain together "Less" functions, each of
// which compares a single field.
func main() {
	// Closures that order the Change structure.
	user := func(c1, c2 *Change) bool {
		return c1.user < c2.user
	}
	language := func(c1, c2 *Change) bool {
		return c1.language < c2.language
	}
	increasingLines := func(c1, c2 *Change) bool {
		return c1.lines < c2.lines
	}
	decreasingLines := func(c1, c2 *Change) bool {
		return c1.lines > c2.lines // Note: > orders downwards.
	}

// Simple use: Sort by user.
	OrderedBy(user).Sort(changes)
	fmt.Println("By user:", changes)

// More examples.
	OrderedBy(user, increasingLines).Sort(changes)
	fmt.Println("By user,<lines:", changes)

OrderedBy(user, decreasingLines).Sort(changes)
	fmt.Println("By user,>lines:", changes)

OrderedBy(language, increasingLines).Sort(changes)
	fmt.Println("By language,<lines:", changes)

OrderedBy(language, increasingLines, user).Sort(changes)
	fmt.Println("By language,<lines,user:", changes)

}

```

```go
Output:
By user: [{dmr C 100} {glenda Go 200} {gri Go 100} {gri Smalltalk 80} {ken C 150} {ken Go 200} {r Go 100} {r C 150} {rsc Go 200}]
By user,<lines: [{dmr C 100} {glenda Go 200} {gri Smalltalk 80} {gri Go 100} {ken C 150} {ken Go 200} {r Go 100} {r C 150} {rsc Go 200}]
By user,>lines: [{dmr C 100} {glenda Go 200} {gri Go 100} {gri Smalltalk 80} {ken Go 200} {ken C 150} {r C 150} {r Go 100} {rsc Go 200}]
By language,<lines: [{dmr C 100} {ken C 150} {r C 150} {gri Go 100} {r Go 100} {glenda Go 200} {ken Go 200} {rsc Go 200} {gri Smalltalk 80}]
By language,<lines,user: [{dmr C 100} {ken C 150} {r C 150} {gri Go 100} {r Go 100} {glenda Go 200} {ken Go 200} {rsc Go 200} {gri Smalltalk 80}]

```

Share Format Run

```go

package main

import (
	"fmt"
	"sort"
)

type Grams int

func (g Grams) String() string { return fmt.Sprintf("%dg", int(g)) }

type Organ struct {
	Name   string
	Weight Grams
}

type Organs []*Organ

func (s Organs) Len() int      { return len(s) }
func (s Organs) Swap(i, j int) { s[i], s[j] = s[j], s[i] }

// ByName implements sort.Interface by providing Less and using the Len and
// Swap methods of the embedded Organs value.
type ByName struct{ Organs }

func (s ByName) Less(i, j int) bool { return s.Organs[i].Name < s.Organs[j].Name }

// ByWeight implements sort.Interface by providing Less and using the Len and
// Swap methods of the embedded Organs value.
type ByWeight struct{ Organs }

func (s ByWeight) Less(i, j int) bool { return s.Organs[i].Weight < s.Organs[j].Weight }

func main() {
	s := []*Organ{
		{"brain", 1340},
		{"heart", 290},
		{"liver", 1494},
		{"pancreas", 131},
		{"prostate", 62},
		{"spleen", 162},
	}

sort.Sort(ByWeight{s})
	fmt.Println("Organs by weight:")
	printOrgans(s)

sort.Sort(ByName{s})
	fmt.Println("Organs by name:")
	printOrgans(s)

}

func printOrgans(s []*Organ) {
	for _, o := range s {
		fmt.Printf("%-8s (%v)\n", o.Name, o.Weight)
	}
}

```
