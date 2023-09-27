# Find

## Find files by multiple extensions

```
find . -type f \( -name "*.html" -o -name "*.js" \)

# Case insensitive.
find . -type f \( -iname "*.jpg" -o -iname "*.png" \)
```

## Remove large number of files

```
find . -maxdepth 1 -name 'prefix_*' | xargs rm -rf
```
