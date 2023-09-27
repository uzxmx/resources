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

## jdb

### Launching java debugger

```
# Start the JVM, and suspend execution before it starts the Java application.
# If you don't want to suspend, change to `suspend=n`.
# The address can be like `localhost:53977`, or just a port `53977`.
# TODO what does `server=y`, `server=n` mean?
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=<address> <class>

# Then attach the debugger to the JVM.
jdb -attach <address>

# Specify sourcepath
jdb -attach <address> -sourcepath org.eclipse.jdt.ls.core/src
```

### jdb commands

```
run

stop in org.eclipse.jdt.ls.core.internal.handlers.JDTLanguageServer.completion
stop at org.eclipse.jdt.ls.core.internal.handlers.JDTLanguageServer:542
stop at org.eclipse.jdt.ls.core.internal.handlers.CompletionHandler:163
stop at org.eclipse.jdt.ls.core.internal.contentassist.CompletionProposalRequestor:187
stop in org.eclipse.jdt.ls.core.internal.handlers.JDTLanguageServer.resolveCompletionItem

sourcepath org.eclipse.jdt.ls.core/src
# Alias for sourcepath.
use org.eclipse.jdt.ls.core/src

use /Users/xmx/tmp/org.eclipse.jdt.core-3.29.0-sources

print <variable-name>
locals

# Step into method call.
step

# Step instruction.
stepi

# Step over method call.
next

threads
where
wherei

stop in java.lang.System.loadLibrary
stop in com.example.android.b.a.e.a(java.lang.String)
stop in com.example.android.Application$1.run
```

### jdb hanging when attaching to android application

Try quitting android studio.

Ref:

* https://stackoverflow.com/a/46373071
* https://stackoverflow.com/a/46372952

## Make Java JVM use HTTP proxy

TODO verify this

Specify below JVM options.

```
-Dhttp.proxyHost=127.0.0.1 -Dhttp.proxyPort=8081
```

For simplicity, if the program supports `JAVA_TOOL_OPTIONS`, you can just do
`export JAVA_TOOL_OPTIONS="$JAVA_TOOL_OPTIONS -Dhttp.proxyHost=127.0.0.1 -Dhttp.proxyPort=8081"`.

-Djava.net.useSystemProxies=true

## Java REPL

```
jshell
```

```
BigDecimal base = new BigDecimal(6);
BigDecimal totalAmount = base.multiply(new BigDecimal(0.063)).setScale(2, RoundingMode.CEILING);
BigDecimal amount = base.multiply(new BigDecimal(0.044)).setScale(2, RoundingMode.CEILING);
totalAmount.subtract(amount);

# Write to a file.
java.nio.file.Files.write(java.nio.file.Paths.get(System.getProperty("user.home"), "tmp/foo.log"), "bar\n".getBytes());

# Append to a file.
java.nio.file.Files.write(java.nio.file.Paths.get(System.getProperty("user.home"), "tmp/foo.log"), "bar\n".getBytes(), java.nio.file.StandardOpenOption.APPEND);


try { java.nio.file.Files.write(java.nio.file.Paths.get(System.getProperty("user.home"), "tmp/foo.log"), String.format("time: %d\n", System.currentTimeMillis() - startTime).getBytes(), java.nio.file.StandardOpenOption.APPEND); } catch(Exception e) {}
```
