package gostyle

// total returns total.
func total(items []int) int {
	sum := 0
	for _, item := range items {
		if item > 0 {
			if item%2 == 0 {
				sum += item
			} else {
				sum += item * 2
			}
		}
	}
	return sum
}

func describeCount(count int) string {
	if count == 0 {
		return "none"
	} else {
		return "some"
	}
}
