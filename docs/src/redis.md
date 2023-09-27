# Redis

```
info
keys *
sync

# Delete all keys
flushall
flushdb
```

## List

```
lrange key 0 -1
```

## Set

```
scard key

smembers key
```

## Zset

```
zcard key
zrange key 0 -1
```
