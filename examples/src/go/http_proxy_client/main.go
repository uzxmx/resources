package main

import (
	"crypto/tls"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
)

func main() {
	proxyStr := "https://username:password@example.com:8443"
	proxyURL, err := url.Parse(proxyStr)
	if err != nil {
		log.Println(err)
	}

	urlStr := "https://www.google.com"
	url, err := url.Parse(urlStr)
	if err != nil {
		log.Println(err)
	}

	transport := &http.Transport{
		Proxy: http.ProxyURL(proxyURL),
	}
	transport.TLSClientConfig = &tls.Config{InsecureSkipVerify: true}

	client := &http.Client{
		Transport: transport,
	}

	request, err := http.NewRequest("GET", url.String(), nil)
	if err != nil {
		log.Println(err)
	}

	response, err := client.Do(request)
	if err != nil {
		log.Println(err)
	}

	data, err := ioutil.ReadAll(response.Body)
	if err != nil {
		log.Println(err)
	}
	log.Println(string(data))
}
