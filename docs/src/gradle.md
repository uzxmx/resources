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

## HTTP proxy

~/.gradle/gradle.properties

```
systemProp.http.proxyHost=localhost
systemProp.http.proxyPort=8123
systemProp.https.proxyHost=localhost
systemProp.https.proxyPort=8123
```

## Java compatibility

Ref: https://stackoverflow.com/questions/41017544/how-to-specify-source-and-target-compatibility-in-java-module

## Skip a task

```
gradle -x <task>

# Skip compiling java.
gradle -x compileJava

# Skip test for gradle.
gradle build -x test
```

Ref: https://stackoverflow.com/questions/4597850/gradle-build-without-tests
