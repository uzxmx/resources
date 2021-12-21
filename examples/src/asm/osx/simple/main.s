# This file demonstrates how to use OSX system calls.

.global _main

_main:
  pushq   %rbp
  movq    %rsp, %rbp
  subq    $0x10, %rsp

  leaq    .msg(%rip), %rsi
  movq    $msglen, %rdx
  callq   _sys_write_stdout

  movq    $0x0, %rdi
  callq   _sys_exit

  movq    $0x0, %rax
  addq    $0x10, %rsp
  popq    %rbp
  retq

_sys_write_stdout:
  pushq   %rbp
  movq    %rsp, %rbp
  movq    $0x2000004, %rax # write
  movq    $0x1, %rdi # stdout
  syscall
  popq    %rbp
  retq

_sys_exit:
  pushq   %rbp
  movq    %rsp, %rbp
  movq    $0x2000001, %rax # exit
  syscall
  popq    %rbp
  retq

.msg: .ascii "Hello, world!\n"
msglen = . - .msg
