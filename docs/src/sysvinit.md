# SysVInit

```
service --status-all
```

According to ansible service module, init systems include BSD init, OpenRC, SysV, Solaris SMF, systemd, upstart.
Ref: https://docs.ansible.com/ansible/latest/modules/service_module.html

We can use `chkconfig` command to update and query runlevel information for
system services.

```
chkconfig --list
chkconfig --list nginx

# Start nginx on boot
chkconfig nginx off

# Do not start nginx on boot
chkconfig nginx off
```

Below are some useful commands about runlevel:

```
# Get current run level
runlevel

man runlevel
man 7 runlevel
```
