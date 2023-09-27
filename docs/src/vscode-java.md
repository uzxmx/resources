# vscode-java

### Trace java language server

Ref: https://github.com/redhat-developer/vscode-java/wiki/Troubleshooting

For Mac OSX, the log will be located at `~/Library/Application Support/Code/User/workspaceStorage/<id>/redhat.java/client.log.<suffix>`.

Hint: you can use `ps aux | grep java` to find the jdtls process info.

The log file is rotated when its size is larger than 1MB. TODO how to tail it?


```
/Users/xmx/.vscode/extensions/redhat.java-1.5.0/jre/17.0.2-macosx-x86_64/bin/java --add-modules=ALL-SYSTEM --add-opens java.base/java.util=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/sun.nio.fs=ALL-UNNAMED -Declipse.application=org.eclipse.jdt.ls.core.id1 -Dosgi.bundles.defaultStartLevel=4 -Declipse.product=org.eclipse.jdt.ls.core.product -Djava.import.generatesMetadataFilesAtProjectRoot=false -Dfile.encoding=utf8 -XX:+UseParallelGC -XX:GCTimeRatio=4 -XX:AdaptiveSizePolicyWeight=90 -Dsun.zip.disableMemoryMapping=true -Xmx1G -Xms100m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/Users/xmx/Library/Application Support/Code/User/workspaceStorage/b810ff2d76bf39e3282b776cbed68b43/redhat.java -jar /Users/xmx/.vscode/extensions/redhat.java-1.5.0/server/plugins/org.eclipse.equinox.launcher_1.6.400.v20210924-0641.jar -configuration /Users/xmx/Library/Application Support/Code/User/globalStorage/redhat.java/1.5.0/config_mac -data /Users/xmx/Library/Application Support/Code/User/workspaceStorage/b810ff2d76bf39e3282b776cbed68b43/redhat.java/jdt_ws
```

```
/Users/xmx/.asdf/installs/java/adopt-openjdk-11.0.6+10/bin/java --add-modules=ALL-SYSTEM --add-opens java.base/java.util=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED -Declipse.application=org.eclipse.jdt.ls.core.id1 -Dosgi.bundles.defaultStartLevel=4 -Declipse.product=org.eclipse.jdt.ls.core.product -Dfile.encoding=utf-8 -XX:+UseParallelGC -XX:GCTimeRatio=4 -XX:AdaptiveSizePolicyWeight=90 -Dsun.zip.disableMemoryMapping=true -Xmx1G -Xms100m -noverify -javaagent:/Users/xmx/lombok/lombok.jar -jar /Users/xmx/.config/coc/extensions/coc-java-data/server/plugins/org.eclipse.equinox.launcher_1.5.800.v20200727-1323.jar -configuration /Users/xmx/.config/coc/extensions/coc-java-data/server/config_mac -data /Users/xmx/.config/coc/extensions/coc-java-data/jdt_ws_156a2507632dd381cff02d4c4f869af8
```

```
[Trace - 4:52:11 PM] Received response 'textDocument/completion - (142)' in 928ms.
Result: {
    "isIncomplete": false,
    "items": [
        {
            "label": "AbstractMethodError - java.lang",
            "kind": 7,
            "detail": "java.lang.AbstractMethodError",
```
