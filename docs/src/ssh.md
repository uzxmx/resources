## sshkey-gen

```
# Generate ssh key to a customized place
ssh-keygen -t rsa -f path-to-private-key-to-save

# For Mac OSX mojave, you may also need to add `-m PEM`
# Ref: https://serverfault.com/questions/939909/ssh-keygen-does-not-create-rsa-private-key
ssh-keygen -m PEM -t rsa -f path-to-private-key-to-save

# Get public key from private key
ssh-keygen -y -f id_rsa >id_rsa.pub

# Show fingerprint
ssh-keygen -E md5 -lf id_rsa
ssh-keygen -E md5 -lf id_rsa.pub
```

## SSH Command

```
Press `enter` `~` `?` to show help
Press `enter` `~` `.` to terminate connection
```

### Force ssh client to use password authentication

```
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no user@host
```

> Make sure `/etc/ssh/sshd_config` is configured with `PasswordAuthentication yes`, otherwise
the connection will be closed.

## keyboard-interactive authentication

If you want to use keyboard-interactive authentication, you may need to configure `/etc/ssh/sshd_config`:

```
PasswordAuthentication no
ChallengeResponseAuthentication yes
```

Then execute:

```
ssh -o PreferredAuthentications=keyboard-interactive user@host
```

## Agent forwarding

```
ssh -A user@host
```

If a new ssh agent is started in remote shell's initialization process, then agent forwarding will not work.

### Test if an ssh key works for a connection

```
ssh -o IdentitiesOnly=yes -i <pem-file> user@host
```

Note that `-o IdentitiesOnly=yes` is important, because it prevents ssh client
using keys from ssh-agent.

Ref: https://superuser.com/a/436015

##  Run a command on local machine while on ssh in bash

https://stackoverflow.com/questions/38567427/run-a-command-on-local-machine-while-on-ssh-in-bash

https://superuser.com/questions/322757/reverse-tunnel-commands-through-ssh

How to support navigation when starting a ssh session in a tmux pane and executing vim on remote machine?

* tmux -> remote vim

we can check if vim is running by pane title.
Ref: https://github.com/christoomey/vim-tmux-navigator/blob/master/vim-tmux-navigator.tmux

* remote vim -> tmux

We can create a server on local machine which executes commands from remote machine. That server will listen at some port, and that port can be tunneled to remote through ssh.

Question: Is the tunnel secure?

https://github.com/ptenteromano/remote-shell-OS

## Useful links

https://superuser.com/questions/421997/what-is-a-ssh-key-fingerprint-and-how-is-it-generated
https://security.stackexchange.com/questions/41380/are-duplicate-ssh-server-host-keys-a-problem

## How to run sshd on WSL Ubuntu?

```
service ssh status
service ssh start

# Use below command to debug.
sudo /usr/sbin/sshd -d

# Make sure three types (rsa, ecdsa, ed25519) of keys exist in /etc/ssh/.
sudo ssh-kengen -t <type> -f /etc/ssh/ssh_host_<type>_key
```

## Expose a private SSH server to public

Use `autossh` to keep ssh client alive.

The ssh option `-N` is required when only forwarding ports.

```
# Turn the monitoring function off. Ask ssh client to disconnect after 60 seconds of no
# response from the server, and then `autossh` would reconnect automatically.
autossh -M 0 -f user@host -L LOCAL_PORT:localhost:32443 -N -o "ServerAliveInterval 20" -o "ServerAliveCountMax 3"

# By specifying `-M 20000`, `autossh` will set up forwards so that it can send
# data on port 20000 and receive it back on 20001.
autossh -M 20000 -f user@host -R REMOTE_PORT:localhost:22 -N
```

Note: The remote ssh server must be configured with `GatewayPorts yes` when ssh
client wants to bind to all remote interfaces.

## Connect to a private host through a bastion host

* Using `ProxyJump` option or `-J` which is a shortcut.

```
ssh -J user@bastion-host user@target-host
```

* Using `ProxyCommand` option.

```
ssh -o ProxyCommand="ssh user@bastion-host -W %h:%p" user@target-host
```

Note:`ProxyJump` is a simplified way of `ProxyCommand`. `ProxyCommand` can also be
used for other purposes.

## Disable host key checking and do not add host key to `known_hosts` file

```
ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null user@host
```

## Cheatsheet

```
# Forward traffic from local to remote.
ssh user@host -L [local_bind_address:]local_port:localhost:remote_port

# Forward traffic from remote to local.
#
# * An empty bind_address, or the address `*`, indicates that the remote socket should listen
# on all interfaces.
#
# * When binding to all remote interfaces, the remote ssh server must be configured with `GatewayPorts yes`.
#
# * Specifying a remote bind_address will only succeed if the server's `GatewayPorts` option is enabled.

ssh user@host -R [remote_bind_address:]remote_port:localhost:local_port

# Create a SOCKS server on local side at a specific port which routes all requests through the
remote server.
ssh user@host -D port
```

## ProxyCommand

OpenSSH runs `ProxyCommand` with `$SHELL` by `execv`. So if `$SHELL` doesn't
expand to an absolute path, it will fail with such error like: `bash: No such
file or directory`.

Ref:
* https://stackoverflow.com/a/64893356
* https://github.com/theos/theos/issues/481
