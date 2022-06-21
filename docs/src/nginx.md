# Nginx

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
