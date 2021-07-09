# Nginx

```
# When nginx sends out css files, the content type may be `text/plain`. To
# resolve this issue, we can add below into the http block.
include /etc/nginx/mime.types;
```
