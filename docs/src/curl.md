# Curl

## Post a form

```
curl -i -F name=test -F filedata=@localfile.jpg http://example.com/upload
```

## Cookie

For the first time, pass the cookie by HTTP header, and the response cookie will
be saved into `cookie.txt` file.

```
curl http://example.com -H 'Cookie: ...' -c cookie.txt
```

Later we don't need to pass the cookie by HTTP header any more.

```
curl http://example.com -b cookie.txt -c cookie.txt
```

## httpbin

```
curl -XPOST https://httpbin.org/post -H 'Content-Type: application/json' -d'
{
  "a_string": "foo",
  "a_boolean": true
}
'
```

## HTTP encode

See `url_encode_by_curl` from [here](https://github.com/uzxmx/dotfiles/blob/master/scripts/lib/url.sh).

## HTTP Proxy

```
# HTTP proxy.
curl --proxy http://username:password@host:port example.com

# HTTPS proxy with TLS verification disabled.
curl --proxy https://username:password@host:port --proxy-insecure example.com
```
