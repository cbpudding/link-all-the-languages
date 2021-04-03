package main

import "fmt"
import "C"

//export hello_go
func hello_go() {
	fmt.Println("Hello from Go!")
}

func main(){}
