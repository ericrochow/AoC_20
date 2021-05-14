// Solution to day 1 written in Go
package main

import (
  "fmt"
  "strconv"
  "strings"
  utils "AoC_20/utils"
)

func part_one(vals []string) int {
  for _, x := range vals {
    for _, y := range vals {
      x, _ := strconv.Atoi(x)
      y, _ := strconv.Atoi(y)
      if x + y == 2020 {
        return x * y
      }
    }
  }
  return 0
}

func part_two(vals []string) int {
  for _, x := range vals {
    for _, y := range vals {
      for _, z := range vals {
        x, _ := strconv.Atoi(x)
        y, _ := strconv.Atoi(y)
        z, _ := strconv.Atoi(z)
        if x + y + z == 2020 {
          return x * y * z
        }
      }
    }
  }
  return 0
}

func main() {
  input := utils.ReadInput(1)
  parsed_input := strings.Split(input, "\n")
  fmt.Println(part_one(parsed_input))
  fmt.Println(part_two(parsed_input))
}
