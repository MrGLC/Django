package main

import "fmt"

func Hello() string { // string used here gives this type to the result
    return "Hello, World!"
}

func main() {
    fmt.Println(Hello())
}
