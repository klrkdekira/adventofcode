package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func calc(mass int) int {
	return mass/3 - 2
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

	var sum int

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		mass, err := strconv.Atoi(scanner.Text())
		if err != nil {
			panic(err)
		}

		sum += calc(mass)
	}

	fmt.Println(sum)
}
