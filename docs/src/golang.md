# Golang

## Golang install binary from github.com

Take `https://github.com/saferwall/pe` as an example.

When executing below command, a binary named as `cmd` will be installed in
`$GOPATH/bin`.

```
go install github.com/saferwall/pe/cmd@latest
```

If we want to use a different binary name, we can do as below shown.

```
go get github.com/saferwall/pe@v1.1.3
cd "$GOPATH/pkg/mod/github.com/saferwall/pe@v1.1.3"
go build -o "$GOPATH/bin/pedumper" ./cmd
```
