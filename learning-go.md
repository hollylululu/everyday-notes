# Learning Go

### Install Go on Mac

* brew install go 
* go get golang.org/x/tools/cmd/godoc
* go get github.com/golang/lint/golint
* godoc builtin

### "Hello World" in Go

```go
package main
import "fmt"
func main(){
    fmt.Printf("Hello World")
}
```

Run in command line: go build hello\_world.go

This will generate an executable named hello\_world. Then do: ./hello\_world

### Data types in Go

#### Arrays

An array is defined by: `[n]<type>`

Arrays are rarely used in Go because its size is fixed at initialization time. Another data type is more commonly used: slices, because of its flexibility.

```go
var array [4]int
arr[0] = 0
```

#### Slices







