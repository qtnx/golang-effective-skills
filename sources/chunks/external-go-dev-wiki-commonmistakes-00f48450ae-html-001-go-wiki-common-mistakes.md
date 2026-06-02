---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CommonMistakes"
source_path: "sources/raw/external/go-dev-wiki-commonmistakes-00f48450ae.html"
license_ref: ""
---

# Go Wiki: Common Mistakes

Go Wiki: Common Mistakes - The Go Programming Language
# Go Wiki: Common Mistakes

# Table of Contents

- Introduction
- Using reference to loop iterator variable
- Using goroutines on loop iterator variables

# Introduction

When new programmers start using Go or when old Go programmers start using a new concept, there are some common mistakes that many of them make. Here is a non-exhaustive list of some frequent mistakes that show up on the mailing lists and in IRC.

# Using reference to loop iterator variable

**NOTE:** the following section applies to Go < 1.22. Go versions >= 1.22 uses variables scoped to the iteration, see Fixing For Loops in Go 1.22 <https://go.dev/blog/loopvar-preview> for details.

In Go, the loop iterator variable is a single variable that takes different values in each loop iteration. This is very efficient, but might lead to unintended behavior when used incorrectly. For example, see the following program:

```go
func main() {
    var out []*int
    for i := 0; i < 3; i++ {
        out = append(out, &i)
    }
    fmt.Println("Values:", *out[0], *out[1], *out[2])
    fmt.Println("Addresses:", out[0], out[1], out[2])
}

```

It will output unexpected results:

```go
Values: 3 3 3
Addresses: 0x40e020 0x40e020 0x40e020

```

Explanation: in each iteration we append the address of `i` to the `out` slice, but since it is the same variable, we append the same address which eventually contains the last value that was assigned to `i`. One of the solutions is to copy the loop variable into a new variable:

```go
 for i := 0; i < 3; i++ {
+   i := i // Copy i into a new variable.
    out = append(out, &i)
 }

```

The new output of the program is what was expected:

```go
Values: 0 1 2
Addresses: 0x40e024 0x40e028 0x40e032

```

Explanation: the line `i := i` copies the loop variable `i` into a new variable scoped to the for loop body block, also called `i`. The address of the new variable is the one that is appended to the array, which makes it outlive the for loop body block. In each loop iteration a new variable is created.

While this example might look a bit obvious, the same unexpected behavior could be more hidden in some other cases. For example, the loop variable can be an array and the reference can be a slice:

```go
func main() {
    var out [][]int
    for _, i := range [][1]int{{1}, {2}, {3}} {
        out = append(out, i[:])
    }
    fmt.Println("Values:", out)
}

```

Output:

```go
Values: [[3] [3] [3]]

```

The same issue can be demonstrated also when the loop variable is being used in a Goroutine (see the following section).
