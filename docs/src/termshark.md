# Termshark

### Commands

```
# Print a list of the interfaces on which termshark can capture.
termshark -D

termshark -i lo0 -Y tcp.port==10800

termshark -i lo0 -Y tcp.port==10800 -w foo.pcap

termshark -r foo.pcap -Y tcp.port==10800
```
