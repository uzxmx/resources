# iptables

## Tables and chains

* filter (default table)
  * INPUT
  * FORWARD
  * OUTPUT
* nat
  * PREROUTING
  * INPUT
  * OUTPUT
  * POSTROUTING
* mangle
* raw
* security

## Recipes

### Show rules

```
iptables -L
iptables -L -t nat
iptables -L -n -v
```

### Modify behavior commands

```
# Drop all incoming packets
iptables -A INPUT -j DROP

# Allow outgoing tcp packet at 80
iptables -A OUPUT -p tcp --dport 80 -j ACCEPT

# Drop all packets
iptables -P OUTPUT DROP
```

### Add log

```
# Add log for incoming packet for 192.168.11.0/24
iptables -A INPUT -s 192.168.11.0/24 -j LOG --log-prefix='[netfilter] '

# Add log for outgoing tcp packet at 80 port
iptables -A OUTPUT -p tcp --dport 80 -j LOG --log-prefix='[netfilter] '

# With specific source address
iptables -A OUTPUT -p tcp -s 192.168.3.5 --dport 80 -j LOG --log-prefix='[netfilter] '

# Use below commands to watch the log
tail -F /var/log/kern.log
wget --bind-address=192.168.3.5 www.example.com -O- >/dev/null
```

### Flush rules for system defined chain

```
# Delete all the rules for all the chains of filter table
iptables -F

# Delete all the rules for all the chains of nat table
iptables -F -t nat
```

### Delete user defined chains

```
iptables -X
iptables -X -t nat
```

### Save rules

```
iptables-save >iptables.rules
```

### Restore rules

```
iptables-restore <iptables.rules
```

This command won't clear iptables before restoring, so be cautious to avoid duplicated rules.

### Enable internet access for traffic from 172.17.0.0/16

```
iptables -t nat -A POSTROUTING -s 172.17.0.0/16 ! -d 10.0.0.0/8 -m addrtype ! --dst-type LOCAL -j MASQUERADE
```

## Using iptables for shadowsocks relay

If you want your client connected to a Japan VPS, but you want an US IP.

```
Client <--> Japan VPS <--> US VPS
```

```
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A PREROUTING -p tcp --dport 8388 -j DNAT --to-destination US_VPS_IP:8388
iptables -t nat -A POSTROUTING -p tcp -d US_VPS_IP --dport 8388 -j SNAT --to-source JAPAN_VPS_IP
```

### Service relay

Must enable ip forwarding

add `net.ipv4.ip_forward = 1` to /etc/sysctl.conf

```
sudo iptables -t nat -A PREROUTING -p tcp --dport 5432 -j DNAT --to-destination 10.0.1.236:31090
sudo iptables -t nat -A POSTROUTING -p tcp -d 10.0.1.236 --dport 31090 -j MASQUERADE
```

## MASQUERADE v.s. SNAT

Ref: https://unix.stackexchange.com/a/264540
