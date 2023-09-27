# Nginx

## Variables

For all the variables, please visit [here](https://nginx.org/en/docs/http/ngx_http_core_module.html#variables).

#### $host

In this order of precedence: host name from the request line, or host name from
the Host request header field, or the server name matching a request.

One difference between `$host` and `$http_host` is that `$host` doesn't contain
the port even if it's present.

#### $http_name

Arbitrary request header field; the last part of a variable name is the field
name converted to lower case with dashes replaced by underscores.

E.g. `$http_host`, `$http_user_agent`, `$http_referer`, etc.

## Directives

### location

```
location ~* ^/(_nuxt|__webpack_hmr|_loading)/ {
  include /etc/nginx/include.d/frontend_upstream.inc;
}
```

Ref: http://nginx.org/en/docs/http/ngx_http_core_module.html#location

## MIME

```
# When nginx sends out css files, the content type may be `text/plain`. To
# resolve this issue, we can add below into the http block.
include /etc/nginx/mime.types;
```
