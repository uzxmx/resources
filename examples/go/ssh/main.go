package main

import (
	"io/ioutil"
	"log"
	"net"

	gossh "golang.org/x/crypto/ssh"

	goflag "github.com/jessevdk/go-flags"
	"strings"
)

func main() {
	var opts struct {
		// Slice of bool will append 'true' each time the option
		// is encountered (can be set multiple times, like -vvv)
		Verbose []bool `short:"v" description:"Show verbose debug information"`

		Version bool `short:"V" description:"Display the version number and exit"`

		IdentityFile string `short:"i" description:"Identity file" value-name:"FILE"`

		LocalBinds []string `short:"L" description:"A slice of strings"`

		Port string `short:"p" description:"Port"`
	}

	args, err := goflag.Parse(&opts)
	if err != nil {
		log.Fatal(err)
	}

	config := gossh.ClientConfig{
		HostKeyCallback: gossh.InsecureIgnoreHostKey(),
	}

	if len(opts.IdentityFile) > 0 {
		data, err := ioutil.ReadFile(opts.IdentityFile)
		if err != nil {
			log.Fatal(err)
		}

		key, err := gossh.ParsePrivateKey(data)
		if err != nil {
			log.Fatal(err)
		}

		config.Auth = []gossh.AuthMethod{
			gossh.PublicKeys(key),
		}
	}

	if len(args) == 0 {
		log.Fatal("A host is required.")
	}

	var host string
	ary := strings.SplitN(args[0], "@", 2)
	if len(ary) == 1 {
		host = ary[0]
	} else {
		config.User = ary[0]
		host = ary[1]
	}

	conn, err := gossh.Dial("tcp", host, &config)
	if err != nil {
		log.Fatal(err)
	}

	conn.Close()
}
