# Brew

## Terminology

formula: Homebrew package definition built from upstream sources

cask: Homebrew package definition that installs macOS native applications

keg: installation destination directory of a given formula version e.g. /usr/local/Cellar/foo/0.1

rack: directory containing one or more versioned kegs e.g. /usr/local/Cellar/foo

keg-only a formula is keg-only if it is not symlinked into Homebrew's prefix (e.g. /usr/local)

cellar: directory containing one or more named racks e.g. /usr/local/Cellar

Caskroom: directory containing one or more named casks e.g. /usr/local/Caskroom

tap: directory (and usually Git repository) of formulae, casks and/or external commands

bottle: pre-built keg poured into the cellar/rack instead of building from upstream

## Commands

```
man brew

# Show homebrew directory.
brew --repo

# Show a tap directory.
brew --repo user/repo
brew --repo homebrew/core
brew --repo homebrew/cask

brew deps imagemagick@6

# Allow keg-only formulae to be linked into places like `/usr/local/bin`,
# `/usr/local/lib`, etc.
brew link --force imagemagick@6

# List all installed formulae and casks.
brew list -1 -l
```

## keg-only

For a software to be "keg-only" means it is installed in `/usr/local/Cellar` but
not linked into places like `/usr/local/bin`, `/usr/local/lib`, etc. That means
other software that depends on it has to be compiled with specific instructions
to use the files in `/usr/local/Cellar`.

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

## Formula v.s. Cask

Homebrew calls its package definition files “formulae” (British plural for
“formula”). Homebrew-Cask calls them “casks”. A cask, just like a formula, is a
file written in a Ruby-based DSL that describes how to install something.

Homebrew-Cask is an extension to Homebrew to install GUI applications such as
Google Chrome or Atom. It started independently but its maintainers now work
closely with Homebrew’s core team.

Homebrew Cask extends Homebrew and brings its elegance, simplicity, and speed to
the installation and management of GUI macOS applications such as Atom and
Google Chrome.

## Tap (Third-Party Repositories)

Brew tap adds more repositories to the list of formulae that brew tracks,
updates, and installs from. By default, tap assumes that the repositories come
from GitHub, but the command isn’t limited to any one location.
