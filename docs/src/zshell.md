# Zshell

## Builtins

```
bindkey
zle -l

# Alias for `fc -l`
history
fc -l
fc -rln 1
```

Ref: https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html

## Zshell widgets

```
# _search_global_history() {
#   # local selected=$(fc -p -a "$HISTFILE"; fc -rln 1 | FZF_DEFAULT_OPTS="--height 50% $FZF_DEFAULT_OPTS --tiebreak=index --bind=ctrl-r:toggle-sort --query=${(qqq)LBUFFER} +m" fzf)
#   local selected=$(fc -p -a "$HISTFILE"; fc -rln 1 | FZF_DEFAULT_OPTS="--height 50% $FZF_DEFAULT_OPTS --tiebreak=index --bind=ctrl-r:toggle-sort --query=${(qqq)LBUFFER} +m" fzf)
#   local ret=$?
#   if [ -n "$selected" ]; then
#     BUFFER=$selected
#     zle end-of-line
#   fi
#   zle reset-prompt
#   return $ret
# }
```
