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

			input[r] = input[p] + input[q]
		case 2:
			p := input[i+1]
			q := input[i+2]
			r := input[i+3]

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

func preprocess(input []int) []int {
	input[1] = 12
	input[2] = 2

	return input
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

	fmt.Println(compute(preprocess(program))[0])
}
