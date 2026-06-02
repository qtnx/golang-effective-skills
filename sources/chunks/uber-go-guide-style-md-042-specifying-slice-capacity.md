---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

#### Specifying Slice Capacity

Where possible, provide capacity hints when initializing slices with `make()`,
particularly when appending.

```go
make([]T, length, capacity)
```

Unlike maps, slice capacity is not a hint: the compiler will allocate enough
memory for the capacity of the slice as provided to `make()`, which means that
subsequent `append()` operations will incur zero allocations (until the length
of the slice matches the capacity, after which any appends will require a resize
to hold additional elements).

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
for n := 0; n < b.N; n++ {
  data := make([]int, 0)
  for k := 0; k < size; k++{
    data = append(data, k)
  }
}
```

</td><td>

```go
for n := 0; n < b.N; n++ {
  data := make([]int, 0, size)
  for k := 0; k < size; k++{
    data = append(data, k)
  }
}
```

</td></tr>
<tr><td>

```plain
BenchmarkBad-4    100000000    2.48s
```

</td><td>

```plain
BenchmarkGood-4   100000000    0.21s
```

</td></tr>
</tbody></table>
