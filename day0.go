package main

import (
	"fmt"
	"log"
	"math"
)

// main
func main() {
	input_data, err = open("day3.in", "r").read().strip().split("\n")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(math.Abs(-5))
}
