package main

import (
	"os"
	"testing"
)

func BenchmarkPart1(b *testing.B) {
	file, err := os.Open("input")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	plane := NewPlaneFromReader(file)
	for i := 0; i < b.N; i++ {
		part1(plane)
	}
}

func BenchmarkPart2(b *testing.B) {
	file, err := os.Open("input")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	plane := NewPlaneFromReader(file)
	for i := 0; i < b.N; i++ {
		part2(plane)
	}
}
