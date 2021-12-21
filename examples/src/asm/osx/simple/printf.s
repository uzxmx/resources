.global _main

_main:
  pushq   %rbp
  movq    %rsp, %rbp
  subq    $0x10, %rsp
  movl    $0x0, -0x4(%rbp)
  leaq    .str(%rip), %rdi
  movb    $0x0, %al
  callq   _printf
  xorl    %ecx, %ecx
  movl    %eax, -0x8(%rbp)
  movl    %ecx, %eax
  addq    $0x10, %rsp
  popq    %rbp
  retq

.str: .asciz "Hello, world!\n"
