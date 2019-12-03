package main

import (
	"reflect"
	"testing"
)

func TestCompute(t *testing.T) {
	tests := [][2][]int{
		{
			{1, 0, 0, 0, 99},
			{2, 0, 0, 0, 99},
		},
		{
			{2, 3, 0, 3, 99},
			{2, 3, 0, 6, 99},
		},
		{
			{2, 4, 4, 5, 99, 0},
			{2, 4, 4, 5, 99, 9801},
		},
		{
			{1, 1, 1, 4, 99, 5, 6, 0, 99},
			{30, 1, 1, 4, 2, 5, 6, 0, 99},
		},
	}

	for _, test := range tests {
		input := test[0]
		expected := test[1]
		result := compute(input)

		if !reflect.DeepEqual(result, expected) {
			t.Errorf("expected %v, got %v", expected, result)
		}
	}
}
