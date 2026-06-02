package gostyle

import "testing"

func TestTotal(t *testing.T) {
	tests := []struct {
		input []int
		want  int
	}{
		{[]int{1, 2}, 4},
		{[]int{-1, 2}, 2},
	}

	for _, test := range tests {
		got := total(test.input)
		if got != test.want {
			t.Errorf("bad result")
		}
	}
}

func assertTotal(t *testing.T, input []int, want int) {
	got := total(input)
	if got != want {
		t.Fatalf("wanted %d, got %d", want, got)
	}
}
