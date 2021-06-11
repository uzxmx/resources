## synchronize

When using synchronize module, if you specify `ansible_ssh_common_args` in inventory file, you may also want to
add `use_ssh_args: yes` like below:

```
synchronize:
  src: src
  dest: dest
  use_ssh_args: yes
```

## Best practices

### Use `_` to separate words instead of `-`
