# This file demonstrates `cmp` instructions.

.global _main

_main:
  pushq   %rbp
  movq    %rsp, %rbp
  subq    $0x10, %rsp

  # Compare r14 with a local variable in the stack.
  movq   $0x2, %r14
  movq   $0x1, (%rbp)
  cmpq   %r14, (%rbp)
  jae    _exit

  leaq    .msg1(%rip), %rsi
  movq    $msg1_len, %rdx
  callq  _sys_write_stdout

_exit:
  movl    $0x0, %eax
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

.msg1: .ascii "Compare 2 with 1, not jumped.\n"
msg1_len = . - .msg1
