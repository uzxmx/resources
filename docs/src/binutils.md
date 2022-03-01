# binutils

## Compiler

## Linker

ld v.s. gold(bin.gold) v.s. lld

gold(bin.gold) is better than ld.

lld provided by LLVM is better than gold.

Ref: https://stackoverflow.com/questions/3476093/replacing-ld-with-gold-any-experience

### Static library

### Dynamic library: build time v.s. runtime

#### Build time

-L/opt/openssl/lib -lcrypto

#### Runtime

rpath

Note when building, you must specify the rpath.

For clang, use:

```
clang main.c -o main -I./openssl-build/include -lcrypto -L./openssl-build/lib -rpath ./openssl-build/lib
```

## Debug

```
# Generate debug information.
clang -g
```

## Mac OSX specific ones

### otool

#### Display names and version numbers of referenced shared libraries for an object file

```
otool -L object-file
otool -l object-file
```
