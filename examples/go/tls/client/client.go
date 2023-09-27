package main

import (
	"crypto/tls"
	"fmt"
	"log"
)

func main() {
	config := &tls.Config{
		InsecureSkipVerify: true,
	}

	conn, err := tls.Dial("tcp", "127.0.0.1:8443", config)
	if err != nil {
		log.Println(err)
		return
	}
	defer conn.Close()

	n, err := conn.Write([]byte("Hello, world\n"))
	if err != nil {
		log.Fatal(err)
	}

	buf := make([]byte, 100)
	n, err = conn.Read(buf)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Print(string(buf[:n]))
}
