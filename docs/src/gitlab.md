# Gitlab

## Commands

```
# Restart nginx bundled with gitlab.
gitlab-ctl restart nginx

# Show logs.
gitlab-ctl tail
```

## gitlab runner shell executor ERROR: Job failed: exit status 1

This may be caused by `cd` redefined by `rvm`.
