# nmap

### Examples

#### Get all hosts in a local network

```
nmap -sP 10.0.1.0/24
sudo nmap -sn 192.168.3.0/24
```

```
# Ref: https://superuser.com/questions/591863/how-to-resolve-local-domain-name
# TODO see mDNS
# sudo dns-sd -B _services._dns-sd._udp 192.168.3.8
ping DESKTOP-FOO.local
```

#### Scan ports in a local network

```
nmap -sV -p 22,80,443 10.0.1.0/24
```
