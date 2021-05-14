package ReadInput

import (
  "fmt"
  "io/ioutil"
  "log"
  // "strings"
)


func ReadInput(day int) string {
  input_file := fmt.Sprintf("../inputs/day%d.txt", day)
  data, err := ioutil.ReadFile(input_file)
  if err != nil {
    log.Fatal(err)
  }
  return string(data)
}
