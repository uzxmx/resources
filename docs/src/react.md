# React

## Component dirty, update, cache

A component may be created once, and in later updates, its `props` may be
updated.

## Error: ENOSPC: System limit for number of file watchers reached

For Linux, this error may happen because of the watch limit. To increase the
limit, do as follows:

```
# insert the new value into the system config
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p

# check that the new value was applied
cat /proc/sys/fs/inotify/max_user_watches
```

Ref: https://stackoverflow.com/questions/55763428/react-native-error-enospc-system-limit-for-number-of-file-watchers-reached
