# Frida CLI example

This example demonstrates how to use frida to instrument a CLI application.

## Get Started

```
make
frida -l script.js -f ./main
```

The output is like below:

```
     ____
    / _  |   Frida 16.0.1 - A world-class dynamic instrumentation toolkit
   | (_| |
    > _  |   Commands:
   /_/ |_|       help      -> Displays the help system
   . . . .       object?   -> Display information about 'object'
   . . . .       exit/quit -> Exit
   . . . .
   . . . .   More info at https://frida.re/docs/home/
   . . . .
   . . . .   Connected to Local System (id=local)
Spawned `./main`. Resuming main thread!
[Local::main ]-> say_hello called
static_say_hello called
malloc(10240)
-> 0xb77930
free(0xb77930)
say_hello()
puts(0x4006d8)
static_say_hello()
puts(0x4006c0)
Process terminated
[Local::main ]->

Thank you for using Frida!
```

## Ref

https://monosource.github.io/tutorial/2017/01/26/frida-linux-part1/
