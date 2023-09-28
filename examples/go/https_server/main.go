package main

import "fmt"
import "net/http"

func main() {
	port := 8090
	addr := fmt.Sprintf("%s:%d", "localhost", port)
	fmt.Printf("Running server at %s\n", addr)
	if err := http.ListenAndServeTLS(addr, "cert/cert.pem", "cert/key.pem", http.FileServer(http.Dir("."))); err != nil {
		panic(err)
	}
}
