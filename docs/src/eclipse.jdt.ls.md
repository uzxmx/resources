# Eclipse JDT Language Server for Java

An utility is provided in `dotfiles`.

## Related project

```
https://github.com/eclipse-jdt/eclipse.jdt.core
```

## Build

```
git clone --depth 1 https://github.com/eclipse/eclipse.jdt.ls.git

# The following command will install Apache Maven if necessary, then build the
# server into the `<project-root>/org.eclipse.jdt.ls.product/target/repository` folder:
./mvnw clean verify -Dmaven.test.skip=true

./mvnw verify -Dmaven.test.skip=true

./mvnw package
```

Ref: https://github.com/eclipse/eclipse.jdt.ls#installation

## Dependencies

```
org.eclipse.equinox.launcher
Main

org.eclipse.core.runtime
```

## Command

```
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=1044 -Declipse.application=org.eclipse.jdt.ls.core.id1 -Dosgi.bundles.defaultStartLevel=4 -Declipse.product=org.eclipse.jdt.ls.core.product -Dlog.level=ALL -noverify -Xmx1G -jar ./plugins/org.eclipse.equinox.launcher_1.5.200.v20180922-1751.jar -configuration ./config_linux -data /path/to/data

# When running with JDK9 or more recent, you need to start the server with some extra parameters:
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=1044 -Declipse.application=org.eclipse.jdt.ls.core.id1 -Dosgi.bundles.defaultStartLevel=4 -Declipse.product=org.eclipse.jdt.ls.core.product -Dlog.level=ALL -noverify -Xmx1G -jar ./plugins/org.eclipse.equinox.launcher_1.5.200.v20180922-1751.jar -configuration ./config_linux -data /path/to/data --add-modules=ALL-SYSTEM --add-opens java.base/java.util=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED
```

```
CLIENT_HOST=127.0.0.1 socket.stream.debug=true CLIENT_PORT=5036 /Users/xmx/.asdf/installs/java/adopt-openjdk-11.0.6+10/bin/java
 -agentlib:jdwp=transport=dt_socket,server=n,suspend=y,address=localhost:53977 -Djava.import.generatesMetadataFilesAtProjectRoot=false -cp /Use
rs/xmx/.vscode/extensions/redhat.java-1.5.0/server/plugins/org.eclipse.equinox.launcher_1.6.400.v20210924-0641.jar org.eclipse.equinox.launcher
.Main -application org.eclipse.jdt.ls.core.id1 -data "/Users/xmx/Library/Application Support/Code/User/workspaceStorage/8c7b8bb41733ada472ea0fc
0e59abbff/redhat.java/jdt_ws/../runtime-JDT-LS" -configuration "file:/Users/xmx/Library/Application Support/Code/User/workspaceStorage/8c7b8bb4
1733ada472ea0fc0e59abbff/redhat.java/jdt_ws/.metadata/.plugins/org.eclipse.pde.core/jdt.ls.socket-stream/" -dev "file:/Users/xmx/Library/Applic
ation Support/Code/User/workspaceStorage/8c7b8bb41733ada472ea0fc0e59abbff/redhat.java/jdt_ws/.metadata/.plugins/org.eclipse.pde.core/jdt.ls.soc
ket-stream/dev.properties" -os macosx -ws cocoa -arch x86_64 -nl en_CN -consoleLog 
```

```
CLIENT_HOST=127.0.0.1 CLIENT_PORT=5036 /Users/xmx/.asdf/installs/java/adopt-openjdk-11.0.6+10/bin/java --add-modules=ALL-SYSTEM --add-opens java.base/java.util=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED -Declipse.application=org.eclipse.jdt.ls.core.id1 -Dosgi.bundles.defaultStartLevel=4 -Declipse.product=org.eclipse.jdt.ls.core.product -Dfile.encoding=utf-8 -XX:+UseParallelGC -XX:GCTimeRatio=4 -XX:AdaptiveSizePolicyWeight=90 -Dsun.zip.disableMemoryMapping=true -Xmx1G -Xms100m -noverify -javaagent:/Users/xmx/lombok/lombok.jar -jar /Users/xmx/.config/coc/extensions/coc-java-data/server/plugins/org.eclipse.equinox.launcher_1.5.800.v20200727-1323.jar -configuration /Users/xmx/.config/coc/extensions/coc-java-data/server/config_mac -data /Users/xmx/.config/coc/extensions/coc-java-data/jdt_ws_156a2507632dd381cff02d4c4f869af8
```

```
CLIENT_HOST=127.0.0.1 CLIENT_PORT=5036 \
java \
	-Declipse.application=org.eclipse.jdt.ls.core.id1 \
	-Dosgi.bundles.defaultStartLevel=4 \
	-Declipse.product=org.eclipse.jdt.ls.core.product \
	-Dlog.level=ALL \
	-noverify \
	-Xmx1G \
	--add-modules=ALL-SYSTEM \
	--add-opens java.base/java.util=ALL-UNNAMED \
	--add-opens java.base/java.lang=ALL-UNNAMED \
	-jar org.eclipse.jdt.ls.product/target/repository/plugins/org.eclipse.equinox.launcher_1.6.400.v20210924-0641.jar \
	-configuration org.eclipse.jdt.ls.product/target/repository/config_mac \
	-data /Users/xmx/.config/coc/extensions/coc-java-data/jdt_ws_156a2507632dd381cff02d4c4f869af8
```

```
 position; = "CompletionParams [
  context = CompletionContext [
    triggerKind = Invoked
    triggerCharacter = null
  ]
  partialResultToken = null
  workDoneToken = null
  textDocument = TextDocumentIdentifier [
    uri = "file:///Users/xmx/projects/zoro/src/main/java/com/fqhr/Application.java"
  ]
  uri = null
  position = Position [
    line = 28
    character = 9
  ]
]"
```

Ref: https://www.eclipse.org/community/eclipse_newsletter/2017/may/article4.php

### Debug jdtls

In a shell, execute:

```
export SERVER_PORT=3333
```

Then open a java file by `nvim`, it will show a message: `[coc.nvim] Launching
client with $SERVER_PORT: 3333`.

In another shell, execute:

```
export CLIENT_HOST=127.0.0.1
export CLIENT_PORT=3333
jdtls run
```

Then switch to `nvim`, the client should connect to the Language server.
