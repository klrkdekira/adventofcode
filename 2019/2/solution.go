package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func compute(input []int) []int {
	i := 0
	for i < len(input) {
		code := input[i]

		switch code {
		case 1:
			p := input[i+1]
			q := input[i+2]
			r := input[i+3]

			if r > len(input) {
				break
			}

			fmt.Println(r, len(input))

			input[r] = input[p] + input[q]
		case 2:
			p := input[i+1]
			q := input[i+2]
			r := input[i+3]

			if r > len(input) {
				break
			}

			input[r] = input[p] * input[q]
		case 99:
			break
		default:
			break
		}

		i += 4
	}

	return input
}

func preprocess(input []int, noun, verb int) []int {
	input[1] = noun
	input[2] = verb

	return input
}

func part2(input []int) int {
	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb++ {
			if preprocess(compute(input), noun, verb)[0] == 19690720 {
				return 100*noun + verb
			}
		}
	}

	return 0
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

	// Cheat
	var builder strings.Builder
	builder.WriteString("[")
	builder.WriteString(string(b))
	builder.WriteString("]")

	var program []int
	err = json.Unmarshal([]byte(builder.String()), &program)
	if err != nil {
		panic(err)
	}

	fmt.Println(compute(preprocess(program, 1, 12))[0])
	fmt.Println(part2(program))
}
