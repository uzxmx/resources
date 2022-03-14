package main

import (
	"fmt"
	"time"
)

func main() {
	done := make(chan bool)
	ch := make(chan bool, 2)
	go func() {
		for {
			val := <-ch
			fmt.Printf("Got: %v\n", val)
			if !val {
				break
			} else {
				time.Sleep(5 * time.Second)
			}
		}
		done <- true
	}()
	ch <- true
	ch <- false
	fmt.Println("send false")
	<-done
}
