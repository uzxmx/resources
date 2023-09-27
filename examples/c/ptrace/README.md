
db $$ @@=`axt sym.imp.sysctl~CALL~call[1]`

pd @ 0x10a667e28

dr

px @ rdx
px @ 0x7ff7b589ba58

dcu `axt sym.imp.sysctl~CALL~call[1]`

dcu rip+5

pd @ 0x10b397e28
s `axt sym.imp.sysctl~CALL~call[1]`
pd 5
wa nop
"wa nop;nop;nop;nop;nop"
"wa xor rax, rax;nop;nop"
wa* xor rax, rax

s `axt sym.imp.sysctl~CALL~call[1]`
"wa xor rax, rax;nop;nop"
