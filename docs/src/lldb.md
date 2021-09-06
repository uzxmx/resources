# LLDB

`lldb` is a powerful debugger used in Xcode. You can use this tool to reverse
engineer and debug code written in C++, Objective-C, and C. `lldb` allows you to
debug code on both actual iOS devices and simulators.

## Workflow

### Execution

Start lldb:

```
$ lldb [path-to-executable]
```

If you don't specify an executable when launching lldb, you may specify it when
you are in a lldb session:

```
(lldb) target create <path-to-executable>
```

If you don't know where to stop the program at, you can stop it at the entry:

```
(lldb) process launch --stop-at-entry
```

Also, you may want to redirect the program IO so you can input lldb commands:

```
(lldb) process launch --stop-at-entry -o stdout.txt -e stderr.txt -i stdin.txt
```

Or just not set up for terminal I/O to go to running process:

```
(lldb) process launch --stop-at-entry -n
```

For more info, please see `help process launch`.

Step out of the currently selected frame:

```
(lldb) finish
```

### Thread

List threads:

```
(lldb) thread list
```

Show thread call stacks:

```
# Show call stack for current thread.
(lldb) thread backtrace
# Below is the abbreviation.
(lldb) bt

# Show call stacks for all threads.
(lldb) thread backtrace all

# Show call stack for thread with a specific index.
(lldb) thread backtrace <thread-index>
```

Others:

```
(lldb) process interrupt
(lldb) thread select <thread-index>
```

### Breakpoints

Set the breakpoint by function name:

```
(lldb) break set -n main
(lldb) break set -n func1 -n func2
```

Set the breakpoint at an address:

```
(lldb) break set -N <breakpoint-name> -a 0xbffff3c0
```

Add command to run after a breakpoint is hit:

```
# If no breakpoint id is specified, adds the commands to the last created breakpoint.
(lldb) break command add
x $rsi
DONE
```

Add python scripts to run after a breakpoint is hit:

```
(lldb) command script import path/to/foo.py

(lldb) break set -N foo -a 0x100aebf81

# If no breakpoint id is specified, adds the commands to the last created breakpoint.
(lldb) break command add -s python
# `foo` is a function defined in `path/to/foo.py`.
foo(frame)
return False
DONE
```

Optionally, a Python breakpoint command can return a value. Returning False
tells LLDB that you do not want to stop at the breakpoint. Any other return
value (including None or leaving out the return statement altogether) is akin to
telling LLDB to actually stop at the breakpoint. This can be useful in
situations where a breakpoint only needs to stop the process when certain
conditions are met, and you do not want to inspect the program state manually at
every stop and then continue.

### Disassemble

Show current instruction:

```
(lldb) dis -p
```

Start disassembling from an address, with number of instructions to display:

```
(lldb) dis -s 0x101ac5fdb -c 10
```

Disassemble function containing an address:

```
(lldb) dis -a 0x101ac5fdb
```

Show opcode bytes when disassembling:

```
(lldb) dis -a 0x101ac5fdb -b
```

### Display

```
(lldb) memory read 0x10505C400
(lldb) memory read 0x10505C400 -c 128
(lldb) memory read 0x10505C400 -c 2048 --force
```

### Watchpoints

```
(lldb) watch set expression -w read -- 0x101008200
```

### Show all shared libraries (modules)

```
(lldb) image list -g
```

### Expression

```
# Suppose `0x112a04080` is a pointer to an instance of `NSButton`.
(lldb) expression -lobjc -O -- id obj = (id) 0x112a04080; [obj target];
(lldb) expression -lobjc -O -- id obj = (id) 0x112a04080; SEL sel = (SEL) [obj action]; sel_getName(sel);
(lldb) expression -lobjc -O -- id obj = (id) 0x112a04080; SEL sel = (SEL) [obj action]; object_getMethodImplementation((id) [obj target], sel);

(lldb) expression -lobjc -O -- id obj = (id) 0x112a04080; [obj setHidden:YES];
(lldb) expression -lobjc -O -- id obj = (id) 0x112a04080; [obj isHidden];
(lldb) expression -lobjc -O -- id obj = (id) 0x112a04080; [obj title];
(lldb) expression -lobjc -O -- id obj = (id) 0x112a04080; [obj setTitle:@"foo"];

# Convert `NSString` to `NSData`.
(lldb) expression -lobjc -O -- NSString* str = @"foo"; [str dataUsingEncoding:NSUTF8StringEncoding];
```

### Modify instructions

Let's look at an example. Below is an assembly function found in
`CoreFoundation`.

```
CoreFoundation`__CFRunLoopServiceMachPort:
    ...
    0x7fff205cad03 <+784>: testl  %r14d, %r14d
    0x7fff205cad06 <+787>: jne    0x7fff205cad45            ; <+850>
    0x7fff205cad08 <+789>: movl   0xc(%r13), %eax
    ...
    0x7fff205cad43 <+848>: popq   %rbp
    0x7fff205cad44 <+849>: retq
->  0x7fff205cad45 <+850>: ud2
    0x7fff205cad47 <+852>: nop
    0x7fff205cad48 <+853>: nop
    0x7fff205cad49 <+854>: nop
```

For the above example, we don't want to jump to `<+850>`, so we can use two `nop` (0x90)
instructions to replace the two-bytes `jne` instruction as shown below.

```
(lldb) memory write 0x7fff205cad06 0x90 0x90
```
