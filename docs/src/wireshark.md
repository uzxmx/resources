# Wireshark

## Logical operators

Filters can be combined by such logical operators:

```
or (||)
and (&&)
```

## Filters

Filter by IP address:

```
# Filter by source or destination IP address
ip.addr == xxx.0.0.0/8
ip.addr == xxx.xxx.xxx.xxx
ip.src == xxx.xxx.xxx.xxx or ip.dst == xxx.xxx.xxx.xxx

# Filter by destination IP address
ip.dst == xxx.xxx.xxx.0/24
ip.dst == xxx.xxx.xxx.xxx
```

Filter by protocol:

```
icmp
tcp
udp
tls
dns
udp or tls
```

Filter by TCP attributes:

```
# Filter all sync packets
tcp.flags.syn == 1 and tcp.flags.ack == 0
```
