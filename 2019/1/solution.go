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

func calcCalc(mass int) int {
	var sum int
	for {
		fuel := calc(mass)
		if fuel < 0 {
			break
		}

		sum += fuel
		mass = fuel
	}
	return sum
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

	var (
		sum1, sum2 int
	)

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		mass, err := strconv.Atoi(scanner.Text())
		if err != nil {
			panic(err)
		}

		sum1 += calc(mass)
		sum2 += calcCalc(mass)
	}

	fmt.Println(sum1)
	fmt.Println(sum2)
}
