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
# Or
tail -F /var/log/messages

wget --bind-address=192.168.3.5 www.example.com -O- >/dev/null

# Add logs for remote host port-forwarding (forward traffic arriving at local port 32443 to remote port 32443).
iptables -t nat -A PREROUTING -p tcp --dport 32443 -j LOG --log-prefix='[nat-prerouting] '
iptables -t nat -A PREROUTING -p tcp --dport 32443 -j DNAT --to-destination <remote-host-ip>:32443
iptables -t nat -A POSTROUTING -p tcp -d <remote-host-ip> --dport 32443 -j LOG --log-prefix='[nat-postrouting] '
iptables -t nat -A POSTROUTING -p tcp -d <remote-host-ip> --dport 32443 -j MASQUERADE
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

### Service relay (port-forwarding)

A service is listening at port 32443 on `Host B`. We want to forward all packets
arriving at port 32443 on `Host A` to the port 32443 on `Host B`.

First, we must enable IP forwarding on `Host A`.

```
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
```

Or add `net.ipv4.ip_forward = 1` to `/etc/sysctl.conf` to enable it permanently.

Then setup iptables on `Host A`.

```
sudo iptables -I FORWARD -p tcp -d <host-A-ip> --dport 32443 -j ACCEPT
sudo iptables -I FORWARD -p tcp -s <host-A-ip> --dport 32443 -j ACCEPT

sudo iptables -t nat -A PREROUTING -p tcp --dport 32443 -j DNAT --to-destination <host-A-IP>:32443
sudo iptables -t nat -A POSTROUTING -p tcp -d <host-A-IP> --dport 32443 -j MASQUERADE
```

## MASQUERADE v.s. SNAT

Ref: https://unix.stackexchange.com/a/264540
