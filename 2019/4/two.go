package main

import (
	"fmt"
	"sync"
)

func Qualify(wg *sync.WaitGroup, input int, output chan<- bool) {
	defer wg.Done()

	b := []byte(fmt.Sprint(input))

	var (
		qualify bool
		c       byte
		repeat  int
	)

	for i := 1; i < len(b); i++ {
		if b[i] < b[i-1] {
			return
		}

		if b[i] == b[i-1] {
			if c == b[i] {
				repeat++
			} else {
				if c != 0 && repeat == 1 {
					qualify = true
				}

				c = b[i]
				repeat = 1
			}
		}
	}

	if qualify || repeat == 1 {
		output <- true
	}
}

func Total(c <-chan bool) <-chan int {
	out := make(chan int)

	go func() {
		total := 0
		for range c {
			total++
		}
		out <- total
		close(out)
	}()

	return out
}

func main() {
	p := 128392
	q := 643281

	var wg sync.WaitGroup
	wg.Add(q - p)

	c := make(chan bool)
	total := Total(c)

	for i := p; i < q; i++ {
		go Qualify(&wg, i, c)
	}

	wg.Wait()
	close(c)

	fmt.Println(<-total)
}
