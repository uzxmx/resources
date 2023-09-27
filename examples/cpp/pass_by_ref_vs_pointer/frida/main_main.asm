main`main:
    0x10074f040 <+0>:  pushq  %rbp
    0x10074f041 <+1>:  movq   %rsp, %rbp
    0x10074f044 <+4>:  subq   $0x20, %rsp
    0x10074f048 <+8>:  movl   $0x0, -0x4(%rbp)
    0x10074f04f <+15>: callq  0x10074f0a0               ; std::__1::__get_nullptr_t()
    0x10074f054 <+20>: movq   %rax, -0x20(%rbp)
    0x10074f058 <+24>: leaq   -0x20(%rbp), %rdi
    0x10074f05c <+28>: callq  0x10074f0d0               ; std::__1::nullptr_t::operator void*<void>() const
    0x10074f061 <+33>: movq   %rax, %rsi
    0x10074f064 <+36>: leaq   -0x18(%rbp), %rdi
    0x10074f068 <+40>: movl   $0x100, %edx              ; imm = 0x100 
    0x10074f06d <+45>: callq  0x10074ee80               ; Buffer::Buffer(void*, unsigned long)
    0x10074f072 <+50>: leaq   -0x18(%rbp), %rdi
    0x10074f076 <+54>: callq  0x10074eef0               ; printbuffer(buffer&)
    0x10074f07b <+59>: leaq   -0x18(%rbp), %rdi
    0x10074f07f <+63>: callq  0x10074eff0               ; printBuffer(Buffer*)
    0x10074f084 <+68>: movl   $0x2, %edi
    0x10074f089 <+73>: callq  0x10074fd98               ; symbol stub for: sleep
    0x10074f08e <+78>: jmp    0x10074f072               ; <+50>
    0x10074f093 <+83>: nopw   %cs:(%rax,%rax)
    0x10074f09d <+93>: nopl   (%rax)
