package main

import "testing"

func TestCalc(t *testing.T) {
	tests := [][]int{
		{12, 2},
		{14, 2},
		{1969, 654},
		{100756, 33583},
	}

	for _, test := range tests {
		input := test[0]
		expected := test[1]
		result := calc(input)

		if result != expected {
			t.Errorf("expected %d, received %d", expected, result)
		}
	}
}
