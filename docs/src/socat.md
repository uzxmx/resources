# socat

`socat` is a command line based utility that establishes **two bidirectional byte streams**
and **transfers data** between them. Because the streams can be constructed from a large
set of different types of data sinks and sources (called address types), and because lots
of address options may be applied to the streams, `socat` can be used for many different
purposes.

### Examples

#### Basic use

Transfer data between STDIO (-) and a TCP4 connection to port 80 on a host named
`www.example.com`.

```
socat - TCP4:www.example.com:80
```

As an echo server.

```
socat - EXEC:cat

# Also write the transferred data to the stderr in text format.
socat -v - EXEC:cat

# Also write the transferred data to the stderr in hexadecimal format.
socat -x - EXEC:cat
```

As a shell command interpreter.

```
socat - EXEC:bash

```

Accept connections at port 5000 as a shell command interpreter. Use `nc
localhost 5000` or `socat - TCP:localhost:5000` to connect.

```
socat -v TCP-LISTEN:5000,fork,reuseaddr EXEC:bash
```

Run a command with arguments. If the argument contains a colon, you must quote
the argument, otherwise an error will happen.

```
socat - EXEC:"YOUR_COMMAND_NAME ARG1 ARG2 ..."
```

#### Use socat as a TCP port forwarder

For one-shot connection, forward the connection to 8080 on the local side to
port 80 on the remote host `www.example.com`.

```
socat TCP4-LISTEN:8080 TCP4:www.example.com:80
```

For multiple connections, forward the connections to 8080 on the local side to
port 80 on the remote host `www.example.com`.

```
socat TCP4-LISTEN:8080,fork,reuseaddr TCP4:www.example.com:80
```

Forward connections to 5000 on the local side to a Unix socket.

```
socat TCP4-LISTEN:5000,fork,reuseaddr UNIX-CONNECT:/var/run/docker.sock
```

Forward connections to a Unix socket to port 80 on the remote host
`www.example.com`.

Execute `curl --unix-socket /tmp/test.sock http://wwww.example.com/` to test if
that works.

```
socat UNIX-LISTEN:/tmp/test.sock,fork,reuseaddr,unlink-early,mode=777 TCP4:www.example.com:80
```

#### Use socat as a message collector

```
socat -u TCP4-LISTEN:5000,fork,reuseaddr OPEN:/tmp/test.log,creat,append
```

In this example, when a client connects to port 5000, a new child process is
generated. All data sent by the clients is appended to the file `/tmp/test.log`.
If the file does not exist, `socat` creates it.

#### Send data through a specific network interface

```
socat - TCP4:www.example.com:80,bind=10.0.0.1
```

In this example, it sends HTTP request through a network interface which has
address `10.0.0.1`. If that is a virtual interface, you may need to enable
kernel IP forward, and make sure there is one iptables rule exists like below:

```
iptables -t nat -I POSTROUTING -o eno2 -j MASQUERADE
```

`eno2` is a physical NIC with internet access. Change it as you need.
