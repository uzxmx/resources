# Vimscript

## Function

### Special parameters

| Parameter | Description                              |
|-----------|------------------------------------------|
| a:0       | The number of arguments                  |
| a:000     | The list of arguments                    |
| a:1       | The first argument, the same as a:000[0] |
| a:2       | The second argument                      |
| ...       | The nth argument                         |


### Default parameter value

```
let foo = a:0 > 0 ? a:1 : 'default_string'
```

### Builtin functions

```
type()
string()
function()
repeat(): repeat a string count times
```

## Command

```
command! -bang -range CommandName <line1>,<line2>call s:foo(<bang>0)

command! -bang -range CommandName <line1>,<line2>call s:foo(<bang>0)

command! -nargs=* Gadd call s:GitAdd(<f-args>)
# <q-args> v.s. <f-args>
```
