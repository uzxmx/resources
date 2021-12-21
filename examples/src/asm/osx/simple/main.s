.global _main

_main:
  pushq   %rbp
  movq    %rsp, %rbp
  subq    $0x10, %rsp

  movq    $0x2000004, %rax # write
  movq    $0x1, %rdi # stdout
  leaq    .msg(%rip), %rsi
  movq    $msglen, %rdx
  syscall

  movq    $0x2000001, %rax # exit
  movq    $0x0, %rdi
  syscall

  movl    $0x1, %eax
  addq    $0x10, %rsp
  popq    %rbp
  retq

.msg: .ascii "Hello, world!\n"
msglen = . - .msg
