# Ubuntu

## Shortcuts

```
F11: maximize the terminal window
```

## Manage packages

```
# List installed packages.
apt list --installed
apt list --installed | grep firefox

# List installed packages by `dpkg-query`.
dpkg-query -l

# List installed files from <package-name>.
dpkg -L <package-name>

# List contents of a deb package.
dpkg -c foo.deb

# Extract the files contained by package to a directory.
dpkg -x foo.deb <dir>
```
