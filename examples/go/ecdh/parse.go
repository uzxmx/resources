package main

import (
	"encoding/hex"

	"crypto/x509"
	"log"
	// "math/big"
	"crypto/elliptic"
	"io/ioutil"
)

// 0x1069044c0: c2 30 3f 99 9a ef 5a 62 6e eb 2f d9 9c 2b 2c f0  0?..Zbn/.+,
// 0x1069044d0: 54 e0 38 fc 49 84 9e 6e 04 ee 10 01 92 36 da cf  T8I..n....6

func main() {
	// content, err := ioutil.ReadFile("privkey.der")
	// if err != nil {
	// 	log.Fatal(err)
	// }

	content, _ := hex.DecodeString("3077020101042056553d78f9e90c73bb782452589a4fbe32af9b13bad2e08240ccfdf69b357242a00a06082a8648ce3d030107a14403420004024c23e31462996eac53bdb770728b11bf1f54eb4f81b23324418b40212860f014c116dc2763a51c40210fb4d7fe7a5ad5be4c7a8040538a7a1ad3c2669e159e")

	privkey, err := x509.ParseECPrivateKey(content)
	if err != nil {
		log.Fatal(err)
	}

	p224 := elliptic.P224()

	log.Println(params.BitSize)
	log.Println(p224.Params().BitSize)

	point, err := ioutil.ReadFile("point.der")
	if err != nil {
		log.Fatal(err)
	}
	x, y := elliptic.Unmarshal(privkey, point)

	log.Println(x)
	log.Println(y)

	log.Println(privkey.IsOnCurve(x, y))

	str := "\004Vv\242\323s[\000B\t\226\220\274\225\200#\037\276\375\334\3511?o\302\320\016\013\221\374w\356\271L0&\306\316\304V3]\000}\021\265l\315@\204\031\364\016ej\322\377"
	// ary := make([]byte, 65)
	// copy(ary, []byte(str))
	// log.Println(hex.EncodeToString(ary))

	// x, y = elliptic.Unmarshal(p224, ary)
	x, y = elliptic.Unmarshal(p224, []byte(str))
	log.Println(x)
	log.Println(y)
	log.Println(p224.IsOnCurve(x, y))
}
