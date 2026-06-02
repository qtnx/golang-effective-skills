# Examples

Use these as calibration snippets before writing or reviewing tests.

## Named Table Rows

```go
tests := []struct {
	input []int
	want  int
}{
	{[]int{1, 2}, 3},
}
```

```go
tests := []struct {
	name  string
	input []int
	want  int
}{
	{name: "sums positive items", input: []int{1, 2}, want: 3},
}
```

## Subtests and Useful Failures

```go
for _, tt := range tests {
	got := total(tt.input)
	if got != tt.want {
		t.Errorf("bad result")
	}
}
```

```go
for _, tt := range tests {
	t.Run(tt.name, func(t *testing.T) {
		got := total(tt.input)
		if got != tt.want {
			t.Errorf("total(%v) = %d, want %d", tt.input, got, tt.want)
		}
	})
}
```

## Helpers

```go
func assertTotal(t *testing.T, input []int, want int) {
	got := total(input)
	if got != want {
		t.Fatalf("total() = %d, want %d", got, want)
	}
}
```

```go
func assertTotal(t *testing.T, input []int, want int) {
	t.Helper()
	got := total(input)
	if got != want {
		t.Fatalf("total(%v) = %d, want %d", input, got, want)
	}
}
```
