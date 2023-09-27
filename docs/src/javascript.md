# TypeScript

## Disable property does not exist
https://stackoverflow.com/questions/18083389/ignore-typescript-errors-property-does-not-exist-on-value-of-type

## Show stacktrace

### Method 1

```
console.log(new Error().stack);
```

### Method 2

```
console.trace();
```
