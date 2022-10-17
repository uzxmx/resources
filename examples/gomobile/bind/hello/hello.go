// Package hello is a trivial package for gomobile bind example.
package hello

import "fmt"

func Greetings(name string) string {
	return fmt.Sprintf("Hello, %s!", name)
}
