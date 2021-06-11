## How to pass arguments to java?

```
gradle run --args="-foo bar --baz"
```

## Add local jars

```
dependencies {
    compile fileTree(dir: 'lib', include: ['*.jar'])
}
```

Ref: https://stackoverflow.com/questions/20700053/how-to-add-local-jar-file-dependency-to-build-gradle-file
