# This file demonstrates how to use OSX system calls.

.global _main

_main:
  pushq   %rbp
  movq    %rsp, %rbp
  subq    $0x10, %rsp

  leaq    .str(%rip), %rdi
  movq    $0x0, %rsi
  movq    $0x200003b, %rax # execve
  syscall

  movq    $0x0, %rdi
  callq   _sys_exit

  movq    $0x0, %rax
  addq    $0x10, %rsp
  popq    %rbp
  retq

_sys_exit:
  pushq   %rbp
  movq    %rsp, %rbp
  movq    $0x2000001, %rax # exit
  syscall
  popq    %rbp
  retq

.str: .asciz "/bin/sh"
