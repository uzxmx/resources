# Gradle

## How to pass arguments to java?

```
gradle run --args="-foo bar --baz"
```

## Cheatsheet for gradle script

### Add local jars

```
dependencies {
  implementation files("${System.getProperty('user.home')}/foo/bar.jar")
  implementation fileTree(dir: 'lib', include: ['*.jar'])
}
```

Ref: https://stackoverflow.com/questions/20700053/how-to-add-local-jar-file-dependency-to-build-gradle-file

### Custom java source directory in initscript

```
allprojects {
  apply plugin: 'java'

    sourceSets {
      main {
        java {
          srcDir "${System.getProperty('user.home')}/foo/src/main/java'
        }
      }
    }
}
```
