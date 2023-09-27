package main

import (
	"encoding/binary"
	"encoding/hex"
	"fmt"
)

const big_endian = true

func main() {
	b := parse("c3beade6")
	// c is rbx
	c := parse("8620aef1")
	// d is r12
	d := parse("e9b8d16b")

	result := (b & c) | ((^b) & d)

	fmt.Printf("%x\n", result)
}

func parse(s string) uint32 {
	ary, _ := hex.DecodeString(s)
	return binary.BigEndian.Uint32(ary)
}
