# coc.nvim

## Debug language server

Ref: https://github.com/neoclide/coc.nvim/wiki/Debug-language-server

## Languages

For other language servers not listed below, please visit
`https://github.com/neoclide/coc.nvim/wiki/Language-servers`.

### Java

Use `coc-java` extension.

#### Commands

```
# Below is the same as when you execute `:CocCommand`, and then select `java.open.serverLog`.
# For supported commands, please visit https://github.com/neoclide/coc-java#available-commands
:call CocAction('runCommand', 'java.open.serverLog')

:call CocActionAsync('runCommand', 'java.action.organizeImports')
```

#### coc-java-dependency

```
:echo CocRequest('java', 'workspace/executeCommand', { 'command': 'java.project.getAll' })

# Replace `workspace-uri` with the output of the above command.
:echo CocRequest('java', 'workspace/executeCommand', { 'command': 'java.project.list', 'arguments': ['workspace-uri'] })
:echo CocRequest('java', 'workspace/executeCommand', { 'command': 'java.project.getMainClasses', 'arguments': ['workspace-uri'] })

```

#### How to integrate with `Project Lombok`?

Download some version of lombok jar to somewhere and optionally create a link `lombok.jar`
to that file. Add below settings to `coc-settings.json`.

```
{
  "java.jdt.ls.vmargs": "-javaagent:<absolute-path-to-lombok-jar>"
}
```

Refs:

* https://github.com/neoclide/coc-java/issues/27
* https://github.com/redhat-developer/vscode-java/wiki/Lombok-support

#### Troubleshooting

* Run `:messages` to get echoed messages in vim.
* Enable verbose trace for jdt.ls by adding `"java.trace.server": "verbose"` in your settings file, then check output by `:CocCommand workspace.showOutput java`.
* Run `:CocCommand java.open.serverLog` to open log of jdt.ls.
* Try `:CocCommand java.clean.workspace` to clean workspace cache.

### C/C++(a.k.a CPP)/Objective-C

Use `clangd` with `coc-clangd` extension.

Run `$dotfiles_dir/scripts/install/coc_extensions clangd` to install.

Note that `clangd` relies on `compile_commands.json` file to work, so you
need to use other tools to generate that file or do it manually. You can find
available tools [here](https://clangd.llvm.org/installation.html#project-setup).

If all files in a project use the same build flags, you don't need to provide
`compile_commands.json`. Instead, you can put those flags one-per-line in
`compile_flags.txt` in your source root.

Ref:
* https://github.com/clangd/coc-clangd

## How to develop or debug coc.nvim

Based on commit `ba262ef03029c3fd6a5062bebce7d8553e3b1a1f`.

### Build on file change

```
npm run build -- --watch
# Or
yarn build --watch
```

### Debug by log

```
export NVIM_COC_LOG_FILE=<path-to-log-file>
# The default log level is `info`.
export NVIM_COC_LOG_LEVEL=debug
```

Ref: https://github.com/neoclide/coc.nvim/wiki/Environment-variables#logger

### Show communication between coc.nvim and language server

Ref: https://github.com/neoclide/coc.nvim/wiki/Debug-language-server#using-output-channel

## How to debug kotlin-language-server?

Open a terminal and change to kotlin-language-server root directory.

```
# Suppose kotlin-language-server is listening at 18091.
./gradlew :server:run --args='--tcpServerPort 18091'
```

Add below configuration to `coc-settings.json`.

```
{
  "languageserver": {
    "kotlin": {
      "port": 18091,
      "filetypes": ["kotlin"]
    }
  }
}
```

Open another terminal and use vim to open a kotlin project. You can
use `CocInfo` to view kotlin-language-server log.

## Misc

### Automatically select first item of popup menu

```
Add `"coc.preferences.noselect": false` to coc-settings.json.

Ref: https://github.com/neoclide/coc.nvim/issues/124
```

### Loading order of `coc-settings.json`

TODO
We can create a custom configuration file at `<project-root-dir>/.vim/coc-settings.json`.

### Resources

https://github.com/neoclide/coc.nvim/issues/308
https://github.com/neoclide/coc.nvim/wiki/Using-snippets

https://github.com/neoclide/coc.nvim/wiki/F.A.Q

https://github.com/Shougo/echodoc.vim

https://zhuanlan.zhihu.com/p/37588324
https://github.com/tenfyzhong/CompleteParameter.vim
https://github.com/neoclide/coc-snippets

https://github.com/neoclide/coc.nvim/wiki/Using-coc-list

https://github.com/neoclide/coc.nvim/wiki/Completion-with-sources#trigger-mode-of-completion

https://github.com/neoclide/coc.nvim/wiki
