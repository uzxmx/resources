# GDB

The executable to debug should be rebuilt with debug symbols added. For example,
the file size of executable `postgres` after rebuilt with debug symbols
increases tens of megabytes.

## Usage

### Basic

```
# Step one instruction exactly.
stepi
si

nexti
ni
```

### Expression

```
p/f 0x3ff199999999999a

# Print the return address.
p *(long *)($rbp + 8)
```

### Attach to a running process

Start gdb with `gdb -p <target-pid>`, or use `attach <target-pid>` command when
in a gdb session.

Note that the user running gdb should be the same user as the one running the
target process, or root. In order to be able to view the source code when
debugging, the user running gdb should also have read permissions for those
source files targeted by debug symbols. So running gdb as root is a better
choice.

### Switch to TUI mode

In order to view source codes clearly, press `Ctrl-x a` to show source code
view.

### Breakpoints

```
# Break at a function.
b func_foo

# Break at a function without skipping prologue.
# See https://stackoverflow.com/a/46880192
b *func_foo

# Break at a specific address.
b *0x400448

# Break at a offset from main function.
b *main+15

# Show breakpoints.
i b

# Remove a breakpoint.
d break <breakpoint-number>
```

### Show information

```
help i
# Show breakpoints
i b
```

### Disassemble

```
disas main

# Disassemble the caller function.
disas *(long *)($rbp + 8)
```

### Misc

```
where
frame
```

### Memory

#### Read memory

```
help x
x/i $pc
x/i 0xffff0
x/10i 0xffff0

```

#### Write memory

### Switch between gdb debug console and program input

* Switch from program input to gdb debug console, hit `CTRL-C`.

* Switch from gdb debug console to program input, input `continue`.

## GEF (GDB Enhanced Features)

### Basic commands

```
# Show regs/stack/code/threads/trace panels.
context
```

### Redirecting context output to another tty/file

#### Method 1

Run below command in gdb console, if gdb is running in a tmux session, then it
will split the pane vertically.

```
gef> tmux-setup
```

#### Method 2

Get the device file by executing `tty`:

```
$ tty
/dev/pts/2
```

Substitute `/dev/pts/2` with the above output and input in gdb console:

```
gef> gef config context.redirect /dev/pts/2
```

If you want to go back to normal, input below:

```
gef> gef config context.redirect ""
```

### Break at a certain offset of a function

```
b *(&func_name + 25)
```
