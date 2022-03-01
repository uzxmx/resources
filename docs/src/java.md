# Java

## Change java locale

### Method 1: use environment variable

This method only works if the program supports environment variable:
`JAVA_TOOL_OPTIONS`.

```
JAVA_TOOL_OPTIONS="-Duser.language=en -Duser.region=US" java -h
JAVA_TOOL_OPTIONS="-Duser.language=en -Duser.region=US" jdb -h
JAVA_TOOL_OPTIONS="-Duser.language=en -Duser.region=US" jarsigner -h
```

Ref:
* https://stackoverflow.com/a/24987464
* https://stackoverflow.com/questions/28327620/difference-between-java-options-java-tool-options-and-java-opts/

### Method 2: use options

This method only works if the program supports passing options:
`-Duser.language=en -Duser.region=US`.

```
# Change local to en_US for java CLI.
java -Duser.language=en -Duser.region=US -h

# Show current locale.
java -XshowSettings -version
```
