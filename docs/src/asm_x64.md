# ASM for x64 CPU

This document covers X86-64 registers, stack, assembly language, etc.

Intel syntax v.s. AT&T syntax

You can convert C source file to assembly file by using `gcc -S` or `clang -S`.

## Gas (GNU assembler)

For how to write assembly in `gas` syntax, see:

https://stackoverflow.com/questions/36854078/whats-the-difference-between-the-asciz-and-the-string-assembler-directives/59427479
https://sourceware.org/binutils/docs/as/index.html#SEC_Contents
https://sourceware.org/binutils/docs/as/Equiv.html
https://ftp.gnu.org/old-gnu/Manuals/gas-2.9.1/html_chapter/as_7.html
https://stackoverflow.com/questions/8987767/is-there-a-symbol-that-represents-the-current-address-in-gnu-gas-assembly
https://developer.ibm.com/articles/l-gas-nasm/

## Regsiters

### RBP

A register which stores the address of the base of the stack for the current
frame.

### RSP

A register which stores the address of the top of the stack for the current
frame.

`push` and `pop` instructions will change the value of `RSP`.

TODO Summarize registers by referencing https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/x64-architecture

## Stack

The stack grows from high address to low address. In other words, `push` makes
`RSP` decrease, `pop` makes `RSP` increase.

## Assembly language

### Test

```
0x100220678 <+72>:  testb  $0x1, %dl ; perform dl & 0x1
0x10022067b <+75>:  jne    0x100220682               ; <+82> jump if not zero
```

### Jump

Jump when rax is not zero.

```
testq  %rax, %rax
jne    0x101af4274
```

### Compare

```
cmpq   $0x4, 0x110(%rbx)
```

### Rotate

ROL

```
# Rotate ECX register left 26 times.
# Example: 0x510E527F -> 0xFD443949
roll   $0x1a, %ecx
```

### ud2

undefined instruction

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

## Calling conventions

### System V AMD64 ABI

Both Linux and Mac OSX conform to this calling convention.

The first 6 arguments are passed in by `rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9` in
order. More arguments are passed onto the stack.

The return value is passed out by `rax`.

Ref: https://ddeville.me/static/media/files/posts/2013/02/System_V_ABI.pdf

#### Objective-C

For objc instance method:
`rdi` saves the object
`rsi` saves the method selector name
`rdx` saves the first argument
`rcx` saves the second argument

Before jumping to `objc_autoreleaseReturnValue` to return, `rdi` saves the return
value.
...

## Memory address

```
0x10e4fcdd9 <+43>:  movq   %r14, %rdi
0x10e4fce33 <+133>: leaq   -0x1(%rbx), %rcx
0x10e4fce59 <+171>: movq   (%r13), %rax
0x10e4fce5d <+175>: movq   (%rax,%rdi,8), %rax
0x10e4fce25 <+119>: movq   0x8(%r14,%rbx), %rbx
0x10e4fce2d <+127>: movq   %r14, -0x40(%rbp)
0x10e4fce14 <+102>: callq  *0x1ba1876(%rip)          ; (void *)0x00007fff20311690: objc_retain
```


3.7.5 Specifying an Offset
The offset part of a memory address can be specified directly as a static value (called a displacement) or through an address computation made up of one or more of the following components:

Displacement — An 8-, 16-, or 32-bit value.
Base — The value in a general-purpose register.
Index — The value in a general-purpose register. [can't be ESP/RSP]
Scale factor — A value of 2, 4, or 8 that is multiplied by the index value.

In AT&T syntax, it's disp(base, index, scale) - constants go outside the parens.

```
base + (index * scale) + disp.
```

Ref: https://stackoverflow.com/a/27937263

## TODO

https://stackoverflow.com/questions/55623357/can-we-store-a-floating-point-in-a-regular-register
