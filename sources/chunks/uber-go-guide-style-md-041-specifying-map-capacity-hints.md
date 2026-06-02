---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

#### Specifying Map Capacity Hints

Where possible, provide capacity hints when initializing
maps with `make()`.

```go
make(map[T1]T2, hint)
```

Providing a capacity hint to `make()` tries to right-size the
map at initialization time, which reduces the need for growing
the map and allocations as elements are added to the map.

Note that, unlike slices, map capacity hints do not guarantee complete,
preemptive allocation, but are used to approximate the number of hashmap buckets
required. Consequently, allocations may still occur when adding elements to the
map, even up to the specified capacity.

<table>
<thead><tr><th>Bad</th><th>Good</th></tr></thead>
<tbody>
<tr><td>

```go
files, _ := os.ReadDir("./files")

m := make(map[string]os.DirEntry)
for _, f := range files {
    m[f.Name()] = f
}
```

</td><td>

```go

files, _ := os.ReadDir("./files")

m := make(map[string]os.DirEntry, len(files))
for _, f := range files {
    m[f.Name()] = f
}
```

</td></tr>
<tr><td>

`m` is created without a size hint; the map will resize
dynamically, causing multiple allocations as it grows.

</td><td>

`m` is created with a size hint; there may be fewer
allocations at assignment time.

</td></tr>
</tbody></table>
