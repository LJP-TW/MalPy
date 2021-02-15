# MalPy

Idea from https://github.com/satwikkansal/wtfpython

> The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you just get back a reference to the existing object. So it should be possible to change the value of 1. I suspect the behavior of Python, in this case, is undefined. :-)

So I write a PoC ;)

```python
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
```

Output:
```
59
1
1
60
```

