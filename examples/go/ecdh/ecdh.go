package main

import (
	"bytes"
	"math/big"

	"crypto/rand"
	"fmt"

	"crypto/elliptic"
	"crypto/x509"
	"github.com/aead/ecdh"
	"io/ioutil"
	"log"
	// "math/big"
)

// 0x1069044c0: c2 30 3f 99 9a ef 5a 62 6e eb 2f d9 9c 2b 2c f0  0?..Zbn/.+,
// 0x1069044d0: 54 e0 38 fc 49 84 9e 6e 04 ee 10 01 92 36 da cf  T8I..n....6

func bar() {
	// foo()

	content, err := ioutil.ReadFile("privkey.der")
	if err != nil {
		log.Fatal(err)
	}

	privkey, err := x509.ParseECPrivateKey(content)
	if err != nil {
		log.Fatal(err)
	}

	// x := big.NewInt(1)
	// y := big.NewInt(2)

	point, err := ioutil.ReadFile("point.der")
	if err != nil {
		log.Fatal(err)
	}

	log.Println(len(point))
	x, y := elliptic.Unmarshal(privkey, point)

	log.Println(x)
	log.Println(y)

	log.Println(privkey.IsOnCurve(x, y))
	log.Println(privkey.IsOnCurve(x, big.NewInt(1)))

	// key, ok := checkPrivateKey(privkey)
	// if !ok {
	// 	log.Fatal("Failed to convert private key")
	// }

	secret, _ := privkey.Curve.ScalarMult(x, y, privkey.D.Bytes())

	// 这儿只计算出了第一次的secret，还需要derive一个

	log.Println(secret.Bytes())
	log.Println(len(secret.Bytes()))

	// ary := elliptic.Marshal(privkey, x, y)
	// log.Println(len(ary))

	// privkey.ScalarBaseMult(privkey.Public())

	// log.Println(privkey.Public())

	// curve := elliptic.P256()
	// curve.ScalarBaseMult()
	// curve.ScalarMult()
}

func checkPrivateKey(typeToCheck interface{}) (key []byte, ok bool) {
	switch t := typeToCheck.(type) {
	case []byte:
		key = t
		ok = true
	case *[]byte:
		key = *t
		ok = true
	}
	return
}

func main() {
	foo()
}

func foo() {
	p256 := ecdh.Generic(elliptic.P256())

	privateAlice, publicAlice, err := p256.GenerateKey(rand.Reader)
	if err != nil {
		fmt.Printf("Failed to generate Alice's private/public key pair: %s\n", err)
	}
	privateBob, publicBob, err := p256.GenerateKey(rand.Reader)
	if err != nil {
		fmt.Printf("Failed to generate Bob's private/public key pair: %s\n", err)
	}

	if err := p256.Check(publicBob); err != nil {
		fmt.Printf("Bob's public key is not on the curve: %s\n", err)
	}
	secretAlice := p256.ComputeSecret(privateAlice, publicBob)

	if err := p256.Check(publicAlice); err != nil {
		fmt.Printf("Alice's public key is not on the curve: %s\n", err)
	}
	secretBob := p256.ComputeSecret(privateBob, publicAlice)

	if !bytes.Equal(secretAlice, secretBob) {
		fmt.Printf("key exchange failed - secret X coordinates not equal\n")
	}
	fmt.Println(privateAlice)
	fmt.Println(secretBob)
}
