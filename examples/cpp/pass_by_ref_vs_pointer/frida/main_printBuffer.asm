main`printBuffer:
    0x10074eff0 <+0>:  pushq  %rbp
    0x10074eff1 <+1>:  movq   %rsp, %rbp
    0x10074eff4 <+4>:  subq   $0x10, %rsp
    0x10074eff8 <+8>:  movq   %rdi, %rax
    0x10074effb <+11>: movq   0xffe(%rip), %rdi         ; (void *)0x00007ff8603044f0: std::__1::cout
    0x10074f002 <+18>: movq   %rax, -0x8(%rbp)
    0x10074f006 <+22>: leaq   0xf2d(%rip), %rsi         ; "Buffer len by pointer: "
    0x10074f00d <+29>: callq  0x10074fd7a               ; symbol stub for: std::__1::basic_ostream<char, std::__1::char_traits<char> >& std::__1::operator<<<std::__1::char_traits<char> >(std::__1::basic_ostream<char, std::__1::char_traits<char> >&, char const*)
    0x10074f012 <+34>: movq   %rax, -0x10(%rbp)
    0x10074f016 <+38>: movq   -0x8(%rbp), %rdi
    0x10074f01a <+42>: callq  0x10074eed0               ; Buffer::GetLen() const
    0x10074f01f <+47>: movq   -0x10(%rbp), %rdi
    0x10074f023 <+51>: movq   %rax, %rsi
    0x10074f026 <+54>: callq  0x10074fd5c               ; symbol stub for: std::__1::basic_ostream<char, std::__1::char_traits<char> >::operator<<(unsigned long)
    0x10074f02b <+59>: movq   %rax, %rdi
    0x10074f02e <+62>: movq   0xfd3(%rip), %rsi         ; (void *)0x000000010074efa0: std::__1::basic_ostream<char, std::__1::char_traits<char> >& std::__1::endl<char, std::__1::char_traits<char> >(std::__1::basic_ostream<char, std::__1::char_traits<char> >&)
    0x10074f035 <+69>: callq  0x10074ef80               ; std::__1::basic_ostream<char, std::__1::char_traits<char> >::operator<<(std::__1::basic_ostream<char, std::__1::char_traits<char> >& (*)(std::__1::basic_ostream<char, std::__1::char_traits<char> >&))
    0x10074f03a <+74>: addq   $0x10, %rsp
    0x10074f03e <+78>: popq   %rbp
    0x10074f03f <+79>: retq   

main`printBuffer:
    0x10074eef0 <+0>:  pushq  %rbp
    0x10074eef1 <+1>:  movq   %rsp, %rbp
    0x10074eef4 <+4>:  subq   $0x10, %rsp
    0x10074eef8 <+8>:  movq   %rdi, %rax
    0x10074eefb <+11>: movq   0x10fe(%rip), %rdi        ; (void *)0x00007ff8603044f0: std::__1::cout
    0x10074ef02 <+18>: movq   %rax, -0x8(%rbp)
    0x10074ef06 <+22>: leaq   0x1013(%rip), %rsi        ; "Buffer len by reference: "
    0x10074ef0d <+29>: callq  0x10074fd7a               ; symbol stub for: std::__1::basic_ostream<char, std::__1::char_traits<char> >& std::__1::operator<<<std::__1::char_traits<char> >(std::__1::basic_ostream<char, std::__1::char_traits<char> >&, char const*)
    0x10074ef12 <+34>: movq   %rax, -0x10(%rbp)
    0x10074ef16 <+38>: movq   -0x8(%rbp), %rdi
    0x10074ef1a <+42>: callq  0x10074eed0               ; Buffer::GetLen() const
    0x10074ef1f <+47>: movq   -0x10(%rbp), %rdi
    0x10074ef23 <+51>: movq   %rax, %rsi
    0x10074ef26 <+54>: callq  0x10074fd5c               ; symbol stub for: std::__1::basic_ostream<char, std::__1::char_traits<char> >::operator<<(unsigned long)
    0x10074ef2b <+59>: movq   %rax, %rdi
    0x10074ef2e <+62>: movq   0x10d3(%rip), %rsi        ; (void *)0x000000010074efa0: std::__1::basic_ostream<char, std::__1::char_traits<char> >& std::__1::endl<char, std::__1::char_traits<char> >(std::__1::basic_ostream<char, std::__1::char_traits<char> >&)
    0x10074ef35 <+69>: callq  0x10074ef80               ; std::__1::basic_ostream<char, std::__1::char_traits<char> >::operator<<(std::__1::basic_ostream<char, std::__1::char_traits<char> >& (*)(std::__1::basic_ostream<char, std::__1::char_traits<char> >&))
    0x10074ef3a <+74>: addq   $0x10, %rsp
    0x10074ef3e <+78>: popq   %rbp
    0x10074ef3f <+79>: retq   

