package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

// L - 76 - 0
// . - 46 - -1
// # - 1

type Plane struct {
	base  int
	size  int
	seats []int
}

func NewPlaneFromReader(rd io.Reader) *Plane {
	var base int
	seats := make([]int, 0)

	scanner := bufio.NewScanner(rd)
	for scanner.Scan() {
		b := scanner.Bytes()
		count := len(b)

		if base == 0 {
			base = count
		}

		for i := 0; i < count; i++ {
			var n int

			if b[i] == 76 {
				n = 0
			} else if b[i] == 46 {
				n = -1
			}

			seats = append(seats, n)
		}
	}

	return NewPlane(seats, base)
}

func NewPlane(seats []int, base int) *Plane {
	return &Plane{
		seats: seats,
		base:  base,
		size:  len(seats),
	}
}

func (p *Plane) Clone() *Plane {
	newSeats := make([]int, p.size)

	for i := 0; i < p.size; i++ {
		newSeats[i] = p.seats[i]
	}

	return &Plane{
		seats: newSeats,
		base:  p.base,
		size:  p.size,
	}
}

func (p *Plane) String() string {
	var builder strings.Builder

	for i := 0; i < p.size; i++ {
		if i%p.base == 0 {
			builder.WriteByte('\n')
		}

		switch p.seats[i] {
		case -1:
			builder.WriteByte('.')
		case 0:
			builder.WriteByte('L')
		case 1:
			builder.WriteByte('#')
		}
	}

	builder.WriteByte('\n')

	return builder.String()
}

func (p *Plane) Adjacent(i int, greedy bool) []int {
	list := make([]int, 0)

	y := i / p.base
	x := i % p.base
	for dy := -1; dy < 2; dy++ {
		for dx := -1; dx < 2; dx++ {
			x := x + dx
			if x < 0 || x >= p.base {
				continue
			}

			y := y + dy
			id := x + (y * p.base)

			if id == i || id < 0 || id >= p.size {
				continue
			}

			if greedy {
				for p.seats[id] == -1 {
					x += dx
					if x < 0 || x >= p.base {
						break
					}

					y += dy
					newID := x + (y * p.base)

					if newID < 0 || newID >= p.size {
						break
					}

					id = newID
				}
			}

			list = append(list, id)
		}
	}

	return list
}

func (p *Plane) Occupied(seats []int) int {
	var count int

	for i := 0; i < len(seats); i++ {
		if p.seats[seats[i]] == 1 {
			count++
		}
	}

	return count
}

func (p *Plane) Board(maxOccupied int, greedy bool) (*Plane, bool) {
	var changed bool
	newSeats := make([]int, p.size)

	for i := 0; i < p.size; i++ {
		seat := p.seats[i]
		newSeats[i] = seat
		if seat == -1 {
			continue
		}

		adjacent := p.Adjacent(i, greedy)
		occupied := p.Occupied(adjacent)

		if seat == 0 {
			if occupied == 0 {
				newSeats[i] = 1
				changed = true
			}
		} else if seat == 1 {
			if occupied >= maxOccupied {
				newSeats[i] = 0
				changed = true
			}
		}
	}

	return NewPlane(newSeats, p.base), changed
}

func (p *Plane) TotalOccupied() int {
	var count int

	for i := 0; i < p.size; i++ {
		if p.seats[i] == 1 {
			count++
		}
	}

	return count
}

func part1(plane *Plane) int {
	changed := true
	count := 0

	for changed {
		plane, changed = plane.Board(4, false)
		count++
	}

	return plane.TotalOccupied()
}

func part2(plane *Plane) int {
	changed := true
	count := 0

	for changed {
		plane, changed = plane.Board(5, true)
		count++
	}

	return plane.TotalOccupied()
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	plane := NewPlaneFromReader(file)
	fmt.Println(part1(plane.Clone()))
	fmt.Println(part2(plane.Clone()))
}
