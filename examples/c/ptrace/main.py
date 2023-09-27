#!/usr/bin/env python

import r2pipe

r2 = r2pipe.open("main", flags=['-w', '-d'])
r2.cmd('aaaa')
r2.cmd('db $$ @@=`axt sym.imp.sysctl~CALL~call[1]`')
print(r2.cmd('db'))
r2.cmd('dc')
r2.cmd('dc')
print(r2.cmd('px @ rdx + 0x20'))
print(r2.cmd('pd @ rip'))
r2.cmd('dsf')
print(r2.cmd('pd @ rip'))
print(r2.cmd('px @ rdx + 0x20'))
# print(r2.cmd("afl"))
# print(r2.cmdj("aflj"))            # evaluates JSONs and returns an object
# print(r2.cmdj("ij").core.format)  # shows file format
r2.quit()
