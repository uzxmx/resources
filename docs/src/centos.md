# CentOS

## yum

### yum repolist

List repos

```
yum repolist
yum repolist -v
```

### yum info

```
yum info postgresql96-server
yum info postgresql96-plperl
```

### yum list

```
yum list
yum list installed
yum list available
yum list | grep postgresql

# --showduplicates will show all versions of a package if available
yum list --showduplicates | grep postgresql

yum list postgresql*
yum list --showduplicates postgresql*
yum list --showduplicates docker-ce | expand
```

### yum deplist

```
yum deplist postgresql-server
```

### yum install

```
yum install postgresql93-libs

# Install a specific version by <package-name>-<version>
yum install postgresql93-libs-9.3.24

# Install by url
yum install http://example.com/some-file.rpm
```

### yum remove

```
yum remove postgresql93-server
```

### yumdownloader (depends on yum-utils)

```
yum install yum-utils

# Download package without installation
yumdownloader bucardo
```

### yum whatprovides

Find out which package owns some command:

```
yum whatprovides '*bin/dig'
```

### yum group

```
yum group list
yum group list hidden
yum group info "GNOME Desktop"
yum group info "X Window System"
yum group install "GNOME Desktop"
```

## rpm

### List files in an RPM file

```
rpm -qlpv some-file.rpm
```

### List files in an installed RPM package

```
rpm -ql postgresql96-server
```

### Extract files from an RPM file

```
rpm2cpio some-file.rpm | cpio -idmv
```

### Show preinstall and postinstall scripts

```
# From an RPM file
rpm -qp --scripts some-file.rpm

# From installed package
rpm -q --scripts postgresql96-server
```

## Install local RPM file

```
rpm -i some-file.rpm

# Install without dependencies
rpm -i --nodeps some-file.rpm
```

## Boot in GUI mode

Make sure command `startx` is available, if not, execute below:

```
sudo yum groups install -y 'GNOME Desktop'
```

Then execute `startx` to go into GUI mode. To always go into gui mode after
rebooting, do this: `sudo systemctl set-default graphical.target`.

Ref: https://geekflare.com/centos-gui-mode/

## Create a new user

```
adduser centos
echo "centos ALL=(ALL) NOPASSWD: ALL" | sudo tee -a /etc/sudoers >/dev/null
su - centos
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo YOUR_PUBLIC_KEY >>~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

## Install GCC 8 on CentOS 7

```
sudo yum install -y centos-release-scl
sudo yum install -y devtoolset-8-gcc devtoolset-8-gcc-c++
scl enable devtoolset-8 -- bash
```

Ref: https://stackoverflow.com/a/55345845
