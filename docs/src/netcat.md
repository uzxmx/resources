# netcat

### Examples

#### Basic use

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

#### Execute command when connection is made

Listen at port 5000 as a shell command interpreter. Use `nc localhost 5000` or
`socat - TCP:localhost:5000` to connect.

```
nc -l 5000 -k --exec "/bin/bash"
```

#### Send binary or text to an existing connection interactively

Suppose a server is listening at port 5000.

```
nc -l 5000
```

Now you want to send binary or text to the server interactively from a different
terminal.

First, you should make a named pipe (FIFO).

```
mkfifo test_fifo
```

Then connect to the server.

```
nc localhost 5000 <test_fifo
```

After that, from another terminal, open the named pipe by using FD 3.

```
exec 3> test_fifo
```

Then you can send data to the server by writing to FD 3.

```
echo foo >&3

# Send "hello" in hexadecimal format.
echo -e '\x68\x65\x6c\x6c\x6f' >&3
```

Finally, close the FD 3, and the connection will be closed automatically.

```
exec 3>&-
```
