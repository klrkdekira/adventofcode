package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func Abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

type Point [2]int

func (p Point) X() int {
	return p[0]
}

func (p Point) Y() int {
	return p[1]
}

func (p Point) Move(x, y int) Point {
	return Point{p.X() + x, p.Y() + y}
}

func (p Point) Distance() int {
	return Abs(p.X()) + Abs(p.Y())
}

type Direction string

const (
	Right Direction = "R"
	Left  Direction = "L"
	Up    Direction = "U"
	Down  Direction = "D"
)

type DirectionStep [2]int

func (d Direction) Steps() DirectionStep {
	switch d {
	case Right:
		return DirectionStep{1, 0}
	case Left:
		return DirectionStep{-1, 0}
	case Up:
		return DirectionStep{0, 1}
	case Down:
		return DirectionStep{0, -1}
	default:
		panic("Oh noes")
	}
}

type Command struct {
	Direction DirectionStep
	Steps     int
}

func ParseCommand(c string) (*Command, error) {
	direction := c[0]
	rawSteps := strings.TrimPrefix(c, string(direction))

	steps, err := strconv.Atoi(rawSteps)
	if err != nil {
		return nil, err
	}

	return &Command{
		Direction: Direction(direction).Steps(),
		Steps:     steps,
	}, nil
}

func Calc(input string) (int, int) {
	rows := strings.Split(input, "\n")
	if len(rows) < 2 {
		return 0, 0
	}

	paths := make([]Point, 0)
	{
		point := Point{0, 0}
		commands := strings.Split(rows[0], ",")
		for _, code := range commands {
			cmd, err := ParseCommand(code)
			if err != nil {
				return 0, 0
			}

			for i := 0; i < cmd.Steps; i++ {
				p := point.Move(cmd.Direction[0], cmd.Direction[1])
				paths = append(paths, p)
				point = p
			}
		}
	}

	var distance, steps, traversed int

	point := Point{0, 0}

	commands := strings.Split(rows[1], ",")
	for _, code := range commands {
		cmd, err := ParseCommand(code)
		if err != nil {
			return 0, 0
		}

		for i := 0; i < cmd.Steps; i++ {
			p := point.Move(cmd.Direction[0], cmd.Direction[1])
			traversed++

			for j, q := range paths {
				if q == p {
					d := p.Distance()
					if distance == 0 || distance > d {
						distance = d
					}

					s := traversed + (j + 1)
					if steps == 0 || steps > s {
						steps = s
					}
				}
			}

			point = p
		}
	}

	return distance, steps
}

func main() {
	stat, err := os.Stdin.Stat()
	if err != nil {
		panic(err)
	}

	if (stat.Mode() & os.ModeCharDevice) != 0 {
		fmt.Println("unable to read from pipe")
		os.Exit(1)
	}

	b, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		panic(err)
	}

	fmt.Println(Calc(string(b)))
}
