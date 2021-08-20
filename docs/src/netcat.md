# netcat

### Examples

As a chat server and client.

```
# Listen at 5000.
nc -l 5000

# Connect to the server.
nc localhost 5000
```

Check if a port is open. Note some `netcat` implementation doesn't support `-z` option.

```
# Only scan with verbose output
nc -z -v example.com 80

# Test connection with 5s timeout
nc -z -v -w 5 example.com 80

# For UDP protocol
nc -z -v -u example.com 80
```


Listen at port 5000 as a shell command interpreter. Use `nc localhost 5000` or
`socat - TCP:localhost:5000` to connect.

```
nc -l 5000 -k --exec "/bin/bash"
```
