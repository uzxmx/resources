# Brew

## Commands

```
brew deps imagemagick@6

# What does this do?
brew link --force imagemagick@6
```

## Brew directories

```
# Brew itself exists in below directories.
/usr/local/Homebrew
/usr/local/Caskroom

# All packages are installed in this directory.
/usr/local/Cellar
```

Brew will create links at standard locations. E.g.

```
/usr/local/bin
/usr/local/opt
/usr/local/lib
/usr/local/etc
/usr/local/share
```

## formula v.s. cask

## How can we have a library with different versions in the system?

Suppose you have installed `imagemagick` at
`/usr/local/Cellar/imagemagick/7.1.0-4_1`. Now you want to install
`imagemagick@6` by `brew install imagemagick@6`. After successful installation,
brew shows the following message:

```
imagemagick@6 is keg-only, which means it was not symlinked into /usr/local,
because this is an alternate version of another formula.

If you need to have imagemagick@6 first in your PATH, run:
  echo 'export PATH="/usr/local/opt/imagemagick@6/bin:$PATH"' >> ~/.zshrc

For compilers to find imagemagick@6 you may need to set:
  export LDFLAGS="-L/usr/local/opt/imagemagick@6/lib"
  export CPPFLAGS="-I/usr/local/opt/imagemagick@6/include"

For pkg-config to find imagemagick@6 you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/imagemagick@6/lib/pkgconfig"
```
