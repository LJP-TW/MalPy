#!/usr/bin/env python3.8
import struct

def magic(offset, /):
    offset += 0x18
    with open("/proc/self/mem", 'wb') as mem:
        mem.seek(offset)
        mem.write(b'\x01')
    return

a = 0x3b
print(a)
magic(id(a))
print(a)
print(0x3b)
print(0x3b + 1)
