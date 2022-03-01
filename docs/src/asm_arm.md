# ASM for ARM

## Registers

0 - 30

## Width specifier

W (32 bits)
X (64 bits)

## Instructions

#### TBNZ

Test bit and branch if nonzero to a label at a PC-relative offset, without affecting the condition flags, and with a hint that this is not a subroutine call or return.

Ref: https://developer.arm.com/documentation/dui0802/a/A64-General-Instructions/TBNZ

#### CBZ and CBNZ

Compare and Branch on Zero, Compare and Branch on Non-Zero.

Ref: https://developer.arm.com/documentation/dui0489/i/arm-and-thumb-instructions/cbz-and-cbnz

#### ADRP

Address of 4KB page at a PC-relative offset.

Ref: https://developer.arm.com/documentation/dui0802/a/A64-General-Instructions/ADRP
